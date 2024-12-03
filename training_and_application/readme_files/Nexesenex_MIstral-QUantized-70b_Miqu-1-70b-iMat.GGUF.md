Miqu 1 70b : a leak of Mistral Medium Alpha. Credit for this model goes to the Mistral AI company.

Miqu is probably the best 70b model I could ever play with, especially as a French speaker. Smart like a good Llama 2 70b finetune, no overfitting, little censorship, reasonable alignement, and even a sufficient mastery of French language to have a proper chat in French without feeling like spreaking to a broken bot.


![image/png](https://cdn-uploads.huggingface.co/production/uploads/6451b24dc5d273f95482bfa4/wyeSVsJZ9nijhtuuy4fCC.png)

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/6451b24dc5d273f95482bfa4/PZH8Auv634ob_yMoxbEWf.jpeg)

---

Requantizations with iMatrix (better quality than without) of a Q5_K_M quant of a trending 70b model without better quant/fp16 available, this through a Q8_0 intermediary step.

Miqudev provided Q5_K_M, Q4_K_M, and Q2_K on this page : https://huggingface.co/miqudev/miqu-1-70b

Here, you will find the following quants :

Full offload possible on 48GB VRAM with a huge context size :
- Q4_K_S. Note : A Q5_K_S requant compared to the original Q4_K_M quant of Miqudev wouldn't bring much benefit if any, and take much more VRAM, so I didn't do it.
- Lower quality : Q3_K_L

Full offload possible on 36GB VRAM with a variable context size (up to 7168 with Q3_K_M, for example)
- Q3_K_M, Q3_K_S, Q3_K_XS, IQ3_XXS SOTA (which is equivalent to a Q3_K_S with more context!)
- Lower quality : Q2_K (I remade one with iMatrix, which beats hands-down Miqudev's on perplexity), Q2_K_S

Full offload possible on 24GB VRAM with a decent context size.
- IQ2_XS SOTA
- Lower quality : IQ2_XXS SOTA

Full offload possible on 16GB VRAM with a decent context size.
- IQ1_S (prefer v3 to v2, v2 to v1, etc)

---

Bonus : a Kobold.CPP Frankenstein which reads IQ3_XXS models and is not affected by the Kobold.CPP 1.56/1.57 slowdown at the cost of an absent Mixtral fix.
https://github.com/Nexesenex/kobold.cpp/releases/tag/v1.57_b2030
Now supperseded with another KCPP-F, with 13 different KV cache quantization lebel to chose from :
https://github.com/Nexesenex/kobold.cpp/releases

---

Miku 70b has a theta of 1,000,000, like CodeLlama, and not 10,000, like Llama 2 models usually have.
That feature singularizes it to my knowledge to ALL Llama 2 models, beside Codellamas which also have a theta of 1,000,000..

-> So, no Alpha or Rope Base Frequency change is needed up to its base 32k context, if it works as intended.
And if it does, no linear/yarn rope is necessary either to reach the base 32k context.

BUT Miqu is NOT a CodeLlama 70b (released only a few days after Miqu 70b), because :

- If the Theta of CodeLlama 70b is claimed to be 1,000,000, its base rope actually seems to be 10,000 (see benchs..)
- Which means that CodeLlama might be context limited as Llama 2 is, instead of having a baseline of 100,000 ctx max..
- Meanwhile, Miku's max context is 32k, and not 4k like CodeLlama 70b, and 100,000 like the other CodeLlama.
- And also, Miku's perplexity is close to 70b Llama 2 (less than 4 at 512ctx), while CL 70b is around 5.5 at least.
- Beyond the perplexity, the benchs less sensitive to quantization (Hellaswag, Winogrande, but others as well) confirm this as well..

So, CodeLlama 70b is nerfed like the other CodeLlama in general benchmarks terms, while Miku is matching a FINETUNED Llama-2 expectations.

---

Benchs I made with the original Q2_K quant of Miku 70b, most probably made from an initial FP16 and published by Miqudev :

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6451b24dc5d273f95482bfa4/wiDlIl1FMrVQo0fAcr3YO.png)

