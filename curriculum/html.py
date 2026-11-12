"""Curriculum runs -> a small static site: a home page with the test cases, one page per curriculum
(embedded players, the extract the model read, how the run scored), and an evaluation page.

No build step and no external assets except YouTube itself. Players are click-to-load (a thumbnail
until clicked), so a page with 7 picks doesn't start 7 iframes. Serve over http (`curriculum html
--serve`): YouTube refuses embeds from file:// pages, which send no referrer.
"""

from __future__ import annotations

import json
import re
import urllib.parse
from collections import Counter
from html import escape as e
from pathlib import Path

from .models import Curriculum

CSS = """
:root{--bg:#f6f7f9;--card:#fff;--ink:#16181d;--muted:#5d6472;--line:#e3e6eb;--accent:#2f6fde;--accent-soft:#e8f0fd;
--warn:#8a5a00;--warn-bg:#fff6e0;--bad:#b42318;--bad-bg:#fdecea;--ok:#18794e;--ok-bg:#e6f6ee;--chip:#eef1f5;--mark:#fff1a8;
--shadow:0 1px 2px rgba(16,24,40,.06),0 1px 3px rgba(16,24,40,.08)}
@media (prefers-color-scheme:dark){:root{--bg:#0f1115;--card:#171a21;--ink:#e8eaee;--muted:#9aa3b2;--line:#272c36;--accent:#7aa7ff;
--accent-soft:#1c2740;--warn:#f5c26b;--warn-bg:#2a2214;--bad:#ff8a80;--bad-bg:#2c1716;--ok:#5fd39a;--ok-bg:#122a1f;--chip:#222733;
--mark:#4a4214;--shadow:none}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
html,body{overflow-x:hidden;max-width:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
nav{position:sticky;top:0;z-index:5;background:var(--card);border-bottom:1px solid var(--line)}
nav div{max-width:980px;margin:0 auto;padding:10px 16px;display:flex;gap:18px;align-items:center;font-size:14px}
nav b{margin-right:auto}nav a.on{font-weight:600;color:var(--ink)}
main{max-width:980px;margin:0 auto;padding:24px 16px 64px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
h1{font-size:26px;line-height:1.25;margin:4px 0 6px}h2{font-size:18px;margin:34px 0 12px}h3{font-size:17px;line-height:1.35;margin:0}
h4{font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);margin:14px 0 6px}
.crumb{font-size:13px;color:var(--muted)}.muted{color:var(--muted)}.small{font-size:13px}
code{font:12px ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--chip);padding:1px 5px;border-radius:4px}
.stats{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0}
.stat{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;min-width:120px;box-shadow:var(--shadow)}
.stat b{display:block;font-size:20px}.stat span{font-size:12px;color:var(--muted)}
.bar{display:flex;height:12px;border-radius:6px;overflow:hidden;background:var(--chip);margin:6px 0 4px}
.bar i{display:block;height:100%;border-right:2px solid var(--card)}
.legend{font-size:12px;color:var(--muted)}
.box{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;box-shadow:var(--shadow)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media (max-width:760px){.two{grid-template-columns:1fr}}
.warn{background:var(--warn-bg);color:var(--ink);border-radius:10px;padding:10px 14px;margin:8px 0;font-size:14px}
.warn b{color:var(--warn)}.bad{border-left:4px solid var(--bad)}
.plan{counter-reset:s;list-style:none;padding:0;margin:0;display:grid;gap:8px}
.plan li{counter-increment:s;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px 10px 48px;position:relative}
.plan li:before{content:counter(s);position:absolute;left:14px;top:10px;width:22px;height:22px;border-radius:50%;background:var(--accent-soft);color:var(--accent);font-weight:600;font-size:13px;text-align:center;line-height:22px}
.chip{display:inline-block;background:var(--chip);border-radius:999px;padding:1px 9px;font-size:12px;margin:2px 4px 2px 0;color:var(--muted)}
.chip.c{background:var(--accent-soft);color:var(--accent)}.chip.ok{background:var(--ok-bg);color:var(--ok)}
.chip.no{background:var(--bad-bg);color:var(--bad)}.chip.w{background:var(--warn-bg);color:var(--warn)}
.pick{background:var(--card);border:1px solid var(--line);border-radius:14px;margin:0 0 18px;box-shadow:var(--shadow)}
.pick header{display:flex;gap:12px;padding:14px 16px 10px;align-items:flex-start}
.num{flex:none;width:30px;height:30px;border-radius:50%;background:var(--accent);color:#fff;font-weight:700;text-align:center;line-height:30px}
.meta{font-size:13px;color:var(--muted);margin-top:3px}
.body{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:16px;padding:0 16px 12px}
.body>div:first-child{align-self:start;position:sticky;top:56px}
@media (max-width:760px){.body{grid-template-columns:1fr}.body>div:first-child{position:static}}
.player{position:relative;aspect-ratio:16/9;background:#000;border-radius:10px;overflow:hidden}
.player iframe,.player button{position:absolute;inset:0;width:100%;height:100%;border:0}
.player button{cursor:pointer;padding:0;background:#000 center/cover no-repeat}
.player button:after{content:"";position:absolute;left:50%;top:50%;width:68px;height:48px;margin:-24px 0 0 -34px;border-radius:12px;background:rgba(0,0,0,.72)}
.player button:before{content:"";position:absolute;left:50%;top:50%;margin:-11px 0 0 -7px;border-style:solid;border-width:11px 0 11px 19px;border-color:transparent transparent transparent #fff;z-index:1}
.player button:hover:after{background:#e62117}
.range{font-size:12px;color:var(--muted);margin-top:6px}
.reason{margin:0 0 10px}
.conf{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--muted);margin-bottom:10px}
.conf .m{flex:1;height:6px;border-radius:3px;background:var(--chip);overflow:hidden}.conf .m i{display:block;height:100%}
blockquote{margin:0 0 8px;padding:6px 10px;border-left:3px solid var(--line);font-size:14px}
.ts{font:600 12px ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--accent-soft);color:var(--accent);border:0;border-radius:5px;padding:1px 6px;cursor:pointer;margin-right:6px}
blockquote small{color:var(--muted)}
.note{font-size:13px;color:var(--muted);font-style:italic;margin-top:8px}
details{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;margin:10px 0}
.pick details{margin:0 16px 14px;background:var(--bg)}
summary{cursor:pointer;font-weight:600}details ul{margin:8px 0 0;padding-left:18px}details li{margin:4px 0;font-size:14px}
.extract{max-height:420px;overflow:auto;margin-top:10px;font-size:13px;line-height:1.5}
.extract p{margin:0 0 6px}.extract .ch{color:var(--muted);font-weight:600}
mark{background:var(--mark);color:inherit;border-radius:3px;padding:0 2px}
.gap{color:var(--muted);text-align:center;font-size:12px;margin:8px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
.grid .box h3{margin-bottom:6px}.grid .box p{margin:6px 0;font-size:14px}
.card-tc{display:flex;flex-direction:column}.card-tc>p:last-of-type{margin-bottom:10px}
.cardbtns{margin-top:auto;display:flex;gap:8px;flex-wrap:wrap;padding-top:6px}
.btn-ghost,.btn-soft{font-size:13px;font-weight:600;padding:7px 13px;border-radius:9px;border:1px solid var(--line);white-space:nowrap}
.btn-ghost{color:var(--ink);background:var(--bg)}.btn-ghost:hover{text-decoration:none;border-color:var(--accent)}
.btn-soft{color:#fff;background:var(--accent);border-color:var(--accent)}.btn-soft:hover{text-decoration:none;opacity:.92}
.tbl{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow)}
table{border-collapse:collapse;width:100%;font-size:13px}
th,td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
th{font-weight:600;color:var(--muted);background:var(--bg)}
td:first-child{min-width:130px}tr:last-child td{border-bottom:0}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}
.y{color:var(--ok);font-weight:600}.x{color:var(--bad);font-weight:600}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:8px;margin:14px 0}
.steps div{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px;font-size:13px}
.steps b{display:block;font-size:14px;margin-bottom:2px}
.wk-list{display:grid;gap:10px}
.wk{display:flex;gap:12px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;box-shadow:var(--shadow)}
.wk-n{flex:none;width:26px;height:26px;border-radius:50%;background:var(--accent-soft);color:var(--accent);font-weight:700;text-align:center;line-height:26px;font-size:14px}
.wk-b{min-width:0}.wk-h{font-weight:600;margin-bottom:4px;display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
.why{margin-top:6px;font-size:13px;color:var(--muted);border-left:3px solid var(--line);padding-left:10px}
.why b{color:var(--ink)}
.tryform{display:grid;gap:10px;margin:14px 0}
.tryform label{display:grid;gap:4px;font-size:13px;font-weight:600;color:var(--muted)}
.tryform .row{display:grid;grid-template-columns:1fr 1fr;gap:10px}@media (max-width:600px){.tryform .row{grid-template-columns:1fr}}
.tryform input{font:inherit;font-weight:400;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:8px 10px;width:100%}
.tryform button{justify-self:start;background:var(--accent);color:#fff;border:0;border-radius:8px;padding:10px 18px;font:inherit;font-weight:600;cursor:pointer}
.tryform button:disabled{opacity:.6;cursor:default}
.run-stages{display:grid;gap:8px;margin:16px 0}
.run-stages div{display:flex;gap:10px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px}
.run-stages .dot{width:12px;height:12px;border-radius:50%;background:var(--chip);flex:none}
.run-stages .done .dot{background:var(--ok)}.run-stages .active .dot{background:var(--accent);animation:pulse 1s infinite}
@keyframes pulse{50%{opacity:.4}}
footer{margin-top:36px;font-size:12px;color:var(--muted)}
"""

