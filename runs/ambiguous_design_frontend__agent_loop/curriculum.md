# Curriculum: Get better at design

**Budget:** 180 min · **Planned:** 165 min · **Videos:** 7 · **Candidates assessed:** 33

**How I read the goal:** A React/CSS developer gains practical visual design skill (hierarchy, spacing, type, color, depth) and applies it by watching real redesigns and critiques of existing UIs.

**Assumptions:** 'Better at design' means UI/visual design for web and app interfaces, not branding or UX research.; The learner has no design-tool experience. Figma is shown, but the focus is on principles they can apply in CSS.; Everything in the pool is assumed to date from 2020 or later. None of the videos is flagged as outdated.
> ⚠️ The plan uses about 165 of 180 minutes. I left the rest unused rather than add redundant videos.
> ⚠️ The color video is flagged pure_theory. I kept it because it is the only substantial color coverage and its HSB ranges are actionable.
> ⚠️ I kept Sajid's typography video over DesignSpo's. It is built around redesigning real UIs, while DesignSpo is a pure-theory overview.
> ⚠️ The fImTa4daVc8 spacing video includes Figma card-building and animation sections. The learner can skim these if they only want the spacing principles.
> ⚠️ No video here covers implementing the designs in React/CSS. The learner should practice by redesigning one of their own UIs in code.

## Plan

- **Core principles: contrast, repetition, alignment, proximity** (`principles`): This gives a shared vocabulary for critiquing any UI.
- **Spacing, layout and the 4/8-pt grid** (`spacing`): Spacing is the fastest visible improvement, and it maps directly onto the learner's CSS skills.
- **Typography and hierarchy** (`type`): Most UI is text. Size, weight and color create the hierarchy.
- **Color palettes** (`color`): This helps the learner build palettes that look good together.
- **Depth, shades and shadows with quick redesigns** (`depth`): A fast, repeatable way to lift flat UIs, shown on before/after examples.
- **Full redesign walkthrough (critique + apply)** (`redesign`): Applies every principle to one real UI from start to finish.
- **Real project process and developer handoff** (`process`): Shows how design decisions, feedback and accessibility work on a live project.

## Watch in this order

### 1. [4 Foundational UI Design Principles | C.R.A.P.](https://www.youtube.com/watch?v=uwNClNmekGU)
Jesse Showalter · 9 min · counts 9 min · beginner, concept_explainer · covers principles · **confidence 0.85**

It teaches the four CRAP principles and applies each to a bike website layout redesign, so the learner gets a vocabulary for critique with a first before/after.

> [00:20] “the acronym of the day is c-r-a-p and that stands for contrast repetition alignment and proximity”
> [00:40] “contrast it's all about organizing your design establishing hierarchy emphasizing a focal point and adding visual interest”
> [06:43] “proximity makes elements seem related like they belong together it brings understanding and meaning to multiple elements”

_Confidence note: Concise and practical; the redesign example is small._

### 2. [Why Your UI Designs Look Off — It's Your Spacing & Layout](https://www.youtube.com/watch?v=fImTa4daVc8)
Ali Hassan · 25 min · counts 25 min · beginner, concept_explainer · covers spacing · **confidence 0.75**

It explains the 4/8-pt spacing system and proximity, with before/after examples where only spacing and layout change. Spacing is the biggest lever for developers.

> [00:42] “Spacing doesn't just mean leaving empty space; it tells the user which elements are linked together”
> [01:46] “90 percent of looking pro is just spacing”
> [03:12] “If you are designing for mobile, you have to keep multiples of 4. Meaning 4, 8, 12, 16”
> [06:26] “Before, the design was like this, but after, it became like this, why? It is purely just a difference in spacing and layout, nothing else”

_Confidence note: Includes some Figma card-building and animation that is less relevant._

### 3. [The 80% of UI Design - Typography](https://www.youtube.com/watch?v=9-oefwZ6Z74)
Sajid · 12 min · counts 12 min · beginner, concept_explainer · covers type · **confidence 0.85**

It redesigns a social feed and a subscription list using size, weight and HSL lightness. It also gives a minimal type scale the learner can use in CSS.

> [00:20] “there is no hierarchy and point of focus so it's tough to tell what we are looking at it's just a bunch of text”
> [02:05] “you are going to need size color and spacing to group or separate elements technically spacing falls under the law of proximity”
> [07:49] “these are all the font sizes you need to design 99% of apps and uis and if you want just these three combined with weight and color are enough”

