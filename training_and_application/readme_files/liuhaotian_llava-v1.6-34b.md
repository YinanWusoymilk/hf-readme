---
inference: false
license: apache-2.0
library_name: LLaVA
pipeline_tag: image-text-to-text
tags:
- llava
---

<br>
<br>

# LLaVA Model Card

## Model details

**Model type:**
LLaVA is an open-source chatbot trained by fine-tuning LLM on multimodal instruction-following data.
It is an auto-regressive language model, based on the transformer architecture.
Base LLM: [NousResearch/Nous-Hermes-2-Yi-34B](https://huggingface.co/NousResearch/Nous-Hermes-2-Yi-34B)

**Model date:**
LLaVA-v1.6-34B was trained in December 2023.

**Paper or resources for more information:**
https://llava-vl.github.io/

## License
[NousResearch/Nous-Hermes-2-Yi-34B](https://huggingface.co/NousResearch/Nous-Hermes-2-Yi-34B) license.

**Where to send questions or comments about the model:**
https://github.com/haotian-liu/LLaVA/issues

## Intended use
**Primary intended uses:**
The primary use of LLaVA is research on large multimodal models and chatbots.

**Primary intended users:**
The primary intended users of the model are researchers and hobbyists in computer vision, natural language processing, machine learning, and artificial intelligence.

## Training dataset
- 558K filtered image-text pairs from LAION/CC/SBU, captioned by BLIP.
- 158K GPT-generated multimodal instruction-following data.
- 500K academic-task-oriented VQA data mixture.
- 50K GPT-4V data mixture.
- 40K ShareGPT data.

## Evaluation dataset
A collection of 12 benchmarks, including 5 academic VQA benchmarks and 7 recent benchmarks specifically proposed for instruction-following LMMs.