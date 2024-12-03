---
license: cc-by-nc-sa-4.0
language:
- ab
- af
- am
- ar
- as
- az
- ba
- be
- bn
- bo
- bs
- br
- bg
- ca
- cs
- cv
- cy
- da
- de
- dv
- el
- en
- eo
- et
- eu
- ee
- fo
- fa
- tl
- fi
- fr
- fy
- ga
- gl
- gv
- gn
- gu
- ht
- ha
- he
- hi
- hr
- hu
- hy
- ig
- ia
- id
- is
- it
- jv
- ja
- kn
- ka
- kk
- km
- rw
- ky
- ku
- ko
- lo
- la
- lv
- ln
- lt
- lb
- lg
- ml
- mr
- mk
- mg
- mt
- mn
- mi
- ms
- my
- ne
- nl
- nn
- no
- oc
- or
- pa
- pl
- pt
- ps
- ro
- ru
- sa
- si
- sl
- sk
- sn
- sd
- so
- st
- es
- sq
- sc
- sr
- su
- sw
- sv
- ta
- tt
- te
- tg
- th
- tn
- tk
- tr
- tw
- ug
- uk
- ur
- uz
- vi
- xh
- yi
- yo
- zh
---
**This repository contains the best mHuBERT-147 pre-trained model.**

**MODEL DETAILS:** 3rd iteration, K=1000, HuBERT base architecture (95M parameters), 147 languages.

# Table of Contents:

1. [Summary](https://huggingface.co/utter-project/mHuBERT-147#mhubert-147-models)
2. [Training Data and Code](https://huggingface.co/utter-project/mHuBERT-147#training)
3. [ML-SUPERB Scores](https://huggingface.co/utter-project/mHuBERT-147#ml-superb-scores)
4. [Languages and Datasets](https://huggingface.co/utter-project/mHuBERT-147#languages-and-datasets)
6. [Citing and Funding Information](https://huggingface.co/utter-project/mHuBERT-147#citing-and-funding-information)
   
# mHuBERT-147 models

mHuBERT-147 are compact and competitive multilingual HuBERT models trained on 90K hours of open-license data in 147 languages. 
Different from *traditional* HuBERTs, mHuBERT-147 models are trained using faiss IVF discrete speech units. 
Training employs a two-level language, data source up-sampling during training. See more information in [our paper](https://arxiv.org/pdf/2406.06371).

**This repository contains:**
* Fairseq checkpoint (original);
* HuggingFace checkpoint (conversion using transformers library);
* Faiss index for continuous pre-training (OPQ16_64,IVF1000_HNSW32,PQ16x4fsr).

**Related Models:**
* [2nd Iteration mHuBERT-147](https://huggingface.co/utter-project/mHuBERT-147-base-2nd-iter)
* [1st Iteration mHuBERT-147](https://huggingface.co/utter-project/mHuBERT-147-base-1st-iter)
* [CommonVoice Prototype (12 languages)](https://huggingface.co/utter-project/hutter-12-3rd-base)

# Training

* **[Manifest list available here.](https://huggingface.co/utter-project/mHuBERT-147-base-3rd-iter/tree/main/manifest)** Please note that since training, there were CommonVoice removal requests. This means that some of the listed files are no longer available.

* **[Fairseq fork](https://github.com/utter-project/fairseq)** contains the scripts for training with multilingual batching with two-level up-sampling.

* **[Scripts for pre-processing/faiss clustering available here.](https://github.com/utter-project/mHuBERT-147-scripts)** 

# ML-SUPERB Scores

mHubert-147 reaches second and first position in the 10min and 1h leaderboards respectively. We achieve new SOTA scores for three LID tasks.
See more information in [our paper](https://arxiv.org/pdf/2406.06371).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/62262e19d36494a6f743a28d/chXjExnWc3rhhtdsyiU-W.png)

# Languages and Datasets

**Datasets:** For ASR/ST/TTS datasets, only train set is used.
* [Aishell](https://www.openslr.org/33/) and [AISHELL-3](https://www.openslr.org/93/)
* [BibleTTS](https://www.openslr.org/129/)
* [ClovaCall](https://github.com/clovaai/ClovaCall)
* [CommonVoice v11](https://commonvoice.mozilla.org/en/datasets)
* Google TTS data: [Javanese](https://www.openslr.org/41/), [Khmer](https://www.openslr.org/42/), [Nepali](https://www.openslr.org/43/), [Sundanese](https://www.openslr.org/44/), [South African Languages](https://www.openslr.org/32/), [Bengali Languages](https://www.openslr.org/37/)  
* IISc-MILE: [Tamil](https://www.openslr.org/127/), [Kannada](https://www.openslr.org/126/)
* [Japanese Versatile Speech](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvs_corpus) 
* [Kokoro](https://github.com/kaiidams/Kokoro-Speech-Dataset)
* [Kosp2e](https://github.com/warnikchow/kosp2e)
* Media Speech: [Turkish Only](https://www.openslr.org/108/)
* [Multilingual LibriSpeech](https://www.openslr.org/94/)
* [Samrómur](https://www.openslr.org/128/)
* [THCHS-30](https://www.openslr.org/18/) and [THUYG-20](https://www.openslr.org/22/)
* [VoxLingua107](https://bark.phon.ioc.ee/voxlingua107/)
* [VoxPopuli](https://github.com/facebookresearch/voxpopuli/)

**Languages present not indexed by Huggingface:** Asturian (ast), Basaa (bas), Cebuano (ceb), Central Kurdish/Sorani (ckb), Hakha Chin (cnh), Hawaiian (haw), Upper Sorbian (hsb) Kabyle (kab), Moksha (mdf), Meadow Mari (mhr), Hill Mari (mrj), Erzya (myv), Taiwanese Hokkien (nan-tw), Sursilvan (rm-sursilv), Vallader (rm-vallader), Sakha (sah), Santali (sat), Scots (sco), Saraiki (skr), Tigre (tig), Tok Pisin (tpi), Akwapen Twi (tw-akuapem), Asante Twi (tw-asante), Votic (vot), Waray (war), Cantonese (yue).


# Citing and Funding Information

```
@inproceedings{boito2024mhubert,
author={Marcely Zanon Boito, Vivek Iyer, Nikolaos Lagos, Laurent Besacier, Ioan Calapodescu},
title={{mHuBERT-147: A Compact Multilingual HuBERT Model}},
year=2024,
booktitle={Interspeech 2024},
}
```

<img src="https://cdn-uploads.huggingface.co/production/uploads/62262e19d36494a6f743a28d/HbzC1C-uHe25ewTy2wyoK.png" width=7% height=7%> 
This is an output of the European Project UTTER (Unified Transcription and Translation for Extended Reality) funded by European Union’s Horizon Europe Research and Innovation programme under grant agreement number 101070631.

For more information please visit https://he-utter.eu/

