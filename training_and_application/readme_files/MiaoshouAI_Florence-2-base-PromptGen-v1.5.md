---
license: mit
---
# Florence-2-base-PromptGen v1.5
This is a major version upgrade for PromptGen. In this new version, two new caption instructions are added: \<GENERATE_TAGS\> and \<MIXED_CAPTION\>
You'll also notice significantly improved accuracy with this version, thanks to a new training dataset. It no longer relies on Civitai Data, avoiding the issues of lora trigger words and inaccurate tags from misinterpretation.

# About PromptGen
Florence-2-base-PromptGen is a model trained for [MiaoshouAI Tagger for ComfyUI](https://github.com/miaoshouai/ComfyUI-Miaoshouai-Tagger).
It is an advanced image captioning tool based on the [Microsoft Florence-2 Model Base](https://huggingface.co/microsoft/Florence-2-base) and fine-tuned to perfection.

## Why another tagging model?
Most vision models today are trained mainly for general vision recognition purposes, but when doing prompting and image tagging for model training, the format and details of the captions is quite different.
Florence-2-base-PromptGen is trained on such a purpose as aiming to improve the tagging experience and accuracy of the prompt and tagging job. The model is trained based on images and cleaned tags from Civitai so that the end result for tagging the images are the prompts you use to generate these images.
You won't get annoying captions like "This is image is about a girl..." or 

## Features:
* Describes image in much detail when using \<MORE_DETAILED_CAPTION\> instruction.
  <img style="width:100%; hight:100%" src="https://msdn.miaoshouai.com/miaoshou/bo/2024-09-05_12-40-34.png" />
* When using \<DETAILED_CAPTION\> instruction, it creates a structured caption with infomation on subject's position and also reads the text from the image, which can be super useful when recreate a scene.
  <img style="width:100%; hight:100%" src="https://msdn.miaoshouai.com/miaoshou/bo/2024-09-05_13-07-54.png" />
* Memory efficient compare to other models! This is a really light weight caption model that allows you to use a little more than 1G of VRAM and produce lightening fast and high quality image captions.
  <img style="width:100%; hight:100%" src="https://msdn.miaoshouai.com/miaoshou/bo/2024-09-05_12-56-39.png" />
* Designed to handle image captions for Flux model for both T5XXL CLIP and CLIP_L, the Miaoshou Tagger new node called "Flux CLIP Text Encode" which eliminates the need to run two separate tagger tools for caption creation. You can easily populate both CLIPs in a single generation, significantly boosting speed when working with Flux models.
  <img style="width:100%; hight:100%" src="https://msdn.miaoshouai.com/miaoshou/bo/2024-09-05_14-11-02.png" />
  
## Instruction prompt:
\<GENERATE_TAGS\> generate prompt as danbooru style tags<br>
\<CAPTION\> a one line caption for the image<br>
\<DETAILED_CAPTION\> a structured caption format which detects the position of the subjects in the image<br>
\<MORE_DETAILED_CAPTION\> a very detailed description for the image<br>
\<MIXED_CAPTION\> a mixed caption style of more detailed caption and tags, this is extremely useful for FLUX model when using T5XXL and CLIP_L together. A new node in MiaoshouTagger ComfyUI is added to support this instruction.<br>

## Version History:
For version 1.5, you will notice the following
1. \<GENERATE_PROMPT\> is deprecated and replace by \<GENERATE_TAGS\>
2. A new instruction for \<MIXED_CAPTION\>
3. A much improve accuracy for \<DETAILED_CAPTION\> and \<MORE_DETAILED_CAPTION\>
4. Improved ability for recognizing watermarks on images.


## How to use:

To use this model, you can load it directly from the Hugging Face Model Hub:

```python

model = AutoModelForCausalLM.from_pretrained("MiaoshouAI/Florence-2-base-PromptGen-v1.5", trust_remote_code=True)
processor = AutoProcessor.from_pretrained("MiaoshouAI/Florence-2-base-PromptGen-v1.5", trust_remote_code=True)

prompt = "<MORE_DETAILED_CAPTION>"

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(text=prompt, images=image, return_tensors="pt").to(device)

generated_ids = model.generate(
    input_ids=inputs["input_ids"],
    pixel_values=inputs["pixel_values"],
    max_new_tokens=1024,
    do_sample=False,
    num_beams=3
)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]

parsed_answer = processor.post_process_generation(generated_text, task=prompt, image_size=(image.width, image.height))

print(parsed_answer)
```

## Use under MiaoshouAI Tagger ComfyUI
If you just want to use this model, you can use it under ComfyUI-Miaoshouai-Tagger

https://github.com/miaoshouai/ComfyUI-Miaoshouai-Tagger

A detailed use and install instruction is already there.
(If you have already installed MiaoshouAI Tagger, you need to update the node in ComfyUI Manager first or use git pull to get the latest update.)