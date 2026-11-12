# Curriculum: Build a small React app this weekend, something like a habit tracker with local storage

**Budget:** 360 min · **Planned:** 172 min · **Videos:** 8 · **Candidates assessed:** 36

**How I read the goal:** By the end of the weekend, the learner has built and run a working habit tracker in React (Vite) that persists data to localStorage, and understands the hooks and component patterns behind it.

**Assumptions:** The 360 minutes is video viewing time only, so the plan fits about 6 hours of videos with no time reserved for practice.; Learner is comfortable with modern JS (ES6 modules, arrow functions, destructuring, array methods) given 'JavaScript fundamentals', so these are not re-taught.; A habit tracker means adding, completing and deleting habits, with daily or streak tracking and data persisted in localStorage.; Plain JavaScript React is preferred over TypeScript since only JS fundamentals are known.; Functional components and hooks are taught, not legacy class components.
> ⚠️ None of the 36 candidates has a transcript, so every pick rests on titles, chapters and descriptions. Expect low confidence throughout, and treat each reason as a hypothesis to check while watching.
> ⚠️ The curriculum uses about 172 of the 360 minutes (roughly 48%), leaving about 188 unused. The pool has no good habit-tracker video, and the long courses either contain off-topic projects or are heavier than the learner needs. Adding JavaScript Mastery's props, state and useEffect chapters (26:15-42:40) would fill about 16 more minutes, but it adds a new creator with no transcript to check.
> ⚠️ Sub-topic coverage is thin for custom hooks and component patterns, and there is no source for lifting state up. The learner may need to add material from official React documentation or a transcript-verified video.
> ⚠️ Programming with Mosh is used in two non-overlapping parts, with the Vite video between them. Its setup section may use different tooling, and the course may use TypeScript. Skip any TypeScript-specific detail.
> ⚠️ Learn the Tech's localStorage video is Part 2 of a series, and Part 1 is not in the pool. If the learner has not seen the to-do basics, the setup may be missing.
> ⚠️ HT0SMABqHAQ uses react-spring, yarn and TypeScript tooling. Skip the animation section and use plain JavaScript and npm.
> ⚠️ X92kk5iT8CM builds a to-do app with a dashboard and Tailwind. Treat it as a reference build, and adapt it to a habit model with daily check-ins and streaks rather than copying it.
> ⚠️ Assumes the 360-minute budget is viewing time only, so no time is reserved for practice. Plan on spending extra time coding the habit tracker yourself.

## Plan

- **React mental model and JSX** (`react_mental_model_jsx`): As a backend engineer who knows JS, they need to learn the declarative UI, components, props and JSX syntax, and how these differ from DOM scripting.
- **Vite project setup and project structure** (`vite_setup`): They know npm, so they only need Vite scaffolding, the dev server, file layout and how the entry point mounts the app.
- **Components, props and composition patterns** (`components_props`): A habit tracker needs a list, items, a form and a header, so they need to split the UI into reusable components and pass data and callbacks down.
- **useState, event handling, controlled forms and rendering lists** (`state_events_forms`): Adding, toggling and deleting habits requires state updates, controlled inputs, keys and immutable updates to arrays and objects.
- **useEffect and persisting state to localStorage** (`effects_localstorage`): Saving and loading habits needs side effects, dependency arrays, lazy state initialization and JSON serialization, which they already know. A custom useLocalStorage hook is a good fit.
- **Custom hooks, lifting state up and component patterns** (`custom_hooks_patterns`): Structuring the app cleanly means extracting reusable logic and deciding where state lives, a step toward maintainable code.
- **Build a habit tracker app in React end to end** (`build_habit_tracker`): A project video that builds a similar app with local storage ties all the concepts together and is the backbone of the plan.

## Watch in this order

### 1. [React Tutorial for Beginners](https://www.youtube.com/watch?v=SqcY0GlETPk)
Programming with Mosh · 80 min · watch 00:00–19:55 · counts 20 min · beginner, lecture · covers react_mental_model_jsx · **confidence 0.40**

The opening segment covers what React is and how a dev environment is set up, which is the mental model the learner lacks. The card lists a 'what is react' section and a dev environment setup, so this is the framing before any code.

> [00:00] “Build amazing front-end apps with this beginner-friendly tutorial.” _(from chapters/description; no transcript)_

_Confidence note: Transcript was unavailable, so this rests on chapter titles only. Only the first 20 minutes are used. The setup may use create-react-app or TypeScript rather than Vite, and the card has just one generic quote._

