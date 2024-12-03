---
license: llama2
train: false
inference: false
pipeline_tag: text-generation
---

This is an experimental <a href="https://github.com/mobiusml/hqq/">HQQ</a> 1-bit quantized (<b>binary weights</b>) <a href="https://huggingface.co/meta-llama/Llama-2-7b-chat-hf"> Llama2-7B-chat model </a> using a low-rank adapter to improve the performance (referred to as <a href="https://mobiusml.github.io/1bit_blog/">HQQ+</a>).  

![image/gif](https://cdn-uploads.huggingface.co/production/uploads/636b945ef575d3705149e982/3fOfrg-5WtJwC5cpcVDub.gif)

Quantizing small models at extreme low-bits is a challenging task. The purpose of this model is to show the community what to expect when fine-tuning such models. 
We notice that, 1-bit quantization doesn't work well when applied directly on small models such as the Llama2-7B. However, when fine-tuned, the model's ouput significantly improves. In fact, the 1-bit base model outperforms Quip# 2-bit after fine-tuning on ~2.8K samples.  

Note that the weights here are unsigned 1-bit (0 or 1), <a href="https://arxiv.org/abs/2402.17764">not ternary like the recent 1.58-bit work </a>. This is a more challenging task since we lose the sign of the weights and only fine-tune a small fraction of the parameters (~94MB worth of weights). 
The dequantization step can be rewriten as a 1-bit matmul which could potentially require only additions + a very low-rank matmul which is fast to compute. 

This version offloads the meta-data to the CPU, so only the binary weights and the low-rank adapters are stored in the GPU memory. 

## Datasets
The adapter was trained via SFT on random subsets of the following:

### Base Model
* <a href="https://huggingface.co/datasets/wikitext">wikitext-2-raw-v1</a> (full)

### Chat Model
* <a href="https://huggingface.co/datasets/timdettmers/openassistant-guana"> timdettmers/openassistant-guanaco </a> (full)
* <a href="https://huggingface.co/datasets/icrosoft/orca-math-word-problems-200k"> microsoft/orca-math-word-problems-200k </a> (25K)
* <a href="https://huggingface.co/datasets/meta-math/MetaMathQA"> meta-math/MetaMathQA </a> (25K)
* <a href="https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized"> HuggingFaceH4/ultrafeedback_binarized </a> (25K - chosen answers only)

## Performance
| Models            | Llama2-7B (fp16)| Llama2-7B (HQQ 1-bit)| Llama2-7B (HQQ+ 1-bit)| Quip# (2-bit)|
|-------------------|------------------|------------------|------------------|------------------|
| Wiki Perpexlity   |    5.18          |      9866        |    <b>8.53</b>   |      8.54        |
| VRAM (GB)         |    13.5          |   <b>1.76</b>    |    1.85          |      2.72        |
| forward time (sec)|   <b>0.1<b>      |    0.231         |     0.257        |      0.353       |

| Models            | Llama2-7B-chat (fp16)| Llama2-7B-chat (HQQ 1-bit)| Llama2-7B-chat (HQQ+ 1-bit)|
|-------------------|------------------|------------------|------------------|
| ARC (25-shot)     |    53.67         |  21.59           |  31.14  |
| HellaSwag (10-shot)|   78.56         |  25.66           |  52.96  |
| MMLU (5-shot)     |    48.16         |  25.08           |  26.54  |
| TruthfulQA-MC2    |    45.32         |  47.81           |  43.16  |
| Winogrande (5-shot)|   72.53         |  49.72           |  60.54  |
| GSM8K (5-shot)    |    23.12         |  0               |  11     |
| Average           |    53.56         |  28.31           |  37.56  |

## Usage
First, install <a href="https://github.com/mobiusml/hqq/">HQQ</a>:
```
pip install hqq==0.1.8
pip install transformers==4.40
```
Then you can use the sample code below:
``` Python
from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer

#Load the model
model_id = 'mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq' 
model     = HQQModelForCausalLM.from_quantized(model_id, adapter='adapter_v0.1.lora')
tokenizer = AutoTokenizer.from_pretrained(model_id)

#Setup Inference Mode
tokenizer.add_bos_token = False
tokenizer.add_eos_token = False
if not tokenizer.pad_token: tokenizer.add_special_tokens({'pad_token': '[PAD]'})
model.config.use_cache  = True
model.eval();

# Optional: torch compile for faster inference
# model = torch.compile(model)

#Streaming Inference
import torch, transformers
from threading import Thread

def chat_processor(chat, max_new_tokens=100, do_sample=True, device='cuda'):
    tokenizer.use_default_system_prompt = False
    streamer = transformers.TextIteratorStreamer(tokenizer, timeout=10.0, skip_prompt=True, skip_special_tokens=True)

    generate_params = dict(
        tokenizer("<s> [INST] " + chat + " [/INST] ", return_tensors="pt").to(device),
        streamer=streamer,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        pad_token_id=tokenizer.pad_token_id,
        top_p=0.90 if do_sample else None,
        top_k=50 if do_sample else None,
        temperature= 0.6 if do_sample else None,
        num_beams=1,
        repetition_penalty=1.2,
    )

    t = Thread(target=model.generate, kwargs=generate_params)
    t.start()
    
    print("User: ", chat); 
    print("Assistant: ");
    outputs = ""
    for text in streamer:
        outputs += text
        print(text, end="", flush=True)

    torch.cuda.empty_cache()
  
    return outputs
```

### Example
``` Python
outputs = chat_processor("What is the solution to x^2 - 1 = 0", max_new_tokens=1000, do_sample=False)
```
```
User:  What is the solution to x^2 - 1 = 0
Assistant: 
The equation $x^2 - 1 = 0$ can be factored as $(x-1)(x+1) = 0$.
You want to find a value of $x$ that makes this true for all values of $x$. This means that either $x=1$ or $-1$, or $x=-1$. So, there are two solutions: $x=\boxed{1}$ and $x=\boxed{-1}$. The answer is: 1
```
