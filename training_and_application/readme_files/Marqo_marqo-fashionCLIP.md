---
tags:
- clip
- e-commerce
- fashion
- multimodal retrieval
- transformers.js
- transformers
library_name: open_clip
pipeline_tag: zero-shot-image-classification
license: apache-2.0
language:
- en
metrics:
- precision
- recall
- MRR
---

[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/marqo-ai/marqo-FashionCLIP)

# Marqo-FashionCLIP Model Card
Marqo-FashionCLIP and Marqo-FashionSigLIP outperform the previous state-of-the-art fashion CLIP models (see results below). 
Marqo-FashionCLIP leverages Generalised Contrastive Learning ([GCL](https://www.marqo.ai/blog/generalized-contrastive-learning-for-multi-modal-retrieval-and-ranking)) which allows the model to be trained on not just text descriptions but also categories, style, colors, materials, keywords and fine-details to provide highly relevant search results on fashion products. 
The model was fine-tuned from ViT-B-16 (laion2b_s34b_b88k). 

**Github Page**: [Marqo-FashionCLIP](https://github.com/marqo-ai/marqo-FashionCLIP)

**Blog**: [Marqo Blog](https://www.marqo.ai/blog/search-model-for-fashion)

## Usage

### Hugging Face

The model can be loaded with AutoModel by

```python
from transformers import AutoModel, AutoProcessor
model = AutoModel.from_pretrained('Marqo/marqo-fashionCLIP', trust_remote_code=True)
processor = AutoProcessor.from_pretrained('Marqo/marqo-fashionCLIP', trust_remote_code=True)

import torch
from PIL import Image

image = [Image.open("docs/fashion-hippo.png")]
text = ["a hat", "a t-shirt", "shoes"]
processed = processor(text=text, images=image, padding='max_length', return_tensors="pt")

with torch.no_grad():
    image_features = model.get_image_features(processed['pixel_values'], normalize=True)
    text_features = model.get_text_features(processed['input_ids'], normalize=True)

    text_probs = (100.0 * image_features @ text_features.T).softmax(dim=-1)

print("Label probs:", text_probs)
# [0.99990773, 0.00006382, 0.00002847]
```

### OpenCLIP

The model can be seamlessly used with [OpenCLIP](https://github.com/mlfoundations/open_clip) by

```python
import open_clip
model, preprocess_train, preprocess_val = open_clip.create_model_and_transforms('hf-hub:Marqo/marqo-fashionCLIP')
tokenizer = open_clip.get_tokenizer('hf-hub:Marqo/marqo-fashionCLIP')

import torch
from PIL import Image

image = preprocess_val(Image.open("docs/fashion-hippo.png")).unsqueeze(0)
text = tokenizer(["a hat", "a t-shirt", "shoes"])

with torch.no_grad(), torch.cuda.amp.autocast():
    image_features = model.encode_image(image, normalize=True)
    text_features = model.encode_text(text, normalize=True)

    text_probs = (100.0 * image_features @ text_features.T).softmax(dim=-1)

print("Label probs:", text_probs)
# [0.9998498302475922, 0.000119267522939106, 0.000030902229468640687]
```

### Transformers.js

You can also run the model in JavaScript with the [Transformers.js](https://huggingface.co/docs/transformers.js) library.

First, install it from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:

```bash
npm i @huggingface/transformers
```

Then, compute embeddings as follows:

```js
import { CLIPTextModelWithProjection, CLIPVisionModelWithProjection, AutoTokenizer, AutoProcessor, RawImage, softmax, dot } from '@huggingface/transformers';

const model_id = 'Marqo/marqo-fashionCLIP';

// Load tokenizer and text model
const tokenizer = await AutoTokenizer.from_pretrained(model_id);
const text_model = await CLIPTextModelWithProjection.from_pretrained(model_id);

// Load processor and vision model
const processor = await AutoProcessor.from_pretrained(model_id);
const vision_model = await CLIPVisionModelWithProjection.from_pretrained(model_id);

// Run tokenization
const texts = ['a hat', 'a t-shirt', 'shoes'];
const text_inputs = tokenizer(texts, { padding: 'max_length', truncation: true });

// Compute text embeddings
const { text_embeds } = await text_model(text_inputs);

// Read image and run processor
const image = await RawImage.read('https://raw.githubusercontent.com/marqo-ai/marqo-FashionCLIP/main/docs/fashion-hippo.png');
const image_inputs = await processor(image);

// Compute vision embeddings
const { image_embeds } = await vision_model(image_inputs);

// Compute similarity scores
const normalized_text_embeds = text_embeds.normalize().tolist();
const normalized_image_embeds = image_embeds.normalize().tolist()[0];

const text_probs = softmax(normalized_text_embeds.map((text_embed) => 
    100.0 * dot(normalized_image_embeds, text_embed)
));
console.log(text_probs);
// [0.9998498302475922, 0.000119267522939106, 0.000030902229468640687]
```

## Benchmark Results
Average evaluation results on 6 public multimodal fashion datasets ([Atlas](https://huggingface.co/datasets/Marqo/atlas), [DeepFashion (In-shop)](https://huggingface.co/datasets/Marqo/deepfashion-inshop), [DeepFashion (Multimodal)](https://huggingface.co/datasets/Marqo/deepfashion-multimodal), [Fashion200k](https://huggingface.co/datasets/Marqo/fashion200k), [KAGL](https://huggingface.co/datasets/Marqo/KAGL), and [Polyvore](https://huggingface.co/datasets/Marqo/polyvore)) are reported below: 

**Text-To-Image (Averaged across 6 datasets)**
| Model                      | AvgRecall   | Recall@1   | Recall@10   | MRR       |
|----------------------------|-------------|------------|-------------|-----------|
| Marqo-FashionCLIP          | **0.192**       | **0.094**      | **0.290**       | **0.200**     |
| FashionCLIP2.0                | 0.163       | 0.077      | 0.249       | 0.165     |
| OpenFashionCLIP            | 0.132       | 0.060      | 0.204       | 0.135     |
| ViT-B-16-laion2b_s34b_b88k | 0.174       | 0.088      | 0.261       | 0.180     |

**Category-To-Product (Averaged across 5 datasets)**
| Model                      | AvgP      | P@1       | P@10      | MRR       |
|----------------------------|-----------|-----------|-----------|-----------|
| Marqo-FashionCLIP          | **0.705**     | **0.734**     | 0.676     | **0.776**     |
| FashionCLIP2.0                | 0.684     | 0.681     | **0.686**     | 0.741     |
| OpenFashionCLIP            | 0.646     | 0.653     | 0.639     | 0.720     |
| ViT-B-16-laion2b_s34b_b88k | 0.662     | 0.673     | 0.652     | 0.743     |

**Sub-Category-To-Product (Averaged across 4 datasets)**
| Model                      | AvgP      | P@1       | P@10      | MRR       |
|----------------------------|-----------|-----------|-----------|-----------|
| Marqo-FashionCLIP          | **0.707**     | **0.747**     | **0.667**     | **0.772**     |
| FashionCLIP2.0                | 0.657     | 0.676     | 0.638     | 0.733     |
| OpenFashionCLIP            | 0.598     | 0.619     | 0.578     | 0.689     |
| ViT-B-16-laion2b_s34b_b88k | 0.638     | 0.651     | 0.624     | 0.712     |