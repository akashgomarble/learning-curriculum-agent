"""Layer 1: deterministic checks. No LLM, so they are cheap, repeatable and can't be talked round.

Every system (the agent, the baselines, the ablation) is scored against the SAME reference
assessments: the transcript-based assessments from the agent's candidate pool. So a baseline is not
rewarded for knowing less about the videos it picked.
"""

from __future__ import annotations

import re
from collections import Counter

from curriculum.dedup import topic_overlap
from curriculum.models import Assessment, Candidate, Curriculum, Persona
from curriculum.verify import locate_quote

LEVELS = {"beginner": 0, "intermediate": 1, "advanced": 2}

# Checks that decide pass/fail. Everything else is reported, not gated.
HARD = ["no_hallucinated_videos", "budget_fit", "constraint_violations", "known_leakage", "evidence_verified",
        "project_based", "level_floor", "language", "infeasibility_flagged", "assumptions_stated", "near_dup_respected",
        "recency_ok", "sitting_ok", "creators_ok"]
# Expectations that matter but are matters of degree: reported next to the pass/fail so a "pass" that
# used a third of the budget doesn't look like a clean pass.
SOFT = ["utilisation_ok", "pick_count_ok", "order_ok", "has_dropped_list"]


def _covers(text: str, words: list[str]) -> bool:
    t = text.lower()
    return any(w.lower() in t for w in words)


def learner_limits(picks: list, pool: dict[str, Candidate], ex) -> dict:
    """Constraints stated in the learner's own words (recency, sitting length, creators), checked
    against the candidate pool's metadata."""
    m: dict = {}
    old_picks = [p.video_id for p in picks if ex.min_upload_year and p.video_id in pool and pool[p.video_id].upload_date
                 and int(pool[p.video_id].upload_date[:4]) < ex.min_upload_year]
    m["too_old_list"] = old_picks
    m["recency_ok"] = not old_picks
    long_picks = [f"{p.video_id} ({p.minutes_counted:.0f} min)" for p in picks
                  if ex.max_sitting_minutes and p.minutes_counted > ex.max_sitting_minutes + 0.5]
    m["too_long_list"] = long_picks
    m["sitting_ok"] = not long_picks
    per = Counter(p.channel for p in picks)
    creator_issues = []
    if ex.max_channels and len(per) > ex.max_channels:
        creator_issues.append(f"{len(per)} creators (max {ex.max_channels})")
    if ex.max_per_channel:
        creator_issues += [f"{n} picks from {ch} (max {ex.max_per_channel})" for ch, n in per.items() if n > ex.max_per_channel]
    m["creator_issue_list"] = creator_issues
    m["creators_ok"] = not creator_issues
    return m


