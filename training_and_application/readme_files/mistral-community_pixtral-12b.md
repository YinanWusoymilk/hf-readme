---
library_name: transformers
pipeline_tag: image-text-to-text
---

# Model Card for Model ID
Transformers compatible pixtral checkpoints. Make sure to install from source or wait for v4.45! 

```python
from PIL import Image
from transformers import AutoProcessor, LlavaForConditionalGeneration
model_id = "mistral-community/pixtral-12b"
model = LlavaForConditionalGeneration.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id)

IMG_URLS = [
"https://picsum.photos/id/237/400/300", 
"https://picsum.photos/id/231/200/300", 
"https://picsum.photos/id/27/500/500",
"https://picsum.photos/id/17/150/600",
]
PROMPT = "<s>[INST]Describe the images.\n[IMG][IMG][IMG][IMG][/INST]"

inputs = processor(text=PROMPT, images=IMG_URLS, return_tensors="pt").to("cuda")
generate_ids = model.generate(**inputs, max_new_tokens=500)
output = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
```

You should get an output similar to the below:
```

"""
Describe the images.
Sure, let's break down each image description:

1. **Image 1:**
   - **Description:** A black dog with a glossy coat is sitting on a wooden floor. The dog has a focused expression and is looking directly at the camera.
   - **Details:** The wooden floor has a rustic appearance with visible wood grain patterns. The dog's eyes are a striking color, possibly brown or amber, which contrasts with its black fur.

2. **Image 2:**
   - **Description:** A scenic view of a mountainous landscape with a winding road cutting through it. The road is surrounded by lush green vegetation and leads to a distant valley.
   - **Details:** The mountains are rugged with steep slopes, and the sky is clear, indicating good weather. The winding road adds a sense of depth and perspective to the image.

3. **Image 3:**
   - **Description:** A beach scene with waves crashing against the shore. There are several people in the water and on the beach, enjoying the waves and the sunset.
   - **Details:** The waves are powerful, creating a dynamic and lively atmosphere. The sky is painted with hues of orange and pink from the setting sun, adding a warm glow to the scene.

4. **Image 4:**
   - **Description:** A garden path leading to a large tree with a bench underneath it. The path is bordered by well-maintained grass and flowers.
   - **Details:** The path is made of small stones or gravel, and the tree provides a shaded area with the bench invitingly placed beneath it. The surrounding area is lush and green, suggesting a well-kept garden.

Each image captures a different scene, from a close-up of a dog to expansive natural landscapes, showcasing various elements of nature and human interaction with it.
"""
```

You can also use a chat template to format your chat history for Pixtral. Make sure that the `images` argument to the `processor` contains the images in the order
that they appear in the chat, so that the model understands where each image is supposed to go.

Here's an example with text and multiple images interleaved in the same message:

```python
from PIL import Image
from transformers import AutoProcessor, LlavaForConditionalGeneration
model_id = "mistral-community/pixtral-12b"
model = LlavaForConditionalGeneration.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id)

url_dog = "https://picsum.photos/id/237/200/300"
url_mountain = "https://picsum.photos/seed/picsum/200/300"

chat = [
    {
      "role": "user", "content": [
        {"type": "text", "content": "Can this animal"}, 
        {"type": "image"}, 
        {"type": "text", "content": "live here?"}, 
        {"type": "image"}
      ]
    }
]

prompt = processor.apply_chat_template(chat)
inputs = processor(text=prompt, images=[url_dog, url_mountain], return_tensors="pt").to(model.device)
generate_ids = model.generate(**inputs, max_new_tokens=500)
output = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
```

You should get something like this:

```
Can this animallive here?Certainly! Here are some details about the images you provided:

### First Image
- **Description**: The image shows a black dog lying on a wooden surface. The dog has a curious expression with its head tilted slightly to one side.
- **Details**: The dog appears to be a young puppy with soft, shiny fur. Its eyes are wide and alert, and it has a playful demeanor.
- **Context**: This image could be used to illustrate a pet-friendly environment or to showcase the dog's personality.

### Second Image
- **Description**: The image depicts a serene landscape with a snow-covered hill in the foreground. The sky is painted with soft hues of pink, orange, and purple, indicating a sunrise or sunset.
- **Details**: The hill is covered in a blanket of pristine white snow, and the horizon meets the sky in a gentle curve. The scene is calm and peaceful.
- **Context**: This image could be used to represent tranquility, natural beauty, or a winter wonderland.

### Combined Context
If you're asking whether the dog can "live here," referring to the snowy landscape, it would depend on the breed and its tolerance to cold weather. Some breeds, like Huskies or Saint Bernards, are well-adapted to cold environments, while others might struggle. The dog in the first image appears to be a breed that might prefer warmer climates.

Would you like more information on any specific aspect?
```

While it may appear that spacing in the input is disrupted, this is caused by us skipping special tokens for display, and actually "Can this animal" and "live here" are
correctly separated by image tokens. Try decoding with special tokens included to see exactly what the model sees!

