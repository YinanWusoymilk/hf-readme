---
datasets:
- liuhaotian/LLaVA-Pretrain
- liuhaotian/LLaVA-Instruct-150K
language:
- en
tags:
- llava
- phi
license: mit
library_name: transformers
widget:
- text: "What animal is it?"
  src: "https://huggingface.co/datasets/mishig/sample_images/resolve/main/tiger.jpg"
- text: "Where is it?"
  src: "https://huggingface.co/datasets/mishig/sample_images/resolve/main/palace.jpg"
---

# Multi-crop LLaVA-3b

<a target="_blank" href="https://colab.research.google.com/drive/1W7JQrFXwFunAY1XvS31mwC7mrXBgGD_M">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Model details

Usually, in LLaVA models, we generate N embeddings for the image, which we then combine with text embeddings and send to the LLM. But what if instead of creating N tokens 
for one image, we create K<<N tokens for M<N parts of the image (crops)? It would allow us to get visual information from small parts of the image and not inflate the 
number of image "tokens" too much. I called this method multi-crop LLaVA (MC-LLaVA).

You can read more about the model in the [blog post](https://huggingface.co/blog/visheratin/vlm-resolution-curse).

MC-LLaVA-3b was fine-tuned from [Phi-2 merge](vince62s/phi-2-psy) using vision tower from
[SigLIP 400M](https://huggingface.co/google/siglip-so400m-patch14-384). 

As Dolphin 2.6 Phi, LLaVA-3b uses ChatML prompt format:

```
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

## How to use

```python
from transformers import AutoModel, AutoProcessor
import torch

model = AutoModel.from_pretrained("visheratin/MC-LLaVA-3b", torch_dtype=torch.float16, trust_remote_code=True).to("cuda")

processor = AutoProcessor.from_pretrained("visheratin/MC-LLaVA-3b", trust_remote_code=True)

with torch.inference_mode():
    inputs = processor(prompt, [raw_image], model, max_crops=100, num_tokens=728)
    output = model.generate(**inputs, max_new_tokens=200, use_cache=True, do_sample=False,
        eos_token_id=processor.tokenizer.eos_token_id, pad_token_id=processor.tokenizer.eos_token_id)

result = processor.tokenizer.decode(output[0]).replace(prompt, "").replace("<|im_end|>", "")
print(result)
```

## Benchmarks

- TextVQA - 50.9%
- GQA - 59.5%
- VQAv2 - 76.72%
- VizWiz - 32.68%
- V*-bench - OCR - 56.66%, GPT4V-hard - 52.94%, direct attributes - 40.86%, relative position - 56.57%

## Examples

<a target="_blank" href="https://colab.research.google.com/drive/1sXDvVl5s9fTcE0N2bQGOlXhnNlKEdeun">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## License

The model is licensed under MIT license, but since the data used for model training is largely synthetic, you should also follow OpenAI and Google Gemini terms of service. 
Which means don't create competitor models for them.

## Acknowledgments

Thanks to [Lambda](https://lambdalabs.com/) for providing a machine to train the model.

Thanks to [ML Collective](https://mlcollective.org/) for continuous support and providing compute resources for testing the model.