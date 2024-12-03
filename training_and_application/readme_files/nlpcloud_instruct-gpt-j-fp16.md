---
license: gpl-3.0
datasets:
- nlpcloud/instructions-dataset-adapted-from-stanford-alpaca-for-gpt-j
widget:
- example_title: "Spelling Correction"
  text: Correct spelling and grammar from the following text.\nI do not wan to go\n
- example_title: "Story Generation"
  text: Write a short story about space.\n
---

# Description

This model demonstrates that GPT-J can work perfectly well as an "instruct" model when properly fine-tuned. It is an fp16 version that makes it easy to deploy the model on entry level GPU like an NVIDIA Tesla T4. Want to know more about NLP Cloud? [Have a look at our platform here](https://nlpcloud.com).

We fine-tuned GPT-J on an instruction dataset created by the [Stanford Alpaca team](https://github.com/tatsu-lab/stanford_alpaca). You can find the original dataset [here](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json).

The dataset was slightly reworked in order to match the GPT-J fine-tuning format with [Mesh Transformer Jax](https://github.com/kingoflolz/mesh-transformer-jax) on TPUs. [Here is the final dataset we used](https://huggingface.co/datasets/nlpcloud/instructions-dataset-adapted-from-stanford-alpaca-for-gpt-j).

The base GPT-J model needs few-shot learning in order to properly understand what you want. [See more details here about how to properly use few-shot learning](https://nlpcloud.com/effectively-using-gpt-j-gpt-neo-gpt-3-alternatives-few-shot-learning.html). For example let's say that you want to correct spelling with GPT-J. Here is an example of a prompt you had to use:

```text
I love goin to the beach.
Correction: I love going to the beach.
###
Let me hav it!
Correction: Let me have it!
###
It have too many drawbacks.
Correction: It has too many drawbacks.
###
I do not wan to go
Correction:
```

Now, with Instruct GPT-J, you can ask things in natural language "like a human":

```text
Correct spelling and grammar from the following text.
I do not wan to go\n
```

Which returns the following:

```text
I do not want to go.
```

You can also perfectly keep using few-shot learning on this model for very advanced use cases.

## How To Use The Model?

Using the model in fp16 with the text generation pipeline, here is what you can do:

```python
from transformers import pipeline
import torch

generator = pipeline(model="nlpcloud/instruct-gpt-j-fp16", torch_dtype=torch.float16, device=0)

prompt = "Correct spelling and grammar from the following text.\nI do not wan to go\n"

print(generator(prompt))
```

You can also use the `generate()` function. Here is what you can do:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained('nlpcloud/instruct-gpt-j-fp16')
generator = AutoModelForCausalLM.from_pretrained("nlpcloud/instruct-gpt-j-fp16",torch_dtype=torch.float16).cuda()

prompt = "Correct spelling and grammar from the following text.\nI do not wan to go\n"

inputs = tokenizer(prompt, return_tensors='pt')
outputs = generator.generate(inputs.input_ids.cuda())

print(tokenizer.decode(outputs[0]))
```

## Special Note About Input Format

Due to the way this model was fine-tuned, you should always use new lines at the end of your instructions.

For example the following instruction might not always work:

```text
Correct spelling and grammar from the following text.\nI do not wan to go
```

But this one would:

```text
Correct spelling and grammar from the following text.\nI do not wan to go\n
```

## Hardware Requirements

This model is an fp16 version of our fine-tuned model, which works very well on a GPU with 16GB of VRAM like an NVIDIA Tesla T4.

We did not notice any difference between the fp32 and fp16 versions in terms of quality.