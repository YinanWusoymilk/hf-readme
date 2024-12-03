---
pipeline_tag: text-generation
language:
- multilingual
inference: false
license: cc-by-nc-4.0
library_name: transformers
---

<br><br>

<p align="center">
<img src="https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/603763514de52ff951d89793/AFoybzd5lpBQXEBrQHuTt.png?w=200&h=200&f=face" alt="Finetuner logo: Finetuner helps you to create experiments in order to improve embeddings on search tasks. It accompanies you to deliver the last mile of performance-tuning for neural search applications." width="150px">
</p>

<p align="center">
<b>Trained by <a href="https://jina.ai/"><b>Jina AI</b></a>.</b>
</p>

[Blog](https://jina.ai/news/reader-lm-small-language-models-for-cleaning-and-converting-html-to-markdown) | [Colab](https://colab.research.google.com/drive/1wXWyj5hOxEHY6WeHbOwEzYAC0WB1I5uA)

# Intro

Jina Reader-LM is a series of models that convert HTML content to Markdown content, which is useful for content conversion tasks. The model is trained on a curated collection of HTML content and its corresponding Markdown content.

# Models

| Name            |  Context Length   | Download                                                                                                                                          |
|-----------------|-------------------|-----------------------------------------------------------------------|
| reader-lm-0.5b  |  256K             | [🤗 Hugging Face](https://huggingface.co/jinaai/reader-lm-0.5b)       |
| reader-lm-1.5b  |  256K             | [🤗 Hugging Face](https://huggingface.co/jinaai/reader-lm-1.5b)       |
|                 |

# Get Started

## On Google Colab
The easiest way to experience reader-lm is by running [our Colab notebook](https://colab.research.google.com/drive/1wXWyj5hOxEHY6WeHbOwEzYAC0WB1I5uA), 
where we demonstrate how to use reader-lm-1.5b to convert the HackerNews website into markdown. The notebook is optimized to run smoothly on Google Colab’s free T4 GPU tier. You can also load reader-lm-0.5b or change the URL to any website and explore the output. Note that the input (i.e., the prompt) to the model is the raw HTML—no prefix instruction is required.

## Local

To use this model, you need to install `transformers`:

```bash
pip install transformers<=4.43.4
```

Then, you can use the model as follows:

```python
# pip install transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
checkpoint = "jinaai/reader-lm-1.5b"

device = "cuda" # for GPU usage or "cpu" for CPU usage
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

# example html content
html_content = "<html><body><h1>Hello, world!</h1></body></html>"

messages = [{"role": "user", "content": html_content}]
input_text=tokenizer.apply_chat_template(messages, tokenize=False)

print(input_text)

inputs = tokenizer.encode(input_text, return_tensors="pt").to(device)
outputs = model.generate(inputs, max_new_tokens=1024, temperature=0, do_sample=False, repetition_penalty=1.08)

print(tokenizer.decode(outputs[0]))
```

## AWS Sagemaker & Azure Marketplace
[AWS 0.5b](https://aws.amazon.com/marketplace/pp/prodview-nli7b6dueo424?sr=0-1&ref_=beagle&applicationId=AWSMPContessa)
[AWS 1.5b](https://aws.amazon.com/marketplace/pp/prodview-ms27ixcwq3wjk?sr=0-2&ref_=beagle&applicationId=AWSMPContessa)
[Azure 0.5b](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/jinaai.reader-lm-500m)
[Azure 1.5b](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/jinaai.reader-lm-1500m)

