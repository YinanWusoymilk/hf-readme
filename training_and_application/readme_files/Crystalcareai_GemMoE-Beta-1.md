---
license: other
license_name: gemma-terms-of-use
license_link: https://ai.google.dev/gemma/terms
---

<p align="center">
  <a href="https://ibb.co/wgSH65b">
    <img src="https://i.ibb.co/JtvLkDb/Gemmoe-Logo.png" alt="Gemmoe-Logo" border="0">
  </a>
</p>


# ⚠️ REPO DEPRECATED ⚠️

> **NOTE:** This repo is deprecated in favor of the models found [here](https://huggingface.co/Crystalcareai/GemMoE-Base-Random/blob/main/howto.md).

## Purpose of this Repo

This repo purely serves to host the remote files needed to make GemMoE run with transformers. 

## ❌ Training and Inference

If you try to run training or inference from here, it will not work. Please refer to the new location of the models mentioned above.


# GemMoE: An 8x8 Mixture Of Experts based on Gemma.

I am delighted to finally be able to share the beta release of GemMoE, a project that has been a labor of love and a testament to the power of collaboration within the AI community. GemMoE is a Mixture of Experts (MoE) model that combines the strength of Deepmind's Gemma architecture with a custom-tailored approach to enable easy training and inference.

At its core, GemMoE comprises 8 separately fine-tuned Gemma models, with 2 experts per token. I have meticulously incorporated bug fixes for Gemma, ensuring that you can train and perform inference with GemMoE just as you would with any other model in the transformers library. My goal was to create a model that is not only powerful but also user-friendly and accessible to researchers, developers, and users alike.

## The Journey: Challenges and Gratitude

The development of GemMoE was challenging yet incredibly rewarding. Although I encountered numerous obstacles along the way, with the help and support of the AI community, I was able to overcome them and create something truly special.

One of the most significant challenges I faced was the lack of experience in developing a custom MoE architecture. As a self-taught developer, I had to learn many hard lessons from my previous project, Qwen1.5-8x7b. Although the methodology was there, the execution was lacking. I soon realized that I would need to create a completely new model class within the transformers library and implement a custom MoE architecture tailored specifically for Gemma. Through countless iterations and a tremendous amount of trial and error, I was able to refine the architecture and optimize its performance.

I cannot stress enough how grateful I am for the support and contributions of the AI community throughout this journey. Hugging Face, in particular, played a crucial role in making GemMoE a reality. Their generous compute grant allowed me to refine the architecture and optimize the model before committing resources to the full training. Victor M and Apolinaro from the Hugging Face team were instrumental in getting this project off the ground, and their swift support and dedication were truly inspiring.

I also want to express my heartfelt thanks to Eric Hartford, who provided invaluable assistance in troubleshooting Gemma's unstable loss curve during the early stages of development. Daniel Han from Unsloth deserves a special mention for his tireless work in identifying and fixing many of the bugs in Gemma's transformers implementation. His fixes enabled me to fine-tune 8 different versions of Gemma and combine them using a hidden gate with a heavily modified version of mergekit, a tool developed by the brilliant Charles Goddard.

Adapting Mergekit to support Gemma was no small feat, and I had to make significant alterations to ensure compatibility with GemMoE's architecture. This process involved a great deal of trial and error, but with persistence and the guidance of others in the community, I was able to integrate the modified mergekit into GemMoE successfully.

I want to extend my gratitude to Maxime Labonne for his incredibly useful LLM course and colab notebooks, which helped me level up my fine-tuning skills. Jon Durbin's bagel GitHub repository was a crash course in what makes good data, and it played a crucial role in informing my data selection process. The transparency and example set by Teknium inspired me to turn my AI side hustle into a full-time gig, and for that, I am deeply grateful.

Locutusque's datasets were a prime example of aggregating data like a pro. Justin Lin from Alibaba research supported my previous project, Qwen1.5 - 8x7b, which laid the foundation for GemMoE. I also want to thank Deepmind for releasing Gemma and acknowledge the hard work and dedication of everyone who contributed to its development.

The Deepseek team's DeepseekMoE paper was a game-changer for me, providing critical insights into what makes an MoE as good as possible. I am also incredibly grateful to the entire Perplexity team, whose answer engine accelerated my education and understanding of AI by a factor of five (source: vibes).

## The Future: Continuous Improvement and Community Collaboration

GemMoE is currently in beta, and I am actively working on refining the model, architecture, and implementation for full integration into the transformers library. I will release a comprehensive technical report detailing the development process and the solutions employed in GemMoE.

I am incredibly excited about GemMoE's future and potential. By collaborating with the community, we can continue to refine and improve GemMoE, pushing the boundaries of what is possible with MoE architectures and limited amounts of compute.

To facilitate this collaboration, I will release all 8 of the Gemma fine-tunes that went into GemMoE, along with a detailed technical breakdown of the model's architecture and training process. My hope is that by sharing this information, I can inspire and empower others to build upon GemMoE and create even more powerful models.

## A Heartfelt Thank You

Finally, I want to express my deepest gratitude to every member of the open-source community who has contributed to and supported this project. Your dedication, expertise, and willingness to share knowledge have been instrumental in bringing GemMoE to life.

To the users who will be working with GemMoE, thank you for your interest and support. Your enthusiasm humbles me, and I cannot wait to see what incredible applications and use cases you will find with this model.

GemMoE is a testament to the collaboration, perseverance, and unwavering commitment of the AI community to push the boundaries of what is possible for the GPU poor. I am honored to be a part of this community and look forward to continuing this journey of discovery with all of you.

-Lucas