_Confidence note: Practical redesign-based typography lesson. I chose it over the DesignSpo typography video, which is pure theory._

### 4. [Super Practical Guide to Color Theory, Color Models and Perfect Color Palettes | UI Design](https://www.youtube.com/watch?v=GyVMoejbGFg)
Elizabeth Alli - DesignerUp · 24 min · counts 24 min · beginner, concept_explainer · covers color · **confidence 0.65**

It gives concrete saturation and brightness ranges per palette category, plus a rule to pair one category with neutrals. That makes building palettes a repeatable method.

> [12:46] “the ideal saturation and brightness for creating jewel tone color palettes lies within a saturation value range between 83 and 73 and a brightness value range between 76 and 56”
> [11:24] “the trick to getting really great looking color palettes is to stick with one of the following categories or pair one category with neutrals”

_Confidence note: Flagged pure_theory, but the learner has no color grounding and the formulas are actionable. It is the only substantial color coverage found._

### 5. [The Easy Way to Fix Boring UIs](https://www.youtube.com/watch?v=wcZ6jSlZqDc)
Sajid · 9 min · counts 9 min · beginner, project_build · covers depth · **confidence 0.85**

It uses a two-step method, layered shades plus shadows, to fix boring UIs, shown as before/after redesigns of components and a dashboard.

> [01:02] “create three to four shades of the same color and then create some shadows”
> [01:23] “Let's fix some boring UIs. We are going to start with this clean and simple design”
> [05:15] “The design is changed so much by just using four shades of gray and some shadow”

_Confidence note: Short, practical and redesign-focused._

### 6. [MASTER VISUAL HIERARCHY: Principles of VISUAL DESIGN for Designing Mobile Apps!](https://www.youtube.com/watch?v=LfkDiDyn6nU)
Design Pilot · 76 min · counts 76 min · beginner, project_build · covers redesign · **confidence 0.80**

A long hands-on redesign of a flight booking app. It starts from user needs and a critique of existing apps, then applies hierarchy, typography, spacing and color. It meets the real-redesign requirement.

> [00:41] “visual hierarchy is ensuring that the most important and relevant information is easily available to the user”
> [03:08] “users are going to be comparing various data points that we have over here and who's going to be comparing what is your job as a designer to figure out”
> [17:09] “even though ticket price is important doesn't mean that has to be the first data point right”
> [1:14:45] “with just a few textiles and just a few colors we have been able to create a beautiful in interface that makes a lot of sense very easy for users to make a decision”

_Confidence note: Long at 76 minutes, but it fits the budget and works as the capstone._

### 7. [Steal My UI/UX Process in 2026 (Real Project Breakdown)](https://www.youtube.com/watch?v=t7cnk3aQp2c)
Agatha Richards · 9 min · counts 9 min · beginner, project_build · covers process · **confidence 0.65**

It shows a live healthcare app project, including feedback-driven changes to a design that looked unclickable, a contrast and accessibility fix, and handoff to developers. This ties the learner's design work to real-world constraints.

> [01:24] “not to copy the design but to understand the structure, spacing, the UX decision and why I like specific screen more than others”
> [03:32] “I initially did like the today overview banner but after feedback that it look unclickable and there is no actions I've decided to just do a cards”
> [04:56] “the primary color was like a salmon orange and the contrast was pretty bad. Since it's a healthcare app, the accessibility is non-negotiable”

_Confidence note: Brief, process-level overview._

## Considered and dropped

- [UI/UX Website Redesign Before and After - CaterGraphix Design Academy](https://www.youtube.com/watch?v=7AhCIBGTiEA): A real redesign, but it is done in a no-code builder (Oxygen). Some advice is shaky, such as 'always give a margin, not padding', and the learner already knows CSS Grid and spacing mechanics.
- [The ULTIMATE Guide To Typography For Beginners](https://www.youtube.com/watch?v=AXpxZMRM1EY): A solid typography overview, but pure theory with no redesign. It overlaps with the Sajid typography video, which is more practical.
- [Give Me 7 Minutes & Your Web Design Skills Will Take Off](https://www.youtube.com/watch?v=1NTKwpAVcHg): A 7-minute surface-level overview flagged surface_intro. It duplicates the principles, hierarchy and color content covered in more depth elsewhere.

_Models: agent_loop=anthropic/claude-sonnet-5.5 · cost $0.144 · 46 s_
