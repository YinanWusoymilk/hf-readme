---
license: creativeml-openrail-m
metrics:
- character
library_name: diffusers
tags:
- LoRa
- embeddings
---
### SD-textual-inversion-embeddings/Lora repo

### Lora Networks

Still Exploring on this training process

prompt: masterpiece, best_quality, clear details,1girl, cowboy_shot, simple_background

with respective LoRa net
![](lora_samples.png)
![](lora_samples2.png)
![](lora_samples3.png)
![](lora_samples4.png)



### Lora characters and outfits
using char-* and outfit-* togeather


masterpiece, best_quality, clear details,1girl, reverse_outfit (pasties) (maebari) high_heels \<lora:outfit-reverseoutfit:1\>, (fullbody), looking_at_viewer, floor , \<lora:char-seia:0.9\>,  

![](seia_outfit_sample.png)



----
### Textual inversion embeddings


### stable diffusion emeddings of characters and outfits

Check each image's PNG info inthe preview folder for excat gen params

# Sample of shinymas/character embeddings
generated with the same prompt with interchanging character phrase (char-X) 

prompt: masterpiece, best_quality, clear details, char-kogane ,shirt,1girl,upper body

Negative prompt: fake_animal_ears, bad_prompt:0.8, (Cropped head), (Extra hands), (extra legs), (cropped), (missing legs), (duplicate), (morbid), cropped, (error), (bad anatomy), text, jpeg artifacts, (ugly), (morbid), (blurry), (low quality), (long leg), (poorly drawn), (bad proportions),


![](shinymas.png)

# Sample of char-toru wearing various outfit embeddings

generated with the same prompt with interchanging outfit phrase (char-X) 

prompt: masterpiece, best_quality, clear details, illustration of char-toru standing wearing outfit-null:1.1, ((full body)) , (smile),(solo), boots, floor,

Negative prompt: fake_animal_ears, bad_prompt:0.8, (Cropped head), (Extra hands), (extra legs), (cropped), (missing legs), (duplicate), (morbid), cropped, (error), (bad anatomy), text, jpeg artifacts, (ugly), (morbid), (blurry), (low quality), (long leg), (poorly drawn), (bad proportions),

![](outfit.png)


![](RO-hina.png)

![](SFsample.png)

![](out1.png)



---
license: osl-3.0
---