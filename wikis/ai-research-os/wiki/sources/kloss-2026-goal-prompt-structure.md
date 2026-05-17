---
title: "klöss /goal Prompt Structure"
date_created: 2026-05-17
date_modified: 2026-05-17
summary: "X thread proposing a structured mission contract for /goal prompts in Codex, Claude Code, and Hermes."
tags: [prompt-structure, codex, claude-code, hermes]
type: source
status: final
---

# klöss /goal Prompt Structure

**Type:** thread  
**Date:** 2026-05-16  
**URL:** https://x.com/kloss_xyz/status/2054096165055217987  
**Raw file:** [[../raw/x-threads/2026-05-16-kloss-xyz-goal-prompt-structure.md]]

## Summary

This X thread argues that `/goal` prompts fail when they rely on generic caution such as “make no mistakes” instead of a clear mission contract. The proposed structure breaks an agent run into one measurable goal, relevant repo/context facts, constraints, optional priorities, a plan-first execution style, verifiable done criteria, explicit verification steps, output expectations, and stop rules. Its most important contribution is the stop-rule section: the agent should halt on high-impact ambiguity or risk, surface ranked uncertainties and proposals, and stop expanding scope once the stated outcome is satisfied.

For Hermes, Codex, Claude Code, and Self-OS, the thread is a compact operational pattern for unattended or semi-autonomous work. It overlaps with existing execution discipline, but makes the contract portable across tools. The useful mapping is straightforward: GOAL becomes desired outcome; CONTEXT becomes files, architecture, assumptions, and prior decisions; CONSTRAINTS become non-negotiables and forbidden actions; DONE WHEN becomes acceptance criteria; VERIFY becomes the validation plan; STOP RULES become escalation policy. The source is especially relevant for Night Shift or cron-style agent runs where the system cannot ask open-ended clarification questions.

## Key contributions

- Converts vague agent instructions into a structured, verifiable mission prompt.
- Elevates constraints, verification, output format, and stop rules to first-class prompt sections.
- Provides a reusable shape for one-off agent work that is too small for full taskOS promotion.

**Related:** [[concepts/goal-prompt-contracts.md]], [[concepts/scope-control-for-agents.md]], [[entities/kloss-xyz.md]]
