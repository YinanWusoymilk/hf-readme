---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
tags:
- chat
base_model: Qwen/Qwen2-7B-Instruct
---

# Qwen2-7B-Instruct-AWQ

## Introduction

Qwen2 is the new series of Qwen large language models. For Qwen2, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters, including a Mixture-of-Experts model. This repo contains the instruction-tuned 7B Qwen2 model.

Compared with the state-of-the-art opensource language models, including the previous released Qwen1.5, Qwen2 has generally surpassed most opensource models and demonstrated competitiveness against proprietary models across a series of benchmarks targeting for language understanding, language generation, multilingual capability, coding, mathematics, reasoning, etc.

Qwen2-7B-Instruct-AWQ supports a context length of up to 131,072 tokens, enabling the processing of extensive inputs. Please refer to [this section](#processing-long-texts) for detailed instructions on how to deploy Qwen2 for handling long texts.

For more details, please refer to our [blog](https://qwenlm.github.io/blog/qwen2/), [GitHub](https://github.com/QwenLM/Qwen2), and [Documentation](https://qwen.readthedocs.io/en/latest/).
<br>

## Model Details
Qwen2 is a language model series including decoder language models of different model sizes. For each size, we release the base language model and the aligned chat model. It is based on the Transformer architecture with SwiGLU activation, attention QKV bias, group query attention, etc. Additionally, we have an improved tokenizer adaptive to multiple natural languages and codes.

## Training details
We pretrained the models with a large amount of data, and we post-trained the models with both supervised finetuning and direct preference optimization.


## Requirements
The code of Qwen2 has been in the latest Hugging face transformers and we advise you to install `transformers>=4.37.0`, or you might encounter the following error:
```
KeyError: 'qwen2'
```

## Quickstart

Here provides a code snippet with `apply_chat_template` to show you how to load the tokenizer and model and how to generate contents.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2-7B-Instruct-AWQ",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-7B-Instruct-AWQ")

prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

### Processing Long Texts

To handle extensive inputs exceeding 32,768 tokens, we utilize [YARN](https://arxiv.org/abs/2309.00071), a technique for enhancing model length extrapolation, ensuring optimal performance on lengthy texts.

For deployment, we recommend using vLLM. You can enable the long-context capabilities by following these steps:

1. **Install vLLM**: You can install vLLM by running the following command.

```bash
pip install "vllm>=0.4.3"
```

Or you can install vLLM from [source](https://github.com/vllm-project/vllm/).

2. **Configure Model Settings**: After downloading the model weights, modify the `config.json` file by including the below snippet:
    ```json
        {
            "architectures": [
                "Qwen2ForCausalLM"
            ],
            // ...
            "vocab_size": 152064,

            // adding the following snippets
            "rope_scaling": {
                "factor": 4.0,
                "original_max_position_embeddings": 32768,
                "type": "yarn"
            }
        }
    ```
    This snippet enable YARN to support longer contexts.

3. **Model Deployment**: Utilize vLLM to deploy your model. For instance, you can set up an openAI-like server using the command:

    ```bash
    python -m vllm.entrypoints.openai.api_server --served-model-name Qwen2-7B-Instruct-AWQ --model path/to/weights
    ```

    Then you can access the Chat API by:

    ```bash
    curl http://localhost:8000/v1/chat/completions \
        -H "Content-Type: application/json" \
        -d '{
        "model": "Qwen2-7B-Instruct-AWQ",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Your Long Input Here."}
        ]
        }'
    ```

    For further usage instructions of vLLM, please refer to our [Github](https://github.com/QwenLM/Qwen2).

**Note**: Presently, vLLM only supports static YARN, which means the scaling factor remains constant regardless of input length, **potentially impacting performance on shorter texts**. We advise adding the `rope_scaling` configuration only when processing long contexts is required.

## Benchmark and Speed

To compare the generation performance between bfloat16 (bf16) and quantized models such as GPTQ-Int8, GPTQ-Int4, and AWQ, please consult our [Benchmark of Quantized Models](https://qwen.readthedocs.io/en/latest/benchmark/quantization_benchmark.html). This benchmark provides insights into how different quantization techniques affect model performance.

For those interested in understanding the inference speed and memory consumption when deploying these models with either ``transformer`` or ``vLLM``, we have compiled an extensive [Speed Benchmark](https://qwen.readthedocs.io/en/latest/benchmark/speed_benchmark.html).

## Citation

If you find our work helpful, feel free to give us a cite.

```
@article{qwen2,
  title={Qwen2 Technical Report},
  year={2024}
}
```