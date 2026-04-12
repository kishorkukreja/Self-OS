# Personal OS — Wiki Content Schema

## File Naming
- All filenames: kebab-case lowercase
- Domain-prefixed: `bakers-2026-q1-summary.md`, `self-finance-jan-2026.md`
- No spaces, no special characters

---

## index.md Schema

Updated by ingest agent after every run. Do not edit manually.

```markdown
# Personal OS — Index
_Last updated: YYYY-MM-DD_

## Summaries (N)
- [summary-title](summaries/summary-slug.md) — domain, period

## Decisions (N)
- [decision-title](decisions/decision-slug.md) — domain, date, status

## Actions (N)
- [action-title](actions/action-slug.md) — domain, status, due-date
```

## log.md Schema

Append-only. One entry per ingest run.

```markdown
## YYYY-MM-DD HH:MM
- Ingested: N files from {domains}
- Added: file1.md, file2.md
- Updated: file3.md
- Open actions surfaced: N
```

---

## summaries/ File Schema

Periodic summaries per domain. One file per period per domain.

```markdown
# {Domain} — {Period} Summary
_Period: YYYY-MM to YYYY-MM | Generated: YYYY-MM-DD_

## Highlights
- key point 1
- key point 2

## Financials (if applicable)
| Category | Amount | vs Prior Period |
|----------|--------|----------------|
| Revenue | | |
| Expenses | | |
| Net | | |

## Key events
- brief description of notable events

## Carry-forward
- items or issues rolling into next period
```

## decisions/ File Schema

One decision per file. Permanent record — never deleted.

```markdown
# {Decision Title}
_Date: YYYY-MM-DD | Domain: deepchand-bakers | deepchand-weddings | self-finance | family-finance | health_

## Decision
{What was decided — one sentence}

## Context
{Why this decision needed to be made}

## Options considered
1. Option A — pros/cons
2. Option B — pros/cons

## Outcome
{Which option was chosen and why}

## Review date
{When to revisit this decision, if applicable}
```

## actions/ File Schema

One action item per file. Updated as status changes.

```markdown
# {Action Title}
_Domain: {domain} | Status: open | in-progress | done | cancelled_

**Due:** YYYY-MM-DD
**Owner:** Kish

## What needs to happen
{Clear description of the action}

## Why it matters
{Context}

## Progress
- YYYY-MM-DD: {update}
```
