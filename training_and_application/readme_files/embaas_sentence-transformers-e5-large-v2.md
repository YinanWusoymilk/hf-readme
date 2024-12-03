---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity

---

# embaas/sentence-transformers-e5-large-v2

This is a the sentence-transformers version of the [intfloat/e5-large-v2](https://huggingface.co/intfloat/e5-large-v2) model: It maps sentences & paragraphs to a 1024 dimensional dense vector space and can be used for tasks like clustering or semantic search.

<!--- Describe your model here -->

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('embaas/sentence-transformers-e5-large-v2')
embeddings = model.encode(sentences)
print(embeddings)
```

## Using with API

You can use the [embaas API](https://embaas.io) to encode your input. Get your free API key from [embaas.io](https://embaas.io)

```python
import requests
 
url = "https://api.embaas.io/v1/embeddings/"
 
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ${YOUR_API_KEY}"
}
 
data = {
    "texts": ["This is an example sentence.", "Here is another sentence."],
    "instruction": "query"
    "model": "e5-large-v2"
}
 
response = requests.post(url, json=data, headers=headers)
```


## Evaluation Results

<!--- Describe how your model was evaluated -->

Find the results of the e5 at the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard)



## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False})
  (2): Normalize()
)
```

## Citing & Authors

<!--- Describe where people can find more information -->