# Design decisions and the reasoning behind them

Each entry gives the decision, why it was made, what else was considered, and what evidence would
make me change it. The README has the one-paragraph version; this file is the long form.

---

## 1. Architecture

### 1.1 An agent loop, with a fixed pipeline built as the experiment

**Decision.** The product is a tool-using **agent loop**: a bounded loop (max turns) in which the model calls three tools — `search_youtube`, `read_video` and a terminal `submit_curriculum` — deciding for itself what to search, what to read and when to stop. It narrates each step, so the work streams to the learner live, and it stays in the conversation afterwards to explain or revise the curriculum from its own working memory. To check that a model-driven loop does not cost quality, I also built the same task as a deterministic seven-stage pipeline (plan → discover → hydrate → assess → dedup → select → verify) and evaluated the two head to head.

**Why the loop is the product.**
- **It can defend and change its own work.** The model that built the curriculum answers "why this video?" and revises on request with the real context it gathered — not a fresh call reconstructing intent from a trace. That conversation is the feature a learner actually wants, and the fixed pipeline cannot give it.
- **It held up in the eval.** Loop vs pipeline was a **3-2-3 pairwise tie**, with identical quote grounding (1.0 verified) and higher judge scores on tailoring, constraints and budget use. The loop is not the flashier-but-worse option here; it matched the deterministic system on quality (see [EVAL.md](EVAL.md)).
- **The expensive guarantees are kept the same way in both.** Grounding, valid ids and the budget are enforced in code at `submit_curriculum`, exactly as the pipeline enforces them at its verify stage — so the loop's freedom never reaches the output unchecked (see 4.1, 4.2).

**What the pipeline experiment showed (why it stays in the repo).** Fixed stages are a little cheaper, one Layer-1 pass stricter on hard constraints, and every stage writes inspectable output to `trace.json` so a failure is easy to localise (bad queries? bad assessment? bad selection?). Those are real advantages, and for a batch job with no human in the loop they might tip the choice — which is exactly why the pipeline stays as the comparison and the conservative fallback, not dead code. Both systems share all of their data (the same candidate pool and per-video assessments) and all of their output checks, so the eval isolates exactly one variable: who drives the control flow, the code or the model.

**Alternatives.** LangChain or LlamaIndex for the loop: rejected, because a hand-rolled loop in plain Python with pydantic (mirroring how our inference service runs its own tools) is easier to read and to bound than framework glue. An unbounded agent: rejected — the loop is capped and `submit_curriculum` is its only exit.

**Would change if.** A deployment were a pure batch job with no follow-up conversation and a hard cost ceiling; then the pipeline's predictability and slightly lower cost would make it the better default. The eval is set up to keep that call honest.

### 1.2 Plan first, then select against the plan

**Decision.** A planning call turns the learner profile into ordered sub-topics with prerequisites and time shares, search queries, title exclusions, topics to skip, an explicit feasibility verdict and stated assumptions. The selector chooses videos *against* that plan.

**Why.**
- Search queries written from the learner's gaps beat searching the raw goal. "Build a habit tracker in React" finds project builds; "learn React" finds 100-second explainers.
- The plan makes tailoring checkable: coverage of the learner's `unknown` list and leakage into their `known` list are measured against it.
- Feasibility and assumptions are decided once, up front, where they belong (`impossible_k8s_in_45`, `ambiguous_design_frontend`).

**Alternatives.** Rank videos directly from the goal (a single "select" call). Kept as a planned ablation in the model/prompt comparison.

### 1.3 Read the content: transcripts are the core evidence

**Decision.** Every candidate is assessed from its transcript (windowed, see 2.2). Titles, views and channel names are never treated as evidence of what a video teaches.

**Why.** The brief's central point is that search and view count don't solve this problem, and that reasons must reference *content*. The only way to know a video builds a habit tracker with `localStorage`, or uses Vite rather than `create-react-app`, is to read what is said.

**Alternatives.** Assess from title and description only. That is exactly the `no_transcript` ablation in the eval, kept to measure what reading the content buys.

---

## 2. Data sources

### 2.1 yt-dlp search and youtube-transcript-api; no YouTube Data API key

**Decision.** Search with `yt-dlp` in flat mode. Get details (chapters, upload date, full description) with a full `yt-dlp` extract. Get transcripts with `youtube-transcript-api`.

