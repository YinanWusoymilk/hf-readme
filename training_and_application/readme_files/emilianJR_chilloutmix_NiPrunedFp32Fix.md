---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: true
---

Diffuser model for this SD checkpoint:
https://civitai.com/models/6424/chilloutmix

**emilianJR/chilloutmix_NiPrunedFp32Fix** is the HuggingFace diffuser that you can use with **diffusers.StableDiffusionPipeline()**.

Examples | Examples | Examples
---- | ---- | ----
![](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/079b552b-9ef8-419d-e104-82b2a6be4400/width=450/295008.jpeg) | ![](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/805e70fc-5f4a-4e03-c3aa-8f9f1084e500/width=450/00000-741120674.jpeg) | ![](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d92ac5f5-bfd5-4280-84d9-de7b5184c400/width=450/220749.jpeg)
![](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/63fa98e5-1484-48eb-411a-cae5ff007100/width=450/222716.jpeg) | ![](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/eded64c7-fdd7-4976-8fae-32c2d8ea6800/width=450/151212.jpeg) | ![](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a8524732-e2b1-44c2-7a4a-e943ea74cf00/width=450/226780.jpeg)
-------


## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).


```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "emilianJR/chilloutmix_NiPrunedFp32Fix"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "YOUR PROMPT"
image = pipe(prompt).images[0]

image.save("image.png")
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)