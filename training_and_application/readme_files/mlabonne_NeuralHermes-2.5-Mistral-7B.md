---
language:
- en
license: apache-2.0
tags:
- mistral
- instruct
- finetune
- chatml
- gpt4
- synthetic data
- distillation
- dpo
- rlhf
datasets:
- mlabonne/chatml_dpo_pairs
base_model: teknium/OpenHermes-2.5-Mistral-7B
model-index:
- name: NeuralHermes-2.5-Mistral-7B
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
      value: 66.55
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=mlabonne/NeuralHermes-2.5-Mistral-7B
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
      value: 84.9
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=mlabonne/NeuralHermes-2.5-Mistral-7B
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
      value: 63.32
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=mlabonne/NeuralHermes-2.5-Mistral-7B
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
      value: 54.93
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=mlabonne/NeuralHermes-2.5-Mistral-7B
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
      value: 78.3
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=mlabonne/NeuralHermes-2.5-Mistral-7B
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
      value: 61.33
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=mlabonne/NeuralHermes-2.5-Mistral-7B
      name: Open LLM Leaderboard
---

<center><img src="https://i.imgur.com/qIhaFNM.png"></center>

# NeuralHermes 2.5 - Mistral 7B

NeuralHermes is based on the [teknium/OpenHermes-2.5-Mistral-7B](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B) model that has been further fine-tuned with Direct Preference Optimization (DPO) using the [mlabonne/chatml_dpo_pairs](https://huggingface.co/datasets/mlabonne/chatml_dpo_pairs) dataset. It surpasses the original model on most benchmarks (see results).

It is directly inspired by the RLHF process described by [Intel/neural-chat-7b-v3-1](https://huggingface.co/Intel/neural-chat-7b-v3-1)'s authors to improve performance. I used the same dataset and reformatted it to apply the ChatML template.

The code to train this model is available on [Google Colab](https://colab.research.google.com/drive/15iFBr1xWgztXvhrj5I9fBv20c7CFOPBE?usp=sharing) and [GitHub](https://github.com/mlabonne/llm-course/tree/main). It required an A100 GPU for about an hour.

## Quantized models

* **GGUF**: https://huggingface.co/TheBloke/NeuralHermes-2.5-Mistral-7B-GGUF
* **AWQ**: https://huggingface.co/TheBloke/NeuralHermes-2.5-Mistral-7B-AWQ
* **GPTQ**: https://huggingface.co/TheBloke/NeuralHermes-2.5-Mistral-7B-GPTQ
* **EXL2**:
  * 3.0bpw: https://huggingface.co/LoneStriker/NeuralHermes-2.5-Mistral-7B-3.0bpw-h6-exl2
  * 4.0bpw: https://huggingface.co/LoneStriker/NeuralHermes-2.5-Mistral-7B-4.0bpw-h6-exl2
  * 5.0bpw: https://huggingface.co/LoneStriker/NeuralHermes-2.5-Mistral-7B-5.0bpw-h6-exl2
  * 6.0bpw: https://huggingface.co/LoneStriker/NeuralHermes-2.5-Mistral-7B-6.0bpw-h6-exl2
  * 8.0bpw: https://huggingface.co/LoneStriker/NeuralHermes-2.5-Mistral-7B-8.0bpw-h8-exl2

## Results

**Update:** NeuralHermes-2.5 became the best Hermes-based model on the Open LLM leaderboard and one of the very best 7b models. 🎉

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/yWe6VBFxkHiuOlDVBXtGo.png)

Teknium (author of OpenHermes-2.5-Mistral-7B) benchmarked the model ([see his tweet](https://twitter.com/Teknium1/status/1729955709377503660)).

Results are improved on every benchmark: **AGIEval** (from 43.07% to 43.62%), **GPT4All** (from 73.12% to 73.25%), and **TruthfulQA**.

### AGIEval
![](https://i.imgur.com/7an3B1f.png)

### GPT4All
![](https://i.imgur.com/TLxZFi9.png)

### TruthfulQA
![](https://i.imgur.com/V380MqD.png)

You can check the Weights & Biases project [here](https://wandb.ai/mlabonne/DPO/runs/axe71gr0?nw=nwusermlabonne).

## Usage

You can run this model using [LM Studio](https://lmstudio.ai/) or any other frontend.

You can also run this model using the following code:

```python
import transformers
from transformers import AutoTokenizer

# Format prompt
message = [
    {"role": "system", "content": "You are a helpful assistant chatbot."},
    {"role": "user", "content": "What is a Large Language Model?"}
]
tokenizer = AutoTokenizer.from_pretrained(new_model)
prompt = tokenizer.apply_chat_template(message, add_generation_prompt=True, tokenize=False)

# Create pipeline
pipeline = transformers.pipeline(
    "text-generation",
    model=new_model,
    tokenizer=tokenizer
)

# Generate text
sequences = pipeline(
    prompt,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    num_return_sequences=1,
    max_length=200,
)
print(sequences[0]['generated_text'])
```

## Training hyperparameters

**LoRA**:
* r=16
* lora_alpha=16
* lora_dropout=0.05
* bias="none"
* task_type="CAUSAL_LM"
* target_modules=['k_proj', 'gate_proj', 'v_proj', 'up_proj', 'q_proj', 'o_proj', 'down_proj']

**Training arguments**:
* per_device_train_batch_size=4
* gradient_accumulation_steps=4
* gradient_checkpointing=True
* learning_rate=5e-5
* lr_scheduler_type="cosine"
* max_steps=200
* optim="paged_adamw_32bit"
* warmup_steps=100

**DPOTrainer**:
* beta=0.1
* max_prompt_length=1024
* max_length=1536
