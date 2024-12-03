---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/model-cards
license: cc-by-4.0
language:
- en
library_name: moshi
---

# Model Card for Moshi


Moshi is a speech-text foundation model and full-duplex spoken dialogue framework

## Model Details

MLX version for Mac quantized with 8-bits precision. 

### Model Description

Moshi is a speech-text foundation model that casts spoken dialogue as speech-to-speech generation. Starting from a text language model backbone, Moshi generates speech as tokens from the residual quantizer of a neural audio codec, while modeling separately its own speech and that of the user into parallel streams. This allows for the removal of explicit speaker turns, and the modeling of arbitrary conversational dynamics.
Moshi also predicts time-aligned text tokens as a prefix to audio tokens. This “Inner
Monologue” method significantly improves the linguistic quality of generated speech and provides streaming speech recognition and text-to-speech. As a result, Moshi is the first real-time full-duplex spoken large language model, with a theoretical latency of 160ms, 200ms in practice. 


- **Developed by:**  Kyutai
- **Model type:** Multimodal speech-text foundation model
- **Language(s) (NLP):** English
- **License:** CC-BY

### Model Sources 


- **Repository:** [repo](https://github.com/kyutai-labs/moshi) 
- **Paper:** [paper](http://kyutai.org/Moshi.pdf) 
- **Demo:** [demo](https://moshi.chat/) 

## Uses

### Direct Use

The model can be used as a conversational agent for casual conversations, basic facts and advice (e.g. recipes, trivia), roleplay, etc. However, the model has limited abilities for complex tasks and cannot access tools, but rather focues on natural, low-latency interactions. 


### Downstream Use

Some components of the model can be used independently or repurposed relatively easily. 
For instance the Mimi codec is a state-of-the-art audio neural codec that combines semantic and acoustic information into audio tokens running at 12Hz and a bitrate of 1.1kbps, which make it particularly adapted to train speech language models or text-to-speech systems.. Regarding the main Moshi architecture, other downstream usecases would require some finetuning / domain adaptation. 


### Out-of-Scope Use

The model is not intended to be used to impersonate other people or any malicious use of any kind. 
This model is for research only and we do not recommend it for providing advices or to perform any professionnal duty. 


## Bias, Risks, and Limitations

The model has been trained with a few safeguards to try to limit potential toxic usages, however our toxicity analysis shows that it behaves in the middle of existing models with respect to textual generation. It has some bias towards certain domains and topics that are over-represented in the training data. Its capabilities are relatively limited so far and it is trained to produce only one voice to avoid impersonation. Yet, we need the perspective in time to establish the sociotechnical limitations. 


## How to Get Started with the Model

See the main [README](https://github.com/kyutai-labs/moshi) file. 

## Training Details

### Training Data

- Textual data: The underlying Helium model is trained on a mix of data, more precisely:

  - 12.5% is high-quality data sources from the following curated sources: [Wikipedia](https://dumps.wikimedia.org/) Wikibooks, Wikisource, Wikinews,
[StackExchange](https://archive.org/details/stackexchange) and the collection of [scientific articles pes2o](https://github.com/allenai/peS2o). For Wikipedia, we use five different dumps from 2017, 2018, 2019, 2021 and 2022.
  - 87.5% is filtered web data from CommonCrawl, using the following crawls: 2018-30, 2019-04, 2019-30, 2020-05, 2020-34, 2021-04, 2021-31, 2022-05, 2022-33, 2023-40. 

- Audio data

  - **Unsupervised audio dataset:** used for pre-training, this is a collection of 7 million hours of readily available audio content, which consists mostly of English speech. This training set is transcribed with [Whisper](https://github.com/openai/whisper) (large v3 model)
  - **The Fisher dataset:**: used to enable multi-stream. It consists of 2000 hours of phone conversations at 8kHz from Fisher, which we upsample to 24kHz using [AudioSR](https://audioldm.github.io/audiosr/).
  - **Supervised multi-stream dataset:** A dataset of 170 hours of natural and scripted conversation between multiple pairs of participants, collected by Kyutai. This dataset is used to train the TTS system used to create synthetic data.
  - **Synthetic data:** 20,000 hours of synthetic data generated by our TTS system, and simulating a dialogue between Moshi and a user.

### Training procedure and hyper-parameters

The different stages of the training procedure are detailled in the paper along with the hyper-parameters. 

### Compute Infrastructure

The training was performed on 127 DGX nodes provided by Scaleway, accounting for 1016 H100 Nvidia GPUs. 


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

Alexandre Défossez, Laurent Mazaré, Manu Orsini, Amélie Royer, Patrick Pérez, Hervé Jégou, Edouard Grave, Neil Zeghidour