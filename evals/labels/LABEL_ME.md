# Human labelling sheet (blind)

You are the human ground truth for the LLM judge. Label from this file only: do not open `evals/results/`, `runs/` or `blind_key.json` until every row you intend to label is filled in.

## How to fill it

1. Each persona below has four curricula, S1-S4, built from the same candidate pool. Which system is which is shuffled per persona (key in `blind_key.json`).
2. Open `human_labels.csv` in a spreadsheet. Fill two columns only: `label` (`pass` or `fail`) and `critique` (one short sentence; required for every `fail`). Leave all other columns as they are.
3. Rows with `item = overall` ask: *would you hand this curriculum to this learner as is?* Pass only if you would.
4. The other rows are one per video: *is this a good pick for its place in this learner's curriculum?* Judge the video for this learner, not the curriculum around it.
5. Minimum useful pass: the `overall` rows only (32 rows, about 40-50 minutes). Per-video rows are optional but give a larger n. Blank rows are ignored, so a partial sheet is fine.
6. Then run `uv run curriculum eval --skip-judge` (free; reuses the saved judge verdicts) to compute judge-human agreement into `evals/results/RESULTS.md`.

Notes: the REFERENCE SUMMARY under each video is the pipeline's own assessment; where it says "chapters/description only" there was no transcript. One system's reasons are a fixed template, so it is not fully blind; label it on its picks anyway.

## ambiguous_design_frontend

```
Goal: Get better at design
Time budget: 180 minutes
Background: Frontend developer, 2 years, React and CSS
Already knows: CSS, React, Flexbox and Grid
Does not know yet: -
Constraints: Make it practical: include at least one real redesign or critique of an existing UI. Nothing older than 2020.
```

### ambiguous_design_frontend / S1

Planned viewing time: 178 of 180 min.

1. [a5KYlHNKQB8] Beginning Graphic Design: Layout & Composition - 5 min
   Curriculum's reason: Popular result (3,958,596 views) for 'spacing and layout design tips for developers'.
   REFERENCE SUMMARY: This video covers the foundational principles of layout and composition in graphic design, including proximity, white space, alignment, grids, contrast, visual hierarchy, and repetition. It explains how these principles work together to create organized, professional designs that guide viewers through content effectively. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory, wrong_language.

2. [c9Wg6Cb_YlU] UI / UX Design Tutorial – Wireframe, Mockup & Design in Figma - 86 min
   Curriculum's reason: Popular result (3,422,824 views) for 'UI design basics for developers'.
   REFERENCE SUMMARY: A comprehensive tutorial on the UI/UX design process that walks through wireframing a website on iPad, then creating a full mockup in Figma with proper spacing, typography, and layout. The instructor builds a complete website design from scratch, including desktop and mobile versions, demonstrating visual hierarchy, consistent spacing scales, and design decision-making. Builds: A complete website design with wireframe, desktop mockup, and mobile responsive version in Figma. Level: beginner. Format: project_build. Language: en.

3. [wIuVvCuiJhU] world's shortest UI/UX design course - 7 min
   Curriculum's reason: Popular result (2,198,175 views) for 'UI design basics for developers'.
   REFERENCE SUMMARY: A beginner's overview of UI/UX design fundamentals covering the complete design process from user flows and wireframing through design systems to final visual design. The video walks through designing a real website (stacksorted.com) step-by-step, demonstrating each principle with practical examples and tools like Figma and Real-time Colors. Builds: A website design for stacksorted.com - a design inspiration collection tool with categories, sidebar navigation, and grid layout. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

4. [AXpxZMRM1EY] The ULTIMATE Guide To Typography For Beginners - 14 min
   Curriculum's reason: Popular result (1,362,498 views) for 'typography for web developers UI design'.
   REFERENCE SUMMARY: A comprehensive beginner's guide to typography fundamentals covering typeface categories (serif, sans-serif, display, script, monospace), typographic variables (size, weight, line height, letter spacing, kerning, contrast), and building cohesive typography systems across designs. The video teaches practical principles for choosing and styling fonts to improve legibility and visual hierarchy. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

