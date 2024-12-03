---
license: apache-2.0
---



# Model

## TL;DR

CLAP is to audio what CLIP is to image. This is an improved CLAP checkpoint, specifically trained on general audio, music and speech.

## Description

CLAP (Contrastive Language-Audio Pretraining) is a neural network trained on a variety of (audio, text) pairs. It can be instructed in to predict the most relevant text snippet, given an audio, without directly optimizing for the task. The CLAP model uses a SWINTransformer to get audio features from a log-Mel spectrogram input, and a RoBERTa model to get text features. Both the text and audio features are then projected to a latent space with identical dimension. The dot product between the projected audio and text features is then used as a similar score.


# Usage

You can use this model for zero shot audio classification or extracting audio and/or textual features.

# Uses

## Perform zero-shot audio classification

### Using `pipeline`

```python
from datasets import load_dataset
from transformers import pipeline

dataset = load_dataset("ashraq/esc50")
audio = dataset["train"]["audio"][-1]["array"]

audio_classifier = pipeline(task="zero-shot-audio-classification", model="laion/larger_clap_general")
output = audio_classifier(audio, candidate_labels=["Sound of a dog", "Sound of vaccum cleaner"])
print(output)
>>> [{"score": 0.999, "label": "Sound of a dog"}, {"score": 0.001, "label": "Sound of vaccum cleaner"}]
```

## Run the model:

You can also get the audio and text embeddings using `ClapModel`

### Run the model on CPU:

```python
from datasets import load_dataset
from transformers import ClapModel, ClapProcessor

librispeech_dummy = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
audio_sample = librispeech_dummy[0]

model = ClapModel.from_pretrained("laion/larger_clap_general")
processor = ClapProcessor.from_pretrained("laion/larger_clap_general")

inputs = processor(audios=audio_sample["audio"]["array"], return_tensors="pt")
audio_embed = model.get_audio_features(**inputs)
```

### Run the model on GPU:

```python
from datasets import load_dataset
from transformers import ClapModel, ClapProcessor

librispeech_dummy = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
audio_sample = librispeech_dummy[0]

model = ClapModel.from_pretrained("laion/larger_clap_general").to(0)
processor = ClapProcessor.from_pretrained("laion/larger_clap_general")

inputs = processor(audios=audio_sample["audio"]["array"], return_tensors="pt").to(0)
audio_embed = model.get_audio_features(**inputs)
```


# Citation

If you are using this model for your work, please consider citing the original paper:
```
@misc{https://doi.org/10.48550/arxiv.2211.06687,
  doi = {10.48550/ARXIV.2211.06687},
  url = {https://arxiv.org/abs/2211.06687},
  author = {Wu, Yusong and Chen, Ke and Zhang, Tianyu and Hui, Yuchen and Berg-Kirkpatrick, Taylor and Dubnov, Shlomo},
  keywords = {Sound (cs.SD), Audio and Speech Processing (eess.AS), FOS: Computer and information sciences, FOS: Computer and information sciences, FOS: Electrical engineering, electronic engineering, information engineering, FOS: Electrical engineering, electronic engineering, information engineering},
  title = {Large-scale Contrastive Language-Audio Pretraining with Feature Fusion and Keyword-to-Caption Augmentation},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

