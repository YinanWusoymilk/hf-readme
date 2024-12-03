<p><strong><font size="5">Information</font></strong></p>
GPT4-X-Alpaca 30B 4-bit working with GPTQ versions used in Oobabooga's Text Generation Webui and KoboldAI.

<p>This was made using <a href="https://huggingface.co/chansung/gpt4-alpaca-lora-30b">Chansung's GPT4-Alpaca Lora</a></p>

<p><strong><font size="5">Update 05.26.2023</font></strong></p>
<p>Updated the ggml quantizations to be compatible with the latest version of llamacpp (again).</p>

<p><strong>What's included</strong></p>

<P>GPTQ: 2 quantized versions. One quantized --true-sequential and act-order optimizations, and the other was quantized using --true-sequential --groupsize 128 optimizations</P>
<P>GGML: 3 quantized versions. One quantized using q4_1, another one was quantized using q5_0, and the last one was quantized using q5_1.</P> 

<p><strong>GPU/GPTQ Usage</strong></p>
<p>To use with your GPU using GPTQ pick one of the .safetensors along with all of the .jsons and .model files.</p>
<p>Oobabooga: If you require further instruction, see <a href="https://github.com/oobabooga/text-generation-webui/blob/main/docs/GPTQ-models-(4-bit-mode).md">here</a> and <a href="https://github.com/oobabooga/text-generation-webui/blob/main/docs/LLaMA-model.md">here</a></p>
<p>KoboldAI: If you require further instruction, see <a href="https://github.com/0cc4m/KoboldAI">here</a></p>

<p><strong>CPU/GGML Usage</strong></p> 
<p>To use your CPU using GGML(Llamacpp) you only need the single .bin ggml file.</p>
<p>Oobabooga: If you require further instruction, see <a href="https://github.com/oobabooga/text-generation-webui/blob/main/docs/llama.cpp-models.md">here</a></p>
<p>KoboldAI: If you require further instruction, see <a href="https://github.com/LostRuins/koboldcpp">here</a></p>

<p><strong>Training Parameters</strong></p>
<ul><li>num_epochs=10</li><li>cutoff_len=512</li><li>group_by_length</li><li>lora_target_modules='[q_proj,k_proj,v_proj,o_proj]'</li><li>lora_r=16</li><li>micro_batch_size=8</li></ul>

<p><strong><font size="5">Benchmarks</font></strong></p>

<p><strong><font size="4">--true-sequential --act-order</font></strong></p>

<strong>Wikitext2</strong>: 4.481280326843262

<strong>Ptb-New</strong>: 8.539161682128906

<strong>C4-New</strong>: 6.451964855194092

<strong>Note</strong>: This version does not use <i>--groupsize 128</i>, therefore evaluations are minimally higher. However, this version allows fitting the whole model at full context using only 24GB VRAM.

<p><strong><font size="4">--true-sequential --groupsize 128</font></strong></p>

<strong>Wikitext2</strong>: 4.285132884979248

<strong>Ptb-New</strong>: 8.34856128692627

<strong>C4-New</strong>: 6.292652130126953

<strong>Note</strong>: This version uses <i>--groupsize 128</i>, resulting in better evaluations. However, it consumes more VRAM.