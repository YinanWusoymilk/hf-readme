---
license: other
language:
- ja
- en
tags:
- stable-diffusion
- text-to-image
---

<div class="flex justify-center">
  <div class="container p-0 w-100">
    <img class="mt-0 object-cover rounded-t-lg w-100"
         style="height: 320px;"
         src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/header.jpg"
         width="100%"/>
    <div class="flex px-4">
      <div class="flex-auto">
        <h1 class="mb-2 text-3xl font-bold leading-tight" style="color: rgb(56 189 248/var(--tw-text-opacity));">
          blue_pencil
          <a href="https://huggingface.co/bluepen5805/blue_pencil/blob/main/README.md" class="ml-2 inline-block">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
              <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" />
            </svg>
          </a>
        </h1>
        <p class="mb-4 text-base text-neutral-600 dark:text-neutral-200">
          A series of merged models that is just a messy merge of various models.
        </p>
      </div>
      <div class="flex gap-2" style="height: fit-content;">
        <a
          href="https://twitter.com/blue_pen5805"
          class="mb-2 inline-block rounded px-6 py-2.5 text-white shadow-md"
          style="background-color: #1da1f2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="currentColor" viewBox="0 0 24 24">
            <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z" />
          </svg>
        </a>
        <a
          href="https://discord.gg/s49mASQHkE"
          class="mb-2 inline-block rounded px-6 py-2.5 text-white shadow-md"
          style="background-color: #7289da">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="currentColor" viewbox="0 0 24 24">
            <path d="M19.54 0c1.356 0 2.46 1.104 2.46 2.472v21.528l-2.58-2.28-1.452-1.344-1.536-1.428.636 2.22h-13.608c-1.356 0-2.46-1.104-2.46-2.472v-16.224c0-1.368 1.104-2.472 2.46-2.472h16.08zm-4.632 15.672c2.652-.084 3.672-1.824 3.672-1.824 0-3.864-1.728-6.996-1.728-6.996-1.728-1.296-3.372-1.26-3.372-1.26l-.168.192c2.04.624 2.988 1.524 2.988 1.524-1.248-.684-2.472-1.02-3.612-1.152-.864-.096-1.692-.072-2.424.024l-.204.024c-.42.036-1.44.192-2.724.756-.444.204-.708.348-.708.348s.996-.948 3.156-1.572l-.12-.144s-1.644-.036-3.372 1.26c0 0-1.728 3.132-1.728 6.996 0 0 1.008 1.74 3.66 1.824 0 0 .444-.54.804-.996-1.524-.456-2.1-1.416-2.1-1.416l.336.204.048.036.047.027.014.006.047.027c.3.168.6.3.876.408.492.192 1.08.384 1.764.516.9.168 1.956.228 3.108.012.564-.096 1.14-.264 1.74-.516.42-.156.888-.384 1.38-.708 0 0-.6.984-2.172 1.428.36.456.792.972.792.972zm-5.58-5.604c-.684 0-1.224.6-1.224 1.332 0 .732.552 1.332 1.224 1.332.684 0 1.224-.6 1.224-1.332.012-.732-.54-1.332-1.224-1.332zm4.38 0c-.684 0-1.224.6-1.224 1.332 0 .732.552 1.332 1.224 1.332.684 0 1.224-.6 1.224-1.332 0-.732-.54-1.332-1.224-1.332z" />
          </svg>
        </a>
        <a
          href="https://github.com/blue-pen5805"
          class="mb-2 inline-block rounded px-6 py-2.5 text-white shadow-md"
          style="background-color: #333">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
          </svg>
        </a>
      </div>
    </div>
  </div>
</div>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<div class="px-2">
  <table class="table-auto">
    <tbody>
      <tr>
        <td colspan="2">
          <a href="#blue_pencil-EX">blue_pencil-EX (@20230726)</a>
        </td>
      </tr>
      <tr>
        <td colspan="2">
          <a href="#blue_pencil-v10">blue_pencil-v10 (@20230627v2)</a>
        </td>
      </tr>
      <tr>
        <td><a href="#blue_pencil-v9b">blue_pencil-v9b (@20230602)</a></td>
        <td><a href="#blue_pencil-v9">blue_pencil-v9 (@20230526v4)</a></td>
      </tr>
      <tr>
        <td colspan="2">
          <a href="#blue_pencil-v8">blue_pencil-v8 (@20230507)</a>
        </td>
      </tr>
      <tr>
        <td colspan="2">
          <a href="#blue_pencil-v7">blue_pencil-v7 (@20230414)</a>
        </td>
      </tr>
      <tr>
        <td colspan="2">
          <a href="#blue_pencil-v6">blue_pencil-v6 (@20230327)</a>
        </td>
      </tr>
      <tr>
        <td><a href="#blue_pencil-v5">blue_pencil-v5b (@20230314)</a></td>
        <td><a href="#blue_pencil-v5">blue_pencil-v5 (@20230310)</a></td>
      </tr>
      <tr>
        <td colspan="2">
          <a href="#blue_pencil-v4">blue_pencil-v4 (@20230227)</a>
        </td>
      </tr>
      <tr>
        <td colspan="2">
          <a href="#blue_pencil-v3">blue_pencil-v3 (@20230223)</a>
        </td>
      </tr>
      <tr>
        <td><a href="#blue_pencil-v2">blue_pencil-v2b (@20230219)</a></td>
        <td><a href="#blue_pencil-v2">blue_pencil-v2 (@20230217)</a></td>
      </tr>
      <tr>
        <td><a href="#blue_pencil-v1">blue_pencil-v1b (@20230212)</a></td>
        <td><a href="#blue_pencil-v1">blue_pencil-v1 (@20230211)</a></td>
      </tr>
    </tbody>
  </table>
</div>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-EX" class="mt-0 text-2xl">
  <code>blue_pencil-EX</code> <small>(<code>@20230726</code>)</small>
</h3>
  
  <div>
    おまけです。かなり扱いにくいとおもいます。v10かv8を使ってください。
  </div>
    
  <h4>📄 ライセンス / License</h4>
  <div class="px-2">
    <table class="table-fixed border mt-0 text-xs">
      <tbody>
        <tr>
          <td class="px-4 text-base" colspan="2">
            <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license">
              CreativeML OpenRAIL-M ライセンス / CreativeML OpenRAIL-M license
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
</h3>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v10" class="mt-0 text-2xl">
  <code>blue_pencil-v10</code> <small>(<code>@20230627v2</code>)</small>
</h3>
  
  <div>
    かわいいね。<br/>
    ネガティブプロンプトは `(worst quality, bad quality:2.0)` だけで大丈夫です（EasyNegative とかを使ってもいいけどね）
  </div>
    
  <h4>📄 ライセンス / License</h4>
  <div class="px-2">
    <table class="table-fixed border mt-0 text-xs">
      <tbody>
        <tr>
          <td class="px-4 text-base" colspan="2">
            <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license">
              CreativeML OpenRAIL-M ライセンス / CreativeML OpenRAIL-M license
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
</h3>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v9b" class="mt-0 text-2xl">
  <code>blue_pencil-v9b</code> <small>(<code>@20230602</code>)</small>
</h3>

