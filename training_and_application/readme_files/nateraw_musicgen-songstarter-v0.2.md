---
pipeline_tag: text-to-audio
library_name: audiocraft
language: en
tags:
- text-to-audio
- musicgen
- songstarter
license: cc-by-nc-4.0
---

# Model Card for musicgen-songstarter-v0.2

[![Replicate demo and cloud API](https://replicate.com/nateraw/musicgen-songstarter-v0.2/badge)](https://replicate.com/nateraw/musicgen-songstarter-v0.2) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/nateraw/0cb4c242b70af10044e9ae73f4617c86/songstarter-v0-2-demo.ipynb) [![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/nateraw/singing-songstarter)

musicgen-songstarter-v0.2 is a [`musicgen-stereo-melody-large`](https://huggingface.co/facebook/musicgen-stereo-melody-large) fine-tuned on a dataset of melody loops from my Splice sample library. It's intended to be used to generate song ideas that are useful for music producers. It generates stereo audio in 32khz.

**👀 Update:** I wrote a [blogpost](https://nateraw.com/posts/training_musicgen_songstarter.html) detailing how and why I trained this model, including training details, the dataset, Weights and Biases logs, etc.

Compared to [`musicgen-songstarter-v0.1`](https://huggingface.co/nateraw/musicgen-songstarter-v0.1), this new version:
- was trained on 3x more unique, manually-curated samples that I painstakingly purchased on Splice
- Is twice the size, bumped up from size `medium` ➡️ `large` transformer LM

If you find this model interesting, please consider:
  - following me on [GitHub](https://github.com/nateraw)
  - following me on [Twitter](https://twitter.com/_nateraw)

## Usage

Install [audiocraft](https://github.com/facebookresearch/audiocraft):

```
pip install -U git+https://github.com/facebookresearch/audiocraft#egg=audiocraft
```

Then, you should be able to load this model just like any other musicgen checkpoint here on the Hub:

```python
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

model = MusicGen.get_pretrained('nateraw/musicgen-songstarter-v0.2')
model.set_generation_params(duration=8)  # generate 8 seconds.
wav = model.generate_unconditional(4)    # generates 4 unconditional audio samples
descriptions = ['acoustic, guitar, melody, trap, d minor, 90 bpm'] * 3
wav = model.generate(descriptions)  # generates 3 samples.

melody, sr = torchaudio.load('./assets/bach.mp3')
# generates using the melody from the given audio and the provided descriptions.
wav = model.generate_with_chroma(descriptions, melody[None].expand(3, -1, -1), sr)

for idx, one_wav in enumerate(wav):
    # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
    audio_write(f'{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)
```

## Prompt Format

Follow the following prompt format:

```
{tag_1}, {tag_2}, ..., {tag_n}, {key}, {bpm} bpm
```

For example:

```
hip hop, soul, piano, chords, jazz, neo jazz, G# minor, 140 bpm
```

For some example tags, [see the prompt format section of musicgen-songstarter-v0.1's readme](https://huggingface.co/nateraw/musicgen-songstarter-v0.1#prompt-format). The tags there are for the smaller v1 dataset, but should give you an idea of what the model saw.

## Samples

<table style="width:100%; text-align:center;">
  <tr>
    <th>Audio Prompt</th>
    <th>Text Prompt</th>
    <th>Output</th>
  </tr>
  <tr>
    <td>
      <audio controls>
        <source src="https://huggingface.co/nateraw/musicgen-songstarter-v0.2/resolve/main/assets/kalhonaho.wav?download=true" type="audio/wav">
        Your browser does not support the audio element.
      </audio>
    </td>
    <td>
      trap, synthesizer, songstarters, dark, G# minor, 140 bpm
    </td>
    <td>
      <audio controls>
        <source src="https://huggingface.co/nateraw/musicgen-songstarter-v0.2/resolve/main/assets/kalhonaho_trap.wav?download=true" type="audio/wav">
        Your browser does not support the audio element.
      </audio>
    </td>
  </tr>
  <tr>
    <td>
      <audio controls>
        <source src="https://huggingface.co/nateraw/musicgen-songstarter-v0.2/resolve/main/assets/bach.mp3?download=true" type="audio/mp3">
        Your browser does not support the audio element.
      </audio>
    </td>
    <td>
      acoustic, guitar, melody, trap, D minor, 90 bpm
    </td>
    <td>
      <audio controls>
        <source src="https://huggingface.co/nateraw/musicgen-songstarter-v0.2/resolve/main/assets/bach_guitar.wav?download=true" type="audio/wav">
        Your browser does not support the audio element.
      </audio>
    </td>
  </tr>
</table>

## Training Details

For more verbose details, you can check out the [blogpost](https://nateraw.com/posts/training_musicgen_songstarter.html#training).

- **code**:
  - Repo is [here](https://github.com/nateraw/audiocraft). It's an undocumented fork of [facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft) where I rewrote the training loop with PyTorch Lightning, which worked a bit better for me.
- **data**:
  - around 1700-1800 samples I manually listened to + purchased via my personal [Splice](https://splice.com) account. About 7-8 hours of audio.
  - Given the licensing terms, I cannot share the data.
- **hardware**:
  - 8xA100 40GB instance from Lambda Labs
- **procedure**:
  - trained for 10k steps, which took about 6 hours
  - reduced segment duration at train time to 15 seconds
- **hparams/logs**:
  - See the wandb [run](https://wandb.ai/nateraw/musicgen-songstarter-v0.2/runs/63gh4l7m), which includes training metrics, logs, hardware metrics at train time, hyperparameters, and the exact command I used when I ran the training script.

## Acknowledgements

This work would not have been possible without:

- [Lambda Labs](https://lambdalabs.com/), for subsidizing larger training runs by providing some compute credits
- [Replicate](https://replicate.com/), for early development compute resources

Thank you ❤️
