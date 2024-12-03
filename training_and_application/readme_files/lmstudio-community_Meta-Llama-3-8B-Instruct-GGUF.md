---
language:
- en
pipeline_tag: text-generation
tags:
- facebook
- meta
- pytorch
- llama
- llama-3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
license: llama3
extra_gated_prompt: >-
  ### META LLAMA 3 COMMUNITY LICENSE AGREEMENT

  Meta Llama 3 Version Release Date: April 18, 2024
  
  "Agreement" means the terms and conditions for use, reproduction, distribution and modification of the
  Llama Materials set forth herein.

  "Documentation" means the specifications, manuals and documentation accompanying Meta Llama 3
  distributed by Meta at https://llama.meta.com/get-started/.

  "Licensee" or "you" means you, or your employer or any other person or entity (if you are entering into
  this Agreement on such person or entity’s behalf), of the age required under applicable laws, rules or
  regulations to provide legal consent and that has legal authority to bind your employer or such other
  person or entity if you are entering in this Agreement on their behalf.

  "Meta Llama 3" means the foundational large language models and software and algorithms, including
  machine-learning model code, trained model weights, inference-enabling code, training-enabling code,
  fine-tuning enabling code and other elements of the foregoing distributed by Meta at
  https://llama.meta.com/llama-downloads.

  "Llama Materials" means, collectively, Meta’s proprietary Meta Llama 3 and Documentation (and any
  portion thereof) made available under this Agreement.

  "Meta" or "we" means Meta Platforms Ireland Limited (if you are located in or, if you are an entity, your
  principal place of business is in the EEA or Switzerland) and Meta Platforms, Inc. (if you are located
  outside of the EEA or Switzerland).
     
  1. License Rights and Redistribution.

  a. Grant of Rights. You are granted a non-exclusive, worldwide, non-transferable and royalty-free
  limited license under Meta’s intellectual property or other rights owned by Meta embodied in the Llama
  Materials to use, reproduce, distribute, copy, create derivative works of, and make modifications to the
  Llama Materials.

  b. Redistribution and Use.

  i. If you distribute or make available the Llama Materials (or any derivative works
  thereof), or a product or service that uses any of them, including another AI model, you shall (A) provide
  a copy of this Agreement with any such Llama Materials; and (B) prominently display “Built with Meta
  Llama 3” on a related website, user interface, blogpost, about page, or product documentation. If you
  use the Llama Materials to create, train, fine tune, or otherwise improve an AI model, which is
  distributed or made available, you shall also include “Llama 3” at the beginning of any such AI model
  name.

  ii. If you receive Llama Materials, or any derivative works thereof, from a Licensee as part 
  of an integrated end user product, then Section 2 of this Agreement will not apply to you.

  iii. You must retain in all copies of the Llama Materials that you distribute the following
  attribution notice within a “Notice” text file distributed as a part of such copies: “Meta Llama 3 is
  licensed under the Meta Llama 3 Community License, Copyright © Meta Platforms, Inc. All Rights
  Reserved.”

  iv. Your use of the Llama Materials must comply with applicable laws and regulations
  (including trade compliance laws and regulations) and adhere to the Acceptable Use Policy for the Llama
  Materials (available at https://llama.meta.com/llama3/use-policy), which is hereby incorporated by
  reference into this Agreement.

  v. You will not use the Llama Materials or any output or results of the Llama Materials to
  improve any other large language model (excluding Meta Llama 3 or derivative works thereof).

  2. Additional Commercial Terms. If, on the Meta Llama 3 version release date, the monthly active users
  of the products or services made available by or for Licensee, or Licensee’s affiliates, is greater than 700
  million monthly active users in the preceding calendar month, you must request a license from Meta,
  which Meta may grant to you in its sole discretion, and you are not authorized to exercise any of the
  rights under this Agreement unless or until Meta otherwise expressly grants you such rights.

  3. Disclaimer of Warranty. UNLESS REQUIRED BY APPLICABLE LAW, THE LLAMA MATERIALS AND ANY
  OUTPUT AND RESULTS THEREFROM ARE PROVIDED ON AN “AS IS” BASIS, WITHOUT WARRANTIES OF
  ANY KIND, AND META DISCLAIMS ALL WARRANTIES OF ANY KIND, BOTH EXPRESS AND IMPLIED,
  INCLUDING, WITHOUT LIMITATION, ANY WARRANTIES OF TITLE, NON-INFRINGEMENT,
  MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE. YOU ARE SOLELY RESPONSIBLE FOR
  DETERMINING THE APPROPRIATENESS OF USING OR REDISTRIBUTING THE LLAMA MATERIALS AND
  ASSUME ANY RISKS ASSOCIATED WITH YOUR USE OF THE LLAMA MATERIALS AND ANY OUTPUT AND
  RESULTS.

  4. Limitation of Liability. IN NO EVENT WILL META OR ITS AFFILIATES BE LIABLE UNDER ANY THEORY OF
  LIABILITY, WHETHER IN CONTRACT, TORT, NEGLIGENCE, PRODUCTS LIABILITY, OR OTHERWISE, ARISING
  OUT OF THIS AGREEMENT, FOR ANY LOST PROFITS OR ANY INDIRECT, SPECIAL, CONSEQUENTIAL,
  INCIDENTAL, EXEMPLARY OR PUNITIVE DAMAGES, EVEN IF META OR ITS AFFILIATES HAVE BEEN ADVISED
  OF THE POSSIBILITY OF ANY OF THE FOREGOING.

  5. Intellectual Property.

  a. No trademark licenses are granted under this Agreement, and in connection with the Llama
  Materials, neither Meta nor Licensee may use any name or mark owned by or associated with the other
  or any of its affiliates, except as required for reasonable and customary use in describing and
  redistributing the Llama Materials or as set forth in this Section 5(a). Meta hereby grants you a license to
  use “Llama 3” (the “Mark”) solely as required to comply with the last sentence of Section 1.b.i. You will
  comply with Meta’s brand guidelines (currently accessible at
  https://about.meta.com/brand/resources/meta/company-brand/ ). All goodwill arising out of your use
  of the Mark will inure to the benefit of Meta.

  b. Subject to Meta’s ownership of Llama Materials and derivatives made by or for Meta, with
  respect to any derivative works and modifications of the Llama Materials that are made by you, as
  between you and Meta, you are and will be the owner of such derivative works and modifications.

  c. If you institute litigation or other proceedings against Meta or any entity (including a
  cross-claim or counterclaim in a lawsuit) alleging that the Llama Materials or Meta Llama 3 outputs or
  results, or any portion of any of the foregoing, constitutes infringement of intellectual property or other
  rights owned or licensable by you, then any licenses granted to you under this Agreement shall
  terminate as of the date such litigation or claim is filed or instituted. You will indemnify and hold
  harmless Meta from and against any claim by any third party arising out of or related to your use or
  distribution of the Llama Materials.

  6. Term and Termination. The term of this Agreement will commence upon your acceptance of this
  Agreement or access to the Llama Materials and will continue in full force and effect until terminated in
  accordance with the terms and conditions herein. Meta may terminate this Agreement if you are in
  breach of any term or condition of this Agreement. Upon termination of this Agreement, you shall delete
  and cease use of the Llama Materials. Sections 3, 4 and 7 shall survive the termination of this
  Agreement.

  7. Governing Law and Jurisdiction. This Agreement will be governed and construed under the laws of
  the State of California without regard to choice of law principles, and the UN Convention on Contracts
  for the International Sale of Goods does not apply to this Agreement. The courts of California shall have
  exclusive jurisdiction of any dispute arising out of this Agreement.

  ### Meta Llama 3 Acceptable Use Policy

  Meta is committed to promoting safe and fair use of its tools and features, including Meta Llama 3. If you
  access or use Meta Llama 3, you agree to this Acceptable Use Policy (“Policy”). The most recent copy of
  this policy can be found at [https://llama.meta.com/llama3/use-policy](https://llama.meta.com/llama3/use-policy)

  #### Prohibited Uses

  We want everyone to use Meta Llama 3 safely and responsibly. You agree you will not use, or allow
  others to use, Meta Llama 3 to:
  1. Violate the law or others’ rights, including to:
      1. Engage in, promote, generate, contribute to, encourage, plan, incite, or further illegal or unlawful activity or content, such as:
          1. Violence or terrorism
          2. Exploitation or harm to children, including the solicitation, creation, acquisition, or dissemination of child exploitative content or failure to report Child Sexual Abuse Material
          3. Human trafficking, exploitation, and sexual violence
          4. The illegal distribution of information or materials to minors, including obscene materials, or failure to employ legally required age-gating in connection with such information or materials.
          5. Sexual solicitation
          6. Any other criminal activity
      2. Engage in, promote, incite, or facilitate the harassment, abuse, threatening, or bullying of individuals or groups of individuals
      3. Engage in, promote, incite, or facilitate discrimination or other unlawful or harmful conduct in the provision of employment, employment benefits, credit, housing, other economic benefits, or other essential goods and services
      4. Engage in the unauthorized or unlicensed practice of any profession including, but not limited to, financial, legal, medical/health, or related professional practices
      5. Collect, process, disclose, generate, or infer health, demographic, or other sensitive personal or private information about individuals without rights and consents required by applicable laws
      6. Engage in or facilitate any action or generate any content that infringes, misappropriates, or otherwise violates any third-party rights, including the outputs or results of any products or services using the Llama Materials
      7. Create, generate, or facilitate the creation of malicious code, malware, computer viruses or do anything else that could disable, overburden, interfere with or impair the proper working, integrity, operation or appearance of a website or computer system
  2. Engage in, promote, incite, facilitate, or assist in the planning or development of activities that present a risk of death or bodily harm to individuals, including use of Meta Llama 3 related to the following:
      1. Military, warfare, nuclear industries or applications, espionage, use for materials or activities that are subject to the International Traffic Arms Regulations (ITAR) maintained by the United States Department of State
      2. Guns and illegal weapons (including weapon development)
      3. Illegal drugs and regulated/controlled substances
      4. Operation of critical infrastructure, transportation technologies, or heavy machinery
      5. Self-harm or harm to others, including suicide, cutting, and eating disorders
      6. Any content intended to incite or promote violence, abuse, or any infliction of bodily harm to an individual
  3. Intentionally deceive or mislead others, including use of Meta Llama 3 related to the following:
      1. Generating, promoting, or furthering fraud or the creation or promotion of disinformation
      2. Generating, promoting, or furthering defamatory content, including the creation of defamatory statements, images, or other content
      3. Generating, promoting, or further distributing spam
      4. Impersonating another individual without consent, authorization, or legal right
      5. Representing that the use of Meta Llama 3 or outputs are human-generated
      6. Generating or facilitating false online engagement, including fake reviews and other means of fake online engagement
  4. Fail to appropriately disclose to end users any known dangers of your AI system
  
  Please report any violation of this Policy, software “bug,” or other problems that could lead to a violation
  of this Policy through one of the following means:
      * Reporting issues with the model: [https://github.com/meta-llama/llama3](https://github.com/meta-llama/llama3)
      * Reporting risky content generated by the model:
      developers.facebook.com/llama_output_feedback
      * Reporting bugs and security concerns: facebook.com/whitehat/info
      * Reporting violations of the Acceptable Use Policy or unlicensed uses of Meta Llama 3: LlamaUseReport@meta.com
extra_gated_fields:
  First Name: text
  Last Name: text
  Date of birth: date_picker
  Country: country
  Affiliation: text
  geo: ip_location  
  By clicking Submit below I accept the terms of the license and acknowledge that the information I provide will be collected stored processed and shared in accordance with the Meta Privacy Policy: checkbox
extra_gated_description: The information you provide will be collected, stored, processed and shared in accordance with the [Meta Privacy Policy](https://www.facebook.com/privacy/policy/).
extra_gated_button_content: Submit
quantized_by: bartowski
lm_studio:
  param_count: 8b
  use_case: general
  release_date: 18-04-2024
  model_creator: meta-llama
  prompt_template: Llama 3
  system_prompt: You are a helpful AI assistant.
  base_model: llama
  original_repo: meta-llama/Meta-Llama-3-8B-Instruct
---

## 💫 Community Model> Llama 3 8B Instruct by Meta

*👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)*.

**Model creator:** [meta-llama](https://huggingface.co/meta-llama)<br>
**Original model**: [Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)<br>
**GGUF quantization:** provided by [bartowski](https://huggingface.co/bartowski) based on `llama.cpp` PR [6745](https://github.com/ggerganov/llama.cpp/pull/6745)<br>

## Model Summary:
Llama 3 represents a huge update to the Llama family of models. This model is the 8B parameter instruction tuned model, meaning it's small, fast, and tuned for following instructions.<br>
This model is very happy to follow the given system prompt, so use this to your advantage to get the behavior you desire.<br>
Llama 3 excels at all the general usage situations, including multi turn conversations, general world knowledge, and coding.<br>
This 8B model exceeds the performance of Llama 2's 70B model, showing that the performance is far greater than the previous iteration.

## Prompt Template:

Choose the 'Llama 3' preset in your LM Studio. 

Under the hood, the model will see a prompt that's formatted like so:

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

```

## Use case and examples

Llama 3 should be great for anything you throw at it. Try it with conversations, coding, and just all around general inquiries.

## Creative conversations

Using a system prompt of `You are a pirate chatbot who always responds in pirate speak!`

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/PYIhzOZtKVSHEUq24u3ll.png)

## General knowledge

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/3XDcR9e10CxcdVhmeco_W.png)

## Coding

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/l-AHfv39hXG9IPzKqIBpv.png)

## Technical Details

Llama 3 was trained on over 15T tokens from a massively diverse range of subjects and languages, and includes 4 times more code than Llama 2.

This model also features Grouped Attention Query (GQA) so that memory usage scales nicely over large contexts.

Instruction fine tuning was performed with a combination of supervised fine-tuning (SFT), rejection sampling, proximal policy optimization (PPO), and direct policy optimization (DPO).

Check out their blog post for more information [here](https://ai.meta.com/blog/meta-llama-3/)

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.

🙏 Special thanks to [Kalomaze](https://github.com/kalomaze) for his dataset (linked [here](https://github.com/ggerganov/llama.cpp/discussions/5263)) that was used for calculating the imatrix for these quants, which improves the overall quality!

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model.  You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models.  LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.
