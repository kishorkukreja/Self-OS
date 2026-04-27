---
status: processed
---
     1|---
     2|source: https://x.com/garrytan/status/2046876981711769720
     3|date: 2026-04-26
     4|type: thread
     5|tags: [skillify, agent-reliability, testing, skills, openclaw, gbrain, langchain, agent-workflow]
     6|---
     7|
     8|# How to really stop your agents from making the same mistakes — Garry Tan
     9|
    10|**Author:** Garry Tan (@garrytan)  
    11|**Posted:** Apr 22, 2026  
    12|**Engagement:** 788K views, 4.3K bookmarks, 1.5K likes  
    13|**Related repos:** [gstack](https://github.com/garrytan/gstack), [gbrain](https://github.com/garrytan/gbrain)
    14|
    15|---
    16|
    17|> "Most AI agent 'reliability' is vibes-based. Prompt tweaks. Bigger system messages. 'Please don't hallucinate' incantations. That stuff decays the moment the conversation gets complex."
    18|
    19|---
    20|
    21|## The Problem: Frameworks Give You Tools, Not Workflows
    22|
    23|Garry Tan critiques LangChain ($160M raised, billion-dollar valuation) for providing sophisticated testing primitives (LangSmith: trajectory evals, trace-to-dataset pipelines, LLM-as-judge, regression suites) but **no opinionated workflow** for what to test, in what order, or when you're done.
    24|
    25|> "A great many users of AI still don't test their agents at all, because the framework they chose probably gave them a gym membership without a workout plan."
    26|
    27|---
    28|
    29|## Skillify: The Pattern
    30|
    31|**"Skillify"** = Every agent failure becomes a permanent structural fix: a skill with tests that run every day, forever.
    32|
    33|### Two Real Failures
    34|
    35|**Failure 1: The Trip That Was Already in the Database**  
    36|Agent searched live calendar APIs and email for a 10-year-old trip, spinning for 5 minutes. The answer was already in a local knowledge base (3,146 calendar files, indexed, one grep away). The agent just didn't look there first.
    37|
    38|**Failure 2: "28 Minutes"**  
    39|Agent said next meeting was in 28 minutes. Reality: 88 minutes. A script (`context-now.mjs`) already existed that outputs the correct answer in 50ms. The agent did UTC→PT timezone math in its head instead.
    40|
    41|Both failures share the same shape: **deterministic work done in latent (LLM reasoning) space instead of deterministic (code) space.**
    42|
    43|---
    44|
    45|## The 10-Step Skillify Checklist
    46|
    47|| Step | What | Example |
    48||------|------|---------|
    49|| 1 | **SKILL.md** | The contract: name, triggers, rules |
    50|| 2 | **Deterministic code** | `scripts/*.mjs` — no LLM for what code can do |
    51|| 3 | **Unit tests** | vitest, pure functions, fixtures |
    52|| 4 | **Integration tests** | Live endpoints, real data |
    53|| 5 | **LLM evals** | LLM-as-judge for quality/correctness |
    54|| 6 | **Resolver trigger** | Entry in AGENTS.md routing table |
    55|| 7 | **Resolver eval** | Verify the trigger actually routes correctly |
    56|| 8 | **Check-resolvable + DRY audit** | No unreachable skills, no overlapping triggers |
    57|| 9 | **E2E smoke test** | Full pipeline: ask → skill → script → answer |
    58|| 10 | **Brain filing rules** | Where knowledge base writes go |
    59|
    60|> "A feature that doesn't pass all ten is not a skill. It's just code that happens to work today."
    61|
    62|---
    63|
    64|## Skillify as a Verb
    65|
    66|Garry's actual workflow: prototype in conversation, see it work, say **"skillify it"** — and the ad-hoc session becomes durable infrastructure with tests, resolver entry, and documentation.
    67|
    68|Examples:
    69|- OAuth webhook integration → webhook skill
    70|- Headless vs headed browser needs → browser skill
    71|- ngrok link validation → link-check skill
    72|- Calendar double-booking detection → calendar-check skill
    73|
    74|> "One message. The agent writes the skill. Now every future session that needs a browser gets routed to the right tool automatically."
    75|
    76|---
    77|
    78|## The 10 Steps in Detail
    79|
    80|### Step 1: SKILL.md
    81|A markdown procedure that teaches the model *how* to approach a task. The user supplies the *what*.
    82|
    83|Example `calendar-recall`:
    84|```yaml
    85|name: calendar-recall
    86|description: "Brain-first historical calendar lookup. ALWAYS use
    87|  this before any live API for any event not in the future or
    88|  the last 48 hours."
    89|```
    90|
    91|### Step 2: Deterministic Code
    92|The agent itself writes the script. The skill tells it how. The script does the work.
    93|
    94|```bash
    95|$ node scripts/calendar-recall.mjs search "Singapore"
    96|Found 2 matching day(s):
    97|── 2016-05-07 ──
    98|  Flight to Singapore, Mandarin Oriental check-in
    99|```
   100|
   101|### Step 3: Unit Tests
   102|Classic vitest. 179 tests across 5 suites, under 2 seconds.
   103|
   104|### Step 4: Integration Tests
   105|Hit live endpoints and real data. Catches bugs that clean fixtures miss.
   106|
   107|### Step 5: LLM Evals
   108|LLM-as-judge: feed the agent a message like "my flight leaves in 45 minutes" and check whether it runs `context-now.mjs` before answering or tries mental math.
   109|
   110|> "The most honest eval heuristic I've found: search your conversation history for when you said 'fucking shit' or 'wtf.' Those are the test cases you're missing."
   111|
   112|### Step 6: Resolver Trigger
   113|Routing table in AGENTS.md: when task type X appears, load skill Y.
   114|
   115|### Step 7: Resolver Eval
   116|50+ test cases verifying intent → skill routing. Catches false negatives (skill should fire but doesn't) and false positives (wrong skill fires).
   117|
   118|### Step 8: Check-Resolvable + DRY Audit
   119|Meta-test walking the full chain: resolver → SKILL.md → script/cron. First run found **6 unreachable skills out of 40+** (15% of capabilities were dark).
   120|
   121|### Step 9: E2E Smoke Test
   122|Ask "when did I go to Singapore?" and verify the full pipeline works end-to-end.
   123|
   124|### Step 10: Brain Filing Rules
   125|Every skill that writes to the knowledge base needs to know where things go (people/, companies/, civic/, etc.). Caught 10 of 13 skills filing to wrong directories.
   126|
   127|---
   128|
   129|## GBrain
   130|
   131|GBrain is Garry's open-source knowledge engine that manages brain repos, runs evals, and enforces quality gates.
   132|
   133|- `gbrain doctor --fix` auto-repairs DRY violations, replaces duplicated blocks with convention references
   134|- **SkillPacks** = portable bundles of skills, triggers, scripts, and tests installable into any agent setup
   135|
   136|---
   137|
   138|## Why Hermes Agent Isn't Enough on Its Own
   139|
   140|Hermes Agent (Nous Research) has `skill_manage` for auto-creating skills — procedural memory the agent earns on its own. But:
   141|- No unit tests on deterministic code
   142|- No resolver evals
   143|- No check-resolvable for dark skills
   144|- No DRY audit for duplicates
   145|- No daily health check
   146|
   147|> "Hermes handles creation beautifully. GBrain handles verification. You need both."
   148|
   149|---
   150|
   151|## The Big Idea
   152|
   153|> "In a healthy software engineering team, every bug gets a test. That test lives forever. The bug becomes structurally impossible to recur. AI agents should work the same way."
   154|
   155|Every failure → skill. Every skill → evals. Every eval → daily. The agent's judgment improves permanently, not just for the current session.
   156|
   157|> "Boil the ocean. Make your agent do something, then skillify it. You do that every day and you have a god damn smart OpenClaw that does everything you want it to do."
   158|