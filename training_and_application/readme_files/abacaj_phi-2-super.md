---
license: mit
license_link: https://huggingface.co/microsoft/phi-2/resolve/main/LICENSE
language:
- en
widget:
- text: Hello who are you?
  example_title: Identity
- text: What can you do?
  example_title: Capabilities
- text: Create a fastapi endpoint to retrieve the weather given a zip code.
  example_title: Coding
tags:
- convAI
- conversational
pipeline_tag: text-generation
model-index:
- name: phi-2-super
  results:
  # IFEval
  - task: 
      type: text-generation
      name: Text Generation
    dataset:
      name: Instruction Following Eval
      type: wis-k/instruction-following-eval
    metrics:
       - type: acc
         name: prompt_level_loose_acc
         value: 0.2717
    source:
      name: LightEval
      url: https://github.com/huggingface/lighteval
---
# Phi-2-super (SFT + cDPO)

Base Model: [microsoft/phi-2](https://huggingface.co/microsoft/phi-2)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/62ceeb27e7f6014c0e9d9268/5-LQCMrXi8FN_ewcWL47v.png)

# How to run inference:

```python
import transformers
import torch

if __name__ == "__main__":
  model_name = "abacaj/phi-2-super"
  tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
  
  model = (
      transformers.AutoModelForCausalLM.from_pretrained(
          model_name,
      )
      .to("cuda:0")
      .eval()
  )
  
  messages = [
      {"role": "user", "content": "Hello, who are you?"}
  ]
  inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
  input_ids_cutoff = inputs.size(dim=1)
  
  with torch.no_grad():
      generated_ids = model.generate(
          input_ids=inputs,
          use_cache=True,
          max_new_tokens=512,
          temperature=0.2,
          top_p=0.95,
          do_sample=True,
          eos_token_id=tokenizer.eos_token_id,
          pad_token_id=tokenizer.pad_token_id,
      )
  
  completion = tokenizer.decode(
      generated_ids[0][input_ids_cutoff:],
      skip_special_tokens=True,
  )
  
  print(completion)
```

# Chat template

The model uses the same chat template as found in Mistral instruct models:

```python
text = "<|endoftext|>[INST] What is your favourite condiment? [/INST]"
"Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!<|endoftext|> "
"[INST] Do you have mayonnaise recipes? [/INST]"
```

You don't need to do it manually if you use the HF transformers tokenizer:

```python
  messages = [
      {"role": "user", "content": "Hello, who are you?"},
      {"role": "assistant": "content": "I am ..."}
  ]
  inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
```

# MT-bench / heval

![image/png](https://cdn-uploads.huggingface.co/production/uploads/62ceeb27e7f6014c0e9d9268/lnFu3x1ufdpQVysIrX4-G.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/62ceeb27e7f6014c0e9d9268/mJfBpH8dIW7Ii2KAGI_A7.png)