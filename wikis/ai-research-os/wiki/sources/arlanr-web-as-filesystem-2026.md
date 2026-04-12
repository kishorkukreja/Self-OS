---
title: "Turning the Entire Web Into a Filesystem"
date_created: 2026-04-12
date_modified: 2026-04-12
summary: "Code hallucination is a docs staleness problem — the solution is mounting documentation sites as Unix filesystems so agents browse with familiar shell tools instead of RAG."
tags: [web-as-filesystem, nia-docs, code-hallucination, rag-alternative, agent-tools]
type: source
status: final
---

# Turning the Entire Web Into a Filesystem

**Type:** thread
**Date:** 2026-04-06
**URL:** https://x.com/arlanr/status/2041215978957389908
**Raw file:** [[../../raw/x-threads/Turning the entire web into a filesystem.md]]

**Summary:** Code hallucinations are a data problem, not a model problem — models can't keep up with API changes. The solution: mount any documentation site as a Unix filesystem so agents can `cat`, `grep`, `tree` and `find` docs the same way they read code. Built as `nia-docs` / `agentsearch.sh`. One command gives an agent a bash shell where any documentation is mounted as a filesystem, with full text search in milliseconds.

**Key contributions:**
- Reframes code hallucination as a docs staleness problem, not a model capability problem
- Unix filesystem abstraction as the universal agent interface (50+ years of pretraining baked in)
- nia-docs: `npx nia-docs https://docs.example.com` mounts docs as filesystem, no API key needed
- No chunking/RAG tradeoffs: agents `cat` whole files, not fragments
- Namespaces are shared — once someone indexes `docs.stripe.com`, everyone benefits
- Comparison to MCP: filesystem needs no JSON schema, no NL descriptions, no argument construction

**Tags:** code-hallucination, web-as-filesystem, nia-docs, agent-tools, documentation, rag-alternative
