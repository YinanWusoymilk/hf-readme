---
license: apache-2.0
thumbnail: https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis/resolve/main/logo_no_bg.png
tags:
- generated_from_trainer
- financial
- stocks
- sentiment
widget:
- text: "Operating profit totaled EUR 9.4 mn , down from EUR 11.7 mn in 2004 ."
datasets:
- financial_phrasebank
metrics:
- accuracy
model-index:
- name: distilRoberta-financial-sentiment
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: financial_phrasebank
      type: financial_phrasebank
      args: sentences_allagree
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9823008849557522
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->


<div style="text-align:center;width:250px;height:250px;">
    <img src="https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis/resolve/main/logo_no_bg.png" alt="logo">
</div>


# DistilRoberta-financial-sentiment


This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the financial_phrasebank dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1116
- Accuracy: **0.98**23

## Base Model description

This model is a distilled version of the [RoBERTa-base model](https://huggingface.co/roberta-base). It follows the same training procedure as [DistilBERT](https://huggingface.co/distilbert-base-uncased).
The code for the distillation process can be found [here](https://github.com/huggingface/transformers/tree/master/examples/distillation).
This model is case-sensitive: it makes a difference between English and English.

The model has 6 layers, 768 dimension and 12 heads, totalizing 82M parameters (compared to 125M parameters for RoBERTa-base).
On average DistilRoBERTa is twice as fast as Roberta-base.

## Training Data

Polar sentiment dataset of sentences from financial news. The dataset consists of 4840 sentences from English language financial news categorised by sentiment. The dataset is divided by agreement rate of 5-8 annotators.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 255  | 0.1670          | 0.9646   |
| 0.209         | 2.0   | 510  | 0.2290          | 0.9558   |
| 0.209         | 3.0   | 765  | 0.2044          | 0.9558   |
| 0.0326        | 4.0   | 1020 | 0.1116          | 0.9823   |
| 0.0326        | 5.0   | 1275 | 0.1127          | 0.9779   |


### Framework versions

- Transformers 4.10.2
- Pytorch 1.9.0+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3
