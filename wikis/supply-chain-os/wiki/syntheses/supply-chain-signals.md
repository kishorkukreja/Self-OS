---
title: "Supply Chain Signals"
date_created: 2026-05-02
date_modified: 2026-05-02
summary: "Auto-generated summary."
tags: [stub, auto-fix]
type: synthesis
status: draft
---

# Supply Chain Signals

**Status:** active
**Date:** 2026-04-29
**Sources consulted:** [[../raw/newsletters/supply-chain-signals/2026-W18/README]]

## Question

What is the weekly Supply Chain Signals publishing pipeline, and where should the latest issue material be found?

## Findings

Supply Chain Signals is the weekly supply chain newsletter pipeline for tracking the bottlenecks, breakthroughs, and hidden systems shaping global supply chains.

The source of truth for each issue is the weekly raw folder:

- Current week: [[../raw/newsletters/supply-chain-signals/2026-W18/README]]
- Root folder: `wikis/supply-chain-os/raw/newsletters/supply-chain-signals/`

Each weekly folder contains:

- `daily/` — daily research captures
- `sources/` — source lists and extraction notes
- `brief/` — Sunday publishing drafts for Substack, LinkedIn, X/thread, carousel outline, and PPT/consulting-style outline

The automation runs at 1 PM UK time. During the week it collects research. On Sundays it creates the publishable weekly package.

## Current editorial defaults

- First Chain of the Week: Wafer to Rack
- Source mix: executive sources, operator sources, research sources, and tech/systems sources
- Voice: clear, specific, humanized, operator-useful, not AI-sounding
- Output formats: Substack draft, LinkedIn posts, X/thread, carousel outline, PPT/consulting-style outline

## Automation

- BST months cron: `eaf6208b3a6b`, 12:00 UTC, equivalent to 1 PM UK time
- GMT months cron: `f42ba370f3a2`, 13:00 UTC, equivalent to 1 PM UK time
- Daily wiki compile cron: `f1e3ba7d9109`, midnight UTC, processes raw files into structured wiki pages

## Evidence

- [[../raw/newsletters/supply-chain-signals/2026-W18/README]]: current weekly research folder

## Confidence

high — cron jobs and current weekly folder have been verified.

## Gaps

This page should be updated as new weekly issue folders are generated.

_Last updated: 2026-04-29_
