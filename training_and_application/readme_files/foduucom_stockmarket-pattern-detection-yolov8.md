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
library_name: ultralytics
library_version: 8.0.43
inference: false
model-index:
- name: foduucom/stockmarket-pattern-detection-yolov8
  results:
  - task:
      type: object-detection
    metrics:
    - type: precision
      value: 0.61355
      name: mAP@0.5(box)
language:
- en
pipeline_tag: object-detection
---

<div align="center">
  <img width="500" alt="foduucom/stockmarket-pattern-detection-yolov8" src="https://huggingface.co/foduucom/stockmarket-pattern-detection-yolov8/resolve/main/thumbnail.jpg">
</div>

# Model Card for YOLOv8s Stock Market Pattern Detection on Live Trading Video Data

## Model Summary

The YOLOv8s Stock Market Pattern Detection model is an object detection model based on the YOLO (You Only Look Once) framework. It is designed to detect various chart patterns in real-time stock market trading video data. The model aids traders and investors by automating the analysis of chart patterns, providing timely insights for informed decision-making. The model has been fine-tuned on a diverse dataset and achieved high accuracy in detecting and classifying stock market patterns in live trading scenarios.

## Model Details

### Model Description
The YOLOv8s Stock Market Pattern Detection model offers a transformative solution for traders and investors by enabling real-time detection of crucial chart patterns within live trading video data. As stock markets evolve rapidly, this model's capabilities empower users with timely insights, allowing them to make informed decisions with speed and accuracy.

The model seamlessly integrates into live trading systems, providing instant pattern detection and classification. By leveraging advanced bounding box techniques and pattern-specific feature extraction, the model excels in identifying patterns such as 'Head and shoulders bottom,' 'Head and shoulders top,' 'M_Head,' 'StockLine,' 'Triangle,' and 'W_Bottom.' This enables traders to optimize their strategies, automate trading decisions, and respond to market trends in real-time.

To facilitate integration into live trading systems or to inquire about customization, please contact us at info@foduu.com. Your collaboration and feedback are instrumental in refining and enhancing the model's performance in dynamic trading environments.

- **Developed by:** FODUU AI
- **Model type:** Object Detection
- **Task:** Stock Market Pattern Detection on Live Trading Video Data

The YOLOv8s Stock Market Pattern Detection model is designed to adapt to the fast-paced nature of live trading environments. Its ability to operate on real-time video data allows traders and investors to harness pattern-based insights without delay.

### Supported Labels

```
['Head and shoulders bottom', 'Head and shoulders top', 'M_Head', 'StockLine', 'Triangle', 'W_Bottom']
```

## Uses

### Direct Use

The YOLOv8s Stock Market Pattern Detection model can be directly integrated into live trading systems to provide real-time detection and classification of chart patterns. Traders can utilize the model's insights for timely decision-making.

### Downstream Use

The model's real-time capabilities can be leveraged to automate trading strategies, generate alerts for specific patterns, and enhance overall trading performance.

### Training data 
The Stockmarket model was trained on custom dataset consisting of 9000/800 annotated images for training/validation respectively. 


### Out-of-Scope Use

The model is not designed for unrelated object detection tasks or scenarios outside the scope of stock market pattern detection in live trading video data.

## Bias, Risks, and Limitations

The YOLOv8s Stock Market Pattern Detection model may exhibit some limitations and biases:

- Performance may be affected by variations in video quality, lighting conditions, and pattern complexity within live trading data.
- Rapid market fluctuations and noise in video data may impact the model's accuracy and responsiveness.
- Market-specific patterns or anomalies not well-represented in the training data may pose challenges for detection.

### Recommendations

Users should be aware of the model's limitations and potential biases. Thorough testing and validation within live trading simulations are advised before deploying the model in real trading environments.

## How to Get Started with the Model

To begin using the YOLOv8s Stock Market Pattern Detection model on live trading video data, follow these steps:
```bash
pip install ultralyticsplus==0.0.28 ultralytics==8.0.43
```

- Load model and perform real-time prediction:

```python
from ultralyticsplus import YOLO, render_result
import cv2

# load model
model = YOLO('foduucom/stockmarket-pattern-detection-yolov8')

# set model parameters
model.overrides['conf'] = 0.25  # NMS confidence threshold
model.overrides['iou'] = 0.45  # NMS IoU threshold
model.overrides['agnostic_nms'] = False  # NMS class-agnostic
model.overrides['max_det'] = 1000  # maximum number of detections per image

# initialize video capture
# Open the video file
video_path = "path/to/your/video/file.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
```

## Training Details

### Training Data

The model is trained on a diverse dataset containing stock market chart images with various chart patterns, capturing different market conditions and scenarios.

### Training Procedure

The training process involves extensive computation and is conducted over multiple epochs. The model's weights are adjusted to minimize detection loss and optimize performance for stock market pattern detection.

#### Metrics

- mAP@0.5 (box): 
  - All patterns: 0.932
  - Individual patterns: Varies based on pattern type

### Model Architecture and Objective

The YOLOv8s architecture incorporates modifications tailored to stock market pattern detection. It features a specialized backbone network, self-attention mechanisms, and pattern-specific feature extraction modules.

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
               Pranjal Singh Thakur},
  title     = {YOLOv8s Stock Market Pattern Detection on Live Trading Video Data},
  year      = {2023}
}
```