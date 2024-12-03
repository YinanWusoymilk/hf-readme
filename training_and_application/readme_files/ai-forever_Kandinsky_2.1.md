---
license: apache-2.0
tags:
- Kandinsky
- text-image
- text2image
- diffusion
- latent diffusion
- mCLIP-XLMR
- mT5
---

# Kandinsky 2.1


[Open In Colab](https://colab.research.google.com/drive/1xSbu-b-EwYd6GdaFPRVgvXBX_mciZ41e?usp=sharing)

[GitHub repository](https://github.com/ai-forever/Kandinsky-2)

[Habr post](https://habr.com/ru/company/sberbank/blog/725282/)

[Demo](https://rudalle.ru/)

## Architecture

Kandinsky 2.1 inherits best practicies from Dall-E 2 and Latent diffusion, while introducing some new ideas.

As text and image encoder it uses CLIP model and diffusion image prior (mapping) between latent spaces of CLIP modalities. This approach increases the visual performance of the model and unveils new horizons in blending images and text-guided image manipulation.

For diffusion mapping of latent spaces we use transformer with num_layers=20, num_heads=32 and hidden_size=2048.

![](https://raw.githubusercontent.com/ai-forever/Kandinsky-2/main/content/kandinsky21.png)

Other architecture parts:

+ Text encoder (XLM-Roberta-Large-Vit-L-14) - 560M
+ Diffusion Image Prior — 1B
+ CLIP image encoder (ViT-L/14) - 427M
+ Latent Diffusion U-Net - 1.22B
+ MoVQ encoder/decoder - 67M


![](https://raw.githubusercontent.com/ai-forever/Kandinsky-2/main/content/einstein.png)


# Authors

+ Arseniy Shakhmatov: [Github](https://github.com/cene555), [Blog](https://t.me/gradientdip)
+ Anton Razzhigaev: [Github](https://github.com/razzant), [Blog](https://t.me/abstractDL)
+ Aleksandr Nikolich: [Github](https://github.com/AlexWortega), [Blog](https://t.me/lovedeathtransformers)
+ Vladimir Arkhipkin: [Github](https://github.com/oriBetelgeuse)
+ Igor Pavlov: [Github](https://github.com/boomb0om)
+ Andrey Kuznetsov: [Github](https://github.com/kuznetsoffandrey)
+ Denis Dimitrov: [Github](https://github.com/denndimitrov)