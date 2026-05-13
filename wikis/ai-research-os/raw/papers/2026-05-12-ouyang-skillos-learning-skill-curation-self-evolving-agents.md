---
source: https://arxiv.org/html/2605.06614v1
date: 2026-05-12
type: paper
tags: [skillos, skills, skill-curation, self-evolving-agents, reinforcement-learning, agent-memory, procedural-memory, markdown-skills]
status: processed
---

# SkillOS: Learning Skill Curation for Self-Evolving Agents

## Summary
SkillOS is an RL-based framework for training LLM agents to curate reusable skills from prior task experience. It separates the system into a frozen Agent Executor, a trainable Skill Curator, and an external Markdown-based SkillRepo. The curator learns to insert, update, and delete skills based on downstream task outcomes over grouped task streams, rather than relying on manual rules or direct human labels. The paper reports gains across ALFWorld, WebShop, AIME24, AIME25, and GPQA-Diamond, with generalization across executor backbones including Qwen and Gemini models.

## Paper metadata
- Title: SkillOS: Learning Skill Curation for Self-Evolving Agents
- arXiv: 2605.06614v1
- Category: cs.AI
- Date: 7 May 2026
- Authors: Siru Ouyang, Jun Yan, Yanfei Chen, Rujun Han, Zifeng Wang, Bhavana Dalvi Mishra, Rui Meng, Chun-Liang Li, Yizhu Jiao, Kaiwen Zha, Maohao Shen, Vishy Tirumalashetty, George Lee, Jiawei Han, Tomas Pfister, Chen-Yu Lee
- Affiliations noted in extraction: Google Cloud AI Research, UIUC, MIT

## Key points
- SkillOS treats skill curation as a long-horizon learning problem, not a prompt-engineering or manual-memory problem.
- The executor is frozen; the skill curator is trained to edit the external SkillRepo.
- Skills are represented as Markdown files with YAML frontmatter and reusable procedural instructions, close to Anthropic-style `SKILL.md` conventions.
- The curator can call three repository operations: `insert_skill`, `update_skill`, and `delete_skill`.
- Training uses grouped task streams: early related tasks generate/modify skills; later tasks evaluate whether those skills improve executor performance.
- Rewards combine downstream task success with valid function-call behavior, skill content quality, and repository compactness/compression.
- The paper emphasizes atomic, modular, reusable skills that avoid problem-specific IDs/details and do not hallucinate facts.

## Why it matters
This is directly relevant to Hermes because Hermes already uses a persistent skill library and has a human-operated version of the same loop: create skills after successful complex workflows, patch skills when they are wrong or stale, and keep procedural memory separate from raw conversation logs. SkillOS provides a research framing for turning that into a measurable self-improvement loop: skill changes should be rewarded by downstream task success, not by how plausible the skill looks.

## Self-OS implications
- Strong candidate concept for `skill-curation` / `self-evolving-agents` in `ai-research-os`.
- Hermes skill maintenance could adopt a light version of SkillOS reward design:
  - Did the skill improve task success on future similar tasks?
  - Was the skill valid and executable?
  - Did it remain compact and general rather than bloated with stale session details?
- The paper supports the existing memory rule: durable procedures belong in skills; temporary outcomes belong in session history or raw notes.
- This also connects to GBrain/OpenClaw/GStack-style “skillify” loops, where a repeated manual workflow becomes a reusable skill and then gets refined after failures.

## Raw content notes
The extracted paper frames the system as a closed loop:
1. Retrieve relevant skills from SkillRepo.
2. Frozen executor solves the incoming task using retrieved skills.
3. Curator observes the task trajectory, correctness signal, and related skills.
4. Curator emits structured edit operations: insert, update, delete.
5. SkillRepo updates and is reused for future tasks.

The paper's skill-format guidance says skills should be atomic, modular, reusable, general, and free of problem-specific details. The curator prompt includes principles such as “No Specifics” and “No Hallucination.”
