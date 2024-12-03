---
datasets:
- cardiffnlp/tweet_topic_multi
metrics:
- f1
- accuracy
model-index:
- name: cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-multi-all
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: cardiffnlp/tweet_topic_multi
      type: cardiffnlp/tweet_topic_multi
      args: cardiffnlp/tweet_topic_multi
      split: test_2021 
    metrics:
    - name: F1
      type: f1
      value: 0.7647668393782383
    - name: F1 (macro)
      type: f1_macro
      value: 0.6187022581213811
    - name: Accuracy
      type: accuracy
      value: 0.5485407980941036
pipeline_tag: text-classification
widget:
- text: "I'm sure the {@Tampa Bay Lightning@} would’ve rather faced the Flyers but man does their experience versus the Blue Jackets this year and last help them a lot versus this Islanders team. Another meat grinder upcoming for the good guys"
  example_title: "Example 1"
- text: "Love to take night time bike rides at the jersey shore. Seaside Heights boardwalk. Beautiful weather. Wishing everyone a safe Labor Day weekend in the US." 
  example_title: "Example 2"
---
# cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-multi-all

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base-dec2021](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021) on the [tweet_topic_multi](https://huggingface.co/datasets/cardiffnlp/tweet_topic_multi). This model is fine-tuned on `train_all` split and validated on `test_2021` split of tweet_topic.
Fine-tuning script can be found [here](https://huggingface.co/datasets/cardiffnlp/tweet_topic_multi/blob/main/lm_finetuning.py). It achieves the following results on the test_2021 set:

- F1 (micro): 0.7647668393782383
- F1 (macro): 0.6187022581213811
- Accuracy: 0.5485407980941036


### Usage

```python
import math
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def sigmoid(x):
  return 1 / (1 + math.exp(-x))
  
tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-multi-all")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-multi-all", problem_type="multi_label_classification")
model.eval()
class_mapping = model.config.id2label

with torch.no_grad():
  text = #NewVideo Cray Dollas- Water- Ft. Charlie Rose- (Official Music Video)- {{URL}} via {@YouTube@} #watchandlearn {{USERNAME}}
  tokens = tokenizer(text, return_tensors='pt')
  output = model(**tokens)
  flags = [sigmoid(s) > 0.5 for s in output[0][0].detach().tolist()]
  topic = [class_mapping[n] for n, i in enumerate(flags) if i]
print(topic)
```

### Reference

```

@inproceedings{dimosthenis-etal-2022-twitter,
    title = "{T}witter {T}opic {C}lassification",
    author = "Antypas, Dimosthenis  and
    Ushio, Asahi  and
    Camacho-Collados, Jose  and
    Neves, Leonardo  and
    Silva, Vitor  and
    Barbieri, Francesco",
    booktitle = "Proceedings of the 29th International Conference on Computational Linguistics",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "International Committee on Computational Linguistics"
}

```
