---
source: https://x.com/garrytan/status/2046876981711769720
date: 2026-04-26
type: thread
tags: [skillify, agent-reliability, testing, skills, openclaw, gbrain, langchain, agent-workflow]
---

# How to really stop your agents from making the same mistakes — Garry Tan

**Author:** Garry Tan (@garrytan)  
**Posted:** Apr 22, 2026  
**Engagement:** 788K views, 4.3K bookmarks, 1.5K likes  
**Related repos:** [gstack](https://github.com/garrytan/gstack), [gbrain](https://github.com/garrytan/gbrain)

---

> "Most AI agent 'reliability' is vibes-based. Prompt tweaks. Bigger system messages. 'Please don't hallucinate' incantations. That stuff decays the moment the conversation gets complex."

---

## The Problem: Frameworks Give You Tools, Not Workflows

Garry Tan critiques LangChain ($160M raised, billion-dollar valuation) for providing sophisticated testing primitives (LangSmith: trajectory evals, trace-to-dataset pipelines, LLM-as-judge, regression suites) but **no opinionated workflow** for what to test, in what order, or when you're done.

> "A great many users of AI still don't test their agents at all, because the framework they chose probably gave them a gym membership without a workout plan."

---

## Skillify: The Pattern

**"Skillify"** = Every agent failure becomes a permanent structural fix: a skill with tests that run every day, forever.

### Two Real Failures

**Failure 1: The Trip That Was Already in the Database**  
Agent searched live calendar APIs and email for a 10-year-old trip, spinning for 5 minutes. The answer was already in a local knowledge base (3,146 calendar files, indexed, one grep away). The agent just didn't look there first.

**Failure 2: "28 Minutes"**  
Agent said next meeting was in 28 minutes. Reality: 88 minutes. A script (`context-now.mjs`) already existed that outputs the correct answer in 50ms. The agent did UTC→PT timezone math in its head instead.

Both failures share the same shape: **deterministic work done in latent (LLM reasoning) space instead of deterministic (code) space.**

---

## The 10-Step Skillify Checklist

| Step | What | Example |
|------|------|---------|
| 1 | **SKILL.md** | The contract: name, triggers, rules |
| 2 | **Deterministic code** | `scripts/*.mjs` — no LLM for what code can do |
| 3 | **Unit tests** | vitest, pure functions, fixtures |
| 4 | **Integration tests** | Live endpoints, real data |
| 5 | **LLM evals** | LLM-as-judge for quality/correctness |
| 6 | **Resolver trigger** | Entry in AGENTS.md routing table |
| 7 | **Resolver eval** | Verify the trigger actually routes correctly |
| 8 | **Check-resolvable + DRY audit** | No unreachable skills, no overlapping triggers |
| 9 | **E2E smoke test** | Full pipeline: ask → skill → script → answer |
| 10 | **Brain filing rules** | Where knowledge base writes go |

> "A feature that doesn't pass all ten is not a skill. It's just code that happens to work today."

---

## Skillify as a Verb

Garry's actual workflow: prototype in conversation, see it work, say **"skillify it"** — and the ad-hoc session becomes durable infrastructure with tests, resolver entry, and documentation.

Examples:
- OAuth webhook integration → webhook skill
- Headless vs headed browser needs → browser skill
- ngrok link validation → link-check skill
- Calendar double-booking detection → calendar-check skill

> "One message. The agent writes the skill. Now every future session that needs a browser gets routed to the right tool automatically."

---

## The 10 Steps in Detail

### Step 1: SKILL.md
A markdown procedure that teaches the model *how* to approach a task. The user supplies the *what*.

Example `calendar-recall`:
```yaml
name: calendar-recall
description: "Brain-first historical calendar lookup. ALWAYS use
  this before any live API for any event not in the future or
  the last 48 hours."
```

### Step 2: Deterministic Code
The agent itself writes the script. The skill tells it how. The script does the work.

```bash
$ node scripts/calendar-recall.mjs search "Singapore"
Found 2 matching day(s):
── 2016-05-07 ──
  Flight to Singapore, Mandarin Oriental check-in
```

### Step 3: Unit Tests
Classic vitest. 179 tests across 5 suites, under 2 seconds.

### Step 4: Integration Tests
Hit live endpoints and real data. Catches bugs that clean fixtures miss.

### Step 5: LLM Evals
LLM-as-judge: feed the agent a message like "my flight leaves in 45 minutes" and check whether it runs `context-now.mjs` before answering or tries mental math.

> "The most honest eval heuristic I've found: search your conversation history for when you said 'fucking shit' or 'wtf.' Those are the test cases you're missing."

### Step 6: Resolver Trigger
Routing table in AGENTS.md: when task type X appears, load skill Y.

### Step 7: Resolver Eval
50+ test cases verifying intent → skill routing. Catches false negatives (skill should fire but doesn't) and false positives (wrong skill fires).

### Step 8: Check-Resolvable + DRY Audit
Meta-test walking the full chain: resolver → SKILL.md → script/cron. First run found **6 unreachable skills out of 40+** (15% of capabilities were dark).

### Step 9: E2E Smoke Test
Ask "when did I go to Singapore?" and verify the full pipeline works end-to-end.

### Step 10: Brain Filing Rules
Every skill that writes to the knowledge base needs to know where things go (people/, companies/, civic/, etc.). Caught 10 of 13 skills filing to wrong directories.

---

## GBrain

GBrain is Garry's open-source knowledge engine that manages brain repos, runs evals, and enforces quality gates.

- `gbrain doctor --fix` auto-repairs DRY violations, replaces duplicated blocks with convention references
- **SkillPacks** = portable bundles of skills, triggers, scripts, and tests installable into any agent setup

---

## Why Hermes Agent Isn't Enough on Its Own

Hermes Agent (Nous Research) has `skill_manage` for auto-creating skills — procedural memory the agent earns on its own. But:
- No unit tests on deterministic code
- No resolver evals
- No check-resolvable for dark skills
- No DRY audit for duplicates
- No daily health check

> "Hermes handles creation beautifully. GBrain handles verification. You need both."

---

## The Big Idea

> "In a healthy software engineering team, every bug gets a test. That test lives forever. The bug becomes structurally impossible to recur. AI agents should work the same way."

Every failure → skill. Every skill → evals. Every eval → daily. The agent's judgment improves permanently, not just for the current session.

> "Boil the ocean. Make your agent do something, then skillify it. You do that every day and you have a god damn smart OpenClaw that does everything you want it to do."
