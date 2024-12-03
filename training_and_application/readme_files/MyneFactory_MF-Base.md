---
license: creativeml-openrail-m
language:
- en
pipeline_tag: text-to-image
tags:
- text-to-image
- stable-diffusion
- anime
- aiart
---
<div style="padding-bottom: 40px">
  <!--Logo-->
  <div style="text-align: center;">
    <img src="https://logo.mynefactory.ai/MF-Base" alt="Myne Factory Logo" style="margin:0;">
  </div>
  <!--Table of contents-->
  <div style="font-size: 14px; padding: 4px 8px; display: flex; justify-content: space-around; color: black; font-weight: 500;">
    <a href="#model-info" style="text-decoration: none; color: #204F8F">Model Info</a> | 
    <a href="#recsettings" style="text-decoration: none; color: #204F8F"">Recommmended Settings</a> | 
    <a href="#promptformat" style="text-decoration: none; color: #204F8F"">Prompt Format</a> | 
    <a href="#examples" style="text-decoration: none; color: #204F8F"">Examples</a> |
    <a href="#mynelinks" style="text-decoration: none; color: #204F8F"">Socials</a>
  </div>
</div>
<!--Title-->

<div style="text-align: center; display: flex; flex-direction: column; padding-bottom: 10px;">
  <h1 style=" font-size:38px; padding:2px; margin:20px 0 0 0">Myne Factory Base Model</h1>
  <span style=" font-size:18px; padding:2px; margin:5px 0 0 0">The foundation of our models</span>
</div>


<!--Example shortcuts-->
<div style="display: flex; align-items:top; justify-content:space-around; align-items: center; padding-bottom: 0px;">
  <a href="#example3" style="padding:10px">
    <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/2.jpg" style="margin:0"/>
  </a>
  <a href="#example6" style="padding:5px">
    <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/6.jpg" style="margin:0"/>
  </a>
  <a href="#example7" style="padding:5px">
    <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/7.jpg" style="margin:0"/>
  </a>
  <a href="#example4" style="padding:10px">
    <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/4.jpg" style="margin:0"/>
  </a>
</div>
<div style="display: flex; align-items:top; justify-content:space-around; align-items: center; padding-bottom: 0px;">
  <a href="#example11" style="padding:0px">
    <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/9.jpg" style="margin:0"/>
  </a>
  <a href="#example9" style="padding:20px">
    <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/grid-6502.jpg" style="margin:0"/>
  </a>
  <a href="#example12" style="padding:0px">
    <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/10.jpg" style="margin:0"/>
  </a>
</div>
<div style="display: flex; align-items:top; justify-content:space-around; align-items: center; padding-bottom: 0px;">
  <a href="#example5" style="padding:5px">
    <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/5.jpg" style="margin:0"/>
  </a>
  <a href="#example1" style="padding:5px">
    <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/3.jpg" style="margin:0"/>
  </a>
  <a href="#example8" style="padding:5px">
    <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/8.jpg" style="margin:0"/>
  </a>
