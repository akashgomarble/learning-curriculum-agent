"""Agent-loop variant of the curriculum builder.

Same task as the fixed pipeline, but the model drives it with tools instead of fixed stages: it plans,
searches, reads videos and chooses through a manual tool-use loop (mirroring inference-service's hand-rolled
loop — bounded turns, read-only tools in parallel, a terminal `submit_curriculum` tool as the stop signal).

Deliberately, it runs over the SAME cached candidate pool and per-video assessments the fixed pipeline used,
and the submitted picks are assembled and verified by the SAME code (`pipeline.assemble`, `selection._sanitize`).
So an eval of `agent` vs `agent_loop` isolates the control flow — fixed stages vs a model-driven loop — not the
data or the output checks. What differs is who decides: the code, or the model turn by turn.
"""

from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path

from .llm import Ledger, chat_tools
from .models import (Assessment, Candidate, Curriculum, DroppedOut, Persona, PickOut, PlanOut, SelectOut, SubTopic)
from .pipeline import DEFAULT_MODELS, _fixture_path, assemble, save
from .prompts import load, persona_block
from .selection import _sanitize, counted_minutes

MAX_TURNS = 40

TOOLS = [
    {"type": "function", "function": {
        "name": "search_youtube",
        "description": "Search the candidate pool for this learner. Returns matching videos with id, title, channel, "
                       "duration, upload date and view count. Call it several times with different queries (one per sub-topic, plus a "
                       "project-style query that mirrors the goal). View count is popularity, NOT fit.",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string", "description": "A YouTube-style search query, in the videos' language."}},
            "required": ["query"], "additionalProperties": False}}},
    {"type": "function", "function": {
        "name": "read_video",
        "description": "Read what a video actually teaches: a content summary, level, format, red flags, topics covered, "
                       "and verbatim quotes each with an id (q1, q2, …) and timestamp. The ONLY way to learn a video's "
                       "content. You must read a video before you can pick it, and may only cite quote ids it returns.",
        "parameters": {"type": "object", "properties": {
            "video_id": {"type": "string", "description": "A video id from search_youtube."}},
            "required": ["video_id"], "additionalProperties": False}}},
    {"type": "function", "function": {
        "name": "submit_curriculum",
        "description": "Finish and return the curriculum. Call exactly once, when the plan is covered. Picks must be videos "
                       "you have read, in watch order, each grounded in verified quote ids from that video.",
        "parameters": {"type": "object", "properties": {
            "interpretation": {"type": "string", "description": "One sentence: what success looks like for this learner."},
            "assumptions": {"type": "array", "items": {"type": "string"}, "description": "Assumptions for an ambiguous goal; [] if none."},
            "feasible": {"type": "boolean", "description": "Can the goal realistically be met within the budget?"},
            "feasibility_note": {"type": "string", "description": "If not feasible, what part is realistic; else ''."},
            "sub_topics": {"type": "array", "description": "Ordered sub-topics, prerequisites first.", "items": {
                "type": "object", "properties": {
                    "id": {"type": "string"}, "title": {"type": "string"}, "why": {"type": "string"},
                    "prereqs": {"type": "array", "items": {"type": "string"}},
                    "minutes_share": {"type": "number"}},
                "required": ["id", "title", "why", "prereqs", "minutes_share"], "additionalProperties": False}},
            "picks": {"type": "array", "description": "Videos in watch order.", "items": {
                "type": "object", "properties": {
                    "video_id": {"type": "string"},
                    "covers": {"type": "array", "items": {"type": "string"}, "description": "sub-topic ids this pick covers"},
                    "reason": {"type": "string", "description": "1-3 sentences: why this video for this learner, grounded in what it teaches"},
                    "evidence_quote_ids": {"type": "array", "items": {"type": "string"}, "description": "verified quote ids from read_video backing the reason"},
                    "watch_from_s": {"type": ["integer", "null"], "description": "start second if only part is needed, else null"},
                    "watch_until_s": {"type": ["integer", "null"], "description": "end second if only part is needed, else null"},
                    "confidence": {"type": "number", "description": "0-1"},
                    "confidence_note": {"type": "string"}},
                "required": ["video_id", "covers", "reason", "evidence_quote_ids", "watch_from_s", "watch_until_s", "confidence", "confidence_note"],
                "additionalProperties": False}},
            "warnings": {"type": "array", "items": {"type": "string"}, "description": "gaps, infeasibility, dedup notes, unused budget"},
            "dropped": {"type": "array", "description": "strong candidates you read but did NOT pick, each with a content-based reason", "items": {
                "type": "object", "properties": {"video_id": {"type": "string"}, "reason": {"type": "string"}},
                "required": ["video_id", "reason"], "additionalProperties": False}}},
            "required": ["interpretation", "assumptions", "feasible", "feasibility_note", "sub_topics", "picks", "warnings"],
            "additionalProperties": False}}},
]


