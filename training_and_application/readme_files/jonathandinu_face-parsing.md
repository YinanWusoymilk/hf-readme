---
language: en
library_name: transformers
tags:
  - vision
  - image-segmentation
  - nvidia/mit-b5
  - transformers.js
  - onnx
datasets:
  - celebamaskhq
---

# Face Parsing

![example image and output](demo.png)

[Semantic segmentation](https://huggingface.co/docs/transformers/tasks/semantic_segmentation) model fine-tuned from [nvidia/mit-b5](https://huggingface.co/nvidia/mit-b5) with [CelebAMask-HQ](https://github.com/switchablenorms/CelebAMask-HQ) for face parsing. For additional options, see the Transformers [Segformer docs](https://huggingface.co/docs/transformers/model_doc/segformer).

> ONNX model for web inference contributed by [Xenova](https://huggingface.co/Xenova).

## Usage in Python

Exhaustive list of labels can be extracted from [config.json](https://huggingface.co/jonathandinu/face-parsing/blob/65972ac96180b397f86fda0980bbe68e6ee01b8f/config.json#L30).

| id  | label      | note              |
| :-: | :--------- | :---------------- |
|  0  | background |                   |
|  1  | skin       |                   |
|  2  | nose       |                   |
|  3  | eye_g      | eyeglasses        |
|  4  | l_eye      | left eye          |
|  5  | r_eye      | right eye         |
|  6  | l_brow     | left eyebrow      |
|  7  | r_brow     | right eyebrow     |
|  8  | l_ear      | left ear          |
|  9  | r_ear      | right ear         |
| 10  | mouth      | area between lips |
| 11  | u_lip      | upper lip         |
| 12  | l_lip      | lower lip         |
| 13  | hair       |                   |
| 14  | hat        |                   |
| 15  | ear_r      | earring           |
| 16  | neck_l     | necklace          |
| 17  | neck       |                   |
| 18  | cloth      | clothing          |

```python
import torch
from torch import nn
from transformers import SegformerImageProcessor, SegformerForSemanticSegmentation

from PIL import Image
import matplotlib.pyplot as plt
import requests

# convenience expression for automatically determining device
device = (
    "cuda"
    # Device for NVIDIA or AMD GPUs
    if torch.cuda.is_available()
    else "mps"
    # Device for Apple Silicon (Metal Performance Shaders)
    if torch.backends.mps.is_available()
    else "cpu"
)

# load models
image_processor = SegformerImageProcessor.from_pretrained("jonathandinu/face-parsing")
model = SegformerForSemanticSegmentation.from_pretrained("jonathandinu/face-parsing")
model.to(device)

# expects a PIL.Image or torch.Tensor
url = "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6"
image = Image.open(requests.get(url, stream=True).raw)

# run inference on image
inputs = image_processor(images=image, return_tensors="pt").to(device)
outputs = model(**inputs)
logits = outputs.logits  # shape (batch_size, num_labels, ~height/4, ~width/4)

# resize output to match input image dimensions
upsampled_logits = nn.functional.interpolate(logits,
                size=image.size[::-1], # H x W
                mode='bilinear',
                align_corners=False)

# get label masks
labels = upsampled_logits.argmax(dim=1)[0]

# move to CPU to visualize in matplotlib
labels_viz = labels.cpu().numpy()
plt.imshow(labels_viz)
plt.show()
```

## Usage in the browser (Transformers.js)

```js
import {
  pipeline,
  env,
} from "https://cdn.jsdelivr.net/npm/@xenova/transformers@2.14.0";

// important to prevent errors since the model files are likely remote on HF hub
env.allowLocalModels = false;

// instantiate image segmentation pipeline with pretrained face parsing model
model = await pipeline("image-segmentation", "jonathandinu/face-parsing");

// async inference since it could take a few seconds
const output = await model(url);

// each label is a separate mask object
// [
//   { score: null, label: 'background', mask: transformers.js RawImage { ... }}
//   { score: null, label: 'hair', mask: transformers.js RawImage { ... }}
//    ...
// ]
for (const m of output) {
  print(`Found ${m.label}`);
  m.mask.save(`${m.label}.png`);
}
```

### p5.js

Since [p5.js](https://p5js.org/) uses an animation loop abstraction, we need to take care loading the model and making predictions.

```js
// ...

// asynchronously load transformers.js and instantiate model
async function preload() {
  // load transformers.js library with a dynamic import
  const { pipeline, env } = await import(
    "https://cdn.jsdelivr.net/npm/@xenova/transformers@2.14.0"
  );

  // important to prevent errors since the model files are remote on HF hub
  env.allowLocalModels = false;

  // instantiate image segmentation pipeline with pretrained face parsing model
  model = await pipeline("image-segmentation", "jonathandinu/face-parsing");

  print("face-parsing model loaded");
}

// ...
```

[full p5.js example](https://editor.p5js.org/jonathan.ai/sketches/wZn15Dvgh)

### Model Description

- **Developed by:** [Jonathan Dinu](https://twitter.com/jonathandinu)
- **Model type:** Transformer-based semantic segmentation image model
- **License:** non-commercial research and educational purposes
- **Resources for more information:** Transformers docs on [Segformer](https://huggingface.co/docs/transformers/model_doc/segformer) and/or the [original research paper](https://arxiv.org/abs/2105.15203).

## Limitations and Bias

### Bias

While the capabilities of computer vision models are impressive, they can also reinforce or exacerbate social biases. The [CelebAMask-HQ](https://github.com/switchablenorms/CelebAMask-HQ) dataset used for fine-tuning is large but not necessarily perfectly diverse or representative. Also, they are images of.... just celebrities.
