# Learning Curriculum Builder

Give it a learning goal, a time budget and a short learner profile. A tool-using **agent** searches YouTube, **reads the transcripts** of the candidates, and returns an ordered curriculum — then stays in the conversation to explain or revise it. Each pick comes with a reason grounded in what the video actually teaches, verbatim quotes with timestamps, and a confidence score. The output also lists the videos considered and dropped, and why near-duplicates were not both picked.

- Design decisions, with the reasoning behind each: [DECISIONS.md](DECISIONS.md)
- How the outputs were evaluated, results, and what the eval does not tell you: [EVAL.md](EVAL.md)

## Setup

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
cp .env.example .env          # then set OPENROUTER_API_KEY=...
```

Optional: set `YOUTUBE_API_KEY` (a Google Cloud API key with YouTube Data API v3 enabled) to use the official API for search and video details instead of yt-dlp. It reads public data only. A curriculum costs about 7 `search.list` calls and 1-2 `videos.list` calls (50 videos per call). (Its `caption` flag is not used to skip videos: it ignores auto-generated captions.) The Data API cannot return caption text for videos you don't own (`captions.download` requires edit permission on the video), so transcripts still come from `youtube-transcript-api`.

## Run

```bash
# the live agent + streaming chat UI — the product
uv run curriculum serve                               # http://localhost:8000

# the agent loop on the command line (one learner, or the whole test set)
uv run curriculum agentloop test_set/weekend_react_dev.json
uv run curriculum agentloop test_set/                 # reuses the saved pools in fixtures/

# the fixed-pipeline experiment it was measured against
uv run curriculum run test_set/ --offline
```

Each run writes `runs/<persona_id>/` (the agent loop writes `runs/<persona_id>__agent_loop/`):
- `curriculum.html`: the curriculum as a page, with an embedded player per video set to its watch range and clickable quote timestamps. `uv run curriculum html --serve` rebuilds every page plus `runs/index.html` and serves them at http://localhost:8000 (YouTube won't play embeds opened from `file://`).
- `curriculum.md`: the same curriculum as Markdown.
- `curriculum.json`: the same content, structured.
- `trace.json`: the plan, every candidate's assessment, dedup clusters, the raw selector output, cost per stage and timings.

Other commands:

```bash
uv run curriculum eval                    # score all runs, baselines and judges -> evals/results/RESULTS.md
                                          # to reproduce the committed verdicts, keep .env.example's
                                          # JUDGE_MODEL / FAITH_MODEL values (the round-2 Gemini judges)
uv run curriculum eval --skip-judge       # deterministic checks only (free)
uv run curriculum eval --stability 3      # also re-run selection 3x per persona to measure stability
uv run curriculum ask runs/weekend_react_dev "why not the 100-seconds React video?"
uv run curriculum compare --models anthropic/claude-sonnet-5.5 anthropic/claude-opus-5.5 openai/gpt-5.6-terra
uv run pytest
```

A persona file looks like this (see `test_set/`):

```json
{
  "persona_id": "weekend_react_dev",
  "goal": "Build a small React app this weekend, something like a habit tracker with local storage",
  "time_budget_minutes": 360,
  "user_context": {
    "background": "Python backend engineer, 5 years experience",
    "known": ["JavaScript fundamentals", "HTTP, REST, JSON", "Git, npm"],
    "unknown": ["React", "JSX", "Vite tooling", "React hooks", "Component patterns"],
    "constraints": "I prefer project-based content. Avoid pure-theory lectures and 'in 100 seconds' surface intros."
  },
  "expectations": { "...": "machine-checkable expectations used only by the eval" }
}
```

## How it works

The product is a **tool-using agent**. Given the learner and a budget, it works the problem with three tools and decides each step itself — there is no fixed script:

```
persona ─▶  the agent loops (bounded):                                   ─▶ curriculum
            search_youtube(q) · read_video(id) · submit_curriculum(…)
            its own queries     reads transcripts   one terminal call
                                                           │
                                                  code verifies before accepting:
                                                  ids in pool · quotes in transcript · budget holds
```

1. **Plan (in the loop).** The agent turns the profile into ordered sub-topics, prerequisites first, and decides what to search for. It narrates this to the learner as it goes.
2. **`search_youtube(query)`.** It issues its own queries — one per sub-topic, plus a project-style query that mirrors the goal — against a candidate pool. View count is returned but the prompt forbids picking on it: popularity is not fit.
3. **`read_video(id)`.** The only way to learn what a video teaches: a content summary, level, format, red flags, topics covered, and verbatim quotes with timestamps. The agent **must read a video before it may pick it**.
4. **`submit_curriculum(…)`.** When the plan is covered, it submits picks in watch order — each with the sub-topics it covers, a content-based reason, verified quote ids, an optional watch range, a confidence score, a dropped list and warnings. This one terminal call ends the loop.
5. **Verify — code, not the model.** The submission is checked in Python: every id must be in the pool, only quotes verified against the transcript may be cited, and the budget arithmetic must hold. An over-budget or ungrounded submission is rejected and the agent must fix it; on the last turn a logged trim enforces the budget. Grounding is a property of the code, not a hope.

