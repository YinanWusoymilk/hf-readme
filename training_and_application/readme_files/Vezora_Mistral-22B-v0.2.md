---
license: apache-2.0
---
<img src="https://huggingface.co/Vezora/Mistral-22B-v0.1/resolve/main/unsloth.png" width="100" height="150" />

### Mistral-22b-v.02 Release Announcement 🚀

## This model is not an moe, it is infact a 22B parameter dense model!

**Date**: April 13
**Creator** [Nicolas Mejia-Petit](https://twitter.com/mejia_petit)

### Overview
- Just two days after our release of **Mistral-22b-v0.1**, we are excited to introduce our handcrafted experimental model, **Mistral-22b-v.02**. This model is a culmination of equal knowledge distilled from all experts into a single, dense 22b model. This model is not a single trained expert, rather its a compressed MOE model, turning it into a dense 22b mode. This is the first working MOE to Dense model conversion.
- v0.2 has trained on 8x more data than v0.1!
  
### Capabilities
- **Math Proficiency**: The model exhibits strong mathematical abilities. Dispite not being trained on math.
- **Better at Coding** The model is significantly better at coding, than V1, it passed some of my simple coding test, such as "Create a simple HTML site with a button that changes the background color to a random color", which V1 failed.
- **More Cohesive** This V2 model is significantly more cohesive, and better at aunderstanding the prompts and answering with the appopriate answer.
- **Highly Uncencored** Since this model was also Re-Alligned to be uncencored, it can just answer anything you ask. So use at your own risk, we take no responsibility for your generated responces.
- **Multi Turn** The dataset this model trained on was mostly all multi turn conversations, spanning many different topics, with some emphasis on coding.
- **Json Mode** I did train this model on answering in JSON and using JSON tools., I have yet to try it, in depth but preliminary test shows it works, including.
- **Agent abilities** I did train this model on agent datasets, that teach it to do real world tasks such as picking up an object, and even navigating a webpage based off HTML.
- **Good Chili Recipe** The model gives a good chili recipe :)
- **32k Sequence Length** This model was trained with a 32k sequence length.
- **GUANACO PROMPT FORMAT** YOU MUST USE THE GUANACO PROMPT FORMAT SHOWN BELLOW IN USAGE. Not using this prompt format will lead to sub optimal results.

### Experimental Nature
Please note that Mistral-22b is still in a WIP. v0.3 has started training now, with a different method than used before, this is to hopefully make the model more round in its internel knowlledge. Through my testing I found V2 to be a significant improvement over v.1.

### Upcoming Release: V.3
- v0.3 will feature a different base model for testing purposes, however this model is pretty darn good for a second test. :)
- I have done some preliminary results with my new v0.3 base model, and it appears to achieve a lower loss after the first epoch compared to the other base model used for v0.1 and v0.2. so we have started training v0.3 with the new base model and with the longer dataset, will be done and released in the next 48 hours. :)

### Stay Updated
**V.3**, coming soon! And is currently training, will be done in the next ~24 hours. 🌟Paper Coming Soon🌟
- There will be more of these 22b models. They 5-6 siblings till I find what the best results are for MOE compression.
- However I am very surprised at how good this V.2 model is, off my small testing. 
- I will be releasing a blog post soon on how I did this, I still will release a paper with testing and results, but I'm gonna rush out a paper before hand so I can share how I did this. I'd just like to make sure the right people get the right credit for their work that I used, so I have to read up some and make sure everyone gets the credit they deserve, ( and I need quality sleep my entire sleep schedule has been abominated since mixtrals drop.) I appreciate your understanding.
- I have a bunch of other methods I have yet to try, and many of those methods required me making this model, and running the initial tests, so they are only going to get better from here, I appretiate feedback, thank you!

### Usage:
- This model requires a specific chat template, as the training format was Guanaco this is what it looks like:
- "### System: You are a helpful assistant. ### Human###: Give me the best chili recipe you can ###Assistant: Here is the best chili recipe..."


## Thank you!
- Thank you to [Daniel Han](https://twitter.com/danielhanchen), for Unsloth AI which was used to train this model. this led to a 2-3x speed increae and 2-3x decrease in memmory consumption.
- Thank you to [Charles Goddard](https://twitter.com/chargoddard), for providng me with a script that was nessary to make this model.
- Thank you to Mistral, for releasing Another Wonderful open source model, under Apache 2.0.
- Thank you to [Tim Dettmers](https://twitter.com/Tim_Dettmers), for creating QLora
- Thank you to [Tri Dao](https://twitter.com/tri_dao), for creating Flash Attention
- Thank you to Microsoft, for the Lora paper, and the Slice-GPT paper.
- Thank you to the Hugging Face team, for everything.❤️ We really do appreciate you guys and all your hard work and commitment to the open source community!❤️
- Thank you to [Jon Durbin](https://x.com/jon_durbin?s=21) I used one of his DPO datasets converted to SFT, more info will be explained in paper.


## Future plans, train 4-5 more of these experimental models gather preliminary testing results, and then run evaluations on all the models I see have the best possibilities of excelling, then use the best one.