JS = """
function play(el, start){
  const p = el.closest('.pick').querySelector('.player');
  const id = (p.dataset.id || '').replace(/[^A-Za-z0-9_-]/g, ''), end = p.dataset.end;
  const s = start ?? p.dataset.start;
  const q = new URLSearchParams({autoplay:'1', rel:'0', modestbranding:'1'});
  if (s) q.set('start', s); if (end && (start == null || +start < +end)) q.set('end', end);
  p.innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${id}?${q}" title="${(p.dataset.title || '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'})[c])}"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
    referrerpolicy="strict-origin-when-cross-origin"></iframe>`;
  p.scrollIntoView({block:'nearest', behavior:'smooth'});
}
"""

PALETTE = ["#2f6fde", "#16a34a", "#d97706", "#9333ea", "#0891b2", "#db2777", "#65a30d", "#dc2626", "#4f46e5", "#0d9488"]
BLOCKING = {"surface_intro", "outdated_tooling", "too_basic_for_learner", "too_advanced_for_learner",
            "off_topic", "wrong_language", "clickbait", "vlog", "equipment_review"}

# Layer-1 checks shown on the curriculum page, in reading order, with plain-English labels.
CHECKS = [
    ("no_hallucinated_videos", "Every pick is a real candidate"), ("budget_fit", "Fits the time budget"),
    ("utilisation_ok", "Uses enough of the budget"), ("pick_count_ok", "Sensible number of videos"),
    ("constraint_violations", "No pick breaks the learner's constraints"), ("language", "Right spoken language"),
    ("known_leakage", "Doesn't re-teach what the learner knows"), ("order_ok", "Prerequisites come first"),
    ("near_dup_respected", "No near-duplicate videos"), ("evidence_verified", "Every reason backed by a verified quote"),
    ("level_floor", "Not below the learner's level"), ("infeasibility_flagged", "Flags an impossible goal"),
    ("assumptions_stated", "States its assumptions"), ("has_dropped_list", "Explains what was dropped"),
    ("recency_ok", "Recent enough for this topic"), ("sitting_ok", "No sitting longer than the learner allows"),
    ("creators_ok", "Respects the creator limits"),
]
CRITERIA = ["tailored", "content_grounded_reasons", "goal_mirroring", "prereq_order_sensible", "constraints_respected",
            "budget_well_used", "dropped_reasons_sound", "overall"]
SYSTEMS = [("agent", "Fixed pipeline"), ("agent_loop", "Agent loop (tools)"),
           ("no_transcript", "Fixed, no transcripts"), ("top_n_by_views", "Top videos by views")]


def _secs(t: str | None) -> int | None:
    if not t:
        return None
    s = 0
    for part in t.split(":"):
        s = s * 60 + int(part)
    return s


def _label(s: str) -> str:
    return s.replace("_", " ")


def _page(title: str, body: str, depth: int = 0, active: str = "") -> str:
    up = "../" * depth
    nav = (f'<nav><div><b>Learning Curriculum Builder</b>'
           f'<a href="{up}index.html" class="{"on" if active == "home" else ""}">Test cases</a>'
           f'<a href="{up}how-it-works.html" class="{"on" if active == "how" else ""}">How it works</a>'
           f'<a href="{up}evaluation.html" class="{"on" if active == "eval" else ""}">Evaluation</a>'
           f'<a href="/chat" class="{"on" if active == "chat" else ""}">Chat ✨</a></div></nav>')
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="referrer" content="strict-origin-when-cross-origin"><link rel="icon" href="data:,">'
            f"<title>{e(title)}</title><style>{CSS}</style></head><body>{nav}<main>{body}</main>"
            f"<script>{JS}</script></body></html>")


def _yn(ok: bool | None) -> str:
    return "<span class='y'>✓</span>" if ok else ("<span class='x'>✗</span>" if ok is False else "<span class='muted'>–</span>")


# ---------------------------------------------------------------- pieces of the curriculum page

def _profile(persona: dict) -> str:
    ctx, ex = persona.get("user_context", {}), persona.get("expectations", {})
    chips = lambda xs, cls="": "".join(f"<span class='chip {cls}'>{e(x)}</span>" for x in xs)  # noqa: E731
    return ("<div class='two'><div class='box'><h4 style='margin-top:0'>Learner</h4>"
            f"<div>{e(ctx.get('background', ''))}</div>"
            f"<h4>Already knows</h4><div>{chips(ctx.get('known', []))}</div>"
            f"<h4>Wants to learn</h4><div>{chips(ctx.get('unknown', []), 'c')}</div>"
            + (f"<h4>Constraints</h4><div class='small'>{e(ctx['constraints'])}</div>" if ctx.get("constraints") else "")
            + "</div><div class='box'><h4 style='margin-top:0'>What this test case checks</h4>"
            f"<div class='small'>{e(ex.get('notes', ''))}</div>"
            + (f"<h4>Must not pick videos flagged</h4><div>{chips(map(_label, ex.get('forbidden_flags', [])), 'no')}</div>" if ex.get("forbidden_flags") else "")
            + (f"<h4>Minimum level</h4><div>{e(ex['min_level'])}</div>" if ex.get("min_level") else "")
            + (f"<h4>Pick count</h4><div>{ex['pick_count'][0]}–{ex['pick_count'][1]} videos</div>" if ex.get("pick_count") else "")
            + ("<h4>Expected</h4><div>says the goal is not achievable in the budget</div>" if ex.get("expect_infeasible") else "")
            + (f"<h4>Nothing older than</h4><div>{ex['min_upload_year']}</div>" if ex.get("min_upload_year") else "")
            + (f"<h4>Longest single sitting</h4><div>{ex['max_sitting_minutes']:.0f} min</div>" if ex.get("max_sitting_minutes") else "")
            + (f"<h4>Creators</h4><div>at most {ex['max_channels']} creators</div>" if ex.get("max_channels") else "")
            + (f"<h4>Per creator</h4><div>at most {ex['max_per_channel']} videos each</div>" if ex.get("max_per_channel") else "")
            + "</div></div>")


