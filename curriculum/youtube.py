"""YouTube discovery and transcripts.

- Search and details: the official YouTube Data API v3 when YOUTUBE_API_KEY is set (public data only,
  API key, no OAuth); otherwise yt-dlp `ytsearchN:` in flat mode (~1-2 s per query; gives id, title,
  duration, views, channel). The Data API cannot return caption text for videos you don't own
  (captions.download needs edit permission on the video), so transcripts always come from below.
- Transcripts: youtube-transcript-api. When YouTube blocks this IP and SUPADATA_API_KEY is set, the
  hosted Supadata API (existing captions only, 1 credit per video) takes over, within a credit cap.
  Missing transcripts are recorded, not fatal.
- Everything is cached on disk by query / video id, so re-runs don't hit YouTube again.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import ssl
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import certifi

os.environ.setdefault("SSL_CERT_FILE", certifi.where())  # python.org macOS builds ship without CA certs

import yt_dlp  # noqa: E402
from youtube_transcript_api import (  # noqa: E402
    IpBlocked,
    NoTranscriptFound,
    RequestBlocked,
    TranscriptsDisabled,
    VideoUnavailable,
    YouTubeTranscriptApi,
)

from . import store  # noqa: E402
from .models import Candidate, Snippet  # noqa: E402

CACHE = Path(os.getenv("CURRICULUM_CACHE", ".cache"))
SEARCH_TTL_S = 7 * 24 * 3600

# Windowing: what the assessor reads. ~171 spoken words per minute measured on 25 videos.
FULL_UNTIL_S = 25 * 60
WINDOW_S = 90
N_WINDOWS = 10
MAX_WORDS = 5000


def _cache_path(kind: str, key: str) -> Path:
    p = CACHE / kind / f"{key}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


# ---------------------------------------------------------------- YouTube Data API v3 (optional)

API = "https://www.googleapis.com/youtube/v3"
_SSL = ssl.create_default_context(cafile=certifi.where())


def _api_key() -> str | None:
    return os.getenv("YOUTUBE_API_KEY") or None


def _api_get(endpoint: str, **params) -> dict:
    """One Data API call. search.list draws on its own small daily bucket; videos.list costs 1 unit per
    call for up to 50 ids. Errors never include the URL, so the key can't leak into logs or traces."""
    url = f"{API}/{endpoint}?" + urllib.parse.urlencode({**params, "key": _api_key()})
    try:
        with urllib.request.urlopen(url, timeout=20, context=_SSL) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        try:
            reason = json.loads(e.read())["error"]["errors"][0]["reason"]
        except Exception:
            reason = ""
        raise RuntimeError(f"YouTube Data API {endpoint}: HTTP {e.code} {reason}".strip()) from None


def _iso_duration(d: str) -> int:
    """ISO 8601 duration (PT1H2M3S, P1DT2H) -> seconds."""
    m = re.fullmatch(r"P(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?", d or "")
    if not m:
        return 0
    days, h, mi, sec = (int(x or 0) for x in m.groups())
    return ((days * 24 + h) * 60 + mi) * 60 + sec


_CHAPTER = re.compile(r"^\s*[\[(]?((?:\d{1,2}:)?\d{1,2}:\d{2})[\])]?\s*[-–—:|.]?\s*(.+?)\s*$")


def parse_chapters(description: str) -> list[dict]:
    """YouTube's chapter rule: time-stamped lines in the description, the first at 0:00, at least 3,
    ascending. The Data API has no chapters field, so this mirrors what the player shows."""
    out = []
    for line in (description or "").splitlines():
        m = _CHAPTER.match(line)
        if m:
            secs = 0
            for part in m.group(1).split(":"):
                secs = secs * 60 + int(part)
            out.append({"start": secs, "title": m.group(2)})
    if len(out) < 3 or out[0]["start"] != 0 or any(b["start"] <= a["start"] for a, b in zip(out, out[1:])):
        return []
    return out


