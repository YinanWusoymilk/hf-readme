---
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- sentence-embedding
- mteb
model-index:
- name: bilingual-embedding-large
  results:
  - task:
      type: Clustering
    dataset:
      type: lyon-nlp/alloprof
      name: MTEB AlloProfClusteringP2P
      config: default
      split: test
      revision: 392ba3f5bcc8c51f578786c1fc3dae648662cb9b
    metrics:
    - type: v_measure
      value: 65.3004467686438
    - type: v_measures
      value: [0.632560011824588, 0.6345771823814063, 0.6333686484625257, 0.6508206816667124, 0.6378451181543632]
  - task:
      type: Clustering
    dataset:
      type: lyon-nlp/alloprof
      name: MTEB AlloProfClusteringS2S
      config: default
      split: test
      revision: 392ba3f5bcc8c51f578786c1fc3dae648662cb9b
    metrics:
    - type: v_measure
      value: 55.3684183324479
    - type: v_measures
      value: [0.5262468095085737, 0.586151012721014, 0.5192907959178751, 0.5610730679809162, 0.6360060059791816]
  - task:
      type: Reranking
    dataset:
      type: lyon-nlp/mteb-fr-reranking-alloprof-s2p
      name: MTEB AlloprofReranking
      config: default
      split: test
      revision: 65393d0d7a08a10b4e348135e824f385d420b0fd
    metrics:
    - type: map
      value: 73.63055206572554
    - type: mrr
      value: 74.69705225210407
    - type: nAUC_map_diff1
      value: 56.61121737089957
    - type: nAUC_map_max
      value: 21.353273116363358
    - type: nAUC_mrr_diff1
      value: 55.98316099424804
    - type: nAUC_mrr_max
      value: 22.29736406333825
  - task:
      type: Retrieval
    dataset:
      type: lyon-nlp/alloprof
      name: MTEB AlloprofRetrieval
      config: default
      split: test
      revision: fcf295ea64c750f41fadbaa37b9b861558e1bfbd
    metrics:
    - type: map_at_1
      value: 30.009000000000004
    - type: map_at_10
      value: 41.563
    - type: map_at_100
      value: 42.498999999999995
    - type: map_at_1000
      value: 42.541000000000004
    - type: map_at_20
      value: 42.142
    - type: map_at_3
      value: 38.443
    - type: map_at_5
      value: 40.23
    - type: mrr_at_1
      value: 30.008635578583764
    - type: mrr_at_10
      value: 41.563313869013434
    - type: mrr_at_100
      value: 42.49919838395685
    - type: mrr_at_1000
      value: 42.54117981321103
    - type: mrr_at_20
      value: 42.14177102110932
    - type: mrr_at_3
      value: 38.44271732872777
    - type: mrr_at_5
      value: 40.23028209556721
    - type: nauc_map_at_1000_diff1
      value: 37.69874084954785
    - type: nauc_map_at_1000_max
      value: 35.67975084044886
    - type: nauc_map_at_100_diff1
      value: 37.683425621005334
    - type: nauc_map_at_100_max
      value: 35.70179282323718
    - type: nauc_map_at_10_diff1
      value: 37.60741578478419
    - type: nauc_map_at_10_max
      value: 35.73500192122569
    - type: nauc_map_at_1_diff1
      value: 43.314035692233396
    - type: nauc_map_at_1_max
      value: 31.881007724238064
    - type: nauc_map_at_20_diff1
      value: 37.604821571809694
    - type: nauc_map_at_20_max
      value: 35.71558055856275
    - type: nauc_map_at_3_diff1
      value: 37.64200820646518
    - type: nauc_map_at_3_max
      value: 34.558370321480005
    - type: nauc_map_at_5_diff1
      value: 37.48910576281629
    - type: nauc_map_at_5_max
      value: 35.16709650751366
    - type: nauc_mrr_at_1000_diff1
      value: 37.69874084954785
    - type: nauc_mrr_at_1000_max
      value: 35.67975084044886
    - type: nauc_mrr_at_100_diff1
      value: 37.683425621005334
    - type: nauc_mrr_at_100_max
      value: 35.70179282323718
    - type: nauc_mrr_at_10_diff1
      value: 37.60741578478419
    - type: nauc_mrr_at_10_max
      value: 35.73500192122569
    - type: nauc_mrr_at_1_diff1
      value: 43.314035692233396
    - type: nauc_mrr_at_1_max
      value: 31.881007724238064
    - type: nauc_mrr_at_20_diff1
      value: 37.604821571809694
    - type: nauc_mrr_at_20_max
      value: 35.71558055856275
    - type: nauc_mrr_at_3_diff1
      value: 37.64200820646518
    - type: nauc_mrr_at_3_max
      value: 34.558370321480005
    - type: nauc_mrr_at_5_diff1
      value: 37.48910576281629
    - type: nauc_mrr_at_5_max
      value: 35.16709650751366
    - type: nauc_ndcg_at_1000_diff1
      value: 36.79519873157631
    - type: nauc_ndcg_at_1000_max
      value: 37.14476960275735
    - type: nauc_ndcg_at_100_diff1
      value: 36.283195451522566
    - type: nauc_ndcg_at_100_max
      value: 37.987689519253216
    - type: nauc_ndcg_at_10_diff1
      value: 35.911654796234906
    - type: nauc_ndcg_at_10_max
      value: 38.02420676430751
    - type: nauc_ndcg_at_1_diff1
      value: 43.314035692233396
    - type: nauc_ndcg_at_1_max
      value: 31.881007724238064
    - type: nauc_ndcg_at_20_diff1
      value: 35.84645351663945
    - type: nauc_ndcg_at_20_max
      value: 38.01406125615156
    - type: nauc_ndcg_at_3_diff1
      value: 36.088922679698285
    - type: nauc_ndcg_at_3_max
      value: 35.41968041752933
    - type: nauc_ndcg_at_5_diff1
      value: 35.750269212484895
    - type: nauc_ndcg_at_5_max
      value: 36.490862523260134
    - type: nauc_precision_at_1000_diff1
      value: 40.85377128270902
    - type: nauc_precision_at_1000_max
      value: 78.7188042554787
    - type: nauc_precision_at_100_diff1
      value: 25.95337392513788
    - type: nauc_precision_at_100_max
      value: 59.85395510353242
    - type: nauc_precision_at_10_diff1
      value: 29.989736669251176
    - type: nauc_precision_at_10_max
      value: 47.01836650640274
    - type: nauc_precision_at_1_diff1
      value: 43.314035692233396
    - type: nauc_precision_at_1_max
      value: 31.881007724238064
    - type: nauc_precision_at_20_diff1
      value: 28.236939136767763
    - type: nauc_precision_at_20_max
      value: 49.05567543361526
    - type: nauc_precision_at_3_diff1
      value: 31.697690633887817
    - type: nauc_precision_at_3_max
      value: 37.90080773298326
    - type: nauc_precision_at_5_diff1
      value: 30.466477711769823
    - type: nauc_precision_at_5_max
      value: 40.649885707001
    - type: nauc_recall_at_1000_diff1
      value: 40.85377128270638
    - type: nauc_recall_at_1000_max
      value: 78.71880425547653
    - type: nauc_recall_at_100_diff1
      value: 25.95337392513813
    - type: nauc_recall_at_100_max
      value: 59.8539551035326
    - type: nauc_recall_at_10_diff1
      value: 29.989736669251165
    - type: nauc_recall_at_10_max
      value: 47.01836650640268
    - type: nauc_recall_at_1_diff1
      value: 43.314035692233396
    - type: nauc_recall_at_1_max
      value: 31.881007724238064
    - type: nauc_recall_at_20_diff1
      value: 28.23693913676786
    - type: nauc_recall_at_20_max
      value: 49.055675433615214
    - type: nauc_recall_at_3_diff1
      value: 31.69769063388779
    - type: nauc_recall_at_3_max
      value: 37.90080773298324
    - type: nauc_recall_at_5_diff1
      value: 30.466477711769823
    - type: nauc_recall_at_5_max
      value: 40.64988570700102
    - type: ndcg_at_1
      value: 30.009000000000004
    - type: ndcg_at_10
      value: 47.598
    - type: ndcg_at_100
      value: 52.293
    - type: ndcg_at_1000
      value: 53.525999999999996
    - type: ndcg_at_20
      value: 49.697
    - type: ndcg_at_3
      value: 41.159
    - type: ndcg_at_5
      value: 44.379000000000005
    - type: precision_at_1
      value: 30.009000000000004
    - type: precision_at_10
      value: 6.675000000000001
    - type: precision_at_100
      value: 0.8909999999999999
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_20
      value: 3.752
    - type: precision_at_3
      value: 16.336000000000002
    - type: precision_at_5
      value: 11.364
    - type: recall_at_1
      value: 30.009000000000004
    - type: recall_at_10
      value: 66.753
    - type: recall_at_100
      value: 89.076
    - type: recall_at_1000
      value: 99.007
    - type: recall_at_20
      value: 75.043
    - type: recall_at_3
      value: 49.007
    - type: recall_at_5
      value: 56.821999999999996
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (fr)
      config: fr
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 43.422
    - type: f1
      value: 41.92216694262306
    - type: f1_weighted
      value: 41.92216694262306
  - task:
      type: Retrieval
    dataset:
      type: maastrichtlawtech/bsard
      name: MTEB BSARDRetrieval
      config: default
      split: test
      revision: 5effa1b9b5fa3b0f9e12523e6e43e5f86a6e6d59
    metrics:
    - type: map_at_1
      value: 10.811
    - type: map_at_10
      value: 15.839
    - type: map_at_100
      value: 17.031
    - type: map_at_1000
      value: 17.125
    - type: map_at_20
      value: 16.523
    - type: map_at_3
      value: 13.514000000000001
    - type: map_at_5
      value: 14.482000000000001
    - type: mrr_at_1
      value: 10.81081081081081
    - type: mrr_at_10
      value: 15.83923208923209
    - type: mrr_at_100
      value: 17.03089784389729
    - type: mrr_at_1000
      value: 17.12470244170791
    - type: mrr_at_20
      value: 16.522687430195177
    - type: mrr_at_3
      value: 13.513513513513514
    - type: mrr_at_5
      value: 14.481981981981978
    - type: nauc_map_at_1000_diff1
      value: 12.296170850430006
    - type: nauc_map_at_1000_max
      value: 5.662103058568523
    - type: nauc_map_at_100_diff1
      value: 12.285666762866096
    - type: nauc_map_at_100_max
      value: 5.590666559899351
    - type: nauc_map_at_10_diff1
      value: 11.58049149054967
    - type: nauc_map_at_10_max
      value: 5.209805828037212
    - type: nauc_map_at_1_diff1
      value: 20.141109249858847
    - type: nauc_map_at_1_max
      value: 9.425358945072293
    - type: nauc_map_at_20_diff1
      value: 11.617354631783714
    - type: nauc_map_at_20_max
      value: 5.241556548291933
    - type: nauc_map_at_3_diff1
      value: 13.315116892826943
    - type: nauc_map_at_3_max
      value: 6.207004916063591
    - type: nauc_map_at_5_diff1
      value: 11.212726154717592
    - type: nauc_map_at_5_max
      value: 5.3760763604334425
    - type: nauc_mrr_at_1000_diff1
      value: 12.296170850430006
    - type: nauc_mrr_at_1000_max
      value: 5.662103058568523
    - type: nauc_mrr_at_100_diff1
      value: 12.285666762866096
    - type: nauc_mrr_at_100_max
      value: 5.590666559899351
    - type: nauc_mrr_at_10_diff1
      value: 11.58049149054967
    - type: nauc_mrr_at_10_max
      value: 5.209805828037212
    - type: nauc_mrr_at_1_diff1
      value: 20.141109249858847
    - type: nauc_mrr_at_1_max
      value: 9.425358945072293
    - type: nauc_mrr_at_20_diff1
      value: 11.617354631783714
    - type: nauc_mrr_at_20_max
      value: 5.241556548291933
    - type: nauc_mrr_at_3_diff1
      value: 13.315116892826943
    - type: nauc_mrr_at_3_max
      value: 6.207004916063591
    - type: nauc_mrr_at_5_diff1
      value: 11.212726154717592
    - type: nauc_mrr_at_5_max
      value: 5.3760763604334425
    - type: nauc_ndcg_at_1000_diff1
      value: 12.38831869003625
    - type: nauc_ndcg_at_1000_max
      value: 6.675430140878355
    - type: nauc_ndcg_at_100_diff1
      value: 11.843284381117181
    - type: nauc_ndcg_at_100_max
      value: 5.542728863687718
    - type: nauc_ndcg_at_10_diff1
      value: 8.66584135181116
    - type: nauc_ndcg_at_10_max
      value: 4.199774551140183
    - type: nauc_ndcg_at_1_diff1
      value: 20.141109249858847
    - type: nauc_ndcg_at_1_max
      value: 9.425358945072293
    - type: nauc_ndcg_at_20_diff1
      value: 8.680542981318624
    - type: nauc_ndcg_at_20_max
      value: 4.216498269464542
    - type: nauc_ndcg_at_3_diff1
      value: 11.094054719430453
    - type: nauc_ndcg_at_3_max
      value: 5.507171227350456
    - type: nauc_ndcg_at_5_diff1
      value: 7.748133598511381
    - type: nauc_ndcg_at_5_max
      value: 4.076288186702726
    - type: nauc_precision_at_1000_diff1
      value: 25.897031968656297
    - type: nauc_precision_at_1000_max
      value: 19.982892062685394
    - type: nauc_precision_at_100_diff1
      value: 14.201820489201856
    - type: nauc_precision_at_100_max
      value: 6.304295684751489
    - type: nauc_precision_at_10_diff1
      value: 2.939526558265023
    - type: nauc_precision_at_10_max
      value: 2.467000352864203
    - type: nauc_precision_at_1_diff1
      value: 20.141109249858847
    - type: nauc_precision_at_1_max
      value: 9.425358945072293
    - type: nauc_precision_at_20_diff1
      value: 2.9380349371686325
    - type: nauc_precision_at_20_max
      value: 2.4267726696156506
    - type: nauc_precision_at_3_diff1
      value: 5.710288720068727
    - type: nauc_precision_at_3_max
      value: 3.885431233734222
    - type: nauc_precision_at_5_diff1
      value: -0.1440114189741616
    - type: nauc_precision_at_5_max
      value: 1.113579440082908
    - type: nauc_recall_at_1000_diff1
      value: 25.89703196865645
    - type: nauc_recall_at_1000_max
      value: 19.98289206268554
    - type: nauc_recall_at_100_diff1
      value: 14.20182048920192
    - type: nauc_recall_at_100_max
      value: 6.304295684751512
    - type: nauc_recall_at_10_diff1
      value: 2.939526558265029
    - type: nauc_recall_at_10_max
      value: 2.4670003528641624
    - type: nauc_recall_at_1_diff1
      value: 20.141109249858847
    - type: nauc_recall_at_1_max
      value: 9.425358945072293
    - type: nauc_recall_at_20_diff1
      value: 2.9380349371685828
    - type: nauc_recall_at_20_max
      value: 2.4267726696155965
    - type: nauc_recall_at_3_diff1
      value: 5.710288720068724
    - type: nauc_recall_at_3_max
      value: 3.885431233734255
    - type: nauc_recall_at_5_diff1
      value: -0.14401141897419695
    - type: nauc_recall_at_5_max
      value: 1.1135794400828594
    - type: ndcg_at_1
      value: 10.811
    - type: ndcg_at_10
      value: 19.583000000000002
    - type: ndcg_at_100
      value: 26.135
    - type: ndcg_at_1000
      value: 28.916999999999998
    - type: ndcg_at_20
      value: 22.158
    - type: ndcg_at_3
      value: 14.543000000000001
    - type: ndcg_at_5
      value: 16.345000000000002
    - type: precision_at_1
      value: 10.811
    - type: precision_at_10
      value: 3.198
    - type: precision_at_100
      value: 0.644
    - type: precision_at_1000
      value: 0.087
    - type: precision_at_20
      value: 2.117
    - type: precision_at_3
      value: 5.856
    - type: precision_at_5
      value: 4.414
    - type: recall_at_1
      value: 10.811
    - type: recall_at_10
      value: 31.982
    - type: recall_at_100
      value: 64.414
    - type: recall_at_1000
      value: 86.937
    - type: recall_at_20
      value: 42.342
    - type: recall_at_3
      value: 17.568
    - type: recall_at_5
      value: 22.072
  - task:
      type: Clustering
    dataset:
      type: lyon-nlp/clustering-hal-s2s
      name: MTEB HALClusteringS2S
      config: default
      split: test
      revision: e06ebbbb123f8144bef1a5d18796f3dec9ae2915
    metrics:
    - type: v_measure
      value: 26.26502535631247
    - type: v_measures
      value: [0.30893096531878045, 0.27408569069152805, 0.2872676670832888, 0.26871778422889214, 0.2421329238735192]
  - task:
      type: Clustering
    dataset:
      type: reciTAL/mlsum
      name: MTEB MLSUMClusteringP2P
      config: fr
      split: test
      revision: b5d54f8f3b61ae17845046286940f03c6bc79bc7
    metrics:
    - type: v_measure
      value: 42.60059039120384
    - type: v_measures
      value: [0.4248169037837413, 0.44678284494908554, 0.4386784796938775, 0.41609051956546156, 0.37929269357080225]
  - task:
      type: Clustering
    dataset:
      type: reciTAL/mlsum
      name: MTEB MLSUMClusteringS2S
      config: fr
      split: test
      revision: b5d54f8f3b61ae17845046286940f03c6bc79bc7
    metrics:
    - type: v_measure
      value: 42.92324222522204
    - type: v_measures
      value: [0.4320945601805418, 0.43467886343873713, 0.4345273113581795, 0.4277842446367462, 0.381555432691925]
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (fr)
      config: fr
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 88.33385530848732
    - type: f1
      value: 88.36975245849551
    - type: f1_weighted
      value: 88.310383667222
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (fr)
      config: fr
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 62.84685248982148
    - type: f1
      value: 44.420122133882366
    - type: f1_weighted
      value: 65.2728620649712
  - task:
      type: Classification
    dataset:
      type: mteb/masakhanews
      name: MTEB MasakhaNEWSClassification (fra)
      config: fra
      split: test
      revision: 18193f187b92da67168c655c9973a165ed9593dd
    metrics:
    - type: accuracy
      value: 80.56872037914692
    - type: f1
      value: 77.28557364601339
    - type: f1_weighted
      value: 80.51403795220486
  - task:
      type: Clustering
    dataset:
      type: masakhane/masakhanews
      name: MTEB MasakhaNEWSClusteringP2P (fra)
      config: fra
      split: test
      revision: 8ccc72e69e65f40c70e117d8b3c08306bb788b60
    metrics:
    - type: v_measure
      value: 71.29428035967938
    - type: v_measures
      value: [1.0, 0.2773866490640993, 0.7679216739314454, 0.8367645040119921, 0.6826411909764316]
  - task:
      type: Clustering
    dataset:
      type: masakhane/masakhanews
      name: MTEB MasakhaNEWSClusteringS2S (fra)
      config: fra
      split: test
      revision: 8ccc72e69e65f40c70e117d8b3c08306bb788b60
    metrics:
    - type: v_measure
      value: 55.090949643200084
    - type: v_measures
      value: [1.0, 0.0008196849334082873, 0.7532269197656756, 0.37056337344528145, 0.6299375040156386]
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (fr)
      config: fr
      split: test
      revision: 4672e20407010da34463acc759c162ca9734bca6
    metrics:
    - type: accuracy
      value: 66.80564895763281
    - type: f1
      value: 64.35238995318795
    - type: f1_weighted
      value: 65.7206181780162
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (fr)
      config: fr
      split: test
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
    metrics:
    - type: accuracy
      value: 72.98587760591795
    - type: f1
      value: 72.51250718054763
    - type: f1_weighted
      value: 72.81793917434213
  - task:
      type: Retrieval
    dataset:
      type: jinaai/mintakaqa
      name: MTEB MintakaRetrieval (fr)
      config: fr
      split: test
      revision: efa78cc2f74bbcd21eff2261f9e13aebe40b814e
    metrics:
    - type: map_at_1
      value: 18.96
    - type: map_at_10
      value: 27.744999999999997
    - type: map_at_100
      value: 28.799000000000003
    - type: map_at_1000
      value: 28.884
    - type: map_at_20
      value: 28.375
    - type: map_at_3
      value: 25.108999999999998
    - type: map_at_5
      value: 26.508
    - type: mrr_at_1
      value: 18.95986895986896
    - type: mrr_at_10
      value: 27.744936494936507
    - type: mrr_at_100
      value: 28.79940115805784
    - type: mrr_at_1000
      value: 28.88414927603794
    - type: mrr_at_20
      value: 28.375232375900854
    - type: mrr_at_3
      value: 25.109200109200113
    - type: mrr_at_5
      value: 26.50764400764402
    - type: nauc_map_at_1000_diff1
      value: 18.685236785487458
    - type: nauc_map_at_1000_max
      value: 28.85413041872925
    - type: nauc_map_at_100_diff1
      value: 18.643854459374264
    - type: nauc_map_at_100_max
      value: 28.86568866859659
    - type: nauc_map_at_10_diff1
      value: 18.95179019467019
    - type: nauc_map_at_10_max
      value: 28.978754512041366
    - type: nauc_map_at_1_diff1
      value: 24.276017299858978
    - type: nauc_map_at_1_max
      value: 23.470875089293564
    - type: nauc_map_at_20_diff1
      value: 18.635084934956904
    - type: nauc_map_at_20_max
      value: 28.94762423672467
    - type: nauc_map_at_3_diff1
      value: 19.78833161521705
    - type: nauc_map_at_3_max
      value: 27.717678662759226
    - type: nauc_map_at_5_diff1
      value: 19.121183364075133
    - type: nauc_map_at_5_max
      value: 28.33281003699522
    - type: nauc_mrr_at_1000_diff1
      value: 18.685236785487458
    - type: nauc_mrr_at_1000_max
      value: 28.85413041872925
    - type: nauc_mrr_at_100_diff1
      value: 18.643854459374264
    - type: nauc_mrr_at_100_max
      value: 28.86568866859659
    - type: nauc_mrr_at_10_diff1
      value: 18.95179019467019
    - type: nauc_mrr_at_10_max
      value: 28.978754512041366
    - type: nauc_mrr_at_1_diff1
      value: 24.276017299858978
    - type: nauc_mrr_at_1_max
      value: 23.470875089293564
    - type: nauc_mrr_at_20_diff1
      value: 18.635084934956904
    - type: nauc_mrr_at_20_max
      value: 28.94762423672467
    - type: nauc_mrr_at_3_diff1
      value: 19.78833161521705
    - type: nauc_mrr_at_3_max
      value: 27.717678662759226
    - type: nauc_mrr_at_5_diff1
      value: 19.121183364075133
    - type: nauc_mrr_at_5_max
      value: 28.33281003699522
    - type: nauc_ndcg_at_1000_diff1
      value: 16.9385175619818
    - type: nauc_ndcg_at_1000_max
      value: 30.464626780924114
    - type: nauc_ndcg_at_100_diff1
      value: 15.784507139472703
    - type: nauc_ndcg_at_100_max
      value: 30.783304190943873
    - type: nauc_ndcg_at_10_diff1
      value: 17.074677821502657
    - type: nauc_ndcg_at_10_max
      value: 31.39661325771708
    - type: nauc_ndcg_at_1_diff1
      value: 24.276017299858978
    - type: nauc_ndcg_at_1_max
      value: 23.470875089293564
    - type: nauc_ndcg_at_20_diff1
      value: 15.905931373911173
    - type: nauc_ndcg_at_20_max
      value: 31.283157447315457
    - type: nauc_ndcg_at_3_diff1
      value: 18.520146441301954
    - type: nauc_ndcg_at_3_max
      value: 28.855566633100217
    - type: nauc_ndcg_at_5_diff1
      value: 17.414930054902594
    - type: nauc_ndcg_at_5_max
      value: 29.89288498763886
    - type: nauc_precision_at_1000_diff1
      value: 5.6404707169181485
    - type: nauc_precision_at_1000_max
      value: 51.53249587390901
    - type: nauc_precision_at_100_diff1
      value: 2.6401827420753463
    - type: nauc_precision_at_100_max
      value: 37.544518255619415
    - type: nauc_precision_at_10_diff1
      value: 12.07308037199035
    - type: nauc_precision_at_10_max
      value: 38.23001565740937
    - type: nauc_precision_at_1_diff1
      value: 24.276017299858978
    - type: nauc_precision_at_1_max
      value: 23.470875089293564
    - type: nauc_precision_at_20_diff1
      value: 7.157477225670103
    - type: nauc_precision_at_20_max
      value: 38.273237139593256
    - type: nauc_precision_at_3_diff1
      value: 15.259422549391488
    - type: nauc_precision_at_3_max
      value: 31.763923868965588
    - type: nauc_precision_at_5_diff1
      value: 13.005921624910583
    - type: nauc_precision_at_5_max
      value: 33.92162820494794
    - type: nauc_recall_at_1000_diff1
      value: 5.6404707169180055
    - type: nauc_recall_at_1000_max
      value: 51.53249587390878
    - type: nauc_recall_at_100_diff1
      value: 2.640182742075308
    - type: nauc_recall_at_100_max
      value: 37.544518255619444
    - type: nauc_recall_at_10_diff1
      value: 12.073080371990335
    - type: nauc_recall_at_10_max
      value: 38.230015657409375
    - type: nauc_recall_at_1_diff1
      value: 24.276017299858978
    - type: nauc_recall_at_1_max
      value: 23.470875089293564
    - type: nauc_recall_at_20_diff1
      value: 7.157477225670139
    - type: nauc_recall_at_20_max
      value: 38.27323713959323
    - type: nauc_recall_at_3_diff1
      value: 15.259422549391505
    - type: nauc_recall_at_3_max
      value: 31.763923868965588
    - type: nauc_recall_at_5_diff1
      value: 13.005921624910567
    - type: nauc_recall_at_5_max
      value: 33.92162820494793
    - type: ndcg_at_1
      value: 18.96
    - type: ndcg_at_10
      value: 32.617000000000004
    - type: ndcg_at_100
      value: 37.974000000000004
    - type: ndcg_at_1000
      value: 40.65
    - type: ndcg_at_20
      value: 34.888000000000005
    - type: ndcg_at_3
      value: 27.106
    - type: ndcg_at_5
      value: 29.614
    - type: precision_at_1
      value: 18.96
    - type: precision_at_10
      value: 4.824
    - type: precision_at_100
      value: 0.738
    - type: precision_at_1000
      value: 0.096
    - type: precision_at_20
      value: 2.858
    - type: precision_at_3
      value: 10.961
    - type: precision_at_5
      value: 7.789
    - type: recall_at_1
      value: 18.96
    - type: recall_at_10
      value: 48.239
    - type: recall_at_100
      value: 73.833
    - type: recall_at_1000
      value: 95.82300000000001
    - type: recall_at_20
      value: 57.166
    - type: recall_at_3
      value: 32.883
    - type: recall_at_5
      value: 38.943
  - task:
      type: PairClassification
    dataset:
      type: GEM/opusparcus
      name: MTEB OpusparcusPC (fr)
      config: fr
      split: test
      revision: 9e9b1f8ef51616073f47f306f7f47dd91663f86a
    metrics:
    - type: cos_sim_accuracy
      value: 84.80926430517711
    - type: cos_sim_ap
      value: 94.76661922683681
    - type: cos_sim_f1
      value: 89.31480594154289
    - type: cos_sim_precision
      value: 86.29629629629629
    - type: cos_sim_recall
      value: 92.55213505461768
    - type: dot_accuracy
      value: 84.80926430517711
    - type: dot_ap
      value: 94.76663088644299
    - type: dot_f1
      value: 89.31480594154289
    - type: dot_precision
      value: 86.29629629629629
    - type: dot_recall
      value: 92.55213505461768
    - type: euclidean_accuracy
      value: 84.80926430517711
    - type: euclidean_ap
      value: 94.76661922683681
    - type: euclidean_f1
      value: 89.31480594154289
    - type: euclidean_precision
      value: 86.29629629629629
    - type: euclidean_recall
      value: 92.55213505461768
    - type: manhattan_accuracy
      value: 84.94550408719346
    - type: manhattan_ap
      value: 94.78582392571815
    - type: manhattan_f1
      value: 89.33912204534491
    - type: manhattan_precision
      value: 86.86679174484052
    - type: manhattan_recall
      value: 91.95630585898709
    - type: max_accuracy
      value: 84.94550408719346
    - type: max_ap
      value: 94.78582392571815
    - type: max_f1
      value: 89.33912204534491
  - task:
      type: PairClassification
    dataset:
      type: google-research-datasets/paws-x
      name: MTEB PawsX (fr)
      config: fr
      split: test
      revision: 8a04d940a42cd40658986fdd8e3da561533a3646
    metrics:
    - type: cos_sim_accuracy
      value: 64.5
    - type: cos_sim_ap
      value: 64.51219412005997
    - type: cos_sim_f1
      value: 62.84885828198622
    - type: cos_sim_precision
      value: 46.713362068965516
    - type: cos_sim_recall
      value: 96.01328903654485
    - type: dot_accuracy
      value: 64.5
    - type: dot_ap
      value: 64.50290830259848
    - type: dot_f1
      value: 62.84885828198622
    - type: dot_precision
      value: 46.713362068965516
    - type: dot_recall
      value: 96.01328903654485
    - type: euclidean_accuracy
      value: 64.5
    - type: euclidean_ap
      value: 64.51219412005995
    - type: euclidean_f1
      value: 62.84885828198622
    - type: euclidean_precision
      value: 46.713362068965516
    - type: euclidean_recall
      value: 96.01328903654485
    - type: manhattan_accuracy
      value: 64.55
    - type: manhattan_ap
      value: 64.54022554293084
    - type: manhattan_f1
      value: 62.836363636363636
    - type: manhattan_precision
      value: 46.778559826746076
    - type: manhattan_recall
      value: 95.68106312292359
    - type: max_accuracy
      value: 64.55
    - type: max_ap
      value: 64.54022554293084
    - type: max_f1
      value: 62.84885828198622
  - task:
      type: STS
    dataset:
      type: Lajavaness/SICK-fr
      name: MTEB SICKFr
      config: default
      split: test
      revision: e077ab4cf4774a1e36d86d593b150422fafd8e8a
    metrics:
    - type: cos_sim_pearson
      value: 85.15315949054092
    - type: cos_sim_spearman
      value: 79.19701933507372
    - type: euclidean_pearson
      value: 82.68441006897395
    - type: euclidean_spearman
      value: 79.1963186010215
    - type: manhattan_pearson
      value: 82.6725500567899
    - type: manhattan_spearman
      value: 79.13255295711785
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (fr)
      config: fr
      split: test
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
    metrics:
    - type: cos_sim_pearson
      value: 83.13328685349694
    - type: cos_sim_spearman
      value: 84.64291479319418
    - type: euclidean_pearson
      value: 83.28605886303359
    - type: euclidean_spearman
      value: 84.64291479319418
    - type: manhattan_pearson
      value: 83.01485484058145
    - type: manhattan_spearman
      value: 84.35826862976153
  - task:
      type: STS
    dataset:
      type: mteb/stsb_multi_mt
      name: MTEB STSBenchmarkMultilingualSTS (fr)
      config: fr
      split: test
      revision: 29afa2569dcedaaa2fe6a3dcfebab33d28b82e8c
    metrics:
    - type: cos_sim_pearson
      value: 86.15391910168253
    - type: cos_sim_spearman
      value: 87.0224186207858
    - type: euclidean_pearson
      value: 86.04463800957714
    - type: euclidean_spearman
      value: 87.02424394489165
    - type: manhattan_pearson
      value: 86.03126279628441
    - type: manhattan_spearman
      value: 86.99427177229043
  - task:
      type: Summarization
    dataset:
      type: lyon-nlp/summarization-summeval-fr-p2p
      name: MTEB SummEvalFr
      config: default
      split: test
      revision: b385812de6a9577b6f4d0f88c6a6e35395a94054
    metrics:
    - type: cos_sim_pearson
      value: 31.415083738613355
    - type: cos_sim_spearman
      value: 30.301784303588285
    - type: dot_pearson
      value: 31.415089981266963
    - type: dot_spearman
      value: 30.286152348575108
  - task:
      type: Reranking
    dataset:
      type: lyon-nlp/mteb-fr-reranking-syntec-s2p
      name: MTEB SyntecReranking
      config: default
      split: test
      revision: daf0863838cd9e3ba50544cdce3ac2b338a1b0ad
    metrics:
    - type: map
      value: 85.95238095238095
    - type: mrr
      value: 85.95238095238095
    - type: nAUC_map_diff1
      value: 70.42176052252755
    - type: nAUC_map_max
      value: 19.806028833551718
    - type: nAUC_mrr_diff1
      value: 70.42176052252755
    - type: nAUC_mrr_max
      value: 19.806028833551718
  - task:
      type: Retrieval
    dataset:
      type: lyon-nlp/mteb-fr-retrieval-syntec-s2p
      name: MTEB SyntecRetrieval
      config: default
      split: test
      revision: 19661ccdca4dfc2d15122d776b61685f48c68ca9
    metrics:
    - type: map_at_1
      value: 69.0
    - type: map_at_10
      value: 79.668
    - type: map_at_100
      value: 79.791
    - type: map_at_1000
      value: 79.791
    - type: map_at_20
      value: 79.751
    - type: map_at_3
      value: 78.167
    - type: map_at_5
      value: 79.067
    - type: mrr_at_1
      value: 69.0
    - type: mrr_at_10
      value: 79.66785714285714
    - type: mrr_at_100
      value: 79.7911904761905
    - type: mrr_at_1000
      value: 79.7911904761905
    - type: mrr_at_20
      value: 79.75119047619049
    - type: mrr_at_3
      value: 78.16666666666666
    - type: mrr_at_5
      value: 79.06666666666666
    - type: nauc_map_at_1000_diff1
      value: 57.567834845260215
    - type: nauc_map_at_1000_max
      value: 19.884081021539316
    - type: nauc_map_at_100_diff1
      value: 57.567834845260215
    - type: nauc_map_at_100_max
      value: 19.884081021539316
    - type: nauc_map_at_10_diff1
      value: 57.58744042822529
    - type: nauc_map_at_10_max
      value: 20.086792005769567
    - type: nauc_map_at_1_diff1
      value: 58.094784556502134
    - type: nauc_map_at_1_max
      value: 16.46471594616999
    - type: nauc_map_at_20_diff1
      value: 57.51896058548769
    - type: nauc_map_at_20_max
      value: 19.71285790868927
    - type: nauc_map_at_3_diff1
      value: 57.896383908331885
    - type: nauc_map_at_3_max
      value: 19.524006306996704
    - type: nauc_map_at_5_diff1
      value: 57.45922462199208
    - type: nauc_map_at_5_max
      value: 21.48138549193403
    - type: nauc_mrr_at_1000_diff1
      value: 57.567834845260215
    - type: nauc_mrr_at_1000_max
      value: 19.884081021539316
    - type: nauc_mrr_at_100_diff1
      value: 57.567834845260215
    - type: nauc_mrr_at_100_max
      value: 19.884081021539316
    - type: nauc_mrr_at_10_diff1
      value: 57.58744042822529
    - type: nauc_mrr_at_10_max
      value: 20.086792005769567
    - type: nauc_mrr_at_1_diff1
      value: 58.094784556502134
    - type: nauc_mrr_at_1_max
      value: 16.46471594616999
    - type: nauc_mrr_at_20_diff1
      value: 57.51896058548769
    - type: nauc_mrr_at_20_max
      value: 19.71285790868927
    - type: nauc_mrr_at_3_diff1
      value: 57.896383908331885
    - type: nauc_mrr_at_3_max
      value: 19.524006306996704
    - type: nauc_mrr_at_5_diff1
      value: 57.45922462199208
    - type: nauc_mrr_at_5_max
      value: 21.48138549193403
    - type: nauc_ndcg_at_1000_diff1
      value: 57.45681586498414
    - type: nauc_ndcg_at_1000_max
      value: 20.083159493214627
    - type: nauc_ndcg_at_100_diff1
      value: 57.45681586498414
    - type: nauc_ndcg_at_100_max
      value: 20.083159493214627
    - type: nauc_ndcg_at_10_diff1
      value: 57.41282118307387
    - type: nauc_ndcg_at_10_max
      value: 20.46449823725533
    - type: nauc_ndcg_at_1_diff1
      value: 58.094784556502134
    - type: nauc_ndcg_at_1_max
      value: 16.46471594616999
    - type: nauc_ndcg_at_20_diff1
      value: 57.121174268460486
    - type: nauc_ndcg_at_20_max
      value: 18.898176707436974
    - type: nauc_ndcg_at_3_diff1
      value: 57.98367634437588
    - type: nauc_ndcg_at_3_max
      value: 20.131770232644623
    - type: nauc_ndcg_at_5_diff1
      value: 56.88983122749084
    - type: nauc_ndcg_at_5_max
      value: 24.213859501270516
    - type: nauc_precision_at_1000_diff1
      value: nan
    - type: nauc_precision_at_1000_max
      value: nan
    - type: nauc_precision_at_100_diff1
      value: nan
    - type: nauc_precision_at_100_max
      value: nan
    - type: nauc_precision_at_10_diff1
      value: 54.014939309057695
    - type: nauc_precision_at_10_max
      value: 21.82539682539744
    - type: nauc_precision_at_1_diff1
      value: 58.094784556502134
    - type: nauc_precision_at_1_max
      value: 16.46471594616999
    - type: nauc_precision_at_20_diff1
      value: 35.80765639589114
    - type: nauc_precision_at_20_max
      value: -56.34920634920767
    - type: nauc_precision_at_3_diff1
      value: 58.57142857142844
    - type: nauc_precision_at_3_max
      value: 23.053221288515303
    - type: nauc_precision_at_5_diff1
      value: 51.26050420168061
    - type: nauc_precision_at_5_max
      value: 49.00404606286964
    - type: nauc_recall_at_1000_diff1
      value: nan
    - type: nauc_recall_at_1000_max
      value: nan
    - type: nauc_recall_at_100_diff1
      value: nan
    - type: nauc_recall_at_100_max
      value: nan
    - type: nauc_recall_at_10_diff1
      value: 54.0149393090569
    - type: nauc_recall_at_10_max
      value: 21.825396825396858
    - type: nauc_recall_at_1_diff1
      value: 58.094784556502134
    - type: nauc_recall_at_1_max
      value: 16.46471594616999
    - type: nauc_recall_at_20_diff1
      value: 35.80765639589109
    - type: nauc_recall_at_20_max
      value: -56.34920634920657
    - type: nauc_recall_at_3_diff1
      value: 58.571428571428505
    - type: nauc_recall_at_3_max
      value: 23.05322128851543
    - type: nauc_recall_at_5_diff1
      value: 51.260504201680824
    - type: nauc_recall_at_5_max
      value: 49.004046062869584
    - type: ndcg_at_1
      value: 69.0
    - type: ndcg_at_10
      value: 84.198
    - type: ndcg_at_100
      value: 84.681
    - type: ndcg_at_1000
      value: 84.681
    - type: ndcg_at_20
      value: 84.46900000000001
    - type: ndcg_at_3
      value: 81.202
    - type: ndcg_at_5
      value: 82.837
    - type: precision_at_1
      value: 69.0
    - type: precision_at_10
      value: 9.8
    - type: precision_at_100
      value: 1.0
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.95
    - type: precision_at_3
      value: 30.0
    - type: precision_at_5
      value: 18.8
    - type: recall_at_1
      value: 69.0
    - type: recall_at_10
      value: 98.0
    - type: recall_at_100
      value: 100.0
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 99.0
    - type: recall_at_3
      value: 90.0
    - type: recall_at_5
      value: 94.0
  - task:
      type: Retrieval
    dataset:
      type: jinaai/xpqa
      name: MTEB XPQARetrieval (fr)
      config: fr
      split: test
      revision: c99d599f0a6ab9b85b065da6f9d94f9cf731679f
    metrics:
    - type: map_at_1
      value: 37.454
    - type: map_at_10
      value: 59.729
    - type: map_at_100
      value: 61.231
    - type: map_at_1000
      value: 61.282000000000004
    - type: map_at_20
      value: 60.675000000000004
    - type: map_at_3
      value: 53.425999999999995
    - type: map_at_5
      value: 57.565999999999995
    - type: mrr_at_1
      value: 59.279038718291055
    - type: mrr_at_10
      value: 68.25534575200794
    - type: mrr_at_100
      value: 68.80659018708569
    - type: mrr_at_1000
      value: 68.81865645170022
    - type: mrr_at_20
      value: 68.62067293285176
    - type: mrr_at_3
      value: 66.24388072986201
    - type: mrr_at_5
      value: 67.57231864708496
    - type: nauc_map_at_1000_diff1
      value: 47.188346029255904
    - type: nauc_map_at_1000_max
      value: 49.17571323638286
    - type: nauc_map_at_100_diff1
      value: 47.16123074739342
    - type: nauc_map_at_100_max
      value: 49.19310263766242
    - type: nauc_map_at_10_diff1
      value: 47.06916702645733
    - type: nauc_map_at_10_max
      value: 48.71944957298283
    - type: nauc_map_at_1_diff1
      value: 59.84256327261954
    - type: nauc_map_at_1_max
      value: 32.90724281546186
    - type: nauc_map_at_20_diff1
      value: 46.88963870698908
    - type: nauc_map_at_20_max
      value: 48.837735052949604
    - type: nauc_map_at_3_diff1
      value: 49.17542430030986
    - type: nauc_map_at_3_max
      value: 43.2855626692105
    - type: nauc_map_at_5_diff1
      value: 46.947951705937555
    - type: nauc_map_at_5_max
      value: 47.00840211882553
    - type: nauc_mrr_at_1000_diff1
      value: 55.082943973528565
    - type: nauc_mrr_at_1000_max
      value: 55.52321995030937
    - type: nauc_mrr_at_100_diff1
      value: 55.08053171175168
    - type: nauc_mrr_at_100_max
      value: 55.52564563109655
    - type: nauc_mrr_at_10_diff1
      value: 54.77154085090217
    - type: nauc_mrr_at_10_max
      value: 55.49364009135962
    - type: nauc_mrr_at_1_diff1
      value: 59.73731850363215
    - type: nauc_mrr_at_1_max
      value: 56.85669277331276
    - type: nauc_mrr_at_20_diff1
      value: 55.03367328751308
    - type: nauc_mrr_at_20_max
      value: 55.455991589323304
    - type: nauc_mrr_at_3_diff1
      value: 54.93497528080088
    - type: nauc_mrr_at_3_max
      value: 55.18680886181823
    - type: nauc_mrr_at_5_diff1
      value: 54.54195519307725
    - type: nauc_mrr_at_5_max
      value: 55.4153590074824
    - type: nauc_ndcg_at_1000_diff1
      value: 48.58663186947544
    - type: nauc_ndcg_at_1000_max
      value: 51.99609046381255
    - type: nauc_ndcg_at_100_diff1
      value: 48.03018958632311
    - type: nauc_ndcg_at_100_max
      value: 52.125240134521114
    - type: nauc_ndcg_at_10_diff1
      value: 46.8502876003221
    - type: nauc_ndcg_at_10_max
      value: 50.503877687033835
    - type: nauc_ndcg_at_1_diff1
      value: 59.73731850363215
    - type: nauc_ndcg_at_1_max
      value: 56.85669277331276
    - type: nauc_ndcg_at_20_diff1
      value: 46.84490807723349
    - type: nauc_ndcg_at_20_max
      value: 50.52318724553352
    - type: nauc_ndcg_at_3_diff1
      value: 47.45898183007377
    - type: nauc_ndcg_at_3_max
      value: 48.81807045626343
    - type: nauc_ndcg_at_5_diff1
      value: 46.27687550860212
    - type: nauc_ndcg_at_5_max
      value: 48.524704004044295
    - type: nauc_precision_at_1000_diff1
      value: -18.94279209896168
    - type: nauc_precision_at_1000_max
      value: 14.915754364583092
    - type: nauc_precision_at_100_diff1
      value: -17.608482478959505
    - type: nauc_precision_at_100_max
      value: 18.949680192042006
    - type: nauc_precision_at_10_diff1
      value: -7.9400256804121385
    - type: nauc_precision_at_10_max
      value: 28.840998769682585
    - type: nauc_precision_at_1_diff1
      value: 59.73731850363215
    - type: nauc_precision_at_1_max
      value: 56.85669277331276
    - type: nauc_precision_at_20_diff1
      value: -13.001497535637426
    - type: nauc_precision_at_20_max
      value: 23.362385750737513
    - type: nauc_precision_at_3_diff1
      value: 5.181216436208995
    - type: nauc_precision_at_3_max
      value: 36.84098890657479
    - type: nauc_precision_at_5_diff1
      value: -3.1561904832474466
    - type: nauc_precision_at_5_max
      value: 33.445624155484644
    - type: nauc_recall_at_1000_diff1
      value: 32.404068350548236
    - type: nauc_recall_at_1000_max
      value: 42.69981564475632
    - type: nauc_recall_at_100_diff1
      value: 24.30279254543539
    - type: nauc_recall_at_100_max
      value: 47.25263562130483
    - type: nauc_recall_at_10_diff1
      value: 34.095052463639355
    - type: nauc_recall_at_10_max
      value: 42.41582396664135
    - type: nauc_recall_at_1_diff1
      value: 59.84256327261954
    - type: nauc_recall_at_1_max
      value: 32.90724281546186
    - type: nauc_recall_at_20_diff1
      value: 30.621144467577782
    - type: nauc_recall_at_20_max
      value: 38.964128296844216
    - type: nauc_recall_at_3_diff1
      value: 40.61968199464558
    - type: nauc_recall_at_3_max
      value: 36.5150764611547
    - type: nauc_recall_at_5_diff1
      value: 34.535585254334265
    - type: nauc_recall_at_5_max
      value: 39.98160090846506
    - type: ndcg_at_1
      value: 59.279
    - type: ndcg_at_10
      value: 66.434
    - type: ndcg_at_100
      value: 71.32
    - type: ndcg_at_1000
      value: 72.04899999999999
    - type: ndcg_at_20
      value: 68.75
    - type: ndcg_at_3
      value: 61.144
    - type: ndcg_at_5
      value: 63.047
    - type: precision_at_1
      value: 59.279
    - type: precision_at_10
      value: 15.554000000000002
    - type: precision_at_100
      value: 1.965
    - type: precision_at_1000
      value: 0.20600000000000002
    - type: precision_at_20
      value: 8.598
    - type: precision_at_3
      value: 37.561
    - type: precision_at_5
      value: 26.968999999999998
    - type: recall_at_1
      value: 37.454
    - type: recall_at_10
      value: 76.629
    - type: recall_at_100
      value: 95.138
    - type: recall_at_1000
      value: 99.655
    - type: recall_at_20
      value: 84.11699999999999
    - type: recall_at_3
      value: 59.884
    - type: recall_at_5
      value: 68.556
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (en)
      config: en
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 78.19402985074629
    - type: ap
      value: 41.57371176187882
    - type: ap_weighted
      value: 41.57371176187882
    - type: f1
      value: 72.09309315449407
    - type: f1_weighted
      value: 80.00505225103721
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_polarity
      name: MTEB AmazonPolarityClassification
      config: default
      split: test
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
    metrics:
    - type: accuracy
      value: 90.69565
    - type: ap
      value: 87.20602734201051
    - type: ap_weighted
      value: 87.20602734201051
    - type: f1
      value: 90.68451855153312
    - type: f1_weighted
      value: 90.68451855153312
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (en)
      config: en
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 47.93600000000001
    - type: f1
      value: 46.501364617676295
    - type: f1_weighted
      value: 46.50136461767628
  - task:
      type: Retrieval
    dataset:
      type: mteb/arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
    metrics:
    - type: map_at_1
      value: 30.014000000000003
    - type: map_at_10
      value: 46.554
    - type: map_at_100
      value: 47.374
    - type: map_at_1000
      value: 47.377
    - type: map_at_20
      value: 47.258
    - type: map_at_3
      value: 41.323
    - type: map_at_5
      value: 44.391999999999996
    - type: mrr_at_1
      value: 30.440967283072546
    - type: mrr_at_10
      value: 46.711768159136604
    - type: mrr_at_100
      value: 47.538967857374644
    - type: mrr_at_1000
      value: 47.542068835741816
    - type: mrr_at_20
      value: 47.422917075943836
    - type: mrr_at_3
      value: 41.48885727833096
    - type: mrr_at_5
      value: 44.55784732100524
    - type: nauc_map_at_1000_diff1
      value: 7.6518211870914215
    - type: nauc_map_at_1000_max
      value: -10.684552114979383
    - type: nauc_map_at_100_diff1
      value: 7.656106287133195
    - type: nauc_map_at_100_max
      value: -10.68027433120124
    - type: nauc_map_at_10_diff1
      value: 7.770440175757533
    - type: nauc_map_at_10_max
      value: -10.444279562177176
    - type: nauc_map_at_1_diff1
      value: 9.646653573653193
    - type: nauc_map_at_1_max
      value: -12.191767601922637
    - type: nauc_map_at_20_diff1
      value: 7.670546318998091
    - type: nauc_map_at_20_max
      value: -10.578685600766276
    - type: nauc_map_at_3_diff1
      value: 7.932525764083823
    - type: nauc_map_at_3_max
      value: -11.166242804817701
    - type: nauc_map_at_5_diff1
      value: 7.0892133434661515
    - type: nauc_map_at_5_max
      value: -10.829011883079351
    - type: nauc_mrr_at_1000_diff1
      value: 6.544773528828528
    - type: nauc_mrr_at_1000_max
      value: -11.303671909227932
    - type: nauc_mrr_at_100_diff1
      value: 6.549166052428763
    - type: nauc_mrr_at_100_max
      value: -11.299336735364719
    - type: nauc_mrr_at_10_diff1
      value: 6.653925049219008
    - type: nauc_mrr_at_10_max
      value: -11.081039433083244
    - type: nauc_mrr_at_1_diff1
      value: 8.394062483723184
    - type: nauc_mrr_at_1_max
      value: -12.66533134347915
    - type: nauc_mrr_at_20_diff1
      value: 6.56854492054585
    - type: nauc_mrr_at_20_max
      value: -11.194548037319171
    - type: nauc_mrr_at_3_diff1
      value: 6.891320677829977
    - type: nauc_mrr_at_3_max
      value: -11.70764455911193
    - type: nauc_mrr_at_5_diff1
      value: 6.062371803493383
    - type: nauc_mrr_at_5_max
      value: -11.381227727849522
    - type: nauc_ndcg_at_1000_diff1
      value: 7.526059324989312
    - type: nauc_ndcg_at_1000_max
      value: -10.106189267639783
    - type: nauc_ndcg_at_100_diff1
      value: 7.638616834366962
    - type: nauc_ndcg_at_100_max
      value: -9.964210357553782
    - type: nauc_ndcg_at_10_diff1
      value: 8.003174440708406
    - type: nauc_ndcg_at_10_max
      value: -8.77943407411311
    - type: nauc_ndcg_at_1_diff1
      value: 9.646653573653193
    - type: nauc_ndcg_at_1_max
      value: -12.191767601922637
    - type: nauc_ndcg_at_20_diff1
      value: 7.725293263852487
    - type: nauc_ndcg_at_20_max
      value: -9.133349757489318
    - type: nauc_ndcg_at_3_diff1
      value: 7.706553072166292
    - type: nauc_ndcg_at_3_max
      value: -10.728722029578856
    - type: nauc_ndcg_at_5_diff1
      value: 6.172713913900365
    - type: nauc_ndcg_at_5_max
      value: -9.968139051699756
    - type: nauc_precision_at_1000_diff1
      value: -2.6984056766826683
    - type: nauc_precision_at_1000_max
      value: 18.24025472404024
    - type: nauc_precision_at_100_diff1
      value: 26.731821288726067
    - type: nauc_precision_at_100_max
      value: 33.37949043353564
    - type: nauc_precision_at_10_diff1
      value: 11.194115052979745
    - type: nauc_precision_at_10_max
      value: 3.641866414806816
    - type: nauc_precision_at_1_diff1
      value: 9.646653573653193
    - type: nauc_precision_at_1_max
      value: -12.191767601922637
    - type: nauc_precision_at_20_diff1
      value: 13.092287471108587
    - type: nauc_precision_at_20_max
      value: 20.7021272808658
    - type: nauc_precision_at_3_diff1
      value: 7.133407073291083
    - type: nauc_precision_at_3_max
      value: -9.377928260039624
    - type: nauc_precision_at_5_diff1
      value: 2.774426521753896
    - type: nauc_precision_at_5_max
      value: -6.601100615009791
    - type: nauc_recall_at_1000_diff1
      value: -2.6984056766845947
    - type: nauc_recall_at_1000_max
      value: 18.240254724037225
    - type: nauc_recall_at_100_diff1
      value: 26.731821288725556
    - type: nauc_recall_at_100_max
      value: 33.379490433531856
    - type: nauc_recall_at_10_diff1
      value: 11.194115052979765
    - type: nauc_recall_at_10_max
      value: 3.641866414806695
    - type: nauc_recall_at_1_diff1
      value: 9.646653573653193
    - type: nauc_recall_at_1_max
      value: -12.191767601922637
    - type: nauc_recall_at_20_diff1
      value: 13.092287471108433
    - type: nauc_recall_at_20_max
      value: 20.702127280865565
    - type: nauc_recall_at_3_diff1
      value: 7.133407073291095
    - type: nauc_recall_at_3_max
      value: -9.377928260039656
    - type: nauc_recall_at_5_diff1
      value: 2.7744265217538717
    - type: nauc_recall_at_5_max
      value: -6.60110061500983
    - type: ndcg_at_1
      value: 30.014000000000003
    - type: ndcg_at_10
      value: 55.888000000000005
    - type: ndcg_at_100
      value: 59.105
    - type: ndcg_at_1000
      value: 59.172000000000004
    - type: ndcg_at_20
      value: 58.351
    - type: ndcg_at_3
      value: 45.182
    - type: ndcg_at_5
      value: 50.70099999999999
    - type: precision_at_1
      value: 30.014000000000003
    - type: precision_at_10
      value: 8.57
    - type: precision_at_100
      value: 0.991
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.7620000000000005
    - type: precision_at_3
      value: 18.8
    - type: precision_at_5
      value: 13.954
    - type: recall_at_1
      value: 30.014000000000003
    - type: recall_at_10
      value: 85.70400000000001
    - type: recall_at_100
      value: 99.14699999999999
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_20
      value: 95.235
    - type: recall_at_3
      value: 56.401
    - type: recall_at_5
      value: 69.772
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-p2p
      name: MTEB ArxivClusteringP2P
      config: default
      split: test
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
    metrics:
    - type: v_measure
      value: 46.17799646172208
    - type: v_measures
      value: [0.4723643361016671, 0.47021470393991005, 0.4665618875983067, 0.4694759882110438, 0.4710825932088269]
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-s2s
      name: MTEB ArxivClusteringS2S
      config: default
      split: test
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
    metrics:
    - type: v_measure
      value: 38.95382181977256
    - type: v_measures
      value: [0.37434399646466177, 0.4073444922309873, 0.39190374625714786, 0.3822490240275778, 0.40695566104112885]
  - task:
      type: Reranking
    dataset:
      type: mteb/askubuntudupquestions-reranking
      name: MTEB AskUbuntuDupQuestions
      config: default
      split: test
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
    metrics:
    - type: map
      value: 60.77428226049288
    - type: mrr
      value: 74.66231367893418
    - type: nAUC_map_diff1
      value: 8.088030406617092
    - type: nAUC_map_max
      value: 20.837499060141965
    - type: nAUC_mrr_diff1
      value: 14.808914539705173
    - type: nAUC_mrr_max
      value: 32.61075208984127
  - task:
      type: STS
    dataset:
      type: mteb/biosses-sts
      name: MTEB BIOSSES
      config: default
      split: test
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
    metrics:
    - type: cos_sim_pearson
      value: 90.14203628237179
    - type: cos_sim_spearman
      value: 87.86103811793475
    - type: euclidean_pearson
      value: 89.1570350222214
    - type: euclidean_spearman
      value: 87.86103811793475
    - type: manhattan_pearson
      value: 88.89930974259032
    - type: manhattan_spearman
      value: 87.87188173850797
  - task:
      type: Classification
    dataset:
      type: mteb/banking77
      name: MTEB Banking77Classification
      config: default
      split: test
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
    metrics:
    - type: accuracy
      value: 80.99025974025975
    - type: f1
      value: 80.34391357314699
    - type: f1_weighted
      value: 80.34391357314702
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-p2p
      name: MTEB BiorxivClusteringP2P
      config: default
      split: test
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
    metrics:
    - type: v_measure
      value: 37.413831528948
    - type: v_measures
      value: [0.36284135654233984, 0.3894746578427554, 0.3687193652607847, 0.369732449263521, 0.37046011245380284]
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-s2s
      name: MTEB BiorxivClusteringS2S
      config: default
      split: test
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
    metrics:
    - type: v_measure
      value: 34.952359512754214
    - type: v_measures
      value: [0.33651162601651474, 0.34349610750910153, 0.3497787542108308, 0.3354268169706765, 0.3423103936159304]
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-android
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: f46a197baaae43b4f621051089b82a364682dfeb
    metrics:
    - type: map_at_1
      value: 33.042
    - type: map_at_10
      value: 44.330999999999996
    - type: map_at_100
      value: 45.94
    - type: map_at_1000
      value: 46.06
    - type: map_at_20
      value: 45.303
    - type: map_at_3
      value: 40.338
    - type: map_at_5
      value: 42.626999999999995
    - type: mrr_at_1
      value: 41.48783977110158
    - type: mrr_at_10
      value: 51.47898358198787
    - type: mrr_at_100
      value: 52.20317087348633
    - type: mrr_at_1000
      value: 52.23993132896152
    - type: mrr_at_20
      value: 51.952609512502676
    - type: mrr_at_3
      value: 48.80782069623272
    - type: mrr_at_5
      value: 50.37434430138291
    - type: nauc_map_at_1000_diff1
      value: 48.89688396225479
    - type: nauc_map_at_1000_max
      value: 39.51982543452405
    - type: nauc_map_at_100_diff1
      value: 48.84486047376536
    - type: nauc_map_at_100_max
      value: 39.47618125790692
    - type: nauc_map_at_10_diff1
      value: 48.64778903091507
    - type: nauc_map_at_10_max
      value: 38.65727315638928
    - type: nauc_map_at_1_diff1
      value: 52.718043416663264
    - type: nauc_map_at_1_max
      value: 36.05458738264693
    - type: nauc_map_at_20_diff1
      value: 48.674520991493274
    - type: nauc_map_at_20_max
      value: 39.13049374867919
    - type: nauc_map_at_3_diff1
      value: 48.856641802372955
    - type: nauc_map_at_3_max
      value: 36.39687289406316
    - type: nauc_map_at_5_diff1
      value: 48.5068735124891
    - type: nauc_map_at_5_max
      value: 37.94774282180534
    - type: nauc_mrr_at_1000_diff1
      value: 50.86529654190889
    - type: nauc_mrr_at_1000_max
      value: 42.945676316661455
    - type: nauc_mrr_at_100_diff1
      value: 50.86738962836933
    - type: nauc_mrr_at_100_max
      value: 42.93895809947348
    - type: nauc_mrr_at_10_diff1
      value: 50.80787884821388
    - type: nauc_mrr_at_10_max
      value: 43.06530286605344
    - type: nauc_mrr_at_1_diff1
      value: 54.91425946606372
    - type: nauc_mrr_at_1_max
      value: 42.88388878131396
    - type: nauc_mrr_at_20_diff1
      value: 50.773844073424556
    - type: nauc_mrr_at_20_max
      value: 42.91601484038108
    - type: nauc_mrr_at_3_diff1
      value: 51.455139461166624
    - type: nauc_mrr_at_3_max
      value: 42.68923339240631
    - type: nauc_mrr_at_5_diff1
      value: 50.93357041799253
    - type: nauc_mrr_at_5_max
      value: 42.897260914203045
    - type: nauc_ndcg_at_1000_diff1
      value: 48.825613953213015
    - type: nauc_ndcg_at_1000_max
      value: 41.78992987142924
    - type: nauc_ndcg_at_100_diff1
      value: 48.15913399970223
    - type: nauc_ndcg_at_100_max
      value: 41.50178459973945
    - type: nauc_ndcg_at_10_diff1
      value: 47.386623100508864
    - type: nauc_ndcg_at_10_max
      value: 40.43396398321854
    - type: nauc_ndcg_at_1_diff1
      value: 54.91425946606372
    - type: nauc_ndcg_at_1_max
      value: 42.88388878131396
    - type: nauc_ndcg_at_20_diff1
      value: 47.30049480608728
    - type: nauc_ndcg_at_20_max
      value: 40.672480439383726
    - type: nauc_ndcg_at_3_diff1
      value: 48.48278253566928
    - type: nauc_ndcg_at_3_max
      value: 39.06887235132945
    - type: nauc_ndcg_at_5_diff1
      value: 47.324309938750154
    - type: nauc_ndcg_at_5_max
      value: 39.9475104940194
    - type: nauc_precision_at_1000_diff1
      value: -8.854973706380369
    - type: nauc_precision_at_1000_max
      value: 2.0466638723983874
    - type: nauc_precision_at_100_diff1
      value: -0.9047567876867986
    - type: nauc_precision_at_100_max
      value: 14.436598502482099
    - type: nauc_precision_at_10_diff1
      value: 16.81131823944348
    - type: nauc_precision_at_10_max
      value: 31.222844580594227
    - type: nauc_precision_at_1_diff1
      value: 54.91425946606372
    - type: nauc_precision_at_1_max
      value: 42.88388878131396
    - type: nauc_precision_at_20_diff1
      value: 8.91236626494447
    - type: nauc_precision_at_20_max
      value: 25.700031761460394
    - type: nauc_precision_at_3_diff1
      value: 33.62613953132739
    - type: nauc_precision_at_3_max
      value: 36.81289621298019
    - type: nauc_precision_at_5_diff1
      value: 24.28512312107285
    - type: nauc_precision_at_5_max
      value: 35.445710974295665
    - type: nauc_recall_at_1000_diff1
      value: 41.20343859145517
    - type: nauc_recall_at_1000_max
      value: 61.44192065212247
    - type: nauc_recall_at_100_diff1
      value: 34.59097958116937
    - type: nauc_recall_at_100_max
      value: 41.235073100728385
    - type: nauc_recall_at_10_diff1
      value: 35.80526424971499
    - type: nauc_recall_at_10_max
      value: 35.01947143696681
    - type: nauc_recall_at_1_diff1
      value: 52.718043416663264
    - type: nauc_recall_at_1_max
      value: 36.05458738264693
    - type: nauc_recall_at_20_diff1
      value: 33.1496774921526
    - type: nauc_recall_at_20_max
      value: 35.42909868847532
    - type: nauc_recall_at_3_diff1
      value: 42.029271302810116
    - type: nauc_recall_at_3_max
      value: 32.53905541437273
    - type: nauc_recall_at_5_diff1
      value: 38.51927212842635
    - type: nauc_recall_at_5_max
      value: 34.3176010851305
    - type: ndcg_at_1
      value: 41.488
    - type: ndcg_at_10
      value: 51.144999999999996
    - type: ndcg_at_100
      value: 56.518
    - type: ndcg_at_1000
      value: 58.229
    - type: ndcg_at_20
      value: 53.543
    - type: ndcg_at_3
      value: 45.822
    - type: ndcg_at_5
      value: 48.278
    - type: precision_at_1
      value: 41.488
    - type: precision_at_10
      value: 9.943
    - type: precision_at_100
      value: 1.568
    - type: precision_at_1000
      value: 0.2
    - type: precision_at_20
      value: 5.937
    - type: precision_at_3
      value: 22.175
    - type: precision_at_5
      value: 16.166
    - type: recall_at_1
      value: 33.042
    - type: recall_at_10
      value: 63.307
    - type: recall_at_100
      value: 85.702
    - type: recall_at_1000
      value: 96.542
    - type: recall_at_20
      value: 72.031
    - type: recall_at_3
      value: 47.339999999999996
    - type: recall_at_5
      value: 54.605000000000004
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-english
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
    metrics:
    - type: map_at_1
      value: 25.799
    - type: map_at_10
      value: 35.142
    - type: map_at_100
      value: 36.352000000000004
    - type: map_at_1000
      value: 36.482
    - type: map_at_20
      value: 35.782000000000004
    - type: map_at_3
      value: 32.580999999999996
    - type: map_at_5
      value: 33.953
    - type: mrr_at_1
      value: 32.22929936305732
    - type: mrr_at_10
      value: 40.52792943079566
    - type: mrr_at_100
      value: 41.29468360785318
    - type: mrr_at_1000
      value: 41.34756133983024
    - type: mrr_at_20
      value: 40.977132571875295
    - type: mrr_at_3
      value: 38.535031847133745
    - type: mrr_at_5
      value: 39.60828025477706
    - type: nauc_map_at_1000_diff1
      value: 48.53888035316322
    - type: nauc_map_at_1000_max
      value: 38.885071022650244
    - type: nauc_map_at_100_diff1
      value: 48.57301602413753
    - type: nauc_map_at_100_max
      value: 38.84549426874644
    - type: nauc_map_at_10_diff1
      value: 48.77594440671453
    - type: nauc_map_at_10_max
      value: 38.18916807035125
    - type: nauc_map_at_1_diff1
      value: 53.7151009143777
    - type: nauc_map_at_1_max
      value: 35.67797250661703
    - type: nauc_map_at_20_diff1
      value: 48.741754265789446
    - type: nauc_map_at_20_max
      value: 38.68568816358472
    - type: nauc_map_at_3_diff1
      value: 49.80638050841809
    - type: nauc_map_at_3_max
      value: 37.62441778614408
    - type: nauc_map_at_5_diff1
      value: 49.144942257915616
    - type: nauc_map_at_5_max
      value: 38.02201040966136
    - type: nauc_mrr_at_1000_diff1
      value: 47.53755489603709
    - type: nauc_mrr_at_1000_max
      value: 39.8275293867551
    - type: nauc_mrr_at_100_diff1
      value: 47.52218111509617
    - type: nauc_mrr_at_100_max
      value: 39.81919277633853
    - type: nauc_mrr_at_10_diff1
      value: 47.580170749058325
    - type: nauc_mrr_at_10_max
      value: 39.80714471500064
    - type: nauc_mrr_at_1_diff1
      value: 53.16078794554316
    - type: nauc_mrr_at_1_max
      value: 40.85318206812723
    - type: nauc_mrr_at_20_diff1
      value: 47.51575634431614
    - type: nauc_mrr_at_20_max
      value: 39.88877176053388
    - type: nauc_mrr_at_3_diff1
      value: 48.57219468298523
    - type: nauc_mrr_at_3_max
      value: 39.99334565930618
    - type: nauc_mrr_at_5_diff1
      value: 47.85633780446893
    - type: nauc_mrr_at_5_max
      value: 39.62507950702868
    - type: nauc_ndcg_at_1000_diff1
      value: 45.36022329851297
    - type: nauc_ndcg_at_1000_max
      value: 39.61816922442756
    - type: nauc_ndcg_at_100_diff1
      value: 45.473763443711896
    - type: nauc_ndcg_at_100_max
      value: 39.528687290793656
    - type: nauc_ndcg_at_10_diff1
      value: 46.17836029609691
    - type: nauc_ndcg_at_10_max
      value: 38.80359542708498
    - type: nauc_ndcg_at_1_diff1
      value: 53.16078794554316
    - type: nauc_ndcg_at_1_max
      value: 40.85318206812723
    - type: nauc_ndcg_at_20_diff1
      value: 46.010684279423415
    - type: nauc_ndcg_at_20_max
      value: 39.65825927104732
    - type: nauc_ndcg_at_3_diff1
      value: 47.87796377448456
    - type: nauc_ndcg_at_3_max
      value: 39.5303651682398
    - type: nauc_ndcg_at_5_diff1
      value: 46.930158462575626
    - type: nauc_ndcg_at_5_max
      value: 38.89494195110121
    - type: nauc_precision_at_1000_diff1
      value: -10.55140312981742
    - type: nauc_precision_at_1000_max
      value: 9.29257821505048
    - type: nauc_precision_at_100_diff1
      value: -1.6477250608550713
    - type: nauc_precision_at_100_max
      value: 20.26704114790026
    - type: nauc_precision_at_10_diff1
      value: 19.231383164295735
    - type: nauc_precision_at_10_max
      value: 32.06949418715237
    - type: nauc_precision_at_1_diff1
      value: 53.16078794554316
    - type: nauc_precision_at_1_max
      value: 40.85318206812723
    - type: nauc_precision_at_20_diff1
      value: 12.343661815533256
    - type: nauc_precision_at_20_max
      value: 31.16859079177672
    - type: nauc_precision_at_3_diff1
      value: 33.98501406059714
    - type: nauc_precision_at_3_max
      value: 39.69786673453753
    - type: nauc_precision_at_5_diff1
      value: 27.048260073962886
    - type: nauc_precision_at_5_max
      value: 36.46400147355659
    - type: nauc_recall_at_1000_diff1
      value: 26.736945520548854
    - type: nauc_recall_at_1000_max
      value: 40.11949642000136
    - type: nauc_recall_at_100_diff1
      value: 32.618233624639096
    - type: nauc_recall_at_100_max
      value: 37.471570861127034
    - type: nauc_recall_at_10_diff1
      value: 38.24166212483116
    - type: nauc_recall_at_10_max
      value: 35.78917554877273
    - type: nauc_recall_at_1_diff1
      value: 53.7151009143777
    - type: nauc_recall_at_1_max
      value: 35.67797250661703
    - type: nauc_recall_at_20_diff1
      value: 37.40989768179516
    - type: nauc_recall_at_20_max
      value: 38.83116721748485
    - type: nauc_recall_at_3_diff1
      value: 43.87847612583987
    - type: nauc_recall_at_3_max
      value: 35.85792223399428
    - type: nauc_recall_at_5_diff1
      value: 40.86081574693399
    - type: nauc_recall_at_5_max
      value: 35.293665570406915
    - type: ndcg_at_1
      value: 32.229
    - type: ndcg_at_10
      value: 40.459
    - type: ndcg_at_100
      value: 45.226
    - type: ndcg_at_1000
      value: 47.528
    - type: ndcg_at_20
      value: 42.230000000000004
    - type: ndcg_at_3
      value: 36.623
    - type: ndcg_at_5
      value: 38.228
    - type: precision_at_1
      value: 32.229
    - type: precision_at_10
      value: 7.567
    - type: precision_at_100
      value: 1.282
    - type: precision_at_1000
      value: 0.178
    - type: precision_at_20
      value: 4.513
    - type: precision_at_3
      value: 17.813000000000002
    - type: precision_at_5
      value: 12.484
    - type: recall_at_1
      value: 25.799
    - type: recall_at_10
      value: 50.349999999999994
    - type: recall_at_100
      value: 70.563
    - type: recall_at_1000
      value: 85.531
    - type: recall_at_20
      value: 56.728
    - type: recall_at_3
      value: 38.853
    - type: recall_at_5
      value: 43.412
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-gaming
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
    metrics:
    - type: map_at_1
      value: 40.577999999999996
    - type: map_at_10
      value: 53.212
    - type: map_at_100
      value: 54.226
    - type: map_at_1000
      value: 54.282
    - type: map_at_20
      value: 53.859
    - type: map_at_3
      value: 49.580999999999996
    - type: map_at_5
      value: 51.687000000000005
    - type: mrr_at_1
      value: 46.33228840125392
    - type: mrr_at_10
      value: 56.53291536050165
    - type: mrr_at_100
      value: 57.16895265822186
    - type: mrr_at_1000
      value: 57.195436719992266
    - type: mrr_at_20
      value: 56.96343773126635
    - type: mrr_at_3
      value: 53.74085684430517
    - type: mrr_at_5
      value: 55.48380355276916
    - type: nauc_map_at_1000_diff1
      value: 51.598554728993896
    - type: nauc_map_at_1000_max
      value: 39.15548201170092
    - type: nauc_map_at_100_diff1
      value: 51.572169653620236
    - type: nauc_map_at_100_max
      value: 39.138122726267824
    - type: nauc_map_at_10_diff1
      value: 51.706299666815234
    - type: nauc_map_at_10_max
      value: 38.664500048817914
    - type: nauc_map_at_1_diff1
      value: 54.65549997502165
    - type: nauc_map_at_1_max
      value: 33.17776284922168
    - type: nauc_map_at_20_diff1
      value: 51.61722904567759
    - type: nauc_map_at_20_max
      value: 39.06733683117071
    - type: nauc_map_at_3_diff1
      value: 51.75319065227536
    - type: nauc_map_at_3_max
      value: 37.649161464056746
    - type: nauc_map_at_5_diff1
      value: 51.984911768670905
    - type: nauc_map_at_5_max
      value: 37.84708277261099
    - type: nauc_mrr_at_1000_diff1
      value: 51.29966271621572
    - type: nauc_mrr_at_1000_max
      value: 41.19269678217316
    - type: nauc_mrr_at_100_diff1
      value: 51.27647634492216
    - type: nauc_mrr_at_100_max
      value: 41.188075434891445
    - type: nauc_mrr_at_10_diff1
      value: 51.25933342020841
    - type: nauc_mrr_at_10_max
      value: 41.19583058928442
    - type: nauc_mrr_at_1_diff1
      value: 54.486057363901296
    - type: nauc_mrr_at_1_max
      value: 39.70923841169991
    - type: nauc_mrr_at_20_diff1
      value: 51.2663412823939
    - type: nauc_mrr_at_20_max
      value: 41.205935007286286
    - type: nauc_mrr_at_3_diff1
      value: 51.35186455722468
    - type: nauc_mrr_at_3_max
      value: 41.174712489505175
    - type: nauc_mrr_at_5_diff1
      value: 51.4936465099448
    - type: nauc_mrr_at_5_max
      value: 41.03149465128671
    - type: nauc_ndcg_at_1000_diff1
      value: 50.70988207357748
    - type: nauc_ndcg_at_1000_max
      value: 41.14232544679912
    - type: nauc_ndcg_at_100_diff1
      value: 50.042773827923156
    - type: nauc_ndcg_at_100_max
      value: 41.08896965715729
    - type: nauc_ndcg_at_10_diff1
      value: 50.175621571195414
    - type: nauc_ndcg_at_10_max
      value: 40.38913760035848
    - type: nauc_ndcg_at_1_diff1
      value: 54.486057363901296
    - type: nauc_ndcg_at_1_max
      value: 39.70923841169991
    - type: nauc_ndcg_at_20_diff1
      value: 50.06207172334041
    - type: nauc_ndcg_at_20_max
      value: 40.983813594676974
    - type: nauc_ndcg_at_3_diff1
      value: 50.46764333088301
    - type: nauc_ndcg_at_3_max
      value: 39.637132346570354
    - type: nauc_ndcg_at_5_diff1
      value: 50.85495861471141
    - type: nauc_ndcg_at_5_max
      value: 39.31722283055888
    - type: nauc_precision_at_1000_diff1
      value: -12.264915409866878
    - type: nauc_precision_at_1000_max
      value: 12.621466086946453
    - type: nauc_precision_at_100_diff1
      value: -8.574663908234603
    - type: nauc_precision_at_100_max
      value: 18.984908440696007
    - type: nauc_precision_at_10_diff1
      value: 12.487528289273806
    - type: nauc_precision_at_10_max
      value: 30.906956883213777
    - type: nauc_precision_at_1_diff1
      value: 54.486057363901296
    - type: nauc_precision_at_1_max
      value: 39.70923841169991
    - type: nauc_precision_at_20_diff1
      value: 3.220510277389277
    - type: nauc_precision_at_20_max
      value: 28.088902012149426
    - type: nauc_precision_at_3_diff1
      value: 31.914576103337044
    - type: nauc_precision_at_3_max
      value: 38.9802507491805
    - type: nauc_precision_at_5_diff1
      value: 24.4322963915954
    - type: nauc_precision_at_5_max
      value: 34.412198187901645
    - type: nauc_recall_at_1000_diff1
      value: 49.484820907450114
    - type: nauc_recall_at_1000_max
      value: 72.27913694185548
    - type: nauc_recall_at_100_diff1
      value: 34.33945500829377
    - type: nauc_recall_at_100_max
      value: 47.19595321254844
    - type: nauc_recall_at_10_diff1
      value: 42.51513987913315
    - type: nauc_recall_at_10_max
      value: 40.64530426633379
    - type: nauc_recall_at_1_diff1
      value: 54.65549997502165
    - type: nauc_recall_at_1_max
      value: 33.17776284922168
    - type: nauc_recall_at_20_diff1
      value: 39.931766770782424
    - type: nauc_recall_at_20_max
      value: 43.462236338673506
    - type: nauc_recall_at_3_diff1
      value: 47.01169666298634
    - type: nauc_recall_at_3_max
      value: 38.71661483121504
    - type: nauc_recall_at_5_diff1
      value: 46.636973604810436
    - type: nauc_recall_at_5_max
      value: 37.93651923057122
    - type: ndcg_at_1
      value: 46.332
    - type: ndcg_at_10
      value: 59.3
    - type: ndcg_at_100
      value: 63.144999999999996
    - type: ndcg_at_1000
      value: 64.196
    - type: ndcg_at_20
      value: 61.129999999999995
    - type: ndcg_at_3
      value: 53.20700000000001
    - type: ndcg_at_5
      value: 56.289
    - type: precision_at_1
      value: 46.332
    - type: precision_at_10
      value: 9.618
    - type: precision_at_100
      value: 1.2449999999999999
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_20
      value: 5.379
    - type: precision_at_3
      value: 23.636
    - type: precision_at_5
      value: 16.414
    - type: recall_at_1
      value: 40.577999999999996
    - type: recall_at_10
      value: 73.92800000000001
    - type: recall_at_100
      value: 90.335
    - type: recall_at_1000
      value: 97.7
    - type: recall_at_20
      value: 80.67
    - type: recall_at_3
      value: 57.777
    - type: recall_at_5
      value: 65.264
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-gis
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: 5003b3064772da1887988e05400cf3806fe491f2
    metrics:
    - type: map_at_1
      value: 23.923
    - type: map_at_10
      value: 31.826999999999998
    - type: map_at_100
      value: 32.969
    - type: map_at_1000
      value: 33.056000000000004
    - type: map_at_20
      value: 32.531
    - type: map_at_3
      value: 28.987000000000002
    - type: map_at_5
      value: 30.514000000000003
    - type: mrr_at_1
      value: 25.98870056497175
    - type: mrr_at_10
      value: 34.06546498071922
    - type: mrr_at_100
      value: 35.09126424165195
    - type: mrr_at_1000
      value: 35.15930448144987
    - type: mrr_at_20
      value: 34.728786599018015
    - type: mrr_at_3
      value: 31.525423728813568
    - type: mrr_at_5
      value: 32.926553672316395
    - type: nauc_map_at_1000_diff1
      value: 40.53568978877159
    - type: nauc_map_at_1000_max
      value: 24.017152390712713
    - type: nauc_map_at_100_diff1
      value: 40.465126251405216
    - type: nauc_map_at_100_max
      value: 24.00219845459832
    - type: nauc_map_at_10_diff1
      value: 40.89662927517162
    - type: nauc_map_at_10_max
      value: 23.884797645661507
    - type: nauc_map_at_1_diff1
      value: 47.66862456961046
    - type: nauc_map_at_1_max
      value: 23.178785033806612
    - type: nauc_map_at_20_diff1
      value: 40.61327977862771
    - type: nauc_map_at_20_max
      value: 23.968685123247937
    - type: nauc_map_at_3_diff1
      value: 42.158035916801964
    - type: nauc_map_at_3_max
      value: 23.73190519661713
    - type: nauc_map_at_5_diff1
      value: 41.19982202919823
    - type: nauc_map_at_5_max
      value: 24.02821512187476
    - type: nauc_mrr_at_1000_diff1
      value: 40.00607387909823
    - type: nauc_mrr_at_1000_max
      value: 25.3100454072437
    - type: nauc_mrr_at_100_diff1
      value: 39.944554243015766
    - type: nauc_mrr_at_100_max
      value: 25.30441358891755
    - type: nauc_mrr_at_10_diff1
      value: 40.35108318848009
    - type: nauc_mrr_at_10_max
      value: 25.266437318063474
    - type: nauc_mrr_at_1_diff1
      value: 46.86905124510021
    - type: nauc_mrr_at_1_max
      value: 25.798435739081206
    - type: nauc_mrr_at_20_diff1
      value: 40.005155401228144
    - type: nauc_mrr_at_20_max
      value: 25.30049770260261
    - type: nauc_mrr_at_3_diff1
      value: 41.70808830620455
    - type: nauc_mrr_at_3_max
      value: 25.581473945950638
    - type: nauc_mrr_at_5_diff1
      value: 40.67811332232744
    - type: nauc_mrr_at_5_max
      value: 25.59583031517064
    - type: nauc_ndcg_at_1000_diff1
      value: 37.789315958522366
    - type: nauc_ndcg_at_1000_max
      value: 24.732278855527596
    - type: nauc_ndcg_at_100_diff1
      value: 36.11005015150818
    - type: nauc_ndcg_at_100_max
      value: 24.481118474622875
    - type: nauc_ndcg_at_10_diff1
      value: 38.05600817464286
    - type: nauc_ndcg_at_10_max
      value: 23.843193633623606
    - type: nauc_ndcg_at_1_diff1
      value: 46.86905124510021
    - type: nauc_ndcg_at_1_max
      value: 25.798435739081206
    - type: nauc_ndcg_at_20_diff1
      value: 36.89241258073012
    - type: nauc_ndcg_at_20_max
      value: 24.00494460363686
    - type: nauc_ndcg_at_3_diff1
      value: 40.365155713927905
    - type: nauc_ndcg_at_3_max
      value: 24.147776638952134
    - type: nauc_ndcg_at_5_diff1
      value: 38.75811774555819
    - type: nauc_ndcg_at_5_max
      value: 24.34507156699549
    - type: nauc_precision_at_1000_diff1
      value: -0.43779992271010504
    - type: nauc_precision_at_1000_max
      value: 18.014562731389443
    - type: nauc_precision_at_100_diff1
      value: 4.781866779340611
    - type: nauc_precision_at_100_max
      value: 24.101124500402392
    - type: nauc_precision_at_10_diff1
      value: 26.227299845047753
    - type: nauc_precision_at_10_max
      value: 25.46662356995603
    - type: nauc_precision_at_1_diff1
      value: 46.86905124510021
    - type: nauc_precision_at_1_max
      value: 25.798435739081206
    - type: nauc_precision_at_20_diff1
      value: 19.293563777255283
    - type: nauc_precision_at_20_max
      value: 25.659177432920526
    - type: nauc_precision_at_3_diff1
      value: 34.4615177098042
    - type: nauc_precision_at_3_max
      value: 26.43595627373827
    - type: nauc_precision_at_5_diff1
      value: 29.76719132298527
    - type: nauc_precision_at_5_max
      value: 27.04359051786532
    - type: nauc_recall_at_1000_diff1
      value: 23.898720213374496
    - type: nauc_recall_at_1000_max
      value: 30.495718100359383
    - type: nauc_recall_at_100_diff1
      value: 14.199951069499797
    - type: nauc_recall_at_100_max
      value: 24.192596324819863
    - type: nauc_recall_at_10_diff1
      value: 29.1494599904968
    - type: nauc_recall_at_10_max
      value: 21.218550813646498
    - type: nauc_recall_at_1_diff1
      value: 47.66862456961046
    - type: nauc_recall_at_1_max
      value: 23.178785033806612
    - type: nauc_recall_at_20_diff1
      value: 23.343557821312057
    - type: nauc_recall_at_20_max
      value: 21.087644815552554
    - type: nauc_recall_at_3_diff1
      value: 35.61572753794292
    - type: nauc_recall_at_3_max
      value: 22.48203544476738
    - type: nauc_recall_at_5_diff1
      value: 31.3735878031144
    - type: nauc_recall_at_5_max
      value: 22.780362537734227
    - type: ndcg_at_1
      value: 25.989
    - type: ndcg_at_10
      value: 36.664
    - type: ndcg_at_100
      value: 42.197
    - type: ndcg_at_1000
      value: 44.452999999999996
    - type: ndcg_at_20
      value: 39.162
    - type: ndcg_at_3
      value: 31.286
    - type: ndcg_at_5
      value: 33.814
    - type: precision_at_1
      value: 25.989
    - type: precision_at_10
      value: 5.718
    - type: precision_at_100
      value: 0.89
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_20
      value: 3.4290000000000003
    - type: precision_at_3
      value: 13.22
    - type: precision_at_5
      value: 9.401
    - type: recall_at_1
      value: 23.923
    - type: recall_at_10
      value: 49.441
    - type: recall_at_100
      value: 74.726
    - type: recall_at_1000
      value: 91.701
    - type: recall_at_20
      value: 59.046
    - type: recall_at_3
      value: 35.120000000000005
    - type: recall_at_5
      value: 41.105999999999995
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-mathematica
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
    metrics:
    - type: map_at_1
      value: 14.971
    - type: map_at_10
      value: 21.733
    - type: map_at_100
      value: 22.986
    - type: map_at_1000
      value: 23.101
    - type: map_at_20
      value: 22.354
    - type: map_at_3
      value: 18.6
    - type: map_at_5
      value: 20.282
    - type: mrr_at_1
      value: 18.28358208955224
    - type: mrr_at_10
      value: 25.521499644633966
    - type: mrr_at_100
      value: 26.56337467191487
    - type: mrr_at_1000
      value: 26.6340022787211
    - type: mrr_at_20
      value: 26.087154278521353
    - type: mrr_at_3
      value: 22.429519071310118
    - type: mrr_at_5
      value: 24.06509121061359
    - type: nauc_map_at_1000_diff1
      value: 24.25147571236624
    - type: nauc_map_at_1000_max
      value: 22.768079776516746
    - type: nauc_map_at_100_diff1
      value: 24.25026133742646
    - type: nauc_map_at_100_max
      value: 22.733915881805615
    - type: nauc_map_at_10_diff1
      value: 24.653400843024155
    - type: nauc_map_at_10_max
      value: 23.002528658758354
    - type: nauc_map_at_1_diff1
      value: 28.369403071456073
    - type: nauc_map_at_1_max
      value: 24.353121678819484
    - type: nauc_map_at_20_diff1
      value: 24.2810955115316
    - type: nauc_map_at_20_max
      value: 22.56085848928233
    - type: nauc_map_at_3_diff1
      value: 26.404468625977124
    - type: nauc_map_at_3_max
      value: 22.75636429110974
    - type: nauc_map_at_5_diff1
      value: 24.478028307615297
    - type: nauc_map_at_5_max
      value: 23.06675290764163
    - type: nauc_mrr_at_1000_diff1
      value: 25.17718018617494
    - type: nauc_mrr_at_1000_max
      value: 23.766544519882718
    - type: nauc_mrr_at_100_diff1
      value: 25.17161074247674
    - type: nauc_mrr_at_100_max
      value: 23.749609869133465
    - type: nauc_mrr_at_10_diff1
      value: 25.499497632708533
    - type: nauc_mrr_at_10_max
      value: 23.947414255390825
    - type: nauc_mrr_at_1_diff1
      value: 29.693800058620468
    - type: nauc_mrr_at_1_max
      value: 25.209233166626444
    - type: nauc_mrr_at_20_diff1
      value: 25.220453375569868
    - type: nauc_mrr_at_20_max
      value: 23.651070356457634
    - type: nauc_mrr_at_3_diff1
      value: 26.914681944004187
    - type: nauc_mrr_at_3_max
      value: 24.02788958604021
    - type: nauc_mrr_at_5_diff1
      value: 25.066709251413872
    - type: nauc_mrr_at_5_max
      value: 23.829128622178818
    - type: nauc_ndcg_at_1000_diff1
      value: 21.518084429129047
    - type: nauc_ndcg_at_1000_max
      value: 22.94654293593645
    - type: nauc_ndcg_at_100_diff1
      value: 21.394864699409837
    - type: nauc_ndcg_at_100_max
      value: 22.245197430786725
    - type: nauc_ndcg_at_10_diff1
      value: 23.088959622104102
    - type: nauc_ndcg_at_10_max
      value: 22.747264555679106
    - type: nauc_ndcg_at_1_diff1
      value: 29.693800058620468
    - type: nauc_ndcg_at_1_max
      value: 25.209233166626444
    - type: nauc_ndcg_at_20_diff1
      value: 21.81438142024938
    - type: nauc_ndcg_at_20_max
      value: 21.378206553759235
    - type: nauc_ndcg_at_3_diff1
      value: 26.22901493401714
    - type: nauc_ndcg_at_3_max
      value: 22.707998579806507
    - type: nauc_ndcg_at_5_diff1
      value: 22.68045655876842
    - type: nauc_ndcg_at_5_max
      value: 22.7647451392375
    - type: nauc_precision_at_1000_diff1
      value: -3.1430311570325475
    - type: nauc_precision_at_1000_max
      value: 5.545460812686058
    - type: nauc_precision_at_100_diff1
      value: 2.1386034643858167
    - type: nauc_precision_at_100_max
      value: 10.097473871112502
    - type: nauc_precision_at_10_diff1
      value: 17.18530782987866
    - type: nauc_precision_at_10_max
      value: 19.943966966733125
    - type: nauc_precision_at_1_diff1
      value: 29.693800058620468
    - type: nauc_precision_at_1_max
      value: 25.209233166626444
    - type: nauc_precision_at_20_diff1
      value: 11.86012437117262
    - type: nauc_precision_at_20_max
      value: 14.950950398417962
    - type: nauc_precision_at_3_diff1
      value: 24.362152407838188
    - type: nauc_precision_at_3_max
      value: 20.97253622362092
    - type: nauc_precision_at_5_diff1
      value: 16.924558194319285
    - type: nauc_precision_at_5_max
      value: 21.158164075975677
    - type: nauc_recall_at_1000_diff1
      value: 0.8507872273057012
    - type: nauc_recall_at_1000_max
      value: 27.62961752670282
    - type: nauc_recall_at_100_diff1
      value: 9.041767797784955
    - type: nauc_recall_at_100_max
      value: 18.747226189196343
    - type: nauc_recall_at_10_diff1
      value: 17.415788768054586
    - type: nauc_recall_at_10_max
      value: 20.120616403763233
    - type: nauc_recall_at_1_diff1
      value: 28.369403071456073
    - type: nauc_recall_at_1_max
      value: 24.353121678819484
    - type: nauc_recall_at_20_diff1
      value: 12.784706856811361
    - type: nauc_recall_at_20_max
      value: 15.376595791636444
    - type: nauc_recall_at_3_diff1
      value: 23.50138610578596
    - type: nauc_recall_at_3_max
      value: 20.180363639888935
    - type: nauc_recall_at_5_diff1
      value: 16.765137232464685
    - type: nauc_recall_at_5_max
      value: 20.04595551697802
    - type: ndcg_at_1
      value: 18.284
    - type: ndcg_at_10
      value: 26.849
    - type: ndcg_at_100
      value: 33.171
    - type: ndcg_at_1000
      value: 35.882
    - type: ndcg_at_20
      value: 29.009
    - type: ndcg_at_3
      value: 20.828
    - type: ndcg_at_5
      value: 23.564
    - type: precision_at_1
      value: 18.284
    - type: precision_at_10
      value: 5.236
    - type: precision_at_100
      value: 0.988
    - type: precision_at_1000
      value: 0.135
    - type: precision_at_20
      value: 3.2399999999999998
    - type: precision_at_3
      value: 9.908999999999999
    - type: precision_at_5
      value: 7.736
    - type: recall_at_1
      value: 14.971
    - type: recall_at_10
      value: 38.944
    - type: recall_at_100
      value: 67.02900000000001
    - type: recall_at_1000
      value: 86.17
    - type: recall_at_20
      value: 46.686
    - type: recall_at_3
      value: 22.904
    - type: recall_at_5
      value: 29.503
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-physics
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
    metrics:
    - type: map_at_1
      value: 26.392
    - type: map_at_10
      value: 36.754
    - type: map_at_100
      value: 38.073
    - type: map_at_1000
      value: 38.194
    - type: map_at_20
      value: 37.484
    - type: map_at_3
      value: 33.355000000000004
    - type: map_at_5
      value: 35.262
    - type: mrr_at_1
      value: 33.301251203079886
    - type: mrr_at_10
      value: 42.665604900927306
    - type: mrr_at_100
      value: 43.484677247616176
    - type: mrr_at_1000
      value: 43.54184906127189
    - type: mrr_at_20
      value: 43.15923651973285
    - type: mrr_at_3
      value: 39.89412897016359
    - type: mrr_at_5
      value: 41.50144369586136
    - type: nauc_map_at_1000_diff1
      value: 45.864458981619094
    - type: nauc_map_at_1000_max
      value: 32.118941905810836
    - type: nauc_map_at_100_diff1
      value: 45.850902650401515
    - type: nauc_map_at_100_max
      value: 32.06314733345846
    - type: nauc_map_at_10_diff1
      value: 45.83156768369814
    - type: nauc_map_at_10_max
      value: 31.628565525768902
    - type: nauc_map_at_1_diff1
      value: 52.186731161714064
    - type: nauc_map_at_1_max
      value: 31.294454235319886
    - type: nauc_map_at_20_diff1
      value: 45.906750616328516
    - type: nauc_map_at_20_max
      value: 31.90200947801426
    - type: nauc_map_at_3_diff1
      value: 46.56102602531871
    - type: nauc_map_at_3_max
      value: 31.003984505733552
    - type: nauc_map_at_5_diff1
      value: 46.28126917940926
    - type: nauc_map_at_5_max
      value: 31.873045197665036
    - type: nauc_mrr_at_1000_diff1
      value: 46.39499265153352
    - type: nauc_mrr_at_1000_max
      value: 35.430647378018804
    - type: nauc_mrr_at_100_diff1
      value: 46.365007651920976
    - type: nauc_mrr_at_100_max
      value: 35.40605673373685
    - type: nauc_mrr_at_10_diff1
      value: 46.30336976338955
    - type: nauc_mrr_at_10_max
      value: 35.2890270181767
    - type: nauc_mrr_at_1_diff1
      value: 51.70112831336965
    - type: nauc_mrr_at_1_max
      value: 37.486019074857545
    - type: nauc_mrr_at_20_diff1
      value: 46.405348743745506
    - type: nauc_mrr_at_20_max
      value: 35.3532252404196
    - type: nauc_mrr_at_3_diff1
      value: 46.67222098559337
    - type: nauc_mrr_at_3_max
      value: 35.138714207684394
    - type: nauc_mrr_at_5_diff1
      value: 46.358893332958424
    - type: nauc_mrr_at_5_max
      value: 35.337962595981665
    - type: nauc_ndcg_at_1000_diff1
      value: 44.20225010243809
    - type: nauc_ndcg_at_1000_max
      value: 33.85142313176272
    - type: nauc_ndcg_at_100_diff1
      value: 43.64430267495509
    - type: nauc_ndcg_at_100_max
      value: 32.831976316723804
    - type: nauc_ndcg_at_10_diff1
      value: 43.63837088039455
    - type: nauc_ndcg_at_10_max
      value: 31.528806142031762
    - type: nauc_ndcg_at_1_diff1
      value: 51.70112831336965
    - type: nauc_ndcg_at_1_max
      value: 37.486019074857545
    - type: nauc_ndcg_at_20_diff1
      value: 44.04376192877168
    - type: nauc_ndcg_at_20_max
      value: 32.11101049110647
    - type: nauc_ndcg_at_3_diff1
      value: 44.78629324861377
    - type: nauc_ndcg_at_3_max
      value: 32.0765208889963
    - type: nauc_ndcg_at_5_diff1
      value: 44.49661502805839
    - type: nauc_ndcg_at_5_max
      value: 32.4935834459969
    - type: nauc_precision_at_1000_diff1
      value: -10.665808399449734
    - type: nauc_precision_at_1000_max
      value: 9.508118742960512
    - type: nauc_precision_at_100_diff1
      value: 0.9965788997167621
    - type: nauc_precision_at_100_max
      value: 17.825618552243437
    - type: nauc_precision_at_10_diff1
      value: 17.877056244565143
    - type: nauc_precision_at_10_max
      value: 26.670711200894644
    - type: nauc_precision_at_1_diff1
      value: 51.70112831336965
    - type: nauc_precision_at_1_max
      value: 37.486019074857545
    - type: nauc_precision_at_20_diff1
      value: 13.469130238466779
    - type: nauc_precision_at_20_max
      value: 25.14582568014069
    - type: nauc_precision_at_3_diff1
      value: 32.617136541117944
    - type: nauc_precision_at_3_max
      value: 32.19845850876858
    - type: nauc_precision_at_5_diff1
      value: 27.089481622940916
    - type: nauc_precision_at_5_max
      value: 32.04685190524753
    - type: nauc_recall_at_1000_diff1
      value: 25.345000533118366
    - type: nauc_recall_at_1000_max
      value: 45.335600118089594
    - type: nauc_recall_at_100_diff1
      value: 27.97181257050334
    - type: nauc_recall_at_100_max
      value: 26.42929240047483
    - type: nauc_recall_at_10_diff1
      value: 33.5410320871382
    - type: nauc_recall_at_10_max
      value: 25.047564064709
    - type: nauc_recall_at_1_diff1
      value: 52.186731161714064
    - type: nauc_recall_at_1_max
      value: 31.294454235319886
    - type: nauc_recall_at_20_diff1
      value: 34.60094954885383
    - type: nauc_recall_at_20_max
      value: 25.991385488198215
    - type: nauc_recall_at_3_diff1
      value: 38.785937018332525
    - type: nauc_recall_at_3_max
      value: 26.48398470584179
    - type: nauc_recall_at_5_diff1
      value: 36.86067904440702
    - type: nauc_recall_at_5_max
      value: 27.740739348375882
    - type: ndcg_at_1
      value: 33.300999999999995
    - type: ndcg_at_10
      value: 42.976
    - type: ndcg_at_100
      value: 48.351
    - type: ndcg_at_1000
      value: 50.67
    - type: ndcg_at_20
      value: 45.09
    - type: ndcg_at_3
      value: 37.628
    - type: ndcg_at_5
      value: 40.196
    - type: precision_at_1
      value: 33.300999999999995
    - type: precision_at_10
      value: 8.017000000000001
    - type: precision_at_100
      value: 1.274
    - type: precision_at_1000
      value: 0.167
    - type: precision_at_20
      value: 4.74
    - type: precision_at_3
      value: 18.029999999999998
    - type: precision_at_5
      value: 13.07
    - type: recall_at_1
      value: 26.392
    - type: recall_at_10
      value: 55.827000000000005
    - type: recall_at_100
      value: 78.171
    - type: recall_at_1000
      value: 93.60000000000001
    - type: recall_at_20
      value: 63.172
    - type: recall_at_3
      value: 40.46
    - type: recall_at_5
      value: 47.260000000000005
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-programmers
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
    metrics:
    - type: map_at_1
      value: 24.846
    - type: map_at_10
      value: 35.475
    - type: map_at_100
      value: 36.76
    - type: map_at_1000
      value: 36.874
    - type: map_at_20
      value: 36.144
    - type: map_at_3
      value: 31.995
    - type: map_at_5
      value: 34.152
    - type: mrr_at_1
      value: 30.59360730593607
    - type: mrr_at_10
      value: 40.23048488801914
    - type: mrr_at_100
      value: 41.133760645262264
    - type: mrr_at_1000
      value: 41.18151460856815
    - type: mrr_at_20
      value: 40.742005593886496
    - type: mrr_at_3
      value: 37.366818873668194
    - type: mrr_at_5
      value: 39.17617960426178
    - type: nauc_map_at_1000_diff1
      value: 42.80424009699214
    - type: nauc_map_at_1000_max
      value: 33.725293061149195
    - type: nauc_map_at_100_diff1
      value: 42.776847198709866
    - type: nauc_map_at_100_max
      value: 33.70505189600135
    - type: nauc_map_at_10_diff1
      value: 42.790379082991535
    - type: nauc_map_at_10_max
      value: 33.3320315752561
    - type: nauc_map_at_1_diff1
      value: 47.246062086068235
    - type: nauc_map_at_1_max
      value: 28.359771168971115
    - type: nauc_map_at_20_diff1
      value: 42.60750623653338
    - type: nauc_map_at_20_max
      value: 33.43767341363528
    - type: nauc_map_at_3_diff1
      value: 43.70825195522167
    - type: nauc_map_at_3_max
      value: 31.726835129782273
    - type: nauc_map_at_5_diff1
      value: 43.274775396782935
    - type: nauc_map_at_5_max
      value: 32.70895131341521
    - type: nauc_mrr_at_1000_diff1
      value: 42.99721876676844
    - type: nauc_mrr_at_1000_max
      value: 34.01237872571581
    - type: nauc_mrr_at_100_diff1
      value: 42.98874587454992
    - type: nauc_mrr_at_100_max
      value: 34.017143533550254
    - type: nauc_mrr_at_10_diff1
      value: 42.895695388416605
    - type: nauc_mrr_at_10_max
      value: 34.03560692108162
    - type: nauc_mrr_at_1_diff1
      value: 47.43746467307071
    - type: nauc_mrr_at_1_max
      value: 33.090216128367736
    - type: nauc_mrr_at_20_diff1
      value: 42.82350948241532
    - type: nauc_mrr_at_20_max
      value: 33.931126556842855
    - type: nauc_mrr_at_3_diff1
      value: 43.42025274432862
    - type: nauc_mrr_at_3_max
      value: 33.95388307382994
    - type: nauc_mrr_at_5_diff1
      value: 43.30110911279515
    - type: nauc_mrr_at_5_max
      value: 34.10057032518187
    - type: nauc_ndcg_at_1000_diff1
      value: 41.368277694849716
    - type: nauc_ndcg_at_1000_max
      value: 35.43335475120229
    - type: nauc_ndcg_at_100_diff1
      value: 41.041233441414285
    - type: nauc_ndcg_at_100_max
      value: 35.316555805430966
    - type: nauc_ndcg_at_10_diff1
      value: 40.721559421808315
    - type: nauc_ndcg_at_10_max
      value: 34.18965204589481
    - type: nauc_ndcg_at_1_diff1
      value: 47.43746467307071
    - type: nauc_ndcg_at_1_max
      value: 33.090216128367736
    - type: nauc_ndcg_at_20_diff1
      value: 40.18939317714461
    - type: nauc_ndcg_at_20_max
      value: 34.07353152343469
    - type: nauc_ndcg_at_3_diff1
      value: 42.20980264549485
    - type: nauc_ndcg_at_3_max
      value: 33.65119409518058
    - type: nauc_ndcg_at_5_diff1
      value: 41.74753311666698
    - type: nauc_ndcg_at_5_max
      value: 33.9538812368522
    - type: nauc_precision_at_1000_diff1
      value: -5.072070114071463
    - type: nauc_precision_at_1000_max
      value: 7.00735816140548
    - type: nauc_precision_at_100_diff1
      value: 5.76371809901476
    - type: nauc_precision_at_100_max
      value: 22.525109443008358
    - type: nauc_precision_at_10_diff1
      value: 19.75308373783922
    - type: nauc_precision_at_10_max
      value: 35.86370451223885
    - type: nauc_precision_at_1_diff1
      value: 47.43746467307071
    - type: nauc_precision_at_1_max
      value: 33.090216128367736
    - type: nauc_precision_at_20_diff1
      value: 13.327022725323756
    - type: nauc_precision_at_20_max
      value: 31.315919177108505
    - type: nauc_precision_at_3_diff1
      value: 33.236985143510076
    - type: nauc_precision_at_3_max
      value: 38.06028914966596
    - type: nauc_precision_at_5_diff1
      value: 27.697118951302773
    - type: nauc_precision_at_5_max
      value: 38.08338575982885
    - type: nauc_recall_at_1000_diff1
      value: 24.5554164444929
    - type: nauc_recall_at_1000_max
      value: 57.016793794468946
    - type: nauc_recall_at_100_diff1
      value: 28.85523670973284
    - type: nauc_recall_at_100_max
      value: 39.93212234361002
    - type: nauc_recall_at_10_diff1
      value: 31.806810855656558
    - type: nauc_recall_at_10_max
      value: 32.918322810428776
    - type: nauc_recall_at_1_diff1
      value: 47.246062086068235
    - type: nauc_recall_at_1_max
      value: 28.359771168971115
    - type: nauc_recall_at_20_diff1
      value: 29.01918120602967
    - type: nauc_recall_at_20_max
      value: 31.807933098443048
    - type: nauc_recall_at_3_diff1
      value: 36.94973707115803
    - type: nauc_recall_at_3_max
      value: 30.571001616703402
    - type: nauc_recall_at_5_diff1
      value: 35.045284393587714
    - type: nauc_recall_at_5_max
      value: 31.969117652354782
    - type: ndcg_at_1
      value: 30.593999999999998
    - type: ndcg_at_10
      value: 41.494
    - type: ndcg_at_100
      value: 47.185
    - type: ndcg_at_1000
      value: 49.347
    - type: ndcg_at_20
      value: 43.577
    - type: ndcg_at_3
      value: 35.862
    - type: ndcg_at_5
      value: 38.867000000000004
    - type: precision_at_1
      value: 30.593999999999998
    - type: precision_at_10
      value: 7.683
    - type: precision_at_100
      value: 1.225
    - type: precision_at_1000
      value: 0.16
    - type: precision_at_20
      value: 4.503
    - type: precision_at_3
      value: 17.199
    - type: precision_at_5
      value: 12.626000000000001
    - type: recall_at_1
      value: 24.846
    - type: recall_at_10
      value: 54.716
    - type: recall_at_100
      value: 79.081
    - type: recall_at_1000
      value: 93.245
    - type: recall_at_20
      value: 62.092999999999996
    - type: recall_at_3
      value: 39.521
    - type: recall_at_5
      value: 47.28
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-stats
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
    metrics:
    - type: map_at_1
      value: 22.136
    - type: map_at_10
      value: 29.096
    - type: map_at_100
      value: 29.987000000000002
    - type: map_at_1000
      value: 30.080000000000002
    - type: map_at_20
      value: 29.587999999999997
    - type: map_at_3
      value: 26.624
    - type: map_at_5
      value: 28.153
    - type: mrr_at_1
      value: 25.153374233128833
    - type: mrr_at_10
      value: 31.839943032427687
    - type: mrr_at_100
      value: 32.60360779338875
    - type: mrr_at_1000
      value: 32.6688197586382
    - type: mrr_at_20
      value: 32.25160220042008
    - type: mrr_at_3
      value: 29.601226993865037
    - type: mrr_at_5
      value: 30.943251533742334
    - type: nauc_map_at_1000_diff1
      value: 52.455633563736285
    - type: nauc_map_at_1000_max
      value: 37.60755242814028
    - type: nauc_map_at_100_diff1
      value: 52.45214127732582
    - type: nauc_map_at_100_max
      value: 37.59795326016924
    - type: nauc_map_at_10_diff1
      value: 52.24312132948332
    - type: nauc_map_at_10_max
      value: 37.11045415677249
    - type: nauc_map_at_1_diff1
      value: 56.98636684380831
    - type: nauc_map_at_1_max
      value: 34.98161163952515
    - type: nauc_map_at_20_diff1
      value: 52.36199775771774
    - type: nauc_map_at_20_max
      value: 37.27645637818285
    - type: nauc_map_at_3_diff1
      value: 53.83141960606124
    - type: nauc_map_at_3_max
      value: 37.229970040701346
    - type: nauc_map_at_5_diff1
      value: 53.15168000537631
    - type: nauc_map_at_5_max
      value: 37.539566125117005
    - type: nauc_mrr_at_1000_diff1
      value: 53.74688871125647
    - type: nauc_mrr_at_1000_max
      value: 41.26635263696367
    - type: nauc_mrr_at_100_diff1
      value: 53.740853962619575
    - type: nauc_mrr_at_100_max
      value: 41.27609969941193
    - type: nauc_mrr_at_10_diff1
      value: 53.780412829062364
    - type: nauc_mrr_at_10_max
      value: 41.23227433633308
    - type: nauc_mrr_at_1_diff1
      value: 58.25420348925137
    - type: nauc_mrr_at_1_max
      value: 40.707310022974156
    - type: nauc_mrr_at_20_diff1
      value: 53.64611118249694
    - type: nauc_mrr_at_20_max
      value: 41.04316014976299
    - type: nauc_mrr_at_3_diff1
      value: 54.73369595690322
    - type: nauc_mrr_at_3_max
      value: 41.5536466430315
    - type: nauc_mrr_at_5_diff1
      value: 54.60882845484611
    - type: nauc_mrr_at_5_max
      value: 41.844921732375276
    - type: nauc_ndcg_at_1000_diff1
      value: 50.74395212773536
    - type: nauc_ndcg_at_1000_max
      value: 39.06047216781442
    - type: nauc_ndcg_at_100_diff1
      value: 50.43711073076296
    - type: nauc_ndcg_at_100_max
      value: 39.1366325247916
    - type: nauc_ndcg_at_10_diff1
      value: 49.95511388688238
    - type: nauc_ndcg_at_10_max
      value: 37.36429944040018
    - type: nauc_ndcg_at_1_diff1
      value: 58.25420348925137
    - type: nauc_ndcg_at_1_max
      value: 40.707310022974156
    - type: nauc_ndcg_at_20_diff1
      value: 49.95606208222694
    - type: nauc_ndcg_at_20_max
      value: 37.297667173989424
    - type: nauc_ndcg_at_3_diff1
      value: 52.889515948632535
    - type: nauc_ndcg_at_3_max
      value: 39.11848555749881
    - type: nauc_ndcg_at_5_diff1
      value: 51.941920893459724
    - type: nauc_ndcg_at_5_max
      value: 38.79386401598912
    - type: nauc_precision_at_1000_diff1
      value: 15.659337654254507
    - type: nauc_precision_at_1000_max
      value: 28.857709990794667
    - type: nauc_precision_at_100_diff1
      value: 30.04624728253852
    - type: nauc_precision_at_100_max
      value: 42.98624472925551
    - type: nauc_precision_at_10_diff1
      value: 37.76954077186731
    - type: nauc_precision_at_10_max
      value: 41.087735036565995
    - type: nauc_precision_at_1_diff1
      value: 58.25420348925137
    - type: nauc_precision_at_1_max
      value: 40.707310022974156
    - type: nauc_precision_at_20_diff1
      value: 36.60760711819881
    - type: nauc_precision_at_20_max
      value: 41.9758712053368
    - type: nauc_precision_at_3_diff1
      value: 49.18539873142893
    - type: nauc_precision_at_3_max
      value: 45.84808718647459
    - type: nauc_precision_at_5_diff1
      value: 44.14556369952622
    - type: nauc_precision_at_5_max
      value: 45.133909279581246
    - type: nauc_recall_at_1000_diff1
      value: 36.16141258053102
    - type: nauc_recall_at_1000_max
      value: 37.25522806032212
    - type: nauc_recall_at_100_diff1
      value: 39.01185923471967
    - type: nauc_recall_at_100_max
      value: 38.637345088019984
    - type: nauc_recall_at_10_diff1
      value: 40.17794898514513
    - type: nauc_recall_at_10_max
      value: 32.118702708964605
    - type: nauc_recall_at_1_diff1
      value: 56.98636684380831
    - type: nauc_recall_at_1_max
      value: 34.98161163952515
    - type: nauc_recall_at_20_diff1
      value: 39.054641759787934
    - type: nauc_recall_at_20_max
      value: 30.368589073820928
    - type: nauc_recall_at_3_diff1
      value: 48.02597451526117
    - type: nauc_recall_at_3_max
      value: 35.92366556203388
    - type: nauc_recall_at_5_diff1
      value: 46.27418708067057
    - type: nauc_recall_at_5_max
      value: 36.27284558761095
    - type: ndcg_at_1
      value: 25.153
    - type: ndcg_at_10
      value: 33.372
    - type: ndcg_at_100
      value: 37.818000000000005
    - type: ndcg_at_1000
      value: 40.27
    - type: ndcg_at_20
      value: 35.071000000000005
    - type: ndcg_at_3
      value: 28.833
    - type: ndcg_at_5
      value: 31.241000000000003
    - type: precision_at_1
      value: 25.153
    - type: precision_at_10
      value: 5.367999999999999
    - type: precision_at_100
      value: 0.819
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: precision_at_20
      value: 3.113
    - type: precision_at_3
      value: 12.423
    - type: precision_at_5
      value: 9.049
    - type: recall_at_1
      value: 22.136
    - type: recall_at_10
      value: 43.952999999999996
    - type: recall_at_100
      value: 64.328
    - type: recall_at_1000
      value: 82.643
    - type: recall_at_20
      value: 50.409000000000006
    - type: recall_at_3
      value: 31.517
    - type: recall_at_5
      value: 37.468
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-tex
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: 46989137a86843e03a6195de44b09deda022eec7
    metrics:
    - type: map_at_1
      value: 14.882000000000001
    - type: map_at_10
      value: 21.733
    - type: map_at_100
      value: 22.847
    - type: map_at_1000
      value: 22.978
    - type: map_at_20
      value: 22.299
    - type: map_at_3
      value: 19.576
    - type: map_at_5
      value: 20.71
    - type: mrr_at_1
      value: 18.58224363386098
    - type: mrr_at_10
      value: 25.510055823201093
    - type: mrr_at_100
      value: 26.4274952364281
    - type: mrr_at_1000
      value: 26.515127162140832
    - type: mrr_at_20
      value: 26.0032579063492
    - type: mrr_at_3
      value: 23.45147969717827
    - type: mrr_at_5
      value: 24.535443909153518
    - type: nauc_map_at_1000_diff1
      value: 30.339772886963996
    - type: nauc_map_at_1000_max
      value: 24.935921324887698
    - type: nauc_map_at_100_diff1
      value: 30.301770543899686
    - type: nauc_map_at_100_max
      value: 24.909041701182836
    - type: nauc_map_at_10_diff1
      value: 30.48068546946062
    - type: nauc_map_at_10_max
      value: 24.54627061306137
    - type: nauc_map_at_1_diff1
      value: 36.93642654829299
    - type: nauc_map_at_1_max
      value: 22.50173107442962
    - type: nauc_map_at_20_diff1
      value: 30.345295141632473
    - type: nauc_map_at_20_max
      value: 24.845725164109208
    - type: nauc_map_at_3_diff1
      value: 31.79476218275898
    - type: nauc_map_at_3_max
      value: 24.08283763808268
    - type: nauc_map_at_5_diff1
      value: 31.09928760864003
    - type: nauc_map_at_5_max
      value: 24.524851930683894
    - type: nauc_mrr_at_1000_diff1
      value: 29.391285408000776
    - type: nauc_mrr_at_1000_max
      value: 25.53365596439313
    - type: nauc_mrr_at_100_diff1
      value: 29.36146558826297
    - type: nauc_mrr_at_100_max
      value: 25.53479888199332
    - type: nauc_mrr_at_10_diff1
      value: 29.49701708299281
    - type: nauc_mrr_at_10_max
      value: 25.445288651094366
    - type: nauc_mrr_at_1_diff1
      value: 34.932244435127345
    - type: nauc_mrr_at_1_max
      value: 24.823165105243614
    - type: nauc_mrr_at_20_diff1
      value: 29.365144551785114
    - type: nauc_mrr_at_20_max
      value: 25.588527106117564
    - type: nauc_mrr_at_3_diff1
      value: 30.424606847387935
    - type: nauc_mrr_at_3_max
      value: 25.328547737515677
    - type: nauc_mrr_at_5_diff1
      value: 29.962669010836922
    - type: nauc_mrr_at_5_max
      value: 25.613281078525773
    - type: nauc_ndcg_at_1000_diff1
      value: 27.68785785303868
    - type: nauc_ndcg_at_1000_max
      value: 25.571497899024408
    - type: nauc_ndcg_at_100_diff1
      value: 26.89754520486157
    - type: nauc_ndcg_at_100_max
      value: 25.362278762986357
    - type: nauc_ndcg_at_10_diff1
      value: 27.97761968218868
    - type: nauc_ndcg_at_10_max
      value: 24.99449024754301
    - type: nauc_ndcg_at_1_diff1
      value: 34.932244435127345
    - type: nauc_ndcg_at_1_max
      value: 24.823165105243614
    - type: nauc_ndcg_at_20_diff1
      value: 27.480897811510086
    - type: nauc_ndcg_at_20_max
      value: 25.635476091661964
    - type: nauc_ndcg_at_3_diff1
      value: 30.19504028941922
    - type: nauc_ndcg_at_3_max
      value: 25.097464879189353
    - type: nauc_ndcg_at_5_diff1
      value: 29.321717134119986
    - type: nauc_ndcg_at_5_max
      value: 25.458952638585824
    - type: nauc_precision_at_1000_diff1
      value: 6.085024737270128
    - type: nauc_precision_at_1000_max
      value: 20.9514352363991
    - type: nauc_precision_at_100_diff1
      value: 9.317325203828315
    - type: nauc_precision_at_100_max
      value: 25.379707373414607
    - type: nauc_precision_at_10_diff1
      value: 17.708763858185637
    - type: nauc_precision_at_10_max
      value: 27.646913345710487
    - type: nauc_precision_at_1_diff1
      value: 34.932244435127345
    - type: nauc_precision_at_1_max
      value: 24.823165105243614
    - type: nauc_precision_at_20_diff1
      value: 14.974953557657674
    - type: nauc_precision_at_20_max
      value: 28.987768784081673
    - type: nauc_precision_at_3_diff1
      value: 24.34596295813935
    - type: nauc_precision_at_3_max
      value: 28.096899529522197
    - type: nauc_precision_at_5_diff1
      value: 21.700178152316
    - type: nauc_precision_at_5_max
      value: 29.110974331559586
    - type: nauc_recall_at_1000_diff1
      value: 16.420585376470505
    - type: nauc_recall_at_1000_max
      value: 22.63713737420985
    - type: nauc_recall_at_100_diff1
      value: 15.284555452851478
    - type: nauc_recall_at_100_max
      value: 22.21189128618475
    - type: nauc_recall_at_10_diff1
      value: 20.556521124888956
    - type: nauc_recall_at_10_max
      value: 22.39123153463326
    - type: nauc_recall_at_1_diff1
      value: 36.93642654829299
    - type: nauc_recall_at_1_max
      value: 22.50173107442962
    - type: nauc_recall_at_20_diff1
      value: 19.252640987221948
    - type: nauc_recall_at_20_max
      value: 24.127632767083174
    - type: nauc_recall_at_3_diff1
      value: 26.134042393957728
    - type: nauc_recall_at_3_max
      value: 23.073122370729664
    - type: nauc_recall_at_5_diff1
      value: 23.999913037385387
    - type: nauc_recall_at_5_max
      value: 23.900796765497354
    - type: ndcg_at_1
      value: 18.582
    - type: ndcg_at_10
      value: 26.180999999999997
    - type: ndcg_at_100
      value: 31.541999999999998
    - type: ndcg_at_1000
      value: 34.742
    - type: ndcg_at_20
      value: 28.015
    - type: ndcg_at_3
      value: 22.262
    - type: ndcg_at_5
      value: 23.916999999999998
    - type: precision_at_1
      value: 18.582
    - type: precision_at_10
      value: 4.945
    - type: precision_at_100
      value: 0.91
    - type: precision_at_1000
      value: 0.135
    - type: precision_at_20
      value: 3.02
    - type: precision_at_3
      value: 10.84
    - type: precision_at_5
      value: 7.811
    - type: recall_at_1
      value: 14.882000000000001
    - type: recall_at_10
      value: 35.88
    - type: recall_at_100
      value: 60.056
    - type: recall_at_1000
      value: 83.222
    - type: recall_at_20
      value: 42.601
    - type: recall_at_3
      value: 24.751
    - type: recall_at_5
      value: 29.112
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-unix
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
    metrics:
    - type: map_at_1
      value: 24.015
    - type: map_at_10
      value: 33.634
    - type: map_at_100
      value: 34.933
    - type: map_at_1000
      value: 35.036
    - type: map_at_20
      value: 34.409
    - type: map_at_3
      value: 30.717
    - type: map_at_5
      value: 32.393
    - type: mrr_at_1
      value: 28.35820895522388
    - type: mrr_at_10
      value: 37.819533285951145
    - type: mrr_at_100
      value: 38.77138432965933
    - type: mrr_at_1000
      value: 38.83196591479693
    - type: mrr_at_20
      value: 38.40237397518708
    - type: mrr_at_3
      value: 35.30783582089549
    - type: mrr_at_5
      value: 36.70708955223875
    - type: nauc_map_at_1000_diff1
      value: 45.75309175655292
    - type: nauc_map_at_1000_max
      value: 38.49792787207316
    - type: nauc_map_at_100_diff1
      value: 45.76215370483687
    - type: nauc_map_at_100_max
      value: 38.48606967443172
    - type: nauc_map_at_10_diff1
      value: 46.061534066365326
    - type: nauc_map_at_10_max
      value: 38.390568231468706
    - type: nauc_map_at_1_diff1
      value: 53.2832306680782
    - type: nauc_map_at_1_max
      value: 35.797130668551134
    - type: nauc_map_at_20_diff1
      value: 45.73526011589201
    - type: nauc_map_at_20_max
      value: 38.362204368643646
    - type: nauc_map_at_3_diff1
      value: 47.07534453092877
    - type: nauc_map_at_3_max
      value: 37.78226453745493
    - type: nauc_map_at_5_diff1
      value: 46.169313251169754
    - type: nauc_map_at_5_max
      value: 37.83701771591998
    - type: nauc_mrr_at_1000_diff1
      value: 45.23881471207375
    - type: nauc_mrr_at_1000_max
      value: 40.77731247124415
    - type: nauc_mrr_at_100_diff1
      value: 45.23745441095213
    - type: nauc_mrr_at_100_max
      value: 40.76830735884476
    - type: nauc_mrr_at_10_diff1
      value: 45.183326577153665
    - type: nauc_mrr_at_10_max
      value: 40.87182785123997
    - type: nauc_mrr_at_1_diff1
      value: 52.01397826228804
    - type: nauc_mrr_at_1_max
      value: 39.09099466581579
    - type: nauc_mrr_at_20_diff1
      value: 45.14418876051915
    - type: nauc_mrr_at_20_max
      value: 40.825238496360676
    - type: nauc_mrr_at_3_diff1
      value: 45.95160361174372
    - type: nauc_mrr_at_3_max
      value: 41.126276367781074
    - type: nauc_mrr_at_5_diff1
      value: 45.14482966725835
    - type: nauc_mrr_at_5_max
      value: 40.67938024905255
    - type: nauc_ndcg_at_1000_diff1
      value: 42.821543508400154
    - type: nauc_ndcg_at_1000_max
      value: 39.612436924551
    - type: nauc_ndcg_at_100_diff1
      value: 42.96991815711811
    - type: nauc_ndcg_at_100_max
      value: 39.57961493833335
    - type: nauc_ndcg_at_10_diff1
      value: 43.29772946848505
    - type: nauc_ndcg_at_10_max
      value: 39.489639223306064
    - type: nauc_ndcg_at_1_diff1
      value: 52.01397826228804
    - type: nauc_ndcg_at_1_max
      value: 39.09099466581579
    - type: nauc_ndcg_at_20_diff1
      value: 42.5532902026286
    - type: nauc_ndcg_at_20_max
      value: 39.377121314973934
    - type: nauc_ndcg_at_3_diff1
      value: 44.68337061978331
    - type: nauc_ndcg_at_3_max
      value: 39.08953214410666
    - type: nauc_ndcg_at_5_diff1
      value: 43.42718010643401
    - type: nauc_ndcg_at_5_max
      value: 38.625943146251764
    - type: nauc_precision_at_1000_diff1
      value: -11.089310838362945
    - type: nauc_precision_at_1000_max
      value: 5.164856457144553
    - type: nauc_precision_at_100_diff1
      value: 1.8731943277967116
    - type: nauc_precision_at_100_max
      value: 19.650352646582913
    - type: nauc_precision_at_10_diff1
      value: 21.850758035619346
    - type: nauc_precision_at_10_max
      value: 36.15105948507746
    - type: nauc_precision_at_1_diff1
      value: 52.01397826228804
    - type: nauc_precision_at_1_max
      value: 39.09099466581579
    - type: nauc_precision_at_20_diff1
      value: 12.971365605869542
    - type: nauc_precision_at_20_max
      value: 29.069367371532483
    - type: nauc_precision_at_3_diff1
      value: 34.77160434034485
    - type: nauc_precision_at_3_max
      value: 40.07750794527956
    - type: nauc_precision_at_5_diff1
      value: 27.12676655417735
    - type: nauc_precision_at_5_max
      value: 36.727657492656334
    - type: nauc_recall_at_1000_diff1
      value: 8.64965782549129
    - type: nauc_recall_at_1000_max
      value: 31.773973054840575
    - type: nauc_recall_at_100_diff1
      value: 29.332324742493928
    - type: nauc_recall_at_100_max
      value: 34.525665846625174
    - type: nauc_recall_at_10_diff1
      value: 34.16931770311844
    - type: nauc_recall_at_10_max
      value: 37.24430458684276
    - type: nauc_recall_at_1_diff1
      value: 53.2832306680782
    - type: nauc_recall_at_1_max
      value: 35.797130668551134
    - type: nauc_recall_at_20_diff1
      value: 30.845649064531024
    - type: nauc_recall_at_20_max
      value: 36.23180524582533
    - type: nauc_recall_at_3_diff1
      value: 38.491192992186605
    - type: nauc_recall_at_3_max
      value: 37.150651248551256
    - type: nauc_recall_at_5_diff1
      value: 34.896873561011915
    - type: nauc_recall_at_5_max
      value: 35.56617840104705
    - type: ndcg_at_1
      value: 28.358
    - type: ndcg_at_10
      value: 39.247
    - type: ndcg_at_100
      value: 45.01
    - type: ndcg_at_1000
      value: 47.262
    - type: ndcg_at_20
      value: 41.661
    - type: ndcg_at_3
      value: 34.178
    - type: ndcg_at_5
      value: 36.592999999999996
    - type: precision_at_1
      value: 28.358
    - type: precision_at_10
      value: 6.800000000000001
    - type: precision_at_100
      value: 1.099
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: precision_at_20
      value: 4.104
    - type: precision_at_3
      value: 15.765
    - type: precision_at_5
      value: 11.325000000000001
    - type: recall_at_1
      value: 24.015
    - type: recall_at_10
      value: 52.075
    - type: recall_at_100
      value: 76.93900000000001
    - type: recall_at_1000
      value: 92.69800000000001
    - type: recall_at_20
      value: 60.575
    - type: recall_at_3
      value: 38.316
    - type: recall_at_5
      value: 44.305
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-webmasters
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
    metrics:
    - type: map_at_1
      value: 22.587
    - type: map_at_10
      value: 33.358
    - type: map_at_100
      value: 35.032000000000004
    - type: map_at_1000
      value: 35.27
    - type: map_at_20
      value: 34.322
    - type: map_at_3
      value: 29.99
    - type: map_at_5
      value: 31.863000000000003
    - type: mrr_at_1
      value: 27.66798418972332
    - type: mrr_at_10
      value: 37.98928728276552
    - type: mrr_at_100
      value: 38.957240914604526
    - type: mrr_at_1000
      value: 39.015802550827765
    - type: mrr_at_20
      value: 38.66004236653195
    - type: mrr_at_3
      value: 35.07905138339921
    - type: mrr_at_5
      value: 36.81818181818182
    - type: nauc_map_at_1000_diff1
      value: 48.0564580757036
    - type: nauc_map_at_1000_max
      value: 38.66390651485306
    - type: nauc_map_at_100_diff1
      value: 48.13870970563177
    - type: nauc_map_at_100_max
      value: 38.794746243147166
    - type: nauc_map_at_10_diff1
      value: 48.08695810938951
    - type: nauc_map_at_10_max
      value: 37.85493948938392
    - type: nauc_map_at_1_diff1
      value: 52.693975808368776
    - type: nauc_map_at_1_max
      value: 32.96177976807811
    - type: nauc_map_at_20_diff1
      value: 48.21832743397784
    - type: nauc_map_at_20_max
      value: 38.418488817167436
    - type: nauc_map_at_3_diff1
      value: 48.03103140889738
    - type: nauc_map_at_3_max
      value: 36.899652971690045
    - type: nauc_map_at_5_diff1
      value: 48.1791531189517
    - type: nauc_map_at_5_max
      value: 37.5651105817285
    - type: nauc_mrr_at_1000_diff1
      value: 45.38478613411569
    - type: nauc_mrr_at_1000_max
      value: 39.97889298875148
    - type: nauc_mrr_at_100_diff1
      value: 45.36753991032062
    - type: nauc_mrr_at_100_max
      value: 39.99803043087455
    - type: nauc_mrr_at_10_diff1
      value: 45.42191136126624
    - type: nauc_mrr_at_10_max
      value: 39.75801737012346
    - type: nauc_mrr_at_1_diff1
      value: 50.102185726419336
    - type: nauc_mrr_at_1_max
      value: 37.39820522099986
    - type: nauc_mrr_at_20_diff1
      value: 45.36124204624035
    - type: nauc_mrr_at_20_max
      value: 39.85806399752809
    - type: nauc_mrr_at_3_diff1
      value: 45.18597933351319
    - type: nauc_mrr_at_3_max
      value: 39.572873715118476
    - type: nauc_mrr_at_5_diff1
      value: 45.22616093194043
    - type: nauc_mrr_at_5_max
      value: 39.52725751466559
    - type: nauc_ndcg_at_1000_diff1
      value: 46.17235311248278
    - type: nauc_ndcg_at_1000_max
      value: 41.32028799973092
    - type: nauc_ndcg_at_100_diff1
      value: 45.990253582703964
    - type: nauc_ndcg_at_100_max
      value: 41.86548491632821
    - type: nauc_ndcg_at_10_diff1
      value: 45.98895644674703
    - type: nauc_ndcg_at_10_max
      value: 39.21777947408553
    - type: nauc_ndcg_at_1_diff1
      value: 50.102185726419336
    - type: nauc_ndcg_at_1_max
      value: 37.39820522099986
    - type: nauc_ndcg_at_20_diff1
      value: 46.26991677954197
    - type: nauc_ndcg_at_20_max
      value: 40.15497569845344
    - type: nauc_ndcg_at_3_diff1
      value: 45.585385042043605
    - type: nauc_ndcg_at_3_max
      value: 39.85762696465296
    - type: nauc_ndcg_at_5_diff1
      value: 46.139462074561955
    - type: nauc_ndcg_at_5_max
      value: 39.629082814584635
    - type: nauc_precision_at_1000_diff1
      value: -12.938606789292932
    - type: nauc_precision_at_1000_max
      value: -2.2107163272237527
    - type: nauc_precision_at_100_diff1
      value: -1.751083504475916
    - type: nauc_precision_at_100_max
      value: 14.225965549694685
    - type: nauc_precision_at_10_diff1
      value: 23.156822706657543
    - type: nauc_precision_at_10_max
      value: 37.61203594103195
    - type: nauc_precision_at_1_diff1
      value: 50.102185726419336
    - type: nauc_precision_at_1_max
      value: 37.39820522099986
    - type: nauc_precision_at_20_diff1
      value: 13.661464281345804
    - type: nauc_precision_at_20_max
      value: 31.576607836276693
    - type: nauc_precision_at_3_diff1
      value: 34.67281194105616
    - type: nauc_precision_at_3_max
      value: 44.42902772348034
    - type: nauc_precision_at_5_diff1
      value: 30.598395820028358
    - type: nauc_precision_at_5_max
      value: 41.91224173434709
    - type: nauc_recall_at_1000_diff1
      value: 36.72706004007518
    - type: nauc_recall_at_1000_max
      value: 66.48829863163812
    - type: nauc_recall_at_100_diff1
      value: 35.31061540058103
    - type: nauc_recall_at_100_max
      value: 52.25782268338071
    - type: nauc_recall_at_10_diff1
      value: 39.694414296215726
    - type: nauc_recall_at_10_max
      value: 35.69959653494372
    - type: nauc_recall_at_1_diff1
      value: 52.693975808368776
    - type: nauc_recall_at_1_max
      value: 32.96177976807811
    - type: nauc_recall_at_20_diff1
      value: 39.381784442500226
    - type: nauc_recall_at_20_max
      value: 38.80216780548151
    - type: nauc_recall_at_3_diff1
      value: 41.692680582718744
    - type: nauc_recall_at_3_max
      value: 36.25763755041077
    - type: nauc_recall_at_5_diff1
      value: 41.35336857782357
    - type: nauc_recall_at_5_max
      value: 36.73723799283182
    - type: ndcg_at_1
      value: 27.668
    - type: ndcg_at_10
      value: 39.966
    - type: ndcg_at_100
      value: 45.751
    - type: ndcg_at_1000
      value: 48.285
    - type: ndcg_at_20
      value: 42.68
    - type: ndcg_at_3
      value: 34.461000000000006
    - type: ndcg_at_5
      value: 37.132
    - type: precision_at_1
      value: 27.668
    - type: precision_at_10
      value: 7.925
    - type: precision_at_100
      value: 1.601
    - type: precision_at_1000
      value: 0.248
    - type: precision_at_20
      value: 5.188000000000001
    - type: precision_at_3
      value: 16.667
    - type: precision_at_5
      value: 12.411
    - type: recall_at_1
      value: 22.587
    - type: recall_at_10
      value: 53.616
    - type: recall_at_100
      value: 78.014
    - type: recall_at_1000
      value: 94.25200000000001
    - type: recall_at_20
      value: 63.598
    - type: recall_at_3
      value: 38.281
    - type: recall_at_5
      value: 45.235
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-wordpress
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
    metrics:
    - type: map_at_1
      value: 16.980999999999998
    - type: map_at_10
      value: 24.664
    - type: map_at_100
      value: 25.765
    - type: map_at_1000
      value: 25.877
    - type: map_at_20
      value: 25.317
    - type: map_at_3
      value: 21.683
    - type: map_at_5
      value: 23.28
    - type: mrr_at_1
      value: 18.853974121996302
    - type: mrr_at_10
      value: 26.748745709004478
    - type: mrr_at_100
      value: 27.69499469589774
    - type: mrr_at_1000
      value: 27.7790497499605
    - type: mrr_at_20
      value: 27.31636942914361
    - type: mrr_at_3
      value: 23.813924830560676
    - type: mrr_at_5
      value: 25.375847196549582
    - type: nauc_map_at_1000_diff1
      value: 30.135055330893472
    - type: nauc_map_at_1000_max
      value: 29.211781642478435
    - type: nauc_map_at_100_diff1
      value: 30.109096015606145
    - type: nauc_map_at_100_max
      value: 29.223028024025314
    - type: nauc_map_at_10_diff1
      value: 30.129974921878848
    - type: nauc_map_at_10_max
      value: 29.245101619773134
    - type: nauc_map_at_1_diff1
      value: 37.823290282037355
    - type: nauc_map_at_1_max
      value: 29.422090891644682
    - type: nauc_map_at_20_diff1
      value: 30.202570329126242
    - type: nauc_map_at_20_max
      value: 29.197785884015737
    - type: nauc_map_at_3_diff1
      value: 29.549778119396457
    - type: nauc_map_at_3_max
      value: 27.893992741038097
    - type: nauc_map_at_5_diff1
      value: 29.336004934982462
    - type: nauc_map_at_5_max
      value: 28.588249820343854
    - type: nauc_mrr_at_1000_diff1
      value: 29.339172028800693
    - type: nauc_mrr_at_1000_max
      value: 29.27328797503361
    - type: nauc_mrr_at_100_diff1
      value: 29.302051383442663
    - type: nauc_mrr_at_100_max
      value: 29.261464917945435
    - type: nauc_mrr_at_10_diff1
      value: 29.372044154749936
    - type: nauc_mrr_at_10_max
      value: 29.36307616248193
    - type: nauc_mrr_at_1_diff1
      value: 37.03290480962605
    - type: nauc_mrr_at_1_max
      value: 31.077713199666157
    - type: nauc_mrr_at_20_diff1
      value: 29.271217609971373
    - type: nauc_mrr_at_20_max
      value: 29.257249702536477
    - type: nauc_mrr_at_3_diff1
      value: 29.504640031548313
    - type: nauc_mrr_at_3_max
      value: 29.069322973200634
    - type: nauc_mrr_at_5_diff1
      value: 29.210638024296976
    - type: nauc_mrr_at_5_max
      value: 29.29717323459694
    - type: nauc_ndcg_at_1000_diff1
      value: 28.168859454720575
    - type: nauc_ndcg_at_1000_max
      value: 28.624142716676854
    - type: nauc_ndcg_at_100_diff1
      value: 27.53254314991802
    - type: nauc_ndcg_at_100_max
      value: 28.662648150774817
    - type: nauc_ndcg_at_10_diff1
      value: 28.058520401646025
    - type: nauc_ndcg_at_10_max
      value: 28.911524889930355
    - type: nauc_ndcg_at_1_diff1
      value: 37.03290480962605
    - type: nauc_ndcg_at_1_max
      value: 31.077713199666157
    - type: nauc_ndcg_at_20_diff1
      value: 28.00028907481166
    - type: nauc_ndcg_at_20_max
      value: 28.70016295408203
    - type: nauc_ndcg_at_3_diff1
      value: 27.60403796605041
    - type: nauc_ndcg_at_3_max
      value: 27.706673269710404
    - type: nauc_ndcg_at_5_diff1
      value: 26.933782633072024
    - type: nauc_ndcg_at_5_max
      value: 28.18966705713242
    - type: nauc_precision_at_1000_diff1
      value: -13.194601322238986
    - type: nauc_precision_at_1000_max
      value: -5.683449778390299
    - type: nauc_precision_at_100_diff1
      value: 8.191927897734349
    - type: nauc_precision_at_100_max
      value: 19.003145996688513
    - type: nauc_precision_at_10_diff1
      value: 23.064974274243575
    - type: nauc_precision_at_10_max
      value: 31.804683525034783
    - type: nauc_precision_at_1_diff1
      value: 37.03290480962605
    - type: nauc_precision_at_1_max
      value: 31.077713199666157
    - type: nauc_precision_at_20_diff1
      value: 20.75135128322255
    - type: nauc_precision_at_20_max
      value: 27.938848671100903
    - type: nauc_precision_at_3_diff1
      value: 21.85414901265657
    - type: nauc_precision_at_3_max
      value: 27.738658486946843
    - type: nauc_precision_at_5_diff1
      value: 21.330913305405705
    - type: nauc_precision_at_5_max
      value: 29.677546011333977
    - type: nauc_recall_at_1000_diff1
      value: 22.625301001590273
    - type: nauc_recall_at_1000_max
      value: 23.335780171797488
    - type: nauc_recall_at_100_diff1
      value: 18.671904596812176
    - type: nauc_recall_at_100_max
      value: 24.718480194959664
    - type: nauc_recall_at_10_diff1
      value: 22.697666279006068
    - type: nauc_recall_at_10_max
      value: 26.266294976782085
    - type: nauc_recall_at_1_diff1
      value: 37.823290282037355
    - type: nauc_recall_at_1_max
      value: 29.422090891644682
    - type: nauc_recall_at_20_diff1
      value: 22.23509003584087
    - type: nauc_recall_at_20_max
      value: 25.792991641838327
    - type: nauc_recall_at_3_diff1
      value: 21.454508617723867
    - type: nauc_recall_at_3_max
      value: 24.862663252665286
    - type: nauc_recall_at_5_diff1
      value: 20.09701623174741
    - type: nauc_recall_at_5_max
      value: 25.365036926878993
    - type: ndcg_at_1
      value: 18.854000000000003
    - type: ndcg_at_10
      value: 29.647000000000002
    - type: ndcg_at_100
      value: 34.945
    - type: ndcg_at_1000
      value: 37.755
    - type: ndcg_at_20
      value: 31.863000000000003
    - type: ndcg_at_3
      value: 23.835
    - type: ndcg_at_5
      value: 26.528000000000002
    - type: precision_at_1
      value: 18.854000000000003
    - type: precision_at_10
      value: 4.954
    - type: precision_at_100
      value: 0.826
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: precision_at_20
      value: 3.031
    - type: precision_at_3
      value: 10.413
    - type: precision_at_5
      value: 7.725999999999999
    - type: recall_at_1
      value: 16.980999999999998
    - type: recall_at_10
      value: 43.256
    - type: recall_at_100
      value: 67.388
    - type: recall_at_1000
      value: 88.201
    - type: recall_at_20
      value: 51.486
    - type: recall_at_3
      value: 27.862
    - type: recall_at_5
      value: 34.251
  - task:
      type: Retrieval
    dataset:
      type: mteb/climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
    metrics:
    - type: map_at_1
      value: 10.349
    - type: map_at_10
      value: 17.338
    - type: map_at_100
      value: 19.195
    - type: map_at_1000
      value: 19.392
    - type: map_at_20
      value: 18.294
    - type: map_at_3
      value: 14.135
    - type: map_at_5
      value: 15.76
    - type: mrr_at_1
      value: 23.061889250814332
    - type: mrr_at_10
      value: 33.37523912931077
    - type: mrr_at_100
      value: 34.46356661164784
    - type: mrr_at_1000
      value: 34.507303914243415
    - type: mrr_at_20
      value: 34.106438818389506
    - type: mrr_at_3
      value: 29.58740499457109
    - type: mrr_at_5
      value: 31.828447339847934
    - type: nauc_map_at_1000_diff1
      value: 24.671596968947938
    - type: nauc_map_at_1000_max
      value: 36.36603177252633
    - type: nauc_map_at_100_diff1
      value: 24.649442373925137
    - type: nauc_map_at_100_max
      value: 36.343326969183224
    - type: nauc_map_at_10_diff1
      value: 25.14978380446113
    - type: nauc_map_at_10_max
      value: 35.48311569850909
    - type: nauc_map_at_1_diff1
      value: 30.563036672557143
    - type: nauc_map_at_1_max
      value: 31.070224949027498
    - type: nauc_map_at_20_diff1
      value: 24.639891887511133
    - type: nauc_map_at_20_max
      value: 36.02290358468666
    - type: nauc_map_at_3_diff1
      value: 25.961138377808542
    - type: nauc_map_at_3_max
      value: 32.91173523346739
    - type: nauc_map_at_5_diff1
      value: 25.25579892161452
    - type: nauc_map_at_5_max
      value: 34.34423263684557
    - type: nauc_mrr_at_1000_diff1
      value: 22.338651921698233
    - type: nauc_mrr_at_1000_max
      value: 32.34456145494825
    - type: nauc_mrr_at_100_diff1
      value: 22.34047872641543
    - type: nauc_mrr_at_100_max
      value: 32.35363163490476
    - type: nauc_mrr_at_10_diff1
      value: 22.1669510472365
    - type: nauc_mrr_at_10_max
      value: 32.18098432324906
    - type: nauc_mrr_at_1_diff1
      value: 27.98859530439485
    - type: nauc_mrr_at_1_max
      value: 29.59835641778479
    - type: nauc_mrr_at_20_diff1
      value: 22.27557719524807
    - type: nauc_mrr_at_20_max
      value: 32.30332929957556
    - type: nauc_mrr_at_3_diff1
      value: 22.313118213403783
    - type: nauc_mrr_at_3_max
      value: 30.935968996729713
    - type: nauc_mrr_at_5_diff1
      value: 22.060046326212177
    - type: nauc_mrr_at_5_max
      value: 31.750738973149428
    - type: nauc_ndcg_at_1000_diff1
      value: 21.97637391967232
    - type: nauc_ndcg_at_1000_max
      value: 37.71874258101174
    - type: nauc_ndcg_at_100_diff1
      value: 22.047948671314682
    - type: nauc_ndcg_at_100_max
      value: 37.6858266885773
    - type: nauc_ndcg_at_10_diff1
      value: 22.456547498971513
    - type: nauc_ndcg_at_10_max
      value: 35.824465568616304
    - type: nauc_ndcg_at_1_diff1
      value: 27.98859530439485
    - type: nauc_ndcg_at_1_max
      value: 29.59835641778479
    - type: nauc_ndcg_at_20_diff1
      value: 21.69148966899244
    - type: nauc_ndcg_at_20_max
      value: 36.78340454303582
    - type: nauc_ndcg_at_3_diff1
      value: 23.246124156166704
    - type: nauc_ndcg_at_3_max
      value: 32.180944983977966
    - type: nauc_ndcg_at_5_diff1
      value: 22.437450155736038
    - type: nauc_ndcg_at_5_max
      value: 34.11186787901359
    - type: nauc_precision_at_1000_diff1
      value: -1.4789987463520418
    - type: nauc_precision_at_1000_max
      value: 13.165421048488732
    - type: nauc_precision_at_100_diff1
      value: 5.872177506645959
    - type: nauc_precision_at_100_max
      value: 23.11662789406202
    - type: nauc_precision_at_10_diff1
      value: 12.653231523260141
    - type: nauc_precision_at_10_max
      value: 32.69646843930873
    - type: nauc_precision_at_1_diff1
      value: 27.98859530439485
    - type: nauc_precision_at_1_max
      value: 29.59835641778479
    - type: nauc_precision_at_20_diff1
      value: 9.222810011251163
    - type: nauc_precision_at_20_max
      value: 31.642107803413644
    - type: nauc_precision_at_3_diff1
      value: 17.714754420945663
    - type: nauc_precision_at_3_max
      value: 31.20039968669417
    - type: nauc_precision_at_5_diff1
      value: 14.644243741155094
    - type: nauc_precision_at_5_max
      value: 32.38364025060788
    - type: nauc_recall_at_1000_diff1
      value: 12.54999721282459
    - type: nauc_recall_at_1000_max
      value: 35.6779997373079
    - type: nauc_recall_at_100_diff1
      value: 13.367778034443528
    - type: nauc_recall_at_100_max
      value: 33.13162691061
    - type: nauc_recall_at_10_diff1
      value: 16.949293497026215
    - type: nauc_recall_at_10_max
      value: 33.7705705210919
    - type: nauc_recall_at_1_diff1
      value: 30.563036672557143
    - type: nauc_recall_at_1_max
      value: 31.070224949027498
    - type: nauc_recall_at_20_diff1
      value: 14.089682455255875
    - type: nauc_recall_at_20_max
      value: 33.6191893484996
    - type: nauc_recall_at_3_diff1
      value: 19.948256200601705
    - type: nauc_recall_at_3_max
      value: 31.317477585260324
    - type: nauc_recall_at_5_diff1
      value: 17.598556491640565
    - type: nauc_recall_at_5_max
      value: 32.6807321944485
    - type: ndcg_at_1
      value: 23.061999999999998
    - type: ndcg_at_10
      value: 24.97
    - type: ndcg_at_100
      value: 32.554
    - type: ndcg_at_1000
      value: 36.076
    - type: ndcg_at_20
      value: 27.821
    - type: ndcg_at_3
      value: 19.349
    - type: ndcg_at_5
      value: 21.484
    - type: precision_at_1
      value: 23.061999999999998
    - type: precision_at_10
      value: 7.9350000000000005
    - type: precision_at_100
      value: 1.6039999999999999
    - type: precision_at_1000
      value: 0.22499999999999998
    - type: precision_at_20
      value: 5.176
    - type: precision_at_3
      value: 13.985
    - type: precision_at_5
      value: 11.401
    - type: recall_at_1
      value: 10.349
    - type: recall_at_10
      value: 30.913
    - type: recall_at_100
      value: 57.245999999999995
    - type: recall_at_1000
      value: 77.029
    - type: recall_at_20
      value: 39.003
    - type: recall_at_3
      value: 17.618000000000002
    - type: recall_at_5
      value: 22.988
  - task:
      type: Retrieval
    dataset:
      type: mteb/dbpedia
      name: MTEB DBPedia
      config: default
      split: test
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
    metrics:
    - type: map_at_1
      value: 7.649
    - type: map_at_10
      value: 14.697
    - type: map_at_100
      value: 19.591
    - type: map_at_1000
      value: 20.982
    - type: map_at_20
      value: 16.509999999999998
    - type: map_at_3
      value: 11.217
    - type: map_at_5
      value: 12.852
    - type: mrr_at_1
      value: 51.74999999999999
    - type: mrr_at_10
      value: 61.94424603174603
    - type: mrr_at_100
      value: 62.472815812182205
    - type: mrr_at_1000
      value: 62.49216916485864
    - type: mrr_at_20
      value: 62.25443952976847
    - type: mrr_at_3
      value: 59.708333333333364
    - type: mrr_at_5
      value: 61.03333333333334
    - type: nauc_map_at_1000_diff1
      value: 23.191206559088798
    - type: nauc_map_at_1000_max
      value: 10.1438640283226
    - type: nauc_map_at_100_diff1
      value: 23.265705221042555
    - type: nauc_map_at_100_max
      value: 7.523040573652397
    - type: nauc_map_at_10_diff1
      value: 24.45733842552937
    - type: nauc_map_at_10_max
      value: -2.443693369828331
    - type: nauc_map_at_1_diff1
      value: 31.091654941492397
    - type: nauc_map_at_1_max
      value: -10.771443812269371
    - type: nauc_map_at_20_diff1
      value: 24.7570707688042
    - type: nauc_map_at_20_max
      value: 1.2077637280889133
    - type: nauc_map_at_3_diff1
      value: 26.774816301177122
    - type: nauc_map_at_3_max
      value: -7.11823028171499
    - type: nauc_map_at_5_diff1
      value: 25.345353380719832
    - type: nauc_map_at_5_max
      value: -5.526653916514835
    - type: nauc_mrr_at_1000_diff1
      value: 32.38684163091411
    - type: nauc_mrr_at_1000_max
      value: 23.24553685116483
    - type: nauc_mrr_at_100_diff1
      value: 32.382740964614776
    - type: nauc_mrr_at_100_max
      value: 23.251303906728214
    - type: nauc_mrr_at_10_diff1
      value: 32.086483636799365
    - type: nauc_mrr_at_10_max
      value: 23.369924984911552
    - type: nauc_mrr_at_1_diff1
      value: 34.434642218762605
    - type: nauc_mrr_at_1_max
      value: 19.832378549067112
    - type: nauc_mrr_at_20_diff1
      value: 32.360936515565655
    - type: nauc_mrr_at_20_max
      value: 23.300550497980236
    - type: nauc_mrr_at_3_diff1
      value: 32.084876778026164
    - type: nauc_mrr_at_3_max
      value: 22.109999122391084
    - type: nauc_mrr_at_5_diff1
      value: 31.824992326704688
    - type: nauc_mrr_at_5_max
      value: 22.81862153744175
    - type: nauc_ndcg_at_1000_diff1
      value: 21.36050568892246
    - type: nauc_ndcg_at_1000_max
      value: 14.681554058855834
    - type: nauc_ndcg_at_100_diff1
      value: 22.127878465050646
    - type: nauc_ndcg_at_100_max
      value: 8.368076579475803
    - type: nauc_ndcg_at_10_diff1
      value: 22.317953022845348
    - type: nauc_ndcg_at_10_max
      value: 10.095615105971731
    - type: nauc_ndcg_at_1_diff1
      value: 26.646739843884106
    - type: nauc_ndcg_at_1_max
      value: 10.372045899012758
    - type: nauc_ndcg_at_20_diff1
      value: 21.917052129883217
    - type: nauc_ndcg_at_20_max
      value: 6.909226743372991
    - type: nauc_ndcg_at_3_diff1
      value: 23.54314184017729
    - type: nauc_ndcg_at_3_max
      value: 13.885591700571023
    - type: nauc_ndcg_at_5_diff1
      value: 22.89409432469125
    - type: nauc_ndcg_at_5_max
      value: 12.308023309358072
    - type: nauc_precision_at_1000_diff1
      value: -4.0950394245249875
    - type: nauc_precision_at_1000_max
      value: 28.095752660879537
    - type: nauc_precision_at_100_diff1
      value: 2.599292519176294
    - type: nauc_precision_at_100_max
      value: 35.03985690925802
    - type: nauc_precision_at_10_diff1
      value: 9.698448521965727
    - type: nauc_precision_at_10_max
      value: 33.560035529503644
    - type: nauc_precision_at_1_diff1
      value: 34.434642218762605
    - type: nauc_precision_at_1_max
      value: 19.832378549067112
    - type: nauc_precision_at_20_diff1
      value: 7.031542419630589
    - type: nauc_precision_at_20_max
      value: 33.062841844543094
    - type: nauc_precision_at_3_diff1
      value: 18.69763783368493
    - type: nauc_precision_at_3_max
      value: 28.484713601053613
    - type: nauc_precision_at_5_diff1
      value: 12.932644940053518
    - type: nauc_precision_at_5_max
      value: 29.729718202329618
    - type: nauc_recall_at_1000_diff1
      value: 14.018400068283235
    - type: nauc_recall_at_1000_max
      value: 11.044259871020023
    - type: nauc_recall_at_100_diff1
      value: 16.771246252998623
    - type: nauc_recall_at_100_max
      value: 4.49108000932358
    - type: nauc_recall_at_10_diff1
      value: 15.961719909920715
    - type: nauc_recall_at_10_max
      value: -5.026464376792105
    - type: nauc_recall_at_1_diff1
      value: 31.091654941492397
    - type: nauc_recall_at_1_max
      value: -10.771443812269371
    - type: nauc_recall_at_20_diff1
      value: 17.293696440962712
    - type: nauc_recall_at_20_max
      value: -1.1330071114103524
    - type: nauc_recall_at_3_diff1
      value: 21.93321186290146
    - type: nauc_recall_at_3_max
      value: -9.179810454022938
    - type: nauc_recall_at_5_diff1
      value: 17.797695611702576
    - type: nauc_recall_at_5_max
      value: -8.203514465529903
    - type: ndcg_at_1
      value: 42.0
    - type: ndcg_at_10
      value: 30.909
    - type: ndcg_at_100
      value: 35.508
    - type: ndcg_at_1000
      value: 43.774
    - type: ndcg_at_20
      value: 30.606
    - type: ndcg_at_3
      value: 34.525
    - type: ndcg_at_5
      value: 32.75
    - type: precision_at_1
      value: 51.74999999999999
    - type: precision_at_10
      value: 23.35
    - type: precision_at_100
      value: 7.478
    - type: precision_at_1000
      value: 1.69
    - type: precision_at_20
      value: 17.4
    - type: precision_at_3
      value: 36.833
    - type: precision_at_5
      value: 31.2
    - type: recall_at_1
      value: 7.649
    - type: recall_at_10
      value: 19.778000000000002
    - type: recall_at_100
      value: 42.652
    - type: recall_at_1000
      value: 68.417
    - type: recall_at_20
      value: 25.098
    - type: recall_at_3
      value: 12.631999999999998
    - type: recall_at_5
      value: 15.673
  - task:
      type: Classification
    dataset:
      type: mteb/emotion
      name: MTEB EmotionClassification
      config: default
      split: test
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
    metrics:
    - type: accuracy
      value: 50.20999999999999
    - type: f1
      value: 44.74511638629181
    - type: f1_weighted
      value: 52.23753103034543
  - task:
      type: Retrieval
    dataset:
      type: mteb/fever
      name: MTEB FEVER
      config: default
      split: test
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
    metrics:
    - type: map_at_1
      value: 51.953
    - type: map_at_10
      value: 65.45100000000001
    - type: map_at_100
      value: 65.804
    - type: map_at_1000
      value: 65.821
    - type: map_at_20
      value: 65.682
    - type: map_at_3
      value: 63.119
    - type: map_at_5
      value: 64.667
    - type: mrr_at_1
      value: 55.74557455745575
    - type: mrr_at_10
      value: 69.4821386900595
    - type: mrr_at_100
      value: 69.74729404754542
    - type: mrr_at_1000
      value: 69.75343973923911
    - type: mrr_at_20
      value: 69.67064873408133
    - type: mrr_at_3
      value: 67.25672567256748
    - type: mrr_at_5
      value: 68.78237823782375
    - type: nauc_map_at_1000_diff1
      value: 41.18640527838548
    - type: nauc_map_at_1000_max
      value: 13.428727470575682
    - type: nauc_map_at_100_diff1
      value: 41.17468986756459
    - type: nauc_map_at_100_max
      value: 13.426715044498552
    - type: nauc_map_at_10_diff1
      value: 41.06075186086762
    - type: nauc_map_at_10_max
      value: 13.470740909244022
    - type: nauc_map_at_1_diff1
      value: 43.27767138528766
    - type: nauc_map_at_1_max
      value: 9.510265612441069
    - type: nauc_map_at_20_diff1
      value: 41.163134792057996
    - type: nauc_map_at_20_max
      value: 13.47131574134347
    - type: nauc_map_at_3_diff1
      value: 40.910348768893975
    - type: nauc_map_at_3_max
      value: 12.768125096526042
    - type: nauc_map_at_5_diff1
      value: 40.92528504891088
    - type: nauc_map_at_5_max
      value: 13.399071004697873
    - type: nauc_mrr_at_1000_diff1
      value: 44.95436097694384
    - type: nauc_mrr_at_1000_max
      value: 14.88135771553486
    - type: nauc_mrr_at_100_diff1
      value: 44.954378878260215
    - type: nauc_mrr_at_100_max
      value: 14.890733027176758
    - type: nauc_mrr_at_10_diff1
      value: 44.86373608659125
    - type: nauc_mrr_at_10_max
      value: 15.059791916748255
    - type: nauc_mrr_at_1_diff1
      value: 46.43929638087247
    - type: nauc_mrr_at_1_max
      value: 10.272622414068575
    - type: nauc_mrr_at_20_diff1
      value: 44.95818657400733
    - type: nauc_mrr_at_20_max
      value: 14.997217206405592
    - type: nauc_mrr_at_3_diff1
      value: 44.548749443035376
    - type: nauc_mrr_at_3_max
      value: 14.469622419991582
    - type: nauc_mrr_at_5_diff1
      value: 44.69074207900513
    - type: nauc_mrr_at_5_max
      value: 15.062504791381482
    - type: nauc_ndcg_at_1000_diff1
      value: 41.520533924005
    - type: nauc_ndcg_at_1000_max
      value: 15.125821530506498
    - type: nauc_ndcg_at_100_diff1
      value: 41.30390080881711
    - type: nauc_ndcg_at_100_max
      value: 15.247971802551044
    - type: nauc_ndcg_at_10_diff1
      value: 40.888490879980694
    - type: nauc_ndcg_at_10_max
      value: 15.817174059922767
    - type: nauc_ndcg_at_1_diff1
      value: 46.43929638087247
    - type: nauc_ndcg_at_1_max
      value: 10.272622414068575
    - type: nauc_ndcg_at_20_diff1
      value: 41.25023892348253
    - type: nauc_ndcg_at_20_max
      value: 15.776116311231558
    - type: nauc_ndcg_at_3_diff1
      value: 40.94688695514675
    - type: nauc_ndcg_at_3_max
      value: 14.504886210246811
    - type: nauc_ndcg_at_5_diff1
      value: 40.70211773073117
    - type: nauc_ndcg_at_5_max
      value: 15.705189801150077
    - type: nauc_precision_at_1000_diff1
      value: 0.5912928729505902
    - type: nauc_precision_at_1000_max
      value: 11.701719862031078
    - type: nauc_precision_at_100_diff1
      value: 5.047154087374933
    - type: nauc_precision_at_100_max
      value: 17.913943619005344
    - type: nauc_precision_at_10_diff1
      value: 24.612684850432128
    - type: nauc_precision_at_10_max
      value: 29.105423290906558
    - type: nauc_precision_at_1_diff1
      value: 46.43929638087247
    - type: nauc_precision_at_1_max
      value: 10.272622414068575
    - type: nauc_precision_at_20_diff1
      value: 18.774237778586176
    - type: nauc_precision_at_20_max
      value: 27.91823531074064
    - type: nauc_precision_at_3_diff1
      value: 37.666635036168486
    - type: nauc_precision_at_3_max
      value: 21.5767280681348
    - type: nauc_precision_at_5_diff1
      value: 32.319221505378025
    - type: nauc_precision_at_5_max
      value: 28.066697359866183
    - type: nauc_recall_at_1000_diff1
      value: 17.59003049631559
    - type: nauc_recall_at_1000_max
      value: 20.93685086253374
    - type: nauc_recall_at_100_diff1
      value: 21.76964375449178
    - type: nauc_recall_at_100_max
      value: 22.758634756027416
    - type: nauc_recall_at_10_diff1
      value: 28.889097764221383
    - type: nauc_recall_at_10_max
      value: 25.30585436023595
    - type: nauc_recall_at_1_diff1
      value: 43.27767138528766
    - type: nauc_recall_at_1_max
      value: 9.510265612441069
    - type: nauc_recall_at_20_diff1
      value: 28.12473216551451
    - type: nauc_recall_at_20_max
      value: 27.143846458113202
    - type: nauc_recall_at_3_diff1
      value: 34.4572195153852
    - type: nauc_recall_at_3_max
      value: 17.36854161760104
    - type: nauc_recall_at_5_diff1
      value: 31.29465419375182
    - type: nauc_recall_at_5_max
      value: 22.273653125961907
    - type: ndcg_at_1
      value: 55.745999999999995
    - type: ndcg_at_10
      value: 71.86099999999999
    - type: ndcg_at_100
      value: 73.355
    - type: ndcg_at_1000
      value: 73.74000000000001
    - type: ndcg_at_20
      value: 72.61999999999999
    - type: ndcg_at_3
      value: 67.529
    - type: ndcg_at_5
      value: 70.15
    - type: precision_at_1
      value: 55.745999999999995
    - type: precision_at_10
      value: 9.568999999999999
    - type: precision_at_100
      value: 1.045
    - type: precision_at_1000
      value: 0.11
    - type: precision_at_20
      value: 4.96
    - type: precision_at_3
      value: 27.433000000000003
    - type: precision_at_5
      value: 17.924
    - type: recall_at_1
      value: 51.953
    - type: recall_at_10
      value: 87.459
    - type: recall_at_100
      value: 93.89800000000001
    - type: recall_at_1000
      value: 96.536
    - type: recall_at_20
      value: 90.303
    - type: recall_at_3
      value: 75.993
    - type: recall_at_5
      value: 82.39
  - task:
      type: Retrieval
    dataset:
      type: mteb/fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
    metrics:
    - type: map_at_1
      value: 18.267
    - type: map_at_10
      value: 30.447999999999997
    - type: map_at_100
      value: 32.469
    - type: map_at_1000
      value: 32.658
    - type: map_at_20
      value: 31.528
    - type: map_at_3
      value: 26.125999999999998
    - type: map_at_5
      value: 28.444999999999997
    - type: mrr_at_1
      value: 37.191358024691354
    - type: mrr_at_10
      value: 45.883793846756774
    - type: mrr_at_100
      value: 46.816652956013066
    - type: mrr_at_1000
      value: 46.84959707640699
    - type: mrr_at_20
      value: 46.41953427971011
    - type: mrr_at_3
      value: 43.389917695473244
    - type: mrr_at_5
      value: 44.863683127571996
    - type: nauc_map_at_1000_diff1
      value: 40.85830662982769
    - type: nauc_map_at_1000_max
      value: 29.735257029193157
    - type: nauc_map_at_100_diff1
      value: 40.82501487440629
    - type: nauc_map_at_100_max
      value: 29.636048452078445
    - type: nauc_map_at_10_diff1
      value: 40.68075705213936
    - type: nauc_map_at_10_max
      value: 28.337659980829322
    - type: nauc_map_at_1_diff1
      value: 48.01290466458539
    - type: nauc_map_at_1_max
      value: 19.261551938733852
    - type: nauc_map_at_20_diff1
      value: 40.856805860284226
    - type: nauc_map_at_20_max
      value: 29.077526730127286
    - type: nauc_map_at_3_diff1
      value: 43.039504408969904
    - type: nauc_map_at_3_max
      value: 24.878477839738057
    - type: nauc_map_at_5_diff1
      value: 41.724698595479595
    - type: nauc_map_at_5_max
      value: 27.113239282827994
    - type: nauc_mrr_at_1000_diff1
      value: 43.920794707966756
    - type: nauc_mrr_at_1000_max
      value: 34.614706567116606
    - type: nauc_mrr_at_100_diff1
      value: 43.895282962033846
    - type: nauc_mrr_at_100_max
      value: 34.61550432452366
    - type: nauc_mrr_at_10_diff1
      value: 43.95091533739387
    - type: nauc_mrr_at_10_max
      value: 34.663758974026365
    - type: nauc_mrr_at_1_diff1
      value: 47.61919353455421
    - type: nauc_mrr_at_1_max
      value: 33.962956428123746
    - type: nauc_mrr_at_20_diff1
      value: 43.87590747124477
    - type: nauc_mrr_at_20_max
      value: 34.67882996441685
    - type: nauc_mrr_at_3_diff1
      value: 44.88684388166846
    - type: nauc_mrr_at_3_max
      value: 34.22294561243905
    - type: nauc_mrr_at_5_diff1
      value: 43.98850549790516
    - type: nauc_mrr_at_5_max
      value: 34.83639805635503
    - type: nauc_ndcg_at_1000_diff1
      value: 40.223553918616375
    - type: nauc_ndcg_at_1000_max
      value: 33.43814923773947
    - type: nauc_ndcg_at_100_diff1
      value: 39.43807819766326
    - type: nauc_ndcg_at_100_max
      value: 32.57630719703927
    - type: nauc_ndcg_at_10_diff1
      value: 39.33282304016679
    - type: nauc_ndcg_at_10_max
      value: 30.27641232989905
    - type: nauc_ndcg_at_1_diff1
      value: 47.61919353455421
    - type: nauc_ndcg_at_1_max
      value: 33.962956428123746
    - type: nauc_ndcg_at_20_diff1
      value: 39.53511269739587
    - type: nauc_ndcg_at_20_max
      value: 31.260873254810246
    - type: nauc_ndcg_at_3_diff1
      value: 41.101187311841876
    - type: nauc_ndcg_at_3_max
      value: 32.03042648723637
    - type: nauc_ndcg_at_5_diff1
      value: 40.01327057932772
    - type: nauc_ndcg_at_5_max
      value: 31.030938992630848
    - type: nauc_precision_at_1000_diff1
      value: -0.4352015904891744
    - type: nauc_precision_at_1000_max
      value: 30.061282683255385
    - type: nauc_precision_at_100_diff1
      value: 5.39586253637153
    - type: nauc_precision_at_100_max
      value: 35.41655677334673
    - type: nauc_precision_at_10_diff1
      value: 16.69240019440236
    - type: nauc_precision_at_10_max
      value: 38.565307428383036
    - type: nauc_precision_at_1_diff1
      value: 47.61919353455421
    - type: nauc_precision_at_1_max
      value: 33.962956428123746
    - type: nauc_precision_at_20_diff1
      value: 14.485164333893326
    - type: nauc_precision_at_20_max
      value: 39.1476438430299
    - type: nauc_precision_at_3_diff1
      value: 27.334529666495627
    - type: nauc_precision_at_3_max
      value: 35.18301078607926
    - type: nauc_precision_at_5_diff1
      value: 22.50332891872499
    - type: nauc_precision_at_5_max
      value: 38.26704908439035
    - type: nauc_recall_at_1000_diff1
      value: 24.718367772502805
    - type: nauc_recall_at_1000_max
      value: 28.7950545028825
    - type: nauc_recall_at_100_diff1
      value: 22.416515348099285
    - type: nauc_recall_at_100_max
      value: 24.272228778780377
    - type: nauc_recall_at_10_diff1
      value: 27.73925715455505
    - type: nauc_recall_at_10_max
      value: 22.555074735100856
    - type: nauc_recall_at_1_diff1
      value: 48.01290466458539
    - type: nauc_recall_at_1_max
      value: 19.261551938733852
    - type: nauc_recall_at_20_diff1
      value: 26.301321924063288
    - type: nauc_recall_at_20_max
      value: 23.330876453596332
    - type: nauc_recall_at_3_diff1
      value: 37.24025810217652
    - type: nauc_recall_at_3_max
      value: 21.98119880123036
    - type: nauc_recall_at_5_diff1
      value: 32.28600801369084
    - type: nauc_recall_at_5_max
      value: 23.454012972204232
    - type: ndcg_at_1
      value: 37.191
    - type: ndcg_at_10
      value: 38.26
    - type: ndcg_at_100
      value: 45.719
    - type: ndcg_at_1000
      value: 48.786
    - type: ndcg_at_20
      value: 41.082
    - type: ndcg_at_3
      value: 34.521
    - type: ndcg_at_5
      value: 35.657
    - type: precision_at_1
      value: 37.191
    - type: precision_at_10
      value: 11.111
    - type: precision_at_100
      value: 1.8599999999999999
    - type: precision_at_1000
      value: 0.24
    - type: precision_at_20
      value: 6.6979999999999995
    - type: precision_at_3
      value: 23.714
    - type: precision_at_5
      value: 17.654
    - type: recall_at_1
      value: 18.267
    - type: recall_at_10
      value: 45.196
    - type: recall_at_100
      value: 73.21
    - type: recall_at_1000
      value: 91.603
    - type: recall_at_20
      value: 54.175
    - type: recall_at_3
      value: 30.804
    - type: recall_at_5
      value: 36.762
  - task:
      type: Retrieval
    dataset:
      type: mteb/hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
    metrics:
    - type: map_at_1
      value: 34.416000000000004
    - type: map_at_10
      value: 53.018
    - type: map_at_100
      value: 53.959999999999994
    - type: map_at_1000
      value: 54.037
    - type: map_at_20
      value: 53.586
    - type: map_at_3
      value: 49.532
    - type: map_at_5
      value: 51.745
    - type: mrr_at_1
      value: 68.83187035786631
    - type: mrr_at_10
      value: 76.47855374425244
    - type: mrr_at_100
      value: 76.75914198501198
    - type: mrr_at_1000
      value: 76.77222735751764
    - type: mrr_at_20
      value: 76.65679003625789
    - type: mrr_at_3
      value: 75.16092730137284
    - type: mrr_at_5
      value: 76.01575512041389
    - type: nauc_map_at_1000_diff1
      value: 28.665599655244538
    - type: nauc_map_at_1000_max
      value: 26.51149017702271
    - type: nauc_map_at_100_diff1
      value: 28.632597932013145
    - type: nauc_map_at_100_max
      value: 26.490932953231923
    - type: nauc_map_at_10_diff1
      value: 28.580107701324735
    - type: nauc_map_at_10_max
      value: 26.3217679581979
    - type: nauc_map_at_1_diff1
      value: 67.67936763409298
    - type: nauc_map_at_1_max
      value: 40.30036941793513
    - type: nauc_map_at_20_diff1
      value: 28.558170611509183
    - type: nauc_map_at_20_max
      value: 26.43052335111512
    - type: nauc_map_at_3_diff1
      value: 29.85672153745689
    - type: nauc_map_at_3_max
      value: 26.743012500467856
    - type: nauc_map_at_5_diff1
      value: 28.736851055431988
    - type: nauc_map_at_5_max
      value: 26.447068009197793
    - type: nauc_mrr_at_1000_diff1
      value: 65.79129234779417
    - type: nauc_mrr_at_1000_max
      value: 42.55373395618259
    - type: nauc_mrr_at_100_diff1
      value: 65.78897966625267
    - type: nauc_mrr_at_100_max
      value: 42.55832275158884
    - type: nauc_mrr_at_10_diff1
      value: 65.72331806462918
    - type: nauc_mrr_at_10_max
      value: 42.658423245180046
    - type: nauc_mrr_at_1_diff1
      value: 67.67936763409298
    - type: nauc_mrr_at_1_max
      value: 40.30036941793513
    - type: nauc_mrr_at_20_diff1
      value: 65.75380315795078
    - type: nauc_mrr_at_20_max
      value: 42.5668897917014
    - type: nauc_mrr_at_3_diff1
      value: 65.82731891309994
    - type: nauc_mrr_at_3_max
      value: 42.563700481571395
    - type: nauc_mrr_at_5_diff1
      value: 65.76141260167854
    - type: nauc_mrr_at_5_max
      value: 42.70170127345266
    - type: nauc_ndcg_at_1000_diff1
      value: 33.827746587645436
    - type: nauc_ndcg_at_1000_max
      value: 29.782418377743486
    - type: nauc_ndcg_at_100_diff1
      value: 32.972298156089224
    - type: nauc_ndcg_at_100_max
      value: 29.29551768033599
    - type: nauc_ndcg_at_10_diff1
      value: 32.938633120475814
    - type: nauc_ndcg_at_10_max
      value: 28.910191583030425
    - type: nauc_ndcg_at_1_diff1
      value: 67.67936763409298
    - type: nauc_ndcg_at_1_max
      value: 40.30036941793513
    - type: nauc_ndcg_at_20_diff1
      value: 32.731879592210355
    - type: nauc_ndcg_at_20_max
      value: 29.040697341299047
    - type: nauc_ndcg_at_3_diff1
      value: 35.47870104596234
    - type: nauc_ndcg_at_3_max
      value: 29.847488867914084
    - type: nauc_ndcg_at_5_diff1
      value: 33.54909514232655
    - type: nauc_ndcg_at_5_max
      value: 29.292689443865523
    - type: nauc_precision_at_1000_diff1
      value: 3.5615989847587506
    - type: nauc_precision_at_1000_max
      value: 19.786379641713445
    - type: nauc_precision_at_100_diff1
      value: 7.78080334803686
    - type: nauc_precision_at_100_max
      value: 19.056747747303994
    - type: nauc_precision_at_10_diff1
      value: 14.63417360636118
    - type: nauc_precision_at_10_max
      value: 20.746850850581108
    - type: nauc_precision_at_1_diff1
      value: 67.67936763409298
    - type: nauc_precision_at_1_max
      value: 40.30036941793513
    - type: nauc_precision_at_20_diff1
      value: 12.26770611631996
    - type: nauc_precision_at_20_max
      value: 20.323172131707494
    - type: nauc_precision_at_3_diff1
      value: 23.256512645251487
    - type: nauc_precision_at_3_max
      value: 25.316290441498758
    - type: nauc_precision_at_5_diff1
      value: 18.249828903730126
    - type: nauc_precision_at_5_max
      value: 23.2166512871753
    - type: nauc_recall_at_1000_diff1
      value: 3.5615989847591156
    - type: nauc_recall_at_1000_max
      value: 19.786379641713587
    - type: nauc_recall_at_100_diff1
      value: 7.780803348036787
    - type: nauc_recall_at_100_max
      value: 19.056747747303987
    - type: nauc_recall_at_10_diff1
      value: 14.634173606361264
    - type: nauc_recall_at_10_max
      value: 20.74685085058111
    - type: nauc_recall_at_1_diff1
      value: 67.67936763409298
    - type: nauc_recall_at_1_max
      value: 40.30036941793513
    - type: nauc_recall_at_20_diff1
      value: 12.267706116319852
    - type: nauc_recall_at_20_max
      value: 20.32317213170743
    - type: nauc_recall_at_3_diff1
      value: 23.25651264525152
    - type: nauc_recall_at_3_max
      value: 25.31629044149875
    - type: nauc_recall_at_5_diff1
      value: 18.249828903730062
    - type: nauc_recall_at_5_max
      value: 23.216651287175274
    - type: ndcg_at_1
      value: 68.83200000000001
    - type: ndcg_at_10
      value: 62.037
    - type: ndcg_at_100
      value: 65.405
    - type: ndcg_at_1000
      value: 66.92099999999999
    - type: ndcg_at_20
      value: 63.491
    - type: ndcg_at_3
      value: 56.899
    - type: ndcg_at_5
      value: 59.82300000000001
    - type: precision_at_1
      value: 68.83200000000001
    - type: precision_at_10
      value: 13.186
    - type: precision_at_100
      value: 1.5810000000000002
    - type: precision_at_1000
      value: 0.178
    - type: precision_at_20
      value: 7.059
    - type: precision_at_3
      value: 36.39
    - type: precision_at_5
      value: 24.154
    - type: recall_at_1
      value: 34.416000000000004
    - type: recall_at_10
      value: 65.928
    - type: recall_at_100
      value: 79.061
    - type: recall_at_1000
      value: 89.061
    - type: recall_at_20
      value: 70.594
    - type: recall_at_3
      value: 54.584999999999994
    - type: recall_at_5
      value: 60.385
  - task:
      type: Classification
    dataset:
      type: mteb/imdb
      name: MTEB ImdbClassification
      config: default
      split: test
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
    metrics:
    - type: accuracy
      value: 88.7704
    - type: ap
      value: 84.14695674023965
    - type: ap_weighted
      value: 84.14695674023965
    - type: f1
      value: 88.73968806391585
    - type: f1_weighted
      value: 88.73968806391585
  - task:
      type: Retrieval
    dataset:
      type: mteb/msmarco
      name: MTEB MSMARCO
      config: default
      split: test
      revision: c5a29a104738b98a9e76336939199e264163d4a0
    metrics:
    - type: main_score
      value: 32.11
    - type: map_at_1
      value: 15.061
    - type: map_at_10
      value: 25.754
    - type: map_at_100
      value: 27.049
    - type: map_at_1000
      value: 27.116
    - type: map_at_20
      value: 26.513
    - type: map_at_3
      value: 21.982
    - type: map_at_5
      value: 24.163
    - type: mrr_at_1
      value: 15.501432664756448
    - type: mrr_at_10
      value: 26.20690635375438
    - type: mrr_at_100
      value: 27.47484603015855
    - type: mrr_at_1000
      value: 27.534814732511403
    - type: mrr_at_20
      value: 26.962510204234486
    - type: mrr_at_3
      value: 22.478510028653206
    - type: mrr_at_5
      value: 24.644699140401147
    - type: nauc_map_at_1000_diff1
      value: 27.65573005952806
    - type: nauc_map_at_1000_max
      value: -0.6664915829456446
    - type: nauc_map_at_1000_std
      value: -13.294854242050996
    - type: nauc_map_at_100_diff1
      value: 27.65309051861404
    - type: nauc_map_at_100_max
      value: -0.6705678793129132
    - type: nauc_map_at_100_std
      value: -13.26026777113775
    - type: nauc_map_at_10_diff1
      value: 27.61977151321742
    - type: nauc_map_at_10_max
      value: -0.8411682912254755
    - type: nauc_map_at_10_std
      value: -14.078806656682952
    - type: nauc_map_at_1_diff1
      value: 31.101427439711116
    - type: nauc_map_at_1_max
      value: -2.1665597079685583
    - type: nauc_map_at_1_std
      value: -14.838541556063686
    - type: nauc_map_at_20_diff1
      value: 27.640862405035926
    - type: nauc_map_at_20_max
      value: -0.7508506379638504
    - type: nauc_map_at_20_std
      value: -13.635264331784255
    - type: nauc_map_at_3_diff1
      value: 27.816001535921503
    - type: nauc_map_at_3_max
      value: -1.4258402359181212
    - type: nauc_map_at_3_std
      value: -14.734019274210775
    - type: nauc_map_at_5_diff1
      value: 27.594758229009125
    - type: nauc_map_at_5_max
      value: -1.1541185696293443
    - type: nauc_map_at_5_std
      value: -14.543039460349144
    - type: nauc_mrr_at_1000_diff1
      value: 27.324172493369325
    - type: nauc_mrr_at_1000_max
      value: -0.5301623684083077
    - type: nauc_mrr_at_1000_std
      value: -13.085482957897204
    - type: nauc_mrr_at_100_diff1
      value: 27.31756425346039
    - type: nauc_mrr_at_100_max
      value: -0.5329475311701841
    - type: nauc_mrr_at_100_std
      value: -13.05068875597533
    - type: nauc_mrr_at_10_diff1
      value: 27.277609851940166
    - type: nauc_mrr_at_10_max
      value: -0.6898071390120286
    - type: nauc_mrr_at_10_std
      value: -13.83061727295856
    - type: nauc_mrr_at_1_diff1
      value: 30.70206781271504
    - type: nauc_mrr_at_1_max
      value: -2.011455223691345
    - type: nauc_mrr_at_1_std
      value: -14.70598014976441
    - type: nauc_mrr_at_20_diff1
      value: 27.29001503541975
    - type: nauc_mrr_at_20_max
      value: -0.5909600755849776
    - type: nauc_mrr_at_20_std
      value: -13.376016681585357
    - type: nauc_mrr_at_3_diff1
      value: 27.52254144099272
    - type: nauc_mrr_at_3_max
      value: -1.3519790006530379
    - type: nauc_mrr_at_3_std
      value: -14.649312191742936
    - type: nauc_mrr_at_5_diff1
      value: 27.29546586753163
    - type: nauc_mrr_at_5_max
      value: -1.024127157001698
    - type: nauc_mrr_at_5_std
      value: -14.345538969418342
    - type: nauc_ndcg_at_1000_diff1
      value: 26.79147605755793
    - type: nauc_ndcg_at_1000_max
      value: 0.8591996554984977
    - type: nauc_ndcg_at_1000_std
      value: -10.161918646262949
    - type: nauc_ndcg_at_100_diff1
      value: 26.63542557896811
    - type: nauc_ndcg_at_100_max
      value: 0.9443929053004976
    - type: nauc_ndcg_at_100_std
      value: -8.719362345905009
    - type: nauc_ndcg_at_10_diff1
      value: 26.517293695303856
    - type: nauc_ndcg_at_10_max
      value: 0.10338195612605405
    - type: nauc_ndcg_at_10_std
      value: -13.009131978823454
    - type: nauc_ndcg_at_1_diff1
      value: 30.538890646051947
    - type: nauc_ndcg_at_1_max
      value: -2.0080997088111858
    - type: nauc_ndcg_at_1_std
      value: -14.570358622599258
    - type: nauc_ndcg_at_20_diff1
      value: 26.54428829139771
    - type: nauc_ndcg_at_20_max
      value: 0.4099242177386758
    - type: nauc_ndcg_at_20_std
      value: -11.371084751648103
    - type: nauc_ndcg_at_3_diff1
      value: 26.958426344106917
    - type: nauc_ndcg_at_3_max
      value: -1.1589433435709675
    - type: nauc_ndcg_at_3_std
      value: -14.602252601262475
    - type: nauc_ndcg_at_5_diff1
      value: 26.59589076335421
    - type: nauc_ndcg_at_5_max
      value: -0.6453240745202081
    - type: nauc_ndcg_at_5_std
      value: -14.184185282205794
    - type: nauc_precision_at_1000_diff1
      value: -0.9922818023581059
    - type: nauc_precision_at_1000_max
      value: 16.26409042185654
    - type: nauc_precision_at_1000_std
      value: 18.321904970324764
    - type: nauc_precision_at_100_diff1
      value: 14.851754812243906
    - type: nauc_precision_at_100_max
      value: 11.328667762948233
    - type: nauc_precision_at_100_std
      value: 21.811183999636896
    - type: nauc_precision_at_10_diff1
      value: 22.530404228796173
    - type: nauc_precision_at_10_max
      value: 2.6697442120229727
    - type: nauc_precision_at_10_std
      value: -9.50958201686599
    - type: nauc_precision_at_1_diff1
      value: 30.538890646051947
    - type: nauc_precision_at_1_max
      value: -2.0080997088111858
    - type: nauc_precision_at_1_std
      value: -14.570358622599258
    - type: nauc_precision_at_20_diff1
      value: 21.512594268414414
    - type: nauc_precision_at_20_max
      value: 4.5033444829840355
    - type: nauc_precision_at_20_std
      value: -2.682841767575556
    - type: nauc_precision_at_3_diff1
      value: 24.64073891564328
    - type: nauc_precision_at_3_max
      value: -0.6975028267715811
    - type: nauc_precision_at_3_std
      value: -14.236786751518174
    - type: nauc_precision_at_5_diff1
      value: 23.781199263805577
    - type: nauc_precision_at_5_max
      value: 0.6022253719319227
    - type: nauc_precision_at_5_std
      value: -13.147295623802737
    - type: nauc_recall_at_1000_diff1
      value: 18.701134720847118
    - type: nauc_recall_at_1000_max
      value: 33.07873112775353
    - type: nauc_recall_at_1000_std
      value: 54.15619201728818
    - type: nauc_recall_at_100_diff1
      value: 22.077211961799387
    - type: nauc_recall_at_100_max
      value: 10.717243598328174
    - type: nauc_recall_at_100_std
      value: 25.184427234923484
    - type: nauc_recall_at_10_diff1
      value: 23.71859755775575
    - type: nauc_recall_at_10_max
      value: 2.5941400628857667
    - type: nauc_recall_at_10_std
      value: -9.968353668010164
    - type: nauc_recall_at_1_diff1
      value: 31.101427439711116
    - type: nauc_recall_at_1_max
      value: -2.1665597079685583
    - type: nauc_recall_at_1_std
      value: -14.838541556063686
    - type: nauc_recall_at_20_diff1
      value: 23.44415387325979
    - type: nauc_recall_at_20_max
      value: 3.887148509398752
    - type: nauc_recall_at_20_std
      value: -3.3523843677396054
    - type: nauc_recall_at_3_diff1
      value: 24.949023964253328
    - type: nauc_recall_at_3_max
      value: -0.5407315733631601
    - type: nauc_recall_at_3_std
      value: -14.250771036329174
    - type: nauc_recall_at_5_diff1
      value: 24.25304324109004
    - type: nauc_recall_at_5_max
      value: 0.5197135086143335
    - type: nauc_recall_at_5_std
      value: -13.305622144189252
    - type: ndcg_at_1
      value: 15.53
    - type: ndcg_at_10
      value: 32.11
    - type: ndcg_at_100
      value: 38.647
    - type: ndcg_at_1000
      value: 40.381
    - type: ndcg_at_20
      value: 34.844
    - type: ndcg_at_3
      value: 24.398
    - type: ndcg_at_5
      value: 28.306
    - type: precision_at_1
      value: 15.53
    - type: precision_at_10
      value: 5.418
    - type: precision_at_100
      value: 0.871
    - type: precision_at_1000
      value: 0.102
    - type: precision_at_20
      value: 3.272
    - type: precision_at_3
      value: 10.669
    - type: precision_at_5
      value: 8.375
    - type: recall_at_1
      value: 15.061
    - type: recall_at_10
      value: 51.899
    - type: recall_at_100
      value: 82.764
    - type: recall_at_1000
      value: 96.181
    - type: recall_at_20
      value: 62.567
    - type: recall_at_3
      value: 30.9
    - type: recall_at_5
      value: 40.308
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (en)
      config: en
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 92.42818057455541
    - type: f1
      value: 92.25564326311375
    - type: f1_weighted
      value: 92.41061793109351
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (en)
      config: en
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 69.23848609211126
    - type: f1
      value: 48.9439789973939
    - type: f1_weighted
      value: 71.6729639393754
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (en)
      config: en
      split: test
      revision: 4672e20407010da34463acc759c162ca9734bca6
    metrics:
    - type: accuracy
      value: 72.02084734364492
    - type: f1
      value: 69.82831463248417
    - type: f1_weighted
      value: 71.0866116386183
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (en)
      config: en
      split: test
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
    metrics:
    - type: accuracy
      value: 76.60053799596503
    - type: f1
      value: 75.85228266341957
    - type: f1_weighted
      value: 76.39049709549106
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-p2p
      name: MTEB MedrxivClusteringP2P
      config: default
      split: test
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
    metrics:
    - type: v_measure
      value: 33.65530712156858
    - type: v_measures
      value: [0.32595386072267324, 0.33095198942462645, 0.3210039965548432, 0.31914657724467665, 0.32881699064270725]
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-s2s
      name: MTEB MedrxivClusteringS2S
      config: default
      split: test
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
    metrics:
    - type: v_measure
      value: 32.2413045953903
    - type: v_measures
      value: [0.30824475884815805, 0.31071992071723326, 0.31005833310589537, 0.3153048824437766, 0.3050758199530619]
  - task:
      type: Reranking
    dataset:
      type: mteb/mind_small
      name: MTEB MindSmallReranking
      config: default
      split: test
      revision: 59042f120c80e8afa9cdbb224f67076cec0fc9a7
    metrics:
    - type: map
      value: 31.72032807796656
    - type: mrr
      value: 32.79115297194465
    - type: nAUC_map_diff1
      value: 12.922385473036147
    - type: nAUC_map_max
      value: -21.168506489275178
    - type: nAUC_mrr_diff1
      value: 12.121226745227537
    - type: nAUC_mrr_max
      value: -15.893446651123377
  - task:
      type: Retrieval
    dataset:
      type: mteb/nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
    metrics:
    - type: map_at_1
      value: 5.178
    - type: map_at_10
      value: 11.745999999999999
    - type: map_at_100
      value: 15.338
    - type: map_at_1000
      value: 16.891000000000002
    - type: map_at_20
      value: 13.256
    - type: map_at_3
      value: 8.37
    - type: map_at_5
      value: 9.894
    - type: mrr_at_1
      value: 46.749226006191954
    - type: mrr_at_10
      value: 53.71062460071747
    - type: mrr_at_100
      value: 54.47247226245396
    - type: mrr_at_1000
      value: 54.517516853423054
    - type: mrr_at_20
      value: 54.22033299509839
    - type: mrr_at_3
      value: 51.39318885448917
    - type: mrr_at_5
      value: 52.941176470588225
    - type: nauc_map_at_1000_diff1
      value: 23.238665543167727
    - type: nauc_map_at_1000_max
      value: 26.064909426436465
    - type: nauc_map_at_100_diff1
      value: 23.816943692454025
    - type: nauc_map_at_100_max
      value: 24.807156605259607
    - type: nauc_map_at_10_diff1
      value: 26.42104653124257
    - type: nauc_map_at_10_max
      value: 17.563038967727557
    - type: nauc_map_at_1_diff1
      value: 34.28917819392563
    - type: nauc_map_at_1_max
      value: 8.807377216099283
    - type: nauc_map_at_20_diff1
      value: 24.433294443909347
    - type: nauc_map_at_20_max
      value: 20.997009633165497
    - type: nauc_map_at_3_diff1
      value: 28.25335734652218
    - type: nauc_map_at_3_max
      value: 10.082598453534985
    - type: nauc_map_at_5_diff1
      value: 27.99688513776781
    - type: nauc_map_at_5_max
      value: 13.571235043636662
    - type: nauc_mrr_at_1000_diff1
      value: 22.0509325142702
    - type: nauc_mrr_at_1000_max
      value: 43.51018240855255
    - type: nauc_mrr_at_100_diff1
      value: 22.072311889586203
    - type: nauc_mrr_at_100_max
      value: 43.55130857448483
    - type: nauc_mrr_at_10_diff1
      value: 21.963828969833823
    - type: nauc_mrr_at_10_max
      value: 43.31497835062094
    - type: nauc_mrr_at_1_diff1
      value: 23.512116034730113
    - type: nauc_mrr_at_1_max
      value: 37.75543182603972
    - type: nauc_mrr_at_20_diff1
      value: 21.990415122028125
    - type: nauc_mrr_at_20_max
      value: 43.46861874289571
    - type: nauc_mrr_at_3_diff1
      value: 21.585455204189483
    - type: nauc_mrr_at_3_max
      value: 42.13202892082703
    - type: nauc_mrr_at_5_diff1
      value: 22.35605683721401
    - type: nauc_mrr_at_5_max
      value: 43.41250658367915
    - type: nauc_ndcg_at_1000_diff1
      value: 21.71738572680482
    - type: nauc_ndcg_at_1000_max
      value: 43.922463308684804
    - type: nauc_ndcg_at_100_diff1
      value: 22.43463939289653
    - type: nauc_ndcg_at_100_max
      value: 38.238637635131546
    - type: nauc_ndcg_at_10_diff1
      value: 19.014112195173833
    - type: nauc_ndcg_at_10_max
      value: 36.594960587851425
    - type: nauc_ndcg_at_1_diff1
      value: 24.042510046095366
    - type: nauc_ndcg_at_1_max
      value: 36.39029701364018
    - type: nauc_ndcg_at_20_diff1
      value: 19.381660442822373
    - type: nauc_ndcg_at_20_max
      value: 36.46556880736698
    - type: nauc_ndcg_at_3_diff1
      value: 18.6981496929732
    - type: nauc_ndcg_at_3_max
      value: 37.03091762139768
    - type: nauc_ndcg_at_5_diff1
      value: 19.289506369260305
    - type: nauc_ndcg_at_5_max
      value: 36.89125198180722
    - type: nauc_precision_at_1000_diff1
      value: -3.321795388086352
    - type: nauc_precision_at_1000_max
      value: 11.780778190351443
    - type: nauc_precision_at_100_diff1
      value: -1.8335609332536786
    - type: nauc_precision_at_100_max
      value: 23.20838971569252
    - type: nauc_precision_at_10_diff1
      value: 5.060854298695712
    - type: nauc_precision_at_10_max
      value: 36.09865020909382
    - type: nauc_precision_at_1_diff1
      value: 24.359024943159383
    - type: nauc_precision_at_1_max
      value: 38.027491208220326
    - type: nauc_precision_at_20_diff1
      value: 1.9562618966703311
    - type: nauc_precision_at_20_max
      value: 33.18760266754642
    - type: nauc_precision_at_3_diff1
      value: 11.269030511726923
    - type: nauc_precision_at_3_max
      value: 37.10153897042483
    - type: nauc_precision_at_5_diff1
      value: 9.968730085466428
    - type: nauc_precision_at_5_max
      value: 37.00822946454896
    - type: nauc_recall_at_1000_diff1
      value: 8.832722831911937
    - type: nauc_recall_at_1000_max
      value: 18.989194551015615
    - type: nauc_recall_at_100_diff1
      value: 20.173587155507132
    - type: nauc_recall_at_100_max
      value: 23.86772407377265
    - type: nauc_recall_at_10_diff1
      value: 24.975640968119407
    - type: nauc_recall_at_10_max
      value: 15.352297604598686
    - type: nauc_recall_at_1_diff1
      value: 34.28917819392563
    - type: nauc_recall_at_1_max
      value: 8.807377216099283
    - type: nauc_recall_at_20_diff1
      value: 22.57447019024638
    - type: nauc_recall_at_20_max
      value: 18.92022289045624
    - type: nauc_recall_at_3_diff1
      value: 24.107935793328
    - type: nauc_recall_at_3_max
      value: 8.801301163274843
    - type: nauc_recall_at_5_diff1
      value: 26.249224020618783
    - type: nauc_recall_at_5_max
      value: 13.064633082931609
    - type: ndcg_at_1
      value: 45.046
    - type: ndcg_at_10
      value: 33.375
    - type: ndcg_at_100
      value: 31.297000000000004
    - type: ndcg_at_1000
      value: 40.43
    - type: ndcg_at_20
      value: 31.554
    - type: ndcg_at_3
      value: 37.639
    - type: ndcg_at_5
      value: 36.1
    - type: precision_at_1
      value: 46.44
    - type: precision_at_10
      value: 25.108000000000004
    - type: precision_at_100
      value: 8.315999999999999
    - type: precision_at_1000
      value: 2.145
    - type: precision_at_20
      value: 19.164
    - type: precision_at_3
      value: 34.985
    - type: precision_at_5
      value: 31.455
    - type: recall_at_1
      value: 5.178
    - type: recall_at_10
      value: 15.953999999999999
    - type: recall_at_100
      value: 32.302
    - type: recall_at_1000
      value: 66.141
    - type: recall_at_20
      value: 20.164
    - type: recall_at_3
      value: 9.543
    - type: recall_at_5
      value: 12.122
  - task:
      type: Retrieval
    dataset:
      type: mteb/nq
      name: MTEB NQ
      config: default
      split: test
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
    metrics:
    - type: map_at_1
      value: 26.055
    - type: map_at_10
      value: 41.083999999999996
    - type: map_at_100
      value: 42.224000000000004
    - type: map_at_1000
      value: 42.257
    - type: map_at_20
      value: 41.784
    - type: map_at_3
      value: 36.723
    - type: map_at_5
      value: 39.273
    - type: mrr_at_1
      value: 29.606025492468135
    - type: mrr_at_10
      value: 43.45453061487235
    - type: mrr_at_100
      value: 44.359307196291084
    - type: mrr_at_1000
      value: 44.381684050779526
    - type: mrr_at_20
      value: 44.030997469996194
    - type: mrr_at_3
      value: 39.720934723831505
    - type: mrr_at_5
      value: 42.022499034376175
    - type: nauc_map_at_1000_diff1
      value: 26.76541483517918
    - type: nauc_map_at_1000_max
      value: 19.809039380824913
    - type: nauc_map_at_100_diff1
      value: 26.760924553836734
    - type: nauc_map_at_100_max
      value: 19.83428751875836
    - type: nauc_map_at_10_diff1
      value: 26.769732207295267
    - type: nauc_map_at_10_max
      value: 19.863047353529897
    - type: nauc_map_at_1_diff1
      value: 29.201621041718667
    - type: nauc_map_at_1_max
      value: 14.364492945564905
    - type: nauc_map_at_20_diff1
      value: 26.674976321149973
    - type: nauc_map_at_20_max
      value: 19.884257572716017
    - type: nauc_map_at_3_diff1
      value: 26.76312057995921
    - type: nauc_map_at_3_max
      value: 17.62825139877827
    - type: nauc_map_at_5_diff1
      value: 26.644381444678316
    - type: nauc_map_at_5_max
      value: 18.856601570559434
    - type: nauc_mrr_at_1000_diff1
      value: 26.684030004000704
    - type: nauc_mrr_at_1000_max
      value: 19.119179846940394
    - type: nauc_mrr_at_100_diff1
      value: 26.675761985594686
    - type: nauc_mrr_at_100_max
      value: 19.140587878258298
    - type: nauc_mrr_at_10_diff1
      value: 26.665760431219944
    - type: nauc_mrr_at_10_max
      value: 19.31261761413767
    - type: nauc_mrr_at_1_diff1
      value: 28.709762717708536
    - type: nauc_mrr_at_1_max
      value: 15.149659927369385
    - type: nauc_mrr_at_20_diff1
      value: 26.624043063321917
    - type: nauc_mrr_at_20_max
      value: 19.209958573063687
    - type: nauc_mrr_at_3_diff1
      value: 26.77330097531843
    - type: nauc_mrr_at_3_max
      value: 17.612231301724815
    - type: nauc_mrr_at_5_diff1
      value: 26.56889614476147
    - type: nauc_mrr_at_5_max
      value: 18.656150785847572
    - type: nauc_ndcg_at_1000_diff1
      value: 26.397751149487984
    - type: nauc_ndcg_at_1000_max
      value: 21.545907180381313
    - type: nauc_ndcg_at_100_diff1
      value: 26.309403626759497
    - type: nauc_ndcg_at_100_max
      value: 22.31843541483522
    - type: nauc_ndcg_at_10_diff1
      value: 26.142309559894073
    - type: nauc_ndcg_at_10_max
      value: 22.717825303945634
    - type: nauc_ndcg_at_1_diff1
      value: 28.709762717708536
    - type: nauc_ndcg_at_1_max
      value: 15.149659927369385
    - type: nauc_ndcg_at_20_diff1
      value: 25.818506896789568
    - type: nauc_ndcg_at_20_max
      value: 22.651962737600197
    - type: nauc_ndcg_at_3_diff1
      value: 26.145934086132776
    - type: nauc_ndcg_at_3_max
      value: 18.26235061310097
    - type: nauc_ndcg_at_5_diff1
      value: 25.85449614918472
    - type: nauc_ndcg_at_5_max
      value: 20.381012048917516
    - type: nauc_precision_at_1000_diff1
      value: -0.6827860286776168
    - type: nauc_precision_at_1000_max
      value: 8.378483017985578
    - type: nauc_precision_at_100_diff1
      value: 4.067738574805885
    - type: nauc_precision_at_100_max
      value: 17.55071297375258
    - type: nauc_precision_at_10_diff1
      value: 15.705216899414992
    - type: nauc_precision_at_10_max
      value: 27.119798265006324
    - type: nauc_precision_at_1_diff1
      value: 28.709762717708536
    - type: nauc_precision_at_1_max
      value: 15.149659927369385
    - type: nauc_precision_at_20_diff1
      value: 11.127812517802427
    - type: nauc_precision_at_20_max
      value: 25.355692634039844
    - type: nauc_precision_at_3_diff1
      value: 21.38569968325444
    - type: nauc_precision_at_3_max
      value: 20.50280718163951
    - type: nauc_precision_at_5_diff1
      value: 19.098857947112037
    - type: nauc_precision_at_5_max
      value: 24.102611808955704
    - type: nauc_recall_at_1000_diff1
      value: 16.862538443135836
    - type: nauc_recall_at_1000_max
      value: 61.40503097936373
    - type: nauc_recall_at_100_diff1
      value: 21.658523699091088
    - type: nauc_recall_at_100_max
      value: 51.2872759882369
    - type: nauc_recall_at_10_diff1
      value: 22.71058292832909
    - type: nauc_recall_at_10_max
      value: 33.33181387306634
    - type: nauc_recall_at_1_diff1
      value: 29.201621041718667
    - type: nauc_recall_at_1_max
      value: 14.364492945564905
    - type: nauc_recall_at_20_diff1
      value: 20.04313016737262
    - type: nauc_recall_at_20_max
      value: 35.97358308781672
    - type: nauc_recall_at_3_diff1
      value: 23.41931684712934
    - type: nauc_recall_at_3_max
      value: 19.09561618140646
    - type: nauc_recall_at_5_diff1
      value: 22.3205510124055
    - type: nauc_recall_at_5_max
      value: 24.11939747473056
    - type: ndcg_at_1
      value: 29.605999999999998
    - type: ndcg_at_10
      value: 48.92
    - type: ndcg_at_100
      value: 53.95100000000001
    - type: ndcg_at_1000
      value: 54.725
    - type: ndcg_at_20
      value: 51.266
    - type: ndcg_at_3
      value: 40.668
    - type: ndcg_at_5
      value: 44.967
    - type: precision_at_1
      value: 29.605999999999998
    - type: precision_at_10
      value: 8.386000000000001
    - type: precision_at_100
      value: 1.123
    - type: precision_at_1000
      value: 0.12
    - type: precision_at_20
      value: 4.745
    - type: precision_at_3
      value: 19.003
    - type: precision_at_5
      value: 13.847000000000001
    - type: recall_at_1
      value: 26.055
    - type: recall_at_10
      value: 70.45400000000001
    - type: recall_at_100
      value: 92.586
    - type: recall_at_1000
      value: 98.346
    - type: recall_at_20
      value: 79.251
    - type: recall_at_3
      value: 49.102000000000004
    - type: recall_at_5
      value: 58.971
  - task:
      type: Retrieval
    dataset:
      type: mteb/quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: e4e08e0b7dbe3c8700f0daef558ff32256715259
    metrics:
    - type: map_at_1
      value: 69.447
    - type: map_at_10
      value: 83.64
    - type: map_at_100
      value: 84.288
    - type: map_at_1000
      value: 84.303
    - type: map_at_20
      value: 84.053
    - type: map_at_3
      value: 80.574
    - type: map_at_5
      value: 82.505
    - type: mrr_at_1
      value: 80.11
    - type: mrr_at_10
      value: 86.60214682539649
    - type: mrr_at_100
      value: 86.71441260512907
    - type: mrr_at_1000
      value: 86.71536101979181
    - type: mrr_at_20
      value: 86.6827468831904
    - type: mrr_at_3
      value: 85.52499999999968
    - type: mrr_at_5
      value: 86.27599999999961
    - type: nauc_map_at_1000_diff1
      value: 76.63421277726033
    - type: nauc_map_at_1000_max
      value: 27.08476517398696
    - type: nauc_map_at_100_diff1
      value: 76.64091194725574
    - type: nauc_map_at_100_max
      value: 27.064003267679915
    - type: nauc_map_at_10_diff1
      value: 76.94636311335489
    - type: nauc_map_at_10_max
      value: 26.623445177537064
    - type: nauc_map_at_1_diff1
      value: 80.35741239227117
    - type: nauc_map_at_1_max
      value: 19.601081851834493
    - type: nauc_map_at_20_diff1
      value: 76.75819861748138
    - type: nauc_map_at_20_max
      value: 26.90908360101246
    - type: nauc_map_at_3_diff1
      value: 77.16382759231664
    - type: nauc_map_at_3_max
      value: 24.01363829066626
    - type: nauc_map_at_5_diff1
      value: 77.18575783199175
    - type: nauc_map_at_5_max
      value: 25.401311808248085
    - type: nauc_mrr_at_1000_diff1
      value: 76.36693861595076
    - type: nauc_mrr_at_1000_max
      value: 29.77726330795949
    - type: nauc_mrr_at_100_diff1
      value: 76.36757607506709
    - type: nauc_mrr_at_100_max
      value: 29.78003637254935
    - type: nauc_mrr_at_10_diff1
      value: 76.33194717359089
    - type: nauc_mrr_at_10_max
      value: 29.79427135219049
    - type: nauc_mrr_at_1_diff1
      value: 77.30787208693424
    - type: nauc_mrr_at_1_max
      value: 29.30894249756117
    - type: nauc_mrr_at_20_diff1
      value: 76.35228591402253
    - type: nauc_mrr_at_20_max
      value: 29.808161336278626
    - type: nauc_mrr_at_3_diff1
      value: 76.06947603126537
    - type: nauc_mrr_at_3_max
      value: 29.530736224652838
    - type: nauc_mrr_at_5_diff1
      value: 76.27457245547217
    - type: nauc_mrr_at_5_max
      value: 29.71429279915661
    - type: nauc_ndcg_at_1000_diff1
      value: 76.206745321555
    - type: nauc_ndcg_at_1000_max
      value: 28.677077854053035
    - type: nauc_ndcg_at_100_diff1
      value: 76.25100867278728
    - type: nauc_ndcg_at_100_max
      value: 28.65320148254074
    - type: nauc_ndcg_at_10_diff1
      value: 76.44814390944579
    - type: nauc_ndcg_at_10_max
      value: 27.831581434534886
    - type: nauc_ndcg_at_1_diff1
      value: 77.29022798554173
    - type: nauc_ndcg_at_1_max
      value: 29.423034034080292
    - type: nauc_ndcg_at_20_diff1
      value: 76.35440195917975
    - type: nauc_ndcg_at_20_max
      value: 28.283452431778972
    - type: nauc_ndcg_at_3_diff1
      value: 75.60134116134631
    - type: nauc_ndcg_at_3_max
      value: 26.160288096068555
    - type: nauc_ndcg_at_5_diff1
      value: 76.34144562744945
    - type: nauc_ndcg_at_5_max
      value: 26.703986078695465
    - type: nauc_precision_at_1000_diff1
      value: -44.3837577877707
    - type: nauc_precision_at_1000_max
      value: -1.3120146902477923
    - type: nauc_precision_at_100_diff1
      value: -43.99532254640492
    - type: nauc_precision_at_100_max
      value: -1.1475475372605297
    - type: nauc_precision_at_10_diff1
      value: -37.820031999886965
    - type: nauc_precision_at_10_max
      value: 2.789769770604332
    - type: nauc_precision_at_1_diff1
      value: 77.29022798554173
    - type: nauc_precision_at_1_max
      value: 29.423034034080292
    - type: nauc_precision_at_20_diff1
      value: -41.12842066028903
    - type: nauc_precision_at_20_max
      value: 0.8848328472327934
    - type: nauc_precision_at_3_diff1
      value: -15.499086324388763
    - type: nauc_precision_at_3_max
      value: 8.825638297398093
    - type: nauc_precision_at_5_diff1
      value: -29.15689830583447
    - type: nauc_precision_at_5_max
      value: 5.222909637803313
    - type: nauc_recall_at_1000_diff1
      value: 58.316380735449044
    - type: nauc_recall_at_1000_max
      value: 35.474215603329014
    - type: nauc_recall_at_100_diff1
      value: 74.02961332717067
    - type: nauc_recall_at_100_max
      value: 34.87738243272472
    - type: nauc_recall_at_10_diff1
      value: 71.73536883864209
    - type: nauc_recall_at_10_max
      value: 24.763680858463065
    - type: nauc_recall_at_1_diff1
      value: 80.35741239227117
    - type: nauc_recall_at_1_max
      value: 19.601081851834493
    - type: nauc_recall_at_20_diff1
      value: 71.44247977786146
    - type: nauc_recall_at_20_max
      value: 27.15094620537665
    - type: nauc_recall_at_3_diff1
      value: 72.96240828568985
    - type: nauc_recall_at_3_max
      value: 19.89319465322196
    - type: nauc_recall_at_5_diff1
      value: 72.2253431450756
    - type: nauc_recall_at_5_max
      value: 21.07584062401138
    - type: ndcg_at_1
      value: 80.12
    - type: ndcg_at_10
      value: 87.58200000000001
    - type: ndcg_at_100
      value: 88.838
    - type: ndcg_at_1000
      value: 88.932
    - type: ndcg_at_20
      value: 88.23
    - type: ndcg_at_3
      value: 84.468
    - type: ndcg_at_5
      value: 86.217
    - type: precision_at_1
      value: 80.12
    - type: precision_at_10
      value: 13.404
    - type: precision_at_100
      value: 1.536
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_20
      value: 7.105
    - type: precision_at_3
      value: 37.083
    - type: precision_at_5
      value: 24.490000000000002
    - type: recall_at_1
      value: 69.447
    - type: recall_at_10
      value: 95.261
    - type: recall_at_100
      value: 99.556
    - type: recall_at_1000
      value: 99.98700000000001
    - type: recall_at_20
      value: 97.329
    - type: recall_at_3
      value: 86.454
    - type: recall_at_5
      value: 91.302
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering
      name: MTEB RedditClustering
      config: default
      split: test
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
    metrics:
    - type: v_measure
      value: 57.01720770852658
    - type: v_measures
      value: [0.5756544791593571, 0.6377272023562836, 0.5350514791957027, 0.5727084874879221, 0.5741416733953204]
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering-p2p
      name: MTEB RedditClusteringP2P
      config: default
      split: test
      revision: 385e3cb46b4cfa89021f56c4380204149d0efe33
    metrics:
    - type: v_measure
      value: 63.39660435448354
    - type: v_measures
      value: [0.6741507650969407, 0.6776857590180145, 0.6519472016355243, 0.4016811296197587, 0.7184490438164246]
  - task:
      type: Retrieval
    dataset:
      type: mteb/scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: f8c2fcf00f625baaa80f62ec5bd9e1fff3b8ae88
    metrics:
    - type: map_at_1
      value: 4.123
    - type: map_at_10
      value: 11.003
    - type: map_at_100
      value: 13.086
    - type: map_at_1000
      value: 13.406
    - type: map_at_20
      value: 12.006
    - type: map_at_3
      value: 7.505000000000001
    - type: map_at_5
      value: 9.139
    - type: mrr_at_1
      value: 20.3
    - type: mrr_at_10
      value: 31.21436507936507
    - type: mrr_at_100
      value: 32.43997259322759
    - type: mrr_at_1000
      value: 32.49804601067173
    - type: mrr_at_20
      value: 31.961783515332247
    - type: mrr_at_3
      value: 27.833333333333343
    - type: mrr_at_5
      value: 29.79833333333332
    - type: nauc_map_at_1000_diff1
      value: 14.661473310156135
    - type: nauc_map_at_1000_max
      value: 23.969100824477742
    - type: nauc_map_at_100_diff1
      value: 14.703051233516987
    - type: nauc_map_at_100_max
      value: 23.881944995141712
    - type: nauc_map_at_10_diff1
      value: 15.225425788786485
    - type: nauc_map_at_10_max
      value: 22.39713605775864
    - type: nauc_map_at_1_diff1
      value: 20.404606112095774
    - type: nauc_map_at_1_max
      value: 12.759366847303136
    - type: nauc_map_at_20_diff1
      value: 14.985657067007502
    - type: nauc_map_at_20_max
      value: 23.379808618858394
    - type: nauc_map_at_3_diff1
      value: 17.087758058517867
    - type: nauc_map_at_3_max
      value: 19.754509850158033
    - type: nauc_map_at_5_diff1
      value: 15.453826256469172
    - type: nauc_map_at_5_max
      value: 19.720929794286146
    - type: nauc_mrr_at_1000_diff1
      value: 15.440551763342134
    - type: nauc_mrr_at_1000_max
      value: 16.67610367954031
    - type: nauc_mrr_at_100_diff1
      value: 15.446397904682927
    - type: nauc_mrr_at_100_max
      value: 16.68538737853014
    - type: nauc_mrr_at_10_diff1
      value: 15.130957558462777
    - type: nauc_mrr_at_10_max
      value: 16.729201930834854
    - type: nauc_mrr_at_1_diff1
      value: 20.599787166082688
    - type: nauc_mrr_at_1_max
      value: 13.086396766722139
    - type: nauc_mrr_at_20_diff1
      value: 15.521589995373436
    - type: nauc_mrr_at_20_max
      value: 16.807989440190692
    - type: nauc_mrr_at_3_diff1
      value: 14.779375429377223
    - type: nauc_mrr_at_3_max
      value: 15.799708324795999
    - type: nauc_mrr_at_5_diff1
      value: 14.714606377690822
    - type: nauc_mrr_at_5_max
      value: 15.82617740543559
    - type: nauc_ndcg_at_1000_diff1
      value: 13.39201747975155
    - type: nauc_ndcg_at_1000_max
      value: 25.33597144067427
    - type: nauc_ndcg_at_100_diff1
      value: 13.80191100123789
    - type: nauc_ndcg_at_100_max
      value: 25.22623989738723
    - type: nauc_ndcg_at_10_diff1
      value: 14.052113477249403
    - type: nauc_ndcg_at_10_max
      value: 22.61410174349243
    - type: nauc_ndcg_at_1_diff1
      value: 20.599787166082688
    - type: nauc_ndcg_at_1_max
      value: 13.086396766722139
    - type: nauc_ndcg_at_20_diff1
      value: 14.54284244377066
    - type: nauc_ndcg_at_20_max
      value: 24.09340663574116
    - type: nauc_ndcg_at_3_diff1
      value: 15.283233264388679
    - type: nauc_ndcg_at_3_max
      value: 19.276973272574264
    - type: nauc_ndcg_at_5_diff1
      value: 13.930696883287624
    - type: nauc_ndcg_at_5_max
      value: 18.73611502366555
    - type: nauc_precision_at_1000_diff1
      value: 5.180565775548697
    - type: nauc_precision_at_1000_max
      value: 24.82929948766495
    - type: nauc_precision_at_100_diff1
      value: 9.162311335376176
    - type: nauc_precision_at_100_max
      value: 26.64992389415198
    - type: nauc_precision_at_10_diff1
      value: 11.364602358380695
    - type: nauc_precision_at_10_max
      value: 25.52348798501451
    - type: nauc_precision_at_1_diff1
      value: 20.599787166082688
    - type: nauc_precision_at_1_max
      value: 13.086396766722139
    - type: nauc_precision_at_20_diff1
      value: 12.045746243312522
    - type: nauc_precision_at_20_max
      value: 26.867317370076194
    - type: nauc_precision_at_3_diff1
      value: 13.040150636666178
    - type: nauc_precision_at_3_max
      value: 21.357221278029044
    - type: nauc_precision_at_5_diff1
      value: 11.314395666011867
    - type: nauc_precision_at_5_max
      value: 20.004759964663357
    - type: nauc_recall_at_1000_diff1
      value: 4.149648293224201
    - type: nauc_recall_at_1000_max
      value: 23.5600226747804
    - type: nauc_recall_at_100_diff1
      value: 8.522718126025284
    - type: nauc_recall_at_100_max
      value: 25.922981469643343
    - type: nauc_recall_at_10_diff1
      value: 10.804397935171327
    - type: nauc_recall_at_10_max
      value: 24.77066994708541
    - type: nauc_recall_at_1_diff1
      value: 20.404606112095774
    - type: nauc_recall_at_1_max
      value: 12.759366847303136
    - type: nauc_recall_at_20_diff1
      value: 11.425764665711029
    - type: nauc_recall_at_20_max
      value: 26.18551564490963
    - type: nauc_recall_at_3_diff1
      value: 12.708708044291516
    - type: nauc_recall_at_3_max
      value: 20.833248700871195
    - type: nauc_recall_at_5_diff1
      value: 10.890559276299753
    - type: nauc_recall_at_5_max
      value: 19.28508635673444
    - type: ndcg_at_1
      value: 20.3
    - type: ndcg_at_10
      value: 18.829
    - type: ndcg_at_100
      value: 27.095000000000002
    - type: ndcg_at_1000
      value: 32.748
    - type: ndcg_at_20
      value: 21.648
    - type: ndcg_at_3
      value: 17.041999999999998
    - type: ndcg_at_5
      value: 15.17
    - type: precision_at_1
      value: 20.3
    - type: precision_at_10
      value: 10.09
    - type: precision_at_100
      value: 2.2089999999999996
    - type: precision_at_1000
      value: 0.357
    - type: precision_at_20
      value: 6.68
    - type: precision_at_3
      value: 16.1
    - type: precision_at_5
      value: 13.56
    - type: recall_at_1
      value: 4.123
    - type: recall_at_10
      value: 20.487
    - type: recall_at_100
      value: 44.835
    - type: recall_at_1000
      value: 72.458
    - type: recall_at_20
      value: 27.102999999999998
    - type: recall_at_3
      value: 9.778
    - type: recall_at_5
      value: 13.763
  - task:
      type: STS
    dataset:
      type: mteb/sickr-sts
      name: MTEB SICK-R
      config: default
      split: test
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
    metrics:
    - type: cos_sim_pearson
      value: 86.67710766878982
    - type: cos_sim_spearman
      value: 81.0146278511025
    - type: euclidean_pearson
      value: 84.6541976779553
    - type: euclidean_spearman
      value: 81.01462483847283
    - type: manhattan_pearson
      value: 84.63222929587954
    - type: manhattan_spearman
      value: 80.95879743785594
  - task:
      type: STS
    dataset:
      type: mteb/sts12-sts
      name: MTEB STS12
      config: default
      split: test
      revision: a0d554a64d88156834ff5ae9920b964011b16384
    metrics:
    - type: cos_sim_pearson
      value: 91.56759945236915
    - type: cos_sim_spearman
      value: 85.52036823639511
    - type: euclidean_pearson
      value: 89.13232574418899
    - type: euclidean_spearman
      value: 85.51983870200014
    - type: manhattan_pearson
      value: 89.13468354750995
    - type: manhattan_spearman
      value: 85.5125095149674
  - task:
      type: STS
    dataset:
      type: mteb/sts13-sts
      name: MTEB STS13
      config: default
      split: test
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
    metrics:
    - type: cos_sim_pearson
      value: 88.77431350593656
    - type: cos_sim_spearman
      value: 89.36590409791387
    - type: euclidean_pearson
      value: 89.41057125926268
    - type: euclidean_spearman
      value: 89.36590409791387
    - type: manhattan_pearson
      value: 89.23527839147364
    - type: manhattan_spearman
      value: 89.1460164042126
  - task:
      type: STS
    dataset:
      type: mteb/sts14-sts
      name: MTEB STS14
      config: default
      split: test
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
    metrics:
    - type: cos_sim_pearson
      value: 91.28072839903398
    - type: cos_sim_spearman
      value: 91.60879188296313
    - type: euclidean_pearson
      value: 90.82019203957024
    - type: euclidean_spearman
      value: 91.60879056019314
    - type: manhattan_pearson
      value: 90.68711650077914
    - type: manhattan_spearman
      value: 91.51996736811303
  - task:
      type: STS
    dataset:
      type: mteb/sts15-sts
      name: MTEB STS15
      config: default
      split: test
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
    metrics:
    - type: cos_sim_pearson
      value: 91.30086405535995
    - type: cos_sim_spearman
      value: 92.02450415044238
    - type: euclidean_pearson
      value: 91.62742541974103
    - type: euclidean_spearman
      value: 92.02448526713779
    - type: manhattan_pearson
      value: 91.58340156488379
    - type: manhattan_spearman
      value: 91.97028302271599
  - task:
      type: STS
    dataset:
      type: mteb/sts16-sts
      name: MTEB STS16
      config: default
      split: test
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
    metrics:
    - type: cos_sim_pearson
      value: 84.26589373642062
    - type: cos_sim_spearman
      value: 86.29327410655272
    - type: euclidean_pearson
      value: 86.14121596120088
    - type: euclidean_spearman
      value: 86.2932736410034
    - type: manhattan_pearson
      value: 86.099615966564
    - type: manhattan_spearman
      value: 86.23990988150905
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-en)
      config: en-en
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: cos_sim_pearson
      value: 88.83802620244516
    - type: cos_sim_spearman
      value: 88.70915251373806
    - type: euclidean_pearson
      value: 89.23928842159836
    - type: euclidean_spearman
      value: 88.70915251373806
    - type: manhattan_pearson
      value: 89.3066543956283
    - type: manhattan_spearman
      value: 88.72003093613347
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (en)
      config: en
      split: test
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
    metrics:
    - type: cos_sim_pearson
      value: 69.16204861304973
    - type: cos_sim_spearman
      value: 68.57518139813385
    - type: euclidean_pearson
      value: 70.11263405788239
    - type: euclidean_spearman
      value: 68.57518139813385
    - type: manhattan_pearson
      value: 70.02611504966039
    - type: manhattan_spearman
      value: 68.54506840432155
  - task:
      type: STS
    dataset:
      type: mteb/stsbenchmark-sts
      name: MTEB STSBenchmark
      config: default
      split: test
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
    metrics:
    - type: cos_sim_pearson
      value: 88.48685029144609
    - type: cos_sim_spearman
      value: 89.28237056532355
    - type: euclidean_pearson
      value: 88.790582154664
    - type: euclidean_spearman
      value: 89.28237627971608
    - type: manhattan_pearson
      value: 88.7750314966219
    - type: manhattan_spearman
      value: 89.24273911375099
  - task:
      type: Reranking
    dataset:
      type: mteb/scidocs-reranking
      name: MTEB SciDocsRR
      config: default
      split: test
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
    metrics:
    - type: map
      value: 84.26465304018446
    - type: mrr
      value: 95.55740102308728
    - type: nAUC_map_diff1
      value: 2.3010600094211826
    - type: nAUC_map_max
      value: 51.82496315164315
    - type: nAUC_mrr_diff1
      value: 47.20050019161225
    - type: nAUC_mrr_max
      value: 82.06692909101838
  - task:
      type: Retrieval
    dataset:
      type: mteb/scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
    metrics:
    - type: map_at_1
      value: 52.261
    - type: map_at_10
      value: 63.474
    - type: map_at_100
      value: 64.101
    - type: map_at_1000
      value: 64.12400000000001
    - type: map_at_20
      value: 63.92099999999999
    - type: map_at_3
      value: 60.202
    - type: map_at_5
      value: 62.346999999999994
    - type: mrr_at_1
      value: 55.333333333333336
    - type: mrr_at_10
      value: 64.810582010582
    - type: mrr_at_100
      value: 65.29369311756177
    - type: mrr_at_1000
      value: 65.31668703226731
    - type: mrr_at_20
      value: 65.142404762993
    - type: mrr_at_3
      value: 62.27777777777778
    - type: mrr_at_5
      value: 63.89444444444443
    - type: nauc_map_at_1000_diff1
      value: 71.57738550930519
    - type: nauc_map_at_1000_max
      value: 52.120881969712784
    - type: nauc_map_at_100_diff1
      value: 71.5681737134227
    - type: nauc_map_at_100_max
      value: 52.129646665477416
    - type: nauc_map_at_10_diff1
      value: 71.5021261214607
    - type: nauc_map_at_10_max
      value: 51.90640420773687
    - type: nauc_map_at_1_diff1
      value: 74.72600050724301
    - type: nauc_map_at_1_max
      value: 45.859865902655
    - type: nauc_map_at_20_diff1
      value: 71.41589038508471
    - type: nauc_map_at_20_max
      value: 52.18146822557371
    - type: nauc_map_at_3_diff1
      value: 71.70482718158765
    - type: nauc_map_at_3_max
      value: 49.510310769007184
    - type: nauc_map_at_5_diff1
      value: 71.43450369677332
    - type: nauc_map_at_5_max
      value: 51.63328958880189
    - type: nauc_mrr_at_1000_diff1
      value: 71.41985649990272
    - type: nauc_mrr_at_1000_max
      value: 53.91827766909258
    - type: nauc_mrr_at_100_diff1
      value: 71.41063093218023
    - type: nauc_mrr_at_100_max
      value: 53.92567207016017
    - type: nauc_mrr_at_10_diff1
      value: 71.29002807688848
    - type: nauc_mrr_at_10_max
      value: 53.929340888153035
    - type: nauc_mrr_at_1_diff1
      value: 75.33047097398506
    - type: nauc_mrr_at_1_max
      value: 51.21196178092619
    - type: nauc_mrr_at_20_diff1
      value: 71.2670444409678
    - type: nauc_mrr_at_20_max
      value: 53.98922395823477
    - type: nauc_mrr_at_3_diff1
      value: 71.34253146019464
    - type: nauc_mrr_at_3_max
      value: 53.88566895296174
    - type: nauc_mrr_at_5_diff1
      value: 71.22395053830624
    - type: nauc_mrr_at_5_max
      value: 53.95661663889736
    - type: nauc_ndcg_at_1000_diff1
      value: 70.70906891526685
    - type: nauc_ndcg_at_1000_max
      value: 53.75091762583295
    - type: nauc_ndcg_at_100_diff1
      value: 70.50810836912629
    - type: nauc_ndcg_at_100_max
      value: 54.16895375464208
    - type: nauc_ndcg_at_10_diff1
      value: 69.93929339259867
    - type: nauc_ndcg_at_10_max
      value: 53.77039667237021
    - type: nauc_ndcg_at_1_diff1
      value: 75.33047097398506
    - type: nauc_ndcg_at_1_max
      value: 51.21196178092619
    - type: nauc_ndcg_at_20_diff1
      value: 69.56746634646002
    - type: nauc_ndcg_at_20_max
      value: 54.570390765735674
    - type: nauc_ndcg_at_3_diff1
      value: 70.29929722219461
    - type: nauc_ndcg_at_3_max
      value: 51.98432322450574
    - type: nauc_ndcg_at_5_diff1
      value: 69.91123944884558
    - type: nauc_ndcg_at_5_max
      value: 53.413153135040034
    - type: nauc_precision_at_1000_diff1
      value: -17.62636021560043
    - type: nauc_precision_at_1000_max
      value: 24.21573612664845
    - type: nauc_precision_at_100_diff1
      value: -3.0012526096032692
    - type: nauc_precision_at_100_max
      value: 32.47821851078637
    - type: nauc_precision_at_10_diff1
      value: 20.940060915480927
    - type: nauc_precision_at_10_max
      value: 45.96592813527698
    - type: nauc_precision_at_1_diff1
      value: 75.33047097398506
    - type: nauc_precision_at_1_max
      value: 51.21196178092619
    - type: nauc_precision_at_20_diff1
      value: 8.077545225645986
    - type: nauc_precision_at_20_max
      value: 41.63579071297479
    - type: nauc_precision_at_3_diff1
      value: 49.7270000524541
    - type: nauc_precision_at_3_max
      value: 50.338806048439
    - type: nauc_precision_at_5_diff1
      value: 32.83291402594661
    - type: nauc_precision_at_5_max
      value: 49.9039946475297
    - type: nauc_recall_at_1000_diff1
      value: 12.278244631182748
    - type: nauc_recall_at_1000_max
      value: 12.278244631182748
    - type: nauc_recall_at_100_diff1
      value: 60.89519140989744
    - type: nauc_recall_at_100_max
      value: 66.77462651727343
    - type: nauc_recall_at_10_diff1
      value: 60.68672210792195
    - type: nauc_recall_at_10_max
      value: 56.36646101118327
    - type: nauc_recall_at_1_diff1
      value: 74.72600050724301
    - type: nauc_recall_at_1_max
      value: 45.859865902655
    - type: nauc_recall_at_20_diff1
      value: 55.29680767802708
    - type: nauc_recall_at_20_max
      value: 63.48062195652917
    - type: nauc_recall_at_3_diff1
      value: 65.48457154826137
    - type: nauc_recall_at_3_max
      value: 52.45983257437835
    - type: nauc_recall_at_5_diff1
      value: 63.012725559525876
    - type: nauc_recall_at_5_max
      value: 55.32310936331189
    - type: ndcg_at_1
      value: 55.333
    - type: ndcg_at_10
      value: 68.547
    - type: ndcg_at_100
      value: 71.203
    - type: ndcg_at_1000
      value: 71.839
    - type: ndcg_at_20
      value: 69.973
    - type: ndcg_at_3
      value: 62.982000000000006
    - type: ndcg_at_5
      value: 66.116
    - type: precision_at_1
      value: 55.333
    - type: precision_at_10
      value: 9.367
    - type: precision_at_100
      value: 1.077
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_20
      value: 5.017
    - type: precision_at_3
      value: 24.778
    - type: precision_at_5
      value: 17.0
    - type: recall_at_1
      value: 52.261
    - type: recall_at_10
      value: 82.756
    - type: recall_at_100
      value: 94.667
    - type: recall_at_1000
      value: 99.667
    - type: recall_at_20
      value: 88.1
    - type: recall_at_3
      value: 68.072
    - type: recall_at_5
      value: 75.594
  - task:
      type: PairClassification
    dataset:
      type: mteb/sprintduplicatequestions-pairclassification
      name: MTEB SprintDuplicateQuestions
      config: default
      split: test
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
    metrics:
    - type: cos_sim_accuracy
      value: 99.7089108910891
    - type: cos_sim_ap
      value: 92.56973112464647
    - type: cos_sim_f1
      value: 85.71428571428572
    - type: cos_sim_precision
      value: 83.36483931947069
    - type: cos_sim_recall
      value: 88.2
    - type: dot_accuracy
      value: 99.7089108910891
    - type: dot_ap
      value: 92.56973112464647
    - type: dot_f1
      value: 85.71428571428572
    - type: dot_precision
      value: 83.36483931947069
    - type: dot_recall
      value: 88.2
    - type: euclidean_accuracy
      value: 99.7089108910891
    - type: euclidean_ap
      value: 92.56973112464647
    - type: euclidean_f1
      value: 85.71428571428572
    - type: euclidean_precision
      value: 83.36483931947069
    - type: euclidean_recall
      value: 88.2
    - type: manhattan_accuracy
      value: 99.71089108910891
    - type: manhattan_ap
      value: 92.61210920251231
    - type: manhattan_f1
      value: 85.67335243553008
    - type: manhattan_precision
      value: 81.99268738574041
    - type: manhattan_recall
      value: 89.7
    - type: max_accuracy
      value: 99.71089108910891
    - type: max_ap
      value: 92.61210920251231
    - type: max_f1
      value: 85.71428571428572
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering
      name: MTEB StackExchangeClustering
      config: default
      split: test
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
    metrics:
    - type: v_measure
      value: 63.52867442696344
    - type: v_measures
      value: [0.6625048987673257, 0.6592452238860584, 0.5336897183180842, 0.6536652552260772, 0.6447075326923979]
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering-p2p
      name: MTEB StackExchangeClusteringP2P
      config: default
      split: test
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
    metrics:
    - type: v_measure
      value: 34.484264639302125
    - type: v_measures
      value: [0.32723348522700696, 0.32988067014351286, 0.3321795520202266, 0.3280894871874504, 0.334180768657311]
  - task:
      type: Reranking
    dataset:
      type: mteb/stackoverflowdupquestions-reranking
      name: MTEB StackOverflowDupQuestions
      config: default
      split: test
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
    metrics:
    - type: map
      value: 48.297646501427
    - type: mrr
      value: 48.996066229522114
    - type: nAUC_map_diff1
      value: 35.64070514812399
    - type: nAUC_map_max
      value: 14.117031860096372
    - type: nAUC_mrr_diff1
      value: 36.00922952321859
    - type: nAUC_mrr_max
      value: 15.053021581086082
  - task:
      type: Summarization
    dataset:
      type: mteb/summeval
      name: MTEB SummEval
      config: default
      split: test
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
    metrics:
    - type: cos_sim_pearson
      value: 31.07533307224652
    - type: cos_sim_spearman
      value: 31.140404379619575
    - type: dot_pearson
      value: 31.07533309209607
    - type: dot_spearman
      value: 31.163489511951852
  - task:
      type: Retrieval
    dataset:
      type: mteb/trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
    metrics:
    - type: map_at_1
      value: 0.185
    - type: map_at_10
      value: 1.165
    - type: map_at_100
      value: 7.086
    - type: map_at_1000
      value: 20.807000000000002
    - type: map_at_20
      value: 2.09
    - type: map_at_3
      value: 0.41700000000000004
    - type: map_at_5
      value: 0.629
    - type: mrr_at_1
      value: 68.0
    - type: mrr_at_10
      value: 79.0547619047619
    - type: mrr_at_100
      value: 79.0547619047619
    - type: mrr_at_1000
      value: 79.0547619047619
    - type: mrr_at_20
      value: 79.0547619047619
    - type: mrr_at_3
      value: 77.0
    - type: mrr_at_5
      value: 77.9
    - type: nauc_map_at_1000_diff1
      value: -22.67750756125608
    - type: nauc_map_at_1000_max
      value: 35.11625077601572
    - type: nauc_map_at_100_diff1
      value: -13.451821118067087
    - type: nauc_map_at_100_max
      value: 36.94777978235449
    - type: nauc_map_at_10_diff1
      value: -1.945674720620008
    - type: nauc_map_at_10_max
      value: 33.20773892261476
    - type: nauc_map_at_1_diff1
      value: -6.48595577983789
    - type: nauc_map_at_1_max
      value: 2.3330438771924435
    - type: nauc_map_at_20_diff1
      value: -4.297796014166373
    - type: nauc_map_at_20_max
      value: 30.725951163880875
    - type: nauc_map_at_3_diff1
      value: 4.796998423926565
    - type: nauc_map_at_3_max
      value: 26.150071629546893
    - type: nauc_map_at_5_diff1
      value: 2.6871952838061723
    - type: nauc_map_at_5_max
      value: 30.408421467098012
    - type: nauc_mrr_at_1000_diff1
      value: -13.814249836896042
    - type: nauc_mrr_at_1000_max
      value: 31.88498612201202
    - type: nauc_mrr_at_100_diff1
      value: -13.814249836896042
    - type: nauc_mrr_at_100_max
      value: 31.88498612201202
    - type: nauc_mrr_at_10_diff1
      value: -13.814249836896042
    - type: nauc_mrr_at_10_max
      value: 31.88498612201202
    - type: nauc_mrr_at_1_diff1
      value: -13.92094533895383
    - type: nauc_mrr_at_1_max
      value: 29.306889641351635
    - type: nauc_mrr_at_20_diff1
      value: -13.814249836896042
    - type: nauc_mrr_at_20_max
      value: 31.88498612201202
    - type: nauc_mrr_at_3_diff1
      value: -12.33170416820374
    - type: nauc_mrr_at_3_max
      value: 31.011004549366817
    - type: nauc_mrr_at_5_diff1
      value: -14.747452402364146
    - type: nauc_mrr_at_5_max
      value: 33.79476229635637
    - type: nauc_ndcg_at_1000_diff1
      value: -12.074426607123078
    - type: nauc_ndcg_at_1000_max
      value: 33.784478850282134
    - type: nauc_ndcg_at_100_diff1
      value: -18.479165151069303
    - type: nauc_ndcg_at_100_max
      value: 31.708196197267974
    - type: nauc_ndcg_at_10_diff1
      value: -8.73408016992012
    - type: nauc_ndcg_at_10_max
      value: 39.0688844845927
    - type: nauc_ndcg_at_1_diff1
      value: -13.560131212172575
    - type: nauc_ndcg_at_1_max
      value: 17.753684567169206
    - type: nauc_ndcg_at_20_diff1
      value: -8.582159015596881
    - type: nauc_ndcg_at_20_max
      value: 33.106491777127104
    - type: nauc_ndcg_at_3_diff1
      value: -6.39676867708739
    - type: nauc_ndcg_at_3_max
      value: 35.95467958722493
    - type: nauc_ndcg_at_5_diff1
      value: -8.853297663525334
    - type: nauc_ndcg_at_5_max
      value: 36.93824928813642
    - type: nauc_precision_at_1000_diff1
      value: -19.126005690414093
    - type: nauc_precision_at_1000_max
      value: 25.35047417077917
    - type: nauc_precision_at_100_diff1
      value: -18.97447376593622
    - type: nauc_precision_at_100_max
      value: 31.37636574830301
    - type: nauc_precision_at_10_diff1
      value: -8.160447388056866
    - type: nauc_precision_at_10_max
      value: 48.43344948807299
    - type: nauc_precision_at_1_diff1
      value: -13.92094533895383
    - type: nauc_precision_at_1_max
      value: 29.306889641351635
    - type: nauc_precision_at_20_diff1
      value: -9.369598971997679
    - type: nauc_precision_at_20_max
      value: 35.32023344220161
    - type: nauc_precision_at_3_diff1
      value: -2.1110502891686957
    - type: nauc_precision_at_3_max
      value: 45.669609919794304
    - type: nauc_precision_at_5_diff1
      value: -6.195574785037542
    - type: nauc_precision_at_5_max
      value: 46.58113806889752
    - type: nauc_recall_at_1000_diff1
      value: -7.222231464081126
    - type: nauc_recall_at_1000_max
      value: 29.974242681745476
    - type: nauc_recall_at_100_diff1
      value: -9.033068000256877
    - type: nauc_recall_at_100_max
      value: 26.59705019847799
    - type: nauc_recall_at_10_diff1
      value: -2.528142472559607
    - type: nauc_recall_at_10_max
      value: 26.835309548148146
    - type: nauc_recall_at_1_diff1
      value: -6.48595577983789
    - type: nauc_recall_at_1_max
      value: 2.3330438771924435
    - type: nauc_recall_at_20_diff1
      value: -3.6307369621295957
    - type: nauc_recall_at_20_max
      value: 20.070170533525516
    - type: nauc_recall_at_3_diff1
      value: 7.584755152275265
    - type: nauc_recall_at_3_max
      value: 25.752559205882235
    - type: nauc_recall_at_5_diff1
      value: 2.5491891310722266
    - type: nauc_recall_at_5_max
      value: 29.321004066680604
    - type: ndcg_at_1
      value: 61.0
    - type: ndcg_at_10
      value: 52.92
    - type: ndcg_at_100
      value: 44.021
    - type: ndcg_at_1000
      value: 47.164
    - type: ndcg_at_20
      value: 51.358000000000004
    - type: ndcg_at_3
      value: 55.05
    - type: ndcg_at_5
      value: 52.702000000000005
    - type: precision_at_1
      value: 68.0
    - type: precision_at_10
      value: 56.599999999999994
    - type: precision_at_100
      value: 45.660000000000004
    - type: precision_at_1000
      value: 21.756
    - type: precision_at_20
      value: 54.6
    - type: precision_at_3
      value: 58.667
    - type: precision_at_5
      value: 55.2
    - type: recall_at_1
      value: 0.185
    - type: recall_at_10
      value: 1.459
    - type: recall_at_100
      value: 11.053
    - type: recall_at_1000
      value: 46.711000000000006
    - type: recall_at_20
      value: 2.795
    - type: recall_at_3
      value: 0.447
    - type: recall_at_5
      value: 0.705
  - task:
      type: Retrieval
    dataset:
      type: mteb/touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
    metrics:
    - type: map_at_1
      value: 1.321
    - type: map_at_10
      value: 6.138
    - type: map_at_100
      value: 11.575000000000001
    - type: map_at_1000
      value: 13.142000000000001
    - type: map_at_20
      value: 8.277
    - type: map_at_3
      value: 3.117
    - type: map_at_5
      value: 4.322
    - type: mrr_at_1
      value: 18.367346938775512
    - type: mrr_at_10
      value: 32.81988986070618
    - type: mrr_at_100
      value: 33.90531120374521
    - type: mrr_at_1000
      value: 33.90531120374521
    - type: mrr_at_20
      value: 33.05798509880142
    - type: mrr_at_3
      value: 28.571428571428577
    - type: mrr_at_5
      value: 30.30612244897959
    - type: nauc_map_at_1000_diff1
      value: -12.650026713453016
    - type: nauc_map_at_1000_max
      value: -38.89899178585712
    - type: nauc_map_at_100_diff1
      value: -11.351425881232563
    - type: nauc_map_at_100_max
      value: -38.1084063615639
    - type: nauc_map_at_10_diff1
      value: -14.054275493851973
    - type: nauc_map_at_10_max
      value: -39.654901190516576
    - type: nauc_map_at_1_diff1
      value: -14.176844679266438
    - type: nauc_map_at_1_max
      value: -35.43233406535061
    - type: nauc_map_at_20_diff1
      value: -7.782883131410578
    - type: nauc_map_at_20_max
      value: -34.811736013580074
    - type: nauc_map_at_3_diff1
      value: -20.44134409811859
    - type: nauc_map_at_3_max
      value: -43.74179111772745
    - type: nauc_map_at_5_diff1
      value: -14.859493570845277
    - type: nauc_map_at_5_max
      value: -39.23961072955786
    - type: nauc_mrr_at_1000_diff1
      value: -20.089514178024398
    - type: nauc_mrr_at_1000_max
      value: -33.00720178570727
    - type: nauc_mrr_at_100_diff1
      value: -20.089514178024398
    - type: nauc_mrr_at_100_max
      value: -33.00720178570727
    - type: nauc_mrr_at_10_diff1
      value: -20.9446166904634
    - type: nauc_mrr_at_10_max
      value: -33.02192033292625
    - type: nauc_mrr_at_1_diff1
      value: -15.911220891245758
    - type: nauc_mrr_at_1_max
      value: -26.218283032718976
    - type: nauc_mrr_at_20_diff1
      value: -20.230803838354994
    - type: nauc_mrr_at_20_max
      value: -32.73210777421129
    - type: nauc_mrr_at_3_diff1
      value: -19.732723268458965
    - type: nauc_mrr_at_3_max
      value: -31.18864347028755
    - type: nauc_mrr_at_5_diff1
      value: -19.007764514449406
    - type: nauc_mrr_at_5_max
      value: -32.30329515402053
    - type: nauc_ndcg_at_1000_diff1
      value: -21.119533433583715
    - type: nauc_ndcg_at_1000_max
      value: -43.75261603824236
    - type: nauc_ndcg_at_100_diff1
      value: -24.303320372101975
    - type: nauc_ndcg_at_100_max
      value: -48.448935730363644
    - type: nauc_ndcg_at_10_diff1
      value: -18.50545573831141
    - type: nauc_ndcg_at_10_max
      value: -36.750080074249034
    - type: nauc_ndcg_at_1_diff1
      value: -10.113714494673975
    - type: nauc_ndcg_at_1_max
      value: -24.06470181107808
    - type: nauc_ndcg_at_20_diff1
      value: -14.291225537849158
    - type: nauc_ndcg_at_20_max
      value: -36.39732010219852
    - type: nauc_ndcg_at_3_diff1
      value: -17.343926323555642
    - type: nauc_ndcg_at_3_max
      value: -30.873097187690806
    - type: nauc_ndcg_at_5_diff1
      value: -17.628895004119695
    - type: nauc_ndcg_at_5_max
      value: -32.36698704574697
    - type: nauc_precision_at_1000_diff1
      value: 8.169456186810706
    - type: nauc_precision_at_1000_max
      value: 28.584039287780318
    - type: nauc_precision_at_100_diff1
      value: -31.96792574965573
    - type: nauc_precision_at_100_max
      value: -36.31964691177863
    - type: nauc_precision_at_10_diff1
      value: -21.750286138613905
    - type: nauc_precision_at_10_max
      value: -36.08986455494077
    - type: nauc_precision_at_1_diff1
      value: -15.911220891245758
    - type: nauc_precision_at_1_max
      value: -26.218283032718976
    - type: nauc_precision_at_20_diff1
      value: -13.583009329717136
    - type: nauc_precision_at_20_max
      value: -28.563248289076466
    - type: nauc_precision_at_3_diff1
      value: -22.309332363658
    - type: nauc_precision_at_3_max
      value: -34.3364478818448
    - type: nauc_precision_at_5_diff1
      value: -20.923667944175943
    - type: nauc_precision_at_5_max
      value: -35.18685578264413
    - type: nauc_recall_at_1000_diff1
      value: -15.680456983942094
    - type: nauc_recall_at_1000_max
      value: -44.754312719365174
    - type: nauc_recall_at_100_diff1
      value: -26.52205219781742
    - type: nauc_recall_at_100_max
      value: -54.5272192375575
    - type: nauc_recall_at_10_diff1
      value: -13.179833612683423
    - type: nauc_recall_at_10_max
      value: -39.41974472115443
    - type: nauc_recall_at_1_diff1
      value: -14.176844679266438
    - type: nauc_recall_at_1_max
      value: -35.43233406535061
    - type: nauc_recall_at_20_diff1
      value: -8.91943188201611
    - type: nauc_recall_at_20_max
      value: -34.5908793542195
    - type: nauc_recall_at_3_diff1
      value: -17.972433176642863
    - type: nauc_recall_at_3_max
      value: -41.2243455915633
    - type: nauc_recall_at_5_diff1
      value: -12.340791676500281
    - type: nauc_recall_at_5_max
      value: -36.85458567578151
    - type: ndcg_at_1
      value: 16.326999999999998
    - type: ndcg_at_10
      value: 16.762
    - type: ndcg_at_100
      value: 29.751
    - type: ndcg_at_1000
      value: 41.85
    - type: ndcg_at_20
      value: 18.541
    - type: ndcg_at_3
      value: 16.182
    - type: ndcg_at_5
      value: 15.792
    - type: precision_at_1
      value: 18.367
    - type: precision_at_10
      value: 17.347
    - type: precision_at_100
      value: 6.877999999999999
    - type: precision_at_1000
      value: 1.49
    - type: precision_at_20
      value: 13.469000000000001
    - type: precision_at_3
      value: 19.048000000000002
    - type: precision_at_5
      value: 17.551
    - type: recall_at_1
      value: 1.321
    - type: recall_at_10
      value: 12.25
    - type: recall_at_100
      value: 44.012
    - type: recall_at_1000
      value: 80.706
    - type: recall_at_20
      value: 19.094
    - type: recall_at_3
      value: 4.2909999999999995
    - type: recall_at_5
      value: 6.802999999999999
  - task:
      type: Classification
    dataset:
      type: mteb/toxic_conversations_50k
      name: MTEB ToxicConversationsClassification
      config: default
      split: test
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
    metrics:
    - type: accuracy
      value: 65.56640625
    - type: ap
      value: 12.336183192628836
    - type: ap_weighted
      value: 12.336183192628836
    - type: f1
      value: 50.61953920605424
    - type: f1_weighted
      value: 73.10180241141433
  - task:
      type: Classification
    dataset:
      type: mteb/tweet_sentiment_extraction
      name: MTEB TweetSentimentExtractionClassification
      config: default
      split: test
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
    metrics:
    - type: accuracy
      value: 62.80418788907753
    - type: f1
      value: 63.050557758931134
    - type: f1_weighted
      value: 62.13337985337418
  - task:
      type: Clustering
    dataset:
      type: mteb/twentynewsgroups-clustering
      name: MTEB TwentyNewsgroupsClustering
      config: default
      split: test
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
    metrics:
    - type: v_measure
      value: 49.00618373985209
    - type: v_measures
      value: [0.49421217801171224, 0.4740440424893081, 0.4886726035776056, 0.5198976504195676, 0.4827070012054274]
  - task:
      type: PairClassification
    dataset:
      type: mteb/twittersemeval2015-pairclassification
      name: MTEB TwitterSemEval2015
      config: default
      split: test
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
    metrics:
    - type: cos_sim_accuracy
      value: 86.97025689932646
    - type: cos_sim_ap
      value: 77.06565012359437
    - type: cos_sim_f1
      value: 70.32217308907138
    - type: cos_sim_precision
      value: 67.46666666666667
    - type: cos_sim_recall
      value: 73.43007915567283
    - type: dot_accuracy
      value: 86.97025689932646
    - type: dot_ap
      value: 77.0656524331512
    - type: dot_f1
      value: 70.32217308907138
    - type: dot_precision
      value: 67.46666666666667
    - type: dot_recall
      value: 73.43007915567283
    - type: euclidean_accuracy
      value: 86.97025689932646
    - type: euclidean_ap
      value: 77.06564828845742
    - type: euclidean_f1
      value: 70.32217308907138
    - type: euclidean_precision
      value: 67.46666666666667
    - type: euclidean_recall
      value: 73.43007915567283
    - type: manhattan_accuracy
      value: 86.90469094593789
    - type: manhattan_ap
      value: 76.94347285253252
    - type: manhattan_f1
      value: 70.18523217457499
    - type: manhattan_precision
      value: 67.59530791788856
    - type: manhattan_recall
      value: 72.98153034300792
    - type: max_accuracy
      value: 86.97025689932646
    - type: max_ap
      value: 77.0656524331512
    - type: max_f1
      value: 70.32217308907138
  - task:
      type: PairClassification
    dataset:
      type: mteb/twitterurlcorpus-pairclassification
      name: MTEB TwitterURLCorpus
      config: default
      split: test
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
    metrics:
    - type: cos_sim_accuracy
      value: 89.64567081926495
    - type: cos_sim_ap
      value: 87.19162831580245
    - type: cos_sim_f1
      value: 79.67696578577352
    - type: cos_sim_precision
      value: 74.92033358193775
    - type: cos_sim_recall
      value: 85.07853403141361
    - type: dot_accuracy
      value: 89.64567081926495
    - type: dot_ap
      value: 87.19162304433766
    - type: dot_f1
      value: 79.67696578577352
    - type: dot_precision
      value: 74.92033358193775
    - type: dot_recall
      value: 85.07853403141361
    - type: euclidean_accuracy
      value: 89.64567081926495
    - type: euclidean_ap
      value: 87.19162847931055
    - type: euclidean_f1
      value: 79.67696578577352
    - type: euclidean_precision
      value: 74.92033358193775
    - type: euclidean_recall
      value: 85.07853403141361
    - type: manhattan_accuracy
      value: 89.67283735009897
    - type: manhattan_ap
      value: 87.19033616510255
    - type: manhattan_f1
      value: 79.67444226437031
    - type: manhattan_precision
      value: 75.43690656391908
    - type: manhattan_recall
      value: 84.41638435478903
    - type: max_accuracy
      value: 89.67283735009897
    - type: max_ap
      value: 87.19162847931055
    - type: max_f1
      value: 79.67696578577352
