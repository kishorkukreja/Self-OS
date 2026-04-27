---
status: processed
---
     1|---
     2|source: https://github.com/zilliztech/claude-context
     3|date: 2026-04-26
     4|type: repo
     5|tags: [mcp, code-search, claude-code, zilliz, vector-search, semantic-search, agent-tooling]
     6|---
     7|
     8|# Claude Context (zilliztech/claude-context)
     9|
    10|**Repository:** https://github.com/zilliztech/claude-context  
    11|**License:** MIT  
    12|**Latest Version:** `0.1.9` (as of Apr 25, 2026)
    13|
    14|## Repository Stats
    15|- **Stars:** 9.6k | **Forks:** 730 | **Watchers:** 48
    16|- **Contributors:** 21
    17|- **Commits:** 180 on `master`
    18|- **Languages:** TypeScript (69.6%), Python (15.1%), JavaScript (10.4%)
    19|
    20|## What It Is
    21|**Claude Context** is a Model Context Protocol (MCP) plugin that adds semantic code search to Claude Code and other AI coding agents, enabling deep context from entire codebases.
    22|
    23|> Looking for persistent memory for Claude Code? Check out [memsearch Claude Code plugin](https://github.com/zilliztech/memsearch#for-claude-code-users) — a markdown-first memory system for long-term memory across sessions.
    24|
    25|### Core Value Propositions
    26|- **Entire Codebase as Context:** Uses semantic search (hybrid BM25 + dense vector) to find relevant code from millions of lines instantly. No multi-round discovery needed.
    27|- **Cost-Effective:** Stores codebases in a vector database instead of loading entire directories into the LLM for every request. Achieves **~40% token reduction** under equivalent retrieval quality conditions.
    28|
    29|---
    30|
    31|## Prerequisites
    32|
    33|- **Node.js:** `>= 20.0.0` and `< 24.0.0` (Node 24+ is incompatible)
    34|- **Vector Database:** Zilliz Cloud account (free tier available) or self-hosted Milvus
    35|- **Embedding API Key:** OpenAI API key (or VoyageAI, Ollama, Gemini)
    36|
    37|**Required Environment Variables:**
    38|- `OPENAI_API_KEY` — e.g., `sk-...`
    39|- `MILVUS_ADDRESS` — Zilliz Cloud public endpoint
    40|- `MILVUS_TOKEN` — Zilliz Cloud API key (Personal Key)
    41|
    42|---
    43|
    44|## MCP Client Configuration
    45|
    46|### Claude Code (CLI)
    47|```bash
    48|claude mcp add claude-context \\
    49|  -e OPENAI_API_KEY=*** \\
    50|  -e MILVUS_ADDRESS=your-zilliz-cloud-public-endpoint \\
    51|  -e MILVUS_TOKEN=your-z...-key \\
    52|  -- npx @zilliz/claude-context-mcp@latest
    53|```
    54|
    55|### OpenAI Codex CLI (TOML)
    56|File: `~/.codex/config.toml`
    57|```toml
    58|# IMPORTANT: the top-level key is `mcp_servers` rather than `mcpServers`.
    59|[mcp_servers.claude-context]
    60|command = "npx"
    61|args = ["@zilliz/claude-context-mcp@latest"]
    62|env = { "OPENAI_API_KEY" = "your-openai-api-key", "MILVUS_TOKEN" = "your-zilliz-cloud-api-key" }
    63|# Optional: override the default 10s startup timeout
    64|startup_timeout_ms = 20000
    65|```
    66|
    67|### Standard JSON Configuration
    68|Used by **Gemini CLI**, **Qwen Code**, **Claude Desktop**, **Cline**, **Roo Code**, **VS Code**, **Windsurf**, **Cursor**, and **Void**.
    69|
    70|*File paths vary by client* (e.g., `~/.gemini/settings.json`, `~/.qwen/settings.json`, `~/.cursor/mcp.json`, `.cursor/mcp.json`, `cline_mcp_settings.json`, etc.)
    71|
    72|```json
    73|{
    74|  "mcpServers": {
    75|    "claude-context": {
    76|      "command": "npx",
    77|      "args": ["@zilliz/claude-context-mcp@latest"],
    78|      "env": {
    79|        "OPENAI_API_KEY": "your-openai-api-key",
    80|        "MILVUS_ADDRESS": "your-zilliz-cloud-public-endpoint",
    81|        "MILVUS_TOKEN": "your-zilliz-cloud-api-key"
    82|      }
    83|    }
    84|  }
    85|}
    86|```
    87|
    88|**Notable Variations:**
    89|- **Cursor / Windsurf / VS Code:** Add `-y` to args: `["-y", "@zilliz/claude-context-mcp@latest"]`
    90|- **Void:** Server name is `code-context` instead of `claude-context`; args include `-y`
    91|- **Gemini example** omits `MILVUS_ADDRESS` in the shown config; **Qwen** includes it
    92|- **Augment Code (Manual):** Uses an array format under `augment.advanced.mcpServers`
    93|- **Augment Code (UI):** `Settings → Tools → + Add MCP` → Command: `npx @zilliz/claude-context-mcp@latest`, Name: `Claude Context`
    94|- **Cherry Studio:** GUI configuration — Type: `STDIO`, Command: `npx`, Arguments: `["@zilliz/claude-context-mcp@latest"]`, plus env vars.
    95|- **Zencoder:** Add via `Tools → Add Custom MCP`. Config is a flat JSON object (not wrapped in `mcpServers`)
    96|- **LangChain/LangGraph:** See integration example in repo.
    97|
    98|---
    99|
   100|## Usage Workflow
   101|
   102|```bash
   103|cd your-project-directory
   104|claude
   105|```
   106|
   107|Then use natural language commands:
   108|1. **Index:** `Index this codebase`
   109|2. **Check status:** `Check the indexing status`
   110|3. **Search:** `Find functions that handle user authentication`
   111|
   112|---
   113|
   114|## Available MCP Tools
   115|
   116|1. **`index_codebase`** — Index a codebase directory for hybrid search
   117|2. **`check_index_status`** — Check whether indexing is complete
   118|3. **`search_code`** — Semantic search across indexed code
   119|4. **`semantic_grep`** — Find code by meaning rather than literal string match
   120|
   121|---
   122|
   123|## Architecture
   124|
   125|- **Hybrid retrieval:** Combines BM25 (keyword) + dense vector (semantic) search via Milvus/Zilliz Cloud
   126|- **Code parsing:** Splits code into chunks with AST-aware boundaries
   127|- **Embedding:** Supports OpenAI, VoyageAI, Ollama, Gemini embedders
   128|- **Storage:** Vector DB (Milvus/Zilliz Cloud) for scalable codebase indexing
   129|
   130|---
   131|
   132|## Why It Matters
   133|
   134|Claude Context solves the "context window bottleneck" for coding agents. Instead of loading entire directories into the LLM (expensive, slow), it indexes the codebase once and retrieves only relevant snippets on demand — reducing token usage by ~40% while improving relevance through semantic search.
   135|
   136|This pattern (index once, retrieve on demand) is becoming standard for agentic coding workflows and could generalize beyond code to docs, wikis, and knowledge bases.
   137|