def _details_from_item(it: dict) -> dict:
    sn, cd, st = it.get("snippet", {}), it.get("contentDetails", {}), it.get("statistics", {})
    desc = sn.get("description") or ""
    return {
        "title": sn.get("title") or "",
        "channel": sn.get("channelTitle") or "",
        "duration_s": _iso_duration(cd.get("duration", "")),
        "view_count": int(st["viewCount"]) if st.get("viewCount") else None,
        "description": desc,
        "chapters": parse_chapters(desc),
        "upload_date": (sn.get("publishedAt") or "")[:10].replace("-", "") or None,
        "like_count": int(st["likeCount"]) if st.get("likeCount") else None,
        "language": sn.get("defaultAudioLanguage") or sn.get("defaultLanguage"),
        "has_uploaded_captions": cd.get("caption") == "true",  # ignores auto-generated captions
        "source": "data_api",
    }


def api_videos(ids: list[str]) -> dict[str, dict]:
    """videos.list for many ids (50 per call, 1 quota unit per call); results land in the details cache.
    Ids missing from the response are private, removed or region-blocked."""
    out: dict[str, dict] = {}
    for i in range(0, len(ids), 50):
        chunk = ids[i : i + 50]
        items = _api_get("videos", part="snippet,contentDetails,statistics", id=",".join(chunk), maxResults=50).get("items", [])
        found = {it["id"]: _details_from_item(it) for it in items}
        for vid in chunk:
            d = found.get(vid, {"error": "Video unavailable (not returned by the Data API)"})
            _cache_path("details", vid).write_text(json.dumps(d))
            out[vid] = d
    return out


def _api_search(query: str, n: int) -> list[dict]:
    if re.fullmatch(r"[\w-]{11}", query):  # a bare video id (used by `ask`): look it up, don't search for it
        ids = [query]
    else:
        res = _api_get("search", part="snippet", q=query, type="video", maxResults=min(n, 50), safeSearch="moderate")
        ids = [it["id"]["videoId"] for it in res.get("items", []) if it.get("id", {}).get("videoId")]
    details = api_videos(ids) if ids else {}
    return [
        {"id": vid, "title": d["title"], "channel": d["channel"], "duration": d["duration_s"],
         "view_count": d["view_count"], "description": d["description"]}
        for vid in ids if not (d := details[vid]).get("error")
    ]


def search(query: str, n: int = 10) -> list[Candidate]:
    path = _cache_path("search", hashlib.sha1(f"{n}:{query}".encode()).hexdigest()[:16])
    if path.exists() and time.time() - path.stat().st_mtime < SEARCH_TTL_S:
        entries = json.loads(path.read_text())
    elif _api_key():
        entries = _api_search(query, n)
        path.write_text(json.dumps(entries))
    else:
        opts = {"quiet": True, "no_warnings": True, "extract_flat": True, "skip_download": True}
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(f"ytsearch{n}:{query}", download=False)
        entries = [
            {k: e.get(k) for k in ("id", "title", "channel", "duration", "view_count", "description", "_type", "url")}
            for e in info.get("entries") or []
        ]
        path.write_text(json.dumps(entries))
    out = []
    for e in entries:
        vid = e.get("id") or ""
        # Playlists and channels show up in search results; they have no duration.
        if len(vid) != 11 or not e.get("duration"):
            continue
        out.append(
            Candidate(
                video_id=vid,
                title=e.get("title") or "",
                channel=e.get("channel") or "",
                duration_s=int(e["duration"]),
                view_count=e.get("view_count"),
                description=(e.get("description") or "")[:500],
                found_by=[query],
            )
        )
    return out


class _Breaker:
    """Stops asking YouTube for transcripts after repeated blocks, instead of hammering it
    (which extends the block). Shared across threads for the whole process."""

    def __init__(self, limit: int = 3):
        self.limit, self.strikes, self.lock = limit, 0, threading.Lock()

    @property
    def open(self) -> bool:
        return self.strikes >= self.limit

    def hit(self, blocked: bool) -> None:
        with self.lock:
            self.strikes = self.strikes + 1 if blocked else 0


transcript_breaker = _Breaker()
_PERMANENT = ("TranscriptsDisabled", "NoTranscriptFound", "VideoUnavailable", "no_preferred_language")


# ---------------------------------------------------------------- Supadata (hosted transcripts, optional)

SUPADATA = "https://api.supadata.ai/v1"


