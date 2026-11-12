# Curriculum: Get better at design

**Budget:** 180 min · **Planned:** 137 min · **Videos:** 11 · **Candidates assessed:** 33

**How I read the goal:** A frontend developer comes away able to make their own UIs look noticeably more polished by applying core visual design principles (hierarchy, spacing, typography, color) and by critiquing and redesigning real interfaces.

**Assumptions:** 'Design' means UI/visual design for web apps, not graphic design, UX research, or brand design; The learner wants to improve the look of interfaces they build in code, so developer-oriented design content fits best; Because they know CSS, layout mechanics are skipped and the focus is on design decisions; 'Nothing older than 2020' means videos published in 2020 or later; No design tool such as Figma is assumed; tool basics are included only as far as needed to follow redesigns
> ⚠️ About 136.6 of 180 minutes are used (about 76%). The remaining ~43 minutes are unused because the other candidates were redundant, theory-only or tied to Figma, and I preferred under-filling to padding.
> ⚠️ Border radius, icons and borders get only light coverage, mainly inside wcZ6jSlZqDc and vvPklRN0Tco. No strong dedicated video exists in the pool.
> ⚠️ Several cards have segment maps longer than the listed minutes (e.g. LfkDiDyn6nU, MlsV3hu84as). I counted the listed minutes and used segment-map timestamps for partial ranges, so check the Design Pilot and Flux ranges when you watch.
> ⚠️ The Design Pilot redesign is a Figma walkthrough, and no code-based full redesign is in the pool. I assumed you can follow along without learning Figma.
> ⚠️ This is the one creator-heavy segment: three videos are by Sajid and two parts come from Design Pilot. All picks are dated 2020 or later.
> ⚠️ Practice by applying each lesson to one of your own React UIs, which the videos won't do for you.

## Plan

- **Visual hierarchy and layout composition** (`visual_hierarchy`): They can build any layout with Flexbox and Grid, but need to learn how to guide the eye with size, weight, contrast and emphasis.
- **Spacing, alignment and consistent spacing scales** (`spacing_alignment`): Inconsistent spacing is the most common reason developer-built UIs look amateur, and a spacing scale maps directly onto CSS variables.
- **Typography for interfaces** (`typography`): Font choice, type scale, line height and line length strongly affect polish and readability and are easy to apply in CSS.
- **Color systems, contrast and accessibility** (`color_contrast`): They need a practical way to build palettes, shades and accessible contrast rather than picking colors by guesswork.
- **Polish details: shadows, borders, radius, and icons** (`depth_details`): Small refinements make UIs feel finished, and they translate directly into CSS properties.
- **Critiquing existing UIs and spotting problems** (`ui_critique`): Learning to diagnose what is wrong with a real interface builds the design eye and satisfies the need for practical critique.
- **Full redesign of a real UI, step by step** (`redesign_walkthrough`): Watching principles applied end to end on a real interface shows how to combine them and gives a repeatable process.

## Watch in this order

### 1. [Visual Hierarchy in UI/UX — Why NOBODY can READ your DESIGNS](https://www.youtube.com/watch?v=OqAdmfRztds)
Ali Hassan · 20 min · counts 20 min · beginner, concept_explainer · covers visual_hierarchy · **confidence 0.70**

Shows how size, weight, color, spacing and position set the reading order, using pricing cards, notifications and full pages. Its 'if everything shouts the user hears nothing' framing and mistakes-to-avoid section suit a developer who can build layouts but doesn't yet make them prioritise.

> [00:00] “if everything on the screen has the same font weight and size you will be distracted about what to see first”
> [02:27] “the job of hierarchy is that if everything shouts the user hears nothing”

_Confidence note: Flagged pure_theory, but it uses concrete UI examples. The card's segment map runs longer than the listed length, so later examples may be cut off._

### 2. [4 Foundational UI Design Principles | C.R.A.P.](https://www.youtube.com/watch?v=uwNClNmekGU)
Jesse Showalter · 9 min · counts 9 min · beginner, concept_explainer · covers visual_hierarchy, spacing_alignment · **confidence 0.80**

Applies contrast, repetition, alignment and proximity step by step to redesign a bike website layout. This is the first hands-on before/after in the course and ties hierarchy to alignment and grouping.

> [00:40] “contrast it's all about organizing your design establishing hierarchy emphasizing a focal point and adding visual interest”
> [04:36] “alignment organizes and groups elements together it creates rhythm it brings order to chaos”
> [06:43] “proximity makes elements seem related like they belong together it brings understanding and meaning to multiple elements”

_Confidence note: Clear content at the right level. Segment timestamps are slightly inconsistent, so I used the full video._

