---
license: afl-3.0
language:
- en
metrics:
- accuracy
library_name: transformers
pipeline_tag: text-classification
---

## Model description
This model is a fine-tuned version of the [bert-base-uncased](https://huggingface.co/transformers/model_doc/bert.html) model to classify toxic comments.

## How to use

You can use the model with the following code.

```python
from transformers import BertForSequenceClassification, BertTokenizer, TextClassificationPipeline

model_path = "JungleLee/bert-toxic-comment-classification"
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path, num_labels=2)

pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer)
print(pipeline("You're a fucking nerd."))
```

## Training data
The training data comes from this [Kaggle competition](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data). We use 90% of the `train.csv` data to train the model.

## Evaluation results

The model achieves 0.95 AUC in a 1500 rows held-out test set.