---
title: "open-slide"
date_created: 2026-05-06
date_modified: 2026-05-06
summary: "1weiho/open slide is an MIT licensed TypeScript/React slide framework built for coding agents. The core idea is that slides are visual code: the user describes a deck in natural language, and a coding agent writes arbitrary React components"
tags: [slides, presentations, agent-native-authoring, react, coding-agents, open-slide]
type: source
status: final
---

# open-slide

**Type:** repo
**Date:** 2026-05-05
**URL/Source:** https://github.com/1weiho/open-slide
**Raw file:** [[../raw/repos/open-slide-2026-05-05.md]]
**Concepts:** [[concepts/slides]], [[concepts/presentations]], [[concepts/agent-native-authoring]]
**Entities:** [[entities/github]], [[entities/claude-code]]

## Summary

1weiho/open slide is an MIT licensed TypeScript/React slide framework built for coding agents. The core idea is that slides are visual code: the user describes a deck in natural language, and a coding agent writes arbitrary React components for a fixed 1920 × 1080 slide canvas. It includes runtime support for canvas rendering, scaling, navigation, hot reload, present mode, static export, and agent driven editing workflows. User instruction captured with this source: use/consider open slide when the user asks Hermes to create slides or decks. This is directly relevant to Hermes/Self OS slide generation because it turns deck creation into an agent editable code workflow rather than a one shot PowerPoint export. The browser comment and /apply comments loop is especially aligned with the user's preference for iterative QA, strategy mapping, and thorough outline/design review before finalizing artifacts. Agent native authoring: designed for Claude Code, Codex, Cursor, and other coding agents to generate decks as React code. Natural language deck creation: scaffolded projects include /create slide, which asks about topic/aesthetic, page count, text density, and motion vs static, then plans and writes pages. Agent technical reference: scaffolded projects include /slide authoring, which documents the fixed canvas, type scale, palette, and layout rules agents should read before writing slides. Fixed canvas model: every slide renders into a 1920 × 1080 canvas; slides are arbitrary React components rather than a constrained presentation DSL. Browser comment workflow: the in browser inspector lets a user click elements and leave comments such as “make this red,” “change this text,” or “shrink the headline.” These persist as @slide comment markers in source. Apply comments loop: user comments can be applied by an agent via /apply comments, then cleared, enabling a review loop: present → click to comment → /apply comments → repeat. Assets and logos: includes an asset manager for images, videos, fonts, and SVGL logo search. Presentation mode: includes fullscreen playback, keyboard navigation, presenter mode, current/next previews, speaker notes, and timer. Export: can export decks to self contained static HTML or print ready PDF. Deployable output: produces static builds suitable for Vercel, Cloudflare Pages, Zeabur, Netlify, or any static host.

## Key takeaways

- Description: A slide framework built for agents.
- Last pushed at capture: 2026 05 05
- Agent native authoring: designed for Claude Code, Codex, Cursor, and other coding agents to generate decks as React code.
- Natural language deck creation: scaffolded projects include /create slide, which asks about topic/aesthetic, page count, text density, and motion vs static, then plans and writes pages.

## Compilation notes

Compiled from `raw/repos/open-slide-2026-05-05.md` during the 2026-05-06 wiki compile. The raw capture remains the canonical source for exact excerpts, links, and figures.
