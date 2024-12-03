---
license: other
datasets:
- tiiuae/falcon-refinedweb
- togethercomputer/RedPajama-Data-1T
- uonlp/CulturaX
- CarperAI/pilev2-dev
- bigcode/starcoderdata
- DataProvenanceInitiative/Commercially-Verified-Licenses
language:
- en
- de
- es
- fr
- it
- nl
- pt
tags:
- causal-lm
---
# `Stable LM 2 1.6B`

Please note: For commercial use, please refer to https://stability.ai/license

## Model Description

`Stable LM 2 1.6B` is a 1.6 billion parameter decoder-only language model pre-trained on 2 trillion tokens of diverse multilingual and code datasets for two epochs.

## Usage

Get started generating text with `Stable LM 2 1.6B` by using the following code snippet:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablelm-2-1_6b")
model = AutoModelForCausalLM.from_pretrained(
  "stabilityai/stablelm-2-1_6b",
  torch_dtype="auto",
)
model.cuda()
inputs = tokenizer("The weather is always wonderful", return_tensors="pt").to(model.device)
tokens = model.generate(
  **inputs,
  max_new_tokens=64,
  temperature=0.70,
  top_p=0.95,
  do_sample=True,
)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))
```

### Run with Flash Attention 2 ⚡️

<details>
<summary> Click to expand </summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablelm-2-1_6b")
model = AutoModelForCausalLM.from_pretrained(
  "stabilityai/stablelm-2-1_6b",
  torch_dtype="auto",
  attn_implementation="flash_attention_2",
)
model.cuda()
inputs = tokenizer("The weather is always wonderful", return_tensors="pt").to(model.device)
tokens = model.generate(
  **inputs,
  max_new_tokens=64,
  temperature=0.70,
  top_p=0.95,
  do_sample=True,
)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))
```

</details>


## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: `Stable LM 2 1.6B` models are auto-regressive language models based on the transformer decoder architecture.
* **Language(s)**: English
* **Paper**: [Stable LM 2 1.6B Technical Report](https://drive.google.com/file/d/1JYJHszhS8EFChTbNAf8xmqhKjogWRrQF/view?usp=sharing)
* **Library**: [GPT-NeoX](https://github.com/EleutherAI/gpt-neox)
* **License**: [Stability AI Community License](https://huggingface.co/stabilityai/stablelm-2-1_6b/blob/main/LICENSE.md).
* **Commercial License**: to use this model commercially, please refer to https://stability.ai/license
* **Contact**: For questions and comments about the model, please email `lm@stability.ai`

### Model Architecture

The model is a decoder-only transformer similar to the LLaMA ([Touvron et al., 2023](https://arxiv.org/abs/2307.09288)) architecture with the following modifications:

| Parameters     | Hidden Size | Layers | Heads | Sequence Length |
|----------------|-------------|--------|-------|-----------------|
| 1,644,417,024  | 2048        | 24     | 32    | 4096            |

* **Position Embeddings**: Rotary Position Embeddings ([Su et al., 2021](https://arxiv.org/abs/2104.09864)) applied to the first 25% of head embedding dimensions for improved throughput following [Black et al. (2022)](https://arxiv.org/pdf/2204.06745.pdf).
* **Normalization**: LayerNorm ([Ba et al., 2016](https://arxiv.org/abs/1607.06450)) with learned bias terms as opposed to RMSNorm ([Zhang & Sennrich, 2019](https://arxiv.org/abs/1910.07467)).
* **Biases**: We remove all bias terms from the feed-forward networks and multi-head self-attention layers, except for the biases of the query, key, and value projections ([Bai et al., 2023](https://arxiv.org/abs/2309.16609)).
* **Tokenizer**: We use Arcade100k, a BPE tokenizer extended from OpenAI's [`tiktoken.cl100k_base`](https://github.com/openai/tiktoken). We split digits into individual tokens following findings by [Liu & Low (2023)](https://arxiv.org/abs/2305.14201).

## Training

### Training Dataset

The dataset is comprised of a filtered mixture of open-source large-scale datasets available on the [HuggingFace Hub](https://huggingface.co/datasets): Falcon RefinedWeb extract ([Penedo et al., 2023](https://huggingface.co/datasets/tiiuae/falcon-refinedweb)), RedPajama-Data ([Together Computer., 2023](https://github.com/togethercomputer/RedPajama-Data)) and The Pile ([Gao et al., 2020](https://arxiv.org/abs/2101.00027)) both without the *Books3* subset, and StarCoder ([Li et al., 2023](https://arxiv.org/abs/2305.06161)). We further supplement our training with multi-lingual data from CulturaX ([Nguyen et al., 2023](https://arxiv.org/abs/2309.09400)) and, in particular, from its OSCAR corpora, as well as restructured data in the style of [Yuan & Liu (2022)](https://arxiv.org/abs/2206.11147).

* Given the large amount of web data, we recommend fine-tuning the base `Stable LM 2 1.6B` for your downstream tasks.

### Training Procedure

The model is pre-trained on the aforementioned datasets in `bfloat16` precision, optimized with AdamW, and trained using the Arcade100k tokenizer with a vocabulary size of 100,352. We outline the complete hyperparameters choices in the project's [GitHub repository - config*](https://github.com/Stability-AI/StableLM/blob/main/configs/stablelm-2-1_6b.yml). The final checkpoint of pre-training, before cooldown, is provided in the `global_step420000` [branch](https://huggingface.co/stabilityai/stablelm-2-1_6b/blob/global_step420000/README.md).

### Training Infrastructure

* **Hardware**: `Stable LM 2 1.6B` was trained on the Stability AI cluster across 512 NVIDIA A100 40GB GPUs (AWS P4d instances).

* **Software**: We use a fork of `gpt-neox` ([EleutherAI, 2021](https://github.com/EleutherAI/gpt-neox)), train under 2D parallelism (Data and Tensor Parallel) with ZeRO-1 ([Rajbhandari et al., 2019](https://arxiv.org/abs/1910.02054v3)), and rely on flash-attention as well as SwiGLU and Rotary Embedding kernels from FlashAttention-2 ([Dao et al., 2023](https://tridao.me/publications/flash2/flash2.pdf))

## Use and Limitations

### Intended Use

The model is intended to be used as a foundational base model for application-specific fine-tuning. Developers must evaluate and fine-tune the model for safe performance in downstream applications. For commercial use, please refer to https://stability.ai/membership.

### Limitations and Bias
​
As a base model, this model may exhibit unreliable, unsafe, or other undesirable behaviors that must be corrected through evaluation and fine-tuning prior to deployment. The pre-training dataset may have contained offensive or inappropriate content, even after applying data cleansing filters, which can be reflected in the model-generated text. We recommend that users exercise caution when using these models in production systems. Do not use the models if they are unsuitable for your application, or for any applications that may cause deliberate or unintentional harm to others.

## How to Cite

```bibtex
@article{bellagente2024stable,
  title={Stable LM 2 1.6 B Technical Report},
  author={Bellagente, Marco and Tow, Jonathan and Mahan, Dakota and Phung, Duy and Zhuravinskyi, Maksym and Adithyan, Reshinth and Baicoianu, James and Brooks, Ben and Cooper, Nathan and Datta, Ashish and others},
  journal={arXiv preprint arXiv:2402.17834},
  year={2024}
}
```
