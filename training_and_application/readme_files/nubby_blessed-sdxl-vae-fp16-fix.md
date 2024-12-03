---
license: openrail++
---

These VAEs are modified versions of [madebyollin](https://huggingface.co/madebyollin)'s [sdxl-vae-fp16-fix](https://huggingface.co/madebyollin/sdxl-vae-fp16-fix).

These VAEs should not produce a NaN in VAE error even when used on half precision. 

They have been modified using the ideas from [VAE-BlessUp script](https://github.com/sALTaccount/VAE-BlessUp) to produce higher contrast and lower brightness images than the original version. 

## The recommended version is [sdxl-vae-fp16fix-blessed.safetensors](https://huggingface.co/nubby/blessed-sdxl-vae-fp16-fix/blob/main/sdxl_vae-fp16fix-blessed.safetensors)

For most SDXL models, you probably should probably just use the non-blessed [sdxl-vae-fp16-fix](https://huggingface.co/madebyollin/sdxl-vae-fp16-fix).

I made these mostly for fun, but found that slightly increasing contrast and decreasing brightness actually improved the outputs on the model I was testing.

You may find one of them to be beneficial for PonyDiffusionV6-XL and other models based on it.

Best - [sdxl-vae-fp16fix-blessed.safetensors](https://huggingface.co/nubby/blessed-sdxl-vae-fp16-fix/blob/main/sdxl_vae-fp16fix-blessed.safetensors) = 1.1 contrast multiplier/0.7 brightness multiplier

Good - [sdxl_vae-fp16fix-c-1.1-b-0.5.safetensors](https://huggingface.co/nubby/blessed-sdxl-vae-fp16-fix/blob/main/sdxl_vae-fp16fix-c-1.1-b-0.5.safetensors) = 1.1 contrast multiplier/0.5 brightness multiplier

High Contrast - [sdxl_vae-fp16fix-c-1.2-b-0.7.safetensors](https://huggingface.co/nubby/blessed-sdxl-vae-fp16-fix/blob/main/sdxl_vae-fp16fix-c-1.2-b-0.7.safetensors) = 1.2 contrast multiplier/0.7 brightness multiplier

Very High Contrast - [sdxl_vae-fp16fix-c-1.2-b-0.5.safetensors](https://huggingface.co/nubby/kl-f8-anime2-blessed/blob/main/WD1-4-kl-f8-anime2-bless1-1.safetensors) = 1.2 contrast multiplier/0.5 brightness multiplier

Untested:

[sdxl_vae-fp16fix-c-0.9.safetensors](https://huggingface.co/nubby/blessed-sdxl-vae-fp16-fix/blob/main/sdxl_vae-fp16fix-c-0.9.safetensors) = 0.9 contrast multiplier

[sdxl_vae-fp16fix-c-0.9-b-0.9.safetensors](https://huggingface.co/nubby/blessed-sdxl-vae-fp16-fix/blob/main/sdxl_vae-fp16fix-c-0.9-b-0.9.safetensors) = 0.9 contrast multiplier/0.9 brightness multiplier

[sdxl_vae-fp16fix-c-0.8.safetensors](https://huggingface.co/nubby/blessed-sdxl-vae-fp16-fix/blob/main/sdxl_vae-fp16fix-c-0.8.safetensors) = 0.8 contrast multiplier

[sdxl_vae-fp16fix-c-0.8-b-0.9.safetensors](https://huggingface.co/nubby/blessed-sdxl-vae-fp16-fix/blob/main/sdxl_vae-fp16fix-c-0.8-b-0.9.safetensors) = 0.8 contrast multiplier/0.9 brightness multiplier

[sdxl_vae-fp16fix-c-0.8-b-0.8.safetensors](https://huggingface.co/nubby/blessed-sdxl-vae-fp16-fix/blob/main/sdxl_vae-fp16fix-c-0.8-b-0.8.safetensors) = 0.8 contrast multiplier/0.8 brightness multiplier

## Example images (made using AutismMix_confetti):
![](./Examples/ComfyUI_temp_ldfob_00001_.png)

Thank you Neggles for the script used to make them!