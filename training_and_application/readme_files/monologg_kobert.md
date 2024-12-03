---
license: apache-2.0
language:
  - ko
inference: false
---

# KoBERT

## How to use

> If you want to import KoBERT tokenizer with `AutoTokenizer`, you should give `trust_remote_code=True`.

```python
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("monologg/kobert")
tokenizer = AutoTokenizer.from_pretrained("monologg/kobert", trust_remote_code=True)
```

## Reference

- https://github.com/SKTBrain/KoBERT
