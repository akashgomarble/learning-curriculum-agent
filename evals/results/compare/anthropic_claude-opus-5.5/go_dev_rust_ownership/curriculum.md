# Curriculum: Get comfortable with Rust ownership, borrowing and lifetimes so I can port a small Go CLI tool

**Budget:** 240 min · **Planned:** 208 min · **Videos:** 6 · **Candidates assessed:** 36

**How I read the goal:** Within 240 minutes of watching, the learner understands Rust ownership, borrowing and lifetimes deeply enough to reason about the borrow checker, and can use traits and Result well enough to port a small Go CLI tool to Rust.

**Assumptions:** The learner has little or no Rust syntax beyond what transfers from C-like languages, so a brief Rust-specific syntax orientation is folded into the ownership material rather than taught as a separate topic.; Porting a small Go CLI implies argument parsing, file or stdin I/O, and error propagation, so a CLI-style project video is the plan's backbone.; Traits and Result are included because they are needed for the port, though the emphasis (about 60% of the budget) is on ownership, borrowing and lifetimes.; The learner has no interest in beginner material, so videos aimed at complete programming novices are undesirable.
> ⚠️ No candidate had a transcript; every assessment rests on chapter lists and descriptions, so depth and teaching quality are unverified.
> ⚠️ Total counted viewing time is about 207.5 of 240 minutes (86%); about 32 minutes are deliberately unused because the remaining candidates are beginner-level, off-topic or redundant.
> ⚠️ Lifetimes get about 100 minutes, more than the planned 60, while ownership and borrowing get about 45 minutes of dedicated material, less than planned. The extra lifetimes time also covers advanced borrowing in practice.
> ⚠️ No video confirms an explicit comparison between traits and Go interfaces. Expect to map that yourself: trait bounds roughly correspond to interface constraints, and dyn Trait to interface values.
> ⚠️ The Steve Smith talk carries a pure_theory flag, and the error-handling video is labeled beginner. Both were kept because no unflagged alternative covers their angle.

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

An intermediate explainer that starts from the idea that each piece of data has one owner. It walks through String moves versus copies, mutable references passed to functions, and when cloning is a crutch. This gives a Go developer a concrete first model of moves before going deeper on the borrow checker.

> [03:02] “Each bit of data, e.g. "hello", has an owner” _(from chapters/description; no transcript)_
> [12:27] “Clone is your friend, but not an excuse for sloppy code” _(from chapters/description; no transcript)_
> [00:00] “It can be a little tricky to understand, but once you do you will understand why Rust is called a memory safe language.” _(from chapters/description; no transcript)_

_Confidence note: Judged only from chapter titles and the description, with no transcript. The chapters line up well with ownership and moves, but the depth is unverified._

### 2. [Understanding Rust – Or How to Stop Worrying & Love the Borrow-Checker • Steve Smith • YOW! 2024](https://www.youtube.com/watch?v=zfb1y8yn8QI)
GOTO Conferences · 42 min · watch 00:00–25:11 · counts 25 min · intermediate, lecture · covers ownership_moves, borrowing_refs · **confidence 0.50**

A conference talk on why Rust's move, borrow and mutability rules exist. It compares them with garbage collection and resource management and covers stack and heap sharing, which maps directly onto your Go and GC background and gives the conceptual depth on the borrow checker you asked for. It carries a pure_theory flag; I kept it because you asked for depth rather than hands-on coding, and no other intermediate candidate frames the borrow checker against GC.

> [00:00] “In this talk Steve Smith takes you through some of these core rules and why they exist” _(from chapters/description; no transcript)_
> [00:00] “drawing comparisons to existing programming techniques such as garbage collection and resource management” _(from chapters/description; no transcript)_
> [00:00] “Rust can be very welcoming, but it expects you to abide by a few rules that other languages regard as optional” _(from chapters/description; no transcript)_

_Confidence note: There is no transcript, and the chapter map ends at 25:11 of a 41.9-minute video, so the rest is probably Q&A and is excluded. The talk is conceptual only._

### 3. [🦀Master Rust Programming #8 | Rust Generics, Traits, Trait Bound & Lifetimes | Advanced Type System🚀](https://www.youtube.com/watch?v=Ns-GgnxN7HY)
BlockDev · 78 min · watch 14:54–1:18:32 · counts 64 min · intermediate, lecture · covers traits_generics, lifetimes, borrowing_refs · **confidence 0.55**

From generic functions onward, this covers trait bounds and where clauses, then dangling references, lifetime annotations and syntax, and the 'static lifetime. That gives you the traits-as-bounds material you need for the port, plus a structured first pass at lifetimes before the deep dive. The basic generic-types section at the start is skipped because you already know Go generics.

> [00:00] “Lifetimes prevent dangling references at compile time” _(from chapters/description; no transcript)_
> [00:00] “Traits provide safe polymorphism without inheritance” _(from chapters/description; no transcript)_
> [00:00] “Generics enable code reuse without runtime cost” _(from chapters/description; no transcript)_

_Confidence note: The chapter titles match the plan closely, but there is no transcript. There is no confirmed explicit comparison with Go interfaces._

### 4. [Understanding Rust Lifetimes](https://www.youtube.com/watch?v=MSi3E5Z8oRw)
Ryan Levick · 81 min · watch 05:56–1:14:49 · counts 69 min · intermediate, other · covers lifetimes, borrowing_refs, traits_generics · **confidence 0.60**

