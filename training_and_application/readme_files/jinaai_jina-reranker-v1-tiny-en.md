---
library_name: transformers
license: apache-2.0
language:
- en
tags:
- reranker
- cross-encoder
- transformers.js
pipeline_tag: text-classification
---

<br><br>

<p align="center">
<img src="https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/603763514de52ff951d89793/AFoybzd5lpBQXEBrQHuTt.png?w=200&h=200&f=face" alt="Finetuner logo: Finetuner helps you to create experiments in order to improve embeddings on search tasks. It accompanies you to deliver the last mile of performance-tuning for neural search applications." width="150px">
</p>

<p align="center">
<b>Trained by <a href="https://jina.ai/"><b>Jina AI</b></a>.</b>
</p>

# jina-reranker-v1-tiny-en

This model is designed for **blazing-fast** reranking while maintaining **competitive performance**. What's more, it leverages the power of our [JinaBERT](https://arxiv.org/abs/2310.19923) model as its foundation. `JinaBERT` itself is a unique variant of the BERT architecture that supports the symmetric bidirectional variant of [ALiBi](https://arxiv.org/abs/2108.12409). This allows `jina-reranker-v1-tiny-en` to process significantly longer sequences of text compared to other reranking models, up to an impressive **8,192** tokens.

To achieve the remarkable speed, the `jina-reranker-v1-tiny-en` employ a technique called knowledge distillation. Here, a complex, but slower, model (like our original [jina-reranker-v1-base-en](https://jina.ai/reranker/)) acts as a teacher, condensing its knowledge into a smaller, faster student model. This student retains most of the teacher's knowledge, allowing it to deliver similar accuracy in a fraction of the time.

Here's a breakdown of the reranker models we provide:

| Model Name                                                                           | Layers | Hidden Size | Parameters (Millions) |
| ------------------------------------------------------------------------------------ | ------ | ----------- | --------------------- |
| [jina-reranker-v1-base-en](https://jina.ai/reranker/)                                | 12     | 768         | 137.0                 |
| [jina-reranker-v1-turbo-en](https://huggingface.co/jinaai/jina-reranker-v1-turbo-en) | 6      | 384         | 37.8                  |
| [jina-reranker-v1-tiny-en](https://huggingface.co/jinaai/jina-reranker-v1-tiny-en)   | 4      | 384         | 33.0                  |

> Currently, the `jina-reranker-v1-base-en` model is not available on Hugging Face. You can access it via the [Jina AI Reranker API](https://jina.ai/reranker/).

As you can see, the `jina-reranker-v1-turbo-en` offers a balanced approach with **6 layers** and **37.8 million** parameters. This translates to fast search and reranking while preserving a high degree of accuracy. The `jina-reranker-v1-tiny-en` prioritizes speed even further, achieving the fastest inference speeds with its **4-layer**, **33.0 million** parameter architecture. This makes it ideal for scenarios where absolute top accuracy is less crucial.

# Usage

1. The easiest way to starting using `jina-reranker-v1-tiny-en` is to use Jina AI's [Reranker API](https://jina.ai/reranker/).

```bash
curl https://api.jina.ai/v1/rerank \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
  "model": "jina-reranker-v1-tiny-en",
  "query": "Organic skincare products for sensitive skin",
  "documents": [
    "Eco-friendly kitchenware for modern homes",
    "Biodegradable cleaning supplies for eco-conscious consumers",
    "Organic cotton baby clothes for sensitive skin",
    "Natural organic skincare range for sensitive skin",
    "Tech gadgets for smart homes: 2024 edition",
    "Sustainable gardening tools and compost solutions",
    "Sensitive skin-friendly facial cleansers and toners",
    "Organic food wraps and storage solutions",
    "All-natural pet food for dogs with allergies",
    "Yoga mats made from recycled materials"
  ],
  "top_n": 3
}'
```

2. Alternatively, you can use the latest version of the `sentence-transformers>=0.27.0` library. You can install it via pip:

```bash
pip install -U sentence-transformers
```

Then, you can use the following code to interact with the model:

```python
from sentence_transformers import CrossEncoder

# Load the model, here we use our tiny sized model
model = CrossEncoder("jinaai/jina-reranker-v1-tiny-en", trust_remote_code=True)

# Example query and documents
query = "Organic skincare products for sensitive skin"
documents = [
    "Eco-friendly kitchenware for modern homes",
    "Biodegradable cleaning supplies for eco-conscious consumers",
    "Organic cotton baby clothes for sensitive skin",
    "Natural organic skincare range for sensitive skin",
    "Tech gadgets for smart homes: 2024 edition",
    "Sustainable gardening tools and compost solutions",
    "Sensitive skin-friendly facial cleansers and toners",
    "Organic food wraps and storage solutions",
    "All-natural pet food for dogs with allergies",
    "Yoga mats made from recycled materials"
]

results = model.rank(query, documents, return_documents=True, top_k=3)
```

3. You can also use the `transformers` library to interact with the model programmatically.

```python
!pip install transformers
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    'jinaai/jina-reranker-v1-tiny-en', num_labels=1, trust_remote_code=True
)

# Example query and documents
query = "Organic skincare products for sensitive skin"
documents = [
    "Eco-friendly kitchenware for modern homes",
    "Biodegradable cleaning supplies for eco-conscious consumers",
    "Organic cotton baby clothes for sensitive skin",
    "Natural organic skincare range for sensitive skin",
    "Tech gadgets for smart homes: 2024 edition",
    "Sustainable gardening tools and compost solutions",
    "Sensitive skin-friendly facial cleansers and toners",
    "Organic food wraps and storage solutions",
    "All-natural pet food for dogs with allergies",
    "Yoga mats made from recycled materials"
]

# construct sentence pairs
sentence_pairs = [[query, doc] for doc in documents]

scores = model.compute_score(sentence_pairs)
```

4. You can also use the `transformers.js` library to run the model directly in JavaScript (in-browser, Node.js, Deno, etc.)!

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@xenova/transformers) using:
```bash
npm i @xenova/transformers
```

Then, you can use the following code to interact with the model:
```js
import { AutoTokenizer, AutoModelForSequenceClassification } from '@xenova/transformers';

const model_id = 'jinaai/jina-reranker-v1-tiny-en';
const model = await AutoModelForSequenceClassification.from_pretrained(model_id, { quantized: false });
const tokenizer = await AutoTokenizer.from_pretrained(model_id);

/**
 * Performs ranking with the CrossEncoder on the given query and documents. Returns a sorted list with the document indices and scores.
 * @param {string} query A single query
 * @param {string[]} documents A list of documents
 * @param {Object} options Options for ranking
 * @param {number} [options.top_k=undefined] Return the top-k documents. If undefined, all documents are returned.
 * @param {number} [options.return_documents=false] If true, also returns the documents. If false, only returns the indices and scores.
 */
async function rank(query, documents, {
    top_k = undefined,
    return_documents = false,
} = {}) {
    const inputs = tokenizer(
        new Array(documents.length).fill(query),
        { text_pair: documents, padding: true, truncation: true }
    )
    const { logits } = await model(inputs);
    return logits.sigmoid().tolist()
        .map(([score], i) => ({
            corpus_id: i,
            score,
            ...(return_documents ? { text: documents[i] } : {})
        })).sort((a, b) => b.score - a.score).slice(0, top_k);
}

// Example usage:
const query = "Organic skincare products for sensitive skin"
const documents = [
    "Eco-friendly kitchenware for modern homes",
    "Biodegradable cleaning supplies for eco-conscious consumers",
    "Organic cotton baby clothes for sensitive skin",
    "Natural organic skincare range for sensitive skin",
    "Tech gadgets for smart homes: 2024 edition",
    "Sustainable gardening tools and compost solutions",
    "Sensitive skin-friendly facial cleansers and toners",
    "Organic food wraps and storage solutions",
    "All-natural pet food for dogs with allergies",
    "Yoga mats made from recycled materials",
]

const results = await rank(query, documents, { return_documents: true, top_k: 3 });
console.log(results);
```


That's it! You can now use the `jina-reranker-v1-tiny-en` model in your projects.

# Evaluation

We evaluated Jina Reranker on 3 key benchmarks to ensure top-tier performance and search relevance.

| Model Name                                 | NDCG@10 (17 BEIR datasets) | NDCG@10 (5 LoCo datasets) | Hit Rate (LlamaIndex RAG) |
| ------------------------------------------ | -------------------------- | ------------------------- | ------------------------- |
| `jina-reranker-v1-base-en`                 | **52.45**                  | **87.31**                 | **85.53**                 |
| `jina-reranker-v1-turbo-en`                | **49.60**                  | **69.21**                 | **85.13**                 |
| `jina-reranker-v1-tiny-en` (you are here)  | **48.54**                  | **70.29**                 | **85.00**                 |
| `mxbai-rerank-base-v1`                     | 49.19                      | -                         | 82.50                     |
| `mxbai-rerank-xsmall-v1`                   | 48.80                      | -                         | 83.69                     |
| `ms-marco-MiniLM-L-6-v2`                   | 48.64                      | -                         | 82.63                     |
| `ms-marco-MiniLM-L-4-v2`                   | 47.81                      | -                         | 83.82                     |
| `bge-reranker-base`                        | 47.89                      | -                         | 83.03                     |

**Note:**

- `NDCG@10` is a measure of ranking quality, with higher scores indicating better search results. `Hit Rate` measures the percentage of relevant documents that appear in the top 10 search results.
- The results of LoCo datasets on other models are not available since they **do not support** long documents more than 512 tokens.

For more details, please refer to our [benchmarking sheets](https://docs.google.com/spreadsheets/d/1V8pZjENdBBqrKMzZzOWc2aL60wtnR0yrEBY3urfO5P4/edit?usp=sharing).

# Contact

Join our [Discord community](https://discord.jina.ai/) and chat with other community members about ideas.