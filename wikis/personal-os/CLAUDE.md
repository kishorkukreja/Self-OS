# Personal OS

**Domain:** Personal & Family
**Purpose:** Manage Deepchand family businesses, personal finances, family finances, and health.

---

## Raw Folder Sources

| Folder | Content Type | Filename Convention |
|--------|-------------|---------------------|
| `raw/deepchand-bakers/` | Bakery receipts, invoices, P&L docs, supplier info | `YYYY-MM-DD-{doc-type}.md` |
| `raw/deepchand-weddings/` | Wedding bookings, contracts, vendor records, timelines | `YYYY-MM-DD-{event-or-type}.md` |
| `raw/self-finance/` | Personal investments, expenses, savings goals, income | `YYYY-MM-DD-{category}.md` |
| `raw/family-finance/` | Shared family accounts, loans, property, joint expenses | `YYYY-MM-DD-{category}.md` |
| `raw/health/` | Health records, appointments, goals, lab results | `YYYY-MM-DD-{type}.md` |

## Required Frontmatter

Every raw file must include:

```yaml
---
date: YYYY-MM-DD
type: financial | operational | health | contract | record
domain: deepchand-bakers | deepchand-weddings | self-finance | family-finance | health
tags: [tag1, tag2]
status: raw | processed
---
```

## Ingest Rules

1. Files land in the correct subfolder — never directly in `raw/`
2. All content in this wiki is private — never cross-reference into supply-chain-os outputs
3. Ingest produces summaries, highlights decisions, and surfaces action items
4. Financial data is summarised (totals, trends) — raw figures stay in raw/ files
5. After processing, mark raw file frontmatter `status: processed`

## Wiki Output Structure

| Folder | Purpose |
|--------|---------|
| `wiki/summaries/` | Periodic summaries: monthly/quarterly/annual by domain |
| `wiki/decisions/` | Key decisions made with context, options considered, outcome |
| `wiki/actions/` | Action items: open, in-progress, closed |

## What NOT to Put Here

- AI research or tools → `ai-research-os`
- Client or professional work → `supply-chain-os`
- Code sessions or engineering projects → `coding-projects-os`
