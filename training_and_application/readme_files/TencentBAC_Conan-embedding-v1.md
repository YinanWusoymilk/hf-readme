---
tags:
- mteb
model-index:
- name: conan-embedding
  results:
  - task:
      type: STS
    dataset:
      type: C-MTEB/AFQMC
      name: MTEB AFQMC
      config: default
      split: validation
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 56.613572467148856
    - type: cos_sim_spearman
      value: 60.66446211824284
    - type: euclidean_pearson
      value: 58.42080485872613
    - type: euclidean_spearman
      value: 59.82750030458164
    - type: manhattan_pearson
      value: 58.39885271199772
    - type: manhattan_spearman
      value: 59.817749720366734
  - task:
      type: STS
    dataset:
      type: C-MTEB/ATEC
      name: MTEB ATEC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 56.60530380552331
    - type: cos_sim_spearman
      value: 58.63822441736707
    - type: euclidean_pearson
      value: 62.18551665180664
    - type: euclidean_spearman
      value: 58.23168804495912
    - type: manhattan_pearson
      value: 62.17191480770053
    - type: manhattan_spearman
      value: 58.22556219601401
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (zh)
      config: zh
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 50.308
    - type: f1
      value: 46.927458607895126
  - task:
      type: STS
    dataset:
      type: C-MTEB/BQ
      name: MTEB BQ
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 72.6472074172711
    - type: cos_sim_spearman
      value: 74.50748447236577
    - type: euclidean_pearson
      value: 72.51833296451854
    - type: euclidean_spearman
      value: 73.9898922606105
    - type: manhattan_pearson
      value: 72.50184948939338
    - type: manhattan_spearman
      value: 73.97797921509638
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/CLSClusteringP2P
      name: MTEB CLSClusteringP2P
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 60.63545326048343
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/CLSClusteringS2S
      name: MTEB CLSClusteringS2S
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 52.64834762325994
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/CMedQAv1-reranking
      name: MTEB CMedQAv1
      config: default
      split: test
      revision: None
    metrics:
    - type: map
      value: 91.38528814655234
    - type: mrr
      value: 93.35857142857144
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/CMedQAv2-reranking
      name: MTEB CMedQAv2
      config: default
      split: test
      revision: None
    metrics:
    - type: map
      value: 89.72084678877096
    - type: mrr
      value: 91.74380952380953
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CmedqaRetrieval
      name: MTEB CmedqaRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 26.987
    - type: map_at_10
      value: 40.675
    - type: map_at_100
      value: 42.495
    - type: map_at_1000
      value: 42.596000000000004
    - type: map_at_3
      value: 36.195
    - type: map_at_5
      value: 38.704
    - type: mrr_at_1
      value: 41.21
    - type: mrr_at_10
      value: 49.816
    - type: mrr_at_100
      value: 50.743
    - type: mrr_at_1000
      value: 50.77700000000001
    - type: mrr_at_3
      value: 47.312
    - type: mrr_at_5
      value: 48.699999999999996
    - type: ndcg_at_1
      value: 41.21
    - type: ndcg_at_10
      value: 47.606
    - type: ndcg_at_100
      value: 54.457
    - type: ndcg_at_1000
      value: 56.16100000000001
    - type: ndcg_at_3
      value: 42.108000000000004
    - type: ndcg_at_5
      value: 44.393
    - type: precision_at_1
      value: 41.21
    - type: precision_at_10
      value: 10.593
    - type: precision_at_100
      value: 1.609
    - type: precision_at_1000
      value: 0.183
    - type: precision_at_3
      value: 23.881
    - type: precision_at_5
      value: 17.339
    - type: recall_at_1
      value: 26.987
    - type: recall_at_10
      value: 58.875
    - type: recall_at_100
      value: 87.023
    - type: recall_at_1000
      value: 98.328
    - type: recall_at_3
      value: 42.265
    - type: recall_at_5
      value: 49.334
  - task:
      type: PairClassification
    dataset:
      type: C-MTEB/CMNLI
      name: MTEB Cmnli
      config: default
      split: validation
      revision: None
    metrics:
    - type: cos_sim_accuracy
      value: 85.91701743836441
    - type: cos_sim_ap
      value: 92.53650618807644
    - type: cos_sim_f1
      value: 86.80265975431082
    - type: cos_sim_precision
      value: 83.79025239338556
    - type: cos_sim_recall
      value: 90.039747486556
    - type: dot_accuracy
      value: 77.17378232110643
    - type: dot_ap
      value: 85.40244368166546
    - type: dot_f1
      value: 79.03038001481951
    - type: dot_precision
      value: 72.20502901353966
    - type: dot_recall
      value: 87.2808043020809
    - type: euclidean_accuracy
      value: 84.65423932651834
    - type: euclidean_ap
      value: 91.47775530034588
    - type: euclidean_f1
      value: 85.64471499723298
    - type: euclidean_precision
      value: 81.31567885666246
    - type: euclidean_recall
      value: 90.46060322656068
    - type: manhattan_accuracy
      value: 84.58208057726999
    - type: manhattan_ap
      value: 91.46228709402014
    - type: manhattan_f1
      value: 85.6631626034444
    - type: manhattan_precision
      value: 82.10075026795283
    - type: manhattan_recall
      value: 89.5487491232172
    - type: max_accuracy
      value: 85.91701743836441
    - type: max_ap
      value: 92.53650618807644
    - type: max_f1
      value: 86.80265975431082
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CovidRetrieval
      name: MTEB CovidRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 83.693
    - type: map_at_10
      value: 90.098
    - type: map_at_100
      value: 90.145
    - type: map_at_1000
      value: 90.146
    - type: map_at_3
      value: 89.445
    - type: map_at_5
      value: 89.935
    - type: mrr_at_1
      value: 83.878
    - type: mrr_at_10
      value: 90.007
    - type: mrr_at_100
      value: 90.045
    - type: mrr_at_1000
      value: 90.046
    - type: mrr_at_3
      value: 89.34
    - type: mrr_at_5
      value: 89.835
    - type: ndcg_at_1
      value: 84.089
    - type: ndcg_at_10
      value: 92.351
    - type: ndcg_at_100
      value: 92.54599999999999
    - type: ndcg_at_1000
      value: 92.561
    - type: ndcg_at_3
      value: 91.15299999999999
    - type: ndcg_at_5
      value: 91.968
    - type: precision_at_1
      value: 84.089
    - type: precision_at_10
      value: 10.011000000000001
    - type: precision_at_100
      value: 1.009
    - type: precision_at_1000
      value: 0.101
    - type: precision_at_3
      value: 32.28
    - type: precision_at_5
      value: 19.789
    - type: recall_at_1
      value: 83.693
    - type: recall_at_10
      value: 99.05199999999999
    - type: recall_at_100
      value: 99.895
    - type: recall_at_1000
      value: 100
    - type: recall_at_3
      value: 95.917
    - type: recall_at_5
      value: 97.893
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/DuRetrieval
      name: MTEB DuRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 26.924
    - type: map_at_10
      value: 81.392
    - type: map_at_100
      value: 84.209
    - type: map_at_1000
      value: 84.237
    - type: map_at_3
      value: 56.998000000000005
    - type: map_at_5
      value: 71.40100000000001
    - type: mrr_at_1
      value: 91.75
    - type: mrr_at_10
      value: 94.45
    - type: mrr_at_100
      value: 94.503
    - type: mrr_at_1000
      value: 94.505
    - type: mrr_at_3
      value: 94.258
    - type: mrr_at_5
      value: 94.381
    - type: ndcg_at_1
      value: 91.75
    - type: ndcg_at_10
      value: 88.53
    - type: ndcg_at_100
      value: 91.13900000000001
    - type: ndcg_at_1000
      value: 91.387
    - type: ndcg_at_3
      value: 87.925
    - type: ndcg_at_5
      value: 86.461
    - type: precision_at_1
      value: 91.75
    - type: precision_at_10
      value: 42.05
    - type: precision_at_100
      value: 4.827
    - type: precision_at_1000
      value: 0.48900000000000005
    - type: precision_at_3
      value: 78.55
    - type: precision_at_5
      value: 65.82000000000001
    - type: recall_at_1
      value: 26.924
    - type: recall_at_10
      value: 89.338
    - type: recall_at_100
      value: 97.856
    - type: recall_at_1000
      value: 99.11
    - type: recall_at_3
      value: 59.202999999999996
    - type: recall_at_5
      value: 75.642
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/EcomRetrieval
      name: MTEB EcomRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 54.800000000000004
    - type: map_at_10
      value: 65.613
    - type: map_at_100
      value: 66.185
    - type: map_at_1000
      value: 66.191
    - type: map_at_3
      value: 62.8
    - type: map_at_5
      value: 64.535
    - type: mrr_at_1
      value: 54.800000000000004
    - type: mrr_at_10
      value: 65.613
    - type: mrr_at_100
      value: 66.185
    - type: mrr_at_1000
      value: 66.191
    - type: mrr_at_3
      value: 62.8
    - type: mrr_at_5
      value: 64.535
    - type: ndcg_at_1
      value: 54.800000000000004
    - type: ndcg_at_10
      value: 70.991
    - type: ndcg_at_100
      value: 73.434
    - type: ndcg_at_1000
      value: 73.587
    - type: ndcg_at_3
      value: 65.324
    - type: ndcg_at_5
      value: 68.431
    - type: precision_at_1
      value: 54.800000000000004
    - type: precision_at_10
      value: 8.790000000000001
    - type: precision_at_100
      value: 0.9860000000000001
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 24.2
    - type: precision_at_5
      value: 16.02
    - type: recall_at_1
      value: 54.800000000000004
    - type: recall_at_10
      value: 87.9
    - type: recall_at_100
      value: 98.6
    - type: recall_at_1000
      value: 99.8
    - type: recall_at_3
      value: 72.6
    - type: recall_at_5
      value: 80.10000000000001
  - task:
      type: Classification
    dataset:
      type: C-MTEB/IFlyTek-classification
      name: MTEB IFlyTek
      config: default
      split: validation
      revision: None
    metrics:
    - type: accuracy
      value: 51.94305502116199
    - type: f1
      value: 39.82197338426721
  - task:
      type: Classification
    dataset:
      type: C-MTEB/JDReview-classification
      name: MTEB JDReview
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 90.31894934333957
    - type: ap
      value: 63.89821836499594
    - type: f1
      value: 85.93687177603624
  - task:
      type: STS
    dataset:
      type: C-MTEB/LCQMC
      name: MTEB LCQMC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 73.18906216730208
    - type: cos_sim_spearman
      value: 79.44570226735877
    - type: euclidean_pearson
      value: 78.8105072242798
    - type: euclidean_spearman
      value: 79.15605680863212
    - type: manhattan_pearson
      value: 78.80576507484064
    - type: manhattan_spearman
      value: 79.14625534068364
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/Mmarco-reranking
      name: MTEB MMarcoReranking
      config: default
      split: dev
      revision: None
    metrics:
    - type: map
      value: 41.58107192600853
    - type: mrr
      value: 41.37063492063492
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MMarcoRetrieval
      name: MTEB MMarcoRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 68.33
    - type: map_at_10
      value: 78.261
    - type: map_at_100
      value: 78.522
    - type: map_at_1000
      value: 78.527
    - type: map_at_3
      value: 76.236
    - type: map_at_5
      value: 77.557
    - type: mrr_at_1
      value: 70.602
    - type: mrr_at_10
      value: 78.779
    - type: mrr_at_100
      value: 79.00500000000001
    - type: mrr_at_1000
      value: 79.01
    - type: mrr_at_3
      value: 77.037
    - type: mrr_at_5
      value: 78.157
    - type: ndcg_at_1
      value: 70.602
    - type: ndcg_at_10
      value: 82.254
    - type: ndcg_at_100
      value: 83.319
    - type: ndcg_at_1000
      value: 83.449
    - type: ndcg_at_3
      value: 78.46
    - type: ndcg_at_5
      value: 80.679
    - type: precision_at_1
      value: 70.602
    - type: precision_at_10
      value: 9.989
    - type: precision_at_100
      value: 1.05
    - type: precision_at_1000
      value: 0.106
    - type: precision_at_3
      value: 29.598999999999997
    - type: precision_at_5
      value: 18.948
    - type: recall_at_1
      value: 68.33
    - type: recall_at_10
      value: 94.00800000000001
    - type: recall_at_100
      value: 98.589
    - type: recall_at_1000
      value: 99.60799999999999
    - type: recall_at_3
      value: 84.057
    - type: recall_at_5
      value: 89.32900000000001
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (zh-CN)
      config: zh-CN
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 78.13718897108272
    - type: f1
      value: 74.07613180855328
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (zh-CN)
      config: zh-CN
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 86.20040349697376
    - type: f1
      value: 85.05282136519973
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MedicalRetrieval
      name: MTEB MedicalRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 56.8
    - type: map_at_10
      value: 64.199
    - type: map_at_100
      value: 64.89
    - type: map_at_1000
      value: 64.917
    - type: map_at_3
      value: 62.383
    - type: map_at_5
      value: 63.378
    - type: mrr_at_1
      value: 56.8
    - type: mrr_at_10
      value: 64.199
    - type: mrr_at_100
      value: 64.89
    - type: mrr_at_1000
      value: 64.917
    - type: mrr_at_3
      value: 62.383
    - type: mrr_at_5
      value: 63.378
    - type: ndcg_at_1
      value: 56.8
    - type: ndcg_at_10
      value: 67.944
    - type: ndcg_at_100
      value: 71.286
    - type: ndcg_at_1000
      value: 71.879
    - type: ndcg_at_3
      value: 64.163
    - type: ndcg_at_5
      value: 65.96600000000001
    - type: precision_at_1
      value: 56.8
    - type: precision_at_10
      value: 7.9799999999999995
    - type: precision_at_100
      value: 0.954
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 23.1
    - type: precision_at_5
      value: 14.74
    - type: recall_at_1
      value: 56.8
    - type: recall_at_10
      value: 79.80000000000001
    - type: recall_at_100
      value: 95.39999999999999
    - type: recall_at_1000
      value: 99.8
    - type: recall_at_3
      value: 69.3
    - type: recall_at_5
      value: 73.7
  - task:
      type: Classification
    dataset:
      type: C-MTEB/MultilingualSentiment-classification
      name: MTEB MultilingualSentiment
      config: default
      split: validation
      revision: None
    metrics:
    - type: accuracy
      value: 78.57666666666667
    - type: f1
      value: 78.23373528202681
  - task:
      type: PairClassification
    dataset:
      type: C-MTEB/OCNLI
      name: MTEB Ocnli
      config: default
      split: validation
      revision: None
    metrics:
    - type: cos_sim_accuracy
      value: 85.43584190579317
    - type: cos_sim_ap
      value: 90.76665640338129
    - type: cos_sim_f1
      value: 86.5021770682148
    - type: cos_sim_precision
      value: 79.82142857142858
    - type: cos_sim_recall
      value: 94.40337909186906
    - type: dot_accuracy
      value: 78.66811044937737
    - type: dot_ap
      value: 85.84084363880804
    - type: dot_f1
      value: 80.10075566750629
    - type: dot_precision
      value: 76.58959537572254
    - type: dot_recall
      value: 83.9493136219641
    - type: euclidean_accuracy
      value: 84.46128857606931
    - type: euclidean_ap
      value: 88.62351100230491
    - type: euclidean_f1
      value: 85.7709469509172
    - type: euclidean_precision
      value: 80.8411214953271
    - type: euclidean_recall
      value: 91.34107708553326
    - type: manhattan_accuracy
      value: 84.51543042772063
    - type: manhattan_ap
      value: 88.53975607870393
    - type: manhattan_f1
      value: 85.75697211155378
    - type: manhattan_precision
      value: 81.14985862393968
    - type: manhattan_recall
      value: 90.91869060190075
    - type: max_accuracy
      value: 85.43584190579317
    - type: max_ap
      value: 90.76665640338129
    - type: max_f1
      value: 86.5021770682148
  - task:
      type: Classification
    dataset:
      type: C-MTEB/OnlineShopping-classification
      name: MTEB OnlineShopping
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 95.06999999999998
    - type: ap
      value: 93.45104559324996
    - type: f1
      value: 95.06036329426092
  - task:
      type: STS
    dataset:
      type: C-MTEB/PAWSX
      name: MTEB PAWSX
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 40.01998290519605
    - type: cos_sim_spearman
      value: 46.5989769986853
    - type: euclidean_pearson
      value: 45.37905883182924
    - type: euclidean_spearman
      value: 46.22213849806378
    - type: manhattan_pearson
      value: 45.40925124776211
    - type: manhattan_spearman
      value: 46.250705124226386
  - task:
      type: STS
    dataset:
      type: C-MTEB/QBQTC
      name: MTEB QBQTC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 42.719516197112526
    - type: cos_sim_spearman
      value: 44.57507789581106
    - type: euclidean_pearson
      value: 35.73062264160721
    - type: euclidean_spearman
      value: 40.473523909913695
    - type: manhattan_pearson
      value: 35.69868964086357
    - type: manhattan_spearman
      value: 40.46349925372903
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (zh)
      config: zh
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 62.340118285801104
    - type: cos_sim_spearman
      value: 67.72781908620632
    - type: euclidean_pearson
      value: 63.161965746091596
    - type: euclidean_spearman
      value: 67.36825684340769
    - type: manhattan_pearson
      value: 63.089863788261425
    - type: manhattan_spearman
      value: 67.40868898995384
  - task:
      type: STS
    dataset:
      type: C-MTEB/STSB
      name: MTEB STSB
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 79.1646360962365
    - type: cos_sim_spearman
      value: 81.24426700767087
    - type: euclidean_pearson
      value: 79.43826409936123
    - type: euclidean_spearman
      value: 79.71787965300125
    - type: manhattan_pearson
      value: 79.43377784961737
    - type: manhattan_spearman
      value: 79.69348376886967
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/T2Reranking
      name: MTEB T2Reranking
      config: default
      split: dev
      revision: None
    metrics:
    - type: map
      value: 68.35595092507496
    - type: mrr
      value: 79.00244892585788
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/T2Retrieval
      name: MTEB T2Retrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 26.588
    - type: map_at_10
      value: 75.327
    - type: map_at_100
      value: 79.095
    - type: map_at_1000
      value: 79.163
    - type: map_at_3
      value: 52.637
    - type: map_at_5
      value: 64.802
    - type: mrr_at_1
      value: 88.103
    - type: mrr_at_10
      value: 91.29899999999999
    - type: mrr_at_100
      value: 91.408
    - type: mrr_at_1000
      value: 91.411
    - type: mrr_at_3
      value: 90.801
    - type: mrr_at_5
      value: 91.12700000000001
    - type: ndcg_at_1
      value: 88.103
    - type: ndcg_at_10
      value: 83.314
    - type: ndcg_at_100
      value: 87.201
    - type: ndcg_at_1000
      value: 87.83999999999999
    - type: ndcg_at_3
      value: 84.408
    - type: ndcg_at_5
      value: 83.078
    - type: precision_at_1
      value: 88.103
    - type: precision_at_10
      value: 41.638999999999996
    - type: precision_at_100
      value: 5.006
    - type: precision_at_1000
      value: 0.516
    - type: precision_at_3
      value: 73.942
    - type: precision_at_5
      value: 62.056
    - type: recall_at_1
      value: 26.588
    - type: recall_at_10
      value: 82.819
    - type: recall_at_100
      value: 95.334
    - type: recall_at_1000
      value: 98.51299999999999
    - type: recall_at_3
      value: 54.74
    - type: recall_at_5
      value: 68.864
  - task:
      type: Classification
    dataset:
      type: C-MTEB/TNews-classification
      name: MTEB TNews
      config: default
      split: validation
      revision: None
    metrics:
    - type: accuracy
      value: 55.029
    - type: f1
      value: 53.043617905026764
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/ThuNewsClusteringP2P
      name: MTEB ThuNewsClusteringP2P
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 77.83675116835911
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/ThuNewsClusteringS2S
      name: MTEB ThuNewsClusteringS2S
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 74.19701455865277
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/VideoRetrieval
      name: MTEB VideoRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 64.7
    - type: map_at_10
      value: 75.593
    - type: map_at_100
      value: 75.863
    - type: map_at_1000
      value: 75.863
    - type: map_at_3
      value: 73.63300000000001
    - type: map_at_5
      value: 74.923
    - type: mrr_at_1
      value: 64.7
    - type: mrr_at_10
      value: 75.593
    - type: mrr_at_100
      value: 75.863
    - type: mrr_at_1000
      value: 75.863
    - type: mrr_at_3
      value: 73.63300000000001
    - type: mrr_at_5
      value: 74.923
    - type: ndcg_at_1
      value: 64.7
    - type: ndcg_at_10
      value: 80.399
    - type: ndcg_at_100
      value: 81.517
    - type: ndcg_at_1000
      value: 81.517
    - type: ndcg_at_3
      value: 76.504
    - type: ndcg_at_5
      value: 78.79899999999999
    - type: precision_at_1
      value: 64.7
    - type: precision_at_10
      value: 9.520000000000001
    - type: precision_at_100
      value: 1
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 28.266999999999996
    - type: precision_at_5
      value: 18.060000000000002
    - type: recall_at_1
      value: 64.7
    - type: recall_at_10
      value: 95.19999999999999
    - type: recall_at_100
      value: 100
    - type: recall_at_1000
      value: 100
    - type: recall_at_3
      value: 84.8
    - type: recall_at_5
      value: 90.3
  - task:
      type: Classification
    dataset:
      type: C-MTEB/waimai-classification
      name: MTEB Waimai
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 89.69999999999999
    - type: ap
      value: 75.91371640164184
    - type: f1
      value: 88.34067777698694
