---
source: https://x.com/kloss_xyz/status/2054096165055217987
date: 2026-05-16
type: thread
tags: [goal-prompt, codex, claude-code, hermes, agent-workflows, prompt-structure, task-scoping, verification, self-os]
---

# klöss: /goal prompt structure for Codex, Claude Code, and Hermes

## Summary

klöss argues that `/goal` is one of the most useful commands in Codex, Claude Code, and Hermes, but that most users under-specify it with vague instructions like “make no mistakes.” The post proposes a structured `/goal` template that frames an agent run as a mission: a single measurable outcome, concrete repo/context constraints, priorities, a plan-first execution style, verifiable done criteria, explicit verification steps, concise output expectations, and stop rules for ambiguity and scope creep.

## Key points

- `/goal` should describe one clear mission, not a broad wish or generic “be careful” instruction.
- Context should include repo/files/architecture/current state, assumptions, dependencies, and prior decisions.
- Constraints should make non-negotiables explicit: what must not change, required standards, and forbidden files/actions.
- Done criteria and verification are first-class parts of the prompt, not afterthoughts.
- Stop rules are the most important guardrail: halt on high-impact ambiguity, surface ranked uncertainties/proposals before acting, and stop expanding scope once the goal is satisfied.

## Why it matters

This is directly relevant to Self-OS and Hermes because it operationalizes a recurring failure mode in agent workflows: agents drift, over-edit, or act under ambiguous instructions when the mission contract is underspecified. The template overlaps with Hermes’s existing verification and scope-control discipline, but packages it in a compact form that can be reused for Codex/Claude/Hermes tasks.

## Self-OS implications

- Use this as a lightweight task contract shape for one-off Codex/Hermes runs when full taskOS promotion is overkill.
- For taskOS, map the sections naturally: GOAL → desired outcome, CONTEXT → current state/files, CONSTRAINTS → boundaries, DONE WHEN → acceptance criteria, VERIFY → validation plan, STOP RULES → escalation policy.
- The “rank uncertainties before acting” rule is especially useful for Night Shift / AFK agent runs, where open-ended clarification is not available.
- The template reinforces that agent reliability is often more about mission framing than about adding generic “do not make mistakes” language.

## Image

Image URL: https://pbs.twimg.com/media/HIGdkyEbUAAIqeh?format=jpg&name=small

The image is a visual card summarizing the `/goal` structure with sections for GOAL, CONTEXT, CONSTRAINTS, PRIORITY, PLAN, DONE WHEN, VERIFY, OUTPUT, and STOP RULES, with the central text “/goal — and how to structure yours.”

## Raw post text

Author: klöss / @kloss_xyz  
Posted: 7:07 AM · May 12, 2026  
Visible metrics at capture: 32 replies, 99 reposts, 890 likes, 1.5K bookmarks, 236.1K views

> /goal is the best command in Codex, Claude Code, and Hermes right now.
>
> And most are using it wrong.
>
> They write "make no mistakes".
>
> And pray.
>
> Here's how to structure yours for a mission, to rank your uncertainties before acting, to kill scope creep, and to close every loop other prompts leave open.
>
> /goal prompt [structure below]
>
> GOAL:
> <single clear measurable outcome; one mission only>
>
> CONTEXT:
> <repo/files/architecture/current state>
> <known assumptions, dependencies, and relevant prior decisions>
>
> CONSTRAINTS:
> <what must not change>
> <required standards/patterns>
> <forbidden files/actions if any>
>
> PRIORITY: (optional)
> 1. <highest priority>
> 2. <secondary priority>
> 3. <tertiary priority>
>
> PLAN:
> <understand first, then act>
> <restate understanding before executing non-trivial changes>
> <prefer minimal sufficient changes over broad rewrites>
>
> DONE WHEN:
> <verifiable completion state>
> <expected behavior preserved or improved>
>
> VERIFY:
> <tests/build/lint/typecheck/manual validation>
> <state what could not be verified and why>
> <include rollback/containment plan for destructive or high-risk changes>
>
> OUTPUT:
> <concise summary/docs/audit/results>
> <changed files, key decisions, risks, and follow-ups>
>
> STOP RULES:
> <halt on high-impact ambiguity or risk; do not invent architecture, behavior, or requirements>
> <surface uncertainties together with ranked highest-confidence proposals before acting; not open-ended clarification questions>
> <do not continue expanding scope after the goal is satisfied>

## Extraction notes

Captured via browser extraction from the public X page because X posts are not reliably handled by normal webpage extraction. The visible post text and attached image were accessible without login; replies were not expanded or captured.
