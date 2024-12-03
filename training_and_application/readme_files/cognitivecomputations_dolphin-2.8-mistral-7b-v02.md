---
base_model: alpindale/Mistral-7B-v0.2-hf
language:
- en
license: apache-2.0
datasets:
- cognitivecomputations/dolphin
- cognitivecomputations/dolphin-coder
- cognitivecomputations/samantha-data
- jondurbin/airoboros-2.2.1
- teknium/openhermes-2.5
- m-a-p/Code-Feedback
- m-a-p/CodeFeedback-Filtered-Instruction
model-index:
- name: dolphin-2.8-mistral-7b-v02
  results:
  - task:
      type: text-generation
    dataset:
      type: openai_humaneval
      name: HumanEval
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.469
      verified: false
---

# Dolphin 2.8 Mistral 7b v0.2 🐬

By Eric Hartford and Cognitive Computations

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/cognitivecomputations)
Discord: https://discord.gg/cognitivecomputations

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/ldkN1J0WIDQwU4vutGYiD.png" width="600" />

My appreciation for the sponsors of Dolphin 2.8:
- [Crusoe Cloud](https://crusoe.ai/) - provided excellent on-demand 10xL40S node
- [Winston Sou](https://twitter.com/WinsonDabbles) - Along with a generous anonymous sponsor, donated a massive personally owned compute resource!
- [Abacus AI](https://abacus.ai/) - my employer and partner in many things.

This model is based on [Mistral-7b-v0.2](https://huggingface.co/alpindale/Mistral-7B-v0.2-hf) a new base model released by MistralAI on March 23, 2024 but they have not yet published on HuggingFace.  Thanks to @alpindale for converting / publishing.

The base model has 32k context, and the full-weights fine-tune was with 16k sequence lengths.

It took 3 days on 10x L40S provided by [Crusoe Cloud](https://crusoe.ai/)

Dolphin-2.8 has a variety of instruction, conversational, and coding skills.

Dolphin is uncensored. I have filtered the dataset to remove alignment and bias. This makes the model more compliant. You are advised to implement your own alignment layer before exposing the model as a service. It will be highly compliant to any requests, even unethical ones. Please read my blog post about uncensored models. https://erichartford.com/uncensored-models You are responsible for any content you create using this model. Enjoy responsibly.

Dolphin is licensed Apache 2.0.  I grant permission for any use including commercial.  Dolphin was trained on data generated from GPT4 among other models.

# Evals

```
{
  "arc_challenge": {
    "acc,none": 0.5921501706484642,
    "acc_stderr,none": 0.014361097288449701,
    "acc_norm,none": 0.6339590443686007,
    "acc_norm_stderr,none": 0.014077223108470139
  },
  "gsm8k": {
    "exact_match,strict-match": 0.4783927217589083,
    "exact_match_stderr,strict-match": 0.013759618667051773,
    "exact_match,flexible-extract": 0.5367702805155421,
    "exact_match_stderr,flexible-extract": 0.013735191956468648
  },
  "hellaswag": {
    "acc,none": 0.6389165504879506,
    "acc_stderr,none": 0.004793330525656218,
    "acc_norm,none": 0.8338976299541924,
    "acc_norm_stderr,none": 0.00371411888431746
  },
  "mmlu": {
    "acc,none": 0.6122347243982339,
    "acc_stderr,none": 0.003893774654142997
  },
  "truthfulqa_mc2": {
    "acc,none": 0.5189872652778472,
    "acc_stderr,none": 0.014901128316426086
  },
  "winogrande": {
    "acc,none": 0.7971586424625099,
    "acc_stderr,none": 0.011301439925936643
  }
}
```

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.4.0`
```yaml

base_model: alpindale/Mistral-7B-v0.2-hf
model_type: MistralForCausalLM
tokenizer_type: LlamaTokenizer
is_mistral_derived_model: true

load_in_8bit: false
load_in_4bit: false
strict: false

datasets:
  - path: /workspace/datasets/dolphin201-sharegpt2.jsonl
    type: sharegpt
  - path: /workspace/datasets/dolphin-coder-translate-sharegpt2.jsonl
    type: sharegpt
  - path: /workspace/datasets/dolphin-coder-codegen-sharegpt2.jsonl
    type: sharegpt
  - path: /workspace/datasets/m-a-p_Code-Feedback-sharegpt.jsonl
    type: sharegpt
  - path: /workspace/datasets/m-a-p_CodeFeedback-Filtered-Instruction-sharegpt.jsonl
    type: sharegpt
  - path: /workspace/datasets/not_samantha_norefusals.jsonl
    type: sharegpt
  - path: /workspace/datasets/openhermes2_5-sharegpt.jsonl
    type: sharegpt

chat_template: chatml

dataset_prepared_path: last_run_prepared
val_set_size: 0.001
output_dir: /workspace/dolphin-2.8-mistral-7b

sequence_len: 16384
sample_packing: true
pad_to_sequence_len: true

wandb_project: dolphin
wandb_entity:
wandb_watch:
wandb_run_id:
wandb_log_model:

gradient_accumulation_steps: 8
micro_batch_size: 3
num_epochs: 4
adam_beta2: 0.95
adam_epsilon: 0.00001
max_grad_norm: 1.0
lr_scheduler: cosine
learning_rate: 0.000005
optimizer: adamw_bnb_8bit

train_on_inputs: false
group_by_length: false
bf16: true
fp16: false
tf32: false

gradient_checkpointing: true
gradient_checkpointing_kwargs:
  use_reentrant: true
early_stopping_patience:
resume_from_checkpoint:
local_rank:
logging_steps: 1
xformers_attention:
flash_attention: true

warmup_steps: 10

eval_steps: 73
eval_table_size:
eval_table_max_new_tokens:
eval_sample_packing: false
saves_per_epoch: 
save_steps: 73
save_total_limit: 2
debug:
deepspeed: deepspeed_configs/zero3_bf16.json
weight_decay: 0.1
fsdp:
fsdp_config:
special_tokens:
  eos_token: "<|im_end|>"
tokens:
  - "<|im_start|>"

```

</details><br>

# workspace/dolphin-2.8-mistral-7b

This model is a fine-tuned version of [alpindale/Mistral-7B-v0.2-hf](https://huggingface.co/alpindale/Mistral-7B-v0.2-hf) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4828

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 3
- eval_batch_size: 3
- seed: 42
- distributed_type: multi-GPU
- num_devices: 10
- gradient_accumulation_steps: 8
- total_train_batch_size: 240
- total_eval_batch_size: 30
- optimizer: Adam with betas=(0.9,0.95) and epsilon=1e-05
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 10
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.1736        | 0.0   | 1    | 1.0338          |
| 0.6106        | 0.36  | 73   | 0.5439          |
| 0.5766        | 0.72  | 146  | 0.5171          |
| 0.5395        | 1.06  | 219  | 0.5045          |
| 0.5218        | 1.42  | 292  | 0.4976          |
| 0.5336        | 1.78  | 365  | 0.4915          |
| 0.5018        | 2.13  | 438  | 0.4885          |
| 0.5113        | 2.48  | 511  | 0.4856          |
| 0.5066        | 2.84  | 584  | 0.4838          |
| 0.4967        | 3.19  | 657  | 0.4834          |
| 0.4956        | 3.55  | 730  | 0.4830          |
| 0.5026        | 3.9   | 803  | 0.4828          |


### Framework versions

- Transformers 4.40.0.dev0
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.0


# Quants

- [dagbs/-GGUF](https://huggingface.co/dagbs/dolphin-2.8-mistral-7b-v02-GGUF)

- [bartowski/ExLlamaV2](https://huggingface.co/bartowski/dolphin-2.8-mistral-7b-v02-exl2)

- [solidrust/AWQ](https://huggingface.co/solidrust/dolphin-2.8-mistral-7b-v02-AWQ)