### 3. [Why Your UI Designs Look Off — It's Your Spacing & Layout](https://www.youtube.com/watch?v=fImTa4daVc8)
Ali Hassan · 25 min · counts 25 min · beginner, concept_explainer · covers spacing_alignment · **confidence 0.70**

Teaches the 4/8-point spacing scale and how spacing groups elements, with before/after critiques of cards. Then builds a card with consistent spacing, which turns spacing into rules a developer can reuse as CSS tokens.

> [00:42] “Spacing doesn't just mean leaving empty space; it tells the user which elements are linked together”
> [01:46] “90 percent of looking pro is just spacing”
> [03:12] “If you are designing for mobile, you have to keep multiples of 4. Meaning 4, 8, 12, 16”

_Confidence note: The later part uses Figma and a stacked-card animation that this learner doesn't need. The spacing material is solid, and the full video is used to reach the practical build._

### 4. [The 80% of UI Design - Typography](https://www.youtube.com/watch?v=9-oefwZ6Z74)
Sajid · 12 min · counts 12 min · beginner, concept_explainer · covers typography, visual_hierarchy, spacing_alignment · **confidence 0.85**

Builds hierarchy from font size, weight, color and spacing, redesigns a social feed and a subscription list, and ends with a minimal three-size type scale. The scale and CSS-variable approach fit a React/CSS developer.

> [00:20] “there is no hierarchy and point of focus so it's tough to tell what we are looking at it's just a bunch of text”
> [02:05] “you are going to need size color and spacing to group or separate elements technically spacing falls under the law of proximity”
> [07:49] “these are all the font sizes you need to design 99% of apps and uis and if you want just these three combined with weight and color are enough”

_Confidence note: Strong match with a practical redesign. Segment map runs past the listed length, so I count the listed 12.4 minutes._

### 5. [The ULTIMATE Guide To Typography For Beginners](https://www.youtube.com/watch?v=AXpxZMRM1EY)
DesignSpo · 14 min · counts 14 min · beginner, concept_explainer · covers typography · **confidence 0.70**

Fills the gap the previous video leaves: typeface categories, line height, letter spacing and kerning, and how to turn them into a typography system with rules per text type. Gives the vocabulary for choosing and pairing fonts.

> [11:27] “building a typography system makes our whole design look clean consistent and makes creating new text sections as easy as putting together Lego pieces”
> [11:27] “the basis of our system is typographical hierarchy the idea is to create rules for each text type in our design”

_Confidence note: Flagged pure_theory, but the learner has not asked to avoid theory. It is the only video with broad coverage of font choice and spacing._

### 6. [The Easy Way to Pick UI Colors](https://www.youtube.com/watch?v=vvPklRN0Tco)
Sajid · 10 min · counts 10 min · beginner, concept_explainer · covers color_contrast, depth_details · **confidence 0.85**

Builds neutral and brand palettes with HSL and CSS variables, with light and dark themes, readable contrast, borders and highlights. It is code-friendly and ends with OKLCH.

> [00:21] “Neutral colors for background, text, borders, and a lot of other elements. the brand or primary color for main actions”
> [01:02] “You have hue or the actual color on the color wheel that goes from 0 to 360. Then the saturation, which goes from 0 to 100”
> [08:22] “OKLCH is the newer and better version of it. With the V4 update, Tailwind has also switched to OKLCH as the default color format”

_Confidence note: Clear, practical and unflagged. It focuses on palettes more than WCAG contrast ratios, which the next pick helps with._

### 7. [Steal My UI/UX Process in 2026 (Real Project Breakdown)](https://www.youtube.com/watch?v=t7cnk3aQp2c)
Agatha Richards · 9 min · counts 9 min · beginner, project_build · covers color_contrast, ui_critique, redesign_walkthrough · **confidence 0.60**

Follows a real healthcare app project: reference collection, then a bad-contrast salmon primary color fixed for accessibility, and a banner redesigned after feedback made it look unclickable. Shows contrast and critique decisions on real work, ending with a before/after.

> [01:24] “not to copy the design but to understand the structure, spacing, the UX decision and why I like specific screen more than others”
> [04:56] “the primary color was like a salmon orange and the contrast was pretty bad. Since it's a healthcare app, the accessibility is non-negotiable”

_Confidence note: Process-oriented rather than a deep color lesson, and the transcript is auto-generated. It helps fill the accessibility and real-project gap._

### 8. [The Easy Way to Fix Boring UIs](https://www.youtube.com/watch?v=wcZ6jSlZqDc)
Sajid · 9 min · counts 9 min · beginner, project_build · covers depth_details, redesign_walkthrough · **confidence 0.85**

