---
license: apache-2.0
inference: false
datasets:
  - Lin-Chen/ShareGPT4V
  - ShareGPT4Video/ShareGPT4Video
pipeline_tag: visual-question-answering
---
<br>
<br>

# sharegpt4video-8b Model Card

## Model details

**Model type:**
sharegpt4video-8b is an open-source video chatbot trained by fine-tuning the entire model on open-source [video instruction data](https://huggingface.co/datasets/ShareGPT4Video/ShareGPT4Video). The training process takes around 5 hour on 32xA100 GPUs.

**Model date:**
sharegpt4video-8b was trained in May 2024.

**Paper or resources for more information:**
[[Code](https://github.com/ShareGPT4Omni/ShareGPT4Video)] [[Project Page](https://sharegpt4video.github.io/)]

## Usage

You can utilize this model as we provide in our [[repository](https://github.com/ShareGPT4Omni/ShareGPT4Video)].

## Training dataset

All training data are open-sourced, you can find the usage in our [repository](https://github.com/ShareGPT4Omni/ShareGPT4Video).

- 153K collection of various video instruction data
- 28K high-quality video caption data from [[ShareGPT4Video](https://huggingface.co/datasets/ShareGPT4Video/ShareGPT4Video)]

## Intended use

**Primary intended uses:**
The primary use of sharegpt4video-8b is research on large video-language models and video chatbots.

**Primary intended users:**
The primary intended users of the model are researchers and hobbyists in computer vision, natural language processing, machine learning, and artificial intelligence.

## Paper 
arxiv.org/abs/2406.04325
