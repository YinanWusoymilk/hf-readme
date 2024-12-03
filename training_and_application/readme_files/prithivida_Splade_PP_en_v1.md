---
license: apache-2.0
language:
- en
datasets:
- ms_marco
tags:
- splade++
- document-expansion
- sparse representation
- bag-of-words
- passage-retrieval
- knowledge-distillation
- document encoder
pretty_name:  Independent Implementation of SPLADE++ Model with some efficiency tweaks for Industry setting.
library_name: transformers
pipeline_tag: fill-mask
---

# Independent Implementation of SPLADE++ Model (`a.k.a splade-cocondenser* and family`) for the Industry setting.
--------------

This work stands on the shoulders of 2 robust researches: [Naver's From Distillation to Hard Negative Sampling: Making Sparse Neural IR Models More Effective paper](https://arxiv.org/pdf/2205.04733.pdf) and [Google's SparseEmbed](https://storage.googleapis.com/gweb-research2023-media/pubtools/pdf/79f16d3b3b948706d191a7fe6dd02abe516f5564.pdf). 
Props to both the teams for such a robust work.

## 1. What are Sparse Representations and Why learn one?

**Beginner ?** expand this. **Expert in Sparse & Dense representations ?** feel free skip to next section 2,

<details>

**1. Lexical search:**

Lexical search with BOW based sparse vectors are strong baselines, but they famously suffer from vocabulary mismatch problem, as they can only do exact term matching. Here are the pros and cons: 


- ✅ Efficient and Cheap.
- ✅ No need to fine-tune models.
- ✅️ Interpretable.
- ✅️ Exact Term Matches.
- ❌ Vocabulary mismatch (Need to remember exact terms)


**2. Semantic Search:**

Learned Neural / Dense retrievers (DPR, Sentence transformers*, BGE* models) with approximate nearest neighbors search has shown impressive results. Here are the pros and cons: 

- ✅ Search how humans innately think.
- ✅ When finetuned beats sparse by long way.
- ✅ Easily works with Multiple modals.
- ❌ Suffers token amnesia (misses term matching), 
- ❌ Resource intensive (both index & retreival), 
- ❌ Famously hard to interpret.
- ❌ Needs fine-tuning for OOD data.

**3. The big idea:**

Getting pros of both searches made sense and that gave rise to interest in learning sparse representations for queries and documents with some interpretability. The sparse representations also double as implicit or explicit (latent, contextualized) expansion mechanisms for both query and documents. If you are new to query expansion learn more here from the master himself Daniel Tunkelang.

**4. What a Sparse model learns ?**

The model learns to project it's learned dense representations over a MLM head to give a vocabulary distribution. Which is just to say the model can do automatic token expansion. (Image courtesy of pinecone)

<img src="./expansion.png" width=600 height=550/>
  
</details>

## **[Skip to "HOW TO USE with POPULAR VECTORDBs and more"](#htu) or continue for more details.**


## 2. Motivation:
SPLADE models are a fine balance between retrieval effectiveness (quality) and retrieval efficiency (latency and $), with that in mind we did **very minor retrieval efficiency tweaks** to make it more suitable for a industry setting. 
*(Pure MLE folks should not conflate efficiency to model inference efficiency. Our main focus is on retrieval efficiency. Hereinafter efficiency is a short hand for retrieval efficiency unless explicitly qualified otherwise. Not that inference efficiency is not important, we will address that subsequently.)* 

**TL;DR of Our attempt & results**
1. FLOPS tuning: Seperate **Seq lens and Severely restrictive FLOPs schedule and token budget** doc(128) & query(24) NOT 256 unlike Official SPLADE++. Inspired from **SparseEmbed** 
3. Init Weights: Vanilla **bert-base-uncased**. No corpus awarness unlike Official splade++ / ColBERT
4. Yet achieves competitive effectiveness of MRR@10 **37.22** in ID data (& OOD 48.7) and a retrieval latency of - **47.27ms**. (multi-threaded) all On **Consumer grade-GPUs** with **only 5 negatives per query**.
4. For Industry setting: Effectiveness on custom domains needs more than just **Trading FLOPS for tiny gains** and The Premise "SPLADE++ are not well suited to mono-cpu retrieval" does not hold.
5. Owing to query-time inference latency we still need 2 models one for query & doc, This is a Doc model and Query model will be **released soon.**

<img src="./ID.png" width=750 height=650/>

*Note: The paper refers to the best performing models as SPLADE++, hence for consistency we are reusing the same.*


<br/>

## 3. Why FLOPS is one of the key metrics for industry setting ?

<details>
  
  While ONLY a empirical analysis on large sample make sense here is a spot checking - a qualitatively example to give you an idea. Our models achieve par competitive effectiveness with **~10% and ~100%, lesser tokens comparable SPLADE++ models including SoTA**. 
(We will show Quantitative results in the next section.)

So, **by design "how to beat SoTA MRR?" was never our goal**, Instead "At what cost can we achieve an acceptable effectiveness i.e. MRR@10". Non-chalantly reducing lambda values (λQ,λD, see above table) will achieve a better MRR. 
But Lower lambda values = Higher FLOPS = More tokens = Poorer efficiency. This is NOT desirable for a Industry setting.


  
**Ours**
```python
number of actual dimensions:  113
SPLADE BOW rep:
 [('stress', 2.36), ('glass', 2.15), ('thermal', 2.06), ('pan', 1.83), ('glasses', 1.67), ('break', 1.47), ('crack', 1.47), ('heat', 1.45), ('warmth', 1.36), ('depression', 1.34), ('hotter', 1.23), ('hottest', 1.11), ('window', 1.11), ('hot', 1.1), ('area', 1.04), ('cause', 1.01), ('adjacent', 0.99), ('too', 0.94), ('created', 0.86), ('##pan', 0.84), ('phenomenon', 0.81), ('when', 0.78), ('temperature', 0.76), ('cracked', 0.75), ('factors', 0.74), ('windows', 0.72), ('create', 0.71), ('level', 0.7), ('formed', 0.61), ('stresses', 0.59), ('warm', 0.58), ('fracture', 0.57), ('adjoining', 0.56), ('areas', 0.56), ('nearby', 0.56), ('causes', 0.56), ('broken', 0.54), ('produced', 0.52), ('sash', 0.51), ('if', 0.51), ('breaks', 0.49), ('is', 0.49), ('effect', 0.45), ('heated', 0.44), ('process', 0.42), ('breaking', 0.42), ('one', 0.4), ('mirror', 0.39), ('factor', 0.38), ('shatter', 0.38), ('formation', 0.37), ('mathias', 0.37), ('damage', 0.36), ('cracking', 0.35), ('climate', 0.35), ('ceramic', 0.34), ('reaction', 0.34), ('steam', 0.33), ('reflection', 0.33), ('generated', 0.33), ('material', 0.32), ('burst', 0.31), ('fire', 0.31), ('neighboring', 0.3), ('explosion', 0.29), ('caused', 0.29), ('warmer', 0.29), ('because', 0.28), ('anxiety', 0.28), ('furnace', 0.28), ('tear', 0.27), ('induced', 0.27), ('fail', 0.26), ('are', 0.26), ('collapse', 0.26), ('##thermal', 0.26), ('and', 0.25), ('great', 0.25), ('get', 0.24), ('spark', 0.23), ('lens', 0.2), ('cooler', 0.19), ('determined', 0.19), ('leak', 0.19), ('disease', 0.19), ('emotion', 0.16), ('cork', 0.14), ('cooling', 0.14), ('heating', 0.13), ('governed', 0.13), ('optical', 0.12), ('surrounding', 0.12), ('warming', 0.12), ('convection', 0.11), ('regulated', 0.11), ('problem', 0.1), ('cool', 0.09), ('violence', 0.09), ('breaker', 0.09), ('image', 0.09), ('photo', 0.05), ('strike', 0.05), ('.', 0.04), ('shattering', 0.04), ('snap', 0.03), ('wilson', 0.03), ('weather', 0.02), ('eye', 0.02), ('produce', 0.01), ('crime', 0.01), ('humid', 0.0), ('impact', 0.0), ('earthquake', 0.0)]```
```

**naver/splade-cocondenser-ensembledistil** (SoTA, ~10% more tokens + FLOPS = 1.85)
```python
number of actual dimensions:  126
SPLADE BOW rep:
 [('stress', 2.25), ('glass', 2.23), ('thermal', 2.18), ('glasses', 1.65), ('pan', 1.62), ('heat', 1.56), ('stressed', 1.42), ('crack', 1.31), ('break', 1.12), ('cracked', 1.1), ('hot', 0.93), ('created', 0.9), ('factors', 0.81), ('broken', 0.73), ('caused', 0.71), ('too', 0.71), ('damage', 0.69), ('if', 0.68), ('hotter', 0.65), ('governed', 0.61), ('heating', 0.59), ('temperature', 0.59), ('adjacent', 0.59), ('cause', 0.58), ('effect', 0.57), ('fracture', 0.56), ('bradford', 0.55), ('strain', 0.53), ('hammer', 0.51), ('brian', 0.48), ('error', 0.47), ('windows', 0.45), ('will', 0.45), ('reaction', 0.42), ('create', 0.42), ('windshield', 0.41), ('heated', 0.41), ('factor', 0.4), ('cracking', 0.39), ('failure', 0.38), ('mechanical', 0.38), ('when', 0.38), ('formed', 0.38), ('bolt', 0.38), ('mechanism', 0.37), ('warm', 0.37), ('areas', 0.36), ('area', 0.36), ('energy', 0.34), ('disorder', 0.33), ('barry', 0.33), ('shock', 0.32), ('determined', 0.32), ('gage', 0.32), ('sash', 0.31), ('theory', 0.31), ('level', 0.31), ('resistant', 0.31), ('brake', 0.3), ('window', 0.3), ('crash', 0.3), ('hazard', 0.29), ('##ink', 0.27), ('ceramic', 0.27), ('storm', 0.25), ('problem', 0.25), ('issue', 0.24), ('impact', 0.24), ('fridge', 0.24), ('injury', 0.23), ('ross', 0.22), ('causes', 0.22), ('affect', 0.21), ('pressure', 0.21), ('fatigue', 0.21), ('leak', 0.21), ('eye', 0.2), ('frank', 0.2), ('cool', 0.2), ('might', 0.19), ('gravity', 0.18), ('ray', 0.18), ('static', 0.18), ('collapse', 0.18), ('physics', 0.18), ('wave', 0.18), ('reflection', 0.17), ('parker', 0.17), ('strike', 0.17), ('hottest', 0.17), ('burst', 0.16), ('chance', 0.16), ('burn', 0.14), ('rubbing', 0.14), ('interference', 0.14), ('bailey', 0.13), ('vibration', 0.12), ('gilbert', 0.12), ('produced', 0.12), ('rock', 0.12), ('warmer', 0.11), ('get', 0.11), ('drink', 0.11), ('fireplace', 0.11), ('ruin', 0.1), ('brittle', 0.1), ('fragment', 0.1), ('stumble', 0.09), ('formation', 0.09), ('shatter', 0.08), ('great', 0.08), ('friction', 0.08), ('flash', 0.07), ('cracks', 0.07), ('levels', 0.07), ('smash', 0.04), ('fail', 0.04), ('fra', 0.04), ('##glass', 0.03), ('variables', 0.03), ('because', 0.02), ('knock', 0.02), ('sun', 0.02), ('crush', 0.01), ('##e', 0.01), ('anger', 0.01)]
```

**naver/splade-v2-distil** (~100% more tokens + FLOPS = 3.82)
```python
number of actual dimensions:  234
SPLADE BOW rep:
 [('glass', 2.55), ('stress', 2.39), ('thermal', 2.38), ('glasses', 1.95), ('stressed', 1.87), ('crack', 1.84), ('cool', 1.78), ('heat', 1.62), ('pan', 1.6), ('break', 1.53), ('adjacent', 1.44), ('hotter', 1.43), ('strain', 1.21), ('area', 1.16), ('adjoining', 1.14), ('heated', 1.11), ('window', 1.07), ('stresses', 1.04), ('hot', 1.03), ('created', 1.03), ('create', 1.03), ('cause', 1.02), ('factors', 1.02), ('cooler', 1.01), ('broken', 1.0), ('too', 0.99), ('fracture', 0.96), ('collapse', 0.96), ('cracking', 0.95), ('great', 0.93), ('happen', 0.93), ('windows', 0.89), ('broke', 0.87), ('##e', 0.87), ('pressure', 0.84), ('hottest', 0.84), ('breaking', 0.83), ('govern', 0.79), ('shatter', 0.76), ('level', 0.75), ('heating', 0.69), ('temperature', 0.69), ('cracked', 0.69), ('panel', 0.68), ('##glass', 0.68), ('ceramic', 0.67), ('sash', 0.66), ('warm', 0.66), ('areas', 0.64), ('creating', 0.63), ('will', 0.62), ('tension', 0.61), ('cracks', 0.61), ('optical', 0.6), ('mechanism', 0.58), ('kelly', 0.58), ('determined', 0.58), ('generate', 0.58), ('causes', 0.56), ('if', 0.56), ('factor', 0.56), ('the', 0.56), ('chemical', 0.55), ('governed', 0.55), ('crystal', 0.55), ('strike', 0.55), ('microsoft', 0.54), ('creates', 0.53), ('than', 0.53), ('relation', 0.53), ('glazed', 0.52), ('compression', 0.51), ('painting', 0.51), ('governing', 0.5), ('harden', 0.49), ('solar', 0.48), ('reflection', 0.48), ('ic', 0.46), ('split', 0.45), ('mirror', 0.44), ('damage', 0.43), ('ring', 0.42), ('formation', 0.42), ('wall', 0.41), ('burst', 0.4), ('radiant', 0.4), ('determine', 0.4), ('one', 0.4), ('plastic', 0.39), ('furnace', 0.39), ('difference', 0.39), ('melt', 0.39), ('get', 0.39), ('contract', 0.38), ('forces', 0.38), ('gets', 0.38), ('produce', 0.38), ('surrounding', 0.37), ('vibration', 0.37), ('tile', 0.37), ('fail', 0.36), ('warmer', 0.36), ('rock', 0.35), ('fault', 0.35), ('roof', 0.34), ('burned', 0.34), ('physics', 0.33), ('welding', 0.33), ('why', 0.33), ('a', 0.32), ('pop', 0.32), ('and', 0.31), ('fra', 0.3), ('stat', 0.3), ('withstand', 0.3), ('sunglasses', 0.3), ('material', 0.29), ('ice', 0.29), ('generated', 0.29), ('matter', 0.29), ('frame', 0.28), ('elements', 0.28), ('then', 0.28), ('.', 0.28), ('pont', 0.28), ('blow', 0.28), ('snap', 0.27), ('metal', 0.26), ('effect', 0.26), ('reaction', 0.26), ('related', 0.25), ('aluminium', 0.25), ('neighboring', 0.25), ('weight', 0.25), ('steel', 0.25), ('bulb', 0.25), ('tear', 0.25), ('coating', 0.25), ('plumbing', 0.25), ('co', 0.25), ('microwave', 0.24), ('formed', 0.24), ('pipe', 0.23), ('drink', 0.23), ('chemistry', 0.23), ('energy', 0.22), ('reflect', 0.22), ('dynamic', 0.22), ('leak', 0.22), ('is', 0.22), ('lens', 0.21), ('frost', 0.21), ('lenses', 0.21), ('produced', 0.21), ('induced', 0.2), ('arise', 0.2), ('plate', 0.2), ('equations', 0.19), ('affect', 0.19), ('tired', 0.19), ('mirrors', 0.18), ('thickness', 0.18), ('bending', 0.18), ('cabinet', 0.17), ('apart', 0.17), ('##thermal', 0.17), ('gas', 0.17), ('equation', 0.17), ('relationship', 0.17), ('composition', 0.17), ('engineering', 0.17), ('block', 0.16), ('breaks', 0.16), ('when', 0.16), ('definition', 0.16), ('collapsed', 0.16), ('generation', 0.16), (',', 0.16), ('philips', 0.16), ('later', 0.15), ('wood', 0.15), ('neighbouring', 0.15), ('structural', 0.14), ('regulate', 0.14), ('neighbors', 0.13), ('lighting', 0.13), ('happens', 0.13), ('more', 0.13), ('property', 0.13), ('cooling', 0.12), ('shattering', 0.12), ('melting', 0.12), ('how', 0.11), ('cloud', 0.11), ('barriers', 0.11), ('lam', 0.11), ('conditions', 0.11), ('rule', 0.1), ('insulation', 0.1), ('bathroom', 0.09), ('convection', 0.09), ('cavity', 0.09), ('source', 0.08), ('properties', 0.08), ('bend', 0.08), ('bottles', 0.08), ('ceramics', 0.07), ('temper', 0.07), ('tense', 0.07), ('keller', 0.07), ('breakdown', 0.07), ('concrete', 0.07), ('simon', 0.07), ('solids', 0.06), ('windshield', 0.05), ('eye', 0.05), ('sunlight', 0.05), ('brittle', 0.03), ('caused', 0.03), ('suns', 0.03), ('floor', 0.02), ('components', 0.02), ('photo', 0.02), ('change', 0.02), ('sun', 0.01), ('crystals', 0.01), ('problem', 0.01), ('##proof', 0.01), ('parameters', 0.01), ('gases', 0.0), ('prism', 0.0), ('doing', 0.0), ('lattice', 0.0), ('ground', 0.0)]
```

- *Note 1: This specific passage was used as an example for [ease of comparison](https://github.com/naver/splade/blob/main/inference_splade.ipynb)*

</details>

## 4. How does it translate into Empirical metrics?

Our models are token sparse and yet effective. It translates to faster retrieval (User experience) and smaller index size ($). Mean retrieval time on the standard MS-MARCO small dev set and Scaled total FLOPS loss are the respective metrics are below.
This is why Google's SparseEmbed is interesting as they also achieve SPLADE quality retrieval effectiveness with much lower FLOPs. Compared to ColBERT, SPLADE and SparseEmbed match query and
document terms with a linear complexity as ColBERT’s late interaction i.e. all query-document term pairs takes a quadratic complexity. The Challenge with SparseEmbed is it uses a hyperparameter called **Top-k to restrict number of tokens used to learn contextual dense representations.**  Say 64 and 256 tokens for query and passage encoding.
But it is unclear how well these hyperparameters are transferable to other domains or languages (where the notion of tokens changes a lot like our mother tongue Tamil which is Agglutinative in nature). 

<img src="./Metrics.png" width=800/>

<details>

**Note: Why Anserini not PISA?** *Anserini is a production ready lucene based library. Common industry search deployments use Solr or elastic which are lucene based, hence the performance can be comparable. PISA latency is irrelevant for industry as it is a a research only system.*
The full [anserini evaluation log](https://huggingface.co/prithivida/Splade_PP_en_v1/blob/main/anserini_run.log) with encoding, indexing and querying details are here.

- **BEIR ZST OOD performance**: Will be added to the end of page.

**Our model is different in few more aspects**
- **Cocondenser Weights**: Unlike the best Official SPLADE++ or SparseEmbed we do NOT initialse weights from Luyu/co-condenser* models. Yet we achieve CoCondenser SPLADE level performance. More on this later.
- **Same size models:** Official SPLADE++, SparseEmbed and Ours all finetune on the same size based model. Size of `bert-base-uncased`.
</details>

## 5. Roadmap and future directions for Industry Suitability.

- **Improve efficiency**: This is a bottomless pit, Will continue to improve serving and retrieval efficiency.
- **Custom/Domain Finetuning**: OOD Zeroshot performance of SPLADE models is great but unimportant in the industry setting as we need the ability to finetune on custom datasets or domains. Finetuning SPLADE on a new dataset is not cheap and needs labelling of queries and passages.
  So we will continue to see how we can enable economically finetuning our recipe on custom datasets without expensive labelling.
- **Multilingual SPLADE**: Training cost of SPLADE i.e (GPU budget) directly proportional to Vocab size of the base model, So Mulitlingual SPLADE either using mbert or XLMR can be expensive as they have
  120K and 250K vocab as opposed to 30K as in bert-base-uncased. We will continue to research to see how best we can extend our recipe to the multilingual world.


## 6. Usage

To enable a light weight inference solution without heavy **No Torch dependency** we will also release a library - **SPLADERunner**
Ofcourse if it doesnt matter you could always use these models with Huggingface transformers library.


<h1 id="htu">How to use? </h1>


## 6a. With Popular VectorDBs

| VectorDB | Colab Link |
|----------|------------|
| Pinecone | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1fB6LheD9wYG0G-nBHiz0z2juvljrsBum?usp=sharing) |
| Qdrant | TBD |

 

## 6b. With SPLADERunner Library

[SPLADERunner Library](https://github.com/PrithivirajDamodaran/SPLADERunner)

```python 
pip install spladerunner

#One-time init
from spladerunner import Expander
# Default model is the document expander.
exapander = Expander()

#Sample Document expansion
sparse_rep = expander.expand(
    ["The Manhattan Project and its atomic bomb helped bring an end to World War II. Its legacy of peaceful uses of atomic energy continues to have an impact on history and science."])
```

 

## 6c. With HuggingFace

**NOTEBOOK user? Login first**

```
!huggingface-cli login
```

**Integrating in your code ?**
[How to use HF tokens in code](https://huggingface.co/docs/hub/en/security-tokens) 
Make these changes

```
tokenizer = AutoTokenizer.from_pretrained('prithivida/Splade_PP_en_v1', token=<Your token>)
model = AutoModelForMaskedLM.from_pretrained('prithivida/Splade_PP_en_v1', token=<Your token>)
```

**Full code**

```python
import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer

device = "cuda:0" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained('prithivida/Splade_PP_en_v1')
reverse_voc = {v: k for k, v in tokenizer.vocab.items()}
model = AutoModelForMaskedLM.from_pretrained('prithivida/Splade_PP_en_v1')
model.to(device)

sentence = """The Manhattan Project and its atomic bomb helped bring an end to World War II. Its legacy of peaceful uses of atomic energy continues to have an impact on history and science."""

inputs = tokenizer(sentence, return_tensors='pt')
inputs = {key: val.to(device) for key, val in inputs.items()}
input_ids = inputs['input_ids']

attention_mask = inputs['attention_mask']

outputs = model(**inputs)

logits, attention_mask = outputs.logits, attention_mask
relu_log = torch.log(1 + torch.relu(logits))
weighted_log = relu_log * attention_mask.unsqueeze(-1)
max_val, _ = torch.max(weighted_log, dim=1)
vector = max_val.squeeze()


cols = vector.nonzero().squeeze().cpu().tolist()
print("number of actual dimensions: ", len(cols))
weights = vector[cols].cpu().tolist()

d = {k: v for k, v in zip(cols, weights)}
sorted_d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
bow_rep = []
for k, v in sorted_d.items():
    bow_rep.append((reverse_voc[k], round(v,2)))

print("SPLADE BOW rep:\n", bow_rep)

```

## BEIR Zeroshot OOD performance:
<img src="./splade_v1.png" width=100% height=850/>


## Training details:
T.B.D  

## Acknowledgements

- Thanks to Nils Reimers for all the inputs.
- Thanks to authors of the Anserini library.


## Limitations and bias

All limitations and biases of the BERT model applies to finetuning effort.

## Citation

Please cite if you use our models or libraries. Citation info below.

```
Damodaran, P. (2024). Splade_PP_en_v1: Independent Implementation of SPLADE++ Model (`a.k.a splade-cocondenser* and family`) for the Industry setting. (Version 1.0.0) [Computer software].
```
