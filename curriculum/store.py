"""Optional MongoDB persistence.

Local files stay the source of truth: `--offline` reproduction, the eval and the showcase all read from
`runs/`, `fixtures/` and `.cache/`. MongoDB is an *additive* durability + query layer, enabled only when
`MONGODB_URI` is set. Two things get persisted:

- **curricula**: every completed run (fixed pipeline, agent loop, baselines) as one document — queryable
  history that survives a machine, and what a real service would serve from.
- **cache**: the expensive, reusable artifacts (assessments, transcripts, details, searches). This is the
  README's production-scaling lever — "cache assessments by video and prompt version" — backed by a database
  instead of the local disk, so many workers share one cache.

Every function is a no-op that returns False/None/empty when `MONGODB_URI` is unset or the cluster is
unreachable, so the rest of the system never depends on it.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone

import certifi

DB_NAME = os.getenv("MONGODB_DB", "curriculum")
_db = None
_tried = False


def db():
    """Lazily connect; cache the handle. Returns None if unconfigured or unreachable (logged once)."""
    global _db, _tried
    if _tried:
        return _db
    _tried = True
    from dotenv import load_dotenv  # the db CLI path doesn't import llm, so load .env here too
    load_dotenv()
    uri = os.getenv("MONGODB_URI")
    if not uri:
        return None
    try:
        from pymongo import MongoClient

        client = MongoClient(uri, tlsCAFile=certifi.where(), serverSelectionTimeoutMS=20000, connectTimeoutMS=20000)
        client.admin.command("ping")  # fail fast with a clear reason instead of hanging later
        _db = client[DB_NAME]
    except Exception as e:
        print(f"[store] MongoDB not used ({type(e).__name__}: {str(e)[:120]})")
        _db = None
    return _db


def enabled() -> bool:
    return db() is not None


def _now():
    return datetime.now(timezone.utc)


def save_curriculum(cur, trace: dict) -> bool:
    """Upsert one completed run, keyed by persona + mode. Called from pipeline.save after the files are written."""
    d = db()
    if d is None:
        return False
    try:
        doc = {
            "_id": f"{cur.persona_id}:{cur.mode}", "persona_id": cur.persona_id, "mode": cur.mode,
            "goal": cur.goal, "budget_minutes": cur.budget_minutes, "total_minutes": cur.total_minutes,
            "n_videos": len({p.video_id for p in cur.picks}), "n_picks": len(cur.picks),
            "feasible": cur.feasible, "cost_usd": cur.cost_usd, "latency_s": cur.latency_s,
            "updated_at": _now(), "curriculum": json.loads(cur.model_dump_json()),
            "trace": {k: trace.get(k) for k in ("mode", "models", "turns", "videos_read", "timings_s",
                                                "cost_by_stage", "fixes", "tool_log")},
        }
        d.curricula.replace_one({"_id": doc["_id"]}, doc, upsert=True)
        return True
    except Exception as e:
        print(f"[store] save_curriculum failed ({type(e).__name__}: {str(e)[:100]})")
        return False


def list_curricula(persona_id: str | None = None) -> list[dict]:
    d = db()
    if d is None:
        return []
    q = {"persona_id": persona_id} if persona_id else {}
    return list(d.curricula.find(q, {"curriculum": 0}).sort("updated_at", -1))


def get_curriculum(persona_id: str, mode: str = "agent") -> dict | None:
    d = db()
    return d.curricula.find_one({"_id": f"{persona_id}:{mode}"}) if d is not None else None


# ---------------------------------------------------------------- shared cache (assessments, transcripts, …)

def cache_get(kind: str, key: str) -> dict | None:
    d = db()
    if d is None:
        return None
    doc = d.cache.find_one({"_id": f"{kind}:{key}"})
    return doc["value"] if doc else None


def cache_set(kind: str, key: str, value: dict) -> bool:
    d = db()
    if d is None:
        return False
    try:
        d.cache.replace_one({"_id": f"{kind}:{key}"},
                            {"_id": f"{kind}:{key}", "kind": kind, "value": value, "updated_at": _now()}, upsert=True)
        return True
    except Exception:
        return False


def stats() -> dict:
    d = db()
    if d is None:
        return {"enabled": False}
    out = {"enabled": True, "db": DB_NAME, "curricula": d.curricula.estimated_document_count(),
           "cache_total": d.cache.estimated_document_count()}
    out["cache_by_kind"] = {r["_id"]: r["n"] for r in d.cache.aggregate(
        [{"$group": {"_id": "$kind", "n": {"$sum": 1}}}])}
    out["by_mode"] = {r["_id"]: r["n"] for r in d.curricula.aggregate(
        [{"$group": {"_id": "$mode", "n": {"$sum": 1}}}])}
    return out
