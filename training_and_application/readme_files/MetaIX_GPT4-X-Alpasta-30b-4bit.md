<p><strong><font size="5">Information</font></strong></p>
GPT4-X-Alpasta-30b working with Oobabooga's Text Generation Webui and KoboldAI.
<p>This is an attempt at improving Open Assistant's performance as an instruct while retaining its excellent prose. The merge consists of <a href="https://huggingface.co/chansung/gpt4-alpaca-lora-30b">Chansung's GPT4-Alpaca Lora</a> and <a href="https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor">Open Assistant's native fine-tune</a>.</p>

<p><strong><font size="5">Update 05.27.2023</font></strong></p>
<p>Updated the ggml quantizations to be compatible with the latest version of llamacpp (again).</p>

<p><strong>What's included</strong></p>

<P>GPTQ: 2 quantized versions. One quantized --true-sequential and act-order optimizations, and the other was quantized using --true-sequential --groupsize 128 optimizations.</P>
<P>GGML: 3 quantized versions. One quantized using q4_1, another was quantized using q5_0, and the last one was quantized using q5_1.</P> 

<p><strong>GPU/GPTQ Usage</strong></p>
<p>To use with your GPU using GPTQ pick one of the .safetensors along with all of the .jsons and .model files.</p>
<p>Oobabooga: If you require further instruction, see <a href="https://github.com/oobabooga/text-generation-webui/blob/main/docs/GPTQ-models-(4-bit-mode).md">here</a> and <a href="https://github.com/oobabooga/text-generation-webui/blob/main/docs/LLaMA-model.md">here</a></p>
<p>KoboldAI: If you require further instruction, see <a href="https://github.com/0cc4m/KoboldAI">here</a></p>

<p><strong>CPU/GGML Usage</strong></p> 
<p>To use your CPU using GGML(Llamacpp) you only need the single .bin ggml file.</p>
<p>Oobabooga: If you require further instruction, see <a href="https://github.com/oobabooga/text-generation-webui/blob/main/docs/llama.cpp-models.md">here</a></p>
<p>KoboldAI: If you require further instruction, see <a href="https://github.com/LostRuins/koboldcpp">here</a></p>

<p><strong><font size="5">Benchmarks</font></strong></p>

<p><strong><font size="4">--true-sequential --act-order</font></strong></p>

<strong>Wikitext2</strong>: 4.998758792877197

<strong>Ptb-New</strong>: 9.802155494689941

<strong>C4-New</strong>: 7.341384410858154

<strong>Note</strong>: This version does not use <i>--groupsize 128</i>, therefore evaluations are minimally higher. However, this version allows fitting the whole model at full context using only 24GB VRAM.

<p><strong><font size="4">--true-sequential --groupsize 128</font></strong></p>

<strong>Wikitext2</strong>: 4.70257568359375

<strong>Ptb-New</strong>: 9.323467254638672

<strong>C4-New</strong>: 7.041860580444336

<strong>Note</strong>: This version uses <i>--groupsize 128</i>, resulting in better evaluations. However, it consumes more VRAM.