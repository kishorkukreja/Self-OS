---
title: "Thread by @yoonholeee"
source: "https://x.com/yoonholeee/status/2038640635482456118"
author:
  - "[[@yoonholeee]]"
published: 2026-03-30
created: 2026-04-12
description: "How can we autonomously improve LLM harnesses on problems humans are actively working on? Doing so requires solving a hard, long-horizon cr"
status: processed
tags:
  - "clippings"
---
**Yoonho Lee** @yoonholeee [2026-03-30](https://x.com/yoonholeee/status/2038640635482456118)

How can we autonomously improve LLM harnesses on problems humans are actively working on?

Doing so requires solving a hard, long-horizon credit-assignment problem over all prior code, traces, and scores.

Announcing Meta-Harness: a method for optimizing harnesses end-to-end

![Image](https://pbs.twimg.com/media/HEq02pQakAERs85?format=jpg&name=large)

---

**Yoonho Lee** @yoonholeee [2026-03-30](https://x.com/yoonholeee/status/2038640660815937856)

The key idea is simple:

\- Use a coding agent as the proposer

\- Give it filesystem access to the full history of prior experience (this directory gets very big)

Our iterative loop lets the agent try different ideas while selectively inspecting a very long raw history.

![Image](https://pbs.twimg.com/media/HEq029taEAEKQxo?format=jpg&name=large)

---

**Yoonho Lee** @yoonholeee [2026-03-30](https://x.com/yoonholeee/status/2038640665647837451)

We find that unrestricted access to all previous history is essential in our settings, because the dependencies are so long-horizon.

Previous text optimization loops that only see rewards/summaries/previous attempts discard important information and underperform here.

![Image](https://pbs.twimg.com/media/HEq04bAbUAAwQhT?format=jpg&name=large)

---

**Yoonho Lee** @yoonholeee [2026-03-30](https://x.com/yoonholeee/status/2038640670714581375)

We make progress on optimizing harnesses for TerminalBench-2.

The proposer, after reading dozens of files (82 median), reasons through why its previous attempts failed to form a targeted hypothesis. It's surprisingly similar to how a human engineer might approach this problem

![Image](https://pbs.twimg.com/media/HEq04soasAAyafg?format=png&name=large)

---

**Yoonho Lee** @yoonholeee [2026-03-30](https://x.com/yoonholeee/status/2038640672950173943)

Meta-Harness is itself a harness: one whose purpose is to optimize other harnesses.

It's a new instantiation of classic meta-learning ideas, with even less imposed structure:

1\. Let an agent inspect any part of prior attempts

2\. Give it a good hill to climb

---

**Yoonho Lee** @yoonholeee [2026-03-31](https://x.com/yoonholeee/status/2038823887816057300)

With amazing collaborators @roshen\_nair @qizhengz\_alex @Kangwook\_Lee @lateinteraction @chelseabfinn

Project page w/ interactive demo: https://yoonholee.com/meta-harness/

Paper: https://arxiv.org/abs/2603.28052

---

**Viv** @Vtrivedy10 [2026-03-30](https://x.com/Vtrivedy10/status/2038663045002477604)

awesome work!! how do you guys think about “overfitting to the hill”? hold out set? guidelines + manual inspection?

love this flavor and have found success with it on tb2 as well at langchain

there’s some fun tradeoffs between generalization vs “let me just rock at this task”