Because it narrates each step, the chat UI (`curriculum serve`) streams the agent's reasoning and tool calls live while the curriculum takes shape. Afterwards it **stays in the conversation** — from the same working memory it built — to answer "why this video?" or to revise the curriculum on request. (That working memory lives in each run's `conversation.json`, which is not committed — build a curriculum first, in the UI or with `curriculum agentloop`, and the follow-ups work on that run.)

### The fixed-pipeline experiment

I also built the same task as a deterministic seven-stage pipeline — plan → discover → hydrate → assess → dedup → select → verify — and evaluated the two head to head. The loop matched it: a **3-2-3 pairwise tie**, identical quote grounding (1.0 verified), and higher judge scores on tailoring, constraints and budget use. The pipeline is a little cheaper and one Layer-1 pass stricter on hard constraints, so it stays in the repo as the experiment and the conservative comparison. Both run through the **same** candidate pool, the same per-video assessments and the same output checks, so the comparison isolates one thing: who decides the control flow — the code, or the model turn by turn. Details in [EVAL.md](EVAL.md); code in `curriculum/agent_loop.py` and `curriculum/pipeline.py`.

## Design decisions (short version; reasons in [DECISIONS.md](DECISIONS.md))

- **An agent loop, measured against a fixed pipeline.** The product is a tool-using agent (search → read → choose) that narrates its work and stays to revise it. I also built the deterministic seven-stage version and evaluated both: the loop tied it (3-2-3 pairwise) with equal quote grounding and higher judge scores on tailoring, constraints and budget use — so the loop's live reasoning and revisable output win. The pipeline stays as the experiment and the stricter-constraint comparison (`curriculum/pipeline.py`).
- **Read the transcripts.** The brief's point is that titles and views can't tell you fit. Reasons must quote what is said, and the `no_transcript` ablation in the eval measures what reading buys.
- **Quotes are verified in code and cited by id.** The selector physically cannot cite evidence that isn't in the transcript, so grounding is a property of the code, not a hope.
- **Cheap model reads, strong model chooses.** Haiku for ~30 extraction calls per run; Sonnet 5.5 for planning and selection, where judgment matters. Model choice is tested by `compare`, not assumed.
- **Code enforces what the learner ruled out.** A pick with a quality red flag is replaced when an unflagged video teaches the same sub-topic; if replacing it would leave the curriculum under 75% of the budget, it stays with a warning to the learner. Limits the learner states ("nothing before 2022", "90 minutes at a sitting", "two bakers at most") are hard rules for the selector and checked by the eval.
- **Code owns the arithmetic.** Budget sums, valid ids and quote ids are checked in Python, not trusted to the model.
- **Dedup from topic labels, not embeddings.** Free, explainable, and guarded by level and format so a beginner explainer and an advanced build aren't merged.
- **Strict JSON schema plus pydantic validation** on every call, with one repair retry and one retry for truncation.
- **Judges from a different model family** than the curator (OpenAI and Google judge Anthropic picks), to avoid self-preference bias.
- **When YouTube blocks transcripts, degrade honestly.** Use a hosted transcript provider if one is configured, otherwise fall back to chapters and description and label that evidence as weaker everywhere. No cookies, rotating proxies or scrapers of our own. Details in [DECISIONS.md](DECISIONS.md) (2.4).

## Models and providers

