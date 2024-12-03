---
library_name: transformers
language:
- en
pipeline_tag: image-feature-extraction
license: cc-by-nc-4.0
inference: false
---

# nomic-embed-vision-v1: Expanding the Latent Space

`nomic-embed-vision-v1` is a high performing vision embedding model that shares the same embedding space as [nomic-embed-text-v1](https://huggingface.co/nomic-ai/nomic-embed-text-v1).

All Nomic Embed Text models are now **multimodal**!

| Name                             | Imagenet 0-shot | Datacomp (Avg. 38) | MTEB      |
| :-------------------------------:| :-------------- | :----------------- | :------:  | 
| `nomic-embed-vision-v1.5`        | **71.0**        | **56.8**           | 62.28     | 
| `nomic-embed-vision-v1`          | 70.7            | 56.7               | **62.39** |
| OpenAI CLIP ViT B/16             | 68.3            | 56.3               | 43.82     |
| Jina CLIP v1                     | 59.1            | 52.2               | 60.1      |


## Hosted Inference API

The easiest way to get started with Nomic Embed is through the Nomic Embedding API.

Generating embeddings with the `nomic` Python client is as easy as 
```python
from nomic import embed
import numpy as np

output = embed.image(
    images=[
        "image_path_1.jpeg",
        "image_path_2.png",
    ],
    model='nomic-embed-vision-v1',
)

print(output['usage'])
embeddings = np.array(output['embeddings'])
print(embeddings.shape)
```
For more information, see the [API reference](https://docs.nomic.ai/reference/endpoints/nomic-embed-vision)

## Data Visualization
Click the Nomic Atlas map below to visualize a 100,000 sample CC3M comparing the Vision and Text Embedding Space!


[![image/webp](https://cdn-uploads.huggingface.co/production/uploads/607997c83a565c15675055b3/aKJogjDQ4BBiYGRIIrFMa.webp)](https://atlas.nomic.ai/data/nomic-multimodal-series/cc3m-100k-image-bytes-v15/map)

## Training Details

We align our vision embedder to the text embedding by employing a technique similar to [LiT](https://arxiv.org/abs/2111.07991) but instead lock the text embedder!

For more details, see the Nomic Embed Vision Technical Report (soon to be released!) and corresponding [blog post](https://blog.nomic.ai/posts/nomic-embed-vision)

Training code is released in the `contrastors` [repository](https://github.com/nomic-ai/contrastors)

## Usage

Remember `nomic-embed-text` *requires* prefixes and so, when using Nomic Embed in multimodal RAG scenarios (e.g. text to image retrieval),
you should use the `search_query: ` prefix. 


### Transformers

```python
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel, AutoImageProcessor
from PIL import Image
import requests

processor = AutoImageProcessor.from_pretrained("nomic-ai/nomic-embed-vision-v1")
vision_model = AutoModel.from_pretrained("nomic-ai/nomic-embed-vision-v1", trust_remote_code=True)

url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(image, return_tensors="pt")

img_emb = vision_model(**inputs).last_hidden_state
img_embeddings = F.normalize(img_emb[:, 0], p=2, dim=1)
```

Additionally, you can perform multimodal retrieval!

```python

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

sentences = ['search_query: What are cute animals to cuddle with?', 'search_query: What do cats look like?']

tokenizer = AutoTokenizer.from_pretrained('nomic-ai/nomic-embed-text-v1')
text_model = AutoModel.from_pretrained('nomic-ai/nomic-embed-text-v1', trust_remote_code=True)
text_model.eval()

encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

with torch.no_grad():
    model_output = text_model(**encoded_input)

text_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
text_embeddings = F.normalize(text_embeddings, p=2, dim=1)

print(torch.matmul(img_embeddings, text_embeddings.T))
```


# Join the Nomic Community

- Nomic: [https://nomic.ai](https://nomic.ai)
- Discord: [https://discord.gg/myY5YDR8z8](https://discord.gg/myY5YDR8z8)
- Twitter: [https://twitter.com/nomic_ai](https://twitter.com/nomic_ai)
