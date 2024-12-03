---
base_model: aifeifei798/llama3-8B-DarkIdol-2.2-Uncensored-1048K
language:
- en
- ja
- zh
library_name: transformers
license: llama3
quantized_by: mradermacher
tags:
- roleplay
- llama3
- sillytavern
- idol
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags:  -->
static quants of https://huggingface.co/aifeifei798/llama3-8B-DarkIdol-2.2-Uncensored-1048K

<!-- provided-files -->
weighted/imatrix quants are available at https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.Q2_K.gguf) | Q2_K | 3.3 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.IQ3_XS.gguf) | IQ3_XS | 3.6 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.Q3_K_S.gguf) | Q3_K_S | 3.8 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.IQ3_S.gguf) | IQ3_S | 3.8 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.IQ3_M.gguf) | IQ3_M | 3.9 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.Q3_K_M.gguf) | Q3_K_M | 4.1 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.Q3_K_L.gguf) | Q3_K_L | 4.4 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.IQ4_XS.gguf) | IQ4_XS | 4.6 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.Q4_K_S.gguf) | Q4_K_S | 4.8 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.Q4_K_M.gguf) | Q4_K_M | 5.0 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.Q5_K_S.gguf) | Q5_K_S | 5.7 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.Q5_K_M.gguf) | Q5_K_M | 5.8 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.Q6_K.gguf) | Q6_K | 6.7 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.Q8_0.gguf) | Q8_0 | 8.6 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/llama3-8B-DarkIdol-2.2-Uncensored-1048K-GGUF/resolve/main/llama3-8B-DarkIdol-2.2-Uncensored-1048K.f16.gguf) | f16 | 16.2 | 16 bpw, overkill |

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
