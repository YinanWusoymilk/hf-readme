---
license: wtfpl
language:
- en
pipeline_tag: text-generation
tags:
- llama
library_name: adapter-transformers
---

# Alpaca Native Enhanced 7B model download for Alpaca.cpp, Llama.cpp, and Dalai

Use this command to run with llama.cpp
```sh
main -m models/ANE-7B/ggml-model-q4_1.bin -n -1 --ctx_size 2048 --batch_size 16 --keep 512 --repeat_penalty 1.0 -t 16 --temp 0.4 --top_k 30 --top_p 0.18 --interactive-first -ins --color -i -r "User:" -f prompts/alpacanativeenhanced.txt
```

contents of `prompts/alpacanativeenhanced.txt` should be
```txt
You are an AI language model designed to assist the User by answering their questions, offering advice, and engaging in casual conversation in a friendly, helpful, and informative manner. You respond clearly, coherently, and you consider the conversation history.

User: Hey, how's it going?

Assistant: Hey there! I'm doing great, thank you. What can I help you with today? Let's have a fun chat!
```

Original model https://huggingface.co/8bit-coder/alpaca-7b-nativeEnhanced