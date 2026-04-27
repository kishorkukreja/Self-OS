---
status: processed
---
     1|---
     2|source: https://x.com/eng_khairallah1/status/2046519525907317043
     3|date: 2026-04-26
     4|type: thread
     5|tags: [claude-code, tips, tricks, workflow, productivity, agent-coding, commands]
     6|---
     7|
     8|# 35 Claude Code Commands, Tricks, and Workflows That Most Users Don't Know — The Complete List
     9|
    10|**Author:** Khairallah AL-Awady (@eng_khairallah1)  
    11|**Posted:** Apr 21, 2026  
    12|**Engagement:** 57 replies, 262 reposts, 1.5K likes, 11K bookmarks, 5M views
    13|
    14|---
    15|
    16|> I have been using Claude Code daily for months. These are the 35 techniques that make it feel like a cheat code.
    17|>
    18|> Most developers install Claude Code, use it for basic code generation, and think they have seen what it can do. They have seen maybe 20 percent.
    19|>
    20|> The other 80 percent — the techniques that turn Claude Code from "useful assistant" into "the most productive I have ever been" — are buried in documentation, discovered through experimentation, or shared in small communities.
    21|>
    22|> I compiled every technique that moved the needle for me. Tested daily. Zero theory.
    23|
    24|---
    25|
    26|## Essential Commands (01 to 08)
    27|
    28|**01. Plan Mode (Shift + Tab)**  
    29|Before any implementation, switch to plan mode. Claude Code analyzes your codebase and creates an architecture plan WITHOUT writing any code. Review the plan. Approve it. Then switch back to implementation. This single habit prevents more bugs than any other technique on this list.
    30|
    31|**02. Compact (/compact)**  
    32|After 30 to 45 minutes of conversation, your context gets bloated. Type `/compact` to compress the entire conversation history into a focused summary of key decisions and current state. Claude Code stays sharp instead of gradually losing track of what you discussed.
    33|
    34|**03. Clear (/clear)**  
    35|Starting a new task? Clear the slate entirely. Carrying context from a database refactor into a frontend redesign produces confused, conflicting code. One conversation per feature. Always.
    36|
    37|**04. Init (/init)**  
    38|Run this at the start of any new project. Claude Code scans your codebase and generates a `CLAUDE.md` file — a persistent context document that it reads automatically in every future session. Includes project structure, tech stack, coding patterns, and key architecture decisions.
    39|
    40|**05. The Cost Check (/cost)**  
    41|Displays your token usage for the current session. Check this every hour during long sessions. AI-assisted development costs money and surprises are never fun. Set a mental budget per session and check against it.
    42|
    43|**06. Memory (/memory)**  
    44|Add persistent instructions that Claude Code remembers across all sessions. "Always use TypeScript strict mode." "Always add JSDoc comments to public functions." "Always run tests after modifying any file in /src/core." These rules apply automatically in every future conversation without repeating them.
    45|
    46|**07. Terminal Integration (! prefix)**  
    47|Prefix any message with `!` to run it as a terminal command instead of sending it to Claude. Quick way to run tests, check git status, or navigate directories without leaving the Claude Code interface.
    48|
    49|**08. Multi-Model Switching**  
    50|Use Opus for planning and architecture decisions. Switch to Sonnet for implementation and execution. Opus thinks deeper but costs more. Sonnet executes faster and cheaper. Plan with the thinker. Build with the builder.
    51|
    52|---
    53|
    54|## Productivity Techniques (09 to 18)
    55|
    56|**09. The Reference File Technique**  
    57|Instead of describing the code style you want, point to an existing file: "Look at how authentication is implemented in `src/auth/login.ts`. Implement password reset following the exact same patterns." Claude Code reads the reference and replicates the patterns precisely.
    58|
    59|**10. The Screenshot Debug**  
    60|Something looks wrong in the UI? Do not write a paragraph. Screenshot it. Paste with Ctrl+V. Say: "The button is misaligned with the input field. The spacing between cards is inconsistent. Fix both." Visual feedback is faster and more accurate than written descriptions.
    61|
    62|**11. The Test-First Workflow**  
    63|"Write tests for a function that calculates discounted prices. Cover: normal discounts, zero discount, 100 percent discount, negative prices, and string inputs. Then implement the function to pass all tests." Tests define behavior before code exists.
    64|
    65|**12. The Incremental Build**  
    66|Never say "build the entire feature." Break it into steps: "Create the database schema." Test. "Build the API endpoint." Test. "Add validation." Test. "Build the frontend form." Test. Five small steps with testing between each one produces dramatically better code.
    67|
    68|**13. The Codebase Question**  
    69|Before implementing anything in an unfamiliar part of the codebase: "Read `src/services/` and explain how data flows from the API routes to the database. What patterns are used? What should I know before modifying anything here?"
    70|
    71|**14. The Diff Review**  
    72|After Claude Code makes changes: "Show me a diff of every file you modified. Explain each change in one sentence." This catches unintended modifications.
    73|
    74|**15. The Error Paste**  
    75|When something breaks, copy the COMPLETE error message and stack trace. Not a summary. "I got this error: [paste full error]. Diagnose the root cause step by step before suggesting a fix."
    76|
    77|**16. The Undo Checkpoint**  
    78|Before every major change: `git add . && git commit -m "checkpoint before [change]"`. If Claude Code breaks something, you revert in seconds instead of spending thirty minutes debugging.
    79|
    80|**17. The Parallel Session**  
    81|For large features, open two terminal windows. One runs Claude Code for the backend. The other for the frontend. Each session has clean, focused context. Connect the pieces at the end.
    82|
    83|**18. The Documentation Pass**  
    84|After completing a feature: "Read every file you created or modified for this feature. Generate comprehensive documentation..." Documentation generated immediately after building is more accurate than written days later from memory.
    85|
    86|---
    87|
    88|## Architecture Techniques (19 to 26)
    89|
    90|**19. The Architecture Audit**  
    91|"Analyze my project requirements: [list them]. Propose 2 different architectural approaches. For each: component diagram, pros, cons, estimated complexity, and what could go wrong. Recommend one with clear reasoning."
    92|
    93|**20. The Dependency Check**  
    94|Before adding any new package: "I want to add [package] to handle [use case]. Check: is this actively maintained? Are there known security issues? What is the bundle size impact? Are there lighter alternatives?"
    95|
    96|**21. The Pattern Enforcer**  
    97|Add to your `CLAUDE.md`: "When creating new files, follow these patterns: API routes follow the structure in `src/api/example-route.ts`. Database queries use the repository pattern in `src/repositories/example-repo.ts`. React components follow the structure in `src/components/ExampleComponent.tsx`."
    98|
    99|**22. The Migration Builder**  
   100|"I need to change the user table schema: add a 'role' column... Generate the migration file, update the repository layer, update all API routes that reference the old schema, and update the TypeScript types. Show me every file that needs to change before making any modifications."
   101|
   102|**23. The API Design Review**  
   103|"Review my API design: [paste route definitions]. Check for: inconsistent naming, missing error responses, endpoints that should be paginated, missing authentication on protected routes, and any REST convention violations."
   104|
   105|**24. The Security Scan**  
   106|"Scan this codebase for security vulnerabilities: SQL injection, XSS, exposed secrets in code or config files, missing input validation, insecure direct object references, and missing rate limiting. For each finding: severity, exact location, why it is dangerous, and the fix."
   107|
   108|**25. The Performance Profiler**  
   109|"Analyze this codebase for performance issues: N+1 database queries, missing indexes based on query patterns, unnecessary re-renders in React components, large bundle imports that could be lazy loaded, and API endpoints that should be cached. Prioritize by estimated impact."
   110|
   111|**26. The Refactoring Planner**  
   112|"Read `src/services/user-service.ts`. This file has grown to 800 lines and handles too many responsibilities. Propose a refactoring plan that splits it into focused modules. Show the proposed file structure, what moves where, and verify that no external imports will break. Do NOT start refactoring yet — just show me the plan."
   113|
   114|---
   115|
   116|## Workflow Automation (27 to 31)
   117|
   118|**27. The Git Hook Writer**  
   119|"Create a pre-commit hook that: runs the linter on staged files, runs type checking, checks for console.log statements in production code, and blocks commits that fail any check. Install it in `.husky/pre-commit`."
   120|
   121|**28. The CI Pipeline Builder**  
   122|"Create a GitHub Actions workflow that: runs on every PR, installs dependencies, runs the full test suite, runs the linter, builds the project, and posts a comment on the PR with the results. Use caching for `node_modules`."
   123|
   124|**29. The Environment Setup Script**  
   125|"Create a `setup.sh` script that a new developer runs once to set up the entire development environment: install dependencies, create `.env` from `.env.example`, set up the local database, run migrations, seed test data, and verify everything works by running the test suite."
   126|
   127|**30. The Release Notes Generator**  
   128|"Read the git log since the last tag. Generate release notes organized by: new features, bug fixes, performance improvements, and breaking changes. Write each entry in user-friendly language, not developer jargon."
   129|
   130|**31. The Database Seed Builder**  
   131|"Create a comprehensive seed file for the development database. Include: 5 users (1 admin, 2 editors, 2 viewers), 20 sample projects with realistic data, relationships between entities, and edge cases... Make the data realistic, not 'test123'."
   132|
   133|---
   134|
   135|## Debug and Recovery (32 to 35)
   136|
   137|**32. The Reproduction Prompt**  
   138|"This bug was reported by a user: [paste bug report]. Create a minimal reproduction: the exact steps, the expected behavior, the actual behavior. Then write a failing test that captures this bug. Then fix the code to make the test pass."
   139|
   140|**33. The Blame Investigator**  
   141|"This function started failing yesterday. Read the git log for this file over the past week. Identify which commit likely introduced the issue and explain what changed. Then suggest the fix."
   142|
   143|**34. The Dependency Conflict Resolver**  
   144|"I am getting this dependency conflict: [paste error]. Analyze the conflict. Identify which packages require conflicting versions of the shared dependency. Suggest the resolution that requires the fewest changes and explain the tradeoffs."
   145|
   146|**35. The Recovery Mode**  
   147|When Claude Code produces a broken implementation and you have been going back and forth for too long: "Stop. Read the original working version of this file from git: [paste the git show command output]. Now look at what we have been trying to achieve: [restate the goal simply]. Start fresh with a different approach. The previous approach clearly is not working."
   148|
   149|---
   150|
   151|## The Setup That Ties It All Together
   152|
   153|When you start a new project, run this sequence:
   154|1. `/init` — generate the `CLAUDE.md` file
   155|2. Add your coding standards and patterns to `CLAUDE.md`
   156|3. `/memory` — add persistent rules you want in every session
   157|4. **Plan mode** — design the architecture before writing any code
   158|5. **Start building incrementally** — one feature at a time, tested at each step
   159|
   160|> This five-minute setup transforms every subsequent hour of development.
   161|
   162|---
   163|
   164|## TL;DR
   165|
   166|35 techniques. Tested daily. Each one solves a real development problem.
   167|- Essential commands for session management
   168|- Productivity techniques for faster building
   169|- Architecture techniques for better design
   170|- Workflow automation for consistent quality
   171|- Debug and recovery for when things break
   172|
   173|Claude Code is the most powerful development tool available. These 35 techniques unlock all of it.
   174|