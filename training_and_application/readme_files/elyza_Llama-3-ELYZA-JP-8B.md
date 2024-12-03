---
library_name: transformers
license: llama3
language:
- ja
- en
---
## Llama-3-ELYZA-JP-8B

![Llama-3-ELYZA-JP-8B-image](./key_visual.png)

### Model Description

**Llama-3-ELYZA-JP-8B** is a large language model trained by [ELYZA, Inc](https://elyza.ai/). 
Based on [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct), it has been enhanced for Japanese usage through additional pre-training and instruction tuning. (Built with Meta Llama3)

For more details, please refer to [our blog post](https://note.com/elyza/n/n360b6084fdbd).

### Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

DEFAULT_SYSTEM_PROMPT = "あなたは誠実で優秀な日本人のアシスタントです。特に指示が無い場合は、常に日本語で回答してください。"
text = "仕事の熱意を取り戻すためのアイデアを5つ挙げてください。"

model_name = "elyza/Llama-3-ELYZA-JP-8B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto",
)
model.eval()

messages = [
    {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
    {"role": "user", "content": text},
]
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
token_ids = tokenizer.encode(
    prompt, add_special_tokens=False, return_tensors="pt"
)

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        max_new_tokens=1200,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
    )
output = tokenizer.decode(
    output_ids.tolist()[0][token_ids.size(1):], skip_special_tokens=True
)
print(output)
```

### Developers

Listed in alphabetical order.

- [Masato Hirakawa](https://huggingface.co/m-hirakawa)
- [Shintaro Horie](https://huggingface.co/e-mon)
- [Tomoaki Nakamura](https://huggingface.co/tyoyo)
- [Daisuke Oba](https://huggingface.co/daisuk30ba)
- [Sam Passaglia](https://huggingface.co/passaglia)
- [Akira Sasaki](https://huggingface.co/akirasasaki)

### License

[Meta Llama 3 Community License](https://llama.meta.com/llama3/license/)

### How to Cite

```tex
@misc{elyzallama2024,
      title={elyza/Llama-3-ELYZA-JP-8B},
      url={https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B},
      author={Masato Hirakawa and Shintaro Horie and Tomoaki Nakamura and Daisuke Oba and Sam Passaglia and Akira Sasaki},
      year={2024},
}
```

### Citations

```tex
@article{llama3modelcard,
    title={Llama 3 Model Card},
    author={AI@Meta},
    year={2024},
    url = {https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md}
}
```