# Curriculum: Understand SQL window functions well enough to rewrite my self-join reports

**Budget:** 30 min · **Planned:** 23 min · **Videos:** 4 · **Candidates assessed:** 36

**How I read the goal:** After 30 minutes of watching, the learner can read and write PostgreSQL window functions (OVER, PARTITION BY, ranking, LAG/LEAD, running totals) and confidently replace their self-join based reports with them.

**Assumptions:** Self-join reports are typically things like previous-row comparisons, running totals, and top-N per group, so the plan targets those patterns.; 'No full SQL courses' means the learner wants short, focused videos rather than long multi-hour course uploads.; PostgreSQL syntax is preferred, but examples in other SQL dialects are acceptable since window function syntax is largely standard.
> ⚠️ Every candidate in the pool is assessed from metadata only, with no transcript, so every pick is lower confidence than a verified one; check each video early and swap if the content does not match.
> ⚠️ Picked time is about 23.2 of 30 minutes (roughly 77%), leaving about 6.8 minutes unused. The reason is that the remaining good material is too thin or redundant to add without padding.
> ⚠️ Running totals and default frame behaviour are covered only by a 5.65-minute slice of Vq9H8_wMn0k, so frame coverage is thin; the learner should practise a running total with ROWS BETWEEN on their own data.
> ⚠️ LAG/LEAD is covered by a 3.8-minute SQLite video, and the rewrite sub-topic by a 5.8-minute overview, so the self-join rewrite is the weakest part of the plan and needs hands-on practice.
> ⚠️ Syntax in the picks comes from different dialects (PostgreSQL, SQLite and PostgreSQL); the standard OVER syntax transfers, but check the frame and LAG/LEAD details against PostgreSQL docs.
> ⚠️ Hindi-language videos were excluded because the learner's language was not stated as Hindi; reconsider if the learner is comfortable with Hindi.
> ⚠️ Four creators over 23 minutes is a lot of switching; this was accepted because each pick covers a sub-topic the others leave open.

## Plan

- **OVER() and PARTITION BY: how window functions differ from GROUP BY** (`window_basics`): The learner knows GROUP BY aggregates well, so the key shift is keeping row-level detail while computing per-group values.
- **ROW_NUMBER, RANK, DENSE_RANK with ORDER BY inside OVER** (`ranking_functions`): Replaces self-joins and correlated subqueries used for top-N per group and de-duplication.
- **LAG and LEAD for previous/next row comparisons** (`lag_lead`): Self-joins on id-1 or date-1 for period-over-period reports are exactly what LAG/LEAD replace.
- **Running totals and window frames (ROWS BETWEEN, default frame behavior)** (`running_totals_frames`): Cumulative sums and moving averages are usually done with self-joins on <= conditions; frames make this simple and fast.
- **Rewriting self-join reports with window functions in PostgreSQL** (`rewrite_self_joins`): Ties the pieces together by converting real self-join queries into window function versions, which is the learner's actual goal.

## Watch in this order

### 1. [SQL Window Functions | Clearly Explained | PARTITION BY, ORDER BY, ROW_NUMBER, RANK, DENSE_RANK](https://www.youtube.com/watch?v=rIcB4zMYMas)
Maven Analytics · 8 min · counts 8 min · intermediate, concept_explainer · covers window_basics, ranking_functions · **confidence 0.50**

Walks through OVER, PARTITION BY, ORDER BY, ROW_NUMBER, RANK and DENSE_RANK step by step on a small table, and the card shows it is PostgreSQL. That gives the learner the GROUP BY versus window distinction and the ranking syntax in one short video.

> [00:00] “SQL Pocket Guide author Alice Zhao breaks down each part of a window function, step-by-step.” _(from chapters/description; no transcript)_
> [00:00] “INSERT INTO baby_names (Gender, Name, Total) VALUES ('Girl', 'Ava', 95), ('Girl', 'Emma', 106), ('Boy', 'Ethan', 115)” _(from chapters/description; no transcript)_

_Confidence note: Built from chapters and description only, with no transcript, so the depth of the ranking section is unverified. Confidence would rise if the transcript showed PARTITION BY used with a real report-style query, and fall if the video stays at the single-table example level._

