---
license: cc-by-nc-4.0
language:
- af
- am
- ar
- as
- az
- be
- bn
- bs
- bg
- ca
- cs
- zh
- cy
- da
- de
- el
- en
- et
- fi
- fr
- or
- om
- ga
- gl
- gu
- ha
- he
- hi
- hr
- hu
- hy
- ig
- id
- is
- it
- jv
- ja
- kn
- ka
- kk
- mn
- km
- ky
- ko
- lo
- ln
- lt
- lb
- lg
- lv
- ml
- mr
- mk
- mt
- mi
- my
- nl
- nb
- ne
- ny
- oc
- pa
- ps
- fa
- pl
- pt
- ro
- ru
- sk
- sl
- sn
- sd
- so
- es
- sr
- sv
- sw
- ta
- te
- tg
- tl
- th
- tr
- uk
- ur
- uz
- vi
- wo
- xh
- yo
- ms
- zu
- ary
- arz
- yue
- kea
metrics:
- bleu
- wer
- chrf
inference: False
pipeline_tag: automatic-speech-recognition
tags:
  - audio-to-audio
  - text-to-speech
  - speech-to-text
  - text2text-generation
  - seamless_communication  
library_name: fairseq2
---
# SeamlessM4T Medium

SeamlessM4T is a collection of models designed to provide high quality translation, allowing people from different 
linguistic communities to communicate effortlessly through speech and text. 

SeamlessM4T covers:
- 📥 101 languages for speech input
- ⌨️ 96 Languages for text input/output
- 🗣️ 35 languages for speech output.

-------------------

