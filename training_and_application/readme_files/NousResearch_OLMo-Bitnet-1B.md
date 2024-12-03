---
license: apache-2.0
datasets:
- allenai/dolma
---
# OLMo-Bitnet-1B

OLMo-Bitnet-1B is a 1B parameter model trained using the method described in [The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits](https://arxiv.org/abs/2402.17764).

It was trained on the first 60B tokens of the [Dolma](https://huggingface.co/datasets/allenai/dolma) dataset, so it is merely a research proof-of-concept to test out the methodolgy.

A separate training run was run with the exact same hyperparameters, but using standard fp16 weights.
The comparison can be found in [this wandb report](https://api.wandb.ai/links/emozilla/evltqiv7).


![image/png](https://cdn-uploads.huggingface.co/production/uploads/6317aade83d8d2fd903192d9/NAw-hyWJl5ihVsAPqz3Xe.png)

Sample inference code

```sh
pip install ai2-olmo
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, TextStreamer

tokenizer = AutoTokenizer.from_pretrained("NousResearch/OLMo-Bitnet-1B")
model = AutoModelForCausalLM.from_pretrained("NousResearch/OLMo-Bitnet-1B",
    torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")

streamer = TextStreamer(tokenizer)
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, pad_token_id=tokenizer.eos_token_id,
    temperature=0.8, repetition_penalty=1.1, do_sample=True,streamer=streamer)
pipe("The capitol of Paris is",  max_new_tokens=256)
```

Training was performed using [OLMo](https://github.com/allenai/OLMo).