A graph, courtesy of Ipechman, with the TQA of WinterGooddess 32k at 39.65728274 and not 20.

Data :

Miqudev's original Q2_K quant :

- miqu-1-70b.q2_K.gguf,-,Hellaswag,86.5,,1000,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,
- miqu-1-70b.q2_K.gguf,-,Hellaswag,86,,2000,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,
- miqu-1-70b.q2_K.gguf,-,Hellaswag_Bin,83.7,,1000,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,
- miqu-1-70b.q2_K.gguf,-,Hellaswag_Bin,84,,2000,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,
- miqu-1-70b.q2_K.gguf,-,Arc-Challenge,56.18729097,,299,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,
- miqu-1-70b.q2_K.gguf,-,Arc-Easy,75.78947368,,570,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,
- miqu-1-70b.q2_K.gguf,-,MMLU,46.96485623,,313,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,
- miqu-1-70b.q2_K.gguf,-,Thruthful-QA,41.49326805,,817,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqude
- miqu-1-70b.q2_K.gguf,-,Winogrande,78.2163,,1267,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,
- miqu-1-70b.q2_K.gguf,-,wikitext,4.6476,512,512,2024-01-29 01:40:00,RBF1000000,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,81
- miqu-1-70b.q2_K.gguf,-,wikitext,4.3063,512,512,2024-01-29 01:40:00,RBF1000000,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,655
- miqu-1-70b.q2_K.gguf,-,wikitext,3.8606,4096,4096,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,655
- miqu-1-70b.q2_K.gguf,-,wikitext,3.6864,6144,6144,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,655

- miqu-1-70b.q2_K.gguf,-,wikitext,4.6576,512,512,2024-01-29 01:40:00,RBF500000,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,81
- miqu-1-70b.q2_K.gguf,-,wikitext,4.7762,512,512,2024-01-29 01:40:00,RBF100000,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,81
- miqu-1-70b.q2_K.gguf,-,wikitext,4.8766,512,512,2024-01-29 01:40:00,RBF50000,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,81
- miqu-1-70b.q2_K.gguf,-,wikitext,5.3367,512,512,2024-01-29 01:40:00,RBF10000,70b,Mistral_Medium,32768,,,GGUF,miqudev,miqudev,81

Benchs I made with the Q2_K I quantized from Miqudev's Q5_K_M with an intermediary Q8_0 step, and an iMatrix of 12800 tokens from wiki.train.raw :

- miqu-1-70b-Requant-b2035-iMat-c32_ch400-Q2_K.gguf,-,Hellaswag,86.8,,1000,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b-Requant-b2035-iMat-c32_ch400-Q2_K.gguf,-,Hellaswag_Bin,83.8,,1000,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b-Requant-b2035-iMat-c32_ch400-Q2_K.gguf,-,Arc-Challenge,56.18729097,,299,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b-Requant-b2035-iMat-c32_ch400-Q2_K.gguf,-,Arc-Easy,76.84210526,,570,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b-Requant-b2035-iMat-c32_ch400-Q2_K.gguf,-,MMLU,49.84025559,,313,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b-Requant-b2035-iMat-c32_ch400-Q2_K.gguf,-,Thruthful-QA,41.37086903,,817,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b-Requant-b2035-iMat-c32_ch400-Q2_K.gguf,-,Winogrande,77.8216,,1267,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b-Requant-b2035-iMat-c32_ch400-Q2_K.gguf,-,wikitext,4.6252,512,512,2024-01-29 01:40:00,RBF1000000,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,81
- miqu-1-70b-Requant-b2035-iMat-c32_ch400-Q2_K.gguf,-,wikitext,4.2173,512,512,2024-01-29 01:40:00,RBF1000000,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,655
- miqu-1-70b-Requant-b2035-iMat-c32_ch400-Q2_K.gguf,-,wikitext,3.6799,4096,4096,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,655
- miqu-1-70b-Requant-b2035-iMat-c32_ch400-Q2_K.gguf,-,wikitext,3.6381,6144,6144,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,655

