---
license: other
pipeline_tag: visual-question-answering
---


<p align="center">
    <img src="logo_4k_en.png" width="600"/>
<p>

<p align="center">
    <b><font size="6">InternLM-XComposer2-4KHD</font></b> 
<p>

<div align="center">

[💻Github Repo](https://github.com/InternLM/InternLM-XComposer)

[Paper](https://arxiv.org/abs/2401.16420)

</div>

**InternLM-XComposer2-4KHD** is a general vision-language large model (VLLM) based on [InternLM2](https://github.com/InternLM/InternLM), with the capability of 4K resolution image understanding.

### Import from Transformers
To load the InternLM-XComposer2-4KHD model using Transformers, use the following code:
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
ckpt_path = "internlm/internlm-xcomposer2-4khd-7b"
tokenizer = AutoTokenizer.from_pretrained(ckpt_path, trust_remote_code=True).cuda()
# Set `torch_dtype=torch.floatb16` to load model in bfloat16, otherwise it will be loaded as float32 and might cause OOM Error.
model = AutoModelForCausalLM.from_pretrained(ckpt_path, torch_dtype=torch.bfloat16, trust_remote_code=True).cuda()
model = model.eval()
```

## Quickstart
We provide a simple example to show how to use InternLM-XComposer with 🤗 Transformers.
```python
import torch
from transformers import AutoModel, AutoTokenizer

torch.set_grad_enabled(False)

# init model and tokenizer
model = AutoModel.from_pretrained('internlm/internlm-xcomposer2-4khd-7b', torch_dtype=torch.bfloat16, trust_remote_code=True).cuda().eval()
tokenizer = AutoTokenizer.from_pretrained('internlm/internlm-xcomposer2-4khd-7b', trust_remote_code=True)

###############
# First Round
###############

query1 = '<ImageHere>Illustrate the fine details present in the image'
image = './example.webp'
with torch.cuda.amp.autocast():
  response, his = model.chat(tokenizer, query=query, image=image, hd_num=55, history=[], do_sample=False, num_beams=3)
print(response)
# The image is a vibrant and colorful infographic that showcases 7 graphic design trends that will dominate in 2021. The infographic is divided into 7 sections, each representing a different trend. 
# Starting from the top, the first section focuses on "Muted Color Palettes", highlighting the use of muted colors in design.
# The second section delves into "Simple Data Visualizations", emphasizing the importance of easy-to-understand data visualizations. 
# The third section introduces "Geometric Shapes Everywhere", showcasing the use of geometric shapes in design. 
# The fourth section discusses "Flat Icons and Illustrations", explaining how flat icons and illustrations are being used in design. 
# The fifth section is dedicated to "Classic Serif Fonts", illustrating the resurgence of classic serif fonts in design.
# The sixth section explores "Social Media Slide Decks", illustrating how slide decks are being used on social media. 
# Finally, the seventh section focuses on "Text Heavy Videos", illustrating the trend of using text-heavy videos in design. 
# Each section is filled with relevant images and text, providing a comprehensive overview of the 7 graphic design trends that will dominate in 2021.

###############
# Second Round
###############
query1 = 'what is the detailed explanation of the third part.'
with torch.cuda.amp.autocast():
  response, _ = model.chat(tokenizer, query=query1, image=image, hd_num=55, history=his, do_sample=False, num_beams=3)
print(response)
# The third part of the infographic is about "Geometric Shapes Everywhere". It explains that last year, designers used a lot of
# flowing and abstract shapes in their designs. However, this year, they have been replaced with rigid, hard-edged geometric
# shapes and patterns. The hard edges of a geometric shape create a great contrast against muted colors.



```

### Open Source License
The code is licensed under Apache-2.0, while model weights are fully open for academic research and also allow free commercial usage. To apply for a commercial license, please fill in the application form (English)/申请表（中文）. For other questions or collaborations, please contact internlm@pjlab.org.cn.