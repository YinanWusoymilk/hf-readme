---
license: llama3
tags:
- function-calling
---

# FireFunction V2: Fireworks Function Calling Model

[**Try on Fireworks**](https://fireworks.ai/models/fireworks/firefunction-v2) | [**API Docs**](https://readme.fireworks.ai/docs/function-calling) | [**Demo App**](https://functional-chat.vercel.app/) | [**Discord**](https://discord.gg/mMqQxvFD9A)

<img src="https://cdn-uploads.huggingface.co/production/uploads/64b6f3a72f5a966b9722de88/nJNtxLzWswBDKK1iOZblb.png" alt="firefunction" width="400"/>

FireFunction is a state-of-the-art function calling model with a commercially viable license. View detailed info in our [announcement blog](https://fireworks.ai/blog/firefunction-v2-launch-post). Key info and highlights:

**Comparison with other models:**
- Competitive with GPT-4o at function-calling, scoring 0.81 vs 0.80 on a medley of public evaluations
- Trained on Llama 3 and retains Llama 3’s conversation and instruction-following capabilities, scoring 0.84 vs Llama 3’s 0.89 on MT bench
- Significant quality improvements over FireFunction v1 across the broad range of metrics


**General info:**

🐾 Successor of the [FireFunction](https://fireworks.ai/models/fireworks/firefunction-v1) model

🔆 Support of parallel function calling (unlike FireFunction v1) and good instruction following

💡 Hosted on the [Fireworks](https://fireworks.ai/models/fireworks/firefunction-v2) platform at < 10% of the cost of GPT 4o and 2x the speed




## Intended Use and Limitations

### Supported usecases
The model was tuned to perfom well on a range of usecases including:
 * general instruction following
 * multi-turn chat mixing vanilla messages with function calls
 * single- and parallel function calling
 * up to 20 function specs supported at once
 * structured information extraction
   
The model has an 8k context window, like Llama 3

### Out-of-Scope Use
The model was not optimized for the following use cases:
  * 100+ function specs
  * nested function calling

## Metrics

| Benchmark                          | Firefunction v1 | Firefunction v2 | Llama 3 70b Instruct | Gpt-4o |
|:-----------------------------------|:----------------|:----------------|:---------------------|:-------|
| Gorilla simple                     | 0.91            | 0.94            | 0.925                | 0.88   |
| Gorilla multiple_function          | 0.92            | 0.91            | 0.86                 | 0.91   |
| Gorilla parallel_function          | 0               | 0.9             | 0.86                 | 0.89   |
| Gorilla parallel_multiple_function | 0               | 0.8             | 0.615                | 0.72   |
| Nexus parallel                     | 0.38            | 0.53            | 0.3                  | 0.47   |
| Mtbench                            | 0.73            | 0.84            | 0.89                 | 0.93   |
| Average                            | 0.49            | 0.82            | 0.74                 | 0.8    |

## Example Usage

See [documentation](https://readme.fireworks.ai/docs/function-calling) for more detail.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import json
from datetime import datetime

device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained("fireworks-ai/firefunction-v2", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("fireworks-ai/firefunction-v2")

function_spec = [
    {
        "name": "get_stock_price",
        "description": "Get the current stock price",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The stock symbol, e.g. AAPL, GOOG"
                }
            },
            "required": [
                "symbol"
            ]
        }
    },
    {
        "name": "check_word_anagram",
        "description": "Check if two words are anagrams of each other",
        "parameters": {
            "type": "object",
            "properties": {
                "word1": {
                    "type": "string",
                    "description": "The first word"
                },
                "word2": {
                    "type": "string",
                    "description": "The second word"
                }
            },
            "required": [
                "word1",
                "word2"
            ]
        }
    }
]
functions = json.dumps(function_spec, indent=4)

messages = [
    {'role': 'system', 'content': 'You are a helpful assistant with access to functions. Use them if required.'},
    {'role': 'user', 'content': 'Hi, can you tell me the current stock price of google and netflix?'}
]

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

model_inputs = tokenizer.apply_chat_template(messages, functions=functions, datetime=now, return_tensors="pt").to(model.device)

generated_ids = model.generate(model_inputs, max_new_tokens=128)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])
```

## Resources
* [Fireworks discord with function calling channel](https://discord.gg/mMqQxvFD9A)
* [Documentation](https://readme.fireworks.ai/docs/function-calling)
* [Demo app](https://functional-chat.vercel.app/)
* [Try in Fireworks prompt playground UI](https://fireworks.ai/models/fireworks/firefunction-v2)