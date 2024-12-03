---
datasets:
- bigcode/starcoderdata
language:
- code
tags:
- causal-lm
model-index:
  - name: stabilityai/stablecode-completion-alpha-3b-4k
    results:
      - task:
          type: text-generation
        dataset:
          type: openai_humaneval
          name: HumanEval
        metrics:
          - name: pass@1
            type: pass@1
            value: 0.1768
            verified: false
          - name: pass@10
            type: pass@10
            value: 0.2701
            verified: false

license: apache-2.0
---
# `StableCode-Completion-Alpha-3B-4K`

## Model Description

`StableCode-Completion-Alpha-3B-4K` is a 3 billion parameter decoder-only code completion model pre-trained on diverse set of programming languages that topped the stackoverflow developer survey. 

## Usage
The model is intended to do single/multiline code completion from a long context window upto 4k tokens.
Get started generating code with `StableCode-Completion-Alpha-3B-4k` by using the following code snippet:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablecode-completion-alpha-3b-4k")
model = AutoModelForCausalLM.from_pretrained(
  "stabilityai/stablecode-completion-alpha-3b-4k",
  trust_remote_code=True,
  torch_dtype="auto",
)
model.cuda()
inputs = tokenizer("import torch\nimport torch.nn as nn", return_tensors="pt").to("cuda")
tokens = model.generate(
  **inputs,
  max_new_tokens=48,
  temperature=0.2,
  do_sample=True,
)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))
```

## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: `StableCode-Completion-Alpha-3B-4k` models are auto-regressive language models based on the transformer decoder architecture.
* **Language(s)**: Code
* **Library**: [GPT-NeoX](https://github.com/EleutherAI/gpt-neox)
* **License**: Model checkpoints are licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.
* **Contact**: For questions and comments about the model, please email `lm@stability.ai`

### Model Architecture

| Parameters     | Hidden Size | Layers | Heads | Sequence Length |
|----------------|-------------|--------|-------|-----------------|
| 2,796,431,360  | 2560        | 32     | 32    | 4096            |


* **Decoder Layer**: Parallel Attention and MLP residuals with a single input LayerNorm ([Wang & Komatsuzaki, 2021](https://github.com/kingoflolz/mesh-transformer-jax/tree/master))
* **Position Embeddings**: Rotary Position Embeddings ([Su et al., 2021](https://arxiv.org/abs/2104.09864))
* **Bias**: LayerNorm bias terms only

## Training

`StableCode-Completion-Alpha-3B-4k` is pre-trained at a context length of 4096 for 300 billion tokens on the `bigcode/starcoder-data`.

### Training Dataset

The first pre-training stage relies on 300B tokens sourced from various top programming languages occuring in the stackoverflow developer survey present in the `starcoder-data` dataset. 

### Training Procedure

The model is pre-trained on the dataset mixes mentioned above in mixed-precision BF16), optimized with AdamW, and trained using the [StarCoder](https://huggingface.co/bigcode/starcoder) tokenizer with a vocabulary size of 49k.

* **Software**: We use a fork of gpt-neox ([EleutherAI, 2021](https://github.com/EleutherAI/gpt-neox)) and train under 2D parallelism (Data and Tensor Parallel) with ZeRO-1 ([Rajbhandari et al., 2019](https://arxiv.org/abs/1910.02054v3)) and rely on flash-attention as well as rotary embedding kernels from FlashAttention-2 ([Dao et al., 2023](https://tridao.me/publications/flash2/flash2.pdf))

## Use and Limitations

### Intended Use

StableCode-Completion-Alpha-3B-4K independently generates new code completions, but we recommend that you use StableCode-Completion-Alpha-3B-4K together with the tool developed by BigCode and HuggingFace [(huggingface/huggingface-vscode: Code completion VSCode extension for OSS models (github.com))](https://github.com/huggingface/huggingface-vscode), to identify and, if necessary, attribute any outputs that match training code.

### Limitations and bias

This model is intended to be used responsibly. It is not intended to be used to create unlawful content of any kind, to further any unlawful activity, or to engage in activities with a high risk of physical or economic harm.

## How to cite

```bibtex
@misc{StableCodeCompleteAlpha4K, 
      url={[https://huggingface.co/stabilityai/stablecode-complete-alpha-3b-4k](https://huggingface.co/stabilityai/stablecode-complete-alpha-3b-4k)}, 
      title={Stable Code Complete Alpha}, 
      author={Adithyan, Reshinth and Phung, Duy and Cooper, Nathan and Pinnaparaju, Nikhil and Laforte, Christian}
}
```