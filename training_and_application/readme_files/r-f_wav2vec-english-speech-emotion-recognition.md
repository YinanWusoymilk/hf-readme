---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model_index:
  name: wav2vec-english-speech-emotion-recognition
---
# Speech Emotion Recognition By Fine-Tuning Wav2Vec 2.0
The model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) for a Speech Emotion Recognition (SER) task.

Several datasets were used the fine-tune the original model:  
- Surrey Audio-Visual Expressed Emotion [(SAVEE)](http://kahlan.eps.surrey.ac.uk/savee/Database.html) - 480 audio files from 4 male actors
- Ryerson Audio-Visual Database of Emotional Speech and Song [(RAVDESS)](https://zenodo.org/record/1188976) - 1440 audio files from 24 professional actors (12 female, 12 male)
- Toronto emotional speech set [(TESS)](https://tspace.library.utoronto.ca/handle/1807/24487) - 2800 audio files from 2 female actors

7 labels/emotions were used as classification labels
```python
emotions = ['angry' 'disgust' 'fear' 'happy' 'neutral' 'sad' 'surprise']
```
It achieves the following results on the evaluation set:
- Loss: 0.104075
- Accuracy: 0.97463
## Model description
More information needed
## Intended uses & limitations
More information needed
## Training and evaluation data
More information needed
## Training procedure
### Training hyperparameters
The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 4
- eval_batch_size: 4
- eval_steps: 500
- seed: 42
- gradient_accumulation_steps: 2
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- num_epochs: 4
- max_steps=7500
- save_steps: 1500

### Training results
| Step | Training Loss | Validation Loss | Accuracy |
| ---- | ------------- | --------------- | -------- |
| 500  | 1.8124        | 1.365212        | 0.486258 |
| 1000 | 0.8872        | 0.773145        | 0.79704  |
| 1500 | 0.7035        | 0.574954        | 0.852008 |
| 2000 | 0.6879        | 1.286738        | 0.775899 |
| 2500 | 0.6498        | 0.697455        | 0.832981 |
| 3000 | 0.5696        | 0.33724         | 0.892178 |
| 3500 | 0.4218        | 0.307072        | 0.911205 |
| 4000 | 0.3088        | 0.374443        | 0.930233 |
| 4500 | 0.2688        | 0.260444        | 0.936575 |
| 5000 | 0.2973        | 0.302985        | 0.92389  |
| 5500 | 0.1765        | 0.165439        | 0.961945 |
| 6000 | 0.1475        | 0.170199        | 0.961945 |
| 6500 | 0.1274        | 0.15531         | 0.966173 |
| 7000 | 0.0699        | 0.103882        | 0.976744 |
| 7500 | 0.083         | 0.104075        | 0.97463  |