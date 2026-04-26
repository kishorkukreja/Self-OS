---
source: X/Twitter post by Matt Pocock (paraphrased/quoted)
date: 2026-04-26
type: article
tags: [afk-agents, day-shift, night-shift, agent-workflow, sandcastle, evalite, software-factory, planning, review, qa]
---

# How to Ship with AFK Agents — Day Shift vs Night Shift (Matt Pocock)

**Author:** Matt Pocock  
**Repos shipped with this workflow:** `mattpocock/evalite`, `mattpocock/sandcastle`, `mattpocock/software-factory`

---

> "Tons of folks are piling in here saying that AFK agents are a myth. I have been using them to ship these GitHub repos..."

---

## Definitions

**Day shift** = planning / review / QA  
**Night shift** = AFK implementation

---

## Day Shift (Part 1) — Planning

1. **Use `/grill-me`** to align with the AI
2. **Use `/to-prd`** and `/to-issues`** to create:
   - A **PRD** (the destination)
   - Implementation steps as **separate tickets**, which can be grabbed in parallel (the journey)
3. The **PRD is a ticket**, but it's not an actionable step. You just put the user stories there.

> "This is pure requirements gathering shit, same as it ever was."

---

## Night Shift — AFK Implementation

1. Run a **planner agent** which looks at all the tickets and sees what can be worked on now, and what's blocked
2. The planner agent then kicks off **multiple agents** (sandboxed using **Sandcastle**, his OSS tool) to implement the code
3. Automated **reviewer agent** looks at the commits produced — one agent per implementation. Checks:
   - Alignment to the original PRD
   - Code quality
4. These commits end up on **branches that get PR'd to main**
5. The planner agent runs again until all work has been completed

> "The review is a crucial step — it's saved me MANY times. I am planning to massively increase the amount of review I do, hopefully with multiple agents."

---

## Why AFK Agents Sometimes Produce Bad Code

| Cause | Description |
|-------|-------------|
| **a. Bad original plan** | Best solution was something different |
| **b. Unknown unknowns** | Plan didn't account for everything; AI made bad decisions during coding |
| **c. AI shat the bed** | Twice — once in review, once during implementation |
| **d. Bad codebase** | Feedback loops don't tell the agent if it did a good job |

---

## Day Shift (Part 2) — QA

1. **QA all branches** created
2. **Create follow-up issues**, potentially editing the original PRD to adjust the destination

> "This will usually take a long time, often as long as planning. But then you kick off the night shift again."

Once QA is done, review important bits of code manually, usually in PRs. There isn't anything better than the PR UI right now.

---

## Wake-Up Calls

1. **If you let the AI run all night unbounded by planning, it's going to produce shit code**
2. Mostly, loops **finish before bedtime** — night shift catches up to the day shift
3. The **only reason for AFK** is to automate review and not care about latency
4. **Night and day shift run in parallel** — can't plan too far ahead without working code to base plans on. Aggressively QA stuff that lands.

---

## Related Tools

| Repo | Purpose |
|------|---------|
| `mattpocock/evalite` | Evaluation framework |
| `mattpocock/sandcastle` | Sandboxing for parallel AFK agents |
| `mattpocock/software-factory` | Software factory (possibly public) |
