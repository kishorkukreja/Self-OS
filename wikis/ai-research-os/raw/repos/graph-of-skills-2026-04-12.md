---
status: processed
---
     1|---
     2|source: https://github.com/davidliuk/graph-of-skills
     3|date: 2026-04-12
     4|type: repo
     5|tags: [skill-graph, agent-skills, retrieval, dependency-aware, llm-agents]
     6|status: raw
     7|---
     8|
     9|<h1 align="center">Graph of Skills (GoS)</h1>
    10|
    11|<p align="center">
    12|  <strong>Dependency-Aware Structural Retrieval for Massive Agent Skills</strong>
    13|</p>
    14|
    15|<p align="center">
    16|  <em>Dawei Liu*, Zongxia Li*, Hongyang Du, Xiyang Wu, Shihang Gui, Yongbei Kuang, Lichao Sun</em>
    17|</p>
    18|
    19|<p align="center">
    20|  <a href="https://arxiv.org/abs/2604.05333"><img src="https://img.shields.io/badge/arXiv-2604.05333-b31b1b?logo=arxiv" alt="Paper"></a>
    21|  <a href="https://huggingface.co/datasets/DLPenn/graph-of-skills-data"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Data-yellow" alt="Data"></a>
    22|  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue" alt="License"></a>
    23|  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.10--3.12-3776ab?logo=python&logoColor=white" alt="Python"></a>
    24|</p>
    25|
    26|---
    27|
    28|Graph of Skills builds a **skill graph** offline from a library of `SKILL.md` documents, then retrieves a small, ranked set of relevant skills at task time. Instead of flooding the agent context with an entire skill library, GoS surfaces only the skills most likely to help -- along with their prerequisites and related capabilities.
    29|
    30|<p align="center">
    31|  <img src="assets/demo.png" alt="Comparison of Vanilla Skills, Vector Skills, and Graph of Skills" width="800">
    32|</p>
    33|
    34|## How It Works
    35|
    36|<p align="center">
    37|  <img src="assets/pipeline.png" alt="GoS pipeline: Offline Indexing ? Graph Construction ? Online Retrieval" width="800">
    38|</p>
    39|
    40|**Retrieval pipeline:**
    41|
    42|1. **Seed** -- retrieve semantic candidates (embedding similarity) and lexical candidates (exact-match tokens)
    43|2. **Merge** -- combine both candidate pools
    44|3. **Rerank** -- rerank using the skill-graph structure (dependencies, co-occurrence)
    45|4. **Return** -- emit a capped, agent-readable skill bundle
    46|
    47|## Documentation
    48|
    49|| Document | What it covers |
    50||----------|----------------|
    51|| [DATA.md](DATA.md) | Downloading skill sets, SkillsBench tasks, and prebuilt workspaces (`scripts/download_data.sh`); rebuilding a workspace from source; packaging uploads for HuggingFace |
    52|| [evaluation/README.md](evaluation/README.md) | **Evaluation overview**: ALFWorld, SkillsBench runners, retrieval modes (`gos` / `vector` / `all_full` / `none`), environment setup for benchmark tracks |
    53|| [evaluation/skillsbench/README.md](evaluation/skillsbench/README.md) | **SkillsBench detail**: Harbor, Docker, generating task variants (`graphskills_benchmark.py`), batch configs, agents |
    54|| [`.env.example`](.env.example) | All `GOS_*` and provider variables for indexing, retrieval, and CLI |
    55|| [CONTRIBUTING.md](CONTRIBUTING.md) | Dev setup, tests, project layout for contributors |
    56|
    57|## Installation
    58|
    59|### Requirements
    60|
    61|- Python 3.10 -- 3.12
    62|- [`uv`](https://docs.astral.sh/uv/) (recommended) or `pip`
    63|- An embedding API key (OpenAI, Gemini, or any OpenAI-compatible provider)
    64|
    65|### Setup
    66|
    67|```bash
    68|git clone https://github.com/graph-of-skills/graph-of-skills.git
    69|cd graph-of-skills
    70|uv sync
    71|cp .env.example .env   # then fill in your API keys
    72|```
    73|
    74|<details>
    75|<summary><strong>Provider: OpenAI (direct)</strong></summary>
    76|
    77|```bash
    78|OPENAI_API_KEY=***
    79|# Use the ``openai/...`` prefix so LiteLLM targets the OpenAI API (omit OPENAI_BASE_URL).
    80|GOS_EMBEDDING_MODEL=openai/text-embedding-3-large
    81|GOS_EMBEDDING_DIM=3072
    82|```
    83|</details>
    84|
    85|<details>
    86|<summary><strong>Provider: OpenRouter</strong></summary>
    87|
    88|```bash
    89|OPENROUTER_API_KEY=***
    90|OPENAI_BASE_URL=https://openrouter.ai/api/v1
    91|GOS_EMBEDDING_MODEL=openrouter/openai/text-embedding-3-large
    92|GOS_EMBEDDING_DIM=3072
    93|```
    94|</details>
    95|
    96|<details>
    97|<summary><strong>Provider: Azure AI (OpenAI-compatible)</strong></summary>
    98|
    99|```bash
   100|OPENAI_API_KEY=***
   101|OPENAI_BASE_URL=https://YOUR-RESOURCE.services.ai.azure.com/openai/v1
   102|# Must match your **deployment name** in Azure (not necessarily ``text-embedding-3-large``).
   103|GOS_EMBEDDING_MODEL=openai/<your-deployment-name>
   104|GOS_EMBEDDING_DIM=<vector-dimension-for-that-model>
   105|```
   106|</details>
   107|
   108|<details>
   109|<summary><strong>Provider: Google Gemini</strong></summary>
   110|
   111|```bash
   112|GEMINI_API_KEY=***
   113|GOS_EMBEDDING_MODEL=gemini/gemini-embedding-001
   114|GOS_EMBEDDING_DIM=3072
   115|```
   116|</details>
   117|
   118|## Quick Start
   119|
   120|**Goal:** install the package, pull the published skill libraries, build (or download) a graph workspace, then run retrieval from the shell.
   121|
   122|**Read next:** [DATA.md](DATA.md) for every download flag and asset size; [`.env.example`](.env.example) for embedding providers. After GoS works locally, use [evaluation/README.md](evaluation/README.md) for benchmark runners and [evaluation/skillsbench/README.md](evaluation/skillsbench/README.md) for Harbor-based SkillsBench.
   123|
   124|### Step 0: Install (once per machine)
   125|
   126|Complete [Installation](#installation) above: clone, `uv sync`, `cp .env.example .env`, and set **embedding** (and optional LLM) keys. Indexing and retrieval load `.env` from the repo root when you use `uv run gos �`.
   127|
   128|### Step 1: Download skill libraries
   129|
   130|The collections **`skills_200`**, **`skills_500`**, **`skills_1000`**, **`skills_2000`** are directories of `SKILL.md` files on [HuggingFace](https://huggingface.co/datasets/DLPenn/graph-of-skills-data), **not** in git. They unpack to:
   131|
   132|- `data/skillsets/skills_200/` � `data/skillsets/skills_2000/`
   133|
   134|```bash
   135|./scripts/download_data.sh --skillsets
   136|```
   137|
   138|This tries each archive, **skips** directories that already have files, and logs `[skip]` if an archive is not yet on the Hub. Gated datasets: `HF_TOKEN=*** ./scripts/download_data.sh --skillsets`. Full reference (tasks, workspaces, selective flags): **[DATA.md](DATA.md)**.
   139|
   140|**Tiny smoke test without HuggingFace:** index the built-in folder `skills/` (only a few skills) with any `--workspace` path you like.
   141|
   142|### Step 2: Workspace directory layout (recommended for benchmarks)
   143|
   144|`--workspace` is where GoS stores the **indexed graph** (vectors + graph storage). Use the **same** path for `gos retrieve`, `gos status`, and `gos add`.
   145|
   146|For **ALFWorld** and **SkillsBench** defaults, keep this mapping (see [evaluation/README.md](evaluation/README.md) and `evaluation/skillsbench/graphskills_benchmark.py`):
   147|
   148|| Skill tree you index | Recommended `--workspace` |
   149||----------------------|---------------------------|
   150|| `data/skillsets/skills_200` | `data/gos_workspace/skills_200_v1` |
   151|| `data/skillsets/skills_500` | `data/gos_workspace/skills_500_v1` |
   152|| `data/skillsets/skills_1000` | `data/gos_workspace/skills_1000_v1` |
   153|| `data/skillsets/skills_2000` | `data/gos_workspace/skills_2000_v1` |
   154|
   155|### Step 3: Get a workspace (choose one path)
   156|
   157|**A. Build locally** (needs embedding API; duration grows with library size):
   158|
   159|```bash
   160|mkdir -p data/gos_workspace
   161|uv run gos index data/skillsets/skills_200 \
   162|  --workspace data/gos_workspace/skills_200_v1 --clear
   163|```
   164|
   165|Use the matching pair for other sets (e.g. `skills_1000` ? `data/gos_workspace/skills_1000_v1`). **Embedding model and dimension in `.env` must stay the same** for later retrieval (see [Configuration](#configuration)).
   166|
   167|**B. Download a prebuilt workspace** (no `gos index`; must match the embedding used to build that archive):
   168|
   169|```bash
   170|./scripts/download_data.sh --workspace
   171|```
   172|
   173|See **[DATA.md](DATA.md)** for which `gos_workspace_skills_*_v1.tar.gz` files exist on the Hub and how they map to `data/gos_workspace/`.
   174|
   175|### Step 4: Retrieve
   176|
   177|```bash
   178|uv run gos retrieve "parse binary STL file, calculate volume and mass" \
   179|  --workspace data/gos_workspace/skills_200_v1 --max-skills 5
   180|```
   181|
   182|### Step 5: Inspect or extend
   183|
   184|```bash
   185|uv run gos status --workspace data/gos_workspace/skills_200_v1
   186|uv run gos add path/to/NEW_SKILL.md --workspace data/gos_workspace/skills_200_v1
   187|```
   188|
   189|### Step 6: What to run next
   190|
   191|- **End-to-end sanity check** (retrieval + one Docker task): [Minimal verification](#minimal-verification) below.
   192|- **Paper benchmarks** (ALFWorld, SkillsBench): **[evaluation/README.md](evaluation/README.md)** (overview) and **[evaluation/skillsbench/README.md](evaluation/skillsbench/README.md)** (Harbor / task generation).
   193|
   194|## Minimal verification
   195|
   196|**Scope:** GoS retrieval against a real workspace, then **one** [SkillsBench](evaluation/skillsbench/README.md) task in Docker via [Harbor](https://github.com/harbor-ai/harbor). This is a smoke test, not a full benchmark sweep. For all tracks, see [evaluation/README.md](evaluation/README.md).
   197|
   198|### Prerequisites
   199|
   200|- `uv sync` and a filled `.env` (embedding provider for the workspace you use, plus **`GEMINI_API_KEY`** for the Harbor agent when using `gemini-cli`).
   201|- **Docker** running (Harbor drives the task container).
   202|- **Harbor** on your `PATH`, e.g. `uv tool install harbor` (see [evaluation/skillsbench/README.md](evaluation/skillsbench/README.md)).
   203|- **Skill library** `data/skillsets/skills_200/` (from `./scripts/download_data.sh --skillsets` or the full download script).
   204|- A **workspace** at `data/gos_workspace/skills_200_v1`: either build with `gos index` or download with `./scripts/download_data.sh --workspace` ([Quick Start, Step 3](#step-3-get-a-workspace-choose-one-path); full detail in [DATA.md](DATA.md)).
   205|
   206|The embedding model in `.env` must match how that workspace was built (same `GOS_EMBEDDING_MODEL` / `GOS_EMBEDDING_DIM` as at index time).
   207|
   208|### 1. Retrieval smoke test
   209|
   210|```bash
   211|uv run gos retrieve "unit tests with pytest" \
   212|  --workspace data/gos_workspace/skills_200_v1 --max-skills 3
   213|```
   214|
   215|You should see **`SKILL_HIT`** and at least one skill block. If you get errors about embedding dimension or missing keys, fix `.env` before continuing.
   216|
   217|### 2. Generate a single graph-skills task pack
   218|
   219|From the **repository root**, materialize one task (`dialogue-parser` is a small, standard example; it must exist under `evaluation/skillsbench/tasks/`):
   220|
   221|```bash
   222|uv run python evaluation/skillsbench/graphskills_benchmark.py \
   223|  --skillset-name skills_200 \
   224|  --task dialogue-parser \
   225|  --skip-allskills --skip-vectorskills \
   226|  --output-root evaluation/skillsbench/generated_verify
   227|```
   228|
   229|This writes `evaluation/skillsbench/generated_verify/tasks_graph_skills/dialogue-parser/` with the graph-retrieval sidecar and mounts your workspace into the task image.
   230|
   231|### 3. Run that task with Harbor
   232|
   233|Still from the repo, load keys then run Harbor **from `evaluation/skillsbench/`** so paths resolve like the rest of the eval docs:
   234|
   235|```bash
   236|cd evaluation/skillsbench
   237|set -a && source ../../.env && set +a
   238|harbor run --agent gemini-cli \
   239|  --model gemini/gemini-3-flash-preview \
   240|  --force-build \
   241|  -p generated_verify/tasks_graph_skills/dialogue-parser \
   242|  -o jobs/verify-sample
   243|```
   244|
   245|Use a `--model` string your Harbor agent accepts (often the same family as in `.env`). First run may spend time on **image build**.
   246|
   247|### 4. What �success� looks like
   248|
   249|- Harbor finishes with **`Errors: 0`** in the summary table.
   250|- A **`result.json`** appears under `evaluation/skillsbench/jobs/verify-sample/<timestamp>/`.
   251|- **Reward** may be `0.0`, partial (e.g. `0.5`), or `1.0` depending on the task and agent; that is normal. The goal of this minimal path is to confirm **retrieval, task packaging, Docker, and the agent all run**, not to maximize score.
   252|
   253|For more agents, configs, and batch YAML, see [evaluation/skillsbench/README.md](evaluation/skillsbench/README.md).
   254|
   255|## CLI Reference
   256|
   257|| Command | Description |
   258||---------|-------------|
   259|| `gos index <dir>` | Build a graph workspace from a skill directory |
   260|| `gos add <file>` | Add a single skill to an existing workspace |
   261|| `gos retrieve <query>` | Retrieve a ranked skill bundle for a query |
   262|| `gos query <query>` | Compact retrieval output (for debugging) |
   263|| `gos status` | Show workspace statistics |
   264|| `gos experiment` | Run built-in experiment presets |
   265|| `graphskills-query` | Agent-facing retrieval (rewrites `Source:` paths for containers) |
   266|| `gos-server` | Start the MCP server for tool-based retrieval |
   267|
   268|## Agent Integration
   269|
   270|Inside a Docker container, an agent calls `graphskills-query` with a natural-language task description and receives a bounded skill bundle:
   271|
   272|```bash
   273|graphskills-query "parse binary STL file and calculate mass"
   274|```
   275|
   276|Each returned skill includes a `Source:` path the agent can open directly:
   277|
   278|```
   279|Source: /opt/graphskills/skills/mesh-analysis/SKILL.md
   280|```
   281|
   282|Set `GOS_SKILLS_DIR` to control path rewriting, so the same workspace can be indexed on a host and queried inside a container.
   283|
   284|## Configuration
   285|
   286|All runtime settings are driven by environment variables. See [`.env.example`](.env.example) for the full template. Download paths and workspace layout on disk are documented in **[DATA.md](DATA.md)**.
   287|
   288|| Variable | Default | Description |
   289||----------|---------|-------------|
   290|| `GOS_EMBEDDING_MODEL` | `openai/text-embedding-3-large` | Embedding model for indexing and retrieval (use `openai/<deployment>` on Azure) |
   291|| `GOS_EMBEDDING_DIM` | `3072` | Embedding dimension (must match the model output) |
   292|| `GOS_PREBUILT_WORKING_DIR` | -- | Path to a prebuilt workspace for retrieval |
   293|| `GOS_RETRIEVAL_TOP_N` | `8` | Maximum number of skills returned |
   294|| `GOS_SEED_TOP_K` | `5` | Initial seed count before graph expansion |
   295|| `GOS_MAX_CONTEXT_CHARS` | `12000` | Hard cap on total returned bundle size (chars) |
   296|| `GOS_SKILLS_DIR` | -- | Container-side skill root (for `Source:` path rewriting) |
   297|
   298|> **Note:** The embedding model at retrieval time **must** match the model used when the workspace was indexed.
   299|
   300|## Repository Layout
   301|
   302|```
   303|graph-of-skills/
   304|??? gos/                          # Core GoS package
   305|?   ??? core/                     #   Engine, retrieval, parsing, schema
   306|?   ??? interfaces/               #   CLI and MCP server
   307|?   ??? utils/                    #   Configuration (pydantic-settings)
   308|??? data/                         # Downloaded data (gitignored; see [DATA.md](DATA.md))
   309|?   ??? skillsets/                #   Skill libraries (skills_200, 500, 1000, 2000)
   310|?   ??? gos_workspace/            #   Indexed or prebuilt graph workspaces
   311|??? evaluation/                   # See [evaluation/README.md](evaluation/README.md)
   312|?   ??? alfworld_run.py           #   ALFWorld benchmark runner
   313|?   ??? skill.py                  #   SkillModule adapter for GoS
   314|?   ??? skillsbench/              #   SkillsBench � [skillsbench/README.md](evaluation/skillsbench/README.md)
   315|??? skills/                       # Agent bootstrap skills for retrieval
   316|??? scripts/                      # Utility scripts (data download, etc.)
   317|??? tests/                        # Test suite
   318|??? pyproject.toml                # Package definition & CLI entry points
   319|??? .env.example                  # Environment variable template
   320|??? DATA.md                       # [Data & downloads](DATA.md)
   321|??? evaluation/README.md          # [Benchmark overview](evaluation/README.md)
   322|```
   323|
   324|## Evaluation
   325|
   326|**Docs:** Start with **[evaluation/README.md](evaluation/README.md)** (all tracks, modes, env vars). For SkillsBench + Harbor only, use **[evaluation/skillsbench/README.md](evaluation/skillsbench/README.md)**. Dataset files and scripts are described in **[DATA.md](DATA.md)**.
   327|
   328|We evaluate GoS on three benchmarks:
   329|
   330|| Benchmark | Type | Tasks |
   331||-----------|------|-------|
   332|| **ALFWorld** | Interactive household tasks | 134 games |
   333|| **SkillsBench** | Dockerized coding tasks | 87 tasks |
   334|
   335|For **running these evaluations**, we recommend routing the agent�s chat / completion API through [OpenRouter](https://openrouter.ai/): use an OpenAI-compatible `BASE_URL` (for example `https://openrouter.ai/api/v1`) and the API key your runner documents. The GoS project�s own evaluation testing is done mainly this way. Embeddings for indexing and retrieval are separate; configure them in `.env` as in [`.env.example`](.env.example) (OpenRouter, direct OpenAI, Gemini, or Azure).
   336|
   337|Benchmark data is hosted externally and **not** included in this repository:
   338|
   339|```bash
   340|./scripts/download_data.sh          # download all assets (~780 MB); options in DATA.md
   341|```
   342|
   343|Selective downloads and workspace rebuild steps: **[DATA.md](DATA.md)**.
   344|
   345|## Citation
   346|
   347|If you find this work useful, please cite:
   348|
   349|```bibtex
   350|@misc{li2026graphskillsdependencyawarestructural,
   351|      title={Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills},
   352|      author={Dawei Liu and Zongxia Li and Hongyang Du and Xiyang Wu and Shihang Gui and Yongbei Kuang and Lichao Sun},
   353|      year={2026},
   354|      eprint={2604.05333},
   355|      archivePrefix={arXiv},
   356|      primaryClass={cs.AI},
   357|      url={https://arxiv.org/abs/2604.05333},
   358|}
   359|```
   360|
   361|## License
   362|
   363|This project is licensed under the [MIT License](LICENSE).
   364|
   365|