---
library_name: transformers
language:
- ru
pipeline_tag: feature-extraction
datasets:
- uonlp/CulturaX
---

# ruRoPEBert Sentence Model for Russian language

This is an encoder model from **Tochka AI** based on the **RoPEBert** architecture, using the cloning method described in [our article on Habr](https://habr.com/ru/companies/tochka/articles/797561/).

[CulturaX](https://huggingface.co/papers/2309.09400) dataset was used for model training. The **hivaze/ru-e5-base** (only english and russian embeddings of **intfloat/multilingual-e5-base**) model was used as the original; this model surpasses it and all other models in quality (at the time of creation), according to the `S+W` score of [encodechka](https://github.com/avidale/encodechka) benchmark.

The model source code is available in the file [modeling_rope_bert.py](https://huggingface.co/Tochka-AI/ruRoPEBert-e5-base-2k/blob/main/modeling_rope_bert.py)

The model is trained on contexts **up to 2048 tokens** in length, but can be used on larger contexts.

## Usage

**Important**: 4.37.2 and higher is the recommended version of `transformers`. To load the model correctly, you must enable dowloading code from the model's repository: `trust_remote_code=True`, this will download the **modeling_rope_bert.py** script and load the weights into the correct architecture.
Otherwise, you can download this script manually and use classes from it directly to load the model.

### Basic usage (no efficient attention)

```python
model_name = 'Tochka-AI/ruRoPEBert-e5-base-2k'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True, attn_implementation='eager')
```

### With SDPA (efficient attention)

```python
model = AutoModel.from_pretrained(model_name, trust_remote_code=True, attn_implementation='sdpa')
```

### Getting embeddings

The correct pooler (`mean`) is already **built into the model architecture**, which averages embeddings based on the attention mask. You can also select the pooler type (`first_token_transform`), which performs a learnable linear transformation on the first token.

To change built-in pooler implementation use `pooler_type` parameter in `AutoModel.from_pretrained` function

```python
test_batch = tokenizer.batch_encode_plus(["Привет, чем занят?", "Здравствуйте, чем вы занимаетесь?"], return_tensors='pt', padding=True)
with torch.inference_mode():
  pooled_output = model(**test_batch).pooler_output   
```

In addition, you can calculate cosine similarities between texts in batch using normalization and matrix multiplication:

```python
import torch.nn.functional as F
F.normalize(pooled_output, dim=1) @ F.normalize(pooled_output, dim=1).T
```

### Using as classifier

To load the model with trainable classification head on top (change `num_labels` parameter):

```python
model = AutoModelForSequenceClassification.from_pretrained(model_name, trust_remote_code=True, attn_implementation='sdpa', num_labels=4)
```

### With RoPE scaling

Allowed types for RoPE scaling are: `linear` and `dynamic`. To extend the model's context window you need to change tokenizer max length and add `rope_scaling` parameter.

If you want to scale your model context by 2x:
```python
tokenizer.model_max_length = 4096
model = AutoModel.from_pretrained(model_name,
                                  trust_remote_code=True,
                                  attn_implementation='sdpa',
                                  rope_scaling={'type': 'dynamic','factor': 2.0}
                                  ) # 2.0 for x2 scaling, 4.0 for x4, etc..
```

P.S. Don't forget to specify the dtype and device you need to use resources efficiently.

## Metrics

Evaluation of this model on encodechka benchmark:

 | Model name          | STS | PI   | NLI | SA  | TI  | IA  | IC  | ICX | NE1 | NE2 | Avg S (no NE) | Avg S+W (with NE) |
|---------------------|-----|------|-----|-----|-----|-----|-----|-----|-----|-----|---------------|-------------------|
| ruRoPEBert-e5-base-512    | 0.793 | 0.704 | 0.457 | 0.803 | 0.970 | 0.788 | 0.802 | 0.749 | 0.328 | 0.396 | 0.758     | 0.679                 |
| **ruRoPEBert-e5-base-2k**    | 0.787 | 0.708 | 0.460 | 0.804 | 0.970 | 0.792 | 0.803 | 0.749 | 0.402 | 0.423 | 0.759     | 0.689                 |
| intfloat/multilingual-e5-base | 0.834 | 0.704 | 0.458 | 0.795 | 0.964 | 0.782 | 0.803 | 0.740 | 0.234 | 0.373 | 0.76      | 0.668                 |

## Authors
- Sergei Bratchikov (Tochka AI Team, [HF](https://huggingface.co/hivaze), [GitHub](https://github.com/hivaze))
- Maxim Afanasiev (Tochka AI Team, [HF](https://huggingface.co/mrapplexz), [GitHub](https://github.com/mrapplexz))