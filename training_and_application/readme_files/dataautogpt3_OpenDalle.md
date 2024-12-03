---
license: cc-by-nc-nd-4.0
pipeline_tag: text-to-image
widget:
- text: '-'
  output:
    url: GBvPhMyWoAAp_fT.jpeg
- text: '-'
  output:
    url: GBvMRyqXMAAX8jj.jpeg
- text: '-'
  output:
    url: GBuwGoJXUAA89jm.jpeg
- text: panther head coming out of smoke, dark, moody, detailed, shadows
  output:
    url: GBvRG6FXcAEOvcG.jpeg
- text: >-
    Manga from the early 1990s, characterized by its surreal aesthetic. The
    artwork is depicted in matte colors and created using a digital medium.
    Notable illustrators include Junji Ito, Yoshiyuki Sadamoto, and Rumiko
    Takahashi.
  output:
    url: ComfyUI_00497_.jpeg
- text: >-
    in the style of artgerm, comic style,3D model, mythical seascape, negative
    space, space quixotic dreams, temporal hallucination, psychedelic, mystical,
    intricate details, very bright neon colors, (vantablack background:1.5),
    pointillism, pareidolia, melting, symbolism, very high contrast, chiaroscuro
  parameters:
    negative_prompt: >-
      bad quality, bad anatomy, worst quality, low quality, low resolution,
      extra fingers, blur, blurry, ugly, wrong proportions, watermark, image
      artifacts, lowres, ugly, jpeg artifacts, deformed, noisy image,
      embedding:ac_neg1,
  output:
    url: ComfyUI_00318_.jpeg
- text: >-
    Contemporary poster art featuring a profile captured in a detailed
    lithograph with fine coal texture, tar and vinyl color palette, set against
    a Chiaroscuro environment with layered depth composition, etched outlines
    within a chromatic Renaissance setting, continent fictional astrology
    elements in a Chiaroscuro daydream shelter, circuitry tone resembling
    emphatic expanded horror themes, utilizing both palette knife and brush
    strokes, matte finish, realized in cinematic abstractions, 8K resolution,
    36.5 mm
  parameters:
    negative_prompt: >-
      nude, naked, porn, ugly, tiling, extra hands, extra drawn feet, Extra
      fingers, poorly drawn face, (oversaturated: 2), (saturated: 1.6), big
      contrast, contrast white burn, white spots overexposed, over saturated,
      extra limbs, blurry, bad anatomy, blurred, watermark, grainy, signature,
      cut off, closed eyes, text, logo embedding:ac_neg1,
  output:
    url: ComfyUI_00488_.jpeg
- text: >-
    Super Closeup Portrait, action shot, Profoundly dark whiteish meadow, glass
    flowers, Stains, space grunge style, Jeanne d Arc wearing White Olive green
    used styled Cotton frock, Wielding thin silver sword, Sci-fi vibe, dirty,
    noisy, Vintage monk style, very detailed, hd,
  parameters:
    negative_prompt: >-
      bad quality, bad anatomy, worst quality, low quality, low resolutions,
      extra fingers, blur, blurry, ugly, wrongs proportions, watermark, image
      artifacts, lowres, ugly, jpeg artifacts, deformed, noisy image
  output:
    url: ComfyUI_00284_.jpeg
- text: >-
    cinematic film still of Kodak Motion Picture Film: (Sharp Detailed Image) An
    Oscar winning movie for Best Cinematography a woman in a kimono standing on
    a subway train in Japan Kodak Motion Picture Film Style, shallow depth of
    field, vignette, highly detailed, high budget, bokeh, cinemascope, moody,
    epic, gorgeous, film grain, grainy,
  parameters:
    negative_prompt: >-
      bad quality, bad anatomy, worst quality, low quality, low resolutions,
      extra fingers, blur, blurry, ugly, wrongs proportions, watermark, image
      artifacts, lowres, ugly, jpeg artifacts, deformed, noisy image
  output:
    url: ComfyUI_00265_.jpeg
---
## This is outdated! newest version 1.1 can be found here! https://huggingface.co/dataautogpt3/OpenDalleV1.1 
# OpenDalle

<Gallery />


