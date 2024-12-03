---
license: cc-by-nc-4.0
language:
  - multilingual
  - af
  - am
  - ar
  - as
  - az
  - be
  - bg
  - bn
  - br
  - bs
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - fy
  - ga
  - gd
  - gl
  - gu
  - ha
  - he
  - hi
  - hr
  - hu
  - hy
  - id
  - is
  - it
  - ja
  - jv
  - ka
  - kk
  - km
  - kn
  - ko
  - ku
  - ky
  - la
  - lo
  - lt
  - lv
  - mg
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - 'no'
  - om
  - or
  - pa
  - pl
  - ps
  - pt
  - ro
  - ru
  - sa
  - sd
  - si
  - sk
  - sl
  - so
  - sq
  - sr
  - su
  - sv
  - sw
  - ta
  - te
  - th
  - tl
  - tr
  - ug
  - uk
  - ur
  - uz
  - vi
  - xh
  - yi
  - zh
inference: false
tags:
- ColBERT
- passage-retrieval
---

<br><br>

<p align="center">
<img src="https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/603763514de52ff951d89793/AFoybzd5lpBQXEBrQHuTt.png?w=200&h=200&f=face" alt="Finetuner logo: Finetuner helps you to create experiments in order to improve embeddings on search tasks. It accompanies you to deliver the last mile of performance-tuning for neural search applications." width="150px">
</p>


<p align="center">
<b>Trained by <a href="https://jina.ai/"><b>Jina AI</b></a>.</b>
</p>

<p align="center">
<b>JinaColBERT V2: your multilingual late interaction retriever!</b>
</p>

