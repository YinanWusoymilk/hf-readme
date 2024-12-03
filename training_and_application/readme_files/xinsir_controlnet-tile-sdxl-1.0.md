---
license: apache-2.0
pipeline_tag: text-to-image
---

# ***ControlNet Tile SDXL***
![images](./masonry.webp)

# Image Deblur Example(Repaint Detail)
![images_0)](./000118_tile_blur_concat.webp)

![images_1)](./000126_tile_blur_concat.webp)

![images_2)](./000129_tile_blur_concat.webp)

![images_3)](./000132_tile_blur_concat.webp)

![images_4)](./000139_tile_blur_concat.webp)

# Image Variation Example(like midjourney)

![images_5)](./000003_tile_var_concat.webp)

![images_6)](./000008_tile_var_concat.webp)

![images_7)](./000018_tile_var_concat.webp)

![images_8)](./000030_tile_var_concat.webp)

![images_9)](./000039_tile_var_concat.webp)

# Image Super-resolution(like realESRGAN)

support any aspect ratio and any times upscale, followings are 3 * 3 times

![images_5)](./000003.webp)

![images_6)](./000003_scribble.webp)

![images_7)](./000053.webp)

![images_8)](./000053_scribble.webp)

# Code to Use Tile blur

code reference: https://huggingface.co/TTPlanet/TTPLanet_SDXL_Controlnet_Tile_Realistic/blob/main/TTP_tile_preprocessor_v5.py  
https://github.com/lllyasviel/ControlNet-v1-1-nightly/blob/main/gradio_tile.py

```python
from diffusers import ControlNetModel, StableDiffusionXLControlNetPipeline, AutoencoderKL
from diffusers import DDIMScheduler, EulerAncestralDiscreteScheduler
from PIL import Image
from guided_filter import FastGuidedFilter # I have upload this file in this repo
import torch
import numpy as np
import cv2

def resize_image_control(control_image, resolution):
    HH, WW, _ = control_image.shape
    crop_h = random.randint(0, HH - resolution[1])
    crop_w = random.randint(0, WW - resolution[0])
    crop_image = control_image[crop_h:crop_h+resolution[1], crop_w:crop_w+resolution[0], :]
    return crop_image, crop_w, crop_h

def apply_gaussian_blur(image_np, ksize=5, sigmaX=1.0):
    if ksize % 2 == 0:
        ksize += 1  # ksize must be odd
    blurred_image = cv2.GaussianBlur(image_np, (ksize, ksize), sigmaX=sigmaX)
    return blurred_image

def apply_guided_filter(image_np, radius, eps, scale):
    filter = FastGuidedFilter(image_np, radius, eps, scale)
    return filter.filter(image_np)


controlnet_conditioning_scale = 1.0  
prompt = "your prompt, the longer the better, you can describe it as detail as possible"
negative_prompt = 'longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality'

eulera_scheduler = EulerAncestralDiscreteScheduler.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", subfolder="scheduler")


controlnet = ControlNetModel.from_pretrained(
    "xinsir/controlnet-tile-sdxl-1.0",
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

controlnet_img = cv2.imread("your original image path")
height, width, _  = controlnet_img.shape
ratio = np.sqrt(1024. * 1024. / (width * height))
W, H = int(width * ratio), int(height * ratio)

crop_w, crop_h = 0, 0
controlnet_img = cv2.resize(controlnet_img, (W, H))


blur_strength = random.sample([i / 10. for i in range(10, 201, 2)], k=1)[0]
radius = random.sample([i for i in range(1, 40, 2)], k=1)[0]
eps = random.sample([i / 1000. for i in range(1, 101, 2)], k=1)[0]
scale_factor = random.sample([i / 10. for i in range(10, 181, 5)], k=1)[0]


if random.random() > 0.5:
    controlnet_img = apply_gaussian_blur(controlnet_img, ksize=int(blur_strength), sigmaX=blur_strength / 2)            

if random.random() > 0.5:
    # Apply Guided Filter
    controlnet_img = apply_guided_filter(controlnet_img, radius, eps, scale_factor)

# Resize image
controlnet_img = cv2.resize(controlnet_img, (int(W / scale_factor), int(H / scale_factor)), interpolation=cv2.INTER_AREA)
controlnet_img = cv2.resize(controlnet_img, (W, H), interpolation=cv2.INTER_CUBIC)

controlnet_img = cv2.cvtColor(controlnet_img, cv2.COLOR_BGR2RGB)
controlnet_img = Image.fromarray(controlnet_img)

# need to resize the image resolution to 1024 * 1024 or same bucket resolution to get the best performance

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
# Code to Use Tile var

Use more detail prompt to regerate can help!

```python
from diffusers import ControlNetModel, StableDiffusionXLControlNetPipeline, AutoencoderKL
from diffusers import DDIMScheduler, EulerAncestralDiscreteScheduler
from PIL import Image
import torch
import numpy as np
import cv2

