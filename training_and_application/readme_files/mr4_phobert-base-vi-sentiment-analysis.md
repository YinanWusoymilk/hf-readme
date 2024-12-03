---
language:
- vi
library_name: transformers
pipeline_tag: text-classification
tags:
- Vietnamese
- sentiment
- analysis
---

# Sentiment Analysis in Vietnamese - Phân tích cảm xúc trong tiếng Việt
## Phở Bert phân tích cảm xúc


## Model description

Mô hình có tác dụng xác định cảm xúc của đoạn văn.
Sử dụng nhãn: "Tích cực", "Tiêu cực", "Trung tính"

Ví dụ:
Thời tiết hôm nay không được đẹp, trời mưa và lạnh.
```text
    Tiêu cực: 0.9596341252326965
    Tích cực: 0.010115462355315685
    Trung tính: 0.030250443145632744
```

Hôm nay đi làm thật vui, ăn uống thật ngon.
```text
    Tiêu cực: 0.002220266032963991
    Tích cực: 0.9917450547218323
    Trung tính: 0.006034655496478081
```

Bình thường. Không có gì đặc biệt.
```text
    Tiêu cực: 0.03198615834116936
    Tích cực: 0.05307402461767197
    Trung tính: 0.9149397611618042
```

## Base model

Mô hình được đạo tạo dựa trên cơ sở của model PhoBert-Base của VinAI (https://huggingface.co/vinai/phobert-large)

## Training data

Mô hình được đào tạo dựa trên dữ liệu được thu thập bởi linhlpv (https://www.kaggle.com/datasets/linhlpv/vietnamese-sentiment-analyst) - có chỉnh sửa.
Với 31436 nội dung đánh giá sảm phẩm.

## Model variations

Chưa xác định

## Intended uses & limitations

Chưa xác định

## License

Đây là một open-source library, bạn có thể sử dụng nó với bất kì mục đích nào.
Rất cảm ơn nếu bạn ghi nguồn khi sử dụng mô hình này (nếu không ghi cũng không sao).

### How to use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os


def clear():
    os.system('clear')


checkpoint = "mr4/phobert-base-vi-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
clear()
print("Ngày hôm nay của bạn thế nào?")
val = input("")
raw_inputs = [val]
inputs = tokenizer(raw_inputs, padding=True,
                   truncation=True, return_tensors="pt")
outputs = model(**inputs)
predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
clear()
print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
for i, prediction in enumerate(predictions):
    print(raw_inputs[i])
    for j, value in enumerate(prediction):
        print(
            "    " + model.config.id2label[j] + ": " + str(value.item()))
print("<<<<<<<<<<<<<<<<<<<<<<<<<<")

```

## Liên hệ

Mọi thông tin liên quan có thể liên hệ qua email: zZz4everzZz@live.co.uk.