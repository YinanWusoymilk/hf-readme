---
pipeline_tag: image-text-to-text
language:
- multilingual
datasets:
- openbmb/RLAIF-V-Dataset
library_name: transformers
tags:
- minicpm-v
- vision
- ocr
- custom_code
---


<h1>A GPT-4V Level Multimodal LLM on Your Phone</h1>

[GitHub](https://github.com/OpenBMB/MiniCPM-V) | [Demo](https://huggingface.co/spaces/openbmb/MiniCPM-Llama3-V-2_5) | <a href="https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/wechat.md" target="_blank"> WeChat</a> 


## News <!-- omit in toc -->

#### 📌 Pinned


* [2024.08.10] 🚀🚀🚀 MiniCPM-Llama3-V 2.5 is now fully supported by [official](https://github.com/ggerganov/llama.cpp) llama.cpp! GGUF models of various sizes are available [here](https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5-gguf).
* [2024.08.06] 🔥🔥🔥 We open-source [MiniCPM-V 2.6](https://huggingface.co/openbmb/MiniCPM-V-2_6), which outperforms GPT-4V on single image, multi-image and video understanding. It advances popular features of MiniCPM-Llama3-V 2.5, and can support real-time video understanding on iPad. Try it now!
* [2024.08.03] MiniCPM-Llama3-V 2.5 technical report is released! See [here](https://github.com/OpenBMB/MiniCPM-V/tree/main/docs/MiniCPM_Llama3_V_25_technical_report.pdf).
* [2024.07.19] MiniCPM-Llama3-V 2.5 supports vLLM now! See [here](https://github.com/OpenBMB/MiniCPM-V/tree/main?tab=readme-ov-file#vllm).
* [2024.05.28] 🚀🚀🚀 MiniCPM-Llama3-V 2.5 now fully supports its feature in llama.cpp and ollama! Please pull the latest code **of our provided forks** ([llama.cpp](https://github.com/OpenBMB/llama.cpp/blob/minicpm-v2.5/examples/minicpmv/README.md), [ollama](https://github.com/OpenBMB/ollama/tree/minicpm-v2.5/examples/minicpm-v2.5)). GGUF models in various sizes are available [here](https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5-gguf/tree/main). MiniCPM-Llama3-V 2.5 series is **not supported by the official repositories yet**, and we are working hard to merge PRs. Please stay tuned! You can visit our [GitHub](https://github.com/OpenBMB/MiniCPM-V) repository for more information!
* [2024.05.28] 💫 We now support LoRA fine-tuning for MiniCPM-Llama3-V 2.5, using only 2 V100 GPUs! See more statistics [here](https://github.com/OpenBMB/MiniCPM-V/tree/main/finetune#model-fine-tuning-memory-usage-statistics).
* [2024.05.23] 🔥🔥🔥 MiniCPM-V tops GitHub Trending and HuggingFace Trending! Our demo, recommended by Hugging Face Gradio’s official account, is available [here](https://huggingface.co/spaces/openbmb/MiniCPM-Llama3-V-2_5). Come and try it out!

<br>

* [2024.06.03] Now, you can run MiniCPM-Llama3-V 2.5 on multiple low VRAM GPUs(12 GB or 16 GB) by distributing the model's layers across multiple GPUs. For more details, Check this [link](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/inference_on_multiple_gpus.md).
* [2024.05.25] MiniCPM-Llama3-V 2.5 now supports streaming outputs and customized system prompts. Try it at [here](#usage)
* [2024.05.24]  We release the [MiniCPM-Llama3-V 2.5 gguf](https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5-gguf), which supports [llama.cpp](https://github.com/OpenBMB/MiniCPM-V/tree/main?tab=readme-ov-file#inference-with-llamacpp) inference and provides a 6~8 token/s smooth decoding on mobile phones. Try it now!
* [2024.05.23] 🔍 We've released a comprehensive comparison between Phi-3-vision-128k-instruct and MiniCPM-Llama3-V 2.5, including benchmarks evaluations, multilingual capabilities, and inference efficiency 🌟📊🌍🚀. Click [here](https://github.com/OpenBMB/MiniCPM-V/blob/main/docs/compare_with_phi-3_vision.md) to view more details.
* [2024.05.20] We open-soure MiniCPM-Llama3-V 2.5, it has improved OCR capability and supports 30+ languages, representing the first end-side MLLM achieving GPT-4V level performance! We provide [efficient inference](#deployment-on-mobile-phone) and [simple fine-tuning](https://github.com/OpenBMB/MiniCPM-V/blob/main/finetune/readme.md). Try it now!


## Model Summary

**MiniCPM-Llama3-V 2.5** is the latest model in the MiniCPM-V series. The model is built on SigLip-400M and Llama3-8B-Instruct with a total of 8B parameters. It exhibits a significant performance improvement over MiniCPM-V 2.0. Notable features of MiniCPM-Llama3-V 2.5 include:

- 🔥 **Leading Performance.**
  MiniCPM-Llama3-V 2.5 has achieved an average score of 65.1 on OpenCompass, a comprehensive evaluation over 11 popular benchmarks. **With only 8B parameters, it surpasses widely used proprietary models like GPT-4V-1106, Gemini Pro, Claude 3 and Qwen-VL-Max** and greatly outperforms other Llama 3-based MLLMs.

- 💪 **Strong OCR Capabilities.**
  MiniCPM-Llama3-V 2.5 can process images with any aspect ratio and up to 1.8 million pixels (e.g., 1344x1344), achieving an **700+ score on OCRBench, surpassing proprietary models such as GPT-4o, GPT-4V-0409, Qwen-VL-Max and Gemini Pro**. Based on recent user feedback, MiniCPM-Llama3-V 2.5 has now enhanced full-text OCR extraction, table-to-markdown conversion, and other high-utility capabilities, and has further strengthened its instruction-following and complex reasoning abilities, enhancing multimodal interaction experiences.

- 🏆 **Trustworthy Behavior.**
  Leveraging the latest [RLAIF-V](https://github.com/RLHF-V/RLAIF-V/) method (the newest technology in the [RLHF-V](https://github.com/RLHF-V) [CVPR'24] series), MiniCPM-Llama3-V 2.5 exhibits more trustworthy behavior. It achieves **10.3%** hallucination rate on Object HalBench, lower than GPT-4V-1106 (13.6%), achieving the best-level performance within the open-source community. [Data released](https://huggingface.co/datasets/openbmb/RLAIF-V-Dataset).

- 🌏 **Multilingual Support.**
  Thanks to the strong multilingual capabilities of Llama 3 and the cross-lingual generalization technique from [VisCPM](https://github.com/OpenBMB/VisCPM), MiniCPM-Llama3-V 2.5 extends its bilingual (Chinese-English) multimodal capabilities to **over 30 languages including German, French, Spanish, Italian, Korean, Japanese etc.** [All Supported Languages](./assets/minicpm-llama-v-2-5_languages.md).

- 🚀 **Efficient Deployment.**
  MiniCPM-Llama3-V 2.5 systematically employs **model quantization, CPU optimizations, NPU optimizations and compilation optimizations**, achieving high-efficiency deployment on edge devices. For mobile phones with Qualcomm chips, we have integrated the NPU acceleration framework QNN into llama.cpp for the first time. After systematic optimization, MiniCPM-Llama3-V 2.5 has realized a **150-fold acceleration in multimodal large model end-side image encoding** and a **3-fold increase in language decoding speed**.

-  💫  **Easy Usage.**
  MiniCPM-Llama3-V 2.5 can be easily used in various ways: (1) [llama.cpp](https://github.com/OpenBMB/llama.cpp/blob/minicpm-v2.5/examples/minicpmv/README.md) and [ollama](https://github.com/OpenBMB/ollama/tree/minicpm-v2.5/examples/minicpm-v2.5) support for efficient CPU inference on local devices, (2) [GGUF](https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5-gguf) format quantized models in 16 sizes, (3) efficient [LoRA](https://github.com/OpenBMB/MiniCPM-V/tree/main/finetune#lora-finetuning) fine-tuning with only 2 V100 GPUs, (4) [streaming output](https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5#usage), (5) quick local WebUI demo setup with [Gradio](https://github.com/OpenBMB/MiniCPM-V/blob/main/web_demo_2.5.py) and [Streamlit](https://github.com/OpenBMB/MiniCPM-V/blob/main/web_demo_streamlit-2_5.py), and (6) interactive demos on [HuggingFace Spaces](https://huggingface.co/spaces/openbmb/MiniCPM-Llama3-V-2_5).

### Evaluation <!-- omit in toc -->

Results on TextVQA, DocVQA, OCRBench, OpenCompass MultiModal Avg , MME, MMBench, MMMU, MathVista, LLaVA Bench, RealWorld QA, Object HalBench.

<div align="center">
    <img src="https://cdn-uploads.huggingface.co/production/uploads/64abc4aa6cadc7aca585dddf/v2KE3wqQgM05ZW3dH2wbx.png" width="110%" />
</div>


Evaluation results of multilingual LLaVA Bench 
<div align="center">
    <img src="assets/minicpmv-llama3-v2.5/llavabench_compare.png" width="110%" />
</div>


### Examples <!-- omit in toc -->

<table align="center">
    <p align="center">
      <img src="assets/minicpmv-llama3-v2.5/cases_all.png" width=95%/>
    </p>
</table>

We deploy MiniCPM-Llama3-V 2.5 on end devices. The demo video is the raw screen recording on a Xiaomi 14 Pro without edition.

<table align="center">
    <p align="center">
      <img src="assets/gif_cases/ticket.gif" width=40% style="display:inline-block;"/>
      <img src="assets/gif_cases/meal_plan.gif" width=40% style="display:inline-block;"/>
    </p>
</table>

<table align="center">
    <p align="center">
      <img src="assets/gif_cases/1-4.gif" width=80%/>
    </p>
</table>



## Demo
Click here to try out the Demo of [MiniCPM-Llama3-V 2.5](https://huggingface.co/spaces/openbmb/MiniCPM-Llama3-V-2_5).

## Deployment on Mobile Phone
Coming soon.

## Usage
Inference using Huggingface transformers on NVIDIA GPUs. Requirements tested on python 3.10：
```
Pillow==10.1.0
torch==2.1.2
torchvision==0.16.2
transformers==4.40.0
sentencepiece==0.1.99
```

```python
# test.py
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True, torch_dtype=torch.float16)
model = model.to(device='cuda')

tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True)
model.eval()

image = Image.open('xx.jpg').convert('RGB')
question = 'What is in the image?'
msgs = [{'role': 'user', 'content': question}]

res = model.chat(
    image=image,
    msgs=msgs,
    tokenizer=tokenizer,
    sampling=True, # if sampling=False, beam_search will be used by default
    temperature=0.7,
    # system_prompt='' # pass system_prompt if needed
)
print(res)

## if you want to use streaming, please make sure sampling=True and stream=True
## the model.chat will return a generator
res = model.chat(
    image=image,
    msgs=msgs,
    tokenizer=tokenizer,
    sampling=True,
    temperature=0.7,
    stream=True
)

generated_text = ""
for new_text in res:
    generated_text += new_text
    print(new_text, flush=True, end='')
```

Please look at [GitHub](https://github.com/OpenBMB/MiniCPM-V) for more detail about usage.


## Inference with llama.cpp<a id="llamacpp"></a>
MiniCPM-Llama3-V 2.5 can run with llama.cpp now! See our fork of [llama.cpp](https://github.com/OpenBMB/llama.cpp/tree/minicpm-v2.5/examples/minicpmv) for more detail.


## Int4 quantized version
Download the int4 quantized version for lower GPU memory (8GB) usage:  [MiniCPM-Llama3-V-2_5-int4](https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5-int4).

## MiniCPM-V 2.0 <!-- omit in toc -->
Please see the info about MiniCPM-V 2.0 [here](https://huggingface.co/openbmb/MiniCPM-V-2).

## License
#### Model License
* The code in this repo is released under the [Apache-2.0](https://github.com/OpenBMB/MiniCPM/blob/main/LICENSE) License. 
* The usage of MiniCPM-V series model weights must strictly follow [MiniCPM Model License.md](https://github.com/OpenBMB/MiniCPM/blob/main/MiniCPM%20Model%20License.md).
* The models and weights of MiniCPM are completely free for academic research. after filling out a ["questionnaire"](https://modelbest.feishu.cn/share/base/form/shrcnpV5ZT9EJ6xYjh3Kx0J6v8g) for registration, are also available for free commercial use.



#### Statement
* As an LLM, MiniCPM-Llama3-V 2.5 generates contents by learning a large mount of texts, but it cannot comprehend, express personal opinions or make value judgement. Anything generated by MiniCPM-Llama3-V 2.5 does not represent the views and positions of the model developers
* We will not be liable for any problems arising from the use of the MinCPM-V open Source model, including but not limited to data security issues, risk of public opinion, or any risks and problems arising from the misdirection, misuse, dissemination or misuse of the model.

## Key Techniques and Other Multimodal Projects

👏 Welcome to explore key techniques of MiniCPM-V 2.6 and other multimodal projects of our team:

[VisCPM](https://github.com/OpenBMB/VisCPM/tree/main) | [RLHF-V](https://github.com/RLHF-V/RLHF-V) | [LLaVA-UHD](https://github.com/thunlp/LLaVA-UHD)  | [RLAIF-V](https://github.com/RLHF-V/RLAIF-V)

## Citation

If you find our work helpful, please consider citing our papers 📝 and liking this project ❤️！

```bib
@article{yao2024minicpmv,
      title={MiniCPM-V: A GPT-4V Level MLLM on Your Phone}, 
      author={Yao, Yuan and Yu, Tianyu and Zhang, Ao and Wang, Chongyi and Cui, Junbo and Zhu, Hongji and Cai, Tianchi and Li, Haoyu and Zhao, Weilin and He, Zhihui and Chen, Qianyu and Zhou, Huarong and Zou, Zhensheng and Zhang, Haoye and Hu, Shengding and Zheng, Zhi and Zhou, Jie and Cai, Jie and Han, Xu and Zeng, Guoyang and Li, Dahai and Liu, Zhiyuan and Sun, Maosong},
      journal={arXiv preprint 2408.01800},
      year={2024},
}
```