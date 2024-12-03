---
library_name: diffusers
pipeline_tag: text-to-image
---
# Phased Consistency Model

LoRA weights of Stable Diffusion XL for fast text-to-image generation.


## Update

- [2024.06.19]: Upload the initial version of PCM LoRA weights of Stable Diffusion 3.

  - pcm_deterministic_2step_shift1.safetensors
  - pcm_deterministic_4step_shift3.safetensors
  - pcm_deterministic_4step_shift1.safetensors
  - pdm_stochastic_shift3.safetensors
- See our Github Code base for proper lora loading and scheduler usage.

- [2024.06.03]: Converted all LoRA weights and merge the repo of Stable Diffusion v1-5 and Stable Diffusion XL. Add LCM-Like PCM LoRAs, which functions just like LCM but works better at low-step regime. Note LoRA is not sufficient for one-step generation.

## Important Usage Guidance

1. Use DDIM or Euler instead of LCM for sampling! When using DDIM, set timestep_spacing="trailing", clip_sample = False and set_alpha_to_one = False.

2. The name of each LoRA weights indicates how many inference steps they should be applied.

3. The name of each LoRA weights indicates whether they are able to use normal CFGs or small CFGs
   - NormalCFG means that model equipped with the LoRA can use CFG value 2-9 for generation. Yet you should adjust the CFG values given the steps you applied.
When using fewer steps, you should use smaller CFGs. For example, use CFG 2.5 - 3.5 with 4 four steps and use CFG 3 - 6 with 8 steps. This is because that fewer-step means the model has fewer chance to fix the issues caused by the CFG.
   - SmallCFG means that the model equipped with the LoRA can use CFG value 1-2 for generation.



Note: 
- The normalCFG LoRAs are more sensitive to the prompts. Set proper positive and negative prompts for better quality.
- Just find the normalCFG with 4-step is not working very well. Trying to solve the issue.

[[paper](https://huggingface.co/papers/2405.18407)] [[arXiv](https://arxiv.org/abs/2405.18407)]  [[code](https://github.com/G-U-N/Phased-Consistency-Model)] [[project page](https://g-u-n.github.io/projects/pcm)]

If you have issues on usage or feel some weights are broken, please feel free to contact me. Email: fywang@link.cuhk.edu.hk