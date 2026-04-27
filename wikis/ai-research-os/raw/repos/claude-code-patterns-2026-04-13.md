---
status: processed
---
     1|---
     2|source: https://github.com/AaronRoeF/claude-code-patterns
     3|date: 2026-04-13
     4|type: repo
     5|tags: [claude-code, patterns, productivity, skills, knowledge-base, obsidian]
     6|status: raw
     7|---
     8|
     9|# Claude Code Pattern Library
    10|
    11|**137 techniques for getting the most out of Claude Code + VS Code � for power users, business operators, and anyone who wants to 10x their productivity.**
    12|
    13|By the community | April 2026 | 137 techniques
    14|
    15|> This is a community-maintained collection of real-world patterns, tips, and architectural decisions for Claude Code. Everything here has been tested in production setups. Contributions welcome � see the bottom of this file.
    16|
    17|---
    18|
    19|## How This Guide Is Organized
    20|
    21|| Part | What's Inside | Tips |
    22||------|-------------|------|
    23|| **[Part 1: What I'm Already Doing Well](#part-1-what-im-already-doing-well)** | Patterns from a real setup worth sharing | 1-11 |
    24|| **[Part 2: Pro-Tips by Category](PART2-PRO-TIPS.md)** | 97 researched techniques in 15 categories, each rated Beginner / Intermediate / Advanced | 12-124 |
    25|| **[Part 3: The AI Wiki Pattern](PART3-AI-WIKI.md)** | Building a persistent, compounding knowledge base with Claude Code + Obsidian (Karpathy's LLM Wiki, production-grade) | 125-137 |
    26|| **[Part 4: Quick Reference](PART4-QUICK-REFERENCE.md)** | Cheat sheets, keyboard shortcuts, slash commands, MCP starter kit | � |
    27|| **[Part 5: Implemented Patterns](PART5-IMPLEMENTED-PATTERNS.md)** | Live examples: hooks, test suites, and scripts actually running in production | � |
    28|
    29|---
    30|
    31|# Part 1: What I'm Already Doing Well
    32|
    33|These are patterns from a live setup that are genuinely worth replicating. Each one represents real operational leverage.
    34|
    35|## 1. The "Two OS" Architecture
    36|
    37|I run two separate repos, each with their own `CLAUDE.md`:
    38|- **WorkOS** � work skills (meeting prep, memos, RFDs, PM methodology, voice ghostwriting, ICP evaluation, rhetorical analysis)
    39|- **PersonalOS** � personal skills and compute (health data, iMessage relationship analysis, MCP servers)
    40|
    41|**Why it matters:** Clean separation of concerns. Work context never bleeds into personal tools and vice versa. Each CLAUDE.md stays focused and under the ~300-line sweet spot.
    42|
    43|**Pattern to copy:** If you have distinct domains (work vs. personal, or multiple projects), give each its own repo with its own CLAUDE.md rather than cramming everything into one.
    44|
    45|## 2. Trigger-Phrase Architecture
    46|
    47|Instead of slash commands or memorizing syntax, I use natural language triggers:
    48|
    49|| I say... | Claude loads... |
    50||----------|----------------|
    51|| "prep [name]" | meeting-prep skill ? full meeting pre-brief |
    52|| "draft a post" | ghostwriter skill ? ghostwritten content |
    53|| "PM a [concept]" | product-mgmt skill ? 9-step Working Backwards process |
    54|| "grade this" | content-review skill ? rhetorical analysis |
    55|| "health sleep" | health-tracker skill ? sleep analysis |
    56|
    57|**Why it matters:** Zero friction. I don't think about *tools* � I think about *outcomes*. Claude matches my intent to the right skill using LLM reasoning, not regex.
    58|
    59|**Pattern to copy:** Write your skill descriptions as natural phrases people would actually say. "Create a deployment plan for staging or production" beats "Deploy stuff."
    60|
    61|## 3. Skills as Markdown Files with Reference Data
    62|
    63|Each skill is a directory:
    64|```
    65|skills/meeting-prep/
    66|??? meeting-prep.md    ? the skill (triggers, workflows, guardrails)
    67|??? ref-tools.md       ? reference material (API docs, tool catalog)
    68|```
    69|
    70|**Why it matters:** The skill file tells Claude *what to do*. The ref file gives it *what it needs to know*. Progressive disclosure � Claude loads ref data only when the skill is triggered, not on every conversation.
    71|
    72|**Pattern to copy:** Don't paste your entire API reference into CLAUDE.md. Put it in a ref file and tell Claude where to find it.
    73|
    74|## 4. MCP-First Data Gathering
    75|
    76|My skills are designed to pull live data from every available source *before* producing output. The meeting-prep skill, for example:
    77|- Pulls calendar events (Google Calendar MCP)
    78|- Searches email threads (Gmail MCP)
    79|- Researches attendees (Playwright MCP ? LinkedIn)
    80|- Pulls meeting transcripts (Granola MCP)
    81|- Searches Notion for relevant docs
    82|- Does web research on companies
    83|
    84|**Why it matters:** The briefing is always richer than what I could assemble manually. Claude does in 30 seconds what would take me 15-20 minutes.
    85|
    86|**Pattern to copy:** When building skills, list every data source Claude should pull from. Be explicit: "Search Gmail for threads with [attendee]. Search Notion for relevant docs. Web search [company] for recent news."
    87|
    88|## 5. Global MCP Configuration
    89|
    90|All 7+ MCP servers are configured globally in `~/.claude.json`, not per-project. They're available everywhere:
    91|
    92|| Server | What It Does |
    93||--------|-------------|
    94|| Google Drive | Drive, Docs, Sheets, Slides, Calendar |
    95|| Gmail | Read/send email |
    96|| Jira | Issues, projects, boards, sprints |
    97|| Slack | Channels, messages, conversations |
    98|| iMessage | 25 read-only tools for message history |
    99|| Playwright | Browser automation (LinkedIn, web research) |
   100|| Granola | Meeting transcripts |
   101|| Notion | Search, fetch, create/update (built-in connector) |
   102|
   103|**Why it matters:** No configuration drift. Every session has the same capabilities. I never think "do I have access to X?" � the answer is always yes.
   104|
   105|**Pattern to copy:** Use `claude mcp add` to configure servers globally. Reserve per-project MCP for project-specific servers only.
   106|
   107|## 6. Confirmation Gates on Destructive Actions
   108|
   109|My skills explicitly do NOT send emails, push Slack messages, or make calendar changes without confirmation. Claude drafts, I confirm.
   110|
   111|**Why it matters:** I can let Claude operate with broad access (push to git, read all my email, access Slack) because the guardrails are in the *skills*, not the *permissions*. Trust but verify at the action boundary.
   112|
   113|**Pattern to copy:** In your skill files, add explicit rules like: "Draft the Slack message and present it for approval. Do NOT send until the user confirms."
   114|
   115|## 7. Pre-Approved Permissions for Speed
   116|
   117|My `settings.local.json` pre-approves dozens of commands:
   118|- Safe git operations (log, status, diff, push to specific repos)
   119|- npm/node commands for MCP servers
   120|- Specific MCP tools (Jira search, iMessage read, Notion fetch)
   121|- WebFetch for specific domains
   122|
   123|**Why it matters:** Eliminates the "approve/deny" friction that makes Claude feel slow. Safe commands fly through instantly. Risky commands still prompt me.
   124|
   125|**Pattern to copy:** Start with a small allowlist and expand it over time. Pre-approve `git log`, `git status`, `git diff`, and your test runner first.
   126|
   127|## 8. Structured Output to Defined Locations
   128|
   129|- Analyses ? `analyses/<firstname-lastname>.md`
   130|- PM packages ? `products/`
   131|- RFDs ? Notion database
   132|- Meeting debriefs ? Slack (after confirmation)
   133|
   134|**Why it matters:** I always know where to find things. No ad hoc files scattered everywhere.
   135|
   136|**Pattern to copy:** Define output locations in your skill files. "Save the analysis to `analyses/<name>.md`" ensures consistency.
   137|
   138|## 9. Environment-Aware Skills
   139|
   140|Every skill documents what's available in Claude Code vs. Claude AI:
   141|```
   142|Claude Code: Google Drive MCP, Gmail MCP, Jira MCP, Slack MCP, Playwright...
   143|Claude AI: Google Calendar (built-in), Email (built-in), Web search...
   144|```
   145|
   146|**Why it matters:** The same skills work in both environments. Claude gracefully degrades when a tool isn't available, following inline fallbacks.
   147|
   148|**Pattern to copy:** If your skills need to work across environments, document what's available where and add fallback instructions.
   149|
   150|## 10. User Identity System
   151|
   152|WorkOS detects who's using it (via `git config user.name`) and adapts:
   153|- If the owner ? use the ghostwriter voice for memos and posts
   154|- If a team member ? use professional prose, but can still invoke the ghostwriter to write *for* the owner
   155|
   156|**Why it matters:** One skill set serves the entire team. No per-user configuration needed.
   157|
   158|**Pattern to copy:** If multiple people share your CLAUDE.md, add identity detection. "Check `git config user.name` to determine the current user."
   159|
   160|## 11. Hook-Driven Self-Maintenance
   161|
   162|The most durable environments don't need manual upkeep � the hooks keep them in sync. Three hooks run silently on every file edit:
   163|
   164|- **`claude-context-updater.sh`** � when a skill, hook script, or MCP source file is modified, appends a timestamped note to `MEMORY.md` so the next session knows what changed
   165|- **`test-suite-updater.sh`** � when a new skill or MCP source file is created, automatically inserts the corresponding `assert_file_exists` assertion into `run-tests.sh`, keeping test coverage current without manual edits
   166|- **`remote-approver.sh`** � on any `PermissionRequest`, sends a push notification to phone via ntfy.sh with Approve/Deny action buttons; falls back to local prompt after 90 seconds
   167|
   168|The result: add a new skill file ? tests automatically cover it. Edit a hook ? MEMORY.md logs it. Start a long autonomous task ? approve permissions from your phone.
   169|
   170|**Why it matters:** Maintenance work that requires developer attention compounds over time. Hooks that maintain the environment autonomously pay back immediately and permanently.
   171|
   172|**Pattern to copy:** Think about what goes stale in your setup (tests, docs, logs) and write PostToolUse hooks that update them. Start with file existence tests � they're simple to auto-generate and prevent silent gaps.
   173|
   174|---
   175|
   176|## Key Sources
   177|
   178|- [Andrej Karpathy � LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) � the pattern that inspired Part 3
   179|- [Adventures in Claude](https://adventuresinclaude.ai/) � 35 posts on Claude Code workflows, learning loops, security patterns, and workflow state machines
   180|- [Claude Code Official Docs](https://code.claude.com/docs/en/best-practices)
   181|- [Builder.io � How to Write a Good CLAUDE.md](https://www.builder.io/blog/claude-md-guide)
   182|- [HumanLayer � Writing a Good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
   183|- [Arize � CLAUDE.md Best Practices](https://arize.com/blog/claude-md-best-practices-learned-from-optimizing-claude-code-with-prompt-learning/)
   184|- [SFEIR Institute � Claude Code Courses](https://institute.sfeir.com/en/claude-code/)
   185|- [Addy Osmani � Claude Code Agent Teams](https://addyosmani.com/blog/claude-code-agent-teams/)
   186|- [MCPcat � Managing Context](https://mcpcat.io/guides/managing-claude-code-context/)
   187|- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips)
   188|- [DataCamp � Claude Code Hooks Tutorial](https://www.datacamp.com/tutorial/claude-code-hooks)
   189|- [Claude Cowork](https://claude.com/product/cowork)
   190|- [MCP Specification � Tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools.md) � official tool definition requirements, error handling, naming rules
   191|
   192|---
   193|
   194|## Contributing
   195|
   196|This pattern library is a living document. If you've discovered a technique that makes Claude Code significantly more effective, we'd love to include it.
   197|
   198|**How to contribute:**
   199|
   200|1. **Fork this repo** and create a branch
   201|2. **Add your pattern** in the appropriate category, following the existing format:
   202|   - Title as `### N. Pattern Name`
   203|   - 2-4 sentence explanation of what it does and why it matters
   204|   - `**Level:**` rating (Beginner / Intermediate / Advanced)
   205|   - `**Source:**` link if applicable
   206|3. **Submit a PR** with a brief description of the pattern and how you've used it
   207|
   208|**Guidelines:**
   209|- Patterns should be tested in real workflows, not theoretical
   210|- Include the difficulty level � this helps readers prioritize
   211|- Link to sources where possible so readers can go deeper
   212|- Keep explanations concise: what it does, why it matters, how to set it up
   213|- Genericize any personal or company-specific details
   214|
   215|**What we're looking for:**
   216|- Novel hook configurations
   217|- Creative skill architectures
   218|- MCP server patterns and gotchas
   219|- Cost optimization strategies
   220|- Multi-agent orchestration patterns
   221|- Security and permission patterns
   222|
   223|