### 2. [SQL LAG and LEAD Functions: Compare Rows & Month-over-Month Change](https://www.youtube.com/watch?v=-r7DpMSLuDw)
PM Techhub · 4 min · counts 4 min · intermediate, concept_explainer · covers lag_lead · **confidence 0.40**

Compares each row with the previous or next row for period-over-period change, which is the same job as the learner's self-join previous-row reports. It runs every example as real SQL, so the pattern can be copied directly.

> [00:00] “Compare each row with the previous or next row and calculate period-over-period changes.” _(from chapters/description; no transcript)_
> [00:00] “Every example runs real SQL on SQLite, with the code on the left and the result on the right.” _(from chapters/description; no transcript)_

_Confidence note: The examples run on SQLite, not PostgreSQL, though LAG and LEAD syntax is standard. Only the description was available, so the depth is unconfirmed. Confidence would rise if the transcript showed LAG with PARTITION BY and ORDER BY._

### 3. [Rows Between vs Range Between in SQL Window Functions | Real Difference Explained with Examples](https://www.youtube.com/watch?v=Vq9H8_wMn0k)
Ankit Bansal · 15 min · watch 02:47–08:26 · counts 6 min · intermediate, concept_explainer · covers running_totals_frames · **confidence 0.40**

Explains ROWS BETWEEN versus RANGE BETWEEN with a running-total case in PostgreSQL, which covers the frame behavior that matters for the default frame and running totals. Only the rows and range section is needed, so the watch range is limited to 02:47 to 08:26.

> [00:00] “This video explains the real difference with simple examples, same date scenarios, PostgreSQL use cases” _(from chapters/description; no transcript)_

_Confidence note: The segment map gives the timing, but the content of the running-total example is only known from the description. Confidence would rise if the rows and range section shows the default RANGE frame producing a different result from ROWS on tied values._

### 4. [How to Use Window Functions for High-Performance Postgres Queries](https://www.youtube.com/watch?v=UkFjJ0Wvtjs)
Sachin: PostgreSQL Instructor · 6 min · counts 6 min · intermediate, other · covers rewrite_self_joins · **confidence 0.45**

Its stated purpose is replacing self-join bottlenecks in PostgreSQL with windowed operations, and it contrasts GROUP BY with window functions. That is the exact rewrite the learner wants, though only as a short overview.

> [00:00] “We’ll show you how to identify bottlenecks in your current SQL and replace them with high-performance windowed operations.” _(from chapters/description; no transcript)_
> [00:00] “The difference between GROUP BY and window functions. How to use essential window functions like ROW_NUMBER(), RANK(), LEAD(), and LAG().” _(from chapters/description; no transcript)_

_Confidence note: A 5.8-minute description-only card that promises the rewrite but cannot show how deep the worked example goes. Confidence would rise if the transcript includes an actual self-join to window function conversion; the learner should also practise one rewrite on their own report afterwards._

## Similar videos: why only one made the cut

- kept `Ww71knvhQ-s` over `fpPIOiGFh38` (both cover aggregates as window functions, over and partition by, rank and dense_rank, row_number, window functions syntax): Neither was picked, because rIcB4zMYMas covers the basics in less time. Ww71knvhQ-s stays the fallback because its card also lists LEAD/LAG, which fpPIOiGFh38 does not.
- kept `MnDqhGAcRug` over `SnHuzYstzHw` (both cover aggregate vs window functions, dense_rank, over clause, partition by, rank, row_number): Neither was picked. MnDqhGAcRug is the better content fit because it also lists LAG and LEAD, though it is beginner level and description-only.
- kept `UkFjJ0Wvtjs` over `6iKWzyqyms8` (both cover dense_rank, lag, lead, order by in window functions, rank, row_number, window functions): UkFjJ0Wvtjs is PostgreSQL-specific and explicitly promises the self-join replacement the learner needs, while 6iKWzyqyms8 is a 42.5-minute interview overview that is not PostgreSQL-focused.
- kept `UkFjJ0Wvtjs` over `CBnlLY67cbc` (both cover dense_rank, lag, lead, order by in window functions, rank, row_number, window functions): Both are PostgreSQL, but CBnlLY67cbc is a 29.9-minute part of a series that appears to be in Hindi and has no self-join content. UkFjJ0Wvtjs covers the rewrite goal in 5.8 minutes.
- kept `UkFjJ0Wvtjs` over `pbwEhL_RP_g` (both cover dense_rank, lag, lead, order by in window functions, rank, row_number, window functions): pbwEhL_RP_g is a 31.5-minute mid-series PostgreSQL video with no self-join content and a description-only card. UkFjJ0Wvtjs covers the rewrite goal in far less time.

