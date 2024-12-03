---
base_model: mistralai/Mistral-Nemo-Instruct-2407
language:
- en
- fr
- de
- es
- it
- pt
- ru
- zh
- ja
library_name: transformers
license: apache-2.0
quantized_by: mradermacher
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags:  -->
static quants of https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407

<!-- provided-files -->
weighted/imatrix quants are available at https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.Q2_K.gguf) | Q2_K | 4.9 |  |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.IQ3_XS.gguf) | IQ3_XS | 5.4 |  |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.Q3_K_S.gguf) | Q3_K_S | 5.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.IQ3_S.gguf) | IQ3_S | 5.7 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.IQ3_M.gguf) | IQ3_M | 5.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.Q3_K_M.gguf) | Q3_K_M | 6.2 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.Q3_K_L.gguf) | Q3_K_L | 6.7 |  |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.IQ4_XS.gguf) | IQ4_XS | 6.9 |  |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.Q4_K_S.gguf) | Q4_K_S | 7.2 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.Q4_K_M.gguf) | Q4_K_M | 7.6 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.Q5_K_S.gguf) | Q5_K_S | 8.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.Q5_K_M.gguf) | Q5_K_M | 8.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.Q6_K.gguf) | Q6_K | 10.2 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407.Q8_0.gguf) | Q8_0 | 13.1 | fast, best quality |

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
