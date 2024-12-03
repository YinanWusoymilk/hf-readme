---
license: apache-2.0
datasets:
- wikipedia
- mc4
- cc100
- oscar
language:
- ja
---
# japanese-large-lm-3.6b

This repository provides a 3.6B parameters Japanese language model, trained by [LINE Corporation](https://linecorp.com/ja/).

[Tech Blog](https://engineering.linecorp.com/ja/blog/3.6-billion-parameter-japanese-language-model) explains details.

## How to use

```
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, set_seed
 
model = AutoModelForCausalLM.from_pretrained("line-corporation/japanese-large-lm-3.6b", torch_dtype=torch.float16)
tokenizer = AutoTokenizer.from_pretrained("line-corporation/japanese-large-lm-3.6b", use_fast=False)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)
set_seed(101)
 
text = generator(
    "おはようございます、今日の天気は",
    max_length=30,
    do_sample=True,
    pad_token_id=tokenizer.pad_token_id,
    num_return_sequences=5,
)
 
for t in text:
  print(t)
 
# 下記は生成される出力の例
# [{'generated_text': 'おはようございます、今日の天気は雨模様ですね。梅雨のこの時期の 朝は洗濯物が乾きにくいなど、主婦にとっては悩みどころですね。 では、'},
#  {'generated_text': 'おはようございます、今日の天気は晴れ。 気温は8°C位です。 朝晩は結構冷え込むようになりました。 寒くなってくると、...'},
#  {'generated_text': 'おはようございます、今日の天気は曇りです。 朝起きたら雪が軽く積もっていた。 寒さもそれほどでもありません。 日中は晴れるみたいですね。'},
#  {'generated_text': 'おはようございます、今日の天気は☁のち☀です。 朝の気温5°C、日中も21°Cと 暖かい予報です'},
#  {'generated_text': 'おはようございます、今日の天気は晴天ですが涼しい1日です、気温は午後になり低くなり25°Cくらい、風も強いようですので、'}]
```

## Model architecture
| Model | Vocab size | Architecture | Position type | Layers | Hidden dim | Attention heads |
| :---: | :--------: | :----------- | :-----------: | :----: | :--------: | :-------------: |
| 1.7B  | 51200      | GPT2         | Absolute      | 24     | 2304       | 24 |
| 3.6B  | 51200      | GPTNeoX      | RoPE          | 30     | 3072       | 32 |

## Training Corpus
Our training corpus consists of the Japanese portions of publicly available corpus such as C4, CC-100, and Oscar.
We also incorporated the Web texts crawled by in-house system.
The total size of our training corpus is about 650 GB.
The trained model achieves 7.50 perplexity on the internal validation sets of Japanese C4.

## Tokenization
We use a sentencepiece tokenizer with a unigram language model and byte-fallback.
We **do not** apply pre-tokenization with Japanese tokenizer.
Thus, a user may directly feed raw sentences into the tokenizer.


## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)