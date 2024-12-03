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
base_model: cagliostrolab/animagine-xl-3.0
widget:
- text: 1girl, green hair, sweater, looking at viewer, upper body, beanie, outdoors, night, turtleneck, masterpiece, best quality, very aesthetic, absurdes
  parameter:
    negative_prompt: nsfw, lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]
  example_title: 1girl
- text: 1boy, male focus, green hair, sweater, looking at viewer, upper body, beanie, outdoors, night, turtleneck, masterpiece, best quality, very aesthetic, absurdes
  parameter: 
    negative_prompt: nsfw, lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]
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
  }
  .overlay-text {
    background: linear-gradient(45deg, #7ed56f, #28b485);
    -webkit-background-clip: text;
    color: transparent;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    
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
  <span>Animagine XL 3.1</span>
</h1>
<table class="custom-table">
  <tr>
    <td>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/yq_5AWegnLsGyCYyqJ-1G.png" alt="sample1">
      </div>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/sp6w1elvXVTbckkU74v3o.png" alt="sample4">
      </div>
    </td>
    <td>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/OYBuX1XzffN7Pxi4c75JV.png" alt="sample2">
      </div>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/ytT3Oaf-atbqrnPIqz_dq.png" alt="sample3">
    </td>
    <td>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/0oRq204okFxRGECmrIK6d.png" alt="sample1">
      </div>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/DW51m0HlDuAlXwu8H8bIS.png" alt="sample4">
      </div>
    </td>
  </tr>
</table>
        
**Animagine XL 3.1** is an update in the Animagine XL V3 series, enhancing the previous version, Animagine XL 3.0. This open-source, anime-themed text-to-image model has been improved for generating anime-style images with higher quality. It includes a broader range of characters from well-known anime series, an optimized dataset, and new aesthetic tags for better image creation. Built on Stable Diffusion XL, Animagine XL 3.1 aims to be a valuable resource for anime fans, artists, and content creators by producing accurate and detailed representations of anime characters.

## Model Details
- **Developed by**: [Cagliostro Research Lab](https://huggingface.co/cagliostrolab)
- **In collaboration with**: [SeaArt.ai](https://www.seaart.ai/)
- **Model type**: Diffusion-based text-to-image generative model 
- **Model Description**: Animagine XL 3.1 generates high-quality anime images from textual prompts. It boasts enhanced hand anatomy, improved concept understanding, and advanced prompt interpretation.
- **License**: [Fair AI Public License 1.0-SD](https://freedevproject.org/faipl-1.0-sd/)
- **Fine-tuned from**: [Animagine XL 3.0](https://huggingface.co/cagliostrolab/animagine-xl-3.0)

## Gradio & Colab Integration

Try the demo powered by Gradio in Huggingface Spaces: [![Open In Spaces](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/spaces/cagliostrolab/animagine-xl-3.1)

Or open the demo in Google Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#fileId=https%3A//huggingface.co/spaces/cagliostrolab/animagine-xl-3.1/blob/main/demo.ipynb)

## 🧨 Diffusers Installation

First install the required libraries:

```bash
pip install diffusers transformers accelerate safetensors --upgrade
```

Then run image generation with the following example code:

```python
import torch
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained(
    "cagliostrolab/animagine-xl-3.1", 
    torch_dtype=torch.float16, 
    use_safetensors=True, 
)
pipe.to('cuda')

prompt = "1girl, souryuu asuka langley, neon genesis evangelion, solo, upper body, v, smile, looking at viewer, outdoors, night"
negative_prompt = "nsfw, lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]"

image = pipe(
    prompt, 
    negative_prompt=negative_prompt,
    width=832,
    height=1216, 
    guidance_scale=7,
    num_inference_steps=28
).images[0]

image.save("./output/asuka_test.png")
```

## Usage Guidelines

### Tag Ordering

For optimal results, it's recommended to follow the structured prompt template because we train the model like this:

```
1girl/1boy, character name, from what series, everything else in any order.
```

## Special Tags

Animagine XL 3.1 utilizes special tags to steer the result toward quality, rating, creation date and aesthetic. While the model can generate images without these tags, using them can help achieve better results.

### Quality Modifiers

Quality tags now consider both scores and post ratings to ensure a balanced quality distribution. We've refined labels for greater clarity, such as changing 'high quality' to 'great quality'.

| Quality Modifier | Score Criterion   |
|------------------|-------------------|
| `masterpiece`    | > 95%             |
| `best quality`   | > 85% & ≤ 95%     |
| `great quality`  | > 75% & ≤ 85%     |
| `good quality`   | > 50% & ≤ 75%     |
| `normal quality` | > 25% & ≤ 50%     |
| `low quality`    | > 10% & ≤ 25%     |
| `worst quality`  | ≤ 10%             |

### Rating Modifiers

We've also streamlined our rating tags for simplicity and clarity, aiming to establish global rules that can be applied across different models. For example, the tag 'rating: general' is now simply 'general', and 'rating: sensitive' has been condensed to 'sensitive'. 

| Rating Modifier   | Rating Criterion |
|-------------------|------------------|
| `safe`            | General          |
| `sensitive`       | Sensitive        |
| `nsfw`            | Questionable     |
| `explicit, nsfw`  | Explicit         |

### Year Modifier

We've also redefined the year range to steer results towards specific modern or vintage anime art styles more accurately. This update simplifies the range, focusing on relevance to current and past eras.

| Year Tag | Year Range       |
|----------|------------------|
| `newest` | 2021 to 2024     |
| `recent` | 2018 to 2020     |
| `mid`    | 2015 to 2017     |
| `early`  | 2011 to 2014     |
| `oldest` | 2005 to 2010     |

### Aesthetic Tags

We've enhanced our tagging system with aesthetic tags to refine content categorization based on visual appeal. These tags are derived from evaluations made by a specialized ViT (Vision Transformer) image classification model, specifically trained on anime data. For this purpose, we utilized the model [shadowlilac/aesthetic-shadow-v2](https://huggingface.co/shadowlilac/aesthetic-shadow-v2), which assesses the aesthetic value of content before it undergoes training. This ensures that each piece of content is not only relevant and accurate but also visually appealing.

| Aesthetic Tag     | Score Range       |
|-------------------|-------------------|
| `very aesthetic`  | > 0.71            |
| `aesthetic`       | > 0.45 & < 0.71   |
| `displeasing`     | > 0.27 & < 0.45   |
| `very displeasing`| ≤ 0.27            |

## Recommended settings

To guide the model towards generating high-aesthetic images, use negative prompts like:

```
nsfw, lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]
```

For higher quality outcomes, prepend prompts with:

```
masterpiece, best quality, very aesthetic, absurdres
```

it’s recommended to use a lower classifier-free guidance (CFG Scale) of around 5-7, sampling steps below 30, and to use Euler Ancestral (Euler a) as a sampler. 

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

**Animagine XL 3.1** was trained on 2x A100 80GB GPUs for approximately 15 days, totaling over 350 GPU hours. The training process consisted of three stages:
  - **Pretraining**: Utilized a data-rich collection of 870k ordered and tagged images to increase Animagine XL 3.0's model knowledge.
  - **Finetuning - First Stage**: Employed labeled and curated aesthetic datasets to refine the broken U-Net after pretraining.
  - **Finetuning - Second Stage**: Utilized labeled and curated aesthetic datasets to refine the model's art style and improve hand and anatomy rendering.

### Hyperparameters

| Stage                    | Epochs | UNet lr | Train Text Encoder | Batch Size | Noise Offset | Optimizer  | LR Scheduler                  | Grad Acc Steps | GPUs |
|--------------------------|--------|---------|--------------------|------------|--------------|------------|-------------------------------|----------------|------|
| **Pretraining**    | 10     | 1e-5    | True               | 16         | N/A          | AdamW      | Cosine Annealing Warm Restart | 3              | 2    |
| **Finetuning 1st Stage** | 10     | 2e-6    | False              | 48         | 0.0357       | Adafactor  | Constant with Warmup          | 1              | 1    |
| **Finetuning 2nd Stage** | 15     | 1e-6    | False              | 48         | 0.0357       | Adafactor  | Constant with Warmup          | 1              | 1    |

## Model Comparison (Pretraining only)

### Training Config

| Configuration Item              | Animagine XL 3.0                         | Animagine XL 3.1                               |
|---------------------------------|------------------------------------------|------------------------------------------------|
| **GPU**                         | 2 x A100 80G                             | 2 x A100 80G                                   |
| **Dataset**                     | 1,271,990                                | 873,504                                        |
| **Shuffle Separator**           | True                                     | True                                           |
| **Num Epochs**                  | 10                                       | 10                                             |
| **Learning Rate**               | 7.5e-6                                   | 1e-5                                           |
| **Text Encoder Learning Rate**  | 3.75e-6                                  | 1e-5                                           |
| **Effective Batch Size**        | 48 x 1 x 2                               | 16 x 3 x 2                                     |
| **Optimizer**                   | Adafactor                                | AdamW                                          |
| **Optimizer Args**              | Scale Parameter: False, Relative Step: False, Warmup Init: False | Weight Decay: 0.1, Betas: (0.9, 0.99)   |
| **LR Scheduler**                | Constant with Warmup                     | Cosine Annealing Warm Restart                  |
| **LR Scheduler Args**           | Warmup Steps: 100                        | Num Cycles: 10, Min LR: 1e-6, LR Decay: 0.9, First Cycle Steps: 9,099 |

Source code and training config are available here: https://github.com/cagliostrolab/sd-scripts/tree/main/notebook 

### Acknowledgements

The development and release of Animagine XL 3.1 would not have been possible without the invaluable contributions and support from the following individuals and organizations:

- **[SeaArt.ai](https://www.seaart.ai/)**: Our collaboration partner and sponsor.
- **[Shadow Lilac](https://huggingface.co/shadowlilac)**: For providing the aesthetic classification model, [aesthetic-shadow-v2](https://huggingface.co/shadowlilac/aesthetic-shadow-v2).
- **[Derrian Distro](https://github.com/derrian-distro)**: For their custom learning rate scheduler, adapted from [LoRA Easy Training Scripts](https://github.com/derrian-distro/LoRA_Easy_Training_Scripts/blob/main/custom_scheduler/LoraEasyCustomOptimizer/CustomOptimizers.py).
- **[Kohya SS](https://github.com/kohya-ss)**: For their comprehensive training scripts.
- **Cagliostrolab Collaborators**: For their dedication to model training, project management, and data curation.
- **Early Testers**: For their valuable feedback and quality assurance efforts.
- **NovelAI**: For their innovative approach to aesthetic tagging, which served as an inspiration for our implementation.
- **KBlueLeaf**: For providing inspiration in balancing quality tags distribution and managing tags based on [Hakubooru Metainfo](https://github.com/KohakuBlueleaf/HakuBooru/blob/main/hakubooru/metainfo.py)

Thank you all for your support and expertise in pushing the boundaries of anime-style image generation.

## Collaborators

- [Linaqruf](https://huggingface.co/Linaqruf)
- [ItsMeBell](https://huggingface.co/ItsMeBell)
- [Asahina2K](https://huggingface.co/Asahina2K)
- [DamarJati](https://huggingface.co/DamarJati)
- [Zwicky18](https://huggingface.co/Zwicky18)
- [Scipius2121](https://huggingface.co/Scipius2121)
- [Raelina](https://huggingface.co/Raelina)
- [Kayfahaarukku](https://huggingface.co/kayfahaarukku)
- [Kriz](https://huggingface.co/Kr1SsSzz)

## Limitations

While Animagine XL 3.1 represents a significant advancement in anime-style image generation, it is important to acknowledge its limitations:

1. **Anime-Focused**: This model is specifically designed for generating anime-style images and is not suitable for creating realistic photos. 
2. **Prompt Complexity**: This model may not be suitable for users who expect high-quality results from short or simple prompts. The training focus was on concept understanding rather than aesthetic refinement, which may require more detailed and specific prompts to achieve the desired output.
3. **Prompt Format**: Animagine XL 3.1 is optimized for Danbooru-style tags rather than natural language prompts. For best results, users are encouraged to format their prompts using the appropriate tags and syntax.
4. **Anatomy and Hand Rendering**: Despite the improvements made in anatomy and hand rendering, there may still be instances where the model produces suboptimal results in these areas. 
5. **Dataset Size**: The dataset used for training Animagine XL 3.1 consists of approximately 870,000 images. When combined with the previous iteration's dataset (1.2 million), the total training data amounts to around 2.1 million images. While substantial, this dataset size may still be considered limited in scope for an "ultimate" anime model.
6. **NSFW Content**: Animagine XL 3.1 has been designed to generate more balanced NSFW content. However, it is important to note that the model may still produce NSFW results, even if not explicitly prompted. 

By acknowledging these limitations, we aim to provide transparency and set realistic expectations for users of Animagine XL 3.1. Despite these constraints, we believe that the model represents a significant step forward in anime-style image generation and offers a powerful tool for artists, designers, and enthusiasts alike.

## License

Based on Animagine XL 3.0, Animagine XL 3.1 falls under [Fair AI Public License 1.0-SD](https://freedevproject.org/faipl-1.0-sd/) license, which is compatible with Stable Diffusion models’ license. Key points:

1. **Modification Sharing:** If you modify Animagine XL 3.1, you must share both your changes and the original license.
2. **Source Code Accessibility:** If your modified version is network-accessible, provide a way (like a download link) for others to get the source code. This applies to derived models too.
3. **Distribution Terms:** Any distribution must be under this license or another with similar rules.
4. **Compliance:** Non-compliance must be fixed within 30 days to avoid license termination, emphasizing transparency and adherence to open-source values.
   
The choice of this license aims to keep Animagine XL 3.1 open and modifiable, aligning with open source community spirit. It protects contributors and users, encouraging a collaborative, ethical open-source community. This ensures the model not only benefits from communal input but also respects open-source development freedoms.

## Cagliostro Lab Discord Server

Finally Cagliostro Lab Server open to public
https://discord.gg/cqh9tZgbGc 

Feel free to join our discord server