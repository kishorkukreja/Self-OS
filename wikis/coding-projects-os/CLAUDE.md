# Coding Projects OS

**Domain:** Engineering & Development
**Purpose:** Capture coding sessions, track active projects, and accumulate reusable patterns and architectural decisions.

---

## Raw Folder Sources

| Folder | Content Type | Naming Convention |
|--------|-------------|-------------------|
| `raw/sessions/claude/{session-id}/` | Claude Code session artefacts | `summary.md`, `decisions.md`, `artefacts/` |
| `raw/sessions/codex/{session-id}/` | Codex session artefacts | `summary.md`, `decisions.md`, `artefacts/` |
| `raw/projects/{project-name}/` | Project planning documents | `prd.md`, `architecture.md`, `specs/` |

## Session Folder Schema

Each session folder must contain:

```
{session-id}/
├── summary.md       ← What was built, context, outcome
├── decisions.md     ← Key decisions made, alternatives rejected
└── artefacts/       ← Any output files: configs, scripts, snippets
```

**session-id format:** `YYYY-MM-DD-{topic-slug}` (e.g., `2026-04-12-self-os-foundation`)

## Project Folder Schema

Each project folder must contain:

```
{project-name}/
├── prd.md           ← Product requirements document
├── architecture.md  ← System design and key decisions
└── specs/           ← Detailed specifications per component
```

## Ingest Rules

1. Sessions and projects are standalone units — ingest one at a time
2. Ingest extracts patterns and decisions from sessions → populates wiki/patterns/ and wiki/decisions/
3. coding-projects-os is **isolated** — never cross-queried from other wikis
4. After processing, session summary.md gets `status: processed` appended

## Wiki Output Structure

| Folder | Purpose |
|--------|---------|
| `wiki/projects/` | Active and archived project overviews with status |
| `wiki/patterns/` | Reusable patterns, conventions, and approaches discovered across sessions |
| `wiki/decisions/` | Cross-project architectural decisions with context and rationale |
| `wiki/outputs/` | Shared components, templates, reference implementations |

## What NOT to Put Here

- AI research not tied to a specific coding project → `ai-research-os`
- Client work or supply chain deliverables → `supply-chain-os`
- Personal or family matters → `personal-os`
