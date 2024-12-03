---
inference: false
license: gpl-3.0
datasets:
- JosephusCheung/GuanacoDataset
language:
- en
- zh
- ja
- de
pipeline_tag: conversational
tags:
- llama
- guannaco
- alpaca
---

![](https://huggingface.co/JosephusCheung/Guanaco/resolve/main/StupidBanner.png)

**You can run on Colab free T4 GPU now**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ocSmoy3ba1EkYu7JWT1oCw9vz8qC2cMk#scrollTo=zLORi5OcPcIJ)

 **It is highly recommended to use fp16 inference for this model, as 8-bit precision may significantly affect performance. If you require a more Consumer Hardware friendly version, please use the specialized quantized, only 5+GB V-Ram required** [JosephusCheung/GuanacoOnConsumerHardware](https://huggingface.co/JosephusCheung/GuanacoOnConsumerHardware).

 **You are encouraged to use the latest version of transformers from GitHub.**

Guanaco is an advanced instruction-following language model built on Meta's LLaMA 7B model. Expanding upon the initial 52K dataset from the Alpaca model, an additional 534K+ entries have been incorporated, covering English, Simplified Chinese, Traditional Chinese (Taiwan), Traditional Chinese (Hong Kong), Japanese, Deutsch, and various linguistic and grammatical tasks. This wealth of data enables Guanaco to perform exceptionally well in multilingual environments.

In an effort to foster openness and replicability in research, we have made the Guanaco Dataset publicly accessible and we have released the model weights here. By providing these resources, we aim to inspire more researchers to pursue related research and collectively advance the development of instruction-following language models.

[KBlueLeaf](https://huggingface.co/KBlueLeaf)’s invaluable contributions to the conceptual validation, [trained model](https://huggingface.co/KBlueLeaf/guanaco-7B-leh) and [inference development](https://github.com/KohakuBlueleaf/guanaco-lora) of the model would be gratefully acknowledged, without whose efforts the project shall never have come to fruition.

When utilizing the Guanaco model, please bear in mind the following points:

The Guanaco model has not been filtered for harmful, biased, or explicit content. As a result, outputs that do not adhere to ethical norms may be generated during use. Please exercise caution when using the model in research or practical applications.
1. ### Improved context and prompt role support:

   The new format is designed to be similar to ChatGPT, allowing for better integration with the Alpaca format and enhancing the overall user experience.

   Instruction is utilized as a few-shot context to support diverse inputs and responses, making it easier for the model to understand and provide accurate responses to user queries.

   The format is as follows:

```
### Instruction:
User: History User Input
Assistant: History Assistant Answer
### Input:
System: Knowledge
User: New User Input
### Response:
New Assistant Answer
```

   This structured format allows for easier tracking of the conversation history and maintaining context throughout a multi-turn dialogue.

3. ### Role-playing support:

   Guanaco now offers advanced role-playing support, similar to Character.AI, in English, Simplified Chinese, Traditional Chinese, Japanese, and Deutsch, making it more versatile for users from different linguistic backgrounds.

   Users can instruct the model to assume specific roles, historical figures, or fictional characters, as well as personalities based on their input. This allows for more engaging and immersive conversations.

   The model can use various sources of information to provide knowledge and context for the character's background and behavior, such as encyclopedic entries, first-person narrations, or a list of personality traits.

   The model will consistently output responses in the format "Character Name: Reply" to maintain the chosen role throughout the conversation, enhancing the user's experience.

4. ### Rejection of answers and avoidance of erroneous responses:
   
   The model has been updated to handle situations where it lacks sufficient knowledge or is unable to provide a valid response more effectively.

   Reserved keywords have been introduced to indicate different scenarios and provide clearer communication with the user, use in System Prompt:

   NO IDEA: Indicates that the model lacks the necessary knowledge to provide an accurate answer, and will explain this to the user, encouraging them to seek alternative sources.
   
   FORBIDDEN: Indicates that the model refuses to answer due to specific reasons (e.g., legal, ethical, or safety concerns), which will be inferred based on the context of the query.

   SFW: Indicates that the model refuses to answer a question because it has been filtered for NSFW content, ensuring a safer and more appropriate user experience.

6. ### Continuation of responses for ongoing topics:

   The Guanaco model can now continue answering questions or discussing topics upon the user's request, making it more adaptable and better suited for extended conversations.

   The contextual structure consisting of System, Assistant, and User roles allows the model to engage in multi-turn dialogues, maintain context-aware conversations, and provide more coherent responses.

   The model can now accommodate role specification and character settings, providing a more immersive and tailored conversational experience based on the user's preferences.

It is important to remember that Guanaco is a 7B-parameter model, and **any knowledge-based content should be considered potentially inaccurate**. We strongly recommend **providing verifiable sources in System Prompt, such as Wikipedia, for knowledge-based answers**. In the absence of sources, it is crucial to inform users of this limitation to prevent the dissemination of false information and to maintain transparency.

Due to the differences in the format between this project and [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca), please refer to *Guanaco-lora: LoRA for training Multilingual Instruction-following LM based on LLaMA* (https://github.com/KohakuBlueleaf/guanaco-lora) for further training and inference our models.

## Recent News

We've noticed a recent entrant in the field, the QLoRa method, which we find concerning due to its attempt to piggyback on the reputation of Guanaco. We strongly disapprove of such practices. QLoRa, as far as we can tell, lacks mathematical robustness and its performance significantly trails behind that of GPTQ and advancements such as PEFT fine-tuning, which have been successful in improving upon it.

Guanaco has been diligent, consistently releasing multilingual datasets since March 2023, along with publishing weights that are not only an enhanced version of GPTQ but also support multimodal VQA and have been optimized for 4-bit. Despite the substantial financial investment of tens of thousands of dollars in distilling data from OpenAI's GPT models, we still consider these efforts to be incremental.

We, however, aim to move beyond the incremental:

1. We strive to no longer rely on distillation data from OpenAI: We've found that relying on GPT-generated data impedes significant breakthroughs. Furthermore, this approach has proven to be disastrous when dealing with the imbalances in multilingual tasks.

2. We're focusing on the enhancement of quantization structure and partial native 4-bit fine-tuning: We are deeply appreciative of the GPTQ-Llama project for paving the way in state-of-the-art LLM quantization. Its unique qualities, especially at the 7B size, are facilitating significant progress in multilingual and multimodal tasks.

3. We plan to utilize visual data to adjust our language models: We believe this will fundamentally address the issues of language imbalance, translation inaccuracies, and the lack of graphical logic in LLM.

While our work is still in the early stages, we're determined to break new ground in these areas. Our critique of QLoRa's practices does not stem from animosity but rather from the fundamental belief that innovation should be rooted in originality, integrity, and substantial progress.
