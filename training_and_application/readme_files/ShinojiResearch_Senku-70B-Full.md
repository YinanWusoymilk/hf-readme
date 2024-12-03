---
license: cc0-1.0
library_name: peft
tags:
- generated_from_trainer
datasets:
- Open-Orca/SlimOrca
base_model: 152334H/miqu-1-70b-sf
model-index:
- name: Senku-70B-Full
  results: []
---

# ShinojiResearch/Senku-70B-Full

[<img src="https://cdna.artstation.com/p/assets/images/images/034/109/324/large/bella-factor-senku-ishigami.jpg?1611427638" width="420">](Senku-70B-Full)
## UPDATE: **85.09** EQ-Bench with ChatML teamplate
* EQ-Bench: (Mistral) *84.89* -> **85.09** (ChatML)
* GSM8k: (Mistral) *77.18* -> **71.04** (ChatML)
* Hellaswag: (Mistral) 87.67 -> ??

Finetune of miqu-70b-sf dequant of miqudev's leak of Mistral-70B (allegedly an early mistral medium). My diffs are available under CC-0 (That is the Senku-70B repo, full includes the merge), this is a merge with the leaked model, you can use the other repository to save bandwidth.

**Update**: Upon further testing a score of **85.09** was achieved using ChatML instead of Mistral's prompt. 

## Prompt Template

I recommend using the ChatML format instead, I will run more benchmarks. This also fixes the bug with Miqu dequant failing to provide a stop. 
```
<|im_start|>system 
Provide some context and/or instructions to the model.
<|im_end|> 
<|im_start|>user 
The user’s message goes here
<|im_end|> 
<|im_start|>assistant <|im_end|>
```

## Kudos
`Credit to https://twitter.com/hu_yifei for providing GSM & Hellaswag. It is the first open weight model to dethrone GPT-4 on EQ bench.`

## Base Model Details
This model is a fine-tuned version of [152334H/miqu-1-70b-sf](https://huggingface.co/152334H/miqu-1-70b-sf) on the Slimorca dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3110

## Training procedure

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.4.0`
```yaml
base_model: 152334H/miqu-1-70b-sf
model_type: MistralForCausalLM
tokenizer_type: LlamaTokenizer
is_mistral_derived_model: true

load_in_8bit: false
load_in_4bit: true
strict: false

datasets:
  - path: Open-Orca/SlimOrca
    type: sharegpt
    conversation: chatml
dataset_prepared_path: last_run_prepared
val_set_size: 0.1
output_dir: ./qlora-out

adapter: qlora
lora_model_dir:

sequence_len: 8192
sample_packing: true
pad_to_sequence_len: true

lora_r: 32
lora_alpha: 16
lora_dropout: 0.05
lora_target_linear: true
lora_fan_in_fan_out:
lora_target_modules:
  - gate_proj
  - down_proj
  - up_proj
  - q_proj
  - v_proj
  - k_proj
  - o_proj

wandb_project:
wandb_entity:
wandb_watch:
wandb_name:
wandb_log_model:

gradient_accumulation_steps: 4
micro_batch_size: 2
num_epochs: 1
optimizer: adamw_bnb_8bit
lr_scheduler: cosine
learning_rate: 0.0002

train_on_inputs: false
group_by_length: false
bf16: auto
fp16:
tf32: false

gradient_checkpointing: true
early_stopping_patience:
resume_from_checkpoint:
local_rank:
logging_steps: 1
xformers_attention:
flash_attention: true

loss_watchdog_threshold: 5.0
loss_watchdog_patience: 3

warmup_steps: 10
evals_per_epoch: 4
eval_table_size:
eval_table_max_new_tokens: 128
saves_per_epoch: 1
debug:
deepspeed:
weight_decay: 0.0
fsdp:
fsdp_config:
special_tokens:
  bos_token: "<s>"
  eos_token: "</s>"
  unk_token: "<unk>"
```

</details><br>

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 10
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.9043        | 0.0   | 1    | 0.6387          |
| 0.5612        | 0.25  | 881  | 0.3279          |
| 0.6044        | 0.5   | 1762 | 0.3177          |
| 0.6592        | 0.75  | 2643 | 0.3110          |


### Framework versions

- PEFT 0.8.2
- Transformers 4.38.0.dev0
- Pytorch 2.1.2+cu118
- Datasets 2.16.1
- Tokenizers 0.15.0
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_ShinojiResearch__Senku-70B-Full)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |75.44|
|AI2 Reasoning Challenge (25-Shot)|71.50|
|HellaSwag (10-Shot)              |87.88|
|MMLU (5-Shot)                    |75.20|
|TruthfulQA (0-shot)              |61.96|
|Winogrande (5-shot)              |84.77|
|GSM8k (5-shot)                   |71.34|

