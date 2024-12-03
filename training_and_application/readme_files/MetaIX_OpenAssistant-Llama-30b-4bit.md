<p><strong><font size="5">Information</font></strong></p>
OpenAssistant-Llama-30B-4-bit working with GPTQ versions used in Oobabooga's Text Generation Webui and KoboldAI.

<p>This was made using <a href="https://huggingface.co/OpenAssistant/oasst-sft-7-llama-30b-xor">Open Assistant's native fine-tune</a> of Llama 30b on their dataset.</p>

<p><strong>What's included</strong></p>

<P>GPTQ: 2 quantized versions. One quantized --true-sequential and act-order optimizations, and the other was quantized using --true-sequential --groupsize 128 optimizations</P>
<P>GGML: 3 quantized versions. One quantized using q4_1, another one was quantized using q5_0, and the last one was quantized using q5_1.</P> 

<p><strong><font size="5">Update 05.27.2023</font></strong></p>
<p>Updated the ggml quantizations to be compatible with the latest version of llamacpp (again).</p>

<p><strong><font size="5">Update 04.29.2023</font></strong></p>
<p>Updated to the latest fine-tune by Open Assistant <a href="https://huggingface.co/OpenAssistant/oasst-sft-7-llama-30b-xor">oasst-sft-7-llama-30b-xor</a>.</p>

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

<strong>Wikitext2</strong>: 4.964076519012451

<strong>Ptb-New</strong>: 9.641128540039062

<strong>C4-New</strong>: 7.203001022338867

<strong>Note</strong>: This version does not use <i>--groupsize 128</i>, therefore evaluations are minimally higher. However, this version allows fitting the whole model at full context using only 24GB VRAM.

<p><strong><font size="4">--true-sequential --groupsize 128</font></strong></p>

<strong>Wikitext2</strong>: 4.641914367675781

<strong>Ptb-New</strong>: 9.117929458618164

<strong>C4-New</strong>: 6.867942810058594

<strong>Note</strong>: This version uses <i>--groupsize 128</i>, resulting in better evaluations. However, it consumes more VRAM.