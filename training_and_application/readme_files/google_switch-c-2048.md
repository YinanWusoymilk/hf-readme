---
language: 
- en

tags:
- text2text-generation

widget:
- text: "The <extra_id_0> walks in <extra_id_1> park"
  example_title: "Masked Language Modeling"

datasets:
- c4

inference: false
license: apache-2.0
---

# Model Card for Switch Transformers C - 2048 experts (1.6T parameters for 3.1 TB)

![model image](https://cdn-uploads.huggingface.co/production/uploads/1666966931908-62441d1d9fdefb55a0b7d12c.png)

#  Table of Contents

0. [TL;DR](#TL;DR)
1. [Model Details](#model-details)
2. [Usage](#usage)
3. [Uses](#uses)
4. [Bias, Risks, and Limitations](#bias-risks-and-limitations)
5. [Training Details](#training-details)
6. [Evaluation](#evaluation)
7. [Environmental Impact](#environmental-impact)
8. [Citation](#citation)
9. [Model Card Authors](#model-card-authors)

# TL;DR

Switch Transformers is a Mixture of Experts (MoE) model trained on Masked Language Modeling (MLM) task. The model architecture is similar to the classic T5, but with the Feed Forward layers replaced by the Sparse MLP layers containing "experts" MLP. According to the [original paper](https://arxiv.org/pdf/2101.03961.pdf) the model enables faster training (scaling properties) while being better than T5 on fine-tuned tasks. 
As mentioned in the first few lines of the abstract : 
>  we advance the current scale of language models by pre-training up to trillion parameter models on the “Colossal Clean Crawled Corpus”, and achieve a 4x speedup over the T5-XXL model.

**Disclaimer**: Content from **this** model card has been written by the Hugging Face team, and parts of it were copy pasted from the [original paper](https://arxiv.org/pdf/2101.03961.pdf).

# Model Details

## Model Description


- **Model type:** Language model
- **Language(s) (NLP):** English
- **License:** Apache 2.0
- **Related Models:** [All FLAN-T5 Checkpoints](https://huggingface.co/models?search=switch)
- **Original Checkpoints:** [All Original FLAN-T5 Checkpoints](https://github.com/google-research/t5x/blob/main/docs/models.md#mixture-of-experts-moe-checkpoints)
- **Resources for more information:**
  - [Research paper](https://arxiv.org/pdf/2101.03961.pdf)
  - [GitHub Repo](https://github.com/google-research/t5x)
  - [Hugging Face Switch Transformers Docs (Similar to T5) ](https://huggingface.co/docs/transformers/model_doc/switch_transformers)

# Usage

Note that these checkpoints has been trained on Masked-Language Modeling (MLM) task. Therefore the checkpoints are not "ready-to-use" for downstream tasks. You may want to check `FLAN-T5` for running fine-tuned weights or fine-tune your own MoE following [this notebook](https://colab.research.google.com/drive/1aGGVHZmtKmcNBbAwa9hbu58DDpIuB5O4?usp=sharing)

Find below some example scripts on how to use the model in `transformers` - bear in mind that the model is **extremely** large, so you may consider using disk offload from `accelerate`:

## Using the Pytorch model

### Running the model on a CPU

<details>
<summary> Click to expand </summary>

```python
# pip install accelerate
from transformers import AutoTokenizer, SwitchTransformersForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("google/switch-c-2048")
model = SwitchTransformersForConditionalGeneration.from_pretrained("google/switch-c-2048", device_map="auto", offload_folder=<OFFLOAD_FOLDER>)

input_text = "A <extra_id_0> walks into a bar a orders a <extra_id_1> with <extra_id_2> pinch of <extra_id_3>."
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
>>> <pad> <extra_id_0> man<extra_id_1> beer<extra_id_2> a<extra_id_3> salt<extra_id_4>.</s>
```

</details>

### Running the model on a GPU

<details>
<summary> Click to expand </summary>

```python
# pip install accelerate
from transformers import AutoTokenizer, SwitchTransformersForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("google/switch-c-2048")
model = SwitchTransformersForConditionalGeneration.from_pretrained("google/switch-c-2048", device_map="auto", offload_folder=<OFFLOAD_FOLDER>)

input_text = "A <extra_id_0> walks into a bar a orders a <extra_id_1> with <extra_id_2> pinch of <extra_id_3>."
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(0)

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
>>> <pad> <extra_id_0> man<extra_id_1> beer<extra_id_2> a<extra_id_3> salt<extra_id_4>.</s>
```

</details>

### Running the model on a GPU using different precisions

#### BF16

<details>
<summary> Click to expand </summary>

```python
# pip install accelerate
from transformers import AutoTokenizer, SwitchTransformersForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("google/switch-c-2048")
model = SwitchTransformersForConditionalGeneration.from_pretrained("google/switch-c-2048", device_map="auto", torch_dtype=torch.bfloat16, offload_folder=<OFFLOAD_FOLDER>)

input_text = "A <extra_id_0> walks into a bar a orders a <extra_id_1> with <extra_id_2> pinch of <extra_id_3>."
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(0)

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
>>> <pad> <extra_id_0> man<extra_id_1> beer<extra_id_2> a<extra_id_3> salt<extra_id_4>.</s>
```

</details>

#### INT8

<details>
<summary> Click to expand </summary>

```python
# pip install bitsandbytes accelerate
from transformers import AutoTokenizer, SwitchTransformersForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("google/switch-c-2048")
model = SwitchTransformersForConditionalGeneration.from_pretrained("google/switch-c-2048", device_map="auto", offload_folder=<OFFLOAD_FOLDER>)

input_text = "A <extra_id_0> walks into a bar a orders a <extra_id_1> with <extra_id_2> pinch of <extra_id_3>."
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(0)

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
>>> <pad> <extra_id_0> man<extra_id_1> beer<extra_id_2> a<extra_id_3> salt<extra_id_4>.</s>
```

</details>

# Uses

## Direct Use and Downstream Use

See the [research paper](https://arxiv.org/pdf/2101.03961.pdf) for further details.

## Out-of-Scope Use

More information needed.

# Bias, Risks, and Limitations

More information needed.

## Ethical considerations and risks

More information needed.

## Known Limitations

More information needed.

## Sensitive Use:

More information needed.

# Training Details

## Training Data

The model was trained on a Masked Language Modeling task, on Colossal Clean Crawled Corpus (C4) dataset, following the same procedure as `T5`.


## Training Procedure

According to the model card from the [original paper](https://arxiv.org/pdf/2101.03961.pdf) the model has been trained on TPU v3 or TPU v4 pods, using [`t5x`](https://github.com/google-research/t5x) codebase together with [`jax`](https://github.com/google/jax).


# Evaluation

## Testing Data, Factors & Metrics

The authors evaluated the model on various tasks and compared the results against T5. See the table below for some quantitative evaluation:
![image.png](https://s3.amazonaws.com/moonup/production/uploads/1666967660372-62441d1d9fdefb55a0b7d12c.png)
For full details, please check the [research paper](https://arxiv.org/pdf/2101.03961.pdf).

## Results 

For full results for Switch Transformers, see the [research paper](https://arxiv.org/pdf/2101.03961.pdf), Table 5.

# Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** Google Cloud TPU Pods - TPU v3 or TPU v4  | Number of chips ≥ 4.
- **Hours used:** More information needed
- **Cloud Provider:** GCP
- **Compute Region:** More information needed
- **Carbon Emitted:** More information needed

# Citation

**BibTeX:**

```bibtex
@misc{https://doi.org/10.48550/arxiv.2101.03961,
  doi = {10.48550/ARXIV.2101.03961},
  
  url = {https://arxiv.org/abs/2101.03961},
  
  author = {Fedus, William and Zoph, Barret and Shazeer, Noam},
  
  keywords = {Machine Learning (cs.LG), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity},
  
  publisher = {arXiv},
  
  year = {2021},
  
  copyright = {arXiv.org perpetual, non-exclusive license}
}

```