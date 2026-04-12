# AI Research OS

**Domain:** AI & Machine Learning
**Purpose:** Track and synthesize AI/ML research, papers, frameworks, tools, and community knowledge.

---

## Raw Folder Sources

| Folder | Content Type | Filename Convention |
|--------|-------------|---------------------|
| `raw/articles/` | Blog posts, Substack, Medium, personal sites | `YYYY-MM-DD-{slug}.md` |
| `raw/papers/` | arXiv papers, conference papers | `YYYY-MM-DD-{author}-{title-slug}.md` |
| `raw/x-threads/` | X/Twitter threads saved as markdown | `YYYY-MM-DD-{username}-{topic}.md` |
| `raw/newsletters/` | Newsletter issues (The Batch, TLDR AI, etc.) | `YYYY-MM-DD-{newsletter}-{issue}.md` |
| `raw/youtube/` | Video transcripts, summaries | `YYYY-MM-DD-{channel}-{title-slug}.md` |
| `raw/repos/` | README files, key source files from notable repos | `{repo-name}-{YYYY-MM-DD}.md` |
| `raw/requests/` | NotebookLM research request tickets | `YYYY-MM-DD-{topic}-request.md` |

## Required Frontmatter

Every raw file must include:

```yaml
---
source: {url or reference}
date: YYYY-MM-DD
type: article | paper | thread | newsletter | video | repo | request
tags: [tag1, tag2]
status: raw | processed
---
```

## Ingest Rules

1. Files land in the correct subfolder — never directly in `raw/`
2. Ingest fires automatically on any push to `raw/`
3. After processing, mark raw file frontmatter `status: processed`
4. Wiki files are updated incrementally — existing entries are enhanced, not replaced
5. Contradictions between sources are flagged in `wiki/log.md`

## Wiki Output Structure

| Folder | Purpose |
|--------|---------|
| `wiki/concepts/` | Foundational ideas, techniques, mental models |
| `wiki/entities/` | Models, companies, people, frameworks as named entries |
| `wiki/sources/` | Source registry — one file per source |
| `wiki/syntheses/` | Multi-source analysis, comparisons, research answers |
| `wiki/outputs/` | Final outputs ready to use: reports, briefs, essays |

## What NOT to Put Here

- Personal documents or finances → `personal-os`
- Client deliverables or supply chain content → `supply-chain-os`
- Code session logs or project artefacts → `coding-projects-os`