## Considered and dropped

- [SQL Window Function | How to write SQL Query using RANK, DENSE RANK, LEAD/LAG | SQL Queries Tutorial](https://www.youtube.com/watch?v=Ww71knvhQ-s): Covers window syntax, ranking, LEAD/LAG and aggregates, but the card is description-only with a poor-transcript flag and no sign of frames or self-join rewrites. It is also a near-duplicate of fpPIOiGFh38, so one was enough, and rIcB4zMYMas covers the same ground in less time.
- [Window Function in SQL - Day - 27 - SQL - From Basic to Advance](https://www.youtube.com/watch?v=fpPIOiGFh38): Mentions ROW_NUMBER, DENSE_RANK, partitioning and running totals, but the card is description-only and does not cover LAG/LEAD or self-join rewrites. It duplicates Ww71knvhQ-s in content.
- [Window Functions in SQL Full Tutorial 🔥 | ROW_NUMBER, RANK, LAG, LEAD Explained](https://www.youtube.com/watch?v=MnDqhGAcRug): Lists ROW_NUMBER, RANK, LAG and LEAD, but it is labelled beginner, is description-only, and has no running totals or frames. For a learner who already knows SQL well, that is likely too basic.
- [SQL Joins & Window Functions Explained | Data Engineering Interview Prep| Jun Batch DE Roadmap #4](https://www.youtube.com/watch?v=6iKWzyqyms8): A 42.5-minute interview-prep overview of joins and window functions. It names the functions but is unlikely to show practical use, and at that length it would consume most of the budget.
- [LAG() & LEAD() in SQL Explained with Real Examples | Complete Window Functions Tutorial](https://www.youtube.com/watch?v=OsMV0p8_3mk): Covers LAG and LEAD in PostgreSQL with previous-month comparisons, which fits well, but it is beginner level and description-only. The shorter -r7DpMSLuDw is the intermediate pick for the same sub-topic.
- [SQL Window Frames Explained! 🔥 | ROWS BETWEEN, PRECEDING & CURRENT ROW | Real SQL Problem](https://www.youtube.com/watch?v=Uxv2_C1Eh7I): Covers window frames and rolling sums in PostgreSQL in 8.3 minutes, a reasonable alternative for the frame sub-topic. It was not picked because the Vq9H8_wMn0k section also covers RANGE versus ROWS default-frame behaviour, which this card does not mention.
- [SQL Value Window Functions | LEAD, LAG, FIRST_VALUE, LAST_VALUE | #SQL Course 25](https://www.youtube.com/watch?v=Jag6Eb2i-bQ): Covers LEAD, LAG, FIRST_VALUE and LAST_VALUE over 45 minutes, which is too long for the budget. It has no running totals or ranking, and its examples are mostly analytical rather than self-join rewrites.
- [Lead/Lag Window Analytical functions in SQL | Advance SQL concepts](https://www.youtube.com/watch?v=speKIs60TRs): Introduces LEAD and LAG for previous and next row comparison, but it is description-only and does not show how much hands-on work it contains. -r7DpMSLuDw covers the same function in less time.
- [Month Over Month Revenue Growth Rate | LAG() + Growth Formula Explained | SQL Interview #37](https://www.youtube.com/watch?v=5xOxNWJMjwA): Solves a month-over-month growth question with LAG on MySQL. It is description-only and 13.4 minutes, and it adds the growth formula rather than the window syntax the learner needs.
- [SQL Window Function with Example- RANK, DENSE RANK, ROW NUMBER, LEAD/LAG | SQL Tutorial in Hindi 14](https://www.youtube.com/watch?v=S1do1EeA7ng): Covers ranking and LEAD/LAG, but it is taught in Hindi, which is not the learner's language. The card also has no verified content.
- [Running & Rolling Total | Moving & Rolling Average |  SQL Key Data Analysis Concepts](https://www.youtube.com/watch?v=GzRyOsQsugk): Covers running and rolling totals as concepts, but no window SQL syntax is visible in the card, so it does not teach the learner how to write them.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-5.5, select=anthropic/claude-haiku-5.5 · cost $0.008 · 50 s_
