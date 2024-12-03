---
license: cc-by-nc-4.0
base_model: microsoft/Phi-3
model-index:
- name: Octopus-V4-3B
  results: []
tags:
- AI agent
- Graph
inference: false
space: false
spaces: false
language:
- en
---
# Octopus V4: Graph of language models

## Octopus V4
<p align="center">
- <a href="https://www.nexa4ai.com/" target="_blank">Nexa AI Website</a>
- <a href="https://github.com/NexaAI/octopus-v4" target="_blank">Octopus-v4 Github</a>
- <a href="https://arxiv.org/abs/2404.19296" target="_blank">ArXiv</a>
- <a href="https://huggingface.co/spaces/NexaAIDev/domain_llm_leaderboard" target="_blank">Domain LLM Leaderbaord</a>
- <a href="https://graph.nexa4ai.com/" target="_blank">Graph demo</a>
</p>

<p align="center" width="100%">
  <a><img src="octopus-v4-logo.png" alt="nexa-octopus" style="width: 40%; min-width: 300px; display: block; margin: auto;"></a>
</p>

## Quantized Octopus V4
To run the model on-device, we have prepared [quantized models](https://huggingface.co/NexaAIDev/octopus-v4-gguf) in gguf format for you.

## Introduction

Octopus-V4-3B, an advanced open-source language model with 3 billion parameters, serves as the master node in Nexa AI's envisioned graph of language models. Tailored specifically for the MMLU benchmark topics, this model efficiently translates user queries into formats that specialized models can effectively process. It excels at directing these queries to the appropriate specialized model, ensuring precise and effective query handling.

📱 **Compact Size**: Octopus-V4-3B is compact, enabling it to operate on smart devices efficiently and swiftly.

🐙 **Accuracy**: Octopus-V4-3B accurately maps user queries to the specialized model using a functional token design, enhancing its precision.

💪 **Reformat Query**: Octopus-V4-3B assists in converting natural human language into a more professional format, improving query description and resulting in more accurate responses.

## Example Use Cases

```text
Query: Tell me the result of derivative of x^3 when x is 2?

# <nexa_4> represents the math gpt.
Response: <nexa_4> ('Determine the derivative of the function f(x) = x^3 at the point where x equals 2, and interpret the result within the context of rate of change and tangent slope.')<nexa_end>
```

You can run the model on a GPU using the following code. 
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import time
torch.random.manual_seed(0)

model = AutoModelForCausalLM.from_pretrained(
    "NexaAIDev/Octopus-v4", 
    device_map="cuda:0", 
    torch_dtype=torch.bfloat16, 
    trust_remote_code=True 
)
tokenizer = AutoTokenizer.from_pretrained("NexaAIDev/Octopus-v4")

question = "Tell me the result of derivative of x^3 when x is 2?"

inputs = f"<|system|>You are a router. Below is the query from the users, please call the correct function and generate the parameters to call the function.<|end|><|user|>{question}<|end|><|assistant|>"

print('\n============= Below is the response ==============\n')

# You should consider to use early stopping with <nexa_end> token to accelerate
input_ids = tokenizer(inputs, return_tensors="pt")['input_ids'].to(model.device)

generated_token_ids = []
start = time.time()

# set a large enough number here to avoid insufficient length
for i in range(200):
    next_token = model(input_ids).logits[:, -1].argmax(-1)
    generated_token_ids.append(next_token.item())
    
    input_ids = torch.cat([input_ids, next_token.unsqueeze(1)], dim=-1)

    # 32041 is the token id of <nexa_end>
    if next_token.item() == 32041:
        break

print(tokenizer.decode(generated_token_ids))
end = time.time()
print(f'Elapsed time: {end - start:.2f}s')
```



## License
This model was trained on commercially viable data. For use of our model, refer to the [license information](https://www.nexa4ai.com/licenses/licenses-v4).


## Performance
###  Model Selection
We leverage the latest Language Large Models for a variety of domains. Below is a summary of the chosen models for each category. In cases where no specialized model exists for a subject, we utilize generic models like Llama3-8b.


| **Model**                               | **Category**       | **Subjects**                                                                                                                                                      |
|-----------------------------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `jondurbin/bagel-8b-v1.0`               | Biology            | `college_biology`, `high_school_biology`                                                                                                                          |
| `Weyaxi/Einstein-v6.1-Llama3-8B`        | Physics            | `astronomy`, `college_physics`, `conceptual_physics`, `high_school_physics`                                                                                       |
| `meta-llama/Meta-Llama-3-8B-Instruct`   | Business           | `business_ethics`, `management`, `marketing`                                                                                                                      |
| `meta-llama/Meta-Llama-3-8B-Instruct`   | Chemistry          | `college_chemistry`, `high_school_chemistry`                                                                                                                      |
| `abacusai/Llama-3-Smaug-8B`             | Computer Science   | `college_computer_science`, `computer_security`, `high_school_computer_science`, `machine_learning`                                                               |
| `Open-Orca/Mistral-7B-OpenOrca`         | Math               | `abstract_algebra`, `college_mathematics`, `elementary_mathematics`, `high_school_mathematics`, `high_school_statistics`                                          |
| `meta-llama/Meta-Llama-3-8B-Instruct`   | Economics          | `econometrics`, `high_school_macroeconomics`, `high_school_microeconomics`                                                                                       |
| `AdaptLLM/medicine-chat`                | Health             | `anatomy`, `clinical_knowledge`, `college_medicine`, `human_aging`, `medical_genetics`, `nutrition`, `professional_medicine`, `virology`                          |
| `STEM-AI-mtl/phi-2-electrical-engineering` | Engineering     | `electrical_engineering`                                                                                                                                         |
| `meta-llama/Meta-Llama-3-8B-Instruct`   | Philosophy         | `formal_logic`, `logical_fallacies`, `moral_disputes`, `moral_scenarios`, `philosophy`, `world_religions`                                                        |
| `microsoft/Phi-3-mini-128k-instruct`    | Other              | `global_facts`, `miscellaneous`, `professional_accounting`                                                                                                       |
| `meta-llama/Meta-Llama-3-8B-Instruct`   | History            | `high_school_european_history`, `high_school_us_history`, `high_school_world_history`, `prehistory`                                                              |
| `meta-llama/Meta-Llama-3-8B-Instruct`   | Culture            | `human_sexuality`, `sociology`                                                                                                                                   |
| `AdaptLLM/law-chat`                     | Law                | `international_law`, `jurisprudence`, `professional_law`                                                                                                         |
| `meta-llama/Meta-Llama-3-8B-Instruct`   | Psychology         | `high_school_psychology`, `professional_psychology`                                                                                                              |


### MMLU Benchmark Results (5-shot learning)
Here are the comparative MMLU scores for various models tested under a 5-shot learning setup:

| **Model**                         | **MMLU Score** |
|-----------------------------------|----------------|
| Octopus-V4                        | **74.8%**      |
| GPT-3.5                           | 70.0%          |
| Phi-3-mini-128k-instruct          | 68.1%          |
| OpenELM-3B                        | 26.7%          |
| Lamma3-8b-instruct                | 68.4%          |
| Gemma-2b                          | 42.3%          |
| Gemma-7b                          | 64.3%          |

###  Domain LLM Leaderboard
Explore our collection of domain-specific large language models (LLMs) or contribute by suggesting new models tailored to specific domains. For detailed information on available models and to engage with our community, please visit our [Domain LLM Leaderboard](https://huggingface.co/spaces/NexaAIDev/domain_llm_leaderboard).

## References
We thank the Microsoft team for their amazing model!
```
@article{abdin2024phi,
  title={Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone},
  author={Abdin, Marah and Jacobs, Sam Ade and Awan, Ammar Ahmad and Aneja, Jyoti and Awadallah, Ahmed and Awadalla, Hany and Bach, Nguyen and Bahree, Amit and Bakhtiari, Arash and Behl, Harkirat and others},
  journal={arXiv preprint arXiv:2404.14219},
  year={2024}
}
```

## Citation
```
@misc{chen2024octopus,
      title={Octopus v4: Graph of language models}, 
      author={Wei Chen and Zhiyuan Li},
      year={2024},
      eprint={2404.19296},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Contact
Please [contact us](mailto:alexchen@nexa4ai.com) to reach out for any issues and comments!