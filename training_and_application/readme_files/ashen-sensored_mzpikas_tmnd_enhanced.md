---
license: creativeml-openrail-m
---

# MzPikas TMND Enhanced


![00002-3533137131.jpg](https://s3.amazonaws.com/moonup/production/uploads/63d260547bec3be0c3e82402/ulIKsnXF7Ho1KlA1nARCA.jpeg)

## experimental Attention Agreement Score merge model

Using the sum of negative DAAM cumulative attention scores from teacher models as loss, running neuron-wise merge with AdamW from four teacher models, trained on images with resolution 2048x2048

https://civitai.com/models/27259/tmnd-mix

https://civitai.com/models/47067/pikas-new-generation-v10

https://civitai.com/models/31383/mzmix

https://huggingface.co/Xynon/SD-Silicon/tree/main
## Model does not yield satisfactory result below resolution 2048x1024 during tests.

Tested workflow:

t2i  1024x512   x2 hiresfix SwinIR_4x or 4x-UltraSharp    denoising strength 0.5-0.55  output 2048x1024

i2i  multidiffusion  Euler a or DPM++ 2M Karras  x2 Ultrasharp  Denoising strength 0.35-0.4    output 4096x2048

- Slight face/limb distortion under t2i result can be fixed automatically in i2i step

- reduce the weight of silicon isolation Lora/reduce the overall weight of background prompt/increase the overall weight of character prompt if foreground character does not appear.

- All images have metadata embeded in, please check the demo metadata for optimal prompt format

Lora used is included in repo.

You may also use controlnet in t2i step for character placement.




![00015-2258858428.png](https://s3.amazonaws.com/moonup/production/uploads/63d260547bec3be0c3e82402/vXiQuNlDdiQBdu-5QPet7.png)




![00015-1732540132.png](https://s3.amazonaws.com/moonup/production/uploads/63d260547bec3be0c3e82402/2WgO3yUkhkS7HjdKdMjln.png)






![00005-1054975534.jpg](https://s3.amazonaws.com/moonup/production/uploads/63d260547bec3be0c3e82402/AQH8OnJONdzNQv6d0j1Nq.jpeg)




![00011-2480169264.jpg](https://s3.amazonaws.com/moonup/production/uploads/63d260547bec3be0c3e82402/hM7KgUbSTubIOdqN6cvXh.jpeg)





![00019-1065916204.png](https://s3.amazonaws.com/moonup/production/uploads/63d260547bec3be0c3e82402/fftKr5gmBWYXY9F2INAXB.png)




![00029-3681388676.png](https://s3.amazonaws.com/moonup/production/uploads/63d260547bec3be0c3e82402/pWBaWfDuDDmGS9F1AEStx.png)




![00003-3533137131.jpg](https://s3.amazonaws.com/moonup/production/uploads/63d260547bec3be0c3e82402/1Xiu20rDdnNfPwDEgBudj.jpeg)




![00006-1054975534.png](https://s3.amazonaws.com/moonup/production/uploads/63d260547bec3be0c3e82402/QXhEwqBwBfiyqWGV5ySDq.png)




![00012-4135706202.jpg](https://s3.amazonaws.com/moonup/production/uploads/63d260547bec3be0c3e82402/KyKWyYVYH1h4YAEHDe3OL.jpeg)