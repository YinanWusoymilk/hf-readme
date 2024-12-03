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
inference: false
base_model: rinna/japanese-gpt-neox-3.6b
---

# japanese-gpt-neox-3.6b-instruction-ppo

![rinna-icon](./rinna.png)

# Overview
This repository provides a Japanese GPT-NeoX model of 3.6 billion parameters. The model is based on [`rinna/japanese-gpt-neox-3.6b-instruction-sft-v2`](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) and has been aligned to serve as an instruction-following conversational agent.

* **Model architecture**

    A 36-layer, 2816-hidden-size transformer-based language model.

* **RLHF**

    Following the [OpenAI InstructGPT paper](https://arxiv.org/abs/2203.02155), **Reinforcement Learning from Human Feedback** (RLHF) has been applied to aligning the model's behaviour with input instructions. Particularly, the model has been trained in two stages, i.e. **Supervised Fine-Tuning** (SFT) and [PPO](https://arxiv.org/abs/1707.06347)-based **Reinforcement Learning** (RL). 
    * The first SFT stage produces [`rinna/japanese-gpt-neox-3.6b-instruction-sft-v2`](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2).
    * The second RL stage produces this model.

* **PPO vs. SFT evaluation**
    
    We conducted human evaluation and ChatGPT-based automated evaluation on 100 prompts to assess the *performance gain from reinforcement learning*. 

    | [PPO](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) vs. [SFT](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) | win | tie | loss |
    | :---: | :---: | :---: | :---: |
    | Human evaluation | **47**% | 30% | 23% |
    | ChatGPT auto. evaluation | **63**% | 3% | 34% |

* **Reinforcement learning**
    
    We used [CarperAI/trlx](https://github.com/CarperAI/trlx) and its implementation of the PPO algorithm for the RL stage.
    
    The RL data is the subset of the following dataset and has been translated into Japanese.
    * [Anthropic HH RLHF data](https://huggingface.co/datasets/Anthropic/hh-rlhf)

* **Model Series**

    | Variant | Link |
    | :-- | :--|
    | 3.6B PPO | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo |
    | 3.6B SFT-v2 | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2 |
    | 3.6B SFT | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft |
    | 3.6B pretrained | https://huggingface.co/rinna/japanese-gpt-neox-3.6b |
    
* **Contributors**
    
    [Tianyu Zhao](https://huggingface.co/tianyuz) and [Kei Sawada](https://huggingface.co/keisawada)

# Limitations
* We found this verison of PPO model tends to generate repeated text more often than its SFT counterpart, and thus we set `repetition_penalty=1.1` for better generation performance. (*The same generation hyper-parameters are applied to the SFT model in aforementioned evaluation experiments.*) You can also explore other hyperparameter combinations that yield higher generation randomness/diversity for better generation quality, e.g. `temperature=0.9, repetition_penalty=1.0`.

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
        "text": "コンタクトレンズを慣れるにはどうすればよいですか？"
    },
    {
        "speaker": "システム",
        "text": "これについて具体的に説明していただけますか？何が難しいのでしょうか？"
    },
    {
        "speaker": "ユーザー",
        "text": "目が痛いのです。"
    },
    {
        "speaker": "システム",
        "text": "分かりました、コンタクトレンズをつけると目がかゆくなるということですね。思った以上にレンズを外す必要があるでしょうか？"
    },
    {
        "speaker": "ユーザー",
        "text": "いえ、レンズは外しませんが、目が赤くなるんです。"
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
# "ユーザー: コンタクトレンズを慣れるにはどうすればよいですか？<NL>システム: これについて具体的に説明していただけますか？何が難しいのでしょうか？<NL>ユーザー: 目が痛いのです。<NL>システム: 分かりました、コンタクトレンズをつけると目がかゆくなるということですね。思った以上にレンズを外す必要があるでしょうか？<NL>ユーザー: いえ、レンズは外しませんが、目が赤くなるんです。<NL>システム: "
~~~
# How to use the model

~~~~python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt-neox-3.6b-instruction-ppo", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt-neox-3.6b-instruction-ppo")

if torch.cuda.is_available():
    model = model.to("cuda")

token_ids = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        do_sample=True,
        max_new_tokens=128,
        temperature=0.7,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.pad_token_id,
        bos_token_id=tokenizer.bos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

output = tokenizer.decode(output_ids.tolist()[0][token_ids.size(1):])
output = output.replace("<NL>", "\n")
print(output)
"""それは、コンタクトレンズが目に合わないために起こることがあります。レンズが目の表面に長時間触れ続けることが原因となることがあります。また、コンタクトレンズが汚れている可能性もあります。コンタクトレンズケースを定期的に洗浄したり、コンタクトレンズを正しくフィットさせるようにしたりすることが役立ちます。</s>"""
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
@misc{rinna-japanese-gpt-neox-3.6b-instruction-ppo,
    title = {rinna/japanese-gpt-neox-3.6b-instruction-ppo},
    author = {Zhao, Tianyu and Sawada, Kei},
    url = {https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo}
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