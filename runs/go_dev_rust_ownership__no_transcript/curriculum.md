# Curriculum: Get comfortable with Rust ownership, borrowing and lifetimes so I can port a small Go CLI tool

**Budget:** 240 min · **Planned:** 191 min · **Videos:** 9 · **Candidates assessed:** 36

**How I read the goal:** After about 4 hours of watching, the learner can reason about Rust ownership, borrowing and lifetimes with confidence, use Result and the ? operator idiomatically, and port their small Go CLI tool to Rust.

**Assumptions:** The learner needs enough Rust syntax and tooling (cargo, structs, enums, match) to follow videos, but this is covered by mapping from Go rather than taught from scratch.; Traits are needed mainly as they relate to error handling, generics bounds and lifetimes, not as a full deep dive.; The ported CLI uses typical pieces: argument parsing (e.g. clap), file or stdin IO, and error propagation.; Videos in English; the learner prefers material aimed at experienced developers coming from Go, C, or C++.
> ⚠️ Every candidate was assessed from metadata only: no transcripts were available and there are no verified quotes. All evidence_quote_ids are empty and confidences are moderate to low. Skim each video's opening minutes before committing.
> ⚠️ Total viewing time is about 191 minutes of the 240-minute budget (about 80%). The remaining 49 minutes were left unused because the remaining candidates were redundant, beginner-level, flagged, or had no usable transcript.
> ⚠️ Coverage of Drop, Copy vs Clone and 'static is unverified. The ownership video and the lifetimes videos were chosen from titles and summaries.
> ⚠️ No candidate is explicitly for Go developers beyond the 7.5-minute orientation. You will need to map Go's error returns and pointers to Result and references yourself when porting.
> ⚠️ The CLI video covers clap, serde and anyhow with the file/log processing the learner needs. It is short (13 minutes), so expect to consult the clap docs for your own tool's argument layout.
> ⚠️ Some upload dates are in the future relative to other metadata (e.g. 2026), so I assumed these are metadata errors and treated the material as current.
> ⚠️ The plan has 9 picks from 9 different creators, so expect a different codebase and style for each video. This was accepted because no single creator covered all sub-topics.

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
Masa Tech Team · 8 min · counts 8 min · intermediate, concept_explainer · covers rust_for_go_devs · **confidence 0.50**

Maps Rust onto Go: ownership and borrowing, Result and Option, and compiler feedback. This suits a senior Go developer who needs orientation, not syntax basics. It is also the only candidate aimed at Go developers.


_Confidence note: Only metadata was assessed and there are no verified quotes or segment map. Depth is probably light, since the video is a six-topic overview._

### 2. [Understanding Ownership in Rust](https://www.youtube.com/watch?v=VFIOSWy93H0)
Let's Get Rusty · 26 min · counts 26 min · intermediate, concept_explainer · covers ownership_moves · **confidence 0.35**

A dedicated ownership video (moves, and likely Copy vs Clone and Drop) to build the move-semantics foundation before borrowing. It is the only candidate dedicated to ownership that is not flagged as a surface intro.


_Confidence note: The transcript was unavailable, so this is judged from the title and channel only. I would be more sure with a transcript showing stack/heap, moves, Clone and Drop at a non-beginner level._

### 3. [Understanding Rust – Or How to Stop Worrying & Love the Borrow-Checker • Steve Smith • YOW! 2024](https://www.youtube.com/watch?v=zfb1y8yn8QI)
GOTO Conferences · 42 min · counts 42 min · intermediate, lecture · covers borrowing_refs, ownership_moves · **confidence 0.50**

A conference talk aimed at understanding the borrow checker, with the strongest borrowing relevance in the pool. It matches the learner's request for depth on the borrow checker. The pure_theory flag does not count against it here because the learner wants the concepts behind the checker.


_Confidence note: The transcript is poor and there are no quotes. It is described as an introduction, so depth on mutable-borrow error patterns is unverified._

### 4. [but what is 'a lifetime?](https://www.youtube.com/watch?v=gRAVZv7V91Q)
leddoo · 12 min · counts 12 min · intermediate, concept_explainer · covers lifetimes · **confidence 0.40**

Explains what a lifetime is as a way of reasoning about references, a mental model that suits an experienced systems programmer. It comes before the annotation-focused videos.


_Confidence note: Judged from the title and a metadata summary only. It could be pure conceptual talk with no code._

### 5. [Rust Lifetimes explained Tutorial](https://www.youtube.com/watch?v=S-SkEA4QWWE)
Francesco Ciulla · 15 min · counts 15 min · intermediate, concept_explainer · covers lifetimes, borrowing_refs · **confidence 0.45**

Covers lifetime annotations, how the borrow checker validates references, and when explicit lifetime parameters are needed in function signatures and structs. This is the practical annotation side that follows the mental model.


_Confidence note: The transcript was not verified. It is unclear whether it covers elision rules and 'static in depth._

### 6. [Rust Generics, Traits & Lifetimes Explained — Book Chapter 10 Project](https://www.youtube.com/watch?v=p2uAN6SJorA)
Kush_EXE · 22 min · counts 22 min · intermediate, project_build · covers lifetimes, traits_basics · **confidence 0.40**

Works through generics, traits and lifetimes on a Rust Book Chapter 10 project, showing lifetimes in structs and function signatures alongside trait bounds. This sets up the trait knowledge that error handling needs.


_Confidence note: The transcript is poor and the video is based on the Rust Book, so it may be gentler than this learner needs. No segment map was available._

### 7. [Introduction to Generics and Traits | Advanced Rust Part 1](https://www.youtube.com/watch?v=AnsRR-i5UWQ)
Green Tea Coding · 16 min · counts 16 min · intermediate, concept_explainer · covers traits_basics · **confidence 0.40**

