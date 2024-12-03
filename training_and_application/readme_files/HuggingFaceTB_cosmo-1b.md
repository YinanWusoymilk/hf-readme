---
license: apache-2.0
datasets:
- HuggingFaceTB/cosmopedia
language:
- en
inference:
  parameters:
    temperature: 0.6
    top_p: 0.95
    top_k: 50
    repetition_penalty: 1.2
widget:
  - text: 'Photosynthesis is'
    example_title: Textbook
    group: Completion
  - text: '<s> [INST]  How to take care of plants? [/INST] '
    example_title: Wikihow
    group: Completion
  - text: '<s> [INST] Generate a story about a flying cat [/INST] '
    example_title: Story
    group: Completion
---

# Model Summary
This is a 1.8B model trained on [Cosmopedia](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia) synthetic dataset.

# Training dataset
The training corpus consisted of 30B tokens, 25B of which are synthetic from Cosmopedia. Since we didn't explore the synthetic generation of code, we augmented the dataset with 5B tokens of non-synthetic sources like the `code-python-0.60-to-1.00` and `web-0.50-to-1.00` subsets of [AutoMathText](https://huggingface.co/datasets/math-ai/AutoMathText). We also added 1M files from [The Stack](https://huggingface.co/datasets/bigcode/the-stack)'s Jupyter Notebooks, converted to script. They tend to have educational code interleaved with text. 
We also included [ultrachat](https://huggingface.co/datasets/stingning/ultrachat) formatted in the chat format of `LlaMa` models, so we don't have to instruction-tune the model after the pre-training. Additionally, we upsampled twice the data from these seed sources to help with commonsense and reasoning: stories, AutoMathText & KhanAcademy. 

We trained for 6 epochs, resulting in a model trained on 180B tokens with a sequence length of 2k, a global batch size of 1.3M tokens and a learning rate of 3e-4 with a cosine schedule for 140k steps.
We used the tokenizer from [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1/).

# How to use

Although the model wasn't instruction-tuned after the pre-training. However, given that included UltraChat in the pre-training , you can use it in a Chat format using:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda"  # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/cosmo-1b")
model = AutoModelForCausalLM.from_pretrained("HuggingFaceTB/cosmo-1b").to(device)
prompt = "Generate a story involving a dog, an astronaut and a baker"
prompt= tokenizer.apply_chat_template([{"role": "user", "content": prompt}], tokenize=False)
inputs = tokenizer(prompt, return_tensors="pt").to(device)

output = model.generate(**inputs, max_length=300, do_sample=True, temperature=0.6, top_p=0.95, repetition_penalty=1.2)
print(tokenizer.decode(output[0]))
```
Output:
```
<s><s> [INST] Generate a story involving a dog, an astronaut and a baker [/INST] Once upon a time, there was a sweet little terrier named Max who lived in the bustling city of New York. He loved nothing more than chasing after his owner, Dr. Sarah Johnson, as she worked tirelessly on her latest invention - a spaceship that would take humans to distant galaxies!

One day, Dr. Johnson decided it was time for her to leave Earth's atmosphere behind and embark on this exciting adventure with her loyal companion, Max. She knew he had always been fascinated by space travel, so she hoped he would be just as excited about the journey ahead.

As they boarded their rocket ship and blasted off into outer space, Max felt both nervous and thrilled at the same time. His ears perked up every time they passed clouds or saw stars twinkling far out from earth. But as days turned into weeks, Max started feeling homesick. The vast emptiness around him made him feel lonely and isolated.

Meanwhile back on planet Earth, Mr. Baker was busy baking cookies when suddenly, an idea popped into his head. Why not send some treats along with Dr. Johnson's family? It might make them all feel better knowing that someone else was also having fun exploring the universe.
```

You can also use the model in text completion mode i.e without applying the chat template, but it might not follow isntructions.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda"  # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/cosmo-1b")
model = AutoModelForCausalLM.from_pretrained("HuggingFaceTB/cosmo-1b").to(device)
prompt = "Photosynthesis is"

inputs = tokenizer(prompt, return_tensors="pt").to(device)
output = model.generate(**inputs, max_length=300, do_sample=True, temperature=0.6, top_p=0.95, repetition_penalty=1.2)
print(tokenizer.decode(output[0]))
```
Output:
```
<s> Photosynthesis is the process by which green plants, algae and some bacteria convert light energy into chemical energy in order to fuel their metabolic processes. The reaction takes place within specialized cells called chloroplasts. This article focuses on the electron transport chain (ETC), a critical part of photosystem II where most of the solar-driven electrons are passed through before being reduced to water.
```
# Evaluation
Below are the evaluation results of Cosmo-1B. The model is better than TinyLlama 1.1B on ARC-easy, ARC-challenge, OpenBookQA and MMLU, and has comparable performance to Qwen-1.5-1B on ARC-challenge and OpenBookQA.
However, we notice some perfoamnce gaps compared to Phi-1.5 suggesting a better synthetic generation quality which can be related to the LLM used for generation, topic coverage or prompts.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61c141342aac764ce1654e43/GgWzl6k9BO9jGhGd5O45y.png)

# Limitations

This is a small 1.8B model trained on synthetic data, so it might hallucinate, give incomplete or incorrect answers.

# Training

## Model

- **Architecture:** Llama-2 
- **Pretraining steps:** 120k
- **Pretraining tokens:** 180B
- **Precision:** bfloat16

## Hardware

- **GPUs:** 160 H100
- **Training time:** 15hours

The training loss:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61c141342aac764ce1654e43/rJobY7F6tqTAvIox1ZGKR.png)
