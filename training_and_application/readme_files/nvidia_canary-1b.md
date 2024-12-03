---
license: cc-by-nc-4.0
language:
- en
- de
- es
- fr
library_name: nemo
datasets:
- librispeech_asr
- fisher_corpus
- Switchboard-1
- WSJ-0
- WSJ-1
- National-Singapore-Corpus-Part-1
- National-Singapore-Corpus-Part-6
- vctk
- voxpopuli
- europarl
- multilingual_librispeech
- mozilla-foundation/common_voice_8_0
- MLCommons/peoples_speech
thumbnail: null
tags:
- automatic-speech-recognition
- automatic-speech-translation
- speech
- audio
- Transformer
- FastConformer
- Conformer
- pytorch
- NeMo
- hf-asr-leaderboard
widget:
- example_title: Librispeech sample 1
  src: https://cdn-media.huggingface.co/speech_samples/sample1.flac
- example_title: Librispeech sample 2
  src: https://cdn-media.huggingface.co/speech_samples/sample2.flac
model-index:
- name: canary-1b
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: LibriSpeech (other)
      type: librispeech_asr
      config: other
      split: test
      args:
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 2.89
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: SPGI Speech
      type: kensho/spgispeech
      config: test
      split: test
      args:
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 4.79
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 16.1
      type: mozilla-foundation/common_voice_16_1
      config: en
      split: test
      args:
        language: en
    metrics:
    - name: Test WER (En)
      type: wer
      value: 7.97
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 16.1
      type: mozilla-foundation/common_voice_16_1
      config: de
      split: test
      args:
        language: de
    metrics:
    - name: Test WER (De)
      type: wer
      value: 4.61
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 16.1
      type: mozilla-foundation/common_voice_16_1
      config: es
      split: test
      args:
        language: es
    metrics:
    - name: Test WER (ES)
      type: wer
      value: 3.99
  - task:
      type: Automatic Speech Recognition
      name: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 16.1
      type: mozilla-foundation/common_voice_16_1
      config: fr
      split: test
      args:
        language: fr
    metrics:
    - name: Test WER (Fr)
      type: wer
      value: 6.53
  - task:
      type: Automatic Speech Translation
      name: automatic-speech-translation
    dataset:
      name: FLEURS
      type: google/fleurs
      config: en_us
      split: test
      args:
        language: en-de
    metrics:
    - name: Test BLEU (En->De)
      type: bleu
      value: 32.15
  - task:
      type: Automatic Speech Translation
      name: automatic-speech-translation
    dataset:
      name: FLEURS
      type: google/fleurs
      config: en_us
      split: test
      args:
        language: en-de
    metrics:
    - name: Test BLEU (En->Es)
      type: bleu
      value: 22.66
  - task:
      type: Automatic Speech Translation
      name: automatic-speech-translation
    dataset:
      name: FLEURS
      type: google/fleurs
      config: en_us
      split: test
      args:
        language: en-de
    metrics:
    - name: Test BLEU (En->Fr)
      type: bleu
      value: 40.76
  - task:
      type: Automatic Speech Translation
      name: automatic-speech-translation
    dataset:
      name: FLEURS
      type: google/fleurs
      config: de_de
      split: test
      args:
        language: de-en
    metrics:
    - name: Test BLEU (De->En)
      type: bleu
      value: 33.98
  - task:
      type: Automatic Speech Translation
      name: automatic-speech-translation
    dataset:
      name: FLEURS
      type: google/fleurs
      config: es_419
      split: test
      args:
        language: es-en
    metrics:
    - name: Test BLEU (Es->En)
      type: bleu
      value: 21.80
  - task:
      type: Automatic Speech Translation
      name: automatic-speech-translation
    dataset:
      name: FLEURS
      type: google/fleurs
      config: fr_fr
      split: test
      args:
        language: fr-en
    metrics:
    - name: Test BLEU (Fr->En)
      type: bleu
      value: 30.95
  - task:
      type: Automatic Speech Translation
      name: automatic-speech-translation
    dataset:
      name: COVOST
      type: covost2
      config: de_de
      split: test
      args:
        language: de-en
    metrics:
    - name: Test BLEU (De->En)
      type: bleu
      value: 37.67
  - task:
      type: Automatic Speech Translation
      name: automatic-speech-translation
    dataset:
      name: COVOST
      type: covost2
      config: es_419
      split: test
      args:
        language: es-en
    metrics:
    - name: Test BLEU (Es->En)
      type: bleu
      value: 40.7
  - task:
      type: Automatic Speech Translation
      name: automatic-speech-translation
    dataset:
      name: COVOST
      type: covost2
      config: fr_fr
      split: test
      args:
        language: fr-en
    metrics:
    - name: Test BLEU (Fr->En)
      type: bleu
      value: 40.42
  
