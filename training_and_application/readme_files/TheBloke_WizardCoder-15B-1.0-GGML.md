---
inference: false
license: bigcode-openrail-m
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

# WizardLM's WizardCoder 15B 1.0 GGML

These files are GGML format model files for [WizardLM's WizardCoder 15B 1.0](https://huggingface.co/WizardLM/WizardCoder-15B-V1.0).

Please note that these GGMLs are **not compatible with llama.cpp, or currently with text-generation-webui**. Please see below for a list of tools known to work with these model files.

## Repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/WizardCoder-15B-1.0-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU+GPU inference](https://huggingface.co/TheBloke/WizardCoder-15B-1.0-GGML)
* [WizardLM's unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/WizardLM/WizardCoder-15B-V1.0)

## Prompt template

```
Below is an instruction that describes a task. Write a response that appropriately completes the request

### Instruction: prompt

### Response:
```

## Live demo

[Matt Hoeffner](https://huggingface.co/matthoffner) has put up a live Space with a demo of this model:

- https://huggingface.co/spaces/matthoffner/wizardcoder-ggml
- 
<!-- compatibility_ggml start -->
## Compatibilty

These files are **not** compatible with llama.cpp.

Currently they can be used with:
* KoboldCpp, a powerful inference engine based on llama.cpp, with good UI: [KoboldCpp](https://github.com/LostRuins/koboldcpp)
* The ctransformers Python library, which includes LangChain support: [ctransformers](https://github.com/marella/ctransformers)
* The GPT4All-UI which uses ctransformers: [GPT4All-UI](https://github.com/ParisNeo/gpt4all-ui)
* [rustformers' llm](https://github.com/rustformers/llm)
* The example `starcoder` binary provided with [ggml](https://github.com/ggerganov/ggml)

As other options become available I will endeavour to update them here (do let me know in the Community tab if I've missed something!)

## Tutorial for using GPT4All-UI

* [Text tutorial, written by **Lucas3DCG**](https://huggingface.co/TheBloke/MPT-7B-Storywriter-GGML/discussions/2#6475d914e9b57ce0caa68888)
* [Video tutorial, by GPT4All-UI's author **ParisNeo**](https://www.youtube.com/watch?v=ds_U0TDzbzI)
<!-- compatibility_ggml end -->

## Provided files
| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| WizardCoder-15B-1.0.ggmlv3.q4_0.bin | q4_0 | 4 | 10.75 GB | 13.25 GB | 4-bit. |
| WizardCoder-15B-1.0.ggmlv3.q4_1.bin | q4_1 | 4 | 11.92 GB | 14.42 GB | 4-bit. Higher accuracy than q4_0 but not as high as q5_0. However has quicker inference than q5 models. |
| WizardCoder-15B-1.0.ggmlv3.q5_0.bin | q5_0 | 5 | 13.09 GB | 15.59 GB | 5-bit. Higher accuracy, higher resource usage and slower inference. |
| WizardCoder-15B-1.0.ggmlv3.q5_1.bin | q5_1 | 5 | 14.26 GB | 16.76 GB | 5-bit. Even higher accuracy, resource usage and slower inference. |
| WizardCoder-15B-1.0.ggmlv3.q8_0.bin | q8_0 | 8 | 20.11 GB | 22.61 GB | 8-bit. Almost indistinguishable from float16. High resource use and slow. Not recommended for most users. |

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

**Patreon special mentions**: Oscar Rangel, Eugene Pentland, Talal Aujan, Cory Kujawski, Luke, Asp the Wyvern, Ai Maven, Pyrater, Alps Aficionado, senxiiz, Willem Michiel, Junyu Yang, trip7s trip, Sebastain Graf, Joseph William Delisle, Lone Striker, Jonathan Leane, Johann-Peter Hartmann, David Flickinger, Spiking Neurons AB, Kevin Schuppel, Mano Prime, Dmitriy Samsonov, Sean Connelly, Nathan LeClaire, Alain Rossmann, Fen Risland, Derek Yates, Luke Pendergrass, Nikolai Manek, Khalefa Al-Ahmad, Artur Olbinski, John Detwiler, Ajan Kanaga, Imad Khwaja, Trenton Dambrowitz, Kalila, vamX, webtim, Illia Dulskyi.

Thank you to all my generous patrons and donaters!

<!-- footer end -->

# Original model card: WizardLM's WizardCoder 15B 1.0

This is the Full-Weight of WizardCoder.

**Repository**: https://github.com/nlpxucan/WizardLM/tree/main/WizardCoder

**Twitter**: https://twitter.com/WizardLM_AI/status/1669109414559911937

**Paper**: Is coming, with brand-new Evol+ methods for code LLMs.

**Demos (Only support code-related English instructions now.)**: 

[Demo](https://8194635813f45a1e.gradio.app/), 
[Backup Demo1](https://375cead61e4db124.gradio.app/), 
[Backup Demo2](https://1594ad375fc80cc7.gradio.app/),
[Backup Demo3](https://4989441110ee350f.gradio.app/)



# WizardCoder: Empowering Code Large Language Models with Evol-Instruct


To develop our WizardCoder model, we begin by adapting the Evol-Instruct method specifically for coding tasks. This involves tailoring the prompt to the domain of code-related instructions. Subsequently, we fine-tune the Code LLM, StarCoder, utilizing the newly created instruction-following training set.

## News

- 🔥 Our **WizardCoder-15B-v1.0** model achieves the **57.3 pass@1** on the [HumanEval Benchmarks](https://github.com/openai/human-eval), which is **22.3** points higher than the SOTA open-source Code LLMs.
- 🔥 We released **WizardCoder-15B-v1.0** trained with **78k** evolved code instructions. Please checkout the [Model Weights](https://huggingface.co/WizardLM/WizardCoder-15B-V1.0), and [Paper]().
- &#x1F4E3; Please refer to our Twitter account https://twitter.com/WizardLM_AI and HuggingFace Repo https://huggingface.co/WizardLM . We will use them to announce any new release at the 1st time. 


## Comparing WizardCoder with the Closed-Source Models.


🔥 The following figure shows that our **WizardCoder attains the third position in this benchmark**, surpassing Claude-Plus (59.8 vs. 53.0) and Bard (59.8 vs. 44.5). Notably, our model exhibits a substantially smaller size compared to these models.

<p align="center" width="100%">
<a ><img src="https://raw.githubusercontent.com/nlpxucan/WizardLM/main/WizardCoder/imgs/pass1.png" alt="WizardCoder" style="width: 86%; min-width: 300px; display: block; margin: auto;"></a>
</p>

❗**Note: In this study, we copy the scores for HumanEval and HumanEval+ from the [LLM-Humaneval-Benchmarks](https://github.com/my-other-github-account/llm-humaneval-benchmarks). Notably, all the mentioned models generate code solutions for each problem utilizing a **single attempt**, and the resulting pass rate percentage is reported. Our **WizardCoder** generates answers using greedy decoding and tests with the same [code](https://github.com/evalplus/evalplus).**

## Comparing WizardCoder with the Open-Source Models.

The following table clearly demonstrates that our **WizardCoder** exhibits a substantial performance advantage over all the open-source models. ❗**If you are confused with the different scores of our model (57.3 and 59.8), please check the Notes.**


| Model            | HumanEval Pass@1 | MBPP Pass@1 |
|------------------|------------------|-------------|
| CodeGen-16B-Multi| 18.3             |20.9         |
| CodeGeeX         | 22.9             |24.4         |
| LLaMA-33B        | 21.7             |30.2         |
| LLaMA-65B        | 23.7             |37.7         |
| PaLM-540B        | 26.2             |36.8         |
| PaLM-Coder-540B  | 36.0             |47.0         |
| PaLM 2-S         | 37.6             |50.0         |
| CodeGen-16B-Mono | 29.3             |35.3         |
| Code-Cushman-001 | 33.5             |45.9         |
| StarCoder-15B    | 33.6             |43.6*        |
| InstructCodeT5+  | 35.0             |--           |
| WizardLM-30B  1.0| 37.8             |--           |
| WizardCoder-15B  1.0 | **57.3**     |**51.8**     |


❗**Note: The reproduced result of StarCoder on MBPP.**

❗**Note: The above table conducts a comprehensive comparison of our **WizardCoder** with other models on the HumanEval and MBPP benchmarks. We adhere to the approach outlined in previous studies by generating **20 samples** for each problem to estimate the pass@1 score and evaluate with the same [code](https://github.com/openai/human-eval/tree/master). The scores of GPT4 and GPT3.5 reported by [OpenAI](https://openai.com/research/gpt-4) are 67.0 and 48.1 (maybe these are the early version GPT4&3.5).**

## Call for Feedbacks
We welcome everyone to use your professional and difficult instructions to evaluate WizardCoder, and show us examples of poor performance and your suggestions in the [issue discussion](https://github.com/nlpxucan/WizardLM/issues) area. We are focusing on improving the Evol-Instruct now and hope to relieve existing weaknesses and issues in the the next version of WizardCoder. After that, we will open the code and pipeline of up-to-date Evol-Instruct algorithm and work with you together to improve it.


## Contents

1. [Online Demo](#online-demo)

2. [Fine-tuning](#fine-tuning)

3. [Inference](#inference)

4. [Evaluation](#evaluation)

5. [Citation](#citation)

6. [Disclaimer](#disclaimer)

## Online Demo

We will provide our latest models for you to try for as long as possible. If you find a link is not working, please try another one. At the same time, please try as many **real-world** and **challenging** code-related problems that you encounter in your work and life as possible. We will continue to evolve our models with your feedbacks.



## Fine-tuning

We fine-tune WizardCoder using the modified code `train.py` from [Llama-X](https://github.com/AetherCortex/Llama-X).
We fine-tune StarCoder-15B with the following hyperparameters:

| Hyperparameter | StarCoder-15B |
|----------------|---------------|
| Batch size     | 512           |
| Learning rate  | 2e-5          |
| Epochs         | 3             |
| Max length     | 2048          |
| Warmup step    | 30            |
| LR scheduler   | cosine        |

To reproduce our fine-tuning of WizardCoder, please follow the following steps:
1. According to the instructions of [Llama-X](https://github.com/AetherCortex/Llama-X), install the environment, download the training code, and deploy. (Note: `deepspeed==0.9.2` and `transformers==4.29.2`)
2. Replace the `train.py` with the `train_wizardcoder.py` in our repo (`src/train_wizardcoder.py`)
3. Login Huggingface:
```bash
huggingface-cli login
```
4. Execute the following training command:
```bash
deepspeed train_wizardcoder.py \
    --model_name_or_path "bigcode/starcoder" \
    --data_path "/your/path/to/code_instruction_data.json" \
    --output_dir "/your/path/to/ckpt" \
    --num_train_epochs 3 \
    --model_max_length 2048 \
    --per_device_train_batch_size 16 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 4 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 50 \
    --save_total_limit 2 \
    --learning_rate 2e-5 \
    --warmup_steps 30 \
    --logging_steps 2 \
    --lr_scheduler_type "cosine" \
    --report_to "tensorboard" \
    --gradient_checkpointing True \
    --deepspeed configs/deepspeed_config.json \
    --fp16 True
```

## Inference

We provide the decoding script for WizardCoder, which reads a input file and generates corresponding responses for each sample, and finally consolidates them into an output file.

You can specify `base_model`, `input_data_path` and `output_data_path` in `src\inference_wizardcoder.py` to set the decoding model, path of input file and path of output file.

```bash
pip install jsonlines
```

The decoding command is:
```
python src\inference_wizardcoder.py \
    --base_model "/your/path/to/ckpt" \
    --input_data_path "/your/path/to/input/data.jsonl" \
    --output_data_path "/your/path/to/output/result.jsonl"
```

The format of `data.jsonl` should be:
```
{"idx": 11, "Instruction": "Write a Python code to count 1 to 10."}
{"idx": 12, "Instruction": "Write a Jave code to sum 1 to 10."}
```

The prompt for our WizardCoder in `src\inference_wizardcoder.py` is:
```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:
```

## Evaluation

We provide the evaluation script on HumanEval for WizardCoder.

1. According to the instructions of [HumanEval](https://github.com/openai/human-eval), install the environment.
2. Run the following script to generate the answer.
```bash
model="/path/to/your/model"
temp=0.2
max_len=2048
pred_num=200
num_seqs_per_iter=2

output_path=preds/T${temp}_N${pred_num}

mkdir -p ${output_path}
echo 'Output path: '$output_path
echo 'Model to eval: '$model

# 164 problems, 21 per GPU if GPU=8
index=0
gpu_num=8
for ((i = 0; i < $gpu_num; i++)); do
  start_index=$((i * 21))
  end_index=$(((i + 1) * 21))

  gpu=$((i))
  echo 'Running process #' ${i} 'from' $start_index 'to' $end_index 'on GPU' ${gpu}
  ((index++))
  (
    CUDA_VISIBLE_DEVICES=$gpu python humaneval_gen.py --model ${model} \
      --start_index ${start_index} --end_index ${end_index} --temperature ${temp} \
      --num_seqs_per_iter ${num_seqs_per_iter} --N ${pred_num} --max_len ${max_len} --output_path ${output_path}
  ) &
  if (($index % $gpu_num == 0)); then wait; fi
done
```
3. Run the post processing code `src/process_humaneval.py` to collect the code completions from all answer files.
```bash
output_path=preds/T${temp}_N${pred_num}

echo 'Output path: '$output_path
python process_humaneval.py --path ${output_path} --out_path ${output_path}.jsonl --add_prompt

evaluate_functional_correctness ${output_path}.jsonl
```

## Citation

Please cite the repo if you use the data or code in this repo.

```
@misc{luo2023wizardcoder,
      title={WizardCoder: Empowering Code Large Language Models with Evol-Instruct}, 
      author={Ziyang Luo and Can Xu and Pu Zhao and Qingfeng Sun and Xiubo Geng and Wenxiang Hu and Chongyang Tao and Jing Ma and Qingwei Lin and Daxin Jiang},
      year={2023},
}
```
## Disclaimer

The resources, including code, data, and model weights, associated with this project are restricted for academic research purposes only and cannot be used for commercial purposes. The content produced by any version of WizardCoder is influenced by uncontrollable variables such as randomness, and therefore, the accuracy of the output cannot be guaranteed by this project. This project does not accept any legal liability for the content of the model output, nor does it assume responsibility for any losses incurred due to the use of associated resources and output results.
