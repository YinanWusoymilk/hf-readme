# HeBERT: Pre-trained BERT for Polarity Analysis and Emotion Recognition
<img align="right" src="https://github.com/avichaychriqui/HeBERT/blob/main/data/heBERT_logo.png?raw=true" width="250">

HeBERT is a Hebrew pretrained language model. It is based on [Google's BERT](https://arxiv.org/abs/1810.04805) architecture and it is BERT-Base config. <br>

HeBert was trained on three dataset: 
1. A Hebrew version of [OSCAR](https://oscar-corpus.com/): ~9.8 GB of data, including 1 billion words and over 20.8 millions sentences. 
2. A Hebrew dump of [Wikipedia](https://dumps.wikimedia.org/): ~650 MB of data, including over 63 millions words and 3.8 millions sentences
3. Emotion User Generated Content (UGC) data that was collected for the purpose of this study (described below).


## Named-entity recognition (NER)
The ability of the model to classify named entities in text, such as persons' names, organizations, and locations; tested on a labeled dataset from [Ben Mordecai and M Elhadad (2005)](https://www.cs.bgu.ac.il/~elhadad/nlpproj/naama/), and evaluated with F1-score.

### How to use
```
	from transformers import pipeline
	
	# how to use?
	NER = pipeline(
	    "token-classification",
	    model="avichr/heBERT_NER",
	    tokenizer="avichr/heBERT_NER",
	)
	NER('דויד לומד באוניברסיטה העברית שבירושלים')
```

## Other tasks
[**Emotion Recognition Model**](https://huggingface.co/avichr/hebEMO_trust).
An online model can be found at [huggingface spaces](https://huggingface.co/spaces/avichr/HebEMO_demo) or as [colab notebook](https://colab.research.google.com/drive/1Jw3gOWjwVMcZslu-ttXoNeD17lms1-ff?usp=sharing)
<br>
[**Sentiment Analysis**](https://huggingface.co/avichr/heBERT_sentiment_analysis).
<br>
[**masked-LM model**](https://huggingface.co/avichr/heBERT) (can be fine-tunned to any down-stream task).

## Contact us
[Avichay Chriqui](mailto:avichayc@mail.tau.ac.il) <br>
[Inbal yahav](mailto:inbalyahav@tauex.tau.ac.il) <br>
The Coller Semitic Languages AI Lab <br>
Thank you, תודה, شكرا <br>

## If you used this model please cite us as :
Chriqui, A., & Yahav, I. (2021). HeBERT & HebEMO: a Hebrew BERT Model and a Tool for Polarity Analysis and Emotion Recognition. arXiv preprint arXiv:2102.01909.
```
@article{chriqui2021hebert,
  title={HeBERT \& HebEMO: a Hebrew BERT Model and a Tool for Polarity Analysis and Emotion Recognition},
  author={Chriqui, Avihay and Yahav, Inbal},
  journal={arXiv preprint arXiv:2102.01909},
  year={2021}
}
```
[git](https://github.com/avichaychriqui/HeBERT)

