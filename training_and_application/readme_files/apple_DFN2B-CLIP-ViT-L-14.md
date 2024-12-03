---
license: other
license_name: apple-sample-code-license
license_link: LICENSE
---

A CLIP (Contrastive Language-Image Pre-training) model trained on DFN-2B. 
Data Filtering Networks (DFNs) are small networks used to automatically filter large pools of uncurated data. 
This model was trained on 2B images that were filtered from a pool of 12.8B uncurated image-text pairs 
(12.8B image-text pairs from CommonPool-12.8B).

This model has been converted to PyTorch from the original JAX checkpoints from Axlearn (https://github.com/apple/axlearn). 
These weights are directly usable in OpenCLIP (image + text).


## Model Details

- **Model Type:**  Contrastive Image-Text, Zero-Shot Image Classification.
- **Dataset:** DFN-2b
- **Papers:**
  - Data Filtering Networks: https://arxiv.org/abs/2309.17425
- **Examples Seen:** 12.8B


## Model Metrics 
| Eval Dataset                |   Metric |
|:-----------------------|---------:|
| ImageNet 1k            | 0.81396  |
| Caltech-101            | 0.953141 |
| CIFAR-10               | 0.9836   |
| CIFAR-100              | 0.8835   |
| CLEVR Counts           | 0.3338   |
| CLEVR Distance         | 0.248733 |
| Country211             | 0.28237  |
| Describable Textures   | 0.66117  |
| EuroSAT                | 0.646296 |
| FGVC Aircraft          | 0.395945 |
| Food-101               | 0.945861 |
| GTSRB                  | 0.616152 |
| ImageNet Sketch        | 0.683311 |
| ImageNet v2            | 0.7453   |
| ImageNet-A             | 0.6676   |
| ImageNet-O             | 0.3915   |
| ImageNet-R             | 0.900033 |
| KITTI Vehicle Distance | 0.201125 |
| MNIST                  | 0.8468   |
| ObjectNet              | 0.739367 |
| Oxford Flowers-102     | 0.865822 |
| Oxford-IIIT Pet        | 0.954941 |
| Pascal VOC 2007        | 0.81644  |
| PatchCamelyon          | 0.63028  |
| Rendered SST2          | 0.551345 |
| RESISC45               | 0.733175 |
| Stanford Cars          | 0.947146 |
| STL-10                 | 0.976625 |
| SUN397                 | 0.754565 |
| SVHN                   | 0.653503 |
| Flickr                 | 0.8244   |
| MSCOCO                 | 0.570363 |
| WinoGAViL              | 0.551645 |
| iWildCam               | 0.18877  |
| Camelyon17             | 0.626179 |
| FMoW                   | 0.222137 |
| Dollar Street          | 0.688084 |
| GeoDE                  | 0.91023  |
| **Average**                | **0.668558** |

## Model Usage
### With OpenCLIP
```
import torch
import torch.nn.functional as F
from urllib.request import urlopen
from PIL import Image
from open_clip import create_model_from_pretrained, get_tokenizer 

model, preprocess = create_model_from_pretrained('hf-hub:apple/DFN2B-CLIP-ViT-L-14')
tokenizer = get_tokenizer('ViT-L-14')

image = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))
image = preprocess(image).unsqueeze(0)

labels_list = ["a dog", "a cat", "a donut", "a beignet"]
text = tokenizer(labels_list, context_length=model.context_length)

with torch.no_grad(), torch.cuda.amp.autocast():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)
    image_features = F.normalize(image_features, dim=-1)
    text_features = F.normalize(text_features, dim=-1)

    text_probs = torch.sigmoid(image_features @ text_features.T * model.logit_scale.exp() + model.logit_bias)

zipped_list = list(zip(labels_list, [round(p.item(), 3) for p in text_probs[0]]))
print("Label probabilities: ", zipped_list)
```

## Citation
```bibtex
@article{fang2023data,
  title={Data Filtering Networks},
  author={Fang, Alex and Jose, Albin Madappally and Jain, Amit and Schmidt, Ludwig and Toshev, Alexander and Shankar, Vaishaal},
  journal={arXiv preprint arXiv:2309.17425},
  year={2023}
}

```

