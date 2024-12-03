---
pipeline_tag: text-to-image
widget:
- text: >-
    Food photography style photo RAW,piece of fried grilled meat, splashes of ketchup and mustard sauce, (rosemary), spices, exceptional shallow depth-of-field capabilities, atmospheric haze blur,vivid colors,high quality textures of materials, volumetric textures, coating textures, metal textures . Appetizing, professional, culinary, high-resolution, commercial, highly detailed
  output:
    url: steakj.png 
- text: >-
     amazing quality, sci-fi, desert landscape,  a massive dragon crashing through the dunes, epic scene, fabulous, knight running away
  output:
    url: dragon.png  
- text: >-
     Super Closeup Portrait, action shot, Profoundly dark whitish meadow, glass flowers, Stains, space grunge style, Jeanne d'Arc wearing White Olive green used styled Cotton frock, Wielding thin silver sword, Sci-fi vibe, dirty, noisy, Vintage monk style, very detailed, hd, cinematic, 2k 
  output:
    url: final_output_02499_.png 
- text: >-
     lizard
  output:
    url: liz.jpeg 
license: gpl-3.0 
---
<Gallery />

Who needs upscalers? 
-
The TempestV0.1 Initiative is a powerhouse in image generation, leveraging an unparalleled dataset of over 6 million images. The collection's vast scale, with resolutions from 1400x2100 to 4800x7200, encompasses 200GB of high-quality content.

With a groundbreaking 3 million iterations in its training cycle, TempestV0.1 underscores the rigorous effort input by its creator. This training intensity notably eclipses that of all other contemporarie models.
TempestV0.1 shatters the conventional limits of image generation, particularly in delivering unparalleled detail and texture. 

due to the distrabution diffrenece loras will not work with this model at higher resolutions. 
_____________________________________________________________________________________________________________________________________________________
What is the diffrence between Base and Artistic?
-

Base is the pure 100% trained model without any special loras or models throw into the mix. 
suggested settings for Base are:

cfg: 7 to 8

steps: 60 to 80

Artistic is less overall cohesive at larger sizes but has much more flare and stylistic promise. (Proteus+Tempest=Artistic Tempest)
suggested settings for Artistic are:

cfg: 3 to 8

steps: 60 to 80

both of these checkpoints have there place and are seperate for ease of understanding for the user.

supported sizes:
| 2048x1024 | 1920x1088 |
_____________________________________________________________________________________________________________________________________________________
please support the work I do through donating to me on: https://www.buymeacoffee.com/DataVoid or following me on https://twitter.com/DataPlusEngine