---
library_name: transformers
tags:
- text-to-speech
license: cc-by-nc-sa-4.0
language:
- en
- zh
- ja
pipeline_tag: text-to-speech
inference: false
extra_gated_prompt: "You agree to not use the model to generate contents that violate DMCA or local laws."
extra_gated_fields:
  Country: country
  Specific date: date_picker
  I agree to use this model for non-commercial use ONLY: checkbox
---


# Fish Speech V1

<a target="_blank" href="https://huggingface.co/spaces/fishaudio/fish-speech-1">
  <img src="https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm.svg" alt="Open in HuggingFace"/>
</a>


**Fish Speech V1** is a leading text-to-speech (TTS) model trained on 150k hours of English, Chinese, and Japanese audio data. 

Please refer to [Fish Speech Github](https://github.com/fishaudio/fish-speech) for more info.  
Demo available at [Huggingface Spaces](https://huggingface.co/spaces/fishaudio/fish-speech-1) and [Fish Audio](https://fish.audio/text-to-speech/).

## Citation

If you found this repository useful, please consider citing this work:

```
@misc{fish-speech-v1,
  author = {Shijia Liao, Tianyu Li},
  title = {Fish Speech V1},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/fishaudio/fish-speech}}
}
```

## License

This model is permissively licensed under the BY-CC-NC-SA-4.0 license.
The source code is released under BSD-3-Clause license.