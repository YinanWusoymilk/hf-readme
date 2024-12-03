---
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
pipeline_tag: text-generation
tags:
- llama-3.1
- conversational
- instruction following
- reasoning
- function calling
- mergekit
- finetuning
- axolotl
license: llama3.1
library_name: transformers
---

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/64c75c1237333ccfef30a602/tmOlbERGKP7JSODa6T06J.jpeg)

Authors: [Ashvini Kumar Jindal](https://www.linkedin.com/in/ashvini-jindal-26653262/), [Pawan Kumar Rajpoot](https://www.linkedin.com/in/pawanrajpoot/), [Ankur Parikh](https://www.linkedin.com/in/ankurnlpexpert/), [Akshita Sukhlecha](https://www.linkedin.com/in/akshita-sukhlecha/)

**🤗 Hugging Face Announcement Blog**: https://huggingface.co/blog/akjindal53244/llama31-storm8b

**🚀Ollama:** `ollama run ajindal/llama3.1-storm:8b`


## TL;DR

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64c75c1237333ccfef30a602/mDtDeiHwnBupw1k_n99Lf.png)

We present the [**Llama-3.1-Storm-8B**](https://huggingface.co/akjindal53244/Llama-3.1-Storm-8B) model that outperforms Meta AI's [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) and [Hermes-3-Llama-3.1-8B](https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B) models significantly across diverse benchmarks as shown in the performance comparison plot in the next section. Our approach consists of three key steps:
1. **Self-Curation**: We applied two self-curation methods to select approximately 1 million high-quality examples from a pool of ~2.8 million open-source examples. **Our curation criteria focused on educational value and difficulty level, using the same SLM for annotation instead of larger models (e.g. 70B, 405B).**
2. **Targeted fine-tuning**: We performed [Spectrum](https://arxiv.org/abs/2406.06623)-based targeted fine-tuning over the Llama-3.1-8B-Instruct model. The Spectrum method accelerates training by selectively targeting layer modules based on their signal-to-noise ratio (SNR), and freezing the remaining modules. In our work, 50% of layers are frozen.
3. **Model Merging**: We merged our fine-tuned model with the [Llama-Spark](https://huggingface.co/arcee-ai/Llama-Spark) model using [SLERP](https://huggingface.co/blog/mlabonne/merge-models#1-slerp) method. The merging method produces a blended model with characteristics smoothly interpolated from both parent models, ensuring the resultant model captures the essence of both its parents. [Llama-3.1-Storm-8B](https://huggingface.co/akjindal53244/Llama-3.1-Storm-8B) improves Llama-3.1-8B-Instruct across 10 diverse benchmarks. These benchmarks cover areas such as instruction-following, knowledge-driven QA, reasoning, truthful answer generation, and function calling.

## 🏆 Introducing Llama-3.1-Storm-8B
[**Llama-3.1-Storm-8B**](https://huggingface.co/akjindal53244/Llama-3.1-Storm-8B) builds upon the foundation of Llama-3.1-8B-Instruct, aiming to enhance both conversational and function calling capabilities within the 8B parameter model class.

As shown in the left subplot of the above figure, [**Llama-3.1-Storm-8B**](https://huggingface.co/akjindal53244/Llama-3.1-Storm-8B) model improves Meta-Llama-3.1-8B-Instruct across various benchmarks - Instruction-following ([IFEval](https://arxiv.org/abs/2311.07911)), Knowledge-driven QA benchmarks ([GPQA](https://arxiv.org/abs/2311.12022), [MMLU-Pro](https://arxiv.org/pdf/2406.01574)), Reasoning ([ARC-C](https://arxiv.org/abs/1803.05457), [MuSR](https://arxiv.org/abs/2310.16049), [BBH](https://arxiv.org/pdf/2210.09261)), Reduced Hallucinations ([TruthfulQA](https://arxiv.org/abs/2109.07958)), and Function-Calling ([BFCL](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard)). This improvement is particularly significant for AI developers and enthusiasts who work with limited computational resources.

We also benchmarked our model with the recently published model [Hermes-3-Llama-3.1-8B](https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B) built on top of the Llama-3.1-8B-Instruct model. As shown in the right subplot of the above figure, **Llama-3.1-Storm-8B outperforms Hermes-3-Llama-3.1-8B on 7 out of 9 benchmarks**, with Hermes-3-Llama-3.1-8B surpassing Llama-3.1-Storm-8B on the MuSR benchmark and both models showing comparable performance on the BBH benchmark.


## Llama-3.1-Storm-8B Model Strengths
Llama-3.1-Storm-8B is a powerful generalist model useful for diverse applications. We invite the AI community to explore [Llama-3.1-Storm-8B](https://huggingface.co/collections/akjindal53244/storm-66ba6c96b7e24ecb592787a9) and look forward to seeing how it will be utilized in various projects and applications.

<table>
  <tr>
   <td><strong>Model Strength</strong>
   </td>
   <td><strong>Relevant Benchmarks</strong>
   </td>
  <tr>
  <tr>
   <td>🎯 Improved Instruction Following
   </td>
   <td>IFEval Strict (+3.93%)
   </td>
  <tr>
  <tr>
   <td>🌐 Enhanced Knowledge Driven Question Answering
   </td>
   <td>GPQA (+7.21%), MMLU-Pro (+0.55%), AGIEval (+3.77%)
   </td>
  <tr>
  <tr>
   <td>🧠 Better Reasoning
   </td>
   <td>ARC-C (+3.92%), MuSR (+2.77%), BBH (+1.67%), AGIEval (+3.77%)
   </td>
  <tr>
  <tr>
   <td>🤖 Superior Agentic Capabilities
   </td>
   <td>BFCL: Overall Acc (+7.92%), BFCL: AST Summary (+12.32%)
   </td>
  <tr>
  <tr>
   <td>🚫 Reduced Hallucinations
   </td>
   <td>TruthfulQA (+9%)
   </td>
  <tr>
</table>

**Note**: All improvements are absolute gains over Meta-Llama-3.1-8B-Instruct.


## Llama-3.1-Storm-8B Models
1. `BF16`: [Llama-3.1-Storm-8B](https://huggingface.co/akjindal53244/Llama-3.1-Storm-8B)
2. ⚡ `FP8`: [Llama-3.1-Storm-8B-FP8-Dynamic](https://huggingface.co/akjindal53244/Llama-3.1-Storm-8B-FP8-Dynamic)
3. ⚡ `GGUF`: [Llama-3.1-Storm-8B-GGUF](https://huggingface.co/akjindal53244/Llama-3.1-Storm-8B-GGUF)
4. 🚀 Ollama: `ollama run ajindal/llama3.1-storm:8b`


## 💻 How to Use the Model
The Hugging Face `transformers` library loads the model in `bfloat16` by default. This is the type used by the [Llama-3.1-Storm-8B](https://huggingface.co/akjindal53244/Llama-3.1-Storm-8B) checkpoint, so it’s the recommended way to run to ensure the best results.

### Installation
```bash
pip install --upgrade "transformers>=4.43.2" torch==2.3.1 accelerate vllm==0.5.3.post1
```

Developers can easily integrate Llama-3.1-Storm-8B into their projects using popular libraries like Transformers and vLLM. The following sections illustrate the usage with simple hands-on examples:

### Conversational Use-case
#### Use with [🤗 Transformers](https://github.com/huggingface/transformers)
##### Using `transformers.pipeline()` API
```python
import transformers
import torch

model_id = "akjindal53244/Llama-3.1-Storm-8B"
pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is 2+2?"}
]

outputs = pipeline(messages, max_new_tokens=128, do_sample=True, temperature=0.01, top_k=100, top_p=0.95)
print(outputs[0]["generated_text"][-1])  # Expected Output: {'role': 'assistant', 'content': '2 + 2 = 4'}
```

##### Using `model.generate()` API
```bash
pip install flash_attn==2.6.3
```

```python
import torch
from transformers import AutoTokenizer, LlamaForCausalLM

# Apply Llama3.1 chat-template
def format_prompt(user_query):
    template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"""
    return template.format(user_query)


model_id = 'akjindal53244/Llama-3.1-Storm-8B'
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = LlamaForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    load_in_8bit=False,
    load_in_4bit=False,
    use_flash_attention_2=True
)

# Build final input prompt after applying chat-template
prompt = format_prompt("What is 2+2?")

input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to("cuda")
generated_ids = model.generate(input_ids, max_new_tokens=128, temperature=0.01, do_sample=True, eos_token_id=tokenizer.eos_token_id)
response = tokenizer.decode(generated_ids[0][input_ids.shape[-1]:], skip_special_tokens=True)
print(response)  # Expected Output: '2 + 2 = 4'
```

#### Use with [vLLM](https://github.com/vllm-project/vllm)
```python
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

model_id = "akjindal53244/Llama-3.1-Storm-8B"  # FP8 model: "akjindal53244/Llama-3.1-Storm-8B-FP8-Dynamic"
num_gpus = 1

tokenizer = AutoTokenizer.from_pretrained(model_id)
llm = LLM(model=model_id, tensor_parallel_size=num_gpus)
sampling_params = SamplingParams(max_tokens=128, temperature=0.01, top_k=100, top_p=0.95)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is 2+2?"}
]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize = False)
print(llm.generate([prompt], sampling_params)[0].outputs[0].text.strip())  # Expected Output: 2 + 2 = 4
```

#### Use with [LitGPT](https://github.com/Lightning-AI/litgpt)
```bash
pip install 'litgpt[all]'
litgpt download akjindal53244/Llama-3.1-Storm-8B --model_name meta-llama/Meta-Llama-3.1-8B
```

```python
from litgpt import LLM

llm = LLM.load(model="akjindal53244/Llama-3.1-Storm-8B")
llm.generate("What do Llamas eat?")
```

### Function Calling Use-case

[**Llama-3.1-Storm-8B**](https://huggingface.co/collections/akjindal53244/storm-66ba6c96b7e24ecb592787a9) has impressive function calling capabilities compared to Meta-Llama-3.1-8B-Instruct as demonstrated by the BFCL benchmark.

#### Prompt Format for Function Calling
Llama-3.1-Storm-8B is trained with specific system prompt for Function Calling:
```
You are a function calling AI model. You may call one or more functions to assist with the user query. Don't make assumptions about what values to plug into function. The user may use the terms function calling or tool use interchangeably.

Here are the available functions:
<tools>LIST_OF_TOOLS</tools>

For each function call return a json object with function name and arguments within <tool_call></tool_call> XML tags in the format:
<tool_call>{"tool_name": <function-name>, "tool_arguments": <args-dict>}</tool_call>
```
Above system prompt should be used with passing `LIST_OF_TOOLS` as input.


#### Use with [vLLM](https://github.com/vllm-project/vllm)
```python
import json
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

model_id = "akjindal53244/Llama-3.1-Storm-8B"  # FP8 model: "akjindal53244/Llama-3.1-Storm-8B-FP8-Dynamic"
num_gpus = 1

tokenizer = AutoTokenizer.from_pretrained(model_id)
llm = LLM(model=model_id, tensor_parallel_size=num_gpus)
sampling_params = SamplingParams(max_tokens=128, temperature=0.01, top_k=100, top_p=0.95)


def create_system_prompt(tools_list):
    system_prompt_format = """You are a function calling AI model. You may call one or more functions to assist with the user query. Don't make assumptions about what values to plug into function. The user may use the terms function calling or tool use interchangeably.

Here are the available functions:
<tools>{}</tools>

For each function call return a json object with function name and arguments within <tool_call></tool_call> XML tags in the format:
<tool_call>{"tool_name": <function-name>, "tool_arguments": <args-dict>}</tool_call>"""
    
    # Convert the tools list to a string representation
    tools_str = json.dumps(tools_list, ensure_ascii=False)
    # Format the system prompt with the tools list
    system_prompt = system_prompt_format.format(tools_str)
    return system_prompt


# Example tools list
tools_list = [
    {
        "name": "peers",
        "description": "Retrieves a list of company peers given a stock symbol.",
        "parameters": {
            "symbol": {
                "description": "The stock symbol for the company.",
                "type": "str",
                "default": ""
            }
        }
    },
    {
        "name": "web_chain_details",
        "description": "python",
        "parameters": {
            "chain_slug": {
                "description": "The slug identifier for the blockchain (e.g., 'ethereum' for Ethereum mainnet).",
                "type": "str",
                "default": "ethereum"
            }
        }
    }
]

# Create the system prompt with the tools list
system_prompt = create_system_prompt(tools_list)

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "I need to understand the details of the Ethereum blockchain for my cryptocurrency project. Can you fetch the details for 'ethereum'?"}
]

prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize = False)
print(llm.generate([prompt], sampling_params)[0].outputs[0].text.strip())  # Expected Output: <tool_call>{'tool_name': 'web_chain_details', 'tool_arguments': {'chain_slug': 'ethereum'}}</tool_call>
```

#### Use with [Ollama](https://ollama.com/)
```
import ollama

tools = [{
      'type': 'function',
      'function': {
        'name': 'get_current_weather',
        'description': 'Get the current weather for a city',
        'parameters': {
          'type': 'object',
          'properties': {
            'city': {
              'type': 'string',
              'description': 'The name of the city',
            },
          },
          'required': ['city'],
        },
      },
    },
    {
      'type': 'function',
      'function': {
        'name': 'get_places_to_vist',
        'description': 'Get places to visit in a city',
        'parameters': {
          'type': 'object',
          'properties': {
            'city': {
              'type': 'string',
              'description': 'The name of the city',
            },
          },
          'required': ['city'],
        },
      },
    },
  ]

response = ollama.chat(
    model='ajindal/llama3.1-storm:8b',
    messages=[
        {'role': 'system', 'content': 'Do not answer to nay vulgar questions.'},
        {'role': 'user', 'content': 'What is the weather in Toronto and San Francisco?'}
        ],
    tools=tools
)

print(response['message'])  # Expected Response: {'role': 'assistant', 'content': "<tool_call>{'tool_name': 'get_current_weather', 'tool_arguments': {'city': 'Toronto'}}</tool_call>"}
```


## Alignment Note
While **Llama-3.1-Storm-8B** did not undergo an explicit model alignment process, it may still retain some alignment properties inherited from the Meta-Llama-3.1-8B-Instruct model.

## Cite Our Work
```
@misc {ashvini_kumar_jindal_2024,
    author       = { {Ashvini Kumar Jindal, Pawan Kumar Rajpoot, Ankur Parikh, Akshita Sukhlecha} },
    title        = { Llama-3.1-Storm-8B },
    year         = 2024,
    url          = { https://huggingface.co/akjindal53244/Llama-3.1-Storm-8B },
    doi          = { 10.57967/hf/2902 },
    publisher    = { Hugging Face }
}
```

## Support Our Work
With 3 team-members spanned across 3 different time-zones, we have won [NeurIPS LLM Efficiency Challenge 2023](https://llm-efficiency-challenge.github.io/) and 4 other competitions in Finance and Arabic LLM space. We have also published [SOTA mathematical reasoning model](https://huggingface.co/akjindal53244/Arithmo-Mistral-7B).

**Llama-3.1-Storm-8B** is our most valuable contribution so far towards the open-source community. We are committed in developing efficient generalist LLMs. **We're seeking both computational resources and innovative collaborators to drive this initiative forward.**