---
language: en
license: cc-by-4.0
datasets:
- squad_v2
model-index:
- name: deepset/bert-large-uncased-whole-word-masking-squad2
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
      value: 80.8846
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2E5ZGNkY2ExZWViZGEwNWE3OGRmMWM2ZmE4ZDU4ZDQ1OGM3ZWE0NTVmZjFmYmZjZmJmNjJmYTc3NTM3OTk3OSIsInZlcnNpb24iOjF9.aSblF4ywh1fnHHrN6UGL392R5KLaH3FCKQlpiXo_EdQ4XXEAENUCjYm9HWDiFsgfSENL35GkbSyz_GAhnefsAQ
    - type: f1
      value: 83.8765
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGFlNmEzMTk2NjRkNTI3ZTk3ZTU1NWNlYzIyN2E0ZDFlNDA2ZjYwZWJlNThkMmRmMmE0YzcwYjIyZDM5NmRiMCIsInZlcnNpb24iOjF9.-rc2_Bsp_B26-o12MFYuAU0Ad2Hg9PDx7Preuk27WlhYJDeKeEr32CW8LLANQABR3Mhw2x8uTYkEUrSDMxxLBw
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
      value: 85.904
      name: Exact Match
    - type: f1
      value: 92.586
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
      value: 28.233
      name: Exact Match
    - type: f1
      value: 41.170
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
      value: 78.064
      name: Exact Match
    - type: f1
      value: 83.591
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
      value: 65.615
      name: Exact Match
    - type: f1
      value: 80.733
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
      value: 81.570
      name: Exact Match
    - type: f1
      value: 91.199
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
      value: 83.279
      name: Exact Match
    - type: f1
      value: 91.090
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
      value: 69.305
      name: Exact Match
    - type: f1
      value: 82.405
      name: F1
---

# bert-large-uncased-whole-word-masking-squad2 for Extractive QA

This is a berta-large model, fine-tuned using the SQuAD2.0 dataset for the task of question answering.

## Overview
**Language model:** bert-large  
**Language:** English  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0  
**Eval data:** SQuAD 2.0  
**Code:**  See [an example extractive QA pipeline built with Haystack](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline)  

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

reader = ExtractiveReader(model="deepset/bert-large-uncased-whole-word-masking-squad2")
reader.warm_up()

question = "What is a popular programming language?"
result = reader.run(query=question, documents=docs)
# {'answers': [ExtractedAnswer(query='What is a popular programming language?', score=0.5740374326705933, data='python', document=Document(id=..., content: '...'), context=None, document_offset=ExtractedAnswer.Span(start=0, end=6),...)]}
```
For a complete example with an extractive question answering pipeline that scales over many documents, check out the [corresponding Haystack tutorial](https://haystack.deepset.ai/tutorials/34_extractive_qa_pipeline).

### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/bert-large-uncased-whole-word-masking-squad2"

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