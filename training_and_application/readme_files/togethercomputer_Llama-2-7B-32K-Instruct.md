---
license: llama2
language:
- en
library_name: transformers
datasets:
- togethercomputer/llama-instruct
---

# Llama-2-7B-32K-Instruct

## Model Description

Llama-2-7B-32K-Instruct is an open-source, long-context chat model finetuned from [Llama-2-7B-32K](https://huggingface.co/togethercomputer/Llama-2-7B-32K), over high-quality instruction and chat data.
We built Llama-2-7B-32K-Instruct with less than 200 lines of Python script using [Together API](https://together.ai/blog/api-announcement), and we also make the [recipe fully available](https://github.com/togethercomputer/Llama-2-7B-32K-Instruct).
We hope that this can enable everyone to finetune their own version of [Llama-2-7B-32K](https://huggingface.co/togethercomputer/Llama-2-7B-32K) — play with [Together API](https://together.ai/blog/api-announcement) and give us feedback! 

## Data Collection Details

Llama-2-7B-32K-Instruct is fine-tuned over a combination of two parts:
1. **19K single- and multi-round conversations generated by human instructions and [Llama-2-70B-Chat](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) outputs**.
   We collected the dataset following the distillation paradigm that is used by Alpaca, Vicuna, WizardLM, Orca — producing instructions by querying a powerful LLM (in this case, [Llama-2-70B-Chat](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)).
   The complete dataset is also released [here](https://huggingface.co/datasets/togethercomputer/llama-instruct).
   We also share the complete recipe for the data collection process [here](https://github.com/togethercomputer/Llama-2-7B-32K-Instruct).
   
2. **Long-context Summarization and Long-context QA**.
   We follow the recipe of [Llama-2-7B-32K](https://together.ai/blog/Llama-2-7B-32K), and train our model with the [BookSum dataset](https://huggingface.co/datasets/togethercomputer/Long-Data-Collections) and [Multi-document Question Answering](https://arxiv.org/abs/2307.03172).

The final data mixture used for model finetuning is: 19K instruction (50%) + BookSum (25%) + MQA (25%).

## Model Usage

We encourage you to try out this model using the [Together API](https://together.ai/blog/api-announcement). The updated inference stack allows for efficient inference.

To run the model locally, we strongly recommend to install Flash Attention V2, which is necessary to obtain the best performance:
```
# Please update the path of `CUDA_HOME`
export CUDA_HOME=/usr/local/cuda-11.8
pip install transformers==4.31.0
pip install sentencepiece
pip install ninja
pip install flash-attn --no-build-isolation
pip install git+https://github.com/HazyResearch/flash-attention.git#subdirectory=csrc/rotary
```
You can load the model directly from the Hugging Face model hub using
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("togethercomputer/Llama-2-7B-32K-Instruct")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/Llama-2-7B-32K-Instruct",
    trust_remote_code=True, torch_dtype=torch.float16)
input_ids = tokenizer.encode("[INST]\nWrite a poem about cats\n[/INST]\n\n", return_tensors="pt")
output = model.generate(input_ids, max_length=128,
    temperature=0.7, repetition_penalty=1.1, top_p=0.7, top_k=50)
output_text = tokenizer.decode(output[0], skip_special_tokens=True)
```

The model is also hosted on [Together Playground](https://api.together.xyz/playground). You can simply play with the model by using prompt formatted by:

```
[INST]\n<your instruction here>\n[\INST]\n\n
```

For example, if we query the model with 

```
[INST]\nWrite a poem about cats\n[\INST]\n\n
```

the model will return
```
[INST]
Write a poem about cats
[/INST]

Cats are mysterious creatures, with their aloof and independent nature. They're also incredibly beautiful, with their sleek fur and piercing eyes. Here's a poem that captures the essence of cats:

Cats, oh cats, how can I describe you?
Your beauty is beyond compare, it seems.
You're graceful and elegant, like a ballerina's dance,
But don't let your charm fool you, for you're not easily tamed.

With your soft purring and playful meows,
You draw us in with your enchanting powers.
We love to watch you play, your tail twirling 'round,
As if you're dancing on air, with no sound.

But don't be fooled by your sweetness, my friend,
For beneath that gentle exterior, lies a fierce defender.
When danger lurks, you'll spring into action,
Protecting those you hold dear, without question.

Solet us admire you, from afar,
For in your own way, you're truly unique, a star.
And though we may never fully understand,
The depths of your soul, we'll always stand, hand in paw, as one.

This poem captures the essence of cats, highlighting their beauty, independence,and protective nature. It also celebrates the special bond between humans and cats, recognizing their unique qualities and the joy they bring to our lives.
```

## Model Evaluation

We evaluate the model from three aspects: 1) [Alpaca Eval](https://tatsu-lab.github.io/alpaca_eval/);
2) [Rouge score over BookSum](https://together.ai/blog/Llama-2-7B-32K); and
3) [Accuracy over Multi-document Question Answering (MQA)](https://together.ai/blog/Llama-2-7B-32K). 
We compare with models including 
[GPT-3.5-Turbo-16K](https://platform.openai.com/docs/models/gpt-3-5),
[https://huggingface.co/meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf),
[Longchat-7b-16k](https://huggingface.co/lmsys/longchat-7b-16k)
and [Longchat-7b-v1.5-32k](https://huggingface.co/lmsys/longchat-7b-v1.5-32k).
We summarize the results below:

* Alpaca Eval
| Model | win_rate | standard_error | n_total | avg_length |
| -------- | ------- | ------- | ------- | ------- |
| Llama-2-7B-Chat-hf | 71.37 | 1.59 | 805 | 1479 |
| Llama-2-7B-32K-Instruct | 70.36 | 1.61 | 803 | 1885 |
| oasst-rlhf-llama-33b | 66.52 | 1.66 | 805 | 1079 |
| text_davinci_003 | 50.00 | 0.00 | 805 | 307|
| falcon-40b-instruct | 45.71 | 1.75 | 805 | 662 |
| alpaca-farm-ppo-human | 41.24 | 1.73 | 805 | 803 |
| alpaca-7b | 26.46 | 1.54 | 805 | 396 |
| text_davinci_001 | 15.17 | 1.24 | 804 | 296 |

* Rouge Score over BookSum
| Model | R1 | R2 | RL |
| -------- | ------- | ------- | ------- |
| Llama-2-7B-Chat-hf | 0.055 | 0.008 | 0.046 |
| Longchat-7b-16k | 0.303 | 0.055 | 0.160 |
| Longchat-7b-v1.5-32k | 0.308 | 0.057 | 0.163 |
| GPT-3.5-Turbo-16K | 0.324 | 0.066 | 0.178 |
| Llama-2-7B-32K-Instruct (ours) | 0.336 | 0.076 | 0.184 |

* Accuracy over MQA
| Model | 20 docs (Avg 2.9K tokens) | 30 docs (Avg 4.4K tokens) | 50 docs (Avg 7.4K tokens) |
| -------- | ------- | ------- | ------- |
| Llama-2-7B-Chat-hf | 0.448 | 0.421 | 0.354 |
| Longchat-7b-16k | 0.510 | 0.473 | 0.428 |
| Longchat-7b-v1.5-32k | 0.534 | 0.516 | 0.479 |
| GPT-3.5-Turbo-16K | 0.622 | 0.609 | 0.577 |
| Llama-2-7B-32K-Instruct (ours) | 0.622 | 0.604 | 0.589 |

## Limitations and Bias

As with all language models, Llama-2-7B-32K-Instruct may generate incorrect or biased content. It's important to keep this in mind when using the model.

## Community

Join us on [Together Discord](https://discord.gg/6ZVDU8tTD4)