---
tags:
- pytorch_model_hub_mixin
- model_hub_mixin
- image-to-3d
library_name: dust3r
repo_url: https://github.com/naver/dust3r
---

## DUSt3R: Geometric 3D Vision Made Easy

```bibtex
@inproceedings{dust3r_cvpr24,
      title={DUSt3R: Geometric 3D Vision Made Easy}, 
      author={Shuzhe Wang and Vincent Leroy and Yohann Cabon and Boris Chidlovskii and Jerome Revaud},
      booktitle = {CVPR},
      year = {2024}
}

@misc{dust3r_arxiv23,
      title={DUSt3R: Geometric 3D Vision Made Easy}, 
      author={Shuzhe Wang and Vincent Leroy and Yohann Cabon and Boris Chidlovskii and Jerome Revaud},
      year={2023},
      eprint={2312.14132},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2312.14132}, 
}
```

# License
The code is distributed under the CC BY-NC-SA 4.0 License. See [LICENSE](https://github.com/naver/dust3r/blob/main/LICENSE) for more information.
For the checkpoints, make sure to agree to the license of all the public training datasets and base checkpoints we used, in addition to CC-BY-NC-SA 4.0. See [section: Our Hyperparameters](https://github.com/naver/dust3r?tab=readme-ov-file#our-hyperparameters) for details.

# Model info

Gihub page: https://github.com/naver/dust3r/
Project page: https://dust3r.europe.naverlabs.com/

| Modelname   | Training resolutions | Head | Encoder | Decoder |
|-------------|----------------------|------|---------|---------|
| DUSt3R_ViTLarge_BaseDecoder_512_dpt | 512x384, 512x336, 512x288, 512x256, 512x160 | DPT | ViT-L | ViT-B |

# How to use

First, [install dust3r](https://github.com/naver/dust3r?tab=readme-ov-file#installation).
To load the model:

```python
from dust3r.model import AsymmetricCroCo3DStereo
import torch

model = AsymmetricCroCo3DStereo.from_pretrained("naver/DUSt3R_ViTLarge_BaseDecoder_512_dpt")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
```