</div>
<a href="https://huggingface.co/MyneFactory/MF-Base/tree/main/Example%20Pictures/V1.0%20Examples">All example images</a>
<!--Model Info-->
<div style="padding:10px; margin: 40px 0; background-color: #f9f9f9; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" id="model-info">
  <h2 style="font-size:28px; font-family: Arial, Helvetica, sans-serif; font-weight: bold; margin:0; color: #222;">Model Info</h2>
  <p style="font-size: 18px;  color: #666;">
    <strong>Downloads: </strong>
    <a style="color: #333" href="https://huggingface.co/MyneFactory/MF-Base/blob/main/Full%20release%20models/MyneFactoryBase%20V1.0.ckpt">MyneFactoryBase V1.0.ckpt (2.13 GB), </a>
    <a style="color: #333" href="https://huggingface.co/MyneFactory/MF-Base/blob/main/Full%20release%20models/MyneFactoryBase%20V1.0.safetensors">MyneFactoryBase V1.0.safetensors (2.13 GB)</a>
  </p>
  <!-- Technical details start here -->
  <h3 style="font-size:24px; font-family: Arial, Helvetica, sans-serif; font-weight: bold; margin:20px 0; color: #222;">Technical Details</h3>
  <h4 style="font-size:20px; font-family: Arial, Helvetica, sans-serif; font-weight: bold; margin:20px 0; color: #222;">Model Training</h4>
  <p style="font-size: 18px; color: #666;">
    MyneFactoryBase was trained using ~18000 high scored samples from Yande.re and ~5000 high scored samples from Konachan. File captions were generated using 3 iterations of WD1.4 tagger to ensure maximum identification of objects within the training data. A second captioning run was done using one tagger with a reduced threshold to produce shorter captions for later use. Adam optimizer was used with a manually set maximum learning rate and cosine decay. Training was done on an RTX 4090 with a batch size of 4, utilizing DDIM sample scheduler and DDPM noise scheduler with mix precision.
  </p>
  <h4 style="font-size:20px; font-family: Arial, Helvetica, sans-serif; font-weight: bold; margin:20px 0; color: #222;">Text Encoder Training</h4>
  <p style="font-size: 18px; color: #666;">
    Text Encoder was trained for 50% of the training durations, freezing and unfreezing every 10ep. During the final 20ep of finetuning, the TE was frozen.
  </p>
  <h4 style="font-size:20px; font-family: Arial, Helvetica, sans-serif; font-weight: bold; margin:20px 0; color: #222;">Block Merge</h4>
  <p style="font-size: 18px; color: #666;">
    At the ep20 milestone, a block merge was done with BasilMix. However, it was evident that the merged weights were being trained out quickly, and the weights had entirely shifted back to the training data by the end of the training. Ultimately, the decision was made to not use a block merge for the final release.
  </p>
  <p style="font-size: 18px;  color: #666;">
    For more detailed technical information on the training process and model architecture, please refer to <a style="color: #333" href="https://docs.google.com/document/d/1smqGRy3Y2ADGWAXMLs9LoYmw9-_7M9f1bzlbux-O56w">this document</a>.
  </p>
  <!-- Technical details end here -->
  <p style="font-size: 18px; color: #666;">
    <strong>Authors: </strong><span>金Goldkoron, tsmkirby, Juusoz</span>
    <div>Visit our <a href="https://discord.gg/GdJBzaTSCF">Discord</a> community if you have any questions.</div>
  </p>
</div>
<!--Prompt format-->
<div style="padding:10px; margin: 40px 0; background-color: #f9f9f9; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" id="promptformat">
  <h2 style="font-size:28px; font-family: Arial, Helvetica, sans-serif; font-weight: bold; margin:0; color: #222;">Prompt Format</h2>
  <p style="font-size: 18px; color: #666;">It is recommended to use booru styled tags to for the prompts.</p>
  <div style="padding:8px">
    <strong style="font-size: 16px; color: #333;">Example:</strong>
    <code style="font-size: 14px; padding: 6px; line-height: 22px; background-color: #f5f5f5; border-radius: 4px; color: #000;">woman, decorated horns, long robes, fog, long curly hair, freckles, solo, masterpiece, reflective, depth of field, caustics, detailed night, forest, leaves, moonlight, eyes, orange hair, green eyes, vines</code>
  </div>
  <div style="padding:8px">
    <strong style="font-size: 16px; color: #333;">Example:</strong>
    <code style="font-size: 14px; padding: 6px; line-height: 22px; background-color: #f5f5f5; border-radius: 4px; color: #000;">1girl, solo, skirt, book, glasses, long hair, looking at viewer, bookshelf, jacket, plaid skirt, school uniform, long sleeves, parted lips, semi-rimless eyewear, bangs, blush, holding, blazer, indoors, sweater, under-rim eyewear, red-framed eyewear, holding book, brown eyes, library, sitting</code>
  </div>
  <p style="font-size: 18px; color: #666;">The tags were generated with <a href="https://github.com/toriato/stable-diffusion-webui-wd14-tagger">WD14 tagger</a> for the dataset.</p>
  <p style="font-size: 18px; color: #666;">The model has also been fine tuned to be better at handling shorter prompts.</p>
