---
language:
- en
- zh
license: other
tags:
- chat
base_model: Qwen/Qwen2-72B-Instruct
license_name: tongyi-qianwen
license_link: https://huggingface.co/Qwen/Qwen2-72B-Instruct/blob/main/LICENSE
pipeline_tag: text-generation
model-index:
- name: magnum-72b-v1
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
      value: 76.06
      name: strict accuracy
    - type: inst_level_strict_acc and prompt_level_strict_acc
      value: 76.06
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=alpindale/magnum-72b-v1
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
      value: 57.65
      name: normalized accuracy
    - type: acc_norm
      value: 57.65
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=alpindale/magnum-72b-v1
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
      value: 35.27
      name: exact match
    - type: exact_match
      value: 35.27
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=alpindale/magnum-72b-v1
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
      value: 18.79
      name: acc_norm
    - type: acc_norm
      value: 18.79
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=alpindale/magnum-72b-v1
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
      value: 15.62
      name: acc_norm
    - type: acc_norm
      value: 15.62
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=alpindale/magnum-72b-v1
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
      value: 49.64
      name: accuracy
    - type: acc
      value: 49.85
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=alpindale/magnum-72b-v1
      name: Open LLM Leaderboard
---

![](https://files.catbox.moe/ngqnb1.png)

This is the first in a series of models designed to replicate the prose quality of the Claude 3 models, specifically Sonnet and Opus. This model is fine-tuned on top of [Qwen-2 72B Instruct](https://huggingface.co/Qwen/Qwen2-72B-Instruct).


## Prompting
Model has been Instruct tuned with the ChatML formatting. A typical input would look like this:

```py
"""<|im_start|>user
Hi there!<|im_end|>
<|im_start|>assistant
Nice to meet you!<|im_end|>
<|im_start|>user
Can I ask a question?<|im_end|>
<|im_start|>assistant
"""
```

## Credits

This model has been a team effort, and the credits goes to all members of Anthracite.

We'd also like to thank [Kearm](https://twitter.com/Nottlespike) for sponsoring the compute needed to train this model.

## Training
The training was done with 55 million tokens of high-quality RP data, over 1.5 epochs. We used 8x [AMD Instinct™ MI300X Accelerators](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html) for the full-parameter fine-tuning of the model.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

## Safety
...

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_alpindale__magnum-72b-v1)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |42.17|
|IFEval (0-Shot)    |76.06|
|BBH (3-Shot)       |57.65|
|MATH Lvl 5 (4-Shot)|35.27|
|GPQA (0-shot)      |18.79|
|MuSR (0-shot)      |15.62|
|MMLU-PRO (5-shot)  |49.64|


# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_anthracite-org__magnum-v1-72b)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |42.21|
|IFEval (0-Shot)    |76.06|
|BBH (3-Shot)       |57.65|
|MATH Lvl 5 (4-Shot)|35.27|
|GPQA (0-shot)      |18.79|
|MuSR (0-shot)      |15.62|
|MMLU-PRO (5-shot)  |49.85|

