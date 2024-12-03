---
language:
- en
tags:
- toxic comments classification
licenses:
- cc-by-nc-sa
---

## Toxicity Classification Model

This model is trained for toxicity classification task. The dataset used for training is the merge of the English parts of the three datasets by **Jigsaw** ([Jigsaw 2018](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge), [Jigsaw 2019](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification), [Jigsaw 2020](https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification)), containing around 2 million examples. We split it into two parts and fine-tune a RoBERTa model ([RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692)) on it. The classifiers perform closely on the test set of the first Jigsaw competition, reaching the **AUC-ROC** of 0.98 and **F1-score** of 0.76.

## How to use
```python
import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification

tokenizer = RobertaTokenizer.from_pretrained('s-nlp/roberta_toxicity_classifier')
model = RobertaForSequenceClassification.from_pretrained('s-nlp/roberta_toxicity_classifier')

batch = tokenizer.encode("You are amazing!", return_tensors="pt")

output = model(batch)
predicted_label = torch.sigmoid(output.logits).argmax().item()
# 0 for neutral, 1 for toxic
```

## Citation

If you use our model in your research, please, cite our work:

```
@inproceedings{logacheva-etal-2022-paradetox,
    title = "{P}ara{D}etox: Detoxification with Parallel Data",
    author = "Logacheva, Varvara  and
      Dementieva, Daryna  and
      Ustyantsev, Sergey  and
      Moskovskiy, Daniil  and
      Dale, David  and
      Krotova, Irina  and
      Semenov, Nikita  and
      Panchenko, Alexander",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-long.469",
    pages = "6804--6818",
    abstract = "We present a novel pipeline for the collection of parallel data for the detoxification task. We collect non-toxic paraphrases for over 10,000 English toxic sentences. We also show that this pipeline can be used to distill a large existing corpus of paraphrases to get toxic-neutral sentence pairs. We release two parallel corpora which can be used for the training of detoxification models. To the best of our knowledge, these are the first parallel datasets for this task.We describe our pipeline in detail to make it fast to set up for a new language or domain, thus contributing to faster and easier development of new parallel resources.We train several detoxification models on the collected data and compare them with several baselines and state-of-the-art unsupervised approaches. We conduct both automatic and manual evaluations. All models trained on parallel data outperform the state-of-the-art unsupervised models by a large margin. This suggests that our novel datasets can boost the performance of detoxification systems.",
}
```

## Licensing Information

[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png