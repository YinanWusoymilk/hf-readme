---
license: other
license_name: fair-ai-public-license-1.0-sd
license_link: https://freedevproject.org/faipl-1.0-sd/
language:
- en
base_model: KBlueLeaf/kohaku-xl-beta5
pipeline_tag: text-to-image
---
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&family=Playwrite+DE+Grund:wght@100..400&display=swap');
.title-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh;
}
/* Title Base Styling */
.title {
  text-align: center;
  letter-spacing: -0.02em;
  line-height: 1.2;
  padding: 0.5em 0;
}
.playwrite-de-grund-title {
  font-size: 40px;
  font-style: normal; /* You can change to italic if needed */
  color: black;
}
@keyframes titlePulse {
  0% { transform: scale(1); }
  100% { transform: scale(1.05); }
}
.custom-table {
  table-layout: fixed;
  width: 100%;
  border-collapse: separate;
  border-spacing: 1em;
  margin-top: 2em;
}
.custom-table td {
  width: 33.333%;
  vertical-align: top;
  padding: 0;
}
.custom-image-container {
  position: relative;
  width: 100%;
  height: 100%
  margin-bottom: 1em;
  overflow: hidden;
  align-items: center;
  border-radius: 15px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
}
.custom-image-container:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
}
.custom-image {
  width: 100%;
  height: auto;
  object-fit: cover;
  transition: transform 0.5s;
}
.last-image-container {
  display: grid;
  grid-template-columns: 1fr; /* One column for vertical layout */
  gap: 0px; /* Remove space between images */
  width: 80%; /* Adjust as needed */
  height: 100%; /* Set full height */
}
.last-image-container img {
  width: 100%; /* Full width for each image */
  height: auto; /* Maintain aspect ratio */
}
.custom-image-container:hover .custom-image {
  transform: scale(1.1);
}
.playwrite-de-grund-title .company-name {
    font-size: 40px;
}
.nsfw-filter {
  filter: blur(10px);
  transition: filter 0.3s ease;
}
.custom-image-container:hover .nsfw-filter {
  filter: blur(5px);
}
.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: opacity 0.3s;
}
.custom-image-container:hover .overlay {
  opacity: 1;
}
.overlay-text {
  font-size: 1.5em;
  font-weight: bold;
  color: #FFFFFF;
  text-align: center;
  padding: 0.5em;
  background: linear-gradient(45deg, #E74C3C, #C0392B);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.7);
}
.overlay-subtext {
  font-size: 0.85em;
  color: #F0F0F0;
  margin-top: 0.5em;
  font-style: italic;
  text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.5);
}
.model-info {
  font-style: bold;
}
@media (max-width: 768px) {
  .title {
    font-size: 3rem;
  }
  .custom-table td {
    display: block;
    width: 70%;
  }
}
.playwrite-de-grund-title .trained-by {
    font-size: 32px; /* Smaller font size for "trained by" part */
}
</style>
<head>
    <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.min.css"
  />
