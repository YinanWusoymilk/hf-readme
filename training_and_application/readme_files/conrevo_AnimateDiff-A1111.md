# AnimateDiff Model Checkpoints for A1111 SD WebUI
This repository saves all AnimateDiff models in fp16 & safetensors format for A1111 AnimateDiff users, including
- motion module (v1-v3)
- [motion LoRA](#motion-lora) (v2 only, use like any other LoRA)
- domain adapter (v3 only, use like any other LoRA)
- [sparse ControlNet](#sparse-controlnet) (v3 only, use like any other ControlNet)

Unless specified below, you are fine to use models from the [official model repository](https://huggingface.co/guoyww/animatediff/tree/main). I will only convert state dict keys if absolutely necessary.


## Motion LoRA
Put Motion LoRAs to `stable-diffusion-webui/models/Lora` and use Motion LoRAs like any other LoRA you use.

[lora_v2](https://huggingface.co/conrevo/AnimateDiff-A1111/tree/main/lora_v2) contains motion LoRAs for AnimateDiff-A1111 v2.0.0 and later. I converted state dict keys inside motion LoRAs. Originlal motion LoRAs won't work for AnimateDiff-A1111 v2.0.0 and later due to maintenance reason.

Use [convert.py](convert.py) in the following way if you want to convert a third-party motion LoRA to be compatible with A1111:
- Activate your A1111 Python environment first.
- Command: `python script.py lora [file_path] [save_path]`
- Replace `[file_path]` with the path to your old LoRA checkpoint.
- Replace `[save_path]` with the path where you want to save the new LoRA checkpoint.


## Sparse ControlNet
Put Sparse ControlNets to `stable-diffusion-webui/models/ControlNet` and use Sparse ControlNets like any other ControlNet you use.

Like Motion LoRA, I converted state dict keys inside sparse ControlNet. Original sparse ControlNets won't work for A1111 due to maintenance reason.

Use [convert.py](convert.py) in the following way if you want to convert a third-party sparse ControlNet to be compatible with A1111:
- Activate your A1111 Python environment first.
- Command: `python script.py controlnet [ad_cn_old] [ad_cn_new] [normal_cn_path]`
- Replace `[ad_cn_old]` with the path to your old sparse ControlNet checkpoint.
- Replace `[ad_cn_new]` with the path where you want to save the new sparse ControlNet checkpoint.
- Replace `[normal_cn_path]` with the path to the normal ControlNet model. Download normal ControlNet from [here](https://huggingface.co/lllyasviel/control_v11p_sd15_openpose/resolve/main/diffusion_pytorch_model.fp16.safetensors?download=true).


## HotShotXL
You need to use HotShotXL in this repository if you want to use it for AnimateDiff-A1111 v2.0.0 and later. Like Motion LoRA, I converted state dict keys inside HotShotXL. Original HotShotXL won't work for AnimateDiff-A1111 v2.0.0 and later due to maintenance reason.
