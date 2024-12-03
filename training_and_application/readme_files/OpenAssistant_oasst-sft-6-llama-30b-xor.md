---
license: other
---

# OpenAssistant LLaMa 30B SFT 6

Due to the license attached to LLaMA models by Meta AI it is not possible to directly distribute LLaMA-based models. Instead we provide XOR weights for the OA models.

Thanks to Mick for writing the `xor_codec.py` script which enables this process

## The Process

Note: This process applies to `oasst-sft-6-llama-30b` model. The same process can be applied to other models in future, but the checksums will be different..

**This process is tested only on Linux (specifically Ubuntu). Some users have reported that the process does not work on Windows. We recommend using WSL if you only have a Windows machine.**

To use OpenAssistant LLaMA-Based Models, you should have a copy of the original LLaMA model weights and add them to a `llama` subdirectory here. If you cannot obtain the original LLaMA, see the note in italic below for a possible alternative.

Ensure your LLaMA 30B checkpoint matches the correct md5sums:

```
f856e9d99c30855d6ead4d00cc3a5573  consolidated.00.pth
d9dbfbea61309dc1e087f5081e98331a  consolidated.01.pth
2b2bed47912ceb828c0a37aac4b99073  consolidated.02.pth
ea0405cdb5bc638fee12de614f729ebc  consolidated.03.pth
4babdbd05b8923226a9e9622492054b6  params.json
```

