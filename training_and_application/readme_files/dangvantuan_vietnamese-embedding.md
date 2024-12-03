---
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- phobert
- vietnamese
- sentence-embedding
license: apache-2.0
language:
- vi
metrics:
- pearsonr
- spearmanr
---
## Model Description:
[**vietnamese-embedding**](https://huggingface.co/dangvantuan/vietnamese-embedding) is the Embedding Model for Vietnamese language. This model is a specialized sentence-embedding trained specifically for the Vietnamese language, leveraging the robust capabilities of PhoBERT, a pre-trained language model based on the RoBERTa architecture.
The model utilizes PhoBERT to encode Vietnamese sentences into a 768-dimensional vector space, facilitating a wide range of applications from semantic search to text clustering. The embeddings capture the nuanced meanings of Vietnamese sentences, reflecting both the lexical and contextual layers of the language.

## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: RobertaModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```
## Training and Fine-tuning process
The model underwent a rigorous four-stage training and fine-tuning process, each tailored to enhance its ability to generate precise and contextually relevant sentence embeddings for the Vietnamese language. Below is an outline of these stages:
#### Stage 1: Initial Training
- Dataset: [ViNLI-SimCSE-supervised](https://huggingface.co/datasets/anti-ai/ViNLI-SimCSE-supervised)
- Method: Trained using the [SimCSE approach](https://arxiv.org/abs/2104.08821) which employs a supervised contrastive learning framework. The model was optimized using [Triplet Loss](https://www.sbert.net/docs/package_reference/losses.html#tripletloss) to effectively learn from high-quality annotated sentence pairs.
#### Stage 2: Continued Fine-tuning
- Dataset: [XNLI-vn ](https://huggingface.co/datasets/xnli/viewer/vi)
- Method: Continued fine-tuning using Multi-Negative Ranking Loss. This stage focused on improving the model's ability to discern and rank nuanced differences in sentence semantics.
### Stage 3: Continued Fine-tuning for Semantic Textual Similarity on STS Benchmark
- Dataset: [STSB-vn](https://huggingface.co/datasets/doanhieung/vi-stsbenchmark)
- Method: Fine-tuning specifically for the semantic textual similarity benchmark using Siamese BERT-Networks configured with the 'sentence-transformers' library. This stage honed the model's precision in capturing semantic similarity across various types of Vietnamese texts.
### Stage 4: Advanced Augmentation Fine-tuning
- Dataset: STSB-vn with generate [silver sample from gold sample](https://www.sbert.net/examples/training/data_augmentation/README.html)
- Method: Employed an advanced strategy using [Augmented SBERT](https://arxiv.org/abs/2010.08240) with Pair Sampling Strategies, integrating both Cross-Encoder and Bi-Encoder models. This stage further refined the embeddings by enriching the training data dynamically, enhancing the model's robustness and accuracy in understanding and processing complex Vietnamese language constructs.


## Usage:

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
pip install -q pyvi
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
from pyvi.ViTokenizer import tokenize

sentences = ["Hà Nội là thủ đô của Việt Nam", "Đà Nẵng là thành phố du lịch"]
tokenizer_sent = [tokenize(sent) for sent in sentences]

model = SentenceTransformer('dangvantuan/vietnamese-embedding')
embeddings = model.encode(tokenizer_sent)
print(embeddings)

```


## Evaluation
The model can be evaluated as follows on the [Vienamese data of stsb](https://huggingface.co/datasets/doanhieung/vi-stsbenchmark).

```python
from sentence_transformers import SentenceTransformer
from sentence_transformers import SentenceTransformer
from sentence_transformers.readers import InputExample
from datasets import load_dataset
from pyvi.ViTokenizer import tokenize
def convert_dataset(dataset):
    dataset_samples=[]
    for df in dataset:
        score = float(df['score'])/5.0  # Normalize score to range 0 ... 1
        inp_example = InputExample(texts=[tokenize(df['sentence1']), 
                                    tokenize(df['sentence2'])], label=score)
        dataset_samples.append(inp_example)
    return dataset_samples

# Loading the dataset for evaluation
vi_sts = load_dataset("doanhieung/vi-stsbenchmark")["train"]
df_dev = vi_sts.filter(lambda example: example['split'] == 'dev')
df_test = vi_sts.filter(lambda example: example['split'] == 'test')

# Convert the dataset for evaluation

# For Dev set:
dev_samples = convert_dataset(df_dev)
val_evaluator = EmbeddingSimilarityEvaluator.from_input_examples(dev_samples, name='sts-dev')
val_evaluator(model, output_path="./")

# For Test set:
test_samples = convert_dataset(df_test)
test_evaluator = EmbeddingSimilarityEvaluator.from_input_examples(test_samples, name='sts-test')
test_evaluator(model, output_path="./")
```


### Test Result:
The performance is measured using Pearson and Spearman correlation:
- On dev
| Model  | Pearson correlation | Spearman correlation  | #params  |
| ------------- | ------------- | ------------- |------------- |
| [dangvantuan/vietnamese-embedding](dangvantuan/vietnamese-embedding)| 88.33 |88.20 | 135M| 
| [VoVanPhuc/sup-SimCSE-VietNamese-phobert-base](https://huggingface.co/VoVanPhuc/sup-SimCSE-VietNamese-phobert-base)  | 84.65|84.59 | 135M |
| [keepitreal/vietnamese-sbert](https://huggingface.co/keepitreal/vietnamese-sbert) | 84.51 | 84.44|135M |
| [bkai-foundation-models/vietnamese-bi-encoder](https://huggingface.co/bkai-foundation-models/vietnamese-bi-encoder) | 78.05 | 77.94|135M |

### Metric for all dataset of [Semantic Textual Similarity on STS Benchmark](https://huggingface.co/datasets/anti-ai/ViSTS)
You can run an evaluation on this [Colab](https://colab.research.google.com/drive/1JZLWKiknSUnA92UY2RIhvS65WtP6sgqW?hl=fr#scrollTo=IkTAwPqxDTOK)

**Pearson score**
| Model                                                                                                               | [STSB]   | [STS12]| [STS13] | [STS14] | [STS15] |    [STS16] | [SICK] | Mean |
|-----------------------------------------------------------|---------|----------|----------|----------|----------|----------|---------|--------|
| [dangvantuan/vietnamese-embedding](dangvantuan/vietnamese-embedding)                                                 |**84.87**	|**87.23**|	**85.39**|	**82.94**|	**86.91**|	**79.39**|	**82.77**|	**84.21**|
| [VoVanPhuc/sup-SimCSE-VietNamese-phobert-base](https://huggingface.co/VoVanPhuc/sup-SimCSE-VietNamese-phobert-base)  |81.52|	85.02|	78.22|	75.94|	81.53|	75.39|	77.75|	79.33|
| [keepitreal/vietnamese-sbert](https://huggingface.co/keepitreal/vietnamese-sbert)                                    |80.54|	78.58|	80.75|	76.98|	82.57|	73.21|	80.16|	78.97|
| [bkai-foundation-models/vietnamese-bi-encoder](https://huggingface.co/bkai-foundation-models/vietnamese-bi-encoder)  |73.30|	67.84|	71.69|	69.80|	78.40|	74.29|	76.01|	73.04|


**Spearman score**
| Model                                                                                                               | [STSB]   | [STS12]| [STS13] | [STS14] | [STS15] |    [STS16] | [SICK] | Mean |
|-----------------------------------------------------------|---------|----------|----------|----------|----------|----------|---------|--------|
| [dangvantuan/vietnamese-embedding](dangvantuan/vietnamese-embedding)                                                 |**84.84**|	**79.04**|	**85.30**|	**81.38**|	**87.06**|	**79.95**|	**79.58**|	**82.45**|
| [VoVanPhuc/sup-SimCSE-VietNamese-phobert-base](https://huggingface.co/VoVanPhuc/sup-SimCSE-VietNamese-phobert-base)  |81.43|	76.51|	79.19|	74.91|	81.72|	76.57|	76.45|	78.11|
| [keepitreal/vietnamese-sbert](https://huggingface.co/keepitreal/vietnamese-sbert)                                    |80.16|	69.08|	80.99|	73.67|	82.81|	74.30|	73.40|	76.34|
| [bkai-foundation-models/vietnamese-bi-encoder](https://huggingface.co/bkai-foundation-models/vietnamese-bi-encoder)  |72.16|	63.86|	71.82|	66.20|	78.62|	74.24|	70.87|	71.11|

## Citation


	@article{reimers2019sentence,
	   title={Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks},
	   author={Nils Reimers, Iryna Gurevych},
	   journal={https://arxiv.org/abs/1908.10084},
	   year={2019}
	}


	@article{martin2020camembert,
	   title={CamemBERT: a Tasty French Language Mode},
	   author={Martin, Louis and Muller, Benjamin and Su{\'a}rez, Pedro Javier Ortiz and Dupont, Yoann and Romary, Laurent and de la Clergerie, {\'E}ric Villemonte and Seddah, Djam{\'e} and Sagot, Beno{\^\i}t},
	   journal={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
	   year={2020}
	}
    @article{thakur2020augmented,
      title={Augmented SBERT: Data Augmentation Method for Improving Bi-Encoders for Pairwise Sentence Scoring Tasks},
      author={Thakur, Nandan and Reimers, Nils and Daxenberger, Johannes and Gurevych, Iryna},
      journal={arXiv e-prints},
      pages={arXiv--2010},
      year={2020}