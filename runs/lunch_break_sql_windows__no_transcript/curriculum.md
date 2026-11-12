# Curriculum: Understand SQL window functions well enough to rewrite my self-join reports

**Budget:** 30 min · **Planned:** 19 min · **Videos:** 2 · **Candidates assessed:** 35

**How I read the goal:** In 30 minutes of viewing across at most two videos, the learner understands window functions (OVER, PARTITION BY, ranking, frames, LAG/LEAD) well enough to replace their self-join based reports with window function queries in PostgreSQL.

**Assumptions:** Self-join reports are typically things like previous-row comparisons, running totals, and top-N per group, which map to LAG/LEAD, window frames, and ROW_NUMBER/RANK.; Videos should use PostgreSQL or standard SQL syntax that works in PostgreSQL.; Two videos at most means the plan should favor one comprehensive practical video plus optionally one short complementary video, not many small ones.; No practice time is reserved, so the 30 minutes is all watching.
> ⚠️ Total viewing time is 18.9 of 30 min (63%), leaving 11.1 min unused. The other candidates that covered the remaining sub-topics repeated the first pick, were over budget, or lacked usable transcripts, so I did not add them.
> ⚠️ No candidate card has verified quotes, so evidence_quote_ids are empty. All reasons rest on card summaries and topic lists, not checked transcript content.
> ⚠️ The self-join rewriting sub-topic is only thinly covered. No candidate clearly walks through converting a self-join report into a window query. Expect to practise the mapping yourself, for example a self-join on id-1 becomes LAG, a join with a <= condition becomes SUM() OVER (ORDER BY ...), and top-N per group becomes ROW_NUMBER() filtered in a subquery or CTE.
> ⚠️ I assumed the examples in both videos use standard SQL that runs in PostgreSQL. The tool tags suggest so, but this is unverified.
> ⚠️ The 11 spare minutes could be used on -JtMlZI6MZE (7.6 min) for deeper coverage of ROWS vs RANGE, but that would make three videos and break your two-video limit.

## Plan

- **OVER() and PARTITION BY: window vs GROUP BY** (`over_partition_basics`): The learner knows GROUP BY aggregates, so the key mental shift is keeping row-level detail while computing aggregates over partitions, which replaces self-joins to aggregated subqueries.
- **ROW_NUMBER, RANK, DENSE_RANK for top-N per group** (`ranking_functions`): Top-N per group and deduplication are common self-join/subquery report patterns that ranking functions replace directly.
- **LAG and LEAD for previous/next row comparisons** (`lag_lead`): Comparing a row with its previous or next row is the classic self-join use case, and LAG/LEAD make it a single pass.
- **Running totals and window frames (ORDER BY, ROWS/RANGE BETWEEN)** (`running_totals_frames`): Running totals and moving averages usually require painful self-joins with inequality conditions; frames replace them.
- **Rewriting self-join reports as window function queries** (`rewrite_self_joins`): The goal is to convert existing reports, so seeing before/after examples of self-join to window function rewrites ties everything together.

## Watch in this order

### 1. [SQL Window Functions Explained: OVER, PARTITION BY, RANK, LAG, Running Totals](https://www.youtube.com/watch?v=Kd64mv2kjX8)
CodeFlow Daily · 13 min · counts 13 min · intermediate, concept_explainer · covers over_partition_basics, ranking_functions, lag_lead, running_totals_frames · **confidence 0.70**

The only unflagged candidate that covers OVER/PARTITION BY, ROW_NUMBER/RANK/DENSE_RANK, LAG/LEAD and running totals with window frames in one PostgreSQL-friendly video. Its example of ranking sales reps per region without losing rows is the kind of top-N-per-group report you now write with self-joins.


_Confidence note: Based on the card summary and topics only, with no verified quotes. The segment map is a single coarse entry. Confidence would rise if the transcript showed frame clauses (ROWS BETWEEN) explained in depth._

### 2. [How to Use Window Functions for High-Performance Postgres Queries](https://www.youtube.com/watch?v=UkFjJ0Wvtjs)
Sachin: PostgreSQL Instructor · 6 min · counts 6 min · intermediate, concept_explainer · covers rewrite_self_joins · **confidence 0.50**

Presents PostgreSQL window functions as a replacement for self-joins and subqueries, with running totals, rolling averages and ranking. It is the only short candidate aimed at your rewrite goal, so it ties the first video's functions back to your self-join reports.


_Confidence note: The transcript is poor and the video is short, so it probably shows the idea rather than a full step-by-step rewrite. Confidence would rise if it showed an actual self-join query next to its window version._

## Considered and dropped

- [SQL Window Functions Explained: ROW_NUMBER, RANK, LAG, LEAD](https://www.youtube.com/watch?v=dUzivpyLK1s): Covers the same four sub-topics as the first pick, in PostgreSQL, but at 15.5 min. A second general overview would mostly repeat the first and add nothing on self-join rewriting. It also has a poor transcript.
- [SQL Running Total, LAG and LEAD, Moving Average, ROWS vs RANGE | Real-Time #6](https://www.youtube.com/watch?v=-JtMlZI6MZE): Good on running totals, LAG/LEAD and ROWS vs RANGE, but it has no ranking coverage and nothing on self-joins. Kd64mv2kjX8 already covers those topics, and only two videos are allowed.
- [LAG() & LEAD() in SQL Explained with Real Examples | Complete Window Functions Tutorial](https://www.youtube.com/watch?v=OsMV0p8_3mk): LAG/LEAD only, in the sales-vs-previous-month style. Redundant with the first pick and leaves ranking and frames uncovered.
- [SQL in 30 Days 🚀 | Day 15: Window Functions Explained with Real Examples](https://www.youtube.com/watch?v=WUeTSd04EIw): At 4.7 min it claims every topic, but that is too short to teach them in depth. Its poor transcript prevents verifying the content, and it is more of a quick overview than practical teaching.
- [SQL Window Functions | Clearly Explained | PARTITION BY, ORDER BY, ROW_NUMBER, RANK, DENSE_RANK](https://www.youtube.com/watch?v=rIcB4zMYMas): Flagged surface_intro with a poor transcript. It covers only PARTITION BY and ranking, with no LAG/LEAD or frames.
- [Running & Rolling Total | Moving & Rolling Average |  SQL Key Data Analysis Concepts](https://www.youtube.com/watch?v=GzRyOsQsugk): Covers only running totals and moving averages, at 19.1 min. That is too long for one sub-topic and it would not fit alongside the first pick.
- [SQL Window Function | How to write SQL Query using RANK, DENSE RANK, LEAD/LAG | SQL Queries Tutorial](https://www.youtube.com/watch?v=Ww71knvhQ-s): Flagged pure_theory. It has no frames or self-join content and runs 24.9 min, which would crowd out the second video.
- [SQL Window Function Crash Course for Data Analyst ](https://www.youtube.com/watch?v=OqhfXIK1NhY): A 67-minute crash course with no transcript to check. It is far over the budget and is a course-length video, which you said you don't want.
- [MySQL Window Functions Tutorial | ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD | SQL Interview Questions](https://www.youtube.com/watch?v=ew_afdYhV-E): MySQL-based, 59 min, and without a transcript. It is over budget and not PostgreSQL.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.191 · 35 s_
