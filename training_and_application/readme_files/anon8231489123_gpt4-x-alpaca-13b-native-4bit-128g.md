
Update (4/1): Added ggml for Cuda model

Dataset is here (instruct): https://github.com/teknium1/GPTeacher

Okay... Two different models now. One generated in the Triton branch, one generated in Cuda. Use the Cuda one for now unless the Triton branch becomes widely used.

Cuda info (use this one):
Command: 

CUDA_VISIBLE_DEVICES=0 python llama.py ./models/chavinlo-gpt4-x-alpaca --wbits 4 --true-sequential --groupsize 128 --save gpt-x-alpaca-13b-native-4bit-128g-cuda.pt


Prev. info

Quantized on GPTQ-for-LLaMa commit 5955e9c67d9bfe8a8144ffbe853c2769f1e87cdd

GPTQ 4bit quantization of: https://huggingface.co/chavinlo/gpt4-x-alpaca

Note: This was quantized with this branch of GPTQ-for-LLaMA: https://github.com/qwopqwop200/GPTQ-for-LLaMa/tree/triton

Because of this, it appears to be incompatible with Oobabooga at the moment. Stay tuned?

Command: 

CUDA_VISIBLE_DEVICES=0 python llama.py ./models/chavinlo-gpt4-x-alpaca --wbits 4 --true-sequential --act-order --groupsize 128 --save gpt-x-alpaca-13b-native-4bit-128g.pt
