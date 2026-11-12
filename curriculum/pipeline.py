"""Runs the stages end to end and writes curriculum.json, curriculum.md and trace.json."""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path

from . import discover, html, render, youtube
from .assess import assess_all
from .dedup import clusters
from .llm import Ledger
from .models import Assessment, Candidate, Curriculum, Dropped, Evidence, Persona, Pick, PlanOut
from .plan import make_plan
from .prompts import load
from .selection import counted_minutes, select

DEFAULT_MODELS = {
    "plan": os.getenv("PLAN_MODEL", "anthropic/claude-sonnet-5.5"),
    "assess": os.getenv("ASSESS_MODEL", "anthropic/claude-haiku-5.5"),
    "select": os.getenv("SELECT_MODEL", "anthropic/claude-sonnet-5.5"),
}
FIXTURES = Path("fixtures")


def load_persona(path: str | Path) -> Persona:
    return Persona.model_validate_json(Path(path).read_text())


def _fixture_path(persona_id: str) -> Path:
    return FIXTURES / f"{persona_id}.json"


def run(persona: Persona, *, models: dict | None = None, use_transcripts: bool = True, offline: bool = False,
        out_dir: Path | None = None, mode: str = "agent", save_fixture: bool = True,
        progress: "callable | None" = None) -> tuple[Curriculum, dict]:
    models = {**DEFAULT_MODELS, **(models or {})}
    ledger = Ledger()
    timings: dict[str, float] = {}
    t0 = time.time()

    def lap(name: str, since: float) -> float:
        timings[name] = round(time.time() - since, 2)
        if progress:
            progress(name)  # a stage just finished, for the live showcase
        return time.time()

    fixture = json.loads(_fixture_path(persona.persona_id).read_text()) if offline else None
    t = time.time()
    profile = hashlib.sha1(json.dumps([persona.goal, persona.time_budget_minutes, persona.user_context.model_dump()],
                                      sort_keys=True).encode()).hexdigest()[:12]
    same_profile = bool(fixture) and fixture.get("profile") == profile
    if fixture:
        if same_profile:
            plan = PlanOut.model_validate(fixture["plan"])
        else:  # the learner profile changed since the pool was collected: keep the pool, redo the plan
            plan = make_plan(persona, ledger, models["plan"])
            t = lap("plan", t)
        pool_list = [Candidate.model_validate(c) for c in fixture["pool"]]
        pre_dropped = [Dropped.model_validate(d) for d in fixture["dropped"]]
        t = lap("load_fixture", t)
    else:
        plan = make_plan(persona, ledger, models["plan"])
        t = lap("plan", t)
        pool_list, pre_dropped = discover.discover(persona, plan)
        t = lap("discover", t)
        pool_list, lang_dropped = discover.hydrate(pool_list, plan, use_transcripts=True)
        pre_dropped += lang_dropped
        t = lap("hydrate", t)

    # Saved assessments are reused only if the plan they were scored against, the model and the assess
    # prompt are all unchanged (relevance scores refer to the plan's sub-topic ids). An --offline run
    # exists to REPRODUCE the committed fixtures, so it reuses them as-is instead of silently
    # re-assessing (and rewriting them) because the configured model differs from the one that built them.
    assess_prompt = hashlib.sha1(load("assess").encode()).hexdigest()[:12]
    reuse = same_profile and use_transcripts and (offline or (fixture.get("assess_model") == models["assess"]
                                                              and fixture.get("assess_prompt") == assess_prompt))
    if reuse:
        assessments = {k: Assessment.model_validate(v) for k, v in fixture["assessments"].items()}
    else:
        assessments = assess_all(pool_list, persona, plan, ledger, models["assess"], use_transcripts=use_transcripts)
    t = lap("assess", t)

    if use_transcripts and save_fixture and not reuse:  # offline re-assessments refresh the fixture too
        FIXTURES.mkdir(exist_ok=True)
        _fixture_path(persona.persona_id).write_text(json.dumps({
            "persona_id": persona.persona_id,
            "profile": profile,
            "plan": plan.model_dump(),
            "pool": [c.model_dump() for c in pool_list],
            "dropped": [d.model_dump() for d in pre_dropped],
            "assess_model": models["assess"],
            "assess_prompt": assess_prompt,
            "assessments": {k: v.model_dump() for k, v in assessments.items()},
        }, ensure_ascii=False, indent=1))

    pool = {c.video_id: c for c in pool_list}
    dup = clusters(assessments)
    t = lap("dedup", t)
    sel, fixes = select(persona, plan, pool, assessments, dup, ledger, models["select"])
    t = lap("select", t)

    cur = assemble(persona, plan, pool, assessments, sel, pre_dropped, models, ledger.total_cost, round(time.time() - t0, 1), mode)
    trace = {
        "persona": persona.model_dump(),
        "mode": mode,
        "models": models,
        "offline": offline,
        "use_transcripts": use_transcripts,
        "timings_s": timings,
        "cost_by_stage": ledger.by_stage(),
        "calls": [c.__dict__ for c in ledger.calls],
        "plan": plan.model_dump(),
        "pool": [{"video_id": c.video_id, "title": c.title, "channel": c.channel, "minutes": c.minutes,
                  "views": c.view_count, "found_by": c.found_by, "transcript_lang": c.transcript_lang,
                  "transcript_generated": c.transcript_generated, "transcript_error": c.transcript_error}
                 for c in pool_list],
        "assessments": {k: v.model_dump() for k, v in assessments.items()},
        "dup_clusters": dup,
        "selector_raw": sel.model_dump(),
        "fixes": fixes,
    }
    if out_dir:
        save(cur, trace, out_dir)
    return cur, trace


