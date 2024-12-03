---
tags:
- ultralyticsplus
- yolov8
- ultralytics
- yolo
- vision
- object-detection
- pytorch
- awesome-yolov8-models
library_name: ultralytics
library_version: 8.0.21
inference: false
datasets:
- keremberke/table-extraction
model-index:
- name: keremberke/yolov8m-table-extraction
  results:
  - task:
      type: object-detection
    dataset:
      type: keremberke/table-extraction
      name: table-extraction
      split: validation
    metrics:
    - type: precision
      value: 0.95194
      name: mAP@0.5(box)
license: agpl-3.0
---

<div align="center">
  <img width="640" alt="keremberke/yolov8m-table-extraction" src="https://huggingface.co/keremberke/yolov8m-table-extraction/resolve/main/thumbnail.jpg">
</div>

### Supported Labels

```
['bordered', 'borderless']
```

### How to use

- Install [ultralyticsplus](https://github.com/fcakyon/ultralyticsplus):

```bash
pip install ultralyticsplus==0.0.23 ultralytics==8.0.21
```

- Load model and perform prediction:

```python
from ultralyticsplus import YOLO, render_result

# load model
model = YOLO('keremberke/yolov8m-table-extraction')

# set model parameters
model.overrides['conf'] = 0.25  # NMS confidence threshold
model.overrides['iou'] = 0.45  # NMS IoU threshold
model.overrides['agnostic_nms'] = False  # NMS class-agnostic
model.overrides['max_det'] = 1000  # maximum number of detections per image

# set image
image = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'

# perform inference
results = model.predict(image)

# observe results
print(results[0].boxes)
render = render_result(model=model, image=image, result=results[0])
render.show()
```

**More models available at: [awesome-yolov8-models](https://yolov8.xyz)**