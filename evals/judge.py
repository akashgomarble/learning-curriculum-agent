"""Layer 2: LLM judges, from a different model family than the curator (self-preference bias).

- rubric(): pointwise, binary pass/fail per criterion with the critique written first.
- pairwise(): A vs B on the same pool, run in both orders; if the two orders disagree it's a tie.
- faithfulness(): splits each pick's reason into claims and checks them against the evidence text.

The judge never sees view counts, and always gets a reference summary of what each video teaches,
so it grades the content choice rather than the prose.
"""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor
import os
from pathlib import Path
from typing import Literal

from pydantic import BaseModel

from curriculum.llm import Ledger, chat_json
from curriculum.models import Assessment, Candidate, Curriculum, Persona
from curriculum.prompts import persona_block

JUDGE_MODEL = os.getenv("JUDGE_MODEL", "openai/gpt-5.6-terra")
FAITH_MODEL = os.getenv("FAITH_MODEL", "openai/gpt-5.6-luna")
_P = Path(__file__).parent / "prompts"
CRITERIA = ["tailored", "content_grounded_reasons", "goal_mirroring", "prereq_order_sensible",
            "constraints_respected", "budget_well_used", "dropped_reasons_sound", "overall"]


class Verdict(BaseModel):
    critique: str
    verdict: Literal["pass", "fail"]


class PickVerdict(BaseModel):
    video_id: str
    critique: str
    verdict: Literal["pass", "fail"]


class RubricOut(BaseModel):
    tailored: Verdict
    content_grounded_reasons: Verdict
    goal_mirroring: Verdict
    prereq_order_sensible: Verdict
    constraints_respected: Verdict
    budget_well_used: Verdict
    dropped_reasons_sound: Verdict
    overall: Verdict
    per_pick: list[PickVerdict]


class PairOut(BaseModel):
    critique: str
    winner: Literal["A", "B", "tie"]


class Claim(BaseModel):
    claim: str
    supported: bool


class FaithOut(BaseModel):
    claims: list[Claim]


def _ref(a: Assessment | None) -> str:
    if not a:
        return "(no reference assessment)"
    proj = f" Builds: {a.project_built}." if a.project_built else ""
    flags = f" Flags: {', '.join(a.red_flags)}." if a.red_flags else ""
    src = "" if a.evidence_source == "transcript" else " [Assessed from chapters/description only; no transcript.]"
    return f"{a.summary}{proj} Level: {a.level}. Format: {a.format}. Language: {a.spoken_language}.{flags}{src}"


def curriculum_text(cur: Curriculum, ref: dict[str, Assessment], reason_chars: int | None = None,
                    show_dropped: bool = True) -> str:
    L = [f"Planned viewing time: {cur.total_minutes:.0f} of {cur.budget_minutes} min."]
    if cur.assumptions:
        L.append("Assumptions stated: " + "; ".join(cur.assumptions))
    if not cur.feasible:
        L.append("Feasibility note: " + cur.feasibility_note)
    if cur.warnings:
        L.append("Warnings to the learner: " + " | ".join(cur.warnings[:4]))
    for p in cur.picks:
        reason = p.reason if reason_chars is None else p.reason[:reason_chars]
        part = f" (watch {p.watch_from or '0:00'}-{p.watch_until or 'end'})" if (p.watch_from or p.watch_until) else ""
        L.append(f"\n{p.rank}. [{p.video_id}] {p.title} - {p.minutes_counted:.0f} min{part}")
        L.append(f"   Curriculum's reason: {reason}")
        for e in p.evidence[:2]:
            L.append(f"   Quote [{e.t}]: \"{e.quote}\"")
        L.append(f"   REFERENCE SUMMARY: {_ref(ref.get(p.video_id))}")
    sel = [d for d in cur.dropped if d.stage == "select"]
    if show_dropped and sel:
        L.append("\nConsidered and dropped:")
        L += [f"- {d.title}: {d.reason}" for d in sel[:10]]
    return "\n".join(L)


def rubric(cur: Curriculum, persona: Persona, ref: dict[str, Assessment], ledger: Ledger, model: str = JUDGE_MODEL) -> RubricOut:
    user = f"LEARNER\n{persona_block(persona)}\n\nCURRICULUM\n{curriculum_text(cur, ref)}"
    return chat_json(model, (_P / "rubric.md").read_text(), user, RubricOut, stage="judge_rubric", ledger=ledger, max_tokens=12000)


def pairwise(a: Curriculum, b: Curriculum, persona: Persona, ref: dict[str, Assessment], ledger: Ledger,
             model: str = JUDGE_MODEL, reason_chars: int = 160) -> dict:
    """Returns {'winner': 'a'|'b'|'tie', 'orders': [...], 'critiques': [...]}. Reasons are cut to the same
    length in both arms and dropped lists hidden, so only the selection itself is compared."""
    sysmsg = (_P / "pairwise.md").read_text()

    def ask(x: Curriculum, y: Curriculum) -> PairOut:
        user = (f"LEARNER\n{persona_block(persona)}\n\nCURRICULUM A\n{curriculum_text(x, ref, reason_chars, False)}"
                f"\n\nCURRICULUM B\n{curriculum_text(y, ref, reason_chars, False)}")
        return chat_json(model, sysmsg, user, PairOut, stage="judge_pairwise", ledger=ledger, max_tokens=8000)

    with ThreadPoolExecutor(2) as ex:
        first, second = ex.map(lambda xy: ask(*xy), [(a, b), (b, a)])
    w1 = {"A": "a", "B": "b", "tie": "tie"}[first.winner]
    w2 = {"A": "b", "B": "a", "tie": "tie"}[second.winner]
    return {"winner": w1 if w1 == w2 else "tie", "orders": [w1, w2], "critiques": [first.critique, second.critique]}


def faithfulness(cur: Curriculum, pool: dict[str, Candidate], ledger: Ledger, model: str = FAITH_MODEL) -> dict:
    sysmsg = (_P / "faithfulness.md").read_text()

    def one(p):
        c = pool.get(p.video_id)
        if not c or not c.windows:
            return p.video_id, None
        user = f"JUSTIFICATION\n{p.reason}\n\nEVIDENCE TEXT for '{c.title}'\n{c.windows}"
        out = chat_json(model, sysmsg, user, FaithOut, stage="judge_faith", ledger=ledger, max_tokens=4000)
        return p.video_id, [c.model_dump() for c in out.claims]

    with ThreadPoolExecutor(6) as ex:
        res = dict(ex.map(one, cur.picks))
    claims = [c for v in res.values() if v for c in v]
    frac = round(sum(c["supported"] for c in claims) / len(claims), 2) if claims else None
    return {"reason_faithfulness": frac, "claims": res}


def dump(obj) -> str:
    return json.dumps(obj, indent=1, ensure_ascii=False)
