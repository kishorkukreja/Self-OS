---
title: "Idea Capture Template"
date: 2026-05-09
type: idea-template
status: active
---

# Idea Capture Template

Copy this file to:

```text
/data/Self-OS/wikis/coding-projects-os/raw/ideas/YYYY-MM-DD-{idea-slug}.md
```

## Required frontmatter

```yaml
---
title: "Short Human Title"
date: YYYY-MM-DD
type: idea
status: seed # seed | shaping | ready-for-taskos | promoted-taskos | promoted-kanban | archived | killed
domain: coding-projects-os
source: telegram | daily-brief | weekly-synthesis | conversation | manual
origin_ref: "optional link/path/message reference"
tags: [idea, self-os]
taskos_path: null
kanban_tasks: []
---
```

## Body template

```markdown
# Short Human Title

## One-line idea

What is the idea in one sentence?

## Why it might matter

What problem, opportunity, or repeated signal does this respond to?

## Current shape

- What we know:
- What is fuzzy:
- What triggered it:

## Links / evidence

- Related wiki notes:
- Related daily/weekly briefs:
- Related external sources:

## Possible implementation shape

- Likely repo/system:
- Likely files/services:
- Dependencies:
- Risks / objections:

## Promotion checklist

Ready for taskOS when:

- [ ] Desired outcome is clear.
- [ ] Constraints are known enough.
- [ ] Acceptance criteria can be written.
- [ ] It is worth turning into a durable task/spec.

Ready for Kanban when:

- [ ] taskOS folder exists.
- [ ] Work can be assigned to a profile.
- [ ] Next action is concrete and testable.

## Next question

What is the single question that would most improve this idea?
```
