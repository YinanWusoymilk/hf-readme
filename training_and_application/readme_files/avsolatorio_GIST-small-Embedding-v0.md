---
language:
- en
library_name: sentence-transformers
license: mit
pipeline_tag: sentence-similarity
tags:
  - feature-extraction
  - mteb
  - sentence-similarity
  - sentence-transformers

model-index:
- name: GIST-small-Embedding-v0
  results:
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
      value: 75.26865671641791
    - type: ap
      value: 38.25623793370476
    - type: f1
      value: 69.26434651320257
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
      value: 93.232225
    - type: ap
      value: 89.97936072879344
    - type: f1
      value: 93.22122653806187
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
      value: 49.715999999999994
    - type: f1
      value: 49.169789920136076
  - task:
      type: Retrieval
    dataset:
      type: arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 34.922
    - type: map_at_10
      value: 50.524
    - type: map_at_100
      value: 51.247
    - type: map_at_1000
      value: 51.249
    - type: map_at_3
      value: 45.887
    - type: map_at_5
      value: 48.592999999999996
    - type: mrr_at_1
      value: 34.922
    - type: mrr_at_10
      value: 50.382000000000005
    - type: mrr_at_100
      value: 51.104000000000006
    - type: mrr_at_1000
      value: 51.105999999999995
    - type: mrr_at_3
      value: 45.733000000000004
    - type: mrr_at_5
      value: 48.428
    - type: ndcg_at_1
      value: 34.922
    - type: ndcg_at_10
      value: 59.12
    - type: ndcg_at_100
      value: 62.083999999999996
    - type: ndcg_at_1000
      value: 62.137
    - type: ndcg_at_3
      value: 49.616
    - type: ndcg_at_5
      value: 54.501
    - type: precision_at_1
      value: 34.922
    - type: precision_at_10
      value: 8.649
    - type: precision_at_100
      value: 0.991
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 20.152
    - type: precision_at_5
      value: 14.466999999999999
    - type: recall_at_1
      value: 34.922
    - type: recall_at_10
      value: 86.48599999999999
    - type: recall_at_100
      value: 99.14699999999999
    - type: recall_at_1000
      value: 99.57300000000001
    - type: recall_at_3
      value: 60.455000000000005
    - type: recall_at_5
      value: 72.333
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
      value: 47.623282347623714
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
      value: 39.86487843524932
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
      value: 62.3290291318171
    - type: mrr
      value: 75.2379853141626
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
      value: 88.52002953574285
    - type: cos_sim_spearman
      value: 86.98752423842483
    - type: euclidean_pearson
      value: 86.89442688314197
    - type: euclidean_spearman
      value: 86.88631711307471
    - type: manhattan_pearson
      value: 87.03723618507175
    - type: manhattan_spearman
      value: 86.76041062975224
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
      value: 86.64935064935065
    - type: f1
      value: 86.61903824934998
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
      value: 39.21904455377494
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
      value: 35.43342755570654
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 31.843
    - type: map_at_10
      value: 43.379
    - type: map_at_100
      value: 44.946999999999996
    - type: map_at_1000
      value: 45.078
    - type: map_at_3
      value: 39.598
    - type: map_at_5
      value: 41.746
    - type: mrr_at_1
      value: 39.199
    - type: mrr_at_10
      value: 49.672
    - type: mrr_at_100
      value: 50.321000000000005
    - type: mrr_at_1000
      value: 50.365
    - type: mrr_at_3
      value: 46.805
    - type: mrr_at_5
      value: 48.579
    - type: ndcg_at_1
      value: 39.199
    - type: ndcg_at_10
      value: 50.163999999999994
    - type: ndcg_at_100
      value: 55.418
    - type: ndcg_at_1000
      value: 57.353
    - type: ndcg_at_3
      value: 44.716
    - type: ndcg_at_5
      value: 47.268
    - type: precision_at_1
      value: 39.199
    - type: precision_at_10
      value: 9.757
    - type: precision_at_100
      value: 1.552
    - type: precision_at_1000
      value: 0.20500000000000002
    - type: precision_at_3
      value: 21.602
    - type: precision_at_5
      value: 15.479000000000001
    - type: recall_at_1
      value: 31.843
    - type: recall_at_10
      value: 62.743
    - type: recall_at_100
      value: 84.78099999999999
    - type: recall_at_1000
      value: 96.86099999999999
    - type: recall_at_3
      value: 46.927
    - type: recall_at_5
      value: 54.355
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 29.321
    - type: map_at_10
      value: 39.062999999999995
    - type: map_at_100
      value: 40.403
    - type: map_at_1000
      value: 40.534
    - type: map_at_3
      value: 36.367
    - type: map_at_5
      value: 37.756
    - type: mrr_at_1
      value: 35.987
    - type: mrr_at_10
      value: 44.708999999999996
    - type: mrr_at_100
      value: 45.394
    - type: mrr_at_1000
      value: 45.436
    - type: mrr_at_3
      value: 42.463
    - type: mrr_at_5
      value: 43.663000000000004
    - type: ndcg_at_1
      value: 35.987
    - type: ndcg_at_10
      value: 44.585
    - type: ndcg_at_100
      value: 49.297999999999995
    - type: ndcg_at_1000
      value: 51.315
    - type: ndcg_at_3
      value: 40.569
    - type: ndcg_at_5
      value: 42.197
    - type: precision_at_1
      value: 35.987
    - type: precision_at_10
      value: 8.369
    - type: precision_at_100
      value: 1.366
    - type: precision_at_1000
      value: 0.184
    - type: precision_at_3
      value: 19.427
    - type: precision_at_5
      value: 13.58
    - type: recall_at_1
      value: 29.321
    - type: recall_at_10
      value: 54.333
    - type: recall_at_100
      value: 74.178
    - type: recall_at_1000
      value: 86.732
    - type: recall_at_3
      value: 42.46
    - type: recall_at_5
      value: 47.089999999999996
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 38.811
    - type: map_at_10
      value: 51.114000000000004
    - type: map_at_100
      value: 52.22
    - type: map_at_1000
      value: 52.275000000000006
    - type: map_at_3
      value: 47.644999999999996
    - type: map_at_5
      value: 49.675000000000004
    - type: mrr_at_1
      value: 44.389
    - type: mrr_at_10
      value: 54.459
    - type: mrr_at_100
      value: 55.208999999999996
    - type: mrr_at_1000
      value: 55.239000000000004
    - type: mrr_at_3
      value: 51.954
    - type: mrr_at_5
      value: 53.571999999999996
    - type: ndcg_at_1
      value: 44.389
    - type: ndcg_at_10
      value: 56.979
    - type: ndcg_at_100
      value: 61.266
    - type: ndcg_at_1000
      value: 62.315
    - type: ndcg_at_3
      value: 51.342
    - type: ndcg_at_5
      value: 54.33
    - type: precision_at_1
      value: 44.389
    - type: precision_at_10
      value: 9.26
    - type: precision_at_100
      value: 1.226
    - type: precision_at_1000
      value: 0.136
    - type: precision_at_3
      value: 22.926
    - type: precision_at_5
      value: 15.987000000000002
    - type: recall_at_1
      value: 38.811
    - type: recall_at_10
      value: 70.841
    - type: recall_at_100
      value: 89.218
    - type: recall_at_1000
      value: 96.482
    - type: recall_at_3
      value: 56.123999999999995
    - type: recall_at_5
      value: 63.322
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 25.378
    - type: map_at_10
      value: 34.311
    - type: map_at_100
      value: 35.399
    - type: map_at_1000
      value: 35.482
    - type: map_at_3
      value: 31.917
    - type: map_at_5
      value: 33.275
    - type: mrr_at_1
      value: 27.683999999999997
    - type: mrr_at_10
      value: 36.575
    - type: mrr_at_100
      value: 37.492
    - type: mrr_at_1000
      value: 37.556
    - type: mrr_at_3
      value: 34.35
    - type: mrr_at_5
      value: 35.525
    - type: ndcg_at_1
      value: 27.683999999999997
    - type: ndcg_at_10
      value: 39.247
    - type: ndcg_at_100
      value: 44.424
    - type: ndcg_at_1000
      value: 46.478
    - type: ndcg_at_3
      value: 34.684
    - type: ndcg_at_5
      value: 36.886
    - type: precision_at_1
      value: 27.683999999999997
    - type: precision_at_10
      value: 5.989
    - type: precision_at_100
      value: 0.899
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 14.84
    - type: precision_at_5
      value: 10.215
    - type: recall_at_1
      value: 25.378
    - type: recall_at_10
      value: 52.195
    - type: recall_at_100
      value: 75.764
    - type: recall_at_1000
      value: 91.012
    - type: recall_at_3
      value: 39.885999999999996
    - type: recall_at_5
      value: 45.279
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 17.326
    - type: map_at_10
      value: 25.247000000000003
    - type: map_at_100
      value: 26.473000000000003
    - type: map_at_1000
      value: 26.579000000000004
    - type: map_at_3
      value: 22.466
    - type: map_at_5
      value: 24.113
    - type: mrr_at_1
      value: 21.393
    - type: mrr_at_10
      value: 30.187
    - type: mrr_at_100
      value: 31.089
    - type: mrr_at_1000
      value: 31.15
    - type: mrr_at_3
      value: 27.279999999999998
    - type: mrr_at_5
      value: 29.127
    - type: ndcg_at_1
      value: 21.393
    - type: ndcg_at_10
      value: 30.668
    - type: ndcg_at_100
      value: 36.543
    - type: ndcg_at_1000
      value: 39.181
    - type: ndcg_at_3
      value: 25.552000000000003
    - type: ndcg_at_5
      value: 28.176000000000002
    - type: precision_at_1
      value: 21.393
    - type: precision_at_10
      value: 5.784000000000001
    - type: precision_at_100
      value: 1.001
    - type: precision_at_1000
      value: 0.136
    - type: precision_at_3
      value: 12.231
    - type: precision_at_5
      value: 9.179
    - type: recall_at_1
      value: 17.326
    - type: recall_at_10
      value: 42.415000000000006
    - type: recall_at_100
      value: 68.605
    - type: recall_at_1000
      value: 87.694
    - type: recall_at_3
      value: 28.343
    - type: recall_at_5
      value: 35.086
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 29.069
    - type: map_at_10
      value: 40.027
    - type: map_at_100
      value: 41.308
    - type: map_at_1000
      value: 41.412
    - type: map_at_3
      value: 36.864000000000004
    - type: map_at_5
      value: 38.641999999999996
    - type: mrr_at_1
      value: 35.707
    - type: mrr_at_10
      value: 45.527
    - type: mrr_at_100
      value: 46.348
    - type: mrr_at_1000
      value: 46.392
    - type: mrr_at_3
      value: 43.086
    - type: mrr_at_5
      value: 44.645
    - type: ndcg_at_1
      value: 35.707
    - type: ndcg_at_10
      value: 46.117000000000004
    - type: ndcg_at_100
      value: 51.468
    - type: ndcg_at_1000
      value: 53.412000000000006
    - type: ndcg_at_3
      value: 41.224
    - type: ndcg_at_5
      value: 43.637
    - type: precision_at_1
      value: 35.707
    - type: precision_at_10
      value: 8.459999999999999
    - type: precision_at_100
      value: 1.2970000000000002
    - type: precision_at_1000
      value: 0.165
    - type: precision_at_3
      value: 19.731
    - type: precision_at_5
      value: 14.013
    - type: recall_at_1
      value: 29.069
    - type: recall_at_10
      value: 58.343999999999994
    - type: recall_at_100
      value: 81.296
    - type: recall_at_1000
      value: 93.974
    - type: recall_at_3
      value: 44.7
    - type: recall_at_5
      value: 50.88700000000001
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 23.905
    - type: map_at_10
      value: 33.983000000000004
    - type: map_at_100
      value: 35.372
    - type: map_at_1000
      value: 35.487
    - type: map_at_3
      value: 30.902
    - type: map_at_5
      value: 32.505
    - type: mrr_at_1
      value: 29.794999999999998
    - type: mrr_at_10
      value: 39.28
    - type: mrr_at_100
      value: 40.215
    - type: mrr_at_1000
      value: 40.276
    - type: mrr_at_3
      value: 36.701
    - type: mrr_at_5
      value: 38.105
    - type: ndcg_at_1
      value: 29.794999999999998
    - type: ndcg_at_10
      value: 40.041
    - type: ndcg_at_100
      value: 45.884
    - type: ndcg_at_1000
      value: 48.271
    - type: ndcg_at_3
      value: 34.931
    - type: ndcg_at_5
      value: 37.044
    - type: precision_at_1
      value: 29.794999999999998
    - type: precision_at_10
      value: 7.546
    - type: precision_at_100
      value: 1.216
    - type: precision_at_1000
      value: 0.158
    - type: precision_at_3
      value: 16.933
    - type: precision_at_5
      value: 12.1
    - type: recall_at_1
      value: 23.905
    - type: recall_at_10
      value: 52.945
    - type: recall_at_100
      value: 77.551
    - type: recall_at_1000
      value: 93.793
    - type: recall_at_3
      value: 38.364
    - type: recall_at_5
      value: 44.044
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 25.24441666666667
    - type: map_at_10
      value: 34.4595
    - type: map_at_100
      value: 35.699999999999996
    - type: map_at_1000
      value: 35.8155
    - type: map_at_3
      value: 31.608333333333338
    - type: map_at_5
      value: 33.189416666666666
    - type: mrr_at_1
      value: 29.825250000000004
    - type: mrr_at_10
      value: 38.60875
    - type: mrr_at_100
      value: 39.46575
    - type: mrr_at_1000
      value: 39.52458333333333
    - type: mrr_at_3
      value: 36.145166666666675
    - type: mrr_at_5
      value: 37.57625
    - type: ndcg_at_1
      value: 29.825250000000004
    - type: ndcg_at_10
      value: 39.88741666666667
    - type: ndcg_at_100
      value: 45.17966666666667
    - type: ndcg_at_1000
      value: 47.440583333333336
    - type: ndcg_at_3
      value: 35.04591666666666
    - type: ndcg_at_5
      value: 37.32025
    - type: precision_at_1
      value: 29.825250000000004
    - type: precision_at_10
      value: 7.07225
    - type: precision_at_100
      value: 1.1462499999999998
    - type: precision_at_1000
      value: 0.15325
    - type: precision_at_3
      value: 16.18375
    - type: precision_at_5
      value: 11.526833333333334
    - type: recall_at_1
      value: 25.24441666666667
    - type: recall_at_10
      value: 51.744916666666676
    - type: recall_at_100
      value: 75.04574999999998
    - type: recall_at_1000
      value: 90.65558333333334
    - type: recall_at_3
      value: 38.28349999999999
    - type: recall_at_5
      value: 44.16591666666667
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 24.237000000000002
    - type: map_at_10
      value: 30.667
    - type: map_at_100
      value: 31.592
    - type: map_at_1000
      value: 31.688
    - type: map_at_3
      value: 28.810999999999996
    - type: map_at_5
      value: 29.788999999999998
    - type: mrr_at_1
      value: 26.840000000000003
    - type: mrr_at_10
      value: 33.305
    - type: mrr_at_100
      value: 34.089000000000006
    - type: mrr_at_1000
      value: 34.159
    - type: mrr_at_3
      value: 31.518
    - type: mrr_at_5
      value: 32.469
    - type: ndcg_at_1
      value: 26.840000000000003
    - type: ndcg_at_10
      value: 34.541
    - type: ndcg_at_100
      value: 39.206
    - type: ndcg_at_1000
      value: 41.592
    - type: ndcg_at_3
      value: 31.005
    - type: ndcg_at_5
      value: 32.554
    - type: precision_at_1
      value: 26.840000000000003
    - type: precision_at_10
      value: 5.3069999999999995
    - type: precision_at_100
      value: 0.8340000000000001
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 13.292000000000002
    - type: precision_at_5
      value: 9.049
    - type: recall_at_1
      value: 24.237000000000002
    - type: recall_at_10
      value: 43.862
    - type: recall_at_100
      value: 65.352
    - type: recall_at_1000
      value: 82.704
    - type: recall_at_3
      value: 34.009
    - type: recall_at_5
      value: 37.878
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 16.482
    - type: map_at_10
      value: 23.249
    - type: map_at_100
      value: 24.388
    - type: map_at_1000
      value: 24.519
    - type: map_at_3
      value: 20.971
    - type: map_at_5
      value: 22.192
    - type: mrr_at_1
      value: 19.993
    - type: mrr_at_10
      value: 26.985
    - type: mrr_at_100
      value: 27.975
    - type: mrr_at_1000
      value: 28.052
    - type: mrr_at_3
      value: 24.954
    - type: mrr_at_5
      value: 26.070999999999998
    - type: ndcg_at_1
      value: 19.993
    - type: ndcg_at_10
      value: 27.656
    - type: ndcg_at_100
      value: 33.256
    - type: ndcg_at_1000
      value: 36.275
    - type: ndcg_at_3
      value: 23.644000000000002
    - type: ndcg_at_5
      value: 25.466
    - type: precision_at_1
      value: 19.993
    - type: precision_at_10
      value: 5.093
    - type: precision_at_100
      value: 0.932
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_3
      value: 11.149000000000001
    - type: precision_at_5
      value: 8.149000000000001
    - type: recall_at_1
      value: 16.482
    - type: recall_at_10
      value: 37.141999999999996
    - type: recall_at_100
      value: 62.696
    - type: recall_at_1000
      value: 84.333
    - type: recall_at_3
      value: 26.031
    - type: recall_at_5
      value: 30.660999999999998
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 24.887999999999998
    - type: map_at_10
      value: 34.101
    - type: map_at_100
      value: 35.27
    - type: map_at_1000
      value: 35.370000000000005
    - type: map_at_3
      value: 31.283
    - type: map_at_5
      value: 32.72
    - type: mrr_at_1
      value: 29.011
    - type: mrr_at_10
      value: 38.004
    - type: mrr_at_100
      value: 38.879000000000005
    - type: mrr_at_1000
      value: 38.938
    - type: mrr_at_3
      value: 35.571999999999996
    - type: mrr_at_5
      value: 36.789
    - type: ndcg_at_1
      value: 29.011
    - type: ndcg_at_10
      value: 39.586
    - type: ndcg_at_100
      value: 44.939
    - type: ndcg_at_1000
      value: 47.236
    - type: ndcg_at_3
      value: 34.4
    - type: ndcg_at_5
      value: 36.519
    - type: precision_at_1
      value: 29.011
    - type: precision_at_10
      value: 6.763
    - type: precision_at_100
      value: 1.059
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_3
      value: 15.609
    - type: precision_at_5
      value: 10.896
    - type: recall_at_1
      value: 24.887999999999998
    - type: recall_at_10
      value: 52.42
    - type: recall_at_100
      value: 75.803
    - type: recall_at_1000
      value: 91.725
    - type: recall_at_3
      value: 38.080999999999996
    - type: recall_at_5
      value: 43.47
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 23.953
    - type: map_at_10
      value: 32.649
    - type: map_at_100
      value: 34.181
    - type: map_at_1000
      value: 34.398
    - type: map_at_3
      value: 29.567
    - type: map_at_5
      value: 31.263
    - type: mrr_at_1
      value: 29.051
    - type: mrr_at_10
      value: 37.419999999999995
    - type: mrr_at_100
      value: 38.396
    - type: mrr_at_1000
      value: 38.458
    - type: mrr_at_3
      value: 34.782999999999994
    - type: mrr_at_5
      value: 36.254999999999995
    - type: ndcg_at_1
      value: 29.051
    - type: ndcg_at_10
      value: 38.595
    - type: ndcg_at_100
      value: 44.6
    - type: ndcg_at_1000
      value: 47.158
    - type: ndcg_at_3
      value: 33.56
    - type: ndcg_at_5
      value: 35.870000000000005
    - type: precision_at_1
      value: 29.051
    - type: precision_at_10
      value: 7.53
    - type: precision_at_100
      value: 1.538
    - type: precision_at_1000
      value: 0.24
    - type: precision_at_3
      value: 15.744
    - type: precision_at_5
      value: 11.542
    - type: recall_at_1
      value: 23.953
    - type: recall_at_10
      value: 50.08200000000001
    - type: recall_at_100
      value: 77.364
    - type: recall_at_1000
      value: 93.57799999999999
    - type: recall_at_3
      value: 35.432
    - type: recall_at_5
      value: 41.875
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 17.72
    - type: map_at_10
      value: 25.724000000000004
    - type: map_at_100
      value: 26.846999999999998
    - type: map_at_1000
      value: 26.964
    - type: map_at_3
      value: 22.909
    - type: map_at_5
      value: 24.596999999999998
    - type: mrr_at_1
      value: 18.854000000000003
    - type: mrr_at_10
      value: 27.182000000000002
    - type: mrr_at_100
      value: 28.182000000000002
    - type: mrr_at_1000
      value: 28.274
    - type: mrr_at_3
      value: 24.276
    - type: mrr_at_5
      value: 26.115
    - type: ndcg_at_1
      value: 18.854000000000003
    - type: ndcg_at_10
      value: 30.470000000000002
    - type: ndcg_at_100
      value: 35.854
    - type: ndcg_at_1000
      value: 38.701
    - type: ndcg_at_3
      value: 24.924
    - type: ndcg_at_5
      value: 27.895999999999997
    - type: precision_at_1
      value: 18.854000000000003
    - type: precision_at_10
      value: 5.009
    - type: precision_at_100
      value: 0.835
    - type: precision_at_1000
      value: 0.117
    - type: precision_at_3
      value: 10.721
    - type: precision_at_5
      value: 8.133
    - type: recall_at_1
      value: 17.72
    - type: recall_at_10
      value: 43.617
    - type: recall_at_100
      value: 67.941
    - type: recall_at_1000
      value: 88.979
    - type: recall_at_3
      value: 29.044999999999998
    - type: recall_at_5
      value: 36.044
  - task:
      type: Retrieval
    dataset:
      type: climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 13.427
    - type: map_at_10
      value: 22.935
    - type: map_at_100
      value: 24.808
    - type: map_at_1000
      value: 24.994
    - type: map_at_3
      value: 19.533
    - type: map_at_5
      value: 21.261
    - type: mrr_at_1
      value: 30.945
    - type: mrr_at_10
      value: 43.242000000000004
    - type: mrr_at_100
      value: 44.013999999999996
    - type: mrr_at_1000
      value: 44.048
    - type: mrr_at_3
      value: 40.109
    - type: mrr_at_5
      value: 42.059999999999995
    - type: ndcg_at_1
      value: 30.945
    - type: ndcg_at_10
      value: 31.828
    - type: ndcg_at_100
      value: 38.801
    - type: ndcg_at_1000
      value: 42.126999999999995
    - type: ndcg_at_3
      value: 26.922
    - type: ndcg_at_5
      value: 28.483999999999998
    - type: precision_at_1
      value: 30.945
    - type: precision_at_10
      value: 9.844
    - type: precision_at_100
      value: 1.7309999999999999
    - type: precision_at_1000
      value: 0.23500000000000001
    - type: precision_at_3
      value: 20.477999999999998
    - type: precision_at_5
      value: 15.27
    - type: recall_at_1
      value: 13.427
    - type: recall_at_10
      value: 37.141000000000005
    - type: recall_at_100
      value: 61.007
    - type: recall_at_1000
      value: 79.742
    - type: recall_at_3
      value: 24.431
    - type: recall_at_5
      value: 29.725
  - task:
      type: Retrieval
    dataset:
      type: dbpedia-entity
      name: MTEB DBPedia
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 9.122
    - type: map_at_10
      value: 18.799
    - type: map_at_100
      value: 25.724999999999998
    - type: map_at_1000
      value: 27.205000000000002
    - type: map_at_3
      value: 14.194999999999999
    - type: map_at_5
      value: 16.225
    - type: mrr_at_1
      value: 68.0
    - type: mrr_at_10
      value: 76.035
    - type: mrr_at_100
      value: 76.292
    - type: mrr_at_1000
      value: 76.297
    - type: mrr_at_3
      value: 74.458
    - type: mrr_at_5
      value: 75.558
    - type: ndcg_at_1
      value: 56.00000000000001
    - type: ndcg_at_10
      value: 39.761
    - type: ndcg_at_100
      value: 43.736999999999995
    - type: ndcg_at_1000
      value: 51.146
    - type: ndcg_at_3
      value: 45.921
    - type: ndcg_at_5
      value: 42.756
    - type: precision_at_1
      value: 68.0
    - type: precision_at_10
      value: 30.275000000000002
    - type: precision_at_100
      value: 9.343
    - type: precision_at_1000
      value: 1.8270000000000002
    - type: precision_at_3
      value: 49.167
    - type: precision_at_5
      value: 40.699999999999996
    - type: recall_at_1
      value: 9.122
    - type: recall_at_10
      value: 23.669999999999998
    - type: recall_at_100
      value: 48.719
    - type: recall_at_1000
      value: 72.033
    - type: recall_at_3
      value: 15.498999999999999
    - type: recall_at_5
      value: 18.657
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
      value: 55.885000000000005
    - type: f1
      value: 50.70726446938571
  - task:
      type: Retrieval
    dataset:
      type: fever
      name: MTEB FEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 75.709
    - type: map_at_10
      value: 83.345
    - type: map_at_100
      value: 83.557
    - type: map_at_1000
      value: 83.572
    - type: map_at_3
      value: 82.425
    - type: map_at_5
      value: 83.013
    - type: mrr_at_1
      value: 81.593
    - type: mrr_at_10
      value: 88.331
    - type: mrr_at_100
      value: 88.408
    - type: mrr_at_1000
      value: 88.41
    - type: mrr_at_3
      value: 87.714
    - type: mrr_at_5
      value: 88.122
    - type: ndcg_at_1
      value: 81.593
    - type: ndcg_at_10
      value: 86.925
    - type: ndcg_at_100
      value: 87.67
    - type: ndcg_at_1000
      value: 87.924
    - type: ndcg_at_3
      value: 85.5
    - type: ndcg_at_5
      value: 86.283
    - type: precision_at_1
      value: 81.593
    - type: precision_at_10
      value: 10.264
    - type: precision_at_100
      value: 1.084
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 32.388
    - type: precision_at_5
      value: 19.991
    - type: recall_at_1
      value: 75.709
    - type: recall_at_10
      value: 93.107
    - type: recall_at_100
      value: 96.024
    - type: recall_at_1000
      value: 97.603
    - type: recall_at_3
      value: 89.08500000000001
    - type: recall_at_5
      value: 91.15299999999999
  - task:
      type: Retrieval
    dataset:
      type: fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 19.121
    - type: map_at_10
      value: 31.78
    - type: map_at_100
      value: 33.497
    - type: map_at_1000
      value: 33.696
    - type: map_at_3
      value: 27.893
    - type: map_at_5
      value: 30.087000000000003
    - type: mrr_at_1
      value: 38.272
    - type: mrr_at_10
      value: 47.176
    - type: mrr_at_100
      value: 48.002
    - type: mrr_at_1000
      value: 48.044
    - type: mrr_at_3
      value: 45.086999999999996
    - type: mrr_at_5
      value: 46.337
    - type: ndcg_at_1
      value: 38.272
    - type: ndcg_at_10
      value: 39.145
    - type: ndcg_at_100
      value: 45.696999999999996
    - type: ndcg_at_1000
      value: 49.0
    - type: ndcg_at_3
      value: 36.148
    - type: ndcg_at_5
      value: 37.023
    - type: precision_at_1
      value: 38.272
    - type: precision_at_10
      value: 11.065
    - type: precision_at_100
      value: 1.7840000000000003
    - type: precision_at_1000
      value: 0.23600000000000002
    - type: precision_at_3
      value: 24.587999999999997
    - type: precision_at_5
      value: 18.056
    - type: recall_at_1
      value: 19.121
    - type: recall_at_10
      value: 44.857
    - type: recall_at_100
      value: 69.774
    - type: recall_at_1000
      value: 89.645
    - type: recall_at_3
      value: 32.588
    - type: recall_at_5
      value: 37.939
  - task:
      type: Retrieval
    dataset:
      type: hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 36.428
    - type: map_at_10
      value: 56.891999999999996
    - type: map_at_100
      value: 57.82899999999999
    - type: map_at_1000
      value: 57.896
    - type: map_at_3
      value: 53.762
    - type: map_at_5
      value: 55.718
    - type: mrr_at_1
      value: 72.856
    - type: mrr_at_10
      value: 79.245
    - type: mrr_at_100
      value: 79.515
    - type: mrr_at_1000
      value: 79.525
    - type: mrr_at_3
      value: 78.143
    - type: mrr_at_5
      value: 78.822
    - type: ndcg_at_1
      value: 72.856
    - type: ndcg_at_10
      value: 65.204
    - type: ndcg_at_100
      value: 68.552
    - type: ndcg_at_1000
      value: 69.902
    - type: ndcg_at_3
      value: 60.632
    - type: ndcg_at_5
      value: 63.161
    - type: precision_at_1
      value: 72.856
    - type: precision_at_10
      value: 13.65
    - type: precision_at_100
      value: 1.6260000000000001
    - type: precision_at_1000
      value: 0.181
    - type: precision_at_3
      value: 38.753
    - type: precision_at_5
      value: 25.251
    - type: recall_at_1
      value: 36.428
    - type: recall_at_10
      value: 68.25099999999999
    - type: recall_at_100
      value: 81.317
    - type: recall_at_1000
      value: 90.27
    - type: recall_at_3
      value: 58.13
    - type: recall_at_5
      value: 63.126000000000005
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
      value: 89.4868
    - type: ap
      value: 84.88319192880247
    - type: f1
      value: 89.46144458052846
  - task:
      type: Retrieval
    dataset:
      type: msmarco
      name: MTEB MSMARCO
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 21.282999999999998
    - type: map_at_10
      value: 33.045
    - type: map_at_100
      value: 34.238
    - type: map_at_1000
      value: 34.29
    - type: map_at_3
      value: 29.305999999999997
    - type: map_at_5
      value: 31.391000000000002
    - type: mrr_at_1
      value: 21.92
    - type: mrr_at_10
      value: 33.649
    - type: mrr_at_100
      value: 34.791
    - type: mrr_at_1000
      value: 34.837
    - type: mrr_at_3
      value: 30.0
    - type: mrr_at_5
      value: 32.039
    - type: ndcg_at_1
      value: 21.92
    - type: ndcg_at_10
      value: 39.729
    - type: ndcg_at_100
      value: 45.484
    - type: ndcg_at_1000
      value: 46.817
    - type: ndcg_at_3
      value: 32.084
    - type: ndcg_at_5
      value: 35.789
    - type: precision_at_1
      value: 21.92
    - type: precision_at_10
      value: 6.297
    - type: precision_at_100
      value: 0.918
    - type: precision_at_1000
      value: 0.10300000000000001
    - type: precision_at_3
      value: 13.639000000000001
    - type: precision_at_5
      value: 10.054
    - type: recall_at_1
      value: 21.282999999999998
    - type: recall_at_10
      value: 60.343999999999994
    - type: recall_at_100
      value: 86.981
    - type: recall_at_1000
      value: 97.205
    - type: recall_at_3
      value: 39.452999999999996
    - type: recall_at_5
      value: 48.333
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
      value: 95.47879616963064
    - type: f1
      value: 95.21800589958251
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
      value: 79.09256725946192
    - type: f1
      value: 60.554043889452515
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (en)
      config: en
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 75.53463349024882
    - type: f1
      value: 73.14418495756476
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (en)
      config: en
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 79.22663080026899
    - type: f1
      value: 79.331456217501
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
      value: 34.50316010430136
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
      value: 32.15612040042282
  - task:
      type: Reranking
    dataset:
      type: mteb/mind_small
      name: MTEB MindSmallReranking
      config: default
      split: test
      revision: 3bdac13927fdc888b903db93b2ffdbd90b295a69
    metrics:
    - type: map
      value: 32.36227552557184
    - type: mrr
      value: 33.57901344209811
  - task:
      type: Retrieval
    dataset:
      type: nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 5.6610000000000005
    - type: map_at_10
      value: 12.992
    - type: map_at_100
      value: 16.756999999999998
    - type: map_at_1000
      value: 18.25
    - type: map_at_3
      value: 9.471
    - type: map_at_5
      value: 11.116
    - type: mrr_at_1
      value: 43.653
    - type: mrr_at_10
      value: 53.388999999999996
    - type: mrr_at_100
      value: 53.982
    - type: mrr_at_1000
      value: 54.033
    - type: mrr_at_3
      value: 51.858000000000004
    - type: mrr_at_5
      value: 53.019000000000005
    - type: ndcg_at_1
      value: 41.641
    - type: ndcg_at_10
      value: 34.691
    - type: ndcg_at_100
      value: 32.305
    - type: ndcg_at_1000
      value: 41.132999999999996
    - type: ndcg_at_3
      value: 40.614
    - type: ndcg_at_5
      value: 38.456
    - type: precision_at_1
      value: 43.344
    - type: precision_at_10
      value: 25.881999999999998
    - type: precision_at_100
      value: 8.483
    - type: precision_at_1000
      value: 2.131
    - type: precision_at_3
      value: 38.803
    - type: precision_at_5
      value: 33.87
    - type: recall_at_1
      value: 5.6610000000000005
    - type: recall_at_10
      value: 16.826
    - type: recall_at_100
      value: 32.939
    - type: recall_at_1000
      value: 65.161
    - type: recall_at_3
      value: 10.756
    - type: recall_at_5
      value: 13.331000000000001
  - task:
      type: Retrieval
    dataset:
      type: nq
      name: MTEB NQ
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 26.692
    - type: map_at_10
      value: 41.065000000000005
    - type: map_at_100
      value: 42.235
    - type: map_at_1000
      value: 42.27
    - type: map_at_3
      value: 36.635
    - type: map_at_5
      value: 39.219
    - type: mrr_at_1
      value: 30.214000000000002
    - type: mrr_at_10
      value: 43.443
    - type: mrr_at_100
      value: 44.326
    - type: mrr_at_1000
      value: 44.352000000000004
    - type: mrr_at_3
      value: 39.623999999999995
    - type: mrr_at_5
      value: 41.898
    - type: ndcg_at_1
      value: 30.214000000000002
    - type: ndcg_at_10
      value: 48.692
    - type: ndcg_at_100
      value: 53.671
    - type: ndcg_at_1000
      value: 54.522000000000006
    - type: ndcg_at_3
      value: 40.245
    - type: ndcg_at_5
      value: 44.580999999999996
    - type: precision_at_1
      value: 30.214000000000002
    - type: precision_at_10
      value: 8.3
    - type: precision_at_100
      value: 1.1079999999999999
    - type: precision_at_1000
      value: 0.11900000000000001
    - type: precision_at_3
      value: 18.521
    - type: precision_at_5
      value: 13.627
    - type: recall_at_1
      value: 26.692
    - type: recall_at_10
      value: 69.699
    - type: recall_at_100
      value: 91.425
    - type: recall_at_1000
      value: 97.78099999999999
    - type: recall_at_3
      value: 47.711
    - type: recall_at_5
      value: 57.643
  - task:
      type: Retrieval
    dataset:
      type: quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 70.962
    - type: map_at_10
      value: 84.772
    - type: map_at_100
      value: 85.402
    - type: map_at_1000
      value: 85.418
    - type: map_at_3
      value: 81.89
    - type: map_at_5
      value: 83.685
    - type: mrr_at_1
      value: 81.67
    - type: mrr_at_10
      value: 87.681
    - type: mrr_at_100
      value: 87.792
    - type: mrr_at_1000
      value: 87.79299999999999
    - type: mrr_at_3
      value: 86.803
    - type: mrr_at_5
      value: 87.392
    - type: ndcg_at_1
      value: 81.69
    - type: ndcg_at_10
      value: 88.429
    - type: ndcg_at_100
      value: 89.66
    - type: ndcg_at_1000
      value: 89.762
    - type: ndcg_at_3
      value: 85.75
    - type: ndcg_at_5
      value: 87.20700000000001
    - type: precision_at_1
      value: 81.69
    - type: precision_at_10
      value: 13.395000000000001
    - type: precision_at_100
      value: 1.528
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 37.507000000000005
    - type: precision_at_5
      value: 24.614
    - type: recall_at_1
      value: 70.962
    - type: recall_at_10
      value: 95.339
    - type: recall_at_100
      value: 99.543
    - type: recall_at_1000
      value: 99.984
    - type: recall_at_3
      value: 87.54899999999999
    - type: recall_at_5
      value: 91.726
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
      value: 55.506631779239555
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering-p2p
      name: MTEB RedditClusteringP2P
      config: default
      split: test
      revision: 282350215ef01743dc01b456c7f5241fa8937f16
    metrics:
    - type: v_measure
      value: 60.63731341848479
  - task:
      type: Retrieval
    dataset:
      type: scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 4.852
    - type: map_at_10
      value: 13.175
    - type: map_at_100
      value: 15.623999999999999
    - type: map_at_1000
      value: 16.002
    - type: map_at_3
      value: 9.103
    - type: map_at_5
      value: 11.068999999999999
    - type: mrr_at_1
      value: 23.9
    - type: mrr_at_10
      value: 35.847
    - type: mrr_at_100
      value: 36.968
    - type: mrr_at_1000
      value: 37.018
    - type: mrr_at_3
      value: 32.300000000000004
    - type: mrr_at_5
      value: 34.14
    - type: ndcg_at_1
      value: 23.9
    - type: ndcg_at_10
      value: 21.889
    - type: ndcg_at_100
      value: 30.903000000000002
    - type: ndcg_at_1000
      value: 36.992000000000004
    - type: ndcg_at_3
      value: 20.274
    - type: ndcg_at_5
      value: 17.773
    - type: precision_at_1
      value: 23.9
    - type: precision_at_10
      value: 11.61
    - type: precision_at_100
      value: 2.4539999999999997
    - type: precision_at_1000
      value: 0.391
    - type: precision_at_3
      value: 19.133
    - type: precision_at_5
      value: 15.740000000000002
    - type: recall_at_1
      value: 4.852
    - type: recall_at_10
      value: 23.507
    - type: recall_at_100
      value: 49.775000000000006
    - type: recall_at_1000
      value: 79.308
    - type: recall_at_3
      value: 11.637
    - type: recall_at_5
      value: 15.947
  - task:
      type: STS
    dataset:
      type: mteb/sickr-sts
      name: MTEB SICK-R
      config: default
      split: test
      revision: a6ea5a8cab320b040a23452cc28066d9beae2cee
    metrics:
    - type: cos_sim_pearson
      value: 86.03345827446948
    - type: cos_sim_spearman
      value: 80.53174518259549
    - type: euclidean_pearson
      value: 83.44538971660883
    - type: euclidean_spearman
      value: 80.57344324098692
    - type: manhattan_pearson
      value: 83.36528808195459
    - type: manhattan_spearman
      value: 80.48931287157902
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
      value: 85.21363088257881
    - type: cos_sim_spearman
      value: 75.56589127055523
    - type: euclidean_pearson
      value: 82.32868324521908
    - type: euclidean_spearman
      value: 75.31928550664554
    - type: manhattan_pearson
      value: 82.31332875713211
    - type: manhattan_spearman
      value: 75.35376322099196
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
      value: 85.09085593258487
    - type: cos_sim_spearman
      value: 86.26355088415221
    - type: euclidean_pearson
      value: 85.49646115361156
    - type: euclidean_spearman
      value: 86.20652472228703
    - type: manhattan_pearson
      value: 85.44084081123815
    - type: manhattan_spearman
      value: 86.1162623448951
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
      value: 84.68250248349368
    - type: cos_sim_spearman
      value: 82.29883673695083
    - type: euclidean_pearson
      value: 84.17633035446019
    - type: euclidean_spearman
      value: 82.19990511264791
    - type: manhattan_pearson
      value: 84.17408410692279
    - type: manhattan_spearman
      value: 82.249873895981
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
      value: 87.31878760045024
    - type: cos_sim_spearman
      value: 88.7364409031183
    - type: euclidean_pearson
      value: 88.230537618603
    - type: euclidean_spearman
      value: 88.76484309646318
    - type: manhattan_pearson
      value: 88.17689071136469
    - type: manhattan_spearman
      value: 88.72809249037928
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
      value: 83.41078559110638
    - type: cos_sim_spearman
      value: 85.27439135411049
    - type: euclidean_pearson
      value: 84.5333571592088
    - type: euclidean_spearman
      value: 85.25645460575957
    - type: manhattan_pearson
      value: 84.38428921610226
    - type: manhattan_spearman
      value: 85.07796040798796
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-en)
      config: en-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 88.82374132382576
    - type: cos_sim_spearman
      value: 89.02101343562433
    - type: euclidean_pearson
      value: 89.50729765458932
    - type: euclidean_spearman
      value: 89.04184772869253
    - type: manhattan_pearson
      value: 89.51737904059856
    - type: manhattan_spearman
      value: 89.12925950440676
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (en)
      config: en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 67.56051823873482
    - type: cos_sim_spearman
      value: 68.50988748185463
    - type: euclidean_pearson
      value: 69.16524346147456
    - type: euclidean_spearman
      value: 68.61859952449579
    - type: manhattan_pearson
      value: 69.10618915706995
    - type: manhattan_spearman
      value: 68.36401769459522
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
      value: 85.4159693872625
    - type: cos_sim_spearman
      value: 87.07819121764247
    - type: euclidean_pearson
      value: 87.03013260863153
    - type: euclidean_spearman
      value: 87.06547293631309
    - type: manhattan_pearson
      value: 86.8129744446062
    - type: manhattan_spearman
      value: 86.88494096335627
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
      value: 86.47758088996575
    - type: mrr
      value: 96.17891458577733
  - task:
      type: Retrieval
    dataset:
      type: scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 57.538999999999994
    - type: map_at_10
      value: 66.562
    - type: map_at_100
      value: 67.254
    - type: map_at_1000
      value: 67.284
    - type: map_at_3
      value: 63.722
    - type: map_at_5
      value: 65.422
    - type: mrr_at_1
      value: 60.0
    - type: mrr_at_10
      value: 67.354
    - type: mrr_at_100
      value: 67.908
    - type: mrr_at_1000
      value: 67.93299999999999
    - type: mrr_at_3
      value: 65.056
    - type: mrr_at_5
      value: 66.43900000000001
    - type: ndcg_at_1
      value: 60.0
    - type: ndcg_at_10
      value: 70.858
    - type: ndcg_at_100
      value: 73.67099999999999
    - type: ndcg_at_1000
      value: 74.26700000000001
    - type: ndcg_at_3
      value: 65.911
    - type: ndcg_at_5
      value: 68.42200000000001
    - type: precision_at_1
      value: 60.0
    - type: precision_at_10
      value: 9.4
    - type: precision_at_100
      value: 1.083
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 25.444
    - type: precision_at_5
      value: 17.0
    - type: recall_at_1
      value: 57.538999999999994
    - type: recall_at_10
      value: 83.233
    - type: recall_at_100
      value: 95.667
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 69.883
    - type: recall_at_5
      value: 76.19399999999999
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
      value: 99.82574257425742
    - type: cos_sim_ap
      value: 95.78722833053911
    - type: cos_sim_f1
      value: 90.94650205761316
    - type: cos_sim_precision
      value: 93.64406779661016
    - type: cos_sim_recall
      value: 88.4
    - type: dot_accuracy
      value: 99.83366336633664
    - type: dot_ap
      value: 95.89733601612964
    - type: dot_f1
      value: 91.41981613891727
    - type: dot_precision
      value: 93.42379958246346
    - type: dot_recall
      value: 89.5
    - type: euclidean_accuracy
      value: 99.82574257425742
    - type: euclidean_ap
      value: 95.75227035138846
    - type: euclidean_f1
      value: 90.96509240246407
    - type: euclidean_precision
      value: 93.45991561181435
    - type: euclidean_recall
      value: 88.6
    - type: manhattan_accuracy
      value: 99.82574257425742
    - type: manhattan_ap
      value: 95.76278266220176
    - type: manhattan_f1
      value: 91.08409321175279
    - type: manhattan_precision
      value: 92.29979466119097
    - type: manhattan_recall
      value: 89.9
    - type: max_accuracy
      value: 99.83366336633664
    - type: max_ap
      value: 95.89733601612964
    - type: max_f1
      value: 91.41981613891727
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
      value: 61.905425988638605
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
      value: 36.159589881679736
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
      value: 53.0605499476397
    - type: mrr
      value: 53.91594516594517
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
      value: 30.202718009067
    - type: cos_sim_spearman
      value: 31.136199912366987
    - type: dot_pearson
      value: 30.66329011927951
    - type: dot_spearman
      value: 30.107664909625107
  - task:
      type: Retrieval
    dataset:
      type: trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 0.209
    - type: map_at_10
      value: 1.712
    - type: map_at_100
      value: 9.464
    - type: map_at_1000
      value: 23.437
    - type: map_at_3
      value: 0.609
    - type: map_at_5
      value: 0.9440000000000001
    - type: mrr_at_1
      value: 78.0
    - type: mrr_at_10
      value: 86.833
    - type: mrr_at_100
      value: 86.833
    - type: mrr_at_1000
      value: 86.833
    - type: mrr_at_3
      value: 85.333
    - type: mrr_at_5
      value: 86.833
    - type: ndcg_at_1
      value: 74.0
    - type: ndcg_at_10
      value: 69.14
    - type: ndcg_at_100
      value: 53.047999999999995
    - type: ndcg_at_1000
      value: 48.577
    - type: ndcg_at_3
      value: 75.592
    - type: ndcg_at_5
      value: 72.509
    - type: precision_at_1
      value: 78.0
    - type: precision_at_10
      value: 73.0
    - type: precision_at_100
      value: 54.44
    - type: precision_at_1000
      value: 21.326
    - type: precision_at_3
      value: 80.667
    - type: precision_at_5
      value: 77.2
    - type: recall_at_1
      value: 0.209
    - type: recall_at_10
      value: 1.932
    - type: recall_at_100
      value: 13.211999999999998
    - type: recall_at_1000
      value: 45.774
    - type: recall_at_3
      value: 0.644
    - type: recall_at_5
      value: 1.0290000000000001
  - task:
      type: Retrieval
    dataset:
      type: webis-touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 2.609
    - type: map_at_10
      value: 8.334999999999999
    - type: map_at_100
      value: 14.604000000000001
    - type: map_at_1000
      value: 16.177
    - type: map_at_3
      value: 4.87
    - type: map_at_5
      value: 6.3149999999999995
    - type: mrr_at_1
      value: 32.653
    - type: mrr_at_10
      value: 45.047
    - type: mrr_at_100
      value: 45.808
    - type: mrr_at_1000
      value: 45.808
    - type: mrr_at_3
      value: 41.497
    - type: mrr_at_5
      value: 43.231
    - type: ndcg_at_1
      value: 30.612000000000002
    - type: ndcg_at_10
      value: 21.193
    - type: ndcg_at_100
      value: 34.97
    - type: ndcg_at_1000
      value: 46.69
    - type: ndcg_at_3
      value: 24.823
    - type: ndcg_at_5
      value: 22.872999999999998
    - type: precision_at_1
      value: 32.653
    - type: precision_at_10
      value: 17.959
    - type: precision_at_100
      value: 7.4079999999999995
    - type: precision_at_1000
      value: 1.537
    - type: precision_at_3
      value: 25.85
    - type: precision_at_5
      value: 22.448999999999998
    - type: recall_at_1
      value: 2.609
    - type: recall_at_10
      value: 13.63
    - type: recall_at_100
      value: 47.014
    - type: recall_at_1000
      value: 83.176
    - type: recall_at_3
      value: 5.925
    - type: recall_at_5
      value: 8.574
  - task:
      type: Classification
    dataset:
      type: mteb/toxic_conversations_50k
      name: MTEB ToxicConversationsClassification
      config: default
      split: test
      revision: d7c0de2777da35d6aae2200a62c6e0e5af397c4c
    metrics:
    - type: accuracy
      value: 72.80239999999999
    - type: ap
      value: 15.497911013214791
    - type: f1
      value: 56.258411577947285
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
      value: 61.00452744765139
    - type: f1
      value: 61.42228624410908
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
      value: 50.00516915962345
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
      value: 85.62317458425225
    - type: cos_sim_ap
      value: 72.95115658063823
    - type: cos_sim_f1
      value: 66.78976523344764
    - type: cos_sim_precision
      value: 66.77215189873418
    - type: cos_sim_recall
      value: 66.80738786279683
    - type: dot_accuracy
      value: 85.62317458425225
    - type: dot_ap
      value: 73.10385271517778
    - type: dot_f1
      value: 66.94853829427399
    - type: dot_precision
      value: 61.74242424242424
    - type: dot_recall
      value: 73.11345646437995
    - type: euclidean_accuracy
      value: 85.65893783155511
    - type: euclidean_ap
      value: 72.87428208473992
    - type: euclidean_f1
      value: 66.70919994896005
    - type: euclidean_precision
      value: 64.5910551025451
    - type: euclidean_recall
      value: 68.97097625329816
    - type: manhattan_accuracy
      value: 85.59933241938367
    - type: manhattan_ap
      value: 72.67282695064966
    - type: manhattan_f1
      value: 66.67537215983286
    - type: manhattan_precision
      value: 66.00310237849017
    - type: manhattan_recall
      value: 67.36147757255937
    - type: max_accuracy
      value: 85.65893783155511
    - type: max_ap
      value: 73.10385271517778
    - type: max_f1
      value: 66.94853829427399
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
      value: 88.69096130709822
    - type: cos_sim_ap
      value: 85.30326978668063
    - type: cos_sim_f1
      value: 77.747088683189
    - type: cos_sim_precision
      value: 75.4491451753115
    - type: cos_sim_recall
      value: 80.189405605174
    - type: dot_accuracy
      value: 88.43870066363954
    - type: dot_ap
      value: 84.62999949222983
    - type: dot_f1
      value: 77.3074661963551
    - type: dot_precision
      value: 73.93871239808828
    - type: dot_recall
      value: 80.99784416384355
    - type: euclidean_accuracy
      value: 88.70066363953894
    - type: euclidean_ap
      value: 85.34184508966621
    - type: euclidean_f1
      value: 77.76871756856931
    - type: euclidean_precision
      value: 74.97855917667239
    - type: euclidean_recall
      value: 80.77456113335386
    - type: manhattan_accuracy
      value: 88.68319944114566
    - type: manhattan_ap
      value: 85.3026464242333
    - type: manhattan_f1
      value: 77.66561049296294
    - type: manhattan_precision
      value: 74.4665818849795
    - type: manhattan_recall
      value: 81.15183246073299
    - type: max_accuracy
      value: 88.70066363953894
    - type: max_ap
      value: 85.34184508966621
    - type: max_f1
      value: 77.76871756856931
