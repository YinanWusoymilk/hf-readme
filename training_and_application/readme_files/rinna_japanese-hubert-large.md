---
thumbnail: https://github.com/rinnakk/japanese-pretrained-models/blob/master/rinna.png
language: ja
license: apache-2.0
datasets: reazon-research/reazonspeech
inference: false
tags:
  - hubert
  - speech
---

# `rinna/japanese-hubert-large`

![rinna-icon](./rinna.png)

# Overview

This is a Japanese HuBERT Large model trained by [rinna Co., Ltd.](https://rinna.co.jp/)

* **Model summary**

  The model architecture is the same as the [original HuBERT Large model](https://huggingface.co/facebook/hubert-large-ll60k), which contains 24 transformer layers with 16 attention heads.
  The model was trained using code from the [official repository](https://github.com/facebookresearch/fairseq/tree/main/examples/hubert), and the detailed training configuration can be found in the same repository and the [original paper](https://ieeexplore.ieee.org/document/9585401).

* **Training**

  The model was trained on approximately 19,000 hours of following Japanese speech corpus ReazonSpeech v1.
  - [ReazonSpeech](https://huggingface.co/datasets/reazon-research/reazonspeech)

* **Contributors**

  - [Yukiya Hono](https://huggingface.co/yky-h)
  - [Kentaro Mitsui](https://huggingface.co/Kentaro321)
  - [Kei Sawada](https://huggingface.co/keisawada)
    
---

# How to use the model

```python
import soundfile as sf
from transformers import AutoFeatureExtractor, AutoModel

model_name = "rinna/japanese-hubert-large"
feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
model.eval()

raw_speech_16kHz, sr = sf.read(audio_file)
inputs = feature_extractor(
    raw_speech_16kHz,
    return_tensors="pt",
    sampling_rate=sr,
)
outputs = model(**inputs)

print(f"Input:  {inputs.input_values.size()}")  # [1, #samples]
print(f"Output: {outputs.last_hidden_state.size()}")  # [1, #frames, 1024]
```

A fairseq checkpoint file can also be available [here](https://huggingface.co/rinna/japanese-hubert-large/tree/main/fairseq).

---

# How to cite
```bibtex
@misc{rinna-japanese-hubert-large,
    title = {rinna/japanese-hubert-large},
    author = {Hono, Yukiya and Mitsui, Kentaro and Sawada, Kei},
    url = {https://huggingface.co/rinna/japanese-hubert-large}
}

@inproceedings{sawada2024release,
    title = {Release of Pre-Trained Models for the {J}apanese Language},
    author = {Sawada, Kei and Zhao, Tianyu and Shing, Makoto and Mitsui, Kentaro and Kaga, Akio and Hono, Yukiya and Wakatsuki, Toshiaki and Mitsuda, Koh},
    booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)},
    month = {5},
    year = {2024},
    pages = {13898--13905},
    url = {https://aclanthology.org/2024.lrec-main.1213},
    note = {\url{https://arxiv.org/abs/2404.01657}}
}
```

---

# References
```bibtex
@article{hsu2021hubert,
    author = {Hsu, Wei-Ning and Bolte, Benjamin and Tsai, Yao-Hung Hubert and Lakhotia, Kushal and Salakhutdinov, Ruslan and Mohamed, Abdelrahman},
    journal = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},
    title = {HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units},
    year = {2021},
    volume = {29},
    pages = {3451-3460},
    doi = {10.1109/TASLP.2021.3122291}
}
```
---

# License
[The Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0)
