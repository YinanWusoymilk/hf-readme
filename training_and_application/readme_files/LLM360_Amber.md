---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
library_name: transformers
tags:
- nlp
- llm
---
# Amber

<center><img src="amber_logo.png" alt="amber logo" width="150"/></center>

Amber is an7B English language model with the LLaMA architecture. Amber is part of LLM360's Pebble model series.

360 model checkpoints and the full data sequence are available under the Apache 2.0 license.

## Evaluations
| Metric      | Score |
| ----------- | ----------- |
| ARC-C      | 42.57       |
| HellaSwag   | 73.91        |
| MMLU   | 28.53        |
| TruthfulQA   | 43.67        |
| WinoGrande   | 64.35        |

Amber is not a SOTA model. Amber is released to make LLM training knowledge accessible to all.

Please refer to our [W&B project page](https://wandb.ai/llm360/Amber?nw=lnzi8o2g4z) for complete training logs and evaluation results.


## Final 10 Checkpoints
| Checkpoints      |  |
| ----------- | ----------- |
| [Checkpoint 358](https://huggingface.co/LLM360/Amber/tree/ckpt_358)     | [Checkpoint 353](https://huggingface.co/LLM360/Amber/tree/ckpt_353)       |
| [Checkpoint 357](https://huggingface.co/LLM360/Amber/tree/ckpt_357)   | [Checkpoint 352](https://huggingface.co/LLM360/Amber/tree/ckpt_352)        |
| [Checkpoint 356](https://huggingface.co/LLM360/Amber/tree/ckpt_356)   | [Checkpoint 351](https://huggingface.co/LLM360/Amber/tree/ckpt_351)        |
| [Checkpoint 355](https://huggingface.co/LLM360/Amber/tree/ckpt_355)   | [Checkpoint 350](https://huggingface.co/LLM360/Amber/tree/ckpt_350)        |
| [Checkpoint 354](https://huggingface.co/LLM360/Amber/tree/ckpt_354)   | [Checkpoint 349](https://huggingface.co/LLM360/Amber/tree/ckpt_349)        |
- 360 checkpoints are available for download
- To downloading other checkpoints, change the branch from 'main' to the checkpoint you want (e.g. 'ckpt_000'). 
- This is completed on the 'Files and versions' tab (to the right of the Model Card).

## 🟠 Loading Amber 

To load a specific checkpoint, simply pass a revision with a value between `"ckpt_000"` and `"ckpt_358"`. If no revision is provided, it will load `"ckpt_359"`, which is the final checkpoint.

```python
from transformers import LlamaTokenizer, LlamaForCausalLM

tokenizer = LlamaTokenizer.from_pretrained("LLM360/Amber", revision="ckpt_356")
model = LlamaForCausalLM.from_pretrained("LLM360/Amber", revision="ckpt_356")

input_text = "translate English to German: How old are you?"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))

```

# 🟠 Amber Training Details

## Datasets and Mix
[Access the fully processed Amber pretraining data here](https://huggingface.co/datasets/LLM360/AmberDatasets)
| Subset      | Tokens (Billion) |
| ----------- | ----------- |
| Arxiv      | 30.00       |
| Book   | 28.86        |
| C4   | 197.67        |
| Refined-Web   | 665.01        |
| StarCoder   | 291.92        |
| StackExchange   | 21.75        |
| Wikipedia   | 23.90        |
| Total | 1259.13 |


## 🟠 Model Description

- **Model type:** Language model with the same architecture as LLaMA-7B
- **Language(s) (NLP):** English
- **License:** Apache 2.0
- **Resources for more information:**
  - [Training Code](https://github.com/LLM360/amber-train)
  - [Data Preparation](https://github.com/LLM360/amber-data-prep)
  - [Metrics](https://github.com/LLM360/Analysis360)
  - [Fully processed Amber pretraining data](https://huggingface.co/datasets/LLM360/AmberDatasets)

| Model Hyperparameter      | Value |
| ----------- | ----------- |
| Total Parameters      | 6.7B       |
| Hidden Size   | 4096        |
| Intermediate Size (MLPs)   | 11008        |
| Number of Attention Heads   | 32        |
| Number of Hidden Lyaers  | 32        |
| RMSNorm ɛ  | 1e^-6        |
| Max Seq Length   | 2048        |
| Vocab Size | 32000 |

## About LLM360
LLM360 is an initiative for comprehensive and fully open-sourced LLMs, 
where all training details, model checkpoints, intermediate results, and 
additional analyses are made available to the community. Our goal is to advance 
the field by inviting the community to deepen the understanding of LLMs 
together. As the first step of the project LLM360, we release all intermediate 
model checkpoints, our fully-prepared pre-training dataset, all source code and
configurations, and training details. We are
committed to continually pushing the boundaries of LLMs through this open-source 
effort.

# 🟠 Citation

**BibTeX:**

```bibtex
@misc{liu2023llm360,
      title={LLM360: Towards Fully Transparent Open-Source LLMs}, 
      author={Zhengzhong Liu and Aurick Qiao and Willie Neiswanger and Hongyi Wang and Bowen Tan and Tianhua Tao and Junbo Li and Yuqi Wang and Suqi Sun and Omkar Pangarkar and Richard Fan and Yi Gu and Victor Miller and Yonghao Zhuang and Guowei He and Haonan Li and Fajri Koto and Liping Tang and Nikhil Ranjan and Zhiqiang Shen and Xuguang Ren and Roberto Iriondo and Cun Mu and Zhiting Hu and Mark Schulze and Preslav Nakov and Tim Baldwin and Eric P. Xing},
      year={2023},
      eprint={2312.06550},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
