"""Stage 5: find candidates that teach the same material, using the topic labels the assessor
already produced (no extra LLM calls, no embedding model).

Two videos are near-duplicates when their topic sets overlap strongly (soft Jaccard >= 0.6,
where labels match fuzzily, so 'usestate hook' ~ 'usestate'), they are at the same level and in the
same format family. The selector gets the clusters and must keep at most one per cluster."""

from __future__ import annotations

from rapidfuzz import fuzz

from .models import Assessment

THRESHOLD = 0.6
_FAMILY = {"project_build": "build", "crash_course": "course", "full_course": "course", "lecture": "talk", "concept_explainer": "talk"}


def _match(a: str, b: str) -> bool:
    return a == b or fuzz.token_set_ratio(a, b) >= 88


def topic_overlap(x: list[str], y: list[str]) -> tuple[float, list[str]]:
    xs, ys = sorted(set(t.lower().strip() for t in x)), sorted(set(t.lower().strip() for t in y))
    if not xs or not ys:
        return 0.0, []
    shared = [a for a in xs if any(_match(a, b) for b in ys)]
    union = len(xs) + len(ys) - len(shared)
    return len(shared) / union, shared


def clusters(assessments: dict[str, Assessment]) -> list[dict]:
    """Greedy single-link clustering over pairs above the threshold."""
    ids = list(assessments)
    parent = {i: i for i in ids}

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i

    shared_by_pair = {}
    for i, a in enumerate(ids):
        for b in ids[i + 1 :]:
            A, B = assessments[a], assessments[b]
            if A.level != B.level or _FAMILY.get(A.format, A.format) != _FAMILY.get(B.format, B.format):
                continue
            score, shared = topic_overlap(A.topics_covered, B.topics_covered)
            if score >= THRESHOLD:
                parent[find(b)] = find(a)
                shared_by_pair[(a, b)] = shared
    groups: dict[str, list[str]] = {}
    for i in ids:
        groups.setdefault(find(i), []).append(i)
    out = []
    for members in groups.values():
        if len(members) < 2:
            continue
        shared = sorted({t for (a, b), s in shared_by_pair.items() if a in members and b in members for t in s})
        out.append({"members": members, "shared_topics": shared})
    return out
