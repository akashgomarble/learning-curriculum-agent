# Curriculum: Build a small React app this weekend, something like a habit tracker with local storage

**Budget:** 360 min · **Planned:** 105 min · **Videos:** 3 · **Candidates assessed:** 29

**How I read the goal:** By the end of the weekend, the learner has built and run a working habit tracker in React (Vite) that persists data to localStorage, and understands the hooks and component patterns behind it.

**Assumptions:** Habit tracker means: add/delete habits, mark them complete per day, view streaks, with data persisted in localStorage; The 360 minutes is pure watching time, so a long project build video can serve as the backbone; Plain JavaScript (not TypeScript) is fine since the learner knows JS fundamentals but did not mention TypeScript; Modern function components and hooks only; class components are not needed; The 'nothing before 2022' constraint is handled by the later video-selection step using upload dates; the exclusions here cover title-based filters only
> ⚠️ Budget use is about 105 of 360 minutes (29%). About 255 minutes are unused because the remaining candidates were flagged, unverifiable (poor transcripts), pre-2022, off-stack (Redux/Next.js/TypeScript) or redundant. I chose to under-fill rather than pad with weak videos.
> ⚠️ None of the cards had verified quotes, so evidence_quote_ids are empty and all confidence values are moderate. The picks rest on summaries, topics and segment maps only.
> ⚠️ No candidate teaches habit-specific streak logic or per-day completion tracking. You will need to write the streak calculation yourself, using the todo builds' list and toggle patterns plus plain JavaScript date handling.
> ⚠️ Component patterns are only partly covered. Lists/keys and composition come from the build videos, and custom hooks from the short hook video. Lifting state up is covered only implicitly in the builds, and no video teaches it explicitly.
> ⚠️ Both builds are plain JavaScript todo apps rather than habit trackers. The QdT video is from 2022 and may not use Vite, so rely on the X92 video for Vite setup.
> ⚠️ The X92 card lists 27 minutes of runtime but segment timestamps up to 45:00. I counted 27 minutes toward the budget.
> ⚠️ The 'at most two videos per creator' constraint is satisfied: all three picks come from different creators.

## Plan

- **Vite project setup and React project structure** (`vite_setup`): The learner knows npm but not Vite; they need to scaffold a modern React project and understand the folder layout, dev server and build, instead of using create-react-app.
- **JSX and function components with props** (`jsx_components`): As a JS-literate backend dev, they need the mental model of JSX as JS expressions plus component composition and props to build UI.
- **State with useState and event handling** (`state_events`): A habit tracker is driven by state (habits list, completion toggles); they need immutable updates of arrays/objects and form handling.
- **useEffect and persisting state to localStorage** (`effects_localstorage`): Persistence is a core requirement; they need to understand effects, dependency arrays, lazy state initialization and JSON serialization (which they already know).
- **Component patterns: lifting state up, lists and keys, custom hooks** (`component_patterns`): To structure a multi-component app cleanly, they need to share state between components, render lists correctly, and extract a reusable useLocalStorage hook.
- **Build a habit tracker / similar small app end-to-end** (`project_build`): Following a project build ties all concepts together and mirrors the weekend goal; it is the backbone of the plan.
- **Streak logic, styling and finishing touches** (`polish_deploy`): The learner needs to adapt the tutorial project into their own habit tracker by adding date-based completion and streak calculation.

## Watch in this order

### 1. [Build a Complete To-Do List App with React + Vite | Dashboard, Reminders & Local Storage Tutorial](https://www.youtube.com/watch?v=X92kk5iT8CM)
DevCrafted Learn-Build-Deploy · 27 min · counts 27 min · beginner, project_build · covers vite_setup, jsx_components, state_events, effects_localstorage · **confidence 0.70**

A short, project-based React + Vite build with no red flags. Per its summary and segment map it goes from Vite setup through JSX components, useState and event handling to useEffect + localStorage, and it also covers lists/keys. That gives a Python engineer a fast first pass through the whole stack on a small app.


_Confidence note: Card has no verified quotes, and its 27-minute duration conflicts with segment timestamps running to 45:00. Higher if the full build is confirmed; lower if the later segments are missing._

### 2. [Build a Todo App with React.js | Beginner React Project using hooks](https://www.youtube.com/watch?v=QdTHUv79EZc)
Coding With Dawid · 62 min · counts 62 min · beginner, project_build · covers jsx_components, state_events, effects_localstorage, component_patterns, project_build, polish_deploy · **confidence 0.70**

