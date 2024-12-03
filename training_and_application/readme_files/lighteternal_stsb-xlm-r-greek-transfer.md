---

language:
- en
- el

tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers


widget:
- source_sentence: "Το κινητό έπεσε και έσπασε."
  sentences: [
				"H πτώση κατέστρεψε τη συσκευή.",
				"Το αυτοκίνητο έσπασε στα δυο.",
				"Ο υπουργός έπεσε και έσπασε το πόδι του."
			]

pipeline_tag: sentence-similarity

license: apache-2.0
---

# Semantic Textual Similarity for the Greek language using Transformers and Transfer Learning
### By the Hellenic Army Academy (SSE) and the Technical University of Crete (TUC)


This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

We follow a Teacher-Student transfer learning approach described [here](https://www.sbert.net/examples/training/multilingual/README.html) to train an XLM-Roberta-base model on STS using parallel EN-EL sentence pairs.

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('{MODEL_NAME}')

sentences1 = ['Το κινητό έπεσε και έσπασε.',
             'Το κινητό έπεσε και έσπασε.',
             'Το κινητό έπεσε και έσπασε.']

sentences2 = ["H πτώση κατέστρεψε τη συσκευή.",
             "Το αυτοκίνητο έσπασε στα δυο.",
             "Ο υπουργός έπεσε και έσπασε το πόδι του."]


embeddings1 = model.encode(sentences1, convert_to_tensor=True)
embeddings2 = model.encode(sentences2, convert_to_tensor=True)

#Compute cosine-similarities (clone repo for util functions)
from sentence_transformers import util
cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)

#Output the pairs with their score
for i in range(len(sentences1)):
    print("{} 		 {} 		 Score: {:.4f}".format(sentences1[i], sentences2[i], cosine_scores[i][i]))
    
#Outputs:
#Το κινητό έπεσε και έσπασε. 		 H πτώση κατέστρεψε τη συσκευή. 		 Score: 0.6741
#Το κινητό έπεσε και έσπασε. 		 Το αυτοκίνητο έσπασε στα δυο. 		 Score: 0.5067
#Το κινητό έπεσε και έσπασε. 		 Ο υπουργός έπεσε και έσπασε το πόδι του. 		 Score: 0.4548

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
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('{MODEL_NAME}')
model = AutoModel.from_pretrained(

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

#### Similarity Evaluation on STS.en-el.txt (translated manually for evaluation purposes)
We measure the semantic textual similarity (STS) between sentence pairs in different languages:

| cosine_pearson | cosine_spearman | euclidean_pearson | euclidean_spearman | manhattan_pearson | manhattan_spearman | dot_pearson | dot_spearman |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
0.834474802920369 | 0.845687403828107 | 0.815895882192263 | 0.81084300966291 | 0.816333562677654 | 0.813879742416394 | 0.7945167996031 | 0.802604238383742 |

#### Translation
We measure the translation accuracy. Given a list with source sentences, for example, 1000 English sentences. And a list with matching target (translated) sentences, for example, 1000 Greek sentences. For each sentence pair, we check if their embeddings are the closest using cosine similarity. I.e., for each src_sentences[i] we check if trg_sentences[i] has the highest similarity out of all target sentences. If this is the case, we have a hit, otherwise an error. This evaluator reports accuracy (higher = better).

| src2trg | trg2src |
| ----------- | ----------- |
| 0.981 |	0.9775 | 

## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 135121 with parameters:
```
{'batch_size': 16, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.MSELoss.MSELoss` 

Parameters of the fit()-Method:
```
{
    "callback": null,
    "epochs": 4,
    "evaluation_steps": 1000,
    "evaluator": "sentence_transformers.evaluation.SequentialEvaluator.SequentialEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'transformers.optimization.AdamW'>",
    "optimizer_params": {
        "correct_bias": false,
        "eps": 1e-06,
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 10000,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 400, 'do_lower_case': False}) with Transformer model: XLMRobertaModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Acknowledgement
The research work was supported by the Hellenic Foundation for Research and Innovation (HFRI) under the HFRI PhD Fellowship grant (Fellowship Number:50, 2nd call)



## Citing & Authors
Citation info for Greek model: TBD

Based on the transfer learning approach of [Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation](https://arxiv.org/abs/2004.09813)
