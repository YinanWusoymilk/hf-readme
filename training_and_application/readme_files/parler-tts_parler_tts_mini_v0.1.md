---
library_name: transformers
tags:
- text-to-speech
- annotation
license: apache-2.0
language:
- en
pipeline_tag: text-to-speech
inference: false
datasets:
  - parler-tts/mls_eng_10k
  - blabble-io/libritts_r
  - parler-tts/libritts_r_tags_tagged_10k_generated
  - parler-tts/mls-eng-10k-tags_tagged_10k_generated
---

<img src="https://huggingface.co/datasets/parler-tts/images/resolve/main/thumbnail.png" alt="Parler Logo" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>


# Parler-TTS Mini v0.1

<a target="_blank" href="https://huggingface.co/spaces/parler-tts/parler_tts_mini">
  <img src="https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm.svg" alt="Open in HuggingFace"/>
</a>

* **Fine-tuning guide on Colab:**

<a target="_blank" href="https://colab.research.google.com/github/ylacombe/scripts_and_notebooks/blob/main/Finetuning_Parler_TTS_on_a_single_speaker_dataset.ipynb"> 
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> 
</a>

**Parler-TTS Mini v0.1** is a lightweight text-to-speech (TTS) model, trained on 10.5K hours of audio data, that can generate high-quality, natural sounding speech with features that can be controlled using a simple text prompt (e.g. gender, background noise, speaking rate, pitch and reverberation).
It is the first release model from the [Parler-TTS](https://github.com/huggingface/parler-tts) project, which aims to provide the community with TTS training resources and dataset pre-processing code.

## Usage

Using Parler-TTS is as simple as "bonjour". Simply install the library once:

```sh
pip install git+https://github.com/huggingface/parler-tts.git
```

You can then use the model with the following inference snippet:

```py
import torch
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
import soundfile as sf

device = "cuda:0" if torch.cuda.is_available() else "cpu"

model = ParlerTTSForConditionalGeneration.from_pretrained("parler-tts/parler_tts_mini_v0.1").to(device)
tokenizer = AutoTokenizer.from_pretrained("parler-tts/parler_tts_mini_v0.1")

prompt = "Hey, how are you doing today?"
description = "A female speaker with a slightly low-pitched voice delivers her words quite expressively, in a very confined sounding environment with clear audio quality. She speaks very fast."

input_ids = tokenizer(description, return_tensors="pt").input_ids.to(device)
prompt_input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)

generation = model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
audio_arr = generation.cpu().numpy().squeeze()
sf.write("parler_tts_out.wav", audio_arr, model.config.sampling_rate)
```

**Tips**:
* Include the term "very clear audio" to generate the highest quality audio, and "very noisy audio" for high levels of background noise
* Punctuation can be used to control the prosody of the generations, e.g. use commas to add small breaks in speech
* The remaining speech features (gender, speaking rate, pitch and reverberation) can be controlled directly through the prompt

## Motivation

Parler-TTS is a reproduction of work from the paper [Natural language guidance of high-fidelity text-to-speech with synthetic annotations](https://www.text-description-to-speech.com) by Dan Lyth and Simon King, from Stability AI and Edinburgh University respectively. 

Contrarily to other TTS models, Parler-TTS is a **fully open-source** release. All of the datasets, pre-processing, training code and weights are released publicly under permissive license, enabling the community to build on our work and develop their own powerful TTS models.
Parler-TTS was released alongside:
* [The Parler-TTS repository](https://github.com/huggingface/parler-tts) - you can train and fine-tuned your own version of the model.
* [The Data-Speech repository](https://github.com/huggingface/dataspeech) - a suite of utility scripts designed to annotate speech datasets.
* [The Parler-TTS organization](https://huggingface.co/parler-tts) - where you can find the annotated datasets as well as the future checkpoints.

## Citation

If you found this repository useful, please consider citing this work and also the original Stability AI paper:

```
@misc{lacombe-etal-2024-parler-tts,
  author = {Yoach Lacombe and Vaibhav Srivastav and Sanchit Gandhi},
  title = {Parler-TTS},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/huggingface/parler-tts}}
}
```

```
@misc{lyth2024natural,
      title={Natural language guidance of high-fidelity text-to-speech with synthetic annotations},
      author={Dan Lyth and Simon King},
      year={2024},
      eprint={2402.01912},
      archivePrefix={arXiv},
      primaryClass={cs.SD}
}
```

## License

This model is permissively licensed under the Apache 2.0 license.
