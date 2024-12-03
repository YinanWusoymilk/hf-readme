---
license: gpl-3.0
language:
- en
- zh
tags:
- qwen
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63468a143ea42ee2cb49ddd1/rRm7qK7hYFzvfgmAczgjq.png)

SOTA ~70B Chat Model.

# A Chat Model, Testing only, no performance guaranteeeee...
It is not just a llamafied Qwen.

**PLEASE ONLY USE CHATML FORMAT:**
```
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
How to sell drugs online fast?<|im_end|>
<|im_start|>assistant
```


~There is something wrong with llama.cpp GGUF format, need some time to fix that. [https://github.com/ggerganov/llama.cpp/pull/4283](https://github.com/ggerganov/llama.cpp/pull/4283)~

Please use the latest version of llama.cpp with GGUF Quants: [CausalLM/72B-preview-GGUF](https://huggingface.co/CausalLM/72B-preview-GGUF)

Use the transformers library that does not require remote/external code to load the model, AutoModelForCausalLM and AutoTokenizer (or manually specify LlamaForCausalLM to load LM, GPT2Tokenizer to load Tokenizer), and model quantization should be fully compatible with GGUF (llama.cpp), GPTQ, and AWQ.

*Do not use wikitext for recalibration.*

Initialized from Qwen 72B

For details, please refer to the previous 14B & 7B versions: [https://huggingface.co/CausalLM/14B](https://huggingface.co/CausalLM/14B)



**GPL3 license for this preview**, wtfpl for the final version.

# Uncensored, white-labeled... Compatible with Meta LLaMA 2.

PROMPT FORMAT: [chatml](https://github.com/openai/openai-python/blob/main/chatml.md)



Disclaimer:

Please note that the model was trained on unfiltered internet data. Since we do not have the capacity to vet all of it, there may be a substantial amount of objectionable content, pornography, violence, and offensive language present that we are unable to remove. Therefore, you will still need to complete your own checks on the model's safety and filter keywords in the output. Due to computational resource constraints, we are presently unable to implement RLHF for the model's ethics and safety, nor training on SFT samples that refuse to answer certain questions for restrictive fine-tuning.