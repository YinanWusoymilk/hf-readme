---
license: creativeml-openrail-m
language:
- ja
- en
pipeline_tag: text-to-image
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
library_name: diffusers
---

<div class="flex justify-center">
  <div class="container p-0 w-100">
    <img class="mt-0 object-cover rounded-t-lg w-100"
         style="height: 320px;"
         src="https://huggingface.co/natsusakiyomi/HimawariMixs/resolve/main/image/header.jpeg"
         width="100%"/>
    <div class="flex px-4">
      <div class="flex-auto">
        <h1 class="mb-2 text-3xl font-bold leading-tight" style="color: rgb(255, 151, 0/var(--tw-text-opacity));">
          HimawariMixSeries
        </h1>
        <p class="mb-4 text-base text-neutral-600 dark:text-neutral-200">
          様々なモデルをマージした背景や細部の表現力が強いVAE内蔵型モデル<br>
          VAEの内臓はないぞ！と言わせないぞ！！！！<br>
          Models with built-in VAE with strong expression of backgrounds and details merging various models
        </p>
      </div>
      <div>
        <a
          href="https://twitter.com/min__san"
          class="mb-2 inline-block rounded px-6 py-2.5 text-white shadow-md"
          style="background-color: #1da1f2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="currentColor" viewBox="0 0 24 24">
            <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z" />
          </svg>
        </a>
      </div>
    </div>
  </div>
</div>
          

---

  <h4>📄 ライセンス / License</h4>
  <div class="px-2">
    <table class="table-fixed border mt-0 text-xs">
      <tbody>
        <tr>
          <td class="px-4 text-base" colspan="2">
            <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license">
              修正 CreativeML OpenRAIL-M ライセンス / Modified CreativeML OpenRAIL-M license
            </a>
          </td>
        </tr>
        <tr>
          <td class="align-middle px-2 w-8">
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
              </svg>
            </span>
          </td>
          <td>
            このモデルのクレジットを入れずに使用する<br>
            Use the model without crediting the creator
          </td>
        </tr>
        <tr>
          <td class="align-middle px-2 w-8">
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
              </svg>
            </span>
          </td>
          <td>
            このモデルで生成した画像を商用利用する<br>
            Sell images they generate
          </td>
        </tr>
        <tr class="bg-danger-100">
          <td class="align-middle px-2 w-8">
            <span class="text-red-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </span>
          </td>
          <td>
            このモデルを商用の画像生成サービスで利用する</br>
            Run on services that generate images for money
          </td>
        </tr>
        <tr>
          <td class="align-middle px-2 w-8">
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
              </svg>
            </span>
          </td>
          <td>
            このモデルを使用したマージモデルを共有する<br>
            Share merges using this model
          </td>
        </tr>
        <tr class="bg-danger-100">
          <td class="align-middle px-2 w-8">
            <span class="text-red-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </span>
          </td>
          <td>
            このモデル、またはこのモデルをマージしたモデルを販売する</br>
            Sell this model or merges using this model
          </td>
        </tr>
        <tr class="bg-danger-100">
          <td class="align-middle px-2 w-8">
            <span class="text-red-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </span>
          </td>
          <td>
            このモデルをマージしたモデルに異なる権限を設定する</br>
            Have different permissions when sharing merges
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v7" class="mt-0 text-2xl">
  <code>HimawariMix-v4</code> <small></small>
</h3>

<div>
  HimawariMix-v3の改造モデル<br>
  v3と比べ手や服装や構図など増えた気がする<br>
  Aの方が繊細に描け　Bの方シンプルに描くことが多くが比較的扱いやすいような気がする
  
<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v7" class="mt-0 text-2xl">
  <code>HimawariMix-v3</code> <small></small>
</h3>

<div>
  背景強化をメインに改修したモデルでリアル系のモデルの比率が多くなったモデル<br>
  リアル系を多く含んでいるため手の破綻は他と比べて比較的出ずらい.....気がする<br>
  B型のほうが比較的扱いやすい気がします

  
 <hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v7" class="mt-0 text-2xl">
  <code>HimawariMix-v2</code> <small></small>
</h3>

<div>
  背景よりキャラを重視して作られたモデル<br>
  v1.20v1.10やv1とは違いいろいろな場面でも使えるようになりました<br>
  このHimawariMixの特徴である彩度の高さが出始めた<br>
  悪く言えば器用貧乏


 <hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v7" class="mt-0 text-2xl">
  <code>HimawariMix-v1.20 and 1.10</code> <small></small>
</h3>

<div>
  HimawariMix-v1のマージ比率を変えたマイナーチェンジモデル<br>
  クローズアップに特化しておりそれ以外はあまりさえない<br>
  マイナーチェンジにより破綻が少なくなり安定性が増した
  v1.20とv1.10の違いはVAEの違い

   <hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">




<h3 id="blue_pencil-v7" class="mt-0 text-2xl">
  <code>HimawariMix-v1</code> <small></small>
</h3>

<div>
 初代HimawariMix<br>
  当時あまりなかった背景とキャラクターを両立させるために作ったモデル<br>
  特徴は背景が割と強いモデルなお今となっては普通でHimawariMixの特徴である彩度の高さはこの時点ではまだない
  

---

# 作者&連絡先
Twiter: [@min__san](https://twitter.com/min__san)