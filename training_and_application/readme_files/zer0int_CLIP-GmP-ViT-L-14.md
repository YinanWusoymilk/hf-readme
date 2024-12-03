---
license: mit
base_model: openai/clip-vit-large-patch14
datasets:
- SPRIGHT-T2I/spright_coco
---
## A fine-tune of CLIP-L. Original model: [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14)
- ❤️ this CLIP? [Help feed it](https://ko-fi.com/zer0int) if you can. Besides data, CLIP eats time & expensive electricity of DE. TY! 🤗
- Want to feed it yourself? All code for fine-tuning and much more is on [my GitHub](https://github.com/zer0int).
-----
## Update 23/SEP/2024:
- Huggingface Transformers / Diffusers pipeline now implemented.
- See here for an example script: [Integrating my CLIP-L with Flux.1](https://github.com/zer0int/CLIP-txt2img-diffusers-scripts)
- Otherwise, use as normal / any HF model:
```
from transformers import CLIPModel, CLIPProcessor, CLIPConfig
model_id = "zer0int/CLIP-GmP-ViT-L-14"
config = CLIPConfig.from_pretrained(model_id)
```
## Update 03/SEP/2024 / edit 05/AUG:

## 👋 Looking for a Text Encoder for Flux.1 (or SD3, SDXL, SD, ...) to replace CLIP-L? 👀
You'll generally want the "TE-only" .safetensors:

- 👉 The "TEXT" model has superior prompt following, especially for text, but also for other details. [DOWNLOAD](https://huggingface.co/zer0int/CLIP-GmP-ViT-L-14/blob/main/ViT-L-14-TEXT-detail-improved-hiT-GmP-TE-only-HF.safetensors)
- 👉 The "SMOOTH" model can sometimes** have better details (when there's no text in the image). [DOWNLOAD](https://huggingface.co/zer0int/CLIP-GmP-ViT-L-14/blob/main/ViT-L-14-BEST-smooth-GmP-TE-only-HF-format.safetensors)
- The "GmP" initial fine-tune is deprecated / inferior to the above models. Still, you can [DOWNLOAD](https://huggingface.co/zer0int/CLIP-GmP-ViT-L-14/blob/main/ViT-L-14-GmP-ft-TE-only-HF-format.safetensors) it.

**: The "TEXT" model is the best for text. Full stop. But whether the "SMOOTH" model is better for your (text-free) scenario than the "TEXT" model really depends on the specific prompt. It might also be the case that the "TEXT" model leads to images that you prefer over "SMOOTH"; the only way to know is to experiment with both.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6490359a877fc29cb1b09451/y-B-FimzahYqskNr2MV1C.png)

## 🤓👨‍💻 In general (because we're not limited to text-to-image generative AI), I provide four versions / downloads:

- Text encoder only .safetensors.
- Full model .safetensors.
- State_dict pickle.
- Full model pickle (can be used as-is with "import clip" -> clip.load() after bypassing SHA checksum verification).

## The TEXT model has a modality gap of 0.80 (OpenAI pre-trained: 0.82).
- Trained with high temperature of 0.1 + tinkering.
- ImageNet/ObjectNet accuracy ~0.91 for both "SMOOTH" and "TEXT" models (pre-trained: ~0.84).
- The models (this plot = "TEXT" model on MSCOCO) are also golden retrievers: 🥰🐕

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6490359a877fc29cb1b09451/WiyuZLZVyjBTdPwHaVG_6.png)

----
## Update 11/AUG/2024:

New Best-Performing CLIP ViT-L/14 'GmP-smooth' model added (simply download the files named *BEST*!):

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6490359a877fc29cb1b09451/qb5hYNxSTMB5z7rSs7N9k.png)

Or just create a fine-tune yourself: [https://github.com/zer0int/CLIP-fine-tune](https://github.com/zer0int/CLIP-fine-tune)

How?
- Geometric Parametrization (GmP) (same as before)
- Activation Value manipulation for 'adverb neuron' (same as before)
- NEW: Custom loss function with label smoothing!
- For in-depth details, see my GitHub. 🤗

----

## A fine-tune of OpenAI / CLIP ViT-L/14 that has an unprecedented ImageNet/ObjectNet accuracy of ~0.90 (original pre-trained model / OpenAI's CLIP: ~0.85)**.

Made possible with Geometric Parametrization (GmP):

```

"Normal" CLIP MLP (multi-layer perceptron):

(mlp): Sequential(
  |-(c_fc): Linear(in_features=1024, out_features=4096, bias=True)
  | (gelu): QuickGELU()
|-}-(c_proj): Linear(in_features=4096, out_features=1024, bias=True)
| | 
| |-- visual.transformer.resblocks.0.mlp.c_fc.weight
| |-- visual.transformer.resblocks.0.mlp.c_fc.bias
|
|---- visual.transformer.resblocks.0.mlp.c_proj.weight
|---- visual.transformer.resblocks.0.mlp.c_proj.bias


GmP CLIP MLP:

Weight decomposition into:
- radial component 'r' as norm of pre-trained weights
- angular component 'theta' as normalized direction
-> preserves weight vectors' directionality and magnitude

(mlp): Sequential(
  |-(c_fc): GeometricLinear()
  | (gelu): QuickGELU()
|-}-(c_proj): GeometricLinear()
| | 
| |-- visual.transformer.resblocks.0.mlp.c_fc.r
| |-- visual.transformer.resblocks.0.mlp.c_fc.theta
| |-- visual.transformer.resblocks.0.mlp.c_fc.bias
|
|---- visual.transformer.resblocks.0.mlp.c_proj.r
|---- visual.transformer.resblocks.0.mlp.c_proj.theta
|---- visual.transformer.resblocks.0.mlp.c_proj.bias

(Same thing for [text] transformer.resblocks)

```

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6490359a877fc29cb1b09451/mqIgsH_aWKop_DDQ2KglN.png)

✅ The model / state_dict I am sharing was converted back to .weight after fine-tuning - alas, it can be used in the same manner as any state_dict, e.g. for use with ComfyUI as the SDXL / SD3 Text Encoder! 🤗

- ** For details on training and those numbers / the eval, please see [https://github.com/zer0int/CLIP-fine-tune](https://github.com/zer0int/CLIP-fine-tune)
- -> You can use "exp-acts-ft-finetune-OpenAI-CLIP-ViT-L-14-GmP-manipulate-neurons.py" to replicate my exact model fine-tune.

Pre-trained CLIP model by OpenAI, License: [MIT License](https://github.com/openai/CLIP/blob/main/LICENSE)