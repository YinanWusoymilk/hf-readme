---
license: apache-2.0
language:
- en
pipeline_tag: sentence-similarity
inference: false
---

# Monarch Mixer-BERT

An 80M checkpoint of M2-BERT, pretrained with sequence length 32768, and it has been fine-tuned for long-context retrieval.

Check out the paper [Monarch Mixer: A Simple Sub-Quadratic GEMM-Based Architecture](https://arxiv.org/abs/2310.12109) and our [blog post]() on retrieval for more on how we trained this model for long sequence.

This model was trained by Jon Saad-Falcon, Dan Fu, and Simran Arora.

Check out our [GitHub](https://github.com/HazyResearch/m2/tree/main) for instructions on how to download and fine-tune it!

## How to use

You can load this model using Hugging Face `AutoModel`:
```python
from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained(
  "togethercomputer/m2-bert-80M-32k-retrieval",
  trust_remote_code=True
)
```

You should expect to see a large error message about unused parameters for FlashFFTConv.
If you'd like to load the model with FlashFFTConv, you can check out our [GitHub](https://github.com/HazyResearch/m2/tree/main).

This model generates embeddings for retrieval. The embeddings have a dimensionality of 768:
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

max_seq_length = 32768
testing_string = "Every morning, I make a cup of coffee to start my day."
model = AutoModelForSequenceClassification.from_pretrained(
  "togethercomputer/m2-bert-80M-32k-retrieval",
  trust_remote_code=True
)

tokenizer = AutoTokenizer.from_pretrained(
  "bert-base-uncased",
  model_max_length=max_seq_length
)
input_ids = tokenizer(
  [testing_string],
  return_tensors="pt",
  padding="max_length",
  return_token_type_ids=False,
  truncation=True,
  max_length=max_seq_length
)

outputs = model(**input_ids)
embeddings = outputs['sentence_embedding']
```

You can also get embeddings from this model using the Together API as follows (you can find your API key [here](https://api.together.xyz/settings/api-keys)):
```python
import os
import requests

def generate_together_embeddings(text: str, model_api_string: str, api_key: str):
    url = "https://api.together.xyz/api/v1/embeddings"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    session = requests.Session()
    response = session.post(
        url,
        headers=headers,
        json={
            "input": text,
            "model": model_api_string
        }
    )
    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")
    return response.json()['data'][0]['embedding']

print(generate_together_embeddings(
  'Hello world',
  'togethercomputer/m2-bert-80M-32k-retrieval',
  os.environ['TOGETHER_API_KEY'])[:10]
)
```

## Acknowledgments

Alycia Lee helped with AutoModel support.

## Citation

If you use this model, or otherwise found our work valuable, you can cite us as follows:
```
@inproceedings{fu2023monarch,
  title={Monarch Mixer: A Simple Sub-Quadratic GEMM-Based Architecture},
  author={Fu, Daniel Y and Arora, Simran and Grogan, Jessica and Johnson, Isys and Eyuboglu, Sabri and Thomas, Armin W and Spector, Benjamin and Poli, Michael and Rudra, Atri and R{\'e}, Christopher},
  booktitle={Advances in Neural Information Processing Systems},
  year={2023}
}
```