A deep stream on one lifetime-heavy example that 'can challenge even long time Rustaceans.' It covers missing lifetime specifiers, mutable slices and iterators, returning a trait, conflicting requirements, the anonymous lifetime, and a long walk through the compiler's error messages. This is the borrow-checker depth you asked for, aimed above beginner level.

> [00:00] “In this stream we attempt to discuss one example that can challenge even long time Rustaceans when it comes to understanding lifetimes.” _(from chapters/description; no transcript)_
> [00:00] “Follow along as we dive deep into lifetimes.” _(from chapters/description; no transcript)_

_Confidence note: The chapters point strongly to deep lifetime reasoning, but this is an unedited stream with no transcript, so pacing may be slow. The final mutable-iterators section and the intro are skipped._

### 5. [Rust Error Handling Tutorial: thiserror, anyhow, and the Source Chain You're Losing](https://www.youtube.com/watch?v=3Z-7MFNPzL0)
Elite Dev News · 17 min · counts 17 min · beginner, concept_explainer · covers result_errors · **confidence 0.60**

Covers Result and the ? operator, what makes a type an error, thiserror derives with from and source, anyhow for applications, and the pitfall of losing the source chain when printing errors. This is the error-handling toolkit you need for a CLI port. It is labeled beginner, but the content is Rust-specific error design, not general programming basics.

> [00:00] “Result and the question mark, writing an error type, adding context, and the four ways to print an error” _(from chapters/description; no transcript)_
> [11:44] “The gotcha: losing the source chain” _(from chapters/description; no transcript)_
> [00:00] “one of which silently throws away the root cause” _(from chapters/description; no transcript)_

_Confidence note: It is the only candidate rated 2 on result_errors, and its chapters are specific. With no transcript, the depth is unconfirmed._

### 6. [Build a Rust CLI Tool from Scratch (clap, serde, anyhow) – logscan](https://www.youtube.com/watch?v=uvP1bKTfa_Q)
Back To Code · 13 min · counts 13 min · intermediate, project_build · covers cli_port_project, lifetimes, result_errors · **confidence 0.65**

Builds a log-analyzer CLI with clap arguments, anyhow error context and zero-copy &str parsing with lifetimes. Along the way it hits and fixes a real E0515 borrow-checker error, which ties together everything you need for your Go CLI port.

> [00:00] “Along the way we hit a real borrow-checker error (E0515: cannot return value referencing local variable)” _(from chapters/description; no transcript)_
> [00:00] “Zero-copy parsing with &str and lifetimes” _(from chapters/description; no transcript)_
> [04:45] “The borrow checker strikes (E0515)” _(from chapters/description; no transcript)_

_Confidence note: The project closely matches your goal, but without a transcript the depth of each step is unverified, and 13 minutes is brisk for this much content._

## Considered and dropped

- [Rust Error Handling: The ? Operator, thiserror & anyhow](https://www.youtube.com/watch?v=6WykcOk78sc): Only about 7 minutes cover ownership, borrowing and Result. The remaining roughly 25 minutes are Tokio, atomics and benchmarks, which are outside the plan.
- [Modern Rust Systems: Complete Architecture Deep Dive & Advanced Systems Roadmap](https://www.youtube.com/watch?v=8hRctxuLCW0): A roadmap overview of a series, flagged surface_intro, that names topics without teaching them in depth.
- [🦀Master Rust Programming #2 | Ownership, Borrowing, References, Slices & Structs | Full Course 2025🚀](https://www.youtube.com/watch?v=2J9nYgrSTDg): A beginner full-course episode flagged too_basic_for_learner; it covers ownership at a novice pace.
- [Rust Book Club #10: Generics, Traits & Lifetimes](https://www.youtube.com/watch?v=kUzhjVExJIc): A book-club discussion of generics, traits and lifetimes that overlaps the BlockDev lecture, which has a clearer chapter structure on trait bounds and lifetimes.
- [Rust Error E0502 Explained Visually – Borrow Checker Finally Makes Sense](https://www.youtube.com/watch?v=94ju0zfnwhI): A visual E0502 explainer that is useful but short and description-only. The Levick stream and the logscan E0515 fix already cover concrete borrow-error debugging.
- [How to fight Rust's borrow checker... and win.](https://www.youtube.com/watch?v=Pg07HQJ0tvI): A short collection of borrow-checker tips with no verified depth; it would add another creator for overlapping content.
- [🚀 Build a Robust CLI App in Rust with Clap | Rust Programming Tutorial](https://www.youtube.com/watch?v=OcaerPp59Gs): A clap CLI build focused on configuration and async tasks rather than ownership, borrowing and lifetimes; flagged off_topic.
- [JavaScript Dev Learns Rust | Building a CLI tool with Rust and clap](https://www.youtube.com/watch?v=RLy-KJSyK4w): A beginner live session that starts with installing Rust and Hello World, which is too basic. logscan covers CLI building with borrow-checker content.
- [Rust’s most complicated features explained](https://www.youtube.com/watch?v=9RsgFFp67eo): Advanced and mostly about async, pinning and Send/Sync, which is off-topic for this plan.
- [Ownership in Rust | Rust Book](https://www.youtube.com/watch?v=K682q8p-YHg): A beginner Rust Book read-through spending an hour on ownership alone, at the wrong level for an experienced systems developer.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-5.5, select=anthropic/claude-opus-5.5 · cost $0.209 · 66 s_
