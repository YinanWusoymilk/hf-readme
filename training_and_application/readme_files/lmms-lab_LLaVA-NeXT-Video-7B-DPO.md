---
inference: false
license: llama2
pipeline_tag: video-text-to-text
---

<br>

# LLaVA-Next-Video Model Card

## Model details

**Model type:**
<br>
LLaVA-Next-Video is an open-source chatbot trained by fine-tuning LLM on multimodal instruction-following data.
<br>
 Base LLM: lmsys/vicuna-7b-v1.5

**Model date:**
<br>
LLaVA-Next-Video-7B-DPO was trained in April 2024.

**Paper or resources for more information:**
<br>
https://github.com/LLaVA-VL/LLaVA-NeXT

## License
Llama 2 is licensed under the LLAMA 2 Community License, 
Copyright (c) Meta Platforms, Inc. All Rights Reserved.

## Where to send questions or comments about the model
https://github.com/LLaVA-VL/LLaVA-NeXT/issues

## Intended use
**Primary intended uses:**
<br>
The primary use of LLaVA is research on large multimodal models and chatbots.

**Primary intended users:**
<br>
The primary intended users of the model are researchers and hobbyists in computer vision, natural language processing, machine learning, and artificial intelligence.

## Training dataset

### Image
- 558K filtered image-text pairs from LAION/CC/SBU, captioned by BLIP.
- 158K GPT-generated multimodal instruction-following data.
- 500K academic-task-oriented VQA data mixture.
- 50K GPT-4V data mixture.
- 40K ShareGPT data.
### Video
- 100K VideoChatGPT-Instruct.
- 17k video preference data: https://huggingface.co/datasets/ShareGPTVideo/train_video_and_instruction

## Evaluation dataset
A collection of 4 benchmarks, including 3 academic VQA benchmarks and 1 captioning benchmark.