"""Stage 6: the stronger model picks, orders and justifies videos from the assessed pool.

The code, not the model, owns the arithmetic: it computes minutes, rejects unknown ids and
unverified quote ids, and if the budget is blown asks the model once to fix it before trimming.
It also owns the red-flag rule: a flagged video may only be picked when nothing unflagged teaches
the same sub-topic (with transcripts, the selector otherwise filled slots with flagged videos)."""

from __future__ import annotations

import json

from . import youtube
from .llm import Ledger, chat_json
from .models import Assessment, Candidate, Persona, PickOut, PlanOut, SelectOut
from .prompts import load, persona_block


def card(c: Candidate, a: Assessment) -> dict:
    quotes = [{"id": q.id, "t": youtube.ts(q.t), "text": q.text} for q in a.quotes if q.id in a.verified_quote_ids]
    return {
        "video_id": c.video_id,
        "title": c.title,
        "channel": c.channel,
        "minutes": c.minutes,
        "evidence_source": a.evidence_source,
        "transcript": ("auto-generated" if c.transcript_generated else "manual") if c.evidence_kind == "transcript" else "none (assessed from chapters/description only: weaker evidence)",
        "uploaded": c.upload_date,
        "summary": a.summary,
        "level": a.level,
        "format": a.format,
        "project_built": a.project_built or None,
        "topics": a.topics_covered,
        "tools": a.tools_and_versions,
        "red_flags": a.red_flags,
        "relevance": {r.sub_topic_id: r.score for r in a.relevance},
        "segments": [f"{youtube.ts(s.start_s)}-{youtube.ts(s.end_s)} {s.topic}" for s in a.segments],
        "verified_quotes": quotes,
    }


# Flags that make a video wrong for any learner, whatever their goal — these the code enforces.
# Learner-relative flags (surface_intro, too_basic_for_learner, pure_theory, outdated_tooling) are left
# to the selector, which reads the learner's constraints: the SAME flag is disqualifying for one learner
# and desirable for another (pure_theory is wrong for "no lectures" but right for "I want the math
# intuition"; surface_intro is wrong for an expert but right for "the mistakes beginners make"). Enforcing
# those in code blocked content learners explicitly asked for (career's theory, sourdough's gotchas).
BLOCKING_FLAGS = {"off_topic", "wrong_language", "clickbait", "vlog", "equipment_review"}


def flag_conflicts(out: SelectOut, pool: dict[str, Candidate], assessments: dict[str, Assessment]) -> list[tuple[PickOut, list[str], list[str]]]:
    """Picks with a blocking flag, each with the unpicked, unflagged candidates that teach (score >= 2)
    one of the sub-topics it covers. An empty alternative list means the flagged pick is the only option."""
    picked = {p.video_id for p in out.picks}
    res = []
    for p in out.picks:
        a = assessments.get(p.video_id)
        flags = sorted(set(a.red_flags) & BLOCKING_FLAGS) if a else []
        if not flags:
            continue
        alts = [v for v, a in assessments.items()
                if v in pool and v not in picked and not set(a.red_flags) & BLOCKING_FLAGS
                and any(r.sub_topic_id in p.covers and r.score >= 2 for r in a.relevance)]
        res.append((p, flags, alts))
    return res


def counted_minutes(p: PickOut, c: Candidate) -> float:
    if p.watch_from_s is not None or p.watch_until_s is not None:
        a = max(0, p.watch_from_s or 0)
        b = min(c.duration_s, p.watch_until_s or c.duration_s)
        if b > a:
            return round((b - a) / 60, 1)
    return c.minutes


