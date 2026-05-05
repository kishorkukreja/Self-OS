---
title: text-to-cad — Local Agent Harness for CAD Generation
date_created: '2026-05-05'
date_modified: '2026-05-05'
summary: text-to-cad is a concrete example of domain-specific harness engineering.
  Instead of asking a general chat agent to describe a CAD model, it gives coding
  agents a local repository, CAD Explorer, export/render tooling, ge
tags:
- cad
- ai-agents
- domain-specific-agents
- agent-skills
- robotics
- harness-engineering
- github-repo
type: source
status: final
---

# text-to-cad — Local Agent Harness for CAD Generation

**Type:** repo  
**Date:** 2026-05-04  
**URL:** https://github.com/earthtojake/text-to-cad  
**Raw file:** [[../raw/repos/text-to-cad-2026-05-04.md]]

## Summary
text-to-cad is a concrete example of domain-specific harness engineering. Instead of asking a general chat agent to describe a CAD model, it gives coding agents a local repository, CAD Explorer, export/render tooling, geometry references, and file-targeted skills for CAD, URDF, robot motion, and manufacturing preflight. The source matters because it shows how an agent can become useful in a specialized domain when the harness supplies stable artifacts, inspection loops, and domain operations around the model. For Self-OS, it is a reference pattern for turning raw model ability into reliable work: define the editable artifacts, make results inspectable, preserve source control, and give follow-up edits precise handles rather than vague natural-language references.

## Key contributions
- Shows how CAD generation can be organized as source-controlled agent work rather than one-shot generation.
- Uses stable geometry references and export formats to support iterative edits.
- Demonstrates a reusable pattern for domain-specific agent skills and local tool loops.

## Linked concepts and entities
- Concepts: [[concepts/domain-specific-agent-harnesses]], [[concepts/agent-skills]], [[concepts/harness-engineering]]
- Entities: [[entities/text-to-cad]]

**Tags:** cad, ai-agents, domain-specific-agents, agent-skills, robotics, harness-engineering, github-repo
