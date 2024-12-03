---
tags:
- text-to-image
- stable-diffusion
- diffusers
- image-generation
- flux
- safetensors
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
language:
- en
base_model: black-forest-labs/FLUX.1-dev
library_name: diffusers
---

# AWPortrait-FL

<div class="container">
  <img src="./poster.jpeg" width="1024"/>
</div>


AWPortrait-FL is finetuned on FLUX.1-dev using the training set of [AWPortrait-XL](https://huggingface.co/awplanet/AWPortraitXL) and nearly 2,000 fashion photography photos with extremely high aesthetic quality.
It has remarkable improvements in composition and details, with more delicate and realistic skin and textual. Trained by [DynamicWang](https://www.shakker.ai/userpage/dfca7abc67c04a9492ea738d864de070/publish) at [AWPlanet](https://huggingface.co/awplanet).


<div class="container">
  <img src="./cover.jpeg" width="1024"/>
</div>

## Comparison

The following example shows a simple comparison with FLUX.1-dev under the same parameter setting.

<div class="container">
  <img src="./compare.png" width="1024"/>
</div>

## Inference

```python
import torch
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained("Shakker-Labs/AWPortrait-FL", torch_dtype=torch.bfloat16)
pipe.to("cuda")

prompt = "close up portrait, Amidst the interplay of light and shadows in a photography studio,a soft spotlight traces the contours of a face,highlighting a figure clad in a sleek black turtleneck. The garment,hugging the skin with subtle luxury,complements the Caucasian model's understated makeup,embodying minimalist elegance. Behind,a pale gray backdrop extends,its fine texture shimmering subtly in the dim light,artfully balancing the composition and focusing attention on the subject. In a palette of black,gray,and skin tones,simplicity intertwines with profundity,as every detail whispers untold stories."

image = pipe(prompt, 
             num_inference_steps=24, 
             guidance_scale=3.5,
             width=768, height=1024,
            ).images[0]
image.save(f"example.png")
```

## LoRA Inference
To save memory, we also add a LoRA version to achieve same performance.

```python
import torch
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16)
pipe.load_lora_weights('Shakker-Labs/AWPortrait-FL', weight_name='AWPortrait-FL-lora.safetensors')
pipe.fuse_lora(lora_scale=0.9)
pipe.to("cuda")

prompt = "close up portrait, Amidst the interplay of light and shadows in a photography studio,a soft spotlight traces the contours of a face,highlighting a figure clad in a sleek black turtleneck. The garment,hugging the skin with subtle luxury,complements the Caucasian model's understated makeup,embodying minimalist elegance. Behind,a pale gray backdrop extends,its fine texture shimmering subtly in the dim light,artfully balancing the composition and focusing attention on the subject. In a palette of black,gray,and skin tones,simplicity intertwines with profundity,as every detail whispers untold stories."

image = pipe(prompt, 
             num_inference_steps=24, 
             guidance_scale=3.5,
             width=768, height=1024,
            ).images[0]
image.save(f"example.png")
```

## Online Inference

You can also download this model at [Shakker AI](https://www.shakker.ai/modelinfo/baa0dc46adb34547860a17a571065c9d?from=feed), where we provide an online interface to generate images.


## Acknowledgements
This model is trained by our copyrighted users [DynamicWang](https://www.shakker.ai/userpage/dfca7abc67c04a9492ea738d864de070/publish). We release this model under permissions. The model follows [flux-1-dev-non-commercial-license](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md) and the generated images are also non commercial.