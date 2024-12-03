---
license: apache-2.0
metrics:
- accuracy
- f1
---
Returns with about 99.2% accuracy whether the face belongs to man or woman based on face image.

See https://www.kaggle.com/code/dima806/man-woman-face-image-detection-vit for more details.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6449300e3adf50d864095b90/jFvQNwdQhfI7e6zSXAQg1.png)

```
Classification report:

              precision    recall  f1-score   support

         man     0.9919    0.9921    0.9920      7071
       woman     0.9921    0.9919    0.9920      7072

    accuracy                         0.9920     14143
   macro avg     0.9920    0.9920    0.9920     14143
weighted avg     0.9920    0.9920    0.9920     14143
```