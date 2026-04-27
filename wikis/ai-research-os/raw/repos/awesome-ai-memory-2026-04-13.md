---
status: processed
---
     1|---
     2|source: https://github.com/IAAR-Shanghai/Awesome-AI-Memory
     3|date: 2026-04-13
     4|type: repo
     5|tags: [agent-memory, awesome-list, survey, long-term-memory, retrieval, memory-native]
     6|status: raw
     7|---
     8|
     9|# Awesome-AI-Memory
    10|
    11|<p align="center">
    12|    ?English | <a href="README_cn.md">??</a></a>?
    13|</p>
    14|
    15|<div align="center">
    16|    <img src="assets/Gemini_Generated_Image_hretabhretabhret.png" alt="Survey Framework" width="82%">
    17|</div>
    18|
    19|[![Awesome](https://awesome.re/badge.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)
    20|[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
    21|![](https://img.shields.io/badge/PRs-Welcome-red)
    22|[![Papers](https://img.shields.io/badge/Papers-303-blue.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/papers)
    23|[![Open Source Projects](https://img.shields.io/badge/Open%20Source%20Projects-91-green.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/projects)
    24|
    25|## ? Introduction
    26|Large Language Models (LLMs) have rapidly evolved into powerful general-purpose reasoning and generation engines. Nevertheless, despite their continuously advancing capabilities, LLMs remain fundamentally constrained by a critical limitation: the finite length of their context window. This constraint defines the scope of information directly accessible during a single inference process, endowing models with only short-term memory capabilities. Consequently, they struggle to support extended conversations, personalized interactions, continuous learning, and complex multi-stage tasks.
    27|
    28|To transcend the inherent limitations of context windows, AI memory and memory systems for LLMs have emerged as a vital and active research and engineering frontier. By introducing external, persistent, and controllable memory structures beyond model parameters, these systems enable large models to store, retrieve, compress, and manage historical information during generation processes. This capability allows models to continuously leverage long-term experiences within limited context windows, achieving cross-session consistency and continuous reasoning abilities.
    29|
    30|Awesome-AI-Memory is a comprehensive repository dedicated to AI memory and memory systems for large language models, systematically curating relevant research papers, framework tools, and practical implementations. This repository endeavors to map the rapidly evolving research landscape in LLM memory systems, bridging multiple disciplines including natural language processing, information retrieval, intelligent agent systems, and cognitive science.
    31|
    32|---
    33|
    34|## ? Goal of Repository
    35|Our mission is to establish a centralized, continuously evolving knowledge base that serves as a valuable reference for researchers and practitioners, ultimately accelerating the development of intelligent systems capable of long-term memory retention, sustained reasoning, and adaptive evolution over time.
    36|
    37|---
    38|
    39|## ? Project Scope
    40|This repository focuses on memory mechanisms and system designs that extend or augment the context window capabilities of large language models, rather than merely addressing model pre-training or general knowledge learning. The content encompasses both theoretical research and engineering practices.
    41|
    42|? Included Content (In Scope)
    43|- Memory and memory system designs for large language models
    44|- External explicit memory beyond model parameters
    45|- Short-term memory, long-term memory, episodic memory, and semantic memory
    46|- Retrieval-Augmented Generation (RAG) as a memory access mechanism
    47|- Memory management strategies (writing, updating, forgetting, compression)
    48|- Memory systems in intelligent agents (Agents)
    49|- Shared and collaborative memory in multi-agent systems
    50|- Memory models inspired by cognitive science and biological memory
    51|- Evaluation methods, benchmarks, and datasets related to LLM memory
    52|- Open-source frameworks and tools for memory-enhanced LLMs
    53|
    54|? Excluded Content (Out of Scope)
    55|- General model pre-training or scaling research without direct memory relevance
    56|- Purely parameterized knowledge learning without memory interaction
    57|- Traditional databases or information retrieval systems unrelated to LLMs
    58|- Generic memory systems outside the LLM context (unless demonstrating direct transfer value)
    59|
    60|---
    61|
    62|<!-- ## ?? AI-Memory Taxonomy
    63|
    64|To systematically organize the diverse research and practical resources in the field of AI large model memory, this repository categorizes memory systems across multiple orthogonal dimensions, reflecting variations in storage methods, temporal scales, content forms, operational processes, and system architectures.
    65|1. Memory by Storage Location
    66|- Parametric Memory
    67|  - Knowledge implicitly encoded within model weights
    68|  - Static and not directly editable during inference
    69|- External / Explicit Memory
    70|  - Memory stored outside model parameters
    71|  - Readable, writable, and dynamically updatable
    72|2. Memory by Temporal Scope
    73|- Short-Term Memory
    74|  - Entirely dependent on context window
    75|  - Session-level, temporary information
    76|- Long-Term Memory
    77|  - Persistent memory across sessions and time scales
    78|  - Supports long-term consistency and personalization
    79|3. Memory by Content Type
    80|- Episodic Memory
    81|  - Event-based historical interaction memory
    82|  - Preserves temporal sequence and contextual relationships
    83|- Semantic Memory
    84|  - Facts, rules, and preferences abstracted from multiple experiences
    85|  - Typically derived from compression or induction of episodic memory
    86|- Procedural Memory
    87|  - Memory related to action patterns, skills, and task execution strategies
    88|4. Memory Operations
    89|- Writing: Determining which information should be stored
    90|- Retrieval: Selecting relevant memories for current tasks
    91|- Updating: Correcting or merging existing memories
    92|- Forgetting: Removing or weakening low-value information
    93|- Compression: Summarizing historical information to fit context windows
    94|5. Memory Mechanisms & Architectures
    95|- Retrieval-Augmented Generation (RAG)
    96|- Summary-based memory mechanisms
    97|- Vectorized semantic retrieval
    98|- Symbolic-neural hybrid memory systems
    99|- Event-driven and trigger-based memory mechanisms
   100|- Reinforcement learning-based memory strategy optimization
   101|6. Memory in Agent Systems
   102|- Single-agent memory
   103|- Multi-agent shared memory
   104|- Tool-augmented memory
   105|- Planning-aware memory
   106|- Personality and emotion-related memory
   107|7. Evaluation & Benchmarks
   108|- Long-term consistency evaluation
   109|- Continuous interaction and long-term task benchmarks
   110|- Memory recall and utilization efficiency metrics
   111|- Personalization and user preference retention evaluation
   112|
   113|--- -->
   114|
   115|## ? Recent hot research and news
   116|+ 2026-04-07 - ? Updated 16 papers, including 15 on methods, and 1 on benchmarks
   117|+ 2026-03-15 - ? Updated 14 papers, including 14 on methods
   118|+ 2026-03-08 - ? Updated 15 papers, including 3 on survey, 2 on systems and models, 5 on benchmarks, and 5 on methods
   119|+ 2026-03-02 - ? Add a new code agent to this repo
   120|+ 2026-02-27 - ? Updated 20 papers, including 1 on survey, 2 on systems and models, 2 on benchmarks, and 15 on methods
   121|+ 2026-02-26 - ? Updated 14 papers, including 14 on methods
   122|+ 2026-02-14 - ? Updated 15 papers, including 1 on survey, 12 on methods, 1 on benchmarks, and 1 on systems and models
   123|+ 2026-02-09 - ? Updated 15 papers
   124|+ 2026-02-01 - ? Updated 16 papers, including 9 on methods, 4 on benchmarks, and 3 on systems and models
   125|+ 2025-12-24 � ? Release Repository V(1.0)
   126|+ 2025-12-10 � ? Initial Repo
   127|
   128|---
   129|
   130|?? Table of Contents
   131|- [Awesome-AI-Memory](#awesome-ai-memory)
   132|  - [? Introduction](#-introduction)
   133|  - [? Goal of Repository](#-goal-of-repository)
   134|  - [? Project Scope](#-project-scope)
   135|  - [? Recent hot research and news](#-recent-hot-research-and-news)
   136|  - [? Core Concepts](#-core-concepts)
   137|  - [? Paper List](#-paper-list)
   138|  - [? Resources](#-resources)
   139|    - [? Benchmarks and Tasks](#-benchmarks-and-tasks)
   140|    - [? Systems and Open Sources](#-systems-and-open-sources)
   141|    - [? Multi-media resource](#-multi-media-resource)
   142|    - [? Adam Framework](#-adam-framework)
   143|  - [?  Make a Contribution](#--make-a-contribution)
   144|  - [? Community \& Support](#-community--support)
   145|  - [? Star Trends](#-star-trends)
   146|
   147|---
   148|
   149|## ? Core Concepts
   150|
   151|- LLM Memory: A fusion of implicit knowledge encoded within parameters (acquired during training) and explicit storage outside parameters (retrieved at runtime), enabling models to transcend token limitations and possess human-like abilities to "remember the past, understand the present, and predict the future."
   152|
   153|- Memory System: The complete technical stack implementing memory functionality for large language models, comprising four core components:
   154|  - Memory Storage Layer: Vector databases (e.g., Chroma, Weaviate), graph databases, or hybrid storage solutions
   155|  - Memory Processing Layer: Embedding models, summarization generators, and memory segmenters
   156|  - Memory Retrieval Layer: Multi-stage retrievers, reranking modules, and context injectors
   157|  - Memory Control Layer: Memory prioritization managers, forgetting controllers, and consistency coordinators
   158|
   159|- Memory Operations: Atomic memory operations executed through tool calling in memory systems:
   160|  - Writing: Converting dialogue content into vectors for storage, often combined with summarization to reduce noise
   161|  - Retrieval: Generating queries based on current context to obtain Top-K relevant memories
   162|  - Updating: Finding relevant memories via vector similarity and replacing or enhancing them
   163|  - Deletion: Removing specific memories based on user instructions or automatic policies (e.g., privacy expiration)
   164|  - Compression: Merging multiple related memories into summaries to free storage space
   165|
   166|- Memory Management: The methodology for managing memories within memory systems, including:
   167|  - Memory Lifecycle: End-to-end management from creation, active usage, infrequent access, to archiving/deletion
   168|  - Conflict Resolution: Arbitration mechanisms for contradictory information (e.g., timestamp priority, source credibility weighting)
   169|  - Resource Budgeting: Allocating memory quotas to different users/tasks to prevent resource abuse
   170|  - Security Governance: Automatic detection and de-identification of PII (Personally Identifiable Information)
   171|
   172|- Memory Classification: A multi-dimensional classification system unique to memory systems:
   173|  - By Access Frequency: Working memory (current tasks), frequent memory (personal preferences), archived memory (historical records)
   174|  - By Structured Degree: Structured memory (database records), semi-structured memory (dialogue summaries), unstructured memory (raw conversations)
   175|  - By Sharing Scope: Personal memory (single user), team memory (collaborative spaces), public memory (shared knowledge bases)
   176|  - By Temporal Validity: Permanent memory (core facts), temporary memory (conversation context), time-sensitive memory (e.g., "user is in a bad mood today")
   177|
   178|- Memory Mechanisms: Core technical components enabling memory system functionality:
   179|  - Retrieval-Augmented Generation (RAG): Enhancing generation by retrieving relevant information from knowledge bases
   180|  - Memory Reflection Loop: Models periodically "review" conversation history to generate high-level summaries
   181|  - Memory Routing: Automatically selecting retrieval sources based on query type (personal memory/public knowledge base)
   182|
   183|- Explicit Memory: Memory stored as raw text outside the model, implemented through vector databases with hybrid indexing strategies:
   184|  - Dense Vector Indexing: Handling semantic similarity queries
   185|  - Sparse Keyword Indexing: Processing exact match queries
   186|  - Multi-vector Indexing: Segmenting long documents into multiple parts, each independently indexed
   187|
   188|- Parametric Memory: Knowledge and capabilities stored within the fixed weights of a language model's architecture, characterized by:
   189|  - Serving as the model's core long-term semantic memory carrier
   190|  - Being activatable without external retrieval or explicit contextual support
   191|  - Providing the foundational capability for zero-shot reasoning, general responses, and language generation
   192|
   193|- Long-Term Memory: Key information designed for persistent storage, typically implemented as external knowledge bases with capabilities including:
   194|  - Automatic Summarization: Distilling multi-turn dialogues into structured memory
   195|  - Context Binding: Recording memory context to prevent erroneous generalization
   196|  - Multimodal Storage: Simultaneously preserving text, images, audio, and other multimodal memories
   197|
   198|- Short-Term Memory: Active information within the LLM's context window, constrained by attention mechanisms. Key techniques include:
   199|  - KV Cache Management: Reusing key-value caches to reduce redundant computation
   200|  - Context Compression: Using summaries instead of detailed history (e.g., "the previous 5 dialogue rounds discussed project budget")
   201|  - Sliding Window Attention: Focusing only on the most recent N tokens while preserving special markers
   202|  - Memory Summary Injection: Dynamically inserting summaries of long-term memory into short-term context
   203|
   204|- Episodic Memory: Memory type recording specific user interaction history, fundamental to personalized AI:
   205|  - User Identity Recognition: Identifying the same user across sessions
   206|  - Interaction Trajectory Recording: Preserving user decision paths and feedback
   207|  - Emotional State Tracking: Recording patterns of user mood changes
   208|  - Preference Evolution Modeling: Capturing long-term changes in user interests
   209|
   210|- Memory Forgetting: Deliberately designed forgetting mechanisms in large models, including:
   211|  - Selective Forgetting (Machine Unlearning): Removing the influence of specific information from training data, such as covering specific knowledge with forgetting layers
   212|  - Privacy-Driven Forgetting: Automatically identifying and deleting PII information, or setting automatic expiration
   213|  - Memory Decay: Automatically lowering the priority of infrequently accessed memories based on usage frequency
   214|  - Conflict-Driven Forgetting: Strategically updating or discarding old memories when new evidence conflicts with them
   215|
   216|- Memory Retrieval: The complex process of precisely locating relevant information from massive memory repositories:
   217|  - Semantic Pre-filtering: Vector similarity matching to obtain Top-100 candidates
   218|  - Contextual Reranking: Reordering results based on current query context
   219|  - Temporal Filtering: Prioritizing the most recent relevant information
   220|
   221|- Memory Compression: A collection of techniques maximizing memory utility under limited resources:
   222|  - Content-level Compression: Extracting core information while discarding redundant details
   223|  - Representation-level Compression: Vector quantization (e.g., PQ coding), dimensionality reduction
   224|  - Organization-level Compression: Clustering similar memories, building hierarchical memory structures
   225|  - Knowledge Distillation: Transferring key patterns from external memory into parametric memory
   226|
   227|---
   228|
   229|## ? Paper List
   230|Papers below are ordered by **publication date**:
   231|
   232|<details>
   233|  <summary><strong>Survey</strong></summary>
   234|
   235|  <table style="width: 100%;">
   236|    <tr>
   237|      <td><strong>Date</strong></td>
   238|      <td><strong>Paper & Summary</strong></td>
   239|      <td><strong>Tags</strong></td>
   240|      <td><strong>Links</strong></td>
   241|    </tr>
   242|    <tr>
   243|        <td rowspan="2" style="width: 15%;">2026-03-05</td>
   244|        <td style="width: 55%;"><strong>Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents</strong></td>
   245|        <td style="width: 15%;">
   246|            <img src="https://img.shields.io/badge/Long%20Context-blue" alt="Long Context">
   247|            <img src="https://img.shields.io/badge/Cost%20Analysis-brightgreen" alt="Cost Analysis">
   248|        </td>
   249|        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04814">
   250|            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
   251|        </a></td>
   252|    </tr>
   253|    <tr>
   254|        <td colspan="3">
   255|            � Addresses the ongoing industry debate over the performance and cost trade-offs between long-context models and external memory systems for building persistent agents.<br>
   256|            � Conducts a systematic cross-benchmark evaluation of long-context approaches and fact-based external memory solutions across three major memory benchmarks, assessing both accuracy and cumulative API inference cost.<br>
   257|            � Long-context models demonstrate advantages in factual recall, but their costs increase with each interaction turn; at a 100k context length, memory systems surpass them in cost efficiency after approximately 10 turns, providing a quantitative basis for real-world engineering decisions.
   258|        </td>
   259|    </tr>
   260|    <tr>
   261|        <td rowspan="2" style="width: 15%;">2026-03-02</td>
   262|        <td style="width: 55%;"><strong>Modular Memory is the Key to Continual Learning Agents</strong></td>
   263|        <td style="width: 15%;">
   264|            <img src="https://img.shields.io/badge/Continual%20Learning-blue" alt="Continual Learning">
   265|            <img src="https://img.shields.io/badge/Architecture-brightgreen" alt="Architecture">
   266|        </td>
   267|        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01761">
   268|            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
   269|        </a></td>
   270|    </tr>
   271|    <tr>
   272|        <td colspan="3">
   273|            � Traditional foundation models rely on weight updates for continual learning, which can easily lead to catastrophic forgetting and makes large-scale experience accumulation difficult.<br>
   274|            � Proposes a roadmap for a modular memory architecture that integrates in-context learning with learning encoded in model weights.<br>
   275|            � This architecture leverages in-context learning for rapid adaptation and weight updates for capability consolidation, offering theoretical guidance for building truly lifelong learning agents.
   276|        </td>
   277|    </tr>
   278|    <tr>
   279|        <td rowspan="2" style="width: 15%;">2026-03-02</td>
   280|        <td style="width: 55%;"><strong>Emerging Human-like Strategies for Semantic Memory Foraging in Large Language Models</strong></td>
   281|        <td style="width: 15%;">
   282|            <img src="https://img.shields.io/badge/Cognitive%20Alignment-blue" alt="Cognitive Alignment">
   283|            <img src="https://img.shields.io/badge/Interpretability-brightgreen" alt="Interpretability">
   284|        </td>
   285|        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01822">
   286|            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
   287|        </a></td>
   288|    </tr>
   289|    <tr>
   290|        <td colspan="3">
   291|            � Investigates whether large language models possess human-like, efficient strategic access mechanisms when processing vast amounts of semantic memory.<br>
   292|            � Uses mechanistic interpretability techniques to analyze semantic fluency tasks, rigorously examining convergent and divergent memory search patterns within the model.<br>
   293|            � Confirms the presence of human-like strategic memory search behavior across different layers of LLMs, laying an interpretability foundation for research on cognitive alignment and enhanced human-AI collaboration.
   294|        </td>
   295|    </tr>
   296|    <tr>
   297|        <td rowspan="2" style="width: 15%;">2026-02-26</td>
   298|        <td style="width: 55%;"><strong>Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions</strong></td>
   299|        <td style="width: 15%;">
   300|            <img src="https://img.shields.io/badge/Personalized%20Agents-blue" alt="Personalized Agents">
   301|            <img src="https://img.shields.io/badge/User%20Adaptation-brightgreen" alt="User Adaptation">
   302|            <img src="https://img.shields.io/badge/Evaluation-yellow" alt="Evaluation">
   303|        </td>
   304|        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.22680.pdf">
   305|            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
   306|        </a></td>
   307|    </tr>
   308|    <tr>
   309|        <td colspan="3">
   310|            � This paper explores the foundations, evaluation, and future directions of personalized LLM-driven agents, providing a capability-oriented systematic review of their underlying principles, assessment methodologies, and prospective developments.<br>
   311|            � It constructs a taxonomy centered on four interdependent core components: user profile modeling, memory, planning, and action execution.<br>
   312|            � The paper offers a comprehensive analysis of how user signals are represented, propagated, and utilized, and discusses application scenarios and design trade-offs ranging from general-purpose assistance to specialized domains.
   313|        </td>
   314|    </tr>
   315|    <tr>
   316|      <td rowspan="2" style="width: 15%;">2026-01-14</td>
   317|      <td style="width: 55%;">
   318|      <strong>Rethinking Memory Mechanisms of Foundation Agents in the Second Half: A Survey</strong></td>
   319|      <td style="width: 15%;">
   320|        <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
   321|        <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
   322|        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms Badge">
   323|      </td>
   324|      <td style="width: 15%;">
   325|        <a href="https://arxiv.org/pdf/2602.06052">
   326|        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
   327|        </a>
   328|      </td>
   329|    </tr>
   330|    <tr>
   331|        <td colspan="3">
   332|          � This paper proposes a unified taxonomy for foundation agent memory across three dimensions: memory substrate, cognitive mechanism, and memory subject.<br>
   333|          � It analyzes memory operation mechanisms in single-agent and multi-agent systems while categorizing memory learning policies into prompting, fine-tuning, and reinforcement learning paradigms.<br>
   334|          � It provides a comprehensive review of evaluation metrics and benchmarks across various applications, outlining critical future directions such as memory efficiency, life-long personalization, and multimodal integration.
   335|        </td>
   336|    </tr>
   337|    <tr>
   338|      <td rowspan="2" style="width: 15%;">2025-12-15</td>
   339|      <td style="width: 55%;">
   340|      <strong>Memory in the Age of AI Agents: A Survey</strong></td>
   341|      <td style="width: 15%;">
   342|        <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
   343|        <img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
   344|        <img src="https://img.shields.io/badge/Forms--Functions--Dynamics-purple" alt="Forms-Functions-Dynamics">
   345|      </td>
   346|      <td style="width: 15%;">
   347|        <a href="https://arxiv.org/pdf/2512.13564">
   348|        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
   349|        </a>
   350|      </td>
   351|    </tr>
   352|    <tr>
   353|        <td colspan="3">
   354|          � Provides a comprehensive and up-to-date landscape of agent memory, explicitly distinguishing it from related concepts like LLM memory, RAG, and context engineering.<br>
   355|          � Introduces a unified taxonomy examining memory through three lenses: <strong>Forms</strong> (token-level, parametric, latent), <strong>Functions</strong> (factual, experiential, working), and <strong>Dynamics</strong> (formation, evolution, retrieval).<br>
   356|          � Discusses emerging research frontiers such as automation-oriented memory design, reinforcement learning integration, and trustworthiness, while compiling representative benchmarks and frameworks.
   357|        </td>
   358|    </tr>
   359|    <tr>
   360|      <td rowspan="2" style="width: 15%;">2025-09-18</td>
   361|      <td style="width: 55%;">
   362|      <strong>A Survey of Machine Unlearning</strong></td>
   363|      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting"></td>
   364|      <td style="width: 15%;">
   365|        <a href="https://dl.acm.org/doi/full/10.1145/3749987">
   366|        <img src="https://img.shields.io/badge/ACM-Paper-black?labelColor=blue" alt="Paper Badge">
   367|        </a>
   368|      </td>
   369|    </tr>
   370|    <tr>
   371|        <td colspan="3">
   372|          � Provides an in-depth exploration of the concept and background of machine unlearning, highlighting its importance in modern machine learning.<br>
   373|          � Machine unlearning aims to enable learning algorithms to effectively remove the influence of specific data without requiring full model retraining.<br>
   374|          � The paper analyzes the necessity, challenges, and design requirements of machine unlearning, reviews current research progress, and emphasizes the field�s complexity and diversity in terms of algorithmic effectiveness, fairness, and privacy protection.
   375|        </td>
   376|    </tr>
   377|    <tr>
   378|      <td rowspan="2" style="width: 15%;">2025-09-02</td>
   379|      <td style="width: 55%;">
   380|      <strong>A Survey on the Memory Mechanism of Large Language Model based Agents</strong></td>
   381|      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms Badge">
   382|      <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules Badge">
   383|      <td style="width: 15%;">
   384|        <a href="https://dl.acm.org/doi/pdf/10.1145/3748302">
   385|        <img src="https://img.shields.io/badge/ACM-Paper-black?labelColor=blue" alt="Paper Badge"></a>
   386|      </td>
   387|    </tr>
   388|    <tr>
   389|        <td colspan="3">
   390|          � Explores the memory mechanisms of LLM-based agents, emphasizing the crucial role of memory in agent self-evolution and complex interactions.<br>
   391|          � Systematically summarizes and categorizes existing memory module designs and evaluation methods, while analyzing their roles and limitations across different application scenarios.<br>
   392|          � Such agents are able to improve decision-making and task execution.
   393|        </td>
   394|    </tr>
   395|    <tr>
   396|      <td rowspan="2" style="width: 15%;">2025-05-31</td>
   397|      <td style="width: 55%;">
   398|      <strong>A Survey of Machine Unlearning in Large Language Models: Methods, Challenges and Future Directions</strong></td>
   399|      <td style="width: 15%;">
   400|      <img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting"></td>
   401|      <td style="width: 15%;">
   402|        <a href="https://arxiv.org/pdf/2503.01854v2">
   403|        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
   404|      </td>
   405|    </tr>
   406|    <tr>
   407|        <td colspan="3">
   408|          � The paper investigates machine unlearning in large language models (LLMs), aiming to effectively remove the influence of undesirable data (e.g., sensitive or illegal information) without full retraining, while preserving overall model utility.<br>
   409|          � It defines the objectives and paradigms of LLM unlearning and establishes a comprehensive taxonomy.<br>
   410|          � The paper reviews existing approaches, evaluates their strengths and limitations, and discusses opportunities for future research.
   411|        </td>
   412|    </tr>
   413|    <tr>
   414|      <td rowspan="2" style="width: 15%;">2025-05-27</td>
   415|      <td style="width: 55%;">
   416|      <strong>Rethinking Memory in AI Taxonomy, Operations, Topics, and Future Directions</strong></td>
   417|      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
   418|      <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
   419|      <img src="https://img.shields.io/badge/Memory%20Integration-purple" alt="Memory Integration">
   420|      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
   421|      <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
   422|      <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
   423|      </td>
   424|      <td style="width: 15%;">
   425|        <a href="https://arxiv.org/pdf/2505.00675">
   426|        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
   427|      </td>
   428|    </tr>
   429|    <tr>
   430|        <td colspan="3">
   431|          � Explores multidimensional research on memory in artificial intelligence (AI), with a particular focus on memory operations and management in large language models (LLMs).<br>
   432|          � Categorizes various types of memory representations and operations�including integration, updating, indexing, forgetting, retrieval, and compression�and provides a systematic analysis of the importance of memory in AI and how it is implemented.<br>
   433|          � Through an extensive review of the literature, the paper identifies four key research themes: long-term memory, parametric memory, long-context memory, and multi-source memory integration.
   434|        </td>
   435|    </tr>
   436|    <tr>
   437|      <td rowspan="2" style="width: 15%;">2025-04-24</td>
   438|      <td style="width: 55%;">
   439|      <strong>Cognitive Memory in Large Language Models</strong></td>
   440|      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
   441|      <img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
   442|      </td>
   443|      <td style="width: 15%;">
   444|        <a href="https://arxiv.org/pdf/2504.02441">
   445|        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
   446|      </td>
   447|    </tr>
   448|    <tr>
   449|        <td colspan="3">
   450|          � Provides a comprehensive examination of memory mechanisms in large language models (LLMs), with a particular focus on different types of memory and their roles within the models.<br>
   451|          � While LLMs excel at information retrieval and interaction summarization, their long-term memory remains unstable.<br>
   452|          � Integrating memory into AI systems is crucial for delivering context-rich responses, reducing hallucinations, improving data processing efficiency, and enabling the self-evolution of AI systems.
   453|        </td>
   454|    </tr>
   455|    <tr>
   456|      <td rowspan="2" style="width: 15%;">2025-04-23</td>
   457|      <td style="width: 55%;"><strong>From Human Memory to AI Memory A Survey on Memory Mechanisms in the Era of LLMs </strong></td>
   458|      <td style="width: 15%;"><img src="https://img.shields.io/badge/Human%20Memory-red" alt="Human Memory">
   459|      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
   460|      </td>
   461|      <td style="width: 15%;">
   462|        <a href="https://arxiv.org/pdf/2504.15965">
   463|        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
   464|      </td>
   465|    </tr>
   466|    <tr>
   467|        <td colspan="3">
   468|          � Explores the relationship between human memory and the memory mechanisms of LLM-based artificial intelligence (AI) systems.<br>
   469|          � The main contributions include a systematic definition of memory in LLM-driven AI systems and its conceptual linkage to human memory.<br>
   470|          � The paper proposes a three-dimensional memory taxonomy based on object, form, and time, and summarizes key open issues in current research on personal memory and system memory.
   471|        </td>
   472|    </tr>
   473|    <tr>
   474|      <td rowspan="2" style="width: 15%;">2025-04-02</td>
   475|      <td style="width: 55%;"><strong>Digital Forgetting in Large Language Models: A Survey of Unlearning Methods</strong></td>
   476|      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
   477|      <td style="width: 15%;">
   478|        <a href="https://arxiv.org/pdf/2404.02062">
   479|        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
   480|      </td>
   481|    </tr>
   482|    <tr>
   483|        <td colspan="3">
   484|          � The paper explores digital forgetting in large language models (LLMs) and corresponding unlearning methods, with a focus on addressing issues related to privacy, copyright, and social ethics.<br>
   485|          � It analyzes different types of model architectures and training processes, as well as practical approaches to digital forgetting, including data retraining, machine unlearning, and prompt engineering.<br>
   486|          � By introducing the concept of �forgetting guarantees,� the paper emphasizes effective mechanisms for both exact and approximate forgetting.
   487|        </td>
   488|    </tr>
   489|    <tr>
   490|      <td rowspan="2" style="width: 15%;">2025-01-12</td>
   491|      <td style="width: 55%;"><strong>Human-inspired Perspectives: A Survey on AI Long-term Memory</strong></td>
   492|      <td style="width: 15%;"><img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
   493|      <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
   494|      <img src="https://img.shields.io/badge/Non--Parametric%20Memory-green" alt="Non-Parametric Memory">
   495|      <img src="https://img.shields.io/badge/Sensory%20Memory-brown" alt="Sensory Memory">
   496|      <img src="https://img.shields.io/badge/Working%20Memory-blueviolet" alt="Working Memory">
   497|      </td>
   498|      <td style="width: 15%;">
   499|        <a href="https://arxiv.org/pdf/2411.00489">
   500|        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
   501|