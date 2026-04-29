---
url: https://x.com/aiedge_/status/2046966170868486512
author: AI Edge (@aiedge_)
saved: 2026-04-27
views: 1.86M
likes: 1.8K
bookmarks: 8.7K
status: processed
---
# How to Give Claude Perfect Memory (Complete Guide)

> "I don't care what anyone tells you — by default, Claude's memory is basically useless. It frequently forgets context; you constantly have to re-explain yourself, and even after you do, it still often doesn't remember."

Three layers of memory systems, from beginner to advanced:

---

## Layer One: Basic Memory (Beginner)

Four quick wins that take minutes to set up and immediately improve every conversation.

### 1. Memory Editing Tool
Go to **Settings → Memory**. This is the most overlooked page in Claude.

What you'll find: everything Claude has stored about you (preferences, facts, habits, working styles) accumulated passively across every conversation.

**The fix:** read through everything. Delete outdated, inaccurate, or irrelevant entries. Manually add the context you actually want Claude to carry permanently. Stick to basics (your role and basic preferences).

### 2. Project Instructions
If you use Claude Projects (you should), fill in your **Project Instructions** field.

Advice: Create projects for all your most-used workflows, then voice-prompt all your context into a Google Doc and upload it as a PDF for each project.

### 3. Tell Claude Directly
The simplest memory hack. Mid-conversation, just tell Claude what to remember:
- "Remember that I never want [x]"
- "Remember that my role is [x]"
- "Update your memory with [x]"
- "Remember that I prefer responses under 400 words."

Claude stores these immediately. You can also say: "Forget that I mentioned [x]."

### 4. Memory Imports & Exports
If you've built up context in ChatGPT or another LLM, you don't have to start from scratch:
- Ask ChatGPT to generate a memory export document: "I'm switching this project to Claude, give me a summary document..."
- Use **Settings → Memory → Import/Export** in Claude

These four edits suffice for 90%+ of users and make an immediate impact.

---

## Layer Two: Context File System (Intermediate)

Build a file-based memory architecture that lives on your computer and loads automatically into Cowork and Claude Code.

**Concept:** Instead of prompting Claude for context, store all context in `.md` desktop files that Claude has access to. You can also attach these markdown files to any LLM or AI agent system.

### Setup

Create a new desktop folder called **"Claude Master Folder"** and build these four markdown files inside it:

#### 1. Instructions.md
Tells Claude all your rules & instructions:
- Who you are
- What you do
- Rules
- What good outputs look like

**Crucial line to include:** "Update Memory.md with my preferences over time."

#### 2. Memory.md
The "brain" of Claude. Gets continuously updated over time.
- Preferences
- Corrections
- Patterns
- Decisions

Whenever you say something like "stop using em dashes," Claude goes into the memory file and updates it.

#### 3. Context.md
The specific context file for [x] project. What's in here changes depending on your specific project.

You can also create a general "business context" or "life context" markdown mega file.

#### 4. Archive Copies
Protective backup system. Claude updates memory files automatically as you work. Occasionally it overwrites something incorrectly.

**Fix:** Once a week, copy your entire master folder into a separate archive folder that Claude cannot access, and label it with the date. Restore from archive if anything breaks.

### Quick-Start Prompt

Paste this into a new Cowork chat with your Master Folder attached:

```
Go into my "Claude Master Folder" in my connected workspace and build these four markdown files inside it:

Instructions.md — includes sections for: Who You Are, What You Do, Rules, What Good Outputs Look Like, and a line telling Claude to update Memory.md with my preferences over time.

Memory.md — includes sections for: Preferences, Corrections, Patterns, Decisions, and Personal Context. Pre-fill with placeholder examples so I know what to add.

Context.md — includes sections for: About This Project/Business, Audience, Key People & Collaborators, Active Projects & Priorities, Tools & Stack, and Important Background/History. Use a template format with placeholders I can fill in.

Archive-Guide.md — a step-by-step guide explaining why to archive, how to do it weekly (duplicate the folder, rename with the date, move it somewhere Claude can't access), what to include, how to restore if something breaks, and where to store the backups.
```

### Usage
Anytime you're working in Cowork/Claude Code, attach your Master Folder and Claude will use it as a mini memory database. It will edit the memory markdown file, leaving you with something you can attach to any LLM, new chat, or AI agent.

---

## Layer Three: AI Second Brain (Advanced)

The deepest level. Requires initial setup and ongoing maintenance, but is the best option for an advanced, detailed memory system.

### Option 1: Claude x Notion (Easier)
Connecting Claude to Notion is the highest-leverage thing you can do in 5 minutes.

1. Go to **Claude → Settings → Connectors**, then enable the Notion connector
2. Claude can now read your Notion workspace directly inside any chat
3. Create a new **"Memory Database"** where you store all your AI preferences, rules, and important AI context
4. As you're working with Claude, say: "Send this to my Notion Memory Database."
5. Export Notion data to other LLMs or AI platforms via CSV or the Notion MCP connector

Notion = fast, simple option with nice visuals (board views, to-do lists).

### Option 2: Claude x Obsidian (Most Advanced)
Obsidian stores everything as plain Markdown files on your computer, making it a solid way to connect with Claude and build a second brain.

#### The Setup
1. **Download Obsidian** at obsidian.md
2. **Create a new Vault** (a simple desktop folder where Claude Code will store and access your data)
3. **Select Vault in Claude Cowork/Claude Code** — open the Claude desktop app, click "Select Folder," point it at your Obsidian Vault folder. Claude now has direct read and write access to everything inside it.
4. **Inject mega prompt** — paste Andrej Karpathy's LLM Knowledge Base system prompt into the chatbox. This tells Claude Code how to build, maintain, and evolve your wiki over time.
   - Prompt available at: gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
5. **Feed it your data** — drop in any existing notes, CSV files, article exports, or Notion exports to start populating your second brain. Claude ingests each source, extracts key information, and integrates it into an evolving memory wiki.

**Final product:** an AI second brain knowledge wiki that links ideas, notes, remembers ALL your data.

Obsidian = local storage, and you want Claude to have a deep understanding. This is the most advanced memory system the author has personally found.

For more details on the Claude x Obsidian setup, see: https://x.com/aiedge_/status/1909174500000000000 (Claude Code + Obsidian Ultimate Guide)

---

## Summary

| Layer | Level | Effort | Best For |
|-------|-------|--------|----------|
| 1 | Basic Memory | Minutes | 90%+ of users. Immediate impact. |
| 2 | Context File System | ~60 min setup | Power users who want file-based persistent memory across chats |
| 3a | Claude x Notion | 5 min | Fast, visual option with database features |
| 3b | Claude x Obsidian | 1–2 hours | Most advanced. Local, deep understanding, self-evolving wiki |

## Why It Matters

This is the most comprehensive public guide to building persistent, multi-layered memory for Claude. It bridges simple built-in features (Memory editing, Project Instructions) through intermediate file-based systems (Context File System) to advanced integrations (Notion/Obsidian second brains). The Karpathy LLM Knowledge Base prompt integration for Obsidian is particularly notable as a concrete implementation of the "self-evolving wiki" concept.

## Related

- Karpathy's LLM Wiki: gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- WUPHF: multi-agent office with shared wiki memory
- Autogenesis: self-evolving agent protocol with persistent memory
- Hermes Agent: persistent memory and skills system
