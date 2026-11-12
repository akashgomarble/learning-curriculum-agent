# Curriculum: Understand SQL window functions well enough to rewrite my self-join reports

**Budget:** 30 min · **Planned:** 23 min · **Videos:** 2 · **Candidates assessed:** 35

**How I read the goal:** In 30 minutes of viewing across at most two videos, the learner understands window functions (OVER, PARTITION BY, ranking, frames, LAG/LEAD) well enough to replace their self-join based reports with window function queries in PostgreSQL.

**Assumptions:** Self-join reports are typically things like previous-row comparisons, running totals, and top-N per group, which map to LAG/LEAD, window frames, and ROW_NUMBER/RANK.; Videos should use PostgreSQL or standard SQL syntax that works in PostgreSQL.; Two videos at most means the plan should favor one comprehensive practical video plus optionally one short complementary video, not many small ones.; No practice time is reserved, so the 30 minutes is all watching.
> ⚠️ Neither pick shows a self-join report rewritten as a window query side by side. The rewrite_self_joins sub-topic is covered only indirectly, through month-over-month LAG, top-N and running-total patterns. Map your own reports onto those patterns when you practice.
> ⚠️ The plan targets about 23.1 of 30 minutes (77%), leaving roughly 6.9 minutes unused. The remaining candidates mostly repeat topics, and a third video would break your two-video limit.
> ⚠️ The segment maps for both picks run past the stated durations. If either video is longer than listed, the total could exceed 30 minutes, so check the lengths before you start.
> ⚠️ I assumed PostgreSQL or standard SQL is fine. No time is reserved for practice, so the 30 minutes is viewing only.

## Plan

- **OVER() and PARTITION BY: window vs GROUP BY** (`over_partition_basics`): The learner knows GROUP BY aggregates, so the key mental shift is keeping row-level detail while computing aggregates over partitions, which replaces self-joins to aggregated subqueries.
- **ROW_NUMBER, RANK, DENSE_RANK for top-N per group** (`ranking_functions`): Top-N per group and deduplication are common self-join/subquery report patterns that ranking functions replace directly.
- **LAG and LEAD for previous/next row comparisons** (`lag_lead`): Comparing a row with its previous or next row is the classic self-join use case, and LAG/LEAD make it a single pass.
- **Running totals and window frames (ORDER BY, ROWS/RANGE BETWEEN)** (`running_totals_frames`): Running totals and moving averages usually require painful self-joins with inequality conditions; frames replace them.
- **Rewriting self-join reports as window function queries** (`rewrite_self_joins`): The goal is to convert existing reports, so seeing before/after examples of self-join to window function rewrites ties everything together.

## Watch in this order

### 1. [SQL Window Functions Explained: ROW_NUMBER, RANK, LAG, LEAD](https://www.youtube.com/watch?v=dUzivpyLK1s)
DataBite · 16 min · counts 16 min · intermediate, concept_explainer · covers over_partition_basics, ranking_functions, lag_lead, running_totals_frames · **confidence 0.80**

A PostgreSQL walkthrough that goes from OVER and PARTITION BY through ROW_NUMBER/RANK/DENSE_RANK top-N per group, LAG/LEAD month-over-month growth, and running totals with ROWS BETWEEN. It is one practical video that covers most of the plan, so the learner has a single setup to follow. It also ends with common mistakes such as a missing ORDER BY inside OVER.

> [00:24] “A window function keeps every row and adds a calculated value next to each one.”
> [00:46] “Partition by decides which rows belong together. Order by decides the sequence inside each group.”
> [10:21] “LAG fetches the value from the row before, LEAD fetches the row after.”

_Confidence note: Covers all four core sub-topics at the right level in PostgreSQL. Less sure because the segment map runs past the stated 15.5 minutes, so the real length may differ._

### 2. [SQL Running Total, LAG and LEAD, Moving Average, ROWS vs RANGE | Real-Time #6](https://www.youtube.com/watch?v=-JtMlZI6MZE)
TechBrothersIT · 8 min · counts 8 min · intermediate, concept_explainer · covers running_totals_frames, lag_lead, rewrite_self_joins · **confidence 0.65**

