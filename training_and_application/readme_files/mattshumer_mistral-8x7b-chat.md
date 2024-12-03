A very capable chat model built on top of the new Mistral MoE model, trained on the SlimOrca dataset for 1 epoch, using QLoRA.

Inference:
```py
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("mattshumer/mistral-8x7b-chat", low_cpu_mem_usage=True, device_map="auto", trust_remote_code=True)
tok = AutoTokenizer.from_pretrained("mattshumer/mistral-8x7b-chat")
x = tok.encode(PROMPT_GOES_HERE, return_tensors="pt").cuda()
x = model.generate(x, max_new_tokens=512).cpu()
print(tok.batch_decode(x))
```

Prompt Template:
```
<|im_start|>system
You are an AI assistant.<|im_end|>
<|im_start|>user
Hi, how are you?<|im_end|>
<|im_start|>assistant
I'm doing well, thanks for asking!<|im_end|>
<|im_start|>user
Write me a poem about AI.<|im_end|>
```

Trained w/ Axolotl on 6x H100s for nine hours.