</div>
<!--Recommmended settings-->
<div style="padding:10px; margin: 40px 0; background-color: #f9f9f9; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" id="recsettings">
  <h2 style="font-size:28px; font-family: Arial, Helvetica, sans-serif; font-weight: bold; margin:0; color: #222;">Recommended Settings</h2>
  <p style="font-size: 18px; margin-bottom: 4px; color: #666;">This model performs best with the following settings:</p>
  <ul style="list-style-type: none; padding: 0 8px">
    <li style="margin-bottom: 10px;">
      <div style="display: inline-block; width: 120px; font-weight: 500; color: #333;">Image Size</div> 
      <div style="color: #666; padding-left:8px;"><strong>1024x576</strong> for wide 16:9, <strong>768x768</strong> for square, and <strong>640x1024</strong> for portrait</div>
      <i style="color: #666666e8; padding-left:8px;">Feel free to experiment with higher resolutions, Juusoz made all the examples at higher than recommended resolutions</i>
    </li>
    <li style="margin-bottom: 10px;">
      <div style="display: inline-block; width: 120px; font-weight: 500; color: #333;">Vae</div> 
      <div style="color: #666; padding-left:8px;"><a href="https://huggingface.co/stabilityai/sd-vae-ft-mse-original/blob/main/vae-ft-mse-840000-ema-pruned.ckpt">vae-ft-mse-840000-ema-pruned.ckpt</a></div>
    </li>
    <li style="margin-bottom: 10px;">
      <div style="display: inline-block; width: 120px; font-weight: 500; color: #333;">Sampler</div> 
      <div style="padding:2px 0">
        <div style="color: #666; padding-left:8px;"><strong>DPM++ SDE Karras</strong> (preferred)</div>
        <div style="color: #666; padding-left:8px;"><strong>2S Karras</strong></div>
        <i style="color: #666666e8; padding-left:8px;">Karras samplers tend to create more dynamic and interesting generations.</i>
      </div>
      <div style="padding:2px 0">
        <div style="color: #666; padding-left:8px;"><strong>Euler A</strong></div>
        <i style="color: #666666e8; padding-left:8px;">Results tends to look smoother and more Airbrushed</i>
      </div>
    </li>
    <li style="margin-bottom: 10px;">
      <div style="display: inline-block; width: 120px; font-weight: 500; color: #333;">Steps</div> 
      <div style="color: #666; padding-left:8px;"><strong>30</strong> minimum and <strong>+70</strong> can give nice results</div>
    </li>
    <li style="margin-bottom: 10px;">
      <div style="display: inline-block; width: 120px; font-weight: 500; color: #333;">Skip Clip</div> 
      <div style="color: #666;  padding-left:8px;"><strong>Clip 1</strong></div>
      <div><i style="color: #666666e8; padding-left:8px;">Clip 2 and 4 are valid for experimentation and we recommend trying it for more variation.</i></div>
    </li>
    <li style="margin-bottom: 10px; padding: 0px 10px">
      <div style="display: inline-block; width: 120px; font-weight: 500; color: #333;">CFG</div> 
      <div style="color: #666; padding-left:8px;"><strong>9-12</strong></div>
    </li>
    <p style="font-size: 18px; margin-bottom: 4px; color: #666;">Not required, but these tags improve the quality of the image:</p>
    <div style="padding:8px">
      <strong style="font-size: 16px; color: #333;">Prompt:</strong>
      <code style="font-size: 14px; padding: 6px; line-height: 22px; background-color: #f5f5f5; border-radius: 4px; color: #000;">best quality, masterpiece</code>
    </div>
    <div style="padding:8px">
      <strong style="font-size: 16px; color: #333;">Negative Prompt:</strong>
      <code style="font-size: 14px; padding: 6px; line-height: 22px; background-color: #f5f5f5; border-radius: 4px; color: #000;">lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry</code>
    </div>
  </ul>
