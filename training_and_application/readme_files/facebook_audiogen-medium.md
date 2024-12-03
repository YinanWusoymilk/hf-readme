---
license: cc-by-nc-4.0
tags:
- audiocraft
- audiogen
---

# AudioGen - Medium - 1.5B

AudioGen is an autoregressive transformer LM that synthesizes general audio conditioned on text (Text-to-Audio). 
Internally, AudioGen operates over discrete representations learnt from the raw waveform, using an EnCodec tokenizer.

AudioGen was presented at [AudioGen: Textually Guided Audio Generation](https://arxiv.org/abs/2209.15352) by *Felix Kreuk, Gabriel Synnaeve, Adam Polyak, Uriel Singer, Alexandre Défossez, Jade Copet, Devi Parikh, Yaniv Taigman, Yossi Adi*.

AudioGen 1.5B is a variant of the original AudioGen model that follows [MusicGen](https://arxiv.org/abs/2306.05284) architecture. 
More specifically, it is trained over a 16kHz EnCodec tokenizer with 4 codebooks sampled at 50 Hz with a delay pattern between the codebooks. 
Having only 50 auto-regressive steps per second of audio, this AudioGen model allows faster generation while reaching similar performances to the original AudioGen model introduced in the paper.

## Audiocraft Usage

You can run AudioGen locally through the original [Audiocraft library]((https://github.com/facebookresearch/audiocraft):

1. First install the [`audiocraft` library](https://github.com/facebookresearch/audiocraft)
```
pip install git+https://github.com/facebookresearch/audiocraft.git
```

2. Make sure to have [`ffmpeg`](https://ffmpeg.org/download.html) installed:
```
apt get install ffmpeg
```

3. Run the following Python code:

```py
import torchaudio
from audiocraft.models import AudioGen
from audiocraft.data.audio import audio_write

model = AudioGen.get_pretrained('facebook/audiogen-medium')
model.set_generation_params(duration=5)  # generate 5 seconds.
descriptions = ['dog barking', 'sirenes of an emergency vehicule', 'footsteps in a corridor']
wav = model.generate(descriptions)  # generates 3 samples.

for idx, one_wav in enumerate(wav):
    # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
    audio_write(f'{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)
```

## Model details

See [AudioGen's model card](https://github.com/facebookresearch/audiocraft/blob/main/model_cards/AUDIOGEN_MODEL_CARD.md).