# Self OS Knowledge Base Architecture — Archive

**Exported:** 2026-04-12
**Scope:** Full conversation — design of a multi-wiki personal knowledge operating system built on GitHub, Claude Code, NotebookLM, OpenFang, and Obsidian.

---

## 1. Origin

Kish wants to build a "Self OS" — a Personal Knowledge Operating System that functions as a digital version of himself. The trigger for this specific conversation was two source documents shared:

1. A guide on connecting Claude Code to NotebookLM via `notebooklm-py` CLI, covering four workflows: zero-token research, building expert AI agents, persistent session memory, and Obsidian-based visual knowledge management.
2. A full course on building LLM knowledge bases based on Karpathy's pattern — covering raw/wiki folder structure, CLAUDE.md schema, ingest/query/lint cycles, and automation levels from single Claude Code commands up to GitHub Actions.

The ask: refine thinking from prior Self OS discussions, incorporate both sources, and design a system that works across Claude Code (laptop), web Claude, and app Claude — with NotebookLM for heavy research, OpenFang agents on VPS for automation, and Obsidian as the local IDE.

---

## 2. Context & Constraints

**Existing infrastructure:**
- Hetzner VPS (ARM CAX series) with Coolify, Homarr, OpenClaw, Tailscale installed
- Claude Code on laptop — confirmed installed
- NotebookLM-py — not yet installed, starting from zero
- GitHub — new repo to be created specifically for knowledge base
- Obsidian — to be used as local IDE on laptop

**Core constraints:**
- Data sovereignty — everything self-hosted or in own GitHub repo
- Open formats — markdown only, no proprietary formats
- Multi-client reality — Claude Code writes files; web/app Claude reads and writes via GitHub MCP
- Outline (originally planned as knowledge layer) — dropped from critical path for this system; may be added later as human-readable web UI only
- Notion — explicitly rejected previously (external hosting, proprietary format)

**Prior Self OS architecture (from memory):**
- Four-phase roadmap established in earlier sessions
- Original plan had Outline as central knowledge layer with mcp-outline bridge
- This conversation supersedes that plan for the knowledge base layer specifically

