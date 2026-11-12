# Curriculum: Get comfortable with Rust ownership, borrowing and lifetimes so I can port a small Go CLI tool

**Budget:** 240 min · **Planned:** 179 min · **Videos:** 11 · **Candidates assessed:** 36

**How I read the goal:** After about 4 hours of watching, the learner can reason about Rust ownership, borrowing and lifetimes with confidence, use Result and the ? operator idiomatically, and port their small Go CLI tool to Rust.

**Assumptions:** The learner needs enough Rust syntax and tooling (cargo, structs, enums, match) to follow videos, but this is covered by mapping from Go rather than taught from scratch.; Traits are needed mainly as they relate to error handling, generics bounds and lifetimes, not as a full deep dive.; The ported CLI uses typical pieces: argument parsing (e.g. clap), file or stdin IO, and error propagation.; Videos in English; the learner prefers material aimed at experienced developers coming from Go, C, or C++.
> ⚠️ Budget use is about 191 of 240 minutes (about 80%); roughly 49 minutes are unused. I chose not to pad with repetitive ownership/lifetimes videos or sprawling talks, and I could not widen the OcaerPp59Gs range further without leaving the relevant content.
> ⚠️ The Go-specific orientation is brief (pDM_5HT2UlU, about 7.5 minutes and flagged surface_intro). Expect to look up Rust syntax details such as cargo, struct/enum/match and Option as you go.
> ⚠️ Traits get only moderate coverage and are split across several videos (traits_basics, with From and Error mostly in the Result videos). This is enough for error handling but not a full trait deep dive.
> ⚠️ Some cards have segment maps whose timestamps do not match the stated duration (for example VFIOSWy93H0 and OcaerPp59Gs). I picked full videos wherever possible, and the one watch range (OcaerPp59Gs, 38:20-1:01:40) should be checked against the actual video.
> ⚠️ The pick gRAVZv7V91Q is conceptual and best watched after 178uniabkag; it may feel abstract before you have seen lifetime annotations in code.
> ⚠️ Structs holding references and lifetimes in methods get relatively brief coverage; uvP1bKTfa_Q shows a practical example, but you may want to practice on your own code.
> ⚠️ uvP1bKTfa_Q has an upload date that appears to be in the future (20261015) in the card metadata. I assumed the date is a data quirk and the content is valid.

## Plan

