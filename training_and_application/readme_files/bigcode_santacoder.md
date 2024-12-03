---
license: bigcode-openrail-m
datasets:
- bigcode/the-stack
language:
- code
programming_language:
- Java
- JavaScript
- Python
pipeline_tag: text-generation
inference: true
widget:
- text: 'def print_hello_world():'
  example_title: Hello world
  group: Python
model-index:
- name: SantaCoder
  results:
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL HumanEval (Python)
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.18
      verified: false
    - name: pass@10
      type: pass@10
      value: 0.29
      verified: false
    - name: pass@100
      type: pass@100
      value: 0.49
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL MBPP (Python)
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.35
      verified: false
    - name: pass@10
      type: pass@10
      value: 0.58
      verified: false
    - name: pass@100
      type: pass@100
      value: 0.77
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL HumanEval (JavaScript)
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.16
      verified: false
    - name: pass@10
      type: pass@10
      value: 0.27
      verified: false
    - name: pass@100
      type: pass@100
      value: 0.47
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL MBPP (Javascript)
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.28
      verified: false
    - name: pass@10
      type: pass@10
      value: 0.51
      verified: false
    - name: pass@100
      type: pass@100
      value: 0.7
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL HumanEval (Java)
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.15
      verified: false
    - name: pass@10
      type: pass@10
      value: 0.26
      verified: false
    - name: pass@100
      type: pass@100
      value: 0.41
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL MBPP (Java)
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.28
      verified: false
    - name: pass@10
      type: pass@10
      value: 0.44
      verified: false
    - name: pass@100
      type: pass@100
      value: 0.59
      verified: false
  - task:
      type: text-generation
    dataset:
      type: loubnabnl/humaneval_infilling
      name: HumanEval FIM (Python)
    metrics:
    - name: single_line
      type: exact_match
      value: 0.44
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL HumanEval FIM (Java)
    metrics:
    - name: single_line
      type: exact_match
      value: 0.62
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL HumanEval FIM (JavaScript)
    metrics:
    - name: single_line
      type: exact_match
      value: 0.6
      verified: false
  - task:
      type: text-generation
    dataset:
      type: code_x_glue_ct_code_to_text
      name: CodeXGLUE code-to-text (Python)
    metrics:
    - name: BLEU
      type: bleu
      value: 18.13
      verified: false
---

# SantaCoder

