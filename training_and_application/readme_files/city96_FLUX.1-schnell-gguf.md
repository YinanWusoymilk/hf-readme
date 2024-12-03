---
base_model: black-forest-labs/FLUX.1-schnell
library_name: gguf
license: apache-2.0
quantized_by: city96
tags:
- text-to-image
- image-generation
- flux
---

This is a direct GGUF conversion of [black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell)

The model files can be used with the [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF) custom node.

Place model files in `ComfyUI/models/unet` - see the GitHub readme for further install instructions.

Please refer to [this chart](https://github.com/ggerganov/llama.cpp/blob/master/examples/perplexity/README.md#llama-3-8b-scoreboard) for a basic overview of quantization types.