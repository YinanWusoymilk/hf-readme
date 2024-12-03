---
license: cc-by-nc-sa-4.0
datasets:
- declare-lab/TangoPromptBank
language:
- en
tags:
- music
pipeline_tag: text-to-audio
---
# TANGO: Text to Audio using iNstruction-Guided diffusiOn

**TANGO** is a latent diffusion model for text-to-audio generation. 
**TANGO** can generate realistic audios including human sounds, animal sounds, natural and artificial sounds and sound effects from textual prompts. We use the frozen instruction-tuned LLM Flan-T5 as the text encoder and train a UNet based diffusion model for audio generation. We outperform current state-of-the-art models for audio generation across both objective and subjective metrics. We release our model, training, inference code and pre-trained checkpoints for the research community.

📣 We recently released **Tango 2**. Access it [here](https://huggingface.co/declare-lab/tango2).

📣 We are releasing **Tango-Full** which was pre-trained on **TangoPromptBank**.

## Code

Our code is released here: [https://github.com/declare-lab/tango](https://github.com/declare-lab/tango)

We uploaded several **TANGO** generated samples here: [https://tango-web.github.io/](https://tango-web.github.io/)

Please follow the instructions in the repository for installation, usage and experiments.

## Quickstart Guide

Download the **TANGO** model and generate audio from a text prompt:

```python
import IPython
import soundfile as sf
from tango import Tango

tango = Tango("declare-lab/tango-full-ft-audiocaps")

prompt = "An audience cheering and clapping"
audio = tango.generate(prompt)
sf.write(f"{prompt}.wav", audio, samplerate=16000)
IPython.display.Audio(data=audio, rate=16000)
```
[An audience cheering and clapping.webm](https://user-images.githubusercontent.com/13917097/233851915-e702524d-cd35-43f7-93e0-86ea579231a7.webm)

The model will be automatically downloaded and saved in cache. Subsequent runs will load the model directly from cache.

The `generate` function uses 100 steps by default to sample from the latent diffusion model. We recommend using 200 steps for generating better quality audios. This comes at the cost of increased run-time.

```python
prompt = "Rolling thunder with lightning strikes"
audio = tango.generate(prompt, steps=200)
IPython.display.Audio(data=audio, rate=16000)
```
[Rolling thunder with lightning strikes.webm](https://user-images.githubusercontent.com/13917097/233851929-90501e41-911d-453f-a00b-b215743365b4.webm)

<!-- [MachineClicking](https://user-images.githubusercontent.com/25340239/233857834-bfda52b4-4fcc-48de-b47a-6a6ddcb3671b.mp4 "sample 1") -->

Use the `generate_for_batch` function to generate multiple audio samples for a batch of text prompts:

```python
prompts = [
    "A car engine revving",
    "A dog barks and rustles with some clicking",
    "Water flowing and trickling"
]
audios = tango.generate_for_batch(prompts, samples=2)
```
This will generate two samples for each of the three text prompts.