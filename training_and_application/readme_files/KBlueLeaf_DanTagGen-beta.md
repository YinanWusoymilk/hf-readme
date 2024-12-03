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

# DanTagGen - beta
DanTagGen(Danbooru Tag Generator) is inspired from p1atdev's dart project.
But with different arch, dataset, format and different training strategy.

## Difference between versions
alpha: pretrain on 2M dataset, smaller batch size. Limited ability
beta: pretrain on 5.3M dataset, larger batch size. More stable, better ability with only a few information provided.

## Examples

### Example1: Vivlos
Base prompt:
```
1girl,
vivlos \(umamusume\), umamusume, 
kxl-delta-style1,
swimsuit,
masterpiece, newest, absurdres, sensitive
```
||Without DTG|DTG-Alpha|DTG-Beta|
|-|-|-|-|
|Prompts|Base prompt|Base propmt + "mole under eye, tail, twintails, open mouth, single ear cover, horse ears, breasts, looking at viewer, visor cap, streaked hair, long hair, horse tail, hair between eyes, cowboy shot, blue nails, purple eyes, covered navel, horse girl, competition swimsuit, blush, multicolored hair, collarbone, two-tone swimsuit, animal ears, mole, white hair, ear covers, smile, ear ornament, swimsuit, solo, blue eyes, brown hair, one-piece swimsuit, white headwear, medium breasts, white one-piece swimsuit, bare shoulders,"| base propmt + "blue bikini, tail, twintails, single ear cover, horse ears, striped clothes, ear piercing, cleavage, breasts, blue ribbon, looking at viewer, ribbon, streaked hair, long hair, horse tail, hair between eyes, :3, purple eyes, horse girl, blush, multicolored hair, hair ribbon, collarbone, bikini skirt, piercing, animal ears, striped bikini, sitting, white hair, ear covers, :d, smile, swimsuit, solo, brown hair, ocean, white headwear, medium breasts, bikini,"|
|Result image|![image/png](https://cdn-uploads.huggingface.co/production/uploads/630593e2fca1d8d92b81d2a1/Gwxj16J5wJ0pY1iYWQLtA.png)|![image/png](https://cdn-uploads.huggingface.co/production/uploads/630593e2fca1d8d92b81d2a1/LP3Jxy5rYxo97_03mzxSv.png)|![image/png](https://cdn-uploads.huggingface.co/production/uploads/630593e2fca1d8d92b81d2a1/Bv5vTwXxTzwni9U3a7Yc2.png)|
|Performance|It can't even generate vivlos|It can generate image with correct character features but not enough detail and some features are wrong/lacked |Way better than alpha, provide good character features, also provide lot more details and better composition|





### Example2: Daring Tact
Base prompt:
```
1girl,
daring tact \(umamusume\), umamusume, 
kxl-delta-style1,
horse girl, horse tail, horse ears, cafe, table, chair,
masterpiece, newest, absurdres, safe
```
||Without DTG|DTG-Alpha|DTG-Beta|
|-|-|-|-|
|Prompts|Base prompt|Base propmt + "plant, necktie, tail, indoors, skirt, looking at viewer, cup, lounge chair, green theme, book, alternate costume, potted plant, hair ornament, blue jacket, blush, medium hair, black necktie, green eyes, jacket, animal ears, black hair, round eyewear, bookshelf, adjusting eyewear, ahoge, smile, solo, window, brown hair, crossed legs, glasses, closed mouth, book stack,"| base propmt + "jacket, sitting on table, food, tail, collar, horse racing, black hair, boots, school bag, bag, full body, blue eyes, hair ornament, animal ears, ahoge, sitting, thighhighs, blurry background, looking at viewer, school uniform, long hair, blurry, cup, window, crossed legs, alternate costume, medium breasts, breasts, calendar \(object\), casual, door, solo, disposable cup,"|
|Result image|![image/png](https://cdn-uploads.huggingface.co/production/uploads/630593e2fca1d8d92b81d2a1/6ILQlisS605o9RYUz7pUn.png)|![image/png](https://cdn-uploads.huggingface.co/production/uploads/630593e2fca1d8d92b81d2a1/_n7lHYfiEJE_AJu-14NKX.png)|![image/png](https://cdn-uploads.huggingface.co/production/uploads/630593e2fca1d8d92b81d2a1/3JyItAt-wbKUu1krBJpGc.png)|
|Performance| |It can generate image with more elements and details, but the coherence with character is not good|Way better than alpha, also provide lot more details and better composition|


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
I use the trainer I implemented in HakuPhi to run the training.
with 10epoch on 5.3M data. This model have roughly 6~12B token seen.

The dataset is exported by HakuBooru with my danbooru sqlite database. Use the percentile of fav_count on each rating to filter the data. (2M = top 25%, 5.3M = top 75%)

## Utilities
I'm implementing a gradio UI for this thing and other dev can utilize the API in it to make different app.
I'm also planning to make sd-webui extension.