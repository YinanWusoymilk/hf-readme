---
tags:
- ultralyticsplus
- yolov8
- ultralytics
- yolo
- vision
- object-detection
- pytorch
- finance
- stock market
- candlesticks
- pattern recognition
- option trading
- chart reader
- future stock prediction
- trends prediction
library_name: ultralytics
library_version: 8.0.43
inference: false
model-index:
- name: foduucom/stockmarket-future-prediction
  results:
  - task:
      type: object-detection
    metrics:
    - type: precision
      value: 0.649
      name: mAP@0.5(box)
language:
- en
pipeline_tag: object-detection
---


<div align="center">
  <img width="640" alt="foduucom/product-detection-in-shelf-yolov8" src="https://huggingface.co/foduucom/stockmarket-future-prediction/resolve/main/_Stockmarket-Future-Prediction.jpeg">
</div>
# Model Card for YOLOv8s Stock Market future trends prediction on Live Trading Video Data

## Model Summary

The YOLOv8s Stock Market future trends prediction model is an object detection model based on the YOLO (You Only Look Once) framework. It is designed to detect various chart patterns in real-time stock market trading video data. The model aids traders and investors by automating the analysis of chart patterns, providing timely insights for informed decision-making. The model has been fine-tuned on a diverse dataset and achieved high accuracy in detecting and classifying stock market future trend detection in live trading scenarios.

## Model Details

### Model Description
The YOLOv8s Stock Market future trends prediction model offers a transformative solution for traders and investors by enabling real-time detection of crucial chart patterns within live trading video data. As stock markets evolve rapidly, this model's capabilities empower users with timely insights, allowing them to make informed decisions with speed and accuracy.

The model seamlessly integrates into live trading systems, providing instant trends prediction and classification. By leveraging advanced bounding box techniques and pattern-specific feature extraction, the model excels in identifying patterns such as 'Down','Up'. This enables traders to optimize their strategies, automate trading decisions, and respond to market trends in real-time.

To facilitate integration into live trading systems or to inquire about customization, please contact us at info@foduu.com. Your collaboration and feedback are instrumental in refining and enhancing the model's performance in dynamic trading environments.

- **Developed by:** FODUU AI
- **Model type:** Object Detection
- **Task:** Stock Market future trends prediction on Live Trading Video Data

The YOLOv8s Stock Market Pattern Detection model is designed to adapt to the fast-paced nature of live trading environments. Its ability to operate on real-time video data allows traders and investors to harness pattern-based insights without delay.

### Supported Labels

```
['Down','Up']
```

## Uses

### Direct Use

The YOLOv8s Stock Market future trends prediction model can be directly integrated into live trading systems to provide real-time detection and classification of chart patterns or classify the upcoming trends. Traders can utilize the model's insights for timely decision-making.

### Downstream Use

The model's real-time capabilities can be leveraged to automate trading strategies, generate alerts for specific patterns or trends, and enhance overall trading performance.

### Out-of-Scope Use

The model is not designed for unrelated object detection tasks or scenarios outside the scope of stock market trends prediction in live trading video data.

## Bias, Risks, and Limitations

The YOLOv8s Stock Market future prediction model may exhibit some limitations and biases:

- Performance may be affected by variations in video quality, lighting conditions, and pattern complexity within live trading data.
- Rapid market fluctuations and noise in video data may impact the model's accuracy and responsiveness.
- Market-specific patterns or anomalies not well-represented in the training data may pose challenges for detection.

### Recommendations

Users should be aware of the model's limitations and potential biases. Thorough testing and validation within live trading simulations are advised before deploying the model in real trading environments.

## How to Get Started with the Model

To begin using the YOLOv8s Stock Market future prediction model on live trading video data, follow these steps:
```bash
pip install ultralyticsplus==0.0.28 ultralytics==8.0.43
```

- Load model and perform real-time prediction:

```python
from ultralyticsplus import YOLO, render_result
import cv2

# load model
model = YOLO('foduucom/stockmarket-future-prediction')

# set model parameters
model.overrides['conf'] = 0.25  # NMS confidence threshold
model.overrides['iou'] = 0.45  # NMS IoU threshold
model.overrides['agnostic_nms'] = False  # NMS class-agnostic
model.overrides['max_det'] = 1000  # maximum number of detections per image

# set image
image = '/path/to/your/document/images'

# perform inference
results = model.predict(image)

# observe results
print(results[0].boxes)
render = render_result(model=model, image=image, result=results[0])
render.show()
```

## Training Details

### Training Data

The model is trained on a diverse dataset containing stock market chart images with various chart patterns, capturing different market conditions and scenarios.

### Training Procedure

The training process involves extensive computation and is conducted over multiple epochs. The model's weights are adjusted to minimize detection loss and optimize performance for stock market pattern detection.

#### Metrics

- mAP@0.5 (box): 0.65
  - All patterns: 0.90
  - Individual patterns: Varies based on pattern type

### Model Architecture and Objective

The YOLOv8s architecture incorporates modifications tailored to stock market future prediction. It features a specialized backbone network, self-attention mechanisms, and trends-specific feature extraction modules.

### Compute Infrastructure

#### Hardware

NVIDIA GeForce RTX 3080 card

#### Software

The model was trained and fine-tuned using a Jupyter Notebook environment.

## Model Card Contact

For inquiries and contributions, please contact us at info@foduu.com.

```bibtex
@ModelCard{
  author    = {Nehul Agrawal and
               Rahul parihar},
  title     = {YOLOv8s Stock Market future prediction on Live Trading Video Data},
  year      = {2023}
}
```