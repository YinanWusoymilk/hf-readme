---
license: apache-2.0
pipeline_tag: text-to-image
---

# **This is an anyline model that can generate images comparable with midjourney and support any line type and any width!**
The following five lines are using different control lines, from top to below, Scribble, Canny, HED, PIDI, Lineart
![image](./000028_scribble_concat.webp)
![image](./000028_scribble_concat_canny.webp)
![image](./000028_scribble_concat_hed.webp)
![image](./000028_scribble_concat_pidi.webp)
![image](./000028_scribble_concat_lineart.webp)


# **General Scribble model that can generate images comparable with midjourney!**
![image](./masonry.webp)


# Controlnet-Scribble-Sdxl-1.0

<!-- Provide a quick summary of what the model is/does. -->

Hello, I am very happy to announce the controlnet-scribble-sdxl-1.0 model, **a very powerful controlnet that can generate high resolution images visually comparable with midjourney**. 
The model was trained with large amount of high quality data(over 10000000 images), with carefully filtered and captioned(powerful vllm model). Besides, useful tricks are applied 
during the training, including date augmentation, mutiple loss and multi resolution. Note that this model can achieve higher aesthetic performance than our Controlnet-Canny-Sdxl-1.0 model,
the model support any type of lines and any width of lines, the sketch can be very simple and so does the prompt. This model is more general and good at generate visual appealing images,
The control ability is also strong, for example if you are unstatisfied with some local regions about the generated image, draw a more precise sketch and give a detail prompt will help a lot. 
**Note the model also support lineart or canny lines, you can try it and will get a surpurise!!!**


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

### Examples[**Note the following examples are all generate using stabilityai/stable-diffusion-xl-base-1.0 and xinsir/controlnet-scribble-sdxl-1.0**]
prompt: purple feathered eagle with specks of light like stars in feathers. It glows with arcane power
![image1](./000155_scribble_concat.webp)
prompt: manga girl in the city, drip marketing
![image2](./000186_scribble_concat.webp)
prompt: 17 year old girl with long dark hair in the style of realism with fantasy elements, detailed botanical illustrations, barbs and thorns, ethereal, magical, black, purple and maroon, intricate, photorealistic 
![image3](./000210_scribble_concat.webp)
prompt: a logo for a paintball field named district 7 on a white background featuring paintballs the is bright and colourful eye catching and impactuful
![image4](./000227_scribble_concat.webp)
prompt: a photograph of a handsome crying blonde man with his face painted in the pride flag 
![image5](./000242_scribble_concat.webp)
prompt: simple flat sketch fox play ball 
![image6](./000250_scribble_concat.webp)
prompt: concept art, a surreal magical Tome of the Sun God, the book binding appears to be made of solar fire and emits a holy, radiant glow, Age of Wonders, Unreal Engine v5
![image7](./000256_scribble_concat.webp)
prompt: black Caribbean man walking balance front his fate chaos anarchy liberty independence force energy independence cinematic surreal beautiful rendition intricate sharp detail 8k 
![image8](./000271_scribble_concat.webp)
prompt: die hard nakatomi plaza, explosion at the top, vector, night scene 
![image9](./000285_scribble_concat.webp)
prompt: solitary glowing yellow tree in a desert. ultra wide shot. night time. hdr photography 
![image10](./000290_scribble_concat.webp)


## How to Get Started with the Model

Use the code below to get started with the model.

