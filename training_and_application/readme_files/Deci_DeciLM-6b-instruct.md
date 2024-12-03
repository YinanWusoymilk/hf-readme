---
license: [llama2, other]
datasets:
- cerebras/SlimPajama-627B
- Open-Orca/OpenOrca
language:
- en
tags:
- Deci AI
- DeciLM
- Instruction
model-index:
- name: DeciLM 6B
  results:
  - task:
      type: text-generation
    dataset:
      type: ai2/arc
      name: ai2_arc
    metrics:
    - name: ARC Challenge
      type: ARC Challenge
      value: 43.43
      verified: false
  - task:
      type: text-generation
    dataset:
      type: ai2/arc
      name: ai2_arc
    metrics:
    - name: ARC Easy
      type: ARC Easy
      value: 70.58
      verified: false
  - task:
      type: text-generation
    dataset:
      type: boolq
      name: boolq
    metrics:
    - name: BoolQ
      type: BoolQ
      value: 77.34
      verified: false
  - task:
      type: text-generation
    dataset:
      type: hellaswag
      name: hellaswag
    metrics:
    - name: HellaSwag
      type: HellaSwag
      value: 74.57
      verified: false
  - task:
      type: text-generation
    dataset:
      type: LAMBDA
      name: OpenAI LAMBDA
    metrics:
    - name: LAMBDA
      type: LAMBDA
      value: 70.1
      verified: false
  - task:
      type: text-generation
    dataset:
      type: OpenBookQA
      name: openbookqa
    metrics:
    - name: OpenBookQA
      type: OpenBookQA
      value: 33
      verified: false
  - task:
      type: text-generation
    dataset:
      type: PIQA
      name: piqa
    metrics:
    - name: PIQA
      type: PIQA
      value: 77.52
      verified: false
  - task:
      type: text-generation
    dataset:
      type: truthful_qa
      name: truthful_qa
    metrics:
    - name: TruthfulQA
      type: TruthfulQA
      value: 43.89
      verified: false
  - task:
      type: text-generation
    dataset:
      type: winogrande
      name: winogrande
    metrics:
    - name: Winogrande
      type: Winogrande
      value: 67.64
      verified: false
---
# DeciLM 6B-Instruct

DeciLM 6B-Instruct is a model for short-form instruction following. It is built by LoRA fine-tuning [DeciLM 6B](https://huggingface.co/Deci/DeciLM-6b) on a subset of the [OpenOrca dataset](https://huggingface.co/datasets/Open-Orca/OpenOrca).


- **Developed by:** Deci
- **Model type:** DeciLM is an auto-regressive language model using an optimized transformer decoder architecture that includes variable Grouped-Query Attention.
- **Language(s) (NLP):** English
- **License:**  [Llama 2 Community License Agreement](https://huggingface.co/Deci/DeciLM-6b-instruct/blob/main/LICENSE.md) with an extention of Deci regarding hosting service providers.

### Model Sources

- **Paper:** [DeciLM 6B Technical Blog](https://deci.ai/blog/decilm-15-times-faster-than-llama2-nas-generated-llm-with-variable-gqa/?utm_campaign=repos&utm_source=hugging-face&utm_medium=model-card&utm_content=decilm-6b-instruct)
- **Demo:** [DeciLM 6B-Instruct Demo](https://huggingface.co/spaces/Deci/DeciLM-6b-instruct)
- **Notebook:** [DeciLM 6B-Instruct Notebook](https://bit.ly/decilm-instruct-nb)

## Uses

The model is intended for commercial and research use in English and can be fine-tuned for use in other languages.

## How to Get Started with the Model

Use the code below to get started with the model.

```bibtex
# pip install -q transformers

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "Deci/DeciLM-6b-instruct"
device = "cuda" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint, torch_dtype=torch.bfloat16, trust_remote_code=True).to(device)

inputs = tokenizer.encode("How do I make french toast? Think through it step by step", return_tensors="pt").to(device)
outputs = model.generate(inputs, max_new_tokens=100, do_sample=True, top_p=0.95)
print(tokenizer.decode(outputs[0]))
```

## Training Details

DeciLM 6B underwent training utilizing the SlimPijamas dataset, leveraging advanced proprietary methodologies allowing for fast training. DeciLM 6B was further finetuned on a subset of the OpenOrca dataset, giving rise to DeciLM-6B-Instruct.

## Evaluation

Below are DeciLM's 6B-instruct evaluation results.

| Average | ARC Challenge* | ARC Easy* | BoolQ | HellaSwag* | LAMBDA OpenAI | OpenBookQA | PIQA | TruthfulQA | Winogrande |
|:----------|:----------|:----------|:----------|:----------|:----------|:----------|:----------|:----------|:----------|
| 62.01    | 44.43    | 70.58    | 77.34    | 74.57    | 70.1    | 33    | 77.52    |43.89    | 67.64    | 
Accuracy-norm score*


## Runtime Benchmarks

|Inference Tool/Hardware | A10 (tokens/sec) |
|:----------|:----------|
| PyTorch   | 652.49 | 
| Infery LLM | 2,029.6  | 

- Throughput (tokens/sec) - Measured with optimal batch - PyTorch BS 64, Infery LLM BS 128
- In order to replicate the results of the PyTorch benchmark, use this [code example](https://huggingface.co/Deci/DeciLM-6b-instruct/blob/main/hf_benchmark_example.py)

## Disclaimer

DeciLM 6B-Instruct has not been aligned for safety or trained using RLHF. 

## How to Cite

Please cite this model using this format.

```bibtex
@misc{DeciFoundationModels,
title = {DeciLM 6B Instruct},
author = {DeciAI Research Team},
year = {2023}
url={[https://huggingface.co/Deci/DeciLM-6b-instruct](https://huggingface.co/Deci/DeciLM-6b-instruct)},
}
```