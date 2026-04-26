# ai-research-os — Schema

## Overview

Personal knowledge base on AI & Machine Learning: models, agents, frameworks, research papers, tooling, and community knowledge. Raw sources live in `raw/`. The compiled wiki lives in `wiki/`. You (the AI) maintain all wiki content. I direct strategy; you execute compilation, maintenance, and queries.

## Directory Structure

```
raw/
  articles/     — Blog posts, Substack, Medium, personal sites
  papers/       — arXiv papers, conference papers
  x-threads/    — X/Twitter threads saved as markdown
  newsletters/  — Newsletter issues (The Batch, TLDR AI, etc.)
  youtube/      — Video transcripts, summaries
  repos/        — README files, key source files from notable repos
  resources/    — Official docs, cookbooks, reference material
  requests/     — Research request tickets (triggers research-request.yml)

wiki/index.md        — Master index linking every page with a one-line summary
wiki/log.md          — Append-only changelog of all operations
wiki/ingest-log.md   — Append-only list of processed raw filenames (do NOT modify raw/)
wiki/concepts/       — One article per concept (technique, idea, pattern)
wiki/entities/       — People, organisations, tools, models (one per file)
wiki/sources/        — One summary per raw source document
wiki/syntheses/      — Cross-cutting analysis articles, comparisons, research answers
wiki/outputs/        — Filed answers to queries
```

## Raw File Conventions

|Folder|Filename Convention|
|---|---|
|`articles/`|`YYYY-MM-DD-{slug}.md`|
|`papers/`|`YYYY-MM-DD-{author}-{title-slug}.md`|
|`x-threads/`|`YYYY-MM-DD-{username}-{topic}.md`|
|`newsletters/`|`YYYY-MM-DD-{newsletter}-{issue}.md`|
|`youtube/`|`YYYY-MM-DD-{channel}-{title-slug}.md`|
|`repos/`|`{repo-name}-{YYYY-MM-DD}.md`|
|`resources/`|`{title-slug}-{YYYY-MM-DD}.md`|
|`requests/`|`YYYY-MM-DD-{topic}-request.md`|

Required frontmatter on every raw file:

```yaml
---
source: {url or reference}
date: YYYY-MM-DD
type: article | paper | thread | newsletter | video | repo | resource | request
tags: [tag1, tag2]
---
```

## Wiki File Conventions

- All filenames: kebab-case, lowercase (e.g., `active-inference.md`)
- Source summaries: `{author-or-handle}-{year}-{short-title}.md`
- Every wiki page MUST have YAML frontmatter:

```yaml
---
title: "Page Title"
date_created: YYYY-MM-DD
date_modified: YYYY-MM-DD
summary: "One to two sentences describing this page"
tags: [topic-tag, domain-tag]
type: concept | entity | source | synthesis | output
status: draft | review | final
# concept pages only:
confidence: established | emerging | speculative
source_count: N
---
```

- Use `[[wikilinks]]` for all internal cross-references
- Link only the first occurrence of a concept per section
- **Bold key terms** on first use in each article

## Operations

### INGEST (when new raw sources are added)

1. Read `wiki/ingest-log.md` to identify which raw files have already been processed
2. Read all unprocessed raw source files
3. For each new source: a. Create a source summary in `wiki/sources/` (200–500 words, synthesise — don't copy) b. Identify concepts and entities mentioned c. Create new concept/entity pages if they don't exist yet d. Update existing pages with new information (append — don't rewrite from scratch) e. Add `[[wikilinks]]` to connect new content to existing pages
4. Rebuild `wiki/index.md` to reflect all current wiki files
5. Append processed filenames to `wiki/ingest-log.md`
6. Append all operations to `wiki/log.md`
7. Do NOT modify any files in `raw/` — it is read-only

### QUERY (when asked a research question)

1. Read `wiki/index.md` to understand available content
2. Check `wiki/syntheses/` for existing analysis before reading individual pages
3. Read the relevant wiki pages (concepts, entities, sources)
4. Synthesise an answer with citations to wiki pages via `[[wikilinks]]`
5. Save the answer as `wiki/outputs/{question-slug}.md`
6. Update `wiki/index.md` and append to `wiki/log.md`

### LINT (periodic health check)

1. Find contradictions between pages — flag with ⚠️, noting both positions
2. Find orphan pages (no inbound wikilinks)
3. Find broken `[[wikilinks]]` pointing to non-existent files — create stubs for top 5
4. Identify missing or incomplete frontmatter fields — fix automatically
5. Flag stale content (source date >6 months, no updates)
6. Suggest new articles for frequently mentioned but stub-only concepts
7. Write lint report to `wiki/outputs/lint-report-{date}.md`
8. Append summary to `wiki/log.md`

## Page Creation Threshold

- Create a **full concept/entity page** when a subject appears in 2+ sources
- For single-mention subjects, create a **stub page** (frontmatter + one-line definition + backlink to source)
- Never leave a `[[wikilink]]` pointing to nothing — always create at least a stub

## Quality Standards

- **Source summaries:** 200–500 words, synthesise — don't copy
- **Concept articles:** 500–1500 words with a clear lead section
- Always trace claims to specific source pages via `[[wikilinks]]`
- Flag contradictions with ⚠️, noting both positions
- Prefer recency when sources conflict on facts
- `confidence` field on concept pages: `established` (peer-reviewed or industry consensus), `emerging` (active research, not settled), `speculative` (theoretical or single-source)

## What NOT to Put Here

- Personal documents or finances → `personal-os`
- Client deliverables or supply chain content → `supply-chain-os`
- Code session logs or project artefacts → `coding-projects-os`