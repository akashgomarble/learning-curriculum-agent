"""`curriculum eval`: score every saved run against the baselines and write evals/results/.

For each persona in test_set/ that has a run in runs/:
  1. systems: agent (runs/<id>), top_n_by_views (computed), no_transcript (runs/<id>__no_transcript,
     created offline if missing)
  2. Layer 1 checks for every system, against the agent's transcript-based reference assessments
  3. Layer 2 (unless --skip-judge): rubric judge per system, pairwise agent-vs-baseline in both
     orders, reason faithfulness
  4. optional stability: re-run selection N times on the same pool, mean pairwise Jaccard of pick sets
Then writes RESULTS.md tables, a blind human-labelling sheet, and judge-human agreement if labels exist.
"""

from __future__ import annotations

import json
import os
import random
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from curriculum.llm import Ledger
from curriculum.models import Assessment, Candidate, Curriculum, Persona, PlanOut
from curriculum.pipeline import load_persona, run
from curriculum.prompts import persona_block

from . import agreement, judge
from .baselines import top_n_by_views
from .checks import score

RES = Path("evals/results")
LABELS = Path("evals/labels")
SYSTEMS = ["agent", "agent_loop", "top_n_by_views", "no_transcript"]


def load_system(persona: Persona) -> dict | None:
    run_dir = Path("runs") / persona.persona_id
    fx = Path("fixtures") / f"{persona.persona_id}.json"
    if not (run_dir / "curriculum.json").exists() or not fx.exists():
        return None
    fixture = json.loads(fx.read_text())
    pool = {c["video_id"]: Candidate.model_validate(c) for c in fixture["pool"]}
    ref = {k: Assessment.model_validate(v) for k, v in fixture["assessments"].items()}
    plan = PlanOut.model_validate(fixture["plan"])
    trace = json.loads((run_dir / "trace.json").read_text())
    systems = {"agent": Curriculum.model_validate_json((run_dir / "curriculum.json").read_text())}
    al = Path("runs") / f"{persona.persona_id}__agent_loop"  # the agent-loop variant, if it has been run
    if (al / "curriculum.json").exists():
        systems["agent_loop"] = Curriculum.model_validate_json((al / "curriculum.json").read_text())
    systems["top_n_by_views"] = top_n_by_views(persona.persona_id, persona.goal, persona.time_budget_minutes, plan, list(pool.values()))
    nt = Path("runs") / f"{persona.persona_id}__no_transcript"
    if not (nt / "curriculum.json").exists():
        print(f"  running no-transcript ablation for {persona.persona_id}")
        run(persona, use_transcripts=False, offline=True, out_dir=nt, mode="no_transcript")
    systems["no_transcript"] = Curriculum.model_validate_json((nt / "curriculum.json").read_text())
    return {"pool": pool, "ref": ref, "plan": plan, "dup": trace.get("dup_clusters", []), "systems": systems, "trace": trace}


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a | b else 1.0


