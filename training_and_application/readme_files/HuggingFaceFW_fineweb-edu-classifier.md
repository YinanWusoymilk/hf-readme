---
language:
- en
license: apache-2.0
---

# FineWeb-Edu classifier

## Model summary
This is a classifier for judging the educational value of web pages. It was developed to filter and curate educational content from web datasets and was trained on 450k [annotations](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-llama3-annotations) generated by [LLama3-70B-instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) for web samples from [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) dataset.

We used this classifier to build [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) dataset.
### How to use in transformers
To load the FineWeb-Edu classifier, use the following code:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/fineweb-edu-classifier")
model = AutoModelForSequenceClassification.from_pretrained("HuggingFaceTB/fineweb-edu-classifier")

text = "This is a test sentence."
inputs = tokenizer(text, return_tensors="pt", padding="longest", truncation=True)
outputs = model(**inputs)
logits = outputs.logits.squeeze(-1).float().detach().numpy()
score = logits.item()
result = {
    "text": text,
    "score": score,
    "int_score": int(round(max(0, min(score, 5)))),
}

print(result)
# {'text': 'This is a test sentence.', 'score': 0.07964489609003067, 'int_score': 0}
```

## Training
The classifier was trained on 450,000 pairs of web samples and their scores from 0 to 5, generated by Llama3. The samples were annotated based on their educational quality with 0 being not educational and 5 being highly educational. 

Below is the prompt used for LLama3 annotations:
    <div style="text-align: center; margin: 20px 0;">
        <img src="https://cdn-uploads.huggingface.co/production/uploads/61c141342aac764ce1654e43/fjZQ4izIj1rx1xQnBTKKr.png" alt="Prompt for LLM annotation" style="width: 90%; max-width: 800px; height: auto;">
    </div>    

We added a classification head with a single regression output to [Snowflake-arctic-embed](https://huggingface.co/Snowflake/snowflake-arctic-embed-m) and trained the model for 20 epochs with a learning rate of 3e-4. During training, the embedding and encoder layers were frozen to focus on the classification head. The model achieved an F1 score of 82% when converted to a binary classifier using a score threshold of 3.

**Training Details:**

- Model: Snowflake-arctic-embed with a classification head
- Dataset: 450,000 samples from Llama3 annotations
- Epochs: 20
- Learning Rate: 3e-4
- Evaluation Metric: F1 score

**Classification report**

We treat the regression model's predictions as discrete classes to calculate the metrics on a hold-out set of 46867 Llama3-annotated samples.
```
              precision    recall  f1-score   support

           0       0.75      0.49      0.59      5694
           1       0.78      0.84      0.81     26512
           2       0.57      0.61      0.59     10322
           3       0.56      0.50      0.53      3407
           4       0.58      0.35      0.44       807
           5       0.33      0.01      0.02       125

    accuracy                           0.71     46867
   macro avg       0.60      0.47      0.50     46867
weighted avg       0.71      0.71      0.71     46867
```

**Confusion matrix**

We verify that the predicted educational scores are indeed close to their ground truth, and are mostry impacted by the noisy annotation.
```
        2791  2858    45     0     0     0
         919 22343  3180    69     1     0
y_true     3  3225  6330   757     7     0
           1    66  1473  1694   173     0
           0     4    98   420   283     2
           0     0    18    85    21     1
                    y_pred
```


## Limitations
While the FineWeb-Edu classifier performs well in distinguishing high-quality educational content for FineWeb dataset, there are some limitations:

- Scope: The model's performance might change for other datasets, in particular for out of distribution samples. It is also focused on educational content relevant to primary and grade school levels and may not perform as well on content intended for higher education or specialized domains.
- Bias: The model's performance is dependent on the quality and representativeness of the training data and the LLM used for the annotation. Biases in both can affect the classifier's judgments. It might overfit to academic looking content for the higher scores and we recommend using int_score >= 3 as a threshold for data curation.
- Context: The classifier evaluates individual web pages or extracts without considering broader context, which might impact its effectiveness in certain scenarios.

The training and inference code is available on GitHub 
https://github.com/huggingface/cosmopedia/tree/main/classification