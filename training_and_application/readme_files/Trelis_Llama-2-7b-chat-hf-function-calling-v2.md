---
language:
- en
pipeline_tag: text-generation
inference: false
tags:
- facebook
- meta
- pytorch
- llama
- llama-2
- functions
- function calling
- sharded
---
# Function Calling Llama 2 + Yi + Mistral + Zephyr + Deepseek Coder Models (version 2)
- Function calling Llama extends the hugging face Llama 2 models with function calling capabilities.
- The model responds with a structured json argument with the function name and arguments.

**Recent Updates**
- Nov 15th 2023 -> added Yi 200k context models in 6B and 34B form.
- Nov 8th 2023 -> added Zephyr beta, an improved version of Mistral 7B (achieved via DPO)
- November 6th 2023 -> added Deepseek Coder 1.3B, 6.7B and 33B
- October 11th 2023 -> added Mistral 7B with function calling
- October 11th 2023 -> new models pushed, trained on an improved underlying dataset

**Improvements with v2**
1. Shortened syntax: Only function descriptions are needed for inference and no added instruction is required.
2. Function descriptions are moved outside of the system prompt. This avoids the behaviour of function calling being affected by how the system prompt had been trained to influence the model.

Latest Models:
- Yi-6B-200k context with function calling ([Base Model](Trelis/Yi-6B-200K-Llamafied-function-calling-v2)), ([PEFT Adapters](Trelis/Yi-6B-200K-Llamafied-function-calling-adapters-v2)) - Paid, [purchase here](https://buy.stripe.com/00gdRC7BX1Dt08gbJp)
- Yi-34B-200k context with function calling ([Base Model](Trelis/Yi-34B-200K-Llamafied-chat-SFT-function-calling-v2)), ([PEFT Adapters](Trelis/Yi-34B-200K-Llamafied-chat-SFT-function-calling-adapters-v2)), ([AWQ](Trelis/Yi-34B-200K-Llamafied-chat-SFT-function-calling-v2-AWQ)), ([GGUF - files are in the main branch of the base model]) - Paid, [purchase here](https://buy.stripe.com/fZe14Q7BX4PF7AIeVG)
- Deepseek-Coder-1.3B-Instruct with function calling ([Base Model](https://huggingface.co/Trelis/deepseek-coder-1.3b-instruct-function-calling-v2)), ([PEFT Adapters](https://huggingface.co/Trelis/deepseek-coder-1.3b-instruct-function-calling-adapters-v2/settings)) - Paid, [purchase here](https://buy.stripe.com/9AQbJubSda9Z8EM00A)
- Llama-7B-chat with function calling ([Base Model](https://huggingface.co/Trelis/Llama-2-7b-chat-hf-function-calling-v2)), ([PEFT Adapters](https://huggingface.co/Trelis/Llama-2-7b-chat-hf-function-calling-adapters-v2)), ([GGUF - files are in the main branch of the base model]) - Free
- zephyr-7b-beta with function calling ([Base Model](https://huggingface.co/Trelis/zephyr-7b-beta-function-calling-v2)), ([PEFT Adapters](https://huggingface.co/Trelis/zephyr-7b-beta-function-calling-adapters-v2)), ([GGUF - files are in the main branch of the base model]) - Paid, [purchase here](https://buy.stripe.com/14k00M4pLeqf9IQbJk)
- Mistral-7B-Instruct-v0.1 with function calling ([Base Model](https://huggingface.co/Trelis/Mistral-7B-Instruct-v0.1-function-calling-v2)), ([PEFT Adapters](https://huggingface.co/Trelis/Mistral-7B-Instruct-v0.1-function-calling-adapters-v2)) - Paid, [purchase here](https://buy.stripe.com/cN2cNybSdgyncV25kQ)
- Deepseek-Coder-6.7B-Instruct with function calling ([Base Model](https://huggingface.co/Trelis/deepseek-coder-6.7b-instruct-function-calling-v2)), ([PEFT Adapters](https://huggingface.co/Trelis/deepseek-coder-6.7b-instruct-function-calling-adapters-v2/settings)) - Paid, [purchase here](https://buy.stripe.com/cN27te5tPa9Z6wEdRo)
- Deepseek-Coder-33B-Instruct with function calling ([Base Model](https://huggingface.co/Trelis/deepseek-coder-33b-instruct-function-calling-v2)), ([PEFT Adapters](https://huggingface.co/Trelis/deepseek-coder-33b-instruct-function-calling-adapters-v2/settings)) - Paid, [purchase here](https://buy.stripe.com/9AQ6pabSd81RcV25kT)
- CodeLlama-34B-Instruct with function calling ([Base Model](https://huggingface.co/Trelis/CodeLlama-34b-Instruct-hf-function-calling-v2)), ([PEFT Adapters](https://huggingface.co/Trelis/CodeLlama-34b-Instruct-hf-function-calling-adapters-v2)) - Paid, [purchase here](https://buy.stripe.com/cN27teg8t2Hx5sA8wM)
- Llama-70B-chat with function calling ([Base Model](https://huggingface.co/Trelis/Llama-2-70b-chat-hf-function-calling-v2)), ([PEFT Adapters](https://huggingface.co/Trelis/Llama-2-70b-chat-hf-function-calling-adapters-v2)) - Paid, [purchase here](https://buy.stripe.com/8wMdRC1dzci75sA4gy)

Other Models:
- Llama-13B-chat with function calling ([Base Model](https://huggingface.co/Trelis/Llama-2-13b-chat-hf-function-calling-v2)), ([PEFT Adapters](https://huggingface.co/Trelis/Llama-2-13b-chat-hf-function-calling-adapters-v2)) - Paid, [purchase here](https://buy.stripe.com/9AQ7te3lHdmbdZ68wz)

## Which model is best for what?
1. Larger models are better at handling function calling. The cross entropy training losses are approximately 0.5 for 7B, 0.4 for 13B, 0.3 for 70B. The absolute numbers don't mean anything but the relative values offer a sense of relative performance.
1. Provide very clear function descriptions, including whether the arguments are required or what the default values should be.
1. Make sure to post-process the language model's response to check that all necessary information is provided by the user. If not, prompt the user to let them know they need to provide more info (e.g. their name, order number etc.)

Check out this video overview of performance [here](https://www.loom.com/share/8d7467de95e04af29ff428c46286946c?sid=683c970e-6063-4f1e-b184-894cc1d96115)

Some short tips based on models as of November 2023:
- DeepSeek Coder (all sizes) = best coding model.
- Yi 34B = best for long context.
- Llama 70B = strongest overall model (4k context).
- Mistral 7B = Best model if you have only 8 GB of VRAM (run with quantization).
Zephyr is better than Mistral 7B but is not openly licensed for commercial use.

## Licensing

Llama-7B with function calling is licensed according to the Meta Community license.

Mistral-7B, Llama-13B, Code-llama-34b, Llama-70B and Falcon-180B with function calling require the purchase of access.
- Commercial license purchase required per user.
- Licenses are not transferable to other users/entities.

Use of all Llama models with function calling is further subject to terms in the [Meta license](https://ai.meta.com/resources/models-and-libraries/llama-downloads/).

Yi models are subject to the Yi license, which permits commercial use as of Nov 15th 2023.

Zephr models were generated using Ultrachat, which relies on openai. OpenAI does not permit the use of it's models to train competitive models. This makes it unclear as to whether Zephyr may be used commercial. Buyers/users do so at their sole risk.

## Dataset

The dataset used for training this model can be found at [Trelis Function Calling Extended Dataset](https://huggingface.co/datasets/Trelis/function_calling_extended).

## Inference

!!! Make sure to check the prompt format below and adjust inference accordingly !!!

### Quick Start in Google Colab
Try out this notebook [fLlama_Inference notebook](https://colab.research.google.com/drive/1Ow5cQ0JNv-vXsT-apCceH6Na3b4L7JyW?usp=sharing)

### Text Generation Inference
You can this model with [text-generation-interface](https://github.com/huggingface/text-generation-inference) and [chat-ui](https://github.com/huggingface/chat-ui)

Here is the [github for setup](https://github.com/TrelisResearch/tgi-chat-ui-function-calling)

And here is a video showing it working with [llama-2-7b-chat-hf-function-calling-v2](https://huggingface.co/Trelis/Llama-2-7b-chat-hf-function-calling-v2) (note that we've now moved to v2)

Note that you'll still need to code the server-side handling of making the function calls (which obviously depends on what functions you want to use).

#### Runpod Quickstart
For a quickstart with runpod, you can use this template: [here](https://runpod.io/gsc?template=edxvuji38p&ref=jmfkcdio)

Once up and running, you can make queries to:
```
https://{YOUR_POD_ID}-8080.proxy.runpod.net
```
Then, you can make queries to the api as follows:
```
curl https://{YOUR_POD_ID}-8080.proxy.runpod.net/generate \
    -X POST \
    -d '{"inputs":"What is Deep Learning?","parameters":{"max_new_tokens":20}}' \
    -H 'Content-Type: application/json'
```
Or use /generate_stream for streaming. You can also write python scripts and use python to make requests. More info from the text-generation-inference [github repo](https://github.com/huggingface/text-generation-inference/)

### Run on your laptop
Run on your laptop [video and juypter notebook](https://youtu.be/nDJMHFsBU7M)

After running llama.cpp server, you can call the server with this command, with thanks to @jdo300:
```
import requests
import json

# Define the roles and markers
B_FUNC, E_FUNC = "<FUNCTIONS>", "</FUNCTIONS>\n\n"
B_INST, E_INST = "[INST] ", " [/INST]" #Llama style
# B_INST, E_INST = "\n### Instruction:\n", "\n### Response:\n" #DeepSeek Coder Style
# B_INST, E_INST = "Human: ", " Assistant: " #Yi Style

# Define the function metadata
function_metadata = {
    "function": "search_bing",
    "description": "Search the web for content on Bing. This allows users to search online/the internet/the web for content.",
    "arguments": [
        {
            "name": "query",
            "type": "string",
            "description": "The search query string"
        }
    ]
}

# Define the user prompt
user_prompt = 'Search for the latest news on AI.'

# Format the function list and prompt
function_list = json.dumps(function_metadata, indent=4)
prompt = f"{B_FUNC}{function_list.strip()}{E_FUNC}{B_INST}{user_prompt.strip()}{E_INST}\n\n"

# Define the API endpoint
url = "http:/localhost:8080/completion"

# Send the POST request to the API server
response = requests.post(url, json={"prompt": prompt})

# Print the response
print(response.json())
```

## Syntax

### Prompt Templates

The function descriptions must be wrapped within a function block. You can put this function below before or after the system message block.

Example without a system message:
```
  # Define the roles and markers
  B_FUNC, E_FUNC = "<FUNCTIONS>", "</FUNCTIONS>\n\n"
  B_INST, E_INST = "[INST] ", " [/INST]" #Llama style
  # B_INST, E_INST = "\n### Instruction:\n", "\n### Response:\n" #DeepSeek Coder Style
  # B_INST, E_INST = "Human: ", " Assistant: " #Yi Style

  functionList = {function_1_metadata}{function_2_metadata}...
  user_prompt = '...'

  # Format your prompt template
  prompt = f"{B_FUNC}{functionList.strip()}{E_FUNC}{B_INST}{user_prompt.strip()}{E_INST}\n\n"
```

Example with a system message:
```
  # Define the roles and markers
  B_FUNC, E_FUNC = "<FUNCTIONS>", "</FUNCTIONS>\n\n"
  B_INST, E_INST = "[INST] ", " [/INST]" #Llama style
  # B_INST, E_INST = "\n### Instruction:\n", "\n### Response:\n" #DeepSeek Coder Style
  # B_INST, E_INST = "Human: ", " Assistant: " #Yi Style
  B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

  # assuming functionList is defined as above
  system_prompt = '...'
  user_prompt = '...'

  # Format your prompt template
  prompt = f"{B_FUNC}{functionList.strip()}{E_FUNC}{B_INST}{B_SYS}{system_prompt.strip()}{E_SYS}{user_prompt.strip()}{E_INST}\n\n"

```
Notice that the function block is placed at the very start of the sequence, before 'B_INST'.

### Function Metadata Template

functionMetadata should be a string representation of a JSON object, like this:

```
"functionMetadata": {
        "function": "search_bing",
        "description": "Search the web for content on Bing. This allows users to search online/the internet/the web for content.",
        "arguments": [
            {
                "name": "query",
                "type": "string",
                "description": "The search query string"
            }
        ]
    }
'''
```

and the language model should respond with a json object formatted like this:
```
{
    "function": "function_name",
    "arguments": {
        "argument1": "argument_value",
        "argument2": "argument_value"
    }
}
```

It is recommended to handle cases where:
- There is no json object in the response
- The response contains text in addition to the json response

### Sample functionList

```
{
    "function": "search_bing",
    "description": "Search the web for content on Bing. This allows users to search online/the internet/the web for content.",
    "arguments": [
        {
            "name": "query",
            "type": "string",
            "description": "The search query string"
        }
    ]
}

{
    "function": "search_arxiv",
    "description": "Search for research papers on ArXiv. Make use of AND, OR and NOT operators as appropriate to join terms within the query.",
    "arguments": [
        {
            "name": "query",
            "type": "string",
            "description": "The search query string"
        }
    ]
}
```

### Training Set Argument Types
Models were fine-tuned on argument types including strings, numbers and arrays. The training set includes function calls with 0, 1, 2 or 3 arguments. The larger the model the better it will generalise beyond these types.

Here is a function call with an array:
```
{ "function": "delete_file", "arguments": { "fileNames": [ "Dissecting Transformer Length Extrapolation via The Lens of Receptive Field Analysis", "Luna- Linear Unified Nested Attention", "Substack_Inc_2021_2020_GAAP_Audited_Financials" ] } }
```
Here is a function call with three arguments:
```
{ "function": "save_chat", "arguments": { "fileName": "KiteDiscussion", "fileDescription": "Notes on one and two stringed kites", "fileContent": "--- **Types of Kite** There are one and two string kites. The two string ones are easier to control, although you can get the cords tangled. The one-stringed ones are sometimes used for kite fights, and you lose the kite and have to run after it if the string breaks. ---" } }
```

~

Below follows information on the original Llama 2 model...

~

# **Llama 2**
Llama 2 is a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. This is the repository for the 7B fine-tuned model, optimized for dialogue use cases and converted for the Hugging Face Transformers format. Links to other models can be found in the index at the bottom.

## Model Details
*Note: Use of this model is governed by the Meta license. In order to download the model weights and tokenizer, please visit the [website](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) and accept our License before requesting access here.*

Meta developed and publicly released the Llama 2 family of large language models (LLMs), a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. Our fine-tuned LLMs, called Llama-2-Chat, are optimized for dialogue use cases. Llama-2-Chat models outperform open-source chat models on most benchmarks we tested, and in our human evaluations for helpfulness and safety, are on par with some popular closed-source models like ChatGPT and PaLM.

**Model Developers** Meta

**Variations** Llama 2 comes in a range of parameter sizes — 7B, 13B, and 70B — as well as pretrained and fine-tuned variations.

**Input** Models input text only.

**Output** Models generate text only.

**Model Architecture** Llama 2 is an auto-regressive language model that uses an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align to human preferences for helpfulness and safety.


||Training Data|Params|Content Length|GQA|Tokens|LR|
|---|---|---|---|---|---|---|
|Llama 2|*A new mix of publicly available online data*|7B|4k|&#10007;|2.0T|3.0 x 10<sup>-4</sup>|
|Llama 2|*A new mix of publicly available online data*|13B|4k|&#10007;|2.0T|3.0 x 10<sup>-4</sup>|
|Llama 2|*A new mix of publicly available online data*|70B|4k|&#10004;|2.0T|1.5 x 10<sup>-4</sup>|

*Llama 2 family of models.* Token counts refer to pretraining data only. All models are trained with a global batch-size of 4M tokens. Bigger models -  70B -- use Grouped-Query Attention (GQA) for improved inference scalability.

**Model Dates** Llama 2 was trained between January 2023 and July 2023.

**Status** This is a static model trained on an offline dataset. Future versions of the tuned models will be released as we improve model safety with community feedback.

**License** A custom commercial license is available at: [https://ai.meta.com/resources/models-and-libraries/llama-downloads/](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)

**Research Paper** ["Llama-2: Open Foundation and Fine-tuned Chat Models"](arxiv.org/abs/2307.09288)

## Intended Use
**Intended Use Cases** Llama 2 is intended for commercial and research use in English. Tuned models are intended for assistant-like chat, whereas pretrained models can be adapted for a variety of natural language generation tasks.

To get the expected features and performance for the chat versions, a specific formatting needs to be followed, including the `INST` and `<<SYS>>` tags, `BOS` and `EOS` tokens, and the whitespaces and breaklines in between (we recommend calling `strip()` on inputs to avoid double-spaces). See our reference code in github for details: [`chat_completion`](https://github.com/facebookresearch/llama/blob/main/llama/generation.py#L212).

**Out-of-scope Uses** Use in any manner that violates applicable laws or regulations (including trade compliance laws).Use in languages other than English. Use in any other way that is prohibited by the Acceptable Use Policy and Licensing Agreement for Llama 2.

## Hardware and Software
**Training Factors** We used custom training libraries, Meta's Research Super Cluster, and production clusters for pretraining. Fine-tuning, annotation, and evaluation were also performed on third-party cloud compute.

**Carbon Footprint** Pretraining utilized a cumulative 3.3M GPU hours of computation on hardware of type A100-80GB (TDP of 350-400W). Estimated total emissions were 539 tCO2eq, 100% of which were offset by Meta’s sustainability program.

||Time (GPU hours)|Power Consumption (W)|Carbon Emitted(tCO<sub>2</sub>eq)|
|---|---|---|---|
|Llama 2 7B|184320|400|31.22|
|Llama 2 13B|368640|400|62.44|
|Llama 2 70B|1720320|400|291.42|
|Total|3311616||539.00|

**CO<sub>2</sub> emissions during pretraining.** Time: total GPU time required for training each model. Power Consumption: peak power capacity per GPU device for the GPUs used adjusted for power usage efficiency. 100% of the emissions are directly offset by Meta's sustainability program, and because we are openly releasing these models, the pretraining costs do not need to be incurred by others.

## Training Data
**Overview** Llama 2 was pretrained on 2 trillion tokens of data from publicly available sources. The fine-tuning data includes publicly available instruction datasets, as well as over one million new human-annotated examples. Neither the pretraining nor the fine-tuning datasets include Meta user data.

**Data Freshness** The pretraining data has a cutoff of September 2022, but some tuning data is more recent, up to July 2023.

## Evaluation Results

In this section, we report the results for the Llama 1 and Llama 2 models on standard academic benchmarks.For all the evaluations, we use our internal evaluations library.

|Model|Size|Code|Commonsense Reasoning|World Knowledge|Reading Comprehension|Math|MMLU|BBH|AGI Eval|
|---|---|---|---|---|---|---|---|---|---|
|Llama 1|7B|14.1|60.8|46.2|58.5|6.95|35.1|30.3|23.9|
|Llama 1|13B|18.9|66.1|52.6|62.3|10.9|46.9|37.0|33.9|
|Llama 1|33B|26.0|70.0|58.4|67.6|21.4|57.8|39.8|41.7|
|Llama 1|65B|30.7|70.7|60.5|68.6|30.8|63.4|43.5|47.6|
|Llama 2|7B|16.8|63.9|48.9|61.3|14.6|45.3|32.6|29.3|
|Llama 2|13B|24.5|66.9|55.4|65.8|28.7|54.8|39.4|39.1|
|Llama 2|70B|**37.5**|**71.9**|**63.6**|**69.4**|**35.2**|**68.9**|**51.2**|**54.2**|

**Overall performance on grouped academic benchmarks.** *Code:* We report the average pass@1 scores of our models on HumanEval and MBPP. *Commonsense Reasoning:* We report the average of PIQA, SIQA, HellaSwag, WinoGrande, ARC easy and challenge, OpenBookQA, and CommonsenseQA. We report 7-shot results for CommonSenseQA and 0-shot results for all other benchmarks. *World Knowledge:* We evaluate the 5-shot performance on NaturalQuestions and TriviaQA and report the average. *Reading Comprehension:* For reading comprehension, we report the 0-shot average on SQuAD, QuAC, and BoolQ. *MATH:* We report the average of the GSM8K (8 shot) and MATH (4 shot) benchmarks at top 1.

|||TruthfulQA|Toxigen|
|---|---|---|---|
|Llama 1|7B|27.42|23.00|
|Llama 1|13B|41.74|23.08|
|Llama 1|33B|44.19|22.57|
|Llama 1|65B|48.71|21.77|
|Llama 2|7B|33.29|**21.25**|
|Llama 2|13B|41.86|26.10|
|Llama 2|70B|**50.18**|24.60|

**Evaluation of pretrained LLMs on automatic safety benchmarks.** For TruthfulQA, we present the percentage of generations that are both truthful and informative (the higher the better). For ToxiGen, we present the percentage of toxic generations (the smaller the better).


|||TruthfulQA|Toxigen|
|---|---|---|---|
|Llama-2-Chat|7B|57.04|**0.00**|
|Llama-2-Chat|13B|62.18|**0.00**|
|Llama-2-Chat|70B|**64.14**|0.01|

**Evaluation of fine-tuned LLMs on different safety datasets.** Same metric definitions as above.

## Ethical Considerations and Limitations
Llama 2 is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2, developers should perform safety testing and tuning tailored to their specific applications of the model.

Please see the Responsible Use Guide available at [https://ai.meta.com/llama/responsible-use-guide/](https://ai.meta.com/llama/responsible-use-guide)

## Reporting Issues
Please report any software “bug,” or other problems with the models through one of the following means:
- Reporting issues with the model: [github.com/facebookresearch/llama](http://github.com/facebookresearch/llama)
- Reporting problematic content generated by the model: [developers.facebook.com/llama_output_feedback](http://developers.facebook.com/llama_output_feedback)
- Reporting bugs and security concerns: [facebook.com/whitehat/info](http://facebook.com/whitehat/info)

## Llama Model Index
|Model|Llama2|Llama2-hf|Llama2-chat|Llama2-chat-hf|
|---|---|---|---|---|
|7B| [Link](https://huggingface.co/llamaste/Llama-2-7b) | [Link](https://huggingface.co/llamaste/Llama-2-7b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-7b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-7b-chat-hf)|
|13B| [Link](https://huggingface.co/llamaste/Llama-2-13b) | [Link](https://huggingface.co/llamaste/Llama-2-13b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-13b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-13b-hf)|
|70B| [Link](https://huggingface.co/llamaste/Llama-2-70b) | [Link](https://huggingface.co/llamaste/Llama-2-70b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-70b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-70b-hf)|