- **Rust orientation for Go developers (cargo, structs, enums, match, Option)** (`rust_for_go_devs`): Gives the minimum Rust vocabulary and tooling to follow ownership examples, mapped onto Go concepts they already know, without re-teaching variables or loops.
- **Ownership and moves (stack vs heap, move semantics, Copy vs Clone, Drop)** (`ownership_moves`): Go's GC hides ownership; this learner knows pointers and memory so can grasp move semantics quickly, but must internalize who owns and frees data.
- **Borrowing and references in depth (shared vs mutable borrows, borrow checker rules, common errors)** (`borrowing_refs`): They want depth on the borrow checker; they need to understand aliasing XOR mutability and how to fix typical compiler errors, contrasted with Go pointers and slices.
- **Lifetimes (annotations, elision rules, structs holding references, 'static)** (`lifetimes`): Lifetimes are the hardest part for newcomers and are needed for structs and functions that return references, such as parsed CLI config.
- **Traits and generics essentials (impl Trait, trait bounds, From, Display, Error trait)** (`traits_basics`): Idiomatic error handling relies on traits such as std::error::Error, From and Display, which are unlike Go interfaces in key ways.
- **Error handling with Result and the ? operator (custom error types, thiserror, anyhow, From conversion)** (`result_error_handling`): Their Go CLI returns errors everywhere, so they need to translate if err != nil patterns into Result, ?, and custom or anyhow errors.
- **Build a Rust CLI project (clap, file IO, error propagation, ownership in practice)** (`build_cli_port`): A project-style walkthrough shows ownership, borrowing, lifetimes and Result working together in a tool like the one they are porting.

## Watch in this order

### 1. [Rust for Go Developers: The 6 Things You Actually Need to Learn](https://www.youtube.com/watch?v=pDM_5HT2UlU)
Masa Tech Team · 8 min · counts 8 min · intermediate, concept_explainer · covers rust_for_go_devs · **confidence 0.60**

A short orientation written for Go developers. It maps ownership, borrowing, Result/Option and the ? operator onto what a Go engineer already knows, and it frames the compiler as a teaching tool. It is a light overview (flagged surface_intro), but it is the only candidate aimed at Go developers. Skip the async/Tokio and crate-ecosystem sections.

> [01:04] “Who owns this data right now? The string's ownership moved into the prepare job function.”
> [01:04] “If the function only needs to read the text, borrow it. We change the parameter to a borrowed string slice.”
> [05:17] “When a borrow fails, identify which value owns the data. When a future isn't send, inspect what state is being held.”

_Confidence note: Right audience, but shallow. It only sets the stage for the rest. Confidence would be higher if a longer Go-to-Rust bridge video existed._

### 2. [Understanding Ownership in Rust](https://www.youtube.com/watch?v=VFIOSWy93H0)
Let's Get Rusty · 26 min · counts 26 min · intermediate, concept_explainer · covers ownership_moves, borrowing_refs · **confidence 0.80**

Walks through the ownership rules, move vs Copy, Drop, passing and returning ownership, then references and the one-mutable-reference rule, with compiler errors shown. It gives the mechanics of moves and Drop that the Go learner lacks. The unflagged transcript shows it staying at a working-programmer level.

> [07:08] “each value in rust has a variable that's called its owner so one variable one owner”
> [13:11] “instead of calculate length taking a string we'll make it take a reference to a string”
> [14:59] “you can only have one mutable reference to a particular piece of data in a particular scope”

_Confidence note: Clear, complete coverage of moves and basic borrowing. The stack/heap section is partly review for this learner._

### 3. [The promise of Rust](https://www.youtube.com/watch?v=zo6yZisg7N0)
fasterthanlime · 29 min · counts 29 min · intermediate, concept_explainer · covers ownership_moves, borrowing_refs · **confidence 0.80**

Contrasts Rust's moves and borrows with Go and JavaScript semantics. It explains the aliasing-XOR-mutability rule behind the borrow checker and where the checker is too conservative, plus the Rc/RefCell and Arc/Mutex escape hatches. This gives the depth on the borrow checker the learner asked for. Skip the sponsored segment.

> [00:42] “Copy trait. i64 does implement Copy because copying an integer from one register to another is very fast.”
> [01:03] “String type specifically with a capital S refers to a valid UTF-8 sequence stored somewhere on the heap.”
> [23:15] “Rust compiler rejects an infinity of programs that are memory safe and useful, but that it simply isn't able to verify as such.”

_Confidence note: Strong fit for a senior Go developer. It overlaps somewhat with the previous video on moves, which is deliberate reinforcement._

### 4. [The Secret Behind Rust’s Memory Safety: The Borrow Checker EXPLAINED](https://www.youtube.com/watch?v=hmefR4tE_H4)
Open Source · 5 min · counts 5 min · intermediate, concept_explainer · covers borrowing_refs · **confidence 0.65**

A compact drill on the borrow checker's one-mutable-or-many-immutable rule, scoped borrows, dangling references and common errors with fixes. It consolidates the rules before lifetimes and bridges into reference lifetime tracking.

> [01:03] “you can have either one mutable reference or any number of immutable references, but not both at the same time”
> [01:45] “the borrow checker uses lifetime analysis to figure out how long references live and ensures that no reference outlives the data it points to”
> [02:49] “the borrow checker ensures you're not using data while it's mutably borrowed elsewhere”

_Confidence note: Short and some overlap with earlier picks. It is useful as a consolidation of common errors._

### 5. [Rust Lifetimes Explained — Finally Make Sense of 'a (2026)](https://www.youtube.com/watch?v=178uniabkag)
Aarambh Dev Hub · 14 min · counts 14 min · intermediate, concept_explainer · covers lifetimes · **confidence 0.80**

Frames lifetime annotations as describing relationships between references, not controlling memory. It covers the longest() problem, the three elision rules, struct lifetimes, 'static and higher-ranked bounds. It is the unflagged member of its near-duplicate cluster.

> [03:28] “Lifetime annotations do not change how long a value lives. They do not control memory. They do not affect runtime behavior in any way.”
> [05:34] “By marking both inputs and the output with tick a, you are telling the compiler that the returned reference will live at least as long as the shorter of the two inputs.”
> [12:37] “Static does not mean forever. It means contains no borrowed references that could become invalid.”

_Confidence note: Covers every lifetime sub-topic in the plan. Structs holding references get only a brief treatment._

### 6. [Rust Powered Polymorphism ⚡️ With Traits](https://www.youtube.com/watch?v=CHRNj5oubwc)
Code to the Moon · 10 min · counts 10 min · intermediate, concept_explainer · covers traits_basics · **confidence 0.65**

Explains traits as Rust's analogue of interfaces, covering default implementations, static dispatch with generics vs dynamic dispatch with dyn, and supertraits. This maps directly onto Go interfaces and gives the trait background needed for error types. Flagged surface_intro, but it is short and no unflagged candidate covers dyn vs generics.

> [03:03] “instead of interfaces Rust has something called traits which are very similar to interfaces but with some subtle differences”
> [04:28] “dyn refers to something called Dynamic dispatch which is in contrast to something called Static dispatch”

_Confidence note: Good Go-interface mapping, but light on trait bounds and From/Display, which the next picks cover._

### 7. [Introduction to Generics and Traits | Advanced Rust Part 1](https://www.youtube.com/watch?v=AnsRR-i5UWQ)
Green Tea Coding · 16 min · counts 16 min · intermediate, concept_explainer · covers traits_basics · **confidence 0.60**

Covers generic functions, trait bounds, why the compiler demands bounds like Copy/Add, and how to implement traits manually. This supplies the bounds mechanics that Display/From/Error-based error handling relies on. Flagged pure_theory, but that does not conflict with this learner's constraints.

> [06:10] “traits or interfaces as they are called in most other languages are Concepts that guarantee that an object or struct provides a certain functionality”
> [08:40] “we need to make sure that the copy trait is implemented and we do this by adding the copy trait as a requirement for our type T”

_Confidence note: The generic sum example is basic for a Go developer who already knows generics, but the bounds material is needed. Remaining trait topics (From, Display, Error) come from the Result videos._

### 8. [A Simpler Way to See Results](https://www.youtube.com/watch?v=s5S2Ed5T-dc)
Logan Smith · 19 min · counts 19 min · intermediate, concept_explainer · covers result_error_handling, traits_basics · **confidence 0.80**

Builds Result from sum types, then covers the ? operator, collecting Results, designing custom error types and combining errors with From. It also shows thiserror and anyhow. This is the closest match to Go's if err != nil pattern and gives the conceptual model of idiomatic Result use.

> [09:50] “the question mark is a unary post-fix operator so you use it like this”
> [12:01] “if all the results are okay you get back an OK VEC but if any of them fails the whole thing fails”
> [15:57] “I would personally use the this error crate to derive a bunch of nice trait implementations all at once”

_Confidence note: Covers custom error types and From conversion with depth. thiserror/anyhow are covered more briefly here, so the next video fills that in._

### 9. [Rust Error Handling Explained: thiserror vs anyhow (Best Practices)](https://www.youtube.com/watch?v=-c9JEexiHPE)
Semicolon · 16 min · counts 16 min · intermediate, concept_explainer · covers result_error_handling · **confidence 0.75**

Compares thiserror (typed enum errors for libraries) with anyhow (context-based errors for applications), with examples and a rule of thumb for choosing. This tells the learner which to use in the ported CLI.

> [14:33] “use this error when you are building libraries and crates and use anyhow when you are building applications”
> [14:55] “if it's very straightforward into the face just use anyhow if you require more complex handling then I would prefer this error”

_Confidence note: Practical and unflagged. The segment map has timestamp irregularities, so it is slightly less certain which sections are covered._

### 10. [Build a Rust CLI Tool from Scratch (clap, serde, anyhow) – logscan](https://www.youtube.com/watch?v=uvP1bKTfa_Q)
Back To Code · 13 min · counts 13 min · intermediate, project_build · covers build_cli_port, lifetimes, borrowing_refs · **confidence 0.80**

Builds a log-analysis CLI with clap and anyhow, and uses zero-copy parsing with &str lifetimes. It confronts a real borrow-checker error (E0515) and fixes it by moving ownership up to the caller. This is ownership and lifetimes applied in the CLI shape the learner is porting.

> [03:59] “Time and message are string slices ampersand STR that borrow directly from the file's text instead of copying it. That's zero copy parsing and it's very fast.”
> [05:23] “The idiomatic fix, move ownership up. Let the caller own the text and only borrow from it. The string lives in main, which outlives everything else.”
> [05:44] “Data must live at least as long as anything that borrows it. When the borrow checker complains, ask yourself, who owns this, and does it live long enough?”

_Confidence note: Excellent fit. The only concern is that it is short, so it only sketches the project structure._

### 11. [🚀 Build a Robust CLI App in Rust with Clap | Rust Programming Tutorial](https://www.youtube.com/watch?v=OcaerPp59Gs)
Easy Dev For All · 70 min · watch 38:20–1:01:40 · counts 23 min · intermediate, project_build · covers build_cli_port, result_error_handling · **confidence 0.65**

The chosen range shows the config-handling commands taking references to an AppConfig (ownership in practice), then Result and anyhow error propagation with ? in a clap CLI. This is the longer, more realistic project code after the compact logscan example. The setup and async/Tokio parts are skipped.

> [01:45] “anyhow so this would um allow me to handle errors much more easily and elegantly”
> [45:15] “it's going to just take one thing more or less so it will take this config which should be of type so be a reference to app config”

_Confidence note: Only part of a 70-minute tutorial is used. The range is based on the segment map, and the exact fit would need checking against the video._

## Similar videos: why only one made the cut

- kept `178uniabkag` over `juIINGuZyBc` (both cover lifetime annotations, lifetime elision rules, struct with references, static lifetime): It is unflagged and adds the loans mental model and higher-ranked bounds, which suit a learner who wants borrow-checker depth. juIINGuZyBc covers the same annotation and elision content and is flagged pure_theory.
- kept `178uniabkag` over `3R2Emr5TfV0` (both cover lifetimes, lifetime elision rules, static lifetime, lifetimes in structs): It covers the same topics in more depth with worked reasoning about annotations and elision rules, while 3R2Emr5TfV0 is a brief summary.

## Considered and dropped

- [Understanding Rust – Or How to Stop Worrying & Love the Borrow-Checker • Steve Smith • YOW! 2024](https://www.youtube.com/watch?v=zfb1y8yn8QI): A strong talk on the borrow checker and lifetimes, but it spends much time on Rc, Send/Sync, async and threads, which are beyond the plan. Its segment map extends well past the stated duration, so a safe watch range is hard to define. The lifetimes picks already cover the plan's needs.
- [Rust Lifetimes Finally Explained!](https://www.youtube.com/watch?v=juIINGuZyBc): Same lifetimes cluster as the kept video. It covers annotations, elision, structs and 'static but is flagged pure_theory, while 178uniabkag is unflagged and adds the loans model and higher-ranked bounds.
- [Rust Lifetimes Explained Clearly | Borrow Checker, References & Lifetimes | Learn Rust Step by Step](https://www.youtube.com/watch?v=3R2Emr5TfV0): Same lifetimes cluster. It is a brief summary, so it adds nothing beyond the kept video.
- [Rust Lifetimes explained Tutorial](https://www.youtube.com/watch?v=S-SkEA4QWWE): A solid, unflagged lifetimes tutorial, but it repeats the elision and annotation material already covered by 178uniabkag. A third lifetimes video would be redundant.
- [Rust: Ownership and Borrowing, By Rodrigo Boniatti](https://www.youtube.com/watch?v=9vynzAEhvXo): Good ownership and borrowing walkthrough, but it duplicates VFIOSWy93H0 and zo6yZisg7N0, and adding a third creator on the same ground is redundant.
- [Mastering Error Handling in Rust: From Panics to thiserror & anyhow | with Nathan Stocks](https://www.youtube.com/watch?v=sZV6sz4P6QY): A 74-minute error handling webinar. It is strong on thiserror/anyhow but is too long for the thin remaining slot, and its segment map is gappy and unreliable, so a clean watch range cannot be chosen.
- [Rust: Generics, Traits, Lifetimes](https://www.youtube.com/watch?v=JLfEiJhpTbE): A broad generics/traits/lifetimes lecture of 36 minutes. It is mostly basic generics and repeats lifetimes material, which is less efficient than the targeted picks.
- [Rust Generics, Traits & Lifetimes Explained — Book Chapter 10 Project](https://www.youtube.com/watch?v=p2uAN6SJorA): A task-manager project that mostly covers basic generics and trait impls at beginner level. Its lifetimes coverage is only an overview, so it adds little beyond the chosen trait videos.
- [Rust Error Handling: The ? Operator, thiserror & anyhow](https://www.youtube.com/watch?v=6WykcOk78sc): Marked too_advanced_for_learner. It is a sprawling architecture talk with only a brief error handling segment.
- [🦀 Master Rust Programming #12 | Build CLI with CLAP Crate & Publish to Crates.io | Cargo Deep Dive 🚀](https://www.youtube.com/watch?v=oOaclyKsrjw): Marked off_topic. It focuses on publishing crates, workspaces and docs rather than ownership or error handling.

<details><summary>Filtered before assessment (29)</summary>

- Go vs. Rust: "This was super easy" (prefilter): too short (30s)
- Why Beginners Should AVOID Rust #programming #coding #software (prefilter): too short (52s)
- Learn Rust with one Easy Trick (prefilter): too short (31s)
- programming language, speed compilation #c++ #golang #rust (prefilter): too short (30s)
- Rust Or Go #coding #programming (prefilter): too short (49s)
- Rust Interior Mutability - Sneaking By The Borrow Checker (prefilter): pool cap reached
- Rust's lifetimes made easy (prefilter): pool cap reached
- AM Coder - 100 Days of Rust and Go - #10 - Object Oriented Programming in Rust and Go (prefilter): pool cap reached
- Rust Error Handling Like a Pro: thiserror vs anyhow (Patterns) (prefilter): pool cap reached
- Build a simple Command Line Interface (CLI) in Rust - Full Crash Rust Tutorial for Beginners (prefilter): pool cap reached
- The Rust language: memory, ownership and lifetimes (prefilter): pool cap reached
- Webinar Live | The Rust Borrow Checker: A Deep Dive - Nell Shamrell-Harrington (prefilter): pool cap reached
- Structs in Rust (prefilter): pool cap reached
- Rust Book Club #10: Generics, Traits & Lifetimes (prefilter): pool cap reached
- Rust Error Handling - Best Practices (prefilter): pool cap reached
- Parse Rust CLI Args With Clap 🦀 Rust Tutorial (prefilter): pool cap reached
- 🦀Master Rust Programming #2 | Ownership, Borrowing, References, Slices & Structs | Full Course 2025🚀 (prefilter): pool cap reached
- Rust for the impatient (prefilter): pool cap reached
- Traits: Defining Shared Behavior | Rust Book (prefilter): pool cap reached
- Rust - Anyhow (prefilter): pool cap reached
- Build CLI Tools in Rust with Clap for Easy Distribution (prefilter): pool cap reached
- Rust Traits Tutorial for Beginners IN HINDI (language): transcript is 'hi', learner needs 'en'
- Syntax of Generic Types, Traits, and Lifetimes | Rust Book (language): transcript is 'hi', learner needs 'en'
- The Rust Survival Guide (prefilter): pool cap reached
- Rust Ruined My Career (I Can't Go Back) (prefilter): pool cap reached
- Why Generics in Structs Are Essential in Rust (prefilter): pool cap reached
- Rust Error Handling Tutorial: thiserror, anyhow, and the Source Chain You're Losing (prefilter): pool cap reached
- Writing a CLI App in Rust! - Part 1 (prefilter): pool cap reached
- Understanding Rust's Memory Safety: Ownership, Borrowing, and Lifetimes #9 | Build on Rust (prefilter): pool cap reached

</details>

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.172 · 81 s_
