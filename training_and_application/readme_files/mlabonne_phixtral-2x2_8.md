---
inference: false
license: mit
license_link: https://huggingface.co/microsoft/phi-2/resolve/main/LICENSE
language:
- en
pipeline_tag: text-generation
tags:
- moe
- nlp
- code
- cognitivecomputations/dolphin-2_6-phi-2
- lxuechen/phi-2-dpo
---

![](https://i.imgur.com/UOb2fvh.jpg)

# phixtral-2x2_8

phixtral-2x2_8 is the first Mixure of Experts (MoE) made with two [microsoft/phi-2](https://huggingface.co/microsoft/phi-2) models, inspired by the [mistralai/Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) architecture. It performs better than each individual expert.

You can try it out using this [Space](https://huggingface.co/spaces/mlabonne/phixtral-chat).

## 🏆 Evaluation

The evaluation was performed using [LLM AutoEval](https://github.com/mlabonne/llm-autoeval) on Nous suite.

|                             Model                              |AGIEval|GPT4All|TruthfulQA|Bigbench|Average|
|----------------------------------------------------------------|------:|------:|---------:|-------:|------:|
|[**phixtral-2x2_8**](https://huggingface.co/mlabonne/phixtral-2x2_8)|   **34.1**|  **70.44**|     **48.78**|   **37.82**|  **47.78**|
|[dolphin-2_6-phi-2](https://huggingface.co/cognitivecomputations/dolphin-2_6-phi-2)|  33.12|  69.85|     47.39|    37.2|  46.89|
|[phi-2-dpo](https://huggingface.co/lxuechen/phi-2-dpo)|  30.39|  71.68|     50.75|    34.9|  46.93|
|[phi-2](https://huggingface.co/microsoft/phi-2)|  27.98|   70.8|     44.43|   35.21|  44.61|

Check [YALL - Yet Another LLM Leaderboard](https://huggingface.co/spaces/mlabonne/Yet_Another_LLM_Leaderboard) to compare it with other models.

## 🧩 Configuration

The model has been made with a custom version of the [mergekit](https://github.com/cg123/mergekit) library (mixtral branch) and the following configuration:

```yaml
base_model: cognitivecomputations/dolphin-2_6-phi-2
gate_mode: cheap_embed
experts:
  - source_model: cognitivecomputations/dolphin-2_6-phi-2
    positive_prompts: [""]
  - source_model: lxuechen/phi-2-dpo
    positive_prompts: [""]
```

## 💻 Usage

Here's a [Colab notebook](https://colab.research.google.com/drive/1k6C_oJfEKUq0mtuWKisvoeMHxTcIxWRa?usp=sharing) to run Phixtral in 4-bit precision on a free T4 GPU.

```python
!pip install -q --upgrade transformers einops accelerate bitsandbytes

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "phixtral-2x2_8"
instruction = '''
    def print_prime(n):
        """
        Print all primes between 1 and n
        """
'''

torch.set_default_device("cuda")

# Load the model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    f"mlabonne/{model_name}", 
    torch_dtype="auto", 
    load_in_4bit=True, 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(
    f"mlabonne/{model_name}", 
    trust_remote_code=True
)

# Tokenize the input string
inputs = tokenizer(
    instruction, 
    return_tensors="pt", 
    return_attention_mask=False
)

# Generate text using the model
outputs = model.generate(**inputs, max_length=200)

# Decode and print the output
text = tokenizer.batch_decode(outputs)[0]
print(text)
```

Inspired by [mistralai/Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1), you can specify the `num_experts_per_tok` and `num_local_experts` in the [`config.json`](https://huggingface.co/mlabonne/phixtral-2x2_8/blob/main/config.json#L26-L27) file (2 for both by default). This configuration is automatically loaded in `configuration.py`.

[vince62s](https://huggingface.co/vince62s) implemented the MoE inference code in the `modeling_phi.py` file. In particular, see the [MoE class](https://huggingface.co/mlabonne/phixtral-2x2_8/blob/main/modeling_phi.py#L293-L317).

## 🤝 Acknowledgments

A special thanks to [vince62s](https://huggingface.co/vince62s) for the inference code and the dynamic configuration of the number of experts. He was very patient and helped me to debug everything.

Thanks to [Charles Goddard](https://github.com/cg123) for the [mergekit](https://github.com/cg123/mergekit) library and the implementation of the [MoE for clowns](https://goddard.blog/posts/clown-moe/).

Thanks to [ehartford](https://huggingface.co/ehartford) and [lxuechen](https://huggingface.co/lxuechen) for their fine-tuned phi-2 models.