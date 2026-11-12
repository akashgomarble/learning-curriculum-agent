"""Bonus: follow-up Q&A over a saved run ("why didn't you include video X?").

Loads trace.json (plan + assessments of every candidate, kept and dropped) and the curriculum. If the
question names a YouTube video that wasn't in the pool, it is fetched and assessed on the spot so
the answer compares like with like."""

from __future__ import annotations

import json
import re
from pathlib import Path

from pydantic import BaseModel

from . import discover, youtube
from .assess import assess_one
from .llm import Ledger, chat_json
from .models import Candidate, Curriculum, Persona, PlanOut
from .prompts import load, persona_block

QA_MODEL = "anthropic/claude-sonnet-5.5"
_VID = re.compile(r"(?:v=|youtu\.be/|^)([A-Za-z0-9_-]{11})(?:\b|$)")


class Answer(BaseModel):
    answer: str
    would_change_curriculum: bool


def _referenced_ids(question: str, known: set[str], pool_ids: set[str]) -> list[str]:
    """Video ids the question refers to that need fetching: URL / `v=` references always; a bare id-shaped
    token (the regex allows one only as the question's first word) only when it names a video from this
    run's pool — an unknown 11-char first word ("Recommended", "approx_2024") is a word, not a video id."""
    out = []
    for m in _VID.finditer(question):
        vid = m.group(1)
        if vid in known:
            continue
        if m.group(0) == vid and vid not in pool_ids:
            continue
        out.append(vid)
    return out


def ask(run_dir: Path, question: str) -> str:
    cur = Curriculum.model_validate_json((run_dir / "curriculum.json").read_text())
    trace = json.loads((run_dir / "trace.json").read_text())
    persona = Persona.model_validate(trace["persona"])
    plan = PlanOut.model_validate(trace["plan"])
    ledger = Ledger()
    titles = {p["video_id"]: p["title"] for p in trace["pool"]}
    cards = {vid: {"title": titles.get(vid, ""), **{k: a[k] for k in ("summary", "level", "format", "project_built", "red_flags", "topics_covered")},
                   "verified_quotes": [q for q in a["quotes"] if q["id"] in a["verified_quote_ids"]]}
             for vid, a in trace["assessments"].items()}

    extra = ""
    for vid in _referenced_ids(question, set(cards), set(titles)):
        found = youtube.search(vid, 1)
        c = found[0] if found and found[0].video_id == vid else Candidate(video_id=vid, title="(unknown title)")
        [c], _ = discover.hydrate([c], plan)
        a = assess_one(c, persona, plan, ledger, trace["models"]["assess"])
        extra += f"\n\nVIDEO NOT IN THE ORIGINAL POOL (assessed just now)\n{json.dumps({'video_id': vid, 'title': c.title, 'minutes': c.minutes, **a.model_dump(include={'summary','level','format','project_built','red_flags','topics_covered'})}, ensure_ascii=False)}"

    picked = [{"rank": p.rank, "video_id": p.video_id, "title": p.title, "minutes": p.minutes_counted, "reason": p.reason} for p in cur.picks]
    dropped = [{"video_id": d.video_id, "title": d.title, "stage": d.stage, "reason": d.reason} for d in cur.dropped]
    user = (f"LEARNER\n{persona_block(persona)}\n\nPLAN\n{json.dumps([s.model_dump() for s in plan.sub_topics])}\n\n"
            f"CURRICULUM ({cur.total_minutes:.0f}/{cur.budget_minutes} min)\n{json.dumps(picked, ensure_ascii=False)}\n\n"
            f"DROPPED\n{json.dumps(dropped, ensure_ascii=False)}\n\nASSESSMENTS OF ALL CANDIDATES\n"
            + "\n".join(json.dumps({"video_id": k, **v}, ensure_ascii=False) for k, v in cards.items())
            + extra + f"\n\nQUESTION\n{question}")
    out = chat_json(QA_MODEL, load("qa"), user, Answer, stage="qa", ledger=ledger, max_tokens=6000)
    flag = "\n\n(I would change the curriculum based on this.)" if out.would_change_curriculum else ""
    return f"{out.answer}{flag}\n\n[cost ${ledger.total_cost:.3f}]"
