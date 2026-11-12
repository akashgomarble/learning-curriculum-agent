# Curriculum: Understand SQL window functions well enough to rewrite my self-join reports

**Budget:** 30 min · **Planned:** 26 min · **Videos:** 4 · **Candidates assessed:** 36

**How I read the goal:** After 30 minutes of watching, the learner can read and write PostgreSQL window functions (OVER, PARTITION BY, ranking, LAG/LEAD, running totals) and confidently replace their self-join based reports with them.

**Assumptions:** Self-join reports are typically things like previous-row comparisons, running totals, and top-N per group, so the plan targets those patterns.; 'No full SQL courses' means the learner wants short, focused videos rather than long multi-hour course uploads.; PostgreSQL syntax is preferred, but examples in other SQL dialects are acceptable since window function syntax is largely standard.
> ⚠️ None of the candidates had a transcript; every assessment is based on descriptions and chapters, so the content is unverified.
> ⚠️ The plan uses 25.8 of 30 minutes. The remaining 4.2 minutes were left unused because the alternatives would have added a long lecture fragment or a redundant creator.
> ⚠️ Self-join rewriting has only thin coverage: a 5.8-minute overview. Practice by converting one of your own reports right after watching.
> ⚠️ The LAG/LEAD video uses SQLite. Its syntax matches PostgreSQL for these functions.

## Plan

- **OVER() and PARTITION BY: how window functions differ from GROUP BY** (`window_basics`): The learner knows GROUP BY aggregates well, so the key shift is keeping row-level detail while computing per-group values.
- **ROW_NUMBER, RANK, DENSE_RANK with ORDER BY inside OVER** (`ranking_functions`): Replaces self-joins and correlated subqueries used for top-N per group and de-duplication.
- **LAG and LEAD for previous/next row comparisons** (`lag_lead`): Self-joins on id-1 or date-1 for period-over-period reports are exactly what LAG/LEAD replace.
- **Running totals and window frames (ROWS BETWEEN, default frame behavior)** (`running_totals_frames`): Cumulative sums and moving averages are usually done with self-joins on <= conditions; frames make this simple and fast.
- **Rewriting self-join reports with window functions in PostgreSQL** (`rewrite_self_joins`): Ties the pieces together by converting real self-join queries into window function versions, which is the learner's actual goal.

## Watch in this order

### 1. [SQL Window Functions | Clearly Explained | PARTITION BY, ORDER BY, ROW_NUMBER, RANK, DENSE_RANK](https://www.youtube.com/watch?v=rIcB4zMYMas)
Maven Analytics · 8 min · counts 8 min · intermediate, concept_explainer · covers window_basics, ranking_functions · **confidence 0.70**

A step-by-step breakdown of each part of a window function on a small PostgreSQL baby_names table. It covers OVER, ORDER BY, PARTITION BY, ROW_NUMBER, RANK and DENSE_RANK, and ends with filtering window results in a subquery. That last pattern is the top-N-per-group replacement for a self-join.

> [00:00] “SQL Pocket Guide author Alice Zhao breaks down each part of a window function, step-by-step.” _(from chapters/description; no transcript)_
> [00:00] “INSERT INTO baby_names (Gender, Name, Total) VALUES ('Girl', 'Ava', 95), ('Girl', 'Emma', 106), ('Boy', 'Ethan', 115)” _(from chapters/description; no transcript)_

_Confidence note: The chapters and sample data match the slot well and use PostgreSQL. There is no transcript, so the teaching depth is inferred._

### 2. [SQL LAG and LEAD Functions: Compare Rows & Month-over-Month Change](https://www.youtube.com/watch?v=-r7DpMSLuDw)
PM Techhub · 4 min · counts 4 min · intermediate, concept_explainer · covers lag_lead · **confidence 0.55**

A short lesson on LAG and LEAD that compares each row with the previous or next row to compute period-over-period changes. That is the classic previous-row self-join you want to replace. It runs real SQL with the code shown next to the result.

> [00:00] “Compare each row with the previous or next row and calculate period-over-period changes.” _(from chapters/description; no transcript)_
> [00:00] “Every example runs real SQL on SQLite, with the code on the left and the result on the right.” _(from chapters/description; no transcript)_

_Confidence note: It is very short and the evidence comes from the description only. The examples use SQLite, but LAG/LEAD syntax is the same in PostgreSQL._

### 3. [SQL Window Frames Explained! 🔥 | ROWS BETWEEN, PRECEDING & CURRENT ROW | Real SQL Problem](https://www.youtube.com/watch?v=Uxv2_C1Eh7I)
The Data Dose · 8 min · counts 8 min · intermediate, concept_explainer · covers running_totals_frames · **confidence 0.60**

Explains window frames (ROWS BETWEEN, PRECEDING, FOLLOWING, CURRENT ROW) and calculates a rolling SUM. It then solves a practical problem in PostgreSQL, which covers running totals you may currently build with self-joins.

> [00:00] “In this tutorial, we'll explore how SQL Window Frames work and how to use them to calculate rolling totals and analyze data over a specific set of rows.” _(from chapters/description; no transcript)_
> [00:00] “Calculating Rolling SUM using Window Frames” _(from chapters/description; no transcript)_
> [00:00] “Solving a practical SQL problem using PostgreSQL” _(from chapters/description; no transcript)_

