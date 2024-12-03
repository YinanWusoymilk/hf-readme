---
license: llama2
language:
- en
---
# **Model Overview**

As the demand for large language models grows, a common limitation surfaces: their inability to directly search the internet. Although tech giants like Google (with Bard), Bing, and Perplexity are addressing this challenge, their proprietary methods have data logging issues.

**Introducing Open LLM Search** — A specialized adaptation of Together AI's `llama-2-7b-32k` model, purpose-built for extracting information from web pages. While the model only has a 7 billion parameters, its fine-tuned capabilities and expanded context limit enable it to excel in search tasks.

**License:** This model uses Meta's Llama 2 license.

# **Fine-Tuning Process**

The model's fine tuning involved a combination of GPT-4 and GPT-4-32k to generate synthetic data. Here is the training workflow used:
1. Use GPT-4 to generate a multitude of queries.
2. For each query, identify the top five website results from Google.
3. Extract content from these websites and use GPT-4-32k for their summarization.
4. Record the text and summarizes from GPT-4-32k for fine-tuning.
5. Feed the summaries from all five sources with GPT-4 to craft a cohesive response.
6. Document both the input and output from GPT-4 for fine-tuning.

Fine tuning was done with an `<instructions>:`, `<user>:`, and `<assistant>:` format.

# **Getting Started**

- Experience it firsthand! Check out the live demo [here](https://huggingface.co/spaces/masonbarnes/open-llm-search).
- For DIY enthusiasts, explore or self-deploy this solution using our [GitHub repository](https://github.com/MasonBarnes/open-llm-search).