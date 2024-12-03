---
language: ko
tags:
- bart
license: mit
---

## KoBART-base-v2

With the addition of chatting data, the model is trained to handle the semantics of sequences longer than KoBART.

```python
from transformers import PreTrainedTokenizerFast, BartModel

tokenizer = PreTrainedTokenizerFast.from_pretrained('hyunwoongko/kobart')
model = BartModel.from_pretrained('hyunwoongko/kobart')
```

### Performance 

NSMC
- acc. : 0.901

### hyunwoongko/kobart
- Added bos/eos post processor
- Removed token_type_ids
