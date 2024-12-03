---
language:
- en
thumbnail: >-
  https://s3.amazonaws.com/moonup/production/uploads/1678229171792-62de447b4dcb9177d4bd876c.png
tags:
- compvis
- vae
---
# Blessed Vae
Contrast version of the regular nai/any vae

Good for models that are low on contrast even after using said vae

There's a few VAEs in here
1. blessed.vae.pt : VAE from salt's example VAEs
2. blessed-fix.vae.pt : blessed VAE with Patch Encoder (to fix [this issue](https://github.com/sALTaccount/VAE-BlessUp/issues/1))
3. blessed2.vae.pt : Customly tuned by me

## Differences
```diff
- Left: AnythingVAE (funfact: it's just NAI VAE but renamed)
+ Right: BlessedVAE
```
![xyz_grid-0000-1394207229-masterpiece best quality ultra-detailed hatsune miku from behind upper body looking at viewer _ negative space biolumibb045ad033d22d3956be73a7444d3c63c3ea717c.png](https://s3.amazonaws.com/moonup/production/uploads/1678229171792-62de447b4dcb9177d4bd876c.png)

![xyz_grid-0000-1394207229-masterpiece, best quality, ultra-detailed, hatsune miku, from behind, upper body, looking at viewer, _, negative space, (biolumi.png](https://s3.amazonaws.com/moonup/production/uploads/1678275075891-62de447b4dcb9177d4bd876c.png)

![xyz_grid-0001-2877626089-masterpiece, best quality, hatsune miku, white gown, angel, angel wings, golden halo, dark background, upper body, (closed mouth.png](https://s3.amazonaws.com/moonup/production/uploads/1678275080981-62de447b4dcb9177d4bd876c.png)

![SPOILER_tmp857utfr1.png](https://s3.amazonaws.com/moonup/production/uploads/1678275640402-62de447b4dcb9177d4bd876c.png)

![xyz_grid-0002-601402825-masterpiece, best quality, hatsune miku, white gown, angel, angel wings, golden halo, dark background, upper body, (closed mouth.png](https://s3.amazonaws.com/moonup/production/uploads/1678275680281-62de447b4dcb9177d4bd876c.png)

## Credits
- Salt for the model and script
- Reuploaded from https://github.com/sALTaccount/VAE-BlessUp example