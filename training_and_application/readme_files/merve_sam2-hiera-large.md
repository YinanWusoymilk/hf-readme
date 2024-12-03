---
license: apache-2.0
pipeline_tag: mask-generation
tags:
- sam2
---

# SAM2-Hiera-large

This repository contains large variant of SAM2 model. SAM2 is the state-of-the-art mask generation model released by Meta.

## Usage

You can use it like below. First install packaged version of SAM2.

```bash
pip install samv2 huggingface_hub
```

Each model requires different classes to infer. 

```python
from huggingface_hub import hf_hub_download
from sam2.build_sam import build_sam2
from sam2.sam2_image_predictor import SAM2ImagePredictor

hf_hub_download(repo_id = "merve/sam2-hiera-large", filename="sam2_hiera_large.pt", local_dir = "./")
sam2_checkpoint = "../checkpoints/sam2_hiera_large.pt"
model_cfg = "sam2_hiera_l.yaml"

sam2_model = build_sam2(config, ckpt, device="cuda", apply_postprocessing=False)
predictor = SAM2ImagePredictor(sam2_model)

# it accepts coco format
box = [x1, y1, w, h]
predictor.set_image(image)

masks = predictor.predict(box=box,
multimask_output=False)
```

For automatic mask generation:

```python
from huggingface_hub import hf_hub_download
from sam2.build_sam import build_sam2
from sam2.automatic_mask_generator import SAM2AutomaticMaskGenerator

hf_hub_download(repo_id = "merve/sam2-hiera-large", filename="sam2_hiera_large.pt", local_dir = "./")
sam2_checkpoint = "../checkpoints/sam2_hiera_large.pt"
model_cfg = "sam2_hiera_l.yaml"

sam2 = build_sam2(model_cfg, sam2_checkpoint, device ='cuda', apply_postprocessing=False)

mask_generator = SAM2AutomaticMaskGenerator(sam2)
masks = mask_generator.generate(image)
```


## Resources

The team behind SAM2 made example notebooks for all tasks.

- See [image predictor example](https://github.com/facebookresearch/segment-anything-2/blob/main/notebooks/image_predictor_example.ipynb) for full example on prompting.

- See [automatic mask generation example](https://github.com/facebookresearch/segment-anything-2/blob/main/notebooks/automatic_mask_generator_example.ipynb) for generating all masks.

- See [video object segmentation example](https://github.com/facebookresearch/segment-anything-2/blob/main/notebooks/video_predictor_example.ipynb)