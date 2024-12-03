---
language: ja
library_name: transformers
license: apache-2.0
tags:
- audio
- automatic-speech-recognition
- hf-asr-leaderboard
widget:
- example_title: CommonVoice 8.0 (Test Split)
  src: >-
    https://huggingface.co/datasets/japanese-asr/ja_asr.common_voice_8_0/resolve/main/sample.flac
- example_title: JSUT Basic 5000
  src: >-
    https://huggingface.co/datasets/japanese-asr/ja_asr.jsut_basic5000/resolve/main/sample.flac
- example_title: ReazonSpeech (Test Split)
  src: >-
    https://huggingface.co/datasets/japanese-asr/ja_asr.reazonspeech_test/resolve/main/sample.flac
pipeline_tag: automatic-speech-recognition
datasets:
- japanese-asr/whisper_transcriptions.reazonspeech.all
- japanese-asr/whisper_transcriptions.reazonspeech.all.wer_10.0
- japanese-asr/whisper_transcriptions.reazonspeech.all.wer_10.0.vectorized
---

# Kotoba-Whisper-v2.1
_Kotoba-Whisper-v2.1_ is a Japanese ASR model based on [kotoba-tech/kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0), with 
additional postprocessing stacks integrated as [`pipeline`](https://huggingface.co/docs/transformers/en/main_classes/pipelines). The new features includes 
(i) improved timestamp achieved by [stable-ts](https://github.com/jianfch/stable-ts) and (ii) adding punctuation with [punctuators](https://github.com/1-800-BAD-CODE/punctuators/tree/main). 
These libraries are merged into Kotoba-Whisper-v2.1 via pipeline and will be applied seamlessly to the predicted transcription from [kotoba-tech/kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0).
The pipeline has been developed through the collaboration between [Asahi Ushio](https://asahiushio.com) and [Kotoba Technologies](https://twitter.com/kotoba_tech)


Following table presents the raw CER (unlike usual CER where the punctuations are removed before computing the metrics, see the evaluation script [here](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1/blob/main/run_short_form_eval.py))
along with the.


| model                                                                                                                                             |   [CommonVoice 8 (Japanese test set)](https://huggingface.co/datasets/japanese-asr/ja_asr.common_voice_8_0) |   [JSUT Basic 5000](https://huggingface.co/datasets/japanese-asr/ja_asr.jsut_basic5000) |   [ReazonSpeech (held out test set)](https://huggingface.co/datasets/japanese-asr/ja_asr.reazonspeech_test) |
|:--------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------:|----------------------------------------------------------------------------------------:|------------------------------------------------------------------------------------------------------------:|
| [kotoba-tech/kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0)                                                         |                                                                                                        17.6 |                                                                                    15.4 |                                                                                                        17.4 |
| [kotoba-tech/kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1)                                                         |                                                                                                        17.7 |                                                                                    15.4 |                                                                                                        17   |
| [kotoba-tech/kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) (punctuator + stable-ts)                                |                                                                                                        17.7 |                                                                                    15.4 |                                                                                                        17   |
| [kotoba-tech/kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) (punctuator)                                            |                                                                                                        17.7 |                                                                                    15.4 |                                                                                                        17   |
| [kotoba-tech/kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) (stable-ts)                                             |                                                                                                        17.7 |                                                                                    15.4 |                                                                                                        17   |
| [kotoba-tech/kotoba-whisper-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.0)                                                         |                                                                                                        17.8 |                                                                                    15.2 |                                                                                                        17.8 |
| [kotoba-tech/kotoba-whisper-v1.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1)                                                         |                                                                                                        17.9 |                                                                                    15   |                                                                                                        17.8 |
| [kotoba-tech/kotoba-whisper-v1.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1) (punctuator + stable-ts)                                |                                                                                                        17.9 |                                                                                    15   |                                                                                                        17.8 |
| [kotoba-tech/kotoba-whisper-v1.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1) (punctuator)                                            |                                                                                                        17.9 |                                                                                    15   |                                                                                                        17.8 |
| [kotoba-tech/kotoba-whisper-v1.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1) (stable-ts)                                             |                                                                                                        17.9 |                                                                                    15   |                                                                                                        17.8 |
| [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3)                                                                         |                                                                                                        15.3 |                                                                                    13.4 |                                                                                                        20.5 |
| [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2)                                                                         |                                                                                                        15.9 |                                                                                    10.6 |                                                                                                        34.6 |
| [openai/whisper-large](https://huggingface.co/openai/whisper-large)                                                                               |                                                                                                        16.6 |                                                                                    11.3 |                                                                                                        40.7 |
| [openai/whisper-medium](https://huggingface.co/openai/whisper-medium)                                                                             |                                                                                                        17.9 |                                                                                    13.1 |                                                                                                        39.3 |
| [openai/whisper-base](https://huggingface.co/openai/whisper-base)                                                                                 |                                                                                                        34.5 |                                                                                    26.4 |                                                                                                        76   |
| [openai/whisper-small](https://huggingface.co/openai/whisper-small)                                                                               |                                                                                                        21.5 |                                                                                    18.9 |                                                                                                        48.1 |
| [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny)                                                                                 |                                                                                                        58.8 |                                                                                    38.3 |                                                                                                       153.3 |


Regarding to the normalized CER, since those update from v2.1 will be removed by the normalization, kotoba-tech/kotoba-whisper-v2.1 marks the same CER values as [kotoba-tech/kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0).

### Latency
Please refer to the section of the latency in the kotoba-whisper-v1.1 [here](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1#latency).

## Transformers Usage
Kotoba-Whisper-v2.1 is supported in the Hugging Face 🤗 Transformers library from version 4.39 onwards. To run the model, first 
install the latest version of Transformers.

```bash
pip install --upgrade pip
pip install --upgrade transformers accelerate torchaudio
pip install stable-ts==2.16.0
pip install punctuators==0.0.5
```

### Transcription
The model can be used with the [`pipeline`](https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.AutomaticSpeechRecognitionPipeline)
class to transcribe audio files as follows:

```python
import torch
from transformers import pipeline
from datasets import load_dataset

# config
model_id = "kotoba-tech/kotoba-whisper-v2.1"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
device = "cuda:0" if torch.cuda.is_available() else "cpu"
model_kwargs = {"attn_implementation": "sdpa"} if torch.cuda.is_available() else {}
generate_kwargs = {"language": "ja", "task": "transcribe"}

# load model
pipe = pipeline(
    model=model_id,
    torch_dtype=torch_dtype,
    device=device,
    model_kwargs=model_kwargs,
    chunk_length_s=15,
    batch_size=16,
    trust_remote_code=True,
    stable_ts=True,
    punctuator=True
)

# load sample audio
dataset = load_dataset("japanese-asr/ja_asr.reazonspeech_test", split="test")
sample = dataset[0]["audio"]

# run inference
result = pipe(sample, return_timestamps=True, generate_kwargs=generate_kwargs)
print(result)
```

- To transcribe a local audio file, simply pass the path to your audio file when you call the pipeline:
```diff
- result = pipe(sample, return_timestamps=True, generate_kwargs=generate_kwargs)
+ result = pipe("audio.mp3", return_timestamps=True, generate_kwargs=generate_kwargs)
```

- To deactivate stable-ts:
```diff
-     stable_ts=True,
+     stable_ts=False,
```

- To deactivate punctuator:
```diff
-     punctuator=True,
+     punctuator=False,
```


### Flash Attention 2
We recommend using [Flash-Attention 2](https://huggingface.co/docs/transformers/main/en/perf_infer_gpu_one#flashattention-2) 
if your GPU allows for it. To do so, you first need to install [Flash Attention](https://github.com/Dao-AILab/flash-attention):

```
pip install flash-attn --no-build-isolation
```

Then pass `attn_implementation="flash_attention_2"` to `from_pretrained`:

```diff
- model_kwargs = {"attn_implementation": "sdpa"} if torch.cuda.is_available() else {}
+ model_kwargs = {"attn_implementation": "flash_attention_2"} if torch.cuda.is_available() else {}
```


## Acknowledgements
* [OpenAI](https://openai.com/) for the Whisper [model](https://huggingface.co/openai/whisper-large-v3).
* Hugging Face 🤗 [Transformers](https://github.com/huggingface/transformers) for the model integration.
* Hugging Face 🤗 for the [Distil-Whisper codebase](https://github.com/huggingface/distil-whisper).
* [Reazon Human Interaction Lab](https://research.reazon.jp/) for the [ReazonSpeech dataset](https://huggingface.co/datasets/reazon-research/reazonspeech).