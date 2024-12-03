---
license: mit
language:
- en
library_name: keras
---
# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

This model is used to classify the user-intent for the Danswer project, visit https://github.com/danswer-ai/danswer.

## Model Details
Multiclass classifier on top of distilbert-base-uncased

### Model Description

<!-- Provide a longer summary of what this model is. -->
Classifies user intent of queries into categories including:
0: Keyword Search
1: Semantic Search
2: Direct Question Answering


- **Developed by:** [DanswerAI]
- **License:** [MIT]
- **Finetuned from model [optional]:** [distilbert-base-uncased]

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** [https://github.com/danswer-ai/danswer]
- **Demo [optional]:** [Upcoming!]

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

This model is intended to be used in the Danswer Question-Answering System


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

This model has a very small dataset maintained by DanswerAI. If interested, reach out to danswer.dev@gmail.com.

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

This model is intended to be used in the Danswer (QA System)

## How to Get Started with the Model

```
from transformers import AutoTokenizer
from transformers import TFDistilBertForSequenceClassification
import tensorflow as tf

model = TFDistilBertForSequenceClassification.from_pretrained("danswer/intent-model")
tokenizer = AutoTokenizer.from_pretrained("danswer/intent-model")

class_semantic_mapping = {
        0: "Keyword Search",
        1: "Semantic Search",
        2: "Question Answer"
    }

# Get user input
user_query = "How do I set up Danswer to run on my local environment?"

# Encode the user input
inputs = tokenizer(user_query, return_tensors="tf", truncation=True, padding=True)

# Get model predictions
predictions = model(inputs)[0]

# Get predicted class
predicted_class = tf.math.argmax(predictions, axis=-1)

print(f"Predicted class: {class_semantic_mapping[int(predicted_class)]}")
```