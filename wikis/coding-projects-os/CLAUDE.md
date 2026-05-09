# coding-projects-os — Schema

## Overview

Engineering memory. Captures Claude Code and Codex session outputs, tracks active projects, and accumulates reusable patterns and architectural decisions. This wiki is strictly isolated — never cross-queried from other wikis.

## Directory Structure

```
raw/
  sessions/
    claude/{session-id}/   — Claude Code session artefacts
      summary.md           ← What was built, context, outcome
      decisions.md         ← Key decisions made, alternatives rejected
      artefacts/           ← Output files: configs, scripts, snippets
    codex/{session-id}/    — Codex session artefacts (same structure)
  projects/{project-name}/ — Project planning documents
    prd.md                 ← Product requirements document
    architecture.md        ← System design and key decisions
    specs/                 ← Detailed specifications per component
  ideas/                   — Lightweight raw idea inbox before taskOS/Kanban promotion
    YYYY-MM-DD-{slug}.md   ← Seed/shaping note for implementation-shaped ideas
    templates/idea.md      ← Idea capture template

wiki/index.md        — Master index linking every page with a one-line summary
wiki/log.md          — Append-only changelog of all operations
wiki/ingest-log.md   — Append-only list of processed session/project folders (do NOT modify raw/)
wiki/projects/       — Active and archived project overviews with status
wiki/patterns/       — Reusable patterns, conventions, approaches discovered across sessions
wiki/decisions/      — Cross-project architectural decision records (ADRs)
wiki/templates/      — Shared components, reference implementations, reusable code artefacts
wiki/outputs/        — Filed answers to queries
```

## Raw File Conventions

**session-id format:** `YYYY-MM-DD-{topic-slug}` (e.g., `2026-04-12-self-os-foundation`)

Required frontmatter on `summary.md` in every session folder:

```yaml
---
date: YYYY-MM-DD
project: {project-name or "standalone"}
agent: claude-code | codex
topics: [tag1, tag2]
outcome: completed | partial | abandoned
---
```

Required frontmatter on `decisions.md`:

```yaml
---
date: YYYY-MM-DD
session: {session-id}
project: {project-name or "standalone"}
---
```

Required frontmatter on raw idea notes in `raw/ideas/`:

```yaml
---
title: "Short Human Title"
date: YYYY-MM-DD
type: idea
status: seed | shaping | ready-for-taskos | promoted-taskos | promoted-kanban | archived | killed
domain: coding-projects-os
source: telegram | daily-brief | weekly-synthesis | conversation | manual
origin_ref: "optional link/path/message reference"
tags: [idea]
taskos_path: null
kanban_tasks: []
---
```

Idea notes are the middle layer between wiki knowledge and execution. Promote them to `/data/taskOS/tasks/<slug>/` only once the outcome, constraints, and acceptance criteria are clear. Create Hermes Kanban tasks only after taskOS capture or when the user explicitly asks for immediate execution.

## Wiki File Conventions

- All filenames: kebab-case, lowercase
- ADRs: `YYYY-MM-DD-{decision-slug}.md` (e.g., `2026-04-12-supabase-over-postgres.md`)
- Project pages: `{project-name}.md`
- Pattern pages: `{pattern-slug}.md` (e.g., `supabase-rls-pattern.md`)
- Every wiki page MUST have YAML frontmatter:

```yaml
---
title: "Page Title"
date_created: YYYY-MM-DD
date_modified: YYYY-MM-DD
summary: "One to two sentences describing this page"
tags: [tag1, tag2]
type: project | pattern | decision | template | output
status: draft | active | complete | archived
# project pages only:
project_status: planning | active | paused | complete
tech_stack: [typescript, supabase, react]
# decision pages only:
chose: "option A"
over: "option B, option C"
revisit_if: "condition that would change this"
---
```

- Use `[[wikilinks]]` for all internal cross-references
- **Bold key terms** on first use in each article

## Operations

### INGEST (when new sessions or project docs are added)

Sessions and projects are ingested as standalone units — one at a time.

1. Read `wiki/ingest-log.md` to identify which session folders have already been processed
2. For each unprocessed session folder: a. Read `summary.md` and `decisions.md` b. Create or update `wiki/projects/{project-name}.md` — append session summary block c. Extract reusable patterns → create or update `wiki/patterns/{pattern}.md` (only genuinely reusable ones) d. Extract architectural decisions → create `wiki/decisions/{date}-{slug}.md` per decision e. Add `[[wikilinks]]` between project, pattern, and decision pages
3. For each unprocessed project folder: a. Read `prd.md` and `architecture.md` b. Create or update `wiki/projects/{project-name}.md` with requirements and architecture summary c. Extract any decisions to `wiki/decisions/`
4. Rebuild `wiki/index.md` to reflect all current wiki files
5. Append processed folder paths to `wiki/ingest-log.md`
6. Append all operations to `wiki/log.md`
7. Do NOT modify any files in `raw/` — it is read-only

### QUERY (when asked about a project, pattern, or decision)

1. Read `wiki/index.md` to understand available content
2. Check `wiki/patterns/` first — most queries are pattern or convention lookups
3. Check `wiki/projects/` for project-specific context
4. Check `wiki/decisions/` for architectural rationale
5. Synthesise an answer with `[[wikilink]]` citations
6. Save the answer as `wiki/outputs/{question-slug}.md`
7. Update `wiki/index.md` and append to `wiki/log.md`

### LINT (periodic health check)

1. Find sessions in `wiki/ingest-log.md` with no corresponding `wiki/projects/` entry — flag
2. Find patterns in `wiki/patterns/` with no inbound links from any project page — flag as orphan
3. Find ADRs in `wiki/decisions/` missing the `revisit_if` field — fix by flagging with ⚠️
4. Identify recurring themes across session summaries not yet extracted to `wiki/patterns/`
5. Flag project pages with `project_status: active` but no session ingest in >30 days
6. Write lint report to `wiki/outputs/lint-report-{date}.md`
7. Append summary to `wiki/log.md`

## Page Creation Threshold

- **Project page:** created on first session or project folder ingest for that project
- **Pattern page:** created only when a pattern appears across 2+ sessions — stub on first mention
- **Decision page:** created for every decision extracted from `decisions.md`, even single-session ones
- Never leave a `[[wikilink]]` pointing to nothing — always create at least a stub

## Quality Standards

- **Session summaries in wiki/projects/:** structured blocks, not prose dumps — what was built, what was decided, what remains
- **Pattern pages:** must include a concrete example from at least one session artefact
- **Decision pages:** must have `chose`, `over`, and `revisit_if` fields — incomplete ADRs are flagged in lint
- Always trace claims to specific session folders or project docs

## Isolation Rules

- This wiki is NEVER cross-queried from `ai-research-os`, `supply-chain-os`, or `personal-os`
- MASTER.md routing: `coding-projects-os` responds only to explicit coding/engineering queries
- The `/wrap-up` Claude Code skill is the primary write path into `raw/sessions/`
- Human writes directly to `raw/projects/` for PRDs and architecture docs

## What NOT to Put Here

- AI research not tied to a specific coding project → `ai-research-os`
- Client work or supply chain deliverables → `supply-chain-os`
- Personal or family matters → `personal-os`