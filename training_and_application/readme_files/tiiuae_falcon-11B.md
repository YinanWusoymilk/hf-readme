---
datasets:
- tiiuae/falcon-refinedweb
language:
- en
- de
- es
- fr
- it
- nl
- pl
- pt
- ro
- cs
inference: false
license: unknown
---

# 🚀 Falcon2-11B

**Falcon2-11B is an 11B parameters causal decoder-only model built by [TII](https://www.tii.ae) and trained on over 5,000B tokens of [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb) enhanced with curated corpora. The model is made available under the [TII Falcon License 2.0](https://falconllm-staging.tii.ae/falcon-2-terms-and-conditions.html), the permissive Apache 2.0-based software license which includes an [acceptable use policy](https://falconllm-staging.tii.ae/falcon-2-acceptable-use-policy.html) that promotes the responsible use of AI.**

*[arXiv technical report](https://arxiv.org/abs/2407.14885)*


🤗 To get started with Falcon (inference, finetuning, quantization, etc.), we recommend reading [this great blogpost from HF](https://huggingface.co/blog/falcon)!

⚠️ **This is a raw, pretrained model, which should be further finetuned for most usecases.** 

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "tiiuae/falcon-11B"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
)
sequences = pipeline(
   "Can you explain the concepts of Quantum Computing?",
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

```

💥 **Falcon LLMs require PyTorch 2.0 for use with `transformers`!**

For fast inference with Falcon, check-out [Text Generation Inference](https://github.com/huggingface/text-generation-inference)! Read more in this [blogpost]((https://huggingface.co/blog/falcon). 

# Model Card for Falcon2-11B

## Model Details

### Model Description

- **Developed by:** [https://www.tii.ae](https://www.tii.ae)
- **Model type:** Causal decoder-only
- **Language(s) (NLP):** English, German, Spanish, French, Italian, Portuguese, Polish, Dutch, Romanian, Czech, Swedish
- **License:** [TII Falcon License 2.0](https://falconllm-staging.tii.ae/falcon-2-terms-and-conditions.html)

### Model Source

- **Paper:** *coming soon*.

## Uses

### Direct Use

Research on large language models; as a foundation for further specialization and finetuning for specific usecases (e.g., summarization, text generation, chatbot, etc.)

### Out-of-Scope Use

Production use without adequate assessment of risks and mitigation; any use cases which may be considered irresponsible or harmful. 

## Bias, Risks, and Limitations

Falcon2-11B is trained mostly on English, but also German, Spanish, French, Italian, Portuguese, Polish, Dutch, Romanian, Czech, Swedish. It will not generalize appropriately to other languages. Furthermore, as it is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

### Recommendations

We recommend users of Falcon2-11B to consider finetuning it for the specific set of tasks of interest, and for guardrails and appropriate precautions to be taken for any production use.

## How to Get Started with the Model


```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "tiiuae/falcon-11B"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
sequences = pipeline(
   "Can you explain the concepts of Quantum Computing?",
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

```

## Training Details

### Training Data

Falcon2-11B was trained over 5,000B tokens of [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb), a high-quality filtered and deduplicated web dataset which we enhanced with curated corpora. It followed a four stage training strategy. The first three stages were focused on increasing the context length, from to 2048 to 4096 and finally to 8192 tokens. The last stage aimed to further enhance performance using only high quality data.

Overall, the data sources included RefinedWeb-English, Refined Web-Europe (cs, de, es, fr, it, nl, pl, pt, ro, sv), high quality technical data, code data, and conversational data extracted from public sources.


The training stages were as follows:

| **Stage**    | **Context length** | **Tokens** |
|--------------|-----------------|-------------|
| Stage 1 | 2048            | 4500 B       |
| Stage 2 | 4096            | 250 B        |
| Stage 3 | 8192            | 250 B        |
| Stage 4 | 8192            | 500 B        |


The data was tokenized with the Falcon-[7B](https://huggingface.co/tiiuae/falcon-7b)/[11B](https://huggingface.co/tiiuae/falcon-11B) tokenizer.

### Training Procedure 

Falcon2-11B was trained on 1024 A100 40GB GPUs for the majority of the training, using a 3D parallelism strategy (TP=8, PP=1, DP=128) combined with ZeRO and Flash-Attention 2.

#### Training Hyperparameters

| **Hyperparameter** | **Value**  | **Comment**                               |
|--------------------|------------|-------------------------------------------|
| Precision          | `bfloat16` |                                           |
| Optimizer          | AdamW      |                                           |
| Max learning rate      | 3.7e-4       | Following a linear warm-up, then cosine decay to 1.89e-5 across 4500 B tokens. |
| Weight decay       | 1e-1       |                                           |
| Z-loss             | 1e-4       |                                           |
| Batch size         | Variable        | Batch size was gradually increased during the training                         |


#### Speeds, Sizes, Times

The model training took roughly two months. 


## Evaluation

|English Benchmark | **Value**  |
|--------------------|------------|
| ARC-Challenge-25shots         | 59.73    |
| HellaSwag-10shots  | 82.91     |
| MMLU-5shots | 58.37     |
| Winogrande-5shots | 78.30     |
| TruthfulQA-0shot      | 52.56     |
| GSM8k-5shots | 53.83     |
| ARC-Challenge-0shot | 50.17     |
| ARC-Easy-0shot | 77.78     |
| Hellaswag-0shot    | 82.07     |

We thank the leaderboard team from HuggingFace for providing an official evaluation of our model on the leaderboard tasks.

## Technical Specifications 

### Model Architecture and Objective

Falcon2-11B is a causal decoder-only model trained on a causal language modeling task (i.e., predict the next token).

The architecture is broadly adapted from the GPT-3 paper ([Brown et al., 2020](https://arxiv.org/abs/2005.14165)), with the following differences:

* **Positional embeddings:** rotary ([Su et al., 2021](https://arxiv.org/abs/2104.09864));
* **Attention:** multiquery ([Shazeer et al., 2019](https://arxiv.org/abs/1911.02150)) and FlashAttention-2 ([Dao, 2023](https://arxiv.org/abs/2307.08691));
* **Decoder-block:** parallel attention/MLP.

| **Hyperparameter** | **Value** | **Comment**                            |
|--------------------|-----------|----------------------------------------|
| Layers             | 60        |                                        |
| `d_model`          | 4096      |                                        |
| `head_dim`         | 128       |                                        |
| Vocabulary         | 65024     |                                        |
| Sequence length    | 8192      | During stages 3 and 4                  |

### Compute Infrastructure

#### Hardware

Falcon2-11B was trained on AWS SageMaker, using on average 1024 A100 40GB GPUs in 128 p4d instances. 

#### Software

Falcon2-11B was trained a custom distributed training codebase, Gigatron. It uses a 3D parallelism approach combined with ZeRO, high-performance Triton kernels and FlashAttention-2. More details about the distributed training strategy can be found in [Almazrouei et.al](https://arxiv.org/abs/2311.16867).

## Citation

[Falcon2-11B Technical Report, Malartic et al. 2024](https://www.arxiv.org/abs/2407.14885)

## License

Falcon2-11B is licenced under [TII Falcon License 2.0](https://falconllm-staging.tii.ae/falcon-2-terms-and-conditions.html), the permissive Apache 2.0-based software license which includes an [acceptable use policy](https://falconllm-staging.tii.ae/falcon-2-acceptable-use-policy.html) that promotes the responsible use of AI.

## Contact
falconllm@tii.ae