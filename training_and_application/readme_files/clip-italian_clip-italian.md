---
language: it
license: gpl-3.0
datasets:
- wit
- ctl/conceptualCaptions
- mscoco-it
tags:
- italian
- bert
- vit
- vision
---

# Italian CLIP

Paper: [Contrastive Language-Image Pre-training for the Italian Language](https://arxiv.org/abs/2108.08688)

With a few tricks, we have been able to fine-tune a competitive Italian CLIP model with **only 1.4 million** training samples. Our Italian CLIP model is built upon the [Italian BERT](https://huggingface.co/dbmdz/bert-base-italian-xxl-cased) model provided by [dbmdz](https://huggingface.co/dbmdz) and the OpenAI [vision transformer](https://huggingface.co/openai/clip-vit-base-patch32).

Do you want to test our model right away? We got you covered! You just need to head to our [demo application](https://huggingface.co/spaces/clip-italian/clip-italian-demo).
The demo also contains all the details of the project, from training tricks to our most impressive results, and much more!

# Training data

We considered four main sources of data:

+ [WIT](https://github.com/google-research-datasets/wit) is an image-caption dataset collected from Wikipedia (see, 
[Srinivasan et al., 2021](https://arxiv.org/pdf/2103.01913.pdf)).

+ [MSCOCO-IT](https://github.com/crux82/mscoco-it). This image-caption dataset comes from the work by [Scaiella et al., 2019](http://www.ai-lc.it/IJCoL/v5n2/IJCOL_5_2_3___scaiella_et_al.pdf).

+ [Conceptual Captions](https://ai.google.com/research/ConceptualCaptions/). This image-caption dataset comes from 
the work by [Sharma et al., 2018](https://aclanthology.org/P18-1238.pdf).

+ [La Foto del Giorno](https://www.ilpost.it/foto-del-giorno/). This image-caption dataset is collected from [Il Post](https://www.ilpost.it/), a prominent Italian online newspaper.

We used better data augmentation, strategic training choices (we have way less data than the original CLIP paper), and backbone-freezing pre-training. For all the details on that, please refer to our [demo](https://huggingface.co/spaces/clip-italian/clip-italian-demo).

# Experiments

## Quantitative Evaluation

To better understand how well our clip-italian model works we run an experimental evaluation. Since this is the first clip-based model in Italian, we used the multilingual CLIP model as a comparison baseline. 

### mCLIP

The multilingual CLIP (henceforth, mCLIP), is a model introduced by [Nils Reimers](https://www.sbert.net/docs/pretrained_models.html) in his
[sentence-transformer](https://www.sbert.net/index.html) library. mCLIP is based on a multilingual encoder
that was created through multilingual knowledge distillation (see [Reimers et al., 2020](https://aclanthology.org/2020.emnlp-main.365/)).

### Tasks

We selected two different tasks: 
+ image-retrieval 
+ zero-shot classification

### Reproducibiliy

Both experiments should be very easy to replicate, we share the two colab notebook we used to compute the two results

+ [Image Retrieval](https://colab.research.google.com/drive/1bLVwVKpAndpEDHqjzxVPr_9nGrSbuOQd?usp=sharing)
+ [ImageNet Zero Shot Evaluation](https://colab.research.google.com/drive/1zfWeVWY79XXH63Ci-pk8xxx3Vu_RRgW-?usp=sharing)


### Image Retrieval

This experiment is run against the MSCOCO-IT validation set (that we haven't used in training). Given in input
a caption, we search for the most similar image in the MSCOCO-IT validation set. As evaluation metrics
we use the MRR@K.

| MRR             | CLIP-Italian | mCLIP |
| --------------- | ------------ |-------|
| MRR@1           | **0.3797**   | 0.2874|   
| MRR@5           | **0.5039**   | 0.3957|
| MRR@10          | **0.5204**   | 0.4129|

It is true that we used MSCOCO-IT in training, and this might give us an advantage. However the original CLIP model was trained
on 400million images (and some of them probably were from MSCOCO).


### Zero-shot image classification

This experiment replicates the original one run by OpenAI on zero-shot image classification on ImageNet. 
To do this, we used DeepL to translate the image labels in ImageNet. We evaluate the models computing the accuracy at different levels. 


| Accuracy        | CLIP-Italian | mCLIP |
| --------------- | ------------ |-------|
| Accuracy@1      |  **22.11**   | 20.15 |   
| Accuracy@5      |  **43.69**   | 36.57 |
| Accuracy@10     |  **52.55**   | 42.91 |
| Accuracy@100    |  **81.08**   | 67.11 |

Our results confirm that CLIP-Italian is very competitive and beats mCLIP on the two different task
we have been testing. Note, however, that our results are lower than those shown in the original OpenAI
paper (see, [Radford et al., 2021](https://arxiv.org/abs/2103.00020)). However, considering that our results are in line with those obtained by mCLIP we think that 
the translated image labels might have had an impact on the final scores.


# Team members
- Federico Bianchi ([vinid](https://huggingface.co/vinid))
- Raphael Pisoni ([4rtemi5](https://huggingface.co/4rtemi5))
- Giuseppe Attanasio ([g8a9](https://huggingface.co/g8a9))
- Silvia Terragni ([silviatti](https://huggingface.co/silviatti))
- Dario Balestri ([D3Reo](https://huggingface.co/D3Reo))
- Gabriele Sarti ([gsarti](https://huggingface.co/gsarti))
- Sri Lakshmi ([srisweet](https://huggingface.co/srisweet))