*If you do not have a copy of the original LLaMA weights and cannot obtain one, you may still be able to complete this process. Some users have reported that [this model](https://huggingface.co/elinas/llama-30b-hf-transformers-4.29) can be used as a base for the XOR conversion. This will also allow you to skip to Step 7. However, we only support conversion starting from LLaMA original checkpoint and cannot provide support if you experience issues with this alternative approach.*

**Important: Follow these exact steps to convert your original LLaMA checkpoint to a HuggingFace Transformers-compatible format. If you use the wrong versions of any dependency, you risk ending up with weights which are not compatible with the XOR files.**

1. Create a clean Python **3.10** virtual environment & activate it:

```
python3.10 -m venv xor_venv
source xor_venv/bin/activate
```

2. Clone transformers repo and switch to tested version:

```
git clone https://github.com/huggingface/transformers.git
cd transformers
git checkout d04ec99bec8a0b432fc03ed60cea9a1a20ebaf3c
pip install .
```

3. Install **exactly** these dependency versions:

```
pip install torch==1.13.1 accelerate==0.18.0 sentencepiece==0.1.98 protobuf==3.20.1
```

4. Check `pip freeze` output:

```
accelerate==0.18.0
certifi==2022.12.7
charset-normalizer==3.1.0
filelock==3.12.0
huggingface-hub==0.13.4
idna==3.4
numpy==1.24.2
nvidia-cublas-cu11==11.10.3.66
nvidia-cuda-nvrtc-cu11==11.7.99
nvidia-cuda-runtime-cu11==11.7.99
nvidia-cudnn-cu11==8.5.0.96
packaging==23.1
protobuf==3.20.1
psutil==5.9.5
PyYAML==6.0
regex==2023.3.23
requests==2.28.2
sentencepiece==0.1.98
tokenizers==0.13.3
torch==1.13.1
tqdm==4.65.0
transformers @ file:///mnt/data/koepf/transformers
typing_extensions==4.5.0
urllib3==1.26.15
```

5. While in `transformers` repo root, run HF LLaMA conversion script:

```
python src/transformers/models/llama/convert_llama_weights_to_hf.py --input_dir <input_path_llama_base>  --output_dir <output_path_llama30b_hf> --model_size 30B
```

6. Run `find . -type f -exec md5sum "{}" +` in the conversion target directory (`output_dir`). This should produce exactly the following checksums if your files are correct:

```
462a2d07f65776f27c0facfa2affb9f9  ./pytorch_model-00007-of-00007.bin
e1dc8c48a65279fb1fbccff14562e6a3  ./pytorch_model-00003-of-00007.bin
9cffb1aeba11b16da84b56abb773d099  ./pytorch_model-00001-of-00007.bin
aee09e21813368c49baaece120125ae3  ./generation_config.json
92754d6c6f291819ffc3dfcaf470f541  ./pytorch_model-00005-of-00007.bin
3eddc6fc02c0172d38727e5826181adb  ./pytorch_model-00004-of-00007.bin
eeec4125e9c7560836b4873b6f8e3025  ./tokenizer.model
99762d59efa6b96599e863893cf2da02  ./pytorch_model-00006-of-00007.bin
598538f18fed1877b41f77de034c0c8a  ./config.json
fdb311c39b8659a5d5c1991339bafc09  ./tokenizer.json
fecfda4fba7bfd911e187a85db5fa2ef  ./pytorch_model.bin.index.json
edd1a5897748864768b1fab645b31491  ./tokenizer_config.json
6b2e0a735969660e720c27061ef3f3d3  ./special_tokens_map.json
5cfcb78b908ffa02e681cce69dbe4303  ./pytorch_model-00002-of-00007.bin
```

**Important: You should now have the correct LLaMA weights and be ready to apply the XORs. If the checksums above do not match yours, there is a problem.**

7. Once you have LLaMA weights in the correct format, you can apply the XOR decoding:

```
python xor_codec.py oasst-sft-6-llama-30b/ oasst-sft-6-llama-30b-xor/oasst-sft-6-llama-30b-xor/ llama30b_hf/
```

You should **expect to see one warning message** during execution:

`Exception when processing 'added_tokens.json'`

This is normal. **If similar messages appear for other files, something has gone wrong**.

8. Now run `find . -type f -exec md5sum "{}" +` in the output directory (here `oasst-sft-6-llama-30b`). You should get a file with exactly these checksums:

```
970e99665d66ba3fad6fdf9b4910acc5  ./pytorch_model-00007-of-00007.bin
659fcb7598dcd22e7d008189ecb2bb42  ./pytorch_model-00003-of-00007.bin
ff6e4cf43ddf02fb5d3960f850af1220  ./pytorch_model-00001-of-00007.bin
27b0dc092f99aa2efaf467b2d8026c3f  ./added_tokens.json
2917a1cafb895cf57e746cfd7696bfe5  ./generation_config.json
740c324ae65b1ec25976643cda79e479  ./pytorch_model-00005-of-00007.bin
f7aefb4c63be2ac512fd905b45295235  ./pytorch_model-00004-of-00007.bin
eeec4125e9c7560836b4873b6f8e3025  ./tokenizer.model
369df2f0e38bda0d9629a12a77c10dfc  ./pytorch_model-00006-of-00007.bin
cc9dbf56b68b68a585cc7367696e06a7  ./config.json
76d47e4f51a8df1d703c6f594981fcab  ./pytorch_model.bin.index.json
fd9452959d711be29ccf04a97598e8d1  ./tokenizer_config.json
785905630a0fe583122a8446a5abe287  ./special_tokens_map.json
ae48c4c68e4e171d502dd0896aa19a84  ./pytorch_model-00002-of-00007.bin
```

If so you have successfully decoded the weights and should be able to use the model with HuggingFace Transformers. **If your checksums do not match those above, there is a problem.**

### Configuration

```
llama-30b-sft-6:
  dtype: fp16
  log_dir: "llama_log_30b"
  learning_rate: 1e-5
  model_name: /home/ubuntu/Open-Assistant/model/model_training/.saved/llama-30b-super-pretrain/checkpoint-3500
  output_dir: llama_model_30b
  deepspeed_config: configs/zero3_config_sft.json
  weight_decay: 0.0
  residual_dropout: 0.0
  max_length: 2048
  use_flash_attention: true
  warmup_steps: 20
  gradient_checkpointing: true
  gradient_accumulation_steps: 16
  per_device_train_batch_size: 2
  per_device_eval_batch_size: 3
  eval_steps: 101
  save_steps: 292
  num_train_epochs: 8
  save_total_limit: 3
  use_custom_sampler: true
  sort_by_length: false
  save_strategy: steps
  datasets:
    - oasst_export:
        lang: "bg,ca,cs,da,de,en,es,fr,hr,hu,it,nl,pl,pt,ro,ru,sl,sr,sv,uk"
        input_file_path: 2023-04-12_oasst_release_ready_synth.jsonl.gz
        val_split: 0.05
    - vicuna:
        val_split: 0.05
        max_val_set: 800
        fraction: 0.8
    - dolly15k:
        val_split: 0.05
        max_val_set: 300
    - grade_school_math_instructions:
        val_split: 0.05
    - code_alpaca:
        val_split: 0.05
        max_val_set: 250
```

- **OASST dataset paper:** https://arxiv.org/abs/2304.07327