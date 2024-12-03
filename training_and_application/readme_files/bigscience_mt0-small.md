---
datasets:
- bigscience/xP3
- mc4
license: apache-2.0
language:
- af
- am
- ar
- az
- be
- bg
- bn
- ca
- ceb
- co
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fil
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- haw
- hi
- hmn
- ht
- hu
- hy
- ig
- is
- it
- iw
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lb
- lo
- lt
- lv
- mg
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- my
- ne
- nl
- no
- ny
- pa
- pl
- ps
- pt
- ro
- ru
- sd
- si
- sk
- sl
- sm
- sn
- so
- sq
- sr
- st
- su
- sv
- sw
- ta
- te
- tg
- th
- tr
- uk
- und
- ur
- uz
- vi
- xh
- yi
- yo
- zh
- zu
pipeline_tag: text2text-generation
widget:
- text: "一个传奇的开端，一个不灭的神话，这不仅仅是一部电影，而是作为一个走进新时代的标签，永远彪炳史册。Would you rate the previous review as positive, neutral or negative?"
  example_title: "zh-en sentiment"
- text: "一个传奇的开端，一个不灭的神话，这不仅仅是一部电影，而是作为一个走进新时代的标签，永远彪炳史册。你认为这句话的立场是赞扬、中立还是批评？"
  example_title: "zh-zh sentiment"
- text: "Suggest at least five related search terms to \"Mạng neural nhân tạo\"."
  example_title: "vi-en query"
- text: "Proposez au moins cinq mots clés concernant «Réseau de neurones artificiels»."
  example_title: "fr-fr query"
- text: "Explain in a sentence in Telugu what is backpropagation in neural networks."
  example_title: "te-en qa"
- text: "Why is the sky blue?"
  example_title: "en-en qa"
- text: "Write a fairy tale about a troll saving a princess from a dangerous dragon. The fairy tale is a masterpiece that has achieved praise worldwide and its moral is \"Heroes Come in All Shapes and Sizes\". Story (in Spanish):"
  example_title: "es-en fable"
- text: "Write a fable about wood elves living in a forest that is suddenly invaded by ogres. The fable is a masterpiece that has achieved praise worldwide and its moral is \"Violence is the last refuge of the incompetent\". Fable (in Hindi):"
  example_title: "hi-en fable"
