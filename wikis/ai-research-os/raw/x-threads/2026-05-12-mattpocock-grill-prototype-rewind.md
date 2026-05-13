---
source: https://x.com/mattpocockuk/status/2053459748532392343
date: 2026-05-12
type: thread
tags: [matt-pocock, claude-code, prototyping, grill-me, rewind, ui-design, agent-workflows, self-os]
status: processed
---

# Matt Pocock — grill-with-docs, prototype, rewind, summarize

## Summary

Matt Pocock shares a UI-design flow that combines adversarial questioning with disposable prototyping and Claude Code's rewind/summarize feature. The pattern lets the operator burn tokens freely during prototyping, then rewind back into the strategic questioning session with only the useful learnings retained.

## Extracted post

Author: Matt Pocock / `@mattpocockuk`  
Published/edited: last edited 12:58 PM · May 10, 2026  
Engagement at capture: 73 replies, 102 reposts, 2.3K likes, 2.6K bookmarks, 99.6K views

> A flow I just tried and LOVED:
>
> 1. /grill-with-docs, talking about a new bit of UI
> 2. Asks me a question I can't answer unless I prototype
> 3. /prototype
> 4. Iterate on the prototype, burning tokens freely until we get a good spot
> 5. /rewind to the question, and select 'summarize' (Claude Code feature), saying 'summarize what we learned from prototyping'
> 6. Continue the grilling session, retaining the prototype
>
> Smoooooooth

## Why it matters

This is a clean example of separating **thinking state** from **exploration state**. Instead of letting a messy prototype session pollute the main planning thread, the operator uses the prototype as a temporary branch, then compacts only the useful lessons back into the original design conversation.

## Self-OS implications

- For UI/product strategy, treat prototypes as disposable evidence-gathering branches, not as the canonical plan.
- Add a `prototype → summarize learnings → resume grill` pattern to design/planning workflows.
- This matches the user's preference for architecture/planning before implementation while still allowing empirical prototyping when a question cannot be answered abstractly.
- Could become a Hermes skill or taskOS planning convention for high-uncertainty UI/product work.

## Potential local command shape

```text
/grill-with-docs → question that needs evidence
/prototype → explore freely
/rewind → summarize prototype learnings
continue /grill-with-docs with evidence
```