</div>


<!--Examples-->
<div style="padding:10px; margin: 40px 0; background-color: #f9f9f9; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"" id="examples">
  <h2 style="font-size:28px; font-family: Arial, Helvetica, sans-serif; font-weight: bold; margin:0; color: #222;">Examples</h2>
  <div style="display: flex; flex-wrap: wrap; justify-content: center;">
    <!--Example 9-->
    <div style="padding: 20px; width: 100%; text-align: center;" id="example9">
      <a href="https://huggingface.co/MyneFactory/MF-Base/blob/main/Example%20Pictures/V1.0%20Examples/grid-6502.jpg">
        <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/1.jpg" style="width: 100%; margin: 0px 0; border: 1px solid #ddd;" />
      </a>
      <div>
        <div style="display: flex; flex-direction: column; text-align: left;">
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #333; display: block;">Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f5; border-radius: 4px; color: #000;">1girl, hands, eyes, eyelashes, ponytail, braids, flower hairstick, embroidery, red hair, glasses, solo, plants, sunlight, masterpiece, detailed, depth of field, reflective, caustics, realistic</code>
          </div>
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #696969; display: block;">Negative Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f59d; border-radius: 4px; color: #000;">low quality, worst quality, (bad hands), bad anatomy, watermark, signature, nude, nipples</code>
          </div>
        </div>
      </div>
      <div style="padding:10px 40px">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Steps:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">50</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Sampler:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">DPM++ SDE Karras</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">CFG Scale:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">10</code>
          </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Seed:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">2766314147</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Size:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;"> 896x1152</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Model:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">MyneFactoryBase V1.0</code>
          </div>  
        </div>
      </div>
    </div>
    <!--Example 3-->
    <div style="padding: 20px; width: 100%; text-align: center;" id="example3">
      <a href="https://huggingface.co/MyneFactory/MF-Base/blob/main/Example%20Pictures/V1.0%20Examples/36776-620829716-damaged_robot_woman_in_a_junkyard_cyberpunk_masterpiece_face.png">
        <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/2.jpg" style="width: 100%; margin: 0px 0; border: 1px solid #ddd;" />
      </a>
      <div>
        <div style="display: flex; flex-direction: column; text-align: left;">
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #333; display: block;">Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f5; border-radius: 4px; color: #000;">damaged robot woman in a junkyard, cyberpunk, masterpiece, face</code>
          </div>
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #696969; display: block;">Negative Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f59d; border-radius: 4px; color: #000;">low quality, worst quality, bad hands, bad anatomy, watermark, signature</code>
          </div>
        </div>
      </div>
      <div style="padding:10px 40px">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Steps:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">60</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Sampler:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">Euler a</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">CFG Scale:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">11</code>
          </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Seed:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">620829716</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Size:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">1024x1024</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Model:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">MyneFactoryBase-ep70</code>
          </div>  
        </div>
      </div>
    </div>
    <!--Example 1-->
    <div style="padding: 20px; width: 100%; text-align: center;" id="example1">
      <a href="https://huggingface.co/MyneFactory/MF-Base/blob/main/Example%20Pictures/V1.0%20Examples/38013-3406131780-android%20woman%2C%20masterpiece%2C%20caustics%2C%20depth%20of%20field%2C%20neon%20lights%2C%20eyes%2C%20steam%2C%20city%2C%20night.png">
        <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/3.jpg" style="width: 100%; margin: 0px 0; border: 1px solid #ddd;" />
      </a>
      <div>
        <div style="display: flex; flex-direction: column; text-align: left;">
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #333; display: block;">Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f5; border-radius: 4px; color: #000;">android woman, masterpiece, caustics, depth of field, neon lights, eyes, steam, city, night</code>
          </div>
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #696969; display: block;">Negative Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f59d; border-radius: 4px; color: #000;">low quality, worst quality, bad hands, bad anatomy, watermark, signature</code>
          </div>
        </div>
      </div>
      <div style="padding:10px 40px">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Steps:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">70</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Sampler:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">Euler a</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">CFG Scale:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">10.5</code>
          </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Seed:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">3406131780</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Size:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">1088x960</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Model:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">MyneFactoryBase-ep90</code>
          </div>  
        </div>
      </div>
    </div>
    <!--Example 4-->
    <div style="padding: 20px; width: 100%; text-align: center;" id="example4">
      <a href="https://huggingface.co/MyneFactory/MF-Base/blob/main/Example%20Pictures/V1.0%20Examples/37526-1550904897-Bearded%20old%20man%2C%20glasses%2C%20sitting%20at%20table%2C%20vest%2C%20solo%2C%20masterpiece%2C%20clocks%2C%20wooden%20shack.png">
        <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/4.jpg" style="width: 100%; margin: 0px 0; border: 1px solid #ddd;" />
      </a>
      <div>
        <div style="display: flex; flex-direction: column; text-align: left;">
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #333; display: block;">Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f5; border-radius: 4px; color: #000;">Bearded old man, glasses, sitting at table, vest, solo, masterpiece, clocks, wooden shack</code>
          </div>
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #696969; display: block;">Negative Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f59d; border-radius: 4px; color: #000;">low quality, worst quality, bad hands, bad anatomy, watermark, signature, breasts</code>
          </div>
        </div>
      </div>
      <div style="padding:10px 40px">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Steps:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">60</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Sampler:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">Euler a</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">CFG Scale:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">10</code>
          </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Seed:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">1550904897</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Size:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">1024x1024</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Model:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">MyneFactoryBase-ep90</code>
          </div>  
        </div>
      </div>
    </div>
    <!--Example 5-->
    <div style="padding: 20px; width: 100%; text-align: center;" id="example5">
      <a href="https://huggingface.co/MyneFactory/MF-Base/blob/main/Example%20Pictures/V1.0%20Examples/38249-1057239513-floating%20islands%2C%20caustics%2C%20depth%20of%20field%2C%20masterpiece%2C%20detailed%2C%20waterfall%2C%20reflective%2C%20fog%2C%20foggy%2C%20sunset%2C%20autumn%2C%20lens%20flare.png">
        <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/5.jpg" style="width: 100%; margin: 0px 0; border: 1px solid #ddd;" />
      </a>
      <div>
        <div style="display: flex; flex-direction: column; text-align: left;">
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #333; display: block;">Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f5; border-radius: 4px; color: #000;">floating islands, caustics, depth of field, masterpiece, detailed, waterfall, reflective, fog, foggy, sunset, autumn, lens flare, windy, scenery, leaves, town, buildings</code>
          </div>
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #696969; display: block;">Negative Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f59d; border-radius: 4px; color: #000;">low quality, worst quality, bad hands, bad anatomy, watermark, signature, sitting</code>
          </div>
        </div>
      </div>
      <div style="padding:10px 40px">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Steps:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">70</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Sampler:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">Euler a</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">CFG Scale:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">10.5</code>
          </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Seed:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">1057239513</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Size:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">1216x832</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Model:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">MyneFactoryBase-ep90</code>
          </div>  
        </div>
      </div>
    </div>
    <!--Example 6-->
    <div style="padding: 20px; width: 100%; text-align: center;" id="example6">
      <a href="https://huggingface.co/MyneFactory/MF-Base/blob/main/Example%20Pictures/V1.0%20Examples/37876-1846839782-cropped-woman%2C%20decorated%20horns%2C%20long%20robes%2C%20fog%2C%20long%20curly%20hair%2C%20freckles%2C%20solo%2C%20masterpiece%2C%20reflective%2C%20depth%20of%20field%2C%20caustics%2C%20nig.png">
        <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/6.jpg" style="width: 100%; margin: 0px 0; border: 1px solid #ddd;" />
      </a>
      <div>
        <div style="display: flex; flex-direction: column; text-align: left;">
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #333; display: block;">Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f5; border-radius: 4px; color: #000;">woman, decorated horns, long robes, fog, long curly hair, freckles, solo, masterpiece, reflective, depth of field, caustics, night, forest, leaves, moonlight, eyes, orange hair, green eyes, vines</code>
          </div>
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #696969; display: block;">Negative Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f59d; border-radius: 4px; color: #000;">low quality, worst quality, bad hands, bad anatomy, watermark, signature, kimono</code>
          </div>
        </div>
      </div>
      <div style="padding:10px 40px">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Steps:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">70</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Sampler:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">Euler a</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">CFG Scale:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">10.5</code>
          </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Seed:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">1846839782</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Size:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">1088x960</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Model:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">MyneFactoryBase-ep90</code>
          </div>  
        </div>
      </div>
    </div>
    <!--Example 7-->
    <div style="padding: 20px; width: 100%; text-align: center;" id="example7">
      <a href="https://huggingface.co/MyneFactory/MF-Base/blob/main/Example%20Pictures/V1.0%20Examples/37747-2300296201-woman%2C%20business%20suit%2C%20leather%20vest%2C%20pants%2C%20glasses%2C%20tattoos%2C%20hair%20highlights%2C%20office%2C%20masterpiece%2C%20reflective%2C%20caustics%2C%20solo%2C%20c.png">
        <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/7.jpg" style="width: 100%; margin: 0px 0; border: 1px solid #ddd;" />
      </a>
      <div>
        <div style="display: flex; flex-direction: column; text-align: left;">
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #333; display: block;">Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f5; border-radius: 4px; color: #000;">woman, business suit, leather vest, pants, glasses, tattoos, hair highlights, office, masterpiece, reflective, caustics, solo, coffee cup, curly hair, lamps, depth of field, pictures, folders, sunlight, window, city</code>
          </div>
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #696969; display: block;">Negative Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f59d; border-radius: 4px; color: #000;">low quality, worst quality, bad hands, bad anatomy, watermark, signature</code>
          </div>
        </div>
      </div>
      <div style="padding:10px 40px">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Steps:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">70</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Sampler:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">Euler a</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">CFG Scale:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">10.5</code>
          </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Seed:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">2300296201</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Size:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">1024x1024</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Model:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">MyneFactoryBase-ep90</code>
          </div>  
        </div>
      </div>
    </div>
    <!--Example 8-->
    <div style="padding: 20px; width: 100%; text-align: center;" id="example8">
      <a href="https://huggingface.co/MyneFactory/MF-Base/blob/main/Example%20Pictures/V1.0%20Examples/38285-4020336312-caustics%2C%20depth%20of%20field%2C%20masterpiece%2C%20detailed%2C%20waterfall%2C%20reflective%2C%20fog%2C%20foggy%2C%20scenery%2C%20town%2C%20buildings%2C%20waterfall%2C%20moon%2C%20n.png">
        <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/8.jpg" style="width: 100%; margin: 0px 0; border: 1px solid #ddd;" />
      </a>
      <div>
        <div style="display: flex; flex-direction: column; text-align: left;">
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #333; display: block;">Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f5; border-radius: 4px; color: #000;">caustics, depth of field, masterpiece, detailed, waterfall, reflective, fog, foggy, scenery, town, buildings, waterfall, moon, night, street, lights, cherry blossoms, stars, statue</code>
          </div>
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #696969; display: block;">Negative Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f59d; border-radius: 4px; color: #000;">low quality, worst quality, bad hands, bad anatomy, watermark, signature</code>
          </div>
        </div>
      </div>
      <div style="padding:10px 40px">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Steps:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">70</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Sampler:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">Euler a</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">CFG Scale:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">10.5</code>
          </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Seed:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">4020336312</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Size:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">1216x832</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Model:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">MyneFactoryBase-ep90</code>
          </div>  
        </div>
      </div>
    </div>
    <!--Example 11-->
    <div style="padding: 20px; width: 100%; text-align: center;" id="example11">
      <a href="https://huggingface.co/MyneFactory/MF-Base/blob/main/Example%20Pictures/V1.0%20Examples/38647-3530094527-1girl%2C%20wings%2C%20feathers%2C%20long%20hair%2C%20bloody%2C%20angel%20wings%2C%20dress%2C%20embroidery%2C%20angel%2C%20death%2C%20feathered%20wings%2C%20braid%2C%20sunset%2C%20masterp.png">
        <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/9.jpg" style="width: 100%; margin: 0px 0; border: 1px solid #ddd;" />
      </a>
      <div>
        <div style="display: flex; flex-direction: column; text-align: left;">
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #333; display: block;">Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f5; border-radius: 4px; color: #000;">1girl, wings, feathers, long hair, bloody, angel wings, dress, embroidery, angel, death, feathered wings, braid, sunset, masterpiece, detailed, caustics, depth of field, reflective</code>
          </div>
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #696969; display: block;">Negative Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f59d; border-radius: 4px; color: #000;">low quality, worst quality, bad hands, bad anatomy, watermark, signature</code>
          </div>
        </div>
      </div>
      <div style="padding:10px 40px">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Steps:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">50</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Sampler:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">DPM++ SDE Karras</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">CFG Scale:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">8</code>
          </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Seed:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">3530094527</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Size:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">704x1280</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Model:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">MyneFactoryBase-ep90</code>
          </div>  
        </div>
      </div>
    </div>
    <!--Example 12-->
    <div style="padding: 20px; width: 100%; text-align: center;" id="example12">
      <a href="https://huggingface.co/MyneFactory/MF-Base/blob/main/Example%20Pictures/V1.0%20Examples/38556-2732258039-city%2C%20wet%20road%2C%20car%2C%20sunset%2C%20masterpiece%2C%20detailed%2C%20caustics%2C%20depth%20of%20field%2C%20reflective.png">
        <img src="https://huggingface.co/MyneFactory/MF-Base/resolve/main/Example%20Pictures/V1.0%20Examples/jpgs/10.jpg" style="width: 100%; margin: 0px 0; border: 1px solid #ddd;" />
      </a>
      <div>
        <div style="display: flex; flex-direction: column; text-align: left;">
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #333; display: block;">Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f5; border-radius: 4px; color: #000;">city, wet road, car, sunset, masterpiece, detailed, caustics, depth of field, reflective</code>
          </div>
          <div style="padding: 4px 2px;">
            <strong style="font-size: 16px; color: #696969; display: block;">Negative Prompt:</strong>
            <code style="font-size: 14px;  background-color: #f5f5f59d; border-radius: 4px; color: #000;">low quality, worst quality, bad hands, bad anatomy, watermark, signature</code>
          </div>
        </div>
      </div>
      <div style="padding:10px 40px">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Steps:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">50</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Sampler:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">DPM++ SDE Karras</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">CFG Scale:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">8</code>
          </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Seed:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">2732258039</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Size:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">704x1280</code>
          </div>
          <div style="padding:4px">
            <strong style="font-size: 16px; color: #333;">Model:</strong>
            <code style="font-size: 14px; padding-left: 6px; background-color: #f5f5f5; border-radius: 4px; color: #000;">MyneFactoryBase-ep90</code>
          </div>  
        </div>
      </div>
    </div>
  </div>
</div>

<!--Links-->
<div style="padding: 10px 0; text-align: center; font-size: 18px;" id="mynelinks">
  <h2 style="font-size:28px; font-family: Arial, Helvetica, sans-serif; font-weight: bold; margin:0;">Socials</h2>
  <a href="https://mynefactory.ai" style="text-decoration: none; color: #0077c9;">Website</a> | 
  <a href="https://discord.gg/GdJBzaTSCF" style="text-decoration: none; color: #0077c9;">Discord</a> | 
  <a href="https://www.patreon.com/user?u=36154428" style="text-decoration: none; color: #0077c9;">Patreon</a>
</div>