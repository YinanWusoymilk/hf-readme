---
license: mit
---
# Model Card for functionary-small-v2.5

[https://github.com/MeetKai/functionary](https://github.com/MeetKai/functionary)

<img src="https://huggingface.co/meetkai/functionary-medium-v2.2/resolve/main/functionary_logo.jpg" alt="Functionary Logo" width="300"/>

Functionary is a language model that can interpret and execute functions/plugins.

The model determines when to execute functions, whether in parallel or serially, and can understand their outputs. It only triggers functions as needed. Function definitions are given as JSON Schema Objects, similar to OpenAI GPT function calls.

## Key Features

- Intelligent **parallel tool use**
- Able to analyze functions/tools outputs and provide relevant responses **grounded in the outputs**
- Able to decide **when to not use tools/call functions** and provide normal chat response
- Truly one of the best open-source alternative to GPT-4
- Support code interpreter

## How to Get Started

We provide custom code for parsing raw model responses into a JSON object containing role, content and tool_calls fields. This enables the users to read the function-calling output of the model easily.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("meetkai/functionary-small-v2.5")
model = AutoModelForCausalLM.from_pretrained("meetkai/functionary-small-v2.5", device_map="auto", trust_remote_code=True)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    }
                },
                "required": ["location"]
            }
        }
    }
]
messages = [{"role": "user", "content": "What is the weather in Istanbul and Singapore respectively?"}]

final_prompt = tokenizer.apply_chat_template(messages, tools, add_generation_prompt=True, tokenize=False)
inputs = tokenizer(final_prompt, return_tensors="pt").to("cuda")
pred = model.generate_tool_use(**inputs, max_new_tokens=128, tokenizer=tokenizer)
print(tokenizer.decode(pred.cpu()[0]))
```

## Prompt Template

We convert function definitions to a similar text to TypeScript definitions. Then we inject these definitions as system prompts. After that, we inject the default system prompt. Then we start the conversation messages.

This formatting is also available via our vLLM server which we process the functions into Typescript definitions encapsulated in a system message using a pre-defined Transformers Jinja chat template. This means that the lists of messages can be formatted for you with the apply_chat_template() method within our server:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="functionary")

client.chat.completions.create(
    model="path/to/functionary/model/",
    messages=[{"role": "user",
            "content": "What is the weather for Istanbul?"}
    ],
    tools=[{
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA"
                        }
                    },
                    "required": ["location"]
                }
            }
        }],
    tool_choice="auto"
)
```

will yield:

```
<|start_header_id|>system<|end_header_id|>

// Supported function definitions that should be called when necessary.
namespace functions {

// Get the current weather
type get_current_weather = (_: {
// The city and state, e.g. San Francisco, CA
location: string,
}) => any;

} // namespace functions<|eot_id|><|start_header_id|>user<|end_header_id|>

What is the weather for Istanbul?
```

A more detailed example is provided [here](https://github.com/MeetKai/functionary/blob/main/tests/prompt_test_v2.llama3.txt). 

## Run the model

We encourage users to run our models using our OpenAI-compatible vLLM server [here](https://github.com/MeetKai/functionary).

# The MeetKai Team
![MeetKai Logo](https://huggingface.co/meetkai/functionary-medium-v2.2/resolve/main/meetkai_logo.png "MeetKai Logo")