JinaColBERT V2 (`jina-colbert-v2`) is a new model based on the [JinaColBERT V1](https://jina.ai/news/what-is-colbert-and-late-interaction-and-why-they-matter-in-search/) that expands on the capabilities and performance of the [`jina-colbert-v1-en`](https://huggingface.co/jinaai/jina-colbert-v1-en) model. Like the previous release, it has Jina AI’s 8192 token input context and the [improved efficiency, performance](https://jina.ai/news/what-is-colbert-and-late-interaction-and-why-they-matter-in-search/), and [explainability](https://jina.ai/news/ai-explainability-made-easy-how-late-interaction-makes-jina-colbert-transparent/) of token-level embeddings and late interaction. 

This new release adds new functionality and performance improvements:

- Multilingual support for dozens of languages, with strong performance on major global languages.
- [Matryoshka embeddings](https://huggingface.co/blog/matryoshka), which allow users to trade between efficiency and precision flexibly.
- Superior retrieval performance when compared to the English-only [`jina-colbert-v1-en`](https://huggingface.co/jinaai/jina-colbert-v1-en).

JinaColBERT V2 offers three different versions for different embeddings dimensions:
[`jinaai/jina-colbert-v2`](https://huggingface.co/jinaai/jina-colbert-v2): 128 dimension embeddings
[`jinaai/jina-colbert-v2-96`](https://huggingface.co/jinaai/jina-colbert-v2-96): 96 dimension embeddings
[`jinaai/jina-colbert-v2-64`](https://huggingface.co/jinaai/jina-colbert-v2-64): 64 dimension embeddings 


## Usage

### Installation

`jina-colbert-v2` is trained with flash attention and therefore requires `einops` and `flash_attn` to be installed.

To use the model, you could either use the Standford ColBERT library or use the `pylate`/`ragatouille` package that we provide.

```bash
pip install -U einops flash_attn
pip install -U ragatouille # or
pip install -U colbert-ai # or
pip install -U pylate
```

### PyLate

```python
# Please refer to Pylate: https://github.com/lightonai/pylate for detailed usage
from pylate import indexes, models, retrieve

model = models.ColBERT(
    model_name_or_path="jinaai/jina-colbert-v2",
    query_prefix="[QueryMarker]",
    document_prefix="[DocumentMarker]",
    attend_to_expansion_tokens=True,
    trust_remote_code=True,
)
```

### RAGatouille

```python
from ragatouille import RAGPretrainedModel

RAG = RAGPretrainedModel.from_pretrained("jinaai/jina-colbert-v2")
docs = [
    "ColBERT is a novel ranking model that adapts deep LMs for efficient retrieval.",
    "Jina-ColBERT is a ColBERT-style model but based on JinaBERT so it can support both 8k context length, fast and accurate retrieval.",
]
RAG.index(docs, index_name="demo")
query = "What does ColBERT do?"
results = RAG.search(query)
```

### Stanford ColBERT

```python
from colbert.infra import ColBERTConfig
from colbert.modeling.checkpoint import Checkpoint

ckpt = Checkpoint("jinaai/jina-colbert-v2", colbert_config=ColBERTConfig())
docs = [
    "ColBERT is a novel ranking model that adapts deep LMs for efficient retrieval.",
    "Jina-ColBERT is a ColBERT-style model but based on JinaBERT so it can support both 8k context length, fast and accurate retrieval.",
]
query_vectors = ckpt.queryFromText(docs, bsize=2)
```

## Evaluation Results

### Retrieval Benchmarks

#### BEIR

| **NDCG@10**        | **jina-colbert-v2** | **jina-colbert-v1** | **ColBERTv2.0** | **BM25** |
|--------------------|---------------------|---------------------|-----------------|----------|
| **avg**            | 0.531               | 0.502               | 0.496           | 0.440    |
| **nfcorpus**       | 0.346               | 0.338               | 0.337           | 0.325    |
| **fiqa**           | 0.408               | 0.368               | 0.354           | 0.236    |
| **trec-covid**     | 0.834               | 0.750               | 0.726           | 0.656    |
| **arguana**        | 0.366               | 0.494               | 0.465           | 0.315    |
| **quora**          | 0.887               | 0.823               | 0.855           | 0.789    |
| **scidocs**        | 0.186               | 0.169               | 0.154           | 0.158    |
| **scifact**        | 0.678               | 0.701               | 0.689           | 0.665    |
| **webis-touche**   | 0.274               | 0.270               | 0.260           | 0.367    |
| **dbpedia-entity** | 0.471               | 0.413               | 0.452           | 0.313    |
| **fever**          | 0.805               | 0.795               | 0.785           | 0.753    |
| **climate-fever**  | 0.239               | 0.196               | 0.176           | 0.213    |
| **hotpotqa**       | 0.766               | 0.656               | 0.675           | 0.603    |
| **nq**             | 0.640               | 0.549               | 0.524           | 0.329    |



#### MS MARCO Passage Retrieval

| **MRR@10**  | **jina-colbert-v2** | **jina-colbert-v1** | **ColBERTv2.0** | **BM25** |
|-------------|---------------------|---------------------|-----------------|----------|
| **MSMARCO** | 0.396               | 0.390               | 0.397           | 0.187    |


### Multilingual Benchmarks

#### MIRACLE

| **NDCG@10**    | **jina-colbert-v2** | **mDPR (zero shot)** |
|---------|---------------------|----------------------|
| **avg** | 0.627               | 0.427                |
| **ar**  | 0.753               | 0.499                |
| **bn**  | 0.750               | 0.443                |
| **de**  | 0.504               | 0.490                |
| **es**  | 0.538               | 0.478                |
| **en**  | 0.570               | 0.394                |
| **fa**  | 0.563               | 0.480                |
| **fi**  | 0.740               | 0.472                |
| **fr**  | 0.541               | 0.435                |
| **hi**  | 0.600               | 0.383                |
| **id**  | 0.547               | 0.272                |
| **ja**  | 0.632               | 0.439                |
| **ko**  | 0.671               | 0.419                |
| **ru**  | 0.643               | 0.407                |
| **sw**  | 0.499               | 0.299                |
| **te**  | 0.742               | 0.356                |
| **th**  | 0.772               | 0.358                |
| **yo**  | 0.623               | 0.396                |
| **zh**  | 0.523               | 0.512                |

#### mMARCO

| **MRR@10** | **jina-colbert-v2** | **BM-25** | **ColBERT-XM** |
|------------|---------------------|-----------|----------------|
| **avg**    | 0.313               | 0.141     | 0.254          |
| **ar**     | 0.272               | 0.111     | 0.195          |
| **de**     | 0.331               | 0.136     | 0.270          |
| **nl**     | 0.330               | 0.140     | 0.275          |
| **es**     | 0.341               | 0.158     | 0.285          |
| **fr**     | 0.335               | 0.155     | 0.269          |
| **hi**     | 0.309               | 0.134     | 0.238          |
| **id**     | 0.319               | 0.149     | 0.263          |
| **it**     | 0.337               | 0.153     | 0.265          |
| **ja**     | 0.276               | 0.141     | 0.241          |
| **pt**     | 0.337               | 0.152     | 0.276          |
| **ru**     | 0.298               | 0.124     | 0.251          |
| **vi**     | 0.287               | 0.136     | 0.226          |
| **zh**     | 0.302               | 0.116     | 0.246          |



### Matryoshka Representation Benchmarks

#### BEIR

| **NDCG@10**    | **dim=128** | **dim=96** | **dim=64** |
|----------------|-------------|------------|------------|
| **avg**    | 0.599       | 0.591      | 0.589      |
| **nfcorpus**   | 0.346       | 0.340      | 0.347      |
| **fiqa**       | 0.408       | 0.404      | 0.404      |
| **trec-covid** | 0.834       | 0.808      | 0.805      |
| **hotpotqa**   | 0.766       | 0.764      | 0.756      |
| **nq**         | 0.640       | 0.640      | 0.635      |


#### MSMARCO

| **MRR@10**     | **dim=128** | **dim=96** | **dim=64** |
|----------------|-------------|------------|------------|
| **msmarco**    | 0.396       | 0.391      | 0.388      |

## Other Models

Additionally, we provide the following embedding models, you can also use them for retrieval.

- [`jina-embeddings-v2-base-en`](https://huggingface.co/jinaai/jina-embeddings-v2-base-en): 137 million parameters.
- [`jina-embeddings-v2-base-zh`](https://huggingface.co/jinaai/jina-embeddings-v2-base-zh): 161 million parameters Chinese-English bilingual model.
- [`jina-embeddings-v2-base-de`](https://huggingface.co/jinaai/jina-embeddings-v2-base-de): 161 million parameters German-English bilingual model.
- [`jina-embeddings-v2-base-es`](https://huggingface.co/jinaai/jina-embeddings-v2-base-es): 161 million parameters Spanish-English bilingual model.
- [`jina-reranker-v2`](https://huggingface.co/jinaai/jina-reranker-v2-base-multilingual): multilingual reranker model.
- [`jina-clip-v1`](https://huggingface.co/jinaai/jina-clip-v1): English multimodal (text-image) embedding model.

## Contact

Join our [Discord community](https://discord.jina.ai) and chat with other community members about ideas.

```
@misc{jha2024jinacolbertv2generalpurposemultilinguallate,
      title={Jina-ColBERT-v2: A General-Purpose Multilingual Late Interaction Retriever}, 
      author={Rohan Jha and Bo Wang and Michael Günther and Saba Sturua and Mohammad Kalim Akram and Han Xiao},
      year={2024},
      eprint={2408.16672},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2408.16672}, 
}
```
      