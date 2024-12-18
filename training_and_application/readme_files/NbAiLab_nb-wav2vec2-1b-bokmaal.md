---
license: apache-2.0
tags:
- automatic-speech-recognition
- NbAiLab/NPSC
- no
- nb
- nb-NO
datasets:
- NbAiLab/NPSC
language:
- nb
- no
model-index:
- name: nb-wav2vec2-1b-bokmaal
  results:
  - task:
      name: Automatic Speech Recognition 
      type: automatic-speech-recognition
    dataset:
      name: NPSC
      type: NbAiLab/NPSC
      args: 16K_mp3_bokmaal
    metrics:
       - name: Test (Bokmål) WER
         type: wer
         value: 0.0633
       - name: Test (Bokmål) CER
         type: cer
         value: 0.0248
---

# Norwegian Wav2Vec2 Model - 1B Bokmål
This model is finetuned on top of feature extractor [XLS-R](https://huggingface.co/facebook/wav2vec2-xls-r-1b) from Facebook/Meta. The finetuned model achieves the following results on the test set with a 5-gram KenLM. The numbers in parentheses are the results without the language model:
- **WER: 0.0633** (0.0738)
- **CER: 0.0248** (0.0263)

## Model description
This is one of several Wav2Vec-models our team created during the 🤗 hosted [Robust Speech Event](https://discuss.huggingface.co/t/open-to-the-community-robust-speech-recognition-challenge/13614?s=09). This is the complete list of our models and their final scores:

| Model         | Final WER   | |
|:--------------|:------------|:------------:|
| NbAiLab/nb-wav2vec2-1b-bokmaal (this model) |  6.33 |                                          |
| [NbAiLab/nb-wav2vec2-300m-bokmaal](https://huggingface.co/NbAiLab/nb-wav2vec2-300m-bokmaal) |  7.03 |                                      |
| [NbAiLab/nb-wav2vec2-1b-nynorsk](https://huggingface.co/NbAiLab/nb-wav2vec2-1b-nynorsk) |  11.32 |                                      |
| [NbAiLab/nb-wav2vec2-300m-nynorsk](https://huggingface.co/NbAiLab/nb-wav2vec2-300m-nynorsk) | 12.22  |                                                |

## Dataset
In parallel with the event, the team also converted the [Norwegian Parliamentary Speech Corpus (NPSC)](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-58/) to the [NbAiLab/NPSC](https://huggingface.co/datasets/NbAiLab/NPSC) in 🤗 Dataset format and used that as the main source for training.

## Code
We have released all the code developed during the event so that the Norwegian NLP community can build upon it when developing even better Norwegian ASR models. The finetuning of these models is not very computationally demanding. After following the instructions here, you should be able to train your own automatic speech recognition system in less than a day with an average GPU.

## Team
The following people contributed to building this model: Rolv-Arild Braaten, Per Egil Kummervold, Andre Kåsen, Javier de la Rosa, Per Erik Solberg, and Freddy Wetjen. 

## Training procedure
To reproduce these results, we strongly recommend that you follow the [instructions from 🤗](https://github.com/huggingface/transformers/tree/master/examples/research_projects/robust-speech-event#talks) to train a simple Swedish model.

When you have verified that you are able to do this, create a fresh new repo. You can then start by copying the files ```run.sh``` and ```run_speech_recognition_ctc.py``` from our repo. Running these will create all the other necessary files, and should let you reproduce our results. With some tweaks to the hyperparameters, you might even be able to build an even better ASR. Good luck!

### Language Model
As the scores indicate, adding even a simple 5-gram language will improve the results.  🤗 has provided another [very nice blog](https://huggingface.co/blog/wav2vec2-with-ngram) explaining how to add a 5-gram language model to improve the ASR model. You can build this from your own corpus, for instance by extracting some suitable text from the [Norwegian Colossal Corpus](https://huggingface.co/datasets/NbAiLab/NCC). You can also skip some of the steps in the guide, and copy the [5-gram model from this repo](https://huggingface.co/NbAiLab/XLSR-300M-bokmaal/tree/main/language_model).


### Parameters
The final model was run using these parameters:
```
--dataset_name="NbAiLab/NPSC"
--model_name_or_path="facebook/wav2vec2-xls-r-1b"
--dataset_config_name="16K_mp3_bokmaal"
--output_dir="./"
--overwrite_output_dir
--num_train_epochs="40"
--per_device_train_batch_size="12"
--per_device_eval_batch_size="12" 
--gradient_accumulation_steps="2" 
--learning_rate="2e-5" 
--warmup_steps="2000" 
--length_column_name="input_length" 
--evaluation_strategy="steps" 
--text_column_name="text" 
--save_steps="500" 
--eval_steps="500" 
--logging_steps="100" 
--layerdrop="0.041" 
--attention_dropout="0.094" 
--activation_dropout="0.055" 
--hidden_dropout="0.047" 
--save_total_limit="3"
--freeze_feature_encoder 
--feat_proj_dropout="0.04" 
--mask_time_prob="0.082" 
--mask_time_length="10" 
--mask_feature_prob="0.25" 
--mask_feature_length="64" 
--gradient_checkpointing
--min_duration_in_seconds="0.5" 
--max_duration_in_seconds="30.0" 
	--ctc_zero_infinity=True 
--use_auth_token 
--seed="42" 
--fp16 
--group_by_length 
--do_train --do_eval 
--push_to_hub 
--preprocessing_num_workers="16"
```

Using these settings, the training might take 3-4 days on an average GPU. You can, however, get a decent model and faster results by tweaking these parameters.

| Parameter| Comment | 
|:-------------|:-----|
| per_device_train_batch_size       | Adjust this to the maximum of available memory. 16 or 24 might be good settings depending on your system  |
|gradient_accumulation_steps |Can be adjusted even further up to increase batch size and speed up training without running into memory issues |
| learning_rate|Can be increased, maybe as high as 1e-4. Speeds up training but might add instability |
| epochs| Can be decreased significantly. This is a huge dataset and you might get a decent result already after a couple of epochs|

## Citation

```bibtex
@inproceedings{de-la-rosa-etal-2023-boosting,
    title = "Boosting {N}orwegian Automatic Speech Recognition",
    author = "De La Rosa, Javier  and
      Braaten, Rolv-Arild  and
      Kummervold, Per  and
      Wetjen, Freddy",
    booktitle = "Proceedings of the 24th Nordic Conference on Computational Linguistics (NoDaLiDa)",
    month = may,
    year = "2023",
    address = "T{\'o}rshavn, Faroe Islands",
    publisher = "University of Tartu Library",
    url = "https://aclanthology.org/2023.nodalida-1.55",
    pages = "555--564",
    abstract = "In this paper, we present several baselines for automatic speech recognition (ASR) models for the two official written languages in Norway: Bokm{\aa}l and Nynorsk. We compare the performance of models of varying sizes and pre-training approaches on multiple Norwegian speech datasets. Additionally, we measure the performance of these models against previous state-of-the-art ASR models, as well as on out-of-domain datasets. We improve the state of the art on the Norwegian Parliamentary Speech Corpus (NPSC) from a word error rate (WER) of 17.10{\%} to 7.60{\%}, with models achieving 5.81{\%} for Bokm{\aa}l and 11.54{\%} for Nynorsk. We also discuss the challenges and potential solutions for further improving ASR models for Norwegian.",
}
```

See https://arxiv.org/abs/2307.01672

