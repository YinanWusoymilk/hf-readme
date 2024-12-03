---
license: apache-2.0
tags:
- snowflake
- arctic
- moe
---

## Model Details

Arctic is a dense-MoE Hybrid transformer architecture pre-trained from scratch by the Snowflake AI 
Research Team. We are releasing model checkpoints for both the base and instruct-tuned versions of 
Arctic under an Apache-2.0 license. This means you can use them freely in your own research, 
prototypes, and products. Please see our blog 
[Snowflake Arctic: The Best LLM for Enterprise AI — Efficiently Intelligent, Truly Open](https://www.snowflake.com/blog/arctic-open-efficient-foundation-language-models-snowflake/) 
for more information on Arctic and links to other relevant resources such as our series of cookbooks 
covering topics around training your own custom MoE models, how to produce high-quality training data, 
and much more.

* [Arctic-Base](https://huggingface.co/Snowflake/snowflake-arctic-base/)
* [Arctic-Instruct](https://huggingface.co/Snowflake/snowflake-arctic-instruct/)

For the latest details about Snowflake Arctic including tutorials, etc., please refer to our GitHub repo: 
* https://github.com/Snowflake-Labs/snowflake-arctic

Try a live demo with our [Streamlit app](https://huggingface.co/spaces/Snowflake/snowflake-arctic-st-demo). 

**Model developers** Snowflake AI Research Team

**License** Apache-2.0

**Input** Models input text only.

**Output** Models generate text and code only.

**Model Release Date** April, 24th 2024.

## Model Architecture

Arctic combines a 10B dense transformer model with a residual 128x3.66B MoE MLP resulting in 480B 
total and 17B active parameters chosen using a top-2 gating. For more details about Arctic's model
Architecture, training process, data, etc. [see our series of cookbooks](https://www.snowflake.com/en/data-cloud/arctic/cookbook/).


## Usage

Arctic is currently supported with `transformers` by leveraging the 
[custom code feature](https://huggingface.co/docs/transformers/en/custom_models#using-a-model-with-custom-code), 
to use this you simply need to add `trust_remote_code=True` to your AutoTokenizer and AutoModelForCausalLM calls.
However, we recommend that you use a `transformers` version at or above 4.39:

```python
pip install transformers>=4.39.0
```

Arctic leverages several features from [DeepSpeed](https://github.com/microsoft/DeepSpeed), you will need to 
install the DeepSpeed 0.14.2 or higher to get all of these required features:

```python
pip install deepspeed>=0.14.2
```

### Inference examples

Due to the model size we recommend using a single 8xH100 instance from your
favorite cloud provider such as: AWS [p5.48xlarge](https://aws.amazon.com/ec2/instance-types/p5/), 
Azure [ND96isr_H100_v5](https://learn.microsoft.com/en-us/azure/virtual-machines/nd-h100-v5-series), etc.

In this example we are using FP8 quantization provided by DeepSpeed in the backend, we can also use FP6 
quantization by specifying `q_bits=6` in the `QuantizationConfig` config. The `"150GiB"` setting 
for max_memory is required until we can get DeepSpeed's FP quantization supported natively as a
[HFQuantizer](https://huggingface.co/docs/transformers/main/en/hf_quantizer#build-a-new-hfquantizer-class) which we 
are actively working on.

```python
import os
# enable hf_transfer for faster ckpt download
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from deepspeed.linear.config import QuantizationConfig

tokenizer = AutoTokenizer.from_pretrained(
    "Snowflake/snowflake-arctic-instruct",
    trust_remote_code=True
)
quant_config = QuantizationConfig(q_bits=8)

model = AutoModelForCausalLM.from_pretrained(
    "Snowflake/snowflake-arctic-instruct",
    trust_remote_code=True,
    low_cpu_mem_usage=True,
    device_map="auto",
    ds_quantization_config=quant_config,
    max_memory={i: "150GiB" for i in range(8)},
    torch_dtype=torch.bfloat16)


content = "5x + 35 = 7x - 60 + 10. Solve for x"
messages = [{"role": "user", "content": content}]
input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to("cuda")

outputs = model.generate(input_ids=input_ids, max_new_tokens=256)
print(tokenizer.decode(outputs[0]))
```

The Arctic GitHub page has additional code snippets and examples around running inference:

* Example with pure-HF: https://github.com/Snowflake-Labs/snowflake-arctic/blob/main/inference
* Tutorial using vLLM: https://github.com/Snowflake-Labs/snowflake-arctic/tree/main/inference/vllm