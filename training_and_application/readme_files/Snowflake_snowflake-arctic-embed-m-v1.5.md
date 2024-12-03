---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- mteb
- arctic
- snowflake-arctic-embed
- transformers.js
license: apache-2.0
model-index:
- name: snowflake-arctic-embed-m-v1.5
  results:
  - dataset:
      config: default
      name: MTEB ArguAna
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
      split: test
      type: mteb/arguana
    metrics:
    - type: main_score
      value: 59.53000000000001
    - type: map_at_1
      value: 34.282000000000004
    - type: map_at_10
      value: 50.613
    - type: map_at_100
      value: 51.269
    - type: map_at_1000
      value: 51.271
    - type: map_at_20
      value: 51.158
    - type: map_at_3
      value: 45.626
    - type: map_at_5
      value: 48.638
    - type: mrr_at_1
      value: 34.92176386913229
    - type: mrr_at_10
      value: 50.856081645555406
    - type: mrr_at_100
      value: 51.510739437069034
    - type: mrr_at_1000
      value: 51.51299498830165
    - type: mrr_at_20
      value: 51.39987941081724
    - type: mrr_at_3
      value: 45.993361782835514
    - type: mrr_at_5
      value: 48.88098624940742
    - type: nauc_map_at_1000_diff1
      value: 10.628675774160785
    - type: nauc_map_at_1000_max
      value: -10.11742589992339
    - type: nauc_map_at_1000_std
      value: -18.29277379812427
    - type: nauc_map_at_100_diff1
      value: 10.63250240035489
    - type: nauc_map_at_100_max
      value: -10.112078786734363
    - type: nauc_map_at_100_std
      value: -18.288524872706834
    - type: nauc_map_at_10_diff1
      value: 10.476494913081712
    - type: nauc_map_at_10_max
      value: -9.890937746734037
    - type: nauc_map_at_10_std
      value: -18.279750514750443
    - type: nauc_map_at_1_diff1
      value: 14.549204048461151
    - type: nauc_map_at_1_max
      value: -12.230560087701225
    - type: nauc_map_at_1_std
      value: -19.469903650130362
    - type: nauc_map_at_20_diff1
      value: 10.586564571825674
    - type: nauc_map_at_20_max
      value: -10.00292720526217
    - type: nauc_map_at_20_std
      value: -18.258077347878064
    - type: nauc_map_at_3_diff1
      value: 10.378663968090372
    - type: nauc_map_at_3_max
      value: -10.458896171786185
    - type: nauc_map_at_3_std
      value: -18.38852760333766
    - type: nauc_map_at_5_diff1
      value: 10.235960275925581
    - type: nauc_map_at_5_max
      value: -10.239496080409058
    - type: nauc_map_at_5_std
      value: -18.817023479445886
    - type: nauc_mrr_at_1000_diff1
      value: 8.718212649575722
    - type: nauc_mrr_at_1000_max
      value: -10.81022794038691
    - type: nauc_mrr_at_1000_std
      value: -17.87669499555167
    - type: nauc_mrr_at_100_diff1
      value: 8.722174171165133
    - type: nauc_mrr_at_100_max
      value: -10.804840985713525
    - type: nauc_mrr_at_100_std
      value: -17.872487099359986
    - type: nauc_mrr_at_10_diff1
      value: 8.609421635870238
    - type: nauc_mrr_at_10_max
      value: -10.568644717548432
    - type: nauc_mrr_at_10_std
      value: -17.872968762635814
    - type: nauc_mrr_at_1_diff1
      value: 12.69590006263834
    - type: nauc_mrr_at_1_max
      value: -12.082056561238321
    - type: nauc_mrr_at_1_std
      value: -18.036424092186657
    - type: nauc_mrr_at_20_diff1
      value: 8.684842497970315
    - type: nauc_mrr_at_20_max
      value: -10.691578914627286
    - type: nauc_mrr_at_20_std
      value: -17.84350301434992
    - type: nauc_mrr_at_3_diff1
      value: 8.649761557556763
    - type: nauc_mrr_at_3_max
      value: -11.104694428047496
    - type: nauc_mrr_at_3_std
      value: -18.149917948370344
    - type: nauc_mrr_at_5_diff1
      value: 8.433489750038396
    - type: nauc_mrr_at_5_max
      value: -10.917772454397436
    - type: nauc_mrr_at_5_std
      value: -18.4094211134111
    - type: nauc_ndcg_at_1000_diff1
      value: 10.19041067807956
    - type: nauc_ndcg_at_1000_max
      value: -9.54328201605796
    - type: nauc_ndcg_at_1000_std
      value: -17.824620427456633
    - type: nauc_ndcg_at_100_diff1
      value: 10.289491087585963
    - type: nauc_ndcg_at_100_max
      value: -9.357214331420337
    - type: nauc_ndcg_at_100_std
      value: -17.657600653632873
    - type: nauc_ndcg_at_10_diff1
      value: 9.435530877596092
    - type: nauc_ndcg_at_10_max
      value: -8.182581635383546
    - type: nauc_ndcg_at_10_std
      value: -17.603156479980388
    - type: nauc_ndcg_at_1_diff1
      value: 14.549204048461151
    - type: nauc_ndcg_at_1_max
      value: -12.230560087701225
    - type: nauc_ndcg_at_1_std
      value: -19.469903650130362
    - type: nauc_ndcg_at_20_diff1
      value: 9.885227087275197
    - type: nauc_ndcg_at_20_max
      value: -8.52362662391439
    - type: nauc_ndcg_at_20_std
      value: -17.441705436231764
    - type: nauc_ndcg_at_3_diff1
      value: 9.22542769998547
    - type: nauc_ndcg_at_3_max
      value: -9.903590564219288
    - type: nauc_ndcg_at_3_std
      value: -18.357220221111593
    - type: nauc_ndcg_at_5_diff1
      value: 8.8756720745828
    - type: nauc_ndcg_at_5_max
      value: -9.269764943861245
    - type: nauc_ndcg_at_5_std
      value: -19.009229433187784
    - type: nauc_precision_at_1000_diff1
      value: 3.733355117431035
    - type: nauc_precision_at_1000_max
      value: 3.9603571352517393
    - type: nauc_precision_at_1000_std
      value: 70.07345061131439
    - type: nauc_precision_at_100_diff1
      value: 29.019032142462457
    - type: nauc_precision_at_100_max
      value: 40.75153328286103
    - type: nauc_precision_at_100_std
      value: 62.634249549126594
    - type: nauc_precision_at_10_diff1
      value: 2.5762677254910353
    - type: nauc_precision_at_10_max
      value: 6.096298633773051
    - type: nauc_precision_at_10_std
      value: -11.507400451348587
    - type: nauc_precision_at_1_diff1
      value: 14.549204048461151
    - type: nauc_precision_at_1_max
      value: -12.230560087701225
    - type: nauc_precision_at_1_std
      value: -19.469903650130362
    - type: nauc_precision_at_20_diff1
      value: 1.715540124567996
    - type: nauc_precision_at_20_max
      value: 21.53546453945913
    - type: nauc_precision_at_20_std
      value: 1.537961142195571
    - type: nauc_precision_at_3_diff1
      value: 5.701850652555737
    - type: nauc_precision_at_3_max
      value: -8.180345365085552
    - type: nauc_precision_at_3_std
      value: -18.37033750502482
    - type: nauc_precision_at_5_diff1
      value: 3.6053552181042843
    - type: nauc_precision_at_5_max
      value: -5.207647070615612
    - type: nauc_precision_at_5_std
      value: -19.89491085427258
    - type: nauc_recall_at_1000_diff1
      value: 3.733355117431255
    - type: nauc_recall_at_1000_max
      value: 3.9603571352482194
    - type: nauc_recall_at_1000_std
      value: 70.07345061131205
    - type: nauc_recall_at_100_diff1
      value: 29.01903214246288
    - type: nauc_recall_at_100_max
      value: 40.7515332828621
    - type: nauc_recall_at_100_std
      value: 62.63424954912607
    - type: nauc_recall_at_10_diff1
      value: 2.5762677254911988
    - type: nauc_recall_at_10_max
      value: 6.0962986337729905
    - type: nauc_recall_at_10_std
      value: -11.507400451348577
    - type: nauc_recall_at_1_diff1
      value: 14.549204048461151
    - type: nauc_recall_at_1_max
      value: -12.230560087701225
    - type: nauc_recall_at_1_std
      value: -19.469903650130362
    - type: nauc_recall_at_20_diff1
      value: 1.7155401245682675
    - type: nauc_recall_at_20_max
      value: 21.535464539459632
    - type: nauc_recall_at_20_std
      value: 1.5379611421957025
    - type: nauc_recall_at_3_diff1
      value: 5.7018506525557875
    - type: nauc_recall_at_3_max
      value: -8.180345365085538
    - type: nauc_recall_at_3_std
      value: -18.370337505024796
    - type: nauc_recall_at_5_diff1
      value: 3.6053552181043913
    - type: nauc_recall_at_5_max
      value: -5.207647070615579
    - type: nauc_recall_at_5_std
      value: -19.894910854272492
    - type: ndcg_at_1
      value: 34.282000000000004
    - type: ndcg_at_10
      value: 59.53000000000001
    - type: ndcg_at_100
      value: 62.187000000000005
    - type: ndcg_at_1000
      value: 62.243
    - type: ndcg_at_20
      value: 61.451
    - type: ndcg_at_3
      value: 49.393
    - type: ndcg_at_5
      value: 54.771
    - type: precision_at_1
      value: 34.282000000000004
    - type: precision_at_10
      value: 8.791
    - type: precision_at_100
      value: 0.992
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.769
    - type: precision_at_3
      value: 20.104
    - type: precision_at_5
      value: 14.651
    - type: recall_at_1
      value: 34.282000000000004
    - type: recall_at_10
      value: 87.909
    - type: recall_at_100
      value: 99.21799999999999
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_20
      value: 95.377
    - type: recall_at_3
      value: 60.313
    - type: recall_at_5
      value: 73.257
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackAndroidRetrieval
      revision: f46a197baaae43b4f621051089b82a364682dfeb
      split: test
      type: mteb/cqadupstack-android
    metrics:
    - type: main_score
      value: 53.885000000000005
    - type: map_at_1
      value: 35.429
    - type: map_at_10
      value: 47.469
    - type: map_at_100
      value: 48.997
    - type: map_at_1000
      value: 49.117
    - type: map_at_20
      value: 48.324
    - type: map_at_3
      value: 43.835
    - type: map_at_5
      value: 46.043
    - type: mrr_at_1
      value: 43.34763948497854
    - type: mrr_at_10
      value: 53.258623430297234
    - type: mrr_at_100
      value: 53.99123884299005
    - type: mrr_at_1000
      value: 54.02458101713216
    - type: mrr_at_20
      value: 53.695964669618945
    - type: mrr_at_3
      value: 50.81068192656173
    - type: mrr_at_5
      value: 52.45588936576058
    - type: nauc_map_at_1000_diff1
      value: 51.55382824218782
    - type: nauc_map_at_1000_max
      value: 31.855350695084606
    - type: nauc_map_at_1000_std
      value: -5.465862008150992
    - type: nauc_map_at_100_diff1
      value: 51.55889312452534
    - type: nauc_map_at_100_max
      value: 31.88429637207401
    - type: nauc_map_at_100_std
      value: -5.40805152544196
    - type: nauc_map_at_10_diff1
      value: 51.6592677505875
    - type: nauc_map_at_10_max
      value: 31.554425233617543
    - type: nauc_map_at_10_std
      value: -6.125756131339046
    - type: nauc_map_at_1_diff1
      value: 55.6889617582672
    - type: nauc_map_at_1_max
      value: 27.821166966868176
    - type: nauc_map_at_1_std
      value: -5.778838498211728
    - type: nauc_map_at_20_diff1
      value: 51.70520970992564
    - type: nauc_map_at_20_max
      value: 31.811676633900465
    - type: nauc_map_at_20_std
      value: -5.463596751904718
    - type: nauc_map_at_3_diff1
      value: 53.206169626589606
    - type: nauc_map_at_3_max
      value: 31.64373830824983
    - type: nauc_map_at_3_std
      value: -6.054761451312827
    - type: nauc_map_at_5_diff1
      value: 52.37308971673694
    - type: nauc_map_at_5_max
      value: 31.974302019633644
    - type: nauc_map_at_5_std
      value: -6.302653399940531
    - type: nauc_mrr_at_1000_diff1
      value: 49.345152231490616
    - type: nauc_mrr_at_1000_max
      value: 33.49789501712511
    - type: nauc_mrr_at_1000_std
      value: -6.054730861163538
    - type: nauc_mrr_at_100_diff1
      value: 49.3387577601307
    - type: nauc_mrr_at_100_max
      value: 33.48149992464187
    - type: nauc_mrr_at_100_std
      value: -6.061177137579308
    - type: nauc_mrr_at_10_diff1
      value: 49.08312288449718
    - type: nauc_mrr_at_10_max
      value: 33.470393322577465
    - type: nauc_mrr_at_10_std
      value: -6.180286430216975
    - type: nauc_mrr_at_1_diff1
      value: 52.43364978537192
    - type: nauc_mrr_at_1_max
      value: 31.521755633355713
    - type: nauc_mrr_at_1_std
      value: -7.002499524130836
    - type: nauc_mrr_at_20_diff1
      value: 49.311059224991766
    - type: nauc_mrr_at_20_max
      value: 33.538523037692144
    - type: nauc_mrr_at_20_std
      value: -6.034619474981136
    - type: nauc_mrr_at_3_diff1
      value: 49.90489868439366
    - type: nauc_mrr_at_3_max
      value: 34.400493912164606
    - type: nauc_mrr_at_3_std
      value: -6.028875320994629
    - type: nauc_mrr_at_5_diff1
      value: 49.033661898983475
    - type: nauc_mrr_at_5_max
      value: 33.732315350193936
    - type: nauc_mrr_at_5_std
      value: -6.272548556330368
    - type: nauc_ndcg_at_1000_diff1
      value: 49.81681892539247
    - type: nauc_ndcg_at_1000_max
      value: 33.06518006062093
    - type: nauc_ndcg_at_1000_std
      value: -4.282105713014755
    - type: nauc_ndcg_at_100_diff1
      value: 49.42362108857786
    - type: nauc_ndcg_at_100_max
      value: 32.92024325540483
    - type: nauc_ndcg_at_100_std
      value: -3.7786765305496717
    - type: nauc_ndcg_at_10_diff1
      value: 48.83102435475594
    - type: nauc_ndcg_at_10_max
      value: 31.898404563611958
    - type: nauc_ndcg_at_10_std
      value: -6.2024003866707
    - type: nauc_ndcg_at_1_diff1
      value: 52.43364978537192
    - type: nauc_ndcg_at_1_max
      value: 31.521755633355713
    - type: nauc_ndcg_at_1_std
      value: -7.002499524130836
    - type: nauc_ndcg_at_20_diff1
      value: 49.466526454438316
    - type: nauc_ndcg_at_20_max
      value: 32.424462698701674
    - type: nauc_ndcg_at_20_std
      value: -4.520809563712905
    - type: nauc_ndcg_at_3_diff1
      value: 50.997884562583884
    - type: nauc_ndcg_at_3_max
      value: 33.26787046916917
    - type: nauc_ndcg_at_3_std
      value: -6.340699471083753
    - type: nauc_ndcg_at_5_diff1
      value: 49.68314458398097
    - type: nauc_ndcg_at_5_max
      value: 32.80910071143984
    - type: nauc_ndcg_at_5_std
      value: -6.734495576445887
    - type: nauc_precision_at_1000_diff1
      value: -24.18940012795299
    - type: nauc_precision_at_1000_max
      value: -10.995343674356896
    - type: nauc_precision_at_1000_std
      value: -8.298841004724856
    - type: nauc_precision_at_100_diff1
      value: -18.104939577865935
    - type: nauc_precision_at_100_max
      value: -1.3757613100627637
    - type: nauc_precision_at_100_std
      value: 0.07661922190466432
    - type: nauc_precision_at_10_diff1
      value: 3.9624459059275967
    - type: nauc_precision_at_10_max
      value: 14.841561593450391
    - type: nauc_precision_at_10_std
      value: -2.485374333613117
    - type: nauc_precision_at_1_diff1
      value: 52.43364978537192
    - type: nauc_precision_at_1_max
      value: 31.521755633355713
    - type: nauc_precision_at_1_std
      value: -7.002499524130836
    - type: nauc_precision_at_20_diff1
      value: -4.4791763436505265
    - type: nauc_precision_at_20_max
      value: 9.157872836996276
    - type: nauc_precision_at_20_std
      value: 2.086903518342088
    - type: nauc_precision_at_3_diff1
      value: 28.480888018235568
    - type: nauc_precision_at_3_max
      value: 30.34526267718485
    - type: nauc_precision_at_3_std
      value: -6.3006706923866025
    - type: nauc_precision_at_5_diff1
      value: 16.488039195453517
    - type: nauc_precision_at_5_max
      value: 24.593477099241852
    - type: nauc_precision_at_5_std
      value: -5.316448107840636
    - type: nauc_recall_at_1000_diff1
      value: 34.715187316533076
    - type: nauc_recall_at_1000_max
      value: 58.2266544684947
    - type: nauc_recall_at_1000_std
      value: 63.85237636398278
    - type: nauc_recall_at_100_diff1
      value: 36.08623826028132
    - type: nauc_recall_at_100_max
      value: 33.05011429439473
    - type: nauc_recall_at_100_std
      value: 16.559545021212564
    - type: nauc_recall_at_10_diff1
      value: 39.76738610714205
    - type: nauc_recall_at_10_max
      value: 28.233045706945997
    - type: nauc_recall_at_10_std
      value: -5.13243784043598
    - type: nauc_recall_at_1_diff1
      value: 55.6889617582672
    - type: nauc_recall_at_1_max
      value: 27.821166966868176
    - type: nauc_recall_at_1_std
      value: -5.778838498211728
    - type: nauc_recall_at_20_diff1
      value: 41.18682480073759
    - type: nauc_recall_at_20_max
      value: 29.525993239296945
    - type: nauc_recall_at_20_std
      value: 1.5003598438954298
    - type: nauc_recall_at_3_diff1
      value: 48.31879460301157
    - type: nauc_recall_at_3_max
      value: 32.93751306970167
    - type: nauc_recall_at_3_std
      value: -5.28070084211707
    - type: nauc_recall_at_5_diff1
      value: 44.327686388315435
    - type: nauc_recall_at_5_max
      value: 32.04823486234599
    - type: nauc_recall_at_5_std
      value: -6.4221525602778256
    - type: ndcg_at_1
      value: 43.348
    - type: ndcg_at_10
      value: 53.885000000000005
    - type: ndcg_at_100
      value: 59.204
    - type: ndcg_at_1000
      value: 60.744
    - type: ndcg_at_20
      value: 55.995
    - type: ndcg_at_3
      value: 49.112
    - type: ndcg_at_5
      value: 51.61900000000001
    - type: precision_at_1
      value: 43.348
    - type: precision_at_10
      value: 10.242999999999999
    - type: precision_at_100
      value: 1.6150000000000002
    - type: precision_at_1000
      value: 0.203
    - type: precision_at_20
      value: 6.066
    - type: precision_at_3
      value: 23.605
    - type: precision_at_5
      value: 17.024
    - type: recall_at_1
      value: 35.429
    - type: recall_at_10
      value: 65.77199999999999
    - type: recall_at_100
      value: 87.89
    - type: recall_at_1000
      value: 97.13000000000001
    - type: recall_at_20
      value: 73.299
    - type: recall_at_3
      value: 52.034000000000006
    - type: recall_at_5
      value: 58.96
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackEnglishRetrieval
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
      split: test
      type: mteb/cqadupstack-english
    metrics:
    - type: main_score
      value: 49.55
    - type: map_at_1
      value: 31.684
    - type: map_at_10
      value: 43.258
    - type: map_at_100
      value: 44.628
    - type: map_at_1000
      value: 44.761
    - type: map_at_20
      value: 44.015
    - type: map_at_3
      value: 39.778000000000006
    - type: map_at_5
      value: 41.643
    - type: mrr_at_1
      value: 39.87261146496815
    - type: mrr_at_10
      value: 49.31978566373469
    - type: mrr_at_100
      value: 49.94922739445482
    - type: mrr_at_1000
      value: 49.990325601254106
    - type: mrr_at_20
      value: 49.70597468576704
    - type: mrr_at_3
      value: 47.070063694267546
    - type: mrr_at_5
      value: 48.23248407643316
    - type: nauc_map_at_1000_diff1
      value: 53.44044712371752
    - type: nauc_map_at_1000_max
      value: 34.5651440062204
    - type: nauc_map_at_1000_std
      value: -0.9814384609230475
    - type: nauc_map_at_100_diff1
      value: 53.429004435388464
    - type: nauc_map_at_100_max
      value: 34.52038957273436
    - type: nauc_map_at_100_std
      value: -1.1021936362699805
    - type: nauc_map_at_10_diff1
      value: 53.879128574022005
    - type: nauc_map_at_10_max
      value: 33.74771524140917
    - type: nauc_map_at_10_std
      value: -2.945132777205236
    - type: nauc_map_at_1_diff1
      value: 60.25159799695403
    - type: nauc_map_at_1_max
      value: 26.843892985235808
    - type: nauc_map_at_1_std
      value: -9.618702739509093
    - type: nauc_map_at_20_diff1
      value: 53.56789898225283
    - type: nauc_map_at_20_max
      value: 34.11628845872402
    - type: nauc_map_at_20_std
      value: -2.024376635870884
    - type: nauc_map_at_3_diff1
      value: 54.45882099014072
    - type: nauc_map_at_3_max
      value: 31.29495446507793
    - type: nauc_map_at_3_std
      value: -6.391948228781555
    - type: nauc_map_at_5_diff1
      value: 54.20536489050697
    - type: nauc_map_at_5_max
      value: 32.31001487256826
    - type: nauc_map_at_5_std
      value: -5.050953263346934
    - type: nauc_mrr_at_1000_diff1
      value: 50.835858995999125
    - type: nauc_mrr_at_1000_max
      value: 38.20717381701079
    - type: nauc_mrr_at_1000_std
      value: 4.174163368228787
    - type: nauc_mrr_at_100_diff1
      value: 50.827072441041224
    - type: nauc_mrr_at_100_max
      value: 38.21077622034756
    - type: nauc_mrr_at_100_std
      value: 4.1951082737013365
    - type: nauc_mrr_at_10_diff1
      value: 50.90578491570948
    - type: nauc_mrr_at_10_max
      value: 38.19229691746408
    - type: nauc_mrr_at_10_std
      value: 3.8290750066335546
    - type: nauc_mrr_at_1_diff1
      value: 54.807021746871186
    - type: nauc_mrr_at_1_max
      value: 37.09225642043841
    - type: nauc_mrr_at_1_std
      value: 0.5654547513131355
    - type: nauc_mrr_at_20_diff1
      value: 50.86247832095378
    - type: nauc_mrr_at_20_max
      value: 38.19277867384178
    - type: nauc_mrr_at_20_std
      value: 4.098932316791841
    - type: nauc_mrr_at_3_diff1
      value: 50.788934370903036
    - type: nauc_mrr_at_3_max
      value: 37.72130561895659
    - type: nauc_mrr_at_3_std
      value: 2.7339370381517583
    - type: nauc_mrr_at_5_diff1
      value: 50.72543792525547
    - type: nauc_mrr_at_5_max
      value: 37.57740908475375
    - type: nauc_mrr_at_5_std
      value: 2.742881431085094
    - type: nauc_ndcg_at_1000_diff1
      value: 50.89692885407576
    - type: nauc_ndcg_at_1000_max
      value: 37.250583054716955
    - type: nauc_ndcg_at_1000_std
      value: 5.552279826578831
    - type: nauc_ndcg_at_100_diff1
      value: 50.624606875496944
    - type: nauc_ndcg_at_100_max
      value: 37.1024514234627
    - type: nauc_ndcg_at_100_std
      value: 5.495892760032762
    - type: nauc_ndcg_at_10_diff1
      value: 51.910387255793445
    - type: nauc_ndcg_at_10_max
      value: 36.71168418905039
    - type: nauc_ndcg_at_10_std
      value: 2.3064115117905217
    - type: nauc_ndcg_at_1_diff1
      value: 54.807021746871186
    - type: nauc_ndcg_at_1_max
      value: 37.09225642043841
    - type: nauc_ndcg_at_1_std
      value: 0.5654547513131355
    - type: nauc_ndcg_at_20_diff1
      value: 51.43416588546778
    - type: nauc_ndcg_at_20_max
      value: 36.76387180172346
    - type: nauc_ndcg_at_20_std
      value: 3.7012798827049718
    - type: nauc_ndcg_at_3_diff1
      value: 50.91198494475423
    - type: nauc_ndcg_at_3_max
      value: 34.92770670756687
    - type: nauc_ndcg_at_3_std
      value: -0.9071486759887368
    - type: nauc_ndcg_at_5_diff1
      value: 51.63559468683886
    - type: nauc_ndcg_at_5_max
      value: 34.86849679864564
    - type: nauc_ndcg_at_5_std
      value: -0.734837221224976
    - type: nauc_precision_at_1000_diff1
      value: -13.43645457127175
    - type: nauc_precision_at_1000_max
      value: 12.71162105198664
    - type: nauc_precision_at_1000_std
      value: 33.175399007040255
    - type: nauc_precision_at_100_diff1
      value: -8.549834785105412
    - type: nauc_precision_at_100_max
      value: 22.47383497331883
    - type: nauc_precision_at_100_std
      value: 39.09108761430844
    - type: nauc_precision_at_10_diff1
      value: 7.556572451100043
    - type: nauc_precision_at_10_max
      value: 35.35285122987575
    - type: nauc_precision_at_10_std
      value: 29.417466305615967
    - type: nauc_precision_at_1_diff1
      value: 54.807021746871186
    - type: nauc_precision_at_1_max
      value: 37.09225642043841
    - type: nauc_precision_at_1_std
      value: 0.5654547513131355
    - type: nauc_precision_at_20_diff1
      value: -0.550158641635712
    - type: nauc_precision_at_20_max
      value: 29.9068430006187
    - type: nauc_precision_at_20_std
      value: 33.920603132821185
    - type: nauc_precision_at_3_diff1
      value: 25.551264664276687
    - type: nauc_precision_at_3_max
      value: 37.59463225854679
    - type: nauc_precision_at_3_std
      value: 13.707295021359043
    - type: nauc_precision_at_5_diff1
      value: 17.76136129817151
    - type: nauc_precision_at_5_max
      value: 35.85363807255972
    - type: nauc_precision_at_5_std
      value: 19.48470876841111
    - type: nauc_recall_at_1000_diff1
      value: 37.1593620123866
    - type: nauc_recall_at_1000_max
      value: 46.29322536951135
    - type: nauc_recall_at_1000_std
      value: 51.47312657083967
    - type: nauc_recall_at_100_diff1
      value: 37.7542224949536
    - type: nauc_recall_at_100_max
      value: 38.84120637703135
    - type: nauc_recall_at_100_std
      value: 28.839672572221925
    - type: nauc_recall_at_10_diff1
      value: 46.24130302658384
    - type: nauc_recall_at_10_max
      value: 35.89001724712849
    - type: nauc_recall_at_10_std
      value: 6.985137790828618
    - type: nauc_recall_at_1_diff1
      value: 60.25159799695403
    - type: nauc_recall_at_1_max
      value: 26.843892985235808
    - type: nauc_recall_at_1_std
      value: -9.618702739509093
    - type: nauc_recall_at_20_diff1
      value: 43.63576680886187
    - type: nauc_recall_at_20_max
      value: 36.79079644708101
    - type: nauc_recall_at_20_std
      value: 13.81561928605839
    - type: nauc_recall_at_3_diff1
      value: 48.2299322140522
    - type: nauc_recall_at_3_max
      value: 30.038088484376203
    - type: nauc_recall_at_3_std
      value: -4.871116183843762
    - type: nauc_recall_at_5_diff1
      value: 47.22331872695983
    - type: nauc_recall_at_5_max
      value: 30.398541477173136
    - type: nauc_recall_at_5_std
      value: -3.2038541888528957
    - type: ndcg_at_1
      value: 39.873
    - type: ndcg_at_10
      value: 49.55
    - type: ndcg_at_100
      value: 53.809
    - type: ndcg_at_1000
      value: 55.767999999999994
    - type: ndcg_at_20
      value: 51.275999999999996
    - type: ndcg_at_3
      value: 44.91
    - type: ndcg_at_5
      value: 46.855999999999995
    - type: precision_at_1
      value: 39.873
    - type: precision_at_10
      value: 9.65
    - type: precision_at_100
      value: 1.522
    - type: precision_at_1000
      value: 0.196
    - type: precision_at_20
      value: 5.701
    - type: precision_at_3
      value: 22.166
    - type: precision_at_5
      value: 15.643
    - type: recall_at_1
      value: 31.684
    - type: recall_at_10
      value: 60.69
    - type: recall_at_100
      value: 78.521
    - type: recall_at_1000
      value: 91.02900000000001
    - type: recall_at_20
      value: 66.973
    - type: recall_at_3
      value: 46.807
    - type: recall_at_5
      value: 52.402
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGamingRetrieval
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
      split: test
      type: mteb/cqadupstack-gaming
    metrics:
    - type: main_score
      value: 62.686
    - type: map_at_1
      value: 43.856
    - type: map_at_10
      value: 57.056
    - type: map_at_100
      value: 58.048
    - type: map_at_1000
      value: 58.092
    - type: map_at_20
      value: 57.684000000000005
    - type: map_at_3
      value: 53.958
    - type: map_at_5
      value: 55.80500000000001
    - type: mrr_at_1
      value: 50.03134796238244
    - type: mrr_at_10
      value: 60.31022043091019
    - type: mrr_at_100
      value: 60.91892338857461
    - type: mrr_at_1000
      value: 60.93770463536649
    - type: mrr_at_20
      value: 60.705642387392736
    - type: mrr_at_3
      value: 58.286311389759746
    - type: mrr_at_5
      value: 59.49320794148393
    - type: nauc_map_at_1000_diff1
      value: 54.849140197256695
    - type: nauc_map_at_1000_max
      value: 38.978448968260224
    - type: nauc_map_at_1000_std
      value: 0.4955439383268162
    - type: nauc_map_at_100_diff1
      value: 54.824334747823364
    - type: nauc_map_at_100_max
      value: 38.959443109450994
    - type: nauc_map_at_100_std
      value: 0.49626092018886037
    - type: nauc_map_at_10_diff1
      value: 54.778189277103394
    - type: nauc_map_at_10_max
      value: 38.20972191654546
    - type: nauc_map_at_10_std
      value: -0.7239823837455759
    - type: nauc_map_at_1_diff1
      value: 58.74017164752485
    - type: nauc_map_at_1_max
      value: 31.528974862589585
    - type: nauc_map_at_1_std
      value: -3.273824691929492
    - type: nauc_map_at_20_diff1
      value: 54.78943693416187
    - type: nauc_map_at_20_max
      value: 38.77930316443076
    - type: nauc_map_at_20_std
      value: 0.25607460088355544
    - type: nauc_map_at_3_diff1
      value: 55.68313410225767
    - type: nauc_map_at_3_max
      value: 36.22847284104399
    - type: nauc_map_at_3_std
      value: -3.010979639100503
    - type: nauc_map_at_5_diff1
      value: 55.11385094420661
    - type: nauc_map_at_5_max
      value: 37.319681045490924
    - type: nauc_map_at_5_std
      value: -2.156640733221061
    - type: nauc_mrr_at_1000_diff1
      value: 54.504759468380705
    - type: nauc_mrr_at_1000_max
      value: 40.58849492650406
    - type: nauc_mrr_at_1000_std
      value: 1.8226622175866118
    - type: nauc_mrr_at_100_diff1
      value: 54.4918034449886
    - type: nauc_mrr_at_100_max
      value: 40.59202728933427
    - type: nauc_mrr_at_100_std
      value: 1.8276428096536335
    - type: nauc_mrr_at_10_diff1
      value: 54.33603399493329
    - type: nauc_mrr_at_10_max
      value: 40.58896878978089
    - type: nauc_mrr_at_10_std
      value: 1.5733340909114375
    - type: nauc_mrr_at_1_diff1
      value: 58.062410036466105
    - type: nauc_mrr_at_1_max
      value: 37.660958859966506
    - type: nauc_mrr_at_1_std
      value: 0.029007600674170648
    - type: nauc_mrr_at_20_diff1
      value: 54.43793386924358
    - type: nauc_mrr_at_20_max
      value: 40.66773423875307
    - type: nauc_mrr_at_20_std
      value: 1.891967891797154
    - type: nauc_mrr_at_3_diff1
      value: 54.77901284537966
    - type: nauc_mrr_at_3_max
      value: 40.182219821206964
    - type: nauc_mrr_at_3_std
      value: 0.8911935034597871
    - type: nauc_mrr_at_5_diff1
      value: 54.466068837163675
    - type: nauc_mrr_at_5_max
      value: 40.334996916684126
    - type: nauc_mrr_at_5_std
      value: 0.9460830492892364
    - type: nauc_ndcg_at_1000_diff1
      value: 53.8465376860938
    - type: nauc_ndcg_at_1000_max
      value: 41.63158111016696
    - type: nauc_ndcg_at_1000_std
      value: 3.864205884257578
    - type: nauc_ndcg_at_100_diff1
      value: 53.4025864436944
    - type: nauc_ndcg_at_100_max
      value: 41.805453995307914
    - type: nauc_ndcg_at_100_std
      value: 4.36777557904857
    - type: nauc_ndcg_at_10_diff1
      value: 52.96034987157544
    - type: nauc_ndcg_at_10_max
      value: 40.7601173480795
    - type: nauc_ndcg_at_10_std
      value: 1.905824035879141
    - type: nauc_ndcg_at_1_diff1
      value: 58.062410036466105
    - type: nauc_ndcg_at_1_max
      value: 37.660958859966506
    - type: nauc_ndcg_at_1_std
      value: 0.029007600674170648
    - type: nauc_ndcg_at_20_diff1
      value: 53.2834771889242
    - type: nauc_ndcg_at_20_max
      value: 41.713541932946406
    - type: nauc_ndcg_at_20_std
      value: 3.865102828793311
    - type: nauc_ndcg_at_3_diff1
      value: 54.03389464372289
    - type: nauc_ndcg_at_3_max
      value: 38.41449914649933
    - type: nauc_ndcg_at_3_std
      value: -0.886276189886313
    - type: nauc_ndcg_at_5_diff1
      value: 53.456413320299
    - type: nauc_ndcg_at_5_max
      value: 39.49048882649335
    - type: nauc_ndcg_at_5_std
      value: -0.42692690160443814
    - type: nauc_precision_at_1000_diff1
      value: -14.770791653274824
    - type: nauc_precision_at_1000_max
      value: 21.479874538905246
    - type: nauc_precision_at_1000_std
      value: 28.607024261300207
    - type: nauc_precision_at_100_diff1
      value: -12.189696449878126
    - type: nauc_precision_at_100_max
      value: 26.69785787492456
    - type: nauc_precision_at_100_std
      value: 33.59098307467553
    - type: nauc_precision_at_10_diff1
      value: 6.922968330978399
    - type: nauc_precision_at_10_max
      value: 34.52138344123087
    - type: nauc_precision_at_10_std
      value: 21.768427637079952
    - type: nauc_precision_at_1_diff1
      value: 58.062410036466105
    - type: nauc_precision_at_1_max
      value: 37.660958859966506
    - type: nauc_precision_at_1_std
      value: 0.029007600674170648
    - type: nauc_precision_at_20_diff1
      value: -0.6837867902179278
    - type: nauc_precision_at_20_max
      value: 33.98683709011133
    - type: nauc_precision_at_20_std
      value: 30.8845561918902
    - type: nauc_precision_at_3_diff1
      value: 28.195043041120847
    - type: nauc_precision_at_3_max
      value: 37.659916094938836
    - type: nauc_precision_at_3_std
      value: 7.226520146634867
    - type: nauc_precision_at_5_diff1
      value: 16.633667288096245
    - type: nauc_precision_at_5_max
      value: 34.90176597404891
    - type: nauc_precision_at_5_std
      value: 12.421585442334088
    - type: nauc_recall_at_1000_diff1
      value: 45.20743732415397
    - type: nauc_recall_at_1000_max
      value: 72.77115913579242
    - type: nauc_recall_at_1000_std
      value: 70.48328496679083
    - type: nauc_recall_at_100_diff1
      value: 38.56282680810794
    - type: nauc_recall_at_100_max
      value: 55.46797683321103
    - type: nauc_recall_at_100_std
      value: 36.878791151929136
    - type: nauc_recall_at_10_diff1
      value: 44.18252051452362
    - type: nauc_recall_at_10_max
      value: 43.33391810040086
    - type: nauc_recall_at_10_std
      value: 6.663378192277723
    - type: nauc_recall_at_1_diff1
      value: 58.74017164752485
    - type: nauc_recall_at_1_max
      value: 31.528974862589585
    - type: nauc_recall_at_1_std
      value: -3.273824691929492
    - type: nauc_recall_at_20_diff1
      value: 44.19944231642417
    - type: nauc_recall_at_20_max
      value: 49.401101483915866
    - type: nauc_recall_at_20_std
      value: 18.97803841673839
    - type: nauc_recall_at_3_diff1
      value: 49.56378985428704
    - type: nauc_recall_at_3_max
      value: 36.434210616870224
    - type: nauc_recall_at_3_std
      value: -2.850559971607616
    - type: nauc_recall_at_5_diff1
      value: 47.37107217086109
    - type: nauc_recall_at_5_max
      value: 39.0236745509895
    - type: nauc_recall_at_5_std
      value: -1.7402454457937195
    - type: ndcg_at_1
      value: 50.031000000000006
    - type: ndcg_at_10
      value: 62.686
    - type: ndcg_at_100
      value: 66.403
    - type: ndcg_at_1000
      value: 67.241
    - type: ndcg_at_20
      value: 64.37899999999999
    - type: ndcg_at_3
      value: 57.859
    - type: ndcg_at_5
      value: 60.375
    - type: precision_at_1
      value: 50.031000000000006
    - type: precision_at_10
      value: 9.856
    - type: precision_at_100
      value: 1.266
    - type: precision_at_1000
      value: 0.13799999999999998
    - type: precision_at_20
      value: 5.489
    - type: precision_at_3
      value: 25.746999999999996
    - type: precision_at_5
      value: 17.492
    - type: recall_at_1
      value: 43.856
    - type: recall_at_10
      value: 75.824
    - type: recall_at_100
      value: 91.622
    - type: recall_at_1000
      value: 97.538
    - type: recall_at_20
      value: 81.951
    - type: recall_at_3
      value: 63.016000000000005
    - type: recall_at_5
      value: 69.18299999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGisRetrieval
      revision: 5003b3064772da1887988e05400cf3806fe491f2
      split: test
      type: mteb/cqadupstack-gis
    metrics:
    - type: main_score
      value: 43.983
    - type: map_at_1
      value: 28.942
    - type: map_at_10
      value: 38.621
    - type: map_at_100
      value: 39.7
    - type: map_at_1000
      value: 39.766
    - type: map_at_20
      value: 39.262
    - type: map_at_3
      value: 35.719
    - type: map_at_5
      value: 37.378
    - type: mrr_at_1
      value: 31.29943502824859
    - type: mrr_at_10
      value: 40.76463994260603
    - type: mrr_at_100
      value: 41.67073617629083
    - type: mrr_at_1000
      value: 41.717446259457105
    - type: mrr_at_20
      value: 41.32577374689195
    - type: mrr_at_3
      value: 37.984934086628996
    - type: mrr_at_5
      value: 39.64595103578152
    - type: nauc_map_at_1000_diff1
      value: 43.64461679688985
    - type: nauc_map_at_1000_max
      value: 31.53717883948204
    - type: nauc_map_at_1000_std
      value: 1.193745788248017
    - type: nauc_map_at_100_diff1
      value: 43.63847825079489
    - type: nauc_map_at_100_max
      value: 31.536602619279165
    - type: nauc_map_at_100_std
      value: 1.2001240243342401
    - type: nauc_map_at_10_diff1
      value: 43.845991987142014
    - type: nauc_map_at_10_max
      value: 31.27509937344113
    - type: nauc_map_at_10_std
      value: 0.7327934840520994
    - type: nauc_map_at_1_diff1
      value: 50.62269273984579
    - type: nauc_map_at_1_max
      value: 30.16325757909521
    - type: nauc_map_at_1_std
      value: -0.6398875136233392
    - type: nauc_map_at_20_diff1
      value: 43.630758403790914
    - type: nauc_map_at_20_max
      value: 31.408258098047703
    - type: nauc_map_at_20_std
      value: 1.12616034652217
    - type: nauc_map_at_3_diff1
      value: 44.823493567359456
    - type: nauc_map_at_3_max
      value: 31.075886347614496
    - type: nauc_map_at_3_std
      value: -0.25126874515735426
    - type: nauc_map_at_5_diff1
      value: 43.79768853087658
    - type: nauc_map_at_5_max
      value: 31.091080995725324
    - type: nauc_map_at_5_std
      value: 0.16440771782544047
    - type: nauc_mrr_at_1000_diff1
      value: 42.7865400752329
    - type: nauc_mrr_at_1000_max
      value: 32.84731670326893
    - type: nauc_mrr_at_1000_std
      value: 2.6067637582013825
    - type: nauc_mrr_at_100_diff1
      value: 42.771741548331065
    - type: nauc_mrr_at_100_max
      value: 32.85324232845987
    - type: nauc_mrr_at_100_std
      value: 2.6092786694308376
    - type: nauc_mrr_at_10_diff1
      value: 42.82969738870672
    - type: nauc_mrr_at_10_max
      value: 32.69407549631432
    - type: nauc_mrr_at_10_std
      value: 2.302903910016054
    - type: nauc_mrr_at_1_diff1
      value: 49.05638333657571
    - type: nauc_mrr_at_1_max
      value: 33.12030717171514
    - type: nauc_mrr_at_1_std
      value: 1.3278035087690774
    - type: nauc_mrr_at_20_diff1
      value: 42.74267239536286
    - type: nauc_mrr_at_20_max
      value: 32.78571108973092
    - type: nauc_mrr_at_20_std
      value: 2.5932669908758643
    - type: nauc_mrr_at_3_diff1
      value: 43.69963426089187
    - type: nauc_mrr_at_3_max
      value: 32.78193126956233
    - type: nauc_mrr_at_3_std
      value: 1.634874463134699
    - type: nauc_mrr_at_5_diff1
      value: 42.838630647832524
    - type: nauc_mrr_at_5_max
      value: 32.459318735260545
    - type: nauc_mrr_at_5_std
      value: 1.9412518283209172
    - type: nauc_ndcg_at_1000_diff1
      value: 41.01253839851583
    - type: nauc_ndcg_at_1000_max
      value: 32.69570568894237
    - type: nauc_ndcg_at_1000_std
      value: 3.4254737113410343
    - type: nauc_ndcg_at_100_diff1
      value: 40.62589243745832
    - type: nauc_ndcg_at_100_max
      value: 32.664990655736126
    - type: nauc_ndcg_at_100_std
      value: 3.799569445326048
    - type: nauc_ndcg_at_10_diff1
      value: 41.31658753735306
    - type: nauc_ndcg_at_10_max
      value: 31.511946320339295
    - type: nauc_ndcg_at_10_std
      value: 2.0492930500796662
    - type: nauc_ndcg_at_1_diff1
      value: 49.05638333657571
    - type: nauc_ndcg_at_1_max
      value: 33.12030717171514
    - type: nauc_ndcg_at_1_std
      value: 1.3278035087690774
    - type: nauc_ndcg_at_20_diff1
      value: 40.66188223212841
    - type: nauc_ndcg_at_20_max
      value: 31.926240431497476
    - type: nauc_ndcg_at_20_std
      value: 3.370398664595343
    - type: nauc_ndcg_at_3_diff1
      value: 43.035580180241
    - type: nauc_ndcg_at_3_max
      value: 31.363874129878404
    - type: nauc_ndcg_at_3_std
      value: 0.1422507242819929
    - type: nauc_ndcg_at_5_diff1
      value: 41.29049003955878
    - type: nauc_ndcg_at_5_max
      value: 31.112034994977737
    - type: nauc_ndcg_at_5_std
      value: 0.860179279828966
    - type: nauc_precision_at_1000_diff1
      value: -12.41854465881981
    - type: nauc_precision_at_1000_max
      value: 14.706779246590548
    - type: nauc_precision_at_1000_std
      value: 9.812804367375206
    - type: nauc_precision_at_100_diff1
      value: 2.797520107808461
    - type: nauc_precision_at_100_max
      value: 24.335873541811406
    - type: nauc_precision_at_100_std
      value: 12.87186398750545
    - type: nauc_precision_at_10_diff1
      value: 24.530962799265847
    - type: nauc_precision_at_10_max
      value: 31.00772010798733
    - type: nauc_precision_at_10_std
      value: 6.696733001548185
    - type: nauc_precision_at_1_diff1
      value: 49.05638333657571
    - type: nauc_precision_at_1_max
      value: 33.12030717171514
    - type: nauc_precision_at_1_std
      value: 1.3278035087690774
    - type: nauc_precision_at_20_diff1
      value: 16.25028416351204
    - type: nauc_precision_at_20_max
      value: 29.629326492027342
    - type: nauc_precision_at_20_std
      value: 11.085888573121679
    - type: nauc_precision_at_3_diff1
      value: 33.923667689694256
    - type: nauc_precision_at_3_max
      value: 33.5859782361996
    - type: nauc_precision_at_3_std
      value: 1.9468331086918693
    - type: nauc_precision_at_5_diff1
      value: 27.917827233088875
    - type: nauc_precision_at_5_max
      value: 33.13290043423535
    - type: nauc_precision_at_5_std
      value: 3.800870695945311
    - type: nauc_recall_at_1000_diff1
      value: 9.680283388428789
    - type: nauc_recall_at_1000_max
      value: 49.479399284871235
    - type: nauc_recall_at_1000_std
      value: 31.506985071436088
    - type: nauc_recall_at_100_diff1
      value: 23.607673377885448
    - type: nauc_recall_at_100_max
      value: 36.637750366403935
    - type: nauc_recall_at_100_std
      value: 18.30770690564224
    - type: nauc_recall_at_10_diff1
      value: 33.199683418312446
    - type: nauc_recall_at_10_max
      value: 29.63115497012312
    - type: nauc_recall_at_10_std
      value: 4.813200391480566
    - type: nauc_recall_at_1_diff1
      value: 50.62269273984579
    - type: nauc_recall_at_1_max
      value: 30.16325757909521
    - type: nauc_recall_at_1_std
      value: -0.6398875136233392
    - type: nauc_recall_at_20_diff1
      value: 29.16488387844995
    - type: nauc_recall_at_20_max
      value: 30.788019479459
    - type: nauc_recall_at_20_std
      value: 11.031953917298853
    - type: nauc_recall_at_3_diff1
      value: 38.215351600417065
    - type: nauc_recall_at_3_max
      value: 29.619887154236128
    - type: nauc_recall_at_3_std
      value: -0.13237298980339363
    - type: nauc_recall_at_5_diff1
      value: 33.93788042633265
    - type: nauc_recall_at_5_max
      value: 28.67185092656741
    - type: nauc_recall_at_5_std
      value: 1.316700201091445
    - type: ndcg_at_1
      value: 31.299
    - type: ndcg_at_10
      value: 43.983
    - type: ndcg_at_100
      value: 48.992999999999995
    - type: ndcg_at_1000
      value: 50.757
    - type: ndcg_at_20
      value: 46.152
    - type: ndcg_at_3
      value: 38.367000000000004
    - type: ndcg_at_5
      value: 41.171
    - type: precision_at_1
      value: 31.299
    - type: precision_at_10
      value: 6.734
    - type: precision_at_100
      value: 0.972
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_20
      value: 3.898
    - type: precision_at_3
      value: 16.121
    - type: precision_at_5
      value: 11.344999999999999
    - type: recall_at_1
      value: 28.942
    - type: recall_at_10
      value: 58.343999999999994
    - type: recall_at_100
      value: 80.82300000000001
    - type: recall_at_1000
      value: 94.348
    - type: recall_at_20
      value: 66.449
    - type: recall_at_3
      value: 43.415
    - type: recall_at_5
      value: 50.007999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackMathematicaRetrieval
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
      split: test
      type: mteb/cqadupstack-mathematica
    metrics:
    - type: main_score
      value: 33.144
    - type: map_at_1
      value: 19.41
    - type: map_at_10
      value: 27.802
    - type: map_at_100
      value: 29.157
    - type: map_at_1000
      value: 29.274
    - type: map_at_20
      value: 28.549000000000003
    - type: map_at_3
      value: 25.052999999999997
    - type: map_at_5
      value: 26.521
    - type: mrr_at_1
      value: 23.756218905472636
    - type: mrr_at_10
      value: 32.3623450209271
    - type: mrr_at_100
      value: 33.3648208444617
    - type: mrr_at_1000
      value: 33.427688215162185
    - type: mrr_at_20
      value: 32.93723485575758
    - type: mrr_at_3
      value: 29.539800995024883
    - type: mrr_at_5
      value: 31.156716417910452
    - type: nauc_map_at_1000_diff1
      value: 36.196391248081284
    - type: nauc_map_at_1000_max
      value: 25.650644367091495
    - type: nauc_map_at_1000_std
      value: 6.130340697729844
    - type: nauc_map_at_100_diff1
      value: 36.138890642411376
    - type: nauc_map_at_100_max
      value: 25.587124763888518
    - type: nauc_map_at_100_std
      value: 6.129336379055536
    - type: nauc_map_at_10_diff1
      value: 36.254426743566775
    - type: nauc_map_at_10_max
      value: 25.465599906543034
    - type: nauc_map_at_10_std
      value: 5.880280378112879
    - type: nauc_map_at_1_diff1
      value: 42.890551563179976
    - type: nauc_map_at_1_max
      value: 25.813805281076956
    - type: nauc_map_at_1_std
      value: 5.150718386163028
    - type: nauc_map_at_20_diff1
      value: 35.98551587974314
    - type: nauc_map_at_20_max
      value: 25.501540521726636
    - type: nauc_map_at_20_std
      value: 5.858703157458749
    - type: nauc_map_at_3_diff1
      value: 37.646558039577734
    - type: nauc_map_at_3_max
      value: 26.138491471124247
    - type: nauc_map_at_3_std
      value: 6.0487505175540734
    - type: nauc_map_at_5_diff1
      value: 36.817582976153695
    - type: nauc_map_at_5_max
      value: 25.398200211121146
    - type: nauc_map_at_5_std
      value: 6.31126763919522
    - type: nauc_mrr_at_1000_diff1
      value: 37.313544952847835
    - type: nauc_mrr_at_1000_max
      value: 26.96218532078988
    - type: nauc_mrr_at_1000_std
      value: 6.814359224654042
    - type: nauc_mrr_at_100_diff1
      value: 37.28104407653679
    - type: nauc_mrr_at_100_max
      value: 26.931243040477256
    - type: nauc_mrr_at_100_std
      value: 6.800500150841733
    - type: nauc_mrr_at_10_diff1
      value: 37.315832621275895
    - type: nauc_mrr_at_10_max
      value: 26.941454225978372
    - type: nauc_mrr_at_10_std
      value: 6.837046527796884
    - type: nauc_mrr_at_1_diff1
      value: 43.19904188582958
    - type: nauc_mrr_at_1_max
      value: 26.975620445904795
    - type: nauc_mrr_at_1_std
      value: 4.52071008581395
    - type: nauc_mrr_at_20_diff1
      value: 37.2200524790774
    - type: nauc_mrr_at_20_max
      value: 26.971494160765847
    - type: nauc_mrr_at_20_std
      value: 6.716431228783282
    - type: nauc_mrr_at_3_diff1
      value: 38.46236387340654
    - type: nauc_mrr_at_3_max
      value: 27.846812992192056
    - type: nauc_mrr_at_3_std
      value: 6.550711872569794
    - type: nauc_mrr_at_5_diff1
      value: 37.620346007658476
    - type: nauc_mrr_at_5_max
      value: 27.031025952102038
    - type: nauc_mrr_at_5_std
      value: 7.32343760231163
    - type: nauc_ndcg_at_1000_diff1
      value: 34.95081314840592
    - type: nauc_ndcg_at_1000_max
      value: 26.89265465124325
    - type: nauc_ndcg_at_1000_std
      value: 7.854154466831975
    - type: nauc_ndcg_at_100_diff1
      value: 34.01417812563093
    - type: nauc_ndcg_at_100_max
      value: 25.792737746436835
    - type: nauc_ndcg_at_100_std
      value: 7.726584165493833
    - type: nauc_ndcg_at_10_diff1
      value: 33.895122516474466
    - type: nauc_ndcg_at_10_max
      value: 25.388442204589612
    - type: nauc_ndcg_at_10_std
      value: 6.359560223645991
    - type: nauc_ndcg_at_1_diff1
      value: 43.19904188582958
    - type: nauc_ndcg_at_1_max
      value: 26.975620445904795
    - type: nauc_ndcg_at_1_std
      value: 4.52071008581395
    - type: nauc_ndcg_at_20_diff1
      value: 33.36078689830245
    - type: nauc_ndcg_at_20_max
      value: 25.531794610571563
    - type: nauc_ndcg_at_20_std
      value: 6.136658608653248
    - type: nauc_ndcg_at_3_diff1
      value: 36.44505602530781
    - type: nauc_ndcg_at_3_max
      value: 26.9104071983157
    - type: nauc_ndcg_at_3_std
      value: 6.427178520371878
    - type: nauc_ndcg_at_5_diff1
      value: 35.01384323197442
    - type: nauc_ndcg_at_5_max
      value: 25.5560447088692
    - type: nauc_ndcg_at_5_std
      value: 7.3676236760360485
    - type: nauc_precision_at_1000_diff1
      value: 2.8903331041804514
    - type: nauc_precision_at_1000_max
      value: 4.059662742366004
    - type: nauc_precision_at_1000_std
      value: -1.5891687644008334
    - type: nauc_precision_at_100_diff1
      value: 8.437726471693766
    - type: nauc_precision_at_100_max
      value: 11.250588557568427
    - type: nauc_precision_at_100_std
      value: 4.231571164627862
    - type: nauc_precision_at_10_diff1
      value: 19.57085237210294
    - type: nauc_precision_at_10_max
      value: 20.973093492003905
    - type: nauc_precision_at_10_std
      value: 3.197416248152466
    - type: nauc_precision_at_1_diff1
      value: 43.19904188582958
    - type: nauc_precision_at_1_max
      value: 26.975620445904795
    - type: nauc_precision_at_1_std
      value: 4.52071008581395
    - type: nauc_precision_at_20_diff1
      value: 15.67136554192724
    - type: nauc_precision_at_20_max
      value: 17.706882621057858
    - type: nauc_precision_at_20_std
      value: 1.9363472182867714
    - type: nauc_precision_at_3_diff1
      value: 30.38035695042325
    - type: nauc_precision_at_3_max
      value: 26.48218693244094
    - type: nauc_precision_at_3_std
      value: 6.424657705785632
    - type: nauc_precision_at_5_diff1
      value: 25.272543315171458
    - type: nauc_precision_at_5_max
      value: 22.32441421311652
    - type: nauc_precision_at_5_std
      value: 7.4912569081905716
    - type: nauc_recall_at_1000_diff1
      value: 25.5748044137675
    - type: nauc_recall_at_1000_max
      value: 43.85796585370269
    - type: nauc_recall_at_1000_std
      value: 30.0338086596789
    - type: nauc_recall_at_100_diff1
      value: 22.577080638885093
    - type: nauc_recall_at_100_max
      value: 23.224511700617477
    - type: nauc_recall_at_100_std
      value: 15.187963852289313
    - type: nauc_recall_at_10_diff1
      value: 25.058592299355908
    - type: nauc_recall_at_10_max
      value: 22.24448483279841
    - type: nauc_recall_at_10_std
      value: 6.3179089740052765
    - type: nauc_recall_at_1_diff1
      value: 42.890551563179976
    - type: nauc_recall_at_1_max
      value: 25.813805281076956
    - type: nauc_recall_at_1_std
      value: 5.150718386163028
    - type: nauc_recall_at_20_diff1
      value: 22.433865123187307
    - type: nauc_recall_at_20_max
      value: 22.739695641511762
    - type: nauc_recall_at_20_std
      value: 5.362005125538497
    - type: nauc_recall_at_3_diff1
      value: 32.17919168998616
    - type: nauc_recall_at_3_max
      value: 26.044028436867357
    - type: nauc_recall_at_3_std
      value: 7.420349884006329
    - type: nauc_recall_at_5_diff1
      value: 28.967104573649138
    - type: nauc_recall_at_5_max
      value: 23.40865848168201
    - type: nauc_recall_at_5_std
      value: 9.174406147723621
    - type: ndcg_at_1
      value: 23.756
    - type: ndcg_at_10
      value: 33.144
    - type: ndcg_at_100
      value: 39.261
    - type: ndcg_at_1000
      value: 41.881
    - type: ndcg_at_20
      value: 35.56
    - type: ndcg_at_3
      value: 27.927999999999997
    - type: ndcg_at_5
      value: 30.293999999999997
    - type: precision_at_1
      value: 23.756
    - type: precision_at_10
      value: 5.995
    - type: precision_at_100
      value: 1.053
    - type: precision_at_1000
      value: 0.14100000000000001
    - type: precision_at_20
      value: 3.688
    - type: precision_at_3
      value: 13.059999999999999
    - type: precision_at_5
      value: 9.602
    - type: recall_at_1
      value: 19.41
    - type: recall_at_10
      value: 45.074
    - type: recall_at_100
      value: 71.131
    - type: recall_at_1000
      value: 89.604
    - type: recall_at_20
      value: 53.673
    - type: recall_at_3
      value: 31.055
    - type: recall_at_5
      value: 36.714999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackPhysicsRetrieval
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
      split: test
      type: mteb/cqadupstack-physics
    metrics:
    - type: main_score
      value: 49.675000000000004
    - type: map_at_1
      value: 33.178999999999995
    - type: map_at_10
      value: 43.807
    - type: map_at_100
      value: 45.17
    - type: map_at_1000
      value: 45.271
    - type: map_at_20
      value: 44.516
    - type: map_at_3
      value: 40.813
    - type: map_at_5
      value: 42.457
    - type: mrr_at_1
      value: 40.32723772858518
    - type: mrr_at_10
      value: 49.646867409138814
    - type: mrr_at_100
      value: 50.493686101426285
    - type: mrr_at_1000
      value: 50.525386961808834
    - type: mrr_at_20
      value: 50.120274354884586
    - type: mrr_at_3
      value: 47.49759384023096
    - type: mrr_at_5
      value: 48.72473532242535
    - type: nauc_map_at_1000_diff1
      value: 49.5947127786396
    - type: nauc_map_at_1000_max
      value: 33.39720045844929
    - type: nauc_map_at_1000_std
      value: -3.131428593252271
    - type: nauc_map_at_100_diff1
      value: 49.57797867324617
    - type: nauc_map_at_100_max
      value: 33.356927974709464
    - type: nauc_map_at_100_std
      value: -3.1661365376766337
    - type: nauc_map_at_10_diff1
      value: 49.59294630598952
    - type: nauc_map_at_10_max
      value: 32.86647346990462
    - type: nauc_map_at_10_std
      value: -4.1582043443386745
    - type: nauc_map_at_1_diff1
      value: 53.98646767288695
    - type: nauc_map_at_1_max
      value: 29.45629077638936
    - type: nauc_map_at_1_std
      value: -5.621187380771589
    - type: nauc_map_at_20_diff1
      value: 49.486982890447074
    - type: nauc_map_at_20_max
      value: 33.11681933406332
    - type: nauc_map_at_20_std
      value: -3.5826433195146854
    - type: nauc_map_at_3_diff1
      value: 50.81807107491861
    - type: nauc_map_at_3_max
      value: 32.32552291988859
    - type: nauc_map_at_3_std
      value: -3.952946504088928
    - type: nauc_map_at_5_diff1
      value: 49.70201354274439
    - type: nauc_map_at_5_max
      value: 32.831846031004886
    - type: nauc_map_at_5_std
      value: -3.8330488624207737
    - type: nauc_mrr_at_1000_diff1
      value: 49.04159472507738
    - type: nauc_mrr_at_1000_max
      value: 35.617600171138676
    - type: nauc_mrr_at_1000_std
      value: -1.5975830757486646
    - type: nauc_mrr_at_100_diff1
      value: 49.03848471692094
    - type: nauc_mrr_at_100_max
      value: 35.61936748662614
    - type: nauc_mrr_at_100_std
      value: -1.5922053398594729
    - type: nauc_mrr_at_10_diff1
      value: 48.92463964652612
    - type: nauc_mrr_at_10_max
      value: 35.37757708992045
    - type: nauc_mrr_at_10_std
      value: -2.2052028139567303
    - type: nauc_mrr_at_1_diff1
      value: 52.23915787290734
    - type: nauc_mrr_at_1_max
      value: 34.393531787632334
    - type: nauc_mrr_at_1_std
      value: -1.452007661016969
    - type: nauc_mrr_at_20_diff1
      value: 48.91168438018404
    - type: nauc_mrr_at_20_max
      value: 35.478962544421876
    - type: nauc_mrr_at_20_std
      value: -1.8246048423555414
    - type: nauc_mrr_at_3_diff1
      value: 50.115432665442164
    - type: nauc_mrr_at_3_max
      value: 35.89093796085569
    - type: nauc_mrr_at_3_std
      value: -1.4895016313153366
    - type: nauc_mrr_at_5_diff1
      value: 49.04321261351915
    - type: nauc_mrr_at_5_max
      value: 35.85730520949451
    - type: nauc_mrr_at_5_std
      value: -1.68790556880753
    - type: nauc_ndcg_at_1000_diff1
      value: 48.294697499154374
    - type: nauc_ndcg_at_1000_max
      value: 35.167410242367595
    - type: nauc_ndcg_at_1000_std
      value: -0.6346078535914157
    - type: nauc_ndcg_at_100_diff1
      value: 48.025525283449014
    - type: nauc_ndcg_at_100_max
      value: 34.79288511776105
    - type: nauc_ndcg_at_100_std
      value: -0.7823403044086993
    - type: nauc_ndcg_at_10_diff1
      value: 47.70793258015258
    - type: nauc_ndcg_at_10_max
      value: 33.09558927880104
    - type: nauc_ndcg_at_10_std
      value: -4.7793864166260605
    - type: nauc_ndcg_at_1_diff1
      value: 52.23915787290734
    - type: nauc_ndcg_at_1_max
      value: 34.393531787632334
    - type: nauc_ndcg_at_1_std
      value: -1.452007661016969
    - type: nauc_ndcg_at_20_diff1
      value: 47.354286045074815
    - type: nauc_ndcg_at_20_max
      value: 33.686648806027975
    - type: nauc_ndcg_at_20_std
      value: -3.0189085132476556
    - type: nauc_ndcg_at_3_diff1
      value: 49.68805334316908
    - type: nauc_ndcg_at_3_max
      value: 34.196077748056496
    - type: nauc_ndcg_at_3_std
      value: -2.7167289163768436
    - type: nauc_ndcg_at_5_diff1
      value: 47.94474868912989
    - type: nauc_ndcg_at_5_max
      value: 34.00261603413051
    - type: nauc_ndcg_at_5_std
      value: -3.3541028103046115
    - type: nauc_precision_at_1000_diff1
      value: -12.0150100710755
    - type: nauc_precision_at_1000_max
      value: 5.332942816568796
    - type: nauc_precision_at_1000_std
      value: 14.543288479130458
    - type: nauc_precision_at_100_diff1
      value: -4.920332181588838
    - type: nauc_precision_at_100_max
      value: 14.42313332017491
    - type: nauc_precision_at_100_std
      value: 17.821953321018384
    - type: nauc_precision_at_10_diff1
      value: 14.70509089079217
    - type: nauc_precision_at_10_max
      value: 25.381887131649716
    - type: nauc_precision_at_10_std
      value: 5.226419288645675
    - type: nauc_precision_at_1_diff1
      value: 52.23915787290734
    - type: nauc_precision_at_1_max
      value: 34.393531787632334
    - type: nauc_precision_at_1_std
      value: -1.452007661016969
    - type: nauc_precision_at_20_diff1
      value: 6.312827641507564
    - type: nauc_precision_at_20_max
      value: 22.483038562271933
    - type: nauc_precision_at_20_std
      value: 11.368419856892416
    - type: nauc_precision_at_3_diff1
      value: 33.271443420273606
    - type: nauc_precision_at_3_max
      value: 33.571078182106675
    - type: nauc_precision_at_3_std
      value: 4.47382265155717
    - type: nauc_precision_at_5_diff1
      value: 23.43287104284656
    - type: nauc_precision_at_5_max
      value: 30.909085068105313
    - type: nauc_precision_at_5_std
      value: 5.545672049452433
    - type: nauc_recall_at_1000_diff1
      value: 35.22615594677707
    - type: nauc_recall_at_1000_max
      value: 52.0710533173532
    - type: nauc_recall_at_1000_std
      value: 45.17683523786464
    - type: nauc_recall_at_100_diff1
      value: 36.2169056956332
    - type: nauc_recall_at_100_max
      value: 35.02435003210817
    - type: nauc_recall_at_100_std
      value: 15.833632946282508
    - type: nauc_recall_at_10_diff1
      value: 39.12440292974848
    - type: nauc_recall_at_10_max
      value: 28.0546011979648
    - type: nauc_recall_at_10_std
      value: -9.620558638092172
    - type: nauc_recall_at_1_diff1
      value: 53.98646767288695
    - type: nauc_recall_at_1_max
      value: 29.45629077638936
    - type: nauc_recall_at_1_std
      value: -5.621187380771589
    - type: nauc_recall_at_20_diff1
      value: 36.39254630768161
    - type: nauc_recall_at_20_max
      value: 29.277856508751967
    - type: nauc_recall_at_20_std
      value: -3.048007490798412
    - type: nauc_recall_at_3_diff1
      value: 45.64706642644958
    - type: nauc_recall_at_3_max
      value: 31.003050159737413
    - type: nauc_recall_at_3_std
      value: -4.849763876930667
    - type: nauc_recall_at_5_diff1
      value: 40.918108859971746
    - type: nauc_recall_at_5_max
      value: 30.69907335071493
    - type: nauc_recall_at_5_std
      value: -6.1445436251916865
    - type: ndcg_at_1
      value: 40.327
    - type: ndcg_at_10
      value: 49.675000000000004
    - type: ndcg_at_100
      value: 55.364000000000004
    - type: ndcg_at_1000
      value: 56.992
    - type: ndcg_at_20
      value: 51.803999999999995
    - type: ndcg_at_3
      value: 45.227000000000004
    - type: ndcg_at_5
      value: 47.244
    - type: precision_at_1
      value: 40.327
    - type: precision_at_10
      value: 8.826
    - type: precision_at_100
      value: 1.354
    - type: precision_at_1000
      value: 0.167
    - type: precision_at_20
      value: 5.115
    - type: precision_at_3
      value: 21.303
    - type: precision_at_5
      value: 14.726
    - type: recall_at_1
      value: 33.178999999999995
    - type: recall_at_10
      value: 61.087
    - type: recall_at_100
      value: 85.099
    - type: recall_at_1000
      value: 95.14099999999999
    - type: recall_at_20
      value: 68.623
    - type: recall_at_3
      value: 48.245
    - type: recall_at_5
      value: 53.832
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackProgrammersRetrieval
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
      split: test
      type: mteb/cqadupstack-programmers
    metrics:
    - type: main_score
      value: 44.99
    - type: map_at_1
      value: 28.089
    - type: map_at_10
      value: 38.98
    - type: map_at_100
      value: 40.339000000000006
    - type: map_at_1000
      value: 40.441
    - type: map_at_20
      value: 39.702
    - type: map_at_3
      value: 35.620000000000005
    - type: map_at_5
      value: 37.657000000000004
    - type: mrr_at_1
      value: 35.15981735159817
    - type: mrr_at_10
      value: 44.54075161266937
    - type: mrr_at_100
      value: 45.435730392436646
    - type: mrr_at_1000
      value: 45.47673849356812
    - type: mrr_at_20
      value: 45.05949613726918
    - type: mrr_at_3
      value: 42.00913242009131
    - type: mrr_at_5
      value: 43.52739726027392
    - type: nauc_map_at_1000_diff1
      value: 42.6375513442399
    - type: nauc_map_at_1000_max
      value: 35.83899956589522
    - type: nauc_map_at_1000_std
      value: 5.798620017712549
    - type: nauc_map_at_100_diff1
      value: 42.609712253881504
    - type: nauc_map_at_100_max
      value: 35.85401871065736
    - type: nauc_map_at_100_std
      value: 5.829007296755533
    - type: nauc_map_at_10_diff1
      value: 42.90931172127824
    - type: nauc_map_at_10_max
      value: 35.46694204511423
    - type: nauc_map_at_10_std
      value: 5.131477704152026
    - type: nauc_map_at_1_diff1
      value: 48.066312177855956
    - type: nauc_map_at_1_max
      value: 30.67745267941573
    - type: nauc_map_at_1_std
      value: -1.4170737991670943
    - type: nauc_map_at_20_diff1
      value: 42.730423700784
    - type: nauc_map_at_20_max
      value: 35.710039616497085
    - type: nauc_map_at_20_std
      value: 5.363961887475162
    - type: nauc_map_at_3_diff1
      value: 43.499223646579935
    - type: nauc_map_at_3_max
      value: 33.872570039621564
    - type: nauc_map_at_3_std
      value: 3.0787571843453008
    - type: nauc_map_at_5_diff1
      value: 43.28963642946521
    - type: nauc_map_at_5_max
      value: 35.18327408279892
    - type: nauc_map_at_5_std
      value: 4.516467154662473
    - type: nauc_mrr_at_1000_diff1
      value: 42.71279871641341
    - type: nauc_mrr_at_1000_max
      value: 37.48825064817496
    - type: nauc_mrr_at_1000_std
      value: 8.10015025024314
    - type: nauc_mrr_at_100_diff1
      value: 42.694777404773376
    - type: nauc_mrr_at_100_max
      value: 37.476741768741086
    - type: nauc_mrr_at_100_std
      value: 8.11525130417229
    - type: nauc_mrr_at_10_diff1
      value: 42.954194054560176
    - type: nauc_mrr_at_10_max
      value: 37.606138578797506
    - type: nauc_mrr_at_10_std
      value: 8.092519513302399
    - type: nauc_mrr_at_1_diff1
      value: 48.350790286038574
    - type: nauc_mrr_at_1_max
      value: 33.97992759739641
    - type: nauc_mrr_at_1_std
      value: 1.8332987018664093
    - type: nauc_mrr_at_20_diff1
      value: 42.664983701783044
    - type: nauc_mrr_at_20_max
      value: 37.47450702110784
    - type: nauc_mrr_at_20_std
      value: 8.001067634745462
    - type: nauc_mrr_at_3_diff1
      value: 42.921968602737955
    - type: nauc_mrr_at_3_max
      value: 37.19599728791262
    - type: nauc_mrr_at_3_std
      value: 7.4692697422507575
    - type: nauc_mrr_at_5_diff1
      value: 42.96028546491891
    - type: nauc_mrr_at_5_max
      value: 37.688350071295915
    - type: nauc_mrr_at_5_std
      value: 8.213017954012372
    - type: nauc_ndcg_at_1000_diff1
      value: 40.70763263942397
    - type: nauc_ndcg_at_1000_max
      value: 37.87768319167602
    - type: nauc_ndcg_at_1000_std
      value: 9.908807071686738
    - type: nauc_ndcg_at_100_diff1
      value: 39.97828438221707
    - type: nauc_ndcg_at_100_max
      value: 37.7723393835996
    - type: nauc_ndcg_at_100_std
      value: 10.666779466040097
    - type: nauc_ndcg_at_10_diff1
      value: 41.172233451172936
    - type: nauc_ndcg_at_10_max
      value: 37.12252131573939
    - type: nauc_ndcg_at_10_std
      value: 8.273798754436639
    - type: nauc_ndcg_at_1_diff1
      value: 48.350790286038574
    - type: nauc_ndcg_at_1_max
      value: 33.97992759739641
    - type: nauc_ndcg_at_1_std
      value: 1.8332987018664093
    - type: nauc_ndcg_at_20_diff1
      value: 40.33325895172716
    - type: nauc_ndcg_at_20_max
      value: 37.36015594019951
    - type: nauc_ndcg_at_20_std
      value: 8.818556108749302
    - type: nauc_ndcg_at_3_diff1
      value: 41.652701699747254
    - type: nauc_ndcg_at_3_max
      value: 35.499109874223294
    - type: nauc_ndcg_at_3_std
      value: 5.831784865606119
    - type: nauc_ndcg_at_5_diff1
      value: 41.856346892595475
    - type: nauc_ndcg_at_5_max
      value: 36.940681835687194
    - type: nauc_ndcg_at_5_std
      value: 7.507798515093516
    - type: nauc_precision_at_1000_diff1
      value: -2.4605367806784866
    - type: nauc_precision_at_1000_max
      value: -0.3538142127162922
    - type: nauc_precision_at_1000_std
      value: 8.369794961833236
    - type: nauc_precision_at_100_diff1
      value: -0.34954522096524704
    - type: nauc_precision_at_100_max
      value: 13.159909603146458
    - type: nauc_precision_at_100_std
      value: 19.425561514133996
    - type: nauc_precision_at_10_diff1
      value: 17.048304710148145
    - type: nauc_precision_at_10_max
      value: 29.816041846806375
    - type: nauc_precision_at_10_std
      value: 18.358893367243798
    - type: nauc_precision_at_1_diff1
      value: 48.350790286038574
    - type: nauc_precision_at_1_max
      value: 33.97992759739641
    - type: nauc_precision_at_1_std
      value: 1.8332987018664093
    - type: nauc_precision_at_20_diff1
      value: 10.450903599411344
    - type: nauc_precision_at_20_max
      value: 25.228916373799127
    - type: nauc_precision_at_20_std
      value: 18.46893569529936
    - type: nauc_precision_at_3_diff1
      value: 29.181236567048636
    - type: nauc_precision_at_3_max
      value: 35.64918262500281
    - type: nauc_precision_at_3_std
      value: 13.347538222514968
    - type: nauc_precision_at_5_diff1
      value: 23.693323840550345
    - type: nauc_precision_at_5_max
      value: 33.972399735191225
    - type: nauc_precision_at_5_std
      value: 17.107012760554618
    - type: nauc_recall_at_1000_diff1
      value: 20.297340483227945
    - type: nauc_recall_at_1000_max
      value: 63.084305970127275
    - type: nauc_recall_at_1000_std
      value: 63.04655000858784
    - type: nauc_recall_at_100_diff1
      value: 22.587332148979723
    - type: nauc_recall_at_100_max
      value: 40.740968468024775
    - type: nauc_recall_at_100_std
      value: 34.120423684507124
    - type: nauc_recall_at_10_diff1
      value: 33.361195948673675
    - type: nauc_recall_at_10_max
      value: 37.1411402410262
    - type: nauc_recall_at_10_std
      value: 13.475407196166259
    - type: nauc_recall_at_1_diff1
      value: 48.066312177855956
    - type: nauc_recall_at_1_max
      value: 30.67745267941573
    - type: nauc_recall_at_1_std
      value: -1.4170737991670943
    - type: nauc_recall_at_20_diff1
      value: 28.703982984383984
    - type: nauc_recall_at_20_max
      value: 37.32929431193496
    - type: nauc_recall_at_20_std
      value: 16.139135347989903
    - type: nauc_recall_at_3_diff1
      value: 36.53346179134789
    - type: nauc_recall_at_3_max
      value: 34.11397914899309
    - type: nauc_recall_at_3_std
      value: 7.19358019807132
    - type: nauc_recall_at_5_diff1
      value: 36.24058894947452
    - type: nauc_recall_at_5_max
      value: 37.00990358651097
    - type: nauc_recall_at_5_std
      value: 11.074645476821619
    - type: ndcg_at_1
      value: 35.160000000000004
    - type: ndcg_at_10
      value: 44.99
    - type: ndcg_at_100
      value: 50.661
    - type: ndcg_at_1000
      value: 52.599
    - type: ndcg_at_20
      value: 47.154
    - type: ndcg_at_3
      value: 39.843
    - type: ndcg_at_5
      value: 42.486000000000004
    - type: precision_at_1
      value: 35.160000000000004
    - type: precision_at_10
      value: 8.299
    - type: precision_at_100
      value: 1.2850000000000001
    - type: precision_at_1000
      value: 0.16199999999999998
    - type: precision_at_20
      value: 4.84
    - type: precision_at_3
      value: 19.178
    - type: precision_at_5
      value: 13.927
    - type: recall_at_1
      value: 28.089
    - type: recall_at_10
      value: 57.158
    - type: recall_at_100
      value: 81.461
    - type: recall_at_1000
      value: 94.46900000000001
    - type: recall_at_20
      value: 64.927
    - type: recall_at_3
      value: 42.775999999999996
    - type: recall_at_5
      value: 49.719
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval
      revision: CQADupstackRetrieval is a combined dataset
      split: test
      type: mteb/cqadupstack
    metrics:
    - type: main_score
      value: 44.989166666666655
    - type: ndcg_at_10
      value: 44.989166666666655
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackStatsRetrieval
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
      split: test
      type: mteb/cqadupstack-stats
    metrics:
    - type: main_score
      value: 39.586
    - type: map_at_1
      value: 27.301
    - type: map_at_10
      value: 35.022
    - type: map_at_100
      value: 36.061
    - type: map_at_1000
      value: 36.146
    - type: map_at_20
      value: 35.608000000000004
    - type: map_at_3
      value: 32.978
    - type: map_at_5
      value: 33.994
    - type: mrr_at_1
      value: 30.67484662576687
    - type: mrr_at_10
      value: 38.1696124257474
    - type: mrr_at_100
      value: 38.99730898994137
    - type: mrr_at_1000
      value: 39.049871007408136
    - type: mrr_at_20
      value: 38.62424051396064
    - type: mrr_at_3
      value: 36.40081799591004
    - type: mrr_at_5
      value: 37.23670756646219
    - type: nauc_map_at_1000_diff1
      value: 50.4395097150819
    - type: nauc_map_at_1000_max
      value: 42.36231476768413
    - type: nauc_map_at_1000_std
      value: 1.0739414045485742
    - type: nauc_map_at_100_diff1
      value: 50.4253775421283
    - type: nauc_map_at_100_max
      value: 42.34508969348633
    - type: nauc_map_at_100_std
      value: 1.0590256535050135
    - type: nauc_map_at_10_diff1
      value: 50.74196619464362
    - type: nauc_map_at_10_max
      value: 42.354326434590284
    - type: nauc_map_at_10_std
      value: 0.6330167542705694
    - type: nauc_map_at_1_diff1
      value: 55.7404810490963
    - type: nauc_map_at_1_max
      value: 40.7676941648045
    - type: nauc_map_at_1_std
      value: -5.021772566610674
    - type: nauc_map_at_20_diff1
      value: 50.39792463598886
    - type: nauc_map_at_20_max
      value: 42.25768760228577
    - type: nauc_map_at_20_std
      value: 0.8979017700131807
    - type: nauc_map_at_3_diff1
      value: 51.53267996170815
    - type: nauc_map_at_3_max
      value: 41.78801756883417
    - type: nauc_map_at_3_std
      value: -0.6652383024396911
    - type: nauc_map_at_5_diff1
      value: 50.992783683271504
    - type: nauc_map_at_5_max
      value: 41.8607977828188
    - type: nauc_map_at_5_std
      value: 0.3484379897869807
    - type: nauc_mrr_at_1000_diff1
      value: 48.952907124445126
    - type: nauc_mrr_at_1000_max
      value: 42.93563741482114
    - type: nauc_mrr_at_1000_std
      value: 3.0791495753556424
    - type: nauc_mrr_at_100_diff1
      value: 48.941921107360805
    - type: nauc_mrr_at_100_max
      value: 42.94419657374061
    - type: nauc_mrr_at_100_std
      value: 3.075397087180154
    - type: nauc_mrr_at_10_diff1
      value: 49.098926306303056
    - type: nauc_mrr_at_10_max
      value: 42.941857820499806
    - type: nauc_mrr_at_10_std
      value: 2.8184474174054372
    - type: nauc_mrr_at_1_diff1
      value: 54.428109877009334
    - type: nauc_mrr_at_1_max
      value: 42.50273386972492
    - type: nauc_mrr_at_1_std
      value: -2.1811826216412187
    - type: nauc_mrr_at_20_diff1
      value: 48.82502192775839
    - type: nauc_mrr_at_20_max
      value: 42.92227277257095
    - type: nauc_mrr_at_20_std
      value: 2.975812634368533
    - type: nauc_mrr_at_3_diff1
      value: 49.440009227591176
    - type: nauc_mrr_at_3_max
      value: 42.95503176290712
    - type: nauc_mrr_at_3_std
      value: 2.2997128945013796
    - type: nauc_mrr_at_5_diff1
      value: 49.09846782701398
    - type: nauc_mrr_at_5_max
      value: 42.51449168285772
    - type: nauc_mrr_at_5_std
      value: 2.7785816484421297
    - type: nauc_ndcg_at_1000_diff1
      value: 48.14680758187888
    - type: nauc_ndcg_at_1000_max
      value: 43.57465718500695
    - type: nauc_ndcg_at_1000_std
      value: 5.287435676678261
    - type: nauc_ndcg_at_100_diff1
      value: 47.66081605743284
    - type: nauc_ndcg_at_100_max
      value: 43.28156751251163
    - type: nauc_ndcg_at_100_std
      value: 4.959626409663624
    - type: nauc_ndcg_at_10_diff1
      value: 48.25075619623878
    - type: nauc_ndcg_at_10_max
      value: 43.00688660666578
    - type: nauc_ndcg_at_10_std
      value: 3.2319193368891637
    - type: nauc_ndcg_at_1_diff1
      value: 54.428109877009334
    - type: nauc_ndcg_at_1_max
      value: 42.50273386972492
    - type: nauc_ndcg_at_1_std
      value: -2.1811826216412187
    - type: nauc_ndcg_at_20_diff1
      value: 47.1943098627403
    - type: nauc_ndcg_at_20_max
      value: 42.86954491768707
    - type: nauc_ndcg_at_20_std
      value: 4.08583080150737
    - type: nauc_ndcg_at_3_diff1
      value: 49.32681523192246
    - type: nauc_ndcg_at_3_max
      value: 42.46898641470274
    - type: nauc_ndcg_at_3_std
      value: 1.7416962407725236
    - type: nauc_ndcg_at_5_diff1
      value: 48.59647012439291
    - type: nauc_ndcg_at_5_max
      value: 42.07098889846439
    - type: nauc_ndcg_at_5_std
      value: 2.979621233356828
    - type: nauc_precision_at_1000_diff1
      value: -1.7366334161587105
    - type: nauc_precision_at_1000_max
      value: 17.70969166396819
    - type: nauc_precision_at_1000_std
      value: 17.50619975322144
    - type: nauc_precision_at_100_diff1
      value: 10.082579982582155
    - type: nauc_precision_at_100_max
      value: 28.024893516091776
    - type: nauc_precision_at_100_std
      value: 18.41413013357596
    - type: nauc_precision_at_10_diff1
      value: 28.796167732373657
    - type: nauc_precision_at_10_max
      value: 40.37340024485382
    - type: nauc_precision_at_10_std
      value: 13.718572711091733
    - type: nauc_precision_at_1_diff1
      value: 54.428109877009334
    - type: nauc_precision_at_1_max
      value: 42.50273386972492
    - type: nauc_precision_at_1_std
      value: -2.1811826216412187
    - type: nauc_precision_at_20_diff1
      value: 19.82691920771315
    - type: nauc_precision_at_20_max
      value: 34.45075390159975
    - type: nauc_precision_at_20_std
      value: 16.410812072348058
    - type: nauc_precision_at_3_diff1
      value: 40.85430254962678
    - type: nauc_precision_at_3_max
      value: 43.63016056067074
    - type: nauc_precision_at_3_std
      value: 9.322014634477581
    - type: nauc_precision_at_5_diff1
      value: 35.830272848975795
    - type: nauc_precision_at_5_max
      value: 41.30047691620363
    - type: nauc_precision_at_5_std
      value: 13.145693992266565
    - type: nauc_recall_at_1000_diff1
      value: 35.532000545890504
    - type: nauc_recall_at_1000_max
      value: 50.714223194510325
    - type: nauc_recall_at_1000_std
      value: 43.09037309139045
    - type: nauc_recall_at_100_diff1
      value: 35.11024488875192
    - type: nauc_recall_at_100_max
      value: 43.0874566265193
    - type: nauc_recall_at_100_std
      value: 19.70628521846854
    - type: nauc_recall_at_10_diff1
      value: 40.36203726741153
    - type: nauc_recall_at_10_max
      value: 42.581482582576726
    - type: nauc_recall_at_10_std
      value: 8.642553371022348
    - type: nauc_recall_at_1_diff1
      value: 55.7404810490963
    - type: nauc_recall_at_1_max
      value: 40.7676941648045
    - type: nauc_recall_at_1_std
      value: -5.021772566610674
    - type: nauc_recall_at_20_diff1
      value: 35.97348868186562
    - type: nauc_recall_at_20_max
      value: 41.82695933305065
    - type: nauc_recall_at_20_std
      value: 11.444957541593585
    - type: nauc_recall_at_3_diff1
      value: 44.20020470014979
    - type: nauc_recall_at_3_max
      value: 40.84130855296979
    - type: nauc_recall_at_3_std
      value: 5.004883338558809
    - type: nauc_recall_at_5_diff1
      value: 42.08756885472078
    - type: nauc_recall_at_5_max
      value: 39.90323783606852
    - type: nauc_recall_at_5_std
      value: 8.085182534171127
    - type: ndcg_at_1
      value: 30.675
    - type: ndcg_at_10
      value: 39.586
    - type: ndcg_at_100
      value: 44.737
    - type: ndcg_at_1000
      value: 46.863
    - type: ndcg_at_20
      value: 41.495
    - type: ndcg_at_3
      value: 35.8
    - type: ndcg_at_5
      value: 37.3
    - type: precision_at_1
      value: 30.675
    - type: precision_at_10
      value: 6.196
    - type: precision_at_100
      value: 0.9570000000000001
    - type: precision_at_1000
      value: 0.122
    - type: precision_at_20
      value: 3.6350000000000002
    - type: precision_at_3
      value: 15.337
    - type: precision_at_5
      value: 10.337
    - type: recall_at_1
      value: 27.301
    - type: recall_at_10
      value: 50.346999999999994
    - type: recall_at_100
      value: 74.459
    - type: recall_at_1000
      value: 90.018
    - type: recall_at_20
      value: 57.473
    - type: recall_at_3
      value: 39.672000000000004
    - type: recall_at_5
      value: 43.383
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackTexRetrieval
      revision: 46989137a86843e03a6195de44b09deda022eec7
      split: test
      type: mteb/cqadupstack-tex
    metrics:
    - type: main_score
      value: 32.842
    - type: map_at_1
      value: 19.527
    - type: map_at_10
      value: 27.711999999999996
    - type: map_at_100
      value: 28.98
    - type: map_at_1000
      value: 29.108
    - type: map_at_20
      value: 28.407
    - type: map_at_3
      value: 25.023
    - type: map_at_5
      value: 26.528000000000002
    - type: mrr_at_1
      value: 23.675154852030282
    - type: mrr_at_10
      value: 31.810676323752784
    - type: mrr_at_100
      value: 32.788970614380716
    - type: mrr_at_1000
      value: 32.86028758975889
    - type: mrr_at_20
      value: 32.35935756676056
    - type: mrr_at_3
      value: 29.41615049323246
    - type: mrr_at_5
      value: 30.785730672172633
    - type: nauc_map_at_1000_diff1
      value: 35.597766688968015
    - type: nauc_map_at_1000_max
      value: 26.295790183159845
    - type: nauc_map_at_1000_std
      value: -0.04229904865958209
    - type: nauc_map_at_100_diff1
      value: 35.568782622469925
    - type: nauc_map_at_100_max
      value: 26.27850795471227
    - type: nauc_map_at_100_std
      value: -0.04944875782811099
    - type: nauc_map_at_10_diff1
      value: 35.63760937893694
    - type: nauc_map_at_10_max
      value: 26.130094042028233
    - type: nauc_map_at_10_std
      value: -0.6896882769027717
    - type: nauc_map_at_1_diff1
      value: 41.759098341890976
    - type: nauc_map_at_1_max
      value: 23.918885427783326
    - type: nauc_map_at_1_std
      value: -2.1383574897865074
    - type: nauc_map_at_20_diff1
      value: 35.55706530442612
    - type: nauc_map_at_20_max
      value: 26.23339626569677
    - type: nauc_map_at_20_std
      value: -0.162172033918129
    - type: nauc_map_at_3_diff1
      value: 37.22183376355153
    - type: nauc_map_at_3_max
      value: 25.770512522122186
    - type: nauc_map_at_3_std
      value: -1.3105892187778403
    - type: nauc_map_at_5_diff1
      value: 36.205913161663084
    - type: nauc_map_at_5_max
      value: 25.953300641502064
    - type: nauc_map_at_5_std
      value: -0.7987363137547906
    - type: nauc_mrr_at_1000_diff1
      value: 34.864016559617646
    - type: nauc_mrr_at_1000_max
      value: 26.8689525348564
    - type: nauc_mrr_at_1000_std
      value: -0.5839923973914446
    - type: nauc_mrr_at_100_diff1
      value: 34.83820469598538
    - type: nauc_mrr_at_100_max
      value: 26.864669056231282
    - type: nauc_mrr_at_100_std
      value: -0.5785645654158633
    - type: nauc_mrr_at_10_diff1
      value: 34.81868397381981
    - type: nauc_mrr_at_10_max
      value: 26.79988560460627
    - type: nauc_mrr_at_10_std
      value: -1.1113808365827318
    - type: nauc_mrr_at_1_diff1
      value: 40.0281507903504
    - type: nauc_mrr_at_1_max
      value: 25.036735941806583
    - type: nauc_mrr_at_1_std
      value: -2.508700799268523
    - type: nauc_mrr_at_20_diff1
      value: 34.81954537357966
    - type: nauc_mrr_at_20_max
      value: 26.877673033315453
    - type: nauc_mrr_at_20_std
      value: -0.6706028107452919
    - type: nauc_mrr_at_3_diff1
      value: 35.87313782549696
    - type: nauc_mrr_at_3_max
      value: 26.776261693392335
    - type: nauc_mrr_at_3_std
      value: -1.8010591328112908
    - type: nauc_mrr_at_5_diff1
      value: 35.31673912159536
    - type: nauc_mrr_at_5_max
      value: 26.78720786106881
    - type: nauc_mrr_at_5_std
      value: -1.3096326953900546
    - type: nauc_ndcg_at_1000_diff1
      value: 33.43105244339048
    - type: nauc_ndcg_at_1000_max
      value: 27.52195065724684
    - type: nauc_ndcg_at_1000_std
      value: 2.8376056562675744
    - type: nauc_ndcg_at_100_diff1
      value: 32.90916846420573
    - type: nauc_ndcg_at_100_max
      value: 27.27161017736065
    - type: nauc_ndcg_at_100_std
      value: 2.8703122625872126
    - type: nauc_ndcg_at_10_diff1
      value: 33.12714979317447
    - type: nauc_ndcg_at_10_max
      value: 26.67762031747992
    - type: nauc_ndcg_at_10_std
      value: -0.1341345572932233
    - type: nauc_ndcg_at_1_diff1
      value: 40.0281507903504
    - type: nauc_ndcg_at_1_max
      value: 25.036735941806583
    - type: nauc_ndcg_at_1_std
      value: -2.508700799268523
    - type: nauc_ndcg_at_20_diff1
      value: 32.891656138688546
    - type: nauc_ndcg_at_20_max
      value: 26.991976404027163
    - type: nauc_ndcg_at_20_std
      value: 1.6050741106677746
    - type: nauc_ndcg_at_3_diff1
      value: 35.576958713955484
    - type: nauc_ndcg_at_3_max
      value: 26.41687745899445
    - type: nauc_ndcg_at_3_std
      value: -1.5326687067002291
    - type: nauc_ndcg_at_5_diff1
      value: 34.27335619067276
    - type: nauc_ndcg_at_5_max
      value: 26.479515412084208
    - type: nauc_ndcg_at_5_std
      value: -0.5597648935666003
    - type: nauc_precision_at_1000_diff1
      value: -0.18660914306684007
    - type: nauc_precision_at_1000_max
      value: 7.268255385799229
    - type: nauc_precision_at_1000_std
      value: -0.1968875268478991
    - type: nauc_precision_at_100_diff1
      value: 7.386701205054449
    - type: nauc_precision_at_100_max
      value: 15.477735603019607
    - type: nauc_precision_at_100_std
      value: 4.753153414679307
    - type: nauc_precision_at_10_diff1
      value: 18.4668296945938
    - type: nauc_precision_at_10_max
      value: 25.457144217779597
    - type: nauc_precision_at_10_std
      value: 0.40165373733963605
    - type: nauc_precision_at_1_diff1
      value: 40.0281507903504
    - type: nauc_precision_at_1_max
      value: 25.036735941806583
    - type: nauc_precision_at_1_std
      value: -2.508700799268523
    - type: nauc_precision_at_20_diff1
      value: 14.751135844289335
    - type: nauc_precision_at_20_max
      value: 22.763373329576293
    - type: nauc_precision_at_20_std
      value: 4.360731801761864
    - type: nauc_precision_at_3_diff1
      value: 28.154753888265393
    - type: nauc_precision_at_3_max
      value: 27.838427033527147
    - type: nauc_precision_at_3_std
      value: -1.0042621266717804
    - type: nauc_precision_at_5_diff1
      value: 23.549026872711423
    - type: nauc_precision_at_5_max
      value: 27.192214745385044
    - type: nauc_precision_at_5_std
      value: 0.4455206110174471
    - type: nauc_recall_at_1000_diff1
      value: 17.905404210815632
    - type: nauc_recall_at_1000_max
      value: 32.8674418535776
    - type: nauc_recall_at_1000_std
      value: 35.187050415735435
    - type: nauc_recall_at_100_diff1
      value: 20.903609751984757
    - type: nauc_recall_at_100_max
      value: 27.180306691518364
    - type: nauc_recall_at_100_std
      value: 17.553030959393297
    - type: nauc_recall_at_10_diff1
      value: 25.615147693464387
    - type: nauc_recall_at_10_max
      value: 25.97062699453565
    - type: nauc_recall_at_10_std
      value: 2.2181702899826576
    - type: nauc_recall_at_1_diff1
      value: 41.759098341890976
    - type: nauc_recall_at_1_max
      value: 23.918885427783326
    - type: nauc_recall_at_1_std
      value: -2.1383574897865074
    - type: nauc_recall_at_20_diff1
      value: 23.922775940094386
    - type: nauc_recall_at_20_max
      value: 26.384627814902785
    - type: nauc_recall_at_20_std
      value: 7.944532403561578
    - type: nauc_recall_at_3_diff1
      value: 32.26543270634743
    - type: nauc_recall_at_3_max
      value: 26.36357710828272
    - type: nauc_recall_at_3_std
      value: -0.42723331708340706
    - type: nauc_recall_at_5_diff1
      value: 29.080464141763336
    - type: nauc_recall_at_5_max
      value: 25.81238438303652
    - type: nauc_recall_at_5_std
      value: 1.1649311168287726
    - type: ndcg_at_1
      value: 23.674999999999997
    - type: ndcg_at_10
      value: 32.842
    - type: ndcg_at_100
      value: 38.64
    - type: ndcg_at_1000
      value: 41.367
    - type: ndcg_at_20
      value: 35.032999999999994
    - type: ndcg_at_3
      value: 28.166000000000004
    - type: ndcg_at_5
      value: 30.407
    - type: precision_at_1
      value: 23.674999999999997
    - type: precision_at_10
      value: 6.005
    - type: precision_at_100
      value: 1.053
    - type: precision_at_1000
      value: 0.146
    - type: precision_at_20
      value: 3.6580000000000004
    - type: precision_at_3
      value: 13.352
    - type: precision_at_5
      value: 9.718
    - type: recall_at_1
      value: 19.527
    - type: recall_at_10
      value: 44.096999999999994
    - type: recall_at_100
      value: 69.962
    - type: recall_at_1000
      value: 89.035
    - type: recall_at_20
      value: 52.166000000000004
    - type: recall_at_3
      value: 30.946
    - type: recall_at_5
      value: 36.789
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackUnixRetrieval
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
      split: test
      type: mteb/cqadupstack-unix
    metrics:
    - type: main_score
      value: 46.54
    - type: map_at_1
      value: 29.953999999999997
    - type: map_at_10
      value: 40.742
    - type: map_at_100
      value: 41.964
    - type: map_at_1000
      value: 42.059999999999995
    - type: map_at_20
      value: 41.426
    - type: map_at_3
      value: 37.378
    - type: map_at_5
      value: 39.267
    - type: mrr_at_1
      value: 34.701492537313435
    - type: mrr_at_10
      value: 44.29978085761664
    - type: mrr_at_100
      value: 45.205551401915486
    - type: mrr_at_1000
      value: 45.24735017384963
    - type: mrr_at_20
      value: 44.85338423755729
    - type: mrr_at_3
      value: 41.57338308457707
    - type: mrr_at_5
      value: 43.19185323383077
    - type: nauc_map_at_1000_diff1
      value: 48.45170522932164
    - type: nauc_map_at_1000_max
      value: 31.544164363591204
    - type: nauc_map_at_1000_std
      value: 0.8661088818146858
    - type: nauc_map_at_100_diff1
      value: 48.47347800061323
    - type: nauc_map_at_100_max
      value: 31.568637596620313
    - type: nauc_map_at_100_std
      value: 0.9252699336843858
    - type: nauc_map_at_10_diff1
      value: 48.64849891585432
    - type: nauc_map_at_10_max
      value: 31.40371265579746
    - type: nauc_map_at_10_std
      value: 0.7088016563713089
    - type: nauc_map_at_1_diff1
      value: 53.57918993108331
    - type: nauc_map_at_1_max
      value: 31.392632653740993
    - type: nauc_map_at_1_std
      value: -2.857306170463933
    - type: nauc_map_at_20_diff1
      value: 48.49084353023969
    - type: nauc_map_at_20_max
      value: 31.470313174779374
    - type: nauc_map_at_20_std
      value: 0.8950296035234309
    - type: nauc_map_at_3_diff1
      value: 49.273481161619806
    - type: nauc_map_at_3_max
      value: 31.101471509782826
    - type: nauc_map_at_3_std
      value: -0.886510096257905
    - type: nauc_map_at_5_diff1
      value: 48.85344288229106
    - type: nauc_map_at_5_max
      value: 31.32633663238284
    - type: nauc_map_at_5_std
      value: -0.44752909698881177
    - type: nauc_mrr_at_1000_diff1
      value: 46.27593166906613
    - type: nauc_mrr_at_1000_max
      value: 31.637594372116336
    - type: nauc_mrr_at_1000_std
      value: 0.8444917550670064
    - type: nauc_mrr_at_100_diff1
      value: 46.27161543033672
    - type: nauc_mrr_at_100_max
      value: 31.64330655339695
    - type: nauc_mrr_at_100_std
      value: 0.8717446416398773
    - type: nauc_mrr_at_10_diff1
      value: 46.100348481312864
    - type: nauc_mrr_at_10_max
      value: 31.594271897882237
    - type: nauc_mrr_at_10_std
      value: 0.8807168907688873
    - type: nauc_mrr_at_1_diff1
      value: 51.35163098909763
    - type: nauc_mrr_at_1_max
      value: 31.99084441327899
    - type: nauc_mrr_at_1_std
      value: -2.688594880742662
    - type: nauc_mrr_at_20_diff1
      value: 46.18178546174727
    - type: nauc_mrr_at_20_max
      value: 31.639111674119448
    - type: nauc_mrr_at_20_std
      value: 0.9855008641374622
    - type: nauc_mrr_at_3_diff1
      value: 46.307484835305864
    - type: nauc_mrr_at_3_max
      value: 31.35563850804847
    - type: nauc_mrr_at_3_std
      value: -0.3419536587707561
    - type: nauc_mrr_at_5_diff1
      value: 46.17646418781234
    - type: nauc_mrr_at_5_max
      value: 31.313474270239833
    - type: nauc_mrr_at_5_std
      value: -0.08656550526568331
    - type: nauc_ndcg_at_1000_diff1
      value: 46.12095795101613
    - type: nauc_ndcg_at_1000_max
      value: 31.989083597726314
    - type: nauc_ndcg_at_1000_std
      value: 3.2965704707660763
    - type: nauc_ndcg_at_100_diff1
      value: 46.05376249841318
    - type: nauc_ndcg_at_100_max
      value: 32.39195988574972
    - type: nauc_ndcg_at_100_std
      value: 4.518018135593347
    - type: nauc_ndcg_at_10_diff1
      value: 46.133631183744875
    - type: nauc_ndcg_at_10_max
      value: 31.45358876172339
    - type: nauc_ndcg_at_10_std
      value: 3.4254370918871055
    - type: nauc_ndcg_at_1_diff1
      value: 51.35163098909763
    - type: nauc_ndcg_at_1_max
      value: 31.99084441327899
    - type: nauc_ndcg_at_1_std
      value: -2.688594880742662
    - type: nauc_ndcg_at_20_diff1
      value: 45.94584949766954
    - type: nauc_ndcg_at_20_max
      value: 31.689777515111295
    - type: nauc_ndcg_at_20_std
      value: 4.189082428922442
    - type: nauc_ndcg_at_3_diff1
      value: 46.5057835389752
    - type: nauc_ndcg_at_3_max
      value: 30.941407592082047
    - type: nauc_ndcg_at_3_std
      value: -0.042473944857831535
    - type: nauc_ndcg_at_5_diff1
      value: 46.369027395136136
    - type: nauc_ndcg_at_5_max
      value: 31.057841776505352
    - type: nauc_ndcg_at_5_std
      value: 0.6878993420489522
    - type: nauc_precision_at_1000_diff1
      value: -17.30759714093202
    - type: nauc_precision_at_1000_max
      value: -4.441155558458858
    - type: nauc_precision_at_1000_std
      value: 1.5537300718220326
    - type: nauc_precision_at_100_diff1
      value: -7.18920438222021
    - type: nauc_precision_at_100_max
      value: 8.017878121399253
    - type: nauc_precision_at_100_std
      value: 11.357132919349102
    - type: nauc_precision_at_10_diff1
      value: 15.202451884794076
    - type: nauc_precision_at_10_max
      value: 19.077295902881417
    - type: nauc_precision_at_10_std
      value: 9.885526867355805
    - type: nauc_precision_at_1_diff1
      value: 51.35163098909763
    - type: nauc_precision_at_1_max
      value: 31.99084441327899
    - type: nauc_precision_at_1_std
      value: -2.688594880742662
    - type: nauc_precision_at_20_diff1
      value: 6.827461091494899
    - type: nauc_precision_at_20_max
      value: 15.27268633497114
    - type: nauc_precision_at_20_std
      value: 11.515826649647384
    - type: nauc_precision_at_3_diff1
      value: 31.043021807472027
    - type: nauc_precision_at_3_max
      value: 26.22457157531548
    - type: nauc_precision_at_3_std
      value: 1.788215968301994
    - type: nauc_precision_at_5_diff1
      value: 25.030185818513235
    - type: nauc_precision_at_5_max
      value: 23.680129160901537
    - type: nauc_precision_at_5_std
      value: 4.303018899688115
    - type: nauc_recall_at_1000_diff1
      value: 28.68826642607512
    - type: nauc_recall_at_1000_max
      value: 42.33849804103852
    - type: nauc_recall_at_1000_std
      value: 42.67413575876864
    - type: nauc_recall_at_100_diff1
      value: 36.51494878715
    - type: nauc_recall_at_100_max
      value: 37.4764995034434
    - type: nauc_recall_at_100_std
      value: 28.295671266661017
    - type: nauc_recall_at_10_diff1
      value: 39.416721111463524
    - type: nauc_recall_at_10_max
      value: 29.95985608454179
    - type: nauc_recall_at_10_std
      value: 12.423335839786201
    - type: nauc_recall_at_1_diff1
      value: 53.57918993108331
    - type: nauc_recall_at_1_max
      value: 31.392632653740993
    - type: nauc_recall_at_1_std
      value: -2.857306170463933
    - type: nauc_recall_at_20_diff1
      value: 38.228803480194046
    - type: nauc_recall_at_20_max
      value: 30.87261362975955
    - type: nauc_recall_at_20_std
      value: 16.977113091834095
    - type: nauc_recall_at_3_diff1
      value: 43.154348566653155
    - type: nauc_recall_at_3_max
      value: 29.54536633744803
    - type: nauc_recall_at_3_std
      value: 2.02842672250621
    - type: nauc_recall_at_5_diff1
      value: 41.00436246072242
    - type: nauc_recall_at_5_max
      value: 29.413569555348023
    - type: nauc_recall_at_5_std
      value: 3.845214021958289
    - type: ndcg_at_1
      value: 34.701
    - type: ndcg_at_10
      value: 46.54
    - type: ndcg_at_100
      value: 51.754999999999995
    - type: ndcg_at_1000
      value: 53.71
    - type: ndcg_at_20
      value: 48.679
    - type: ndcg_at_3
      value: 40.892
    - type: ndcg_at_5
      value: 43.595
    - type: precision_at_1
      value: 34.701
    - type: precision_at_10
      value: 8.004
    - type: precision_at_100
      value: 1.185
    - type: precision_at_1000
      value: 0.145
    - type: precision_at_20
      value: 4.632
    - type: precision_at_3
      value: 18.719
    - type: precision_at_5
      value: 13.245999999999999
    - type: recall_at_1
      value: 29.953999999999997
    - type: recall_at_10
      value: 60.246
    - type: recall_at_100
      value: 82.128
    - type: recall_at_1000
      value: 95.622
    - type: recall_at_20
      value: 67.756
    - type: recall_at_3
      value: 45.096000000000004
    - type: recall_at_5
      value: 51.9
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWebmastersRetrieval
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
      split: test
      type: mteb/cqadupstack-webmasters
    metrics:
    - type: main_score
      value: 44.718999999999994
    - type: map_at_1
      value: 28.383999999999997
    - type: map_at_10
      value: 38.422
    - type: map_at_100
      value: 40.058
    - type: map_at_1000
      value: 40.276
    - type: map_at_20
      value: 39.301
    - type: map_at_3
      value: 35.205
    - type: map_at_5
      value: 36.803999999999995
    - type: mrr_at_1
      value: 33.59683794466403
    - type: mrr_at_10
      value: 42.837536859275986
    - type: mrr_at_100
      value: 43.7501703455481
    - type: mrr_at_1000
      value: 43.79258407771123
    - type: mrr_at_20
      value: 43.36044710445095
    - type: mrr_at_3
      value: 40.15151515151516
    - type: mrr_at_5
      value: 41.74242424242425
    - type: nauc_map_at_1000_diff1
      value: 47.934826596875304
    - type: nauc_map_at_1000_max
      value: 32.39759438116062
    - type: nauc_map_at_1000_std
      value: 0.9489007346763054
    - type: nauc_map_at_100_diff1
      value: 47.94844822157888
    - type: nauc_map_at_100_max
      value: 32.51485845519537
    - type: nauc_map_at_100_std
      value: 0.8094339925545622
    - type: nauc_map_at_10_diff1
      value: 48.251456404874645
    - type: nauc_map_at_10_max
      value: 31.412906399154245
    - type: nauc_map_at_10_std
      value: -0.7024825737369933
    - type: nauc_map_at_1_diff1
      value: 55.81906101970174
    - type: nauc_map_at_1_max
      value: 31.811715334193796
    - type: nauc_map_at_1_std
      value: -6.17056859281584
    - type: nauc_map_at_20_diff1
      value: 47.80902650237369
    - type: nauc_map_at_20_max
      value: 32.22465403023091
    - type: nauc_map_at_20_std
      value: 0.20706526946705656
    - type: nauc_map_at_3_diff1
      value: 49.97333984346632
    - type: nauc_map_at_3_max
      value: 31.58195498640799
    - type: nauc_map_at_3_std
      value: -2.577539707727459
    - type: nauc_map_at_5_diff1
      value: 49.40005767350608
    - type: nauc_map_at_5_max
      value: 30.998435600377434
    - type: nauc_map_at_5_std
      value: -2.1231771618690307
    - type: nauc_mrr_at_1000_diff1
      value: 46.86811371969663
    - type: nauc_mrr_at_1000_max
      value: 31.25147138171024
    - type: nauc_mrr_at_1000_std
      value: 1.9954422477585918
    - type: nauc_mrr_at_100_diff1
      value: 46.855870345882195
    - type: nauc_mrr_at_100_max
      value: 31.263524035665966
    - type: nauc_mrr_at_100_std
      value: 2.0160751193806568
    - type: nauc_mrr_at_10_diff1
      value: 46.93294772825783
    - type: nauc_mrr_at_10_max
      value: 30.927002048701663
    - type: nauc_mrr_at_10_std
      value: 1.6538220080908224
    - type: nauc_mrr_at_1_diff1
      value: 52.416386548395664
    - type: nauc_mrr_at_1_max
      value: 32.28582003787206
    - type: nauc_mrr_at_1_std
      value: -2.154991145714492
    - type: nauc_mrr_at_20_diff1
      value: 46.71796185319694
    - type: nauc_mrr_at_20_max
      value: 31.16219902794994
    - type: nauc_mrr_at_20_std
      value: 1.8590646572728409
    - type: nauc_mrr_at_3_diff1
      value: 47.697100317669914
    - type: nauc_mrr_at_3_max
      value: 30.821806030159383
    - type: nauc_mrr_at_3_std
      value: 1.1927626358099177
    - type: nauc_mrr_at_5_diff1
      value: 47.065272061365704
    - type: nauc_mrr_at_5_max
      value: 30.299230962805023
    - type: nauc_mrr_at_5_std
      value: 1.3225842862629529
    - type: nauc_ndcg_at_1000_diff1
      value: 45.20612583136058
    - type: nauc_ndcg_at_1000_max
      value: 33.51931869947315
    - type: nauc_ndcg_at_1000_std
      value: 4.923707509620363
    - type: nauc_ndcg_at_100_diff1
      value: 44.76206243393775
    - type: nauc_ndcg_at_100_max
      value: 33.57771606755598
    - type: nauc_ndcg_at_100_std
      value: 5.30915563331338
    - type: nauc_ndcg_at_10_diff1
      value: 45.12714032463827
    - type: nauc_ndcg_at_10_max
      value: 30.351909495610492
    - type: nauc_ndcg_at_10_std
      value: 2.3972947289996873
    - type: nauc_ndcg_at_1_diff1
      value: 52.416386548395664
    - type: nauc_ndcg_at_1_max
      value: 32.28582003787206
    - type: nauc_ndcg_at_1_std
      value: -2.154991145714492
    - type: nauc_ndcg_at_20_diff1
      value: 44.20281844000005
    - type: nauc_ndcg_at_20_max
      value: 32.14112739396226
    - type: nauc_ndcg_at_20_std
      value: 3.3971385462591916
    - type: nauc_ndcg_at_3_diff1
      value: 47.0633767031858
    - type: nauc_ndcg_at_3_max
      value: 31.032896053733435
    - type: nauc_ndcg_at_3_std
      value: 0.6827544906310201
    - type: nauc_ndcg_at_5_diff1
      value: 46.735352294106484
    - type: nauc_ndcg_at_5_max
      value: 29.784992270528544
    - type: nauc_ndcg_at_5_std
      value: 0.8685943819516141
    - type: nauc_precision_at_1000_diff1
      value: -12.223330179860852
    - type: nauc_precision_at_1000_max
      value: -9.266492213777273
    - type: nauc_precision_at_1000_std
      value: 19.0569899587788
    - type: nauc_precision_at_100_diff1
      value: -5.803751085072067
    - type: nauc_precision_at_100_max
      value: 3.448932057044294
    - type: nauc_precision_at_100_std
      value: 23.470863527030627
    - type: nauc_precision_at_10_diff1
      value: 8.887357341361907
    - type: nauc_precision_at_10_max
      value: 18.67165390928126
    - type: nauc_precision_at_10_std
      value: 19.158543337955404
    - type: nauc_precision_at_1_diff1
      value: 52.416386548395664
    - type: nauc_precision_at_1_max
      value: 32.28582003787206
    - type: nauc_precision_at_1_std
      value: -2.154991145714492
    - type: nauc_precision_at_20_diff1
      value: 0.942496138409553
    - type: nauc_precision_at_20_max
      value: 18.86957127610774
    - type: nauc_precision_at_20_std
      value: 24.075503903246496
    - type: nauc_precision_at_3_diff1
      value: 28.15363877307106
    - type: nauc_precision_at_3_max
      value: 27.064928137991824
    - type: nauc_precision_at_3_std
      value: 8.632807104504753
    - type: nauc_precision_at_5_diff1
      value: 20.805862332497973
    - type: nauc_precision_at_5_max
      value: 21.420201475758404
    - type: nauc_precision_at_5_std
      value: 12.380239645425714
    - type: nauc_recall_at_1000_diff1
      value: 18.478341468055547
    - type: nauc_recall_at_1000_max
      value: 56.293560115074506
    - type: nauc_recall_at_1000_std
      value: 64.31607185065428
    - type: nauc_recall_at_100_diff1
      value: 26.737267337771886
    - type: nauc_recall_at_100_max
      value: 38.011889141496326
    - type: nauc_recall_at_100_std
      value: 30.44904690114732
    - type: nauc_recall_at_10_diff1
      value: 35.22772732735716
    - type: nauc_recall_at_10_max
      value: 26.000054115159486
    - type: nauc_recall_at_10_std
      value: 5.174264254271206
    - type: nauc_recall_at_1_diff1
      value: 55.81906101970174
    - type: nauc_recall_at_1_max
      value: 31.811715334193796
    - type: nauc_recall_at_1_std
      value: -6.17056859281584
    - type: nauc_recall_at_20_diff1
      value: 30.48493302415641
    - type: nauc_recall_at_20_max
      value: 31.05487040370753
    - type: nauc_recall_at_20_std
      value: 10.319948318834136
    - type: nauc_recall_at_3_diff1
      value: 43.12289512340243
    - type: nauc_recall_at_3_max
      value: 28.176279771026135
    - type: nauc_recall_at_3_std
      value: -0.1775154523381921
    - type: nauc_recall_at_5_diff1
      value: 40.9934933741234
    - type: nauc_recall_at_5_max
      value: 25.569156290584733
    - type: nauc_recall_at_5_std
      value: 0.21166696686855038
    - type: ndcg_at_1
      value: 33.597
    - type: ndcg_at_10
      value: 44.718999999999994
    - type: ndcg_at_100
      value: 50.324000000000005
    - type: ndcg_at_1000
      value: 52.468
    - type: ndcg_at_20
      value: 46.822
    - type: ndcg_at_3
      value: 39.558
    - type: ndcg_at_5
      value: 41.827999999999996
    - type: precision_at_1
      value: 33.597
    - type: precision_at_10
      value: 8.735
    - type: precision_at_100
      value: 1.6420000000000001
    - type: precision_at_1000
      value: 0.246
    - type: precision_at_20
      value: 5.375
    - type: precision_at_3
      value: 18.511
    - type: precision_at_5
      value: 13.399
    - type: recall_at_1
      value: 28.383999999999997
    - type: recall_at_10
      value: 56.425000000000004
    - type: recall_at_100
      value: 82.01899999999999
    - type: recall_at_1000
      value: 95.285
    - type: recall_at_20
      value: 64.615
    - type: recall_at_3
      value: 42.171
    - type: recall_at_5
      value: 48.296
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWordpressRetrieval
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
      split: test
      type: mteb/cqadupstack-wordpress
    metrics:
    - type: main_score
      value: 38.269999999999996
    - type: map_at_1
      value: 25.324999999999996
    - type: map_at_10
      value: 33.263
    - type: map_at_100
      value: 34.304
    - type: map_at_1000
      value: 34.394000000000005
    - type: map_at_20
      value: 33.827
    - type: map_at_3
      value: 30.259999999999998
    - type: map_at_5
      value: 31.832
    - type: mrr_at_1
      value: 27.171903881700555
    - type: mrr_at_10
      value: 35.334991051257234
    - type: mrr_at_100
      value: 36.251283465952355
    - type: mrr_at_1000
      value: 36.316236092511055
    - type: mrr_at_20
      value: 35.87141909945257
    - type: mrr_at_3
      value: 32.71719038817007
    - type: mrr_at_5
      value: 34.19593345656194
    - type: nauc_map_at_1000_diff1
      value: 39.614836211522714
    - type: nauc_map_at_1000_max
      value: 22.019768626310192
    - type: nauc_map_at_1000_std
      value: -1.5238708712112499
    - type: nauc_map_at_100_diff1
      value: 39.63008548572307
    - type: nauc_map_at_100_max
      value: 22.044756063752345
    - type: nauc_map_at_100_std
      value: -1.4869190221494792
    - type: nauc_map_at_10_diff1
      value: 39.73025012395569
    - type: nauc_map_at_10_max
      value: 22.117710178892107
    - type: nauc_map_at_10_std
      value: -2.5129984871932973
    - type: nauc_map_at_1_diff1
      value: 45.015617718902654
    - type: nauc_map_at_1_max
      value: 19.313800263189638
    - type: nauc_map_at_1_std
      value: -4.763931386681675
    - type: nauc_map_at_20_diff1
      value: 39.53678019013766
    - type: nauc_map_at_20_max
      value: 21.880316719428258
    - type: nauc_map_at_20_std
      value: -1.882003994523355
    - type: nauc_map_at_3_diff1
      value: 40.37307665298228
    - type: nauc_map_at_3_max
      value: 20.851976075322533
    - type: nauc_map_at_3_std
      value: -2.429569082966531
    - type: nauc_map_at_5_diff1
      value: 39.763015635086
    - type: nauc_map_at_5_max
      value: 22.010102196900725
    - type: nauc_map_at_5_std
      value: -2.654896415670943
    - type: nauc_mrr_at_1000_diff1
      value: 39.74071733680025
    - type: nauc_mrr_at_1000_max
      value: 21.67309640681989
    - type: nauc_mrr_at_1000_std
      value: -1.4003373135477462
    - type: nauc_mrr_at_100_diff1
      value: 39.730614151966485
    - type: nauc_mrr_at_100_max
      value: 21.678390048971767
    - type: nauc_mrr_at_100_std
      value: -1.3655362623563931
    - type: nauc_mrr_at_10_diff1
      value: 39.7900031013241
    - type: nauc_mrr_at_10_max
      value: 21.73643491725051
    - type: nauc_mrr_at_10_std
      value: -2.1175389838696312
    - type: nauc_mrr_at_1_diff1
      value: 46.165736140679776
    - type: nauc_mrr_at_1_max
      value: 20.071083446822147
    - type: nauc_mrr_at_1_std
      value: -5.018909100858311
    - type: nauc_mrr_at_20_diff1
      value: 39.6371295762885
    - type: nauc_mrr_at_20_max
      value: 21.659557440270973
    - type: nauc_mrr_at_20_std
      value: -1.4909603958341686
    - type: nauc_mrr_at_3_diff1
      value: 40.351150322758876
    - type: nauc_mrr_at_3_max
      value: 20.83706249041544
    - type: nauc_mrr_at_3_std
      value: -1.956027373253151
    - type: nauc_mrr_at_5_diff1
      value: 39.57759107791911
    - type: nauc_mrr_at_5_max
      value: 21.79552045204151
    - type: nauc_mrr_at_5_std
      value: -2.1507013120951126
    - type: nauc_ndcg_at_1000_diff1
      value: 37.717619356839016
    - type: nauc_ndcg_at_1000_max
      value: 22.545375504379805
    - type: nauc_ndcg_at_1000_std
      value: 1.682348628141016
    - type: nauc_ndcg_at_100_diff1
      value: 37.656027803682626
    - type: nauc_ndcg_at_100_max
      value: 22.49278246383637
    - type: nauc_ndcg_at_100_std
      value: 2.6818118152357773
    - type: nauc_ndcg_at_10_diff1
      value: 37.834954205539766
    - type: nauc_ndcg_at_10_max
      value: 22.655839885558443
    - type: nauc_ndcg_at_10_std
      value: -1.97159619786231
    - type: nauc_ndcg_at_1_diff1
      value: 46.165736140679776
    - type: nauc_ndcg_at_1_max
      value: 20.071083446822147
    - type: nauc_ndcg_at_1_std
      value: -5.018909100858311
    - type: nauc_ndcg_at_20_diff1
      value: 37.171914857454304
    - type: nauc_ndcg_at_20_max
      value: 21.858904801745897
    - type: nauc_ndcg_at_20_std
      value: 0.3809854859496657
    - type: nauc_ndcg_at_3_diff1
      value: 38.4460623883955
    - type: nauc_ndcg_at_3_max
      value: 20.95244159463402
    - type: nauc_ndcg_at_3_std
      value: -1.2685011660086651
    - type: nauc_ndcg_at_5_diff1
      value: 37.48831054573054
    - type: nauc_ndcg_at_5_max
      value: 22.625921624640526
    - type: nauc_ndcg_at_5_std
      value: -2.049221092724925
    - type: nauc_precision_at_1000_diff1
      value: -19.120500628263994
    - type: nauc_precision_at_1000_max
      value: -6.650707109047473
    - type: nauc_precision_at_1000_std
      value: 15.71193179253002
    - type: nauc_precision_at_100_diff1
      value: 6.254606806876069
    - type: nauc_precision_at_100_max
      value: 14.601826922181823
    - type: nauc_precision_at_100_std
      value: 28.38299592246453
    - type: nauc_precision_at_10_diff1
      value: 22.978614338670816
    - type: nauc_precision_at_10_max
      value: 23.04146766323557
    - type: nauc_precision_at_10_std
      value: 6.226264308612577
    - type: nauc_precision_at_1_diff1
      value: 46.165736140679776
    - type: nauc_precision_at_1_max
      value: 20.071083446822147
    - type: nauc_precision_at_1_std
      value: -5.018909100858311
    - type: nauc_precision_at_20_diff1
      value: 17.681032853225602
    - type: nauc_precision_at_20_max
      value: 18.66680304585122
    - type: nauc_precision_at_20_std
      value: 15.34896796713905
    - type: nauc_precision_at_3_diff1
      value: 31.359396694559194
    - type: nauc_precision_at_3_max
      value: 22.279263308973274
    - type: nauc_precision_at_3_std
      value: 3.6302537979529035
    - type: nauc_precision_at_5_diff1
      value: 26.32257879892933
    - type: nauc_precision_at_5_max
      value: 25.402524493181026
    - type: nauc_precision_at_5_std
      value: 4.731450603747359
    - type: nauc_recall_at_1000_diff1
      value: 23.562925244967875
    - type: nauc_recall_at_1000_max
      value: 30.737399333586797
    - type: nauc_recall_at_1000_std
      value: 34.19418935008663
    - type: nauc_recall_at_100_diff1
      value: 28.703574970574824
    - type: nauc_recall_at_100_max
      value: 22.448663600170278
    - type: nauc_recall_at_100_std
      value: 24.53297349042035
    - type: nauc_recall_at_10_diff1
      value: 31.73603907811882
    - type: nauc_recall_at_10_max
      value: 23.453183748640765
    - type: nauc_recall_at_10_std
      value: -1.8279054407176274
    - type: nauc_recall_at_1_diff1
      value: 45.015617718902654
    - type: nauc_recall_at_1_max
      value: 19.313800263189638
    - type: nauc_recall_at_1_std
      value: -4.763931386681675
    - type: nauc_recall_at_20_diff1
      value: 28.74169081866096
    - type: nauc_recall_at_20_max
      value: 20.035509169577324
    - type: nauc_recall_at_20_std
      value: 7.371615811227748
    - type: nauc_recall_at_3_diff1
      value: 34.09890157333362
    - type: nauc_recall_at_3_max
      value: 20.46565842748346
    - type: nauc_recall_at_3_std
      value: -0.4337283067447526
    - type: nauc_recall_at_5_diff1
      value: 30.974580787842402
    - type: nauc_recall_at_5_max
      value: 23.76379349487105
    - type: nauc_recall_at_5_std
      value: -1.8407515927979428
    - type: ndcg_at_1
      value: 27.172
    - type: ndcg_at_10
      value: 38.269999999999996
    - type: ndcg_at_100
      value: 43.338
    - type: ndcg_at_1000
      value: 45.594
    - type: ndcg_at_20
      value: 40.256
    - type: ndcg_at_3
      value: 32.673
    - type: ndcg_at_5
      value: 35.224
    - type: precision_at_1
      value: 27.172
    - type: precision_at_10
      value: 6.063000000000001
    - type: precision_at_100
      value: 0.9259999999999999
    - type: precision_at_1000
      value: 0.123
    - type: precision_at_20
      value: 3.5029999999999997
    - type: precision_at_3
      value: 13.74
    - type: precision_at_5
      value: 9.797
    - type: recall_at_1
      value: 25.324999999999996
    - type: recall_at_10
      value: 51.634
    - type: recall_at_100
      value: 74.687
    - type: recall_at_1000
      value: 91.412
    - type: recall_at_20
      value: 59.207
    - type: recall_at_3
      value: 36.678
    - type: recall_at_5
      value: 42.742999999999995
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ClimateFEVER
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
      split: test
      type: mteb/climate-fever
    metrics:
    - type: main_score
      value: 36.853
    - type: map_at_1
      value: 15.371000000000002
    - type: map_at_10
      value: 27.122
    - type: map_at_100
      value: 29.226000000000003
    - type: map_at_1000
      value: 29.409999999999997
    - type: map_at_20
      value: 28.274
    - type: map_at_3
      value: 22.431
    - type: map_at_5
      value: 24.877
    - type: mrr_at_1
      value: 34.13680781758958
    - type: mrr_at_10
      value: 47.265911793599145
    - type: mrr_at_100
      value: 48.028369995763846
    - type: mrr_at_1000
      value: 48.05317022537804
    - type: mrr_at_20
      value: 47.75785292259516
    - type: mrr_at_3
      value: 43.887079261672156
    - type: mrr_at_5
      value: 45.906623235613544
    - type: nauc_map_at_1000_diff1
      value: 24.949211292921547
    - type: nauc_map_at_1000_max
      value: 38.69844483304584
    - type: nauc_map_at_1000_std
      value: 18.336359440844753
    - type: nauc_map_at_100_diff1
      value: 24.8951732982492
    - type: nauc_map_at_100_max
      value: 38.65049158594052
    - type: nauc_map_at_100_std
      value: 18.28935278388095
    - type: nauc_map_at_10_diff1
      value: 24.606032216798273
    - type: nauc_map_at_10_max
      value: 38.00608351559887
    - type: nauc_map_at_10_std
      value: 16.61261615173358
    - type: nauc_map_at_1_diff1
      value: 30.83614944448221
    - type: nauc_map_at_1_max
      value: 33.757528532809
    - type: nauc_map_at_1_std
      value: 8.880622713261126
    - type: nauc_map_at_20_diff1
      value: 24.75491310922017
    - type: nauc_map_at_20_max
      value: 38.353679076398834
    - type: nauc_map_at_20_std
      value: 17.58637493443171
    - type: nauc_map_at_3_diff1
      value: 25.563085273287083
    - type: nauc_map_at_3_max
      value: 35.14515679047155
    - type: nauc_map_at_3_std
      value: 11.75594869817732
    - type: nauc_map_at_5_diff1
      value: 24.815807517691614
    - type: nauc_map_at_5_max
      value: 36.25905426665983
    - type: nauc_map_at_5_std
      value: 14.516391726180697
    - type: nauc_mrr_at_1000_diff1
      value: 27.948233427121274
    - type: nauc_mrr_at_1000_max
      value: 37.5893640945859
    - type: nauc_mrr_at_1000_std
      value: 19.588442449629763
    - type: nauc_mrr_at_100_diff1
      value: 27.947962345854037
    - type: nauc_mrr_at_100_max
      value: 37.60375479481945
    - type: nauc_mrr_at_100_std
      value: 19.614791576283793
    - type: nauc_mrr_at_10_diff1
      value: 27.882311310262136
    - type: nauc_mrr_at_10_max
      value: 37.58580968074054
    - type: nauc_mrr_at_10_std
      value: 19.49875186170201
    - type: nauc_mrr_at_1_diff1
      value: 28.017413073648477
    - type: nauc_mrr_at_1_max
      value: 32.87710191514022
    - type: nauc_mrr_at_1_std
      value: 14.04889142608459
    - type: nauc_mrr_at_20_diff1
      value: 27.89129925771968
    - type: nauc_mrr_at_20_max
      value: 37.6142863106945
    - type: nauc_mrr_at_20_std
      value: 19.645390143394163
    - type: nauc_mrr_at_3_diff1
      value: 27.99609559690795
    - type: nauc_mrr_at_3_max
      value: 36.87362332456197
    - type: nauc_mrr_at_3_std
      value: 18.598416821915333
    - type: nauc_mrr_at_5_diff1
      value: 27.68306089976716
    - type: nauc_mrr_at_5_max
      value: 37.12264485659723
    - type: nauc_mrr_at_5_std
      value: 19.18875305730564
    - type: nauc_ndcg_at_1000_diff1
      value: 25.736779186453777
    - type: nauc_ndcg_at_1000_max
      value: 41.93281139456004
    - type: nauc_ndcg_at_1000_std
      value: 25.179038422659993
    - type: nauc_ndcg_at_100_diff1
      value: 25.144796623848322
    - type: nauc_ndcg_at_100_max
      value: 41.72820916876173
    - type: nauc_ndcg_at_100_std
      value: 25.12851686850754
    - type: nauc_ndcg_at_10_diff1
      value: 24.321249191226652
    - type: nauc_ndcg_at_10_max
      value: 40.23711916935706
    - type: nauc_ndcg_at_10_std
      value: 20.89060972334557
    - type: nauc_ndcg_at_1_diff1
      value: 28.017413073648477
    - type: nauc_ndcg_at_1_max
      value: 32.87710191514022
    - type: nauc_ndcg_at_1_std
      value: 14.04889142608459
    - type: nauc_ndcg_at_20_diff1
      value: 24.5090484877482
    - type: nauc_ndcg_at_20_max
      value: 40.752854032983606
    - type: nauc_ndcg_at_20_std
      value: 22.70331074781384
    - type: nauc_ndcg_at_3_diff1
      value: 25.13499057756147
    - type: nauc_ndcg_at_3_max
      value: 35.8325682137567
    - type: nauc_ndcg_at_3_std
      value: 15.23768392706637
    - type: nauc_ndcg_at_5_diff1
      value: 24.614105695451116
    - type: nauc_ndcg_at_5_max
      value: 37.68089587624492
    - type: nauc_ndcg_at_5_std
      value: 17.946406099261708
    - type: nauc_precision_at_1000_diff1
      value: -2.022340544774227
    - type: nauc_precision_at_1000_max
      value: 6.070578645067797
    - type: nauc_precision_at_1000_std
      value: 22.15132728777549
    - type: nauc_precision_at_100_diff1
      value: 4.544144474504255
    - type: nauc_precision_at_100_max
      value: 19.780392159848574
    - type: nauc_precision_at_100_std
      value: 31.107111186002438
    - type: nauc_precision_at_10_diff1
      value: 10.107015022955848
    - type: nauc_precision_at_10_max
      value: 30.779709099060465
    - type: nauc_precision_at_10_std
      value: 27.324148451668602
    - type: nauc_precision_at_1_diff1
      value: 28.017413073648477
    - type: nauc_precision_at_1_max
      value: 32.87710191514022
    - type: nauc_precision_at_1_std
      value: 14.04889142608459
    - type: nauc_precision_at_20_diff1
      value: 8.270881053079405
    - type: nauc_precision_at_20_max
      value: 27.26753946078481
    - type: nauc_precision_at_20_std
      value: 29.156725822074204
    - type: nauc_precision_at_3_diff1
      value: 17.82468940497632
    - type: nauc_precision_at_3_max
      value: 31.490021174215155
    - type: nauc_precision_at_3_std
      value: 18.73818985054394
    - type: nauc_precision_at_5_diff1
      value: 13.24803141673961
    - type: nauc_precision_at_5_max
      value: 29.94926240784298
    - type: nauc_precision_at_5_std
      value: 23.2940906142919
    - type: nauc_recall_at_1000_diff1
      value: 19.09850333580471
    - type: nauc_recall_at_1000_max
      value: 46.026306142840596
    - type: nauc_recall_at_1000_std
      value: 46.50391519568263
    - type: nauc_recall_at_100_diff1
      value: 16.739384224869738
    - type: nauc_recall_at_100_max
      value: 40.68987136431252
    - type: nauc_recall_at_100_std
      value: 36.01609750485591
    - type: nauc_recall_at_10_diff1
      value: 17.51796617221814
    - type: nauc_recall_at_10_max
      value: 39.47453129444401
    - type: nauc_recall_at_10_std
      value: 23.79239002974899
    - type: nauc_recall_at_1_diff1
      value: 30.83614944448221
    - type: nauc_recall_at_1_max
      value: 33.757528532809
    - type: nauc_recall_at_1_std
      value: 8.880622713261126
    - type: nauc_recall_at_20_diff1
      value: 16.978668307251652
    - type: nauc_recall_at_20_max
      value: 39.09115357303713
    - type: nauc_recall_at_20_std
      value: 27.278668534187524
    - type: nauc_recall_at_3_diff1
      value: 22.55937738994021
    - type: nauc_recall_at_3_max
      value: 36.25055459395638
    - type: nauc_recall_at_3_std
      value: 14.828905168761247
    - type: nauc_recall_at_5_diff1
      value: 19.32656748627199
    - type: nauc_recall_at_5_max
      value: 36.28836228620816
    - type: nauc_recall_at_5_std
      value: 19.264352933914278
    - type: ndcg_at_1
      value: 34.137
    - type: ndcg_at_10
      value: 36.853
    - type: ndcg_at_100
      value: 44.279
    - type: ndcg_at_1000
      value: 47.336
    - type: ndcg_at_20
      value: 39.815
    - type: ndcg_at_3
      value: 30.253999999999998
    - type: ndcg_at_5
      value: 32.649
    - type: precision_at_1
      value: 34.137
    - type: precision_at_10
      value: 11.655
    - type: precision_at_100
      value: 1.9619999999999997
    - type: precision_at_1000
      value: 0.254
    - type: precision_at_20
      value: 7.1209999999999996
    - type: precision_at_3
      value: 22.823
    - type: precision_at_5
      value: 17.655
    - type: recall_at_1
      value: 15.371000000000002
    - type: recall_at_10
      value: 43.718
    - type: recall_at_100
      value: 68.81
    - type: recall_at_1000
      value: 85.69600000000001
    - type: recall_at_20
      value: 51.94
    - type: recall_at_3
      value: 27.694000000000003
    - type: recall_at_5
      value: 34.469
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: test
      type: mteb/dbpedia
    metrics:
    - type: main_score
      value: 45.553
    - type: map_at_1
      value: 9.168999999999999
    - type: map_at_10
      value: 22.154
    - type: map_at_100
      value: 32.174
    - type: map_at_1000
      value: 33.974
    - type: map_at_20
      value: 25.899
    - type: map_at_3
      value: 15.275
    - type: map_at_5
      value: 18.291
    - type: mrr_at_1
      value: 70.75
    - type: mrr_at_10
      value: 78.39662698412697
    - type: mrr_at_100
      value: 78.56221458977012
    - type: mrr_at_1000
      value: 78.56669970642338
    - type: mrr_at_20
      value: 78.49688805346696
    - type: mrr_at_3
      value: 76.33333333333333
    - type: mrr_at_5
      value: 77.70833333333333
    - type: nauc_map_at_1000_diff1
      value: 18.465085922071346
    - type: nauc_map_at_1000_max
      value: 24.29804638788498
    - type: nauc_map_at_1000_std
      value: 22.380463943423514
    - type: nauc_map_at_100_diff1
      value: 19.37585410674523
    - type: nauc_map_at_100_max
      value: 22.56424042509462
    - type: nauc_map_at_100_std
      value: 19.672237275984426
    - type: nauc_map_at_10_diff1
      value: 23.597788166305577
    - type: nauc_map_at_10_max
      value: 9.157316105122925
    - type: nauc_map_at_10_std
      value: -3.8881247055786807
    - type: nauc_map_at_1_diff1
      value: 43.96699602275052
    - type: nauc_map_at_1_max
      value: -0.7577088440873263
    - type: nauc_map_at_1_std
      value: -17.732463891968404
    - type: nauc_map_at_20_diff1
      value: 22.326759054850097
    - type: nauc_map_at_20_max
      value: 14.879191412167703
    - type: nauc_map_at_20_std
      value: 5.405751236575241
    - type: nauc_map_at_3_diff1
      value: 28.73583545428074
    - type: nauc_map_at_3_max
      value: 1.5986597211018239
    - type: nauc_map_at_3_std
      value: -16.512455883681515
    - type: nauc_map_at_5_diff1
      value: 25.401810959155057
    - type: nauc_map_at_5_max
      value: 4.418875376978587
    - type: nauc_map_at_5_std
      value: -12.296750992013052
    - type: nauc_mrr_at_1000_diff1
      value: 51.228801807498584
    - type: nauc_mrr_at_1000_max
      value: 61.040998883279585
    - type: nauc_mrr_at_1000_std
      value: 40.93983887257123
    - type: nauc_mrr_at_100_diff1
      value: 51.23715338435314
    - type: nauc_mrr_at_100_max
      value: 61.03971408781317
    - type: nauc_mrr_at_100_std
      value: 40.91796923590573
    - type: nauc_mrr_at_10_diff1
      value: 51.1214868552331
    - type: nauc_mrr_at_10_max
      value: 61.03069045590881
    - type: nauc_mrr_at_10_std
      value: 40.661621199704264
    - type: nauc_mrr_at_1_diff1
      value: 50.84660003035892
    - type: nauc_mrr_at_1_max
      value: 60.692091499960895
    - type: nauc_mrr_at_1_std
      value: 42.126228731502955
    - type: nauc_mrr_at_20_diff1
      value: 51.0402624284872
    - type: nauc_mrr_at_20_max
      value: 60.94577844338166
    - type: nauc_mrr_at_20_std
      value: 40.89505950503613
    - type: nauc_mrr_at_3_diff1
      value: 51.771113665996516
    - type: nauc_mrr_at_3_max
      value: 61.65264793077224
    - type: nauc_mrr_at_3_std
      value: 41.75781827057092
    - type: nauc_mrr_at_5_diff1
      value: 51.0656793772882
    - type: nauc_mrr_at_5_max
      value: 61.08042065139715
    - type: nauc_mrr_at_5_std
      value: 41.11203271084835
    - type: nauc_ndcg_at_1000_diff1
      value: 22.347978262245107
    - type: nauc_ndcg_at_1000_max
      value: 36.56458763955002
    - type: nauc_ndcg_at_1000_std
      value: 35.99616144258822
    - type: nauc_ndcg_at_100_diff1
      value: 23.1120990977162
    - type: nauc_ndcg_at_100_max
      value: 30.79663306311657
    - type: nauc_ndcg_at_100_std
      value: 27.387572106784297
    - type: nauc_ndcg_at_10_diff1
      value: 23.329746066899656
    - type: nauc_ndcg_at_10_max
      value: 28.69246947084685
    - type: nauc_ndcg_at_10_std
      value: 21.457736188325345
    - type: nauc_ndcg_at_1_diff1
      value: 39.99399153456974
    - type: nauc_ndcg_at_1_max
      value: 38.12447856470389
    - type: nauc_ndcg_at_1_std
      value: 27.768869260384676
    - type: nauc_ndcg_at_20_diff1
      value: 24.945374175339907
    - type: nauc_ndcg_at_20_max
      value: 27.67836982165295
    - type: nauc_ndcg_at_20_std
      value: 19.7933631060578
    - type: nauc_ndcg_at_3_diff1
      value: 26.063492354398527
    - type: nauc_ndcg_at_3_max
      value: 33.06541959550656
    - type: nauc_ndcg_at_3_std
      value: 23.278902797288726
    - type: nauc_ndcg_at_5_diff1
      value: 22.521596060750035
    - type: nauc_ndcg_at_5_max
      value: 31.210005673730784
    - type: nauc_ndcg_at_5_std
      value: 22.893106456317927
    - type: nauc_precision_at_1000_diff1
      value: -19.845356495096006
    - type: nauc_precision_at_1000_max
      value: 4.163819381816099
    - type: nauc_precision_at_1000_std
      value: 7.612952884590339
    - type: nauc_precision_at_100_diff1
      value: -8.2679285153361
    - type: nauc_precision_at_100_max
      value: 29.78018175573565
    - type: nauc_precision_at_100_std
      value: 41.07244463956215
    - type: nauc_precision_at_10_diff1
      value: -3.2451428407349057
    - type: nauc_precision_at_10_max
      value: 36.92563008274906
    - type: nauc_precision_at_10_std
      value: 45.06962043489777
    - type: nauc_precision_at_1_diff1
      value: 50.84660003035892
    - type: nauc_precision_at_1_max
      value: 60.692091499960895
    - type: nauc_precision_at_1_std
      value: 42.126228731502955
    - type: nauc_precision_at_20_diff1
      value: -3.432279149061878
    - type: nauc_precision_at_20_max
      value: 37.013592483974875
    - type: nauc_precision_at_20_std
      value: 46.47324739428665
    - type: nauc_precision_at_3_diff1
      value: 7.28495481051025
    - type: nauc_precision_at_3_max
      value: 38.66372411741402
    - type: nauc_precision_at_3_std
      value: 35.23163993723955
    - type: nauc_precision_at_5_diff1
      value: -0.16540230063716202
    - type: nauc_precision_at_5_max
      value: 37.322494255721715
    - type: nauc_precision_at_5_std
      value: 39.666653561269754
    - type: nauc_recall_at_1000_diff1
      value: 11.388326469283681
    - type: nauc_recall_at_1000_max
      value: 32.698146308591674
    - type: nauc_recall_at_1000_std
      value: 49.48830488070777
    - type: nauc_recall_at_100_diff1
      value: 11.497443532756819
    - type: nauc_recall_at_100_max
      value: 20.196970431621615
    - type: nauc_recall_at_100_std
      value: 23.688772100803433
    - type: nauc_recall_at_10_diff1
      value: 16.519851398596003
    - type: nauc_recall_at_10_max
      value: 0.774066845071221
    - type: nauc_recall_at_10_std
      value: -10.89514647001814
    - type: nauc_recall_at_1_diff1
      value: 43.96699602275052
    - type: nauc_recall_at_1_max
      value: -0.7577088440873263
    - type: nauc_recall_at_1_std
      value: -17.732463891968404
    - type: nauc_recall_at_20_diff1
      value: 15.202960269878258
    - type: nauc_recall_at_20_max
      value: 7.067263295590253
    - type: nauc_recall_at_20_std
      value: -0.06050108222640702
    - type: nauc_recall_at_3_diff1
      value: 24.066741361525125
    - type: nauc_recall_at_3_max
      value: -2.1961525860488424
    - type: nauc_recall_at_3_std
      value: -19.48307077749568
    - type: nauc_recall_at_5_diff1
      value: 20.086330794102707
    - type: nauc_recall_at_5_max
      value: -0.8866528062747986
    - type: nauc_recall_at_5_std
      value: -16.53799173962747
    - type: ndcg_at_1
      value: 57.99999999999999
    - type: ndcg_at_10
      value: 45.553
    - type: ndcg_at_100
      value: 51.014
    - type: ndcg_at_1000
      value: 58.226
    - type: ndcg_at_20
      value: 44.98
    - type: ndcg_at_3
      value: 48.981
    - type: ndcg_at_5
      value: 46.794999999999995
    - type: precision_at_1
      value: 70.75
    - type: precision_at_10
      value: 36.85
    - type: precision_at_100
      value: 11.955
    - type: precision_at_1000
      value: 2.247
    - type: precision_at_20
      value: 28.075
    - type: precision_at_3
      value: 52.666999999999994
    - type: precision_at_5
      value: 45.85
    - type: recall_at_1
      value: 9.168999999999999
    - type: recall_at_10
      value: 28.796
    - type: recall_at_100
      value: 58.892999999999994
    - type: recall_at_1000
      value: 81.644
    - type: recall_at_20
      value: 36.659000000000006
    - type: recall_at_3
      value: 16.709
    - type: recall_at_5
      value: 21.387
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FEVER
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
      split: test
      type: mteb/fever
    metrics:
    - type: main_score
      value: 88.41
    - type: map_at_1
      value: 75.637
    - type: map_at_10
      value: 84.674
    - type: map_at_100
      value: 84.909
    - type: map_at_1000
      value: 84.92
    - type: map_at_20
      value: 84.836
    - type: map_at_3
      value: 83.44200000000001
    - type: map_at_5
      value: 84.28099999999999
    - type: mrr_at_1
      value: 81.56315631563157
    - type: mrr_at_10
      value: 88.89571695264748
    - type: mrr_at_100
      value: 88.93671417216285
    - type: mrr_at_1000
      value: 88.93708016011664
    - type: mrr_at_20
      value: 88.9311652665256
    - type: mrr_at_3
      value: 88.20882088208805
    - type: mrr_at_5
      value: 88.72937293729349
    - type: nauc_map_at_1000_diff1
      value: 54.41216035074026
    - type: nauc_map_at_1000_max
      value: 13.346153003554361
    - type: nauc_map_at_1000_std
      value: -6.721664416152164
    - type: nauc_map_at_100_diff1
      value: 54.36538350995795
    - type: nauc_map_at_100_max
      value: 13.355583381471298
    - type: nauc_map_at_100_std
      value: -6.696921015641016
    - type: nauc_map_at_10_diff1
      value: 54.0389127730555
    - type: nauc_map_at_10_max
      value: 13.387802159150663
    - type: nauc_map_at_10_std
      value: -6.73514381731833
    - type: nauc_map_at_1_diff1
      value: 57.99489574836453
    - type: nauc_map_at_1_max
      value: 7.830032589171654
    - type: nauc_map_at_1_std
      value: -10.140208285080295
    - type: nauc_map_at_20_diff1
      value: 54.16841004736076
    - type: nauc_map_at_20_max
      value: 13.345607363689746
    - type: nauc_map_at_20_std
      value: -6.663119775158465
    - type: nauc_map_at_3_diff1
      value: 53.82879543599303
    - type: nauc_map_at_3_max
      value: 12.716952288433902
    - type: nauc_map_at_3_std
      value: -7.746102082835598
    - type: nauc_map_at_5_diff1
      value: 53.82838395350109
    - type: nauc_map_at_5_max
      value: 13.487373534211702
    - type: nauc_map_at_5_std
      value: -6.869504398693434
    - type: nauc_mrr_at_1000_diff1
      value: 68.92783546581906
    - type: nauc_mrr_at_1000_max
      value: 12.076297180596592
    - type: nauc_mrr_at_1000_std
      value: -13.306257067567998
    - type: nauc_mrr_at_100_diff1
      value: 68.92780219775517
    - type: nauc_mrr_at_100_max
      value: 12.078449805054374
    - type: nauc_mrr_at_100_std
      value: -13.303524852703719
    - type: nauc_mrr_at_10_diff1
      value: 68.92686206881258
    - type: nauc_mrr_at_10_max
      value: 12.273295656884873
    - type: nauc_mrr_at_10_std
      value: -13.222483496603965
    - type: nauc_mrr_at_1_diff1
      value: 70.1738022073041
    - type: nauc_mrr_at_1_max
      value: 9.378639533482806
    - type: nauc_mrr_at_1_std
      value: -13.444033823202348
    - type: nauc_mrr_at_20_diff1
      value: 68.91161304905303
    - type: nauc_mrr_at_20_max
      value: 12.117091514817885
    - type: nauc_mrr_at_20_std
      value: -13.258261750160239
    - type: nauc_mrr_at_3_diff1
      value: 68.61982455945467
    - type: nauc_mrr_at_3_max
      value: 12.608213879734578
    - type: nauc_mrr_at_3_std
      value: -13.558003431587839
    - type: nauc_mrr_at_5_diff1
      value: 68.81439097457242
    - type: nauc_mrr_at_5_max
      value: 12.54025598903624
    - type: nauc_mrr_at_5_std
      value: -13.199231514972093
    - type: nauc_ndcg_at_1000_diff1
      value: 56.47563443877495
    - type: nauc_ndcg_at_1000_max
      value: 14.508331783439466
    - type: nauc_ndcg_at_1000_std
      value: -6.206829736668775
    - type: nauc_ndcg_at_100_diff1
      value: 55.54015515673474
    - type: nauc_ndcg_at_100_max
      value: 14.753595778278136
    - type: nauc_ndcg_at_100_std
      value: -5.638517949568802
    - type: nauc_ndcg_at_10_diff1
      value: 54.220845223257996
    - type: nauc_ndcg_at_10_max
      value: 15.265309648490021
    - type: nauc_ndcg_at_10_std
      value: -5.516276098929109
    - type: nauc_ndcg_at_1_diff1
      value: 70.1738022073041
    - type: nauc_ndcg_at_1_max
      value: 9.378639533482806
    - type: nauc_ndcg_at_1_std
      value: -13.444033823202348
    - type: nauc_ndcg_at_20_diff1
      value: 54.481406100854635
    - type: nauc_ndcg_at_20_max
      value: 14.868763583210498
    - type: nauc_ndcg_at_20_std
      value: -5.328097380018734
    - type: nauc_ndcg_at_3_diff1
      value: 54.94411725607744
    - type: nauc_ndcg_at_3_max
      value: 14.27186734506607
    - type: nauc_ndcg_at_3_std
      value: -7.894724962312474
    - type: nauc_ndcg_at_5_diff1
      value: 54.08048166974806
    - type: nauc_ndcg_at_5_max
      value: 15.528233170721006
    - type: nauc_ndcg_at_5_std
      value: -5.984768714537104
    - type: nauc_precision_at_1000_diff1
      value: -8.744323640074445
    - type: nauc_precision_at_1000_max
      value: -0.01881224392053465
    - type: nauc_precision_at_1000_std
      value: 3.8721477979260635
    - type: nauc_precision_at_100_diff1
      value: -11.86150156952171
    - type: nauc_precision_at_100_max
      value: 3.2736651314552314
    - type: nauc_precision_at_100_std
      value: 8.12687620615509
    - type: nauc_precision_at_10_diff1
      value: -10.360708676781178
    - type: nauc_precision_at_10_max
      value: 10.945552490433458
    - type: nauc_precision_at_10_std
      value: 11.016707653014485
    - type: nauc_precision_at_1_diff1
      value: 70.1738022073041
    - type: nauc_precision_at_1_max
      value: 9.378639533482806
    - type: nauc_precision_at_1_std
      value: -13.444033823202348
    - type: nauc_precision_at_20_diff1
      value: -13.557721925696583
    - type: nauc_precision_at_20_max
      value: 6.331386521718574
    - type: nauc_precision_at_20_std
      value: 10.322188778142388
    - type: nauc_precision_at_3_diff1
      value: 15.139456770248968
    - type: nauc_precision_at_3_max
      value: 17.10220985600708
    - type: nauc_precision_at_3_std
      value: 3.0448183682558074
    - type: nauc_precision_at_5_diff1
      value: -1.9825577548111102
    - type: nauc_precision_at_5_max
      value: 17.139148127012625
    - type: nauc_precision_at_5_std
      value: 10.598435750554753
    - type: nauc_recall_at_1000_diff1
      value: 15.641740744283005
    - type: nauc_recall_at_1000_max
      value: 44.65315702195612
    - type: nauc_recall_at_1000_std
      value: 52.34265862835513
    - type: nauc_recall_at_100_diff1
      value: 5.254385435323394
    - type: nauc_recall_at_100_max
      value: 38.53577774395794
    - type: nauc_recall_at_100_std
      value: 43.47744274335829
    - type: nauc_recall_at_10_diff1
      value: 19.135735476268042
    - type: nauc_recall_at_10_max
      value: 30.05417445923848
    - type: nauc_recall_at_10_std
      value: 18.3988023241141
    - type: nauc_recall_at_1_diff1
      value: 57.99489574836453
    - type: nauc_recall_at_1_max
      value: 7.830032589171654
    - type: nauc_recall_at_1_std
      value: -10.140208285080295
    - type: nauc_recall_at_20_diff1
      value: 9.444797759735126
    - type: nauc_recall_at_20_max
      value: 31.001311675371017
    - type: nauc_recall_at_20_std
      value: 29.351418893822178
    - type: nauc_recall_at_3_diff1
      value: 36.88862653262064
    - type: nauc_recall_at_3_max
      value: 19.845892741607823
    - type: nauc_recall_at_3_std
      value: -1.0584273105890794
    - type: nauc_recall_at_5_diff1
      value: 27.360718561944974
    - type: nauc_recall_at_5_max
      value: 26.698311215441738
    - type: nauc_recall_at_5_std
      value: 8.97113997755362
    - type: ndcg_at_1
      value: 81.563
    - type: ndcg_at_10
      value: 88.41
    - type: ndcg_at_100
      value: 89.101
    - type: ndcg_at_1000
      value: 89.25800000000001
    - type: ndcg_at_20
      value: 88.79
    - type: ndcg_at_3
      value: 86.599
    - type: ndcg_at_5
      value: 87.74
    - type: precision_at_1
      value: 81.563
    - type: precision_at_10
      value: 10.699
    - type: precision_at_100
      value: 1.13
    - type: precision_at_1000
      value: 0.116
    - type: precision_at_20
      value: 5.479
    - type: precision_at_3
      value: 33.238
    - type: precision_at_5
      value: 20.744
    - type: recall_at_1
      value: 75.637
    - type: recall_at_10
      value: 95.57600000000001
    - type: recall_at_100
      value: 98.072
    - type: recall_at_1000
      value: 98.951
    - type: recall_at_20
      value: 96.792
    - type: recall_at_3
      value: 90.79599999999999
    - type: recall_at_5
      value: 93.674
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA2018
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: test
      type: mteb/fiqa
    metrics:
    - type: main_score
      value: 42.396
    - type: map_at_1
      value: 21.711
    - type: map_at_10
      value: 34.628
    - type: map_at_100
      value: 36.549
    - type: map_at_1000
      value: 36.719
    - type: map_at_20
      value: 35.673
    - type: map_at_3
      value: 30.585
    - type: map_at_5
      value: 32.875
    - type: mrr_at_1
      value: 41.82098765432099
    - type: mrr_at_10
      value: 50.69505682931607
    - type: mrr_at_100
      value: 51.50556608727901
    - type: mrr_at_1000
      value: 51.53870583208304
    - type: mrr_at_20
      value: 51.15345764364655
    - type: mrr_at_3
      value: 48.35390946502059
    - type: mrr_at_5
      value: 49.87397119341563
    - type: nauc_map_at_1000_diff1
      value: 45.182252919583895
    - type: nauc_map_at_1000_max
      value: 35.66124930024801
    - type: nauc_map_at_1000_std
      value: -0.6925562638650965
    - type: nauc_map_at_100_diff1
      value: 45.116964706960125
    - type: nauc_map_at_100_max
      value: 35.54990469525889
    - type: nauc_map_at_100_std
      value: -0.6667263852859368
    - type: nauc_map_at_10_diff1
      value: 45.39189096228184
    - type: nauc_map_at_10_max
      value: 34.780111261901
    - type: nauc_map_at_10_std
      value: -1.8169859294150819
    - type: nauc_map_at_1_diff1
      value: 47.72764937952259
    - type: nauc_map_at_1_max
      value: 24.83306559709341
    - type: nauc_map_at_1_std
      value: -4.714128457297418
    - type: nauc_map_at_20_diff1
      value: 45.17073365898278
    - type: nauc_map_at_20_max
      value: 35.0938403469058
    - type: nauc_map_at_20_std
      value: -1.373412631183604
    - type: nauc_map_at_3_diff1
      value: 46.525724305731295
    - type: nauc_map_at_3_max
      value: 31.042538866512597
    - type: nauc_map_at_3_std
      value: -4.119355935975354
    - type: nauc_map_at_5_diff1
      value: 45.79569633383187
    - type: nauc_map_at_5_max
      value: 32.88779656647293
    - type: nauc_map_at_5_std
      value: -3.2518474739335312
    - type: nauc_mrr_at_1000_diff1
      value: 52.83619185487903
    - type: nauc_mrr_at_1000_max
      value: 42.30310720405186
    - type: nauc_mrr_at_1000_std
      value: -1.1487703348518024
    - type: nauc_mrr_at_100_diff1
      value: 52.82248853996664
    - type: nauc_mrr_at_100_max
      value: 42.30549701564678
    - type: nauc_mrr_at_100_std
      value: -1.1240113031894834
    - type: nauc_mrr_at_10_diff1
      value: 52.74644276642243
    - type: nauc_mrr_at_10_max
      value: 42.39103029476398
    - type: nauc_mrr_at_10_std
      value: -1.1043413237848576
    - type: nauc_mrr_at_1_diff1
      value: 54.810335521617326
    - type: nauc_mrr_at_1_max
      value: 40.733260207843394
    - type: nauc_mrr_at_1_std
      value: -4.452554921565855
    - type: nauc_mrr_at_20_diff1
      value: 52.788257862499954
    - type: nauc_mrr_at_20_max
      value: 42.32658875363406
    - type: nauc_mrr_at_20_std
      value: -1.2209728080684497
    - type: nauc_mrr_at_3_diff1
      value: 53.43281175319808
    - type: nauc_mrr_at_3_max
      value: 41.735942650867926
    - type: nauc_mrr_at_3_std
      value: -2.462688102468019
    - type: nauc_mrr_at_5_diff1
      value: 52.874037126566606
    - type: nauc_mrr_at_5_max
      value: 41.93740449458822
    - type: nauc_mrr_at_5_std
      value: -1.2928874908441947
    - type: nauc_ndcg_at_1000_diff1
      value: 46.5532425476402
    - type: nauc_ndcg_at_1000_max
      value: 40.369611603370515
    - type: nauc_ndcg_at_1000_std
      value: 3.472567588386994
    - type: nauc_ndcg_at_100_diff1
      value: 45.75244404695404
    - type: nauc_ndcg_at_100_max
      value: 39.36470550675439
    - type: nauc_ndcg_at_100_std
      value: 4.356189041115731
    - type: nauc_ndcg_at_10_diff1
      value: 46.005135323539704
    - type: nauc_ndcg_at_10_max
      value: 37.89018165334218
    - type: nauc_ndcg_at_10_std
      value: 0.7129618297768014
    - type: nauc_ndcg_at_1_diff1
      value: 54.810335521617326
    - type: nauc_ndcg_at_1_max
      value: 40.733260207843394
    - type: nauc_ndcg_at_1_std
      value: -4.452554921565855
    - type: nauc_ndcg_at_20_diff1
      value: 45.841552790490034
    - type: nauc_ndcg_at_20_max
      value: 38.04992825472661
    - type: nauc_ndcg_at_20_std
      value: 1.2748305707955212
    - type: nauc_ndcg_at_3_diff1
      value: 46.683033449357744
    - type: nauc_ndcg_at_3_max
      value: 37.46397870760607
    - type: nauc_ndcg_at_3_std
      value: -2.3421854966319824
    - type: nauc_ndcg_at_5_diff1
      value: 45.82409645378457
    - type: nauc_ndcg_at_5_max
      value: 36.27588234096716
    - type: nauc_ndcg_at_5_std
      value: -1.5141197170944254
    - type: nauc_precision_at_1000_diff1
      value: -3.137944321071885
    - type: nauc_precision_at_1000_max
      value: 24.12803166253776
    - type: nauc_precision_at_1000_std
      value: 11.076454789944101
    - type: nauc_precision_at_100_diff1
      value: 3.9896283891401048
    - type: nauc_precision_at_100_max
      value: 31.00198316788829
    - type: nauc_precision_at_100_std
      value: 15.725887643803063
    - type: nauc_precision_at_10_diff1
      value: 20.493420889888394
    - type: nauc_precision_at_10_max
      value: 41.689699671507405
    - type: nauc_precision_at_10_std
      value: 9.374983385669914
    - type: nauc_precision_at_1_diff1
      value: 54.810335521617326
    - type: nauc_precision_at_1_max
      value: 40.733260207843394
    - type: nauc_precision_at_1_std
      value: -4.452554921565855
    - type: nauc_precision_at_20_diff1
      value: 15.02911800246446
    - type: nauc_precision_at_20_max
      value: 39.227068888505
    - type: nauc_precision_at_20_std
      value: 11.755558515319404
    - type: nauc_precision_at_3_diff1
      value: 34.044986535461746
    - type: nauc_precision_at_3_max
      value: 40.96605829831656
    - type: nauc_precision_at_3_std
      value: 1.1903535705688038
    - type: nauc_precision_at_5_diff1
      value: 26.617002443432707
    - type: nauc_precision_at_5_max
      value: 40.60413785916794
    - type: nauc_precision_at_5_std
      value: 3.6984531670502814
    - type: nauc_recall_at_1000_diff1
      value: 26.96489389440101
    - type: nauc_recall_at_1000_max
      value: 41.811583968523955
    - type: nauc_recall_at_1000_std
      value: 41.5719519496712
    - type: nauc_recall_at_100_diff1
      value: 28.50851434908223
    - type: nauc_recall_at_100_max
      value: 32.19528060706322
    - type: nauc_recall_at_100_std
      value: 25.56935294258179
    - type: nauc_recall_at_10_diff1
      value: 35.139582891180964
    - type: nauc_recall_at_10_max
      value: 32.15221840434225
    - type: nauc_recall_at_10_std
      value: 5.550434611582702
    - type: nauc_recall_at_1_diff1
      value: 47.72764937952259
    - type: nauc_recall_at_1_max
      value: 24.83306559709341
    - type: nauc_recall_at_1_std
      value: -4.714128457297418
    - type: nauc_recall_at_20_diff1
      value: 32.78604811055205
    - type: nauc_recall_at_20_max
      value: 29.62940720700254
    - type: nauc_recall_at_20_std
      value: 6.769941491859872
    - type: nauc_recall_at_3_diff1
      value: 40.76090616138699
    - type: nauc_recall_at_3_max
      value: 27.506425490226867
    - type: nauc_recall_at_3_std
      value: -2.608872693119243
    - type: nauc_recall_at_5_diff1
      value: 37.06532485024711
    - type: nauc_recall_at_5_max
      value: 27.704150556658448
    - type: nauc_recall_at_5_std
      value: 0.4718707152343872
    - type: ndcg_at_1
      value: 41.821000000000005
    - type: ndcg_at_10
      value: 42.396
    - type: ndcg_at_100
      value: 49.370000000000005
    - type: ndcg_at_1000
      value: 52.251000000000005
    - type: ndcg_at_20
      value: 45.097
    - type: ndcg_at_3
      value: 39.028
    - type: ndcg_at_5
      value: 40.222
    - type: precision_at_1
      value: 41.821000000000005
    - type: precision_at_10
      value: 11.451
    - type: precision_at_100
      value: 1.863
    - type: precision_at_1000
      value: 0.23900000000000002
    - type: precision_at_20
      value: 6.798
    - type: precision_at_3
      value: 25.823
    - type: precision_at_5
      value: 18.735
    - type: recall_at_1
      value: 21.711
    - type: recall_at_10
      value: 48.862
    - type: recall_at_100
      value: 74.708
    - type: recall_at_1000
      value: 91.865
    - type: recall_at_20
      value: 57.50999999999999
    - type: recall_at_3
      value: 35.85
    - type: recall_at_5
      value: 41.976
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
      split: test
      type: mteb/hotpotqa
    metrics:
    - type: main_score
      value: 72.21
    - type: map_at_1
      value: 39.487
    - type: map_at_10
      value: 63.949999999999996
    - type: map_at_100
      value: 64.873
    - type: map_at_1000
      value: 64.927
    - type: map_at_20
      value: 64.529
    - type: map_at_3
      value: 60.243
    - type: map_at_5
      value: 62.613
    - type: mrr_at_1
      value: 78.97366644159351
    - type: mrr_at_10
      value: 84.84600173627825
    - type: mrr_at_100
      value: 85.0172804866798
    - type: mrr_at_1000
      value: 85.02245651152857
    - type: mrr_at_20
      value: 84.9625577788225
    - type: mrr_at_3
      value: 83.90276839972962
    - type: mrr_at_5
      value: 84.48278190411845
    - type: nauc_map_at_1000_diff1
      value: 19.825004700775164
    - type: nauc_map_at_1000_max
      value: 19.943221724164182
    - type: nauc_map_at_1000_std
      value: 10.068951166560058
    - type: nauc_map_at_100_diff1
      value: 19.80139472181137
    - type: nauc_map_at_100_max
      value: 19.938006132804347
    - type: nauc_map_at_100_std
      value: 10.100008107666842
    - type: nauc_map_at_10_diff1
      value: 19.53604502514735
    - type: nauc_map_at_10_max
      value: 19.62768870331064
    - type: nauc_map_at_10_std
      value: 9.446859074725705
    - type: nauc_map_at_1_diff1
      value: 67.7764270505257
    - type: nauc_map_at_1_max
      value: 38.45166604737058
    - type: nauc_map_at_1_std
      value: 1.9919181988552352
    - type: nauc_map_at_20_diff1
      value: 19.635871913149913
    - type: nauc_map_at_20_max
      value: 19.812838965919155
    - type: nauc_map_at_20_std
      value: 9.905163140101845
    - type: nauc_map_at_3_diff1
      value: 18.965707122532212
    - type: nauc_map_at_3_max
      value: 17.878860313056517
    - type: nauc_map_at_3_std
      value: 6.189378752019195
    - type: nauc_map_at_5_diff1
      value: 19.493354049675954
    - type: nauc_map_at_5_max
      value: 19.24527088109141
    - type: nauc_map_at_5_std
      value: 8.283883139680066
    - type: nauc_mrr_at_1000_diff1
      value: 66.87150374356781
    - type: nauc_mrr_at_1000_max
      value: 41.413456443203984
    - type: nauc_mrr_at_1000_std
      value: 4.140387282484357
    - type: nauc_mrr_at_100_diff1
      value: 66.87178015619061
    - type: nauc_mrr_at_100_max
      value: 41.419754763150834
    - type: nauc_mrr_at_100_std
      value: 4.15222235416704
    - type: nauc_mrr_at_10_diff1
      value: 66.89720586892301
    - type: nauc_mrr_at_10_max
      value: 41.56353878125211
    - type: nauc_mrr_at_10_std
      value: 4.213376519922392
    - type: nauc_mrr_at_1_diff1
      value: 67.7764270505257
    - type: nauc_mrr_at_1_max
      value: 38.45166604737058
    - type: nauc_mrr_at_1_std
      value: 1.9919181988552352
    - type: nauc_mrr_at_20_diff1
      value: 66.8714688713149
    - type: nauc_mrr_at_20_max
      value: 41.46170778986735
    - type: nauc_mrr_at_20_std
      value: 4.165154741309859
    - type: nauc_mrr_at_3_diff1
      value: 66.31615462679144
    - type: nauc_mrr_at_3_max
      value: 41.419637693259936
    - type: nauc_mrr_at_3_std
      value: 3.814834551396097
    - type: nauc_mrr_at_5_diff1
      value: 66.7289413087213
    - type: nauc_mrr_at_5_max
      value: 41.668346356371586
    - type: nauc_mrr_at_5_std
      value: 4.116331539882484
    - type: nauc_ndcg_at_1000_diff1
      value: 26.37325375970598
    - type: nauc_ndcg_at_1000_max
      value: 24.850915174721735
    - type: nauc_ndcg_at_1000_std
      value: 13.37585683440429
    - type: nauc_ndcg_at_100_diff1
      value: 25.591771178059503
    - type: nauc_ndcg_at_100_max
      value: 24.562820829532473
    - type: nauc_ndcg_at_100_std
      value: 14.093690500501541
    - type: nauc_ndcg_at_10_diff1
      value: 24.64600598115805
    - type: nauc_ndcg_at_10_max
      value: 23.543499404760023
    - type: nauc_ndcg_at_10_std
      value: 11.55823632781553
    - type: nauc_ndcg_at_1_diff1
      value: 67.7764270505257
    - type: nauc_ndcg_at_1_max
      value: 38.45166604737058
    - type: nauc_ndcg_at_1_std
      value: 1.9919181988552352
    - type: nauc_ndcg_at_20_diff1
      value: 24.757843275306726
    - type: nauc_ndcg_at_20_max
      value: 23.951154200380827
    - type: nauc_ndcg_at_20_std
      value: 12.931320453044886
    - type: nauc_ndcg_at_3_diff1
      value: 24.37742630418847
    - type: nauc_ndcg_at_3_max
      value: 21.310512304883723
    - type: nauc_ndcg_at_3_std
      value: 6.503993200818077
    - type: nauc_ndcg_at_5_diff1
      value: 24.813706829269716
    - type: nauc_ndcg_at_5_max
      value: 22.993657212898
    - type: nauc_ndcg_at_5_std
      value: 9.34462052506809
    - type: nauc_precision_at_1000_diff1
      value: -0.6506415756958156
    - type: nauc_precision_at_1000_max
      value: 28.039755644694875
    - type: nauc_precision_at_1000_std
      value: 53.46474329623814
    - type: nauc_precision_at_100_diff1
      value: 3.78462668236152
    - type: nauc_precision_at_100_max
      value: 22.501700881673862
    - type: nauc_precision_at_100_std
      value: 40.56672716474142
    - type: nauc_precision_at_10_diff1
      value: 9.156113228907534
    - type: nauc_precision_at_10_max
      value: 19.734206254833254
    - type: nauc_precision_at_10_std
      value: 19.986282545779602
    - type: nauc_precision_at_1_diff1
      value: 67.7764270505257
    - type: nauc_precision_at_1_max
      value: 38.45166604737058
    - type: nauc_precision_at_1_std
      value: 1.9919181988552352
    - type: nauc_precision_at_20_diff1
      value: 6.6164335644470125
    - type: nauc_precision_at_20_max
      value: 20.29343459608317
    - type: nauc_precision_at_20_std
      value: 26.51115475333977
    - type: nauc_precision_at_3_diff1
      value: 12.476520554399546
    - type: nauc_precision_at_3_max
      value: 16.69401409858964
    - type: nauc_precision_at_3_std
      value: 8.165880294907444
    - type: nauc_precision_at_5_diff1
      value: 11.783242828320958
    - type: nauc_precision_at_5_max
      value: 19.0679467875759
    - type: nauc_precision_at_5_std
      value: 13.615358345509884
    - type: nauc_recall_at_1000_diff1
      value: -0.6506415756960168
    - type: nauc_recall_at_1000_max
      value: 28.039755644694786
    - type: nauc_recall_at_1000_std
      value: 53.46474329623801
    - type: nauc_recall_at_100_diff1
      value: 3.7846266823613877
    - type: nauc_recall_at_100_max
      value: 22.501700881674008
    - type: nauc_recall_at_100_std
      value: 40.566727164741366
    - type: nauc_recall_at_10_diff1
      value: 9.15611322890755
    - type: nauc_recall_at_10_max
      value: 19.73420625483318
    - type: nauc_recall_at_10_std
      value: 19.98628254577951
    - type: nauc_recall_at_1_diff1
      value: 67.7764270505257
    - type: nauc_recall_at_1_max
      value: 38.45166604737058
    - type: nauc_recall_at_1_std
      value: 1.9919181988552352
    - type: nauc_recall_at_20_diff1
      value: 6.616433564446929
    - type: nauc_recall_at_20_max
      value: 20.293434596083248
    - type: nauc_recall_at_20_std
      value: 26.5111547533396
    - type: nauc_recall_at_3_diff1
      value: 12.476520554399531
    - type: nauc_recall_at_3_max
      value: 16.69401409858966
    - type: nauc_recall_at_3_std
      value: 8.165880294907438
    - type: nauc_recall_at_5_diff1
      value: 11.783242828320999
    - type: nauc_recall_at_5_max
      value: 19.067946787575845
    - type: nauc_recall_at_5_std
      value: 13.61535834550991
    - type: ndcg_at_1
      value: 78.974
    - type: ndcg_at_10
      value: 72.21
    - type: ndcg_at_100
      value: 75.264
    - type: ndcg_at_1000
      value: 76.259
    - type: ndcg_at_20
      value: 73.628
    - type: ndcg_at_3
      value: 67.047
    - type: ndcg_at_5
      value: 69.974
    - type: precision_at_1
      value: 78.974
    - type: precision_at_10
      value: 15.267
    - type: precision_at_100
      value: 1.762
    - type: precision_at_1000
      value: 0.189
    - type: precision_at_20
      value: 8.09
    - type: precision_at_3
      value: 43.309
    - type: precision_at_5
      value: 28.294000000000004
    - type: recall_at_1
      value: 39.487
    - type: recall_at_10
      value: 76.334
    - type: recall_at_100
      value: 88.076
    - type: recall_at_1000
      value: 94.59100000000001
    - type: recall_at_20
      value: 80.898
    - type: recall_at_3
      value: 64.96300000000001
    - type: recall_at_5
      value: 70.736
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB MSMARCO
      revision: c5a29a104738b98a9e76336939199e264163d4a0
      split: dev
      type: mteb/msmarco
    metrics:
    - type: main_score
      value: 42.027
    - type: map_at_1
      value: 22.118
    - type: map_at_10
      value: 34.816
    - type: map_at_100
      value: 35.983
    - type: map_at_1000
      value: 36.028999999999996
    - type: map_at_20
      value: 35.545
    - type: map_at_3
      value: 30.752000000000002
    - type: map_at_5
      value: 33.114
    - type: mrr_at_1
      value: 22.793696275071635
    - type: mrr_at_10
      value: 35.47250079592483
    - type: mrr_at_100
      value: 36.576471512902856
    - type: mrr_at_1000
      value: 36.616205680509786
    - type: mrr_at_20
      value: 36.16557033864942
    - type: mrr_at_3
      value: 31.48758357211065
    - type: mrr_at_5
      value: 33.80563514804202
    - type: nauc_map_at_1000_diff1
      value: 32.89234100489284
    - type: nauc_map_at_1000_max
      value: 1.1802816553581001
    - type: nauc_map_at_1000_std
      value: -20.187692925732446
    - type: nauc_map_at_100_diff1
      value: 32.88694493681772
    - type: nauc_map_at_100_max
      value: 1.1732717578080365
    - type: nauc_map_at_100_std
      value: -20.164165529035245
    - type: nauc_map_at_10_diff1
      value: 32.826182211848796
    - type: nauc_map_at_10_max
      value: 1.1551262165737235
    - type: nauc_map_at_10_std
      value: -20.88326292319754
    - type: nauc_map_at_1_diff1
      value: 36.12732122790642
    - type: nauc_map_at_1_max
      value: 1.8197550109156913
    - type: nauc_map_at_1_std
      value: -17.205625720792167
    - type: nauc_map_at_20_diff1
      value: 32.83333177195551
    - type: nauc_map_at_20_max
      value: 1.0937431645506202
    - type: nauc_map_at_20_std
      value: -20.503956514646145
    - type: nauc_map_at_3_diff1
      value: 32.76264193805814
    - type: nauc_map_at_3_max
      value: 0.8560962042500389
    - type: nauc_map_at_3_std
      value: -20.608930717315577
    - type: nauc_map_at_5_diff1
      value: 32.78673238978775
    - type: nauc_map_at_5_max
      value: 1.0511863039329437
    - type: nauc_map_at_5_std
      value: -21.02164728626011
    - type: nauc_mrr_at_1000_diff1
      value: 32.610323934702286
    - type: nauc_mrr_at_1000_max
      value: 1.276669121901405
    - type: nauc_mrr_at_1000_std
      value: -19.908120615285043
    - type: nauc_mrr_at_100_diff1
      value: 32.601373758102795
    - type: nauc_mrr_at_100_max
      value: 1.2752735149992132
    - type: nauc_mrr_at_100_std
      value: -19.87937042610101
    - type: nauc_mrr_at_10_diff1
      value: 32.55795432078168
    - type: nauc_mrr_at_10_max
      value: 1.2881786969258637
    - type: nauc_mrr_at_10_std
      value: -20.54564519015977
    - type: nauc_mrr_at_1_diff1
      value: 35.596301376443726
    - type: nauc_mrr_at_1_max
      value: 1.7633238037306902
    - type: nauc_mrr_at_1_std
      value: -17.1999420019887
    - type: nauc_mrr_at_20_diff1
      value: 32.57185739111023
    - type: nauc_mrr_at_20_max
      value: 1.2212620853201877
    - type: nauc_mrr_at_20_std
      value: -20.179517281041264
    - type: nauc_mrr_at_3_diff1
      value: 32.42681377099514
    - type: nauc_mrr_at_3_max
      value: 0.8745921708861145
    - type: nauc_mrr_at_3_std
      value: -20.41017687790572
    - type: nauc_mrr_at_5_diff1
      value: 32.499107129648266
    - type: nauc_mrr_at_5_max
      value: 1.1159673851851573
    - type: nauc_mrr_at_5_std
      value: -20.695143502133824
    - type: nauc_ndcg_at_1000_diff1
      value: 32.16957965806702
    - type: nauc_ndcg_at_1000_max
      value: 1.6763998947980905
    - type: nauc_ndcg_at_1000_std
      value: -18.970592350332893
    - type: nauc_ndcg_at_100_diff1
      value: 31.977550102558872
    - type: nauc_ndcg_at_100_max
      value: 1.5625858650110014
    - type: nauc_ndcg_at_100_std
      value: -17.990456766123835
    - type: nauc_ndcg_at_10_diff1
      value: 31.82738932481356
    - type: nauc_ndcg_at_10_max
      value: 1.1661362042692103
    - type: nauc_ndcg_at_10_std
      value: -21.872680193994217
    - type: nauc_ndcg_at_1_diff1
      value: 35.596301376443726
    - type: nauc_ndcg_at_1_max
      value: 1.7633238037306902
    - type: nauc_ndcg_at_1_std
      value: -17.1999420019887
    - type: nauc_ndcg_at_20_diff1
      value: 31.749656399266264
    - type: nauc_ndcg_at_20_max
      value: 0.9629024493088691
    - type: nauc_ndcg_at_20_std
      value: -20.4379403899277
    - type: nauc_ndcg_at_3_diff1
      value: 31.731361436850836
    - type: nauc_ndcg_at_3_max
      value: 0.531749791578849
    - type: nauc_ndcg_at_3_std
      value: -21.551112910698674
    - type: nauc_ndcg_at_5_diff1
      value: 31.785373941157303
    - type: nauc_ndcg_at_5_max
      value: 0.86207769368333
    - type: nauc_ndcg_at_5_std
      value: -22.24923399160171
    - type: nauc_precision_at_1000_diff1
      value: -3.841288331986519
    - type: nauc_precision_at_1000_max
      value: 13.558041371634976
    - type: nauc_precision_at_1000_std
      value: 15.181510484512827
    - type: nauc_precision_at_100_diff1
      value: 12.441154582709053
    - type: nauc_precision_at_100_max
      value: 8.428136255841935
    - type: nauc_precision_at_100_std
      value: 14.710391839731656
    - type: nauc_precision_at_10_diff1
      value: 26.185854813986705
    - type: nauc_precision_at_10_max
      value: 1.6348387310504464
    - type: nauc_precision_at_10_std
      value: -23.448927004357298
    - type: nauc_precision_at_1_diff1
      value: 35.596301376443726
    - type: nauc_precision_at_1_max
      value: 1.7633238037306902
    - type: nauc_precision_at_1_std
      value: -17.1999420019887
    - type: nauc_precision_at_20_diff1
      value: 22.69194179544158
    - type: nauc_precision_at_20_max
      value: 1.2972015009169306
    - type: nauc_precision_at_20_std
      value: -15.751482380060269
    - type: nauc_precision_at_3_diff1
      value: 28.255531512125188
    - type: nauc_precision_at_3_max
      value: -0.3715575458464333
    - type: nauc_precision_at_3_std
      value: -24.227970454057697
    - type: nauc_precision_at_5_diff1
      value: 27.65497951098847
    - type: nauc_precision_at_5_max
      value: 0.449773375292472
    - type: nauc_precision_at_5_std
      value: -25.37445450938601
    - type: nauc_recall_at_1000_diff1
      value: 15.243948516763819
    - type: nauc_recall_at_1000_max
      value: 41.821227805251375
    - type: nauc_recall_at_1000_std
      value: 61.66297794838101
    - type: nauc_recall_at_100_diff1
      value: 24.516543685029994
    - type: nauc_recall_at_100_max
      value: 7.093972966253228
    - type: nauc_recall_at_100_std
      value: 17.244452321212282
    - type: nauc_recall_at_10_diff1
      value: 28.404243095182828
    - type: nauc_recall_at_10_max
      value: 1.0805210480930945
    - type: nauc_recall_at_10_std
      value: -24.885018657039527
    - type: nauc_recall_at_1_diff1
      value: 36.12732122790642
    - type: nauc_recall_at_1_max
      value: 1.8197550109156913
    - type: nauc_recall_at_1_std
      value: -17.205625720792167
    - type: nauc_recall_at_20_diff1
      value: 26.956250169438512
    - type: nauc_recall_at_20_max
      value: 0.023973408161285917
    - type: nauc_recall_at_20_std
      value: -18.32944444428131
    - type: nauc_recall_at_3_diff1
      value: 28.9894205130054
    - type: nauc_recall_at_3_max
      value: -0.36140658021466865
    - type: nauc_recall_at_3_std
      value: -24.022505107768364
    - type: nauc_recall_at_5_diff1
      value: 28.907023434955104
    - type: nauc_recall_at_5_max
      value: 0.2501037567297729
    - type: nauc_recall_at_5_std
      value: -25.719919602271496
    - type: ndcg_at_1
      value: 22.794
    - type: ndcg_at_10
      value: 42.027
    - type: ndcg_at_100
      value: 47.601
    - type: ndcg_at_1000
      value: 48.713
    - type: ndcg_at_20
      value: 44.623000000000005
    - type: ndcg_at_3
      value: 33.772999999999996
    - type: ndcg_at_5
      value: 37.991
    - type: precision_at_1
      value: 22.794
    - type: precision_at_10
      value: 6.711
    - type: precision_at_100
      value: 0.9490000000000001
    - type: precision_at_1000
      value: 0.105
    - type: precision_at_20
      value: 3.8920000000000003
    - type: precision_at_3
      value: 14.46
    - type: precision_at_5
      value: 10.822
    - type: recall_at_1
      value: 22.118
    - type: recall_at_10
      value: 64.201
    - type: recall_at_100
      value: 89.878
    - type: recall_at_1000
      value: 98.259
    - type: recall_at_20
      value: 74.34100000000001
    - type: recall_at_3
      value: 41.8
    - type: recall_at_5
      value: 51.959
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NFCorpus
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
      split: test
      type: mteb/nfcorpus
    metrics:
    - type: main_score
      value: 36.201
    - type: map_at_1
      value: 5.654
    - type: map_at_10
      value: 13.402
    - type: map_at_100
      value: 16.849
    - type: map_at_1000
      value: 18.264
    - type: map_at_20
      value: 14.832
    - type: map_at_3
      value: 9.619
    - type: map_at_5
      value: 11.483
    - type: mrr_at_1
      value: 47.6780185758514
    - type: mrr_at_10
      value: 56.47906531033466
    - type: mrr_at_100
      value: 57.04539749991402
    - type: mrr_at_1000
      value: 57.08810157607369
    - type: mrr_at_20
      value: 56.88003170105462
    - type: mrr_at_3
      value: 54.43756449948401
    - type: mrr_at_5
      value: 55.660474716202266
    - type: nauc_map_at_1000_diff1
      value: 31.134615238698192
    - type: nauc_map_at_1000_max
      value: 36.09522002487132
    - type: nauc_map_at_1000_std
      value: 14.72627666649002
    - type: nauc_map_at_100_diff1
      value: 32.777473351864444
    - type: nauc_map_at_100_max
      value: 35.25391471621035
    - type: nauc_map_at_100_std
      value: 12.024428973861083
    - type: nauc_map_at_10_diff1
      value: 36.46466466148528
    - type: nauc_map_at_10_max
      value: 29.707805406826722
    - type: nauc_map_at_10_std
      value: 2.0678757794226335
    - type: nauc_map_at_1_diff1
      value: 54.30208426149679
    - type: nauc_map_at_1_max
      value: 18.69125148481608
    - type: nauc_map_at_1_std
      value: -8.970955660291802
    - type: nauc_map_at_20_diff1
      value: 34.76513311600623
    - type: nauc_map_at_20_max
      value: 32.20666003570514
    - type: nauc_map_at_20_std
      value: 5.924889441518581
    - type: nauc_map_at_3_diff1
      value: 45.73465176835491
    - type: nauc_map_at_3_max
      value: 23.492291524989106
    - type: nauc_map_at_3_std
      value: -5.0123536561688855
    - type: nauc_map_at_5_diff1
      value: 39.7128319374107
    - type: nauc_map_at_5_max
      value: 25.84231729559691
    - type: nauc_map_at_5_std
      value: -2.0861428981140344
    - type: nauc_mrr_at_1000_diff1
      value: 33.0997881703397
    - type: nauc_mrr_at_1000_max
      value: 52.7089709923531
    - type: nauc_mrr_at_1000_std
      value: 28.8517952674151
    - type: nauc_mrr_at_100_diff1
      value: 33.1094984027438
    - type: nauc_mrr_at_100_max
      value: 52.74301398138847
    - type: nauc_mrr_at_100_std
      value: 28.897997840300892
    - type: nauc_mrr_at_10_diff1
      value: 33.300713655464925
    - type: nauc_mrr_at_10_max
      value: 52.572139698742184
    - type: nauc_mrr_at_10_std
      value: 28.66875615527188
    - type: nauc_mrr_at_1_diff1
      value: 32.57632582147155
    - type: nauc_mrr_at_1_max
      value: 46.020072246328816
    - type: nauc_mrr_at_1_std
      value: 20.99097889820076
    - type: nauc_mrr_at_20_diff1
      value: 33.04083904518949
    - type: nauc_mrr_at_20_max
      value: 52.597451362456994
    - type: nauc_mrr_at_20_std
      value: 28.681527293587898
    - type: nauc_mrr_at_3_diff1
      value: 33.64864656322754
    - type: nauc_mrr_at_3_max
      value: 51.82256412011279
    - type: nauc_mrr_at_3_std
      value: 27.241260746740686
    - type: nauc_mrr_at_5_diff1
      value: 33.53201325467246
    - type: nauc_mrr_at_5_max
      value: 52.79440885773516
    - type: nauc_mrr_at_5_std
      value: 28.663081392086028
    - type: nauc_ndcg_at_1000_diff1
      value: 28.632650542040714
    - type: nauc_ndcg_at_1000_max
      value: 51.24103069835822
    - type: nauc_ndcg_at_1000_std
      value: 35.05503784757999
    - type: nauc_ndcg_at_100_diff1
      value: 29.082177715298503
    - type: nauc_ndcg_at_100_max
      value: 45.24750203464315
    - type: nauc_ndcg_at_100_std
      value: 27.146548925680914
    - type: nauc_ndcg_at_10_diff1
      value: 25.123554466093594
    - type: nauc_ndcg_at_10_max
      value: 42.74355537806512
    - type: nauc_ndcg_at_10_std
      value: 22.234407997803935
    - type: nauc_ndcg_at_1_diff1
      value: 33.75083940012058
    - type: nauc_ndcg_at_1_max
      value: 44.44319402133161
    - type: nauc_ndcg_at_1_std
      value: 19.146499358406487
    - type: nauc_ndcg_at_20_diff1
      value: 24.954207968331872
    - type: nauc_ndcg_at_20_max
      value: 41.25991844405748
    - type: nauc_ndcg_at_20_std
      value: 22.169009285868864
    - type: nauc_ndcg_at_3_diff1
      value: 28.186539942033516
    - type: nauc_ndcg_at_3_max
      value: 44.40790009754965
    - type: nauc_ndcg_at_3_std
      value: 20.99226576085115
    - type: nauc_ndcg_at_5_diff1
      value: 25.498387899376706
    - type: nauc_ndcg_at_5_max
      value: 43.174709766261316
    - type: nauc_ndcg_at_5_std
      value: 21.88111962672031
    - type: nauc_precision_at_1000_diff1
      value: -16.22321012507648
    - type: nauc_precision_at_1000_max
      value: 5.808852256649677
    - type: nauc_precision_at_1000_std
      value: 19.875641776698824
    - type: nauc_precision_at_100_diff1
      value: -10.248089374355486
    - type: nauc_precision_at_100_max
      value: 19.29065415127588
    - type: nauc_precision_at_100_std
      value: 31.75019665627339
    - type: nauc_precision_at_10_diff1
      value: 3.6783257583955056
    - type: nauc_precision_at_10_max
      value: 39.22286010695767
    - type: nauc_precision_at_10_std
      value: 31.225485732801022
    - type: nauc_precision_at_1_diff1
      value: 32.57632582147155
    - type: nauc_precision_at_1_max
      value: 46.020072246328816
    - type: nauc_precision_at_1_std
      value: 20.99097889820076
    - type: nauc_precision_at_20_diff1
      value: -3.1632510833242784
    - type: nauc_precision_at_20_max
      value: 31.575496762405734
    - type: nauc_precision_at_20_std
      value: 31.576283324468115
    - type: nauc_precision_at_3_diff1
      value: 17.78864585545647
    - type: nauc_precision_at_3_max
      value: 44.201289661125585
    - type: nauc_precision_at_3_std
      value: 25.447840649726693
    - type: nauc_precision_at_5_diff1
      value: 9.986748662091358
    - type: nauc_precision_at_5_max
      value: 41.214164860776755
    - type: nauc_precision_at_5_std
      value: 28.22551704127726
    - type: nauc_recall_at_1000_diff1
      value: 10.984331766850506
    - type: nauc_recall_at_1000_max
      value: 24.641216018034104
    - type: nauc_recall_at_1000_std
      value: 26.91064221008446
    - type: nauc_recall_at_100_diff1
      value: 23.7009352078473
    - type: nauc_recall_at_100_max
      value: 30.176031609451297
    - type: nauc_recall_at_100_std
      value: 20.360365243211564
    - type: nauc_recall_at_10_diff1
      value: 28.11831737650638
    - type: nauc_recall_at_10_max
      value: 24.21539670487414
    - type: nauc_recall_at_10_std
      value: 2.245504974150148
    - type: nauc_recall_at_1_diff1
      value: 54.30208426149679
    - type: nauc_recall_at_1_max
      value: 18.69125148481608
    - type: nauc_recall_at_1_std
      value: -8.970955660291802
    - type: nauc_recall_at_20_diff1
      value: 26.199425305139908
    - type: nauc_recall_at_20_max
      value: 24.66704097503736
    - type: nauc_recall_at_20_std
      value: 5.86052107206246
    - type: nauc_recall_at_3_diff1
      value: 42.88348677575622
    - type: nauc_recall_at_3_max
      value: 21.189371077603308
    - type: nauc_recall_at_3_std
      value: -4.537510127238226
    - type: nauc_recall_at_5_diff1
      value: 30.7936756722569
    - type: nauc_recall_at_5_max
      value: 21.06136406164962
    - type: nauc_recall_at_5_std
      value: -1.4113804735229794
    - type: ndcg_at_1
      value: 45.975
    - type: ndcg_at_10
      value: 36.201
    - type: ndcg_at_100
      value: 32.736
    - type: ndcg_at_1000
      value: 41.099000000000004
    - type: ndcg_at_20
      value: 33.724
    - type: ndcg_at_3
      value: 42.242000000000004
    - type: ndcg_at_5
      value: 40.137
    - type: precision_at_1
      value: 47.678
    - type: precision_at_10
      value: 26.904
    - type: precision_at_100
      value: 8.368
    - type: precision_at_1000
      value: 2.078
    - type: precision_at_20
      value: 19.845
    - type: precision_at_3
      value: 40.351
    - type: precision_at_5
      value: 35.108
    - type: recall_at_1
      value: 5.654
    - type: recall_at_10
      value: 17.793
    - type: recall_at_100
      value: 32.483000000000004
    - type: recall_at_1000
      value: 63.294
    - type: recall_at_20
      value: 21.754
    - type: recall_at_3
      value: 10.771
    - type: recall_at_5
      value: 14.084
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NQ
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
      split: test
      type: mteb/nq
    metrics:
    - type: main_score
      value: 62.464
    - type: map_at_1
      value: 38.0
    - type: map_at_10
      value: 54.806
    - type: map_at_100
      value: 55.599
    - type: map_at_1000
      value: 55.617000000000004
    - type: map_at_20
      value: 55.336
    - type: map_at_3
      value: 50.58200000000001
    - type: map_at_5
      value: 53.181
    - type: mrr_at_1
      value: 42.46813441483198
    - type: mrr_at_10
      value: 57.060710147326446
    - type: mrr_at_100
      value: 57.60978373431328
    - type: mrr_at_1000
      value: 57.62192762809547
    - type: mrr_at_20
      value: 57.43431796174232
    - type: mrr_at_3
      value: 53.78041714947835
    - type: mrr_at_5
      value: 55.81257242178437
    - type: nauc_map_at_1000_diff1
      value: 38.337572188308194
    - type: nauc_map_at_1000_max
      value: 27.550035254787197
    - type: nauc_map_at_1000_std
      value: -7.5513729587308145
    - type: nauc_map_at_100_diff1
      value: 38.335337794455015
    - type: nauc_map_at_100_max
      value: 27.56919614414171
    - type: nauc_map_at_100_std
      value: -7.526017855405723
    - type: nauc_map_at_10_diff1
      value: 38.308131361353816
    - type: nauc_map_at_10_max
      value: 27.691849580929933
    - type: nauc_map_at_10_std
      value: -7.971461731555123
    - type: nauc_map_at_1_diff1
      value: 42.721072690634884
    - type: nauc_map_at_1_max
      value: 21.750451486885332
    - type: nauc_map_at_1_std
      value: -9.99540950522643
    - type: nauc_map_at_20_diff1
      value: 38.25792874982169
    - type: nauc_map_at_20_max
      value: 27.68877906159661
    - type: nauc_map_at_20_std
      value: -7.560753583212102
    - type: nauc_map_at_3_diff1
      value: 37.950570055936254
    - type: nauc_map_at_3_max
      value: 26.257969511794858
    - type: nauc_map_at_3_std
      value: -9.236868658300553
    - type: nauc_map_at_5_diff1
      value: 37.99893219450212
    - type: nauc_map_at_5_max
      value: 27.293454259158057
    - type: nauc_map_at_5_std
      value: -8.734089449603806
    - type: nauc_mrr_at_1000_diff1
      value: 37.777767467474774
    - type: nauc_mrr_at_1000_max
      value: 27.39507603748298
    - type: nauc_mrr_at_1000_std
      value: -5.554754076870114
    - type: nauc_mrr_at_100_diff1
      value: 37.77981674583538
    - type: nauc_mrr_at_100_max
      value: 27.411100989441557
    - type: nauc_mrr_at_100_std
      value: -5.539061231412731
    - type: nauc_mrr_at_10_diff1
      value: 37.72399003363479
    - type: nauc_mrr_at_10_max
      value: 27.618142546685416
    - type: nauc_mrr_at_10_std
      value: -5.6819843907448195
    - type: nauc_mrr_at_1_diff1
      value: 41.17596078958236
    - type: nauc_mrr_at_1_max
      value: 23.32588591818617
    - type: nauc_mrr_at_1_std
      value: -7.126628034623689
    - type: nauc_mrr_at_20_diff1
      value: 37.695136721588
    - type: nauc_mrr_at_20_max
      value: 27.52850676467322
    - type: nauc_mrr_at_20_std
      value: -5.50667995515647
    - type: nauc_mrr_at_3_diff1
      value: 37.23845700908964
    - type: nauc_mrr_at_3_max
      value: 26.69389772971012
    - type: nauc_mrr_at_3_std
      value: -6.31868405989011
    - type: nauc_mrr_at_5_diff1
      value: 37.33757394192838
    - type: nauc_mrr_at_5_max
      value: 27.42091593836207
    - type: nauc_mrr_at_5_std
      value: -5.993243330132065
    - type: nauc_ndcg_at_1000_diff1
      value: 37.74836061640332
    - type: nauc_ndcg_at_1000_max
      value: 29.03148916289089
    - type: nauc_ndcg_at_1000_std
      value: -5.543065770074502
    - type: nauc_ndcg_at_100_diff1
      value: 37.75593955089626
    - type: nauc_ndcg_at_100_max
      value: 29.67109480272493
    - type: nauc_ndcg_at_100_std
      value: -4.773697596687493
    - type: nauc_ndcg_at_10_diff1
      value: 37.41701174824348
    - type: nauc_ndcg_at_10_max
      value: 30.448703434043445
    - type: nauc_ndcg_at_10_std
      value: -6.306202666419071
    - type: nauc_ndcg_at_1_diff1
      value: 41.17596078958236
    - type: nauc_ndcg_at_1_max
      value: 23.32588591818617
    - type: nauc_ndcg_at_1_std
      value: -7.126628034623689
    - type: nauc_ndcg_at_20_diff1
      value: 37.17445197824622
    - type: nauc_ndcg_at_20_max
      value: 30.47378561555209
    - type: nauc_ndcg_at_20_std
      value: -4.921584853993488
    - type: nauc_ndcg_at_3_diff1
      value: 36.5261976812068
    - type: nauc_ndcg_at_3_max
      value: 27.560538820208926
    - type: nauc_ndcg_at_3_std
      value: -8.556686332882931
    - type: nauc_ndcg_at_5_diff1
      value: 36.571462759614526
    - type: nauc_ndcg_at_5_max
      value: 29.363401730752585
    - type: nauc_ndcg_at_5_std
      value: -7.825739170420347
    - type: nauc_precision_at_1000_diff1
      value: -12.588899483401223
    - type: nauc_precision_at_1000_max
      value: 2.641097890578701
    - type: nauc_precision_at_1000_std
      value: 17.643107625788748
    - type: nauc_precision_at_100_diff1
      value: -8.40579874206785
    - type: nauc_precision_at_100_max
      value: 9.725496771040037
    - type: nauc_precision_at_100_std
      value: 21.558582760191243
    - type: nauc_precision_at_10_diff1
      value: 6.619157191854486
    - type: nauc_precision_at_10_max
      value: 23.767406373688402
    - type: nauc_precision_at_10_std
      value: 10.428535003478808
    - type: nauc_precision_at_1_diff1
      value: 41.17596078958236
    - type: nauc_precision_at_1_max
      value: 23.32588591818617
    - type: nauc_precision_at_1_std
      value: -7.126628034623689
    - type: nauc_precision_at_20_diff1
      value: -0.6449974218292859
    - type: nauc_precision_at_20_max
      value: 20.211503851418783
    - type: nauc_precision_at_20_std
      value: 17.922745410142575
    - type: nauc_precision_at_3_diff1
      value: 19.710276097428657
    - type: nauc_precision_at_3_max
      value: 26.768918044758706
    - type: nauc_precision_at_3_std
      value: -1.0636448912049246
    - type: nauc_precision_at_5_diff1
      value: 13.073181337982613
    - type: nauc_precision_at_5_max
      value: 26.418340338971024
    - type: nauc_precision_at_5_std
      value: 2.9842078949528688
    - type: nauc_recall_at_1000_diff1
      value: 30.52411148739828
    - type: nauc_recall_at_1000_max
      value: 90.96409807536762
    - type: nauc_recall_at_1000_std
      value: 83.94857830921949
    - type: nauc_recall_at_100_diff1
      value: 36.936303690592155
    - type: nauc_recall_at_100_max
      value: 71.91515014325869
    - type: nauc_recall_at_100_std
      value: 48.93061263403371
    - type: nauc_recall_at_10_diff1
      value: 32.84292362076269
    - type: nauc_recall_at_10_max
      value: 44.27252783122478
    - type: nauc_recall_at_10_std
      value: -1.5981198975612385
    - type: nauc_recall_at_1_diff1
      value: 42.721072690634884
    - type: nauc_recall_at_1_max
      value: 21.750451486885332
    - type: nauc_recall_at_1_std
      value: -9.99540950522643
    - type: nauc_recall_at_20_diff1
      value: 29.36724417081702
    - type: nauc_recall_at_20_max
      value: 52.035846390214715
    - type: nauc_recall_at_20_std
      value: 11.967264191332818
    - type: nauc_recall_at_3_diff1
      value: 31.634923771936098
    - type: nauc_recall_at_3_max
      value: 30.225743369869473
    - type: nauc_recall_at_3_std
      value: -9.253665347118615
    - type: nauc_recall_at_5_diff1
      value: 30.66271853090737
    - type: nauc_recall_at_5_max
      value: 35.70815715994996
    - type: nauc_recall_at_5_std
      value: -7.836012956078996
    - type: ndcg_at_1
      value: 42.468
    - type: ndcg_at_10
      value: 62.464
    - type: ndcg_at_100
      value: 65.618
    - type: ndcg_at_1000
      value: 66.014
    - type: ndcg_at_20
      value: 64.12
    - type: ndcg_at_3
      value: 54.790000000000006
    - type: ndcg_at_5
      value: 58.992
    - type: precision_at_1
      value: 42.468
    - type: precision_at_10
      value: 9.959
    - type: precision_at_100
      value: 1.174
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_20
      value: 5.380999999999999
    - type: precision_at_3
      value: 24.73
    - type: precision_at_5
      value: 17.299999999999997
    - type: recall_at_1
      value: 38.0
    - type: recall_at_10
      value: 83.22699999999999
    - type: recall_at_100
      value: 96.584
    - type: recall_at_1000
      value: 99.512
    - type: recall_at_20
      value: 89.291
    - type: recall_at_3
      value: 63.666
    - type: recall_at_5
      value: 73.27900000000001
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB QuoraRetrieval
      revision: e4e08e0b7dbe3c8700f0daef558ff32256715259
      split: test
      type: mteb/quora
    metrics:
    - type: main_score
      value: 87.366
    - type: map_at_1
      value: 69.95700000000001
    - type: map_at_10
      value: 83.55
    - type: map_at_100
      value: 84.196
    - type: map_at_1000
      value: 84.21600000000001
    - type: map_at_20
      value: 83.982
    - type: map_at_3
      value: 80.647
    - type: map_at_5
      value: 82.443
    - type: mrr_at_1
      value: 80.39
    - type: mrr_at_10
      value: 86.65646031746004
    - type: mrr_at_100
      value: 86.7852113210373
    - type: mrr_at_1000
      value: 86.78651118354796
    - type: mrr_at_20
      value: 86.75772838878498
    - type: mrr_at_3
      value: 85.67499999999971
    - type: mrr_at_5
      value: 86.33749999999962
    - type: nauc_map_at_1000_diff1
      value: 76.68189702770007
    - type: nauc_map_at_1000_max
      value: 36.19988239025682
    - type: nauc_map_at_1000_std
      value: -26.231691135645736
    - type: nauc_map_at_100_diff1
      value: 76.68832712120171
    - type: nauc_map_at_100_max
      value: 36.18627717337547
    - type: nauc_map_at_100_std
      value: -26.28243886166
    - type: nauc_map_at_10_diff1
      value: 76.88888516032657
    - type: nauc_map_at_10_max
      value: 35.69809861085124
    - type: nauc_map_at_10_std
      value: -27.859425473864224
    - type: nauc_map_at_1_diff1
      value: 79.5243725217315
    - type: nauc_map_at_1_max
      value: 27.092773841207002
    - type: nauc_map_at_1_std
      value: -26.223200911204543
    - type: nauc_map_at_20_diff1
      value: 76.74938996155176
    - type: nauc_map_at_20_max
      value: 36.07373781351406
    - type: nauc_map_at_20_std
      value: -26.891400098628015
    - type: nauc_map_at_3_diff1
      value: 77.29604745045076
    - type: nauc_map_at_3_max
      value: 33.11431059356283
    - type: nauc_map_at_3_std
      value: -29.555237195931085
    - type: nauc_map_at_5_diff1
      value: 77.14069217901078
    - type: nauc_map_at_5_max
      value: 34.68656073526487
    - type: nauc_map_at_5_std
      value: -28.945053669861508
    - type: nauc_mrr_at_1000_diff1
      value: 76.66087451567746
    - type: nauc_mrr_at_1000_max
      value: 38.78133177265328
    - type: nauc_mrr_at_1000_std
      value: -23.75726541774991
    - type: nauc_mrr_at_100_diff1
      value: 76.66117078261013
    - type: nauc_mrr_at_100_max
      value: 38.782533036423885
    - type: nauc_mrr_at_100_std
      value: -23.752587601473568
    - type: nauc_mrr_at_10_diff1
      value: 76.65866401411019
    - type: nauc_mrr_at_10_max
      value: 38.87950311049704
    - type: nauc_mrr_at_10_std
      value: -23.873660706680578
    - type: nauc_mrr_at_1_diff1
      value: 77.42633506487041
    - type: nauc_mrr_at_1_max
      value: 37.93973722217786
    - type: nauc_mrr_at_1_std
      value: -23.3984130771317
    - type: nauc_mrr_at_20_diff1
      value: 76.66210684923414
    - type: nauc_mrr_at_20_max
      value: 38.81293033048911
    - type: nauc_mrr_at_20_std
      value: -23.736590746133736
    - type: nauc_mrr_at_3_diff1
      value: 76.33711764736019
    - type: nauc_mrr_at_3_max
      value: 38.5659231830368
    - type: nauc_mrr_at_3_std
      value: -23.99588149124865
    - type: nauc_mrr_at_5_diff1
      value: 76.57123830226054
    - type: nauc_mrr_at_5_max
      value: 38.97947097392977
    - type: nauc_mrr_at_5_std
      value: -23.943668957974246
    - type: nauc_ndcg_at_1000_diff1
      value: 76.38447339050585
    - type: nauc_ndcg_at_1000_max
      value: 37.756822792877934
    - type: nauc_ndcg_at_1000_std
      value: -24.046995734357164
    - type: nauc_ndcg_at_100_diff1
      value: 76.44058018066822
    - type: nauc_ndcg_at_100_max
      value: 37.72948294169218
    - type: nauc_ndcg_at_100_std
      value: -24.083432140741795
    - type: nauc_ndcg_at_10_diff1
      value: 76.56246287923074
    - type: nauc_ndcg_at_10_max
      value: 37.0329253490553
    - type: nauc_ndcg_at_10_std
      value: -26.6495163705961
    - type: nauc_ndcg_at_1_diff1
      value: 77.4085129990432
    - type: nauc_ndcg_at_1_max
      value: 38.06139172214421
    - type: nauc_ndcg_at_1_std
      value: -23.656477126977386
    - type: nauc_ndcg_at_20_diff1
      value: 76.50192496743098
    - type: nauc_ndcg_at_20_max
      value: 37.51759311013985
    - type: nauc_ndcg_at_20_std
      value: -25.45517058360004
    - type: nauc_ndcg_at_3_diff1
      value: 75.94398494081794
    - type: nauc_ndcg_at_3_max
      value: 35.7666711547279
    - type: nauc_ndcg_at_3_std
      value: -26.866022682361578
    - type: nauc_ndcg_at_5_diff1
      value: 76.47334274088344
    - type: nauc_ndcg_at_5_max
      value: 36.40830331490731
    - type: nauc_ndcg_at_5_std
      value: -27.170121189572765
    - type: nauc_precision_at_1000_diff1
      value: -43.33672630765437
    - type: nauc_precision_at_1000_max
      value: -5.089751329149161
    - type: nauc_precision_at_1000_std
      value: 30.6241447847051
    - type: nauc_precision_at_100_diff1
      value: -42.736833035629864
    - type: nauc_precision_at_100_max
      value: -4.060198408346224
    - type: nauc_precision_at_100_std
      value: 29.807050266205344
    - type: nauc_precision_at_10_diff1
      value: -35.90810562245906
    - type: nauc_precision_at_10_max
      value: 1.1633204529249133
    - type: nauc_precision_at_10_std
      value: 20.129691203276018
    - type: nauc_precision_at_1_diff1
      value: 77.4085129990432
    - type: nauc_precision_at_1_max
      value: 38.06139172214421
    - type: nauc_precision_at_1_std
      value: -23.656477126977386
    - type: nauc_precision_at_20_diff1
      value: -40.2132286912738
    - type: nauc_precision_at_20_max
      value: -1.3004735030734194
    - type: nauc_precision_at_20_std
      value: 25.15612293757488
    - type: nauc_precision_at_3_diff1
      value: -13.873825299883904
    - type: nauc_precision_at_3_max
      value: 11.038689278907233
    - type: nauc_precision_at_3_std
      value: 5.4276449621706
    - type: nauc_precision_at_5_diff1
      value: -27.151668633894737
    - type: nauc_precision_at_5_max
      value: 5.795130010163115
    - type: nauc_precision_at_5_std
      value: 13.220722167587375
    - type: nauc_recall_at_1000_diff1
      value: 83.903950427863
    - type: nauc_recall_at_1000_max
      value: 37.82919000897223
    - type: nauc_recall_at_1000_std
      value: 70.65670846771707
    - type: nauc_recall_at_100_diff1
      value: 75.23306095335836
    - type: nauc_recall_at_100_max
      value: 37.54281648247423
    - type: nauc_recall_at_100_std
      value: 8.434289114377373
    - type: nauc_recall_at_10_diff1
      value: 72.7872912723047
    - type: nauc_recall_at_10_max
      value: 34.261519652104184
    - type: nauc_recall_at_10_std
      value: -34.60101950810808
    - type: nauc_recall_at_1_diff1
      value: 79.5243725217315
    - type: nauc_recall_at_1_max
      value: 27.092773841207002
    - type: nauc_recall_at_1_std
      value: -26.223200911204543
    - type: nauc_recall_at_20_diff1
      value: 72.8297963091964
    - type: nauc_recall_at_20_max
      value: 36.070220569670916
    - type: nauc_recall_at_20_std
      value: -27.20897179168245
    - type: nauc_recall_at_3_diff1
      value: 73.47456374650459
    - type: nauc_recall_at_3_max
      value: 29.901663407294816
    - type: nauc_recall_at_3_std
      value: -32.83329537040381
    - type: nauc_recall_at_5_diff1
      value: 73.05025750827126
    - type: nauc_recall_at_5_max
      value: 32.35733470860963
    - type: nauc_recall_at_5_std
      value: -34.32357558493091
    - type: ndcg_at_1
      value: 80.4
    - type: ndcg_at_10
      value: 87.366
    - type: ndcg_at_100
      value: 88.7
    - type: ndcg_at_1000
      value: 88.842
    - type: ndcg_at_20
      value: 88.11
    - type: ndcg_at_3
      value: 84.52499999999999
    - type: ndcg_at_5
      value: 86.047
    - type: precision_at_1
      value: 80.4
    - type: precision_at_10
      value: 13.235
    - type: precision_at_100
      value: 1.516
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_20
      value: 7.037
    - type: precision_at_3
      value: 36.9
    - type: precision_at_5
      value: 24.236
    - type: recall_at_1
      value: 69.95700000000001
    - type: recall_at_10
      value: 94.535
    - type: recall_at_100
      value: 99.164
    - type: recall_at_1000
      value: 99.855
    - type: recall_at_20
      value: 96.974
    - type: recall_at_3
      value: 86.33800000000001
    - type: recall_at_5
      value: 90.69
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SCIDOCS
      revision: f8c2fcf00f625baaa80f62ec5bd9e1fff3b8ae88
      split: test
      type: mteb/scidocs
    metrics:
    - type: main_score
      value: 21.492
    - type: map_at_1
      value: 5.192
    - type: map_at_10
      value: 12.959000000000001
    - type: map_at_100
      value: 14.963999999999999
    - type: map_at_1000
      value: 15.261
    - type: map_at_20
      value: 13.988999999999999
    - type: map_at_3
      value: 9.235
    - type: map_at_5
      value: 11.042
    - type: mrr_at_1
      value: 25.5
    - type: mrr_at_10
      value: 36.37313492063491
    - type: mrr_at_100
      value: 37.36517957347626
    - type: mrr_at_1000
      value: 37.42538601073437
    - type: mrr_at_20
      value: 36.987896404421136
    - type: mrr_at_3
      value: 32.966666666666654
    - type: mrr_at_5
      value: 34.95166666666664
    - type: nauc_map_at_1000_diff1
      value: 13.635120934154395
    - type: nauc_map_at_1000_max
      value: 28.03542983005195
    - type: nauc_map_at_1000_std
      value: 17.07156940311778
    - type: nauc_map_at_100_diff1
      value: 13.59237295184475
    - type: nauc_map_at_100_max
      value: 27.992291365051237
    - type: nauc_map_at_100_std
      value: 16.926533467400464
    - type: nauc_map_at_10_diff1
      value: 14.149193235999993
    - type: nauc_map_at_10_max
      value: 26.520643811139305
    - type: nauc_map_at_10_std
      value: 13.168673602548925
    - type: nauc_map_at_1_diff1
      value: 20.096094508148465
    - type: nauc_map_at_1_max
      value: 17.41582245576302
    - type: nauc_map_at_1_std
      value: 5.771729007558897
    - type: nauc_map_at_20_diff1
      value: 13.977726400526427
    - type: nauc_map_at_20_max
      value: 27.2322235491895
    - type: nauc_map_at_20_std
      value: 14.972781677750435
    - type: nauc_map_at_3_diff1
      value: 17.371153027460355
    - type: nauc_map_at_3_max
      value: 24.457758503208254
    - type: nauc_map_at_3_std
      value: 7.719726821179824
    - type: nauc_map_at_5_diff1
      value: 14.600442843442574
    - type: nauc_map_at_5_max
      value: 25.899736370856296
    - type: nauc_map_at_5_std
      value: 10.125349354853359
    - type: nauc_mrr_at_1000_diff1
      value: 18.70342821390236
    - type: nauc_mrr_at_1000_max
      value: 23.365194520549114
    - type: nauc_mrr_at_1000_std
      value: 12.185114294903236
    - type: nauc_mrr_at_100_diff1
      value: 18.677858738015907
    - type: nauc_mrr_at_100_max
      value: 23.372641996726742
    - type: nauc_mrr_at_100_std
      value: 12.216130561991909
    - type: nauc_mrr_at_10_diff1
      value: 18.79094453090232
    - type: nauc_mrr_at_10_max
      value: 23.511686337006466
    - type: nauc_mrr_at_10_std
      value: 11.879716687008134
    - type: nauc_mrr_at_1_diff1
      value: 20.10455171810408
    - type: nauc_mrr_at_1_max
      value: 17.741566234315428
    - type: nauc_mrr_at_1_std
      value: 6.1676764583652215
    - type: nauc_mrr_at_20_diff1
      value: 18.70143648544655
    - type: nauc_mrr_at_20_max
      value: 23.45603239095019
    - type: nauc_mrr_at_20_std
      value: 12.244613576686202
    - type: nauc_mrr_at_3_diff1
      value: 18.894662528857374
    - type: nauc_mrr_at_3_max
      value: 23.3739038101588
    - type: nauc_mrr_at_3_std
      value: 10.4709044796543
    - type: nauc_mrr_at_5_diff1
      value: 18.877786065095563
    - type: nauc_mrr_at_5_max
      value: 23.78061081203872
    - type: nauc_mrr_at_5_std
      value: 11.847882917869622
    - type: nauc_ndcg_at_1000_diff1
      value: 13.99159027398115
    - type: nauc_ndcg_at_1000_max
      value: 29.44766808611483
    - type: nauc_ndcg_at_1000_std
      value: 24.289749574699915
    - type: nauc_ndcg_at_100_diff1
      value: 13.164020363258746
    - type: nauc_ndcg_at_100_max
      value: 29.642442997167723
    - type: nauc_ndcg_at_100_std
      value: 23.761764515453866
    - type: nauc_ndcg_at_10_diff1
      value: 14.839883268638546
    - type: nauc_ndcg_at_10_max
      value: 27.21043708455449
    - type: nauc_ndcg_at_10_std
      value: 15.56110419291775
    - type: nauc_ndcg_at_1_diff1
      value: 20.10455171810408
    - type: nauc_ndcg_at_1_max
      value: 17.741566234315428
    - type: nauc_ndcg_at_1_std
      value: 6.1676764583652215
    - type: nauc_ndcg_at_20_diff1
      value: 14.27998110295395
    - type: nauc_ndcg_at_20_max
      value: 28.2492026337839
    - type: nauc_ndcg_at_20_std
      value: 18.822356982979105
    - type: nauc_ndcg_at_3_diff1
      value: 17.659263157535445
    - type: nauc_ndcg_at_3_max
      value: 25.416706421591396
    - type: nauc_ndcg_at_3_std
      value: 9.650689638152636
    - type: nauc_ndcg_at_5_diff1
      value: 15.38459833918123
    - type: nauc_ndcg_at_5_max
      value: 26.92495519416969
    - type: nauc_ndcg_at_5_std
      value: 12.71017696809276
    - type: nauc_precision_at_1000_diff1
      value: 6.128490135458364
    - type: nauc_precision_at_1000_max
      value: 23.52693893261883
    - type: nauc_precision_at_1000_std
      value: 36.280432732819925
    - type: nauc_precision_at_100_diff1
      value: 5.306163791220436
    - type: nauc_precision_at_100_max
      value: 27.67851033239246
    - type: nauc_precision_at_100_std
      value: 34.29821573752515
    - type: nauc_precision_at_10_diff1
      value: 10.829686435425472
    - type: nauc_precision_at_10_max
      value: 27.201648684015318
    - type: nauc_precision_at_10_std
      value: 19.376999508233254
    - type: nauc_precision_at_1_diff1
      value: 20.10455171810408
    - type: nauc_precision_at_1_max
      value: 17.741566234315428
    - type: nauc_precision_at_1_std
      value: 6.1676764583652215
    - type: nauc_precision_at_20_diff1
      value: 9.416169626702048
    - type: nauc_precision_at_20_max
      value: 27.65257998670333
    - type: nauc_precision_at_20_std
      value: 24.761868509805826
    - type: nauc_precision_at_3_diff1
      value: 16.666456902017348
    - type: nauc_precision_at_3_max
      value: 27.9969730961105
    - type: nauc_precision_at_3_std
      value: 10.991562741393231
    - type: nauc_precision_at_5_diff1
      value: 12.26205064462843
    - type: nauc_precision_at_5_max
      value: 29.083848730874095
    - type: nauc_precision_at_5_std
      value: 15.66630836555747
    - type: nauc_recall_at_1000_diff1
      value: 5.600277836894063
    - type: nauc_recall_at_1000_max
      value: 23.228705161815526
    - type: nauc_recall_at_1000_std
      value: 36.822431061799485
    - type: nauc_recall_at_100_diff1
      value: 4.991781244867178
    - type: nauc_recall_at_100_max
      value: 27.70095625483475
    - type: nauc_recall_at_100_std
      value: 34.67168431597854
    - type: nauc_recall_at_10_diff1
      value: 10.580860425931972
    - type: nauc_recall_at_10_max
      value: 27.145829414223666
    - type: nauc_recall_at_10_std
      value: 19.330630157067382
    - type: nauc_recall_at_1_diff1
      value: 20.096094508148465
    - type: nauc_recall_at_1_max
      value: 17.41582245576302
    - type: nauc_recall_at_1_std
      value: 5.771729007558897
    - type: nauc_recall_at_20_diff1
      value: 9.06945331260344
    - type: nauc_recall_at_20_max
      value: 27.56725251066482
    - type: nauc_recall_at_20_std
      value: 24.77644509886098
    - type: nauc_recall_at_3_diff1
      value: 16.660507676429322
    - type: nauc_recall_at_3_max
      value: 27.816546386536434
    - type: nauc_recall_at_3_std
      value: 10.687824478247007
    - type: nauc_recall_at_5_diff1
      value: 11.992514446369388
    - type: nauc_recall_at_5_max
      value: 28.789031176671948
    - type: nauc_recall_at_5_std
      value: 15.422118990090805
    - type: ndcg_at_1
      value: 25.5
    - type: ndcg_at_10
      value: 21.492
    - type: ndcg_at_100
      value: 29.022
    - type: ndcg_at_1000
      value: 34.298
    - type: ndcg_at_20
      value: 24.237000000000002
    - type: ndcg_at_3
      value: 20.392
    - type: ndcg_at_5
      value: 17.801000000000002
    - type: precision_at_1
      value: 25.5
    - type: precision_at_10
      value: 11.09
    - type: precision_at_100
      value: 2.1919999999999997
    - type: precision_at_1000
      value: 0.346
    - type: precision_at_20
      value: 7.135
    - type: precision_at_3
      value: 18.933
    - type: precision_at_5
      value: 15.52
    - type: recall_at_1
      value: 5.192
    - type: recall_at_10
      value: 22.512999999999998
    - type: recall_at_100
      value: 44.505
    - type: recall_at_1000
      value: 70.267
    - type: recall_at_20
      value: 28.965000000000003
    - type: recall_at_3
      value: 11.522
    - type: recall_at_5
      value: 15.751999999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SciFact
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
      split: test
      type: mteb/scifact
    metrics:
    - type: main_score
      value: 71.586
    - type: map_at_1
      value: 56.760999999999996
    - type: map_at_10
      value: 66.893
    - type: map_at_100
      value: 67.42
    - type: map_at_1000
      value: 67.44200000000001
    - type: map_at_20
      value: 67.232
    - type: map_at_3
      value: 64.193
    - type: map_at_5
      value: 65.73400000000001
    - type: mrr_at_1
      value: 60.0
    - type: mrr_at_10
      value: 68.20383597883595
    - type: mrr_at_100
      value: 68.58867453733343
    - type: mrr_at_1000
      value: 68.61117469977329
    - type: mrr_at_20
      value: 68.43973740684265
    - type: mrr_at_3
      value: 66.11111111111111
    - type: mrr_at_5
      value: 67.44444444444446
    - type: nauc_map_at_1000_diff1
      value: 72.66688261123035
    - type: nauc_map_at_1000_max
      value: 61.02926282006283
    - type: nauc_map_at_1000_std
      value: 11.084549829740526
    - type: nauc_map_at_100_diff1
      value: 72.66226192320828
    - type: nauc_map_at_100_max
      value: 61.04393223108811
    - type: nauc_map_at_100_std
      value: 11.101529343291695
    - type: nauc_map_at_10_diff1
      value: 72.66732266693091
    - type: nauc_map_at_10_max
      value: 61.24124296311832
    - type: nauc_map_at_10_std
      value: 10.91179451961794
    - type: nauc_map_at_1_diff1
      value: 74.2356464256346
    - type: nauc_map_at_1_max
      value: 54.06962758957632
    - type: nauc_map_at_1_std
      value: 0.8037891907963532
    - type: nauc_map_at_20_diff1
      value: 72.65198594061253
    - type: nauc_map_at_20_max
      value: 61.130159351448185
    - type: nauc_map_at_20_std
      value: 11.2246899245522
    - type: nauc_map_at_3_diff1
      value: 72.78578673303954
    - type: nauc_map_at_3_max
      value: 59.19073262936321
    - type: nauc_map_at_3_std
      value: 8.460301560522968
    - type: nauc_map_at_5_diff1
      value: 72.55004168261968
    - type: nauc_map_at_5_max
      value: 59.75181935082357
    - type: nauc_map_at_5_std
      value: 9.440299527201889
    - type: nauc_mrr_at_1000_diff1
      value: 72.82720348470325
    - type: nauc_mrr_at_1000_max
      value: 62.344231223741446
    - type: nauc_mrr_at_1000_std
      value: 12.60196558488974
    - type: nauc_mrr_at_100_diff1
      value: 72.82236849255094
    - type: nauc_mrr_at_100_max
      value: 62.35799491393125
    - type: nauc_mrr_at_100_std
      value: 12.617900773655673
    - type: nauc_mrr_at_10_diff1
      value: 72.7722847495086
    - type: nauc_mrr_at_10_max
      value: 62.66642401155435
    - type: nauc_mrr_at_10_std
      value: 12.906381237738746
    - type: nauc_mrr_at_1_diff1
      value: 74.71208073612343
    - type: nauc_mrr_at_1_max
      value: 59.50430394775893
    - type: nauc_mrr_at_1_std
      value: 8.129514198080512
    - type: nauc_mrr_at_20_diff1
      value: 72.78312367361772
    - type: nauc_mrr_at_20_max
      value: 62.421122493761885
    - type: nauc_mrr_at_20_std
      value: 12.693437522498588
    - type: nauc_mrr_at_3_diff1
      value: 73.50670156385345
    - type: nauc_mrr_at_3_max
      value: 62.01717537699209
    - type: nauc_mrr_at_3_std
      value: 11.926548252191182
    - type: nauc_mrr_at_5_diff1
      value: 72.62204028549876
    - type: nauc_mrr_at_5_max
      value: 62.319358766312085
    - type: nauc_mrr_at_5_std
      value: 13.081257923284342
    - type: nauc_ndcg_at_1000_diff1
      value: 72.29960539074736
    - type: nauc_ndcg_at_1000_max
      value: 62.75096959221402
    - type: nauc_ndcg_at_1000_std
      value: 13.81528462505362
    - type: nauc_ndcg_at_100_diff1
      value: 72.19985782073529
    - type: nauc_ndcg_at_100_max
      value: 63.18837705326287
    - type: nauc_ndcg_at_100_std
      value: 14.506479655117138
    - type: nauc_ndcg_at_10_diff1
      value: 71.85759847832983
    - type: nauc_ndcg_at_10_max
      value: 64.150996056865
    - type: nauc_ndcg_at_10_std
      value: 14.580606901634278
    - type: nauc_ndcg_at_1_diff1
      value: 74.71208073612343
    - type: nauc_ndcg_at_1_max
      value: 59.50430394775893
    - type: nauc_ndcg_at_1_std
      value: 8.129514198080512
    - type: nauc_ndcg_at_20_diff1
      value: 71.80987178228351
    - type: nauc_ndcg_at_20_max
      value: 63.56269460865743
    - type: nauc_ndcg_at_20_std
      value: 15.024978004625922
    - type: nauc_ndcg_at_3_diff1
      value: 72.35095651602592
    - type: nauc_ndcg_at_3_max
      value: 61.60548011855679
    - type: nauc_ndcg_at_3_std
      value: 12.048248788835263
    - type: nauc_ndcg_at_5_diff1
      value: 71.48615621881864
    - type: nauc_ndcg_at_5_max
      value: 61.72870035979784
    - type: nauc_ndcg_at_5_std
      value: 12.83048357446691
    - type: nauc_precision_at_1000_diff1
      value: -14.743011420972
    - type: nauc_precision_at_1000_max
      value: 19.281995763080158
    - type: nauc_precision_at_1000_std
      value: 49.6140660398164
    - type: nauc_precision_at_100_diff1
      value: 0.11278174806205563
    - type: nauc_precision_at_100_max
      value: 29.704511820077332
    - type: nauc_precision_at_100_std
      value: 47.84916954122579
    - type: nauc_precision_at_10_diff1
      value: 20.498227967235728
    - type: nauc_precision_at_10_max
      value: 47.883119365891595
    - type: nauc_precision_at_10_std
      value: 45.182178693450595
    - type: nauc_precision_at_1_diff1
      value: 74.71208073612343
    - type: nauc_precision_at_1_max
      value: 59.50430394775893
    - type: nauc_precision_at_1_std
      value: 8.129514198080512
    - type: nauc_precision_at_20_diff1
      value: 12.551737222341455
    - type: nauc_precision_at_20_max
      value: 40.618899501225634
    - type: nauc_precision_at_20_std
      value: 48.5598454249067
    - type: nauc_precision_at_3_diff1
      value: 47.67720764601145
    - type: nauc_precision_at_3_max
      value: 56.50632017305064
    - type: nauc_precision_at_3_std
      value: 31.14175140162157
    - type: nauc_precision_at_5_diff1
      value: 35.10058622792819
    - type: nauc_precision_at_5_max
      value: 51.88948872657981
    - type: nauc_precision_at_5_std
      value: 37.62796957461928
    - type: nauc_recall_at_1000_diff1
      value: 79.57516339869238
    - type: nauc_recall_at_1000_max
      value: 86.11111111111035
    - type: nauc_recall_at_1000_std
      value: 79.57516339869238
    - type: nauc_recall_at_100_diff1
      value: 70.50859559510081
    - type: nauc_recall_at_100_max
      value: 79.17009941231396
    - type: nauc_recall_at_100_std
      value: 44.32910419069595
    - type: nauc_recall_at_10_diff1
      value: 66.16118569361245
    - type: nauc_recall_at_10_max
      value: 74.73542948302286
    - type: nauc_recall_at_10_std
      value: 27.680330939810037
    - type: nauc_recall_at_1_diff1
      value: 74.2356464256346
    - type: nauc_recall_at_1_max
      value: 54.06962758957632
    - type: nauc_recall_at_1_std
      value: 0.8037891907963532
    - type: nauc_recall_at_20_diff1
      value: 65.4748436545527
    - type: nauc_recall_at_20_max
      value: 73.81532199081235
    - type: nauc_recall_at_20_std
      value: 33.59324708196253
    - type: nauc_recall_at_3_diff1
      value: 68.83194804473622
    - type: nauc_recall_at_3_max
      value: 61.77722610439669
    - type: nauc_recall_at_3_std
      value: 13.984923756556714
    - type: nauc_recall_at_5_diff1
      value: 65.51467417209523
    - type: nauc_recall_at_5_max
      value: 64.08276291427661
    - type: nauc_recall_at_5_std
      value: 19.976472037847167
    - type: ndcg_at_1
      value: 60.0
    - type: ndcg_at_10
      value: 71.586
    - type: ndcg_at_100
      value: 73.76899999999999
    - type: ndcg_at_1000
      value: 74.386
    - type: ndcg_at_20
      value: 72.612
    - type: ndcg_at_3
      value: 66.944
    - type: ndcg_at_5
      value: 69.333
    - type: precision_at_1
      value: 60.0
    - type: precision_at_10
      value: 9.6
    - type: precision_at_100
      value: 1.073
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_20
      value: 5.033
    - type: precision_at_3
      value: 26.333000000000002
    - type: precision_at_5
      value: 17.4
    - type: recall_at_1
      value: 56.760999999999996
    - type: recall_at_10
      value: 84.589
    - type: recall_at_100
      value: 94.333
    - type: recall_at_1000
      value: 99.333
    - type: recall_at_20
      value: 88.43299999999999
    - type: recall_at_3
      value: 72.10600000000001
    - type: recall_at_5
      value: 78.194
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB TRECCOVID
      revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
      split: test
      type: mteb/trec-covid
    metrics:
    - type: main_score
      value: 84.60600000000001
    - type: map_at_1
      value: 0.257
    - type: map_at_10
      value: 2.196
    - type: map_at_100
      value: 13.252
    - type: map_at_1000
      value: 31.473000000000003
    - type: map_at_20
      value: 4.023000000000001
    - type: map_at_3
      value: 0.722
    - type: map_at_5
      value: 1.146
    - type: mrr_at_1
      value: 94.0
    - type: mrr_at_10
      value: 97.0
    - type: mrr_at_100
      value: 97.0
    - type: mrr_at_1000
      value: 97.0
    - type: mrr_at_20
      value: 97.0
    - type: mrr_at_3
      value: 97.0
    - type: mrr_at_5
      value: 97.0
    - type: nauc_map_at_1000_diff1
      value: -30.674816554207062
    - type: nauc_map_at_1000_max
      value: 53.18598689657068
    - type: nauc_map_at_1000_std
      value: 78.88325309469121
    - type: nauc_map_at_100_diff1
      value: -17.6877824653978
    - type: nauc_map_at_100_max
      value: 19.584159765315658
    - type: nauc_map_at_100_std
      value: 48.051154190992726
    - type: nauc_map_at_10_diff1
      value: 20.076631089898626
    - type: nauc_map_at_10_max
      value: -8.642556160185636
    - type: nauc_map_at_10_std
      value: -5.768698617334298
    - type: nauc_map_at_1_diff1
      value: 27.342260509653798
    - type: nauc_map_at_1_max
      value: -23.400451210297994
    - type: nauc_map_at_1_std
      value: -21.152006353733853
    - type: nauc_map_at_20_diff1
      value: 8.019321726240506
    - type: nauc_map_at_20_max
      value: -1.4826378210544222
    - type: nauc_map_at_20_std
      value: 5.698208117745366
    - type: nauc_map_at_3_diff1
      value: 32.073377946749446
    - type: nauc_map_at_3_max
      value: -13.099353983204654
    - type: nauc_map_at_3_std
      value: -15.36319127398037
    - type: nauc_map_at_5_diff1
      value: 22.500045815797876
    - type: nauc_map_at_5_max
      value: -8.548135411428023
    - type: nauc_map_at_5_std
      value: -8.547850460331334
    - type: nauc_mrr_at_1000_diff1
      value: -6.022408963585526
    - type: nauc_mrr_at_1000_max
      value: 4.481792717087155
    - type: nauc_mrr_at_1000_std
      value: 51.6962340491753
    - type: nauc_mrr_at_100_diff1
      value: -6.022408963585526
    - type: nauc_mrr_at_100_max
      value: 4.481792717087155
    - type: nauc_mrr_at_100_std
      value: 51.6962340491753
    - type: nauc_mrr_at_10_diff1
      value: -6.022408963585526
    - type: nauc_mrr_at_10_max
      value: 4.481792717087155
    - type: nauc_mrr_at_10_std
      value: 51.6962340491753
    - type: nauc_mrr_at_1_diff1
      value: -6.022408963585076
    - type: nauc_mrr_at_1_max
      value: 4.481792717087146
    - type: nauc_mrr_at_1_std
      value: 51.69623404917518
    - type: nauc_mrr_at_20_diff1
      value: -6.022408963585526
    - type: nauc_mrr_at_20_max
      value: 4.481792717087155
    - type: nauc_mrr_at_20_std
      value: 51.6962340491753
    - type: nauc_mrr_at_3_diff1
      value: -6.022408963585526
    - type: nauc_mrr_at_3_max
      value: 4.481792717087155
    - type: nauc_mrr_at_3_std
      value: 51.6962340491753
    - type: nauc_mrr_at_5_diff1
      value: -6.022408963585526
    - type: nauc_mrr_at_5_max
      value: 4.481792717087155
    - type: nauc_mrr_at_5_std
      value: 51.6962340491753
    - type: nauc_ndcg_at_1000_diff1
      value: -20.79697283984295
    - type: nauc_ndcg_at_1000_max
      value: 52.97671908009218
    - type: nauc_ndcg_at_1000_std
      value: 75.43907707019758
    - type: nauc_ndcg_at_100_diff1
      value: -38.620752706946455
    - type: nauc_ndcg_at_100_max
      value: 49.41307462381511
    - type: nauc_ndcg_at_100_std
      value: 81.33299379244252
    - type: nauc_ndcg_at_10_diff1
      value: -18.611906363037356
    - type: nauc_ndcg_at_10_max
      value: 44.20544651664479
    - type: nauc_ndcg_at_10_std
      value: 61.322552829935816
    - type: nauc_ndcg_at_1_diff1
      value: 18.625935567849073
    - type: nauc_ndcg_at_1_max
      value: -10.104132769280879
    - type: nauc_ndcg_at_1_std
      value: 22.449560689879743
    - type: nauc_ndcg_at_20_diff1
      value: -30.61130208138771
    - type: nauc_ndcg_at_20_max
      value: 52.68851710375231
    - type: nauc_ndcg_at_20_std
      value: 69.72357683382992
    - type: nauc_ndcg_at_3_diff1
      value: 5.695394821691213
    - type: nauc_ndcg_at_3_max
      value: 37.909122367102135
    - type: nauc_ndcg_at_3_std
      value: 46.2366603255159
    - type: nauc_ndcg_at_5_diff1
      value: -15.273067832464731
    - type: nauc_ndcg_at_5_max
      value: 49.7054639475091
    - type: nauc_ndcg_at_5_std
      value: 58.83754007826166
    - type: nauc_precision_at_1000_diff1
      value: -31.565302588492035
    - type: nauc_precision_at_1000_max
      value: 52.56214379514724
    - type: nauc_precision_at_1000_std
      value: 53.40618234326055
    - type: nauc_precision_at_100_diff1
      value: -44.67273120709088
    - type: nauc_precision_at_100_max
      value: 48.30381155522576
    - type: nauc_precision_at_100_std
      value: 82.1984661602578
    - type: nauc_precision_at_10_diff1
      value: -24.737383556860145
    - type: nauc_precision_at_10_max
      value: 52.816815002878556
    - type: nauc_precision_at_10_std
      value: 67.99052410030845
    - type: nauc_precision_at_1_diff1
      value: -6.022408963585076
    - type: nauc_precision_at_1_max
      value: 4.481792717087146
    - type: nauc_precision_at_1_std
      value: 51.69623404917518
    - type: nauc_precision_at_20_diff1
      value: -40.23628054967093
    - type: nauc_precision_at_20_max
      value: 56.980056980057014
    - type: nauc_precision_at_20_std
      value: 76.60976777785895
    - type: nauc_precision_at_3_diff1
      value: -4.661784068466279
    - type: nauc_precision_at_3_max
      value: 59.052007899934125
    - type: nauc_precision_at_3_std
      value: 58.187952600394986
    - type: nauc_precision_at_5_diff1
      value: -38.11848143512736
    - type: nauc_precision_at_5_max
      value: 68.6149353358365
    - type: nauc_precision_at_5_std
      value: 73.55652899457661
    - type: nauc_recall_at_1000_diff1
      value: -14.886527444436345
    - type: nauc_recall_at_1000_max
      value: 48.07492302795808
    - type: nauc_recall_at_1000_std
      value: 65.05623212485906
    - type: nauc_recall_at_100_diff1
      value: -8.148385729388195
    - type: nauc_recall_at_100_max
      value: 8.041615364614533
    - type: nauc_recall_at_100_std
      value: 33.77187914574611
    - type: nauc_recall_at_10_diff1
      value: 24.333628413035942
    - type: nauc_recall_at_10_max
      value: -14.577877145192078
    - type: nauc_recall_at_10_std
      value: -12.131819145098557
    - type: nauc_recall_at_1_diff1
      value: 27.342260509653798
    - type: nauc_recall_at_1_max
      value: -23.400451210297994
    - type: nauc_recall_at_1_std
      value: -21.152006353733853
    - type: nauc_recall_at_20_diff1
      value: 13.695556376785564
    - type: nauc_recall_at_20_max
      value: -8.872009346408264
    - type: nauc_recall_at_20_std
      value: -3.163199444247112
    - type: nauc_recall_at_3_diff1
      value: 32.00442538217753
    - type: nauc_recall_at_3_max
      value: -15.159737942664552
    - type: nauc_recall_at_3_std
      value: -17.530833132440645
    - type: nauc_recall_at_5_diff1
      value: 22.64740552912405
    - type: nauc_recall_at_5_max
      value: -12.947090597010414
    - type: nauc_recall_at_5_std
      value: -12.914478822476807
    - type: ndcg_at_1
      value: 88.0
    - type: ndcg_at_10
      value: 84.60600000000001
    - type: ndcg_at_100
      value: 64.31700000000001
    - type: ndcg_at_1000
      value: 56.40500000000001
    - type: ndcg_at_20
      value: 80.561
    - type: ndcg_at_3
      value: 87.87700000000001
    - type: ndcg_at_5
      value: 86.641
    - type: precision_at_1
      value: 94.0
    - type: precision_at_10
      value: 88.2
    - type: precision_at_100
      value: 65.9
    - type: precision_at_1000
      value: 25.019999999999996
    - type: precision_at_20
      value: 84.7
    - type: precision_at_3
      value: 92.0
    - type: precision_at_5
      value: 90.0
    - type: recall_at_1
      value: 0.257
    - type: recall_at_10
      value: 2.338
    - type: recall_at_100
      value: 15.831999999999999
    - type: recall_at_1000
      value: 52.519000000000005
    - type: recall_at_20
      value: 4.367
    - type: recall_at_3
      value: 0.74
    - type: recall_at_5
      value: 1.196
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Touche2020
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
      split: test
      type: mteb/touche2020
    metrics:
    - type: main_score
      value: 31.426
    - type: map_at_1
      value: 3.4709999999999996
    - type: map_at_10
      value: 13.236999999999998
    - type: map_at_100
      value: 19.521
    - type: map_at_1000
      value: 21.224
    - type: map_at_20
      value: 15.626000000000001
    - type: map_at_3
      value: 7.152
    - type: map_at_5
      value: 9.914000000000001
    - type: mrr_at_1
      value: 44.89795918367347
    - type: mrr_at_10
      value: 57.54373177842565
    - type: mrr_at_100
      value: 57.855267710139536
    - type: mrr_at_1000
      value: 57.855267710139536
    - type: mrr_at_20
      value: 57.70071764969724
    - type: mrr_at_3
      value: 52.72108843537414
    - type: mrr_at_5
      value: 55.06802721088435
    - type: nauc_map_at_1000_diff1
      value: 21.148857552115558
    - type: nauc_map_at_1000_max
      value: 2.0837572569021323
    - type: nauc_map_at_1000_std
      value: 3.203419709665347
    - type: nauc_map_at_100_diff1
      value: 21.383778167597878
    - type: nauc_map_at_100_max
      value: 0.965767943155967
    - type: nauc_map_at_100_std
      value: 0.3949924961020957
    - type: nauc_map_at_10_diff1
      value: 27.178555638086394
    - type: nauc_map_at_10_max
      value: 4.480675175857958
    - type: nauc_map_at_10_std
      value: -13.69553539513878
    - type: nauc_map_at_1_diff1
      value: 27.63901823865334
    - type: nauc_map_at_1_max
      value: -18.6387233237763
    - type: nauc_map_at_1_std
      value: -27.02164241863646
    - type: nauc_map_at_20_diff1
      value: 23.892104752374888
    - type: nauc_map_at_20_max
      value: 3.5343136621362348
    - type: nauc_map_at_20_std
      value: -8.765101188860816
    - type: nauc_map_at_3_diff1
      value: 22.065793929837493
    - type: nauc_map_at_3_max
      value: 0.8063396680860568
    - type: nauc_map_at_3_std
      value: -20.404849396621824
    - type: nauc_map_at_5_diff1
      value: 22.66626080580714
    - type: nauc_map_at_5_max
      value: 5.423340658352383
    - type: nauc_map_at_5_std
      value: -18.31523779843455
    - type: nauc_mrr_at_1000_diff1
      value: 30.520722269282665
    - type: nauc_mrr_at_1000_max
      value: -16.644959497742267
    - type: nauc_mrr_at_1000_std
      value: -16.3824126273053
    - type: nauc_mrr_at_100_diff1
      value: 30.520722269282665
    - type: nauc_mrr_at_100_max
      value: -16.644959497742267
    - type: nauc_mrr_at_100_std
      value: -16.3824126273053
    - type: nauc_mrr_at_10_diff1
      value: 30.428248939332974
    - type: nauc_mrr_at_10_max
      value: -16.300183919261585
    - type: nauc_mrr_at_10_std
      value: -15.404823235836309
    - type: nauc_mrr_at_1_diff1
      value: 27.041346572613474
    - type: nauc_mrr_at_1_max
      value: -23.181309312755804
    - type: nauc_mrr_at_1_std
      value: -24.33076726484014
    - type: nauc_mrr_at_20_diff1
      value: 30.676558567379303
    - type: nauc_mrr_at_20_max
      value: -16.914268763031416
    - type: nauc_mrr_at_20_std
      value: -15.77742854976336
    - type: nauc_mrr_at_3_diff1
      value: 31.718457109787096
    - type: nauc_mrr_at_3_max
      value: -15.508391132202235
    - type: nauc_mrr_at_3_std
      value: -20.33229438349494
    - type: nauc_mrr_at_5_diff1
      value: 28.73798376227693
    - type: nauc_mrr_at_5_max
      value: -16.086295031060196
    - type: nauc_mrr_at_5_std
      value: -15.644604635769321
    - type: nauc_ndcg_at_1000_diff1
      value: 22.158724660189606
    - type: nauc_ndcg_at_1000_max
      value: -3.1755686809941475
    - type: nauc_ndcg_at_1000_std
      value: 19.258386224159075
    - type: nauc_ndcg_at_100_diff1
      value: 21.83846748649288
    - type: nauc_ndcg_at_100_max
      value: -10.939957598756036
    - type: nauc_ndcg_at_100_std
      value: 14.729678880436623
    - type: nauc_ndcg_at_10_diff1
      value: 26.944882726098424
    - type: nauc_ndcg_at_10_max
      value: -3.5176483833346617
    - type: nauc_ndcg_at_10_std
      value: -5.400606773697211
    - type: nauc_ndcg_at_1_diff1
      value: 26.649410985172985
    - type: nauc_ndcg_at_1_max
      value: -18.806716526067493
    - type: nauc_ndcg_at_1_std
      value: -25.100244999343506
    - type: nauc_ndcg_at_20_diff1
      value: 24.860266153648315
    - type: nauc_ndcg_at_20_max
      value: -7.521401821712892
    - type: nauc_ndcg_at_20_std
      value: -3.3696577425983003
    - type: nauc_ndcg_at_3_diff1
      value: 23.9933326962406
    - type: nauc_ndcg_at_3_max
      value: -0.4609479344284664
    - type: nauc_ndcg_at_3_std
      value: -15.176459166869897
    - type: nauc_ndcg_at_5_diff1
      value: 22.50595978713142
    - type: nauc_ndcg_at_5_max
      value: -2.1093870656000857
    - type: nauc_ndcg_at_5_std
      value: -12.732197425528257
    - type: nauc_precision_at_1000_diff1
      value: -20.335120385950024
    - type: nauc_precision_at_1000_max
      value: 26.95109729939765
    - type: nauc_precision_at_1000_std
      value: 29.981685890622117
    - type: nauc_precision_at_100_diff1
      value: -2.782114329320704
    - type: nauc_precision_at_100_max
      value: 2.9489322002048604
    - type: nauc_precision_at_100_std
      value: 67.3074073674319
    - type: nauc_precision_at_10_diff1
      value: 21.385177180383383
    - type: nauc_precision_at_10_max
      value: -2.4696365259422817
    - type: nauc_precision_at_10_std
      value: 14.469784299536673
    - type: nauc_precision_at_1_diff1
      value: 27.041346572613474
    - type: nauc_precision_at_1_max
      value: -23.181309312755804
    - type: nauc_precision_at_1_std
      value: -24.33076726484014
    - type: nauc_precision_at_20_diff1
      value: 11.993846579997673
    - type: nauc_precision_at_20_max
      value: -2.4792189693296227
    - type: nauc_precision_at_20_std
      value: 28.581394687807745
    - type: nauc_precision_at_3_diff1
      value: 20.70568446328836
    - type: nauc_precision_at_3_max
      value: 0.37326398699875984
    - type: nauc_precision_at_3_std
      value: -12.983918676694389
    - type: nauc_precision_at_5_diff1
      value: 19.47466335828124
    - type: nauc_precision_at_5_max
      value: -1.8921617684385994
    - type: nauc_precision_at_5_std
      value: -6.533875294402164
    - type: nauc_recall_at_1000_diff1
      value: 7.611201305723156
    - type: nauc_recall_at_1000_max
      value: 5.6416194035820055
    - type: nauc_recall_at_1000_std
      value: 61.695208644278
    - type: nauc_recall_at_100_diff1
      value: 10.0183258158735
    - type: nauc_recall_at_100_max
      value: -10.950612455698973
    - type: nauc_recall_at_100_std
      value: 33.06069987640471
    - type: nauc_recall_at_10_diff1
      value: 24.738210305731535
    - type: nauc_recall_at_10_max
      value: -2.6592454032071546
    - type: nauc_recall_at_10_std
      value: -4.83987517793115
    - type: nauc_recall_at_1_diff1
      value: 27.63901823865334
    - type: nauc_recall_at_1_max
      value: -18.6387233237763
    - type: nauc_recall_at_1_std
      value: -27.02164241863646
    - type: nauc_recall_at_20_diff1
      value: 17.79601177409034
    - type: nauc_recall_at_20_max
      value: -6.681637093148051
    - type: nauc_recall_at_20_std
      value: 3.369193919932238
    - type: nauc_recall_at_3_diff1
      value: 24.9589431081204
    - type: nauc_recall_at_3_max
      value: 2.4783640980500232
    - type: nauc_recall_at_3_std
      value: -19.567415651090702
    - type: nauc_recall_at_5_diff1
      value: 23.71803410135437
    - type: nauc_recall_at_5_max
      value: 1.6294309357641652
    - type: nauc_recall_at_5_std
      value: -15.365511906408983
    - type: ndcg_at_1
      value: 40.816
    - type: ndcg_at_10
      value: 31.426
    - type: ndcg_at_100
      value: 41.558
    - type: ndcg_at_1000
      value: 53.042
    - type: ndcg_at_20
      value: 31.108999999999998
    - type: ndcg_at_3
      value: 35.518
    - type: ndcg_at_5
      value: 33.235
    - type: precision_at_1
      value: 44.897999999999996
    - type: precision_at_10
      value: 27.551
    - type: precision_at_100
      value: 8.204
    - type: precision_at_1000
      value: 1.582
    - type: precision_at_20
      value: 19.796
    - type: precision_at_3
      value: 36.735
    - type: precision_at_5
      value: 33.061
    - type: recall_at_1
      value: 3.4709999999999996
    - type: recall_at_10
      value: 19.563
    - type: recall_at_100
      value: 50.3
    - type: recall_at_1000
      value: 85.13199999999999
    - type: recall_at_20
      value: 26.738
    - type: recall_at_3
      value: 7.8420000000000005
    - type: recall_at_5
      value: 11.994
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 68.29850746268657
    - type: ap
      value: 30.109785890841966
    - type: ap_weighted
      value: 30.109785890841966
    - type: f1
      value: 61.76875915202924
    - type: f1_weighted
      value: 71.32073190458556
    - type: main_score
      value: 68.29850746268657
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AmazonPolarityClassification (default)
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
      split: test
      type: mteb/amazon_polarity
    metrics:
    - type: accuracy
      value: 90.3068
    - type: ap
      value: 86.17914339624038
    - type: ap_weighted
      value: 86.17914339624038
    - type: f1
      value: 90.29716826358077
    - type: f1_weighted
      value: 90.29716826358077
    - type: main_score
      value: 90.3068
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonReviewsClassification (en)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 46.272000000000006
    - type: f1
      value: 45.57042543386915
    - type: f1_weighted
      value: 45.57042543386915
    - type: main_score
      value: 46.272000000000006
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P (default)
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 44.9469238081379
    - type: v_measure
      value: 44.9469238081379
    - type: v_measure_std
      value: 13.26811262671461
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringS2S (default)
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
      split: test
      type: mteb/arxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 34.12071448053325
    - type: v_measure
      value: 34.12071448053325
    - type: v_measure_std
      value: 13.7019879046405
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AskUbuntuDupQuestions (default)
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
      split: test
      type: mteb/askubuntudupquestions-reranking
    metrics:
    - type: main_score
      value: 61.597667288657846
    - type: map
      value: 61.597667288657846
    - type: mrr
      value: 75.57940904893813
    - type: nAUC_map_diff1
      value: 8.745172077340095
    - type: nAUC_map_max
      value: 20.114863024035493
    - type: nAUC_map_std
      value: 15.991351189572192
    - type: nAUC_mrr_diff1
      value: 20.781369244159983
    - type: nAUC_mrr_max
      value: 30.78542570228559
    - type: nAUC_mrr_std
      value: 19.861484857303676
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB BIOSSES (default)
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: cosine_pearson
      value: 88.55587996301419
    - type: cosine_spearman
      value: 86.40317357420093
    - type: euclidean_pearson
      value: 86.93771958250231
    - type: euclidean_spearman
      value: 86.40317357420093
    - type: main_score
      value: 86.40317357420093
    - type: manhattan_pearson
      value: 86.92196577117366
    - type: manhattan_spearman
      value: 85.79834051556095
    - type: pearson
      value: 88.55587996301419
    - type: spearman
      value: 86.40317357420093
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB Banking77Classification (default)
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
      split: test
      type: mteb/banking77
    metrics:
    - type: accuracy
      value: 80.0064935064935
    - type: f1
      value: 79.29524254086299
    - type: f1_weighted
      value: 79.295242540863
    - type: main_score
      value: 80.0064935064935
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P (default)
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 35.27186813341181
    - type: v_measure
      value: 35.27186813341181
    - type: v_measure_std
      value: 0.8621482145872432
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringS2S (default)
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
      split: test
      type: mteb/biorxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 28.411805064852295
    - type: v_measure
      value: 28.411805064852295
    - type: v_measure_std
      value: 0.7194290078011281
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB EmotionClassification (default)
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: test
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 43.675
    - type: f1
      value: 40.15061931375577
    - type: f1_weighted
      value: 45.714186572727066
    - type: main_score
      value: 43.675
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ImdbClassification (default)
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
      split: test
      type: mteb/imdb
    metrics:
    - type: accuracy
      value: 84.35640000000001
    - type: ap
      value: 79.07507736685174
    - type: ap_weighted
      value: 79.07507736685174
    - type: f1
      value: 84.32288494833531
    - type: f1_weighted
      value: 84.32288494833531
    - type: main_score
      value: 84.35640000000001
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPDomainClassification (en)
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: test
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 91.35658914728684
    - type: f1
      value: 90.86877537911086
    - type: f1_weighted
      value: 91.3282092774443
    - type: main_score
      value: 91.35658914728684
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPIntentClassification (en)
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: test
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 60.63611491108071
    - type: f1
      value: 42.78886482112741
    - type: f1_weighted
      value: 63.44208631840539
    - type: main_score
      value: 60.63611491108071
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveIntentClassification (en)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 66.68796234028245
    - type: f1
      value: 64.44940791000278
    - type: f1_weighted
      value: 65.77554417406792
    - type: main_score
      value: 66.68796234028245
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveScenarioClassification (en)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 73.0598520511096
    - type: f1
      value: 72.14267273884774
    - type: f1_weighted
      value: 72.93345180137516
    - type: main_score
      value: 73.0598520511096
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MedrxivClusteringP2P (default)
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
      split: test
      type: mteb/medrxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 31.143081341699606
    - type: v_measure
      value: 31.143081341699606
    - type: v_measure_std
      value: 1.5578716347076906
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MedrxivClusteringS2S (default)
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
      split: test
      type: mteb/medrxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 27.010818869829556
    - type: v_measure
      value: 27.010818869829556
    - type: v_measure_std
      value: 1.1771554540819378
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MindSmallReranking (default)
      revision: 59042f120c80e8afa9cdbb224f67076cec0fc9a7
      split: test
      type: mteb/mind_small
    metrics:
    - type: main_score
      value: 30.20503776754942
    - type: map
      value: 30.20503776754942
    - type: mrr
      value: 31.076636002733437
    - type: nAUC_map_diff1
      value: 7.290568655287842
    - type: nAUC_map_max
      value: -21.381599355932945
    - type: nAUC_map_std
      value: -7.709920607543168
    - type: nAUC_mrr_diff1
      value: 7.558397329284913
    - type: nAUC_mrr_max
      value: -15.981397186427607
    - type: nAUC_mrr_std
      value: -4.870495243168834
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB RedditClustering (default)
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
      split: test
      type: mteb/reddit-clustering
    metrics:
    - type: main_score
      value: 51.85893476633338
    - type: v_measure
      value: 51.85893476633338
    - type: v_measure_std
      value: 4.704770139385852
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RedditClusteringP2P (default)
      revision: 385e3cb46b4cfa89021f56c4380204149d0efe33
      split: test
      type: mteb/reddit-clustering-p2p
    metrics:
    - type: main_score
      value: 61.8124222918822
    - type: v_measure
      value: 61.8124222918822
    - type: v_measure_std
      value: 11.994472578100165
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB SICK-R (default)
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
      split: test
      type: mteb/sickr-sts
    metrics:
    - type: cosine_pearson
      value: 77.63310776935984
    - type: cosine_spearman
      value: 69.86468291111039
    - type: euclidean_pearson
      value: 73.91537077798837
    - type: euclidean_spearman
      value: 69.86468376650203
    - type: main_score
      value: 69.86468291111039
    - type: manhattan_pearson
      value: 73.68616048370464
    - type: manhattan_spearman
      value: 69.76232036206659
    - type: pearson
      value: 77.63310776935984
    - type: spearman
      value: 69.86468291111039
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS12 (default)
      revision: a0d554a64d88156834ff5ae9920b964011b16384
      split: test
      type: mteb/sts12-sts
    metrics:
    - type: cosine_pearson
      value: 57.71716838245049
    - type: cosine_spearman
      value: 61.797855543446424
    - type: euclidean_pearson
      value: 58.22958675325848
    - type: euclidean_spearman
      value: 61.797855543446424
    - type: main_score
      value: 61.797855543446424
    - type: manhattan_pearson
      value: 57.63117544997929
    - type: manhattan_spearman
      value: 61.3629404350085
    - type: pearson
      value: 57.71716838245049
    - type: spearman
      value: 61.797855543446424
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS13 (default)
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
      split: test
      type: mteb/sts13-sts
    metrics:
    - type: cosine_pearson
      value: 82.30260026790903
    - type: cosine_spearman
      value: 82.66959813070869
    - type: euclidean_pearson
      value: 82.08383017580783
    - type: euclidean_spearman
      value: 82.66959813070869
    - type: main_score
      value: 82.66959813070869
    - type: manhattan_pearson
      value: 81.77991451392153
    - type: manhattan_spearman
      value: 82.3652534745606
    - type: pearson
      value: 82.30260026790903
    - type: spearman
      value: 82.66959813070869
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS14 (default)
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
      split: test
      type: mteb/sts14-sts
    metrics:
    - type: cosine_pearson
      value: 71.50608384084478
    - type: cosine_spearman
      value: 68.94968064977785
    - type: euclidean_pearson
      value: 70.73381299949564
    - type: euclidean_spearman
      value: 68.94968064977785
    - type: main_score
      value: 68.94968064977785
    - type: manhattan_pearson
      value: 70.5385486953787
    - type: manhattan_spearman
      value: 68.82132770672365
    - type: pearson
      value: 71.50608384084478
    - type: spearman
      value: 68.94968064977785
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS15 (default)
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
      split: test
      type: mteb/sts15-sts
    metrics:
    - type: cosine_pearson
      value: 73.66969825874907
    - type: cosine_spearman
      value: 75.55374982088381
    - type: euclidean_pearson
      value: 75.9339313749594
    - type: euclidean_spearman
      value: 75.55374982088381
    - type: main_score
      value: 75.55374982088381
    - type: manhattan_pearson
      value: 75.88287553383817
    - type: manhattan_spearman
      value: 75.50729812977688
    - type: pearson
      value: 73.66969825874907
    - type: spearman
      value: 75.55374982088381
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS16 (default)
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
      split: test
      type: mteb/sts16-sts
    metrics:
    - type: cosine_pearson
      value: 74.5954724414016
    - type: cosine_spearman
      value: 77.2688820850505
    - type: euclidean_pearson
      value: 77.19866353971555
    - type: euclidean_spearman
      value: 77.2688820850505
    - type: main_score
      value: 77.2688820850505
    - type: manhattan_pearson
      value: 77.27072603680978
    - type: manhattan_spearman
      value: 77.29408453673607
    - type: pearson
      value: 74.5954724414016
    - type: spearman
      value: 77.2688820850505
    task:
      type: STS
  - dataset:
      config: en-en
      name: MTEB STS17 (en-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 71.52588722654055
    - type: cosine_spearman
      value: 74.97235736456061
    - type: euclidean_pearson
      value: 74.51952528854038
    - type: euclidean_spearman
      value: 74.97235736456061
    - type: main_score
      value: 74.97235736456061
    - type: manhattan_pearson
      value: 74.48272300884209
    - type: manhattan_spearman
      value: 74.80633649415176
    - type: pearson
      value: 71.52588722654055
    - type: spearman
      value: 74.97235736456061
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STS22 (en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 68.80031120401976
    - type: cosine_spearman
      value: 69.07945196478491
    - type: euclidean_pearson
      value: 68.99674496430792
    - type: euclidean_spearman
      value: 69.07945196478491
    - type: main_score
      value: 69.07945196478491
    - type: manhattan_pearson
      value: 69.00236107775687
    - type: manhattan_spearman
      value: 68.98064879049272
    - type: pearson
      value: 68.80031120401976
    - type: spearman
      value: 69.07945196478491
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSBenchmark (default)
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
      split: test
      type: mteb/stsbenchmark-sts
    metrics:
    - type: cosine_pearson
      value: 65.6898007230089
    - type: cosine_spearman
      value: 69.72386211803668
    - type: euclidean_pearson
      value: 69.04523003701475
    - type: euclidean_spearman
      value: 69.72386211803668
    - type: main_score
      value: 69.72386211803668
    - type: manhattan_pearson
      value: 68.80479743770702
    - type: manhattan_spearman
      value: 69.43264575177459
    - type: pearson
      value: 65.6898007230089
    - type: spearman
      value: 69.72386211803668
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SciDocsRR (default)
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
      split: test
      type: mteb/scidocs-reranking
    metrics:
    - type: main_score
      value: 79.74088066874383
    - type: map
      value: 79.74088066874383
    - type: mrr
      value: 94.47697455050397
    - type: nAUC_map_diff1
      value: 8.036086256905502
    - type: nAUC_map_max
      value: 54.88199803816819
    - type: nAUC_map_std
      value: 69.16267942176574
    - type: nAUC_mrr_diff1
      value: 50.020738477678115
    - type: nAUC_mrr_max
      value: 83.28922770326483
    - type: nAUC_mrr_std
      value: 83.63973501802224
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SprintDuplicateQuestions (default)
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
      split: test
      type: mteb/sprintduplicatequestions-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 99.83861386138614
    - type: cosine_accuracy_threshold
      value: 74.75666999816895
    - type: cosine_ap
      value: 96.15132792066652
    - type: cosine_f1
      value: 91.84890656063618
    - type: cosine_f1_threshold
      value: 71.70594930648804
    - type: cosine_precision
      value: 91.30434782608695
    - type: cosine_recall
      value: 92.4
    - type: dot_accuracy
      value: 99.83861386138614
    - type: dot_accuracy_threshold
      value: 74.75666999816895
    - type: dot_ap
      value: 96.15132792066653
    - type: dot_f1
      value: 91.84890656063618
    - type: dot_f1_threshold
      value: 71.70596122741699
    - type: dot_precision
      value: 91.30434782608695
    - type: dot_recall
      value: 92.4
    - type: euclidean_accuracy
      value: 99.83861386138614
    - type: euclidean_accuracy_threshold
      value: 71.05395793914795
    - type: euclidean_ap
      value: 96.15132792066652
    - type: euclidean_f1
      value: 91.84890656063618
    - type: euclidean_f1_threshold
      value: 75.22505521774292
    - type: euclidean_precision
      value: 91.30434782608695
    - type: euclidean_recall
      value: 92.4
    - type: main_score
      value: 96.15132792066653
    - type: manhattan_accuracy
      value: 99.83564356435643
    - type: manhattan_accuracy_threshold
      value: 1547.6950645446777
    - type: manhattan_ap
      value: 96.06151211452136
    - type: manhattan_f1
      value: 91.61676646706587
    - type: manhattan_f1_threshold
      value: 1626.3608932495117
    - type: manhattan_precision
      value: 91.43426294820716
    - type: manhattan_recall
      value: 91.8
    - type: max_ap
      value: 96.15132792066653
    - type: max_f1
      value: 91.84890656063618
    - type: max_precision
      value: 91.43426294820716
    - type: max_recall
      value: 92.4
    - type: similarity_accuracy
      value: 99.83861386138614
    - type: similarity_accuracy_threshold
      value: 74.75666999816895
    - type: similarity_ap
      value: 96.15132792066652
    - type: similarity_f1
      value: 91.84890656063618
    - type: similarity_f1_threshold
      value: 71.70594930648804
    - type: similarity_precision
      value: 91.30434782608695
    - type: similarity_recall
      value: 92.4
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB StackExchangeClustering (default)
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
      split: test
      type: mteb/stackexchange-clustering
    metrics:
    - type: main_score
      value: 61.24120328328453
    - type: v_measure
      value: 61.24120328328453
    - type: v_measure_std
      value: 3.9946560691100372
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackExchangeClusteringP2P (default)
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
      split: test
      type: mteb/stackexchange-clustering-p2p
    metrics:
    - type: main_score
      value: 33.808268374864745
    - type: v_measure
      value: 33.808268374864745
    - type: v_measure_std
      value: 1.2212188701887239
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackOverflowDupQuestions (default)
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
      split: test
      type: mteb/stackoverflowdupquestions-reranking
    metrics:
    - type: main_score
      value: 52.19806018468037
    - type: map
      value: 52.19806018468037
    - type: mrr
      value: 52.98921462524404
    - type: nAUC_map_diff1
      value: 37.41443156995912
    - type: nAUC_map_max
      value: 9.410262727675603
    - type: nAUC_map_std
      value: 8.7094185014992
    - type: nAUC_mrr_diff1
      value: 37.78202772392581
    - type: nAUC_mrr_max
      value: 10.517635536565816
    - type: nAUC_mrr_std
      value: 8.509423813772491
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SummEval (default)
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
      split: test
      type: mteb/summeval
    metrics:
    - type: cosine_pearson
      value: 30.48413700430812
    - type: cosine_spearman
      value: 30.357162200875816
    - type: dot_pearson
      value: 30.484140144824938
    - type: dot_spearman
      value: 30.357162200875816
    - type: main_score
      value: 30.357162200875816
    - type: pearson
      value: 30.48413700430812
    - type: spearman
      value: 30.357162200875816
    task:
      type: Summarization
  - dataset:
      config: default
      name: MTEB ToxicConversationsClassification (default)
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
      split: test
      type: mteb/toxic_conversations_50k
    metrics:
    - type: accuracy
      value: 66.8359375
    - type: ap
      value: 12.482653786025985
    - type: ap_weighted
      value: 12.482653786025985
    - type: f1
      value: 51.328608527332385
    - type: f1_weighted
      value: 74.07974463955398
    - type: main_score
      value: 66.8359375
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TweetSentimentExtractionClassification (default)
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
      split: test
      type: mteb/tweet_sentiment_extraction
    metrics:
    - type: accuracy
      value: 53.907753254103
    - type: f1
      value: 54.22707647269581
    - type: f1_weighted
      value: 53.611822984407695
    - type: main_score
      value: 53.907753254103
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TwentyNewsgroupsClustering (default)
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
      split: test
      type: mteb/twentynewsgroups-clustering
    metrics:
    - type: main_score
      value: 38.1364789307295
    - type: v_measure
      value: 38.1364789307295
    - type: v_measure_std
      value: 2.0731634966352077
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB TwitterSemEval2015 (default)
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
      split: test
      type: mteb/twittersemeval2015-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 82.66674614054956
    - type: cosine_accuracy_threshold
      value: 79.80123162269592
    - type: cosine_ap
      value: 63.28209719072804
    - type: cosine_f1
      value: 60.16389710903711
    - type: cosine_f1_threshold
      value: 72.22893834114075
    - type: cosine_precision
      value: 52.90232185748599
    - type: cosine_recall
      value: 69.73614775725594
    - type: dot_accuracy
      value: 82.66674614054956
    - type: dot_accuracy_threshold
      value: 79.8012375831604
    - type: dot_ap
      value: 63.282103870645166
    - type: dot_f1
      value: 60.16389710903711
    - type: dot_f1_threshold
      value: 72.22894430160522
    - type: dot_precision
      value: 52.90232185748599
    - type: dot_recall
      value: 69.73614775725594
    - type: euclidean_accuracy
      value: 82.66674614054956
    - type: euclidean_accuracy_threshold
      value: 63.55905532836914
    - type: euclidean_ap
      value: 63.282095399953164
    - type: euclidean_f1
      value: 60.16389710903711
    - type: euclidean_f1_threshold
      value: 74.5265781879425
    - type: euclidean_precision
      value: 52.90232185748599
    - type: euclidean_recall
      value: 69.73614775725594
    - type: main_score
      value: 63.282103870645166
    - type: manhattan_accuracy
      value: 82.74423317637242
    - type: manhattan_accuracy_threshold
      value: 1415.380859375
    - type: manhattan_ap
      value: 63.26931757839598
    - type: manhattan_f1
      value: 60.11014948859166
    - type: manhattan_f1_threshold
      value: 1632.522201538086
    - type: manhattan_precision
      value: 52.359506559624045
    - type: manhattan_recall
      value: 70.55408970976254
    - type: max_ap
      value: 63.282103870645166
    - type: max_f1
      value: 60.16389710903711
    - type: max_precision
      value: 52.90232185748599
    - type: max_recall
      value: 70.55408970976254
    - type: similarity_accuracy
      value: 82.66674614054956
    - type: similarity_accuracy_threshold
      value: 79.80123162269592
    - type: similarity_ap
      value: 63.28209719072804
    - type: similarity_f1
      value: 60.16389710903711
    - type: similarity_f1_threshold
      value: 72.22893834114075
    - type: similarity_precision
      value: 52.90232185748599
    - type: similarity_recall
      value: 69.73614775725594
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB TwitterURLCorpus (default)
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
      split: test
      type: mteb/twitterurlcorpus-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 88.10105949470253
    - type: cosine_accuracy_threshold
      value: 68.95147562026978
    - type: cosine_ap
      value: 84.65516103854583
    - type: cosine_f1
      value: 76.54581123301605
    - type: cosine_f1_threshold
      value: 63.92929553985596
    - type: cosine_precision
      value: 72.46526344751685
    - type: cosine_recall
      value: 81.11333538651063
    - type: dot_accuracy
      value: 88.10105949470253
    - type: dot_accuracy_threshold
      value: 68.95147562026978
    - type: dot_ap
      value: 84.65516301437592
    - type: dot_f1
      value: 76.54581123301605
    - type: dot_f1_threshold
      value: 63.92928957939148
    - type: dot_precision
      value: 72.46526344751685
    - type: dot_recall
      value: 81.11333538651063
    - type: euclidean_accuracy
      value: 88.10105949470253
    - type: euclidean_accuracy_threshold
      value: 78.80169153213501
    - type: euclidean_ap
      value: 84.65517268264233
    - type: euclidean_f1
      value: 76.54581123301605
    - type: euclidean_f1_threshold
      value: 84.93610620498657
    - type: euclidean_precision
      value: 72.46526344751685
    - type: euclidean_recall
      value: 81.11333538651063
    - type: main_score
      value: 84.65517268264233
    - type: manhattan_accuracy
      value: 88.08941669577366
    - type: manhattan_accuracy_threshold
      value: 1739.3169403076172
    - type: manhattan_ap
      value: 84.64592398855694
    - type: manhattan_f1
      value: 76.62890540443034
    - type: manhattan_f1_threshold
      value: 1861.344337463379
    - type: manhattan_precision
      value: 72.09775967413442
    - type: manhattan_recall
      value: 81.76778564829073
    - type: max_ap
      value: 84.65517268264233
    - type: max_f1
      value: 76.62890540443034
    - type: max_precision
      value: 72.46526344751685
    - type: max_recall
      value: 81.76778564829073
    - type: similarity_accuracy
      value: 88.10105949470253
    - type: similarity_accuracy_threshold
      value: 68.95147562026978
    - type: similarity_ap
      value: 84.65516103854583
    - type: similarity_f1
      value: 76.54581123301605
    - type: similarity_f1_threshold
      value: 63.92929553985596
    - type: similarity_precision
      value: 72.46526344751685
    - type: similarity_recall
      value: 81.11333538651063
    task:
      type: PairClassification
---


<h1 align="center">Snowflake's Arctic-embed-m-v1.5</h1>
<h4 align="center">
   <p>
       <a href=#news>News</a> |
       <a href=#this-model>This Model</a>  |
       <a href=#usage>Usage</a>  |
       <a href="#faq">FAQ</a> |
       <a href="#contact">Contact</a> |
       <a href="#license">License</a> |
       <a href="#acknowledgement">Acknowledgement</a>
   <p>
</h4>


## News

07/26/2024: Release preprint [[2407.18887] Embedding And Clustering Your Data Can Improve Contrastive Pretraining](https://arxiv.org/abs/2407.18887) on arXiv.

07/18/2024: Release of `snowflake-arctic-embed-m-v1.5`, capable of producing highly compressible embedding vectors that preserve quality even when squished as small as 128 bytes per vector. Details about the development of this model are available in the [launch post on the Snowflake engineering blog](https://www.snowflake.com/engineering-blog/arctic-embed-m-v1-5-enterprise-retrieval/).

05/10/2024: Release of the [technical report on Arctic Embed](https://arxiv.org/abs/2405.05374)

04/16/2024: Original release the `snowflake-arctic-embed` family of text embedding models.


## This Model

This model is an updated version of [snowflake-arctic-embed-m](https://huggingface.co/Snowflake/snowflake-arctic-embed-m/) designed to improve embedding vector compressibility. This model achieves a slightly higher performance overall without compression, and it is additionally capable of retaining most of its retrieval quality even down to 128 byte embedding vectors through a combination of [Matryoshka Representation Learning (MRL)](https://arxiv.org/abs/2205.13147) and uniform scalar quanitization.

| Model Name                                                                                      | MTEB Retrieval Score (NDCG @ 10) |
|:------------------------------------------------------------------------------------------------|:---------------------------------|
| [snowflake-arctic-embed-m-v1.5](https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v1.5) | 55.14                            |
| [snowflake-arctic-embed-m](https://huggingface.co/Snowflake/snowflake-arctic-embed-m/)          | 54.91                            |

Compared to several other models trained with MRL to produce 256-dimensional embedding vectors, `snowflake-arctic-embed-m-v1.5` retains a higher degree of original model quality and delivers better retrieval quality on the MTEB Retrieval benchmark.

| Model                         | Model Parameters   | MTEB Retrieval Score at 256 Dimensions (fraction of arctic-embed-m-v1.5)   |
|:------------------------------|:-------------------|:---------------------------------------------------------------------------|
| Snowflake arctic-embed-m-v1.5 | 109M               | 54.2 (100%)                                                                |
| Google gecko                  | 1200M              | 52.4 (97%)                                                                 |
| OpenAI text-embedding-3-large | Not Published      | 51.7 (95%)                                                                 |
| Nomic nomic-embed-text-v1.5   | 138M               | 50.8 (94%)                                                                 |


Additionally, this model was designed to pair well with a corpus-independent scalar quantization scheme to achieve great performance even in as little as 128 bytes per vector (24x compression compared to 768 dimensional vectors stored in float32).

| Model Version   |   Dimensionality | Scalar Quantization   | Bytes Per Vector (fraction of baseline)   | MTEB Retrieval Score (fraction of baseline)   | Vectors Per GB (improvement over baseline)   |
|:----------------|-----------------:|:----------------------|:------------------------------------------|:----------------------------------------------|:---------------------------------------------|
| v1              |              768 | None (float32)        | 3072 (100%)                               | 54.9 (100%)                                   | 0.33M (1.0x)                                 |
| v1              |              768 | int8                  | 768 (25%)                                 | 54.9 (100%)                                   | 1.3M (4x)                                    |
| v1.5            |              768 | int8                  | 768 (25%)                                 | 55.1 (100%)                                   | 1.3M (4x)                                    |
| v1.5            |              256 | int8                  | 256 (8.3%)                                | 54.2 (99%)                                    | 3.9M (12x)                                   |
| v1.5            |              256 | int4                  | 128 (4.2%)                                | 53.7 (98%)                                    | 7.8M (24x)                                   |

NOTE: Good uniform scalar quantization ranges to use with this model (and which were used in the eval above), are -0.18 to +0.18 for 4bit and -0.3 to +0.3 for 8bit. For a detailed walkthrough of using integer quantization with `snowflake-arctic-embed-m-v1.5`, check out our [example notebook on GitHub](https://github.com/Snowflake-Labs/arctic-embed/tree/main/compressed_embeddings_examples/score_arctic_embed_m_v1dot5_with_quantization.ipynb).

## Usage

### Using Sentence Transformers

You can use the sentence-transformers package to use any of the snowflake-arctic-embed models. Here's an example for `snowflake-arctic-embed-m-v1.5`.

```python
import torch
from sentence_transformers import SentenceTransformer
from torch.nn.functional import normalize

# Model constant.
MODEL_ID = "Snowflake/snowflake-arctic-embed-m-v1.5"

# Your queries and docs.
queries = ['what is snowflake?', 'Where can I get the best tacos?']
documents = ['The Data Cloud!', 'Mexico City of Course!']

# Load the model.
model = SentenceTransformer(MODEL_ID)

# Generate text embeddings.
query_embeddings = model.encode(queries, prompt_name="query")
document_embeddings = model.encode(documents)

# Scores via dotproduct.
scores = query_embeddings @ document_embeddings.T

# Pretty-print the results.
for query, query_scores in zip(queries, scores):
    doc_score_pairs = list(zip(documents, query_scores))
    doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)
    print(f'Query: "{query}"')
    for document, score in doc_score_pairs:
        print(f'Score: {score:.4f} | Document: "{document}"')
    print()

#### OUTPUT ####
# Query: "what is snowflake?"
# Score: 0.3521 | Document: "The Data Cloud!"
# Score: 0.2358 | Document: "Mexico City of Course!"

# Query: "Where can I get the best tacos?"
# Score: 0.3884 | Document: "Mexico City of Course!"
# Score: 0.2389 | Document: "The Data Cloud!"
#

#### Variation: Truncated Embeddings ####
query_embeddings_256 = normalize(torch.from_numpy(query_embeddings)[:, :256])
document_embeddings_256 = normalize(torch.from_numpy(document_embeddings)[:, :256])
scores_256 = query_embeddings_256 @ document_embeddings_256.T

# Pretty-print the results.
for query, query_scores in zip(queries, scores_256):
    doc_score_pairs = sorted(zip(documents, query_scores), key=lambda x: x[1], reverse=True)
    print(f'Query: "{query}"')
    for document, score in doc_score_pairs:
        print(f'Score: {score:.4f} | Document: "{document}"')
    print()

#### OUTPUT ####
# Query: "what is snowflake?"
# Score: 0.3852 | Document: "The Data Cloud!"
# Score: 0.2721 | Document: "Mexico City of Course!"

# Query: "Where can I get the best tacos?"
# Score: 0.4337 | Document: "Mexico City of Course!"
# Score: 0.2886 | Document: "The Data Cloud!"
#
```

### Using Huggingface transformers

You can use the transformers package to use an snowflake-arctic-embed model, too. For optimal retrieval quality, remember to use the CLS token for embeddings and to use the query prefix below (just on the query).


```python
import torch
from torch.nn.functional import normalize
from transformers import AutoModel, AutoTokenizer

# Model constants.
MODEL_ID = "Snowflake/snowflake-arctic-embed-m-v1.5"
QUERY_PREFIX = 'Represent this sentence for searching relevant passages: '

# Your queries and docs.
queries  = ['what is snowflake?', 'Where can I get the best tacos?']
documents = ['The Data Cloud!', 'Mexico City of Course!']

# Load the model and tokenizer.
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModel.from_pretrained(MODEL_ID, add_pooling_layer=False)
model.eval()

# Add query prefix and tokenize queries and docs.
queries_with_prefix = [f"{QUERY_PREFIX}{q}" for q in queries]
query_tokens = tokenizer(queries_with_prefix, padding=True, truncation=True, return_tensors='pt', max_length=512)
document_tokens =  tokenizer(documents, padding=True, truncation=True, return_tensors='pt', max_length=512)

# Use the model to generate text embeddings.
with torch.inference_mode():
    query_embeddings = model(**query_tokens)[0][:, 0]
    document_embeddings = model(**document_tokens)[0][:, 0]

# Remember to normalize embeddings.
query_embeddings = normalize(query_embeddings)
document_embeddings = normalize(document_embeddings)

# Scores via dotproduct.
scores = query_embeddings @ document_embeddings.T

# Pretty-print the results.
for query, query_scores in zip(queries, scores):
    doc_score_pairs = list(zip(documents, query_scores))
    doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)
    print(f'Query: "{query}"')
    for document, score in doc_score_pairs:
        print(f'Score: {score:.4f} | Document: "{document}"')
    print()

#### OUTPUT ####
# Query: "what is snowflake?"
# Score: 0.3521 | Document: "The Data Cloud!"
# Score: 0.2358 | Document: "Mexico City of Course!"

# Query: "Where can I get the best tacos?"
# Score: 0.3884 | Document: "Mexico City of Course!"
# Score: 0.2389 | Document: "The Data Cloud!"
#

#### Variation: Truncated Embeddings ####
query_embeddings_256 = normalize(query_embeddings[:, :256])
document_embeddings_256 = normalize(document_embeddings[:, :256])
scores_256 = query_embeddings_256 @ document_embeddings_256.T

# Pretty-print the results.
for query, query_scores in zip(queries, scores_256):
    doc_score_pairs = sorted(zip(documents, query_scores), key=lambda x: x[1], reverse=True)
    print(f'Query: "{query}"')
    for document, score in doc_score_pairs:
        print(f'Score: {score:.4f} | Document: "{document}"')
    print()

#### OUTPUT ####
# Query: "what is snowflake?"
# Score: 0.3852 | Document: "The Data Cloud!"
# Score: 0.2721 | Document: "Mexico City of Course!"

# Query: "Where can I get the best tacos?"
# Score: 0.4337 | Document: "Mexico City of Course!"
# Score: 0.2886 | Document: "The Data Cloud!"
#
```

### Using Transformers.js

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@xenova/transformers) by running:
```bash
npm i @xenova/transformers
```

You can then use the model to compute embeddings as follows:

```js
import { pipeline, dot } from '@xenova/transformers';

// Create feature extraction pipeline
const extractor = await pipeline('feature-extraction', 'Snowflake/snowflake-arctic-embed-m-v1.5', {
    quantized: false, // Comment out this line to use the quantized version
});

// Generate sentence embeddings
const sentences = [
    'Represent this sentence for searching relevant passages: Where can I get the best tacos?',
    'The Data Cloud!',
    'Mexico City of Course!',
]
const output = await extractor(sentences, { normalize: true, pooling: 'cls' });

// Compute similarity scores
const [source_embeddings, ...document_embeddings ] = output.tolist();
const similarities = document_embeddings.map(x => dot(source_embeddings, x));
console.log(similarities); // [0.15664823859882132, 0.24481869975470627]
```

### Compressing to 128 bytes

This model is designed to generate embeddings which compress well down to 128 bytes via a two-part compression scheme:
1. Truncation and renormalization to 256 dimensions (a la Matryoskha Representation Learning, see [the original paper for reference](https://arxiv.org/abs/2205.13147)).
2. 4-bit uniform scalar quantization of all 256 values to the same range (-0.18 to +0.18).
   - For 8-bit uniform scalar quantization, the slightly wider range -0.3 to +0.3 tends to work slightly better given how much more granular 8-bit quantization is.

For an in-depth examples, check out our [arctic-embed GitHub repositiory](https://github.com/Snowflake-Labs/arctic-embed).

## FAQ


TBD


## Contact


Feel free to open an issue or pull request if you have any questions or suggestions about this project.
You also can email Daniel Campos(daniel.campos@snowflake.com).


## License


Arctic is licensed under the [Apache-2](https://www.apache.org/licenses/LICENSE-2.0). The released models can be used for commercial purposes free of charge.


## Acknowledgement


We want to thank the open-source community, which has provided the great building blocks upon which we could make our models.
We thank our modeling engineers, Danmei Xu, Luke Merrick, Gaurav Nuti, and Daniel Campos, for making these great models possible.
We thank our leadership, Himabindu Pucha, Kelvin So, Vivek Raghunathan, and Sridhar Ramaswamy, for supporting this work.
We also thank the open-source community for producing the great models we could build on top of and making these releases possible.
Finally, we thank the researchers who created BEIR and MTEB benchmarks.
It is largely thanks to their tireless work to define what better looks like that we could improve model performance.
