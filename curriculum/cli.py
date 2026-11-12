"""Command line: `curriculum run|eval|ask|compare|html` (see README)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(prog="curriculum")
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="build a curriculum for one persona file (or a directory of them)")
    r.add_argument("persona", nargs="+")
    r.add_argument("--out", default="runs")
    r.add_argument("--offline", action="store_true", help="reuse the saved candidate pool in fixtures/ (no YouTube calls)")
    r.add_argument("--no-transcripts", action="store_true", help="ablation: assess from title/description only")
    r.add_argument("--select-model")
    r.add_argument("--assess-model")
    r.add_argument("--plan-model")

    e = sub.add_parser("eval", help="score saved runs and regenerate evals/results")
    e.add_argument("--personas", nargs="*")
    e.add_argument("--skip-judge", action="store_true")
    e.add_argument("--stability", type=int, default=0, help="re-run selection N times per persona to measure stability")

    a = sub.add_parser("ask", help="follow-up question about a saved run")
    a.add_argument("run_dir")
    a.add_argument("question")

    c = sub.add_parser("compare", help="compare selector models on the saved candidate pools")
    c.add_argument("--models", nargs="+", required=True)
    c.add_argument("--judge", default="google/gemini-3.8-flash")
    c.add_argument("--personas", nargs="*")

    h = sub.add_parser("html", help="write curriculum.html for every run plus runs/index.html (no LLM calls)")
    h.add_argument("--runs", default="runs")
    h.add_argument("--serve", type=int, nargs="?", const=8000, metavar="PORT",
                   help="then serve the pages at http://localhost:PORT (YouTube embeds don't play from file://)")

    al = sub.add_parser("agentloop", help="run the agent-loop variant (tool-using loop) on a persona or directory")
    al.add_argument("persona", nargs="+")
    al.add_argument("--out", default="runs")
    al.add_argument("--model")
    al.add_argument("--max-turns", type=int, default=40)

    db = sub.add_parser("db", help="optional MongoDB persistence (needs MONGODB_URI): stats | push | list")
    db.add_argument("action", choices=["stats", "push", "list"])

    sv = sub.add_parser("serve", help="showcase server: the static site plus a live 'build your own test case' form")
    sv.add_argument("--port", type=int, default=8000)

    args = ap.parse_args(argv)
    if args.cmd == "run":
        _run(args)
    elif args.cmd == "eval":
        from evals.run_eval import main as eval_main
        eval_main(args.personas, skip_judge=args.skip_judge, stability=args.stability)
    elif args.cmd == "ask":
        from .qa import ask
        print(ask(Path(args.run_dir), args.question))
    elif args.cmd == "html":
        _html(args)
    elif args.cmd == "agentloop":
        _agentloop(args)
    elif args.cmd == "db":
        _db(args)
    elif args.cmd == "serve":
        from .server import serve
        serve(args.port)
    elif args.cmd == "compare":
        from evals.compare import main as compare_main
        compare_main(args.models, args.judge, args.personas)


def _db(args) -> None:
    import json
    import os
    import sys

    from . import store
    from .models import Curriculum

    if not store.enabled():
        print("MongoDB is not configured or not reachable. Set MONGODB_URI in .env "
              "(and add your IP in Atlas → Network Access).", file=sys.stderr)
        return
    if args.action == "stats":
        print(json.dumps(store.stats(), indent=2, default=str))
    elif args.action == "list":
        for d in store.list_curricula():
            print(f"{d['persona_id']:32} {d['mode']:12} {d.get('n_videos','?')} videos  "
                  f"{d.get('total_minutes',0):.0f}/{d.get('budget_minutes','?')} min  ${d.get('cost_usd',0):.3f}")
    elif args.action == "push":
        n_cur = n_cache = 0
        for d in sorted(Path("runs").iterdir()):
            f = d / "curriculum.json"
            tr = d / "trace.json"
            if not f.exists() or not tr.exists():
                continue
            cur = Curriculum.model_validate_json(f.read_text())
            if store.save_curriculum(cur, json.loads(tr.read_text())):
                n_cur += 1
        for kind in ("assessments", "transcripts", "details", "search"):
            cdir = Path(os.getenv("CURRICULUM_CACHE", ".cache")) / kind
            if not cdir.exists():
                continue
            for cf in cdir.glob("*.json"):
                if store.cache_set(kind, cf.stem, json.loads(cf.read_text())):
                    n_cache += 1
        print(f"pushed {n_cur} curricula and {n_cache} cache entries to MongoDB ({store.DB_NAME})", file=sys.stderr)


def _agentloop(args) -> None:
    import sys

    from .agent_loop import run_agent_loop
    from .pipeline import load_persona

    paths: list[Path] = []
    for p in args.persona:
        pp = Path(p)
        paths += sorted(pp.glob("*.json")) if pp.is_dir() else [pp]
    for path in paths:
        persona = load_persona(path)
        out = Path(args.out) / f"{persona.persona_id}__agent_loop"
        print(f"→ {persona.persona_id} (agent loop)", file=sys.stderr)
        cur, trace = run_agent_loop(persona, model=args.model, out_dir=out, max_turns=args.max_turns)
        print(f"  {len({p.video_id for p in cur.picks})} videos, {cur.total_minutes:.0f}/{cur.budget_minutes} min, "
              f"{trace['turns']} turns, {trace['videos_read']} read, ${cur.cost_usd:.3f} → {out}/curriculum.md", file=sys.stderr)


def _run(args) -> None:
    from .pipeline import load_persona, run

    paths: list[Path] = []
    for p in args.persona:
        pp = Path(p)
        paths += sorted(pp.glob("*.json")) if pp.is_dir() else [pp]
    models = {k: v for k, v in {"plan": args.plan_model, "assess": args.assess_model, "select": args.select_model}.items() if v}
    mode = "no_transcript" if args.no_transcripts else "agent"
    for path in paths:
        persona = load_persona(path)
        out = Path(args.out) / (persona.persona_id if mode == "agent" else f"{persona.persona_id}__{mode}")
        print(f"→ {persona.persona_id} ({persona.time_budget_minutes} min)", file=sys.stderr)
        cur, _ = run(persona, models=models, use_transcripts=not args.no_transcripts, offline=args.offline,
                     out_dir=out, mode=mode)
        print(f"  {len(cur.picks)} videos, {cur.total_minutes:.0f}/{cur.budget_minutes} min, "
              f"${cur.cost_usd:.3f}, {cur.latency_s:.0f} s → {out}/curriculum.md", file=sys.stderr)


def _html(args) -> None:
    import functools
    import http.server

    from .html import write_all

    pages = write_all(Path(args.runs))
    print(f"wrote {len(pages)} pages; open {pages[0]}", file=sys.stderr)
    if args.serve:
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=args.runs)
        print(f"serving http://localhost:{args.serve}/  (Ctrl+C to stop)", file=sys.stderr)
        http.server.ThreadingHTTPServer(("127.0.0.1", args.serve), handler).serve_forever()


if __name__ == "__main__":
    main()
