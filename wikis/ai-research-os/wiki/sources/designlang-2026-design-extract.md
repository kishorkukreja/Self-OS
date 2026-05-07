---
title: "Designlang / design-extract"
date_created: 2026-05-07
date_modified: 2026-05-07
summary: "Repository summary for Designlang, a tool that extracts live website design systems into tokens, Tailwind/shadcn themes, Figma variables, prompt packs, and MCP payloads."
tags: [design-systems, design-tokens, frontend-tooling, agent-tools]
type: source
status: final
---

# Designlang / design-extract

**Type:** repo
**Date:** 2026-05-06
**URL/Source:** https://github.com/Manavarya09/design-extract
**Raw file:** [[../raw/repos/design-extract-2026-05-06.md]]
**Concepts:** [[concepts/design-system-extraction]], [[concepts/agent-native-ui-generation]]
**Entities:** [[entities/designlang]], [[entities/figma]], [[entities/tailwind]], [[entities/shadcn]]

## Summary

Designlang, also published through the `design-extract` repository, treats a rendered website as an inspectable design-system source of truth. Instead of asking an agent to infer brand language from screenshots or vague prompts, it uses a headless browser to inspect the live DOM and emit structured artifacts: DTCG tokens, CSS variables, Tailwind configuration, shadcn/ui theme variables, Figma variables, component anatomy, motion tokens, page-intent labels, design report cards, and prompt packs for tools such as v0, Lovable, Cursor, and Claude Artifacts. That makes it a bridge between visual inspiration, implementation-ready tokens, and agent-consumable design specifications.

The repo is notable for Self-OS because it supports an agent-native UI workflow. A reference site can be captured, graded for accessibility and consistency, converted into platform-specific emitters, and fed into downstream generation tools without hand-copying palettes and spacing scales. The raw capture also notes responsive analysis, hover/focus/active states, multi-page consistency checks, drift detection, visual diffs, and an MCP/skill workflow for Claude Code, Cursor, Windsurf, and similar coding agents. The durable concept is design-system extraction: using rendered software itself as the data source for style, interaction, and component constraints. That complements existing design-md, Refero, Tailwind, and shadcn knowledge in the wiki.

## Key takeaways

- Live DOM extraction can produce more implementation-ready design artifacts than screenshots or manual brand notes.
- Agent UI generation improves when prompts are backed by structured tokens, component anatomy, and theme files.
- Designlang fits Self-OS design workflows as a capture-and-translate step before UI generation or design review.

## Compilation notes

Compiled from `raw/repos/design-extract-2026-05-06.md` during the 2026-05-07 wiki compile. The raw capture remains the canonical source for exact excerpts, links, figures, and code.
