---
license: apache-2.0
base_model: distilroberta-base
tags:
- generated_from_trainer
- rejection
- no_answer
- chatgpt
metrics:
- accuracy
- recall
- precision
- f1
model-index:
- name: distilroberta-base-rejection-v1
  results: []
language:
- en
pipeline_tag: text-classification
co2_eq_emissions:
  emissions: 0.07987621556153969
  source: code carbon
  training_type: fine-tuning
datasets:
- argilla/notus-uf-dpo-closest-rejected
---

# Model Card for distilroberta-base-rejection-v1

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on multiple combined datasets of rejections from different LLMs and normal responses from RLHF datasets.

It aims to identify rejections in LLMs when the prompt doesn't pass content moderation, classifying inputs into two categories: `0` for normal outputs and `1` for rejection detected.

It achieves the following results on the evaluation set:
- Loss: 0.0544
- Accuracy: 0.9887
- Recall: 0.9810
- Precision: 0.9279
- F1: 0.9537

## Model details

- **Fine-tuned by:** ProtectAI.com
- **Model type:** distilroberta-base
- **Language(s) (NLP):** English
- **License:** Apache license 2.0
- **Finetuned from model:** [distilroberta-base](https://huggingface.co/distilroberta-base)

## Intended Uses & Limitations

It aims to identify rejection, classifying inputs into two categories: `0` for normal output and `1` for rejection detected.

The model's performance is dependent on the nature and quality of the training data. It might not perform well on text styles or topics not represented in the training set.

Additionally, `distilroberta-base` is case-sensitive model.

## How to Get Started with the Model

### Transformers

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

tokenizer = AutoTokenizer.from_pretrained("ProtectAI/distilroberta-base-rejection-v1")
model = AutoModelForSequenceClassification.from_pretrained("ProtectAI/distilroberta-base-rejection-v1")

classifier = pipeline(
  "text-classification",
  model=model,
  tokenizer=tokenizer,
  truncation=True,
  max_length=512,
  device=torch.device("cuda" if torch.cuda.is_available() else "cpu"),
)

print(classifier("Sorry, but I can't assist with that."))
```

### Optimum with ONNX

Loading the model requires the [🤗 Optimum](https://huggingface.co/docs/optimum/index) library installed.

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline

tokenizer = AutoTokenizer.from_pretrained("ProtectAI/distilroberta-base-rejection-v1", subfolder="onnx")
model = ORTModelForSequenceClassification.from_pretrained("ProtectAI/distilroberta-base-rejection-v1", export=False, subfolder="onnx")

classifier = pipeline(
  task="text-classification",
  model=model,
  tokenizer=tokenizer,
  truncation=True,
  max_length=512,
)

print(classifier("Sorry, but I can't assist with that."))
```

### Use in LLM Guard

[NoRefusal Scanner](https://llm-guard.com/output_scanners/no_refusal/) to detect if output was rejected, which can signal that something is going wrong with the prompt.

## Training and evaluation data

The model was trained on a custom dataset from multiple open-source ones. We used ~10% rejections and ~90% of normal outputs.

We used the following papers when preparing the datasets:

- [Do-Not-Answer: A Dataset for Evaluating Safeguards in LLMs](https://arxiv.org/abs/2308.13387)
- [I'm Afraid I Can't Do That: Predicting Prompt Refusal in Black-Box Generative Language Models](https://arxiv.org/abs/2306.03423)

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Recall | Precision | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.0525        | 1.0   | 3536  | 0.0355          | 0.9912   | 0.9583 | 0.9675    | 0.9629 |
| 0.0219        | 2.0   | 7072  | 0.0312          | 0.9919   | 0.9917 | 0.9434    | 0.9669 |
| 0.0121        | 3.0   | 10608 | 0.0350          | 0.9939   | 0.9905 | 0.9596    | 0.9748 |

### Framework versions

- Transformers 4.36.2
- Pytorch 2.1.2+cu121
- Datasets 2.16.1
- Tokenizers 0.15.0

## Community

Join our Slack to give us feedback, connect with the maintainers and fellow users, ask questions,
get help for package usage or contributions, or engage in discussions about LLM security!

<a href="https://join.slack.com/t/laiyerai/shared_invite/zt-28jv3ci39-sVxXrLs3rQdaN3mIl9IT~w"><img src="https://github.com/laiyer-ai/llm-guard/blob/main/docs/assets/join-our-slack-community.png?raw=true" width="200"></a>

## Citation

```
@misc{distilroberta-base-rejection-v1,
  author = {ProtectAI.com},
  title = {Fine-Tuned DistilRoberta-Base for Rejection in the output Detection},
  year = {2024},
  publisher = {HuggingFace},
  url = {https://huggingface.co/ProtectAI/distilroberta-base-rejection-v1},
}
```