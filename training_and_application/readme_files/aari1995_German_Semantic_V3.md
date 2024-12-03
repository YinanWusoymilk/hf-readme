---
language:
- de
library_name: sentence-transformers
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- loss:MatryoshkaLoss
base_model: aari1995/gbert-large-2
metrics:
- spearman_cosine
widget:
- source_sentence: Bundeskanzler.
  sentences:
  - Angela Merkel.
  - Olaf Scholz.
  - Tino Chrupalla.
- source_sentence: Corona.
  sentences:
  - Virus.
  - Krone.
  - Bier.
- source_sentence: Ein Mann übt Boxen
  sentences:
  - Ein Affe praktiziert Kampfsportarten.
  - Eine Person faltet ein Blatt Papier.
  - Eine Frau geht mit ihrem Hund spazieren.
- source_sentence: Zwei Frauen laufen.
  sentences:
  - Frauen laufen.
  - Die Frau prüft die Augen des Mannes.
  - Ein Mann ist auf einem Dach
- source_sentence: Der Mann heißt Joel.
  sentences:
  - Eine Frau namens Jolie
  - Ein Mann mit einem englischen Namen.
  - Freunde gehen feiern.
pipeline_tag: sentence-similarity
license: apache-2.0
---

# 🇩🇪 German Semantic V3 🇩🇪
### (and [**German_Semantic_V3b**](https://huggingface.co/aari1995/German_Semantic_V3b))

The successors of [German_Semantic_STS_V2](https://huggingface.co/aari1995/German_Semantic_STS_V2) are here and come with loads of cool new features! While V3 is really knowledge-heavy, [German_Semantic_V3b](https://huggingface.co/aari1995/German_Semantic_V3b) is more focused on performance. Feel free to provide feedback on the model and what you would like to see next.

**Note:** To run this model properly, see "Usage".

Use this model to create german semantic sentence embeddings.

# Major updates and USPs:

- **Flexibility:** Trained with flexible sequence-length and embedding truncation, flexibility is a core feature of the model. Yet, smaller dimensions bring a minor trade-off in quality. 
- **Sequence length:** Embed up to 8192 tokens (16 times more than V2 and other models)
- **Matryoshka Embeddings:** The model is trained for embedding sizes from 1024 down to 64, allowing you to store much smaller embeddings with little quality loss.
- **German only:** This model is German-only, it has rich cultural knowledge about Germany and German topics. This helps the model to learn more efficient thanks to its tokenizer, deal better with shorter queries and generally be more nuanced in many scenarios.
- **Updated knowledge and quality data:** The backbone of this model is gbert-large by deepset. With Stage-2 pretraining on 1 Billion tokens of German fineweb by occiglot, up-to-date knowledge is ensured.
- **Typo and Casing**: This model was trained to be robust against minor typos and casing, leading to slightly weaker benchmark performance and learning during training, but higher robustness of the embeddings.
- **Pooling Function:** Moving away from mean pooling towards using the CLS token. Generally seems to learn better after the stage-2 pretraining and allows for more flexibility.
- **License:** Apache 2.0

(If you are looking for even better performance on tasks, but with a German knowledge-cutoff around 2020, check out [German_Semantic_V3b](https://huggingface.co/aari1995/German_Semantic_V3))

# Usage:

This model has some build-in functionality that is rather hidden. To profit from it, use this code:

```python
from sentence_transformers import SentenceTransformer


matryoshka_dim = 1024 # How big your embeddings should be, choose from: 64, 128, 256, 512, 768, 1024
model = SentenceTransformer("aari1995/German_Semantic_V3", trust_remote_code=True, truncate_dim=matryoshka_dim)

# model.truncate_dim = 64 # truncation dimensions can also be changed after loading
# model.max_seq_length = 512 #optionally, set your maximum sequence length lower if your hardware is limited 

# Run inference
sentences = [
    'Eine Flagge weht.',
    'Die Flagge bewegte sich in der Luft.',
    'Zwei Personen beobachten das Wasser.',
]

# For FP16 embeddings (half space, no quality loss)
embeddings = model.encode(sentences, convert_to_tensor=True).half()

# For FP32 embeddings (takes more space)
# embeddings = model.encode(sentences)

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)

```


# FAQ

**Q: Is this Model better than V2?**

**A:** In terms of flexibility-definitely. In terms of data-yes as well, as it is more up-to-date. In terms of benchmark they differ, while V3 is better for longer texts, V2 works very well for shorter texts. Keeping in mind that many benchmarks also do not cover cultural knowledge too well.
If you are fine with the model not knowing about developments after early 2020, I'd suggest you use [German_Semantic_V3b](https://huggingface.co/aari1995/German_Semantic_V3).

**Q: What is the difference between V3 and V3b?**

**A:** V3 is slightly worse on benchmarks, while V3b has a knowledge cutoff by 2020, so it really depends on your use-case which model to use.

If you want peak performance and do not worry too much about recent developments, take this [V3b](https://huggingface.co/aari1995/German_Semantic_V3b).

If you are fine with sacrificing a few points on benchmarks and want the model to know what happened from 2020 on (elections, covid, other cultural events etc.), I'd suggest you use this one.

Another noticable difference is that V3 has a broader cosine_similarity spectrum, reaching from -1 to 1 (but mostly, the least is over -0.2). On the other side, V3b is more aligned with V2 and the similarity spectrum is around 0 to 1. Also, V3 uses cls_pooling while V3b uses mean_pooling.


**Q: How does the model perform vs. multilingual models?**

**A:** There are really great multilingual models that will be very useful for many use-cases. This model shines with its cultural knowledge and knowledge about German people and behaviour. 

**Q: What is the trade-off when reducing the embedding size?**

**A:** Broadly speaking, when going from 1024 to 512 dimensions, there is very little trade-off (1 percent). When going down to 64 dimensions, you may face a decrease of up to 3 percent.

# Evaluation

Storage comparison:
![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3801ab7e583543386217ac/Aa5WzHanj-DXc86AKxpEz.png)

Benchmarks: soon.

# Up next:
German_Semantic_V3_Instruct: Guiding your embeddings towards self-selected aspects. - planned: 2024.

# Thank You and Credits

- To [jinaAI](https://huggingface.co/jinaai) for their BERT implementation that is used, especially ALiBi
- To [deepset](https://huggingface.co/deepset) for the gbert-large, which is a really great model
- To [occiglot](https://huggingface.co/occiglot) and OSCAR for their data used to pre-train the model
- To [Tom](https://huggingface.co/tomaarsen), especially for sentence-transformers and feedback, [Björn and Jan from ellamind](https://ellamind.com/de/) for the consultation
- To [Meta](https://huggingface.co/facebook) for XNLI which is used in variations

Idea, Training and Implementation by Aaron Chibb.