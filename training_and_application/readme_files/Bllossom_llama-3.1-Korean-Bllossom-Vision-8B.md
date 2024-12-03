---
language:
- en
- ko
license: llama3.1
library_name: transformers
base_model:
- meta-llama/Meta-Llama-3.1-8B
---

<a href="https://github.com/MLP-Lab/Bllossom">
  <img src="https://github.com/teddysum/bllossom/blob/main//bllossom_icon.png?raw=true" width="30%" height="30%">
</a>

# Update!
* [2024.09.04] Bllossom의 시각-언어 preview 모델이 최초 업데이트 되었습니다.


# Bllossom | [Demo]() | [Homepage](https://www.bllossom.ai/) | [Github](https://github.com/MLP-Lab/Bllossom) |

```bash
저희 Bllossom 팀에서 llama3.1 기반의 한국어-영어 시각-언어모델 Bllossom-Vision을 공개합니다.
이번 Bllossom-Vision은 preview 버전으로 다음과 같은 특징을 보입니다.
 - 일반 언어모델, 시각-언어모델 양방향으로 활용이 가능합니다.
 - 이미지를 넣으면 시각-언어모델, 넣지 않으면 언어모델로 작동하며 시각-언어, 그냥 언어모델 양방향모두 학습 및 추론이 가능합니다.
 - 기존 언어모델의 성능을 최대한 유지하며 시각-언어모델의 역할에 충실하도록 심혈을 기울였습니다.
 - 영어 성능을 전혀 손상시키지 않은 완전한 Bilingual 모델입니다.
 - 다만, (1) 이미지 크기에 따라 추론 편차가 심합니다. (2) 한국어 표, 그래프, pdf문서 해석이 약합니다. 이 두개는 Advanced 모델에서 가능하며 10월달에 공개할 예정입니다.

해당 모델은 다음과 같은 협업을 토대로 구축 되었습니다!
 - 서울과기대 MLP연구실의 시각-언어 + 언어모델 사전학습 기법이 적용되었습니다.
 - 테디썸의 정교한 Instruction Tuning과 RAG 기술이 적용되었습니다.
 - 유클리드소프트에서 제작한 시각-언어 학습데이터를 토대로 학습 되었습니다.
 - AICA의 연구지원이 있었습니다.
 - 서울과기대MLP연구실과 유클리드소프트가 지난 2020~2024년 까지 5년 동안 함께 진행한 한국어 VQA관련 데이터를 모두 활용했습니다.

언제나 그랬듯 해당 모델은 상업적 이용이 가능합니다.

1. Bllossom Vision은 AAAI2024, NAACL2024, LREC-COLING2024 (구두) 발표되었습니다.
2. 좋은 언어모델 계속 업데이트 하겠습니다!! 한국어 강화를위해 공동 연구하실분(특히논문) 언제든 환영합니다!! 
   그리고 소량의 GPU라도 대여 가능한팀은 언제든 연락주세요! 만들고 싶은거 도와드려요.
```

