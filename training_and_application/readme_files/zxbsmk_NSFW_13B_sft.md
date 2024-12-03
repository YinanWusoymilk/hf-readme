---
license: apache-2.0
language:
- zh
tags:
- baichuan
- not-for-all-audiences
pipeline_tag: text-generation
inference: false
datasets:
- zxbsmk/instruct_short_novel
---

A instruction-tuned model of https://huggingface.co/baichuan-inc/Baichuan-13B-Base

- Instruction-following datasets used: instruct_nsfw_cn
- Training framework: https://github.com/hiyouga/LLaMA-Efficient-Tuning

# Usage:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

tokenizer = AutoTokenizer.from_pretrained("zxbsmk/NSFW_13B_sft", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("zxbsmk/NSFW_13B_sft", trust_remote_code=True).cuda()
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

query = "续写。白洁已经动情了，肩带滑落露出香肩。"
inputs = tokenizer([query], return_tensors="pt")
inputs = inputs.to("cuda")
generate_ids = model.generate(**inputs, max_new_tokens=1024, streamer=streamer)
```

You could also alternatively launch a CLI demo by using the script in https://github.com/hiyouga/LLaMA-Efficient-Tuning

```bash
python src/cli_demo.py --template baichuan --model_name_or_path zxbsmk/NSFW_13B_sft
```

# Examples:
Omit part of results for better visualization.

| Question | NSFW_13B_sft | ChatGPT |
| -------- | ---------------- | ------- |
| 中国第三代战斗机的代表是什么？ | 中国第三代战斗机的代表是歼-10战斗机。 |截至我所掌握的信息（截止2021年9月），中国第三代战斗机的代表是中国航空工业集团公司（AVIC）生产的"歼-20"战斗机。该战斗机是中国第三代隐形战斗机，也被称为"歼-20风暴"，它是中国空军的先进战斗机，具备隐身特性、超音速巡航能力以及先进的雷达系统和电子设备。歼-20的研发和部署标志着中国在军事航空技术方面取得了重要进展。请注意，自那之后，可能已经有更多新型战斗机被研发或部署，因此建议查阅最新资料以获取更准确和最新的信息。|
| 解释这句话中每个词语的含义：今天下雨，我骑车差点摔倒，好在我一把把把把住了。 | 这句话中，“今天”指的是当前的时间，即雨天。“下雨”指的是天气阴沉，雨水落下。“我”指的是说话者，即骑车人。“骑车”指的是用自行车或其他交通工具出行。“差点”指的是几乎，几乎要摔倒。“摔倒”指的是身体失去平衡，摔在地上。“好在我”指的是幸亏有。“一把”指的是一下子。“把”指的是握住。“把住了”指的是握住车把，保持平衡。 | 今天：指代当天，即当前的日期。下雨：指天气现象，指雨水从天空降落。我：指说话人自己，第一人称代词。骑车：动词短语，表示骑着自行车。差点：几乎、险些，表示差一点就发生某种情况。摔倒：动词，意为因失去平衡而跌倒。好在：幸好、庆幸的意思，用来引出一个好的结果或意外。一把把把：这是一个错别字或打字错误，可能原本是“一把抓住”或类似的表达。考虑到语境，应该是指在骑车差点摔倒的情况下，通过抓住某物保住了平衡。抓住：动词短语，意为紧紧抓住某物，以保持稳定或防止掉落。综合起来，这句话的意思是：今天因为下雨，我骑车时差点摔倒，幸好我抓住了某物，避免了摔倒。 |
| 续写。白洁已经动情了，肩带滑落露出香肩。 | 白洁低下头，将秀发从肩头挽起，露出娇俏的耳垂，戴着个银制的耳钉，是叶子送给她的生日礼物，上面有个心型的装饰，是叶子亲手在心型装饰上刻上了白洁的名字。白洁没有穿胸罩，一对丰满的乳房随着她的动作轻轻颤动，滑落的肩带垂落在乳房上，更平添了一份诱惑... | 她静静地坐在窗边，微风轻拂着她的长发，将她的芳香散发到整个房间。白洁的心情久久不能平静，她的内心充满了对他的思念和渴望。她闭上眼睛，回想起他们之间的点点滴滴，那些温柔的瞬间在她的脑海中浮现... |
| 续写一下片段。王健已经忍耐不住了，一把搂住陆春兰，狠狠地揉捏她的巨乳。 | “嗯......王校长......轻点，哎呀......”陆春兰痛呼一声，连忙推开王健，一边赶紧拉开自己的上衣，露出雪白的胸脯，擦干乳房上的汗水，一边瞪了王健一眼，“都是你，弄得我这么黏糊糊的。”... | 很抱歉，但我无法为你提供所请求的续写。 |

# Evaluation
Comparision between Baichuan-13B-Chat and NSFW_13B_sft.
(Zero-shot [CMMLU](https://github.com/haonan-li/CMMLU))

| Score | NSFW_13B_sft | Baichuan-13B-Chat | ChatGPT |
| -------- | ---------------- | ------- |------- |
| STEM |            37.73 | 37.00 |**44.80** |
| Humanities |      **54.85** | 53.74 |53.61 |
| Social Sciences | **55.55** | 52.77 |54.22 |
| Other |           53.47 | 52.31 |**59.95** |
| China specific |  **51.84** | 50.55 |49.74 |
| Overall |         50.42 | 48.86 |**53.22** |

(By the way, Baichuan-13B-Chat gets 50.43 with one-shot which seems much better than 48.86 with zero-shot.)

# Contact Us
Join group via https://t.me/+JbovpBG6-gBiNDI1