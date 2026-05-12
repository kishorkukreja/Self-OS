---
source: https://x.com/Mnilax/status/2053116311132155938?s=20
date: 2026-05-11
type: thread
tags: [claude-code, claude-md, coding-agents, development-rules, agent-guardrails, qa, self-os]
status: processed
---

# Mnimiy: 12-rule CLAUDE.md template for Claude Code

## Summary
Mnimiy argues that the original four Karpathy/Forrest Chang `CLAUDE.md` rules reduce common Claude Code errors, but no longer cover the full failure surface of May 2026 agent-driven development. The post adds eight more rules based on six weeks of testing across 30 codebases, targeting failures such as deterministic decisions delegated to models, runaway context usage, conflicting patterns, shallow tests, missing checkpoints, convention drift, and silent failures. The article frames `CLAUDE.md` as a compact behavioral contract, not a preference dump.

## Key points
- The original four rules are: think before coding, simplicity first, surgical changes, and goal-driven execution.
- The eight added rules cover: model-vs-code boundaries, token budgets, surfacing conflicts, read-before-write, intentful tests, checkpoints, convention matching, and fail-loud behavior.
- The author claims mistake rate dropped from 41% to 3% with the 12-rule template across 30 codebases, while compliance stayed roughly similar to the original 4-rule version.
- `CLAUDE.md` should stay compact: beyond ~200 lines, rule compliance reportedly drops because important rules get buried.
- Rules should correspond to concrete failure modes; vague identity prompts like “be senior” or “be careful” do not work.

## Why it matters
This is directly relevant to Self-OS/Hermes development because it provides a concise operating contract for coding-agent work. The strongest finding is that agent reliability is improved less by telling models to be careful and more by encoding explicit behavioral guardrails: inspect before editing, keep changes surgical, use code for deterministic logic, checkpoint long work, verify intent, and fail visibly.

## Self-OS / Hermes action taken
- The 12-rule development contract was added to the `software-project-workflows` skill at `references/claude-md-12-rule-development-contract.md`.
- The skill's shared operating principles were patched to apply these rules during development/implementation work.
- A compact memory was saved so future development work should load/use the `software-project-workflows` contract.

## The 12 rules, compact form
1. Think Before Coding.
2. Simplicity First.
3. Surgical Changes.
4. Goal-Driven Execution.
5. Use the model only for judgment calls.
6. Token budgets are not advisory.
7. Surface conflicts, do not average them.
8. Read before you write.
9. Tests verify intent, not just behavior.
10. Checkpoint after every significant step.
11. Match the codebase's conventions, even if you disagree.
12. Fail loud.

## Raw content
Mnimiy (@Mnilax)
Karpathy's 4 CLAUDE.md rules cut Claude mistakes from 41% to 11%. After 30 codebases, I added 8 more

In late January 2026, Andrej Karpathy posted a thread complaining about how Claude writes code. Three failure modes: silent wrong assumptions, over-complication, orthogonal damage to code it shouldn't have touched.

Forrest Chang read the thread, packaged the complaints into 4 behavioral rules in a single CLAUDE.md file, and dropped it on GitHub. It hit 5,828 stars in the first day. 60,000 bookmarks in two weeks. 120,000 stars today. The fastest-growing single-file repo of 2026.

Then I tested it on 30 codebases over 6 weeks.

The 4 rules work. Mistakes that used to happen ~40% of the time dropped to under 3% on tasks that played to their strengths. But the template was built to fix code-writing mistakes from January.

The Claude Code ecosystem in May 2026 has different problems — agent fights, hook cascades, skill loading conflicts, multi-step workflows that break across sessions.

So I added 8 more rules. Below: the full 12-rule CLAUDE.md, why each one earned its place, and the 4 places where the original Karpathy template silently breaks.

Why this matters
Claude Code's CLAUDE.md is the most under-leveraged file in the entire AI coding stack. Most developers either:
- Treat it as a dump for every preference they've ever had, bloated to 4,000+ tokens, compliance drops to 30%
- Skip it entirely and prompt every time — 5x token waste, no consistency between sessions
- Copy a template once and forget. Works for two weeks, then breaks silently as their codebase shifts

The official Anthropic docs are explicit: CLAUDE.md is advisory. Claude follows it about 80% of the time. Past 200 lines, compliance drops sharply because important rules get buried in the noise.

The original 4 rules
Rule 1 — Think Before Coding. No silent assumptions. State what you're assuming. Surface tradeoffs. Ask before guessing. Push back when a simpler approach exists.
Rule 2 — Simplicity First. Minimum code that solves the problem. No speculative features. No abstractions for single-use code. If a senior engineer would call it overcomplicated — simplify.
Rule 3 — Surgical Changes. Touch only what you must. Don't "improve" adjacent code, comments, or formatting. Don't refactor what isn't broken. Match existing style.
Rule 4 — Goal-Driven Execution. Define success criteria. Loop until verified. Don't tell Claude what steps to follow, tell it what success looks like and let it iterate.

Rule 5 — Use the model only for judgment calls
Use Claude for: classification, drafting, summarization, extraction from unstructured text.
Do NOT use Claude for: routing, retries, status-code handling, deterministic transforms.
If a status code already answers the question, plain code answers the question.

