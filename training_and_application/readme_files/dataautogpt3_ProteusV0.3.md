---
pipeline_tag: text-to-image
widget:
- text: >-
    Anime full body portrait of a swordsman holding his weapon in front of him. He is facing the camera with a fierce look on his face. Anime key visual (best quality, HD, ~+~aesthetic~+~:1.2)
  output:
    url: upscaled_image.png
- text: >-
    spacious,circular underground room,{dirtied and bloodied white tiles},amalgamation,flesh,plastic,dark fabric,core,pulsating heart,limbs,human-like arms,twisted angelic wings,arms,covered in skin,feathers,scales,undulate slowly,unseen current,convulsing,head area,chaotic,mass of eyes,mouths,no human features,smaller forms,cherubs,demons,golden wires,surround,holy light,tv static effect,golden glow,shadows,terrifying essence,overwhelming presence,nightmarish,landscape,sparse,cavernous,eerie,dynamic,motion,striking,awe-inspiring,nightmarish,nightmarish,nightmare,horrifying,bio-mechanical,body horror,amalgamation
  output:
    url: 2.png
- text: >-
    A robot holding a sign saying 'The Application did not respond' in red colors
  output:
    url: 3.png
- text: >-
    A photograph of Hughyen in his early twenties, (an inspiring artist whose art focuses on glitching images and vaporwave color gradients with unexpected conflicting compositions:0.5)
  output:
    url: 4.png
- text: >-
    Anime mugshot of a tough woman. She is holding a prison sign that reads "Proteus". Her face is censored. Anime key visual (best quality, HD, ~+~aesthetic~+~:1.2)
  output:
    url: 7.png
- text: >-
    Glitch art. 1980s anime, vintage, analogue horror. ((static and noise)), chromatic aberration
  output:
    url: 5.png
- text: >-
    Masterpiece, glitch, holy holy holy, fog, by DarkIncursio
  output:
    url: 6.png
license: gpl-3.0
---
<Gallery />
## ProteusV0.3: The Anime Update

Proteus V0.3 has been advanced with an additional 200,000 anime-related images, further refined by a selection of 15,000 aesthetically pleasing images, enhancing its lighting effects significantly. This upgrade preserves its understanding of prompts and maintains its photorealistic and stylistic capabilities without suffering from catastrophic forgetting.

## Proteus

Proteus serves as a sophisticated enhancement over OpenDalleV1.1, leveraging its core functionalities to deliver superior outcomes. Key areas of advancement include heightened responsiveness to prompts and augmented creative capacities. To achieve this, it was fine-tuned using approximately 220,000 GPTV captioned images from copyright-free stock images (with some anime included), which were then normalized. Additionally, DPO (Direct Preference Optimization) was employed through a collection of 10,000 carefully selected high-quality, AI-generated image pairs.

In pursuit of optimal performance, numerous LORA (Low-Rank Adaptation) models are trained independently before being selectively incorporated into the principal model via dynamic application methods. These techniques involve targeting particular segments within the model while avoiding interference with other areas during the learning phase. Consequently, Proteus exhibits marked improvements in portraying intricate facial characteristics and lifelike skin textures, all while sustaining commendable proficiency across various aesthetic domains, notably surrealism, anime, and cartoon-style visualizations.


## Settings for ProteusV0.3

Use these settings for the best results with ProteusV0.3:

CFG Scale: Use a CFG scale of 8 to 7

Steps: 20 to 60 steps for more detail, 20 steps for faster results.

Sampler: DPM++ 2M SDE

Scheduler: Karras

Resolution: 1280x1280 or 1024x1024

please also consider using these keep words to improve your prompts:
best quality, HD, `~*~aesthetic~*~`. 

if you are having trouble coming up with prompts you can use this GPT I put together to help you refine the prompt. https://chat.openai.com/g/g-RziQNoydR-diffusion-master

## Use it with 🧨 diffusers
```python
import torch
from diffusers import (
    StableDiffusionXLPipeline, 
    KDPM2AncestralDiscreteScheduler,
    AutoencoderKL
)

# Load VAE component
vae = AutoencoderKL.from_pretrained(
    "madebyollin/sdxl-vae-fp16-fix", 
    torch_dtype=torch.float16
)

# Configure the pipeline
pipe = StableDiffusionXLPipeline.from_pretrained(
    "dataautogpt3/ProteusV0.3", 
    vae=vae,
    torch_dtype=torch.float16
)
pipe.scheduler = KDPM2AncestralDiscreteScheduler.from_config(pipe.scheduler.config)
pipe.to('cuda')

# Define prompts and generate image
prompt = "black fluffy gorgeous dangerous cat animal creature, large orange eyes, big fluffy ears, piercing gaze, full moon, dark ambiance, best quality, extremely detailed"
negative_prompt = "nsfw, bad quality, bad anatomy, worst quality, low quality, low resolutions, extra fingers, blur, blurry, ugly, wrongs proportions, watermark, image artifacts, lowres, ugly, jpeg artifacts, deformed, noisy image"

image = pipe(
    prompt, 
    negative_prompt=negative_prompt, 
    width=1024,
    height=1024,
    guidance_scale=7,
    num_inference_steps=20
).images[0]
```

please support the work I do through donating to me on: 
https://www.buymeacoffee.com/DataVoid
or following me on
https://twitter.com/DataPlusEngine