```python
from diffusers import ControlNetModel, StableDiffusionXLControlNetPipeline, AutoencoderKL
from diffusers import DDIMScheduler, EulerAncestralDiscreteScheduler
from controlnet_aux import PidiNetDetector, HEDdetector
from diffusers.utils import load_image
from huggingface_hub import HfApi
from pathlib import Path
from PIL import Image
import torch
import numpy as np
import cv2
import os


def nms(x, t, s):
    x = cv2.GaussianBlur(x.astype(np.float32), (0, 0), s)

    f1 = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]], dtype=np.uint8)
    f2 = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]], dtype=np.uint8)
    f3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.uint8)
    f4 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=np.uint8)

    y = np.zeros_like(x)

    for f in [f1, f2, f3, f4]:
        np.putmask(y, cv2.dilate(x, kernel=f) == x, x)

    z = np.zeros_like(y, dtype=np.uint8)
    z[y > t] = 255
    return z


controlnet_conditioning_scale = 1.0  
prompt = "your prompt, the longer the better, you can describe it as detail as possible"
negative_prompt = 'longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality'


eulera_scheduler = EulerAncestralDiscreteScheduler.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", subfolder="scheduler")


controlnet = ControlNetModel.from_pretrained(
    "xinsir/controlnet-scribble-sdxl-1.0",
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

# you can use either hed to generate a fake scribble given an image or a sketch image totally draw by yourself

if random.random() > 0.5:
  # Method 1 
  # if you use hed, you should provide an image, the image can be real or anime, you extract its hed lines and use it as the scribbles
  # The detail about hed detect you can refer to https://github.com/lllyasviel/ControlNet/blob/main/gradio_fake_scribble2image.py
  # Below is a example using diffusers HED detector

  # image_path = Image.open("your image path, the image can be real or anime, HED detector will extract its edge boundery")
  image_path = cv2.imread("your image path, the image can be real or anime, HED detector will extract its edge boundery")
  processor = HEDdetector.from_pretrained('lllyasviel/Annotators')
  controlnet_img = processor(image_path, scribble=False)
  controlnet_img.save("a hed detect path for an image")

  # following is some processing to simulate human sketch draw, different threshold can generate different width of lines
  controlnet_img = np.array(controlnet_img)
  controlnet_img = nms(controlnet_img, 127, 3)
  controlnet_img = cv2.GaussianBlur(controlnet_img, (0, 0), 3)

  # higher threshold, thiner line
  random_val = int(round(random.uniform(0.01, 0.10), 2) * 255)
  controlnet_img[controlnet_img > random_val] = 255
  controlnet_img[controlnet_img < 255] = 0
  controlnet_img = Image.fromarray(controlnet_img)

else:
  # Method 2
  # if you use a sketch image total draw by yourself
  control_path = "the sketch image you draw with some tools, like drawing board, the path you save it"
  controlnet_img = Image.open(control_path) # Note that the image must be black-white(0 or 255), like the examples we list

# must resize to 1024*1024 or same resolution bucket to get the best performance
width, height  = controlnet_img.size
ratio = np.sqrt(1024. * 1024. / (width * height))
new_width, new_height = int(width * ratio), int(height * ratio)
controlnet_img = controlnet_img.resize((new_width, new_height))

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

## Evaluation Data
The test data is randomly sample from midjourney upscale images with prompts, as the purpose of the project is to letting people draw images like midjourney. midjourney’s users include a large number of professional designers,
and the upscale image tend to have more beauty score and prompt consistency, it is suitable to use it as the test set to judge the ability of controlnet. We select 300 prompt-image pairs randomly and generate 4 images per prompt,
totally 1200 images generated. We caculate the Laion Aesthetic Score to measure the beauty and the PerceptualSimilarity to measure the control ability, we find the quality of images have a good consistency with the meric values.
We compare our methods with other SOTA huggingface models and list the result below. We are the models that have highest aesthectic score, and can generate visually appealing images if you prompt it properly.

Note: The condition image are generated using HED detector and random threshold to generate different kinds of lines.

## Quantitative Result
| metric | xinsir/controlnet-scribble-sdxl-1.0 | 
|-------|-------|
| laion_aesthetic |  **6.03**   |
| perceptual similarity | 0.5701 |

laion_aesthetic(the higher the better)  
perceptual similarity(the lower the better)

Note: The values are caculated when save in webp format, when save in png the aesthetic values will increase 0.1-0.3, but the relative relation remains unchanged.

### Conclusion

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->
In our evaluation, the model can generate visually appealing images using simple sketch and simple prompt. This model can support any type of lines and any width of lines, using thick line will give a coarse control
which obey the prompt your write more, and using thick line will give a strong control which obey the condition image more. The model can help you complish the drawing from coarse to fine, the model achieves higher 
aesthetic score than xinsir/controlnet-canny-sdxl-1.0, but the control ability will decrease a bit because of thick line.