---
license: cc-by-nc-4.0
tags:
- galactica

widget:
- text: "The Transformer architecture [START_REF]"
- text: "The Schwarzschild radius is defined as: \\["
- text: "A force of 0.6N is applied to an object, which accelerates at 3m/s. What is its mass? <work>"
- text: "Lecture 1: The Ising Model\n\n"
- text: "[START_I_SMILES]"
- text: "[START_AMINO]GHMQSITAGQKVISKHKNGRFYQCEVVRLTTETFYEVNFDDGSFSDNLYPEDIVSQDCLQFGPPAEGEVVQVRWTDGQVYGAKFVASHPIQMYQVEFEDGSQLVVKRDDVYTLDEELP[END_AMINO] ## Keywords"
inference: false
---

![logo](https://s3.amazonaws.com/moonup/production/uploads/1668679814649-62441d1d9fdefb55a0b7d12c.png)


# GALACTICA 6.7B (standard)

Model card from the original [repo](https://github.com/paperswithcode/galai/blob/main/docs/model_card.md) 

Following [Mitchell et al. (2018)](https://arxiv.org/abs/1810.03993), this model card provides information about the GALACTICA model, how it was trained, and the intended use cases. Full details about how the model was trained and evaluated can be found in the [release paper](https://galactica.org/paper.pdf).

## Model Details

The GALACTICA models are trained on a large-scale scientific corpus. The models are designed to perform scientific tasks, including but not limited to citation prediction, scientific QA, mathematical reasoning, summarization, document generation, molecular property prediction and entity extraction. The models were developed by the Papers with Code team at Meta AI to study the use of language models for the automatic organization of science. We train models with sizes ranging from 125M to 120B parameters. Below is a summary of the released models:

|  Size       | Parameters  |
|:-----------:|:-----------:|
| `mini`      |    125 M    |
| `base`      |    1.3 B    |
| `standard`  |    6.7 B    |
| `large`     |     30 B    |
| `huge`      |    120 B    |


## Release Date

November 2022

## Model Type

Transformer based architecture in a decoder-only setup with a few modifications (see paper for more details). 

## Paper & Demo

[Paper](https://galactica.org/paper.pdf) / [Demo](https://galactica.org)

## Model Use 

The primary intended users of the GALACTICA models are researchers studying language models applied to the scientific domain. We also anticipate the model will be useful for developers who wish to build scientific tooling. However, we caution against production use without safeguards given the potential of language models to hallucinate.

The models are made available under a non-commercial CC BY-NC 4.0 license. More information about how to use the model can be found in the README.md of this repository.

## Training Data

The GALACTICA models are trained on 106 billion tokens of open-access scientific text and data. This includes papers, textbooks, scientific websites, encyclopedias, reference material, knowledge bases, and more. We tokenize different modalities to provide a natural langauge interface for different tasks. See the README.md for more information. See the paper for full information on the training data.

## How to use

Find below some example scripts on how to use the model in `transformers`:

## Using the Pytorch model

### Running the model on a CPU

<details>
<summary> Click to expand </summary>

```python

from transformers import AutoTokenizer, OPTForCausalLM

tokenizer = AutoTokenizer.from_pretrained("facebook/galactica-6.7b")
model = OPTForCausalLM.from_pretrained("facebook/galactica-6.7b")

input_text = "The Transformer architecture [START_REF]"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
```

</details>

### Running the model on a GPU

<details>
<summary> Click to expand </summary>

```python
# pip install accelerate
from transformers import AutoTokenizer, OPTForCausalLM

tokenizer = AutoTokenizer.from_pretrained("facebook/galactica-6.7b")
model = OPTForCausalLM.from_pretrained("facebook/galactica-6.7b", device_map="auto")

input_text = "The Transformer architecture [START_REF]"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
```

</details>

### Running the model on a GPU using different precisions

#### FP16

<details>
<summary> Click to expand </summary>

```python
# pip install accelerate
import torch
from transformers import AutoTokenizer, OPTForCausalLM

tokenizer = AutoTokenizer.from_pretrained("facebook/galactica-6.7b")
model = OPTForCausalLM.from_pretrained("facebook/galactica-6.7b", device_map="auto", torch_dtype=torch.float16)

input_text = "The Transformer architecture [START_REF]"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
```

</details>

#### INT8

<details>
<summary> Click to expand </summary>

```python
# pip install bitsandbytes accelerate
from transformers import AutoTokenizer, OPTForCausalLM

tokenizer = AutoTokenizer.from_pretrained("facebook/galactica-6.7b")
model = OPTForCausalLM.from_pretrained("facebook/galactica-6.7b", device_map="auto", load_in_8bit=True)

input_text = "The Transformer architecture [START_REF]"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
```

</details>


## Performance and Limitations

The model outperforms several existing language models on a range of knowledge probes, reasoning, and knowledge-intensive scientific tasks. This also extends to general NLP tasks, where GALACTICA outperforms other open source general language models. That being said, we note a number of limitations in this section.

As with other language models, GALACTICA is often prone to hallucination - and training on a high-quality academic corpus does not prevent this, especially for less popular and less cited scientific concepts. There are no guarantees of truthful output when generating from the model. This extends to specific modalities such as citation prediction. While GALACTICA's citation behaviour approaches the ground truth citation behaviour with scale, the model continues to exhibit a popularity bias at larger scales.

In addition, we evaluated the model on several types of benchmarks related to stereotypes and toxicity. Overall, the model exhibits substantially lower toxicity rates compared to other large language models. That being said, the model continues to exhibit bias on certain measures (see the paper for details). So we recommend care when using the model for generations.

## Broader Implications

GALACTICA can potentially be used as a new way to discover academic literature. We also expect a lot of downstream use for application to particular domains, such as mathematics, biology, and chemistry. In the paper, we demonstrated several examples of the model acting as alternative to standard search tools. We expect a new generation of scientific tools to be built upon large language models such as GALACTICA.

We encourage researchers to investigate beneficial and new use cases for these models. That being said, it is important to be aware of the current limitations of large language models. Researchers should pay attention to common issues such as hallucination and biases that could emerge from using these models.


## Citation

```bibtex
@inproceedings{GALACTICA,
    title={GALACTICA: A Large Language Model for Science},
    author={Ross Taylor and Marcin Kardas and Guillem Cucurull and Thomas Scialom and Anthony Hartshorn and Elvis Saravia and Andrew Poulton and Viktor Kerkez and Robert Stojnic},
    year={2022}
}
```