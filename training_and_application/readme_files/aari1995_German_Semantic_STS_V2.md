---
pipeline_tag: sentence-similarity
language:
- de
datasets:
- stsb_multi_mt
tags:
- gBERT-large
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- RAG
- retrieval augmented generation
- STS
- MTEB
- mteb

model-index:
- name: German_Semantic_STS_V2
  results:
  - dataset:
      config: de
      name: MTEB AmazonCounterfactualClassification
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 67.00214132762312
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB AmazonCounterfactualClassification
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: validation
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 68.43347639484978
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB AmazonReviewsClassification
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 39.092
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB AmazonReviewsClassification
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: validation
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 39.146000000000003
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BlurbsClusteringP2P
      revision: a2dd5b02a77de3466a3eaa98ae586b5610314496
      split: test
      type: slvnwhrl/blurbs-clustering-p2p
    metrics:
    - type: v_measure
      value: 38.680981669842135
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BlurbsClusteringS2S
      revision: 22793b6a6465bf00120ad525e38c51210858132c
      split: test
      type: slvnwhrl/blurbs-clustering-s2s
    metrics:
    - type: v_measure
      value: 17.624489937027504
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB GermanDPR
      revision: 5129d02422a66be600ac89cd3e8531b4f97d347d
      split: test
      type: deepset/germandpr
    metrics:
    - type: ndcg_at_10
      value: 72.921
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB GermanQuAD-Retrieval
      revision: f5c87ae5a2e7a5106606314eef45255f03151bb3
      split: test
      type: mteb/germanquad-retrieval
    metrics:
    - type: mrr_at_5
      value: 85.316
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB GermanSTSBenchmark
      revision: e36907544d44c3a247898ed81540310442329e20
      split: test
      type: jinaai/german-STSbenchmark
    metrics:
    - type: cos_sim_spearman
      value: 84.67696933608695
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB GermanSTSBenchmark
      revision: e36907544d44c3a247898ed81540310442329e20
      split: validation
      type: jinaai/german-STSbenchmark
    metrics:
    - type: cos_sim_spearman
      value: 88.048957974805
    task:
      type: STS
  - dataset:
      config: de
      name: MTEB MassiveIntentClassification
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 66.25084061869536
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB MassiveIntentClassification
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 66.44859813084113
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB MassiveScenarioClassification
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 72.51176866173503
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB MassiveScenarioClassification
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 72.02164289227742
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB MTOPDomainClassification
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: test
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 89.00253592561285
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB MTOPDomainClassification
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: validation
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 87.70798898071626
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB MTOPIntentClassification
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: test
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 70.06198929275853
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB MTOPIntentClassification
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: validation
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 68.6060606060606
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB PawsX
      revision: 8a04d940a42cd40658986fdd8e3da561533a3646
      split: test
      type: google-research-datasets/paws-x
    metrics:
    - type: ap
      value: 57.47670853851811
    task:
      type: PairClassification
  - dataset:
      config: de
      name: MTEB PawsX
      revision: 8a04d940a42cd40658986fdd8e3da561533a3646
      split: validation
      type: google-research-datasets/paws-x
    metrics:
    - type: ap
      value: 52.85587710877178
    task:
      type: PairClassification
  - dataset:
      config: de
      name: MTEB STS22
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cos_sim_spearman
      value: 50.63839763951755
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB TenKGnadClusteringP2P
      revision: 5c59e41555244b7e45c9a6be2d720ab4bafae558
      split: test
      type: slvnwhrl/tenkgnad-clustering-p2p
    metrics:
    - type: v_measure
      value: 37.996685796529817
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB TenKGnadClusteringS2S
      revision: 6cddbe003f12b9b140aec477b583ac4191f01786
      split: test
      type: slvnwhrl/tenkgnad-clustering-s2s
    metrics:
    - type: v_measure
      value: 23.71145428041516
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB FalseFriendsGermanEnglish
      revision: 15d6c030d3336cbb09de97b2cefc46db93262d40
      split: test
      type: aari1995/false_friends_de_en_mteb
    metrics:
    - type: ap
      value: 71.22096746794873
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB GermanSTSBenchmark
      revision: e36907544d44c3a247898ed81540310442329e20
      split: test
      type: jinaai/german-STSbenchmark
    metrics:
    - type: cos_sim_spearman
      value: 84.67698604065061
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB GermanSTSBenchmark
      revision: e36907544d44c3a247898ed81540310442329e20
      split: validation
      type: jinaai/german-STSbenchmark
    metrics:
    - type: cos_sim_spearman
      value: 88.048957974805
    task:
      type: STS
---

# German_Semantic_STS_V2

**Note:** Check out my new, updated models: [German_Semantic_V3](https://huggingface.co/aari1995/German_Semantic_V3) and [V3b](https://huggingface.co/aari1995/German_Semantic_V3b)!

This model creates german embeddings for semantic use cases.

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 1024 dimensional dense vector space and can be used for tasks like clustering or semantic search.

Special thanks to [deepset](https://huggingface.co/deepset/) for providing the model gBERT-large and also to [Philip May](https://huggingface.co/philipMay) for the Translation of the dataset and chats about the topic.

Model score after fine-tuning scores best, compared to these models:

| Model Name                                                    | Spearman |
|---------------------------------------------------------------|-------------------|
| xlm-r-distilroberta-base-paraphrase-v1                        | 0.8079            |
| [xlm-r-100langs-bert-base-nli-stsb-mean-tokens](https://huggingface.co/sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens)                 | 0.7877            |
| xlm-r-bert-base-nli-stsb-mean-tokens                          | 0.7877            |
| [roberta-large-nli-stsb-mean-tokens](https://huggingface.co/sentence-transformers/roberta-large-nli-stsb-mean-tokens)                            | 0.6371            |
| [T-Systems-onsite/<br/>german-roberta-sentence-transformer-v2](https://huggingface.co/T-Systems-onsite/german-roberta-sentence-transformer-v2)       | 0.8529            |
| [paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2) | 0.8355 |
| [T-Systems-onsite/<br/>cross-en-de-roberta-sentence-transformer](https://huggingface.co/T-Systems-onsite/<br/>cross-en-de-roberta-sentence-transformer) | 0.8550        |
| **aari1995/German_Semantic_STS_V2** | **0.8626**        |



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

model = SentenceTransformer('aari1995/German_Semantic_STS_V2')
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
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('aari1995/German_Semantic_STS_V2')
model = AutoModel.from_pretrained('aari1995/German_Semantic_STS_V2')

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

<!--- Describe how your model was evaluated -->

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name={MODEL_NAME})


## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 1438 with parameters:
```
{'batch_size': 4, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.ContrastiveLoss.ContrastiveLoss` with parameters:
  ```
  {'distance_metric': 'SiameseDistanceMetric.COSINE_DISTANCE', 'margin': 0.5, 'size_average': True}
  ```

Parameters of the fit()-Method:
```
{
    "epochs": 4,
    "evaluation_steps": 500,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'torch.optim.adamw.AdamW'>",
    "optimizer_params": {
        "lr": 5e-06
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 576,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->
The base model is trained by deepset.
The dataset was published / translated by Philip May.
The model was fine-tuned by Aaron Chibb.