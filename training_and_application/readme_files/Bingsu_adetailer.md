---
license: apache-2.0
library_name: ultralytics
datasets:
- wider_face
- skytnt/anime-segmentation
tags:
- pytorch
---

# YOLOv8 Detection Model

## Datasets

### Face

- [Anime Face CreateML](https://universe.roboflow.com/my-workspace-mph8o/anime-face-createml)
- [xml2txt](https://universe.roboflow.com/0oooooo0/xml2txt-njqx1)
- [AN](https://universe.roboflow.com/sed-b8vkf/an-lfg5i)
- [wider face](http://shuoyang1213.me/WIDERFACE/index.html)

### Hand

- [AnHDet](https://universe.roboflow.com/1-yshhi/anhdet)
- [hand-detection-fuao9](https://universe.roboflow.com/catwithawand/hand-detection-fuao9)

### Person

- [coco2017](https://cocodataset.org/#home) (only person)
- [AniSeg](https://github.com/jerryli27/AniSeg)
- [skytnt/anime-segmentation](https://huggingface.co/datasets/skytnt/anime-segmentation)

### deepfashion2

- [deepfashion2](https://github.com/switchablenorms/DeepFashion2)

| id  | label                 |
| --- | --------------------- |
| 0   | short_sleeved_shirt   |
| 1   | long_sleeved_shirt    |
| 2   | short_sleeved_outwear |
| 3   | long_sleeved_outwear  |
| 4   | vest                  |
| 5   | sling                 |
| 6   | shorts                |
| 7   | trousers              |
| 8   | skirt                 |
| 9   | short_sleeved_dress   |
| 10  | long_sleeved_dress    |
| 11  | vest_dress            |
| 12  | sling_dress           |

## Info

| Model                       | Target                | mAP 50                        | mAP 50-95                     |
| --------------------------- | --------------------- | ----------------------------- | ----------------------------- |
| face_yolov8n.pt             | 2D / realistic face   | 0.660                         | 0.366                         |
| face_yolov8n_v2.pt          | 2D / realistic face   | 0.669                         | 0.372                         |
| face_yolov8s.pt             | 2D / realistic face   | 0.713                         | 0.404                         |
| face_yolov8m.pt             | 2D / realistic face   | 0.737                         | 0.424                         |
| face_yolov9c.pt             | 2D / realistic face   | 0.748                         | 0.433                         |
| hand_yolov8n.pt             | 2D / realistic hand   | 0.767                         | 0.505                         |
| hand_yolov8s.pt             | 2D / realistic hand   | 0.794                         | 0.527                         |
| hand_yolov9c.pt             | 2D / realistic hand   | 0.810                         | 0.550                         |
| person_yolov8n-seg.pt       | 2D / realistic person | 0.782 (bbox)<br/>0.761 (mask) | 0.555 (bbox)<br/>0.460 (mask) |
| person_yolov8s-seg.pt       | 2D / realistic person | 0.824 (bbox)<br/>0.809 (mask) | 0.605 (bbox)<br/>0.508 (mask) |
| person_yolov8m-seg.pt       | 2D / realistic person | 0.849 (bbox)<br/>0.831 (mask) | 0.636 (bbox)<br/>0.533 (mask) |
| deepfashion2_yolov8s-seg.pt | realistic clothes     | 0.849 (bbox)<br/>0.840 (mask) | 0.763 (bbox)<br/>0.675 (mask) |

## Usage

```python
from huggingface_hub import hf_hub_download
from ultralytics import YOLO

path = hf_hub_download("Bingsu/adetailer", "face_yolov8n.pt")
model = YOLO(path)
```

```python
import cv2
from PIL import Image

img = "https://farm5.staticflickr.com/4139/4887614566_6b57ec4422_z.jpg"
output = model(img)
pred = output[0].plot()
pred = cv2.cvtColor(pred, cv2.COLOR_BGR2RGB)
pred = Image.fromarray(pred)
pred
```

![image](https://i.imgur.com/9ny1wmD.png)


## Unsafe files

![image](https://i.imgur.com/9Btuy8j.png)

Since `getattr` is classified as a dangerous pickle function, any segmentation model that uses it is classified as unsafe.

All models were created and saved using the official [ultralytics](https://github.com/ultralytics/ultralytics) library, so it's okay to use files downloaded from a trusted source.

See also: https://huggingface.co/docs/hub/security-pickle
