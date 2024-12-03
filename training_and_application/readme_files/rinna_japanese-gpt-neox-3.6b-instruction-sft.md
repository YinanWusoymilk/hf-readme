---
language: ja
thumbnail: https://github.com/rinnakk/japanese-pretrained-models/blob/master/rinna.png
tags:
- gpt_neox
- text-generation
- lm
- nlp
license: mit
datasets:
- Anthropic/hh-rlhf
- stanfordnlp/SHP
inference: false
base_model: rinna/japanese-gpt-neox-3.6b
---

# japanese-gpt-neox-3.6b-instruction-sft

![rinna-icon](./rinna.png)

# Overview
This repository provides a Japanese GPT-NeoX model of 3.6 billion parameters. The model is based on [`rinna/japanese-gpt-neox-3.6b`](https://huggingface.co/rinna/japanese-gpt-neox-3.6b) and has been finetuned to serve as an instruction-following conversational agent.

* **Model architecture**
    
    A 36-layer, 2816-hidden-size transformer-based language model.

* **Finetuning**
    
    The finetuning data is the subset of the following datasets and has been translated into Japanese.
    * [Anthropic HH RLHF data](https://huggingface.co/datasets/Anthropic/hh-rlhf)
    * [FLAN Instruction Tuning data](https://github.com/google-research/FLAN)
    * [Stanford Human Preferences Dataset](https://huggingface.co/datasets/stanfordnlp/SHP)

    The data will **not** be released.

* **Model Series**

    | Variant | Link |
    | :-- | :--|
    | 3.6B PPO | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo |
    | 3.6B SFT-v2 | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2 |
    | 3.6B SFT | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft |
    | 3.6B pretrained | https://huggingface.co/rinna/japanese-gpt-neox-3.6b |
    
* **Contributors**
    
    [Tianyu Zhao](https://huggingface.co/tianyuz) and [Kei Sawada](https://huggingface.co/keisawada)

# I/O Format
A special format has been adopted to construct inputs.
* An input prompt is formatted as a conversation between `ユーザー` and `システム`.
* Each input utterance consists of (1) its speaker (`"ユーザー"` or `"システム"`), (2) a colon (`":"`), (3) a whitespace (`" "`), and (4) utterance text (e.g. `"世界で一番高い山は？"`).
* The input prompt should be ended with `"システム: "` to acknowledge the model to generate a response.
* Since the model's tokenizer does not recognize `"\n"`, a special newline symbol `"<NL>"` is used instead.
* All the newlines in input and output utterances should be replaced with `"<NL>"`.
* All the utterances in the input prompt should be separated by `"<NL>"`.

Following is an example to construct an input from a conversation.
~~~python
prompt = [
    {
        "speaker": "ユーザー",
        "text": "日本のおすすめの観光地を教えてください。"
    },
    {
        "speaker": "システム",
        "text": "どの地域の観光地が知りたいですか？"
    },
    {
        "speaker": "ユーザー",
        "text": "渋谷の観光地を教えてください。"
    }
]
prompt = [
    f"{uttr['speaker']}: {uttr['text']}"
    for uttr in prompt
]
prompt = "<NL>".join(prompt)
prompt = (
    prompt
    + "<NL>"
    + "システム: "
)
print(prompt)
# "ユーザー: 日本のおすすめの観光地を教えてください。<NL>システム: どの地域の観光地が知りたいですか？<NL>ユーザー: 渋谷の観光地を教えてください。<NL>システム: "
~~~

# How to use the model

~~~~python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt-neox-3.6b-instruction-sft", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt-neox-3.6b-instruction-sft")

if torch.cuda.is_available():
    model = model.to("cuda")

token_ids = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        do_sample=True,
        max_new_tokens=128,
        temperature=0.7,
        pad_token_id=tokenizer.pad_token_id,
        bos_token_id=tokenizer.bos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

output = tokenizer.decode(output_ids.tolist()[0][token_ids.size(1):])
output = output.replace("<NL>", "\n")
print(output)
"""分かりました。いくつかのおすすめを紹介します。
1. ハチ公像です。ハチ公像は、日本の観光スポットの1つとして人気があります。
2. スクランブル交差点です。多くの人々が行き交う大きな交差点で、観光客に人気のスポットです。
3. 109です。109は、ショッピングやエンターテイメント施設です。
4. 道玄坂です。道玄坂は、日本の商業地区である坂道です。</s>"""
~~~~

# Tokenization
The model uses a [sentencepiece](https://github.com/google/sentencepiece)-based tokenizer.
* The tokenizer has a vocabulary size of 32,000.
* It uses sentencepiece's byte fallback feature to decompose unknown text pieces into UTF-8 byte pieces and to avoid producing `<UNK>` tokens.
* sentencepiece's `--add_dummy_prefix` option was turned off so that a leading whitespace will not be prepended automatically.
    ~~~
    print(tokenizer.tokenize("吾輩は猫である"))
    # ['吾', '輩', 'は', '猫', 'である']
    # instead of ['▁', '吾', '輩', 'は', '猫', 'である'] as in rinna/japanese-gpt-1b
    ~~~
* sentencepiece's `--remove_extra_whitespaces` option was turned off so that leading, trailing, and duplicate whitespaces are reserved.
    ~~~
    print(tokenizer.tokenize("  吾輩は  猫である   "))
    # ['▁', '▁', '吾', '輩', 'は', '▁', '▁', '猫', 'である', '▁', '▁', '▁']
    # instead of ['▁', '吾', '輩', 'は', '▁猫', 'である'] as in rinna/japanese-gpt-1b
    ~~~
* Don't forget to set `use_fast=False` to make the above features function correctly.
    ~~~
    good_tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt-neox-3.6b", use_fast=False)
    bad_tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt-neox-3.6b")

    print(good_tokenizer.decode(good_tokenizer.encode("გამარჯობა  吾輩は  猫である   ")))
    # 'გამარჯობა  吾輩は  猫である   </s>'
    print(bad_tokenizer.decode(bad_tokenizer.encode("გამარჯობა  吾輩は  猫である   ")))
    # 'გამარ[UNK]ობა 吾輩は 猫である </s>'
    ~~~

# How to cite
```bibtex
@misc{rinna-japanese-gpt-neox-3.6b-instruction-sft,
    title = {rinna/japanese-gpt-neox-3.6b-instruction-sft},
    author = {Zhao, Tianyu and Sawada, Kei},
    url = {https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft}
}

@inproceedings{sawada2024release,
    title = {Release of Pre-Trained Models for the {J}apanese Language},
    author = {Sawada, Kei and Zhao, Tianyu and Shing, Makoto and Mitsui, Kentaro and Kaga, Akio and Hono, Yukiya and Wakatsuki, Toshiaki and Mitsuda, Koh},
    booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)},
    month = {5},
    year = {2024},
    pages = {13898--13905},
    url = {https://aclanthology.org/2024.lrec-main.1213},
    note = {\url{https://arxiv.org/abs/2404.01657}}
}
```

# Licenese
[The MIT license](https://opensource.org/licenses/MIT)