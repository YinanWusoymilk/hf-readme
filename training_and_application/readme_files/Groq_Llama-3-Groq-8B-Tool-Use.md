---
language:
- en
license: llama3
base_model: meta-llama/Meta-Llama-3-8B
pipeline_tag: text-generation
tags:
- facebook
- meta
- pytorch
- llama
- llama-3
- groq
- tool-use
- function-calling
---

# Llama-3-Groq-8B-Tool-Use

This is the 8B parameter version of the Llama 3 Groq Tool Use model, specifically designed for advanced tool use and function calling tasks.

## Model Details

- **Model Type:** Causal language model fine-tuned for tool use
- **Language(s):** English
- **License:** Meta Llama 3 Community License
- **Model Architecture:** Optimized transformer
- **Training Approach:** Full fine-tuning and Direct Preference Optimization (DPO) on Llama 3 8B base model
- **Input:** Text
- **Output:** Text, with enhanced capabilities for tool use and function calling

## Performance

- **Berkeley Function Calling Leaderboard (BFCL) Score:** 89.06% overall accuracy
- This score represents the best performance among all open-source 8B LLMs on the BFCL

## Usage and Limitations

This model is designed for research and development in tool use and function calling scenarios. It excels at tasks involving API interactions, structured data manipulation, and complex tool use. However, users should note:

- For general knowledge or open-ended tasks, a general-purpose language model may be more suitable
- The model may still produce inaccurate or biased content in some cases
- Users are responsible for implementing appropriate safety measures for their specific use case

Note the model is quite sensitive to the `temperature` and `top_p` sampling configuration. Start at `temperature=0.5, top_p=0.65` and move up or down as needed.

Text prompt example:

We'd like to give a special shoutout to [@NousResearch](https://x.com/NousResearch) for pushing open source tool use forward with their public & open exploration of tool use in LLMs.

```
<|start_header_id|>system<|end_header_id|>

You are a function calling AI model. You are provided with function signatures within <tools></tools> XML tags. You may call one or more functions to assist with the user query. Don't make assumptions about what values to plug into functions. For each function call return a json object with function name and arguments within <tool_call></tool_call> XML tags as follows:
<tool_call>
{"name": <function-name>,"arguments": <args-dict>}
</tool_call>

Here are the available tools:
<tools> {
    "name": "get_current_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
        "properties": {
            "location": {
                "description": "The city and state, e.g. San Francisco, CA",
                "type": "string"
            },
            "unit": {
                "enum": [
                    "celsius",
                    "fahrenheit"
                ],
                "type": "string"
            }
        },
        "required": [
            "location"
        ],
        "type": "object"
    }
} </tools><|eot_id|><|start_header_id|>user<|end_header_id|>

What is the weather like in San Francisco?<|eot_id|><|start_header_id|>assistant<|end_header_id|>

<tool_call>
{"id":"call_deok","name":"get_current_weather","arguments":{"location":"San Francisco","unit":"celsius"}}
</tool_call><|eot_id|><|start_header_id|>tool<|end_header_id|>

<tool_response>
{"id":"call_deok","result":{"temperature":"72","unit":"celsius"}}
</tool_response><|eot_id|><|start_header_id|>assistant<|end_header_id|>

```

## Ethical Considerations

While fine-tuned for tool use, this model inherits the ethical considerations of the base Llama 3 model. Use responsibly and implement additional safeguards as needed for your application.

## Availability

The model is available through:
- [Groq API console](https://console.groq.com)
- [Hugging Face](https://huggingface.co/Groq/Llama-3-Groq-8B-Tool-Use)

For full details on responsible use, ethical considerations, and latest benchmarks, please refer to the [official Llama 3 documentation](https://llama.meta.com/) and the Groq model card.
