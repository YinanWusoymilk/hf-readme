---
datasets:
- Yukang/LongAlpaca-16k-length
---

This is an extended (16K) context version of LLaMA 3 8B (base, not instruct). Trained for five hours on 8x A6000 GPUs, using the `Yukang/LongAlpaca-16k-length` dataset.

`rope_theta` was set to `1000000.0`. Trained with Axolotl.