<div>
  <div>
    v9 をベースに目の輝きを増やし、ついでに気分で調整を施したモデルです。<br/>
    短いプロンプトでも安定した出力が得られるような気がしています（女の子以外も）<br/>
    ネガティブプロンプトは `(worst quality, bad quality:2.0)` だけでいい気がしています。
  </div>
    
  <h4>📄 ライセンス / License</h4>
  <div class="px-2">
    <table class="table-fixed border mt-0 text-xs">
      <tbody>
        <tr>
          <td class="px-4 text-base" colspan="2">
            <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license">
              CreativeML OpenRAIL-M ライセンス / CreativeML OpenRAIL-M license
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
  
  <h4>🌱 レシピ / Recipe</h4>
  <div class="px-2">
    <div class="border p-2">
      <details>
        <table>
          <thead>
            <tr>
              <th>A</th>
              <th>B</th>
              <th>C</th>
              <th>Method</th>
              <th>Weight</th>
              <th>OUTPUT</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>@20230526-9</td>
              <td colspan="4">LoRAs(
                <a href="https://civitai.com/models/81346">hohoaka</a>:-1.25,
                <a href="https://civitai.com/models/81345">agomaru</a>:1.5,
                <a href="https://civitai.com/models/81321">faceage</a>:0.5,
                <a href="https://civitai.com/models/69207">colored-eyelashes</a>:0.3,
                <a href="https://civitai.com/models/81928">fantasy world lora</a>:0.05,
                <a href="https://civitai.com/models/58764">FuturisticScapes-v2</a>:0.35,
                <a href="https://huggingface.co/ashen-sensored/mzpikas_tmnd_enhanced">Silicon-landscape-isolation</a>:0.35,
                <a href="https://civitai.com/models/81378">sanDka1</a>:-0.5,
                <a href="https://huggingface.co/ashen-sensored/lora-isolation-collection">pikas-lighting-isolation</a>:0.3,
                <a href="https://civitai.com/models/81360">saturation</a>:0.15
                )
              </td>
              <td>@20230602-LoRA</td>
            </tr>
            <tr>
              <td>@20230602-LoRA</td>
              <td><a href="https://civitai.com/models/77751">NextGenMix</a></td>
              <td></td>
              <td>MBW</td>
              <td>
                1,1,0,0,0,0,0,0,1,1,0,0,<br/>
                0,<br/>
                1,1,0,0,0,0,0,0,0,0,1,1<br/>
                Base alpha 1</td>
              <td>blue_pencil-v9b</td>
            </tr>
          </tbody>
        </table>
      </details>
    </div>
  </div>

  <h4>🔧 推奨設定 / Recommended Settings</h4>
  <div class="px-2">
    <table class="table-auto border mt-0 text-sm">
      <tbody>
        <tr>
          <td class="pl-2" style="width: 12rem;">
            VAE
          </td>
          <td>
            <a href="https://civitai.com/models/22354/clearvae">ClearVAE</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4>🖼️ 例 / Examples</h4>
  <div class="container mx-auto px-2">
    <div class="flex flex-wrap min-w-min items-baseline">
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px; flex-basis: 50%;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v9b/1.webp"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            cute girl and cat. cute clothes, skirt, squatting, torrential rain, umbrella
            Negative prompt: (worst quality, bad quality:2.0)
            Steps: 29
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 1858548488
            Size: 768x768
            Denoising strength: 0.5
            Hires upscale: 2
            Hires steps: 20
            Hires upscaler: SwinIR_4x
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px; flex-basis: 50%;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v9b/2.webp"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            ancient dragon, darkness
            Negative prompt: (worst quality, bad quality:2.0)
            Steps: 22
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 4099565158
            Size: 768x768
            Denoising strength: 0.5
            Hires upscale: 2
            Hires steps: 15
            Hires upscaler: SwinIR_4x
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px; flex-basis: 50%;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v9b/3.webp"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girl, cute clothes, city, cyberpunk
            Negative prompt: (worst quality, bad quality:2.0)
            Steps: 40
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 3260935736
            Size: 768x768
            Denoising strength: 0.6
            Hires upscale: 2
            Hires upscaler: Latent (nearest-exact)
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px; flex-basis: 50%;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v9b/4.webp"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            smiling old man, cigar, sunglasses, holding teddybear, (darkness:1.3)
            Negative prompt: (worst quality, bad quality:2.0)
            Steps: 20
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 1270347467
            Size: 768x768
            Denoising strength: 0.55
            Hires upscale: 2
            Hires upscaler: Latent (nearest-exact)
          </pre>
        </div>
      </div>
    </div>
  </div>
</div>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v9" class="mt-0 text-2xl">
  <code>blue_pencil-v9</code> <small>(<code>@20230526v4</code>)</small>
</h3>

<div>
  <div class="font-bold">
    ※このモデルは実験的なモデルです。安定したモデルを使いたい場合は v8 か v7 をご利用ください。
  </div>
    
  <h4>📄 ライセンス / License</h4>
  <div class="px-2">
    <table class="table-fixed border mt-0 text-xs">
      <tbody>
        <tr>
          <td class="px-4 text-base" colspan="2">
            <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license">
              CreativeML OpenRAIL-M ライセンス / CreativeML OpenRAIL-M license
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
  
  <h4>🌱 レシピ / Recipe</h4>
  <div class="px-2">
    <div class="border p-2">
      <details>
        <table>
          <thead>
            <tr>
              <th>A</th>
              <th>B</th>
              <th>C</th>
              <th>Method</th>
              <th>Weight</th>
              <th>OUTPUT</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><a href="https://huggingface.co/Korakoe/OpenNiji-V2">OpenNiji-V2</a></td>
              <td><a href="https://huggingface.co/prompthero/openjourney-v4">openjourney-v4</a></td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference(smoothAdd)</td>
              <td>1</td>
              <td>@MidNijiV4V2</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/NoCrypt/SomethingV2">somethingv2_1</a></td>
              <td><a href="https://civitai.com/models/29819">neatnessFluffyFurMix_nebula</a></td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference(smoothAdd)</td>
              <td>0.25</td>
              <td>@20230526-0</td>
            </tr>
            <tr>
              <td>@20230526-0</td>
              <td><a href="https://huggingface.co/Vsukiyaki/ShiratakiMix">ShiratakiMix-fixed</a></td>
              <td></td>
              <td>Weighted sum(cosineA)</td>
              <td>0.35</td>
              <td>@20230526-1</td>
            </tr>
            <tr>
              <td><a href="https://civitai.com/models/67145">defacta5rd_5rd</a></td>
              <td>@MidNijiV4V2</td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference(smoothAdd)</td>
              <td>0.25</td>
              <td>@20230526-2</td>
            </tr>
            <tr>
              <td>@20230526-2</td>
              <td><a href="https://civitai.com/models/67120">yuzu_v10</a></td>
              <td></td>
              <td>Weighted sum(cosineA)</td>
              <td>0.45</td>
              <td>@20230526-3</td>
            </tr>
            <tr>
              <td>@20230526-1</td>
              <td>@20230526-3</td>
              <td></td>
              <td>Weighted sum(cosineA)</td>
              <td>0.35</td>
              <td>@20230526-4</td>
            </tr>
            <tr>
              <td><a href="https://civitai.com/models/10028">neverendingDreamNED_v122BakedVae</a></td>
              <td><a href="https://huggingface.co/ashen-sensored/mzpikas_tmnd_enhanced">mzpikas_tmnd_enhanced-fp16</a></td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference(smoothAdd)</td>
              <td>0.25</td>
              <td>@20230526-5</td>
            </tr>
            <tr>
              <td>@20230526-4</td>
              <td>@20230526-5</td>
              <td></td>
              <td>Weighted sum(cosineA)</td>
              <td>0.25</td>
              <td>@20230526-6</td>
            </tr>
            <tr>
              <td>@20230526-6</td>
              <td><a href="https://civitai.com/models/47067">pikasNewGeneration_v20</a></td>
              <td></td>
              <td>Weighted sum(cosineA)</td>
              <td>0.25</td>
              <td>@20230526-7</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/SweetLuna/Aurora">AuroraONE</a></td>
              <td><a href="https://huggingface.co/gsdf/Counterfeit-V3.0">Counterfeit-V3.0_fp32</a></td>
              <td></td>
              <td>Weighted sum(cosineA)</td>
              <td>0.45</td>
              <td>@20230526-8</td>
            </tr>
            <tr>
              <td>@20230526-7</td>
              <td>@20230526-8</td>
              <td></td>
              <td>Weighted sum(cosineA)</td>
              <td>0.5</td>
              <td>@20230526-9</td>
            </tr>
            <tr>
              <td>@20230526-9</td>
              <td colspan="4">LoRAs(
                <a href="https://civitai.com/models/81346">hohoaka</a>:-1.25,
                <a href="https://civitai.com/models/81345">agomaru</a>:0.5,
                <a href="https://civitai.com/models/81321">faceage</a>:0.5,
                <a href="https://civitai.com/models/58764">FuturisticScapes-v2</a>:0.35,
                <a href="https://huggingface.co/ashen-sensored/mzpikas_tmnd_enhanced">Silicon-landscape-isolation</a>:0.3,
                <a href="https://civitai.com/models/81378">sanDka1</a>:-0.5)
              </td>
              <td>@20230526-LoRA</td>
            </tr>
            <tr>
              <td>@20230526-LoRA</td>
              <td><a href="https://huggingface.co/ploughB660/BalorMix-V4">BalorMix-V4.3</a></td>
              <td></td>
              <td>MBW</td>
              <td>
                1,1,0,0,0,0,0,0,1,1,0,0,<br/>
                0,<br/>
                1,1,0,0,0,0,0,0,0,0,1,1<br/>
                Base alpha 1</td>
              <td>blue_pencil-v9</td>
            </tr>
          </tbody>
        </table>
      </details>
    </div>
  </div>

  <h4>🔧 推奨設定 / Recommended Settings</h4>
  <div class="px-2">
    <table class="table-auto border mt-0 text-sm">
      <tbody>
        <tr>
          <td class="pl-2" style="width: 12rem;">
            VAE
          </td>
          <td>
            <a href="https://civitai.com/models/22354/clearvae">ClearVAE</a>
          </td>
        </tr>
        <tr>
          <td class="pl-2">
            Negative Embedding
          </td>
          <td>
            <a href="https://huggingface.co/gsdf/Counterfeit-V3.0">EasyNegativeV2</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4>🖼️ 例 / Examples</h4>
  <div class="container mx-auto px-2">
    <div class="flex flex-wrap min-w-min items-baseline">
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px; flex-basis: 50%;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v9/1.webp"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            colorful girl, cute pose, cute clothes, cute room
            Negative prompt: EasyNegativeV2
            Steps: 30
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 3455183564
            Size: 768x768
            Denoising strength: 0.6
            Hires upscale: 2
            Hires steps: 30
            Hires upscaler: SwinIR_4x
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px; flex-basis: 50%;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v9/2.webp"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            old man, suit, standing, moonlight
            Negative prompt: EasyNegativeV2
            Steps: 24
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 3212346863
            Size: 768x768
            Denoising strength: 0.6
            Hires upscale: 2
            Hires upscaler: SwinIR_4x
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px; flex-basis: 50%;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v9/3.webp"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            knight, from behind, town, gradient sky, dusk, orb, scenery, fantasy, mythology
            Negative prompt: EasyNegativeV2
            Steps: 20
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 2359276410
            Size: 768x768
            Denoising strength: 0.6
            Hires upscale: 2
            Hires upscaler: SwinIR_4x
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px; flex-basis: 50%;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v9/4.webp"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            mechanical dog, roar, fighting stance, apocalyptic, thunder
            Negative prompt: EasyNegativeV2
            Steps: 20
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 694621969
            Size: 768x768
            Denoising strength: 0.5
            Hires upscale: 2
            Hires upscaler: SwinIR_4x
          </pre>
        </div>
      </div>
    </div>
  </div>