class _Credits:
    """Spend at most SUPADATA_MAX_CREDITS per process (default: what the plan has left, minus 5),
    so a run can never silently use up the month. Each native transcript costs 1 credit, hit or miss."""

    def __init__(self):
        self.lock, self.left = threading.Lock(), None

    def take(self) -> bool:
        with self.lock:
            if self.left is None:
                cap = os.getenv("SUPADATA_MAX_CREDITS")
                if cap:
                    self.left = int(cap)
                else:
                    try:
                        me = _supadata_get("/me")
                        self.left = max(0, me["maxCredits"] - me["usedCredits"] - 5)
                    except Exception:
                        self.left = 0
            if self.left <= 0:
                return False
            self.left -= 1
            return True

    def stop(self) -> None:
        with self.lock:
            self.left = 0


supadata_credits = _Credits()
_supadata_lock = threading.Lock()


def _supadata_get(path: str, **params) -> dict:
    url = SUPADATA + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers={"x-api-key": os.environ["SUPADATA_API_KEY"]})
    try:
        with urllib.request.urlopen(req, timeout=120, context=_SSL) as r:
            body = json.loads(r.read() or b"{}")
            return {"_status": r.status, **body}
    except urllib.error.HTTPError as e:
        try:
            body = json.loads(e.read())
        except Exception:
            body = {}
        return {"_status": e.code, **body}


def _supadata_transcript(video_id: str, languages: list[str]) -> dict:
    """Existing captions only (mode=native: never pays for AI generation). Same dict shape as the
    youtube-transcript-api path. Videos over 20 min come back as a job to poll."""
    if not supadata_credits.take():
        return {"error": "skipped: Supadata credit cap reached"}
    for wait in (2, 5, 10, 20, None):
        with _supadata_lock:  # the free plan rejects parallel requests; one at a time
            d = _supadata_get("/transcript", url=f"https://www.youtube.com/watch?v={video_id}", lang=languages[0][:2], mode="native")
        if not (d.get("error") == "limit-exceeded" and "rate" in (d.get("details") or "").lower()) or wait is None:
            break
        time.sleep(wait)
    job = d.get("jobId") if d.get("_status") == 202 else None
    for _ in range(150 if job else 0):  # polls are free; results expire an hour after completion
        time.sleep(1)
        d = _supadata_get(f"/transcript/{job}")
        if d.get("status") not in ("queued", "active"):
            break
    status, err = d.get("_status"), d.get("error")
    if d.get("status") == "failed":
        err = err or "job failed"
    if err == "limit-exceeded" and "usage" in (d.get("details") or "").lower():
        supadata_credits.stop()
    if status == 206 or err == "transcript-unavailable":
        return {"error": "NoTranscriptFound", "permanent": True}
    if status in (403, 404) or err in ("forbidden", "not-found"):
        return {"error": "VideoUnavailable", "permanent": True}
    if err or not isinstance(d.get("content"), list):
        return {"error": f"Supadata {status} {err or 'no content'}"}
    lang = (d.get("lang") or "")[:2]
    if lang and lang != languages[0][:2]:
        return {"error": "no_preferred_language", "lang": lang, "permanent": True}
    return {"snippets": [{"start": x["offset"] / 1000, "text": x["text"]} for x in d["content"] if x.get("text")],
            "lang": d.get("lang"), "generated": None, "error": None, "source": "supadata"}


# ------------------------------------------- Gemini transcription (optional, through OpenRouter)

GEMINI_MODEL = os.getenv("GEMINI_TRANSCRIBE_MODEL", "google/gemini-2.5-flash")


class _Budget:
    """Caps total USD spent on video transcription in one process. GEMINI_MAX_USD unset or 0 keeps the
    fallback off entirely, so nothing is transcribed unless the operator opts in with a ceiling."""

    def __init__(self):
        self.lock, self.spent = threading.Lock(), 0.0
        self.cap = float(os.getenv("GEMINI_MAX_USD", "0"))

    @property
    def enabled(self) -> bool:
        return self.cap > 0

    def ok(self) -> bool:
        with self.lock:
            return self.spent < self.cap

    def charge(self, usd: float) -> None:
        with self.lock:
            self.spent += usd


gemini_budget = _Budget()


