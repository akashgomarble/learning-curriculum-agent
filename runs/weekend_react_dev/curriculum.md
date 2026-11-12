# Curriculum: Build a small React app this weekend, something like a habit tracker with local storage

**Budget:** 360 min · **Planned:** 189 min · **Videos:** 4 · **Candidates assessed:** 29

**How I read the goal:** By the end of the weekend, the learner has built and run a working habit tracker in React (Vite) that persists data to localStorage, and understands the hooks and component patterns behind it.

**Assumptions:** Habit tracker means: add/delete habits, mark them complete per day, view streaks, with data persisted in localStorage; The 360 minutes is pure watching time, so a long project build video can serve as the backbone; Plain JavaScript (not TypeScript) is fine since the learner knows JS fundamentals but did not mention TypeScript; Modern function components and hooks only; class components are not needed; The 'nothing before 2022' constraint is handled by the later video-selection step using upload dates; the exclusions here cover title-based filters only
> ⚠️ The picks total about 189 of 360 minutes (about 52%), leaving about 171 minutes unused. The remaining candidates are flagged for conflicts with your constraints (create-react-app, pure-theory or surface-intro) or only repeat topics already covered, and I preferred under-filling to padding.
> ⚠️ No candidate teaches habit streak logic, such as consecutive-day calculation, so you will need to write that yourself; sub-topic polish_deploy is only partly covered.
> ⚠️ No video here covers lifting state up in depth. You get it only implicitly through the project builds and the Context API.
> ⚠️ Tech With Tim's project fetches a movie API and uses react-router, which a habit tracker doesn't need. Focus on the useState, useEffect and Context/localStorage sections.
> ⚠️ The do62-z3z6FM range (2:45 to 21:04) comes from an overlapping segment map, so adjust a few seconds if it starts mid-sentence.
> ⚠️ The DevCrafted to-do video lists 27 minutes but its segments suggest about 41 minutes, so the real watch time may be longer. Even then the total stays under budget.
> ⚠️ The habit trackers found in the pool use Redux or Next.js, or date from before 2022. I left them out because you asked for Vite and the hooks-based approach.

## Plan

- **Vite project setup and React project structure** (`vite_setup`): The learner knows npm but not Vite; they need to scaffold a modern React project and understand the folder layout, dev server and build, instead of using create-react-app.
- **JSX and function components with props** (`jsx_components`): As a JS-literate backend dev, they need the mental model of JSX as JS expressions plus component composition and props to build UI.
- **State with useState and event handling** (`state_events`): A habit tracker is driven by state (habits list, completion toggles); they need immutable updates of arrays/objects and form handling.
- **useEffect and persisting state to localStorage** (`effects_localstorage`): Persistence is a core requirement; they need to understand effects, dependency arrays, lazy state initialization and JSON serialization (which they already know).
- **Component patterns: lifting state up, lists and keys, custom hooks** (`component_patterns`): To structure a multi-component app cleanly, they need to share state between components, render lists correctly, and extract a reusable useLocalStorage hook.
- **Build a habit tracker / similar small app end-to-end** (`project_build`): Following a project build ties all concepts together and mirrors the weekend goal; it is the backbone of the plan.
- **Streak logic, styling and finishing touches** (`polish_deploy`): The learner needs to adapt the tutorial project into their own habit tracker by adding date-based completion and streak calculation.

## Watch in this order

### 1. [Vite Crash Course – Frontend Build Tool](https://www.youtube.com/watch?v=do62-z3z6FM)
freeCodeCamp.org · 40 min · watch 02:45–21:04 · counts 18 min · beginner, crash_course · covers vite_setup · **confidence 0.80**

Covers scaffolding a React project with npm create vite, the dev server and hot module replacement, and creating components, which is the Vite tooling you haven't used. Only the setup-to-useEffect part is needed, so you skip the TypeScript config and the Vite internals talk.

> [00:00] “Vit is a next generation build tool that offers instant project startup and real-time updates”
> [02:04] “We learned how to build React apps with Vit, how to work with static assets, using environment variables, TypeScript”

_Confidence note: Unflagged and clearly shows Vite setup. Its segment map has overlapping timestamps, so the range boundaries are approximate. The project may lean toward TypeScript._

### 2. [Learn React With This ONE Project](https://www.youtube.com/watch?v=G6D9cBaLViA)
Tech With Tim · 100 min · counts 100 min · beginner, project_build · covers jsx_components, state_events, effects_localstorage, component_patterns · **confidence 0.85**

A project-based Vite build that teaches JSX, components and props, useState re-rendering, mapping lists, useEffect, and React Context with localStorage persistence for a favorites list. That list is structurally close to tracking habits. It is the main backbone for the core concepts.

