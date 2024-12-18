---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
dtype: bfloat16
tags:
- merge
---

# EDIT:
Always check my space for the latest benchmark results for my models!
* https://huggingface.co/spaces/CultriX/Yet_Another_LLM_Leaderboard
  
# Results:
T: 🟦
Model: CultriX/MistralTrix-v1 📑
Average: 73.39
ARC: 72.27
HellaSwag: 88.33
MMLU: 65.24
TruthfulQA: 70.73
Winogrande: 80.98
GSM8K: 62.77

# Edit/Disclaimer:
Currently the #1 ranked 7B LLM on the LLM Leaderboards, woah!
I did not expect that result at all and am in no way a professional when it comes to LLM's or computer science in general,
just a guy that likes to nerd about and tinker around. 

For those wondering how I achieved this, the answer is that I simply attempted to apply the techniques outlined in this amazing article myself: https://towardsdatascience.com/fine-tune-a-mistral-7b-model-with-direct-preference-optimization-708042745aac
Therefore, all credit basically goes to the guy who wrote that. 
He offers the exact Colab notebook I used to train this model for free, as well as a really nice GitHub page I hope he doesn't mind me sharing: https://github.com/mlabonne/llm-course/
So huge thank you to him for sharing his knowledge and learning me a thing or two in the process!

# GGUF
I attempted to quantisize the model myself, which again I pretty much have no clue about, but it seems to run fine for me when I test them:
https://huggingface.co/CultriX/MistralTrix-v1-GGUF

I'll say it one more time though:
"I am a complete beginner to all of this, so if these do end up sucking don't be surprised."

You have been warned :)

# Description:
(trained on a single Colab GPU in less than a few hours)

MistralTrix-v1 is an zyh3826/GML-Mistral-merged-v1 model that has been further fine-tuned with Direct Preference Optimization (DPO) using Intel's dataset for neural-chat-7b-v3-1.
It surpasses the original model on several benchmarks (see results).

It is directly inspired by the RLHF process described by Intel/neural-chat-7b-v3-1's authors to improve performance. 
I used the same dataset and reformatted it to apply the ChatML template.

The code to train this model is available on Google Colab and GitHub. 
Fine-tuning took about an hour on Google Colab A-1000 GPU with 40GB VRAM.

# TRAINING SPECIFICATIONS
> LoRA configuration
peft_config = LoraConfig(
    r=16,
    lora_alpha=16,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=['k_proj', 'gate_proj', 'v_proj', 'up_proj', 'q_proj', 'o_proj', 'down_proj']
)

> Model to fine-tune
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    load_in_4bit=True
)
model.config.use_cache = False

> Reference model
ref_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    load_in_4bit=True
)

> Training arguments
training_args = TrainingArguments(
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    gradient_checkpointing=True,
    learning_rate=5e-5,
    lr_scheduler_type="cosine",
    max_steps=200,
    save_strategy="no",
    logging_steps=1,
    output_dir=new_model,
    optim="paged_adamw_32bit",
    warmup_steps=100,
    bf16=True,
    report_to="wandb",
)

> Create DPO trainer
dpo_trainer = DPOTrainer(
    model,
    ref_model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=tokenizer,
    peft_config=peft_config,
    beta=0.1,
    max_prompt_length=1024,
    max_length=1536,
)