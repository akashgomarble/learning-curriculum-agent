# Curriculum: Get better at design

**Budget:** 180 min · **Planned:** 148 min · **Videos:** 8 · **Candidates assessed:** 33

**How I read the goal:** A frontend developer comes away able to make their own UIs look noticeably more polished by applying core visual design principles (hierarchy, spacing, typography, color) and by critiquing and redesigning real interfaces.

**Assumptions:** 'Design' means UI/visual design for web apps, not graphic design, UX research, or brand design; The learner wants to improve the look of interfaces they build in code, so developer-oriented design content fits best; Because they know CSS, layout mechanics are skipped and the focus is on design decisions; 'Nothing older than 2020' means videos published in 2020 or later; No design tool such as Figma is assumed; tool basics are included only as far as needed to follow redesigns
> ⚠️ No candidate has verified quotes and every card is based on metadata, with poor or unverified transcripts. All picks are therefore based on titles and summaries and carry moderate-to-low confidence, so skim the first minutes of each before committing.
> ⚠️ Colour contrast and accessibility (WCAG ratios) are likely thin: the colour video is about palette building, and no candidate clearly teaches contrast checking.
> ⚠️ Borders, border-radius and icons are not covered. Only shadows are covered in the polish-details slot.
> ⚠️ The redesign and critique videos are a student website and a WordPress site, not React or web-app UIs, so you will need to translate the lessons to your own components.
> ⚠️ Total viewing time is 148.3 of 180 minutes (82%). The remaining 31.7 minutes are unused because the other candidates were redundant, off-level, too long for their slots or had unusable evidence, and padding with weak videos seemed worse than under-filling.
> ⚠️ The plan uses 8 creators because no single creator covers all the topics. Expect to adjust to different teaching styles.
> ⚠️ I read 'nothing older than 2020' as upload dates in 2020 or later, and all picks meet that.

## Plan

- **Visual hierarchy and layout composition** (`visual_hierarchy`): They can build any layout with Flexbox and Grid, but need to learn how to guide the eye with size, weight, contrast and emphasis.
- **Spacing, alignment and consistent spacing scales** (`spacing_alignment`): Inconsistent spacing is the most common reason developer-built UIs look amateur, and a spacing scale maps directly onto CSS variables.
- **Typography for interfaces** (`typography`): Font choice, type scale, line height and line length strongly affect polish and readability and are easy to apply in CSS.
- **Color systems, contrast and accessibility** (`color_contrast`): They need a practical way to build palettes, shades and accessible contrast rather than picking colors by guesswork.
- **Polish details: shadows, borders, radius, and icons** (`depth_details`): Small refinements make UIs feel finished, and they translate directly into CSS properties.
- **Critiquing existing UIs and spotting problems** (`ui_critique`): Learning to diagnose what is wrong with a real interface builds the design eye and satisfies the need for practical critique.
- **Full redesign of a real UI, step by step** (`redesign_walkthrough`): Watching principles applied end to end on a real interface shows how to combine them and gives a repeatable process.

## Watch in this order

### 1. [The Beginner's Guide To Visual Hierarchy](https://www.youtube.com/watch?v=kK1TOpI948o)
DesignSpo · 16 min · counts 16 min · beginner, concept_explainer · covers visual_hierarchy · **confidence 0.50**

Introduces visual hierarchy through contrast, uniformity and making elements stand out, which is the prerequisite for every later topic. Its only red flag is a poor transcript, so it is a better fit for a CSS-literate developer than the surface_intro or pure_theory alternatives.


_Confidence note: Based on title and summary only, with no transcript or verified quotes. Seeing real UI examples in it would raise confidence._

### 2. [Why Your UI Designs Look Off — It's Your Spacing & Layout](https://www.youtube.com/watch?v=fImTa4daVc8)
Ali Hassan · 25 min · counts 25 min · beginner, concept_explainer · covers spacing_alignment · **confidence 0.55**

Targets spacing and layout as the main reason UIs look off. This is the most relevant spacing video in the pool, and as a developer you can turn its fixes straight into CSS values.


_Confidence note: Spacing relevance is high, but the transcript is poor so the depth is unverified. It is unclear whether it teaches an explicit spacing scale._

### 3. [The 80% of UI Design - Typography](https://www.youtube.com/watch?v=9-oefwZ6Z74)
Sajid · 12 min · counts 12 min · beginner, concept_explainer · covers typography · **confidence 0.50**

Covers UI typography decisions: font size, weight and colour, and how they build hierarchy in interfaces. This is the decision-focused content you need, since you already know the CSS mechanics.


_Confidence note: It carries surface_intro and pure_theory flags, but it is the most UI-specific typography option. A transcript confirming concrete size and weight guidance would raise confidence._

### 4. [The ULTIMATE Guide To Typography For Beginners](https://www.youtube.com/watch?v=AXpxZMRM1EY)
DesignSpo · 14 min · counts 14 min · beginner, concept_explainer · covers typography · **confidence 0.40**

Adds typeface selection and text-handling fundamentals that the UI-specific typography video does not cover, such as how to choose and pair fonts. It fills the rest of the typography slot.


_Confidence note: Flagged as a surface intro and pure theory, and it is graphic-design oriented. It is included because it adds typeface-choice coverage that the other typography video lacks._