_TRANSCRIBE_PROMPT = ("Transcribe the spoken audio of this video in its original language. Return JSON only: a list "
                      'of {"t": start_seconds_int, "text": one_sentence_string} in time order, covering the whole video.')


def _parse_segments(text: str, languages: list[str], source: str) -> dict:
    from .llm import _strip_fences
    try:
        seg = json.loads(_strip_fences(text), strict=False)  # ASR text may carry raw control chars inside strings
        snippets = [{"start": float(x["t"]), "text": str(x["text"])} for x in seg if str(x.get("text", "")).strip()]
    except Exception as e:
        return {"error": f"{source} bad JSON: {str(e)[:80]}"}
    if not snippets:
        return {"error": f"{source} returned no speech"}
    return {"snippets": snippets, "lang": languages[0][:2], "generated": True, "error": None, "source": source}


def _transcribe_openrouter(video_id: str, languages: list[str]) -> dict:
    """Primary route: a Gemini model THROUGH OPENROUTER — the same client and key as every other LLM call
    in this project. The provider fetches the video by URL (an official model feature, not a scrape of the
    caption endpoint). Limit: at full media resolution a video past roughly an hour overflows the context."""
    from .llm import client  # late import: this module is also used by LLM-free tooling
    try:
        resp = client().chat.completions.create(
            model=GEMINI_MODEL, max_tokens=48000, timeout=300,  # a dense hour of speech can exceed 16k output tokens
            messages=[{"role": "user", "content": [
                {"type": "video_url", "video_url": {"url": f"https://www.youtube.com/watch?v={video_id}"}},
                {"type": "text", "text": _TRANSCRIBE_PROMPT},
            ]}],
            extra_body={"usage": {"include": True}},
        )
    except Exception as e:
        msg = str(e)[:120]
        if "429" in msg:
            gemini_budget.charge(gemini_budget.cap)  # quota exhausted: stop asking for the rest of the run
        return {"error": f"Gemini {type(e).__name__}: {msg}"}
    usage = resp.usage.model_dump() if resp.usage else {}
    gemini_budget.charge(float(usage.get("cost") or usage.get("estimated_cost") or 0.0))
    choice = resp.choices[0]
    text = (choice.message.content or "").strip()
    if not text or choice.finish_reason not in (None, "stop"):
        return {"error": f"Gemini no content ({choice.finish_reason})"}
    return _parse_segments(text, languages, "gemini")


def _transcribe_google_direct(video_id: str, languages: list[str]) -> dict:
    """Very last backoff, used only when the OpenRouter route failed AND GEMINI_API_KEY is set: the same
    Gemini model on Google's own API, where low media resolution is available — so videos too long for
    the OpenRouter route (context overflow at full resolution) still transcribe. Billed to that key,
    charged against the same GEMINI_MAX_USD budget."""
    body = {
        "contents": [{"parts": [
            {"file_data": {"file_uri": f"https://www.youtube.com/watch?v={video_id}"}},
            {"text": _TRANSCRIBE_PROMPT},
        ]}],
        "generationConfig": {"response_mime_type": "application/json", "maxOutputTokens": 48000,
                             "mediaResolution": "MEDIA_RESOLUTION_LOW"},
    }
    model = GEMINI_MODEL.split("/")[-1]  # OpenRouter-style id -> Google id (google/gemini-2.5-flash -> gemini-2.5-flash)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={os.environ['GEMINI_API_KEY']}"
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300, context=_SSL) as r:
            d = json.loads(r.read())
    except urllib.error.HTTPError as e:
        try:
            status = json.loads(e.read())["error"]["status"]
        except Exception:
            status = ""
        if e.code == 429:
            gemini_budget.charge(gemini_budget.cap)
        return {"error": f"Google {e.code} {status}".strip()}
    except Exception as e:
        return {"error": f"Google {type(e).__name__}: {str(e)[:100]}"}
    u = d.get("usageMetadata", {})
    gemini_budget.charge(u.get("promptTokenCount", 0) / 1e6 * 0.30 + u.get("candidatesTokenCount", 0) / 1e6 * 2.50)
    cands = d.get("candidates") or []
    if not cands or cands[0].get("finishReason") not in (None, "STOP"):
        return {"error": f"Google no content ({cands[0].get('finishReason') if cands else 'empty'})"}
    return _parse_segments(cands[0]["content"]["parts"][0]["text"], languages, "gemini")