**Why.**
- The official Data API cannot download captions of videos you don't own (`captions.download` needs the owner's OAuth scope), so it cannot do the core job.
- Its search quota (100 searches/day on the free tier) is too small for development, let alone the eval.
- yt-dlp flat search was measured at 1–2 s per query with no key and returns duration, views, channel and description.

**Alternatives.** Data API for metadata only. It is the right choice at production scale and is listed in the README's "with more time".

### 2.2 Window transcripts before any LLM call

**Decision.** Videos up to 25 minutes are passed whole. Longer ones get the first 4 minutes, 10 evenly spaced 90-second windows and the last 2 minutes. Chapter markers are added when the video has them. Every line keeps an `[mm:ss]` timestamp, and the total is capped at 5,000 words.

**Why.**
- Measured: ~171 spoken words per minute, and a single 11.5-hour course was 86k words. Sending whole transcripts would cost ~15× more and slow the assess stage.
- The intro says what will be built, evenly spaced windows show what is actually taught, and the ending shows what got built. Together they are enough to judge fit.
- Timestamps let every quote be verified and cited, and let the selector recommend a watch range.

**Trade-off.** Something taught only between windows can be missed. That is acknowledged in EVAL.md; chapters reduce the risk where they exist.

### 2.3 Drop wrong-language videos before assessment

**Decision.** Only download a transcript in the learner's language. If a video only has captions in another language, drop it with the stage `language` and a reason.

**Why.** Searching from an Indian IP returned ~10 of 36 candidates in Hindi for English queries. Assessing them costs money, and recommending them is wrong for an English learner. The same rule makes `hindi_excel_pivots` work in the other direction.

### 2.4 When YouTube blocks transcripts: degrade honestly instead of working around it

**What happened.** Halfway through development YouTube started answering HTTP 429 (`IpBlocked`) for caption requests from this laptop's IP. Search and video details kept working.

