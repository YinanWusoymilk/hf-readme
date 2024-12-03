---
language: en
pipeline_tag: fill-mask
tags: 
- legal
license: mit
---

###  InLegalBERT
Model and tokenizer files for the InLegalBERT model from the paper [Pre-training Transformers on Indian Legal Text](https://arxiv.org/abs/2209.06049).

### Training Data
For building the pre-training corpus of Indian legal text, we collected a large corpus of case documents from the Indian Supreme Court and many High Courts of India.
The court cases in our dataset range from 1950 to 2019, and belong to all legal domains, such as Civil, Criminal, Constitutional, and so on.
In total, our dataset contains around 5.4 million Indian legal documents (all in the English language). 
The raw text corpus size is around 27 GB.

### Training Setup
This model is initialized with the [LEGAL-BERT-SC model](https://huggingface.co/nlpaueb/legal-bert-base-uncased) from the paper [LEGAL-BERT: The Muppets straight out of Law School](https://aclanthology.org/2020.findings-emnlp.261/). In our work, we refer to this model as LegalBERT, and our re-trained model as InLegalBERT.
We further train this model on our data for 300K steps on the Masked Language Modeling (MLM) and Next Sentence Prediction (NSP) tasks.

### Model Overview
This model uses the same tokenizer as [LegalBERT](https://huggingface.co/nlpaueb/legal-bert-base-uncased).
This model has the same configuration as the [bert-base-uncased model](https://huggingface.co/bert-base-uncased):
12 hidden layers, 768 hidden dimensionality, 12 attention heads, ~110M parameters.

### Usage
Using the model to get embeddings/representations for a piece of text
```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("law-ai/InLegalBERT")
text = "Replace this string with yours"
encoded_input = tokenizer(text, return_tensors="pt")
model = AutoModel.from_pretrained("law-ai/InLegalBERT")
output = model(**encoded_input)
last_hidden_state = output.last_hidden_state
```

### Fine-tuning Results
We have fine-tuned all pre-trained models on 3 legal tasks with Indian datasets:
* Legal Statute Identification ([ILSI Dataset](https://arxiv.org/abs/2112.14731))[Multi-label Text Classification]: Identifying relevant statutes (law articles) based on the facts of a court case
* Semantic Segmentation ([ISS Dataset](https://arxiv.org/abs/1911.05405))[Sentence Tagging]: Segmenting the document into 7 functional parts (semantic segments) such as Facts, Arguments, etc.
* Court Judgment Prediction ([ILDC Dataset](https://arxiv.org/abs/2105.13562))[Binary Text Classification]: Predicting whether the claims/petitions of a court case will be accepted/rejected

InLegalBERT beats LegalBERT as well as all other baselines/variants we have used, across all three tasks. For details, see our [paper](https://arxiv.org/abs/2209.06049).

### Citation
```
@inproceedings{paul-2022-pretraining,
  url = {https://arxiv.org/abs/2209.06049},
  author = {Paul, Shounak and Mandal, Arpan and Goyal, Pawan and Ghosh, Saptarshi},
  title = {Pre-trained Language Models for the Legal Domain: A Case Study on Indian Law},
  booktitle = {Proceedings of 19th International Conference on Artificial Intelligence and Law - ICAIL 2023}
  year = {2023},
}
```

### About Us
We are a group of researchers from the Department of Computer Science and Technology, Indian Insitute of Technology, Kharagpur. 
Our research interests are primarily ML and NLP applications for the legal domain, with a special focus on the challenges and oppurtunites for the Indian legal scenario. 
We have, and are currently working on several legal tasks such as:
* named entity recognition, summarization of legal documents
* semantic segmentation of legal documents
* legal statute identification from facts, court judgment prediction
* legal document matching

You can find our publicly available codes and datasets [here](https://github.com/Law-AI). 