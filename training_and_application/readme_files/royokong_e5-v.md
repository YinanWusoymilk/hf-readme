---
library_name: transformers
tags: []
---

# [E5-V: Universal Embeddings with Multimodal Large Language Models](https://arxiv.org/abs/2407.12580)

E5-V is fine-tuned based on lmms-lab/llama3-llava-next-8b.

## Overview
We propose a framework, called E5-V, to adpat MLLMs for achieving multimodal embeddings. E5-V effectively bridges the modality gap between different types of inputs, demonstrating strong performance in multimodal embeddings even without fine-tuning. We also propose a single modality training approach for E5-V, where the model is trained exclusively on text pairs, demonstrating better performance than multimodal training.

More details can be found in https://github.com/kongds/E5-V



## Example
``` python
import torch
import torch.nn.functional as F
import requests
from PIL import Image
from transformers import AutoTokenizer
from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration

llama3_template = '<|start_header_id|>user<|end_header_id|>\n\n{}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n \n'

processor = LlavaNextProcessor.from_pretrained('royokong/e5-v')
model = LlavaNextForConditionalGeneration.from_pretrained('royokong/e5-v', torch_dtype=torch.float16).cuda()

img_prompt = llama3_template.format('<image>\nSummary above image in one word: ')
text_prompt = llama3_template.format('<sent>\nSummary above sentence in one word: ')

urls = ['https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/American_Eskimo_Dog.jpg/360px-American_Eskimo_Dog.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Felis_catus-cat_on_snow.jpg/179px-Felis_catus-cat_on_snow.jpg']
images = [Image.open(requests.get(url, stream=True).raw) for url in urls]

texts = ['A dog sitting in the grass.',
         'A cat standing in the snow.']

text_inputs = processor([text_prompt.replace('<sent>', text) for text in texts], return_tensors="pt", padding=True).to('cuda')
img_inputs = processor([img_prompt]*len(images), images, return_tensors="pt", padding=True).to('cuda')

with torch.no_grad():
    text_embs = model(**text_inputs, output_hidden_states=True, return_dict=True).hidden_states[-1][:, -1, :]
    img_embs = model(**img_inputs, output_hidden_states=True, return_dict=True).hidden_states[-1][:, -1, :]

    text_embs = F.normalize(text_embs, dim=-1)
    img_embs = F.normalize(img_embs, dim=-1)

print(text_embs @ img_embs.t())
```



