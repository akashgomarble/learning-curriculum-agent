# Curriculum: Build a small React app this weekend, something like a habit tracker with local storage

**Budget:** 360 min · **Planned:** 153 min · **Videos:** 6 · **Candidates assessed:** 36

**How I read the goal:** By the end of the weekend, the learner has built and run a working habit tracker in React (Vite) that persists data to localStorage, and understands the hooks and component patterns behind it.

**Assumptions:** The 360 minutes is video viewing time only, so the plan fits about 6 hours of videos with no time reserved for practice.; Learner is comfortable with modern JS (ES6 modules, arrow functions, destructuring, array methods) given 'JavaScript fundamentals', so these are not re-taught.; A habit tracker means adding, completing and deleting habits, with daily or streak tracking and data persisted in localStorage.; Plain JavaScript React is preferred over TypeScript since only JS fundamentals are known.; Functional components and hooks are taught, not legacy class components.
> ⚠️ No candidate had a transcript, so every pick is judged from chapters and descriptions only. Confidence is moderate to low everywhere. Check the first minutes of each video and swap it out if it does not match its description.
> ⚠️ The curriculum uses about 153 of 360 minutes (about 42%), leaving roughly 207 minutes unused. The pool has no verified habit-tracker tutorial, and the remaining videos were TypeScript-based, outdated (Create React App), too advanced, surface-level or redundant. Padding with them would hurt the learner more than under-filling.
> ⚠️ No video builds a habit tracker. The build_habit_tracker slot is covered only by a to-do app (X92kk5iT8CM). The learner should adapt it by adding habit-per-day completion and streak logic themselves, which the unused time can accommodate.
> ⚠️ Lifting state up and component composition patterns are covered only indirectly, through the movie-app and to-do builds. No dedicated video was strong enough to add.
> ⚠️ The first Tech With Tim range (6:02-40:00) is the intended source for JSX and Vite project setup. The Vite details are unconfirmed, so if the setup differs, use the first minutes of the Vite crash course (do62-z3z6FM, 02:48-06:28) for the exact npm create vite steps.
> ⚠️ The Tech With Tim ranges deliberately skip the routing and CSS chapters (about 40:00-1:01:00). The second range includes context and API material, which can be skimmed. The learner already knows HTTP.
> ⚠️ Neither near-duplicate cluster contributed a pick: the custom-hook pair (N7rs5F4f6FA, 1uiNxQIpcLU) was passed over for a clearer description, and the props pair (tjLXot9FsGE, zUV_f5j4NzI) was not needed because the picked project covers props. tjLXot9FsGE is also flagged wrong_language.

## Plan

- **React mental model and JSX** (`react_mental_model_jsx`): As a backend engineer who knows JS, they need to learn the declarative UI, components, props and JSX syntax, and how these differ from DOM scripting.
- **Vite project setup and project structure** (`vite_setup`): They know npm, so they only need Vite scaffolding, the dev server, file layout and how the entry point mounts the app.
- **Components, props and composition patterns** (`components_props`): A habit tracker needs a list, items, a form and a header, so they need to split the UI into reusable components and pass data and callbacks down.
- **useState, event handling, controlled forms and rendering lists** (`state_events_forms`): Adding, toggling and deleting habits requires state updates, controlled inputs, keys and immutable updates to arrays and objects.
- **useEffect and persisting state to localStorage** (`effects_localstorage`): Saving and loading habits needs side effects, dependency arrays, lazy state initialization and JSON serialization, which they already know. A custom useLocalStorage hook is a good fit.
- **Custom hooks, lifting state up and component patterns** (`custom_hooks_patterns`): Structuring the app cleanly means extracting reusable logic and deciding where state lives, a step toward maintainable code.
- **Build a habit tracker app in React end to end** (`build_habit_tracker`): A project video that builds a similar app with local storage ties all the concepts together and is the backbone of the plan.

## Watch in this order

### 1. [Learn React With This ONE Project](https://www.youtube.com/watch?v=G6D9cBaLViA)
Tech With Tim · 100 min · watch 06:02–40:00 · counts 34 min · beginner, project_build · covers react_mental_model_jsx, vite_setup, components_props, state_events_forms · **confidence 0.50**

