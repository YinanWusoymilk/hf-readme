---
language:
- en
license: cc-by-nc-sa-4.0
tags:
- seq2seq
- relation-extraction
- triple-generation
- entity-linking
- entity-type-linking
- relation-linking
datasets: Babelscape/rebel-dataset
widget:
- text: The Italian Space Agency’s Light Italian CubeSat for Imaging of Asteroids,
    or LICIACube, will fly by Dimorphos to capture images and video of the impact
    plume as it sprays up off the asteroid and maybe even spy the crater it could
    leave behind.
model-index:
- name: knowgl
  results:
  - task:
      type: Relation-Extraction
      name: Relation Extraction
    dataset:
      name: Babelscape/rebel-dataset
      type: REBEL
    metrics:
    - type: re+ macro f1
      value: 70.74
      name: RE+ Macro F1
---

# KnowGL: Knowledge Generation and Linking from Text

The `knowgl-large` model is trained by combining Wikidata with an extended version of the training data in the [REBEL](https://huggingface.co/datasets/Babelscape/rebel-dataset) dataset. Given a sentence, KnowGL generates triple(s) in the following format:
```
[(subject mention # subject label # subject type) | relation label | (object mention # object label # object type)]
```
If there are more than one triples generated, they are separated by `$` in the output. More details in [Rossiello et al. (AAAI 2023)](https://arxiv.org/pdf/2210.13952.pdf).

The model achieves state-of-the-art results for relation extraction on the REBEL dataset. See results in [Mihindukulasooriya et al. (ISWC 2022)](https://arxiv.org/pdf/2207.05188.pdf).

The generated labels (for the subject, relation, and object) and their types can be directly mapped to Wikidata IDs associated with them.

#### Citation
```bibtex
@inproceedings{DBLP:conf/aaai/RossielloCMCG23,
  author       = {Gaetano Rossiello and
                  Md. Faisal Mahbub Chowdhury and
                  Nandana Mihindukulasooriya and
                  Owen Cornec and
                  Alfio Massimiliano Gliozzo},
  title        = {KnowGL: Knowledge Generation and Linking from Text},
  booktitle    = {{AAAI}},
  pages        = {16476--16478},
  publisher    = {{AAAI} Press},
  year         = {2023}
}
```

```bibtex
@inproceedings{DBLP:conf/semweb/Mihindukulasooriya22,
  author    = {Nandana Mihindukulasooriya and
               Mike Sava and
               Gaetano Rossiello and
               Md. Faisal Mahbub Chowdhury and
               Irene Yachbes and
               Aditya Gidh and
               Jillian Duckwitz and
               Kovit Nisar and
               Michael Santos and
               Alfio Gliozzo},
  title     = {Knowledge Graph Induction Enabling Recommending and Trend Analysis:
               {A} Corporate Research Community Use Case},
  booktitle = {{ISWC}},
  series    = {Lecture Notes in Computer Science},
  volume    = {13489},
  pages     = {827--844},
  publisher = {Springer},
  year      = {2022}
}
```