def _gemini_transcript(video_id: str, languages: list[str]) -> dict:
    """Transcribe a YouTube video with a Gemini model: OpenRouter first (every LLM call in this project
    goes through that one client), and only if that fails — and a GEMINI_API_KEY is set — Google's own
    API as the very last backoff. Both arms share the GEMINI_MAX_USD budget cap."""
    if not gemini_budget.ok():
        return {"error": "skipped: Gemini budget cap reached"}
    r = _transcribe_openrouter(video_id, languages)
    if r.get("error") and os.getenv("GEMINI_API_KEY") and gemini_budget.ok():
        g = _transcribe_google_direct(video_id, languages)
        if g.get("error") is None:
            return g
        r["error"] += f"; last backoff: {g['error']}"
    return r


def fetch_transcript(video_id: str, languages: list[str]) -> tuple[list[Snippet], str | None, bool | None, str | None]:
    """Returns (snippets, language_code, is_generated, error).

    Only downloads a transcript in one of `languages`; if none exists, reports the language that
    does exist (so the caller can drop the video with a reason) without spending a request on it."""
    path = _cache_path("transcripts", video_id)
    if path.exists():
        d = json.loads(path.read_text())
        return [Snippet(**x) for x in d["snippets"]], d["lang"], d["generated"], d["error"]
    shared = store.cache_get("transcripts", video_id)  # shared MongoDB cache (if configured): pull instead of refetch
    if shared is not None:
        path.write_text(json.dumps(shared))
        return [Snippet(**x) for x in shared["snippets"]], shared["lang"], shared["generated"], shared["error"]
    d = {"snippets": [], "lang": None, "generated": None, "error": None, "available": []}
    for attempt in range(0 if transcript_breaker.open else 2):
        try:
            tlist = YouTubeTranscriptApi().list(video_id)
            d["available"] = [(t.language_code, t.is_generated) for t in tlist]
            try:
                tr = tlist.find_transcript(languages)
            except NoTranscriptFound:
                d["lang"], d["generated"] = (d["available"][0] if d["available"] else (None, None))
                d["error"] = "no_preferred_language"
                break
            fetched = tr.fetch()
            d.update(snippets=[{"start": x.start, "text": x.text} for x in fetched.snippets],
                     lang=tr.language_code, generated=tr.is_generated, error=None)
            transcript_breaker.hit(False)
            break
        except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
            d["error"] = type(e).__name__
            break
        except (IpBlocked, RequestBlocked) as e:
            d["error"] = type(e).__name__
            transcript_breaker.hit(True)
            break
        except Exception as e:  # network hiccup: one retry
            d["error"] = f"{type(e).__name__}: {str(e)[:120]}"
            time.sleep(2)
    if transcript_breaker.open and d["error"] is None and not d["snippets"]:
        d["error"] = "skipped: YouTube is blocking transcript requests from this IP"
    if d["error"] and d["error"] not in _PERMANENT and os.getenv("SUPADATA_API_KEY"):
        sd = _supadata_transcript(video_id, languages)
        if sd.get("error") is None or sd.get("permanent"):
            d.update(snippets=sd.get("snippets", []), lang=sd.get("lang", d["lang"]), generated=sd.get("generated"),
                     error=sd["error"], source="supadata")
        else:
            d["error"] += f"; {sd['error']}"
    if d["error"] and d["error"] not in _PERMANENT and gemini_budget.enabled:
        g = _gemini_transcript(video_id, languages)
        if g.get("error") is None:
            d.update(snippets=g["snippets"], lang=g.get("lang", d["lang"]), generated=g.get("generated"),
                     error=None, source="gemini")
        else:
            d["error"] += f"; {g['error']}"
    if d["error"] is None or d["error"] in _PERMANENT:
        path.write_text(json.dumps(d))  # never cache transient failures
        store.cache_set("transcripts", video_id, d)  # push to the shared cache so other workers skip the fetch
    return [Snippet(**x) for x in d["snippets"]], d["lang"], d["generated"], d["error"]


