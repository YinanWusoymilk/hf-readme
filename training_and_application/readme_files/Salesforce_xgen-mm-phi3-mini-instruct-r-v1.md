---
license: cc-by-nc-4.0
language:
- en
pipeline_tag: image-text-to-text
---

# 📣 News
📌 [08/19/2024] xGen-MM-v1.5 released:
  - [🤗 xgen-mm-phi3-mini-instruct-interleave-r-v1.5](https://huggingface.co/Salesforce/xgen-mm-phi3-mini-instruct-interleave-r-v1.5)
  - [🤗 xgen-mm-phi3-mini-base-r-v1.5](https://huggingface.co/Salesforce/xgen-mm-phi3-mini-base-r-v1.5)
  - [🤗 xgen-mm-phi3-mini-instruct-singleimg-r-v1.5](https://huggingface.co/Salesforce/xgen-mm-phi3-mini-instruct-singleimg-r-v1.5)
  - [🤗 xgen-mm-phi3-mini-instruct-dpo-r-v1.5](https://huggingface.co/Salesforce/xgen-mm-phi3-mini-instruct-dpo-r-v1.5)

# Model description
We are excited to announce the continuation and rebranding of our **BLIP series** into **XGen-MM**, to be better aligned with Salesforce's unified XGen initiative for large foundation models! This rebranding marks a significant step in our ongoing development of cutting-edge multimodal technologies.

`XGen-MM` is a series of the latest foundational Large Multimodal Models (LMMs) developed by Salesforce AI Research. This series advances upon the successful designs of the `BLIP` series, incorporating fundamental enhancements that ensure a more robust and superior foundation. \
These models have been trained at scale on high-quality image caption datasets and interleaved image-text data. XGen-MM highlights a few features below,

* The **pretrained** foundation model, `xgen-mm-phi3-mini-base-r-v1`, achieves state-of-the-art performance under 5b parameters and demonstrates strong in-context learning capabilities.
* The **instruct** fine-tuned model, `xgen-mm-phi3-mini-instruct-r-v1`, achieves state-of-the-art performance among open-source and closed-source VLMs under 5b parameters. 
* `xgen-mm-phi3-mini-instruct-r-v1` supports flexible high-resolution image encoding with efficient visual token sampling.  

More technical details will come with a technical report soon.


# Results

### Pretrain (base model without instruction tuning)
| Model       | Shot | COCO (val) | NoCaps (val) | TextCaps (val) | OKVQA  (val) | TextVQA (val) | VizWiz (testdev) | VQAv2 (testdev) |
|-------------|------|------------|--------------|----------------|--------------|---------------|------------------|-----------------|
| Flamingo-3B |    4 |       85.0 | -            | -              |         43.3 |          32.7 |               34 |            53.2 |
|             |    8 |       90.6 | -            | -              |         44.6 |          32.4 |             38.4 |            55.4 |
| MM1-3B      |    0 |       73.5 |         55.6 |           63.3 |         26.1 |          29.4 |             15.6 |            46.2 |
|             |    4 |      112.3 |         99.7 |           84.1 |         48.6 |          45.3 |             38.0 |            57.9 |
|             |    8 |      114.6 |        104.7 |           88.8 |         48.4 |          44.6 |             46.4 |            63.6 |
| **xgen-mm-phi3-mini-base-r-v1 (Ours)**|    0 |       **81.7** |         **80.2** |           60.7 |         **26.5** |          **36.0** |             **21.2** |            **48.1** |
|             |    4 |      110.5 |        **101.7** |           **84.6** |         **49.2** |          **46.1** |             **38.4** |            **63.9** |
|             |    8 |      112.1 |        104.4 |           87.7 |         **49.1** |          **46.4** |             44.3 |            **63.8** |

### Instruct (after instruction tuning)
| Model                      | SEED-IMG | MMBench(dev) | MME-total | MME-P    | MME-C   | MMStar   | MMMU (val) | MMVet    | MathVista (mini) | ScienceQA (test) | POPE      | AI2D     |   |
|----------------------------|----------|--------------|-----------|----------|---------|----------|------------|----------|------------------|------------------|----------|----------|---|
| MM1-3B-Chat                | 68.8     | 67.8         | 1761      | **1482**     | 279     | -        | 33.9       | 43.7     | -                | -                | **87.4**            | -        |   |
| openbmb/MiniCPM-V-2        | 67.1     | 69.6         | 1808      | -        | -       | -        | 38.2       | -        | 38.7             | -                | -         | -        |   |
| VILA1.5-3B                 | 67.9     | 63.4         | -         | 1442     | -       | -        | 33.3       | 35.4     | -                | 69.0             | 85.9       | -        |   |
| xtuner/llava-phi-3-mini-hf | 70.0     | 69.2         | 1790      | 1477     | 313     | 43.7     | **41.4**       | -        | -                | 73.7             | 87.3       | 69.3     |   |
| **xgen-mm-phi3-mini-instruct-r-v1 (Ours)** | **72.1**     | **74.1**         | **1827**      | 1467     | **360**     | **44.6**     | 39.8       | **45.1**     | **39.3**             | **74.2**             | 87.2       | **75.8**     |   |


# How to use

~~> We require the use of the development version (`"4.41.0.dev0"`) of the `transformers` library. To get it, as of 05/07/2024, one can use `pip uninstall -y transformers && pip install git+https://github.com/huggingface/transformers.`~~

```python
from transformers import AutoModelForVision2Seq, AutoTokenizer, AutoImageProcessor, StoppingCriteria
import torch
import requests
from PIL import Image

# define the prompt template
def apply_prompt_template(prompt):
    s = (
            '<|system|>\nA chat between a curious user and an artificial intelligence assistant. '
            "The assistant gives helpful, detailed, and polite answers to the user's questions.<|end|>\n"
            f'<|user|>\n<image>\n{prompt}<|end|>\n<|assistant|>\n'
        )
    return s 
class EosListStoppingCriteria(StoppingCriteria):
    def __init__(self, eos_sequence = [32007]):
        self.eos_sequence = eos_sequence

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        last_ids = input_ids[:,-len(self.eos_sequence):].tolist()
        return self.eos_sequence in last_ids      

# load models
model_name_or_path = "Salesforce/xgen-mm-phi3-mini-instruct-r-v1"
model = AutoModelForVision2Seq.from_pretrained(model_name_or_path, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True, use_fast=False, legacy=False)
image_processor = AutoImageProcessor.from_pretrained(model_name_or_path, trust_remote_code=True)
tokenizer = model.update_special_tokens(tokenizer)

# craft a test sample
img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg'
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')
query = "how many dogs are in the picture?"

model = model.cuda()
inputs = image_processor([raw_image], return_tensors="pt", image_aspect_ratio='anyres')
prompt = apply_prompt_template(query)
language_inputs = tokenizer([prompt], return_tensors="pt")
inputs.update(language_inputs)
inputs = {name: tensor.cuda() for name, tensor in inputs.items()}
generated_text = model.generate(**inputs, image_size=[raw_image.size],
                                pad_token_id=tokenizer.pad_token_id,
                                do_sample=False, max_new_tokens=768, top_p=None, num_beams=1,
                                stopping_criteria = [EosListStoppingCriteria()],
                                )
prediction = tokenizer.decode(generated_text[0], skip_special_tokens=True).split("<|end|>")[0]
print("==> prediction: ", prediction)
# output: ==> prediction: There is one dog in the picture.
```

More comprehensive examples can be found in the [notebook](demo.ipynb).

# Reproducibility: 

Our SFT evaluation is based on the VLMEvalKit, in which we fixed some inconsistencies with the official benchmarks (e.g., LLM judge API). During our development, we noticed that the raw resolution of the input image would noticeably affect the model output in some cases.


# Bias, Risks, Limitations, and Ethical Considerations
The main data sources are from the internet, including webpages, 
image stock sites, and curated datasets released by the research community. We have excluded certain data, such as LAION, due to known CSAM concerns.
The model may be subject to bias from the original data source, as well as bias from LLMs and commercial APIs. 
We strongly recommend users assess safety and fairness before applying to downstream applications. 


# License

Our code and weights are released under the Creative Commons Attribution Non Commercial 4.0 [LICENSE](LICENSE.txt). Please fill out a form at [here](https://forms.gle/ffPc9oZC2ZGeJ1N68) to consult the commercial use of model weights.

# Code acknowledgment

[LAVIS](https://github.com/salesforce/LAVIS) \
[openflamingo](https://github.com/mlfoundations/open_flamingo) \
[VLMEvalKit](https://github.com/open-compass/VLMEvalKit/tree/main)


# Citation
```
@misc{xue2024xgenmmblip3familyopen,
      title={xGen-MM (BLIP-3): A Family of Open Large Multimodal Models}, 
      author={Le Xue and Manli Shu and Anas Awadalla and Jun Wang and An Yan and Senthil Purushwalkam and Honglu Zhou and Viraj Prabhu and Yutong Dai and Michael S Ryoo and Shrikant Kendre and Jieyu Zhang and Can Qin and Shu Zhang and Chia-Chih Chen and Ning Yu and Juntao Tan and Tulika Manoj Awalgaonkar and Shelby Heinecke and Huan Wang and Yejin Choi and Ludwig Schmidt and Zeyuan Chen and Silvio Savarese and Juan Carlos Niebles and Caiming Xiong and Ran Xu},
      year={2024},
      eprint={2408.08872},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2408.08872}, 
}
```

# Troubleshoot

1. If you missed any packages, please consider the following

```
pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cu121
pip install open_clip_torch==2.24.0
pip install einops
pip install einops-exts
pip install transformers==4.41.1
```

# Changelog

* 05/24/2024
    * update codebase to be compatible with `transformers==4.41.1`.