Notice the perplexity drop brought by the iMatrix despite the requant.

Benchs I made with the Q3_K_M I quantized from Miqudev's Q5_K_M with an intermediary Q8_0 step, and an iMatrix of 12800 tokens from wiki.train.raw :

- miqu-1-70b.Q3_K_M.gguf,-,Hellaswag,88.1,,1000,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.Q3_K_M.gguf,-,Hellaswag,87.3,,2000,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.Q3_K_M.gguf,-,Hellaswag_Bin,85.1,,1000,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.Q3_K_M.gguf,-,Hellaswag_Bin,84.85,,2000,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.Q3_K_M.gguf,-,Arc-Challenge,57.19063545,,299,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.Q3_K_M.gguf,-,Arc-Easy,77.19298246,,570,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.Q3_K_M.gguf,-,MMLU,50.15974441,,313,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.Q3_K_M.gguf,-,Thruthful-QA,41.49326805,,817,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.Q3_K_M.gguf,-,Winogrande,78.8477,,1267,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.Q3_K_M.gguf,-,wikitext,4.2957,512,512,2024-01-29 01:40:00,RBF1000000,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,81
- miqu-1-70b.Q3_K_M.gguf,-,wikitext,3.8380,512,512,2024-01-29 01:40:00,RBF1000000,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,655

And now, the IQ3_XXS, new SOTA 3 bits quant from LlamaCPP, that I made in the same way :

- miqu-1-70b.IQ3_XXS.gguf,-,Hellaswag,88.3,,1000,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.IQ3_XXS.gguf,-,Hellaswag_Bin,85,,1000,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.IQ3_XXS.gguf,-,Arc-Challenge,55.85284281,,299,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.IQ3_XXS.gguf,-,Arc-Easy,78.59649123,,570,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.IQ3_XXS.gguf,-,MMLU,48.88178914,,313,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.IQ3_XXS.gguf,-,Thruthful-QA,41.73806610,,817,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.IQ3_XXS.gguf,-,Winogrande,78.3741,,1267,2024-01-29 05:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,
- miqu-1-70b.IQ3_XXS.gguf,-,wikitext,4.4319,512,512,2024-01-29 01:40:00,RBF1000000,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,81
- miqu-1-70b.IQ3_XXS.gguf,-,wikitext,4.0309,512,512,2024-01-29 01:40:00,RBF1000000,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,655
- miqu-1-70b.IQ3_XXS.gguf,-,wikitext,3.5141,4096,4096,2024-01-29 01:40:00,,70b,Mistral_Medium,32768,,,GGUF,miqudev,Nexesenex,

---

Meanwhile, CodeLlama 70b Q2_K benches as such, to compare with Miqu 70B Q2_K originally quantized from FP16 by Miqudev :

- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,Hellaswag,76.2,,1000,2024-01-30 01:40:00,,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,Hellaswag_Bin,72.5,,1000,2024-01-30 01:40:00,,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,Arc-Challenge,35.11705686,,299,2024-01-30 05:40:00,,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,Arc-Easy,58.77192982,,570,2024-01-30 05:40:00,,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,MMLU,36.10223642,,313,2024-01-30 05:40:00,,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,Thruthful-QA,31.08935129,,817,2024-01-30 05:40:00,,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,Winogrande,70.3236,,1267,2024-01-30 05:40:00,,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,wikitext,6.4634,512,512,2024-01-30 01:40:00,RBF10000,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,655
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,wikitext,9.7866,512,512,2024-01-30 01:40:00,RBF1000000,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,81
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,wikitext,8.5822,512,512,2024-01-30 01:40:00,RBF500000,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,81
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,wikitext,7.1098,512,512,2024-01-30 01:40:00,RBF100000,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,81
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,wikitext,6.8224,512,512,2024-01-30 01:40:00,RBF50000,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,81
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,wikitext,6.5705,512,512,2024-01-30 01:40:00,RBF10000,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,81
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,wikitext,5.6064,4096,4096,2024-01-30 01:40:00,,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,
- CodeLlama-70b-Instruct-hf-Q2_K.gguf,-,wikitext,153.5606,6144,6144,2024-01-30 01:40:00,,70b,CodeLlama,32768,,,GGUF,Meta,Lonestriker,

