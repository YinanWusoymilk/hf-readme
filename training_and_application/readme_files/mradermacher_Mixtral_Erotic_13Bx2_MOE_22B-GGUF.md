---
base_model: cloudyu/Mixtral_Erotic_13Bx2_MOE_22B
language:
- en
library_name: transformers
license: cc-by-nc-4.0
quantized_by: mradermacher
---
## About

static quants of https://huggingface.co/cloudyu/Mixtral_Erotic_13Bx2_MOE_22B

<!-- provided-files -->
weighted/imatrix quants seem not to be available (by me) at this time. If they do not show up a week or so after the static ones, I have probably not planned for them. Feel free to request them by opening a Community Discussion.
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.Q2_K.gguf) | Q2_K | 8.2 |  |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.IQ3_XS.gguf) | IQ3_XS | 9.1 |  |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.IQ3_S.gguf) | IQ3_S | 9.6 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.Q3_K_S.gguf) | Q3_K_S | 9.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.IQ3_M.gguf) | IQ3_M | 10.0 |  |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.Q3_K_M.gguf) | Q3_K_M | 10.7 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.Q3_K_L.gguf) | Q3_K_L | 11.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.IQ4_XS.gguf) | IQ4_XS | 11.9 |  |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.Q4_0.gguf) | Q4_0 | 12.4 | fast, low quality |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.IQ4_NL.gguf) | IQ4_NL | 12.5 | prefer IQ4_XS |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.Q4_K_S.gguf) | Q4_K_S | 12.5 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.Q4_K_M.gguf) | Q4_K_M | 13.3 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.Q5_K_S.gguf) | Q5_K_S | 15.1 |  |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.Q5_K_M.gguf) | Q5_K_M | 15.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.Q6_K.gguf) | Q6_K | 17.9 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/Mixtral_Erotic_13Bx2_MOE_22B-GGUF/resolve/main/Mixtral_Erotic_13Bx2_MOE_22B.Q8_0.gguf) | Q8_0 | 23.1 | fast, best quality |

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
