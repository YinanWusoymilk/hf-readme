---
inference: false
license: other
---

<!-- header start -->
<div style="width: 100%;">
    <img src="https://i.imgur.com/EBdldam.jpg" alt="TheBlokeAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p><a href="https://discord.gg/theblokeai">Chat & support: my new Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<!-- header end -->

# Eric Hartford's Wizard Vicuna 13B Uncensored GGML

These files are GGML format model files for [Eric Hartford's Wizard Vicuna 13B Uncensored](https://huggingface.co/ehartford/Wizard-Vicuna-13B-Uncensored).

These are SuperHOT GGMLs with an increased context length. SuperHOT is a new system that employs RoPE to expand context beyond what was originally possible for a model. It was discovered and developed by [kaiokendev](https://huggingface.co/kaiokendev).

In order to use the increased context length, you can presently use:
* [KoboldCpp](https://github.com/LostRuins/koboldcpp) - [release 1.33](https://github.com/LostRuins/koboldcpp/releases/tag/v1.33) or later.

Support is also expected to come to llama.cpp, however it is still being worked on and there is currently no ETA for that.

To use the increased context with KoboldCpp and (when supported) llama.cpp, simply use `--contextsize` to set the desired context, eg `--contextsize 4096` or `--contextsize 8192`.

## Repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/Wizard-Vicuna-13B-Uncensored-SuperHOT-8K-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU inference](https://huggingface.co/TheBloke/Wizard-Vicuna-13B-Uncensored-SuperHOT-8K-GGML)
* [Unquantised SuperHOT fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/TheBloke/Wizard-Vicuna-13B-Uncensored-SuperHOT-8K-fp16)
* [Unquantised base fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/ehartford/Wizard-Vicuna-13B-Uncensored)

<!-- compatibility_ggml start -->
## Compatibility

These GGMLs will work with any llama.cpp-compatible GGML client that supports k-quants.

However the increased context length won't work without specific support. See the note in the introduction for details on using increased context.

## Explanation of the new k-quant methods

The new methods available are:
* GGML_TYPE_Q2_K - "type-1" 2-bit quantization in super-blocks containing 16 blocks, each block having 16 weight. Block scales and mins are quantized with 4 bits. This ends up effectively using 2.5625 bits per weight (bpw)
* GGML_TYPE_Q3_K - "type-0" 3-bit quantization in super-blocks containing 16 blocks, each block having 16 weights. Scales are quantized with 6 bits. This end up using 3.4375 bpw.
* GGML_TYPE_Q4_K - "type-1" 4-bit quantization in super-blocks containing 8 blocks, each block having 32 weights. Scales and mins are quantized with 6 bits. This ends up using 4.5 bpw.
* GGML_TYPE_Q5_K - "type-1" 5-bit quantization. Same super-block structure as GGML_TYPE_Q4_K resulting in 5.5 bpw
* GGML_TYPE_Q6_K - "type-0" 6-bit quantization. Super-blocks with 16 blocks, each block having 16 weights. Scales are quantized with 8 bits. This ends up using 6.5625 bpw
* GGML_TYPE_Q8_K - "type-0" 8-bit quantization. Only used for quantizing intermediate results. The difference to the existing Q8_0 is that the block size is 256. All 2-6 bit dot products are implemented for this quantization type.

Refer to the Provided Files table below to see what files use which methods, and how.
<!-- compatibility_ggml end -->

## Provided files
| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| wizard-vicuna-13b-uncensored-superhot-8k.ggmlv3.q2_K.bin | q2_K | 2 | 5.51 GB | 8.01 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.vw and feed_forward.w2 tensors, GGML_TYPE_Q2_K for the other tensors. |
| wizard-vicuna-13b-uncensored-superhot-8k.ggmlv3.q3_K_L.bin | q3_K_L | 3 | 6.93 GB | 9.43 GB | New k-quant method. Uses GGML_TYPE_Q5_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| wizard-vicuna-13b-uncensored-superhot-8k.ggmlv3.q3_K_M.bin | q3_K_M | 3 | 6.31 GB | 8.81 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| wizard-vicuna-13b-uncensored-superhot-8k.ggmlv3.q3_K_S.bin | q3_K_S | 3 | 5.66 GB | 8.16 GB | New k-quant method. Uses GGML_TYPE_Q3_K for all tensors |
| wizard-vicuna-13b-uncensored-superhot-8k.ggmlv3.q4_K_M.bin | q4_K_M | 4 | 7.87 GB | 10.37 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q4_K |
| wizard-vicuna-13b-uncensored-superhot-8k.ggmlv3.q4_K_S.bin | q4_K_S | 4 | 7.37 GB | 9.87 GB | New k-quant method. Uses GGML_TYPE_Q4_K for all tensors |
| wizard-vicuna-13b-uncensored-superhot-8k.ggmlv3.q5_K_M.bin | q5_K_M | 5 | 9.23 GB | 11.73 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q5_K |
| wizard-vicuna-13b-uncensored-superhot-8k.ggmlv3.q5_K_S.bin | q5_K_S | 5 | 8.97 GB | 11.47 GB | New k-quant method. Uses GGML_TYPE_Q5_K for all tensors |
| wizard-vicuna-13b-uncensored-superhot-8k.ggmlv3.q6_K.bin | q6_K | 6 | 10.68 GB | 13.18 GB | New k-quant method. Uses GGML_TYPE_Q8_K - 6-bit quantization - for all tensors |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.

## How to run in `koboldcpp`

On Linux I use the following command line to launch the KoboldCpp UI with OpenCL aceleration and a context size of 4096:

```
python ./koboldcpp.py --stream --unbantokens --threads 8 --usecublas 100 wizard-vicuna-13b-uncensored-superhot-8k.ggmlv3.q5_0.bin
```

Change `--gpulayers 100` to the number of layers you want/are able to offload to the GPU. Remove it if you don't have GPU acceleration.

For OpenCL acceleration, change `--usecublas` to `--useclblast 0 0`. You may need to change the second `0` to `1` if you have both an iGPU and a discrete GPU.

<!-- footer start -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[TheBloke AI's Discord server](https://discord.gg/theblokeai)

## Thanks, and how to contribute.

Thanks to the [chirper.ai](https://chirper.ai) team!

I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.

Donaters will get priority support on any and all AI/LLM/model questions and requests, access to a private Discord room, plus other benefits.

* Patreon: https://patreon.com/TheBlokeAI
* Ko-Fi: https://ko-fi.com/TheBlokeAI

**Special thanks to**: Luke from CarbonQuill, Aemon Algiz, Dmitriy Samsonov.

**Patreon special mentions**: zynix , ya boyyy, Trenton Dambrowitz, Imad Khwaja, Alps Aficionado, chris gileta, John Detwiler, Willem Michiel, RoA, Mano Prime, Rainer Wilmers, Fred von Graf, Matthew Berman, Ghost , Nathan LeClaire, Iucharbius , Ai Maven, Illia Dulskyi, Joseph William Delisle, Space Cruiser, Lone Striker, Karl Bernard, Eugene Pentland, Greatston Gnanesh, Jonathan Leane, Randy H, Pierre Kircher, Willian Hasse, Stephen Murray, Alex , terasurfer , Edmond Seymore, Oscar Rangel, Luke Pendergrass, Asp the Wyvern, Junyu Yang, David Flickinger, Luke, Spiking Neurons AB, subjectnull, Pyrater, Nikolai Manek, senxiiz, Ajan Kanaga, Johann-Peter Hartmann, Artur Olbinski, Kevin Schuppel, Derek Yates, Kalila, K, Talal Aujan, Khalefa Al-Ahmad, Gabriel Puliatti, John Villwock, WelcomeToTheClub, Daniel P. Andersen, Preetika Verma, Deep Realms, Fen Risland, trip7s trip, webtim, Sean Connelly, Michael Levine, Chris McCloskey, biorpg, vamX, Viktor Bowallius, Cory Kujawski.

Thank you to all my generous patrons and donaters!

<!-- footer end -->

# Original model card: Kaio Ken's SuperHOT 8K

### SuperHOT Prototype 2 w/ 8K Context

This is a second prototype of SuperHOT, this time 30B with 8K context and no RLHF, using the same technique described in [the github blog](https://kaiokendev.github.io/til#extending-context-to-8k).
Tests have shown that the model does indeed leverage the extended context at 8K.

You will need to **use either the monkeypatch** or, if you are already using the monkeypatch, **change the scaling factor to 0.25 and the maximum sequence length to 8192**

#### Looking for Merged & Quantized Models?
- 30B 4-bit CUDA: [tmpupload/superhot-30b-8k-4bit-safetensors](https://huggingface.co/tmpupload/superhot-30b-8k-4bit-safetensors)
- 30B 4-bit CUDA 128g: [tmpupload/superhot-30b-8k-4bit-128g-safetensors](https://huggingface.co/tmpupload/superhot-30b-8k-4bit-128g-safetensors)


#### Training Details
I trained the LoRA with the following configuration:
- 1200 samples (~400 samples over 2048 sequence length)
- learning rate of 3e-4
- 3 epochs
- The exported modules are:
    - q_proj
    - k_proj
    - v_proj
    - o_proj
    - no bias
- Rank = 4
- Alpha = 8
- no dropout
- weight decay of 0.1
- AdamW beta1 of 0.9 and beta2 0.99, epsilon of 1e-5
- Trained on 4-bit base model

# Original model card: Eric Hartford's Wizard Vicuna 13B Uncensored


This is [wizard-vicuna-13b](https://huggingface.co/junelee/wizard-vicuna-13b) trained with a subset of the dataset - responses that contained alignment / moralizing were removed. The intent is to train a WizardLM that doesn't have alignment built-in, so that alignment (of any sort) can be added separately with for example with a RLHF LoRA.

Shout out to the open source AI/ML community, and everyone who helped me out.

Note:  

An uncensored model has no guardrails.  

You are responsible for anything you do with the model, just as you are responsible for anything you do with any dangerous object such as a knife, gun, lighter, or car.

Publishing anything this model generates is the same as publishing it yourself.

You are responsible for the content you publish, and you cannot blame the model any more than you can blame the knife, gun, lighter, or car for what you do with it.