def _scores(result: dict, system: str = "agent_loop") -> str:
    if not result or system not in result.get("systems", {}):
        return "<div class='box muted'>Not evaluated yet. Run <code>uv run curriculum eval</code>.</div>"
    sysd = result["systems"][system]
    ch = sysd["checks"]
    hard = set(ch.get("hard_failures", []))
    rows = "".join(f"<tr><td>{_yn(ch.get(k))}</td><td>{e(lbl)}"
                   + (" <span class='chip no'>hard fail</span>" if k in hard else "")
                   + _check_detail(k, ch) + "</td></tr>" for k, lbl in CHECKS if k in ch)
    H = ["<div class='two'><div class='tbl'><table><tr><th></th><th>Automatic check</th></tr>" + rows + "</table></div><div>"]
    crit = {k: v for k, v in (sysd.get("rubric") or {}).items() if isinstance(v, dict) and "verdict" in v}
    if crit:
        H.append("<div class='tbl'><table><tr><th></th><th>AI grader criterion (click for its critique)</th></tr>"
                 + "".join(f"<tr><td>{_yn(v['verdict'] == 'pass')}</td><td><details style='margin:0;padding:0;border:0;background:none'>"
                           f"<summary style='font-weight:400'>{e(_label(k))}</summary><div class='muted small'>{e(v.get('critique', ''))}</div></details></td></tr>"
                           for k in CRITERIA if (v := crit.get(k)))
                 + "</table></div>")
        f = (sysd.get("faithfulness") or {}).get("reason_faithfulness")
        if f is not None:
            H.append(f"<div class='small muted' style='margin-top:6px'>Reason faithfulness: {f:.0%} of claims in the reasons are supported by the video's own text.</div>")
    else:
        H.append("<div class='box small muted'>The AI grader has not scored this run yet.</div>")
    H.append("</div></div>")
    return "".join(H)


def _check_detail(k: str, ch: dict) -> str:
    lst = {"constraint_violations": "constraint_violation_list", "level_floor": "below_level_list",
           "order_ok": "order_violation_list", "language": "language_violation_list", "known_leakage": "known_leak_list",
           "recency_ok": "too_old_list", "sitting_ok": "too_long_list", "creators_ok": "creator_issue_list"}.get(k)
    bad = ch.get(lst) if lst else None
    if k == "utilisation_ok" and ch.get("utilisation") is not None:
        return f"<div class='muted small'>{ch['utilisation']:.0%} of the budget used</div>"
    if bad:
        return f"<div class='muted small'>{e('; '.join(map(str, bad))[:300])}</div>"
    return ""


def _extract(windows: str, quotes: list[str]) -> str:
    """The evidence text the assessor read, with timestamps you can click and verified quotes highlighted."""
    out, prev = [], -1
    for line in windows.splitlines():
        m = re.match(r"\[(\d+:\d+(?::\d+)?)\]\s*(.*)", line)
        if not m:
            continue
        t, text = m.group(1), m.group(2)
        s = _secs(t) or 0
        is_ch = text.startswith("(chapter)") or text.startswith("(description)")
        if not is_ch and prev >= 0 and s - prev > 180:
            out.append("<div class='gap'>· · · skipped · · ·</div>")
        if not is_ch:
            prev = s
        body = e(text)
        for q in quotes:
            qe = e(q.strip().strip('"“”'))
            if len(qe) > 8:
                i = body.lower().find(qe.lower())
                if i >= 0:
                    body = body[:i] + "<mark>" + body[i:i + len(qe)] + "</mark>" + body[i + len(qe):]
        cls = " class='ch'" if is_ch else ""
        out.append(f"<p{cls}><button class='ts' onclick='play(this,{s})'>{e(t)}</button>{body}</p>")
    return "<div class='extract'>" + "".join(out) + "</div>"


def _source_chip(cand: dict | None, source: str | None) -> str:
    if not cand:
        return ""
    if cand.get("evidence_kind") == "transcript":
        if source == "gemini":
            return "<span class='chip ok'>read the transcript (Gemini transcription)</span>"
        kind = "auto-generated captions" if cand.get("transcript_generated") else "captions"
        via = " via Supadata" if source == "supadata" else " from YouTube"
        return f"<span class='chip ok'>read the transcript ({kind}{via})</span>"
    if cand.get("evidence_kind") == "metadata":
        return "<span class='chip w'>no transcript: read chapters + description</span>"
    return "<span class='chip no'>no evidence text</span>"


def _candidates(c: Curriculum, trace: dict, fx_pool: dict) -> str:
    picked = {p.video_id for p in c.picks}
    dropped = {d.video_id: d.reason for d in c.dropped if d.stage == "select"}
    rows = []
    for vid, a in (trace.get("assessments") or {}).items():
        cand = fx_pool.get(vid, {})
        status = ("<span class='chip ok'>picked</span>" if vid in picked else
                  "<span class='chip w'>considered</span>" if vid in dropped else "<span class='chip'>not picked</span>")
        flags = "".join(f"<span class='chip {'no' if f in BLOCKING else ''}'>{e(_label(f))}</span>" for f in a.get("red_flags", []))
        ev = {"transcript": "transcript", "metadata": "chapters"}.get(cand.get("evidence_kind"), "–")
        mins = round(cand["duration_s"] / 60) if cand.get("duration_s") else ""
        rows.append(f"<tr><td>{status}</td><td><a href='https://www.youtube.com/watch?v={e(vid)}' target='_blank' rel='noopener'>"
                    f"{e(cand.get('title', vid))}</a><div class='muted small'>{e(a.get('summary', '')[:220])}</div></td>"
                    f"<td class='n'>{mins}</td><td>{e(a.get('level', ''))}</td><td>{ev}</td><td>{flags}</td></tr>")
    if not rows:
        return ""
    return (f"<details><summary>Every candidate assessed ({len(rows)})</summary><div class='tbl' style='margin-top:10px'><table>"
            "<tr><th>Status</th><th>Video and what it teaches</th><th class='n'>Min</th><th>Level</th><th>Read</th><th>Red flags</th></tr>"
            + "".join(rows) + "</table></div></details>")


# ---------------------------------------------------------------- pages