def select(persona: Persona, plan: PlanOut, pool: dict[str, Candidate], assessments: dict[str, Assessment],
           dup_clusters: list[dict], ledger: Ledger, model: str) -> tuple[SelectOut, list[str]]:
    cards = [card(pool[v], assessments[v]) for v in pool if v in assessments]
    subs = [{"id": s.id, "title": s.title, "prereqs": s.prereqs, "minutes": round(s.minutes_share * persona.time_budget_minutes)} for s in plan.sub_topics]
    user = (
        f"LEARNER\n{persona_block(persona)}\n\n"
        f"PLAN\nInterpretation: {plan.interpretation}\nAssumptions: {plan.assumptions or '-'}\n"
        f"Feasible: {plan.feasible} {plan.feasibility_note}\nSkip (already known): {plan.skip_topics}\n"
        f"Sub-topics: {json.dumps(subs)}\n\n"
        f"NEAR-DUPLICATE CLUSTERS (pick at most one per cluster)\n{json.dumps(dup_clusters) if dup_clusters else 'none'}\n\n"
        f"CANDIDATES ({len(cards)})\n" + "\n".join(json.dumps(c, ensure_ascii=False) for c in cards)
    )
    out = chat_json(model, load("select"), user, SelectOut, stage="select", ledger=ledger, max_tokens=16000)
    fixes: list[str] = []
    out = _sanitize(out, pool, assessments, fixes)

    conflicts = [c for c in flag_conflicts(out, pool, assessments) if c[2]]
    if conflicts:
        msg = "These picks have red flags although unflagged candidates teach the same sub-topics:\n" + "\n".join(
            f"- {p.video_id} {flags}: alternatives {alts[:5]}" for p, flags, alts in conflicts
        ) + (f"\nYour picks currently use {sum(counted_minutes(p, pool[p.video_id]) for p in out.picks):.0f} of "
             f"{persona.time_budget_minutes} minutes. Return the full JSON again, replacing each flagged pick with unflagged "
             "candidates (respect the near-duplicate clusters), and keep the total at 75-100% of the budget: when a "
             "replacement is shorter, add further unflagged candidates or widen watch ranges rather than leaving time unused.")
        out = chat_json(model, load("select"), user + "\n\n" + msg, SelectOut, stage="select_flags", ledger=ledger, max_tokens=16000)
        out = _sanitize(out, pool, assessments, fixes)
        fixes.append(f"selector picked {len(conflicts)} flagged video(s) despite unflagged alternatives and was asked once to replace them")
    # Still flagged after the retry: drop it only if the curriculum stays usable (>= 75% of the budget).
    # Removing a long flagged build left 53 of 360 minutes in testing, which is worse for the learner
    # than keeping it with a visible warning.
    for p, flags, alts in flag_conflicts(out, pool, assessments):
        total = sum(counted_minutes(x, pool[x.video_id]) for x in out.picks)
        if alts and total - counted_minutes(p, pool[p.video_id]) >= 0.75 * persona.time_budget_minutes:
            out.picks.remove(p)
            fixes.append(f"removed {p.video_id} (red flags {flags}; unflagged alternatives existed)")
        else:
            why = "only partial alternatives exist" if alts else f"it is the only candidate covering {', '.join(p.covers)}"
            out.warnings.append(f"{pool[p.video_id].title} ({p.video_id}) is flagged {', '.join(flags)} but kept because {why}; treat it as a stopgap.")
            fixes.append(f"kept flagged {p.video_id} ({flags}) with a learner-facing warning")

    total = sum(counted_minutes(p, pool[p.video_id]) for p in out.picks)
    if total > persona.time_budget_minutes:
        msg = (f"Your picks add up to {total:.0f} minutes but the budget is {persona.time_budget_minutes}. "
               "Return the full JSON again with picks that fit (drop or trim the weakest; use watch ranges where sensible).")
        out = chat_json(model, load("select"), user + "\n\n" + msg, SelectOut, stage="select_fix", ledger=ledger, max_tokens=16000)
        out = _sanitize(out, pool, assessments, fixes)
        fixes.append(f"selector exceeded the budget ({total:.0f} min) and was asked once to fix it")
        total = sum(counted_minutes(p, pool[p.video_id]) for p in out.picks)
        while total > persona.time_budget_minutes and out.picks:
            weakest = min(out.picks, key=lambda p: p.confidence)
            out.picks.remove(weakest)
            fixes.append(f"removed {weakest.video_id} (lowest confidence) to fit the budget")
            total = sum(counted_minutes(p, pool[p.video_id]) for p in out.picks)
    return out, fixes


def _range(p: PickOut, c: Candidate) -> tuple[int, int] | None:
    if p.watch_from_s is None and p.watch_until_s is None:
        return None
    return max(0, p.watch_from_s or 0), min(c.duration_s, p.watch_until_s or c.duration_s)


def _sanitize(out: SelectOut, pool: dict[str, Candidate], assessments: dict[str, Assessment], fixes: list[str]) -> SelectOut:
    """Drop unknown ids and unverified quote ids. A long course may appear more than once as separate
    slices (e.g. its intro early, its CNN chapters later), but only with non-overlapping watch ranges;
    any other repeat is dropped, so no minute is counted twice."""
    seen: dict[str, list[tuple[int, int] | None]] = {}
    picks = []
    for p in out.picks:
        if p.video_id not in pool:
            fixes.append(f"dropped pick {p.video_id}: not in the candidate pool")
            continue
        if p.video_id not in assessments:
            fixes.append(f"dropped pick {p.video_id}: no assessment on file")
            continue
        r = _range(p, pool[p.video_id])
        prev = seen.get(p.video_id)
        if prev is not None and (r is None or any(x is None or (r[0] < x[1] and x[0] < r[1]) for x in prev)):
            fixes.append(f"dropped pick {p.video_id}: repeats a video without a separate, non-overlapping watch range")
            continue
        seen.setdefault(p.video_id, []).append(r)
        ok = set(assessments[p.video_id].verified_quote_ids)
        bad = [q for q in p.evidence_quote_ids if q not in ok]
        if bad:
            fixes.append(f"{p.video_id}: removed unverified quote ids {bad}")
            p.evidence_quote_ids = [q for q in p.evidence_quote_ids if q in ok]
        p.confidence = min(1.0, max(0.0, p.confidence))
        picks.append(p)
    out.picks = picks
    out.dropped = [d for d in out.dropped if d.video_id in pool and d.video_id not in seen]
    return out
