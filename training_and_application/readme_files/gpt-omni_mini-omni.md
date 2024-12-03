---
license: mit
language:
- en
base_model: Qwen/Qwen2-0.5B
tags:
- text-to-speech
- speech-to-speech
---


<p align="center"><strong style="font-size: 18px;">
Mini-Omni: Language Models Can Hear, Talk While Thinking in Streaming
</strong>
</p>

<p align="center">
🤗 <a href="">Hugging Face</a>   | 📖 <a href="https://github.com/gpt-omni/mini-omni">Github</a> 
|     📑 <a href="https://arxiv.org/abs/2408.16725">Technical report</a>
</p>

Mini-Omni is an open-source multimodel large language model that can **hear, talk while thinking**. Featuring real-time end-to-end speech input and **streaming audio output** conversational capabilities.

<p align="center">
    <img src="frameworkv3.jpg" width="100%"/>
</p>


## Features

✅ **Real-time speech-to-speech** conversational capabilities. No extra ASR or TTS models required.

✅ **Talking while thinking**, with the ability to generate text and audio at the same time.

✅ **Streaming audio outupt** capabilities.

✅ With "Audio-to-Text" and "Audio-to-Audio" **batch inference** to further boost the performance.

**NOTE**: please refer to the [code repository](https://github.com/gpt-omni/mini-omni) for more details.

## Install

Create a new conda environment and install the required packages:

```sh
conda create -n omni python=3.10
conda activate omni

git clone https://github.com/gpt-omni/mini-omni.git
cd mini-omni
pip install -r requirements.txt
```

## Quick start

**Interactive demo**

- start server
```sh
conda activate omni
cd mini-omni
python3 server.py --ip '0.0.0.0' --port 60808
```

- run streamlit demo

NOTE: you need to run streamlit locally with PyAudio installed.

```sh
pip install PyAudio==0.2.14
API_URL=http://0.0.0.0:60808/chat streamlit run webui/omni_streamlit.py
```

- run gradio demo
```sh
API_URL=http://0.0.0.0:60808/chat python3 webui/omni_gradio.py
```

example:

NOTE: need to unmute first. Gradio seems can not play audio stream instantly, so the latency feels a bit longer.

https://github.com/user-attachments/assets/29187680-4c42-47ff-b352-f0ea333496d9


**Local test**

```sh
conda activate omni
cd mini-omni
# test run the preset audio samples and questions
python inference.py
```

## Acknowledgements 

- [Qwen2](https://github.com/QwenLM/Qwen2/) as the LLM backbone.
- [litGPT](https://github.com/Lightning-AI/litgpt/) for training and inference.
- [whisper](https://github.com/openai/whisper/)  for audio encoding.
- [snac](https://github.com/hubertsiuzdak/snac/)  for audio decoding.
- [CosyVoice](https://github.com/FunAudioLLM/CosyVoice) for generating synthetic speech.
- [OpenOrca](https://huggingface.co/datasets/Open-Orca/OpenOrca) and [MOSS](https://github.com/OpenMOSS/MOSS/tree/main) for alignment.