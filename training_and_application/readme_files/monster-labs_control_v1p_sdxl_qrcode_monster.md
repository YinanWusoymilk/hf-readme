---
tags:
- stable-diffusion
- controlnet
- qrcode
license: openrail++
language:
- en
---
# Controlnet QR Code Monster v1 For SDXL

![QR code in shape of a green monster, reading "https://qrcode.monster"](images/monster.png)

##  Model Description

This model is made to generate creative QR codes that still scan.
Illusions should also work well.
Keep in mind that not all generated codes might be readable, but you can try different parameters and prompts to get the desired results.

## How to Use

- **Condition**: QR codes are passed as condition images with a module size of 16px. Use a higher error correction level to make it easier to read (sometimes a lower level can be easier to read if smaller in size). Use a gray background for the rest of the image to make the code integrate better.

- **Prompts**: Use a prompt to guide the QR code generation. The output will highly depend on the given prompt. Some seem to be really easily accepted by the qr code process, some will require careful tweaking to get good results.

- **Controlnet guidance scale**: Set the controlnet guidance scale value:
   - High values: The generated QR code will be more readable.
   - Low values: The generated QR code will be more creative.

### Tips

- For an optimally readable output, try generating multiple QR codes with similar parameters, then choose the best ones.

- Use the Image-to-Image feature to improve the readability of a generated QR code:
  - Decrease the denoising strength to retain more of the original image.
  - Increase the controlnet guidance scale value for better readability.
  A typical workflow for "saving" a code would be :
  Max out the guidance scale and minimize the denoising strength, then bump the strength until the code scans.

## Example Outputs

![A corridor with a perspective illusion](images/corridor.jpg)
![a fruit salad with a perspective illusion](images/fruits.jpg)
![a beautiful landscape with a checkerboard illusion](images/landscape_checkerboard.jpg)

Feel free to experiment with prompts, parameters, and the Image-to-Image feature to achieve the desired QR code output. Good luck and have fun!