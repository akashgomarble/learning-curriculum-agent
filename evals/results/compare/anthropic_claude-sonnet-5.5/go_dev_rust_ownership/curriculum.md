# Curriculum: Get comfortable with Rust ownership, borrowing and lifetimes so I can port a small Go CLI tool

**Budget:** 240 min · **Planned:** 225 min · **Videos:** 7 · **Candidates assessed:** 36

**How I read the goal:** Within 240 minutes of watching, the learner understands Rust ownership, borrowing and lifetimes deeply enough to reason about the borrow checker, and can use traits and Result well enough to port a small Go CLI tool to Rust.

**Assumptions:** The learner has little or no Rust syntax beyond what transfers from C-like languages, so a brief Rust-specific syntax orientation is folded into the ownership material rather than taught as a separate topic.; Porting a small Go CLI implies argument parsing, file or stdin I/O, and error propagation, so a CLI-style project video is the plan's backbone.; Traits and Result are included because they are needed for the port, though the emphasis (about 60% of the budget) is on ownership, borrowing and lifetimes.; The learner has no interest in beginner material, so videos aimed at complete programming novices are undesirable.
> ⚠️ None of the 36 candidates has a transcript. Every pick rests on chapter lists and descriptions, so confidence is moderate across the board. Skim the first few minutes of each video and swap it out if it is too basic.
> ⚠️ Total picked viewing time is about 225 minutes of the 240-minute budget (about 94%), leaving about 15 unused minutes. I did not pad the rest with weak or redundant videos.
> ⚠️ Coverage of traits compared with Go interfaces is thin. Ns-GgnxN7HY is a general generics and traits lecture, so you will need to map traits to Go interfaces yourself.
> ⚠️ The CLI sub-topic gets only one 13-minute project video. It covers clap and anyhow but probably not much file or stdin I/O. Expect to consult the clap docs for the port.
> ⚠️ The ownership video (79phqVpE7cU) is intermediate but may feel basic in places. Skim past the early Strings material if it repeats what you already know.
> ⚠️ The Ryan Levick lifetimes stream is long and advanced, so you can watch it in two sittings. It is the main depth source for lifetimes and the borrow checker.

## Plan

