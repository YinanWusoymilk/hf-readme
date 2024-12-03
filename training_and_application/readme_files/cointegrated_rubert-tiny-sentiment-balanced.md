---
language: ["ru"]
tags:
- russian
- classification
- sentiment
- multiclass
widget:
- text: "Какая гадость эта ваша заливная рыба!"
---
This is the [cointegrated/rubert-tiny](https://huggingface.co/cointegrated/rubert-tiny) model fine-tuned for classification of sentiment for short Russian texts. 

The problem is formulated as multiclass classification: `negative` vs `neutral` vs `positive`. 
## Usage

The function below estimates the sentiment of the given text:
```python
# !pip install transformers sentencepiece --quiet
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_checkpoint = 'cointegrated/rubert-tiny-sentiment-balanced'
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)
if torch.cuda.is_available():
    model.cuda()
    
def get_sentiment(text, return_type='label'):
    """ Calculate sentiment of a text. `return_type` can be 'label', 'score' or 'proba' """
    with torch.no_grad():
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True).to(model.device)
        proba = torch.sigmoid(model(**inputs).logits).cpu().numpy()[0]
    if return_type == 'label':
        return model.config.id2label[proba.argmax()]
    elif return_type == 'score':
        return proba.dot([-1, 0, 1])
    return proba

text = 'Какая гадость эта ваша заливная рыба!'
# classify the text
print(get_sentiment(text, 'label'))  # negative
# score the text on the scale from -1 (very negative) to +1 (very positive)
print(get_sentiment(text, 'score'))  # -0.5894946306943893
# calculate probabilities of all labels
print(get_sentiment(text, 'proba'))  # [0.7870447  0.4947824  0.19755007]
```

## Training

We trained the model on [the datasets collected by Smetanin](https://github.com/sismetanin/sentiment-analysis-in-russian). We have converted all training data into a 3-class format and have up- and downsampled the training data to balance both the sources and the classes. The training code is available as [a Colab notebook](https://gist.github.com/avidale/e678c5478086c1d1adc52a85cb2b93e6). The metrics on the balanced test set are the following: 


| Source | Macro F1 |
| ----------- | ----------- |
| SentiRuEval2016_banks | 0.83 | 
| SentiRuEval2016_tele  | 0.74 |
| kaggle_news | 0.66 |
| linis | 0.50 |
| mokoron | 0.98 |
| rureviews | 0.72 |
| rusentiment | 0.67 | 