</div>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v8" class="mt-0 text-2xl">
  <code>blue_pencil-v8</code> <small>(<code>@20230507</code>)</small>
</h3>

<div>
  ただ AuroraONE と Counterfeit-V3.0 が混ぜたかっただけです<br/>
  v7の方がいい気がします。
    
  <h4>📄 ライセンス / License</h4>
  <div class="px-2">
    <table class="table-fixed border mt-0 text-xs">
      <tbody>
        <tr>
          <td class="px-4 text-base" colspan="2">
            <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license">
              CreativeML OpenRAIL-M ライセンス / CreativeML OpenRAIL-M license
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
            <span class="text-green-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
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
  
  <h4>🌱 レシピ / Recipe</h4>
  <div class="px-2">
    <div class="border p-2">
      <details>
        <table>
          <thead>
            <tr>
              <th>A</th>
              <th>B</th>
              <th>C</th>
              <th>Method</th>
              <th>Weight</th>
              <th>OUTPUT</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><a href="https://huggingface.co/Korakoe/OpenNiji-V2">OpenNiji-V2</a></td>
              <td><a href="https://huggingface.co/prompthero/openjourney-v4">openjourney-v4</a></td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference</td>
              <td>1</td>
              <td>@MidNijiV4V2</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/NoCrypt/SomethingV2">somethingv2_1</a></td>
              <td><a href="https://civitai.com/models/59813/animal-human-hybrids">animalHumanHybrids_v10</a></td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference</td>
              <td>0.25</td>
              <td>@20230507-0</td>
            </tr>
            <tr>
              <td>@20230507-0</td>
              <td><a href="https://huggingface.co/Vsukiyaki/ShiratakiMix">ShiratakiMix-fixed</a></td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.35</td>
              <td>@20230507-1</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/Hemlok/MandarinMix">MandarinMix-EX</a></td>
              <td><a href="https://huggingface.co/eimiss/EimisAnimeDiffusion_2.0v">EimisAnimeModel_2-0</a></td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference</td>
              <td>0.15</td>
              <td>@20230507-2</td>
            </tr>
            <tr>
              <td>@20230507-2</td>
              <td><a href="https://civitai.com/models/41916/koji">koji_v10</a></td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.45</td>
              <td>@20230507-3</td>
            </tr>
            <tr>
              <td>@20230507-1</td>
              <td>@20230507-3</td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.3</td>
              <td>@20230507-4</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/ashen-sensored/mzpikas_tmnd_enhanced">mzpikas_tmnd_enhanced-fp16</a></td>
              <td>@MidNijiV4V2</td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference</td>
              <td>0.2</td>
              <td>@20230507-5</td>
            </tr>
            <tr>
              <td>@20230507-4</td>
              <td>@20230507-5</td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.25</td>
              <td>@20230507-6</td>
            </tr>
            <tr>
              <td>@20230507-6</td>
              <td>EmotionalBacklightsMix_alpha-fp16</td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.25</td>
              <td>@20230507-7</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/SweetLuna/Aurora">AuroraONE</a></td>
              <td><a href="https://huggingface.co/gsdf/Counterfeit-V3.0">Counterfeit-V3.0_fp32</a></td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.45</td>
              <td>@20230507-8</td>
            </tr>
            <tr>
              <td>@20230507-7</td>
              <td>@20230507-8</td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.5</td>
              <td>@20230507-9</td>
            </tr>
            <tr>
              <td>@20230507-9</td>
              <td><a href="https://huggingface.co/ploughB660/BalorMix-V4">BalorMix-V4.3</a></td>
              <td></td>
              <td>MBW</td>
              <td>
                1,1,0,0,0,0,0,0,1,1,0,0,<br/>
                0,<br/>
                1,1,0,0,0,0,0,0,0,0,1,1<br/>
                Base alpha 1</td>
              <td>blue_pencil-v8</td>
            </tr>
          </tbody>
        </table>
      </details>
    </div>
  </div>

  <h4>🔧 推奨設定 / Recommended Settings</h4>
  <div class="px-2">
    <table class="table-auto border mt-0 text-sm">
      <tbody>
        <tr>
          <td class="pl-2" style="width: 12rem;">
            VAE
          </td>
          <td>
            <a href="https://civitai.com/models/22354/clearvae">ClearVAE</a>
          </td>
        </tr>
        <tr>
          <td class="pl-2">
            Negative Embedding
          </td>
          <td>
            <a href="https://huggingface.co/gsdf/Counterfeit-V3.0">EasyNegativeV2</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4>🖼️ 例 / Examples</h4>
  <div class="container mx-auto px-2">
    <div class="flex flex-wrap min-w-min items-baseline">
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v8/1.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            wakame, girl, scenery
            Negative prompt: EasyNegativeV2
            Steps: 20
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 1217939694
            Size: 768x768
            Denoising strength: 0.6
            SAG Guidance Scale: 0.75
            SAG Mask Threshold: 1
            Hires upscale: 2
            Hires upscaler: Latent (nearest-exact)
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v8/2.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            cats and girl, (colorful pop cute illustration:1.3), sd
            Negative prompt: EasyNegativeV2, (girl:2.0)
            Steps: 20
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 3694801134
            Size: 768x768
            Denoising strength: 0.5
            SAG Guidance Scale: 0.75
            SAG Mask Threshold: 1
            Hires upscale: 2
            Hires upscaler: SwinIR_4x
          </pre>
        </div>
      </div>
    </div>
  </div>
</div>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v7" class="mt-0 text-2xl">
  <code>blue_pencil-v7</code> <small>(<code>@20230414</code>)</small>
</h3>

