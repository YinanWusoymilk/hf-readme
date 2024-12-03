---
license: apache-2.0
language:
- en
datasets:
- togethercomputer/RedPajama-Data-1T
- togethercomputer/RedPajama-Data-Instruct
widget:
- text: |-
    Label the sentences as either 'positive', 'negative', 'mixed', or 'neutral': 

    Sentence: I can say that there isn't anything I would change.
    Label: positive

    Sentence: I'm not sure about this.
    Label: neutral

    Sentence: I liked some parts but I didn't like other parts.
    Label: mixed

    Sentence: I think the background image could have been better.
    Label: negative

    Sentence: I really like it.
    Label:
  example_title: Sentiment Analysis
- text: |-
    Please answer the following question:

    Question: What is the capital of Canada?
    Answer: Ottawa

    Question: What is the currency of Switzerland?
    Answer: Swiss franc

    Question: In which country is Wisconsin located?
    Answer:
  example_title: Question Answering
- text: >-
    Given a news article, classify its topic.

    Possible labels: 1. World 2. Sports 3. Business 4. Sci/Tech


    Article: A nearby star thought to harbor comets and asteroids now appears to
    be home to planets, too.

    Label: Sci/Tech


    Article: Soaring crude prices plus worries about the economy and the outlook
    for earnings are expected to hang over the stock market next week during the
    depth of the summer doldrums.

    Label: Business


    Article: Murtagh a stickler for success Northeastern field hockey coach
    Cheryl Murtagh doesn't want the glare of the spotlight that shines on her to
    detract from a team that has been the America East champion for the past
    three years and has been to the NCAA tournament 13 times.

    Label::
  example_title: Topic Classification
- text: |-
    Paraphrase the given sentence into a different sentence.

    Input: Can you recommend some upscale restaurants in New York?
    Output: What upscale restaurants do you recommend in New York?

    Input: What are the famous places we should not miss in Paris?
    Output: Recommend some of the best places to visit in Paris?

    Input: Could you recommend some hotels that have cheap price in Zurich?
    Output:
  example_title: Paraphrasing
- text: >-
    Given a review from Amazon's food products, the task is to generate a short
    summary of the given review in the input.


    Input: I have bought several of the Vitality canned dog food products and
    have found them all to be of good quality. The product looks more like a
    stew than a processed meat and it smells better. My Labrador is finicky and
    she appreciates this product better than most.

    Output: Good Quality Dog Food


    Input: Product arrived labeled as Jumbo Salted Peanuts...the peanuts were
    actually small sized unsalted. Not sure if this was an error or if the
    vendor intended to represent the product as 'Jumbo'.

    Output: Not as Advertised


    Input: My toddler loves this game to a point where he asks for it. That's a
    big thing for me. Secondly, no glitching unlike one of their competitors
    (PlayShifu). Any tech I don’t have to reach out to support for help is a
    good tech for me. I even enjoy some of the games and activities in this.
    Overall, this is a product that shows that the developers took their time
    and made sure people would not be asking for refund. I’ve become bias
    regarding this product and honestly I look forward to buying more of this
    company’s stuff. Please keep up the great work.

    Output:
  example_title: Text Summarization
- text: |-
    Identify which sense of a word is meant in a given context.

    Context: The river overflowed the bank.
    Word: bank
    Sense: river bank

    Context: A mouse takes much more room than a trackball.
    Word: mouse
    Sense: computer mouse

    Context: The bank will not be accepting cash on Saturdays.
    Word: bank
    Sense: commercial (finance) banks

    Context: Bill killed the project
    Word: kill
    Sense:
  example_title: Word Sense Disambiguation
- text: >-
    Given a pair of sentences, choose whether the two sentences agree
    (entailment)/disagree (contradiction) with each other.

    Possible labels: 1. entailment 2. contradiction


    Sentence 1: The skier was on the edge of the ramp. Sentence 2: The skier was
    dressed in winter clothes.

    Label: entailment


    Sentence 1: The boy skated down the staircase railing. Sentence 2: The boy
    is a newbie skater.

    Label: contradiction


    Sentence 1: Two middle-aged people stand by a golf hole. Sentence 2: A
    couple riding in a golf cart.

    Label:
  example_title: Natural Language Inference
inference:
  parameters:
    temperature: 0.7
    top_p: 0.7
    top_k: 50
    max_new_tokens: 128
---

# RedPajama-INCITE-7B-Instruct

RedPajama-INCITE-7B-Instruct was developed by Together and leaders from the open-source AI community including Ontocord.ai, ETH DS3Lab, AAI CERC, Université de Montréal, MILA - Québec AI Institute, Stanford Center for Research on Foundation Models (CRFM), Stanford Hazy Research research group and LAION. 