Introduces trait definitions and generic type parameters as Rust's alternative to inheritance. This gives the trait and bounds grounding that From, Display and the Error trait build on.


_Confidence note: The transcript was unavailable. It may not reach impl Trait, From or the Error trait specifically._

### 8. [Rust Error Handling: The ? Operator, thiserror & anyhow](https://www.youtube.com/watch?v=6WykcOk78sc)
Lets learn with Ajay · 39 min · counts 39 min · intermediate, concept_explainer · covers result_error_handling · **confidence 0.55**

Directly covers the ? operator, custom error types, From conversions, and thiserror vs anyhow (libraries vs applications). This maps onto the learner's Go habit of returning errors everywhere.


_Confidence note: The summary is detailed and matches the need, but there is no verified transcript or quote. Only an overview segment was listed._

### 9. [Build a Rust CLI Tool from Scratch (clap, serde, anyhow) – logscan](https://www.youtube.com/watch?v=uvP1bKTfa_Q)
Back To Code · 13 min · counts 13 min · intermediate, project_build · covers build_cli_port, result_error_handling, borrowing_refs · **confidence 0.50**

Builds a log-analysis CLI with clap, serde and anyhow, and works through a real borrow-checker error (E0515) during development. This shows ownership, borrowing and error propagation in a project close to the learner's port.


_Confidence note: The transcript is poor, and the segment map (00:12-04:19) does not match the 13-minute duration. Depth is unverified._

## Similar videos: why only one made the cut

- kept `gRAVZv7V91Q` over `juIINGuZyBc` (both cover lifetimes): gRAVZv7V91Q is specifically about how to reason about a lifetime and has a relevance score for lifetimes. juIINGuZyBc has no usable transcript or relevance evidence.
- kept `S-SkEA4QWWE` over `hmefR4tE_H4` (both cover borrow checker, references, mutable references, immutable references): S-SkEA4QWWE covers lifetime annotations, signatures and structs, which the picked borrowing talk does not. hmefR4tE_H4 is a short borrowing-only explainer overlapping that talk.
- kept `S-SkEA4QWWE` over `3R2Emr5TfV0` (both cover lifetimes, lifetime annotations, borrow checker): S-SkEA4QWWE is more than twice as long and covers annotations in functions and structs. 3R2Emr5TfV0 is a short pure_theory explainer.
- kept `S-SkEA4QWWE` over `178uniabkag` (both cover lifetimes, lifetime annotations, borrow checker): Only one video from this cluster was allowed. S-SkEA4QWWE is more clearly aimed at annotations in signatures and structs, while gRAVZv7V91Q already covers the conceptual view.

## Considered and dropped

- [Mastering Error Handling in Rust: From Panics to thiserror & anyhow | with Nathan Stocks](https://www.youtube.com/watch?v=sZV6sz4P6QY): A 73.8-minute error-handling webinar that is flagged pure_theory. Within the 240-minute budget, 6Wykc covers the ? operator, From, thiserror and anyhow with a more practical focus.
- [Rust: Ownership and Borrowing, By Rodrigo Boniatti](https://www.youtube.com/watch?v=9vynzAEhvXo): A second ownership/borrowing explainer without a transcript. It would repeat VFIOSWy93H0 and zfb1y8yn8QI and add another teaching style.
- [The Secret Behind Rust’s Memory Safety: The Borrow Checker EXPLAINED](https://www.youtube.com/watch?v=hmefR4tE_H4): In the borrow-checker/lifetimes duplicate cluster and only a short concept explainer on mutable vs immutable references. The longer talk already covers this.
- [Rust Lifetimes Explained Clearly | Borrow Checker, References & Lifetimes | Learn Rust Step by Step](https://www.youtube.com/watch?v=3R2Emr5TfV0): A short concept explainer flagged pure_theory and poor transcript, in the lifetimes duplicate cluster. The kept lifetimes video is longer and more detailed.
- [Rust Lifetimes Explained — Finally Make Sense of 'a (2026)](https://www.youtube.com/watch?v=178uniabkag): A lifetimes 'loans' mental model, in the same cluster as S-SkEA4QWWE. It is flagged pure_theory and poor transcript, and gRAVZv7V91Q already supplies a conceptual lifetimes view.
- [Rust Lifetimes Finally Explained!](https://www.youtube.com/watch?v=juIINGuZyBc): Duplicate lifetimes video with no usable transcript or relevance scoring. gRAVZv7V91Q has better-grounded evidence of focus.
- [A Simpler Way to See Results](https://www.youtube.com/watch?v=s5S2Ed5T-dc): A 19-minute Result/Option explainer that is largely theory and covers ? only briefly. 6WykcOk78sc covers the ? operator and custom errors, which the learner needs.
- [🚀 Build a Robust CLI App in Rust with Clap | Rust Programming Tutorial](https://www.youtube.com/watch?v=OcaerPp59Gs): A beginner-level, long (69.7 min) clap tutorial with no verified content on ownership or error propagation. It would consume too much of the budget.
- [Rust: What is Ownership and Borrowing?](https://www.youtube.com/watch?v=79phqVpE7cU): A beginner-level ownership explainer flagged surface_intro and pure_theory. The learner wants depth and already has an advanced systems background.
- [Rust: Generics, Traits, Lifetimes](https://www.youtube.com/watch?v=JLfEiJhpTbE): A 35-minute generics/traits/lifetimes video flagged pure_theory with a weak segment map. p2uAN6SJorA and AnsRR-i5UWQ give more targeted coverage.

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

_Models: plan=anthropic/claude-sonnet-5.5, assess=anthropic/claude-haiku-4.5, select=anthropic/claude-sonnet-5.5 · cost $0.102 · 46 s_
