---
title: "pbakaus/impeccable"
date_created: 2026-05-01
date_modified: 2026-05-01
summary: "[[entities/impeccable]] is a frontend-design skill and command suite for making AI coding agents less generic at UI work."
tags: [impeccable, frontend-design, ai-skills, design-systems, cursor, mcp, ui-ux]
type: source
status: final
---

# pbakaus/impeccable

**Type:** repo  
**Date:** 2026-04-30  
**URL:** https://github.com/pbakaus/impeccable  
**Raw file:** [[../raw/repos/impeccable-2026-04-30.md]]

## Summary

[[entities/impeccable]] is a frontend-design skill and command suite for making AI coding agents less generic at UI work. It extends Anthropic's frontend-design skill with a richer design vocabulary, curated anti-patterns, domain references, and 23 `/impeccable` commands covering shaping, crafting, critique, auditing, polish, typography, layout, color, motion, responsive behavior, UX writing, and edge-case hardening. The repo is explicitly aimed at common AI UI failure modes such as default typography, purple gradients, nested cards, weak contrast, and shallow product context.

The source also captures a related runtime-feedback pattern: using Chrome DevTools MCP so agents can inspect a live browser, console, network activity, source-mapped stack traces, and request failures directly. That pairing is important for [[concepts/frontend-agent-workflows]]: Impeccable supplies taste, vocabulary, and design-system discipline, while DevTools MCP supplies evidence from the running interface. The result is a more complete agent harness for frontend work: context gathering, product/design documentation, visual iteration, accessibility and performance review, and browser-grounded debugging.

## Key contributions
- Impeccable packages design taste and frontend quality standards as reusable AI-agent commands and reference material.
- Its domain references cover typography, color, spatial design, motion, interaction, responsive behavior, and UX writing.
- The captured Chrome DevTools MCP pattern complements Impeccable by giving the agent live browser evidence instead of relying on screenshots or pasted errors.

## Concepts and entities

**Concepts:** [[concepts/frontend-agent-workflows]], [[concepts/design-engineering-skills]], [[concepts/ai-coding-skills]], [[concepts/browser-grounded-debugging]]  
**Entities:** [[entities/impeccable]], [[entities/paul-bakaus]], [[entities/chrome-devtools-mcp]]

**Tags:** impeccable, frontend-design, ai-skills, design-systems, cursor, mcp, ui-ux
