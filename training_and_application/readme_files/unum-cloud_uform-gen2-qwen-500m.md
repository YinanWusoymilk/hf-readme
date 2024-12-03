---
library_name: transformers
tags:
- image-captioning
- visual-question-answering
license: apache-2.0
datasets:
- X2FD/LVIS-Instruct4V
- BAAI/SVIT
- HuggingFaceH4/ultrachat_200k
language:
- en
pipeline_tag: image-to-text
widget:
  - src: interior.jpg
    example_title: Detailed caption
    output:
      text: "The image showcases a serene and well-lit bedroom. Dominating the scene is a bed, neatly made with a white blanket and a black headboard. Adjacent to the bed, a dresser stands tall, hosting a mirror, a vase, and a flower arrangement. A chair is positioned near the dresser, offering a comfortable spot to sit and relax. The room is adorned with a large window that offers a picturesque view of trees outside. The walls are painted in a soothing shade of white, enhancing the overall ambiance of the space."
  - src: cat.jpg
    example_title: Short caption
    output:
      text: "A white and orange cat stands on its hind legs, reaching towards a wooden table with a white teapot and a basket of red berries. The table is set on a wooden bench, surrounded by orange flowers. The cat's position and actions suggest curiosity and playfulness."
---

<h1 align="center">UForm</h1>
<h3 align="center">
Pocket-Sized Multimodal AI<br/>
For Content Understanding and Generation<br/>
</h3>

## Description 

UForm-Gen is a small generative vision-language model primarily designed for Image Captioning and Visual Question Answering. The model consists of two parts: 

1. CLIP-like ViT-H/14
2. [Qwen1.5-0.5B-Chat](https://huggingface.co/Qwen/Qwen1.5-0.5B-Chat)

The model was pre-trained on the internal image captioning dataset and fine-tuned on public instructions datasets: SVIT, LVIS, VQAs datasets.
The model took one day to train on a DGX-H100 with 8x H100 GPUs.
Thanks to [Nebius.ai](https://nebius.ai) for providing the compute 🤗

### Usage


The generative model can be used to caption images, answer questions about them. Also it is suitable for a multimodal chat.

```python
from transformers import AutoModel, AutoProcessor

model = AutoModel.from_pretrained("unum-cloud/uform-gen2-qwen-500m", trust_remote_code=True)
processor = AutoProcessor.from_pretrained("unum-cloud/uform-gen2-qwen-500m", trust_remote_code=True)

prompt = "Question or Instruction"
image = Image.open("image.jpg")

inputs = processor(text=[prompt], images=[image], return_tensors="pt")
with torch.inference_mode():
     output = model.generate(
        **inputs,
        do_sample=False,
        use_cache=True,
        max_new_tokens=256,
        eos_token_id=151645,
        pad_token_id=processor.tokenizer.pad_token_id
    )

prompt_len = inputs["input_ids"].shape[1]
decoded_text = processor.batch_decode(output[:, prompt_len:])[0]
```

You can check examples of different prompts in our demo space.

## Evaluation


| Model                               | LLM Size |  SQA  |  MME   | MMBench  | Average¹ |
| :---------------------------------- | -------: | -----:| ------:| --------:| --------:|
| UForm-Gen2-Qwen-500m                |   0.5B   | 45.5  | 880.1  |  42.0    |   29.31  |
| MobileVLM v2                        |   1.4B   | 52.1  | 1302.8 |  57.7    |   36.81  |
| LLaVA-Phi                           |   2.7B   | 68.4  | 1335.1 |  59.8    |   42.95  |

¹MME scores were divided by 2000 before averaging.