---
<h1 align="center">GIST small Embedding v0</h1>

*GISTEmbed: Guided In-sample Selection of Training Negatives for Text Embedding Fine-tuning*

The model is fine-tuned on top of the [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) using the [MEDI dataset](https://github.com/xlang-ai/instructor-embedding.git) augmented with mined triplets from the [MTEB Classification](https://huggingface.co/mteb) training dataset (excluding data from the Amazon Polarity Classification task).

The model does not require any instruction for generating embeddings. This means that queries for retrieval tasks can be directly encoded without crafting instructions.

Technical paper: [GISTEmbed: Guided In-sample Selection of Training Negatives for Text Embedding Fine-tuning](https://arxiv.org/abs/2402.16829)


# Data

The dataset used is a compilation of the MEDI and MTEB Classification training datasets. Third-party datasets may be subject to additional terms and conditions under their associated licenses. A HuggingFace Dataset version of the compiled dataset, and the specific revision used to train the model, is available:

- Dataset: [avsolatorio/medi-data-mteb_avs_triplets](https://huggingface.co/datasets/avsolatorio/medi-data-mteb_avs_triplets)
- Revision: 238a0499b6e6b690cc64ea56fde8461daa8341bb

The dataset contains a `task_type` key, which can be used to select only the mteb classification tasks (prefixed with `mteb_`).

The **MEDI Dataset** is published in the following paper: [One Embedder, Any Task: Instruction-Finetuned Text Embeddings](https://arxiv.org/abs/2212.09741).

The MTEB Benchmark results of the GIST embedding model, compared with the base model, suggest that the fine-tuning dataset has perturbed the model considerably, which resulted in significant improvements in certain tasks while adversely degrading performance in some.

The retrieval performance for the TRECCOVID task is of note. The fine-tuning dataset does not contain significant knowledge about COVID-19, which could have caused the observed performance degradation. We found some evidence, detailed in the paper, that thematic coverage of the fine-tuning data can affect downstream performance.

# Usage

The model can be easily loaded using the Sentence Transformers library.

```Python
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer

revision = None  # Replace with the specific revision to ensure reproducibility if the model is updated.

model = SentenceTransformer("avsolatorio/GIST-small-Embedding-v0", revision=revision)

texts = [
    "Illustration of the REaLTabFormer model. The left block shows the non-relational tabular data model using GPT-2 with a causal LM head. In contrast, the right block shows how a relational dataset's child table is modeled using a sequence-to-sequence (Seq2Seq) model. The Seq2Seq model uses the observations in the parent table to condition the generation of the observations in the child table. The trained GPT-2 model on the parent table, with weights frozen, is also used as the encoder in the Seq2Seq model.",
    "Predicting human mobility holds significant practical value, with applications ranging from enhancing disaster risk planning to simulating epidemic spread. In this paper, we present the GeoFormer, a decoder-only transformer model adapted from the GPT architecture to forecast human mobility.",
    "As the economies of Southeast Asia continue adopting digital technologies, policy makers increasingly ask how to prepare the workforce for emerging labor demands. However, little is known about the skills that workers need to adapt to these changes"
]

# Compute embeddings
embeddings = model.encode(texts, convert_to_tensor=True)

# Compute cosine-similarity for each pair of sentences
scores = F.cosine_similarity(embeddings.unsqueeze(1), embeddings.unsqueeze(0), dim=-1)

print(scores.cpu().numpy())
```

# Training Parameters

Below are the training parameters used to fine-tune the model:

```
Epochs = 40
Warmup ratio = 0.1
Learning rate = 5e-6
Batch size = 16
Checkpoint step = 102000
Contrastive loss temperature = 0.01
```


# Evaluation

The model was evaluated using the [MTEB Evaluation](https://huggingface.co/mteb) suite.


# Citation

Please cite our work if you use GISTEmbed or the datasets we published in your projects or research. 🤗

```
@article{solatorio2024gistembed,
    title={GISTEmbed: Guided In-sample Selection of Training Negatives for Text Embedding Fine-tuning},
    author={Aivin V. Solatorio},
    journal={arXiv preprint arXiv:2402.16829},
    year={2024},
    URL={https://arxiv.org/abs/2402.16829}
    eprint={2402.16829},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

# Acknowledgements

This work is supported by the "KCP IV - Exploring Data Use in the Development Economics Literature using Large Language Models (AI and LLMs)" project funded by the [Knowledge for Change Program (KCP)](https://www.worldbank.org/en/programs/knowledge-for-change) of the World Bank - RA-P503405-RESE-TF0C3444.

The findings, interpretations, and conclusions expressed in this material are entirely those of the authors. They do not necessarily represent the views of the International Bank for Reconstruction and Development/World Bank and its affiliated organizations, or those of the Executive Directors of the World Bank or the governments they represent.