---
license: mit
tags:
- vision
- depth-estimation

model-index:
- name: dpt-beit-large-512
  results:
  - task:
      type: monocular-depth-estimation
      name: Monocular Depth Estimation
    dataset:
      type: MIX-6
      name: MIX-6
    metrics:
    - type: Zero-shot transfer
      value: 10.82
      name: Zero-shot transfer
      config: Zero-shot transfer
      verified: false
---
# Overview of Monocular depth estimation and BEiT
Monocular depth estimation, aiming to infer detailed depth from a single image or camera view, finds applications in fields like generative AI, 3D reconstruction, and autonomous driving. However, deriving depth from individual pixels in a single image is challenging due to the underconstrained nature of the problem. Recent advancements attribute progress to learning-based methods, particularly with MiDaS, leveraging dataset mixing and scale-and-shift-invariant loss. MiDaS has evolved with releases featuring more powerful backbones and lightweight variants for mobile use. With the rise of transformer architectures in computer vision, including those pioneered by models like ViT, there's been a shift towards using them for depth estimation. Inspired by this, MiDaS v3.1 incorporates promising transformer-based encoders alongside traditional convolutional ones, aiming for a comprehensive investigation of depth estimation techniques. The paper focuses on describing the integration of these backbones into MiDaS, providing a thorough comparison of different v3.1 models, and offering guidance on utilizing future backbones with MiDaS.

