---
license: other
license_name: deepseek
license_link: LICENSE
pipeline_tag: image-text-to-text
---

## 1. Introduction

Introducing DeepSeek-VL, an open-source Vision-Language (VL) Model designed for real-world vision and language understanding applications. DeepSeek-VL possesses general multimodal understanding capabilities, capable of processing logical diagrams, web pages, formula recognition, scientific literature, natural images, and embodied intelligence in complex scenarios.

[DeepSeek-VL: Towards Real-World Vision-Language Understanding](https://arxiv.org/abs/2403.05525)

[**Github Repository**](https://github.com/deepseek-ai/DeepSeek-VL)

Haoyu Lu*, Wen Liu*, Bo Zhang**, Bingxuan Wang, Kai Dong, Bo Liu, Jingxiang Sun, Tongzheng Ren, Zhuoshu Li, Hao Yang, Yaofeng Sun, Chengqi Deng, Hanwei Xu, Zhenda Xie, Chong Ruan (*Equal Contribution, **Project Lead)

![](https://github.com/deepseek-ai/DeepSeek-VL/blob/main/images/sample.jpg)


### 2. Model Summary

DeepSeek-VL-1.3b-chat is a tiny vision-language model. It uses the [SigLIP-L](https://huggingface.co/timm/ViT-L-16-SigLIP-384) as the vision encoder supporting 384 x 384 image input 
and is constructed based on the DeepSeek-LLM-1.3b-base which is trained on an approximate corpus of 500B text tokens. The whole DeepSeek-VL-1.3b-base model is finally trained around 400B vision-language tokens.
The DeepSeek-VL-1.3b-chat is an instructed version based on [DeepSeek-VL-1.3b-base](https://huggingface.co/deepseek-ai/deepseek-vl-1.3b-base).


## 3. Quick Start

### Installation

On the basis of `Python >= 3.8` environment, install the necessary dependencies by running the following command:


```shell
git clone https://github.com/deepseek-ai/DeepSeek-VL
cd DeepSeek-VL

pip install -e .
```

### Simple Inference Example

```python
import torch
from transformers import AutoModelForCausalLM

from deepseek_vl.models import VLChatProcessor, MultiModalityCausalLM
from deepseek_vl.utils.io import load_pil_images


# specify the path to the model
model_path = "deepseek-ai/deepseek-vl-1.3b-chat"
vl_chat_processor: VLChatProcessor = VLChatProcessor.from_pretrained(model_path)
tokenizer = vl_chat_processor.tokenizer

vl_gpt: MultiModalityCausalLM = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True)
vl_gpt = vl_gpt.to(torch.bfloat16).cuda().eval()

conversation = [
    {
        "role": "User",
        "content": "<image_placeholder>Describe each stage of this image.",
        "images": ["./images/training_pipelines.png"]
    },
    {
        "role": "Assistant",
        "content": ""
    }
]

# load images and prepare for inputs
pil_images = load_pil_images(conversation)
prepare_inputs = vl_chat_processor(
    conversations=conversation,
    images=pil_images,
    force_batchify=True
).to(vl_gpt.device)

# run image encoder to get the image embeddings
inputs_embeds = vl_gpt.prepare_inputs_embeds(**prepare_inputs)

# run the model to get the response
outputs = vl_gpt.language_model.generate(
    inputs_embeds=inputs_embeds,
    attention_mask=prepare_inputs.attention_mask,
    pad_token_id=tokenizer.eos_token_id,
    bos_token_id=tokenizer.bos_token_id,
    eos_token_id=tokenizer.eos_token_id,
    max_new_tokens=512,
    do_sample=False,
    use_cache=True
)

answer = tokenizer.decode(outputs[0].cpu().tolist(), skip_special_tokens=True)
print(f"{prepare_inputs['sft_format'][0]}", answer)
```

### CLI Chat
```bash

python cli_chat.py --model_path "deepseek-ai/deepseek-vl-1.3b-chat"

# or local path
python cli_chat.py --model_path "local model path"

```

## 4. License

This code repository is licensed under [the MIT License](https://github.com/deepseek-ai/DeepSeek-LLM/blob/HEAD/LICENSE-CODE). The use of DeepSeek-VL Base/Chat models is subject to [DeepSeek Model License](https://github.com/deepseek-ai/DeepSeek-LLM/blob/HEAD/LICENSE-MODEL). DeepSeek-VL series (including Base and Chat) supports commercial use.

## 5. Citation

```
@misc{lu2024deepseekvl,
      title={DeepSeek-VL: Towards Real-World Vision-Language Understanding}, 
      author={Haoyu Lu and Wen Liu and Bo Zhang and Bingxuan Wang and Kai Dong and Bo Liu and Jingxiang Sun and Tongzheng Ren and Zhuoshu Li and Yaofeng Sun and Chengqi Deng and Hanwei Xu and Zhenda Xie and Chong Ruan},
      year={2024},
      eprint={2403.05525},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```

## 6. Contact

If you have any questions, please raise an issue or contact us at [service@deepseek.com](mailto:service@deepseek.com).