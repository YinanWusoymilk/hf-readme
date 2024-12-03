---
language:
- multilingual
- ar
- bg
- de
- el
- en
- es
- fr
- hi
- it
- ja
- nl
- pl
- pt
- ru
- sw
- th
- tr
- ur
- vi
- zh
license: mit
inference: false
tags:
- language
- language-detection
metrics:
- accuracy
- f1
base_model: papluca/xlm-roberta-base-language-detection
model-index:
- name: xlm-roberta-base-language-detection
  results: []
pipeline_tag: text-classification

---

# ONNX version of papluca/xlm-roberta-base-language-detection

**This model is a conversion of [papluca/xlm-roberta-base-language-detection](https://huggingface.co/papluca/xlm-roberta-base-language-detection) to ONNX** format using the [🤗 Optimum](https://huggingface.co/docs/optimum/index) library.

## Model description

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the [Language Identification](https://huggingface.co/datasets/papluca/language-identification#additional-information) dataset.

This model is an XLM-RoBERTa transformer model with a classification head on top (i.e. a linear layer on top of the pooled output). 
For additional information please refer to the [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) model card or to the paper [Unsupervised Cross-lingual Representation Learning at Scale](https://arxiv.org/abs/1911.02116) by Conneau et al.

## Intended uses & limitations

You can directly use this model as a language detector, i.e. for sequence classification tasks. Currently, it supports the following 20 languages: 

`arabic (ar), bulgarian (bg), german (de), modern greek (el), english (en), spanish (es), french (fr), hindi (hi), italian (it), japanese (ja), dutch (nl), polish (pl), portuguese (pt), russian (ru), swahili (sw), thai (th), turkish (tr), urdu (ur), vietnamese (vi), and chinese (zh)`

## Usage

### Optimum

Loading the model requires the [🤗 Optimum](https://huggingface.co/docs/optimum/index) library installed.

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline


tokenizer = AutoTokenizer.from_pretrained("laiyer/xlm-roberta-base-language-detection-onnx")
model = ORTModelForSequenceClassification.from_pretrained("laiyer/xlm-roberta-base-language-detection-onnx")
classifier = pipeline(
    task="text-classification",
    model=model,
    tokenizer=tokenizer,
    top_k=None,
)

classifier_output = ner("It's not toxic comment")
print(classifier_output)
```

### LLM Guard

[Language scanner](https://llm-guard.com/input_scanners/language/)

## Community

Join our Slack to give us feedback, connect with the maintainers and fellow users, ask questions, 
or engage in discussions about LLM security!

<a href="https://join.slack.com/t/laiyerai/shared_invite/zt-28jv3ci39-sVxXrLs3rQdaN3mIl9IT~w"><img src="https://github.com/laiyer-ai/llm-guard/blob/main/docs/assets/join-our-slack-community.png?raw=true" width="200"></a>
