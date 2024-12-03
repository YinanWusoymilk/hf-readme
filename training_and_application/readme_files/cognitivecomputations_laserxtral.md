---
license: cc-by-nc-2.0
---

![image/webp](https://cdn-uploads.huggingface.co/production/uploads/646e57a5cb6ea6e6b6df1ad4/BtnWsqZnaG1I6aa-Ldkfz.webp)

by David, Fernando and Eric

Sponsored by: [VAGO Solutions](https://vago-solutions.de)

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/cognitivecomputations)
Discord: https://discord.gg/cognitivecomputations

An experimentation regarding 'lasering' each expert to denoise and enhance model capabilities.

This model has half size in comparison to the Mixtral 8x7b Instruct. And it basically has the same level of performance (we are working to get a better MMLU score).


# Laserxtral - 4x7b (all, except for base, lasered using laserRMT)

This model is a Mixture of Experts (MoE) made with [mergekit](https://github.com/cg123/mergekit) (mixtral branch). It uses the following base models:
 * [cognitivecomputations/dolphin-2.6-mistral-7b-dpo](https://huggingface.co/cognitivecomputations/dolphin-2.6-mistral-7b-dpo)
 * [mlabonne/Marcoro14-7B-slerp (base)](https://huggingface.co/mlabonne/Marcoro14-7B-slerp)
 * [beowolx/CodeNinja-1.0-OpenChat-7B](https://huggingface.co/beowolx/CodeNinja-1.0-OpenChat-7B)
 * [Q-bert/MetaMath-Cybertron-Starling](https://huggingface.co/Q-bert/MetaMath-Cybertron-Starling)
 * [WizardLM/WizardMath-7B-V1.1](https://huggingface.co/WizardLM/WizardMath-7B-V1.1)

It follows the implementation of laserRMT @ https://github.com/cognitivecomputations/laserRMT

Here, we are controlling layers checking which ones have lower signal to noise ratios (which are more subject to noise), to apply Laser interventions, still using Machenko Pastur to calculate this ratio.

We intend to be the first of a family of experimentations being carried out @ Cognitive Computations.

In this experiment we have observed very high truthfulness and high reasoning capabilities.

# Evals


![image/png](https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/j_fg_zwGXC1RS9npuJMAK.png)

