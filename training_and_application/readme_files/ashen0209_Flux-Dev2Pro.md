---
license: apache-2.0
library_name: diffusers
pipeline_tag: text-to-image
---

## Flux-Dev2Pro

Flux-Dev2Pro finetunes the transformer of Flux-Dev to make LoRA training better.

As discussed in this blog https://medium.com/@zhiwangshi28/why-flux-lora-so-hard-to-train-and-how-to-overcome-it-a0c70bc59eaf, LoRA trained on Flux-Dev often yields bad results, because without guidance distillation the LoRA training is diverged from the original training process. Flux-Dev2Pro recovers Flux-pro from Flux-dev by finetuning the model for many steps. Two epoch of 3M high quality images have been trained.

The LoRA trained on Flux-Dev2pro yields a much better results when being applied on Flux-dev, just like LoRA trained on SDXL and being applied to SDXL-turbo/lightning.


To use this model, run:
```python
from diffusers import FluxTransformer2DModel

transformer = FluxTransformer2DModel.from_pretrained("ashen0209/Flux-Dev2Pro", torch_dtype=torch.bfloat16)
```

