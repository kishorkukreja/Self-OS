---
title: "ClawSweeper"
date_created: 2026-04-29
date_modified: 2026-04-29
summary: "ClawSweeper captures a repo relevant to AI engineering workflows, agent infrastructure, and knowledge-management practices. The source is useful because it records concrete capabilities, setup details, and design trade-o"
tags: [ai-tools]
type: source
status: final
---

# ClawSweeper

**Type:** repo  
**Date:** 2026-04-27  
**URL:** The Unwind AI newsletter  
**Raw file:** [[../../raw/repos/clawsweeper-2026-04-27.md]]

**Summary:** ClawSweeper captures a repo relevant to AI engineering workflows, agent infrastructure, and knowledge-management practices. The source is useful because it records concrete capabilities, setup details, and design trade-offs that can be compared against the rest of the AI Research OS corpus. OpenClaw maintenance bot for openclaw/openclaw. "ClawSweeper scans all issues and PRs and suggest what we can close, and why. It runs every PR / Issue once a week." - Maintains one markdown report per open issue/PR - Publishes one durable Codex automated review comment when useful - Only closes items when the evidence is strong ClawSweeper may propose closing only when an item is clearly one of: - Implemented on current main - Not reproducible on current main - Better suited for ClawHub skill/plugin work than core - Duplicate or superseded by a canonical issue/PR - Concrete but not actionable in this source repo - Incoherent enough that no action can be taken - Stale issue older than 60 days with too little data to verify - Issues with an open PR referencing them using closing syntax (Fixes 123) until that PR merges or closes

**Key contributions:**
- OpenClaw maintenance bot for openclaw/openclaw.
- "ClawSweeper scans all issues and PRs and suggest what we can close, and why. It runs every PR / Issue once a week."
- - Maintains one markdown report per open issue/PR
- - Publishes one durable Codex automated review comment when useful
- - Only closes items when the evidence is strong

**Related concepts:** [[concepts/ai-tools]]  
**Primary entity:** [[entities/clawsweeper]]

**Tags:** ai-tools
