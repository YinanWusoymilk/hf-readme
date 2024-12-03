---
license: llama3.1
library_name: transformers
tags:
- abliterated
- uncensored
base_model: meta-llama/Meta-Llama-3.1-8B-Instruct
model-index:
- name: Meta-Llama-3.1-8B-Instruct-abliterated
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
      value: 73.29
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated
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
      value: 27.13
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated
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
      value: 6.42
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated
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
      value: 0.89
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated
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
      value: 3.21
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated
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
      value: 27.81
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated
      name: Open LLM Leaderboard
---

# 🦙 Meta-Llama-3.1-8B-Instruct-abliterated

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/AsTgL8VCgMHgobq4cr46b.png)

<center>🦙 <a href="https://huggingface.co/mlabonne/Llama-3.1-70B-Instruct-lorablated"><i>Llama 3.1 70B Instruct lorablated</i></a></center>

This is an uncensored version of Llama 3.1 8B Instruct created with abliteration (see [this article](https://huggingface.co/blog/mlabonne/abliteration) to know more about it).

Special thanks to [@FailSpy](https://huggingface.co/failspy) for the original code and technique. Please follow him if you're interested in abliterated models.

## ⚡️ Quantization

Thanks to ZeroWw and Apel-sin for the quants.

* **New GGUF**: https://huggingface.co/mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF
* **ZeroWw GGUF**: https://huggingface.co/ZeroWw/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF
* **EXL2**: https://huggingface.co/Apel-sin/llama-3.1-8B-abliterated-exl2
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_mlabonne__Meta-Llama-3.1-8B-Instruct-abliterated)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |23.13|
|IFEval (0-Shot)    |73.29|
|BBH (3-Shot)       |27.13|
|MATH Lvl 5 (4-Shot)| 6.42|
|GPQA (0-shot)      | 0.89|
|MuSR (0-shot)      | 3.21|
|MMLU-PRO (5-shot)  |27.81|