Defaults: Sonnet 5.5 plans and selects, Haiku 5.5 assesses; `.env.example` pins the judges to the Gemini models behind the committed verdicts (the code's fallback judge is an OpenAI model — stricter, see EVAL.md). All models are configurable in `.env`: `PLAN_MODEL`, `ASSESS_MODEL`, `SELECT_MODEL`, `JUDGE_MODEL`, `FAITH_MODEL` (OpenRouter-style ids). The models each evaluation round ran on are recorded in EVAL.md.

## Cost and latency

Measured from `trace.json` of the cold end-to-end runs of all 8 personas on 10 Nov 2026 (per-persona numbers in `evals/results/cold_run_costs.json`). Seven of the eight ran in metadata mode because YouTube's per-IP caption rate limit blocked transcripts that day (the degrade path in DECISIONS.md 2.4). The one transcript-backed run (`ambiguous_design_frontend`, 33 transcripts) cost $0.158 and took 138 s, inside the same range; its hydrate stage was the slowest at 49 s.

**Per curriculum: median $0.18 (range $0.16-0.20) and 123 s (range 103-139 s), cold.** (These are the fixed-pipeline experiment's cold runs. The **agent loop** — the product — costs a comparable amount: median **$0.13** over the cached pools, range $0.09–$0.32, the extra going to the model's own search/read decisions and its longer tool-use context; a cold run with live discovery for a brand-new goal is ~$0.37. It trades a little cost for live reasoning and a revisable result. Per-stage figures below are the pipeline's.)

| Stage | Calls | Cost (median) | Time (median) |
|---|--:|--:|--:|
| Plan | 1 | $0.016 | 11 s |
| Discover (yt-dlp search) | 0 | - | 3 s |
| Hydrate (details + transcript attempts) | 0 | - | 31 s |
| Assess | 33-36 | $0.043 | 27 s |
| Select | 1 | $0.116 | 46 s |

The selector is about two thirds of the cost, not the 36 assessments. That is the opposite of my estimate before building it: the selector's long structured output plus its reasoning tokens dominate. After the prompt tuning described in EVAL.md, selection alone measured a median of $0.12 and 50 s.

**10,000 curricula a day**, in order of impact:
1. **Cache assessments by video and prompt version** (already done locally). Learning goals are heavily repeated, so most candidates for popular topics will already be assessed. This removes most assess cost and about 25 s of latency.
2. **Shrink the selector's input and output.** Send compact cards instead of full ones, cap the dropped list at 5, and turn on prompt caching for the static instructions. The selector is the cost centre, so this is the biggest lever on the uncached path.
3. **Route by difficulty.** Small budgets with small pools can go to a cheaper selector; `compare` measures whether quality holds.
4. **Cache whole curricula** for identical (goal, budget, profile) inputs, and stream stage progress so ~60–110 s feels responsive.
5. **The non-LLM bottleneck is YouTube itself.** 10K runs a day is ~350K transcript fetches, which a single IP cannot do. Production needs an official or licensed data source for metadata and transcripts, plus a long-lived transcript cache. That is an infrastructure and contracts problem, not a prompt problem.

## What I'd do with more time (in priority order)

1. **A second human labeller and more labels.** Judge-human agreement on one labeller (who also built the system) and a few dozen items has a wide confidence interval; it is the weakest number in the repo.
2. **A real outcome signal.** A short check after each video ("did you get the app running?") would replace proxy metrics with whether the learner actually progressed.
3. **Outdated-content detection.** Explicitly check tools and versions in the transcript (Create React App vs Vite, React 17 vs 19) against the current state of the ecosystem. It is the most common way a good tutorial fails a learner today.
4. **Chapter-level picks as a first-class unit**, so a 3-hour course can serve a 30-minute budget well.
5. **A production data layer**: official API for metadata, a licensed transcript source, and a shared cache.
6. **A bounded second search round** when a sub-topic has no good candidate, instead of only warning about the gap.
7. **Playlist expansion** for huge budgets, and comment mining for "this no longer works" signals.

## Repository layout

```
curriculum/            the agent
  cli.py               serve | agentloop | run | eval | ask | compare | html
  agent_loop.py        the product: tool-using loop (search_youtube, read_video, submit_curriculum) + follow-up/revision
  server.py            showcase server: static site + live streaming chat ("build your own")
  pipeline.py          the fixed-pipeline experiment: stages end to end, writes outputs
  plan.py discover.py assess.py dedup.py selection.py render.py qa.py   (stages, shared by both)
  youtube.py           search, details, transcripts, windowing, cache
  verify.py            quote verification (rapidfuzz)
  llm.py               LLM client (OpenRouter): strict JSON schema, validation, retries, cost ledger
  html.py              static site: test cases, curriculum pages with players and extracts, evaluation
  models.py            pydantic schemas
  prompts/*.md         every prompt, readable without the code (agent_loop.md is the agent's system prompt)
evals/                 checks, baselines, judges, agreement, compare, results
test_set/              8 personas with expectations
fixtures/              saved candidate pools for offline reproduction
runs/                  outputs
tests/                 unit tests
```

## A note on the tag

`v1-submission` is amended in place rather than extended with commits: after first tagging I kept hardening the
submission — reviewer-found fixes with regression tests, the filled human-label sheet, and doc/artifact
consistency passes — and each revision replaced the commit so the tag always points at one coherent state.
EVAL.md records what changed and when; every number in it reproduces from the committed artifacts.
