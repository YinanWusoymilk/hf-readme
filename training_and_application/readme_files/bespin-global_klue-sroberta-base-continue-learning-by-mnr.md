---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
datasets:
- klue
language:
- ko
license: cc-by-4.0
---

# bespin-global/klue-sroberta-base-continue-learning-by-mnr

해당 모델은 KLUE/NLI, KLUE/STS 데이터셋을 활용하였으며, sentence-transformers의 공식 문서 내 소개된 [continue-learning](https://github.com/UKPLab/sentence-transformers/blob/master/examples/training/sts/training_stsbenchmark_continue_training.py) 방법을 통해 아래와 같이 학습되었습니다.
1. NLI 데이터셋을 통해 nagative sampling 후, MultipleNegativeRankingLoss를 활용하여 1차 NLI training 수행
2. 1에서 학습완료 된 모델에 STS 데이터셋을 통해, CosineSimilarityLoss를 활용하여 2차 STS training 수행

학습에 관한 자세한 내용은 [Blog](https://velog.io/@jaehyeong/Basic-NLP-sentence-transformers-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-SBERT-%ED%95%99%EC%8A%B5-%EB%B0%A9%EB%B2%95#225-continue-learning-by-sts)와 [Colab 실습 코드](https://colab.research.google.com/drive/1uDt3o_Nv2cTiVbIAIUkst_eOSD37Wkmf)를 참고해주세요.

---
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
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer("bespin-global/klue-sroberta-base-continue-learning-by-mnr")
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
tokenizer = AutoTokenizer.from_pretrained("bespin-global/klue-sroberta-base-continue-learning-by-mnr")
model = AutoModel.from_pretrained("bespin-global/klue-sroberta-base-continue-learning-by-mnr")

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

**EmbeddingSimilarityEvaluator: Evaluating the model on sts-test dataset:**
- Cosine-Similarity :
	- Pearson: 0.8901	Spearman: 0.8893
- Manhattan-Distance:
	- Pearson: 0.8867	Spearman: 0.8818
- Euclidean-Distance:
	- Pearson: 0.8875	Spearman: 0.8827
- Dot-Product-Similarity:
	- Pearson: 0.8786	Spearman: 0.8735
- Average : 0.8892573547643868


## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 329 with parameters:
```
{'batch_size': 32, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.CosineSimilarityLoss.CosineSimilarityLoss` 

Parameters of the fit()-Method:
```
{
    "epochs": 4,
    "evaluation_steps": 32,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'transformers.optimization.AdamW'>",
    "optimizer_params": {
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 132,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': True}) with Transformer model: RobertaModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->
[JaeHyeong AN](https://huggingface.co/Copycats) at [Bespin Global](https://www.bespinglobal.com/)