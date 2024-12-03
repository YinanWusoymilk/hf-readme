---
license: openrail
datasets:
- KBlueLeaf/danbooru2023-sqlite
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- not-for-all-audiences
- art
widget:
- text: "rating: safe\nartist: <|empty|>\ncharacters: <|empty|>\ncopyrights: <|empty|>\naspect ratio: 1.0\ntarget: <|short|>\ngeneral: 1girl, solo, dragon girl, dragon horns, dragon tail<|input_end|>"
---

# DanTagGen - alpha
DanTagGen(Danbooru Tag Generator) is inspired from p1atdev's dart project.
But with different arch, dataset, format and different training strategy.

## Model arch
This version of DTG is trained from scratch with 400M param LLaMA arch.(In my personal preference I will call it NanoLLaMA)
Since it is llama arch. Theoritically it should be able to be used in any LLaMA inference interface.

This repo also provided converted FP16 gguf model and quantized 8bit/6bit gguf models.
Basically it is recommended to use llama.cpp or llama-cpp-python to run this model. Which will be very fast.

## Format
```python3
prompt = f"""
rating: {rating or '<|empty|>'}
artist: {artist.strip() or '<|empty|>'}
characters: {characters.strip() or '<|empty|>'}
copyrights: {copyrights.strip() or '<|empty|>'}
aspect ratio: {f"{aspect_ratio:.1f}" or '<|empty|>'}
target: {'<|' + target + '|>' if target else '<|long|>'}
general: {", ".join(special_tags)}, {general.strip().strip(",")}<|input_end|>
"""
```

for example:
```
rating: safe
artist: <|empty|>
characters: <|empty|>
copyrights: <|empty|>
aspect ratio: 1.0
target: <|short|>
general: 1girl, solo, dragon girl, dragon horns, dragon tail<|input_end|>
```

And you may get something like:
```
rating: safe
artist: <|empty|>
characters: <|empty|>
copyrights: <|empty|>
aspect ratio: 1.0
target: <|short|>
general: 1girl, solo, dragon girl, dragon horns, dragon tail<|input_end|>open mouth, red eyes, long hair, pointy ears, tail, black hair, chinese clothes, simple background, dragon, hair between eyes, horns, china dress, dress, looking at viewer, breasts
```

## Dataset and Training
I use the trainer I implemented in HakuPhi to run the training. (It should be HakuLLM now LoL)
with 15epoch on 2M data and 5epoch on 5.3M data. This model have roughly 6~12B token seen.

The dataset is exported by HakuBooru with my danbooru sqlite database. Use the percentile of fav_count on each rating to filter the data. (2M = top 25%, 5.3M = top 75%)

## Utilities
I'm implementing a gradio UI for this thing and other dev can utilize the API in it to make different app.
I'm also planning to make sd-webui extension.