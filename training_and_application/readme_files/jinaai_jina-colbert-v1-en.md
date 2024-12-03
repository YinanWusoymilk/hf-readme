---
license: apache-2.0
language:
- en
tags:
- ColBERT
- passage-retrieval
datasets:
- ms_marco
---

<br><br>

<p align="center">
<img src="https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/603763514de52ff951d89793/AFoybzd5lpBQXEBrQHuTt.png?w=200&h=200&f=face" alt="Finetuner logo: Finetuner helps you to create experiments in order to improve embeddings on search tasks. It accompanies you to deliver the last mile of performance-tuning for neural search applications." width="150px">
</p>


<p align="center">
<b>Trained by <a href="https://jina.ai/"><b>Jina AI</b></a>.</b>
</p>

# Jina-ColBERT

**Jina-ColBERT is a ColBERT-style model but based on JinaBERT so it can support both _8k context length_, _fast and accurate retrieval_.**

[JinaBERT](https://arxiv.org/abs/2310.19923) is a BERT architecture that supports the symmetric bidirectional variant of [ALiBi](https://arxiv.org/abs/2108.12409) to allow longer sequence length. The Jina-ColBERT model is trained on MSMARCO passage ranking dataset, following a very similar training procedure with ColBERTv2. The only difference is that we use `jina-bert-v2-base-en` as the backbone instead of `bert-base-uncased`.

For more information about ColBERT, please refer to the [ColBERTv1](https://arxiv.org/abs/2004.12832) and [ColBERTv2](https://arxiv.org/abs/2112.01488v3) paper, and [the original code](https://github.com/stanford-futuredata/ColBERT).

## Usage

### Installation

To use this model, you will need to install the **latest version** of the ColBERT repository:

```bash
pip install git+https://github.com/stanford-futuredata/ColBERT.git torch
conda install -c conda-forge faiss-gpu  # use conda to install the latest version faiss
```

### Indexing

```python
from colbert import Indexer
from colbert.infra import Run, RunConfig, ColBERTConfig

n_gpu: int = 1  # Set your number of available GPUs
experiment: str = ""  # Name of the folder where the logs and created indices will be stored
index_name: str = ""  # The name of your index, i.e. the name of your vector database

if __name__ == "__main__":
    with Run().context(RunConfig(nranks=n_gpu, experiment=experiment)):
        config = ColBERTConfig(
          doc_maxlen=8192  # Our model supports 8k context length for indexing long documents
        )
        indexer = Indexer(
          checkpoint="jinaai/jina-colbert-v1-en",
          config=config,
        )
        documents = [
          "ColBERT is an efficient and effective passage retrieval model.",
          "Jina-ColBERT is a ColBERT-style model but based on JinaBERT so it can support both 8k context length.",
          "JinaBERT is a BERT architecture that supports the symmetric bidirectional variant of ALiBi to allow longer sequence length.",
          "Jina-ColBERT model is trained on MSMARCO passage ranking dataset, following a very similar training procedure with ColBERTv2.",
          "Jina-ColBERT achieves the competitive retrieval performance with ColBERTv2.",
          "Jina is an easier way to build neural search systems.",
          "You can use Jina-ColBERT to build neural search systems with ease.",
          # Add more documents here to ensure the clustering work correctly
        ]
        indexer.index(name=index_name, collection=documents)
```

### Searching

```python
from colbert import Searcher
from colbert.infra import Run, RunConfig, ColBERTConfig

n_gpu: int = 0
experiment: str = ""  # Name of the folder where the logs and created indices will be stored
index_name: str = ""  # Name of your previously created index where the documents you want to search are stored.
k: int = 10  # how many results you want to retrieve

if __name__ == "__main__":
    with Run().context(RunConfig(nranks=n_gpu, experiment=experiment)):
        config = ColBERTConfig(
          query_maxlen=128  # Although the model supports 8k context length, we suggest not to use a very long query, as it may cause significant computational complexity and CUDA memory usage.
        )
        searcher = Searcher(
          index=index_name, 
          config=config
        )  # You don't need to specify the checkpoint again, the model name is stored in the index.
        query = "How to use ColBERT for indexing long documents?"
        results = searcher.search(query, k=k)
        # results: tuple of tuples of length k containing ((passage_id, passage_rank, passage_score), ...)
```


### Creating Vectors


```python
from colbert.modeling.checkpoint import Checkpoint

ckpt = Checkpoint("jinaai/jina-colbert-v1-en", colbert_config=ColBERTConfig(root="experiments"))
query_vectors = ckpt.queryFromText(["What does ColBERT do?", "This is a search query?"], bsize=16)
print(query_vectors)
```

Complete working Colab Notebook is [here](https://colab.research.google.com/drive/1-5WGEYPSBNBg-Z0bGFysyvckFuM8imrg)

### Reranking Using ColBERT

```python
from colbert.modeling.checkpoint import Checkpoint
from colbert.infra import ColBERTConfig

query = ["How to use ColBERT for indexing long documents?"]
documents = [
    "ColBERT is an efficient and effective passage retrieval model.",
    "Jina-ColBERT is a ColBERT-style model but based on JinaBERT so it can support both 8k context length.",
    "JinaBERT is a BERT architecture that supports the symmetric bidirectional variant of ALiBi to allow longer sequence length.",
    "Jina-ColBERT model is trained on MSMARCO passage ranking dataset, following a very similar training procedure with ColBERTv2.",
]

config = ColBERTConfig(query_maxlen=32, doc_maxlen=512)
ckpt = Checkpoint(args.reranker, colbert_config=colbert_config)
Q = ckpt.queryFromText([all_queries[i]])
D = ckpt.docFromText(all_passages, bsize=32)[0]
D_mask = torch.ones(D.shape[:2], dtype=torch.long)
scores = colbert_score(Q, D, D_mask).flatten().cpu().numpy().tolist()
ranking = numpy.argsort(scores)[::-1]
print(ranking)
```

## Evaluation Results

**TL;DR:** Our Jina-ColBERT achieves the competitive retrieval performance with [ColBERTv2](https://huggingface.co/colbert-ir/colbertv2.0) on all benchmarks, and outperforms ColBERTv2 on datasets in where documents have longer context length.

### In-domain benchmarks

We evaluate the in-domain performance on the dev subset of MSMARCO passage ranking dataset. We follow the same evaluation settings in the ColBERTv2 paper and rerun the results of ColBERTv2 using the released checkpoint.

| Model | MRR@10 |  Recall@50 | Recall@1k |
| --- | :---: | :---: | :---: |
| ColBERTv2       | 39.7 | 86.8 | 97.6 |
| Jina-ColBERT-v1 | 39.0 | 85.6 | 96.2 |

### Out-of-domain benchmarks

Following ColBERTv2, we evaluate the out-of-domain performance on 13 public BEIR datasets and use NDCG@10 as the main metric. We follow the same evaluation settings in the ColBERTv2 paper and rerun the results of ColBERTv2 using the released checkpoint.

Note that both ColBERTv2 and Jina-ColBERT-v1 only employ MSMARCO passage ranking dataset for training, so below results are the fully zero-shot performance.

| dataset | ColBERTv2 | Jina-ColBERT-v1 |
| --- | :---: | :---: |
| ArguAna          | 46.5 | 49.4 |
| ClimateFEVER     | 18.1 | 19.6 |
| DBPedia          | 45.2 | 41.3 |
| FEVER            | 78.8 | 79.5 |
| FiQA             | 35.4 | 36.8 |
| HotPotQA         | 67.5 | 65.6 |
| NFCorpus         | 33.7 | 33.8 |
| NQ               | 56.1 | 54.9 |
| Quora            | 85.5 | 82.3 |
| SCIDOCS          | 15.4 | 16.9 |
| SciFact          | 68.9 | 70.1 |
| TREC-COVID       | 72.6 | 75.0 |
| Webis-touché2020 | 26.0 | 27.0 |
| Average          | 50.0 | 50.2 |

### Long context datasets

We also evaluate the zero-shot performance on datasets where documents have longer context length and compare with some long-context embedding models. Here we use the [LoCo benchmark](https://www.together.ai/blog/long-context-retrieval-models-with-monarch-mixer), which contains 5 datasets with long context length.

| Model | Used context length | Model max context length | Avg. NDCG@10 |
| --- | :---: | :---: | :---: |
| ColBERTv2       | 512 | 512 | 74.3 |
| Jina-ColBERT-v1 (truncated) | 512* | 8192 | 75.5 |
| Jina-ColBERT-v1 | 8192 | 8192 | 83.7 |
| Jina-embeddings-v2-base-en | 8192 | 8192 | **85.4** |

\* denotes that we truncate the context length to 512 for documents. The context length of queries is all 512.

**To summarize, Jina-ColBERT achieves the comparable retrieval performance with ColBERTv2 on all benchmarks, and outperforms ColBERTv2 on datasets in where documents have longer context length.**

### Reranking Performance

We evaluate the reranking performance of ColBERTv2 and Jina-ColBERT on BEIR. We use BM25 as the first-stage retrieval model. The full evaluation code can be found in [this repo](https://github.com/liuqi6777/eval_reranker). 

In summary, Jina-ColBERT outperforms ColBERTv2, even achieving comparable performance with some cross-encoder.

The best model, jina-reranker, will be open-sourced soon!

|BM25|ColBERTv2|Jina-ColBERT|MiniLM-L-6-v2|BGE-reranker-base-v1|BGE-reranker-large-v1|Jina-reranker-base-v1|
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
Arguana         |29.99|33.42|33.95|30.67|23.26|25.42|42.59|
Climate-Fever   |16.51|20.66|21.87|24.70|31.60|31.98|25.49|
DBPedia         |31.80|42.16|41.43|43.90|41.56|43.79|43.68|
FEVER           |65.13|81.07|83.49|80.77|87.07|89.11|86.10|
FiQA            |23.61|35.60|36.68|34.87|33.17|37.70|41.38|
HotpotQA        |63.30|68.84|68.62|72.65|79.04|79.98|75.61|
NFCorpus        |33.75|36.69|36.38|36.48|32.71|36.57|37.73|
NQ              |30.55|51.27|51.01|52.01|53.55|56.81|56.82|
Quora           |78.86|85.18|82.75|82.45|78.44|81.06|87.31|
SCIDOCS         |14.90|15.39|16.67|16.28|15.06|16.84|19.56|
SciFact         |67.89|70.23|70.95|69.53|70.62|74.14|75.01|
TREC-COVID      |59.47|75.00|76.89|74.45|67.46|74.32|82.09|
Webis-touche2020|44.22|32.12|32.56|28.40|34.37|35.66|31.62|
Average         |43.08|49.82|50.25|49.78|49.84|52.57|**54.23**|

ColBERT


## Plans

We are planning to improve the performance of Jina-ColBERT by fine-tuning on more datasets in the future.

## Other Models

Additionally, we provide the following embedding models, you can also use them for retrieval.

- [`jina-embeddings-v2-base-en`](https://huggingface.co/jinaai/jina-embeddings-v2-base-en): 137 million parameters.
- [`jina-embeddings-v2-base-zh`](https://huggingface.co/jinaai/jina-embeddings-v2-base-zh): 161 million parameters Chinese-English bilingual model.
- [`jina-embeddings-v2-base-de`](https://huggingface.co/jinaai/jina-embeddings-v2-base-de): 161 million parameters German-English bilingual model.
- [`jina-embeddings-v2-base-es`](https://huggingface.co/jinaai/jina-embeddings-v2-base-es): 161 million parameters Spanish-English bilingual model.

## Contact

Join our [Discord community](https://discord.jina.ai) and chat with other community members about ideas.