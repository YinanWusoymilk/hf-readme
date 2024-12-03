---
license: other
tags:
- vision
- image-segmentation
- generated_from_trainer
widget:
- src: >-
    https://media.istockphoto.com/id/515788534/photo/cheerful-and-confidant.jpg?s=612x612&w=0&k=20&c=T0Z4DfameRpyGhzevPomrm-wjZp7wmGjpAyjGcTzpkA=
  example_title: Person
- src: >-
    https://storage.googleapis.com/pai-images/1484fd9ea9d746eb9f1de0d6778dbea2.jpeg
  example_title: Person
datasets:
- sayeed99/fashion_segmentation
model-index:
- name: segformer-b3-fashion
  results: []
pipeline_tag: image-segmentation
---


# segformer-b3-fashion

This model is a fine-tuned version of [nvidia/mit-b3](https://huggingface.co/nvidia/mit-b3) on the sayeed99/fashion_segmentation dataset using original image sizes without resizing.


```python
from transformers import SegformerImageProcessor, AutoModelForSemanticSegmentation
from PIL import Image
import requests
import matplotlib.pyplot as plt
import torch.nn as nn

processor = SegformerImageProcessor.from_pretrained("sayeed99/segformer-b3-fashion")
model = AutoModelForSemanticSegmentation.from_pretrained("sayeed99/segformer-b3-fashion")

url = "https://plus.unsplash.com/premium_photo-1673210886161-bfcc40f54d1f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8cGVyc29uJTIwc3RhbmRpbmd8ZW58MHx8MHx8&w=1000&q=80"

image = Image.open(requests.get(url, stream=True).raw)
inputs = processor(images=image, return_tensors="pt")

outputs = model(**inputs)
logits = outputs.logits.cpu()

upsampled_logits = nn.functional.interpolate(
    logits,
    size=image.size[::-1],
    mode="bilinear",
    align_corners=False,
)

pred_seg = upsampled_logits.argmax(dim=1)[0]
plt.imshow(pred_seg)
```

Labels : {"0":"Unlabelled", "1": "shirt, blouse", "2": "top, t-shirt, sweatshirt", "3": "sweater", "4": "cardigan", "5": "jacket", "6": "vest", "7": "pants", "8": "shorts", "9": "skirt", "10": "coat", "11": "dress", "12": "jumpsuit", "13": "cape", "14": "glasses", "15": "hat", "16": "headband, head covering, hair accessory", "17": "tie", "18": "glove", "19": "watch", "20": "belt", "21": "leg warmer", "22": "tights, stockings", "23": "sock", "24": "shoe", "25": "bag, wallet", "26": "scarf", "27": "umbrella", "28": "hood", "29": "collar", "30": "lapel", "31": "epaulette", "32": "sleeve", "33": "pocket", "34": "neckline", "35": "buckle", "36": "zipper", "37": "applique", "38": "bead", "39": "bow", "40": "flower", "41": "fringe", "42": "ribbon", "43": "rivet", "44": "ruffle", "45": "sequin", "46": "tassel"}

### Framework versions

- Transformers 4.30.0
- Pytorch 2.2.2+cu121
- Datasets 2.18.0
- Tokenizers 0.13.3


### License

The license for this model can be found [here](https://github.com/NVlabs/SegFormer/blob/master/LICENSE).

### BibTeX entry and citation info

```bibtex
@article{DBLP:journals/corr/abs-2105-15203,
  author    = {Enze Xie and
               Wenhai Wang and
               Zhiding Yu and
               Anima Anandkumar and
               Jose M. Alvarez and
               Ping Luo},
  title     = {SegFormer: Simple and Efficient Design for Semantic Segmentation with
               Transformers},
  journal   = {CoRR},
  volume    = {abs/2105.15203},
  year      = {2021},
  url       = {https://arxiv.org/abs/2105.15203},
  eprinttype = {arXiv},
  eprint    = {2105.15203},
  timestamp = {Wed, 02 Jun 2021 11:46:42 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2105-15203.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}