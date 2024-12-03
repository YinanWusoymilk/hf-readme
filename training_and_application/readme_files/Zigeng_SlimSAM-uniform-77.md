---
license: apache-2.0
tags:
- slimsam
---

# SlimSAM: 0.1% Data Makes Segment Anything Slim
<div align="center">
<img src="images/paper/intro.PNG" width="66%">
<img src="images/paper/everything.PNG" width="100%">
</div>

> **0.1% Data Makes Segment Anything Slim**   
> [Zigeng Chen](https://github.com/czg1225), [Gongfan Fang](https://fangggf.github.io/), [Xinyin Ma](https://horseee.github.io/), [Xinchao Wang](https://sites.google.com/site/sitexinchaowang/)   
> [Learning and Vision Lab](http://lv-nus.org/), National University of Singapore  
> Paper: [[Arxiv]](https://arxiv.org/abs/2312.05284)

## Introduction

<div align="center">
<img src="images/paper/process.PNG" width="100%">
</div>

**SlimSAM** is a novel SAM compression method, which efficiently reuses pre-trained SAMs without the necessity for extensive retraining. This is achieved by the efficient reuse of pre-trained SAMs through a unified pruning-distillation framework. To enhance knowledge inheritance from the original SAM, we employ an innovative alternate slimming strategy that partitions the compression process into a progressive procedure. Diverging from prior pruning techniques, we meticulously prune and distill decoupled model structures in an alternating fashion. Furthermore, a novel label-free pruning criterion is also proposed to align the pruning objective with the optimization target, thereby boosting the post-distillation after pruning.

![Frame](images/paper/frame.PNG?raw=true)

SlimSAM achieves approaching performance while reducing the parameter counts to **0.9\% (5.7M)**, MACs to **0.8\% (21G)**, and requiring mere **0.1\% (10k)** of the training data when compared to the original SAM-H. Extensive experiments demonstrate that our method realize significant superior performance while utilizing over **10 times** less training data when compared to other SAM compression methods.

## Visualization Results

Qualitative comparison of results obtained using point prompts, box prompts, and segment everything prompts are shown in the following section.

### Segment Everything Prompts
<div align="center">
  <img src="images/paper/everything2.PNG" width="100%">
</div>

### Box Prompts and Point Prompts
<div align="center">
  <img src="images/paper/prompt.PNG" width="100%">
</div>


## Quantitative Results

We conducted a comprehensive comparison encompassing performance, efficiency, and training costs with other SAM compression methods and structural pruning methods.

### Comparing with other SAM compression methods.
<div align="center">
  <img src="images/paper/compare_tab1.PNG" width="100%">
</div>

### Comparing with other structural pruning methods.
<div align="center">
  <img src="images/paper/compare_tab2.PNG" width="50%">
</div>




## <a name="Models"></a>Model Using

Fast state_dict loading for local uniform pruning SlimSAM-50 model:

``` python
model = SamModel.from_pretrained("Zigeng/SlimSAM-uniform-77").to("cuda")
processor = SamProcessor.from_pretrained("Zigeng/SlimSAM-uniform-77")

img_url = "https://huggingface.co/ybelkada/segment-anything/resolve/main/assets/car.png"
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert("RGB")
input_points = [[[450, 600]]] # 2D localization of a window
inputs = processor(raw_image, input_points=input_points, return_tensors="pt").to("cuda")
outputs = model(**inputs)
masks = processor.image_processor.post_process_masks(outputs.pred_masks.cpu(), inputs["original_sizes"].cpu(), inputs["reshaped_input_sizes"].cpu())
scores = outputs.iou_scores
```

## BibTex of our SlimSAM
If you use SlimSAM in your research, please use the following BibTeX entry. Thank you!

```bibtex
@misc{chen202301,
      title={0.1% Data Makes Segment Anything Slim}, 
      author={Zigeng Chen and Gongfan Fang and Xinyin Ma and Xinchao Wang},
      year={2023},
      eprint={2312.05284},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## Acknowledgement

<details>
<summary>
<a href="https://github.com/facebookresearch/segment-anything">SAM</a> (Segment Anything) [<b>bib</b>]
</summary>

```bibtex
@article{kirillov2023segany,
  title={Segment Anything}, 
  author={Kirillov, Alexander and Mintun, Eric and Ravi, Nikhila and Mao, Hanzi and Rolland, Chloe and Gustafson, Laura and Xiao, Tete and Whitehead, Spencer and Berg, Alexander C. and Lo, Wan-Yen and Doll{\'a}r, Piotr and Girshick, Ross},
  journal={arXiv:2304.02643},
  year={2023}
}
```
</details>



<details>
<summary>
<a href="https://github.com/VainF/Torch-Pruning">Torch Pruning</a> (DepGraph: Towards Any Structural Pruning) [<b>bib</b>]
</summary>

```bibtex
@inproceedings{fang2023depgraph,
  title={Depgraph: Towards any structural pruning},
  author={Fang, Gongfan and Ma, Xinyin and Song, Mingli and Mi, Michael Bi and Wang, Xinchao},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={16091--16101},
  year={2023}
}
```
</details>