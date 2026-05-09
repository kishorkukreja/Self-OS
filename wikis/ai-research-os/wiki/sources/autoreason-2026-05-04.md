---
title: Autoreason — Self-Refinement That Knows When to Stop
date_created: '2026-05-05'
date_modified: '2026-05-05'
summary: 'Autoreason addresses a failure mode in iterative AI workflows: critique-and-revise
  loops can make outputs worse when they force changes even if the incumbent is already
  better. The framework keeps “do nothing” as a tourn'
tags:
- self-refinement
- evaluation
- ai-reasoning
- judge-panels
- autoresearch
- github-repo
type: source
status: final
tags: [wiki, maintenance]
---

# Autoreason — Self-Refinement That Knows When to Stop

**Type:** repo  
**Date:** 2026-05-04  
**URL:** https://github.com/NousResearch/autoreason  
**Raw file:** [[../raw/repos/autoreason-2026-05-04.md]]

## Summary
Autoreason addresses a failure mode in iterative AI workflows: critique-and-revise loops can make outputs worse when they force changes even if the incumbent is already better. The framework keeps “do nothing” as a tournament candidate and compares the unchanged output, an adversarial revision, and a synthesis under fresh blind judges using Borda count. For Self-OS, the source is useful for review and QA loops because it turns restraint into an explicit option. It suggests that agentic improvement systems should include stop conditions, blind judging, and unchanged baselines instead of assuming every refinement pass is positive. This makes it especially relevant for wiki compilation and writing workflows, where unnecessary revisions can erase useful structure or introduce unsupported claims.

## Key contributions
- Makes the unchanged incumbent a first-class candidate in self-refinement.
- Uses separate critique, revision, synthesis, and judge agents to reduce context contamination.
- Provides a pattern for safer review loops in subjective and open-ended domains.

## Linked concepts and entities
- Concepts: [[concepts/self-improving-agents]], [[concepts/agent-evaluation]], [[concepts/judge-panels]]
- Entities: [[entities/autoreason]]

**Tags:** self-refinement, evaluation, ai-reasoning, judge-panels, autoresearch, github-repo
