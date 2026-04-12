# Web as Filesystem

**Definition:** The pattern of mounting web documentation as a Unix filesystem so AI agents can browse docs using `cat`, `grep`, `tree`, and `find` — the same tools they were pre-trained on — instead of using RAG or MCP tool schemas.

**Why it matters:** Code hallucination is fundamentally a docs staleness problem: model training data lags API changes by months or years. RAG retrieves fragments but loses cross-page context. A filesystem mount gives agents the whole doc, navigated with tools baked into billions of tokens of pretraining. Agents don't need to learn a new interface.

**How it works (nia-docs):**
1. `npx nia-docs https://docs.example.com` — one command, no API key, no install
2. Backend crawls the site, maps each URL to a file path (stripping common prefixes)
3. Exposes `read`, `grep`, `ls`, `tree`, `find` as API endpoints
4. Client-side virtual bash shell (just-bash in TypeScript) runs commands in-memory
5. Namespaces are shared — index once, everyone benefits

**Advantages over RAG:**
- No chunking → full files, no lost context
- No embedding models → no cold start
- No vector DB → millisecond grep across 500 pages
- No JSON schema per tool → one filesystem abstraction for everything

**Advantages over MCP:**
- No schema, no NL description, no argument construction — just standard Unix
- Agents already know these tools from pretraining

**Related:** [[llm-knowledge-base]], [[entities/nia-docs]]

**Sources:** [[sources/arlanr-web-as-filesystem-2026]]

_Last updated: 2026-04-12_
