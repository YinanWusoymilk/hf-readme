---
license: apache-2.0
datasets:
- OpenGVLab/VideoChat2-IT
- Lin-Chen/ShareGPT4V
- liuhaotian/LLaVA-Instruct-150K
language:
- en
metrics:
- accuracy
library_name: transformers
pipeline_tag: visual-question-answering
tags:
- multimodal large language model
- large video-language model
---

<p align="center">
    <img src="https://cdn-uploads.huggingface.co/production/uploads/63913b120cf6b11c487ca31d/ROs4bHIp4zJ7g7vzgUycu.png" width="150" style="margin-bottom: 0.2;"/>
<p>


<h3 align="center"><a href="https://arxiv.org/abs/2406.07476">VideoLLaMA 2: Advancing Spatial-Temporal Modeling and Audio Understanding in Video-LLMs</a></h3>
<h5 align="center"> If you like our project, please give us a star ⭐ on <a href="https://github.com/DAMO-NLP-SG/VideoLLaMA2">Github</a> for the latest update.  </h2>

<p align="center"><video src="https://cdn-uploads.huggingface.co/production/uploads/63913b120cf6b11c487ca31d/Wj7GuqQ0CB9JRoPo6_GoH.webm" width="800"></p>

## 📰 News
* **[2024.06.12]**  Release model weights and the first version of the technical report of VideoLLaMA 2.
* **[2024.06.03]**  Release training, evaluation, and serving codes of VideoLLaMA 2.


## 🌎 Model Zoo
| Model Name     | Type | Visual Encoder | Language Decoder | # Training Frames |
|:-------------------|:--------------:|:----------------|:------------------|:----------------------:|
| [VideoLLaMA2-7B-Base](https://huggingface.co/DAMO-NLP-SG/VideoLLaMA2-7B-Base)  | Base  | [clip-vit-large-patch14-336](https://huggingface.co/openai/clip-vit-large-patch14-336) | [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)  | 8 |
| [VideoLLaMA2-7B](https://huggingface.co/DAMO-NLP-SG/VideoLLaMA2-7B)  | Chat | [clip-vit-large-patch14-336](https://huggingface.co/openai/clip-vit-large-patch14-336) | [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)  | 8 |
| [VideoLLaMA2-7B-16F-Base](https://huggingface.co/DAMO-NLP-SG/VideoLLaMA2-7B-16F-Base)  | Base  | [clip-vit-large-patch14-336](https://huggingface.co/openai/clip-vit-large-patch14-336) | [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)  | 16 |
| [VideoLLaMA2-7B-16F](https://huggingface.co/DAMO-NLP-SG/VideoLLaMA2-7B-16F) (This checkpoint)  | Chat | [clip-vit-large-patch14-336](https://huggingface.co/openai/clip-vit-large-patch14-336) | [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)  | 16 |
| [VideoLLaMA2-8x7B-Base](https://huggingface.co/DAMO-NLP-SG/VideoLLaMA2-8x7B-Base)  | Base | [clip-vit-large-patch14-336](https://huggingface.co/openai/clip-vit-large-patch14-336) | [Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)  | 8 |
| [VideoLLaMA2-8x7B](https://huggingface.co/DAMO-NLP-SG/VideoLLaMA2-8x7B)  | Chat | [clip-vit-large-patch14-336](https://huggingface.co/openai/clip-vit-large-patch14-336) | [Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)  | 8 |
| [VideoLLaMA2-72B-Base](https://huggingface.co/DAMO-NLP-SG/VideoLLaMA2-72B-Base)  | Base | [clip-vit-large-patch14-336](https://huggingface.co/openai/clip-vit-large-patch14-336) | [Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2-72B-Instruct)  | 8 |
| [VideoLLaMA2-72B](https://huggingface.co/DAMO-NLP-SG/VideoLLaMA2-72B)  | Chat | [clip-vit-large-patch14-336](https://huggingface.co/openai/clip-vit-large-patch14-336) | [Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2-72B-Instruct)  | 8 |


## 🚀 Main Results

### Multi-Choice Video QA & Video Captioning
<p><img src="https://github.com/user-attachments/assets/fbe3e3c2-b0f1-4e29-8b92-bc3611192909" width="800" "/></p>


###  Open-Ended Video QA
<p><img src="https://github.com/user-attachments/assets/cee2efe1-309e-4301-a217-e2a848799953" width="800" "/></p>




## 🤖 Inference with VideoLLaMA2
```python
import sys
sys.path.append('./')
from videollama2 import model_init, mm_infer
from videollama2.utils import disable_torch_init


def inference():
    disable_torch_init()

    # Video Inference
    modal = 'video'
    modal_path = 'assets/cat_and_chicken.mp4' 
    instruct = 'What animals are in the video, what are they doing, and how does the video feel?'
   
    # Image Inference
    modal = 'image'
    modal_path = 'assets/sora.png'
    instruct = 'What is the woman wearing, what is she doing, and how does the image feel?'
    
    model_path = 'DAMO-NLP-SG/VideoLLaMA2-7B-16F'
    model, processor, tokenizer = model_init(model_path)
    output = mm_infer(processor[modal](modal_path), instruct, model=model, tokenizer=tokenizer, do_sample=False, modal=modal)

    print(output)

if __name__ == "__main__":
    inference()
```


## Citation

If you find VideoLLaMA useful for your research and applications, please cite using this BibTeX:
```bibtex
@article{damonlpsg2024videollama2,
  title={VideoLLaMA 2: Advancing Spatial-Temporal Modeling and Audio Understanding in Video-LLMs},
  author={Cheng, Zesen and Leng, Sicong and Zhang, Hang and Xin, Yifei and Li, Xin and Chen, Guanzheng and Zhu, Yongxin and Zhang, Wenqi and Luo, Ziyang and Zhao, Deli and Bing, Lidong},
  journal={arXiv preprint arXiv:2406.07476},
  year={2024},
  url = {https://arxiv.org/abs/2406.07476}
}

@article{damonlpsg2023videollama,
  title = {Video-LLaMA: An Instruction-tuned Audio-Visual Language Model for Video Understanding},
  author = {Zhang, Hang and Li, Xin and Bing, Lidong},
  journal = {arXiv preprint arXiv:2306.02858},
  year = {2023},
  url = {https://arxiv.org/abs/2306.02858}
}
```
