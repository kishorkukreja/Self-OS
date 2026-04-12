# Supply Chain OS

**Domain:** Supply Chain & Logistics
**Purpose:** Track client work, industry knowledge, frameworks, and produce client-facing deliverables.

---

## Raw Folder Sources

| Folder | Content Type | Filename Convention |
|--------|-------------|---------------------|
| `raw/client-docs/` | Client-provided documents, briefs, data files | `{client}-{YYYY-MM-DD}-{doc-type}.md` |
| `raw/industry-reports/` | Third-party reports, government data, analyst publications | `YYYY-MM-DD-{publisher}-{title-slug}.md` |
| `raw/frameworks/` | Supply chain methodologies, academic frameworks, playbooks | `{framework-name}-{YYYY-MM-DD}.md` |
| `raw/requests/` | NotebookLM research request tickets | `YYYY-MM-DD-{topic}-request.md` |

## Required Frontmatter

Every raw file must include:

```yaml
---
source: {url, client name, or reference}
date: YYYY-MM-DD
type: client-doc | industry-report | framework | request
client: {client-name or internal}
tags: [tag1, tag2]
status: raw | processed
confidential: true | false
---
```

## Ingest Rules

1. Files land in the correct subfolder — never directly in `raw/`
2. Ingest fires automatically on any push to `raw/`
3. Files marked `confidential: true` are processed but their raw content is not surfaced in outputs
4. After processing, mark raw file frontmatter `status: processed`
5. Client-specific knowledge goes into entities/ under the client name
6. Cross-client patterns go into concepts/ and syntheses/

## Wiki Output Structure

| Folder | Purpose |
|--------|---------|
| `wiki/concepts/` | Supply chain concepts, methodologies, principles |
| `wiki/entities/` | Clients, suppliers, tools, frameworks as named entries |
| `wiki/sources/` | Source registry — one file per source |
| `wiki/collaterals/` | Client-facing decks, framework templates, deliverable scaffolds |
| `wiki/syntheses/` | Cross-source analysis, industry trends, comparative studies |
| `wiki/outputs/` | Final deliverables — reports, assessments, proposals |

## What NOT to Put Here

- AI/ML research unrelated to supply chain → `ai-research-os`
- Personal or family finances → `personal-os`
- Code sessions or project logs → `coding-projects-os`