> [12:55] “JSX simply means kind of a combination of JavaScript and HTML. And you'll see that we have some things that look like HTML”
> [46:53] “When a state change occurs, the entire component is reran or rerendered. So if we just define something as a normal variable”
> [1:21:15] “A context will allow state to be globally available to anything that's within the provided context”

_Confidence note: Plain JS, Vite and modern hooks, and it covers four sub-topics. The movie API and routing are tangential to a habit tracker. The segment map ends at 1:19:30 although the video runs 99.5 minutes._

### 3. [LocalStorage in React Using Custom Hook | The Complete React Course | Ep.41](https://www.youtube.com/watch?v=5uHikv1oBEI)
Anurag Singh ProCodrr · 44 min · counts 44 min · intermediate, project_build · covers effects_localstorage, component_patterns · **confidence 0.80**

Builds a reusable useLocalStorage custom hook in an expense tracker and swaps useState for it across several form fields. It also fixes an infinite render loop with useEffect. This is the custom-hook pattern you will need to persist habits.

> [01:50] “we will make a custom hook of react name it useLocalStorage and with that hook we will implement local storage”
> [29:40] “we have made custom hook, we just changed use state to use local storage and the local storage need a key”

_Confidence note: Unflagged, project-based, and directly on persistence and custom hooks. It is somewhat long for one hook, and Vite is only implied._

### 4. [Build a Complete To-Do List App with React + Vite | Dashboard, Reminders & Local Storage Tutorial](https://www.youtube.com/watch?v=X92kk5iT8CM)
DevCrafted Learn-Build-Deploy · 27 min · counts 27 min · beginner, project_build · covers project_build, polish_deploy · **confidence 0.70**

A complete React + Vite to-do app with add, edit and delete, completion state, localStorage persistence and a statistics dashboard. It is the closest modern end-to-end analogue to a habit tracker, and its Tailwind styling covers the finishing touches. Watch it after the concepts so you can adapt it to habits.

> [00:00] “we have a dashboard for showing our total task completed task pending task and overdue”
> [20:26] “use local storage so I'll copy this and I'll paste this”
> [26:19] “you can see the things are getting added and once you click on this it is incomplete”

_Confidence note: The project fits well, but it is a task app, not a habit tracker, and has no streak logic. Its metadata says 27 minutes while its segment map runs to about 41 minutes, so the time estimate is uncertain._

## Considered and dropped

- [Build a Todo App with React.js | Beginner React Project using hooks](https://www.youtube.com/watch?v=QdTHUv79EZc): Strong todo build with useState, useEffect and localStorage, but it is set up with create-react-app (flagged outdated_tooling), which you ruled out. Unflagged Vite builds cover the same sub-topics.
- [React Tutorial for Beginners](https://www.youtube.com/watch?v=SqcY0GlETPk): A long TypeScript lecture flagged pure_theory built around a ListGroup demo, not a project. Plain-JS project builds already cover props, lists and state.
- [React Tutorial & Vite in 2025: Your First Project From Scratch! (The Easy Way)](https://www.youtube.com/watch?v=wyC25aCGdwk): Vite setup walkthrough flagged surface_intro. The Vite crash course covers the same setup more deeply.
- [Learn React Hooks: useState - Simply Explained!](https://www.youtube.com/watch?v=V9i3cGD-mts): Good useState counter explainer, but it overlaps with the useState coverage in the Tech With Tim build and adds a short isolated demo.
- [ReactJS Tutorial 81: Creating Our Own useLocalStorage Hook In ReactJS](https://www.youtube.com/watch?v=wKjsnUIfGHI): A useLocalStorage hook on a login form that covers the same ground as the expense-tracker hook video, with a less relevant example.
- [Learn How to Use Local Storage in React With an Easy-to-Understand Example](https://www.youtube.com/watch?v=N7rs5F4f6FA): Flagged surface_intro; it shows a counter plus a library hook, and the hook video builds the same idea from scratch.
- [Understand Any React Project in 16 Minutes | Vite + React + TypeScript Folder Structure Explained](https://www.youtube.com/watch?v=8ub_3kjILV8): A TypeScript folder-structure explainer flagged pure_theory; it is not project-based and the Vite coverage is already sufficient.
- [React JS Tutorial for Beginners | Setup React with Vite & Understand Project Structure](https://www.youtube.com/watch?v=CU5cyEeCCBs): A 63-minute lecture flagged pure_theory covering Virtual DOM theory and Vite setup, which conflicts with your preference for project-based content.
- [A Habit Tracker App Using React Redux](https://www.youtube.com/watch?v=7VPULX3WcGE): A habit tracker demo built on Redux, flagged too_advanced_for_learner. It is a short walkthrough, not a build-along tutorial.
- [Functional Components & Props & useState Hook](https://www.youtube.com/watch?v=orLqzKffcXo): A pure-theory CodeSandbox lecture on components, props and useState, dated 2022; redundant with the project builds.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.115 · 53 s_
