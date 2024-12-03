---
language: en
license: apache-2.0
base_model: google/flan-t5-base
pipline_tag: text-classficiation
---

<img referrerpolicy="no-referrer-when-downgrade" src="https://static.scarf.sh/a.png?x-pxid=5f53f560-5ba6-4e73-917b-c7049e9aea2c" />

<img src="https://huggingface.co/vectara/hallucination_evaluation_model/resolve/main/candle.png" width="50" height="50" style="display: inline;">  In Loving memory of Simon Mark Hughes...

**Highlights**:
* HHEM-2.1-Open shows a significant improvement over HHEM-1.0.
* HHEM-2.1-Open outperforms GPT-3.5-Turbo and even GPT-4.
* HHEM-2.1-Open can be run on consumer-grade hardware, occupying less than 600MB RAM space at 32-bit precision and elapsing around 1.5 seconds for a 2k-token input on a modern x86 CPU. 

> HHEM-2.1-Open introduces breaking changes to the usage. Please update your code according to the [new usage](#using-hhem-21-open) below. We are working making it compatible with HuggingFace's Inference Endpoint. We apologize for the inconvenience.

HHEM-2.1-Open is a major upgrade to [HHEM-1.0-Open](https://huggingface.co/vectara/hallucination_evaluation_model/tree/hhem-1.0-open) created by [Vectara](https://vectara.com) in November 2023. The HHEM model series are designed for detecting hallucinations in LLMs. They are particularly useful in the context of building retrieval-augmented-generation (RAG) applications where a set of facts is summarized by an LLM, and HHEM can be used to measure the extent to which this summary is factually consistent with the facts.

If you are interested to learn more about RAG or experiment with Vectara, you can [sign up](https://console.vectara.com/signup/?utm_source=huggingface&utm_medium=space&utm_term=hhem-model&utm_content=console&utm_campaign=) for a free Vectara account.

[**Try out HHEM-2.1-Open from your browser without coding** ](http://13.57.203.109:3000/)

## Hallucination Detection 101
By "hallucinated" or "factually inconsistent", we mean that a text (hypothesis, to be judged) is not supported by another text (evidence/premise, given). You **always need two** pieces of text to determine whether a text is hallucinated or not. When applied to RAG (retrieval augmented generation), the LLM is provided with several pieces of text (often called facts or context) retrieved from some dataset, and a hallucination would indicate that the summary (hypothesis) is not supported by those facts (evidence). 

A common type of hallucination in RAG is **factual but hallucinated**. 
For example, given the premise _"The capital of France is Berlin"_, the hypothesis _"The capital of France is Paris"_ is hallucinated -- although it is true in the world knowledge. This happens when LLMs do not generate content based on the textual data provided to them as part of the RAG retrieval process, but rather generate content based on their pre-trained knowledge.

Additionally, hallucination detection is "asymmetric" or is not commutative. For example, the hypothesis _"I visited Iowa"_ is considered hallucinated given the premise _"I visited the United States"_, but the reverse is consistent.

## Using HHEM-2.1-Open

> HHEM-2.1 has some breaking change from HHEM-1.0. Your code that works with HHEM-1 (November 2023) will not work anymore. While we are working on backward compatibility, please follow the new usage instructions below.

Here we provide several ways to use HHEM-2.1-Open in the `transformers` library.

> You may run into a warning message that "Token indices sequence length is longer than the specified maximum sequence length". Please ignore it which is inherited from the foundation, T5-base. 

### Using with `AutoModel` 

This is the most end-to-end and out-of-the-box way to use HHEM-2.1-Open. It takes a list of pairs of (premise, hypothesis) as the input and returns a score between 0 and 1 for each parir where 0 means that the hypothesis is not evidenced at all by the premise and 1 means the hypothesis is fully supported by the premise.


```python
from transformers import AutoModelForSequenceClassification

pairs = [ # Test data, List[Tuple[str, str]]
    ("The capital of France is Berlin.", "The capital of France is Paris."), # factual but hallucinated
    ('I am in California', 'I am in United States.'), # Consistent
    ('I am in United States', 'I am in California.'), # Hallucinated
    ("A person on a horse jumps over a broken down airplane.", "A person is outdoors, on a horse."),
    ("A boy is jumping on skateboard in the middle of a red bridge.", "The boy skates down the sidewalk on a red bridge"),
    ("A man with blond-hair, and a brown shirt drinking out of a public water fountain.", "A blond man wearing a brown shirt is reading a book."),
    ("Mark Wahlberg was a fan of Manny.", "Manny was a fan of Mark Wahlberg.")
]

# Step 1: Load the model
model = AutoModelForSequenceClassification.from_pretrained(
    'vectara/hallucination_evaluation_model', trust_remote_code=True)

# Step 2: Use the model to predict
model.predict(pairs) # note the predict() method. Do not do model(pairs). 
# tensor([0.0111, 0.6474, 0.1290, 0.8969, 0.1846, 0.0050, 0.0543])
```

### Using with `pipeline`

In the popular  `pipeline` class of the `transformers` library, you have to manually prepare the data using the prompt template in which we trained the model. HHEM-2.1-Open has two output neurons, corresponding to the labels `hallucinated` and `consistent` respectively. In the example below, we will ask `pipeline` to return the scores for both labels (by setting `top_k=None`, formerly `return_all_scores=True`) and then extract the score for the `consistent` label. 

```python
from transformers import pipeline, AutoTokenizer

pairs = [ # Test data, List[Tuple[str, str]]
    ("The capital of France is Berlin.", "The capital of France is Paris."),
    ('I am in California', 'I am in United States.'),
    ('I am in United States', 'I am in California.'),
    ("A person on a horse jumps over a broken down airplane.", "A person is outdoors, on a horse."),
    ("A boy is jumping on skateboard in the middle of a red bridge.", "The boy skates down the sidewalk on a red bridge"),
    ("A man with blond-hair, and a brown shirt drinking out of a public water fountain.", "A blond man wearing a brown shirt is reading a book."),
    ("Mark Wahlberg was a fan of Manny.", "Manny was a fan of Mark Wahlberg.")
]

# Prompt the pairs
prompt = "<pad> Determine if the hypothesis is true given the premise?\n\nPremise: {text1}\n\nHypothesis: {text2}"
input_pairs = [prompt.format(text1=pair[0], text2=pair[1]) for pair in pairs]

# Use text-classification pipeline to predict
classifier = pipeline(
            "text-classification",
            model='vectara/hallucination_evaluation_model',
            tokenizer=AutoTokenizer.from_pretrained('google/flan-t5-base'),
            trust_remote_code=True
        )
full_scores = classifier(input_pairs, top_k=None) # List[List[Dict[str, float]]]

# Optional: Extract the scores for the 'consistent' label
simple_scores = [score_dict['score'] for score_for_both_labels in full_scores for score_dict in score_for_both_labels if score_dict['label'] == 'consistent']

print(simple_scores)
# Expected output: [0.011061512865126133, 0.6473632454872131, 0.1290171593427658, 0.8969419002532959, 0.18462494015693665, 0.005031010136008263, 0.05432349815964699]
```

Of course, with `pipeline`, you can also get the most likely label, or the label with the highest score, by setting `top_k=1`. 


## HHEM-2.1-Open vs. HHEM-1.0

The major difference between HHEM-2.1-Open and the original HHEM-1.0 is that HHEM-2.1-Open has an unlimited context length, while HHEM-1.0 is capped at 512 tokens. The longer context length allows HHEM-2.1-Open to provide more accurate hallucination detection for RAG which often needs more than 512 tokens. 

The tables below compare the two models on the [AggreFact](https://arxiv.org/pdf/2205.12854) and [RAGTruth](https://arxiv.org/abs/2401.00396) benchmarks, as well as GPT-3.5-Turbo and GPT-4. In particular, on AggreFact, we focus on its SOTA subset (denoted as `AggreFact-SOTA`) which contains summaries generated by Google's T5, Meta's BART, and Google's Pegasus, which are the three latest models in the AggreFact benchmark. The results on RAGTruth's summarization (denoted as `RAGTruth-Summ`) and QA (denoted as `RAGTruth-QA`) subsets are reported separately. The GPT-3.5-Turbo and GPT-4 versions are 01-25 and 06-13 respectively. The zero-shot results of the two GPT models were obtained using the prompt template in [this paper](https://arxiv.org/pdf/2303.15621).

Table 1: Performance on AggreFact-SOTA
| model     |    Balanced Accuracy | F1     | Recall | Precision |
|:------------------------|---------:|-------:|-------:|----------:|
| HHEM-1.0                | 78.87%   | 90.47% | 70.81% | 67.27%    |
| HHEM-2.1-Open           | 76.55%   | 66.77% | 68.48% | 65.13%    |
| GPT-3.5-Turbo zero-shot | 72.19%   | 60.88% | 58.48% | 63.49%    |
| GPT-4 06-13 zero-shot   | 73.78%   | 63.87% | 53.03% | 80.28%    |

Table 2: Performance on RAGTruth-Summ
| model     |    Balanced Accuracy | F1         | Recall    | Precision |
|:----------------------|---------:|-----------:|----------:|----------:|
| HHEM-1.0              | 53.36% | 15.77%   | 9.31% | 51.35% |
| HHEM-2.1-Open         | 64.42% | 44.83% | 31.86% | 75.58% |
| GPT-3.5-Turbo zero-shot | 58.49%   | 29.72% | 18.14% | 82.22%    |
| GPT-4 06-13 zero-shot   | 62.62%   | 40.59% | 26.96% | 82.09%    |

Table 3: Performance on RAGTruth-QA
| model     |    Balanced Accuracy | F1         | Recall    | Precision |
|:----------------------|---------:|-----------:|----------:|----------:|
| HHEM-1.0              | 52.58% | 19.40%   | 16.25% | 24.07% |
| HHEM-2.1-Open         | 74.28% | 60.00% | 54.38% | 66.92% |
| GPT-3.5-Turbo zero-shot | 56.16%   | 25.00% | 18.13% | 40.28%    |
| GPT-4 06-13 zero-shot   | 74.11%   | 57.78% | 56.88% | 58.71%    |

The tables above show that HHEM-2.1-Open has a significant improvement over HHEM-1.0 in the RAGTruth-Summ and RAGTruth-QA benchmarks, while it has a slight decrease in the AggreFact-SOTA benchmark. However, when interpreting these results, please note that AggreFact-SOTA is evaluated on relatively older types of LLMs:
- LLMs in AggreFact-SOTA: T5, BART, and Pegasus;
- LLMs in RAGTruth: GPT-4-0613, GPT-3.5-turbo-0613, Llama-2-7B/13B/70B-chat, and Mistral-7B-instruct. 

## HHEM-2.1-Open vs. GPT-3.5-Turbo and GPT-4

From the tables above we can also conclude that HHEM-2.1-Open outperforms both GPT-3.5-Turbo and GPT-4 in all three benchmarks. The quantitative advantage of HHEM-2.1-Open over GPT-3.5-Turbo and GPT-4 is summarized in Table 4 below.

Table 4: Percentage points of HHEM-2.1-Open's balanced accuracies over GPT-3.5-Turbo and GPT-4
|      |    AggreFact-SOTA | RAGTruth-Summ | RAGTruth-QA |
|:----------------------|---------:|-----------:|----------:|
| HHEM-2.1-Open **over** GPT-3.5-Turbo | 4.36% | 5.93% | 18.12% |
| HHEM-2.1-Open **over** GPT-4         | 2.64% | 1.80% | 0.17% | 

Another advantage of HHEM-2.1-Open is its efficiency. HHEM-2.1-Open can be run on consumer-grade hardware, occupying less than 600MB RAM space at 32-bit precision and elapsing around 1.5 second for a 2k-token input on a modern x86 CPU.

## HHEM-2.1: The more powerful, proprietary counterpart of HHEM-2.1-Open

As you may have already sensed from the name, HHEM-2.1-Open is the open source version of the premium HHEM-2.1. HHEM-2.1 (without the `-Open`) is offered exclusively via Vectara's RAG-as-a-service platform. The major difference between HHEM-2.1 and HHEM-2.1-Open is that HHEM-2.1 is cross-lingual on three languages: English, German, and French, while HHEM-2.1-Open is English-only. "Cross-lingual" means any combination of the three languages, e.g., documents in German, query in English, results in French.

### Why RAG in Vectara? 

Vectara provides a Trusted Generative AI platform. The platform allows organizations to rapidly create an AI assistant experience which is grounded in the data, documents, and knowledge that they have. Vectara's serverless RAG-as-a-Service also solves critical problems required for enterprise adoption, namely: reduces hallucination, provides explainability / provenance, enforces access control, allows for real-time updatability of the knowledge, and mitigates intellectual property / bias concerns from large language models.

To start benefiting from HHEM-2.1, you can [sign up](https://console.vectara.com/signup/?utm_source=huggingface&utm_medium=space&utm_term=hhem-model&utm_content=console&utm_campaign=) for a free Vectara account, and you will get the HHEM-2.1 score returned with every query automatically.

Here are some additional resources:
1. Vectara [API documentation](https://docs.vectara.com/docs).
2. Quick start using Forrest's [`vektara` package](https://vektara.readthedocs.io/en/latest/crash_course.html).
3. Learn more about Vectara's [Boomerang embedding model](https://vectara.com/blog/introducing-boomerang-vectaras-new-and-improved-retrieval-model/), [Slingshot reranker](https://vectara.com/blog/deep-dive-into-vectara-multilingual-reranker-v1-state-of-the-art-reranker-across-100-languages/), and [Mockingbird LLM](https://vectara.com/blog/mockingbird-a-rag-and-structured-output-focused-llm/)

## LLM Hallucination Leaderboard
If you want to stay up to date with results of the latest tests using this model to evaluate the top LLM models, we have a [public leaderboard](https://huggingface.co/spaces/vectara/leaderboard) that is periodically updated, and results are also available on the [GitHub repository](https://github.com/vectara/hallucination-leaderboard).

# Cite this model 

```bibtex
@misc {hhem-2.1-open,
	author       = {Forrest Bao and Miaoran Li and Rogger Luo and Ofer Mendelevitch},
	title        = {{HHEM-2.1-Open}},
	year         = 2024,
	url          = { https://huggingface.co/vectara/hallucination_evaluation_model },
	doi          = { 10.57967/hf/3240 },
	publisher    = { Hugging Face }
}
```