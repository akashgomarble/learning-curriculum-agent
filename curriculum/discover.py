"""Stages 2-3: search YouTube with the plan's queries, prefilter, and fetch transcripts."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

from . import youtube
from .models import Candidate, Dropped, Persona, PlanOut

MIN_DURATION_S = 120  # Shorts can't carry a curriculum slot
MAX_POOL = 36  # candidates that get a transcript + assessment


def discover(persona: Persona, plan: PlanOut, per_query: int = 10) -> tuple[list[Candidate], list[Dropped]]:
    with ThreadPoolExecutor(4) as ex:
        results = list(ex.map(lambda q: youtube.search(q, per_query), plan.search_queries))

    merged: dict[str, Candidate] = {}
    order: list[str] = []
    # Interleave results (1st of each query, then 2nd of each, ...) so no single query dominates the pool.
    for rank in range(per_query):
        for res in results:
            if rank < len(res):
                c = res[rank]
                if c.video_id in merged:
                    merged[c.video_id].found_by += c.found_by
                else:
                    merged[c.video_id] = c
                    order.append(c.video_id)

    budget_s = persona.time_budget_minutes * 60
    max_len_s = max(3 * budget_s, budget_s + 3600)  # longer videos can still be watched in part
    dropped: list[Dropped] = []
    kept: list[Candidate] = []
    for vid in order:
        c = merged[vid]
        title = c.title.lower()
        hit = next((x for x in plan.title_exclusions if x in title), None)
        if c.duration_s < MIN_DURATION_S:
            dropped.append(Dropped(video_id=vid, title=c.title, stage="prefilter", reason=f"too short ({c.duration_s}s)"))
        elif hit:
            dropped.append(Dropped(video_id=vid, title=c.title, stage="prefilter", reason=f"title matches exclusion '{hit}' from the learner's constraints"))
        elif c.duration_s > max_len_s:
            dropped.append(Dropped(video_id=vid, title=c.title, stage="prefilter", reason=f"{c.minutes:.0f} min, far beyond the {persona.time_budget_minutes}-min budget"))
        else:
            kept.append(c)
    # Videos surfaced by several queries first; otherwise keep the interleaved order.
    kept.sort(key=lambda c: -len(c.found_by))
    for c in kept[MAX_POOL + 8 :]:
        dropped.append(Dropped(video_id=c.video_id, title=c.title, stage="prefilter", reason="pool cap reached"))
    kept = kept[: MAX_POOL + 8]  # a few spare for language/transcript losses
    return kept, dropped


def metadata_fallback(details: dict, search_description: str) -> tuple[str, str]:
    """Evidence text and kind when there is no transcript. If the details call failed too (e.g. the
    yt-dlp bot check), use the search-result description, so a candidate is never labelled
    'metadata' with no text behind it (which silently left every pick without quotes)."""
    windows = youtube.metadata_evidence(details if not details.get("error") else {"description": search_description})
    return windows, ("metadata" if windows else "none")


def hydrate(pool: list[Candidate], plan: PlanOut, use_transcripts: bool = True) -> tuple[list[Candidate], list[Dropped]]:
    """Fetch transcripts, build the windows the assessor reads, drop wrong-language videos."""
    lang = plan.preferred_language.lower()[:2] or "en"
    languages = [lang, f"{lang}-US", f"{lang}-GB", f"{lang}-IN"]

    def one(c: Candidate) -> Candidate:
        details = youtube.fetch_details(c.video_id)
        if youtube.is_unavailable(details):  # deleted/private videos still show up in search results
            c.transcript_error = "unavailable"
            return c
        c.upload_date, c.chapters = details.get("upload_date"), details.get("chapters", [])
        if details.get("description"):
            c.description = details["description"][:2000]
        snippets = []
        # Not skipped on the Data API's contentDetails.caption == "false": that flag ignores YouTube's
        # auto-generated captions, so it was false for 31 of 36 candidates that mostly do have transcripts.
        if use_transcripts:
            snippets, tlang, generated, err = youtube.fetch_transcript(c.video_id, languages)
            c.transcript_lang, c.transcript_generated, c.transcript_error = tlang, generated, err
            if not tlang and details.get("language"):
                c.transcript_lang = None  # unknown; the assessor reports the spoken language
        chapter_lines = [f"[{youtube.ts(ch['start'])}] (chapter) {ch['title']}" for ch in c.chapters]
        if snippets:
            c.evidence_kind = "transcript"
            c.windows = "\n".join(chapter_lines + [youtube.make_windows(snippets, c.duration_s)])
        elif use_transcripts:
            c.windows, c.evidence_kind = metadata_fallback(details, c.description)
        return c

    with ThreadPoolExecutor(4) as ex:
        pool = list(ex.map(one, pool))

    kept, dropped = [], []
    for c in pool:
        if c.transcript_error == "unavailable":
            dropped.append(Dropped(video_id=c.video_id, title=c.title, stage="prefilter", reason="video is unavailable (private or removed)"))
        elif use_transcripts and c.transcript_error == "no_preferred_language" and c.transcript_lang:
            dropped.append(Dropped(video_id=c.video_id, title=c.title, stage="language",
                                   reason=f"transcript is '{c.transcript_lang}', learner needs '{lang}'"))
        else:
            kept.append(c)
    # Prefer candidates we can actually read: transcript-backed first.
    kept.sort(key=lambda c: c.evidence_kind != "transcript")
    for c in kept[MAX_POOL:]:
        dropped.append(Dropped(video_id=c.video_id, title=c.title, stage="prefilter", reason="pool cap reached"))
    return kept[:MAX_POOL], dropped
