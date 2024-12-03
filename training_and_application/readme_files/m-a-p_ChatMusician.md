---
license: mit
language:
- en
metrics:
- accuracy
pipeline_tag: text-generation
---
# 🎼 ChatMusician: Understanding and Generating Music Intrinsically with LLM

[**🌐 DemoPage**](https://ezmonyi.github.io/ChatMusician/) | [**🤗Pretrain Dataset**](https://huggingface.co/datasets/m-a-p/MusicPile) | [**🤗SFT Dataset**](https://huggingface.co/datasets/m-a-p/MusicPile-sft) | [**🤗 Benchmark**](https://huggingface.co/datasets/m-a-p/MusicTheoryBench) | [**📖 arXiv**](http://arxiv.org/abs/2402.16153) | [💻 **Code**](https://github.com/hf-lin/ChatMusician) | [**🤖 Base Model**](https://huggingface.co/m-a-p/ChatMusician-Base)

## 🔔News
- **🔥[2024-2-28]: The release of ChatMusician's demo, code, model, data, and benchmark. 😆**
- [2024-2-28]: ChatMusician uses a fast symbolic music processing and rendering library, `symusic`. Developed by Yikai-Liao, lzqlzzq and Natooz. Find the project on Github: https://github.com/Yikai-Liao/symusic
- [2023-11-30]: Checkout another awesome project [MMMU](https://huggingface.co/datasets/MMMU/MMMU/) that includes multimodal music reasoning.

## Introduction

While Large Language Models (LLMs) demonstrate impressive capabilities in text generation,
we find that their ability has yet to be generalized to music, humanity’s creative language.
We introduce **ChatMusician**, **an open-source LLM that integrates intrinsic musical abilities**.

It is based on continual pre-training and finetuning LLaMA2 on a text-compatible music representation, ABC notation, and the music is treated as a second language. ChatMusician can understand and generate music with a pure text tokenizer without any external multi-modal neural structures or tokenizers. Interestingly, endowing musical abilities does not harm language abilities, even achieving a slightly higher MMLU score. Our model is capable of composing well-structured, full-length music, conditioned on texts, chords, melodies, motifs, musical forms, etc, surpassing GPT-4 baseline. On our meticulously curated college-level music understanding benchmark, MusicTheoryBench, ChatMusician surpasses LLaMA2 and GPT-3.5 on zero-shot setting by a noticeable
margin. Our work reveals that LLMs can be an excellent compressor for music, but there remains significant territory to be conquered. Code, data, model, and benchmark are open-sourced. 

<!-- <audio controls src="https://cdn-uploads.huggingface.co/production/uploads/5fd6f670053c8345eddc1b68/8NSONUjIF7KGUCfwzPCd9.mpga"></audio> -->

[![Demo Video](chatmusician_demo.png)](https://youtu.be/zt3l49K55Io)
<!-- [![ChatMusician Introduction](http://img.youtube.com/vi/zt3l49K55Io/0.jpg))](http://www.youtube.com/watch?v=zt3l49K55Io "ChatMusician Introduction") -->
<!-- <iframe width="787" height="528" src="https://www.youtube.com/embed/zt3l49K55Io" title="ChatMusician: Fostering Intrinsic Musical Abilities Into LLM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Usage

You can use the models through Huggingface's Transformers library. Check our Github repo for more advanced use: [https://github.com/hf-lin/ChatMusician](https://github.com/hf-lin/ChatMusician) -->

## CLI demo
```python
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
import torch
import torchaudio
import re
from string import Template
prompt_template = Template("Human: ${inst} </s> Assistant: ")

tokenizer = AutoTokenizer.from_pretrained("m-a-p/ChatMusician", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("m-a-p/ChatMusician", torch_dtype=torch.float16, device_map="cuda", resume_download=True).eval()

generation_config = GenerationConfig(
    temperature=0.2,
    top_k=40,
    top_p=0.9,
    do_sample=True,
    num_beams=1,
    repetition_penalty=1.1,
    min_new_tokens=10,
    max_new_tokens=1536
)

instruction = """Develop a musical piece using the given chord progression.
'Dm', 'C', 'Dm', 'Dm', 'C', 'Dm', 'C', 'Dm'
"""

prompt = prompt_template.safe_substitute({"inst": instruction})
inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
response = model.generate(
        input_ids=inputs["input_ids"].to(model.device),
        attention_mask=inputs['attention_mask'].to(model.device),
        eos_token_id=tokenizer.eos_token_id,
        generation_config=generation_config,
        )
response = tokenizer.decode(response[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
print(response)

# to render abc notation, you need to install symusic
# pip install symusic
from symusic import Score, Synthesizer, BuiltInSF3, dump_wav

abc_pattern = r'(X:\d+\n(?:[^\n]*\n)+)'
abc_notation = re.findall(abc_pattern, response+'\n')[0]
s = Score.from_abc(abc_notation)
audio = Synthesizer().render(s, stereo=True)
torchaudio.save('cm_music_piece.wav', torch.FloatTensor(audio), 44100)
```

## Chat demo
ChatMusician supports gradio web demo and multi-turn dialogue, please visit our [github](https://github.com/hf-lin/ChatMusician) for more details.
Our web demo also supports rendering ABC scores into images.

## Limitations
- The model currently only supports strict format and close-ended instructions for the music tasks. If we have more funding, we plan to create a more diverse multi-turn music instruction chat data for better generalization.
- The model suffers from hallucinations, and shouldn't be used for music education. It could be improved by feeding more music textbooks, blogs, etc. And RLHF may help, too.
- A large portion of the training data is in the style of Irish music. If possible, the community should develop a converter between performance midi and ABC scores, so that we can include more established midi datasets.
- The MusicThoeryBench results reported in the paper are obtained with perplexity mode. Direct generation may result in a worse performance.
- We observe that using the current version of training data, ChatMusician presents a weak in-context-learning and chain-of-thoughts ability. The community should work on improving the music data quality. 

## Example Stable Prompts
We provide some of the prompts that are tested to be stable. For more prompts, please check 🤗 [MusicPile](https://huggingface.co/datasets/m-a-p/MusicPile).

### Function: Chord Conditioned Music Generation
```
Develop a musical piece using the given chord progression.
'Dm', 'C', 'Dm', 'Dm', 'C', 'Dm', 'C', 'Dm'
```

### Function: Text2music
```
Develop a tune influenced by Bach's compositions.
```
```
Using ABC notation, recreate the given text as a musical score.
Meter C
Notes The parts are commonly interchanged.
Transcription 1997 by John Chambers
Key D
Note Length 1/8
Rhythm reel
```

### Function: Melody Harmonization

```
Construct smooth-flowing chord progressions for the supplied music.

|: BA | G2 g2"^(C)" edeg | B2 BA"^(D7)" BcBA | G2 g2 edeg | dBAG A2 BA |
G2 g2"^(C)" edeg | B2 BA B2 d2 | e2 ef e2 (3def | gedB A2 :: BA | G2 BG dGBe |
dBBA"^(D7)" B3 A | G2 BG dGBe | dBAG A4 | G2 BG dGBe | dBBA B3 d |
e2 ef e2 (3def | gedB A2 :|
```
```
Develop a series of chord pairings that amplify the harmonious elements in the given music piece.

E |: EAA ABc | Bee e2 d | cBA ABc | BEE E2 D | EAA ABc | Bee e2 d |
cBA ^GAB |1 A2 A A2 E :|2 A2 A GAB || c3 cdc | Bgg g2 ^g | aed cBA |
^GAB E^F^G | A^GA BAB | cde fed | cBA ^GAB |1 A2 A GAB :|2 \n A3 A2 ||
```

### Function: Musical Form Conditioned Music Generation

```
Develop a composition by incorporating elements from the given melodic structure.

Ternary, Sectional: Verse/Chorus/Bridge
```

### Function: Motif and Form Conditioned Music Generation

```
Create music by following the alphabetic representation of the assigned musical structure and the given motif.

Musical Form Input: AB

ABC Notation Music Input:
X:1
L:1/8
M:2/4
K:D
['d>ef>d g>ef>c d>ef>d c2 e2 d>ef>d g>ef>d', '(3(Ace) (3(Ace)']
```

### Function: Music Understanding

```
Investigate the aspects of this musical work and convey its structural organization using suitable musical words.

X:1
L:1/8
M:2/2
K:G
G2 dG BGdG | G2 dc BAGB | A2 eA cAeA | A2 ed cAFA | 
G2 dG BGdG | G2 dc BAGB | ABcd efge |1 aged cAFA :|2 
aged ^cdef |: g3 f g2 ef | gedc BA G2 | eaag agea | 
aged ^cdef | g3 f g2 ef |gedc BAGB | ABcd efge |1 
aged ^cdef :|2 aged cAFA |:"^variations:" G2 BG dGBA | 
G2 dG BAGB | A2 cA eAcA | A2 ed cAFA | G2 BG dGBA | 
G2 dc BAGB | ABcd efge |1 aged cAFA :|2 aged ^cdef |:
g2 af g2 ef | gedc BAGB | Aaag ageg | aged ^cdef | 
gbaf g2 ef | gedc BAGB | ABcd efge |1
aged ^cdef :|2 aged cAFA ||
```

```
Analyze the musical work and pinpoint the consistent melodic element in every section.

X:1
L:1/8
M:4/4
K:G
ge | d2 G2 cBAG | d2 G2 cBAG | e2 A2 ABcd | edcB A2 Bc |
d2 cB g2 fe | edcB cBAG | BAGE DEGA | B2 G2 G2 :: ga |
b2 gb a2 fa | g2 eg edcB | e2 A2 ABcd | edcB A2 ga |
b2 gb a2 fa | g2 eg edcB | cBAG DEGA | B2 G2 G2 :|
```

## Training Data

ChatMusician is pretrained on the 🤗 [MusicPile](https://huggingface.co/datasets/m-a-p/MusicPile), which is the first pretraining corpus for **developing musical abilities** in large language models. Check out the dataset card for more details.
And supervised finetuned on 1.1M samples(2:1 ratio between music scores
and music knowledge & music summary data) from MusicPile. Check our [paper](http://arxiv.org/abs/2402.16153) for more details.


## Evaluation

1. Music understanding abilities are evaluated on the [MusicTheoryBench](https://huggingface.co/datasets/m-a-p/MusicTheoryBench). The following figure is zero-shot accuracy on MusicTheoryBench.
We included GPT-3.5, GPT-4, LLaMA2-7B-Base, ChatMusician-Base, and ChatMusician. The blue bar represents the performance on the music knowledge metric, and the red bar represents the music reasoning metric. The dashed line corresponds to a random baseline, with a score of 25%.
<!-- ![MusicTheoryBench_result](./MusicTheoryBench_result_plt.png) -->
<img src="./MusicTheoryBench_result_plt.png" alt="drawing" width="800"/>
3. General language abilities of ChatMusician are evaluated on the [Massive Multitask Language Understanding (MMLU) dataset](https://huggingface.co/datasets/lukaemon/mmlu).




## Citation
If you find our work helpful, feel free to give us a cite.
```
@misc{yuan2024chatmusician,
      title={ChatMusician: Understanding and Generating Music Intrinsically with LLM}, 
      author={Ruibin Yuan and Hanfeng Lin and Yi Wang and Zeyue Tian and Shangda Wu and Tianhao Shen and Ge Zhang and Yuhang Wu and Cong Liu and Ziya Zhou and Ziyang Ma and Liumeng Xue and Ziyu Wang and Qin Liu and Tianyu Zheng and Yizhi Li and Yinghao Ma and Yiming Liang and Xiaowei Chi and Ruibo Liu and Zili Wang and Pengfei Li and Jingcheng Wu and Chenghua Lin and Qifeng Liu and Tao Jiang and Wenhao Huang and Wenhu Chen and Emmanouil Benetos and Jie Fu and Gus Xia and Roger Dannenberg and Wei Xue and Shiyin Kang and Yike Guo},
      year={2024},
      eprint={2402.16153},
      archivePrefix={arXiv},
      primaryClass={cs.SD}
}
```