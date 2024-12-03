---
pipeline_tag: text-to-image
widget:
- text: >-
    movie scene screencap, cinematic footage. thanos smelling a little yellow
    rose. extreme wide angle,
  output:
    url: images/1man.png
- text: god
  output:
    url: images/god.png
- text: 'A tiny robot taking a break under a tree in the garden '
  output:
    url: images/robot.png
- text: mystery
  output:
    url: images/mystery.png
- text: a cat wearing sunglasses in the summer
  output:
    url: images/cat.png
- text: 'robot holding a sign that says ’a storm is coming’ '
  output:
    url: images/storm.png
- text: >-
    The Exegenesis of the soul, captured within a boundless well of starlight,
    pulsating and vibrating wisps, chiaroscuro, humming transformer
  output:
    url: images/soul.png
- text: >-
    anime boy, protagonist, best quality
  output:
    url: images/animeboy.png
- text: natural photography of a man, glasses, cinematic,
  output:
    url: images/glasses.png
- text: if I could turn back time
  output:
    url: images/time.png
- text: >-
    ("Mobius" text logo) powerful aura, swirling power, cinematic 
  output:
    url: images/mobius.png
- text: the backrooms
  output:
    url: images/backrooms.png
license: apache-2.0
---
<Gallery />

# Mobius: Redefining State-of-the-Art in Debiased Diffusion Models

Mobius, a diffusion model that pushes the boundaries of domain-agnostic debiasing and representation realignment. By employing a brand new constructive deconstruction framework, Mobius achieves unrivaled generalization across a vast array of styles and domains, eliminating the need for expensive pretraining from scratch.

# Domain-Agnostic Debiasing: A Groundbreaking Approach

Domain-agnostic debiasing is a novel technique pioneered Corcel. This innovative approach aims to remove biases inherent in diffusion models without limiting their ability to generalize across diverse domains. Traditional debiasing methods often focus on specific domains or styles, resulting in models that struggle to adapt to new or unseen contexts. In contrast, domain-agnostic debiasing ensures that the model remains unbiased while maintaining its versatility and adaptability.

The key to domain-agnostic debiasing lies in the constructive deconstruction framework. This framework allows for fine-grained reworking of biases and representations without the need for pretraining from scratch. The technical details of this groundbreaking approach will be discussed in an upcoming research paper, "Constructive Deconstruction: Domain-Agnostic Debiasing of Diffusion Models," which will be made available on the Corcel.io website and through scientific publications.

By applying domain-agnostic debiasing, Mobius sets a new standard for fairness and impartiality in image generation while maintaining its exceptional ability to adapt to a wide range of styles and domains.

# Surpassing the State-of-the-Art

Mobius outperforms existing state-of-the-art diffusion models in several key areas:

Unbiased generation: Mobius generates images that are virtually free from the inherent biases commonly found in other diffusion models, setting a new benchmark for fairness and impartiality across all domains.

Exceptional generalization: With its unparalleled ability to adapt to an extensive range of styles and domains, Mobius consistently delivers top-quality results, surpassing the limitations of previous models.

Efficient fine-tuning: The Mobius base model serves as a superior foundation for creating specialized models tailored to specific tasks or domains, requiring significantly less fine-tuning and computational resources compared to other state-of-the-art models.


# Recommendations

- CFG between 3.5 and 7
  - 3.5 for extreme realism and skin detailing
  - 7 for artstic, anime, surrealism, and so on.
- Requires a CLIP skip of -3
- Sampler: DPM++ 3M SDE
- Scheduler: Karras
- Steps: 50
- Resolution: 1024x1024

Please also consider using these keep words to improve your prompts: best quality, HD, '~*~aesthetic~*~'.


# Use it with 🧨 diffusers

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
    "Corcelio/mobius", 
    vae=vae,
    torch_dtype=torch.float16
)
pipe.scheduler = KDPM2AncestralDiscreteScheduler.from_config(pipe.scheduler.config)
pipe.to('cuda')

# Define prompts and generate image
prompt = "mystery"
negative_prompt = ""

image = pipe(
    prompt, 
    negative_prompt=negative_prompt, 
    width=1024,
    height=1024,
    guidance_scale=7,
    num_inference_steps=50,
    clip_skip=3
).images[0]


image.save("generated_image.png")

```

# Credits

Made by Corcel [ https://corcel.io/ ]