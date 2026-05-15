---
source: https://x.com/ChrisHayduk/status/2053807198870880743
date: 2026-05-11
type: thread
tags: [codex, goal-mode, coding-agents, agent-loops, autonomous-agents, qa, self-os]
---

# Chris Hayduk — Using Codex `/goal` Mode Effectively

## Summary

Chris Hayduk explains that Codex now supports a `/goal` command in the Codex app. Starting a prompt with `/goal` triggers Codex to loop continuously until it achieves the specified objective, which makes the quality of the goal specification much more important than in ordinary interactive prompting. His core playbook is: define a clear measurable goal, keep the feedback loop tight, and give Codex markdown files/checklists to think and track progress in. This is directly relevant to Self-OS/Hermes because it matches the existing philosophy of long-running agent loops needing explicit done criteria, validation commands, and persistent state artifacts rather than vague prompts.

## Post metadata

- **Author:** Chris Hayduk
- **Handle:** `@ChrisHayduk`
- **Posted:** 2026-05-11 11:59:28 GMT
- **Engagement surfaced by extractor:** 1,166 likes · 104 retweets
- **Post URL:** https://x.com/ChrisHayduk/status/2053807198870880743

## Key points

- **Codex `/goal` is a loop:** Goal mode executes actions, scores/checks progress, compares the score to the goal, and continues until the goal is achieved or termination conditions are met.
- **Vague goals fail:** Requests like “make my code better” leave the stopping condition undefined.
- **Two failure modes:** With underspecified goals, the agent may either stop too early or never stop while making unfocused changes.
- **Make goals quantitative:** Example: “reduce runtime of code in `specific_file` by 20% without regressions in unit and integration tests.”
- **Convert qualitative goals into checklists:** For an ICML-formatting task, Chris had Codex extract more than 200 rules into a markdown checklist, then asked it to satisfy the checklist without changing technical content.
- **Use markdown files for state:** Markdown checklists let the model persist progress and let the user visually inspect what remains.
- **Tight feedback loops matter:** The agent needs fast, reliable validation signals that tell it whether it is closer to completion.
- **Long-running usefulness depends on eval design:** The post’s claim is not just “Codex can run for hours”; it is that it can grind productively when the loop has measurable targets and persistent working memory.

## Why it matters

This is an operational playbook for making autonomous coding loops less flaky. It turns “goal mode” from a magic command into a control-system problem: define objective, define scoring, define state, define stop conditions. That maps well to serious AFK/night-shift agent work, where vague instructions create expensive drift.

## Self-OS / Hermes implications

- **Use `/goal` only for bounded, verifiable work:** Good candidates include runtime reduction, test coverage increase, migration checklists, lint/schema compliance, and bug reproduction/fix loops.
- **Every long-running goal should have a mission file:** Store objective, constraints, non-goals, validation commands, and done criteria in `mission.md` or equivalent.
- **Checklists are the bridge from qualitative to quantitative:** For vague requests like “make docs better” or “make this PR production-ready,” first ask an agent to extract requirements into a checklist, then run against the checklist.
- **Progress should live in files, not chat memory:** Long-running loops should update markdown state/checklists so humans and follow-up agents can inspect progress.
- **Goal-buddy/reviewer pass remains necessary:** Even with `/goal`, a separate reviewer should check for early stopping, metric gaming, and proxy completion.
- **Night Shift relevance:** This is a strong pattern for the user’s Day/Night workflow: Day shift defines measurable goals and checklists; Night shift agents grind; Morning review inspects artifacts and validation.

## Candidate prompt pattern

```text
/goal Reduce the runtime of <specific target> by at least 20% while preserving public behavior.

Use these files as your operating state:
- mission.md: objective, scope, constraints, non-goals, and done criteria
- checklist.md: concrete requirements and validation steps
- progress.md: completed work, failed attempts, and next hypothesis

Verification commands:
- <unit test command>
- <integration test command>
- <benchmark command>

Stop only when:
- benchmark shows >=20% runtime reduction versus baseline
- all listed tests pass
- checklist.md is fully checked off
- progress.md explains the final approach and remaining risks
```

## Extraction notes

- Browser extraction could not be used in this environment because Chrome was unavailable for the browser tool.
- `xurl` was unavailable or unauthenticated, so the X API path could not be used.
- `web_extract` successfully returned a structured summary of the X post, including author, date, engagement, and the main guidance.
- Web search verified the distinctive phrase “Perceptive Codex users have noticed that the /goal command is now available...” appears in indexed X snippets for `@ChrisHayduk`.

## Raw extracted content summary

```text
Perceptive Codex users have noticed that the /goal command is now available in the Codex app — start your prompt with /goal and specify what you want your agent to do. This triggers Codex to loop continuously until it achieves your goal.

The prompting style needs to change for goal mode. Set up a clear, measurable goal, keep the feedback loop tight, and give the agent markdown files to think in. With those three pieces in place, Codex can work for hours or days on hard problems.

Vague qualitative goals such as “make my code better” fail because the loop end state is underspecified. The model may stop too early or never stop while making unfocused changes.

A better goal is quantitative and constrained, for example: reduce runtime of code in a specific file by 20% without causing regressions in existing unit tests and integration tests.

For qualitative tasks, convert requirements into a checklist. In an example converting a NeurIPS preprint to ICML workshop format, Codex extracted more than 200 formatting and stylistic rules into a markdown checklist. The goal then became: change the paper to ICML format based on checklist.md without changing technical content. The agent can reason about checking off all items better than it can reason about a vague top-level objective.
```
