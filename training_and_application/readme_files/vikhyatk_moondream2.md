---
license: apache-2.0
pipeline_tag: image-text-to-text
---

moondream2 is a small vision language model designed to run efficiently on edge devices. Check out the [GitHub repository](https://github.com/vikhyat/moondream) for details, or try it out on the [Hugging Face Space](https://huggingface.co/spaces/vikhyatk/moondream2)!

**Benchmarks**

| Release | VQAv2 | GQA | TextVQA | DocVQA | TallyQA<br>(simple/full) | POPE<br>(rand/pop/adv) |
| --- | --- | --- | --- | --- | --- | --- |
| **2024-08-26** (latest) | 80.3 | 64.3 | 65.2 | 70.5 | 82.6 / 77.6 | 89.6 / 88.8 / 87.2 |
| 2024-07-23 | 79.4 | 64.9 | 60.2 | 61.9 | 82.0 / 76.8 | 91.3 / 89.7 / 86.9 |
| 2024-05-20 | 79.4 | 63.1 | 57.2 | 30.5 | 82.1 / 76.6 | 91.5 / 89.6 / 86.2 |
| 2024-05-08 | 79.0 | 62.7 | 53.1 | 30.5 | 81.6 / 76.1 | 90.6 / 88.3 / 85.0 |
| 2024-04-02 | 77.7 | 61.7 | 49.7 | 24.3 | 80.1 / 74.2 | - |
| 2024-03-13 | 76.8 | 60.6 | 46.4 | 22.2 | 79.6 / 73.3 | - |
| 2024-03-06 | 75.4 | 59.8 | 43.1 | 20.9 | 79.5 / 73.2 | - |
| 2024-03-04 | 74.2 | 58.5 | 36.4 | - | - | - |


**Usage**

```bash
pip install transformers einops
```

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

model_id = "vikhyatk/moondream2"
revision = "2024-08-26"
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision
)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

image = Image.open('<IMAGE_PATH>')
enc_image = model.encode_image(image)
print(model.answer_question(enc_image, "Describe this image.", tokenizer))
```

The model is updated regularly, so we recommend pinning the model version to a
specific release as shown above.
