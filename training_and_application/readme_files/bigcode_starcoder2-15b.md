---
pipeline_tag: text-generation
inference:
  parameters:
    temperature: 0.2
    top_p: 0.95
widget:
- text: 'def print_hello_world():'
  example_title: Hello world
  group: Python
datasets:
- bigcode/the-stack-v2-train
license: bigcode-openrail-m
library_name: transformers
tags:
- code
model-index:
- name: starcoder2-15b
  results:
  - task:
      type: text-generation
    dataset:
      name: CruxEval-I
      type: cruxeval-i
    metrics:
    - type: pass@1
      value: 48.1
  - task:
      type: text-generation
    dataset:
      name: DS-1000
      type: ds-1000
    metrics:
    - type: pass@1
      value: 33.8
  - task:
      type: text-generation
    dataset:
      name: GSM8K (PAL)
      type: gsm8k-pal
    metrics:
    - type: accuracy
      value: 65.1
  - task:
      type: text-generation
    dataset:
      name: HumanEval+
      type: humanevalplus
    metrics:
    - type: pass@1
      value: 37.8
  - task:
      type: text-generation
    dataset:
      name: HumanEval
      type: humaneval
    metrics:
    - type: pass@1
      value: 46.3
  - task:
      type: text-generation
    dataset:
      name: RepoBench-v1.1
      type: repobench-v1.1
    metrics:
    - type: edit-smiliarity
      value: 74.08
---

# StarCoder2

<center>
    <img src="https://huggingface.co/datasets/bigcode/admin_private/resolve/main/starcoder2_banner.png" alt="SC2" width="900" height="600">
</center>

##  Table of Contents

