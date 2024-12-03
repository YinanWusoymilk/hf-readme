---
tags:
- generated_from_trainer
- code
- coding
model-index:
- name: FalCoder
  results: []
license: apache-2.0
language:
- code
thumbnail: https://huggingface.co/mrm8488/falcoder-7b/resolve/main/falcoder.png
datasets:
- HuggingFaceH4/CodeAlpaca_20K
pipeline_tag: text-generation
---

<div style="text-align:center;width:250px;height:250px;">
    <img src="https://huggingface.co/mrm8488/falcoder-7b/resolve/main/falcoder.png" alt="falcoder logo"">
</div>

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# FalCoder 🦅👩‍💻
**Falcon-7b** fine-tuned on the **CodeAlpaca 20k instructions dataset** by using the method **QLoRA** with [PEFT](https://github.com/huggingface/peft) library.

## Model description 🧠

[Falcon 7B](https://huggingface.co/tiiuae/falcon-7b)


## Training and evaluation data 📚

[CodeAlpaca_20K](https://huggingface.co/datasets/HuggingFaceH4/CodeAlpaca_20K): contains 20K instruction-following data used for fine-tuning the Code Alpaca model.


### Training hyperparameters ⚙

TBA

### Training results 🗒️

| Step | Training Loss | Validation Loss |
|------|---------------|-----------------|
| 100  | 0.798500      | 0.767996        |
| 200  | 0.725900      | 0.749880        |
| 300  | 0.669100      | 0.748029        |
| 400  | 0.687300      | 0.742342        |
| 500  | 0.579900      | 0.736735        |



### Example of usage 👩‍💻
```py
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoTokenizer

model_id = "mrm8488/falcoder-7b"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id).to("cuda")

def generate(
        instruction,
        max_new_tokens=128,
        temperature=0.1,
        top_p=0.75,
        top_k=40,
        num_beams=4,
        **kwargs
):
    prompt = instruction + "\n### Solution:\n"
    print(prompt)
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"].to("cuda")
    attention_mask = inputs["attention_mask"].to("cuda")
    generation_config = GenerationConfig(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        num_beams=num_beams,
        **kwargs,
    )
    with torch.no_grad():
        generation_output = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            generation_config=generation_config,
            return_dict_in_generate=True,
            output_scores=True,
            max_new_tokens=max_new_tokens,
            early_stopping=True
        )
    s = generation_output.sequences[0]
    output = tokenizer.decode(s)
    return output.split("### Solution:")[1].lstrip("\n")

instruction = "Design a class for representing a person in Python."
print(generate(instruction))
```

### Citation
```
@misc {manuel_romero_2023,
	author       = { {Manuel Romero} },
	title        = { falcoder-7b (Revision e061237) },
	year         = 2023,
	url          = { https://huggingface.co/mrm8488/falcoder-7b },
	doi          = { 10.57967/hf/0789 },
	publisher    = { Hugging Face }
}
```