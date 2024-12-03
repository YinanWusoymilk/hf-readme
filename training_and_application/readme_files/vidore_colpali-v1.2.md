---
license: mit
library_name: colpali
base_model: vidore/colpaligemma-3b-pt-448-base
language:
- en
tags:
- vidore
datasets:
- vidore/colpali_train_set
---

# ColPali: Visual Retriever based on PaliGemma-3B with ColBERT strategy

ColPali is a model based on a novel model architecture and training strategy based on Vision Language Models (VLMs) to efficiently index documents from their visual features.
It is a [PaliGemma-3B](https://huggingface.co/google/paligemma-3b-mix-448) extension that generates [ColBERT](https://arxiv.org/abs/2004.12832)- style multi-vector representations of text and images. 
It was introduced in the paper [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449) and first released in [this repository](https://github.com/ManuelFay/colpali)

<p align="center"><img width=800 src="https://github.com/illuin-tech/colpali/blob/main/assets/colpali_architecture.webp?raw=true"/></p>

## Version specificity

This version is trained with `colpali-engine==0.2.0` but can be loaded for any version `>=0.2.0`.

Compared to `colpali`, this version is trained with right padding for queries to fix unwanted tokens in the query encoding.
It also stems from the fixed `vidore/colpaligemma-3b-pt-448-base` to guarantee deterministic projection layer initialization.
It was trained for 5 epochs, with in-batch negatives and hard mined negatives and a warmup of 1000 steps (10x longer) to help reduce non-english language collapse.

Data is the same as the ColPali data described in the paper.

## Model Description

This model is built iteratively starting from an off-the-shelf [SigLIP](https://huggingface.co/google/siglip-so400m-patch14-384) model. 
We finetuned it to create [BiSigLIP](https://huggingface.co/vidore/bisiglip) and fed the patch-embeddings output by SigLIP to an LLM, [PaliGemma-3B](https://huggingface.co/google/paligemma-3b-mix-448) to create [BiPali](https://huggingface.co/vidore/bipali). 

One benefit of inputting image patch embeddings through a language model is that they are natively mapped to a latent space similar to textual input (query). 
This enables leveraging the [ColBERT](https://arxiv.org/abs/2004.12832) strategy to compute interactions between text tokens and image patches, which enables a step-change improvement in performance compared to BiPali. 

## Model Training

### Dataset
Our training dataset of 127,460 query-page pairs is comprised of train sets of openly available academic datasets (63%) and a synthetic dataset made up of pages from web-crawled PDF documents and augmented with VLM-generated (Claude-3 Sonnet) pseudo-questions (37%). 
Our training set is fully English by design, enabling us to study zero-shot generalization to non-English languages. We explicitly verify no multi-page PDF document is used both [*ViDoRe*](https://huggingface.co/collections/vidore/vidore-benchmark-667173f98e70a1c0fa4db00d) and in the train set to prevent evaluation contamination. 
A validation set is created with 2% of the samples to tune hyperparameters.

*Note: Multilingual data is present in the pretraining corpus of the language model (Gemma-2B) and potentially occurs during PaliGemma-3B's multimodal training.*

### Parameters

All models are trained for 1 epoch on the train set. Unless specified otherwise, we train models in `bfloat16` format, use low-rank adapters ([LoRA](https://arxiv.org/abs/2106.09685)) 
with `alpha=32`  and `r=32` on the transformer layers from the language model, 
as well as the final randomly initialized projection layer, and use a `paged_adamw_8bit` optimizer. 
We train on an 8 GPU setup with data parallelism, a learning rate of 5e-5 with linear decay with 2.5% warmup steps, and a batch size of 32.

## Usage

Install [`colpali-engine`](https://github.com/illuin-tech/colpali):

```bash
pip install colpali-engine>=0.3.0,<0.4.0
```

Then run the following code:

```python
from typing import cast

import torch
from PIL import Image

from colpali_engine.models import ColPali, ColPaliProcessor

model_name = "vidore/colpali-v1.2"

model = ColPali.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="cuda:0",  # or "mps" if on Apple Silicon
).eval()

processor = ColPaliProcessor.from_pretrained(model_name)

# Your inputs
images = [
    Image.new("RGB", (32, 32), color="white"),
    Image.new("RGB", (16, 16), color="black"),
]
queries = [
    "Is attention really all you need?",
    "Are Benjamin, Antoine, Merve, and Jo best friends?",
]

# Process the inputs
batch_images = processor.process_images(images).to(model.device)
batch_queries = processor.process_queries(queries).to(model.device)

# Forward pass
with torch.no_grad():
    image_embeddings = model(**batch_images)
    querry_embeddings = model(**batch_queries)

scores = processor.score_multi_vector(querry_embeddings, image_embeddings)
```

## Limitations

 - **Focus**: The model primarily focuses on PDF-type documents and high-ressources languages, potentially limiting its generalization to other document types or less represented languages.
 - **Support**: The model relies on multi-vector retreiving derived from the ColBERT late interaction mechanism, which may require engineering efforts to adapt to widely used vector retrieval frameworks that lack native multi-vector support.

## License

ColPali's vision language backbone model (PaliGemma) is under `gemma` license as specified in its [model card](https://huggingface.co/google/paligemma-3b-mix-448). The adapters attached to the model are under MIT license.

## Contact

- Manuel Faysse: manuel.faysse@illuin.tech
- Hugues Sibille: hugues.sibille@illuin.tech
- Tony Wu: tony.wu@illuin.tech

## Citation

If you use any datasets or models from this organization in your research, please cite the original dataset as follows:

```bibtex
@misc{faysse2024colpaliefficientdocumentretrieval,
  title={ColPali: Efficient Document Retrieval with Vision Language Models}, 
  author={Manuel Faysse and Hugues Sibille and Tony Wu and Bilel Omrani and Gautier Viaud and Céline Hudelot and Pierre Colombo},
  year={2024},
  eprint={2407.01449},
  archivePrefix={arXiv},
  primaryClass={cs.IR},
  url={https://arxiv.org/abs/2407.01449}, 
}
```