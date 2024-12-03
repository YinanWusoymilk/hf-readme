---
tags:
  - sentence-transformers
  - feature-extraction
  - sentence-similarity
  - mteb
  - transformers
  - transformers.js
datasets:
  - allenai/c4
language: en
inference: false
license: apache-2.0
---
<!-- TODO: add evaluation results here -->
<br><br>

<p align="center">
<img src="https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/603763514de52ff951d89793/AFoybzd5lpBQXEBrQHuTt.png?w=200&h=200&f=face" alt="Finetuner logo: Finetuner helps you to create experiments in order to improve embeddings on search tasks. It accompanies you to deliver the last mile of performance-tuning for neural search applications." width="150px">
</p>


<p align="center">
<b>The text embedding set trained by <a href="https://jina.ai/"><b>Jina AI</b></a>.</b>
</p>

## Quick Start

The easiest way to starting using `jina-embeddings-v2-base-code` is to use Jina AI's [Embedding API](https://jina.ai/embeddings/).


## Intended Usage & Model Info

`jina-embeddings-v2-base-code` is an multilingual **embedding model** speaks **English and 30 widely used programming languages**.
Same as other jina-embeddings-v2 series, it supports **8192** sequence length.

`jina-embeddings-v2-base-code` is based on a Bert architecture (JinaBert) that supports the symmetric bidirectional variant of [ALiBi](https://arxiv.org/abs/2108.12409) to allow longer sequence length.
The backbone `jina-bert-v2-base-code` is pretrained on the [github-code](https://huggingface.co/datasets/codeparrot/github-code) dataset.
The model is further trained on Jina AI's collection of more than 150 millions of coding question answer and docstring source code pairs.
These pairs were obtained from various domains and were carefully selected through a thorough cleaning process.

The embedding model was trained using 512 sequence length, but extrapolates to 8k sequence length (or even longer) thanks to ALiBi.
This makes our model useful for a range of use cases, especially when processing long documents is needed, including technical question answering and code search.

This model has 161 million parameters, which enables fast and memory efficient inference, while delivering impressive performance.
Additionally, we provide the following embedding models:

- [`jina-embeddings-v2-small-en`](https://huggingface.co/jinaai/jina-embeddings-v2-small-en): 33 million parameters.
- [`jina-embeddings-v2-base-en`](https://huggingface.co/jinaai/jina-embeddings-v2-base-en): 137 million parameters.
- [`jina-embeddings-v2-base-zh`](https://huggingface.co/jinaai/jina-embeddings-v2-base-zh): Chinese-English Bilingual embeddings.
- [`jina-embeddings-v2-base-de`](https://huggingface.co/jinaai/jina-embeddings-v2-base-de): German-English Bilingual embeddings.
- [`jina-embeddings-v2-base-es`](https://huggingface.co/jinaai/jina-embeddings-v2-base-es): Spanish-English Bilingual embeddings (soon).
- [`jina-embeddings-v2-base-code`](https://huggingface.co/jinaai/jina-embeddings-v2-base-code): 161 million parameters code embeddings.

**<details><summary>Supported (Programming) Languages</summary>**
<p>

- English
- Assembly
- Batchfile
- C
- C#
- C++
- CMake
- CSS
- Dockerfile
- FORTRAN
- GO
- Haskell
- HTML
- Java
- JavaScript
- Julia
- Lua
- Makefile
- Markdown
- PHP
- Perl
- PowerShell
- Python
- Ruby
- Rust
- SQL
- Scala
- Shell
- TypeScript
- TeX
- Visual Basic
</p>
</details>

## Data & Parameters

Jina Embeddings V2 [technical report](https://arxiv.org/abs/2310.19923)

## Usage

**<details><summary>Please apply mean pooling when integrating the model.</summary>**
<p>

### Why mean pooling?

`mean poooling` takes all token embeddings from model output and averaging them at sentence/paragraph level.
It has been proved to be the most effective way to produce high-quality sentence embeddings.
We offer an `encode` function to deal with this.

However, if you would like to do it without using the default `encode` function:

```python
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

sentences = [
    'How do I access the index while iterating over a sequence with a for loop?',
    '# Use the built-in enumerator\nfor idx, x in enumerate(xs):\n    print(idx, x)',
]

tokenizer = AutoTokenizer.from_pretrained('jinaai/jina-embeddings-v2-base-code')
model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-code', trust_remote_code=True)

encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

with torch.no_grad():
    model_output = model(**encoded_input)

embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
embeddings = F.normalize(embeddings, p=2, dim=1)
```

</p>
</details>

You can use Jina Embedding models directly from transformers package:
```python
!pip install transformers
from transformers import AutoModel
from numpy.linalg import norm

cos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))
model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-code', trust_remote_code=True)
embeddings = model.encode(
    [
        'How do I access the index while iterating over a sequence with a for loop?',
        '# Use the built-in enumerator\nfor idx, x in enumerate(xs):\n    print(idx, x)',
    ]
)
print(cos_sim(embeddings[0], embeddings[1]))
>>> tensor([[0.7282]])
```

If you only want to handle shorter sequence, such as 2k, pass the `max_length` parameter to the `encode` function:

```python
embeddings = model.encode(
    ['Very long ... code'],
    max_length=2048
)
```

Using the its latest release (v2.3.0) sentence-transformers also supports Jina embeddings (Please make sure that you are logged into huggingface as well):

```python
!pip install -U sentence-transformers
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer(
    "jinaai/jina-embeddings-v2-base-code",
    trust_remote_code=True
)

# control your input sequence length up to 8192
model.max_seq_length = 1024

embeddings = model.encode([
    'How do I access the index while iterating over a sequence with a for loop?',
    '# Use the built-in enumerator\nfor idx, x in enumerate(xs):\n    print(idx, x)',
])
print(cos_sim(embeddings[0], embeddings[1]))
```

You can also use the [Transformers.js](https://huggingface.co/docs/transformers.js) library to compute embeddings in JavaScript.
```js
// npm i @xenova/transformers
import { pipeline, cos_sim } from '@xenova/transformers';

const extractor = await pipeline('feature-extraction', 'jinaai/jina-embeddings-v2-base-code', {
    quantized: false, // Comment out this line to use the 8-bit quantized version
});

const texts = [
    'How do I access the index while iterating over a sequence with a for loop?',
    '# Use the built-in enumerator\nfor idx, x in enumerate(xs):\n    print(idx, x)',
]
const embeddings = await extractor(texts, { pooling: 'mean' });

const score = cos_sim(embeddings[0].data, embeddings[1].data);
console.log(score);
// 0.7281748759529421
```

## Plans

1. Bilingual embedding models supporting more European & Asian languages, including Spanish, French, Italian and Japanese.
2. Multimodal embedding models enable Multimodal RAG applications.
3. High-performt rerankers.

## Contact

Join our [Discord community](https://discord.jina.ai) and chat with other community members about ideas.