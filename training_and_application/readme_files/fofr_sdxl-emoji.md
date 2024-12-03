---
license: creativeml-openrail-m
tags:
  - text-to-image
  - stable-diffusion
  - lora
  - diffusers
base_model: stabilityai/stable-diffusion-xl-base-1.0
pivotal_tuning: true
textual_embeddings: embeddings.pti
instance_prompt: an <s0><s1> emoji
inference: false
---
# sdxl-emoji LoRA by [fofr](https://replicate.com/fofr)
### An SDXL fine-tune based on Apple Emojis

![lora_image](https://replicate.delivery/pbxt/a3z81v5vwlKfLq1H5uBqpVmkHalOVup0jSLma9E2UaF3tawIA/out-0.png)
>

## Inference with Replicate API
Grab your replicate token [here](https://replicate.com/account)
```bash
pip install replicate
export REPLICATE_API_TOKEN=r8_*************************************
```

```py
import replicate

output = replicate.run(
    "sdxl-emoji@sha256:dee76b5afde21b0f01ed7925f0665b7e879c50ee718c5f78a9d38e04d523cc5e",
    input={"prompt": "A TOK emoji of a man"}
)
print(output)
```
You may also do inference via the API with Node.js or curl, and locally with COG and Docker, [check out the Replicate API page for this model](https://replicate.com/fofr/sdxl-emoji/api)

## Inference with 🧨 diffusers
Replicate SDXL LoRAs are trained with Pivotal Tuning, which combines training a concept via Dreambooth LoRA with training a new token with Textual Inversion.
As `diffusers` doesn't yet support textual inversion for SDXL, we will use cog-sdxl `TokenEmbeddingsHandler` class.

The trigger tokens for your prompt will be `<s0><s1>`

```shell
pip install diffusers transformers accelerate safetensors huggingface_hub
git clone https://github.com/replicate/cog-sdxl cog_sdxl
```

```py
import torch
from huggingface_hub import hf_hub_download
from diffusers import DiffusionPipeline
from cog_sdxl.dataset_and_utils import TokenEmbeddingsHandler
from diffusers.models import AutoencoderKL

pipe = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float16,
        variant="fp16",
).to("cuda")

pipe.load_lora_weights("fofr/sdxl-emoji", weight_name="lora.safetensors")

text_encoders = [pipe.text_encoder, pipe.text_encoder_2]
tokenizers = [pipe.tokenizer, pipe.tokenizer_2]

embedding_path = hf_hub_download(repo_id="fofr/sdxl-emoji", filename="embeddings.pti", repo_type="model")
embhandler = TokenEmbeddingsHandler(text_encoders, tokenizers)
embhandler.load_embeddings(embedding_path)
prompt="A <s0><s1> emoji of a man"
images = pipe(
    prompt,
    cross_attention_kwargs={"scale": 0.8},
).images
#your output image
images[0]
```
