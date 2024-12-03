Collection of community SD control models for users to download flexibly.

All files are already float16 and in safetensor format.



The files are mirrored with the below script:

files = {
'diffusers_xl_canny_small.safetensors': 'https://huggingface.co/diffusers/controlnet-canny-sdxl-1.0-small/resolve/main/diffusion_pytorch_model.bin',
'diffusers_xl_canny_mid.safetensors': 'https://huggingface.co/diffusers/controlnet-canny-sdxl-1.0-mid/resolve/main/diffusion_pytorch_model.bin',
'diffusers_xl_canny_full.safetensors': 'https://huggingface.co/diffusers/controlnet-canny-sdxl-1.0/resolve/main/diffusion_pytorch_model.bin',
'diffusers_xl_depth_small.safetensors': 'https://huggingface.co/diffusers/controlnet-depth-sdxl-1.0-small/resolve/main/diffusion_pytorch_model.bin',
'diffusers_xl_depth_mid.safetensors': 'https://huggingface.co/diffusers/controlnet-depth-sdxl-1.0-mid/resolve/main/diffusion_pytorch_model.bin',
'diffusers_xl_depth_full.safetensors': 'https://huggingface.co/diffusers/controlnet-depth-sdxl-1.0/resolve/main/diffusion_pytorch_model.bin',

'thibaud_xl_openpose.safetensors': 'https://huggingface.co/thibaud/controlnet-openpose-sdxl-1.0/resolve/main/OpenPoseXL2.safetensors',
'thibaud_xl_openpose_256lora.safetensors': 'https://huggingface.co/thibaud/controlnet-openpose-sdxl-1.0/resolve/main/control-lora-openposeXL2-rank256.safetensors',

'sargezt_xl_depth_faid_vidit.safetensors': 'https://huggingface.co/SargeZT/controlnet-sd-xl-1.0-depth-faid-vidit/resolve/main/diffusion_pytorch_model.bin',
'sargezt_xl_depth_zeed.safetensors': 'https://huggingface.co/SargeZT/controlnet-sd-xl-1.0-depth-zeed/resolve/main/diffusion_pytorch_model.bin',
'sargezt_xl_depth.safetensors': 'https://huggingface.co/SargeZT/controlnet-v1e-sdxl-depth/resolve/main/diffusion_pytorch_model.bin',
'sargezt_xl_softedge.safetensors': 'https://huggingface.co/SargeZT/controlnet-sd-xl-1.0-softedge-dexined/resolve/main/controlnet-sd-xl-1.0-softedge-dexined.safetensors',

'sai_xl_canny_128lora.safetensors': 'https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank128/control-lora-canny-rank128.safetensors',
'sai_xl_canny_256lora.safetensors': 'https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-canny-rank256.safetensors',
'sai_xl_depth_128lora.safetensors': 'https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank128/control-lora-depth-rank128.safetensors',
'sai_xl_depth_256lora.safetensors': 'https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-depth-rank256.safetensors',
'sai_xl_sketch_128lora.safetensors': 'https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank128/control-lora-sketch-rank128-metadata.safetensors',
'sai_xl_sketch_256lora.safetensors': 'https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-sketch-rank256.safetensors',
'sai_xl_recolor_128lora.safetensors': 'https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank128/control-lora-recolor-rank128.safetensors',
'sai_xl_recolor_256lora.safetensors': 'https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-recolor-rank256.safetensors',

'ioclab_sd15_recolor.safetensors': 'https://huggingface.co/ioclab/control_v1p_sd15_brightness/resolve/main/diffusion_pytorch_model.safetensors',

't2i-adapter_xl_canny.safetensors': 'https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models_XL/adapter-xl-canny.pth',
't2i-adapter_xl_openpose.safetensors': 'https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models_XL/adapter-xl-openpose.pth',
't2i-adapter_xl_sketch.safetensors': 'https://huggingface.co/TencentARC/T2I-Adapter/resolve/main/models_XL/adapter-xl-sketch.pth',

'ip-adapter_sd15_plus.safetensors': 'https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter-plus_sd15.bin',
'ip-adapter_sd15.safetensors': 'https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter_sd15.bin',
'ip-adapter_xl.safetensors': 'https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter_sdxl.bin',

'kohya_controllllite_xl_depth_anime.safetensors': 'https://huggingface.co/kohya-ss/controlnet-lllite/resolve/main/controllllite_v01008016e_sdxl_depth_anime.safetensors',
'kohya_controllllite_xl_canny_anime.safetensors': 'https://huggingface.co/kohya-ss/controlnet-lllite/resolve/main/controllllite_v01032064e_sdxl_canny_anime.safetensors',
'kohya_controllllite_xl_scribble_anime.safetensors': 'https://huggingface.co/kohya-ss/controlnet-lllite/resolve/main/controllllite_v01032064e_sdxl_fake_scribble_anime.safetensors',
'kohya_controllllite_xl_openpose_anime.safetensors': 'https://huggingface.co/kohya-ss/controlnet-lllite/resolve/main/controllllite_v01032064e_sdxl_pose_anime.safetensors',
'kohya_controllllite_xl_openpose_anime_v2.safetensors': 'https://huggingface.co/kohya-ss/controlnet-lllite/resolve/main/controllllite_v01032064e_sdxl_pose_anime_v2_500-1000.safetensors',

'kohya_controllllite_xl_blur_anime_beta.safetensors': 'https://huggingface.co/kohya-ss/controlnet-lllite/resolve/main/controllllite_v01016032e_sdxl_blur_anime_beta.safetensors',
'kohya_controllllite_xl_blur.safetensors': 'https://huggingface.co/kohya-ss/controlnet-lllite/resolve/main/controllllite_v01032064e_sdxl_blur-500-1000.safetensors',
'kohya_controllllite_xl_blur_anime.safetensors': 'https://huggingface.co/kohya-ss/controlnet-lllite/resolve/main/controllllite_v01032064e_sdxl_blur-anime_500-1000.safetensors',
'kohya_controllllite_xl_canny.safetensors': 'https://huggingface.co/kohya-ss/controlnet-lllite/resolve/main/controllllite_v01032064e_sdxl_canny.safetensors',
'kohya_controllllite_xl_depth.safetensors': 'https://huggingface.co/kohya-ss/controlnet-lllite/resolve/main/controllllite_v01032064e_sdxl_depth_500-1000.safetensors',

't2i-adapter_diffusers_xl_canny.safetensors': 'https://huggingface.co/TencentARC/t2i-adapter-canny-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors',
't2i-adapter_diffusers_xl_lineart.safetensors': 'https://huggingface.co/TencentARC/t2i-adapter-lineart-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors',
't2i-adapter_diffusers_xl_depth_midas.safetensors': 'https://huggingface.co/TencentARC/t2i-adapter-depth-midas-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors',
't2i-adapter_diffusers_xl_openpose.safetensors': 'https://huggingface.co/TencentARC/t2i-adapter-openpose-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors',
't2i-adapter_diffusers_xl_depth_zoe.safetensors': 'https://huggingface.co/TencentARC/t2i-adapter-depth-zoe-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors',
't2i-adapter_diffusers_xl_sketch.safetensors': 'https://huggingface.co/TencentARC/t2i-adapter-sketch-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors',

}

If you download the files from raw URL, you may need to rename them. 

However, files in https://huggingface.co/lllyasviel/sd_control_collection/tree/main are already renamed and can be directly downloaded.

Feel free to contact us if you are author of any listed models and you want some models to be removed/added (by opening an issue in this HuggingFace page).