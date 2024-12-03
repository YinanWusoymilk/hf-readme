---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/model-cards
license: other
inference: false
---

# BLOOMChat V1.0

<!-- Provide a quick summary of what the model is/does. -->

BLOOMChat is a 176 billion parameter multilingual chat model. It is instruction tuned from [BLOOM (176B)](https://huggingface.co/bigscience/bloom) on assistant-style conversation datasets and supports conversation, question answering and generative answers in multiple languages.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** [SambaNova Systems](https://sambanova.ai/)
- **Co-developed by:** [Together Computer](https://www.together.xyz/)
- **Model type:** Language Model
- **Language(s):** Multiple; see [training data from BLOOM](https://huggingface.co/bigscience/bloom#training-data)
- **License:** BLOOMChat-176B LICENSE v1.0
- **Instruction Tuned from model:** [BigScience Group BLOOM](https://huggingface.co/bigscience/bloom)

### Basic Information

<!-- Provide the basic links for the model. -->
- **Blog Post**: [Link](https://sambanova.ai/blog/introducing-bloomchat-176b-the-multilingual-chat-based-llm/)
- **Discord**: [Link](https://discord.com/invite/8z2Pe7cpRv)
- **HF Hosting**: [Chat with me!](https://huggingface.co/spaces/sambanovasystems/BLOOMChat)
- **Github**: [Link](https://github.com/sambanova/bloomchat)

### Licensing

To increase accessibility and to support the open-source community, SambaNova is releasing BLOOMChat under a modified version of the Apache 2.0 license, which includes use-based restrictions from BLOOM’s RAIL license. While use-based restrictions are necessarily passed through, there are no blanket restrictions on reuse, distribution, commercialization or adaptation. [Please review SambaNova’s BLOOMChat-176B License](LICENSE)

## Uses
<details>
<summary>Click to expand</summary>
<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->
This model is intended for commercial and research use.


### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->


BLOOMChat should NOT be used for:

- Mission-critical applications
- Applications that involve the safety of others
- Making highly important decisions
- Important automated pipelines

This model is still in early development and can be prone to mistakes and hallucinations, there is still room for improvement. This model is intended to provide the community with a multilingual chat LLM baseline.

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users should be made aware of the risks, biases, limitations, and restrictions of the model, which are listed down at the bottom of the page. 

</details>


---
## How to Get Started with the Model

<details>
<summary>Click to expand</summary>

### Loading in model with Huggingface

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("sambanovasystems/BLOOMChat-176B-v1")
model = AutoModelForCausalLM.from_pretrained("sambanovasystems/BLOOMChat-176B-v1", device_map="auto", torch_dtype="auto")
```

### Quick Start Inference on SambaNova's in-house Reconfigurable Dataflow Unit (RDU)

The inference code to run the model can be found our [github repo](https://github.com/sambanova/bloomchat/blob/main/rdu_quick_start/inference.py). This code requires the [SambaFlow](https://docs.sambanova.ai/developer/latest/sambaflow-intro.html) SDK to execute. For those interested in running models on RDUs, [please feel free to get in touch](https://sambanova.ai/getstarted).

### Quick Start Inference on GPU

First create a python virtual environment for these packages

```
python3 -m venv bloomchat_venv
source bloomchat_venv/bin/activate
pip install --upgrade pip
```

<!-- Please follow this section [Inference solutions for BLOOM 176B](https://github.com/huggingface/transformers-bloom-inference#bloom-inference-via-command-line) in the Huggingface Tutorial for environment set up and stop before the [BLOOM inference via command-line
](https://github.com/huggingface/transformers-bloom-inference#bloom-inference-via-command-line) section. -->

```
pip install flask flask_api gunicorn pydantic accelerate huggingface_hub>=0.9.0 deepspeed>=0.7.3 deepspeed-mii==0.0.2
```
And then
```
pip install transformers==4.27.0
```

You will see messages like this 
```
ERROR: deepspeed-mii 0.0.2 has requirement transformers==4.21.2, but you'll have transformers 4.27.0 which is incompatible.
Installing collected packages: transformers
  Found existing installation: transformers 4.21.2
    Uninstalling transformers-4.21.2:
      Successfully uninstalled transformers-4.21.2
Successfully installed transformers-4.27.0
```

Now let's git clone the [huggingface/transformers-bloom-inference](https://github.com/huggingface/transformers-bloom-inference) repo.
```
git clone https://github.com/huggingface/transformers-bloom-inference.git
cd transformers-bloom-inference/
```
And then you need to modify two files in this [transformers-bloom-inference](https://github.com/huggingface/transformers-bloom-inference) repo:

- Modifying `inference_server/models/hf_accelerate.py`
    - This is because for our testing of this repo we used 4 80GB A100 GPUs and would run into memory issues
- Modifying `inference_server/cli.py`
    - This is because the model was trained using specific human, bot tags
    - Trailing spaces may lead to subpar performance

Modifications for `inference_server/models/hf_accelerate.py`:

```diff
diff --git a/inference_server/models/hf_accelerate.py b/inference_server/models/hf_accelerate.py
index 9be3c3f..a8ecb1d 100644
--- a/inference_server/models/hf_accelerate.py
+++ b/inference_server/models/hf_accelerate.py
@@ -1,4 +1,5 @@
 from argparse import Namespace
+from accelerate.utils.modeling import get_max_memory
 
 import torch
 
@@ -12,6 +13,12 @@ class HFAccelerateModel(Model):
 
         kwargs = {"pretrained_model_name_or_path": args.model_name, "device_map": "auto"}
 
+        original_max_memory_dict = get_max_memory()
+
+        reduce_max_memory_dict = {device_key: int(original_max_memory_dict[device_key] * 0.85) for device_key in original_max_memory_dict}
+
+        kwargs["max_memory"] = reduce_max_memory_dict
+
         if get_world_size() > 1:
             kwargs["device_map"] = "balanced_low_0"

```

Modifications for `inference_server/cli.py`:

```diff
diff --git a/inference_server/cli.py b/inference_server/cli.py
index fc903d5..5450236 100644
--- a/inference_server/cli.py
+++ b/inference_server/cli.py
@@ -22,6 +22,9 @@ def main() -> None:
     while True:
         input_text = input("Input text: ")
 
+        input_text = input_text.strip()
+        modified_input_text = f"<human>: {input_text}\n<bot>:"
+
         if input("change generate_kwargs? [y/n] ") == "y":
             while True:
                 try:
@@ -33,7 +36,7 @@ def main() -> None:
                     print("message =", e_message)
                     continue
 
-        response = model.generate(text=[input_text], generate_kwargs=generate_kwargs)
+        response = model.generate(text=[modified_input_text], generate_kwargs=generate_kwargs)
 
         print_rank_0("Output text:", response.text[0])
         print_rank_0("Generated tokens:", response.num_generated_tokens[0])

```
And now you are good to go!

Running command for bf16, NO sampling
```
python -m inference_server.cli --model_name sambanovasystems/BLOOMChat-176B-v1 --model_class AutoModelForCausalLM --dtype bf16 --deployment_framework hf_accelerate --generate_kwargs '{"do_sample": false, "max_new_tokens": 512}'
```
Running command for bf16, YES sampling
```
python -m inference_server.cli --model_name sambanovasystems/BLOOMChat-176B-v1 --model_class AutoModelForCausalLM --dtype bf16 --deployment_framework hf_accelerate --generate_kwargs '{"do_sample": true, "temperature": 0.8, "repetition_penalty": 1.2, "top_p": 0.9, "max_new_tokens": 512}'
```
---
Running command for int8 (sub optimal performance, but fast inference time) NO sampling:
```
python -m inference_server.cli --model_name sambanovasystems/BLOOMChat-176B-v1 --model_class AutoModelForCausalLM --dtype int8 --deployment_framework hf_accelerate --generate_kwargs '{"do_sample": false, "max_new_tokens": 512}'
```
Running command for int8 (sub optimal performance, but fast inference time) YES sampling:
```
python -m inference_server.cli --model_name sambanovasystems/BLOOMChat-176B-v1 --model_class AutoModelForCausalLM --dtype int8 --deployment_framework hf_accelerate --generate_kwargs '{"do_sample": true, "temperature": 0.8, "repetition_penalty": 1.2, "top_p": 0.9, "max_new_tokens": 512}'
```

**DISCLAIMER:** When using int8, the results will be subpar compared to bf16 as the model is being [quantized](https://huggingface.co/blog/hf-bitsandbytes-integration#introduction-to-model-quantization).

### Suggested Inference Parameters
- Temperature: 0.8
- Repetition penalty: 1.2
- Top-p: 0.9
- Max generated tokens: 512

### Suggested Prompts To Try in GPU Tutorial
```
Input text: Write a script in which Bob accidentally breaks his dad's guitar
```

```
Input text: Create an itemized list of tasks to complete to start a clothing brand
```

```
Input text: 十七岁的风是什么颜色的?
```


</details>

---

## Some example completions for English

<details>
<summary>Click to expand</summary>

```
<human>: What does it mean for the Fed to raise or lower interest rates?
<bot>: The Federal Reserve (also known as the Fed) is the central banking system of the United States.  It was created in 1913, and is an independent agency of the federal government.  The Fed has a dual mandate of maximizing employment and stabilizing prices.  The Fed sets interest rates, and can influence the money supply and the credit markets through its actions.

Raising interest rates means that the Fed is trying to reduce the money supply in the economy, and is trying to discourage borrowing and encourage saving.  Lowering interest rates means that the Fed is trying to stimulate economic growth by encouraging borrowing and reducing the cost of credit.

The Fed raises or lowers interest rates in order to influence the economy and achieve its goals for employment and price stability.  Interest rates are one of the primary tools that the Fed uses to achieve its goals.
```

```
<human>: Write an engaging and well-written property listing description for selling a house. Address of the house and some of the details are given to you. Fill in the information gap with hallucinations if needed.

Property Address: 412 Monterey Ave, Capitola, CA 95010
Parking: 3 cars + a finished single car garage
Details:
- open floorplan
- window with views to park/mountains
- Kitchen with shaker cabinetry and white Calcatta quartz counters
<bot>: This home at 412 Monterey Ave, Capitola, CA 95010 is the perfect place to call home. With its open floor plan, it provides the perfect space for entertaining guests. The kitchen is equipped with shaker cabinetry and white Calcatta quartz counters, providing the perfect space to create culinary masterpieces. The window with views to the park and mountains provide a beautiful view of the outdoors, making this home feel like a piece of paradise. The three-car garage and finished single car garage provide ample parking space, making this home a must-see for anyone looking for a new home.

```

```
<human>: What is artificial intelligence? Explain it so an 8 year old will understand.
<bot>: Artificial Intelligence (AI) is a computer program or machine that can do things that would normally require human intelligence, such as recognizing patterns, making decisions, and learning from experience. AI can be found in many places, such as self-driving cars, smartphones, and even robots. AI is used to make things easier for people, like when your smartphone can translate text into another language or when your voice-controlled speaker can play music for you.
AI works by using algorithms and big data to learn and improve over time. For example, self-driving cars use AI to analyze the environment around them and make decisions about how to drive. The car gathers data from its sensors, processes it using algorithms, and adjusts its behavior accordingly. This process is called machine learning.
AI is still a developing technology, and there are still many things that AI programs cannot do yet. However, as AI continues to evolve, it is likely that it will become more and more capable of performing tasks that were once thought to require human intelligence.

```

</details>

---

## Some example completions for Multilingual
<details>
<summary>Click to expand</summary>

#### Arabic

```
<human>: هل العمل نصف دوام فكرة جيدة لمراهقين بين عمر ١٥ و ١٩ عام
<bot>: نعم، يمكن أن تكون فكرة جيدة لبعض المراهقين في هذا العمر. هناك العديد من الفوائد التي قد يحققها المراهقون إذا عملوا بنصف دوام:

- يساعدهم على تعلم المسؤولية وإدارة الوقت: عندما يعمل المراهق بنصف دوام، فإنه يتعلم كيفية إدارة وقته بشكل فعال وكيفية تقسيم ساعات عمله إلى مهام أصغر.
- يحسن مهارات التواصل والعمل الجماعي: غالبًا ما يكون مكان العمل بيئة متعددة الثقافات حيث يلتقي المراهقون بمجموعة متنوعة من الأشخاص ويتعلمون كيفية التعاون معهم وتبادل الأفكار.
- يوفر فرصة للتعرف على عالم العمل: يتيح العمل للمراهق التعرف على عالم العمل واكتساب خبرة عملية قيمة ستساعده لاحقًا عند البحث عن وظيفة أو بدء حياته المهنية.
- يعزز الشعور بالمسؤولية والثقة بالنفس: عندما يعمل المراهق بنصف دوام ويحصل على دخل خاص به، فإنه يكتسب شعورًا أكبر بالمسؤولية والثقة بالنفس.

ومع ذلك، لا ينبغي إجبار المراهقين على العمل بنصف دوام دون موافقتهم المسبقة. يجب أيضًا مراعاة أعمارهم وقدراتهم البدنية والعقلية قبل توظيفهم.
```

**DISCLAIMER**: Text ordering may be off for Arabic due to code block not being able to render
#### Chinese

```
<human>: 请向我推荐一部周末看的电影并说明原因。
<bot>: “强烈向您推荐《美丽人生》这部影片。该片由罗伯托·贝尼尼自导自演，讲述了二战时期一对犹太父子被送进了纳粹集中营，父亲用自己的想象力为儿子编织了一个美好童真的世界，让儿子的心灵没有受到丝毫伤害的故事。

该片被誉为“最伟大的战争片”、“人类有史以来最佳影片之一”，豆瓣评分高达9.6分。它不仅是一部感人的亲情片，更是一部富含哲理的励志片和人生启示录。片中父亲的乐观豁达、幽默风趣的人生态度，对任何事都抱有积极热情的态度，即使在残酷无比的集中营里也是如此，深深地感染着观众。同时，这也是一部关于爱与希望的电影，让我们更加珍惜当下所拥有的一切，学会如何去爱身边的每一个人。

总之，这是一部值得一看再看的好电影，相信您一定会喜欢的！

```

#### French

```
<human>: Il y a t’il un petit-déjeuner de 700-1000 calories sans oeuf mais qui inclut des protéines.
<bot>: Oui, voici une recette de petit déjeuner à base d'avoine et de fromage blanc :
Ingrédients :
- 1 tasse (250 ml) de lait d'amande ou autre lait végétal
- 2 cuillères à soupe bombées (30 g) de flocons d'avoine
- 1/2 banane mûre écrasée
- 1/4 de pomme fraîche épluchée et coupée en dés
- 1 cuillère à soupe de beurre d'amande ou autre purée d'oléagineux
- 1 cuillère à café de cannelle moulue
- 1 pincée de sel
Préparation :
1. Dans une petite casserole, faites chauffer le lait jusqu'à ce qu'il soit chaud.
2. Ajoutez les flocons d'avoine, la banane, la pomme, le beurre d'amande, la cannelle et le sel dans le bol du mixeur et mélangez bien pour obtenir une pâte homogène.
3. Versez le mélange dans le lait chaud et remuez rapidement avec une spatule en bois pour éviter que les flocons d'avoine ne s'agglutinent au fond de la casserole.
4. Laissez mijoter sur feu doux pendant environ 5 minutes tout en continuant de remuer régulièrement.
5. Transférez ensuite le porridge dans un bol et servez immédiatement. Vous pouvez ajouter quelques fruits rouges frais pour décorer et apporter encore plus de gourmandise à votre petit déjeuner ! Bon appétit !
```

#### Hindi
```
<human>: दिल्ली से जयपुर कैसे जाये? बस से या कार से? दोनो के बारे मे विस्तार मे बताये.
<bot>: दिल्ली से जयपुर जाने का सबसे आसान और तेज़ तरीका है कि आप अपनी खुद की कार लेकर जाएं, क्योंकि यह आपको अपने समय पर निर्भर रहने की स्वतंत्रता देता है। हालांकि, यदि आपके पास अपनी कार नहीं है, तो आप दिल्ली से जयपुर तक एक निजी वाहन किराए पर ले सकते हैं। यदि आप सार्वजनिक परिवहन (बस) का उपयोग करना चाहते हैं, तो दिल्ली में कई सरकारी और निजी बस सेवाएं उपलब्ध हैं जो जयपुर को जोड़ती हैं। दिल्ली से जयपुर जाने वाली कुछ प्रमुख बसें हैं-
1. राजस्थान रोडवेज: ये राज्य सरकार द्वारा संचालित बसें हैं जो दिल्ली से जयपुर के बीच चलती हैं। ये नियमित रूप से चलती हैं और इनके लिए अग्रिम आरक्षण आवश्यक नहीं है।
2. ALSA: यह एक निजी कंपनी है जो दिल्ली से जयपुर के बीच नियमित रूप से चलती है। इसके टिकटों की बुकिंग ऑनलाइन और ऑफलाइन दोनों माध्यमों से की जा सकती है।
3. RedBus: यह एक ऑनलाइन बस बुकिंग वेबसाइट है जहां से आप दिल्ली से जयपुर के बीच चलनेवाली विभिन्न कंपनियों की बसों में सीट आरक्षित करा सकते हैं।
4. Ola and Uber: इन ऐप्स का उपयोग करके आप दिल्ली से जयपुर तक कैब राइड बुक कर सकते हैं, लेकिन ध्यान रखें कि यह विकल्प सस्ता नहीं होगा। दिल्ली से जयपुर जाने का सबसे अच्छा विकल्प आपकी व्यक्तिगत आवश्यकताओं, बजट, और उपलब्धता पर निर्भर करता है। यदि आप अपनी खुद की कार रखते हैं, तो इसका लाभ उठाएं अन्यथा किसी भी सार्वजनिक परिवहन साधन का चयन करें जो आपकी आवश्यकताओं को पूरा करे।
```

#### Spanish

```
<human>: ¿Me puedes dar algunas recomendaciones de juegos? Estoy buscando juegos de rol con un sistema de magia único, un sistema de construcción único y una buena historia. Por favor limítate a juegos que se puedan jugar en PC directamente, o por emulación.
<bot>: Claro! Aquí te dejo tres recomendaciones:
1. The Outer Worlds: es un juego de rol de ciencia ficción con un sistema de magia basado en la tecnología alienígena que permite al jugador personalizar sus habilidades para adaptarse a su estilo de juego.
2. Divinity: Original Sin 2 - Definitive Edition: este juego combina elementos de RPG con estrategia en tiempo real (RTS), lo que le da al jugador un control total sobre cómo construir y mejorar su personaje y el mundo que lo rodea.
3. Pillars of Eternity: esta aventura de fantasía oscura tiene lugar en un vasto mundo abierto donde los jugadores pueden elegir entre diferentes clases y desarrollar relaciones con otros personajes del juego. La mecánica de combate está basada en turnos y utiliza hechizos y armas cuerpo a cuerpo.
Estos son solo algunos ejemplos de juegos que podrían interesarte según tus criterios. Hay muchos más títulos disponibles en el mercado que podrían ajustarse a tu gusto, así que no dudes en explorar otras opciones si estos juegos no cumplen con tus expectativas.
```


</details>

---

## Evaluation Graphs

<details>
<summary>Click to expand</summary>

<!-- This section describes the evaluation protocols and provides the results. -->

![Human evaluation](images/Human_evaluation.png)
<figure style="text-align:center;">
    <figcaption><b>BLOOMChat vs Baselines Model in Human Preference Rankings</b></figcaption>
</figure>
<br>

![Human evaluation against GPT4](images/Human_evaluation_gpt4.png)
<figure style="text-align:center;">
    <figcaption><b>BLOOMChat vs GPT-4 in Human Preference Ranking</b></figcaption>
</figure>
<br>

![Multilingual evaluation](images/Multilingual_capabilities_comparison.png)
<figure style="text-align:center;">
    <figcaption><b>BLOOMChat surpasses other Bloom variants and state-of-the-art open-source chat models in translation tasks [NOTE: Evaluation of the BLOOM and BLOOMZ in WMT18 en->zh zh->en used (human, bot) ChatML tags due to an unintentional configuration. Results might be suboptimal.]</b></figcaption>
</figure>
<br>

</details>

---

## Training Details

<details>
<summary>Click to expand</summary>

### Training Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

- [OIG dataset from OpenChatKit](https://huggingface.co/datasets/laion/OIG)
- [Dolly 2.0](https://huggingface.co/datasets/databricks/databricks-dolly-15k)
- [Oasst1](https://huggingface.co/datasets/OpenAssistant/oasst1)

### Training Procedure 

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

We trained BLOOMChat with [SambaNova DataScale systems](https://sambanova.ai/products/datascale/) with SambaNova's in-house Reconfigurable Dataflow Unit (RDU). We started from [BLOOM (176B)](https://huggingface.co/bigscience/bloom), an open-source multilingual LLM pretrained by the [BigScience group](https://huggingface.co/bigscience). We instruction-tune BLOOM (176B) on OpenChatKit with each data source subsampled to 100k for one epoch, followed by three epochs over the combined OpenChatKit and Dolly 2.0. 
All of the code used to prepare the datasets and the scripts to run training and inference are open-sourced and freely available at [sambanova/bloomchat](https://github.com/sambanova/bloomchat/tree/main)


### Prompting Style Used For Training
```
<human>: {input1 that the user wants from the bot}
<bot>: {response1}</s>
<human>: {input2 that the user wants from the bot}
<bot>: {response2}</s>
```

### Hyperparameters

**Instruction-tuned Training on OIG**

- Hardware: SambaNova Reconfigurable Dataflow Unit (RDU)
- Optimizer: AdamW
- Grad accumulation: 1
- Epochs: 1
- Global Batch size: 128
- Batch tokens: 128 * 2048 = 262,144 tokens
- Learning Rate: 1e-5
- Learning Rate Scheduler: Cosine Schedule with Warmup
- Warmup Steps: 0
- End Learning Ratio: 0.1
- Weight decay: 0.1

**Instruction-tuned Training on Dolly 2.0 and Oasst1**

- Hardware: SambaNova Reconfigurable Dataflow Unit (RDU)
- Optimizer: AdamW
- Grad accumulation: 1
- Epochs: 3
- Global Batch size: 128
- Batch tokens: 128 * 2048 = 262,144 tokens
- Learning Rate: 1e-5
- Learning Rate Scheduler: Cosine Schedule with Warmup
- Warmup Steps: 0
- End Learning Ratio: 0.1
- Weight decay: 0.1

</details>

---

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

Like all LLMs, BLOOMChat has certain limitations:
- Hallucination: BLOOMChat may sometimes generate responses that contain plausible-sounding but factually incorrect or irrelevant information.
- Code Switching: The model might unintentionally switch between languages or dialects within a single response, affecting the coherence and understandability of the output.
- Repetition: BLOOMChat may produce repetitive phrases or sentences, leading to less engaging and informative responses.
- Coding and Math: The model's performance in generating accurate code or solving complex mathematical problems may be limited.
- Toxicity: BLOOMChat may inadvertently generate responses containing inappropriate or harmful content.

## Acknowledgment

We would like to extend our gratitude to [Together](https://www.together.xyz/) for their insightful technical discussions on overall project planning, data processing, model training, human evaluation experiment design, open-source endeavors, and their contributions on data processing code on OpenChatKit, OASST1, and Dolly 2.0.

We are grateful to the various researchers and open-source projects that have contributed to the development of BLOOMChat. We thank [BigScience](https://bigscience.huggingface.co/) for providing the [BLOOM](https://huggingface.co/bigscience/bloom) model, which served as the base for our instruction tuning. We also thank [LAION](https://laion.ai/) for their [OIG dataset](https://huggingface.co/datasets/laion/OIG), OpenAssistant Conversations Dataset ([OASST1](https://huggingface.co/datasets/OpenAssistant/oasst1)) and also thank [Databricks](https://www.databricks.com/) for providing [Dolly 2.0](https://huggingface.co/datasets/databricks/databricks-dolly-15k), to provide the dataset that we instruction tuned on.

We appreciate [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness) and [BigScience](https://bigscience.huggingface.co/) for their essential benchmarking contributions, which is very helpful in evaluating BLOOMChat's performance. We appreciate the inspiration from the wave of various recent open-source chat models, including [OpenAssistant-30B](https://huggingface.co/OpenAssistant/oasst-sft-7-llama-30b-xor), [LLaMA-Adapter-V2-65B](https://github.com/ZrrSkywalker/LLaMA-Adapter/tree/main/llama_adapter_v2_chat65b), [Vicuna-13b](https://huggingface.co/lmsys/vicuna-13b-delta-v0), [Koala-13b](https://huggingface.co/TheBloke/koala-13B-HF), [OASST-Pythia-12b](https://huggingface.co/OpenAssistant/oasst-sft-1-pythia-12b), [Alpaca-13b](https://huggingface.co/anon8231489123/gpt4-x-alpaca-13b-native-4bit-128g), [ChatGLM-6b](https://github.com/THUDM/ChatGLM-6B), [FastChat-T5-3b](https://huggingface.co/lmsys/fastchat-t5-3b-v1.0), [Dolly-v2-12b](https://huggingface.co/databricks/dolly-v2-12b), [LLaMA-13b](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/), [StableLM-Tuned-Alpha-7b](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b), [RedPajama-INCITE-Chat-7B-v0.1](https://huggingface.co/togethercomputer/RedPajama-INCITE-Chat-7B-v0.1), [RedPajama-INCITE-Chat-3B-v1](https://huggingface.co/togethercomputer/RedPajama-INCITE-Base-7B-v0.1), [MPT-7B-Chat](https://huggingface.co/mosaicml/mpt-7b-chat) and so on. We look forward to witnessing the continued growth and success of open-source chat-based models.

We highly appreciate the hard work and dedication of these researchers and organizations towards the advancement of the open-source community. Their contributions were invaluable in the development of BLOOMChat, and we hope that our model can contribute to further advancements in the field.

## Cite BLOOMChat
```
@software{bloomchat,
  title = {{BLOOMChat: a New Open Multilingual Chat LLM}},
  author = {SambaNova Systems, Together Computer},
  url = {https://huggingface.co/sambanovasystems/BLOOMChat-176B-v1}
  month = {5},
  year = {2023},
  version = {1.0},
}
```