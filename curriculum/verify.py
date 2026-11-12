"""Checks that do not need an LLM. Used by the pipeline (to drop unverifiable quotes before the
selector sees them) and by the eval (to score outputs)."""

from __future__ import annotations

import re

from rapidfuzz import fuzz

from .youtube import window_lines

QUOTE_MATCH_THRESHOLD = 85
NEAR_S = 90


def _norm(s: str) -> str:
    return " ".join(re.sub(r"[^\w\s]", " ", s.lower()).split())


def locate_quote(quote: str, windows: str, t: int | None = None) -> tuple[bool, int | None, float]:
    """Is `quote` (fuzzily) in the transcript excerpt? Returns (found, timestamp_s, score).

    First looks within +-90 s of the claimed timestamp, then anywhere (LLMs misplace timestamps more
    often than they invent words; a quote that exists but at the wrong time still counts, with the
    timestamp corrected)."""
    lines = window_lines(windows)
    q = _norm(quote)
    if not q or not lines:
        return False, None, 0.0

    def best(cands: list[tuple[int, str]]) -> tuple[float, int | None]:
        top, top_t, top_line = 0.0, None, -1.0
        for i in range(len(cands)):
            span = _norm(" ".join(txt for _, txt in cands[i : i + 3]))  # quotes can straddle lines
            sc = fuzz.partial_ratio(q, span)
            if sc < top:
                continue
            # timestamp = the line inside the span that matches best (not the span's first line)
            line_sc, line_t = max((fuzz.partial_ratio(q, _norm(txt)), s) for s, txt in cands[i : i + 3])
            closer = t is not None and top_t is not None and abs(line_t - t) < abs(top_t - t)
            if sc > top or line_sc > top_line or (line_sc == top_line and closer):
                top, top_t, top_line = sc, line_t, line_sc
        return top, top_t

    sc, at = best(lines)
    if t is not None:  # prefer a match near the claimed time, unless a clearly better one exists elsewhere
        near_sc, near_at = best([(s, txt) for s, txt in lines if abs(s - t) <= NEAR_S])
        if near_sc >= QUOTE_MATCH_THRESHOLD and near_sc >= sc:
            return True, near_at, near_sc
    return sc >= QUOTE_MATCH_THRESHOLD, at, sc
