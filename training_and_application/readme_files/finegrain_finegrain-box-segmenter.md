---
license: mit
pipeline_tag: mask-generation
library_name: refiners
tags:
- vision
- image-segmentation
- matting
- remove background
- background
- background-removal
- salient-object-detection
- PyTorch
- refiners
datasets:
- finegrain/finegrain-product-masks-lite
---

# Release note for Finegrain Box Segmenter v0.1

## Demo

If you want to give the Finegrain Box Segmenter a try, the best way to is take a look at the [Finegrain Object Cutter Space](https://huggingface.co/spaces/finegrain/finegrain-object-cutter) we shipped on Hugging Face: it's a fun "prompt to cut out" experience that will enable you to create pixel quality and high resolution cutouts for any object in a photo, by just naming the object.

<video src="https://huggingface.co/finegrain/finegrain-box-segmenter/resolve/main/object_cutter_potted_plant.mp4" autoplay loop></video>

## Motivation

While building Finegrain, we needed a way to create pixel perfect and high resolution cutouts for objects in images. We looked at off-the-shelf solutions, but they simply didn't work for us: 

- On the one hand, traditional background removal models are great at producing HD cutouts, but unfortunately, different people will have different definitions for background and foreground in a given image - a way to prompt these models is missing. 
- On the other hand, new promptable approaches like SAM or SAM2 don't meet the quality bar for the use cases we are pursuing: they are generating internally a 256x256 low resolution mask - with built-in upscaling mechanisms that create artefacts and struggle with complex masks (a la Eiffel Tower). 

The Finegrain Box Segmenter avoids these pitfalls by training [MVANet](https://arxiv.org/abs/2404.07445) to be a box-promptable High Definition (1024x1024) object-cutout model, making no assumption on what is background and what is foreground: users are fully in control.

## License

The Finegrain Box Segmenter is published under the MIT license. Have fun using it in your projects! If you want an optimized version (speed and accuracy wise), we offer an API - just [ping us](mailto:bonjour@lagon.tech)!

## Features

The Finegrain Box Segmenter: 

- produces HD and pixel quality masks,
- gives control to users via box prompting,
- outputs alpha masks: you can use it as an end-to-end Matting Segmenter without any post-processing or trimap.

## Use cases

You should think of the Finegrain Box Segmenter as a way to select an object in a image, with pixel level accuracy, and in high resolution. 

It's a prerequisite for a number of object manipulation tasks like: 

- Remove the background around an object
- Change the background around an object
- Erase an object from an image
- Recolor an object in an image
- Replace an object in an image
- ...

Out-of-the box, the Finegrain Box Segmenter requires a bounding box as an input, but you can easily augment it to enable "prompt to select object" scenarios - see the [Finegrain Object Cutter Hugging Face space](https://huggingface.co/spaces/finegrain/finegrain-object-cutter) for an example implementation.

## Training

Our focus at Finegrain is e-commerce. We therefore trained our model with product datasets coming from 2 sources: 

- **Nfinite**:
    - 7769 images
    - Synthetic data (3D)
    - 14818 pixel quality masks
    - Interior design items
    - Open source: [Nfiniteai/product-masks-sample](https://huggingface.co/datasets/Nfiniteai/product-masks-sample)
- **Finegrain**:
    - 1184 images sourced via hard negative mining
    - Natural data (both studio and UGC photos)
    - 1479 pixel quality masks
    - Common objects
    - Closed source

We moved away from the usual random crop approach. Instead, we designed our custom cropping strategy to make sure the model understands what object to select in a given bounding box. We used batch sizes of 5 to improve the training stability.

## Evaluation

Given our focus on e-commerce, we crafted a specific test set, and in order to ease benchmarking with other models and solutions, we decided to open source part of it as the [Finegrain Product Masks Lite](https://huggingface.co/datasets/finegrain/finegrain-product-masks-lite), containing 120 pixel quality masks of common objects (both UGC and studio photos).

We're using the usual metrics, namely MAE, Smeasure, Emeasure and Dice, computed with [PySODMetrics](https://github.com/lartpang/PySODMetrics). We'll add more later to account for matting aspects (transparent objects) - still a work-in-progress on our end.

| Model | **MAE** ↓ | **Smeasure** ↑ | **Emeasure** ↑ | **Dice** ↑ |
|--|--|--|--|--|
| `briaai/RMBG-1.4` (x) | 0.0226 | 90.7% | 94.3% | 88.5% |
| `ZhengPeng7/BiRefNet` (xx) | 0.0194 | 93.1% | 95.1% | 91.5% |
| `finegrain/finegrain-box-segmenter` | 0.0078 | 97.4% | 98.5% | 96.7% |

(x) Using Cropping with 5% margin

(xx)  Using "Segmentation With Box Guidance" from [BiRefNet](https://github.com/ZhengPeng7/BiRefNet?tab=readme-ov-file#model-zoo)

## Limitations

The Finegrain Box Segmenter v0.1 has a number of limitations that will be tackled in future versions:

- prompting is not baked in yet,
- it struggles when the object is touching the side of the image,
- it doesn't support yet matting of **STM** (Salient Transparent/Meticulous Objects) or **NS** (non-salient) masks (see [Deep Automatic Natural Image Matting](https://www.ijcai.org/proceedings/2021/0111.pdf) for definition of SO/STM/NS),
- it doesn't fully nail yet hard cases like hard shadows, strong reflections or hand-held configurations:

<table>

<thead>
<tr>
<th></th>
<th><strong>Strong reflection</strong></th>
<th><strong>Hard shadow</strong></th>
<th><strong>Hand-held</strong></th>
</tr>
</thead>

<tbody>

<tr>
<td style="text-align: left; vertical-align: middle;">Image</td>
<td><a rel="nofollow" href="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/a1AHBO7fP8GGNMPZX96IX.png"><img alt="image/png" src="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/a1AHBO7fP8GGNMPZX96IX.png"></a></td>
<td><a rel="nofollow" href="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/DTv6BHIIBEfYsjPIGBzIP.png"><img alt="image/png" src="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/DTv6BHIIBEfYsjPIGBzIP.png"></a></td>
<td><a rel="nofollow" href="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/RAacildaNFr4i3idpyOhI.png"><img alt="image/png" src="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/RAacildaNFr4i3idpyOhI.png"></a></td>
</tr>

<tr>
<td style="text-align: left; vertical-align: middle;"><code>briaai/RMBG-1.4</code></td>
<td><a rel="nofollow" href="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/ioF3cKfPmmNEcnffM7tTa.png"><img alt="image/png" src="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/ioF3cKfPmmNEcnffM7tTa.png"></a></td>
<td><a rel="nofollow" href="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/jjmtm8twVl9ZNx3AawcGg.png"><img alt="image/png" src="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/jjmtm8twVl9ZNx3AawcGg.png"></a></td>
<td><a rel="nofollow" href="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/f3MitAdChtoCeOAIYyBfj.png"><img alt="image/png" src="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/f3MitAdChtoCeOAIYyBfj.png"></a></td>
</tr>

<tr>
<td style="text-align: left; vertical-align: middle;"><code>ZhengPeng7/BiRefNet</code></td>
<td><a rel="nofollow" href="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/uGomwlJoRyeIKDXsffhgs.png"><img alt="image/png" src="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/uGomwlJoRyeIKDXsffhgs.png"></a></td>
<td><a rel="nofollow" href="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/8EgCGSPBYDNUwZsOGCX_J.png"><img alt="image/png" src="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/8EgCGSPBYDNUwZsOGCX_J.png"></a></td>
<td><a rel="nofollow" href="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/5elEirUetsWgbFXik6I9A.png"><img alt="image/png" src="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/5elEirUetsWgbFXik6I9A.png"></a></td>
</tr>

<tr>
<td style="text-align: left; vertical-align: middle;"><code>finegrain/finegrain-box-segmenter</code></td>
<td><a rel="nofollow" href="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/nKTnduZsnO9UKO7gY1BHe.png"><img alt="image/png" src="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/nKTnduZsnO9UKO7gY1BHe.png"></a></td>
<td><a rel="nofollow" href="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/iTN_OtOnWjcpNaod4MMzz.png"><img alt="image/png" src="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/iTN_OtOnWjcpNaod4MMzz.png"></a></td>
<td><a rel="nofollow" href="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/b2RHTJrOQxdUf90GX2JRd.png"><img alt="image/png" src="https://cdn-uploads.huggingface.co/production/uploads/632334c533a1e1cf9deebf37/b2RHTJrOQxdUf90GX2JRd.png"></a></td>
</tr>

</tbody>

</table>

## Bias and Fairness

Given our focus on e-commerce, we haven't yet conducted a thorough bias and fairness review. It will be tackled in future releases.

## Usage

### With refiners (https://github.com/finegrain-ai/refiners)

```python
from PIL import Image
from refiners.solutions import BoxSegmenter

input_image = Image.open("input.png") 

# Downloads the weights from finegrain/finegrain-box-segmenter
segmenter = BoxSegmenter()
# box_prompt is (x_min, y_min, x_max, y_max)
mask = segmenter(input_image, box_prompt=(24, 133, 588, 531))
# Or without box_prompt as a background remover
# mask = segmenter(input_image.convert("RGB"))
mask.save("output.png")
```

### With ComfyUI (https://registry.comfy.org/publishers/finegrain/nodes/comfyui-refiners)

Install the `comfyui-refiners` custom nodes:
```
comfy node registry-install comfyui-refiners
```

[Example workflow](https://github.com/finegrain-ai/refiners/blob/main/src/comfyui-refiners/assets/box_segmenter.json)
[![Workflow](https://raw.githubusercontent.com/finegrain-ai/refiners/main/src/comfyui-refiners/assets/box_segmenter.png)](https://github.com/finegrain-ai/refiners/blob/main/src/comfyui-refiners/assets/box_segmenter.json)

### Via our HuggingFace Space (https://huggingface.co/spaces/finegrain/finegrain-object-cutter)

You can directly try it for free on our space, you may get rate-limited by [ZeroGPU](https://huggingface.co/zero-gpu-explorers) though.
You will have better performances running the model yourself, and even more from our API (just [ping us](mailto:bonjour@lagon.tech)!)