_Confidence note: The topic and dialect fit well. Evidence comes from the description only, and it is unclear whether the default frame behavior is explained._

### 4. [How to Use Window Functions for High-Performance Postgres Queries](https://www.youtube.com/watch?v=UkFjJ0Wvtjs)
Sachin: PostgreSQL Instructor · 6 min · counts 6 min · intermediate, other · covers rewrite_self_joins, window_basics · **confidence 0.50**

A PostgreSQL-focused overview that contrasts GROUP BY with window functions and reviews ROW_NUMBER, RANK, LEAD and LAG. It shows how to identify bottlenecks in existing SQL and replace them with windowed operations, which is the closest match in the pool to rewriting your self-join reports.

> [00:00] “We’ll show you how to identify bottlenecks in your current SQL and replace them with high-performance windowed operations.” _(from chapters/description; no transcript)_
> [00:00] “The difference between GROUP BY and window functions. How to use essential window functions like ROW_NUMBER(), RANK(), LEAD(), and LAG().” _(from chapters/description; no transcript)_

_Confidence note: It is the only candidate that explicitly promises the self-join replacement. It is short and its depth is unverified._

## Similar videos: why only one made the cut

- kept `UkFjJ0Wvtjs` over `6iKWzyqyms8` (both cover row_number, rank, lag, lead, window functions): It focuses on PostgreSQL and explicitly targets replacing self-joins. The other is a 42-minute interview-prep session that also covers joins you already know.
- kept `UkFjJ0Wvtjs` over `CBnlLY67cbc` (both cover row_number, rank, dense_rank, lag, lead): It is in English, short, and covers self-join replacement. The other is probably Hindi, 30 minutes long, and covers only the function list.
- kept `UkFjJ0Wvtjs` over `pbwEhL_RP_g` (both cover row_number, rank, dense_rank, lag, lead): The other is probably Hindi, has a noted poor video quality issue, and does not cover self-join rewriting.

## Considered and dropped

- [SQL Window Function | How to write SQL Query using RANK, DENSE RANK, LEAD/LAG | SQL Queries Tutorial](https://www.youtube.com/watch?v=Ww71knvhQ-s): It covers the right functions, but as a 25-minute lecture it would eat most of the budget. The short focused videos cover the same ground in PostgreSQL, plus frames and self-join replacement.
- [Window Functions in SQL Full Tutorial 🔥 | ROW_NUMBER, RANK, LAG, LEAD Explained](https://www.youtube.com/watch?v=MnDqhGAcRug): A beginner-level 30-minute tutorial whose description gives no segment detail. It has no frames or self-join content.
- [SQL Window Functions Basics (Visually Explained) | PARTITION BY, ORDER BY, FRAME | #SQL Course 22](https://www.youtube.com/watch?v=o666k19mZwE): Flagged too basic, and at 57 minutes it is part of a full course, which conflicts with your no-courses constraint.
- [SQL Value Window Functions | LEAD, LAG, FIRST_VALUE, LAST_VALUE | #SQL Course 25](https://www.youtube.com/watch?v=Jag6Eb2i-bQ): A 45-minute course episode on value functions. The LAG/LEAD part alone (about 16 minutes) would exceed its slot.
- [Rows Between vs Range Between in SQL Window Functions | Real Difference Explained with Examples](https://www.youtube.com/watch?v=Vq9H8_wMn0k): A good PostgreSQL frames video, but at 15 minutes for ROWS vs RANGE it goes deeper than needed. The 8-minute frames pick fits the slot.
- [LAG() & LEAD() in SQL Explained with Real Examples | Complete Window Functions Tutorial](https://www.youtube.com/watch?v=OsMV0p8_3mk): A beginner-level LAG/LEAD video that runs 12.7 minutes, too long for the slot. The shorter pick covers the same previous-row comparison.
- [Window Frames in Snowflake | ROWS BETWEEN, Running and Remaining Totals | Snowflake SQL #54](https://www.youtube.com/watch?v=zbL0ID7c7ls): Covers frames well but in Snowflake. A PostgreSQL frames video was available.
- [Day 117 | SQL LAG() & LEAD() Functions Explained | Window Functions | Previous & Next Row](https://www.youtube.com/watch?v=gFvnKtQbKl4): Wrong language (Hindi) and flagged too basic, despite mentioning self-joins.
- [All About SQL Aggregations | SQL Advance | Zero to Hero](https://www.youtube.com/watch?v=5Ighj_2PGV0): A SQL Server aggregation overview. It would add another creator only to repeat topics already covered.
- [PostgreSQL Window Functions Tutorial Database | Part 10 | LAG, LEAD ROW_NUMBER, RANK, DENSE_RANK](https://www.youtube.com/watch?v=CBnlLY67cbc): Probably taught in Hindi, with no visible content detail. It is in the same cluster as the kept PostgreSQL overview.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-5.5, select=anthropic/claude-opus-5.5 · cost $0.165 · 40 s_