The model was fine-tuned for few-shot applications on the data of [GPT-JT](https://huggingface.co/togethercomputer/GPT-JT-6B-v1), with exclusion of tasks that overlap with the HELM core scenarios.

  - Base Model: [RedPajama-INCITE-7B-Base](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base)
  - Instruction-tuned Version: [RedPajama-INCITE-7B-Instruct](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Instruct)
  - Chat Version: [RedPajama-INCITE-7B-Chat](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Chat)


## Model Details
- **Developed by**: Together Computer.
- **Model type**: Language Model
- **Language(s)**: English
- **License**: Apache 2.0
- **Model Description**: A 6.9B parameter pretrained language model.

# Quick Start

Please note that the model requires `transformers` version >= 4.25.1.

## GPU Inference

This requires a GPU with 16GB memory.

```python
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

MIN_TRANSFORMERS_VERSION = '4.25.1'

# check transformers version
assert transformers.__version__ >= MIN_TRANSFORMERS_VERSION, f'Please upgrade transformers to version {MIN_TRANSFORMERS_VERSION} or higher.'

# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Instruct")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Instruct", torch_dtype=torch.float16)
model = model.to('cuda:0')
# infer
prompt = "Q: The capital of France is?\nA:"
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
input_length = inputs.input_ids.shape[1]
outputs = model.generate(
    **inputs, max_new_tokens=128, do_sample=True, temperature=0.7, top_p=0.7, top_k=50, return_dict_in_generate=True
)
token = outputs.sequences[0, input_length:]
output_str = tokenizer.decode(token)
print(output_str)
"""
Paris
"""
```

## GPU Inference in Int8

This requires a GPU with 12GB memory.

To run inference with int8, please ensure you have installed accelerate and bitandbytes. You can install them with the following command:

```bash
pip install accelerate
pip install bitsandbytes
```

Then you can run inference with int8 as follows:

```python
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

MIN_TRANSFORMERS_VERSION = '4.25.1'

# check transformers version
assert transformers.__version__ >= MIN_TRANSFORMERS_VERSION, f'Please upgrade transformers to version {MIN_TRANSFORMERS_VERSION} or higher.'

# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Instruct")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Instruct", device_map='auto', torch_dtype=torch.float16, load_in_8bit=True)

# infer
prompt = "Q: The capital of France is?\nA:"
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
input_length = inputs.input_ids.shape[1]
outputs = model.generate(
    **inputs, max_new_tokens=128, do_sample=True, temperature=0.7, top_p=0.7, top_k=50, return_dict_in_generate=True
)
token = outputs.sequences[0, input_length:]
output_str = tokenizer.decode(token)
print(output_str)
"""
Paris
"""
```

## CPU Inference

```python
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

MIN_TRANSFORMERS_VERSION = '4.25.1'

# check transformers version
assert transformers.__version__ >= MIN_TRANSFORMERS_VERSION, f'Please upgrade transformers to version {MIN_TRANSFORMERS_VERSION} or higher.'

# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Instruct")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Instruct", torch_dtype=torch.bfloat16)
# infer
prompt = "Q: The capital of France is?\nA:"
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
input_length = inputs.input_ids.shape[1]
outputs = model.generate(
    **inputs, max_new_tokens=128, do_sample=True, temperature=0.7, top_p=0.7, top_k=50, return_dict_in_generate=True
)
token = outputs.sequences[0, input_length:]
output_str = tokenizer.decode(token)
print(output_str)
"""
Paris
"""
```

Please note that since `LayerNormKernelImpl` is not implemented in fp16 for CPU, we use `bfloat16` for CPU inference.


# Uses

## Direct Use 

Excluded uses are described below.

### Misuse, Malicious Use, and Out-of-Scope Use

It is the responsibility of the end user to ensure that the model is used in a responsible and ethical manner.

#### Out-of-Scope Use

RedPajama-INCITE-7B-Instruct is a language model and may not perform well for other use cases outside of its intended scope. 
For example, it may not be suitable for use in safety-critical applications or for making decisions that have a significant impact on individuals or society. 
It is important to consider the limitations of the model and to only use it for its intended purpose.

#### Misuse and Malicious Use

RedPajama-INCITE-7B-Instruct is designed for language modeling.
Misuse of the model, such as using it to engage in illegal or unethical activities, is strictly prohibited and goes against the principles of the project.

Using the model to generate content that is cruel to individuals is a misuse of this model. This includes, but is not limited to:

- Generating fake news, misinformation, or propaganda
- Promoting hate speech, discrimination, or violence against individuals or groups
- Impersonating individuals or organizations without their consent
- Engaging in cyberbullying or harassment
- Defamatory content
- Spamming or scamming
- Sharing confidential or sensitive information without proper authorization
- Violating the terms of use of the model or the data used to train it
- Creating automated bots for malicious purposes such as spreading malware, phishing scams, or spamming

## Limitations

RedPajama-INCITE-7B-Instruct, like other language models, has limitations that should be taken into consideration. 
For example, the model may not always provide accurate or relevant answers, particularly for questions that are complex, ambiguous, or outside of its training data. 
We therefore welcome contributions from individuals and organizations, and encourage collaboration towards creating a more robust and inclusive chatbot.

## Training

**Training Data**

Please refer to [togethercomputer/RedPajama-Data-1T](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)

**Training Procedure**

- **Hardware:** 8 A100
- **Optimizer:** Adam
- **Gradient Accumulations**: 1
- **Num of Tokens:** 1B tokens
- **Learning rate:** 1e-5

## Community

Join us on [Together Discord](https://discord.gg/6ZVDU8tTD4)