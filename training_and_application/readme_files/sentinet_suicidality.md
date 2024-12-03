---
license: cc0-1.0
language:
- en
metrics:
- accuracy: 0.939432
- recall: 0.937164
- precision: 0.92822
- f1: 0.92822
tags:
- classification
- suicidality
- suicidal text detection
- suicidal sentiment
- sentiment
- suicide
- self harm
- depression
pipeline_tag: text-classification
---


# Advanced Suicidality Classifier Model

## Introduction

Welcome to the Suicidality Detection AI Model! This project aims to provide a machine learning solution for detecting sequences of words indicative of suicidality in text. By utilizing the ELECTRA architecture and fine-tuning on a diverse dataset, we have created a powerful classification model that can distinguish between suicidal and non-suicidal text expressions.


## Labels

The model classifies input text into two labels:

- `LABEL_0`: Indicates that the text is non-suicidal.
- `LABEL_1`: Indicates that the text is indicative of suicidality.


## Training

The model was fine-tuned using the ELECTRA architecture on a carefully curated dataset. Our training process involved cleaning and preprocessing various text sources to create a comprehensive training set. The training results indicate promising performance, with metrics including:

## Performance

The model's performance on the validation dataset is as follows:

- Accuracy: 0.939432
- Recall: 0.937164
- Precision: 0.92822
- F1 Score: 0.932672

These metrics demonstrate the model's ability to accurately classify sequences of text as either indicative of suicidality or non-suicidal.



## Data Sources

We collected data from multiple sources to create a rich and diverse training dataset:

- https://www.kaggle.com/datasets/thedevastator/c-ssrs-labeled-suicidality-in-500-anonymized-red
- https://www.kaggle.com/datasets/amangoyl/reddit-dataset-for-multi-task-nlp
- https://www.kaggle.com/datasets/imeshsonu/suicideal-phrases
- https://raw.githubusercontent.com/laxmimerit/twitter-suicidal-intention-dataset/master/twitter-suicidal_data.csv
- https://www.kaggle.com/datasets/mohanedmashaly/suicide-notes
- https://www.kaggle.com/datasets/natalialech/suicidal-ideation-on-twitter

The data underwent thorough cleaning and preprocessing before being used for training the model.

## How to Use

### Installation

To use the model, you need to install the Transformers library:

```bash
pip install transformers
```

### Using the Model

You can utilize the model for text classification using the following code snippets:

1. Using the pipeline approach:

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="sentinetyd/suicidality")

result = classifier("text to classify")
print(result)
```

2. Using the tokenizer and model programmatically:

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("sentinetyd/suicidality")
model = AutoModel.from_pretrained("sentinetyd/suicidality")

# Perform tokenization and prediction using the tokenizer and model
```

## Ethical Considerations
Suicidality is a sensitive and serious topic. It's important to exercise caution and consider ethical implications when using this model. Predictions made by the model should be handled with care and used to complement human judgment and intervention.


## Model Credits

We would like to acknowledge the "gooohjy/suicidal-electra" model available on Hugging Face's model repository. You can find the model at [this link](https://huggingface.co/gooohjy/suicidal-electra). We used this model as a starting point and fine-tuned it to create our specialized suicidality detection model.


## Contributions
We welcome contributions and feedback from the community to further improve the model's performance, enhance the dataset, and ensure its responsible deployment.