### 5. [Super Practical Guide to Color Theory, Color Models and Perfect Color Palettes | UI Design](https://www.youtube.com/watch?v=GyVMoejbGFg)
Elizabeth Alli - DesignerUp · 24 min · counts 24 min · beginner, concept_explainer · covers color_contrast · **confidence 0.55**

Teaches how to build professional UI palettes using tone, tint, shade and temperature, which basic colour-harmony tutorials usually skip. It is UI-specific and published in 2020, so it meets your date limit.


_Confidence note: The summary clearly targets UI palettes. Its segment map is thin, and it is unclear whether it covers contrast ratios and accessibility._

### 6. [The Easy Way to Fix Boring UIs](https://www.youtube.com/watch?v=wcZ6jSlZqDc)
Sajid · 9 min · counts 9 min · beginner, concept_explainer · covers depth_details · **confidence 0.50**

Shows how to add depth to flat, boring UIs with shadows, using CodePen. This is the closest match to the polish-details topic and is directly implementable in CSS.


_Confidence note: Only shadows are evidenced, so borders, radius and icons stay uncovered. The flags are surface_intro and pure_theory, but no other candidate offers better practical coverage._

### 7. [Website Redesign | Before & After (EP 01)](https://www.youtube.com/watch?v=CLLObtIpDUU)
Mr Saiful · 5 min · counts 5 min · beginner, project_build · covers ui_critique, redesign_walkthrough · **confidence 0.40**

A short before-and-after redesign of a real WordPress site that points out what was wrong, such as weak hierarchy and unclear calls to action. It gives you a quick critique example before the longer walkthrough.


_Confidence note: Only 4.9 minutes and the transcript is poor, so the critique may be shallow. It is chosen mainly to meet your requirement for a real redesign._

### 8. [UI/UX Website Redesign Before and After - CaterGraphix Design Academy](https://www.youtube.com/watch?v=7AhCIBGTiEA)
Deznr Academy · 44 min · counts 44 min · beginner, project_build · covers ui_critique, redesign_walkthrough · **confidence 0.50**

The longest real redesign in the pool: it walks through before-and-after improvements to an existing website and works as a critique of it. It lets you apply the hierarchy, spacing, typography and colour ideas from the earlier videos, and it meets your requirement for a real redesign or critique.


_Confidence note: The format and relevance fit, but the transcript is poor and the project is a student website. It would be stronger if the critique reasoning were verified._

## Similar videos: why only one made the cut

- kept `GyVMoejbGFg` over `1NTKwpAVcHg` (both cover color models, color palettes, color temperature, color theory): It is a 24-minute UI-specific guide to building palettes with tone, tint, shade and temperature. The dropped one is a 7-minute overview of layout, colour and typography with a surface_intro flag and a poor transcript.

## Considered and dropped

- [Visual Hierarchy in UI/UX — Why NOBODY can READ your DESIGNS](https://www.youtube.com/watch?v=OqAdmfRztds): Another visual hierarchy explainer. It overlaps with the kept hierarchy video, has a poor transcript and a surface_intro flag, and would add a creator without opening a new gap.
- [MASTER VISUAL HIERARCHY: Principles of VISUAL DESIGN for Designing Mobile Apps!](https://www.youtube.com/watch?v=LfkDiDyn6nU): At 76 minutes, it would use most of the hierarchy budget on mobile app design for a single topic. Its transcript is poor and it has no segment map to pick out a useful part.
- [UI / UX Design Tutorial – Wireframe, Mockup & Design in Figma](https://www.youtube.com/watch?v=c9Wg6Cb_YlU): An 86-minute Figma wireframe-to-mockup course. It is tool- and process-heavy, scores relevance 1 or less on the plan's topics, and teaches little design critique.
- [Industry-Standard Shadow System | Shadow Design System Tutorial for Product & UI/UX Designers](https://www.youtube.com/watch?v=dtRGlxI0TL8): At 49.8 minutes it is a pure-theory lecture on shadow systems, far beyond the 20-minute polish slot and not practical enough.
- [UI/UX Design Color Theory CRASH COURSE | Color Theory For Beginners | Saptarshi Prakash](https://www.youtube.com/watch?v=l6LqaAs4hWs): 26 minutes of colour psychology theory aimed at beginners. It overlaps with the kept colour video and does not cover UI palettes or contrast.
- [Complete Layout Guide](https://www.youtube.com/watch?v=MlsV3hu84as): A pure-theory, surface-level layout explainer that duplicates the hierarchy and spacing coverage already picked.
- [4 Foundational UI Design Principles | C.R.A.P.](https://www.youtube.com/watch?v=uwNClNmekGU): The C.R.A.P. principles are covered only as theory, with no redesign. Its alignment and proximity content is already covered by the spacing pick.
- [Steal My UI/UX Process in 2026 (Real Project Breakdown)](https://www.youtube.com/watch?v=t7cnk3aQp2c): A Figma process breakdown of a healthcare product. It is a workflow overview rather than a critique of an existing UI, its transcript is poor, and it has only 8.8 minutes of mixed content.
- [Website Redesign Before & After: Built to Convert, Not Just Look Nice](https://www.youtube.com/watch?v=mRd1qsWnpik): A 2.9-minute redesign comparison, too short to teach anything beyond what the other redesign videos show, with a poor transcript.
- [Beginning Graphic Design: Layout & Composition](https://www.youtube.com/watch?v=a5KYlHNKQB8): Uploaded in 2016, which breaks the 'nothing older than 2020' limit, and it is also graphic-design oriented.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.086 · 38 s_
