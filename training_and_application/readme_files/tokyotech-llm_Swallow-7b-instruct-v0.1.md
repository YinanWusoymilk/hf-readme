---
language:
  - en
  - ja
library_name: transformers
pipeline_tag: text-generation
license: llama2
model_type: llama
---

# Swallow

Our Swallow model has undergone continual pre-training from the [Llama 2 family](https://huggingface.co/meta-llama), primarily with the addition of Japanese language data. The tuned versions use supervised fine-tuning (SFT). 
Links to other models can be found in the index.

# Model Release Updates

We are excited to share the release schedule for our latest models:
- **April 26, 2024**: Released version 0.1 of our enhanced instruction-tuned models: [Swallow-7b-instruct-v0.1](https://huggingface.co/tokyotech-llm/Swallow-7b-instruct-v0.1), [Swallow-13b-instruct-v0.1](https://huggingface.co/tokyotech-llm/Swallow-13b-instruct-v0.1), and [Swallow-70b-instruct-v0.1](https://huggingface.co/tokyotech-llm/Swallow-70b-instruct-v0.1) as preview versions.
- **March 2, 2024**: Released the [Swallow-7b-plus-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-plus-hf), a model trained with approximately twice as many Japanese tokens as [Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf).
- **February 4, 2024**: Released the [Swallow-13b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-NVE-hf).
- **January 26, 2024**: Released the [Swallow-7b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-NVE-hf), [Swallow-7b-NVE-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-NVE-instruct-hf), [Swallow-70b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-NVE-hf), and [Swallow-70b-NVE-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-NVE-instruct-hf)
- **December 19, 2023**: Released the [Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf), [Swallow-7b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-instruct-hf), [Swallow-13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf), [Swallow-13b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-instruct-hf), [Swallow-70b-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-hf), and [Swallow-70b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-instruct-hf).

## Swallow Model Index
|Model|Swallow-hf|Swallow-instruct-hf|Swallow-instruct-v0.1|
|---|---|---|---|
|7B| [Link](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) | [Link](https://huggingface.co/tokyotech-llm/Swallow-7b-instruct-hf)|[Link](https://huggingface.co/tokyotech-llm/Swallow-7b-instruct-v1.0)|
|7B-Plus| [Link](https://huggingface.co/tokyotech-llm/Swallow-7b-plus-hf) | N/A | N/A |
|13B| [Link](https://huggingface.co/tokyotech-llm/Swallow-13b-hf) | [Link](https://huggingface.co/tokyotech-llm/Swallow-13b-instruct-hf)| [Link](https://huggingface.co/tokyotech-llm/Swallow-13b-instruct-v1.0)|
|70B| [Link](https://huggingface.co/tokyotech-llm/Swallow-70b-hf) | [Link](https://huggingface.co/tokyotech-llm/Swallow-70b-instruct-hf)| [Link](https://huggingface.co/tokyotech-llm/Swallow-70b-instruct-v1.0)|

## Swallow Model Index NVE (No Vocabulary Expansion)
|Model|Swallow-NVE-hf|Swallow-NVE-instruct-hf|
|---|---|---|
|7B| [Link](https://huggingface.co/tokyotech-llm/Swallow-7b-NVE-hf) | [Link](https://huggingface.co/tokyotech-llm/Swallow-7b-NVE-instruct-hf)|
|13B| [Link](https://huggingface.co/tokyotech-llm/Swallow-13b-NVE-hf) | N/A |
|70B| [Link](https://huggingface.co/tokyotech-llm/Swallow-70b-NVE-hf) | [Link](https://huggingface.co/tokyotech-llm/Swallow-70b-NVE-instruct-hf)|

![logo](./logo.png)

This repository provides large language models developed by [TokyoTech-LLM](https://tokyotech-llm.github.io/).

## Model Details

* **Model type**: Please refer to LLaMA-2 technical report for details on the model architecture. 
* **Language(s)**: Japanese English
* **Tokenizer**: This model employs a tokenizer that features a broadened vocabulary based on Japanese data. This allows for a more efficient representation of text using fewer tokens, leading to a notably faster inference process.
* **Contact**: swallow[at]nlp.c.titech.ac.jp 

## Instruct Model Performance

### MT-Bench JA


#### Comparison to the past version

* NOTE that the models with the `v0.1` suffix are newer versions compared to their original counterparts with the `hf`.
* We report overall (i.e., average over scores of the first and second turns), first, and second turn scores.

##### Overall


|Model|Average|Writing|Roleplay|Reasoning|Math|Coding|Extraction|STEM|Humanities|
|---|---|---|---|---|---|---|---|---|---|
| Swallow-7b-instruct-v0.1 |0.3435|0.4450|0.4720|0.1853|0.1920|0.2204|0.3015|0.4594|0.4720|
| Swallow-7b-instruct-hf |0.1833|0.2205|0.1975|0.1593|0.1045|0.1282|0.2672|0.1908|0.1980|
| Swallow-13b-instruct-v0.1 |0.3669|0.4816|0.5562|0.2769|0.1020|0.1505|0.4179|0.4347|0.5150|
| Swallow-13b-instruct-hf |0.2004|0.1932|0.2552|0.1507|0.1184|0.1285|0.2641|0.2434|0.2500|
| Swallow-70b-instruct-v0.1 |0.4513|0.4822|0.5353|0.3497|0.3492|0.2668|0.5553|0.4955|0.5767|
| Swallow-70b-instruct-hf |0.3259|0.2925|0.4283|0.3447|0.1562|0.1856|0.5634|0.3315|0.3071|

##### First Turn

|Model|Average|Writing|Roleplay|Reasoning|Math|Coding|Extraction|STEM|Humanities|
|---|---|---|---|---|---|---|---|---|---|
| Swallow-7b-instruct-v0.1 |0.3829|0.4960|0.4800|0.2220|0.2820|0.2164|0.3220|0.5440|0.4980|
| Swallow-7b-instruct-hf |0.2216|0.2830|0.2150|0.1590|0.1080|0.1470|0.3542|0.2450|0.2650|
| Swallow-13b-instruct-v0.1 |0.3948|0.5400|0.5220|0.3020|0.1040|0.1760|0.5040|0.5180|0.4920|
| Swallow-13b-instruct-hf |0.2304|0.2460|0.2640|0.1610|0.1360|0.1330|0.3070|0.3010|0.2950|
| Swallow-70b-instruct-v0.1 |0.4849|0.5720|0.5020|0.4780|0.3680|0.2467|0.5400|0.5720|0.5960|
| Swallow-70b-instruct-hf |0.3631|0.3420|0.4007|0.4220|0.1580|0.2044|0.6120|0.4280|0.3360|

##### Second Turn

|Model|Average|Writing|Roleplay|Reasoning|Math|Coding|Extraction|STEM|Humanities|
|---|---|---|---|---|---|---|---|---|---|
| Swallow-7b-instruct-v0.1 |0.3059|0.3940|0.4640|0.1441|0.1000|0.2253|0.2811|0.3724|0.4449|
| Swallow-7b-instruct-hf |0.1432|0.1567|0.1798|0.1603|0.1010|0.1085|0.1767|0.1343|0.1295|
| Swallow-13b-instruct-v0.1 |0.3353|0.4213|0.5911|0.2516|0.1000|0.1244|0.3194|0.3473|0.5394|
| Swallow-13b-instruct-hf |0.1692|0.1364|0.2453|0.1401|0.1000|0.1237|0.2199|0.1850|0.2050|
| Swallow-70b-instruct-v0.1 |0.4179|0.3913|0.5689|0.2184|0.3280|0.2884|0.5711|0.4171|0.5562|
| Swallow-70b-instruct-hf |0.2872|0.2398|0.4564|0.2647|0.1540|0.1676|0.5118|0.2311|0.2762|

#### Comparison to the existing models

We only provide the overall score in this section.

##### 7B models

|Model|Average|Writing|Roleplay|Reasoning|Math|Coding|Extraction|STEM|Humanities|
|---|---|---|---|---|---|---|---|---|---|
| Swallow-7b-instruct-v0.1 |0.3435|0.4450|0.4720|0.1853|0.1920|0.2204|0.3015|0.4594|0.4720|
| ELYZA-japanese-Llama-2-7b-fast-instruct |0.2827|0.3289|0.3907|0.2424|0.1480|0.1584|0.3511|0.3053|0.3365|
| calm2-7b-chat |0.3204|0.4657|0.4898|0.1837|0.1005|0.1414|0.3927|0.3601|0.4293|
| calm2-7b-chat-dpo-experimental |0.3493|0.5312|0.5237|0.1857|0.1000|0.1813|0.3355|0.4320|0.5051|
| RakutenAI-7B-instruct |0.2994|0.3623|0.3711|0.3333|0.1763|0.1581|0.4215|0.2824|0.2901|
| RakutenAI-7B-chat |0.3667|0.4229|0.4644|0.3990|0.2161|0.2390|0.3416|0.3904|0.4601|

##### 13B models

|Model|Average|Writing|Roleplay|Reasoning|Math|Coding|Extraction|STEM|Humanities|
|---|---|---|---|---|---|---|---|---|---|
| Swallow-13b-instruct-v0.1 |0.3669|0.4816|0.5562|0.2769|0.1020|0.1505|0.4179|0.4347|0.5150|
| ELYZA-japanese-Llama-2-13b-instruct |0.3196|0.4400|0.4373|0.2098|0.2157|0.1572|0.3583|0.3243|0.4141|
| ELYZA-japanese-Llama-2-13b-fast-instruct |0.3042|0.3729|0.3930|0.1236|0.2492|0.1862|0.4360|0.3233|0.3496|

##### 70B models

|Model|Average|Writing|Roleplay|Reasoning|Math|Coding|Extraction|STEM|Humanities|
|---|---|---|---|---|---|---|---|---|---|
| Swallow-70b-instruct-v0.1 |0.4513|0.4822|0.5353|0.3497|0.3492|0.2668|0.5553|0.4955|0.5767|
| japanese-stablelm-instruct-beta-70b |0.3716|0.4179|0.3945|0.3656|0.2580|0.2186|0.4412|0.4663|0.4103|


## Evaluation Benchmarks

### MT-Bench JA

We used [Japanese MT-Bench](https://wandb.ai/wandb-japan/llm-leaderboard/artifacts/dataset/mtbench_ja_question) to assess the instruction-following capabilities of models.
We utilized the following settings:

- Implemantation: FastChat [Zheng+, 2023] (commit #e86e70d0)
- Question: [Nejumi LLM-Leaderboard NEO, mtbench_ja_question_v3](https://wandb.ai/wandb-japan/llm-leaderboard/artifacts/dataset/mtbench_ja_question/v3)
- Reference Answer: [Nejumi LLM-Leaderboard NEO, mtbench_ja_referenceanswer_v1](https://wandb.ai/wandb-japan/llm-leaderboard/artifacts/dataset/mtbench_ja_referenceanswer/v1)
- Prompt for Judge: [Nejumi LLM-Lederboard NEO, mtbench_ja_prompt_v1](https://wandb.ai/wandb-japan/llm-leaderboard/artifacts/dataset/mtbench_ja_prompt/v1)
- Judge: `gpt-4-1106-preview`
- Scoring: Absolute scale normalized to a 0-1 range, averaged over five runs.



## Usage

First install additional dependencies in [requirements.txt](./requirements.txt):

```sh
pip install -r requirements.txt
```

### Instruction format Ver0.1
This format must be adhered to strictly, as deviations may result in less optimal outputs from the model.

The template used to construct a prompt for the Instruct model is specified as follows:

```
<s>[INST] <<SYS>>\n{SYSTEM_PROMPT}\n<</SYS>>\n\n{USER_MESSAGE_1} [/INST] {BOT_MESSAGE_1}</s>[INST] {USER_MESSAGE_2} [/INST] 
```


Please be aware that ``<s>`` and ``</s>`` are special tokens used for the beginning of string (BOS) and end of string (EOS), respectively, while [INST] and [/INST] are considered regular strings.

For the "{SYSTEM_PROMPT}" part, We recommend using "あなたは誠実で優秀な日本人のアシスタントです。"

For the "{USER_MESSAGE_1}" part, We recommend using {instruction}\n{input}

In other words, We recommend the following:

``` 
<s>[INST] <<SYS>>\nあなたは誠実で優秀な日本人のアシスタントです。\n<</SYS>>\n\n{instruction1}\n{input1} [/INST] {BOT_MESSAGE_1}</s>[INST] {instruction2}\n{input2} [/INST] 
```


### Use the instruct model Ver0.1

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "tokyotech-llm/Swallow-70b-instruct-v0.1"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

device = "cuda"

messages = [
    {"role": "system", "content": "あなたは誠実で優秀な日本人のアシスタントです。"},
    {"role": "user", "content": "東京工業大学の主なキャンパスについて教えてください"}
]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(model_inputs, max_new_tokens=128, do_sample=True)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])
```

## Training Datasets

### Instruction Tuning Ver0.1

The following datasets were used for the instruction tuning. 

- [OpenAssistant Conversations Dataset EN top-1 thread](https://huggingface.co/datasets/OpenAssistant/oasst2)
- [OpenAssistant Conversations Dataset](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) was used, where human utterances are included but the responses are not used. Instead, the responses were generated using the [Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) model.
 
## Risks and Limitations

The models released here are still in the early stages of our research and development and have not been tuned to ensure outputs align with human intent and safety considerations.

## Acknowledgements

We thank Meta Research for releasing Llama 2 under an open license for others to build on.

Our project is supported by the [ABCI Large-scale Language Model Building Support Program](https://abci.ai/en/link/llm_support_program.html) of the National Institute of Advanced Industrial Science and Technology. 

## License

Llama 2 is licensed under the LLAMA 2 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved.

## Authors

Here are the team members:
- From [Okazaki Laboratory](https://www.nlp.c.titech.ac.jp/index.en.html), the following members:
  - [Naoaki Okazaki](https://www.chokkan.org/index.ja.html)
  - [Sakae Mizuki](https://s-mizuki-nlp.github.io/)
  - [Hiroki Iida](https://meshidenn.github.io/)
  - [Mengsay Loem](https://loem-ms.github.io/)
  - [Shota Hirai](https://huggingface.co/Kotemo428)
  - [Kakeru Hattori](https://aya-se.vercel.app/)
  - [Masanari Ohi](https://twitter.com/stjohn2007)
- From [YOKOTA Laboratory](https://www.rio.gsic.titech.ac.jp/en/index.html), the following members:
  - [Rio Yokota](https://twitter.com/rioyokota)
  - [Kazuki Fujii](https://twitter.com/okoge_kaz)
  - [Taishi Nakamura](https://twitter.com/Setuna7777_2)
  - [Takumi Okamoto](https://www.linkedin.com/in/takumi-okamoto)
  - [Ishida Shigeki](https://www.wantedly.com/id/reborn27)

## How to cite

If you find our work helpful, please feel free to cite us.

```
@inproceedings{Fujii:COLM2024,
   title={Continual Pre-Training for Cross-Lingual LLM Adaptation:
Enhancing Japanese Language Capabilities},
   author={Kazuki Fujii and Taishi Nakamura and Mengsay Loem and Hiroki
Iida and Masanari Ohi and Kakeru Hattori and Hirai Shota and Sakae
Mizuki and Rio Yokota and Naoaki Okazaki},
   booktitle="Proceedings of the First Conference on Language Modeling",
   series={COLM},
   pages="(to appear)",
   year="2024",
   month=oct,
   address={University of Pennsylvania, USA},
}

@inproceedings{Okazaki:COLM2024,
   title={Building a Large Japanese Web Corpus for Large Language Models},
   author={Naoaki Okazaki and Kakeru Hattori and Hirai Shota and Hiroki
Iida and Masanari Ohi and Kazuki Fujii and Taishi Nakamura and Mengsay
Loem and Rio Yokota and Sakae Mizuki},
   booktitle="Proceedings of the First Conference on Language Modeling",
   series={COLM},
   pages="(to appear)",
   year="2024",
   month=oct,
   address={University of Pennsylvania, USA},
}
```