### 2. [Vite Crash Course – Frontend Build Tool](https://www.youtube.com/watch?v=do62-z3z6FM)
freeCodeCamp.org · 40 min · watch 02:48–06:28 · counts 4 min · beginner, crash_course · covers vite_setup · **confidence 0.45**

The 02:48-06:28 segment is the one part of this tooling overview that creates a first React project with Vite, which fills the Vite gap in the plan. Static assets, environment variables, TypeScript and plugins are skipped because they are not needed for a plain JavaScript habit tracker.

> [02:48] “Create your first React project with Vite” _(from chapters/description; no transcript)_

_Confidence note: No transcript, so the timestamps come from the chapter map only. Confidence would rise if the segment is confirmed to be a hands-on scaffold rather than a slideshow._

### 3. [React Tutorial for Beginners](https://www.youtube.com/watch?v=SqcY0GlETPk)
Programming with Mosh · 80 min · watch 19:55–1:20:00 · counts 60 min · beginner, lecture · covers components_props, state_events_forms · **confidence 0.45**

The main block covers components, JSX, rendering lists, handling events, managing state and passing props, which matches the components and state sub-topics. The card's segments list these as sequential sections with code, so the learner gets the core React patterns used in a habit tracker.

> [00:00] “Build amazing front-end apps with this beginner-friendly tutorial.” _(from chapters/description; no transcript)_

_Confidence note: Based on segment titles only. The sub-topics are covered at beginner depth, and the course may use TypeScript. Confidence would rise with a transcript showing live code for lists and controlled inputs._

### 4. [Todo List Using React Js Hook Component And React-Spring For Animation Tutorial | 2020 HD](https://www.youtube.com/watch?v=HT0SMABqHAQ)
THE SHOW · 36 min · watch 03:00–23:44 · counts 21 min · beginner, crash_course · covers state_events_forms, build_habit_tracker · **confidence 0.35**

The 03:00-23:44 segment builds a card component and a form component, then covers useState to add and remove todos. That is the form and list-state pattern a habit tracker needs. The react-spring animation section that follows is skipped.

> [00:00] “In this React Js Hooks Crash Course video tutorial you will learn to code your first React app using React Hooks and then animate the app using React Spring!” _(from chapters/description; no transcript)_
> [00:00] “We will do this by building a simple todo application which is perfect for beginners and will allow you to understand the fundamentals of React Hooks.” _(from chapters/description; no transcript)_

_Confidence note: Unverified, since no transcript was available. The video uses yarn and TypeScript tooling, and the animation library is out of scope. It is a crash course, so depth is uncertain._

### 5. [React To-Do App Part 2: Local Storage + useEffect — Save Tasks Even After Refresh!](https://www.youtube.com/watch?v=UKgT7SuiieE)
Learn the Tech · 25 min · counts 25 min · beginner, other · covers effects_localstorage · **confidence 0.40**

The video is about syncing React state to localStorage with useEffect so tasks survive a page refresh. That is exactly the effects-plus-persistence step the habit tracker needs, and it is hands-on, because it modifies a to-do app.

> [00:00] “Restore data when the page refreshes” _(from chapters/description; no transcript)_
> [00:00] “Understand how React state + localStorage work together” _(from chapters/description; no transcript)_

_Confidence note: This is Part 2 of a series, and Part 1 is not in the pool, so the learner may need the earlier setup. The description was the only evidence, so the teaching depth is unverified._

### 6. [Learn How to Use Local Storage in React With an Easy-to-Understand Example](https://www.youtube.com/watch?v=N7rs5F4f6FA)
Max Programming · 9 min · counts 9 min · intermediate, concept_explainer · covers effects_localstorage, custom_hooks_patterns · **confidence 0.40**

The video shows how to inspect localStorage in devtools, fix a setter bug, read saved data back, and use a custom hook. This covers persistence and the first custom hook pattern in one short video. It is the kept member of the localStorage cluster.

> [00:00] “In this video, we cover how you can use local storage in your React app!” _(from chapters/description; no transcript)_
> [00:00] “The proper way to do it is the second way...” _(from chapters/description; no transcript)_

_Confidence note: Chapter list only, so the bug fix and the custom hook depth are unverified. The custom hook section relies on a third-party library, so the learner does not get to write the hook from scratch here._

### 7. [Persist State to localStorage in React (Complete Tutorial)](https://www.youtube.com/watch?v=RDAFJ5ToMmQ)
Cosden Solutions · 19 min · watch 13:01–19:00 · counts 6 min · intermediate, other · covers custom_hooks_patterns · **confidence 0.30**