def eval_persona(persona: Persona, data: dict, skip_judge: bool, stability: int, ledger: Ledger) -> dict:
    out: dict = {"persona_id": persona.persona_id, "budget": persona.time_budget_minutes, "systems": {}}
    for name, cur in data["systems"].items():
        out["systems"][name] = {"checks": score(cur, persona, data["pool"], data["ref"], data["dup"]),
                                "picks": [p.video_id for p in cur.picks]}
    prev_path = RES / f"{persona.persona_id}.json"
    if skip_judge and prev_path.exists():  # keep earlier judge verdicts (e.g. to add human labels without paying again)
        prev = json.loads(prev_path.read_text())
        same = all(prev["systems"].get(n, {}).get("picks") == out["systems"][n]["picks"] for n in out["systems"])
        if same:
            for n in out["systems"]:
                for k in ("rubric", "faithfulness"):
                    if k in prev["systems"].get(n, {}):
                        out["systems"][n][k] = prev["systems"][n][k]
            if "pairwise" in prev:
                out["pairwise"] = prev["pairwise"]
            if "stability" in prev and not stability:
                out["stability"] = prev["stability"]
    if not skip_judge:
        with ThreadPoolExecutor(6) as ex:
            rub = {n: ex.submit(judge.rubric, c, persona, data["ref"], ledger) for n, c in data["systems"].items()}
            pw_targets = [b for b in ("agent_loop", "top_n_by_views", "no_transcript") if b in data["systems"]]
            pw = {b: ex.submit(judge.pairwise, data["systems"]["agent"], data["systems"][b], persona, data["ref"], ledger)
                  for b in pw_targets}
            fa = {n: ex.submit(judge.faithfulness, data["systems"][n], data["pool"], ledger)
                  for n in ("agent", "agent_loop", "no_transcript") if n in data["systems"]}
            for n, f in rub.items():
                out["systems"][n]["rubric"] = f.result().model_dump()
            out["pairwise"] = {b: f.result() for b, f in pw.items()}
            for n, f in fa.items():
                out["systems"][n]["faithfulness"] = f.result()
    if stability:
        sets = [set(out["systems"]["agent"]["picks"])]
        for _ in range(stability - 1):
            cur, _ = run(persona, offline=True, save_fixture=False)
            sets.append({p.video_id for p in cur.picks})
        pairs = [jaccard(sets[i], sets[j]) for i in range(len(sets)) for j in range(i + 1, len(sets))]
        out["stability"] = {"runs": len(sets), "mean_pairwise_jaccard": round(sum(pairs) / len(pairs), 2), "pick_sets": [sorted(s) for s in sets]}
    return out


def main(personas: list[str] | None = None, skip_judge: bool = False, stability: int = 0) -> None:
    RES.mkdir(parents=True, exist_ok=True)
    ledger = Ledger()
    results, datas = [], {}
    for path in sorted(Path("test_set").glob("*.json")):
        persona = load_persona(path)
        if personas and persona.persona_id not in personas:
            continue
        data = load_system(persona)
        if not data:
            print(f"skip {persona.persona_id}: no run or fixture yet (run `curriculum run {path}` first)")
            continue
        print(f"eval {persona.persona_id}")
        r = eval_persona(persona, data, skip_judge, stability, ledger)
        (RES / f"{persona.persona_id}.json").write_text(json.dumps(r, indent=1, ensure_ascii=False, default=str))
        results.append(r)
        datas[persona.persona_id] = (persona, data)
    if not personas:
        write_label_sheet(datas)
    summary = summarize(results)
    summary["eval_cost_usd"] = ledger.total_cost
    if not skip_judge:
        summary["judge_models"] = {"rubric_and_pairwise": judge.JUDGE_MODEL, "faithfulness": judge.FAITH_MODEL}
    elif (RES / "summary.json").exists():  # verdicts were kept from the last judged run, so keep its judge names too
        summary["judge_models"] = json.loads((RES / "summary.json").read_text()).get("judge_models")
    (RES / "summary.json").write_text(json.dumps(summary, indent=1, default=str))
    (RES / "RESULTS.md").write_text(render_tables(results, summary))
    print(f"wrote {RES}/RESULTS.md (eval LLM cost ${ledger.total_cost:.2f})")


# ------------------------------------------------------------------ summary + tables

