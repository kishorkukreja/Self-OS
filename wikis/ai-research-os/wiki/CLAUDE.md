# AI Research OS — Wiki Content Schema

## File Naming
- All filenames: kebab-case lowercase
- Descriptive: `attention-mechanism.md` not `paper1.md`
- No spaces, no numbers unless date-prefixed

---

## index.md Schema

Updated by ingest agent after every run. Do not edit manually.

```markdown
# AI Research OS — Index
_Last updated: YYYY-MM-DD_

## Concepts (N)
- [concept-name](concepts/concept-name.md) — one-line definition

## Entities (N)
- [entity-name](entities/entity-name.md) — [type] one-line description

## Sources (N)
- [source-title](sources/source-slug.md) — YYYY-MM-DD, type

## Syntheses (N)
- [synthesis-title](syntheses/synthesis-slug.md) — question answered, status

## Outputs (N)
- [output-title](outputs/output-slug.md) — YYYY-MM-DD, type
```

## log.md Schema

Append-only. One entry per ingest run. Do not edit manually.

```markdown
## YYYY-MM-DD HH:MM
- Ingested: N files from {types}
- Added: file1.md, file2.md
- Updated: file3.md
- Conflicts: none | {description of any contradictions found}
```

---

## concepts/ File Schema

One concept per file.

```markdown
# {Concept Name}

**Definition:** One sentence.

**Why it matters:** One paragraph max.

**Related:** [[other-concept]], [[entities/entity-name]]

**Sources:** [[sources/source-slug]]

_Last updated: YYYY-MM-DD_
```

## entities/ File Schema

One entity per file (model, company, person, framework, tool).

```markdown
# {Entity Name}

**Type:** model | company | person | framework | tool

**Description:** One sentence.

**Key facts:**
- fact 1
- fact 2

**Relationships:** [[concepts/concept]], [[entities/other-entity]]

**Sources:** [[sources/source-slug]]

_Last updated: YYYY-MM-DD_
```

## sources/ File Schema

One source per file — the source registry.

```markdown
# {Source Title}

**Type:** article | paper | thread | newsletter | video | repo
**Date:** YYYY-MM-DD
**URL:** {url}
**Raw file:** [[../raw/{subfolder}/{filename}]]

**Summary:** 2-3 sentences.

**Key contributions:**
- point 1
- point 2

**Tags:** tag1, tag2
```

## syntheses/ File Schema

Multi-source analysis documents.

```markdown
# {Research Question or Topic}

**Status:** draft | complete
**Date:** YYYY-MM-DD
**Sources consulted:** [[sources/source1]], [[sources/source2]]

## Question
{Exact question being answered}

## Findings
{Main answer — 1-3 paragraphs}

## Evidence
- [[sources/source1]]: supports X
- [[sources/source2]]: supports Y, nuances Z

## Confidence
{high | medium | low} — {reason}

## Gaps
{What remains unknown or requires further research}
```

## outputs/ File Schema

Final outputs ready to use. No fixed schema — format for the intended use (essay, brief, report).
Always include this header:

```markdown
_Generated: YYYY-MM-DD | Sources: [[syntheses/synthesis-slug]] | Status: draft | final_

---
```