The 13:01-19:00 segment wraps localStorage logic in a reusable usePersistedState hook, which teaches the custom hook pattern the plan requires. Earlier utility-function sections are skipped to avoid repeating N7rs5F4f6FA.

> [00:00] “putting all of that into a custom hook that we can easily re-use across any component in our application” _(from chapters/description; no transcript)_

_Confidence note: This is an intermediate video flagged too_advanced_for_learner and has no transcript, so the segment may be harder to follow than expected. Confidence would rise if the hook is written step by step rather than just presented._

### 8. [Build a Complete To-Do List App with React + Vite | Dashboard, Reminders & Local Storage Tutorial](https://www.youtube.com/watch?v=X92kk5iT8CM)
DevCrafted Learn-Build-Deploy · 27 min · counts 27 min · beginner, project_build · covers build_habit_tracker, custom_hooks_patterns, effects_localstorage · **confidence 0.35**

The video builds a React and Vite app with add, edit, delete, complete and localStorage persistence through a useLocalStorage hook. That is the closest match in the pool to the end-to-end habit tracker, so the learner ends with a working project to adapt.

> [00:00] “In this comprehensive tutorial, we'll create a feature-rich task management app with a modern dashboard, reminder notifications, and persistent storage.” _(from chapters/description; no transcript)_
> [00:00] “Custom Hook Creation (useLocalStorage)” _(from chapters/description; no transcript)_

_Confidence note: Based on the description and feature list only. It is a to-do app rather than a habit tracker, and it adds dashboard, Tailwind and reminder features that are out of scope, so the learner will need to adapt it._

## Similar videos: why only one made the cut

- kept `N7rs5F4f6FA` over `1uiNxQIpcLU` (both cover custom hook, localstorage, localstorage in devtools): For this learner, N7rs5F4f6FA covers the full persistence story (devtools inspection, a setter bug fix, reading data back) and then a custom hook. 1uiNxQIpcLU covers only the hook and is flagged too_advanced_for_learner, so it would come before the persistence basics.
- kept `zUV_f5j4NzI` over `tjLXot9FsGE` (both cover component reuse, components, passing props, props): tjLXot9FsGE is in Hindi, so it is excluded. zUV_f5j4NzI is the only English option and is a short beginner explainer, but it is not added because the Programming with Mosh segment already covers props and components.

## Considered and dropped

