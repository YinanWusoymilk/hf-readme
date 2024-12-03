---
license: apache-2.0
language:
- en
pipeline_tag: sentence-similarity
---
ONNX port of [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) adjusted to return attention weights.

This model is intended to be used for [BM42 searches](https://qdrant.tech/articles/bm42/).

### Usage

Here's an example of performing inference using the model with [FastEmbed](https://github.com/qdrant/fastembed).

```py
from fastembed import SparseTextEmbedding

documents = [
    "You should stay, study and sprint.",
    "History can only prepare us to be surprised yet again.",
]

model = SparseTextEmbedding(model_name="Qdrant/bm42-all-minilm-l6-v2-attentions")
embeddings = list(model.embed(documents))

# [
#     SparseEmbedding(values=array([0.26399775, 0.24662513, 0.47077307]),
#                     indices=array([1881538586, 150760872, 1932363795])),
#     SparseEmbedding(values=array(
#         [0.38320042, 0.25453135, 0.18017513, 0.30432631, 0.1373556]),
#                     indices=array([
#                         733618285, 1849833631, 1008800696, 2090661150,
#                         1117393019
#                     ]))
# ]

```