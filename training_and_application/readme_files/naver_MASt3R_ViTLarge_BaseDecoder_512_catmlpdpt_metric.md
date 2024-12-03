---
tags:
- image-to-3d
- pytorch_model_hub_mixin
- model_hub_mixin
library_name: mast3r
repo_url: https://github.com/naver/mast3r
---


## Grounding Image Matching in 3D with MASt3R

```bibtex
@misc{mast3r_arxiv24,
      title={Grounding Image Matching in 3D with MASt3R}, 
      author={Vincent Leroy and Yohann Cabon and Jerome Revaud},
      year={2024},
      eprint={2406.09756},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@inproceedings{dust3r_cvpr24,
      title={DUSt3R: Geometric 3D Vision Made Easy}, 
      author={Shuzhe Wang and Vincent Leroy and Yohann Cabon and Boris Chidlovskii and Jerome Revaud},
      booktitle = {CVPR},
      year = {2024}
}
```

# License
The code is distributed under the CC BY-NC-SA 4.0 License. See [LICENSE](https://github.com/naver/mast3r/blob/main/LICENSE) for more information.  
For the checkpoints, make sure to agree to the license of all the public training datasets and base checkpoints we used, in addition to CC-BY-NC-SA 4.0.  
The mapfree dataset license in particular is very restrictive. For more information, check [CHECKPOINTS_NOTICE](https://github.com/naver/mast3r/blob/main/CHECKPOINTS_NOTICE).

# Model info

Gihub page: https://github.com/naver/mast3r/

| Modelname   | Training resolutions | Head | Encoder | Decoder |
|-------------|----------------------|------|---------|---------|
| MASt3R_ViTLarge_BaseDecoder_512_catmlpdpt_nonmetric | 512x384, 512x336, 512x288, 512x256, 512x160 | CatMLP+DPT | ViT-L | ViT-B |

# How to use

First, [install mast3r](https://github.com/naver/mast3r?tab=readme-ov-file#installation).
To load the model:

```python
from mast3r.model import AsymmetricMASt3R
import torch

model = AsymmetricMASt3R.from_pretrained("naver/MASt3R_ViTLarge_BaseDecoder_512_catmlpdpt_nonmetric")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
```