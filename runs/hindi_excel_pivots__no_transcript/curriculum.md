# Curriculum: Learn pivot tables and lookups well enough to build a monthly sales dashboard in Excel

**Budget:** 90 min · **Planned:** 88 min · **Videos:** 6 · **Candidates assessed:** 36

**How I read the goal:** The learner can take their raw monthly sales list, use lookups to enrich it, summarize it with pivot tables, and assemble a single-sheet Excel dashboard with pivot charts and slicers, all by following Hindi-language videos on a phone.

**Assumptions:** Learner has a desktop/laptop Excel (Microsoft 365 or 2021) available to build the dashboard even though videos are watched on a phone, so XLOOKUP is available; VLOOKUP is covered as the fallback for older versions.; Sales data is a simple table with date, product, customer/region, quantity and amount columns.; The 25-minute limit applies to each individual video, not to the total plan, so several shorter videos will be combined.; Hindi-language videos are preferred; Hinglish tutorials are acceptable since they are understandable to a Hindi speaker.
> ⚠️ No candidate has verified quotes or a usable transcript, so every pick rests on titles, summaries and segment maps. Confidence is moderate at best; skim the first minute of each video to confirm it suits you.
> ⚠️ Language was inferred from titles and summaries: the picks are Hindi or Hinglish, but this is not confirmed from the audio.
> ⚠️ The sub-topic 'Preparing sales data as an Excel Table' (about 7 minutes) has no dedicated video in the pool. Convert your list to a Table with Ctrl+T (Insert > Table) before the pivot videos. The pivot videos may touch on this, but it is unverified.
> ⚠️ Timelines (date filters) are not clearly covered by any candidate; the slicer video covers slicers only. Look at the Timeline option under PivotTable Analyze once your dashboard is built.
> ⚠️ Total viewing time is 87.5 of 90 minutes, and every video is under the 25-minute limit for phone viewing. The last pick, PuGzwrnBG_s, is the most optional; dropping it cuts the plan to 66.7 minutes.
> ⚠️ Assumes you have desktop Excel 2021 or Microsoft 365 for XLOOKUP; on older versions use VLOOKUP, which the first two lookup picks cover. Videos from different creators use different sample data, so apply each lesson to your own sales table.

## Plan

- **Preparing sales data as an Excel Table** (`clean_data_table`): Pivot tables and lookups need clean, structured data; the learner only knows basic lists, so converting a list to a Table avoids common errors.
- **VLOOKUP and XLOOKUP to pull in product prices, names and categories** (`lookup_functions`): The learner has no lookup experience, and sales data usually needs product or customer details matched from another sheet before summarizing.
- **Creating pivot tables: rows, columns, values, grouping by month** (`pivot_basics`): Core skill for summarizing sales by month, product and region; builds on their knowledge of SUM and sorting/filtering.
- **Pivot charts for sales trends and comparisons** (`pivot_charts`): Charts turn pivot summaries into visuals that the dashboard needs.
- **Slicers and timelines to filter the dashboard interactively** (`slicers_timelines`): Lets the owner switch month, product or region with a click; extends the filtering they already know.
- **Building a monthly sales dashboard layout end to end** (`dashboard_build`): Brings lookups, pivots, charts and slicers together into one dashboard sheet, which is the actual goal.

## Watch in this order

### 1. [Vlookup का सबसे आसान Example || What is Vlookup in Excel (in Hindi)](https://www.youtube.com/watch?v=hmygrQMcHyU)
BUSINESS EXCEL · 6 min · counts 6 min · beginner, concept_explainer · covers lookup_functions · **confidence 0.50**

A short Hindi VLOOKUP intro with one simple example, a gentle starting point for someone who has never used lookups. It teaches what VLOOKUP is and how to write it before the fuller lookup video. It is flagged surface_intro, but a gentle on-ramp suits this beginner, and the next pick adds depth.


_Confidence note: Transcript was unavailable, so this rests on the title and summary. Higher if the example uses a price or product table._

### 2. [How To Apply VLOOKUP and XLOOKUP Formula on Large Data in Excel [Hindi] #excel](https://www.youtube.com/watch?v=gAY9is-ahQY)
Computer Gyan · 13 min · counts 13 min · beginner, concept_explainer · covers lookup_functions · **confidence 0.60**

A Hindi video that applies both VLOOKUP and XLOOKUP to larger datasets and comes with a practice file. This matches the learner's need to pull prices, names and categories into a sales list, and it covers XLOOKUP for modern Excel plus VLOOKUP as the fallback.


_Confidence note: The card shows both functions with practical examples and a practice file, but there is no transcript or verified quotes._

