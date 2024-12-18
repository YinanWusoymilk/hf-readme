---
language: en
license: cc-by-4.0
datasets:
- squad_v2
model-index:
- name: deepset/tinyroberta-squad2
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad_v2
      type: squad_v2
      config: squad_v2
      split: validation
    metrics:
    - type: exact_match
      value: 78.8627
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDNlZDU4ODAxMzY5NGFiMTMyZmQ1M2ZhZjMyODA1NmFlOGMxNzYxNTA4OGE5YTBkZWViZjBkNGQ2ZmMxZjVlMCIsInZlcnNpb24iOjF9.Wgu599r6TvgMLTrHlLMVAbUtKD_3b70iJ5QSeDQ-bRfUsVk6Sz9OsJCp47riHJVlmSYzcDj_z_3jTcUjCFFXBg
    - type: f1
      value: 82.0355
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTFkMzEzMWNiZDRhMGZlODhkYzcwZTZiMDFjZDg2YjllZmUzYWM5NTgwNGQ2NGYyMDk2ZGQwN2JmMTE5NTc3YiIsInZlcnNpb24iOjF9.ChgaYpuRHd5WeDFjtiAHUyczxtoOD_M5WR8834jtbf7wXhdGOnZKdZ1KclmhoI5NuAGc1NptX-G0zQ5FTHEcBA
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad
      type: squad
      config: plain_text
      split: validation
    metrics:
    - type: exact_match
      value: 83.860
      name: Exact Match
    - type: f1
      value: 90.752
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: adversarial_qa
      type: adversarial_qa
      config: adversarialQA
      split: validation
    metrics:
    - type: exact_match
      value: 25.967
      name: Exact Match
    - type: f1
      value: 37.006
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad_adversarial
      type: squad_adversarial
      config: AddOneSent
      split: validation
    metrics:
    - type: exact_match
      value: 76.329
      name: Exact Match
    - type: f1
      value: 83.292
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squadshifts amazon
      type: squadshifts
      config: amazon
      split: test
    metrics:
    - type: exact_match
      value: 63.915
      name: Exact Match
    - type: f1
      value: 78.395
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squadshifts new_wiki
      type: squadshifts
      config: new_wiki
      split: test
    metrics:
    - type: exact_match
      value: 80.297
      name: Exact Match
    - type: f1
      value: 89.808
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squadshifts nyt
      type: squadshifts
      config: nyt
      split: test
    metrics:
    - type: exact_match
      value: 80.149
      name: Exact Match
    - type: f1
      value: 88.321
      name: F1
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squadshifts reddit
      type: squadshifts
      config: reddit
      split: test
    metrics:
    - type: exact_match
      value: 66.959
      name: Exact Match
    - type: f1
      value: 79.300
      name: F1
---

# tinyroberta for Extractive QA

This is the *distilled* version of the [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2) model. This model has a comparable prediction quality and runs at twice the speed of the base model.

## Overview
**Language model:** tinyroberta-squad2  
**Language:** English  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0  
**Eval data:** SQuAD 2.0  
**Code:**  See [an example extractive QA pipeline built with Haystack](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline)  
**Infrastructure**: 4x Tesla v100

## Hyperparameters

```
batch_size = 96
n_epochs = 4
base_LM_model = "deepset/tinyroberta-squad2-step1"
max_seq_len = 384
learning_rate = 3e-5
lr_schedule = LinearWarmup
warmup_proportion = 0.2
doc_stride = 128
max_query_length = 64
distillation_loss_weight = 0.75
temperature = 1.5
teacher = "deepset/robert-large-squad2"
``` 

