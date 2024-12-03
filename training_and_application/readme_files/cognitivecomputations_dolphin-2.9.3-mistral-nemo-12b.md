---
license: apache-2.0
base_model: mistralai/Mistral-Nemo-Base-2407
tags:
- generated_from_trainer
- axolotl
datasets:
- cognitivecomputations/Dolphin-2.9
- teknium/OpenHermes-2.5
- m-a-p/CodeFeedback-Filtered-Instruction
- cognitivecomputations/dolphin-coder
- cognitivecomputations/samantha-data
- microsoft/orca-math-word-problems-200k
- Locutusque/function-calling-chatml
- internlm/Agent-FLAN
---

# Dolphin 2.9.3 Mistral Nemo 12b 🐬

Curated and trained by Eric Hartford and Cognitive Computations

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/h3K4XGj2RH)
Discord: https://discord.gg/h3K4XGj2RH

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/ldkN1J0WIDQwU4vutGYiD.png" width="600" />

Our appreciation for the sponsors of Dolphin 2.9.3:
- [Crusoe Cloud](https://crusoe.ai/) - provided excellent on-demand 8xL40S node

This model is based on mistralai/Mistral-Nemo-Base-2407, and is governed by the apache 2.0 license.

The base model has 128K context, and our finetuning used 8192 sequence length.

Dolphin 2.9.3 uses ChatML prompt template format.

example:

```
<|im_start|>system
You are Dolphin, a helpful AI assistant.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

Dolphin-2.9.3 has a variety of instruction following, conversational, and coding skills. It also has initial agentic abilities and supports function calling.

Dolphin is uncensored. We have filtered the dataset to remove alignment and bias. This makes the model more compliant. You are advised to implement your own alignment layer before exposing the model as a service. It will be highly compliant with any requests, even unethical ones. Please read my blog post about uncensored models. https://erichartford.com/uncensored-models You are responsible for any content you create using this model. Enjoy responsibly.

Dolphin is licensed according to apache 2.0 license.  We grant permission for any use, including commercial. Dolphin was trained on data generated from GPT4, among other models.

## Evals

<details><summary>See evals</summary>
  
```
|                           Tasks                           |Version|Filter|n-shot|        Metric         |   |Value |   |Stderr|
|-----------------------------------------------------------|-------|------|-----:|-----------------------|---|-----:|---|------|
|leaderboard                                                |N/A    |none  |     0|acc                    |↑  |0.3437|±  |0.0043|
|                                                           |       |none  |     0|acc_norm               |↑  |0.5076|±  |0.0053|
|                                                           |       |none  |     0|exact_match            |↑  |0.0536|±  |0.0061|
|                                                           |       |none  |     0|inst_level_loose_acc   |↑  |0.4388|±  |N/A   |
|                                                           |       |none  |     0|inst_level_strict_acc  |↑  |0.3741|±  |N/A   |
|                                                           |       |none  |     0|prompt_level_loose_acc |↑  |0.3105|±  |0.0199|
|                                                           |       |none  |     0|prompt_level_strict_acc|↑  |0.2477|±  |0.0186|
| - leaderboard_bbh                                         |N/A    |none  |     3|acc_norm               |↑  |0.5549|±  |0.0061|
|  - leaderboard_bbh_boolean_expressions                    |      0|none  |     3|acc_norm               |↑  |0.8640|±  |0.0217|
|  - leaderboard_bbh_causal_judgement                       |      0|none  |     3|acc_norm               |↑  |0.6417|±  |0.0352|
|  - leaderboard_bbh_date_understanding                     |      0|none  |     3|acc_norm               |↑  |0.6080|±  |0.0309|
|  - leaderboard_bbh_disambiguation_qa                      |      0|none  |     3|acc_norm               |↑  |0.6480|±  |0.0303|
|  - leaderboard_bbh_formal_fallacies                       |      0|none  |     3|acc_norm               |↑  |0.5360|±  |0.0316|
|  - leaderboard_bbh_geometric_shapes                       |      0|none  |     3|acc_norm               |↑  |0.5240|±  |0.0316|
|  - leaderboard_bbh_hyperbaton                             |      0|none  |     3|acc_norm               |↑  |0.6440|±  |0.0303|
|  - leaderboard_bbh_logical_deduction_five_objects         |      0|none  |     3|acc_norm               |↑  |0.4600|±  |0.0316|
|  - leaderboard_bbh_logical_deduction_seven_objects        |      0|none  |     3|acc_norm               |↑  |0.4680|±  |0.0316|
|  - leaderboard_bbh_logical_deduction_three_objects        |      0|none  |     3|acc_norm               |↑  |0.7000|±  |0.0290|
|  - leaderboard_bbh_movie_recommendation                   |      0|none  |     3|acc_norm               |↑  |0.8160|±  |0.0246|
|  - leaderboard_bbh_navigate                               |      0|none  |     3|acc_norm               |↑  |0.6040|±  |0.0310|
|  - leaderboard_bbh_object_counting                        |      0|none  |     3|acc_norm               |↑  |0.3680|±  |0.0306|
|  - leaderboard_bbh_penguins_in_a_table                    |      0|none  |     3|acc_norm               |↑  |0.5548|±  |0.0413|
|  - leaderboard_bbh_reasoning_about_colored_objects        |      0|none  |     3|acc_norm               |↑  |0.6320|±  |0.0306|
|  - leaderboard_bbh_ruin_names                             |      0|none  |     3|acc_norm               |↑  |0.7440|±  |0.0277|
|  - leaderboard_bbh_salient_translation_error_detection    |      0|none  |     3|acc_norm               |↑  |0.5280|±  |0.0316|
|  - leaderboard_bbh_snarks                                 |      0|none  |     3|acc_norm               |↑  |0.6292|±  |0.0363|
|  - leaderboard_bbh_sports_understanding                   |      0|none  |     3|acc_norm               |↑  |0.8040|±  |0.0252|
|  - leaderboard_bbh_temporal_sequences                     |      0|none  |     3|acc_norm               |↑  |0.4680|±  |0.0316|
|  - leaderboard_bbh_tracking_shuffled_objects_five_objects |      0|none  |     3|acc_norm               |↑  |0.2160|±  |0.0261|
|  - leaderboard_bbh_tracking_shuffled_objects_seven_objects|      0|none  |     3|acc_norm               |↑  |0.1160|±  |0.0203|
|  - leaderboard_bbh_tracking_shuffled_objects_three_objects|      0|none  |     3|acc_norm               |↑  |0.3000|±  |0.0290|
|  - leaderboard_bbh_web_of_lies                            |      0|none  |     3|acc_norm               |↑  |0.4880|±  |0.0317|
| - leaderboard_gpqa                                        |N/A    |none  |     0|acc_norm               |↑  |0.3146|±  |0.0135|
|  - leaderboard_gpqa_diamond                               |      1|none  |     0|acc_norm               |↑  |0.3182|±  |0.0332|
|  - leaderboard_gpqa_extended                              |      1|none  |     0|acc_norm               |↑  |0.3187|±  |0.0200|
|  - leaderboard_gpqa_main                                  |      1|none  |     0|acc_norm               |↑  |0.3080|±  |0.0218|
| - leaderboard_ifeval                                      |      2|none  |     0|inst_level_loose_acc   |↑  |0.4388|±  |N/A   |
|                                                           |       |none  |     0|inst_level_strict_acc  |↑  |0.3741|±  |N/A   |
|                                                           |       |none  |     0|prompt_level_loose_acc |↑  |0.3105|±  |0.0199|
|                                                           |       |none  |     0|prompt_level_strict_acc|↑  |0.2477|±  |0.0186|
|  - leaderboard_math_algebra_hard                          |      1|none  |     4|exact_match            |↑  |0.0749|±  |0.0150|
|  - leaderboard_math_counting_and_prob_hard                |      1|none  |     4|exact_match            |↑  |0.0244|±  |0.0140|
|  - leaderboard_math_geometry_hard                         |      1|none  |     4|exact_match            |↑  |0.0227|±  |0.0130|
| - leaderboard_math_hard                                   |N/A    |none  |     4|exact_match            |↑  |0.0536|±  |0.0061|
|  - leaderboard_math_intermediate_algebra_hard             |      1|none  |     4|exact_match            |↑  |0.0250|±  |0.0093|
|  - leaderboard_math_num_theory_hard                       |      1|none  |     4|exact_match            |↑  |0.0390|±  |0.0156|
|  - leaderboard_math_prealgebra_hard                       |      1|none  |     4|exact_match            |↑  |0.1295|±  |0.0242|
|  - leaderboard_math_precalculus_hard                      |      1|none  |     4|exact_match            |↑  |0.0296|±  |0.0146|
| - leaderboard_mmlu_pro                                    |    0.1|none  |     5|acc                    |↑  |0.3437|±  |0.0043|
| - leaderboard_musr                                        |N/A    |none  |     0|acc_norm               |↑  |0.4511|±  |0.0178|
|  - leaderboard_musr_murder_mysteries                      |      1|none  |     0|acc_norm               |↑  |0.5880|±  |0.0312|
|  - leaderboard_musr_object_placements                     |      1|none  |     0|acc_norm               |↑  |0.3438|±  |0.0297|
|  - leaderboard_musr_team_allocation                       |      1|none  |     0|acc_norm               |↑  |0.4240|±  |0.0313|

|         Groups         |Version|Filter|n-shot|        Metric         |   |Value |   |Stderr|
|------------------------|-------|------|-----:|-----------------------|---|-----:|---|------|
|leaderboard             |N/A    |none  |     0|acc                    |↑  |0.3437|±  |0.0043|
|                        |       |none  |     0|acc_norm               |↑  |0.5076|±  |0.0053|
|                        |       |none  |     0|exact_match            |↑  |0.0536|±  |0.0061|
|                        |       |none  |     0|inst_level_loose_acc   |↑  |0.4388|±  |N/A   |
|                        |       |none  |     0|inst_level_strict_acc  |↑  |0.3741|±  |N/A   |
|                        |       |none  |     0|prompt_level_loose_acc |↑  |0.3105|±  |0.0199|
|                        |       |none  |     0|prompt_level_strict_acc|↑  |0.2477|±  |0.0186|
| - leaderboard_bbh      |N/A    |none  |     3|acc_norm               |↑  |0.5549|±  |0.0061|
| - leaderboard_gpqa     |N/A    |none  |     0|acc_norm               |↑  |0.3146|±  |0.0135|
| - leaderboard_math_hard|N/A    |none  |     4|exact_match            |↑  |0.0536|±  |0.0061|
| - leaderboard_musr     |N/A    |none  |     0|acc_norm               |↑  |0.4511|±  |0.0178|
```

</details><br>

## Training

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/axolotl-ai-cloud/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.4.1`
```yaml
base_model: /workspace/models/Mistral-Nemo-Base-2407
model_type: AutoModelForCausalLM
tokenizer_type: AutoTokenizer

load_in_8bit: false
# load_in_4bit: true
strict: false

datasets:
  - path: /workspace/datasets/dolphin-2.9.3/dolphin201-sharegpt2.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/SystemChat_filtered_sharegpt.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/SystemChat_multilingual_sharegpt.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/dolphin-coder-translate-sharegpt2.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/dolphin-coder-codegen-sharegpt2.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/m-a-p_Code-Feedback-sharegpt-unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/m-a-p_CodeFeedback-Filtered-Instruction-sharegpt-unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/not_samantha_norefusals.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/Orca-Math-resort-unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/agent_instruct_react_unfiltered.jsonl
    type: sharegpt  
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/toolbench_instruct_j1s1_3k_unfiltered.jsonl
    type: sharegpt  
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/toolbench_negative_unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/toolbench_react_10p_unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/toolbench_tflan_cot_30p_unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9.3/openhermes200k_unfiltered.jsonl
    type: sharegpt 
    conversation: chatml

chat_template: chatml
# adapter: qlora
# lora_r: 128
# lora_alpha: 16
# lora_modules_to_save: [embed_tokens, lm_head]
# lora_dropout: 0.05
# lora_target_linear: true


unfrozen_parameters:
- ^lm_head.weight$
- ^model.embed_tokens.weight$
- input_layernorm
- model.norm
- post_attention_layernorm
- self_attn.rotary_emb
# mlp.down_proj layers
- model.layers.0.mlp.down_proj
- model.layers.1.mlp.down_proj
- model.layers.4.mlp.down_proj
- model.layers.37.mlp.down_proj
- model.layers.24.mlp.down_proj
- model.layers.2.mlp.down_proj
- model.layers.38.mlp.down_proj
- model.layers.35.mlp.down_proj
- model.layers.25.mlp.down_proj
- model.layers.6.mlp.down_proj
- model.layers.22.mlp.down_proj
- model.layers.23.mlp.down_proj
- model.layers.3.mlp.down_proj
- model.layers.21.mlp.down_proj
- model.layers.5.mlp.down_proj
- model.layers.28.mlp.down_proj
- model.layers.20.mlp.down_proj
- model.layers.26.mlp.down_proj
- model.layers.19.mlp.down_proj
- model.layers.34.mlp.down_proj
# mlp.gate_proj layers
- model.layers.2.mlp.gate_proj
- model.layers.1.mlp.gate_proj
- model.layers.3.mlp.gate_proj
- model.layers.5.mlp.gate_proj
- model.layers.4.mlp.gate_proj
- model.layers.35.mlp.gate_proj
- model.layers.36.mlp.gate_proj
- model.layers.37.mlp.gate_proj
- model.layers.38.mlp.gate_proj
- model.layers.34.mlp.gate_proj
- model.layers.33.mlp.gate_proj
- model.layers.8.mlp.gate_proj
- model.layers.32.mlp.gate_proj
- model.layers.6.mlp.gate_proj
- model.layers.28.mlp.gate_proj
- model.layers.26.mlp.gate_proj
- model.layers.30.mlp.gate_proj
- model.layers.23.mlp.gate_proj
- model.layers.29.mlp.gate_proj
- model.layers.27.mlp.gate_proj
# mlp.up_proj layers
- model.layers.3.mlp.up_proj
- model.layers.4.mlp.up_proj
- model.layers.6.mlp.up_proj
- model.layers.2.mlp.up_proj
- model.layers.5.mlp.up_proj
- model.layers.8.mlp.up_proj
- model.layers.10.mlp.up_proj
- model.layers.9.mlp.up_proj
- model.layers.7.mlp.up_proj
- model.layers.0.mlp.up_proj
- model.layers.17.mlp.up_proj
- model.layers.15.mlp.up_proj
- model.layers.22.mlp.up_proj
- model.layers.18.mlp.up_proj
- model.layers.16.mlp.up_proj
- model.layers.11.mlp.up_proj
- model.layers.21.mlp.up_proj
- model.layers.23.mlp.up_proj
- model.layers.20.mlp.up_proj
- model.layers.27.mlp.up_proj
# self_attn.k_proj layers
- model.layers.30.self_attn.k_proj
- model.layers.27.self_attn.k_proj
- model.layers.25.self_attn.k_proj
- model.layers.33.self_attn.k_proj
- model.layers.26.self_attn.k_proj
- model.layers.31.self_attn.k_proj
- model.layers.35.self_attn.k_proj
- model.layers.39.self_attn.k_proj
- model.layers.22.self_attn.k_proj
- model.layers.24.self_attn.k_proj
- model.layers.21.self_attn.k_proj
- model.layers.28.self_attn.k_proj
- model.layers.23.self_attn.k_proj
- model.layers.36.self_attn.k_proj
- model.layers.20.self_attn.k_proj
- model.layers.37.self_attn.k_proj
- model.layers.29.self_attn.k_proj
- model.layers.32.self_attn.k_proj
- model.layers.16.self_attn.k_proj
- model.layers.18.self_attn.k_proj
# self_attn.o_proj layers
- model.layers.7.self_attn.o_proj
- model.layers.6.self_attn.o_proj
- model.layers.9.self_attn.o_proj
- model.layers.5.self_attn.o_proj
- model.layers.27.self_attn.o_proj
- model.layers.26.self_attn.o_proj
- model.layers.4.self_attn.o_proj
- model.layers.31.self_attn.o_proj
- model.layers.8.self_attn.o_proj
- model.layers.16.self_attn.o_proj
- model.layers.3.self_attn.o_proj
- model.layers.10.self_attn.o_proj
- model.layers.18.self_attn.o_proj
- model.layers.33.self_attn.o_proj
- model.layers.17.self_attn.o_proj
- model.layers.32.self_attn.o_proj
- model.layers.30.self_attn.o_proj
- model.layers.2.self_attn.o_proj
- model.layers.15.self_attn.o_proj
- model.layers.11.self_attn.o_proj
# self_attn.q_proj layers
- model.layers.14.self_attn.q_proj
- model.layers.11.self_attn.q_proj
- model.layers.15.self_attn.q_proj
- model.layers.9.self_attn.q_proj
- model.layers.8.self_attn.q_proj
- model.layers.18.self_attn.q_proj
- model.layers.12.self_attn.q_proj
- model.layers.13.self_attn.q_proj
- model.layers.19.self_attn.q_proj
- model.layers.16.self_attn.q_proj
- model.layers.10.self_attn.q_proj
- model.layers.17.self_attn.q_proj
- model.layers.7.self_attn.q_proj
- model.layers.5.self_attn.q_proj
- model.layers.20.self_attn.q_proj
- model.layers.3.self_attn.q_proj
- model.layers.26.self_attn.q_proj
- model.layers.27.self_attn.q_proj
- model.layers.28.self_attn.q_proj
- model.layers.33.self_attn.q_proj
# self_attn.v_proj layers
- model.layers.27.self_attn.v_proj
- model.layers.20.self_attn.v_proj
- model.layers.24.self_attn.v_proj
- model.layers.25.self_attn.v_proj
- model.layers.30.self_attn.v_proj
- model.layers.2.self_attn.v_proj
- model.layers.23.self_attn.v_proj
- model.layers.22.self_attn.v_proj
- model.layers.26.self_attn.v_proj
- model.layers.33.self_attn.v_proj
- model.layers.37.self_attn.v_proj
- model.layers.7.self_attn.v_proj
- model.layers.4.self_attn.v_proj
- model.layers.18.self_attn.v_proj
- model.layers.31.self_attn.v_proj
- model.layers.17.self_attn.v_proj
- model.layers.35.self_attn.v_proj
- model.layers.32.self_attn.v_proj
- model.layers.21.self_attn.v_proj
- model.layers.3.self_attn.v_proj



dataset_prepared_path:  /workspace/axolotl/dolph-2.9.3-nemo-prepared
val_set_size: 0.01
output_dir: /workspace/axolotl/dolphin-2.9.3-mistral-nemo

sequence_len: 8192
sample_packing: true
pad_to_sequence_len: true

wandb_project: dolphin-2.9.3-Mistral-nemo
wandb_watch:
wandb_run_id:
wandb_log_model:

gradient_accumulation_steps: 16
micro_batch_size: 1
num_epochs: 3
optimizer: adamw_torch
lr_scheduler: cosine
learning_rate: 5e-6
train_on_inputs: false
group_by_length: false
bf16: auto
fp16:
tf32:

gradient_checkpointing: true
gradient_checkpointing_kwargs:
  use_reentrant: false
early_stopping_patience:
resume_from_checkpoint:
logging_steps: 1
xformers_attention:
flash_attention: true

warmup_steps: 100
# evals_per_epoch: 4
eval_table_size:
saves_per_epoch: 1
save_total_limit: 2
save_steps:
debug:
deepspeed: deepspeed_configs/zero3_bf16.json
weight_decay: 0.1
special_tokens:
  eos_token: "<|im_end|>"
  pad_token: "<pad>"
  bos_token: "<s>"
  unk_token: "<unk>"
tokens:
  - "<|im_start|>"


# fsdp:
#   - full_shard
#   - auto_wrap
# fsdp_config:
#   fsdp_limit_all_gathers: true
#   fsdp_sync_module_states: true
#   fsdp_offload_params: true
#   fsdp_use_orig_params: false
#   fsdp_cpu_ram_efficient_loading: true
#   fsdp_transformer_layer_cls_to_wrap: MixtralSparseMoeBlock
#   fsdp_state_dict_type: FULL_STATE_DICT
#   fsdp_auto_wrap_policy: TRANSFORMER_BASED_WRAP
#   fsdp_sharding_strategy: FULL_SHARD
#   fsdp_forward_prefetch: false
#   fsdp_backward_prefetch: BACKWARD_PRE
```

</details><br>

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/ehartford/dolphin-2.9.3-Mistral-nemo/runs/c23odyoj)
# workspace/axolotl/dolphin-2.9.3-mistral-nemo

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5605

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 16
- total_train_batch_size: 128
- total_eval_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- num_epochs: 3

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 0.5691        | 1.0162 | 983  | 0.5734          |
| 0.5335        | 2.0174 | 1968 | 0.5609          |
| 0.5297        | 2.9639 | 2901 | 0.5605          |


### Framework versions

- Transformers 4.43.0.dev0
- Pytorch 2.2.2+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
