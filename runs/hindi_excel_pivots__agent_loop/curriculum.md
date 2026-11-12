# Curriculum: Learn pivot tables and lookups well enough to build a monthly sales dashboard in Excel

**Budget:** 90 min · **Planned:** 65 min · **Videos:** 5 · **Candidates assessed:** 36

**How I read the goal:** In about 65 minutes of Hindi videos (each under 25 minutes), the learner can build a pivot table, pull data in with VLOOKUP/XLOOKUP, make pivot charts, and put together a slicer-driven monthly sales dashboard in Excel.

**Assumptions:** Hindi or Hinglish videos are acceptable, since the learner understands Hindi better than English.; The learner has a modern Excel version (2016 or later, ideally 365) so that XLOOKUP and slicers are available.; The dashboard builder video is the practice project, and the learner follows along with their own sales data.
> ⚠️ The plan uses about 65 of the 90 minutes. I left the rest unused rather than add redundant videos.
> ⚠️ A second dashboard build (oKdBEjcgzyw, 20.7 min) exists. It is a near-duplicate of the one I chose, so I did not pick it. The chosen one is monthly, has KPI cards and has a date slicer. You could watch the other one as optional extra practice.
> ⚠️ No Hindi video gave a full, quoted XLOOKUP-only lesson. Both lookup videos are mostly VLOOKUP with some XLOOKUP, so practise XLOOKUP yourself.
> ⚠️ The learner may need to pause and rewatch, since the dashboard video moves quickly.
> ⚠️ Watch order: pivot basics, then lookups, then pivot charts, then the dashboard. If your sales sheet already has all columns filled, you can skip the lookups until you need them.

## Plan

- **Pivot table basics: rows, columns, values, refresh, first slicer** (`pivot_basics`): This is the core skill, and the learner has never used a pivot table.
- **VLOOKUP and XLOOKUP for pulling data into a sales sheet** (`lookups`): Lookups fill in product, price or city columns before the data is summarised.
- **Pivot charts** (`pivot_charts`): These turn pivot summaries into visuals for the dashboard.
- **Dashboard build: KPI cards, charts, connected slicers, layout** (`dashboard`): This is the end goal: a monthly sales dashboard.

## Watch in this order

### 1. [pivot table for beginners in excel in Hindi || Microsoft excel 2007,2010,2016](https://www.youtube.com/watch?v=4A6hjD-61gM)
Deepak EduWorld · 14 min · counts 14 min · beginner, concept_explainer · covers pivot_basics · **confidence 0.85**

A beginner Hindi walkthrough of sales-data pivot tables. It covers inserting one, dragging fields to rows, columns and values, refreshing when records change, and adding a first slicer.

> [02:13] “आप अपना टेबल के अंदर कहीं भी क्लिक कर लीजिए जो रिकॉर्ड आपका है और पिवट टेबल पे क्लिक कीजिए”
> [18:21] “स्लाइसर की हेल्प से हम डाटा को आसानी से ड्रॉप डाउन लिस्ट क्रिएट होगी एक उस पे क्लिक करने से हम डाटा को आसानी से देख सकते हैं”

_Confidence note: Level and language fit well. Its transcript quotes are sparse._

### 2. [Vlookup का सबसे आसान Example || What is Vlookup in Excel (in Hindi)](https://www.youtube.com/watch?v=hmygrQMcHyU)
BUSINESS EXCEL · 6 min · counts 6 min · beginner, concept_explainer · covers lookups · **confidence 0.80**

A gentle Hindi VLOOKUP introduction that explains each argument: lookup value, table array, column index and range lookup. It uses a name, city and sales example.

> [03:25] “इक्वल टू Vlookup, lookup वैल्यू, अब ये कह रहा है कि क्या ढूंढना है”
> [03:48] “कॉलम इंडेक्स नंबर अगर यह नाम जो हमने ढूंढना है वो इस लिस्ट में मिल जाए”
> [06:01] “बड़ा डाटा अगर हमारे पास है और उसमें से छोटा डाटा की बेस पर हमें वैल्यू निकालनी है”

_Confidence note: Short and clear. It is VLOOKUP only._

### 3. [How To Apply VLOOKUP and XLOOKUP Formula on Large Data in Excel [Hindi] #excel](https://www.youtube.com/watch?v=gAY9is-ahQY)
Computer Gyan · 13 min · counts 13 min · beginner, concept_explainer · covers lookups · **confidence 0.75**

