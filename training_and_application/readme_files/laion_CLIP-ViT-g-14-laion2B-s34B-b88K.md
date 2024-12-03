---
tags:
- zero-shot-image-classification
- clip
library_tag: open_clip
license: mit
pipeline_tag: zero-shot-image-classification
---
# Model card for CLIP-ViT-g-14-laion2B-s34B-b88K


#  Table of Contents

1. [Model Details](#model-details)
2. [Uses](#uses)
3. [Training Details](#training-details)
4. [Evaluation](#evaluation)
5. [Acknowledgements](#acknowledgements) 
6. [Citation](#citation)
7. [How To Get Started With the Model](#how-to-get-started-with-the-model)


# Model Details

## Model Description

A CLIP ViT-g/14 model trained with the LAION-2B English subset of LAION-5B (https://laion.ai/blog/laion-5b/, https://openreview.net/forum?id=M3Y74vmsMcY) using OpenCLIP (https://github.com/mlfoundations/open_clip).

Model training done by Jenia Jitsev on [JUWELS Booster](https://apps.fz-juelich.de/jsc/hps/juwels/booster-overview.html) at [Juelich Supercomputing Center](https://www.fz-juelich.de/en/ias/jsc) and on the [stability.ai](https://stability.ai/) AWS HPC cluster. 
Training performed in frame of reproducible scaling law studies, published as [research paper at CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Cherti_Reproducible_Scaling_Laws_for_Contrastive_Language-Image_Learning_CVPR_2023_paper.html). See also the [research repository](https://github.com/LAION-AI/scaling-laws-openclip)

# Uses

As per the original [OpenAI CLIP model card](https://github.com/openai/CLIP/blob/d50d76daa670286dd6cacf3bcd80b5e4823fc8e1/model-card.md), this model is intended as a research output for research communities. We hope that this model will enable researchers to better understand and explore zero-shot, arbitrary image classification. We also hope it can be used for interdisciplinary studies of the potential impact of such model. 

The OpenAI CLIP paper includes a discussion of potential downstream impacts to provide an example for this sort of analysis. Additionally, the LAION-5B blog (https://laion.ai/blog/laion-5b/) and [LAION-5B NeurIPS paper](https://openreview.net/forum?id=M3Y74vmsMcY) include additional discussion as it relates specifically to the training dataset. 

## Direct Use

Zero-shot image classification, image and text retrieval, among others.

## Downstream Use

Image classification and other image task fine-tuning, linear probe image classification, image generation guiding and conditioning, among others.

## Out-of-Scope Use

As per the OpenAI models,

**Any** deployed use case of the model - whether commercial or not - is currently out of scope. Non-deployed use cases such as image search in a constrained environment, are also not recommended unless there is thorough in-domain testing of the model with a specific, fixed class taxonomy. This is because our safety assessment demonstrated a high need for task specific testing especially given the variability of CLIP’s performance with different class taxonomies. This makes untested and unconstrained deployment of the model in any use case currently potentially harmful. 

Certain use cases which would fall under the domain of surveillance and facial recognition are always out-of-scope regardless of performance of the model. This is because the use of artificial intelligence for tasks such as these can be premature currently given the lack of testing norms and checks to ensure its fair use.

Since the model has not been purposefully trained in or evaluated on any languages other than English, its use should be limited to English language use cases.

Further the above notice, the LAION-5B dataset used in training of these models has additional considerations, see below.

# Training Details

## Training Data

This model was trained with the 2 Billion sample English subset of LAION-5B (https://laion.ai/blog/laion-5b/).

**IMPORTANT NOTE:** The motivation behind dataset creation is to democratize research and experimentation around large-scale multi-modal model training and handling of uncurated, large-scale datasets crawled from publically available internet. Our recommendation is therefore to use the dataset for research purposes. Be aware that this large-scale dataset is uncurated. Keep in mind that the uncurated nature of the dataset means that collected links may lead to strongly discomforting and disturbing content for a human viewer. Therefore, please use the demo links with caution and at your own risk. It is possible to extract a “safe” subset by filtering out samples based on the safety tags (using a customized trained NSFW classifier that we built). While this strongly reduces the chance for encountering potentially harmful content when viewing, we cannot entirely exclude the possibility for harmful content being still present in safe mode, so that the warning holds also there. We think that providing the dataset openly to broad research and other interested communities will allow for transparent investigation of benefits that come along with training large-scale models as well as pitfalls and dangers that may stay unreported or unnoticed when working with closed large datasets that remain restricted to a small community. Providing our dataset openly, we however do not recommend using it for creating ready-to-go industrial products, as the basic research about general properties and safety of such large-scale models, which we would like to encourage with this release, is still in progress.

## Training Procedure

OpenCLIP ViT-g/14 model was trained on 34.5B samples (135M * 256 checkpoints) from laion2b-en (part of LAION-5B) dataset. Warmup = 13.5k steps, learning rate = 1e-3, cosine annealing schedule, weight decay = 0.2. Global batch size = 88800, number of GPUs = 1480, local batch size = 60

# Evaluation

Evaluation done with code in the [LAION CLIP Benchmark suite](https://github.com/LAION-AI/CLIP_benchmark).

## Testing Data, Factors & Metrics

### Testing Data

The testing is performed with VTAB+ (A combination of VTAB (https://arxiv.org/abs/1910.04867) w/ additional robustness datasets) for classification and COCO and Flickr for retrieval.

**TODO** - more detail

## Results

The model achieves a 78.4 zero-shot top-1 accuracy on ImageNet-1k.

An initial round of benchmarks have been performed on a wider range of datasets, currently viewable at https://github.com/LAION-AI/CLIP_benchmark/blob/main/benchmark/results.ipynb

**TODO** - create table for just this model's metrics.

# Acknowledgements

We gratefully acknowledge the Gauss Centre for Supercomputing e.V. (www.gauss-centre.eu) for funding the work by providing computing time through the John von Neumann Institute for Computing (NIC) on the GCS Supercomputer [JUWELS Booster](https://apps.fz-juelich.de/jsc/hps/juwels/booster-overview.html) at Jülich Supercomputing Centre (JSC) 
We also acknowledge storage resources on JUST granted and operated by JSC, as well as computing resources from the Helmholtz Data Federation (HDF).
We further acknowledge [stability.ai](https://stability.ai/) providing additional compute used to train this model.

# Citation

**BibTeX:**

Please cite:

LAION-5B paper
```
@inproceedings{Schuhmann2022,
title={{LAION}-5{B}: An open large-scale dataset for training next generation image-text models},
author={Christoph Schuhmann and Romain Beaumont and Richard Vencu and Cade W Gordon and Ross Wightman and Mehdi Cherti and Theo Coombes and Aarush Katta and Clayton Mullis and Mitchell Wortsman and Patrick Schramowski and Srivatsa R Kundurthy and Katherine Crowson and Ludwig Schmidt and Robert Kaczmarczyk and Jenia Jitsev},
booktitle={Thirty-sixth Conference on Advances in Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks Track},
year={2022},
volume={35},
pages={25278--25294},
url={https://openreview.net/forum?id=M3Y74vmsMcY}
}
```

Reproducible scaling laws for openCLIP paper
```
@inproceedings{Cherti2023,
  title={Reproducible scaling laws for contrastive language-image learning},
  author={Cherti, Mehdi and Beaumont, Romain and Wightman, Ross and Wortsman, Mitchell and Ilharco, Gabriel and Gordon, Cade and Schuhmann, Christoph and Schmidt, Ludwig and Jitsev, Jenia},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={2818--2829},
  year={2023}
}
```

OpenAI CLIP paper
```
@inproceedings{Radford2021LearningTV,
  title={Learning Transferable Visual Models From Natural Language Supervision},
  author={Alec Radford and Jong Wook Kim and Chris Hallacy and A. Ramesh and Gabriel Goh and Sandhini Agarwal and Girish Sastry and Amanda Askell and Pamela Mishkin and Jack Clark and Gretchen Krueger and Ilya Sutskever},
  booktitle={ICML},
  year={2021}
}
```

OpenCLIP software
```
@software{ilharco_gabriel_2021_5143773,
  author       = {Ilharco, Gabriel and
                  Wortsman, Mitchell and
                  Wightman, Ross and
                  Gordon, Cade and
                  Carlini, Nicholas and
                  Taori, Rohan and
                  Dave, Achal and
                  Shankar, Vaishaal and
                  Namkoong, Hongseok and
                  Miller, John and
                  Hajishirzi, Hannaneh and
                  Farhadi, Ali and
                  Schmidt, Ludwig},
  title        = {OpenCLIP},
  month        = jul,
  year         = 2021,
  note         = {If you use this software, please cite it as below.},
  publisher    = {Zenodo},
  version      = {0.1},
  doi          = {10.5281/zenodo.5143773},
  url          = {https://doi.org/10.5281/zenodo.5143773}
}
```

# How to Get Started with the Model

Use the code below to get started with the model.

** TODO ** - Hugging Face transformers, OpenCLIP, and timm getting started snippets