def summarize(results: list[dict]) -> dict:
    s: dict = {"personas": len(results), "by_system": {}, "pairwise": {}}
    for name in SYSTEMS:
        rows = [r["systems"][name] for r in results if name in r["systems"]]
        if not rows:
            continue
        ch = [x["checks"] for x in rows]
        mean = lambda k: round(sum(c[k] for c in ch if c.get(k) is not None) / max(1, sum(1 for c in ch if c.get(k) is not None)), 2)
        d = {"layer1_pass": f"{sum(c['pass'] for c in ch)}/{len(ch)}", "unknown_coverage": mean("unknown_coverage"),
             "utilisation": mean("utilisation"), "quote_verifiability": mean("quote_verifiability"),
             "max_redundancy": mean("max_redundancy"),
             "failures": sorted({f for c in ch for f in c["hard_failures"]}),
             "soft_misses": sorted({f for c in ch for f in c.get("soft_misses", [])})}
        rub = [x.get("rubric") for x in rows if x.get("rubric")]
        if rub:
            d["judge_overall_pass"] = f"{sum(r['overall']['verdict'] == 'pass' for r in rub)}/{len(rub)}"
            d["judge_criteria_pass_rate"] = {k: round(sum(r[k]['verdict'] == 'pass' for r in rub) / len(rub), 2) for k in judge.CRITERIA}
            picks = [p for r in rub for p in r["per_pick"]]
            d["judge_pick_pass_rate"] = round(sum(p["verdict"] == "pass" for p in picks) / len(picks), 2) if picks else None
        fa = [x["faithfulness"]["reason_faithfulness"] for x in rows if x.get("faithfulness") and x["faithfulness"]["reason_faithfulness"] is not None]
        if fa:
            d["reason_faithfulness"] = round(sum(fa) / len(fa), 2)
        s["by_system"][name] = d
    for b in ("agent_loop", "top_n_by_views", "no_transcript"):
        ws = [r["pairwise"][b]["winner"] for r in results if r.get("pairwise") and b in r["pairwise"]]
        if ws:
            s["pairwise"][f"agent_vs_{b}"] = {"agent_wins": ws.count("a"), "baseline_wins": ws.count("b"), "ties": ws.count("tie")}
    stab = [r["stability"]["mean_pairwise_jaccard"] for r in results if r.get("stability")]
    if stab:
        s["stability_mean_jaccard"] = round(sum(stab) / len(stab), 2)
    s["human_agreement"] = human_agreement(results)
    return s


def human_agreement(results: list[dict]) -> dict | None:
    labels = agreement.read_labels(LABELS / "human_labels.csv")
    key_path = LABELS / "blind_key.json"
    if not labels or not key_path.exists():
        return None
    key = json.loads(key_path.read_text())
    by_id = {r["persona_id"]: r for r in results}
    overall_h, overall_j, pick_h, pick_j, disagreements = [], [], [], [], []
    for lab in labels:
        r = by_id.get(lab["persona_id"])
        system = key.get(lab["persona_id"], {}).get(lab["system"])
        if not r or not system or not r["systems"].get(system, {}).get("rubric"):
            continue
        rub = r["systems"][system]["rubric"]
        h = 1 if lab["label"].strip().lower() == "pass" else 0
        if lab["item"] == "overall":
            j = 1 if rub["overall"]["verdict"] == "pass" else 0
            overall_h.append(h); overall_j.append(j)
            jc = rub["overall"]["critique"]
        else:
            pv = next((p for p in rub["per_pick"] if p["video_id"] == lab["item"]), None)
            if not pv:
                continue
            j = 1 if pv["verdict"] == "pass" else 0
            pick_h.append(h); pick_j.append(j)
            jc = pv["critique"]
        if h != j:
            disagreements.append({"persona_id": lab["persona_id"], "system": system, "item": lab["item"], "title": lab.get("title", ""),
                                  "human": lab["label"], "human_critique": lab.get("critique", ""),
                                  "judge": "pass" if j else "fail", "judge_critique": jc})
    return {"overall": agreement.compare(overall_h, overall_j) if overall_h else None,
            "per_pick": agreement.compare(pick_h, pick_j) if pick_h else None,
            "disagreements": disagreements}


