---
license: cc-by-nc-4.0
language:
- en
datasets:
- Gryphe/Opus-WritingPrompts
- Sao10K/Claude-3-Opus-Instruct-15K
- Sao10K/Short-Storygen-v2
- Sao10K/c2-Logs-Filtered
---

*Just message me on discord if you want to host this privately for a service or something. We can talk.*

*Train used 1x H100 SXM for like a total of 24 Hours over multiple runs.*

Support me here if you're interested:
<br>Ko-fi: https://ko-fi.com/sao10k
<br> *wink* Euryale v2?

If not, that's fine too. Feedback would be nice.

Contact Me in Discord:
<br>`sao10k` // `Just ping me in the KoboldAI discord, I'll respond faster.`

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

---