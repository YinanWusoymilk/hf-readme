---
license: apache-2.0
---
<img src="https://huggingface.co/Vezora/Mistral-22B-v0.1/resolve/main/unsloth.png" width="100" height="150" />

### Mistral-22b-V.01 Release Announcement 🚀

## This model is not an moe, it is infact a 22B parameter dense model!

**Date**: April 11
**Creator** [Nicolas Mejia-Petit](https://twitter.com/mejia_petit)

### Overview
Just one day after the release of **Mixtral-8x-22b**, we are excited to introduce our handcrafted experimental model, **Mistral-22b-V.01**. This model is a culmination of equal knowledge distilled from all experts into a single, dense 22b model. This model is not a single trained expert, rather its a compressed MOE model, turning it into a dense 22b mode. This is the first working MOE to Dense model conversion.

### Capabilities
- **Math Proficiency**: The model exhibits strong mathematical abilities. Dispite not being trained on math.

### Experimental Nature
Please note that Mistral-22b-V.01 is an experimental model. It has been fine-tuned with fewer examples compared to the model set for release tomorrow. We encourage you to explore its capabilities and provide feedback. This First model was trained on 500 regular human written Q/A and 500 tested python examples, this was done since it was only a test, it trained in less than an hour, so be warned this is a experimental model. Don't expect ground breaking results, expect llama 1 for now,the next V2 fingers crossed will be significantly better.

### Upcoming Release: V.2
Stay tuned for the release of **V.2** tomorrow, which will feature enhancements in:
- Multi-turn conversations
- Multiturn coding
- JSON mode
- Agent abilities

### Background
The decision to release this experimental version was prompted by someone attempting to replicate my experiment based on my tweets. We wanted to ensure our community has access to the official version first.

### Stay Updated
Keep an eye out for **V.2**, it's going to be a game-changer! And is currently training, will be done in the next ~24 hours. 🌟Paper Coming Soon🌟

## Thank you!
- Thank you to [Daniel Han](https://twitter.com/danielhanchen), for Unsloth AI which was used to train this model. this led to a 2-3x speed increae and 2-3x decrease in memmory consumption.
- Thank you to [Charles Coddard](https://twitter.com/chargoddard), for providng me with a script that was nessary to make this model.
- Thank you to Mistral, for releasing Another Wonderful open source model, under Apache 2.0.
- Thank you to [Tim Dettmers](https://twitter.com/Tim_Dettmers), for creating QLora
- Thank you to [Tri Dao](https://twitter.com/tri_dao), for creating Flash Attention
- Thank you to Microsoft, for the Lora paper, and the Slice-GPT paper.
- Thank you to the Hugging Face team, for everything.❤️ We really do appreciate you guys and all your hard work and commitment to the open source community!❤️

## I will answer more questions about this model tomorrow, I have not slept since mixtral 22bx8 dropped. Base model + V.2 Lora checkpoint will be available tomorrow ##

## Future plans, potentially continued pretraning, if 1. more questions dosent help, or 2. My second idea to only use the knowledge from 2 experts as oppsed to all 8. Since compressing all 8 might lead to the DORI effect (yes from findng nemo, and yes I'm taking credit from coining this phrase).