Rule 6 — Token budgets are not advisory
Per-task budget: 4,000 tokens.
Per-session budget: 30,000 tokens.
If a task is approaching budget, summarize and start fresh. Do not push through.
Surfacing the breach > silently overrunning.

Rule 7 — Surface conflicts, don't average them
If two existing patterns in the codebase contradict, don't blend them.
Pick one (the more recent / more tested), explain why, and flag the other for cleanup.
"Average" code that satisfies both rules is the worst code.

Rule 8 — Read before you write
Before adding code in a file, read the file's exports, the immediate caller, and any obvious shared utilities.
If you don't understand why existing code is structured the way it is, ask before adding to it.
"Looks orthogonal to me" is the most dangerous phrase in this codebase.

Rule 9 — Tests verify intent, not just behavior
Every test must encode WHY the behavior matters, not just WHAT it does.
A test like `expect(getUserName()).toBe('John')` is worthless if the function takes a hardcoded ID.
If you can't write a test that would fail when business logic changes, the function is wrong.

Rule 10 — Checkpoint after every significant step
After completing each step in a multi-step task: summarize what was done, what's verified, what's left.
Don't continue from a state you can't describe back to me.
If you lose track, stop and restate.

Rule 11 — Match the codebase's conventions, even if you disagree
If the codebase uses snake_case and you'd prefer camelCase: snake_case.
If the codebase uses class-based components and you'd prefer hooks: class-based.
Disagreement is a separate conversation. Inside the codebase, conformance > taste.
If you genuinely think the convention is harmful, surface it. Don't fork it silently.

Rule 12 — Fail loud
If you can't be sure something worked, say so explicitly.
"Migration completed" is wrong if 30 records were skipped silently.
"Tests pass" is wrong if you skipped any.
"Feature works" is wrong if you didn't verify the edge case I asked about.
Default to surfacing uncertainty, not hiding it.

Where Karpathy's template silently breaks:
1. Long-running agent tasks: no budget rule, checkpoint rule, or fail-loud rule.
2. Multi-codebase consistency: "match existing style" assumes one style; monorepos have many.
3. Test quality: "tests pass" is not enough if tests do not encode intent.
4. Production vs prototype: simplicity can overfire on prototypes that need exploratory scaffolding.

What didn't work: generic rules from Reddit/X, more than 12 rules, tooling-dependent rules, heavy examples in CLAUDE.md, vague phrases like "be careful" or identity prompts like "be senior."

Copy-paste ready template:
# CLAUDE.md — 12-rule template

These rules apply to every task in this project unless explicitly overridden.
Bias: caution over speed on non-trivial work. Use judgment on trivial tasks.

## Rule 1 — Think Before Coding
State assumptions explicitly. If uncertain, ask rather than guess.
Present multiple interpretations when ambiguity exists.
Push back when a simpler approach exists.
Stop when confused. Name what's unclear.

## Rule 2 — Simplicity First
Minimum code that solves the problem. Nothing speculative.
No features beyond what was asked. No abstractions for single-use code.
Test: would a senior engineer say this is overcomplicated? If yes, simplify.

## Rule 3 — Surgical Changes
Touch only what you must. Clean up only your own mess.
Don't "improve" adjacent code, comments, or formatting.
Don't refactor what isn't broken. Match existing style.

## Rule 4 — Goal-Driven Execution
Define success criteria. Loop until verified.
Don't follow steps. Define success and iterate.
Strong success criteria let you loop independently.

## Rule 5 — Use the model only for judgment calls
Use me for: classification, drafting, summarization, extraction.
Do NOT use me for: routing, retries, deterministic transforms.
If code can answer, code answers.

## Rule 6 — Token budgets are not advisory
Per-task: 4,000 tokens. Per-session: 30,000 tokens.
If approaching budget, summarize and start fresh.
Surface the breach. Do not silently overrun.

## Rule 7 — Surface conflicts, don't average them
If two patterns contradict, pick one (more recent / more tested).
Explain why. Flag the other for cleanup.
Don't blend conflicting patterns.

## Rule 8 — Read before you write
Before adding code, read exports, immediate callers, shared utilities.
"Looks orthogonal" is dangerous. If unsure why code is structured a way, ask.

## Rule 9 — Tests verify intent, not just behavior
Tests must encode WHY behavior matters, not just WHAT it does.
A test that can't fail when business logic changes is wrong.

## Rule 10 — Checkpoint after every significant step
Summarize what was done, what's verified, what's left.
Don't continue from a state you can't describe back.
If you lose track, stop and restate.

## Rule 11 — Match the codebase's conventions, even if you disagree
Conformance > taste inside the codebase.
If you genuinely think a convention is harmful, surface it. Don't fork silently.

## Rule 12 — Fail loud
"Completed" is wrong if anything was skipped silently.
"Tests pass" is wrong if any were skipped.
Default to surfacing uncertainty, not hiding it.

Install note: Save as CLAUDE.md at repo root. Add project-specific rules below the 12 (stack, test commands, error patterns). Don't go past 200 lines combined; past that, compliance falls off.

Mental model: CLAUDE.md is not a wishlist. It's a behavioral contract that closes specific failure modes observed in real work. Every rule should answer: what mistake does this prevent?

2:14 PM · May 9, 2026 · 3.2M views · 61 replies · 566 reposts · 5.4K likes · 20K bookmarks

