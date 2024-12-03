---
tags:
- zero-shot-image-classification
- clip
library_tag: open_clip
license: mit
library_name: open_clip
pipeline_tag: zero-shot-image-classification
---
# Model card for CLIP-convnext_xxlarge-laion2B-s34B-b82K-augreg-soup

#  Table of Contents

1. [Model Details](#model-details)
2. [Uses](#uses)
3. [Training Details](#training-details)
4. [Evaluation](#evaluation)
5. [Acknowledgements](#acknowledgements)
6. [Citation](#citation)

# Model Details

## Model Description

A series of CLIP ConvNeXt-XXLarge (a custom `timm` ConvNeXt size) models trained on LAION-2B (english), a subset of [LAION-5B](https://arxiv.org/abs/2210.08402), using [OpenCLIP](https://github.com/mlfoundations/open_clip).

| Model | Dataset | Resolution | AugReg | Top-1 ImageNet Zero-Shot (%) |
| ----- | ------- | ---------- | ------------ | --------- |
| [convnext_xxlarge.laion2b_s34b_b82k-augreg](https://huggingface.co/laion/CLIP-convnext_xxlarge-laion2B-s34B-b82K-augreg) | LAION-2B | 256x256 |  RRC (0.33, 1.0), RE (0.35), SD (0.1) | 79.1 |
| [convnext_xxlarge.laion2b_s34b_b82k-augreg-rewind](https://huggingface.co/laion/CLIP-convnext_xxlarge-laion2B-s34B-b82K-augreg-rewind) | LAION-2B | 256x256 |  RRC (0.3, 1.0), RE (0.4), SD (0.1) | 79.3 |
| [convnext_xxlarge.laion2b_s34b_b82k-augreg-soup](https://huggingface.co/laion/CLIP-convnext_xxlarge-laion2B-s34B-b82K-augreg-soup) | LAION-2B | 256x256 |  N/A | 79.4 |
RRC = Random Resize Crop (crop pcts), RE = Random Erasing (prob), SD = Stochastic Depth (prob) -- image tower only

The core training run was performed in pieces over a period of ~ 2 months. The global batch size for the core run was 81920. The last ~10% of training was re-done at a 95744 global batch size w/ higher LR and aug than original finish. The two were averaged together in a 'soup'. See more details in [Training Details](#training-details).

Goals:
  * Push the size of largest convolutional CLIP image tower into the performance range of ViT-g to ViT-G w/ improved image size scaling for downstream use.

Firsts:
  * Largest released ConvNeXt model pretrained (847M params w/ 198 GMAC and 125 MActs @ 256x256 for image)
  * A non-ViT image tower CLIP model (with no previous image tower pretrain) achieving > 79% ImageNet top-1 zero-shot

The models utilize:
  * the [timm](https://github.com/rwightman/pytorch-image-models) ConvNeXt-XXLarge model (`convnext_xxlarge`) as the image tower
  * a standard projection at end of image tower
  * a text tower with same size (with 1024, heads 16, depth 24) as ViT-H-14 and ViT-g-14 models


The models are trained at 256x256 image resolution. The size of the combined image + text CLIP model is 1.2B params w/ 222 GMAC and 146 MActs. At 256x256, the ConvNext-XXLarge sits just above a ViT-H-14 CLIP configuration in FLOPS and params while being lower in activation counts. It is well under both g-14 and G-14 while being between them in capabilities.

|model                     |image_size|embed_dim|gmacs |macts |mparams|image_gmacs|image_macts|image_mparams|text_gmacs|text_macts|text_mparams|
|--------------------------|----------|---------|------|------|-------|-----------|-----------|-------------|----------|----------|------------|
|ViT-H-16                  |224       |1024     |150.96|122.01|986.26 |127.4      |100.81     |632.23       |23.57     |21.2      |354.03      |
|ViT-H-14                  |224       |1024     |190.97|160.61|986.11 |167.4      |139.41     |632.08       |23.57     |21.2      |354.03      |
|ViT-L-14-336              |336       |768      |197.76|278.19|427.94 |191.1      |270.24     |304.29       |6.66      |7.95      |123.65      |
|convnext_xxlarge          |256       |1024     |221.66|145.66|1200.58|198.09     |124.45     |846.54       |23.57     |21.2      |354.03      |
|RN50x64                   |448       |1024     |276.8 |249.73|623.26 |265.02     |239.13     |420.38       |11.78     |10.6      |202.88      |
|ViT-g-14                  |224       |1024     |290.74|213.84|1366.68|267.18     |192.64     |1012.65      |23.57     |21.2      |354.03      |
|convnext_xxlarge_320      |320       |1024     |333.08|215.66|1200.58|309.52     |194.46     |846.54       |23.57     |21.2      |354.03      |
|ViT-H-14-336              |336       |1024     |414.53|428.74|986.52 |390.97     |407.54     |632.49       |23.57     |21.2      |354.03      |
|ViT-bigG-14               |224       |1280     |532.92|310.71|2539.57|483.96     |275.37     |1844.91      |48.96     |35.34     |694.66      |


Model training done by Ross Wightman across both the [stability.ai](https://stability.ai/) cluster and the [JUWELS Booster](https://apps.fz-juelich.de/jsc/hps/juwels/booster-overview.html) supercomputer. See acknowledgements below.

# Uses

As per the original [OpenAI CLIP model card](https://github.com/openai/CLIP/blob/d50d76daa670286dd6cacf3bcd80b5e4823fc8e1/model-card.md), this model is intended as a research output for research communities. We hope that this model will enable researchers to better understand and explore zero-shot, arbitrary image classification. We also hope it can be used for interdisciplinary studies of the potential impact of such model. 

The OpenAI CLIP paper includes a discussion of potential downstream impacts to provide an example for this sort of analysis. Additionally, the LAION-5B blog (https://laion.ai/blog/laion-5b/) and upcoming paper include additional discussion as it relates specifically to the training dataset. 

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

This model was trained with LAION-2B -- A 2 billion sample English subset of LAION-5B (https://laion.ai/blog/laion-5b/).

**IMPORTANT NOTE:** The motivation behind dataset creation is to democratize research and experimentation around large-scale multi-modal model training and handling of uncurated, large-scale datasets crawled from publically available internet. Our recommendation is therefore to use the dataset for research purposes. Be aware that this large-scale dataset is uncurated. Keep in mind that the uncurated nature of the dataset means that collected links may lead to strongly discomforting and disturbing content for a human viewer. Therefore, please use the demo links with caution and at your own risk. It is possible to extract a “safe” subset by filtering out samples based on the safety tags (using a customized trained NSFW classifier that we built). While this strongly reduces the chance for encountering potentially harmful content when viewing, we cannot entirely exclude the possibility for harmful content being still present in safe mode, so that the warning holds also there. We think that providing the dataset openly to broad research and other interested communities will allow for transparent investigation of benefits that come along with training large-scale models as well as pitfalls and dangers that may stay unreported or unnoticed when working with closed large datasets that remain restricted to a small community. Providing our dataset openly, we however do not recommend using it for creating ready-to-go industrial products, as the basic research about general properties and safety of such large-scale models, which we would like to encourage with this release, is still in progress.

## Training Procedure

The main training run was done at global batch size of 81920 for 256 checkpoint intervals of 135.6M samples for a total of ~34B samples seen over training.

Many difficulties w/ both model numerical stability and cluster stability and performance were encountered while training this model. Initial attempts to train with float16 AMP and default adam beta2 resulted in loss spikes and eventually NaN blow ups. `beta2` was reduced to 0.97 which helped, but the loss / zs curves were not tracking as expected. After switching to PyTorch nightlies, it was possible to use bfloat16 + AMP for training (as with rececnt H/14, g/14, and G/14 models), beta2 was returned to 0.98 and metrics improved.

|Checkpoint Interval |Cluster   |# GPUs|# Nodes|GPU       |local BS|sample/s|sample/s/gpu|precision |adam beta2 |
|--------------------|----------|------|-------|----------|--------|--------|------------|----------|-----------|
|1 - 2               |Stability |1024  |128    |A100 40GB | 80     |37-40k  | 36-39      |amp + fp16|0.97       |
|3 - 32              |Stability |512   |64     |A100 80GB | 160    |27-32k  | 52-62      |amp + fp16|0.97       |
|33 - 75             |Booster   |1024  |256    |A100 40GB | 80     |48k     | 47         |amp + fp16|0.97       |
|76 - 165            |Booster   |1024  |256    |A100 40GB | 80     |51k     | 50         |amp + bf16|0.98       |
|166 - 232           |Stability |320   |40     |A100 80GB | 256    |18-19k  | 56-59      |amp + bf16|0.98       |
|233 - 249           |Booster   |1024  |256    |A100 40GB | 80     |51k     | 50         |amp + bf16|0.98       |
|250 - 256           |Stability |1024  |128    |A100 40GB | 80     |27-31k  | 26-30      |amp + bf16|0.98       |

JUWELS Booster has 4x A100 GPU per node w/ 4x HDR-200 IB adapters per node (200Gbit/sec per GPU). Stability setup used was 8x A100 GPU per node w/ 400Gbit/sec EFA networking per node (50 GBit/sec per GPU). Significant variation in training efficiency (throughput per GPU) as observed across the various configurations. The 1024 GPU configurations across both clusters were particularly prone to crashing (or very difficult to get running w/ a 'good' set of GPUs).

A slurm srun command line below for a 128 8-GPU (40GB A100) configuration:

```
srun --cpu_bind=v --accel-bind=gn python -m training.main \
    --save-frequency 1 \
    --name "xxlarge-2b-81920-bf16" \
    --resume "latest" \
    --logs "/runs" \
    --log-every-n-steps 50 \
    --train-data="pipe:aws s3 cp s3://laion5b/laion2B-data/{000000..231349}.tar -" \
    --train-num-samples 135646078 \
    --dataset-type webdataset \
    --warmup 10000 \
    --batch-size=80 \
    --epochs=256 \
    --dataset-resampled \
    --aug-cfg use_timm=True scale='(0.33, 1.0)' re_prob=0.35 \
    --precision amp_bfloat16 \
    --grad-clip-norm 5.0 \
    --lr 1e-3 \
    --workers=6 \
    --beta2 0.98 \
    --model "convnext_xxlarge" \
    --seed 0 \
    --ddp-static-graph \
    --local-loss \
    --gather-with-grad \
    --grad-checkpointing \
    --report-to "tensorboard"
```

For the rewind of last 10%, a higher global batch size of 95744 was used w/ a higher LR and slightly increased augmentation strength.

|Checkpoint Interval |Cluster  |# GPUs|# Nodes|GPU       |local BS|sample/s|sample/s/gpu|precision |adam beta2 |
|--------------------|---------|------|-------|----------|--------|--------|------------|----------|-----------|
|231 - 256           |stability|1088  |136    |A100 40GB | 88     |32-35k  | 29-32      |amp + bf16|0.98       |

The slurm srun command line for 136 8-GPU (40GB A100) nodes:
```
srun --cpu_bind=v --accel-bind=gn python -m training.main \
    --save-frequency 1 \
    --name "xxlarge-2b-81920-r-bf16" \
    --resume "latest" \
    --logs "/runs" \
    --log-every-n-steps 50 \
    --train-data="pipe:aws s3 cp s3://laion5b/laion2B-data/{000000..231349}.tar -" \
    --train-num-samples 135646078 \
    --dataset-type webdataset \
    --warmup 10000 \
    --batch-size=88 \
    --epochs=256 \
    --dataset-resampled \
    --aug-cfg use_timm=True scale='(0.3, 1.0)' re_prob=0.4 \
    --precision amp_bfloat16 \
    --grad-clip-norm 5.0 \
    --lr 2e-3 \
    --workers=6 \
    --beta2 0.98 \
    --model "convnext_xxlarge" \
    --seed 0 \
    --ddp-static-graph \
    --local-loss \
    --gather-with-grad \
    --grad-checkpointing \
    --report-to "tensorboard"
```

# Evaluation

Evaluation done with code in the [LAION CLIP Benchmark suite](https://github.com/LAION-AI/CLIP_benchmark).

## Testing Data, Factors & Metrics

### Testing Data

The testing is performed with VTAB+ (A combination of VTAB (https://arxiv.org/abs/1910.04867) w/ additional robustness datasets) for classification and COCO and Flickr for retrieval.

## Results

These models achieve between 79.1 and 79.4 top-1 zero-shot accuracy on ImageNet-1k.

![](convnext_xxlarge_zero_shot.png)

A zoom-in on final 10% w/ rewind:

![](convnext_xxlarge_zero_shot_zoom.png)

An initial round of benchmarks have been performed on a wider range of datasets, to be viewable at https://github.com/LAION-AI/CLIP_benchmark/blob/main/benchmark/results.ipynb

# Acknowledgements

Acknowledging [stability.ai](https://stability.ai/) and the Gauss Centre for Supercomputing e.V. (http://gauss-centre.eu) for funding this part of work by providing computing time through the John von Neumann Institute for Computing (NIC) on the GCS Supercomputer JUWELS Booster at Jülich Supercomputing Centre (JSC).

# Citation

**BibTeX:**

LAION-5B
```bibtex
@inproceedings{schuhmann2022laionb,
  title={{LAION}-5B: An open large-scale dataset for training next generation image-text models},
  author={Christoph Schuhmann and
          Romain Beaumont and
          Richard Vencu and
          Cade W Gordon and
          Ross Wightman and
          Mehdi Cherti and
          Theo Coombes and
          Aarush Katta and
          Clayton Mullis and
          Mitchell Wortsman and
          Patrick Schramowski and
          Srivatsa R Kundurthy and
          Katherine Crowson and
          Ludwig Schmidt and
          Robert Kaczmarczyk and
          Jenia Jitsev},
  booktitle={Thirty-sixth Conference on Neural Information Processing Systems Datasets and Benchmarks Track},
  year={2022},
  url={https://openreview.net/forum?id=M3Y74vmsMcY}
}
```

OpenCLIP software
```bibtex
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

OpenAI CLIP paper
```bibtex
@inproceedings{Radford2021LearningTV,
  title={Learning Transferable Visual Models From Natural Language Supervision},
  author={Alec Radford and Jong Wook Kim and Chris Hallacy and A. Ramesh and Gabriel Goh and Sandhini Agarwal and Girish Sastry and Amanda Askell and Pamela Mishkin and Jack Clark and Gretchen Krueger and Ilya Sutskever},
  booktitle={ICML},
  year={2021}
}
```

```bibtex
@Article{liu2022convnet,
  author  = {Zhuang Liu and Hanzi Mao and Chao-Yuan Wu and Christoph Feichtenhofer and Trevor Darrell and Saining Xie},
  title   = {A ConvNet for the 2020s},
  journal = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year    = {2022},
}
```

```bibtex
@misc{rw2019timm,
  author = {Ross Wightman},
  title = {PyTorch Image Models},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  doi = {10.5281/zenodo.4414861},
  howpublished = {\url{https://github.com/rwightman/pytorch-image-models}}
}
```

```
@InProceedings{pmlr-v162-wortsman22a,
  title = 	 {Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time},
  author =       {Wortsman, Mitchell and Ilharco, Gabriel and Gadre, Samir Ya and Roelofs, Rebecca and Gontijo-Lopes, Raphael and Morcos, Ari S and Namkoong, Hongseok and Farhadi, Ali and Carmon, Yair and Kornblith, Simon and Schmidt, Ludwig},
  booktitle = 	 {Proceedings of the 39th International Conference on Machine Learning},
  pages = 	 {23965--23998},
  year = 	 {2022},
  editor = 	 {Chaudhuri, Kamalika and Jegelka, Stefanie and Song, Le and Szepesvari, Csaba and Niu, Gang and Sabato, Sivan},
  volume = 	 {162},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {17--23 Jul},
  publisher =    {PMLR},
  pdf = 	 {https://proceedings.mlr.press/v162/wortsman22a/wortsman22a.pdf},
  url = 	 {https://proceedings.mlr.press/v162/wortsman22a.html}
}
```