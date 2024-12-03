---
license: apache-2.0
---

We introduced a new model designed for the Code generation task. Its test accuracy on the HumanEval base dataset surpasses that of GPT-4 Turbo (April 2024). (90.9% vs 90.2%).

Additionally, compared to previous open-source models, AutoCoder offers a new feature: it can **automatically install the required packages** and attempt to run the code until it deems there are no issues, **whenever the user wishes to execute the code**.

Its base model is deepseeker-coder.

See details on the [AutoCoder GitHub](https://github.com/bin123apple/AutoCoder).

Simple test script:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset

model_path = ""
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, 
                                             device_map="auto")

HumanEval = load_dataset("evalplus/humanevalplus")

Input = "" # input your question here
 
messages=[
    { 'role': 'user', 'content': Input}
]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, 
                                        return_tensors="pt").to(model.device)

outputs = model.generate(inputs, 
                        max_new_tokens=1024, 
                        do_sample=False, 
                        temperature=0.0,
                        top_p=1.0, 
                        num_return_sequences=1, 
                        eos_token_id=tokenizer.eos_token_id)

answer = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)
```

Paper: https://arxiv.org/abs/2405.14906