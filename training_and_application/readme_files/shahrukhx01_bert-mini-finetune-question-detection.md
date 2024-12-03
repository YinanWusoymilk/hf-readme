
---
language: "en"
tags:
- neural-search-query-classification
- neural-search
widget:
- text: "keyword query."
---
# KEYWORD QUERY VS STATEMENT/QUESTION CLASSIFIER FOR NEURAL SEARCH
| Train Loss    | Validation Acc.| Test Acc.|
| ------------- |:-------------: | -----:   |
| 0.000806      | 0.99  | 0.997    |

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
  
tokenizer = AutoTokenizer.from_pretrained("shahrukhx01/bert-mini-finetune-question-detection")

model = AutoModelForSequenceClassification.from_pretrained("shahrukhx01/bert-mini-finetune-question-detection")
```
Trained to add feature for classifying queries between Keyword Query or Question + Statement Query using classification in [Haystack](https://github.com/deepset-ai/haystack/issues/611)

Problem Statement:
One common challenge that we saw in deployments: We need to distinguish between real questions and keyword queries that come in. We only want to route questions to the Reader branch in order to maximize the accuracy of results and minimize computation efforts/costs.



Baseline:
https://www.kaggle.com/shahrukhkhan/question-v-statement-detection

Dataset:
https://www.kaggle.com/stefanondisponibile/quora-question-keyword-pairs

Kaggle Notebook:
https://www.kaggle.com/shahrukhkhan/question-vs-statement-classification-mini-bert/