- **Ownership and moves (vs Go's GC and value copies)** (`ownership_moves`): As a Go dev used to the garbage collector and implicit copying, the learner needs a new mental model of single ownership, moves, Copy vs Clone, and drop/RAII, which maps to their systems and memory knowledge.
- **Borrowing and references: shared vs mutable, borrow checker rules** (`borrowing_refs`): Rust references look like Go pointers but come with aliasing-XOR-mutability rules. Depth here is the learner's stated priority, including common compiler errors and how to restructure code to satisfy the checker.
- **Lifetimes: annotations, elision rules, structs holding references** (`lifetimes`): Lifetimes have no Go equivalent. The learner wants depth, so they need to understand why annotations exist, elision rules, lifetimes in structs and functions, and 'static.
- **Traits and generics (compared to Go interfaces and generics)** (`traits_generics`): Traits are central to idiomatic Rust and to the standard library APIs a CLI port uses. The learner can map them to Go interfaces but must learn trait bounds, impl blocks, derive and dyn vs generics.
- **Error handling with Result, the ? operator, and custom error types** (`result_errors`): Go's if err != nil pattern maps onto Result and ?, but the learner must learn Option/Result, From conversions, and crates like anyhow and thiserror for CLI tools.
- **Building a CLI tool in Rust (clap, file I/O, error propagation)** (`cli_port_project`): The final goal is porting a Go CLI, so seeing ownership, borrowing, traits and Result applied in a realistic command-line project cements the concepts and covers the tooling (cargo, clap).

## Watch in this order

### 1. [Rust: What is Ownership and Borrowing?](https://www.youtube.com/watch?v=79phqVpE7cU)
Gary Explains · 20 min · counts 20 min · intermediate, concept_explainer · covers ownership_moves, borrowing_refs · **confidence 0.55**

Intermediate-level explainer on ownership: moves with Strings, clone, and mutable references passed to functions. It gives a Go developer the move-vs-copy mental model without teaching what a variable is. Chapters also show a `clone` discussion that fits the 'don't clone to dodge the checker' habit.

> [00:00] “It can be a little tricky to understand, but once you do you will understand why Rust is called a memory safe language.” _(from chapters/description; no transcript)_
> [03:02] “Each bit of data, e.g. "hello", has an owner” _(from chapters/description; no transcript)_
> [12:27] “Clone is your friend, but not an excuse for sloppy code” _(from chapters/description; no transcript)_

_Confidence note: Only chapters and description are visible, with no transcript. Depth on shared vs mutable borrow rules is unverified, so the next two picks add borrow-checker depth._

### 2. [How to fight Rust's borrow checker... and win.](https://www.youtube.com/watch?v=Pg07HQJ0tvI)
Let's Get Rusty · 8 min · counts 8 min · intermediate, other · covers borrowing_refs · **confidence 0.50**

Intermediate talk on handling borrow-checker errors (understand the errors, restructure code, avoid fights). It targets the learner's wish for depth on the borrow checker rather than basics.

> [00:00] “Getting bombarded with compile time errors is all too common when writing Rust.” _(from chapters/description; no transcript)_
> [00:00] “Today we'll learn how to fight borrow checker errors and win!” _(from chapters/description; no transcript)_

_Confidence note: Content is inferred from chapter titles only. It is short and conceptual, so it may be lighter than hoped._

### 3. [Rust Error E0502 Explained Visually – Borrow Checker Finally Makes Sense](https://www.youtube.com/watch?v=94ju0zfnwhI)
Stable Rust · 7 min · counts 7 min · intermediate, concept_explainer · covers borrowing_refs, lifetimes · **confidence 0.50**

Walks through error E0502 (mutable vs immutable borrow conflict) with several fixes and a touch of lifetimes. It turns the borrowing rules into concrete compiler-error reasoning.

> [00:00] “What mutable and immutable borrows actually mean” _(from chapters/description; no transcript)_
> [00:00] “Multiple real fixes with clean mental models” _(from chapters/description; no transcript)_

_Confidence note: Description only, with no segment detail. Depth is uncertain._

### 4. [🦀Master Rust Programming #8 | Rust Generics, Traits, Trait Bound & Lifetimes | Advanced Type System🚀](https://www.youtube.com/watch?v=Ns-GgnxN7HY)
BlockDev · 78 min · counts 78 min · intermediate, lecture · covers traits_generics, lifetimes · **confidence 0.50**

Intermediate lecture covering generics, trait bounds and where clauses, then dangling references and lifetime annotation syntax, including 'static. It is the only pool candidate covering both traits/generics and lifetime syntax in one place, which limits switching creators.

> [00:00] “Lifetimes prevent dangling references at compile time” _(from chapters/description; no transcript)_
> [00:00] “Traits provide safe polymorphism without inheritance” _(from chapters/description; no transcript)_

_Confidence note: Chapter list only, with no transcript. The generic-types opening may be slow for a Go developer who knows generics, so skim it if needed._

### 5. [Understanding Rust Lifetimes](https://www.youtube.com/watch?v=MSi3E5Z8oRw)
Ryan Levick · 81 min · counts 81 min · intermediate, other · covers lifetimes, borrowing_refs · **confidence 0.55**

A long stream dedicated to one hard lifetime example: missing lifetime specifiers, mutable slices and iterators, conflicting requirements, anonymous lifetimes and a long compiler error-message walkthrough. It gives the depth on lifetimes and the borrow checker that the learner asked for, including lifetime-bearing structs and iterators.

> [00:00] “In this stream we attempt to discuss one example that can challenge even long time Rustaceans when it comes to understanding lifetimes.” _(from chapters/description; no transcript)_
> [00:00] “Follow along as we dive deep into lifetimes.” _(from chapters/description; no transcript)_

_Confidence note: Chapter titles only. The example is advanced and may be hard going right after the basics, but it is the best depth candidate in the pool._

### 6. [Rust Error Handling Tutorial: thiserror, anyhow, and the Source Chain You're Losing](https://www.youtube.com/watch?v=3Z-7MFNPzL0)
Elite Dev News · 17 min · counts 17 min · beginner, concept_explainer · covers result_errors, traits_generics · **confidence 0.55**

Covers Result and the `?` operator, writing an error type, thiserror derive with From/source, anyhow with context, and the source-chain gotcha. This is the Result and custom-error material a Go developer needs to replace `if err != nil`.

> [00:00] “Result and the question mark, writing an error type, adding context, and the four ways to print an error” _(from chapters/description; no transcript)_
> [11:44] “The gotcha: losing the source chain” _(from chapters/description; no transcript)_

_Confidence note: Labelled beginner in the pool and based on chapters only, but the chapter content is specific to Result and error types. Little other Result coverage is available at a better level._

### 7. [Build a Rust CLI Tool from Scratch (clap, serde, anyhow) – logscan](https://www.youtube.com/watch?v=uvP1bKTfa_Q)
Back To Code · 13 min · counts 13 min · intermediate, project_build · covers cli_port_project, lifetimes, result_errors · **confidence 0.50**

Builds a log-analyzer CLI with clap, anyhow file reading, zero-copy `&str` parsing with lifetimes, a real E0515 borrow-checker error and its fix, and serde JSON output. It ties lifetimes and error propagation to a CLI shaped like the learner's port.

> [00:00] “Along the way we hit a real borrow-checker error (E0515: cannot return value referencing local variable)” _(from chapters/description; no transcript)_
> [03:59] “Step 3: Parsing log lines (zero-copy with lifetimes)” _(from chapters/description; no transcript)_
> [04:45] “The borrow checker strikes (E0515)” _(from chapters/description; no transcript)_

_Confidence note: Chapters only. At 13 minutes it is fast and may skip explanations. It is the only candidate that combines CLI work with borrowing and lifetimes._

## Considered and dropped

- [Understanding Rust – Or How to Stop Worrying & Love the Borrow-Checker • Steve Smith • YOW! 2024](https://www.youtube.com/watch?v=zfb1y8yn8QI): Conceptual talk on move/borrow rules versus GC, flagged pure_theory, with no code and no transcript. A hands-on-leaning learner is better served by the unflagged ownership video.
- [Understanding Ownership in Rust](https://www.youtube.com/watch?v=VFIOSWy93H0): Beginner Rust-book walkthrough (stack and heap, slices). It is too basic for a senior systems developer, and only metadata is available.
- [Ownership in Rust | Rust Book](https://www.youtube.com/watch?v=K682q8p-YHg): Beginner, 64-minute Rust-book ownership lecture. It would spend too much budget on basics the learner already knows (stack and heap, memory safety).
- [Rust Book Club #10: Generics, Traits & Lifetimes](https://www.youtube.com/watch?v=kUzhjVExJIc): Book-club discussion of generics, traits and lifetimes. It is informal, with unverified content, and it overlaps with Ns-GgnxN7HY, which has clearer chapter-level structure.
- [🦀Master Rust Programming #2 | Ownership, Borrowing, References, Slices & Structs | Full Course 2025🚀](https://www.youtube.com/watch?v=2J9nYgrSTDg): Flagged too_basic_for_learner: beginner ownership, slices and structs lecture.
- [🚀 Build a Robust CLI App in Rust with Clap | Rust Programming Tutorial](https://www.youtube.com/watch?v=OcaerPp59Gs): 70-minute clap CLI build flagged off_topic (config, async tasks). It has no ownership or borrowing focus and would use too much of the budget.
- [Rust’s most complicated features explained](https://www.youtube.com/watch?v=9RsgFFp67eo): Advanced and mostly async, pinning and Send/Sync, flagged off_topic. Only part of it covers lifetimes.
- [JavaScript Dev Learns Rust | Building a CLI tool with Rust and clap](https://www.youtube.com/watch?v=RLy-KJSyK4w): Live beginner session (install Rust, hello world), so it largely teaches what the learner already knows. It has weak overlap with the CLI topic.
- [Rust Error Handling: The ? Operator, thiserror & anyhow](https://www.youtube.com/watch?v=6WykcOk78sc): Short chapters on ownership and Result sit inside a long Tokio/atomics episode flagged off_topic, with only chapter lists as evidence.
- [Rust for TypeScript devs : Borrow Checker](https://www.youtube.com/watch?v=ZNFdkTIzdXM): Flagged too_basic_for_learner: a short borrow-checker explainer aimed at TypeScript developers.

<details><summary>Filtered before assessment (32)</summary>

- Understanding the Mutable Borrow Error in Rust (prefilter): too short (88s)
- How to Fix Rust Borrow Checker Issues: Simple Code Solutions Explained (prefilter): too short (90s)
- Why Rust Has No Function Overloading (prefilter): pool cap reached
- Error Handling in Rust (prefilter): pool cap reached
- Parse Rust CLI Args With Clap 🦀 Rust Tutorial (prefilter): pool cap reached
- Rust programming References & Borrowing: Mastering Ownership Like a Pro (prefilter): pool cap reached
- The Rust Survival Guide (prefilter): pool cap reached
- Rust for Dummies in 12 Minutes (prefilter): pool cap reached
- Stop Using Rust Without These Rustc Commands (prefilter): pool cap reached
- Mastering Error Handling in Rust: From Panics to thiserror & anyhow | with Nathan Stocks (prefilter): pool cap reached
- 🦀 Master Rust Programming #12 | Build CLI with CLAP Crate & Publish to Crates.io | Cargo Deep Dive 🚀 (prefilter): pool cap reached
- How to THINK Like the Rust Compiler (Deep Dive) #rust #hackers #programming #compilation (prefilter): pool cap reached
- 8 deadly mistakes beginner Rust developers make (prefilter): pool cap reached
- Complete Rust Marathon in 6 hours (prefilter): pool cap reached
- Understand Ownership and Borrowing In Rust Programming Language (prefilter): pool cap reached
- Crust of Rust: Dispatch and Fat Pointers (prefilter): pool cap reached
- panic! vs Result: When to Use Each Rust Error Type (prefilter): pool cap reached
- Writing a CLI App in Rust! - Part 1 (prefilter): pool cap reached
- Mastering Ownership & Borrowing In Rust (prefilter): pool cap reached
- Will Crichton: Rust for Everyone! (prefilter): pool cap reached
- 🦀Master Rust Programming #11 | Iterators & Closures | Functional Programming Features & Performance🚀 (prefilter): pool cap reached
- Rust 51 | Traits in Rust – part 1 | Rust Programming Course | Uplatz (prefilter): pool cap reached
- Error Handling in Rust | panic! and Result (prefilter): pool cap reached
- Build a simple Command Line Interface (CLI) in Rust - Full Crash Rust Tutorial for Beginners (prefilter): pool cap reached
- Rust Tutorial 5  | Ownership and Borrowing | Rust in Hindi | Tutorial | Learn from scratch (prefilter): pool cap reached
- DevOpsCon Munich 2021: Generics in Go (prefilter): pool cap reached
- Rust error handling made easier with the ?-operator (prefilter): pool cap reached
- Rust Command Line Argument Parsing (A Better Way With Clap) (prefilter): pool cap reached
- Rust Ownership & Borrowing, Finally Visualized (Full Course) (prefilter): pool cap reached
- Adam McCullough- Rust's Borrow Checker Proven Correct!- λC 2019 (prefilter): pool cap reached
- Rust Memory Management: Ownership, Reference, & Lifetime Explained Simply #10 Rust (prefilter): pool cap reached
- Rust for Go Developers: The 6 Things You Actually Need to Learn (prefilter): pool cap reached

</details>

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-5.5, select=anthropic/claude-sonnet-5.5 · cost $0.105 · 38 s_