5. [MlsV3hu84as] Complete Layout Guide - 12 min
   Curriculum's reason: Popular result (945,380 views) for 'spacing and layout design tips for developers'.
   REFERENCE SUMMARY: This video teaches the three foundational principles of layout design: focal point (where the viewer's eye is drawn), white space (quiet areas that give elements room to breathe), and hierarchy (prioritizing important elements). Matt demonstrates these concepts through real-world website examples including Figma, Webflow, and a critique of Pantone's cluttered homepage. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

6. [ODpB9-MCa5s] UI/UX Explained In 8 Minutes | UI/UX Design For Beginners | UI/UX Design Basics | Simplilearn - 8 min
   Curriculum's reason: Popular result (748,309 views) for 'UI design basics for developers'.
   REFERENCE SUMMARY: An introductory overview of UI/UX design through the story of Sam creating a homework organization app. Covers the distinction between UI (visual interface) and UX (user experience), then walks through a simplified design process including user research, wireframing, visual design, information architecture, and usability testing. Builds: Homework organization app for students. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

7. [GyVMoejbGFg] Super Practical Guide to Color Theory, Color Models and Perfect Color Palettes | UI Design - 24 min
   Curriculum's reason: Popular result (594,412 views) for 'color theory for developers choosing a color palette UI'.
   REFERENCE SUMMARY: Elizabeth Alli teaches a practical approach to color theory for UI design by breaking down six color categories (jewel tones, pastels, earth tones, neutrals, fluorescents, and shades) with specific saturation and brightness ranges in HSB color models. She demonstrates how to use these formulas to create harmonious color palettes by adjusting hue while keeping saturation and brightness constant within safe ranges. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

8. [EcbgbKtOELY] Every UI/UX Concept Explained in Under 10 Minutes - 9 min
   Curriculum's reason: Popular result (549,926 views) for 'UI design basics for developers'.
   REFERENCE SUMMARY: A comprehensive overview of 10 core UI/UX design principles including visual hierarchy, spacing, typography, color theory, shadows, icons, feedback states, micro-interactions, and overlays. The video demonstrates each concept with practical visual examples and design adjustments, showing how to apply these principles to improve interface design. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

9. [1NTKwpAVcHg] Give Me 7 Minutes & Your Web Design Skills Will Take Off - 7 min
   Curriculum's reason: Popular result (536,622 views) for 'redesign website UI before and after developer design tutorial'.
   REFERENCE SUMMARY: A 7-minute overview of web design fundamentals covering three core principles: layout (visual hierarchy), color (contrast and accessibility), and typography. The video emphasizes practical principles like the 60-30-10 color rule, avoiding ghost buttons, and designing for conversion and user research rather than personal preference. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

10. [NTmh8l-Xl4c] UI Design Principles | Everything You Need To Know - 6 min
   Curriculum's reason: Popular result (279,377 views) for 'UI design basics for developers'.
   REFERENCE SUMMARY: A concise overview of six fundamental UI design principles: contrast, consistency, typography, color, visual hierarchy, and spacing. The video explains each principle and how to apply them to create effective user interfaces, covering theory and best practices without hands-on redesign or critique work. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

### ambiguous_design_frontend / S2

Planned viewing time: 165 of 180 min.
Assumptions stated: 'Better at design' means UI/visual design for web and app interfaces, not branding or UX research.; The learner has no design-tool experience. Figma is shown, but the focus is on principles they can apply in CSS.; Everything in the pool is assumed to date from 2020 or later. None of the videos is flagged as outdated.
Warnings to the learner: The plan uses about 165 of 180 minutes. I left the rest unused rather than add redundant videos. | The color video is flagged pure_theory. I kept it because it is the only substantial color coverage and its HSB ranges are actionable. | I kept Sajid's typography video over DesignSpo's. It is built around redesigning real UIs, while DesignSpo is a pure-theory overview. | The fImTa4daVc8 spacing video includes Figma card-building and animation sections. The learner can skim these if they only want the spacing principles.

1. [uwNClNmekGU] 4 Foundational UI Design Principles | C.R.A.P. - 9 min
   Curriculum's reason: It teaches the four CRAP principles and applies each to a bike website layout redesign, so the learner gets a vocabulary for critique with a first before/after.
   Quote [00:20]: "the acronym of the day is c-r-a-p and that stands for contrast repetition alignment and proximity"
   Quote [00:40]: "contrast it's all about organizing your design establishing hierarchy emphasizing a focal point and adding visual interest"
   REFERENCE SUMMARY: This video teaches the four foundational UI design principles (CRAP: Contrast, Repetition, Alignment, and Proximity) with hands-on demonstrations redesigning a bike website layout. Each principle is explained conceptually and then applied step-by-step with visual examples showing how organizing typography, spacing, and element relationships transforms a chaotic layout into a cohesive design. Builds: Redesign of a bike website layout applying contrast, repetition, alignment, and proximity principles. Level: beginner. Format: concept_explainer. Language: en.

2. [fImTa4daVc8] Why Your UI Designs Look Off — It's Your Spacing & Layout - 25 min
   Curriculum's reason: It explains the 4/8-pt spacing system and proximity, with before/after examples where only spacing and layout change. Spacing is the biggest lever for developers.
   Quote [00:42]: "Spacing doesn't just mean leaving empty space; it tells the user which elements are linked together"
   Quote [01:46]: "90 percent of looking pro is just spacing"
   REFERENCE SUMMARY: The video teaches how to fix UI designs that look off by mastering spacing and layout principles. It covers the 8-point grid system for consistent spacing, demonstrates how to properly align elements, and walks through building a complete card design in a design tool with proper spacing, alignment, and animations. Builds: A product card with image, title, description, rating, and call-to-action button, with stacked card animation effect. Level: beginner. Format: concept_explainer. Language: en.

3. [9-oefwZ6Z74] The 80% of UI Design - Typography - 12 min
   Curriculum's reason: It redesigns a social feed and a subscription list using size, weight and HSL lightness. It also gives a minimal type scale the learner can use in CSS.
   Quote [00:20]: "there is no hierarchy and point of focus so it's tough to tell what we are looking at it's just a bunch of text"
   Quote [02:05]: "you are going to need size color and spacing to group or separate elements technically spacing falls under the law of proximity"
   REFERENCE SUMMARY: This video teaches typography fundamentals for UI design, demonstrating how font size, weight, and color create visual hierarchy and user experience. It covers practical techniques like using lightness values in HSL for emphasis, building a simple type scale, and converting designs between dark and light modes. Builds: Redesign of a social media feed UI with improved typography hierarchy, and a channel subscription list UI with better visual structure. Level: beginner. Format: concept_explainer. Language: en.

4. [GyVMoejbGFg] Super Practical Guide to Color Theory, Color Models and Perfect Color Palettes | UI Design - 24 min
   Curriculum's reason: It gives concrete saturation and brightness ranges per palette category, plus a rule to pair one category with neutrals. That makes building palettes a repeatable method.
   Quote [12:46]: "the ideal saturation and brightness for creating jewel tone color palettes lies within a saturation value range between 83 and 73 and a brightness value range between 76 and 56"
   Quote [11:24]: "the trick to getting really great looking color palettes is to stick with one of the following categories or pair one category with neutrals"
   REFERENCE SUMMARY: Elizabeth Alli teaches a practical approach to color theory for UI design by breaking down six color categories (jewel tones, pastels, earth tones, neutrals, fluorescents, and shades) with specific saturation and brightness ranges in HSB color models. She demonstrates how to use these formulas to create harmonious color palettes by adjusting hue while keeping saturation and brightness constant within safe ranges. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

5. [wcZ6jSlZqDc] The Easy Way to Fix Boring UIs - 9 min
   Curriculum's reason: It uses a two-step method, layered shades plus shadows, to fix boring UIs, shown as before/after redesigns of components and a dashboard.
   Quote [01:02]: "create three to four shades of the same color and then create some shadows"
   Quote [01:23]: "Let's fix some boring UIs. We are going to start with this clean and simple design"
   REFERENCE SUMMARY: This video teaches how to add visual depth to boring UI designs using layered colors and shadows. The creator demonstrates a two-step process—creating multiple shades of the same color and adding realistic shadows—then applies it to redesign several real UI examples including navigation bars, profile cards, radio buttons, and complete dashboards, showing before/after comparisons. Builds: Redesigned multiple UI components and a complete dashboard using depth, shadows, and color layering. Level: beginner. Format: project_build. Language: en.

6. [LfkDiDyn6nU] MASTER VISUAL HIERARCHY: Principles of VISUAL DESIGN for Designing Mobile Apps! - 76 min
   Curriculum's reason: A long hands-on redesign of a flight booking app. It starts from user needs and a critique of existing apps, then applies hierarchy, typography, spacing and color. It meets the real-redesign requirement.
   Quote [00:41]: "visual hierarchy is ensuring that the most important and relevant information is easily available to the user"
   Quote [03:08]: "users are going to be comparing various data points that we have over here and who's going to be comparing what is your job as a designer to figure out"
   REFERENCE SUMMARY: This tutorial teaches visual hierarchy principles through a hands-on redesign of a flight booking mobile app UI. The instructor walks through identifying user needs, defining metrics, analyzing competitive apps, and systematically redesigning the interface using typography, spacing, colors, and layout to guide user attention and improve decision-making. Builds: Mobile flight booking app UI redesign. Level: beginner. Format: project_build. Language: en.

7. [t7cnk3aQp2c] Steal My UI/UX Process in 2026 (Real Project Breakdown) - 9 min
   Curriculum's reason: It shows a live healthcare app project, including feedback-driven changes to a design that looked unclickable, a contrast and accessibility fix, and handoff to developers. This ties the learner's design work to real-world constraints.
   Quote [01:24]: "not to copy the design but to understand the structure, spacing, the UX decision and why I like specific screen more than others"
   Quote [03:32]: "I initially did like the today overview banner but after feedback that it look unclickable and there is no actions I've decided to just do a cards"
   REFERENCE SUMMARY: A product designer breaks down her complete UI/UX process for designing a real healthcare app (mobile and dashboard). She covers research using Mobbin, mood boarding, user personas, high-fidelity design with iterative feedback, handling branding constraints, motion design, and handoff to developers—all in a practical, step-by-step walkthrough of a live project. Builds: Healthcare app (mobile and dashboard) with design system, animations, accessibility features, and app store assets. Level: beginner. Format: project_build. Language: en.

Considered and dropped:
- UI/UX Website Redesign Before and After - CaterGraphix Design Academy: A real redesign, but it is done in a no-code builder (Oxygen). Some advice is shaky, such as 'always give a margin, not padding', and the learner already knows CSS Grid and spacing mechanics.
- The ULTIMATE Guide To Typography For Beginners: A solid typography overview, but pure theory with no redesign. It overlaps with the Sajid typography video, which is more practical.
- Give Me 7 Minutes & Your Web Design Skills Will Take Off: A 7-minute surface-level overview flagged surface_intro. It duplicates the principles, hierarchy and color content covered in more depth elsewhere.

### ambiguous_design_frontend / S3

Planned viewing time: 148 of 180 min.
Assumptions stated: 'Design' means UI/visual design for web apps, not graphic design, UX research, or brand design; The learner wants to improve the look of interfaces they build in code, so developer-oriented design content fits best; Because they know CSS, layout mechanics are skipped and the focus is on design decisions; 'Nothing older than 2020' means videos published in 2020 or later; No design tool such as Figma is assumed; tool basics are included only as far as needed to follow redesigns
Warnings to the learner: No candidate has verified quotes and every card is based on metadata, with poor or unverified transcripts. All picks are therefore based on titles and summaries and carry moderate-to-low confidence, so skim the first minutes of each before committing. | Colour contrast and accessibility (WCAG ratios) are likely thin: the colour video is about palette building, and no candidate clearly teaches contrast checking. | Borders, border-radius and icons are not covered. Only shadows are covered in the polish-details slot. | The redesign and critique videos are a student website and a WordPress site, not React or web-app UIs, so you will need to translate the lessons to your own components.

1. [kK1TOpI948o] The Beginner's Guide To Visual Hierarchy - 16 min
   Curriculum's reason: Introduces visual hierarchy through contrast, uniformity and making elements stand out, which is the prerequisite for every later topic. Its only red flag is a poor transcript, so it is a better fit for a CSS-literate developer than the surface_intro or pure_theory alternatives.
   REFERENCE SUMMARY: This video teaches the fundamentals of visual hierarchy—how to rank and organize elements in design so viewers notice things in a specific order. It covers five core rules: hierarchy leads the viewer, primacy and element count are correlated, contrast is essential, uniformity gives structure, and composition arranges elements effectively using patterns like Z and F layouts. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

2. [fImTa4daVc8] Why Your UI Designs Look Off — It's Your Spacing & Layout - 25 min
   Curriculum's reason: Targets spacing and layout as the main reason UIs look off. This is the most relevant spacing video in the pool, and as a developer you can turn its fixes straight into CSS values.
   REFERENCE SUMMARY: The video teaches how to fix UI designs that look off by mastering spacing and layout principles. It covers the 8-point grid system for consistent spacing, demonstrates how to properly align elements, and walks through building a complete card design in a design tool with proper spacing, alignment, and animations. Builds: A product card with image, title, description, rating, and call-to-action button, with stacked card animation effect. Level: beginner. Format: concept_explainer. Language: en.

3. [9-oefwZ6Z74] The 80% of UI Design - Typography - 12 min
   Curriculum's reason: Covers UI typography decisions: font size, weight and colour, and how they build hierarchy in interfaces. This is the decision-focused content you need, since you already know the CSS mechanics.
   REFERENCE SUMMARY: This video teaches typography fundamentals for UI design, demonstrating how font size, weight, and color create visual hierarchy and user experience. It covers practical techniques like using lightness values in HSL for emphasis, building a simple type scale, and converting designs between dark and light modes. Builds: Redesign of a social media feed UI with improved typography hierarchy, and a channel subscription list UI with better visual structure. Level: beginner. Format: concept_explainer. Language: en.

4. [AXpxZMRM1EY] The ULTIMATE Guide To Typography For Beginners - 14 min
   Curriculum's reason: Adds typeface selection and text-handling fundamentals that the UI-specific typography video does not cover, such as how to choose and pair fonts. It fills the rest of the typography slot.
   REFERENCE SUMMARY: A comprehensive beginner's guide to typography fundamentals covering typeface categories (serif, sans-serif, display, script, monospace), typographic variables (size, weight, line height, letter spacing, kerning, contrast), and building cohesive typography systems across designs. The video teaches practical principles for choosing and styling fonts to improve legibility and visual hierarchy. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

5. [GyVMoejbGFg] Super Practical Guide to Color Theory, Color Models and Perfect Color Palettes | UI Design - 24 min
   Curriculum's reason: Teaches how to build professional UI palettes using tone, tint, shade and temperature, which basic colour-harmony tutorials usually skip. It is UI-specific and published in 2020, so it meets your date limit.
   REFERENCE SUMMARY: Elizabeth Alli teaches a practical approach to color theory for UI design by breaking down six color categories (jewel tones, pastels, earth tones, neutrals, fluorescents, and shades) with specific saturation and brightness ranges in HSB color models. She demonstrates how to use these formulas to create harmonious color palettes by adjusting hue while keeping saturation and brightness constant within safe ranges. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

6. [wcZ6jSlZqDc] The Easy Way to Fix Boring UIs - 9 min
   Curriculum's reason: Shows how to add depth to flat, boring UIs with shadows, using CodePen. This is the closest match to the polish-details topic and is directly implementable in CSS.
   REFERENCE SUMMARY: This video teaches how to add visual depth to boring UI designs using layered colors and shadows. The creator demonstrates a two-step process—creating multiple shades of the same color and adding realistic shadows—then applies it to redesign several real UI examples including navigation bars, profile cards, radio buttons, and complete dashboards, showing before/after comparisons. Builds: Redesigned multiple UI components and a complete dashboard using depth, shadows, and color layering. Level: beginner. Format: project_build. Language: en.

7. [CLLObtIpDUU] Website Redesign | Before & After (EP 01) - 5 min
   Curriculum's reason: A short before-and-after redesign of a real WordPress site that points out what was wrong, such as weak hierarchy and unclear calls to action. It gives you a quick critique example before the longer walkthrough.
   REFERENCE SUMMARY: A complete website redesign of an outdated WordPress site into a modern, clean responsive design. The video shows before-and-after comparisons of the homepage, about us page, and contact page, highlighting improvements in visual hierarchy, spacing, layout, and overall professionalism. Builds: Complete website redesign (homepage, about us page, contact page) for a WordPress site. Level: beginner. Format: project_build. Language: en. Flags: surface_intro.

8. [7AhCIBGTiEA] UI/UX Website Redesign Before and After - CaterGraphix Design Academy - 44 min
   Curriculum's reason: The longest real redesign in the pool: it walks through before-and-after improvements to an existing website and works as a critique of it. It lets you apply the hierarchy, spacing, typography and colour ideas from the earlier videos, and it meets your requirement for a real redesign or critique.
   REFERENCE SUMMARY: This video shows a real-world redesign of a student's website project, addressing multiple UI/UX issues through hands-on fixes in a no-code builder (Oxygen). The instructor systematically corrects spacing, alignment, responsive design, and component consistency while explaining design theory principles behind each decision. Builds: Redesigned student website with improved spacing, alignment, typography, and responsive behavior across multiple breakpoints. Level: beginner. Format: project_build. Language: en.

Considered and dropped:
- Visual Hierarchy in UI/UX — Why NOBODY can READ your DESIGNS: Another visual hierarchy explainer. It overlaps with the kept hierarchy video, has a poor transcript and a surface_intro flag, and would add a creator without opening a new gap.
- MASTER VISUAL HIERARCHY: Principles of VISUAL DESIGN for Designing Mobile Apps!: At 76 minutes, it would use most of the hierarchy budget on mobile app design for a single topic. Its transcript is poor and it has no segment map to pick out a useful part.
- UI / UX Design Tutorial – Wireframe, Mockup & Design in Figma: An 86-minute Figma wireframe-to-mockup course. It is tool- and process-heavy, scores relevance 1 or less on the plan's topics, and teaches little design critique.
- Industry-Standard Shadow System | Shadow Design System Tutorial for Product & UI/UX Designers: At 49.8 minutes it is a pure-theory lecture on shadow systems, far beyond the 20-minute polish slot and not practical enough.
- UI/UX Design Color Theory CRASH COURSE | Color Theory For Beginners | Saptarshi Prakash: 26 minutes of colour psychology theory aimed at beginners. It overlaps with the kept colour video and does not cover UI palettes or contrast.
- Complete Layout Guide: A pure-theory, surface-level layout explainer that duplicates the hierarchy and spacing coverage already picked.
- 4 Foundational UI Design Principles | C.R.A.P.: The C.R.A.P. principles are covered only as theory, with no redesign. Its alignment and proximity content is already covered by the spacing pick.
- Steal My UI/UX Process in 2026 (Real Project Breakdown): A Figma process breakdown of a healthcare product. It is a workflow overview rather than a critique of an existing UI, its transcript is poor, and it has only 8.8 minutes of mixed content.
- Website Redesign Before & After: Built to Convert, Not Just Look Nice: A 2.9-minute redesign comparison, too short to teach anything beyond what the other redesign videos show, with a poor transcript.
- Beginning Graphic Design: Layout & Composition: Uploaded in 2016, which breaks the 'nothing older than 2020' limit, and it is also graphic-design oriented.

### ambiguous_design_frontend / S4

Planned viewing time: 137 of 180 min.
Assumptions stated: 'Design' means UI/visual design for web apps, not graphic design, UX research, or brand design; The learner wants to improve the look of interfaces they build in code, so developer-oriented design content fits best; Because they know CSS, layout mechanics are skipped and the focus is on design decisions; 'Nothing older than 2020' means videos published in 2020 or later; No design tool such as Figma is assumed; tool basics are included only as far as needed to follow redesigns
Warnings to the learner: About 136.6 of 180 minutes are used (about 76%). The remaining ~43 minutes are unused because the other candidates were redundant, theory-only or tied to Figma, and I preferred under-filling to padding. | Border radius, icons and borders get only light coverage, mainly inside wcZ6jSlZqDc and vvPklRN0Tco. No strong dedicated video exists in the pool. | Several cards have segment maps longer than the listed minutes (e.g. LfkDiDyn6nU, MlsV3hu84as). I counted the listed minutes and used segment-map timestamps for partial ranges, so check the Design Pilot and Flux ranges when you watch. | The Design Pilot redesign is a Figma walkthrough, and no code-based full redesign is in the pool. I assumed you can follow along without learning Figma.

1. [OqAdmfRztds] Visual Hierarchy in UI/UX — Why NOBODY can READ your DESIGNS - 20 min
   Curriculum's reason: Shows how size, weight, color, spacing and position set the reading order, using pricing cards, notifications and full pages. Its 'if everything shouts the user hears nothing' framing and mistakes-to-avoid section suit a developer who can build layouts but doesn't yet make them prioritise.
   Quote [00:00]: "if everything on the screen has the same font weight and size you will be distracted about what to see first"
   Quote [02:27]: "the job of hierarchy is that if everything shouts the user hears nothing"
   REFERENCE SUMMARY: This video explains visual hierarchy in UI/UX design—how to guide users' eyes to important elements first through size, weight, color, spacing, and position. The instructor walks through practical examples like pricing cards, notifications, and full webpage layouts, showing how to avoid making everything equally prominent and demonstrating F-patterns and Z-patterns for guiding user attention. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

2. [uwNClNmekGU] 4 Foundational UI Design Principles | C.R.A.P. - 9 min
   Curriculum's reason: Applies contrast, repetition, alignment and proximity step by step to redesign a bike website layout. This is the first hands-on before/after in the course and ties hierarchy to alignment and grouping.
   Quote [00:40]: "contrast it's all about organizing your design establishing hierarchy emphasizing a focal point and adding visual interest"
   Quote [04:36]: "alignment organizes and groups elements together it creates rhythm it brings order to chaos"
   REFERENCE SUMMARY: This video teaches the four foundational UI design principles (CRAP: Contrast, Repetition, Alignment, and Proximity) with hands-on demonstrations redesigning a bike website layout. Each principle is explained conceptually and then applied step-by-step with visual examples showing how organizing typography, spacing, and element relationships transforms a chaotic layout into a cohesive design. Builds: Redesign of a bike website layout applying contrast, repetition, alignment, and proximity principles. Level: beginner. Format: concept_explainer. Language: en.

3. [fImTa4daVc8] Why Your UI Designs Look Off — It's Your Spacing & Layout - 25 min
   Curriculum's reason: Teaches the 4/8-point spacing scale and how spacing groups elements, with before/after critiques of cards. Then builds a card with consistent spacing, which turns spacing into rules a developer can reuse as CSS tokens.
   Quote [00:42]: "Spacing doesn't just mean leaving empty space; it tells the user which elements are linked together"
   Quote [01:46]: "90 percent of looking pro is just spacing"
   REFERENCE SUMMARY: The video teaches how to fix UI designs that look off by mastering spacing and layout principles. It covers the 8-point grid system for consistent spacing, demonstrates how to properly align elements, and walks through building a complete card design in a design tool with proper spacing, alignment, and animations. Builds: A product card with image, title, description, rating, and call-to-action button, with stacked card animation effect. Level: beginner. Format: concept_explainer. Language: en.

4. [9-oefwZ6Z74] The 80% of UI Design - Typography - 12 min
   Curriculum's reason: Builds hierarchy from font size, weight, color and spacing, redesigns a social feed and a subscription list, and ends with a minimal three-size type scale. The scale and CSS-variable approach fit a React/CSS developer.
   Quote [00:20]: "there is no hierarchy and point of focus so it's tough to tell what we are looking at it's just a bunch of text"
   Quote [02:05]: "you are going to need size color and spacing to group or separate elements technically spacing falls under the law of proximity"
   REFERENCE SUMMARY: This video teaches typography fundamentals for UI design, demonstrating how font size, weight, and color create visual hierarchy and user experience. It covers practical techniques like using lightness values in HSL for emphasis, building a simple type scale, and converting designs between dark and light modes. Builds: Redesign of a social media feed UI with improved typography hierarchy, and a channel subscription list UI with better visual structure. Level: beginner. Format: concept_explainer. Language: en.

5. [AXpxZMRM1EY] The ULTIMATE Guide To Typography For Beginners - 14 min
   Curriculum's reason: Fills the gap the previous video leaves: typeface categories, line height, letter spacing and kerning, and how to turn them into a typography system with rules per text type. Gives the vocabulary for choosing and pairing fonts.
   Quote [11:27]: "building a typography system makes our whole design look clean consistent and makes creating new text sections as easy as putting together Lego pieces"
   Quote [11:27]: "the basis of our system is typographical hierarchy the idea is to create rules for each text type in our design"
   REFERENCE SUMMARY: A comprehensive beginner's guide to typography fundamentals covering typeface categories (serif, sans-serif, display, script, monospace), typographic variables (size, weight, line height, letter spacing, kerning, contrast), and building cohesive typography systems across designs. The video teaches practical principles for choosing and styling fonts to improve legibility and visual hierarchy. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

6. [vvPklRN0Tco] The Easy Way to Pick UI Colors - 10 min
   Curriculum's reason: Builds neutral and brand palettes with HSL and CSS variables, with light and dark themes, readable contrast, borders and highlights. It is code-friendly and ends with OKLCH.
   Quote [00:21]: "Neutral colors for background, text, borders, and a lot of other elements. the brand or primary color for main actions"
   Quote [01:02]: "You have hue or the actual color on the color wheel that goes from 0 to 360. Then the saturation, which goes from 0 to 100"
   REFERENCE SUMMARY: A practical guide to picking UI colors using the HSL color format to create systematic color palettes for backgrounds, text, borders, and semantic states. The video demonstrates how to build dark and light mode themes with proper contrast, gradients, shadows, and highlights, then introduces OKLCH as a modern alternative for more natural color increments. Level: beginner. Format: concept_explainer. Language: en.

7. [t7cnk3aQp2c] Steal My UI/UX Process in 2026 (Real Project Breakdown) - 9 min
   Curriculum's reason: Follows a real healthcare app project: reference collection, then a bad-contrast salmon primary color fixed for accessibility, and a banner redesigned after feedback made it look unclickable. Shows contrast and critique decisions on real work, ending with a before/after.
   Quote [01:24]: "not to copy the design but to understand the structure, spacing, the UX decision and why I like specific screen more than others"
   Quote [04:56]: "the primary color was like a salmon orange and the contrast was pretty bad. Since it's a healthcare app, the accessibility is non-negotiable"
   REFERENCE SUMMARY: A product designer breaks down her complete UI/UX process for designing a real healthcare app (mobile and dashboard). She covers research using Mobbin, mood boarding, user personas, high-fidelity design with iterative feedback, handling branding constraints, motion design, and handoff to developers—all in a practical, step-by-step walkthrough of a live project. Builds: Healthcare app (mobile and dashboard) with design system, animations, accessibility features, and app store assets. Level: beginner. Format: project_build. Language: en.

8. [wcZ6jSlZqDc] The Easy Way to Fix Boring UIs - 9 min
   Curriculum's reason: Shows the layered-shades-plus-shadows technique, then applies it before/after to nav tabs, a profile card, radio buttons and a dashboard. Covers the polish details (shadow, depth) in redesigns that can be coded in CSS.
   Quote [00:00]: "all we need is a few shades of the same color and then layer them like this"
   Quote [01:02]: "create three to four shades of the same color and then create some shadows"
   REFERENCE SUMMARY: This video teaches how to add visual depth to boring UI designs using layered colors and shadows. The creator demonstrates a two-step process—creating multiple shades of the same color and adding realistic shadows—then applies it to redesign several real UI examples including navigation bars, profile cards, radio buttons, and complete dashboards, showing before/after comparisons. Builds: Redesigned multiple UI components and a complete dashboard using depth, shadows, and color layering. Level: beginner. Format: project_build. Language: en.

9. [MlsV3hu84as] Complete Layout Guide - 4 min (watch 07:40-12:00)
   Curriculum's reason: The final part walks through real sites (Figma, Webflow) and critiques Pantone's cluttered homepage against focal point, hierarchy and white space. Gives a repeatable checklist for spotting layout problems on a live site.
   Quote [10:15]: "if they would just go back to these very basic principles focal point hierarchy white space if they were observed pantone's value proposition would come across"
   REFERENCE SUMMARY: This video teaches the three foundational principles of layout design: focal point (where the viewer's eye is drawn), white space (quiet areas that give elements room to breathe), and hierarchy (prioritizing important elements). Matt demonstrates these concepts through real-world website examples including Figma, Webflow, and a critique of Pantone's cluttered homepage. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

10. [LfkDiDyn6nU] MASTER VISUAL HIERARCHY: Principles of VISUAL DESIGN for Designing Mobile Apps! - 6 min (watch 20:54-26:48)
   Curriculum's reason: This part diagnoses the problems in a poorly designed flight-booking UI, such as why ticket price need not be the first data point. It models how to critique an interface against user needs before redesigning.
   Quote [17:09]: "even though ticket price is important doesn't mean that has to be the first data point right"
   REFERENCE SUMMARY: This tutorial teaches visual hierarchy principles through a hands-on redesign of a flight booking mobile app UI. The instructor walks through identifying user needs, defining metrics, analyzing competitive apps, and systematically redesigning the interface using typography, spacing, colors, and layout to guide user attention and improve decision-making. Builds: Mobile flight booking app UI redesign. Level: beginner. Format: project_build. Language: en.

11. [LfkDiDyn6nU] MASTER VISUAL HIERARCHY: Principles of VISUAL DESIGN for Designing Mobile Apps! - 18 min (watch 56:30-1:15:00)
   Curriculum's reason: The capstone: builds text styles, spacing, color sections and emphasis step by step to redesign the flight app. Applies all earlier lessons to one real UI, and the instructor concludes that a few text styles and colors give a clear interface.
   Quote [1:14:45]: "with just a few textiles and just a few colors we have been able to create a beautiful in interface that makes a lot of sense very easy for users to make a decision"
   REFERENCE SUMMARY: This tutorial teaches visual hierarchy principles through a hands-on redesign of a flight booking mobile app UI. The instructor walks through identifying user needs, defining metrics, analyzing competitive apps, and systematically redesigning the interface using typography, spacing, colors, and layout to guide user attention and improve decision-making. Builds: Mobile flight booking app UI redesign. Level: beginner. Format: project_build. Language: en.

Considered and dropped:
- UI/UX Website Redesign Before and After - CaterGraphix Design Academy: A real redesign, but in the no-code Oxygen builder, with questionable advice ('always give a margin') and a long 44 minutes for little design theory.
- UI / UX Design Tutorial – Wireframe, Mockup & Design in Figma: 86 minutes, mostly iPad wireframing and Figma setup, which this learner doesn't need. It has no critique and covers spacing less clearly than the shorter picks.
- UI/UX Design Color Theory CRASH COURSE | Color Theory For Beginners | Saptarshi Prakash: Mostly pure color theory (harmonies, psychology). Its contrast and accessibility sections sit past the listed duration, and vvPklRN0Tco is more practical for a developer.
- Every UI/UX Concept Explained in Under 10 Minutes: A ten-minute overview that is too shallow for this learner, flagged surface_intro, and covered more deeply by the picks.
- Website Redesign Before & After: Built to Convert, Not Just Look Nice: A 3-minute before/after with a brief critique and little teaching of why the changes work, so it adds little beyond the longer redesigns.
- Website Redesign | Before & After (EP 01): A surface-level before/after tour flagged surface_intro, with no explanation of design principles. t7cnk3aQp2c and the Design Pilot parts critique more rigorously.
- UI Typography | Full UX Design Course for Beginners by Cutting Edge School: Mostly Figma text-style organisation and layer naming, which doesn't help design decisions in code.
- Industry-Standard Shadow System | Shadow Design System Tutorial for Product & UI/UX Designers: Nearly 50 minutes on Material elevation tokens in Figma. It would eat the budget and covers shadows only narrowly; wcZ6jSlZqDc covers depth practically in 9 minutes.
- Beginning Graphic Design: Layout & Composition: Uploaded 2016, which breaks the 'nothing older than 2020' limit. It is also a flagged surface-level graphic-design intro.
- Material UI Typography Component | Material UI 5 Tutorial | Typography in Material UI #4: Teaches Material UI's Typography component API rather than typographic design, and is flagged off_topic and too basic.

## career_switch_ml_foundations

```
Goal: Go from zero ML knowledge to training and evaluating a small image classifier in PyTorch
Time budget: 1200 minutes
Background: Mechanical engineer moving into ML; comfortable with Python scripting, numpy and linear algebra from university
Already knows: Python, numpy, basic linear algebra, calculus
Does not know yet: machine learning basics, gradient descent and backpropagation, PyTorch tensors and autograd, training loops, convolutional neural networks, model evaluation and overfitting
Constraints: I learn best from code-along videos but I want to understand the math intuition too. Long courses are fine. I can only study 90 minutes at a sitting, so split long courses into parts.
```

### career_switch_ml_foundations / S1

Planned viewing time: 324 of 1200 min.
Assumptions stated: The 1200 minutes is pure viewing time, so it covers about 20 hours of videos with no time reserved for practice.; Because the learner likes code-along videos, the plan favors tutorials where the presenter writes code live.; 'Small image classifier' means a CNN trained on MNIST, Fashion-MNIST or CIFAR-10, not a large pretrained model pipeline.; Each video or course part should fit within a 90-minute sitting, so long courses are picked in chunks of 90 minutes or less.; Calculus and linear algebra are already known, so math-focused videos should build intuition for ML and not reteach prerequisites.
Warnings to the learner: Under-filled: only about 324 of 1200 minutes are used (~27%), roughly 876 unused. The pool has no long courses and few substantial PyTorch tutorials, and I did not pad with weak or redundant videos. | None of the cards has verified quotes, so evidence_quote_ids is empty for every pick. Reasons rest on the card summaries and metadata, and confidence is moderated for that. | Thin coverage of PyTorch tensors and autograd: the only usable pick is the StatQuest intro, which is flagged surface_intro. Consider supplementing with the official PyTorch tutorials or a longer PyTorch course. | Evaluation coverage is mostly conceptual (bias/variance, regularization). No video clearly shows a train/validation/test split or tracking accuracy in code, so do this yourself in the project.

1. [TH8cvKLSXGg] [ML1] Machine Learning Fundamentals: Supervised Learning & Linear Regression - 12 min
   Curriculum's reason: Starts from zero with supervised learning: model representation, loss functions and optimization, taught with the math. That suits a learner with a strong math background and no ML. It is flagged pure_theory, but that is what this learner asked for.
   REFERENCE SUMMARY: This video teaches the mathematical foundations of supervised machine learning, covering the prediction equation (ŷ = f_θ(x)), loss functions (MSE), and gradient descent optimization. It explains how to represent multiple features using vectors and design matrices, and introduces the concepts of generalization, train/validation/test splits, and overfitting using house price prediction as a worked example. Level: beginner. Format: concept_explainer. Language: en.

2. [EuBBz3bI-aA] Machine Learning Fundamentals: Bias and Variance - 7 min
   Curriculum's reason: Explains bias and variance intuitively. This is the conceptual basis for underfitting, overfitting and train/test behavior, so it sets up the later evaluation material.
   REFERENCE SUMMARY: This video explains bias and variance, two fundamental ML concepts, using intuitive examples of fitting curves to mouse weight-height data. It demonstrates how simple models (linear regression) have high bias but low variance, while complex models (squiggly lines) have low bias but high variance, and introduces the concept of overfitting and the need to find a sweet spot between model complexity. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

3. [4b4MUYve_U8] Stanford CS229: Machine Learning - Linear Regression and Gradient Descent |  Lecture 2 (Autumn 2018) - 78 min
   Curriculum's reason: A full university lecture on supervised learning, linear regression and gradient descent with the derivations. It uses the calculus and linear algebra the learner already has to give a rigorous ML foundation. At 78 minutes it fits one 90-minute sitting.
   REFERENCE SUMMARY: This Stanford lecture covers supervised learning and linear regression, introducing the mathematical foundations of a learning algorithm including the hypothesis function, cost function (ordinary least squares), and two approaches to optimization: gradient descent and the normal equations. The instructor derives the gradient descent update rule and demonstrates how to minimize the squared error loss through iterative parameter updates, as well as providing a closed-form solution via the normal equations. Level: beginner. Format: lecture. Language: en. Flags: pure_theory.

4. [IHZwWFHWa-w] Gradient descent, how neural networks learn | Deep Learning Chapter 2 - 21 min
   Curriculum's reason: Gives the visual and mathematical intuition for cost functions, gradient descent and how neural networks learn their weights. This is the math-intuition backbone the learner wants before touching PyTorch.
   REFERENCE SUMMARY: This video explains gradient descent and backpropagation—the core algorithms that enable neural networks to learn from training data. Using a handwritten digit recognition example, it visualizes how cost functions work, how gradients point toward lower cost, and why repeatedly stepping in the negative gradient direction minimizes error over thousands of training examples. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

5. [vsWrXfO3wWw] Machine Learning Tutorial Python - 4: Gradient Descent and Cost Function - 28 min
   Curriculum's reason: A code-along that implements gradient descent for linear regression in plain Python, covering cost function, MSE and learning rate. It turns the math intuition into numpy-style code the learner can follow.
   REFERENCE SUMMARY: This tutorial covers gradient descent and cost functions for machine learning, using linear regression on home price prediction as the concrete example. The instructor explains the math behind mean squared error, partial derivatives, and the gradient descent algorithm, then implements it in Python code to find the best-fit line for training data. Builds: Linear regression model using gradient descent to predict home prices. Level: beginner. Format: concept_explainer. Language: en.

6. [Ilg3gGewQ5U] Backpropagation, intuitively | Deep Learning Chapter 3 - 13 min
   Curriculum's reason: Builds intuition for backpropagation, showing how each weight's influence on the cost drives its update. It is the most relevant video in the pool for the backprop concept itself.
   REFERENCE SUMMARY: This video explains backpropagation, the core algorithm for training neural networks, using intuitive visual explanations without heavy mathematics. It walks through how a single training example propagates error signals backwards through the network to determine how weights and biases should be adjusted, and introduces stochastic gradient descent as a practical computational shortcut. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

7. [tIeHLnjs5U8] Backpropagation calculus | Deep Learning Chapter 4 - 10 min
   Curriculum's reason: Gives the chain-rule calculus behind backpropagation, which this learner can follow given their calculus background. It shows how gradients flow backward and prepares them for what autograd automates.
   REFERENCE SUMMARY: This video provides a formal mathematical treatment of backpropagation, focusing on how to compute derivatives of the cost function with respect to weights and biases using the chain rule from calculus. It covers single-neuron and multi-neuron layers, explaining how sensitivity to weights, biases, and activations propagates backwards through the network. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

8. [fZtjO2cs3VQ] Backpropagation Explained By Hand: Two-Layer Neural Network, Chain Rule and Gradient Descent - 8 min
   Curriculum's reason: Works through a two-layer network by hand with numerical values and checks the analytic gradients against finite differences. A numerical worked example like this fits an engineer, and it previews what autograd will compute.
   REFERENCE SUMMARY: A detailed hand-worked derivation of backpropagation for a two-layer neural network, showing the forward pass, backward pass using the chain rule, and gradient descent weight updates. Every derivative is computed step-by-step with real numbers, then verified numerically against finite differences, demonstrating how neural networks learn by measuring error and nudging weights. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

9. [FHdlXe1bSe4] The StatQuest Introduction to PyTorch - 23 min
   Curriculum's reason: A step-by-step PyTorch walkthrough that builds a small network, makes predictions and optimizes parameters with backpropagation. It is the best available coverage of tensors and autograd, though it is flagged surface_intro, and no unflagged candidate covers this sub-topic.
   REFERENCE SUMMARY: This video walks through building a simple neural network from scratch in PyTorch, starting with a pre-defined architecture that fits a drug-dose effectiveness dataset using ReLU activations. It covers creating tensors and parameters, building a forward pass, graphing predictions, and then optimizing a single bias parameter using backpropagation and stochastic gradient descent with a training loop. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

10. [JHWqWIoac2I] Create a Basic Neural Network Model - Deep Learning with PyTorch 5 - 16 min
   Curriculum's reason: Code-along showing how to define a PyTorch nn.Module with layers and a forward function. This is the model-building half of the training loop for the learner's first network.
   REFERENCE SUMMARY: This video builds a basic neural network class in PyTorch for classifying Iris flowers. It covers defining model architecture with fully connected layers, implementing the forward pass with ReLU activation, instantiating the model, and debugging common errors. The focus is on hands-on PyTorch code rather than mathematical foundations. Builds: A simple neural network classifier for Iris flower classification with input layer (4 features), two hidden layers (8 neurons each), and output layer (3 classes). Level: beginner. Format: project_build. Language: en.

11. [zfiSAzpy9NM] Simple explanation of convolutional neural network | Deep Learning Tutorial 23 (Tensorflow & Python) - 24 min
   Curriculum's reason: A beginner-friendly explanation of how convolutions, filters and CNN architectures work. The learner has no prior CNN knowledge, so the concept is wanted here even though the examples use TensorFlow.
   REFERENCE SUMMARY: This video provides a visual, intuitive explanation of convolutional neural networks (CNNs) for image recognition, avoiding heavy mathematics. It covers how CNNs use filters to detect features like edges and facial components, applies convolution and pooling operations to reduce computation, and combines these with dense layers for classification. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

12. [jDe5BAsT2-Y] Convolutional Neural Networks from Scratch | In Depth - 13 min
   Curriculum's reason: A math-oriented look at convolution and pooling layers in a PyTorch-trained MNIST model. It adds the deeper intuition this learner wants beyond the basic explainer.
   REFERENCE SUMMARY: This video provides an in-depth walkthrough of how a convolutional neural network processes images through forward propagation, using a pretrained model on MNIST with 95.4% accuracy. The video visualizes and explains the mathematics of each layer: convolutions with filters and activation functions (ReLU and sigmoid), max pooling, flattening, and the fully connected output layer. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

13. [wnK3uWv_WkU] Pytorch CNN example (Convolutional Neural Network) - 10 min
   Curriculum's reason: A short code-along that builds a CNN in PyTorch on MNIST, turning the CNN concepts into code. It is a gentle step before the longer CIFAR-10 project.
   REFERENCE SUMMARY: This video demonstrates how to build a convolutional neural network (CNN) in PyTorch for the MNIST dataset, replacing a simple fully connected network. The instructor walks through defining a CNN class with convolutional layers, pooling, and a fully connected layer, explains the concept of "same convolution" using the output dimension formula, and trains the network to achieve 98.58% training and 98.36% test accuracy. Builds: MNIST image classifier using convolutional neural network in PyTorch. Level: beginner. Format: project_build. Language: en. Flags: surface_intro, pure_theory.

14. [hpFzuMSYg9k] Regularization | L1 & L2 | Dropout | Data Augmentation | Early Stopping |  Deep Learning Part 4 - 14 min
   Curriculum's reason: Covers overfitting remedies: L1/L2 regularization, dropout, data augmentation and early stopping. It gives the learner the main regularization options to try on the classifier.
   REFERENCE SUMMARY: This video explains regularization techniques to prevent overfitting in machine learning models. It covers L1 and L2 regularization, dropout, data augmentation, and early stopping, with geometric intuitions and mathematical foundations for each method. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

15. [fRqQwCXSeqo] 13 PyTorch tutorial - Popular techniques to prevent the overfitting in a Neural Networks - 16 min
   Curriculum's reason: A PyTorch-specific tutorial on techniques to prevent overfitting in neural networks, linking the concepts to the framework the learner is using.
   REFERENCE SUMMARY: This tutorial explains overfitting in neural networks and demonstrates five techniques to prevent it: reducing network complexity, early stopping, adding more data, data augmentation, regularization (L1/L2), and dropout. The video includes code examples showing how to implement dropout and L2 regularization in PyTorch using nn.Dropout and the weight_decay parameter in optimizers. Level: intermediate. Format: concept_explainer. Language: en.

16. [CtzfbUwrYGI] Image Classification CNN in PyTorch - 30 min
   Curriculum's reason: An end-to-end PyTorch walkthrough that trains a CNN on CIFAR-10 and covers the training process. It is the capstone code-along for the learner's goal.
   REFERENCE SUMMARY: Build and train a CNN image classifier on CIFAR-10 in PyTorch from scratch. The video covers data loading with transformations, designing a convolutional neural network with Conv2d, pooling, and fully connected layers, implementing a training loop with loss and optimizer, and evaluating accuracy on test data. Builds: Image classifier CNN trained on CIFAR-10 dataset to classify 10 image classes (dogs, cats, horses, ships, trucks, cars, etc.). Level: intermediate. Format: project_build. Language: en.

Considered and dropped:
- PyTorch Sinhala Tutorial #2 - Auto Grad and Tensor Functions - PyTorch in Sinhala: Taught in Sinhala (wrong_language), so it cannot serve this learner despite covering autograd.
- Fixing loss.backward() Gradient Issues in PyTorch S3FD PGD Attack: Narrow adversarial-attack (PGD) debugging fix, too advanced and off-topic for a first autograd lesson.
- Image classification using CNN (CIFAR10 dataset) | Deep Learning Tutorial 24 (Tensorflow & Python): CIFAR-10 CNN comparison in TensorFlow, not PyTorch; a PyTorch alternative covers the same project.
- Tensorflow Fashion MNIST Tutorial. | Tensorflow Image Classification | Neural Networks Deep learning: TensorFlow Fashion-MNIST tutorial with wrong-language and poor-transcript flags; not PyTorch.
- PyTorch a framework for research of dynamic deep learning models - Adam Paszke: 2017 conference talk on PyTorch design, not a hands-on tutorial, and flagged as outdated tooling.
- Exploring the Deep Learning Framework PyTorch - Stephanie Kim: Overview talk on PyTorch 1.0 design philosophy with no hands-on code, which doesn't fit a code-along learner.
- PyTorch Tutorial 14 - Convolutional Neural Network (CNN): Good CIFAR-10 CNN in PyTorch, but largely redundant with the picked CIFAR-10 project video; the MNIST code-along already covers the CNN code step. A viable swap if the learner prefers it.
- Regularization in a Neural Network | Dealing with overfitting: Conceptual regularization explainer that overlaps the two picked overfitting videos and adds no new gap.
- Building a CNN using PyTorch | Video 11 | CampusX: PyTorch CNN build with unverifiable content from a poor transcript, and it duplicates the picked CNN code-alongs.
- Cat Vs Dog Image Classification Project | Deep Learning Project | CNN Project: Cat vs dog project with an unclear framework and only a brief verified segment; it is less certain than the CIFAR-10 PyTorch project.

### career_switch_ml_foundations / S2

Planned viewing time: 622 of 1200 min.

1. [IHZwWFHWa-w] Gradient descent, how neural networks learn | Deep Learning Chapter 2 - 21 min
   Curriculum's reason: Popular result (9,744,717 views) for 'gradient descent and backpropagation explained calculus chain rule neural network from scratch'.
   REFERENCE SUMMARY: This video explains gradient descent and backpropagation—the core algorithms that enable neural networks to learn from training data. Using a handwritten digit recognition example, it visualizes how cost functions work, how gradients point toward lower cost, and why repeatedly stepping in the negative gradient direction minimizes error over thousands of training examples. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

2. [Ilg3gGewQ5U] Backpropagation, intuitively | Deep Learning Chapter 3 - 13 min
   Curriculum's reason: Popular result (6,401,499 views) for 'gradient descent and backpropagation explained calculus chain rule neural network from scratch'.
   REFERENCE SUMMARY: This video explains backpropagation, the core algorithm for training neural networks, using intuitive visual explanations without heavy mathematics. It walks through how a single training example propagates error signals backwards through the network to determine how weights and biases should be adjusted, and introduces stochastic gradient descent as a practical computational shortcut. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

3. [tIeHLnjs5U8] Backpropagation calculus | Deep Learning Chapter 4 - 10 min
   Curriculum's reason: Popular result (4,010,639 views) for 'gradient descent and backpropagation explained calculus chain rule neural network from scratch'.
   REFERENCE SUMMARY: This video provides a formal mathematical treatment of backpropagation, focusing on how to compute derivatives of the cost function with respect to weights and biases using the chain rule from calculus. It covers single-neuron and multi-neuron layers, explaining how sensitivity to weights, biases, and activations propagates backwards through the network. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

4. [4b4MUYve_U8] Stanford CS229: Machine Learning - Linear Regression and Gradient Descent |  Lecture 2 (Autumn 2018) - 78 min
   Curriculum's reason: Popular result (2,155,520 views) for 'machine learning fundamentals for beginners with math intuition supervised learning loss function'.
   REFERENCE SUMMARY: This Stanford lecture covers supervised learning and linear regression, introducing the mathematical foundations of a learning algorithm including the hypothesis function, cost function (ordinary least squares), and two approaches to optimization: gradient descent and the normal equations. The instructor derives the gradient descent update rule and demonstrates how to minimize the squared error loss through iterative parameter updates, as well as providing a closed-form solution via the normal equations. Level: beginner. Format: lecture. Language: en. Flags: pure_theory.

5. [EuBBz3bI-aA] Machine Learning Fundamentals: Bias and Variance - 7 min
   Curriculum's reason: Popular result (1,818,746 views) for 'machine learning fundamentals for beginners with math intuition supervised learning loss function'.
   REFERENCE SUMMARY: This video explains bias and variance, two fundamental ML concepts, using intuitive examples of fitting curves to mouse weight-height data. It demonstrates how simple models (linear regression) have high bias but low variance, while complex models (squiggly lines) have low bias but high variance, and introduces the concept of overfitting and the need to find a sweet spot between model complexity. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

6. [zfiSAzpy9NM] Simple explanation of convolutional neural network | Deep Learning Tutorial 23 (Tensorflow & Python) - 24 min
   Curriculum's reason: Popular result (1,459,263 views) for 'convolutional neural network explained PyTorch CNN tutorial code along'.
   REFERENCE SUMMARY: This video provides a visual, intuitive explanation of convolutional neural networks (CNNs) for image recognition, avoiding heavy mathematics. It covers how CNNs use filters to detect features like edges and facial components, applies convolution and pooling operations to reduce computation, and combines these with dense layers for classification. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

7. [ORMx45xqWkA] PyTorch in 100 Seconds - 3 min
   Curriculum's reason: Popular result (1,430,192 views) for 'PyTorch tensors and autograd tutorial for numpy users code along'.
   REFERENCE SUMMARY: A 100-second overview of PyTorch covering what it is, how tensors work, GPU acceleration, and how to build a simple neural network classifier by defining a class with layers (flatten, linear, activation) and a forward method. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

8. [vsWrXfO3wWw] Machine Learning Tutorial Python - 4: Gradient Descent and Cost Function - 28 min
   Curriculum's reason: Popular result (854,730 views) for 'machine learning fundamentals for beginners with math intuition supervised learning loss function'.
   REFERENCE SUMMARY: This tutorial covers gradient descent and cost functions for machine learning, using linear regression on home price prediction as the concrete example. The instructor explains the math behind mean squared error, partial derivatives, and the gradient descent algorithm, then implements it in Python code to find the best-fit line for training data. Builds: Linear regression model using gradient descent to predict home prices. Level: beginner. Format: concept_explainer. Language: en.

9. [7HPwo4wnJeA] Image classification using CNN (CIFAR10 dataset) | Deep Learning Tutorial 24 (Tensorflow & Python) - 28 min
   Curriculum's reason: Popular result (621,747 views) for 'PyTorch image classification project CNN CIFAR-10 Fashion-MNIST full tutorial from scratch'.
   REFERENCE SUMMARY: This video builds an image classifier on the CIFAR-10 dataset using TensorFlow/Keras. It first trains a simple artificial neural network, then shows how a convolutional neural network dramatically improves accuracy from 47% to 70%, explaining convolution filters, pooling, and activation functions along the way. Builds: Image classifier on CIFAR-10 dataset using CNN with convolution and pooling layers. Level: beginner. Format: project_build. Language: en. Flags: wrong_language.

10. [0K4J_PTgysc] Cat Vs Dog Image Classification Project | Deep Learning Project | CNN Project - 28 min
   Curriculum's reason: Popular result (351,702 views) for 'PyTorch image classification project CNN CIFAR-10 Fashion-MNIST full tutorial from scratch'.
   REFERENCE SUMMARY: Build a CNN-based dog vs cat image classifier using Keras/TensorFlow on Google Colab. The video walks through loading the dataset, normalizing images, constructing a CNN architecture with convolution and pooling layers, training the model, identifying overfitting, and applying techniques like data augmentation, batch normalization, and dropout to improve performance. Builds: Dog vs cat image classifier CNN in Keras. Level: beginner. Format: project_build. Language: hi.

11. [CRB266Eyjkg] Tutorial 6-Chain Rule of Differentiation with BackPropagation - 14 min
   Curriculum's reason: Popular result (258,676 views) for 'gradient descent and backpropagation explained calculus chain rule neural network from scratch'.
   REFERENCE SUMMARY: This video explains the chain rule of differentiation as the mathematical foundation of backpropagation in neural networks. It walks through how weights are updated during backpropagation by computing gradients using the chain rule, tracing how changes in weights impact the loss function through multiple layers. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

12. [pDdP0TFzsoQ] PyTorch Tutorial 14 - Convolutional Neural Network (CNN) - 22 min
   Curriculum's reason: Popular result (241,988 views) for 'convolutional neural network explained PyTorch CNN tutorial code along'.
   REFERENCE SUMMARY: Implements a CNN from scratch in PyTorch to classify CIFAR-10 images. Covers CNN architecture concepts (convolutional filters, pooling layers, fully connected layers), building a multi-layer CNN model with Conv2d and Linear layers, and training it end-to-end with a training loop and accuracy evaluation. Builds: CIFAR-10 image classifier CNN in PyTorch. Level: intermediate. Format: project_build. Language: en.

13. [FHdlXe1bSe4] The StatQuest Introduction to PyTorch - 23 min
   Curriculum's reason: Popular result (224,798 views) for 'PyTorch tensors and autograd tutorial for numpy users code along'.
   REFERENCE SUMMARY: This video walks through building a simple neural network from scratch in PyTorch, starting with a pre-defined architecture that fits a drug-dose effectiveness dataset using ReLU activations. It covers creating tensors and parameters, building a forward pass, graphing predictions, and then optimizing a single bias parameter using backpropagation and stochastic gradient descent with a training loop. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

14. [QoK1nNAURw4] Machine Learning Crash Course: Gradient Descent - 2 min
   Curriculum's reason: Popular result (222,714 views) for 'machine learning fundamentals for beginners with math intuition supervised learning loss function'.
   REFERENCE SUMMARY: This video explains gradient descent as an algorithm for training machine learning models by iteratively adjusting weights and biases to minimize loss. Using a concrete example of predicting travel times based on the number of stop signs, it demonstrates how gradient descent uses calculus to find optimal model parameters that produce the lowest mean squared error. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

15. [jDe5BAsT2-Y] Convolutional Neural Networks from Scratch | In Depth - 13 min
   Curriculum's reason: Popular result (177,622 views) for 'convolutional neural network explained PyTorch CNN tutorial code along'.
   REFERENCE SUMMARY: This video provides an in-depth walkthrough of how a convolutional neural network processes images through forward propagation, using a pretrained model on MNIST with 95.4% accuracy. The video visualizes and explains the mathematics of each layer: convolutions with filters and activation functions (ReLU and sigmoid), max pooling, flattening, and the fully connected output layer. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

16. [JHWqWIoac2I] Create a Basic Neural Network Model - Deep Learning with PyTorch 5 - 16 min
   Curriculum's reason: Popular result (168,219 views) for 'PyTorch full course beginner neural network training loop code along'.
   REFERENCE SUMMARY: This video builds a basic neural network class in PyTorch for classifying Iris flowers. It covers defining model architecture with fully connected layers, implementing the forward pass with ReLU activation, instantiating the model, and debugging common errors. The focus is on hands-on PyTorch code rather than mathematical foundations. Builds: A simple neural network classifier for Iris flower classification with input layer (4 features), two hidden layers (8 neurons each), and output layer (3 classes). Level: beginner. Format: project_build. Language: en.

17. [EehRcPo1M-Q] Regularization in a Neural Network | Dealing with overfitting - 12 min
   Curriculum's reason: Popular result (122,138 views) for 'overfitting underfitting validation loss PyTorch regularization dropout data augmentation tutorial'.
   REFERENCE SUMMARY: A conceptual explanation of regularization techniques used to combat overfitting in neural networks. The video covers L1 and L2 regularization, dropout, early stopping, and data augmentation, explaining why high weights cause overfitting and how each technique reduces model flexibility to improve generalization. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

18. [wnK3uWv_WkU] Pytorch CNN example (Convolutional Neural Network) - 10 min
   Curriculum's reason: Popular result (100,334 views) for 'convolutional neural network explained PyTorch CNN tutorial code along'.
   REFERENCE SUMMARY: This video demonstrates how to build a convolutional neural network (CNN) in PyTorch for the MNIST dataset, replacing a simple fully connected network. The instructor walks through defining a CNN class with convolutional layers, pooling, and a fully connected layer, explains the concept of "same convolution" using the output dimension formula, and trains the network to achieve 98.58% training and 98.36% test accuracy. Builds: MNIST image classifier using convolutional neural network in PyTorch. Level: beginner. Format: project_build. Language: en. Flags: surface_intro, pure_theory.

19. [o3DztvnfAJg] Underfitting & Overfitting - Explained - 3 min
   Curriculum's reason: Popular result (93,491 views) for 'overfitting underfitting validation loss PyTorch regularization dropout data augmentation tutorial'.
   REFERENCE SUMMARY: A brief overview of underfitting and overfitting in machine learning models. The video explains what causes each problem, how to recognize them by comparing training vs validation performance, and suggests high-level approaches to fix them. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

20. [Idg5uFnpV1M] What is PyTorch | Introduction to PyTorch | PyTorch Tutorial For Beginners | Intellipaat - 4 min
   Curriculum's reason: Popular result (71,739 views) for 'PyTorch tensors and autograd tutorial for numpy users code along'.
   REFERENCE SUMMARY: An overview of PyTorch as a deep learning framework, covering what it is, its core features (tensors, CUDA, dynamic computational graphs), and a high-level description of the PyTorch workflow for model training. The video explains why PyTorch is popular among data scientists and briefly outlines the steps: importing data, building models, backpropagation with autograd, and testing/saving. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

21. [CtzfbUwrYGI] Image Classification CNN in PyTorch - 30 min
   Curriculum's reason: Popular result (47,573 views) for 'convolutional neural network explained PyTorch CNN tutorial code along'.
   REFERENCE SUMMARY: Build and train a CNN image classifier on CIFAR-10 in PyTorch from scratch. The video covers data loading with transformations, designing a convolutional neural network with Conv2d, pooling, and fully connected layers, implementing a training loop with loss and optimizer, and evaluating accuracy on test data. Builds: Image classifier CNN trained on CIFAR-10 dataset to classify 10 image classes (dogs, cats, horses, ships, trucks, cars, etc.). Level: intermediate. Format: project_build. Language: en.

22. [hkiBZLRFvO4] Building a CNN using PyTorch | Video 11 | CampusX - 32 min
   Curriculum's reason: Popular result (47,522 views) for 'convolutional neural network explained PyTorch CNN tutorial code along'.
   REFERENCE SUMMARY: This video builds a convolutional neural network (CNN) from scratch in PyTorch to classify Fashion MNIST images. The instructor walks through CNN architecture design (convolution layers, pooling, fully connected layers), implements it in Google Colab by modifying previous ANN code, and achieves 92% test accuracy while observing some overfitting (99.9% training accuracy). Builds: CNN image classifier for Fashion MNIST dataset. Level: intermediate. Format: project_build. Language: hi.

23. [r6yRAxDpamQ] Convolutional Neural Network Model - Deep Learning with PyTorch 16 - 12 min
   Curriculum's reason: Popular result (19,941 views) for 'convolutional neural network explained PyTorch CNN tutorial code along'.
   REFERENCE SUMMARY: Builds a PyTorch convolutional neural network model class with two convolutional layers, pooling, and three fully connected layers. Implements the forward pass including ReLU activations, flattening, and log softmax output. Sets up the loss function (CrossEntropyLoss) and Adam optimizer with learning rate 0.001. Builds: Convolutional neural network model for image classification on CIFAR-10 dataset. Level: intermediate. Format: project_build. Language: en.

24. [hpFzuMSYg9k] Regularization | L1 & L2 | Dropout | Data Augmentation | Early Stopping |  Deep Learning Part 4 - 14 min
   Curriculum's reason: Popular result (7,751 views) for 'overfitting underfitting validation loss PyTorch regularization dropout data augmentation tutorial'.
   REFERENCE SUMMARY: This video explains regularization techniques to prevent overfitting in machine learning models. It covers L1 and L2 regularization, dropout, data augmentation, and early stopping, with geometric intuitions and mathematical foundations for each method. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

25. [BZyKufPCKdI] PyTorch a framework for research of dynamic deep learning models - Adam Paszke - 34 min
   Curriculum's reason: Popular result (5,233 views) for 'PyTorch tensors and autograd tutorial for numpy users code along'.
   REFERENCE SUMMARY: Adam Paszke introduces PyTorch as a dynamic deep learning framework, explaining its design philosophy of define-by-run graphs versus static graph frameworks like TensorFlow. He covers PyTorch's tensor library with GPU support, automatic differentiation (autograd), neural network modules, datasets, and demonstrates how the framework integrates natively with Python for flexible model building. Level: beginner. Format: lecture. Language: en. Flags: pure_theory, surface_intro.

26. [kUkGR5Lu3DU] Exploring the Deep Learning Framework PyTorch - Stephanie Kim - 36 min
   Curriculum's reason: Popular result (2,764 views) for 'PyTorch tensors and autograd tutorial for numpy users code along'.
   REFERENCE SUMMARY: This talk introduces PyTorch 1.0 as a deep learning framework, covering tensors, computational graphs, automatic differentiation (Autograd), and deployment strategies like TorchScript. The speaker explains PyTorch's advantages such as dynamic computation graphs, ease of debugging with standard Python, and GPU support, while discussing practical considerations for production use. Level: beginner. Format: lecture. Language: en. Flags: pure_theory.

27. [fRqQwCXSeqo] 13 PyTorch tutorial - Popular techniques to prevent the overfitting in a Neural Networks - 16 min
   Curriculum's reason: Popular result (2,063 views) for 'overfitting underfitting validation loss PyTorch regularization dropout data augmentation tutorial'.
   REFERENCE SUMMARY: This tutorial explains overfitting in neural networks and demonstrates five techniques to prevent it: reducing network complexity, early stopping, adding more data, data augmentation, regularization (L1/L2), and dropout. The video includes code examples showing how to implement dropout and L2 regularization in PyTorch using nn.Dropout and the weight_decay parameter in optimizers. Level: intermediate. Format: concept_explainer. Language: en.

28. [36pfg7RpvbQ] Understanding BackPropagation Using Multi-variate Calculus [Machine Learning Tutorial] - 13 min
   Curriculum's reason: Popular result (1,371 views) for 'gradient descent and backpropagation explained calculus chain rule neural network from scratch'.
   REFERENCE SUMMARY: This video explains backpropagation through the lens of multivariate calculus, building up from simple partial derivatives to complex computational graphs. It demonstrates how the chain rule applies when computing gradients through multiple paths in a computation tree, which is the mathematical foundation of backpropagation in neural networks. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

29. [pNI4N6GWdME] Convolutional Neural Network to Identify Particles of Clothing - Part 2 - 10 min
   Curriculum's reason: Popular result (592 views) for 'PyTorch image classification project CNN CIFAR-10 Fashion-MNIST full tutorial from scratch'.
   REFERENCE SUMMARY: This video builds and trains a convolutional neural network using Keras to classify clothing images from the Fashion MNIST dataset. The instructor implements Conv2D layers, max pooling, flattening, dense layers, and compiles the model with sparse categorical cross-entropy loss and Adam optimizer, achieving 89% accuracy on test data. Builds: Convolutional neural network to classify clothing images from Fashion MNIST dataset. Level: beginner. Format: project_build. Language: en. Flags: surface_intro.

30. [lSDhp0kr1ZE] PyTorch Sinhala Tutorial #2 - Auto Grad and Tensor Functions - PyTorch in Sinhala - 14 min
   Curriculum's reason: Popular result (424 views) for 'PyTorch tensors and autograd tutorial for numpy users code along'.
   REFERENCE SUMMARY: This tutorial teaches PyTorch tensors and automatic gradient computation (autograd). It covers creating tensors with requires_grad enabled, computing gradients using backward(), and basic tensor operations like concatenation, reshaping, and trigonometric functions. It also demonstrates NumPy-PyTorch conversion. Level: beginner. Format: concept_explainer. Language: si. Flags: wrong_language.

31. [Ynhr-F5WwOA] Tensorflow Fashion MNIST Tutorial. | Tensorflow Image Classification | Neural Networks Deep learning - 19 min
   Curriculum's reason: Popular result (182 views) for 'PyTorch image classification project CNN CIFAR-10 Fashion-MNIST full tutorial from scratch'.
   REFERENCE SUMMARY: This tutorial trains a deep neural network using TensorFlow/Keras to classify Fashion MNIST clothing images (t-shirts, sneakers, ankle boots, etc.). The video covers data loading, normalization, visualization, model creation with Flatten and Dense layers, compilation with loss and optimizer, training with epochs, and evaluation on test data. Builds: Fashion MNIST image classifier using TensorFlow/Keras. Level: beginner. Format: project_build. Language: en. Flags: wrong_language.

32. [8rqSbzap8oo] Curing Overfitting with Regularization | Season 1 | Part 29 - 5 min
   Curriculum's reason: Popular result (100 views) for 'overfitting underfitting validation loss PyTorch regularization dropout data augmentation tutorial'.
   REFERENCE SUMMARY: This video teaches how to recognize and fix overfitting in neural networks using three complementary techniques: batch normalization, spatial dropout, and data augmentation. Using Fashion MNIST as a hands-on example in PyTorch, the instructor systematically demonstrates how each regularization technique reduces the gap between training and validation loss, ultimately achieving production-grade generalization. Builds: Training and regularizing a convolutional neural network on Fashion MNIST with batch normalization, spatial dropout, and data augmentation. Level: intermediate. Format: project_build. Language: en.

33. [NbPslfbNfjA] Simple CNN (train from scratch) - MNIST datasets - 3 min
   Curriculum's reason: Popular result (88 views) for 'PyTorch image classification project CNN CIFAR-10 Fashion-MNIST full tutorial from scratch'.
   REFERENCE SUMMARY:  Level: beginner. Format: other. Language: vi. Flags: wrong_language, poor_transcript.

34. [TH8cvKLSXGg] [ML1] Machine Learning Fundamentals: Supervised Learning & Linear Regression - 12 min
   Curriculum's reason: Popular result (64 views) for 'machine learning fundamentals for beginners with math intuition supervised learning loss function'.
   REFERENCE SUMMARY: This video teaches the mathematical foundations of supervised machine learning, covering the prediction equation (ŷ = f_θ(x)), loss functions (MSE), and gradient descent optimization. It explains how to represent multiple features using vectors and design matrices, and introduces the concepts of generalization, train/validation/test splits, and overfitting using house price prediction as a worked example. Level: beginner. Format: concept_explainer. Language: en.

35. [fZtjO2cs3VQ] Backpropagation Explained By Hand: Two-Layer Neural Network, Chain Rule and Gradient Descent - 8 min
   Curriculum's reason: Popular result (36 views) for 'gradient descent and backpropagation explained calculus chain rule neural network from scratch'.
   REFERENCE SUMMARY: A detailed hand-worked derivation of backpropagation for a two-layer neural network, showing the forward pass, backward pass using the chain rule, and gradient descent weight updates. Every derivative is computed step-by-step with real numbers, then verified numerically against finite differences, demonstrating how neural networks learn by measuring error and nudging weights. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

36. [DK1GBJ-yWgw] Fixing loss.backward() Gradient Issues in PyTorch S3FD PGD Attack - 4 min
   Curriculum's reason: Popular result (1 views) for 'PyTorch tensors and autograd tutorial for numpy users code along'.
   REFERENCE SUMMARY: This video diagnoses and fixes a common PyTorch error where loss.backward() fails in adversarial PGD attacks because the computational graph is broken by premature conversion to NumPy arrays. The solution is to preserve tensors throughout the computation and avoid .data and .numpy() calls that detach gradients from the autograd system. Level: advanced. Format: concept_explainer. Language: en. Flags: too_advanced_for_learner, off_topic.

### career_switch_ml_foundations / S3

Planned viewing time: 359 of 1200 min.
Assumptions stated: The 1200 minutes is pure viewing time, so it covers about 20 hours of videos with no time reserved for practice.; Because the learner likes code-along videos, the plan favors tutorials where the presenter writes code live.; 'Small image classifier' means a CNN trained on MNIST, Fashion-MNIST or CIFAR-10, not a large pretrained model pipeline.; Each video or course part should fit within a 90-minute sitting, so long courses are picked in chunks of 90 minutes or less.; Calculus and linear algebra are already known, so math-focused videos should build intuition for ML and not reteach prerequisites.
Warnings to the learner: Picks total about 359 minutes of the 1200-minute budget (about 30%). About 841 minutes are unused because the pool has no more good, non-redundant PyTorch material, and I did not pad with weak or redundant videos. | Every pick is under 90 minutes, so the 90-minute sitting limit is met without splitting. The longest is the Stanford lecture at 78 minutes. | Duration is taken from the 'minutes' field, but several transcripts' segment maps run longer than that. Real lengths may differ, so check the total against your sittings. | Tensor and autograd coverage is thin: only the StatQuest video teaches them in code, and the other candidates are flagged lectures or overviews. Practice tensor operations and requires_grad yourself in the PyTorch docs.

1. [TH8cvKLSXGg] [ML1] Machine Learning Fundamentals: Supervised Learning & Linear Regression - 12 min
   Curriculum's reason: Gives the supervised-learning framing: prediction equation, loss (MSE), feature vectors, gradient descent and the train/validation/test split. It is pitched at someone with linear algebra who needs the ML vocabulary first.
   Quote [00:43]: "We want to learn them from the available data. That's the fundamental idea behind supervised machine learning."
   Quote [08:47]: "A loss function measures the discrepancy between the model's prediction and the actual target."
   REFERENCE SUMMARY: This video teaches the mathematical foundations of supervised machine learning, covering the prediction equation (ŷ = f_θ(x)), loss functions (MSE), and gradient descent optimization. It explains how to represent multiple features using vectors and design matrices, and introduces the concepts of generalization, train/validation/test splits, and overfitting using house price prediction as a worked example. Level: beginner. Format: concept_explainer. Language: en.

2. [EuBBz3bI-aA] Machine Learning Fundamentals: Bias and Variance - 7 min
   Curriculum's reason: Short, intuitive treatment of train/test split, bias, variance and overfitting. It sets up the later evaluation material.
   Quote [01:49]: "The first thing we do is split the data into two sets, one for training the machine learning algorithms and one for testing them"
   Quote [03:21]: "The inability for a machine learning method like linear regression to capture the true relationship is called Bias"
   REFERENCE SUMMARY: This video explains bias and variance, two fundamental ML concepts, using intuitive examples of fitting curves to mouse weight-height data. It demonstrates how simple models (linear regression) have high bias but low variance, while complex models (squiggly lines) have low bias but high variance, and introduces the concept of overfitting and the need to find a sweet spot between model complexity. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

3. [4b4MUYve_U8] Stanford CS229: Machine Learning - Linear Regression and Gradient Descent |  Lecture 2 (Autumn 2018) - 78 min
   Curriculum's reason: A full lecture that derives the squared-error cost and the gradient descent update rule, including batch vs stochastic. It suits a learner who wants the math behind training and already has calculus and linear algebra.
   Quote [25:00]: "minimize the square difference between what the hypothesis outputs, H sub-script theta of X, minus Y, squared, right"
   Quote [30:27]: "gradient descent, we are going to start with some value of theta, um, and it could be, you know, theta equals the vector of all zeros"
   REFERENCE SUMMARY: This Stanford lecture covers supervised learning and linear regression, introducing the mathematical foundations of a learning algorithm including the hypothesis function, cost function (ordinary least squares), and two approaches to optimization: gradient descent and the normal equations. The instructor derives the gradient descent update rule and demonstrates how to minimize the squared error loss through iterative parameter updates, as well as providing a closed-form solution via the normal equations. Level: beginner. Format: lecture. Language: en. Flags: pure_theory.

4. [vsWrXfO3wWw] Machine Learning Tutorial Python - 4: Gradient Descent and Cost Function - 28 min
   Curriculum's reason: Code-along that implements gradient descent in plain Python on a linear regression cost function. It shows partial derivatives, learning rate and the update loop in code the learner can already read.
   Quote [07:30]: "gradient descent is that algorithm that finds best fit line for given training data set in very less number of iteration"
   Quote [25:30]: "partial derivatives gives you a slope and then once you have direction, now you need to take a step, so for the step, you use something called a learning rate"
   REFERENCE SUMMARY: This tutorial covers gradient descent and cost functions for machine learning, using linear regression on home price prediction as the concrete example. The instructor explains the math behind mean squared error, partial derivatives, and the gradient descent algorithm, then implements it in Python code to find the best-fit line for training data. Builds: Linear regression model using gradient descent to predict home prices. Level: beginner. Format: concept_explainer. Language: en.

5. [IHZwWFHWa-w] Gradient descent, how neural networks learn | Deep Learning Chapter 2 - 21 min
   Curriculum's reason: Visual explanation of cost functions, the negative gradient as steepest descent, and how this trains a digit-recognizing network. It builds the intuition the learner asked for.
   Quote [00:04]: "the first is to introduce the idea of gradient descent, which underlies not only how neural networks learn, but how a lot of other machine learning works as well"
   Quote [13:59]: "the negative gradient of the cost function is just a vector. It's some direction inside this insanely huge input space that tells you which nudges to all of those numbers is going to cause the most rapid decrease to the cost function"
   REFERENCE SUMMARY: This video explains gradient descent and backpropagation—the core algorithms that enable neural networks to learn from training data. Using a handwritten digit recognition example, it visualizes how cost functions work, how gradients point toward lower cost, and why repeatedly stepping in the negative gradient direction minimizes error over thousands of training examples. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

6. [Ilg3gGewQ5U] Backpropagation, intuitively | Deep Learning Chapter 3 - 13 min
   Curriculum's reason: Explains backpropagation intuitively: how each weight's effect on the cost is computed, and mini-batch stochastic gradient descent. It prepares the learner for what loss.backward() does.
   Quote [02:23]: "Back propagation, the topic of this video, is an algorithm for computing that crazy complicated gradient."
   Quote [03:24]: "The magnitude of each component here is telling you how sensitive the cost function is to each weight and bias."
   REFERENCE SUMMARY: This video explains backpropagation, the core algorithm for training neural networks, using intuitive visual explanations without heavy mathematics. It walks through how a single training example propagates error signals backwards through the network to determine how weights and biases should be adjusted, and introduces stochastic gradient descent as a practical computational shortcut. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

7. [tIeHLnjs5U8] Backpropagation calculus | Deep Learning Chapter 4 - 10 min
   Curriculum's reason: Formal chain-rule derivation of the gradients of cost with respect to weights and biases. It gives the math side of backprop and fits a learner with a calculus background.
   Quote [05:46]: "the chain rule, where multiplying together these three ratios gives us the sensitivity of C to small changes in WL"
   Quote [10:27]: "you can just keep iterating this same chain rule idea backwards to see how sensitive the cost function is to previous weights and previous biases"
   REFERENCE SUMMARY: This video provides a formal mathematical treatment of backpropagation, focusing on how to compute derivatives of the cost function with respect to weights and biases using the chain rule from calculus. It covers single-neuron and multi-neuron layers, explaining how sensitivity to weights, biases, and activations propagates backwards through the network. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

8. [fZtjO2cs3VQ] Backpropagation Explained By Hand: Two-Layer Neural Network, Chain Rule and Gradient Descent - 8 min
   Curriculum's reason: Works backprop through a two-layer network with real numbers, checks the gradients numerically, and ends with weight updates. It makes the earlier intuition concrete just before autograd.
   Quote [00:23]: "First, a forward pass where numbers flow from the inputs to a loss. Second, a backward pass where the error flows back through the network layer by layer using the chain rule."
   Quote [10:12]: "Each step moves every parameter against its gradient with learning rate equal to 0.5. The loss falls at every step."
   REFERENCE SUMMARY: A detailed hand-worked derivation of backpropagation for a two-layer neural network, showing the forward pass, backward pass using the chain rule, and gradient descent weight updates. Every derivative is computed step-by-step with real numbers, then verified numerically against finite differences, demonstrating how neural networks learn by measuring error and nudging weights. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

9. [FHdlXe1bSe4] The StatQuest Introduction to PyTorch - 23 min
   Curriculum's reason: Code-along that builds a small network from tensors and nn.Parameter, then runs a training loop with loss.backward() and optimizer.step(). It is the best coded link between backprop and PyTorch autograd in the pool. It is flagged surface_intro, but no unflagged candidate covers tensors and autograd in code.
   Quote [06:59]: "So we create a new variable called w00, and make it a neural network Parameter."
   Quote [28:21]: "Next we use loss.backward() to calculate the derivative of the loss function with respect to the parameter"
   REFERENCE SUMMARY: This video walks through building a simple neural network from scratch in PyTorch, starting with a pre-defined architecture that fits a drug-dose effectiveness dataset using ReLU activations. It covers creating tensors and parameters, building a forward pass, graphing predictions, and then optimizing a single bias parameter using backpropagation and stochastic gradient descent with a training loop. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

10. [JHWqWIoac2I] Create a Basic Neural Network Model - Deep Learning with PyTorch 5 - 16 min
   Curriculum's reason: Builds an nn.Module with fully connected layers and a forward pass with ReLU, with live debugging. It shows how a PyTorch model class is structured before moving to CNNs.
   Quote [02:24]: "You have an input layer here, an output layer here, and then inside of here, we have hidden layers of neurons."
   Quote [17:04]: "fully connected one and fully connected two, because they are fully connected."
   REFERENCE SUMMARY: This video builds a basic neural network class in PyTorch for classifying Iris flowers. It covers defining model architecture with fully connected layers, implementing the forward pass with ReLU activation, instantiating the model, and debugging common errors. The focus is on hands-on PyTorch code rather than mathematical foundations. Builds: A simple neural network classifier for Iris flower classification with input layer (4 features), two hidden layers (8 neurons each), and output layer (3 classes). Level: beginner. Format: project_build. Language: en.

11. [zfiSAzpy9NM] Simple explanation of convolutional neural network | Deep Learning Tutorial 23 (Tensorflow & Python) - 24 min
   Curriculum's reason: Visual intuition for convolution filters, feature maps, ReLU, pooling and the full conv-pool-dense architecture. It is flagged surface_intro and pure_theory, but the learner wants concept intuition. It uses TensorFlow only for naming.
   Quote [10:04]: "The way convolution operation works is you take 3x3 grid from your original image and multiply individual numbers with this filter."
   Quote [13:24]: "When you apply this filter or a convolution operation, you are generating a feature map that has that particular feature detected."
   REFERENCE SUMMARY: This video provides a visual, intuitive explanation of convolutional neural networks (CNNs) for image recognition, avoiding heavy mathematics. It covers how CNNs use filters to detect features like edges and facial components, applies convolution and pooling operations to reduce computation, and combines these with dense layers for classification. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

12. [jDe5BAsT2-Y] Convolutional Neural Networks from Scratch | In Depth - 13 min
   Curriculum's reason: Walks through the actual arithmetic of convolution, max pooling, flattening and the fully connected output in a trained MNIST CNN. It supplies the math view of CNNs for a learner who wants more than the diagram.
   Quote [00:50]: "First off, we will perform a convolution with two filters that have a filter size of 5x5x1 and use an activation function called ReLU."
   Quote [17:30]: "A fully connected layer consists of input nodes and output nodes that are connected with weights and biases."
   REFERENCE SUMMARY: This video provides an in-depth walkthrough of how a convolutional neural network processes images through forward propagation, using a pretrained model on MNIST with 95.4% accuracy. The video visualizes and explains the mathematics of each layer: convolutions with filters and activation functions (ReLU and sigmoid), max pooling, flattening, and the fully connected output layer. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

13. [pDdP0TFzsoQ] PyTorch Tutorial 14 - Convolutional Neural Network (CNN) - 22 min
   Curriculum's reason: Code-along that implements a CIFAR-10 CNN in PyTorch with Conv2d, pooling, flattening, a training loop and accuracy evaluation. It is the first end-to-end PyTorch CNN, straight after the CNN concepts.
   Quote [27:09]: "now after these convolutional layers, when we put them into our classification layers, we want to flatten the 3D tensor to a 1D tensor"
   REFERENCE SUMMARY: Implements a CNN from scratch in PyTorch to classify CIFAR-10 images. Covers CNN architecture concepts (convolutional filters, pooling layers, fully connected layers), building a multi-layer CNN model with Conv2d and Linear layers, and training it end-to-end with a training loop and accuracy evaluation. Builds: CIFAR-10 image classifier CNN in PyTorch. Level: intermediate. Format: project_build. Language: en.

14. [fRqQwCXSeqo] 13 PyTorch tutorial - Popular techniques to prevent the overfitting in a Neural Networks - 16 min
   Curriculum's reason: Explains how to detect overfitting with validation data and covers early stopping, augmentation, L1/L2 and dropout. It shows nn.Dropout and weight_decay in PyTorch.
   Quote [02:27]: "The best way to tell if your model is overfitted is to use the validation data set during training"
   Quote [10:25]: "The most common regularization method is to add a penalty to the loss function in in proportion to the size of the weights in the model"
   REFERENCE SUMMARY: This tutorial explains overfitting in neural networks and demonstrates five techniques to prevent it: reducing network complexity, early stopping, adding more data, data augmentation, regularization (L1/L2), and dropout. The video includes code examples showing how to implement dropout and L2 regularization in PyTorch using nn.Dropout and the weight_decay parameter in optimizers. Level: intermediate. Format: concept_explainer. Language: en.

15. [8rqSbzap8oo] Curing Overfitting with Regularization | Season 1 | Part 29 - 5 min
   Curriculum's reason: Demonstrates an overfitting gap between training and validation loss on a Fashion-MNIST CNN in PyTorch. It then reduces the gap with batch norm, spatial dropout and augmentation.
   Quote [03:39]: "This diverging space is the overfitting gap, confirming the network stops learning universal properties and starts memorizing specific training noise."
   Quote [05:31]: "By artificially expanding the structural variety of the training data, we provide the network with a much wider empirical foundation."
   REFERENCE SUMMARY: This video teaches how to recognize and fix overfitting in neural networks using three complementary techniques: batch normalization, spatial dropout, and data augmentation. Using Fashion MNIST as a hands-on example in PyTorch, the instructor systematically demonstrates how each regularization technique reduces the gap between training and validation loss, ultimately achieving production-grade generalization. Builds: Training and regularizing a convolutional neural network on Fashion MNIST with batch normalization, spatial dropout, and data augmentation. Level: intermediate. Format: project_build. Language: en.

16. [hkiBZLRFvO4] Building a CNN using PyTorch | Video 11 | CampusX - 32 min
   Curriculum's reason: Builds a Fashion-MNIST CNN in PyTorch, reaching 92% test accuracy while noticing about 99.9% training accuracy (overfitting). This ties the project back to the evaluation lessons.
   Quote [13:21]: "CNN ki sabse badi khaasiyat ye hai ki agar aap usko grid based data doge toh woh uske andar ke jo spatial patterns hain toh unko bahut acche se woh identify kar pata hai"
   Quote [17:06]: "Convolution layer mein aap kya karte ho ki aapke paas chhote-chhote filters hote hain, let's say 3x3 ke aur aap in filters ko uthate ho aur aap apne image ke upar un filters ko apply karte ho"
   REFERENCE SUMMARY: This video builds a convolutional neural network (CNN) from scratch in PyTorch to classify Fashion MNIST images. The instructor walks through CNN architecture design (convolution layers, pooling, fully connected layers), implements it in Google Colab by modifying previous ANN code, and achieves 92% test accuracy while observing some overfitting (99.9% training accuracy). Builds: CNN image classifier for Fashion MNIST dataset. Level: intermediate. Format: project_build. Language: hi.

17. [CtzfbUwrYGI] Image Classification CNN in PyTorch - 30 min
   Curriculum's reason: Complete CIFAR-10 pipeline in PyTorch: transforms, a Conv2d/pool/linear CNN, a training loop with zero_grad, and test accuracy. It is a second full project to consolidate everything.
   Quote [00:24]: "we're going to load the data, we're going to have training and testing data, we're going to train the model, and we're going to evaluate the model"
   Quote [29:06]: "optimizer.zero_grad, so we reset the gradients, we set all of the gradients to none, and then what we do is we say the outputs"
   REFERENCE SUMMARY: Build and train a CNN image classifier on CIFAR-10 in PyTorch from scratch. The video covers data loading with transformations, designing a convolutional neural network with Conv2d, pooling, and fully connected layers, implementing a training loop with loss and optimizer, and evaluating accuracy on test data. Builds: Image classifier CNN trained on CIFAR-10 dataset to classify 10 image classes (dogs, cats, horses, ships, trucks, cars, etc.). Level: intermediate. Format: project_build. Language: en.

Considered and dropped:
- Image classification using CNN (CIFAR10 dataset) | Deep Learning Tutorial 24 (Tensorflow & Python): Strong CNN/CIFAR-10 content, but it is TensorFlow/Keras and flagged wrong_language for a PyTorch goal.
- Regularization | L1 & L2 | Dropout | Data Augmentation | Early Stopping |  Deep Learning Part 4: Good regularization math, but it duplicates the datahacker video's topics and has no PyTorch code.
- Regularization in a Neural Network | Dealing with overfitting: Conceptual regularization overview that adds little beyond the datahacker and ByteQuest-style content, with no code.
- Convolutional Neural Network Model - Deep Learning with PyTorch 16: Only defines the CNN class and optimizer with no training or evaluation, and the CNN model-building is already covered by Loeber and CampusX.
- PyTorch a framework for research of dynamic deep learning models - Adam Paszke: Lecture on PyTorch's design (define-by-run) rather than a code-along. It is flagged pure_theory/surface_intro, and the StatQuest video covers autograd in code.
- Exploring the Deep Learning Framework PyTorch - Stephanie Kim: Overview talk heavy on deployment (TorchScript, ONNX) with little hands-on tensor or autograd teaching.
- Pytorch CNN example (Convolutional Neural Network): Short MNIST CNN code-along, but it explicitly skips how convolutions work and is flagged surface_intro. Other candidates cover CNNs more fully.
- Tutorial 6-Chain Rule of Differentiation with BackPropagation: Chain-rule backprop explanation that duplicates the 3Blue1Brown chapters, which are clearer for this learner.
- PyTorch Sinhala Tutorial #2 - Auto Grad and Tensor Functions - PyTorch in Sinhala: Covers tensors and autograd but is flagged wrong_language (Sinhala).
- Fixing loss.backward() Gradient Issues in PyTorch S3FD PGD Attack: Flagged too_advanced_for_learner and off_topic (adversarial PGD attack debugging).

### career_switch_ml_foundations / S4

Planned viewing time: 291 of 1200 min.
Assumptions stated: Learner is fine with the CS229 lecture as a math-heavy start because they have calculus and linear algebra and asked for the math intuition.; Tensors and autograd are learned inside the StatQuest and CNN code-alongs. The pool has no standalone tensor-operations video in English.; The learner can do the Colab or local setup themselves.
Warnings to the learner: Only about 5.2 hours (about 313 min) of the 1200-minute budget is used. The candidate pool has no more good, non-duplicate English material, and I chose not to pad it. | Suggested sittings, each 90 minutes or less: (1) CS229 lecture; (2) codebasics GD, 3Blue1Brown ch.2–4, bias/variance; (3) StatQuest PyTorch, John Elder NN, codebasics CNN, Erai CNN; (4) NeuralNine CIFAR-10, AssemblyAI, datahacker. | No video covers PyTorch tensor operations or Dataset/DataLoader as a standalone topic. Learn them from the code-alongs and the official PyTorch docs. | No confusion-matrix or precision/recall coverage was found; evaluation here is accuracy and train-versus-validation comparison.

1. [4b4MUYve_U8] Stanford CS229: Machine Learning - Linear Regression and Gradient Descent |  Lecture 2 (Autumn 2018) - 78 min
   Curriculum's reason: A rigorous lecture on supervised learning, the squared-error cost and the derivation of the gradient descent update. It suits an engineer with calculus and linear algebra who wants the math. Sitting 1 (78 min).
   Quote [25:00]: "minimize the square difference between what the hypothesis outputs, H sub-script theta of X, minus Y, squared, right"
   Quote [30:27]: "gradient descent, we are going to start with some value of theta, um, and it could be, you know, theta equals the vector of all zeros"
   REFERENCE SUMMARY: This Stanford lecture covers supervised learning and linear regression, introducing the mathematical foundations of a learning algorithm including the hypothesis function, cost function (ordinary least squares), and two approaches to optimization: gradient descent and the normal equations. The instructor derives the gradient descent update rule and demonstrates how to minimize the squared error loss through iterative parameter updates, as well as providing a closed-form solution via the normal equations. Level: beginner. Format: lecture. Language: en. Flags: pure_theory.

2. [vsWrXfO3wWw] Machine Learning Tutorial Python - 4: Gradient Descent and Cost Function - 28 min
   Curriculum's reason: A code-along that implements gradient descent with MSE and partial derivatives in Python, applying last session's math. Sitting 2 starts here.
   Quote [07:30]: "gradient descent is that algorithm that finds best fit line for given training data set in very less number of iteration"
   Quote [25:30]: "partial derivatives gives you a slope and then once you have direction, now you need to take a step, so for the step, you use something called a learning rate"
   REFERENCE SUMMARY: This tutorial covers gradient descent and cost functions for machine learning, using linear regression on home price prediction as the concrete example. The instructor explains the math behind mean squared error, partial derivatives, and the gradient descent algorithm, then implements it in Python code to find the best-fit line for training data. Builds: Linear regression model using gradient descent to predict home prices. Level: beginner. Format: concept_explainer. Language: en.

3. [IHZwWFHWa-w] Gradient descent, how neural networks learn | Deep Learning Chapter 2 - 21 min
   Curriculum's reason: Gives the geometric intuition for the cost function over thousands of weights and for the negative gradient as the steepest-descent direction.
   Quote [07:30]: "the cost function is a layer of complexity on top of that. It takes as its input those 13,000 or so weights and biases"
   Quote [13:59]: "the negative gradient of the cost function is just a vector. It's some direction inside this insanely huge input space that tells you which nudges to all of those numbers is going to cause the most rapid decrease to the cost function"
   REFERENCE SUMMARY: This video explains gradient descent and backpropagation—the core algorithms that enable neural networks to learn from training data. Using a handwritten digit recognition example, it visualizes how cost functions work, how gradients point toward lower cost, and why repeatedly stepping in the negative gradient direction minimizes error over thousands of training examples. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

4. [Ilg3gGewQ5U] Backpropagation, intuitively | Deep Learning Chapter 3 - 13 min
   Curriculum's reason: Explains intuitively how backpropagation computes the gradient, and introduces mini-batches and stochastic gradient descent, which the PyTorch training loops use.
   Quote [02:23]: "Back propagation, the topic of this video, is an algorithm for computing that crazy complicated gradient."
   Quote [03:24]: "The magnitude of each component here is telling you how sensitive the cost function is to each weight and bias."
   REFERENCE SUMMARY: This video explains backpropagation, the core algorithm for training neural networks, using intuitive visual explanations without heavy mathematics. It walks through how a single training example propagates error signals backwards through the network to determine how weights and biases should be adjusted, and introduces stochastic gradient descent as a practical computational shortcut. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

5. [tIeHLnjs5U8] Backpropagation calculus | Deep Learning Chapter 4 - 10 min
   Curriculum's reason: Applies the chain rule to the cost function, which formalizes backprop and shows what autograd automates. It fits a learner who knows calculus.
   Quote [05:46]: "the chain rule, where multiplying together these three ratios gives us the sensitivity of C to small changes in WL"
   Quote [06:43]: "the derivative of C with respect to AL works out to be two times AL minus Y"
   REFERENCE SUMMARY: This video provides a formal mathematical treatment of backpropagation, focusing on how to compute derivatives of the cost function with respect to weights and biases using the chain rule from calculus. It covers single-neuron and multi-neuron layers, explaining how sensitivity to weights, biases, and activations propagates backwards through the network. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

6. [EuBBz3bI-aA] Machine Learning Fundamentals: Bias and Variance - 7 min
   Curriculum's reason: A short intro to the train/test split, bias, variance and overfitting. It prepares the learner to read train-versus-test accuracy later. Ends sitting 2 (about 79 min total).
   Quote [01:49]: "The first thing we do is split the data into two sets, one for training the machine learning algorithms and one for testing them"
   Quote [03:21]: "The inability for a machine learning method like linear regression to capture the true relationship is called Bias"
   REFERENCE SUMMARY: This video explains bias and variance, two fundamental ML concepts, using intuitive examples of fitting curves to mouse weight-height data. It demonstrates how simple models (linear regression) have high bias but low variance, while complex models (squiggly lines) have low bias but high variance, and introduces the concept of overfitting and the need to find a sweet spot between model complexity. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

7. [FHdlXe1bSe4] The StatQuest Introduction to PyTorch - 23 min
   Curriculum's reason: Builds a network in PyTorch with Parameters, then uses loss.backward() and optimizer.step() in a training loop. It links the backprop theory to autograd. Sitting 3 begins here.
   Quote [06:59]: "So we create a new variable called w00, and make it a neural network Parameter."
   Quote [28:21]: "Next we use loss.backward() to calculate the derivative of the loss function with respect to the parameter"
   REFERENCE SUMMARY: This video walks through building a simple neural network from scratch in PyTorch, starting with a pre-defined architecture that fits a drug-dose effectiveness dataset using ReLU activations. It covers creating tensors and parameters, building a forward pass, graphing predictions, and then optimizing a single bias parameter using backpropagation and stochastic gradient descent with a training loop. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

8. [JHWqWIoac2I] Create a Basic Neural Network Model - Deep Learning with PyTorch 5 - 16 min
   Curriculum's reason: Code-along showing how to write an nn.Module class with fully connected layers and a forward pass, the pattern every later model reuses.
   Quote [02:24]: "You have an input layer here, an output layer here, and then inside of here, we have hidden layers of neurons."
   Quote [17:04]: "fully connected one and fully connected two, because they are fully connected."
   REFERENCE SUMMARY: This video builds a basic neural network class in PyTorch for classifying Iris flowers. It covers defining model architecture with fully connected layers, implementing the forward pass with ReLU activation, instantiating the model, and debugging common errors. The focus is on hands-on PyTorch code rather than mathematical foundations. Builds: A simple neural network classifier for Iris flower classification with input layer (4 features), two hidden layers (8 neurons each), and output layer (3 classes). Level: beginner. Format: project_build. Language: en.

9. [zfiSAzpy9NM] Simple explanation of convolutional neural network | Deep Learning Tutorial 23 (Tensorflow & Python) - 24 min
   Curriculum's reason: Visual intuition for CNNs: convolution filters, feature maps, ReLU and pooling stacked into a classifier. The learner has no CNN background.
   Quote [10:04]: "The way convolution operation works is you take 3x3 grid from your original image and multiply individual numbers with this filter."
   Quote [13:24]: "When you apply this filter or a convolution operation, you are generating a feature map that has that particular feature detected."
   REFERENCE SUMMARY: This video provides a visual, intuitive explanation of convolutional neural networks (CNNs) for image recognition, avoiding heavy mathematics. It covers how CNNs use filters to detect features like edges and facial components, applies convolution and pooling operations to reduce computation, and combines these with dense layers for classification. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

10. [jDe5BAsT2-Y] Convolutional Neural Networks from Scratch | In Depth - 13 min
   Curriculum's reason: Walks through the matrix math of a CNN forward pass (convolution, max pooling, flatten, fully connected layer). It adds the math side that the learner wants. Ends sitting 3 (about 76 min).
   Quote [00:50]: "First off, we will perform a convolution with two filters that have a filter size of 5x5x1 and use an activation function called ReLU."
   Quote [17:30]: "A fully connected layer consists of input nodes and output nodes that are connected with weights and biases."
   REFERENCE SUMMARY: This video provides an in-depth walkthrough of how a convolutional neural network processes images through forward propagation, using a pretrained model on MNIST with 95.4% accuracy. The video visualizes and explains the mathematics of each layer: convolutions with filters and activation functions (ReLU and sigmoid), max pooling, flattening, and the fully connected output layer. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

11. [CtzfbUwrYGI] Image Classification CNN in PyTorch - 30 min
   Curriculum's reason: Full code-along that loads CIFAR-10 with transforms, defines a Conv2d CNN, writes the training loop with zero_grad, and evaluates test accuracy. This is the capstone for the goal. Sitting 4 begins here.
   Quote [00:24]: "we're going to load the data, we're going to have training and testing data, we're going to train the model, and we're going to evaluate the model"
   Quote [13:30]: "we have a 5 * 5 pixel kernel that moves across the image, calculates a dot product and creates feature maps"
   REFERENCE SUMMARY: Build and train a CNN image classifier on CIFAR-10 in PyTorch from scratch. The video covers data loading with transformations, designing a convolutional neural network with Conv2d, pooling, and fully connected layers, implementing a training loop with loss and optimizer, and evaluating accuracy on test data. Builds: Image classifier CNN trained on CIFAR-10 dataset to classify 10 image classes (dogs, cats, horses, ships, trucks, cars, etc.). Level: intermediate. Format: project_build. Language: en.

12. [EehRcPo1M-Q] Regularization in a Neural Network | Dealing with overfitting - 12 min
   Curriculum's reason: Explains why overfitting happens and covers L1/L2 regularization, dropout, early stopping and data augmentation.
   Quote [00:44]: "Overfitting is when your model really closely fits the training data, so much so that it is not able to generalize really well to the real world."
   Quote [03:59]: "Regularization is a way to limit this flexibility that the model has in hopes to avoid overfitting."
   REFERENCE SUMMARY: A conceptual explanation of regularization techniques used to combat overfitting in neural networks. The video covers L1 and L2 regularization, dropout, early stopping, and data augmentation, explaining why high weights cause overfitting and how each technique reduces model flexibility to improve generalization. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

13. [fRqQwCXSeqo] 13 PyTorch tutorial - Popular techniques to prevent the overfitting in a Neural Networks - 16 min
   Curriculum's reason: Shows how to detect overfitting with a validation set and how to apply nn.Dropout and weight_decay in PyTorch, so the learner can fix an overfitting classifier. Sitting 4 totals about 80 min.
   Quote [02:27]: "The best way to tell if your model is overfitted is to use the validation data set during training"
   Quote [10:25]: "The most common regularization method is to add a penalty to the loss function in in proportion to the size of the weights in the model"
   REFERENCE SUMMARY: This tutorial explains overfitting in neural networks and demonstrates five techniques to prevent it: reducing network complexity, early stopping, adding more data, data augmentation, regularization (L1/L2), and dropout. The video includes code examples showing how to implement dropout and L2 regularization in PyTorch using nn.Dropout and the weight_decay parameter in optimizers. Level: intermediate. Format: concept_explainer. Language: en.

## go_dev_rust_ownership

```
Goal: Get comfortable with Rust ownership, borrowing and lifetimes so I can port a small Go CLI tool
Time budget: 240 minutes
Background: Senior Go developer, 8 years; wrote systems tools and services
Already knows: systems programming, pointers and memory, concurrency, Go, CLI tools, basic syntax of C-like languages
Does not know yet: ownership and moves, borrowing and references, lifetimes, traits, error handling with Result, Result-based error handling
Constraints: Skip anything that explains what a variable or a loop is. I want depth on the borrow checker. My Go CLI returns errors everywhere, so I also need idiomatic error handling with Result and the ? operator.
```

### go_dev_rust_ownership / S1

Planned viewing time: 204 of 240 min.
Assumptions stated: Learner knows stack/heap and pointers, so the stack-vs-heap segment of the ownership video can be skimmed.; Generics and traits are only needed at the level required for trait bounds, dyn dispatch and error traits.; Async/Tokio is not needed for a small CLI.
Warnings to the learner: Total is about 204 of 240 minutes. I left the remainder unused rather than pad with weak videos. | The Ardan webinar window (1200–4000 s) is estimated from quote timestamps, so check the edges. | Ownership and lifetimes overlap a little between the Let's Get Rusty video and the conference talk. I kept both because the first teaches the mechanics and the second gives the model (Drop, Rc, Send/Sync). | Traits coverage is shallow, and no video on associated types, iterators or closures was found. The Rust Book chapter on traits would fill that gap.

1. [VFIOSWy93H0] Understanding Ownership in Rust - 26 min
   Curriculum's reason: Walks through moves, Copy, shared and mutable references and the borrow-checker rules with compiler error demos. Skim the early stack/heap section, which you already know.
   Quote [07:08]: "each value in rust has a variable that's called its owner so one variable one owner"
   Quote [13:11]: "instead of calculate length taking a string we'll make it take a reference to a string"
   REFERENCE SUMMARY: A comprehensive walkthrough of Rust's ownership model, covering how Rust manages memory without garbage collection through compile-time rules. The video explains stack vs heap allocation, ownership rules and moves, borrowing with references (immutable and mutable), borrow checker rules, and string slices with practical examples and compiler error demonstrations. Level: intermediate. Format: concept_explainer. Language: en.

2. [zfb1y8yn8QI] Understanding Rust – Or How to Stop Worrying & Love the Borrow-Checker • Steve Smith • YOW! 2024 - 42 min
   Curriculum's reason: Conference talk that frames the compiler as a deterministic garbage collector, which suits a GC-language veteran. It covers lifetimes, Drop, Box, Rc and Send/Sync, which connect to your concurrency background.
   Quote [07:16]: "the compiler is your garbage collector. See all languages are garbage collected."
   Quote [21:24]: "Rust can infer a lot of lifetimes, it can't infer all of them. Sometimes you need to make a promise to the Rust compiler."
   REFERENCE SUMMARY: Steve Smith delivers a conference talk on understanding Rust's borrow checker and ownership system, aimed at developers who have basic Rust knowledge but struggle with the learning curve. The talk covers ownership, borrowing rules, lifetimes, Drop trait, Box, reference counting (Rc), and threading constraints (Send/Sync), positioning the compiler as a garbage collector that ensures memory safety deterministically. Level: intermediate. Format: lecture. Language: en. Flags: pure_theory.

3. [juIINGuZyBc] Rust Lifetimes Finally Explained! - 19 min
   Curriculum's reason: Covers lifetime annotations, the three elision rules, structs holding references and 'static, with worked examples.
   Quote [04:55]: "generic lifetime annotations describe the relationship between the lifetimes of multiple references and how they relate to each other"
   Quote [07:02]: "the lifetime of the returned reference will be the same as the smallest lifetime of the arguments"
   REFERENCE SUMMARY: This video explains Rust lifetimes in depth, starting with the borrow checker and dangling references, then covering generic lifetime annotations, elision rules, struct lifetime annotations, and practical examples combining lifetimes with traits and generics. The instructor demonstrates how the compiler uses lifetime relationships to prevent dangling references and when manual lifetime annotations are required. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

4. [gRAVZv7V91Q] but what is 'a lifetime? - 12 min
   Curriculum's reason: Gives a deeper mental model of what 'a means, using regions, liveness and subtyping. It fills the gap left by the official resources and builds the borrow-checker intuition you asked for.
   Quote [00:21]: "the problem is that the official rust learning resources only tell you about the particle interpretation leaving out half the picture"
   Quote [05:38]: "a reference really is just a special kind of pointer special because it has this tick a that the compiler uses to validate that the reference never points to invalid memory"
   REFERENCE SUMMARY: This video explains two ways to think about lifetimes in Rust: the traditional "particle" interpretation (lifetimes as scopes where variables live) and an alternative "wave" interpretation (lifetimes as regions of memory that references can point into). The presenter demonstrates through examples how thinking of lifetimes as memory regions, combined with liveness analysis and subtyping, provides a more intuitive mental model for understanding the borrow checker's behavior. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

5. [CHRNj5oubwc] Rust Powered Polymorphism ⚡️ With Traits - 10 min
   Curriculum's reason: Compact comparison of traits with interfaces. It covers static dispatch with generics versus dyn dispatch, default methods and supertraits, which map onto Go interfaces.
   Quote [03:03]: "instead of interfaces Rust has something called traits which are very similar to interfaces but with some subtle differences"
   Quote [04:28]: "dyn refers to something called Dynamic dispatch which is in contrast to something called Static dispatch"
   REFERENCE SUMMARY: This video explains how to implement polymorphism in Rust using traits, covering the differences between static dispatch (generics) and dynamic dispatch (dyn trait objects). It demonstrates creating traits, implementing them for structs, using default implementations, and combining traits with supertrait bounds. Level: intermediate. Format: concept_explainer. Language: en. Flags: surface_intro.

6. [AnsRR-i5UWQ] Introduction to Generics and Traits | Advanced Rust Part 1 - 16 min
   Curriculum's reason: Adds trait bounds, Copy/Clone and implementing traits manually, tying them back to what the compiler enforces.
   Quote [06:10]: "traits or interfaces as they are called in most other languages are Concepts that guarantee that an object or struct provides a certain functionality"
   Quote [08:40]: "we need to make sure that the copy trait is implemented and we do this by adding the copy trait as a requirement for our type T"
   REFERENCE SUMMARY: This video introduces Rust generics and traits, explaining how generics allow writing functions that work with multiple types to avoid code duplication. It covers trait bounds to restrict generic parameters, the Copy trait, and how to implement traits manually, showing practical examples of how the borrow checker enforces trait requirements. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

7. [s5S2Ed5T-dc] A Simpler Way to See Results - 19 min
   Curriculum's reason: Presents Result as a sum type and covers the ? operator, collecting Results, error type design, From, and thiserror/anyhow. This is the mental model for replacing Go's err returns.
   Quote [01:02]: "result is a sum type just like all other enums in Rust"
   Quote [09:50]: "the question mark is a unary post-fix operator so you use it like this"
   REFERENCE SUMMARY: This video explains Rust's Result type by showing how it relates to Option as a sum type, then demonstrates practical usage patterns including the question mark operator, error type design, and popular error handling crates like thiserror and anyhow. The presenter builds mental models for when to use Result vs Option and shows hands-on examples of error propagation and composition. Level: intermediate. Format: concept_explainer. Language: en.

8. [sZV6sz4P6QY] Mastering Error Handling in Rust: From Panics to thiserror & anyhow | with Nathan Stocks - 47 min (watch 20:00-1:06:40)
   Curriculum's reason: Webinar that builds a CLI with Result, ? and a custom error enum, then adds thiserror and anyhow context. This is the practical idiomatic error handling a Go dev needs. I selected the core demo section.
   Quote [22:28]: "This does the exact same thing as that match expression. If the result is an okay, then it unwraps the inner value. If the result is an error variant, then it returns the error from the function."
   Quote [28:39]: "result because result implements the termination trait. So, I've chosen to return one of any house results wrapping the unit type, which is just empty because we don't have anything useful to return in the success case."
   REFERENCE SUMMARY: A 1-hour webinar on error handling in Rust, covering when to panic, designing custom error types with enums, and practical use of thiserror and anyhow crates. Nathan Stocks demonstrates idiomatic error handling patterns, the ? operator for error propagation, and builds a working example with a custom error enum and anyhow for context management. Builds: A Rust CLI application that loads puzzles and handles errors with custom error types, demonstrating error propagation with the ? operator and anyhow context management. Level: intermediate. Format: lecture. Language: en.

9. [uvP1bKTfa_Q] Build a Rust CLI Tool from Scratch (clap, serde, anyhow) – logscan - 13 min
   Curriculum's reason: Short CLI build that hits a real E0515 borrow error with zero-copy parsing and fixes it by moving ownership up. It also shows anyhow and clap, which is close to your porting task.
   Quote [03:59]: "Time and message are string slices ampersand STR that borrow directly from the file's text instead of copying it. That's zero copy parsing and it's very fast."
   Quote [05:23]: "The idiomatic fix, move ownership up. Let the caller own the text and only borrow from it. The string lives in main, which outlives everything else."
   REFERENCE SUMMARY: Build a complete Rust CLI tool (logscan) for analyzing log files with subcommands, colored output, and JSON export. The video demonstrates practical Rust concepts including zero-copy parsing with lifetimes, confronts a real borrow-checker error (E0515), fixes it idiomatically by moving ownership upward, and covers error handling with anyhow, argument parsing with clap, and testing. Builds: logscan: a command-line log analyzer with subcommands (summary, top, grep), colored tables, JSON export, and unit tests. Level: intermediate. Format: project_build. Language: en.

Considered and dropped:
- Error Handling in Rust: Covers Result, ? and panic only at a basic level. Logan Smith's video and the Ardan webinar go deeper, including thiserror and anyhow.
- Rust for Go Developers: The 6 Things You Actually Need to Learn: Surface-level 7-minute overview aimed at Go devs. It has no depth on the borrow checker.

### go_dev_rust_ownership / S2

Planned viewing time: 191 of 240 min.
Assumptions stated: The learner needs enough Rust syntax and tooling (cargo, structs, enums, match) to follow videos, but this is covered by mapping from Go rather than taught from scratch.; Traits are needed mainly as they relate to error handling, generics bounds and lifetimes, not as a full deep dive.; The ported CLI uses typical pieces: argument parsing (e.g. clap), file or stdin IO, and error propagation.; Videos in English; the learner prefers material aimed at experienced developers coming from Go, C, or C++.
Warnings to the learner: Every candidate was assessed from metadata only: no transcripts were available and there are no verified quotes. All evidence_quote_ids are empty and confidences are moderate to low. Skim each video's opening minutes before committing. | Total viewing time is about 191 minutes of the 240-minute budget (about 80%). The remaining 49 minutes were left unused because the remaining candidates were redundant, beginner-level, flagged, or had no usable transcript. | Coverage of Drop, Copy vs Clone and 'static is unverified. The ownership video and the lifetimes videos were chosen from titles and summaries. | No candidate is explicitly for Go developers beyond the 7.5-minute orientation. You will need to map Go's error returns and pointers to Result and references yourself when porting.

1. [pDM_5HT2UlU] Rust for Go Developers: The 6 Things You Actually Need to Learn - 8 min
   Curriculum's reason: Maps Rust onto Go: ownership and borrowing, Result and Option, and compiler feedback. This suits a senior Go developer who needs orientation, not syntax basics. It is also the only candidate aimed at Go developers.
   REFERENCE SUMMARY: This video introduces six core Rust concepts for developers experienced with Go or Spring Boot: ownership and borrowing, Result and Option types, shared state management, async with Tokio, the production crate ecosystem (Cargo, Axum, Serde, SQLx), and learning from compiler errors. The video culminates with a homework project: building a small AI job queue API with explicit error handling, bounded concurrency, and safe shared state. Level: intermediate. Format: concept_explainer. Language: en. Flags: surface_intro.

2. [VFIOSWy93H0] Understanding Ownership in Rust - 26 min
   Curriculum's reason: A dedicated ownership video (moves, and likely Copy vs Clone and Drop) to build the move-semantics foundation before borrowing. It is the only candidate dedicated to ownership that is not flagged as a surface intro.
   REFERENCE SUMMARY: A comprehensive walkthrough of Rust's ownership model, covering how Rust manages memory without garbage collection through compile-time rules. The video explains stack vs heap allocation, ownership rules and moves, borrowing with references (immutable and mutable), borrow checker rules, and string slices with practical examples and compiler error demonstrations. Level: intermediate. Format: concept_explainer. Language: en.

3. [zfb1y8yn8QI] Understanding Rust – Or How to Stop Worrying & Love the Borrow-Checker • Steve Smith • YOW! 2024 - 42 min
   Curriculum's reason: A conference talk aimed at understanding the borrow checker, with the strongest borrowing relevance in the pool. It matches the learner's request for depth on the borrow checker. The pure_theory flag does not count against it here because the learner wants the concepts behind the checker.
   REFERENCE SUMMARY: Steve Smith delivers a conference talk on understanding Rust's borrow checker and ownership system, aimed at developers who have basic Rust knowledge but struggle with the learning curve. The talk covers ownership, borrowing rules, lifetimes, Drop trait, Box, reference counting (Rc), and threading constraints (Send/Sync), positioning the compiler as a garbage collector that ensures memory safety deterministically. Level: intermediate. Format: lecture. Language: en. Flags: pure_theory.

4. [gRAVZv7V91Q] but what is 'a lifetime? - 12 min
   Curriculum's reason: Explains what a lifetime is as a way of reasoning about references, a mental model that suits an experienced systems programmer. It comes before the annotation-focused videos.
   REFERENCE SUMMARY: This video explains two ways to think about lifetimes in Rust: the traditional "particle" interpretation (lifetimes as scopes where variables live) and an alternative "wave" interpretation (lifetimes as regions of memory that references can point into). The presenter demonstrates through examples how thinking of lifetimes as memory regions, combined with liveness analysis and subtyping, provides a more intuitive mental model for understanding the borrow checker's behavior. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

5. [S-SkEA4QWWE] Rust Lifetimes explained Tutorial - 15 min
   Curriculum's reason: Covers lifetime annotations, how the borrow checker validates references, and when explicit lifetime parameters are needed in function signatures and structs. This is the practical annotation side that follows the mental model.
   REFERENCE SUMMARY: A comprehensive tutorial on Rust lifetimes, covering how the borrow checker prevents dangling references, lifetime annotations in functions and structs, lifetime elision rules, and practical examples combining lifetimes with generics and trait bounds. Level: intermediate. Format: concept_explainer. Language: en.

6. [p2uAN6SJorA] Rust Generics, Traits & Lifetimes Explained — Book Chapter 10 Project - 22 min
   Curriculum's reason: Works through generics, traits and lifetimes on a Rust Book Chapter 10 project, showing lifetimes in structs and function signatures alongside trait bounds. This sets up the trait knowledge that error handling needs.
   REFERENCE SUMMARY: This video walks through upgrading a Rust Task Manager project to use generics, traits, and lifetimes. The instructor refactors task types by introducing a Summarize trait, making Task generic over extra data (deadline, priority, or none), and implements a print_card helper function that works polymorphically across different task variants. Builds: Task Manager app upgraded with generic tasks using traits (Summarize trait for Deadline, PriorityInfo, NoExtra types). Level: intermediate. Format: project_build. Language: en.

7. [AnsRR-i5UWQ] Introduction to Generics and Traits | Advanced Rust Part 1 - 16 min
   Curriculum's reason: Introduces trait definitions and generic type parameters as Rust's alternative to inheritance. This gives the trait and bounds grounding that From, Display and the Error trait build on.
   REFERENCE SUMMARY: This video introduces Rust generics and traits, explaining how generics allow writing functions that work with multiple types to avoid code duplication. It covers trait bounds to restrict generic parameters, the Copy trait, and how to implement traits manually, showing practical examples of how the borrow checker enforces trait requirements. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

8. [6WykcOk78sc] Rust Error Handling: The ? Operator, thiserror & anyhow - 39 min
   Curriculum's reason: Directly covers the ? operator, custom error types, From conversions, and thiserror vs anyhow (libraries vs applications). This maps onto the learner's Go habit of returning errors everywhere.
   REFERENCE SUMMARY: This video presents a comprehensive systems architecture built in Rust, covering memory management (stack vs heap), zero-cost abstractions, ownership and moves, borrowing rules, lifetimes, RAII resource cleanup, panic isolation, concurrency with Tokio and channels, thread-safe primitives (Arc, Mutex, atomics), and production verification techniques (testing, Clippy audits). The presenter demonstrates a high-throughput event processing system with bounded backpressure channels, worker thread pools, lock-free atomics, and zero-copy wire protocol deserialization, emphasizing compile-time safety and deterministic microsecond latency without garbage collection. Builds: A production-grade, zero-cost high-throughput event processing system with bounded MPSC channels, worker thread pools, panic isolation, Arc/Mutex thread safety, lock-free atomic counters, and zero-copy wire protocol deserialization. Level: advanced. Format: lecture. Language: en. Flags: too_advanced_for_learner, pure_theory.

9. [uvP1bKTfa_Q] Build a Rust CLI Tool from Scratch (clap, serde, anyhow) – logscan - 13 min
   Curriculum's reason: Builds a log-analysis CLI with clap, serde and anyhow, and works through a real borrow-checker error (E0515) during development. This shows ownership, borrowing and error propagation in a project close to the learner's port.
   REFERENCE SUMMARY: Build a complete Rust CLI tool (logscan) for analyzing log files with subcommands, colored output, and JSON export. The video demonstrates practical Rust concepts including zero-copy parsing with lifetimes, confronts a real borrow-checker error (E0515), fixes it idiomatically by moving ownership upward, and covers error handling with anyhow, argument parsing with clap, and testing. Builds: logscan: a command-line log analyzer with subcommands (summary, top, grep), colored tables, JSON export, and unit tests. Level: intermediate. Format: project_build. Language: en.

Considered and dropped:
- Mastering Error Handling in Rust: From Panics to thiserror & anyhow | with Nathan Stocks: A 73.8-minute error-handling webinar that is flagged pure_theory. Within the 240-minute budget, 6Wykc covers the ? operator, From, thiserror and anyhow with a more practical focus.
- Rust: Ownership and Borrowing, By Rodrigo Boniatti: A second ownership/borrowing explainer without a transcript. It would repeat VFIOSWy93H0 and zfb1y8yn8QI and add another teaching style.
- The Secret Behind Rust’s Memory Safety: The Borrow Checker EXPLAINED: In the borrow-checker/lifetimes duplicate cluster and only a short concept explainer on mutable vs immutable references. The longer talk already covers this.
- Rust Lifetimes Explained Clearly | Borrow Checker, References & Lifetimes | Learn Rust Step by Step: A short concept explainer flagged pure_theory and poor transcript, in the lifetimes duplicate cluster. The kept lifetimes video is longer and more detailed.
- Rust Lifetimes Explained — Finally Make Sense of 'a (2026): A lifetimes 'loans' mental model, in the same cluster as S-SkEA4QWWE. It is flagged pure_theory and poor transcript, and gRAVZv7V91Q already supplies a conceptual lifetimes view.
- Rust Lifetimes Finally Explained!: Duplicate lifetimes video with no usable transcript or relevance scoring. gRAVZv7V91Q has better-grounded evidence of focus.
- A Simpler Way to See Results: A 19-minute Result/Option explainer that is largely theory and covers ? only briefly. 6WykcOk78sc covers the ? operator and custom errors, which the learner needs.
- 🚀 Build a Robust CLI App in Rust with Clap | Rust Programming Tutorial: A beginner-level, long (69.7 min) clap tutorial with no verified content on ownership or error propagation. It would consume too much of the budget.
- Rust: What is Ownership and Borrowing?: A beginner-level ownership explainer flagged surface_intro and pure_theory. The learner wants depth and already has an advanced systems background.
- Rust: Generics, Traits, Lifetimes: A 35-minute generics/traits/lifetimes video flagged pure_theory with a weak segment map. p2uAN6SJorA and AnsRR-i5UWQ give more targeted coverage.

### go_dev_rust_ownership / S3

Planned viewing time: 239 of 240 min.

1. [5C_HPTJg5ek] Rust in 100 Seconds - 2 min
   Curriculum's reason: Popular result (2,658,826 views) for 'Rust for Go developers'.
   REFERENCE SUMMARY: A 100-second overview of Rust's key features: memory safety through ownership and borrowing, the borrow checker, immutability by default, stack vs heap memory, cargo package manager, and basic syntax. Introduces the core concepts without hands-on depth or error handling. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

2. [0y6RKiIk6cs] Rust for Dummies in 12 Minutes - 12 min
   Curriculum's reason: Popular result (534,575 views) for 'Rust for Go developers'.
   REFERENCE SUMMARY: A broad Rust orientation video explaining ownership, move semantics, borrowing rules, and how Rust's type system prevents memory safety bugs at compile time. Compares Rust's approach to memory management and error handling against C/C++ and Java, emphasizing immutability by default, the Option and Result enums, and how explicit type signatures prevent production failures. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

3. [VFIOSWy93H0] Understanding Ownership in Rust - 26 min
   Curriculum's reason: Popular result (371,583 views) for 'Rust ownership and borrowing deep dive for experienced programmers'.
   REFERENCE SUMMARY: A comprehensive walkthrough of Rust's ownership model, covering how Rust manages memory without garbage collection through compile-time rules. The video explains stack vs heap allocation, ownership rules and moves, borrowing with references (immutable and mutable), borrow checker rules, and string slices with practical examples and compiler error demonstrations. Level: intermediate. Format: concept_explainer. Language: en.

4. [juIINGuZyBc] Rust Lifetimes Finally Explained! - 19 min
   Curriculum's reason: Popular result (219,476 views) for 'Rust lifetimes explained in depth structs and functions'.
   REFERENCE SUMMARY: This video explains Rust lifetimes in depth, starting with the borrow checker and dangling references, then covering generic lifetime annotations, elision rules, struct lifetime annotations, and practical examples combining lifetimes with traits and generics. The instructor demonstrates how the compiler uses lifetime relationships to prevent dangling references and when manual lifetime annotations are required. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

5. [s5S2Ed5T-dc] A Simpler Way to See Results - 19 min
   Curriculum's reason: Popular result (190,765 views) for 'Rust error handling Result thiserror anyhow explained'.
   REFERENCE SUMMARY: This video explains Rust's Result type by showing how it relates to Option as a sum type, then demonstrates practical usage patterns including the question mark operator, error type design, and popular error handling crates like thiserror and anyhow. The presenter builds mental models for when to use Result vs Option and shows hands-on examples of error propagation and composition. Level: intermediate. Format: concept_explainer. Language: en.

6. [CHRNj5oubwc] Rust Powered Polymorphism ⚡️ With Traits - 10 min
   Curriculum's reason: Popular result (148,616 views) for 'Rust traits and generics explained for Go developers'.
   REFERENCE SUMMARY: This video explains how to implement polymorphism in Rust using traits, covering the differences between static dispatch (generics) and dynamic dispatch (dyn trait objects). It demonstrates creating traits, implementing them for structs, using default implementations, and combining traits with supertrait bounds. Level: intermediate. Format: concept_explainer. Language: en. Flags: surface_intro.

7. [gRAVZv7V91Q] but what is 'a lifetime? - 12 min
   Curriculum's reason: Popular result (148,603 views) for 'Rust borrow checker explained advanced'.
   REFERENCE SUMMARY: This video explains two ways to think about lifetimes in Rust: the traditional "particle" interpretation (lifetimes as scopes where variables live) and an alternative "wave" interpretation (lifetimes as regions of memory that references can point into). The presenter demonstrates through examples how thinking of lifetimes as memory regions, combined with liveness analysis and subtyping, provides a more intuitive mental model for understanding the borrow checker's behavior. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

8. [wM6o70NAWUI] Error Handling in Rust - 16 min
   Curriculum's reason: Popular result (125,137 views) for 'Rust error handling Result thiserror anyhow explained'.
   REFERENCE SUMMARY: This video teaches Rust error handling through panic, the Result enum, error propagation, and the ? operator. It covers when to use panic vs Result, practical error handling patterns with match expressions and unwrap/expect, and introduces custom validation types. Level: intermediate. Format: lecture. Language: en. Flags: pure_theory.

9. [DhiHhQimSa4] How I’d learn Rust (If I could start over) - 9 min
   Curriculum's reason: Popular result (101,131 views) for 'Rust for Go developers'.
   REFERENCE SUMMARY: This video is a motivational meta-discussion about learning strategies for Rust, not a technical tutorial. The speaker recommends learning Rust by domain, maintaining momentum through community and mentorship, and testing skills against real-world job standards, rather than teaching specific Rust concepts or building a project. Level: beginner. Format: vlog. Language: en. Flags: vlog, surface_intro, off_topic.

10. [zo6yZisg7N0] The promise of Rust - 29 min
   Curriculum's reason: Popular result (65,918 views) for 'Rust borrow checker explained advanced'.
   REFERENCE SUMMARY: This video explains Rust's core value proposition: ownership, move semantics, and the borrow checker that enforces memory safety at compile time. It contrasts Rust's approach with garbage-collected languages (JavaScript, Go) and unsafe systems languages (C, C++) through detailed comparisons and code examples, covering Copy vs non-Copy types, shared vs mutable references, and the aliasing XOR mutability rule. Level: intermediate. Format: concept_explainer. Language: en.

11. [JLfEiJhpTbE] Rust: Generics, Traits, Lifetimes - 36 min
   Curriculum's reason: Popular result (65,035 views) for 'Rust lifetimes explained in depth structs and functions'.
   REFERENCE SUMMARY: This tutorial covers Rust generics, traits, and lifetimes through worked examples. It explains how generics work with functions, structs, and enums; demonstrates trait implementations and bounds; and teaches lifetime annotations with the compiler's elision rules for managing reference validity. Level: intermediate. Format: lecture. Language: en. Flags: pure_theory.

12. [1NJ-sFA4lMI] BEST EVER Explanation of the Borrow Checker | Prime Reacts - 2 min
   Curriculum's reason: Popular result (44,987 views) for 'Rust borrow checker explained advanced'.
   REFERENCE SUMMARY: A comedic reaction video where the host watches a 60-second explanation of Rust's borrow checker using a loan shark metaphor. The original video covers the four basic rules of borrowing: ensuring the borrower doesn't misuse the variable, using `mut` for mutable borrows, preventing simultaneous mutations by multiple borrowers, and avoiding dangling references. Level: beginner. Format: vlog. Language: en. Flags: surface_intro, vlog.

13. [zfb1y8yn8QI] Understanding Rust – Or How to Stop Worrying & Love the Borrow-Checker • Steve Smith • YOW! 2024 - 42 min
   Curriculum's reason: Popular result (36,897 views) for 'Rust borrow checker explained advanced'.
   REFERENCE SUMMARY: Steve Smith delivers a conference talk on understanding Rust's borrow checker and ownership system, aimed at developers who have basic Rust knowledge but struggle with the learning curve. The talk covers ownership, borrowing rules, lifetimes, Drop trait, Box, reference counting (Rc), and threading constraints (Send/Sync), positioning the compiler as a garbage collector that ensures memory safety deterministically. Level: intermediate. Format: lecture. Language: en. Flags: pure_theory.

14. [ebaYftHhIq4] Rust | Build a CLI | Tutorial - 4 min
   Curriculum's reason: Popular result (960 views) for 'build a Rust command line tool with clap project tutorial'.
   REFERENCE SUMMARY: Tutorial on building a basic CLI using clap library in Rust. Demonstrates creating a struct with derive attributes to parse command-line arguments, printing values, and installing the CLI globally with cargo install. Builds: A simple CLI that accepts name and age arguments and prints them back. Level: beginner. Format: project_build. Language: en. Flags: surface_intro, too_basic_for_learner.

### go_dev_rust_ownership / S4

Planned viewing time: 179 of 240 min.
Assumptions stated: The learner needs enough Rust syntax and tooling (cargo, structs, enums, match) to follow videos, but this is covered by mapping from Go rather than taught from scratch.; Traits are needed mainly as they relate to error handling, generics bounds and lifetimes, not as a full deep dive.; The ported CLI uses typical pieces: argument parsing (e.g. clap), file or stdin IO, and error propagation.; Videos in English; the learner prefers material aimed at experienced developers coming from Go, C, or C++.
Warnings to the learner: Budget use is about 191 of 240 minutes (about 80%); roughly 49 minutes are unused. I chose not to pad with repetitive ownership/lifetimes videos or sprawling talks, and I could not widen the OcaerPp59Gs range further without leaving the relevant content. | The Go-specific orientation is brief (pDM_5HT2UlU, about 7.5 minutes and flagged surface_intro). Expect to look up Rust syntax details such as cargo, struct/enum/match and Option as you go. | Traits get only moderate coverage and are split across several videos (traits_basics, with From and Error mostly in the Result videos). This is enough for error handling but not a full trait deep dive. | Some cards have segment maps whose timestamps do not match the stated duration (for example VFIOSWy93H0 and OcaerPp59Gs). I picked full videos wherever possible, and the one watch range (OcaerPp59Gs, 38:20-1:01:40) should be checked against the actual video.

1. [pDM_5HT2UlU] Rust for Go Developers: The 6 Things You Actually Need to Learn - 8 min
   Curriculum's reason: A short orientation written for Go developers. It maps ownership, borrowing, Result/Option and the ? operator onto what a Go engineer already knows, and it frames the compiler as a teaching tool. It is a light overview (flagged surface_intro), but it is the only candidate aimed at Go developers. Skip the async/Tokio and crate-ecosystem sections.
   Quote [01:04]: "Who owns this data right now? The string's ownership moved into the prepare job function."
   Quote [01:04]: "If the function only needs to read the text, borrow it. We change the parameter to a borrowed string slice."
   REFERENCE SUMMARY: This video introduces six core Rust concepts for developers experienced with Go or Spring Boot: ownership and borrowing, Result and Option types, shared state management, async with Tokio, the production crate ecosystem (Cargo, Axum, Serde, SQLx), and learning from compiler errors. The video culminates with a homework project: building a small AI job queue API with explicit error handling, bounded concurrency, and safe shared state. Level: intermediate. Format: concept_explainer. Language: en. Flags: surface_intro.

2. [VFIOSWy93H0] Understanding Ownership in Rust - 26 min
   Curriculum's reason: Walks through the ownership rules, move vs Copy, Drop, passing and returning ownership, then references and the one-mutable-reference rule, with compiler errors shown. It gives the mechanics of moves and Drop that the Go learner lacks. The unflagged transcript shows it staying at a working-programmer level.
   Quote [07:08]: "each value in rust has a variable that's called its owner so one variable one owner"
   Quote [13:11]: "instead of calculate length taking a string we'll make it take a reference to a string"
   REFERENCE SUMMARY: A comprehensive walkthrough of Rust's ownership model, covering how Rust manages memory without garbage collection through compile-time rules. The video explains stack vs heap allocation, ownership rules and moves, borrowing with references (immutable and mutable), borrow checker rules, and string slices with practical examples and compiler error demonstrations. Level: intermediate. Format: concept_explainer. Language: en.

3. [zo6yZisg7N0] The promise of Rust - 29 min
   Curriculum's reason: Contrasts Rust's moves and borrows with Go and JavaScript semantics. It explains the aliasing-XOR-mutability rule behind the borrow checker and where the checker is too conservative, plus the Rc/RefCell and Arc/Mutex escape hatches. This gives the depth on the borrow checker the learner asked for. Skip the sponsored segment.
   Quote [00:42]: "Copy trait. i64 does implement Copy because copying an integer from one register to another is very fast."
   Quote [01:03]: "String type specifically with a capital S refers to a valid UTF-8 sequence stored somewhere on the heap."
   REFERENCE SUMMARY: This video explains Rust's core value proposition: ownership, move semantics, and the borrow checker that enforces memory safety at compile time. It contrasts Rust's approach with garbage-collected languages (JavaScript, Go) and unsafe systems languages (C, C++) through detailed comparisons and code examples, covering Copy vs non-Copy types, shared vs mutable references, and the aliasing XOR mutability rule. Level: intermediate. Format: concept_explainer. Language: en.

4. [hmefR4tE_H4] The Secret Behind Rust’s Memory Safety: The Borrow Checker EXPLAINED - 5 min
   Curriculum's reason: A compact drill on the borrow checker's one-mutable-or-many-immutable rule, scoped borrows, dangling references and common errors with fixes. It consolidates the rules before lifetimes and bridges into reference lifetime tracking.
   Quote [01:03]: "you can have either one mutable reference or any number of immutable references, but not both at the same time"
   Quote [01:45]: "the borrow checker uses lifetime analysis to figure out how long references live and ensures that no reference outlives the data it points to"
   REFERENCE SUMMARY: This video explains Rust's borrow checker in depth, covering the core rule that you can have either one mutable reference or any number of immutable references, but not both at the same time. It demonstrates how the borrow checker prevents data races, dangling references, and memory safety violations at compile time through live code examples and practical rules about reference lifetimes and scope. Level: intermediate. Format: concept_explainer. Language: en.

5. [178uniabkag] Rust Lifetimes Explained — Finally Make Sense of 'a (2026) - 14 min
   Curriculum's reason: Frames lifetime annotations as describing relationships between references, not controlling memory. It covers the longest() problem, the three elision rules, struct lifetimes, 'static and higher-ranked bounds. It is the unflagged member of its near-duplicate cluster.
   Quote [03:28]: "Lifetime annotations do not change how long a value lives. They do not control memory. They do not affect runtime behavior in any way."
   Quote [05:34]: "By marking both inputs and the output with tick a, you are telling the compiler that the returned reference will live at least as long as the shorter of the two inputs."
   REFERENCE SUMMARY: This video explains Rust lifetimes as a communication mechanism to the compiler about relationships between references, not as a memory control feature. It covers lifetime annotations in functions and structs, the three elision rules, the loans mental model from QCon London 2026, and advanced concepts like 'static and higher-ranked bounds (for<'a>). Level: intermediate. Format: concept_explainer. Language: en.

6. [CHRNj5oubwc] Rust Powered Polymorphism ⚡️ With Traits - 10 min
   Curriculum's reason: Explains traits as Rust's analogue of interfaces, covering default implementations, static dispatch with generics vs dynamic dispatch with dyn, and supertraits. This maps directly onto Go interfaces and gives the trait background needed for error types. Flagged surface_intro, but it is short and no unflagged candidate covers dyn vs generics.
   Quote [03:03]: "instead of interfaces Rust has something called traits which are very similar to interfaces but with some subtle differences"
   Quote [04:28]: "dyn refers to something called Dynamic dispatch which is in contrast to something called Static dispatch"
   REFERENCE SUMMARY: This video explains how to implement polymorphism in Rust using traits, covering the differences between static dispatch (generics) and dynamic dispatch (dyn trait objects). It demonstrates creating traits, implementing them for structs, using default implementations, and combining traits with supertrait bounds. Level: intermediate. Format: concept_explainer. Language: en. Flags: surface_intro.

7. [AnsRR-i5UWQ] Introduction to Generics and Traits | Advanced Rust Part 1 - 16 min
   Curriculum's reason: Covers generic functions, trait bounds, why the compiler demands bounds like Copy/Add, and how to implement traits manually. This supplies the bounds mechanics that Display/From/Error-based error handling relies on. Flagged pure_theory, but that does not conflict with this learner's constraints.
   Quote [06:10]: "traits or interfaces as they are called in most other languages are Concepts that guarantee that an object or struct provides a certain functionality"
   Quote [08:40]: "we need to make sure that the copy trait is implemented and we do this by adding the copy trait as a requirement for our type T"
   REFERENCE SUMMARY: This video introduces Rust generics and traits, explaining how generics allow writing functions that work with multiple types to avoid code duplication. It covers trait bounds to restrict generic parameters, the Copy trait, and how to implement traits manually, showing practical examples of how the borrow checker enforces trait requirements. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

8. [s5S2Ed5T-dc] A Simpler Way to See Results - 19 min
   Curriculum's reason: Builds Result from sum types, then covers the ? operator, collecting Results, designing custom error types and combining errors with From. It also shows thiserror and anyhow. This is the closest match to Go's if err != nil pattern and gives the conceptual model of idiomatic Result use.
   Quote [09:50]: "the question mark is a unary post-fix operator so you use it like this"
   Quote [12:01]: "if all the results are okay you get back an OK VEC but if any of them fails the whole thing fails"
   REFERENCE SUMMARY: This video explains Rust's Result type by showing how it relates to Option as a sum type, then demonstrates practical usage patterns including the question mark operator, error type design, and popular error handling crates like thiserror and anyhow. The presenter builds mental models for when to use Result vs Option and shows hands-on examples of error propagation and composition. Level: intermediate. Format: concept_explainer. Language: en.

9. [-c9JEexiHPE] Rust Error Handling Explained: thiserror vs anyhow (Best Practices) - 16 min
   Curriculum's reason: Compares thiserror (typed enum errors for libraries) with anyhow (context-based errors for applications), with examples and a rule of thumb for choosing. This tells the learner which to use in the ported CLI.
   Quote [14:33]: "use this error when you are building libraries and crates and use anyhow when you are building applications"
   Quote [14:55]: "if it's very straightforward into the face just use anyhow if you require more complex handling then I would prefer this error"
   REFERENCE SUMMARY: This video explains the differences between thiserror and anyhow libraries for error handling in Rust, with concrete examples of when to use each. It demonstrates structured error handling with thiserror for libraries using custom enum error types with pattern matching, and anyhow for rapid application development with simpler context-based error chaining. Level: intermediate. Format: concept_explainer. Language: en.

10. [uvP1bKTfa_Q] Build a Rust CLI Tool from Scratch (clap, serde, anyhow) – logscan - 13 min
   Curriculum's reason: Builds a log-analysis CLI with clap and anyhow, and uses zero-copy parsing with &str lifetimes. It confronts a real borrow-checker error (E0515) and fixes it by moving ownership up to the caller. This is ownership and lifetimes applied in the CLI shape the learner is porting.
   Quote [03:59]: "Time and message are string slices ampersand STR that borrow directly from the file's text instead of copying it. That's zero copy parsing and it's very fast."
   Quote [05:23]: "The idiomatic fix, move ownership up. Let the caller own the text and only borrow from it. The string lives in main, which outlives everything else."
   REFERENCE SUMMARY: Build a complete Rust CLI tool (logscan) for analyzing log files with subcommands, colored output, and JSON export. The video demonstrates practical Rust concepts including zero-copy parsing with lifetimes, confronts a real borrow-checker error (E0515), fixes it idiomatically by moving ownership upward, and covers error handling with anyhow, argument parsing with clap, and testing. Builds: logscan: a command-line log analyzer with subcommands (summary, top, grep), colored tables, JSON export, and unit tests. Level: intermediate. Format: project_build. Language: en.

11. [OcaerPp59Gs] 🚀 Build a Robust CLI App in Rust with Clap | Rust Programming Tutorial - 23 min (watch 38:20-1:01:40)
   Curriculum's reason: The chosen range shows the config-handling commands taking references to an AppConfig (ownership in practice), then Result and anyhow error propagation with ? in a clap CLI. This is the longer, more realistic project code after the compact logscan example. The setup and async/Tokio parts are skipped.
   Quote [01:45]: "anyhow so this would um allow me to handle errors much more easily and elegantly"
   Quote [45:15]: "it's going to just take one thing more or less so it will take this config which should be of type so be a reference to app config"
   REFERENCE SUMMARY: This tutorial builds a CLI application in Rust using the Clap library for argument parsing. It covers setting up a Cargo project with dependencies (clap, anyhow, serde, confy, tokio), creating command structures, implementing configuration management with structs and the builder pattern, and demonstrates error handling with Result types and the ? operator. Builds: A Rust CLI application with init, update, and configure commands using Clap for argument parsing and Confy for configuration file management. Level: intermediate. Format: project_build. Language: en.

Considered and dropped:
- Understanding Rust – Or How to Stop Worrying & Love the Borrow-Checker • Steve Smith • YOW! 2024: A strong talk on the borrow checker and lifetimes, but it spends much time on Rc, Send/Sync, async and threads, which are beyond the plan. Its segment map extends well past the stated duration, so a safe watch range is hard to define. The lifetimes picks already cover the plan's needs.
- Rust Lifetimes Finally Explained!: Same lifetimes cluster as the kept video. It covers annotations, elision, structs and 'static but is flagged pure_theory, while 178uniabkag is unflagged and adds the loans model and higher-ranked bounds.
- Rust Lifetimes Explained Clearly | Borrow Checker, References & Lifetimes | Learn Rust Step by Step: Same lifetimes cluster. It is a brief summary, so it adds nothing beyond the kept video.
- Rust Lifetimes explained Tutorial: A solid, unflagged lifetimes tutorial, but it repeats the elision and annotation material already covered by 178uniabkag. A third lifetimes video would be redundant.
- Rust: Ownership and Borrowing, By Rodrigo Boniatti: Good ownership and borrowing walkthrough, but it duplicates VFIOSWy93H0 and zo6yZisg7N0, and adding a third creator on the same ground is redundant.
- Mastering Error Handling in Rust: From Panics to thiserror & anyhow | with Nathan Stocks: A 74-minute error handling webinar. It is strong on thiserror/anyhow but is too long for the thin remaining slot, and its segment map is gappy and unreliable, so a clean watch range cannot be chosen.
- Rust: Generics, Traits, Lifetimes: A broad generics/traits/lifetimes lecture of 36 minutes. It is mostly basic generics and repeats lifetimes material, which is less efficient than the targeted picks.
- Rust Generics, Traits & Lifetimes Explained — Book Chapter 10 Project: A task-manager project that mostly covers basic generics and trait impls at beginner level. Its lifetimes coverage is only an overview, so it adds little beyond the chosen trait videos.
- Rust Error Handling: The ? Operator, thiserror & anyhow: Marked too_advanced_for_learner. It is a sprawling architecture talk with only a brief error handling segment.
- 🦀 Master Rust Programming #12 | Build CLI with CLAP Crate & Publish to Crates.io | Cargo Deep Dive 🚀: Marked off_topic. It focuses on publishing crates, workspaces and docs rather than ownership or error handling.

## hindi_excel_pivots

```
Goal: Learn pivot tables and lookups well enough to build a monthly sales dashboard in Excel
Time budget: 90 minutes
Background: Small-business owner in Lucknow; uses Excel for basic lists and sums
Already knows: entering data, SUM and basic formulas, sorting and filtering
Does not know yet: pivot tables, XLOOKUP / VLOOKUP, slicers, pivot charts, dashboard layout
Constraints: I understand Hindi much better than English, so please choose Hindi-language videos. I watch on my phone, so nothing longer than 25 minutes at a time.
```

### hindi_excel_pivots / S1

Planned viewing time: 65 of 90 min.
Assumptions stated: Hindi or Hinglish videos are acceptable, since the learner understands Hindi better than English.; The learner has a modern Excel version (2016 or later, ideally 365) so that XLOOKUP and slicers are available.; The dashboard builder video is the practice project, and the learner follows along with their own sales data.
Warnings to the learner: The plan uses about 65 of the 90 minutes. I left the rest unused rather than add redundant videos. | A second dashboard build (oKdBEjcgzyw, 20.7 min) exists. It is a near-duplicate of the one I chose, so I did not pick it. The chosen one is monthly, has KPI cards and has a date slicer. You could watch the other one as optional extra practice. | No Hindi video gave a full, quoted XLOOKUP-only lesson. Both lookup videos are mostly VLOOKUP with some XLOOKUP, so practise XLOOKUP yourself. | The learner may need to pause and rewatch, since the dashboard video moves quickly.

1. [4A6hjD-61gM] pivot table for beginners in excel in Hindi || Microsoft excel 2007,2010,2016 - 14 min
   Curriculum's reason: A beginner Hindi walkthrough of sales-data pivot tables. It covers inserting one, dragging fields to rows, columns and values, refreshing when records change, and adding a first slicer.
   Quote [02:13]: "आप अपना टेबल के अंदर कहीं भी क्लिक कर लीजिए जो रिकॉर्ड आपका है और पिवट टेबल पे क्लिक कीजिए"
   Quote [18:21]: "स्लाइसर की हेल्प से हम डाटा को आसानी से ड्रॉप डाउन लिस्ट क्रिएट होगी एक उस पे क्लिक करने से हम डाटा को आसानी से देख सकते हैं"
   REFERENCE SUMMARY: This video teaches how to create and use pivot tables in Excel to summarize and analyze sales data by department, person, and year. It demonstrates inserting a pivot table from the Insert menu, dragging fields to rows/columns/values areas, refreshing data when source records change, and adding interactive slicers to filter the pivot table by department. Level: beginner. Format: concept_explainer. Language: hi.

2. [hmygrQMcHyU] Vlookup का सबसे आसान Example || What is Vlookup in Excel (in Hindi) - 6 min
   Curriculum's reason: A gentle Hindi VLOOKUP introduction that explains each argument: lookup value, table array, column index and range lookup. It uses a name, city and sales example.
   Quote [03:25]: "इक्वल टू Vlookup, lookup वैल्यू, अब ये कह रहा है कि क्या ढूंढना है"
   Quote [03:48]: "कॉलम इंडेक्स नंबर अगर यह नाम जो हमने ढूंढना है वो इस लिस्ट में मिल जाए"
   REFERENCE SUMMARY: A detailed beginner-friendly tutorial on VLOOKUP in Hindi, teaching how to search for names in a large dataset and automatically pull corresponding city names and sales amounts using the VLOOKUP formula with four parameters: lookup value, table array, column index number, and range lookup. Level: beginner. Format: concept_explainer. Language: hi.

3. [gAY9is-ahQY] How To Apply VLOOKUP and XLOOKUP Formula on Large Data in Excel [Hindi] #excel - 13 min
   Curriculum's reason: Builds on the basic VLOOKUP video. It applies VLOOKUP and XLOOKUP to large data, using MATCH to find the column number and named ranges to simplify formulas.
   Quote [00:00]: "अगर आपके पास एक लार्ज डाटा है तो उस पर आप VLOOKUP या XLOOKUP कैसे अप्लाई करेंगे"
   Quote [00:41]: "हमें क्या लिखना है यहां पर लुकअप अरे यानी कि एक अरे हम डालेंगे यहां पर जिसका डाटा हम ढूंढ रहे हैं"
   REFERENCE SUMMARY: This video teaches how to apply VLOOKUP and XLOOKUP formulas on large datasets in Excel. It demonstrates both manual and automated approaches, including using the MATCH function to dynamically determine column numbers and Named Ranges to simplify formula references. Level: beginner. Format: concept_explainer. Language: hi.

4. [htOIqJGeewE] How to Create Pivot Charts? | Excel Pivot Table in Hindi | Excel Pivot Table Series - Part - 2 - 10 min
   Curriculum's reason: A Hindi walkthrough of creating a pivot chart together with its pivot table. It covers changing chart type, data labels and formatting, ready for the dashboard.
   Quote [00:26]: "Pivot Chart हम यहां पे बनाने वाले है, तो सबसे पहले मैं Control A बटन प्रेस करूंगा।"
   Quote [02:08]: "Pivot Chart में क्या होता है बेसिकली खाली Chart ही नहीं बनेगा, यहां पे Table भी बनेगा, Chart भी बनेगा।"
   REFERENCE SUMMARY: This video teaches how to create pivot charts from pivot tables in Excel. The instructor demonstrates creating a new pivot chart with both a table and chart simultaneously, configuring rows/columns/values, changing chart types (column to pie), formatting data labels with percentages and category names, and designing the chart appearance. Level: beginner. Format: concept_explainer. Language: hi.

5. [_JtEWpUJPVY] “📊 Excel Dashboard Tutorial (Hindi) | Pivot Table से Dashboard बनाएं | Next-Level Reporting 🚀” - 23 min
   Curriculum's reason: A Hindi project build of an interactive monthly sales dashboard. It has KPI cards, product, region and month-trend charts, and slicers connected across all of them. This matches the learner's end goal.
   Quote [00:21]: "एक्सेल के अंदर एक मिनी सेल्स डाटा डैशबोर्ड बनाने सिखाने जा रहा हूं वो भी एकदम सिंपल और बिगिनर फ्रेंडली मेथड के साथ"
   Quote [07:18]: "अब हम इन रिपोर्ट्स की हेल्प से हम बनाएंगे डैशबोर्ड इन सभी रिपोर्ट्स की हेल्प से अब हम डैशबोर्ड बनाने जा रहे हैं"
   REFERENCE SUMMARY: This video teaches how to build an interactive sales dashboard in Excel using pivot tables, KPI cards, and charts. It demonstrates creating multiple pivot table reports, formatting them, and connecting them with slicers for filtering by product, region, and date. Builds: Interactive monthly sales dashboard with KPI cards (total revenue, units sold, orders), product-wise performance chart, region-wise performance chart, month-wise revenue trend chart, and connected slicers for product, region, and date filtering. Level: beginner. Format: project_build. Language: hi.

Considered and dropped:
- How to make Dashboard in excel ( Interactive + Simple ): This is a good Hinglish dashboard build, but it is a near-duplicate of the chosen one. It focuses on region and seller percentages and has no monthly view or KPI cards.
- XLOOKUP Function in MS Excel | MS Excel Advanced Tutorial | [Hindi] #ms excel: It has a good XLOOKUP explanation, but the read returned no quotes to cite and it is flagged pure_theory. It is also intermediate level.
- How to Use VLOOKUP, HLOOKUP, XLOOKUP || Detailed Explaination with examples || Advance Excel Formula: It is mostly English and flagged pure_theory. It overlaps with the Hindi VLOOKUP videos I picked.
- Pivot Table Mastery in Excel | Pivot Table Tutorial in Hindi | Part - 01: It is flagged surface_intro and is about 22 minutes. It duplicates the shorter pivot basics video and returned no quotes.

### hindi_excel_pivots / S2

Planned viewing time: 90 of 90 min.

1. [4A6hjD-61gM] pivot table for beginners in excel in Hindi || Microsoft excel 2007,2010,2016 - 14 min
   Curriculum's reason: Popular result (3,505,708 views) for 'Excel pivot table Hindi tutorial beginners'.
   REFERENCE SUMMARY: This video teaches how to create and use pivot tables in Excel to summarize and analyze sales data by department, person, and year. It demonstrates inserting a pivot table from the Insert menu, dragging fields to rows/columns/values areas, refreshing data when source records change, and adding interactive slicers to filter the pivot table by department. Level: beginner. Format: concept_explainer. Language: hi.

2. [gAY9is-ahQY] How To Apply VLOOKUP and XLOOKUP Formula on Large Data in Excel [Hindi] #excel - 13 min
   Curriculum's reason: Popular result (3,242,621 views) for 'Excel VLOOKUP aur XLOOKUP Hindi mein'.
   REFERENCE SUMMARY: This video teaches how to apply VLOOKUP and XLOOKUP formulas on large datasets in Excel. It demonstrates both manual and automated approaches, including using the MATCH function to dynamically determine column numbers and Named Ranges to simplify formula references. Level: beginner. Format: concept_explainer. Language: hi.

3. [NbaiGbn4khs] How to Create Pivot Table in Microsoft Excel | Pivot Table in Excel - 5 min
   Curriculum's reason: Popular result (2,791,344 views) for 'Excel table banana Hindi data cleaning for pivot table'.
   REFERENCE SUMMARY: A step-by-step tutorial on creating and using pivot tables in Microsoft Excel. The video demonstrates how to set up a pivot table from sample sales data (employee names, items, quantity, rate, amount), configure fields into Filters, Columns, Rows, and Values sections, and use the filter button to analyze sales by product and employee. Level: beginner. Format: concept_explainer. Language: hi. Flags: surface_intro, too_basic_for_learner.

4. [hxAkt7Pico0] pivot table for beginners in excel in Hindi | pivot table excel in hindi - 24 min
   Curriculum's reason: Popular result (2,383,447 views) for 'Excel pivot table Hindi tutorial beginners'.
   REFERENCE SUMMARY: This video teaches pivot table fundamentals in Hindi for Excel beginners. It covers how to create pivot tables from raw sales data, configure rows/columns/values/filters fields, and generate summary reports showing sales by department, salesman, and state. It also demonstrates pivot charts for graphical visualization and slicers for interactive filtering. Level: beginner. Format: concept_explainer. Language: hi.

5. [DX0V7D0GWwI] How to use VLOOKUP formula in Excel | VLOOKUP in Excel Tutorial - 5 min
   Curriculum's reason: Popular result (2,280,000 views) for 'Excel VLOOKUP aur XLOOKUP Hindi mein'.
   REFERENCE SUMMARY: This video teaches how to use the VLOOKUP formula in Excel to look up values in a table based on a lookup value. The instructor explains the four parameters of VLOOKUP (lookup value, table array, column index number, and match type), demonstrates filling a formula down across rows, and covers important gotchas like duplicate values and the top-to-bottom matching behavior. Level: beginner. Format: concept_explainer. Language: hi.

6. [lCoPTPsTJ4s] Create Pivot Tables In Excel | Use of Pivot Table - Pivot Table Tutorial - 12 min
   Curriculum's reason: Popular result (1,288,526 views) for 'Excel pivot table Hindi tutorial beginners'.
   REFERENCE SUMMARY: This video teaches how to create and use pivot tables in Excel, demonstrating how to summarize and analyze data by placing fields into rows, columns, values, and filters sections. It covers practical examples like comparing scores by gender and house groups, changing calculation methods like sum to average, and formatting pivot table layouts. Level: beginner. Format: concept_explainer. Language: hi.

7. [DUP-Js2vNjs] How To Apply VLOOKUP and XLOOKUP formula on Large / Big Data in Excel (Hindi) - 11 min
   Curriculum's reason: Popular result (846,750 views) for 'Excel VLOOKUP aur XLOOKUP Hindi mein'.
   REFERENCE SUMMARY: This video teaches VLOOKUP and XLOOKUP formulas to retrieve employee data from a large dataset. The instructor demonstrates how to use VLOOKUP with named ranges, the COLUMNS function to automate column indexing, IFERROR to handle missing data, and XLOOKUP as a modern alternative with simpler syntax that doesn't require manual column numbering. Level: intermediate. Format: concept_explainer. Language: hi.

8. [hmygrQMcHyU] Vlookup का सबसे आसान Example || What is Vlookup in Excel (in Hindi) - 6 min
   Curriculum's reason: Popular result (242,654 views) for 'Excel VLOOKUP aur XLOOKUP Hindi mein'.
   REFERENCE SUMMARY: A detailed beginner-friendly tutorial on VLOOKUP in Hindi, teaching how to search for names in a large dataset and automatically pull corresponding city names and sales amounts using the VLOOKUP formula with four parameters: lookup value, table array, column index number, and range lookup. Level: beginner. Format: concept_explainer. Language: hi.

### hindi_excel_pivots / S3

Planned viewing time: 74 of 90 min.
Assumptions stated: Learner has a desktop/laptop Excel (Microsoft 365 or 2021) available to build the dashboard even though videos are watched on a phone, so XLOOKUP is available; VLOOKUP is covered as the fallback for older versions.; Sales data is a simple table with date, product, customer/region, quantity and amount columns.; The 25-minute limit applies to each individual video, not to the total plan, so several shorter videos will be combined.; Hindi-language videos are preferred; Hinglish tutorials are acceptable since they are understandable to a Hindi speaker.
Warnings to the learner: Planned viewing is 73.8 of 90 minutes (about 82%). That leaves 16.2 minutes unused because the remaining Hindi candidates repeated topics already covered, and adding them would only add redundancy and extra creators. | Timelines (date-range filters) are not covered by any Hindi candidate. Slicers are covered, including a month slicer. After the slicer videos, try Analyze > Insert Timeline yourself. | Clean data table preparation is only covered briefly, in the table-conversion part of the first video. Make sure your sales list has one header row, no blank rows or columns, and real dates. | No selected video shows lookups feeding into a dashboard. The dashboard video uses its own sample data, so you will need to apply a lookup to your own list to add product names or categories before building pivots.

1. [JOSh69tzivA] How to use Slicer in Microsoft Excel | Slicer in Excel - 4 min
   Curriculum's reason: Shows in Hindi how to convert a plain list into an Excel Table before using it, which is the first step for your monthly sales list. It also gives a gentle first look at slicers. It is flagged as a surface intro, but that is what a beginner needs for this step and no other short video teaches the table step.
   Quote [00:48]: "स्लाइसर को अप्लाई करने के लिए, सबसे पहले आपको इन डेटा को टेबल में कन्वर्ट कर लेना है"
   Quote [01:42]: "क्लिक करने के साथ ही यहां पे देखिए, वो सारे डेटा टेबल में कन्वर्ट हो चुका है"
   REFERENCE SUMMARY: This video demonstrates how to create and use slicers in Microsoft Excel to filter data by location. The instructor shows the complete process: converting data into a table, inserting a slicer on the Location column, adjusting its layout, and using single and multi-select filtering to display employee data for specific locations. Level: beginner. Format: concept_explainer. Language: hi. Flags: surface_intro.

2. [DX0V7D0GWwI] How to use VLOOKUP formula in Excel | VLOOKUP in Excel Tutorial - 5 min
   Curriculum's reason: A simple Hinglish walkthrough of VLOOKUP: lookup value, table array, column index and exact match, then filling the formula down. It also covers the duplicate-value and top-to-bottom matching pitfalls and pasting as values. This is a good starting point for pulling prices or categories into your sales list.
   Quote [00:48]: "lookup value. matlab aap yahan pe jo bhi value lana chahte hain wo kis kis value ke liye lana chahte hain?"
   Quote [02:07]: "yaad rakhiyega aapko poori table select karna hai sirf ek column ya ek row nahi. poori table select kiya"
   REFERENCE SUMMARY: This video teaches how to use the VLOOKUP formula in Excel to look up values in a table based on a lookup value. The instructor explains the four parameters of VLOOKUP (lookup value, table array, column index number, and match type), demonstrates filling a formula down across rows, and covers important gotchas like duplicate values and the top-to-bottom matching behavior. Level: beginner. Format: concept_explainer. Language: hi.

3. [gAY9is-ahQY] How To Apply VLOOKUP and XLOOKUP Formula on Large Data in Excel [Hindi] #excel - 13 min
   Curriculum's reason: Hindi video that applies VLOOKUP and then XLOOKUP to a large dataset. It uses named ranges and MATCH to avoid hard-coding column numbers, then shows XLOOKUP as the simpler modern option. This extends the basic VLOOKUP into the version you will use on a full monthly sales list.
   Quote [00:00]: "अगर आपके पास एक लार्ज डाटा है तो उस पर आप VLOOKUP या XLOOKUP कैसे अप्लाई करेंगे"
   Quote [00:41]: "हमें क्या लिखना है यहां पर लुकअप अरे यानी कि एक अरे हम डालेंगे यहां पर जिसका डाटा हम ढूंढ रहे हैं"
   REFERENCE SUMMARY: This video teaches how to apply VLOOKUP and XLOOKUP formulas on large datasets in Excel. It demonstrates both manual and automated approaches, including using the MATCH function to dynamically determine column numbers and Named Ranges to simplify formula references. Level: beginner. Format: concept_explainer. Language: hi.

4. [BvYU0GEHJyc] Pivot Table in Excel | Pivot Table with Multiple Slicers | Pivot Table Full Tutorial | CTA - 20 min
   Curriculum's reason: Hindi pivot table course on sales data (seller, region, item, monthly figures). It covers dragging fields into rows, columns and values, switching sum to count, filters, multiple slicers, and a first pivot chart. It gives you the core pivot skills before the chart and dashboard videos.
   Quote [00:41]: "अब हमें इससे बनानी है एक पाइवोट टेबल तो पाइवोट टेबल को बनाने के लिए आपको पता है कि आपको बस अपने डाटा को सेलेक्ट कर लेना है"
   Quote [07:30]: "और जो काउंट करने वाली चीजें हैं उनको आप वैल्यूज में लेके आइए जैसे रीजन चाहिए तो सेलर नेम में ले"
   REFERENCE SUMMARY: This tutorial teaches how to create pivot tables in Excel from scratch, including how to organize data, drag and drop fields into rows/columns/values areas, apply filters, create slicers for interactive filtering, and build pivot charts. The video demonstrates practical examples with sales data showing seller names, regions, items, and monthly sales figures. Builds: Sales data pivot table with multiple slicers for region and item filtering, plus a pivot chart showing sales trends. Level: beginner. Format: full_course. Language: hi.

5. [htOIqJGeewE] How to Create Pivot Charts? | Excel Pivot Table in Hindi | Excel Pivot Table Series - Part - 2 - 10 min
   Curriculum's reason: Hindi video dedicated to pivot charts. It shows that a pivot chart creates a table and a chart together, how to change chart type, and how to format data labels. This gives you the chart skills for sales trends and comparisons.
   Quote [02:08]: "Pivot Chart में क्या होता है बेसिकली खाली Chart ही नहीं बनेगा, यहां पे Table भी बनेगा, Chart भी बनेगा।"
   Quote [12:04]: "बेसिकली Pivot Table जो होता है उसी का ही Pivot Chart होता है। Table यहां पे आएगा-आएगा और Chart आएगा।"
   REFERENCE SUMMARY: This video teaches how to create pivot charts from pivot tables in Excel. The instructor demonstrates creating a new pivot chart with both a table and chart simultaneously, configuring rows/columns/values, changing chart types (column to pie), formatting data labels with percentages and category names, and designing the chart appearance. Level: beginner. Format: concept_explainer. Language: hi.

6. [HBJdxWxG7aU] Microsoft Excel - How to create Dashboard in Excel | Sales Dashboard | Excel Tutorial - 22 min
   Curriculum's reason: Builds a monthly sales dashboard end to end in Hindi, from raw data to pivot tables. It groups dates by month, builds product, brand and city charts, and adds month slicers that control every chart. This brings together the earlier pieces into the dashboard you want.
   Quote [10:30]: "जैसे आप डेट को सेलेक्ट करोगे बाय डिफॉल्ट अपने आप ये इसको डेटा को एनालाइज कर लेगा एंड उस डेट को मंथ वाइज आपके सामने रिप्रेजेंट कर देगा"
   Quote [32:17]: "अब आप देखोगे पूरा कंट्रोल होगा। मार्च पे क्लिक किया तो ये कंट्रोल हो रहा है"
   REFERENCE SUMMARY: This video demonstrates how to create a complete sales dashboard in Excel using pivot tables, charts, and slicers. The instructor builds a multi-chart dashboard showing product-wise, brand-wise, city-wise sales data, with month-based filtering that allows dynamic updates of all visualizations simultaneously. Builds: Monthly sales dashboard with product-wise, brand-wise, and city-wise sales charts filtered by month using slicers. Level: beginner. Format: project_build. Language: hi.

Considered and dropped:
- “📊 Excel Dashboard Tutorial (Hindi) | Pivot Table से Dashboard बनाएं | Next-Level Reporting 🚀”: Good Hindi dashboard with KPI cards and slicers, but it covers the same ground as the chosen dashboard video. Adding it would push the plan over the 90-minute budget and add a second dashboard style.
- pivot table for beginners in excel in Hindi | pivot table excel in hindi: Solid Hindi pivot basics, but it is 23.9 minutes and BvYU0GEHJyc covers the same material more compactly, leaving room for the chart and dashboard videos.
- Excel Tutorial: Sales Dashboard in Excel | Excel Dashboard | Excel Interview: Another Hindi monthly dashboard with a month slicer. It is redundant with HBJdxWxG7aU, which covers the same ground.
- Excel Pivot Table, Pivot Chart & Slicer Tutorial in Hindi | Complete Data Analysis Guide: Good short Hindi demo of a pivot table, chart and slicer. It overlaps the chosen pivot and dashboard videos and would add another creator and codebase.
- Sales Dashboard in Excel In Hindi | अगर अपनी सैलरी बढ़ाना चाहते हैं | तो एक्सेल Dashboard बनाना सीखे: Complete Hindi monthly dashboard, but it is 60 minutes, which breaks the 25-minute limit and would use most of the budget.
- Pivot Table in Excel Full Tutorial 🔥 Data Analysis for Beginners (Hindi) । Computer with Kritika: Hindi pivot table lecture of 31 minutes, over your 25-minute limit and flagged as pure theory.
- Excel Dashboard Course #21 - Creating a Pivot table Dashboard with Slicers in Excel (in 15 minutes): Good dashboard course content, but it is in English, which conflicts with your Hindi preference.
- Bye Bye Manual Work in Excel | Create Fully Automated Dashboard in Excel: Flagged wrong_language and built on a paid third-party add-in (Excel Booster) rather than standard pivot tables.
- XLOOKUP in Excel | How to Use XLOOKUP Function in Excel | Excel Tutorial in Hindi: XLOOKUP with 10 intermediate examples, using CHOOSE, TRANSPOSE and nested formulas. This is too advanced for your first lookup lesson and 21.9 minutes is too long for the lookup slot.
- Learn Excel XLookup Formula A to Z ｜ X Lookup Masterclass by Satish Dhawale: 51-minute XLOOKUP masterclass, over your 25-minute limit and flagged as pure theory.

### hindi_excel_pivots / S4

Planned viewing time: 88 of 90 min.
Assumptions stated: Learner has a desktop/laptop Excel (Microsoft 365 or 2021) available to build the dashboard even though videos are watched on a phone, so XLOOKUP is available; VLOOKUP is covered as the fallback for older versions.; Sales data is a simple table with date, product, customer/region, quantity and amount columns.; The 25-minute limit applies to each individual video, not to the total plan, so several shorter videos will be combined.; Hindi-language videos are preferred; Hinglish tutorials are acceptable since they are understandable to a Hindi speaker.
Warnings to the learner: No candidate has verified quotes or a usable transcript, so every pick rests on titles, summaries and segment maps. Confidence is moderate at best; skim the first minute of each video to confirm it suits you. | Language was inferred from titles and summaries: the picks are Hindi or Hinglish, but this is not confirmed from the audio. | The sub-topic 'Preparing sales data as an Excel Table' (about 7 minutes) has no dedicated video in the pool. Convert your list to a Table with Ctrl+T (Insert > Table) before the pivot videos. The pivot videos may touch on this, but it is unverified. | Timelines (date filters) are not clearly covered by any candidate; the slicer video covers slicers only. Look at the Timeline option under PivotTable Analyze once your dashboard is built.

1. [hmygrQMcHyU] Vlookup का सबसे आसान Example || What is Vlookup in Excel (in Hindi) - 6 min
   Curriculum's reason: A short Hindi VLOOKUP intro with one simple example, a gentle starting point for someone who has never used lookups. It teaches what VLOOKUP is and how to write it before the fuller lookup video. It is flagged surface_intro, but a gentle on-ramp suits this beginner, and the next pick adds depth.
   REFERENCE SUMMARY: A detailed beginner-friendly tutorial on VLOOKUP in Hindi, teaching how to search for names in a large dataset and automatically pull corresponding city names and sales amounts using the VLOOKUP formula with four parameters: lookup value, table array, column index number, and range lookup. Level: beginner. Format: concept_explainer. Language: hi.

2. [gAY9is-ahQY] How To Apply VLOOKUP and XLOOKUP Formula on Large Data in Excel [Hindi] #excel - 13 min
   Curriculum's reason: A Hindi video that applies both VLOOKUP and XLOOKUP to larger datasets and comes with a practice file. This matches the learner's need to pull prices, names and categories into a sales list, and it covers XLOOKUP for modern Excel plus VLOOKUP as the fallback.
   REFERENCE SUMMARY: This video teaches how to apply VLOOKUP and XLOOKUP formulas on large datasets in Excel. It demonstrates both manual and automated approaches, including using the MATCH function to dynamically determine column numbers and Named Ranges to simplify formula references. Level: beginner. Format: concept_explainer. Language: hi.

3. [hro6_y7R310] Pivot Table Mastery in Excel | Pivot Table Tutorial in Hindi | Part - 01 - 22 min
   Curriculum's reason: Part 1 of a Hindi pivot table series covering the basics of creating pivot tables, at a beginner level. It is the main pivot coverage, taking the learner from raw list to summary with rows, columns and values.
   REFERENCE SUMMARY: This video introduces pivot tables in Excel, demonstrating how to create and configure pivot tables from sales data. The instructor shows how to arrange fields in rows, columns, values, and filters sections to generate reports by region, item, state, and city, with practical examples of summarizing quantities and amounts. Level: beginner. Format: concept_explainer. Language: hi. Flags: surface_intro.

4. [mp5RFCvpWI0] Excel mein Pivot Chart aur Slicer kaise Banayein | How to make Pivot Chart and Slicer in Excel - 4 min
   Curriculum's reason: A very short Hinglish walkthrough of making a pivot chart and adding slicers to it. It covers both skills before the dashboard build, and the Hinglish title is understandable to a Hindi speaker.
   REFERENCE SUMMARY: Learn how to create pivot charts in Excel from a sales database with employee data, and then add slicers to filter the pivot chart by region. The video demonstrates customizing the chart appearance, adding data levels for hierarchical filtering, and adjusting slicer column layout. Level: beginner. Format: concept_explainer. Language: hi. Flags: surface_intro.

5. [_JtEWpUJPVY] “📊 Excel Dashboard Tutorial (Hindi) | Pivot Table से Dashboard बनाएं | Next-Level Reporting 🚀” - 23 min
   Curriculum's reason: A Hindi project build of a mini sales dashboard from pivot tables. It ties pivot summaries and pivot charts into one dashboard, which is the learner's end goal.
   REFERENCE SUMMARY: This video teaches how to build an interactive sales dashboard in Excel using pivot tables, KPI cards, and charts. It demonstrates creating multiple pivot table reports, formatting them, and connecting them with slicers for filtering by product, region, and date. Builds: Interactive monthly sales dashboard with KPI cards (total revenue, units sold, orders), product-wise performance chart, region-wise performance chart, month-wise revenue trend chart, and connected slicers for product, region, and date filtering. Level: beginner. Format: project_build. Language: hi.

6. [PuGzwrnBG_s] Excel में Dashboard बनाना सीखे | Interactive Dashboard In Excel | Dashboard Tutorial | - 21 min
   Curriculum's reason: A Hindi interactive-dashboard video that goes through building a dashboard from start to finish. It gives a second example of layout and interactive elements, so the learner can practise the layout on their own sales data.
   REFERENCE SUMMARY: This video demonstrates how to build an interactive sales dashboard in Excel using pivot tables and pivot charts. The instructor creates multiple pivot charts (pie, bar, column, combo) to analyze sales data by channel, state, gender, age group, and order status, then adds a month slicer to filter all charts interactively by month. Builds: Interactive sales dashboard with pivot charts filtered by month using slicers. Level: beginner. Format: project_build. Language: hi.

Considered and dropped:
- XLOOKUP Function in MS Excel | MS Excel Advanced Tutorial | [Hindi] #ms excel: An XLOOKUP-only Hindi video marked intermediate. The chosen VLOOKUP and XLOOKUP video covers both functions at a beginner level.
- XLOOKUP in Excel | How to Use XLOOKUP Function in Excel | Excel Tutorial in Hindi: A good Hindi XLOOKUP tutorial, but adding 22 minutes would repeat lookup coverage and leave no budget for the dashboard picks. VLOOKUP is also not covered.
- pivot table for beginners in excel in Hindi | pivot table excel in hindi: Near-duplicate of the chosen Hindi pivot basics video, and at 23.9 minutes it takes more of the budget for the same content.
- 🔥 Excel Pivot Table Complete Tutorial in Hindi | Beginner to Advanced: Near-duplicate of the chosen pivot video. It is flagged surface_intro, and its segment map shows only about 9 minutes of actual pivot content.
- How to Create Pivot Charts? | Excel Pivot Table in Hindi | Excel Pivot Table Series - Part - 2: Hindi pivot charts video, but it is in the same near-duplicate cluster as the chosen chart and slicer video. It has no slicer coverage, so the chosen pick covers more of the plan.
- Excel Pivot Table, Pivot Chart & Slicer Tutorial in Hindi | Complete Data Analysis Guide: A 5.5-minute video claiming pivot tables, charts and slicers. It has no segment map and only relevance 1 for each topic, so it is too thin.
- Sales Dashboard in Excel In Hindi | अगर अपनी सैलरी बढ़ाना चाहते हैं | तो एक्सेल Dashboard बनाना सीखे: A 60-minute Hindi sales dashboard video flagged clickbait, with no verifiable content and relevance 0. It is also far over the 25-minute sitting limit.
- Pivot Table in Excel Full Tutorial 🔥 Data Analysis for Beginners (Hindi) । Computer with Kritika: A 31-minute Hindi pivot lecture, over the 25-minute limit. It would need splitting and would take most of the budget for beginner pivot content already covered.
- Excel Dashboard Course #21 - Creating a Pivot table Dashboard with Slicers in Excel (in 15 minutes): A well-matched pivot dashboard with slicers, but flagged wrong_language (not Hindi), which is disqualifying for this learner.
- Pivot Table in Excel | Pivot Table with Multiple Slicers | Pivot Table Full Tutorial | CTA: The title suggests pivot tables with multiple slicers, but no topics or content could be verified.

## impossible_k8s_in_45

```
Goal: Learn Kubernetes deeply and pass the CKA exam, including hands-on cluster setup
Time budget: 45 minutes
Background: Junior sysadmin, 1 year; runs Docker containers on single servers
Already knows: Linux command line, Docker, containers
Does not know yet: Kubernetes architecture, pods, deployments, services, kubectl, cluster setup with kubeadm, CKA exam topics
Constraints: Must be exam-prep oriented. The CKA exam changed recently, so nothing from before 2023.
```

### impossible_k8s_in_45 / S1

Planned viewing time: 44 of 45 min.
Assumptions stated: The 2023+ constraint is judged from titles and content (2025/2026 labels). I couldn't check upload dates for the KodeKloud architecture video, which is conceptual and slow to go out of date.; The learner will practice alongside the videos on their own VMs or a lab.; Deep coverage of the whole CKA curriculum needs a full course (50+ hours). 45 minutes can only set the foundation.
Feasibility note: Learning Kubernetes deeply and passing the CKA can't be done in 45 minutes. What fits is the foundation: architecture, a kubeadm cluster build, imperative kubectl for deployments and services, and an exam strategy. Storage, RBAC, etcd backup and restore, cluster upgrades, scheduling, and troubleshooting need a full CKA course plus practice labs such as Killer.sh.
Warnings to the learner: Learning Kubernetes deeply and passing the CKA can't be done in 45 minutes. What fits is the foundation: architecture, a kubeadm cluster build, imperative kubectl for deployments and services, and an exam strategy. Storage, RBAC, etcd backup and restore, cluster upgrades, scheduling, and troubleshooting need a full CKA course plus practice labs such as Killer.sh. | Total is about 44.5 of 45 minutes. | Big gaps remain: storage, RBAC, etcd backup/restore, cluster upgrades, scheduling, NetworkPolicy, and troubleshooting. Follow with a full CKA course and Killer.sh practice. | I chose the KubeSkills kubeadm video (9 min, labeled 2025) over the DevopsCube multi-node video (16 min). The DevopsCube video has no date I could check, and it would not fit the budget alongside the other picks.

1. [klxZke9qbvg] Kubernetes Architecture Explained: Exploring etcd, Schedulers, Managers, and Node Components - 9 min
   Curriculum's reason: The KodeKloud lecture is tied to the CKA course. It walks through etcd, the scheduler, controllers, the API server, kubelet and kube-proxy, which the learner doesn't know yet.
   Quote [03:13]: "The master node is responsible for managing the Kubernetes cluster, storing information regarding the different nodes"
   Quote [08:19]: "The kube API server is the primary management component of Kubernetes. The kube API server is responsible for orchestrating all operations within the cluster"
   REFERENCE SUMMARY: This lecture explains Kubernetes cluster architecture using a cargo ship analogy, covering the control plane (master node) and worker node components. It introduces etcd, kube-scheduler, controllers, kube-apiserver, kubelet, and kube-proxy, explaining their roles and responsibilities in managing containerized applications. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

2. [j3a2Sr2n8eQ] How to Install Kubernetes with Kubeadm (2025 Update) | Full Cluster Setup Walkthrough - 9 min
   Curriculum's reason: A 2025 walkthrough that builds a control plane and worker with containerd, kubeadm init, kubeadm join and a Calico CNI. This is the setup flow the learner needs.
   Quote [00:00]: "we're going to be installing the container D runtime, the Kube ADM, Kublet, and Kubectl to install our Kubernetes cluster"
   Quote [10:27]: "Kube ADM join, and then that contains the token that's going to join the worker node to the cluster"
   REFERENCE SUMMARY: This video walks through installing a production-grade Kubernetes cluster from scratch using kubeadm on Ubuntu 22.04 with containerd runtime and Calico CNI. It covers installing containerd, kubeadm, kubelet and kubectl, configuring network settings, initializing the control plane, joining a worker node, and installing the CNI to make the cluster ready. Builds: A two-node Kubernetes cluster (control plane and worker node) using kubeadm, containerd, and Calico CNI. Level: beginner. Format: project_build. Language: en.

3. [ZDFqVFbX0Ic] Day 13: Imperative commands for Deployments, Services and Troubleshooting | CKA Course 2025 - 13 min (watch 00:00-13:20)
   Curriculum's reason: A CKA 2025 course lesson that uses imperative commands to generate deployment YAML skeletons (dry-run), create deployments, and expose them as services. The first ~13 minutes teach the exam-speed workflow.
   Quote [00:00]: "imperative commands are super handy for quick testing, troubleshooting, and even during the CKA exam"
   Quote [03:46]: "imperative commands can do those things quickly. So we can use imperative commands to create a skeleton deployment YAML"
   REFERENCE SUMMARY: This video teaches imperative kubectl commands for creating Kubernetes Deployments and Services in a hands-on CKA exam context. It covers creating backend and frontend deployments, exposing them with services, and testing inter-pod connectivity using curl and DNS resolution, demonstrating how imperative commands can save time during the exam. Builds: Multi-tier application with frontend and backend deployments exposed via ClusterIP and NodePort services, with test pod for connectivity validation. Level: intermediate. Format: project_build. Language: en.

4. [YNPap3UH1IA] How to Pass the CKA Exam in 2026 | Certified Kubernetes Administrator - 13 min
   Curriculum's reason: It covers the exam rules (one docs tab), time management, repetition-based practice and mock exam resources. That is the exam orientation the learner asked for.
   Quote [00:29]: "during the test, you're allowed to have one additional tab open with your Kubernetes documentation"
   Quote [01:50]: "this exam is, it's about two things. One, knowing how to do the material, but two, also knowing how to manage your time"
   REFERENCE SUMMARY: A study strategy guide for passing the CKA exam as a beginner, covering exam rules, time management, recommended learning resources (CodeCloud/Mumshad's course), documentation bookmarking techniques, and the Killer.sh exam simulator. The video focuses on exam preparation methods rather than teaching Kubernetes concepts hands-on. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

### impossible_k8s_in_45 / S2

Planned viewing time: 44 of 45 min.

1. [TlHvYWVUZyc] Kubernetes Explained in 6 Minutes | k8s Architecture - 6 min
   Curriculum's reason: Popular result (1,981,362 views) for 'Kubernetes architecture explained control plane worker node CKA'.
   REFERENCE SUMMARY: This video explains Kubernetes as a container orchestration platform, covering its architecture with control plane (API server, etcd, scheduler, controller manager) and worker node components (kubelet, container runtime, kube-proxy). It discusses when to use Kubernetes and the trade-offs between scalability/portability and complexity/cost, including the option of managed Kubernetes services. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

2. [T4Z7visMM4E] Kubernetes Services explained | ClusterIP vs NodePort vs LoadBalancer vs Headless Service - 24 min
   Curriculum's reason: Popular result (693,147 views) for 'Kubernetes services ClusterIP NodePort explained CKA'.
   REFERENCE SUMMARY: This video provides a comprehensive explanation of Kubernetes Services, covering five types: ClusterIP, Headless, NodePort, LoadBalancer, and Multi-Port services. The instructor explains when and why each service type is used, how services provide stable IP addresses and load balancing for pods, and the concepts of selectors, labels, ports, and endpoints that enable service-to-pod communication. Level: beginner. Format: concept_explainer. Language: en.

3. [oGPjzCBZGzg] Docker vs. Kubernetes: The ONLY Video You Need to Finally Understand Containers! - 6 min
   Curriculum's reason: Popular result (487,014 views) for 'Kubernetes pods deployments replicasets explained for Docker users'.
   REFERENCE SUMMARY: This video explains the relationship between Docker and Kubernetes, comparing Docker's role as a container packaging tool with Kubernetes's role as a container orchestration platform. It covers how Kubernetes manages containers at scale through Pods, Deployments, ReplicaSets, and features like horizontal pod autoscaling and self-healing, demonstrating how Docker and Kubernetes work together in production environments. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

4. [vmCuNJiNzfg] Kubernetes Architecture in 7 minutes | K8s explained - 7 min
   Curriculum's reason: Popular result (85,924 views) for 'Kubernetes architecture explained control plane worker node CKA'.
   REFERENCE SUMMARY: A high-level overview of Kubernetes cluster architecture, explaining the roles of master (control plane) and worker nodes, and the key components within each: API server, scheduler, controller manager, and etcd on the master; kubelet, container runtime, and kube-proxy on worker nodes. The video focuses on conceptual understanding of how these components interact to manage pods and cluster state. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

### impossible_k8s_in_45 / S3

Planned viewing time: 43 of 45 min.
Assumptions stated: 'Nothing from before 2023' means videos must be published in 2023 or later, and since titles are the only signal available, titles that mention older years or outdated exam versions are excluded.; The learner will use the remaining CKA preparation (practice labs, mock exams) outside this 45-minute video plan.; The learner has no prior Kubernetes exposure, so the plan starts at architecture and does not assume cloud-managed clusters.; The current CKA curriculum covers cluster architecture/installation/configuration, workloads and scheduling, services and networking, storage, and troubleshooting.
Feasibility note: Deep Kubernetes mastery and passing the CKA cannot be achieved in 45 minutes of video. Realistic in this budget: understand the CKA scope and format, learn Kubernetes architecture, pods/deployments/services, core kubectl usage, and see a kubeadm cluster setup walkthrough, which gives a foundation for later hands-on practice and mock exams.
Warnings to the learner: Feasibility: deep Kubernetes mastery and passing the CKA cannot be achieved in 45 minutes of video. This plan is a foundation only; the CKA is a hands-on exam, so you need lab practice and mock exams afterwards. | No verified quotes were available for any candidate, and every transcript is poor or metadata-only. Every pick is therefore judged from titles and summaries and carries moderate confidence; evidence_quote_ids are empty throughout. | The kubectl pick uses an assumed 0-9 minute range of a 31-minute lecture, because the card has no segment map. Check that the range makes sense and keep watching if it is useful. | Services coverage is thin: the pick covers NodePort and the endpoints/selector workflow, but ClusterIP, LoadBalancer and basic cluster networking concepts get little time.

1. [SuKkL8YjXMg] CKA Exam Prep: How I Became a Kubestronaut - 4 min
   Curriculum's reason: Gives a CKA-specific roadmap of exam format and key topics, and it is the only post-2023 exam-overview video that fits the 4-minute slot. This sets the scope before any Kubernetes content.
   REFERENCE SUMMARY: This video is a CKA exam preparation roadmap sharing the presenter's personal journey to passing the exam. It covers the exam format, the 2025 exam changes, study strategy using the CodeCloud CKA course, mock exams via KillerKoda and KillerShell, and five key tips for exam success: kubectl speed, using documentation, verifying work, troubleshooting practice, and time management. Level: beginner. Format: vlog. Language: en. Flags: surface_intro, pure_theory, vlog.

2. [5NHMNVeutT8] Kubernetes Architecture Explained: Control Plane, Nodes & Pod Lifecycle | CKA Ch 1.1 - 10 min
   Curriculum's reason: A CKA-chapter video that covers control plane components (kube-apiserver, etcd, scheduler, controller-manager) and node components (kubelet, runtime, kube-proxy, CNI). It also walks the Deployment-to-Running-Pod lifecycle and shows how to match failure symptoms to components, which is useful for troubleshooting questions.
   REFERENCE SUMMARY: This video explains Kubernetes architecture by detailing the control plane components (API server, etcd, scheduler, controller manager) and worker node components (kubelet, container runtime, kube-proxy, CNI), then walks through the exact six-step process of deploying a pod from kubectl apply to running. It includes practical troubleshooting practice matching failure symptoms to components. Level: beginner. Format: concept_explainer. Language: en.

3. [yeUBojfuhiI] EP05 - Kubernetes Deployments & ReplicaSets - 6 min
   Curriculum's reason: Explains Deployments and ReplicaSets (self-healing, scaling, rolling updates), then creates a Deployment from a YAML manifest with kubectl. This gives a Docker user the jump from single containers to managed replicas.
   REFERENCE SUMMARY: This episode explains Kubernetes Deployments and ReplicaSets, demonstrating how they provide self-healing, high availability, horizontal scaling, and rolling updates. The video includes hands-on demonstrations of creating a Deployment manifest from official Kubernetes documentation, applying it with kubectl, and testing self-healing by deleting a pod to show automatic recovery. Level: beginner. Format: concept_explainer. Language: en.

4. [yL_DurdVxak] Stop Losing Easy Points on the CKA: Complete NodePort Workflow (CKA Trap) - 4 min
   Curriculum's reason: A CKA-oriented NodePort workflow that exposes a Deployment. It covers common exam traps: missing container ports, invalid kubectl flags, and selector mismatches that leave a Service with no Endpoints.
   REFERENCE SUMMARY: A focused CKA exam prep video teaching the correct workflow to expose a Kubernetes deployment using a NodePort service. The video demonstrates the exact four-step process: inspecting the deployment, adding containerPort to the deployment spec, generating service YAML with --dry-run=client, manually editing the YAML to set the nodePort value, and verifying with curl. It emphasizes the common CKA trap that kubectl expose cannot directly set custom NodePort values. Builds: NodePort service for exposing a deployment on port 30080. Level: beginner. Format: project_build. Language: en.

5. [ZDFqVFbX0Ic] Day 13: Imperative commands for Deployments, Services and Troubleshooting | CKA Course 2025 - 9 min (watch 00:00-09:00)
   Curriculum's reason: Part of a CKA 2025 course on imperative commands for Deployments, Services and troubleshooting, which is the exam-speed kubectl skill needed. Only the opening segment is used to fit the budget.
   REFERENCE SUMMARY: This video teaches imperative kubectl commands for creating Kubernetes Deployments and Services in a hands-on CKA exam context. It covers creating backend and frontend deployments, exposing them with services, and testing inter-pod connectivity using curl and DNS resolution, demonstrating how imperative commands can save time during the exam. Builds: Multi-tier application with frontend and backend deployments exposed via ClusterIP and NodePort services, with test pod for connectivity validation. Level: intermediate. Format: project_build. Language: en.

6. [j3a2Sr2n8eQ] How to Install Kubernetes with Kubeadm (2025 Update) | Full Cluster Setup Walkthrough - 9 min
   Curriculum's reason: A step-by-step kubeadm cluster install on Ubuntu 22.04 with containerd and Calico CNI. It has no red flags and was updated for 2025, so the learner sees the init and join flow that the CKA tests.
   REFERENCE SUMMARY: This video walks through installing a production-grade Kubernetes cluster from scratch using kubeadm on Ubuntu 22.04 with containerd runtime and Calico CNI. It covers installing containerd, kubeadm, kubelet and kubectl, configuring network settings, initializing the control plane, joining a worker node, and installing the CNI to make the cluster ready. Builds: A two-node Kubernetes cluster (control plane and worker node) using kubeadm, containerd, and Calico CNI. Level: beginner. Format: project_build. Language: en.

Considered and dropped:
- Kubernetes Architecture Explained: Exploring etcd, Schedulers, Managers, and Node Components: A solid 9-minute architecture explainer, but flagged pure_theory and not exam-framed. 5NHMNVeutT8 covers the same components plus the pod lifecycle and failure mapping.
- Setup Kubernetes Cluster Using Kubeadm [Multi-node]: A 2023 multi-node kubeadm walkthrough, but at 16.4 minutes it would push the plan over budget. It is also a different creator and setup from the chosen kubeadm video.
- How to Setup a Kubernetes Cluster using Kubeadm on Ubuntu | K8S Cluster Setup| LinuxGKTech: A 2026 kubeadm setup, but at 21.6 minutes it is too long for the slot. Much of it is port and prerequisite discussion.
- Kubernetes Services explained | ClusterIp NodePort & LB| Part - 2 ..... #Kubernetes #CKA @AlokKumar: A 2023 CKA-tagged Services video, but flagged pure_theory and 28 minutes long with no segment map to excerpt from. It is far over the services slot.
- How to Pass the CKA Exam in 2026 | Certified Kubernetes Administrator: The title says 2026, but the upload date is 2022, which breaks the learner's 2023 floor. It is also flagged surface_intro with no transcript.
- Kubernetes Crash Course for Absolute Beginners [NEW]: A 2021 upload, which breaks the 2023 floor, and 72 minutes long with no transcript.
- Upgrade Kubernetes Cluster with Kubeadm in 2024: Step-by-Step Guide | CKA | CKS | TechWiseRahul: Covers kubeadm cluster upgrades, not initial setup. It is an intermediate topic the learner is not ready for in this budget.
- Kubernetes Cluster Setup 2026 | Kubeadm Multi-Node Installation: Its title says 2026 but the upload date is 2023, an inconsistency. It is 18.8 minutes long, and the card's segment map gives little evidence of setup depth.
- How Kubernetes Heals Itself: ReplicaSets Explained: Covers ReplicaSets only. yeUBojfuhiI covers Deployments and ReplicaSets with a hands-on part in less time.

### impossible_k8s_in_45 / S4

Planned viewing time: 44 of 45 min.
Assumptions stated: 'Nothing from before 2023' means videos must be published in 2023 or later, and since titles are the only signal available, titles that mention older years or outdated exam versions are excluded.; The learner will use the remaining CKA preparation (practice labs, mock exams) outside this 45-minute video plan.; The learner has no prior Kubernetes exposure, so the plan starts at architecture and does not assume cloud-managed clusters.; The current CKA curriculum covers cluster architecture/installation/configuration, workloads and scheduling, services and networking, storage, and troubleshooting.
Feasibility note: Deep Kubernetes mastery and passing the CKA cannot be achieved in 45 minutes of video. Realistic in this budget: understand the CKA scope and format, learn Kubernetes architecture, pods/deployments/services, core kubectl usage, and see a kubeadm cluster setup walkthrough, which gives a foundation for later hands-on practice and mock exams.
Warnings to the learner: Infeasible as stated: 45 minutes of video cannot teach Kubernetes deeply or get anyone through the CKA. This plan gives a foundation; real practice labs and mock exams (e.g. killer.sh) are needed afterwards. | No post-2022 candidate in the pool is a clean CKA exam overview. The only dedicated overview videos were either flagged (vlog) or pre-2023, so cka_overview is covered only partly, through the exam-scenario framing in the NodePort video and the CKA framing in the architecture video. | Planned viewing time is about 43.6 of 45 minutes (about 97%). The ZDFqVFbX0Ic range (3:46-18:00) stops before its NodePort and DNS/connectivity-testing sections to fit the budget. | Services and networking is covered thinly: ClusterIP in the course excerpt and NodePort in the short exam video. Ingress, DNS and network policies are not covered.

1. [5NHMNVeutT8] Kubernetes Architecture Explained: Control Plane, Nodes & Pod Lifecycle | CKA Ch 1.1 - 10 min
   Curriculum's reason: Gives a CKA-framed walk through control plane components (API server, etcd, scheduler, controller manager) and worker components (kubelet, runtime, kube-proxy, CNI). It also traces the six steps from kubectl apply to a running pod, which links the architecture to the objects that follow.
   Quote [01:50]: "The control plane makes decisions and stores the cluster's state. The worker nodes run your applications."
   Quote [10:01]: "First, Kube control sends the request to the API server, which authenticates it, authorizes it, runs admission, and stores the deployment in ETCD."
   REFERENCE SUMMARY: This video explains Kubernetes architecture by detailing the control plane components (API server, etcd, scheduler, controller manager) and worker node components (kubelet, container runtime, kube-proxy, CNI), then walks through the exact six-step process of deploying a pod from kubectl apply to running. It includes practical troubleshooting practice matching failure symptoms to components. Level: beginner. Format: concept_explainer. Language: en.

2. [yeUBojfuhiI] EP05 - Kubernetes Deployments & ReplicaSets - 6 min
   Curriculum's reason: Explains how a Deployment declares the desired state and how the ReplicaSet keeps the pods running. It shows a Deployment manifest being applied and a pod being deleted and recreated, which gives the learner the object model before the imperative commands.
   Quote [00:20]: "The deployment defines the desired state, in this case three replicas. Then, the replica set ensures that three pods are always running."
   Quote [01:44]: "The replica set constantly checks if the desired number of pods is running. So, if one pod crashes or disappears, Kubernetes automatically creates a new one to replace it."
   REFERENCE SUMMARY: This episode explains Kubernetes Deployments and ReplicaSets, demonstrating how they provide self-healing, high availability, horizontal scaling, and rolling updates. The video includes hands-on demonstrations of creating a Deployment manifest from official Kubernetes documentation, applying it with kubectl, and testing self-healing by deleting a pod to show automatic recovery. Level: beginner. Format: concept_explainer. Language: en.

3. [ZDFqVFbX0Ic] Day 13: Imperative commands for Deployments, Services and Troubleshooting | CKA Course 2025 - 14 min (watch 03:46-18:00)
   Curriculum's reason: A CKA-course lesson on creating deployments imperatively, using --dry-run to generate YAML skeletons, and exposing them as ClusterIP services. It covers the exam-speed kubectl habits the learner needs, and the range stops before the NodePort and DNS-testing sections to fit the budget.
   Quote [00:00]: "imperative commands are super handy for quick testing, troubleshooting, and even during the CKA exam"
   Quote [03:46]: "imperative commands can do those things quickly. So we can use imperative commands to create a skeleton deployment YAML"
   REFERENCE SUMMARY: This video teaches imperative kubectl commands for creating Kubernetes Deployments and Services in a hands-on CKA exam context. It covers creating backend and frontend deployments, exposing them with services, and testing inter-pod connectivity using curl and DNS resolution, demonstrating how imperative commands can save time during the exam. Builds: Multi-tier application with frontend and backend deployments exposed via ClusterIP and NodePort services, with test pod for connectivity validation. Level: intermediate. Format: project_build. Language: en.

4. [yL_DurdVxak] Stop Losing Easy Points on the CKA: Complete NodePort Workflow (CKA Trap) - 4 min
   Curriculum's reason: A short CKA-style task: expose a deployment with a NodePort service. It covers the trap that kubectl expose cannot set a custom nodePort and the dry-run-then-edit workflow. It also gives a realistic sense of how the exam scores such tasks.
   Quote [00:49]: "The trap is that the kubectl expose doesn't let you pass a custom nodeport flag directly."
   Quote [03:40]: "We must use the dry run client to create a YAML file to generate the basic server spec instantly and dump it to the YAML."
   REFERENCE SUMMARY: A focused CKA exam prep video teaching the correct workflow to expose a Kubernetes deployment using a NodePort service. The video demonstrates the exact four-step process: inspecting the deployment, adding containerPort to the deployment spec, generating service YAML with --dry-run=client, manually editing the YAML to set the nodePort value, and verifying with curl. It emphasizes the common CKA trap that kubectl expose cannot directly set custom NodePort values. Builds: NodePort service for exposing a deployment on port 30080. Level: beginner. Format: project_build. Language: en.

5. [j3a2Sr2n8eQ] How to Install Kubernetes with Kubeadm (2025 Update) | Full Cluster Setup Walkthrough - 9 min
   Curriculum's reason: A compact 2025 kubeadm walkthrough: install containerd and kubeadm/kubelet/kubectl, run kubeadm init, join a worker with the join token, and apply the Calico CNI. This is the cluster-setup part of the CKA that this learner has never seen.
   Quote [00:00]: "we're going to be installing the container D runtime, the Kube ADM, Kublet, and Kubectl to install our Kubernetes cluster"
   Quote [10:27]: "Kube ADM join, and then that contains the token that's going to join the worker node to the cluster"
   REFERENCE SUMMARY: This video walks through installing a production-grade Kubernetes cluster from scratch using kubeadm on Ubuntu 22.04 with containerd runtime and Calico CNI. It covers installing containerd, kubeadm, kubelet and kubectl, configuring network settings, initializing the control plane, joining a worker node, and installing the CNI to make the cluster ready. Builds: A two-node Kubernetes cluster (control plane and worker node) using kubeadm, containerd, and Calico CNI. Level: beginner. Format: project_build. Language: en.

Considered and dropped:
- CKA Exam Prep: How I Became a Kubestronaut: Flagged as a vlog, surface intro and pure theory. It is a personal story with only brief exam-format coverage, and the yL_DurdVxak exam-scenario pick replaces it.
- How to Pass the CKA Exam in 2026 | Certified Kubernetes Administrator: Upload date is 2022, which breaks the learner's no-pre-2023 limit, even though its title says 2026.
- Setup Kubernetes Cluster Using Kubeadm [Multi-node]: A good kubeadm video from 2023, but its Terraform/AWS infrastructure setup makes it longer and heavier than the focused kubeadm walkthrough chosen.
- Kubernetes Architecture Explained: Control Plane & Worker Node Components: Unflagged architecture video, but it runs about 28 minutes and would take most of the budget; the chosen video covers architecture plus the pod workflow in 10 minutes.
- Day-31 | KUBERNETES ARCHITECTURE USING EXAMPLES | Kubernetes is Easy #devops #k8s #devopscourse: Flagged pure_theory, 25 minutes long, and spends much of its time on Docker background the learner already knows.
- Kubernetes Architecture Explained: Exploring etcd, Schedulers, Managers, and Node Components: Flagged pure_theory and covers architecture only, with no link to pod workflow or the CKA.
- Kubernetes Explained in 6 Minutes | k8s Architecture: Flagged as a surface intro that includes use-case and trade-off discussion; a CKA-framed unflagged architecture video exists.
- Kubernetes Services explained | ClusterIp NodePort & LB| Part - 2 ..... #Kubernetes #CKA @AlokKumar: 28 minutes on services in an EKS cluster. This is a managed-cloud setup, and the services material is covered more efficiently elsewhere.
- Kubernetes Crash Course: Learn the Basics and Build a Microservice Application: A 130-minute crash course assessed from metadata only, so the evidence is weak and it does not fit the 45-minute budget.

## lunch_break_sql_windows

```
Goal: Understand SQL window functions well enough to rewrite my self-join reports
Time budget: 30 minutes
Background: Data analyst, 3 years writing SQL reports in PostgreSQL
Already knows: SELECT, WHERE, JOIN, GROUP BY and aggregates, subqueries, self-joins
Does not know yet: window functions, PARTITION BY, ROW_NUMBER / RANK, running totals with window frames, LAG / LEAD
Constraints: Only a lunch break. Practical examples, no full SQL courses. Switching videos wastes my time: two videos at most.
```

### lunch_break_sql_windows / S1

Planned viewing time: 30 of 30 min.
Assumptions stated: Self-join reports are typically previous-row comparisons, top-N per group, and running totals, so those patterns are prioritised.; Videos that don't use PostgreSQL are acceptable here because window-function syntax is the same.; Video summaries are the only evidence of content. The picks were not watched end to end.
Warnings to the learner: Total is about 29.9 minutes of a 30-minute budget, so there is no slack for pausing. If time runs short, watch only the first video and skip the second. | The two picks overlap on partitions, ranking and running totals. I kept the second because it is PostgreSQL-specific and shows rolling sums on a different dataset. It has no LAG/LEAD, so the first video is the only coverage of that topic. | Neither video explicitly walks through rewriting a self-join as a window function. The month-over-month and top-N patterns in the first video are the closest match, so you will need to apply the rewrite to your own reports. | Among the alternatives, techTFQ (24.9 min) covers LAG/LEAD but has no running totals, and it would have pushed the plan over budget alongside a second video.

1. [dUzivpyLK1s] SQL Window Functions Explained: ROW_NUMBER, RANK, LAG, LEAD - 16 min
   Curriculum's reason: It covers every gap in one pass: OVER/PARTITION BY, the ranking functions, LAG/LEAD, running totals and ROWS BETWEEN frames. It also shows report-style patterns (top-N per group, month-over-month growth) and common mistakes, and it uses an online store database.
   Quote [00:24]: "A window function keeps every row and adds a calculated value next to each one."
   Quote [00:46]: "Partition by decides which rows belong together. Order by decides the sequence inside each group."
   REFERENCE SUMMARY: This video teaches SQL window functions from OVER and PARTITION BY basics through ranking functions (ROW_NUMBER, RANK, DENSE_RANK), LAG/LEAD for row comparisons, and running totals with window frames. It covers practical patterns like top-N per group, month-over-month growth, moving averages, and mistakes to avoid, using a real online store database. Level: intermediate. Format: concept_explainer. Language: en.

2. [wp8f2ShK9Ro] Window Functions in PostegreSQL - 14 min
   Curriculum's reason: It is a second walkthrough in PostgreSQL. It reinforces the comparison with GROUP BY and PARTITION BY, then works through running and rolling sums with frames. Seeing those queries run in the learner's own database helps them transfer the pattern to their reports.
   Quote [00:24]: "When I think of a window function, I actually compare it a lot to something like a group by"
   Quote [00:24]: "We take it row by row, but then we apply it to each row. We don't aggregate it all into one row."
   REFERENCE SUMMARY: This video teaches SQL window functions in PostgreSQL, covering ROW_NUMBER, RANK, DENSE_RANK for ranking within partitions, and aggregate window functions like SUM and AVG for running totals and rolling averages. The instructor uses practical Star Wars character data examples to demonstrate how OVER() and PARTITION BY differ from GROUP BY, showing how to apply calculations row-by-row instead of collapsing rows. Level: intermediate. Format: concept_explainer. Language: en.

Considered and dropped:
- SQL Window Function | How to write SQL Query using RANK, DENSE RANK, LEAD/LAG | SQL Queries Tutorial: It has good self-join-replacement framing, but it has no running totals or frames, which are a stated gap. At 24.9 minutes it also cannot be paired with another video within 30 minutes.
- SQL Window Functions EXPLAINED: The Only Tutorial You'll Ever Need!: It is flagged too_basic_for_learner. It only covers ROW_NUMBER, RANK and DENSE_RANK, and it has no LAG/LEAD or frames.
- Window Functions in SQL Full Tutorial 🔥 | ROW_NUMBER, RANK, LAG, LEAD Explained: I could only read its chapter list and description, not a transcript, so I can't confirm it covers running totals or frames. It is 29.6 minutes, which uses the whole budget by itself.
- SQL Window Functions Explained: OVER, PARTITION BY, RANK, LAG, Running Totals: Its content is nearly identical to the chosen first video, with ranking, LAG, running totals and frames. It is the same format and level, so it would be a duplicate. I preferred DataBite because its summary adds top-N per group, month-over-month growth and a mistakes section.

### lunch_break_sql_windows / S2

Planned viewing time: 19 of 30 min.
Assumptions stated: Self-join reports are typically things like previous-row comparisons, running totals, and top-N per group, which map to LAG/LEAD, window frames, and ROW_NUMBER/RANK.; Videos should use PostgreSQL or standard SQL syntax that works in PostgreSQL.; Two videos at most means the plan should favor one comprehensive practical video plus optionally one short complementary video, not many small ones.; No practice time is reserved, so the 30 minutes is all watching.
Warnings to the learner: Total viewing time is 18.9 of 30 min (63%), leaving 11.1 min unused. The other candidates that covered the remaining sub-topics repeated the first pick, were over budget, or lacked usable transcripts, so I did not add them. | No candidate card has verified quotes, so evidence_quote_ids are empty. All reasons rest on card summaries and topic lists, not checked transcript content. | The self-join rewriting sub-topic is only thinly covered. No candidate clearly walks through converting a self-join report into a window query. Expect to practise the mapping yourself, for example a self-join on id-1 becomes LAG, a join with a <= condition becomes SUM() OVER (ORDER BY ...), and top-N per group becomes ROW_NUMBER() filtered in a subquery or CTE. | I assumed the examples in both videos use standard SQL that runs in PostgreSQL. The tool tags suggest so, but this is unverified.

1. [Kd64mv2kjX8] SQL Window Functions Explained: OVER, PARTITION BY, RANK, LAG, Running Totals - 13 min
   Curriculum's reason: The only unflagged candidate that covers OVER/PARTITION BY, ROW_NUMBER/RANK/DENSE_RANK, LAG/LEAD and running totals with window frames in one PostgreSQL-friendly video. Its example of ranking sales reps per region without losing rows is the kind of top-N-per-group report you now write with self-joins.
   REFERENCE SUMMARY: This video teaches SQL window functions through a worked example with a sales table, covering the OVER clause, PARTITION BY, ORDER BY within windows, ranking functions (ROW_NUMBER, RANK, DENSE_RANK), running totals with SUM OVER, LAG and LEAD for row comparisons, and moving averages with ROWS BETWEEN frames. The instructor contrasts window functions with GROUP BY to show how windows preserve individual rows while adding aggregate calculations. Level: intermediate. Format: concept_explainer. Language: en.

2. [UkFjJ0Wvtjs] How to Use Window Functions for High-Performance Postgres Queries - 6 min
   Curriculum's reason: Presents PostgreSQL window functions as a replacement for self-joins and subqueries, with running totals, rolling averages and ranking. It is the only short candidate aimed at your rewrite goal, so it ties the first video's functions back to your self-join reports.
   REFERENCE SUMMARY: This video teaches PostgreSQL window functions for analytical queries, demonstrating how they outperform self-joins and external processing. It walks through a practical case study: building a real-time dashboard query that calculates running totals and moving averages of workspace metrics using window frames and indexes. Builds: PostgreSQL query calculating running total of cost and five-row moving average of latency per workspace with index optimization. Level: intermediate. Format: project_build. Language: en.

Considered and dropped:
- SQL Window Functions Explained: ROW_NUMBER, RANK, LAG, LEAD: Covers the same four sub-topics as the first pick, in PostgreSQL, but at 15.5 min. A second general overview would mostly repeat the first and add nothing on self-join rewriting. It also has a poor transcript.
- SQL Running Total, LAG and LEAD, Moving Average, ROWS vs RANGE | Real-Time #6: Good on running totals, LAG/LEAD and ROWS vs RANGE, but it has no ranking coverage and nothing on self-joins. Kd64mv2kjX8 already covers those topics, and only two videos are allowed.
- LAG() & LEAD() in SQL Explained with Real Examples | Complete Window Functions Tutorial: LAG/LEAD only, in the sales-vs-previous-month style. Redundant with the first pick and leaves ranking and frames uncovered.
- SQL in 30 Days 🚀 | Day 15: Window Functions Explained with Real Examples: At 4.7 min it claims every topic, but that is too short to teach them in depth. Its poor transcript prevents verifying the content, and it is more of a quick overview than practical teaching.
- SQL Window Functions | Clearly Explained | PARTITION BY, ORDER BY, ROW_NUMBER, RANK, DENSE_RANK: Flagged surface_intro with a poor transcript. It covers only PARTITION BY and ranking, with no LAG/LEAD or frames.
- Running & Rolling Total | Moving & Rolling Average |  SQL Key Data Analysis Concepts: Covers only running totals and moving averages, at 19.1 min. That is too long for one sub-topic and it would not fit alongside the first pick.
- SQL Window Function | How to write SQL Query using RANK, DENSE RANK, LEAD/LAG | SQL Queries Tutorial: Flagged pure_theory. It has no frames or self-join content and runs 24.9 min, which would crowd out the second video.
- SQL Window Function Crash Course for Data Analyst : A 67-minute crash course with no transcript to check. It is far over the budget and is a course-length video, which you said you don't want.
- MySQL Window Functions Tutorial | ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD | SQL Interview Questions: MySQL-based, 59 min, and without a transcript. It is over budget and not PostgreSQL.

### lunch_break_sql_windows / S3

Planned viewing time: 29 of 30 min.

1. [Ww71knvhQ-s] SQL Window Function | How to write SQL Query using RANK, DENSE RANK, LEAD/LAG | SQL Queries Tutorial - 25 min
   Curriculum's reason: Popular result (1,675,229 views) for 'SQL window functions tutorial PostgreSQL practical examples'.
   REFERENCE SUMMARY: This tutorial covers SQL window functions (ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD) and how they differ from GROUP BY aggregates. It demonstrates partitioning data by department, ranking employees by salary, and comparing current rows with previous/next rows to solve complex analytical queries without self-joins. Level: intermediate. Format: concept_explainer. Language: en.

2. [Ubni4qPP2zQ] 🔍LEAD , LAG , NTILE ! Mastering Window Functions in SQL - 4 min
   Curriculum's reason: Popular result (646 views) for 'SQL LAG LEAD running total window frame ROWS BETWEEN tutorial'.
   REFERENCE SUMMARY: This video demonstrates three SQL window functions: LEAD (fetch next row value), LAG (fetch previous row value), and NTILE (divide data into N groups). The instructor shows practical examples using a smartphone pricing dataset, including calculating price differences between consecutive models. Level: intermediate. Format: concept_explainer. Language: en. Flags: surface_intro.

### lunch_break_sql_windows / S4

Planned viewing time: 23 of 30 min.
Assumptions stated: Self-join reports are typically things like previous-row comparisons, running totals, and top-N per group, which map to LAG/LEAD, window frames, and ROW_NUMBER/RANK.; Videos should use PostgreSQL or standard SQL syntax that works in PostgreSQL.; Two videos at most means the plan should favor one comprehensive practical video plus optionally one short complementary video, not many small ones.; No practice time is reserved, so the 30 minutes is all watching.
Warnings to the learner: Neither pick shows a self-join report rewritten as a window query side by side. The rewrite_self_joins sub-topic is covered only indirectly, through month-over-month LAG, top-N and running-total patterns. Map your own reports onto those patterns when you practice. | The plan targets about 23.1 of 30 minutes (77%), leaving roughly 6.9 minutes unused. The remaining candidates mostly repeat topics, and a third video would break your two-video limit. | The segment maps for both picks run past the stated durations. If either video is longer than listed, the total could exceed 30 minutes, so check the lengths before you start. | I assumed PostgreSQL or standard SQL is fine. No time is reserved for practice, so the 30 minutes is viewing only.

1. [dUzivpyLK1s] SQL Window Functions Explained: ROW_NUMBER, RANK, LAG, LEAD - 16 min
   Curriculum's reason: A PostgreSQL walkthrough that goes from OVER and PARTITION BY through ROW_NUMBER/RANK/DENSE_RANK top-N per group, LAG/LEAD month-over-month growth, and running totals with ROWS BETWEEN. It is one practical video that covers most of the plan, so the learner has a single setup to follow. It also ends with common mistakes such as a missing ORDER BY inside OVER.
   Quote [00:24]: "A window function keeps every row and adds a calculated value next to each one."
   Quote [00:46]: "Partition by decides which rows belong together. Order by decides the sequence inside each group."
   REFERENCE SUMMARY: This video teaches SQL window functions from OVER and PARTITION BY basics through ranking functions (ROW_NUMBER, RANK, DENSE_RANK), LAG/LEAD for row comparisons, and running totals with window frames. It covers practical patterns like top-N per group, month-over-month growth, moving averages, and mistakes to avoid, using a real online store database. Level: intermediate. Format: concept_explainer. Language: en.

2. [-JtMlZI6MZE] SQL Running Total, LAG and LEAD, Moving Average, ROWS vs RANGE | Real-Time #6 - 8 min
   Curriculum's reason: A second pass through the report-style patterns a self-join normally handles: running totals restarting per partition, month-over-month change with LAG/LEAD, and moving averages with explicit frames. It also warns about the ROWS vs RANGE frame trap. These patterns map directly onto the learner's self-join reports.
   Quote [01:54]: "PARTITION BY customer. The running total restarts for every customer."
   Quote [03:42]: "LAG reads the previous row's revenue, and LEAD reads the next row's."
   REFERENCE SUMMARY: This video teaches practical SQL window function techniques through six real interview questions: running totals with SUM() OVER(), the ROWS vs RANGE frame trap, LAG/LEAD for month-over-month comparisons, moving averages with explicit frames, percent-of-total calculations, and FIRST_VALUE/LAST_VALUE pitfalls. Each example includes complete queries with output and practical warnings for production use. Level: intermediate. Format: concept_explainer. Language: en.

Considered and dropped:
- SQL Window Functions Explained: OVER, PARTITION BY, RANK, LAG, Running Totals: Covers all four topics in 13 minutes, but is a generic sales-table walkthrough with no top-N-per-group pattern and no report-style content. It would add little over the first pick.
- SQL Window Functions Explained Visually (ROW_NUMBER, RANK, LEAD, LAG) 🎯: Short and mentions LAG replacing a self-join, but it skims every topic and would mostly repeat the first pick.
- How to Use Window Functions for High-Performance Postgres Queries: Directly contrasts window functions with self-joins in PostgreSQL, but it covers only running totals and moving averages, with no LAG/LEAD. The chosen second video covers more of the gaps.
- SQL Window Function | How to write SQL Query using RANK, DENSE RANK, LEAD/LAG | SQL Queries Tutorial: Good on ranking and LAG/LEAD, but at 24.9 minutes it would use most of the budget, and it has nothing on running totals or frames.
- [Database Lecture 22] Master SQL Window Functions | Running Total, Moving Average, LEAD & LAG: Complete coverage, but at 30.2 minutes it fills the whole budget, leaves no room for a second video, and is a lecture format rather than practical examples.
- SQL Window Functions | Clearly Explained | PARTITION BY, ORDER BY, ROW_NUMBER, RANK, DENSE_RANK: Clear on ranking and top-N with a subquery, but it does not cover frames or running totals, and its LAG/LEAD coverage is minimal.
- Running & Rolling Total | Moving & Rolling Average |  SQL Key Data Analysis Concepts: Excellent on running totals and frames, but at 19.1 minutes it covers only that one sub-topic and does not fit alongside a comprehensive first video.
- SQL Window Function Crash Course for Data Analyst : A 67-minute crash course with no transcript, so it could not be assessed, and it is also far too long for the budget.

## sourdough_first_loaf

```
Goal: Bake my first sourdough loaf this weekend; my starter is already active
Time budget: 120 minutes
Background: Home cook who has baked yeasted sandwich bread a few times
Already knows: kneading, yeasted bread basics, using an oven
Does not know yet: hydration and levain, bulk fermentation and stretch-and-folds, shaping a boule, cold retard, scoring, baking in a Dutch oven
Constraints: No vlogs or equipment reviews. I want a full bake-along I can follow, plus help with the steps beginners get wrong. Different bakers contradict each other, so follow at most two bakers' methods.
```

### sourdough_first_loaf / S1

Planned viewing time: 120 of 120 min.

1. [BJEHsvW2J6M] 15 Mistakes Most Beginner Sourdough Bakers Make - 22 min
   Curriculum's reason: Popular result (10,527,535 views) for 'common sourdough beginner mistakes and how to fix them'.
   REFERENCE SUMMARY: A comprehensive guide to making sourdough bread at home covering 15 common beginner mistakes, from maintaining an active starter through final baking. The video walks through the complete process including autolyse, bulk fermentation with stretch-and-folds, shaping, cold fermentation, and baking in a Dutch oven with practical tips for each stage. Builds: One complete sourdough loaf (50% whole wheat with sesame crust). Level: beginner. Format: project_build. Language: en.

2. [VEtU4Co08yY] YOUR FIRST SOURDOUGH (Sourdough Bread For Complete Beginners) - 14 min
   Curriculum's reason: Popular result (4,646,570 views) for 'beginner sourdough bread recipe full process start to finish Dutch oven'.
   REFERENCE SUMMARY: A complete beginner sourdough bake-along that walks through six stages: building a levain overnight, mixing, bulk fermentation with strength-building folds, shaping into a boule, proofing for 90 minutes, and baking in a Dutch oven or DIY pizza stone setup. The instructor uses lower hydration and higher starter ratios to make the process faster and easier for beginners. Builds: A complete sourdough loaf from start to finish using an active starter. Level: beginner. Format: project_build. Language: en.

3. [4gEoh3sk2AE] Bake the Perfect Sourdough Bread: A Step-by-Step Guide - 12 min
   Curriculum's reason: Popular result (3,492,933 views) for 'how to score sourdough and bake in Dutch oven beginner'.
   REFERENCE SUMMARY: This is a complete step-by-step sourdough bake-along showing how to feed a starter, mix dough, perform stretch-and-folds during bulk fermentation, shape a boule, cold retard in the fridge, score, and bake in a Dutch oven. The video covers the full process from starter preparation through cooling and slicing, with practical tips on hydration, surface tension for shaping, and equipment choices like using rice flour in the banneton and a pizza stone to prevent over-browning the bottom. Builds: One sourdough loaf. Level: beginner. Format: project_build. Language: en.

4. [-9Osn7JsP1Y] Easy Sourdough Starter Guide: Just Flour & Water! - 8 min
   Curriculum's reason: Popular result (3,306,938 views) for 'sourdough for beginners hydration and levain explained'.
   REFERENCE SUMMARY: This video teaches how to create an active sourdough starter from scratch using only flour and water over a 7-day feeding schedule. It covers daily feeding routines, signs of starter readiness, storage, and the float test to confirm the starter has sufficient rising power for baking. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, off_topic.

5. [9fWzWpL5g6w] 18 Sourdough Basics YOU Should Know - 22 min
   Curriculum's reason: Popular result (1,991,515 views) for 'sourdough for beginners hydration and levain explained'.
   REFERENCE SUMMARY: This video presents 18 essential sourdough basics covering starter management, flour selection, hydration levels, fermentation techniques, shaping, cold proofing, and baking. It explains concepts like fermentolyse vs autolyse, stretch-and-fold timing, bulk fermentation readiness, pre-shaping, Dutch oven baking with steam, and how to read crumb structure for troubleshooting. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

6. [QWiouzzCUcs] A Sourdough Masterclass for Home Bakers - 12 min
   Curriculum's reason: Popular result (1,606,560 views) for 'how to score sourdough and bake in Dutch oven beginner'.
   REFERENCE SUMMARY: Grant Bakes walks through a complete sourdough bake-along from feeding the starter through final bake. The method covers mixing, bulk fermentation with stretch-and-folds, pre-shaping, final shaping, cold overnight retard, and Dutch oven baking with scoring. Builds: A complete sourdough loaf baked in a Dutch oven. Level: beginner. Format: project_build. Language: en.

7. [CTuGXdyrWUo] The BEST Beginner Sourdough Bread Tutorial on YouTube - 12 min
   Curriculum's reason: Popular result (1,097,704 views) for 'beginner sourdough bread recipe full process start to finish Dutch oven'.
   REFERENCE SUMMARY: A complete beginner sourdough bake-along that guides you through feeding a starter, mixing dough, performing stretch-and-folds during bulk fermentation, shaping a boule, cold retarding overnight, scoring, and baking in a preheated Dutch oven. The recipe uses just four ingredients and takes about 24 hours total from starter feeding to finished loaf. Builds: One beginner sourdough loaf with crispy crust and soft fluffy interior. Level: beginner. Format: project_build. Language: en.

8. [s8dQ2hnYqp0] STEP-BY-STEP SOURDOUGH FOR BEGINNERS: How to Make Sourdough Starter & Sourdough Bread - 12 min
   Curriculum's reason: Popular result (988,191 views) for 'beginner sourdough bread recipe full process start to finish Dutch oven'.
   REFERENCE SUMMARY: A beginner-friendly guide to making sourdough starter from scratch (7-day process) and baking a complete sourdough loaf using the active starter. The video covers mixing, stretch-and-fold bulk fermentation, shaping, cold retarding overnight in the fridge, scoring, and baking in a Dutch oven with steam. Builds: A sourdough bread loaf (with a cinnamon sugar chocolate chip variation shown). Level: beginner. Format: project_build. Language: en.

9. [hWXA8xFYu9A] How to Shape a Bread into a Boule (Round Ball) - 4 min
   Curriculum's reason: Popular result (460,250 views) for 'how to shape a sourdough boule for beginners'.
   REFERENCE SUMMARY: Kathleen demonstrates how to shape a sourdough boule using surface tension techniques, including initial shaping, a bench rest period to relax gluten, final shaping, and placement in a banneton for the final proof. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

10. [Z8sno5EzPw4] Bulk Fermentation, a Visual Guide. Stop letting your dough double! - 2 min
   Curriculum's reason: Popular result (405,837 views) for 'sourdough cold retard overnight proofing poke test'.
   REFERENCE SUMMARY: Visual guide to recognizing when bulk fermentation is complete by observing dough characteristics (bubbles, jiggle, surface texture) rather than relying on time or doubling. Shows the differences between under-fermented, well-fermented, and over-fermented dough to help beginners identify the optimal fermentation window. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

### sourdough_first_loaf / S2

Planned viewing time: 87 of 120 min.
Assumptions stated: Bread Code (Hendrik) is the main baker for the method; Mike G (LifebyMikeG) is the second baker, used for mistakes and cautions only.; Where the two differ (for example Mike G's 50% whole-wheat recipe and 30-minute fold intervals), follow the Bread Code recipe and use Mike G for the principles.; Learner has a banneton or can use a bowl with a towel, and a Dutch oven or a similar covered pot.
Warnings to the learner: Bread Code's full course was chosen over Brian Lagerstrom's and Grant Bakes' bake-alongs because it explains the reasons behind each step, including cold retard and crumb diagnosis. Those two are near-duplicates and would add a third baker. | Only the Bread Code and Mike G methods are used, which meets the two-baker limit. Do not mix in other creators. | Total is about 87 of 120 minutes. The rest is left unused to avoid padding with redundant videos. The bake itself takes about 24 hours, with waiting time outside viewing time. | The shaping video shows a second, advanced stitching method. Skip it on your first loaf.

1. [9fWzWpL5g6w] 18 Sourdough Basics YOU Should Know - 22 min
   Curriculum's reason: It explains hydration, fermentolyse, stretch-and-fold, knowing when fermentation is done, cold retard and Dutch oven steam. This gives the vocabulary before baking, from the same baker as the bake-along.
   Quote [06:23]: "less water equals happier yeast and happier baker when you're making a sourdough starter"
   Quote [13:02]: "knowing when your fermentation is done is the secret to mastering sourdough bread"
   REFERENCE SUMMARY: This video presents 18 essential sourdough basics covering starter management, flour selection, hydration levels, fermentation techniques, shaping, cold proofing, and baking. It explains concepts like fermentolyse vs autolyse, stretch-and-fold timing, bulk fermentation readiness, pre-shaping, Dutch oven baking with steam, and how to read crumb structure for troubleshooting. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

2. [BJEHsvW2J6M] 15 Mistakes Most Beginner Sourdough Bakers Make - 22 min
   Curriculum's reason: It goes through 15 beginner errors in order, including an inactive starter, autolyse, the stretch-and-fold cadence, and the poke test for proofing. It is the second baker, used for cautions.
   Quote [00:47]: "having a really healthy active sourdough starter this is the life force of your bread this is the yeast"
   Quote [10:37]: "every 30 minutes you're gonna be repeating this stretch and fold process and you're gonna see each stretch and fold your dough is gonna be completely changing"
   REFERENCE SUMMARY: A comprehensive guide to making sourdough bread at home covering 15 common beginner mistakes, from maintaining an active starter through final baking. The video walks through the complete process including autolyse, bulk fermentation with stretch-and-folds, shaping, cold fermentation, and baking in a Dutch oven with practical tips for each stage. Builds: One complete sourdough loaf (50% whole wheat with sesame crust). Level: beginner. Format: project_build. Language: en.

3. [msqU-ylXWUs] Your First Sourdough Bread (FULL COURSE in 30 minutes) - 31 min
   Curriculum's reason: A complete beginner bake-along covering levain hydration, bulk fermentation with stretch-and-folds, shaping, banneton, cold retard, scoring and Dutch oven baking. It is the single recipe to follow.
   Quote [00:00]: "you will learn how to make the perfect sourdough bread at home. It has nice oven spring, it features a crisp crust, it's soft on the inside."
   Quote [11:09]: "with slightly wet hands, I am checking the dough now. And see this, exactly what I promised you. You developed this amazing gluten network simply by waiting."
   REFERENCE SUMMARY: A comprehensive beginner sourdough bake-along that guides you through the complete process from levain preparation through baking, with explanations of hydration, bulk fermentation with stretch-and-folds, shaping, cold retard, and Dutch oven baking techniques. The instructor emphasizes understanding the why behind each step and covers common beginner mistakes. Builds: A complete sourdough boule with proper oven spring, crisp crust, and open crumb structure. Level: beginner. Format: full_course. Language: en.

4. [Koab3fxN4t4] The Last PRESHAPING SOURDOUGH Tutorial You Ever Need - 4 min
   Curriculum's reason: It demonstrates pre-shaping with surface tension and warns against over-handling and degassing the dough. It comes from the same baker as the main recipe.
   Quote [02:11]: "With the tension we can create a nice-looking ball, so now I'm going in here, and with my left hand I'm pulling the dough."
   Quote [04:01]: "only pre-shape as much as you need. Don't too much, because else you're going to degas your dough and that's nothing that we want."
   REFERENCE SUMMARY: Hendrik from The Bread Code demonstrates the pre-shaping technique for sourdough after bulk fermentation, showing how to divide dough in half and shape it into a round with proper surface tension using minimal flour and controlled hand movements. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

5. [h7eqwYLv2tI] The ONLY SOURDOUGH BREAD SHAPING Tutorial You Will Ever Need - 8 min
   Curriculum's reason: It shows final boule shaping, including how surface tension leads to oven spring and how to prepare the banneton with rice flour. Use the simpler beginner method first.
   Quote [01:25]: "you're trying to pull your dough together to create a lot of tension this tension will later on result in oven spring"
   Quote [00:20]: "rice flour is advised it's going to absorb a lot more humidity so sprinkle your banneton with a little bit of rice flour"
   REFERENCE SUMMARY: This video demonstrates two shaping techniques for sourdough loaves: a simpler beginner method and a more advanced technique using stitching. Both methods focus on creating surface tension by pulling and rolling the dough, preparing it for placement in a banneton for final proof before baking. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

### sourdough_first_loaf / S3

Planned viewing time: 101 of 120 min.
Assumptions stated: The 'weekend' bake means mixing Friday/Saturday, a cold retard overnight, and baking the next day, so a 1-2 day timeline is acceptable.; The learner owns or can get a Dutch oven, a kitchen scale, and a banneton or a bowl with a towel.; The learner wants a standard country-style white or lightly whole-wheat boule at around 70-75% hydration, not an advanced high-hydration loaf.; Since 'at most two bakers' methods' is required, the plan favors one primary full bake-along baker plus one optional secondary for troubleshooting.
Warnings to the learner: The near-duplicate cluster (4gEoh3sk2AE, CTuGXdyrWUo, QWiouzzCUcs) was not used because of the two-baker limit, so none of its members is kept. | The plan uses 100.6 of 120 minutes (about 84%), leaving 19.4 minutes unused. The remaining good candidates are from other creators or duplicate the recipe, and adding them would break the two-baker limit. | The baking is done by two bakers: The Bread Code (primary: the course, the hydration and fermentation concepts, shaping, and the cold-proof bake) and Keep it Sweet Kitchen (mistakes only). Follow the Bread Code recipe and use the Keep it Sweet video only as troubleshooting. | Some segment maps do not match the listed durations (for example the course lists sections past its length). Whole videos are listed and counted at their stated minutes.

1. [msqU-ylXWUs] Your First Sourdough Bread (FULL COURSE in 30 minutes) - 31 min
   Curriculum's reason: This is a full beginner bake-along that goes from levain and hydration through bulk with stretch-and-folds, shaping, cold retard, scoring and the Dutch oven bake. It explains the why of each step and ends with crumb troubleshooting. It works as the single recipe to follow this weekend, and it suits a yeast baker who needs the sourdough-specific steps.
   Quote [00:00]: "you will learn how to make the perfect sourdough bread at home. It has nice oven spring, it features a crisp crust, it's soft on the inside."
   Quote [11:09]: "with slightly wet hands, I am checking the dough now. And see this, exactly what I promised you. You developed this amazing gluten network simply by waiting."
   REFERENCE SUMMARY: A comprehensive beginner sourdough bake-along that guides you through the complete process from levain preparation through baking, with explanations of hydration, bulk fermentation with stretch-and-folds, shaping, cold retard, and Dutch oven baking techniques. The instructor emphasizes understanding the why behind each step and covers common beginner mistakes. Builds: A complete sourdough boule with proper oven spring, crisp crust, and open crumb structure. Level: beginner. Format: full_course. Language: en.

2. [9fWzWpL5g6w] 18 Sourdough Basics YOU Should Know - 22 min
   Curriculum's reason: The same baker explains hydration levels, water ratios, fermentolyse, stretch-and-fold timing and how to know bulk fermentation is done. This fills in the hydration and fermentation concepts you lack, using the same method as the main bake-along. It is flagged surface_intro, but the unflagged course gives less depth on these concepts and no other creator is needed.
   Quote [06:23]: "less water equals happier yeast and happier baker when you're making a sourdough starter"
   Quote [13:02]: "knowing when your fermentation is done is the secret to mastering sourdough bread"
   REFERENCE SUMMARY: This video presents 18 essential sourdough basics covering starter management, flour selection, hydration levels, fermentation techniques, shaping, cold proofing, and baking. It explains concepts like fermentolyse vs autolyse, stretch-and-fold timing, bulk fermentation readiness, pre-shaping, Dutch oven baking with steam, and how to read crumb structure for troubleshooting. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

3. [h7eqwYLv2tI] The ONLY SOURDOUGH BREAD SHAPING Tutorial You Will Ever Need - 8 min
   Curriculum's reason: A dedicated demo of shaping with surface tension, including banneton prep with rice flour and a simple beginner roll-and-pull method. Shaping is hard to learn from a fast bake-along, so this adds a closer look from the same baker without changing methods.
   Quote [01:25]: "you're trying to pull your dough together to create a lot of tension this tension will later on result in oven spring"
   Quote [00:20]: "rice flour is advised it's going to absorb a lot more humidity so sprinkle your banneton with a little bit of rice flour"
   REFERENCE SUMMARY: This video demonstrates two shaping techniques for sourdough loaves: a simpler beginner method and a more advanced technique using stitching. Both methods focus on creating surface tension by pulling and rolling the dough, preparing it for placement in a banneton for final proof before baking. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

4. [02WlZa_N-vI] What creates the BEST OPEN CRUMB? Cold proofing or Room temperature? - 17 min
   Curriculum's reason: Shows pre-shaping, the finger poke test, and baking with the lid on in a Dutch oven for steam, then compares a cold-retarded loaf with a room-temperature one. This gives the cold retard and scoring detail the course covers only briefly. It is the same baker, so there are no contradictions.
   Quote [04:31]: "letting this one sit at room temperature until it passes the finger poke test"
   Quote [08:52]: "baking now for 25 minutes at 230 degrees celsius lid covered so that there's a lot of steam"
   REFERENCE SUMMARY: This video experiments with proofing methods for sourdough by baking two identical loaves—one proofed at room temperature and one cold-retarded in the fridge overnight—to determine which produces better open crumb. The baker demonstrates pre-shaping, shaping techniques, the finger poke test for readiness, Dutch oven baking with scoring, and compares the final crumb structure and oven spring of both methods. Builds: Two sourdough loaves baked side-by-side using different proofing methods (room temperature vs. cold retard). Level: intermediate. Format: project_build. Language: en.

5. [5ZvYuz6mDRs] 10 Mistakes Beginner Sourdough Bakers Make - 23 min
   Curriculum's reason: Walks through ten beginner mistakes, including bulk fermentation errors, weak shaping, scoring and oven temperature, and says to skip the cold ferment only at the cost of flavor. It is the second baker and is used only for troubleshooting, not as a second recipe. It addresses the steps beginners get wrong.
   Quote [03:57]: "Bulk fermentation is probably the hardest step for most new bakers, and it's honestly just takes a little bit of time and understanding how your dough should feel"
   Quote [08:59]: "Shaping isn't about making your dough pretty. It's about giving it the structure to spring up in the oven instead of spreading out flat"
   REFERENCE SUMMARY: This video identifies and explains 10 common mistakes beginner sourdough bakers make, including over-complicated scoring, bulk fermentation errors, unhealthy starters, poor shaping, wrong oven temperature, using fancy grains, skipping cold ferment, insufficient dough development, and improper starter maintenance. The presenter demonstrates proper techniques for scoring, shaping with a letter-fold method, identifying proper bulk fermentation doneness, and maintaining a healthy starter. Level: beginner. Format: concept_explainer. Language: en.

Considered and dropped:
- Bake the Perfect Sourdough Bread: A Step-by-Step Guide: A good short bake-along, but it comes from a third creator and the learner allows at most two bakers; the course already covers the same topics in more depth.
- YOUR FIRST SOURDOUGH (Sourdough Bread For Complete Beginners): A strong beginner bake-along, but it has no cold retard, which the learner wants, and it would add a third creator.
- The Complete Beginners Guide to Baking Perfect Sourdough: The same channel as the mistakes pick, but a second full recipe (autolyse, aggressive mixing) would contradict the primary method.
- How to Bake Your First Sourdough (In Just 7 Steps): A solid bake-along, but a second full recipe would duplicate the primary one and conflict with it.
- How to Know When Sourdough Bulk Fermentation Is Done (5 Signs): 33 minutes on bulk fermentation signs is too long for the budget and mostly repeats what the course and the mistakes video cover. Its segment map is also inconsistent.
- 140: How to Calculate SOURDOUGH Hydration - Bake with Jack: The hydration formula is useful but it is a third creator, and the main course already covers hydration.
- Sourdough bread Troubleshooting beginner Mistakes: A good troubleshooting video, but it is a third creator and carries a surface_intro flag, while an unflagged mistakes video exists.
- Stop Over Proofing Your Sourdough, Use This Experiment to Find Your Optimum Proof: Flagged too_advanced_for_learner (an experiment on proofing windows).
- Are You Doing Cold Fermentation Wrong? | The 3-Hour Method for Bread and Pizza: Pure theory on the science of cold fermentation, off-topic for a first sourdough loaf, and flagged off_topic.

### sourdough_first_loaf / S4

Planned viewing time: 74 of 120 min.
Assumptions stated: The 'weekend' bake means mixing Friday/Saturday, a cold retard overnight, and baking the next day, so a 1-2 day timeline is acceptable.; The learner owns or can get a Dutch oven, a kitchen scale, and a banneton or a bowl with a towel.; The learner wants a standard country-style white or lightly whole-wheat boule at around 70-75% hydration, not an advanced high-hydration loaf.; Since 'at most two bakers' methods' is required, the plan favors one primary full bake-along baker plus one optional secondary for troubleshooting.
Warnings to the learner: The pool had no verified quotes, so every pick rests on titles, summaries and metadata rather than checked transcript evidence. Confidence is correspondingly modest. | Time used is about 74 of 120 minutes (62%). Roughly 46 minutes are unused because the remaining videos were third-party, redundant, unverifiable or off-level. Padding them in would have broken your two-baker limit or added weak material. | Only two bakers are used: The Bread Code (main course, shaping, mistakes) and Grant Bakes (cold-proof and bake test). If their timings or hydration differ, follow The Bread Code for the bake and use Grant Bakes only for the cold-proof decision. | The beginner-mistakes cluster (GLSjBbIcUKo, BJEHsvW2J6M, 5ZvYuz6mDRs, ACipczTnezM) was entirely from other creators, so none was picked. The Bread Code '18 basics' video stands in for this topic.

1. [msqU-ylXWUs] Your First Sourdough Bread (FULL COURSE in 30 minutes) - 31 min
   Curriculum's reason: A roughly 30-minute beginner full course from The Bread Code that is described as explaining the why behind each step. It is the only full-length beginner bake-along in the pool with a manual transcript, so it is the spine of the plan and fixes your first baker.
   REFERENCE SUMMARY: A comprehensive beginner sourdough bake-along that guides you through the complete process from levain preparation through baking, with explanations of hydration, bulk fermentation with stretch-and-folds, shaping, cold retard, and Dutch oven baking techniques. The instructor emphasizes understanding the why behind each step and covers common beginner mistakes. Builds: A complete sourdough boule with proper oven spring, crisp crust, and open crumb structure. Level: beginner. Format: full_course. Language: en.

2. [Koab3fxN4t4] The Last PRESHAPING SOURDOUGH Tutorial You Ever Need - 4 min
   Curriculum's reason: Isolates pre-shaping after bulk, with tricks for controlling the dough and building surface tension. It is the same baker as the main course, so the method stays consistent.
   REFERENCE SUMMARY: Hendrik from The Bread Code demonstrates the pre-shaping technique for sourdough after bulk fermentation, showing how to divide dough in half and shape it into a round with proper surface tension using minimal flour and controlled hand movements. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

3. [h7eqwYLv2tI] The ONLY SOURDOUGH BREAD SHAPING Tutorial You Will Ever Need - 8 min
   Curriculum's reason: A shaping tutorial from the same baker, covering beginner and more advanced methods for forming loaves with surface tension. It follows pre-shaping, so you can practise the final boule shape.
   REFERENCE SUMMARY: This video demonstrates two shaping techniques for sourdough loaves: a simpler beginner method and a more advanced technique using stitching. Both methods focus on creating surface tension by pulling and rolling the dough, preparing it for placement in a banneton for final proof before baking. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

4. [TDrc82KTeig] Let cold-proofed sourdough come up to room temperature before baking? - 9 min
   Curriculum's reason: A side-by-side bake of cold-proofed dough straight from the fridge versus after a rest at room temperature, showing oven spring. It fills the cold retard gap, which the main course is not confirmed to cover in depth. Grant Bakes is the second and last baker.
   REFERENCE SUMMARY: Grant Bakes compares baking cold-proofed sourdough directly from the fridge versus letting it warm to room temperature first. Both methods produce acceptable loaves, but the room-temperature dough develops better oven spring, ear definition, and a more open crumb structure, though it takes 4+ hours to warm up and requires careful handling in the banneton. Builds: Two identical sourdough loaves baked using different methods: one cold from fridge, one warmed to room temperature. Level: beginner. Format: project_build. Language: en. Flags: surface_intro.

5. [9fWzWpL5g6w] 18 Sourdough Basics YOU Should Know - 22 min
   Curriculum's reason: Covers 18 sourdough basics including starter care, technique and common mistakes, across every stage you are learning. It comes from The Bread Code, so you get mistake-avoidance without adding a third baker. The surface_intro flag is acceptable because you asked for the beginner-mistakes overview.
   REFERENCE SUMMARY: This video presents 18 essential sourdough basics covering starter management, flour selection, hydration levels, fermentation techniques, shaping, cold proofing, and baking. It explains concepts like fermentolyse vs autolyse, stretch-and-fold timing, bulk fermentation readiness, pre-shaping, Dutch oven baking with steam, and how to read crumb structure for troubleshooting. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

Considered and dropped:
- YOUR FIRST SOURDOUGH (Sourdough Bread For Complete Beginners): The best-rated full beginner bake-along (lower hydration), but it shows no cold retard, scoring or Dutch oven content and would force a third baker once cold-proof and mistakes videos are added.
- The BEST Beginner Sourdough Bread Tutorial on YouTube: A Grant Bakes beginner recipe tutorial with no usable transcript and no verified content. It duplicates the main course, and a second full recipe would add contradictory methods.
- 10 Mistakes Beginner Sourdough Bakers Make: Strongest mistakes video (manual transcript, rated 2) but from Keep it Sweet Kitchen, which would be a third baker and break your limit of two. It is also in the near-duplicate cluster.
- How to Bake Your First Sourdough (In Just 7 Steps): A 28.7-minute '7 steps' course that is probably relevant, but the transcript is unusable, so nothing can be verified, and it is a third creator.
- How to Know When Sourdough Bulk Fermentation Is Done (5 Signs): 33 minutes on bulk fermentation signs only. Pure theory flagged, third creator, and too long for one sub-topic.
- How to Shape a SOURDOUGH BOULE | Sourdough Shaping Techniques: A good short boule demonstration, but the shaping slot is already filled by The Bread Code and a second shaping method would add contradictions.
- Sourdough. Almost over fermented dough, plus 42 hour cold retard, turned out OK.: A vlog of one accidental over-ferment, which you ruled out, and it is not systematic teaching.
- 140: How to Calculate SOURDOUGH Hydration - Bake with Jack: A hydration calculation lesson that is pure theory, from a third baker. Hydration is covered in the main course.
- What creates the BEST OPEN CRUMB? Cold proofing or Room temperature?: An experimental cold versus room-temperature crumb comparison. Intermediate level and flagged off_topic and pure_theory, so it is not a beginner cold-retard guide.
- Bake the Perfect Sourdough Bread: A Step-by-Step Guide: Possibly a bake-along, but no transcript is available to verify it, and it would add a third baker.

## weekend_react_dev

```
Goal: Build a small React app this weekend, something like a habit tracker with local storage
Time budget: 360 minutes
Background: Python backend engineer, 5 years experience
Already knows: JavaScript fundamentals, HTTP, REST, JSON, Git, npm
Does not know yet: React, JSX, Vite tooling, React hooks, Component patterns
Constraints: I prefer project-based content. Avoid pure-theory lectures and 'in 100 seconds' surface intros. Nothing made before 2022 (I want Vite and modern hooks, not create-react-app). At most two videos from any one creator.
```

### weekend_react_dev / S1

Planned viewing time: 185 of 360 min.
Assumptions stated: The habit tracker is a variation of the to-do and favorites apps in the videos: habits are items you add, toggle done and delete, with daily check-offs added on your own.; JavaScript with JSX is fine. Some videos use TypeScript, which you can ignore.; I could not see upload dates. I picked videos that show Vite and hooks, and left out the one flagged outdated_tooling.
Warnings to the learner: Only about 185 of the 360 minutes are used. The remaining time is for building your own habit tracker, which is the real test. I did not pad with weak or redundant videos. | No video builds an actual habit tracker. The to-do and favorites builds are the closest, and you will need to add the daily check-off and streak logic yourself. | Dropped Mosh's React tutorial: it is lecture-style with TypeScript, and the Tech With Tim project covers the same basics. | Dropped Dawid's Todo App: it is flagged outdated_tooling, and the other project builds cover the same ground.

1. [do62-z3z6FM] Vite Crash Course – Frontend Build Tool - 40 min
   Curriculum's reason: Covers Vite scaffolding, project structure, hot module replacement and production builds, which are the tooling gaps you named. The boilerplate it builds is a React app, so it gets you set up for the weekend.
   Quote [00:00]: "Vit is a next generation build tool that offers instant project startup and real-time updates"
   Quote [02:04]: "We learned how to build React apps with Vit, how to work with static assets, using environment variables, TypeScript"
   REFERENCE SUMMARY: A comprehensive Vite crash course that teaches how to set up and configure Vite for React development, covering project scaffolding, hot module replacement, static asset handling, environment variables, TypeScript integration, production builds, and plugin extensions. Builds: React app with boilerplate counter component, header footer components, static asset optimization, environment variables integration, and production build setup. Level: beginner. Format: crash_course. Language: en.

2. [V9i3cGD-mts] Learn React Hooks: useState - Simply Explained! - 8 min
   Curriculum's reason: A short, focused explanation of useState (state as data that changes over time, destructuring, setters in event handlers). It prepares you for the project builds.
   Quote [00:20]: "state the simplest way that you can think about this is data that changes with time"
   Quote [02:07]: "useState is the hook that you use in React to manipulate state"
   REFERENCE SUMMARY: This video teaches useState, one of the fundamental React hooks for managing state in functional components. Through a simple counter application example with increment and decrement buttons, the instructor explains what state is, how to destructure useState to get a state variable and updater function, how to set default values, and how to update state through event handlers. Level: beginner. Format: concept_explainer. Language: en.

3. [G6D9cBaLViA] Learn React With This ONE Project - 100 min
   Curriculum's reason: A project build that teaches components, JSX, useState, useEffect, lists, conditional rendering, context and localStorage-backed favorites. The favorites add/remove logic maps closely onto habit management.
   Quote [03:37]: "Everything revolves around something called a component. Now a component is really just a part of your application"
   Quote [12:55]: "JSX simply means kind of a combination of JavaScript and HTML. And you'll see that we have some things that look like HTML"
   REFERENCE SUMMARY: Learn React by building a movie search app with real-world API integration. The video covers JSX, components, state management with useState, conditional rendering, routing, API calls with async/await, localStorage integration through React Context, and complete project implementation from setup to favorites page. Builds: Movie search and favorites app with API integration, search functionality, favorites list management, and navigation between home and favorites pages. Level: beginner. Format: project_build. Language: en.

4. [1uiNxQIpcLU] React Custom Hooks: useLocalStorage - Simply Explained! - 10 min
   Curriculum's reason: Builds a reusable useLocalStorage custom hook with JSON serialization and try/catch. This is the component pattern to use for habit persistence.
   Quote [00:21]: "we are going to create a hook called use local storage that is going to expose to us three different functions"
   Quote [03:13]: "window local storage set item we're going to give it the key that we have here and then we're going to do json stringify"
   REFERENCE SUMMARY: This video teaches how to build a custom React hook called useLocalStorage that wraps the browser's localStorage API. The hook exposes three functions (setItem, getItem, removeItem) with error handling via try-catch blocks, and demonstrates the hook in a simple app with input and buttons. Builds: A simple app with a text input and three buttons (set, get, remove) that use a custom useLocalStorage hook to interact with browser localStorage. Level: intermediate. Format: project_build. Language: en.

5. [X92kk5iT8CM] Build a Complete To-Do List App with React + Vite | Dashboard, Reminders & Local Storage Tutorial - 27 min
   Curriculum's reason: A Vite + React to-do build with add, edit and delete, a stats dashboard and local storage. It is the closest match to the habit tracker and works as a template for your own build.
   Quote [00:00]: "we are going to build a to-do list app using React plus white"
   Quote [00:00]: "we have a dashboard for showing our total task completed task pending task and overdue"
   REFERENCE SUMMARY: A comprehensive tutorial building a complete to-do list application using React and Vite with Tailwind CSS. The app includes features like task management (add, edit, delete), priority levels, due dates, reminders, local storage persistence, and a dashboard with statistics for total, pending, completed, and overdue tasks. Builds: TaskMaster to-do list app with task management, priority levels, due dates, reminders, local storage, and dashboard with statistics. Level: beginner. Format: project_build. Language: en.

### weekend_react_dev / S2

Planned viewing time: 105 of 360 min.
Assumptions stated: Habit tracker means: add/delete habits, mark them complete per day, view streaks, with data persisted in localStorage; The 360 minutes is pure watching time, so a long project build video can serve as the backbone; Plain JavaScript (not TypeScript) is fine since the learner knows JS fundamentals but did not mention TypeScript; Modern function components and hooks only; class components are not needed; The 'nothing before 2022' constraint is handled by the later video-selection step using upload dates; the exclusions here cover title-based filters only
Warnings to the learner: Budget use is about 105 of 360 minutes (29%). About 255 minutes are unused because the remaining candidates were flagged, unverifiable (poor transcripts), pre-2022, off-stack (Redux/Next.js/TypeScript) or redundant. I chose to under-fill rather than pad with weak videos. | None of the cards had verified quotes, so evidence_quote_ids are empty and all confidence values are moderate. The picks rest on summaries, topics and segment maps only. | No candidate teaches habit-specific streak logic or per-day completion tracking. You will need to write the streak calculation yourself, using the todo builds' list and toggle patterns plus plain JavaScript date handling. | Component patterns are only partly covered. Lists/keys and composition come from the build videos, and custom hooks from the short hook video. Lifting state up is covered only implicitly in the builds, and no video teaches it explicitly.

1. [X92kk5iT8CM] Build a Complete To-Do List App with React + Vite | Dashboard, Reminders & Local Storage Tutorial - 27 min
   Curriculum's reason: A short, project-based React + Vite build with no red flags. Per its summary and segment map it goes from Vite setup through JSX components, useState and event handling to useEffect + localStorage, and it also covers lists/keys. That gives a Python engineer a fast first pass through the whole stack on a small app.
   REFERENCE SUMMARY: A comprehensive tutorial building a complete to-do list application using React and Vite with Tailwind CSS. The app includes features like task management (add, edit, delete), priority levels, due dates, reminders, local storage persistence, and a dashboard with statistics for total, pending, completed, and overdue tasks. Builds: TaskMaster to-do list app with task management, priority levels, due dates, reminders, local storage, and dashboard with statistics. Level: beginner. Format: project_build. Language: en.

2. [QdTHUv79EZc] Build a Todo App with React.js | Beginner React Project using hooks - 62 min
   Curriculum's reason: A full hour-long build of a hooks-based todo app (useState, useEffect, localStorage, CSS animations) that is almost the same shape as a habit tracker (add/delete/toggle items, persisted). It is the project backbone, and you can adapt its list and toggle logic to habits and days. The card is unflagged and project-based.
   REFERENCE SUMMARY: Build a fully functional todo app with React using hooks (useState, useEffect) and localStorage persistence. The tutorial covers HTML structure, CSS styling with animations, checkbox customization, task management (add, delete, rename, mark complete), dynamic messaging, and a task counter with visual feedback. Builds: Todo app with task creation, completion toggling, deletion, renaming, localStorage persistence, animated checkboxes, and dynamic progress counter. Level: beginner. Format: project_build. Language: en. Flags: outdated_tooling.

3. [wKjsnUIfGHI] ReactJS Tutorial 81: Creating Our Own useLocalStorage Hook In ReactJS - 16 min
   Curriculum's reason: Builds a custom useLocalStorage hook that combines useState and useEffect. This is the custom-hook pattern the learner needs and the two project builds don't clearly teach. Use it to refactor the habit tracker's persistence into a reusable hook.
   REFERENCE SUMMARY: This tutorial teaches how to create a custom useLocalStorage React hook that persists user data to the browser's local storage. The video covers browser storage fundamentals, builds a reusable hook with set and get functions, and demonstrates its use in a login component with useState and event handling. Builds: Custom useLocalStorage hook with a login form that persists username to browser local storage. Level: intermediate. Format: project_build. Language: en.

Considered and dropped:
- Learn React With This ONE Project: Poor transcript, and the summary describes an API-fetching project. It cannot be verified to cover Vite, hooks or localStorage, so it is too risky to spend 100 minutes on.
- React Tutorial for Beginners: A lecture-format TypeScript course with an unusable transcript. It does not match the preference for project-based content and plain JS, and its coverage can't be confirmed.
- Functional Components & Props & useState Hook: A 53-minute pure-theory concept explainer on components, props and useState. Unflagged project builds already cover those sub-topics, and the learner wants to avoid pure theory.
- React JS Tutorial for Beginners | Setup React with Vite & Understand Project Structure: Covers only Vite setup and project structure in 63 minutes. It has a poor transcript and no project, and the X92 build covers setup in far less time.
- Understand Any React Project in 16 Minutes | Vite + React + TypeScript Folder Structure Explained: A TypeScript folder-structure explainer flagged surface_intro and pure_theory. The learner uses plain JS, and X92 covers project setup inside a real build.
- Vite Crash Course – Frontend Build Tool: A 40-minute Vite config and tooling crash course flagged pure_theory and surface_intro. It goes deeper into build-tool configuration than a weekend React app needs.
- React Custom Hooks: useLocalStorage - Simply Explained!: Also a useLocalStorage hook explainer, but flagged surface_intro and pure_theory. It overlaps with the chosen custom-hook video, which also combines useState and useEffect.
- A Habit Tracker App Using React Redux: A habit tracker, but built with Redux and Bootstrap, with a poor transcript and only 5.6 minutes. Redux is outside the learner's plan.
- localStorage + Sign-in Frontend: Building a Habit Tracker with React/Redux/Express Part 9: Uploaded in 2021, which violates the 2022 date floor. It is also a Redux/Express sign-in part, not a standalone habit tracker.
- Every React Concept Explained in 12 Minutes: A 12-minute surface overview of every React concept, flagged surface_intro. The learner explicitly wants no shallow intros.

### weekend_react_dev / S3

Planned viewing time: 189 of 360 min.
Assumptions stated: Habit tracker means: add/delete habits, mark them complete per day, view streaks, with data persisted in localStorage; The 360 minutes is pure watching time, so a long project build video can serve as the backbone; Plain JavaScript (not TypeScript) is fine since the learner knows JS fundamentals but did not mention TypeScript; Modern function components and hooks only; class components are not needed; The 'nothing before 2022' constraint is handled by the later video-selection step using upload dates; the exclusions here cover title-based filters only
Warnings to the learner: The picks total about 189 of 360 minutes (about 52%), leaving about 171 minutes unused. The remaining candidates are flagged for conflicts with your constraints (create-react-app, pure-theory or surface-intro) or only repeat topics already covered, and I preferred under-filling to padding. | No candidate teaches habit streak logic, such as consecutive-day calculation, so you will need to write that yourself; sub-topic polish_deploy is only partly covered. | No video here covers lifting state up in depth. You get it only implicitly through the project builds and the Context API. | Tech With Tim's project fetches a movie API and uses react-router, which a habit tracker doesn't need. Focus on the useState, useEffect and Context/localStorage sections.

1. [do62-z3z6FM] Vite Crash Course – Frontend Build Tool - 18 min (watch 02:45-21:04)
   Curriculum's reason: Covers scaffolding a React project with npm create vite, the dev server and hot module replacement, and creating components, which is the Vite tooling you haven't used. Only the setup-to-useEffect part is needed, so you skip the TypeScript config and the Vite internals talk.
   Quote [00:00]: "Vit is a next generation build tool that offers instant project startup and real-time updates"
   Quote [02:04]: "We learned how to build React apps with Vit, how to work with static assets, using environment variables, TypeScript"
   REFERENCE SUMMARY: A comprehensive Vite crash course that teaches how to set up and configure Vite for React development, covering project scaffolding, hot module replacement, static asset handling, environment variables, TypeScript integration, production builds, and plugin extensions. Builds: React app with boilerplate counter component, header footer components, static asset optimization, environment variables integration, and production build setup. Level: beginner. Format: crash_course. Language: en.

2. [G6D9cBaLViA] Learn React With This ONE Project - 100 min
   Curriculum's reason: A project-based Vite build that teaches JSX, components and props, useState re-rendering, mapping lists, useEffect, and React Context with localStorage persistence for a favorites list. That list is structurally close to tracking habits. It is the main backbone for the core concepts.
   Quote [12:55]: "JSX simply means kind of a combination of JavaScript and HTML. And you'll see that we have some things that look like HTML"
   Quote [46:53]: "When a state change occurs, the entire component is reran or rerendered. So if we just define something as a normal variable"
   REFERENCE SUMMARY: Learn React by building a movie search app with real-world API integration. The video covers JSX, components, state management with useState, conditional rendering, routing, API calls with async/await, localStorage integration through React Context, and complete project implementation from setup to favorites page. Builds: Movie search and favorites app with API integration, search functionality, favorites list management, and navigation between home and favorites pages. Level: beginner. Format: project_build. Language: en.

3. [5uHikv1oBEI] LocalStorage in React Using Custom Hook | The Complete React Course | Ep.41 - 44 min
   Curriculum's reason: Builds a reusable useLocalStorage custom hook in an expense tracker and swaps useState for it across several form fields. It also fixes an infinite render loop with useEffect. This is the custom-hook pattern you will need to persist habits.
   Quote [01:50]: "we will make a custom hook of react name it useLocalStorage and with that hook we will implement local storage"
   Quote [29:40]: "we have made custom hook, we just changed use state to use local storage and the local storage need a key"
   REFERENCE SUMMARY: This video teaches how to build a custom `useLocalStorage` hook to persist state across page refreshes in a React expense tracker application. The instructor demonstrates implementing localStorage with the custom hook for various form fields, handling edge cases like function values, and shows the hook working in practice as users add and edit expenses. Builds: Expense tracker with localStorage persistence using custom useLocalStorage hook. Level: intermediate. Format: project_build. Language: en.

4. [X92kk5iT8CM] Build a Complete To-Do List App with React + Vite | Dashboard, Reminders & Local Storage Tutorial - 27 min
   Curriculum's reason: A complete React + Vite to-do app with add, edit and delete, completion state, localStorage persistence and a statistics dashboard. It is the closest modern end-to-end analogue to a habit tracker, and its Tailwind styling covers the finishing touches. Watch it after the concepts so you can adapt it to habits.
   Quote [00:00]: "we have a dashboard for showing our total task completed task pending task and overdue"
   Quote [20:26]: "use local storage so I'll copy this and I'll paste this"
   REFERENCE SUMMARY: A comprehensive tutorial building a complete to-do list application using React and Vite with Tailwind CSS. The app includes features like task management (add, edit, delete), priority levels, due dates, reminders, local storage persistence, and a dashboard with statistics for total, pending, completed, and overdue tasks. Builds: TaskMaster to-do list app with task management, priority levels, due dates, reminders, local storage, and dashboard with statistics. Level: beginner. Format: project_build. Language: en.

Considered and dropped:
- Build a Todo App with React.js | Beginner React Project using hooks: Strong todo build with useState, useEffect and localStorage, but it is set up with create-react-app (flagged outdated_tooling), which you ruled out. Unflagged Vite builds cover the same sub-topics.
- React Tutorial for Beginners: A long TypeScript lecture flagged pure_theory built around a ListGroup demo, not a project. Plain-JS project builds already cover props, lists and state.
- React Tutorial & Vite in 2025: Your First Project From Scratch! (The Easy Way): Vite setup walkthrough flagged surface_intro. The Vite crash course covers the same setup more deeply.
- Learn React Hooks: useState - Simply Explained!: Good useState counter explainer, but it overlaps with the useState coverage in the Tech With Tim build and adds a short isolated demo.
- ReactJS Tutorial 81: Creating Our Own useLocalStorage Hook In ReactJS: A useLocalStorage hook on a login form that covers the same ground as the expense-tracker hook video, with a less relevant example.
- Learn How to Use Local Storage in React With an Easy-to-Understand Example: Flagged surface_intro; it shows a counter plus a library hook, and the hook video builds the same idea from scratch.
- Understand Any React Project in 16 Minutes | Vite + React + TypeScript Folder Structure Explained: A TypeScript folder-structure explainer flagged pure_theory; it is not project-based and the Vite coverage is already sufficient.
- React JS Tutorial for Beginners | Setup React with Vite & Understand Project Structure: A 63-minute lecture flagged pure_theory covering Virtual DOM theory and Vite setup, which conflicts with your preference for project-based content.
- A Habit Tracker App Using React Redux: A habit tracker demo built on Redux, flagged too_advanced_for_learner. It is a short walkthrough, not a build-along tutorial.
- Functional Components & Props & useState Hook: A pure-theory CodeSandbox lecture on components, props and useState, dated 2022; redundant with the project builds.

### weekend_react_dev / S4

Planned viewing time: 359 of 360 min.

1. [SqcY0GlETPk] React Tutorial for Beginners - 80 min
   Curriculum's reason: Popular result (6,298,159 views) for 'React project tutorial for experienced developers Vite'.
   REFERENCE SUMMARY: This is a beginner-friendly React tutorial that covers core concepts including components, JSX, state management with useState, props, event handling, conditional rendering, and lists. The instructor builds a ListGroup component throughout the course, demonstrating how to create interactive UI elements with React 18 and TypeScript. Level: beginner. Format: lecture. Language: en. Flags: pure_theory.

2. [wIyHSOugGGw] Every React Concept Explained in 12 Minutes - 12 min
   Curriculum's reason: Popular result (1,938,402 views) for 'React useState and props explained by building a project'.
   REFERENCE SUMMARY: A rapid overview of core React concepts including components, JSX, props, state, hooks, effects, and advanced features like context and error boundaries. Covers the fundamentals needed to build React applications, with brief explanations of each concept but minimal hands-on coding. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

3. [G6D9cBaLViA] Learn React With This ONE Project - 100 min
   Curriculum's reason: Popular result (1,050,027 views) for 'React project tutorial for experienced developers Vite'.
   REFERENCE SUMMARY: Learn React by building a movie search app with real-world API integration. The video covers JSX, components, state management with useState, conditional rendering, routing, API calls with async/await, localStorage integration through React Context, and complete project implementation from setup to favorites page. Builds: Movie search and favorites app with API integration, search functionality, favorites list management, and navigation between home and favorites pages. Level: beginner. Format: project_build. Language: en.

4. [uvEAvxWvwOs] PROPS in React explained 📧 - 12 min
   Curriculum's reason: Popular result (246,236 views) for 'React useState and props explained by building a project'.
   REFERENCE SUMMARY: This video explains React props: how parent components pass data to child components using key-value pairs. It demonstrates creating a Student component that accepts props (name, age, isStudent), shows how to use PropTypes for type checking, and covers defaultProps for fallback values. Level: beginner. Format: concept_explainer. Language: en. Flags: pure_theory.

5. [V9i3cGD-mts] Learn React Hooks: useState - Simply Explained! - 8 min
   Curriculum's reason: Popular result (162,798 views) for 'React useState and props explained by building a project'.
   REFERENCE SUMMARY: This video teaches useState, one of the fundamental React hooks for managing state in functional components. Through a simple counter application example with increment and decrement buttons, the instructor explains what state is, how to destructure useState to get a state variable and updater function, how to set default values, and how to update state through event handlers. Level: beginner. Format: concept_explainer. Language: en.

6. [do62-z3z6FM] Vite Crash Course – Frontend Build Tool - 40 min
   Curriculum's reason: Popular result (103,225 views) for 'React project tutorial for experienced developers Vite'.
   REFERENCE SUMMARY: A comprehensive Vite crash course that teaches how to set up and configure Vite for React development, covering project scaffolding, hot module replacement, static asset handling, environment variables, TypeScript integration, production builds, and plugin extensions. Builds: React app with boilerplate counter component, header footer components, static asset optimization, environment variables integration, and production build setup. Level: beginner. Format: crash_course. Language: en.

7. [VZ6Qpe3sjhM] How to Set Up React in 2025 | Install React with Vite in 2 minutes - 2 min
   Curriculum's reason: Popular result (47,382 views) for 'Vite React setup and project structure walkthrough'.
   REFERENCE SUMMARY: Step-by-step walkthrough of setting up a new React project using Vite in 2025. Covers installing Node.js, running npm create vite, selecting React and JavaScript, installing dependencies, and starting the development server. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

8. [V1PxgjIhTw0] React Explained in 8 Minutes - 8 min
   Curriculum's reason: Popular result (43,130 views) for 'React project tutorial for experienced developers Vite'.
   REFERENCE SUMMARY: This video explains core React concepts including declarative programming, components, JSX, props, state with useState, and Vite setup. It demonstrates building a simple counter app to show how state changes trigger re-renders, and covers the key differences between React's declarative approach and imperative vanilla JavaScript. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro, pure_theory.

9. [1uiNxQIpcLU] React Custom Hooks: useLocalStorage - Simply Explained! - 10 min
   Curriculum's reason: Popular result (35,159 views) for 'React custom hook useLocalStorage tutorial'.
   REFERENCE SUMMARY: This video teaches how to build a custom React hook called useLocalStorage that wraps the browser's localStorage API. The hook exposes three functions (setItem, getItem, removeItem) with error handling via try-catch blocks, and demonstrates the hook in a simple app with input and buttons. Builds: A simple app with a text input and three buttons (set, get, remove) that use a custom useLocalStorage hook to interact with browser localStorage. Level: intermediate. Format: project_build. Language: en.

10. [QdTHUv79EZc] Build a Todo App with React.js | Beginner React Project using hooks - 62 min
   Curriculum's reason: Popular result (29,737 views) for 'React project tutorial build a todo app with hooks and localStorage step by step'.
   REFERENCE SUMMARY: Build a fully functional todo app with React using hooks (useState, useEffect) and localStorage persistence. The tutorial covers HTML structure, CSS styling with animations, checkbox customization, task management (add, delete, rename, mark complete), dynamic messaging, and a task counter with visual feedback. Builds: Todo app with task creation, completion toggling, deletion, renaming, localStorage persistence, animated checkboxes, and dynamic progress counter. Level: beginner. Format: project_build. Language: en. Flags: outdated_tooling.

11. [N7rs5F4f6FA] Learn How to Use Local Storage in React With an Easy-to-Understand Example - 9 min
   Curriculum's reason: Popular result (11,506 views) for 'React useEffect localStorage tutorial build app'.
   REFERENCE SUMMARY: This video demonstrates how to persist React state to localStorage in two ways: first by manually using localStorage.setItem with useEffect and handling type conversions, then by simplifying the approach with a custom hook from the usehooks-ts library. The example builds a counter app that maintains its state across page refreshes. Level: beginner. Format: concept_explainer. Language: en. Flags: surface_intro.

12. [8bsG5Xg9PaI] #76 - useLocalStorage Custom Hook in React js | React Hooks Tutorial in Hindi - 8 min
   Curriculum's reason: Popular result (2,592 views) for 'React custom hook useLocalStorage tutorial'.
   REFERENCE SUMMARY: This video teaches how to create a custom useLocalStorage hook in React that persists form input values across page refreshes. The instructor builds a functional component that uses useEffect to save values to localStorage via JSON.stringify, and retrieves them on mount using JSON.parse, demonstrating the complete implementation with a working example. Level: intermediate. Format: concept_explainer. Language: en. Flags: pure_theory.

13. [b6dnwttsdTo] Learn React Custom Hooks in 7 minutes | Create useFetch hook - 7 min
   Curriculum's reason: Popular result (1,959 views) for 'React custom hook useLocalStorage tutorial'.
   REFERENCE SUMMARY: This video teaches how to create a custom React hook called useFetch to avoid repeating fetch logic across components. It demonstrates extracting duplicate state management and useEffect code from two similar components into a reusable custom hook that accepts a URL and initial data, then shows how to use the hook in both components. Builds: A custom useFetch hook for fetching random user and address data from APIs. Level: intermediate. Format: project_build. Language: en. Flags: outdated_tooling.