### 3. [Pivot Table Mastery in Excel | Pivot Table Tutorial in Hindi | Part - 01](https://www.youtube.com/watch?v=hro6_y7R310)
TLS Computer Classes · 22 min · counts 22 min · beginner, lecture · covers pivot_basics · **confidence 0.55**

Part 1 of a Hindi pivot table series covering the basics of creating pivot tables, at a beginner level. It is the main pivot coverage, taking the learner from raw list to summary with rows, columns and values.


_Confidence note: No transcript, so grouping by month is unconfirmed. Higher if it shows date grouping._

### 4. [Excel mein Pivot Chart aur Slicer kaise Banayein | How to make Pivot Chart and Slicer in Excel](https://www.youtube.com/watch?v=mp5RFCvpWI0)
Data Saathi · 4 min · counts 4 min · beginner, concept_explainer · covers pivot_charts, slicers_timelines · **confidence 0.50**

A very short Hinglish walkthrough of making a pivot chart and adding slicers to it. It covers both skills before the dashboard build, and the Hinglish title is understandable to a Hindi speaker.


_Confidence note: At under 4 minutes it is probably shallow, and timelines are likely not covered. The dashboard videos that follow reinforce it._

### 5. [“📊 Excel Dashboard Tutorial (Hindi) | Pivot Table से Dashboard बनाएं | Next-Level Reporting 🚀”](https://www.youtube.com/watch?v=_JtEWpUJPVY)
My Computer $kill · 23 min · counts 23 min · beginner, project_build · covers pivot_charts, dashboard_build · **confidence 0.60**

A Hindi project build of a mini sales dashboard from pivot tables. It ties pivot summaries and pivot charts into one dashboard, which is the learner's end goal.


_Confidence note: The card names the project as a mini sales dashboard from pivot tables, but the transcript is poor. Whether it uses slicers is unverified._

### 6. [Excel में Dashboard बनाना सीखे | Interactive Dashboard In Excel | Dashboard Tutorial |](https://www.youtube.com/watch?v=PuGzwrnBG_s)
DevelopersGuides · 21 min · counts 21 min · beginner, concept_explainer · covers dashboard_build · **confidence 0.40**

A Hindi interactive-dashboard video that goes through building a dashboard from start to finish. It gives a second example of layout and interactive elements, so the learner can practise the layout on their own sales data.


_Confidence note: Evidence is thin: relevance is only 1 and there is no transcript. Skip it if the previous dashboard video already feels sufficient._

## Similar videos: why only one made the cut

- kept `gAY9is-ahQY` over `DUP-Js2vNjs` (both cover vlookup, xlookup, lookup_functions): Both are Hindi VLOOKUP and XLOOKUP videos on large data. The kept one is a bit longer, so it has more room for examples, and it comes with a practice file.
- kept `gAY9is-ahQY` over `YW_vqEoe-Sg` (both cover vlookup, xlookup, lookup_functions): The dropped video has no clear Hindi signal in its title. The kept one is explicitly Hindi and uses large-data practical examples.
- kept `hro6_y7R310` over `ETQSNnOKDC0` (both cover pivot table creation, pivot tables): The kept video is a series Part 1 with no surface_intro flag. The dropped one is flagged surface_intro and has only about 9 minutes of relevant content.
- kept `mp5RFCvpWI0` over `5TNgfg-7RKE` (both cover pivot_charts, slicers): The kept video rates 2 for both pivot charts and slicers, while the dropped one rates only 1 on each and has no segment map.
- kept `mp5RFCvpWI0` over `htOIqJGeewE` (both cover pivot_charts): The kept video covers slicers as well as pivot charts. The dropped one covers charts only, so slicers would still be missing.

## Considered and dropped

