---
license: mit
---

# Original model: [NousResearch - Obsidian-3B-V0.5](https://huggingface.co/NousResearch/Obsidian-3B-V0.5) 
## gguf q6 quantised version by Nisten
To run the server inside /llama.cpp/ folder IN YOUR TERMINAL 

## ./server -m obsidian-q6.gguf --mmproj mmproj-obsidian-f16.gguf -ngl 42

that's it, it's literally one command, you open your browser now at http://127.0.0.1:8080

## FIRST TIME TO RUN mac or linux, make a new folder, COPY PASTE THIS TO DL & RUN EVERYTHIN whole in ONE SHOT


```bash
git clone -b stablelm-support https://github.com/Galunid/llama.cpp.git && \
cd llama.cpp && \
make && \
wget https://huggingface.co/nisten/obsidian-3b-multimodal-q6-gguf/resolve/main/obsidian-q6.gguf && \
wget https://huggingface.co/nisten/obsidian-3b-multimodal-q6-gguf/resolve/main/mmproj-obsidian-f16.gguf && \
./server -m obsidian-q6.gguf --mmproj mmproj-obsidian-f16.gguf -ngl 42

