---
license: other
license_name: nvidia-community-model-license
license_link: >-
  https://huggingface.co/nvidia/Nemotron-Mini-4B-Instruct/blob/main/nvidia-community-model-license-aug2024.pdf
language:
- en
base_model: nvidia/Minitron-4B-Base
library_name: nemo
---
# Nemotron-Mini-4B-Instruct

## Model Overview

Nemotron-Mini-4B-Instruct is a model for generating responses for roleplaying, retrieval augmented generation, and function calling.  It is a small language model (SLM) optimized through distillation, pruning and quantization for speed and on-device deployment. It is a fine-tuned version of [nvidia/Minitron-4B-Base](https://huggingface.co/nvidia/Minitron-4B-Base), which was pruned and distilled from [Nemotron-4 15B](https://arxiv.org/abs/2402.16819) using [our LLM compression technique](https://arxiv.org/abs/2407.14679). This instruct model is optimized for roleplay, RAG QA, and function calling in English. It supports a context length of 4,096 tokens. This model is ready for commercial use.

Try this model on [build.nvidia.com](https://build.nvidia.com/nvidia/nemotron-mini-4b-instruct).

For more details about how this model is used for [NVIDIA ACE](https://developer.nvidia.com/ace), please refer to [this blog post](https://developer.nvidia.com/blog/deploy-the-first-on-device-small-language-model-for-improved-game-character-roleplay/) and [this demo video](https://www.youtube.com/watch?v=d5z7oIXhVqg), which showcases how the model can be integrated into a video game. You can download the model checkpoint for NVIDIA AI Inference Manager (AIM) SDK from [here](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ucs-ms/resources/nemotron-mini-4b-instruct).

**Model Developer:** NVIDIA 

**Model Dates:** Nemotron-Mini-4B-Instruct was trained between February 2024 and Aug 2024.

## License

[NVIDIA Community Model License](https://huggingface.co/nvidia/Nemotron-Mini-4B-Instruct/blob/main/nvidia-community-model-license-aug2024.pdf)

## Model Architecture

Nemotron-Mini-4B-Instruct uses a model embedding size of 3072, 32 attention heads, and an MLP intermediate dimension of 9216. It also uses Grouped-Query Attention (GQA) and Rotary Position Embeddings (RoPE). 

**Architecture Type:** Transformer Decoder (auto-regressive language model) 

**Network Architecture:** Nemotron-4 


## Prompt Format:

We recommend using the following prompt template, which was used to fine-tune the model. The model may not perform optimally without it.

**Single Turn**

```
<extra_id_0>System
{system prompt}

<extra_id_1>User
{prompt}
<extra_id_1>Assistant\n
```

**Tool use**

```
<extra_id_0>System
{system prompt}

<tool> ... </tool>
<context> ... </context>

<extra_id_1>User
{prompt}
<extra_id_1>Assistant
<toolcall> ... </toolcall>
<extra_id_1>Tool
{tool response}
<extra_id_1>Assistant\n
```


## Usage

```
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer  = AutoTokenizer.from_pretrained("nvidia/Nemotron-Mini-4B-Instruct")
model = AutoModelForCausalLM.from_pretrained("nvidia/Nemotron-Mini-4B-Instruct")

# Use the prompt template
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds in the style of a pirate",
    },
    {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
 ]
tokenized_chat = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")

outputs = model.generate(tokenized_chat, max_new_tokens=128) 
print(tokenizer.decode(outputs[0]))
```

You can also use `pipeline` but you need to create a tokenizer object and assign it to the pipeline manually.

```
from transformers import AutoTokenizer
from transformers import pipeline

tokenizer  = AutoTokenizer.from_pretrained("nvidia/Nemotron-Mini-4B-Instruct")

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="nvidia/Nemotron-Mini-4B-Instruct")
pipe.tokenizer = tokenizer  # You need to assign tokenizer manually
pipe(messages)
```

## AI Safety Efforts

The Nemotron-Mini-4B-Instruct model underwent AI safety evaluation including adversarial testing via three distinct methods: 
- [Garak](https://github.com/leondz/garak), is an automated LLM vulnerability scanner that probes for common weaknesses, including prompt injection and data leakage. 
- [AEGIS](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0), is a content safety evaluation dataset and LLM based content safety classifier model, that adheres to a broad taxonomy of 13 categories of critical risks in human-LLM interactions.
- Human Content Red Teaming leveraging human interaction and evaluation of the models' responses.


## Limitations

The model was trained on data that contains toxic language and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. This issue could be exacerbated without the use of the recommended prompt template. This issue could be exacerbated without the use of the recommended prompt template.


## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the [Model Card++](https://build.nvidia.com/nvidia/nemotron-mini-4b-instruct/modelcard). Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).