metrics:
- wer
- bleu
pipeline_tag: automatic-speech-recognition
---


# Canary 1B

<style>
img {
 display: inline;
}
</style>

[![Model architecture](https://img.shields.io/badge/Model_Arch-FastConformer--Transformer-lightgrey#model-badge)](#model-architecture)
| [![Model size](https://img.shields.io/badge/Params-1B-lightgrey#model-badge)](#model-architecture)
| [![Language](https://img.shields.io/badge/Language-multilingual-lightgrey#model-badge)](#datasets)

NVIDIA [NeMo Canary](https://nvidia.github.io/NeMo/blogs/2024/2024-02-canary/) is a family of multi-lingual multi-tasking models that achieves state-of-the art performance on multiple benchmarks. With 1 billion parameters, Canary-1B supports automatic speech-to-text recognition (ASR) in 4 languages (English, German, French, Spanish) and translation from English to German/French/Spanish and from German/French/Spanish to English with or without punctuation and capitalization (PnC). 

## Model Architecture

Canary is an encoder-decoder model with FastConformer [1] encoder and Transformer Decoder [2]. 
With audio features extracted from the encoder, task tokens such as `<source language>`, `<target language>`, `<task>` and `<toggle PnC>` 
are fed into the Transformer Decoder to trigger the text generation process. Canary uses a concatenated tokenizer [5] from individual 
SentencePiece [3] tokenizers of each language, which makes it easy to scale up to more languages. 
The Canay-1B model has 24 encoder layers and 24 layers of decoder layers in total.



## NVIDIA NeMo

To train, fine-tune or Transcribe with Canary, you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed Cython and latest PyTorch version.
```
pip install git+https://github.com/NVIDIA/NeMo.git@r1.23.0#egg=nemo_toolkit[asr]
```


## How to Use this Model

The model is available for use in the NeMo toolkit [4], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

### Loading the Model

```python
from nemo.collections.asr.models import EncDecMultiTaskModel

# load model
canary_model = EncDecMultiTaskModel.from_pretrained('nvidia/canary-1b')

# update dcode params
decode_cfg = canary_model.cfg.decoding
decode_cfg.beam.beam_size = 1
canary_model.change_decoding_strategy(decode_cfg)
```

### Input Format
Input to Canary can be either a list of paths to audio files or a jsonl manifest file.

If the input is a list of paths, Canary assumes that the audio is English and Transcribes it. I.e., Canary default behaviour is English ASR. 
```python
predicted_text = canary_model.transcribe(
    paths2audio_files=['path1.wav', 'path2.wav'],
    batch_size=16,  # batch size to run the inference with
)
```

To use Canary for transcribing other supported languages or perform Speech-to-Text translation, specify the input as jsonl manifest file, where each line in the file is a dictionary containing the following fields: 

```yaml
# Example of a line in input_manifest.json
{
    "audio_filepath": "/path/to/audio.wav",  # path to the audio file
    "duration": 1000,  # duration of the audio, can be set to `None` if using NeMo main branch
    "taskname": "asr",  # use "s2t_translation" for speech-to-text translation with r1.23, or "ast" if using the NeMo main branch
    "source_lang": "en",  # language of the audio input, set `source_lang`==`target_lang` for ASR, choices=['en','de','es','fr']
    "target_lang": "en",  # language of the text output, choices=['en','de','es','fr']
    "pnc": "yes",  # whether to have PnC output, choices=['yes', 'no']
    "answer": "na", 
}
```

and then use:
```python
predicted_text = canary_model.transcribe(
    "<path to input manifest file>",
    batch_size=16,  # batch size to run the inference with
)
```


### Automatic Speech-to-text Recognition (ASR)

An example manifest for transcribing English audios can be:

```yaml
# Example of a line in input_manifest.json
{
    "audio_filepath": "/path/to/audio.wav",  # path to the audio file
    "duration": 1000,  # duration of the audio, can be set to `None` if using NeMo main branch
    "taskname": "asr",  
    "source_lang": "en", # language of the audio input, set `source_lang`==`target_lang` for ASR, choices=['en','de','es','fr']
    "target_lang": "en", # language of the text output, choices=['en','de','es','fr']
    "pnc": "yes",  # whether to have PnC output, choices=['yes', 'no']
    "answer": "na", 
}
```


### Automatic Speech-to-text Translation (AST)

An example manifest for transcribing English audios into German text can be:

```yaml
# Example of a line in input_manifest.json
{
    "audio_filepath": "/path/to/audio.wav",  # path to the audio file
    "duration": 1000,  # duration of the audio, can be set to `None` if using NeMo main branch
    "taskname": "s2t_translation", # r1.23 only recognizes "s2t_translation", but "ast" is supported if using the NeMo main branch
    "source_lang": "en", # language of the audio input, choices=['en','de','es','fr']
    "target_lang": "de", # language of the text output, choices=['en','de','es','fr']
    "pnc": "yes",  # whether to have PnC output, choices=['yes', 'no']
    "answer": "na" 
}
```

Alternatively, one can use `transcribe_speech.py` script to do the same. 

```bash
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py 
 pretrained_name="nvidia/canary-1b" 
 audio_dir="<path to audio_directory>" # transcribes all the wav files in audio_directory
```


```bash
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py 
 pretrained_name="nvidia/canary-1b" 
 dataset_manifest="<path to manifest file>" 
```


### Input

This model accepts single channel (mono) audio sampled at 16000 Hz, along with the task/languages/PnC tags as input.

### Output

The model outputs the transcribed/translated text corresponding to the input audio, in the specified target language and with or without punctuation and capitalization.



## Training

Canary-1B is trained using the  NVIDIA NeMo toolkit [4] for 150k steps with dynamic bucketing and a batch duration of 360s per GPU on 128 NVIDIA A100 80GB GPUs. 
The model can be trained using this [example script](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/speech_multitask/speech_to_text_aed.py) and [base config](https://github.com/NVIDIA/NeMo/blob/main/examples/asr/conf/speech_multitask/fast-conformer_aed.yaml).

The tokenizers for these models were built using the text transcripts of the train set with this [script](https://github.com/NVIDIA/NeMo/blob/main/scripts/tokenizers/process_asr_text_tokenizer.py).


### Datasets

The Canary-1B model is trained on a total of 85k hrs of speech data. It consists of 31k hrs of public data, 20k hrs collected by [Suno](https://suno.ai/), and 34k hrs of in-house data. 

The constituents of public data are as follows. 

#### English (25.5k hours)
- Librispeech 960 hours
- Fisher Corpus
- Switchboard-1 Dataset
- WSJ-0 and WSJ-1
- National Speech Corpus (Part 1, Part 6)
- VCTK
- VoxPopuli (EN)
- Europarl-ASR (EN)
- Multilingual Librispeech (MLS EN) - 2,000 hour subset
- Mozilla Common Voice (v7.0)
- People's Speech - 12,000 hour subset
- Mozilla Common Voice (v11.0)  - 1,474 hour subset

#### German (2.5k hours)
- Mozilla Common Voice (v12.0)  - 800 hour subset
- Multilingual Librispeech (MLS DE) - 1,500 hour subset
- VoxPopuli (DE) - 200 hr subset

#### Spanish (1.4k hours)
- Mozilla Common Voice (v12.0)  - 395 hour subset
- Multilingual Librispeech (MLS ES) - 780 hour subset
- VoxPopuli (ES) - 108 hour subset
- Fisher  - 141 hour subset

#### French (1.8k hours)
- Mozilla Common Voice (v12.0)  - 708 hour subset
- Multilingual Librispeech (MLS FR) - 926 hour subset
- VoxPopuli (FR) - 165 hour subset


## Performance

In both ASR and AST experiments, predictions were generated using beam search with width 5 and length penalty 1.0.

### ASR Performance (w/o PnC) 

The ASR performance is measured with word error rate (WER), and we process the groundtruth and predicted text with [whisper-normalizer](https://pypi.org/project/whisper-normalizer/).

WER on [MCV-16.1](https://commonvoice.mozilla.org/en/datasets) test set:

| **Version** | **Model**     | **En**   | **De**   | **Es**   | **Fr**   |
|:---------:|:-----------:|:------:|:------:|:------:|:------:|
| 1.23.0  | canary-1b | 7.97 | 4.61 | 3.99 | 6.53 |


WER on [MLS](https://huggingface.co/datasets/facebook/multilingual_librispeech) test set:

| **Version** | **Model**     | **En**   | **De**   | **Es**   | **Fr**   |
|:---------:|:-----------:|:------:|:------:|:------:|:------:|
| 1.23.0  | canary-1b | 3.06 | 4.19 | 3.15 | 4.12 |


More details on evaluation can be found at [HuggingFace ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)

### AST Performance

We evaluate AST performance with [BLEU score](https://lightning.ai/docs/torchmetrics/stable/text/sacre_bleu_score.html), and use native annotations with punctuation and capitalization in the datasets.

BLEU score on [FLEURS](https://huggingface.co/datasets/google/fleurs) test set:

| **Version** | **Model** | **En->De** | **En->Es** | **En->Fr** | **De->En** | **Es->En** | **Fr->En** |
|:-----------:|:---------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| 1.23.0      | canary-1b | 32.15	   | 22.66      | 40.76      | 33.98      | 21.80      | 30.95      |


BLEU score on [COVOST-v2](https://github.com/facebookresearch/covost) test set:

| **Version** | **Model** | **De->En** | **Es->En** | **Fr->En** |
|:-----------:|:---------:|:----------:|:----------:|:----------:|
| 1.23.0      | canary-1b | 37.67      | 40.7       | 40.42      |

BLEU score on [mExpresso](https://huggingface.co/facebook/seamless-expressive#mexpresso-multilingual-expresso) test set:

| **Version** | **Model** | **En->De** | **En->Es** | **En->Fr** |
|:-----------:|:---------:|:----------:|:----------:|:----------:|
| 1.23.0      | canary-1b | 23.84      |   35.74    | 28.29      |

## Model Fairness Evaluation

As outlined in the paper "Towards Measuring Fairness in AI: the Casual Conversations Dataset", we assessed the canary-1.1b model for fairness. The model was evaluated on the CausalConversations-v1 dataset, and the results are reported as follows:

### Gender Bias:

| Gender | Male | Female | N/A | Other |
| :--- | :--- | :--- | :--- | :--- |
| Num utterances | 19325 | 24532 | 926 | 33 |
| % WER | 14.64 | 12.92 | 17.88 | 126.92 |

### Age Bias:

| Age Group | (18-30) | (31-45) | (46-85) | (1-100) |
| :--- | :--- | :--- | :--- | :--- |
| Num utterances | 15956 | 14585 | 13349 | 43890 |
| % WER | 14.64 | 13.07 | 13.47 | 13.76 |

(Error rates for fairness evaluation are determined by normalizing both the reference and predicted text, similar to the methods used in the evaluations found at https://github.com/huggingface/open_asr_leaderboard.)

## NVIDIA Riva: Deployment

[NVIDIA Riva](https://developer.nvidia.com/riva), is an accelerated speech AI SDK deployable on-prem, in all clouds, multi-cloud, hybrid, on edge, and embedded. 
Additionally, Riva provides: 

* World-class out-of-the-box accuracy for the most common languages with model checkpoints trained on proprietary data with hundreds of thousands of GPU-compute hours 
* Best in class accuracy with run-time word boosting (e.g., brand and product names) and customization of acoustic model, language model, and inverse text normalization 
* Streaming speech recognition, Kubernetes compatible scaling, and enterprise-grade support 

Although this model isn’t supported yet by Riva, the [list of supported models](https://huggingface.co/models?other=Riva) is here.  
Check out [Riva live demo](https://developer.nvidia.com/riva#demos). 


## References
[1] [Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](https://arxiv.org/abs/2305.05084)

[2] [Attention is all you need](https://arxiv.org/abs/1706.03762)

[3] [Google Sentencepiece Tokenizer](https://github.com/google/sentencepiece)

[4] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)

[5] [Unified Model for Code-Switching Speech Recognition and Language Identification Based on Concatenated Tokenizer](https://aclanthology.org/2023.calcs-1.7.pdf)

## Licence

License to use this model is covered by the [CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en#:~:text=NonCommercial%20%E2%80%94%20You%20may%20not%20use,doing%20anything%20the%20license%20permits.). By downloading the public and release version of the model, you accept the terms and conditions of the CC-BY-NC-4.0 license.