A full hour-long build of a hooks-based todo app (useState, useEffect, localStorage, CSS animations) that is almost the same shape as a habit tracker (add/delete/toggle items, persisted). It is the project backbone, and you can adapt its list and toggle logic to habits and days. The card is unflagged and project-based.


_Confidence note: The card has no segment breakdown or verified quotes. It uploaded in Nov 2022, so Vite usage is uncertain (vite_setup relevance is 1), which is why X92 comes first for setup._

### 3. [ReactJS Tutorial 81: Creating Our Own useLocalStorage Hook In ReactJS](https://www.youtube.com/watch?v=wKjsnUIfGHI)
Code Stoic · 16 min · counts 16 min · intermediate, concept_explainer · covers component_patterns · **confidence 0.55**

Builds a custom useLocalStorage hook that combines useState and useEffect. This is the custom-hook pattern the learner needs and the two project builds don't clearly teach. Use it to refactor the habit tracker's persistence into a reusable hook.


_Confidence note: It is flagged pure_theory and is a short concept explainer. I picked it only because no unflagged candidate clearly covers custom hooks. The card shows no verified quotes and its segment map covers only the first 8 of 16 minutes._

## Similar videos: why only one made the cut

- kept `wKjsnUIfGHI` over `h97s1tfi5P8` (both cover custom hooks, localstorage, useeffect, uselocalstorage): It explicitly builds the hook from useState + useEffect, which ties the hook to the earlier effects lesson. The alternative is a codesandbox demo of get/set/remove operations.
- kept `wKjsnUIfGHI` over `5uHikv1oBEI` (both cover custom hooks, localstorage, useeffect, uselocalstorage): A focused 16-minute build of the hook. The alternative is a 44-minute course lecture with a poor transcript and a pure_theory flag.
- kept `wKjsnUIfGHI` over `8bsG5Xg9PaI` (both cover custom hooks, localstorage, uselocalstorage): It is dated 2024, in English, and has a usable transcript. The alternative is a Hindi-language video from 2021, which fails both the wrong-language and date-floor checks.

## Considered and dropped

