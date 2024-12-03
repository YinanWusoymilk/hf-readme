---
license: mit
license_link: https://huggingface.co/upstage/solar-pro-preview-instruct/blob/main/LICENSE
language:
- en
pipeline_tag: text-generation
tags:
- nlp
library_name: transformers
---

<p align="left">
  <a href="https://go.upstage.ai/3Xk9J6X">
    <img src="https://cdn-uploads.huggingface.co/production/uploads/5fd90c758fe27b1a6b077abb/jwMkqV88Hj8sJu7NjTedm.png" width="100%"/>
  </a>
<p>

# **Solar Pro Preview: The most intelligent LLM on a single GPU**

# **Summary**

We introduce **Solar Pro Preview**, an advanced large language model (LLM) with 22 billion parameters designed to [fit into a single GPU](https://www.upstage.ai/products/solar-pro-preview?utm_source=%08platform&utm_medium=huggingface&utm_campaign=solarpro-preview-launch). Solar Pro Preview shows superior performance compared to LLMs with less than 30 billion parameters and delivers performance comparable to models over three times its size, such as Llama 3.1 with 70 billion parameters.

Solar Pro Preview is developed using an enhanced version of our previous depth up-scaling method, which scales a Phi-3-medium model with 14 billion parameters to 22 billion parameters, intended to run on a GPU with 80GB of VRAM. Our carefully curated training strategy and dataset have significantly enhanced performance from Phi-3-medium, particularly on the MMLU-Pro and IFEval benchmarks, both respected for evaluating a model’s knowledge and instruction-following abilities. 

Solar Pro Preview is a pre-release version of the official Solar Pro, with limitations on language coverage and a maximum context length of 4K. However, we believe Solar Pro Preview not only stands out as a highly efficient and capable model, but has the potential to be further extended to cover more languages and capabilities. The official version of Solar Pro will be released this November 2024 with expanded language support beyond English and longer context windows. To stay informed about the latest updates, please sign up for [our mailing list](https://www.upstage.ai/get-upstage-updates). If you have any feedback or questions about the model, please visit our [model discussion board](https://huggingface.co/upstage/solar-pro-preview-instruct/discussions) and connect with us directly.

# **Usage**

Solar Pro Preview is an instruction-tuned language model. This model is specifically designed to follow instructions and engage in conversational tasks.

### Chat Template

As an instruction-tuned model, Solar Pro Preview uses the ChatML template for optimal performance in conversational and instruction-following tasks. This approach aligns with the model's training data and is likely to yield more accurate and relevant responses. For instance, a question formatted in the ChatML template looks like the following, where the model generates the answer after <|im_start|>assistant. Note that system prompts are not currently supported in Solar Pro Preview. This feature will be available in the official release.

```
<|im_start|>user
Please, introduce yourself.<|im_end|>
<|im_start|>assistant
```

### Text Generation

Below is an example inference code that details loading the model, applying the chat template, and generating the model answer.

```python
# Install requirements
# !pip install transformers==4.44.2 torch==2.3.1 flash_attn==2.5.8 accelerate==0.31.0

# Load model
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("upstage/solar-pro-preview-instruct")
model = AutoModelForCausalLM.from_pretrained(
    "upstage/solar-pro-preview-instruct",
    device_map="cuda",  
    torch_dtype="auto",  
    trust_remote_code=True,
)
# Apply chat template
messages = [
    {"role": "user", "content": "Please, introduce yourself."},
]
prompt = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True).to(model.device)
# Generate text
outputs = model.generate(prompt, max_new_tokens=512)
print(tokenizer.decode(outputs[0]))
```

Solar Pro Preview is also available as an API in [Upstage Console](https://go.upstage.ai/3Xl0Hqv) and we provide other easy-to-use methods as well. If you'd like to explore these options, please visit our [blog page](https://www.upstage.ai/products/solar-pro-preview?utm_source=%08platform&utm_medium=huggingface&utm_campaign=solarpro-preview-launch).


# **Evaluation**

Solar Pro Preview is evaluated over a variety of benchmarks. 

|               | Solar-pro-preview | Phi-3-medium-4K-instruct | Phi-3.5-MoE-instruct | Gemma 2 27B IT                             | Llama-3.1-8B-instruct                                                             | Llama-3.1-70B-instruct                                                            |
| ------------- | :---------------: | :----------------------: | :------------------: | :----------------------------------------: | :-------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------: |
| *Release Date*  | 2024.09.08        | 2024.05.02               | 2024.08.20           | 2024.06.25                                 | 2024.06.18                                                                        | 2024.06.16                                                                        |
| *Model size*    | 22B               | 14B                      | 41.9B (6.6B)         | 27B                                        | 8B                                                                                | 70B                                                                               |
| *License*       | MIT               | MIT                      | MIT                  | [gemma](https://ai.google.dev/gemma/terms) | [llama3.1](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B/blob/main/LICENSE) | [llama3.1](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B/blob/main/LICENSE) |
| **MMLU**          | 79.14             | 78.02                    | 78.66                | 76.13                                      | 68.25                                                                             | 82.09                                                                             |
| **MMLU Pro**      | 52.11             | 47.51                    | 46.99                | 45.68                                      | 37.88                                                                             | 53.01                                                                             |
| **IFEval**        | 84.37             | 64.37                    | 69.15                | 75.36                                      | 77.40                                                                             | 84.13                                                                             |
| **ARC-C**         | 68.86             | 66.55                    | 68.34                | 74.06                                      | 60.24                                                                             | 70.39                                                                             |
| **GPQA**          | 36.38             | 35.78                    | 34.38                | 36.38                                      | 35.26                                                                             | 41.06                                                                             |
| **HellaSwag**     | 86.36             | 85.68                    | 85.97                | 86.02                                      | 80.08                                                                             | 86.42                                                                             |
| **EQBench**       | 77.91             | 76.78                    | 77.22                | 80.32                                      | 65.80                                                                             | 82.52                                                                             |
| **BigBench Hard** | 67.31             | 63.09                    | 62.58                | 64.88                                      | 51.06                                                                             | 69.54                                                                             |
| **MUSR**          | 45.85             | 42.28                    | 46.79                | 45.67                                      | 29.68                                                                             | 47.22                                                                             |
| **GSM8K**         | 89.69             | 84.76                    | 82.26                | 62.85                                      | 75.97                                                                             | 92.12                                                                             |
| **MBPP**          | 61.59             | 60.27                    | N/A (\*)             | 63.08                                      | 52.20                                                                             | 65.51                                                                             |

(*) Since the model tends to generate a chat template, the score can't be accurately determined.

### Evaluation Protocol

For easy reproduction of our evaluation results, we list the evaluation tools and settings used below. All evaluations are conducted with NVIDIA DGX H100. 

|               | Evaluation setting    | Metric                                                         | Evaluation tool                                                                                                                                    |
| ------------- | :-------------------- | :------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| MMLU          | 5-shot                | macro_avg / acc                                                | [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/928e8bb6f50d1e93ef5d0bcaa81f8c5fd9a6f4d8) #928e8bb                      |
| MMLU Pro      | 5-shot                | macro_avg / acc                                                | [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/928e8bb6f50d1e93ef5d0bcaa81f8c5fd9a6f4d8) #928e8bb                      |
| IFEval        | 0-shot, chat_template | mean of prompt_level_strict_acc and instruction_level_strict_acc | [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/928e8bb6f50d1e93ef5d0bcaa81f8c5fd9a6f4d8) #928e8bb                      |
| ARC-C         | 25-shot               | acc_norm                                                       | [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/928e8bb6f50d1e93ef5d0bcaa81f8c5fd9a6f4d8) #928e8bb                      |
| GPQA          | 0-shot                | acc_norm                                                       | [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/928e8bb6f50d1e93ef5d0bcaa81f8c5fd9a6f4d8) #928e8bb                      |
| HellaSwag     | 10-shot               | acc_norm                                                       | [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/928e8bb6f50d1e93ef5d0bcaa81f8c5fd9a6f4d8) #928e8bb                      |
| EQBench       | 0-shot, chat_template | eqbench score                                                  | [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/928e8bb6f50d1e93ef5d0bcaa81f8c5fd9a6f4d8) #928e8bb                      |
| BigBench Hard | 3-shot                | macro_avg / acc_norm                                           | [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/928e8bb6f50d1e93ef5d0bcaa81f8c5fd9a6f4d8) #928e8bb                      |
| MUSR          | 0-shot                | macro_avg / acc_norm                                           | [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/928e8bb6f50d1e93ef5d0bcaa81f8c5fd9a6f4d8) #928e8bb                      |
| GSM8K         | 8-shot, CoT           | acc, exact_match & strict_extract                              | [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/928e8bb6f50d1e93ef5d0bcaa81f8c5fd9a6f4d8) #928e8bb                      |
| MBPP          | 0-shot                | pass@1                                                         | [bigcode-evaluation-harness](https://github.com/bigcode-project/bigcode-evaluation-harness/tree/0f3e95f0806e78a4f432056cdb1be93604a51d69) #0f3e95f |

The results may vary slightly for different batch sizes and experimental environment such as GPU type.

# **Contact us**

For any questions and suggestions regarding the model, please visit the [discussion board](https://huggingface.co/upstage/solar-pro-preview-instruct/discussions).

Learn more:

- [Chat with Solar Pro Preview](https://chat.upstage.ai)
- [Solar Pro Preview blog](https://www.upstage.ai/products/solar-pro-preview)
- [Solar Pro Preview developer documents](https://developers.upstage.ai/docs/apis/chat?utm_campaign=solarpro-preview-launch)

Also try out:

- [Document Parse](http://developers.upstage.ai/docs/apis/document-parse?utm_campaign=solarpro-preview-launch): An industry-leading model for converting complex document files to LLM-compatible HTML formats.
- [Solar DocVision Preview](http://developers.upstage.ai/docs/apis/document-qa?utm_campaign=solarpro-preview-launch): A vision LLM specialized on documents.