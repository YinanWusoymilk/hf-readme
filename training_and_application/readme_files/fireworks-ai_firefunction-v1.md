---
license: apache-2.0
tags:
- function-calling
---

# Fireworks Function Calling (FireFunction) Model V1

<img src="https://cdn-uploads.huggingface.co/production/uploads/64b6f3a72f5a966b9722de88/12mfdeAJzW1NdKrN_J--L.png" alt="firefunction" width="400"/>

FireFunction is a state-of-the-art function calling model with a commercially viable license. Key info and highlights:

💡 The model is also hosted on the [Fireworks](https://fireworks.ai/models/fireworks/firefunction-v1) platform. Offered for free during a limited beta period

⭐️ Near GPT-4 level quality for real-world use cases of structured information generation and routing decision-making

💨 Blazing fast speed. Inference speeds are roughly 4x that of GPT-4 when using FireFunction hosted on the Fireworks platform

🔄 Support for "any" parameter in tool_choice. Firefunction is the only model that we're aware that supports an option for the model to always choose a function - particularly helpful for routing use cases 

✅ The model is also API compatible with [OpenAI function calling](https://platform.openai.com/docs/guides/function-calling).
```sh
OPENAI_API_BASE=https://api.fireworks.ai/inference/v1
OPENAI_API_KEY=<YOUR_FIREWORKS_API_KEY>
MODEL=accounts/fireworks/models/firefunction-v1
```

## Resources
* [FireFunction-v1 Blog Post](https://fireworks.ai/blog/firefunction-v1-gpt-4-level-function-calling)
* [Fireworks discord with function calling channel](https://discord.gg/mMqQxvFD9A)
* [Documentation](https://readme.fireworks.ai/docs/function-calling)
* [UI Demo app](https://functional-chat.vercel.app/)
* [Try in Fireworks prompt playground UI](https://fireworks.ai/models/fireworks/firefunction-v1)
* [Running Locally with Ollama](https://ollama.com/joefamous/firefunction-v1/tags)


# Intended Use and Limitations

### Primary Use
Although the model was trained on a variety of tasks, it performs best on:
 * single-turn request routing to a function picked from a pool of up to 20 function specs.
 * structured information extraction.
See [blog post](https://fireworks.ai/blog) for more info on FireFunction.

### Out-of-Scope Use
The model was not optimized for the following use cases:
  * general multi-turn chat,
  * parallel and nested function calls in a single response. These can be broken into multiple messages.

## Example Usage

See [documentation](https://readme.fireworks.ai/docs/function-calling) for more detail.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import json

device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained("fireworks-ai/firefunction-v1", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("fireworks-ai/firefunction-v1")

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
    {'role': 'functions', 'content': functions},
    {'role': 'system', 'content': 'You are a helpful assistant with access to functions. Use them if required.'},
    {'role': 'user', 'content': 'Hi, can you tell me the current stock price of AAPL?'}
]

model_inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)

generated_ids = model.generate(model_inputs, max_new_tokens=128)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])
```

## Demo App

Check our easy-to-extend [demo chat app](https://github.com/fw-ai/forge/tree/main/apps/functional_chat) with function calling capabilities built on Firefunction model.
<video controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/64b6f3a72f5a966b9722de88/A2rFnYxM9xGCc_LiZeXe7.mp4"></video>