model-index:
- name: mt0-small
  results:
  - task:
      type: Coreference resolution
    dataset:
      type: winogrande
      name: Winogrande XL (xl)
      config: xl
      split: validation
      revision: a80f460359d1e9a67c006011c94de42a8759430c
    metrics:
    - type: Accuracy
      value: 50.51
  - task:
      type: Coreference resolution
    dataset:
      type: Muennighoff/xwinograd
      name: XWinograd (en)
      config: en
      split: test
      revision: 9dd5ea5505fad86b7bedad667955577815300cee
    metrics:
    - type: Accuracy
      value: 51.31
  - task:
      type: Coreference resolution
    dataset:
      type: Muennighoff/xwinograd
      name: XWinograd (fr)
      config: fr
      split: test
      revision: 9dd5ea5505fad86b7bedad667955577815300cee
    metrics:
    - type: Accuracy
      value: 54.22
  - task:
      type: Coreference resolution
    dataset:
      type: Muennighoff/xwinograd
      name: XWinograd (jp)
      config: jp
      split: test
      revision: 9dd5ea5505fad86b7bedad667955577815300cee
    metrics:
    - type: Accuracy
      value: 52.45
  - task:
      type: Coreference resolution
    dataset:
      type: Muennighoff/xwinograd
      name: XWinograd (pt)
      config: pt
      split: test
      revision: 9dd5ea5505fad86b7bedad667955577815300cee
    metrics:
    - type: Accuracy
      value: 51.71
  - task:
      type: Coreference resolution
    dataset:
      type: Muennighoff/xwinograd
      name: XWinograd (ru)
      config: ru
      split: test
      revision: 9dd5ea5505fad86b7bedad667955577815300cee
    metrics:
    - type: Accuracy
      value: 54.29
  - task:
      type: Coreference resolution
    dataset:
      type: Muennighoff/xwinograd
      name: XWinograd (zh)
      config: zh
      split: test
      revision: 9dd5ea5505fad86b7bedad667955577815300cee
    metrics:
    - type: Accuracy
      value: 54.17
  - task:
      type: Natural language inference
    dataset:
      type: anli
      name: ANLI (r1)
      config: r1
      split: validation
      revision: 9dbd830a06fea8b1c49d6e5ef2004a08d9f45094
    metrics:
    - type: Accuracy
      value: 34.7
  - task:
      type: Natural language inference
    dataset:
      type: anli
      name: ANLI (r2)
      config: r2
      split: validation
      revision: 9dbd830a06fea8b1c49d6e5ef2004a08d9f45094
    metrics:
    - type: Accuracy
      value: 34.0
  - task:
      type: Natural language inference
    dataset:
      type: anli
      name: ANLI (r3)
      config: r3
      split: validation
      revision: 9dbd830a06fea8b1c49d6e5ef2004a08d9f45094
    metrics:
    - type: Accuracy
      value: 33.83
  - task:
      type: Natural language inference
    dataset:
      type: super_glue
      name: SuperGLUE (cb)
      config: cb
      split: validation
      revision: 9e12063561e7e6c79099feb6d5a493142584e9e2
    metrics:
    - type: Accuracy
      value: 50.0
  - task:
      type: Natural language inference
    dataset:
      type: super_glue
      name: SuperGLUE (rte)
      config: rte
      split: validation
      revision: 9e12063561e7e6c79099feb6d5a493142584e9e2
    metrics:
    - type: Accuracy
      value: 61.01
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (ar)
      config: ar
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 37.43
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (bg)
      config: bg
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 37.55
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (de)
      config: de
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 35.78
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (el)
      config: el
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 37.43
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (en)
      config: en
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 38.47
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (es)
      config: es
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 36.75
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (fr)
      config: fr
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 37.15
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (hi)
      config: hi
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 35.38
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (ru)
      config: ru
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 37.35
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (sw)
      config: sw
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 35.18
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (th)
      config: th
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 37.55
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (tr)
      config: tr
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 36.51
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (ur)
      config: ur
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 35.78
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (vi)
      config: vi
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 36.95
  - task:
      type: Natural language inference
    dataset:
      type: xnli
      name: XNLI (zh)
      config: zh
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 37.07
  - task:
      type: Sentence completion
    dataset:
      type: story_cloze
      name: StoryCloze (2016)
      config: "2016"
      split: validation
      revision: e724c6f8cdf7c7a2fb229d862226e15b023ee4db
    metrics:
    - type: Accuracy
      value: 54.36
  - task:
      type: Sentence completion
    dataset:
      type: super_glue
      name: SuperGLUE (copa)
      config: copa
      split: validation
      revision: 9e12063561e7e6c79099feb6d5a493142584e9e2
    metrics:
    - type: Accuracy
      value: 57.0
  - task:
      type: Sentence completion
    dataset:
      type: xcopa
      name: XCOPA (et)
      config: et
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 57.0
  - task:
      type: Sentence completion
    dataset:
      type: xcopa
      name: XCOPA (ht)
      config: ht
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 60.0
  - task:
      type: Sentence completion
    dataset:
      type: xcopa
      name: XCOPA (id)
      config: id
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 59.0
  - task:
      type: Sentence completion
    dataset:
      type: xcopa
      name: XCOPA (it)
      config: it
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 59.0
  - task:
      type: Sentence completion
    dataset:
      type: xcopa
      name: XCOPA (qu)
      config: qu
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 54.0
  - task:
      type: Sentence completion
    dataset:
      type: xcopa
      name: XCOPA (sw)
      config: sw
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 55.0
  - task:
      type: Sentence completion
    dataset:
      type: xcopa
      name: XCOPA (ta)
      config: ta
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 59.0
  - task:
      type: Sentence completion
    dataset:
      type: xcopa
      name: XCOPA (th)
      config: th
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 65.0
  - task:
      type: Sentence completion
    dataset:
      type: xcopa
      name: XCOPA (tr)
      config: tr
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 58.0
  - task:
      type: Sentence completion
    dataset:
      type: xcopa
      name: XCOPA (vi)
      config: vi
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 54.0
  - task:
      type: Sentence completion
    dataset:
      type: xcopa
      name: XCOPA (zh)
      config: zh
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 56.0
  - task:
      type: Sentence completion
    dataset:
      type: Muennighoff/xstory_cloze
      name: XStoryCloze (ar)
      config: ar
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 48.78
  - task:
      type: Sentence completion
    dataset:
      type: Muennighoff/xstory_cloze
      name: XStoryCloze (es)
      config: es
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 55.2
  - task:
      type: Sentence completion
    dataset:
      type: Muennighoff/xstory_cloze
      name: XStoryCloze (eu)
      config: eu
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 52.95
  - task:
      type: Sentence completion
    dataset:
      type: Muennighoff/xstory_cloze
      name: XStoryCloze (hi)
      config: hi
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 53.01
  - task:
      type: Sentence completion
    dataset:
      type: Muennighoff/xstory_cloze
      name: XStoryCloze (id)
      config: id
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 53.08
  - task:
      type: Sentence completion
    dataset:
      type: Muennighoff/xstory_cloze
      name: XStoryCloze (my)
      config: my
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 51.82
  - task:
      type: Sentence completion
    dataset:
      type: Muennighoff/xstory_cloze
      name: XStoryCloze (ru)
      config: ru
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 49.7
  - task:
      type: Sentence completion
    dataset:
      type: Muennighoff/xstory_cloze
      name: XStoryCloze (sw)
      config: sw
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 54.53
  - task:
      type: Sentence completion
    dataset:
      type: Muennighoff/xstory_cloze
      name: XStoryCloze (te)
      config: te
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 53.67
  - task:
      type: Sentence completion
    dataset:
      type: Muennighoff/xstory_cloze
      name: XStoryCloze (zh)
      config: zh
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 57.78
---

