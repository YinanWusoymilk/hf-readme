---
license: apache-2.0
---

# Tele-FLM-1T
Tele-FLM-1T (aka FLM-2-1T) is a 1T open-sourced multilingual large language model that features a stable, efficient pre-training paradigm and enhanced factual judgement capabilities. 
Built upon the decoder-only transformer architecture, it has been trained on approximately 2.3T tokens.
Tele-FLM-1T, currently the largest size among Tele-FLM series, is build upon Tele-FLM (52B) with superior performances at its scale, is capable of dealing with even harder tasks with better performances in all likelihood. 
For now, it's still under evaluation due to limited computing resouces.
In addition to sharing the model weights, we provide the core designs, engineering practices, and training details, anticipating their benefits for both academic and industrial communities.

## Model Details

- **Developed by:** BAAI & TeleAI
- **Language(s):** English; Chinese; Other languages
- **License:** Apache 2.0

## Technical Report

[52B to 1T: Lessons Learned via Tele-FLM Series](https://arxiv.org/pdf/2407.02783)

[Tele-FLM Technical Report](https://arxiv.org/pdf/2404.16645)

## Bias, Risks, and Limitations

Although we've made extensive efforts to thoroughly clean and filter the training corpus for the model, due to the open nature of the dataset, the model may still have picked up on some unsafe examples. Consequently, the model may still generate unexpected content, including but not limited to discrimination, bias, or offensive language. We would like to strongly advise users not to spread any unsafe content generated by the model. The project developers cannot be held responsible for any repercussions stemming from the dissemination of harmful information.



## Training Details

### Model Architecture
Based on growth technology, the Tele-FLM-1T model training is divided into three stages by parameter size: 52B, 102B, and 1TB. Each stage of the model uses the same backbone structure. Tele-FLM models utilize the standard GPT-style decoder-only transformer architecture with a few adjustments: 
- Rotary Positional Embedding (RoPE)
- RMSNorm for normalization
- SwiGLU for activation function
- Linear bias disabled
- Embedding and language model head untied
- Input and output multiplier

Consequently, Tele-FLM-1T is largely compatible with Llama architecturally.
To maximize convenience for the community, we made minimal adjustments to Llama's code to adapt it to Tele-FLM-1T and released it as open source.


| Models        | layer<br>number | attention<br>heads | hidden<br>size | ffn hidden<br>size | vocab<br>size | context<br>length | params<br>count |
| ------------- | --------------- | ------------------ | -------------- | ------------------ | ------------- | ----------------- | --------------- |
| Tele-FLM-52B  | 64              | 64                 | 8,192          | 21,824             | 80,000        | 4,096             | 52.85 B         |
| Tele-FLM-102B | 80              | 80                 | 10,240         | 27,264             | 80,000        | 4,096             | 102.3 B         |
| Tele-FLM-1T   | 140             | 160                | 20,480         | 98,304             | 80,000        | 4,096             | 1,083.74 B      |


### Hardware

Tele-FLM-1T is trained on a cluster of 112 A800 SXM4 GPU servers, each with 8 NVLink A800 GPUs and 2TB of RAM. 
The nodes have varied CPU configurations: 96 nodes with Intel 8358 (128x 2.60GHz) CPUs and 16 nodes with AMD 7643 (96x 2.30GHz) CPUs. 
All nodes are interconnected via InfiniBand (IB). The training process lasted around two months, including downtime due to unexpected factors.

### Software

Tele-FLM-1T utilizes 3D parallel training, combining the prevailing methodologies: data parallelism, tensor parallelism, and pipeline parallelism.
The parallel training setup for Tele-FLM-1T is configured as follows: tensor parallel=32, pipeline parallel=28, and data parallel=1.

### Relate Work
[Tele-FLM (52B)](https://huggingface.co/CofeAI/Tele-FLM)

[FLM-101B](https://huggingface.co/CofeAI/FLM-101B)

## Citation
If you find our work helpful, please consider citing it.
```
@article{tele-flm-1t,
  author       = {Xiang Li and Yiqun Yao and Xin Jiang and Xuezhi Fang and Chao Wang and Xinzhang Liu and Zihan Wang and Yu Zhao and Xin Wang and Yuyao Huang and Shuangyong Song and Yongxiang Li and Zheng Zhang and Bo Zhao and Aixin Sun and Yequan Wang and Zhongjiang He and Zhongyuan Wang and Xuelong Li and Tiejun Huang},
  title        = {52B to 1T: Lessons Learned via Tele-FLM Series},
  journal      = {CoRR},
  volume       = {abs/2407.02783},
  year         = {2024},
  url          = {https://doi.org/10.48550/arXiv.2407.02783},
  doi          = {10.48550/ARXIV.2407.02783},
  eprinttype   = {arXiv},
  eprint       = {2407.02783},
}

@article{tele-flm-2024,
  author       = {Xiang Li and Yiqun Yao and Xin Jiang and Xuezhi Fang and Chao Wang and Xinzhang Liu and Zihan Wang and Yu Zhao and Xin Wang and Yuyao Huang and Shuangyong Song and Yongxiang Li and Zheng Zhang and Bo Zhao and Aixin Sun and Yequan Wang and Zhongjiang He and Zhongyuan Wang and Xuelong Li and Tiejun Huang},
  title        = {Tele-FLM Technical Report},
  journal      = {CoRR},
  volume       = {abs/2404.16645},
  year         = {2024},
  url          = {https://doi.org/10.48550/arXiv.2404.16645},
  doi          = {10.48550/ARXIV.2404.16645},
  eprinttype   = {arXiv},
  eprint       = {2404.16645},
}
```