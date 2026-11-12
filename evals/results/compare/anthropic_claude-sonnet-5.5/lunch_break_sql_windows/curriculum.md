# Curriculum: Understand SQL window functions well enough to rewrite my self-join reports

**Budget:** 30 min · **Planned:** 26 min · **Videos:** 4 · **Candidates assessed:** 36

**How I read the goal:** After 30 minutes of watching, the learner can read and write PostgreSQL window functions (OVER, PARTITION BY, ranking, LAG/LEAD, running totals) and confidently replace their self-join based reports with them.

**Assumptions:** Self-join reports are typically things like previous-row comparisons, running totals, and top-N per group, so the plan targets those patterns.; 'No full SQL courses' means the learner wants short, focused videos rather than long multi-hour course uploads.; PostgreSQL syntax is preferred, but examples in other SQL dialects are acceptable since window function syntax is largely standard.
> ⚠️ Every candidate was assessed from chapters and descriptions only, because no transcripts were available. All confidences are moderate at best, and the exact teaching quality is unverified.
> ⚠️ rewrite_self_joins is covered only by a 5.8-minute overview (UkFjJ0Wvtjs). Expect to practise converting one of your own self-join reports yourself afterwards.
> ⚠️ The LAG/LEAD video uses SQLite examples, not PostgreSQL. The syntax is the same, but check your own Postgres setup.
> ⚠️ Total viewing time is about 25.8 of 30 minutes (86%). About 4 minutes are unused, because the remaining LAG/LEAD candidates were longer than the leftover time and none could be added without padding.
> ⚠️ Assumed that short focused videos are preferred over courses, so long course uploads were excluded.

## Plan

- **OVER() and PARTITION BY: how window functions differ from GROUP BY** (`window_basics`): The learner knows GROUP BY aggregates well, so the key shift is keeping row-level detail while computing per-group values.
- **ROW_NUMBER, RANK, DENSE_RANK with ORDER BY inside OVER** (`ranking_functions`): Replaces self-joins and correlated subqueries used for top-N per group and de-duplication.
- **LAG and LEAD for previous/next row comparisons** (`lag_lead`): Self-joins on id-1 or date-1 for period-over-period reports are exactly what LAG/LEAD replace.
- **Running totals and window frames (ROWS BETWEEN, default frame behavior)** (`running_totals_frames`): Cumulative sums and moving averages are usually done with self-joins on <= conditions; frames make this simple and fast.
- **Rewriting self-join reports with window functions in PostgreSQL** (`rewrite_self_joins`): Ties the pieces together by converting real self-join queries into window function versions, which is the learner's actual goal.

## Watch in this order

### 1. [SQL Window Functions | Clearly Explained | PARTITION BY, ORDER BY, ROW_NUMBER, RANK, DENSE_RANK](https://www.youtube.com/watch?v=rIcB4zMYMas)
Maven Analytics · 8 min · counts 8 min · intermediate, concept_explainer · covers window_basics, ranking_functions · **confidence 0.70**

A step-by-step PostgreSQL walkthrough of OVER, ORDER BY, ROW_NUMBER, RANK, DENSE_RANK and PARTITION BY on a small table. It ends with filtering window results in a subquery, which is the top-N-per-group pattern that self-joins usually handle. It skips LAG/LEAD and frames, so those are covered by other picks.

> [00:00] “SQL Pocket Guide author Alice Zhao breaks down each part of a window function, step-by-step.” _(from chapters/description; no transcript)_

_Confidence note: Based on the chapter list and description only, with no transcript. The chapters match the sub-topics well and the video is short and uses PostgreSQL. Confidence would rise with a transcript showing the examples._

### 2. [SQL LAG and LEAD Functions: Compare Rows & Month-over-Month Change](https://www.youtube.com/watch?v=-r7DpMSLuDw)
PM Techhub · 4 min · counts 4 min · intermediate, concept_explainer · covers lag_lead · **confidence 0.55**

A short lesson on comparing each row with the previous or next row for period-over-period change. This is the main job self-joins do in reports, and it is the quickest way to learn LAG/LEAD. The examples use SQLite, but the syntax is the same in PostgreSQL.

> [00:00] “Compare each row with the previous or next row and calculate period-over-period changes.” _(from chapters/description; no transcript)_
> [00:00] “Every example runs real SQL on SQLite, with the code on the left and the result on the right.” _(from chapters/description; no transcript)_