<div>
  ちょっとアニメ寄りにしてみたモデルです。今までと勝手が違うかも？<br/>
  ついでになんの影響なのか分からないけど背景の破綻が減った気がします。
    
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
  
  <h4>🌱 レシピ / Recipe</h4>
  <div class="px-2">
    <div class="border p-2">
      <details>
        <table>
          <thead>
            <tr>
              <th>A</th>
              <th>B</th>
              <th>C</th>
              <th>Method</th>
              <th>Weight</th>
              <th>OUTPUT</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><a href="https://huggingface.co/Korakoe/OpenNiji-V2">OpenNiji-V2</a></td>
              <td><a href="https://huggingface.co/prompthero/openjourney-v4">openjourney-v4</a></td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference</td>
              <td>1</td>
              <td>@MidNijiV4V2</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/NoCrypt/SomethingV2">somethingv2_1</a></td>
              <td>wd-1-4-float32-booru-110k</td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference</td>
              <td>0.25</td>
              <td>@20230414-0</td>
            </tr>
            <tr>
              <td><a href="https://civitai.com/models/28828/breakdro">breakdro_A694</a></td>
              <td><a href="https://civitai.com/models/32456/milk-mousse">MilkMousse_v10</a></td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference</td>
              <td>0.25</td>
              <td>@20230414-1</td>
            </tr>
            <tr>
              <td>@20230414-0</td>
              <td><a href="https://huggingface.co/Vsukiyaki/ShiratakiMix">ShiratakiMix-fixed</a></td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.5</td>
              <td>@20230414-2</td>
            </tr>
            <tr>
              <td>@20230414-1</td>
              <td><a href="https://civitai.com/models/2583">hassakuHentaiModel_v11</a></td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.5</td>
              <td>@20230414-3</td>
            </tr>
            <tr>
              <td>@20230414-2</td>
              <td>@20230414-3</td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.45</td>
              <td>@20230414-4</td>
            </tr>
            <tr>
              <td>@MidNijiV4V2</td>
              <td><a href="https://huggingface.co/Deltaadams/HD-22">HD-22</a></td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference</td>
              <td>0.25</td>
              <td>@20230414-5</td>
            </tr>
            <tr>
              <td>@20230414-4</td>
              <td>@20230414-5</td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.2</td>
              <td>@20230414-6</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/Kuyoh/EmotionalBackLightsMix">EmotionalBacklightsMix_alpha-fp16</a></td>
              <td><a href="https://huggingface.co/NegiInNattoMaki/Nabylon">Nabylon-v1.3</a></td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.4</td>
              <td>@20230414-7</td>
            </tr>
            <tr>
              <td>@20230414-6</td>
              <td><a href="https://huggingface.co/Lucetepolis/TriPhaze">TriPhaze_B</a></td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.25</td>
              <td>@20230414-8</td>
            </tr>
            <tr>
              <td>@20230414-8</td>
              <td>@20230414-7</td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.35</td>
              <td>@20230414-9</td>
            </tr>
            <tr>
              <td>@20230414-9</td>
              <td><a href="https://huggingface.co/ploughB660/BalorMix-V4">BalorMix-V4.3</a></td>
              <td></td>
              <td>MBW</td>
              <td>
                1,1,0,0,0,0,0,0,1,1,0,0,<br/>
                0,<br/>
                1,1,0,0,0,0,0,0,0,0,1,1<br/>
                Base alpha 1</td>
              <td>blue_pencil-v7</td>
            </tr>
          </tbody>
        </table>
      </details>
    </div>
  </div>

  <h4>🔧 推奨設定 / Recommended Settings</h4>
  <div class="px-2">
    <table class="table-auto border mt-0 text-sm">
      <tbody>
        <tr>
          <td class="pl-2" style="width: 12rem;">
            VAE
          </td>
          <td>
            <a href="https://civitai.com/models/22354/clearvae">ClearVAE</a>
          </td>
        </tr>
        <tr>
          <td class="pl-2">
            Negative Embedding
          </td>
          <td>
            <a href="https://huggingface.co/datasets/gsdf/EasyNegative">EasyNegative</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4>🖼️ 例 / Examples</h4>
  <div class="container mx-auto px-2">
    <div class="flex flex-wrap min-w-min items-baseline">
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v7/1.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            anime, girl, OOTD, living room, afternoon
            Negative prompt: EasyNegative
            Steps: 30
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 58901123
            Size: 768x768
            Denoising strength: 0.5
            Hires upscale: 2,
            Hires upscaler: SwinIR_4x
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v7/2.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girl, mage, wizard, grasslands, sunset, scenery, fantasy
            Negative prompt: EasyNegative, buildings, tower, statue
            Steps: 35
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 2365232986
            Size: 768x768
            Denoising strength: 0.5
            Hires upscale: 2
            Hires steps: 20
            Hires upscaler: SwinIR_4x
          </pre>
        </div>
      </div>
    </div>
  </div>
</div>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v6" class="mt-0 text-2xl">
  <code>blue_pencil-v6</code> <small>(<code>@20230327</code>)</small>
</h3>

<div>
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
            変更箇所を明示せずにこのモデルを使用したマージモデルを共有する</br>
            <a href="https://huggingface.co/Xynon/SD-Silicon#terms-of-use">Clearly indicate where modifications have been made.</a>
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

  <h4>🌱 レシピ / Recipe</h4>
  <div class="px-2">
    <div class="border p-2">
      <details>
        <table>
          <thead>
            <tr>
              <th>A</th>
              <th>B</th>
              <th>C</th>
              <th>Method</th>
              <th>Weight</th>
              <th>OUTPUT</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><a href="https://huggingface.co/Korakoe/OpenNiji-V2">OpenNiji-V2</a></td>
              <td><a href="https://huggingface.co/prompthero/openjourney-v4">openjourney-v4</a></td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference</td>
              <td>1</td>
              <td>@MidNijiV4V2</td>
            </tr>
            <tr>
              <td>wd-1-4-float32-booru-110k</td>
              <td><a href="https://huggingface.co/haor/Evt_M">Evt_M</a></td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference</td>
              <td>0.5</td>
              <td>@20230327-0</td>
            </tr>
            <tr>
              <td>@MidNijiV4V2</td>
              <td><a href="https://huggingface.co/Deltaadams/HD-22">HD-22</a></td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference</td>
              <td>0.5</td>
              <td>@20230327-1</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/NoCrypt/SomethingV2_2">SomethingV2_2</a></td>
              <td>mechanicmixV2</td>
              <td><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">v1-5-pruned</a></td>
              <td>Add difference</td>
              <td>0.5</td>
              <td>@20230327-2</td>
            </tr>
            <tr>
              <td><a href="https://civitai.com/models/23804/defacta">defacta_6</a></td>
              <td><a href="https://huggingface.co/NegiInNattoMaki/Nabylon">Nabylon-v1.3</a></td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.5</td>
              <td>@20230327-3</td>
            </tr>
            <tr>
              <td><a href="https://civitai.com/models/2583">hassakuv1</a></td>
              <td>@20230327-0</td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.5</td>
              <td>@20230327-4</td>
            </tr>
            <tr>
              <td><a href="https://civitai.com/models/14712/orion-mix">orionMixVersion2</a></td>
              <td>@20230327-1</td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.5</td>
              <td>@20230327-5</td>
            </tr>
            <tr>
              <td>@20230327-4</td>
              <td>@20230327-5</td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.35</td>
              <td>@20230327-6</td>
            </tr>
            <tr>
              <td>@20230327-6</td>
              <td>@20230327-2</td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.15</td>
              <td>@20230327-7</td>
            </tr>
            <tr>
              <td>@20230327-7</td>
              <td><a href="https://huggingface.co/Lucetepolis/TriPhaze">TriPhaze_B</a></td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.25</td>
              <td>@20230327-8</td>
            </tr>
            <tr>
              <td>@20230327-8</td>
              <td>@20230327-3</td>
              <td></td>
              <td>Weighted sum</td>
              <td>0.2</td>
              <td>@20230327-9</td>
            </tr>
            <tr>
              <td>@20230327-9</td>
              <td><a href="https://huggingface.co/ploughB660/BalorMix-V4">BalorMix-V4.1</a></td>
              <td></td>
              <td>MBW</td>
              <td>
                1,1,0,0,0,0,0,0,1,1,0,0,<br/>
                0,<br/>
                1,1,0,0,0,0,0,0,0,0,1,1<br/>
                Base alpha 1</td>
              <td>blue_pencil-v6</td>
            </tr>
          </tbody>
        </table>
      </details>
    </div>
  </div>

  <h4>🔧 推奨設定 / Recommended Settings</h4>
  <div class="px-2">
    <table class="table-auto border mt-0 text-sm">
      <tbody>
        <tr>
          <td class="pl-2" style="width: 12rem;">
            VAE
          </td>
          <td>
            <a href="https://civitai.com/models/22354/clearvae">ClearVAE</a>
          </td>
        </tr>
        <tr>
          <td class="pl-2">
            Negative Embedding
          </td>
          <td>
            <a href="https://huggingface.co/datasets/gsdf/EasyNegative">EasyNegative</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4>🖼️ 例 / Examples</h4>
  <div class="container mx-auto px-2">
    <div class="flex flex-wrap min-w-min items-baseline">
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v6/1.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girls, school, sunset, countryside, (silhouette:1.3)
            Negative prompt: EasyNegative
            Steps: 40
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 9717043
            Size: 768x768
            Denoising strength: 0.7
            Hires upscale: 2,
            Hires steps: 20
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v6/2.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            boy and girl, summer clothes, lakeside, landscape
            Negative prompt: EasyNegative
            Steps: 40
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 676740370
            Size: 768x768
            Denoising strength: 0.65
            Hires upscale: 2
            Hires steps: 25
          </pre>
        </div>
      </div>
    </div>
  </div>
