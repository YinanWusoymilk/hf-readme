---
license: cc-by-4.0
library_name: transformers
tags:
- mimi
- audio
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/62611fcabbcbd1c34f1615f6/QPpyznxSH5CxjJ_mA0rdg.png)

# Model Card for Mimi

Mimi codec is a state-of-the-art audio neural codec, developped by [Kyutai](https://kyutai.org/), that combines semantic and acoustic information into audio tokens running at 12Hz and a bitrate of 1.1kbps.

## Model Details

### Model Description

Mimi is a high-fidelity audio codec leveraging neural networks. It introduces a streaming encoder-decoder architecture with quantized latent space, trained in an end-to-end fashion. 

It was trained on speech data, which makes it particularly adapted to train speech language models or text-to-speech systems.

- **Developed by:**  Kyutai
- **Model type:** Audio codec
- **Audio types:** Speech
- **License:** CC-BY

### Model Sources 


- **Repository:** [repo](https://github.com/kyutai-labs/moshi) 
- **Paper:** [paper](http://kyutai.org/Moshi.pdf) 
- **Demo:** [demo](https://moshi.chat/) 

## Uses


## How to Get Started with the Model

### Usage with `transformers`

Use the following code to get started with the Mimi model using a dummy example from the LibriSpeech dataset (~9MB). First, install the required Python packages:

```
pip install --upgrade pip
pip install --upgrade datasets[audio]
pip install git+https://github.com/huggingface/transformers.git@main
```

Then load an audio sample, and run a forward pass of the model:

```python
from datasets import load_dataset, Audio
from transformers import MimiModel, AutoFeatureExtractor

# load a demonstration datasets
librispeech_dummy = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")

# load the model + feature extractor (for pre-processing the audio)
model = MimiModel.from_pretrained("kyutai/mimi")
feature_extractor = AutoFeatureExtractor.from_pretrained("kyutai/mimi")

# cast the audio data to the correct sampling rate for the model
librispeech_dummy = librispeech_dummy.cast_column("audio", Audio(sampling_rate=feature_extractor.sampling_rate))
audio_sample = librispeech_dummy[0]["audio"]["array"]

# pre-process the inputs
inputs = feature_extractor(raw_audio=audio_sample, sampling_rate=feature_extractor.sampling_rate, return_tensors="pt")

# explicitly encode then decode the audio inputs
encoder_outputs = model.encode(inputs["input_values"])
audio_values = model.decode(encoder_outputs.audio_codes)[0]

# or the equivalent with a forward pass
audio_values = model(inputs["input_values"]).audio_values
```

### Usage with Moshi

See the main [README](https://github.com/kyutai-labs/moshi) file.

### Direct Use

Mimi can be used directly as an audio codec for real-time compression and decompression of speech signals. 
It provides high-quality audio compression and efficient decoding.

### Out-of-Scope Use

The model is not intended to be used to impersonate other people or any malicious use of any kind. 

## Bias, Risks, and Limitations

The model has been trained with a few safeguards to try to limit potential toxic usages, however our toxicity analysis shows that it behaves in the middle of existing models with respect to textual generation. It has some bias towards certain domains and topics that are over-represented in the training data. Its capabilities are relatively limited so far and it is trained to produce only one voice to avoid impersonation. Yet, we need the perspective in time to establish the sociotechnical limitations. 


## Training Details

### Training Data

The training data is detailled in the paper. 

### Training procedure and hyper-parameters

The different stages of the training procedure are detailled in the paper along with the hyper-parameters. 

## Citation 

```
@techreport{kyutai2024moshi,
    author = {Alexandre D\'efossez and Laurent Mazar\'e and Manu Orsini and Am\'elie Royer and Patrick P\'erez and Herv\'e J\'egou and Edouard Grave and Neil Zeghidour},
    title = {Moshi: a speech-text foundation model for real-time dialogue},
    institution = {Kyutai},
    year={2024},
    month={September},
    url={http://kyutai.org/Moshi.pdf},
}
```

## Model Card Authors

Alexandre Défossez, Laurent Mazaré, Manu Orsini, Amélie Royer, Patrick Pérez, Hervé Jégou, Edouard Grave, Neil Zeghidour, Yoach Lacombe