**🌟 SeamlessM4T v2, an improved version of this version with a novel architecture, has been released [here](https://huggingface.co/facebook/seamless-m4t-v2-large).** 

**This new model improves over SeamlessM4T v1 in quality as well as inference speed in speech generation tasks.**

**SeamlessM4T v2 is also supported by 🤗 Transformers, more on it [in the model card of this new version](https://huggingface.co/facebook/seamless-m4t-v2-large#transformers-usage) or directly in [🤗 Transformers docs](https://huggingface.co/docs/transformers/main/en/model_doc/seamless_m4t_v2).**

-------------------

This is the "medium" variant of SeamlessM4T, which enables multiple tasks without relying on multiple separate models:
- Speech-to-speech translation (S2ST)
- Speech-to-text translation (S2TT)
- Text-to-speech translation (T2ST)
- Text-to-text translation (T2TT)
- Automatic speech recognition (ASR)

## SeamlessM4T models
| Model Name         | #params | checkpoint                                                                              | metrics                                                                              |
| ------------------ | ------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [SeamlessM4T-Large v2](https://huggingface.co/facebook/seamless-m4t-v2-large)  | 2.3B    | [checkpoint](https://huggingface.co/facebook/seamless-m4t-v2-large/blob/main/seamlessM4T_v2_large.pt)   | [metrics](https://dl.fbaipublicfiles.com/seamless/metrics/seamlessM4T_large_v2.zip)  |
| [SeamlessM4T-Large (v1)](https://huggingface.co/facebook/seamless-m4t-large) | 2.3B    | [checkpoint](https://huggingface.co/facebook/seamless-m4t-large/blob/main/multitask_unity_large.pt)   | [metrics](https://dl.fbaipublicfiles.com/seamless/metrics/seamlessM4T_large.zip)  |
| [SeamlessM4T-Medium (v1)](https://huggingface.co/facebook/seamless-m4t-medium) | 1.2B    | [checkpoint](https://huggingface.co/facebook/seamless-m4t-medium/blob/main/multitask_unity_medium.pt) | [metrics](https://dl.fbaipublicfiles.com/seamless/metrics/seamlessM4T_medium.zip) |

We provide extensive evaluation results of SeamlessM4T models in the [SeamlessM4T](https://arxiv.org/abs/2308.11596) and [Seamless](https://arxiv.org/abs/2312.05187) papers (as averages) in the `metrics` files above.

## 🤗 Transformers Usage

 First, load the processor and a checkpoint of the model:

 ```python
import torchaudio
from transformers import AutoProcessor, SeamlessM4TModel
processor = AutoProcessor.from_pretrained("facebook/hf-seamless-m4t-medium")
model = SeamlessM4TModel.from_pretrained("facebook/hf-seamless-m4t-medium")
```

 You can seamlessly use this model on text or on audio, to generated either translated text or translated audio.

 Here is how to use the processor to process text and audio:

 ```python
# Read an audio file and resample to 16kHz:
audio, orig_freq =  torchaudio.load("https://www2.cs.uic.edu/~i101/SoundFiles/preamble10.wav")
audio =  torchaudio.functional.resample(audio, orig_freq=orig_freq, new_freq=16_000) # must be a 16 kHz waveform array
audio_inputs = processor(audios=audio, return_tensors="pt")

# Process some input text as well:
text_inputs = processor(text = "Hello, my dog is cute", src_lang="eng", return_tensors="pt")
```

 ### Speech

Generate speech in Russian from either text (T2ST) or speech input (S2ST):

 ```python
audio_array_from_text = model.generate(**text_inputs, tgt_lang="rus")[0].cpu().numpy().squeeze()
audio_array_from_audio = model.generate(**audio_inputs, tgt_lang="rus")[0].cpu().numpy().squeeze()
```

 ### Text

 Similarly, you can generate translated text from audio files (S2TT) or from text (T2TT, conventionally MT) with the same model. 
 You only have to pass `generate_speech=False` to [`SeamlessM4TModel.generate`](https://huggingface.co/docs/transformers/main/en/model_doc/seamless_m4t#transformers.SeamlessM4TModel.generate).

 ```python 
# from audio
output_tokens = model.generate(**audio_inputs, tgt_lang="fra", generate_speech=False)
translated_text_from_audio = processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)

# from text
output_tokens = model.generate(**text_inputs, tgt_lang="fra", generate_speech=False)
translated_text_from_text = processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)
```

## Seamless_communication
You can also use the seamlessM4T models using the [`seamless_communication` library](https://github.com/facebookresearch/seamless_communication/blob/main/docs/m4t/README.md) 

with either CLI:
```bash
m4t_predict <path_to_input_audio> --task s2st --tgt_lang <tgt_lang> --output_path <path_to_save_audio> --model_name seamlessM4T_medium
```
or a `Translator` API:
```py
import torch
from seamless_communication.inference import Translator

# Initialize a Translator object with a multitask model, vocoder on the GPU.
translator = Translator("seamlessM4T_medium", "vocoder_36langs", torch.device("cuda:0"), torch.float16)
text_output, speech_output = translator.predict(
    input=<path_to_input_audio>,
    task_str="S2ST",
    tgt_lang=<tgt_lang>,
    text_generation_opts=text_generation_opts,
    unit_generation_opts=unit_generation_opts
)
```

## Citation

If you plan to use SeamlessM4T in your work or any models/datasets/artifacts published in SeamlessM4T, please cite:

```bibtex
@article{seamlessm4t2023,
  title={"SeamlessM4T—Massively Multilingual \& Multimodal Machine Translation"},
  author={{Seamless Communication}, Lo\"{i}c Barrault, Yu-An Chung, Mariano Cora Meglioli, David Dale, Ning Dong, Paul-Ambroise Duquenne, Hady Elsahar, Hongyu Gong, Kevin Heffernan, John Hoffman, Christopher Klaiber, Pengwei Li, Daniel Licht, Jean Maillard, Alice Rakotoarison, Kaushik Ram Sadagopan, Guillaume Wenzek, Ethan Ye,  Bapi Akula, Peng-Jen Chen, Naji El Hachem, Brian Ellis, Gabriel Mejia Gonzalez, Justin Haaheim, Prangthip Hansanti, Russ Howes, Bernie Huang, Min-Jae Hwang, Hirofumi Inaguma, Somya Jain, Elahe Kalbassi, Amanda Kallet, Ilia Kulikov, Janice Lam, Daniel Li, Xutai Ma, Ruslan Mavlyutov, Benjamin Peloquin, Mohamed Ramadan, Abinesh Ramakrishnan, Anna Sun, Kevin Tran, Tuan Tran, Igor Tufanov, Vish Vogeti, Carleigh Wood, Yilin Yang, Bokai Yu, Pierre Andrews, Can Balioglu, Marta R. Costa-juss\`{a} \footnotemark[3], Onur \,{C}elebi,Maha Elbayad,Cynthia Gao, Francisco Guzm\'an, Justine Kao, Ann Lee, Alexandre Mourachko, Juan Pino, Sravya Popuri, Christophe Ropers, Safiyyah Saleem, Holger Schwenk, Paden Tomasello, Changhan Wang, Jeff Wang, Skyler Wang},
  journal={ArXiv},
  year={2023}
}
```

## License

The Seamless Communication code and weights are CC-BY-NC 4.0 licensed.
