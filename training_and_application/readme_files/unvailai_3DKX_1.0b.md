---
model:
  base_learning_rate: 1.0e-04
  target: ldm.models.diffusion.ddpm.LatentDiffusion
  params:
    linear_start: 0.00085
    linear_end: 0.0120
    num_timesteps_cond: 1
    log_every_t: 200
    timesteps: 1000
    first_stage_key: "jpg"
    cond_stage_key: "txt"
    image_size: 64
    channels: 4
    cond_stage_trainable: false   # Note: different from the one we trained before
    conditioning_key: crossattn
    monitor: val/loss_simple_ema
    scale_factor: 0.18215
    use_ema: False

    scheduler_config: # 10000 warmup steps
      target: ldm.lr_scheduler.LambdaLinearScheduler
      params:
        warm_up_steps: [ 10000 ]
        cycle_lengths: [ 10000000000000 ] # incredibly large number to prevent corner cases
        f_start: [ 1.e-6 ]
        f_max: [ 1. ]
        f_min: [ 1. ]

    unet_config:
      target: ldm.modules.diffusionmodules.openaimodel.UNetModel
      params:
        image_size: 32 # unused
        in_channels: 4
        out_channels: 4
        model_channels: 320
        attention_resolutions: [ 4, 2, 1 ]
        num_res_blocks: 2
        channel_mult: [ 1, 2, 4, 4 ]
        num_heads: 8
        use_spatial_transformer: True
        transformer_depth: 1
        context_dim: 768
        use_checkpoint: True
        legacy: False

    first_stage_config:
      target: ldm.models.autoencoder.AutoencoderKL
      params:
        embed_dim: 4
        monitor: val/rec_loss
        ddconfig:
          double_z: true
          z_channels: 4
          resolution: 256
          in_channels: 3
          out_ch: 3
          ch: 128
          ch_mult:
          - 1
          - 2
          - 4
          - 4
          num_res_blocks: 2
          attn_resolutions: []
          dropout: 0.0
        lossconfig:
          target: torch.nn.Identity

    cond_stage_config:
      target: ldm.modules.encoders.modules.FrozenCLIPEmbedder
---
<a href="https://discord.gg/unvailai">
  <img src="https://cdn.discordapp.com/attachments/1051410188592226364/1061335270194171944/havo_aloe_banner_copie.jpg" alt="image description" width="768">
</a>
<a href="https://www.patreon.com/unvailai">
  <img src="https://cdn.discordapp.com/attachments/1051410188592226364/1061335270483566662/havo_aloe_banner_patreon.jpg" alt="image description" width="768">
</a>



Model name: H&A 3DKX
Model versions: 1.0b, 1.1(latest)

## Changelog:
V1.1: Minor update based on feedback, containing the following fixes:

-“nsfw”, “nudity” , and “erotica” have been trained into the model and work as Negatives to greatly reduce unintended NSFW content.

- CFG can be pushed a bit higher before the images become burnt. As a result, the model can accommodate more complicated prompts now.

- Oversaturated images will be encountered way less often

## Description: 

SFW model with limited nsfw capabilities (suggestive nsfw) that is highly versatile for 3D renders.
The model has the particularity of splitting itself into two different well balanced styles. 
If you'd like to have your 3D characters have a more "Cartoony" face, you simply start your prompt 
with "3d cartoon of", and if you want the classic 3D render style, you write "a 3d render of".

Please check the cheat sheet for prompting tips as the structure of the prompt and negatives used has a huge effect.
Note: Model has an embedded VAE, so do not add one with this model. It will be the best in most cases, and configured for higher resolutions.

## Model has an embedded VAE, do not use an extra one!
If you want to chat with us and join our community visit our discord:
https://discord.gg/CPyqJgXdRG
## Dataset:
 - between 140 and 180 pictures of 3D render of all kind