</head>
<body>
  <div class="title-container">
    <h1 class="title">
      <i class="fa-thin fa-palette"></i>
      <span class="playwrite-de-grund-title"><b>Illustrious XL v0.1</b><br> <span class="trained-by">trained by</span> <a rel="nofollow" href="https://onomaai.com/"><b><span class="company-name">Onoma AI</span></b></a></span>
    </h1>
  </div>
  <table class="custom-table">
    <tr>
      <td>
        <div class="custom-image-container">
          <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/65eea2d62cc24ebc6dbe16c0/dXvGxUKjcsqzt_gDWc9FU.png" alt="s00">
        </div>
        <div class="custom-image-container">
          <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/65eea2d62cc24ebc6dbe16c0/TjfHgNIgpfhX1Josy-a1h.png" alt="s01">
        </div>
        <div class="custom-image-container">
          <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/65eea2d62cc24ebc6dbe16c0/YMxjs05WcbuS5sIjeqOJr.png" alt="s02">
        </div>
      </td>
      <td>
        <div class="custom-image-container">
          <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/65eea2d62cc24ebc6dbe16c0/ChTQ2UKphqbFsyKF9ddNY.png" alt="s10">
        </div>
        <div class="custom-image-container">
          <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/65eea2d62cc24ebc6dbe16c0/PO3_B7AeUVq59OWHidEas.png" alt="s11">
        </div>
        <div class="custom-image-container">
          <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/65eea2d62cc24ebc6dbe16c0/hLR6af7AluIYQPB6GXQYh.png" alt="s12">
        </div>
      </td>
      <td>
        <div class="custom-image-container">
          <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/65eea2d62cc24ebc6dbe16c0/4kdzhZAGp_VLEqat6T5Yv.png" alt="s20">
        </div>
        <div class="custom-image-container">
          <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/65eea2d62cc24ebc6dbe16c0/05bgqY-9S2dNxtpa6WmNV.png" alt="s21">
        </div>
        <div class="custom-image-container">
          <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/65eea2d62cc24ebc6dbe16c0/yAYxcQ1IK_dytlPGObMe4.png" alt="s22">
        </div>
      </td>
    </tr>
  </table>

  <div>
    <p>
      Illustrious XL is the Illustration focused Stable Diffusion XL model which is continued from Kohaku XL Beta 5, trained by OnomaAI Research Team.
      The model focuses on utilizing large-scale annotated dataset, <a href="https://huggingface.co/datasets/nyanko7/danbooru2023">Danbooru2023.</a>
      We release the v0.1 and v0.1-GUIDED model here, under fair public ai license, however discourages the usage of model over monetization purpose / any closed source purposes.
      For full technical details, please refer to our technical report.
    </p>
    <p>
      <strong>Model Information:</strong>
    </p>
    <ul style="margin-left: 20px;">
      <li><strong>Name:</strong> Illustrious-XL-v0.1</li>
      <li><strong>Model Type:</strong> Stable Diffusion XL Model</li>
      <li><strong>Dataset:</strong> Fine-tuned on Danbooru2023 Dataset</li>
    </ul>
    <p>
      <strong>Description</strong>: 
    </p>
    <ul style="margin-left: 20px;">
      <li><strong>Illustrious-XL</strong> is a powerful generative model series, fine-tuned on the comprehensive Danbooru2023 dataset and its variants. It includes a wide variety of character designs, styles, and artistic knowledge derived from the dataset, making it suitable for creative and artistic AI generation tasks.</li>
      <li><strong>Illustrious-XL-v0.1</strong> is untuned BASE model, which works as possible base for all future model variants. LoRAs / Adapters can be trained on this model, ensuring future usecases. The model is research-only purpose, as not tuned for aesthetics / preferences.</li>
      <li><strong>Illustrious-XL-v0.1-GUIDED</strong> is minimally safety controlled model, which works as better option for usual usecases.</li>
    </ul>
    We plan to release several aesthetic-finetuned model variants in near future.  
    <p>
      <strong>Technical Details:</strong>
    </p>
    <ul style="margin-left: 20px;">
        <li> <a href="https://arxiv.org/abs/2409.19946" target="_blank">https://arxiv.org/abs/2409.19946</a> </li>
    </ul>
    <p>
      <strong>Terms and Conditions:</strong>
    </p>
    <ul style="margin-left: 20px;">
      <li>We recommend to use official repositories, to prevent malicious attacks.</li>
      <li>Users must agree with LICENSE to use the model. As mentioned in LICENSE, we do NOT take any actions about generated results or possible variants.</li>
      <li> <strong>As mentioned in LICENSE, users must NOT use the generated result for any prohibited purposes, including but not limited to:</strong></li>
      <ul style="margin-left: 20px;">
        <li><strong>Harmful or malicious activities</strong>: This includes harassment, threats, spreading misinformation, or any use intended to harm individuals or groups.</li>
        <li><strong>Illegal activities</strong>: Using generated content to violate any applicable laws or regulations.</li>
        <li><strong>Unethical, offensive content generation</strong>: Generating offensive, defamatory, or controversial content that violates ethical guidelines.</li>
      </ul>
    </ul>
    By using this model, users agree to comply with the conditions outlined in the LICENSE and acknowledge responsibility for how they utilize the generated content.
    <p>
      <strong>Safety Control Recommendation:</strong>
    </p>
    <ul style="margin-left: 20px;">
      <li>Generative models can occasionally produce unintended or harmful outputs.</li>
      <li>To minimize this risk, it is strongly recommended to use the GUIDED model variant, which incorporates additional safety mechanisms for responsible content generation.</li>
      <li>By choosing this variant, users can significantly reduce the likelihood of generating harmful or unintended content.</li>
      <li>We plan to update GUIDED model variants and its methodologies, with extensive research.</li>
    </ul>
    <p>
      <strong>Training/Merging Policy:</strong><br>
      You may fine-tune, merge, or train LoRA based on this model. However, to foster an open-source community, you are required to:
    </p>
    <ul style="margin-left: 20px;">
      <li>Openly share details of any derived models, including references to the original model licensed under the fair-ai-public-license.</li>
      <li>Provide information on datasets and "merge recipes" used for fine-tuning or training.</li>
      <li>Adhere to the <strong>fair-ai-public-license</strong>, ensuring that any derivative works are also open source.</li>
    </ul>
    <p>
      <strong>Uploading / Generation Policy:</strong><br>
      We do not restrict any upload or spread of the generation results, as we do not own any rights regard to generated materials. This includes 'personally trained models / finetuned models / trained lora-related results'. However, we kindly ask you to open the generation details, to foster the open source communities and researches.
    </p>
    <p>
      <strong>Monetization Prohibition:</strong>
      <ul style="margin-left: 20px;">
        <li>You are prohibited from monetizing any <strong>close-sourced fine-tuned / merged model, which disallows the public from accessing the model's source code / weights and its usages.</strong></li>
        <li>As per the license, you must openly publish any derivative models and variants. This model is intended for open-source use, and all derivatives must follow the same principles.</li>
      </ul>
    </p>
    <p>
      <strong>Usage:</strong><br>
      We do not recommend overusing critical composition tags such as 'close-up', 'upside-down', or 'cowboy shot', as they can be conflicting and lead to confusion, affecting model results.<br>
      Recommended sampling method: Euler a, Sampling Steps: 20–28, CFG: 5–7.5 (may vary based on use case).<br>
      We suggest using suitable composition tags like "upper body," "cowboy shot," "portrait," or "full body" depending on your use case.<br>
      The model supports quality tags such as: "worst quality," "bad quality," "average quality," "good quality," "best quality," and "masterpiece (quality)."<br>
      Note: The model does not have any default style. This is intended behavior for the base model.
    </p>
    <div class="last-image-container">
      <img src="https://cdn-uploads.huggingface.co/production/uploads/651d27e3a00c49c5e50c0653/RiStls1S26meeu8UV8wKj.png" alt="s23">
      <p><strong>Prompt:</strong><br>
        1boy, holding knife, blue eyes, jewelry, jacket, shirt, open mouth, hand up, simple background, hair between eyes, vest, knife, tongue, holding weapon, grey vest, upper body, necktie, solo, looking at viewer, smile, pink blood, weapon, dagger, open clothes, collared shirt, blood on face, tongue out, blonde hair, holding dagger, red necktie, white shirt, blood, short hair, holding, earrings, long sleeves, black jacket, dark theme
      </p>
      <p><strong>Negative Prompt:</strong><br>
        worst quality, comic, multiple views, bad quality, low quality, lowres, displeasing, very displeasing, bad anatomy, bad hands, scan artifacts, monochrome, greyscale, signature, twitter username, jpeg artifacts, 2koma, 4koma, guro, extra digits, fewer digits
      </p>
      <img src="https://cdn-uploads.huggingface.co/production/uploads/63398de08f27255b6b50081a/2QgPFOXbu0W6XjAMvLryY.png" alt="s24">
      <p><strong>Prompt:</strong><br>
        1girl, extremely dark, black theme, silhouette, rim lighting, black, looking at viewer, low contrast, masterpiece
      </p>
      <p><strong>Negative Prompt:</strong><br>
        worst quality, comic, multiple views, bad quality, low quality, lowres, displeasing, very displeasing, bad anatomy, bad hands, scan artifacts, monochrome, greyscale, twitter username, jpeg artifacts, 2koma, 4koma, guro, extra digits, fewer digits, jaggy lines, unclear
      </p>
    </div>

  </div>
</body>