I'm thrilled to share an update on a recent project of mine. After some dedicated work, I've developed a highly effective text-to-image model. This innovation results from integrating the DPO model from Hugging Face with several advanced counterparts, including Juggernaut7XL, ALBEDOXL, MEARGEHEAVEN, and a model of my own design. The outcome is a unique fusion that showcases exceptional prompt adherence and semantic understanding, it seems to be a step above base SDXL and a step closer to DALLE-3 in terms of prompt comprehension. Notably, this model excels in interpreting and adhering to the given prompts, focusing more on semantic accuracy than on ultra-high-fidelity image generation.
also available on ```https://civitai.com/models/238116/opendalle ```

## Settings for OpenDalle v1.0

Use these settings for the best results with OpenDalle v1.0:

CFG Scale: Use a CFG scale of 8 to 7

Steps: 60 to 70 steps for more detail, 35 steps for faster results.

Sampler: DPM2

Scheduler: Normal or Karras


## `*.safetensors` for AUTOMATIC1111, ComfyUI, InvokeAI
[Download *.safetensors file](https://huggingface.co/dataautogpt3/OpenDalle/resolve/main/OpenDalle.safetensors?download=true)


## Use it with 🧨 diffusers
```python
from diffusers import AutoPipelineForText2Image
import torch
        
pipeline = AutoPipelineForText2Image.from_pretrained('dataautogpt3/OpenDalle', torch_dtype=torch.float16).to('cuda')        
image = pipeline('Manga from the early 1990s, characterized by its surreal aesthetic. The artwork is depicted in matte colors and created using a digital medium. Notable illustrators include Junji Ito, Yoshiyuki Sadamoto, and Rumiko Takahashi.').images[0]
```

Non-Commercial Personal Use License Agreement

For dataautogpt3/OpenDalle

1. Introduction

This Non-Commercial Personal Use License Agreement ("Agreement") is between Alexander Izquierdo ("Licensor") and the individual or entity ("Licensee") using the Stable Diffusion model with unique merging method and tuning ("Model") hosted on the Hugging Face repository named OpenDalle.

2. Grant of License

a. Licensor hereby grants to Licensee a non-exclusive, non-transferable, non-sublicensable license to use the Model for personal, non-commercial purposes.

b. "Personal, non-commercial purposes" are defined as use that does not involve any form of compensation or monetary gain. This includes, but is not limited to, academic research, educational use, and hobbyist projects.

c. The Licensee is permitted to modify, merge, and use the Model for personal projects, provided that such use adheres to the terms of this Agreement.

3. Ownership and Intellectual Property Rights

a. The Licensor explicitly retains all rights, title, and interest in and to the unique merging method used in the Model. This merging method is the proprietary creation and intellectual property of the Licensor.

b. The Licensee shall not claim ownership, reverse engineer, or attempt to recreate the merging method for any purpose.

c. The Licensor retains all rights, title, and interest in and to the Model, including any modifications or improvements made by the Licensee.

d. The Licensee agrees to attribute the Licensor in any academic or public display of the Model or derivative works.

4. Restrictions

a. The Licensee shall not use the Model or the merging method for any commercial purposes.

b. The Licensee shall not distribute, sublicense, lease, or lend the Model or the merging method to any third party.

c. The Licensee shall not publicly display, perform, or communicate the Model, the merging method, or any derivative works thereof without the prior written consent of the Licensor.

5. Termination

This Agreement will terminate automatically if the Licensee breaches any of its terms and conditions.

6. Disclaimer of Warranties

The Model and the merging method are provided "as is," and the Licensor makes no warranties, express or implied, regarding their performance, reliability, or suitability for any purpose.

7. Limitation of Liability

The Licensor shall not be liable for any damages arising out of or related to the use or inability to use the Model or the merging method.

8. General Provisions

a. This Agreement constitutes the entire agreement between the parties and supersedes all prior agreements and understandings, whether written or oral, relating to its subject matter.

b. Any amendment to this Agreement must be in writing and signed by both parties.

c. This Agreement shall be governed by the laws of Maryland.

IN WITNESS WHEREOF, the parties have executed this Agreement as of the Effective Date.