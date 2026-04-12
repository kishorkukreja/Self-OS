# Supply Chain OS — Wiki Content Schema

## File Naming
- All filenames: kebab-case lowercase
- Client-prefixed where relevant: `acme-supplier-analysis.md`
- No spaces, no special characters

---

## index.md Schema

Updated by ingest agent after every run. Do not edit manually.

```markdown
# Supply Chain OS — Index
_Last updated: YYYY-MM-DD_

## Concepts (N)
- [concept-name](concepts/concept-name.md) — one-line definition

## Entities (N)
- [entity-name](entities/entity-name.md) — [type] one-line description

## Sources (N)
- [source-title](sources/source-slug.md) — YYYY-MM-DD, type

## Collaterals (N)
- [collateral-title](collaterals/collateral-slug.md) — type, status

## Syntheses (N)
- [synthesis-title](syntheses/synthesis-slug.md) — topic, status

## Outputs (N)
- [output-title](outputs/output-slug.md) — YYYY-MM-DD, client, type
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

One concept per file (methodology, principle, technique).

```markdown
# {Concept Name}

**Definition:** One sentence.

**Application:** Where and how this concept applies in supply chain work.

**Related:** [[other-concept]], [[entities/entity-name]]

**Sources:** [[sources/source-slug]]

_Last updated: YYYY-MM-DD_
```

## entities/ File Schema

One entity per file (client, supplier, tool, framework, regulation).

```markdown
# {Entity Name}

**Type:** client | supplier | tool | framework | regulation

**Description:** One sentence.

**Key facts:**
- fact 1
- fact 2

**Relationships:** [[concepts/concept]], [[entities/other-entity]]

**Sources:** [[sources/source-slug]]

_Last updated: YYYY-MM-DD_
```

## sources/ File Schema

```markdown
# {Source Title}

**Type:** client-doc | industry-report | framework
**Date:** YYYY-MM-DD
**Client:** {client-name or internal}
**Confidential:** true | false
**Raw file:** [[../raw/{subfolder}/{filename}]]

**Summary:** 2-3 sentences.

**Key takeaways:**
- point 1
- point 2
```

## collaterals/ File Schema

Templates and reusable client-facing materials.

```markdown
# {Collateral Name}

**Type:** deck-template | framework | checklist | proposal-scaffold
**Status:** draft | ready-to-use
**Last used:** YYYY-MM-DD

## Purpose
{What this collateral is for}

## Structure
{Overview of sections / slides / components}

## Usage notes
{How to adapt for a specific client or engagement}
```

## syntheses/ File Schema

```markdown
# {Research Question or Topic}

**Status:** draft | complete
**Date:** YYYY-MM-DD
**Sources consulted:** [[sources/source1]], [[sources/source2]]

## Question
{Exact question being answered}

## Findings
{Main answer}

## Evidence
- [[sources/source1]]: supports X
- [[sources/source2]]: nuances Y

## Confidence
{high | medium | low} — {reason}

## Gaps
{What remains unknown}
```

## outputs/ File Schema

Final client deliverables. Always include:

```markdown
_Delivered: YYYY-MM-DD | Client: {name} | Status: draft | final | delivered_

---
```
