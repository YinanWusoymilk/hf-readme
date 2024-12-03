---
license: apache-2.0
tags:
- text_to_image
- diffusers
- controlnet
- controlnet-canny-sdxl-1.0
pipeline_tag: text-to-image
---

# ***Drawing like Midjourney! Come on!***
![images](./masonry.webp)

# Controlnet-Canny-Sdxl-1.0

<!-- Provide a quick summary of what the model is/does. -->

Hello, I am very happy to announce the controlnet-canny-sdxl-1.0 model, **a very powerful controlnet that can generate high resolution images visually comparable with midjourney**. 
The model was trained with large amount of high quality data(over 10000000 images), with carefully filtered and captioned(powerful vllm model). Besides, useful tricks are applied 
during the training, including date augmentation, mutiple loss and multi resolution. With only 1 stage training, the performance outperforms the other opensource canny models
([diffusers/controlnet-canny-sdxl-1.0], [TheMistoAI/MistoLine]). I release it and hope to advance the application of stable diffusion models. Canny is one of the most important 
ControlNet series models and can be applied to many jobs associated with drawing and designing.

## Model Details


### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** xinsir
- **Model type:** ControlNet_SDXL
- **License:** apache-2.0
- **Finetuned from model [optional]:** stabilityai/stable-diffusion-xl-base-1.0 

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Paper [optional]:** https://arxiv.org/abs/2302.05543

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Examples

prompt: A closeup of two day of the dead models, looking to the side, large flowered headdress, full dia de Los muertoe make up, lush red lips, butterflies, 
flowers, pastel colors, looking to the side, jungle, birds, color harmony , extremely detailed, intricate, ornate, motion, stunning, beautiful, unique, soft lighting

![images_0)](./000031_scribble_concat.webp)

prompt: ghost with a plague doctor mask in a venice carnaval hyper realistic
![images_1)](./000028_scribble_concat.webp)

prompt: A picture surrounded by blue stars and gold stars, glowing, dark navy blue and gray tones, distributed in light silver and gold, playful, festive atmosphere, pure fabric, chalk, FHD 8K
![images_2)](./000016_scribble_concat.webp)

prompt: Delicious vegetarian pizza with champignon mushrooms, tomatoes, mozzarella, peppers and black olives, isolated on white background , transparent isolated white background , top down view, studio photo, transparent png, Clean sharp focus. High  end retouching. Food magazine photography. Award winning photography. Advertising photography. Commercial photography
![images_3)](./000010_scribble_concat.webp)

prompt: a blonde woman in a wedding dress in a maple forest in summer with a flower crown laurel. Watercolor painting in the style of John William Waterhouse. Romanticism. Ethereal light.
![images_4)](./000006_scribble_concat.webp)

### Examples Anime(Note that you need to change the base model to CounterfeitXL, others remains the same)

![images_5)](./000013_scribble_concat.webp)

![images_6)](./000034_scribble_concat.webp)

![images_7)](./000059_scribble_concat.webp)

![images_8)](./000078_scribble_concat.webp)

![images_9)](./000097_scribble_concat.webp)


## How to Get Started with the Model

Use the code below to get started with the model.

