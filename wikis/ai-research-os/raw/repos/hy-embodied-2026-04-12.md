---
status: processed
---
     1|---
     2|source: https://github.com/Tencent-Hunyuan/HY-Embodied
     3|date: 2026-04-12
     4|type: repo
     5|tags: [embodied-ai, vlm, vision-language-model, robotics, mixture-of-transformers, tencent]
     6|status: raw
     7|---
     8|
     9|<div align="center">
    10|<h1>HY-Embodied</h1>
    11|<p><b>A Family of Embodied Foundation Models for Real-World Agents</b></p>
    12|<p><i>Tencent Robotics X � HY Vision Team</i></p>
    13|
    14|<a href="hy_embodied_tech_report.pdf"><img src="https://img.shields.io/badge/PDF-Report-green?logo=report" alt="Tech Report"></a>
    15|<a href="https://arxiv.org/abs/2604.07430"><img src="https://img.shields.io/badge/Paper-arXiv-red?logo=report" alt="arXiv"></a>
    16|<a href="https://huggingface.co/tencent/HY-Embodied-0.5/tree/main"><img src="https://img.shields.io/badge/Models-HuggingFace-yellow?logo=huggingface" alt="Models"></a>
    17|
    18|</div>
    19|
    20|https://github.com/user-attachments/assets/a5c6b872-2cb0-4f52-8321-894fee7da27e
    21|
    22|## ? Updates
    23|
    24|  * **`[2026-04-09]`** ? We have released **HY-Embodied-0.5**, featuring the open-sourced `HY-Embodied-0.5 MoT-2B` weights on [Hugging Face](https://huggingface.co/tencent/HY-Embodied-0.5/tree/main) along with the official inference code\!
    25|
    26|## ? Abstract
    27|
    28|We introduce **HY-Embodied-0.5**, a suite of foundation models tailored specifically for real-world embodied intelligence. To bridge the gap between general Vision-Language Models (VLMs) and the strict demands of physical agents, our models are engineered to excel in spatial-temporal visual perception and complex embodied reasoning (prediction, interaction, and planning).
    29|
    30|The suite features an innovative **Mixture-of-Transformers (MoT)** architecture utilizing latent tokens for modality-specific computing, significantly enhancing fine-grained perception. It includes two primary variants: a highly efficient **2B model** for edge deployment and a powerful **32B model** for complex reasoning. Through a self-evolving post-training paradigm and large-to-small on-policy distillation, our compact MoT-2B outperforms state-of-the-art models of similar size across 16 benchmarks, while the 32B variant achieves frontier-level performance comparable to Gemini 3.0 Pro. Ultimately, HY-Embodied serves as a robust "brain" for Vision-Language-Action (VLA) pipelines, delivering compelling results in real-world physical robot control.
    31|
    32|<div align="center">
    33|<img src="figures/teaser.png" alt="HY-Embodied Teaser" width="85%">
    34|</div>
    35|
    36|## ?? Key Features
    37|
    38|  * ? **Evolved MoT Architecture:** Designed for maximum efficiency without sacrificing visual acuity. The MoT-2B variant contains 4B total parameters but requires **only 2.2B activated parameters** during inference. By emphasizing modality-specific computing in the vision pathway, it achieves the high inference speed of a dense 2B model while delivering superior, fine-grained perceptual representations.
    39|  * ? **High-Quality Mixed Chain Reasoning:** We introduce an advanced iterative, self-evolving post-training pipeline. By employing on-policy distillation, we successfully transfer the sophisticated step-by-step reasoning, planning, and high-quality "thinking" capabilities from our powerful 32B model directly to the compact 2B variant.
    40|  * ? **Large-Scale Embodied Pre-training:** Grounded in a massive, specially curated dataset comprising **\>100 million** embodied and spatial-specific data points. Trained on a corpus exceeding **200 billion tokens**, the model develops a deep, native understanding of 3D spaces, physical object interactions, and agent dynamics.
    41|  * ? **Stronger VLA Application:** Beyond standard academic benchmarks, HY-Embodied is engineered to be the core cognitive engine for physical robots. It seamlessly integrates into Vision-Language-Action (VLA) frameworks, acting as a highly robust and capable brain to drive high success rates in complex, real-world robotic control tasks.
    42|
    43|<div align="center">
    44|<img src="figures/arch.png" alt="HY-Embodied Architecture" width="85%">
    45|</div>
    46|
    47|## ? Plannings
    48|
    49|- [x] Transformers Inference
    50|- [ ] vLLM Inference
    51|- [ ] Online Gradio Demo
    52|
    53|## ?? Dependencies and Installation
    54|
    55|### Prerequisites
    56|
    57|- ?? **Operating System**: Linux (recommended)
    58|- ? **Python**: 3.12+ (recommended and tested)
    59|- ? **CUDA**: 12.6
    60|- ? **PyTorch**: 2.8.0
    61|- ? **GPU**: NVIDIA GPU with CUDA support
    62|
    63|### Installation
    64|
    65|1. **Install the specific Transformers version required for this model:**
    66|```bash
    67|pip install git+https://github.com/huggingface/transformers@9293856c419762ebf98fbe2bd9440f9ce7069f1a
    68|```
    69|
    70|> **Note**: We will merge the improvements into the Transformers main branch later.
    71|
    72|2. **Install other dependencies:**
    73|```bash
    74|pip install -r requirements.txt
    75|```
    76|
    77|### Quick Start
    78|
    79|1. **Clone the repository:**
    80|```bash
    81|git clone https://github.com/Tencent-Hunyuan/HY-Embodied
    82|cd HY-Embodied/
    83|```
    84|
    85|2. **Install dependencies:**
    86|```bash
    87|pip install -r requirements.txt
    88|```
    89|
    90|3. **Run inference:**
    91|```bash
    92|python inference.py
    93|```
    94|
    95|The example script demonstrates both single generation and batch generation capabilities.
    96|
    97|### Model Download
    98|
    99|The code automatically downloads the model `tencent/HY-Embodied-0.5` from Hugging Face Hub. Ensure you have sufficient disk space (8 GB) for the model weights.
   100|
   101|### Hardware Requirements
   102|
   103|- **GPU**: Recommended for optimal performance (NVIDIA GPU with at least 16GB VRAM)
   104|- **CPU**: Supported but slower
   105|- **Memory**: At least 16GB RAM recommended
   106|- **Storage**: 20GB+ free space for model and dependencies
   107|
   108|## ? Quick Start with Transformers
   109|
   110|### Basic Inference Example
   111|
   112|```python
   113|import os
   114|import torch
   115|from transformers import AutoModelForImageTextToText, AutoProcessor
   116|
   117|# Load model & processor
   118|MODEL_PATH = "tencent/HY-Embodied-0.5"
   119|DEVICE = "cuda"
   120|THINKING_MODE = False
   121|TEMPERATURE = 0.8
   122|
   123|processor = AutoProcessor.from_pretrained(MODEL_PATH)
   124|
   125|# Load chat template if available
   126|chat_template_path = os.path.join(MODEL_PATH, "chat_template.jinja")
   127|if os.path.exists(chat_template_path):
   128|    processor.chat_template = open(chat_template_path).read()
   129|
   130|model = AutoModelForImageTextToText.from_pretrained(MODEL_PATH, torch_dtype=torch.bfloat16)
   131|model.to(DEVICE).eval()
   132|
   133|# Prepare input messages
   134|messages = [
   135|    {
   136|        "role": "user",
   137|        "content": [
   138|            {"type": "image", "image": "./figures/example.jpg"},
   139|            {"type": "text", "text": "Describe the image in detail."},
   140|        ],
   141|    }
   142|]
   143|
   144|# Process and generate
   145|inputs = processor.apply_chat_template(
   146|    messages,
   147|    tokenize=True,
   148|    add_generation_prompt=True,
   149|    return_dict=True,
   150|    return_tensors="pt",
   151|    enable_thinking=THINKING_MODE,
   152|).to(model.device)
   153|
   154|with torch.no_grad():
   155|    generated_ids = model.generate(
   156|        **inputs,
   157|        max_new_tokens=32768,
   158|        use_cache=True,
   159|        temperature=TEMPERATURE,
   160|        do_sample=TEMPERATURE > 0,
   161|    )
   162|
   163|output_ids = [out[len(inp):] for inp, out in zip(inputs.input_ids, generated_ids)]
   164|print(processor.batch_decode(output_ids, skip_special_tokens=True)[0])
   165|```
   166|
   167|### Batch Inference
   168|
   169|```python
   170|import os
   171|import torch
   172|from transformers import AutoModelForImageTextToText, AutoProcessor
   173|
   174|# Load model & processor
   175|MODEL_PATH = "tencent/HY-Embodied-0.5"
   176|DEVICE = "cuda"
   177|THINKING_MODE = False
   178|TEMPERATURE = 0.8
   179|
   180|processor = AutoProcessor.from_pretrained(MODEL_PATH)
   181|
   182|# Load chat template if available
   183|chat_template_path = os.path.join(MODEL_PATH, "chat_template.jinja")
   184|if os.path.exists(chat_template_path):
   185|    processor.chat_template = open(chat_template_path).read()
   186|
   187|model = AutoModelForImageTextToText.from_pretrained(MODEL_PATH, torch_dtype=torch.bfloat16)
   188|model.to(DEVICE).eval()
   189|
   190|# Batch Inference (multiple prompts at once)
   191|messages_batch = [
   192|    # Sample A: image + text
   193|    [
   194|        {
   195|            "role": "user",
   196|            "content": [
   197|                {"type": "image", "image": "./figures/example.jpg"},
   198|                {"type": "text", "text": "Describe the image in detail."},
   199|            ],
   200|        }
   201|    ],
   202|    # Sample B: text only
   203|    [
   204|        {
   205|            "role": "user",
   206|            "content": [
   207|                {"type": "text", "text": "How to open a fridge?"},
   208|            ],
   209|        }
   210|    ],
   211|]
   212|
   213|# Process each message independently
   214|all_inputs = []
   215|for msgs in messages_batch:
   216|    inp = processor.apply_chat_template(
   217|        msgs,
   218|        tokenize=True,
   219|        add_generation_prompt=True,
   220|        return_dict=True,
   221|        return_tensors="pt",
   222|        enable_thinking=THINKING_MODE,
   223|    )
   224|    all_inputs.append(inp)
   225|
   226|# Left-pad and batch
   227|batch = processor.pad(all_inputs, padding=True, padding_side="left").to(model.device)
   228|
   229|with torch.no_grad():
   230|    batch_generated_ids = model.generate(
   231|        **batch,
   232|        max_new_tokens=32768,
   233|        use_cache=True,
   234|        temperature=TEMPERATURE,
   235|        do_sample=TEMPERATURE > 0,
   236|    )
   237|
   238|# Decode: strip the padded input portion
   239|padded_input_len = batch["input_ids"].shape[1]
   240|for i, msgs in enumerate(messages_batch):
   241|    out_ids = batch_generated_ids[i][padded_input_len:]
   242|    print(f"\n--- Sample {i} ---")
   243|    print(processor.decode(out_ids, skip_special_tokens=True))
   244|```
   245|
   246|## ? Evaluation
   247|
   248|### Visual Perception
   249|
   250|> **Note**: We evaluated HY-Embodied-0.5 MoT-2B across 22 embodied-relevant benchmarks against models of similar size. For detailed performance metrics and methodology, please refer to our technical report.
   251|
   252|| Benchmark | HY-Embodied 0.5 MoT-2B | Qwen3-VL 2B | Qwen3-VL 4B | RoboBrain 2.5 4B | MiMo-Embodied 7B |
   253||-----------|------------------------|-------------|-------------|------------------|------------------|
   254|| CV-Bench  | **89.2** | 80.0 | 85.7 | 86.9 | 88.8 |
   255|| DA-2K     | **92.3** | 69.5 | 76.5 | 79.4 | 72.2 |
   256|
   257|### Embodied Understanding
   258|
   259|| Benchmark | HY-Embodied 0.5 MoT-2B | Qwen3-VL 2B | Qwen3-VL 4B | RoboBrain 2.5 4B | MiMo-Embodied 7B |
   260||-----------|------------------------|-------------|-------------|------------------|------------------|
   261|| ERQA | **54.5** | 41.8 | 47.3 | 43.3 | 46.8 |
   262|| EmbSpatial-Bench | **82.8** | 75.9 | 80.7 | 73.8 | 76.2 |
   263|| RoboBench-MCQ | **49.2** | 36.9 | 45.8 | 44.4 | 43.6 |
   264|| RoboBench-Planning | 54.2 | 36.2 | 36.4 | 39.2 | **58.7** |
   265|| RoboSpatial-Home | 55.7 | 45.3 | **63.2** | 62.3 | 61.8 |
   266|| ShareRobot-Aff. | **26.8** | 19.8 | 25.5 | 25.5 | 9.0 |
   267|| ShareRobot-Traj. | 73.3 | 41.6 | 62.2 | **81.4** | 50.6 |
   268|| Ego-Plan2 | 45.5 | 35.5 | 38.8 | **52.6** | 39.9 |
   269|
   270|### Spatial Understanding
   271|
   272|| Benchmark | HY-Embodied 0.5 MoT-2B | Qwen3-VL 2B | Qwen3-VL 4B | RoboBrain 2.5 4B | MiMo-Embodied 7B |
   273||-----------|------------------------|-------------|-------------|------------------|------------------|
   274|| 3DSRBench | **57.0** | 39.9 | 43.9 | 44.8 | 42.0 |
   275|| All-Angles Bench | **55.1** | 42.3 | 46.7 | 43.8 | 49.0 |
   276|| MindCube | **66.3** | 28.4 | 31.0 | 26.9 | 36.2 |
   277|| MMSI-Bench | **33.2** | 23.6 | 25.1 | 20.5 | 31.9 |
   278|| RefSpatial-Bench | 45.8 | 28.9 | 45.3 | **56.0** | 48.0 |
   279|| SAT | 76.7 | 45.3 | 56.7 | 51.3 | **78.7** |
   280|| SIBench-mini | **58.2** | 42.0 | 50.9 | 47.3 | 53.1 |
   281|| SITE-Bench-Image | **62.7** | 52.3 | 61.0 | 57.9 | 49.9 |
   282|| SITE-Bench-Video | **63.5** | 52.2 | 58.0 | 54.8 | 58.9 |
   283|| ViewSpatial | **53.1** | 37.2 | 41.6 | 36.6 | 36.1 |
   284|| VSIBench | **60.5** | 48.0 | 55.2 | 41.7 | 48.5 |
   285|| Where2Place | **68.0** | 45.0 | 59.0 | 65.0 | 63.6 |
   286|
   287|*Note: Results for HY-Embodied-0.5 MoT-2B are reported in thinking mode, while for all other models, we report the better performance between non-thinking and thinking modes.*
   288|
   289|## ? Citation
   290|
   291|If you find it useful for your research and applications, please cite our paper using this BibTeX:
   292|```bibtex
   293|@article{tencent2026hyembodied05,
   294|title={HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents},
   295|author={Tencent Robotics X and HY Vision Team},
   296|journal={arXiv preprint arXiv:2604.07430},
   297|year={2026}
   298|}
   299|```
   300|
   301|## ? Acknowledgements
   302|
   303|We thank the Hugging Face community for their support and the open-source contributions that made this implementation possible.
   304|
   305|