def _tokens(s: str) -> set[str]:
    return {w for w in re.split(r"[^a-z0-9]+", s.lower()) if len(w) > 2}


def _search(pool: dict[str, Candidate], query: str, k: int = 8) -> dict:
    """Score pool candidates by token overlap with the query (title + the queries that surfaced them)."""
    q = _tokens(query)
    scored = []
    for c in pool.values():
        hay = _tokens(c.title + " " + c.channel + " " + " ".join(c.found_by))
        scored.append((len(q & hay), c))
    scored.sort(key=lambda x: (-x[0], -(x[1].view_count or 0)))
    top = [c for s, c in scored if s > 0][:k] or [c for _, c in scored[:k]]
    return {"success": True, "query": query, "results": [
        {"video_id": c.video_id, "title": c.title, "channel": c.channel, "minutes": c.minutes,
         "uploaded": c.upload_date, "views": c.view_count} for c in top]}


def _read(assessments: dict[str, Assessment], pool: dict[str, Candidate], vid: str) -> dict:
    a, c = assessments.get(vid), pool.get(vid)
    if not a or not c:
        return {"success": False, "error": f"no such video {vid}; use an id from search_youtube"}
    quotes = [{"id": q.id, "t": round(q.t), "text": q.text} for q in a.quotes if q.id in a.verified_quote_ids]
    return {"success": True, "video_id": vid, "title": c.title, "minutes": c.minutes, "uploaded": c.upload_date,
            "evidence": "transcript" if a.evidence_source == "transcript" else "chapters/description only (weaker)",
            "summary": a.summary, "level": a.level, "format": a.format, "red_flags": a.red_flags,
            "topics_covered": a.topics_covered, "project_built": a.project_built or None, "quotes": quotes}


def _int(x):
    try:
        return int(x) if x is not None else None
    except (TypeError, ValueError):
        return None


def _counted(p: dict, c: Candidate) -> float:
    """Minutes a pick counts, from a raw tool-arg dict (robust to a string/missing watch range)."""
    wf, wu = _int(p.get("watch_from_s")), _int(p.get("watch_until_s"))
    if wf is not None or wu is not None:
        a, b = max(0, wf or 0), min(c.duration_s, wu if wu is not None else c.duration_s)
        if b > a:
            return round((b - a) / 60, 1)
    return c.minutes


def _validate(args: dict, pool: dict, assessments: dict, read_ids: set, budget: int) -> list[str]:
    errs = []
    total = 0.0
    for p in args.get("picks", []):
        vid = p.get("video_id")
        if vid not in pool:
            errs.append(f"pick {vid}: not a real video id")
            continue
        if vid not in read_ids:
            errs.append(f"pick {vid}: you must read_video it before picking it")
        total += _counted(p, pool[vid])
    if not args.get("picks"):
        errs.append("no picks: a curriculum needs at least one video")
    if total > budget + 0.5:
        errs.append(f"picks total {total:.0f} min but the budget is {budget}; trim or use watch ranges")
    return errs


