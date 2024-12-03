---
license: apache-2.0
language:
- en
---
 
***<p style="font-size: 24px">Feel free to try out our [OpenChatKit feedback app](https://huggingface.co/spaces/togethercomputer/OpenChatKit)!</p>***

# GPT-NeoXT-Chat-Base-20B-v0.16

> TLDR: As part of OpenChatKit (codebase available [here](https://github.com/togethercomputer/OpenChaT)),
> GPT-NeoXT-Chat-Base-20B-v0.16 is a 20B parameter language model, fine-tuned from EleutherAI’s GPT-NeoX with over 40 million instructions on 100% carbon negative compute.

GPT-NeoXT-Chat-Base-20B-v0.16 is based on ElutherAI’s GPT-NeoX model, and is fine-tuned with data focusing on dialog-style interactions. 
We focused the tuning on several tasks such as question answering, classification, extraction, and summarization. 
We’ve fine-tuned the model with a collection of 43 million high-quality instructions.
Together partnered with LAION and Ontocord.ai, who both helped curate the dataset the model is based on.
You can read more about this process and the availability of this dataset in LAION’s blog post [here](https://laion.ai/blog/oig-dataset/). 

In addition to the aforementioned fine-tuning, GPT-NeoXT-Chat-Base-20B-v0.16 has also undergone further fine-tuning via a small amount of feedback data. 
This allows the model to better adapt to human preferences in the conversations.

## Model Details
- **Developed by**: Together Computer.
- **Model type**: Language Model
- **Language(s)**: English
- **License**: Apache 2.0
- **Model Description**: A 20B parameter open source chat model, fine-tuned from EleutherAI’s NeoX with over 40M instructions on 100% carbon negative compute
- **Resources for more information**: [GitHub Repository](https://github.com/togethercomputer/OpenChaT).

# Quick Start

## GPU Inference

This requires a GPU with 48GB memory.
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/GPT-NeoXT-Chat-Base-20B")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/GPT-NeoXT-Chat-Base-20B", torch_dtype=torch.float16)
model = model.to('cuda:0')
# infer
inputs = tokenizer("<human>: Hello!\n<bot>:", return_tensors='pt').to(model.device)
outputs = model.generate(**inputs, max_new_tokens=10, do_sample=True, temperature=0.8)
output_str = tokenizer.decode(outputs[0])
print(output_str)
```

## GPU Inference in Int8

This requires a GPU with 24GB memory.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/GPT-NeoXT-Chat-Base-20B")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/GPT-NeoXT-Chat-Base-20B", device_map="auto", load_in_8bit=True)
# infer
inputs = tokenizer("<human>: Hello!\n<bot>:", return_tensors='pt').to(model.device)
outputs = model.generate(**inputs, max_new_tokens=10, do_sample=True, temperature=0.8)
output_str = tokenizer.decode(outputs[0])
print(output_str)
```

## CPU Inference

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/GPT-NeoXT-Chat-Base-20B")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/GPT-NeoXT-Chat-Base-20B", torch_dtype=torch.bfloat16)
# infer
inputs = tokenizer("<human>: Hello!\n<bot>:", return_tensors='pt').to(model.device)
outputs = model.generate(**inputs, max_new_tokens=10, do_sample=True, temperature=0.8)
output_str = tokenizer.decode(outputs[0])
print(output_str)
```


## Strengths of the model

There are several tasks that OpenChatKit excels at out of the box. This includes: 

- Example 1: Summarization and question answering within context.
    
    ```markdown
    **Summarize a long document into a single sentence and conduct question answering related to the document, with multiple rounds**
    
    <human>: Last year, the travel industry saw a big rebound in demand — and that demand is showing no signs of slowing down this spring break travel season. Planes and hotels will be full, travelers will likely face long queues, cancellations, massive crowds and plenty of other travel nightmares. But perhaps the most frustrating thing you’ll have to prepare for this spring break is if your luggage goes missing. You’ve got to somehow track down your belongings that were in the airline’s care and then wait to be reunited — all while trying to enjoy the start of your long-awaited vacation. As far as travel nightmares go, lost luggage is up there as one of the worst.
    
    To be honest up front, I am great at strategically losing things — or rather, losing stuff with style. (I hope you appreciate the “Toy Story” reference.) So when a product comes along that’s a perfect way to keep track of my belongings — especially when traveling — I’m adding it to my travel bag.
    
    I’ve been a big fan of Apple’s $29 item tracker, dubbed AirTag. The long-rumored AirTag product finally launched in 2021, and while it’s not the first item tracker to exist, it has two key features that set it apart from the rest to make it the ultimate travel companion: access to the Find My network and Precision Finding technology.
    
    The Federal Aviation Administration has even ruled that having an AirTag in your luggage is permitted and, in fact, not a safety hazard. The devices only contain 0.1 grams of lithium, which falls below the FAA’s limit.
    
    “Luggage tracking devices powered by lithium metal cells that have 0.3 grams or less of lithium can be used on checked baggage,” the FAA said in a statement. “Apple AirTags meet this threshold; other luggage tracking devices may not.”
    
    But, you may be wondering what makes them so special and why you should carry one in your checked luggage this spring break? Let’s explain why.
    
    Summarize the above into a single paragraph.
    
    <bot>: If you're traveling this spring break, you might want to consider investing in an item tracker to help you find your lost luggage. Apple's AirTag is the best option, according to a new report.
    
    <human>: But isn't it unsafe to put AirTag in a luggage?
    
    <bot>: The Federal Aviation Administration has ruled that having an AirTag in your luggage is permitted and, in fact, not a safety hazard.
    
    <human>: Ah, why is that?
    
    <bot>: The devices only contain 0.1 grams of lithium, which falls below the FAA’s limit.
    ```
    
- Example 2: Extraction.
    
    ```markdown
    **Extract structured information from unstructured documents, as illustrated in the following example.**
    
    <human>: Generate a table summarizing the options outlined in this email. 
    
    Team, we have to make a decision on the product plan for Goocrux v2. 
    
    The first option will take us 3 weeks of development, and will achieve performance of 80ms, but means that the UI has to change. 
    
    The second option will take us 4 weeks of development, and will achieve performance of 60ms, without any UI change. 
    
    The third option will take the longest -- 6 weeks of development, will achieve performance of 30ms, without any UI change. 
    
    A markdown table with four columns: (1) Option ID, (2) Development time, (3) Performance, (4) UI Change:
    
    <bot>: #.
    | ID | Option ID | Development time | Performance | UI Change |
    | --------- | --------- | --------- | --------- | --------- |
    | 1 | 1 | 3 weeks | 80ms | Yes |
    | 2 | 2 | 4 weeks | 60ms | No |
    | 3 | 3 | 6 weeks | 30ms | No |
    ```
    
- Example 3: Classification.

   ```markdown
   **Classifying a sentence or paragraph into different categories.**
   
   <human>: Classify the sentiment of the following sentence into Positive, Neutral, or Negative: Super excited about teaching Stanford’s first course on Large Language Models! Check the syllabus out here
   <bot>: Positive
   
   <human>: Classify the sentiment of the following sentence into Positive, Neutral, or Negative: How about the following sentence: It is raining outside and I feel so blue
   <bot>: Negative
   ```

In addition, the model does well on few-shot prompts. For both classification and extraction, the model performs even better with few shots, as in most HELM tasks. [Contact us](https://www.together.xyz/contact) if you’re interested in trying few-shot prompts with the model. 

## Weaknesses of the model

That said, there are several areas where we have more work to do, and we need your help! Some of these include: 

- Knowledge-based closed question and answering: The chatbot may hallucinate and give incorrect results. Be sure to fact check, and if possible provide feedback with the corrected information.
- Coding tasks: The chatbot was not trained on a large enough corpus of source code to excel at writing code. We welcome contributions of additional datasets to improve this!
- Repetition: Sometimes the chatbot will repeat its response. We’re working to improve this, but in the meantime you can click the refresh button to start a new conversation.
- Context switching: If you change the topic in the middle of a conversation the chatbot often cannot make the switch automatically and will continue to give answers related to the prior topic.
- Creative writing and longer answers: The chatbot does not generate long, creative text such as an essay or story.

We are excited to work with you to address these weaknesses by getting your feedback, bolstering data sets, and improving accuracy.

# Uses

## Direct Use 

The model is intended for research purposes. Possible research areas and tasks include

- Safe deployment of models which have the potential to generate harmful content.
- Probing and understanding the limitations and biases of dialogue models or language models.
- Generation of artworks and use in design and other artistic processes.
- Applications in educational or creative tools.
- Research on dialogue models or language models.

Excluded uses are described below.

### Misuse, Malicious Use, and Out-of-Scope Use

The OpenChatKit community provides GPT-NeoXT-Chat-Base-20B-v0.16 as an open source tool for building chatbots. 
The community is not responsible for any misuse, malicious use, or out-of-scope use of the model. 
It is the responsibility of the end user to ensure that the model is used in a responsible and ethical manner.

#### Out-of-Scope Use

GPT-NeoXT-Chat-Base-20B-v0.16 is designed for use in chatbot applications and may not perform well for other use cases outside of its intended scope. 
For example, it may not be suitable for use in safety-critical applications or for making decisions that have a significant impact on individuals or society. 
It is important to consider the limitations of the model and to only use it for its intended purpose.

#### Misuse and Malicious Use

GPT-NeoXT-Chat-Base-20B-v0.16 is designed for use in chatbot applications and should not be used for any other purpose.
Misuse of the model, such as using it to engage in illegal or unethical activities, is strictly prohibited and goes against the principles of the OpenChatKit community project.

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

GPT-NeoXT-Chat-Base-20B-v0.16, like other language model-based chatbots, has limitations that should be taken into consideration. 
For example, the model may not always provide accurate or relevant answers, particularly for questions that are complex, ambiguous, or outside of its training data. 
We therefore welcome contributions from individuals and organizations, and encourage collaboration towards creating a more robust and inclusive chatbot.

## Training

**Training Data**

Please refer to [togethercomputer/OpenDataHub](https://github.com/togethercomputer/OpenDataHub)

**Training Procedure**

- **Hardware:** 2 x 8 x A100 GPUs
- **Optimizer:** [8bit-AdamW](https://github.com/TimDettmers/bitsandbytes)
- **Gradient Accumulations**: 2
- **Batch:** 2 x 2 x 64 x 2048 = 524288 tokens
- **Learning rate:** warmup to 1e-6 for 100 steps and then kept constant

## Community

Join us on [Together Discord](https://discord.gg/6ZVDU8tTD4)
