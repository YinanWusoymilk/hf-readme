---
license: wtfpl
pipeline_tag: text-to-image
tags:
- Civitai
- mirror
- stable diffusion
---

# A mirror of anything interesting on civitai or elsewhere on the web.

This repo is *mostly* organized around the structure 
that's necessary to import the entire repo into an 
automatic1111 install. This is because models were originally
uploaded directly from such an install via google drive in 
a colab session.

Currently I'm uploading files via my new space over at 
https://hf.co/anonderpling/repo_uploader, however I expect 
to go back to a real file system and git uploads soon, 
hopefully paperspace can help with that.

## Workflow

My workflow for downloading files into paperspace gradient 
is to download the entire repo *without* pulling LFS 
files, do a sparse checkout, and then pull the files I 
want with LFS --include (slow) or aria2 (fast). This 
workflow should work with colab, too. Whether you use 
colab or paperspace, you'll probably need the latest 
version of git to use `sparse-checkout --add`.

## How to upload and download files

<details>
<summary>sparse checkout with git, bypassing LFS, download with aria2c</summary>

```bash
!GIT_LFS_SPARSE_CHECKOUT=1 git clone git@hf.co:anonderpling/civitai_mirror # this is my command so I can push changes, you'll need to use the https://hf.co/ instead of git@hf.co:
!cd civitai_mirror
!git sparse-checkout set embeddings # embeddings are small, so it's easy enough to just pull all of them
!git sparse-checkout add models/VAE # there's only a few VAEs, and they're generally needed, so grab all those too...
!git sparse-checkout add models/Stable-diffusion/illuminati* models/Stable-diffusion/revAnimated* # add some stable diffusion models I intend to work with in this session
!apt install aria2 # make sure aria2c is installed
# let's break the following command down into parts, since there's multiple commands on one line
# find models embeddings --type f --size -2 # find files in models and embeddings directories smaller than 2 kilobytes (these are the lfs pointers that were checked out)
#   | while read a; do #lets build an aria2c input file
#        echo "https://huggingface.co/anonderpling/civitai_mirror/resolve/main/${a}"; # tell aria2c where to find the file
#        echo "        out=${a}"; # tell aria2c where to place said file
#        rm "${a}"; remove the existing file, because I'm too lazy to look up the option to have aria2c overwrite it (plus if you stop in the middle, you can tell at a glance what else is needed)
#   done | tee aria2.in.txt # end the loop, but watch to make sure theres nothing accidentally included by wildcards that shouldnt have been...downloads could take a while (and fill the disk) if I accidentally put a space before the *
# aria2 -x16 --split=16 -i aria2.in.txt # download all the files as fast as possible
!find models embeddings --type f --size -2 | while read a; do echo "https://huggingface.co/anonderpling/civitai_mirror/resolve/main/${a}"; echo "        out=${a}"; rm "${a}"; done | tee aria2.in.txt
!aria2 -x16 --split=16 -i aria2.in.txt 
```
</details>

#### Uploading files:

