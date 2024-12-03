---
license: mpl-2.0
datasets:
- mozilla-foundation/common_voice_17_0
base_model:
- meta-llama/Llama-3.1-8B-Instruct
---
# Model Card for Diva Llama 3

<!-- Provide a quick summary of what the model is/does. [Optional] -->
This is an end-to-end Voice Assistant Model which can handle speech and text as inputs. It is trained using distillation loss. More details in the [pre-print](https://arxiv.org/abs/2410.02678) here.

See the model in action at [diva-audio.github.io](https://diva-audio.github.io) or look at the full training logs on [Weights&Biases](https://wandb.ai/i18nlp/DiVA%20Training%20Runs/runs/gqpwnd99?nw=nwuserheld).

## Citation
**BibTeX:**

```
@misc{DiVA,
      title={{D}istilling an {E}nd-to-{E}nd {V}oice {A}ssistant {W}ithout {I}nstruction {T}raining {D}ata}, 
      author={William Held and Ella Li and Michael Ryan and Weiyan Shi and Yanzhe Zhang and Diyi Yang},
      year={2024},
      eprint={2410.02678},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.02678}, 
}
    
```

### Inference Example
```python
from transformers import AutoModel
import librosa
import wget
from modeling_diva import DiVAModel

filename = wget.download(
    "https://github.com/ffaisal93/SD-QA/raw/refs/heads/master/dev/eng/irl/wav_eng/-1008642825401516622.wav"
)

speech_data, _ = librosa.load(filename, sr=16_000)

model = AutoModel.from_pretrained("WillHeld/DiVA-llama-3-v0-8b", trust_remote_code=True)

print(model.generate([speech_data]))
print(model.generate([speech_data], ["Reply Briefly Like A Pirate"]))

filename = wget.download(
    "https://github.com/ffaisal93/SD-QA/raw/refs/heads/master/dev/eng/irl/wav_eng/-2426554427049983479.wav"
)

speech_data2, _ = librosa.load(filename, sr=16_000)

print(
    model.generate(
        [speech_data, speech_data2],
        ["Reply Briefly Like A Pirate", "Reply Briefly Like A New Yorker"],
    )
)
```

##  Table of Contents

- [Model Card for DiVA Llama 3](#model-card-for-DiVA-Llama-3)
- [Citation](#citation)
- [Table of Contents](#table-of-contents)
- [Training Details](#training-details)
  - [Training Data](#training-data)
  - [Training Procedure](#training-procedure)
- [Environmental Impact](#environmental-impact)
- [Technical Specifications [optional]](#technical-specifications-optional)
  - [Model Architecture and Objective](#model-architecture-and-objective)
  - [Compute Infrastructure](#compute-infrastructure)
    - [Hardware](#hardware)
    - [Software](#software)
- [Model Card Contact](#model-card-contact)

## Training Details

### Training Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

This model was trained on the [CommonVoice](https://huggingface.co/datasets/mozilla-foundation/common_voice_16_1) corpus.


### Training Procedure

This model was trained for 7k gradient steps with a batch size of 512 Recordings and a linearly decaying learning rate from 5e-5 to zero, with a linear warmup of 70 steps.

### Environmental Impact

- **Hardware Type:** V4-256 TPU
- **Hours used:** 11 Hours
- **Cloud Provider:** Google Cloud.
- **Compute Region:** US Central C


### Hardware

This model was trained on at V4-256 TPU on Google Cloud.

### Software

This model was trained with [Levanter](https://github.com/stanford-crfm/levanter) 


## Model Card Authors [optional]

<!-- This section provides another layer of transparency and accountability. Whose views is this model card representing? How many voices were included in its construction? Etc. -->

Will Held

## Model Card Contact

held@stanford.edu
