---
language: eng
license: mit
dataset: Logical Fallacy Dataset
---

# distilbert-base-fallacy-classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the [Logical Fallacy Dataset](https://github.com/causalNLP/logical-fallacy).

## Model description

The model is fine-tuned for text classification of logical fallacies. There are a total of 14 classes: ad hominem, ad populum, appeal to emotion, circular reasoning, equivocation, fallacy of credibility, fallacy of extension, fallacy of logic, fallacy of relevance, false causality, false dilemma, faulty generalization, intentional, and miscellaneous.

## Example Pipeline

```python
from transformers import pipeline

text = "We know that the earth is flat because it looks and feels flat."
model_path = "q3fer/distilbert-base-fallacy-classification"
pipe = pipeline("text-classification", model=model_path, tokenizer=model_path)
pipe(text)
```

```
[{'label': 'circular reasoning', 'score': 0.951125979423523}]
```

## Full Classification Example

```python
import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("q3fer/distilbert-base-fallacy-classification")
tokenizer = AutoTokenizer.from_pretrained("q3fer/distilbert-base-fallacy-classification")

text = "We know that the earth is flat because it looks and feels flat."
inputs = tokenizer(text, return_tensors='pt')

with torch.no_grad():
  logits = model(**inputs)
  scores = logits[0][0]
  scores = torch.nn.Softmax(dim=0)(scores)

  _, ranking = torch.topk(scores, k=scores.shape[0])
  ranking = ranking.tolist()

results = [f"{i+1}) {model.config.id2label[ranking[i]]} {scores[ranking[i]]:.4f}" for i in range(scores.shape[0])]
print('\n'.join(results))
```

```
1) circular reasoning 0.9511
2) fallacy of logic 0.0154
3) equivocation 0.0080
4) fallacy of credibility 0.0069
5) ad populum 0.0028
6) fallacy of extension 0.0025
7) intentional 0.0024
8) faulty generalization 0.0021
9) appeal to emotion 0.0021
10) fallacy of relevance 0.0019
11) false dilemma 0.0017
12) ad hominem 0.0013
13) false causality 0.0012
14) miscellaneous 0.0004
```

## Training and evaluation data

The [Logical Fallacy Dataset](https://github.com/causalNLP/logical-fallacy) is used for training and evaluation.

Jin, Z., Lalwani, A., Vaidhya, T., Shen, X., Ding, Y., Lyu, Z., ... Schölkopf, B. (2022). Logical Fallacy Detection. arXiv. https://doi.org/10.48550/arxiv.2202.13758

## Training procedure

The following hyperparameters were used during fine-tuning:

- learning_rate : 2e-5
- warmup steps : 0
- batch_size: 16
- num_epochs: 8
- batches_per_epoch: 122
- total_train_steps: 976