- [repo uploader](https://anonderpling-repo-uploader.hf.space), for single files. requires write permission to repo.
- [Civitai model uploader](https://mirroring-upload-civitai-model.hf.space), for uploading a model from Civitai. can create PR. intended for uploading model previews and civitai's API response json as well as the model, for use by Civitai unofficial extension.

</details>

<details>
<summary>to upload more files via git</summary>

```bash
# enable the git lfs filters
!pip install huggingface_hub
!huggingface-cli lfs_enable_largefiles . 
# yup, not telling. I'm an *anonymous* derpling, after all
!git config --local user.name 'not telling' 
# really couldnt care less if this is accurate...maybe I'll start randomizing it...
!git config --local user.email 'anonderpling@users.noreply.huggingface.co' 
# create an rsa key with no password
!ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_hf.co -P '' 
# a clickable link in jupyter/colab/paperspace
print('https://hf.co/settings/keys') 
# give the public key so it can be easily copied to huggingface
!cat ~/.ssh/id_hf.co.pub 
# track files 1mb+ with lfs manually (huggingface filter deals with models automatically, but large previews will give you errors)
!find -type f -size +999k -not \( -name '*.safetensors' -o -name '*.ckpt' -o -name '*.pt' \) -exec git lfs track '{}' +
# IMPORTANT: make sure you add the git ssh key above before uploading
!sleep 1m # gives you time to do so
# upload your files now. do make sure you dont upload files that didnt download properly (interrupted aria2c, lfs pointers, etc)
!git add .gitattributes models embeddings
!git commit -m "add a message..."
!git push
```
</details>

<details>
<summary>to upload a single file via huggingface_hub:</summary>

```python
inurl=api.upload_folder( # https://huggingface.co/docs/huggingface_hub/v0.14.1/en/package_reference/hf_api#huggingface_hub.HfApi.upload_folder
  token="hf_token", # only needed if you didn't already use huggingface_hub.login() previously.
  path_or_fileobj="/content/stable-diffusion-webui/models/Stable-diffusion/Rev-Animated.safetensors", # location of the file you want to upload
  path_in_repo="models/Stable-diffusion/Rev-Animated.safetensors",
  repo_id="mirroring/civitai_mirror",
  commit_message="Uploading Rev Animated", # optional.
  commit_description="I want to upload Rev Animated because it's a special file for me.\nPlease accept my PR. I don't want to host it on my own HF repo!" # optional. Required (here) for PRs.
  create_pr=True # optional. needed if you're not a special person allowed to add new files to the repo (ie, if you just want us to mirror something; make sure to fill out the description/message above, as well)
)
print("Uploaded files. Check them out at "+inurl)  
```
</details>

<details>
<summary>to upload multiple files via huggingface_hub:</summary>
  
```python
inurl=api.upload_folder( # https://huggingface.co/docs/huggingface_hub/v0.14.1/en/package_reference/hf_api#huggingface_hub.HfApi.upload_folder
  token="hf_token", # only needed if you didn't already use huggingface_hub.login() previously.
  folder_path="/stable-diffusion-webui/models/",
  path_in_repo="models",
  repo_id="mirroring/civitai_mirror",
  allow_patterns="*.safetensors", # optional. Only upload certain files.
  ignore_patterns=["*.tmp","tmp/*","*.jpg"], # optional. Ignore certain files.
  commit_message="Uploading my own models",
  commit_description="I want to upload these models because..."
  create_pr=True # needed if you're not a special person allowed to add new files to the repo (ie, if you just want us to mirror something)
)
print("Uploaded files. Check them out at "+inurl)  
```
</details>

#### Using paperspace: It's extremely important to remove the ssh key from your HF repo after you're done with it. this ensures that nobody else can access your account.

Paperspace makes free notebooks public, and I'm not sure 
if that includes filesystem access or outputs; if someone 
can access that ssh key and you didnt remove the access it 
generates, you've given them thr ability to make changes 
to your repo! This means they could delete *everything*. 
If you're technically inclined, you can possibly use the 
paperspace secrets configuration to hide such information 
(I'm not sure how it works yet)

Alternatively, you can add big files via 
https://hf.co/anonderpling/repo_uploader before your 
session (the renamed file part is pretty much added for 
uploading from HF urls, but also works for adding preview 
images), and manually upload the civitai.info files 
locally (these are just simple civitai api responses 
afaik)


## TODO:

1. finish moving files around (figure out a way to do so without 2 commits per file (one to copy, one to delete file) without downloading every single file
2. move sfw models into a subdirectory
3. consider moving locons to their own directory in models, now that I'm using paperspace...
- Perpetual: keep an eye on civitai update notifications

## License

I like WTFPL. That means anything generated by @anonderpling is licensed WTFPL. That means pretty much only this readme and a couple scripts, since everything else is someone else's work.

Other files? You'll have to find their official sources to find their licenses. The licenses for the civitai uploads *might* be in the .civitai.info files, which are standard json as returned by the civitai API.