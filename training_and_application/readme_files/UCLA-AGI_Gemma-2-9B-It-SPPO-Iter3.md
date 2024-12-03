---
license: gemma
datasets:
- openbmb/UltraFeedback
language:
- en
pipeline_tag: text-generation
---
Self-Play Preference Optimization for Language Model Alignment (https://arxiv.org/abs/2405.00675)

# Gemma-2-9B-It-SPPO-Iter3

This model was developed using [Self-Play Preference Optimization](https://arxiv.org/abs/2405.00675) at iteration 3, based on the [google/gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it) architecture as starting point. We utilized the prompt sets from the [openbmb/UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback) dataset, splited to 3 parts for 3 iterations by [snorkelai/Snorkel-Mistral-PairRM-DPO-Dataset](https://huggingface.co/datasets/snorkelai/Snorkel-Mistral-PairRM-DPO-Dataset). All responses used are synthetic.

**Terms of Use**: [Terms](https://www.kaggle.com/models/google/gemma/license/consent/verify/huggingface?returnModelRepoId=google/gemma-2-9b-it)


## Links to Other Models
- [Gemma-2-9B-It-SPPO-Iter1](https://huggingface.co/UCLA-AGI/Gemma-2-9B-It-SPPO-Iter1)
- [Gemma-2-9B-It-SPPO-Iter2](https://huggingface.co/UCLA-AGI/Gemma-2-9B-It-SPPO-Iter2)
- [Gemma-2-9B-It-SPPO-Iter3](https://huggingface.co/UCLA-AGI/Gemma-2-9B-It-SPPO-Iter3)

### Model Description

- Model type: A 8B parameter GPT-like model fine-tuned on synthetic datasets.
- Language(s) (NLP): Primarily English
- License: Apache-2.0
- Finetuned from model: google/gemma-2-9b-it


## [AlpacaEval Leaderboard Evaluation Results](https://tatsu-lab.github.io/alpaca_eval/)


|                Model                           | LC. Win Rate | Win Rate | Avg. Length |
|-------------------------------------------|:------------:|:--------:|:-----------:|
|[Gemma-2-9B-SPPO Iter1](https://huggingface.co/UCLA-AGI/Gemma-2-9B-It-SPPO-Iter1) |48.70 |40.76 | 1669
|[Gemma-2-9B-SPPO Iter2](https://huggingface.co/UCLA-AGI/Gemma-2-9B-It-SPPO-Iter2) |50.93 | 44.64 | 1759
|[Gemma-2-9B-SPPO Iter3](https://huggingface.co/UCLA-AGI/Gemma-2-9B-It-SPPO-Iter3) |**53.27** |**47.74** | 1803






### Training hyperparameters
The following hyperparameters were used during training:

- learning_rate: 5e-07
- eta: 1000
- per_device_train_batch_size: 8
- gradient_accumulation_steps: 1
- seed: 42
- distributed_type: deepspeed_zero3
- num_devices: 8
- optimizer: RMSProp 
- lr_scheduler_type: linear 
- lr_scheduler_warmup_ratio: 0.1
- num_train_epochs: 1.0



  
## Citation
```
@misc{wu2024self,
      title={Self-Play Preference Optimization for Language Model Alignment}, 
      author={Wu, Yue and Sun, Zhiqing and Yuan, Huizhuo and Ji, Kaixuan and Yang, Yiming and Gu, Quanquan},
      year={2024},
      eprint={2405.00675},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```

