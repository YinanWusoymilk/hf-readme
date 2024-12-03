---
license: apache-2.0
language:
- en
tags:
- Kolors
- text-to-image
- stable-diffusion
library_name: diffusers
---


# Kolors-IP-Adapter-Plus weights and inference code

<div align="center" style="display: flex; justify-content: center; flex-wrap: wrap;">
  <a href="https://github.com/Kwai-Kolors/Kolors"><img src="https://img.shields.io/static/v1?label=Kolors Code&message=Github&color=blue&logo=github-pages"></a> &ensp;
  <a href="https://kwai-kolors.github.io/"><img src="https://img.shields.io/static/v1?label=Team%20Page&message=Page&color=green"></a> &ensp;
  <a href="https://github.com/Kwai-Kolors/Kolors/blob/master/imgs/Kolors_paper.pdf"><img src="https://img.shields.io/static/v1?label=Tech Report&message=Arxiv:Kolors&color=red&logo=arxiv"></a> &ensp;
  <a href="https://kolors.kuaishou.com/"><img src="https://img.shields.io/static/v1?label=Official Website&message=Page&color=green"></a>
</div>

## <a name="Introduction"></a>📖 Introduction

We provide IP-Adapter-Plus weights and inference code based on [Kolors-Basemodel](https://huggingface.co/Kwai-Kolors/Kolors). Examples of Kolors-IP-Adapter-Plus results are as follows:
<img src="demo.png">


**Our improvements**

- A stronger image feature extractor. We employ the Openai-CLIP-336 model as the image encoder, which allows us to preserve more details in the reference images
- More diverse and high-quality training data: We construct a large-scale and high-quality training dataset inspired by the data strategies of other works. We believe that paired training data can effectively improve performance.


## <a name="Evaluation"></a>📊 Evaluation
For evaluation, we create a test set consisting of over 200 reference images and text prompts. We invite several image experts to provide fair ratings for the generated results of different models. The experts rate the generated images based on four criteria: visual appeal, text faithfulness, image faithfulness, and overall satisfaction. Image faithfulness measures the semantic preservation ability of IP-Adapter on reference images, while the other criteria follow the evaluation standards of BaseModel. The specific results are summarized in the table below, where Kolors-IP-Adapter-Plus achieves the highest overall satisfaction score.

|       Model       |  Average Overall Satisfaction | Average Image Faithfulness | Average Visual Appeal | Average Text Faithfulness |
| :--------------: | :--------: | :--------: | :--------: | :--------: |
| SDXL-IP-Adapter-Plus |	2.29	| 2.64	| 3.22	| 4.02 |
| Midjourney-v6-CW |	2.79	| 3.0	| 3.92	| 4.35 |
|    **Kolors-IP-Adapter-Plus**    | **3.04** |  **3.25**    |    **4.45**    |    **4.30**    |

<font color=gray style="font-size:12px">*The ip_scale parameter is set to 0.3 in SDXL-IP-Adapter-Plus, while Midjourney-v6-CW utilizes the default cw scale.*</font>


<img src="compare_demo.png">

<font color=gray style="font-size:12px">*Kolors-IP-Adapter-Plus employs chinese prompts, while other methods use english prompts.*</font>


------

## <a name="Usage"></a>🛠️ Usage

### Requirements

The dependencies and installation are basically the same as the [Kolors-BaseModel](https://huggingface.co/Kwai-Kolors/Kolors).

1. Repository Cloning and Dependency Installation

```bash
apt-get install git-lfs
git clone https://github.com/Kwai-Kolors/Kolors
cd Kolors
conda create --name kolors python=3.8
conda activate kolors
pip install -r requirements.txt
python3 setup.py install
```

2. Weights download [link](https://huggingface.co/Kwai-Kolors/Kolors-IP-Adapter-Plus)：
```bash
huggingface-cli download --resume-download Kwai-Kolors/Kolors-IP-Adapter-Plus --local-dir weights/Kolors-IP-Adapter-Plus
```
or
```bash
git lfs clone https://huggingface.co/Kwai-Kolors/Kolors-IP-Adapter-Plus weights/Kolors-IP-Adapter-Plus
```

3. Inference：
```bash
python ipadapter/sample_ipadapter_plus.py ./ipadapter/https://raw.githubusercontent.com/junqiangwu/Kolors/master/ipadapter/asset/test_ip.jpg "穿着黑色T恤衫，上面中文绿色大字写着“可图”"

python ipadapter/sample_ipadapter_plus.py ./ipadapter/https://raw.githubusercontent.com/junqiangwu/Kolors/master/ipadapter/asset/test_ip2.png "一只可爱的小狗在奔跑"

# The image will be saved to "scripts/outputs/"
```


**Note**

The IP-Adapter-FaceID model based on Kolors will also be released soon!


### Acknowledgments
- Thanks to [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) for providing the codebase.
<br>