---
pipeline_tag: text-to-image
widget:
- text: >-
    3 fish in a fish tank wearing adorable outfits, best quality, hd
  output:
    url: GGuziQaXYAAudCW.png 
- text: >-
    a woman sitting in a wooden chair in the middle of a grass field on a farm, moonlight, best quality, hd, anime art
  output:
    url: upscaled_image (1).webp 
- text: >-
    Masterpiece, glitch, holy holy holy, fog, by DarkIncursio 
  output:
    url: GGvDC_qWUAAcuQA.jpeg
- text: >-
    jpeg Full Body Photo of a weird imaginary Female creatures captured on celluloid film, (((ghost))),heavy rain, thunder, snow, water's surface, night, expressionless, Blood, Japan God,(school), Ultra Realistic, ((Scary)),looking at camera, screem, plaintive cries, Long claws, fangs, scales,8k, HDR, 500px, mysterious and ornate digital art, photic, intricate, fantasy aesthetic.
  output:
    url: upscaled_image2.png
- text: >-
    The divine tree of knowledge, an interplay between purple and gold, floats in the void of the sea of quanta, the tree is made of crystal, the void is made of nothingness, strong contrast, dim lighting, beautiful and surreal scene. wide shot
  output:
    url: upscaled_image.png
- text: >-
    The image features an older man, a long white beard and mustache, He has a stern expression, giving the impression of a wise and experienced individual. The mans beard and mustache are prominent, adding to his distinguished appearance. The close-up shot of the mans face emphasizes his facial features and the intensity of his gaze.
  output:
    url: old.png
- text: >-
    Ghost in the Shell Stand Alone Complex 
  output:
    url: upscaled_image4.png
- text: >-
    (impressionistic realism by csybgh), a 50 something male, working in banking, very short dyed dark curly balding hair, Afro-Asiatic ancestry, talks a lot but listens poorly, stuck in the past, wearing a suit, he has a certain charm, bronze skintone, sitting in a bar at night, he is smoking and feeling cool, drunk on plum wine, masterpiece, 8k, hyper detailed, smokey ambiance, perfect hands AND fingers
  output:
    url: collage.png
- text: >-
    black fluffy gorgeous dangerous cat animal creature, large orange eyes, big fluffy ears, piercing gaze, full moon, dark ambiance, best quality, extremely detailed
  output:
    url: collage2.png
license: gpl-3.0
---
<Gallery />
## ProteusV0.4: The Style Update

This update enhances stylistic capabilities, similar to Midjourney's approach, rather than advancing prompt comprehension. Methods used do not infringe on any copyrighted material.

## Proteus

Proteus serves as a sophisticated enhancement over OpenDalleV1.1, leveraging its core functionalities to deliver superior outcomes. Key areas of advancement include heightened responsiveness to prompts and augmented creative capacities. To achieve this, it was fine-tuned using approximately 220,000 GPTV captioned images from copyright-free stock images (with some anime included), which were then normalized. Additionally, DPO (Direct Preference Optimization) was employed through a collection of 10,000 carefully selected high-quality, AI-generated image pairs.

In pursuit of optimal performance, numerous LORA (Low-Rank Adaptation) models are trained independently before being selectively incorporated into the principal model via dynamic application methods. These techniques involve targeting particular segments within the model while avoiding interference with other areas during the learning phase. Consequently, Proteus exhibits marked improvements in portraying intricate facial characteristics and lifelike skin textures, all while sustaining commendable proficiency across various aesthetic domains, notably surrealism, anime, and cartoon-style visualizations.

finetuned/trained on a total of 400k+ images at this point.



## Settings for ProteusV0.4

Use these settings for the best results with ProteusV0.4:

CFG Scale: Use a CFG scale of 4 to 6

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
    "dataautogpt3/ProteusV0.4", 
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
    guidance_scale=4,
    num_inference_steps=20
).images[0]
```

please support the work I do through donating to me on: 
https://www.buymeacoffee.com/DataVoid
or following me on
https://twitter.com/DataPlusEngine