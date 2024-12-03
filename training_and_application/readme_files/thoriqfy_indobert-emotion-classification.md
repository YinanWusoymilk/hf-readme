---
language:
- id
tags:
- indobert
- indobenchmark
- indonlu
---
How to import:
```python
from transformers import BertForSequenceClassification, BertTokenizer, BertConfig

tokenizer = BertTokenizer.from_pretrained("thoriqfy/indobert-emotion-classification")
config = BertConfig.from_pretrained("thoriqfy/indobert-emotion-classification")
model = BertForSequenceClassification.from_pretrained("thoriqfy/indobert-emotion-classification", config=config)
```

How to use:
```python
from transformers import pipeline

nlp = pipeline("text-classification", model="thoriqfy/indobert-emotion-classification")

results = nlp("Your input text here")
```