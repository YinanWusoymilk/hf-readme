---
tags:
- pytorch_model_hub_mixin
- model_hub_mixin
license: apache-2.0
---
# Domain Classifier

# Model Overview
This is a text classification model to classify documents into one of 26 domain classes:

'Adult', 'Arts_and_Entertainment', 'Autos_and_Vehicles', 'Beauty_and_Fitness', 'Books_and_Literature', 'Business_and_Industrial', 'Computers_and_Electronics', 'Finance', 'Food_and_Drink', 'Games', 'Health', 'Hobbies_and_Leisure', 'Home_and_Garden', 'Internet_and_Telecom', 'Jobs_and_Education', 'Law_and_Government', 'News', 'Online_Communities', 'People_and_Society', 'Pets_and_Animals', 'Real_Estate', 'Science', 'Sensitive_Subjects', 'Shopping', 'Sports', 'Travel_and_Transportation'
# Model Architecture
The model architecture is Deberta V3 Base
Context length is 512 tokens
# Training (details)
## Training data:
- 1 million Common Crawl samples, labeled using Google Cloud’s Natural Language API: https://cloud.google.com/natural-language/docs/classifying-text
- 500k Wikepedia articles, curated using Wikipedia-API: https://pypi.org/project/Wikipedia-API/
## Training steps:
Model was trained in multiple rounds using Wikipedia and Common Crawl data, labeled by a combination of pseudo labels and Google Cloud API.
# How To Use This Model
## Input
The model takes one or several paragraphs of text as input.
Example input:
```
q Directions
1. Mix 2 flours and baking powder together
2. Mix water and egg in a separate bowl. Add dry to wet little by little
3. Heat frying pan on medium
4. Pour batter into pan and then put blueberries on top before flipping
5. Top with desired toppings!
```
## Output
The model outputs one of the 26 domain classes as the predicted domain for each input sample.
Example output:
```
Food_and_Drink
```

# How to use in NeMo Curator

The inference code is available on [NeMo Curator's GitHub repository](https://github.com/NVIDIA/NeMo-Curator). Download the [model.pth](https://huggingface.co/nvidia/domain-classifier/blob/main/model.pth) file and check out this [example notebook](https://github.com/NVIDIA/NeMo-Curator/blob/main/tutorials/distributed_data_classification/distributed_data_classification.ipynb) to get started.

# How to use in transformers
To use the Domain classifier, use the following code:

```python

import torch
from torch import nn
from transformers import AutoModel, AutoTokenizer, AutoConfig
from huggingface_hub import PyTorchModelHubMixin

class CustomModel(nn.Module, PyTorchModelHubMixin):
    def __init__(self, config):
        super(CustomModel, self).__init__()
        self.model = AutoModel.from_pretrained(config['base_model'])
        self.dropout = nn.Dropout(config['fc_dropout'])
        self.fc = nn.Linear(self.model.config.hidden_size, len(config['id2label']))

    def forward(self, input_ids, attention_mask):
        features = self.model(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state
        dropped = self.dropout(features)
        outputs = self.fc(dropped)
        return torch.softmax(outputs[:, 0, :], dim=1)

# Setup configuration and model
config = AutoConfig.from_pretrained("nvidia/domain-classifier")
tokenizer = AutoTokenizer.from_pretrained("nvidia/domain-classifier")
model = CustomModel.from_pretrained("nvidia/domain-classifier")

# Prepare and process inputs
text_samples = ["Sports is a popular domain", "Politics is a popular domain"]
inputs = tokenizer(text_samples, return_tensors="pt", padding="longest", truncation=True)
outputs = model(inputs['input_ids'], inputs['attention_mask'])

# Predict and display results
predicted_classes = torch.argmax(outputs, dim=1)
predicted_domains = [config.id2label[class_idx.item()] for class_idx in predicted_classes.cpu().numpy()]
print(predicted_domains)
# ['Sports', 'News']
```

# Evaluation Benchmarks

Evaluation Metric: PR-AUC

PR-AUC score on evaluation set with 105k samples - 0.9873 

PR-AUC score for each domain:
| Domain                   | PR-AUC |
|:-------------------------|:-------|
| Adult                    | 0.999  |
| Arts_and_Entertainment   | 0.997  |
| Autos_and_Vehicles       | 0.997  |
| Beauty_and_Fitness       | 0.997  |
| Books_and_Literature     | 0.995  |
| Business_and_Industrial  | 0.982  |
| Computers_and_Electronics| 0.992  |
| Finance                  | 0.989  |
| Food_and_Drink           | 0.998  |
| Games                    | 0.997  |
| Health                   | 0.997  |
| Hobbies_and_Leisure      | 0.984  |
| Home_and_Garden          | 0.997  |
| Internet_and_Telecom     | 0.982  |
| Jobs_and_Education       | 0.993  |
| Law_and_Government       | 0.967  |
| News                     | 0.918  |
| Online_Communities       | 0.983  |
| People_and_Society       | 0.975  |
| Pets_and_Animals         | 0.997  |
| Real_Estate              | 0.997  |
| Science                  | 0.988  |
| Sensitive_Subjects       | 0.982  |
| Shopping                 | 0.995  |
| Sports                   | 0.995  |
| Travel_and_Transportation| 0.996  |
| Mean                     | 0.9873 |

# References
- https://arxiv.org/abs/2111.09543
- https://github.com/microsoft/DeBERTa
# License
License to use this model is covered by the Apache 2.0. By downloading the public and release version of the model, you accept the terms and conditions of the Apache License 2.0.
This repository contains the code for the domain classifier model.