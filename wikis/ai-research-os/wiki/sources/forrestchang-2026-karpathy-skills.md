---
title: "Karpathy-Inspired Claude Code Guidelines"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "CLAUDE.md plugin derived from Andrej Karpathy's observations on LLM coding pitfalls, enforcing four principles: Think Before Coding, Simplicity First, Surgical Changes, and Goal-Driven Execution."
tags: [claude-code, claude-md, coding-guidelines, karpathy, llm-pitfalls, simplicity]
type: source
status: final
---

# Karpathy-Inspired Claude Code Guidelines

**Type:** repo
**Date:** 2026-04-13
**URL:** https://github.com/forrestchang/andrej-karpathy-skills
**Raw file:** [[../../raw/repos/karpathy-skills-2026-04-13.md]]

**Summary:** This repository distils Andrej Karpathy's observations on common LLM coding failures into a single CLAUDE.md file designed to improve Claude Code behaviour. It addresses four core problems: models making wrong assumptions silently, overcomplicating code and APIs, touching orthogonal code as side effects, and failing to verify success. The solution is organised into four principles—Think Before Coding, Simplicity First, Surgical Changes, and Goal-Driven Execution—each with concrete rules and verification tests. Installable either as a Claude Code plugin or appended to a project's CLAUDE.md.

**Key contributions:**
- Explicit assumption-surfacing and tradeoff-presentation rules
- Simplicity guardrails: no speculative features, no premature abstraction
- Surgical change discipline: touch only what is requested, clean up only your own orphans
- Goal-driven execution: transform imperative instructions into declarative goals with verifiable success criteria

**Tags:** claude-code, claude-md, coding-guidelines, karpathy, llm-pitfalls, simplicity
