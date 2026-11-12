# Evaluation

How I decided whether a curriculum is good, what was measured, the results, and what the numbers do not tell you. All tables are produced by `uv run curriculum eval` (raw output in [evals/results/RESULTS.md](evals/results/RESULTS.md), per-persona JSON next to it). The results below are the **final round of 10 Nov 2026 (round 2)**: harder test cases, three pipeline fixes, and a model change (see "Models in round 2"). The round-1 numbers are summarised at the end of that section for comparison, but they are not directly comparable.

## Read this first: what evidence each persona rests on

YouTube rate-limits caption requests from this laptop's network (`IpBlocked`, HTTP 429): the egress is a mobile carrier's shared (CGNAT) address. I did not work around the block with cookies, rotating proxies or scrapers; transcripts were collected through the fallback chain documented in DECISIONS.md 2.4 — the direct request where YouTube allowed it, a hosted caption provider (Supadata, existing captions only) where it refused, and budget-capped Gemini video transcription (now routed through the same OpenRouter key as every other LLM call) as the last resort. Every cached transcript records its source, and all three go through the same quote verification.

| Persona | Evidence the assessor read |
|---|---|
| `ambiguous_design_frontend` | **Transcripts**, 33/33 candidates |
| `career_switch_ml_foundations` | **Transcripts**, 36/36 |
| `go_dev_rust_ownership` | **Transcripts**, 36/36 |
| `hindi_excel_pivots` | **Transcripts**, 36/36 |
| `sourdough_first_loaf` | **Transcripts**, 36/36 |
| `weekend_react_dev` | **Transcripts**, 29/29 |
| `impossible_k8s_in_45` | Transcripts for 33/36; 3 on chapters + description |
| `lunch_break_sql_windows` | Transcripts for 28/35; 7 on chapters + description |

So 267 of the 277 committed candidates are transcript-backed. The 10 that are not fall back to chapters plus the full description, every quote from them is labelled as such in the output, and the `transcript-backed` column in RESULTS.md shows the share per curriculum.

## Method

Three layers, decided before looking at outputs (PLAN.md section 5; DECISIONS.md section 6).

1. **Deterministic checks (Layer 1, no LLM).** Read each persona's `expectations` block. Hard checks (fail the curriculum): invented video ids, budget overrun, constraint violations (forbidden title patterns, or red flags the learner ruled out), known-topic leakage, unverified or missing evidence quotes, project-based requirement, level floor, language, infeasibility flagged, assumptions stated, near-duplicate rule, and three added in round 2 for limits the learner states in their own words: **recency** (nothing uploaded before a year), **longest sitting** (no pick or watch range longer than N minutes) and **creator limits** (at most N creators, or N videos per creator). Soft checks (reported, not gated): budget utilisation in range, number of distinct videos in range, prerequisite order, dropped list present.
2. **LLM judges (Layer 2), from another model family than the curator.** The curator is Anthropic (Sonnet 5.5 plans and selects; Haiku assesses). The judges are Google in round 2:
   - Rubric (`google/gemini-3.1-pro`): pass/fail per criterion with the critique written first, plus per-pick pass/fail. The judge sees a reference summary of every picked video and is told when it came from chapters/description only.
   - Pairwise (`google/gemini-3.1-pro`): the agent against each baseline in both orders; if the orders disagree the result is a tie. Reasons are cut to 160 characters in both arms and dropped lists are hidden, so only the selection is compared.
   - Faithfulness (`google/gemini-3.7-flash`): splits each reason into claims and checks each against that video's evidence text.
3. **Human labels (Layer 3).** A blind sheet for me to label, to measure whether the judge can be trusted. All 32 `overall` rows are labelled; agreement is under "Judge vs human".

