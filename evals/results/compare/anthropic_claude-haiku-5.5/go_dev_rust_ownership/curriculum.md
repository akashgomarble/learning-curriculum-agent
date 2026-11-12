# Curriculum: Get comfortable with Rust ownership, borrowing and lifetimes so I can port a small Go CLI tool

**Budget:** 240 min · **Planned:** 198 min · **Videos:** 9 · **Candidates assessed:** 36

**How I read the goal:** Within 240 minutes of watching, the learner understands Rust ownership, borrowing and lifetimes deeply enough to reason about the borrow checker, and can use traits and Result well enough to port a small Go CLI tool to Rust.

**Assumptions:** The learner has little or no Rust syntax beyond what transfers from C-like languages, so a brief Rust-specific syntax orientation is folded into the ownership material rather than taught as a separate topic.; Porting a small Go CLI implies argument parsing, file or stdin I/O, and error propagation, so a CLI-style project video is the plan's backbone.; Traits and Result are included because they are needed for the port, though the emphasis (about 60% of the budget) is on ownership, borrowing and lifetimes.; The learner has no interest in beginner material, so videos aimed at complete programming novices are undesirable.
> ⚠️ Every candidate was assessed from chapter lists or descriptions only, with no transcript, so all confidences are low and the picks should be checked against the actual videos.
> ⚠️ Total chosen viewing time is about 198.5 minutes, about 83% of the 240-minute budget, within the target range.
> ⚠️ The Ryan Levick lifetimes stream is about 69 minutes, which is more than the 60-minute lifetimes share. It was extended to the error-message walkthrough because that is the most direct borrow-checker reasoning available in the pool; its last section is chapter-title only.
> ⚠️ Only one candidate (logscan) teaches the CLI port with verified relevance, and it is chapter-only evidence, so the CLI-port sub-topic is the thinnest part of the curriculum.
> ⚠️ The learner should expect a gap in hands-on borrow-checker practice: no candidate with a transcript was found that works through ownership and borrowing with code.
> ⚠️ Steve Smith's borrow-checker talk was excluded as pure_theory; the learner may want it as an optional conceptual extra if they still want more depth.
> ⚠️ The Book Club pick covers only the generics and traits chapters, so trait-related depth beyond that is limited.

## Plan

