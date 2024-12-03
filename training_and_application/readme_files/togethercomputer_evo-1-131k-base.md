---
license: apache-2.0
tags:
- stripedhyena
- long context
- deep signal processing
- hybrid
- biology
- genomics
---


## Evo-1 (Phase 2)

<p align="center">
<img src="https://cdn-uploads.huggingface.co/production/uploads/62a1306bbe7fa896d2c8de44/JoEHcvLTUlHoMcgh3mmAz.png" width="70%" />
</p>

### News

We identified and fixed an issue related to a wrong permutation of some projections, which affects generation quality. To use the new model revision, please load as follows:

```python
config = AutoConfig.from_pretrained(model_name, trust_remote_code=True, revision="1.1_fix")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    config=config,
    trust_remote_code=True,
    revision="1.1_fix"
)
```

### About 

Evo is a biological foundation model capable of long-context modeling and design.

Evo uses the [StripedHyena architecture](https://github.com/togethercomputer/stripedhyena) to enable modeling of sequences at a single-nucleotide, byte-level resolution with near-linear scaling of compute and memory relative to context length.
Evo has 7 billion parameters and is trained on OpenGenome, a prokaryotic whole-genome dataset containing ~300 billion tokens.

Technical details about Evo can be found in our preprint and our accompanying blog posts. Evo was collaboratively developed by the [Arc Institute](https://arcinstitute.org/) and TogetherAI.

As part of our commitment to open science, we release **weights of 15 intermediate pretraining checkpoints** for phase 1 and phase 2 of pretraining. The checkpoints are available as branches of the corresponding HuggingFace repository.

**Evo-1 (Phase 2)** is our **longer context model** in the Evo family, trained at a context length of 131k and tested on generation of sequences of length >650k

| Checkpoint Name                        | Description |
|----------------------------------------|-------------|
| `evo-1-8k-base`     | A model pretrained with 8,192 context. We use this model as the base model for molecular-scale finetuning tasks. |
| `evo-1-131k-base`   | A model pretrained with 131,072 context using `evo-1-8k-base` as the initialization. We use this model to reason about and generate sequences at the genome scale. |

### Model Architecture

StripedHyena is a deep signal processing, hybrid architecture composed of multi-head attention and gated convolutions arranged in [Hyena](https://arxiv.org/abs/2302.10866) blocks, improving over decoder-only Transformers.  

StripedHyena is designed to leverage the specialization of each of its layer classes, with Hyena layers implementing the bulk of the computation required for sequence processing and attention layers supplementing the ability to perform targeted pattern recall.


Some highlights of the architecture:
- **Efficient autoregressive generation** via a recurrent mode (>500k generation with a single 80GB GPU)
- **Significantly faster training and finetuning** at long context (>3x at 131k)
- **Improved scaling laws over state-of-the-art architectures** (e.g., Transformer++) on both natural language and biological sequences.
- **Robust to training beyond the compute-optimal frontier** e.g., training way beyond Chinchilla-optimal token amounts (see preprint for details -- more details to come)


### How to use Evo

Example usage is provided in the [standalone repo](https://github.com/evo-design/evo).


#### Parametrization for Inference and Finetuning

One of the advantages of deep signal processing models is their flexibility. Different parametrizations of convolutions can be used depending on the memory, expressivity and causality requirements of pretraining, finetuning or inference workloads. 

The main classes are:
- Modal canonical: unconstrained poles ([reference](https://arxiv.org/pdf/2203.14343.pdf), [reference](https://arxiv.org/abs/2310.18780)), or constrained poles ([reference](https://arxiv.org/abs/2206.11893), [reference](https://arxiv.org/pdf/2303.06349.pdf)).
- Companion canonical / rational: TBA.
- Hypernetworks: hypernetwork ([reference](https://arxiv.org/abs/2102.02611)), modulated hypernetwork ([reference](https://arxiv.org/abs/2302.10866)).
- Explicit: modulated explicit ([reference](https://arxiv.org/pdf/2210.09298.pdf)).

StripedHyena is a mixed precision model. Make sure to keep your `poles` and `residues` in `float32` precision, especially for longer prompts or training.



### Disclaimer 

To use StripedHyena outside of the playground, you will need to install custom kernels. Please follow the instructions from the [standalone repository](https://github.com/togethercomputer/stripedhyena).

## Cite

```
@article{nguyen2024sequence,
   author = {Eric Nguyen and Michael Poli and Matthew G. Durrant and Armin W. Thomas and Brian Kang and Jeremy Sullivan and Madelena Y. Ng and Ashley Lewis and Aman Patel and Aaron Lou and Stefano Ermon and Stephen A. Baccus and Tina Hernandez-Boussard and Christopher Ré and Patrick D. Hsu and Brian L. Hie},
   journal = {Arc Institute manuscripts},
   title = {Sequence modeling and design from molecular to genome scale with Evo},
   url = {https://arcinstitute.org/manuscripts/Evo},
   year = {2024},
}
```