---
language: en
tags:
- tapex
- table-question-answering
datasets:
- wikitablequestions
license: mit
---

# TAPEX (large-sized model) 

TAPEX was proposed in [TAPEX: Table Pre-training via Learning a Neural SQL Executor](https://arxiv.org/abs/2107.07653) by Qian Liu, Bei Chen, Jiaqi Guo, Morteza Ziyadi, Zeqi Lin, Weizhu Chen, Jian-Guang Lou. The original repo can be found [here](https://github.com/microsoft/Table-Pretraining).

## Model description

TAPEX (**Ta**ble **P**re-training via **Ex**ecution) is a conceptually simple and empirically powerful pre-training approach to empower existing models with *table reasoning* skills. TAPEX realizes table pre-training by learning a neural SQL executor over a synthetic corpus, which is obtained by automatically synthesizing executable SQL queries.

TAPEX is based on the BART architecture, the transformer encoder-decoder (seq2seq) model with a bidirectional (BERT-like) encoder and an autoregressive (GPT-like) decoder.

This model is the `tapex-base` model fine-tuned on the [WikiTableQuestions](https://huggingface.co/datasets/wikitablequestions) dataset.

## Intended Uses

You can use the model for table question answering on *complex* questions. Some **solveable** questions are shown below (corresponding tables now shown):

| Question | Answer |
|:---: |:---:|
| according to the table, what is the last title that spicy horse produced? | Akaneiro: Demon Hunters |
| what is the difference in runners-up from coleraine academical institution and royal school dungannon? | 20 |
| what were the first and last movies greenstreet acted in? | The Maltese Falcon, Malaya |
| in which olympic games did arasay thondike not finish in the top 20? | 2012 |
| which broadcaster hosted 3 titles but they had only 1 episode? | Channel 4 |


### How to Use

Here is how to use this model in transformers:

```python
from transformers import TapexTokenizer, BartForConditionalGeneration
import pandas as pd

tokenizer = TapexTokenizer.from_pretrained("microsoft/tapex-large-finetuned-wtq")
model = BartForConditionalGeneration.from_pretrained("microsoft/tapex-large-finetuned-wtq")

data = {
    "year": [1896, 1900, 1904, 2004, 2008, 2012],
    "city": ["athens", "paris", "st. louis", "athens", "beijing", "london"]
}
table = pd.DataFrame.from_dict(data)

# tapex accepts uncased input since it is pre-trained on the uncased corpus
query = "In which year did beijing host the Olympic Games?"
encoding = tokenizer(table=table, query=query, return_tensors="pt")

outputs = model.generate(**encoding)

print(tokenizer.batch_decode(outputs, skip_special_tokens=True))
# [' 2008.0']
```

### How to Eval

Please find the eval script [here](https://github.com/huggingface/transformers/tree/main/examples/research_projects/tapex).

### BibTeX entry and citation info

```bibtex
@inproceedings{
    liu2022tapex,
    title={{TAPEX}: Table Pre-training via Learning a Neural {SQL} Executor},
    author={Qian Liu and Bei Chen and Jiaqi Guo and Morteza Ziyadi and Zeqi Lin and Weizhu Chen and Jian-Guang Lou},
    booktitle={International Conference on Learning Representations},
    year={2022},
    url={https://openreview.net/forum?id=O50443AsCP}
}
```