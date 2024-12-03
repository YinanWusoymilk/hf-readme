---
license: other
language:
- en
tags:
- biology
- medical
- cancer
datasets:
- owkin/nct-crc-he
- owkin/camelyon16-features
pipeline_tag: feature-extraction
---

# Model Card for Phikon

---

> [!IMPORTANT]
> 🎉 Check out the latest version of Phikon here: [Phikon-v2](https://huggingface.co/owkin/phikon-v2)
>
> 
Phikon is a self-supervised learning model for histopathology trained with iBOT. 

To learn more about how to use the model, we encourage you to read our blog post and view this Colab notebook.

### Model Description

- **Developed by:** Owkin
- **Funded by:** Owkin and IDRIS
- **Model type:** Vision Transformer Base
- **Model Stats:**
  - Params (M): 85.8
  - Image size: 224 x 224 x 3
- **Paper:**
  - Scaling Self-Supervised Learning for Histopathology with Masked Image Modeling. A. Filiot et al., medRxiv 2023.07.21.23292757; doi: [https://doi.org/10.1101/2023.07.21.23292757](https://www.medrxiv.org/content/10.1101/2023.07.21.23292757v2)
- **Pretrain Dataset:** 40 million pan-cancer tiles extracted from [TGCA](https://portal.gdc.cancer.gov/)
- **Original:** https://github.com/owkin/HistoSSLscaling/
- **License:** [Owkin non-commercial license](https://github.com/owkin/HistoSSLscaling/blob/main/LICENSE.txt)
 
## Uses

### Direct Use

The primary use of the Phikon model can be used for feature extraction from histology image tiles. 

### Downstream Use 

The model can be used for cancer classification on a variety of cancer subtypes. The model can also be finetuned to specialise on cancer subtypes.


## Technical Specifications

### Compute Infrastructure

All the models we built were trained on the French Jean Zay cluster.

### Hardware

NVIDIA V100 GPUs with 32Gb RAM 

### Software

PyTorch 1.13.1

---

### BibTeX entry and citation info

```bibtex
@article{Filiot2023ScalingSSLforHistoWithMIM,
	author       = {Alexandre Filiot and Ridouane Ghermi and Antoine Olivier and Paul Jacob and Lucas Fidon and Alice Mac Kain and Charlie Saillard and Jean-Baptiste Schiratti},
	title        = {Scaling Self-Supervised Learning for Histopathology with Masked Image Modeling},
	elocation-id = {2023.07.21.23292757},
	year         = {2023},
	doi          = {10.1101/2023.07.21.23292757},
	publisher    = {Cold Spring Harbor Laboratory Press},
	url          = {https://www.medrxiv.org/content/early/2023/07/26/2023.07.21.23292757},
	eprint       = {https://www.medrxiv.org/content/early/2023/07/26/2023.07.21.23292757.full.pdf},
	journal      = {medRxiv}
}
```