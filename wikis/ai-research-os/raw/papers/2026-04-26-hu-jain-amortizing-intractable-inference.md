---
status: processed
---
     1|---
     2|source: https://arxiv.org/abs/2310.04363
     3|date: 2026-04-26
     4|type: paper
     5|tags: [gflownets, bayesian-inference, llm-fine-tuning, chain-of-thought, latent-variable, iclr-2024]
     6|---
     7|
     8|# Amortizing intractable inference in large language models
     9|
    10|**arXiv:** [2310.04363](https://arxiv.org/abs/2310.04363) [cs.LG, cs.CL] · **ICLR 2024** · 23 pages  
    11|**Authors:** Edward J. Hu, Moksh Jain, Eric Elmoznino, Younesse Kaddar, Guillaume Lajoie, Yoshua Bengio, Nikolay Malkin
    12|
    13|---
    14|
    15|## Abstract
    16|
    17|> Autoregressive large language models (LLMs) compress knowledge from their training data through next-token conditional distributions. This limits tractable querying of this knowledge to start-to-end autoregressive sampling. However, many tasks of interest -- including sequence continuation, infilling, and other forms of constrained generation -- involve sampling from intractable posterior distributions. We address this limitation by using amortized Bayesian inference to sample from these intractable posteriors. Such amortization is algorithmically achieved by fine-tuning LLMs via diversity-seeking reinforcement learning algorithms: generative flow networks (GFlowNets). We empirically demonstrate that this distribution-matching paradigm of LLM fine-tuning can serve as an effective alternative to maximum-likelihood training and reward-maximizing policy optimization. As an important application, we interpret chain-of-thought reasoning as a latent variable modeling problem and demonstrate that our approach enables data-efficient adaptation of LLMs to tasks that require multi-step rationalization and tool use.
    18|
    19|---
    20|
    21|## Key Contributions
    22|
    23|- **Problem identified:** Standard autoregressive LLMs only permit tractable start-to-end sampling. Many useful tasks (infilling, continuation, constrained generation) require sampling from *intractable* posteriors.
    24|- **Core method:** Apply **amortized Bayesian inference** to sample from these posteriors by fine-tuning LLMs with **GFlowNets** — diversity-seeking reinforcement learning algorithms.
    25|- **Training paradigm:** Proposes a **distribution-matching** approach to LLM fine-tuning as an alternative to both maximum-likelihood training and reward-maximizing policy optimization (e.g., RLHF/PPO-style methods).
    26|- **Application:** Frames **chain-of-thought reasoning** as a latent variable modeling problem, showing the method enables **data-efficient adaptation** for multi-step rationalization and tool use.
    27|
    28|---
    29|
    30|## Access & Resources
    31|
    32|| Resource | Link |
    33||----------|------|
    34|| **PDF** | [https://arxiv.org/pdf/2310.04363](https://arxiv.org/pdf/2310.04363) |
    35|| **HTML** | [https://arxiv.org/html/2310.04363v2](https://arxiv.org/html/2310.04363v2) |
    36|| **Code** | [https://github.com/GFNOrg/gfn-lm-tuning](https://github.com/GFNOrg/gfn-lm-tuning) |
    37|
    38|- **License:** CC BY 4.0
    39|- **Subjects:** Machine Learning (cs.LG); Computation and Language (cs.CL)
    40|