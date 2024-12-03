---
pipeline_tag: object-detection
tags:
- vision
---
# Detection Transformers with Assignment

By [Jeffrey Ouyang-Zhang](https://jozhang97.github.io/),  [Jang Hyun Cho](https://sites.google.com/view/janghyuncho/), [Xingyi Zhou](https://www.cs.utexas.edu/~zhouxy/), [Philipp Krähenbühl](http://www.philkr.net/)

From the paper [NMS Strikes Back](https://arxiv.org/abs/2212.06137).


**TL; DR.** **De**tection **T**ransformers with **A**ssignment (DETA) re-introduce IoU assignment and NMS for transformer-based detectors. DETA trains and tests comparibly as fast as Deformable-DETR and converges much faster (50.2 mAP in 12 epochs on COCO).