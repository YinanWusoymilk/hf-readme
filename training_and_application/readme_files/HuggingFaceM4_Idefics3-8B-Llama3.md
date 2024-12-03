---
license: apache-2.0
datasets:
- HuggingFaceM4/OBELICS
- HuggingFaceM4/the_cauldron
- HuggingFaceM4/Docmatix
- HuggingFaceM4/WebSight
language:
- en
tags:
- multimodal
- vision
- image-text-to-text
library_name: transformers
---

<p align="center">
    <img src="https://huggingface.co/HuggingFaceM4/idefics-80b/resolve/main/assets/IDEFICS.png" alt="Idefics-Obelics logo" width="200" height="100">
</p>

**Transformers version**: until the next Transformers pypi release, please install Transformers from source and use [this PR](https://github.com/huggingface/transformers/pull/32473) to be able to use Idefics3. TODO: change when new version.

# Idefics3

Idefics3 is an open multimodal model that accepts arbitrary sequences of image and text inputs and produces text outputs. The model can answer questions about images, describe visual content, create stories grounded on multiple images, or simply behave as a pure language model without visual inputs. It improves upon [Idefics1](https://huggingface.co/HuggingFaceM4/idefics-80b-instruct) and [Idefics2](https://huggingface.co/HuggingFaceM4/idefics2-8b), significantly enhancing capabilities around OCR, document understanding and visual reasoning.

We release the checkpoints under the Apache 2.0.

# Model Summary

- **Developed by:** Hugging Face
- **Model type:** Multi-modal model (image+text)
- **Language(s) (NLP):** en
- **License:** Apache 2.0
- **Parent Models:** [google/siglip-so400m-patch14-384](https://huggingface.co/google/siglip-so400m-patch14-384) and [meta-llama/Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)
- **Resources for more information:**
    - Idefics1 paper: [OBELICS: An Open Web-Scale Filtered Dataset of Interleaved Image-Text Documents
](https://huggingface.co/papers/2306.16527)
    - Idefics2 paper: [What matters when building vision-language models?
](https://huggingface.co/papers/2405.02246)
    - Idefics3 paper: [Building and better understanding vision-language models: insights and future directions](https://huggingface.co/papers/2408.12637)

# Uses

`Idefics3-8B` can be used to perform inference on multimodal (image + text) tasks in which the input is composed of a text query along with one (or multiple) image(s). Text and images can be arbitrarily interleaved. That includes image captioning, visual question answering, etc. These model does not support image generation.

The post-training of Idefics3-8B involves only a supervised fine-tuning stage, without RLHF alignment. As a result, the model may produce short answers or require prompt iterations to fully address the user's request. Adding a prefix to the assistant's response, such as "Let's fix this step by step" has been found to effectively influence the generated output.

To fine-tune `Idefics3-8B` on a specific task, we provide a [fine-tuning tutorial](https://github.com/merveenoyan/smol-vision/blob/main/Idefics_FT.ipynb).
Other resources for the fine-tuning of Idefics2 (can easily be adapted to Idefics3):
- With the [TRL library](https://github.com/huggingface/trl): [Script](https://gist.github.com/edbeeching/228652fc6c2b29a1641be5a5778223cb)
- With the [Hugging Face Trainer](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#api-reference%20][%20transformers.Trainer): [Tutorial notebook](https://colab.research.google.com/drive/1NtcTgRbSBKN7pYD3Vdx1j9m8pt3fhFDB?usp=sharing)


# Technical summary

Idefics3 demonstrates a great improvement over Idefics2, especially in document understanding tasks. It serves as a strong foundation for various use-case specific fine-tunings.

| Model           | MMMU <br>(val)   | MathVista <br>(test)   | MMStar <br>(val)    | DocVQA <br>(test)    | TextVQA <br>(val) |
|:---------------:|:----------------:|:----------------------:|:-------------------:|:--------------------:|:-----------------:|
| **Idefics2-8B** | 45.2             | 52.2                   | 49.5                | 74.0                 | 73.0              |
| **Idefics3-8B** | 46.6             | 58.4                   | 55.9                | 87.7                 | 74.9              |


**Idefics3 introduces several changes compared to Idefics2:**
- We use 169 visual tokens to encode a image of size 364x364. Each image is divided into several sub images of sizes at most 364x364, which are then encoded separately.
- For the fine-tuning datasets, we have extended [The Cauldron](https://huggingface.co/datasets/HuggingFaceM4/the_cauldron) and added several datasets, including [Docmatix](HuggingFaceM4/Docmatix). We will push soon these datasets to the same repo of The Cauldron (TODO).

More details about the training of the model is available in our [technical report](https://huggingface.co/papers/2408.12637).


# How to Get Started

This section shows snippets of code for generation for `Idefics3-8B`.

```python
import requests
import torch
from PIL import Image
from io import BytesIO

from transformers import AutoProcessor, AutoModelForVision2Seq
from transformers.image_utils import load_image

DEVICE = "cuda:0"

# Note that passing the image urls (instead of the actual pil images) to the processor is also possible
image1 = load_image("https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg")
image2 = load_image("https://cdn.britannica.com/59/94459-050-DBA42467/Skyline-Chicago.jpg")
image3 = load_image("https://cdn.britannica.com/68/170868-050-8DDE8263/Golden-Gate-Bridge-San-Francisco.jpg")

processor = AutoProcessor.from_pretrained("HuggingFaceM4/Idefics3-8B-Llama3")
model = AutoModelForVision2Seq.from_pretrained(
    "HuggingFaceM4/Idefics3-8B-Llama3", torch_dtype=torch.bfloat16
).to(DEVICE)

# Create inputs
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "What do we see in this image?"},
        ]
    },
    {
        "role": "assistant",
        "content": [
            {"type": "text", "text": "In this image, we can see the city of New York, and more specifically the Statue of Liberty."},
        ]
    },
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "And how about this image?"},
        ]
    },       
]
prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
inputs = processor(text=prompt, images=[image1, image2], return_tensors="pt")
inputs = {k: v.to(DEVICE) for k, v in inputs.items()}


# Generate
generated_ids = model.generate(**inputs, max_new_tokens=500)
generated_texts = processor.batch_decode(generated_ids, skip_special_tokens=True)

print(generated_texts)
```

</details>

**Text generation inference**

TODO.

# Model optimizations

If your GPU allows, we first recommend loading (and running inference) in half precision (`torch.float16` or `torch.bfloat16`).

```diff
model = AutoModelForVision2Seq.from_pretrained(
    "HuggingFaceM4/Idefics3-8B-Llama3",
+    torch_dtype=torch.bfloat16,    
).to(DEVICE)
```

**Vision encoder efficiency**

You can choose the default resolution the images will be rescaled to by adding `size= {"longest_edge": N*364}` when initializing the processor (`AutoProcessor.from_pretrained`), with `N` your desired value.
`N=4` works best in practice (this is the default value), but for very large images, it could be interesting to pass `N=5`.
This will have an impact on the number of visual tokens passed to the language model.
If you are GPU-memory-constrained, you can decrease `N`, and choose for example `N=3` or `N=2`, especially for low resolution images.

**Using Flash-attention 2 to speed up generation**

<details><summary>Click to expand.</summary>

First, make sure to install `flash-attn`. Refer to the [original repository of Flash Attention](https://github.com/Dao-AILab/flash-attention) for the package installation. Simply change the snippet above with: 

```diff
model = AutoModelForVision2Seq.from_pretrained(
    "HuggingFaceM4/Idefics3-8B-Llama3",
+    torch_dtype=torch.bfloat16,    
+    _attn_implementation="flash_attention_2",
).to(DEVICE)
```

</details>


# Misuse and Out-of-scope use

Using the model in [high-stakes](https://huggingface.co/bigscience/bloom/blob/main/README.md#glossary-and-calculations) settings is out of scope for this model. The model is not designed for [critical decisions](https://huggingface.co/bigscience/bloom/blob/main/README.md#glossary-and-calculations) nor uses with any material consequences on an individual's livelihood or wellbeing. The model outputs content that appears factual but may not be correct. Out-of-scope uses include:
- Usage for evaluating or scoring individuals, such as for employment, education, or credit
- Applying the model for critical automatic decisions, generating factual content, creating reliable summaries, or generating predictions that must be correct

Intentionally using the model for harm, violating [human rights](https://huggingface.co/bigscience/bloom/blob/main/README.md#glossary-and-calculations), or other kinds of malicious activities, is a misuse of this model. This includes:
- Spam generation
- Disinformation and influence operations
- Disparagement and defamation
- Harassment and abuse
- [Deception](https://huggingface.co/bigscience/bloom/blob/main/README.md#glossary-and-calculations)
- Unconsented impersonation and imitation
- Unconsented surveillance


# License

The model is built on top of two pre-trained models: [google/siglip-so400m-patch14-384](https://huggingface.co/google/siglip-so400m-patch14-384) and [meta-llama/Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct). We release the Idefics3 checkpoints under the Apache 2.0 license.


# Citation

**BibTeX:**

```bibtex
@misc{laurençon2024building,
      title={Building and better understanding vision-language models: insights and future directions.}, 
      author={Hugo Laurençon and Andrés Marafioti and Victor Sanh and Léo Tronchon},
      year={2024},
      eprint={2408.12637},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```


# Acknowledgements

We thank @andito and @amyeroberts for helping on the integration in Transformers.