def curriculum_page(c: Curriculum, persona_label: str = "", extra: dict | None = None) -> str:
    x = extra or {}
    persona, result, trace = x.get("persona") or {}, x.get("result") or {}, x.get("trace") or {}
    fx_pool, sources = x.get("fixture_pool") or {}, x.get("sources") or {}
    sub = {s.id: s.title for s in c.sub_topics}
    color = {p.rank: PALETTE[i % len(PALETTE)] for i, p in enumerate(c.picks)}
    used = min(1.0, c.total_minutes / c.budget_minutes) if c.budget_minutes else 0
    sys_key = "agent_loop" if c.mode == "agent_loop" else "agent"
    l1 = (result.get("systems", {}).get(sys_key, {}).get("checks", {}).get("hard_failures") if result else None)

    H = [f'<div class="crumb"><a href="../index.html">Test cases</a> · {e(persona_label)}</div>',
         f"<h1>{e(c.goal)}</h1>", f'<div class="muted">{e(c.interpretation)}</div>']
    H.append('<div class="stats">'
             f'<div class="stat"><b>{c.total_minutes:.0f} / {c.budget_minutes} min</b><span>planned / budget ({used:.0%})</span></div>'
             f'<div class="stat"><b>{len(c.picks)}</b><span>videos to watch</span></div>'
             f'<div class="stat"><b>{c.pool_size}</b><span>candidates read and assessed</span></div>'
             f'<div class="stat"><b>{"yes" if c.feasible else "partly"}</b><span>goal achievable in budget</span></div>'
             + (f'<div class="stat"><b class="{"y" if not l1 else "x"}">{"pass" if not l1 else "fail"}</b><span>automatic checks</span></div>' if l1 is not None else "")
             + "</div>")
    segs = "".join(f'<i style="width:{100 * p.minutes_counted / max(c.budget_minutes, c.total_minutes):.2f}%;background:{color[p.rank]}" '
                   f'title="{p.rank}. {e(p.title)} ({p.minutes_counted:.0f} min)"></i>' for p in c.picks)
    H.append(f'<div class="bar" role="img" aria-label="budget use">{segs}</div>'
             f'<div class="legend">Each colour is one video, in watch order; the grey remainder is unused budget.</div>')
    if not c.feasible and c.feasibility_note:
        H.append(f'<div class="warn bad"><b>Not fully achievable in this budget.</b> {e(c.feasibility_note)}</div>')
    notes = [w for w in c.warnings if w != c.feasibility_note]
    for w in notes[:2]:
        H.append(f'<div class="warn"><b>Note</b> · {e(w)}</div>')
    if notes[2:]:
        H.append(f"<details><summary>{len(notes) - 2} more notes</summary>"
                 + "".join(f'<div class="warn"><b>Note</b> · {e(w)}</div>' for w in notes[2:]) + "</details>")

    if persona:
        H.append("<h2>Test case</h2>" + _profile(persona))
    if result or persona:
        H.append("<h2>How this curriculum scored</h2>" + _scores(result, sys_key))
    if trace and trace.get("mode") == "agent_loop":
        H.append("<h2>How the agent loop built this</h2>" + agent_loop_walkthrough(c, trace, fx_pool))
    elif trace:
        H.append("<h2>How the agent built this, step by step</h2>" + pipeline_walkthrough(c, trace, fx_pool))

    H.append("<h2>Plan</h2>")
    if c.assumptions:
        H.append("<details><summary>Assumptions I made</summary><ul>" + "".join(f"<li>{e(a)}</li>" for a in c.assumptions) + "</ul></details>")
    H.append("<ol class='plan'>" + "".join(f"<li><b>{e(s.title)}</b><div class='muted small'>{e(s.why)}</div></li>" for s in c.sub_topics) + "</ol>")

    H.append("<h2>Watch in this order</h2>")
    for p in c.picks:
        start, end = _secs(p.watch_from), _secs(p.watch_until)
        rng = (f"Watch {p.watch_from or '0:00'} – {p.watch_until or 'end'} ({p.minutes_counted:.0f} of {p.duration_min:.0f} min)"
               if (p.watch_from or p.watch_until) else f"Watch all {p.duration_min:.0f} min")
        conf_col = "var(--ok)" if p.confidence >= 0.7 else ("var(--warn)" if p.confidence >= 0.45 else "var(--bad)")
        cand = fx_pool.get(p.video_id)
        asm = (trace.get("assessments") or {}).get(p.video_id, {})
        flags = [f for f in asm.get("red_flags", []) if f in BLOCKING]
        H.append(f'<article class="pick" id="p{p.rank}"><header><div class="num" style="background:{color[p.rank]}">{p.rank}</div><div>'
                 f'<h3><a href="{e(p.url)}" target="_blank" rel="noopener">{e(p.title)}</a></h3>'
                 f'<div class="meta">{e(p.channel)} · {p.duration_min:.0f} min' + (f" · {e(p.level)}" if p.level else "")
                 + (f" · {e(_label(p.format))}" if p.format else "") + "</div><div>"
                 + "".join(f'<span class="chip c">{e(sub.get(s, s))}</span>' for s in p.covers)
                 + _source_chip(cand, sources.get(p.video_id))
                 + "".join(f"<span class='chip no'>flagged {e(_label(f))}</span>" for f in flags) + "</div></div></header>")
        H.append('<div class="body"><div>'
                 f'<div class="player" data-id="{e(p.video_id)}" data-start="{start or ""}" data-end="{end or ""}" data-title="{e(p.title)}">'
                 f'<button aria-label="Play {e(p.title)}" onclick="play(this)" '
                 f'style="background-image:url(https://i.ytimg.com/vi/{e(p.video_id)}/hqdefault.jpg)"></button></div>'
                 f'<div class="range">{rng}</div></div><div>'
                 f'<p class="reason">{e(p.reason)}</p>'
                 f'<div class="conf">confidence <div class="m"><i style="width:{p.confidence * 100:.0f}%;background:{conf_col}"></i></div>{p.confidence:.2f}</div>')
        for ev in p.evidence:
            src = "" if ev.source == "transcript" else " <small>(chapters/description; no transcript)</small>"
            H.append(f'<blockquote><button class="ts" onclick="play(this,{_secs(ev.t) or 0})" title="Play from {e(ev.t)}">{e(ev.t)}</button>'
                     f"“{e(ev.quote)}”{src}</blockquote>")
        H.append(f'<div class="note">{e(p.confidence_note)}</div></div></div>')
        if cand and cand.get("windows"):
            what = "transcript extract" if cand.get("evidence_kind") == "transcript" else "chapters and description"
            H.append(f"<details><summary>What the model read ({what}, {len(cand['windows'].split()):,} words)</summary>"
                     + (f"<div class='small' style='margin-top:6px'><b>Assessment:</b> {e(asm.get('summary', ''))}</div>" if asm else "")
                     + "<div class='muted small' style='margin-top:4px'>Highlighted lines are the verified quotes; click a timestamp to play from there. "
                       "Long videos are read as an intro, spaced windows and the ending.</div>"
                     + _extract(cand["windows"], [ev.quote for ev in p.evidence]) + "</details>")
        H.append("</article>")

    if c.near_duplicates:
        H.append("<h2>Similar videos: why only one made the cut</h2><div class='box'><ul style='margin:0;padding-left:18px'>")
        for d in c.near_duplicates:
            H.append(f"<li>Kept <code>{e(d.kept)}</code> over <code>{e(d.dropped)}</code> (both cover {e(', '.join(sub.get(s, s) for s in d.shared_topics))}): {e(d.why_kept)}</li>")
        H.append("</ul></div>")
    sel = [d for d in c.dropped if d.stage == "select"]
    if sel:
        H.append(f"<h2>Considered and dropped</h2><div class='box'><ul style='margin:0;padding-left:18px'>"
                 + "".join(f'<li><a href="https://www.youtube.com/watch?v={e(d.video_id)}" target="_blank" rel="noopener">{e(d.title)}</a>: {e(d.reason)}</li>' for d in sel)
                 + "</ul></div>")
    if trace:
        H.append(_candidates(c, trace, fx_pool))
    other = [d for d in c.dropped if d.stage != "select"]
    if other:
        H.append(f"<details><summary>Filtered before assessment ({len(other)})</summary><ul>"
                 + "".join(f"<li>{e(d.title)} <span class='muted'>({e(d.stage)})</span>: {e(d.reason)}</li>" for d in other) + "</ul></details>")
    if trace.get("fixes"):
        H.append("<details><summary>Corrections the code made to the model's output</summary><ul>"
                 + "".join(f"<li>{e(f)}</li>" for f in trace["fixes"]) + "</ul></details>")
    H.append(f"<footer>Models: {e(', '.join(f'{k}={v}' for k, v in c.models.items()))} · cost ${c.cost_usd:.3f} · {c.latency_s:.0f} s · "
             f"<a href='curriculum.json'>curriculum.json</a> · <a href='curriculum.md'>curriculum.md</a> · <a href='trace.json'>trace.json</a></footer>")
    return _page(c.goal, "".join(H), depth=1)


STEPS = [("Plan", "sub-topics, queries, feasibility"), ("Discover", "YouTube search"), ("Hydrate", "details + transcripts"),
         ("Assess", "Haiku reads each video, quotes checked in code"), ("Dedup", "near-duplicates grouped"),
         ("Select", "Sonnet picks and orders"), ("Verify", "code checks ids, quotes, budget, red flags")]