- [Learn React With This ONE Project](https://www.youtube.com/watch?v=G6D9cBaLViA): Tech With Tim's 99.5-minute movie-browsing app is off_topic for a habit tracker and does not cover localStorage. It is also poor_transcript, so the useful parts cannot be confirmed.
- [React JS 19 Full Course 2025 | Build an App and Master React in 2 Hours](https://www.youtube.com/watch?v=dCLhUialKPQ): JavaScript Mastery's 127-minute intermediate course builds a movie app with Tailwind and an API. It covers props, state and useEffect, but the useful segments are much shorter than the full video, and adding a second creator on unverified material is not worth it here.
- [React JSX , Babel, React Components & Props Explained from Scratch | ReactJS Full Course #2](https://www.youtube.com/watch?v=JdFUNKGwWLw): Coder Army's 66-minute JSX and Babel session is a concept explainer with no project. Its focus on why React works is useful background but is mostly theory, and the learner wants hands-on work.
- [Every React Concept Explained in 12 Minutes](https://www.youtube.com/watch?v=wIyHSOugGGw): Code Bootcamp's 12-minute overview is a surface_intro that touches about 20 concepts without building anything, so it cannot teach the sub-topics in depth.
- [React Custom Hooks: useLocalStorage - Simply Explained!](https://www.youtube.com/watch?v=1uiNxQIpcLU): Cosden's useLocalStorage hook video is a near-duplicate of N7rs5F4f6FA. It covers only the hook, is flagged too_advanced_for_learner, and comes before the learner has the persistence basics.
- [#13: Props in React JS - Making Netflix Cards Reusable🔥React Tutorial in Hindi](https://www.youtube.com/watch?v=tjLXot9FsGE): The Thapa Technical props video is in Hindi (wrong_language), so the learner would not be able to follow it.
- [React Todo List App Tutorial with TypeScript & Tailwind CSS | Beginner React.js Project](https://www.youtube.com/watch?v=2W-y7ze2k9M): EgbonTech's to-do app is built in TypeScript with Tailwind, which conflicts with the plain-JavaScript preference. It also does not cover localStorage.
- [React To-Do App Tutorial | Build a Todo List with CRUD in React JS | Frontend Project](https://www.youtube.com/watch?v=fsyfL33soRQ): CodeFlow's CRUD to-do app with localStorage is a strong topical match, but it uses create-react-app and Tailwind (outdated_tooling), and at 67.7 minutes it is too long for the slot it would fill.
- [Learn Custom Hooks In 10 Minutes](https://www.youtube.com/watch?v=6ThXsUwLWvc): Web Dev Simplified's 10-minute custom hooks video is flagged too_advanced_for_learner. It is an intermediate-level primer on hook design, which comes after the basics the learner still needs.
- [localStorage + Sign-in Frontend: Building a Habit Tracker with React/Redux/Express Part 9](https://www.youtube.com/watch?v=35LuyXrByPM): Taha Khan's part 9 of a habit tracker series depends on Redux, Express and sign-in, and is too_advanced_for_learner. The series would also need parts 1 to 8 to make sense.
- [I am building an open-source habit tracker app!](https://www.youtube.com/watch?v=Uy74FxBnQEk): The React Native and SQLite vlog is off_topic, since it covers neither React web nor the hooks and localStorage the learner needs.
- [Build this to-do-list app with React! ☝](https://www.youtube.com/watch?v=9wiWzu_tRB0): Bro Code's useState-only to-do app is mostly HTML and CSS plus plain JS functions, and the card gives no evidence of real React component work, so it is a weak fit.

<details><summary>Filtered before assessment (29)</summary>

- React Project | Habit Tracker (prefilter): too short (23s)
- How to Update LocalStorage Automatically in React When State Changes (prefilter): too short (105s)
- 🚀🔥 React & Redux Complete Course (2024) with Projects | Notes | Free Certification (prefilter): 1194 min, far beyond the 360-min budget
- Learn React With This One Project (prefilter): pool cap reached
- React JS Components & Props in Hindi | Beginner to Practical Project (prefilter): pool cap reached
- How To Make a To Do List Using React - useState/Hooks [Part 1/3] (prefilter): pool cap reached
- Creating a Custom React Hook for Local Storage: Persisting State Effortlessly (prefilter): pool cap reached
- Fullstack Nextjs15 Habit Tracker | local storage & stage-management | overview (prefilter): pool cap reached
- Build a React To-Do App with Local Storage (Hooks) (prefilter): pool cap reached
- React js 19 tutorial in Hindi #7 Make First Component (prefilter): pool cap reached
- #48: Registration Forms in React: Handling Multiple Input Fields with useState – The Hard Way (prefilter): pool cap reached
- useEffect Dependency Array Explained: Persisting React Native State with AsyncStorage (prefilter): pool cap reached
- LocalStorage in React Using Custom Hook | The Complete React Course | Ep.41 (prefilter): pool cap reached
- Habit-Tracker App in React (prefilter): pool cap reached
- Todo List App with React & Tailwind Tutorial (prefilter): pool cap reached
- React Course For Beginners (Build a Project) (prefilter): pool cap reached
- ReactJS Component & JSX Tutorial in Hindi / Urdu (prefilter): pool cap reached
- Todo List Application using React JS in Hindi | React Projects for beginners in Hindi (prefilter): pool cap reached
- How to Persist Data in localStorage with React After Page Refresh? (prefilter): pool cap reached
- React  Habit Tracker (prefilter): pool cap reached
- 🚀 React JS ToDo App Tutorial for 2024 | Edit Task Functionality | Hindi 🧑‍💻 (prefilter): pool cap reached
- Build TODO List App with React JS from Scratch - React JS Mini Project [2026] (language): transcript is 'hi', learner needs 'en'
- #34: React Project - Build a Complete Todo App from Scratch with Advanced Features (language): transcript is 'hi', learner needs 'en'
- React Tutorial in Hindi 🔥🔥 (language): transcript is 'hi', learner needs 'en'
- Learning Components/Props/JSX in React 2024 (language): transcript is 'hi', learner needs 'en'
- Habit-tracker app with the help of react and redux (prefilter): video is unavailable (private or removed)
- A Habit Tracker App Using React Redux (prefilter): video is unavailable (private or removed)
- Sign-in Backend + Logout: Building a Habit Tracker with React/Redux/Express Part 10 (prefilter): pool cap reached
- TodoList App using React, Tailwind & React Icons | Sigma Web Development Course - Tutorial #114 (prefilter): pool cap reached

</details>

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-5.5, select=anthropic/claude-haiku-5.5 · cost $0.021 · 151 s_
