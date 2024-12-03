---
license: other
pipeline_tag: visual-question-answering
---


<p align="center">
    <img src="logo_en.png" width="400"/>
<p>

<p align="center">
    <b><font size="6">InternLM-XComposer2</font></b> 
<p>

<div align="center">

[💻Github Repo](https://github.com/InternLM/InternLM-XComposer)

[Paper](https://arxiv.org/abs/2401.16420)

</div>

**InternLM-XComposer2** is a vision-language large model (VLLM) based on [InternLM2](https://github.com/InternLM/InternLM) for advanced text-image comprehension and composition. 

We release InternLM-XComposer2 series in two versions:

- InternLM-XComposer2-VL: The pretrained VLLM model with InternLM2 as the initialization of the LLM, achieving strong performance on various multimodal benchmarks.
- InternLM-XComposer2: The finetuned VLLM for *Free-from Interleaved Text-Image Composition*.


### Import from Transformers
To load the InternLM-XComposer2-VL-7B model using Transformers, use the following code:
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
ckpt_path = "internlm/internlm-xcomposer2-vl-7b"
tokenizer = AutoTokenizer.from_pretrained(ckpt_path, trust_remote_code=True).cuda()
# Set `torch_dtype=torch.float16` to load model in float16, otherwise it will be loaded as float32 and might cause OOM Error.
model = AutoModelForCausalLM.from_pretrained(ckpt_path, torch_dtype=torch.float16, trust_remote_code=True).cuda()
model = model.eval()
```

## Quickstart
We provide a simple example to show how to use InternLM-XComposer with 🤗 Transformers.
```python
import torch
from transformers import AutoModel, AutoTokenizer

torch.set_grad_enabled(False)

# init model and tokenizer
model = AutoModel.from_pretrained('internlm/internlm-xcomposer2-vl-7b', trust_remote_code=True).cuda().eval()
tokenizer = AutoTokenizer.from_pretrained('internlm/internlm-xcomposer2-vl-7b', trust_remote_code=True)

query = '<ImageHere>Please describe this image in detail.'
image = './image1.webp'
with torch.cuda.amp.autocast():
  response, _ = model.chat(tokenizer, query=query, image=image, history=[], do_sample=False)
print(response)
#The image features a quote by Oscar Wilde, "Live life with no excuses, travel with no regret,"
# set against a backdrop of a breathtaking sunset. The sky is painted in hues of pink and orange,
# creating a serene atmosphere. Two silhouetted figures stand on a cliff, overlooking the horizon.
# They appear to be hiking or exploring, embodying the essence of the quote.
# The overall scene conveys a sense of adventure and freedom, encouraging viewers to embrace life without hesitation or regrets.

```

### Open Source License
The code is licensed under Apache-2.0, while model weights are fully open for academic research and also allow free commercial usage. To apply for a commercial license, please fill in the application form (English)/申请表（中文）. For other questions or collaborations, please contact internlm@pjlab.org.cn.