Shows the layered-shades-plus-shadows technique, then applies it before/after to nav tabs, a profile card, radio buttons and a dashboard. Covers the polish details (shadow, depth) in redesigns that can be coded in CSS.

> [00:00] “all we need is a few shades of the same color and then layer them like this”
> [01:02] “create three to four shades of the same color and then create some shadows”
> [05:15] “The design is changed so much by just using four shades of gray and some shadow”

_Confidence note: Practical, unflagged and in code. Border radius and icons are only lightly covered. Includes a short sponsor segment._

### 9. [Complete Layout Guide](https://www.youtube.com/watch?v=MlsV3hu84as)
Flux Academy · 12 min · watch 07:40–12:00 · counts 4 min · beginner, concept_explainer · covers ui_critique · **confidence 0.55**

The final part walks through real sites (Figma, Webflow) and critiques Pantone's cluttered homepage against focal point, hierarchy and white space. Gives a repeatable checklist for spotting layout problems on a live site.

> [10:15] “if they would just go back to these very basic principles focal point hierarchy white space if they were observed pantone's value proposition would come across”

_Confidence note: The segment map is partly inconsistent (the Pantone entry is mistimed), so the range is approximate. Only the critique tail is used._

### 10. [MASTER VISUAL HIERARCHY: Principles of VISUAL DESIGN for Designing Mobile Apps!](https://www.youtube.com/watch?v=LfkDiDyn6nU)
Design Pilot · 76 min · watch 20:54–26:48 · counts 6 min · beginner, project_build · covers ui_critique · **confidence 0.60**

This part diagnoses the problems in a poorly designed flight-booking UI, such as why ticket price need not be the first data point. It models how to critique an interface against user needs before redesigning.

> [17:09] “even though ticket price is important doesn't mean that has to be the first data point right”

_Confidence note: Range is from the segment map, whose timestamps run past the listed length. Check that the critique starts around 20:54._

### 11. [MASTER VISUAL HIERARCHY: Principles of VISUAL DESIGN for Designing Mobile Apps!](https://www.youtube.com/watch?v=LfkDiDyn6nU)
Design Pilot · 76 min · watch 56:30–1:15:00 · counts 18 min · beginner, project_build · covers redesign_walkthrough, typography, spacing_alignment, color_contrast · **confidence 0.65**

The capstone: builds text styles, spacing, color sections and emphasis step by step to redesign the flight app. Applies all earlier lessons to one real UI, and the instructor concludes that a few text styles and colors give a clear interface.

> [1:14:45] “with just a few textiles and just a few colors we have been able to create a beautiful in interface that makes a lot of sense very easy for users to make a decision”

_Confidence note: Starts at the typography section and stops near the last verified quote. The remainder (spacing, color, nav bar) is cut to stay inside the budget, and the instructor works in Figma._

## Considered and dropped