# What the DEFAULT system (the agent loop) actually does, for the home page. It is a tool-using loop, not
# fixed stages: the model searches, reads and chooses turn by turn; grounding is still enforced in code.
AGENT_STEPS = [("Plan", "sub-topics & feasibility"), ("Search", "gather a candidate pool from YouTube"),
               ("Read", "transcripts — what each video actually teaches"), ("Choose", "pick & order, grounded in verified quotes"),
               ("Verify", "code checks the quotes, budget & red flags")]


def pipeline_walkthrough(c: Curriculum, trace: dict, fx_pool: dict) -> str:
    """Per-run, stage-by-stage account of what the agent did and why, from the trace and fixtures."""
    plan, asmts = trace.get("plan", {}), trace.get("assessments", {})
    timings, costs = trace.get("timings_s", {}), trace.get("cost_by_stage", {})
    pre = [d for d in c.dropped if d.stage != "select"]
    ev = Counter((fx_pool.get(v) or {}).get("evidence_kind") for v in asmts)
    n_tr, n_meta = ev.get("transcript", 0), ev.get("metadata", 0) + ev.get("none", 0)
    verified = sum(len(a.get("verified_quote_ids", [])) for a in asmts.values())
    quotes = sum(len(a.get("quotes", [])) for a in asmts.values())
    clusters = trace.get("dup_clusters") or []
    src = Counter()
    for v in asmts:
        k = (fx_pool.get(v) or {})
        if k.get("evidence_kind") == "transcript":
            src["transcript"] += 1

    def stage(n, name, t, cost, what, why):
        tc = (f" · {t:.0f}s" if t else "") + (f" · ${cost:.3f}" if cost else "")
        return (f"<div class='wk'><div class='wk-n'>{n}</div><div class='wk-b'><div class='wk-h'>{e(name)}"
                f"<span class='muted small'>{tc}</span></div><div>{what}</div>"
                f"<div class='why'><b>Why:</b> {why}</div></div></div>")

    S = []
    S.append(stage(1, "Plan", timings.get("plan"), (costs.get("plan") or {}).get("cost_usd"),
        f"Read the goal as: <i>{e(plan.get('interpretation',''))}</i> Learner level <b>{e(plan.get('learner_level',''))}</b>, "
        f"language <b>{e(plan.get('preferred_language',''))}</b>, feasible in budget: <b>{'yes' if plan.get('feasible') else 'no'}</b>. "
        f"Produced <b>{len(plan.get('sub_topics',[]))}</b> ordered sub-topics, <b>{len(plan.get('search_queries',[]))}</b> search queries"
        + (f", and {len(plan.get('title_exclusions',[]))} title exclusions from the constraints" if plan.get('title_exclusions') else "")
        + (f". Skipping what the learner knows: {e(', '.join(plan.get('skip_topics',[])))}" if plan.get('skip_topics') else "") + ".",
        "One model call turns a vague request into a checkable structure: ordered sub-topics with prerequisites drive everything downstream, "
        "and deciding feasibility now lets the agent tell an impossible goal (e.g. the CKA in 45 minutes) the truth instead of faking a plan."))
    S.append(stage(2, "Discover", timings.get("discover"), None,
        f"Ran the queries through YouTube and interleaved the results into a pool, then dropped <b>{len(pre)}</b> before spending any model on them "
        f"(too short, title excluded, or far longer than the budget). <b>{len(asmts)}</b> candidates went forward.",
        "Interleaving the queries stops one phrasing from dominating the pool, and the cheap prefilter (duration, title) removes obvious misses "
        "before the agent pays to read them."))
    S.append(stage(3, "Hydrate", timings.get("hydrate"), None,
        f"Fetched each candidate's details and transcript. <b>{n_tr}</b> had a usable transcript; <b>{n_meta}</b> fell back to chapters + description.",
        "The brief's whole point is that titles and views can't tell you fit, so the agent reads what each video actually says. When a transcript "
        "is unavailable it degrades to chapters and description and labels that evidence as weaker everywhere, rather than guessing."))
    S.append(stage(4, "Assess", timings.get("assess"), (costs.get("assess") or {}).get("cost_usd"),
        f"A cheap model read all <b>{len(asmts)}</b> candidates and recorded, per video: what it teaches, level, format, red flags, relevance to each "
        f"sub-topic, and verbatim quotes. Of <b>{quotes}</b> quotes the model offered, <b>{verified}</b> were found in the transcript by code and kept; the rest were discarded.",
        "Reading is the bulk of the work, so it uses the cheap model; judgement is saved for selection. Crucially, every quote is checked against the "
        "transcript <i>in code</i> — the model physically cannot cite evidence that isn't there, so grounding is a property of the system, not a hope."))
    S.append(stage(5, "Dedup", timings.get("dedup"), None,
        f"Grouped near-duplicate candidates (same topic, level and format) into <b>{len(clusters)}</b> cluster(s) using the labels already produced — no extra model calls.",
        "Two videos that teach the same thing the same way shouldn't both be picked. Doing this from existing topic labels (not embeddings) is free and "
        "explainable, and guarding by level/format keeps a beginner explainer and an advanced build from being wrongly merged."))
    picked_ids = {p.video_id for p in c.picks}
    S.append(stage(6, "Select", timings.get("select"), (costs.get("select") or {}).get("cost_usd"),
        f"The stronger model picked and ordered <b>{len({p.video_id for p in c.picks})}</b> video(s) against the plan, each with a reason citing verified "
        f"quote ids, a confidence score, optional watch ranges, and a dropped list. It used <b>{c.total_minutes:.0f}</b> of <b>{c.budget_minutes}</b> minutes.",
        "Only the ordering and justification need the strong model, and it works from compact cards, not raw transcripts. It may cite only quote ids that "
        "were verified upstream, so its reasons are grounded by construction."))
    fixes = trace.get("fixes") or []
    S.append(stage(7, "Verify & render", timings.get("verify"), None,
        f"Code enforced what the model can't be trusted with: every picked id is in the pool, only verified quotes are cited, and the counted minutes "
        f"add up. " + (f"<b>{len(fixes)}</b> correction(s) were applied to the model's output (e.g. the red-flag and budget rules)." if fixes else "No corrections were needed."),
        "The arithmetic and the hard rules (budget, valid ids, red-flag replacement) live in Python, not in a prompt, so they hold every time regardless "
        "of what the model returns."))
    return ("<div class='muted small' style='margin-bottom:10px'>The pipeline is fixed, not an agent loop: the task always needs "
            "search → read → choose, so fixed stages are cheaper, predictable, and every decision is traceable. Here is what each stage did for this test case.</div>"
            + "<div class='wk-list'>" + "".join(S) + "</div>")


