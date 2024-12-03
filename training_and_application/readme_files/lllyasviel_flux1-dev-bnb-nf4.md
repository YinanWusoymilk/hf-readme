---
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
---

Main page: https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/981

---

Update:

Always use V2 by default. 

V2 is quantized in a better way to turn off the second stage of double quant. 

V2 is 0.5 GB larger than the previous version, since the chunk 64 norm is now stored in full precision float32, making it much more precise than the previous version. Also, since V2 does not have second compression stage, it now has less computation overhead for on-the-fly decompression, making the inference a bit faster.

The only drawback of V2 is being 0.5 GB larger.

---

Main model in bnb-nf4 (v1 with chunk 64 norm in nf4, v2 with chunk 64 norm in float32)

T5xxl in fp8e4m3fn

CLIP-L in fp16

VAE in bf16


