---
status: processed
---
     1|---
     2|source: https://github.com/HUST-AI-HYZ/MemoryAgentBench
     3|date: 2026-04-13
     4|type: repo
     5|tags: [agent-memory, benchmark, evaluation, iclr-2026, multi-turn]
     6|status: raw
     7|---
     8|
     9|# ?? MemoryAgentBench: Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions
    10|
    11|[Yuanzhe Hu](https://hust-ai-hyz.github.io), [Yu Wang](https://yuwang.us), [Julian McAuley](https://cseweb.ucsd.edu/~jmcauley/).
    12|
    13|This project benchmarks agents with memory capabilities. Follow the steps below to set up your environment and install dependencies.
    14|
    15|[Full paper](https://arxiv.org/abs/2507.05257)
    16|
    17|## ? LongMemEval Overview
    18|
    19|Four Core Competencies for Evaluation:
    20|* Accurate Retrieval (AR)
    21|
    22|* Test-Time Learning (TTL)
    23|
    24|* Long-Range Understanding (LRU)
    25|
    26|* Conflict Resolution (CR)
    27|
    28|![Example Questions in MemoryAgentBench](assets/intro.png)
    29|
    30|We collected and reformulated data from previous benchmarks and datasets. All data is split into chunks to simulate real multi-turn interaction scenarios�just like your daily conversations with an AI assistant. We also newly constructed two datasets **EventQA** and **FactConsolidation**.
    31|
    32|Notably, the team adopted a "inject once, query multiple times" design philosophy�one long text corresponds to multiple questions, significantly improving evaluation efficiency.
    33|
    34|## ? Update
    35|- [x] (Jan. 26th, 2026)
    36|    Our paper is accepted by Fourteenth International Conference on Learning Representations (ICLR 2026). We will make some improvement for our current benchmark.
    37|
    38|- [x] (Sep. 28th, 2025)
    39|    We publish a new version of our paper.
    40|
    41|- [x] (Aug. 5th, 2025)
    42|    We optimized the ```template.py``` for better usage.
    43|
    44|- [x] (July 22th, 2025)
    45|    We updated the ```Readme.md``` and release the code for ```longmemeval``` and ```infbench_sum```. They are needed to evaluate by using ```gpt-4o``` as a judge.
    46|
    47|    We change the ```uuid``` into ```qa_pair_id``` in our code.
    48|
    49|    We updated the huggingface dataset slightly.
    50|
    51|- [x] (July 7th, 2025)
    52|    We released the code for reproducing the main experiment.
    53|
    54|- TODO List ?? .
    55|
    56|    <del> [x] New Dataset in Long Range Understanding (LRU). </del>
    57|
    58|    [] Leaderboard website for our benchmark.
    59|
    60|    [] The code framework with separated front-end and back-end is easier to integrate with custom memory agents.
    61|
    62|**? More details (such as datasets collection) coming soon! ?**
    63|
    64|## ? Quick Setup
    65|
    66|### 1. Create a Conda Environment
    67|
    68|It�s recommended to use a dedicated conda environment for reproducibility:
    69|```
    70|conda create --name MABench python=3.10.16
    71|```
    72|
    73|### 2. Install Python Dependencies
    74|
    75|```
    76|pip install torch
    77|pip install -r requirements.txt
    78|pip install "numpy<2"
    79|```
    80|We did not include the `hipporag` in `requirements.txt` since the current version of `hipporag` will cause some conflicts on pacakge version. You can create another environment with hipporag instead.
    81|
    82|Sometimes you can try to supplement the lacked packages for `cognee` and `letta`. If you met some package related errors after installing `requirements.txt`.
    83|```
    84|pip install letta
    85|pip uninstall letta
    86|pip install cognee
    87|pip uninstall cognee
    88|```
    89|
    90|## ? Data Download & API Settings
    91|
    92|To use this project, you need to download the processed data files and place them in the correct directory.
    93|
    94|### 1. Download the Data from HuggingFace ?
    95|
    96|- HuggingFace dataset [link](https://huggingface.co/datasets/ai-hyz/MemoryAgentBench). It can be automatically downloaded if you run the code directly.
    97|
    98|- Do not forget the `entity2id.json` for Movie Recommendation task.
    99|
   100|### 2. Environment Variable Settings
   101|
   102|To run this project, you need to configure your API keys and model settings in a `.env` file at the project root.
   103|
   104|Create a `.env` file and add the following content, replacing the placeholder values with your actual API keys:
   105|
   106|#### OpenAI API Keys
   107|
   108|```
   109|OPENAI_API_KEY=###you..._key
   110|```
   111|
   112|#### Settings for Cognee
   113|```
   114|LLM_MODEL=gpt-4o-mini
   115|LLM_API_KEY=***
   116|```
   117|
   118|#### Other API Keys
   119|```
   120|Anthropic_API_KEY=###you..._api
   121|Google_API_KEY=###you..._api
   122|```
   123|
   124|## ???? Run Evaluation
   125|
   126|Follow these steps to evaluate the benchmarking agent:
   127|
   128|### Run Example Evaluation Command
   129|
   130|You can run an evaluation using the following example command:
   131|
   132|#### Long Context Agents
   133|```
   134|bash bash_files/eniac/run_memagent_longcontext.sh
   135|```
   136|- `--agent_config`: Path to the agent/model configuration file.
   137|- `--dataset_config`: Path to the dataset configuration file.
   138|
   139|#### Rag Agents and Agentic Memory Methods
   140|
   141|```
   142|bash bash_files/eniac/run_memagent_rag_agents.sh
   143|```
   144|#### Ablation Study for Chunk Size
   145|```
   146|bash bash_files/eniac/run_memagent_rag_agents_chunksize.sh
   147|```
   148|
   149|Remember that `hipporag (2.0.0a3)` reuqires `openai==1.58.1`, which may cause some latest OpenAI models could not be used in same environment.
   150|
   151|### Run LLM-based Metric Evaluation
   152|
   153|You can run an evaluation using the following example python files, you also need to set the configs
   154|
   155|#### LongmemEval
   156|
   157|```
   158|python llm_based_eval/longmem_qa_evaluate.py
   159|```
   160|
   161|#### InfBench Summarization
   162|```
   163|python llm_based_eval/summarization_evaluate.py
   164|```
   165|
   166|## ? Acknowledgement
   167|
   168|We thank the open-source code and datasets from RULER, InfBench, HELMET and LongmemEval.
   169|
   170|## ? Citation
   171|
   172|We would appreciate it if you could cite the following paper if you found the repository useful for your work:
   173|```
   174|@article{hu2025evaluating,
   175|  title={Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions},
   176|  author={Hu, Yuanzhe and Wang, Yu and McAuley, Julian},
   177|  journal={arXiv preprint arXiv:2507.05257},
   178|  year={2025}
   179|}
   180|```
   181|
   182|