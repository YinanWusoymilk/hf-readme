---
inference: false
---

<br>
<br>

# LWM-1M-Jax Model Card

## Model details

**Model type:**
LWM-1M-Jax is an open-source model trained from LLaMA-2 on a subset of Books3 filtered data, along with a large collection if image and video data. It is an auto-regressive vision-language model, based on the transformer architecture. These are the Jax / Flax version of the parameters.

The model is a Jax checkpoint. Inference code and instructions can be found at: https://github.com/LargeWorldModel/lwm

**Model date:**
LWM-1M-Jax was trained in January 2024.

**Paper or resources for more information:**
https://largeworldmodel.github.io/

## License
Llama 2 is licensed under the LLAMA 2 Community License, 
Copyright (c) Meta Platforms, Inc. All Rights Reserved.

**Where to send questions or comments about the model:**
https://github.com/LargeWorldModel/lwm/issues

## Training dataset
- Books3 dataset
- 700B text-image pairs from Laion-2B-en, filtered to only keep images with at least 256 resolution
- 400M text-image pairs from COYO-700M, filtered to only keep images with at least 256 resolution
- 10M text-video pairs from WebVid10M
- 3M text-video pairs from a subset of InternVid10M
- 73K text-video chat pairs from Valley-Instruct-73K 
- 100K text-video chat pairs from Video-ChatGPT