- [XLOOKUP Function in MS Excel | MS Excel Advanced Tutorial | [Hindi] #ms excel](https://www.youtube.com/watch?v=RdA04dRgF44): An XLOOKUP-only Hindi video marked intermediate. The chosen VLOOKUP and XLOOKUP video covers both functions at a beginner level.
- [XLOOKUP in Excel | How to Use XLOOKUP Function in Excel | Excel Tutorial in Hindi](https://www.youtube.com/watch?v=1Sg1KaRwQzg): A good Hindi XLOOKUP tutorial, but adding 22 minutes would repeat lookup coverage and leave no budget for the dashboard picks. VLOOKUP is also not covered.
- [pivot table for beginners in excel in Hindi | pivot table excel in hindi](https://www.youtube.com/watch?v=hxAkt7Pico0): Near-duplicate of the chosen Hindi pivot basics video, and at 23.9 minutes it takes more of the budget for the same content.
- [🔥 Excel Pivot Table Complete Tutorial in Hindi | Beginner to Advanced](https://www.youtube.com/watch?v=ETQSNnOKDC0): Near-duplicate of the chosen pivot video. It is flagged surface_intro, and its segment map shows only about 9 minutes of actual pivot content.
- [How to Create Pivot Charts? | Excel Pivot Table in Hindi | Excel Pivot Table Series - Part - 2](https://www.youtube.com/watch?v=htOIqJGeewE): Hindi pivot charts video, but it is in the same near-duplicate cluster as the chosen chart and slicer video. It has no slicer coverage, so the chosen pick covers more of the plan.
- [Excel Pivot Table, Pivot Chart & Slicer Tutorial in Hindi | Complete Data Analysis Guide](https://www.youtube.com/watch?v=5TNgfg-7RKE): A 5.5-minute video claiming pivot tables, charts and slicers. It has no segment map and only relevance 1 for each topic, so it is too thin.
- [Sales Dashboard in Excel In Hindi | अगर अपनी सैलरी बढ़ाना चाहते हैं | तो एक्सेल Dashboard बनाना सीखे](https://www.youtube.com/watch?v=E48tn7LcxFU): A 60-minute Hindi sales dashboard video flagged clickbait, with no verifiable content and relevance 0. It is also far over the 25-minute sitting limit.
- [Pivot Table in Excel Full Tutorial 🔥 Data Analysis for Beginners (Hindi) । Computer with Kritika](https://www.youtube.com/watch?v=W3tM8BVhsuo): A 31-minute Hindi pivot lecture, over the 25-minute limit. It would need splitting and would take most of the budget for beginner pivot content already covered.
- [Excel Dashboard Course #21 - Creating a Pivot table Dashboard with Slicers in Excel (in 15 minutes)](https://www.youtube.com/watch?v=5TkRnGdC1NM): A well-matched pivot dashboard with slicers, but flagged wrong_language (not Hindi), which is disqualifying for this learner.
- [Pivot Table in Excel | Pivot Table with Multiple Slicers | Pivot Table Full Tutorial | CTA](https://www.youtube.com/watch?v=BvYU0GEHJyc): The title suggests pivot tables with multiple slicers, but no topics or content could be verified.

<details><summary>Filtered before assessment (18)</summary>

- XLOOKUP Excel में सीखें | VLOOKUP और HLOOKUP से बेहतर | Data Search Made Easy Xlookup in Excel Hindi (prefilter): too short (118s)
- Pivot Table & Slicer use in excel | pivot table and slicer in excel | Slicer kaise use kare excel me (prefilter): too short (91s)
- Data filter using Slicer in excel #excelshorts #ytshorts #shorts (prefilter): too short (50s)
- Create Pivot Table & Pivot Chart In Excel 🔥 | Microsoft Excel Tricks 💯 #shorts #exceltips #bytetech (prefilter): too short (37s)
- Pivot Table In Excel | Pivot Table In Excel In Hindi #shorts #excel (prefilter): too short (36s)
- Create Instant Dashboard In Excel 🔥 | This Excel Trick Will Blow Your Mind ‼️ #exceltips #bytetech (prefilter): too short (46s)
- How to make a Pivot Table in 3 Steps‼️ #excel (prefilter): too short (34s)
- XLOOKUP function in #excel better than VLOOKUP (prefilter): too short (41s)
- How to use slicer with pivot chart and pivot table #excel #exceltutorial (prefilter): too short (59s)
- Excel XLOOKUP Function 😱 | Find Anything Instantly in Seconds 💥 (prefilter): too short (17s)
- How to create a Simple Dashboard Report in Microsoft Excel (prefilter): pool cap reached
- How to Create Professional Excel Dashboard in 12 mins | Beginner to Pro (prefilter): pool cap reached
- Excel Pivot Table Tutorial: From Beginner to Advanced in Hindi! (prefilter): pool cap reached
- Professional 🔥 Sales Dashboard in Excel | Office work in Excel | MS Excel #sales (prefilter): pool cap reached
- MS Excel - Lookup, Vlookup, Hlookup and Xlookup Formula Explained ( अब कोई डाउट नहीं बचेगा  ) (prefilter): pool cap reached
- Dashboard In Excel For Beginners In Hindi || Complete Tutorial (prefilter): pool cap reached
- Full Project in Excel with Interactive Dashboard | Excel Tutorial for Beginners (prefilter): pool cap reached
- Pivot Table Full Course Tutorial || Basic to Advance || Hindi (prefilter): pool cap reached

</details>

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.228 · 54 s_
