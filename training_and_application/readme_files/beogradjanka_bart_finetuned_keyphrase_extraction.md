---
datasets:
- midas/krapivin
- midas/inspec
- midas/kptimes
- midas/duc2001
language:
- en

widget:
  - text: "Relevance has traditionally been linked with feature subset selection, but formalization of this link has not been attempted. In this paper, we propose two axioms for feature subset selection sufficiency axiom and necessity axiombased on which this link is formalized: The expected feature subset is the one which maximizes relevance. Finding the expected feature subset turns out to be NP-hard. We then devise a heuristic algorithm to find the expected subset which has a polynomial time complexity. The experimental results show that the algorithm finds good enough subset of features which, when presented to C4.5, results in better prediction accuracy."
  - text: "In this paper, we investigate cross-domain limitations of keyphrase generation using the models for abstractive text summarization. We present an evaluation of BART fine-tuned for keyphrase generation across three types of texts, namely scientific texts from computer science and biomedical domains and news texts. We explore the role of transfer learning between different domains to improve the model performance on small text corpora."
---

# BART fine-tuned for keyphrase generation

<!-- Provide a quick summary of what the model is/does. -->

This is the <a href="https://huggingface.co/facebook/bart-base">bart-base</a> (<a href = "https://arxiv.org/abs/1910.13461">Lewis et al.. 2019</a>) model finetuned for the keyphrase generation task (<a href="https://arxiv.org/pdf/2312.10700.pdf">Glazkova & Morozov, 2023</a>) on the fragments of the following corpora: 

* Krapivin (<a href = "http://eprints.biblio.unitn.it/1671/1/disi09055%2Dkrapivin%2Dautayeu%2Dmarchese.pdf">Krapivin et al., 2009</a>)
* Inspec (<a href = "https://aclanthology.org/W03-1028.pdf">Hulth, 2003</a>)
* KPTimes (<a href = "https://aclanthology.org/W19-8617.pdf">Gallina, 2019</a>)
* DUC-2001 (<a href = "https://cdn.aaai.org/AAAI/2008/AAAI08-136.pdf">Wan, 2008</a>)
* PubMed (<a href = "https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=08b75d31a90f206b36e806a7ec372f6f0d12457e">Schutz, 2008</a>)
* NamedKeys (<a href = "https://joyceho.github.io/assets/pdf/paper/gero-bcb19.pdf">Gero & Ho, 2019</a>).

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("beogradjanka/bart_finetuned_keyphrase_extraction")
model = AutoModelForSeq2SeqLM.from_pretrained("beogradjanka/bart_finetuned_keyphrase_extraction")

text = "In this paper, we investigate cross-domain limitations of keyphrase generation using the models for abstractive text summarization.\
        We present an evaluation of BART fine-tuned for keyphrase generation across three types of texts, \
        namely scientific texts from computer science and biomedical domains and news texts. \
        We explore the role of transfer learning between different domains to improve the model performance on small text corpora."

tokenized_text = tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')
translation = model.generate(**tokenized_text)
translated_text = tokenizer.batch_decode(translation, skip_special_tokens=True)[0]
print(translated_text)
```

#### Training Hyperparameters

The following hyperparameters were used during training:

* learning_rate: 4e-5
* train_batch_size: 8
* optimizer: AdamW with betas=(0.9,0.999) and epsilon=1e-08
* num_epochs: 6

**BibTeX:**

```
@InProceedings{10.1007/978-3-031-67826-4_19,
author="Glazkova, Anna
and Morozov, Dmitry",
title="Cross-Domain Robustness of Transformer-Based Keyphrase Generation",
booktitle="Data Analytics and Management in Data Intensive Domains",
year="2024",
publisher="Springer Nature Switzerland",
address="Cham",
pages="249--265"
}
```

