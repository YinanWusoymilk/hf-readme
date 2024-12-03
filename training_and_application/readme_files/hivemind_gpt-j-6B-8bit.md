---
language:
- en
tags:
- pytorch
- causal-lm
license: apache-2.0
datasets:
- The Pile

---

Note: this model was superceded by the [`load_in_8bit=True` feature in transformers](https://github.com/huggingface/transformers/pull/17901)
by Younes Belkada and Tim Dettmers. Please see [this usage example](https://colab.research.google.com/drive/1qOjXfQIAULfKvZqwCen8-MoWKGdSatZ4#scrollTo=W8tQtyjp75O).
This legacy model was built for [transformers v4.15.0](https://github.com/huggingface/transformers/releases/tag/v4.15.0) and pytorch 1.11. Newer versions could work, but are not supported.


### Quantized EleutherAI/gpt-j-6b with 8-bit weights

This is a version of EleutherAI's GPT-J with 6 billion parameters that is modified so you can generate **and fine-tune the model in colab or equivalent desktop gpu (e.g. single 1080Ti)**.

Here's how to run it: [![colab](https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/drive/1ft6wQU0BhqG5PRlwgaZJv2VukKKjU4Es)

__The [original GPT-J](https://huggingface.co/EleutherAI/gpt-j-6B/tree/main)__ takes 22+ GB memory for float32 parameters alone, and that's before you account for gradients & optimizer. Even if you cast everything to 16-bit, it will still not fit onto most single-GPU setups short of A6000 and A100. You can inference it [on TPU](https://colab.research.google.com/github/kingoflolz/mesh-transformer-jax/blob/master/colab_demo.ipynb) or CPUs, but fine-tuning is way more expensive.

Here, we apply several techniques to make GPT-J usable and fine-tunable on a single GPU with ~11 GB memory:
- large weight tensors are quantized using dynamic 8-bit quantization and de-quantized just-in-time for multiplication
- using gradient checkpoints to store one only activation per layer: using dramatically less memory at the cost of 30% slower training
- scalable fine-tuning with [LoRA](https://arxiv.org/abs/2106.09685) and [8-bit Adam](https://arxiv.org/abs/2110.02861)

In other words, all of the large weight-matrices are frozen in 8-bit, and you only train small adapters and optionally 1d tensors (layernorm scales, biases).

![img](https://i.imgur.com/n4XXo1x.png)


__Does 8-bit affect model quality?__ Technically yes, but the effect is negligible in practice. [This notebook measures wikitext test perplexity](https://nbviewer.org/urls/huggingface.co/hivemind/gpt-j-6B-8bit/raw/main/check_perplexity.ipynb) and it is nigh indistinguishable from the original GPT-J. Quantized model is even slightly better, but that is not statistically significant.

Our code differs from other 8-bit methods in that we use **8-bit only for storage, and all computations are performed in float16 or float32**. As a result, we can take advantage of nonlinear quantization that fits to each individual weight distribution. Such nonlinear quantization does not accelerate inference, but it allows for much smaller error.


__What about performance?__ Both checkpointing and de-quantization has some overhead, but it's surprisingly manageable. Depending on GPU and batch size, the quantized model is 1-10% slower than the original model on top of using gradient checkpoints (which is 30% overhead). In short, this is because block-wise quantization from bitsandbytes is really fast on GPU.


### How should I fine-tune the model?

We recommend starting with the original hyperparameters from [the LoRA paper](https://arxiv.org/pdf/2106.09685.pdf).
On top of that, there is one more trick to consider: the overhead from de-quantizing weights does not depend on batch size.
As a result, the larger batch size you can fit, the more efficient you will train.


### Where can I train for free?

You can train fine in colab, but if you get a K80, it's probably best to switch to other free gpu providers: [kaggle](https://towardsdatascience.com/amazon-sagemaker-studio-lab-a-great-alternative-to-google-colab-7194de6ef69a), [aws sagemaker](https://towardsdatascience.com/amazon-sagemaker-studio-lab-a-great-alternative-to-google-colab-7194de6ef69a) or [paperspace](https://docs.paperspace.com/gradient/more/instance-types/free-instances). For intance, this is the same notebook [running in kaggle](https://www.kaggle.com/justheuristic/dmazur-converted) using a more powerful P100 instance.


### Can I use this technique with other models?

The model was converted using [this notebook](https://nbviewer.org/urls/huggingface.co/hivemind/gpt-j-6B-8bit/raw/main/convert-gpt-j.ipynb). It can be adapted to work with other model types. However, please bear in mind that some models replace Linear and Embedding with custom alternatives that require their own BNBWhateverWithAdapters.

