## MiniCPM-V 2.6

### Prepare models and code

Download [MiniCPM-V-2_6](https://huggingface.co/openbmb/MiniCPM-V-2_6) PyTorch model from huggingface to "MiniCPM-V-2_6" folder.

Clone llama.cpp:
```bash
git clone git@github.com:OpenBMB/llama.cpp.git
cd llama.cpp
git checkout minicpmv-main
```

### Usage of MiniCPM-V 2.6

Convert PyTorch model to gguf files (You can also download the converted [gguf](https://huggingface.co/openbmb/MiniCPM-V-2_6-gguf) by us)

```bash
python ./examples/llava/minicpmv-surgery.py -m ../MiniCPM-V-2_6
python ./examples/llava/minicpmv-convert-image-encoder-to-gguf.py -m ../MiniCPM-V-2_6 --minicpmv-projector ../MiniCPM-V-2_6/minicpmv.projector --output-dir ../MiniCPM-V-2_6/ --image-mean 0.5 0.5 0.5 --image-std 0.5 0.5 0.5 --minicpmv_version 3
python ./convert_hf_to_gguf.py ../MiniCPM-V-2_6/model

# quantize int4 version
./llama-quantize ../MiniCPM-V-2_6/model/ggml-model-f16.gguf ../MiniCPM-V-2_6/model/ggml-model-Q4_K_M.gguf Q4_K_M
```

Build for Linux or Mac

```bash
make
make llama-minicpmv-cli
```

Inference on Linux or Mac
```
# run f16 version
./llama-minicpmv-cli -m ../MiniCPM-V-2_6/model/ggml-model-f16.gguf --mmproj ../MiniCPM-V-2_6/mmproj-model-f16.gguf -c 4096 --temp 0.7 --top-p 0.8 --top-k 100 --repeat-penalty 1.05 --image xx.jpg -p "What is in the image?"

# run quantized int4 version
./llama-minicpmv-cli -m ../MiniCPM-V-2_6/model/ggml-model-Q4_K_M.gguf --mmproj ../MiniCPM-V-2_6/mmproj-model-f16.gguf -c 4096 --temp 0.7 --top-p 0.8 --top-k 100 --repeat-penalty 1.05 --image xx.jpg  -p "What is in the image?"

# or run in interactive mode
./llama-minicpmv-cli -m ../MiniCPM-V-2_6/model/ggml-model-Q4_K_M.gguf --mmproj ../MiniCPM-V-2_6/mmproj-model-f16.gguf -c 4096 --temp 0.7 --top-p 0.8 --top-k 100 --repeat-penalty 1.05 --image xx.jpg -i
```