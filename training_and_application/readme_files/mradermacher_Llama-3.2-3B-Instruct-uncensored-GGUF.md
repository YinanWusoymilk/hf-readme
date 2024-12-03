---
base_model: chuanli11/Llama-3.2-3B-Instruct-uncensored
language:
- en
library_name: transformers
quantized_by: mradermacher
tags: []
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags:  -->
static quants of https://huggingface.co/chuanli11/Llama-3.2-3B-Instruct-uncensored

<!-- provided-files -->
weighted/imatrix quants are available at https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.Q2_K.gguf) | Q2_K | 1.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.IQ3_XS.gguf) | IQ3_XS | 1.7 |  |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.IQ3_S.gguf) | IQ3_S | 1.8 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.Q3_K_S.gguf) | Q3_K_S | 1.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.IQ3_M.gguf) | IQ3_M | 1.9 |  |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.Q3_K_M.gguf) | Q3_K_M | 2.0 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.Q3_K_L.gguf) | Q3_K_L | 2.1 |  |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.IQ4_XS.gguf) | IQ4_XS | 2.2 |  |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.Q4_K_S.gguf) | Q4_K_S | 2.2 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.Q4_K_M.gguf) | Q4_K_M | 2.3 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.Q5_K_S.gguf) | Q5_K_S | 2.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.Q5_K_M.gguf) | Q5_K_M | 2.7 |  |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.Q6_K.gguf) | Q6_K | 3.1 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.Q8_0.gguf) | Q8_0 | 3.9 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF/resolve/main/Llama-3.2-3B-Instruct-uncensored.f16.gguf) | f16 | 7.3 | 16 bpw, overkill |

Here is a handy graph by ikawrakow comparing some lower-quality quant
types (lower is better):

![image.png](https://www.nethype.de/huggingface_embed/quantpplgraph.png)

And here are Artefact2's thoughts on the matter:
https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9

## FAQ / Model Request

See https://huggingface.co/mradermacher/model_requests for some answers to
questions you might have and/or if you want some other model quantized.

## Thanks

I thank my company, [nethype GmbH](https://www.nethype.de/), for letting
me use its servers and providing upgrades to my workstation to enable
this work in my free time.

<!-- end -->