- [UI/UX Website Redesign Before and After - CaterGraphix Design Academy](https://www.youtube.com/watch?v=7AhCIBGTiEA): A real redesign, but in the no-code Oxygen builder, with questionable advice ('always give a margin') and a long 44 minutes for little design theory.
- [UI / UX Design Tutorial – Wireframe, Mockup & Design in Figma](https://www.youtube.com/watch?v=c9Wg6Cb_YlU): 86 minutes, mostly iPad wireframing and Figma setup, which this learner doesn't need. It has no critique and covers spacing less clearly than the shorter picks.
- [UI/UX Design Color Theory CRASH COURSE | Color Theory For Beginners | Saptarshi Prakash](https://www.youtube.com/watch?v=l6LqaAs4hWs): Mostly pure color theory (harmonies, psychology). Its contrast and accessibility sections sit past the listed duration, and vvPklRN0Tco is more practical for a developer.
- [Every UI/UX Concept Explained in Under 10 Minutes](https://www.youtube.com/watch?v=EcbgbKtOELY): A ten-minute overview that is too shallow for this learner, flagged surface_intro, and covered more deeply by the picks.
- [Website Redesign Before & After: Built to Convert, Not Just Look Nice](https://www.youtube.com/watch?v=mRd1qsWnpik): A 3-minute before/after with a brief critique and little teaching of why the changes work, so it adds little beyond the longer redesigns.
- [Website Redesign | Before & After (EP 01)](https://www.youtube.com/watch?v=CLLObtIpDUU): A surface-level before/after tour flagged surface_intro, with no explanation of design principles. t7cnk3aQp2c and the Design Pilot parts critique more rigorously.
- [UI Typography | Full UX Design Course for Beginners by Cutting Edge School](https://www.youtube.com/watch?v=HQvOF7TK7hg): Mostly Figma text-style organisation and layer naming, which doesn't help design decisions in code.
- [Industry-Standard Shadow System | Shadow Design System Tutorial for Product & UI/UX Designers](https://www.youtube.com/watch?v=dtRGlxI0TL8): Nearly 50 minutes on Material elevation tokens in Figma. It would eat the budget and covers shadows only narrowly; wcZ6jSlZqDc covers depth practically in 9 minutes.
- [Beginning Graphic Design: Layout & Composition](https://www.youtube.com/watch?v=a5KYlHNKQB8): Uploaded 2016, which breaks the 'nothing older than 2020' limit. It is also a flagged surface-level graphic-design intro.
- [Material UI Typography Component | Material UI 5 Tutorial | Typography in Material UI #4](https://www.youtube.com/watch?v=TGGBUd_qRog): Teaches Material UI's Typography component API rather than typographic design, and is flagged off_topic and too basic.

<details><summary>Filtered before assessment (32)</summary>

- Perfect shadows in UI design: Figma tutorial (prefilter): too short (32s)
- Typography Explained!  – For Logo, Graphic & UI/UX Designers (prefilter): too short (56s)
- Master Modern CSS Depth: Build an Interactive 3D Shadow Generator (prefilter): too short (29s)
- University Website Makeover 🔥 | Before vs After Redesign of CSKHPKV Website (Responsive & Modern UI) (prefilter): too short (75s)
- 12 UI/UX Laws You MUST KNOW 🧠 | Become a UI/UX Designer in 2024 | Saptarshi Prakash (prefilter): pool cap reached
- Understanding Visual Design Principles | Google UX Design Certificate (prefilter): pool cap reached
- Layout Space Grids UI UX | Design Fundamentals pt 1 (prefilter): pool cap reached
- How to choose fonts (typefaces) as a UX/UI designer (prefilter): pool cap reached
- Color Theory in UI Design (prefilter): pool cap reached
- The Laws of UX - 19 Psychological Design Principles (prefilter): pool cap reached
- Complete Website Redesign Process (8 Years of Conversion Secrets in 4 Minutes) (prefilter): pool cap reached
- How to Become a UI/UX designer in 2025 | Without Degree | Complete Guide in Hindi, English Captions (prefilter): pool cap reached
- Master Layout Design In 8 Minutes! (IMPORTANT) (prefilter): pool cap reached
- 6 EASY Tips to 10x Any Site's Design (prefilter): pool cap reached
- Color Theory In UI Design | How To Choose Colors ? | UI Design Color Theory | Simplilearn (prefilter): pool cap reached
- Graphic Design Hierarchy Explained | Make Your Designs Easy to Read (prefilter): pool cap reached
- 5 laws of design layout & composition *golden rules* (prefilter): pool cap reached
- Typography for Developers Tutorial - Full Course (prefilter): pool cap reached
- UI Design | How to choose colors and color palettes (prefilter): pool cap reached
- Figma Shadow and Blur Tutorial in Urdu/Hindi - Adding Depth and Dimension to Your Designs! (prefilter): pool cap reached
- Website Redesign Guide For WordPress - FULL PROCESS (prefilter): pool cap reached
- Color Theory for UI Design | How to Choose Colors for Better User Interfaces (language): transcript is 'hi', learner needs 'en'
- Visual Hierarchy in UI Design | Control Attention and Improve Interface Design (language): transcript is 'hi', learner needs 'en'
- UI Layout and Spacing Explained | Build Clean and Organized Interfaces (language): transcript is 'hi', learner needs 'en'
- UI Colour Systems in Hindi | Full UX Design Course for Beginners by Cutting Edge School (language): transcript is 'hi', learner needs 'en'
- Typography in UI Design | Visual Hierarchy and Readability Explained (language): transcript is 'hi', learner needs 'en'
- UI/UX Design Full Course for Beginners 2025 | Lets Uncover (language): transcript is 'hi', learner needs 'en'
- Color Theory Masterclass 2026 | Full Free Course for UI/UX Designers | Saurabh Saini (language): transcript is 'hi', learner needs 'en'
- How to Redesign Website Using Claude AI | Complete Website + SEO Tutorial (language): transcript is 'hi', learner needs 'en'
- Web Design mein 12 Column Layout | Figma Tutorial in Hindi | Design Systems | Ansh Mehra UX (language): transcript is 'hi', learner needs 'en'
- Typography in UI Designing by graphics guruji | UI Skills in Hindi part 7 (language): transcript is 'hi', learner needs 'en'
- How to Choose Colors (Easy 3-Step Process) (language): transcript is 'hi', learner needs 'en'

</details>

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.168 · 79 s_
