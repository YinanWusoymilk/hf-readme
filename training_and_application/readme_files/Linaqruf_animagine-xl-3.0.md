---
license: other
license_name: faipl-1.0-sd
license_link: https://freedevproject.org/faipl-1.0-sd/
language:
- en
tags:
  - text-to-image
  - stable-diffusion
  - safetensors
  - stable-diffusion-xl
base_model: Linaqruf/animagine-xl-2.0
widget:
- text: 1girl, green hair, sweater, looking at viewer, upper body, beanie, outdoors, night, turtleneck, masterpiece, best quality
  parameter:
    negative_prompt: nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name
  example_title: 1girl
- text: 1boy, male focus, green hair, sweater, looking at viewer, upper body, beanie, outdoors, night, turtleneck, masterpiece, best quality
  parameter: 
    negative_prompt: nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name
  example_title: 1boy
---

<style>
  .title-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Adjust this value to position the title vertically */
  }
  
  .title {
    font-size: 2.5em;
    text-align: center;
    color: #333;
    font-family: 'Helvetica Neue', sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    padding: 0.5em 0;
    background: transparent;
  }
  
  .title span {
    background: -webkit-linear-gradient(45deg, #7ed56f, #28b485);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  
  .custom-table {
    table-layout: fixed;
    width: 100%;
    border-collapse: collapse;
    margin-top: 2em;
  }
  
  .custom-table td {
    width: 50%;
    vertical-align: top;
    padding: 10px;
    box-shadow: 0px 0px 0px 0px rgba(0, 0, 0, 0.15);
  }

  .custom-image-container {
    position: relative;
    width: 100%;
    margin-bottom: 0em;
    overflow: hidden;
    border-radius: 10px;
    transition: transform .7s;
    /* Smooth transition for the container */
  }

  .custom-image-container:hover {
    transform: scale(1.05);
    /* Scale the container on hover */
  }

  .custom-image {
    width: 100%;
    height: auto;
    object-fit: cover;
    border-radius: 10px;
    transition: transform .7s;
    margin-bottom: 0em;
  }

  .nsfw-filter {
    filter: blur(8px); /* Apply a blur effect */
    transition: filter 0.3s ease; /* Smooth transition for the blur effect */
  }

  .custom-image-container:hover .nsfw-filter {
    filter: none; /* Remove the blur effect on hover */
  }
  
  .overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    color: white;
    width: 100%;
    height: 40%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 1vw;
    font-style: bold;
    text-align: center;
    opacity: 0;
    /* Keep the text fully opaque */
    background: linear-gradient(0deg, rgba(0, 0, 0, 0.8) 60%, rgba(0, 0, 0, 0) 100%);
    transition: opacity .5s;
  }
  .custom-image-container:hover .overlay {
    opacity: 1;
    /* Make the overlay always visible */
  }
  .overlay-text {
    background: linear-gradient(45deg, #7ed56f, #28b485);
    -webkit-background-clip: text;
    color: transparent;
    /* Fallback for browsers that do not support this effect */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    /* Enhanced text shadow for better legibility */
    
  .overlay-subtext {
    font-size: 0.75em;
    margin-top: 0.5em;
    font-style: italic;
  }
    
  .overlay,
  .overlay-subtext {
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  }
    
</style>

<h1 class="title">
  <span>Animagine XL 3.0</span>
</h1>
<table class="custom-table">
  <tr>
    <td>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/ep_oy_NVSMQaU162w8Gwp.png" alt="sample1">
      </div>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/FGFZgsqrhOcor5mid5eap.png" alt="sample4">
      </div>
    </td>
    <td>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/EuvINvBsCKZQuspZHN-uF.png" alt="sample2">
      </div>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/yyRqdHJfePKl7ytB6ieX9.png" alt="sample3">
    </td>
    <td>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/2oWmFh728T0hzEkUtSmgy.png" alt="sample1">
      </div>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/3yaZxWkUOenZSSNtGQR_3.png" alt="sample4">
      </div>
    </td>
  </tr>
</table>

**Animagine XL 3.0** is the latest version of the sophisticated open-source anime text-to-image model, building upon the capabilities of its predecessor, Animagine XL 2.0. Developed based on Stable Diffusion XL, this iteration boasts superior image generation with notable improvements in hand anatomy, efficient tag ordering, and enhanced knowledge about anime concepts. Unlike the previous iteration, we focused to make the model learn concepts rather than aesthetic.

## Model Details
- **Developed by**: [Linaqruf](https://huggingface.co/Linaqruf)
- **Model type**: Diffusion-based text-to-image generative model
- **Model Description**: Animagine XL 3.0 is engineered to generate high-quality anime images from textual prompts. It features enhanced hand anatomy, better concept understanding, and prompt interpretation, making it the most advanced model in its series.
- **License**: [Fair AI Public License 1.0-SD](https://freedevproject.org/faipl-1.0-sd/)
- **Finetuned from model**: [Animagine XL 2.0](https://huggingface.co/Linaqruf/animagine-xl-2.0)

## Gradio & Colab Integration

Animagine XL 3.0 is accessible through user-friendly platforms such as Gradio and Google Colab:

- **Gradio Web UI**: [Open In Spaces](https://huggingface.co/spaces/Linaqruf/Animagine-XL)
- **Google Colab**: [Open In Colab](https://colab.research.google.com/#fileId=https%3A//huggingface.co/Linaqruf/animagine-xl/blob/main/Animagine_XL_demo.ipynb)

## 🧨 Diffusers Installation

To use Animagine XL 3.0, install the required libraries as follows:

```bash
pip install diffusers --upgrade
pip install transformers accelerate safetensors
```

Example script for generating images with Animagine XL 3.0:

```python
import torch
from diffusers import (
    StableDiffusionXLPipeline, 
    EulerAncestralDiscreteScheduler,
    AutoencoderKL
)

# Load VAE component
vae = AutoencoderKL.from_pretrained(
    "madebyollin/sdxl-vae-fp16-fix", 
    torch_dtype=torch.float16
)

# Configure the pipeline
pipe = StableDiffusionXLPipeline.from_pretrained(
    "Linaqruf/animagine-xl-3.0", 
    vae=vae,
    torch_dtype=torch.float16, 
    use_safetensors=True, 
)
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
pipe.to('cuda')

# Define prompts and generate image
prompt = "1girl, arima kana, oshi no ko, solo, upper body, v, smile, looking at viewer, outdoors, night"
negative_prompt = "nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name"

image = pipe(
    prompt, 
    negative_prompt=negative_prompt, 
    width=832,
    height=1216,
    guidance_scale=7,
    num_inference_steps=28
).images[0]
```

## Usage Guidelines

### Tag Ordering

Prompting is a bit different in this iteration, for optimal results, it's recommended to follow the structured prompt template because we train the model like this:

```
1girl/1boy, character name, from what series, everything else in any order.
```

## Special Tags

Like the previous iteration, this model was trained with some special tags to steer the result toward quality, rating and when the posts was created. The model can still do the job without these special tags, but it’s recommended to use them if we want to make the model easier to handle.

### Quality Modifiers

| Quality Modifier | Score Criterion |
| ---------------- | --------------- |
| `masterpiece`    | >150            |
| `best quality`   | 100-150         |
| `high quality`   | 75-100          |
| `medium quality` | 25-75           |
| `normal quality` | 0-25            |
| `low quality`    | -5-0            |
| `worst quality`  | <-5             |

### Rating Modifiers

| Rating Modifier               | Rating Criterion          |
| ------------------------------| ------------------------- |
| `rating: general`             | General                   |
| `rating: sensitive`           | Sensitive                 |
| `rating: questionable`, `nsfw`| Questionable              |
| `rating: explicit`, `nsfw`    | Explicit                  |

### Year Modifier

These tags help to steer the result toward modern or vintage anime art styles, ranging from `newest` to `oldest`.

| Year Tag | Year Range       |
| -------- | ---------------- |
| `newest` | 2022 to 2023     |
| `late`   | 2019 to 2021     |
| `mid`    | 2015 to 2018     |
| `early`  | 2011 to 2014     |
| `oldest` | 2005 to 2010     |

## Recommended settings

To guide the model towards generating high-aesthetic images, use negative prompts like:

```
nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name
```

For higher quality outcomes, prepend prompts with:

```
masterpiece, best quality
```

However, be careful to use `masterpiece`, `best quality` because many high-scored datasets are NSFW. It’s better to add `nsfw`, `rating: sensitive` to the negative prompt and `rating: general` to the positive prompt. it’s recommended to use a lower classifier-free guidance (CFG Scale) of around 5-7, sampling steps below 30, and to use Euler Ancestral (Euler a) as a sampler. 

### Multi Aspect Resolution

This model supports generating images at the following dimensions:

| Dimensions        | Aspect Ratio    |
|-------------------|-----------------|
| `1024 x 1024`     | 1:1 Square      |
| `1152 x 896`      | 9:7             |
| `896 x 1152`      | 7:9             |
| `1216 x 832`      | 19:13           |
| `832 x 1216`      | 13:19           |
| `1344 x 768`      | 7:4 Horizontal  |
| `768 x 1344`      | 4:7 Vertical    |
| `1536 x 640`      | 12:5 Horizontal |
| `640 x 1536`      | 5:12 Vertical   |

## Training and Hyperparameters

- **Animagine XL 3.0** was trained on a 2x A100 GPU with 80GB memory for 21 days or over 500 gpu hours. The training process encompassed three stages:
  - Base: 
    - **Feature Alignment Stage**: Utilized 1.2m images to acquaint the model with basic anime concepts.
    - **Refining UNet Stage**: Employed 2.5k curated datasets to only fine-tune the UNet.
  - Curated: 
    - **Aesthetic Tuning Stage**: Employed 3.5k high-quality curated datasets to refine the model's art style.

### Hyperparameters

| Stage                       | Epochs | UNet Learning Rate | Train Text Encoder | Text Encoder Learning Rate | Batch Size     | Mixed Precision | Noise Offset |
|-----------------------------|--------|--------------------|--------------------|----------------------------|----------------|-----------------|--------------|
| **Feature Alignment Stage** | 10     | 7.5e-6             | True               | 3.75e-6                    | 48 x 2         | fp16            | N/A          |
| **Refining UNet Stage**     | 10     | 2e-6               | False              | N/A                        | 48             | fp16            | 0.0357       |
| **Aesthetic Tuning Stage**  | 10     | 1e-6               | False              | N/A                        | 48             | fp16            | 0.0357       |

## Model Comparison

### Training Config

| Configuration Item    | Animagine XL 2.0        | Animagine 3.0           |
|-----------------------|-------------------------|-------------------------|
| **GPU**               | A100 80G                | 2 x A100 80G            |
| **Dataset**           | 170k + 83k images       | 1271990 + 3500 Images   |
| **Shuffle Separator** | N/A                     | True                    |
| **Global Epochs**     | 20                      | 20                      |
| **Learning Rate**     | 1e-6                    | 7.5e-6                  |
| **Batch Size**        | 32                      | 48 x 2                  |
| **Train Text Encoder**| True                    | True                    |
| **Train Special Tags**| True                    | True                    |
| **Image Resolution**  | 1024                    | 1024                    |
| **Bucket Resolution** | 2048 x 512              | 2048 x 512              |

Source code and training config are available here: https://github.com/cagliostrolab/sd-scripts/tree/main/notebook 

## Limitations

While "Animagine XL 3.0" represents a significant advancement in anime text-to-image generation, it's important to acknowledge its limitations to understand its best use cases and potential areas for future improvement.

1. **Concept Over Artstyle Focus**: The model prioritizes learning concepts rather than specific art styles, which might lead to variations in aesthetic appeal compared to its predecessor.
2. **Non-Photorealistic Design**: Animagine XL 3.0 is not designed for generating photorealistic or realistic images, focusing instead on anime-style artwork.
3. **Anatomical Challenges**: Despite improvements, the model can still struggle with complex anatomical structures, particularly in dynamic poses, resulting in occasional inaccuracies.
4. **Dataset Limitations**: The training dataset of 1.2 million images may not encompass all anime characters or series, limiting the model's ability to generate less known or newer characters.
5. **Natural Language Processing**: The model is not optimized for interpreting natural language, requiring more structured and specific prompts for best results.
6. **NSFW Content Risk**: Using high-quality tags like 'masterpiece' or 'best quality' carries a risk of generating NSFW content inadvertently, due to the prevalence of such images in high-scoring training datasets.

These limitations highlight areas for potential refinement in future iterations and underscore the importance of careful prompt crafting for optimal results. Understanding these constraints can help users better navigate the model's capabilities and tailor their expectations accordingly.

## Acknowledgements

We extend our gratitude to the entire team and community that contributed to the development of Animagine XL 3.0, including our partners and collaborators who provided resources and insights crucial for this iteration.

- **Main:** For the open source grant supporting our research, thank you so much.
- **Cagliostro Lab Collaborator:** For helping quality checking during pretraining and curating datasets during fine-tuning.
- **Kohya SS:** For providing the essential training script and merged our PR about `keep_tokens_separator` or Shuffle Separator.
- **Camenduru Server Community:** For invaluable insights and support and quality checking
- **NovelAI:** For inspiring how to build the datasets and label it using tag ordering.

## Collaborators

- [Linaqruf](https://huggingface.co/Linaqruf)
- [DamarJati](https://huggingface.co/DamarJati)
- [Asahina2K](https://huggingface.co/Asahina2K)
- [ItsMeBell](https://huggingface.co/ItsMeBell)
- [Zwicky18](https://huggingface.co/Zwicky18)
- [NekoFi](https://huggingface.co/NekoFi)
- [Scipius2121](https://huggingface.co/Scipius2121)
- [Raelina](https://huggingface.co/Raelina)

## License

Animagine XL 3.0 now uses the [Fair AI Public License 1.0-SD](https://freedevproject.org/faipl-1.0-sd/), compatible with Stable Diffusion models. Key points:
1. **Modification Sharing:** If you modify Animagine XL 3.0, you must share both your changes and the original license.
2. **Source Code Accessibility:** If your modified version is network-accessible, provide a way (like a download link) for others to get the source code. This applies to derived models too.
3. **Distribution Terms:** Any distribution must be under this license or another with similar rules.
4. **Compliance:** Non-compliance must be fixed within 30 days to avoid license termination, emphasizing transparency and adherence to open-source values.

The choice of this license aims to keep Animagine XL 3.0 open and modifiable, aligning with open source community spirit. It protects contributors and users, encouraging a collaborative, ethical open-source community. This ensures the model not only benefits from communal input but also respects open-source development freedoms.
