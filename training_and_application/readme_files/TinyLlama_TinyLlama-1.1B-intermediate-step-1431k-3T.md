---
language:
- en
license: apache-2.0
datasets:
- cerebras/SlimPajama-627B
- bigcode/starcoderdata
model-index:
- name: TinyLlama-1.1B-intermediate-step-1431k-3T
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: AI2 Reasoning Challenge (25-Shot)
      type: ai2_arc
      config: ARC-Challenge
      split: test
      args:
        num_few_shot: 25
    metrics:
    - type: acc_norm
      value: 33.87
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: HellaSwag (10-Shot)
      type: hellaswag
      split: validation
      args:
        num_few_shot: 10
    metrics:
    - type: acc_norm
      value: 60.31
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU (5-Shot)
      type: cais/mmlu
      config: all
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 26.04
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: TruthfulQA (0-shot)
      type: truthful_qa
      config: multiple_choice
      split: validation
      args:
        num_few_shot: 0
    metrics:
    - type: mc2
      value: 37.32
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: Winogrande (5-shot)
      type: winogrande
      config: winogrande_xl
      split: validation
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 59.51
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GSM8k (5-shot)
      type: gsm8k
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 1.44
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
      name: Open LLM Leaderboard
---
<div align="center">

# TinyLlama-1.1B
</div>

https://github.com/jzhang38/TinyLlama

The TinyLlama project aims to **pretrain** a **1.1B Llama model on 3 trillion tokens**. With some proper optimization, we can achieve this within a span of "just" 90 days using 16 A100-40G GPUs 🚀🚀. The training has started on 2023-09-01. 

<div align="center">
  <img src="./TinyLlama_logo.png" width="300"/>
</div>

We adopted exactly the same architecture and tokenizer as Llama 2. This means TinyLlama can be plugged and played in many open-source projects built upon Llama. Besides, TinyLlama is compact with only 1.1B parameters. This compactness allows it to cater to a multitude of applications demanding a restricted computation and memory footprint.

#### This Collection
This collection contains all checkpoints after the 1T fix. Branch name indicates the step and number of tokens seen.

#### Eval

| Model                                     | Pretrain Tokens | HellaSwag | Obqa | WinoGrande | ARC_c | ARC_e | boolq | piqa | avg |
|-------------------------------------------|-----------------|-----------|------|------------|-------|-------|-------|------|-----|
| Pythia-1.0B                               |        300B     | 47.16     | 31.40| 53.43      | 27.05 | 48.99 | 60.83 | 69.21 | 48.30 |
| TinyLlama-1.1B-intermediate-step-50K-104b |        103B     | 43.50     | 29.80| 53.28      | 24.32 | 44.91 | 59.66 | 67.30 | 46.11|
| TinyLlama-1.1B-intermediate-step-240k-503b|        503B     | 49.56     |31.40 |55.80       |26.54  |48.32  |56.91  |69.42  | 48.28 |
| TinyLlama-1.1B-intermediate-step-480k-1007B |     1007B     | 52.54     | 33.40 | 55.96      | 27.82 | 52.36 | 59.54 | 69.91 | 50.22 |
| TinyLlama-1.1B-intermediate-step-715k-1.5T |     1.5T     | 53.68     | 35.20 | 58.33      | 29.18 | 51.89 | 59.08 | 71.65 | 51.29 |
| TinyLlama-1.1B-intermediate-step-955k-2T |     2T     | 54.63     | 33.40 | 56.83      | 28.07 | 54.67 | 63.21 | 70.67 | 51.64 |
| TinyLlama-1.1B-intermediate-step-1195k-2.5T              |     2.5T     | 58.96     | 34.40 | 58.72      | 31.91 | 56.78 | 63.21 | 73.07 | 53.86|
| TinyLlama-1.1B-intermediate-step-1431k-3T |     3T     | 59.20     | 36.00 | 59.12      | 30.12 | 55.25 | 57.83 | 73.29 | 52.99|
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_TinyLlama__TinyLlama-1.1B-intermediate-step-1431k-3T)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |36.42|
|AI2 Reasoning Challenge (25-Shot)|33.87|
|HellaSwag (10-Shot)              |60.31|
|MMLU (5-Shot)                    |26.04|
|TruthfulQA (0-shot)              |37.32|
|Winogrande (5-shot)              |59.51|
|GSM8k (5-shot)                   | 1.44|

