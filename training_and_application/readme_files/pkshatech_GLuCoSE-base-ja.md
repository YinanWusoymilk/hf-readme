---
pipeline_tag: sentence-similarity
language: ja
license: apache-2.0
tags:
- transformers
- sentence-similarity
- feature-extraction
- sentence-transformers
inference: false
datasets:
- mc4
- clips/mqa
- shunk031/JGLUE
- paws-x
- MoritzLaurer/multilingual-NLI-26lang-2mil7
- castorini/mr-tydi
- hpprc/jsick
base_model: studio-ousia/luke-base
---


# GLuCoSE (General Luke-based Contrastive Sentence Embedding)-base-Japanese

[日本語のREADME/Japanese README](https://huggingface.co/pkshatech/GLuCoSE-base-ja/blob/main/README_JA.md)

GLuCoSE (General LUke-based COntrastive Sentence Embedding, "glucose") is a Japanese text embedding model based on [LUKE](https://github.com/studio-ousia/luke). In order to create a general-purpose, user-friendly Japanese text embedding model, GLuCoSE has been trained on a mix of web data and various datasets associated with natural language inference and search. This model is not only suitable for sentence vector similarity tasks but also for semantic search tasks.
- Maximum token count: 512
- Output dimension: 768
- Pooling: mean pooling
- Supported language: Japanese

## Usage
You can use this model easily with [sentence-transformers](https://www.SBERT.net).  

First, install sentence-transformers with pip as follows:  

```
pip install -U sentence-transformers
```

You can load the model and convert sentences into dense vectors as shown below:  

```python
from sentence_transformers import SentenceTransformer
sentences = [
    "PKSHA Technologyは機械学習/深層学習技術に関わるアルゴリズムソリューションを展開している。",
    "この深層学習モデルはPKSHA Technologyによって学習され、公開された。",
    "広目天は、仏教における四天王の一尊であり、サンスクリット語の「種々の眼をした者」を名前の由来とする。",
]

model = SentenceTransformer('pkshatech/GLuCoSE-base-ja')
embeddings = model.encode(sentences)
print(embeddings)
```

Since the loss function used during training is cosine similarity, we recommend using cosine similarity for downstream tasks.

This text embedding model can also be used in LangChain. Please refer to [this page](https://python.langchain.com/docs/modules/data_connection/text_embedding/integrations/sentence_transformers) for more information.

## Resources Used
The following resources were used to train this model.
### Pre-trained model
- [studio-ousia/luke-japanese-base-lite](https://huggingface.co/studio-ousia/luke-japanese-base-lite)

### Datasets
- [mC4](https://huggingface.co/datasets/mc4)
- [MQA](https://huggingface.co/datasets/clips/mqa)
- [JNLI](https://github.com/yahoojapan/JGLUE)
- [JSNLI](https://nlp.ist.i.kyoto-u.ac.jp/?%E6%97%A5%E6%9C%AC%E8%AA%9ESNLI%28JSNLI%29%E3%83%87%E3%83%BC%E3%82%BF%E3%82%BB%E3%83%83%E3%83%88)
- [PAWS-X](https://huggingface.co/datasets/paws-x)
- [JSeM](https://github.com/DaisukeBekki/JSeM)
- [MoritzLaurer/multilingual-NLI-26lang-2mil7](https://huggingface.co/datasets/MoritzLaurer/multilingual-NLI-26lang-2mil7)
    - [MultiNLI](https://huggingface.co/datasets/multi_nli)
    - [WANLI](https://huggingface.co/datasets/alisawuffles/WANLI)
    - [FeverNLI](https://github.com/easonnie/combine-FEVER-NSMN/blob/master/other_resources/nli_fever.md)
    - [LingNLI](https://arxiv.org/pdf/2104.07179.pdf)
- [JSICK](https://github.com/verypluming/JSICK)
- [Mr.Tidy](https://huggingface.co/datasets/castorini/mr-tydi)
- [JSTS](https://github.com/yahoojapan/JGLUE) (used for validation) [^1]

## Benchmarks
### Semantic Similarity Calculation ([JSTS](https://github.com/yahoojapan/JGLUE) dev set)
Evaluation by Spearman's correlation coefficient and Pearson's correlation coefficient.
| Model | Spearman | Pearson |
| --- | --- | --- |
| [text-embedding-ada-002](https://platform.openai.com/docs/guides/embeddings) |0.837[^2] | 0.790[^2] |
| [pkshatech/simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp)[^3] | 0.850 | 0.801 |
| pkshatech/GLuCoSE-base-ja | **0.864**  | **0.818** | 

### Zero-shot Search ([AIO3](https://sites.google.com/view/project-aio/competition3?authuser=0) dev set)
Evaluation by top-k retrieval accuracy[^4] (the fraction of questions that have a correct answer in the top-k retrieved documents at least once.)
| Model | Top-1 | Top-5 | Top-10 | Top-50 |
| --- | --- | --- | --- | --- |
| [text-embedding-ada-002](https://platform.openai.com/docs/guides/embeddings) | 33.50 | 57.80 | 65.10 | 76.60 |
| [pkshatech/simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp)[^3] | 30.60 | 54.50 | 62.50 | 76.70 |
| pkshatech/GLuCoSE-base-ja | **36.10** | **59.40** | **66.40** | **78.30** |


# Authors
[Akihiko Fukuchi](https://huggingface.co/akiFQC), [Yuichiro Hoshino](https://huggingface.co/Yuichiroh), [Yotarow Watanabe](https://huggingface.co/yotarow)

## License
This model is published under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

[^1]: When we trained this model, the test data of JGLUE was not released, so we used the dev set of JGLUE as a private evaluation data. Therefore, we selected the checkpoint on the train set of JGLUE insted of its dev set.  
[^2]: https://qiita.com/akeyhero/items/ce371bfed64399027c23     
[^3]: This is the model we have released before.  
[^4]: For more details, please refer to https://arxiv.org/pdf/2004.04906.pdf.