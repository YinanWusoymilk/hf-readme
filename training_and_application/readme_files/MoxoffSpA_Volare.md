---
license: mit
language:
- it
- en
library_name: transformers
tags:
- sft
- it
- gemma
- chatml
---

# Model Information

Volare is an updated version of [Gemma7B](https://huggingface.co/google/gemma-7b), specifically fine-tuned with SFT and LoRA adjustments.

- It's trained on publicly available datasets, like [SQUAD-it](https://huggingface.co/datasets/squad_it), and datasets we've created in-house.
- it's designed to understand and maintain context, making it ideal for Retrieval Augmented Generation (RAG) tasks and applications requiring contextual awareness.

# Evaluation

We evaluated the model using the same test sets as used for the [Open Ita LLM Leaderboard](https://huggingface.co/spaces/FinancialSupport/open_ita_llm_leaderboard) 

| hellaswag_it acc_norm | arc_it acc_norm | m_mmlu_it 5-shot acc | Average | F1 |
|:----------------------| :--------------- | :-------------------- | :------- | :-- |
| 0.6474 | 0.4671 | 0.5521 | 0.555 | 69.82 |


## Usage

Be sure to install these dependencies before running the program

```python
!pip install transformers torch sentencepiece
```

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cpu" # if you want to use the gpu make sure to have cuda toolkit installed and change this to "cuda"

model = AutoModelForCausalLM.from_pretrained("MoxoffSpA/Volare")
tokenizer = AutoTokenizer.from_pretrained("MoxoffSpA/Volare")

question = """Quanto è alta la torre di Pisa?"""
context = """
La Torre di Pisa è un campanile del XII secolo, famoso per la sua inclinazione. Alta circa 56 metri.
"""

prompt = f"Domanda: {question}, contesto: {context}"

messages = [
    {"role": "user", "content": prompt}
]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(
    model_inputs, # The input to the model
    max_new_tokens=128, # Limiting the maximum number of new tokens generated
    do_sample=True, # Enabling sampling to introduce randomness in the generation
    temperature=0.1, # Setting temperature to control the randomness, lower values make it more deterministic
    top_p=0.95, # Using nucleus sampling with top-p filtering for more coherent generation       
    eos_token_id=tokenizer.eos_token_id # Specifying the token that indicates the end of a sequence
)

decoded_output = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
trimmed_output = decoded_output.strip()
print(trimmed_output)
```

## Bias, Risks and Limitations

Volare has not been aligned to human preferences for safety within the RLHF phase or deployed with in-the-loop filtering of 
responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). It is also unknown what the size and composition 
of the corpus was used to train the base model, however it is likely to have included a mix of Web data and technical sources 
like books and code.

## Links to resources

- SQUAD-it dataset: https://huggingface.co/datasets/squad_it
- Gemma-7b model: https://huggingface.co/google/gemma-7b
- Open Ita LLM Leaderbord: https://huggingface.co/spaces/FinancialSupport/open_ita_llm_leaderboard

## Quantized versions

We have published as well the 4 bit and 8 bit versions of this model:
https://huggingface.co/MoxoffSpA/VolareQuantized

## The Moxoff Team

Jacopo Abate, Marco D'Ambra, Luigi Simeone, Gianpaolo Francesco Trotta