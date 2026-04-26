---
source: https://github.com/zilliztech/claude-context
date: 2026-04-26
type: repo
tags: [mcp, code-search, claude-code, zilliz, vector-search, semantic-search, agent-tooling]
---

# Claude Context (zilliztech/claude-context)

**Repository:** https://github.com/zilliztech/claude-context  
**License:** MIT  
**Latest Version:** `0.1.9` (as of Apr 25, 2026)

## Repository Stats
- **Stars:** 9.6k | **Forks:** 730 | **Watchers:** 48
- **Contributors:** 21
- **Commits:** 180 on `master`
- **Languages:** TypeScript (69.6%), Python (15.1%), JavaScript (10.4%)

## What It Is
**Claude Context** is a Model Context Protocol (MCP) plugin that adds semantic code search to Claude Code and other AI coding agents, enabling deep context from entire codebases.

> Looking for persistent memory for Claude Code? Check out [memsearch Claude Code plugin](https://github.com/zilliztech/memsearch#for-claude-code-users) — a markdown-first memory system for long-term memory across sessions.

### Core Value Propositions
- **Entire Codebase as Context:** Uses semantic search (hybrid BM25 + dense vector) to find relevant code from millions of lines instantly. No multi-round discovery needed.
- **Cost-Effective:** Stores codebases in a vector database instead of loading entire directories into the LLM for every request. Achieves **~40% token reduction** under equivalent retrieval quality conditions.

---

## Prerequisites

- **Node.js:** `>= 20.0.0` and `< 24.0.0` (Node 24+ is incompatible)
- **Vector Database:** Zilliz Cloud account (free tier available) or self-hosted Milvus
- **Embedding API Key:** OpenAI API key (or VoyageAI, Ollama, Gemini)

**Required Environment Variables:**
- `OPENAI_API_KEY` — e.g., `sk-...`
- `MILVUS_ADDRESS` — Zilliz Cloud public endpoint
- `MILVUS_TOKEN` — Zilliz Cloud API key (Personal Key)

---

## MCP Client Configuration

### Claude Code (CLI)
```bash
claude mcp add claude-context \\
  -e OPENAI_API_KEY=sk-your-openai-api-key \\
  -e MILVUS_ADDRESS=your-zilliz-cloud-public-endpoint \\
  -e MILVUS_TOKEN=your-zilliz-cloud-api-key \\
  -- npx @zilliz/claude-context-mcp@latest
```

### OpenAI Codex CLI (TOML)
File: `~/.codex/config.toml`
```toml
# IMPORTANT: the top-level key is `mcp_servers` rather than `mcpServers`.
[mcp_servers.claude-context]
command = "npx"
args = ["@zilliz/claude-context-mcp@latest"]
env = { "OPENAI_API_KEY" = "your-openai-api-key", "MILVUS_TOKEN" = "your-zilliz-cloud-api-key" }
# Optional: override the default 10s startup timeout
startup_timeout_ms = 20000
```

### Standard JSON Configuration
Used by **Gemini CLI**, **Qwen Code**, **Claude Desktop**, **Cline**, **Roo Code**, **VS Code**, **Windsurf**, **Cursor**, and **Void**.

*File paths vary by client* (e.g., `~/.gemini/settings.json`, `~/.qwen/settings.json`, `~/.cursor/mcp.json`, `.cursor/mcp.json`, `cline_mcp_settings.json`, etc.)

```json
{
  "mcpServers": {
    "claude-context": {
      "command": "npx",
      "args": ["@zilliz/claude-context-mcp@latest"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "MILVUS_ADDRESS": "your-zilliz-cloud-public-endpoint",
        "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
      }
    }
  }
}
```

**Notable Variations:**
- **Cursor / Windsurf / VS Code:** Add `-y` to args: `["-y", "@zilliz/claude-context-mcp@latest"]`
- **Void:** Server name is `code-context` instead of `claude-context`; args include `-y`
- **Gemini example** omits `MILVUS_ADDRESS` in the shown config; **Qwen** includes it
- **Augment Code (Manual):** Uses an array format under `augment.advanced.mcpServers`
- **Augment Code (UI):** `Settings → Tools → + Add MCP` → Command: `npx @zilliz/claude-context-mcp@latest`, Name: `Claude Context`
- **Cherry Studio:** GUI configuration — Type: `STDIO`, Command: `npx`, Arguments: `["@zilliz/claude-context-mcp@latest"]`, plus env vars.
- **Zencoder:** Add via `Tools → Add Custom MCP`. Config is a flat JSON object (not wrapped in `mcpServers`)
- **LangChain/LangGraph:** See integration example in repo.

---

## Usage Workflow

```bash
cd your-project-directory
claude
```

Then use natural language commands:
1. **Index:** `Index this codebase`
2. **Check status:** `Check the indexing status`
3. **Search:** `Find functions that handle user authentication`

---

## Available MCP Tools

1. **`index_codebase`** — Index a codebase directory for hybrid search
2. **`check_index_status`** — Check whether indexing is complete
3. **`search_code`** — Semantic search across indexed code
4. **`semantic_grep`** — Find code by meaning rather than literal string match

---

## Architecture

- **Hybrid retrieval:** Combines BM25 (keyword) + dense vector (semantic) search via Milvus/Zilliz Cloud
- **Code parsing:** Splits code into chunks with AST-aware boundaries
- **Embedding:** Supports OpenAI, VoyageAI, Ollama, Gemini embedders
- **Storage:** Vector DB (Milvus/Zilliz Cloud) for scalable codebase indexing

---

## Why It Matters

Claude Context solves the "context window bottleneck" for coding agents. Instead of loading entire directories into the LLM (expensive, slow), it indexes the codebase once and retrieves only relevant snippets on demand — reducing token usage by ~40% while improving relevance through semantic search.

This pattern (index once, retrieve on demand) is becoming standard for agentic coding workflows and could generalize beyond code to docs, wikis, and knowledge bases.