| Input Image | Output Depth Image | 
| --- | --- | 
| ![input image](https://cdn-uploads.huggingface.co/production/uploads/63dc702662dc193e6d460f1b/PDwRwuryaO3YtuyRjraiM.jpeg)  | ![Depth image](https://cdn-uploads.huggingface.co/production/uploads/63dc702662dc193e6d460f1b/ugqri6LcqJBuU9zI9aeqN.jpeg) |  


## Model description

This DPT model uses the [BEiT](https://huggingface.co/docs/transformers/model_doc/beit) model as backbone and adds a neck + head on top for monocular depth estimation.
![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/dpt_architecture.jpg)

The previous release MiDaS v3.0 solely leverages the
vanilla vision transformer ViT, MiDaS v3.1 offers additional models based on BEiT, Swin, SwinV2, Next-ViT and LeViT.  

# DPT 3.1 (BEiT backbone)

The highest quality depth estimation is achieved using the BEiT transformer. We provide variants such as BEiT512-L, BEiT384-L, and BEiT384-B, where the numbers signify training resolutions of 512x512 and 384x384, while the letters denote large and base models respectively. Although newer versions like BEiT v2 and BEiT-3 exist, they were not explored in our study. BEiT v2 lacked pretrained checkpoints with resolutions of 384x384 or higher, only offering them at 224x224. BEiT-3 was released after our study was completed.

DPT (Dense Prediction Transformer) model trained on 1.4 million images for monocular depth estimation. It was introduced in the paper [Vision Transformers for Dense Prediction](https://arxiv.org/abs/2103.13413) by Ranftl et al. (2021) and first released in [this repository](https://github.com/isl-org/MiDaS/tree/master). 

This model card refers specifically to BEiT512-L in the paper, and is refered to dpt-beit-large-512. A more recent paper from 2013, specifically discussing BEit, is in this paper [MiDaS v3.1 – A Model Zoo for Robust Monocular Relative Depth Estimation
](https://arxiv.org/pdf/2307.14460.pdf)

The model card has been written in combination by the Hugging Face team and Intel.

| Model Detail | Description |
| ----------- | ----------- | 
| Model Authors - Company | Intel | 
| Date | March 7, 2024 | 
| Version | 1 | 
| Type | Computer Vision - Monocular Depth Estimation | 
| Paper or Other Resources | [MiDaS v3.1 – A Model Zoo for Robust Monocular Relative Depth Estimation](https://arxiv.org/pdf/2307.14460.pdf) and [GitHub Repo](https://github.com/isl-org/MiDaS/blob/master/README.md) | 
| License | MIT |
| Questions or Comments | [Community Tab](https://huggingface.co/Intel/dpt-beit-large-512/discussions) and [Intel Developers Discord](https://discord.gg/rv2Gp55UJQ)|

| Intended Use | Description |
| ----------- | ----------- | 
| Primary intended uses | You can use the raw model for zero-shot monocular depth estimation. See the [model hub](https://huggingface.co/models?search=dpt-beit-large) to look for fine-tuned versions on a task that interests you. | 
| Primary intended users | Anyone doing monocular depth estimation | 
| Out-of-scope uses | This model in most cases will need to be fine-tuned for your particular task.  The model should not be used to intentionally create hostile or alienating environments for people.|


## How to use

Be sure the to update PyTorch as Transformers as mismatches in versions can generate erros such as: "TypeError: unsupported operand type(s) for //: 'NoneType' and 'NoneType'".

As tested by this contributor, the following versions ran correctly:
```python
import torch
import transformers
print(torch.__version__)
print(transformers.__version__)
```
```bash
out: '2.2.1+cpu'
out: '4.37.2'
```

### To Install:

```pythopn
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
 
```

# To Use:
Here is how to use this model for zero-shot depth estimation on an image:

```python
from transformers import DPTImageProcessor, DPTForDepthEstimation
import torch
import numpy as np
from PIL import Image
import requests

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

processor = DPTImageProcessor.from_pretrained("Intel/dpt-beit-large-512")
model = DPTForDepthEstimation.from_pretrained("Intel/dpt-beit-large-512")

# prepare image for the model
inputs = processor(images=image, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    predicted_depth = outputs.predicted_depth

# interpolate to original size
prediction = torch.nn.functional.interpolate(
    predicted_depth.unsqueeze(1),
    size=image.size[::-1],
    mode="bicubic",
    align_corners=False,
)

# visualize the prediction
output = prediction.squeeze().cpu().numpy()
formatted = (output * 255 / np.max(output)).astype("uint8")
depth = Image.fromarray(formatted)
depth
```

or one can use the pipeline API:

```python
from transformers import pipeline

pipe = pipeline(task="depth-estimation", model="Intel/dpt-beit-large-512")
result = pipe("http://images.cocodataset.org/val2017/000000181816.jpg")
result["depth"]
```

## Quantitative Analyses
| Model | Square Resolution HRWSI RMSE  | Square Resolution Blended MVS REL | Square Resolution ReDWeb RMSE |
| --- | --- | --- | --- |  
| BEiT 384-L | 0.068 | 0.070 | 0.076 |
| Swin-L Training 1| 0.0708 | 0.0724  | 0.0826  | 
| Swin-L Training 2  | 0.0713 | 0.0720  | 0.0831  | 
| ViT-L | 0.071 | 0.072 | 0.082  | 
| --- | --- | --- | --- |
 | Next-ViT-L-1K-6M  | 0.075 |0.073 | 0.085 | 
 | DeiT3-L-22K-1K |  0.070 | 0.070 | 0.080  |
 | ViT-L-Hybrid | 0.075 | 0.075 | 0.085  | 
 | DeiT3-L | 0.077 | 0.075 | 0.087  | 
 | --- | --- | --- | --- |
 | ConvNeXt-XL | 0.075 | 0.075 | 0.085  | 
 | ConvNeXt-L | 0.076 | 0.076 | 0.087  | 
 | EfficientNet-L2| 0.165 | 0.277 | 0.219 | 
 | --- | --- | --- | --- |
| ViT-L Reversed | 0.071 | 0.073 | 0.081  | 
| Swin-L Equidistant  | 0.072 | 0.074  | 0.083  | 
| --- | --- | --- | --- |

# Ethical Considerations and Limitations
dpt-beit-large-512 can produce factually incorrect output, and should not be relied on to produce factually accurate information. Because of the limitations of the pretrained model and the finetuning datasets, it is possible that this model could generate lewd, biased or otherwise offensive outputs.

Therefore, before deploying any applications of dpt-beit-large-512, developers should perform safety testing.

# Caveats and Recommendations
Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model.

Here are a couple of useful links to learn more about Intel's AI software:

- Intel Neural Compressor [link](https://github.com/intel/neural-compressor)
- Intel Extension for Transformers [link](https://github.com/intel/intel-extension-for-transformers)

# Disclaimer
The license on this model does not constitute legal advice. We are not responsible for the actions of third parties who use this model. Please cosult an attorney before using this model for commercial purposes.


### BibTeX entry and citation info

```bibtex
@article{DBLP:journals/corr/abs-2103-13413,
  author    = {Ren{\'{e}} Reiner Birkl, Diana Wofk, Matthias Muller},
  title     = {MiDaS v3.1 – A Model Zoo for Robust Monocular Relative Depth Estimation},
  journal   = {CoRR},
  volume    = {abs/2307.14460},
  year      = {2021},
  url       = {https://arxiv.org/abs/2307.14460},
  eprinttype = {arXiv},
  eprint    = {2307.14460},
  timestamp = {Wed, 26 Jul 2023},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2307.14460.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```