## Distillation
This model was distilled using the TinyBERT approach described in [this paper](https://arxiv.org/pdf/1909.10351.pdf) and implemented in [haystack](https://github.com/deepset-ai/haystack).
Firstly, we have performed intermediate layer distillation with roberta-base as the teacher which resulted in [deepset/tinyroberta-6l-768d](https://huggingface.co/deepset/tinyroberta-6l-768d).
Secondly, we have performed task-specific distillation with [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2) as the teacher for further intermediate layer distillation on an augmented version of SQuADv2 and then with [deepset/roberta-large-squad2](https://huggingface.co/deepset/roberta-large-squad2) as the teacher for prediction layer distillation. 

## Usage

### In Haystack
Haystack is an AI orchestration framework to build customizable, production-ready LLM applications. You can use this model in Haystack to do extractive question answering on documents. 
To load and run the model with [Haystack](https://github.com/deepset-ai/haystack/):
```python
# After running pip install haystack-ai "transformers[torch,sentencepiece]"

from haystack import Document
from haystack.components.readers import ExtractiveReader

docs = [
    Document(content="Python is a popular programming language"),
    Document(content="python ist eine beliebte Programmiersprache"),
]

reader = ExtractiveReader(model="deepset/tinyroberta-squad2")
reader.warm_up()

question = "What is a popular programming language?"
result = reader.run(query=question, documents=docs)
# {'answers': [ExtractedAnswer(query='What is a popular programming language?', score=0.5740374326705933, data='python', document=Document(id=..., content: '...'), context=None, document_offset=ExtractedAnswer.Span(start=0, end=6),...)]}
```
For a complete example with an extractive question answering pipeline that scales over many documents, check out the [corresponding Haystack tutorial](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline).

### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/tinyroberta-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'Why is model conversion important?',
    'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
}
res = nlp(QA_input)

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```

## Performance
Evaluated on the SQuAD 2.0 dev set with the [official eval script](https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/).

```
"exact": 78.69114798281817,
"f1": 81.9198998536977,

"total": 11873,
"HasAns_exact": 76.19770580296895,
"HasAns_f1": 82.66446878592329,
"HasAns_total": 5928,
"NoAns_exact": 81.17746005046257,
"NoAns_f1": 81.17746005046257,
"NoAns_total": 5945
```

## Authors
**Branden Chan:** branden.chan@deepset.ai  
**Timo Möller:** timo.moeller@deepset.ai  
**Malte Pietsch:** malte.pietsch@deepset.ai  
**Tanay Soni:** tanay.soni@deepset.ai  
**Michel Bartels:** michel.bartels@deepset.ai

## About us

<div class="grid lg:grid-cols-2 gap-x-4 gap-y-3">
    <div class="w-full h-40 object-cover mb-2 rounded-lg flex items-center justify-center">
         <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/deepset-logo-colored.png" class="w-40"/>
     </div>
     <div class="w-full h-40 object-cover mb-2 rounded-lg flex items-center justify-center">
         <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/haystack-logo-colored.png" class="w-40"/>
     </div>
</div>

[deepset](http://deepset.ai/) is the company behind the production-ready open-source AI framework [Haystack](https://haystack.deepset.ai/).

Some of our other work: 
- [Distilled roberta-base-squad2 (aka "tinyroberta-squad2")](https://huggingface.co/deepset/tinyroberta-squad2)
- [German BERT](https://deepset.ai/german-bert), [GermanQuAD and GermanDPR](https://deepset.ai/germanquad), [German embedding model](https://huggingface.co/mixedbread-ai/deepset-mxbai-embed-de-large-v1)
- [deepset Cloud](https://www.deepset.ai/deepset-cloud-product), [deepset Studio](https://www.deepset.ai/deepset-studio)

## Get in touch and join the Haystack community

<p>For more info on Haystack, visit our <strong><a href="https://github.com/deepset-ai/haystack">GitHub</a></strong> repo and <strong><a href="https://docs.haystack.deepset.ai">Documentation</a></strong>. 

We also have a <strong><a class="h-7" href="https://haystack.deepset.ai/community">Discord community open to everyone!</a></strong></p>

[Twitter](https://twitter.com/Haystack_AI) | [LinkedIn](https://www.linkedin.com/company/deepset-ai/) | [Discord](https://haystack.deepset.ai/community) | [GitHub Discussions](https://github.com/deepset-ai/haystack/discussions) | [Website](https://haystack.deepset.ai/) | [YouTube](https://www.youtube.com/@deepset_ai)

By the way: [we're hiring!](http://www.deepset.ai/jobs)