- [Learn React With This ONE Project](https://www.youtube.com/watch?v=G6D9cBaLViA): Poor transcript, and the summary describes an API-fetching project. It cannot be verified to cover Vite, hooks or localStorage, so it is too risky to spend 100 minutes on.
- [React Tutorial for Beginners](https://www.youtube.com/watch?v=SqcY0GlETPk): A lecture-format TypeScript course with an unusable transcript. It does not match the preference for project-based content and plain JS, and its coverage can't be confirmed.
- [Functional Components & Props & useState Hook](https://www.youtube.com/watch?v=orLqzKffcXo): A 53-minute pure-theory concept explainer on components, props and useState. Unflagged project builds already cover those sub-topics, and the learner wants to avoid pure theory.
- [React JS Tutorial for Beginners | Setup React with Vite & Understand Project Structure](https://www.youtube.com/watch?v=CU5cyEeCCBs): Covers only Vite setup and project structure in 63 minutes. It has a poor transcript and no project, and the X92 build covers setup in far less time.
- [Understand Any React Project in 16 Minutes | Vite + React + TypeScript Folder Structure Explained](https://www.youtube.com/watch?v=8ub_3kjILV8): A TypeScript folder-structure explainer flagged surface_intro and pure_theory. The learner uses plain JS, and X92 covers project setup inside a real build.
- [Vite Crash Course – Frontend Build Tool](https://www.youtube.com/watch?v=do62-z3z6FM): A 40-minute Vite config and tooling crash course flagged pure_theory and surface_intro. It goes deeper into build-tool configuration than a weekend React app needs.
- [React Custom Hooks: useLocalStorage - Simply Explained!](https://www.youtube.com/watch?v=1uiNxQIpcLU): Also a useLocalStorage hook explainer, but flagged surface_intro and pure_theory. It overlaps with the chosen custom-hook video, which also combines useState and useEffect.
- [A Habit Tracker App Using React Redux](https://www.youtube.com/watch?v=7VPULX3WcGE): A habit tracker, but built with Redux and Bootstrap, with a poor transcript and only 5.6 minutes. Redux is outside the learner's plan.
- [localStorage + Sign-in Frontend: Building a Habit Tracker with React/Redux/Express Part 9](https://www.youtube.com/watch?v=35LuyXrByPM): Uploaded in 2021, which violates the 2022 date floor. It is also a Redux/Express sign-in part, not a standalone habit tracker.
- [Every React Concept Explained in 12 Minutes](https://www.youtube.com/watch?v=wIyHSOugGGw): A 12-minute surface overview of every React concept, flagged surface_intro. The learner explicitly wants no shallow intros.

<details><summary>Filtered before assessment (38)</summary>

- React useEffect: Save Cart to localStorage | Beginner Tutorial (prefilter): too short (49s)
- Habit Tracker Using HTML, CSS and JS | JavaScript Beginner Friendly Project #100dayschallenge (prefilter): too short (35s)
- Persist State to localStorage in React (prefilter): too short (55s)
- How to Install React in 2026 - Goodbye Create React App - Vite React Project (prefilter): too short (114s)
- useEffect Syntax Explained in 30 Seconds (prefilter): too short (38s)
- React Project | Habit Tracker (prefilter): too short (23s)
- React JS vs Vite JS Explained for Beginners | 2025 Web Development Guide #shorts #reactjs (prefilter): too short (47s)
- UseEffect React Hook the complete guide: Fetch data + Dependency Array + convert class to function (prefilter): pool cap reached
- Creating a Custom React Hook for Local Storage: Persisting State Effortlessly (prefilter): pool cap reached
- Habit-Tracker App in React (prefilter): pool cap reached
- How To Make To-Do List App Using React JS And Tailwind CSS | Create Task App In React JS (prefilter): pool cap reached
- React JS with Vite Tutorial in English 🚀 | Build Home, About Us & Contact Pages | Beginner to Adv. (prefilter): pool cap reached
- React JS Tutorial #2 | Setup React Project using Vite, Node.js & Create React App (prefilter): pool cap reached
- React State Vs Props (prefilter): pool cap reached
- Persist State to localStorage in React (Complete Tutorial) (prefilter): pool cap reached
- ReactJS Tutorial 80: Creating Custom Hooks In React (prefilter): pool cap reached
- 🔴 Building a Todo List App Project with Local Storage in React JS  & Hooks in 2021 (prefilter): pool cap reached
- React JS Setup with Vite | Beginner Guide (2026) (prefilter): pool cap reached
- Learn useState In 15 Minutes - React Hooks Explained (prefilter): pool cap reached
- #40: Keep Todo Data After Refresh: Adding Local Storage in React (prefilter): pool cap reached
- 13. Custom hooks in react - useCounter, useLocalstorage ,useForm & useFetch | react in Hindi (prefilter): pool cap reached
- JWT for User Auth: Building a Habit Tracker with React/Redux/Express Part 11 (prefilter): pool cap reached
- Building a Todo List App Project in ReactJS from Scratch in Hindi in 2020. #viral #python #shorts (prefilter): pool cap reached
- 80 : useEffect in React and how to retrieve data from localStorage (language): transcript is 'ar', learner needs 'en'
- #34: React Project - Build a Complete Todo App from Scratch with Advanced Features (language): transcript is 'hi', learner needs 'en'
- Build TODO List App with React JS from Scratch - React JS Mini Project [2026] (language): transcript is 'hi', learner needs 'en'
- Hooks & State in React | Sigma Web Development Course - Tutorial #107 (language): transcript is 'hi', learner needs 'en'
- Todo List Application using React JS in Hindi | React Projects for beginners in Hindi (language): transcript is 'hi', learner needs 'en'
- Add to Cart in React JS | useState + Props Explained with Simple E-Commerce Project (language): transcript is 'ta', learner needs 'en'
- React Custom Hook useLocalStorage() Hook The Complete Beginner’s Guide!🚀#reactjs #coding #javascript (language): transcript is 'hi', learner needs 'en'
- 🚀 React JS ToDo App Tutorial for 2024 | Edit Task Functionality | Hindi 🧑‍💻 (language): transcript is 'hi', learner needs 'en'
- Create a React App Using Vite + Folder Structure Explained (language): transcript is 'fi', learner needs 'en'
- Components, Props and JSX in React | Sigma Web Development Course - Tutorial #106 (language): transcript is 'hi', learner needs 'en'
- Working with localStorage in ReactJS, ReactJS Tutorial In Telugu #coding #js #reactjs (language): transcript is 'te', learner needs 'en'
- Learn "useState" Hook in React 2024 (language): transcript is 'hi', learner needs 'en'
- Building a Dynamic To-Do List in Local Storage in Hindi | JavaScript 2024🔥 (language): transcript is 'hi', learner needs 'en'
- React Tutorial in Hindi 🔥🔥 (language): transcript is 'hi', learner needs 'en'
- React Installation and Setup | Create React App using Vite | React Tutorial for Beginners #3 (language): transcript is 'hi', learner needs 'en'

</details>

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.083 · 38 s_
