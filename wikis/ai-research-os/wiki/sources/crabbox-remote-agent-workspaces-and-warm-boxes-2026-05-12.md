---
title: "Crabbox \u2014 remote agent workspaces and warm boxes"
date_created: 2026-05-13
date_modified: 2026-05-13
summary: "Compiled source summary for Crabbox \u2014 remote agent workspaces and warm boxes."
tags: [crabbox, remote-execution, agent-workspaces, sandboxing, ci-hydration, parallel-agents, verification-loops, self-os]
type: source
status: final
---

# Crabbox — remote agent workspaces and warm boxes

**Type:** resource
**Date:** 2026-05-12
**URL/source:** https://crabbox.sh/
**Raw file:** [[../raw/resources/crabbox-remote-agent-workspaces-2026-05-12.md]]

**Summary:** This resource source captures **Crabbox — remote agent workspaces and warm boxes** as part of the AI Research OS stream for 2026-05-12. It is most useful as evidence about crabbox, remote-execution, agent-workspaces, sandboxing, ci-hydration, with emphasis on how agents, models, tools, workflows, or research artifacts are being operationalized rather than as an isolated announcement.

The source's main signal is that Crabbox — remote agent workspaces and warm boxes Summary Crabbox is a shared agent workspace control plane for keeping the local developer loop while running compute heavy commands on remote machines. Its tagline is: "Warm a box, sync the diff, run the suite." A local CLI leases or reuses a remote target, syncs tracked and nonignored files, runs commands remotely, streams stdout/stderr back, and releases the target. Key points Keeps the normal local workflow: editor, Git, CLI commands, dirty checkout. Moves executi.

For Self-OS, the practical implication is to treat the source as a pattern library entry: identify which capabilities should become durable skills, which workflows need reviewable artifacts, and which claims require follow-up evidence before being promoted into canonical operating guidance.

Specific details worth preserving include: Keeps the normal local workflow: editor, Git, CLI commands, dirty checkout.; Moves execution to remote capacity: brokered cloud machines, static SSH hosts, or sandbox providers.; Uses a Cloudflare Worker + Durable Object broker to manage provider credentials, leases, cleanup, usage tracking, and cost guardrails.; The CLI carries only a bearer token; provider credentials are not distributed to local machines or runners..

The raw capture remains the authoritative record; this page provides a synthesized pointer back to the raw file and should be connected to concepts/entities only where those links improve retrieval.

**Key connections:** [[concepts/remote-agent-workspaces.md|Remote Agent Workspaces]], [[concepts/iterative-repair-loops.md|Iterative Repair Loops]]

**Entities:** [[entities/openai-codex.md|Codex]], [[entities/crabbox.md|Crabbox]]

**Tags:** crabbox, remote-execution, agent-workspaces, sandboxing, ci-hydration, parallel-agents, verification-loops, self-os
