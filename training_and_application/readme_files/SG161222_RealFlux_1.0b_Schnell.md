---
license: apache-2.0
---
<strong>Check my exclusive models on Mage: </strong><a href="https://www.mage.space/play/4371756b27bf52e7a1146dc6fe2d969c" rel="noopener noreferrer nofollow"><strong>ParagonXL</strong></a><strong> / </strong><a href="https://www.mage.space/play/df67a9f27f19629a98cb0fb619d1949a" rel="noopener noreferrer nofollow"><strong>NovaXL</strong></a><strong> / </strong><a href="https://www.mage.space/play/d8db06ae964310acb4e090eec03984df" rel="noopener noreferrer nofollow"><strong>NovaXL Lightning</strong></a><strong> / </strong><a href="https://www.mage.space/play/541da1e10976ab82976a5cacc770a413" rel="noopener noreferrer nofollow"><strong>NovaXL V2</strong></a><strong> / </strong><a href="https://www.mage.space/play/a56d2680c464ef25b8c66df126b3f706" rel="noopener noreferrer nofollow"><strong>NovaXL Pony</strong></a><strong> / </strong><a href="https://www.mage.space/play/b0ab6733c3be2408c93523d57a605371" rel="noopener noreferrer nofollow"><strong>NovaXL Pony Lightning</strong></a><strong> / </strong><a href="https://www.mage.space/play/e3b01cd493ed86ed8e4708751b1c9165" rel="noopener noreferrer nofollow"><strong>RealDreamXL</strong></a><strong> / </strong><a href="https://www.mage.space/play/ef062fc389c3f8723002428290c1158c" rel="noopener noreferrer nofollow"><strong>RealDreamXL Lightning</strong></a></p>
<b>It's important! Read it!</b><br>
This version of the model may contain errors in anatomy and text, and it may also contain artifacts.<br>

<b>You can support me directly on Boosty - https://boosty.to/sg_161222</b>

<h2>Using the Model</h2>
<b>Compact Version</b> The Compact version already includes VAE, Clip-L, and T5XXL.
  <ul>
      <li>For ComfyUI, place the model in the following path: ComfyUI_windows_portable\ComfyUI\models\checkpoints</li>
      <li>For Forge, place the model in the following path: webui_forge_cu121_torch231\webui\models\Stable-diffusion</li>
  </ul>

<b>Transformer Version (Unet)</b> The Transformer version requires you to have Flux VAE, Clip-L, and T5XXL.
  <ul>
      <li>For ComfyUI:</li>
          <ul>
              <li>Place the VAE in the following path: ComfyUI_windows_portable\ComfyUI\models\vae</li>
              <li>Place Clip-L and T5XXL in the following path: ComfyUI_windows_portable\ComfyUI\models\clip</li>
              <li>Place the Transformer (Unet) in the following path: ComfyUI_windows_portable\ComfyUI\models\unet</li>
          </ul>
  </ul>

Then you can use the Basic Workflow by moving the image into the ComfyUI workspace.

<h2>Optimal Generation Settings</h2>

<b>Sampling Method and Schedule Type:</b> Euler Beta<br>
<b>Sampling Steps:</b> 4-6<br>
<b>Distilled CFG Scale:</b> 3.5<br>
<b>CFG Scale:</b> 1.0

<h2>Limitations of RealFlux 1.0b Schnell</h2>
    <ul>
        <li>This version of the model does not have a variety of styles and is intended for realism.</li>
        <li>Cannot generate NSFW content.</li>
        <li>There may be issues with anatomy and text, as the model is based on Flux Schnell.</li>
    </ul>