**Systems compared**, all on the same candidate pool:
- **`agent_loop`** — the product: the tool-using agent that drives its own search / read / choose loop and stays to revise (DECISIONS 1.1).
- `agent` — the fixed seven-stage pipeline, built as the experiment to test whether the model-driven loop costs quality. It shares the loop's pool, per-video assessments and output checks, so the two differ only in *who drives the control flow*.
- `top_n_by_views` — sort the pool by view count and fill the budget greedily (the brief's "search and view count" world).
- `no_transcript` — the pipeline, but the assessor sees only the title and the first 400 characters of the description (ablation: what reading the transcript buys).

**Models in round 2.** Plan and select ran on `claude-sonnet-5.5`, assess on **`claude-haiku-4.5`** — the committed fixtures record this per persona, and `--offline` reproduces from them as-is — judges as above (round 1 used `gpt-5.6-terra`/`-luna`). One asterisk: the committed `lunch_break_sql_windows` and `weekend_react_dev` agent-loop runs were rebuilt on 12 Nov with the current loop code, so those two personas were re-judged with `google/gemini-3.1-pro-preview` — OpenRouter now serves the round-2 rubric judge under that preview suffix, which is why RESULTS.md names it. (The committed traces log the loop's tool calls, not tool results, so "the loop now sees upload dates" is established by the code and its unit test, not by the trace.) To reproduce the committed verdicts, run the eval with `JUDGE_MODEL=google/gemini-3.1-pro-preview FAITH_MODEL=google/gemini-3.7-flash` — `.env.example` ships both; unset, the code defaults to the round-1 judge, which fails far more curricula. All curricula in this round were assessed and judged with the same models, so comparisons within the round are fair; comparisons with round 1 are not.

## Test cases (round 2)

Each persona gained one limit stated in the learner's own words, checked by code:

| Persona | Budget | Added in round 2 |
|---|--:|---|
| weekend_react_dev | 360 | nothing before 2022 (Vite, not create-react-app); at most 2 videos per creator |
| go_dev_rust_ownership | 240 | also needs idiomatic `Result`/`?` error handling (a new learning goal) |
| career_switch_ml_foundations | 1200 | at most 90 minutes per sitting: long courses must be split |
| hindi_excel_pivots | 90 | watches on a phone: nothing longer than 25 minutes at a time |
| impossible_k8s_in_45 | 45 | the CKA changed: nothing before 2023 |
| lunch_break_sql_windows | 30 | two videos at most |
| sourdough_first_loaf | 120 | follow at most two bakers' methods |
| ambiguous_design_frontend | 180 | include a real redesign or critique; nothing before 2020 |

## Results

### The product (agent loop) vs the fixed-pipeline experiment

The question to settle before shipping the loop: does letting the model drive the control flow cost quality versus deterministic stages? It does not. From the generated results (`evals/results/RESULTS.md`, `uv run curriculum eval`):

| | **agent_loop** (product) | agent (pipeline) | top_n_by_views | no_transcript |
|---|--:|--:|--:|--:|
| Layer-1 hard pass | 5/8 | **6/8** | 0/8 | 0/8 |
| Unknown-topic coverage | 1.0 | 1.0 | 0.9 | 1.0 |
| Budget utilisation | **0.74** | 0.72 | 0.93 | 0.67 |
| Quotes verified | 1.0 | 1.0 | 0.0 | 0.0 |
| Judge `overall` pass | **7/8** | 6/8 | 0/8 | 6/8 |
| Judge per-pick pass rate | **1.00** | 0.97 | 0.23 | 0.93 |
| Reason faithfulness | 0.93 | 0.95 | - | 0.79 |

Head to head (judge, both orders, disagreement = tie), from `RESULTS.md` (`agent_vs_agent_loop | 3 | 2 | 3`, read as pipeline-wins / loop-wins / ties): **pipeline 3, loop 2, 3 ties — a tie** at one sample per persona (n=8). On the judge's per-criterion rubric the loop scored **higher** on goal-mirroring (1.00 vs 0.88), constraints respected (1.00 vs 0.88) and the overall verdict (7/8 vs 6/8), and **equal** on tailoring, ordering, budget use and grounding (quotes verified 1.0). The pipeline's one clear edge is Layer-1 hard-constraint pass (6/8 vs 5/8). The failures on both sides are flagged-pick constraint violations — one flag class, owned under "Per persona" below — plus one recency slip by the loop with a root cause in code, not judgment: its `read_video`/`search_youtube` results omitted the upload date, so it could not check a floor it was told to respect (the tools now return `uploaded`). Both systems beat the two naive baselines on every quality axis.

**Conclusion.** The loop matches the deterministic pipeline on quality while adding what the pipeline cannot — live reasoning and a revisable, defendable result — so it is the product; the pipeline stays as the comparison and the stricter-constraint fallback.

### Per persona (fixed-pipeline run)

The full per-persona table — budget, picks, minutes, utilisation, transcript share, the Layer-1 verdict with the exact failed checks, judge verdicts, faithfulness, pairwise results, cost and latency — is generated into [evals/results/RESULTS.md](evals/results/RESULTS.md) by `uv run curriculum eval`; the committed copy is the authoritative record of the committed runs. What those numbers mean:

- **Every round-2 learner limit held in the pipeline run**: no pick older than its recency floor, no sitting over 90 or 25 minutes, creator caps respected, and Rust's added error-handling goal is covered. The Layer-1 failures below are flag and language violations, not the new limits.
- **`career_switch_ml_foundations` is the worst committed result, and it is kept as-is.** Both systems fail Layer 1 on it: the pipeline picked one Hindi-language video for an English learner (the `language` check) and both kept a `surface_intro`-flagged pick (`constraint_violations`), while filling only 359 of 1,200 minutes (utilisation 0.30) across 17 picks. The eval exists to surface this, not to hide it: a 20-hour foundations goal stretches a 36-video pool thin, and the selector under-fills rather than padding with flagged material — the right bias, overdone here.
- **The residual failure mode is one flag class.** Every remaining Layer-1 constraint failure in both systems (`career_switch`, `go_dev_rust_ownership`, and the loop's `impossible_k8s_in_45`) traces to a `surface_intro` pick. Round 2 deliberately moved that flag from an unconditional code gate to prompt guidance plus a replace-once rule (bug 4 below) because the hard gate starved budgets; the cost of the trade is a flagged pick leaking through in a minority of runs. Owning that rate — rather than silently re-gating — is the honest reading, and the next change is listed under "What I would change next".
- `lunch_break_sql_windows` passes every code check and the judge still fails it overall: the ablation's second video was a more focused window-functions tutorial. A fair call, and exactly the kind the human labels are for. (Its "two videos at most" limit is the soft `pick_count` check; it passed with 2.)
- `weekend_react_dev` uses 53% of 360 minutes (4 picks, 189 minutes). With the 2022 floor and the 2-per-creator cap there is not enough unflagged, recent React material in this 29-video pool; the curriculum says so in a warning.
- **Soft pick-count drift**: 5 of 8 pipeline runs land above the expected video-count band (11-17 picks where the expectation says 3-8), driven by budget-fill pressure and course slicing. Soft checks are reported, not gated; this is the next prompt iteration.

### By system

The headline by-system table is at the top of "Results"; the generated copy with the exact failed checks per system is in `RESULTS.md`. Judge pass rate per criterion (from `RESULTS.md`):

| Criterion | **agent_loop** (product) | agent (pipeline) | top_n_by_views | no_transcript |
|---|--:|--:|--:|--:|
| tailored | 1.00 | 1.00 | 0.12 | 1.00 |
| content_grounded_reasons | 1.00 | 1.00 | 0.00 | 0.88 |
| goal_mirroring | **1.00** | 0.88 | 0.75 | 1.00 |
| prereq_order_sensible | 1.00 | 1.00 | 0.12 | 0.88 |
| constraints_respected | **1.00** | 0.88 | 0.25 | 0.75 |
| budget_well_used | 1.00 | 1.00 | 0.00 | 0.88 |
| dropped_reasons_sound | 0.88 | 0.88 | 0.00 | 0.88 |
| overall | **0.88** | 0.75 | 0.00 | 0.75 |

Both naive baselines fail `evidence_verified` by construction (no verified quotes), so their 0/8 Layer 1 is not informative alone. `top_n_by_views` also fails the round-2 learner limits (recency, sitting length, creators), the language check and the near-duplicate rule. The ablation (`no_transcript`) clears the judge's overall bar on 6 of 8 — selection logic carries a lot — but its reasons are markedly less faithful (0.79 vs 0.93-0.95) and its per-pick pass rate lower (0.93 vs 0.97-1.00): what reading the transcript buys most is trustworthy, checkable reasons.

### Pairwise against the baselines (both orders; disagreement = tie)

| Comparison | Agent wins | Baseline wins | Ties |
|---|--:|--:|--:|
| agent vs `top_n_by_views` | 8 | 0 | 0 |
| agent vs `no_transcript` | 6 | 2 | 0 |

The agent's two losses to the ablation are `career_switch_ml_foundations` (the worst committed run, owned above) and `lunch_break_sql_windows` (one weaker second pick). One run per persona is too few to size the transcript advantage from pairwise alone; the faithfulness gap (0.95 vs 0.79) is the more robust signal.

### Stability and selector comparison (round 1)

These were measured in round 1 (before the round-2 test cases and models) and were not re-run. Selection re-run three times on the same pool: mean pairwise Jaccard of the pick sets **0.77** (three personas fully stable; `weekend_react_dev` least stable at 0.43). Selector comparison on four personas (Gemini 3.8 Flash pairwise judge, against Sonnet 5.5): Opus 5.5 0 wins / 2 ties / 2 losses at 1.6x the selection cost; Haiku 5.5 0/1/3 and failed Layer 1 once. Details: [evals/results/compare/COMPARE.md](evals/results/compare/COMPARE.md). One sample per persona: treat all single-run differences in this document as direction, not effect size.

## Bugs the eval found, and changes

### Round 1 (morning of 10 Nov)

1. **Metadata fallback with no metadata**: when both transcripts and the yt-dlp details call were blocked, candidates had empty evidence text; 6 of 7 metadata personas failed `evidence_verified`. Fixed (`discover.metadata_fallback`, unit test).
2. **Course slices silently dropped**: repeats of a video id were removed even with non-overlapping watch ranges, so `career_switch` counted 356 of 1,200 minutes while telling the learner 96%. Fixed (`selection._sanitize`, unit test).
3. **One round of selector prompt changes** (previous version in `evals/results/before_tuning/`): fill toward 75% before settling, treat quality flags as disqualifying when an unflagged alternative exists, 3-6 picks for a few hours. Layer 1 went from 5/8 to 7/8.

### Round 2 (afternoon of 10 Nov)

4. **Transcripts exposed a selector weakness.** With real transcripts the assessor flags far more problems, and the selector still filled slots with flagged videos (React and Rust both failed `constraint_violations`). **Code now enforces the rule**: if a pick carries a quality flag (`surface_intro`, `outdated_tooling`, `too_basic_for_learner`, ...) while an unflagged candidate teaches the same sub-topic, the selector is asked once to replace it; a pick still flagged after that is removed only if the curriculum keeps at least 75% of the budget, otherwise kept with a learner-facing warning (`selection.flag_conflicts`, unit test). My first version removed flagged picks unconditionally and cut React to 53 of 360 minutes, which is worse for a learner than a labelled stopgap.
5. **The assessor's "too basic" flag was wrong for newcomers.** It flagged beginner React courses as `too_basic_for_learner` for a senior Python engineer who knows no React, leaving 95 usable minutes in a 29-video pool. The assess prompt now defines the flag as "spends most of its time on things in the learner's KNOWN list"; React utilisation went from 0.18 to 0.73 on the same pool before the round-2 limits were added.
6. **Offline runs reused stale assessments (caching bug).** When a persona changed, `--offline` re-planned but reused assessments scored against the old plan's sub-topic ids, and never saved the new fixture, so every run re-planned again. Now saved assessments are reused only when the profile (hence the plan), the assess model and the assess prompt all match, and a re-assessment refreshes the fixture. Verified: a repeat offline run of `lunch_break_sql_windows` made one LLM call (selection) and no plan, assessment or YouTube calls. A later hardening: `--offline` now always reuses the committed assessments as-is — it exists to reproduce the committed artifacts — so only a live run re-assesses when the model or prompt changes.
7. **The video-count check counted sittings, not videos.** A course split into 90-minute sittings counted as many videos. It now counts distinct videos.

## What I would change next

- Make the red-flag rule respect explicit requests: a flag the learner did not rule out (sourdough's `surface_intro` on a "common mistakes" video) should not block a sub-topic the learner asked for by name.
- Re-run stability and the selector comparison on the round-2 configuration.
- Add a second labeller and label the 262 per-video rows: κ 0.80 from one labeller who also built the system is encouraging, not conclusive.
- Tame the soft pick-count drift (5 of 8 pipeline runs above the expected video-count band).

## Judge vs human

Labelled on 12 Nov from the blind sheet in `evals/labels/` (`LABEL_ME.md` to read, `human_labels.csv` holds the labels): all 32 `overall` rows, each curriculum judged against its persona as "would I hand this to this learner as is", with a one-line critique on every fail (20 pass / 12 fail). `uv run curriculum eval --skip-judge` (no LLM spend) computes agreement into RESULTS.md:

- **Agreement 0.91 (29/32), κ = 0.803 (95% CI 0.55-1.0), TPR 0.90, TNR 0.92** — the judge and I disagree on 3 of 32 curricula.
- The one case where the judge was **too lenient** is the most instructive: it passed the loop's `impossible_k8s_in_45` run, which I failed for including an architecture lecture of unverified (likely pre-2023) date against the learner's explicit nothing-before-2023 rule — the same recency blind spot whose root cause (the loop's tools omitted upload dates) is now fixed in code. The human layer caught what both the code checks of that run and the judge missed.
- The two cases where the judge was **too strict**: it failed the loop's `career_switch` run for not presenting a dropped-videos list (a format criterion I weighed less than the picks themselves), and failed the pipeline's `lunch_break` run for dropping a video the judge preferred — a defensible mentor-level quibble on a curriculum that meets every stated constraint.

Judge strictness still depends on the judge: round 1's `gpt-5.6-terra` failed the `overall` verdict for all 24 curricula, while round 2's Gemini judge passes 6-7 of 8 for the transcript-backed systems and 0 of 8 for the view-count baseline. The ranking of the systems is the same under both judges (and under my labels: the view-sorted baseline failed all 8 of mine too), which is the more robust signal; the absolute pass rates are judge-relative.

## What the evaluation does not tell you

- **Whether a learner gets to the goal.** There is no outcome data. Every number here is a proxy for "a careful mentor would pick this".
- **Teaching quality.** Even with transcripts, the pipeline sees what is said, not pacing, audio, on-screen code or whether the shown tool versions still work. Where only metadata was available (10 of the 277 committed candidates), it sees chapter titles and descriptions, which are partly marketing.
- **The transcript advantage rests on one ablation.** The claim that reading transcripts beats metadata is tested by `no_transcript` over the same pool, one run per persona; its strongest signal is the faithfulness of reasons, not different picks.
- **Generalisation.** Eight personas written by the author, with expectations written by the author. Hidden personas may hit cases the set misses (very thin topics, hands-on hardware skills, other languages).
- **Judge reliability.** The agreement above is one labeller, who also built the system, on 32 `overall` labels (the 262 per-video rows are unlabelled); κ = 0.80 on that n carries a wide confidence interval (0.55-1.0), and a labeller who wrote the rubric is not independent of it.
- **Discovery quality.** The checks measure selection given a pool. YouTube search is personalised and geo-dependent (this pool was built from India; a grader elsewhere gets a different one). `fixtures/` freezes my pool so results reproduce.
- **Noise.** One sample per persona per configuration. The stability numbers above show how much a re-run changes the picks.
- **Cost and latency** are provider prices on one day, from one laptop on one network. Round-2 offline runs report re-planning, re-assessment and selection, not discovery.

## Signals considered and discarded

| Signal | Why discarded |
|---|---|
| View count, likes | Ranks popularity, not fit (the brief's premise). Kept as the baseline to beat. |
| Like/view ratio | Needs a slow full extract per video; noisy at low views; rewards entertainment. |
| Comments | Slow to fetch, mostly praise, and would need another LLM pass per video. |
| Subscriber count | Brand bias against the small channel that builds exactly the right thing. |
| Upload recency as a score | Matters for React tooling, not for sourdough or SQL. Kept as an `outdated_tooling` flag from the content instead. |
| Words per minute as "density" | Measured 87-235 wpm; confounded by accent and auto-caption gaps. |
| Goal-to-transcript embedding similarity as the ranker | Favours keyword-dense overviews over long builds where the goal words are rare. |
| Likert (1-10) judge scores | Drift between runs and hide the failure mode; binary verdicts with critiques instead. |
| BLEU/ROUGE against a gold list | There is no single gold curriculum; two good ones share few videos. |
| A judge from the curator's family | Self-preference bias (Panickssery et al., 2024). |

## Cost of the evaluation

| Round | Item | Spend |
|---|---|--:|
| 1 | Cold re-runs, tuning, ablation, stability, judges, selector comparison (OpenRouter usage counter) | $8.28 |
| 2 | Transcript re-runs and flag-rule iterations (OpenRouter usage counter) | about $7.9 |
| 2 | 8 agent runs (re-plan, re-assess, select), from the traces | $3.49 |
| 2 | 8 `no_transcript` runs | $2.03 |
| 2 | Judges for 24 curricula (eval ledger) | $1.62 |
| 2 | Re-judging the two personas whose loop runs were rebuilt after the upload-date fix (eval ledger, 12 Nov) | $0.59 |
| 2 | Transcripts via the Supadata fallback (existing captions only) | 86 of 100 free credits |

The first test-set run on the morning of 10 Nov and interrupted runs are not included.