![banner](https://huggingface.co/datasets/bigcode/admin/resolve/main/banner.png)

Play with the model on the [SantaCoder Space Demo](https://huggingface.co/spaces/bigcode/santacoder-demo).

#  Table of Contents

1. [Model Summary](#model-summary)
2. [Use](#use)
3. [Limitations](#limitations)
4. [Training](#training)
5. [License](#license)
6. [Citation](#citation)

# Model Summary

The SantaCoder models are a series of 1.1B parameter models trained on the Python, Java, and JavaScript subset of [The Stack (v1.1)](https://huggingface.co/datasets/bigcode/the-stack) (which excluded opt-out requests). 
The main model uses [Multi Query Attention](https://arxiv.org/abs/1911.02150), a context window of 2048 tokens, and was trained using near-deduplication and comment-to-code ratio as filtering criteria and using the [Fill-in-the-Middle objective](https://arxiv.org/abs/2207.14255).
In addition there are several models that were trained on datasets with different filter parameters and with architecture and objective variations. 

- **Repository:** [bigcode/Megatron-LM](https://github.com/bigcode-project/Megatron-LM)
- **Project Website:** [bigcode-project.org](https://www.bigcode-project.org)
- **Paper:** [🎅SantaCoder: Don't reach for the stars!🌟](https://arxiv.org/abs/2301.03988)
- **Point of Contact:** [contact@bigcode-project.org](mailto:contact@bigcode-project.org)
- **Languages:** Python, Java, and JavaScript

|Model|Architecture|Objective|Filtering|
|:-|:-|:-|:-|
|`mha`|MHA|AR + FIM| Base |
|`no-fim`| MQA | AR| Base |
|`fim`| MQA | AR + FIM | Base |
|`stars`| MQA | AR + FIM | GitHub stars |
|`fertility`| MQA | AR + FIM | Tokenizer fertility |
|`comments`| MQA | AR + FIM | Comment-to-code ratio |
|`dedup-alt`| MQA | AR + FIM | Stronger near-deduplication |
|`final`| MQA | AR + FIM | Stronger near-deduplication and comment-to-code ratio |

The `final` model is the best performing model and was trained twice as long (236B tokens) as the others. This checkpoint is the default model and available on the `main` branch. All other checkpoints are on separate branches with according names.

# Use

## Intended use

The model was trained on GitHub code. As such it is _not_ an instruction model and commands like "Write a function that computes the square root." do not work well.
You should phrase commands like they occur in source code such as comments (e.g. `# the following function computes the sqrt`) or write a function signature and docstring and let the model complete the function body.

**Feel free to share your generations in the Community tab!**

## How to use

### Generation
```python
# pip install -q transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigcode/santacoder"
device = "cuda" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True).to(device)

inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to(device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```

### Fill-in-the-middle
Fill-in-the-middle uses special tokens to identify the prefix/middle/suffix part of the input and output:

```python
input_text = "<fim-prefix>def print_hello_world():\n    <fim-suffix>\n    print('Hello world!')<fim-middle>"
inputs = tokenizer.encode(input_text, return_tensors="pt").to(device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```
Make sure to use `<fim-prefix>, <fim-suffix>, <fim-middle>` and not  `<fim_prefix>, <fim_suffix>, <fim_middle>` as in StarCoder models.

### Load other checkpoints
We upload the checkpoint of each experiment to a separate branch as well as the intermediate checkpoints as commits on the branches. You can load them with the `revision` flag:

```python
model = AutoModelForCausalLM.from_pretrained(
    "bigcode/santacoder",
    revision="no-fim", # name of branch or commit hash
    trust_remote_code=True
)
```

### Attribution & Other Requirements

The pretraining dataset of the model was filtered for permissive licenses only. Nevertheless, the model can generate source code verbatim from the dataset. The code's license might require attribution and/or other specific requirements that must be respected. We provide a [search index](https://huggingface.co/spaces/bigcode/santacoder-search) that let's you search through the pretraining data to identify where generated code came from and apply the proper attribution to your code.

# Limitations

The model has been trained on source code in Python, Java, and JavaScript. The predominant language in source is English although other languages are also present. As such the model is capable to generate code snippets provided some context but the generated code is not guaranteed to work as intended. It can be inefficient, contain bugs or exploits.

# Training

## Model

- **Architecture:** GPT-2 model with multi-query attention and Fill-in-the-Middle objective
- **Pretraining steps:** 600K
- **Pretraining tokens:** 236 billion
- **Precision:** float16

## Hardware

- **GPUs:** 96 Tesla V100
- **Training time:** 6.2 days
- **Total FLOPS:** 2.1 x 10e21

## Software

- **Orchestration:** [Megatron-LM](https://github.com/bigcode-project/Megatron-LM)
- **Neural networks:** [PyTorch](https://github.com/pytorch/pytorch)
- **FP16 if applicable:** [apex](https://github.com/NVIDIA/apex)

# License
The model is licensed under the BigCode OpenRAIL-M v1 license agreement. You can find the full agreement [here](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement).

# Citation
```
@article{allal2023santacoder,
  title={SantaCoder: don't reach for the stars!},
  author={Allal, Loubna Ben and Li, Raymond and Kocetkov, Denis and Mou, Chenghao and Akiki, Christopher and Ferrandis, Carlos Munoz and Muennighoff, Niklas and Mishra, Mayank and Gu, Alex and Dey, Manan and others},
  journal={arXiv preprint arXiv:2301.03988},
  year={2023}
}
```