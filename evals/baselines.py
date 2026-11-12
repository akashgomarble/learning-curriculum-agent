"""Baselines the agent has to beat.

- top_n_by_views: the brief's "search and view count" world. Same candidate pool as the agent,
  sorted by views, greedily filled up to the budget. No LLM.
- no_transcript: the full pipeline, but the assessor only sees title + description
  (`curriculum run --offline --no-transcripts`). Isolates what reading the content buys.
"""

from __future__ import annotations

from curriculum.models import Candidate, Curriculum, Pick, PlanOut


def top_n_by_views(persona_id: str, goal: str, budget: int, plan: PlanOut, pool: list[Candidate]) -> Curriculum:
    picks, total = [], 0.0
    for c in sorted(pool, key=lambda c: -(c.view_count or 0)):
        if total + c.minutes <= budget:
            total += c.minutes
            picks.append(Pick(
                rank=len(picks) + 1, video_id=c.video_id, title=c.title, channel=c.channel, url=c.url,
                duration_min=c.minutes, minutes_counted=c.minutes, covers=[],
                reason=f"Popular result ({c.view_count or 0:,} views) for '{c.found_by[0]}'.",
                evidence=[], confidence=0.5, confidence_note="ranked by view count only",
            ))
    return Curriculum(
        persona_id=persona_id, goal=goal, budget_minutes=budget, total_minutes=round(total, 1),
        interpretation="(baseline: no interpretation)", assumptions=[], feasible=True,
        feasibility_note="", sub_topics=plan.sub_topics, picks=picks, dropped=[],
        near_duplicates=[], warnings=[], pool_size=len(pool), models={}, cost_usd=0.0, latency_s=0.0,
        mode="top_n_by_views",
    )
