---
license: apache-2.0
datasets:
- berkeley-nest/Nectar
language:
- en
library_name: transformers
tags:
- reward model
- RLHF
- RLAIF
---
# Starling-LM-7B-beta

<!-- Provide a quick summary of what the model is/does. -->

- **Developed by: The Nexusflow Team (** Banghua Zhu * , Evan Frick * , Tianhao Wu * , Hanlin Zhu, Karthik Ganesan, Wei-Lin Chiang, Jian Zhang, and Jiantao Jiao).
- **Model type:** Language Model finetuned with RLHF / RLAIF
- **License:** Apache-2.0 license under the condition that the model is not used to compete with OpenAI
- **Finetuned from model:** [Openchat-3.5-0106](https://huggingface.co/openchat/openchat-3.5-0106) (based on [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1))
 


We introduce Starling-LM-7B-beta, an open large language model (LLM) trained by Reinforcement Learning from AI Feedback (RLAIF). Starling-LM-7B-beta is trained from [Openchat-3.5-0106](https://huggingface.co/openchat/openchat-3.5-0106) with our new reward model [Nexusflow/Starling-RM-34B](https://huggingface.co/Nexusflow/Starling-RM-34B) and policy optimization method [Fine-Tuning Language Models from Human Preferences (PPO)](https://arxiv.org/abs/1909.08593).
Harnessing the power of the ranking dataset, [berkeley-nest/Nectar](https://huggingface.co/datasets/berkeley-nest/Nectar), the upgraded reward model, [Starling-RM-34B](https://huggingface.co/Nexusflow/Starling-RM-34B), and the new reward training and policy tuning pipeline, Starling-LM-7B-beta scores an improved 8.12 in MT Bench with GPT-4 as a judge. 


## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

**Important: Please use the exact chat template provided below for the model. Otherwise there will be a degradation in the performance. The model output can be verbose in rare cases. Please consider setting temperature = 0 to make this happen less.**

Our model follows the exact chat template and usage as [Openchat-3.5-0106](https://huggingface.co/openchat/openchat-3.5-0106). Please refer to their model card for more details.
In addition, our model is hosted on LMSYS [Chatbot Arena](https://chat.lmsys.org) for free test.

The conversation template is the same as Openchat-3.5-0106:
```
import transformers
tokenizer = transformers.AutoTokenizer.from_pretrained("openchat/openchat-3.5-0106")

# Single-turn
tokens = tokenizer("GPT4 Correct User: Hello<|end_of_turn|>GPT4 Correct Assistant:").input_ids
assert tokens == [1, 420, 6316, 28781, 3198, 3123, 1247, 28747, 22557, 32000, 420, 6316, 28781, 3198, 3123, 21631, 28747]

# Multi-turn
tokens = tokenizer("GPT4 Correct User: Hello<|end_of_turn|>GPT4 Correct Assistant: Hi<|end_of_turn|>GPT4 Correct User: How are you today?<|end_of_turn|>GPT4 Correct Assistant:").input_ids
assert tokens == [1, 420, 6316, 28781, 3198, 3123, 1247, 28747, 22557, 32000, 420, 6316, 28781, 3198, 3123, 21631, 28747, 15359, 32000, 420, 6316, 28781, 3198, 3123, 1247, 28747, 1602, 460, 368, 3154, 28804, 32000, 420, 6316, 28781, 3198, 3123, 21631, 28747]

# Coding Mode
tokens = tokenizer("Code User: Implement quicksort using C++<|end_of_turn|>Code Assistant:").input_ids
assert tokens == [1, 7596, 1247, 28747, 26256, 2936, 7653, 1413, 334, 1680, 32000, 7596, 21631, 28747]
```
## Code Examples

```python
import transformers

tokenizer = transformers.AutoTokenizer.from_pretrained("Nexusflow/Starling-LM-7B-beta")
model = transformers.AutoModelForCausalLM.from_pretrained("Nexusflow/Starling-LM-7B-beta")

def generate_response(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(
        input_ids,
        max_length=256,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
    response_ids = outputs[0]
    response_text = tokenizer.decode(response_ids, skip_special_tokens=True)
    return response_text

# Single-turn conversation
prompt = "Hello, how are you?"
single_turn_prompt = f"GPT4 Correct User: {prompt}<|end_of_turn|>GPT4 Correct Assistant:"
response_text = generate_response(single_turn_prompt)
print("Response:", response_text)

## Multi-turn conversation
prompt = "Hello"
follow_up_question =  "How are you today?"
response = ""
multi_turn_prompt = f"GPT4 Correct User: {prompt}<|end_of_turn|>GPT4 Correct Assistant: {response}<|end_of_turn|>GPT4 Correct User: {follow_up_question}<|end_of_turn|>GPT4 Correct Assistant:"
response_text = generate_response(multi_turn_prompt)
print("Multi-turn conversation response:", response_text)

### Coding conversation
prompt = "Implement quicksort using C++"
coding_prompt = f"Code User: {prompt}<|end_of_turn|>Code Assistant:"
response = generate_response(coding_prompt)
print("Coding conversation response:", response)
```

## License
The dataset, model and online demo is subject to the [Terms of Use](https://openai.com/policies/terms-of-use) of the data generated by OpenAI, and [Privacy Practices](https://chrome.google.com/webstore/detail/sharegpt-share-your-chatg/daiacboceoaocpibfodeljbdfacokfjb) of ShareGPT. Please contact us if you find any potential violation.


## Acknowledgment
We would like to thank Tianle Li from UC Berkeley for detailed feedback and evaluation of this beta release. We would like to thank the [LMSYS Organization](https://lmsys.org/) for their support of [lmsys-chat-1M](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) dataset, evaluation and online demo. We would like to thank the open source community for their efforts in providing the datasets and base models we used to develope the project, including but not limited to Anthropic, Llama, Mistral, Hugging Face H4, LMSYS, OpenChat, OpenBMB, Flan and ShareGPT.

## Citation
```
@misc{starling2023,
    title = {Starling-7B: Improving LLM Helpfulness & Harmlessness with RLAIF},
    url = {},
    author = {Zhu, Banghua and Frick, Evan and Wu, Tianhao and Zhu, Hanlin and Ganesan, Karthik and Chiang, Wei-Lin and Zhang, Jian and Jiao, Jiantao},
    month = {November},
    year = {2023}
}
```