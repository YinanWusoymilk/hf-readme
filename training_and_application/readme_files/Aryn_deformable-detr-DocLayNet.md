---
license: apache-2.0
tags:
- object-detection
- vision
datasets:
- DocLayNet
widget:
- src: https://huggingface.co/Aryn/deformable-detr-DocLayNet/resolve/main/examples/doclaynet_example_1.png
  example_title: DocLayNet Example 1
- src: https://huggingface.co/Aryn/deformable-detr-DocLayNet/resolve/main/examples/doclaynet_example_2.png
  example_title: DocLayNet Example 2
- src: https://huggingface.co/Aryn/deformable-detr-DocLayNet/resolve/main/examples/doclaynet_example_3.png
  example_title: DocLayNet Example 3
---

# Deformable DETR model trained on DocLayNet

Deformable DEtection TRansformer (DETR), trained on DocLayNet (including 80k annotated pages in 11 classes). 

You can use this model in the serverless [Aryn Partitioning Service](https://sycamore.readthedocs.io/en/stable/aryn_cloud/aryn_partitioning_service.html). You can get started [here](https://www.aryn.ai/get-started)

## Model description

The DETR model is an encoder-decoder transformer with a convolutional backbone. Two heads are added on top of the decoder outputs in order to perform 
object detection: a linear layer for the class labels and a MLP (multi-layer perceptron) for the bounding boxes. The model uses so-called object queries 
to detect objects in an image. Each object query looks for a particular object in the image. For COCO, the number of object queries is set to 100. 

The model is trained using a "bipartite matching loss": one compares the predicted classes + bounding boxes of each of the N = 100 object queries to the 
ground truth annotations, padded up to the same length N (so if an image only contains 4 objects, 96 annotations will just have a "no object" as class and 
"no bounding box" as bounding box). The Hungarian matching algorithm is used to create an optimal one-to-one mapping between each of the N queries and each 
of the N annotations. Next, standard cross-entropy (for the classes) and a linear combination of the L1 and generalized IoU loss (for the bounding boxes) are 
used to optimize the parameters of the model.

![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/deformable_detr_architecture.png)

## Intended uses & limitations

You can use the raw model for object detection. See the [model hub](https://huggingface.co/models?search=sensetime/deformable-detr) to look for all available 
Deformable DETR models.

### How to use

Here is how to use this model:

```python
from transformers import AutoImageProcessor, DeformableDetrForObjectDetection
import torch
from PIL import Image
import requests

url = "https://huggingface.co/Aryn/deformable-detr-DocLayNet/resolve/main/examples/doclaynet_example_1.png"
image = Image.open(requests.get(url, stream=True).raw)

processor = AutoImageProcessor.from_pretrained("Aryn/deformable-detr-DocLayNet")
model = DeformableDetrForObjectDetection.from_pretrained("Aryn/deformable-detr-DocLayNet")

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)

# convert outputs (bounding boxes and class logits) to COCO API
# let's only keep detections with score > 0.7
target_sizes = torch.tensor([image.size[::-1]])
results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.7)[0]

for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]
    print(
            f"Detected {model.config.id2label[label.item()]} with confidence "
            f"{round(score.item(), 3)} at location {box}"
    )
```

## Evaluation results

This model achieves 57.1 box mAP on DocLayNet.

## Training data

The Deformable DETR model was trained on DocLayNet. It was introduced in the paper [DocLayNet: A Large Human-Annotated Dataset for
Document-Layout Analysis](https://arxiv.org/abs/2206.01062) by Pfitzmann et al. and first released in [this repository](https://github.com/DS4SD/DocLayNet). 

### BibTeX entry and citation info

```bibtex
@misc{https://doi.org/10.48550/arxiv.2010.04159,
  doi = {10.48550/ARXIV.2010.04159},
  url = {https://arxiv.org/abs/2010.04159}, 
  author = {Zhu, Xizhou and Su, Weijie and Lu, Lewei and Li, Bin and Wang, Xiaogang and Dai, Jifeng},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Deformable DETR: Deformable Transformers for End-to-End Object Detection},
  publisher = {arXiv},
  year = {2020},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```