license: apache-2.0
language:
    - fr
    - en
---

# [bilingual-embedding-large](https://huggingface.co/Lajavaness/bilingual-embedding-large)

Bilingual-embedding is the Embedding Model for bilingual language: french and english. This model is a specialized sentence-embedding trained specifically for the bilingual language, leveraging the robust capabilities of [XLM-RoBERTa](https://huggingface.co/FacebookAI/xlm-roberta-large), a pre-trained language model based on the [XLM-RoBERTa](https://huggingface.co/FacebookAI/xlm-roberta-large) architecture. The model utilizes xlm-roberta to encode english-french sentences into a 1024-dimensional vector space, facilitating a wide range of applications from semantic search to text clustering. The embeddings capture the nuanced meanings of english-french sentences, reflecting both the lexical and contextual layers of the language.


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BilingualModel 
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Training and Fine-tuning process
#### Stage 1: NLI Training
- Dataset: [(SNLI+XNLI) for english+french]
- Method: Training using Multi-Negative Ranking Loss. This stage focused on improving the model's ability to discern and rank nuanced differences in sentence semantics.
### Stage 3: Continued Fine-tuning for Semantic Textual Similarity on STS Benchmark
- Dataset: [STSB-fr and en]
- Method: Fine-tuning specifically for the semantic textual similarity benchmark using Siamese BERT-Networks configured with the 'sentence-transformers' library. 
### Stage 4: Advanced Augmentation Fine-tuning
- Dataset: STSB with generate [silver sample from gold sample](https://www.sbert.net/examples/training/data_augmentation/README.html)
- Method: Employed an advanced strategy using [Augmented SBERT](https://arxiv.org/abs/2010.08240) with Pair Sampling Strategies, integrating both Cross-Encoder and Bi-Encoder models. This stage further refined the embeddings by enriching the training data dynamically, enhancing the model's robustness and accuracy.


## Usage:

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer

sentences = ["Paris est une capitale de la France", "Paris is a capital of France"]

model = SentenceTransformer('Lajavaness/bilingual-embedding-large', trust_remote_code=True)
print(embeddings)

```





## Evaluation

TODO

## Citation

    @article{conneau2019unsupervised,
      title={Unsupervised cross-lingual representation learning at scale},
      author={Conneau, Alexis and Khandelwal, Kartikay and Goyal, Naman and Chaudhary, Vishrav and Wenzek, Guillaume and Guzm{\'a}n, Francisco and Grave, Edouard and Ott, Myle and Zettlemoyer, Luke and Stoyanov, Veselin},
      journal={arXiv preprint arXiv:1911.02116},
      year={2019}
    }

	@article{reimers2019sentence,
	   title={Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks},
	   author={Nils Reimers, Iryna Gurevych},
	   journal={https://arxiv.org/abs/1908.10084},
	   year={2019}
	}

    @article{thakur2020augmented,
      title={Augmented SBERT: Data Augmentation Method for Improving Bi-Encoders for Pairwise Sentence Scoring Tasks},
      author={Thakur, Nandan and Reimers, Nils and Daxenberger, Johannes and Gurevych, Iryna},
      journal={arXiv e-prints},
      pages={arXiv--2010},
      year={2020}