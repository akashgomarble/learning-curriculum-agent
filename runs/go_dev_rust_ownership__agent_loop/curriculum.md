# Curriculum: Get comfortable with Rust ownership, borrowing and lifetimes so I can port a small Go CLI tool

**Budget:** 240 min · **Planned:** 204 min · **Videos:** 9 · **Candidates assessed:** 36

**How I read the goal:** A senior Go dev can reason about moves, borrows and lifetimes, read borrow-checker errors, use traits, and write idiomatic Result/? error handling well enough to port a small Go CLI.

**Assumptions:** Learner knows stack/heap and pointers, so the stack-vs-heap segment of the ownership video can be skimmed.; Generics and traits are only needed at the level required for trait bounds, dyn dispatch and error traits.; Async/Tokio is not needed for a small CLI.
> ⚠️ Total is about 204 of 240 minutes. I left the remainder unused rather than pad with weak videos.
> ⚠️ The Ardan webinar window (1200–4000 s) is estimated from quote timestamps, so check the edges.
> ⚠️ Ownership and lifetimes overlap a little between the Let's Get Rusty video and the conference talk. I kept both because the first teaches the mechanics and the second gives the model (Drop, Rc, Send/Sync).
> ⚠️ Traits coverage is shallow, and no video on associated types, iterators or closures was found. The Rust Book chapter on traits would fill that gap.
> ⚠️ Clap and argument parsing are only touched in the logscan video. There was no time to cover them fully.
> ⚠️ The dropped list contains a placeholder entry (CHRNj5oubwc_dup) that I added by mistake and that should be ignored. The substantive drops are wM6o70NAWUI and pDM_5HT2UlU.

## Plan

- **Ownership, moves, borrowing and the borrow-checker rules** (`own`): Core mental shift from Go's GC and free aliasing
- **Lifetimes: annotations, elision, structs, and a mental model** (`life`): Depth on the borrow checker was explicitly requested
- **Traits and generics (trait bounds, dyn vs static dispatch)** (`traits`): Rust's analogue of Go interfaces; needed for error types and bounds
- **Result, ? operator, custom errors with thiserror/anyhow** (`err`): Replaces Go's `if err != nil` pattern throughout the CLI
- **Applied CLI example combining borrowing and errors** (`proj`): Shows the borrow checker and anyhow in a real CLI

## Watch in this order

### 1. [Understanding Ownership in Rust](https://www.youtube.com/watch?v=VFIOSWy93H0)
Let's Get Rusty · 26 min · counts 26 min · intermediate, concept_explainer · covers own · **confidence 0.80**

Walks through moves, Copy, shared and mutable references and the borrow-checker rules with compiler error demos. Skim the early stack/heap section, which you already know.

> [07:08] “each value in rust has a variable that's called its owner so one variable one owner”
> [13:11] “instead of calculate length taking a string we'll make it take a reference to a string”
> [14:59] “you can only have one mutable reference to a particular piece of data in a particular scope”

_Confidence note: Solid on the rules but somewhat beginner-paced at the start._

### 2. [Understanding Rust – Or How to Stop Worrying & Love the Borrow-Checker • Steve Smith • YOW! 2024](https://www.youtube.com/watch?v=zfb1y8yn8QI)
GOTO Conferences · 42 min · counts 42 min · intermediate, lecture · covers own, life · **confidence 0.75**

Conference talk that frames the compiler as a deterministic garbage collector, which suits a GC-language veteran. It covers lifetimes, Drop, Box, Rc and Send/Sync, which connect to your concurrency background.

> [07:16] “the compiler is your garbage collector. See all languages are garbage collected.”
> [21:24] “Rust can infer a lot of lifetimes, it can't infer all of them. Sometimes you need to make a promise to the Rust compiler.”
> [27:32] “RC allows you to create multiple pointers to something on the heap and each one of them is owned.”

_Confidence note: Lecture format and light on code, but good depth on the model._

### 3. [Rust Lifetimes Finally Explained!](https://www.youtube.com/watch?v=juIINGuZyBc)
Let's Get Rusty · 19 min · counts 19 min · intermediate, concept_explainer · covers life · **confidence 0.85**

Covers lifetime annotations, the three elision rules, structs holding references and 'static, with worked examples.

> [04:55] “generic lifetime annotations describe the relationship between the lifetimes of multiple references and how they relate to each other”
> [07:02] “the lifetime of the returned reference will be the same as the smallest lifetime of the arguments”
> [15:26] “the compiler will try to follow these three rules and if at the end of these three rules it still can't figure out what the lifetimes are then we have to manually specify them”
> [17:10] “all string literals have a static lifetime and that's because string literals are stored in the program's binary”

_Confidence note: Clear and complete on lifetime syntax._

### 4. [but what is 'a lifetime?](https://www.youtube.com/watch?v=gRAVZv7V91Q)
leddoo · 12 min · counts 12 min · intermediate, concept_explainer · covers life · **confidence 0.75**

Gives a deeper mental model of what 'a means, using regions, liveness and subtyping. It fills the gap left by the official resources and builds the borrow-checker intuition you asked for.

