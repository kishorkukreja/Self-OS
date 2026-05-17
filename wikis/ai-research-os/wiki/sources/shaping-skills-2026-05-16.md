---
title: "rjs/shaping-skills"
date_created: 2026-05-17
date_modified: 2026-05-17
summary: "Repository capture of Ryan Singer's Claude Code skill pack for Shape Up-style shaping, framing, kickoff, and breadboarding workflows."
tags: [claude-code, skills, shape-up, agent-workflows]
type: source
status: final
---

# rjs/shaping-skills

**Type:** repo  
**Date:** 2026-05-16  
**URL:** https://github.com/rjs/shaping-skills  
**Raw file:** [[../raw/repos/shaping-skills-2026-05-16.md]]

## Summary

The `rjs/shaping-skills` repository is a high-signal bridge between product shaping practice and LLM-assisted implementation. It packages Shape Up-inspired work into Claude Code skills for framing documents, kickoff documents, shaping, breadboarding, and breadboard reflection. The raw capture emphasizes that the skills are not magic quality generators: the repository’s own GIGO warning says they can format and distill bad inputs as easily as good ones. The useful pattern is therefore not “let the agent decide the project,” but “use the agent to preserve a disciplined shaping process before coding begins.”

For Self-OS and taskOS, the repository maps directly onto the idea-to-execution gap. Framing documents help clarify why a problem is worth solving and which alternatives are rejected. Kickoff documents turn a shaped conversation into a builder-facing handoff. Breadboarding connects UI affordances, code affordances, and wiring so implementation agents get a vertical slice rather than vague product prose. The capture also suggests a quality control improvement: pair transcript-to-document skills with adversarial review before work is promoted into taskOS or Kanban.

## Key contributions

- Provides concrete skill-file patterns for shaping, framing, kickoff handoff, and breadboarding.
- Reinforces a separate shaping layer between raw ideas and autonomous coding-agent execution.
- Suggests Self-OS should combine document-generation skills with review gates that test whether the problem is worth building.

**Related:** [[concepts/shaping-layer-for-agent-workflows.md]], [[concepts/breadboarding-for-agent-handoffs.md]], [[entities/rjs-shaping-skills.md]]
