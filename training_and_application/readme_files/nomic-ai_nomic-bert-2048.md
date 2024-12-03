---
language:
- en
license: apache-2.0
datasets:
- wikimedia/wikipedia
- bookcorpus
- nomic-ai/nomic-bert-2048-pretraining-data
inference: false
---

# nomic-bert-2048: A 2048 Sequence Length Pretrained BERT

`nomic-bert-2048` is a BERT model pretrained on `wikipedia` and `bookcorpus` with a max sequence length of 2048. 

We make several modifications to our BERT training procedure similar to [MosaicBERT](https://www.databricks.com/blog/mosaicbert).
Namely, we add:
- Use [Rotary Position Embeddings](https://arxiv.org/pdf/2104.09864.pdf) to allow for context length extrapolation.
- Use SwiGLU activations as it has [been shown](https://arxiv.org/abs/2002.05202) to [improve model performance](https://www.databricks.com/blog/mosaicbert)
- Set dropout to 0

We evaluate the quality of nomic-bert-2048 on the standard [GLUE](https://gluebenchmark.com/) benchmark. We find
it performs comparably to other BERT models but with the advantage of a significantly longer context length.

| Model       | Bsz | Steps | Seq   | Avg      | Cola     | SST2     | MRPC | STSB | QQP  | MNLI | QNLI | RTE  |
|-------------|-----|-------|-------|----------|----------|----------|------|------|------|------|------|------|
| NomicBERT   | 4k  | 100k  | 2048  | 0.84     | 0.50     | 0.93     | 0.88 | 0.90 | 0.92 | 0.86 | 0.92 | 0.82 |
| RobertaBase | 8k  | 500k  | 512   | 0.86     | 0.64     | 0.95     | 0.90 | 0.91 | 0.92 | 0.88 | 0.93 | 0.79 |
| JinaBERTBase| 4k  | 100k  | 512   | 0.83     | 0.51     | 0.95     | 0.88 | 0.90 | 0.81 | 0.86 | 0.92 | 0.79 |
| MosaicBERT  | 4k  | 178k  | 128   | 0.85     | 0.59     | 0.94     | 0.89 | 0.90 | 0.92 | 0.86 | 0.91 | 0.83 |

## Pretraining Data

We use [BookCorpus](https://huggingface.co/datasets/bookcorpus) and a 2023 dump of [wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia). 
We pack and tokenize the sequences to 2048 tokens. If a document is shorter than 2048 tokens, we append another document until it fits 2048 tokens.
If a document is greater than 2048 tokens, we split it across multiple documents. We release the dataset [here](https://huggingface.co/datasets/nomic-ai/nomic-bert-2048-pretraining-data/)


# Usage

```python
from transformers import AutoModelForMaskedLM, AutoConfig, AutoTokenizer, pipeline

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased') # `nomic-bert-2048` uses the standard BERT tokenizer

config = AutoConfig.from_pretrained('nomic-ai/nomic-bert-2048', trust_remote_code=True) # the config needs to be passed in
model = AutoModelForMaskedLM.from_pretrained('nomic-ai/nomic-bert-2048',config=config, trust_remote_code=True)

# To use this model directly for masked language modeling
classifier = pipeline('fill-mask', model=model, tokenizer=tokenizer,device="cpu")

print(classifier("I [MASK] to the store yesterday."))
```
To finetune the model for a Sequence Classification task, you can use the following snippet

```python
from transformers import AutoConfig, AutoModelForSequenceClassification
model_path = "nomic-ai/nomic-bert-2048"
config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)
# strict needs to be false here since we're initializing some new params
model = AutoModelForSequenceClassification.from_pretrained(model_path, config=config, trust_remote_code=True, strict=False)
```

# Join the Nomic Community

- Nomic: [https://nomic.ai](https://nomic.ai)
- Discord: [https://discord.gg/myY5YDR8z8](https://discord.gg/myY5YDR8z8)
- Twitter: [https://twitter.com/nomic_ai](https://twitter.com/nomic_ai)