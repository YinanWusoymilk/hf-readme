---
language:
- en
library_name: transformers
---
Converted with https://github.com/qwopqwop200/GPTQ-for-LLaMa 
All models tested on A100-80G
*Conversion may require lot of RAM, LLaMA-7b takes ~12 GB, 13b around 21 GB, 30b around 62 and 65b takes more than 120 GB of RAM. 

Installation instructions as mentioned in above repo:
1. Install Anaconda and create a venv with python 3.8
2. Install pytorch(tested with torch-1.13-cu116)
3. Install Transformers library (you'll need the latest transformers with this PR : https://github.com/huggingface/transformers/pull/21955 ).
4. Install sentencepiece from pip
5. Run python cuda_setup.py install in venv
6. You can either convert the llama models yourself with the instructions from GPTQ-for-llama repo
7. or directly use these weights by individually downloading them following these instructions (https://huggingface.co/docs/huggingface_hub/guides/download)
8. Profit!
9. Best results are obtained by putting a repetition_penalty(~1/0.85),temperature=0.7 in model.generate() for most LLaMA models