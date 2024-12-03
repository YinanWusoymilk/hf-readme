---
pipeline_type: "text-classification"

widget:
- text: "this is a lovely message"
  example_title: "Example 1"
  multi_class: false
- text: "you are an idiot and you and your family should go back to your country"
  example_title: "Example 2"
  multi_class: false


language: 
  - en
  - nl
  - fr
  - pt
  - it
  - es
  - de
  - da
  - pl
  - af
  
datasets:
- jigsaw_toxicity_pred
metrics:
- F1 Accuracy
---

# citizenlab/twitter-xlm-roberta-base-sentiment-finetunned

This is multilingual XLM-Roberta model sequence classifier fine tunned and based on [Cardiff NLP Group](cardiffnlp/twitter-roberta-base-sentiment) sentiment classification model.

## How to use it

```python
from transformers import pipeline

model_path = "citizenlab/twitter-xlm-roberta-base-sentiment-finetunned"

sentiment_classifier = pipeline("text-classification", model=model_path, tokenizer=model_path)
sentiment_classifier("this is a lovely message")
> [{'label': 'Positive', 'score': 0.9918450713157654}]

sentiment_classifier("you are an idiot and you and your family should go back to your country")
> [{'label': 'Negative', 'score': 0.9849833846092224}]

```

## Evaluation

```
              precision    recall  f1-score   support

    Negative       0.57      0.14      0.23        28
     Neutral       0.78      0.94      0.86       132
    Positive       0.89      0.80      0.85        51

    accuracy                           0.80       211
   macro avg       0.75      0.63      0.64       211
weighted avg       0.78      0.80      0.77       211
```

