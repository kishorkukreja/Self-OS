# supply-chain-os — Schema

## Overview

Supply chain and logistics knowledge base for Coefficient Advisory client work. Covers client engagements, industry reports, operational frameworks, and client-facing deliverables. Sensitive: client content is confidential by default — never cross-reference into personal-os or other wikis.

## Directory Structure

```
raw/
  client-docs/       — Client-provided documents, briefs, data files
  industry-reports/  — Third-party reports, government data, analyst publications
  frameworks/        — Supply chain methodologies, academic frameworks, playbooks
  newsletters/       — Non-confidential newsletter research folders and draft briefs
  requests/          — Research request tickets (triggers research-request.yml)

wiki/index.md        — Master index linking every page with a one-line summary
wiki/log.md          — Append-only changelog of all operations
wiki/ingest-log.md   — Append-only list of processed raw filenames (do NOT modify raw/)
wiki/concepts/       — Supply chain concepts, methodologies, principles
wiki/entities/       — Clients, suppliers, tools, frameworks as named entries
wiki/sources/        — Source registry — one file per source
wiki/collaterals/    — Work-in-progress client-facing scaffolds and framework drafts
wiki/syntheses/      — Cross-source analysis, industry trends, comparative studies
wiki/deliverables/   — Finalised client outputs: reports, assessments, proposals
wiki/outputs/        — Filed answers to internal queries
```

## Raw File Conventions

|Folder|Filename Convention|
|---|---|
|`client-docs/`|`{client}-{YYYY-MM-DD}-{doc-type}.md`|
|`industry-reports/`|`YYYY-MM-DD-{publisher}-{title-slug}.md`|
|`frameworks/`|`{framework-name}-{YYYY-MM-DD}.md`|
|`newsletters/`|`supply-chain-signals/YYYY-Www/{daily,sources,brief}/...`|
|`requests/`|`YYYY-MM-DD-{topic}-request.md`|

Required frontmatter on every raw file:

```yaml
---
source: {url, client name, or reference}
date: YYYY-MM-DD
type: client-doc | industry-report | framework | newsletter-research | newsletter | request
client: {client-name or "internal"}
confidential: true | false
tags: [tag1, tag2]
---
```

`confidential: true` is the default for all `client-docs/`. Industry reports and frameworks default to `false`.

## Wiki File Conventions

- All filenames: kebab-case, lowercase
- Source summaries: `{client-or-publisher}-{year}-{short-title}.md`
- Deliverables: `{client}-{deliverable-type}-{version}.md` (e.g., `acme-order-cut-framework-v1.md`)
- Every wiki page MUST have YAML frontmatter:

```yaml
---
title: "Page Title"
date_created: YYYY-MM-DD
date_modified: YYYY-MM-DD
summary: "One to two sentences describing this page"
tags: [tag1, tag2]
type: concept | entity | source | synthesis | collateral | deliverable | output
status: draft | review | final | delivered
# client-specific pages only:
client: {client-name}
confidential: true | false
# concept pages only:
confidence: established | emerging | speculative
source_count: N
---
```

- Use `[[wikilinks]]` for all internal cross-references
- Link only the first occurrence of a concept per section
- **Bold key terms** on first use in each article

## Confidentiality Rules

These apply to every operation, checked before any content is written to wiki/:

1. **Before processing any file**, check its `confidential` field in frontmatter
2. Files with `confidential: true`:
    - Create a source entry in `wiki/sources/` with metadata only (title, date, client, type — no content reproduction)
    - The client's entity page in `wiki/entities/` may be updated with high-level context only
    - Do NOT create concept pages sourced solely from confidential material
    - Do NOT reproduce any content, quotes, figures, or specifics in any wiki page
3. Cross-client patterns (going into `concepts/` or `syntheses/`) must be sourced from non-confidential material only, or must be sufficiently abstracted that no client is identifiable
4. `wiki/deliverables/` pages inherit the confidentiality of their source client — mark accordingly

## Operations

### INGEST (when new raw files are added)

1. Read `wiki/ingest-log.md` to identify which raw files have already been processed
2. **Check `confidential` field first** — apply confidentiality rules before reading content
3. For each unprocessed file: a. Create a source entry in `wiki/sources/` — full summary for non-confidential, metadata-only for confidential b. Identify supply chain concepts and entities (clients, tools, regions, methodologies) c. Client-specific knowledge → create or update `wiki/entities/{client-name}.md` d. Cross-client patterns → create or update `wiki/concepts/{concept}.md` and `wiki/syntheses/` e. For confidential files: stop at step (a) — do not populate concept or entity pages with raw content f. Add `[[wikilinks]]` between related pages
4. Rebuild `wiki/index.md` to reflect all current wiki files
5. Append processed filenames to `wiki/ingest-log.md`
6. Append all operations to `wiki/log.md`
7. Do NOT modify any files in `raw/` — it is read-only

### QUERY (when asked a research or client question)

1. Read `wiki/index.md` to understand available content
2. Check `wiki/syntheses/` for existing cross-source analysis first
3. Check `wiki/collaterals/` for draft frameworks relevant to the query
4. Read relevant concept, entity, and source pages
5. Synthesise an answer — respect confidentiality: do not surface client-specific content across client contexts
6. Save the answer as `wiki/outputs/{question-slug}.md`
7. Update `wiki/index.md` and append to `wiki/log.md`

### LINT (periodic health check)

1. Find contradictions between concept pages — flag with ⚠️, noting both positions
2. Find orphan pages (no inbound wikilinks)
3. Find broken `[[wikilinks]]` pointing to non-existent files — create stubs for top 5
4. Identify missing or incomplete frontmatter fields — fix automatically
5. Flag industry reports >12 months old with no newer source on the same topic
6. Flag collaterals in `wiki/collaterals/` with `status: draft` older than 30 days — may need promotion to deliverable or archiving
7. Write lint report to `wiki/outputs/lint-report-{date}.md`
8. Append summary to `wiki/log.md`

## Page Creation Threshold

- **Full concept page:** subject appears in 2+ non-confidential sources
- **Stub page:** single mention — frontmatter + one-line definition + backlink
- **Entity page:** created on first mention of a client, supplier, or named tool
- Never leave a `[[wikilink]]` pointing to nothing — always create at least a stub

## collaterals/ vs deliverables/ Distinction

- `wiki/collaterals/` — work in progress: framework scaffolds, deck structures, draft outputs not yet shared with a client
- `wiki/deliverables/` — finalised outputs: documents that have been or are ready to be delivered to a client. Set `status: delivered` once sent.
- Promote from collaterals → deliverables when the output is finalised

## Quality Standards

- **Source summaries:** 200–500 words, synthesise — don't copy. Confidential sources: metadata block only.
- **Concept articles:** 500–1500 words with a clear lead section
- **Industry reports:** flag recency — supply chain data ages fast. Note report date prominently.
- Always trace claims to specific source pages via `[[wikilinks]]`
- Prefer recency when sources conflict on facts

## Isolation Rules

- Never cross-reference supply-chain-os content into `personal-os` outputs
- Never surface client-specific content in responses routed to other wikis
- Research requests in `raw/requests/` always specify `client` in frontmatter

## What NOT to Put Here

- AI/ML research unrelated to supply chain → `ai-research-os`
- Personal or family finances → `personal-os`
- Code sessions or project logs → `coding-projects-os`