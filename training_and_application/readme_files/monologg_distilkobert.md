---
license: apache-2.0
language:
  - ko
inference: false
---

# DistilKoBERT

## How to use

> If you want to import DistilKoBERT tokenizer with `AutoTokenizer`, you should give `trust_remote_code=True`.

```python
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("monologg/distilkobert")
tokenizer = AutoTokenizer.from_pretrained("monologg/distilkobert", trust_remote_code=True)
```

## Reference

- https://github.com/monologg/DistilKoBERT
