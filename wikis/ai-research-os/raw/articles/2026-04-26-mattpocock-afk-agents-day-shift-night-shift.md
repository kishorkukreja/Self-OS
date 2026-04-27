---
status: processed
---
     1|---
     2|source: X/Twitter post by Matt Pocock (paraphrased/quoted)
     3|date: 2026-04-26
     4|type: article
     5|tags: [afk-agents, day-shift, night-shift, agent-workflow, sandcastle, evalite, software-factory, planning, review, qa]
     6|---
     7|
     8|# How to Ship with AFK Agents — Day Shift vs Night Shift (Matt Pocock)
     9|
    10|**Author:** Matt Pocock  
    11|**Repos shipped with this workflow:** `mattpocock/evalite`, `mattpocock/sandcastle`, `mattpocock/software-factory`
    12|
    13|---
    14|
    15|> "Tons of folks are piling in here saying that AFK agents are a myth. I have been using them to ship these GitHub repos..."
    16|
    17|---
    18|
    19|## Definitions
    20|
    21|**Day shift** = planning / review / QA  
    22|**Night shift** = AFK implementation
    23|
    24|---
    25|
    26|## Day Shift (Part 1) — Planning
    27|
    28|1. **Use `/grill-me`** to align with the AI
    29|2. **Use `/to-prd`** and `/to-issues`** to create:
    30|   - A **PRD** (the destination)
    31|   - Implementation steps as **separate tickets**, which can be grabbed in parallel (the journey)
    32|3. The **PRD is a ticket**, but it's not an actionable step. You just put the user stories there.
    33|
    34|> "This is pure requirements gathering shit, same as it ever was."
    35|
    36|---
    37|
    38|## Night Shift — AFK Implementation
    39|
    40|1. Run a **planner agent** which looks at all the tickets and sees what can be worked on now, and what's blocked
    41|2. The planner agent then kicks off **multiple agents** (sandboxed using **Sandcastle**, his OSS tool) to implement the code
    42|3. Automated **reviewer agent** looks at the commits produced — one agent per implementation. Checks:
    43|   - Alignment to the original PRD
    44|   - Code quality
    45|4. These commits end up on **branches that get PR'd to main**
    46|5. The planner agent runs again until all work has been completed
    47|
    48|> "The review is a crucial step — it's saved me MANY times. I am planning to massively increase the amount of review I do, hopefully with multiple agents."
    49|
    50|---
    51|
    52|## Why AFK Agents Sometimes Produce Bad Code
    53|
    54|| Cause | Description |
    55||-------|-------------|
    56|| **a. Bad original plan** | Best solution was something different |
    57|| **b. Unknown unknowns** | Plan didn't account for everything; AI made bad decisions during coding |
    58|| **c. AI shat the bed** | Twice — once in review, once during implementation |
    59|| **d. Bad codebase** | Feedback loops don't tell the agent if it did a good job |
    60|
    61|---
    62|
    63|## Day Shift (Part 2) — QA
    64|
    65|1. **QA all branches** created
    66|2. **Create follow-up issues**, potentially editing the original PRD to adjust the destination
    67|
    68|> "This will usually take a long time, often as long as planning. But then you kick off the night shift again."
    69|
    70|Once QA is done, review important bits of code manually, usually in PRs. There isn't anything better than the PR UI right now.
    71|
    72|---
    73|
    74|## Wake-Up Calls
    75|
    76|1. **If you let the AI run all night unbounded by planning, it's going to produce shit code**
    77|2. Mostly, loops **finish before bedtime** — night shift catches up to the day shift
    78|3. The **only reason for AFK** is to automate review and not care about latency
    79|4. **Night and day shift run in parallel** — can't plan too far ahead without working code to base plans on. Aggressively QA stuff that lands.
    80|
    81|---
    82|
    83|## Related Tools
    84|
    85|| Repo | Purpose |
    86||------|---------|
    87|| `mattpocock/evalite` | Evaluation framework |
    88|| `mattpocock/sandcastle` | Sandboxing for parallel AFK agents |
    89|| `mattpocock/software-factory` | Software factory (possibly public) |
    90|