---
license: mit
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/cat-dog-music.png
  candidate_labels: playing music, playing sports
  example_title: Cat & Dog
---
# Model Card for CLIP ViT-H/14 frozen xlm roberta large - LAION-5B

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

A CLIP ViT-H/14 frozen xlm roberta large model trained with the LAION-5B (https://laion.ai/blog/laion-5b/) using OpenCLIP (https://github.com/mlfoundations/open_clip).

Model training done by Romain Beaumont on the [stability.ai](https://stability.ai/) cluster. 

# Uses

## Direct Use

Zero-shot image classification, image and text retrieval, among others.

## Downstream Use

Image classification and other image task fine-tuning, linear probe image classification, image generation guiding and conditioning, among others.

# Training Details

## Training Data

This model was trained with the full LAION-5B (https://laion.ai/blog/laion-5b/).

## Training Procedure

Training with batch size 90k for 13B sample of laion5B, see https://wandb.ai/rom1504/open-clip/reports/xlm-roberta-large-unfrozen-vit-h-14-frozen--VmlldzoyOTc3ODY3

Model is H/14 on visual side, xlm roberta large initialized with pretrained weights on text side.

The H/14 was initialized from https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K and kept frozen during training.

# Evaluation

Evaluation done with code in the [LAION CLIP Benchmark suite](https://github.com/LAION-AI/CLIP_benchmark).

## Testing Data, Factors & Metrics

### Testing Data

The testing is performed with VTAB+ (A combination of VTAB (https://arxiv.org/abs/1910.04867) w/ additional robustness datasets) for classification and COCO and Flickr for retrieval.

## Results

The model achieves imagenet 1k 77.0% (vs 78% for the english H/14)
![results_xlm_roberta_large.png](results_xlm_roberta_large.png)

On zero shot classification on imagenet with translated prompts this model reaches:
* 56% in italian (vs 21% for https://github.com/clip-italian/clip-italian)
* 53% in japanese (vs 54.6% for https://github.com/rinnakk/japanese-clip)
* 55.7% in chinese (to be compared with https://github.com/OFA-Sys/Chinese-CLIP)

This model reaches strong results in both english and other languages.


# Acknowledgements

Acknowledging [stability.ai](https://stability.ai/) for the compute used to train this model.

# Citation

**BibTeX:**

In addition to forthcoming LAION-5B (https://laion.ai/blog/laion-5b/) paper, please cite:

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

# How To Get Started With the Model

https://github.com/mlfoundations/open_clip