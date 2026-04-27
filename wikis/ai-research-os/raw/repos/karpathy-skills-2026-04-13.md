---
status: processed
---
     1|---
     2|source: https://github.com/forrestchang/andrej-karpathy-skills
     3|date: 2026-04-13
     4|type: repo
     5|tags: [claude-code, claude-md, coding-guidelines, karpathy, llm-pitfalls, simplicity]
     6|status: raw
     7|---
     8|
     9|# Karpathy-Inspired Claude Code Guidelines
    10|
    11|A single `CLAUDE.md` file to improve Claude Code behavior, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls.
    12|
    13|## The Problems
    14|
    15|From Andrej's post:
    16|
    17|> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should."
    18|
    19|> "They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code... implement a bloated construction over 1000 lines when 100 would do."
    20|
    21|> "They still sometimes change/remove comments and code they don't sufficiently understand as side effects, even if orthogonal to the task."
    22|
    23|## The Solution
    24|
    25|Four principles in one file that directly address these issues:
    26|
    27|| Principle | Addresses |
    28||-----------|-----------|
    29|| **Think Before Coding** | Wrong assumptions, hidden confusion, missing tradeoffs |
    30|| **Simplicity First** | Overcomplication, bloated abstractions |
    31|| **Surgical Changes** | Orthogonal edits, touching code you shouldn't |
    32|| **Goal-Driven Execution** | Leverage through tests-first, verifiable success criteria |
    33|
    34|## The Four Principles in Detail
    35|
    36|### 1. Think Before Coding
    37|
    38|**Don't assume. Don't hide confusion. Surface tradeoffs.**
    39|
    40|LLMs often pick an interpretation silently and run with it. This principle forces explicit reasoning:
    41|
    42|- **State assumptions explicitly** � If uncertain, ask rather than guess
    43|- **Present multiple interpretations** � Don't pick silently when ambiguity exists
    44|- **Push back when warranted** � If a simpler approach exists, say so
    45|- **Stop when confused** � Name what's unclear and ask for clarification
    46|
    47|### 2. Simplicity First
    48|
    49|**Minimum code that solves the problem. Nothing speculative.**
    50|
    51|Combat the tendency toward overengineering:
    52|
    53|- No features beyond what was asked
    54|- No abstractions for single-use code
    55|- No "flexibility" or "configurability" that wasn't requested
    56|- No error handling for impossible scenarios
    57|- If 200 lines could be 50, rewrite it
    58|
    59|**The test:** Would a senior engineer say this is overcomplicated? If yes, simplify.
    60|
    61|### 3. Surgical Changes
    62|
    63|**Touch only what you must. Clean up only your own mess.**
    64|
    65|When editing existing code:
    66|
    67|- Don't "improve" adjacent code, comments, or formatting
    68|- Don't refactor things that aren't broken
    69|- Match existing style, even if you'd do it differently
    70|- If you notice unrelated dead code, mention it � don't delete it
    71|
    72|When your changes create orphans:
    73|
    74|- Remove imports/variables/functions that YOUR changes made unused
    75|- Don't remove pre-existing dead code unless asked
    76|
    77|**The test:** Every changed line should trace directly to the user's request.
    78|
    79|### 4. Goal-Driven Execution
    80|
    81|**Define success criteria. Loop until verified.**
    82|
    83|Transform imperative tasks into verifiable goals:
    84|
    85|| Instead of... | Transform to... |
    86||--------------|-----------------|
    87|| "Add validation" | "Write tests for invalid inputs, then make them pass" |
    88|| "Fix the bug" | "Write a test that reproduces it, then make it pass" |
    89|| "Refactor X" | "Ensure tests pass before and after" |
    90|
    91|For multi-step tasks, state a brief plan:
    92|
    93|```
    94|1. [Step] ? verify: [check]
    95|2. [Step] ? verify: [check]
    96|3. [Step] ? verify: [check]
    97|```
    98|
    99|Strong success criteria let the LLM loop independently. Weak criteria ("make it work") require constant clarification.
   100|
   101|## Install
   102|
   103|**Option A: Claude Code Plugin (recommended)**
   104|
   105|From within Claude Code, first add the marketplace:
   106|```
   107|/plugin marketplace add forrestchang/andrej-karpathy-skills
   108|```
   109|
   110|Then install the plugin:
   111|```
   112|/plugin install andrej-karpathy-skills@karpathy-skills
   113|```
   114|
   115|This installs the guidelines as a Claude Code plugin, making the skill available across all your projects.
   116|
   117|**Option B: CLAUDE.md (per-project)**
   118|
   119|New project:
   120|```bash
   121|curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
   122|```
   123|
   124|Existing project (append):
   125|```bash
   126|echo "" >> CLAUDE.md
   127|curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
   128|```
   129|
   130|## Key Insight
   131|
   132|From Andrej:
   133|
   134|> "LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go."
   135|
   136|The "Goal-Driven Execution" principle captures this: transform imperative instructions into declarative goals with verification loops.
   137|
   138|## How to Know It's Working
   139|
   140|These guidelines are working if you see:
   141|
   142|- **Fewer unnecessary changes in diffs** � Only requested changes appear
   143|- **Fewer rewrites due to overcomplication** � Code is simple the first time
   144|- **Clarifying questions come before implementation** � Not after mistakes
   145|- **Clean, minimal PRs** � No drive-by refactoring or "improvements"
   146|
   147|## Customization
   148|
   149|These guidelines are designed to be merged with project-specific instructions. Add them to your existing `CLAUDE.md` or create a new one.
   150|
   151|For project-specific rules, add sections like:
   152|
   153|```markdown
   154|## Project-Specific Guidelines
   155|
   156|- Use TypeScript strict mode
   157|- All API endpoints must have tests
   158|- Follow the existing error handling patterns in `src/utils/errors.ts`
   159|```
   160|
   161|## Tradeoff Note
   162|
   163|These guidelines bias toward **caution over speed**. For trivial tasks (simple typo fixes, obvious one-liners), use judgment � not every change needs the full rigor.
   164|
   165|The goal is reducing costly mistakes on non-trivial work, not slowing down simple tasks.
   166|
   167|## License
   168|
   169|MIT
   170|
   171|