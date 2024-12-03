---
tags:
- vision
---

# Model Card: clip-rsicd

## Model Details

This model is a fine-tuned [CLIP by OpenAI](https://huggingface.co/openai/clip-vit-base-patch32). It is designed with an aim to improve zero-shot image classification, text-to-image and image-to-image retrieval specifically on remote sensing images.

### Model Date

July 2021

### Model Type

The base model uses a ViT-B/32 Transformer architecture as an image encoder and uses a masked self-attention Transformer as a text encoder. These encoders are trained to maximize the similarity of (image, text) pairs via a contrastive loss.

### Model Version

We release several checkpoints for `clip-rsicd` model. Refer to [our github repo](https://github.com/arampacha/CLIP-rsicd#evaluation-results) for performance metrics on zero-shot classification for each of those.

### Training

To reproduce the fine-tuning procedure one can use released [script](https://github.com/arampacha/CLIP-rsicd/blob/master/run_clip_flax_tv.py). 
The model was trained using batch size 1024, adafactor optimizer with linear warmup and decay with peak learning rate 1e-4 on 1 TPU-v3-8.
Full log of the training run can be found on [WandB](https://wandb.ai/wandb/hf-flax-clip-rsicd/runs/2dj1exsw).

### Demo

Check out the model text-to-image and image-to-image capabilities using [this demo](https://huggingface.co/spaces/sujitpal/clip-rsicd-demo).


### Documents

- [Fine-tuning CLIP on RSICD with HuggingFace and flax/jax on colab using TPU](https://colab.research.google.com/github/arampacha/CLIP-rsicd/blob/master/nbs/Fine_tuning_CLIP_with_HF_on_TPU.ipynb)


### Use with Transformers

```python
from PIL import Image
import requests

from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("flax-community/clip-rsicd-v2")
processor = CLIPProcessor.from_pretrained("flax-community/clip-rsicd-v2")

url = "https://raw.githubusercontent.com/arampacha/CLIP-rsicd/master/data/stadium_1.jpg"
image = Image.open(requests.get(url, stream=True).raw)

labels = ["residential area", "playground", "stadium", "forest", "airport"]
inputs = processor(text=[f"a photo of a {l}" for l in labels], images=image, return_tensors="pt", padding=True)

outputs = model(**inputs)
logits_per_image = outputs.logits_per_image # this is the image-text similarity score
probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities
for l, p in zip(labels, probs[0]):
    print(f"{l:<16} {p:.4f}")
```
[Try it on colab](https://colab.research.google.com/github/arampacha/CLIP-rsicd/blob/master/nbs/clip_rsicd_zero_shot.ipynb)


## Model Use

### Intended Use

The model is intended as a research output for research communities. We hope that this model will enable researchers to better understand and explore zero-shot, arbitrary image classification. 

In addition, we can imagine applications in defense and law enforcement, climate change and global warming, and even some consumer applications. A partial list of applications can be found [here](https://github.com/arampacha/CLIP-rsicd#applications). In general we think such models can be useful as digital assistants for humans engaged in searching through large collections of images.

We also hope it can be used for interdisciplinary studies of the potential impact of such models - the CLIP paper includes a discussion of potential downstream impacts to provide an example for this sort of analysis.


#### Primary intended uses

The primary intended users of these models are AI researchers.

We primarily imagine the model will be used by researchers to better understand robustness, generalization, and other capabilities, biases, and constraints of computer vision models.



## Data

The model was trained on publicly available remote sensing image captions datasets. Namely [RSICD](https://github.com/201528014227051/RSICD_optimal), [UCM](https://mega.nz/folder/wCpSzSoS#RXzIlrv--TDt3ENZdKN8JA) and [Sydney](https://mega.nz/folder/pG4yTYYA#4c4buNFLibryZnlujsrwEQ). More information on the datasets used can be found on [our project page](https://github.com/arampacha/CLIP-rsicd#dataset).



## Performance and Limitations

### Performance

| Model-name                       | k=1   | k=3   | k=5   | k=10  |
| -------------------------------- | ----- | ----- | ----- | ----- |
| original CLIP                    | 0.572 | 0.745 | 0.837 | 0.939 |
| clip-rsicd-v2 (this model)       | **0.883** | **0.968** | **0.982** | **0.998** |

## Limitations

The model is fine-tuned on RSI data but can contain some biases and limitations of the original CLIP model. Refer to [CLIP model card](https://huggingface.co/openai/clip-vit-base-patch32#limitations) for details on those.
