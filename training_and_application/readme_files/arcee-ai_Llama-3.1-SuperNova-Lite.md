---
language:
- en
license: llama3
library_name: transformers
base_model: meta-llama/Meta-Llama-3.1-8B-Instruct
datasets:
- arcee-ai/EvolKit-20k
model-index:
- name: Llama-3.1-SuperNova-Lite
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: IFEval (0-Shot)
      type: HuggingFaceH4/ifeval
      args:
        num_few_shot: 0
    metrics:
    - type: inst_level_strict_acc and prompt_level_strict_acc
      value: 80.17
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=arcee-ai/Llama-3.1-SuperNova-Lite
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: BBH (3-Shot)
      type: BBH
      args:
        num_few_shot: 3
    metrics:
    - type: acc_norm
      value: 31.57
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=arcee-ai/Llama-3.1-SuperNova-Lite
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MATH Lvl 5 (4-Shot)
      type: hendrycks/competition_math
      args:
        num_few_shot: 4
    metrics:
    - type: exact_match
      value: 15.48
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=arcee-ai/Llama-3.1-SuperNova-Lite
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GPQA (0-shot)
      type: Idavidrein/gpqa
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 7.49
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=arcee-ai/Llama-3.1-SuperNova-Lite
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MuSR (0-shot)
      type: TAUR-Lab/MuSR
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 11.67
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=arcee-ai/Llama-3.1-SuperNova-Lite
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU-PRO (5-shot)
      type: TIGER-Lab/MMLU-Pro
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 31.97
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=arcee-ai/Llama-3.1-SuperNova-Lite
      name: Open LLM Leaderboard
---
<div align="center">
  <img src="https://i.ibb.co/r072p7j/eopi-ZVu-SQ0-G-Cav78-Byq-Tg.png" alt="Llama-3.1-SuperNova-Lite" style="border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); max-width: 100%; height: auto;">
</div>

## Overview

Llama-3.1-SuperNova-Lite is an 8B parameter model developed by Arcee.ai, based on the Llama-3.1-8B-Instruct architecture. It is a distilled version of the larger Llama-3.1-405B-Instruct model, leveraging offline logits extracted from the 405B parameter variant. This 8B variation of Llama-3.1-SuperNova maintains high performance while offering exceptional instruction-following capabilities and domain-specific adaptability. 

The model was trained using a state-of-the-art distillation pipeline and an instruction dataset generated with [EvolKit](https://github.com/arcee-ai/EvolKit), ensuring accuracy and efficiency across a wide range of tasks. For more information on its training, visit blog.arcee.ai. 

Llama-3.1-SuperNova-Lite excels in both benchmark performance and real-world applications, providing the power of large-scale models in a more compact, efficient form ideal for organizations seeking high performance with reduced resource requirements.

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_arcee-ai__Llama-3.1-SuperNova-Lite)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |29.73|
|IFEval (0-Shot)    |80.17|
|BBH (3-Shot)       |31.57|
|MATH Lvl 5 (4-Shot)|15.48|
|GPQA (0-shot)      | 7.49|
|MuSR (0-shot)      |11.67|
|MMLU-PRO (5-shot)  |31.97|

