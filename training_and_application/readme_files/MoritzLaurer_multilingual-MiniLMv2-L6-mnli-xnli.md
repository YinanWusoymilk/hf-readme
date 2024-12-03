
---
language: 
- multilingual
- en 
- ar 
- bg 
- de 
- el 
- es 
- fr 
- hi 
- ru 
- sw 
- th 
- tr 
- ur 
- vi 
- zh
license: mit
tags:
- zero-shot-classification
- text-classification
- nli
- pytorch
metrics:
- accuracy
datasets:
- multi_nli
- xnli
pipeline_tag: zero-shot-classification
widget:
- text: "Angela Merkel ist eine Politikerin in Deutschland und Vorsitzende der CDU"
  candidate_labels: "politics, economy, entertainment, environment"
---


---
# Multilingual MiniLMv2-L6-mnli-xnli
## Model description
This multilingual model can perform natural language inference (NLI) on 100+ languages and is therefore also 
suitable for multilingual zero-shot classification. The underlying multilingual-MiniLM-L6 model was created 
by Microsoft and was distilled from XLM-RoBERTa-large (see details [in the original paper](https://arxiv.org/pdf/2002.10957.pdf) 
and newer information in [this repo](https://github.com/microsoft/unilm/tree/master/minilm)). 
The model was then fine-tuned on the [XNLI dataset](https://huggingface.co/datasets/xnli), which contains hypothesis-premise pairs from 15 languages, 
as well as the English [MNLI dataset](https://huggingface.co/datasets/multi_nli).

The main advantage of distilled models is that they are smaller (faster inference, lower memory requirements) than their teachers (XLM-RoBERTa-large).
The disadvantage is that they lose some of the performance of their larger teachers. 

For highest inference speed, I recommend using this 6-layer model. For higher performance I recommend 
[mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) (as of 14.02.2023).

### How to use the model
#### Simple zero-shot classification pipeline
```python
from transformers import pipeline
classifier = pipeline("zero-shot-classification", model="MoritzLaurer/multilingual-MiniLMv2-L6-mnli-xnli")

sequence_to_classify = "Angela Merkel ist eine Politikerin in Deutschland und Vorsitzende der CDU"
candidate_labels = ["politics", "economy", "entertainment", "environment"]
output = classifier(sequence_to_classify, candidate_labels, multi_label=False)
print(output)
```
#### NLI use-case
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

model_name = "MoritzLaurer/multilingual-MiniLMv2-L6-mnli-xnli"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

premise = "Angela Merkel ist eine Politikerin in Deutschland und Vorsitzende der CDU"
hypothesis = "Emmanuel Macron is the President of France"

input = tokenizer(premise, hypothesis, truncation=True, return_tensors="pt")
output = model(input["input_ids"].to(device))  # device = "cuda:0" or "cpu"
prediction = torch.softmax(output["logits"][0], -1).tolist()
label_names = ["entailment", "neutral", "contradiction"]
prediction = {name: round(float(pred) * 100, 1) for pred, name in zip(prediction, label_names)}
print(prediction)
```

### Training data
This model was trained on the XNLI development dataset and the MNLI train dataset. 
The XNLI development set consists of 2490 professionally translated texts from English 
to 14 other languages (37350 texts in total) (see [this paper](https://arxiv.org/pdf/1809.05053.pdf)). 
Note that the XNLI contains a training set of 15 machine translated versions of the MNLI dataset for 15 languages, 
but due to quality issues with these machine translations, this model was only trained on the professional translations 
from the XNLI development set and the original English MNLI training set (392 702 texts). 
Not using machine translated texts can avoid overfitting the model to the 15 languages; 
avoids catastrophic forgetting of the other languages it was pre-trained on; 
and significantly reduces training costs. 

### Training procedure
The model was trained using the Hugging Face trainer with the following hyperparameters. 
The exact underlying model is [mMiniLMv2-L6-H384-distilled-from-XLMR-Large](https://huggingface.co/nreimers/mMiniLMv2-L6-H384-distilled-from-XLMR-Large).
```
training_args = TrainingArguments(
    num_train_epochs=3,              # total number of training epochs
    learning_rate=4e-05,
    per_device_train_batch_size=64,   # batch size per device during training
    per_device_eval_batch_size=120,    # batch size for evaluation
    warmup_ratio=0.06,                # number of warmup steps for learning rate scheduler
    weight_decay=0.01,               # strength of weight decay
)
```

### Eval results
The model was evaluated on the XNLI test set on 15 languages (5010 texts per language, 75150 in total). 
Note that multilingual NLI models are capable of classifying NLI texts without receiving NLI training data 
in the specific language (cross-lingual transfer). This means that the model is also able of doing NLI on 
the other languages it was training on, but performance is most likely lower than for those languages available in XNLI.

The average XNLI performance of multilingual-MiniLM-L6 reported in the paper is 0.68 ([see table 11](https://arxiv.org/pdf/2002.10957.pdf)). 
This reimplementation has an average performance of 0.713. 
This increase in performance is probably thanks to the addition of MNLI in the training data and this model was distilled from 
XLM-RoBERTa-large instead of -base (multilingual-MiniLM-L6-v2). 

|Datasets|avg_xnli|ar|bg|de|el|en|es|fr|hi|ru|sw|th|tr|ur|vi|zh|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Accuracy|0.713|0.687|0.742|0.719|0.723|0.789|0.748|0.741|0.691|0.714|0.642|0.699|0.696|0.664|0.723|0.721|
|Speed text/sec (A100 GPU, eval_batch=120)|6093.0|6210.0|6003.0|6053.0|5409.0|6531.0|6205.0|5615.0|5734.0|5970.0|6219.0|6289.0|6533.0|5851.0|5970.0|6798.0|


|Datasets|mnli_m|mnli_mm|
| :---: | :---: | :---: |
|Accuracy|0.782|0.8|
|Speed text/sec (A100 GPU, eval_batch=120)|4430.0|4395.0|



## Limitations and bias
Please consult the original paper and literature on different NLI datasets for potential biases. 

## Citation
If you use this model, please cite: Laurer, Moritz, Wouter van Atteveldt, Andreu Salleras Casas, and Kasper Welbers. 2022. 
‘Less Annotating, More Classifying – Addressing the Data Scarcity Issue of Supervised Machine Learning with Deep Transfer Learning and BERT - NLI’. 
Preprint, June. Open Science Framework. https://osf.io/74b8k.

## Ideas for cooperation or questions?
If you have questions or ideas for cooperation, contact me at m{dot}laurer{at}vu{dot}nl or [LinkedIn](https://www.linkedin.com/in/moritz-laurer/)








