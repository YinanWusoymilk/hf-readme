---
license: apache-2.0
pipeline_tag: sentence-similarity
---

ONNX port of [prithivida/Splade_PP_en_v1](https://huggingface.co/prithivida/Splade_PP_en_v1) for text classification and similarity searches.

### Usage

Here's an example of performing inference using the model with [FastEmbed](https://github.com/qdrant/fastembed).

```py
from fastembed import SparseTextEmbedding

documents = [
    "You should stay, study and sprint.",
    "History can only prepare us to be surprised yet again.",
]

model = SparseTextEmbedding(model_name="prithivida/Splade_PP_en_v1")
embeddings = list(model.embed(documents))

# [
#     SparseEmbedding(values=array(
#         [0.45940185, 0.64054322, 0.2425732, 0.1623179, 1.20566428,
#          0.62039357...]),
#                     indices=array([1012, 1998, 2000, 2005, 2017, 2022...])),
#     SparseEmbedding(values=array([
#         0.09767706, 0.4374367, 0.00468039, 1.01167965, 1.02318227, 1.30155718
#     ...]),
#                     indices=array([2017, 2022, 2025, 2057, 2064, 2069...]))
# ]

```