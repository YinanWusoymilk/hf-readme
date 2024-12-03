---
language:
- ru
- en
tags:
- PyTorch
thumbnail: "https://github.com/sberbank-ai/Real-ESRGAN"
---

# Real-ESRGAN

PyTorch implementation of a Real-ESRGAN model trained on custom dataset. This model shows better results on faces compared to the original version. It is also easier to integrate this model into your projects.

Real-ESRGAN is an upgraded ESRGAN trained with pure synthetic data is capable of enhancing details while removing annoying artifacts for common real-world images.

- [Paper](https://arxiv.org/abs/2107.10833)
- [Original implementation](https://github.com/xinntao/Real-ESRGAN)
- [Our github](https://github.com/sberbank-ai/Real-ESRGAN)

## Usage

Code for using model you can obtain in our [repo](https://github.com/sberbank-ai/Real-ESRGAN).
```python
import torch
from PIL import Image
import numpy as np
from RealESRGAN import RealESRGAN

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = RealESRGAN(device, scale=4)
model.load_weights('weights/RealESRGAN_x4.pth', download=True)

path_to_image = 'inputs/lr_image.png'
image = Image.open(path_to_image).convert('RGB')

sr_image = model.predict(image)

sr_image.save('results/sr_image.png')
```