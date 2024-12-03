---
language:
- en
license:
- mit
library_name: "pytorch"
multilinguality:
- monolingual
pretty_name: FairBERTa
tags:
- counterfactual
- perturb
- fairness
- nlp
- demographic
- diverse
- gender
- non-binary
- race
- age
metrics:
- bleu
---

# FairBERTa
FairBERTa is the first large language model trained on demographically perturbed corpora. Compared to RoBERTa, FairBERTa's fairness is improved, while its performance does not degrade on downstream tasks.

- **Repository:** https://github.com/facebookresearch/ResponsibleNLP/
- **Paper:** https://aclanthology.org/2022.emnlp-main.646/
- **Point of Contact:** rebeccaqian@meta.com, ccross@meta.com, douwe@huggingface.co, adinawilliams@meta.com
- **License:** MIT

## Model Description
FairBERTa is a transformers model pretrained on a large corpus of English data with the Masked language modeling (MLM) objective. The model randomly masks 15% of words in the input sequence then run the entire masked sentence through the model and has to predict the masked words. This is different from traditional recurrent neural networks (RNNs) that usually see the words one after the other, or from autoregressive models like GPT which internally mask the future tokens. It allows the model to learn a bidirectional representation of the sentence.

The model learns an inner representation of the English language that can then be used to extract features useful for downstream tasks.

### Model Summary

FairBERTa can be finetuned on a variety of downstream tasks.

FairBERTa is trained using the FairSeq library, with the same parameters as the RoBERTa-base model.

### Uses

The perturber is intended for use by fairness researchers and engineers working on demographic debiasing applications. The perturber is a controllable generation model that given a word, target demographic attribute and input text, outputs text where the selected word and associated references are rewritten to the target demographic attribute. Control variables and the input text are separated by a <PERT_SEP> token.

## Training
The FairBERTa model was pretrained in a similar manner to [RoBERTa](https://huggingface.co/roberta-base). It was pretrained on 160GB of perturbed datasets. The training data consists of five sources: BookCorpus, English Wikipedia, CC-News, OpenWebText, Stories.

We sample chunks of 512 token sequences (the perturber's max context window), select a 

## Bias, Risks & Limitations
FairBERTa shows improved performance compared to RoBERTa on a variety of fairness metrics.

For an in-depth discussion of bias, risks and limitations, see the Results and Limitations sections of [our paper](https://aclanthology.org/2022.emnlp-main.646/).

## Citation
```
@inproceedings{qian-etal-2022-perturbation,
    title = "Perturbation Augmentation for Fairer {NLP}",
    author = "Qian, Rebecca  and
      Ross, Candace  and
      Fernandes, Jude  and
      Smith, Eric Michael  and
      Kiela, Douwe  and
      Williams, Adina",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.emnlp-main.646",
    pages = "9496--9521",
    abstract = "Unwanted and often harmful social biases are becoming ever more salient in NLP research, affecting both models and datasets. In this work, we ask whether training on demographically perturbed data leads to fairer language models. We collect a large dataset of human annotated text perturbations and train a neural perturbation model, which we show outperforms heuristic alternatives. We find that (i) language models (LMs) pre-trained on demographically perturbed corpora are typically more fair, and (ii) LMs finetuned on perturbed GLUE datasets exhibit less demographic bias on downstream tasks, and (iii) fairness improvements do not come at the expense of performance on downstream tasks. Lastly, we discuss outstanding questions about how best to evaluate the (un)fairness of large language models. We hope that this exploration of neural demographic perturbation will help drive more improvement towards fairer NLP.",
}
```

### Model Card Contact

Thanks to [@Rebecca-Qian](https://github.com/Rebecca-Qian) for adding this model.