def score(cur: Curriculum, persona: Persona, pool: dict[str, Candidate], ref: dict[str, Assessment],
          dup_clusters: list[dict]) -> dict:
    ex = persona.expectations
    m: dict = {}
    picks = cur.picks
    picked_ref = [ref.get(p.video_id) for p in picks]

    m["n_picks"] = len(picks)
    m["total_min"] = round(cur.total_minutes, 1)
    m["utilisation"] = round(cur.total_minutes / cur.budget_minutes, 2) if cur.budget_minutes else 0
    m["no_hallucinated_videos"] = all(p.video_id in pool for p in picks)
    m["budget_fit"] = cur.total_minutes <= cur.budget_minutes + 0.5
    m["utilisation_ok"] = ex.min_utilisation <= m["utilisation"] <= ex.max_utilisation
    # Count distinct videos: a long course split into several sittings is still one video to the learner.
    m["n_videos"] = len({p.video_id for p in picks})
    m["pick_count_ok"] = ex.pick_count[0] <= m["n_videos"] <= ex.pick_count[1]

    # Constraint violations: forbidden title patterns, red flags the learner ruled out, wrong language.
    viol = []
    for p, a in zip(picks, picked_ref):
        if ex.forbidden_title_regex and re.search(ex.forbidden_title_regex, p.title):
            viol.append(f"{p.video_id}: title matches forbidden pattern")
        if a:
            bad = sorted(set(a.red_flags) & set(ex.forbidden_flags))
            if bad:
                viol.append(f"{p.video_id}: red flags {bad}")
    m["constraint_violation_list"] = viol
    m["constraint_violations"] = len(viol) == 0

    if ex.required_language:
        wrong = [p.video_id for p, a in zip(picks, picked_ref) if a and not a.spoken_language.lower().startswith(ex.required_language)]
        m["language_violation_list"] = wrong
        m["language"] = not wrong
    else:
        m["language"] = True

    # Known-topic leakage: a pick that mostly re-teaches what the learner knows and covers none of the gaps.
    gap_words = [w for ws in ex.unknown_synonyms.values() for w in ws]
    leaks = []
    for p, a in zip(picks, picked_ref):
        if not a:
            continue
        topics = a.topics_covered
        known_hits = [t for t in topics if any(k in t or t in k for k in ex.known_topics)]
        teaches_gap = _covers(" ".join(topics) + " " + a.summary, gap_words) if gap_words else True
        if topics and len(known_hits) / len(topics) >= 0.5 and not teaches_gap:
            leaks.append(p.video_id)
    m["known_leak_list"] = leaks
    m["known_leakage"] = not leaks

    # Coverage of the learner's 'unknown' list, judged on what the picks actually teach.
    covered = {}
    content = " ".join((" ".join(a.topics_covered) + " " + a.summary) for a in picked_ref if a)
    for item, words in ex.unknown_synonyms.items():
        covered[item] = _covers(content, words)
    m["unknown_covered"] = covered
    m["unknown_coverage"] = round(sum(covered.values()) / len(covered), 2) if covered else None

    # Order: a pick should not come before the pick that first covers its prerequisites.
    prereqs = {s.id: s.prereqs for s in cur.sub_topics}
    first_at: dict[str, int] = {}
    for i, p in enumerate(picks):
        for sid in p.covers:
            first_at.setdefault(sid, i)
    order_v = []
    for i, p in enumerate(picks):
        for sid in p.covers:
            for pre in prereqs.get(sid, []):
                if pre in first_at and first_at[pre] > i:
                    order_v.append(f"{p.video_id} covers {sid} before its prerequisite {pre}")
    levels = [LEVELS.get(a.level, 0) for a in picked_ref if a]
    for i in range(1, len(levels)):
        if levels[i - 1] - levels[i] >= 2:
            order_v.append(f"level drops from advanced to beginner at rank {i + 1}")
    m["order_violation_list"] = order_v
    m["order_ok"] = not order_v

    # Redundancy between picks (content overlap of their topics).
    red = 0.0
    for i in range(len(picked_ref)):
        for j in range(i + 1, len(picked_ref)):
            if picked_ref[i] and picked_ref[j] and picks[i].video_id != picks[j].video_id:  # slices of one course aren't redundant
                red = max(red, topic_overlap(picked_ref[i].topics_covered, picked_ref[j].topics_covered)[0])
    m["max_redundancy"] = round(red, 2)
    ids = {p.video_id for p in picks}
    m["near_dup_respected"] = all(len(ids & set(c["members"])) <= 1 for c in dup_clusters)

    # Grounding: every evidence quote must be findable in that video's evidence text; every pick needs one.
    n_q = n_ok = 0
    no_evidence = []
    for p in picks:
        if not p.evidence:
            no_evidence.append(p.video_id)
        c = pool.get(p.video_id)
        for e in p.evidence:
            n_q += 1
            if c and locate_quote(e.quote, c.windows)[0]:
                n_ok += 1
    m["quote_verifiability"] = round(n_ok / n_q, 2) if n_q else 0.0
    m["picks_without_evidence"] = no_evidence
    m["evidence_verified"] = n_q > 0 and n_ok == n_q and not no_evidence
    m["transcript_backed_share"] = round(
        sum(1 for a in picked_ref if a and a.evidence_source == "transcript") / len(picks), 2) if picks else 0.0

    m["project_based"] = (not ex.require_project_based) or any(a and a.is_project_based for a in picked_ref)
    if ex.min_level:
        low = [p.video_id for p, a in zip(picks, picked_ref) if a and LEVELS[a.level] < LEVELS[ex.min_level]]
        m["below_level_list"] = low
        m["level_floor"] = not low
    else:
        m["level_floor"] = True
    m.update(learner_limits(picks, pool, ex))
    m["infeasibility_flagged"] = (not ex.expect_infeasible) or (cur.feasible is False)
    m["assumptions_stated"] = (not ex.expect_assumptions) or bool(cur.assumptions)
    m["has_dropped_list"] = any(d.stage == "select" for d in cur.dropped)
    m["mean_confidence"] = round(sum(p.confidence for p in picks) / len(picks), 2) if picks else None
    m["cost_usd"] = cur.cost_usd
    m["latency_s"] = cur.latency_s
    m["hard_failures"] = [k for k in HARD if m.get(k) is False]
    m["soft_misses"] = [k for k in SOFT if m.get(k) is False]
    m["pass"] = not m["hard_failures"]
    return m
