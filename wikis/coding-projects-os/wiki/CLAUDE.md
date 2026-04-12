# Coding Projects OS — Wiki Content Schema

## File Naming
- All filenames: kebab-case lowercase
- Project-prefixed where relevant: `self-os-architecture.md`
- Session files use session-id as the folder name

---

## index.md Schema

Updated by ingest agent after every run. Do not edit manually.

```markdown
# Coding Projects OS — Index
_Last updated: YYYY-MM-DD_

## Projects (N)
- [project-name](projects/project-name.md) — status, last session

## Patterns (N)
- [pattern-name](patterns/pattern-name.md) — category, source sessions

## Decisions (N)
- [decision-title](decisions/decision-slug.md) — project, date

## Outputs (N)
- [output-title](outputs/output-slug.md) — type, project
```

## log.md Schema

Append-only. One entry per ingest run.

```markdown
## YYYY-MM-DD HH:MM
- Session ingested: {session-id} ({claude | codex})
- Project: {project-name}
- Patterns extracted: N (list)
- Decisions extracted: N (list)
- Updated: projects/{project-name}.md
```

---

## projects/ File Schema

One file per project. Updated after every session.

```markdown
# {Project Name}
_Status: active | on-hold | complete | archived_
_Last session: YYYY-MM-DD_

## What it is
{One paragraph description}

## Architecture
{Key design decisions and system structure}

## Sessions
| Session ID | Date | What happened |
|------------|------|----------------|
| {id} | YYYY-MM-DD | brief summary |

## Open questions
- question 1
- question 2

## Links
- PRD: [[../raw/projects/{project-name}/prd.md]]
- Architecture: [[../raw/projects/{project-name}/architecture.md]]
```

## patterns/ File Schema

Reusable patterns discovered across sessions.

```markdown
# {Pattern Name}

**Category:** architecture | testing | tooling | workflow | data | api

**Description:** One sentence summary.

## The Pattern
{Clear description of what the pattern is}

## When to use
{Context / trigger conditions}

## Implementation
{Code example or step-by-step}

## Discovered in
- [[../raw/sessions/claude/{session-id}/summary.md]]

_Last updated: YYYY-MM-DD_
```

## decisions/ File Schema

Cross-project architectural decisions. Permanent record.

```markdown
# {Decision Title}
_Date: YYYY-MM-DD | Project: {project-name} | Status: active | superseded_

## Decision
{What was decided — one sentence}

## Context
{Problem being solved, constraints that shaped the decision}

## Options considered
1. Option A — pros/cons
2. Option B — pros/cons

## Rationale
{Why this option was chosen}

## Superseded by
{Link if this decision was later revised}
```

## outputs/ File Schema

Shared components, templates, reference implementations.

```markdown
# {Output Title}

**Type:** component | template | reference-impl | config | script
**Project:** {project-name or cross-project}
**Status:** draft | stable | deprecated

## Purpose
{What this output is for}

## Usage
{How to use it}
```
