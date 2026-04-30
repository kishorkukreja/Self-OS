---
source: https://github.com/mksglu/context-mode
date: 2026-04-29
type: repo
tags: [context-mode, mcp, coding-agents, context-window, claude-code, agent-harnesses]
status: processed
---

# mksglu/context-mode

## Summary
`mksglu/context-mode` is an MCP server/plugin/extension for AI coding agents that reduces context-window waste by sandboxing large tool outputs, indexing data locally, and returning compact relevant results to the model. It targets 14 AI coding platforms including Claude Code, Qwen Code, Gemini CLI, VS Code Copilot, JetBrains Copilot, Cursor, OpenCode, KiloCode, Codex CLI, Kiro, Zed, and others.

The repository's core claim is that large raw outputs can be compressed dramatically before entering the model context: for example, 315 KB becomes 5.4 KB, a 98% reduction. It also adds session-continuity primitives, sandboxed execution, a local SQLite FTS5 knowledge base, BM25/RRF retrieval, output-compression guidance, analytics, and hook-based routing enforcement on supported platforms.

## Key points
- Repository: https://github.com/mksglu/context-mode
- Website: https://context-mode.com
- Extracted repo stats: 11.2k stars, 767 forks, 70 watchers, 49 contributors, 129 releases, latest `v1.0.103`.
- License: Elastic License 2.0.
- Core claim: “The other half of the context problem.”
- Main technique: sandbox large tool output and return only compact relevant results to the model.
- Claims 315 KB can become 5.4 KB, a 98% reduction.
- Adds session continuity after compaction/resume by tracking events in SQLite and retrieving relevant state with FTS5/BM25.
- Encourages “think in code”: the LLM should program the analysis rather than read all raw data into context.
- Claude Code integration registers hooks such as `PreToolUse`, `PostToolUse`, `PreCompact`, and `SessionStart`, plus tools such as `ctx_execute`, `ctx_batch_execute`, `ctx_index`, `ctx_search`, `ctx_fetch_and_index`, `ctx_stats`, `ctx_doctor`, `ctx_upgrade`, `ctx_purge`, and `ctx_insight`.

## Why it matters
Context Mode is relevant to agent harness engineering because it attacks one of the biggest practical bottlenecks in long-running coding agents: context pollution from raw tool output. It pairs well with Self-OS patterns around compaction, resumability, file-backed state, token efficiency, and multi-agent coding workflows.

## Raw content
The repository title says: “Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 14 platforms.” The extracted repository summary described Context Mode as an MCP server, plugin, or extension for AI coding agents that reduces context-window waste by sandboxing large tool outputs, indexing data locally, and returning compact relevant results to the model.

Supported platforms listed include Claude Code, Qwen Code, Gemini CLI, VS Code Copilot, JetBrains Copilot, Cursor, OpenCode, KiloCode, OpenClaw / Pi Agent, Codex CLI, Antigravity, Kiro, Zed, and Pi Coding Agent.

The README frames the problem as every MCP/tool call dumping raw output into model context: Playwright snapshots, GitHub issue lists, access logs, and other bulky outputs can consume context quickly. After compaction, agents may forget edited files, in-progress tasks, last user requests, resolved errors, decisions, and constraints.

Context Mode claims to solve “all four sides” of the context problem. For context saving, sandbox tools keep raw data out of the context window, with the headline claim “315 KB becomes 5.4 KB. 98% reduction.” For session continuity, Context Mode tracks session events in SQLite: file edits, git operations, tasks, errors, user decisions, constraints, rules, tool calls, and more. It indexes events into SQLite FTS5 and retrieves relevant state via BM25 search instead of dumping all history back into context. Fresh sessions delete prior session data unless `--continue` is used.

The README advocates “think in code”: the LLM should program the analysis, not compute it. Rather than reading many files into context, the model writes code that processes data and prints only the answer. The example contrasts 47 file reads totaling 700 KB with one `ctx_execute` call producing 3.6 KB.

The output-compression guidance uses a terse style: “Terse like caveman. Technical substance exact. Only fluff die.” Rules include dropping articles and filler words, dropping pleasantries and hedging, allowing fragments, keeping code unchanged, using the pattern `[thing] [action] [reason]. [next step].`, and auto-expanding for security warnings, irreversible actions, and user confusion.

For Claude Code, installation uses plugin marketplace commands and verification through `/context-mode:ctx-doctor`. The Claude Code plugin registers hooks including `PreToolUse`, `PostToolUse`, `PreCompact`, and `SessionStart`, sandbox tools including `ctx_batch_execute`, `ctx_execute`, `ctx_execute_file`, `ctx_index`, `ctx_search`, and `ctx_fetch_and_index`, plus meta-tools such as `ctx_stats`, `ctx_doctor`, `ctx_upgrade`, `ctx_purge`, and `ctx_insight`.
