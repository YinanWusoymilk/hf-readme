---
license: cc-by-sa-3.0
tags:
- art
---
<div align="center"><font size="8"><b>starlake</b><font></div>
<div align="center"><font size="5"><b>这是一个试图同时兼顾风景和人物的模型</b><font></div>

<font size="5">在无人物描述时，不会出现通常模型倾向于添加人物的情况
![xyz_grid-0002-4154837933.png](https://s3.amazonaws.com/moonup/production/uploads/1678859211392-640cae30536d9fe0f002ee62.png)

<font color="red">PS:负面可以直接使用emb：easynegative或者verybadimagenegative_v1.3,这两个都是影响强烈的emb模型，可以降权使用，比如(verybadimagenegative_v1.3:0.8),否则会给模型带来一定的过拟合光影，当不需要过度光影的情况下，这是个好方法。</font>
![xyz_grid-0033-1174306601.png](https://cdn-uploads.huggingface.co/production/uploads/640cae30536d9fe0f002ee62/MMccIAkPYzm7njo4TMw4p.png)
![xyz_grid-0035-84983774.png](https://cdn-uploads.huggingface.co/production/uploads/640cae30536d9fe0f002ee62/gi2RG1n9GL63zDBlwQUd0.png)

___________________________
已完成5.0版本，5.0软化了过拟合因素，不加入详细的提示词不会自主添加元素，同时也增强了读tag能力。

本次训练全程添加金字塔噪声，5.0可以直接出明暗强烈的图。

新的例图展示如下：

人物
![00010-1710471201.png](https://cdn-uploads.huggingface.co/production/uploads/640cae30536d9fe0f002ee62/770CynRxico7AEXpRsMWl.png)
![00747-285416818.png](https://cdn-uploads.huggingface.co/production/uploads/640cae30536d9fe0f002ee62/2yXSzdWgGJhTkf-Y-UfG2.png)
![00069-3762213293.png](https://cdn-uploads.huggingface.co/production/uploads/640cae30536d9fe0f002ee62/Qeqm5JjuUpZ_u97Mvru_b.png)

场景
![00064-1030430370.png](https://cdn-uploads.huggingface.co/production/uploads/640cae30536d9fe0f002ee62/v8WfCsaEutiCT4OOFfJUv.png)
![00072-1703637542.png](https://cdn-uploads.huggingface.co/production/uploads/640cae30536d9fe0f002ee62/bUyxFMVEUq5jfMPkI38NL.png)
![00748-824635104.png](https://cdn-uploads.huggingface.co/production/uploads/640cae30536d9fe0f002ee62/DYBsyLy1g0AHrRFwvnGlc.png)
___________________________
3.5版本已上传。

![00126-2780910881.png](https://s3.amazonaws.com/moonup/production/uploads/640cae30536d9fe0f002ee62/TIbqPtSkH-bF_Eh53wYBY.png)
![00026-3840530172.png](https://s3.amazonaws.com/moonup/production/uploads/640cae30536d9fe0f002ee62/R3HhLHFoKStUb4M9RegQp.png)
![00048-1899924086.png](https://s3.amazonaws.com/moonup/production/uploads/640cae30536d9fe0f002ee62/g-7lIfJ3-D0Ly9SxrmhGt.png)
![00091-1273521536.png](https://s3.amazonaws.com/moonup/production/uploads/640cae30536d9fe0f002ee62/mxaR4pMPruWCUmZVi6TE5.png)
![00088-2351873475.png](https://s3.amazonaws.com/moonup/production/uploads/640cae30536d9fe0f002ee62/2OpHleA3vDFS80i6VEAq7.png)


以下为2.0旧测试
___________________________

远景测试：
![00255-3579052070.png](https://s3.amazonaws.com/moonup/production/uploads/1678716145346-640cae30536d9fe0f002ee62.png)
![grid-0005.png](https://s3.amazonaws.com/moonup/production/uploads/1678716104574-640cae30536d9fe0f002ee62.png)
![00254-2280245862.png](https://s3.amazonaws.com/moonup/production/uploads/1678716181398-640cae30536d9fe0f002ee62.png)

人物测试：
![grid-0016.png](https://s3.amazonaws.com/moonup/production/uploads/1678716259214-640cae30536d9fe0f002ee62.png)
![grid-0001.png](https://s3.amazonaws.com/moonup/production/uploads/1678716224999-640cae30536d9fe0f002ee62.png)
![grid-0009.png](https://s3.amazonaws.com/moonup/production/uploads/1678716241591-640cae30536d9fe0f002ee62.png)
![grid-0011.png](https://s3.amazonaws.com/moonup/production/uploads/1678716307863-640cae30536d9fe0f002ee62.png)

其他例图：
![00299-279408421.png](https://s3.amazonaws.com/moonup/production/uploads/1678716327013-640cae30536d9fe0f002ee62.png)
![00256-3983416131.png](https://s3.amazonaws.com/moonup/production/uploads/1678716354044-640cae30536d9fe0f002ee62.png)


<font size="5"><b>starlake为未融合版本，存在较多人体结构问题，可用于融合。</b><font>

<b>starlake-2.0为通过模型融合修正后的版本，可直接使用。</b>