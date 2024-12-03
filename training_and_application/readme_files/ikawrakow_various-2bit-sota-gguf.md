---
license: apache-2.0
---
Various models in GGUF format quantized with a new 2-bit approach. Intended for use with llama.cpp. Requires llama.cpp PR 4773.

Update: PR 4773 has been merged into `llama.cpp`, but I have added new models that require PR 4856.
The new models are those that have around 2.3-2.4 bpw. They have a lower quantization error at the xpense of being ~10% larger.