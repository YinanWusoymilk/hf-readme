---
license: openrail
tags:
- stable diffusion
- controlnet
---

Can be used in [sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet). Put the yaml file with model because it is sd2.1 v_prediction model.

Model is the difference from the original checkpoint created by [extract_controlnet_diff.py](https://github.com/Mikubill/sd-webui-controlnet/blob/main/extract_controlnet_diff.py).

These are not the final version and need to be adjusted to be more accurate. Someone please do this.

# wd15_controlnet_edge_depth_pose.ckpt
+ target model: https://huggingface.co/waifu-diffusion/wd-1-5-beta2
+ dataset: 20k 1girl images
+ epoch: 5
+ batch size: 8
+ lr: 5e-5
+ amp:bfloat16

# diff_control_wd15beta2_canny.safetensors
**updated in 2023/03/05.**
+ target model: https://huggingface.co/waifu-diffusion/wd-1-5-beta2
+ dataset: 11k 1girl images
+ epoch: 2
+ batch size: 16
+ lr: 5e-5
+ amp:bfloat16

and resumed on:

+ dataset: 60k 1girl images
+ epoch: 2
+ batch size: 16
+ lr: 1e-5
+ amp:bfloat16

# diff_control_wd15beta2_pose.safetensors
**updated in 2023/03/06.**
+ target model: https://huggingface.co/waifu-diffusion/wd-1-5-beta2
+ dataset: 14k umamusume images. **Therefore, the model may have a bias**
+ epoch: 5 (The “sudden convergence phenomenon” occurred at the fourth epoch)
+ batch size: 16
+ lr: 5e-5
+ amp:bfloat16

and resumed on:

+ dataset: 52k 1girl images
+ epoch: 2
+ batch size: 16
+ lr: 1e-5
+ amp:bfloat16

# diff_control_wd15beta2_depth.safetensors
**updated in 2023/03/06.**
+ target model: https://huggingface.co/waifu-diffusion/wd-1-5-beta2
+ dataset: 11k 1girl images
+ epoch: 2
+ batch size: 16
+ lr: 5e-5
+ amp:bfloat16

and resumed on:

+ dataset: 60k 1girl images
+ epoch: 1
+ batch size: 16
+ lr: 1e-5
+ amp:bfloat16