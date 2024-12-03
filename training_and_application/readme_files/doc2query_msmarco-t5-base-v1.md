---
language: en
datasets:
- sentence-transformers/embedding-training-data
widget:
- text: "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."

license: apache-2.0
---

# doc2query/msmarco-t5-base-v1

This is a [doc2query](https://arxiv.org/abs/1904.08375) model based on T5 (also known as [docT5query](https://cs.uwaterloo.ca/~jimmylin/publications/Nogueira_Lin_2019_docTTTTTquery-v2.pdf)).

It can be used for:
- **Document expansion**: You generate for your paragraphs 20-40 queries and index the paragraphs and the generates queries in a standard BM25 index like Elasticsearch, OpenSearch, or Lucene. The generated queries help to close the lexical gap of lexical search, as the generate queries contain synonyms. Further, it re-weights words giving important words a higher weight even if they appear seldomn in a paragraph. In our [BEIR](https://arxiv.org/abs/2104.08663) paper we showed that BM25+docT5query is a powerful search engine. In the [BEIR repository](https://github.com/UKPLab/beir) we have an example how to use docT5query with Pyserini.
- **Domain Specific Training Data Generation**: It can be used to generate training data to learn an embedding model. On [SBERT.net](https://www.sbert.net/examples/unsupervised_learning/query_generation/README.html) we have an example how to use the model to generate (query, text) pairs for a given collection of unlabeled texts. These pairs can then be used to train powerful dense embedding models.

## Usage
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

model_name = 'doc2query/msmarco-t5-base-v1'
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

text = "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."


input_ids = tokenizer.encode(text, max_length=320, truncation=True, return_tensors='pt')
outputs = model.generate(
    input_ids=input_ids,
    max_length=64,
    do_sample=True,
    top_p=0.95,
    num_return_sequences=5)

print("Text:")
print(text)

print("\nGenerated Queries:")
for i in range(len(outputs)):
    query = tokenizer.decode(outputs[i], skip_special_tokens=True)
    print(f'{i + 1}: {query}')
```

**Note:** `model.generate()` is non-deterministic. It produces different queries each time you run it.

## Training
This model fine-tuned [google/t5-v1_1-base](https://huggingface.co/google/t5-v1_1-base) for 31k training steps (about 4 epochs on the 500k training pairs from MS MARCO). For the  training script, see the `train_script.py` in this repository.

The input-text was truncated to 320 word pieces. Output text was generated up to 64 word pieces. 

This model was trained on a (query, passage) from the [MS MARCO Passage-Ranking dataset](https://github.com/microsoft/MSMARCO-Passage-Ranking).