---

And, for information, a comparable base Llama 2 70b finetuned by NousResearch for 32k context (Yarn) :

- Yarn-Llama-2-70b-32k-Q3_K_S.gguf,-,Hellaswag,87,400,,2024-01-23 01:40:00,PEC8,70b,Llama_2,4096,,,GGUF,Meta,Artefact2,
- Yarn-Llama-2-70b-32k-Q3_K_S.gguf,-,Hellaswag_Bin,81.25,,400,2024-01-23 01:40:00,PEC8,70b,Llama_2,4096,,,GGUF,Meta,Artefact2,
- Yarn-Llama-2-70b-32k-Q3_K_S.gguf,-,Arc-Challenge,43.81270903,,299,2024-01-23 05:40:00,PEC8,70b,Llama_2,4096,,,GGUF,Meta,Artefact2,
- Yarn-Llama-2-70b-32k-Q3_K_S.gguf,-,Arc-Easy,65.6140,24.9890,570,2024-01-23 05:40:00,PEC8,70b,Llama_2,4096,,,GGUF,Meta,Artefact2,
- Yarn-Llama-2-70b-32k-IQ2_XS.gguf,-,MMLU,36.06557377,,1159,2024-01-24 05:40:00,PEC8,70b,Llama_2,4096,,,GGUF,Meta,Artefact2,
- Yarn-Llama-2-70b-32k-Q3_K_S.gguf,-,Thruthful-QA,30.72215422,19.8590,817,2024-01-23 05:40:00,PEC8,70b,Llama_2,4096,,,GGUF,Meta,Artefact2,
- Yarn-Llama-2-70b-32k-Q3_K_S.gguf,-,Winogrande,78.1373,,1267,2024-01-23 05:40:00,PEC8,70b,Llama_2,4096,,,GGUF,Meta,Artefact2,
- Yarn-Llama-2-70b-32k-Q3_K_S.gguf,-,wikitext,3.6948,512,512,2024-01-23 01:40:00,PEC8,70b,Llama_2,4096,,,GGUF,Meta,Artefact2,

This yarn version performs closely to Llama 2 70b (but with 32k max context), and.. Much more poorly than Miqu 70b.

---

Also, for information, another requant from a Q4_K_S orphan of a 32k finetune of Sao10K's WinterGoddess 70b At Linear rope 2.5 (for 10k context) :