def agent_loop_walkthrough(c: Curriculum, trace: dict, fx_pool: dict) -> str:
    """What the agent actually did: its tool calls turn by turn."""
    log = trace.get("tool_log") or []
    turns, read, pool = trace.get("turns", "?"), trace.get("videos_read", "?"), len(fx_pool) or len(trace.get("pool") or []) or c.pool_size
    cost = (trace.get("cost_by_stage", {}).get("agent_loop") or {}).get("cost_usd", c.cost_usd)
    H = ["<div class='muted small' style='margin-bottom:10px'>No stage order is hard-coded here: "
         "the model chose what to search for, which videos to read, and when to stop, through a tool-use loop. "
         "It read only what it needed — <b>" + f"{read}</b> of {pool} candidates — in <b>{turns}</b> turns.</div>"]
    H.append("<div class='stats'>"
             f"<div class='stat'><b>{turns}</b><span>turns (model calls)</span></div>"
             f"<div class='stat'><b>{read}</b><span>videos read (of {pool})</span></div>"
             f"<div class='stat'><b>{len([x for x in log if x['tool']=='search_youtube'])}</b><span>searches</span></div>"
             f"<div class='stat'><b>${cost:.3f}</b><span>cost</span></div></div>")
    # group the tool log by turn
    by_turn: dict[int, list] = {}
    for x in log:
        by_turn.setdefault(x["turn"], []).append(x)
    H.append("<div class='wk-list'>")
    for t in sorted(by_turn):
        items = by_turn[t]
        searches = [x["arg"] for x in items if x["tool"] == "search_youtube"]
        reads = [x["arg"] for x in items if x["tool"] == "read_video"]
        subs = [x for x in items if x["tool"] == "submit_curriculum"]
        parts = []
        if searches:
            parts.append("Searched: " + "; ".join(f"<i>{e(s[:70])}</i>" for s in searches))
        if reads:
            parts.append(f"Read {len(reads)} video(s): " + ", ".join(f"<code>{e(v)}</code>" for v in reads[:8])
                         + (" …" if len(reads) > 8 else ""))
        if subs:
            ok = subs[-1].get("ok")
            parts.append("<b>Submitted the curriculum.</b>" if ok else
                         "Tried to submit — the code rejected it (unread pick, unverified quote, or over budget) and asked the model to fix it.")
        H.append(f"<div class='wk'><div class='wk-n'>{t + 1}</div><div class='wk-b'>" + "<br>".join(parts) + "</div></div>")
    H.append("</div>")
    H.append("<div class='why' style='margin-top:12px'><b>Grounding is enforced, not requested:</b> the model's submitted picks are "
             "verified and assembled by library code — ids must exist in the pool, quotes must be verified against the transcript, and the "
             "budget must hold. The agent decides; the code keeps it honest.</div>")
    return "".join(H)


DECISIONS = [
    ("An agent loop, and it stays to defend its work", "The model drives search → read → choose itself, then remains in the conversation to answer 'why this video?' and to revise on request — with its real working context, not a reconstruction. Grounding is still enforced in code, so the openness costs nothing on correctness."),
    ("Read the transcripts, not titles or views", "The brief's premise is that popularity and titles don't tell you fit. Reasons must quote what is actually said. The 'no transcript' baseline in the eval measures what reading buys."),
    ("Quotes verified in code and cited by id", "The selector can only cite quote ids that code already found in the transcript, so a reason cannot be backed by invented evidence. Grounding is enforced, not requested."),
    ("Cheap model reads, strong model chooses", "~30 extraction calls per run go to the cheap model (Haiku); planning and selection, where judgement matters, go to Sonnet 5.5. The split is tested by the model comparison, not assumed."),
    ("Code owns the arithmetic and the hard rules", "Budget sums, valid ids, quote ids, red-flag replacement and the learner's stated limits (recency, sitting length, creators) are checked in Python. Models are unreliable at arithmetic and rule-following under pressure."),
    ("Dedup from topic labels, not embeddings", "Free, explainable, and guarded by level and format so a beginner explainer and an advanced build are not merged."),
    ("Degrade honestly when YouTube blocks transcripts", "Fall back to chapters and description, label that evidence as weaker everywhere, and don't work around the block with scrapers or proxies. A hosted provider on the user's own key can fill gaps if configured."),
    ("Judge from a different model family", "A model preferring its own outputs would inflate the scores, so OpenAI/Google models judge the Anthropic curator's picks, in both orders, with binary verdicts and critiques rather than drift-prone scores."),
]


def how_it_works_page() -> str:
    H = ["<h1>How it works</h1>",
         "<div class='muted'>A learning-curriculum agent: goal + time budget + learner profile in, an ordered, justified curriculum out. "
         "This page explains how the agent works, every design decision and why, and how it is evaluated.</div>",
         "<h2>The agent</h2>",
         "<div class='muted small' style='margin-bottom:10px'>A tool-using loop, not fixed stages. The model plans, then decides each move for "
         "itself — search, read, choose — over a bounded number of turns. Code, not the model, enforces the rules it can't be trusted with.</div>",
         "<div class='wk-list'>"]
    loop = [
        ("Plan", "From the learner profile it names 3–7 ordered sub-topics with prerequisites, judges whether the goal is feasible in the budget, "
                 "and narrates what it is about to do — the narration you see streaming live."),
        ("search_youtube(query)", "It issues its own queries — one per sub-topic, plus a project-style query that mirrors the goal — against a candidate "
                 "pool gathered from YouTube search (yt-dlp by default; the official Data API when a key is set). View count is returned but the prompt is explicit that popularity is not fit."),
        ("read_video(video_id)", "The only way to learn what a video teaches: a content summary, level, format, red flags, topics covered, and verbatim "
                 "quotes with ids and timestamps. It reads only as many as it needs to choose well — typically far fewer than the whole pool."),
        ("submit_curriculum(…)", "When the plan is covered it submits picks in watch order, each with the sub-topics it covers, a reason, the verified "
                 "quote ids backing that reason, an optional watch range, a confidence, and a list of strong candidates it read but dropped."),
        ("Verify (in code)", "Every submission runs the same guardrails as a code pipeline would: ids must be in the pool, only quotes verified against "
                 "the transcript may be cited, the budget must hold, flagged picks are replaced when an unflagged alternative exists, and the learner's "
                 "stated limits are applied. A submission that fails is handed back to the agent to fix."),
    ]
    for i, (name, d) in enumerate(loop, 1):
        H.append(f"<div class='wk'><div class='wk-n'>{i}</div><div class='wk-b'><div class='wk-h'><code>{e(name)}</code></div><div>{e(d)}</div></div></div>")
    H.append("</div>")
    H.append("<div class='box small'><b>Why a loop, not a chain?</b> The agent reads only what it needs, can back out of a dead end, and — because the "
             "model that built the curriculum is still in the conversation — it can defend each choice and revise on request with its real working context, "
             "not a reconstruction. Transcript grounding, quote verification, assessment and assembly are shared library code, so the loop is about "
             "<i>who decides</i>, never about cutting corners on the checks.</div>")
    H.append("<h2>Design decisions, and why</h2><div class='tbl'><table><tr><th>Decision</th><th>Why</th></tr>"
             + "".join(f"<tr><td><b>{e(dn)}</b></td><td>{e(why)}</td></tr>" for dn, why in DECISIONS) + "</table></div>")
    H.append("<h2>How it's evaluated</h2><div class='box'><p>Three layers, decided before looking at any output:</p>"
             "<ol><li><b>Deterministic checks</b> (no model): invented ids, budget overrun, constraint and red-flag violations, "
             "known-topic leakage, unverified quotes, level floor, language, and the learner's stated limits. Hard checks gate a pass.</li>"
             "<li><b>LLM judges from another model family</b>: a per-criterion rubric with written critiques, pairwise comparisons against both "
             "baselines in both orders, and a faithfulness check that each reason's claims are supported by the video's text.</li>"
             "<li><b>Human labels</b> (blind) to measure whether the judge can be trusted.</li></ol>"
             "<p class='small muted'>Two baselines run on the same candidate pool: the agent without transcripts, and the top videos by view "
             "count. See the <a href='evaluation.html'>evaluation page</a> for results.</p></div>")
    H.append("<h2>What it deliberately does not do</h2><div class='box small'><ul>"
             "<li>Measure teaching quality beyond what is said — pacing, audio and on-screen code are not seen.</li>"
             "<li>Work around YouTube's caption block with scrapers or proxies; it degrades to weaker evidence and says so.</li>"
             "<li>Promise a learner reaches the goal — every number is a proxy for 'a careful mentor would pick this'.</li></ul></div>")
    return _page("How it works", "".join(H), active="how")


