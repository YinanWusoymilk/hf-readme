---
license: apache-2.0
pipeline_tag: text-to-image
tags:
- stable diffusion
- ip adapter
---

# IP Composition Adapter

This adapter for Stable Diffusion 1.5 and SDXL is designed to inject the general composition of an image into the model while mostly ignoring the style and content. Meaning a portrait of a person waving their left hand will result in an image of a completely different person waving with their left hand.

### Follow Me
I do a lot of experiments and other things. To keep up to date, follow me on [Twitter](https://twitter.com/ostrisai).

### Thanks

I want to give a special thanks to [POM](https://huggingface.co/peteromallet) with [BANODOCO](https://huggingface.co/BANODOCO). This was their idea, I just trained it. Full credit goes to them.

## Usage

Use just like other IP+ adapters from [h94/IP-Adapter](https://huggingface.co/h94/IP-Adapter). For both SD1.5 and SDXL variants, use the CLIP vision encoder ([CLIP-H](https://huggingface.co/h94/IP-Adapter/tree/main/models/image_encoder))

You may need to lower the CFG to around 3 for best results, especially on the SDXL variant.

### How is it different from control nets?

Control nets are more rigid. A control net will spatially align an image to nearly perfectly match the control image. The composition adapter allows the control to be more flexible.

## SDXL Examples

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%202024-03-19%20195340.png" alt="1" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%202024-03-19%20194130.png" alt="1" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%202024-03-19%20193948.png" alt="1" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%202024-03-19%20193802.png" alt="1" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%202024-03-19%20193632.png" alt="1" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%202024-03-19%20192659.png" alt="1" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%202024-03-19%20192445.png" alt="1" width="100%"/>

## SD 1.5 Examples

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%20from%202024-03-16%2013-06-32.jpg" alt="1" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%20from%202024-03-16%2013-09-57.jpg" alt="2" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%20from%202024-03-16%2013-11-27.jpg" alt="3" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%20from%202024-03-16%2013-13-19.jpg" alt="4" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%20from%202024-03-16%2013-56-51.jpg" alt="5" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%20from%202024-03-16%2014-00-31.jpg" alt="6" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%20from%202024-03-16%2014-04-41.jpg" alt="7" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%20from%202024-03-16%2014-09-31.jpg" alt="8" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%20from%202024-03-16%2014-11-10.jpg" alt="9" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%20from%202024-03-16%2014-13-26.jpg" alt="10" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%20from%202024-03-16%2014-19-20.jpg" alt="11" width="100%"/>

<img src="https://huggingface.co/ostris/ip-composition-adapter/resolve/main/resources/Screenshot%20from%202024-03-16%2014-21-50.jpg?download=true" alt="12" width="100%"/>