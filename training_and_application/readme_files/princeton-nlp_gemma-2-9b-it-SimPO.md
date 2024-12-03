---
base_model: google/gemma-2-9b-it
tags:
- alignment-handbook
- generated_from_trainer
datasets:
- princeton-nlp/gemma2-ultrafeedback-armorm
model-index:
- name: princeton-nlp/gemma-2-9b-it-SimPO 
  results: []
license: mit
---

# gemma-2-9b-it-SimPO Model Card

SimPO (Simple Preference Optimization) is an offline preference optimization algorithm designed to enhance the training of large language models (LLMs) with preference optimization datasets. SimPO aligns the reward function with the generation likelihood, eliminating the need for a reference model and incorporating a target reward margin to boost performance. Please refer to our [preprint](https://arxiv.org/pdf/2405.14734) and [github repo](https://github.com/princeton-nlp/SimPO) for more details.


## Model Details

### Model Description

We fine-tuned [google/gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it) on [princeton-nlp/gemma2-ultrafeedback-armorm](https://huggingface.co/datasets/princeton-nlp/gemma2-ultrafeedback-armorm) with the SimPO objective.

- **Developed by:** Yu Meng, Mengzhou Xia, Danqi Chen
- **Model type:** Causal Language Model
- **License:** gemma
- **Finetuned from model:** [google/gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it)

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/princeton-nlp/SimPO
- **Paper:** https://arxiv.org/pdf/2405.14734


## How to Get Started with the Model
```
import torch
from transformers import pipeline

model_id = "princeton-nlp/gemma-2-9b-it-SimPO"

generator = pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="cuda",
)
outputs = generator([{"role": "user", "content": "What's the difference between llamas and alpacas?"}],
                      do_sample=False,
                      eos_token_id=[generator.tokenizer.convert_tokens_to_ids("<end_of_turn>"), generator.tokenizer.eos_token_id],
                      max_new_tokens=200)
print(outputs[0]['generated_text'])
```

## Training Details

### Training Data

We use [princeton-nlp/gemma2-ultrafeedback-armorm](https://huggingface.co/datasets/princeton-nlp/gemma2-ultrafeedback-armorm) as the preference optimization dataset.

#### Training Hyperparameters

The hyperparameters used can be found in the [training script](https://github.com/princeton-nlp/SimPO/blob/main/training_configs/gemma-2-9b-it-simpo.yaml).

#### Speeds, Sizes, Times

Fine-tuning the [google/gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it) on [princeton-nlp/gemma2-ultrafeedback-armorm](https://huggingface.co/datasets/princeton-nlp/gemma2-ultrafeedback-armorm) takes around 100 mins to finish on 8xH100 GPUs.

## Evaluation Results


|               models                    | AE2 LC | AE2 WR | AE2 Length |  AH  | AH Length |  GSM | GSM Length | MMLU | MMLU Length |
|-----------------------------------|:------:|:------:|:----------:|:----:|:---------:|:----:|:----------:|:----:|:-----------:|
|        [google/gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it)       |  51.1  |  38.1  |    1571    | 40.8 |    545    | 87.4 |     395    | 72.7 |     515     |
|  [princeton-nlp/gemma-2-9b-it-DPO](https://huggingface.co/princeton-nlp/gemma-2-9b-it-DPO)  |  67.8  |  65.4  |    2016    | 58.9 |    717    | 88.5 |     392    | 72.2 |     624     |
| [princeton-nlp/gemma-2-9b-it-SimPO](https://huggingface.co/princeton-nlp/gemma-2-9b-it-SimPO) |  72.4  |  65.9  |    1833    | 59.1 |    693    | 88.0 |     341    | 72.2 |     441     |


## Technical Specifications

### Model Architecture and Objective

The model architecture is based on [google/gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it). We use the SimPO training objective proposed in our [preprint](https://arxiv.org/pdf/2405.14734).

#### Hardware

We used 8xH100 GPUs for model training.

#### Software

Training was done using the [alignment-handbook](https://github.com/huggingface/alignment-handbook) library.

## Citation

gemma model:
```
@article{gemma_2024,
    title={Gemma},
    url={https://www.kaggle.com/m/3301},
    DOI={10.34740/KAGGLE/M/3301},
    publisher={Kaggle},
    author={Gemma Team},
    year={2024}
}
```

SimPO paper:
```
@article{meng2024simpo,
  title={{SimPO}: Simple preference optimization with a reference-free reward},
  author={Meng, Yu and Xia, Mengzhou and Chen, Danqi},
  journal={arXiv preprint arXiv:2405.14734},
  year={2024}
}
```

UltraFeedback paper:
```
@article{cui2023ultrafeedback,
  title={{UltraFeedback}: Boosting language models with high-quality feedback},
  author={Cui, Ganqu and Yuan, Lifan and Ding, Ning and Yao, Guanming and Zhu, Wei and Ni, Yuan and Xie, Guotong and Liu, Zhiyuan and Sun, Maosong},
  journal={arXiv preprint arXiv:2310.01377},
  year={2023}
}
```

ArmoRM paper:
```
@article{wang2024interpretable,
  title={Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts},
  author={Wang, Haoxiang and Xiong, Wei and Xie, Tengyang and Zhao, Han and Zhang, Tong},
  journal={arXiv preprint arXiv:2406.12845},
  year={2024}
}
```