---
language:
  - as
  - bn
  - brx
  - doi
  - en
  - gom
  - gu
  - hi
  - kn
  - ks
  - kas
  - mai
  - ml
  - mr
  - mni
  - mnb
  - ne
  - or
  - pa
  - sa
  - sat
  - sd
  - snd
  - ta
  - te
  - ur
language_details: >-
  asm_Beng, ben_Beng, brx_Deva, doi_Deva, eng_Latn, gom_Deva, guj_Gujr,
  hin_Deva, kan_Knda, kas_Arab, kas_Deva, mai_Deva, mal_Mlym, mar_Deva,
  mni_Beng, mni_Mtei, npi_Deva, ory_Orya, pan_Guru, san_Deva, sat_Olck,
  snd_Arab, snd_Deva, tam_Taml, tel_Telu, urd_Arab
tags:
  - indicbert2
  - ai4bharat
  - multilingual
license: mit
metrics:
- accuracy
pipeline_tag: fill-mask
---
# IndicBERT
A multilingual language model trained on IndicCorp v2 and evaluated on IndicXTREME benchmark. The model has 278M parameters and is available in 23 Indic languages and English. The models are trained with various objectives and datasets. The list of models are as follows:

- IndicBERT-MLM [[Model](https://huggingface.co/ai4bharat/IndicBERTv2-MLM-only)] - A vanilla BERT style model trained on IndicCorp v2 with the MLM objective
    - +Samanantar [[Model](https://huggingface.co/ai4bharat/IndicBERTv2-MLM-Sam-TLM)] - TLM as an additional objective with Samanantar Parallel Corpus [[Paper](https://aclanthology.org/2022.tacl-1.9)] | [[Dataset](https://huggingface.co/datasets/ai4bharat/samanantar)]
    - +Back-Translation [[Model](https://huggingface.co/ai4bharat/IndicBERTv2-MLM-Back-TLM)] - TLM as an additional objective by translating the Indic parts of IndicCorp v2 dataset into English w/ IndicTrans model [[Model](https://github.com/AI4Bharat/indicTrans#download-model)]
- IndicBERT-SS [[Model](https://huggingface.co/ai4bharat/IndicBERTv2-SS)] - To encourage better lexical sharing among languages we convert the scripts from Indic languages to Devanagari and train a BERT style model with the MLM objective

## Run Fine-tuning
Fine-tuning scripts are based on transformers library. Create a new conda environment and set it up as follows:
```shell
conda create -n finetuning python=3.9
pip install -r requirements.txt
```

All the tasks follow the same structure, please check individual files for detailed hyper-parameter choices. The following command runs the fine-tuning for a task:
```shell
python IndicBERT/fine-tuning/$TASK_NAME/$TASK_NAME.py \
    --model_name_or_path=$MODEL_NAME \
    --do_train
```
Arguments:
- MODEL_NAME: name of the model to fine-tune, can be a local path or a model from the [HuggingFace Model Hub](https://huggingface.co/models)
- TASK_NAME: one of [`ner, paraphrase, qa, sentiment, xcopa, xnli, flores`]

> For MASSIVE task, please use the instrction provided in the [official repository](https://github.com/alexa/massive)


## Citation

```
@inproceedings{doddapaneni-etal-2023-towards,
    title = "Towards Leaving No {I}ndic Language Behind: Building Monolingual Corpora, Benchmark and Models for {I}ndic Languages",
    author = "Doddapaneni, Sumanth  and
      Aralikatte, Rahul  and
      Ramesh, Gowtham  and
      Goyal, Shreya  and
      Khapra, Mitesh M.  and
      Kunchukuttan, Anoop  and
      Kumar, Pratyush",
    editor = "Rogers, Anna  and
      Boyd-Graber, Jordan  and
      Okazaki, Naoaki",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-long.693",
    doi = "10.18653/v1/2023.acl-long.693",
    pages = "12402--12426",
    abstract = "Building Natural Language Understanding (NLU) capabilities for Indic languages, which have a collective speaker base of more than one billion speakers is absolutely crucial. In this work, we aim to improve the NLU capabilities of Indic languages by making contributions along 3 important axes (i) monolingual corpora (ii) NLU testsets (iii) multilingual LLMs focusing on Indic languages. Specifically, we curate the largest monolingual corpora, IndicCorp, with 20.9B tokens covering 24 languages from 4 language families - a 2.3x increase over prior work, while supporting 12 additional languages. Next, we create a human-supervised benchmark, IndicXTREME, consisting of nine diverse NLU tasks covering 20 languages. Across languages and tasks, IndicXTREME contains a total of 105 evaluation sets, of which 52 are new contributions to the literature. To the best of our knowledge, this is the first effort towards creating a standard benchmark for Indic languages that aims to test the multilingual zero-shot capabilities of pretrained language models. Finally, we train IndicBERT v2, a state-of-the-art model supporting all the languages. Averaged across languages and tasks, the model achieves an absolute improvement of 2 points over a strong baseline. The data and models are available at \url{https://github.com/AI4Bharat/IndicBERT}.",
}
```