"""Stage 4: a cheap model reads each candidate's transcript excerpt and fills in an AssessOut.

Quotes are then checked word-for-word against the excerpt; only verified quotes are passed on, so
the selector can't cite evidence that isn't there.
"""

from __future__ import annotations

import hashlib
from concurrent.futures import ThreadPoolExecutor

from . import store, youtube
from .llm import Ledger, chat_json
from .models import AssessOut, Assessment, Candidate, Persona, PlanOut
from .prompts import load, persona_block
from .verify import locate_quote


def _plan_block(plan: PlanOut) -> str:
    subs = "\n".join(f"- {s.id}: {s.title}" for s in plan.sub_topics)
    return f"Learner level: {plan.learner_level}\nPreferred language: {plan.preferred_language}\nSub-topics:\n{subs}"


def _video_block(c: Candidate, use_transcript: bool) -> str:
    head = (
        f"Title: {c.title}\nChannel: {c.channel}\nDuration: {youtube.ts(c.duration_s)}\nUploaded: {c.upload_date or 'unknown'}\n"
        f"Description (truncated): {c.description[:400] or '-'}\n"
    )
    if use_transcript and c.evidence_kind == "transcript":
        kind = "auto-generated" if c.transcript_generated else "manual"
        return head + f"Transcript ({kind}, language {c.transcript_lang}), with chapter markers if the video has them:\n{c.windows}"
    if use_transcript and c.evidence_kind == "metadata":
        return head + ("Transcript: NOT AVAILABLE. Below are the video's chapter list and full description instead. "
                       "Quote from these lines only, add the red flag poor_transcript, and keep the assessment cautious:\n" + c.windows)
    return head + "Transcript: NOT AVAILABLE. Judge only from the title and description, return no quotes, and keep the assessment cautious."


def assess_one(c: Candidate, persona: Persona, plan: PlanOut, ledger: Ledger, model: str, use_transcript: bool = True) -> Assessment:
    user = f"LEARNER\n{persona_block(persona)}\n\nPLAN\n{_plan_block(plan)}\n\nVIDEO\n{_video_block(c, use_transcript)}"
    key = hashlib.sha1(f"{model}|{load('assess')}|{user}".encode()).hexdigest()[:20]
    path = youtube._cache_path("assessments", f"{c.video_id}.{key}")
    # Cache order: local file, then the shared MongoDB cache (keyed by video + prompt version, so many
    # workers reuse one assessment — the README's main lever for serving popular topics at scale), then compute.
    if path.exists():
        out = AssessOut.model_validate_json(path.read_text())
    elif (cached := store.cache_get("assessments", f"{c.video_id}.{key}")) is not None:
        out = AssessOut.model_validate(cached)
        path.write_text(out.model_dump_json())
    else:
        out = chat_json(model, load("assess"), user, AssessOut, stage="assess", ledger=ledger, max_tokens=6000)
        path.write_text(out.model_dump_json())
        store.cache_set("assessments", f"{c.video_id}.{key}", out.model_dump())

    has_text = use_transcript and c.evidence_kind != "none" and bool(c.windows)
    source = "transcript" if use_transcript and c.evidence_kind == "transcript" else "metadata"
    a = Assessment(**out.model_dump(), video_id=c.video_id, evidence_source=source)
    if has_text:
        for q in a.quotes:
            found, at, _ = locate_quote(q.text, c.windows, q.t)
            if found:
                q.t = at if at is not None else q.t
                a.verified_quote_ids.append(q.id)
    else:
        a.quotes = []
    return a


def assess_all(pool: list[Candidate], persona: Persona, plan: PlanOut, ledger: Ledger, model: str,
               use_transcripts: bool = True, workers: int = 12) -> dict[str, Assessment]:
    with ThreadPoolExecutor(workers) as ex:
        results = list(ex.map(lambda c: assess_one(c, persona, plan, ledger, model, use_transcripts), pool))
    return {a.video_id: a for a in results}


