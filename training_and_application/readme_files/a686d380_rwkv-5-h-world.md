---
license: apache-2.0
language:
- zh
pipeline_tag: text-generation
tags:
  - not-for-all-audiences
---
 


这是一个中文色情小说续写模型，训练自h-corpus-2023。没有对话数据，不建议用于对话。


## 模型的使用教程

本模型训练自国产开源模型RWKV，所以接入了RWKV生态，建议配合RWKV Runner使用

RWKV Runner地址: https://github.com/josStorer/RWKV-Runner

首先在进入RWKV Runner的release界面 https://github.com/josStorer/RWKV-Runner/releases

点击最新的 RWKV-Runner_windows_x64.exe 下载

将 RWKV-Runner_windows_x64.exe 放置在一个空文件夹下然后运行

接着打开模型链接: https://huggingface.co/a686d380/rwkv-5-h-world

或者国内镜像: https://hf-mirror.com/a686d380/rwkv-5-h-world

点击 Files and versions, 再点击rwkv-5-h-world-1b5.pth 右侧的下载按钮下载模型

将下载好的rwkv-5-h-world-1b5.pth 放在 RWKV-Runner_windows_x64.exe 目录下的models文件夹内

进入RWKV Runner的配置界面，在模型参数中选择模型为 rwkv-5-h-world-1b5.pth

接着根据你的显卡

### 如果你是Nvidia显卡

Strategy 选择CUDA，精度选择fp16，载入显存层数拉满，开启自定义CUDA算子

### 如果是AMD显卡

Strategy 选择WebGPU，精度选为fp16

### 如果你只有集显，使用CPU

Strategy 选择CPU，精度选为fp16


接着点击运行（A卡先点击转为Safetensors格式再点击运行）

Runner会先提醒你下载python，安装完成后再次点击，会提醒安装依赖，下载并等待安装完成

进入续写界面，开始使用

由于没有对话数据，聊天功能不正常，不建议使用

如果你不知道该从何下手，可以尝试把喜欢的小说段落放在续写界面尝试，AI模型目前仍然不擅长超长的有逻辑的叙事，因此建议使用此模型用来描写短篇段落

## 配置进阶

在精度上，int8会比fp16占用显存/内存更小，但是通常更慢。如果你的显卡过于陈旧以至于不支持fp16，请选择fp32。载入显存层数会调配显存和内存的占用，通常尽可能调大此参数使得显存占满。

如果出现问题可以尝试关闭自定义CUDA算子

如果你是intel显卡，也可以尝试WebGPU

有关显存占用的估计: 1b5中的b指代的是billion，十亿。所以1b5也就是十五亿。Billion是目前大语言模型常见的单位，1B=10^9,而常见的KB MB GB分别指代10^3,10^6,10^9字节(注意此时的B指代byte)。因此，当1.5B参数的模型以int8(8比特,1字节)存储时，会占用1.5GB存储，以fp16存储时，会占用3GB。

## 文本生成进阶

在续写界面右侧有Temperature Top_P Presence Penalty Frequency Penalty四个重要参数，这些参数非常影响模型的生成，你可以把鼠标放在上面查看说明

简言之，如果你觉得模型天马行空胡编乱造，请调低Temperature和Top_P，如果模型过于保守，请提高Temperature和Top_P

如果你发现模型在重复相同的句子或词语，请提高Presence Penalty和Frequency Penalty


## 训练

RWKV Runner暂不支持对RWKV5的训练，请等待更新。但在另一方面，随着模型大小不断增大，训练对显卡的要求越来越高，而且小规模训练也越来越难改变模型，因此训练对个人来说可能会越来越困难。

因此若要想改变文风，可以尝试将想要模仿的文本放在续写文章的前面作为铺垫。

## 更大的模型

3B模型已经上传，效果更佳，但也更吃显存和配置。建议首先测试通过1b5后再尝试3B。3B fp16占用约6G，int8占用约3G

[2024.02.28] 更大的7B模型训练完成，7B fp16占用显存15G,int8占用约7.5G

## 在线测试

Google Colab在线测试，但还是建议本地运行

### 3B gpu推理 速度快
https://colab.research.google.com/drive/1KAn6TNcoGayBceEo1uMuTJpdU7RPFenZ?usp=sharing

### 7B cpu推理 速度慢
https://colab.research.google.com/drive/1KKTesMvL1frynfW-NaTkwUDlyeons3-K?usp=sharing

## 交流讨论

https://discord.gg/V5m42EqZE5