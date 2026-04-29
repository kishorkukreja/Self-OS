---
status: processed
---
# Prompt Master

**URL:** https://github.com/nidhinjs/prompt-master  
**License:** MIT  
**Stars:** 6.4k | **Forks:** 679 | **Watchers:** 126 | **Commits:** 46 | **Contributors:** 4  
**Latest Version:** 1.6.0 (updated Apr 28, 2026)

## Overview

> A Claude skill that writes accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention.

Eliminates the expensive cycle of vague prompt → wrong output → re-prompt → re-prompt again.

> **"The best prompt is not the longest. It's the one where every word is load-bearing."**

Most generators make prompts longer. This skill makes them **sharper**.

## Installation

### Recommended: Claude.ai (Browser)
1. Download this repo as a ZIP
2. Go to **claude.ai → Sidebar → Customize → Skills → Upload a Skill**

### Alternative: Claude Code (Not Suggested)
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master
```

## Usage

Invoke naturally in Claude:
```
Write me a prompt for Cursor to refactor my auth module
```
```
I need a prompt for Claude Code to build a REST API — ask me what you need to know
```
```
Here's a bad prompt I wrote for GPT-4o, fix it: [paste prompt]
```
```
Generate a Midjourney prompt for a cyberpunk city at night
```

Or explicitly invoke:
```
/prompt-master
I want to ask Claude Code to build a todo app with React and Supabase
```

## How It Works (7-Step Pipeline)

1. **Detects target tool** — silent routing to the correct approach
2. **Extracts 9 dimensions of intent** — task, input, output, constraints, context, audience, memory, success criteria, examples
3. **Asks targeted clarifying questions** — max 3 if critical info is missing
4. **Routes to the right framework** — auto-selected architecture (never shown to user)
5. **Applies safe techniques only** — role assignment, few-shot, XML structure, grounding anchors, memory block
6. **Runs a token efficiency audit** — strips non-load-bearing words
7. **Delivers the prompt** — one clean copyable block + one-line strategy note

## Example Output

### Midjourney Prompt
**Input:** `Write me a midjourney prompt for a realistic samurai standing in the rain at night`

**Generated:**
```
lone samurai standing in heavy rain at night, traditional armor,
neon reflections on wet cobblestone street, cinematic lighting,
dramatic shadows, fog, ultra detailed, photorealistic,
shallow depth of field --ar 16:9 --v 6 --style raw

negative: blurry, low quality, watermark, cartoon, anime, extra limbs
```
**Meta:** 🎯 Midjourney · ⚡ Visual Descriptor · 💰 Light (~60 tokens) · 💡 Strategy: Comma-separated descriptors over prose; lighting/mood anchored early; aspect ratio/version locked; negative prompt prevents style drift.

### Claude Code Prompt (Notion-Style Landing Page)
**Input:** `Build a claude code prompt for a landing page for a business dashboard that looks and feels exactly like notion`

**Generated:** Detailed single-file HTML/CSS/JS spec with exact color codes, spacing units, border radii, 8 sections with specific copy, and animation requirements.

## Why It Matters

Unlike generic prompt generators that just make prompts longer, Prompt Master applies a structured 7-step pipeline to produce **engineered prompts** that are tool-aware, intent-calibrated, and token-efficient. The skill format means it integrates directly into Claude's skill system with persistent memory of your preferences.

## Tags

- prompt-engineering
- claude-skill
- prompt-generator
- token-efficiency
- ai-workflow
- typescript