def _assistant_msg(msg) -> dict:
    out = {"role": "assistant", "content": msg.content or ""}
    if msg.tool_calls:
        out["tool_calls"] = [{"id": tc.id, "type": "function",
                              "function": {"name": tc.function.name, "arguments": tc.function.arguments}}
                             for tc in msg.tool_calls]
    return out


def _ensure_pool(persona: Persona, ledger: Ledger) -> tuple[PlanOut, dict, dict]:
    """The candidate pool + per-video assessments: from the saved fixture when one exists (the cached
    data the fixed pipeline used, for a fair comparison), or built live via the pipeline's discovery
    stages for a brand-new chat goal that has no fixture yet."""
    fp = _fixture_path(persona.persona_id)
    if fp.exists():
        fx = json.loads(fp.read_text())
        return (PlanOut.model_validate(fx["plan"]),
                {c["video_id"]: Candidate.model_validate(c) for c in fx["pool"]},
                {k: Assessment.model_validate(v) for k, v in fx["assessments"].items()})
    from . import discover as _disc  # live discovery for a new goal (plan → search → hydrate → assess)
    from .assess import assess_all
    from .plan import make_plan
    plan = make_plan(persona, ledger, os.getenv("PLAN_MODEL") or DEFAULT_MODELS["plan"])
    pool_list, _ = _disc.discover(persona, plan)
    pool_list, _ = _disc.hydrate(pool_list, plan, use_transcripts=True)
    assessments = assess_all(pool_list, persona, plan, ledger, os.getenv("ASSESS_MODEL") or DEFAULT_MODELS["assess"])
    return plan, {c.video_id: c for c in pool_list}, assessments


def run_agent_loop(persona: Persona, *, model: str | None = None, out_dir: Path | None = None,
                   max_turns: int = MAX_TURNS, on_event=None) -> tuple[Curriculum, dict]:
    model = model or os.getenv("SELECT_MODEL") or DEFAULT_MODELS["select"]
    emit = on_event or (lambda e: None)  # live chat stream; no-op for the CLI
    ledger = Ledger()
    t0 = time.time()
    emit({"kind": "status", "text": "Gathering candidate videos…"})
    base_plan, pool, assessments = _ensure_pool(persona, ledger)
    emit({"kind": "status", "text": f"Have {len(pool)} candidates. Planning and choosing…"})

    messages = [{"role": "system", "content": load("agent_loop")},
                {"role": "user", "content": persona_block(persona)}]
    read_ids: set[str] = set()
    tool_log: list[dict] = []
    submission = None
    turns = 0

    on_token = (lambda d: emit({"kind": "token", "text": d})) if on_event else None  # stream narration in the chat UI
    for turn in range(max_turns):
        turns = turn + 1
        force = turn == max_turns - 1  # last turn: force a submission and accept it even if imperfect
        try:
            msg = chat_tools(model, messages, TOOLS, stage="agent_loop", ledger=ledger, max_tokens=8000, on_token=on_token,
                             tool_choice=({"type": "function", "function": {"name": "submit_curriculum"}} if force else "auto"))
        except Exception as ex:  # budget cap, provider error, forced-tool-choice unsupported: stop and finalise
            tool_log.append({"turn": turn, "tool": "error", "arg": f"{type(ex).__name__}: {str(ex)[:80]}", "ok": False})
            break
        messages.append(_assistant_msg(msg))
        calls = msg.tool_calls or []
        if not calls:
            messages.append({"role": "user", "content": "Continue with a tool, or call submit_curriculum to finish."})
            continue
        done = False
        for tc in calls:
            name = tc.function.name
            try:
                args = json.loads(tc.function.arguments or "{}")
            except json.JSONDecodeError:
                args = {}
            if name == "search_youtube":
                result = _search(pool, args.get("query", ""))
                emit({"kind": "search", "query": args.get("query", ""), "n": len(result.get("results", []))})
            elif name == "read_video":
                vid = args.get("video_id", "")
                if vid in pool:
                    read_ids.add(vid)
                result = _read(assessments, pool, vid)
                emit({"kind": "read", "video_id": vid, "title": result.get("title", vid), "level": result.get("level")})
            elif name == "submit_curriculum":
                errs = _validate(args, pool, assessments, read_ids, persona.time_budget_minutes)
                if errs and not force:
                    result = {"success": False, "errors": errs, "message": "Fix these and call submit_curriculum again."}
                    emit({"kind": "retry", "errors": errs})
                else:  # accept; on the forced last turn take it with its issues (sanitize + trim clean it up)
                    submission, done = args, True
                    result = {"success": True, "message": "Curriculum accepted." + (f" (forced, issues: {errs})" if errs else "")}
                    emit({"kind": "submit", "n_picks": len(args.get("picks", []))})
            else:
                result = {"success": False, "error": f"unknown tool {name}"}
            tool_log.append({"turn": turn, "tool": name, "arg": args.get("query") or args.get("video_id") or "submit",
                             "ok": result.get("success")})
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": json.dumps(result)[:7000]})
        if done:
            break

    return _finalize(persona, submission, base_plan, pool, assessments, model, ledger, t0,
                     tool_log, turns, read_ids, messages, out_dir, emit)


