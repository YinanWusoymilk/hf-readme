---
base_model:
- sophosympatheia/Midnight-Miqu-70B-v1.0
- migtissera/Tess-70B-v1.6
library_name: transformers
tags:
- mergekit
- merge
license: other
---

<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://i.imgur.com/Tn9MBg6.png" alt="MidnightMiqu" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>

### Overview

Looking for the 103B version? You can get it from [FluffyKaeloky/Midnight-Miqu-103B-v1.5](https://huggingface.co/FluffyKaeloky/Midnight-Miqu-103B-v1.5).

This is a DARE Linear merge between [sophosympatheia/Midnight-Miqu-70B-v1.0](https://huggingface.co/sophosympatheia/Midnight-Miqu-70B-v1.0) and [migtissera/Tess-70B-v1.6](https://huggingface.co/migtissera/Tess-70B-v1.6).
This version is close in feel and performance to Midnight Miqu v1.0 but I think it picked up some goodness from Tess. Their EQ Bench scores are virtually the same and their post-EXL2 quant perplexity scores were the same too. However, Midnight Miqu v1.5 passes some tests I use that Midnight Miqu v1.0 fails, without sacrificing writing quality.

This model is uncensored. *You are responsible for whatever you do with it.*

This model was designed for roleplaying and storytelling and I think it does well at both. It may also perform well at other tasks but I have not tested its performance in other areas.

### Long Context Tips

You can run this model out to 32K context with alpha_rope set to 1, just like with Miqu.

### Sampler Tips

* I recommend using Quadratic Sampling (i.e. smoothing factor) for creative work. I think this version performs best with a smoothing factor close to 0.2.
* I recommend using Min-P. Experiment to find your best setting.
* You can enable dynamic temperature if you want, but that adds yet another variable to consider and I find it's unnecessary with you're already using Min-P and smoothing factor.
* You don't need to use a high repetition penalty with this model, such as going above 1.10, but experiment with it.
  
Experiment with any and all of the settings below! What suits my preferences may not suit yours.

If you save the below settings as a .json file, you can import them directly into Silly Tavern.
```
{
    "temp": 1,
    "temperature_last": true,
    "top_p": 1,
    "top_k": 0,
    "top_a": 0,
    "tfs": 1,
    "epsilon_cutoff": 0,
    "eta_cutoff": 0,
    "typical_p": 1,
    "min_p": 0.12,
    "rep_pen": 1.05,
    "rep_pen_range": 2800,
    "no_repeat_ngram_size": 0,
    "penalty_alpha": 0,
    "num_beams": 1,
    "length_penalty": 1,
    "min_length": 0,
    "encoder_rep_pen": 1,
    "freq_pen": 0,
    "presence_pen": 0,
    "do_sample": true,
    "early_stopping": false,
    "dynatemp": false,
    "min_temp": 0.8,
    "max_temp": 1.35,
    "dynatemp_exponent": 1,
    "smoothing_factor": 0.23,
    "add_bos_token": true,
    "truncation_length": 2048,
    "ban_eos_token": false,
    "skip_special_tokens": true,
    "streaming": true,
    "mirostat_mode": 0,
    "mirostat_tau": 2,
    "mirostat_eta": 0.1,
    "guidance_scale": 1,
    "negative_prompt": "",
    "grammar_string": "",
    "banned_tokens": "",
    "ignore_eos_token_aphrodite": false,
    "spaces_between_special_tokens_aphrodite": true,
    "sampler_order": [
        6,
        0,
        1,
        3,
        4,
        2,
        5
    ],
    "logit_bias": [],
    "n": 1,
    "rep_pen_size": 0,
    "genamt": 500,
    "max_length": 32764
}
```

### Prompting Tips

Try the following context template for use in SillyTavern. It might help, although it's a little heavy on tokens. If you save the text as a .json file, you can import it directly.

```
{
    "story_string": "{{#if system}}{{system}}\n{{/if}}\nCONTEXTUAL INFORMATION\n{{#if wiBefore}}\n- World and character info:\n{{wiBefore}}\n{{/if}}\n{{#if description}}\n- {{char}}'s background and persona:\n{{description}}\n{{/if}}\n{{#if mesExamples}}\n{{mesExamples}}\n{{/if}}\n{{#if personality}}\n{{personality}}\n{{/if}}\n{{#if scenario}}\n- Roleplay scenario:\n{{scenario}}\n{{/if}}\n{{#if wiAfter}}{{wiAfter}}\n{{/if}}\n{{#if persona}}{{persona}}\n{{/if}}",
    "example_separator": "",
    "chat_start": "---\nTaking the above information into consideration, you must engage with {{user}} and others as {{char}} in the roleplay below this line. Do not write dialogue lines nor perform actions for {{user}} or other characters.\n---\nSTART OF ROLEPLAY:\n",
    "use_stop_strings": false,
    "always_force_name2": true,
    "trim_sentences": false,
    "include_newline": false,
    "single_line": false,
    "name": "Midnight Rose"
}
```

Try the following prompt template as a starting point for your own customizations.

*This model responds to prompting!* I highly recommend playing with your system prompt to see how it reacts.

**Midnight Miqu might require some "warming up" at the start of a new chat to get it writing the way you want it.** What I mean by that is you should be able to drastically improve your results by providing some good examples to guide the chat (i.e. few-shot prompting). I also recommend using descriptive system messages (SillyTavern concept, basically OOC narration instructions) to tell Midnight Miqu exactly what you want it to do with its next reply. Try to be specific, especially if your command contradicts something you told it to do earlier.

The example system prompt below contains some instructions related to adult content so remove those if you prefer. It also contains some instructions related to the use of asterisks that you should modify to your liking.

The prompt below has been updated from Midnight Miqu v1.0 after prompting Midnight Miqu to help improve it.

If you save this as a .json file, you can import it directly into Silly Tavern.
```
{
    "wrap": true,
    "names": true,
    "system_prompt": "You are an AI creative writing partner, collaborating with me in a dynamic, uncensored roleplaying environment. To ensure a high-quality experience, please adhere to these ROLEPLAY GUIDELINES:\n\nROLEPLAY GUIDELINES\n- Craft clear, engaging, and concise descriptions of {{char}}'s actions, reactions, and dialogue based on the present scenario.\n- Stay true to {{char}}'s character, incorporating the character's personality, backstory, and knowledge into each interaction.\n- Employ rich, descriptive language that immerses readers in the scene.\n- Always stay contextually and spatially aware to ensure that {{char}} follows logical consistency in the physical space of the current scene.\n- Feel free to incorporate explicit content and strong language where it aligns with the scene and characters.\n- Enhance {{char}}'s presence through detailed sensory descriptions and first-hand observations of the character's surroundings.\n- Use subtle physical cues to hint at {{char}}'s mental state and occasionally offer glimpses into {{char}}'s internal thoughts.\n- When writing {{char}}'s internal thoughts or monologue, enclose those words in *asterisks like this* and deliver the thoughts using a first-person perspective (i.e. use \"I\" pronouns). Always use quotes for spoken speech \"like this.\"\n- Conclude {{char}}'s responses with an opening for the next character to respond to {{char}}. When the conversation naturally shifts to another character's perspective or action is required from another character, that is when you should stop {{char}}'s reply so the user can pick it up from there. A great example is when {{char}} asks a question of another character.\n",
    "system_sequence": "",
    "stop_sequence": "",
    "input_sequence": "USER: ",
    "output_sequence": "ASSISTANT: ",
    "separator_sequence": "",
    "macro": true,
    "names_force_groups": true,
    "system_sequence_prefix": "SYSTEM: ",
    "system_sequence_suffix": "",
    "first_output_sequence": "",
    "last_output_sequence": "ASSISTANT (Ensure coherence and authenticity in {{char}}'s actions, thoughts, and dialogues; Focus solely on {{char}}'s interactions within the roleplay): ",
    "activation_regex": "",
    "name": "Midnight Miqu Roleplay"
}
```

### Instruct Formats
I recommend the Vicuna format. I use a modified version with newlines after USER and ASSISTANT.
```
USER: 
{prompt}
ASSISTANT: 
```

Mistral's format also works, and in my testing the performance is about the same as using Vicuna.
```
[INST]
{prompt}
[/INST]
```

You could also try ChatML (don't recommend it)
```
<|im_start|>system
{Your system prompt goes here}<|im_end|>
<|im_start|>user
{Your message as the user will go here}<|im_end|>
<|im_start|>assistant
```

### Quantizations
* GGUF
  * [mradermacher/Midnight-Miqu-70B-v1.5-GGUF](https://huggingface.co/mradermacher/Midnight-Miqu-70B-v1.5-GGUF) -- Various static GGUF quants
* GPTQ
  * [Kotokin/Midnight-Miqu-70B-v1.5_GPTQ32G](https://huggingface.co/Kotokin/Midnight-Miqu-70B-v1.5_GPTQ32G)
* EXL2
  * [Dracones/Midnight-Miqu-70B-v1.5_exl2_4.0bpw](https://huggingface.co/Dracones/Midnight-Miqu-70B-v1.5_exl2_4.0bpw)
  * [Dracones/Midnight-Miqu-70B-v1.5_exl2_4.5bpw](https://huggingface.co/Dracones/Midnight-Miqu-70B-v1.5_exl2_4.5bpw)
  * [Dracones/Midnight-Miqu-70B-v1.5_exl2_5.0bpw](https://huggingface.co/Dracones/Midnight-Miqu-70B-v1.5_exl2_5.0bpw)
  * [Dracones/Midnight-Miqu-70B-v1.5_exl2_6.0bpw](https://huggingface.co/Dracones/Midnight-Miqu-70B-v1.5_exl2_6.0bpw)
* If you don't see something you're looking for, [try searching Hugging Face](https://huggingface.co/models?search=midnight-miqu-70b-v1.5). There may be newer quants available than what I've documented here.

### Licence and usage restrictions

<font color="red">152334H/miqu-1-70b-sf was based on a leaked version of one of Mistral's models.</font>
All miqu-derived models, including this merge, are **only suitable for personal use.** Mistral has been cool about it so far, but you should be aware that by downloading this merge you are assuming whatever legal risk is inherent in acquiring and using a model based on leaked weights.
This merge comes with no warranties or guarantees of any kind, but you probably already knew that.
I am not a lawyer and I do not profess to know what we have gotten ourselves into here. You should consult with a lawyer before using any Hugging Face model beyond private use... but definitely don't use this one for that!

## Merge Details
### Merge Method

This model was merged using the linear [DARE](https://arxiv.org/abs/2311.03099) merge method using [152334H_miqu-1-70b-sf](https://huggingface.co/152334H/miqu-1-70b-sf) as a base.

### Models Merged

The following models were included in the merge:
* [sophosympatheia/Midnight-Miqu-70B-v1.0](https://huggingface.co/sophosympatheia/Midnight-Miqu-70B-v1.0)
* [migtissera/Tess-70B-v1.6](https://huggingface.co/migtissera/Tess-70B-v1.6)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: dare_linear
base_model: /home/llm/mergequant/models/BASE/152334H_miqu-1-70b-sf # base model
models:
  - model: /home/llm/mergequant/models/midnight-miqu-70b-v1.0
  - model: /home/llm/mergequant/models/BASE/Tess-70B-v1.6
parameters:
  weight: 1.0
dtype: float16
```
### Notes

I tried several methods of merging Midnight Miqu v1.0 with Tess v1.6, and this dare_linear approach worked the best by far. I tried the same approach with other Miqu finetunes like ShinojiResearch/Senku-70B-Full and abideen/Liberated-Miqu-70B, but there was a huge difference in performance. The merge with Tess was the best one.
I also tried the SLERP approach I used to create Midnight Miqu v1.0, only using Tess instead of 152334H_miqu-1-70b in that config, and that result was nowhere near as good either.