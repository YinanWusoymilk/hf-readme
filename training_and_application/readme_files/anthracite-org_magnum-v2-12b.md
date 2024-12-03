---
language:
- en
- fr
- de
- es
- it
- pt
- ru
- zh
- ja
license: apache-2.0
tags:
- chat
base_model: mistralai/Mistral-Nemo-Base-2407
pipeline_tag: text-generation
model-index:
- name: magnum-v2-12b
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
      value: 37.62
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=anthracite-org/magnum-v2-12b
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
      value: 28.79
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=anthracite-org/magnum-v2-12b
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
      value: 4.76
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=anthracite-org/magnum-v2-12b
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
      value: 5.48
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=anthracite-org/magnum-v2-12b
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
      value: 11.37
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=anthracite-org/magnum-v2-12b
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
      value: 24.08
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=anthracite-org/magnum-v2-12b
      name: Open LLM Leaderboard
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/658a46cbfb9c2bdfae75b3a6/A9n8EJBDQziJWnXhOYeEE.png)

This is the fourth in a series of models designed to replicate the prose quality of the Claude 3 models, specifically Sonnet and Opus. This model is fine-tuned on top of [Mistral-Nemo-Base-2407](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407).

## Prompting
Model has been Instruct tuned with the ChatML formatting. A typical input would look like this:

```py
"""<|im_start|>system
system prompt<|im_end|>
<|im_start|>user
Hi there!<|im_end|>
<|im_start|>assistant
Nice to meet you!<|im_end|>
<|im_start|>user
Can I ask a question?<|im_end|>
<|im_start|>assistant
"""
```

## Credits
- Stheno dataset (filtered)
- [kalomaze/Opus_Instruct_25k](https://huggingface.co/datasets/kalomaze/Opus_Instruct_25k)
- [Nopm/Opus_WritingStruct](https://huggingface.co/datasets/Nopm/Opus_WritingStruct)
- [Gryphe/Sonnet3.5-SlimOrcaDedupCleaned](https://huggingface.co/datasets/Gryphe/Sonnet3.5-SlimOrcaDedupCleaned) (A ~16k rows subset)
- [kalomaze/Opus_Instruct_3k](https://huggingface.co/datasets/kalomaze/Opus_Instruct_3k)

This model has been a team effort, and the credits goes to all members of Anthracite.

## Training
The training was done for 2 epochs. We used 8x [NVIDIA H100 Tensor Core](https://www.nvidia.com/en-us/data-center/h100/) GPUs for the full-parameter fine-tuning of the model.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

## Safety
...
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_anthracite-org__magnum-v2-12b)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |18.68|
|IFEval (0-Shot)    |37.62|
|BBH (3-Shot)       |28.79|
|MATH Lvl 5 (4-Shot)| 4.76|
|GPQA (0-shot)      | 5.48|
|MuSR (0-shot)      |11.37|
|MMLU-PRO (5-shot)  |24.08|