**Source materials referenced:**
- LLM Wiki v2 article (extending Karpathy's pattern with agent memory)
- Karpathy's original LLM knowledge base tweet (April 2, 2026)
- notebooklm-py CLI documentation and workflow guide

---

## 3. Evolution

**Starting question — where does the wiki live?**
Original Self OS plan had Outline on VPS. The two source documents pointed toward local markdown vaults (Obsidian-style). These are different beasts. Three options were considered:

- Option A: Local-first (Obsidian + Claude Code on laptop). Problem: web/app Claude can't reach local files.
- Option B: VPS-first (Outline as web UI + API). Problem: loses Obsidian's plugin ecosystem entirely.
- Option C: Both, synced via Git. Files live locally (Obsidian + Claude Code), Git pushes to VPS, agents run on VPS, web/app Claude accesses via GitHub MCP. **Selected.**

**Outline re-evaluation:**
Once GitHub MCP was established as the web Claude write path, Outline's role collapsed. OpenFang agents on VPS don't need Outline — they git clone and read/write markdown directly. Web Claude accesses via GitHub MCP. Outline was dropped from the critical path. May be added later as a human-readable browser UI only.

**Multi-wiki architecture:**
Kish confirmed he'll need 5-8 wikis over time. Options considered:
- Code-based router (MoE approach) — rejected as overengineered at this scale
- Separate repo per wiki — rejected (cross-reference harder, access control only reason to do it)
- Single repo, directory per wiki, MASTER.md as router — **selected**

MASTER.md handles both the wiki map (what each wiki contains) and routing rules (which wikis to query for a given request). Originally proposed as two files (MASTER.md + ROUTER.md) — correctly called out as redundant and collapsed into one.

**NotebookLM integration:**
- From Claude Code: direct CLI invocation → findings saved to raw/ → git push → ingest fires. Clean.
- From web Claude: web Claude writes a `research_request.md` job ticket to `raw/requests/` via GitHub MCP → OpenFang agent on VPS detects it → runs notebooklm-py → saves findings to raw/ → deletes ticket → git push → ingest fires. Confirmed as workable pattern, also reusable for any future heavy VPS task.

**Session storage for coding projects:**
Kish wanted a folder in raw/ for Claude Code and Codex session outputs, keyed by session ID. Agreed that coding sessions get their own dedicated wiki (`coding-projects-os`) rather than routing into other wikis.

**Wiki naming convention:**
All four wikis use `-os` suffix, consistent with Self OS framing.

**Raw folder design per wiki:**
Each wiki has a tailored raw/ structure based on its source types, established through Q&A:
- ai-research-os: articles, papers, x-threads, newsletters, youtube, repos, requests
- supply-chain-os: client-docs, industry-reports, frameworks, requests
- personal-os: deepchand-bakers, deepchand-weddings, self-finance, family-finance, health
- coding-projects-os: sessions/claude/{session-id}, sessions/codex/{session-id}, projects/{project-name}

---

## 4. Decisions & Outputs

**Decisions made:**

1. Option C architecture — local Obsidian + Claude Code + Git sync to VPS + GitHub MCP for web/app Claude
2. GitHub as source of truth, single repo: `knowledge-base`
3. Outline dropped from knowledge base critical path
4. Single repo, directory-per-wiki structure with MASTER.md router
5. Four wikis at launch: ai-research-os, supply-chain-os, personal-os, coding-projects-os
6. NotebookLM write path from web Claude: job ticket pattern via raw/requests/
7. GitHub Actions as universal ingest trigger (fires on any push to raw/)
8. coding-projects-os is isolated — fed only from raw/sessions/, never cross-queried
9. Each session folder has consistent structure: summary.md, decisions.md, artefacts/

**Complete folder structure produced:**

```
knowledge-base/                          ← GitHub repo root
│
├── MASTER.md                            ← wiki map + routing rules
│
├── wikis/
│   │
│   ├── ai-research-os/
│   │   ├── CLAUDE.md
│   │   ├── raw/
│   │   │   ├── articles/
│   │   │   ├── papers/
│   │   │   ├── x-threads/
│   │   │   ├── newsletters/
│   │   │   ├── youtube/
│   │   │   ├── repos/
│   │   │   └── requests/
│   │   └── wiki/
│   │       ├── CLAUDE.md
│   │       ├── index.md
│   │       ├── log.md
│   │       ├── concepts/
│   │       ├── entities/
│   │       ├── sources/
│   │       ├── syntheses/
│   │       └── outputs/
│   │
│   ├── supply-chain-os/
│   │   ├── CLAUDE.md
│   │   ├── raw/
│   │   │   ├── client-docs/
│   │   │   ├── industry-reports/
│   │   │   ├── frameworks/
│   │   │   └── requests/
│   │   └── wiki/
│   │       ├── CLAUDE.md
│   │       ├── index.md
│   │       ├── log.md
│   │       ├── concepts/
│   │       ├── entities/
│   │       ├── sources/
│   │       ├── collaterals/
│   │       ├── syntheses/
│   │       └── outputs/
│   │
│   ├── personal-os/
│   │   ├── CLAUDE.md
│   │   ├── raw/
│   │   │   ├── deepchand-bakers/
│   │   │   ├── deepchand-weddings/
│   │   │   ├── self-finance/
│   │   │   ├── family-finance/
│   │   │   └── health/
│   │   └── wiki/
│   │       ├── CLAUDE.md
│   │       ├── index.md
│   │       ├── log.md
│   │       ├── summaries/
│   │       ├── decisions/
│   │       └── actions/
│   │
│   └── coding-projects-os/
│       ├── CLAUDE.md
│       ├── raw/
│       │   ├── sessions/
│       │   │   ├── claude/
│       │   │   │   └── {session-id}/
│       │   │   │       ├── summary.md
│       │   │   │       ├── decisions.md
│       │   │   │       └── artefacts/
│       │   │   └── codex/
│       │   │       └── {session-id}/
│       │   │           ├── summary.md
│       │   │           ├── decisions.md
│       │   │           └── artefacts/
│       │   └── projects/
│       │       └── {project-name}/
│       │           ├── prd.md
│       │           ├── architecture.md
│       │           └── specs/
│       └── wiki/
│           ├── CLAUDE.md
│           ├── index.md
│           ├── log.md
│           ├── projects/
│           ├── patterns/
│           ├── decisions/
│           └── outputs/
│
└── .github/
    └── workflows/
        ├── ingest.yml
        └── research-request.yml
```

**Architecture diagram (full system):**

```
╔══════════════════════════════════════════════════════════════════════════╗
║  CLIENTS                                                                 ║
║  ┌─────────────┐   ┌─────────────────┐   ┌──────────────────────────┐  ║
║  │ Claude Code │   │   Web Claude    │   │      App Claude          │  ║
║  │  (laptop)   │   │ (GitHub MCP)    │   │   (GitHub MCP)           │  ║
║  └──────┬──────┘   └────────┬────────┘   └────────────┬─────────────┘  ║
╚═════════╪══════════════════╪═════════════════════════╪════════════════╝
          │ git push         │ writes via MCP           │ reads via MCP
╔═════════╪══════════════════╪══════════════════════════╪════════════════╗
║  GITHUB REPO (source of truth)                                          ║
║          ▼                  ▼                          ▼                ║
║  ┌───────────────────────────────────────────────────────────────────┐  ║
║  │  knowledge-base/                                                  │  ║
║  │  MASTER.md + wikis/ai-research-os/ + supply-chain-os/             │  ║
║  │  personal-os/ + coding-projects-os/                               │  ║
║  └──────────────────────────┬────────────────────────────────────────┘  ║
║                    push to raw/ triggers                                 ║
║  ┌─────────────────────────────────────────────────────────────────────┐ ║
║  │  GitHub Actions                                                     │ ║
║  │  ingest.yml (fires on raw/ push)                                    │ ║
║  │  research-request.yml (fires on requests/ push)                     │ ║
║  └──────────────────────────┬────────────────────────────────────────── ║
╚═════════════════════════════╪══════════════════════════════════════════╝
                              ▼
╔═════════════════════════════════════════════════════════════════════════╗
║  VPS (Hetzner)                                                          ║
║  ┌──────────────────────────┐   ┌─────────────────────────────────┐    ║
║  │   OpenFang Agents        │   │   notebooklm-py                 │    ║
║  │  Ingest Agent            │   │  ← triggered by research-       │    ║
║  │  ├── reads raw/          │   │    request.yml                  │    ║
║  │  ├── compiles wiki/      │   │  → runs deep research           │    ║
║  │  ├── updates index.md    │   │  → saves findings to raw/       │    ║
║  │  └── git push back       │   │  → deletes request ticket       │    ║
║  │  Wrap-up Agent           │   │  → git push → ingest fires      │    ║
║  │  ├── end of session      │   └─────────────────────────────────┘    ║
║  │  ├── writes sessions/    │                                           ║
║  │  └── git push → ingest   │                                           ║
║  └──────────────────────────┘                                           ║
╚═════════════════════════════════════════════════════════════════════════╝
╔═════════════════════════════════════════════════════════════════════════╗
║  LOCAL (laptop)                                                         ║
║  ┌──────────────┐     ┌──────────────────────────────────────────┐    ║
║  │   Obsidian   │     │   Claude Code                            │    ║
║  │  graph view  │◀────│   ├── /wiki-ingest                       │    ║
║  │  dataview    │     │   ├── /wiki-query                        │    ║
║  │  plugins     │     │   ├── /wiki-lint                         │    ║
║  └──────────────┘     │   ├── /notebooklm-research               │    ║
║                        │   └── /wrap-up                           │    ║
║                        └──────────────────────────────────────────┘    ║
║         both read from git clone of knowledge-base repo                 ║
╚═════════════════════════════════════════════════════════════════════════╝
```

**Phased build plan:**

```
PHASE 1 — FOUNDATION
├── Create GitHub repo: knowledge-base
├── Scaffold full folder structure
├── Write MASTER.md
├── Write CLAUDE.md for each wiki
└── Git clone to laptop → open in Obsidian

PHASE 2 — LOCAL LOOP
├── Install notebooklm-py + authenticate
├── Create Claude Code skills:
│   ├── /wiki-ingest
│   ├── /wiki-query
│   ├── /wiki-lint
│   ├── /notebooklm-research
│   └── /wrap-up
└── Test end-to-end: drop file in raw/ → ingest → wiki/

PHASE 3 — WEB CLAUDE WRITE PATH
├── Add GitHub MCP to web Claude
├── Test: web Claude writes to raw/ via MCP
└── Test: web Claude writes research_request.md → VPS picks it up

PHASE 4 — VPS AUTOMATION
├── Set up OpenFang ingest agent
├── Set up GitHub Actions (ingest.yml + research-request.yml)
├── Set up notebooklm-py on VPS
└── Test full pipeline: request ticket → research → raw/ → wiki/

PHASE 5 — PERIODIC MAINTENANCE
├── Scheduled lint (weekly)
├── Scheduled digest generation (daily/weekly/monthly)
└── Cross-wiki query testing via MASTER.md
```

---

## 5. Current State

Architecture is fully designed and agreed. Nothing has been built yet. The conversation ended at the point of producing the archive.

**Completed in this session:**
- Full system architecture decided
- All four wikis named and scoped
- Complete folder structure for all four wikis designed
- GitHub Actions trigger pattern agreed
- NotebookLM job ticket pattern (web Claude → VPS) agreed
- Phased build plan produced

**Not yet started:**
- GitHub repo creation
- Folder scaffolding
- Any CLAUDE.md files
- notebooklm-py installation
- GitHub MCP setup on web Claude
- Any OpenFang agent configuration
- GitHub Actions workflows

---

## 6. Open Items

- **notebooklm-py installation** — needs to happen on both laptop (for Claude Code) and VPS (for agent automation). Starting from zero.
- **GitHub MCP** — needs to be added to web Claude connectors before Phase 3 can start.
- **OpenFang agent configuration** — how exactly to configure the ingest agent and wrap-up agent on VPS. Not yet designed at implementation level.
- **CLAUDE.md content** — the actual schema files for each wiki need to be written. Structure agreed, content not yet produced.
- **MASTER.md content** — routing rules format not yet designed. Needs a template.
- **research_request.md format** — skeleton agreed (YAML frontmatter with type, query, wiki, depth, requested_by) but not fully specced.
- **Outline** — parked. May be added later as human-readable browser UI pointing at the same markdown files. Not in critical path.
- **Cross-wiki query behaviour** — MASTER.md will handle routing but exact prompting pattern for multi-wiki queries not yet designed.
- **Digest generation** — daily/weekly/monthly review digests were part of original Self OS vision. Format and trigger not yet designed.

---

## 7. Raw Context

**Research request ticket format (agreed skeleton):**
```markdown
---
type: research_request
query: "B2B outbound sales strategies 2026"
wiki: supply-chain-os
depth: deep
requested_by: web-claude
---
```

**Session folder structure (coding-projects-os):**
```
raw/sessions/claude/{session-id}/
├── summary.md
├── decisions.md
└── artefacts/

raw/sessions/codex/{session-id}/
├── summary.md
├── decisions.md
└── artefacts/
```

**GitHub Actions files to create:**
- `.github/workflows/ingest.yml` — fires on push to any `raw/` directory
- `.github/workflows/research-request.yml` — fires on push to any `requests/` directory

**Claude Code skills to create:**
- `/wiki-ingest` — process new raw/ files into wiki/
- `/wiki-query` — research question across wiki, file answer back
- `/wiki-lint` — health check, fix contradictions/orphans/broken links
- `/notebooklm-research` — invoke notebooklm-py, save findings to raw/
- `/wrap-up` — end of session extraction, write to sessions/ folder, git push

**Key naming conventions:**
- Wiki names: `{domain}-os` (e.g., `ai-research-os`)
- All filenames: kebab-case lowercase
- Session folders: named by session ID
- Project folders: named by project name

**supply-chain-os wiki/ has one extra folder vs others:**
- `collaterals/` — for client-facing decks, frameworks, deliverable outputs

**personal-os wiki/ structure differs from others:**
- `summaries/`, `decisions/`, `actions/` instead of concepts/entities/sources/syntheses