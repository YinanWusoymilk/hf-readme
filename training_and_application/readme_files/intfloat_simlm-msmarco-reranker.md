---
license: mit
language:
- en
---
# SimLM: Pre-training with Representation Bottleneck for Dense Passage Retrieval 

paper available at [https://arxiv.org/pdf/2207.02578](https://arxiv.org/pdf/2207.02578)

code available at [https://github.com/microsoft/unilm/tree/master/simlm](https://github.com/microsoft/unilm/tree/master/simlm)

## Paper abstract

In this paper, we propose SimLM (Similarity matching with Language Model pre-training), a simple yet effective pre-training method for dense passage retrieval. 
It employs a simple bottleneck architecture that learns to compress the passage information into a dense vector through self-supervised pre-training. 
We use a replaced language modeling objective, which is inspired by ELECTRA, 
to improve the sample efficiency and reduce the mismatch of the input distribution between pre-training and fine-tuning. 
SimLM only requires access to unlabeled corpus, and is more broadly applicable when there are no labeled data or queries. 
We conduct experiments on several large-scale passage retrieval datasets, and show substantial improvements over strong baselines under various settings. 
Remarkably, SimLM even outperforms multi-vector approaches such as ColBERTv2 which incurs significantly more storage cost.

## Results on MS-MARCO passage ranking task

| Model | dev MRR@10 | dev R@50  | dev R@1k  |  TREC DL 2019 nDCG@10 | TREC DL 2020 nDCG@10  |
|--|---|---|---|---|---|
| **SimLM (this model)** | 43.8 |  89.2 | 98.6  | 74.6 | 72.7 |

## Usage

Since we use a listwise loss to train the re-ranker,
the relevance score is not bounded to a specific numerical range.
Higher scores mean more relevant between the given query and passage.

Get relevance score from our re-ranker:

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, BatchEncoding, PreTrainedTokenizerFast
from transformers.modeling_outputs import SequenceClassifierOutput

def encode(tokenizer: PreTrainedTokenizerFast,
           query: str, passage: str, title: str = '-') -> BatchEncoding:
    return tokenizer(query,
                     text_pair='{}: {}'.format(title, passage),
                     max_length=192,
                     padding=True,
                     truncation=True,
                     return_tensors='pt')

tokenizer = AutoTokenizer.from_pretrained('intfloat/simlm-msmarco-reranker')
model = AutoModelForSequenceClassification.from_pretrained('intfloat/simlm-msmarco-reranker')
model.eval()

with torch.no_grad():
    batch_dict = encode(tokenizer, 'how long is super bowl game', 'The Super Bowl is typically four hours long. The game itself takes about three and a half hours, with a 30 minute halftime show built in.')
    outputs: SequenceClassifierOutput = model(**batch_dict, return_dict=True)
    print(outputs.logits[0])

    batch_dict = encode(tokenizer, 'how long is super bowl game', 'The cost of a Super Bowl commercial runs about $5 million for 30 seconds of airtime. But the benefits that the spot can bring to a brand can help to justify the cost.')
    outputs: SequenceClassifierOutput = model(**batch_dict, return_dict=True)
    print(outputs.logits[0])
```

## Citation

```bibtex
@article{Wang2022SimLMPW,
  title={SimLM: Pre-training with Representation Bottleneck for Dense Passage Retrieval},
  author={Liang Wang and Nan Yang and Xiaolong Huang and Binxing Jiao and Linjun Yang and Daxin Jiang and Rangan Majumder and Furu Wei},
  journal={ArXiv},
  year={2022},
  volume={abs/2207.02578}
}
```