## PromptGuide/Cheat Sheet
[3DKX_1.0b/1.1 Guide](https://docs.google.com/document/d/15pJ3TkbmX3LRoSTNsMYsbetvO7A46L60wVOxIL2ZZ6E/)

## Has a high success rate at:
- sfw portraits, full body poses, close ups, etc 
- high versatility in terms of outputs, it isn't locked to perform well on portraits
- Landscapes, cyberpunk, steampunk, natural, scifi, etc
- 2B Nier Automata (Don't ask us why)
- different body types - different ethnicity
- nsfw portraits, full body poses, close ups, etc 

## What it "In theory" shouldn't exceed at:
- anything outside the scope of portraits, people, landscapes, game artworks, 3D sculptures, 3D fantasy, 3D film stills, etc
- celebrities
- highly specific animated cartoon characters
- multiple subjects 
- highly specific video-game characters
- pornography, genitalia and highly explicit materials

<img width="768px" src="https://cdn.discordapp.com/attachments/1056287982363086930/1056331346177425438/00011-3928902726-A203d20render20of2020epic20portrait20close20shot20of20beautiful20turkish20woman20wearing20with20angelic20feathered20wings20gold20armour20neckline.png">
<img width="768px" src="https://cdn.discordapp.com/attachments/323893037379878912/1056823178846031882/00494-2262985444-3d_render_of_a_sharp_focused_detailed_photo_of_a_super_car_with_iridescent_metallic_color_driving_on_a_midnight_road_multicolo.png">
<img width="768px" src="https://media.discordapp.net/attachments/1056287982363086930/1056387208900268062/00102-971809704-movie_still_of_a_alien_from_mass_effect_wearing_scifi_armor_disney_pixar_animation_3d_render_4k_resolution_very_detail.png">
<img width="768px" src="https://cdn.discordapp.com/attachments/1056287982363086930/1056399456695767151/00143-556286556-3d_render_of_a_cute_simba_from_the_lion_king_disney_pixar_animation_RDR_2_game_render_lion_king_movie_still_very_detailed_4.png">
<img width="768px" src="https://media.discordapp.net/attachments/1056287982363086930/1056385527907110963/00097-3269033961-picture_of_a_handsome_viking_chief_in_his_village_disney_pixar_animation_3d_render_4k_resolution_very_detailed_movie_stil.png?width=645&height=806">
<img width="768px" src="https://cdn.discordapp.com/attachments/1056287982363086930/1056340815011659917/02082-2709311262-A_3d_render_of_a_cute_tiny_little_fluffy_monster_with_googly_eyes_running_in_a_huge_bedroom_antview_bokeh_closeup_highly_det.png">
<img width="768px" src="https://media.discordapp.net/attachments/1051410188592226364/1056636097330942022/02045-172340656-A_3d_render_of_A_mature_woman_with_short_styled_hair_and_wearing_a_colorful_printed_blouse_seated_in_a_cozy_armchair_with_a_wa.png">
<img width="768px" src="https://cdn.discordapp.com/attachments/1051410188592226364/1056636096412389508/02029-172340656-A_3d_cartoon_of_A_mature_woman_with_short_styled_hair_and_wearing_a_colorful_printed_blouse_seated_in_a_cozy_armchair_with_a.png">
<img width="768px" src="https://cdn.discordapp.com/attachments/1051410188592226364/1056636286347247616/01925-2050823061-A_woman_with_short_bobbed_hair_styled_in_a_choppy_textured_look_wearing_a_cyberpunk-inspired_outfit_with_neon_accents_and_boo.png">
<img width="768px" src="https://cdn.discordapp.com/attachments/1051410188592226364/1056636296103198740/01858-1327022461-A_slender_woman_with_pale_skin_short_blonde_hair_and_bright_blue_eyes._She_is_standing_in_a_bright_white_studio_surrounded_by.png">
<img width="768px" src="https://cdn.discordapp.com/attachments/1051410188592226364/1056636414059618406/02107-599009770-A_3d_cartoon_of_a_a_beautiful_spanish_woman_wearing_Kimono_neckline_fine_-_art_photography_cinematic_portrait_shot_8_k_mid.png">

## Use Restrictions
You agree not to use the Model or Derivatives of the Model:
- In any way that violates any applicable national, federal, state, local or international law or regulation;
- For the purpose of exploiting, harming or attempting to exploit or harm minors in any way;
- To generate or disseminate verifiably false information and/or content with the purpose of harming others;
- To generate or disseminate personal identifiable information that can be used to harm an individual;
- To defame, disparage or otherwise harass others;
- For fully automated decision making that adversely impacts an individual’s legal rights or otherwise creates or modifies a binding, enforceable obligation;
- For any use intended to or which has the effect of discriminating against or harming individuals or groups based on online or offline social behavior or known or predicted personal or personality characteristics;
- To exploit any of the vulnerabilities of a specific group of persons based on their age, social, physical or mental characteristics, in order to materially distort the behavior of a person pertaining to that group in a manner that causes or is likely to cause that person or another person physical or psychological harm;
- For any use intended to or which has the effect of discriminating against individuals or groups based on legally protected characteristics or categories;
- To provide medical advice and medical results interpretation;
- To generate or disseminate information for the purpose to be used for administration of justice, law enforcement, immigration or asylum processes, such as predicting an individual will commit fraud/crime commitment (e.g. by text profiling, drawing causal relationships between assertions made in documents, indiscriminate and arbitrarily-targeted use).
## Important notes: 
- This model’s datasets do NOT contain any character that could be remotely described as a child, or underage.
- Our datasets contains no mentions of the artist's name, nor specific styles from any artist whatsoever. 
- The creators (Havo and Aloe Vera) will not be held accountable for the way this model is being used or the outputs that any person may generate.
- The purpose of this model isn't to replicate a style, but to provide a useful tool to creators of all kinds to generate 3D related contents
- Be advised that this model can generate explicit material and therefore shouldn't be used in any way to cause harm or produce non-consensual sexual content.  

## Conclusion:

We do have limited resources, so our weeks worth of testing cannot realistically encapsulate the full potential of the model. Which is why we're very excited to discover that YOU, the awesome creators will make out of this tool. And for anyone that feels like we're worth a shot, we invite you to please have a look at our Patreon in which you can choose to chip in and support our work. 
We have many plans and we'd like to have some more resources that will allow us to work more efficiently and to eventually be able to create models of professional standards. It's our goal !
https://www.patreon.com/aloeNhavo