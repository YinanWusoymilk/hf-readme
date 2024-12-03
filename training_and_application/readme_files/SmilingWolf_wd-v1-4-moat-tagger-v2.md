---
license: apache-2.0
---
# WD 1.4 MOAT Tagger V2

Supports ratings, characters and general tags.

Trained using https://github.com/SmilingWolf/SW-CV-ModelZoo.  
TPUs used for training kindly provided by the [TRC program](https://sites.research.google/trc/about/).

## Dataset
Last image id: 5944504  
Trained on Danbooru images with IDs modulo 0000-0899.  
Validated on images with IDs modulo 0950-0999.  
Images with less than 10 general tags were filtered out.  
Tags with less than 600 images were filtered out.

## Validation results
`P=R: threshold = 0.3771, F1 = 0.6911`

## Paper
[`MOAT: Alternating Mobile Convolution and Attention Brings Strong Vision Models`](https://arxiv.org/abs/2210.01820)

## Final words
Subject to change and updates.  
Downstream users are encouraged to use tagged releases rather than relying on the head of the repo.