def fetch_details(video_id: str) -> dict:
    """Full metadata for one video: full description, chapters, upload date, likes. From the details
    cache (filled in bulk by the Data API during search), the Data API, or yt-dlp (~3 s). Uses a
    different endpoint from transcripts, so it still works when those are blocked."""
    path = _cache_path("details", video_id)
    if path.exists():
        return json.loads(path.read_text())
    if _api_key():
        try:
            return api_videos([video_id])[video_id]
        except Exception as e:
            return {"error": f"{type(e).__name__}: {str(e)[:120]}"}
    opts = {"quiet": True, "no_warnings": True, "skip_download": True}
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
        d = {
            "description": info.get("description") or "",
            "chapters": [{"start": int(c["start_time"]), "title": c["title"]} for c in info.get("chapters") or []],
            "upload_date": info.get("upload_date"),
            "like_count": info.get("like_count"),
            "language": info.get("language"),
        }
        path.write_text(json.dumps(d))
        return d
    except Exception as e:
        return {"error": f"{type(e).__name__}: {str(e)[:120]}"}


def is_unavailable(details: dict) -> bool:
    """yt-dlp's error for private, removed or region-blocked videos (as opposed to a network failure)."""
    return bool(re.search(r"not available|private video|has been removed|unavailable", details.get("error", ""), re.I))


def metadata_evidence(details: dict) -> str:
    """Evidence text when no transcript is available: chapters (time-stamped) + full description."""
    lines = [f"[{ts(c['start'])}] (chapter) {c['title']}" for c in details.get("chapters", [])]
    desc = " ".join((details.get("description") or "").split())[:2500]
    return "\n".join(lines + ([f"[00:00] (description) {desc}"] if desc else []))


def ts(seconds: float) -> str:
    s = int(seconds)
    return f"{s // 3600}:{s // 60 % 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60:02d}:{s % 60:02d}"


def make_windows(snippets: list[Snippet], duration_s: int) -> str:
    """Time-stamped excerpt the assessor reads.

    Short videos (<= 25 min) are passed whole. Longer ones get the first 4 minutes (the outline),
    10 evenly spaced 90-second windows, and the last 2 minutes (what was built / recap).
    Capped at ~5,000 words so one assessment stays around 7k tokens.
    """
    if not snippets:
        return ""
    end = max(duration_s, int(snippets[-1].start) + 1)
    if end <= FULL_UNTIL_S:
        ranges = [(0, end)]
    else:
        step = (end - 360) / (N_WINDOWS + 1)
        ranges = [(0, 240)] + [(int(240 + step * (i + 1)), int(240 + step * (i + 1) + WINDOW_S)) for i in range(N_WINDOWS)]
        ranges.append((end - 120, end))
    lines, words = [], 0
    for a, b in ranges:
        chunk = [s for s in snippets if a <= s.start < b]
        if not chunk:
            continue
        if len(ranges) > 1:
            lines.append(f"--- [{ts(a)} - {ts(b)}] ---")
        # One line per ~20 s so timestamps stay precise without bloating the prompt.
        buf, buf_start = [], chunk[0].start
        for s in chunk:
            if s.start - buf_start >= 20 and buf:
                lines.append(f"[{ts(buf_start)}] {' '.join(buf)}")
                buf, buf_start = [], s.start
            buf.append(s.text.replace("\n", " ").strip())
        if buf:
            lines.append(f"[{ts(buf_start)}] {' '.join(buf)}")
        words = sum(len(line.split()) for line in lines)
        if words > MAX_WORDS:
            break
    text = "\n".join(lines)
    return " ".join(text.split(" ")[:MAX_WORDS]) if words > MAX_WORDS else text


_TS_LINE = re.compile(r"^\[(?:(\d+):)?(\d+):(\d{2})\] (.*)$")


def window_lines(windows: str) -> list[tuple[int, str]]:
    """Parse '[mm:ss] text' lines back into (seconds, text)."""
    out = []
    for line in windows.splitlines():
        m = _TS_LINE.match(line)
        if m:
            h, mnt, sec, txt = m.groups()
            out.append((int(h or 0) * 3600 + int(mnt) * 60 + int(sec), txt))
    return out
