---
license: cc-by-4.0
language:
- 'no'
- nb
- nn
- en
datasets:
- NbAiLab/ncc_speech
- NbAiLab/NST
- NbAiLab/NPSC
tags:
- audio
- asr
- automatic-speech-recognition
- hf-asr-leaderboard
metrics:
- wer
- cer
library_name: transformers
pipeline_tag: automatic-speech-recognition
widget:
- src: https://datasets-server.huggingface.co/assets/google/fleurs/--/nb_no/train/1/audio/audio.mp3
  example_title: FLEURS sample 1
- src: https://datasets-server.huggingface.co/assets/google/fleurs/--/nb_no/train/4/audio/audio.mp3
  example_title: FLEURS sample 2
---

# NB-Whisper Large (beta)

This is a **_public beta_** of the Norwegian NB-Whisper Large model released by the National Library of Norway. NB-Whisper is a series of models for automatic speech recognition (ASR) and speech translation, building upon the foundation laid by [OpenAI's Whisper](https://arxiv.org/abs/2212.04356). All models are trained on 20,000 hours of labeled data.

<center>
  <figure>
    <video controls>
      <source src="https://huggingface.co/NbAiLab/nb-whisper-small-beta/resolve/main/king.mp4" type="video/mp4">
    Your browser does not support the video tag.
    </video>   
  <figcaption><a href="https://www.royalcourt.no/tale.html?tid=137662&sek=28409&scope=27248" target="_blank">Speech given by His Majesty The King of Norway at the garden party hosted by Their Majesties The King and Queen at the Palace Park on 1 September 2016.</a>Transcribed using the Small model.</figcaption>
</figure> 
</center>


## Model Details

NB-Whisper models will be available in five different sizes:

| Model Size | Parameters | Availability |
|------------|------------|--------------|
| tiny       | 39M        | [NB-Whisper Tiny (beta)](https://huggingface.co/NbAiLab/nb-whisper-tiny-beta) |
| base       | 74M        | [NB-Whisper Base (beta)](https://huggingface.co/NbAiLab/nb-whisper-base-beta) |
| small      | 244M       | [NB-Whisper Small (beta)](https://huggingface.co/NbAiLab/nb-whisper-small-beta) |
| medium     | 769M       | [NB-Whisper Medium (beta)](https://huggingface.co/NbAiLab/nb-whisper-medium-beta) |
| large      | 1550M      | [NB-Whisper Large (beta)](https://huggingface.co/NbAiLab/nb-whisper-large-beta) |

An official release of NB-Whisper models is planned for the Fall 2023.

Please refer to the OpenAI Whisper model card for more details about the backbone model.

### Model Description

- **Developed by:** [NB AI-Lab](https://ai.nb.no/)
- **Shared by:** [NB AI-Lab](https://ai.nb.no/)
- **Model type:** `whisper`
- **Language(s) (NLP):** Norwegian, Norwegian Bokmål, Norwegian Nynorsk, English
- **License:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- **Finetuned from model:** [openai/whisper-small](https://huggingface.co/openai/whisper-small)

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/NbAiLab/nb-whisper/
- **Paper:** _Coming soon_
- **Demo:** http://ai.nb.no/demo/nb-whisper

## Uses

### Direct Use

This is a **_public beta_** release. The models published in this repository are intended for a generalist purpose and are available to third parties.


### Downstream Use

For Norwegian transcriptions we are confident that this public beta will give you State-of-the-Art results compared to currently available Norwegian ASR models of the same size. However, it is still known to show some hallucinations, as well as a tendency to drop part of the transcript from time to time. Please also note that the transcripts are typically not word by word. Spoken language and written language are often very different, and the model aims to "translate" spoken utterances into grammatically correct written sentences. We strongly believe that the best way to understand these models is to try them yourself.

A significant part of the training material comes from TV subtitles. Subtitles often shorten the content to make it easier to read. Typically, non-essential parts of the utterance can be also dropped. In some cases, this is a desired ability, in other cases, this is undesired. The final release of these model will provida a mechanism to control for this beaviour.



## Bias, Risks, and Limitations

This is a public beta that is not intended for production. Production use without adequate assessment of risks and mitigation may be considered irresponsible or harmful. These models may have bias and/or any other undesirable distortions. When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence. In no event shall the owner of the models (The National Library of Norway) be liable for any results arising from the use made by third parties of these models.



## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import pipeline

asr = pipeline(
    "automatic-speech-recognition",
    "NbAiLab/nb-whisper-large-beta"
)
asr(
    "audio.mp3",
    generate_kwargs={'task': 'transcribe', 'language': 'no'}
)
# {'text': ' Så mange anga kører seg i så viktig sak, så vi får du kører det tilbake med. Om kabaret gudam i at vi skal hjælge. Kør seg vi gjør en uda? Nei noe skal å abelistera sonvorne skrifer. Det er sak, så kjent det bare handling i samtatsen til bargører. Trudet første lask. På den å først så å køre og en gange samme, og så får vi gjør å vorte vorte vorte når vi kjent dit.'}
```

Timestamps can also be retrieved by passing in the right parameter.

```python
asr(
    "audio.mp3",
    generate_kwargs={'task': 'transcribe', 'language': 'no'},
    return_timestamps=True,
)
# {'text': ' at så mange angar til seg så viktig sak, så vi får jo kjølget klare tilbakemeldingen om hva valget dem gjør at vi skal gjøre. Hva skjer vi gjøre nå da? Nei, nå skal jo administrationen vår skrivferdige sak, så kjem til behandling i samfærdshetshøyvalget, tror det første 
#  r. Først så kan vi ta og henge dem kjemme, og så får vi gjøre vårt valget når vi kommer dit.',
#  'chunks': [{'timestamp': (0.0, 5.34),
#    'text': ' at så mange angar til seg så viktig sak, så vi får jo kjølget klare tilbakemeldingen om'},
#   {'timestamp': (5.34, 8.64),
#    'text': ' hva valget dem gjør at vi skal gjøre.'},
#   {'timestamp': (8.64, 10.64), 'text': ' Hva skjer vi gjøre nå da?'},
#   {'timestamp': (10.64, 17.44),
#    'text': ' Nei, nå skal jo administrationen vår skrivferdige sak, så kjem til behandling i samfærdshetshøyvalget,'},
#   {'timestamp': (17.44, 19.44), 'text': ' tror det første år.'},
#   {'timestamp': (19.44, 23.94),
#    'text': ' Først så kan vi ta og henge dem kjemme, og så får vi gjøre vårt valget når vi kommer dit.'}]}
```

## Training Data
Trained data comes from Språkbanken and the digital collection at the National Library of Norway. Training data includes:

- NST Norwegian ASR Database (16 kHz), and its corresponding dataset
- Transcribed speeches from the Norwegian Parliament produced by Språkbanken
- TV broadcast (NRK) subtitles (NLN digital collection)
- Audiobooks (NLN digital collection)


## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** TPUv4
- **Hours used:** 1,536
- **Cloud Provider:** Google Cloud
- **Compute Region:** `us-central1`
- **Carbon Emitted:** Total emissions are estimated to be 247.77 kgCO₂ of which 100 percents were directly offset by the cloud provider.


#### Software

The model is trained using Jax/Flax. The final model is converted to Pytorch, Tensorflow, whisper.cpp and ONXX. Please tell us if you would like future models to be converted to other format. 

## Citation & Contributors
The development of this model was part of the contributors' professional roles at the National Library of Norway, under the _NoSTram_ project led by _Per Egil Kummervold (PEK)_. The Jax code, dataset loaders, and training scripts were collectively designed by _Javier de la Rosa (JdlR)_, _Freddy Wetjen (FW)_, _Rolv-Arild Braaten (RAB)_, and _PEK_. Primary dataset curation was handled by _FW_, _RAB_, and _PEK_, while _JdlR_ and _PEK_ crafted the documentation. The project was completed under the umbrella of AiLab, directed by _Svein Arne Brygfjeld_. 

All contributors played a part in shaping the optimal training strategy for the Norwegian ASR model based on the Whisper architecture. 

_A paper detailing our process and findings is underway!_


## Acknowledgements

Thanks to [Google TPU Research Cloud](https://sites.research.google/trc/about/) for supporting this project with extensive training resources. Thanks to Google Cloud for supporting us with credits for translating large parts of the corpus. A special thanks to [Sanchit Ghandi](https://huggingface.co/sanchit-gandhi) for providing thorough technical advice in debugging and with the work of getting this to train on Google TPUs. A special thanks to Per Erik Solberg at Språkbanken for the collaboration with regard to the Stortinget corpus.

## Contact
We are releasing this ASR Whisper model as a public beta to gather constructive feedback on its performance. Please do not hesitate to contact us with any experiences, insights, or suggestions that you may have. Your input is invaluable in helping us to improve the model and ensure that it effectively serves the needs of users. Whether you have technical concerns, usability suggestions, or ideas for future enhancements, we welcome your input. Thank you for participating in this critical stage of our model's development.

If you intend to incorporate this model into your research, we kindly request that you reach out to us. We can provide you with the most current status of our upcoming paper, which you can cite to acknowledge and provide context for the work done on this model. 


Please use this email as the main contact point, it is read by the entire team: <a rel="noopener nofollow" href="mailto:ailab@nb.no">ailab@nb.no</a>
