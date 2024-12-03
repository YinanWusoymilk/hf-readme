---
language:
- en
license: apache-2.0
datasets:
- openbmb/UltraFeedback
pipeline_tag: text-generation
model-index:
- name: Llama-3-Instruct-8B-SPPO-Iter3
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
      value: 68.28
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter3
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
      value: 29.74
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter3
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
      value: 7.33
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter3
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
      value: 2.01
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter3
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
      value: 3.09
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter3
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
      value: 29.38
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter3
      name: Open LLM Leaderboard
---
Self-Play Preference Optimization for Language Model Alignment (https://arxiv.org/abs/2405.00675)

# Llama-3-Instruct-8B-SPPO-Iter3

This model was developed using [Self-Play Preference Optimization](https://arxiv.org/abs/2405.00675) at iteration 3, based on the [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) architecture as starting point. We utilized the prompt sets from the [openbmb/UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback) dataset, splited to 3 parts for 3 iterations by [snorkelai/Snorkel-Mistral-PairRM-DPO-Dataset](https://huggingface.co/datasets/snorkelai/Snorkel-Mistral-PairRM-DPO-Dataset). All responses used are synthetic.


## Links to Other Models
- [Llama-3-Instruct-8B-SPPO-Iter1](https://huggingface.co/UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter1)
- [Llama-3-Instruct-8B-SPPO-Iter2](https://huggingface.co/UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter2)
- [Llama-3-Instruct-8B-SPPO-Iter3](https://huggingface.co/UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter3)

### Model Description

- Model type: A 8B parameter GPT-like model fine-tuned on synthetic datasets.
- Language(s) (NLP): Primarily English
- License: Apache-2.0
- Finetuned from model: meta-llama/Meta-Llama-3-8B-Instruct


## [AlpacaEval Leaderboard Evaluation Results](https://tatsu-lab.github.io/alpaca_eval/)


|                Model                           | LC. Win Rate | Win Rate | Avg. Length |
|-------------------------------------------|:------------:|:--------:|:-----------:|
|[Llama-3-8B-SPPO Iter1](https://huggingface.co/UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter1) |31.73 |31.74 | 1962
|[Llama-3-8B-SPPO Iter2](https://huggingface.co/UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter2) |35.15 |35.98 | 2021
|[Llama-3-8B-SPPO Iter3](https://huggingface.co/UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter3) |**38.77** |**39.85** | 2066



## [Open LLM Leaderboard Evaluation Results](https://github.com/EleutherAI/lm-evaluation-harness)

Results are reported by using [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) v0.4.1

|        | arc_challenge | truthfulqa_mc2 | winogrande | gsm8k | hellaswag | mmlu  | average |
|--------|---------------|----------------|------------|-------|-----------|-------|---------|
|[Llama-3-8B-SPPO Iter1](https://huggingface.co/UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter1) | 63.82 | 54.96 | 76.40 | 75.44 | 79.80 | 65.65 | 69.35
|[Llama-3-8B-SPPO Iter2](https://huggingface.co/UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter2) | 64.93 | 56.48 | 76.87 | 75.13 | 80.39 | 65.67 | 69.91
|[Llama-3-8B-SPPO Iter3](https://huggingface.co/UCLA-AGI/Llama-3-Instruct-8B-SPPO-Iter3) | 65.19 | 58.04 | 77.11 | 74.91 | 80.86 | 65.60 | **70.29**


# [Open LLM Leaderboard 2 Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/UCLA-AGI__Llama-3-Instruct-8B-SPPO-Iter3-details)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |23.68|
|IFEval (0-Shot)    |68.28|
|BBH (3-Shot)       |29.74|
|MATH Lvl 5 (4-Shot)| 7.33|
|GPQA (0-shot)      | 2.01|
|MuSR (0-shot)      | 3.09|
|MMLU-PRO (5-shot)  |29.38|


### Training hyperparameters
The following hyperparameters were used during training:

- learning_rate: 5e-07
- eta: 1000
- per_device_train_batch_size: 8
- gradient_accumulation_steps: 1
- seed: 42
- distributed_type: deepspeed_zero3
- num_devices: 8
- optimizer: RMSProp 
- lr_scheduler_type: linear 
- lr_scheduler_warmup_ratio: 0.1
- num_train_epochs: 6.0 (stop at epoch=1.0)



  
## Citation
```
@misc{wu2024self,
      title={Self-Play Preference Optimization for Language Model Alignment}, 
      author={Wu, Yue and Sun, Zhiqing and Yuan, Huizhuo and Ji, Kaixuan and Yang, Yiming and Gu, Quanquan},
      year={2024},
      eprint={2405.00675},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```

