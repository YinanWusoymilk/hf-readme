---
language:
- en
thumbnail: ''
tags:
- controlnet
- laion
- face
- mediapipe
- image-to-image
license: openrail
base_model: stabilityai/stable-diffusion-2-1-base
datasets:
- LAION-Face
- LAION
pipeline_tag: image-to-image
---

# ControlNet LAION Face Dataset

## Table of Contents:
- Overview: Samples, Contents, and Construction
- Usage: Downloading, Training, and Inference
- License
- Credits and Thanks

# Overview:

This dataset is designed to train a ControlNet with human facial expressions.  It includes keypoints for pupils to allow gaze direction.  Training has been tested on Stable Diffusion v2.1 base (512) and Stable Diffusion v1.5.

## Samples:

Cherry-picked from ControlNet + Stable Diffusion v2.1 Base

|Input|Face Detection|Output|
|:---:|:---:|:---:|
|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/happy_source.jpg">|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/happy_annotation.png">|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/happy_result.png">|
|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/neutral_source.jpg">|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/neutral_annotation.png">|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/neutral_result.png">|
|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/sad_source.jpg">|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/sad_annotation.png">|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/sad_result.png">|
|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/screaming_source.jpg">|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/screaming_annotation.png">|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/screaming_result.png">|
|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/sideways_source.jpg">|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/sideways_annotation.png">|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/sideways_result.png">|
|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/surprised_source.jpg">|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/surprised_annotation.png">|<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/surprised_result.png">|

Images with multiple faces are also supported:

<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/family_source.jpg">

<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/family_annotation.png">

<img src="https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/family_result.png">


## Dataset Contents:

- train_laion_face.py - Entrypoint for ControlNet training.
- laion_face_dataset.py - Code for performing dataset iteration.  Cropping and resizing happens here.
- tool_download_face_targets.py - A tool to read metadata.json and populate the target folder.
- tool_generate_face_poses.py - The original file used to generate the source images.  Included for reproducibility, but not required for training.
- training/laion-face-processed/prompt.jsonl - Read by laion_face_dataset.  Includes prompts for the images.
- training/laion-face-processed/metadata.json - Excerpts from LAION for the relevant data.  Also used for downloading the target dataset.
- training/laion-face-processed/source/xxxxxxxxx.jpg - Images with detections performed.  Generated from the target images.
- training/laion-face-processed/target/xxxxxxxxx.jpg - Selected images from LAION Face.

## Dataset Construction:

Source images were generated by pulling slice 00000 from LAION Face and passing them through MediaPipe's face detector with special configuration parameters.  

The colors and line thicknesses used for MediaPipe are as follows:

```
f_thick = 2
f_rad = 1
right_iris_draw = DrawingSpec(color=(10, 200, 250), thickness=f_thick, circle_radius=f_rad)
right_eye_draw = DrawingSpec(color=(10, 200, 180), thickness=f_thick, circle_radius=f_rad)
right_eyebrow_draw = DrawingSpec(color=(10, 220, 180), thickness=f_thick, circle_radius=f_rad)
left_iris_draw = DrawingSpec(color=(250, 200, 10), thickness=f_thick, circle_radius=f_rad)
left_eye_draw = DrawingSpec(color=(180, 200, 10), thickness=f_thick, circle_radius=f_rad)
left_eyebrow_draw = DrawingSpec(color=(180, 220, 10), thickness=f_thick, circle_radius=f_rad)
mouth_draw = DrawingSpec(color=(10, 180, 10), thickness=f_thick, circle_radius=f_rad)
head_draw = DrawingSpec(color=(10, 200, 10), thickness=f_thick, circle_radius=f_rad)

iris_landmark_spec = {468: right_iris_draw, 473: left_iris_draw}
```

We have implemented a method named `draw_pupils` which modifies some functionality from MediaPipe.  It exists as a stopgap until some pending changes are merged.


# Usage:

The containing ZIP file should be decompressed into the root of the ControlNet directory.  The `train_laion_face.py`, `laion_face_dataset.py`, and other `.py` files should sit adjacent to `tutorial_train.py` and `tutorial_train_sd21.py`.  We are assuming a checkout of the ControlNet repo at 0acb7e5, but there is no direct dependency on the repository.

## Downloading:

For copyright reasons, we cannot include the original target files.  We have provided a script (tool_download_face_targets.py) which will read from training/laion-face-processed/metadata.json and populate the target folder.  This file has no requirements, but will use tqdm if it is installed.

## Training:

When the targets folder is fully populated, training can be run on a machine with at least 24 gigabytes of VRAM.  Our model was trained for 200 hours (four epochs) on an A6000.

```bash
python tool_add_control.py ./models/v1-5-pruned-emaonly.ckpt ./models/controlnet_sd15_laion_face.ckpt
python ./train_laion_face_sd15.py
```

## Inference:

We have provided `gradio_face2image.py`.  Update the following two lines to point them to your trained model.

```
model = create_model('./models/cldm_v21.yaml').cpu()  # If you fine-tune on SD2.1 base, this does not need to change.
model.load_state_dict(load_state_dict('./models/control_sd21_openpose.pth', location='cuda'))
```

The model has some limitations: while it is empirically better at tracking gaze and mouth poses than previous attempts, it may still ignore controls.  Adding details to the prompt like, "looking right" can abate bad behavior. 

## 🧨 Diffusers

It is recommended to use the checkpoint with [Stable Diffusion 2.1 - Base](stabilityai/stable-diffusion-2-1-base) as the checkpoint has been trained on it.
Experimentally, the checkpoint can be used with other diffusion models such as dreamboothed stable diffusion.

To use with Stable Diffusion 1.5, insert `subfolder="diffusion_sd15"` into the from_pretrained arguments.  A v1.5 half-precision variant is provided but untested.

1. Install `diffusers` and related packages:
```
$ pip install diffusers transformers accelerate
```

2. Run code:
```py
from PIL import Image
import numpy as np
import torch
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler
from diffusers.utils import load_image

image = load_image(
    "https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/samples_laion_face_dataset/family_annotation.png"
)

# Stable Diffusion 2.1-base:
controlnet = ControlNetModel.from_pretrained("CrucibleAI/ControlNetMediaPipeFace", torch_dtype=torch.float16, variant="fp16")
pipe = StableDiffusionControlNetPipeline.from_pretrained(
	"stabilityai/stable-diffusion-2-1-base", controlnet=controlnet, safety_checker=None, torch_dtype=torch.float16
)
# OR
# Stable Diffusion 1.5:
controlnet = ControlNetModel.from_pretrained("CrucibleAI/ControlNetMediaPipeFace", subfolder="diffusion_sd15")
pipe = StableDiffusionControlNetPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", controlnet=controlnet, safety_checker=None)

pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)

# Remove if you do not have xformers installed
# see https://huggingface.co/docs/diffusers/v0.13.0/en/optimization/xformers#installing-xformers
# for installation instructions
pipe.enable_xformers_memory_efficient_attention()
pipe.enable_model_cpu_offload()

image = pipe("a happy family at a dentist advertisement", image=image, num_inference_steps=30).images[0]
image.save('./images.png')
```


# License:

### Source Images: (/training/laion-face-processed/source/)
This work is marked with CC0 1.0. To view a copy of this license, visit http://creativecommons.org/publicdomain/zero/1.0

### Trained Models:
Our trained ControlNet checkpoints are released under CreativeML Open RAIL-M.

### Source Code:
lllyasviel/ControlNet is licensed under the Apache License 2.0

Our modifications are released under the same license.


# Credits and Thanks:

Greatest thanks to Zhang et al. for ControlNet, Rombach et al. (StabilityAI) for Stable Diffusion, and Schuhmann et al. for LAION.

Sample images for this document were obtained from Unsplash and are CC0.

```
@misc{zhang2023adding,
  title={Adding Conditional Control to Text-to-Image Diffusion Models}, 
  author={Lvmin Zhang and Maneesh Agrawala},
  year={2023},
  eprint={2302.05543},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}

@misc{rombach2021highresolution,
      title={High-Resolution Image Synthesis with Latent Diffusion Models}, 
      author={Robin Rombach and Andreas Blattmann and Dominik Lorenz and Patrick Esser and Björn Ommer},
      year={2021},
      eprint={2112.10752},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{schuhmann2022laion5b,
      title={LAION-5B: An open large-scale dataset for training next generation image-text models}, 
      author={Christoph Schuhmann and Romain Beaumont and Richard Vencu and Cade Gordon and Ross Wightman and Mehdi Cherti and Theo Coombes and Aarush Katta and Clayton Mullis and Mitchell Wortsman and Patrick Schramowski and Srivatsa Kundurthy and Katherine Crowson and Ludwig Schmidt and Robert Kaczmarczyk and Jenia Jitsev},
      year={2022},
      eprint={2210.08402},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

This project was made possible by Crucible AI.