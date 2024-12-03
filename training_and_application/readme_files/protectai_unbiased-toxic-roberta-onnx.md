---
language:
- en
inference: false
pipeline_tag: token-classification
tags:
- toxicity
- bias
- roberta
license: apache-2.0
base_model: unitary/unbiased-toxic-roberta
---

# ONNX version of unitary/unbiased-toxic-roberta

**This model is a conversion of [unitary/unbiased-toxic-roberta](https://huggingface.co/unitary/unbiased-toxic-roberta) to ONNX** format using the [🤗 Optimum](https://huggingface.co/docs/optimum/index) library.

Trained models & code to predict toxic comments on 3 Jigsaw challenges: Toxic comment classification, Unintended Bias in Toxic comments, Multilingual toxic comment classification.

Built by [Laura Hanu](https://laurahanu.github.io/) at [Unitary](https://www.unitary.ai/). 

**⚠️ Disclaimer:**
The huggingface models currently give different results to the detoxify library (see issue [here](https://github.com/unitaryai/detoxify/issues/15)). 

## Labels
All challenges have a toxicity label. The toxicity labels represent the aggregate ratings of up to 10 annotators according the following schema:
- **Very Toxic** (a very hateful, aggressive, or disrespectful comment that is very likely to make you leave a discussion or give up on sharing your perspective)
- **Toxic** (a rude, disrespectful, or unreasonable comment that is somewhat likely to make you leave a discussion or give up on sharing your perspective)
- **Hard to Say**
- **Not Toxic**

More information about the labelling schema can be found [here](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data).

### Toxic Comment Classification Challenge
This challenge includes the following labels:

- `toxic`
- `severe_toxic`
- `obscene`
- `threat`
- `insult`
- `identity_hate`

### Jigsaw Unintended Bias in Toxicity Classification
This challenge has 2 types of labels: the main toxicity labels and some additional identity labels that represent the identities mentioned in the comments. 

Only identities with more than 500 examples in the test set (combined public and private) are included during training as additional labels and in the evaluation calculation.

- `toxicity`
- `severe_toxicity`
- `obscene`
- `threat`
- `insult`
- `identity_attack`
- `sexual_explicit`

Identity labels used:
- `male`
- `female`
- `homosexual_gay_or_lesbian`
- `christian`
- `jewish`
- `muslim`
- `black`
- `white`
- `psychiatric_or_mental_illness`

A complete list of all the identity labels available can be found [here](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data).

## Usage

### Optimum

Loading the model requires the [🤗 Optimum](https://huggingface.co/docs/optimum/index) library installed.

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline


tokenizer = AutoTokenizer.from_pretrained("laiyer/unbiased-toxic-roberta-onnx")
model = ORTModelForSequenceClassification.from_pretrained("laiyer/unbiased-toxic-roberta-onnx")
classifier = pipeline(
    task="text-classification",
    model=model,
    tokenizer=tokenizer,
)

classifier_output = ner("It's not toxic comment")
print(classifier_output)
```

### LLM Guard

[Toxicity scanner](https://llm-guard.com/input_scanners/toxicity/)

## Community

Join our Slack to give us feedback, connect with the maintainers and fellow users, ask questions, 
or engage in discussions about LLM security!

<a href="https://join.slack.com/t/laiyerai/shared_invite/zt-28jv3ci39-sVxXrLs3rQdaN3mIl9IT~w"><img src="https://github.com/laiyer-ai/llm-guard/blob/main/docs/assets/join-our-slack-community.png?raw=true" width="200"></a>