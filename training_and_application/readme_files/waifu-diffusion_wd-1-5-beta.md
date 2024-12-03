---
license: other
---

IMPORTANT: this is a BETA MODEL! It is not done!

# Release Notes
https://cafeai.notion.site/WD-1-5-Beta-Release-Notes-967d3a5ece054d07bb02cba02e8199b7

# Checkpoints
Checkpoints are located in the "checkpoints" folder, under the files tab

# VAE
WD 1.5 uses the same VAE as WD 1.4, which can be found here https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/vae/kl-f8-anime2.ckpt

# Aesthetic Embeddings
I've included a "wdgoodprompt" and "wdbadprompt" embedding in the embeddings folder to help make generation easier. With in progress models, its common to have to use long prompts for good results. Using these embeddings helps alleviate some of that.
 
# Generation
With Waifu Diffusion 1.5, best results are generated from generating at a resolution of somewhere between 500 and 1000 and then using 2x latent upscale hiresfix

Here are some prompting examples: https://cafeai.notion.site/WD-1-5-Beta-Examples-d9417e2f1f064437996b581f361e7ef3

## License
WD 1.5 is released under the Fair AI Public License 1.0-SD (https://freedevproject.org/faipl-1.0-sd/). If any derivative of this model is made, please share your changes accordingly. Special thanks to ronsor/undeleted (https://undeleted.ronsor.com/) for help with the license.
