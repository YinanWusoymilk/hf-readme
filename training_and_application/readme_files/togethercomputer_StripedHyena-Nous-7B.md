---
license: apache-2.0
language:
- en
---

## StripedHyena-Nous-7B (SH-N 7B)

<p align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/62a1306bbe7fa896d2c8de44/Bfjh77emDsWOY-VmfvU9C.png" width="60%" />
</p>

### About 

One of the focus areas at Together Research is new architectures for long context, improved training, and inference performance over the Transformer architecture. Spinning out of a research program from our team and academic collaborators, with roots in **signal processing-inspired sequence models**, we are excited to introduce the **StripedHyena** models. StripedHyena is the **first alternative model competitive with the best open-source Transformers** of similar sizes in short and long-context evaluations.

**StripedHyena-Nous-7B (SH-N 7B)** is our **chat model** for this release, and was developed with our collaborators at [Nous Research](https://nousresearch.com/).

- Read more here in [our blog](https://www.together.ai/blog/stripedhyena-7b).
- Play with the model on our [playground](https://api.together.xyz/playground/chat/togethercomputer/StripedHyena-Nous-7B)!
- Dive into the details of our [standalone implementation](https://github.com/togethercomputer/stripedhyena), and our related research: [1](https://arxiv.org/abs/2302.10866), [2](https://arxiv.org/abs/2310.18780), [3](https://arxiv.org/abs/2311.05908).

### Model Architecture

StripedHyena is a hybrid architecture composed of multi-head, grouped-query attention and gated convolutions arranged in [Hyena](https://arxiv.org/abs/2302.10866) blocks, different from traditional decoder-only Transformers.  
  - Costant memory decoding in Hyena blocks via representation of convolutions as state-space models (modal or canonical form), or as truncated filters.
  - Low latency, faster decoding and higher throughput than Transformers. 
  - Improvement to training and inference-optimal scaling laws, compared to optimized Transformer architectures such as Llama-2.
  - Trained on sequences of up to 32k, allowing it to process longer prompts.

### Prompt Format

StripedHyena-Nous 7B uses this prompt format:

```
### Instruction:\n{prompt}\n\n### Response:\n{response}
```

### Disclaimer 

To use StripedHyena outside of the playground, you will need to install custom kernels. Please follow the instructions from the [standalone repository](https://github.com/togethercomputer/stripedhyena).

StripedHyena is a mixed precision model. Make sure to keep your `poles` and `residues` in `float32` precision, especially for longer prompts or training.


## Cite

If you have found the pretrained models or architecture useful for you research or application, consider citing: 
```
@software{stripedhyena,
  title        = {{StripedHyena: Moving Beyond Transformers with Hybrid Signal Processing Models}},
  author       = { Poli, Michael and Wang, Jue and Massaroli, Stefano and Quesnelle, Jeffrey and Carlow, Ryan and Nguyen, Eric and Thomas, Armin},
  month        = 12,
  year         = 2023,
  url          = { https://github.com/togethercomputer/stripedhyena },
  doi          = { 10.57967/hf/1595 },
}
```