---
license: apache-2.0
base_model: distilbert-base-cased
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: distilbert-NER
  results: []
datasets:
- conll2003
language:
- en
pipeline_tag: token-classification
---
# distilbert-NER

If my open source models have been useful to you, please consider supporting me in building small, useful AI models for everyone (and help me afford med school / help out my parents financially). Thanks!

<a href="https://www.buymeacoffee.com/dslim" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## Model description

**distilbert-NER** is the fine-tuned version of **DistilBERT**, which is a distilled variant of the BERT model. DistilBERT has fewer parameters than BERT, making it smaller, faster, and more efficient. distilbert-NER is specifically fine-tuned for the task of **Named Entity Recognition (NER)**.

This model accurately identifies the same four types of entities as its BERT counterparts: location (LOC), organizations (ORG), person (PER), and Miscellaneous (MISC). Although it is a more compact model, distilbert-NER demonstrates a robust performance in NER tasks, balancing between size, speed, and accuracy.

The model was fine-tuned on the English version of the [CoNLL-2003 Named Entity Recognition](https://www.aclweb.org/anthology/W03-0419.pdf) dataset, which is widely recognized for its comprehensive and diverse range of entity types.

### Available NER models 
| Model Name | Description | Parameters |
|-------------------|-------------|------------------|
| [distilbert-NER](https://huggingface.co/dslim/distilbert-NER) | Fine-tuned DistilBERT - a smaller, faster, lighter version of BERT | 66M |
| [bert-large-NER](https://huggingface.co/dslim/bert-large-NER/) | Fine-tuned bert-large-cased - larger model with slightly better performance | 340M |
| [bert-base-NER](https://huggingface.co/dslim/bert-base-NER)-([uncased](https://huggingface.co/dslim/bert-base-NER-uncased)) | Fine-tuned bert-base, available in both cased and uncased versions | 110M |

## Intended uses & limitations

#### How to use

This model can be utilized with the Transformers *pipeline* for NER, similar to the BERT models.

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("dslim/distilbert-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/distilbert-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "My name is Wolfgang and I live in Berlin"

ner_results = nlp(example)
print(ner_results)
```

#### Limitations and bias

The performance of distilbert-NER is linked to its training on the CoNLL-2003 dataset. Therefore, it might show limited effectiveness on text data that significantly differs from this training set. Users should be aware of potential biases inherent in the training data and the possibility of entity misclassification in complex sentences.


## Training data

This model was fine-tuned on English version of the standard [CoNLL-2003 Named Entity Recognition](https://www.aclweb.org/anthology/W03-0419.pdf) dataset. 

The training dataset distinguishes between the beginning and continuation of an entity so that if there are back-to-back entities of the same type, the model can output where the second entity begins. As in the dataset, each token will be classified as one of the following classes:

Abbreviation|Description
-|-
O|Outside of a named entity
B-MISC |Beginning of a miscellaneous entity right after another miscellaneous entity
I-MISC | Miscellaneous entity
B-PER |Beginning of a person’s name right after another person’s name
I-PER |Person’s name
B-ORG |Beginning of an organization right after another organization
I-ORG |organization
B-LOC |Beginning of a location right after another location
I-LOC |Location


### CoNLL-2003 English Dataset Statistics
This dataset was derived from the Reuters corpus which consists of Reuters news stories. You can read more about how this dataset was created in the CoNLL-2003 paper. 
#### # of training examples per entity type
Dataset|LOC|MISC|ORG|PER
-|-|-|-|-
Train|7140|3438|6321|6600
Dev|1837|922|1341|1842
Test|1668|702|1661|1617
#### # of articles/sentences/tokens per dataset
Dataset |Articles |Sentences |Tokens
-|-|-|-
Train |946 |14,987 |203,621
Dev |216 |3,466 |51,362
Test |231 |3,684 |46,435

## Training procedure

This model was trained on a single NVIDIA V100 GPU with recommended hyperparameters from the [original BERT paper](https://arxiv.org/pdf/1810.04805) which trained & evaluated the model on CoNLL-2003 NER task. 

## Eval results
| Metric     | Score |
|------------|-------|
| Loss       | 0.0710|
| Precision  | 0.9202|
| Recall     | 0.9232|
| F1         | 0.9217|
| Accuracy   | 0.9810|

The training and validation losses demonstrate a decrease over epochs, signaling effective learning. The precision, recall, and F1 scores are competitive, showcasing the model's robustness in NER tasks.

### BibTeX entry and citation info

For DistilBERT:

```
@article{sanh2019distilbert,
  title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
  author={Sanh, Victor and Debut, Lysandre and Chaumond, Julien and Wolf, Thomas},
  journal={arXiv preprint arXiv:1910.01108},
  year={2019}
}
```

For the underlying BERT model:

```
@article{DBLP:journals/corr/abs-1810-04805,
  author    = {Jacob Devlin and
               Ming{-}Wei Chang and
               Kenton Lee and
               Kristina Toutanova},
  title     = {{BERT:} Pre-training of Deep Bidirectional Transformers for Language
               Understanding},
  journal   = {CoRR},
  volume    = {abs/1810.04805},
  year      = {2018},
  url       = {http://arxiv.org/abs/1810.04805},
  archivePrefix = {arXiv},
  eprint    = {1810.04805},
  timestamp = {Tue, 30 Oct 2018 20:39:56 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1810-04805.bib},
  bibsource = {db

lp computer science bibliography, https://dblp.org}
}
```