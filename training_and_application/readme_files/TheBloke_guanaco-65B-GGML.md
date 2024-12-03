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
        <p><a href="https://discord.gg/Jq4vkcDakD">Chat & support: my new Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<!-- header end -->

# Tim Dettmers' Guanaco 65B GGML

These files are GGML format model files for [Tim Dettmers' Guanaco 65B](https://huggingface.co/timdettmers/guanaco-65b).

GGML files are for CPU + GPU inference using [llama.cpp](https://github.com/ggerganov/llama.cpp) and libraries and UIs which support this format, such as:
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui)
* [KoboldCpp](https://github.com/LostRuins/koboldcpp)
* [ParisNeo/GPT4All-UI](https://github.com/ParisNeo/gpt4all-ui)
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
* [ctransformers](https://github.com/marella/ctransformers)

## Repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/guanaco-65B-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU+GPU inference](https://huggingface.co/TheBloke/guanaco-65B-GGML)
* [Unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/TheBloke/guanaco-65B-HF)

## Prompt template

```
### Human: prompt
### Assistant:
```

<!-- compatibility_ggml start -->
## Compatibility

### Original llama.cpp quant methods: `q4_0, q4_1, q5_0, q5_1, q8_0`

I have quantized these 'original' quantisation methods using an older version of llama.cpp so that they remain compatible with llama.cpp as of May 19th, commit `2d5db48`.

They should be compatible with all current UIs and libraries that use llama.cpp, such as those listed at the top of this README.

### New k-quant methods: `q2_K, q3_K_S, q3_K_M, q3_K_L, q4_K_S, q4_K_M, q5_K_S, q6_K`

These new quantisation methods are compatible with llama.cpp as of June 6th, commit `2d43387`.

They are now also compatible with recent releases of text-generation-webui, KoboldCpp, llama-cpp-python and ctransformers. Other tools and libraries may or may not be compatible - check their documentation if in doubt.

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
| guanaco-65B.ggmlv3.q2_K.bin | q2_K | 2 | 27.33 GB | 29.83 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.vw and feed_forward.w2 tensors, GGML_TYPE_Q2_K for the other tensors. |
| guanaco-65B.ggmlv3.q3_K_L.bin | q3_K_L | 3 | 34.55 GB | 37.05 GB | New k-quant method. Uses GGML_TYPE_Q5_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| guanaco-65B.ggmlv3.q3_K_M.bin | q3_K_M | 3 | 31.40 GB | 33.90 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| guanaco-65B.ggmlv3.q3_K_S.bin | q3_K_S | 3 | 28.06 GB | 30.56 GB | New k-quant method. Uses GGML_TYPE_Q3_K for all tensors |
| guanaco-65B.ggmlv3.q4_0.bin | q4_0 | 4 | 36.73 GB | 39.23 GB | Original llama.cpp quant method, 4-bit. |
| guanaco-65B.ggmlv3.q4_1.bin | q4_1 | 4 | 40.81 GB | 43.31 GB | Original llama.cpp quant method, 4-bit. Higher accuracy than q4_0 but not as high as q5_0. However has quicker inference than q5 models. |
| guanaco-65B.ggmlv3.q4_K_M.bin | q4_K_M | 4 | 39.28 GB | 41.78 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q4_K |
| guanaco-65B.ggmlv3.q4_K_S.bin | q4_K_S | 4 | 36.73 GB | 39.23 GB | New k-quant method. Uses GGML_TYPE_Q4_K for all tensors |
| guanaco-65B.ggmlv3.q5_0.bin | q5_0 | 5 | 44.89 GB | 47.39 GB | Original llama.cpp quant method, 5-bit. Higher accuracy, higher resource usage and slower inference. |
| guanaco-65B.ggmlv3.q5_1.bin | q5_1 | 5 | 48.97 GB | 51.47 GB | Original llama.cpp quant method, 5-bit. Even higher accuracy, resource usage and slower inference. |
| guanaco-65B.ggmlv3.q5_K_M.bin | q5_K_M | 5 | 46.20 GB | 48.70 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q5_K |
| guanaco-65B.ggmlv3.q5_K_S.bin | q5_K_S | 5 | 44.89 GB | 47.39 GB | New k-quant method. Uses GGML_TYPE_Q5_K for all tensors |
| guanaco-65B.ggmlv3.q6_K.bin | q6_K | 6 | 53.56 GB | 56.06 GB | New k-quant method. Uses GGML_TYPE_Q8_K - 6-bit quantization - for all tensors |
| guanaco-65B.ggmlv3.q8_0.bin | q8_0 | 8 | 69.370 GB | 71.87 GB | Original llama.cpp quant method, 8-bit. Almost indistinguishable from float16. High resource use and slow. Not recommended for most users. |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.

### q6_K and q8_0 files require expansion from archive

**Note:** HF does not support uploading files larger than 50GB. Therefore I have uploaded the q6_K and q8_0 files as multi-part ZIP files. They are not compressed, it is just storing the .bin file in two parts.

### q6_K 
Please download:
* `guanaco-65B.ggmlv3.q6_K.zip`
* `guanaco-65B.ggmlv3.q6_K.z01`

### q8_0
Please download:
* `guanaco-65B.ggmlv3.q8_0.zip`
* `guanaco-65B.ggmlv3.q8_0.z01`

Then extract the .zip archive. This will will expand both parts automatically. On Linux I found I had to use `7zip` - the basic `unzip` tool did not work. Example:
```
sudo apt update -y && sudo apt install 7zip
7zz x guanaco-65B.ggmlv3.q6_K.zip`
```

Once the `.bin` is extracted you can delete the `.zip` and `.z01` files

## How to run in `llama.cpp`

I use the following command line; adjust for your tastes and needs:

```
./main -t 10 -ngl 32 -m guanaco-65B.ggmlv3.q5_0.bin --color -c 2048 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "USER: Write a story about llamas\nASSISTANT:"
```
Change `-t 10` to the number of physical CPU cores you have. For example if your system has 8 cores/16 threads, use `-t 8`.

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

## How to run in `text-generation-webui`

Further instructions here: [text-generation-webui/docs/llama.cpp-models.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/llama.cpp-models.md).

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

**Special thanks to**: Luke from CarbonQuill, Aemon Algiz, Dmitriy Samsonov.

**Patreon special mentions**: Ajan Kanaga, Kalila, Derek Yates, Sean Connelly, Luke, Nathan LeClaire, Trenton Dambrowitz, Mano Prime, David Flickinger, vamX, Nikolai Manek, senxiiz, Khalefa Al-Ahmad, Illia Dulskyi, trip7s trip, Jonathan Leane, Talal Aujan, Artur Olbinski, Cory Kujawski, Joseph William Delisle, Pyrater, Oscar Rangel, Lone Striker, Luke Pendergrass, Eugene Pentland, Johann-Peter Hartmann.

Thank you to all my generous patrons and donaters!

<!-- footer end -->

# Original model card: Tim Dettmers' Guanaco 65B

# Guanaco Models Based on LLaMA

| [Paper](https://arxiv.org/abs/2305.14314) | [Code](https://github.com/artidoro/qlora) | [Demo](https://huggingface.co/spaces/uwnlp/guanaco-playground-tgi) | 

**The Guanaco models are open-source finetuned chatbots obtained through 4-bit QLoRA tuning of LLaMA base models on the OASST1 dataset. They are available in 7B, 13B, 33B, and 65B parameter sizes.**

⚠️Guanaco is a model purely intended for research purposes and could produce problematic outputs.

## Why use Guanaco?
- **Competitive with commercial chatbot systems on the Vicuna and OpenAssistant benchmarks** (ChatGPT and BARD) according to human and GPT-4 raters. We note that the relative performance on tasks not covered in these benchmarks could be very different. In addition, commercial systems evolve over time (we used outputs from the March 2023 version of the models).
- **Available open-source for research purposes**. Guanaco models allow *cheap* and *local* experimentation with high-quality chatbot systems.
- **Replicable and efficient training procedure** that can be extended to new use cases. Guanaco training scripts are available in the [QLoRA repo](https://github.com/artidoro/qlora).
- **Rigorous comparison to 16-bit methods** (both 16-bit full-finetuning and LoRA) in [our paper](https://arxiv.org/abs/2305.14314) demonstrates the effectiveness of 4-bit QLoRA finetuning. 
- **Lightweight** checkpoints which only contain adapter weights.

## License and Intended Use
Guanaco adapter weights are available under Apache 2 license. Note the use of the Guanaco adapter weights, requires access to the LLaMA model weighs. 
Guanaco is based on LLaMA and therefore should be used according to the LLaMA license. 

## Usage
Here is an example of how you would load Guanaco 7B in 4-bits:
```python
import torch
from peft import PeftModel    
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

model_name = "huggyllama/llama-7b"
adapters_name = 'timdettmers/guanaco-7b'

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_4bit=True,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    max_memory= {i: '24000MB' for i in range(torch.cuda.device_count())},
    quantization_config=BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type='nf4'
    ),
)
model = PeftModel.from_pretrained(model, adapters_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

```
Inference can then be performed as usual with HF models as follows:
```python
prompt = "Introduce yourself"
formatted_prompt = (
    f"A chat between a curious human and an artificial intelligence assistant."
    f"The assistant gives helpful, detailed, and polite answers to the user's questions.\n"
    f"### Human: {prompt} ### Assistant:"
)
inputs = tokenizer(formatted_prompt, return_tensors="pt").to("cuda:0")
outputs = model.generate(inputs=inputs.input_ids, max_new_tokens=20)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```
Expected output similar to the following:
```
A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.
### Human: Introduce yourself ### Assistant: I am an artificial intelligence assistant. I am here to help you with any questions you may have.
```


## Current Inference Limitations 
Currently, 4-bit inference is slow. We recommend loading in 16 bits if inference speed is a concern. We are actively working on releasing efficient 4-bit inference kernels.

Below is how you would load the model in 16 bits:
```python
model_name = "huggyllama/llama-7b"
adapters_name = 'timdettmers/guanaco-7b'
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    max_memory= {i: '24000MB' for i in range(torch.cuda.device_count())},
)
model = PeftModel.from_pretrained(model, adapters_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

```


## Model Card
**Architecture**: The Guanaco models are LoRA adapters to be used on top of LLaMA models. They are added to all layers. For all model sizes, we use $r=64$.

**Base Model**: Guanaco uses LLaMA as base model with sizes 7B, 13B, 33B, 65B. LLaMA is a causal language model pretrained on a large corpus of text. See [LLaMA paper](https://arxiv.org/abs/2302.13971) for more details. Note that Guanaco can inherit biases and limitations of the base model.

**Finetuning Data**: Guanaco is finetuned on OASST1. The exact dataset is available at [timdettmers/openassistant-guanaco](https://huggingface.co/datasets/timdettmers/openassistant-guanaco).

**Languages**: The OASST1 dataset is multilingual (see [the paper](https://arxiv.org/abs/2304.07327) for details) and as such Guanaco responds to user queries in different languages. We note, however, that OASST1 is heavy in high-resource languages. In addition, human evaluation of Guanaco was only performed in English and based on qualitative analysis we observed degradation in performance in other languages. 

Next, we describe Training and Evaluation details.

### Training
Guanaco models are the result of 4-bit QLoRA supervised finetuning on the OASST1 dataset. 

All models use NormalFloat4 datatype for the base model and LoRA adapters on all linear layers with BFloat16 as computation datatype. We set LoRA $r=64$, $\alpha=16$. We also use Adam beta2 of 0.999, max grad norm of 0.3 and LoRA dropout of 0.1 for models up to 13B and 0.05 for 33B and 65B models.
For the finetuning process, we use constant learning rate schedule and paged AdamW optimizer. 

### Training hyperparameters
Size| Dataset | Batch Size | Learning Rate | Max Steps | Sequence length 
---|---|---|---|---|---
7B | OASST1      | 16 | 2e-4 | 1875 | 512
13B | OASST1     | 16 | 2e-4 | 1875 | 512
33B | OASST1     | 16 | 1e-4 | 1875 | 512
65B | OASST1     | 16 | 1e-4 | 1875 | 512

### Evaluation
We test generative language capabilities through both automated and human evaluations. This second set of evaluations relies on queries curated by humans and aims at measuring the quality of model responses. We use the Vicuna and OpenAssistant datasets with 80 and 953 prompts respectively. 

In both human and automated evaluations, for each prompt, raters compare all pairs of responses across the models considered. For human raters we randomize the order of the systems, for GPT-4 we evaluate with both orders.

  
Benchmark | Vicuna |  | Vicuna |   | OpenAssistant |   | -
-----------|----|-----|--------|---|---------------|---|---
Prompts    | 80 |     | 80     |   | 953           |   |
Judge | Human | | GPT-4 | | GPT-4 | |  
Model | Elo | Rank | Elo | Rank | Elo | Rank | **Median Rank** 
GPT-4 | 1176 | 1 | 1348 | 1 | 1294 | 1 | 1 
Guanaco-65B | 1023 | 2 | 1022 | 2 | 1008 | 3 | 2 
Guanaco-33B | 1009 | 4 | 992 | 3 | 1002 | 4 | 4 
ChatGPT-3.5 Turbo | 916 | 7 | 966 | 5 | 1015 | 2 | 5 
Vicuna-13B | 984 | 5 | 974 | 4 | 936 | 5 | 5 
Guanaco-13B | 975 | 6 | 913 | 6 | 885 | 6 | 6 
Guanaco-7B | 1010 | 3 | 879 | 8 | 860 | 7 | 7 
Bard | 909 | 8 | 902 | 7 | - | - | 8 


We also use the MMLU benchmark to measure performance on a range of language understanding tasks. This is a multiple-choice benchmark covering 57 tasks including elementary mathematics, US history, computer science, law, and more. We report 5-shot test accuracy.

 Dataset | 7B | 13B | 33B | 65B 
---|---|---|---|---
 LLaMA no tuning | 35.1 | 46.9 | 57.8 | 63.4 
 Self-Instruct | 36.4 | 33.3 | 53.0 | 56.7 
 Longform | 32.1 | 43.2 | 56.6 | 59.7 
 Chip2 | 34.5 | 41.6 | 53.6 | 59.8 
 HH-RLHF | 34.9 | 44.6 | 55.8 | 60.1 
 Unnatural Instruct | 41.9 | 48.1 | 57.3 | 61.3 
 OASST1 (Guanaco) | 36.6 | 46.4 | 57.0 | 62.2 
 Alpaca | 38.8 | 47.8 | 57.3 | 62.5 
 FLAN v2 | 44.5 | 51.4 | 59.2 | 63.9 

## Risks and Biases
The model can produce factually incorrect output, and should not be relied on to produce factually accurate information. The model was trained on various public datasets; it is possible that this model could generate lewd, biased, or otherwise offensive outputs.

However, we note that finetuning on OASST1 seems to reduce biases as measured on the CrowS dataset. We report here the performance of Guanaco-65B compared to other baseline models on the CrowS dataset.

|                      | LLaMA-65B | GPT-3 | OPT-175B | Guanaco-65B   |
|----------------------|-----------|-------|----------|---------------|
| Gender               | 70.6      | 62.6  | 65.7     | **47.5** |
| Religion             | {79.0}    | 73.3  | 68.6     | **38.7** |
| Race/Color           | 57.0      | 64.7  | 68.6     | **45.3** |
| Sexual orientation   | {81.0}    | 76.2  | 78.6     | **59.1** |
| Age                  | 70.1      | 64.4  | 67.8     | **36.3** |
| Nationality          | 64.2      | 61.6  | 62.9     | **32.4** |
| Disability           | 66.7      | 76.7  | 76.7     | **33.9** |
| Physical appearance  | 77.8      | 74.6  | 76.2     | **43.1** |
| Socioeconomic status | 71.5      | 73.8  | 76.2     | **55.3** |
| Average              | 66.6      | 67.2  | 69.5     | **43.5** |

## Citation

```bibtex
@article{dettmers2023qlora,
  title={QLoRA: Efficient Finetuning of Quantized LLMs},
  author={Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
  journal={arXiv preprint arXiv:2305.14314},
  year={2023}
}
```