- **Ownership and moves (vs Go's GC and value copies)** (`ownership_moves`): As a Go dev used to the garbage collector and implicit copying, the learner needs a new mental model of single ownership, moves, Copy vs Clone, and drop/RAII, which maps to their systems and memory knowledge.
- **Borrowing and references: shared vs mutable, borrow checker rules** (`borrowing_refs`): Rust references look like Go pointers but come with aliasing-XOR-mutability rules. Depth here is the learner's stated priority, including common compiler errors and how to restructure code to satisfy the checker.
- **Lifetimes: annotations, elision rules, structs holding references** (`lifetimes`): Lifetimes have no Go equivalent. The learner wants depth, so they need to understand why annotations exist, elision rules, lifetimes in structs and functions, and 'static.
- **Traits and generics (compared to Go interfaces and generics)** (`traits_generics`): Traits are central to idiomatic Rust and to the standard library APIs a CLI port uses. The learner can map them to Go interfaces but must learn trait bounds, impl blocks, derive and dyn vs generics.
- **Error handling with Result, the ? operator, and custom error types** (`result_errors`): Go's if err != nil pattern maps onto Result and ?, but the learner must learn Option/Result, From conversions, and crates like anyhow and thiserror for CLI tools.
- **Building a CLI tool in Rust (clap, file I/O, error propagation)** (`cli_port_project`): The final goal is porting a Go CLI, so seeing ownership, borrowing, traits and Result applied in a realistic command-line project cements the concepts and covers the tooling (cargo, clap).

## Watch in this order

### 1. [Rust: What is Ownership and Borrowing?](https://www.youtube.com/watch?v=79phqVpE7cU)
Gary Explains · 20 min · counts 20 min · intermediate, concept_explainer · covers ownership_moves, borrowing_refs · **confidence 0.50**

Walks through ownership of data, moves with Strings, clone versus move, and mutable references passed to functions, which is the core of the ownership and borrowing gap. The card's quotes cover the owner-per-value idea and the clone trade-off.

> [03:02] “Each bit of data, e.g. "hello", has an owner” _(from chapters/description; no transcript)_
> [12:27] “Clone is your friend, but not an excuse for sloppy code” _(from chapters/description; no transcript)_

_Confidence note: No transcript; the chapter list is the only evidence. Confidence would rise if the transcript confirmed the mutable-reference and move examples are explained in depth rather than introduced briefly._

### 2. [RustEdu Workshop 2022 - RustViz: Interactively Visualizing Ownership and Borrowing](https://www.youtube.com/watch?v=zCF8QVkc6IY)
Rust Programming Language · 21 min · counts 21 min · intermediate, lecture · covers ownership_moves, borrowing_refs · **confidence 0.40**

RustViz visualises ownership and borrowing through compiler-assisted diagrams on annotated code, which suits a learner who wants to reason about why the borrow checker accepts or rejects code. It is a lecture rather than a hands-on build.

> [00:00] “Cyrus Omar describes RustViz, a tool for annotating Rust code that can provide compiler-assisted visualization of ownership and borrowing patterns.” _(from chapters/description; no transcript)_

_Confidence note: No transcript, and the talk is about a teaching tool, so it may spend more time on the tool than on the Rust rules. Confidence would rise if the transcript showed the borrow rules explained through the visualisations._

### 3. [Rust Error E0502 Explained Visually – Borrow Checker Finally Makes Sense](https://www.youtube.com/watch?v=94ju0zfnwhI)
Stable Rust · 7 min · counts 7 min · intermediate, concept_explainer · covers borrowing_refs, lifetimes · **confidence 0.45**

Explains what mutable and immutable borrows mean, using the E0502 error as the vehicle, and promises several fixes and a basic lifetimes view. It targets the exact borrow-checker reasoning the learner asked for.

> [00:00] “What mutable and immutable borrows actually mean” _(from chapters/description; no transcript)_
> [00:00] “Multiple real fixes with clean mental models” _(from chapters/description; no transcript)_

_Confidence note: No transcript and only 7 minutes, so depth is uncertain. Confidence would rise if the transcript showed the fixes reasoned through the borrow rules rather than just applied._

### 4. [How to fight Rust's borrow checker... and win.](https://www.youtube.com/watch?v=Pg07HQJ0tvI)
Let's Get Rusty · 8 min · counts 8 min · intermediate, other · covers borrowing_refs · **confidence 0.35**

Covers how to read and respond to borrow checker errors, which builds the debugging habit the learner needs while porting code. It is conceptual and short, so it supplements the deeper borrowing material.

> [00:00] “Getting bombarded with compile time errors is all too common when writing Rust.” _(from chapters/description; no transcript)_
> [00:00] “Today we'll learn how to fight borrow checker errors and win!” _(from chapters/description; no transcript)_

_Confidence note: Chapter titles only, and the card describes tips rather than a rigorous treatment of the rules. Confidence would rise if the transcript showed the reasoning behind each error class._

### 5. [Understanding Rust Lifetimes](https://www.youtube.com/watch?v=MSi3E5Z8oRw)
Ryan Levick · 81 min · watch 05:56–1:14:49 · counts 69 min · intermediate, other · covers lifetimes · **confidence 0.40**

Works through one lifetime-heavy example, including missing lifetime specifiers, conflicting lifetime requirements, anonymous lifetimes, and a walkthrough of compiler error messages. Watching from the lifetime-specifier chapter to the end of the error walkthrough targets lifetime reasoning directly.

> [00:00] “In this stream we attempt to discuss one example that can challenge even long time Rustaceans when it comes to understanding lifetimes.” _(from chapters/description; no transcript)_
> [00:00] “Follow along as we dive deep into lifetimes.” _(from chapters/description; no transcript)_

_Confidence note: No transcript and an 81-minute stream with chapter titles only. The range is long, and the error-walkthrough section is unverified. Confidence would rise if the transcript confirmed the conflicting-requirements and anonymous-lifetime sections are explained._

### 6. [Rust Book Club #10: Generics, Traits & Lifetimes](https://www.youtube.com/watch?v=kUzhjVExJIc)
Shiddy Programming · 66 min · watch 01:15–30:20 · counts 29 min · intermediate, lecture · covers traits_generics · **confidence 0.40**

Covers generics and then traits from Rust Book chapter 10, which is the gap on trait bounds and how Rust traits compare to Go interfaces and generics. The range is limited to the generics and traits sections.

> [00:00] “This chapter is dope, now when we look at a function definition we actually know what's going on.” _(from chapters/description; no transcript)_
> [00:00] “Lot's o' concepts here, and a lot to talk about.” _(from chapters/description; no transcript)_

_Confidence note: No transcript and the chapter list is the only evidence. It is a book-club discussion, so the explanations may be informal. Confidence would rise if the transcript showed trait definitions and bounds explained with code._

### 7. [Rust Type Conversions: The Traits You Need to Know! | Advanced Rust Part 10](https://www.youtube.com/watch?v=VkqZEhER__4)
Green Tea Coding · 14 min · counts 14 min · intermediate, concept_explainer · covers traits_generics, result_errors · **confidence 0.40**

Covers the conversion traits (From/Into, TryFrom/TryInto, FromStr, AsRef, Deref), which are the traits that make Result's ? operator and error conversion work. It fits the port's need for error propagation.

> [00:00] “Correct use of Rust's built in traits is oftentimes the difference between slightly awkward and idiomatic, professional code.” _(from chapters/description; no transcript)_
> [00:00] “Conversion traits are some of the most used ones.” _(from chapters/description; no transcript)_

_Confidence note: No transcript; the chapter list suggests these traits are covered briefly, one per chapter. Confidence would rise if the transcript showed From-driven error conversion explained._

### 8. [Rust Error Handling Tutorial: thiserror, anyhow, and the Source Chain You're Losing](https://www.youtube.com/watch?v=3Z-7MFNPzL0)
Elite Dev News · 17 min · counts 17 min · beginner, concept_explainer · covers result_errors · **confidence 0.50**

Introduces Result, the question mark operator, custom error types with thiserror, and anyhow, and warns about losing the error source chain. It covers the Result gap the learner needs for the port.

> [00:00] “Result and the question mark, writing an error type, adding context, and the four ways to print an error” _(from chapters/description; no transcript)_

_Confidence note: Labelled beginner and metadata-only. The Result material is new to this learner, so the level is acceptable, but the depth is unverified. Confidence would rise if the transcript confirmed the source-chain discussion._

### 9. [Build a Rust CLI Tool from Scratch (clap, serde, anyhow) – logscan](https://www.youtube.com/watch?v=uvP1bKTfa_Q)
Back To Code · 13 min · counts 13 min · intermediate, project_build · covers lifetimes, result_errors, cli_port_project · **confidence 0.50**

Builds a real Rust CLI with clap and anyhow, then hits and fixes a real E0515 borrow error on a zero-copy parser that uses lifetimes. It closes the plan by applying lifetimes and Result to a CLI, matching the Go port.

> [00:00] “Along the way we hit a real borrow-checker error (E0515: cannot return value referencing local variable)” _(from chapters/description; no transcript)_
> [03:59] “Step 3: Parsing log lines (zero-copy with lifetimes)” _(from chapters/description; no transcript)_

_Confidence note: No transcript, but the chapter titles show a real borrow-checker error and its fix plus a clap CLI, which is a close match. Confidence would rise if the transcript showed the E0515 fix reasoned through lifetimes._

## Considered and dropped

- [Understanding Rust – Or How to Stop Worrying & Love the Borrow-Checker • Steve Smith • YOW! 2024](https://www.youtube.com/watch?v=zfb1y8yn8QI): Steve Smith's talk is strong on the borrow checker, but it is flagged pure_theory, and it is a lecture with no hands-on coding. Unflagged candidates cover the same borrowing material, so it is excluded under the hands-on rule. It is worth watching separately if the learner wants conceptual depth.
- [Ownership in Rust | Rust Book](https://www.youtube.com/watch?v=K682q8p-YHg): Piyush Garg's ownership chapter is beginner-level, and an unflagged candidate (Gary Explains) covers the same ownership ground at intermediate level. Metadata only, so the depth is unverified.
- [Understanding Ownership in Rust](https://www.youtube.com/watch?v=VFIOSWy93H0): A beginner walk through the Rust Book chapter by chapter, with a 25-minute runtime. The learner already knows what a variable is, and the level does not match the gap. The chapter list does not confirm depth beyond introductory material.
- [Rust Error Handling: The ? Operator, thiserror & anyhow](https://www.youtube.com/watch?v=6WykcOk78sc): Covers ownership, borrowing, lifetimes, and Result, but about 25 of its 39 minutes are Tokio concurrency, atomics, and benchmarks, which the learner already knows or does not need. Chapter list only, so the useful part cannot be confirmed.
- [🚀 Build a Robust CLI App in Rust with Clap | Rust Programming Tutorial](https://www.youtube.com/watch?v=OcaerPp59Gs): A clap-based CLI build, but it leans toward async tasks and configuration management, with no ownership, borrowing, or lifetime content. It is flagged off_topic and has no transcript. logscan covers the CLI-with-clap need with more relevant borrow-checker content.
- [Code Your Own CLI With Rust](https://www.youtube.com/watch?v=5UA9UWWAagc): A beginner code-along CLI build with no transcript, so nothing confirms the content beyond the description. The learner would need to sit through basics, and nothing in it is verified for the borrow-checker gap.
- [Rust’s most complicated features explained](https://www.youtube.com/watch?v=9RsgFFp67eo): Flagged advanced and off_topic. It is mostly about pinning, async, and Send/Sync, with only a brief lifetimes chapter, and no transcript.
- [Rust Error Handling Explained: thiserror vs anyhow (Best Practices)](https://www.youtube.com/watch?v=-c9JEexiHPE): A thiserror-versus-anyhow comparison that overlaps the Elite Dev News pick, with no transcript to show it adds depth. Excluded to avoid redundancy.
- [Rust Error Handling: A Practical Guide to Result](https://www.youtube.com/watch?v=hF1rnf22VZA): A short Result overview, with chapter list only. It adds little beyond the Elite Dev News pick and would be filler against the time budget.
- [Learning Rust: Memory, Ownership and Borrowing](https://www.youtube.com/watch?v=8M0QfLUDaaA): Flagged surface_intro and poor_transcript. It is a short 2018 introduction to ownership, which the learner has already outgrown.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-5.5, select=anthropic/claude-haiku-5.5 · cost $0.009 · 57 s_
