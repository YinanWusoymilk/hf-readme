---
language:
- tr
pipeline_tag: sentence-similarity
license: apache-2.0
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
datasets:
- nli_tr
- emrecan/stsb-mt-turkish
widget:
  source_sentence: "Bu çok mutlu bir kişi"
  sentences:
    - "Bu mutlu bir köpek"
    - "Bu sevincinden havalara uçan bir insan"
    - "Çok kar yağıyor"
    
---

# emrecan/bert-base-turkish-cased-mean-nli-stsb-tr

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search. The model was trained on Turkish machine translated versions of [NLI](https://huggingface.co/datasets/nli_tr) and [STS-b](https://huggingface.co/datasets/emrecan/stsb-mt-turkish) datasets, using example [training scripts]( https://github.com/UKPLab/sentence-transformers/tree/master/examples/training) from sentence-transformers GitHub repository.

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["Bu örnek bir cümle", "Her cümle vektöre çevriliyor"]

model = SentenceTransformer('emrecan/bert-base-turkish-cased-mean-nli-stsb-tr')
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
sentences = ["Bu örnek bir cümle", "Her cümle vektöre çevriliyor"]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('emrecan/bert-base-turkish-cased-mean-nli-stsb-tr')
model = AutoModel.from_pretrained('emrecan/bert-base-turkish-cased-mean-nli-stsb-tr')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, mean pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)
```



## Evaluation Results

Evaluation results on test and development sets are given below:

| Split      | Epoch | cosine_pearson | cosine_spearman | euclidean_pearson | euclidean_spearman | manhattan_pearson | manhattan_spearman | dot_pearson | dot_spearman |
|------------|-------|----------------|-----------------|-------------------|--------------------|-------------------|--------------------|-------------|--------------|
| test       |   -   | 0.834          | 0.830           | 0.820             | 0.819              | 0.819             | 0.818              | 0.799       | 0.789        |
| validation | 1     | 0.850          | 0.848           | 0.831             | 0.835              | 0.83              | 0.83               | 0.80        | 0.806        |
| validation | 2     | 0.857          | 0.857           | 0.844             | 0.848              | 0.844             | 0.848              | 0.813       | 0.810        |
| validation | 3     | 0.860          | 0.859           | 0.846             | 0.851              | 0.846             | 0.850              | 0.825       | 0.822        |
| validation | 4     | 0.859          | 0.860           | 0.846             | 0.851              | 0.846             | 0.851              | 0.825       | 0.823        |


## Training
Training scripts [`training_nli_v2.py`](https://github.com/UKPLab/sentence-transformers/blob/master/examples/training/nli/training_nli_v2.py) and [`training_stsbenchmark_continue_training.py`](https://github.com/UKPLab/sentence-transformers/blob/master/examples/training/sts/training_stsbenchmark_continue_training.py) were used to train the model.

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
    "epochs": 4,
    "evaluation_steps": 200,
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
  (0): Transformer({'max_seq_length': 75, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->