"""Layer 3: how far can the LLM judge be trusted? Compare it with human labels.

Reports raw agreement, Cohen's kappa with a bootstrap 95% CI, and TPR/TNR with the human as ground
truth (raw agreement alone is misleading when most items pass)."""

from __future__ import annotations

import csv
import random
from pathlib import Path

FIELDS = ["persona_id", "system", "item", "title", "label", "critique"]


def kappa(a: list[int], b: list[int]) -> float | None:
    n = len(a)
    if n == 0:
        return None
    po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return 1.0 if pe == 1 else round((po - pe) / (1 - pe), 3)


def bootstrap_ci(a: list[int], b: list[int], iters: int = 1000, seed: int = 0) -> tuple[float, float] | None:
    if len(a) < 5:
        return None
    rng, ks = random.Random(seed), []
    idx = list(range(len(a)))
    for _ in range(iters):
        s = [rng.choice(idx) for _ in idx]
        k = kappa([a[i] for i in s], [b[i] for i in s])
        if k is not None:
            ks.append(k)
    ks.sort()
    return round(ks[int(0.025 * len(ks))], 2), round(ks[int(0.975 * len(ks)) - 1], 2)


def compare(human: list[int], judge: list[int]) -> dict:
    """1 = pass, 0 = fail. 'Positive' = pass."""
    tp = sum(h == 1 and j == 1 for h, j in zip(human, judge))
    tn = sum(h == 0 and j == 0 for h, j in zip(human, judge))
    fp = sum(h == 0 and j == 1 for h, j in zip(human, judge))
    fn = sum(h == 1 and j == 0 for h, j in zip(human, judge))
    n = len(human)
    return {
        "n": n,
        "agreement": round((tp + tn) / n, 2) if n else None,
        "kappa": kappa(human, judge),
        "kappa_ci95": bootstrap_ci(human, judge),
        "tpr": round(tp / (tp + fn), 2) if tp + fn else None,  # judge passes what the human passes
        "tnr": round(tn / (tn + fp), 2) if tn + fp else None,  # judge fails what the human fails
        "confusion": {"tp": tp, "tn": tn, "fp_judge_too_lenient": fp, "fn_judge_too_strict": fn},
    }


def read_labels(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as f:
        return [r for r in csv.DictReader(f) if r.get("label", "").strip().lower() in ("pass", "fail")]


def write_template(path: Path, rows: list[dict]) -> None:
    """Blank labelling sheet. Existing labels are kept so re-running the eval never wipes human work."""
    existing = {(r["persona_id"], r["system"], r["item"]): r for r in read_labels(path)}
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            key = (r["persona_id"], r["system"], r["item"])
            w.writerow(existing.get(key, {**r, "label": "", "critique": ""}))
