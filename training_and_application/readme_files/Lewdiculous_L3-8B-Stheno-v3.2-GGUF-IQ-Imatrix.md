---
base_model: Sao10K/L3-8B-Stheno-v3.2
quantized_by: Lewdiculous
library_name: transformers
license: cc-by-nc-4.0
inference: false
language:
- en
tags:
- roleplay
- llama3
- sillytavern
---

# #roleplay #sillytavern #llama3

My GGUF-IQ-Imatrix quants for [Sao10K/L3-8B-Stheno-v3.2](https://huggingface.co/Sao10K/L3-8B-Stheno-v3.2).

**Sao10K** with Stheno again, another banger! I recommend checking his page for feedback and support.

> [!IMPORTANT]
> **Quantization process:** <br>
> For future reference, these quants have been done after the fixes from [**#6920**](https://github.com/ggerganov/llama.cpp/pull/6920) have been merged. <br>
> Imatrix data was generated from the FP16-GGUF and conversions directly from the BF16-GGUF. <br>
> This was a bit more disk and compute intensive but hopefully avoided any losses during conversion. <br>
> If you noticed any issues let me know in the discussions.

> [!NOTE]
> **General usage:** <br>
> Use the [**latest version of KoboldCpp**](https://github.com/LostRuins/koboldcpp/releases/latest). <br>
> For **8GB VRAM** GPUs, I recommend the **Q4_K_M-imat** (4.89 BPW) quant for up to 12288 context sizes. <br>
>
> **Presets:** <br>
> Some compatible SillyTavern presets can be found [**here (Virt's Roleplay Presets)**](https://huggingface.co/Virt-io/SillyTavern-Presets). <br>
> Check [**discussions such as this one**](https://huggingface.co/Virt-io/SillyTavern-Presets/discussions/5#664d6fb87c563d4d95151baa) for other recommendations and samplers.

> [!TIP]
> **Personal-support:** <br>
> I apologize for disrupting your experience. <br>
> Currently I'm working on moving for a better internet provider. <br>
> If you **want** and you are **able to**... <br>
> You can [**spare some change over here (Ko-fi)**](https://ko-fi.com/Lewdiculous). <br>
>
> **Author-support:** <br>
> You can support the author [**at their own page**](https://ko-fi.com/sao10k).


![image/png](https://cdn-uploads.huggingface.co/production/uploads/65d4cf2693a0a3744a27536c/1rLk3xdnfD7AkdQBXWUqb.png)

<details>
<summary>Click here for the original model card information.</summary>

Support me here if you're interested:
<br>Ko-fi: https://ko-fi.com/sao10k
<br> *wink* Euryale v2?

If not, that's fine too. Feedback would be nice.

Contact Me in Discord:
<br>`sao10k`

`Art by navy_(navy.blue)` - [Danbooru](https://danbooru.donmai.us/posts/3214477)

---

![Stheno](https://huggingface.co/Sao10K/L3-8B-Stheno-v3.2/resolve/main/Stheno.png?)

Stheno-v3.2-Zeta

I have done a test run with multiple variations of the models, merged back to its base at various weights, different training runs too, and this Sixth iteration is the one I like most.


Changes compared to v3.1
<br>\- Included a mix of SFW and NSFW Storywriting Data, thanks to [Gryphe](https://huggingface.co/datasets/Gryphe/Opus-WritingPrompts)
<br>\- Included More Instruct / Assistant-Style Data
<br>\- Further cleaned up Roleplaying Samples from c2 Logs -> A few terrible, really bad samples escaped heavy filtering. Manual pass fixed it.
<br>\- Hyperparameter tinkering for training, resulting in lower loss levels.


Testing Notes - Compared to v3.1
<br>\- Handles SFW / NSFW seperately better. Not as overly excessive with NSFW now. Kinda balanced.
<br>\- Better at Storywriting / Narration.
<br>\- Better at Assistant-type Tasks.
<br>\- Better Multi-Turn Coherency -> Reduced Issues?
<br>\- Slightly less creative? A worthy tradeoff. Still creative.
<br>\- Better prompt / instruction adherence.

---

**Recommended Samplers:**

```
Temperature - 1.12-1.22
Min-P - 0.075
Top-K - 50
Repetition Penalty - 1.1
```

**Stopping Strings:**

```
\n\n{{User}} # Or Equivalent, depending on Frontend
<|eot_id|>
<|end_of_text|>
```

**Prompting Template - Llama-3-Instruct**

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

{output}<|eot_id|>
```

**Basic Roleplay System Prompt**
```
You are an expert actor that can fully immerse yourself into any role given. You do not break character for any reason, even if someone tries addressing you as an AI or language model.
Currently your role is {{char}}, which is described in detail below. As {{char}}, continue the exchange with {{user}}.
```

</details>