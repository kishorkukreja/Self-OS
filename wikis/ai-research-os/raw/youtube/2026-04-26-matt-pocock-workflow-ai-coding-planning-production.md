---
status: processed
---
     1|---
     2|source: https://www.youtube.com/watch?v=-QFHIoCo-Ko
     3|date: 2026-04-26
     4|type: video
     5|tags: [ai-coding, workflow, planning, prd, kanban, matt-pocock, software-engineering, agent-workflow]
     6|---
     7|
     8|# Full Walkthrough: Workflow for AI Coding from Planning to Production — Matt Pocock
     9|
    10|**Speaker:** Matt Pocock (@mattpocockuk)  
    11|**Source:** [YouTube](https://www.youtube.com/watch?v=-QFHIoCo-Ko)  
    12|**Length:** 1:36:29  
    13|**Core Thesis:** *Software engineering fundamentals that work for humans also work super well with AI.* This is not a "specs-to-code" paradigm where you ignore the code; the code remains your battleground.
    14|
    15|---
    16|
    17|## 1. The Constraints of LLMs
    18|
    19|Before building a workflow, you must accept two weird constraints of LLMs.
    20|
    21|### The Smart Zone vs. The Dumb Zone
    22|LLMs have a "smart zone" and a "dumb zone." As tokens accumulate in a session, attention relationships strain quadratically.
    23|
    24|> "By around sort of 40% or around I would say around 100k is kind of my new marker for this because it doesn't matter whether you're using 1 million uh context window or 200k. It's always going to be about this."
    25|
    26|**Implication:** Size tasks to stay within the smart zone. Don't let the AI bite off more than it can chew.
    27|
    28|### The Memento Problem
    29|LLMs are like *the guy from Memento*: they continually forget and reset.
    30|
    31|**Session Lifecycle:**
    32|1. **System Prompt** (keep this tiny; 250k tokens here dumps you straight into the dumb zone)
    33|2. **Exploratory Phase** (codebase exploration)
    34|3. **Implementation Phase**
    35|4. **Testing/Feedback Phase**
    36|
    37|When you clear context, you **boomerang back to the system prompt state**. Matt prefers this brutal reset over "compacting" because it is deterministic.
    38|
    39|> "This state is always the same. Always the same. Every time you do it, you clear and you go back to the beginning."
    40|
    41|**Actionable tip:** Display exact token count in every session. Treat it like an essential status line.
    42|
    43|---
    44|
    45|## 2. The Full Workflow at a Glance
    46|
    47|```
    48|Idea/Feature Request
    49|    ↓
    50|Grill Me Session (Human-in-the-loop)
    51|    ↓
    52|PRD (Destination Document)
    53|    ↓
    54|Kanban Board / Vertical Slices (Journey Document)
    55|    ↓
    56|AFK Agent Implementation (Night Shift)
    57|    ↓
    58|QA, Code Review, Human Taste
    59|```
    60|
    61|**Key Rule:** Planning is **human-in-the-loop**. Implementation is **AFK** (away from keyboard).
    62|
    63|---
    64|
    65|## 3. Phase 1: Alignment with the "Grill Me" Skill
    66|
    67|Matt argues against the "specs-to-code movement" (throwing a spec over the wall and ignoring the resulting code).
    68|
    69|> "The code is your battleground. And so this again is where we're going."
    70|
    71|### The Skill
    72|Invoke a `grill me` skill with the raw brief. The prompt is extremely short and intentional:
    73|
    74|> "Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies one by one. For each question, provide your recommended answer. Ask the questions one at a time."
    75|
    76|### Why This Works
    77|The goal is not a plan or an asset; it is a **shared design concept** (from Frederick P. Brooks' *The Design of Design*).
    78|
    79|> "I needed to reach a shared understanding. I didn't need an asset. I didn't need a plan. I needed to be on the same wavelength as the AI as my agent."
    80|
    81|- The AI asks one question at a time and offers a recommended answer.
    82|- You can accept the recommendation, modify it, or use it to trigger team discussion.
    83|- These sessions can last 40–100 questions. The transcript itself becomes the alignment artifact.
    84|
    85|**Team dynamic:** Use this in "mob programming with AI" sessions. Loop in domain experts or developers as needed.
    86|
    87|---
    88|
    89|## 4. Phase 2: Destination & Journey Documents
    90|
    91|### The PRD (Destination)
    92|After grilling, generate a PRD. Matt's template includes:
    93|- Problem statement
    94|- Solution description
    95|- User stories
    96|- Implementation decisions
    97|- Testing decisions
    98|- **Out-of-scope section** (crucial for definition of done)
    99|
   100|**Important:** Matt does **not** carefully review the PRD.
   101|
   102|> "I don't tend to read these... I have reached the same wavelength as the LLM... all I'm doing is I'm just essentially checking the LLM's ability to summarize."
   103|
   104|### From PRD to Issues (Journey)
   105|Turn the PRD into independently grabbable issues on a **Kanban board** with blocking relationships. This creates a DAG (directed acyclic graph) that allows **parallelization**.
   106|
   107|**Critical technique: Vertical Slices (Tracer Bullets)**
   108|AI defaults to coding **horizontally** (all DB layer, then all API layer, then all frontend). This is bad because you get zero integration feedback until the final phase.
   109|
   110|> "Tracer bullets... increase our level of feedback and we get near instant feedback on what we're building because without that the AI is kind of coding blind."
   111|
   112|A vertical slice crosses all necessary layers (schema + service + minimal UI) so the agent can test the full flow immediately.
   113|
   114|**Avoid:** Sequential numbered phase plans (Phase 1, Phase 2...). They cannot be parallelized.
   115|
   116|---
   117|
   118|## 5. Phase 3: AFK Implementation
   119|
   120|### The Ralph Loop
   121|Once issues are sliced, the human steps back. The agent enters "Ralph loop" mode (named after Ralph Wiggum: "just make a small change that gets us closer").
   122|
   123|**`once.sh` concept:**
   124|The agent runs a script that:
   125|1. Picks the next unblocked issue
   126|2. Implements it in a single focused pass
   127|3. Runs tests
   128|4. Commits
   129|5. Repeats
   130|
   131|This lets the agent work autonomously through the night (the "Night Shift").
   132|
   133|---
   134|
   135|## Key Takeaways
   136|
   137|1. **Smart Zone:** Keep tasks under ~100k tokens. Display token count constantly.
   138|2. **Grill Me:** Use adversarial interviewing (40–100 questions) to reach shared understanding before building.
   139|3. **PRD is a checkpoint, not a contract.** Don't over-review it — the alignment is what matters.
   140|4. **Vertical Slices > Horizontal Layers.** Cross-cutting slices give immediate integration feedback.
   141|5. **AFK Agent:** Once planned, let the agent work in a loop through the night.
   142|6. **Code is your battleground.** Don't fall for "specs to code" — stay engaged with the implementation.
   143|