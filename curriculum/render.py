"""Curriculum JSON -> Markdown a learner can read."""

from .models import Curriculum


def markdown(c: Curriculum) -> str:
    L = [f"# Curriculum: {c.goal}", ""]
    L.append(f"**Budget:** {c.budget_minutes} min · **Planned:** {c.total_minutes:.0f} min · **Videos:** {len(c.picks)} · "
             f"**Candidates assessed:** {c.pool_size}")
    L += ["", f"**How I read the goal:** {c.interpretation}"]
    if c.assumptions:
        L += ["", "**Assumptions:** " + "; ".join(c.assumptions)]
    if not c.feasible:
        L += ["", f"> **Not fully achievable in this budget.** {c.feasibility_note}"]
    for w in c.warnings:
        if w != c.feasibility_note:
            L.append(f"> ⚠️ {w}")
    L += ["", "## Plan", ""]
    for s in c.sub_topics:
        L.append(f"- **{s.title}** (`{s.id}`): {s.why}")
    L += ["", "## Watch in this order", ""]
    for p in c.picks:
        part = ""
        if p.watch_from or p.watch_until:
            part = f" · watch {p.watch_from or '0:00'}–{p.watch_until or 'end'}"
        L.append(f"### {p.rank}. [{p.title}]({p.url})")
        L.append(f"{p.channel} · {p.duration_min:.0f} min{part} · counts {p.minutes_counted:.0f} min · "
                 f"{p.level}, {p.format} · covers {', '.join(p.covers)} · **confidence {p.confidence:.2f}**")
        L += ["", p.reason, ""]
        for e in p.evidence:
            L.append(f"> [{e.t}] “{e.quote}”" + ("" if e.source == "transcript" else f" _(from {e.source}; no transcript)_"))
        L += ["", f"_Confidence note: {p.confidence_note}_", ""]
    if c.near_duplicates:
        L += ["## Similar videos: why only one made the cut", ""]
        for d in c.near_duplicates:
            L.append(f"- kept `{d.kept}` over `{d.dropped}` (both cover {', '.join(d.shared_topics)}): {d.why_kept}")
        L.append("")
    sel = [d for d in c.dropped if d.stage == "select"]
    if sel:
        L += ["## Considered and dropped", ""]
        for d in sel:
            L.append(f"- [{d.title}](https://www.youtube.com/watch?v={d.video_id}): {d.reason}")
        L.append("")
    other = [d for d in c.dropped if d.stage != "select"]
    if other:
        L += [f"<details><summary>Filtered before assessment ({len(other)})</summary>", ""]
        for d in other:
            L.append(f"- {d.title} ({d.stage}): {d.reason}")
        L += ["", "</details>", ""]
    L.append(f"_Models: {', '.join(f'{k}={v}' for k, v in c.models.items())} · cost ${c.cost_usd:.3f} · {c.latency_s:.0f} s_")
    return "\n".join(L) + "\n"
