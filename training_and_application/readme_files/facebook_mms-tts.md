---
license: cc-by-nc-4.0
inference: false
tags:
- mms
- vits
pipeline_tag: text-to-speech
---

# Massively Multilingual Speech (MMS) : Text-to-Speech Models

This repository contains a collection of text-to-speech (TTS) models, offering support for over 1000 languages. These models are part of Facebook's [Massively Multilingual Speech](https://arxiv.org/abs/2305.13516) project, aiming to provide speech technology across a diverse range of languages.  

## Table Of Contents

- [Usage](#usage)
- [Supported Languages](#supported-languages)
- [Model details](#model-details)
- [Additional links](#additional-links)
  
## Usage 
For detailed instructions on utilizing the models, please refer to the [fairseq docs](https://github.com/facebookresearch/fairseq/blob/main/examples/mms/README.md#tts-1). Additionally, you can explore the models on [MMS Space](https://huggingface.co/spaces/facebook/MMS) available on HuggingFace.

*models* folder consists of only generator, which is enough to run TTS inference. Full model checkpoint which also includes the discriminator and the optimizer states can be found in *full_models* folder. The models can be downloaded locally using *[hf_hub_download](https://huggingface.co/docs/huggingface_hub/guides/download)* API.

See [this section](https://github.com/facebookresearch/fairseq/blob/main/examples/mms/README.md#tts-1) for instructions on using the models for inference. 

## Supported Languages

This model supports 1107 languages. Unclick the following to toogle all supported languages of this checkpoint in [ISO 639-3 code](https://en.wikipedia.org/wiki/ISO_639-3).
You can find more details about the languages and their ISO 639-3 codes in the [MMS Language Coverage Overview](https://dl.fbaipublicfiles.com/mms/misc/language_coverage_mms.html).
<details>
  <summary>Click to toggle</summary>

 - abi
 - ace
 - aca
 - acn
 - acr
 - ach
 - acu
 - guq
 - ade
 - adj
 - agd
 - agx
 - agn
 - aha
 - aka
 - knj
 - ake
 - aeu
 - ahk
 - bss
 - alj
 - sqi
 - alt
 - alp
 - alz
 - kab
 - amk
 - mmg
 - amh
 - ami
 - azg
 - agg
 - boj
 - cko
 - any
 - arl
 - ara
 - atq
 - luc
 - hyw
 - apr
 - aia
 - msy
 - cni
 - cjo
 - cpu
 - cpb
 - asm
 - asa
 - teo
 - ati
 - djk
 - ava
 - avn
 - avu
 - awb
 - kwi
 - awa
 - agr
 - agu
 - ayr
 - ayo
 - abp
 - blx
 - sgb
 - azj-script_cyrillic
 - azj-script_latin
 - azb
 - bba
 - bhz
 - bvc
 - bfy
 - bgq
 - bdq
 - bdh
 - bqi
 - bjw
 - blz
 - ban
 - bcc-script_latin
 - bcc-script_arabic
 - bam
 - ptu
 - bcw
 - bqj
 - bno
 - bbb
 - bfa
 - bjz
 - bak
 - eus
 - bsq
 - akb
 - btd
 - btx
 - bts
 - bbc
 - bvz
 - bjv
 - bep
 - bkv
 - bzj
 - bem
 - bng
 - ben
 - bom
 - btt
 - bha
 - bgw
 - bht
 - beh
 - sne
 - ubl
 - bcl
 - bim
 - bkd
 - bjr
 - bfo
 - biv
 - bib
 - bis
 - bzi
 - bqp
 - bpr
 - bps
 - bwq
 - bdv
 - bqc
 - bus
 - bnp
 - bmq
 - bdg
 - boa
 - ksr
 - bor
 - bru
 - box
 - bzh
 - bgt
 - sab
 - bul
 - bwu
 - bmv
 - mya
 - tte
 - cjp
 - cbv
 - kaq
 - cot
 - cbc
 - car
 - cat
 - ceb
 - cme
 - cbi
 - ceg
 - cly
 - cya
 - che
 - hne
 - nya
 - dig
 - dug
 - bgr
 - cek
 - cfm
 - cnh
 - hlt
 - mwq
 - ctd
 - tcz
 - zyp
 - cco
 - cnl
 - cle
 - chz
 - cpa
 - cso
 - cnt
 - cuc
 - hak
 - nan
 - xnj
 - cap
 - cax
 - ctg
 - ctu
 - chf
 - cce
 - crt
 - crq
 - cac-dialect_sansebastiáncoatán
 - cac-dialect_sanmateoixtatán
 - ckt
 - ncu
 - cdj
 - chv
 - caa
 - asg
 - con
 - crn
 - cok
 - crk-script_latin
 - crk-script_syllabics
 - crh
 - cui
 - dsh
 - dbq
 - dga
 - dgi
 - dgk
 - dnj-dialect_gweetaawueast
 - dnj-dialect_blowowest
 - daa
 - dnt
 - dnw
 - dar
 - tcc
 - dwr
 - ded
 - mzw
 - ntr
 - ddn
 - des
 - dso
 - nfa
 - dhi
 - gud
 - did
 - mhu
 - dip
 - dik
 - tbz
 - dts
 - dos
 - dgo
 - mvp
 - nld
 - jen
 - dzo
 - idd
 - eka
 - cto
 - emp
 - eng
 - enx
 - sja
 - myv
 - mcq
 - ese
 - evn
 - eza
 - fal
 - fao
 - far
 - fij
 - fin
 - fon
 - frd
 - fra
 - ful
 - flr
 - gau
 - gbk
 - gag-script_cyrillic
 - gag-script_latin
 - gbi
 - gmv
 - lug
 - pwg
 - gbm
 - cab
 - grt
 - krs
 - gso
 - nlg
 - gej
 - deu
 - gri
 - kik
 - acd
 - glk
 - gof-script_latin
 - gog
 - gkn
 - wsg
 - gjn
 - gqr
 - gor
 - gux
 - gbo
 - ell
 - grc
 - guh
 - gub
 - grn
 - gyr
 - guo
 - gde
 - guj
 - gvl
 - guk
 - rub
 - dah
 - gwr
 - gwi
 - hat
 - hlb
 - amf
 - hag
 - hnn
 - bgc
 - had
 - hau
 - hwc
 - hvn
 - hay
 - xed
 - heb
 - heh
 - hil
 - hin
 - hif
 - hns
 - hoc
 - hoy
 - hus-dialect_westernpotosino
 - hus-dialect_centralveracruz
 - huv
 - hui
 - hun
 - hap
 - iba
 - isl
 - dbj
 - ifa
 - ifb
 - ifu
 - ifk
 - ife
 - ign
 - ikk
 - iqw
 - ilb
 - ilo
 - imo
 - ind
 - inb
 - ipi
 - irk
 - icr
 - itv
 - itl
 - atg
 - ixl-dialect_sanjuancotzal
 - ixl-dialect_sangasparchajul
 - ixl-dialect_santamarianebaj
 - nca
 - izr
 - izz
 - jac
 - jam
 - jav
 - jvn
 - kac
 - dyo
 - csk
 - adh
 - jun
 - jbu
 - dyu
 - bex
 - juy
 - gna
 - urb
 - kbp
 - cwa
 - dtp
 - kbr
 - cgc
 - kki
 - kzf
 - lew
 - cbr
 - kkj
 - keo
 - kqe
 - kak
 - kyb
 - knb
 - kmd
 - kml
 - ify
 - xal
 - kbq
 - kay
 - ktb
 - hig
 - gam
 - cbu
 - xnr
 - kmu
 - kne
 - kan
 - kby
 - pam
 - cak-dialect_santamaríadejesús
 - cak-dialect_southcentral
 - cak-dialect_yepocapa
 - cak-dialect_western
 - cak-dialect_santodomingoxenacoj
 - cak-dialect_central
 - xrb
 - krc
 - kaa
 - krl
 - pww
 - xsm
 - cbs
 - pss
 - kxf
 - kyz
 - kyu
 - txu
 - kaz
 - ndp
 - kbo
 - kyq
 - ken
 - ker
 - xte
 - kyg
 - kjh
 - kca
 - khm
 - kxm
 - kjg
 - nyf
 - kij
 - kia
 - kqr
 - kqp
 - krj
 - zga
 - kin
 - pkb
 - geb
 - gil
 - kje
 - kss
 - thk
 - klu
 - kyo
 - kog
 - kfb
 - kpv
 - bbo
 - xon
 - kma
 - kno
 - kxc
 - ozm
 - kqy
 - kor
 - coe
 - kpq
 - kpy
 - kyf
 - kff-script_telugu
 - kri
 - rop
 - ktj
 - ted
 - krr
 - kdt
 - kez
 - cul
 - kle
 - kdi
 - kue
 - kum
 - kvn
 - cuk
 - kdn
 - xuo
 - key
 - kpz
 - knk
 - kmr-script_latin
 - kmr-script_arabic
 - kmr-script_cyrillic
 - xua
 - kru
 - kus
 - kub
 - kdc
 - kxv
 - blh
 - cwt
 - kwd
 - tnk
 - kwf
 - cwe
 - kyc
 - tye
 - kir
 - quc-dialect_north
 - quc-dialect_east
 - quc-dialect_central
 - lac
 - lsi
 - lbj
 - lhu
 - las
 - lam
 - lns
 - ljp
 - laj
 - lao
 - lat
 - lav
 - law
 - lcp
 - lzz
 - lln
 - lef
 - acf
 - lww
 - mhx
 - eip
 - lia
 - lif
 - onb
 - lis
 - loq
 - lob
 - yaz
 - lok
 - llg
 - ycl
 - lom
 - ngl
 - lon
 - lex
 - lgg
 - ruf
 - dop
 - lnd
 - ndy
 - lwo
 - lee
 - mev
 - mfz
 - jmc
 - myy
 - mbc
 - mda
 - mad
 - mag
 - ayz
 - mai
 - mca
 - mcp
 - mak
 - vmw
 - mgh
 - kde
 - mlg
 - zlm
 - pse
 - mkn
 - xmm
 - mal
 - xdy
 - div
 - mdy
 - mup
 - mam-dialect_central
 - mam-dialect_northern
 - mam-dialect_southern
 - mam-dialect_western
 - mqj
 - mcu
 - mzk
 - maw
 - mjl
 - mnk
 - mge
 - mbh
 - knf
 - mjv
 - mbt
 - obo
 - mbb
 - mzj
 - sjm
 - mrw
 - mar
 - mpg
 - mhr
 - enb
 - mah
 - myx
 - klv
 - mfh
 - met
 - mcb
 - mop
 - yua
 - mfy
 - maz
 - vmy
 - maq
 - mzi
 - maj
 - maa-dialect_sanantonio
 - maa-dialect_sanjerónimo
 - mhy
 - mhi
 - zmz
 - myb
 - gai
 - mqb
 - mbu
 - med
 - men
 - mee
 - mwv
 - meq
 - zim
 - mgo
 - mej
 - mpp
 - min
 - gum
 - mpx
 - mco
 - mxq
 - pxm
 - mto
 - mim
 - xta
 - mbz
 - mip
 - mib
 - miy
 - mih
 - miz
 - xtd
 - mxt
 - xtm
 - mxv
 - xtn
 - mie
 - mil
 - mio
 - mdv
 - mza
 - mit
 - mxb
 - mpm
 - soy
 - cmo-script_latin
 - cmo-script_khmer
 - mfq
 - old
 - mfk
 - mif
 - mkl
 - mox
 - myl
 - mqf
 - mnw
 - mon
 - mog
 - mfe
 - mor
 - mqn
 - mgd
 - mtj
 - cmr
 - mtd
 - bmr
 - moz
 - mzm
 - mnb
 - mnf
 - unr
 - fmu
 - mur
 - tih
 - muv
 - muy
 - sur
 - moa
 - wmw
 - tnr
 - miq
 - mos
 - muh
 - nas
 - mbj
 - nfr
 - kfw
 - nst
 - nag
 - nch
 - nhe
 - ngu
 - azz
 - nhx
 - ncl
 - nhy
 - ncj
 - nsu
 - npl
 - nuz
 - nhw
 - nhi
 - nlc
 - nab
 - gld
 - nnb
 - npy
 - pbb
 - ntm
 - nmz
 - naw
 - nxq
 - ndj
 - ndz
 - ndv
 - new
 - nij
 - sba
 - gng
 - nga
 - nnq
 - ngp
 - gym
 - kdj
 - nia
 - nim
 - nin
 - nko
 - nog
 - lem
 - not
 - nhu
 - bud
 - nus
 - yas
 - nnw
 - nwb
 - nyy
 - nyn
 - rim
 - lid
 - nuj
 - nyo
 - nzi
 - ann
 - ory
 - ojb-script_latin
 - ojb-script_syllabics
 - oku
 - bsc
 - bdu
 - orm
 - ury
 - oss
 - ote
 - otq
 - stn
 - sig
 - kfx
 - bfz
 - sey
 - pao
 - pau
 - pce
 - plw
 - pmf
 - pag
 - pap
 - prf
 - pab
 - pbi
 - pbc
 - pad
 - ata
 - pez
 - peg
 - fas
 - pcm
 - pis
 - pny
 - pir
 - pjt
 - poy
 - pol
 - pps
 - pls
 - poi
 - poh-dialect_eastern
 - poh-dialect_western
 - por
 - prt
 - pui
 - pan
 - tsz
 - suv
 - lme
 - quy
 - qvc
 - quz
 - qve
 - qub
 - qvh
 - qwh
 - qvw
 - quf
 - qvm
 - qul
 - qvn
 - qxn
 - qxh
 - qvs
 - quh
 - qxo
 - qxr
 - qvo
 - qvz
 - qxl
 - quw
 - kjb
 - kek
 - rah
 - rjs
 - rai
 - lje
 - rnl
 - rkt
 - rap
 - yea
 - raw
 - rej
 - rel
 - ril
 - iri
 - rgu
 - rhg
 - rmc-script_latin
 - rmc-script_cyrillic
 - rmo
 - rmy-script_latin
 - rmy-script_cyrillic
 - ron
 - rol
 - cla
 - rng
 - rug
 - run
 - rus
 - lsm
 - spy
 - sck
 - saj
 - sch
 - sml
 - xsb
 - sbl
 - saq
 - sbd
 - smo
 - rav
 - sxn
 - sag
 - sbp
 - xsu
 - srm
 - sas
 - apb
 - sgw
 - tvw
 - lip
 - slu
 - snw
 - sea
 - sza
 - seh
 - crs
 - ksb
 - shn
 - sho
 - mcd
 - cbt
 - xsr
 - shk
 - shp
 - sna
 - cjs
 - jiv
 - snp
 - sya
 - sid
 - snn
 - sri
 - srx
 - sil
 - sld
 - akp
 - xog
 - som
 - bmu
 - khq
 - ses
 - mnx
 - spa
 - srn
 - sxb
 - suc
 - tgo
 - suk
 - sun
 - suz
 - sgj
 - sus
 - swh
 - swe
 - syl
 - dyi
 - myk
 - spp
 - tap
 - tby
 - tna
 - shi
 - klw
 - tgl
 - tbk
 - tgj
 - blt
 - tbg
 - omw
 - tgk
 - tdj
 - tbc
 - tlj
 - tly
 - ttq-script_tifinagh
 - taj
 - taq
 - tam
 - tpm
 - tgp
 - tnn
 - tac
 - rif-script_latin
 - rif-script_arabic
 - tat
 - tav
 - twb
 - tbl
 - kps
 - twe
 - ttc
 - tel
 - kdh
 - tes
 - tex
 - tee
 - tpp
 - tpt
 - stp
 - tfr
 - twu
 - ter
 - tew
 - tha
 - nod
 - thl
 - tem
 - adx
 - bod
 - khg
 - tca
 - tir
 - txq
 - tik
 - dgr
 - tob
 - tmf
 - tng
 - tlb
 - ood
 - tpi
 - jic
 - lbw
 - txa
 - tom
 - toh
 - tnt
 - sda
 - tcs
 - toc
 - tos
 - neb
 - trn
 - trs
 - trc
 - tri
 - cof
 - tkr
 - kdl
 - cas
 - tso
 - tuo
 - iou
 - tmc
 - tuf
 - tur
 - tuk-script_latin
 - tuk-script_arabic
 - bov
 - tue
 - kcg
 - tzh-dialect_bachajón
 - tzh-dialect_tenejapa
 - tzo-dialect_chenalhó
 - tzo-dialect_chamula
 - tzj-dialect_western
 - tzj-dialect_eastern
 - aoz
 - udm
 - udu
 - ukr
 - ppk
 - ubu
 - urk
 - ura
 - urt
 - urd-script_devanagari
 - urd-script_arabic
 - urd-script_latin
 - upv
 - usp
 - uig-script_arabic
 - uig-script_cyrillic
 - uzb-script_cyrillic
 - vag
 - bav
 - vid
 - vie
 - vif
 - vun
 - vut
 - prk
 - wwa
 - rro
 - bao
 - waw
 - lgl
 - wlx
 - cou
 - hub
 - gvc
 - mfi
 - wap
 - wba
 - war
 - way
 - guc
 - cym
 - kvw
 - tnp
 - hto
 - huu
 - wal-script_latin
 - wal-script_ethiopic
 - wlo
 - noa
 - wob
 - kao
 - xer
 - yad
 - yka
 - sah
 - yba
 - yli
 - nlk
 - yal
 - yam
 - yat
 - jmd
 - tao
 - yaa
 - ame
 - guu
 - yao
 - yre
 - yva
 - ybb
 - pib
 - byr
 - pil
 - yor
 - ycn
 - ess
 - yuz
 - atb
 - zne
 - zaq
 - zpo
 - zad
 - zpc
 - zca
 - zpg
 - zai
 - zpl
 - zam
 - zaw
 - zpm
 - zac
 - zao
 - ztq
 - zar
 - zpt
 - zpi
 - zas
 - zaa
 - zpz
 - zab
 - zpu
 - zae
 - zty
 - zav
 - zza
 - zyb
 - ziw
 - zos
 - gnd
 - ewe

</details>

## Model details

- **Developed by:** Vineel Pratap et al.
- **Model type:** Text-to-speech model
- **Language(s):** 1107 languages, see [supported languages](#supported-languages)
- **License:** CC-BY-NC 4.0 license
- **Cite as:**

      @article{pratap2023mms,
        title={Scaling Speech Technology to 1,000+ Languages},
        author={Vineel Pratap and Andros Tjandra and Bowen Shi and Paden Tomasello and Arun Babu and Sayani Kundu and Ali Elkahky and Zhaoheng Ni and Apoorv Vyas and Maryam Fazel-Zarandi and Alexei Baevski and Yossi Adi and Xiaohui Zhang and Wei-Ning Hsu and Alexis Conneau and Michael Auli},
      journal={arXiv},
      year={2023}
      }

## Additional Links

- [Blog post](https://ai.facebook.com/blog/multilingual-model-speech-recognition/)
- [Transformers documentation](https://huggingface.co/docs/transformers/main/en/model_doc/mms).
- [Paper](https://arxiv.org/abs/2305.13516)
- [GitHub Repository](https://github.com/facebookresearch/fairseq/tree/main/examples/mms#asr)
- [Other **MMS** checkpoints](https://huggingface.co/models?other=mms)
- MMS base checkpoints:
  - [facebook/mms-1b](https://huggingface.co/facebook/mms-1b)
  - [facebook/mms-300m](https://huggingface.co/facebook/mms-300m)
- [Official Space](https://huggingface.co/spaces/facebook/MMS)