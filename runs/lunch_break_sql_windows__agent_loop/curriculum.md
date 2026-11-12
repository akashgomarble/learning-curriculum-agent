# Curriculum: Understand SQL window functions well enough to rewrite my self-join reports

**Budget:** 30 min · **Planned:** 30 min · **Videos:** 2 · **Candidates assessed:** 35

**How I read the goal:** In one lunch break, the learner can read and write window functions (OVER/PARTITION BY, ROW_NUMBER/RANK, running totals with frames, LAG/LEAD) and spot which self-join reports to rewrite with them.

**Assumptions:** Self-join reports are typically previous-row comparisons, top-N per group, and running totals, so those patterns are prioritised.; Videos that don't use PostgreSQL are acceptable here because window-function syntax is the same.; Video summaries are the only evidence of content. The picks were not watched end to end.
> ⚠️ Total is about 29.9 minutes of a 30-minute budget, so there is no slack for pausing. If time runs short, watch only the first video and skip the second.
> ⚠️ The two picks overlap on partitions, ranking and running totals. I kept the second because it is PostgreSQL-specific and shows rolling sums on a different dataset. It has no LAG/LEAD, so the first video is the only coverage of that topic.
> ⚠️ Neither video explicitly walks through rewriting a self-join as a window function. The month-over-month and top-N patterns in the first video are the closest match, so you will need to apply the rewrite to your own reports.
> ⚠️ Among the alternatives, techTFQ (24.9 min) covers LAG/LEAD but has no running totals, and it would have pushed the plan over budget alongside a second video.

## Plan

- **OVER, PARTITION BY and how windows differ from GROUP BY** (`over_partition`): The core mental model. It makes the move away from self-joins and GROUP BY possible.
- **ROW_NUMBER / RANK / DENSE_RANK and top-N per group** (`ranking`): Replaces self-joins and correlated subqueries that find the top row in each group.
- **LAG / LEAD for previous/next-row comparisons** (`lag_lead`): Directly replaces the classic self-join on id-1 or on the previous month.
- **Running totals and moving averages with window frames** (`frames`): Replaces self-joins that use a <= condition to build cumulative totals.

## Watch in this order

### 1. [SQL Window Functions Explained: ROW_NUMBER, RANK, LAG, LEAD](https://www.youtube.com/watch?v=dUzivpyLK1s)
DataBite · 16 min · counts 16 min · intermediate, concept_explainer · covers over_partition, ranking, lag_lead, frames · **confidence 0.85**

It covers every gap in one pass: OVER/PARTITION BY, the ranking functions, LAG/LEAD, running totals and ROWS BETWEEN frames. It also shows report-style patterns (top-N per group, month-over-month growth) and common mistakes, and it uses an online store database.

> [00:24] “A window function keeps every row and adds a calculated value next to each one.”
> [00:46] “Partition by decides which rows belong together. Order by decides the sequence inside each group.”
> [10:21] “LAG fetches the value from the row before, LEAD fetches the row after.”
> [15:45] “ROWS BETWEEN controls exactly which rows count.”
> [21:40] “Forgetting ORDER BY inside OVER. LAG and running totals need a defined order or the results are random.”

_Confidence note: The summary matches the learner's needs closely. It is a small channel, so I can't judge teaching quality beyond the transcript._

### 2. [Window Functions in PostegreSQL](https://www.youtube.com/watch?v=wp8f2ShK9Ro)
Alex The Analyst · 14 min · counts 14 min · intermediate, concept_explainer · covers over_partition, ranking, frames · **confidence 0.60**

It is a second walkthrough in PostgreSQL. It reinforces the comparison with GROUP BY and PARTITION BY, then works through running and rolling sums with frames. Seeing those queries run in the learner's own database helps them transfer the pattern to their reports.

> [00:24] “When I think of a window function, I actually compare it a lot to something like a group by”
> [00:24] “We take it row by row, but then we apply it to each row. We don't aggregate it all into one row.”
> [03:42] “Partition by is kind of like a grouping. We're grouping it by the species, and then we're applying this row number.”
> [15:21] “This is what's called a rolling sum. As we go down, we're just adding the next row into this total”

_Confidence note: It overlaps the first video on ranking and does not cover LAG/LEAD. The value is a different dataset and PostgreSQL practice._

## Considered and dropped

- [SQL Window Function | How to write SQL Query using RANK, DENSE RANK, LEAD/LAG | SQL Queries Tutorial](https://www.youtube.com/watch?v=Ww71knvhQ-s): It has good self-join-replacement framing, but it has no running totals or frames, which are a stated gap. At 24.9 minutes it also cannot be paired with another video within 30 minutes.
- [SQL Window Functions EXPLAINED: The Only Tutorial You'll Ever Need!](https://www.youtube.com/watch?v=Nz4vDHE-eJo): It is flagged too_basic_for_learner. It only covers ROW_NUMBER, RANK and DENSE_RANK, and it has no LAG/LEAD or frames.
- [Window Functions in SQL Full Tutorial 🔥 | ROW_NUMBER, RANK, LAG, LEAD Explained](https://www.youtube.com/watch?v=MnDqhGAcRug): I could only read its chapter list and description, not a transcript, so I can't confirm it covers running totals or frames. It is 29.6 minutes, which uses the whole budget by itself.
- [SQL Window Functions Explained: OVER, PARTITION BY, RANK, LAG, Running Totals](https://www.youtube.com/watch?v=Kd64mv2kjX8): Its content is nearly identical to the chosen first video, with ranking, LAG, running totals and frames. It is the same format and level, so it would be a duplicate. I preferred DataBite because its summary adds top-N per group, month-over-month growth and a mistakes section.

_Models: agent_loop=anthropic/claude-sonnet-5.5 · cost $0.085 · 28 s_
