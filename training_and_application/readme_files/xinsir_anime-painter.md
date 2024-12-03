---
license: apache-2.0
tags:
- diffusers
- controlnet
- text_to_image
- controlnet-scribble-sdxl-1.0
pipeline_tag: text-to-image
---

# ***Make everyone an anime painter, even you don't know anything about drawing.***

![An image of a sunset](./masonry_anime.webp)

<!-- Provide a quick summary of what the model is/does. -->

# Controlnet-scribble-sdxl-1.0-anime
This is a controlnet-scribble-sdxl-1.0 model that can generate very high quality images with an anime sketch, it can support any type of and any width of lines. As you can see from the examples that the sketch
can be very simple and unclear, we suppose you are just a child or a person know nothing about drawing, you can simple doodle and write some danbooru tags to generate a beautiful anime Illustration. In our evalution, 
the model achieves state of the art performance, obviously better than the original SDXL1.5 Scribble trained by lvming Zhang[https://github.com/lllyasviel/ControlNet], the model have been trained with complex tricks 
and high quality dataset, besides the aesthetic score, the prompt following ability[propose by Openai in the paper(https://cdn.openai.com/papers/dall-e-3.pdf)] and the image deformity rate[the probability that the images generate abnormal human struction]
also improves a lot. The founder of Midjourney said that: midjourney can help those who don't know drawing to draw, so it expands the boundaries of their imagination. We have the similar vision that: we hope to let those 
person who don't know anime or cartoons to create their own characters in a simple way, to express yourself and unleash your creativity. AIGC will reshape the animation industry, **the model we released can generate anime images with 
aesthetic score higher than almost all popular anime websites in average, so just enjoy it**. If you want to generate especially visually appealing images, you should use danbooru tags along with natural language, due to the reason that the anime images 
is far less than the real images, you can't just use natural language input like "a girl walk in the street" as the information is limited. Instead you should describe it with more detail such as "a girl, blue shirt, white hair, black eye, smile, pink flower, cherry blossoms ..."
In summary, you should first use tags to describle what in the image[danbooru tag] and then describe what happened in the image[natural language], the detail the better. If you don't describe it very clean, the image generated will be something totally by probability,
anyway, it will suit the condition image you draw and the edge detection will coincide between the condition and the generated image, the model can understand your drawing from semantics to some degree, and give you a result that is not bad. To the best of our knowledge, 
we haven't see other SDXL-Scribble model in the opensource community, probably we are the first.
### Attention
To generate anime images with our model, you need to choose an 
anime sdxl base model from huggingface[https://huggingface.co/models?pipeline_tag=text-to-image&sort=trending&search=blue] or civitai[https://civitai.com/search/models?baseModel=SDXL%201.0&sortBy=models_v8&query=anime].  
The showcases we list here is based on CounterfeitXL[https://huggingface.co/gsdf/CounterfeitXL/tree/main], different base model have different image styles and you can use bluepencil or other model as well. The model was trained with large amount of anime images which includes 
almost all the anime images we can found in the Internet. We filtered it seriously to preserve the images that have high visual quality, comparable to nijijourney or popular anime Illustration. We trained it with controlnet-sdxl-1.0, 
[https://arxiv.org/abs/2302.05543], the technical detail won't not be disclosed in this report. 


### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** xinsir
- **Model type:** ControlNet_SDXL
- **License:** apache-2.0
- **Finetuned from model [optional]:** stabilityai/stable-diffusion-xl-base-1.0 

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Paper [optional]:** https://arxiv.org/abs/2302.05543
- 

## Examples Display
prompt: 1girl, breasts, solo, long hair, pointy ears, red eyes, horns, navel, sitting, cleavage, toeless legwear, hair ornament, smoking pipe, oni horns, thighhighs, detached sleeves, looking at viewer, smile, large breasts, holding smoking pipe, wide sleeves, bare shoulders, flower, barefoot, holding, nail polish, black thighhighs, jewelry, hair flower, oni, japanese clothes, fire, kiseru, very long hair, ponytail, black hair, long sleeves, bangs, red nails, closed mouth, toenails, navel cutout, cherry blossoms, water, red dress, fingernails
![image0](./000013_scribble_concat.webp)

prompt: 1girl, solo, blonde hair, weapon, sword, hair ornament, hair flower, flower, dress, holding weapon, holding sword, holding, gloves, breasts, full body, black dress, thighhighs, looking at viewer, boots, bare shoulders, bangs, medium breasts, standing, black gloves, short hair with long locks, thigh boots, sleeveless dress, elbow gloves, sidelocks, black background, black footwear, yellow eyes, sleeveless
![image1](./000015_scribble_concat.webp)

prompt: 1girl, solo, holding, white gloves, smile, purple eyes, gloves, closed mouth, balloon, holding microphone, microphone, blue flower, long hair, puffy sleeves, purple flower, blush, puffy short sleeves, short sleeves, bangs, dress, shoes, very long hair, standing, pleated dress, white background, flower, full body, blue footwear, one side up, arm up, hair bun, brown hair, food, mini crown, crown, looking at viewer, hair between eyes, heart balloon, heart, tilted headwear, single side bun, hand up
![image2](./000010_scribble_concat.webp)

prompt: tiger, 1boy, male focus, blue eyes, braid, animal ears, tiger ears, 2022, solo, smile, chinese zodiac, year of the tiger, looking at viewer, hair over one eye, weapon, holding, white tiger, grin, grey hair, polearm, arm up, white hair, animal, holding weapon, arm behind head, multicolored hair, holding polearm
![image3](./000000_scribble_concat.webp)

prompt: 1boy, male child, glasses, male focus, shorts, solo, closed eyes, bow, bowtie, smile, open mouth, red bow, jacket, red bowtie, white background, shirt, happy, black shorts, child, simple background, long sleeves, ^_^, short hair, white shirt, brown hair, black-framed eyewear, :d, facing viewer, black hair
![image4](./000035_scribble_concat.webp)

prompt: solo, 1girl, swimsuit, blue eyes, plaid headwear, bikini, blue hair, virtual youtuber, side ponytail, looking at viewer, navel, grey bik    ini, ribbon, long hair, parted lips, blue nails, hat, breasts, plaid, hair ribbon, water, arm up, bracelet, star (symbol), cowboy shot, stomach, thigh strap, hair between eyes, beach, small breasts, jewelry, wet, bangs, plaid bikini, nail polish, grey headwear, blue ribbon, adapted costume, choker, ocean, bare shoulders, outdoors, beret
![image5](./000043_scribble_concat.webp)

prompt: fruit, food, no humans, food focus, cherry, simple background, english text, strawberry, signature, border, artist name, cream
![image6](./000067_scribble_concat.webp)

prompt: 1girl, solo, ball, swimsuit, bikini, mole, beachball, white bikini, breasts, hairclip, navel, looking at viewer, hair ornament, chromatic aberration, holding, holding ball, pool, cleavage, water, collarbone, mole on breast, blush, bangs, parted lips, bare shoulders, mole on thigh, bare arms, smile, large breasts, blonde hair, halterneck, hair between eyes, stomach
![image7](./000092_scribble_concat.webp)



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


eulera_scheduler = EulerAncestralDiscreteScheduler.from_pretrained("gsdf/CounterfeitXL", subfolder="scheduler")


controlnet = ControlNetModel.from_pretrained(
    "xinsir/anime-painter",
    torch_dtype=torch.float16
)

# when test with other base model, you need to change the vae also.
vae = AutoencoderKL.from_pretrained("gsdf/CounterfeitXL", subfolder="vae", torch_dtype=torch.float16)

pipe = StableDiffusionXLControlNetPipeline.from_pretrained(
    "gsdf/CounterfeitXL",
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

  image_path = Image.open("your image path, the image can be real or anime, HED detector will extract its edge boundery")
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
The test data is randomly sample from popular wallpaper anime images(pixiv, nijijourney and so on), the purpose of the project is to letting everyone can draw an anime Illustration.
We select 100 images and generate text with waifu-tagger[https://huggingface.co/spaces/SmilingWolf/wd-tagger] and generate 4 images per prompt, totally 400 images generated, the images
The images resolution should be 1024 * 1024 or same bucket for SDXL and 512 * 768 or same bucket for SD1.5, we then resize sdxl-generated images to 512 * 768 or same bucket for fair comparison. 
We caculate the Laion Aesthetic Score to measure the beauty and the PerceptualSimilarity to measure the control ability, we find the quality of images have a good consistency with the meric values. 
We compare our methods with other SOTA huggingface models and list the result below. We are the models that have highest aesthectic score, and can generate visually appealing images if you prompt it properly.

## Quantitative Result
| metric | xinsir/anime-painter | lllyasviel/control_v11p_sd15_scribble |
|-------|-------|-------|
| laion_aesthetic | **5.95** | 5.86 |
| perceptual similarity | **0.5171** | 0.577 | 

laion_aesthetic(the higher the better)  
perceptual similarity(the lower the better)

Note: The values are caculated when save in webp format, when save in png the aesthetic values will increase 0.1-0.3, but the relative relation remains unchanged.

### Conclusion

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

In our evaluation, the model got better aesthetic score in anime images compared with lllyasviel/control_v11p_sd15_scribble, we want to compare with other sdxl-1.0-scribble model but find nothing, The model is better in control ability when test with perception similarity due to bigger base model and complex data augmentation.
Besides, the model has lower rate to generate abnormal images which tend to include some abnormal human structure.