A second pass through the report-style patterns a self-join normally handles: running totals restarting per partition, month-over-month change with LAG/LEAD, and moving averages with explicit frames. It also warns about the ROWS vs RANGE frame trap. These patterns map directly onto the learner's self-join reports.

> [01:54] “PARTITION BY customer. The running total restarts for every customer.”
> [03:42] “LAG reads the previous row's revenue, and LEAD reads the next row's.”
> [05:15] “ROWS BETWEEN TWO PRECEDING AND CURRENT ROW. That's this month plus the two before it.”

_Confidence note: Strong on frames and LAG/LEAD in PostgreSQL. It never shows a self-join query side by side with its window rewrite, and its segment map also runs past the stated 7.6 minutes._

## Considered and dropped

- [SQL Window Functions Explained: OVER, PARTITION BY, RANK, LAG, Running Totals](https://www.youtube.com/watch?v=Kd64mv2kjX8): Covers all four topics in 13 minutes, but is a generic sales-table walkthrough with no top-N-per-group pattern and no report-style content. It would add little over the first pick.
- [SQL Window Functions Explained Visually (ROW_NUMBER, RANK, LEAD, LAG) 🎯](https://www.youtube.com/watch?v=OCMpARjC-VU): Short and mentions LAG replacing a self-join, but it skims every topic and would mostly repeat the first pick.
- [How to Use Window Functions for High-Performance Postgres Queries](https://www.youtube.com/watch?v=UkFjJ0Wvtjs): Directly contrasts window functions with self-joins in PostgreSQL, but it covers only running totals and moving averages, with no LAG/LEAD. The chosen second video covers more of the gaps.
- [SQL Window Function | How to write SQL Query using RANK, DENSE RANK, LEAD/LAG | SQL Queries Tutorial](https://www.youtube.com/watch?v=Ww71knvhQ-s): Good on ranking and LAG/LEAD, but at 24.9 minutes it would use most of the budget, and it has nothing on running totals or frames.
- [[Database Lecture 22] Master SQL Window Functions | Running Total, Moving Average, LEAD & LAG](https://www.youtube.com/watch?v=_zBEsmNhIiE): Complete coverage, but at 30.2 minutes it fills the whole budget, leaves no room for a second video, and is a lecture format rather than practical examples.
- [SQL Window Functions | Clearly Explained | PARTITION BY, ORDER BY, ROW_NUMBER, RANK, DENSE_RANK](https://www.youtube.com/watch?v=rIcB4zMYMas): Clear on ranking and top-N with a subquery, but it does not cover frames or running totals, and its LAG/LEAD coverage is minimal.
- [Running & Rolling Total | Moving & Rolling Average |  SQL Key Data Analysis Concepts](https://www.youtube.com/watch?v=GzRyOsQsugk): Excellent on running totals and frames, but at 19.1 minutes it covers only that one sub-topic and does not fit alongside a comprehensive first video.
- [SQL Window Function Crash Course for Data Analyst ](https://www.youtube.com/watch?v=OqhfXIK1NhY): A 67-minute crash course with no transcript, so it could not be assessed, and it is also far too long for the budget.

<details><summary>Filtered before assessment (8)</summary>

- SQL Window Functions for Interviews #sql #dataanalysis #interviews (prefilter): too short (60s)
- SQL Window Functions Basics (Visually Explained) | PARTITION BY, ORDER BY, FRAME | #SQL Course 22 (prefilter): title matches exclusion 'sql course' from the learner's constraints
- The Ultimate SQL Window Functions Course | Complete End-to-End Guide (prefilter): 231 min, far beyond the 30-min budget
- Master Advanced SQL in 90 Minutes | CASE, CTE, Subqueries & Window Functions Explained (prefilter): 93 min, far beyond the 30-min budget
- SQL Window Functions | ROW_NUMBER, RANK, LEAD, LAG + Interview Questions (prefilter): 325 min, far beyond the 30-min budget
- SQL Window Functions with Examples | ROW_NUMBER, RANK, SUM, LAG & LEAD (prefilter): too short (16s)
- Session 36 - Window Functions in SQL | DSMP 2023 (prefilter): 100 min, far beyond the 30-min budget
- Data Analysis SQL Interview Questions | Running SUM | Who Hit the Sales Target First (prefilter): too short (60s)

</details>

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.099 · 32 s_