_Confidence note: Based on the description only, so the depth is unknown at 3.8 minutes. It uses SQLite rather than PostgreSQL. A transcript showing PARTITION BY with LAG would raise confidence._

### 3. [SQL Window Frames Explained! 🔥 | ROWS BETWEEN, PRECEDING & CURRENT ROW | Real SQL Problem](https://www.youtube.com/watch?v=Uxv2_C1Eh7I)
The Data Dose · 8 min · counts 8 min · intermediate, concept_explainer · covers running_totals_frames · **confidence 0.60**

Covers window frames (ROWS BETWEEN, PRECEDING, CURRENT ROW) and a rolling SUM, solved as a practical problem in PostgreSQL. This is the running-total and rolling-window pattern that self-join reports often build by hand.

> [00:00] “In this tutorial, we'll explore how SQL Window Frames work and how to use them to calculate rolling totals and analyze data over a specific set of rows.” _(from chapters/description; no transcript)_
> [00:00] “Calculating Rolling SUM using Window Frames” _(from chapters/description; no transcript)_

_Confidence note: Based on the description and chapter list only. It is PostgreSQL and practical, but it is unclear whether it explains the default frame behaviour of ORDER BY inside OVER._

### 4. [How to Use Window Functions for High-Performance Postgres Queries](https://www.youtube.com/watch?v=UkFjJ0Wvtjs)
Sachin: PostgreSQL Instructor · 6 min · counts 6 min · intermediate, other · covers rewrite_self_joins, window_basics, lag_lead · **confidence 0.50**

A short PostgreSQL overview of GROUP BY versus window functions and ROW_NUMBER, RANK, LEAD and LAG. It promises to replace self-joins with windowed operations, which is the only candidate aimed at this goal. Watch it last as a capstone that ties the earlier pieces to rewriting reports.

> [00:00] “We’ll show you how to identify bottlenecks in your current SQL and replace them with high-performance windowed operations.” _(from chapters/description; no transcript)_
> [00:00] “The difference between GROUP BY and window functions. How to use essential window functions like ROW_NUMBER(), RANK(), LEAD(), and LAG().” _(from chapters/description; no transcript)_

_Confidence note: Based on the description only, and at 5.8 minutes the self-join rewrite is likely shallow. It is the only candidate that targets this sub-topic, so it fills the slot despite thin evidence._

## Similar videos: why only one made the cut

- kept `UkFjJ0Wvtjs` over `CBnlLY67cbc` (both cover dense_rank, lag, lead, order by in window functions, rank, row_number, window functions): It is the only one in the cluster that targets replacing self-joins with window functions, and it is a PostgreSQL overview in 5.8 minutes rather than a 30-minute series part.
- kept `UkFjJ0Wvtjs` over `pbwEhL_RP_g` (both cover dense_rank, lag, lead, rank, row_number): It adds the self-join replacement angle. The dropped video is a 31-minute series part with only a title and chapter marker as evidence.
- kept `UkFjJ0Wvtjs` over `6iKWzyqyms8` (both cover window functions, partition by, row_number, rank, dense_rank, lag, lead): The dropped video is a 42-minute interview-prep session that mixes joins and window functions and lists the topics without showing how they are taught.

## Considered and dropped

