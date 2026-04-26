# personal-os — Schema

## Overview

Personal and family life management. Covers Deepchand family businesses (bakers, weddings), personal finances, family finances, and health. All content in this wiki is private. Never surface personal-os content in outputs from any other wiki.

## Directory Structure

```
raw/
  deepchand-bakers/    — Bakery receipts, invoices, P&L docs, supplier info
  deepchand-weddings/  — Wedding bookings, contracts, vendor records, timelines
  self-finance/        — Personal investments, expenses, savings goals, income
  family-finance/      — Shared family accounts, loans, property, joint expenses
  health/              — Health records, appointments, goals, lab results

wiki/index.md        — Master index linking every page with a one-line summary
wiki/log.md          — Append-only changelog of all operations
wiki/ingest-log.md   — Append-only list of processed raw filenames (do NOT modify raw/)
wiki/summaries/      — Periodic summaries: monthly/quarterly/annual by domain
wiki/decisions/      — Key decisions made with context, options considered, outcome
wiki/actions/        — Action items: open, in-progress, closed
```

## Raw File Conventions

|Folder|Filename Convention|
|---|---|
|`deepchand-bakers/`|`YYYY-MM-DD-{doc-type}.md`|
|`deepchand-weddings/`|`YYYY-MM-DD-{event-or-type}.md`|
|`self-finance/`|`YYYY-MM-DD-{category}.md`|
|`family-finance/`|`YYYY-MM-DD-{category}.md`|
|`health/`|`YYYY-MM-DD-{type}.md`|

Required frontmatter on every raw file:

```yaml
---
date: YYYY-MM-DD
type: financial | operational | health | contract | record
domain: deepchand-bakers | deepchand-weddings | self-finance | family-finance | health
tags: [tag1, tag2]
---
```

## Wiki File Conventions

- All filenames: kebab-case, lowercase
- Summaries: `{domain}-{YYYY}-{period}.md` (e.g., `deepchand-bakers-2026-q1.md`)
- Decisions: `YYYY-MM-DD-{decision-slug}.md`
- Actions: `{domain}-actions-{YYYY-MM-DD}.md`
- Every wiki page MUST have YAML frontmatter:

```yaml
---
title: "Page Title"
date_created: YYYY-MM-DD
date_modified: YYYY-MM-DD
summary: "One to two sentences describing this page"
tags: [tag1, tag2]
type: summary | decision | action
domain: deepchand-bakers | deepchand-weddings | self-finance | family-finance | health
status: draft | active | resolved | archived
# action pages only:
priority: high | medium | low
due: YYYY-MM-DD
---
```

- Use `[[wikilinks]]` for all internal cross-references

## Sensitive Data Rules

These rules are non-negotiable and apply to every operation:

1. **Never reproduce raw financial figures verbatim** — wiki summaries contain totals, trends, and directional language only ("income up 12% vs prior quarter", not the actual numbers)
2. **Never write account identifiers** — reference accounts by label only ("Barclays current account", never the account number, sort code, or card detail)
3. **Never reproduce contract terms verbatim** — summarise key obligations and dates only
4. **Health data** — summaries capture status and goals, not raw test values or medication dosages
5. Raw files in `raw/` are the single source for sensitive data — wiki pages must always be safe to read without exposing the underlying figures

## Operations

### INGEST (when new raw files are added)

1. Read `wiki/ingest-log.md` to identify which raw files have already been processed
2. Identify the domain from the file path (`deepchand-bakers`, `deepchand-weddings`, etc.)
3. For each unprocessed file: a. Read the source — apply sensitive data rules strictly b. Create or update `wiki/summaries/{domain}-{period}.md` — append a summary block with totals and trends only c. Extract any explicit decisions → create `wiki/decisions/{date}-{slug}.md` d. Extract any action items → append to `wiki/actions/{domain}-actions-{date}.md` e. Add `[[wikilinks]]` between related summaries, decisions, and actions
4. Never synthesise across domains without explicit instruction (bakery financials must not merge with personal finance)
5. Rebuild `wiki/index.md` to reflect all current wiki files
6. Append processed filenames to `wiki/ingest-log.md`
7. Append all operations to `wiki/log.md`
8. Do NOT modify any files in `raw/` — it is read-only

### QUERY (when asked about a domain or topic)

1. Read `wiki/index.md` to understand available content
2. Identify the domain from the query
3. Read relevant summaries, decisions, and actions for that domain only
4. Synthesise an answer — apply sensitive data rules to the output
5. Do not cross domain boundaries in a single answer unless explicitly asked
6. Save complex answers to `wiki/outputs/{slug}.md` if warranted
7. Update `wiki/index.md` and append to `wiki/log.md`

### LINT (periodic health check)

1. Find action items in `wiki/actions/` with `status: open` past their `due` date — flag with ⚠️
2. Find decisions in `wiki/decisions/` with no follow-up summary or outcome recorded
3. Find summaries >3 months old in active domains with no update — flag for review
4. Find raw files in `wiki/ingest-log.md` that have not been ingested — list them
5. Write lint report to `wiki/actions/lint-report-{date}.md`
6. Append summary to `wiki/log.md`

## Domain Notes

**Deepchand Bakers / Deepchand Weddings** Treat as small business operations. Summaries capture: operational status, key contacts, open issues, and high-level financial position. Separate summaries per business — never merge.

**Self Finance / Family Finance** Separate at all times — self-finance is personal, family-finance is shared. Summaries capture: active goals, key decisions pending, directional financial position. No raw figures in wiki pages.

**Health** Summaries capture: active protocols, recent changes, open actions. Always append: _"This is a personal health log, not medical advice."_ Never reproduce lab values or medication dosages in wiki pages.

## Isolation Rules

- personal-os is NEVER cross-queried from `supply-chain-os`, `ai-research-os`, or `coding-projects-os`
- personal-os appears in multi-wiki queries only when explicitly requested by user
- MASTER.md routing excludes personal-os from all default fan-out patterns

## What NOT to Put Here

- AI research or tools → `ai-research-os`
- Client or professional work → `supply-chain-os`
- Code sessions or engineering projects → `coding-projects-os`