![xmtf](https://github.com/bigscience-workshop/xmtf/blob/master/xmtf_banner.png?raw=true)

#  Table of Contents

1. [Model Summary](#model-summary)
2. [Use](#use)
3. [Limitations](#limitations)
4. [Training](#training)
5. [Evaluation](#evaluation)
7. [Citation](#citation)

# Model Summary

> We present BLOOMZ & mT0, a family of models capable of following human instructions in dozens of languages zero-shot. We finetune BLOOM & mT5 pretrained multilingual language models on our crosslingual task mixture (xP3) and find our resulting models capable of crosslingual generalization to unseen tasks & languages.

- **Repository:** [bigscience-workshop/xmtf](https://github.com/bigscience-workshop/xmtf)
- **Paper:** [Crosslingual Generalization through Multitask Finetuning](https://arxiv.org/abs/2211.01786)
- **Point of Contact:** [Niklas Muennighoff](mailto:niklas@hf.co)
- **Languages:** Refer to [mc4](https://huggingface.co/datasets/mc4) for pretraining & [xP3](https://huggingface.co/datasets/bigscience/xP3) for finetuning language proportions. It understands both pretraining & finetuning languages.
- **BLOOMZ & mT0 Model Family:**

<div class="max-w-full overflow-auto">
<table>
  <tr>
<th colspan="12">Multitask finetuned on <a style="font-weight:bold" href=https://huggingface.co/datasets/bigscience/xP3>xP3</a>. Recommended for prompting in English.
</tr>
<tr>
<td>Parameters</td>
<td>300M</td>
<td>580M</td>
<td>1.2B</td>
<td>3.7B</td>
<td>13B</td>
<td>560M</td>
<td>1.1B</td>
<td>1.7B</td>
<td>3B</td>
<td>7.1B</td>
<td>176B</td>
</tr>
<tr>
<td>Finetuned Model</td>
<td><a href=https://huggingface.co/bigscience/mt0-small>mt0-small</a></td>  
<td><a href=https://huggingface.co/bigscience/mt0-base>mt0-base</a></td>
<td><a href=https://huggingface.co/bigscience/mt0-large>mt0-large</a></td>
<td><a href=https://huggingface.co/bigscience/mt0-xl>mt0-xl</a></td>
<td><a href=https://huggingface.co/bigscience/mt0-xxl>mt0-xxl</a></td>
<td><a href=https://huggingface.co/bigscience/bloomz-560m>bloomz-560m</a></td>
<td><a href=https://huggingface.co/bigscience/bloomz-1b1>bloomz-1b1</a></td>
<td><a href=https://huggingface.co/bigscience/bloomz-1b7>bloomz-1b7</a></td>
<td><a href=https://huggingface.co/bigscience/bloomz-3b>bloomz-3b</a></td>
<td><a href=https://huggingface.co/bigscience/bloomz-7b1>bloomz-7b1</a></td>
<td><a href=https://huggingface.co/bigscience/bloomz>bloomz</a></td>
</tr>
</tr>
  <tr>
<th colspan="12">Multitask finetuned on <a style="font-weight:bold" href=https://huggingface.co/datasets/bigscience/xP3mt>xP3mt</a>. Recommended for prompting in non-English.</th>
</tr>
<tr>
<td>Finetuned Model</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><a href=https://huggingface.co/bigscience/mt0-xxl-mt>mt0-xxl-mt</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><a href=https://huggingface.co/bigscience/bloomz-7b1-mt>bloomz-7b1-mt</a></td>
<td><a href=https://huggingface.co/bigscience/bloomz-mt>bloomz-mt</a></td>
</tr>
<th colspan="12">Multitask finetuned on <a style="font-weight:bold" href=https://huggingface.co/datasets/Muennighoff/P3>P3</a>. Released for research purposes only. Strictly inferior to above models!</th>
</tr>
<tr>
<td>Finetuned Model</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><a href=https://huggingface.co/bigscience/mt0-xxl-p3>mt0-xxl-p3</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><a href=https://huggingface.co/bigscience/bloomz-7b1-p3>bloomz-7b1-p3</a></td>
<td><a href=https://huggingface.co/bigscience/bloomz-p3>bloomz-p3</a></td>
</tr>
<th colspan="12">Original pretrained checkpoints. Not recommended.</th>
<tr>
<td>Pretrained Model</td>
<td><a href=https://huggingface.co/google/mt5-small>mt5-small</a></td>
<td><a href=https://huggingface.co/google/mt5-base>mt5-base</a></td>
<td><a href=https://huggingface.co/google/mt5-large>mt5-large</a></td>
<td><a href=https://huggingface.co/google/mt5-xl>mt5-xl</a></td>
<td><a href=https://huggingface.co/google/mt5-xxl>mt5-xxl</a></td>
<td><a href=https://huggingface.co/bigscience/bloom-560m>bloom-560m</a></td>
<td><a href=https://huggingface.co/bigscience/bloom-1b1>bloom-1b1</a></td>
<td><a href=https://huggingface.co/bigscience/bloom-1b7>bloom-1b7</a></td>
<td><a href=https://huggingface.co/bigscience/bloom-3b>bloom-3b</a></td>
<td><a href=https://huggingface.co/bigscience/bloom-7b1>bloom-7b1</a></td>
<td><a href=https://huggingface.co/bigscience/bloom>bloom</a></td>
</tr>
</table>
</div>


# Use

## Intended use

We recommend using the model to perform tasks expressed in natural language. For example, given the prompt "*Translate to English: Je t’aime.*", the model will most likely answer "*I love you.*". Some prompt ideas from our paper: 
- 一个传奇的开端，一个不灭的神话，这不仅仅是一部电影，而是作为一个走进新时代的标签，永远彪炳史册。你认为这句话的立场是赞扬、中立还是批评?
- Suggest at least five related search terms to "Mạng neural nhân tạo".
- Write a fairy tale about a troll saving a princess from a dangerous dragon. The fairy tale is a masterpiece that has achieved praise worldwide and its moral is "Heroes Come in All Shapes and Sizes". Story (in Spanish):
- Explain in a sentence in Telugu what is backpropagation in neural networks.

**Feel free to share your generations in the Community tab!**

## How to use

### CPU

<details>
<summary> Click to expand </summary>

```python
# pip install -q transformers
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

checkpoint = "bigscience/mt0-small"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

inputs = tokenizer.encode("Translate to English: Je t’aime.", return_tensors="pt")
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```

</details>

### GPU

<details>
<summary> Click to expand </summary>

```python
# pip install -q transformers accelerate
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

checkpoint = "bigscience/mt0-small"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint, torch_dtype="auto", device_map="auto")

inputs = tokenizer.encode("Translate to English: Je t’aime.", return_tensors="pt").to("cuda")
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```

</details>

### GPU in 8bit

<details>
<summary> Click to expand </summary>

```python
# pip install -q transformers accelerate bitsandbytes
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

checkpoint = "bigscience/mt0-small"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint, device_map="auto", load_in_8bit=True)

inputs = tokenizer.encode("Translate to English: Je t’aime.", return_tensors="pt").to("cuda")
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```

</details>

<!-- Necessary for whitespace -->
###

# Limitations

**Prompt Engineering:** The performance may vary depending on the prompt. For BLOOMZ models, we recommend making it very clear when the input stops to avoid the model trying to continue it. For example, the prompt "*Translate to English: Je t'aime*" without the full stop (.) at the end, may result in the model trying to continue the French sentence. Better prompts are e.g. "*Translate to English: Je t'aime.*", "*Translate to English: Je t'aime. Translation:*" "*What is "Je t'aime." in English?*", where it is clear for the model when it should answer. Further, we recommend providing the model as much context as possible. For example, if you want it to answer in Telugu, then tell the model, e.g. "*Explain in a sentence in Telugu what is backpropagation in neural networks.*".

# Training

## Model

- **Architecture:** Same as [mt5-small](https://huggingface.co/google/mt5-small), also refer to the `config.json` file
- **Finetuning steps:** 25000
- **Finetuning tokens:** 4.62 billion
- **Precision:** bfloat16

## Hardware

- **TPUs:** TPUv4-64

## Software

- **Orchestration:** [T5X](https://github.com/google-research/t5x)
- **Neural networks:** [Jax](https://github.com/google/jax)

# Evaluation

We refer to Table 7 from our [paper](https://arxiv.org/abs/2211.01786) & [bigscience/evaluation-results](https://huggingface.co/datasets/bigscience/evaluation-results) for zero-shot results on unseen tasks. The sidebar reports zero-shot performance of the best prompt per dataset config.

# Citation
```bibtex
@article{muennighoff2022crosslingual,
  title={Crosslingual generalization through multitask finetuning},
  author={Muennighoff, Niklas and Wang, Thomas and Sutawika, Lintang and Roberts, Adam and Biderman, Stella and Scao, Teven Le and Bari, M Saiful and Shen, Sheng and Yong, Zheng-Xin and Schoelkopf, Hailey and others},
  journal={arXiv preprint arXiv:2211.01786},
  year={2022}
}
```