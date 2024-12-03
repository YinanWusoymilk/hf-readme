---
license: other
---
# cotton in mouth.safetensors
Concepts: This LoRA has the effect of inserting the rounded cotton fabric onto the mouths of the characters.

Normally, the weight property should be set to 2, but for prompts that contain many of the tags used in the training dataset tags, less than or equal 1 may also be used.


# skinny.safetensors
Silder: skinny
<img src="https://huggingface.co/SenY/LoRA/resolve/main/skinny%20plot.png">

# short legs.safetensors
Slider: short legs
<img src="https://huggingface.co/SenY/LoRA/resolve/main/short%20legs%20plot.png">

# breathing fire.safetensors
Concepts: Breathing fire
<img src="https://huggingface.co/SenY/LoRA/resolve/main/breathing%20fire.png" width="320">
```prompt example
<lyco:breathing fire:1>
1girl, (breathing fire:1.1), outdoors
```
This LyCORIS is blockweighted.
breathing_fire_full.safetensors is full version.
The full version has the same effect as the general version by applying the following settings in Lora Block Weight.
```prompt example
<lora:breathing_fire_full:1:0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0>
```


# danchi.safetensors
Backgrounds: "Danchi" is Japanese public housing complex.

The common area is tiny, with only a narrow staircase and a landing. The whole place is dingy, dark, and poorly lit.
There is also a park where children who have no access to childcare facilities or sitters can spend their time until their parents come back.
<img src="https://huggingface.co/SenY/LoRA/resolve/main/danchi.webp" width="320">

```prompt example
<lora:danchi:1> 1girl, outdoors
```

<img src="https://huggingface.co/SenY/LoRA/resolve/main/danchi_full.webp" width="320">

```prompt example
<lora:danchi:1> 1girl, indoors, stairs
```
"danchi_full.safetensors"  is the variation in which unnecessary layers are not discarded. Weights should be weakened.

The full version has the same effect as the general version by applying the following settings in Lora Block Weight.
```
<lora:danchi_full:1:0,0.9,0.9,0,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0,0.9,0.9,0.9,0.9,0,0,0,0.9,0>
```

# potty.safetensors
![](https://imgur.com/8vyT15Nm.jpg)
Concepts: For toilet training.
```prompt example
<lora:potty:1> 1girl, potty, sitting
```
I think "sitting" is more acceptable, though "sitting" and "squatting" are also acceptable.

Letting her wear non-white sneakers or socks may improve her chances of success in potty training.

# naked_ribbon.safetensors
![](https://imgur.com/fDrEEoVm.jpg)
Concepts: This loha draws a person with a ribbon wrapped directly around bare skin.
```prompt example
<lora:naked_ribbon:1> 1girl, nrc
```
The file in the title is trained 20 epochs. A file named "naked_ribbon_66e.safetensors" has also been uploaded. This one is over-trained.

See also https://www.pixiv.net/artworks/106100764

# studio_microphone.safetensors
![](https://i.imgur.com/ULjILxpm.jpg)
Concepts: These is a condenser microphone that is used for singers and voice actors who need high-quality sound recording in professional studios.
```prompt example
<lora:studio_microphone:1>
headphones, upper body, hand on headphones, looking at another, singing, music studio, open mouth
```
Auxiliary tokens may be used to control the direction of the microphone. (Not very reliable).
for bottom up
```prompt example
<lora:studio_microphone:1> qx
```
for top down
```prompt example
<lora:studio_microphone:1> jv
```
Do not use the word '''microphone''' in a positive prompt. In fact, it may be better to use it in negative prompts.

# double_v.safetensors
![](https://imgur.com/99QRjJCm.jpg)
Councepts: ✌ double v ✌
```prompt example
<lora:double_v:1> 1girl, wvu
```

# tux.safetensors
![](https://imgur.com/jjNm1hAm.jpg)
Character: tux
```prompt example
<lora:tux:1> tux, penguin
```

# otl.safetensors
![](https://i.imgur.com/yTzTtljm.jpg)
Concepts: otl means "One-piece swimsuit TanLine".
```prompt example
<lora:otl:1> otl, tan, micro bikini
```
You must always include **"tan"** or **"dark skin"** in the prompt. 

This LoRA is strongly influenced by Ro-500 desutte.
You can lessen the impact of her dominance by specifying the hair color and by putting "hair flower" in the negative prompt desutte.

see also https://www.pixiv.net/artworks/105095203

# backpack.safetensors
![](https://i.imgur.com/G3ucTvUm.jpg)
Concepts: A randoseru is a firm-sided backpack made of stitched firm leather or leather-like synthetic material, most commonly used in Japan by elementary schoolchildren. 
```prompt example
<lora:backpack:1> backpack, female child
```

# smock.safetensors
![](https://i.imgur.com/GgZFT7Hm.jpg)
Concepts: A smock is a typical uniform in Japanese kindergartens.
```prompt example
<lora:smock:1> smock, female child
```
It is difficult to get adult women to wear these smocks. It will be converted into just a blue shirt and the LoRA will not be effective.
If needed, the prompt should be emphasized with something like "smock:1.2".


see also https://www.pixiv.net/artworks/105096332

# CheapCotton.safetensors
Concepts: This LoRA transforms the fabric of a girl's particular garment into an inexpensive, stretchy cotton texture.

# guruguru.safetensors
![](https://i.imgur.com/fFgiHltm.jpg)
Concepts: Indicates swirling which represents confusion, dizziness, being overwhelmed, goofiness, or being KO'd. More rare, a character who is drunk or angry can be shown with these eyes.
Also applies when a character's iris design is naturally swirled/spiraled.
```prompt example
<lora:guruguru:1>
```
All eyes change on their own, so there is no need to specify the '@_@' tag.

# hfb.safetensors
Concepts: hfb means "Handjob From Back".
```prompt example
<lora:hfb:1> 1girl, 1boy, hfb, handjob
```

# ootomo sourin.safetensors
Characters: Ootomo Sourin
```prompt example
<lora:ootomo sourin:1> ootomo sourin, hat, armor, dress, holding weapon, cross
```
You must always include **"hat"** or **"blonde hair"** in the prompt.

see also https://rentry.co/sourin_chan