def _finalize(persona, submission, base_plan, pool, assessments, model, ledger, t0,
              tool_log, turns, read_ids, messages, out_dir, emit):
    """Turn a (possibly imperfect) submission into a verified Curriculum, save it + the conversation, and
    emit the final event. Shared by the first build and any follow-up revision, so both go through the
    same validation/assembly as the fixed pipeline."""
    if submission is None:  # never produced a valid submission
        submission = {"interpretation": base_plan.interpretation, "assumptions": [], "feasible": base_plan.feasible,
                      "feasibility_note": base_plan.feasibility_note, "sub_topics": [s.model_dump() for s in base_plan.sub_topics],
                      "picks": [], "warnings": ["The agent loop did not produce a valid curriculum within the turn budget."]}

    def _subtopic(s: dict):
        try:
            return SubTopic.model_validate({"id": s.get("id", ""), "title": s.get("title", ""), "why": s.get("why", ""),
                                            "prereqs": s.get("prereqs", []), "minutes_share": s.get("minutes_share", 0.0)})
        except Exception:
            return None

    def _pick(p: dict):
        try:
            return PickOut.model_validate({"video_id": p.get("video_id"), "covers": p.get("covers", []),
                                           "reason": p.get("reason", ""), "evidence_quote_ids": p.get("evidence_quote_ids", []),
                                           "watch_from_s": _int(p.get("watch_from_s")), "watch_until_s": _int(p.get("watch_until_s")),
                                           "confidence": p.get("confidence", 0.5), "confidence_note": p.get("confidence_note", "")})
        except Exception:
            return None

    sub_topics = [s for s in (_subtopic(x) for x in submission.get("sub_topics", [])) if s] or base_plan.sub_topics
    plan = PlanOut(interpretation=submission.get("interpretation", base_plan.interpretation), assumptions=submission.get("assumptions", []),
                   feasible=submission.get("feasible", True), feasibility_note=submission.get("feasibility_note", ""),
                   preferred_language=base_plan.preferred_language, learner_level=base_plan.learner_level,
                   sub_topics=sub_topics, search_queries=[], title_exclusions=[], skip_topics=base_plan.skip_topics)
    picks = [p for p in (_pick(x) for x in submission.get("picks", [])) if p]
    dropped = [DroppedOut(video_id=d["video_id"], reason=str(d.get("reason", "")))
               for d in submission.get("dropped", []) if isinstance(d, dict) and d.get("video_id")]
    sel = SelectOut(picks=picks, dropped=dropped, near_duplicates=[], warnings=submission.get("warnings", []))
    fixes: list[str] = []
    sel = _sanitize(sel, pool, assessments, fixes)
    while sum(counted_minutes(p, pool[p.video_id]) for p in sel.picks) > persona.time_budget_minutes and sel.picks:
        weakest = min(sel.picks, key=lambda p: p.confidence)
        sel.picks.remove(weakest)
        fixes.append(f"removed {weakest.video_id} (lowest confidence) to fit the budget")

    # A revision (turns == 0, called from continue_loop) updates the curriculum but must not erase how the
    # original build worked: keep that trace's provenance and make the cost cumulative across revisions.
    prev_trace, prev_cost = None, 0.0
    if turns == 0 and out_dir and (out_dir / "trace.json").exists():
        try:
            prev_trace = json.loads((out_dir / "trace.json").read_text())
            prev_cost = float(json.loads((out_dir / "curriculum.json").read_text()).get("cost_usd") or 0.0)
        except Exception:
            prev_trace, prev_cost = None, 0.0  # a damaged old trace never blocks saving the new curriculum

    cur = assemble(persona, plan, pool, assessments, sel, pre_dropped=[], models={"agent_loop": model},
                   cost=round(ledger.total_cost + prev_cost, 5), latency=round(time.time() - t0, 1), mode="agent_loop")
    trace = {
        "persona": persona.model_dump(), "mode": "agent_loop", "models": {"agent_loop": model},
        "turns": turns, "tool_log": tool_log, "videos_read": len(read_ids),
        "timings_s": {"agent_loop": round(time.time() - t0, 1)}, "cost_by_stage": ledger.by_stage(),
        "calls": [c.__dict__ for c in ledger.calls], "plan": plan.model_dump(),
        "pool": [{"video_id": c.video_id, "title": c.title, "channel": c.channel, "minutes": c.minutes,
                  "views": c.view_count, "found_by": c.found_by, "transcript_lang": c.transcript_lang,
                  "transcript_generated": c.transcript_generated, "transcript_error": c.transcript_error}
                 for c in pool.values()],
        "assessments": {k: v.model_dump() for k, v in assessments.items()},
        "dup_clusters": [], "selector_raw": sel.model_dump(), "fixes": fixes,
    }
    if prev_trace is not None:  # carry the original build's provenance through the revision
        trace["turns"] = prev_trace.get("turns", 0)
        trace["tool_log"] = prev_trace.get("tool_log") or []
        trace["videos_read"] = max(trace["videos_read"], prev_trace.get("videos_read", 0))
        trace["timings_s"] = {**prev_trace.get("timings_s", {}), "revision": round(time.time() - t0, 1)}
        merged = dict(prev_trace.get("cost_by_stage", {}))
        for k, v in ledger.by_stage().items():
            merged[k] = ({m: round(merged[k].get(m, 0) + v.get(m, 0), 5) for m in set(merged[k]) | set(v)}
                         if k in merged else v)
        trace["cost_by_stage"] = merged
        trace["calls"] = prev_trace.get("calls", []) + trace["calls"]
        trace["revisions"] = prev_trace.get("revisions", 0) + 1
    if out_dir:
        save(cur, trace, out_dir)
        # persist the conversation + its tool context so a follow-up can resume it (Q&A or revision)
        (out_dir / "conversation.json").write_text(json.dumps({
            "persona": persona.model_dump(), "messages": messages, "base_plan": base_plan.model_dump(),
            "pool": [c.model_dump() for c in pool.values()],
            "assessments": {k: v.model_dump() for k, v in assessments.items()},
            "read_ids": list(read_ids),
        }, default=str))
    # the curriculum itself drives the right-hand artifact panel; each emit is a new version there
    emit({"kind": "curriculum", "data": cur.model_dump(), "fixes": fixes, "revision": turns == 0})
    if turns:  # initial build (continue_loop passes turns=0 for a revision, which only adds a version)
        emit({"kind": "done", "n_videos": len({p.video_id for p in cur.picks}), "minutes": round(cur.total_minutes),
              "budget": cur.budget_minutes, "turns": turns, "read": len(read_ids), "cost": round(cur.cost_usd, 3)})
    return cur, trace


