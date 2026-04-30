---
title: "mksglu/context-mode"
date_created: 2026-04-30
date_modified: 2026-04-30
summary: "mksglu/context-mode is an MCP server/plugin/extension for AI coding agents that reduces context-window waste by sandboxing large tool outputs, indexing data locally, and returning compact relevant results to the model. I"
tags: [context-mode, mcp, coding-agents, context-window, claude-code, agent-harnesses]
type: source
status: final
---

# mksglu/context-mode

**Type:** repo  
**Date:** 2026-04-29  
**URL:** https://github.com/mksglu/context-mode  
**Raw file:** [[../raw/repos/context-mode-2026-04-29.md]]

**Summary:** mksglu/context-mode is an MCP server/plugin/extension for AI coding agents that reduces context-window waste by sandboxing large tool outputs, indexing data locally, and returning compact relevant results to the model. It targets 14 AI coding platforms including Claude Code, Qwen Code, Gemini CLI, VS Code Copilot, JetBrains Copilot, Cursor, OpenCode, KiloCode, Codex CLI, Kiro, Zed, and others.
The repository's core claim is that large raw outputs can be compressed dramatically before entering the model context: for example, 315 KB becomes 5.4 KB, a 98% reduction. It also adds session-continuity primitives, sandboxed execution, a local SQLite FTS5 knowledge base, BM25/RRF retrieval, output-compression guidance, analytics, and hook-based routing enforcement on supported platforms.

**Key contributions:**
- Repository: https://github.com/mksglu/context-mode
- Website: https://context-mode.com
- Extracted repo stats: 11.2k stars, 767 forks, 70 watchers, 49 contributors, 129 releases, latest v1.0.103.
- License: Elastic License 2.0.
- Core claim: “The other half of the context problem.”
- Main technique: sandbox large tool output and return only compact relevant results to the model.

**Tags:** context-mode, mcp, coding-agents, context-window, claude-code, agent-harnesses
