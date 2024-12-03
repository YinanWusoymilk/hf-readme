---
license: [llama2, other]
datasets:
- cerebras/SlimPajama-627B
language:
- en
pipeline_tag: text-generation
tags:
- Deci AI
- DeciLM
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
      value: 42.06
      verified: false
  - task:
      type: text-generation
    dataset:
      type: ai2/arc
      name: ai2_arc
    metrics:
    - name: ARC Easy
      type: ARC Easy
      value: 70.02
      verified: false
  - task:
      type: text-generation
    dataset:
      type: boolq
      name: boolq
    metrics:
    - name: BoolQ
      type: BoolQ
      value: 71.01
      verified: false
  - task:
      type: text-generation
    dataset:
      type: hellaswag
      name: hellaswag
    metrics:
    - name: HellaSwag
      type: HellaSwag
      value: 74.58
      verified: false
  - task:
      type: text-generation
    dataset:
      type: LAMBDA
      name: OpenAI LAMBDA
    metrics:
    - name: LAMBDA
      type: LAMBDA
      value: 69.78
      verified: false
  - task:
      type: text-generation
    dataset:
      type: OpenBookQA
      name: openbookqa
    metrics:
    - name: OpenBookQA
      type: OpenBookQA
      value: 34
      verified: false
  - task:
      type: text-generation
    dataset:
      type: PIQA
      name: piqa
    metrics:
    - name: PIQA
      type: PIQA
      value: 77.09
      verified: false
  - task:
      type: text-generation
    dataset:
      type: truthful_qa
      name: truthful_qa
    metrics:
    - name: TruthfulQA
      type: TruthfulQA
      value: 36.19
      verified: false
  - task:
      type: text-generation
    dataset:
      type: winogrande
      name: winogrande
    metrics:
    - name: Winogrande
      type: Winogrande
      value: 68.03
      verified: false
---
# DeciLM 6B

DeciLM 6B is a 5.7 billion parameter decoder-only text generation model. With a context window of 4096 tokens, the highly efficient model uses variable Grouped-Query Attention (GQA) to achieve an optimal balance between performance and computational efficiency. The model's architecture was generated using Deci's proprietary Neural Architecture Search-based technology, AutoNAC. 
## Model Details

### Model Description

Deci developed and publically released the DeciLM 6B large language model, a pretrained, high-efficiency generative text model with 5.7 billion parameters. DeciLM 6B outpaces pretrained models in its class, with a throughput that's up to 15 times that of Llama 2 7B's. DeciLM-6B was further fine-tuned using [LoRA ](https://arxiv.org/pdf/2106.09685.pdf)  for instruction following on a subset of the OpenOrca dataset, creating [DeciLM 6B-Instruct](https://huggingface.co/Deci/DeciLM-6b-instruct) 

- **Developed by:** Deci
- **Model type:** DeciLM is an auto-regressive language model using an optimized transformer decoder architecture that includes variable Grouped-Query Attention.
- **Language(s) (NLP):** English
- **License:**  [Llama 2 Community License Agreement](https://huggingface.co/Deci/DeciLM-6b/blob/main/LICENSE.md) with an extention of Deci regarding hosting service providers.

## Model Architecture

| Parameters | Layers | Heads  | Sequence Length  | GQA num_key_value_heads*  | Hidden Size  |
|:----------|:----------|:----------|:----------|:----------|:----------|
| 5.7B    | 32    | 32    | 4096   | Variable  | 4096 |  |

*AutoNAC was employed to optimize the selection of the GQA num_key_value_heads for each layer of the model.

- **Decoder layer:** Varible Grouped Query Attention. Grouped Query Attention (GQA) was introduced in [Ainslie et al., 2023](https://arxiv.org/abs/2305.13245)
- **Position Embeddings:** Dynamic NTK Scaling Rotary Position Embeddings [Su et al., 2021](https://arxiv.org/abs/2104.09864)


### Model Sources

- **Paper:** [DeciLM Technical Blog](https://deci.ai/blog/decilm-15-times-faster-than-llama2-nas-generated-llm-with-variable-gqa/?utm_campaign=repos&utm_source=hugging-face&utm_medium=model-card&utm_content=decilm-6b)
- **Demo:** [DeciLM 6B Instruct Demo](https://huggingface.co/spaces/Deci/DeciLM-6b-instruct)
- **Notebook:** [DeciLM 6B Notebook](https://colab.research.google.com/drive/1LugJCifOv0L426ukRHjOblBRWwUImAit)

## Uses

The model is intended for commercial and research use in English and can be fine-tuned for use in other languages.

## How to Get Started with the Model

Use the code below to get started with the model.

```bibtex
# pip install -q transformers

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "Deci/DeciLM-6b"
device = "cuda" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint, torch_dtype=torch.bfloat16, trust_remote_code=True).to(device)

inputs = tokenizer.encode("In a shocking finding, scientists discovered a herd of unicorns living in", return_tensors="pt").to(device)
outputs = model.generate(inputs, max_new_tokens=100, do_sample=True, top_p=0.95)
print(tokenizer.decode(outputs[0]))
```

## Training Details

DeciLM 6B underwent training utilizing a subset of the SlimPajamas dataset, leveraging advanced proprietary methodologies allowing for fast training.

## Evaluation

Below are DeciLM's 6B evaluation results.

| Average | ARC Challenge* | ARC Easy* | BoolQ | HellaSwag* | LAMBDA OpenAI | OpenBookQA | PIQA | TruthfulQA | Winogrande |
|:----------|:----------|:----------|:----------|:----------|:----------|:----------|:----------|:----------|:----------|
| 60.33    | 42.06    | 70.02    | 71.01    | 74.58    | 69.78    | 34    | 77.09    |36.19    | 68.03    | 
Accuracy-norm score*


### Runtime Benchmarks

|Inference Tool/Hardware | A10 (tokens/sec) |
|:----------|:----------|
| PyTorch  | 652.49 | 
| Infery LLM | 2,029.6  | 

- Throughput (tokens/sec) - Measured with optimal batch - PyTorch BS 64, Infery LLM BS 128
- In order to replicate the results of the PyTorch benchmark, use this [code example](https://huggingface.co/Deci/DeciLM-6b/blob/main/hf_benchmark_example.py)


## How to Cite

Please cite this model using this format.

```bibtex
@misc{DeciFoundationModels,
title = {DeciLM 6B},
author = {DeciAI Research Team},
year = {2023}
url={[https://huggingface.co/Deci/DeciLM-6b](https://huggingface.co/Deci/DeciLM-6b)},
}
```