---
license: other
tags:
- merge
- mergekit
- lazymergekit
base_model:
- meta-llama/Meta-Llama-3-70B-Instruct
- meta-llama/Meta-Llama-3-70B-Instruct
- meta-llama/Meta-Llama-3-70B-Instruct
- meta-llama/Meta-Llama-3-70B-Instruct
- meta-llama/Meta-Llama-3-70B-Instruct
- meta-llama/Meta-Llama-3-70B-Instruct
- meta-llama/Meta-Llama-3-70B-Instruct
---

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/C-Xw_m97bhXaTA1TEpHB7.jpeg)

# Meta-Llama-3-120B-Instruct

Meta-Llama-3-120B-Instruct is a [meta-llama/Meta-Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) self-merge made with [MergeKit](https://github.com/arcee-ai/mergekit/tree/main).

It was inspired by large merges like:

- [alpindale/goliath-120b](https://huggingface.co/alpindale/goliath-120b)
- [nsfwthrowitaway69/Venus-120b-v1.0](https://huggingface.co/nsfwthrowitaway69/Venus-120b-v1.0)
- [cognitivecomputations/MegaDolphin-120b](https://huggingface.co/cognitivecomputations/MegaDolphin-120b)
- [wolfram/miquliz-120b-v2.0](https://huggingface.co/wolfram/miquliz-120b-v2.0).

Special thanks to [Eric Hartford](https://huggingface.co/ehartford) for both inspiring and evaluating this model and to [Charles Goddard](https://huggingface.co/chargoddard) for creating MergeKit.

## 🔍 Applications

I recommend using this model for creative writing. It uses the Llama 3 chat template with a default context window of 8K (can be extended with rope theta).

Check the examples in the evaluation section to get an idea of its performance. The model is generally quite unhinged but has a good writing style. It sometimes outputs typos and is a big fan of uppercase.

## ⚡ Quantized models

Thanks to [Bartowski](https://huggingface.co/ehartford), [elinas](https://huggingface.co/elinas), the [mlx-community](https://huggingface.co/mlx-community) and others for providing these models.

* **GGUF**: https://huggingface.co/lmstudio-community/Meta-Llama-3-120B-Instruct-GGUF
* **EXL2**: https://huggingface.co/elinas/Meta-Llama-3-120B-Instruct-4.0bpw-exl2
* **mlx**: https://huggingface.co/mlx-community/Meta-Llama-3-120B-Instruct-4bit

## 🏆 Evaluation

This model is great for creative writing but struggles in other tasks. I'd say use it with caution and don't expect it to outperform GPT-4 outside of some very specific use cases.

* **X thread by Eric Hartford (creative writing)**: https://twitter.com/erhartford/status/1787050962114207886
* **X thread by Daniel Kaiser (creative writing)**: https://twitter.com/spectate_or/status/1787257261309518101
* **X thread by Simon (reasoning)**: https://twitter.com/NewDigitalEdu/status/1787403266894020893
* **r/LocalLLaMa**: https://www.reddit.com/r/LocalLLaMA/comments/1cl525q/goliath_lovers_where_is_the_feedback_about/

### Creative Writing

Thanks to [Sam Paech](https://huggingface.co/sam-paech) for evaluating this model and sending me his outputs! 

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/-LJ7ivCRIPR1ur-LJHk3m.png)

## 🧩 Configuration

```yaml
slices:
- sources:
  - layer_range: [0, 20]
    model: meta-llama/Meta-Llama-3-70B-Instruct
- sources:
  - layer_range: [10, 30]
    model: meta-llama/Meta-Llama-3-70B-Instruct
- sources:
  - layer_range: [20, 40]
    model: meta-llama/Meta-Llama-3-70B-Instruct
- sources:
  - layer_range: [30, 50]
    model: meta-llama/Meta-Llama-3-70B-Instruct
- sources:
  - layer_range: [40, 60]
    model: meta-llama/Meta-Llama-3-70B-Instruct
- sources:
  - layer_range: [50, 70]
    model: meta-llama/Meta-Llama-3-70B-Instruct
- sources:
  - layer_range: [60, 80]
    model: meta-llama/Meta-Llama-3-70B-Instruct
merge_method: passthrough
dtype: float16
```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "mlabonne/Meta-Llama-3-120B-Instruct"
messages = [{"role": "user", "content": "What is a large language model?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```