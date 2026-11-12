# Curriculum: Build a small React app this weekend, something like a habit tracker with local storage

**Budget:** 360 min · **Planned:** 185 min · **Videos:** 5 · **Candidates assessed:** 29

**How I read the goal:** In a weekend, go from zero React to a working habit tracker (add, toggle and delete habits, persisted in localStorage) built with Vite and modern hooks.

**Assumptions:** The habit tracker is a variation of the to-do and favorites apps in the videos: habits are items you add, toggle done and delete, with daily check-offs added on your own.; JavaScript with JSX is fine. Some videos use TypeScript, which you can ignore.; I could not see upload dates. I picked videos that show Vite and hooks, and left out the one flagged outdated_tooling.
> ⚠️ Only about 185 of the 360 minutes are used. The remaining time is for building your own habit tracker, which is the real test. I did not pad with weak or redundant videos.
> ⚠️ No video builds an actual habit tracker. The to-do and favorites builds are the closest, and you will need to add the daily check-off and streak logic yourself.
> ⚠️ Dropped Mosh's React tutorial: it is lecture-style with TypeScript, and the Tech With Tim project covers the same basics.
> ⚠️ Dropped Dawid's Todo App: it is flagged outdated_tooling, and the other project builds cover the same ground.
> ⚠️ Dropped Max Programming's localStorage video: it is a surface intro, and Cosden's hook video covers the same sub-topic in more depth.
> ⚠️ Dropped the 2–3 minute Vite setup clips and the 'React in 8/12 minutes' summaries: they are surface intros.

## Plan

- **Vite tooling and project structure** (`vite`): Replaces create-react-app. You need to scaffold, run and understand the project layout.
- **Components, JSX, props and useState** (`state`): These are the core React mental model. State is what the habits list lives in.
- **Guided React project: lists, events, useEffect, context** (`project`): Applies the basics in a full app with list rendering, conditional rendering and effects.
- **localStorage persistence and custom hooks** (`persist`): The key feature of the habit tracker. A reusable useLocalStorage hook is the idiomatic way to do it.
- **Build a CRUD tracker with local storage and a stats dashboard** (`build`): A second, smaller build close to the habit tracker, with forms, a dashboard and persistence.

## Watch in this order

### 1. [Vite Crash Course – Frontend Build Tool](https://www.youtube.com/watch?v=do62-z3z6FM)
freeCodeCamp.org · 40 min · counts 40 min · beginner, crash_course · covers vite · **confidence 0.70**

Covers Vite scaffolding, project structure, hot module replacement and production builds, which are the tooling gaps you named. The boilerplate it builds is a React app, so it gets you set up for the weekend.

> [00:00] “Vit is a next generation build tool that offers instant project startup and real-time updates”
> [02:04] “We learned how to build React apps with Vit, how to work with static assets, using environment variables, TypeScript”

_Confidence note: It is a tooling crash course rather than a project, but it is the only substantial Vite coverage I found._

### 2. [Learn React Hooks: useState - Simply Explained!](https://www.youtube.com/watch?v=V9i3cGD-mts)
Cosden Solutions · 8 min · counts 8 min · beginner, concept_explainer · covers state · **confidence 0.75**

A short, focused explanation of useState (state as data that changes over time, destructuring, setters in event handlers). It prepares you for the project builds.

> [00:20] “state the simplest way that you can think about this is data that changes with time”
> [02:07] “useState is the hook that you use in React to manipulate state”
> [06:47] “setCount and we're using this function to manipulate the state”

_Confidence note: Concept explainer, but short and beginner-level, and it feeds straight into the projects._

### 3. [Learn React With This ONE Project](https://www.youtube.com/watch?v=G6D9cBaLViA)
Tech With Tim · 100 min · counts 100 min · beginner, project_build · covers state, project · **confidence 0.85**

A project build that teaches components, JSX, useState, useEffect, lists, conditional rendering, context and localStorage-backed favorites. The favorites add/remove logic maps closely onto habit management.

> [03:37] “Everything revolves around something called a component. Now a component is really just a part of your application”
> [12:55] “JSX simply means kind of a combination of JavaScript and HTML. And you'll see that we have some things that look like HTML”
> [46:53] “When a state change occurs, the entire component is reran or rerendered. So if we just define something as a normal variable”
> [1:21:15] “A context will allow state to be globally available to anything that's within the provided context”

_Confidence note: The movie API part is not needed for your app, but the rest is directly relevant._

### 4. [React Custom Hooks: useLocalStorage - Simply Explained!](https://www.youtube.com/watch?v=1uiNxQIpcLU)
Cosden Solutions · 10 min · counts 10 min · intermediate, project_build · covers persist · **confidence 0.80**

Builds a reusable useLocalStorage custom hook with JSON serialization and try/catch. This is the component pattern to use for habit persistence.

> [00:21] “we are going to create a hook called use local storage that is going to expose to us three different functions”
> [03:13] “window local storage set item we're going to give it the key that we have here and then we're going to do json stringify”
> [09:55] “any component that wants to make use of the local storage can just use this hook directly and get access to all of these functions”

_Confidence note: Uses TypeScript typing, which is a small hurdle. It is the second Cosden video, within the two-per-creator limit._

### 5. [Build a Complete To-Do List App with React + Vite | Dashboard, Reminders & Local Storage Tutorial](https://www.youtube.com/watch?v=X92kk5iT8CM)
DevCrafted Learn-Build-Deploy · 27 min · counts 27 min · beginner, project_build · covers build, persist · **confidence 0.80**

A Vite + React to-do build with add, edit and delete, a stats dashboard and local storage. It is the closest match to the habit tracker and works as a template for your own build.

> [00:00] “we are going to build a to-do list app using React plus white”
> [00:00] “we have a dashboard for showing our total task completed task pending task and overdue”
> [20:26] “use local storage so I'll copy this and I'll paste this”
> [26:19] “you can see the things are getting added and once you click on this it is incomplete”

_Confidence note: Short and fast-paced. It uses Tailwind, which is extra to learn but optional._

_Models: agent_loop=anthropic/claude-sonnet-5.5 · cost $0.157 · 64 s_