Builds on the basic VLOOKUP video. It applies VLOOKUP and XLOOKUP to large data, using MATCH to find the column number and named ranges to simplify formulas.

> [00:00] “अगर आपके पास एक लार्ज डाटा है तो उस पर आप VLOOKUP या XLOOKUP कैसे अप्लाई करेंगे”
> [00:41] “हमें क्या लिखना है यहां पर लुकअप अरे यानी कि एक अरे हम डालेंगे यहां पर जिसका डाटा हम ढूंढ रहे हैं”

_Confidence note: Hindi, beginner level and under 25 minutes. It runs a little fast for a complete beginner._

### 4. [How to Create Pivot Charts? | Excel Pivot Table in Hindi | Excel Pivot Table Series - Part - 2](https://www.youtube.com/watch?v=htOIqJGeewE)
Excel Tutorial by SkillCourse · 10 min · counts 10 min · beginner, concept_explainer · covers pivot_charts · **confidence 0.85**

A Hindi walkthrough of creating a pivot chart together with its pivot table. It covers changing chart type, data labels and formatting, ready for the dashboard.

> [00:26] “Pivot Chart हम यहां पे बनाने वाले है, तो सबसे पहले मैं Control A बटन प्रेस करूंगा।”
> [02:08] “Pivot Chart में क्या होता है बेसिकली खाली Chart ही नहीं बनेगा, यहां पे Table भी बनेगा, Chart भी बनेगा।”
> [12:04] “बेसिकली Pivot Table जो होता है उसी का ही Pivot Chart होता है। Table यहां पे आएगा-आएगा और Chart आएगा।”

_Confidence note: Directly covers the pivot chart gap._

### 5. [“📊 Excel Dashboard Tutorial (Hindi) | Pivot Table से Dashboard बनाएं | Next-Level Reporting 🚀”](https://www.youtube.com/watch?v=_JtEWpUJPVY)
My Computer $kill · 23 min · counts 23 min · beginner, project_build · covers dashboard, pivot_charts · **confidence 0.85**

A Hindi project build of an interactive monthly sales dashboard. It has KPI cards, product, region and month-trend charts, and slicers connected across all of them. This matches the learner's end goal.

> [00:21] “एक्सेल के अंदर एक मिनी सेल्स डाटा डैशबोर्ड बनाने सिखाने जा रहा हूं वो भी एकदम सिंपल और बिगिनर फ्रेंडली मेथड के साथ”
> [07:18] “अब हम इन रिपोर्ट्स की हेल्प से हम बनाएंगे डैशबोर्ड इन सभी रिपोर्ट्स की हेल्प से अब हम डैशबोर्ड बनाने जा रहे हैं”
> [33:20] “किसी भी आपको चार्ट पर सेलेक्ट करने के बाद एनालाइज वाले ऑप्शन पे जाएंगे और यहां इंसर्ट स्लाइसर पे जाएंगे”

_Confidence note: At 22.7 minutes it is under the 25-minute limit. Pause and follow along with your own data._

## Considered and dropped

- [How to make Dashboard in excel ( Interactive + Simple )](https://www.youtube.com/watch?v=oKdBEjcgzyw): This is a good Hinglish dashboard build, but it is a near-duplicate of the chosen one. It focuses on region and seller percentages and has no monthly view or KPI cards.
- [XLOOKUP Function in MS Excel | MS Excel Advanced Tutorial | [Hindi] #ms excel](https://www.youtube.com/watch?v=RdA04dRgF44): It has a good XLOOKUP explanation, but the read returned no quotes to cite and it is flagged pure_theory. It is also intermediate level.
- [How to Use VLOOKUP, HLOOKUP, XLOOKUP || Detailed Explaination with examples || Advance Excel Formula](https://www.youtube.com/watch?v=d9yXBRbNuho): It is mostly English and flagged pure_theory. It overlaps with the Hindi VLOOKUP videos I picked.
- [Pivot Table Mastery in Excel | Pivot Table Tutorial in Hindi | Part - 01](https://www.youtube.com/watch?v=hro6_y7R310): It is flagged surface_intro and is about 22 minutes. It duplicates the shorter pivot basics video and returned no quotes.

_Models: agent_loop=anthropic/claude-sonnet-5.5 · cost $0.142 · 41 s_
