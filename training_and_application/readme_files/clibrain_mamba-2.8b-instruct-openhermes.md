---
license: wtfpl
datasets:
- teknium/openhermes
pipeline_tag: text-generation
thumbnail: https://huggingface.co/clibrain/mamba-2.8b-instruct-openhermes/resolve/main/mamba_hermes_logo_1.png?download=true
language:
- en
---

# MAMBA (2.8B) 🐍 fine-tuned on OpenHermes

<div style="text-align:center;width:250px;height:250px;">
    <img src="https://huggingface.co/clibrain/mamba-2.8b-instruct-openhermes/resolve/main/mamba_hermes_logo_1.png?download=true" alt="mamba-hermes logo"">
</div>

Model Card is still WIP!


## Base model info

Mamba is a new state space model architecture showing promising performance on information-dense data such as language modeling, where previous subquadratic models fall short of Transformers.
It is based on the line of progress on [structured state space models](https://github.com/state-spaces/s4),
with an efficient hardware-aware design and implementation in the spirit of [FlashAttention](https://github.com/Dao-AILab/flash-attention).

## Dataset info

The OpenHermes dataset is composed of 242,000 entries of primarily GPT-4 generated data, from open datasets across the AI landscape, including:

OpenHermes 13B is the first fine tune of the Hermes dataset that has a fully open source dataset!

OpenHermes was trained on 242,000 entries of primarily GPT-4 generated data, from open datasets across the AI landscape, including:

- GPTeacher - General Instruct, Roleplay v1, Roleplay v2, and Code Instruct Datasets, by Teknium
- WizardLM (v1, evol_instruct 70k), by WizardLM Team/nlpxucan
- Airoboros GPT-4 (v1.0), by JonDurbin
- Camel-AI's domain expert datasets, by the Camel-AI Team
- CodeAlpaca, by Sahil2801
- GPT4-LLM and Unnatural Instructions, by Microsoft
Filtering included removal of OpenAI refusals, disclaimers, and "As an AI" type examples and more
The base dataset mix is identical to the original Nous-Hermes', minus the Nous-Instruct and PDACTL datasets which were private datasets.

## Usage

```sh
pip install torch==2.1.0 transformers==4.35.0 causal-conv1d==1.0.0 mamba-ssm==1.0.1
```

```py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel

CHAT_TEMPLATE_ID = "HuggingFaceH4/zephyr-7b-beta"

device = "cuda:0" if torch.cuda.is_available() else "cpu"
model_name = "clibrain/mamba-2.8b-instruct-openhermes"

eos_token = "<|endoftext|>"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.eos_token = eos_token
tokenizer.pad_token = tokenizer.eos_token
tokenizer.chat_template = AutoTokenizer.from_pretrained(CHAT_TEMPLATE_ID).chat_template

model = MambaLMHeadModel.from_pretrained(
        model_name, device=device, dtype=torch.float16)

messages = []
prompt = "Tell me 5 sites to visit in Spain"
messages.append(dict(role="user", content=prompt))

input_ids = tokenizer.apply_chat_template(
            messages, return_tensors="pt", add_generation_prompt=True
).to(device)

out = model.generate(
    input_ids=input_ids,
    max_length=2000,
    temperature=0.9,
    top_p=0.7,
    eos_token_id=tokenizer.eos_token_id,
)

decoded = tokenizer.batch_decode(out)
assistant_message = (
    decoded[0].split("<|assistant|>\n")[-1].replace(eos_token, "")
)

print(assistant_message)
```


## Gradio Demo

```sh
git clone https://github.com/mrm8488/mamba-chat.git
cd mamba-chat

pip install -r requirements.txt
pip install -q gradio==4.8.0

python app.py \
--model clibrain/mamba-2.8b-instruct-openhermes \
--share
```
## Evaluations

Coming soon!


## Acknowledgments

Thanks to [mamba-chat](https://github.com/havenhq/mamba-chat/tree/main) for heavily inspiring our work