def _try_form() -> str:
    return (
        "<h2 id='build'>Curate your own</h2>"
        "<form class='tryform box' method='get' action='/chat'>"
        "<div class='muted small' id='tf-note'>Describe a learner and press Build. The agent loop runs live and "
        "streams its work — searching, reading transcripts, choosing — into a chat on the left while the curriculum "
        "takes shape on the right. Then you can ask it why, or tell it to change things. "
        "Available when the site is served with <code>uv run curriculum serve</code>; a brand-new goal takes 1–2 minutes.</div>"
        "<label>Learning goal<input name='goal' required placeholder='Build a small React app this weekend, a habit tracker with local storage'></label>"
        "<div class='row'><label>Time budget (minutes)<input name='budget' type='number' min='15' max='3000' value='360' required></label>"
        "<label>Learner background<input name='background' placeholder='Python backend engineer, 5 years'></label></div>"
        "<div class='row'><label>Already knows (comma-separated)<input name='known' placeholder='JavaScript, HTTP, Git, npm'></label>"
        "<label>Wants to learn (comma-separated)<input name='unknown' placeholder='React, JSX, hooks, Vite'></label></div>"
        "<label>Constraints (optional)<input name='constraints' placeholder='Project-based; avoid 100-seconds intros; nothing before 2022'></label>"
        "<button type='submit'>Build it live →</button>"
        "</form>")


def index_page(rows: list[tuple[str, Curriculum, dict, dict, str]], summary: dict,
               mine: list[tuple[str, Curriculum]] | None = None) -> str:
    H = ["<h1>Learning Curriculum Builder</h1>",
         "<div class='muted'>Give it a learning goal, a time budget and a learner profile. An agent searches YouTube, reads the "
         "transcripts, and builds an ordered curriculum where every pick is justified by quotes from the video itself — then it "
         "stays to answer <b>why</b>, or to change the plan on request.</div>",
         "<div class='steps'>" + "".join(f"<div><b>{i}. {e(a)}</b><span class='muted'>{e(b)}</span></div>" for i, (a, b) in enumerate(AGENT_STEPS, 1)) + "</div>"
         + "<div class='small muted'>A tool-using agent that decides each step for itself. "
         "See <a href='how-it-works.html'>How it works</a> for the design, and the <a href='evaluation.html'>evaluation</a> for how it scores.</div>",
         _try_form()]
    H.append("<h2>Test cases</h2><div class='muted small' style='margin-bottom:10px'>Eight curated learners spanning the hard cases — a tiny budget, "
             "a non-English goal, an infeasible ask, an ambiguous one. <b>Open</b> any one to read the finished curriculum the agent built, "
             "with its reasons, caveats and scores. To build one for your own learner, use <a href='#build'>Build your own</a> below.</div><div class='grid'>")
    for rid, c, persona, result, suffix in rows:
        ctx = persona.get("user_context", {})
        ch = (result.get("systems", {}).get("agent", {}).get("checks", {}) if result else {})
        tr = ch.get("transcript_backed_share")
        H.append(f"<div class='box card-tc'><h3><a href='{e(rid)}{suffix}/curriculum.html'>{e(c.goal)}</a></h3>"
                 f"<p class='muted'>{e(ctx.get('background', ''))}</p>"
                 f"<p>{''.join(f'<span class=chip>{e(u)}</span>' for u in ctx.get('unknown', [])[:4])}</p>"
                 f"<p><span class='chip c'>{c.budget_minutes} min budget</span><span class='chip c'>{len(c.picks)} videos · {c.total_minutes:.0f} min</span>"
                 + ("" if tr is None else f"<span class='chip'>{tr:.0%} transcript-backed</span>")
                 + ("" if c.feasible else "<span class='chip w'>flags infeasible goal</span>") + "</p>"
                 + (f"<p class='small muted'>{e(persona.get('expectations', {}).get('notes', ''))}</p>" if persona else "")
                 + f"<div class='cardbtns'><a class='btn-ghost' href='{e(rid)}{suffix}/curriculum.html'>Open ↗</a></div>"
                 + "</div>")
    H.append("</div>")
    if mine:
        H.append("<h2>My curriculums</h2><div class='muted small' style='margin-bottom:10px'>Curriculums you built live in the agent, newest first.</div><div class='grid'>")
        for rid, c in reversed(mine):
            H.append(f"<div class='box card-tc'><h3><a href='{e(rid)}/curriculum.html'>{e(c.goal)}</a></h3>"
                     f"<p><span class='chip c'>{c.budget_minutes} min budget</span><span class='chip c'>{len(c.picks)} videos · {c.total_minutes:.0f} min</span>"
                     + ("" if c.feasible else "<span class='chip w'>flags infeasible goal</span>") + "</p>"
                     f"<div class='cardbtns'><a class='btn-ghost' href='{e(rid)}/curriculum.html'>Open ↗</a></div></div>")
        H.append("</div>")
    H.append("<footer>Generated by <code>uv run curriculum html</code> from runs/, test_set/ and evals/results/.</footer>")
    return _page("Learning Curriculum Builder", "".join(H), active="home")


def _pct(v) -> str:
    return "–" if v is None else f"{v:.0%}"


# The evaluation page presents the agent (the default system) against two baselines on the same candidate pools.
# The fixed-pipeline control-flow comparison is kept in the repo (EVAL.md, evals/results) as evidence, not here.
EVAL_SYSTEMS = [("agent_loop", "The agent"), ("no_transcript", "Without transcripts"), ("top_n_by_views", "Top videos by views")]


