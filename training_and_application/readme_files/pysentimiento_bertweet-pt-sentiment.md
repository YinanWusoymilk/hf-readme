---
language: 
  - pt
library_name: pysentimiento

tags:
  - twitter
  - sentiment-analysis

---
# Sentiment Analysis in Portuguese


Repository: [https://github.com/pysentimiento/pysentimiento/](https://github.com/pysentimiento/pysentimiento/)


Model trained for polarity detection in Portuguese. Base model is [BERTabaporu](https://huggingface.co/pablocosta/bertabaporu-base-uncased), a RoBERTa model trained in Portuguese tweets.

Uses `POS`, `NEG`, `NEU` labels.

## Usage

Use it directly with [pysentimiento](https://github.com/pysentimiento/pysentimiento)

```python
from pysentimiento import create_analyzer
analyzer = create_analyzer(task="sentiment", lang="pt")

analyzer.predict("isto é bonito")
# returns AnalyzerOutput(output=POS, probas={POS: 0.998, NEG: 0.002, NEU: 0.000})
```


## Citation

If you use this model in your research, please cite pysentimiento and RoBERTuito papers:

```
@misc{perez2021pysentimiento,
      title={pysentimiento: A Python Toolkit for Sentiment Analysis and SocialNLP tasks},
      author={Juan Manuel Pérez and Juan Carlos Giudici and Franco Luque},
      year={2021},
      eprint={2106.09462},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
@misc {pablo_botton_da_costa_2022,
author = { {pablo botton da costa} },
title = { bertabaporu-base-uncased (Revision 1982d0f) },
year = 2022,
url = { https://huggingface.co/pablocosta/bertabaporu-base-uncased },
doi = { 10.57967/hf/0019 },
publisher = { Hugging Face }
}
@InProceedings{BRUM18.389,
  author = {Henrico Brum and Maria das Gra\c{c}as Volpe Nunes},
  title = "{Building a Sentiment Corpus of Tweets in Brazilian Portuguese}",
  booktitle = {Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  year = {2018},
  month = {May 7-12, 2018},
  address = {Miyazaki, Japan},
  editor = {Nicoletta Calzolari (Conference chair) and Khalid Choukri and Christopher Cieri and Thierry Declerck and Sara Goggi and Koiti Hasida and Hitoshi Isahara and Bente Maegaard and Joseph Mariani and HÚlŔne Mazo and Asuncion Moreno and Jan Odijk and Stelios Piperidis and Takenobu Tokunaga},
  publisher = {European Language Resources Association (ELRA)},
  isbn = {979-10-95546-00-9},
  language = {english}
}
```