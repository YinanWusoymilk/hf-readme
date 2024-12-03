---
license: apache-2.0
tags:
- text2image
- stable-diffusion
---

# Model Card for ELLA

<!-- Provide a quick summary of what the model is/does. -->


ELLA(*Efficient Large Language Model Adapter*) equips text-to-image diffusion models with powerful Large Language Models (LLM) to enhance text alignment without training of either U-Net or LLM.



[**Project Page**](https://ella-diffusion.github.io/) **|** [**Paper (ArXiv)**](https://arxiv.org/abs/2403.05135) **|** [**Code**](https://github.com/TencentQQGYLab/ELLA)

---

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

Diffusion models have demonstrated remarkable performance in the domain of text-to-image generation. However, the majority of these models still employ CLIP as their text encoder, which constrains their ability to comprehend dense prompts, which encompass multiple objects, detailed attributes, complex relationships, long-text alignment, etc. In this paper, We introduce an Efficient Large Language Model Adapter, termed ELLA, which equips text-to-image diffusion models with powerful Large Language Models (LLM) to enhance text alignment without training of either U-Net or LLM. To seamlessly bridge two pre-trained models, we investigate a range of semantic alignment connector designs and propose a novel module, the Timestep-Aware Semantic Connector (TSC), which dynamically extracts timestep-dependent conditions from LLM. Our approach adapts semantic features at different stages of the denoising process, assisting diffusion models in interpreting lengthy and intricate prompts over sampling timesteps. Additionally, ELLA can be readily incorporated with community models and tools to improve their prompt-following capabilities. To assess text-to-image models in dense prompt following, we introduce Dense Prompt Graph Benchmark (DPG-Bench), a challenging benchmark consisting of 1K dense prompts. Extensive experiments demonstrate the superiority of ELLA in dense prompt following compared to state-of-the-art methods, particularly in multiple object compositions involving diverse attributes and relationships.




- **Developed by:** [Xiwei Hu*](https://openreview.net/profile?id=~Xiwei_Hu1)
   [Rui Wang*](https://wrong.wang/)
   [Yixiao Fang*](https://openreview.net/profile?id=~Yixiao_Fang1)
   [Bin Fu*](https://openreview.net/profile?id=~BIN_FU2)
   [Pei Cheng](https://openreview.net/profile?id=~Pei_Cheng1)
   [Gang Yu✦](https://www.skicyyu.org/) 
- **License:** [apache-2.0]


### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/TencentQQGYLab/ELLA
- **Paper:** https://arxiv.org/abs/2403.05135


## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```
  @misc{hu2024ella,
        title={ELLA: Equip Diffusion Models with LLM for Enhanced Semantic Alignment}, 
        author={Xiwei Hu and Rui Wang and Yixiao Fang and Bin Fu and Pei Cheng and Gang Yu},
        year={2024},
        eprint={2403.05135},
        archivePrefix={arXiv},
        primaryClass={cs.CV}
  }
```