1. [Model Summary](#model-summary)
2. [Use](#use)
3. [Limitations](#limitations)
4. [Training](#training)
5. [License](#license)
6. [Citation](#citation)

## Model Summary

StarCoder2-15B model is a 15B parameter model trained on 600+ programming languages from [The Stack v2](https://huggingface.co/datasets/bigcode/the-stack-v2-train), with opt-out requests excluded. The model uses [Grouped Query Attention](https://arxiv.org/abs/2305.13245), [a context window of 16,384 tokens](https://arxiv.org/abs/2205.14135) with [a sliding window attention of 4,096 tokens](https://arxiv.org/abs/2004.05150v2),  and was trained using the [Fill-in-the-Middle objective](https://arxiv.org/abs/2207.14255) on 4+ trillion tokens.  
The model was trained with [NVIDIA NeMo™ Framework](https://www.nvidia.com/en-us/ai-data-science/generative-ai/nemo-framework/) using the [NVIDIA Eos Supercomputer](https://blogs.nvidia.com/blog/eos/) built with [NVIDIA DGX H100](https://www.nvidia.com/en-us/data-center/dgx-h100/) systems.

- **Project Website:** [bigcode-project.org](https://www.bigcode-project.org)
- **Paper:** [Link](https://huggingface.co/papers/2402.19173)
- **Point of Contact:** [contact@bigcode-project.org](mailto:contact@bigcode-project.org)
- **Languages:** 600+ Programming languages

## Use

### Intended use

The model was trained on GitHub code as well as additional selected data sources such as Arxiv and Wikipedia. As such it is _not_ an instruction model and commands like "Write a function that computes the square root." do not work well.

### Generation
Here are some examples to get started with the model. You can find a script for fine-tuning in StarCoder2's [GitHub repository](https://github.com/bigcode-project/starcoder2).

First, make sure to install `transformers` from source:
```bash
pip install git+https://github.com/huggingface/transformers.git
```

#### Running the model on CPU/GPU/multi GPU
* _Using full precision_
```python
# pip install git+https://github.com/huggingface/transformers.git # TODO: merge PR to main
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigcode/starcoder2-15b"
device = "cuda" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# for multiple GPUs install accelerate and do `model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto")`
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to(device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```

* _Using `torch.bfloat16`_
```python
# pip install accelerate
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

checkpoint = "bigcode/starcoder2-15b"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

# for fp16 use `torch_dtype=torch.float16` instead
model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto", torch_dtype=torch.bfloat16)

inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to("cuda")
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```
```bash
>>> print(f"Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")
Memory footprint: 32251.33 MB
```

#### Quantized Versions through `bitsandbytes`
* _Using 8-bit precision (int8)_

```python
# pip install bitsandbytes accelerate
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# to use 4bit use `load_in_4bit=True` instead
quantization_config = BitsAndBytesConfig(load_in_8bit=True)

checkpoint = "bigcode/starcoder2-15b"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint, quantization_config=quantization_config)

inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to("cuda")
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```
```bash
>>> print(f"Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")
# load_in_8bit
Memory footprint: 16900.18 MB
# load_in_4bit
>>> print(f"Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")
Memory footprint: 9224.60 MB
```
### Attribution & Other Requirements

The pretraining dataset of the model was filtered for permissive licenses and code with no license only. Nevertheless, the model can generate source code verbatim from the dataset. The code's license might require attribution and/or other specific requirements that must be respected. We provide a [search index](https://huggingface.co/spaces/bigcode/search-v2) that let's you search through the pretraining data to identify where generated code came from and apply the proper attribution to your code.

# Limitations

The model has been trained on source code from 600+ programming languages. The predominant language in source is English although other languages are also present. As such the model is capable to generate code snippets provided some context but the generated code is not guaranteed to work as intended. It can be inefficient, contain bugs or exploits. See [the paper](https://huggingface.co/papers/2402.19173) for an in-depth discussion of the model limitations. 

# Training

## Model

- **Architecture:** Transformer decoder with grouped-query and sliding window attention and Fill-in-the-Middle objective
- **Pretraining steps:** 1 million
- **Pretraining tokens:** 4+ trillion
- **Precision:** bfloat16

## Hardware

- **GPUs:** 1024 x H100

## Software

- **Framework:** [NeMo Framework](https://www.nvidia.com/en-us/ai-data-science/generative-ai/nemo-framework/) 
- **Neural networks:** [PyTorch](https://github.com/pytorch/pytorch)

# License

The model is licensed under the BigCode OpenRAIL-M v1 license agreement. You can find the full agreement [here](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement).

# Citation

```bash
@misc{lozhkov2024starcoder,
      title={StarCoder 2 and The Stack v2: The Next Generation}, 
      author={Anton Lozhkov and Raymond Li and Loubna Ben Allal and Federico Cassano and Joel Lamy-Poirier and Nouamane Tazi and Ao Tang and Dmytro Pykhtar and Jiawei Liu and Yuxiang Wei and Tianyang Liu and Max Tian and Denis Kocetkov and Arthur Zucker and Younes Belkada and Zijian Wang and Qian Liu and Dmitry Abulkhanov and Indraneil Paul and Zhuang Li and Wen-Ding Li and Megan Risdal and Jia Li and Jian Zhu and Terry Yue Zhuo and Evgenii Zheltonozhskii and Nii Osae Osae Dade and Wenhao Yu and Lucas Krauß and Naman Jain and Yixuan Su and Xuanli He and Manan Dey and Edoardo Abati and Yekun Chai and Niklas Muennighoff and Xiangru Tang and Muhtasham Oblokulov and Christopher Akiki and Marc Marone and Chenghao Mou and Mayank Mishra and Alex Gu and Binyuan Hui and Tri Dao and Armel Zebaze and Olivier Dehaene and Nicolas Patry and Canwen Xu and Julian McAuley and Han Hu and Torsten Scholak and Sebastien Paquet and Jennifer Robinson and Carolyn Jane Anderson and Nicolas Chapados and Mostofa Patwary and Nima Tajbakhsh and Yacine Jernite and Carlos Muñoz Ferrandis and Lingming Zhang and Sean Hughes and Thomas Wolf and Arjun Guha and Leandro von Werra and Harm de Vries},
      year={2024},
      eprint={2402.19173},
      archivePrefix={arXiv},
      primaryClass={cs.SE}
}
```