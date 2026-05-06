---
title: "Self-OS Operating Brief"
date_created: 2026-05-03
date_modified: 2026-05-03
summary: "A workflow pattern for producing daily Self-OS status briefs from repo, cron, raw, and wiki signals."
tags: [self-os, operating-brief, workflow]
type: pattern
status: draft
---

# Self-OS Operating Brief

**Category:** workflow

**Description:** A scheduled or manual workflow that turns repository and wiki state into a concise operating brief.

## The Pattern

Collect recent commits, raw captures, cron failures, and open wiki maintenance signals into a daily briefing document. Keep raw evidence in the project folder and compile only the reusable operating-loop lessons into the wiki.

## When to use

Use this when Self-OS needs a daily control-plane view: what changed, what needs attention, and which automation should run next.

## Implementation

Generate a raw brief with `scripts/generate_self_os_brief.py`, inspect it for usefulness, then promote stable sections into a Hermes skill or scheduled workflow.

## Discovered in
- [[../raw/projects/self-os-operating-loop/ops/daily/2026-05-02-manual.md]]

_Last updated: 2026-05-03_
- [[../raw/projects/self-os-operating-loop/ops/daily/2026-05-05-morning.md]]
