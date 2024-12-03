---
license: apache-2.0
datasets:
- HuggingFaceM4/WebSight
language:
- en
tags:
- code
---


**Try out the [demo](https://huggingface.co/spaces/HuggingFaceM4/screenshot2html)!**

# Model Description

This model converts screenshots of website components into HTML/CSS codes.

It is based on a very early checkpoint of our forthcoming vision-language foundation model, which has been fine-tuned using the [Websight](https://huggingface.co/datasets/HuggingFaceM4/Websight) dataset.

This is very much an alpha version. The goal is to kick off an effort to develop improved models capable of converting a website screenshot into actual code.

# Code snippet

```python
import torch

from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor

from transformers.image_utils import to_numpy_array, PILImageResampling, ChannelDimension
from transformers.image_transforms import resize, to_channel_dimension_format

DEVICE = torch.device("cuda")
PROCESSOR = AutoProcessor.from_pretrained(
    "HuggingFaceM4/VLM_WebSight_finetuned",
    token=API_TOKEN,
)
MODEL = AutoModelForCausalLM.from_pretrained(
    "HuggingFaceM4/VLM_WebSight_finetuned",
    token=API_TOKEN,
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
).to(DEVICE)
image_seq_len = MODEL.config.perceiver_config.resampler_n_latents
BOS_TOKEN = PROCESSOR.tokenizer.bos_token
BAD_WORDS_IDS = PROCESSOR.tokenizer(["<image>", "<fake_token_around_image>"], add_special_tokens=False).input_ids


def convert_to_rgb(image):
    # `image.convert("RGB")` would only work for .jpg images, as it creates a wrong background
    # for transparent images. The call to `alpha_composite` handles this case
    if image.mode == "RGB":
        return image

    image_rgba = image.convert("RGBA")
    background = Image.new("RGBA", image_rgba.size, (255, 255, 255))
    alpha_composite = Image.alpha_composite(background, image_rgba)
    alpha_composite = alpha_composite.convert("RGB")
    return alpha_composite

# The processor is the same as the Idefics processor except for the BILINEAR interpolation,
# so this is a hack in order to redefine ONLY the transform method
def custom_transform(x):
    x = convert_to_rgb(x)
    x = to_numpy_array(x)
    x = resize(x, (960, 960), resample=PILImageResampling.BILINEAR)
    x = PROCESSOR.image_processor.rescale(x, scale=1 / 255)
    x = PROCESSOR.image_processor.normalize(
        x,
        mean=PROCESSOR.image_processor.image_mean,
        std=PROCESSOR.image_processor.image_std
    )
    x = to_channel_dimension_format(x, ChannelDimension.FIRST)
    x = torch.tensor(x)
    return x

inputs = PROCESSOR.tokenizer(
    f"{BOS_TOKEN}<fake_token_around_image>{'<image>' * image_seq_len}<fake_token_around_image>",
    return_tensors="pt",
    add_special_tokens=False,
)
inputs["pixel_values"] = PROCESSOR.image_processor([image], transform=custom_transform)
inputs = {k: v.to(DEVICE) for k, v in inputs.items()}
generated_ids = MODEL.generate(**inputs, bad_words_ids=BAD_WORDS_IDS, max_length=4096)
generated_text = PROCESSOR.batch_decode(generated_ids, skip_special_tokens=True)[0]

print(generated_text)
```

# Model Details

- **Developed by:** Hugging Face
- **Model type:** Multi-modal model (screenshot of website component to HTML/CSS code)
- **Language(s) (NLP):** en
- **License:** see [License section](#license)
- **Parent Models:** [SigLIP](https://github.com/huggingface/transformers/pull/26522) and [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)
- **Resources for more information:**
    <!-- - [GitHub Repo](https://github.com/huggingface/m4/) -->
    - Websight dataset: [Dataset card](https://huggingface.co/datasets/HuggingFaceM4/Websight)
    - Websight technical report: [Report](https://arxiv.org/abs/2403.09029)

# License

The model is built on top of two pre-trained models: [SigLIP](https://github.com/huggingface/transformers/pull/26522) and [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1), which are delivered under an Apache-2.0 license. As such, users should comply with the licenses of these models.

The two pre-trained models are connected to each other with newly initialized parameters that we train. These are not based on any of the two base frozen models forming the composite model. We release the additional weights we trained under an Apache-2.0 license.