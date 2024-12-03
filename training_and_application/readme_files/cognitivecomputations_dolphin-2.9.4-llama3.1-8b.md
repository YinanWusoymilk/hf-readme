---
license: llama3.1
base_model: meta-llama/Meta-Llama-3.1-8B
tags:
- generated_from_trainer
datasets:
- cognitivecomputations/Dolphin-2.9
- m-a-p/CodeFeedback-Filtered-Instruction
- cognitivecomputations/dolphin-coder
- cognitivecomputations/samantha-data
- microsoft/orca-math-word-problems-200k
- mlabonne/FineTome-100k
- arcee/agent_data
- PawanKrd/math-gpt-4o-200k
- cognitivecomputations/SystemChat-2.0
---

# Dolphin 2.9.4 Llama 3.1 8b 🐬

Curated and trained by Eric Hartford and Cognitive Computations

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/h3K4XGj2RH)
Discord: https://discord.gg/h3K4XGj2RH

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/ldkN1J0WIDQwU4vutGYiD.png" width="600" />

Our appreciation for the sponsors of Dolphin 2.9.4:
- [Crusoe Cloud](https://crusoe.ai/) - provided excellent on-demand 8xL40S node

This model is based on Meta Llama 3.1 8b, and is governed by the Llama 3.1 license.

The base model has 128K context, and our finetuning used 8192 sequence length.

Dolphin 2.9.4 uses ChatML prompt template format.

example:

```
<|im_start|>system
You are Dolphin, a helpful AI assistant.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

Dolphin-2.9.4 has a variety of instruction following, conversational, and coding skills. It also has agentic abilities and supports function calling.
It is especially trained to obey the system prompt, and follow instructions in many languages.

Dolphin is uncensored. We have filtered the dataset to remove alignment and bias. This makes the model more compliant. You are advised to implement your own alignment layer before exposing the model as a service. It will be highly compliant with any requests, even unethical ones. Please read my blog post about uncensored models. https://erichartford.com/uncensored-models You are responsible for any content you create using this model. Enjoy responsibly.


<details><summary>Evals</summary>

```
hf (pretrained=/workspace/axolotl/dolphin-2.9.4-llama3.1-8b-hf,dtype=bfloat16), gen_kwargs: (None), limit: None, num_fewshot: None, batch_size: auto (4)
|                           Tasks                           |Version|Filter|n-shot|        Metric         |   |Value |   |Stderr|
|-----------------------------------------------------------|-------|------|-----:|-----------------------|---|-----:|---|------|
|leaderboard                                                |N/A    |none  |     0|acc                    |↑  |0.2926|±  |0.0041|
|                                                           |       |none  |     0|acc_norm               |↑  |0.4513|±  |0.0053|
|                                                           |       |none  |     0|exact_match            |↑  |0.0982|±  |0.0079|
|                                                           |       |none  |     0|inst_level_loose_acc   |↑  |0.3825|±  |N/A   |
|                                                           |       |none  |     0|inst_level_strict_acc  |↑  |0.3597|±  |N/A   |
|                                                           |       |none  |     0|prompt_level_loose_acc |↑  |0.2421|±  |0.0184|
|                                                           |       |none  |     0|prompt_level_strict_acc|↑  |0.2181|±  |0.0178|
| - leaderboard_bbh                                         |N/A    |none  |     3|acc_norm               |↑  |0.4931|±  |0.0061|
|  - leaderboard_bbh_boolean_expressions                    |      0|none  |     3|acc_norm               |↑  |0.8000|±  |0.0253|
|  - leaderboard_bbh_causal_judgement                       |      0|none  |     3|acc_norm               |↑  |0.5615|±  |0.0364|
|  - leaderboard_bbh_date_understanding                     |      0|none  |     3|acc_norm               |↑  |0.4520|±  |0.0315|
|  - leaderboard_bbh_disambiguation_qa                      |      0|none  |     3|acc_norm               |↑  |0.6640|±  |0.0299|
|  - leaderboard_bbh_formal_fallacies                       |      0|none  |     3|acc_norm               |↑  |0.5600|±  |0.0315|
|  - leaderboard_bbh_geometric_shapes                       |      0|none  |     3|acc_norm               |↑  |0.3640|±  |0.0305|
|  - leaderboard_bbh_hyperbaton                             |      0|none  |     3|acc_norm               |↑  |0.6320|±  |0.0306|
|  - leaderboard_bbh_logical_deduction_five_objects         |      0|none  |     3|acc_norm               |↑  |0.4600|±  |0.0316|
|  - leaderboard_bbh_logical_deduction_seven_objects        |      0|none  |     3|acc_norm               |↑  |0.4360|±  |0.0314|
|  - leaderboard_bbh_logical_deduction_three_objects        |      0|none  |     3|acc_norm               |↑  |0.6160|±  |0.0308|
|  - leaderboard_bbh_movie_recommendation                   |      0|none  |     3|acc_norm               |↑  |0.7880|±  |0.0259|
|  - leaderboard_bbh_navigate                               |      0|none  |     3|acc_norm               |↑  |0.5200|±  |0.0317|
|  - leaderboard_bbh_object_counting                        |      0|none  |     3|acc_norm               |↑  |0.4520|±  |0.0315|
|  - leaderboard_bbh_penguins_in_a_table                    |      0|none  |     3|acc_norm               |↑  |0.5205|±  |0.0415|
|  - leaderboard_bbh_reasoning_about_colored_objects        |      0|none  |     3|acc_norm               |↑  |0.5120|±  |0.0317|
|  - leaderboard_bbh_ruin_names                             |      0|none  |     3|acc_norm               |↑  |0.6320|±  |0.0306|
|  - leaderboard_bbh_salient_translation_error_detection    |      0|none  |     3|acc_norm               |↑  |0.4320|±  |0.0314|
|  - leaderboard_bbh_snarks                                 |      0|none  |     3|acc_norm               |↑  |0.5843|±  |0.0370|
|  - leaderboard_bbh_sports_understanding                   |      0|none  |     3|acc_norm               |↑  |0.7040|±  |0.0289|
|  - leaderboard_bbh_temporal_sequences                     |      0|none  |     3|acc_norm               |↑  |0.1440|±  |0.0222|
|  - leaderboard_bbh_tracking_shuffled_objects_five_objects |      0|none  |     3|acc_norm               |↑  |0.1560|±  |0.0230|
|  - leaderboard_bbh_tracking_shuffled_objects_seven_objects|      0|none  |     3|acc_norm               |↑  |0.1320|±  |0.0215|
|  - leaderboard_bbh_tracking_shuffled_objects_three_objects|      0|none  |     3|acc_norm               |↑  |0.2840|±  |0.0286|
|  - leaderboard_bbh_web_of_lies                            |      0|none  |     3|acc_norm               |↑  |0.4840|±  |0.0317|
| - leaderboard_gpqa                                        |N/A    |none  |     0|acc_norm               |↑  |0.2903|±  |0.0132|
|  - leaderboard_gpqa_diamond                               |      1|none  |     0|acc_norm               |↑  |0.2980|±  |0.0326|
|  - leaderboard_gpqa_extended                              |      1|none  |     0|acc_norm               |↑  |0.2839|±  |0.0193|
|  - leaderboard_gpqa_main                                  |      1|none  |     0|acc_norm               |↑  |0.2946|±  |0.0216|
| - leaderboard_ifeval                                      |      2|none  |     0|inst_level_loose_acc   |↑  |0.3825|±  |N/A   |
|                                                           |       |none  |     0|inst_level_strict_acc  |↑  |0.3597|±  |N/A   |
|                                                           |       |none  |     0|prompt_level_loose_acc |↑  |0.2421|±  |0.0184|
|                                                           |       |none  |     0|prompt_level_strict_acc|↑  |0.2181|±  |0.0178|
|  - leaderboard_math_algebra_hard                          |      1|none  |     4|exact_match            |↑  |0.1596|±  |0.0209|
|  - leaderboard_math_counting_and_prob_hard                |      1|none  |     4|exact_match            |↑  |0.0488|±  |0.0195|
|  - leaderboard_math_geometry_hard                         |      1|none  |     4|exact_match            |↑  |0.0530|±  |0.0196|
| - leaderboard_math_hard                                   |N/A    |none  |     4|exact_match            |↑  |0.0982|±  |0.0079|
|  - leaderboard_math_intermediate_algebra_hard             |      1|none  |     4|exact_match            |↑  |0.0143|±  |0.0071|
|  - leaderboard_math_num_theory_hard                       |      1|none  |     4|exact_match            |↑  |0.0455|±  |0.0168|
|  - leaderboard_math_prealgebra_hard                       |      1|none  |     4|exact_match            |↑  |0.2591|±  |0.0316|
|  - leaderboard_math_precalculus_hard                      |      1|none  |     4|exact_match            |↑  |0.0519|±  |0.0192|
| - leaderboard_mmlu_pro                                    |    0.1|none  |     5|acc                    |↑  |0.2926|±  |0.0041|
| - leaderboard_musr                                        |N/A    |none  |     0|acc_norm               |↑  |0.3862|±  |0.0173|
|  - leaderboard_musr_murder_mysteries                      |      1|none  |     0|acc_norm               |↑  |0.5280|±  |0.0316|
|  - leaderboard_musr_object_placements                     |      1|none  |     0|acc_norm               |↑  |0.3594|±  |0.0300|
|  - leaderboard_musr_team_allocation                       |      1|none  |     0|acc_norm               |↑  |0.2720|±  |0.0282|

|         Groups         |Version|Filter|n-shot|        Metric         |   |Value |   |Stderr|
|------------------------|-------|------|-----:|-----------------------|---|-----:|---|------|
|leaderboard             |N/A    |none  |     0|acc                    |↑  |0.2926|±  |0.0041|
|                        |       |none  |     0|acc_norm               |↑  |0.4513|±  |0.0053|
|                        |       |none  |     0|exact_match            |↑  |0.0982|±  |0.0079|
|                        |       |none  |     0|inst_level_loose_acc   |↑  |0.3825|±  |N/A   |
|                        |       |none  |     0|inst_level_strict_acc  |↑  |0.3597|±  |N/A   |
|                        |       |none  |     0|prompt_level_loose_acc |↑  |0.2421|±  |0.0184|
|                        |       |none  |     0|prompt_level_strict_acc|↑  |0.2181|±  |0.0178|
| - leaderboard_bbh      |N/A    |none  |     3|acc_norm               |↑  |0.4931|±  |0.0061|
| - leaderboard_gpqa     |N/A    |none  |     0|acc_norm               |↑  |0.2903|±  |0.0132|
| - leaderboard_math_hard|N/A    |none  |     4|exact_match            |↑  |0.0982|±  |0.0079|
| - leaderboard_musr     |N/A    |none  |     0|acc_norm               |↑  |0.3862|±  |0.0173|
```

</details>

[<img src="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/axolotl-ai-cloud/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.4.1`
```yaml
base_model: meta-llama/Meta-Llama-3.1-8B
model_type: LlamaForCausalLM
tokenizer_type: AutoTokenizer

load_in_8bit: false
# load_in_4bit: true
strict: false

datasets:
  - path: /workspace/datasets/dolphin-2.9.4/dolphin201-sharegpt2.jsonl
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
- input_layernorm
- model.norm
- post_attention_layernorm
- self_attn.rotary_emb
- ^lm_head.weight$
- ^model.embed_tokens.weight$
# mlp.down_proj layers
- model.layers.1.mlp.down_proj
- model.layers.0.mlp.down_proj
- model.layers.30.mlp.down_proj
- model.layers.2.mlp.down_proj
- model.layers.21.mlp.down_proj
- model.layers.22.mlp.down_proj
- model.layers.29.mlp.down_proj
- model.layers.5.mlp.down_proj
- model.layers.4.mlp.down_proj
- model.layers.20.mlp.down_proj
- model.layers.23.mlp.down_proj
- model.layers.19.mlp.down_proj
- model.layers.3.mlp.down_proj
- model.layers.17.mlp.down_proj
- model.layers.6.mlp.down_proj
- model.layers.31.mlp.down_proj
# mlp.up_proj layers
- model.layers.4.mlp.up_proj
- model.layers.3.mlp.up_proj
- model.layers.0.mlp.up_proj
- model.layers.5.mlp.up_proj
- model.layers.7.mlp.up_proj
- model.layers.6.mlp.up_proj
- model.layers.2.mlp.up_proj
- model.layers.1.mlp.up_proj
- model.layers.8.mlp.up_proj
- model.layers.12.mlp.up_proj
- model.layers.14.mlp.up_proj
- model.layers.9.mlp.up_proj
- model.layers.15.mlp.up_proj
- model.layers.17.mlp.up_proj
- model.layers.13.mlp.up_proj
- model.layers.19.mlp.up_proj
# self_attn.k_proj layers
- model.layers.29.self_attn.k_proj
- model.layers.25.self_attn.k_proj
- model.layers.23.self_attn.k_proj
- model.layers.28.self_attn.k_proj
- model.layers.21.self_attn.k_proj
- model.layers.19.self_attn.k_proj
- model.layers.22.self_attn.k_proj
- model.layers.20.self_attn.k_proj
- model.layers.24.self_attn.k_proj
- model.layers.31.self_attn.k_proj
- model.layers.27.self_attn.k_proj
- model.layers.26.self_attn.k_proj
- model.layers.17.self_attn.k_proj
- model.layers.11.self_attn.k_proj
- model.layers.18.self_attn.k_proj
- model.layers.14.self_attn.k_proj
# self_attn.o_proj layers
- model.layers.14.self_attn.o_proj
- model.layers.7.self_attn.o_proj
- model.layers.5.self_attn.o_proj
- model.layers.11.self_attn.o_proj
- model.layers.6.self_attn.o_proj
- model.layers.24.self_attn.o_proj
- model.layers.9.self_attn.o_proj
- model.layers.13.self_attn.o_proj
- model.layers.10.self_attn.o_proj
- model.layers.12.self_attn.o_proj
- model.layers.8.self_attn.o_proj
- model.layers.25.self_attn.o_proj
- model.layers.21.self_attn.o_proj
- model.layers.23.self_attn.o_proj
- model.layers.15.self_attn.o_proj
- model.layers.16.self_attn.o_proj
# self_attn.q_proj layers
- model.layers.8.self_attn.q_proj
- model.layers.13.self_attn.q_proj
- model.layers.9.self_attn.q_proj
- model.layers.14.self_attn.q_proj
- model.layers.10.self_attn.q_proj
- model.layers.11.self_attn.q_proj
- model.layers.0.self_attn.q_proj
- model.layers.15.self_attn.q_proj
- model.layers.1.self_attn.q_proj
- model.layers.6.self_attn.q_proj
- model.layers.5.self_attn.q_proj
- model.layers.7.self_attn.q_proj
- model.layers.12.self_attn.q_proj
- model.layers.16.self_attn.q_proj
- model.layers.17.self_attn.q_proj
- model.layers.26.self_attn.q_proj
# self_attn.v_proj layers
- model.layers.26.self_attn.v_proj
- model.layers.17.self_attn.v_proj
- model.layers.3.self_attn.v_proj
- model.layers.28.self_attn.v_proj
- model.layers.29.self_attn.v_proj
- model.layers.21.self_attn.v_proj
- model.layers.15.self_attn.v_proj
- model.layers.16.self_attn.v_proj
- model.layers.20.self_attn.v_proj
- model.layers.25.self_attn.v_proj
- model.layers.6.self_attn.v_proj
- model.layers.23.self_attn.v_proj
- model.layers.4.self_attn.v_proj
- model.layers.1.self_attn.v_proj
- model.layers.22.self_attn.v_proj
- model.layers.14.self_attn.v_proj
# mlp.gate_proj layers
- model.layers.1.mlp.gate_proj
- model.layers.2.mlp.gate_proj
- model.layers.3.mlp.gate_proj
- model.layers.4.mlp.gate_proj
- model.layers.0.mlp.gate_proj
- model.layers.25.mlp.gate_proj
- model.layers.26.mlp.gate_proj
- model.layers.5.mlp.gate_proj
- model.layers.24.mlp.gate_proj
- model.layers.28.mlp.gate_proj
- model.layers.23.mlp.gate_proj
- model.layers.27.mlp.gate_proj
- model.layers.21.mlp.gate_proj
- model.layers.22.mlp.gate_proj
- model.layers.29.mlp.gate_proj
- model.layers.20.mlp.gate_proj




dataset_prepared_path:  /workspace/axolotl/dolph-2.9.4-nemo-prepared
val_set_size: 0.01
output_dir: /workspace/axolotl/dolphin-2.9.4-llama3.1-8b

sequence_len: 8192
sample_packing: true
pad_to_sequence_len: true

wandb_project: dolphin-2.9.4-llama3.1-8b
wandb_watch:
wandb_run_id:
wandb_log_model:

gradient_accumulation_steps: 16
micro_batch_size: 2
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
  bos_token: "<|begin_of_text|>"
  pad_token: "<|finetune_right_pad_id|>"
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

# workspace/axolotl/dolphin-2.9.4-llama3.1-8b

This model is a fine-tuned version of [meta-llama/Meta-Llama-3.1-8B](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5655

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 16
- total_train_batch_size: 256
- total_eval_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- num_epochs: 3

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 0.5837        | 1.0180 | 1161 | 0.5814          |
| 0.5525        | 2.0179 | 2322 | 0.5671          |
| 0.5514        | 2.9624 | 3420 | 0.5655          |


### Framework versions

- Transformers 4.44.0.dev0
- Pytorch 2.4.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
