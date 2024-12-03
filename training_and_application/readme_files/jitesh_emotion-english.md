---
license: mit
language:
- en
pipeline_tag: text-classification
tags:
- emotion
- 20 classes
- code
- emotions
widget:
- text: I'm so angry right now. I can't believe he did that to me.
  example_title: anger
- text: I'm feeling disgusted by the smell of this food.
  example_title: disgust
- text: I'm feeling very afraid of what might happen next.
  example_title: fear
- text: I'm so joyful right now! This is the best day of my life.
  example_title: joy
- text: >-
    I'm feeling neutral about this situation. I don't really care one way or
    another.
  example_title: neutral
- text: I'm feeling really sad today after my dog passed away."
  example_title: sadness
- text: I'm so surprised by what just happened! I never saw that coming.
  example_title: surprise
- text: I'm feeling cheeky today. I'm going to play a little prank on my friend.
  example_title: cheeky
- text: I'm feeling confused about what to do next. I need some guidance.
  example_title: confuse
- text: I'm feeling curious about the world around me. There's so much to learn!
  example_title: curious
- text: I'm feeling empathetic towards my friend who is going through a tough time.
  example_title: empathetic
- text: I'm feeling grumpy today. Everything is annoying me!
  example_title: grumpy
- text: I'm feeling guilty about what I did. I wish I could take it back.
  example_title: guilty
- text: I'm feeling very energetic today. I'm ready to take on the world!
  example_title: energetic
- text: I'm feeling impatient waiting for this movie to start.
  example_title: impatient
- text: >-
    I'm feeling so much love for my family right now. They mean everything to
    me.
  example_title: love
- text: I'm thinking about my future and what I want to achieve.
  example_title: think
- text: >-
    I'm feeling serious about this issue. It's important and needs to be
    addressed.
  example_title: serious
- text: >-
    I'm feeling suspicious of what he's telling me. I think he's hiding
    something.
  example_title: suspicious
- text: I'm feeling whiny today. Everything is bothering me!
  example_title: whiny
- text: I love football so much
  example_title: love 2
- text: I'm reflecting on my experiences to gain insights
  example_title: think 2
- text: >-
    I borrowed money from a friend and haven't paid it back yet. Now I feel
    ashamed.
  example_title: guilty 2
- text: I'm starting to think that he's up to something.
  example_title: suspicious 2
- text: We need to approach this matter with a sense of purpose
  example_title: serious 2
---

# Emotion classification from 20 classes

## 20 Emotion labels
| id  | label      |
| --- | ---------- |
| 0   | anger      |
| 1   | cheeky     |
| 2   | confuse    |
| 3   | curious    |
| 4   | disgust    |
| 5   | empathetic |
| 6   | energetic  |
| 7   | fear       |
| 8   | grumpy     |
| 9   | guilty     |
| 10  | impatient  |
| 11  | joy        |
| 12  | love       |
| 13  | neutral    |
| 14  | sadness    |
| 15  | serious    |
| 16  | surprise   |
| 17  | suspicious |
| 18  | think      |
| 19  | whiny      |


## How to use
Here is how to use this model to get the emotion label of a given text:


```python
from transformers import AutoModelForSequenceClassification, pipeline

model_name = 'jitesh/emotion-english'
model = AutoModelForSequenceClassification.from_pretrained(model_name)
classifier = pipeline("text-classification", model=model, tokenizer=model_name)

text = "I can't wait any longer "

prediction = classifier(text)
print(prediction[0], text)
```

The above code outputs the following line.
```bash
{'label': 'impatient', 'score': 0.924211859703064} I can't wait any longer 
```