---
license: openrail
datasets:
- Gustavosta/Stable-Diffusion-Prompts
---
## Model Description

## 重要声明
本人郑重声明：本模型原则上禁止用于训练基于明星、公众人物肖像的风格模型训练，因为这会带来争议，对AI社区的发展造成不良的负面影响。 如各位一定要违反以上声明训练相关模型并公开发布，请在您的发布说明中删除与本模型有关的一切描述。感谢各位使用者的支持与理解。

In principle, this model is prohibited from being used for training style models based on portraits of celebrities and public figures, because it will cause controversy and have a negative impact on the development of the AI community. If you must violate the above statement to train the relevant model and release it publicly, please delete all descriptions related to this model in your release notes. Thank you for your support and understanding.

<!-- Provide a longer summary of what this model is. -->
该模型基于basil mix,dreamlike,ProtoGen等优秀模型微调，融合而来。
用于解决上述模型在绘制亚洲、中国元素内容时，只能绘制丑陋的刻板印象脸的问题。
同时也能改善和减少绘制亚洲、中国元素内容时，得到更接近tags的绘制内容。
This model based on basil mix,dreamlike,ProtoGen,etc. After finetune and merging, it solved the big problem that the other model can only draw ugly stereotyped woman faces from hundreds years ago When drawing Asian and Chinese elements.
This model can also improve the drawing content of Asian and Chinese elements to get closer to tags.
# 基于dreamlike微调与AsiaFacemix效果图
Based on dreamlike finetune example：
![1.png](https://s3.amazonaws.com/moonup/production/uploads/1674043921260-636c3fa9aae2da3c76ba966b.png)
![2.png](https://s3.amazonaws.com/moonup/production/uploads/1674043993544-636c3fa9aae2da3c76ba966b.png)
![37.png](https://s3.amazonaws.com/moonup/production/uploads/1674044034015-636c3fa9aae2da3c76ba966b.png)

# 基于Image to Image效果图
Based on Image to Image example：
![s1.png](https://s3.amazonaws.com/moonup/production/uploads/1674044372718-636c3fa9aae2da3c76ba966b.png)
![S2.png](https://s3.amazonaws.com/moonup/production/uploads/1674044468671-636c3fa9aae2da3c76ba966b.png)

# 添加国风汉服lora模型
Added Chinese Hanfu LORA model
lora-hanfugirl-v1
V1模型基于真实的汉服照片训练，相对于v1-5，有更细腻美丽的脸部。
The V1 model is trained on real Hanfu photos and has more delicate and beautiful faces than v1-5.
![lora-1-05.png](https://s3.amazonaws.com/moonup/production/uploads/1675083455418-636c3fa9aae2da3c76ba966b.png)
![lora-1-0502.jpg](https://s3.amazonaws.com/moonup/production/uploads/1675083514690-636c3fa9aae2da3c76ba966b.jpeg)

lora-hanfugirl-v1-5
V1.5模型同样基于真实的汉服照片训练，相对于v1,对不同的多个模型和不同分辨下的图片兼容性更好。
V1.5 model is also trained on real Hanfu photos. Compared with v1, it has better compatibility for different multiple faces, scene and pictures under different resolution.
![lora0501.png](https://s3.amazonaws.com/moonup/production/uploads/1675083569243-636c3fa9aae2da3c76ba966b.png)
![lora0502.png](https://s3.amazonaws.com/moonup/production/uploads/1675083579745-636c3fa9aae2da3c76ba966b.png)