---
base_model: mistralai/Mistral-7B-v0.1
tags:
- mistral
- instruct
- finetune
- chatml
- gpt4
- synthetic data
- distillation
- multimodal
- llava
model-index:
- name: Nous-Hermes-2-Vision
  results: []
license: apache-2.0
language:
- en
---

# Nous-Hermes-2-Vision - Mistral 7B


![image/png](https://camo.githubusercontent.com/b09dc35a93b4b70748fa4e2f307b011cd3d548369dd926ec9a2d3a51f7b3721e/68747470733a2f2f66696c65732e6f616975736572636f6e74656e742e636f6d2f66696c652d6b4437565358734f5649576472624b3042353662686644363f73653d323032332d31322d3033543137253341333425334135385a2673703d722673763d323032312d30382d30362673723d6226727363633d6d61782d6167652533443331353336303030253243253230696d6d757461626c6526727363643d6174746163686d656e7425334225323066696c656e616d6525334439643530333039622d356236342d343964302d623832362d6165316638366132396661382e77656270267369673d50396973694b4679654a54435a47424b526d45494b3043586e6e55676c6334704a583071312532425478666a34253344)

*In the tapestry of Greek mythology, Hermes reigns as the eloquent Messenger of the Gods, a deity who deftly bridges the realms through the art of communication. It is in homage to this divine mediator that I name this advanced LLM "Hermes," a system crafted to navigate the complex intricacies of human discourse with celestial finesse.*

## Model description

Nous-Hermes-2-Vision stands as a pioneering Vision-Language Model, leveraging advancements from the renowned **OpenHermes-2.5-Mistral-7B** by teknium. This model incorporates two pivotal enhancements, setting it apart as a cutting-edge solution:

- **SigLIP-400M Integration**: Diverging from traditional approaches that rely on substantial 3B vision encoders, Nous-Hermes-2-Vision harnesses the formidable SigLIP-400M. This strategic choice not only streamlines the model's architecture, making it more lightweight, but also capitalizes on SigLIP's remarkable capabilities. The result? A remarkable boost in performance that defies conventional expectations.

- **Custom Dataset Enriched with Function Calling**: Our model's training data includes a unique feature – function calling. This distinctive addition transforms Nous-Hermes-2-Vision into a **Vision-Language Action Model**. Developers now have a versatile tool at their disposal, primed for crafting a myriad of ingenious automations.

This project is led by [qnguyen3](https://twitter.com/stablequan) and [teknium](https://twitter.com/Teknium1).
## Training
### Dataset
- 220K from **LVIS-INSTRUCT4V**
- 60K from **ShareGPT4V**
- 150K Private **Function Calling Data**
- 50K conversations from teknium's **OpenHermes-2.5**

## Usage
### Prompt Format
- Like other LLaVA's variants, this model uses Vicuna-V1 as its prompt template. Please refer to `conv_llava_v1` in [this file](https://github.com/qnguyen3/hermes-llava/blob/main/llava/conversation.py)
- For Gradio UI, please visit this [GitHub Repo](https://github.com/qnguyen3/hermes-llava)

### Function Calling
- For functiong calling, the message should start with a `<fn_call>` tag. Here is an example:

```json
<fn_call>{
  "type": "object",
  "properties": {
    "bus_colors": {
      "type": "array",
      "description": "The colors of the bus in the image.",
      "items": {
        "type": "string",
        "enum": ["red", "blue", "green", "white"]
      }
    },
    "bus_features": {
      "type": "string",
      "description": "The features seen on the back of the bus."
    },
    "bus_location": {
      "type": "string",
      "description": "The location of the bus (driving or pulled off to the side).",
      "enum": ["driving", "pulled off to the side"]
    }
  }
}
```

Output:
```json
{
  "bus_colors": ["red", "white"],
  "bus_features": "An advertisement",
  "bus_location": "driving"
}
```

## Example

### Chat
![image/png](https://i.ibb.co/tMg8h2t/Screenshot-from-2023-12-04-00-13-59.png)

### Function Calling
Input image:

![image/png](https://www.slcmenu.com/wp-content/uploads/2017/11/In-N-Out-Burger-menu-2020-982x1024.jpg)

Input message:
```json
<fn_call>{
    "type": "object",
    "properties": {
      "food_list": {
        "type": "array",
        "description": "List of all the food",
        "items": {
          "type": "string",
        }
      },
    }
}
```

Output:
```json
{
    "food_list": [
        "Double Burger",
        "Cheeseburger",
        "French Fries",
        "Shakes",
        "Coffee"
    ]
}
```