Project-based start: the chapters for this stretch cover project setup, a template walkthrough, JSX and components, then a movie card component with conditional rendering, map() over a list and state. That fills the learner's missing JSX, components, props and list-rendering basics with a hands-on build instead of a lecture. The movie app is not a habit tracker, so the learner should map the patterns across.

> [00:00] “In this video, you'll learn React by walking through a practical project.” _(from chapters/description; no transcript)_
> [00:00] “We're going to use a real-world API that can fetch and display data, and cover all of the important React components and features.” _(from chapters/description; no transcript)_

_Confidence note: No transcript, so this rests on chapter titles. The off_topic flag (movie app) and the unverified Vite setup lower confidence. A transcript confirming Vite and props explanations would raise it._

### 2. [Build this to-do-list app with React! ☝](https://www.youtube.com/watch?v=9wiWzu_tRB0)
Bro Code · 23 min · counts 23 min · beginner, project_build · covers state_events_forms · **confidence 0.45**

A to-do list built using only useState, with chapters for setup, HTML structure, CSS and JS functions. It gives practice on the add/complete/delete-style state logic and event handlers a habit tracker needs, and avoids useEffect so it stays on this one concept. It is closer to a habit tracker's add/delete list than the movie app.

> [00:00] “This is a project you can write using React JS with only using the useState hook.” _(from chapters/description; no transcript)_

_Confidence note: No transcript, so form handling and Vite use are unconfirmed. The 7-minute CSS chapter is not essential. Transcript evidence of controlled inputs would raise confidence._

### 3. [Learn React With This ONE Project](https://www.youtube.com/watch?v=G6D9cBaLViA)
Tech With Tim · 100 min · watch 1:01:00–1:39:30 · counts 38 min · beginner, project_build · covers effects_localstorage · **confidence 0.40**

The chapters for this stretch cover calling APIs, useEffect, search and contexts. It teaches how useEffect and its dependency array work and shows a controlled search input, which the learner needs before wiring effects to localStorage. The learner already knows HTTP, so the fetch details can be skimmed.

> [00:00] “We're going to use a real-world API that can fetch and display data, and cover all of the important React components and features.” _(from chapters/description; no transcript)_

_Confidence note: Chapter list only, and the exact boundaries of the useEffect and context chapters are unknown. Part of the range is API and context material beyond the plan, so the fit is partial._

### 4. [React To-Do App Part 2: Local Storage + useEffect — Save Tasks Even After Refresh!](https://www.youtube.com/watch?v=UKgT7SuiieE)
Learn the Tech · 25 min · counts 25 min · beginner, other · covers effects_localstorage · **confidence 0.45**

Directly targets persisting a to-do task list: how useEffect works, localStorage vs sessionStorage, syncing tasks to localStorage and restoring them on refresh. That is the same persistence loop the habit tracker needs.

> [00:00] “Learn how to store your React To-Do app data permanently even after page refresh!” _(from chapters/description; no transcript)_
> [00:00] “Restore data when the page refreshes” _(from chapters/description; no transcript)_
> [00:00] “Understand how React state + localStorage work together” _(from chapters/description; no transcript)_

_Confidence note: Description only. It is Part 2 of a series whose Part 1 is not in the pool, so the learner may need to adapt the code to their own app. Unclear how hands-on it is._

### 5. [React.JS Interview Question:  useLocalStorage : Custom Hook](https://www.youtube.com/watch?v=4CU9uV8Hck0)
Adarsh Singh · 5 min · counts 5 min · intermediate, concept_explainer · covers custom_hooks_patterns · **confidence 0.40**

A short build of a reusable useLocalStorage hook combining useState, useEffect and JSON parse/stringify, loading saved data on mount. It turns the persistence logic just learned into the custom-hook pattern the habit tracker can reuse.

> [00:00] “In this video, we'll build a reusable useLocalStorage custom hook in React.js that keeps your React state synchronized with the browser's localStorage.” _(from chapters/description; no transcript)_
> [00:00] “Load previously saved data when the component mounts” _(from chapters/description; no transcript)_

_Confidence note: Description only, with an interview-question style that may be terse. Lifting state up and wider component patterns are not covered here._

