---
inference: false
tags:
- text-generation
- opt

license: other
commercial: false
---
# OPT-IML

## Model Description

[OPT-IML (OPT + Instruction Meta-Learning)](https://arxiv.org/abs/2212.12017) is a set of instruction-tuned versions of OPT, on a collection of ~2000 NLP tasks gathered from 8 NLP benchmarks, called OPT-IML Bench.

We provide two model versions: 
* OPT-IML trained on 1500 tasks with several tasks held-out for purposes of downstream evaluation, and 
* OPT-IML-Max trained on all ~2000 tasks

### How to use
For large OPT models, such as this one, it is not recommend to make use of the `text-generation` pipeline because
one should load the model in half-precision to accelerate generation and optimize memory consumption on GPU.
It is recommended to directly call the [`generate`](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.generation_utils.GenerationMixin.generate)
 method as follows:

```python
>>> from transformers import AutoModelForCausalLM, AutoTokenizer
>>> import torch

>>> model = AutoModelForCausalLM.from_pretrained("facebook/opt-iml-30b", torch_dtype=torch.float16).cuda()

>>> # the fast tokenizer currently does not work correctly
>>> tokenizer = AutoTokenizer.from_pretrained("facebook/opt-iml-30b", use_fast=False)

>>> prompt = "What is the color of a carrot?\nA:"

>>> input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()

>>> generated_ids = model.generate(input_ids)

>>> tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
```

### Limitations and bias

While OPT-IML models outperform baseline OPT on an extensive set of evaluations,
nevertheless, they are susceptible to the various risks associated with using large language models
relating to factual correctness, generation of toxic language and enforcing stereotypes. While we release our
OPT-IML models to proliferate future work on instruction-tuning and to improve the availability
of large instruction-tuned causal LMs, the use of these models should be
accompanied with responsible best practices.

## Training data
OPT-IML models are trained on OPT-IML Bench, a large benchmark for Instruction MetaLearning (IML) of 2000 NLP tasks consolidated into task categories from 8 existing benchmarks include Super-NaturalInstructions, FLAN, PromptSource, etc. 

## Training procedure
The texts are tokenized using the GPT2 byte-level version of Byte Pair Encoding (BPE) (for unicode characters) and a vocabulary size of 50272. The inputs are sequences of 2048 consecutive tokens.

The 30B model was fine-tuned on 64 40GB A100 GPUs. During fine-tuning, models saw approximately 2 billion tokens, which is only 0.6% of the pre-training
budget of OPT.


### BibTeX entry and citation info
```bibtex
@misc{iyer2022opt,
      title={OPT-IML: Scaling Language Model Instruction Meta Learning through the Lens of Generalization}, 
      author={Iyer, Srinivasan and Lin, Xi Victoria and Pasunuru, Ramakanth and Mihaylov, Todor and Simig, D{\'a}niel and Yu, Ping and Shuster, Kurt and Wang, Tianlu and Liu, Qing and Koura, Punit Singh and others},
      year={2022},
      eprint={2212.12017},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```