</div>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v5" class="mt-0 text-2xl">
  <code>blue_pencil-v5b</code> <small>(<code>@20230314</code>)</small> / <code>blue_pencil-v5</code> <small>(<code>@20230310</code>)</small>
</h3>

<div>
  openjourney-v2 と OpenNiji-V2 を多めに配合して表現力が高まってくれるといいなと願いながら作ったモデルです。<br />
  実際効果があるかはわかりません。<br />
  blue_pencil-v5b は<a href="https://huggingface.co/ploughB660/Balor-V3">Balor-V2.5</a>の代わりに<a href="https://huggingface.co/ploughB660/BalorMix-V4">BalorMix-V4.1</a>を階層マージしたモデルです。

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

  <h4>🌱 マージ元モデル / Merged models</h4>
  <div class="px-2">
    <div class="border p-2">
      <details>

* [wd-1-4-float32-booru-110k](https://huggingface.co/hakurei/waifu-diffusion-v1-4) / CreativeML OpenRAIL M 
* [Evt_M](https://huggingface.co/haor/Evt_M) / CreativeML OpenRAIL M
  * [Evt_V4](https://huggingface.co/haor/Evt_V4-preview) / CreativeML OpenRAIL M
    * [ACertainty](https://huggingface.co/JosephusCheung/ACertainty) / CreativeML OpenRAIL M
* [HD-22](https://huggingface.co/Deltaadams/HD-22) / BigScience OpenRAIL M
* [openjourney-v2](https://huggingface.co/prompthero/openjourney-v2) / CreativeML OpenRAIL M
* [OpenNiji-V2](https://huggingface.co/Korakoe/OpenNiji-V2) / CreativeML OpenRAIL M
* [SomethingV2_1](https://huggingface.co/NoCrypt/SomethingV2) / CreativeML OpenRAIL M
* [mechanicmix_V2](https://civitai.com/models/14880/mechanicmixv2) / CreativeML OpenRAIL M
* [HighRiseMixV2](https://huggingface.co/0RisingStar0/HighRiseMixV2) / CreativeML OpenRAIL M
  * [AbyssOrangeMix2_NSFW](https://huggingface.co/WarriorMama777/OrangeMixs) / CreativeML OpenRAIL M
    * [AnythingV3.0](https://huggingface.co/Linaqruf/anything-v3.0) / CreativeML OpenRAIL M
    * [basil_mix](https://huggingface.co/nuigurumi/basil_mix) / OpenRAIL M
    * NovelAI / ???
    * Gape60 / ???
  * [AnythingV4.5](https://huggingface.co/andite/anything-v4.0) / CreativeML OpenRAIL M
  * [AikimiXPv1.0](https://huggingface.co/Aikimi/AikimiX) / unknown
  * [AikimixCv1.5](https://huggingface.co/Aikimi/AikimiX) / unknown
  * [basil_mix_fixed](https://huggingface.co/nuigurumi/basil_mix) / OpenRAIL M
  * [Counterfeit-V2.0](https://huggingface.co/gsdf/Counterfeit-V2.0) / CreativeML OpenRAIL M
  * [Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5) / CreativeML OpenRAIL M
  * [EerieOrangeMix2](https://huggingface.co/WarriorMama777/OrangeMixs) / CreativeML OpenRAIL M
    * [Instagram](https://huggingface.co/cafeai/cafe-instagram-sd-1-5-v6) / AGPL-3.0
    * F222 / ???
    * [Elysium_V1](https://huggingface.co/hesw23168/SD-Elysium-Model) / OpenRAIL M
    * NovelAI / ???
    * Gape60 / ???
  * [pastelmix-better-vae](https://huggingface.co/andite/pastel-mix) / Modified CreativeML OpenRAIL M
  * [powercolor.v2](https://civitai.com/models/6167/powercolorv2) / CreativeML OpenRAIL M
* [Nabylon-v1.3](https://huggingface.co/NegiInNattoMaki/Nabylon) / CreativeML OpenRAIL M
  * [AbyssOrangeMix2](https://huggingface.co/WarriorMama777/OrangeMixs) / CreativeML OpenRAIL M
  * [LonganMix](https://huggingface.co/Hemlok/LonganMix) / other
    * [7th_Layer](https://huggingface.co/syaimu/7th_Layer) / ???
  * and others
* [grapefruitv4](https://civitai.com/models/2583) / Modified CreativeML OpenRAIL M
  * [AnythingV3.0](https://huggingface.co/Linaqruf/anything-v3.0) / CreativeML OpenRAIL M
  * [Elysium_V2](https://huggingface.co/hesw23168/SD-Elysium-Model) / OpenRAIL M
  * [AbyssOrangeMix](https://huggingface.co/WarriorMama777/OrangeMixs) / CreativeML OpenRAIL M
    * [Instagram](https://huggingface.co/cafeai/cafe-instagram-sd-1-5-v6) / AGPL-3.0
    * F222 / ???
    * [AnythingV3.0](https://huggingface.co/Linaqruf/anything-v3.0) / CreativeML OpenRAIL M
    * NovelAI / ???
    * Gape60 / ???
  * [AbyssOrangeMix2](https://huggingface.co/WarriorMama777/OrangeMixs) / CreativeML OpenRAIL M
  * [basil_mix](https://huggingface.co/nuigurumi/basil_mix) / OpenRAIL M
  * and LoRAs
  * ❌ Run on services that generate images for money
  * ❌ Sell this model or merges using this model
* [Orion-Mix](https://civitai.com/models/14712/orion-mix) / CreativeML OpenRAIL M
  * [Cetus-Mix](https://civitai.com/models/6755/cetus-mix) / CreativeML OpenRAIL M
    * [AbyssOrangeMix2](https://huggingface.co/WarriorMama777/OrangeMixs) / CreativeML OpenRAIL M
    * [pastel-mix](https://huggingface.co/andite/pastel-mix) / Modified CreativeML OpenRAIL M
  * [Andromeda-Mix](https://civitai.com/models/6408/andromeda-mix) / CreativeML OpenRAIL M
    * [AbyssOrangeMix2](https://huggingface.co/WarriorMama777/OrangeMixs) / CreativeML OpenRAIL M
    * [pastel-mix](https://huggingface.co/andite/pastel-mix) / Modified CreativeML OpenRAIL M
* [TriPhase_B](https://huggingface.co/Lucetepolis/TriPhaze) / CreativeML OpenRAIL M
  * [ultracolor.v4](https://civitai.com/models/5777/ultracolorv4) / CreativeML OpenRAIL M
  * [Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5) / CreativeML OpenRAIL M
  * [Treebark](https://huggingface.co/HIZ/aichan_pick) / ???
    * [AnythingV3.0](https://huggingface.co/Linaqruf/anything-v3.0) / CreativeML OpenRAIL M
    * NovelAI / ???
    * Gape60 / ???
    * [basil_mix](https://huggingface.co/nuigurumi/basil_mix) / OpenRAIL M
    * [SXD](https://civitai.com/models/1169/sxd) / CreativeML OpenRAIL M
* [Balor-V2.5](https://huggingface.co/ploughB660/Balor-V3) / CreativeML OpenRAIL M
  * [Elysium_V2](https://huggingface.co/hesw23168/SD-Elysium-Model) / OpenRAIL M
  * [ultracolor.v4](https://civitai.com/models/5777/ultracolorv4) / CreativeML OpenRAIL M
  * [basil_mix](https://huggingface.co/nuigurumi/basil_mix) / OpenRAIL M
  * [ACertainThing](https://huggingface.co/JosephusCheung/ACertainThing) / CreativeML OpenRAIL M
* [BalorMix-V4.1](https://huggingface.co/ploughB660/BalorMix-V4) / CreativeML OpenRAIL M
      </details>
    </div>
  </div>

  <h4>🔧 推奨設定 / Recommended Settings</h4>
  <div class="px-2">
    <table class="table-auto border mt-0 text-sm">
      <tbody>
        <tr>
          <td class="pl-2" style="width: 12rem;">
            VAE
          </td>
          <td>
            <a href="https://huggingface.co/stabilityai/sd-vae-ft-mse-original">vae-ft-mse-840000-ema-pruned</a>
          </td>
        </tr>
        <tr>
          <td class="pl-2">
            Negative Embedding
          </td>
          <td>
            <a href="https://huggingface.co/datasets/gsdf/EasyNegative">EasyNegative</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4>🖼️ 例 / Examples</h4>
  <div class="container mx-auto px-2">
    <div class="flex flex-wrap min-w-min items-baseline">
      <div class="p-1 flex-2" style="width: 100%;">blue_pencil-v5b</div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v5b/1.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            cute girl, garden, sunset
            Negative prompt: EasyNegative
            Steps: 20
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 3384784851
            Size: 768x768
            Denoising strength: 0.6
            Hires upscale: 2
            Hires upscaler: Latent (nearest-exact)
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v5b/2.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            (robot:1.1), abandoned city, scenery
            Negative prompt: EasyNegative
            Steps: 20
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 1038840067
            Size: 768x768
            Denoising strength: 0.5
            Hires upscale: 2
            Hires upscaler: SwinIR_4x
          </pre>
        </div>
      </div>
      <div class="p-1 flex-2" style="width: 100%;">blue_pencil-v5</div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v5/1.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            animal girl, jungle, scenery
            Negative prompt: EasyNegative, animal tail
            Steps: 30
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 1859865872
            Size: 768x768
            Denoising strength: 0.55
            Hires upscale: 2
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v5/2.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            robotic girl, laboratory, indoors
            Negative prompt: EasyNegative
            Steps: 30
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 3600640974
            Size: 768x768
            Denoising strength: 0.6
            Hires upscale: 2
          </pre>
        </div>
      </div>
    </div>
  </div>
</div>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v4" class="mt-0 text-2xl">
  <code>blue_pencil-v4</code> <small>(<code>@20230227</code>)</small>
</h3>

<div>
  混ぜ方を微調整したモデルです。

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

  <h4>🌱 マージ元モデル / Merged models</h4>
  <div class="px-2">
    <div class="border p-2">
      <details>

* [Waifu Diffusion](https://huggingface.co/hakurei/waifu-diffusion-v1-4) / CreativeML OpenRAIL M 
* [Evt_M](https://huggingface.co/haor/Evt_M) / CreativeML OpenRAIL M
  * [Evt_V4](https://huggingface.co/haor/Evt_V4-preview) / CreativeML OpenRAIL M
    * [ACertainty](https://huggingface.co/JosephusCheung/ACertainty) / CreativeML OpenRAIL M
* [Hentai Diffusion](https://www.cognitionai.org/hdhowtogetstarted) / BigScience OpenRAIL M
* [Elysium_Anime_V3](https://huggingface.co/hesw23168/SD-Elysium-Model) / Openrail M
* [AniReal](https://huggingface.co/Hosioka/AniReal) / CreativeML OpenRAIL M
* [WhiteSpace Prism](https://civitai.com/models/12933/whitespace-prism) / CreativeML OpenRAIL M
  * [pastel-mix](https://huggingface.co/andite/pastel-mix) / Modified CreativeML OpenRAIL M
    * [dpepmkmp](https://huggingface.co/closertodeath/dpepmkmp) / CreativeML OpenRAIL M
    * [Tea](https://huggingface.co/andite/desserts) / CreativeML OpenRAIL M
    * [basil_mix](https://huggingface.co/nuigurumi/basil_mix) / OpenRAIL M
    * LoRAs
      * Magic LORA / ???
      * Jordan_3 / ???
      * [sttabi_v1.4-04](https://huggingface.co/dolphinz/stlora) / CC BY-NC 4.0
      * [xlimo768](https://huggingface.co/closertodeath/ctdlora) / CC BY-NC 2.0
      * [dpep 2 768](https://huggingface.co/closertodeath/ctdlora) / CC BY-NC 2.0
    * ❌ Run on services that generate images for money
    * ❌ Sell this model or merges using this model
* [HighRiseMixV2](https://huggingface.co/0RisingStar0/HighRiseMixV2) / CreativeML OpenRAIL M
  * [AbyssOrangeMix2_NSFW](https://huggingface.co/WarriorMama777/OrangeMixs) / CreativeML OpenRAIL M
    * [AnythingV3.0](https://huggingface.co/Linaqruf/anything-v3.0) / CreativeML OpenRAIL M
    * [basil_mix](https://huggingface.co/nuigurumi/basil_mix) / OpenRAIL M
    * NovelAI / ???
    * Gape60 / ???
  * [AnythingV4.5](https://huggingface.co/andite/anything-v4.0) / CreativeML OpenRAIL M
  * [AikimiXPv1.0](https://huggingface.co/Aikimi/AikimiX) / unknown
  * [AikimixCv1.5](https://huggingface.co/Aikimi/AikimiX) / unknown
  * [basil_mix_fixed](https://huggingface.co/nuigurumi/basil_mix) / OpenRAIL M
  * [Counterfeit-V2.0](https://huggingface.co/gsdf/Counterfeit-V2.0) / CreativeML OpenRAIL M
  * [Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5) / CreativeML OpenRAIL M
  * [EerieOrangeMix2](https://huggingface.co/WarriorMama777/OrangeMixs) / CreativeML OpenRAIL M
    * [Instagram](https://huggingface.co/cafeai/cafe-instagram-sd-1-5-v6) / AGPL-3.0
    * F222 / ???
    * [Elysium_V1](https://huggingface.co/hesw23168/SD-Elysium-Model) / OpenRAIL M
    * NovelAI / ???
    * Gape60 / ???
  * [pastelmix-better-vae](https://huggingface.co/andite/pastel-mix) / Modified CreativeML OpenRAIL M
  * [powercolor.v2](https://civitai.com/models/6167/powercolorv2) / CreativeML OpenRAIL M
* [Nabylon-v1.3](https://huggingface.co/NegiInNattoMaki/Nabylon) / CreativeML OpenRAIL M
  * [AbyssOrangeMix2](https://huggingface.co/WarriorMama777/OrangeMixs) / CreativeML OpenRAIL M
  * [LonganMix](https://huggingface.co/Hemlok/LonganMix) / other
    * [7th_Layer](https://huggingface.co/syaimu/7th_Layer) / ???
  * and others
* [grapefruitv4](https://civitai.com/models/2583) / Modified CreativeML OpenRAIL M
  * [AnythingV3.0](https://huggingface.co/Linaqruf/anything-v3.0) / CreativeML OpenRAIL M
  * [Elysium_V2](https://huggingface.co/hesw23168/SD-Elysium-Model) / OpenRAIL M
  * [AbyssOrangeMix](https://huggingface.co/WarriorMama777/OrangeMixs) / CreativeML OpenRAIL M
    * [Instagram](https://huggingface.co/cafeai/cafe-instagram-sd-1-5-v6) / AGPL-3.0
    * F222 / ???
    * [AnythingV3.0](https://huggingface.co/Linaqruf/anything-v3.0) / CreativeML OpenRAIL M
    * NovelAI / ???
    * Gape60 / ???
  * [AbyssOrangeMix2](https://huggingface.co/WarriorMama777/OrangeMixs) / CreativeML OpenRAIL M
  * [basil_mix](https://huggingface.co/nuigurumi/basil_mix) / OpenRAIL M
  * and LoRAs
  * ❌ Run on services that generate images for money
  * ❌ Sell this model or merges using this model
* [VaLJ-fp32](https://huggingface.co/Hemlok/VaLMix) / CreativeML OpenRAIL M
  * [pastel-mix](https://huggingface.co/andite/pastel-mix) / Modified CreativeML OpenRAIL M
  * [ACertainThing](https://huggingface.co/JosephusCheung/ACertainThing) / CreativeML OpenRAIL M
  * [basil_mix](https://huggingface.co/nuigurumi/basil_mix) / OpenRAIL M
  * [Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5) / CreativeML OpenRAIL M
  * [openjourney](https://huggingface.co/prompthero/openjourney) / CreativeML OpenRAIL M
* [TriPhase_B](https://huggingface.co/Lucetepolis/TriPhaze) / CreativeML OpenRAIL M
  * [ultracolor.v4](https://civitai.com/models/5777/ultracolorv4) / CreativeML OpenRAIL M
  * [Counterfeit-V2.5](https://huggingface.co/gsdf/Counterfeit-V2.5) / CreativeML OpenRAIL M
  * [Treebark](https://huggingface.co/HIZ/aichan_pick) / ???
    * [AnythingV3.0](https://huggingface.co/Linaqruf/anything-v3.0) / CreativeML OpenRAIL M
    * NovelAI / ???
    * Gape60 / ???
    * [basil_mix](https://huggingface.co/nuigurumi/basil_mix) / OpenRAIL M
    * [SXD](https://civitai.com/models/1169/sxd) / CreativeML OpenRAIL M
* [Balor-V2.5](https://huggingface.co/ploughB660/Balor-V3) / CreativeML OpenRAIL M
  * [Elysium_V2](https://huggingface.co/hesw23168/SD-Elysium-Model) / OpenRAIL M
  * [ultracolor.v4](https://civitai.com/models/5777/ultracolorv4) / CreativeML OpenRAIL M
  * [basil_mix](https://huggingface.co/nuigurumi/basil_mix) / OpenRAIL M
  * [ACertainThing](https://huggingface.co/JosephusCheung/ACertainThing) / CreativeML OpenRAIL M

      </details>
    </div>
  </div>

  <h4>🔧 推奨設定 / Recommended Settings</h4>
  <div class="px-2">
    <table class="table-auto border mt-0 text-sm">
      <tbody>
        <tr>
          <td class="pl-2" style="width: 12rem;">
            VAE
          </td>
          <td>
            <a href="https://huggingface.co/stabilityai/sd-vae-ft-mse-original">vae-ft-mse-840000-ema-pruned</a>
          </td>
        </tr>
        <tr>
          <td class="pl-2">
            Negative Embedding
          </td>
          <td>
            <a href="https://huggingface.co/datasets/gsdf/EasyNegative">EasyNegative</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4>🖼️ 例 / Examples</h4>
  <div class="container mx-auto px-2">
    <div class="flex flex-wrap min-w-min items-baseline">
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v4/1.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girl, kyoto, scenery
            Negative prompt: EasyNegative
            Steps: 40
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 2236433764
            Size: 768x768
            Denoising strength: 0.65
            Hires upscale: 2
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v4/2.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girl, wasteland, scenery
            Negative prompt: EasyNegative
            Steps: 40
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 252972019
            Size: 768x768
            Denoising strength: 0.6
            Hires upscale: 2
          </pre>
        </div>
      </div>
    </div>
  </div>
</div>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v3" class="mt-0 text-2xl">
  <code>blue_pencil-v3</code> <small>(<code>@20230223</code>)</small>
</h3>

<div>
  blue_pencil-v2 を微妙に変更したモデルです。<br />
  雰囲気は変わってませんが若干構図が変化すると思います。

  <h4>📄 ライセンス / License</h4>
  <div class="px-2">
    <table class="table-fixed border mt-0 text-xs">
      <tbody>
        <tr>
          <td class="px-4 text-base text-bold" colspan="2">
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

  <h4>🌱 マージ元モデル / Merged models</h4>
  <div class="px-2">
    <div class="border p-2">
      <details>

* [HighRiseMixV2](https://huggingface.co/0RisingStar0/HighRiseMixV2)
  * AbyssOrangeMix2_NSFW
  * AnythingV4.5
  * AikimiXPv1.0
  * AikimixCv1.5
  * BasilMixFixed
  * Counterfeit V2.0
  * CounterfeitV2.5
  * EerieOrangeMix2
  * pastelmix-better-vae
  * PowercolorV2
* [Evt_M](https://huggingface.co/haor/Evt_M)
  * Evt_V4
    * ACertainty
* [GrapefuitV4](https://huggingface.co/iZELX1/Grapefruit)
  * AnythingV3
  * ElysiumV2
  * AbyssOrangeMix
  * AbyssOrangeMix2
  * basilMix
* [Elysium_Anime_V3](https://huggingface.co/hesw23168/SD-Elysium-Model)
* [VaLJMix](https://huggingface.co/Hemlok/VaLMix)
  * pastel-mix
  * ACertainThing
  * basil_mix
  * Counterfeit-V2.5
  * openjourney
* [HD-22](https://www.cognitionai.org/hdhowtogetstarted)
* [7th_anime_v3_testA](https://huggingface.co/syaimu/7th_test)
* [AniReal](https://huggingface.co/Hosioka/AniReal)
* [atwcustom_V4](https://huggingface.co/atsuwo/ATW-custom)
* [Nabylon-v1.2](https://huggingface.co/NegiInNattoMaki/Nabylon-v1.0)
  * AbyssOrangeMix2
  * LonganMix
  * and more
* [TriPhaze_B](https://huggingface.co/Lucetepolis/TriPhaze)
  * ultracolor.v4
  * Counterfeit-V2.5
  * Treebark
* [Balor-V2.5](https://huggingface.co/ploughB660/Balor-V3)
  * Elysium_anime_V
  * Ultracolor4
  * basil mix

      </details>
    </div>
  </div>

  <h4>🔧 推奨設定 / Recommended Settings</h4>
  <div class="px-2">
    <table class="table-auto border mt-0 text-sm">
      <tbody>
        <tr>
          <td class="pl-2" style="width: 12rem;">
            VAE
          </td>
          <td>
            <a href="https://huggingface.co/stabilityai/sd-vae-ft-mse-original">vae-ft-mse-840000-ema-pruned</a>
          </td>
        </tr>
        <tr>
          <td class="pl-2">
            Negative Embedding
          </td>
          <td>
            <a href="https://huggingface.co/datasets/gsdf/EasyNegative">EasyNegative</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4>🖼️ 例 / Examples</h4>
  <div class="container mx-auto px-2">
    <div class="flex flex-wrap min-w-min items-baseline">
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v3/1.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girl, tokyo, scenery
            Negative prompt: EasyNegative
            Steps: 40
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 1874281989
            Size: 768x768
            Denoising strength: 0.65
            Hires upscale: 2
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v3/2.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girl, bed room, cute clothes
            Negative prompt: EasyNegative
            Steps: 50
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 2666530891
            Size: 768x768
            Denoising strength: 0.6
            Hires upscale: 2
          </pre>
        </div>
      </div>
    </div>
  </div>
</div>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v2" class="mt-0 text-2xl">
  <code>blue_pencil-v2b</code> <small>(<code>@20230219</code>)</small> / <code>blue_pencil-v2</code> <small>(<code>@20230217</code>)</small>
</h3>

<div>
  <a href="https://huggingface.co/WarriorMama777/OrangeMixs">AbyssOrangeMix3A1</a>をベースに配合しなおしたモデルです。<br />
  blue_pencil-v2b は Balor-V2 の代わりに Balor-V3 を階層マージしたモデルです。

  <h4>📄 ライセンス / License</h4>
  <div class="px-2">
    <table class="table-fixed border mt-0 text-xs">
      <tbody>
        <tr>
          <td class="px-4 text-base text-bold" colspan="2">
            <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license">
              修正 CreativeML OpenRAIL-M ライセンス / Modified CreativeML OpenRAIL-M license
            </a>
          </td>
        </tr>
        <tr>
          <td class="align-middle px-2 w-8">
            <span class="text-red-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
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
            <span class="text-red-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
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

  <h4>🌱 マージ元モデル / Merged models</h4>
  <div class="px-2">
    <div class="border p-2">
      <details>

* [AbyssOrangeMix3A1](https://huggingface.co/WarriorMama777/OrangeMixs)
  * AnythingV3.0
  * ChilloutMix
  * GAPE60
  * Counterfeit2.5
  * Kenshi
* [Evt_M](https://huggingface.co/haor/Evt_M)
  * Evt_V4
    * ACertainty
* [GingerMixR](https://huggingface.co/Hemlok/GingerMix)
  * LimeMixV2
* [Elysium_Anime_V3](https://huggingface.co/hesw23168/SD-Elysium-Model)
* [VaLJMix](https://huggingface.co/Hemlok/VaLMix)
  * pastel-mix
  * ACertainThing
  * basil_mix
  * Counterfeit-V2.5
  * openjourney
* [HD-22](https://www.cognitionai.org/hdhowtogetstarted)
* [7th_anime_v3_testA](https://huggingface.co/syaimu/7th_test)
* [AniReal](https://huggingface.co/Hosioka/AniReal)
* [atwcustom_V4](https://huggingface.co/atsuwo/ATW-custom)
* [Nabylon-v1.2](https://huggingface.co/NegiInNattoMaki/Nabylon-v1.0)
  * AbyssOrangeMix2
  * LonganMix
  * and more
* [TriPhaze_B](https://huggingface.co/Lucetepolis/TriPhaze)
  * ultracolor.v4
  * Counterfeit-V2.5
  * Treebark
* [Balor-V2](https://huggingface.co/ploughB660/Balor-V2)
* [Balor-V3](https://huggingface.co/ploughB660/Balor-V3)
      </details>
    </div>
  </div>

  <h4>🔧 推奨設定 / Recommended Settings</h4>
  <div class="px-2">
    <table class="table-auto border mt-0 text-sm">
      <tbody>
        <tr>
          <td class="pl-2" style="width: 12rem;">
            VAE
          </td>
          <td>
            <a href="https://huggingface.co/stabilityai/sd-vae-ft-mse-original">vae-ft-mse-840000-ema-pruned</a>
          </td>
        </tr>
        <tr>
          <td class="pl-2">
            Negative Embedding
          </td>
          <td>
            <a href="https://huggingface.co/datasets/gsdf/EasyNegative">EasyNegative</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4>🖼️ 例 / Examples</h4>
  <div class="container mx-auto px-2">
    <div class="flex flex-wrap min-w-min items-baseline">
      <div class="p-1 flex-2" style="width: 100%;">blue_pencil-v2b</div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v2b/1.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girl, berlin, scenery
            Negative prompt: EasyNegative
            Steps: 30
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 3164975857
            Size: 768x768
            Denoising strength: 0.65
            Hires upscale: 2
          </pre>
        </div>
      </div>
      <div class="p-1 flex-2" style="width: 100%;">blue_pencil-v2</div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v2/1.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girl, tokyo, scenery
            Negative prompt: EasyNegative
            Steps: 30
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 205537258
            Size: 768x768
            Denoising strength: 0.65
            Hires upscale: 2
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v2/2.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girl, spacesuit, beautiful earth, scenery, on the moon
            Negative prompt: EasyNegative
            Steps: 50
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 1069444343
            Size: 960x640
            Denoising strength: 0.6
            Hires upscale: 2
          </pre>
        </div>
      </div>
    </div>
  </div>
</div>

<hr class="my-6 h-0.5 border-t-0 opacity-100 dark:opacity-50" style="background-color: rgb(245 245 245/var(--tw-bg-opacity));">

<h3 id="blue_pencil-v1" class="mt-0 text-2xl">
  <code>blue_pencil-v1b</code> <small>(<code>@20230212</code>)</small> / <code>blue_pencil-v1</code> <small>(<code>@20230211</code>)</small>
</h3>

<div>
  blue_pencil-v1b は<a href="https://civitai.com/models/4758/amalgammix">Amalgam_Mix</a>の代わりに<a href="https://huggingface.co/ploughB660/Balor-V2">Balor-V2</a>を階層マージしたモデルです

  <h4>📄 ライセンス / License</h4>
  <div class="px-2">
    <table class="table-fixed border mt-0 text-xs">
      <tbody>
        <tr>
          <td class="px-4 text-base text-bold" colspan="2">
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

  <h4>🌱 マージ元モデル / Merged models</h4>
  <div class="px-2">
    <div class="border p-2">
      <details>

* [Defmix-v1.1](https://huggingface.co/Defpoint/Defmix-v1.0)
  * Counterfeit v1.0
  * Counterfeit v2.0
  * Basil Mix
  * Anything v4.0
* [PastelRainier](https://huggingface.co/Hemlok/RainierMix)
  * ACertainThing
  * Anything-V4.5
  * Counterfeit-V2.0
  * Evt_V4-preview
  * basil_mix
  * pastel-mix
* [GingerMixR](https://huggingface.co/Hemlok/GingerMix)
  * LimeMixV2
* [Elysium_Anime_V3](https://huggingface.co/hesw23168/SD-Elysium-Model)
* [SukiyakiMix-v1.0](https://huggingface.co/Vsukiyaki/SukiyakiMix-v1.0)
  * pastel-mix
  * AbyssOrangeMix2
* [HD-20](https://www.cognitionai.org/hdhowtogetstarted)
* [7th_anime_v3_testA](https://huggingface.co/syaimu/7th_test)
* [AniReal](https://huggingface.co/Hosioka/AniReal)
* [TriPhaze_B](https://huggingface.co/Lucetepolis/TriPhaze)
  * ultracolor.v4
  * Counterfeit-V2.5
  * Treebark
* [Nabylon-v1.2](https://huggingface.co/NegiInNattoMaki/Nabylon-v1.0)
  * AbyssOrangeMix2
  * LonganMix
  * and more
* [atwcustom_V4](https://huggingface.co/atsuwo/ATW-custom)
* [Amalgam_Mix](https://civitai.com/models/4758/amalgammix)
* [Balor-V2](https://huggingface.co/ploughB660/Balor-V2)
      </details>
    </div>
  </div>

  <h4>🔧 推奨設定 / Recommended Settings</h4>
  <div class="px-2">
    <table class="table-auto border mt-0 text-sm">
      <tbody>
        <tr>
          <td class="pl-2" style="width: 12rem;">
            VAE
          </td>
          <td>
            <a href="https://huggingface.co/stabilityai/sd-vae-ft-mse-original">vae-ft-mse-840000-ema-pruned</a>
          </td>
        </tr>
        <tr>
          <td class="pl-2">
            Negative Embedding
          </td>
          <td>
            <a href="https://huggingface.co/datasets/gsdf/EasyNegative">EasyNegative</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4>🖼️ 例 / Examples</h4>
  <div class="container mx-auto px-2">
    <div class="flex flex-wrap min-w-min items-baseline">
      <div class="p-1 flex-2" style="width: 100%;">blue_pencil-v1b</div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v1b/1.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girl, tokyo, scenery
            Negative prompt: EasyNegative
            Steps: 30
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 205537258
            Size: 768x768
            Denoising strength: 0.65
            Hires upscale: 2
          </pre>
        </div>
      </div>
      <div class="p-1 flex-2" style="width: 100%;">blue_pencil-v1</div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="flex-1">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v1/1-2.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girl, tokyo, scenery
            Negative prompt: EasyNegative
            Steps: 30
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 2526423076
            Size: 768x768
            Denoising strength: 0.6
            Hires upscale: 2
          </pre>
        </div>
      </div>
      <div class="p-1 flex-1" style="width: 50%; min-width: 320px;">
        <div class="w-full">
          <img
            alt="gallery"
            class="block h-full w-full rounded-t-lg object-contain object-center"
            src="https://huggingface.co/bluepen5805/blue_pencil/resolve/main/images/blue_pencil-v1/2-2.png"
            loading="lazy"
          />
        </div>
        <div class="w-full">
          <pre class="w-full" style="white-space: pre-line;">
            girl, early teen, kimono, sakura, particles
            Negative prompt: EasyNegative
            Steps: 20
            Sampler: DPM++ SDE Karras
            CFG scale: 7.5
            Seed: 4036639388,
            Size: 512x768
            Denoising strength: 0.62
            Hires upscale: 2
          </pre>
        </div>
      </div>
    </div>
  </div>
</div>
