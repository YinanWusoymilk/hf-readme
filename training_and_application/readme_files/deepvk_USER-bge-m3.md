---
language:
- ru
library_name: sentence-transformers
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
widget: []
pipeline_tag: sentence-similarity
license: apache-2.0
datasets:
  - deepvk/ru-HNP
  - deepvk/ru-WANLI
  - Shitao/bge-m3-data
  - RussianNLP/russian_super_glue
  - reciTAL/mlsum
  - Milana/russian_keywords
  - IlyaGusev/gazeta
  - d0rj/gsm8k-ru
  - bragovo/dsum_ru
  - CarlBrendt/Summ_Dialog_News
---

# USER-bge-m3


**U**niversal **S**entence **E**ncoder for **R**ussian (USER) is a [sentence-transformer](https://www.SBERT.net) model for extracting embeddings exclusively for Russian language.
It maps sentences & paragraphs to a 1024 dimensional dense vector space and can be used for tasks like clustering or semantic search.


This model is initialized from [`TatonkaHF/bge-m3_en_ru`](https://huggingface.co/TatonkaHF/bge-m3_en_ru) which is shrinked version of [`baai/bge-m3`](https://huggingface.co/BAAI/bge-m3) model and trained to work mainly with the Russian language. Its quality on other languages was not evaluated.


## Usage


Using this model becomes easy when you have [`sentence-transformers`](https://www.SBERT.net) installed:


```
pip install -U sentence-transformers
```


Then you can use the model like this:


```python
from sentence_transformers import SentenceTransformer


input_texts = [
  "Когда был спущен на воду первый миноносец «Спокойный»?",
  "Есть ли нефть в Удмуртии?",
  "Спокойный (эсминец)\nЗачислен в списки ВМФ СССР 19 августа 1952 года.",
  "Нефтепоисковые работы в Удмуртии были начаты сразу после Второй мировой войны в 1945 году и продолжаются по сей день. Добыча нефти началась в 1967 году."
]


model = SentenceTransformer("deepvk/USER-bge-m3")
embeddings = model.encode(input_texts, normalize_embeddings=True)
```


However, you can use model directly with [`transformers`](https://huggingface.co/docs/transformers/en/index)


```python
import torch.nn.functional as F
from torch import Tensor, inference_mode
from transformers import AutoTokenizer, AutoModel


input_texts = [
  "Когда был спущен на воду первый миноносец «Спокойный»?",
  "Есть ли нефть в Удмуртии?",
  "Спокойный (эсминец)\nЗачислен в списки ВМФ СССР 19 августа 1952 года.",
  "Нефтепоисковые работы в Удмуртии были начаты сразу после Второй мировой войны в 1945 году и продолжаются по сей день. Добыча нефти началась в 1967 году."
]


tokenizer = AutoTokenizer.from_pretrained("deepvk/USER-bge-m3")
model = AutoModel.from_pretrained("deepvk/USER-bge-m3")
model.eval()


encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
with torch.no_grad():
  model_output = model(**encoded_input) 
  # Perform pooling. In this case, cls pooling.
  sentence_embeddings = model_output[0][:, 0]

# normalize embeddings
sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)

# [[0.5567, 0.3014],
#  [0.1701, 0.7122]]
scores = (sentence_embeddings[:2] @ sentence_embeddings[2:].T)
```

Also, you can use native [FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) library for evaluation. Usage is described in [`bge-m3` model card](https://huggingface.co/BAAI/bge-m3).


# Training Details


We follow the [`USER-base`](https://huggingface.co/deepvk/USER-base) model training algorithm, with several changes as we use different backbone.


**Initialization:** [`TatonkaHF/bge-m3_en_ru`](https://huggingface.co/TatonkaHF/bge-m3_en_ru) – shrinked version of [`baai/bge-m3`](https://huggingface.co/BAAI/bge-m3) to support only Russian and English tokens.


**Fine-tuning:** Supervised fine-tuning two different models based on data symmetry and then merging via [`LM-Cocktail`](https://arxiv.org/abs/2311.13534):


1. Since we split the data, we could additionally apply the [AnglE loss](https://arxiv.org/abs/2309.12871) to the symmetric model, which enhances performance on symmetric tasks.


2. Finally, we added the original `bge-m3` model to the two obtained models to prevent catastrophic forgetting, tuning the weights for the merger using `LM-Cocktail` to produce the final model, **USER-bge-m3**.


### Dataset


During model development, we additional collect 2 datasets:
[`deepvk/ru-HNP`](https://huggingface.co/datasets/deepvk/ru-HNP) and 
[`deepvk/ru-WANLI`](https://huggingface.co/datasets/deepvk/ru-WANLI).


| Symmetric Dataset | Size  | Asymmetric Dataset | Size |
|-------------------|-------|--------------------|------|
| **AllNLI**        | 282 644 | [**MIRACL**](https://huggingface.co/datasets/Shitao/bge-m3-data/tree/main)         | 10 000 |
| [MedNLI](https://github.com/jgc128/mednli)            | 3 699  | [MLDR](https://huggingface.co/datasets/Shitao/bge-m3-data/tree/main)               | 1 864  |
| [RCB](https://huggingface.co/datasets/RussianNLP/russian_super_glue)               | 392   | [Lenta](https://github.com/yutkin/Lenta.Ru-News-Dataset)              | 185 972 |
| [Terra](https://huggingface.co/datasets/RussianNLP/russian_super_glue)             | 1 359  | [Mlsum](https://huggingface.co/datasets/reciTAL/mlsum)              | 51 112  |
| [Tapaco](https://huggingface.co/datasets/tapaco)            | 91 240 | [Mr-TyDi](https://huggingface.co/datasets/Shitao/bge-m3-data/tree/main)            | 536 600 |
|  [**deepvk/ru-WANLI**](https://huggingface.co/datasets/deepvk/ru-WANLI)         | 35 455 | [Panorama](https://huggingface.co/datasets/its5Q/panorama)          | 11 024  |
|   [**deepvk/ru-HNP**](https://huggingface.co/datasets/deepvk/ru-HNP)       | 500 000 | [PravoIsrael](https://huggingface.co/datasets/TarasHu/pravoIsrael)        | 26 364  |
| |  | [Xlsum](https://huggingface.co/datasets/csebuetnlp/xlsum)           | 124 486 |
|      |  | [Fialka-v1](https://huggingface.co/datasets/0x7o/fialka-v1)          | 130 000 |
|             |  | [RussianKeywords](https://huggingface.co/datasets/Milana/russian_keywords)    | 16 461  |
|        |  | [Gazeta](https://huggingface.co/datasets/IlyaGusev/gazeta)             | 121 928 |
|                   |       | [Gsm8k-ru](https://huggingface.co/datasets/d0rj/gsm8k-ru)           | 7 470   |
|                   |       | [DSumRu](https://huggingface.co/datasets/bragovo/dsum_ru)             | 27 191  |
|                   |       | [SummDialogNews](https://huggingface.co/datasets/CarlBrendt/Summ_Dialog_News)     | 75 700  |




**Total positive pairs:** 2,240,961
**Total negative pairs:** 792,644 (negative pairs from AIINLI, MIRACL, deepvk/ru-WANLI, deepvk/ru-HNP)


For all labeled datasets, we only use its training set for fine-tuning.
For datasets Gazeta, Mlsum, Xlsum: pairs (title/text) and (title/summary) are combined and used as asymmetric data.


`AllNLI` is an translated to Russian combination of SNLI, MNLI and ANLI.


## Experiments


We compare our mode with the basic [`baai/bge-m3`](https://huggingface.co/BAAI/bge-m3) on the [`encodechka`](https://github.com/avidale/encodechka) benchmark.
In addition, we evaluate model on the russian subset of [`MTEB`](https://github.com/embeddings-benchmark/mteb) on Classification, Reranking, Multilabel Classification, STS, Retrieval, and PairClassification tasks.
We use validation scripts from the official repositories for each of the tasks.


Results on encodechka: 
| Model       | Mean S | Mean S+W | STS  | PI   | NLI  | SA   | TI   | IA   | IC   | ICX  | NE1  | NE2  |
|-------------|--------|----------|------|------|------|------|------|------|------|------|------|------|
| [`baai/bge-m3`](https://huggingface.co/BAAI/bge-m3) | 0.787     | 0.696     | 0.86     | 0.75     | 0.51     | 0.82 | 0.97 | 0.79 | 0.81 | 0.78 | 0.24     | 0.42     |
| `USER-bge-m3`                                       | **0.799** | **0.709** | **0.87** | **0.76** | **0.58** | 0.82 | 0.97 | 0.79 | 0.81 | 0.78 | **0.28** | **0.43** |


Results on MTEB:


| Type                      | [`baai/bge-m3`](https://huggingface.co/BAAI/bge-m3) | `USER-bge-m3` |
|---------------------------|--------|-------------|
| Average (30 datasets)           | 0.689  | **0.706**       |
| Classification Average (12 datasets)           | 0.571  | **0.594**      |
| Reranking Average (2 datasets)                | **0.698**  | 0.688       |
| MultilabelClassification (2 datasets)  | 0.343  | **0.359**       |
| STS Average (4 datasets)                      | 0.735  | **0.753**       |
| Retrieval Average (6 datasets)                | **0.945**  | 0.934       |
| PairClassification Average (4 datasets)       | 0.784  | **0.833**       |


## Limitations


We did not thoroughly evaluate the model's ability for sparse and multi-vec encoding.


## Citations


```
@misc{deepvk2024user,
    title={USER: Universal Sentence Encoder for Russian},
    author={Malashenko, Boris and  Zemerov, Anton and Spirin, Egor},
    url={https://huggingface.co/datasets/deepvk/USER-base},
    publisher={Hugging Face}
    year={2024},
}
```
