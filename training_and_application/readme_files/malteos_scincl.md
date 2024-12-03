---
tags:
- feature-extraction
- sentence-transformers
- transformers
library_name: sentence-transformers
language: en
datasets:
- SciDocs
- s2orc
metrics:
- F1
- accuracy
- map
- ndcg
license: mit
---

## SciNCL

SciNCL is a pre-trained BERT language model to generate document-level embeddings of research papers.
It uses the citation graph neighborhood to generate samples for contrastive learning.
Prior to the contrastive training, the model is initialized with weights from [scibert-scivocab-uncased](https://huggingface.co/allenai/scibert_scivocab_uncased).
The underlying citation embeddings are trained on the [S2ORC citation graph](https://github.com/allenai/s2orc).

Paper: [Neighborhood Contrastive Learning for Scientific Document Representations with Citation Embeddings (EMNLP 2022 paper)](https://arxiv.org/abs/2202.06671).

Code: https://github.com/malteos/scincl

PubMedNCL: Working with biomedical papers? Try [PubMedNCL](https://huggingface.co/malteos/PubMedNCL).

## How to use the pretrained model

### Sentence Transformers

```python
from sentence_transformers import SentenceTransformer

# Load the model
model = SentenceTransformer("malteos/scincl")

# Concatenate the title and abstract with the [SEP] token
papers = [
    "BERT [SEP] We introduce a new language representation model called BERT",
    "Attention is all you need [SEP] The dominant sequence transduction models are based on complex recurrent or convolutional neural networks",
]
# Inference
embeddings = model.encode(papers)

# Compute the (cosine) similarity between embeddings
similarity = model.similarity(embeddings[0], embeddings[1])
print(similarity.item())
# => 0.8440517783164978
```

### Transformers

```python
from transformers import AutoTokenizer, AutoModel

# load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('malteos/scincl')
model = AutoModel.from_pretrained('malteos/scincl')

papers = [{'title': 'BERT', 'abstract': 'We introduce a new language representation model called BERT'},
          {'title': 'Attention is all you need', 'abstract': ' The dominant sequence transduction models are based on complex recurrent or convolutional neural networks'}]

# concatenate title and abstract with [SEP] token
title_abs = [d['title'] + tokenizer.sep_token + (d.get('abstract') or '') for d in papers]

# preprocess the input
inputs = tokenizer(title_abs, padding=True, truncation=True, return_tensors="pt", max_length=512)

# inference
result = model(**inputs)

# take the first token ([CLS] token) in the batch as the embedding
embeddings = result.last_hidden_state[:, 0, :]

# calculate the similarity
embeddings = torch.nn.functional.normalize(embeddings, p=2, dim=1)
similarity = (embeddings[0] @ embeddings[1].T)
print(similarity.item())
# => 0.8440518379211426
```

## Triplet Mining Parameters

| **Setting**             | **Value**          |
|-------------------------|--------------------|
| seed                    | 4                  |
| triples_per_query       | 5                  |
| easy_positives_count    | 5                  |
| easy_positives_strategy | 5                  |
| easy_positives_k        | 20-25              |
| easy_negatives_count    | 3                  |
| easy_negatives_strategy | random_without_knn |
| hard_negatives_count    | 2                  |
| hard_negatives_strategy | knn                |
| hard_negatives_k        | 3998-4000          |

## SciDocs Results

These model weights are the ones that yielded the best results on SciDocs (`seed=4`).
In the paper we report the SciDocs results as mean over ten seeds.

| **model**         | **mag-f1** | **mesh-f1** | **co-view-map** | **co-view-ndcg** | **co-read-map** | **co-read-ndcg** | **cite-map** | **cite-ndcg** | **cocite-map** | **cocite-ndcg** | **recomm-ndcg** | **recomm-P@1** | **Avg** |
|-------------------|-----------:|------------:|----------------:|-----------------:|----------------:|-----------------:|-------------:|--------------:|---------------:|----------------:|----------------:|---------------:|--------:|
| Doc2Vec           |       66.2 |        69.2 |            67.8 |             82.9 |            64.9 |             81.6 |         65.3 |          82.2 |           67.1 |            83.4 |            51.7 |           16.9 |    66.6 |
| fasttext-sum      |       78.1 |        84.1 |            76.5 |             87.9 |            75.3 |             87.4 |         74.6 |          88.1 |           77.8 |            89.6 |            52.5 |             18 |    74.1 |
| SGC               |       76.8 |        82.7 |            77.2 |               88 |            75.7 |             87.5 |         91.6 |          96.2 |           84.1 |            92.5 |            52.7 |           18.2 |    76.9 |
| SciBERT           |       79.7 |        80.7 |            50.7 |             73.1 |            47.7 |             71.1 |         48.3 |          71.7 |           49.7 |            72.6 |            52.1 |           17.9 |    59.6 |
| SPECTER           |         82 |        86.4 |            83.6 |             91.5 |            84.5 |             92.4 |         88.3 |          94.9 |           88.1 |            94.8 |            53.9 |             20 |      80 |
| SciNCL (10 seeds) |       81.4 |        88.7 |            85.3 |             92.3 |            87.5 |             93.9 |         93.6 |          97.3 |           91.6 |            96.4 |            53.9 |           19.3 |    81.8 |
| **SciNCL (seed=4)**   |       81.2 |        89.0 |            85.3 |             92.2 |            87.7 |             94.0 |         93.6 |          97.4 |           91.7 |            96.5 |            54.3 |           19.6 |    81.9 |

Additional evaluations are available in the paper.

## License

MIT
