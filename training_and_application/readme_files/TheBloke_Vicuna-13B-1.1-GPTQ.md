---
license: other
inference: false
pipeline_tag: conversational
---
<!-- header start -->
<div style="width: 100%;">
    <img src="https://i.imgur.com/EBdldam.jpg" alt="TheBlokeAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p><a href="https://discord.gg/Jq4vkcDakD">Chat & support: my new Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<!-- header end -->
# Vicuna 13B 1.1 GPTQ 4bit 128g

This is a 4-bit GPTQ version of the [Vicuna 13B 1.1 model](https://huggingface.co/lmsys/vicuna-13b-delta-v1.1).

It was created by merging the deltas provided in the above repo with the original Llama 13B model, [using the code provided on their Github page](https://github.com/lm-sys/FastChat#vicuna-weights).

It was then quantized to 4bit using [GPTQ-for-LLaMa](https://github.com/qwopqwop200/GPTQ-for-LLaMa).

## Want to try this in Colab for free?

Check out this Google Colab provided by [eucdee](https://huggingface.co/eucdee): [Google Colab for Vicuna 1.1](https://colab.research.google.com/github/eucdee/AI/blob/main/4bit_TextGen_Gdrive.ipynb)

## My Vicuna 1.1 model repositories

I have the following Vicuna 1.1 repositories available:

**13B models:**
* [Unquantized 13B 1.1 model for GPU - HF format](https://huggingface.co/TheBloke/vicuna-13B-1.1-HF)
* [GPTQ quantized 4bit 13B 1.1 for GPU - `safetensors` and `pt` formats](https://huggingface.co/TheBloke/vicuna-13B-1.1-GPTQ-4bit-128g)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU inference](https://huggingface.co/TheBloke/vicuna-13B-1.1-GGML)

**7B models:**
* [Unquantized 7B 1.1 model for GPU - HF format](https://huggingface.co/TheBloke/vicuna-7B-1.1-HF)
* [GPTQ quantized 4bit 7B 1.1 for GPU - `safetensors` and `pt` formats](https://huggingface.co/TheBloke/vicuna-7B-1.1-GPTQ-4bit-128g)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU inference](https://huggingface.co/TheBloke/vicuna-7B-1.1-GGML)

## How to easily download and use this model in text-generation-webui

Open the text-generation-webui UI as normal.

1. Click the **Model tab**.
2. Under **Download custom model or LoRA**, enter `TheBloke/vicuna-13B-1.1-GPTQ-4bit-128g`.
3. Click **Download**.
4. Wait until it says it's finished downloading.
5. Click the **Refresh** icon next to **Model** in the top left.
6. In the **Model drop-down**: choose the model you just downloaded, `vicuna-13B-1.1-GPTQ-4bit-128g`.
7. If you see an error in the bottom right, ignore it - it's temporary.
8. Check that the `GPTQ parameters` are correct on the right: `Bits = 4`, `Groupsize = 128`, `model_type = Llama`
9. Click **Save settings for this model** in the top right.
10. Click **Reload the Model** in the top right.
11. Once it says it's loaded, click the **Text Generation tab** and enter a prompt!

## GIBBERISH OUTPUT

If you get gibberish output, it is because you are using the `safetensors` file without updating GPTQ-for-LLaMA.

If you use the `safetensors` file you must have the latest version of GPTQ-for-LLaMA inside text-generation-webui.

If you don't want to update, or you can't, use the `pt` file instead.

Either way, please read the instructions below carefully.

## Provided files

Two model files are provided. Ideally use the `safetensors` file. Full details below:

Details of the files provided:
* `vicuna-13B-1.1-GPTQ-4bit-128g.compat.no-act-order.pt`
  * `pt` format file, created without the `--act-order` flag.
  * This file may have slightly lower quality, but is included as it can be used without needing to compile the latest GPTQ-for-LLaMa code.
  * It will therefore work with one-click-installers on Windows, which include the older GPTQ-for-LLaMa code.
  * Command to create:
    * `python3 llama.py vicuna-13B-1.1-HF c4 --wbits 4 --true-sequential --groupsize 128 --save_safetensors vicuna-13B-1.1-GPTQ-4bit-128g.no-act-order.pt`

* `vicuna-13B-1.1-GPTQ-4bit-128g.latest.safetensors`
  * `safetensors` format, with improved file security, created with the latest [GPTQ-for-LLaMa](https://github.com/qwopqwop200/GPTQ-for-LLaMa) code.
  * Command to create:
    * `python3 llama.py vicuna-13B-1.1-HF c4 --wbits 4 --true-sequential --act-order --groupsize 128 --save_safetensors vicuna-13B-1.1-GPTQ-4bit-128g.safetensors`

## Manual instructions for `text-generation-webui`

File `vicuna-13B-1.1-GPTQ-4bit-128g.compat.no-act-order.pt` can be loaded the same as any other GPTQ file, without requiring any updates to [oobaboogas text-generation-webui](https://github.com/oobabooga/text-generation-webui).

[Instructions on using GPTQ 4bit files in text-generation-webui are here](https://github.com/oobabooga/text-generation-webui/wiki/GPTQ-models-\(4-bit-mode\)).

The other `safetensors` model file was created using `--act-order` to give the maximum possible quantisation quality, but this means it requires that the latest GPTQ-for-LLaMa is used inside the UI.

If you want to use the act-order `safetensors` files and need to update the Triton branch of GPTQ-for-LLaMa, here are the commands I used to clone the Triton branch of GPTQ-for-LLaMa, clone text-generation-webui, and install GPTQ into the UI:
```
# Clone text-generation-webui, if you don't already have it
git clone https://github.com/oobabooga/text-generation-webui
# Make a repositories directory
mkdir text-generation-webui/repositories
cd text-generation-webui/repositories
# Clone the latest GPTQ-for-LLaMa code inside text-generation-webui
git clone https://github.com/qwopqwop200/GPTQ-for-LLaMa
```

Then install this model into `text-generation-webui/models` and launch the UI as follows:
```
cd text-generation-webui
python server.py --model vicuna-13B-1.1-GPTQ-4bit-128g --wbits 4 --groupsize 128 --model_type Llama # add any other command line args you want
```

The above commands assume you have installed all dependencies for GPTQ-for-LLaMa and text-generation-webui. Please see their respective repositories for further information.

If you are on Windows, or cannot use the Triton branch of GPTQ for any other reason, you can instead use the CUDA branch:
```
git clone https://github.com/qwopqwop200/GPTQ-for-LLaMa -b cuda
cd GPTQ-for-LLaMa
python setup_cuda.py install
```
Then link that into `text-generation-webui/repositories` as described above.

Or just use `vicuna-13B-1.1-GPTQ-4bit-128g.compat.no-act-order.pt` as mentioned above, which should work without any upgrades to text-generation-webui.

<!-- footer start -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[TheBloke AI's Discord server](https://discord.gg/Jq4vkcDakD)

## Thanks, and how to contribute.

Thanks to the [chirper.ai](https://chirper.ai) team!

I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.

Donaters will get priority support on any and all AI/LLM/model questions and requests, access to a private Discord room, plus other benefits.

* Patreon: https://patreon.com/TheBlokeAI
* Ko-Fi: https://ko-fi.com/TheBlokeAI

**Patreon special mentions**: Aemon Algiz, Dmitriy Samsonov, Nathan LeClaire, Trenton Dambrowitz, Mano Prime, David Flickinger, vamX, Nikolai Manek, senxiiz, Khalefa Al-Ahmad, Illia Dulskyi, Jonathan Leane, Talal Aujan, V. Lukas, Joseph William Delisle, Pyrater, Oscar Rangel, Lone Striker, Luke Pendergrass, Eugene Pentland, Sebastain Graf, Johann-Peter Hartman.

Thank you to all my generous patrons and donaters!
<!-- footer end -->
# Vicuna Model Card

## Model details

**Model type:**
Vicuna is an open-source chatbot trained by fine-tuning LLaMA on user-shared conversations collected from ShareGPT.
It is an auto-regressive language model, based on the transformer architecture.

**Model date:**
Vicuna was trained between March 2023 and April 2023.

**Organizations developing the model:**
The Vicuna team with members from UC Berkeley, CMU, Stanford, and UC San Diego.

**Paper or resources for more information:**
https://vicuna.lmsys.org/

**License:**
Apache License 2.0

**Where to send questions or comments about the model:**
https://github.com/lm-sys/FastChat/issues

## Intended use
**Primary intended uses:**
The primary use of Vicuna is research on large language models and chatbots.

**Primary intended users:**
The primary intended users of the model are researchers and hobbyists in natural language processing, machine learning, and artificial intelligence.

## Training dataset
70K conversations collected from ShareGPT.com.

## Evaluation dataset
A preliminary evaluation of the model quality is conducted by creating a set of 80 diverse questions and utilizing GPT-4 to judge the model outputs. See https://vicuna.lmsys.org/ for more details.

## Major updates of weights v1.1
- Refactor the tokenization and separator. In Vicuna v1.1, the separator has been changed from `"###"` to the EOS token `"</s>"`. This change makes it easier to determine the generation stop criteria and enables better compatibility with other libraries.
- Fix the supervised fine-tuning loss computation for better model quality.