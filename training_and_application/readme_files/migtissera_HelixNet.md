---
license: apache-2.0
---

# HelixNet

![HelixNet](https://huggingface.co/migtissera/HelixNet/resolve/main/media/HelixNet.png)

HelixNet is a Deep Learning architecture consisting of 3 x Mistral-7B LLMs. It has an `actor`, a `critic`, and a `regenerator`. The `actor` LLM produces an initial response to a given system-context and a question. The `critic` then takes in as input, a tuple of (system-context, question, response) and provides a critique based on the provided answer to the given system-context and the question. Its job is not to criticize, but to provide an intelligent critique so that the answer can be modified/regenerated to address the question better. Finally, the `regenerator` takes in a tuple of (system-context, question, response, critique) and regenerates the answer.

HelixNet is insprired from an actor-critic architecture most prominent in Reinforcement Learning algorithms. The name derives from Helix, referring to the spiral structure of a DNA molecule. It symbolizes the intertwined nature of the three networks, working in tandem, much like the strands of a DNA molecule.

HelixNet regenerates very pleasing and accurate responses, due to the entropy preservation of the regenerator. The regenerator was only trained on a dataset of 1000 samples, similar to Meta's LIMA. The actor network here was trained on about 250K very high-quality samples, and the critic network was trained on further 10K samples.

# Training Methodology

## Phase 1: Actor

The actor network was trained with Supervised Fine-Tuning, on 250K very high-quality samples. It has 75K of Open-Orca's Chain-of-Thought data, and a mixture of Dolphin (GPT-4), SynthIA's Tree-of-Thought data.

Here are the results for the Actor network on metrics used by [HuggingFaceH4 Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

||||
|:------:|:--------:|:-------:|
|**Task**|**Metric**|**Value**|
|*arc_challenge*|acc_norm|62.28|
|*hellaswag*|acc_norm|83.22|
|*mmlu*|acc_norm|63.10|
|*truthfulqa_mc*|mc2|50.10|
|**Total Average**|-|**0.64675**||


## Phase 2: Critic

To train the critic, the following process was followed:
- Use Actor, and send 10K system-context and question pairs. Generate responses
- Use the (system-context, question, response) tuples to generate critiques. Used OpenAI's GPT-4.

Using the above training dataset, a Mistral-7B was fine-tuned.

## Phase 3: Regenerator
- Use the (system-context, question, response, critique) tuples to regenerate the answers. Used OpenAI's GPT-4.

A thrid LLM was fine-tuned using the above data.


# Reusability of the critic and the regenerator

The `critic` and the `regenerator` was tested not only on the accopanying actor model, but 13B and 70B SynthIA models as well. They seem to be readily transferrable, as the function that it has learnt is to provide an intelligent critique and then a regeneration of the original response. Please feel free to try out other models as the `actor`. However, the architecture works best with all three as presented here in HelixNet.

# Sample Generations

![HelixNet](https://huggingface.co/migtissera/HelixNet/resolve/main/media/sample-answer.png)

![HelixNet](https://huggingface.co/migtissera/HelixNet/resolve/main/media/sample-critique.png)

![HelixNet](https://huggingface.co/migtissera/HelixNet/resolve/main/media/sample-regeneration.png)


# Prompt format:

```
SYSTEM: Elaborate on the topic using a Tree of Thoughts and backtrack when necessary to construct a clear, cohesive Chain of Thought reasoning. Always answer without hesitation.
USER: What is the relationship between Earth's atmosphere, magnetic field and gravity?
ASSISTANT:
```

# Example Usage

## Code example (Verbose):

The following is a code example on how to use HelixNet. No special system-context messages are needed for the `critic` and the `regenerator`.

```python
import torch, json
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path_actor = "/home/ubuntu/llm/HelixNet/actor"
model_path_critic = "/home/ubuntu/llm/HelixNet/critic"
model_path_regenerator = "/home/ubuntu/llm/HelixNet/regenerator"

def load_model(model_path):
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map="cuda",
        load_in_4bit=False,
        trust_remote_code=True,
    )
    return model

def load_tokenizer(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    return tokenizer

model_actor = load_model(model_path_actor)
model_critic = load_model(model_path_critic)
model_regenerator = load_model(model_path_regenerator)

tokenizer_actor = load_tokenizer(model_path_actor)
tokenizer_critic = load_tokenizer(model_path_critic)
tokenizer_regenerator = load_tokenizer(model_path_regenerator)

def generate_text(instruction, model, tokenizer):
    tokens = tokenizer.encode(instruction)
    tokens = torch.LongTensor(tokens).unsqueeze(0)
    tokens = tokens.to("cuda")

    instance = {
        "input_ids": tokens,
        "top_p": 1.0,
        "temperature": 0.75,
        "generate_len": 1024,
        "top_k": 50,
    }

    length = len(tokens[0])
    with torch.no_grad():
        rest = model.generate(
            input_ids=tokens,
            max_length=length + instance["generate_len"],
            use_cache=True,
            do_sample=True,
            top_p=instance["top_p"],
            temperature=instance["temperature"],
            top_k=instance["top_k"],
            num_return_sequences=1,
        )
    output = rest[0][length:]
    string = tokenizer.decode(output, skip_special_tokens=True)
    return f"{string}"

system_prompt = "You are HelixNet. Elaborate on the topic using a Tree of Thoughts and backtrack when necessary to construct a clear, cohesive Chain of Thought reasoning. Always answer without hesitation."
  

while True:
    user_input = input("You: ")
    
    prompt_actor = f"SYSTEM: {system_prompt} \nUSER: {user_input} \nASSISTANT: "
    actor_response = generate_text(prompt_actor, model_actor, tokenizer_actor)
    print(f"ACTOR: {actor_response}\n\n")
   
    prompt_critic = f"SYSTEM: {system_prompt} \nUSER: {user_input} \nRESPONSE: {actor_response} \nCRITIQUE:"
    critic_response = generate_text(prompt_critic, model_critic, tokenizer_critic)
    print(f"CRITIQUE: {critic_response}\n\n")

    prompt_regenerator = f"SYSTEM: {system_prompt} \nUSER: {user_input} \nRESPONSE: {actor_response} \nCRITIQUE: {critic_response} \nREGENERATOR: REGENERATED ANSWER:"
    regenerator_response = generate_text(prompt_regenerator, model_regenerator, tokenizer_regenerator)
    print(f"REGENERATION: {regenerator_response}")

```



## Code Example (Continuing a conversation)

To have a back-and-forth conversation, only carry forward the system-context, questions and regenerations as shown below.

```python
import torch, json
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path_actor = "/home/ubuntu/llm/HelixNet/actor"
model_path_critic = "/home/ubuntu/llm/HelixNet/critic"
model_path_regenerator = "/home/ubuntu/llm/HelixNet/regenerator"

def load_model(model_path):
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map="cuda",
        load_in_4bit=False,
        trust_remote_code=True,
    )
    return model

def load_tokenizer(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    return tokenizer

model_actor = load_model(model_path_actor)
model_critic = load_model(model_path_critic)
model_regenerator = load_model(model_path_regenerator)

tokenizer_actor = load_tokenizer(model_path_actor)
tokenizer_critic = load_tokenizer(model_path_critic)
tokenizer_regenerator = load_tokenizer(model_path_regenerator)

def generate_text(instruction, model, tokenizer):
    tokens = tokenizer.encode(instruction)
    tokens = torch.LongTensor(tokens).unsqueeze(0)
    tokens = tokens.to("cuda")

    instance = {
        "input_ids": tokens,
        "top_p": 1.0,
        "temperature": 0.75,
        "generate_len": 1024,
        "top_k": 50,
    }

    length = len(tokens[0])
    with torch.no_grad():
        rest = model.generate(
            input_ids=tokens,
            max_length=length + instance["generate_len"],
            use_cache=True,
            do_sample=True,
            top_p=instance["top_p"],
            temperature=instance["temperature"],
            top_k=instance["top_k"],
            num_return_sequences=1,
        )
    output = rest[0][length:]
    string = tokenizer.decode(output, skip_special_tokens=True)
    return f"{string}"

system_prompt = "You are HelixNet. Elaborate on the topic using a Tree of Thoughts and backtrack when necessary to construct a clear, cohesive Chain of Thought reasoning. Always answer without hesitation."
  
conversation = f"SYSTEM:{system_prompt}"

while True:
    user_input = input("You: ")

    prompt_actor = f"{conversation} \nUSER: {user_input} \nASSISTANT: "
    actor_response = generate_text(prompt_actor, model_actor, tokenizer_actor)
    print("Generated ACTOR RESPONSE")

    prompt_critic = f"SYSTEM: {system_prompt} \nUSER: {user_input} \nRESPONSE: {actor_response} \nCRITIQUE:"
    critic_response = generate_text(prompt_critic, model_critic, tokenizer_critic)
    print("Generated CRITIQUE")

    prompt_regenerator = f"SYSTEM: {system_prompt} \nUSER: {user_input} \nRESPONSE: {actor_response} \nCRITIQUE: {critic_response} \nREGENERATOR: REGENERATED ANSWER:"
    regenerator_response = generate_text(prompt_regenerator, model_regenerator, tokenizer_regenerator)
    print("Generated REGENERATION")

    conversation = f"{conversation} \nUSER: {user_input} \nASSISTANT: {regenerator_response}"
    print(conversation)
```

# Quantized versions by the community

- https://huggingface.co/LoneStriker?search_models=helixnet

# Updates:
 
- Added a fix suggested by user @mammour to stop returing "REGENERATED ANSWER" on the regenerator. Thanks for the fix!