controlnet_conditioning_scale = 1.0  
prompt = "your prompt, the longer the better, you can describe it as detail as possible"
negative_prompt = 'longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality'

eulera_scheduler = EulerAncestralDiscreteScheduler.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", subfolder="scheduler")


controlnet = ControlNetModel.from_pretrained(
    "xinsir/controlnet-tile-sdxl-1.0",
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

controlnet_img = cv2.imread("your original image path")
height, width, _  = controlnet_img.shape
ratio = np.sqrt(1024. * 1024. / (width * height))
W, H = int(width * ratio), int(height * ratio)

crop_w, crop_h = 0, 0
controlnet_img = cv2.resize(controlnet_img, (W, H))
controlnet_img = cv2.cvtColor(controlnet_img, cv2.COLOR_BGR2RGB)
controlnet_img = Image.fromarray(controlnet_img)

# need to resize the image resolution to 1024 * 1024 or same bucket resolution to get the best performance
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


# Code to Use Tile super

performance may unstable and next version is optimizing!

```python
from diffusers import ControlNetModel, StableDiffusionXLControlNetPipeline, AutoencoderKL
from diffusers import DDIMScheduler, EulerAncestralDiscreteScheduler
from PIL import Image
import torch
import numpy as np
import cv2

controlnet_conditioning_scale = 1.0  
prompt = "your prompt, the longer the better, you can describe it as detail as possible"
negative_prompt = 'longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality'

eulera_scheduler = EulerAncestralDiscreteScheduler.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", subfolder="scheduler")


controlnet = ControlNetModel.from_pretrained(
    "xinsir/controlnet-tile-sdxl-1.0",
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

controlnet_img = cv2.imread("your original image path")
height, width, _  = controlnet_img.shape
ratio = np.sqrt(1024. * 1024. / (width * height))
W, H = int(width * ratio) // 48 * 48, int(height * ratio) // 48 * 48
controlnet_img = cv2.resize(controlnet_img, (W, H))
controlnet_img = cv2.cvtColor(controlnet_img, cv2.COLOR_BGR2RGB)
controlnet_img = Image.fromarray(controlnet_img)

# need to resize the image resolution to 1024 * 1024 or same bucket resolution to get the best performance
target_width = W // 3
target_height = H // 3

for i in range(3):  # 两行
  for j in range(3):  # 两列
    left = j * target_width
    top = i * target_height
    right = left + target_width
    bottom = top + target_height

    # 根据计算的边界裁剪图像
    cropped_image = controlnet_img.crop((left, top, right, bottom))
    cropped_image = cropped_image.resize((W, H))

    images.append(cropped_image)

seed = random.randint(0, 2147483647)
generator = torch.Generator('cuda').manual_seed(seed)

result_images = []
for sub_img in images:
  new_width, new_height = W, H
  out = pipe(prompt=[prompt]*1,
                    image=sub_img, 
                    control_image=sub_img,
                    negative_prompt=[negative_prompt]*1,
                    generator=generator,
                    width=new_width, 
                    height=new_height,
                    num_inference_steps=30,
                    crops_coords_top_left=(W, H),
                    target_size=(W, H),
                    original_size=(W * 2, H * 2),
                )
  result_images.append(out.images[0])

new_im = Image.new('RGB', (new_width*3, new_height*3))
# 拼接图片到新的图像上
new_im.paste(result_images[0], (0, 0))  
new_im.paste(result_images[1], (new_width, 0))
new_im.paste(result_images[2], (new_width * 2, 0))
new_im.paste(result_images[3], (0, new_height))
new_im.paste(result_images[4], (new_width, new_height))  
new_im.paste(result_images[5], (new_width * 2, new_height))
new_im.paste(result_images[6], (0, new_height * 2))
new_im.paste(result_images[7], (new_width, new_height * 2))
new_im.paste(result_images[8], (new_width * 2, new_height * 2))  

new_im.save(f"your image save path, png format is usually better than jpg or webp in terms of image quality but got much bigger")

```