```python
from diffusers import ControlNetModel, StableDiffusionXLControlNetPipeline, AutoencoderKL
from diffusers import DDIMScheduler, EulerAncestralDiscreteScheduler
from PIL import Image
import torch
import numpy as np
import cv2

def HWC3(x):
    assert x.dtype == np.uint8
    if x.ndim == 2:
        x = x[:, :, None]
    assert x.ndim == 3
    H, W, C = x.shape
    assert C == 1 or C == 3 or C == 4
    if C == 3:
        return x
    if C == 1:
        return np.concatenate([x, x, x], axis=2)
    if C == 4:
        color = x[:, :, 0:3].astype(np.float32)
        alpha = x[:, :, 3:4].astype(np.float32) / 255.0
        y = color * alpha + 255.0 * (1.0 - alpha)
        y = y.clip(0, 255).astype(np.uint8)
        return y

controlnet_conditioning_scale = 1.0  
prompt = "your prompt, the longer the better, you can describe it as detail as possible"
negative_prompt = 'longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality'



eulera_scheduler = EulerAncestralDiscreteScheduler.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", subfolder="scheduler")


controlnet = ControlNetModel.from_pretrained(
    "xinsir/controlnet-canny-sdxl-1.0",
    torch_dtype=torch.float16
)

# when test with other base model, you need to change the vae also.
vae = AutoencoderKL.from_pretrained("madebyollin/sdxl-vae-fp16-fix", torch_dtype=torch.float16)

pipe = StableDiffusionXLControlNetPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    controlnet=controlnet,
    vae=vae,
    safety_checker=None,
    torch_dtype=torch.float16,
    scheduler=eulera_scheduler,
)

# need to resize the image resolution to 1024 * 1024 or same bucket resolution to get the best performance

controlnet_img = cv2.imread("your image path")
height, width, _  = controlnet_img.shape
ratio = np.sqrt(1024. * 1024. / (width * height))
new_width, new_height = int(width * ratio), int(height * ratio)
controlnet_img = cv2.resize(controlnet_img, (new_width, new_height))

controlnet_img = cv2.Canny(controlnet_img, 100, 200)
controlnet_img = HWC3(controlnet_img)
controlnet_img = Image.fromarray(controlnet_img)

images = pipe(
    prompt,
    negative_prompt=negative_prompt,
    image=controlnet_img,
    controlnet_conditioning_scale=controlnet_conditioning_scale,
    width=new_width,
    height=new_height,
    num_inference_steps=30,
    ).images

images[0].save(f"your image save path, png format is usually better than jpg or webp in terms of image quality but got much bigger")
```


## Evaluation Metric
1 Laion Aesthetic Score [https://laion.ai/blog/laion-aesthetics/]  
2 PerceptualSimilarity [https://github.com/richzhang/PerceptualSimilarity]


## Evaluation Data
The test data is randomly sample from midjourney upscale images with prompts, as the purpose of the project is to letting people draw images like midjourney. midjourney’s users include a large number of professional designers,
and the upscale image tend to have more beauty score and prompt consistency, it is suitable to use it as the test set to judge the ability of controlnet. We select 300 prompt-image pairs randomly and generate 4 images per prompt,
totally 1200 images generated. We caculate the Laion Aesthetic Score to measure the beauty and the PerceptualSimilarity to measure the control ability, we find the quality of images have a good consistency with the meric values.
We compare our methods with other SOTA huggingface models and list the result below. We are the models that have highest aesthectic score, and can generate visually appealing images if you prompt it properly.

## Quantitative Result
| metric | xinsir/controlnet-canny-sdxl-1.0 | diffusers/controlnet-canny-sdxl-1.0 | TheMistoAI/MistoLine |
|-------|-------|-------|-------|
| laion_aesthetic | **6.03** | 5.93 | 5.82 |
| perceptual similarity | **0.4200** | 0.5053 | 0.5387 |

laion_aesthetic(the higher the better)  
perceptual similarity(the lower the better)
Note: The values are calculate when saved in webp format, if you save in png format the aesthetic values will increase 0.1-0.3 but the relative relation remains unchanged.


## Training Details

The model is trained using high quality data, only 1 stage training, the resolution setting is the same with sdxl-base, 1024*1024. We use random threshold to generate canny images like lvming zhang, It is essential to find proper hyerparameters 
to realize data augmentation, too easy or too hard will hurt the model performance. Besides, we use random mask to random mask out a random percentage of canny images to force the model to learn more semantic meaning between the prompt and the line.
We use over 10000000 images, which are annotated carefully, cogvlm is proved to be a powerful image caption model[https://github.com/THUDM/CogVLM?tab=readme-ov-file]. For comic images, it is recommened to use waifu tagger to generate special tags
[https://huggingface.co/spaces/SmilingWolf/wd-tagger]. More than 64 A100s are used to train the model and the real batch size is 2560 when used accumulate_grad_batches.


### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

The data consists of many sources, including midjourney, laion 5B, danbooru, and so on. The data is carefully filtered and annotated. 


### Conclusion

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

In our evaluation, the model got better aesthetic score in real images compared with stabilityai/stable-diffusion-xl-base-1.0,  and comparable performance in cartoon sytle images.
The model is better in control ability when test with perception similarity due to more strong data augmentation and more training steps. 
Besides, the model has lower rate to generate abnormal images which tend to include some abnormal human structure.