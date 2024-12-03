---
library_name: transformers
tags:
- text-to-speech
- annotation
license: apache-2.0
language:
- en
pipeline_tag: text-to-speech
inference: false
datasets:
  - ylacombe/expresso
  - reach-vb/jenny_tts_dataset
  - blabble-io/libritts_r
---

<img src="https://huggingface.co/datasets/parler-tts/images/resolve/main/thumbnail.png" alt="Parler Logo" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>


# Parler-TTS Mini: Expresso

<a target="_blank" href="https://huggingface.co/spaces/parler-tts/parler-tts-expresso">
  <img src="https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm.svg" alt="Open in HuggingFace"/>
</a>

**Parler-TTS Mini: Expresso** is a fine-tuned version of [Parler-TTS Mini v0.1](https://huggingface.co/parler-tts/parler_tts_mini_v0.1)
on the [Expresso](https://huggingface.co/datasets/ylacombe/expresso) dataset. It is a lightweight text-to-speech (TTS) 
model that can generate high-quality, natural sounding speech. Compared to the original model, Parler-TTS Expresso provides
superior control over **emotions** (happy, confused, laughing, sad) and **consistent voices** (Jerry, Thomas, Elisabeth, Talia).

It is part of the first release from the [Parler-TTS](https://github.com/huggingface/parler-tts) project, which aims to 
provide the community with TTS training resources and dataset pre-processing code. Details for reproducing this entire 
training run are provided in the section [Training Procedure](#training-procedure).

## Usage

Using Expresso is as simple as "bonjour". Simply install the library from source:

```sh
pip install git+https://github.com/huggingface/parler-tts.git
```

You can then use the model with the following inference snippet:

```py
import torch
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer, set_seed
import soundfile as sf

device = "cuda:0" if torch.cuda.is_available() else "cpu"

model = ParlerTTSForConditionalGeneration.from_pretrained("parler-tts/parler-tts-mini-expresso").to(device)
tokenizer = AutoTokenizer.from_pretrained("parler-tts/parler-tts-mini-expresso")

prompt = "Why do you make me do these examples? They're *so* generic."
description = "Thomas speaks moderately slowly in a sad tone with emphasis and high quality audio."

input_ids = tokenizer(description, return_tensors="pt").input_ids.to(device)
prompt_input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)

set_seed(42)
generation = model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
audio_arr = generation.cpu().numpy().squeeze()
sf.write("parler_tts_out.wav", audio_arr, model.config.sampling_rate)
```

**Tips**:
* Specify the name of a male speaker (Jerry, Thomas) or female speaker (Talia, Elisabeth) for consistent voices
* The model can generate in a range of emotions, including: "happy", "confused", "default" (meaning no particular emotion conveyed), "laughing", "sad", "whisper", "emphasis"
* Include the term "high quality audio" to generate the highest quality audio, and "very noisy audio" for high levels of background noise
* Punctuation can be used to control the prosody of the generations, e.g. use commas to add small breaks in speech
* To emphasise particular words, wrap them in asterisk (e.g. `*you*` in the example above) and include "emphasis" in the prompt

## Training Procedure

Expresso is a high-quality, expressive speech dataset that includes samples from four speakers (two male, two female).
By fine-tuning Parler-TTS Mini v0.1 on this dataset, we can train the model to follow emotion and speaker prompts.

To reproduce this fine-tuning run, we need to perform two steps:
1. Create text descriptions from the audio samples in the Expresso dataset
2. Train the model on the (text, audio) pairs

Step 1 is performed using the [DataSpeech](https://github.com/huggingface/dataspeech) library, and step 2 using 
[Parler-TTS](https://github.com/huggingface/parler-tts). Should you wish to use the pre-annotated dataset from our 
experiments, you can jump straight to [step 2](#step-2--fine-tune-the-model). For both, you can follow step 0 for 
getting set-up.

### Step 0: Set-Up

We'll start by creating a fresh Python environment:

```sh
python3 -m venv parler-env
source parler-env/bin/activate
```

Next, install PyTorch according to the [official instructions](https://pytorch.org/get-started/locally/). We can then 
install DataSpeech and Parler-TTS sequentially:

```sh
git clone git@github.com:huggingface/dataspeech.git && cd dataspeech && pip install -r requirements.txt
cd ..
git clone https://github.com/huggingface/parler-tts.git && cd parler-tts && pip install -e ."[train]"
cd ..
```

You can link your Hugging Face account so that you can push model repositories on the Hub. This will allow you to save 
your trained models on the Hub so that you can share them with the community. Simply run the command:

```sh
git config --global credential.helper store
huggingface-cli login
```

And then enter an authentication token from https://huggingface.co/settings/tokens. Create a new token if you do not 
have one already. You should make sure that this token has "write" privileges.

You also have the option to configure Accelerate by running the following command. Note that you should set the number 
of GPUs you wish to use for training/inference, and also the data type (dtype) based on your device (e.g. bfloat16 on 
A100 GPUs, float16 on V100 GPUs, etc.):

```sh
accelerate config
```

Optionally, you can also login to Weights and Biases for automatic logging:

```sh
wandb login
```

### Step 1: Create Text Descriptions

Creating text descriptions for the dataset comprises three sub-stages from DataSpeech, which we'll cover below.

#### 1.A. Annotate the Expresso dataset

We'll use the [`main.py`](https://github.com/huggingface/dataspeech/blob/main/main.py) file from DataSpeech to label 
the following continuous variables:
- Speaking rate
- Signal-to-noise ratio (SNR)
- Reverberation
- Speech monotony

This can be done with the following command:
```sh
python ./dataspeech/main.py "ylacombe/expresso" \
  --configuration "default" \
  --text_column_name "text" \
  --audio_column_name "audio" \
  --cpu_num_workers 8 \
  --rename_column \
  --repo_id "expresso-tags"
```

Note that the script will be faster if you have GPUs at your disposal. It will automatically scale up to every GPU available in your environment. To control which GPUs to run the script on consider indicating via `CUDA_VISIBLE_DEVICES` environment variable.

The resulting dataset will be pushed to the Hugging Face Hub under your Hugging Face handle. Mine was pushed to [reach-vb/expresso-tags](https://huggingface.co/datasets/reach-vb/expresso-tags).
We can see that the dataset is annotated with continuous features like "speaking_rate" and "snr".

#### 1.B. Map annotations to text bins

The next step involves mapping the continuous variables to discrete ones. This is achieved by binning the continuous variables
into buckets, and assigning each one a text label.

Since the ultimate goal here is to fine-tune the [Parler-TTS v0.1 checkpoint](https://huggingface.co/parler-tts/parler_tts_mini_v0.1) 
on the Expresso dataset, we want to stay consistent with the text bins of the dataset on which the original model was trained.

To do this, we'll pass [`v01_bin_edges.json`](https://github.com/huggingface/dataspeech/blob/main/examples/tags_to_annotations/v01_bin_edges.json)
as an input argument to our script, which holds the bin edges from the original dataset:

```sh
python ./dataspeech/scripts/metadata_to_text.py \
    "reach-vb/expresso-tags" \
    --repo_id "expresso-tags" \
    --configuration "default" \
    --cpu_num_workers "8" \
    --path_to_bin_edges "./examples/tags_to_annotations/v01_bin_edges.json" \
    --avoid_pitch_computation
```

Since we leverage the bins from the original dataset, the above script only takes a few seconds. The resulting dataset 
will be pushed to the Hugging Face Hub under your Hugging Face handle. Mine was pushed to [reach-vb/expresso-tags](https://huggingface.co/datasets/reach-vb/expresso-tags).

You can notice that text bins such as "slightly noisy", "quite monotone" have been added to the samples.

#### 1.C. Create natural language descriptions from those text bins

Now that we have text bins associated to the Expresso dataset, the next step is to create natural language descriptions. 
This involves passing the text bins to a large-language model (LLM), and have it generate corresponding descriptions.

There is a template [prompt creation script](https://github.com/huggingface/dataspeech/blob/main/scripts/run_prompt_creation.py) 
in Parler-TTS which can be used to generate descriptions from the features tagged in [step 1.A](#1a-annotate-the-expresso-dataset) (reverberation, noise, speaking rate, etc).

However, not all of these features are relevant for the Expresso dataset. For instance, Expresso was recorded in a 
professional recording studio, so all the samples are high quality. Thus, we chose to create prompts with the following subset of features:
1. Name: we mapped the speaker ids (ex1, ex2, ex3, ex4) to unique speaker names (Jerry, Elisabeth, Thomas, Talia). This encourages the model to learn specific speakers from the training data
2. Emotion: we include the emotion provided in the Expresso dataset
3. Speaking rate: we use the pre-computed text bins from the previous step

4. In addition, we also hard-coded the quality of the audio to be "very high-quality", given the studio recording conditions.

As an example, if we passed:
1. Speaker: Jerry
2. Emotion: confused
3. Speaking rate: moderate speed

We would expect to generate a sample along the lines of: "Jerry speaks with a confused tone and at a moderate speed with high quality audio."

The modified prompt creation script can be found in this repository. You can download this script with the following Python command:

```python
from huggingface_hub import hf_hub_download

hf_hub_download(repo_id="parler-tts/parler-tts-mini-expresso", filename="run_prompt_creation.py", local_dir="./run_prompt_creation_expresso.py")
```

You can then launch prompt creation using the [Mistral Instruct 7B](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) 
model with the following command:  

```sh
accelerate launch ./dataspeech/run_prompt_creation_expresso.py \
  --dataset_name "reach-vb/expresso-tags" \
  --dataset_config_name "default" \
  --model_name_or_path "mistralai/Mistral-7B-Instruct-v0.2" \
  --per_device_eval_batch_size 32 \
  --attn_implementation "sdpa" \
  --dataloader_num_workers 8 \
  --output_dir "./tmp_expresso" \
  --load_in_4bit \
  --push_to_hub \
  --hub_dataset_id "expresso-tagged-w-speech-mistral" \
  --preprocessing_num_workers 16
```

Note that the Mistral model is gated, so you should ensure you have accepted the terms-of-use from the [model card](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2).
You can find the annotated dataset under TODO [reach-vb/expresso-tagged-w-speech-mistral](https://huggingface.co/datasets/reach-vb/expresso-tagged-w-speech-mistral),
where you'll find sensible descriptions from the features that we passed.

This step generally demands more resources and times and should use one or many GPUs. Scaling to multiple GPUs using [distributed data parallelism (DDP)](https://pytorch.org/tutorials/beginner/ddp_series_theory.html)
is trivial: simply run `accelerate config` and select the multi-GPU option, specifying the IDs of the GPUs you wish to use. The 
above script can then be run using DDP with no code changes.

If you are resource constrained and need to use a smaller model, [Gemma 2B](https://huggingface.co/google/gemma-2b-it) 
is an excellent choice.

### Step 2: Fine-Tune the Model

Fine-tuning is performed using the Parler-TTS training script [run_parler_tts_training.py](https://github.com/huggingface/parler-tts/blob/main/training/run_parler_tts_training.py).
It is the same script used to pre-train the model, and can be used for fine-tuning without any code-changes.

To preserve the model's ability to generate speech with generic voice descriptions, such as in the style of 
[Parler-TTS Mini v0.1](https://huggingface.co/parler-tts/parler_tts_mini_v0.1), we fine-tuned the model 
on a combination of three datasets, including the test split of LibriTTS-R:
1. [Expresso](https://huggingface.co/datasets/ylacombe/expresso)
2. [Jenny](https://huggingface.co/datasets/reach-vb/jenny_tts_dataset)
3. [LibriTTS-R](https://huggingface.co/datasets/blabble-io/libritts_r)

This was achieved through the following command:

```sh
accelerate launch ./training/run_parler_tts_training.py \
    --model_name_or_path "parler-tts/parler_tts_mini_v0.1" \
    --feature_extractor_name "parler-tts/dac_44khZ_8kbps" \
    --description_tokenizer_name "parler-tts/parler_tts_mini_v0.1" \
    --prompt_tokenizer_name "parler-tts/parler_tts_mini_v0.1" \
    --report_to "wandb" \
    --overwrite_output_dir true \
    --train_dataset_name "ylacombe/expresso+reach-vb/jenny_tts_dataset+blabble-io/libritts_r+blabble-io/libritts_r" \
    --train_metadata_dataset_name "reach-vb/expresso-tagged-w-speech-mistral-v3+ylacombe/jenny-tts-10k-tagged+parler-tts/libritts_r_tags_tagged_10k_generated+parler-tts/libritts_r_tags_tagged_10k_generated" \
    --train_dataset_config_name "read+default+clean+other" \
    --train_split_name "train+train[:20%]+test.clean+test.other" \
    --eval_dataset_name "ylacombe/expresso+reach-vb/jenny_tts_dataset+blabble-io/libritts_r+blabble-io/libritts_r" \
    --eval_metadata_dataset_name "reach-vb/expresso-tagged-w-speech-mistral-v3+ylacombe/jenny-tts-10k-tagged+parler-tts/libritts_r_tags_tagged_10k_generated+parler-tts/libritts_r_tags_tagged_10k_generated" \
    --eval_dataset_config_name "read+default+clean+other" \
    --eval_split_name "train+train[:20%]+test.clean+test.other" \
    --max_eval_samples 8 \
    --per_device_eval_batch_size 16 \
    --target_audio_column_name "audio" \
    --description_column_name "text_description" \
    --prompt_column_name "text" \
    --max_duration_in_seconds 30.0 \
    --min_duration_in_seconds 2.0 \
    --max_text_length 400 \
    --preprocessing_num_workers 2 \
    --do_train true \
    --num_train_epochs 8 \
    --gradient_accumulation_steps 8 \
    --gradient_checkpointing true \
    --per_device_train_batch_size 16 \
    --learning_rate 0.00008 \
    --adam_beta1 0.9 \
    --adam_beta2 0.99 \
    --weight_decay 0.01 \
    --lr_scheduler_type "cosine" \
    --warmup_steps 250 \
    --logging_steps 2 \
    --freeze_text_encoder true \
    --audio_encoder_per_device_batch_size 4 \
    --dtype "bfloat16" \
    --seed 456 \
    --output_dir "./parler-tts-mini-expresso" \
    --temporary_save_to_disk "./audio_code_tmp" \
    --save_to_disk "./tmp_dataset_audio" \
    --dataloader_num_workers 4 \
    --do_eval \
    --predict_with_generate \
    --include_inputs_for_metrics \
    --group_by_length true
```

On a single 80GB A100 GPU, training took approximately 1.5 hours and returned a final evaluation loss of 4.0. Again, the 
script can be configured for multiple GPUs by running `accelerate config` from the command line; no further 
code-changes are required.

Training performance is quite sensitive to learning rate and number of epochs: you should tune these according to your task 
and the size of your dataset. In our experiments, we found the best performance to occur after 8 epochs of training
with a learning rate of 8e-5.

If you followed to the end of these steps: congratulations! You should now have a fine-tuned model you can use for your
downstream applications using the [inference code-example](#usage) above. You can try substituting your own dataset, or
run training using a single-speaker dataset, like the [Jenny example](https://colab.research.google.com/github/ylacombe/scripts_and_notebooks/blob/main/Finetuning_Parler_TTS_on_a_single_speaker_dataset.ipynb).

## Motivation

Parler-TTS is a reproduction of work from the paper [Natural language guidance of high-fidelity text-to-speech with synthetic annotations](https://www.text-description-to-speech.com) by Dan Lyth and Simon King, from Stability AI and Edinburgh University respectively. 

Contrarily to other TTS models, Parler-TTS is a **fully open-source** release. All datasets, pre-processing, training code and weights are released publicly under permissive license, enabling the community to build on our work and develop their own powerful TTS models.
Parler-TTS was released alongside:
* [The Parler-TTS repository](https://github.com/huggingface/parler-tts) - you can train and fine-tuned your own version of the model.
* [The Data-Speech repository](https://github.com/huggingface/dataspeech) - a suite of utility scripts designed to annotate speech datasets.
* [The Parler-TTS organization](https://huggingface.co/parler-tts) - where you can find the annotated datasets as well as the future checkpoints.

## Citation

If you found this repository useful, please consider citing this work and also the original Stability AI paper:

```
@misc{lacombe-etal-2024-parler-tts,
  author = {Yoach Lacombe and Vaibhav Srivastav and Sanchit Gandhi},
  title = {Parler-TTS},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/huggingface/parler-tts}}
}
```

```
@misc{lyth2024natural,
      title={Natural language guidance of high-fidelity text-to-speech with synthetic annotations},
      author={Dan Lyth and Simon King},
      year={2024},
      eprint={2402.01912},
      archivePrefix={arXiv},
      primaryClass={cs.SD}
}
```

## License

This model is permissively licensed under the Apache 2.0 license.
