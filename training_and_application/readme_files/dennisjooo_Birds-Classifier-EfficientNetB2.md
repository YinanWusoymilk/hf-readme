---
license: apache-2.0
base_model: google/efficientnet-b2
metrics:
- accuracy
pipeline_tag: image-classification
tags:
- biology
- efficientnet-b2
- image-classification
- vision
---

# Bird Classifier EfficientNet-B2 

## Model Description

Have you look at a bird and said "Boahh if only I know what bird that is". 
Unless you're an avid bird spotter (or just love birds in general), it's hard to differentiate some species of birds.
Well you're in luck, turns out you can use a image classifier to identify bird species!

This model is a fine-tuned version of [google/efficientnet-b2](https://huggingface.co/google/efficientnet-b2)
on the [gpiosenka/100-bird-species](https://www.kaggle.com/datasets/gpiosenka/100-bird-species) dataset available on Kaggle.
The dataset used to train the model was taken on September 24th, 2023. 

The original model itself was trained on ImageNet-1K, thus it might still have some useful features for identifying creatures like birds.

In theory, the accuracy for a random guess on this dataset is 0.0019047619 (essentially 1/525). 
The model performed significantly well on all three sets with result being:

- **Training**: 0.999480
- **Validation**: 0.985904
- **Test**: 0.991238

## Intended Uses

You can use the raw model for image classification.
Here is an example of the model in action using a picture of a bird

```python
# Importing the libraries needed
import torch
import urllib.request
from PIL import Image
from transformers import EfficientNetImageProcessor, EfficientNetForImageClassification

# Determining the file URL
url = 'some url'

# Opening the image using PIL
img = Image.open(urllib.request.urlretrieve(url)[0])

# Loading the model and preprocessor from HuggingFace
preprocessor = EfficientNetImageProcessor.from_pretrained("dennisjooo/Birds-Classifier-EfficientNetB2")
model = EfficientNetForImageClassification.from_pretrained("dennisjooo/Birds-Classifier-EfficientNetB2")

# Preprocessing the input
inputs = preprocessor(img, return_tensors="pt")

# Running the inference
with torch.no_grad():
    logits = model(**inputs).logits

# Getting the predicted label
predicted_label = logits.argmax(-1).item()
print(model.config.id2label[predicted_label])
```

Or alternatively you can streamline it using Huggingface's Pipeline

```python
# Importing the libraries needed
import torch
import urllib.request
from PIL import Image
from transformers import pipeline

# Determining the file URL
url = 'some url'

# Opening the image using PIL
img = Image.open(urllib.request.urlretrieve(url)[0])

# Loading the model and preprocessor using Pipeline
pipe = pipeline("image-classification", model="dennisjooo/Birds-Classifier-EfficientNetB2")

# Running the inference
result = pipe(img)[0]

# Printing the result label
print(result['label'])
```

## Training and Evaluation

### Data

The dataset was taken from [gpiosenka/100-bird-species](https://www.kaggle.com/datasets/gpiosenka/100-bird-species) on Kaggle. 
It contains a set of 525 bird species, with 84,635 training images, 2,625 each for validation and test images. 
Every image in the dataset is a 224 by 224 RGB image.

The training process used the same split provided by the author.
For more details, please refer to the [author's Kaggle page](https://www.kaggle.com/datasets/gpiosenka/100-bird-species).

### Training Procedure 

The training was done using PyTorch on Kaggle's free P100 GPU. The process also includes the usage of Lightning and Torchmetrics libraries.

### Preprocessing 
Each image is preprocessed according to the the orginal author's [config](https://huggingface.co/google/efficientnet-b2/blob/main/preprocessor_config.json).

The training set was also augmented using:

- Random rotation of 10 degrees with probability of 50%
- Random horizontal flipping with probability of 50%

### Training Hyperparameters

The following are the hyperparameters used for training:

- **Training regime:** fp32
- **Loss:** Cross entropy
- **Optimizer**: Adam with default betas (0.99, 0.999)
- **Learning rate**: 1e-3
- **Learning rate scheduler**: Reduce on plateau which monitors validation loss with patience of 2 and decay rate of 0.1
- **Batch size**: 64
- **Early stopping**: Monitors validation accuracy with patience of 10

### Results

The image below is the result of the training process both on the training and validation set:

![Training results](https://github.com/dennisjooo/Birds-Classifier-EfficientNetB2/raw/main/logs/metrics.png)