### 6. [Build a Complete To-Do List App with React + Vite | Dashboard, Reminders & Local Storage Tutorial](https://www.youtube.com/watch?v=X92kk5iT8CM)
DevCrafted Learn-Build-Deploy · 27 min · counts 27 min · beginner, project_build · covers effects_localstorage, custom_hooks_patterns, build_habit_tracker · **confidence 0.45**

The closest end-to-end build in the pool: a React + Vite app with add/edit/delete/complete, form handling, a custom useLocalStorage hook and localStorage persistence. The learner can mirror it to make the habit tracker by swapping tasks for habits and adding daily or streak tracking.

> [00:00] “In this comprehensive tutorial, we'll create a feature-rich task management app with a modern dashboard, reminder notifications, and persistent storage.” _(from chapters/description; no transcript)_
> [00:00] “Learn how to build a professional To-Do List application from scratch using React + Vite!” _(from chapters/description; no transcript)_
> [00:00] “Custom Hook Creation (useLocalStorage)” _(from chapters/description; no transcript)_

_Confidence note: Description and feature list only, so teaching depth is unverified. At 27 minutes it is a fast build, and Tailwind adds styling noise. A transcript showing step-by-step explanation would raise confidence._

## Considered and dropped

- [React To-Do App Tutorial | Build a Todo List with CRUD in React JS | Frontend Project](https://www.youtube.com/watch?v=fsyfL33soRQ): The most complete CRUD plus localStorage to-do build, but flagged outdated_tooling (Create React App). It is disqualified because an unflagged video covers the same persistence and build topics.
- [CRUD Todo App | React Typescript Project | Create TODO Web App With ReactJs + Typescript | Tutorial](https://www.youtube.com/watch?v=gNEQ8PSkaI4): A Vite CRUD to-do with TodoList and TodoForm components, but built in TypeScript with no localStorage. This adds type syntax the learner has not asked for, and persistence is the key missing piece.
- [React JS 19 Full Course 2025 | Build an App and Master React in 2 Hours](https://www.youtube.com/watch?v=dCLhUialKPQ): At 127 minutes it is intermediate-level, and its project is a movie app with Tailwind and an API. It largely overlaps the movie-app material already picked, with no localStorage.
- [React Tutorial for Beginners](https://www.youtube.com/watch?v=SqcY0GlETPk): A beginner lecture-style course that appears to use TypeScript and has no effects or localStorage. It is weaker as a project-based fit for this learner.
- [React JSX , Babel, React Components & Props Explained from Scratch | ReactJS Full Course #2](https://www.youtube.com/watch?v=JdFUNKGwWLw): A concept-heavy explainer of JSX, Babel and props with no app built. It conflicts with the preference for project-based content.
- [Every React Concept Explained in 12 Minutes](https://www.youtube.com/watch?v=wIyHSOugGGw): Flagged surface_intro: a 12-minute survey of about 20 concepts, which is the kind of shallow overview the learner wants to avoid.
- [Vite Crash Course – Frontend Build Tool](https://www.youtube.com/watch?v=do62-z3z6FM): A 40-minute Vite tooling tour, mostly TypeScript, environment variables, builds and plugins. Only the first few minutes are relevant, and the picked project video already covers setup.
- [Save State to LocalStorage & Persist on Refresh with React.js](https://www.youtube.com/watch?v=rWfhwW9forg): A decent short localStorage hydration demo, but it persists a single banner value rather than a list. UKgT7SuiieE is closer to the habit tracker.
- [React Todo App Tutorial – Build with React Hooks from Scratch](https://www.youtube.com/watch?v=nwj4W4Em75A): A to-do app that appears to use useEffect to add and remove todos, which is a questionable pattern. It is redundant with the other to-do builds picked.
- [React Custom Hooks: useLocalStorage - Simply Explained!](https://www.youtube.com/watch?v=1uiNxQIpcLU): It appears to teach the useLocalStorage hook well, but is flagged too_advanced_for_learner and has no transcript. It is in a near-duplicate cluster with N7rs5F4f6FA, and neither was needed.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-5.5, select=anthropic/claude-sonnet-5.5 · cost $0.194 · 133 s_
