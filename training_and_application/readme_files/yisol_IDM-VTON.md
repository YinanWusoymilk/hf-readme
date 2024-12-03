---
base_model: stable-diffusion-xl-1.0-inpainting-0.1
tags:
  - stable-diffusion-xl
  - inpainting
  - virtual try-on
license: cc-by-nc-sa-4.0
---



# Check out more codes on our [github repository](https://github.com/yisol/IDM-VTON)!

# IDM-VTON : Improving Diffusion Models for Authentic Virtual Try-on in the Wild
This is an official implementation of paper 'Improving Diffusion Models for Authentic Virtual Try-on in the Wild'
- [paper](https://arxiv.org/abs/2403.05139) 
- [project page](https://idm-vton.github.io/) 

🤗 Try our huggingface [Demo](https://huggingface.co/spaces/yisol/IDM-VTON)

![teaser](assets/teaser.png)&nbsp;
![teaser2](assets/teaser2.png)&nbsp;


## TODO LIST


- [x] demo model
- [x] inference code
- [ ] training code




## Acknowledgements

For the demo, GPUs are supported from [zerogpu](https://huggingface.co/zero-gpu-explorers), and auto masking generation codes are based on [OOTDiffusion](https://github.com/levihsu/OOTDiffusion) and [DCI-VTON](https://github.com/bcmi/DCI-VTON-Virtual-Try-On).  
Parts of the code are based on [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter).



## Citation
```
@article{choi2024improving,
  title={Improving Diffusion Models for Virtual Try-on},
  author={Choi, Yisol and Kwak, Sangkyung and Lee, Kyungmin and Choi, Hyungwon and Shin, Jinwoo},
  journal={arXiv preprint arXiv:2403.05139},
  year={2024}
}
```

## License
The codes and checkpoints in this repository are under the [CC BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).