LABEL_INSTRUCTIONS = [
    "# Human labelling sheet (blind)", "",
    "You are the human ground truth for the LLM judge. Label from this file only: do not open "
    "`evals/results/`, `runs/` or `blind_key.json` until every row you intend to label is filled in.", "",
    "## How to fill it", "",
    "1. Each persona below has four curricula, S1-S4, built from the same candidate pool. Which system is which "
    "is shuffled per persona (key in `blind_key.json`).",
    "2. Open `human_labels.csv` in a spreadsheet. Fill two columns only: `label` (`pass` or `fail`) and `critique` "
    "(one short sentence; required for every `fail`). Leave all other columns as they are.",
    "3. Rows with `item = overall` ask: *would you hand this curriculum to this learner as is?* Pass only if you would.",
    "4. The other rows are one per video: *is this a good pick for its place in this learner's curriculum?* "
    "Judge the video for this learner, not the curriculum around it.",
    "5. Minimum useful pass: the `overall` rows only (32 rows, about 40-50 minutes). Per-video rows are optional but "
    "give a larger n. Blank rows are ignored, so a partial sheet is fine.",
    "6. Then run `uv run curriculum eval --skip-judge` (free; reuses the saved judge verdicts) to compute "
    "judge-human agreement into `evals/results/RESULTS.md`.", "",
    "Notes: the REFERENCE SUMMARY under each video is the pipeline's own assessment; where it says "
    "\"chapters/description only\" there was no transcript. One system's reasons are a fixed template, so it is not "
    "fully blind; label it on its picks anyway.", "",
]


def write_label_sheet(datas: dict) -> None:
    """Blind sheet: systems are shuffled into S1-S4 per persona so the labeller can't tell which is which."""
    rng = random.Random(42)
    key, rows, md = {}, [], LABEL_INSTRUCTIONS[:]
    for pid, (persona, data) in datas.items():
        names = SYSTEMS[:]
        rng.shuffle(names)
        key[pid] = {f"S{i + 1}": n for i, n in enumerate(names)}
        md += [f"## {pid}", "", "```", persona_block(persona), "```", ""]
        for i, n in enumerate(names):
            code = f"S{i + 1}"
            cur = data["systems"][n]
            md += [f"### {pid} / {code}", "", judge.curriculum_text(cur, data["ref"]), ""]
            rows.append({"persona_id": pid, "system": code, "item": "overall", "title": "(whole curriculum)"})
            rows += [{"persona_id": pid, "system": code, "item": p.video_id, "title": p.title} for p in cur.picks]
    LABELS.mkdir(parents=True, exist_ok=True)
    (LABELS / "blind_key.json").write_text(json.dumps(key, indent=1))
    (LABELS / "LABEL_ME.md").write_text("\n".join(md))
    # One row per (persona, system, video) even when a course is used in slices; overall rows first,
    # since they are the minimum useful set.
    uniq = list({(r["persona_id"], r["system"], r["item"]): r for r in rows}.values())
    uniq.sort(key=lambda r: r["item"] != "overall")
    agreement.write_template(LABELS / "human_labels.csv", uniq)


def _fails(c: dict) -> str:
    """Hard failures in bold, soft misses (degree-of-quality expectations) in italics."""
    parts = [f"**{f}**" for f in c["hard_failures"]] + [f"_{f}_" for f in c.get("soft_misses", [])]
    return ", ".join(parts) or "-"


