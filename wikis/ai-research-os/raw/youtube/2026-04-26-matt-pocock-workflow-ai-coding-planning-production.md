---
source: https://www.youtube.com/watch?v=-QFHIoCo-Ko
date: 2026-04-26
type: video
tags: [ai-coding, workflow, planning, prd, kanban, matt-pocock, software-engineering, agent-workflow]
---

# Full Walkthrough: Workflow for AI Coding from Planning to Production — Matt Pocock

**Speaker:** Matt Pocock (@mattpocockuk)  
**Source:** [YouTube](https://www.youtube.com/watch?v=-QFHIoCo-Ko)  
**Length:** 1:36:29  
**Core Thesis:** *Software engineering fundamentals that work for humans also work super well with AI.* This is not a "specs-to-code" paradigm where you ignore the code; the code remains your battleground.

---

## 1. The Constraints of LLMs

Before building a workflow, you must accept two weird constraints of LLMs.

### The Smart Zone vs. The Dumb Zone
LLMs have a "smart zone" and a "dumb zone." As tokens accumulate in a session, attention relationships strain quadratically.

> "By around sort of 40% or around I would say around 100k is kind of my new marker for this because it doesn't matter whether you're using 1 million uh context window or 200k. It's always going to be about this."

**Implication:** Size tasks to stay within the smart zone. Don't let the AI bite off more than it can chew.

### The Memento Problem
LLMs are like *the guy from Memento*: they continually forget and reset.

**Session Lifecycle:**
1. **System Prompt** (keep this tiny; 250k tokens here dumps you straight into the dumb zone)
2. **Exploratory Phase** (codebase exploration)
3. **Implementation Phase**
4. **Testing/Feedback Phase**

When you clear context, you **boomerang back to the system prompt state**. Matt prefers this brutal reset over "compacting" because it is deterministic.

> "This state is always the same. Always the same. Every time you do it, you clear and you go back to the beginning."

**Actionable tip:** Display exact token count in every session. Treat it like an essential status line.

---

## 2. The Full Workflow at a Glance

```
Idea/Feature Request
    ↓
Grill Me Session (Human-in-the-loop)
    ↓
PRD (Destination Document)
    ↓
Kanban Board / Vertical Slices (Journey Document)
    ↓
AFK Agent Implementation (Night Shift)
    ↓
QA, Code Review, Human Taste
```

**Key Rule:** Planning is **human-in-the-loop**. Implementation is **AFK** (away from keyboard).

---

## 3. Phase 1: Alignment with the "Grill Me" Skill

Matt argues against the "specs-to-code movement" (throwing a spec over the wall and ignoring the resulting code).

> "The code is your battleground. And so this again is where we're going."

### The Skill
Invoke a `grill me` skill with the raw brief. The prompt is extremely short and intentional:

> "Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies one by one. For each question, provide your recommended answer. Ask the questions one at a time."

### Why This Works
The goal is not a plan or an asset; it is a **shared design concept** (from Frederick P. Brooks' *The Design of Design*).

> "I needed to reach a shared understanding. I didn't need an asset. I didn't need a plan. I needed to be on the same wavelength as the AI as my agent."

- The AI asks one question at a time and offers a recommended answer.
- You can accept the recommendation, modify it, or use it to trigger team discussion.
- These sessions can last 40–100 questions. The transcript itself becomes the alignment artifact.

**Team dynamic:** Use this in "mob programming with AI" sessions. Loop in domain experts or developers as needed.

---

## 4. Phase 2: Destination & Journey Documents

### The PRD (Destination)
After grilling, generate a PRD. Matt's template includes:
- Problem statement
- Solution description
- User stories
- Implementation decisions
- Testing decisions
- **Out-of-scope section** (crucial for definition of done)

**Important:** Matt does **not** carefully review the PRD.

> "I don't tend to read these... I have reached the same wavelength as the LLM... all I'm doing is I'm just essentially checking the LLM's ability to summarize."

### From PRD to Issues (Journey)
Turn the PRD into independently grabbable issues on a **Kanban board** with blocking relationships. This creates a DAG (directed acyclic graph) that allows **parallelization**.

**Critical technique: Vertical Slices (Tracer Bullets)**
AI defaults to coding **horizontally** (all DB layer, then all API layer, then all frontend). This is bad because you get zero integration feedback until the final phase.

> "Tracer bullets... increase our level of feedback and we get near instant feedback on what we're building because without that the AI is kind of coding blind."

A vertical slice crosses all necessary layers (schema + service + minimal UI) so the agent can test the full flow immediately.

**Avoid:** Sequential numbered phase plans (Phase 1, Phase 2...). They cannot be parallelized.

---

## 5. Phase 3: AFK Implementation

### The Ralph Loop
Once issues are sliced, the human steps back. The agent enters "Ralph loop" mode (named after Ralph Wiggum: "just make a small change that gets us closer").

**`once.sh` concept:**
The agent runs a script that:
1. Picks the next unblocked issue
2. Implements it in a single focused pass
3. Runs tests
4. Commits
5. Repeats

This lets the agent work autonomously through the night (the "Night Shift").

---

## Key Takeaways

1. **Smart Zone:** Keep tasks under ~100k tokens. Display token count constantly.
2. **Grill Me:** Use adversarial interviewing (40–100 questions) to reach shared understanding before building.
3. **PRD is a checkpoint, not a contract.** Don't over-review it — the alignment is what matters.
4. **Vertical Slices > Horizontal Layers.** Cross-cutting slices give immediate integration feedback.
5. **AFK Agent:** Once planned, let the agent work in a loop through the night.
6. **Code is your battleground.** Don't fall for "specs to code" — stay engaged with the implementation.