- WinterGoddess-1.4x-limarpv3-70B-L2-32k-Requant-AR-b1952-iMat-c32_ch2500-Q3_K_XS.gguf,-,Hellaswag,89.25,,400,2024-01-23 01:40:00,PEC2.5,70b,Llama_2,4096,,,GGUF,Mishima,Nexesenex,
- WinterGoddess-1.4x-limarpv3-70B-L2-32k-Requant-AR-b1952-iMat-c32_ch2500-Q3_K_XS.gguf,-,Hellaswag_Bin,84,,400,2024-01-23 01:40:00,PEC2.5,70b,Llama_2,4096,,,GGUF,Mishima,Nexesenex,
- WinterGoddess-1.4x-limarpv3-70B-L2-32k-Requant-AR-b1952-iMat-c32_ch2500-Q3_K_XS.gguf,-,Arc-Challenge,54.84949833,,299,2024-01-23 05:40:00,PEC2.5,70b,Llama_2,4096,,,GGUF,Mishima,Nexesenex,
- WinterGoddess-1.4x-limarpv3-70B-L2-32k-Requant-AR-b1952-iMat-c32_ch2500-Q3_K_XS.gguf,-,Arc-Easy,74.03508772,,570,2024-01-23 05:40:00,PEC2.5,70b,Llama_2,4096,,,GGUF,Mishima,Nexesenex,
- WinterGoddess-1.4x-limarpv3-70B-L2-32k-Requant-AR-b1952-iMat-c32_ch2500-Q3_K_XS.gguf,-,Thruthful-QA,39.65728274,19.8590,817,2024-01-23 05:40:00,PEC2.5,70b,Llama_2,4096,,,GGUF,Mishima,Nexesenex,
- WinterGoddess-1.4x-limarpv3-70B-L2-32k-Requant-AR-b1952-iMat-c32_ch2500-Q3_K_XS.gguf,-,Winogrande,77.8216,,1267,2024-01-23 05:40:00,PEC2.5,70b,Llama_2,4096,,,GGUF,Mishima,Nexesenex,
- WinterGoddess-1.4x-limarpv3-70B-L2-32k-Requant-AR-b1952-iMat-c32_ch2500-Q3_K_XS.gguf,-,wikitext,4.2327,512,512,2024-01-23 01:40:00,PEC2.5,70b,Llama_2,4096,,,GGUF,Mishima,Nexesenex,

Draw your own conclusions as well !

---- 

New quants IQ1 :

V3 :

- miqu-1-70b-Requant-b2131-iMat-c32_ch400-IQ1_S_v3.gguf,-,Hellaswag,78.1,1000,,2024-02-12 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2131-iMat-c32_ch400-IQ1_S_v3.gguf,-,Arc-Challenge,45.15050167,,299,2024-02-12 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2131-iMat-c32_ch400-IQ1_S_v3.gguf,-,Arc-Easy,70.70175439,,570,2024-02-12 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2131-iMat-c32_ch400-IQ1_S_v3.gguf,-,MMLU,38.97763578,,313,2024-02-12 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2131-iMat-c32_ch400-IQ1_S_v3.gguf,-,Thruthful-QA,33.29253366,,817,2024-02-12 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2131-iMat-c32_ch400-IQ1_S_v3.gguf,-,Winogrande,72.2178,,1267,2024-02-12 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2131-iMat-c32_ch400-IQ1_S_v3.gguf,-,wikitext,6.7606,512,512,2024-02-12 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2131-iMat-c32_ch400-IQ1_S_v3.gguf,-,wikitext,5.5886,4096,4096,2024-02-12 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2131-iMat-c32_ch400-IQ1_S_v3.gguf,-,wikitext,5.5291,8192,8192,2024-02-12 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,

V5 :

- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_S_v5.gguf,-,Hellaswag,80.6,1000,,2024-03-13 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_S_v5.gguf,-,Arc-Challenge,46.48829431,,299,2024-03-13 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_S_v5.gguf,-,Arc-Easy,71.22807018,,570,2024-03-13 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_S_v5.gguf,-,MMLU,41.85303514,,313,2024-03-13 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_S_v5.gguf,-,Thruthful-QA,34.14932681,,817,2024-03-13 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_S_v5.gguf,-,Winogrande,73.9542,,1267,2024-03-13 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_S_v5.gguf,-,wikitext,6.2547,512,512,2024-03-13 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_S_v5.gguf,-,wikitext,5.2290,4096,4096,2024-03-13 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,

-----

CUSTOM QUANTS :

New quantizations strategies to bundle optimally the last tensor quantizations of Ikawrakow (LlamaCPP b2404 and beyond) and reach the hightest possible quality/size ratio.
A work in progress. These quants strategies will be updated as soon as higher IQ tensor quants are available for the pertinent tensors.

Here's one new quant strategy, currently labelled IQ1_FSR, a 2% smaller quant than .IQ1_S v3/v5 with a quality slightly above IQ1_S_v3 but quite a bit lower than IQ1_S_v5 :

- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_FS.gguf,-,Hellaswag,79.9,1000,,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_FS.gguf,-,Arc-Challenge,50.16722408,,299,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_FS.gguf,-,Arc-Easy,69.47368421,,570,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_FS.gguf,-,MMLU,39.29712460,,313,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_FS.gguf,-,Thruthful-QA,34.27172583,,817,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_FS.gguf,-,Winogrande,72.2178,,1267,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_FS.gguf,-,wikitext,6.4324,512,512,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_FS.gguf,-,wikitext,5.3399,4096,4096,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,

Second new quant strategy, currently labelled IQ1_PS, a 0.5% bigger quant than .IQ1_S v3/v5 with a quality a bit above with IQ1_S_v5 :

- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_PS.gguf,-,Hellaswag,80.5,1000,,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_PS.gguf,-,Arc-Challenge,49.16387960,,299,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_PS.gguf,-,Arc-Easy,72.45614035,,570,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_PS.gguf,-,MMLU,43.45047923,,313,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_PS.gguf,-,Thruthful-QA,33.90452876,,817,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_PS.gguf,-,Winogrande,74.3489,,1267,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_PS.gguf,-,wikitext,6.1692,512,512,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_PS.gguf,-,wikitext,5.1600,4096,4096,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,

And 4 bigger IQ1 quants, up to 1.92 bpw :

IQ1_NS :

- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_NS.gguf,-,Hellaswag,80.8,1000,,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_NS.gguf,-,Arc-Challenge,47.49163880,,299,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_NS.gguf,-,Arc-Easy,73.15789474,,570,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_NS.gguf,-,MMLU,45.04792332,,313,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_NS.gguf,-,Thruthful-QA,33.90452876,,817,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_NS.gguf,-,Winogrande,74.2699,,1267,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_NS.gguf,-,wikitext,6.0276,512,512,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_NS.gguf,-,wikitext,5.0610,4096,4096,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,

IQ1_MS :

- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_MS.gguf,-,Hellaswag,81.7,1000,,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_MS.gguf,-,Arc-Challenge,49.49832776,,299,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_MS.gguf,-,Arc-Easy,75.61403509,,570,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_MS.gguf,-,MMLU,44.40894569,,313,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_MS.gguf,-,Thruthful-QA,36.71970624,,817,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_MS.gguf,-,Winogrande,74.9803,,1267,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_MS.gguf,-,wikitext,5.7734,512,512,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_MS.gguf,-,wikitext,4.8859,4096,4096,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,

IQ1_ES :

- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_ES.gguf,-,Hellaswag,82.5,1000,,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_ES.gguf,-,Arc-Challenge,50.50167224,,299,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_ES.gguf,-,Arc-Easy,74.73684211,,570,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_ES.gguf,-,MMLU,46.00638978,,313,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_ES.gguf,-,Thruthful-QA,36.10771114,,817,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_ES.gguf,-,Winogrande,74.4278,,1267,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_ES.gguf,-,wikitext,5.6421,512,512,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_ES.gguf,-,wikitext,4.7946,4096,4096,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,

IQ1_SR :

- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_SR.gguf,-,Hellaswag,83.6,1000,,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_SR.gguf,-,Arc-Challenge,50.83612040,,299,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_SR.gguf,-,Arc-Easy,74.73684211,,570,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_SR.gguf,-,MMLU,46.32587859,,313,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_SR.gguf,-,Thruthful-QA,36.71970624,,817,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_SR.gguf,-,Winogrande,75.8485,,1267,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_SR.gguf,-,wikitext,5.4279,512,512,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,
- miqu-1-70b-Requant-b2409-iMat-c512_ch600-IQ1_SR.gguf,-,wikitext,4.6538,4096,4096,2024-03-14 00:00:00,,70b,Mistral_Medium,32768,,,GGUF,Miqudev,Nexesenex,