def assemble(persona: Persona, plan: PlanOut, pool: dict[str, Candidate], assessments: dict[str, Assessment], sel,
             pre_dropped: list[Dropped], models: dict, cost: float, latency: float, mode: str) -> Curriculum:
    picks = []
    for i, p in enumerate(sel.picks, 1):
        c, a = pool[p.video_id], assessments[p.video_id]
        quotes = {q.id: q for q in a.quotes}
        src = "transcript" if a.evidence_source == "transcript" else "chapters/description"
        evidence = [Evidence(quote_id=q, t=youtube.ts(quotes[q].t), quote=quotes[q].text, source=src) for q in p.evidence_quote_ids if q in quotes]
        picks.append(Pick(
            rank=i, video_id=c.video_id, title=c.title, channel=c.channel, url=c.url, duration_min=c.minutes,
            minutes_counted=counted_minutes(p, c),
            watch_from=youtube.ts(p.watch_from_s) if p.watch_from_s is not None else None,
            watch_until=youtube.ts(p.watch_until_s) if p.watch_until_s is not None else None,
            covers=p.covers, reason=p.reason, evidence=evidence, confidence=round(p.confidence, 2),
            confidence_note=p.confidence_note, level=a.level, format=a.format,
        ))
    dropped = list(pre_dropped) + [
        Dropped(video_id=d.video_id, title=pool[d.video_id].title, stage="select", reason=d.reason) for d in sel.dropped
    ]
    warnings = list(sel.warnings)
    if not plan.feasible and plan.feasibility_note and not any("feasib" in w.lower() for w in warnings):
        warnings.insert(0, plan.feasibility_note)
    return Curriculum(
        persona_id=persona.persona_id, goal=persona.goal, budget_minutes=persona.time_budget_minutes,
        total_minutes=round(sum(p.minutes_counted for p in picks), 1), interpretation=plan.interpretation,
        assumptions=plan.assumptions, feasible=plan.feasible, feasibility_note=plan.feasibility_note,
        sub_topics=plan.sub_topics, picks=picks, dropped=dropped, near_duplicates=sel.near_duplicates,
        warnings=warnings, pool_size=len(pool), models=models, cost_usd=cost, latency_s=latency, mode=mode,
    )


def save(cur: Curriculum, trace: dict, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "curriculum.json").write_text(cur.model_dump_json(indent=2))
    (out_dir / "curriculum.md").write_text(render.markdown(cur))
    if cur.mode in ("agent", "agent_loop"):
        (out_dir / "curriculum.html").write_text(html.curriculum_page(cur, out_dir.name, html.extras_for(cur, out_dir)))
    (out_dir / "trace.json").write_text(json.dumps(trace, indent=1, ensure_ascii=False, default=str))
    from . import store  # optional MongoDB mirror; a no-op unless MONGODB_URI is set
    store.save_curriculum(cur, trace)
