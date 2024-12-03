---
language:
 - en
 - ru
 - de
 - es
 - fr
 - ja
 - it
 - vi
 - nl
 - pl
 - pt
 - id
 - fa
 - ar
 - el
 - tr
 - cs
 - zh
 - ro
 - sv
 - hu
 - uk
 - bg
 - no
 - hi
 - fi
 - da
 - sk
 - ko
 - hr
 - ca
 - he
 - bn
 - lt
 - ta
 - sr
 - sl
 - et
 - lv
 - ne
 - mr
 - ka
 - ml
 - mk
 - ur
 - sq
 - kk
 - te
 - hy
 - az
 - is
 - gl
 - kn
library_name: nemo
tags:
- text generation
- pytorch
- causal-lm
license: cc-by-4.0

---
# GPT-2B-001

<style>
img {
 display: inline;
}
</style>

|[![Model architecture](https://img.shields.io/badge/Model%20Arch-Transformer%20Decoder-green)](#model-architecture)|[![Model size](https://img.shields.io/badge/Params-2B-green)](#model-architecture)|[![Language](https://img.shields.io/badge/Language-Multilingual-green)](#datasets)


## Model Description

GPT-2B-001 is a transformer-based language model. GPT refers to a class of transformer decoder-only models similar to GPT-2 and 3 while 2B refers to the total trainable parameter count (2 Billion) [1, 2].

This model was trained on 1.1T tokens with [NeMo](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/stable/nlp/nemo_megatron/intro.html).

## Model Architecture improvements

- The model uses the SwiGLU activation function [4]
- Rotary positional embeddings (RoPE) [5]
- Maximum sequence length of 4,096 compared to 2,048 in https://huggingface.co/nvidia/nemo-megatron-gpt-20B.
- No dropout.
- No bias terms in all linear layers.
- Untied embedding and output layers.

## Getting started

Note: You will need NVIDIA Ampere or Hopper GPUs to work with this model.

### Step 1: Install NeMo and dependencies

You will need to install NVIDIA Apex and NeMo. 

```
git clone https://github.com/NVIDIA/apex.git
cd apex
git checkout 03c9d80ed54c0eaa5b581bf42ceca3162f085327
pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" --global-option="--fast_layer_norm" --global-option="--distributed_adam" --global-option="--deprecated_fused_adam" ./
```

```
pip install nemo_toolkit['nlp']==1.17.0
``` 

Alternatively, you can use NeMo Megatron training docker container with all dependencies pre-installed.

### Step 2: Launch eval server 

**Note.** The example below launches a model variant with Tensor Parallelism (TP) of 1 and Pipeline Parallelism (PP) of 1 on 1 GPU.


```
git clone https://github.com/NVIDIA/NeMo.git 
cd NeMo/examples/nlp/language_modeling
git checkout v1.17.0
python megatron_gpt_eval.py gpt_model_file=nemo_2b_bf16_tp1.nemo trainer.precision=bf16 server=True tensor_model_parallel_size=1 trainer.devices=1
```

### Step 3: Send prompts to your model!
```python
import json
import requests

port_num = 5555
headers = {"Content-Type": "application/json"}

def request_data(data):
    resp = requests.put('http://localhost:{}/generate'.format(port_num),
                        data=json.dumps(data),
                        headers=headers)
    sentences = resp.json()['sentences']
    return sentences


data = {
    "sentences": ["It was a warm summer morning when"]*1,
    "tokens_to_generate": 50,
    "temperature": 1.0,
    "add_BOS": False,
    "top_k": 0,
    "top_p": 0.9,
    "greedy": False,
    "all_probs": False,
    "repetition_penalty": 1.2,
    "min_tokens_to_generate": 2,
}

sentences = request_data(data)
print(sentences)
```


## Training Data

The model was trained on 1.1T tokens obtained from publicly available data sources. The dataset comprises 53 languages and code.

## Evaluation results

*Zero-shot performance.* Evaluated using [LM Evaluation Test Suite from AI21](https://github.com/AI21Labs/lm-evaluation)

| ARC-Challenge	| ARC-Easy | RACE-middle |Winogrande | RTE | BoolQA | HellaSwag | PiQA |
| ------------- | -------- | ----------- | ----------| --- | ------ | --------- | ---- |
| 0.3558        | 0.45300  | 0.3997      | 0.5801    | 0.556 | 0.5979 | 0.592 | 0.7437 | 

## Limitations

The model was trained on the data originally crawled from the Internet. This data contains toxic language and societal biases. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts.
We did not perform any bias/toxicity removal or model alignment on this checkpoint.

## References

[1] [Improving Language Understanding by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)

[2] [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/pdf/1909.08053.pdf)

[3] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)

[4] [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202)

[5] [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864)

## Licence

License to use this model is covered by the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). By downloading the public and release version of the model, you accept the terms and conditions of the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license.

