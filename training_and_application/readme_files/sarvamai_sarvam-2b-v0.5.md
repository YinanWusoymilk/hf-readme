---
library_name: transformers
license: other
---

Update (Aug 15, 2024): You can now get started with text completions and supervised finetuning using [this notebook](https://colab.research.google.com/drive/1IZ-KJgzRAMr4Rm_-OWvWwnfTQwRxOknp?usp=sharing) on Google colab!

This is an early checkpoint of `sarvam-2b`, a small, yet powerful language model pre-trained from scratch on 2 trillion tokens. It is trained to be good at 10 Indic languages + English. Officially, the Indic languages supported are: Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, and Telugu. 

The final checkpoint of `sarvam-2b` will be released soon, and it will be trained on a data mixture of 4 trillion tokens: containing equal parts English (2T) and Indic (2T) tokens. 

The current checkpoint has not undergone any post-training. You can see the capabilities of the current checkpoint in [this video](https://www.youtube.com/watch?v=DFtAS1BCKvk).

The model was trained with [NVIDIA NeMo™ Framework](https://github.com/NVIDIA/NeMo) on the Yotta Shakti Cloud using HGX H100 systems.

Getting started:
```
from transformers import pipeline
pipe = pipeline(model='sarvamai/sarvam-2b-v0.5', device=0)
pipe('भारत के प्रथम प्रधानमंत्री', max_new_tokens=15, temperature=0.1, repetition_penalty=1.2)[0]['generated_text']
# 'भारत के प्रथम प्रधानमंत्री जवाहरलाल नेहरू थे।\n\n'
```

## Tokenizer

`sarvam-2b`'s tokenizer is built to be efficient for Indic languages and has an average fertility score of ~2 which is significantly lower than other models.

Here is a comparison of fertility scores between `sarvam-2b` and other popular models.
|     |Sarvam-2B|Llama-3.1|Gemma-2|GPT-4o|
|--------|------|---------|-------|------|
|ben_Beng|2.07  |8.02     |3.72   |2.34  |
|eng_Latn|1.43  |1.24     |1.23   |1.23  |
|guj_Gujr|1.81  |9.97     |3.9    |2.3   |
|hin_Deva|1.4   |2.67     |1.96   |1.65  |
|kan_Knda|2.37  |14.95    |5.55   |3.29  |
|mal_Mlym|2.85  |16.26    |5.88   |3.52  |
|mar_Deva|1.77  |3.99     |3.2    |2.56  |
|ory_Orya|2.35  |16.84    |6.87   |6.83  |
|pan_Guru|1.68  |8.19     |3.37   |2.72  |
|tam_Taml|2.17  |12.39    |4.19   |3.17  |
|tel_Telu|2.14  |13.3     |4.57   |3.06  |
|**Average** |**2.08**  |**9.34**     |**4.01**   |**3.00**  |

More technical details like evaluations and benchmarking will be posted soon.