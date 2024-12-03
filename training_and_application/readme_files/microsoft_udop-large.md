---
license: mit
tags:
- vision
inference: false
pipeline_tag: image-text-to-text
---

# UDOP model

The UDOP model was proposed in [Unifying Vision, Text, and Layout for Universal Document Processing](https://arxiv.org/abs/2212.02623) by Zineng Tang, Ziyi Yang, Guoxin Wang, Yuwei Fang, Yang Liu, Chenguang Zhu, Michael Zeng, Cha Zhang, Mohit Bansal.

## Model description

UDOP adopts an encoder-decoder Transformer architecture based on T5 for document AI tasks like document image classification, document parsing and document visual question answering.

## Intended uses & limitations

You can use the model for document image classification, document parsing and document visual question answering (DocVQA).

### How to use

Here's how to use the model on a document image:

```python
from transformers import AutoProcessor, UdopForConditionalGeneration
from datasets import load_dataset

# load model and processor
# in this case, we already have performed OCR ourselves
# so we initialize the processor with `apply_ocr=False`
processor = AutoProcessor.from_pretrained("microsoft/udop-large", apply_ocr=False)
model = UdopForConditionalGeneration.from_pretrained("microsoft/udop-large")

# load an example image, along with the words and coordinates
# which were extracted using an OCR engine
dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train")
example = dataset[0]
image = example["image"]
words = example["tokens"]
boxes = example["bboxes"]
question = "Question answering. What is the date on the form?"

# prepare everything for the model
encoding = processor(image, question, words, boxes=boxes, return_tensors="pt")

# autoregressive generation
predicted_ids = model.generate(**encoding)
print(processor.batch_decode(predicted_ids, skip_special_tokens=True)[0])
9/30/92
```

Refer to the [demo notebooks](https://github.com/NielsRogge/Transformers-Tutorials/tree/master/UDOP) for fine-tuning/inference.

### BibTeX entry and citation info

```bibtex
@misc{tang2023unifying,
      title={Unifying Vision, Text, and Layout for Universal Document Processing}, 
      author={Zineng Tang and Ziyi Yang and Guoxin Wang and Yuwei Fang and Yang Liu and Chenguang Zhu and Michael Zeng and Cha Zhang and Mohit Bansal},
      year={2023},
      eprint={2212.02623},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```