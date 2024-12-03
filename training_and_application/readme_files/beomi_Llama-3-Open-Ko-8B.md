---
language:
- en
- ko
license: other
tags:
- facebook
- meta
- pytorch
- llama
- llama-3
- llama-3-ko
pipeline_tag: text-generation
license_name: llama3
license_link: LICENSE
---

> Update @ 2024.05.20: Re-Upload RoPE fixed model

> Update @ 2024.05.01: Pre-Release [Llama-3-KoEn-8B](https://huggingface.co/beomi/Llama-3-KoEn-8B-preview) model & [Llama-3-KoEn-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-KoEn-8B-Instruct-preview)

> Update @ 2024.04.24: Release Llama-3-Open-Ko-8B model & [Llama-3-Open-Ko-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-Open-Ko-8B-Instruct-preview)

## Model Details

**Llama-3-Open-Ko-8B**

Llama-3-Open-Ko-8B model is continued pretrained language model based on Llama-3-8B.

This model is trained fully with publicily available resource, with 60GB+ of deduplicated texts.

With the new Llama-3 tokenizer, the pretraining conducted with 17.7B+ tokens, which slightly more than Korean tokenizer(Llama-2-Ko tokenizer).

The train was done on TPUv5e-256, with the warm support from TRC program by Google.

**Note for [Llama-3-Open-Ko-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-Open-Ko-8B-Instruct-preview)**

With applying the idea from [Chat Vector paper](https://arxiv.org/abs/2310.04799), I released Instruction model named [Llama-3-Open-Ko-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-Open-Ko-8B-Instruct-preview).

Since it is NOT finetuned with any Korean instruction set(indeed `preview`), but it would be great starting point for creating new Chat/Instruct models.

**Meta Llama-3**

Meta developed and released the Meta Llama 3 family of large language models (LLMs), a collection of pretrained and instruction tuned generative text models in 8 and 70B sizes. The Llama 3 instruction tuned models are optimized for dialogue use cases and outperform many of the available open source chat models on common industry benchmarks. Further, in developing these models, we took great care to optimize helpfulness and safety. 

**Model developers** Junbum Lee (Beomi)

**Variations** Llama-3-Open-Ko comes in one size — 8B.

**Input** Models input text only.

**Output** Models generate text and code only.

**Model Architecture** Llama 3 is an auto-regressive language model that uses an optimized transformer architecture. 

<table>
  <tr>
   <td>
   </td>
   <td><strong>Training Data</strong>
   </td>
   <td><strong>Params</strong>
   </td>
   <td><strong>Context length</strong>
   </td>
   <td><strong>GQA</strong>
   </td>
   <td><strong>Token count</strong>
   </td>
   <td><strong>Knowledge cutoff</strong>
   </td>
  </tr>
  <tr>
   <td rowspan="2" >Llama-3-Open-Ko
   </td>
   <td rowspan="2" >Same as *Open-Solar-Ko Dataset
   </td>
   <td>8B
   </td>
   <td>8k
   </td>
   <td>Yes
   </td>
   <td rowspan="2" >17.7B+
   </td>
   <td>Jun, 2023
   </td>
  </tr>
</table>

*You can find dataset list here: https://huggingface.co/beomi/OPEN-SOLAR-KO-10.7B/tree/main/corpus


**Model Release Date** 2024.04.24.

**Status** This is a static model trained on an offline dataset.

**License** Llama3 License: [https://llama.meta.com/llama3/license](https://llama.meta.com/llama3/license)

## Intended Use

**Intended Use Cases** Llama 3 is intended for commercial and research use in English. Instruction tuned models are intended for assistant-like chat, whereas pretrained models can be adapted for a variety of natural language generation tasks.

**Out-of-scope** Use in any manner that violates applicable laws or regulations (including trade compliance laws). Use in any other way that is prohibited by the Acceptable Use Policy and Llama 3 Community License. Use in languages other than English**.

**Note: Developers may fine-tune Llama 3 models for languages beyond English provided they comply with the Llama 3 Community License and the Acceptable Use Policy.

## How to use

TBD

### Responsibility & Safety

We believe that an open approach to AI leads to better, safer products, faster innovation, and a bigger overall market. We are committed to Responsible AI development and took a series of steps to limit misuse and harm and support the open source community.

Foundation models are widely capable technologies that are built to be used for a diverse range of applications. They are not designed to meet every developer preference on safety levels for all use cases, out-of-the-box, as those by their nature will differ across different applications. 

Rather, responsible LLM-application deployment is achieved by implementing a series of safety best practices throughout the development of such applications, from the model pre-training, fine-tuning and the deployment of systems composed of safeguards to tailor the safety needs specifically to the use case and audience. 


As part of the Llama 3 release, we updated our [Responsible Use Guide](https://llama.meta.com/responsible-use-guide/) to outline the steps and best practices for developers to implement model and system level safety for their application. We also provide a set of resources including [Meta Llama Guard 2](https://llama.meta.com/purple-llama/) and [Code Shield](https://llama.meta.com/purple-llama/) safeguards. These tools have proven to drastically reduce residual risks of LLM Systems, while maintaining a high level of helpfulness. We encourage developers to tune and deploy these safeguards according to their needs and we provide a [reference implementation](https://github.com/meta-llama/llama-recipes/tree/main/recipes/responsible_ai) to get you started.


#### Responsible release 

In addition to responsible use considerations outlined above, we followed a rigorous process that requires us to take extra measures against misuse and critical risks before we make our release decision. 

Misuse

If you access or use Llama 3, you agree to the Acceptable Use Policy. The most recent copy of this policy can be found at [https://llama.meta.com/llama3/use-policy/](https://llama.meta.com/llama3/use-policy/).


## Ethical Considerations and Limitations

The core values of Llama 3 are openness, inclusivity and helpfulness. It is meant to serve everyone, and to work for a wide range of use cases. It is thus designed to be accessible to people across many different backgrounds, experiences and perspectives. Llama 3 addresses users and their needs as they are, without insertion unnecessary judgment or normativity, while reflecting the understanding that even content that may appear problematic in some cases can serve valuable purposes in others. It respects the dignity and autonomy of all users, especially in terms of the values of free thought and expression that power innovation and progress. 

But Llama 3 is a new technology, and like any new technology, there are risks associated with its use. Testing conducted to date has been in English, and has not covered, nor could it cover, all scenarios. For these reasons, as with all LLMs, Llama 3’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 3 models, developers should perform safety testing and tuning tailored to their specific applications of the model. As outlined in the Responsible Use Guide, we recommend incorporating [Purple Llama](https://github.com/facebookresearch/PurpleLlama) solutions into your workflows and specifically [Llama Guard](https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/) which provides a base model to filter input and output prompts to layer system-level safety on top of model-level safety. 

Please see the Responsible Use Guide available at [http://llama.meta.com/responsible-use-guide](http://llama.meta.com/responsible-use-guide)

## Benchmark Scores

- vllm (pretrained=beomi/Llama-3-Open-Ko-8B,revision=081e85a,tensor_parallel_size=1,dtype=bfloat16,data_parallel_size=2,gpu_memory_utilization=0.8), gen_kwargs: (None), limit: None, num_fewshot: 5, batch_size: auto

|                          Tasks                           |Version|Filter|n-shot|  Metric   |Value |   |Stderr|
|----------------------------------------------------------|-------|------|-----:|-----------|-----:|---|------|
|haerae                                                    |N/A    |none  |     5|acc        |0.6801|±  |0.0138|
|                                                          |       |none  |     5|acc_norm   |0.6801|±  |0.0138|
| - haerae_general_knowledge                               |      1|none  |     5|acc        |0.4375|±  |0.0375|
|                                                          |       |none  |     5|acc_norm   |0.4375|±  |0.0375|
| - haerae_history                                         |      1|none  |     5|acc        |0.7340|±  |0.0323|
|                                                          |       |none  |     5|acc_norm   |0.7340|±  |0.0323|
| - haerae_loan_word                                       |      1|none  |     5|acc        |0.7870|±  |0.0316|
|                                                          |       |none  |     5|acc_norm   |0.7870|±  |0.0316|
| - haerae_rare_word                                       |      1|none  |     5|acc        |0.7012|±  |0.0228|
|                                                          |       |none  |     5|acc_norm   |0.7012|±  |0.0228|
| - haerae_standard_nomenclature                           |      1|none  |     5|acc        |0.7190|±  |0.0365|
|                                                          |       |none  |     5|acc_norm   |0.7190|±  |0.0365|
|kmmlu_direct                                              |N/A    |none  |     5|exact_match|0.4054|±  |0.0026|
| - kmmlu_direct_accounting                                |      2|none  |     5|exact_match|0.3600|±  |0.0482|
| - kmmlu_direct_agricultural_sciences                     |      2|none  |     5|exact_match|0.3130|±  |0.0147|
| - kmmlu_direct_aviation_engineering_and_maintenance      |      2|none  |     5|exact_match|0.3690|±  |0.0153|
| - kmmlu_direct_biology                                   |      2|none  |     5|exact_match|0.3330|±  |0.0149|
| - kmmlu_direct_chemical_engineering                      |      2|none  |     5|exact_match|0.4190|±  |0.0156|
| - kmmlu_direct_chemistry                                 |      2|none  |     5|exact_match|0.3833|±  |0.0199|
| - kmmlu_direct_civil_engineering                         |      2|none  |     5|exact_match|0.3870|±  |0.0154|
| - kmmlu_direct_computer_science                          |      2|none  |     5|exact_match|0.6340|±  |0.0152|
| - kmmlu_direct_construction                              |      2|none  |     5|exact_match|0.3340|±  |0.0149|
| - kmmlu_direct_criminal_law                              |      2|none  |     5|exact_match|0.2850|±  |0.0320|
| - kmmlu_direct_ecology                                   |      2|none  |     5|exact_match|0.4210|±  |0.0156|
| - kmmlu_direct_economics                                 |      2|none  |     5|exact_match|0.4077|±  |0.0433|
| - kmmlu_direct_education                                 |      2|none  |     5|exact_match|0.5000|±  |0.0503|
| - kmmlu_direct_electrical_engineering                    |      2|none  |     5|exact_match|0.3620|±  |0.0152|
| - kmmlu_direct_electronics_engineering                   |      2|none  |     5|exact_match|0.4790|±  |0.0158|
| - kmmlu_direct_energy_management                         |      2|none  |     5|exact_match|0.3110|±  |0.0146|
| - kmmlu_direct_environmental_science                     |      2|none  |     5|exact_match|0.3210|±  |0.0148|
| - kmmlu_direct_fashion                                   |      2|none  |     5|exact_match|0.4190|±  |0.0156|
| - kmmlu_direct_food_processing                           |      2|none  |     5|exact_match|0.3600|±  |0.0152|
| - kmmlu_direct_gas_technology_and_engineering            |      2|none  |     5|exact_match|0.3320|±  |0.0149|
| - kmmlu_direct_geomatics                                 |      2|none  |     5|exact_match|0.3640|±  |0.0152|
| - kmmlu_direct_health                                    |      2|none  |     5|exact_match|0.5100|±  |0.0502|
| - kmmlu_direct_industrial_engineer                       |      2|none  |     5|exact_match|0.3970|±  |0.0155|
| - kmmlu_direct_information_technology                    |      2|none  |     5|exact_match|0.5720|±  |0.0157|
| - kmmlu_direct_interior_architecture_and_design          |      2|none  |     5|exact_match|0.4740|±  |0.0158|
| - kmmlu_direct_korean_history                            |      2|none  |     5|exact_match|0.2700|±  |0.0446|
| - kmmlu_direct_law                                       |      2|none  |     5|exact_match|0.3990|±  |0.0155|
| - kmmlu_direct_machine_design_and_manufacturing          |      2|none  |     5|exact_match|0.4080|±  |0.0155|
| - kmmlu_direct_management                                |      2|none  |     5|exact_match|0.4660|±  |0.0158|
| - kmmlu_direct_maritime_engineering                      |      2|none  |     5|exact_match|0.4417|±  |0.0203|
| - kmmlu_direct_marketing                                 |      2|none  |     5|exact_match|0.6720|±  |0.0149|
| - kmmlu_direct_materials_engineering                     |      2|none  |     5|exact_match|0.4130|±  |0.0156|
| - kmmlu_direct_math                                      |      2|none  |     5|exact_match|0.2567|±  |0.0253|
| - kmmlu_direct_mechanical_engineering                    |      2|none  |     5|exact_match|0.3800|±  |0.0154|
| - kmmlu_direct_nondestructive_testing                    |      2|none  |     5|exact_match|0.3890|±  |0.0154|
| - kmmlu_direct_patent                                    |      2|none  |     5|exact_match|0.2700|±  |0.0446|
| - kmmlu_direct_political_science_and_sociology           |      2|none  |     5|exact_match|0.4433|±  |0.0287|
| - kmmlu_direct_psychology                                |      2|none  |     5|exact_match|0.3620|±  |0.0152|
| - kmmlu_direct_public_safety                             |      2|none  |     5|exact_match|0.3200|±  |0.0148|
| - kmmlu_direct_railway_and_automotive_engineering        |      2|none  |     5|exact_match|0.3200|±  |0.0148|
| - kmmlu_direct_real_estate                               |      2|none  |     5|exact_match|0.3650|±  |0.0341|
| - kmmlu_direct_refrigerating_machinery                   |      2|none  |     5|exact_match|0.3210|±  |0.0148|
| - kmmlu_direct_social_welfare                            |      2|none  |     5|exact_match|0.4500|±  |0.0157|
| - kmmlu_direct_taxation                                  |      2|none  |     5|exact_match|0.3550|±  |0.0339|
| - kmmlu_direct_telecommunications_and_wireless_technology|      2|none  |     5|exact_match|0.5490|±  |0.0157|
|kobest_boolq                                              |      1|none  |     5|acc        |0.7984|±  |0.0107|
|                                                          |       |none  |     5|f1         |0.7961|±  |N/A   |
|kobest_copa                                               |      1|none  |     5|acc        |0.8150|±  |0.0123|
|                                                          |       |none  |     5|f1         |0.8148|±  |N/A   |
|kobest_hellaswag                                          |      1|none  |     5|acc        |0.4800|±  |0.0224|
|                                                          |       |none  |     5|f1         |0.4771|±  |N/A   |
|                                                          |       |none  |     5|acc_norm   |0.6120|±  |0.0218|
|kobest_sentineg                                           |      1|none  |     5|acc        |0.9597|±  |0.0099|
|                                                          |       |none  |     5|f1         |0.9597|±  |N/A   |
|haerae      |N/A    |none  |     5|acc        |0.6801|±  |0.0138|
|            |       |none  |     5|acc_norm   |0.6801|±  |0.0138|
|kmmlu_direct|N/A    |none  |     5|exact_match|0.4054|±  |0.0026|


## Citation instructions

**Llama-3-Open-Ko**

```
@article{llama3openko,
  title={Llama-3-Open-Ko},
  author={L, Junbum},
  year={2024},
  url={https://huggingface.co/beomi/Llama-3-Open-Ko-8B}
}
```

**Original Llama-3**

```
@article{llama3modelcard,
  title={Llama 3 Model Card},
  author={AI@Meta},
  year={2024},
  url = {https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md}
}
```
