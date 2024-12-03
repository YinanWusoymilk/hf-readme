---
license: other
license_name: deepseek
license_link: https://github.com/deepseek-ai/DeepSeek-Math/blob/main/LICENSE-MODEL
---


<p align="center">
<img width="500px" alt="DeepSeek Chat" src="https://github.com/deepseek-ai/DeepSeek-LLM/blob/main/images/logo.png?raw=true">
</p>
<p align="center"><a href="https://www.deepseek.com/">[🏠Homepage]</a>  |  <a href="https://chat.deepseek.com/">[🤖 Chat with DeepSeek LLM]</a>  |  <a href="https://discord.gg/Tc7c45Zzu5">[Discord]</a>  |  <a href="https://github.com/deepseek-ai/DeepSeek-LLM/blob/main/images/qr.jpeg">[Wechat(微信)]</a> </p>

<p align="center">
  <a href="https://arxiv.org/pdf/2402.03300.pdf"><b>Paper Link</b>👁️</a>
</p>

<hr>





### 1. Introduction to DeepSeekMath
See the [Introduction](https://github.com/deepseek-ai/DeepSeek-Math) for more details.

### 2. How to Use
Here give some examples of how to use our model.

**Text Completion**

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig

model_name = "deepseek-ai/deepseek-math-7b-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="auto")
model.generation_config = GenerationConfig.from_pretrained(model_name)
model.generation_config.pad_token_id = model.generation_config.eos_token_id

text = "The integral of x^2 from 0 to 2 is"
inputs = tokenizer(text, return_tensors="pt")
outputs = model.generate(**inputs.to(model.device), max_new_tokens=100)

result = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(result)
```

### 3. License
This code repository is licensed under the MIT License. The use of DeepSeekMath models is subject to the Model License. DeepSeekMath supports commercial use.

See the [LICENSE-MODEL](https://github.com/deepseek-ai/DeepSeek-Math/blob/main/LICENSE-MODEL) for more details.

### 4. Contact

If you have any questions, please raise an issue or contact us at [service@deepseek.com](mailto:service@deepseek.com).