**Decision.**
- A circuit breaker stops asking for transcripts after 3 consecutive blocks instead of hammering the endpoint, because retrying extends a block.
- Two optional hosted fallbacks sit between the direct request and the metadata degrade, each tried only when configured (its key, or its spend cap) and the direct request was refused: **Supadata** (existing captions only, one credit per video, capped by `SUPADATA_MAX_CREDITS`) and, as a last resort, **Gemini video transcription** — a Gemini model fetches the video by URL and transcribes it (an official model feature), called through the same OpenRouter client and key as every other LLM call in the project, enabled and hard-capped by `GEMINI_MAX_USD`. If that route fails (at full media resolution a video past roughly an hour overflows the model's context) and a `GEMINI_API_KEY` is set, the same model is tried once more on Google's own API at low media resolution — the very last backoff in the chain, charged against the same cap. A transcript from either is cached with its `source` recorded and goes through exactly the same quote verification as a direct one.
- Each candidate falls back to *metadata evidence*: its chapter list plus the full description. If the details call is refused as well (yt-dlp's bot check), the search-result snippet is used, and a candidate with no text at all is marked `none` rather than `metadata`. Its `evidence_kind` is recorded as `metadata`, and quotes from it are labelled "from chapters/description; no transcript" in the output.
- The selector is told this is weaker evidence. The eval reports `transcript_backed_share` so a reader can see how much of a curriculum rests on real transcripts.
- Transient failures are never cached, so the next run on an unblocked network fetches real transcripts automatically.
- I did not add proxy rotation or browser scraping to get around the block. It would be fragile, it is against the spirit of the rate limit, and a reviewer should not need it to run the project.

**How the reviewer is protected.** The candidate pools and assessments for the test set are committed in `fixtures/`, so `curriculum run --offline` and `curriculum eval` reproduce the published results with no YouTube access at all.

**At scale.** Ten thousand curricula a day means hundreds of thousands of transcript fetches. That needs a licensed or official data source and a long-lived transcript cache, not a laptop scraper. It is covered in the README's cost section.

---

## 3. Models

### 3.1 A different model per stage, chosen by what the stage needs

| Stage | Model | Reasoning |
|---|---|---|
| Plan | `anthropic/claude-sonnet-5.5` | One small call that needs judgment about prerequisites, feasibility and ambiguity. |
| Assess | `anthropic/claude-haiku-5.5` | ~30 calls per run of extraction work (topics, level, quotes). At $0.10/M input it costs a few cents per run; a stronger model buys little for extraction. |
| Select | `anthropic/claude-sonnet-5.5` | The one place where taste matters: trading off coverage, budget and redundancy, and writing reasons a learner trusts. Opus 5.5 is 2× the price; whether it is better is measured by `compare`, not assumed. |
| Judge (rubric, pairwise) | `openai/gpt-5.6-terra` | A different model family from the curator, because LLM judges favour their own family's outputs (Panickssery et al., 2024). |
| Faithfulness | `openai/gpt-5.6-luna` | A narrow "is this claim supported by this text?" task; cheap and from a different family. |
| Comparison judge | `google/gemini-3.8-flash` | Used when an OpenAI model is a contestant, so no contestant is judged by its own family. |

All calls go through OpenRouter as the brief asks.

### 3.2 Strict JSON schema plus pydantic validation on every call

**Decision.** Each call sends a strict `json_schema` generated from a pydantic model, with `provider.require_parameters` so OpenRouter only routes to endpoints that honour it. The reply is validated again with pydantic. A malformed reply gets one retry with the validation error attached. A reply truncated by the token limit gets one retry with double the limit.

**Why.** Some providers treat the schema as a hint, not a guarantee. Validation in code makes every downstream stage able to trust its inputs. The truncation retry exists because these models' built-in reasoning tokens count against `max_tokens`, which truncated the selector during development.

### 3.3 No temperature parameter; stability is measured instead

**Why.** Sonnet/Haiku/Opus 5.5 and the GPT-5.6 models reject `temperature` on OpenRouter (requests returned "No endpoints found"). Even where it is accepted, temperature 0 is not deterministic. So `curriculum eval --stability N` re-runs selection on the same pool and reports how much the picks change.

---

## 4. Making the reasons trustworthy

### 4.1 Quotes are extracted once, verified in code, and cited by id

**Decision.**
1. The assessor extracts 2–4 verbatim quotes per video, each with an id and a timestamp.
2. Code checks every quote against the transcript text (rapidfuzz `partial_ratio ≥ 85` over 3-line spans). It prefers matches near the claimed time and corrects the timestamp if the words exist elsewhere.
3. Unverified quotes are removed *before* the selector sees the candidate.
4. The selector can only cite quote *ids*, and `_sanitize` removes any id that isn't verified.

**Why.** A model asked to "justify with evidence" will happily invent plausible quotes. Making it impossible to cite unverified text turns "grounded reasons" from a hope into a property of the code, and `evidence_verified` becomes a hard check in the eval.

**Why fuzzy matching.** Auto-captions have no punctuation, and models normalise casing and fillers. Exact matching rejected real quotes during testing; 85 was the lowest threshold that still rejected invented sentences in the unit tests.

### 4.2 The code owns the arithmetic

**Decision.** The selector proposes picks and optional watch ranges; the code computes minutes. If the total is over budget, the selector gets one corrective call with the exact overrun. If it is still over, the lowest-confidence picks are removed and the trim is logged in `fixes`.

**Why.** Models are unreliable at adding durations. Budget fit is the most basic promise to the learner, so it is enforced in code and recorded rather than hoped for.

**Course slices.** A long course may appear more than once, as picks with non-overlapping watch ranges (its basics early, its CNN chapters later). Any other repeat of a video is dropped and logged. Before this rule existed the code dropped every repeat, so a 20-hour curriculum counted 356 minutes while the selector told the learner it used 96% of the budget; the eval caught it (EVAL.md).

### 4.3 The budget means viewing time

**Decision.** Prompts say the budget is time spent watching, and selection should use 75–95% of it. Watch ranges count only the range.

**Why.** Early runs left most of the budget unused because the planner was saving time for practice. The reference "good output" uses about 5 of 6 hours of video, which is what the brief expects.

### 4.4 Prefer a few substantial videos over many fragments

**Decision.** The selector is told that each extra video must cover a gap the others leave open.

**Why.** An early run picked 8 videos (two todo apps, two props explainers and a separate localStorage video). Each switch to a new creator means a new project setup, folder structure and style, which costs a weekend learner real time. This is a general rule about learning, not a rule tuned to the reference persona; the pick-count expectation in each persona file is what checks it.

### 4.5 Legibility: dropped list, near-duplicates, confidence

**Decision.** Every curriculum includes the videos considered and dropped, each with a reason and a stage. It also includes the near-duplicate pairs, with why one was kept, and a confidence score plus note for each pick.

**Why.** The brief asks for exactly this. In practice it is also what lets a learner ask "why not X?", and the `ask` command can answer that from the saved trace.

---

## 5. Dedup without embeddings

**Decision.** Two candidates are near-duplicates when their assessed topic lists overlap strongly (a fuzzy Jaccard ≥ 0.6, with labels matched fuzzily so "usestate hook" ≈ "usestate"), *and* they are at the same level, *and* they are in the same format family. The selector keeps at most one per cluster and must explain which and why.

**Why.**
- It costs nothing: the topic lists already exist from assessment.
- It is explainable ("both cover: Vite setup, useState, localStorage").
- The same-level and same-format guards stop false merges. A beginner explainer and an advanced build can share topics without being duplicates, and a learner may need both.

**Alternatives.** Transcript embeddings, which need an embedding model; OpenRouter exposes none on this key, and a local model would add a large dependency for ~30 items. Pairwise LLM comparison costs ~435 pairs per pool. Both were rejected as overkill.

---

## 6. Evaluation

### 6.1 Three layers, and why each exists

1. **Deterministic checks (no LLM)** catch the embarrassing failures that can't be argued with: invented video ids, blown budgets, forbidden content ("in 100 seconds"), known-topic leakage, unverified quotes, wrong language, a missing infeasibility flag or missing assumptions. They are cheap, run on every output, and can't be fooled by good prose.
2. **LLM judges** grade what code can't, such as whether a selection is tailored and whether the order makes sense:
   - Binary pass/fail per criterion with the critique written first. Likert scores drift and hide the failure mode.
   - Pairwise comparisons run in both orders, and disagreement between the orders counts as a tie (position bias, Zheng et al., 2023).
   - Reasons are cut to the same length in both arms (verbosity bias).
   - The judge gets a reference summary of each video built from transcript-based assessments, so it grades the content choice rather than the titles.
3. **Human labels** measure whether the judge can be trusted at all:
   - Cohen's κ with a bootstrap CI, plus TPR/TNR. Raw agreement is misleading when most items pass.
   - A table of every disagreement.
   - The labelling sheet is blind: systems are shuffled into S1–S3, so the labeller doesn't know which output is the agent's.

### 6.2 Baselines that make the numbers mean something

- **`top_n_by_views`:** same candidate pool, ranked by views, greedily filled to the budget. This is the brief's "search and view count" world turned into a system.
- **`no_transcript`:** the full pipeline, but assessed from title and description only. It isolates what reading the content buys.

### 6.3 Human labels come from a person, never from a model

**Decision.** The labelling sheet is generated, and the agreement numbers are computed only from labels a person entered. Nothing is pre-filled.

**Why.** Labels produced by a model would measure model-model agreement and present it as judge-human agreement. The labels come from the author, who also built the system; that bias is stated in EVAL.md.

### 6.4 Signals considered and discarded

These are listed with reasons in EVAL.md: view count and likes, like/view ratio, comments, subscriber count, upload recency as a score, words-per-minute, goal-to-transcript embedding similarity as the ranker, Likert judge scores, BLEU/ROUGE against a gold list, and a judge from the curator's family.

---

## 7. Test set

**Decision.** Eight personas, each built to break a different assumption:

| Persona | What it tests |
|---|---|
| `weekend_react_dev` | The reference case from the brief. |
| `lunch_break_sql_windows` | A 30-minute budget; watch ranges matter. |
| `career_switch_ml_foundations` | A 20-hour budget; prerequisite order and keeping utilisation up. |
| `sourdough_first_loaf` | A non-technical domain, to prove it isn't React-specific. |
| `go_dev_rust_ownership` | An advanced learner; must avoid beginner content. |
| `hindi_excel_pivots` | A non-English learner. |
| `impossible_k8s_in_45` | An impossible goal; must say so. |
| `ambiguous_design_frontend` | An ambiguous goal; must state its assumption. |

Each persona carries an `expectations` block, written *before* any run, which the deterministic checks read. Deciding what "good" means before seeing outputs is the main guard against grading to the answer.

---

## 8. Reproducibility and cost safety

- **Disk cache** for searches (7-day TTL), details, transcripts and assessments (keyed by model + prompt + input hash). A changed prompt re-assesses automatically, and re-runs are cheap.
- **Fixtures** in `fixtures/`: the exact pool, windows and assessments behind each published run, so results reproduce offline.
- **Cost guard:** `MAX_RUN_USD` aborts a run that passes a dollar ceiling (off unless set; `.env.example` ships it at $2), and the hosted transcript fallbacks carry their own caps (`SUPADATA_MAX_CREDITS`, `GEMINI_MAX_USD`). This protects the $20 key provided for the assignment.
- **Cost and latency are measured, not estimated:** every call records `usage.cost` from OpenRouter and its wall time in `trace.json`.
