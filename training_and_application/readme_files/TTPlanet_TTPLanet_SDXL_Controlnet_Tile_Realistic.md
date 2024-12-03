---
library_name: diffusers
pipeline_tag: image-feature-extraction
tags:
- Controlnet
- Tile
- stable diffustion
license: openrail
---
# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->
Controlnet SDXL Tile model realistic version, fit for both webui extention and comfyui controlnet node.

### Model Description

Here's a refined version of the update notes for the Tile V2:

-Introducing the new Tile V2, enhanced with a vastly improved training dataset and more extensive training steps.

-The Tile V2 now automatically recognizes a wider range of objects without needing explicit prompts.

-I've made significant improvements to the color offset issue. if you are still seeing the significant offset, it's normal, just adding the prompt or use a color fix node.

-The control strength is more robust, allowing it to replace canny+openpose in some conditions.

If you encounter the edge halo issue with t2i or i2i, particularly with i2i, ensure that the preprocessing provides the controlnet image with sufficient blurring. If the output is too sharp, it may result in a 'halo'—a pronounced shape around the edges with high contrast. In such cases, apply some blur before sending it to the controlnet. If the output is too blurry, this could be due to excessive blurring during preprocessing, or the original picture may be too small.

Enjoy the enhanced capabilities of Tile V2!

![TBT9$5UL`53RKP`85JXIZ_H.jpg](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/yS1ax7FWZS7b5Zz1co8_b.jpeg)

![Q5A0[{{0{]I~`KJFCZJ7`}4.jpg](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/HMGmYz7IiLSqfoiMgcmgU.jpeg)

<!-- Provide a longer summary of what this model is. -->
- This is a SDXL based controlnet Tile model, trained with huggingface diffusers sets, fit for Stable diffusion SDXL controlnet.
- It is original trained for my personal realistic model project used for Ultimate upscale process to boost the picture details. with a proper workflow, it can provide a good result for high detailed, high resolution image fix.
- As there is no SDXL Tile available from the most open source, I decide to share this one out.
- I will share my workflow soon as I am still working on it to have better result.
- **I am still working on the better workflow for super upscale as I showed in the example, trust me, it's all real!!! and Enjoy**
- 
![image/png](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/ddFT3326ddNOWBeoFnfZl.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/OETMPhSCVEKdyUvILMsyp.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/lznGyTnKy91AwRmSaCxTF.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/iokmuDnYy7UC47t7AoLc1.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/gjNEgVlr2I2uf9hPJiivu.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/wSZTq340GTG3ojx75HNyH.png)


- **Developed by:** TTPlanet
- **Model type:** Controlnet Tile
- **Language(s) (NLP):** No language limitation


## Uses
- **Important: Tile model is not a upscale model!!! it enhance or change the detial of the original size image, remember this before you use it!**
- This model will not significant change the base model style. it only adding the features to the upscaled pixel blocks....
- --Just use a regular controlnet model in Webui by select as tile model and use tile_resample for Ultimate Upscale script.
- --Just use load controlnet model in comfyui and apply to control net condition.
- --if you try to use it in webui t2i, need proper prompt setup, otherwise it will significant modify the original image color. I don't know the reason, as I don't really use this function.
- --it do perform much better with the image from the datasets. However, everything works fine for the i2i model and what is the place usually the ultimate upscale is applied!!
- **--Please also notice this is a realistic training set, so no comic, animation application are promised.**
- --For tile upscale, set the denoise around 0.3-0.4 to get good result.
- --For controlnet strength, set to 0.9 will be better choice
- --For human image fix, IPA and early stop on controlnet will provide better reslut
- **--Pickup a good realistic base model is important!**
![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/zPyYn2fSFmD1Q07ME0Hkg.jpeg)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/00gDy93frzcF-WH8hh1NS.png)
- **bsides the basic function, Tile can also change the picture style based on you model, please select the preprocessor as None(not resample!!!!) you can build different style from one single picture with great control!**
- Just enjoy  
![image/png](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/RjZiSX1oBXas1y1Tjq_dW.png)
- 
- **additional instruction to use this tile**
- **Part 1：update for style change application instruction（**cloth change and keep consistent pose**）:**

- 1. Open a A1111 webui.

- 2. select a image you want to use for controlnet tile

- 3. remember the setting is like this, make 100% preprocessor is none. and control mode is My prompt is more important.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/RfSSfKxjpxvHSUmswTfhH.png)

- 4. type in the prompts in positive and negative text box, gen the image as you wish. if you want to change the cloth, type like a woman dressed in yellow T-shirt, and change the background like in a shopping mall,

- 5. Hires fix is supported!!!

- 6. You will get the result as below:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/XS-Qi-FuofnPABl5hZAoi.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/641edd91eefe94aff6de024c/KYyRUJjuxg5YKs0UFYUw0.png)

- **Part2： for ultimate sd upscale application**

Here is the simplified workflow just for ultimate upscale, you can modify and add pre process for your image based on the real condition. In my case, I usually make a image to image with 0.1 denoise rate for the real low quality image such as 600*400 to 1200*800 before I through it into this ultimate upscale process.

Please add IPA process if you need the face likes identical, please also add IPA in the raw pre process for low quality image i2i. Remember, over resolution than downscale is always the best way to boost the quality from low resolution image.

https://civitai.com/models/333060/simplified-workflow-for-ultimate-sd-upscale


## Bias, Risks, and Limitations

- **Please do not use it for adult content**

### Recommendations

- Use comfyui to build your own Upscale process, it works fine!!!

- **Special thanks to the Controlnet builder lllyasviel Lvmin Zhang (Lyumin Zhang) who bring so much fun to us, and thanks huggingface make the training set to make the training so smooth.**


## Model Card Contact

--contact me if you want, discord with "ttplanet", Civitai with "ttplanet"
--you can also join the group discussion with QQ gourp number: 294060503