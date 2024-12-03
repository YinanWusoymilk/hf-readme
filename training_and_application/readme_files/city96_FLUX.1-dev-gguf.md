---
base_model: black-forest-labs/FLUX.1-dev
library_name: gguf
license: other
license_name: flux-1-dev-non-commercial-license
license_link: LICENSE.md
quantized_by: city96
tags:
- text-to-image
- image-generation
- flux
---

This is a direct GGUF conversion of [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main)

As this is a quantized model not a finetune, all the same restrictions/original license terms still apply.

The model files can be used with the [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF) custom node.

Place model files in `ComfyUI/models/unet` - see the GitHub readme for further install instructions.

Please refer to [this chart](https://github.com/ggerganov/llama.cpp/blob/master/examples/perplexity/README.md#llama-3-8b-scoreboard) for a basic overview of quantization types.
