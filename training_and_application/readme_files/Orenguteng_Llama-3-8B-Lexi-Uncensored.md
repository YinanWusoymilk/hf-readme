---
license: llama3
tags:
- uncensored
- llama3
- instruct
- open
model-index:
- name: Llama-3-8B-Lexi-Uncensored
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
      value: 59.56
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Orenguteng/Llama-3-8B-Lexi-Uncensored
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
      value: 77.88
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Orenguteng/Llama-3-8B-Lexi-Uncensored
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
      value: 67.68
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Orenguteng/Llama-3-8B-Lexi-Uncensored
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
      value: 47.72
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Orenguteng/Llama-3-8B-Lexi-Uncensored
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
      value: 75.85
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Orenguteng/Llama-3-8B-Lexi-Uncensored
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
      value: 68.39
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Orenguteng/Llama-3-8B-Lexi-Uncensored
      name: Open LLM Leaderboard
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/644ad182f434a6a63b18eee6/H6axm5mlmiOWnbIFvx_em.png)

This model is based on Llama-3-8b-Instruct, and is governed by [META LLAMA 3 COMMUNITY LICENSE AGREEMENT](https://llama.meta.com/llama3/license/)

Lexi is uncensored, which makes the model compliant. You are advised to implement your own alignment layer before exposing the model as a service. It will be highly compliant with any requests, even unethical ones. 

You are responsible for any content you create using this model. Please use it responsibly.

Lexi is licensed according to Meta's Llama license. I grant permission for any use, including commercial, that falls within accordance with Meta's Llama-3 license.

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Orenguteng__Llama-3-8B-Lexi-Uncensored)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |66.18|
|AI2 Reasoning Challenge (25-Shot)|59.56|
|HellaSwag (10-Shot)              |77.88|
|MMLU (5-Shot)                    |67.68|
|TruthfulQA (0-shot)              |47.72|
|Winogrande (5-shot)              |75.85|
|GSM8k (5-shot)                   |68.39|

