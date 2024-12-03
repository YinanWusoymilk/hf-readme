---
license: apache-2.0
datasets:
- bigcode/starcoderdata
language:
- code
pipeline_tag: text-generation
---

# CodeGen2.5-7B-multi

Title: [**CodeGen2.5: Small, but mighty**](https://blog.salesforceairesearch.com/codegen25)

Authors: [Erik Nijkamp](https://eriknijkamp.com)\*, [Hiroaki Hayashi](https://hiroakih.me)\*, Yingbo Zhou, Caiming Xiong

(\* equal contribution)

## Model description

[CodeGen2.5](https://github.com/salesforce/CodeGen) is a family of autoregressive language models for **program synthesis**.

Building upon [CodeGen2](https://arxiv.org/abs/2305.02309), the model is trained on [StarCoderData](https://huggingface.co/datasets/bigcode/starcoderdata) for 1.4T tokens, achieving competitive results compared to StarCoderBase-15.5B with less than half the size.

Like CodeGen2, this model is capable of infilling, and supports multiple programming languages.

We then further train on Python, then on instruction data. We release all the models as follows:

* **CodeGen2.5-7B-multi** (this repo): Trained on StarCoderData. Licensed under Apache-2.0.
* **CodeGen2.5-7B-mono**: Further trained on additional Python tokens. Licensed under Apache-2.0.
* **CodeGen2.5-7B-instruct**: Further trained from CodeGen2.5-7B-mono on instruction data. *Research purposes only*.

## How to use

This model can be easily loaded using the `AutoModelForCausalLM` functionality.

### Pre-requisite

Please install OpenAI `tiktoken` for the tokenizer.

```bash
pip install tiktoken==0.4.0
```

### Causal sampling (code autocompletion)

For regular causal sampling, simply generate completions given the context:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen25-7b-multi", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen25-7b-multi")

text = "def hello_world():"
input_ids = tokenizer(text, return_tensors="pt").input_ids
generated_ids = model.generate(input_ids, max_length=128)
print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
```

### Infill sampling

For **infill** sampling, we follow the CodeGen2 format:

* `<mask_N>`: N-th span to be masked. In practice, use `<mask_1>` to where you want to sample infill.
* `<sep>`: Separator token between the suffix and the infilled sample. See below.
* `<eom>`: "End-Of-Mask" token that model will output at the end of infilling. You may use this token to truncate the output.

For example, if we want to generate infill for the following cursor position of a function:
```python
def hello_world():
    |
    return name
```
we construct an input to the model by

1. Inserting `<mask_1>` token in place of cursor position
2. Append `<sep>` token to indicate the boundary
3. Insert another `<mask_1>` to indicate which mask we want to infill.

The final snippet looks as follows:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen25-7b-multi", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen25-7b-multi")


def format(prefix, suffix):
  return prefix + "<mask_1>" + suffix + "<|endoftext|>" + "<sep>" + "<mask_1>"


prefix = "def hello_world():\n    "
suffix = "    return name"
text = format(prefix, suffix)
input_ids = tokenizer(text, return_tensors="pt").input_ids
generated_ids = model.generate(input_ids, max_length=128)
print(tokenizer.decode(generated_ids[0], skip_special_tokens=False)[len(text):])
```

You might want to truncate the model output with `<eom>`.

## Evaluation results

We evaluate our models on HumanEval and HumanEval-Infill.
Please refer to the [blog](https://blog.salesforceairesearch.com/codegen25) for more details.

## Intended use and limitations

As an autoregressive language model, CodeGen2.5 is capable of extracting features from given natural language and programming language texts, and calculating the likelihood of them.
However, the model is intended for and best at **program synthesis**, that is, generating executable code given English prompts, where the prompts should be in the form of a comment string. The model can complete partially-generated code as well.

## Attribution & Other Requirements
The pretraining dataset of the model was filtered for permissive licenses only.
Nevertheless, the model can generate source code verbatim from the dataset.
The code's license might require attribution and/or other specific requirements that must be respected.
The data provider BigCode provides a [search index](https://huggingface.co/spaces/bigcode/starcoder-search) that lets you search through the pretraining data to identify where generated code came from and apply the proper attribution to your code.

## BibTeX entry and citation info

Please cite CodeGen2 paper:

```bibtex
@article{Nijkamp2023codegen2,
  title={CodeGen2: Lessons for Training LLMs on Programming and Natural Languages},
  author={Nijkamp, Erik and Hayashi, Hiroaki and Xiong, Caiming and Savarese, Silvio and Zhou, Yingbo},
  journal={arXiv preprint},
  year={2023}
}
```