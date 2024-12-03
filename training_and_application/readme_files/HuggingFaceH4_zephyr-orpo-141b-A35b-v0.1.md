---
license: apache-2.0
base_model: mistral-community/Mixtral-8x22B-v0.1
tags:
- trl
- orpo
- generated_from_trainer
datasets:
- argilla/distilabel-capybara-dpo-7k-binarized
model-index:
- name: zephyr-orpo-141b-A35b-v0.1
  results: []
inference:
  parameters:
    temperature: 0.7
---

<img src="https://huggingface.co/HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1/resolve/main/logo.png" alt="Zephyr 141B Logo" width="400" style="margin-left:'auto' margin-right:'auto' display:'block'"/>


# Model Card for Zephyr 141B-A39B

Zephyr is a series of language models that are trained to act as helpful assistants. Zephyr 141B-A39B is the latest model in the series, and is a fine-tuned version of [mistral-community/Mixtral-8x22B-v0.1](https://huggingface.co/mistral-community/Mixtral-8x22B-v0.1) that was trained using a novel alignment algorithm called [Odds Ratio Preference Optimization (ORPO)](https://huggingface.co/papers/2403.07691) with **7k instances** for **1.3 hours** on 4 nodes of 8 x H100s. ORPO does not require an SFT step to achieve high performance and is thus much more computationally efficient than methods like DPO and PPO. To train Zephyr-141B-A39B, we used the [`argilla/distilabel-capybara-dpo-7k-binarized`](https://huggingface.co/datasets/argilla/distilabel-capybara-dpo-7k-binarized) preference dataset, which consists of synthetic, high-quality, multi-turn preferences that have been scored via LLMs.

> [!NOTE]
> This model was trained collaboratively between Argilla, KAIST, and Hugging Face

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Model type:** A Mixture of Experts (MoE) model with 141B total parameters and 39B active parameters. (We initially made a small error in calculating the number of active parameters for the model ID. The model card states the correct number.) Fine-tuned on a mix of publicly available, synthetic datasets.
- **Language(s) (NLP):** Primarily English.
- **License:** Apache 2.0
- **Finetuned from model:** [mistral-community/Mixtral-8x22B-v0.1](https://huggingface.co/mistral-community/Mixtral-8x22B-v0.1)

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/huggingface/alignment-handbook
- **Dataset:** https://huggingface.co/datasets/argilla/distilabel-capybara-dpo-7k-binarized

## Performance

Zephyr 141B-A39B was trained to test the effectiveness of ORPO at scale and the underlying dataset contains a mix of general chat capabilities. It achieves strong performance on chat benchmarks like [MT Bench](https://huggingface.co/spaces/lmsys/mt-bench) and [IFEval](https://arxiv.org/abs/2311.07911). The scores reported below were obtained using the [LightEval](https://github.com/huggingface/lighteval) evaluation suite and each prompt has been formatted with the model's corresponding chat template to simulate real-world usage. This is why some scores may differ from those reported in technical reports or on the Open LLM Leaderboard. 

| Model                                                                                               | MT Bench | IFEval |   BBH | AGIEval |
|-----------------------------------------------------------------------------------------------------|---------:|-------:|------:|--------:|
| [zephyr-orpo-141b-A39b-v0.1](https://huggingface.co/HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1)       |     8.17 |  65.06 | 58.96 |   44.16 |
| [databricks/dbrx-instruct](https://huggingface.co/databricks/dbrx-instruct)                         |     8.26 |  52.13 | 48.50 |   41.16 |
| [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) |     8.30 |  55.08 | 45.31 |   47.68 |


## Intended uses & limitations

The model was fine-tuned on a blend of chat, code, math, and reasoning data. Here's how you can run the model using the `pipeline()` function from 🤗 Transformers:

```python
# pip install 'transformers>=4.39.3'
# pip install accelerate

import torch
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1",
    device_map="auto",
    torch_dtype=torch.bfloat16,
)
messages = [
    {
        "role": "system",
        "content": "You are Zephyr, a helpful assistant.",
    },
    {"role": "user", "content": "Explain how Mixture of Experts work in language a child would understand."},
]
outputs = pipe(
    messages,
    max_new_tokens=512,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95,
)
print(outputs[0]["generated_text"][-1]["content"])
```

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

Zephyr 141B-A39B has not been aligned to human preferences for safety within the RLHF phase or deployed with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). 
It is also unknown what the size and composition of the corpus was used to train the base model (`mistral-community/Mixtral-8x22B-v0.1`), however it is likely to have included a mix of Web data and technical sources like books and code. See the [Falcon 180B model card](https://huggingface.co/tiiuae/falcon-180B#training-data) for an example of this.


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 32
- total_train_batch_size: 32
- total_eval_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: inverse_sqrt
- lr_scheduler_warmup_steps: 100
- num_epochs: 3


### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2+cu121
- Datasets 2.18.0
- Tokenizers 0.15.1

## Citation

If you find Zephyr 141B-A39B is useful in your work, please cite the ORPO paper:

```
@misc{hong2024orpo,
      title={ORPO: Monolithic Preference Optimization without Reference Model}, 
      author={Jiwoo Hong and Noah Lee and James Thorne},
      year={2024},
      eprint={2403.07691},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

You may also wish to cite the creators of this model:

```
@misc{zephyr_141b,
  author = {Alvaro Bartolome and Jiwoo Hong and Noah Lee and Kashif Rasul and Lewis Tunstall},
  title = {Zephyr 141B A39B},
  year = {2024},
  publisher = {Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\url{https://huggingface.co/HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1}}
}
```