---
license: apache-2.0
---
# Cross-Encoder for Quora Duplicate Questions Detection
This model was trained using [SentenceTransformers](https://sbert.net) [Cross-Encoder](https://www.sbert.net/examples/applications/cross-encoder/README.html) class.

## Training Data
Given a question and paragraph, can the question be answered by the paragraph? The models have been trained on the [GLUE QNLI](https://arxiv.org/abs/1804.07461) dataset, which transformed the [SQuAD dataset](https://rajpurkar.github.io/SQuAD-explorer/) into an NLI task.

## Performance
For performance results of this model, see [SBERT.net Pre-trained Cross-Encoder][https://www.sbert.net/docs/pretrained_cross-encoders.html].

## Usage

Pre-trained models can be used like this:
```python
from sentence_transformers import CrossEncoder
model = CrossEncoder('model_name')
scores = model.predict([('Query1', 'Paragraph1'), ('Query2', 'Paragraph2')])

#e.g.
scores = model.predict([('How many people live in Berlin?', 'Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers.'), ('What is the size of New York?', 'New York City is famous for the Metropolitan Museum of Art.')])
```

## Usage with Transformers AutoModel
You can use the model also directly with Transformers library (without SentenceTransformers library):
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained('model_name')
tokenizer = AutoTokenizer.from_pretrained('model_name')

features = tokenizer(['How many people live in Berlin?', 'What is the size of New York?'], ['Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers.', 'New York City is famous for the Metropolitan Museum of Art.'],  padding=True, truncation=True, return_tensors="pt")

model.eval()
with torch.no_grad():
    scores = torch.nn.functional.sigmoid(model(**features).logits)
    print(scores)
```