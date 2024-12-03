---
language: ko
---

# Albert base model for Korean

* 70GB Korean text dataset and 42000 lower-cased subwords are used
* Check the model performance and other language models for Korean in [github](https://github.com/kiyoungkim1/LM-kor)

```python
from transformers import BertTokenizerFast, AlbertModel

tokenizer_albert = BertTokenizerFast.from_pretrained("kykim/albert-kor-base")
model_albert = AlbertModel.from_pretrained("kykim/albert-kor-base")
```