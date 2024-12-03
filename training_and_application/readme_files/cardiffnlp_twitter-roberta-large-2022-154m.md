---
language: en
tags:
- timelms
- twitter
license: mit
datasets:
- twitter-api
---

# Twitter 2022 154M (RoBERTa-large, 154M - full update)

This is a RoBERTa-large model trained on 154M tweets until the end of December 2022 (from original checkpoint, no incremental updates). 
A base model trained on the same datais available [here](https://huggingface.co/cardiffnlp/twitter-roberta-base-2022-154m).

These 154M tweets result from filtering 220M tweets obtained exclusively from the Twitter Academic API, covering every month between 2018-01 and 2022-12.
Filtering and preprocessing details are available in the [TimeLMs paper](https://arxiv.org/abs/2202.03829).

Below, we provide some usage examples using the standard Transformers interface. For another interface more suited to comparing predictions and perplexity scores between models trained at different temporal intervals, check the [TimeLMs repository](https://github.com/cardiffnlp/timelms).

For other models trained until different periods, check this [table](https://github.com/cardiffnlp/timelms#released-models).

## Preprocess Text 
Replace usernames and links for placeholders: "@user" and "http".
If you're interested in retaining verified users which were also retained during training, you may keep the users listed [here](https://github.com/cardiffnlp/timelms/tree/main/data).
```python
def preprocess(text):
    preprocessed_text = []
    for t in text.split():
        if len(t) > 1:
            t = '@user' if t[0] == '@' and t.count('@') == 1 else t
            t = 'http' if t.startswith('http') else t
        preprocessed_text.append(t)
    return ' '.join(preprocessed_text)
```

## Example Masked Language Model 

```python
from transformers import pipeline, AutoTokenizer

MODEL = "cardiffnlp/twitter-roberta-large-2022-154m"
fill_mask = pipeline("fill-mask", model=MODEL, tokenizer=MODEL)
tokenizer = AutoTokenizer.from_pretrained(MODEL)

def pprint(candidates, n):
    for i in range(n):
        token = tokenizer.decode(candidates[i]['token'])
        score = candidates[i]['score']
        print("%d) %.5f %s" % (i+1, score, token))

texts = [
    "So glad I'm <mask> vaccinated.",
    "I keep forgetting to bring a <mask>.",
    "Looking forward to watching <mask> Game tonight!",
]
for text in texts:
    t = preprocess(text)
    print(f"{'-'*30}\n{t}")
    candidates = fill_mask(t)
    pprint(candidates, 5)
```

Output: 

```
------------------------------
So glad I'm <mask> vaccinated.
1) 0.37136  fully
2) 0.20631  a
3) 0.09422  the
4) 0.07649  not
5) 0.04505  already
------------------------------
I keep forgetting to bring a <mask>.
1) 0.10507  mask
2) 0.05810  pen
3) 0.05142  charger
4) 0.04082  tissue
5) 0.03955  lighter
------------------------------
Looking forward to watching <mask> Game tonight!
1) 0.45783  The
2) 0.32842  the
3) 0.02705  Squid
4) 0.01157  Big
5) 0.00538  Match
```

## Example Tweet Embeddings
```python
from transformers import AutoTokenizer, AutoModel, TFAutoModel
import numpy as np
from scipy.spatial.distance import cosine
from collections import Counter

def get_embedding(text):  # naive approach for demonstration
  text = preprocess(text)
  encoded_input = tokenizer(text, return_tensors='pt')
  features = model(**encoded_input)
  features = features[0].detach().cpu().numpy() 
  return np.mean(features[0], axis=0) 


MODEL = "cardiffnlp/twitter-roberta-large-2022-154m"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModel.from_pretrained(MODEL)

query = "The book was awesome"
tweets = ["I just ordered fried chicken 🐣", 
          "The movie was great",
          "What time is the next game?",
          "Just finished reading 'Embeddings in NLP'"]

sims = Counter()
for tweet in tweets:
    sim = 1 - cosine(get_embedding(query), get_embedding(tweet))
    sims[tweet] = sim

print('Most similar to: ', query)
print(f"{'-'*30}")
for idx, (tweet, sim) in enumerate(sims.most_common()):
    print("%d) %.5f %s" % (idx+1, sim, tweet))
```
Output: 

```
Most similar to:  The book was awesome
------------------------------
1) 0.99820 The movie was great
2) 0.99306 Just finished reading 'Embeddings in NLP'
3) 0.99257 What time is the next game?
4) 0.98561 I just ordered fried chicken 🐣
```

## Example Feature Extraction 

```python
from transformers import AutoTokenizer, AutoModel, TFAutoModel
import numpy as np

MODEL = "cardiffnlp/twitter-roberta-large-2022-154m"
tokenizer = AutoTokenizer.from_pretrained(MODEL)

text = "Good night 😊"
text = preprocess(text)

# Pytorch
model = AutoModel.from_pretrained(MODEL)
encoded_input = tokenizer(text, return_tensors='pt')
features = model(**encoded_input)
features = features[0].detach().cpu().numpy() 
features_mean = np.mean(features[0], axis=0) 
#features_max = np.max(features[0], axis=0)

# # Tensorflow
# model = TFAutoModel.from_pretrained(MODEL)
# encoded_input = tokenizer(text, return_tensors='tf')
# features = model(encoded_input)
# features = features[0].numpy()
# features_mean = np.mean(features[0], axis=0) 
# #features_max = np.max(features[0], axis=0)
```

### BibTeX entry and citation info

Please cite the [reference paper](https://arxiv.org/abs/2308.02142) if you use this model.

```bibtex
@article{loureiro2023tweet,
  title={Tweet Insights: A Visualization Platform to Extract Temporal Insights from Twitter},
  author={Loureiro, Daniel and Rezaee, Kiamehr and Riahi, Talayeh and Barbieri, Francesco and Neves, Leonardo and Anke, Luis Espinosa and Camacho-Collados, Jose},
  journal={arXiv preprint arXiv:2308.02142},
  year={2023}
}
```
