---
license: apache-2.0
language:
- en
tags:
- moe
- olmo
- olmoe
co2_eq_emissions: 1
datasets:
- allenai/ultrafeedback_binarized_cleaned
base_model: allenai/OLMoE-1B-7B-0924-SFT
library_name: transformers
---

<img alt="OLMoE Logo." src="olmoe-logo.png" width="250px">

# Model Summary

> OLMoE-1B-7B-Instruct is a Mixture-of-Experts LLM with 1B active and 7B total parameters released in September 2024 (0924) that has been adapted via SFT and DPO from [OLMoE-1B-7B](https://hf.co/allenai/OLMoE-1B-7B-0924). It yields state-of-the-art performance among models with a similar cost (1B) and is competitive with much larger models like Llama2-13B-Chat. OLMoE is 100% open-source.

This information and more can also be found on the [**OLMoE GitHub repository**](https://github.com/allenai/OLMoE).
- **Paper**: https://arxiv.org/abs/2409.02060
- **Pretraining** [Checkpoints](https://hf.co/allenai/OLMoE-1B-7B-0924), [Code](https://github.com/allenai/OLMo/tree/Muennighoff/MoE), [Data](https://huggingface.co/datasets/allenai/OLMoE-mix-0924) and [Logs](https://wandb.ai/ai2-llm/olmoe/reports/OLMoE-1B-7B-0924--Vmlldzo4OTcyMjU3).
- **SFT (Supervised Fine-Tuning)** [Checkpoints](https://huggingface.co/allenai/OLMoE-1B-7B-0924-SFT), [Code](https://github.com/allenai/open-instruct/tree/olmoe-sft), [Data](https://hf.co/datasets/allenai/tulu-v3.1-mix-preview-4096-OLMoE) and [Logs](https://github.com/allenai/OLMoE/blob/main/logs/olmoe-sft-logs.txt).
- **DPO/KTO (Direct Preference Optimization/Kahneman-Tversky Optimization)**, [Checkpoints](https://huggingface.co/allenai/OLMoE-1B-7B-0924-Instruct), [Preference Data](https://hf.co/datasets/allenai/ultrafeedback_binarized_cleaned), [DPO code](https://github.com/allenai/open-instruct/tree/olmoe-sft), [KTO code](https://github.com/Muennighoff/kto/blob/master/kto.py) and [Logs](https://github.com/allenai/OLMoE/blob/main/logs/olmoe-dpo-logs.txt).

# Use

Install `transformers` **from source** until a release after [this PR](https://github.com/huggingface/transformers/pull/32406) & `torch` and run:

```python
from transformers import OlmoeForCausalLM, AutoTokenizer
import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load different ckpts via passing e.g. `revision=kto`
model = OlmoeForCausalLM.from_pretrained("allenai/OLMoE-1B-7B-0924-Instruct").to(DEVICE)
tokenizer = AutoTokenizer.from_pretrained("allenai/OLMoE-1B-7B-0924-Instruct")
messages = [{"role": "user", "content": "Explain to me like I'm five what is Bitcoin."}]
inputs = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt").to(DEVICE)
out = model.generate(inputs, max_length=100)
print(tokenizer.decode(out[0]))
"""
<|endoftext|><|user|>
Explain to me like I'm five what is Bitcoin.
<|assistant|>
Bitcoin is like a special kind of money that you can use to buy things online. But unlike regular money, like dollars or euros, Bitcoin isn't printed by governments or banks. Instead, it's created by a special computer program that helps people keep track of it.

Here's how it works: imagine you have a bunch of toys, and you want to
"""
```

Branches:
- `main`: Preference tuned via DPO model of https://hf.co/allenai/OLMoE-1B-7B-0924-SFT (`main` branch)
- `load-balancing`: Ablation with load balancing loss during DPO starting from the `load-balancing` branch of https://hf.co/allenai/OLMoE-1B-7B-0924-SFT
- `non-annealed`: Ablation starting from the `non-annealed` branch of https://hf.co/allenai/OLMoE-1B-7B-0924-SFT which is an SFT of the pretraining checkpoint prior to annealing (branch `step1200000-tokens5033B` of https://hf.co/allenai/OLMoE-1B-7B-0924)
- `kto`: Ablation using KTO instead of DPO. This branch is the checkpoint after 5,000 steps with the RMS optimizer. The other `kto*` branches correspond to the other checkpoints mentioned in the paper.

# Evaluation Snapshot

| Task (→)      | MMLU | GSM8k | BBH  | Human-Eval | Alpaca-Eval 1.0 | XSTest | IFEval | Avg  |
|---------------|------|-------|------|------------|-----------------|--------|--------|------|
| **Setup (→)**     | 0-shot | 8-shot CoT | 3-shot | 0-shot | 0-shot | 0-shot | 0-shot |      |
| **Metric (→)**    | EM   | EM    | EM   | Pass@10    | %win            | F1     | Loose Acc |      |
|  |     |      |     |      |              |       |   |      |
| OLMo-1B (0724) | 25.0 | 7.0   | 22.5 | 16.0       | -               | 67.6   | 20.5   | -    |
| +SFT          | 36.0 | 12.5  | 27.2 | 21.2       | 41.5            | 81.9   | 26.1   | 35.9 |
| +DPO          | 36.7 | 12.5  | 30.6 | 22.0       | 50.9            | 79.8   | 24.2   | 37.4 |
| OLMo-7B (0724) | 50.8 | 32.5  | 36.9 | 32.3       | -               | 80.8   | 19.6   | -    |
| +SFT          | 54.2 | 25.0  | 35.7 | 38.5       | 70.9            | 86.1   | 39.7   | 49.3 |
| +DPO          | 52.8 | 9.0   | 16.6 | 35.0       | 83.5            | **87.5** | 37.9   | 49.1 |
| JetMoE-2B-9B  | 45.6 | 43.0  | 37.2 | 54.6       | -               | 68.2   | 20.0   | -    |
| +SFT          | 46.1 | 53.5  | 35.6 | 64.8       | 69.3            | 55.6   | 30.5   | 50.4 |
| DeepSeek-3B-16B | 37.7 | 18.5  | 39.4 | 48.3       | -               | 65.9   | 13.5   | -    |
| +Chat         | 48.5 | 46.5  | **40.8** | **70.1** | 74.8            | 85.6   | 32.3   | 57.0 |
| Qwen1.5-3B-14B | **60.4** | 13.5  | 27.2 | 60.2       | -               | 73.4   | 20.9   | -    |
| +Chat         | 58.9 | **55.5** | 21.3 | 59.7       | 83.9            | 85.6   | 36.2   | 57.3 |
| **OLMoE (This Model)**      | 49.8 | 3.0   | 33.6 | 22.4       | -               | 59.7   | 16.6   | -    |
| **+SFT**      | 51.4 | 40.5  | 38.0 | 51.6       | 69.2            | 84.1   | 43.3   | 54.0 |
| **+DPO**      | 51.9 | 45.5  | 37.0 | 54.8       | **84.0**         | 82.6   | **48.1** | **57.7** |

# Citation

```bibtex
@misc{muennighoff2024olmoeopenmixtureofexpertslanguage,
      title={OLMoE: Open Mixture-of-Experts Language Models}, 
      author={Niklas Muennighoff and Luca Soldaini and Dirk Groeneveld and Kyle Lo and Jacob Morrison and Sewon Min and Weijia Shi and Pete Walsh and Oyvind Tafjord and Nathan Lambert and Yuling Gu and Shane Arora and Akshita Bhagia and Dustin Schwenk and David Wadden and Alexander Wettig and Binyuan Hui and Tim Dettmers and Douwe Kiela and Ali Farhadi and Noah A. Smith and Pang Wei Koh and Amanpreet Singh and Hannaneh Hajishirzi},
      year={2024},
      eprint={2409.02060},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2409.02060}, 
}
```