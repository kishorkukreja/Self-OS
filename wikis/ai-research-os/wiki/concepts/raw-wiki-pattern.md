# Raw-Wiki Pattern

**Definition:** A folder convention where `raw/` holds unstructured source material and `wiki/` holds LLM-curated, synthesised knowledge — with the LLM as the only writer of wiki/ content.

**Why it matters:** Separating input collection (raw/) from compiled knowledge (wiki/) keeps concerns clean: humans never need to structure input, and the wiki is always in a consistent state because only the LLM writes to it. This also enables automation — any push to raw/ can trigger an ingest job.

**Structure:**
```
raw/          ← humans dump anything here, any format
wiki/
  concepts/   ← one file per idea, LLM-maintained
  entities/   ← people, tools, companies, frameworks
  sources/    ← source registry with summaries
  syntheses/  ← multi-source analysis and answers
  index.md    ← master index, rebuilt on every ingest
  log.md      ← ingest history, append-only
```

**Key properties:**
- Raw files need minimal structure (just frontmatter for metadata)
- Wiki files are never edited by hand — always LLM-generated
- index.md is always a current map of the entire wiki
- Conflicts between sources are flagged at ingest time

**Related:** [[llm-knowledge-base]], [[knowledge-compounding]], [[entities/obsidian]]

**Sources:** [[sources/karpathy-llm-os-tweet-2026]], [[sources/hooeem-llm-knowledge-base-guide-2026]]

_Last updated: 2026-04-12_
