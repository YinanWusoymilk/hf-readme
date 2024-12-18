---
pipeline_tag: sentence-similarity
language:
- es
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
license: apache-2.0
---

# hiiamsid/sentence_similarity_spanish_es

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

<!--- Describe your model here -->

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ['Mi nombre es Siddhartha', 'Mis amigos me llamaron por mi nombre Siddhartha']

model = SentenceTransformer('hiiamsid/sentence_similarity_spanish_es')
embeddings = model.encode(sentences)
print(embeddings)
```



## Usage (HuggingFace Transformers)
Without [sentence-transformers](https://www.SBERT.net), you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.

```python
from transformers import AutoTokenizer, AutoModel
import torch


#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ['Mi nombre es Siddhartha', 'Mis amigos me llamaron por mi nombre Siddhartha']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('hiiamsid/sentence_similarity_spanish_es')
model = AutoModel.from_pretrained('hiiamsid/sentence_similarity_spanish_es')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, max pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)
```



## Evaluation Results
```
cosine_pearson : 0.8280372842978689
cosine_spearman : 0.8232689765056079
euclidean_pearson : 0.81021993884437
euclidean_spearman : 0.8087904592393836
manhattan_pearson : 0.809645390126291
manhattan_spearman : 0.8077035464970413
dot_pearson : 0.7803662255836028
dot_spearman : 0.7699607641618339
```

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name=hiiamsid/sentence_similarity_spanish_es)


## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 360 with parameters:
```
{'batch_size': 16, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.CosineSimilarityLoss.CosineSimilarityLoss` 

Parameters of the fit()-Method:
```
{
    "callback": null,
    "epochs": 4,
    "evaluation_steps": 1000,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'transformers.optimization.AdamW'>",
    "optimizer_params": {
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 144,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors
- Datasets : [stsb_multi_mt](https://huggingface.co/datasets/stsb_multi_mt)
- Model : [dccuchile/bert-base-spanish-wwm-cased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased)
- Sentence Transformers [Semantic Textual Similarity](https://www.sbert.net/examples/training/sts/README.html)