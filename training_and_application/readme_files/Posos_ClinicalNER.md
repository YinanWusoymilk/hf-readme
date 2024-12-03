---
license: cc-by-nc-sa-4.0
datasets:
- Posos/MedNERF
metrics:
- f1
tags:
- medical
widget:
- text: take two pills every morning during one week
- text: xeplion 50mg 2 fois par jour
- text: doliprane 500 1 comprimé effervescent le matin pendant une semaine
- text: >-
    Der Patient sollte zehn Tage lang während dem Frühstück eine
    Paracetamol-Tablette einnehmen
- text: una cápsula por la mañana y por la noche
model-index:
- name: Posos/ClinicalNER
  results:
  - task:
      type: token-classification
      name: Clinical NER
    dataset:
      type: Posos/MedNERF
      name: MedNERF
      split: test
    metrics:
    - type: f1
      value: 0.804
      name: micro-F1 score
    - type: precision
      value: 0.817
      name: precision
    - type: recall
      value: 0.791
      name: recall
    - type: accuracy
      value: 0.859
      name: accuracy
language:
- fr
- en
- de
- multilingual
- es
- it
---

# ClinicalNER

## Model Description

This is a multilingual clinical NER model extracting DRUG, STRENGTH, FREQUENCY, DURATION, DOSAGE and FORM entities from a medical text.

It consist of XLM-R Base fine-tuned on n2c2 (English). It is the model that obtains the best results on our French evaluation test set [MedNERF](https://huggingface.co/datasets/Posos/MedNERF) in a zero-shot cross-lingual transfer setting.

## Evaluation Metrics on [MedNERF dataset](https://huggingface.co/datasets/Posos/MedNERF)

- Loss: 0.692
- Accuracy: 0.859
- Precision: 0.817
- Recall: 0.791
- micro-F1: 0.804
- macro-F1: 0.819

## Usage

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("Posos/ClinicalNER")
tokenizer = AutoTokenizer.from_pretrained("Posos/ClinicalNER")

inputs = tokenizer("Take 2 pills every morning", return_tensors="pt")
outputs = model(**inputs)
```

## Citation information

```
@inproceedings{mednerf,
    title = "Multilingual Clinical NER: Translation or Cross-lingual Transfer?",
    author = "Gaschi, Félix and Fontaine, Xavier and Rastin, Parisa and Toussaint, Yannick",
    booktitle = "Proceedings of the 5th Clinical Natural Language Processing Workshop",
    publisher = "Association for Computational Linguistics",
    year = "2023"
}
```