def render_tables(results: list[dict], s: dict) -> str:
    L = ["# Results (generated by `uv run curriculum eval`)", ""]
    if s.get("judge_models"):
        L += [f"Judges: {s['judge_models']['rubric_and_pairwise']} (rubric, pairwise), {s['judge_models']['faithfulness']} (faithfulness).", ""]
    L += ["Failed checks: **bold** = hard failure (fails Layer 1), _italic_ = soft miss (reported, not gated).", ""]
    L += ["## Per persona: agent", "",
          "| persona | budget | picks | min | util | unknown cov | quotes verified | transcript-backed | redundancy | L1 pass | failed checks | judge overall | faithfulness | vs views | vs no-transcript | cost $ | latency s |",
          "|---|--:|--:|--:|--:|--:|--:|--:|--:|:-:|---|:-:|--:|:-:|:-:|--:|--:|"]
    for r in results:
        a = r["systems"]["agent"]
        c = a["checks"]
        rub = a.get("rubric", {}).get("overall", {}).get("verdict", "-")
        fa = (a.get("faithfulness") or {}).get("reason_faithfulness", "-")
        pw = r.get("pairwise", {})
        L.append(f"| {r['persona_id']} | {r['budget']} | {c['n_picks']} | {c['total_min']:.0f} | {c['utilisation']} | "
                 f"{c['unknown_coverage']} | {c['quote_verifiability']} | {c['transcript_backed_share']} | {c['max_redundancy']} | "
                 f"{'✅' if c['pass'] else '❌'} | {_fails(c)} | {rub} | {fa} | "
                 f"{pw.get('top_n_by_views', {}).get('winner', '-')} | {pw.get('no_transcript', {}).get('winner', '-')} | "
                 f"{c['cost_usd']:.3f} | {c['latency_s']:.0f} |")
    L += ["", "_cost $ / latency s are from the run's own trace. A run made with `--offline` reuses the saved plan and "
          "assessments, so it reports the selection stage only; cold end-to-end numbers are in EVAL.md._"]
    L += ["", "## By system", "", "| system | L1 pass | unknown cov | util | quotes verified | redundancy | judge overall | judge pick pass | faithfulness | failed checks seen |",
          "|---|:-:|--:|--:|--:|--:|:-:|--:|--:|---|"]
    for n, d in s["by_system"].items():
        L.append(f"| {n} | {d['layer1_pass']} | {d['unknown_coverage']} | {d['utilisation']} | {d['quote_verifiability']} | "
                 f"{d['max_redundancy']} | {d.get('judge_overall_pass', '-')} | {d.get('judge_pick_pass_rate', '-')} | "
                 f"{d.get('reason_faithfulness', '-')} | {_fails({'hard_failures': d['failures'], 'soft_misses': d['soft_misses']})} |")
    if s.get("pairwise"):
        L += ["", "## Pairwise (judge, both orders; disagreement between orders = tie)", "", "| comparison | agent wins | baseline wins | ties |", "|---|--:|--:|--:|"]
        for k, v in s["pairwise"].items():
            L.append(f"| {k} | {v['agent_wins']} | {v['baseline_wins']} | {v['ties']} |")
    crit = {n: d.get("judge_criteria_pass_rate") for n, d in s["by_system"].items() if d.get("judge_criteria_pass_rate")}
    if crit:
        L += ["", "## Judge pass rate per criterion", "", "| criterion | " + " | ".join(crit) + " |", "|---|" + "--:|" * len(crit)]
        for k in judge.CRITERIA:
            L.append(f"| {k} | " + " | ".join(str(crit[n][k]) for n in crit) + " |")
    if s.get("stability_mean_jaccard") is not None:
        L += ["", f"Stability (same pool, selection re-run): mean pairwise Jaccard of pick sets = {s['stability_mean_jaccard']}"]
    ha = s.get("human_agreement")
    if ha:
        L += ["", "## Judge vs human", ""]
        for lvl in ("overall", "per_pick"):
            if ha.get(lvl):
                v = ha[lvl]
                L.append(f"- {lvl}: n={v['n']}, agreement={v['agreement']}, κ={v['kappa']} (95% CI {v['kappa_ci95']}), "
                         f"TPR={v['tpr']}, TNR={v['tnr']}, confusion={v['confusion']}")
        if ha["disagreements"]:
            L += ["", "| persona | system | item | human | judge | human critique | judge critique |", "|---|---|---|:-:|:-:|---|---|"]
            for d in ha["disagreements"]:
                L.append(f"| {d['persona_id']} | {d['system']} | {d['title'][:40] or d['item']} | {d['human']} | {d['judge']} | "
                         f"{d['human_critique'][:120]} | {d['judge_critique'][:160]} |")
    else:
        L += ["", "_Judge-vs-human agreement: no human labels yet (fill evals/labels/human_labels.csv, then re-run `uv run curriculum eval`)._"]
    spend = s.get("eval_cost_usd", 0)
    note = "" if spend else " (a --skip-judge run reuses the saved judge verdicts; what the judges cost is in EVAL.md's cost table)"
    L += ["", f"Eval LLM spend this run: ${spend:.2f}{note}" if "eval_cost_usd" in s else ""]
    return "\n".join(L) + "\n"
