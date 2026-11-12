# Curriculum: Build a small React app this weekend, something like a habit tracker with local storage

**Budget:** 360 min · **Planned:** 296 min · **Videos:** 6 · **Candidates assessed:** 36

**How I read the goal:** By the end of the weekend, the learner has built and run a working habit tracker in React (Vite) that persists data to localStorage, and understands the hooks and component patterns behind it.

**Assumptions:** The 360 minutes is video viewing time only, so the plan fits about 6 hours of videos with no time reserved for practice.; Learner is comfortable with modern JS (ES6 modules, arrow functions, destructuring, array methods) given 'JavaScript fundamentals', so these are not re-taught.; A habit tracker means adding, completing and deleting habits, with daily or streak tracking and data persisted in localStorage.; Plain JavaScript React is preferred over TypeScript since only JS fundamentals are known.; Functional components and hooks are taught, not legacy class components.
> ⚠️ None of the candidates had a transcript, so every assessment is based on chapters and descriptions only. Confidence is moderate at best.
> ⚠️ Selected viewing time is about 296 of 360 minutes (around 64 minutes unused). The remaining candidates were redundant todo builds, surface intros, or flagged videos, so adding them would only pad the plan.
> ⚠️ No video builds a habit tracker specifically. You will adapt the todo-app patterns (add, complete, delete, localStorage) and add streak or daily logic yourself.
> ⚠️ Two picks (Mosh's segment and gNEQ8PSkaI4) use TypeScript. Follow along in plain JavaScript by dropping the type annotations.
> ⚠️ Custom hooks and component patterns get thin, unverified coverage, mainly from X92kk5iT8CM, N7rs5F4f6FA and Mosh's props segment.
> ⚠️ The plan assumes the JavaScript Mastery course sets up with Vite, as its 2025 version likely does. gNEQ8PSkaI4 covers Vite setup explicitly as a backup.

## Plan

- **React mental model and JSX** (`react_mental_model_jsx`): As a backend engineer who knows JS, they need to learn the declarative UI, components, props and JSX syntax, and how these differ from DOM scripting.
- **Vite project setup and project structure** (`vite_setup`): They know npm, so they only need Vite scaffolding, the dev server, file layout and how the entry point mounts the app.
- **Components, props and composition patterns** (`components_props`): A habit tracker needs a list, items, a form and a header, so they need to split the UI into reusable components and pass data and callbacks down.
- **useState, event handling, controlled forms and rendering lists** (`state_events_forms`): Adding, toggling and deleting habits requires state updates, controlled inputs, keys and immutable updates to arrays and objects.
- **useEffect and persisting state to localStorage** (`effects_localstorage`): Saving and loading habits needs side effects, dependency arrays, lazy state initialization and JSON serialization, which they already know. A custom useLocalStorage hook is a good fit.
- **Custom hooks, lifting state up and component patterns** (`custom_hooks_patterns`): Structuring the app cleanly means extracting reusable logic and deciding where state lives, a step toward maintainable code.
- **Build a habit tracker app in React end to end** (`build_habit_tracker`): A project video that builds a similar app with local storage ties all the concepts together and is the backbone of the plan.

## Watch in this order

### 1. [React JS 19 Full Course 2025 | Build an App and Master React in 2 Hours](https://www.youtube.com/watch?v=dCLhUialKPQ)
JavaScript Mastery · 127 min · counts 127 min · intermediate, full_course · covers react_mental_model_jsx, vite_setup, components_props, state_events_forms, effects_localstorage, build_habit_tracker · **confidence 0.60**

A hands-on course that goes from JSX basics through components, props, useState and useEffect, then builds a real app. For an experienced engineer it is the fastest single path through the React mental model, and the build section gives end-to-end practice with effects.

> [00:00] “Dive straight into React—from basic JSX to advanced hooks—and build a real, modern app in this hands-on crash course!” _(from chapters/description; no transcript)_
> [00:00] “Time Stamps 00:00:00 — Intro 00:01:41 — Crash Course 00:05:08 — React Setup 00:07:33 — Create React.js Project” _(from chapters/description; no transcript)_

_Confidence note: Judged from chapters and description only. The movie-app project does not cover localStorage. It would rank higher if the transcript confirmed the setup uses Vite and that the explanations go deep enough._

### 2. [React Tutorial for Beginners](https://www.youtube.com/watch?v=SqcY0GlETPk)
Programming with Mosh · 80 min · watch 33:20–1:20:00 · counts 47 min · beginner, lecture · covers components_props, state_events_forms, custom_hooks_patterns · **confidence 0.50**

This segment covers rendering lists, conditional rendering, event handling, state, props, passing functions to children, state vs props, and the children prop, ending with exercises. Together these are the composition and lifting-state patterns a habit tracker needs.

> [00:00] “Build amazing front-end apps with this beginner-friendly tutorial.” _(from chapters/description; no transcript)_

_Confidence note: Judged from chapters only, and the video uses TypeScript. The format is closer to a lecture, but it is code-along with exercises. The segment starts partway into a project built earlier in the video, so some context from before 33:20 may be missing._

### 3. [CRUD Todo App | React Typescript Project | Create TODO Web App With ReactJs + Typescript | Tutorial](https://www.youtube.com/watch?v=gNEQ8PSkaI4)
TSXpert · 61 min · counts 61 min · beginner, project_build · covers vite_setup, components_props, state_events_forms, build_habit_tracker · **confidence 0.55**

Builds a CRUD todo app from a fresh Vite install, split into TodoList and TodoForm components. This is the same add/complete/delete structure a habit tracker uses, and it covers Vite setup and project structure directly.

> [00:00] “In this tutorial, join me as we dive into the exciting world of building a CRUD (Create, Read, Update, Delete) Todo App using React and TypeScript.” _(from chapters/description; no transcript)_
> [02:10] “Installing React with Vite & Cleaning Up Defaults” _(from chapters/description; no transcript)_
> [44:09] “Rendering TodoList & Creating UI for App Component” _(from chapters/description; no transcript)_

_Confidence note: Judged from chapters only, and the app is written in TypeScript. The learner can drop the type annotations while following along. It does not cover persistence._

### 4. [React To-Do App Part 2: Local Storage + useEffect — Save Tasks Even After Refresh!](https://www.youtube.com/watch?v=UKgT7SuiieE)
Learn the Tech · 25 min · counts 25 min · beginner, other · covers effects_localstorage · **confidence 0.50**

Focuses on how useEffect works and on syncing to-do tasks into localStorage, then restoring them on refresh. This is the persistence layer the habit tracker needs.

> [00:00] “Learn how to store your React To-Do app data permanently even after page refresh!” _(from chapters/description; no transcript)_
> [00:00] “Restore data when the page refreshes” _(from chapters/description; no transcript)_
> [00:00] “Understand how React state + localStorage work together” _(from chapters/description; no transcript)_

_Confidence note: Judged from the description only, so it is unclear whether it is hands-on. It is part 2 of a series, so it may refer back to code from part 1._

### 5. [Learn How to Use Local Storage in React With an Easy-to-Understand Example](https://www.youtube.com/watch?v=N7rs5F4f6FA)
Max Programming · 9 min · counts 9 min · intermediate, concept_explainer · covers effects_localstorage, custom_hooks_patterns · **confidence 0.55**

Compares two ways to persist state, inspects localStorage in devtools, fixes a common setter bug, reads saved data back, and finishes with a custom hook. It is a compact way to learn the correct pattern after the basics.

> [00:00] “In this video, we cover how you can use local storage in your React app!” _(from chapters/description; no transcript)_
> [00:00] “The proper way to do it is the second way...” _(from chapters/description; no transcript)_

_Confidence note: Its chapter list is the most relevant to localStorage in the pool, but it is metadata only. The custom hook part uses a library rather than a hand-written hook._

### 6. [Build a Complete To-Do List App with React + Vite | Dashboard, Reminders & Local Storage Tutorial](https://www.youtube.com/watch?v=X92kk5iT8CM)
DevCrafted Learn-Build-Deploy · 27 min · counts 27 min · beginner, project_build · covers custom_hooks_patterns, effects_localstorage, build_habit_tracker · **confidence 0.45**

Builds a complete React and Vite task app with a hand-written useLocalStorage custom hook, form handling and persistence. Of all the candidates, it is the closest end-to-end match for the habit tracker to build this weekend.

> [00:00] “In this comprehensive tutorial, we'll create a feature-rich task management app with a modern dashboard, reminder notifications, and persistent storage.” _(from chapters/description; no transcript)_
> [00:00] “Learn how to build a professional To-Do List application from scratch using React + Vite!” _(from chapters/description; no transcript)_
> [00:00] “Custom Hook Creation (useLocalStorage)” _(from chapters/description; no transcript)_

_Confidence note: No transcript or chapters were available, only the feature list, so the actual teaching depth is unknown. It uses Tailwind._

## Similar videos: why only one made the cut

- kept `N7rs5F4f6FA` over `1uiNxQIpcLU` (both cover custom hook, localstorage, localstorage in devtools): Its chapters show the basic persistence approach, the common setter bug and reading data back before it reaches hooks, which fits a React newcomer. The Cosden video jumps straight to a custom hook and is flagged too advanced.

## Considered and dropped

- [React To-Do App Tutorial | Build a Todo List with CRUD in React JS | Frontend Project](https://www.youtube.com/watch?v=fsyfL33soRQ): A todo build with useEffect and localStorage that matches the goal well, but it uses Create React App (outdated tooling), and unflagged videos cover the same content with Vite.
- [Learn React With This ONE Project](https://www.youtube.com/watch?v=G6D9cBaLViA): Flagged off-topic: a movie-API app with no localStorage, and it overlaps with the JavaScript Mastery course already picked.
- [Every React Concept Explained in 12 Minutes](https://www.youtube.com/watch?v=wIyHSOugGGw): A 12-minute surface survey of React concepts, which the learner explicitly asked to avoid.
- [React Todo App Tutorial – Build with React Hooks from Scratch](https://www.youtube.com/watch?v=nwj4W4Em75A): Another useState/useEffect todo build. It would be the third todo project, so it is redundant with gNEQ8PSkaI4 and X92kk5iT8CM.
- [Vite Crash Course – Frontend Build Tool](https://www.youtube.com/watch?v=do62-z3z6FM): A Vite tooling overview with no React app built. Vite setup is already covered inside gNEQ8PSkaI4.
- [React Todo List App Tutorial with TypeScript & Tailwind CSS | Beginner React.js Project](https://www.youtube.com/watch?v=2W-y7ze2k9M): A TypeScript and Tailwind todo app with no persistence, so it overlaps with gNEQ8PSkaI4 and adds Tailwind setup.
- [Persist State to localStorage in React (Complete Tutorial)](https://www.youtube.com/watch?v=RDAFJ5ToMmQ): Flagged too advanced. Its usePersistedState content is covered by unflagged picks.
- [localStorage + Sign-in Frontend: Building a Habit Tracker with React/Redux/Express Part 9](https://www.youtube.com/watch?v=35LuyXrByPM): Part 9 of a React/Redux/Express series, focused on sign-in with Redux. It is too advanced and does not stand alone.
- [#13: Props in React JS - Making Netflix Cards Reusable🔥React Tutorial in Hindi](https://www.youtube.com/watch?v=tjLXot9FsGE): In Hindi (wrong language), and it only covers basic props.
- [React JSX , Babel, React Components & Props Explained from Scratch | ReactJS Full Course #2](https://www.youtube.com/watch?v=JdFUNKGwWLw): A conceptual JSX/Babel explainer with no project, which the learner prefers to avoid.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-5.5, select=anthropic/claude-opus-5.5 · cost $0.241 · 88 s_
