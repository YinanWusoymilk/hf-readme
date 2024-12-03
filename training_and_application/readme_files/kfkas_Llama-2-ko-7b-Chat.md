---
language:
- en
- ko
pipeline_tag: text-generation
inference: false
tags:
- facebook
- meta
- pytorch
- llama
- llama-2
- kollama
- llama-2-ko
- llama-2-ko-chat
---

# **Llama-2-Ko-Chat** 🦙🇰🇷
<img src=https://github.com/boostcampaitech5/level2_klue-nlp-08/assets/96530685/9dc3a02a-f554-42c7-9aa7-e7bd8c8870b7 style="max-width: 700px; width: 100%" />

Llama-2-Ko-7b-Chat은 [beomi/llama-2-ko-7b 40B](https://huggingface.co/beomi/llama-2-ko-7b)를 토대로 만들어졌습니다. 학습 데이터는 [nlpai-lab/kullm-v2](https://huggingface.co/datasets/nlpai-lab/kullm-v2)를 통해 학습하였습니다. 아직 학습이 진행 중이며 추후 [beomi/llama-2-ko-7b](https://huggingface.co/beomi/llama-2-ko-7b)의 업데이트에 따라 추가로 훈련을 진행할 계획입니다. 이 모델은 [Naver BoostCamp NLP-08](https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08) 프로젝트를 토대로 만들어졌습니다. 

프로젝트 링크 : [LLaMA](https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-08)

## Model Details

**Backbone Model** beomi/llama-2-ko-7b

**Model Developers** [Taemin Kim (kfkas)](https://github.com/taemin6697), [Juwon Kim (uomnf97)](https://github.com/Kim-Ju-won)

**data** nlpai-lab/kullm-v2

**prompts** kullm

**Input** Models input text only.

**Output** Models generate text only.

---
| Model              | 질문 : 캠핑 여행에 필요한 10가지 품목의 목록을 생성합니다.                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Llama-2-7b-chat-hf | `[Hello! As a helpful and respectful assistant, I'd be happy to help you with your camping trip. To ensure a safe and enjoyable experience, here is a list of 10 essential items you may need for your camping trip:Tent: A sturdy, waterproof tent to provide shelter and protection from the elements.Sleeping Bag: A warm, insulated sleeping bag to keep you cozy during the night.Sleeping Pad: A comfortable sleeping pad to provide extra cushioning and insulation.Backpack: A sturdy, comfortable backpack to carry all your gear.Clothing: Pack layers of breathable, moisture-wicking clothing to stay warm and dry.Footwear: Sturdy, waterproof hiking boots or shoes to protect your feet and provide traction.Headlamp: A reliable, battery-powered headlamp to light your way during the night.First Aid Kit: A well-stocked first aid kit to treat any injuries or illnesses.Water Bottle: A refillable, BPA-free water bottle to stay hydrated.Personal Hygiene Items: Toothbrush, toothpaste, biodegradable soap, and toilet paper to maintain personal hygiene.]`                                                                                                                      |
| Llama-2-ko         | `[3일용 캠핑장 용품 - 의류 (5일) : 속옷 , 잠옷, 긴팔 및 반팔이 필요하므로 준비하기!\u200b- 식량 (9일 이상)- 연료 (6일 사용 예정이지만 최소 7 일분 보유해야 합니다.)\u200b- 텐트/거주지역 : 20 ~ 40 평방 미터가 필요합니다.- 물 탱크 (물탱커 / 수족관 )\u200b캠핑에 사용할 8 명 (남자 4명 / 여자 4명이 필요합니다!).이 작업에는 두 개의 조건 부가가 있습니다.(조건 1) 모든 아이템 목록에서 중복 제거를위한 1 번 반복.이 옵션은 중복을 식별하여 제거할뿐만 아니라 추가 항목이 포함 된 카운트를 재설정 할 때 유용하군요.(조건 = "모든 아이템 리스트에서 한 개 이상의 동일 아이템" 이거나 "(모든 항목)"에서 동일한 숫자 값으로 식별 된)\u200b(조건 2) 작업시 각 행이 하나의 아이템 만 포함 할 필요가 없으므로 아이템이 서로 다른 선행자 로부터 여러 번]` |
| Llama-2-ko-Chat    | `[1) 텐트 - 가장 기본적이면서 유용한 장비 중 하나이며 캠핑 여행을 편안하게 해줍니다.2) 베개 및 침대 시트와 같이 푹신한 수면 용품을 챙기는 것도 잊지 마세요!3) 매트리스 - 편안함과 지지력을 제공하여 잠을 잘 자게 합니다.4) 의류 - 땀을 흘리고 휴식하는 시간을 늘리기 위해 방수재질이 포함된 긴팔옷과 반바지를 챙겨요5) 식기 세트 - 야외 조리에서 음식을 먹으려면 반드시 챙겨야 할 도구지요.6) 스토브와 연료 또는 휴대용 가스 렌턴 등 열 기구를 가져옵니다; 음식 조리에 매우 편리하게 사용할 수 있습니다.7) 랜턴, 플래시 또는 LED 스탠드를 준비하세요! 어두운 밤에 더 안전하도록 돕고, 야외에서 요리하고 놀 때 필수적인 필수 소품이 될 것입니다.8) 손전등 - 밤늦게 이동할 수도 있고 숲속 오솔길을 걸을 때도 이용할 것이므로 반드시 가지고 있어야 해요.9) 구급약상자 - 다양한 상해에 대비해서 알칼리 미스트, 소독제, 항생제, 연고 등 일반적이고 인기 있는 구급 약물을 항상 비축해야 해요. 캠프에서는 응급 상황에 처하더라도 쉽게 찾을 수 있도록 상자에 담습니다.10) 휴대폰 보조 배터리/충전기 또는 충전 가능한 외부 콘센트나 연결된 외부 전원장치 - 이것은 스마트폰이나 스마트 워치를 위한 필수품일 뿐만 아니라 다른 사람들이 필요로 하는 상황에서 긴급 연락이 되도록 도와 줄 수도 있다는 점 기억하세요.]`                                                                                                                                                                                                                                                                                        |
---
| Model              | 질문 : 삼원색에 대해 알려줘                                                                                                                                                                                                                                                                                                        |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Llama-2-7b-chat-hf | `[Regarding your question, "삼원색에 대해 알려줘" (which means "Tell me about trichromacy" in Korean), I can provide some information. Trichromacy is a concept in vision science that refers to the ability of the human visual system to perceive and distinguish between three primary colors: red, green, and blue...]` |
| Llama-2-ko         | `[C1, R0.625 G8 B275\u200b3-4, 삼각형 그리기.\u200b아래에는 삼각형을 그림니다 (그림을 그려야 할 영역의 좌표를 지정) - 명령어와 함께 사용되는 문자열로 입력할 좌표 값과 동일한 결과를 얻음 - 예를 들어 "X=-19. Y=0" 으로 입력을 하면 좌표값을 지정된 값과 같게 출력을 한다. ##########################\u200b##3_0-6-1, 좌표 입력으로 텍스트 파일을 생성하라(ex C4 D6 E10 A10 )-명령문에서 각 문자를 입력과 동일하다. -이 명령은 현재 수행중인 프로그램을 종료한다.-파일은 실행 가능한 파일과 일치할]`                 |
| Llama-2-ko-Chat    | `[물체를 인식하고 색상에 대한 시각적인 이미지를 생성하기 위해 두 개의 눈은 서로 반대쪽 방향에서 물체의 색상 정보와 명암 정보를 받아들이기 때문에, 인간은 일반적으로 색상을 삼원색이라고 하는 세 가지 원추 형태(빨강, 녹색, 파랑색)로 분류합니다. 이 중 한가지 색상이 다른 색상보다 눈에 훨씬 더 빨리 들어오는 경향이 있다고 합니다. 하지만 모든 사람이 그렇지는 않으므로 항상 삼각형 모양으로 색상을 분류하지는 않습니다. 하지만 삼원색이 우리 눈에 잘 전달되며 색상 구별에 중요하다는 것은 부정할 수 없습니다.]`                                                                                                                                                                                     |
---

## 훈련 진행 현황
<img src=https://github.com/taemin6697/Paper_Review/assets/96530685/b9a697a2-ef06-4b1c-97e1-e72b20d9a8b5 style="max-width: 700px; width: 100%" />
---

### Inference

```python
def gen(x, model, tokenizer, device):
    prompt = (
        f"아래는 작업을 설명하는 명령어입니다. 요청을 적절히 완료하는 응답을 작성하세요.\n\n### 명령어:\n{x}\n\n### 응답:"
    )
    len_prompt = len(prompt)
    gened = model.generate(
        **tokenizer(prompt, return_tensors="pt", return_token_type_ids=False).to(
            device
        ),
        max_new_tokens=1024,
        early_stopping=True,
        do_sample=True,
        top_k=20,
        top_p=0.92,
        no_repeat_ngram_size=3,
        eos_token_id=2,
        repetition_penalty=1.2,
        num_beams=3
    )
    return tokenizer.decode(gened[0])[len_prompt:]

def LLM_infer(input):
    device = (
        torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")
    )
    model_id = "kfkas/Llama-2-ko-7b-Chat"
    model = AutoModelForCausalLM.from_pretrained(
        model_id, device_map={"": 0},torch_dtype=torch.float16, low_cpu_mem_usage=True
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model.eval()
    model.config.use_cache = (True)
    tokenizer.pad_token = tokenizer.eos_token
    output = gen(input, model=model, tokenizer=tokenizer, device=device)

    return output


if __name__ == "__main__":
    text = LLM_infer("삼원색에 대해 알려줘")
    print(text)
```

## Note for oobabooga/text-generation-webui

Remove `ValueError` at `load_tokenizer` function(line 109 or near), in `modules/models.py`.

```python
diff --git a/modules/models.py b/modules/models.py
index 232d5fa..de5b7a0 100644
--- a/modules/models.py
+++ b/modules/models.py
@@ -106,7 +106,7 @@ def load_tokenizer(model_name, model):
                 trust_remote_code=shared.args.trust_remote_code,
                 use_fast=False
             )
-        except ValueError:
+        except:
             tokenizer = AutoTokenizer.from_pretrained(
                 path_to_model,
                 trust_remote_code=shared.args.trust_remote_code,
```

Since Llama-2-Ko uses FastTokenizer provided by HF tokenizers NOT sentencepiece package, 
it is required to use `use_fast=True` option when initialize tokenizer.

Apple Sillicon does not support BF16 computing, use CPU instead. (BF16 is supported when using NVIDIA GPU)


---

> Below is the original model card of the Llama-2 model.

# **Llama 2**
Llama 2 is a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. This is the repository for the 7B pretrained model, converted for the Hugging Face Transformers format. Links to other models can be found in the index at the bottom.

## Model Details
*Note: Use of this model is governed by the Meta license. In order to download the model weights and tokenizer, please visit the [website](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) and accept our License before requesting access here.*

Meta developed and publicly released the Llama 2 family of large language models (LLMs), a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. Our fine-tuned LLMs, called Llama-2-Chat, are optimized for dialogue use cases. Llama-2-Chat models outperform open-source chat models on most benchmarks we tested, and in our human evaluations for helpfulness and safety, are on par with some popular closed-source models like ChatGPT and PaLM.

**Model Developers** Meta

**Variations** Llama 2 comes in a range of parameter sizes — 7B, 13B, and 70B — as well as pretrained and fine-tuned variations.

**Input** Models input text only.

**Output** Models generate text only.

**Model Architecture** Llama 2 is an auto-regressive language model that uses an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align to human preferences for helpfulness and safety.


||Training Data|Params|Content Length|GQA|Tokens|LR|
|---|---|---|---|---|---|---|
|Llama 2|*A new mix of publicly available online data*|7B|4k|&#10007;|2.0T|3.0 x 10<sup>-4</sup>|
|Llama 2|*A new mix of publicly available online data*|13B|4k|&#10007;|2.0T|3.0 x 10<sup>-4</sup>|
|Llama 2|*A new mix of publicly available online data*|70B|4k|&#10004;|2.0T|1.5 x 10<sup>-4</sup>|

*Llama 2 family of models.* Token counts refer to pretraining data only. All models are trained with a global batch-size of 4M tokens. Bigger models -  70B -- use Grouped-Query Attention (GQA) for improved inference scalability.

**Model Dates** Llama 2 was trained between January 2023 and July 2023.

**Status** This is a static model trained on an offline dataset. Future versions of the tuned models will be released as we improve model safety with community feedback.

**License** A custom commercial license is available at: [https://ai.meta.com/resources/models-and-libraries/llama-downloads/](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)

**Research Paper** ["Llama-2: Open Foundation and Fine-tuned Chat Models"](arxiv.org/abs/2307.09288)

## Intended Use
**Intended Use Cases** Llama 2 is intended for commercial and research use in English. Tuned models are intended for assistant-like chat, whereas pretrained models can be adapted for a variety of natural language generation tasks.

To get the expected features and performance for the chat versions, a specific formatting needs to be followed, including the `INST` and `<<SYS>>` tags, `BOS` and `EOS` tokens, and the whitespaces and breaklines in between (we recommend calling `strip()` on inputs to avoid double-spaces). See our reference code in github for details: [`chat_completion`](https://github.com/facebookresearch/llama/blob/main/llama/generation.py#L212).

**Out-of-scope Uses** Use in any manner that violates applicable laws or regulations (including trade compliance laws).Use in languages other than English. Use in any other way that is prohibited by the Acceptable Use Policy and Licensing Agreement for Llama 2.

## Hardware and Software
**Training Factors** We used custom training libraries, Meta's Research Super Cluster, and production clusters for pretraining. Fine-tuning, annotation, and evaluation were also performed on third-party cloud compute.

**Carbon Footprint** Pretraining utilized a cumulative 3.3M GPU hours of computation on hardware of type A100-80GB (TDP of 350-400W). Estimated total emissions were 539 tCO2eq, 100% of which were offset by Meta’s sustainability program.

||Time (GPU hours)|Power Consumption (W)|Carbon Emitted(tCO<sub>2</sub>eq)|
|---|---|---|---|
|Llama 2 7B|184320|400|31.22|
|Llama 2 13B|368640|400|62.44|
|Llama 2 70B|1720320|400|291.42|
|Total|3311616||539.00|

**CO<sub>2</sub> emissions during pretraining.** Time: total GPU time required for training each model. Power Consumption: peak power capacity per GPU device for the GPUs used adjusted for power usage efficiency. 100% of the emissions are directly offset by Meta's sustainability program, and because we are openly releasing these models, the pretraining costs do not need to be incurred by others.

## Training Data
**Overview** Llama 2 was pretrained on 2 trillion tokens of data from publicly available sources. The fine-tuning data includes publicly available instruction datasets, as well as over one million new human-annotated examples. Neither the pretraining nor the fine-tuning datasets include Meta user data.

**Data Freshness** The pretraining data has a cutoff of September 2022, but some tuning data is more recent, up to July 2023.

## Evaluation Results

In this section, we report the results for the Llama 1 and Llama 2 models on standard academic benchmarks.For all the evaluations, we use our internal evaluations library.

|Model|Size|Code|Commonsense Reasoning|World Knowledge|Reading Comprehension|Math|MMLU|BBH|AGI Eval|
|---|---|---|---|---|---|---|---|---|---|
|Llama 1|7B|14.1|60.8|46.2|58.5|6.95|35.1|30.3|23.9|
|Llama 1|13B|18.9|66.1|52.6|62.3|10.9|46.9|37.0|33.9|
|Llama 1|33B|26.0|70.0|58.4|67.6|21.4|57.8|39.8|41.7|
|Llama 1|65B|30.7|70.7|60.5|68.6|30.8|63.4|43.5|47.6|
|Llama 2|7B|16.8|63.9|48.9|61.3|14.6|45.3|32.6|29.3|
|Llama 2|13B|24.5|66.9|55.4|65.8|28.7|54.8|39.4|39.1|
|Llama 2|70B|**37.5**|**71.9**|**63.6**|**69.4**|**35.2**|**68.9**|**51.2**|**54.2**|

**Overall performance on grouped academic benchmarks.** *Code:* We report the average pass@1 scores of our models on HumanEval and MBPP. *Commonsense Reasoning:* We report the average of PIQA, SIQA, HellaSwag, WinoGrande, ARC easy and challenge, OpenBookQA, and CommonsenseQA. We report 7-shot results for CommonSenseQA and 0-shot results for all other benchmarks. *World Knowledge:* We evaluate the 5-shot performance on NaturalQuestions and TriviaQA and report the average. *Reading Comprehension:* For reading comprehension, we report the 0-shot average on SQuAD, QuAC, and BoolQ. *MATH:* We report the average of the GSM8K (8 shot) and MATH (4 shot) benchmarks at top 1.

|||TruthfulQA|Toxigen|
|---|---|---|---|
|Llama 1|7B|27.42|23.00|
|Llama 1|13B|41.74|23.08|
|Llama 1|33B|44.19|22.57|
|Llama 1|65B|48.71|21.77|
|Llama 2|7B|33.29|**21.25**|
|Llama 2|13B|41.86|26.10|
|Llama 2|70B|**50.18**|24.60|

**Evaluation of pretrained LLMs on automatic safety benchmarks.** For TruthfulQA, we present the percentage of generations that are both truthful and informative (the higher the better). For ToxiGen, we present the percentage of toxic generations (the smaller the better).


|||TruthfulQA|Toxigen|
|---|---|---|---|
|Llama-2-Chat|7B|57.04|**0.00**|
|Llama-2-Chat|13B|62.18|**0.00**|
|Llama-2-Chat|70B|**64.14**|0.01|

**Evaluation of fine-tuned LLMs on different safety datasets.** Same metric definitions as above.

## Ethical Considerations and Limitations
Llama 2 is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2, developers should perform safety testing and tuning tailored to their specific applications of the model.

Please see the Responsible Use Guide available at [https://ai.meta.com/llama/responsible-use-guide/](https://ai.meta.com/llama/responsible-use-guide)

## Reporting Issues
Please report any software “bug,” or other problems with the models through one of the following means:
- Reporting issues with the model: [github.com/facebookresearch/llama](http://github.com/facebookresearch/llama)
- Reporting problematic content generated by the model: [developers.facebook.com/llama_output_feedback](http://developers.facebook.com/llama_output_feedback)
- Reporting bugs and security concerns: [facebook.com/whitehat/info](http://facebook.com/whitehat/info)

## Llama Model Index
|Model|Llama2|Llama2-hf|Llama2-chat|Llama2-chat-hf|
|---|---|---|---|---|
|7B| [Link](https://huggingface.co/llamaste/Llama-2-7b) | [Link](https://huggingface.co/llamaste/Llama-2-7b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-7b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-7b-chat-hf)|
|13B| [Link](https://huggingface.co/llamaste/Llama-2-13b) | [Link](https://huggingface.co/llamaste/Llama-2-13b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-13b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-13b-hf)|
|70B| [Link](https://huggingface.co/llamaste/Llama-2-70b) | [Link](https://huggingface.co/llamaste/Llama-2-70b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-70b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-70b-hf)|