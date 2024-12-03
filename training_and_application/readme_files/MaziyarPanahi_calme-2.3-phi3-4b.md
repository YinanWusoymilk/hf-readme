---
language:
- en
license: mit
library_name: transformers
tags:
- axolotl
- finetune
- dpo
- microsoft
- phi
- pytorch
- phi-3
- nlp
- code
- chatml
base_model: microsoft/Phi-3-mini-4k-instruct
pipeline_tag: text-generation
inference: false
model_creator: MaziyarPanahi
quantized_by: MaziyarPanahi
model-index:
- name: calme-2.3-phi3-4b
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
      value: 63.48
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=MaziyarPanahi/calme-2.3-phi3-4b
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
      value: 80.86
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=MaziyarPanahi/calme-2.3-phi3-4b
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
      value: 69.24
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=MaziyarPanahi/calme-2.3-phi3-4b
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
      value: 60.66
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=MaziyarPanahi/calme-2.3-phi3-4b
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
      value: 72.77
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=MaziyarPanahi/calme-2.3-phi3-4b
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
      value: 74.53
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=MaziyarPanahi/calme-2.3-phi3-4b
      name: Open LLM Leaderboard
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
      value: 49.26
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=MaziyarPanahi/calme-2.3-phi3-4b
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
      value: 37.66
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=MaziyarPanahi/calme-2.3-phi3-4b
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
      value: 2.95
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=MaziyarPanahi/calme-2.3-phi3-4b
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
      value: 9.06
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=MaziyarPanahi/calme-2.3-phi3-4b
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
      value: 7.75
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=MaziyarPanahi/calme-2.3-phi3-4b
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
      value: 31.42
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=MaziyarPanahi/calme-2.3-phi3-4b
      name: Open LLM Leaderboard
---

<img src="./phi-3-instruct.webp" alt="Phi-3 Logo" width="500" style="margin-left:'auto' margin-right:'auto' display:'block'"/>


# MaziyarPanahi/calme-2.3-phi3-4b

This model is a fine-tune (DPO) of `microsoft/Phi-3-mini-4k-instruct` model.

# ⚡ Quantized GGUF

All GGUF models are available here: [MaziyarPanahi/calme-2.3-phi3-4b-GGUF](https://huggingface.co/MaziyarPanahi/calme-2.3-phi3-4b-GGUF)

# 🏆 [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_MaziyarPanahi__calme-2.3-phi3-4b)



** Leaderboard 2**

|      Metric       |Value|
|-------------------|----:|
|Avg.               |23.38|
|IFEval (0-Shot)    |49.26|
|BBH (3-Shot)       |37.66|
|MATH Lvl 5 (4-Shot)| 2.95|
|GPQA (0-shot)      | 9.06|
|MuSR (0-shot)      | 7.75|
|MMLU-PRO (5-shot)  |31.42|


** Leaderboard 1**

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |70.26|
|AI2 Reasoning Challenge (25-Shot)|63.48|
|HellaSwag (10-Shot)              |80.86|
|MMLU (5-Shot)                    |69.24|
|TruthfulQA (0-shot)              |60.66|
|Winogrande (5-shot)              |72.77|
|GSM8k (5-shot)                   |74.53|



`MaziyarPanahi/calme-2.3-phi3-4b` is the best-performing Phi-3-mini-4k model on the Open LLM Leaderboard. (03/06/2024).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/5fd5e18a90b6dc4633f6d292/tKhQ55r7znR4X8GofwYj1.png)

# Prompt Template

This model uses `ChatML` prompt template:

```
<|im_start|>system
{System}
<|im_end|>
<|im_start|>user
{User}
<|im_end|>
<|im_start|>assistant
{Assistant}
````

# How to use

You can use this model by using `MaziyarPanahi/calme-2.3-phi3-4b` as the model name in Hugging Face's
transformers library.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
from transformers import pipeline
import torch

model_id = "MaziyarPanahi/calme-2.3-phi3-4b"

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
    # attn_implementation="flash_attention_2"
)

tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    trust_remote_code=True
)

streamer = TextStreamer(tokenizer)

messages = [
    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user", "content": "Who are you?"},
]

# this should work perfectly for the model to stop generating
terminators = [
    tokenizer.eos_token_id, # this should be <|im_end|>
    tokenizer.convert_tokens_to_ids("<|assistant|>"), # sometimes model stops generating at <|assistant|>
    tokenizer.convert_tokens_to_ids("<|end|>") # sometimes model stops generating at <|end|>
]

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

generation_args = {
    "max_new_tokens": 500,
    "return_full_text": False,
    "temperature": 0.0,
    "do_sample": False,
    "streamer": streamer,
    "eos_token_id": terminators,
}

output = pipe(messages, **generation_args)
print(output[0]['generated_text'])


```