def continue_loop(run_dir: Path, question: str, *, model: str | None = None, on_event=None, max_turns: int = 12):
    """Resume a saved agent-loop conversation with a learner follow-up. The agent answers from its OWN
    working memory (what it searched, read and chose) and may re-read videos to check; if the learner asks
    for a change it re-submits a revised curriculum. Returns (answer_text, changed, curriculum_or_None).

    This is the agent loop's native advantage over the fixed pipeline's `ask`: the model defending the
    curriculum is the one that built it, with its real context — not a fresh call reconstructing from a trace."""
    model = model or os.getenv("SELECT_MODEL") or DEFAULT_MODELS["select"]
    emit = on_event or (lambda e: None)
    conv = json.loads((run_dir / "conversation.json").read_text())
    persona = Persona.model_validate(conv["persona"])
    pool = {c["video_id"]: Candidate.model_validate(c) for c in conv["pool"]}
    assessments = {k: Assessment.model_validate(v) for k, v in conv["assessments"].items()}
    base_plan = PlanOut.model_validate(conv["base_plan"])
    read_ids = set(conv.get("read_ids", []))
    ledger = Ledger()
    t0 = time.time()
    messages = conv["messages"] + [{"role": "user", "content": question +
        "\n\n(Answer in plain text, grounded in what you actually read. Use search_youtube/read_video if you need to check "
        "something. Only call submit_curriculum if I asked you to CHANGE the curriculum.)"}]
    on_token = (lambda d: emit({"kind": "token", "text": d})) if on_event else None  # stream the answer in the chat UI
    answer, submission = "", None
    for _ in range(max_turns):
        try:
            msg = chat_tools(model, messages, TOOLS, stage="agent_loop_qa", ledger=ledger, max_tokens=4000, on_token=on_token)
        except Exception as ex:
            answer = f"(sorry — error: {type(ex).__name__})"
            break
        messages.append(_assistant_msg(msg))
        calls = msg.tool_calls or []
        if not calls:
            answer = msg.content or ""
            break
        for tc in calls:
            name = tc.function.name
            try:
                args = json.loads(tc.function.arguments or "{}")
            except json.JSONDecodeError:
                args = {}
            if name == "search_youtube":
                result = _search(pool, args.get("query", ""))
                emit({"kind": "search", "query": args.get("query", "")})
            elif name == "read_video":
                vid = args.get("video_id", "")
                if vid in pool:
                    read_ids.add(vid)
                result = _read(assessments, pool, vid)
                emit({"kind": "read", "video_id": vid, "title": result.get("title", vid)})
            elif name == "submit_curriculum":
                errs = _validate(args, pool, assessments, read_ids, persona.time_budget_minutes)
                if errs:  # a revision obeys the same rules as the first build: read before you pick, stay in budget
                    result = {"success": False, "errors": errs, "message": "Fix these and call submit_curriculum again."}
                    emit({"kind": "retry", "errors": errs})
                else:
                    submission = args
                    result = {"success": True, "message": "Revised curriculum accepted."}
                    emit({"kind": "submit", "n_picks": len(args.get("picks", []))})
            else:
                result = {"success": False, "error": f"unknown tool {name}"}
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": json.dumps(result)[:7000]})
        if submission is not None:
            break

    changed, cur = submission is not None, None
    if changed:
        cur, _ = _finalize(persona, submission, base_plan, pool, assessments, model, ledger, t0,
                           [], 0, read_ids, messages, run_dir, emit)
        answer = answer or "I've updated the curriculum based on your request — see above."
    else:  # persist the extended conversation so the next follow-up keeps the context
        conv["messages"], conv["read_ids"] = messages, list(read_ids)
        (run_dir / "conversation.json").write_text(json.dumps(conv, default=str))
    # the answer text was already streamed via on_token; `text` here is a fallback for a client that missed the stream
    emit({"kind": "answer_done", "text": answer, "changed": changed})
    return answer, changed, cur
