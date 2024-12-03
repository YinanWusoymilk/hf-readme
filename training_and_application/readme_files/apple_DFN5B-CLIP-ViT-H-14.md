---
license: other
license_name: apple-sample-code-license
license_link: LICENSE
---
A CLIP (Contrastive Language-Image Pre-training) model trained on DFN-5B. 
Data Filtering Networks (DFNs) are small networks used to automatically filter large pools of uncurated data. 
This model was trained on 5B images that were filtered from a pool of 43B uncurated image-text pairs 
(12.8B image-text pairs from CommonPool-12.8B + 30B additional public image-text pairs).

This model has been converted to PyTorch from the original JAX checkpoints from Axlearn (https://github.com/apple/axlearn). 
These weights are directly usable in OpenCLIP (image + text).


## Model Details

- **Model Type:**  Contrastive Image-Text, Zero-Shot Image Classification.
- **Dataset:** DFN-5b
- **Papers:**
  - Data Filtering Networks: https://arxiv.org/abs/2309.17425
- **Samples Seen:** 39B  
## Model Metrics 

| Eval Dataset                |   Metric |
|:-----------------------|---------:|
| ImageNet 1k            | 0.8344   |
| Caltech-101            | 0.954935 |
| CIFAR-10               | 0.9878   |
| CIFAR-100              | 0.9051   |
| CLEVR Counts           | 0.2966   |
| CLEVR Distance         | 0.2124   |
| Country211             | 0.343981 |
| Describable Textures   | 0.706383 |
| EuroSAT                | 0.654815 |
| FGVC Aircraft          | 0.714055 |
| Food-101               | 0.956792 |
| GTSRB                  | 0.677514 |
| ImageNet Sketch        | 0.727308 |
| ImageNet v2            | 0.773    |
| ImageNet-A             | 0.6988   |
| ImageNet-O             | 0.381    |
| ImageNet-R             | 0.929367 |
| KITTI Vehicle Distance | 0.336146 |
| MNIST                  | 0.8579   |
| ObjectNet              | 0.765156 |
| Oxford Flowers-102     | 0.899534 |
| Oxford-IIIT Pet        | 0.965515 |
| Pascal VOC 2007        | 0.818309 |
| PatchCamelyon          | 0.653625 |
| Rendered SST2          | 0.546403 |
| RESISC45               | 0.750476 |
| Stanford Cars          | 0.957592 |
| STL-10                 | 0.989    |
| SUN397                 | 0.769149 |
| SVHN                   | 0.676168 |
| Flickr                 | 0.8645   |
| MSCOCO                 | 0.631112 |
| WinoGAViL              | 0.556329 |
| iWildCam               | 0.205549 |
| Camelyon17             | 0.705034 |
| FMoW                   | 0.207482 |
| Dollar Street          | 0.699766 |
| GeoDE                  | 0.928184 |
| **Average**                | **0.698347** |
## Model Usage
### With OpenCLIP
```
import torch
import torch.nn.functional as F
from urllib.request import urlopen
from PIL import Image
from open_clip import create_model_from_pretrained, get_tokenizer 

model, preprocess = create_model_from_pretrained('hf-hub:apple/DFN5B-CLIP-ViT-H-14')
tokenizer = get_tokenizer('ViT-H-14')

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