license: cc-by-nc-4.0
library_name: sentence-transformers
---

# Conan-embedding-v1

## Performance

| Model                 | **Average** | **CLS**   | **Clustering** | **Reranking** | **Retrieval** | **STS**   | **Pair_CLS** |
| :-------------------: | :---------: | :-------: | :------------: | :-----------: | :-----------: | :-------: | :----------: |
| gte-Qwen2-7B-instruct | 72.05       | 75.09     | 66.06          | 68.92         | 76.03         | 65.33     | 87.48        |
| xiaobu-embedding-v2   | 72.43       | 74.67     | 65.17          | 72.58         | 76.5          | 64.53     | 91.87        |
| **Conan-embedding-v1** | **72.62**  | 75.03     | 66.33          | 72.76         | 76.67         | 64.18     | 91.66        |


## Methods and Training Detials

Please refer to our [technical report](https://arxiv.org/abs/2408.15710).

## Citation

If you find our models / papers useful in your research, please consider giving ❤️ and citations. Thanks!

```
@misc{li2024conanembeddinggeneraltextembedding,
  title={Conan-embedding: General Text Embedding with More and Better Negative Samples}, 
  author={Shiyu Li and Yang Tang and Shizhe Chen and Xi Chen},
  year={2024},
  eprint={2408.15710},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2408.15710}, 
}
```

---

**About**

Created by the Tencent BAC Group. All rights reserved.

**License**

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).