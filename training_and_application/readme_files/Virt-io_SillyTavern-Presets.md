---
tags:
- roleplay
---

> [!IMPORTANT]
> v1.9 is still recommended<br>
> v2.0 is simmilar to v1.9 | json is a master import.<br>
> **Samplers are just for messing around**<br>
> **Turn on trim if you like it I just suffer from FOMO.**<br>


> [!IMPORTANT]
> Thanks to:<br>
> [SerialKicked](https://huggingface.co/SerialKicked) for [fixing context](https://huggingface.co/Virt-io/SillyTavern-Presets/discussions/3)<br>
> [saishf](https://huggingface.co/saishf) for testing all the bad versions<br>
> [Lewdiculous](https://huggingface.co/Lewdiculous) for testing and quantizing<br>
> [Herman555](https://huggingface.co/Herman555) for reminding me that [some models need a jailbreak](https://huggingface.co/Virt-io/SillyTavern-Presets/discussions/4)<br>
> [Clevyby](https://huggingface.co/Clevyby) for sharing their [sampler knowledge](https://huggingface.co/LWDCLS/LLM-Discussions/discussions/2#663b90a7a55b06346368adae)<br>
> [shrinkedd](https://www.reddit.com/r/SillyTavernAI/comments/1ca4xo8/ive_thought_of_a_way_to_decrease_chances_of/) for ideas<br>

### SillyTavern Presets

# Usage

Make sure to grab both context and instruct templates.
It should look something like this.

<img src="https://huggingface.co/Virt-io/SillyTavern-Presets/resolve/main/Images/Silly_Tavern_preset.png">

When using these presets you must set **Example Messages Behavior: Never include examples** otherwise they will be sent twice.

<img src="https://huggingface.co/Virt-io/SillyTavern-Presets/resolve/main/Images/ExampleMessages.png">

The reason for this, is because I explicitly set for them to be sent. The default behavior is for them to just be added at the end of the context prompt.


# Character Cards

**The following is just personal preference. However, it is recommended for a better experience.**

<img src="https://huggingface.co/Virt-io/SillyTavern-Presets/resolve/main/Images/Character_Cards_01.png">

> [!IMPORTANT]
> **Create a new neutral persona(USER_01)**<br>
> **For scenario, use a really vague description. This is to prevent the LLM from locking in. (Unless you want that)**<br>
> **I am currently running https://github.com/gaffe-buck/tavern-v2-character-creator inside a container**<br>

**Choosing a mode**

Prepend one of the following, before your request.

```
> Text Editor

> Character Creator

> Flexible P-list Formatter

> Ali-chat Generator

> Opening Scenario Writer
```

Example:
```
> Text Editor

---

Re-write the scenario in a dark fantasy philosophical style.
```

Example:
```
> Opening Scenario Writer

Create an opening scene for Char, Char enters a coffee shop.

> Text Editor

Re-write Char's opening scenario, in a dark comedy style.
```

<img src="https://huggingface.co/Virt-io/SillyTavern-Presets/resolve/main/Images/Character_Cards_02.png">


# Samplers

**I have decided to remove old samplers and only keep basic presets, I want people to play around and find what works best for them. Change context to desired context length**

[SillyTavern Docs](https://docs.sillytavern.app/usage/common-settings/#sampler-parameters)

**Temperature**
Feel free to play with this one, lower values are more grounded.

**Min-P**
Higher values chop off more probabilities.


Values between 0.025 - 0.10 are good, personally I would use 0.075 or lower.

**Repetition Penalty**
Tries to decrease repetition.


Do not set it higher than 1.2.


1.05 - 1.15 seem to work fine.

**Rep Pen Range**
The range of tokens which Repetition Penalty can see.
I have it set to 2048.

**Frequency Penalty**
Decreases repetition.

**Presence Penalty**
Increases word variety.

**Dynamic Temperature**
Min and Max temps, free to change as desired.


Exponent, do not set Exponent higher than the default of 1.


You might want to try playing around and setting it lower than 1, this pushes lower probabilies higher.


When setting exponent lower than 1, set Min-P a little higher (0.075)

**Smooth Sampling**
This one is great, smoothens out probabilities.


Lower is more diverse.


Recommended range 0.1 - 0.3