```bash
We, the Bllossom team, are pleased to announce the release of Bllossom-Vision, a Korean-English vision-language model based on llama3.1. This Bllossom-Vision is a preview version and features the following:
 - It can be utilized both as a general language model and as a vision-language model.
 - It operates as a vision-language model when an image is provided, and as a language model when no image is provided. It is capable of both training and inference in both directions, whether as a vision-language or just a language model.
 - We have put significant effort into ensuring it remains faithful to the role of a vision-language model while maintaining the performance of a traditional language model as much as possible.
 - It is a fully bilingual model that does not compromise English performance at all.
```
**Bllossom is developed by [MLPLab at Seoultech](http://mlp.seoultech.ac.kr), [Teddysum](http://teddysum.ai/) and [Yonsei Univ](https://sites.google.com/view/hansaemkim/hansaem-kim)**


## Demo Video

<div style="display: flex; justify-content: space-between;">
  <!-- 첫 번째 컬럼 -->
  <div style="width: 49%;">
    <a>
      <img src="https://github.com/lhsstn/lhsstn/blob/main/x-llava_dem.gif?raw=true" style="width: 100%; height: auto;">
    </a>
    <p style="text-align: center;">Bllossom-V Demo</p>
  </div>
</div>




## Example code

### Colab Tutorial
 - [Inference-Code-Link](Inference code coming soon)

### Install Dependencies
```bash
pip install torch transformers==4.44.0 
```

### Python code without Image
```python
from transformers import LlavaNextForConditionalGeneration,LlavaNextProcessor
import torch

model = LlavaNextForConditionalGeneration.from_pretrained(
  'Bllossom/llama-3.1-Korean-Bllossom-Vision-8B',
  torch_dtype=torch.bfloat16,
  device_map='auto'
)
processor = LlavaNextProcessor.from_pretrained('Bllossom/llama-3.1-Korean-Bllossom-Vision-8B')

with torch.no_grad():

    PROMPT=\
    """You are a versatile AI assistant named Bllava, capable of both understanding and generating text as well as interpreting and analyzing images. Your role is to kindly and effectively answer the user’s questions, whether they are about text or images, and provide appropriate and helpful responses to all types of queries.
    
    당신은 텍스트를 이해하고 생성하는 것뿐만 아니라 이미지를 해석하고 분석할 수 있는 다재다능한 AI 어시스턴트 블라바입니다. 사용자의 질문이 텍스트에 관한 것이든 이미지에 관한 것이든 친절하고 효과적으로 답변하며, 모든 유형의 질의에 대해 적절하고 유용한 응답을 제공하는 것이 당신의 역할입니다."""

    instruction = '자연어처리 15주 분량 커리큘럼을 짜줘'
    
    messages = [
        {'role': 'system', 'content': f"{PROMPT}"},
        {'role': 'user', 'content': f"{instruction}"}
    ]

    chat_messages = processor.tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors='pt',
    )
    
    bos_token = processor.tokenizer.bos_token_id
    chat_messages = torch.cat([torch.tensor([[bos_token]]),chat_messages],dim=-1).to(model.device)
    

    output = model.generate(
        input_ids = chat_messages,
        use_cache=False,
        max_new_tokens=2048,
        top_p=0.9,
        temperature=0.6,
        do_sample=True,
    )

    print(processor.tokenizer.decode(output[0]))
```

### Python code with Image
```python
from PIL import Image
from transformers import LlavaNextForConditionalGeneration,LlavaNextProcessor
import torch

model = LlavaNextForConditionalGeneration.from_pretrained(
  'Bllossom/llama-3.1-Korean-Bllossom-Vision-8B',
  torch_dtype=torch.bfloat16,
  device_map='auto'
)
processor = LlavaNextProcessor.from_pretrained('Bllossom/llama-3.1-Korean-Bllossom-Vision-8B')

image = Image.open('[IMAGE_PATH]').convert('RGB')

PROMPT=\
"""You are a versatile AI assistant named Bllava, capable of both understanding and generating text as well as interpreting and analyzing images. Your role is to kindly and effectively answer the user’s questions, whether they are about text or images, and provide appropriate and helpful responses to all types of queries.

당신은 텍스트를 이해하고 생성하는 것뿐만 아니라 이미지를 해석하고 분석할 수 있는 다재다능한 AI 어시스턴트 블라바입니다. 사용자의 질문이 텍스트에 관한 것이든 이미지에 관한 것이든 친절하고 효과적으로 답변하며, 모든 유형의 질의에 대해 적절하고 유용한 응답을 제공하는 것이 당신의 역할입니다."""


instruction = '이미지에 대해서 설명해주세요.'
messages = [
    {'role': 'system', 'content': f"{PROMPT}"},
    {'role': 'user', 'content': f"<image>\n{instruction}"}
]

chat_messages = processor.tokenizer.apply_chat_template(
  messages,
  tokenize=False,
  add_generation_prompt=True
).to(model.device)

inputs = processor(
    chat_messages,
    image,
    return_tensors='pt',
)

output = model.generate(
    **inputs,
    max_new_tokens=1024,
    )

print(processor.tokenizer.decode(output[0]))
```


## Supported by

 - AICA  <img src="https://aica-gj.kr/images/logo.png" width="20%" height="20%">
 - 유클리드소프트 <img src="https://euclidsoft.co.kr/_next/image?url=%2Fimg%2Flogo.png&w=384&q=75" width="20%" height="20%">

## Citation
**Language Model**
```text
@misc{bllossom,
  author = {ChangSu Choi, Yongbin Jeong, Seoyoon Park, InHo Won, HyeonSeok Lim, SangMin Kim, Yejee Kang, Chanhyuk Yoon, Jaewan Park, Yiseul Lee, HyeJin Lee, Younggyun Hahm, Hansaem Kim, KyungTae Lim},
  title = {Optimizing Language Augmentation for Multilingual Large Language Models: A Case Study on Korean},
  year = {2024},
  journal = {LREC-COLING 2024},
  paperLink = {\url{https://arxiv.org/pdf/2403.10882}},
 },
}
```

**Vision-Language Model**
```text
@misc{bllossom-V,
  author = {Dongjae Shin, Hyunseok Lim, Inho Won, Changsu Choi, Minjun Kim, Seungwoo Song, Hangyeol Yoo, Sangmin Kim, Kyungtae Lim},
  title = {X-LLaVA: Optimizing Bilingual Large Vision-Language Alignment},
  year = {2024},
  publisher = {GitHub},
  journal = {NAACL 2024 findings},
  paperLink = {\url{https://arxiv.org/pdf/2403.11399}},
 },
}
```

## Contact
 - 임경태(KyungTae Lim), Professor at Seoultech. `ktlim@seoultech.ac.kr`
 - 함영균(Younggyun Hahm), CEO of Teddysum. `hahmyg@teddysum.ai`
 - 김한샘(Hansaem Kim), Professor at Yonsei. `khss@yonsei.ac.kr`

## Contributor
 - **신동재(Dongjae Shin)**, dylan1998@seoultech.ac.kr
 - **임현석(Hyeonseok Lim)**, gustjrantk@seoultech.ac.kr
 - 원인호(Inho Won), wih1226@seoultech.ac.kr
 - 김민준(Minjun Kim), mjkmain@seoultech.ac.kr
 - 유한결(Hangyeol Yoo), hgyoo@seoultech.ac.kr
 - 송승우(Seungwoo Song), sswoo@seoultech.ac.kr
 - 육정훈(Jeonghun Yuk), usually670@gmail.com
 - 최창수(Chansu Choi), choics2623@seoultech.ac.kr
 - 송서현(Seohyun Song), alexalex225225@gmail.com