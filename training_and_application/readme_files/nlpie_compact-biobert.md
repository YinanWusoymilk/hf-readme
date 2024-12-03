---
title: README
emoji: 🏃
colorFrom: gray
colorTo: purple
sdk: static
pinned: false
license: mit
---

# Model Description
CompactBioBERT is a distilled version of the [BioBERT](https://huggingface.co/dmis-lab/biobert-base-cased-v1.2?text=The+goal+of+life+is+%5BMASK%5D.) model which is distilled for 100k training steps using a total batch size of 192 on the PubMed dataset. 

# Distillation Procedure
This model has the same overall architecture as [DistilBioBERT](https://huggingface.co/nlpie/distil-biobert) with the difference that here we combine the distillation approaches of DistilBioBERT and [TinyBioBERT](https://huggingface.co/nlpie/tiny-biobert). We utilise the same initialisation technique as in [DistilBioBERT](https://huggingface.co/nlpie/distil-biobert), and apply a layer-to-layer distillation with three major components, namely, MLM, layer, and output distillation.

# Initialisation
Following [DistilBERT](https://huggingface.co/distilbert-base-uncased?text=The+goal+of+life+is+%5BMASK%5D.), we initialise the student model by taking weights from every other layer of the teacher.

# Architecture
In this model, the size of the hidden dimension and the embedding layer are both set to 768. The vocabulary size is 28996. The number of transformer layers is 6 and the expansion rate of the feed-forward layer is 4. Overall, this model has around 65 million parameters.

# Citation
If you use this model, please consider citing the following paper:

```bibtex
@article{rohanian2023effectiveness,
  title={On the effectiveness of compact biomedical transformers},
  author={Rohanian, Omid and Nouriborji, Mohammadmahdi and Kouchaki, Samaneh and Clifton, David A},
  journal={Bioinformatics},
  volume={39},
  number={3},
  pages={btad103},
  year={2023},
  publisher={Oxford University Press}
}
```