"""Bonus: `curriculum compare --models A B ...` runs selection with each model on the saved pools
(same plan, same assessments, so only the selector differs), scores Layer 1, and has a judge from a
family not in the comparison decide pairwise against the first model."""

from __future__ import annotations

import json
from pathlib import Path

from curriculum.llm import Ledger
from curriculum.models import Curriculum
from curriculum.pipeline import load_persona, run

from . import judge
from .run_eval import load_system
from .checks import score

OUT = Path("evals/results/compare")


def main(models: list[str], judge_model: str, personas: list[str] | None) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ledger = Ledger()
    rows = []
    for path in sorted(Path("test_set").glob("*.json")):
        persona = load_persona(path)
        if personas and persona.persona_id not in personas:
            continue
        data = load_system(persona)
        if not data:
            continue
        curs = {}
        for m in models:
            d = OUT / m.replace("/", "_") / persona.persona_id
            if (d / "curriculum.json").exists():
                curs[m] = Curriculum.model_validate_json((d / "curriculum.json").read_text())
            else:
                curs[m], _ = run(persona, models={"select": m}, offline=True, out_dir=d, mode=f"select={m}", save_fixture=False)
        base = models[0]
        for m in models:
            ch = score(curs[m], persona, data["pool"], data["ref"], data["dup"])
            row = {"persona": persona.persona_id, "model": m, "pass": ch["pass"], "failed": ch["hard_failures"],
                   "util": ch["utilisation"], "unknown_cov": ch["unknown_coverage"], "redundancy": ch["max_redundancy"],
                   "select_cost": round(curs[m].cost_usd, 4), "latency_s": curs[m].latency_s}
            if m != base:
                w = judge.pairwise(curs[m], curs[base], persona, data["ref"], ledger, model=judge_model)["winner"]
                row["vs_" + base] = {"a": "win", "b": "loss", "tie": "tie"}[w]
            rows.append(row)
            print(row)
    (OUT / "compare.json").write_text(json.dumps(rows, indent=1))
    L = [f"# Selector comparison (judge: {judge_model}; pairwise vs {models[0]}, both orders)", "",
         "| persona | model | L1 pass | failed | util | unknown cov | redundancy | selection $ | latency s | pairwise vs base |",
         "|---|---|:-:|---|--:|--:|--:|--:|--:|:-:|"]
    for r in rows:
        L.append(f"| {r['persona']} | {r['model']} | {'✅' if r['pass'] else '❌'} | {', '.join(r['failed']) or '-'} | {r['util']} | "
                 f"{r['unknown_cov']} | {r['redundancy']} | {r['select_cost']} | {r['latency_s']} | {r.get('vs_' + models[0], '(base)')} |")
    L.append(f"\nJudge spend: ${ledger.total_cost:.2f}")
    (OUT / "COMPARE.md").write_text("\n".join(L) + "\n")
    print(f"wrote {OUT}/COMPARE.md")
