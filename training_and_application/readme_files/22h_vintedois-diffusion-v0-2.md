---
license: creativeml-openrail-m
tags:
  - text-to-image
---

### Vintedois (22h) Diffusion model trained by [Predogl](https://twitter.com/Predogl) and [piEsposito](https://twitter.com/piesposi_to) with open weights, configs and prompts (as it should be)

This model was trained on a large amount of high quality images with simple prompts to generate beautiful images without a lot of prompt engineering.

You can enforce style by prepending your prompt with `estilovintedois` if it is not good enough. It also works well with different aspect ratios, such as `2:3` and `3:2`.

It should also be very dreamboothable, being able to generate high fidelity faces with a little amount of steps.

**You can use this model commercially or whatever, but we are not liable if you do messed up stuff with it.**

### Gradio

TBA

### Model card

Everything from [Stable Diffusion v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5), plus the fact that this is being built by two indie devs, so it was not extensively tested for new biases.

You can run this concept via `diffusers` [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb)

### Sample results

<img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/montage-1_resized.jpg" width=768/>

<img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/montage-2_resized.jpg" width=768/>

<img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/montage-3_resized.jpg" width=768/>

### Example prompts

- Prompt: a beautiful girl In front of the cabin, the country, by Artgerm Lau and Krenz Cushart，hyperdetailed, trending on artstation, trending on deviantart
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/a%20beautiful%20girl%20In%20front%20of%20the%20cabin%2C%20the%20country%2C%20by%20Artgerm%20Lau%20and%20Krenz%20Cushart%EF%BC%8Chyperdetailed%2C%20trending%20on%20artstation%2C%20trending%20on%20deviantar.jpg" width=512/>

- Prompt: estilovintedois a girl with rainbow hair, happy, soft eyes and narrow chin, dainty figure, long hair straight down, torn kawaii shirt and baggy jeans, In style of by Jordan Grimmer and greg rutkowski, crisp lines
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/a%20girl%20with%20rainbow%20hair%2C%20happy%2C%20soft%20eyes%20and%20narrow%20chin%2C%20dainty%20figure%2C%20long%20hair%20straight%20down%2C%20torn%20kawaii%20shirt%20and%20baggy%20jeans%2C%20In%20style%20of%20by%20Jordan%20Grimmer%20and%20greg%20rutkowski%2C%20crisp%20lines.jpg" width=512/>

- Prompt: a photorealistic dramatic fantasy render of a beautiful woman wearing a beautiful intricately detailed japanese komainu kitsune mask and clasical japanese kimono by wlop, artgerm, greg rutkowski,
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/a%20photorealistic%20dramatic%20fantasy%20render%20of%20a%20beautiful%20woman%20wearing%20a%20beautiful%20intricately%20detailed%20japanese%20komainu%20kitsune%20mask%20and%20clasical%20japanese%20kimono%20by%20wlop%2C%20artgerm%2C%20greg%20rutkowski%2C%20.jpg" width=512/>

- Prompt: estilovintedois cyberpunk samurai
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/cyberpunk%20samurai.jpg" width=512/>

- Prompt: estilovintedois destroyed city
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/destroyed%20city.jpg" width=512/>

- Prompt: estilovintedois ghost of the forest by Anna Dittmann, digital art, horror, trending on artstation, anime arts, featured on Pixiv, HD, 8K
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/ghost%20of%20the%20forest%20by%20Anna%20Dittmann%2C%20digital%20art%2C%20horror%2C%20trending%20on%20artstation%2C%20anime%20arts%2C%20featured%20on%20Pixiv%2C%20HD%2C%208K.jpg" width=512/>

- Prompt: estilovintedoisgolden retriever knight portrait, finely detailed armor, intricate design, silver, silk, cinematic lighting, 4k
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/golden%20retriever%20knight%20portrait%2C%20finely%20detailed%20armor%2C%20intricate%20design%2C%20silver%2C%20silk%2C%20cinematic%20lighting%2C%204k.jpg" width=512/>

- Prompt: estilovintedois interior of a cyberpunk bedroom
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/interior%20of%20a%20cyberpunk%20bedroom.jpg" width=512/>

- Prompt: estilovintedois interior of a victorian bedroom
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/interior%20of%20a%20victorian%20bedroom.jpg" width=512/>

- Prompt: estilovintedois kneeling cat knight, portrait, finely detailed armor, intricate design, silver, silk, cinematic lighting, 4k
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/kneeling%20cat%20knight%2C%20portrait%2C%20finely%20detailed%20armor%2C%20intricate%20design%2C%20silver%2C%20silk%2C%20cinematic%20lighting%2C%204k.jpg" width=512/>

- Prompt: estilovintedois medieval town landscape
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/medieval%20town%20landscape.jpg" width=512/>

- Prompt: estilovintedois photo of an old man in a jungle, looking at the camera
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/photo%20of%20an%20old%20man%20in%20a%20jungle%2C%20looking%20at%C2%A0the%C2%A0camera.jpg" width=512/>

- Prompt: estilovintedois soviet ninja, intricate design, 3d render
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/soviet%20ninja%2C%20intricate%20design%2C%203d%20render.jpg" width=512/>

- Prompt: estilovintedois victorian city landscape
- CFG Scale: 7.5
- Scheduler: `diffusers.EulerAncestralDiscreteScheduler`
- Steps: 30
- Seed: 44

  <img src="https://huggingface.co/22h/vintedois-diffusion-v0-2/resolve/main/assets/victorian%20city%20landscape.jpg" width=512/>
