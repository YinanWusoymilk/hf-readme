---
pipeline_tag: visual-question-answering
language:
- en
- zh
datasets:
- HaoyeZhang/RLHF-V-Dataset
- Yirany/UniMM-Chat
- HuggingFaceM4/VQAv2
- liuhaotian/LLaVA-Instruct-150K
---

[GitHub](https://github.com/OpenBMB/MiniCPM-V) | [Demo](https://huggingface.co/spaces/openbmb/MiniCPM-V-2)

## News <!-- omit in toc -->
* [2024.05.20] 🔥 The GPT-4V level multimodal model [**MiniCPM-Llama3-V 2.5**](https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5) is out.
* [2024.04.23] MiniCPM-V 2.0 supports [vLLM](#vllm) now!
* [2024.04.18] We create a HuggingFace Space to host the demo of MiniCPM-V 2.0 at [here](https://huggingface.co/spaces/openbmb/MiniCPM-V-2)!
* [2024.04.17] MiniCPM-V 2.0 supports deploying [WebUI Demo](https://github.com/OpenBMB/MiniCPM-V/blob/8a1f766b85595a8095651eed9a44a83a965b305b/README_en.md#minicpm-v-) now!
* [2024.04.15] MiniCPM-V 2.0 supports [fine-tuning](https://github.com/modelscope/swift/blob/main/docs/source/Multi-Modal/minicpm-v-2最佳实践.md) with the SWIFT framework!
* [2024.04.12] We open-source MiniCPM-V-2.0, which achieves comparable performance with Gemini Pro in understanding scene text and outperforms strong Qwen-VL-Chat 9.6B and Yi-VL 34B on <a href="https://rank.opencompass.org.cn/leaderboard-multimodal">OpenCompass</a>, a comprehensive evaluation over 11 popular benchmarks. Click <a href="https://openbmb.vercel.app/minicpm-v-2">here</a> to view the MiniCPM-V 2.0 technical blog.

## MiniCPM-V 2.0


**MiniCPM-V 2.8B** is a strong multimodal large language model for efficient end-side deployment. The model is built based on SigLip-400M and [MiniCPM-2.4B](https://github.com/OpenBMB/MiniCPM/), connected by a perceiver resampler. Our latest version, **MiniCPM-V 2.0** has several notable features. 

- 🔥 **State-of-the-art Performance.** 

  MiniCPM-V 2.0 achieves **state-of-the-art performance** on multiple benchmarks (including OCRBench, TextVQA, MME, MMB, MathVista, etc) among models under 7B parameters. It even **outperforms strong Qwen-VL-Chat 9.6B, CogVLM-Chat 17.4B, and Yi-VL 34B on OpenCompass, a comprehensive evaluation over 11 popular benchmarks**. Notably, MiniCPM-V 2.0 shows **strong OCR capability**, achieving **comparable performance to Gemini Pro in scene-text understanding**, and **state-of-the-art performance on OCRBench** among open-source models.

- 🏆 **Trustworthy Behavior.** 

  LMMs are known for suffering from hallucination, often generating text not factually grounded in images. MiniCPM-V 2.0 is **the first end-side LMM aligned via multimodal RLHF for trustworthy behavior** (using the recent [RLHF-V](https://rlhf-v.github.io/) [CVPR'24] series technique). This allows the model to **match GPT-4V in preventing hallucinations** on Object HalBench.

- 🌟 **High-Resolution Images at Any Aspect Raito.**

  MiniCPM-V 2.0 can accept **1.8 million pixels (e.g., 1344x1344) images at any aspect ratio**. This enables better perception of fine-grained visual information such as small objects and optical characters, which is achieved via a recent technique from [LLaVA-UHD](https://arxiv.org/pdf/2403.11703.pdf).

- ⚡️ **High Efficiency.** 

  MiniCPM-V 2.0 can be **efficiently deployed on most GPU cards and personal computers**, and **even on end devices such as mobile phones**. For visual encoding, we compress the image representations into much fewer tokens via a perceiver resampler. This allows MiniCPM-V 2.0 to operate with **favorable memory cost and speed during inference even when dealing with high-resolution images**.



- 🙌 **Bilingual Support.** 

  MiniCPM-V 2.0 **supports strong bilingual multimodal capabilities in both English and Chinese**. This is enabled by generalizing multimodal capabilities across languages, a technique from [VisCPM](https://arxiv.org/abs/2308.12038) [ICLR'24].

## Evaluation <!-- omit in toc -->

<div align="center">
    <img src=/openbmb/MiniCPM-V-2.0/resolve/main/assets/minicpmv-2-peformance2.png width=100% />
</div>
Results on TextVQA, DocVQA, OCRBench, OpenCompass, MME, MMBench, MMMU, MathVista, LLaVA Bench, Object HalBench.
<div align="center">
    <img src=/openbmb/MiniCPM-V-2.0/resolve/main/assets/minicpmv-2-benchmark.png width=140% />
</div>


## Examples <!-- omit in toc -->

<table align="center">
    <p align="center">
      <img src="assets/minicpmv2-cases_2.png" width=95%/>
    </p>
</table>

We deploy MiniCPM-V 2.0 on end devices. The demo video is the raw screen recording on a Xiaomi 14 Pro without edition.

<table align="center">
    <p align="center">
      <img src="assets/station.gif" width=40% style="display:inline-block;"/>
      <img src="assets/london_car.gif" width=40% style="display:inline-block;"/>
    </p>
</table>




## Demo
Click here to try out the Demo of [MiniCPM-V 2.0](https://huggingface.co/spaces/openbmb/MiniCPM-V-2).

## Deployment on Mobile Phone
MiniCPM-V 2.0 can be deployed on mobile phones with Android and Harmony operating systems. 🚀 Try it out [here](https://github.com/OpenBMB/mlc-MiniCPM).

## Inference with vLLM<a id="vllm"></a>

<details>
<summary>Click to see how to inference with vLLM </summary>
Because our pull request to vLLM is still waiting for reviewing, we fork this repository to build and test our vLLM demo. Here are the steps:

1. Clone our version of vLLM:
```shell
git clone https://github.com/OpenBMB/vllm.git
```
2. Install vLLM:
```shell
cd vllm
pip install -e .
```
3. Install timm: 
```shell
pip install timm=0.9.10
```
4. Run our demo:
```shell
python examples/minicpmv_example.py 
```
</details>


## Usage
Inference using Huggingface transformers on Nivdia GPUs or Mac with MPS (Apple silicon or AMD GPUs). Requirements tested on python 3.10：
```
Pillow==10.1.0
timm==0.9.10
torch==2.1.2
torchvision==0.16.2
transformers==4.36.0
sentencepiece==0.1.99
```

```python
# test.py
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained('openbmb/MiniCPM-V-2', trust_remote_code=True, torch_dtype=torch.bfloat16)
# For Nvidia GPUs support BF16 (like A100, H100, RTX3090)
model = model.to(device='cuda', dtype=torch.bfloat16)
# For Nvidia GPUs do NOT support BF16 (like V100, T4, RTX2080)
#model = model.to(device='cuda', dtype=torch.float16)
# For Mac with MPS (Apple silicon or AMD GPUs).
# Run with `PYTORCH_ENABLE_MPS_FALLBACK=1 python test.py`
#model = model.to(device='mps', dtype=torch.float16)

tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-V-2', trust_remote_code=True)
model.eval()

image = Image.open('xx.jpg').convert('RGB')
question = 'What is in the image?'
msgs = [{'role': 'user', 'content': question}]

res, context, _ = model.chat(
    image=image,
    msgs=msgs,
    context=None,
    tokenizer=tokenizer,
    sampling=True,
    temperature=0.7
)
print(res)
```

Please look at [GitHub](https://github.com/OpenBMB/MiniCPM-V) for more detail about usage.


## MiniCPM-V 1.0 <!-- omit in toc -->
Please see the info about MiniCPM-V 1.0 [here](https://huggingface.co/openbmb/MiniCPM-V).

## License
#### Model License
* The code in this repo is released under the [Apache-2.0](https://github.com/OpenBMB/MiniCPM/blob/main/LICENSE) License. 
* The usage of MiniCPM-V series model weights must strictly follow [MiniCPM Model License.md](https://github.com/OpenBMB/MiniCPM/blob/main/MiniCPM%20Model%20License.md).
* The models and weights of MiniCPM are completely free for academic research. after filling out a ["questionnaire"](https://modelbest.feishu.cn/share/base/form/shrcnpV5ZT9EJ6xYjh3Kx0J6v8g) for registration, are also available for free commercial use.


#### Statement
* As a LLM, MiniCPM-V 2.0 generates contents by learning a large mount of texts, but it cannot comprehend, express personal opinions or make value judgement. Anything generated by MiniCPM-V 2.0 does not represent the views and positions of the model developers
* We will not be liable for any problems arising from the use of the MinCPM-V open Source model, including but not limited to data security issues, risk of public opinion, or any risks and problems arising from the misdirection, misuse, dissemination or misuse of the model.

## Other Multimodal Projects from Our Team

[VisCPM](https://github.com/OpenBMB/VisCPM/tree/main) | [RLHF-V](https://github.com/RLHF-V/RLHF-V) | [LLaVA-UHD](https://github.com/thunlp/LLaVA-UHD)

## Citation

If you find our work helpful, please consider citing the following papers

```bib
@article{yu2023rlhf,
  title={Rlhf-v: Towards trustworthy mllms via behavior alignment from fine-grained correctional human feedback},
  author={Yu, Tianyu and Yao, Yuan and Zhang, Haoye and He, Taiwen and Han, Yifeng and Cui, Ganqu and Hu, Jinyi and Liu, Zhiyuan and Zheng, Hai-Tao and Sun, Maosong and others},
  journal={arXiv preprint arXiv:2312.00849},
  year={2023}
}
@article{viscpm,
    title={Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages}, 
    author={Jinyi Hu and Yuan Yao and Chongyi Wang and Shan Wang and Yinxu Pan and Qianyu Chen and Tianyu Yu and Hanghao Wu and Yue Zhao and Haoye Zhang and Xu Han and Yankai Lin and Jiao Xue and Dahai Li and Zhiyuan Liu and Maosong Sun},
    journal={arXiv preprint arXiv:2308.12038},
    year={2023}
}
@article{xu2024llava-uhd,
  title={{LLaVA-UHD}: an LMM Perceiving Any Aspect Ratio and High-Resolution Images},
  author={Xu, Ruyi and Yao, Yuan and Guo, Zonghao and Cui, Junbo and Ni, Zanlin and Ge, Chunjiang and Chua, Tat-Seng and Liu, Zhiyuan and Huang, Gao},
  journal={arXiv preprint arXiv:2403.11703},
  year={2024}
}
@article{yao2024minicpmvgpt4vlevelmllm,
  title={MiniCPM-V: A GPT-4V Level MLLM on Your Phone},
  author={Yao, Yuan and Yu, Tianyu and Zhang, Ao and Wang, Chongyi and Cui, Junbo and Zhu, Hongji and Cai, Tianchi and Li, Haoyu and Zhao, Weilin and He, Zhihui and Chen, Qianyu and Zhou, Huarong and Zou, Zhensheng and Zhang, Haoye and Hu, Shengding and Zheng, Zhi and Zhou, Jie and Cai, Jie and Han, Xu and Zeng, Guoyang and Li, Dahai and Liu, Zhiyuan and Sun, Maosong},
  journal={arXiv preprint arXiv:2408.01800},
  year={2024},
  url={https://arxiv.org/abs/2408.01800},
}
```