- [LAG() & LEAD() in SQL Explained with Real Examples | Complete Window Functions Tutorial](https://www.youtube.com/watch?v=OsMV0p8_3mk): A promising PostgreSQL LAG/LEAD video, but at 12.7 minutes it would not fit once the other slots were filled. It is also labelled beginner level, and its content is unverified.
- [Rows Between vs Range Between in SQL Window Functions | Real Difference Explained with Examples](https://www.youtube.com/watch?v=Vq9H8_wMn0k): ROWS vs RANGE BETWEEN in PostgreSQL is useful but too deep for this budget at 15.1 minutes, and the learner needs only basic frames first.
- [SQL Window Function | How to write SQL Query using RANK, DENSE RANK, LEAD/LAG | SQL Queries Tutorial](https://www.youtube.com/watch?v=Ww71knvhQ-s): Covers basics, ranking and LEAD/LAG in one video, but at 24.9 minutes it would use almost the whole budget. There is no transcript, and it does not cover frames or self-joins.
- [SQL Window Functions Basics (Visually Explained) | PARTITION BY, ORDER BY, FRAME | #SQL Course 22](https://www.youtube.com/watch?v=o666k19mZwE): At 57 minutes it is far over budget, flagged too_basic_for_learner, and its content is a beginner explainer of GROUP BY vs window functions.
- [SQL Value Window Functions | LEAD, LAG, FIRST_VALUE, LAST_VALUE | #SQL Course 25](https://www.youtube.com/watch?v=Jag6Eb2i-bQ): At 45 minutes it is a long course-style video with a lot of FIRST_VALUE/LAST_VALUE content, and it is too long for a lunch break.
- [PostgreSQL Window Functions Tutorial Database | Part 10 | LAG, LEAD ROW_NUMBER, RANK, DENSE_RANK](https://www.youtube.com/watch?v=CBnlLY67cbc): Part of a long, probably Hindi-language PostgreSQL series (about 30 minutes). It fills the whole budget, and nothing about self-join rewrites or frames can be verified.
- [Window Frames in Snowflake | ROWS BETWEEN, Running and Remaining Totals | Snowflake SQL #54](https://www.youtube.com/watch?v=zbL0ID7c7ls): Snowflake-specific frames video. The Postgres-based Uxv2_C1Eh7I covers the same ground in the learner's dialect.
- [Lead/Lag Window Analytical functions in SQL | Advance SQL concepts](https://www.youtube.com/watch?v=speKIs60TRs): LEAD/LAG overview at 10.6 minutes with no verifiable hands-on content. The shorter LAG/LEAD pick leaves room for the frames and rewrite videos.
- [Day 117 | SQL LAG() & LEAD() Functions Explained | Window Functions | Previous & Next Row](https://www.youtube.com/watch?v=gFvnKtQbKl4): Hindi-language, beginner-level LAG/LEAD on single-query Employees examples. It is flagged wrong_language and too_basic_for_learner.

<details><summary>Filtered before assessment (15)</summary>

- SQL for beginners: Self Join Explained with Real Example | Employees & Managers (prefilter): title matches exclusion 'for beginners' from the learner's constraints
- Master Advanced SQL in 90 Minutes | CASE, CTE, Subqueries & Window Functions Explained (prefilter): 93 min, far beyond the 30-min budget
- Snowflake SQL Interview Question: Manager Reports Count & Average Age | Self Join (prefilter): too short (101s)
- SQL Window Function Crash Course for Data Analyst  (prefilter): title matches exclusion 'crash course' from the learner's constraints
- 🔥 SQL Window Functions Explained | ROW_NUMBER, RANK & LEAD/LAG | LIVE (prefilter): 185 min, far beyond the 30-min budget
- 🚀 Complete SQL Masterclass for Data Analysts | 50+ SQL Interview Questions & Real Business Projects (prefilter): 100 min, far beyond the 30-min budget
- The Ultimate SQL Window Functions Course | Complete End-to-End Guide (prefilter): 231 min, far beyond the 30-min budget
- Compare Rows with SQL LAG & LEAD | Window Functions Crash Course (prefilter): title matches exclusion 'crash course' from the learner's constraints
- Advanced SQL Full Course | Master Joins, Window Functions, Subqueries, CTEs in SQL (prefilter): title matches exclusion 'full course' from the learner's constraints
- 26. SQL Functions | Aggregate Functions & Basic Window Functions with GROUP BY, OVER & PARTITION BY (prefilter): 104 min, far beyond the 30-min budget
- Complete SQL JOINS For Beginners | SQL JOIN Queries with Examples | SQL Tutorial in Hindi 11 (prefilter): title matches exclusion 'for beginners' from the learner's constraints
- Session 36 - Window Functions in SQL | DSMP 2023 (prefilter): 100 min, far beyond the 30-min budget
- SQL Window Functions Full Course (2026) | ROW_NUMBER, RANK, DENSE_RANK, LEAD|SQL Interview Questions (prefilter): title matches exclusion 'full course' from the learner's constraints
- Replace, Stuff, Substring and Translate | SQL String Functions | SQL Fundamentals (prefilter): pool cap reached
- Learn SQL: SELF JOIN (prefilter): pool cap reached

</details>

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-5.5, select=anthropic/claude-sonnet-5.5 · cost $0.094 · 32 s_
