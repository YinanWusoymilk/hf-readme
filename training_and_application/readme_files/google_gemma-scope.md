---
license: cc-by-4.0
library_name: saelens
---

# Gemma Scope:

![](gemma_scope.gif)

This is a landing page for **Gemma Scope**, a comprehensive, open suite of sparse autoencoders for Gemma 2 9B and 2B. Sparse Autoencoders are a "microscope" of sorts that can help us break down a model’s internal activations into the underlying concepts, just as biologists use microscopes to study the individual cells of plants and animals.

**There are no model weights in this repo. If you are looking for them, please visit one of our repos:**

- https://huggingface.co/google/gemma-scope-2b-pt-res
- https://huggingface.co/google/gemma-scope-2b-pt-mlp
- https://huggingface.co/google/gemma-scope-2b-pt-att
- https://huggingface.co/google/gemma-scope-9b-pt-res
- https://huggingface.co/google/gemma-scope-9b-pt-mlp
- https://huggingface.co/google/gemma-scope-9b-pt-att
- https://huggingface.co/google/gemma-scope-27b-pt-res
- https://huggingface.co/google/gemma-scope-9b-it-res
- https://huggingface.co/google/gemma-scope-2b-pt-transcoders

[This tutorial](https://colab.research.google.com/drive/17dQFYUYnuKnP6OwQPH9v_GSYUW5aj-Rp?ts=66a77041) has instructions on how to load the SAEs, and [this tutorial](https://colab.research.google.com/drive/1PlFzI_PWGTN9yCQLuBcSuPJUjgHL7GiD) explains and implements JumpReLU SAE training in PyTorch and JAX.

# Key links:

![](gs-demo-tweet.gif)
- Check out the [interactive Gemma Scope demo](https://www.neuronpedia.org/gemma-scope) made by [Neuronpedia](https://www.neuronpedia.org/).
- (NEW!) We have a colab notebook tutorial for JumpReLU SAE training in JAX and PyTorch [here](https://colab.research.google.com/drive/1PlFzI_PWGTN9yCQLuBcSuPJUjgHL7GiD).
- Learn more about Gemma Scope in our [Google DeepMind blog post](https://deepmind.google/discover/blog/gemma-scope-helping-the-safety-community-shed-light-on-the-inner-workings-of-language-models).
- Check out our [Google Colab notebook tutorial](https://colab.research.google.com/drive/17dQFYUYnuKnP6OwQPH9v_GSYUW5aj-Rp?ts=66a77041) for how to use Gemma Scope.
- Read [the Gemma Scope technical report](https://arxiv.org/abs/2408.05147).
- Check out [Mishax](https://github.com/google-deepmind/mishax), a GDM internal tool that we used in this project to expose the internal activations inside Gemma 2 models.

# Full weight set:

The full list of SAEs we trained at which sites and layers are linked from the following table, adapted from Figure 1 of our technical report:

| <big>Gemma 2 Model</big> | <big>SAE Width</big> | <big>Attention</big> | <big>MLP</big> | <big>Residual</big> | <big>Tokens</big> |
|---------------|-----------|-----------|-----|----------|----------|
| 2.6B PT<br>(26 layers) | 2^14 ≈ 16.4K | [All](https://huggingface.co/google/gemma-scope-2b-pt-att) | [All](https://huggingface.co/google/gemma-scope-2b-pt-mlp) | [All](https://huggingface.co/google/gemma-scope-2b-pt-res)[+](https://huggingface.co/google/gemma-scope-2b-pt-transcoders) | 4B |
| | 2^15 |  |  | {[12](https://huggingface.co/google/gemma-scope-2b-pt-res/tree/main/layer_12/width_32k/)} | 8B |
| | 2^16 | [All](https://huggingface.co/google/gemma-scope-2b-pt-att) | [All](https://huggingface.co/google/gemma-scope-2b-pt-mlp) | [All](https://huggingface.co/google/gemma-scope-2b-pt-res) | 8B |
| | 2^17 |  |  | {[12](https://huggingface.co/google/gemma-scope-2b-pt-res/tree/main/layer_12/width_131k/)} | 8B |
| | 2^18 |  |  | {[12](https://huggingface.co/google/gemma-scope-2b-pt-res/tree/main/layer_12/width_262k/)} | 8B |
| | 2^19 |  |  | {[12](https://huggingface.co/google/gemma-scope-2b-pt-res/tree/main/layer_12/width_524k/)} | 8B |
| | 2^20 ≈ 1M |  |  | {[5](https://huggingface.co/google/gemma-scope-2b-pt-res/tree/main/layer_5/width_1m/), [12](https://huggingface.co/google/gemma-scope-2b-pt-res/tree/main/layer_12/width_1m/), [19](https://huggingface.co/google/gemma-scope-2b-pt-res/tree/main/layer_19/width_1m/)} | 16B |
| 9B PT<br>(42 layers) | 2^14 | [All](https://huggingface.co/google/gemma-scope-9b-pt-att) | [All](https://huggingface.co/google/gemma-scope-9b-pt-mlp) | [All](https://huggingface.co/google/gemma-scope-9b-pt-res) | 4B |
| | 2^15 |  |  | {[20](https://huggingface.co/google/gemma-scope-9b-pt-res/tree/main/layer_20/width_32k/)} | 8B |
| | 2^16 |  |  | {[20](https://huggingface.co/google/gemma-scope-9b-pt-res/tree/main/layer_20/width_65k/)} | 8B |
| | 2^17 | [All](https://huggingface.co/google/gemma-scope-9b-pt-att) | [All](https://huggingface.co/google/gemma-scope-9b-pt-mlp) | [All](https://huggingface.co/google/gemma-scope-9b-pt-res) | 8B |
| | 2^18 |  |  | {[20](https://huggingface.co/google/gemma-scope-9b-pt-res/tree/main/layer_20/width_262k/)} | 8B |
| | 2^19 |  |  | {[20](https://huggingface.co/google/gemma-scope-9b-pt-res/tree/main/layer_20/width_524k/)} | 8B |
| | 2^20 |  |  | {[9](https://huggingface.co/google/gemma-scope-9b-pt-res/tree/main/layer_9/width_1m/), [20](https://huggingface.co/google/gemma-scope-9b-pt-res/tree/main/layer_20/width_1m/), [31](https://huggingface.co/google/gemma-scope-9b-pt-res/tree/main/layer_31/width_1m/)} | 16B |
| 27B PT<br>(46 layers) | 2^17 |  |  | {[10](https://huggingface.co/google/gemma-scope-27b-pt-res/tree/main/layer_10/width_131k/), [22](https://huggingface.co/google/gemma-scope-27b-pt-res/tree/main/layer_22/width_131k/), [34](https://huggingface.co/google/gemma-scope-27b-pt-res/tree/main/layer_34/width_131k/)} | 8B |
| 9B IT<br>(42 layers) | 2^14 |  |  | {[9](https://huggingface.co/google/gemma-scope-9b-it-res/tree/main/layer_9/width_16k/), [20](https://huggingface.co/google/gemma-scope-9b-it-res/tree/main/layer_20/width_16k/), [31](https://huggingface.co/google/gemma-scope-9b-it-res/tree/main/layer_31/width_16k/)} | 4B |
| | 2^17 |  |  | {[9](https://huggingface.co/google/gemma-scope-9b-it-res/tree/main/layer_9/width_131k/), [20](https://huggingface.co/google/gemma-scope-9b-it-res/tree/main/layer_20/width_131k/), [31](https://huggingface.co/google/gemma-scope-9b-it-res/tree/main/layer_31/width_131k/)} | 8B |

# Which SAE is in the [Neuronpedia demo](https://www.neuronpedia.org/gemma-scope)?

https://huggingface.co/google/gemma-scope-2b-pt-res/tree/main/layer_20/width_16k/average_l0_71

# Citation

```
@misc{lieberum2024gemmascopeopensparse,
      title={Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2}, 
      author={Tom Lieberum and Senthooran Rajamanoharan and Arthur Conmy and Lewis Smith and Nicolas Sonnerat and Vikrant Varma and János Kramár and Anca Dragan and Rohin Shah and Neel Nanda},
      year={2024},
      eprint={2408.05147},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2408.05147}, 
}
```

Paper link: https://arxiv.org/abs/2408.05147