def evaluation_page(summary: dict, results: dict[str, dict], arch: dict | None = None) -> str:
    H = ["<h1>Evaluation</h1>",
         "<div class='muted'>Every test case is scored three ways: automatic checks in code (hard checks gate a pass), an AI grader from a "
         "different model family than the agent, and head-to-head comparisons in both orders. The agent is measured against two baselines on "
         "the same candidate pools — the same agent denied transcripts (does reading the content actually matter?), and the top videos by view "
         "count (is popularity enough?).</div>"]
    bs = summary.get("by_system", {})
    if bs:
        H.append("<h2>By system</h2><div class='tbl'><table><tr><th>System</th><th class='n'>Pass hard checks</th><th class='n'>Learning gaps covered</th>"
                 "<th class='n'>Budget used</th><th class='n'>Quotes verified</th><th class='n'>Redundancy</th><th class='n'>Grader pick pass</th>"
                 "<th class='n'>Faithfulness</th></tr>"
                 + "".join(f"<tr><td>{e(name)}</td><td class='n'>{e(str(s.get('layer1_pass', '–')))}</td><td class='n'>{_pct(s.get('unknown_coverage'))}</td>"
                           f"<td class='n'>{_pct(s.get('utilisation'))}</td><td class='n'>{_pct(s.get('quote_verifiability'))}</td>"
                           f"<td class='n'>{_pct(s.get('max_redundancy'))}</td><td class='n'>{_pct(s.get('judge_pick_pass_rate'))}</td>"
                           f"<td class='n'>{_pct(s.get('reason_faithfulness'))}</td></tr>"
                           for k, name in EVAL_SYSTEMS if (s := bs.get(k)))
                 + "</table></div><div class='muted small' style='margin-top:6px'>Transcripts earn their place: denied them, faithfulness and the "
                 "grader's pick-pass fall sharply. Picking by views alone passes almost nothing the grader accepts.</div>"
                 "<div class='box small' style='margin-top:10px'><b>Hard checks failed in at least one test case</b>"
                 + "".join(f"<div style='margin-top:6px'>{e(name)}: " + ("".join(f"<span class='chip no'>{e(_label(f))}</span>" for f in s.get('failures', [])) or "none")
                           + "</div>" for k, name in EVAL_SYSTEMS if (s := bs.get(k)))
                 + "</div>")
        if arch and arch.get("agent_loop"):
            al = arch["agent_loop"]
            H.append("<h2>Cost & shape of a run</h2><div class='tbl'><table><tr><th class='n'>Videos read (median)</th>"
                     "<th class='n'>Turns (median)</th><th class='n'>Cost per run (median)</th></tr>"
                     f"<tr><td class='n'>{al.get('reads','–')}</td><td class='n'>{al.get('turns','–')}</td><td class='n'>${al.get('cost',0):.3f}</td></tr>"
                     "</table></div><div class='muted small' style='margin-top:6px'>The agent reads only what it needs to decide, not the whole pool. "
                     "Cost here reuses cached per-video assessments; a from-cold run pays once to assess each video it reads — see the cost note in EVAL.md.</div>")
    if results:
        H.append("<h2>Per test case</h2><div class='muted small'>Pass/fail is the automatic hard checks, per system.</div>"
                 "<div class='tbl'><table><tr><th>Test case</th>"
                 + "".join(f"<th>{e(n)}</th>" for _, n in EVAL_SYSTEMS) + "</tr>")
        for pid, r in results.items():
            cells = []
            for k, _ in EVAL_SYSTEMS:
                ch = r.get("systems", {}).get(k, {}).get("checks", {})
                hard = ch.get("hard_failures")
                cells.append("<td>–</td>" if hard is None else "<td><span class='y'>pass</span></td>" if not hard
                             else f"<td><span class='x'>fail</span><div class='muted small'>{e(', '.join(map(_label, hard)))}</div></td>")
            link = f"{e(pid)}__agent_loop/curriculum.html" if "agent_loop" in r.get("systems", {}) else f"{e(pid)}/curriculum.html"
            H.append(f"<tr><td><a href='{link}'>{e(pid)}</a></td>{''.join(cells)}</tr>")
        H.append("</table></div>")
    crit = {k: bs[k].get("judge_criteria_pass_rate", {}) for k, _ in EVAL_SYSTEMS if k in bs}
    if any(crit.values()):
        H.append("<h2>AI grader pass rate per criterion</h2><div class='tbl'><table><tr><th>Criterion</th>"
                 + "".join(f"<th class='n'>{e(n)}</th>" for k, n in EVAL_SYSTEMS if k in crit) + "</tr>"
                 + "".join(f"<tr><td>{e(_label(c))}</td>" + "".join(f"<td class='n'>{_pct(crit[k].get(c))}</td>" for k, _ in EVAL_SYSTEMS if k in crit) + "</tr>" for c in CRITERIA)
                 + "</table></div>")
    stab = summary.get("stability_mean_jaccard")
    if stab is not None:
        H.append(f"<h2>Stability</h2><div class='box small'>Selection re-run 3 times on the same candidate pool: mean pairwise Jaccard "
                 f"of the pick sets is <b>{stab:.2f}</b> (1.0 = identical picks every time).</div>")
    ha = (summary.get("human_agreement") or {}).get("overall")
    if ha:
        c = ha.get("confusion", {})
        lo, hi = (ha.get("kappa_ci95") or [None, None])[:2]
        ha_html = (f"Every curriculum was also labelled pass/fail by a human from a blind sheet ({ha['n']} labels). "
                   f"Grader and human agree on <b>{_pct(ha['agreement'])}</b> of them "
                   f"(Cohen's κ <b>{ha['kappa']:.2f}</b>, 95% CI {lo:.2f}–{hi:.2f}; "
                   f"TPR {_pct(ha['tpr'])}, TNR {_pct(ha['tnr'])}). "
                   f"Of the disagreements, the grader was too lenient on {c.get('fp_judge_too_lenient', 0)} "
                   f"and too strict on {c.get('fn_judge_too_strict', 0)}; the full disagreement table is in "
                   f"evals/results/RESULTS.md.")
    else:
        ha_html = "Not measured yet: human labels are pending (evals/labels/human_labels.csv)."
    H.append("<h2>AI grader vs human labels</h2><div class='box small'>" + ha_html + "</div>")
    H.append("<footer>Full method and caveats: EVAL.md in the repository. Numbers from evals/results/.</footer>")
    return _page("Evaluation", "".join(H), active="eval")


# ---------------------------------------------------------------- write everything

def _load(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception:
        return {}


def extras_for(c: Curriculum, run_dir: Path, root: Path = Path(".")) -> dict:
    """Everything beyond curriculum.json that the page shows; each part is optional."""
    persona = next((p for f in sorted((root / "test_set").glob("*.json")) if (p := _load(f)).get("persona_id") == c.persona_id), {})
    fx = _load(root / "fixtures" / f"{c.persona_id}.json")
    cache = Path(__import__("os").getenv("CURRICULUM_CACHE", str(root / ".cache"))) / "transcripts"
    pool = {x["video_id"]: x for x in fx.get("pool", [])}
    return {"persona": persona, "result": _load(root / "evals" / "results" / f"{c.persona_id}.json"),
            "trace": _load(run_dir / "trace.json"), "fixture_pool": pool,
            "sources": {v: _load(cache / f"{v}.json").get("source") for v in pool}}


def _median(xs: list[float]):
    xs = sorted(xs)
    return xs[len(xs) // 2] if xs else None


def _arch_stats(runs_dir: Path) -> dict:
    """Median cost / videos-read / turns for the fixed pipeline and the agent loop, from their traces."""
    out = {}
    for mode, suffix in (("agent", ""), ("agent_loop", "__agent_loop")):
        costs, reads, turns = [], [], []
        for d in runs_dir.iterdir():
            if not d.name.endswith(suffix) or (suffix == "" and "__" in d.name):
                continue
            tr, cur = _load(d / "trace.json"), _load(d / "curriculum.json")
            if tr.get("mode") != mode:
                continue
            costs.append(cur.get("cost_usd", 0))
            reads.append(tr.get("videos_read", len(tr.get("assessments", {}))))
            if tr.get("turns"):
                turns.append(tr["turns"])
        if costs:
            out[mode] = {"cost": _median(costs), "reads": _median(reads)}
            if turns:
                out[mode]["turns"] = _median(turns)
    return out


def write_all(runs_dir: Path, root: Path = Path(".")) -> list[Path]:
    """(Re)write every curriculum page, the home page and the evaluation page. No LLM calls."""
    rows, written, results, mine = [], [], {}, []
    for d in sorted(runs_dir.iterdir()):
        f = d / "curriculum.json"
        if not f.exists() or "__" in d.name:  # baselines are eval inputs, not learner-facing
            continue
        c = Curriculum.model_validate_json(f.read_text())
        x = extras_for(c, d, root)
        (d / "curriculum.html").write_text(curriculum_page(c, d.name, x))
        written.append(d / "curriculum.html")
        # the agent loop is the default system, so the home card shows its curriculum and links to its page
        al = runs_dir / f"{d.name}__agent_loop" / "curriculum.json"
        card_c = Curriculum.model_validate_json(al.read_text()) if al.exists() else c
        rows.append((d.name, card_c, x["persona"], x["result"], "__agent_loop" if al.exists() else ""))
        if x["result"]:
            results[d.name] = x["result"]
    for d in sorted(runs_dir.glob("*__agent_loop")):  # regenerate the agent-loop variant pages (not index cards)
        f = d / "curriculum.json"
        if not f.exists():
            continue
        c = Curriculum.model_validate_json(f.read_text())
        (d / "curriculum.html").write_text(curriculum_page(c, d.name, extras_for(c, d, root)))
        written.append(d / "curriculum.html")
        if d.name.startswith("custom_"):  # the learner's own live builds, for the "My curriculums" list
            mine.append((d.name, c))
    summary = _load(root / "evals" / "results" / "summary.json")
    arch = _arch_stats(runs_dir)
    (runs_dir / "index.html").write_text(index_page(rows, summary, mine))
    (runs_dir / "evaluation.html").write_text(evaluation_page(summary, results, arch))
    (runs_dir / "how-it-works.html").write_text(how_it_works_page())
    return [runs_dir / "index.html", runs_dir / "how-it-works.html", runs_dir / "evaluation.html", *written]
