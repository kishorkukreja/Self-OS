---
title: "Memory Intelligence Agent"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Deep research agent framework using Manager-Planner-Executor architecture with alternating RL, test-time learning, and bidirectional parametric/non-parametric memory evolution."
tags: [deep-research-agents, memory-system, reinforcement-learning, test-time-learning, parametric-memory]
type: source
status: final
---

# Memory Intelligence Agent

**Type:** paper
**Date:** 2026-04-13
**URL:** https://arxiv.org/abs/2604.04503
**Authors:** Jingyang Qiao, Weicheng Meng, Yu Cheng, Zhihang Lin, Zhizhong Zhang, Xin Tan, Jingyu Gong, Kun Shao, Yuan Xie
**Raw file:** [[../../raw/papers/2026-04-13-qiao-memory-intelligence-agent.md]]

**Summary:** Qiao et al. propose the **Memory Intelligence Agent (MIA)**, a framework for deep research agents that addresses limitations of long-context memory systems. MIA uses a **Manager-Planner-Executor** architecture: the Memory Manager stores compressed historical trajectories as non-parametric memory; the Planner is a parametric memory agent producing search plans; and the Executor carries out guided information retrieval. A two-stage alternating RL paradigm (GRPO-based) trains the Executor to follow plans and the Planner to generate better plans using memory context. Crucially, the Planner evolves continuously during test-time learning without interrupting inference, and a bidirectional conversion loop between parametric and non-parametric memories enables efficient memory evolution. Reflection and unsupervised judgment mechanisms support open-world self-evolution. Experiments show MIA boosts GPT-5.4 by up to 9% on LiveVQA and 6% on HotpotQA, while a lightweight Qwen2.5-VL-7B Executor achieves 31% average improvement across datasets, outperforming Qwen2.5-VL-32B by 18%.

**Key contributions:**
- Manager-Planner-Executor architecture decoupling historic memory, parametric planning, and dynamic execution
- Alternating GRPO training aligning Planner and Executor strategies
- Continual test-time learning allowing Planner parametric updates during inference
- Bidirectional parametric/non-parametric memory conversion loop
- Reflection and unsupervised judgment for autonomous self-evolution

**Tags:** deep-research-agents, memory-system, reinforcement-learning, test-time-learning, parametric-memory
