---
title: "Claude Context — Semantic Code Search MCP Plugin"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "MCP plugin from Zilliz that adds hybrid semantic code search to Claude Code and other AI coding agents, reducing token usage by ~40% through Milvus-backed retrieval."
tags: [mcp, code-search, claude-code, zilliz, vector-search, semantic-search, agent-tooling]
type: source
status: final
---

# Claude Context — Semantic Code Search MCP Plugin

**Type:** repo
**Date:** 2026-04-26
**URL:** https://github.com/zilliztech/claude-context
**Raw file:** [[../../raw/repos/claude-context-2026-04-26.md]]

**Summary:** Claude Context is a Model Context Protocol (MCP) plugin that adds semantic code search to Claude Code and other AI coding agents. It indexes entire codebases using hybrid BM25 + dense vector retrieval via Milvus or Zilliz Cloud, enabling agents to find relevant code from millions of lines instantly without multi-round discovery. By retrieving only pertinent snippets instead of loading full directories, the tool achieves approximately 40% token reduction under equivalent retrieval quality. It supports multiple MCP clients including Claude Code, OpenAI Codex, Cursor, Gemini CLI, and VS Code.

**Key contributions:**
- Hybrid retrieval combining BM25 keyword search with dense vector semantic search
- AST-aware code chunking for precise indexing boundaries
- Support for multiple embedding providers (OpenAI, VoyageAI, Ollama, Gemini)
- Broad MCP client compatibility (Claude Code, Codex, Cursor, Cline, Gemini CLI)
- ~40% token reduction compared to full-directory context loading

**Tags:** mcp, code-search, claude-code, zilliz, vector-search, semantic-search, agent-tooling
