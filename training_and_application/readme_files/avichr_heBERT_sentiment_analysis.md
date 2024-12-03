## HeBERT: Pre-trained BERT for Polarity Analysis and Emotion Recognition
HeBERT is a Hebrew pre-trained language model. It is based on Google's BERT architecture and it is BERT-Base config [(Devlin et al. 2018)](https://arxiv.org/abs/1810.04805). <br>

HeBert was trained on three datasets: 
1. A Hebrew version of OSCAR [(Ortiz, 2019)](https://oscar-corpus.com/): ~9.8 GB of data, including 1 billion words and over 20.8 million sentences. 
2. A Hebrew dump of Wikipedia: ~650 MB of data, including over 63 million words and 3.8 million sentences
3. Emotion UGC data was collected for the purpose of this study. (described below)
We evaluated the model on emotion recognition and sentiment analysis, for downstream tasks. 

### Emotion UGC Data Description
Our User-Generated Content (UGC) is comments written on articles collected from 3 major news sites, between January 2020 to August 2020, Total data size of ~150 MB of data, including over 7 million words and 350K sentences.
4000 sentences annotated by crowd members (3-10 annotators per sentence) for 8 emotions (anger, disgust, expectation, fear, happy, sadness, surprise, and trust) and overall sentiment/polarity <br>
In order to validate the annotation, we search for an agreement between raters to emotion in each sentence using Krippendorff's alpha [(krippendorff, 1970)](https://journals.sagepub.com/doi/pdf/10.1177/001316447003000105). We left sentences that got alpha > 0.7. Note that while we found a general agreement between raters about emotions like happiness, trust, and disgust, there are few emotions with general disagreement about them, apparently given the complexity of finding them in the text (e.g. expectation and surprise).

### Performance
#### sentiment analysis  

|              | precision | recall | f1-score |
|--------------|-----------|--------|----------|
| natural      | 0.83      | 0.56   | 0.67     |
| positive     | 0.96      | 0.92   | 0.94     |
| negative     | 0.97      | 0.99   | 0.98     |
| accuracy     |           |        | 0.97     |
| macro avg    | 0.92      | 0.82   | 0.86     |
| weighted avg | 0.96      | 0.97   | 0.96     |

## How to use
### For masked-LM model (can be fine-tunned to any down-stream task)
```
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("avichr/heBERT")
model = AutoModel.from_pretrained("avichr/heBERT")
	
from transformers import pipeline
fill_mask = pipeline(
    "fill-mask",
    model="avichr/heBERT",
    tokenizer="avichr/heBERT"
)
fill_mask("הקורונה לקחה את [MASK] ולנו לא נשאר דבר.")
```

### For sentiment classification model (polarity ONLY):
```
from transformers import AutoTokenizer, AutoModel, pipeline
tokenizer = AutoTokenizer.from_pretrained("avichr/heBERT_sentiment_analysis") #same as 'avichr/heBERT' tokenizer
model = AutoModel.from_pretrained("avichr/heBERT_sentiment_analysis")

# how to use?
sentiment_analysis = pipeline(
    "sentiment-analysis",
    model="avichr/heBERT_sentiment_analysis",
    tokenizer="avichr/heBERT_sentiment_analysis",
    return_all_scores = True
)

>>>  sentiment_analysis('אני מתלבט מה לאכול לארוחת צהריים')	
[[{'label': 'natural', 'score': 0.9978172183036804},
{'label': 'positive', 'score': 0.0014792329166084528},
{'label': 'negative', 'score': 0.0007035882445052266}]]

>>>  sentiment_analysis('קפה זה טעים')
[[{'label': 'natural', 'score': 0.00047328314394690096},
{'label': 'possitive', 'score': 0.9994067549705505},
{'label': 'negetive', 'score': 0.00011996887042187154}]]

>>>  sentiment_analysis('אני לא אוהב את העולם')
[[{'label': 'natural', 'score': 9.214012970915064e-05}, 
{'label': 'possitive', 'score': 8.876807987689972e-05}, 
{'label': 'negetive', 'score': 0.9998190999031067}]]
```

Our model is also available on AWS! for more information visit [AWS' git](https://github.com/aws-samples/aws-lambda-docker-serverless-inference/tree/main/hebert-sentiment-analysis-inference-docker-lambda)


## Stay tuned!
We are still working on our model and will edit this page as we progress.<br>
Note that we have released only sentiment analysis (polarity) at this point, emotion detection will be released later on.<br>
our git: https://github.com/avichaychriqui/HeBERT


## If you used this model please cite us as :
Chriqui, A., & Yahav, I. (2021). HeBERT & HebEMO: a Hebrew BERT Model and a Tool for Polarity Analysis and Emotion Recognition. arXiv preprint arXiv:2102.01909.
```
@article{chriqui2021hebert,
  title={HeBERT \\\\\\\\\\\\\\\\& HebEMO: a Hebrew BERT Model and a Tool for Polarity Analysis and Emotion Recognition},
  author={Chriqui, Avihay and Yahav, Inbal},
  journal={arXiv preprint arXiv:2102.01909},
  year={2021}
}
```