> [00:21] “the problem is that the official rust learning resources only tell you about the particle interpretation leaving out half the picture”
> [05:38] “a reference really is just a special kind of pointer special because it has this tick a that the compiler uses to validate that the reference never points to invalid memory”
> [05:59] “what if instead of thinking about tick a as when the reference needs to be valid we thought of it as what the reference can point to”

_Confidence note: Somewhat advanced and theory-heavy, but that is what the learner wants._

### 5. [Rust Powered Polymorphism ⚡️ With Traits](https://www.youtube.com/watch?v=CHRNj5oubwc)
Code to the Moon · 10 min · counts 10 min · intermediate, concept_explainer · covers traits · **confidence 0.70**

Compact comparison of traits with interfaces. It covers static dispatch with generics versus dyn dispatch, default methods and supertraits, which map onto Go interfaces.

> [03:03] “instead of interfaces Rust has something called traits which are very similar to interfaces but with some subtle differences”
> [04:28] “dyn refers to something called Dynamic dispatch which is in contrast to something called Static dispatch”

_Confidence note: Short intro, but nothing better on traits was found for this level._

### 6. [Introduction to Generics and Traits | Advanced Rust Part 1](https://www.youtube.com/watch?v=AnsRR-i5UWQ)
Green Tea Coding · 16 min · counts 16 min · intermediate, concept_explainer · covers traits · **confidence 0.60**

Adds trait bounds, Copy/Clone and implementing traits manually, tying them back to what the compiler enforces.

> [06:10] “traits or interfaces as they are called in most other languages are Concepts that guarantee that an object or struct provides a certain functionality”
> [08:40] “we need to make sure that the copy trait is implemented and we do this by adding the copy trait as a requirement for our type T”

_Confidence note: Partly basic generics. Skim what Go generics already taught you._

### 7. [A Simpler Way to See Results](https://www.youtube.com/watch?v=s5S2Ed5T-dc)
Logan Smith · 19 min · counts 19 min · intermediate, concept_explainer · covers err · **confidence 0.85**

Presents Result as a sum type and covers the ? operator, collecting Results, error type design, From, and thiserror/anyhow. This is the mental model for replacing Go's err returns.

> [01:02] “result is a sum type just like all other enums in Rust”
> [09:50] “the question mark is a unary post-fix operator so you use it like this”
> [12:01] “if all the results are okay you get back an OK VEC but if any of them fails the whole thing fails”
> [15:57] “I would personally use the this error crate to derive a bunch of nice trait implementations all at once”

_Confidence note: Good conceptual coverage._

### 8. [Mastering Error Handling in Rust: From Panics to thiserror & anyhow | with Nathan Stocks](https://www.youtube.com/watch?v=sZV6sz4P6QY)
Ardan Labs · 74 min · watch 20:00–1:06:40 · counts 47 min · intermediate, lecture · covers err · **confidence 0.75**

Webinar that builds a CLI with Result, ? and a custom error enum, then adds thiserror and anyhow context. This is the practical idiomatic error handling a Go dev needs. I selected the core demo section.

> [22:28] “This does the exact same thing as that match expression. If the result is an okay, then it unwraps the inner value. If the result is an error variant, then it returns the error from the function.”
> [28:39] “result because result implements the termination trait. So, I've chosen to return one of any house results wrapping the unit type, which is just empty because we don't have anything useful to return in the success case.”
> [53:59] “we can use this errors error macro to derive the display and error traits. So let's check and see if we've got those.”

_Confidence note: The timestamp window is estimated from quote times. The edges may start or end mid-topic._

### 9. [Build a Rust CLI Tool from Scratch (clap, serde, anyhow) – logscan](https://www.youtube.com/watch?v=uvP1bKTfa_Q)
Back To Code · 13 min · counts 13 min · intermediate, project_build · covers proj, life, err · **confidence 0.75**

Short CLI build that hits a real E0515 borrow error with zero-copy parsing and fixes it by moving ownership up. It also shows anyhow and clap, which is close to your porting task.

> [03:59] “Time and message are string slices ampersand STR that borrow directly from the file's text instead of copying it. That's zero copy parsing and it's very fast.”
> [05:23] “The idiomatic fix, move ownership up. Let the caller own the text and only borrow from it. The string lives in main, which outlives everything else.”
> [05:44] “Data must live at least as long as anything that borrows it. When the borrow checker complains, ask yourself, who owns this, and does it live long enough?”

_Confidence note: Fast-paced, but it applies the earlier material to a CLI._

## Considered and dropped

- [Error Handling in Rust](https://www.youtube.com/watch?v=wM6o70NAWUI): Covers Result, ? and panic only at a basic level. Logan Smith's video and the Ardan webinar go deeper, including thiserror and anyhow.
- [Rust for Go Developers: The 6 Things You Actually Need to Learn](https://www.youtube.com/watch?v=pDM_5HT2UlU): Surface-level 7-minute overview aimed at Go devs. It has no depth on the borrow checker.

_Models: agent_loop=anthropic/claude-sonnet-5.5 · cost $0.117 · 42 s_
