---
license: apache-2.0
language:
- zh
- en
pipeline_tag: text-generation
---

<h4 align="center">
    <p>
        <b>English</b> |
        <a href="https://huggingface.co/CofeAI/FLM-101B/blob/main/README_zh.md">简体中文</a> |
    <p>
</h4>


# FLM-101B

FLM-101B is an open-source decoder-only LLM with 101 billion parameters. During the training process, model growth technique was employed. The model rapidly acquires knowledge on a small-scale model(16B) in the early stages of training and gradually scales up to 101B, resulting in a cost-effective 100B-scale LLM training(costing approximately $100,000).
FLM-101B supports both Chinese and English languages. It has a context window length of 2048 in training. Thanks to the use of [xPos](https://arxiv.org/pdf/2212.10554.pdf) rotary position embedding, it allows for efficient expansion of the window size during inference.

To advance the development of 100B-scale Large Language Models (LLMs), FLM-101B has now been fully open-sourced.


## Why use FLM-101B

- It's an open-source 100B scaled Chinese-English bilingual model.
- It's the largest known language model trained with xPos.
- It's the largest known language model that successfully implements μp transfer and loss prediction.
- It's the largest known language model that successfully implements progressive learning with model growth.

## Quick Started with FLM-101B

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("CofeAI/FLM-101B", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("CofeAI/FLM-101B", torch_dtype=torch.bfloat16, low_cpu_mem_usage=True, device_map="auto", trust_remote_code=True)
inputs = tokenizer('A house without books is like a body without a soul;', return_tensors='pt').to(model.device)
generated = model.generate(**inputs, max_new_tokens=64, repetition_penalty=1.1)
print(tokenizer.decode(generated.cpu()[0], skip_special_tokens=True))
```

## Model Details

### Model Description

- **Model type:** Decoder-only language model
- **Language(s) (NLP):** zh, en
- **License:** apache-2.0


<!-- Provide a longer summary of what this model is. -->

### Model size

| Hyperparameter | Value |
|----------------|-------|
| n_parameters   | 101B  |
| n_layers       | 80    |
| n_heads        | 80    |
| d_model        | 10240 |
| vocab size     | 100256|
| sequence length| 2048  |


### Model Architecture and Objective

- **[Extrapolatable Position Embedding (xPos)](https://arxiv.org/pdf/2212.10554.pdf)**
- **[Flash Attention (In Training)](https://arxiv.org/pdf/2205.14135.pdf)**
- **[Model Growth](https://arxiv.org/pdf/2305.02869.pdf)**
- **[Loss Prediction](https://arxiv.org/abs/2304.06875)**



### Training Details


#### Training Hyper Parameter
| **Hyperparameter** | **16b**           |**51b**           |**101b**           |
|--------------------|-------------------|------------------|-------------------|
| Optimizer          |                   | AdamW            |                   |
| Precision          |                   | bfloat16         |                   |
| Weight decay       |                   | 0.1              |                   |
| Gradient clipping  |                   | 1.0              |                   |
| Learning rate      | 4e-4              | 3.4e-4           | 2e-4              |
| Batch size(M tokens)|4.72              | 4.72             | 4.31              |
| Warmup(M samples)  | 4.61              | 0.23             | 0.23              |
| Time(day)          | 9.63              | 5.37             | 6.54              |
| Tokens(B)          | 245.37            | 39.64            | 26.54             |


#### Parallel Strategies

| **Params(billion)** | **TP Size**  | **PP Size**  | **DP Size**  | **Number of GPUs**  | **Batch Size**  | **TFLOP/s per GPU**  | **GPU Utilization**  |
|---------------------|--------------|--------------|--------------|---------------------|-----------------|----------------------|----------------------|
| 16                  | 2            | 1            | 96           | 192                 | 2304            | 162                  | 51.90%               | 
| 51                  | 4            | 2            | 24           | 192                 | 2304            | 160                  | 51.30%               | 
| 101                 | 4            | 4            | 12           | 192                 | 2160            | 165                  | 52.88%               | 

#### Hardware

FLM-101B is trained on a cluster of 24 DGX-A800 GPU (8×80G) servers for less than 26 days. Based on the growth strategy, we sequentially completed the model training for sizes 16B, 51B, and 101B on this cluster.

#### Software

FLM-101B was trained with a codebase adapted from Megatron-LM, and will be open-sourced soon.
It uses a 3D(DP+TP+PP) parallelism approach and distributed optimizer.


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
Although we've made extensive efforts to thoroughly clean and filter the training corpus for the model, due to the open nature of the dataset, the model may still have picked up on some unsafe examples. Consequently, the model may still generate unexpected content, including but not limited to discrimination, bias, or offensive language. We would like to strongly advise users not to spread any unsafe content generated by the model. The project developers cannot be held responsible for any repercussions stemming from the dissemination of harmful information.

At the current stage of training, FLM-101B has a relatively low token count, leaving significant room for improvement in knowledge, especially in specialized domains. Additionally, the model's inference process is not yet optimized, leading to high resource usage and limited speed. We will soon introduce support for Flash Attention in inference.
If you have suggestions for improvement in these areas or any other aspects, please feel free to open an issue on GitHub, and we will respond promptly. Thank you!


## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

```
@article{flm-101b,
  author       = {Xiang Li and Yiqun Yao and Xin Jiang and Xuezhi Fang and Xuying Meng and
                  Siqi Fan and Peng Han and Jing Li and Li Du and Bowen Qin and Zheng Zhang and
                  Aixin Sun and Yequan Wang},
  title        = {FLM-101B: An Open LLM and How to Train It with \$100K Budget},
  year         = {2023}
}
```


## Contact

tshwangyequan at gmail.com