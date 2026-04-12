# Self OS — Master Wiki Router

**Last updated:** 2026-04-12
**Wikis:** 4 active

---

## Wiki Index

| Wiki | Path | Domain | Description |
|------|------|--------|-------------|
| ai-research-os | `wikis/ai-research-os/` | AI & ML | Research papers, frameworks, tools, community knowledge |
| supply-chain-os | `wikis/supply-chain-os/` | Supply Chain | Client work, industry reports, frameworks, deliverables |
| personal-os | `wikis/personal-os/` | Personal | Family businesses, personal & family finances, health |
| coding-projects-os | `wikis/coding-projects-os/` | Engineering | Coding sessions, projects, patterns, architecture decisions |

---

## Routing Rules

### Single-Topic Queries

Route to the most specific wiki first:

| Keywords / Domain | Primary Wiki | Secondary Wiki |
|-------------------|-------------|----------------|
| AI, ML, LLM, models, agents, papers, research, transformers | ai-research-os | — |
| Supply chain, logistics, procurement, sourcing, client, deliverable | supply-chain-os | — |
| Deepchand, family, bakery, weddings, personal finance, health | personal-os | — |
| Code, session, bug, architecture, project, pattern, Claude session | coding-projects-os | — |

### Multi-Topic Queries

Fan out when a query spans wikis:

| Query Pattern | Wikis to Query |
|---------------|----------------|
| "AI tools for supply chain" | ai-research-os + supply-chain-os |
| "Automation for personal finance" | ai-research-os + personal-os |
| "Build a tool for [client domain]" | coding-projects-os + supply-chain-os |
| Ambiguous / broad | Start with most specific, fan out if incomplete |

### Isolation Rules

- `coding-projects-os` is **never** cross-queried from other wikis
- `personal-os` contents are **never** surfaced in supply-chain-os outputs
- Research requests in `raw/requests/` always specify a target wiki in frontmatter

---

## Query Protocol

When given a research question:

1. Identify the domain → select wiki(s) using the routing table above
2. Navigate to `wikis/{wiki-name}/wiki/`
3. Read `index.md` first — it maps all content in the wiki
4. Check `syntheses/` for existing analysis before diving into raw content
5. If answer is incomplete, check `raw/` for unprocessed material
6. For deep research requiring NotebookLM, write a ticket to `wikis/{wiki-name}/raw/requests/`

---

## Adding a New Wiki

1. Add a row to the Wiki Index table above
2. Create `wikis/{name}/` with full folder structure (match existing wikis as template)
3. Write `wikis/{name}/CLAUDE.md` with domain purpose and raw folder schema
4. Write `wikis/{name}/wiki/CLAUDE.md` with content conventions
5. Add routing rules to this file
6. Update `.github/workflows/ingest.yml` path triggers if needed
