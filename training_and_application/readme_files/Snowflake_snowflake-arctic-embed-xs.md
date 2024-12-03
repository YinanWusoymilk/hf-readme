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
model-index:
- name: snowflake-snowflake-arctic-embed-xs
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
      value: 65.08955223880598
    - type: ap
      value: 28.514291209445364
    - type: f1
      value: 59.2604580112738
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
      value: 70.035375
    - type: ap
      value: 64.29444264250405
    - type: f1
      value: 69.78382333907138
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
      value: 35.343999999999994
    - type: f1
      value: 34.69618251902858
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
      value: 28.592000000000002
    - type: map_at_10
      value: 43.597
    - type: map_at_100
      value: 44.614
    - type: map_at_1000
      value: 44.624
    - type: map_at_3
      value: 38.928000000000004
    - type: map_at_5
      value: 41.453
    - type: mrr_at_1
      value: 29.232000000000003
    - type: mrr_at_10
      value: 43.829
    - type: mrr_at_100
      value: 44.852
    - type: mrr_at_1000
      value: 44.862
    - type: mrr_at_3
      value: 39.118
    - type: mrr_at_5
      value: 41.703
    - type: ndcg_at_1
      value: 28.592000000000002
    - type: ndcg_at_10
      value: 52.081
    - type: ndcg_at_100
      value: 56.37
    - type: ndcg_at_1000
      value: 56.598000000000006
    - type: ndcg_at_3
      value: 42.42
    - type: ndcg_at_5
      value: 46.965
    - type: precision_at_1
      value: 28.592000000000002
    - type: precision_at_10
      value: 7.922999999999999
    - type: precision_at_100
      value: 0.979
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 17.52
    - type: precision_at_5
      value: 12.717
    - type: recall_at_1
      value: 28.592000000000002
    - type: recall_at_10
      value: 79.232
    - type: recall_at_100
      value: 97.866
    - type: recall_at_1000
      value: 99.57300000000001
    - type: recall_at_3
      value: 52.559999999999995
    - type: recall_at_5
      value: 63.585
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
      value: 43.50220588953974
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
      value: 32.08725826118282
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
      value: 60.25381587694928
    - type: mrr
      value: 73.79776194873148
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
      value: 85.47489332445278
    - type: cos_sim_spearman
      value: 84.05432487336698
    - type: euclidean_pearson
      value: 84.5108222177219
    - type: euclidean_spearman
      value: 84.05432487336698
    - type: manhattan_pearson
      value: 84.20440618321464
    - type: manhattan_spearman
      value: 83.9290208134097
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
      value: 76.37337662337663
    - type: f1
      value: 75.33296834885043
  - task:
      type: Clustering
    dataset:
      type: jinaai/big-patent-clustering
      name: MTEB BigPatentClustering
      config: default
      split: test
      revision: 62d5330920bca426ce9d3c76ea914f15fc83e891
    metrics:
    - type: v_measure
      value: 21.31174373264835
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
      value: 34.481973521597844
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
      value: 26.14094256567341
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
      value: 32.527
    - type: map_at_10
      value: 43.699
    - type: map_at_100
      value: 45.03
    - type: map_at_1000
      value: 45.157000000000004
    - type: map_at_3
      value: 39.943
    - type: map_at_5
      value: 42.324
    - type: mrr_at_1
      value: 39.771
    - type: mrr_at_10
      value: 49.277
    - type: mrr_at_100
      value: 49.956
    - type: mrr_at_1000
      value: 50.005
    - type: mrr_at_3
      value: 46.304
    - type: mrr_at_5
      value: 48.493
    - type: ndcg_at_1
      value: 39.771
    - type: ndcg_at_10
      value: 49.957
    - type: ndcg_at_100
      value: 54.678000000000004
    - type: ndcg_at_1000
      value: 56.751
    - type: ndcg_at_3
      value: 44.608
    - type: ndcg_at_5
      value: 47.687000000000005
    - type: precision_at_1
      value: 39.771
    - type: precision_at_10
      value: 9.557
    - type: precision_at_100
      value: 1.5010000000000001
    - type: precision_at_1000
      value: 0.194
    - type: precision_at_3
      value: 21.173000000000002
    - type: precision_at_5
      value: 15.794
    - type: recall_at_1
      value: 32.527
    - type: recall_at_10
      value: 61.791
    - type: recall_at_100
      value: 81.49300000000001
    - type: recall_at_1000
      value: 95.014
    - type: recall_at_3
      value: 46.605000000000004
    - type: recall_at_5
      value: 54.83
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
      value: 29.424
    - type: map_at_10
      value: 38.667
    - type: map_at_100
      value: 39.771
    - type: map_at_1000
      value: 39.899
    - type: map_at_3
      value: 35.91
    - type: map_at_5
      value: 37.45
    - type: mrr_at_1
      value: 36.687999999999995
    - type: mrr_at_10
      value: 44.673
    - type: mrr_at_100
      value: 45.289
    - type: mrr_at_1000
      value: 45.338
    - type: mrr_at_3
      value: 42.601
    - type: mrr_at_5
      value: 43.875
    - type: ndcg_at_1
      value: 36.687999999999995
    - type: ndcg_at_10
      value: 44.013000000000005
    - type: ndcg_at_100
      value: 48.13
    - type: ndcg_at_1000
      value: 50.294000000000004
    - type: ndcg_at_3
      value: 40.056999999999995
    - type: ndcg_at_5
      value: 41.902
    - type: precision_at_1
      value: 36.687999999999995
    - type: precision_at_10
      value: 8.158999999999999
    - type: precision_at_100
      value: 1.321
    - type: precision_at_1000
      value: 0.179
    - type: precision_at_3
      value: 19.045
    - type: precision_at_5
      value: 13.427
    - type: recall_at_1
      value: 29.424
    - type: recall_at_10
      value: 53.08500000000001
    - type: recall_at_100
      value: 70.679
    - type: recall_at_1000
      value: 84.66
    - type: recall_at_3
      value: 41.399
    - type: recall_at_5
      value: 46.632
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
      value: 39.747
    - type: map_at_10
      value: 51.452
    - type: map_at_100
      value: 52.384
    - type: map_at_1000
      value: 52.437
    - type: map_at_3
      value: 48.213
    - type: map_at_5
      value: 50.195
    - type: mrr_at_1
      value: 45.391999999999996
    - type: mrr_at_10
      value: 54.928
    - type: mrr_at_100
      value: 55.532000000000004
    - type: mrr_at_1000
      value: 55.565
    - type: mrr_at_3
      value: 52.456
    - type: mrr_at_5
      value: 54.054
    - type: ndcg_at_1
      value: 45.391999999999996
    - type: ndcg_at_10
      value: 57.055
    - type: ndcg_at_100
      value: 60.751999999999995
    - type: ndcg_at_1000
      value: 61.864
    - type: ndcg_at_3
      value: 51.662
    - type: ndcg_at_5
      value: 54.613
    - type: precision_at_1
      value: 45.391999999999996
    - type: precision_at_10
      value: 9.103
    - type: precision_at_100
      value: 1.1780000000000002
    - type: precision_at_1000
      value: 0.132
    - type: precision_at_3
      value: 22.717000000000002
    - type: precision_at_5
      value: 15.812000000000001
    - type: recall_at_1
      value: 39.747
    - type: recall_at_10
      value: 70.10499999999999
    - type: recall_at_100
      value: 86.23100000000001
    - type: recall_at_1000
      value: 94.025
    - type: recall_at_3
      value: 55.899
    - type: recall_at_5
      value: 63.05500000000001
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
      value: 27.168999999999997
    - type: map_at_10
      value: 34.975
    - type: map_at_100
      value: 35.94
    - type: map_at_1000
      value: 36.021
    - type: map_at_3
      value: 32.35
    - type: map_at_5
      value: 33.831
    - type: mrr_at_1
      value: 28.701
    - type: mrr_at_10
      value: 36.698
    - type: mrr_at_100
      value: 37.546
    - type: mrr_at_1000
      value: 37.613
    - type: mrr_at_3
      value: 34.256
    - type: mrr_at_5
      value: 35.685
    - type: ndcg_at_1
      value: 28.701
    - type: ndcg_at_10
      value: 39.639
    - type: ndcg_at_100
      value: 44.389
    - type: ndcg_at_1000
      value: 46.46
    - type: ndcg_at_3
      value: 34.52
    - type: ndcg_at_5
      value: 37.076
    - type: precision_at_1
      value: 28.701
    - type: precision_at_10
      value: 5.955
    - type: precision_at_100
      value: 0.8880000000000001
    - type: precision_at_1000
      value: 0.109
    - type: precision_at_3
      value: 14.274999999999999
    - type: precision_at_5
      value: 10.011000000000001
    - type: recall_at_1
      value: 27.168999999999997
    - type: recall_at_10
      value: 52.347
    - type: recall_at_100
      value: 74.1
    - type: recall_at_1000
      value: 89.739
    - type: recall_at_3
      value: 38.567
    - type: recall_at_5
      value: 44.767
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
      value: 15.872
    - type: map_at_10
      value: 23.153000000000002
    - type: map_at_100
      value: 24.311
    - type: map_at_1000
      value: 24.432000000000002
    - type: map_at_3
      value: 20.707
    - type: map_at_5
      value: 21.921
    - type: mrr_at_1
      value: 19.776
    - type: mrr_at_10
      value: 27.755999999999997
    - type: mrr_at_100
      value: 28.709
    - type: mrr_at_1000
      value: 28.778
    - type: mrr_at_3
      value: 25.186999999999998
    - type: mrr_at_5
      value: 26.43
    - type: ndcg_at_1
      value: 19.776
    - type: ndcg_at_10
      value: 28.288999999999998
    - type: ndcg_at_100
      value: 34.011
    - type: ndcg_at_1000
      value: 36.916
    - type: ndcg_at_3
      value: 23.551
    - type: ndcg_at_5
      value: 25.429000000000002
    - type: precision_at_1
      value: 19.776
    - type: precision_at_10
      value: 5.311
    - type: precision_at_100
      value: 0.9440000000000001
    - type: precision_at_1000
      value: 0.132
    - type: precision_at_3
      value: 11.360000000000001
    - type: precision_at_5
      value: 8.209
    - type: recall_at_1
      value: 15.872
    - type: recall_at_10
      value: 39.726
    - type: recall_at_100
      value: 65.035
    - type: recall_at_1000
      value: 85.846
    - type: recall_at_3
      value: 26.432
    - type: recall_at_5
      value: 31.22
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
      value: 28.126
    - type: map_at_10
      value: 37.537
    - type: map_at_100
      value: 38.807
    - type: map_at_1000
      value: 38.923
    - type: map_at_3
      value: 34.65
    - type: map_at_5
      value: 36.248000000000005
    - type: mrr_at_1
      value: 34.649
    - type: mrr_at_10
      value: 42.893
    - type: mrr_at_100
      value: 43.721
    - type: mrr_at_1000
      value: 43.775999999999996
    - type: mrr_at_3
      value: 40.488
    - type: mrr_at_5
      value: 41.729
    - type: ndcg_at_1
      value: 34.649
    - type: ndcg_at_10
      value: 43.072
    - type: ndcg_at_100
      value: 48.464
    - type: ndcg_at_1000
      value: 50.724000000000004
    - type: ndcg_at_3
      value: 38.506
    - type: ndcg_at_5
      value: 40.522000000000006
    - type: precision_at_1
      value: 34.649
    - type: precision_at_10
      value: 7.68
    - type: precision_at_100
      value: 1.214
    - type: precision_at_1000
      value: 0.16
    - type: precision_at_3
      value: 18.029999999999998
    - type: precision_at_5
      value: 12.666
    - type: recall_at_1
      value: 28.126
    - type: recall_at_10
      value: 54.396
    - type: recall_at_100
      value: 76.988
    - type: recall_at_1000
      value: 91.85799999999999
    - type: recall_at_3
      value: 41.169
    - type: recall_at_5
      value: 46.658
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
      value: 26.68
    - type: map_at_10
      value: 35.702
    - type: map_at_100
      value: 36.864999999999995
    - type: map_at_1000
      value: 36.977
    - type: map_at_3
      value: 32.828
    - type: map_at_5
      value: 34.481
    - type: mrr_at_1
      value: 32.991
    - type: mrr_at_10
      value: 40.993
    - type: mrr_at_100
      value: 41.827
    - type: mrr_at_1000
      value: 41.887
    - type: mrr_at_3
      value: 38.623000000000005
    - type: mrr_at_5
      value: 40.021
    - type: ndcg_at_1
      value: 32.991
    - type: ndcg_at_10
      value: 41.036
    - type: ndcg_at_100
      value: 46.294000000000004
    - type: ndcg_at_1000
      value: 48.644
    - type: ndcg_at_3
      value: 36.419000000000004
    - type: ndcg_at_5
      value: 38.618
    - type: precision_at_1
      value: 32.991
    - type: precision_at_10
      value: 7.385999999999999
    - type: precision_at_100
      value: 1.176
    - type: precision_at_1000
      value: 0.151
    - type: precision_at_3
      value: 17.122999999999998
    - type: precision_at_5
      value: 12.215
    - type: recall_at_1
      value: 26.68
    - type: recall_at_10
      value: 51.644
    - type: recall_at_100
      value: 74.55000000000001
    - type: recall_at_1000
      value: 90.825
    - type: recall_at_3
      value: 38.579
    - type: recall_at_5
      value: 44.512
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
    metrics:
    - type: map_at_1
      value: 26.30825
    - type: map_at_10
      value: 34.97866666666666
    - type: map_at_100
      value: 36.109249999999996
    - type: map_at_1000
      value: 36.22508333333333
    - type: map_at_3
      value: 32.239083333333326
    - type: map_at_5
      value: 33.75933333333334
    - type: mrr_at_1
      value: 31.05308333333333
    - type: mrr_at_10
      value: 39.099833333333336
    - type: mrr_at_100
      value: 39.92008333333334
    - type: mrr_at_1000
      value: 39.980000000000004
    - type: mrr_at_3
      value: 36.75958333333333
    - type: mrr_at_5
      value: 38.086416666666665
    - type: ndcg_at_1
      value: 31.05308333333333
    - type: ndcg_at_10
      value: 40.11558333333334
    - type: ndcg_at_100
      value: 45.05966666666667
    - type: ndcg_at_1000
      value: 47.36516666666667
    - type: ndcg_at_3
      value: 35.490833333333335
    - type: ndcg_at_5
      value: 37.64541666666666
    - type: precision_at_1
      value: 31.05308333333333
    - type: precision_at_10
      value: 6.968416666666666
    - type: precision_at_100
      value: 1.1156666666666666
    - type: precision_at_1000
      value: 0.14950000000000002
    - type: precision_at_3
      value: 16.123
    - type: precision_at_5
      value: 11.451166666666666
    - type: recall_at_1
      value: 26.30825
    - type: recall_at_10
      value: 51.19283333333333
    - type: recall_at_100
      value: 73.0285
    - type: recall_at_1000
      value: 89.11133333333333
    - type: recall_at_3
      value: 38.26208333333333
    - type: recall_at_5
      value: 43.855916666666666
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
      value: 23.363999999999997
    - type: map_at_10
      value: 30.606
    - type: map_at_100
      value: 31.491999999999997
    - type: map_at_1000
      value: 31.578
    - type: map_at_3
      value: 28.610000000000003
    - type: map_at_5
      value: 29.602
    - type: mrr_at_1
      value: 26.38
    - type: mrr_at_10
      value: 33.472
    - type: mrr_at_100
      value: 34.299
    - type: mrr_at_1000
      value: 34.361999999999995
    - type: mrr_at_3
      value: 31.696999999999996
    - type: mrr_at_5
      value: 32.503
    - type: ndcg_at_1
      value: 26.38
    - type: ndcg_at_10
      value: 34.772999999999996
    - type: ndcg_at_100
      value: 39.334
    - type: ndcg_at_1000
      value: 41.676
    - type: ndcg_at_3
      value: 31.097
    - type: ndcg_at_5
      value: 32.561
    - type: precision_at_1
      value: 26.38
    - type: precision_at_10
      value: 5.475
    - type: precision_at_100
      value: 0.84
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: precision_at_3
      value: 13.395000000000001
    - type: precision_at_5
      value: 9.11
    - type: recall_at_1
      value: 23.363999999999997
    - type: recall_at_10
      value: 44.656
    - type: recall_at_100
      value: 65.77199999999999
    - type: recall_at_1000
      value: 83.462
    - type: recall_at_3
      value: 34.213
    - type: recall_at_5
      value: 38.091
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
      value: 17.971999999999998
    - type: map_at_10
      value: 24.913
    - type: map_at_100
      value: 25.916
    - type: map_at_1000
      value: 26.049
    - type: map_at_3
      value: 22.569
    - type: map_at_5
      value: 23.858999999999998
    - type: mrr_at_1
      value: 21.748
    - type: mrr_at_10
      value: 28.711
    - type: mrr_at_100
      value: 29.535
    - type: mrr_at_1000
      value: 29.621
    - type: mrr_at_3
      value: 26.484999999999996
    - type: mrr_at_5
      value: 27.701999999999998
    - type: ndcg_at_1
      value: 21.748
    - type: ndcg_at_10
      value: 29.412
    - type: ndcg_at_100
      value: 34.204
    - type: ndcg_at_1000
      value: 37.358000000000004
    - type: ndcg_at_3
      value: 25.202
    - type: ndcg_at_5
      value: 27.128000000000004
    - type: precision_at_1
      value: 21.748
    - type: precision_at_10
      value: 5.279
    - type: precision_at_100
      value: 0.902
    - type: precision_at_1000
      value: 0.135
    - type: precision_at_3
      value: 11.551
    - type: precision_at_5
      value: 8.437999999999999
    - type: recall_at_1
      value: 17.971999999999998
    - type: recall_at_10
      value: 39.186
    - type: recall_at_100
      value: 60.785999999999994
    - type: recall_at_1000
      value: 83.372
    - type: recall_at_3
      value: 27.584999999999997
    - type: recall_at_5
      value: 32.448
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
      value: 26.684
    - type: map_at_10
      value: 35.188
    - type: map_at_100
      value: 36.379
    - type: map_at_1000
      value: 36.481
    - type: map_at_3
      value: 32.401
    - type: map_at_5
      value: 34.132
    - type: mrr_at_1
      value: 31.063000000000002
    - type: mrr_at_10
      value: 39.104
    - type: mrr_at_100
      value: 40.062999999999995
    - type: mrr_at_1000
      value: 40.119
    - type: mrr_at_3
      value: 36.692
    - type: mrr_at_5
      value: 38.161
    - type: ndcg_at_1
      value: 31.063000000000002
    - type: ndcg_at_10
      value: 40.096
    - type: ndcg_at_100
      value: 45.616
    - type: ndcg_at_1000
      value: 47.869
    - type: ndcg_at_3
      value: 35.256
    - type: ndcg_at_5
      value: 37.826
    - type: precision_at_1
      value: 31.063000000000002
    - type: precision_at_10
      value: 6.622999999999999
    - type: precision_at_100
      value: 1.046
    - type: precision_at_1000
      value: 0.135
    - type: precision_at_3
      value: 15.641
    - type: precision_at_5
      value: 11.231
    - type: recall_at_1
      value: 26.684
    - type: recall_at_10
      value: 51.092999999999996
    - type: recall_at_100
      value: 75.099
    - type: recall_at_1000
      value: 90.644
    - type: recall_at_3
      value: 38.063
    - type: recall_at_5
      value: 44.518
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
      value: 26.249
    - type: map_at_10
      value: 34.694
    - type: map_at_100
      value: 36.208
    - type: map_at_1000
      value: 36.443
    - type: map_at_3
      value: 31.868000000000002
    - type: map_at_5
      value: 33.018
    - type: mrr_at_1
      value: 31.818
    - type: mrr_at_10
      value: 39.416000000000004
    - type: mrr_at_100
      value: 40.327
    - type: mrr_at_1000
      value: 40.388000000000005
    - type: mrr_at_3
      value: 37.120999999999995
    - type: mrr_at_5
      value: 38.07
    - type: ndcg_at_1
      value: 31.818
    - type: ndcg_at_10
      value: 40.405
    - type: ndcg_at_100
      value: 45.816
    - type: ndcg_at_1000
      value: 48.403
    - type: ndcg_at_3
      value: 35.823
    - type: ndcg_at_5
      value: 37.191
    - type: precision_at_1
      value: 31.818
    - type: precision_at_10
      value: 7.806
    - type: precision_at_100
      value: 1.518
    - type: precision_at_1000
      value: 0.241
    - type: precision_at_3
      value: 16.535
    - type: precision_at_5
      value: 11.738999999999999
    - type: recall_at_1
      value: 26.249
    - type: recall_at_10
      value: 50.928
    - type: recall_at_100
      value: 75.271
    - type: recall_at_1000
      value: 91.535
    - type: recall_at_3
      value: 37.322
    - type: recall_at_5
      value: 41.318
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
      value: 21.884999999999998
    - type: map_at_10
      value: 29.158
    - type: map_at_100
      value: 30.208000000000002
    - type: map_at_1000
      value: 30.304
    - type: map_at_3
      value: 26.82
    - type: map_at_5
      value: 28.051
    - type: mrr_at_1
      value: 23.66
    - type: mrr_at_10
      value: 31.277
    - type: mrr_at_100
      value: 32.237
    - type: mrr_at_1000
      value: 32.308
    - type: mrr_at_3
      value: 29.205
    - type: mrr_at_5
      value: 30.314000000000004
    - type: ndcg_at_1
      value: 23.66
    - type: ndcg_at_10
      value: 33.64
    - type: ndcg_at_100
      value: 39.028
    - type: ndcg_at_1000
      value: 41.423
    - type: ndcg_at_3
      value: 29.189
    - type: ndcg_at_5
      value: 31.191999999999997
    - type: precision_at_1
      value: 23.66
    - type: precision_at_10
      value: 5.287
    - type: precision_at_100
      value: 0.86
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 12.631
    - type: precision_at_5
      value: 8.762
    - type: recall_at_1
      value: 21.884999999999998
    - type: recall_at_10
      value: 45.357
    - type: recall_at_100
      value: 70.338
    - type: recall_at_1000
      value: 88.356
    - type: recall_at_3
      value: 33.312000000000005
    - type: recall_at_5
      value: 38.222
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
      value: 13.058
    - type: map_at_10
      value: 21.549
    - type: map_at_100
      value: 23.287
    - type: map_at_1000
      value: 23.444000000000003
    - type: map_at_3
      value: 18.18
    - type: map_at_5
      value: 19.886
    - type: mrr_at_1
      value: 28.73
    - type: mrr_at_10
      value: 40.014
    - type: mrr_at_100
      value: 40.827000000000005
    - type: mrr_at_1000
      value: 40.866
    - type: mrr_at_3
      value: 36.602000000000004
    - type: mrr_at_5
      value: 38.702
    - type: ndcg_at_1
      value: 28.73
    - type: ndcg_at_10
      value: 29.881
    - type: ndcg_at_100
      value: 36.662
    - type: ndcg_at_1000
      value: 39.641999999999996
    - type: ndcg_at_3
      value: 24.661
    - type: ndcg_at_5
      value: 26.548
    - type: precision_at_1
      value: 28.73
    - type: precision_at_10
      value: 9.094
    - type: precision_at_100
      value: 1.6480000000000001
    - type: precision_at_1000
      value: 0.22100000000000003
    - type: precision_at_3
      value: 17.98
    - type: precision_at_5
      value: 13.811000000000002
    - type: recall_at_1
      value: 13.058
    - type: recall_at_10
      value: 35.458
    - type: recall_at_100
      value: 58.719
    - type: recall_at_1000
      value: 75.495
    - type: recall_at_3
      value: 22.607
    - type: recall_at_5
      value: 28.067999999999998
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
      value: 8.811
    - type: map_at_10
      value: 19.134999999999998
    - type: map_at_100
      value: 26.905
    - type: map_at_1000
      value: 28.503
    - type: map_at_3
      value: 13.863
    - type: map_at_5
      value: 16.062
    - type: mrr_at_1
      value: 67
    - type: mrr_at_10
      value: 74.607
    - type: mrr_at_100
      value: 74.941
    - type: mrr_at_1000
      value: 74.954
    - type: mrr_at_3
      value: 73.042
    - type: mrr_at_5
      value: 73.992
    - type: ndcg_at_1
      value: 52.87500000000001
    - type: ndcg_at_10
      value: 40.199
    - type: ndcg_at_100
      value: 44.901
    - type: ndcg_at_1000
      value: 52.239999999999995
    - type: ndcg_at_3
      value: 44.983000000000004
    - type: ndcg_at_5
      value: 42.137
    - type: precision_at_1
      value: 67
    - type: precision_at_10
      value: 31.8
    - type: precision_at_100
      value: 10.315000000000001
    - type: precision_at_1000
      value: 2.0420000000000003
    - type: precision_at_3
      value: 48.667
    - type: precision_at_5
      value: 40.9
    - type: recall_at_1
      value: 8.811
    - type: recall_at_10
      value: 24.503
    - type: recall_at_100
      value: 51.288999999999994
    - type: recall_at_1000
      value: 74.827
    - type: recall_at_3
      value: 15.254999999999999
    - type: recall_at_5
      value: 18.698999999999998
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
      value: 41.839999999999996
    - type: f1
      value: 37.78718146306379
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
      value: 68.47999999999999
    - type: map_at_10
      value: 78.782
    - type: map_at_100
      value: 79.021
    - type: map_at_1000
      value: 79.035
    - type: map_at_3
      value: 77.389
    - type: map_at_5
      value: 78.347
    - type: mrr_at_1
      value: 73.837
    - type: mrr_at_10
      value: 83.41499999999999
    - type: mrr_at_100
      value: 83.53399999999999
    - type: mrr_at_1000
      value: 83.535
    - type: mrr_at_3
      value: 82.32300000000001
    - type: mrr_at_5
      value: 83.13000000000001
    - type: ndcg_at_1
      value: 73.837
    - type: ndcg_at_10
      value: 83.404
    - type: ndcg_at_100
      value: 84.287
    - type: ndcg_at_1000
      value: 84.52199999999999
    - type: ndcg_at_3
      value: 81.072
    - type: ndcg_at_5
      value: 82.537
    - type: precision_at_1
      value: 73.837
    - type: precision_at_10
      value: 10.254000000000001
    - type: precision_at_100
      value: 1.088
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 31.538
    - type: precision_at_5
      value: 19.811
    - type: recall_at_1
      value: 68.47999999999999
    - type: recall_at_10
      value: 92.98100000000001
    - type: recall_at_100
      value: 96.50800000000001
    - type: recall_at_1000
      value: 97.925
    - type: recall_at_3
      value: 86.764
    - type: recall_at_5
      value: 90.39
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
      value: 16.786
    - type: map_at_10
      value: 26.97
    - type: map_at_100
      value: 28.488000000000003
    - type: map_at_1000
      value: 28.665000000000003
    - type: map_at_3
      value: 23.3
    - type: map_at_5
      value: 25.249
    - type: mrr_at_1
      value: 33.025
    - type: mrr_at_10
      value: 41.86
    - type: mrr_at_100
      value: 42.673
    - type: mrr_at_1000
      value: 42.714
    - type: mrr_at_3
      value: 39.403
    - type: mrr_at_5
      value: 40.723
    - type: ndcg_at_1
      value: 33.025
    - type: ndcg_at_10
      value: 34.522999999999996
    - type: ndcg_at_100
      value: 40.831
    - type: ndcg_at_1000
      value: 44.01
    - type: ndcg_at_3
      value: 30.698999999999998
    - type: ndcg_at_5
      value: 31.832
    - type: precision_at_1
      value: 33.025
    - type: precision_at_10
      value: 9.583
    - type: precision_at_100
      value: 1.619
    - type: precision_at_1000
      value: 0.22100000000000003
    - type: precision_at_3
      value: 20.216
    - type: precision_at_5
      value: 15.031
    - type: recall_at_1
      value: 16.786
    - type: recall_at_10
      value: 41.969
    - type: recall_at_100
      value: 66.353
    - type: recall_at_1000
      value: 85.299
    - type: recall_at_3
      value: 28.111000000000004
    - type: recall_at_5
      value: 33.645
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
      value: 37.346000000000004
    - type: map_at_10
      value: 56.184999999999995
    - type: map_at_100
      value: 57.062000000000005
    - type: map_at_1000
      value: 57.126999999999995
    - type: map_at_3
      value: 52.815
    - type: map_at_5
      value: 54.893
    - type: mrr_at_1
      value: 74.693
    - type: mrr_at_10
      value: 81.128
    - type: mrr_at_100
      value: 81.356
    - type: mrr_at_1000
      value: 81.363
    - type: mrr_at_3
      value: 80.05600000000001
    - type: mrr_at_5
      value: 80.74
    - type: ndcg_at_1
      value: 74.693
    - type: ndcg_at_10
      value: 65.249
    - type: ndcg_at_100
      value: 68.357
    - type: ndcg_at_1000
      value: 69.64200000000001
    - type: ndcg_at_3
      value: 60.377
    - type: ndcg_at_5
      value: 63.044
    - type: precision_at_1
      value: 74.693
    - type: precision_at_10
      value: 13.630999999999998
    - type: precision_at_100
      value: 1.606
    - type: precision_at_1000
      value: 0.178
    - type: precision_at_3
      value: 38.222
    - type: precision_at_5
      value: 25.040000000000003
    - type: recall_at_1
      value: 37.346000000000004
    - type: recall_at_10
      value: 68.157
    - type: recall_at_100
      value: 80.297
    - type: recall_at_1000
      value: 88.832
    - type: recall_at_3
      value: 57.333
    - type: recall_at_5
      value: 62.6
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
      value: 62.80240000000001
    - type: ap
      value: 58.22949464075975
    - type: f1
      value: 62.55694937343487
  - task:
      type: Retrieval
    dataset:
      type: mteb/msmarco
      name: MTEB MSMARCO
      config: default
      split: dev
      revision: c5a29a104738b98a9e76336939199e264163d4a0
    metrics:
    - type: map_at_1
      value: 20.918
    - type: map_at_10
      value: 32.732
    - type: map_at_100
      value: 33.922000000000004
    - type: map_at_1000
      value: 33.976
    - type: map_at_3
      value: 29.051
    - type: map_at_5
      value: 31.101
    - type: mrr_at_1
      value: 21.418
    - type: mrr_at_10
      value: 33.284000000000006
    - type: mrr_at_100
      value: 34.426
    - type: mrr_at_1000
      value: 34.473
    - type: mrr_at_3
      value: 29.644
    - type: mrr_at_5
      value: 31.691000000000003
    - type: ndcg_at_1
      value: 21.418
    - type: ndcg_at_10
      value: 39.427
    - type: ndcg_at_100
      value: 45.190999999999995
    - type: ndcg_at_1000
      value: 46.544000000000004
    - type: ndcg_at_3
      value: 31.885
    - type: ndcg_at_5
      value: 35.555
    - type: precision_at_1
      value: 21.418
    - type: precision_at_10
      value: 6.254999999999999
    - type: precision_at_100
      value: 0.915
    - type: precision_at_1000
      value: 0.10300000000000001
    - type: precision_at_3
      value: 13.591000000000001
    - type: precision_at_5
      value: 10.011000000000001
    - type: recall_at_1
      value: 20.918
    - type: recall_at_10
      value: 60.074000000000005
    - type: recall_at_100
      value: 86.726
    - type: recall_at_1000
      value: 97.116
    - type: recall_at_3
      value: 39.506
    - type: recall_at_5
      value: 48.319
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
      value: 90.79799361605106
    - type: f1
      value: 90.0757957511057
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
      value: 58.00501595987233
    - type: f1
      value: 39.85731569133947
  - task:
      type: Classification
    dataset:
      type: masakhane/masakhanews
      name: MTEB MasakhaNEWSClassification (eng)
      config: eng
      split: test
      revision: 8ccc72e69e65f40c70e117d8b3c08306bb788b60
    metrics:
    - type: accuracy
      value: 77.10970464135022
    - type: f1
      value: 76.12037616356896
  - task:
      type: Clustering
    dataset:
      type: masakhane/masakhanews
      name: MTEB MasakhaNEWSClusteringP2P (eng)
      config: eng
      split: test
      revision: 8ccc72e69e65f40c70e117d8b3c08306bb788b60
    metrics:
    - type: v_measure
      value: 69.81323966287493
  - task:
      type: Clustering
    dataset:
      type: masakhane/masakhanews
      name: MTEB MasakhaNEWSClusteringS2S (eng)
      config: eng
      split: test
      revision: 8ccc72e69e65f40c70e117d8b3c08306bb788b60
    metrics:
    - type: v_measure
      value: 33.112774215788455
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
      value: 63.51042367182246
    - type: f1
      value: 60.99310361578824
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
      value: 71.0053799596503
    - type: f1
      value: 69.7794673003686
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
      value: 30.56899174856954
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
      value: 26.21848014733929
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
      value: 30.256308756916646
    - type: mrr
      value: 31.123872086825656
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
      value: 5.07
    - type: map_at_10
      value: 11.286999999999999
    - type: map_at_100
      value: 13.630999999999998
    - type: map_at_1000
      value: 14.844
    - type: map_at_3
      value: 8.395
    - type: map_at_5
      value: 9.721
    - type: mrr_at_1
      value: 41.486000000000004
    - type: mrr_at_10
      value: 51.041000000000004
    - type: mrr_at_100
      value: 51.661
    - type: mrr_at_1000
      value: 51.7
    - type: mrr_at_3
      value: 49.226
    - type: mrr_at_5
      value: 50.526
    - type: ndcg_at_1
      value: 39.783
    - type: ndcg_at_10
      value: 30.885
    - type: ndcg_at_100
      value: 27.459
    - type: ndcg_at_1000
      value: 35.988
    - type: ndcg_at_3
      value: 36.705
    - type: ndcg_at_5
      value: 34.156
    - type: precision_at_1
      value: 41.486000000000004
    - type: precision_at_10
      value: 22.415
    - type: precision_at_100
      value: 6.819999999999999
    - type: precision_at_1000
      value: 1.8980000000000001
    - type: precision_at_3
      value: 34.572
    - type: precision_at_5
      value: 29.287999999999997
    - type: recall_at_1
      value: 5.07
    - type: recall_at_10
      value: 14.576
    - type: recall_at_100
      value: 27.112000000000002
    - type: recall_at_1000
      value: 57.995
    - type: recall_at_3
      value: 9.242
    - type: recall_at_5
      value: 11.668000000000001
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
      value: 32.263999999999996
    - type: map_at_10
      value: 47.219
    - type: map_at_100
      value: 48.209999999999994
    - type: map_at_1000
      value: 48.24
    - type: map_at_3
      value: 42.905
    - type: map_at_5
      value: 45.501000000000005
    - type: mrr_at_1
      value: 36.153
    - type: mrr_at_10
      value: 49.636
    - type: mrr_at_100
      value: 50.357
    - type: mrr_at_1000
      value: 50.378
    - type: mrr_at_3
      value: 46.094
    - type: mrr_at_5
      value: 48.233
    - type: ndcg_at_1
      value: 36.124
    - type: ndcg_at_10
      value: 54.764
    - type: ndcg_at_100
      value: 58.867999999999995
    - type: ndcg_at_1000
      value: 59.548
    - type: ndcg_at_3
      value: 46.717999999999996
    - type: ndcg_at_5
      value: 50.981
    - type: precision_at_1
      value: 36.124
    - type: precision_at_10
      value: 8.931000000000001
    - type: precision_at_100
      value: 1.126
    - type: precision_at_1000
      value: 0.11900000000000001
    - type: precision_at_3
      value: 21.051000000000002
    - type: precision_at_5
      value: 15.104000000000001
    - type: recall_at_1
      value: 32.263999999999996
    - type: recall_at_10
      value: 75.39099999999999
    - type: recall_at_100
      value: 93.038
    - type: recall_at_1000
      value: 98.006
    - type: recall_at_3
      value: 54.562999999999995
    - type: recall_at_5
      value: 64.352
  - task:
      type: Classification
    dataset:
      type: ag_news
      name: MTEB NewsClassification
      config: default
      split: test
      revision: eb185aade064a813bc0b7f42de02595523103ca4
    metrics:
    - type: accuracy
      value: 77.75
    - type: f1
      value: 77.504243291547
  - task:
      type: PairClassification
    dataset:
      type: GEM/opusparcus
      name: MTEB OpusparcusPC (en)
      config: en
      split: test
      revision: 9e9b1f8ef51616073f47f306f7f47dd91663f86a
    metrics:
    - type: cos_sim_accuracy
      value: 99.89816700610999
    - type: cos_sim_ap
      value: 100
    - type: cos_sim_f1
      value: 99.9490575649516
    - type: cos_sim_precision
      value: 100
    - type: cos_sim_recall
      value: 99.89816700610999
    - type: dot_accuracy
      value: 99.89816700610999
    - type: dot_ap
      value: 100
    - type: dot_f1
      value: 99.9490575649516
    - type: dot_precision
      value: 100
    - type: dot_recall
      value: 99.89816700610999
    - type: euclidean_accuracy
      value: 99.89816700610999
    - type: euclidean_ap
      value: 100
    - type: euclidean_f1
      value: 99.9490575649516
    - type: euclidean_precision
      value: 100
    - type: euclidean_recall
      value: 99.89816700610999
    - type: manhattan_accuracy
      value: 99.89816700610999
    - type: manhattan_ap
      value: 100
    - type: manhattan_f1
      value: 99.9490575649516
    - type: manhattan_precision
      value: 100
    - type: manhattan_recall
      value: 99.89816700610999
    - type: max_accuracy
      value: 99.89816700610999
    - type: max_ap
      value: 100
    - type: max_f1
      value: 99.9490575649516
  - task:
      type: PairClassification
    dataset:
      type: paws-x
      name: MTEB PawsX (en)
      config: en
      split: test
      revision: 8a04d940a42cd40658986fdd8e3da561533a3646
    metrics:
    - type: cos_sim_accuracy
      value: 61.75000000000001
    - type: cos_sim_ap
      value: 57.9482264289061
    - type: cos_sim_f1
      value: 62.444061962134256
    - type: cos_sim_precision
      value: 45.3953953953954
    - type: cos_sim_recall
      value: 100
    - type: dot_accuracy
      value: 61.75000000000001
    - type: dot_ap
      value: 57.94808038610475
    - type: dot_f1
      value: 62.444061962134256
    - type: dot_precision
      value: 45.3953953953954
    - type: dot_recall
      value: 100
    - type: euclidean_accuracy
      value: 61.75000000000001
    - type: euclidean_ap
      value: 57.94808038610475
    - type: euclidean_f1
      value: 62.444061962134256
    - type: euclidean_precision
      value: 45.3953953953954
    - type: euclidean_recall
      value: 100
    - type: manhattan_accuracy
      value: 61.7
    - type: manhattan_ap
      value: 57.996119308184966
    - type: manhattan_f1
      value: 62.46078773091669
    - type: manhattan_precision
      value: 45.66768603465851
    - type: manhattan_recall
      value: 98.78721058434398
    - type: max_accuracy
      value: 61.75000000000001
    - type: max_ap
      value: 57.996119308184966
    - type: max_f1
      value: 62.46078773091669
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
      value: 69.001
    - type: map_at_10
      value: 82.573
    - type: map_at_100
      value: 83.226
    - type: map_at_1000
      value: 83.246
    - type: map_at_3
      value: 79.625
    - type: map_at_5
      value: 81.491
    - type: mrr_at_1
      value: 79.44
    - type: mrr_at_10
      value: 85.928
    - type: mrr_at_100
      value: 86.05199999999999
    - type: mrr_at_1000
      value: 86.054
    - type: mrr_at_3
      value: 84.847
    - type: mrr_at_5
      value: 85.596
    - type: ndcg_at_1
      value: 79.41
    - type: ndcg_at_10
      value: 86.568
    - type: ndcg_at_100
      value: 87.965
    - type: ndcg_at_1000
      value: 88.134
    - type: ndcg_at_3
      value: 83.55900000000001
    - type: ndcg_at_5
      value: 85.244
    - type: precision_at_1
      value: 79.41
    - type: precision_at_10
      value: 13.108
    - type: precision_at_100
      value: 1.509
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 36.443
    - type: precision_at_5
      value: 24.03
    - type: recall_at_1
      value: 69.001
    - type: recall_at_10
      value: 94.132
    - type: recall_at_100
      value: 99.043
    - type: recall_at_1000
      value: 99.878
    - type: recall_at_3
      value: 85.492
    - type: recall_at_5
      value: 90.226
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
      value: 48.3161352736264
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
      value: 57.83784484156747
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
      value: 4.403
    - type: map_at_10
      value: 10.922
    - type: map_at_100
      value: 12.626000000000001
    - type: map_at_1000
      value: 12.883
    - type: map_at_3
      value: 7.982
    - type: map_at_5
      value: 9.442
    - type: mrr_at_1
      value: 21.7
    - type: mrr_at_10
      value: 31.653
    - type: mrr_at_100
      value: 32.757999999999996
    - type: mrr_at_1000
      value: 32.824999999999996
    - type: mrr_at_3
      value: 28.266999999999996
    - type: mrr_at_5
      value: 30.127
    - type: ndcg_at_1
      value: 21.7
    - type: ndcg_at_10
      value: 18.355
    - type: ndcg_at_100
      value: 25.228
    - type: ndcg_at_1000
      value: 30.164
    - type: ndcg_at_3
      value: 17.549
    - type: ndcg_at_5
      value: 15.260000000000002
    - type: precision_at_1
      value: 21.7
    - type: precision_at_10
      value: 9.47
    - type: precision_at_100
      value: 1.9290000000000003
    - type: precision_at_1000
      value: 0.312
    - type: precision_at_3
      value: 16.3
    - type: precision_at_5
      value: 13.28
    - type: recall_at_1
      value: 4.403
    - type: recall_at_10
      value: 19.18
    - type: recall_at_100
      value: 39.182
    - type: recall_at_1000
      value: 63.378
    - type: recall_at_3
      value: 9.934999999999999
    - type: recall_at_5
      value: 13.459999999999999
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
      value: 76.90841073432534
    - type: cos_sim_spearman
      value: 69.2566375434526
    - type: euclidean_pearson
      value: 73.00183878559413
    - type: euclidean_spearman
      value: 69.25664656235413
    - type: manhattan_pearson
      value: 72.89594756197533
    - type: manhattan_spearman
      value: 69.23247111043545
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
      value: 69.60878511794063
    - type: cos_sim_spearman
      value: 65.89916377105551
    - type: euclidean_pearson
      value: 66.90761876557181
    - type: euclidean_spearman
      value: 65.89915018368384
    - type: manhattan_pearson
      value: 66.78502575257721
    - type: manhattan_spearman
      value: 65.79977053467938
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
      value: 77.2869334987418
    - type: cos_sim_spearman
      value: 77.86961921643416
    - type: euclidean_pearson
      value: 77.43179820479914
    - type: euclidean_spearman
      value: 77.86961921643416
    - type: manhattan_pearson
      value: 77.18900647348373
    - type: manhattan_spearman
      value: 77.61209060062608
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
      value: 76.26453932960364
    - type: cos_sim_spearman
      value: 72.81574657995401
    - type: euclidean_pearson
      value: 75.0708953437423
    - type: euclidean_spearman
      value: 72.81574657995401
    - type: manhattan_pearson
      value: 74.88396609999512
    - type: manhattan_spearman
      value: 72.65437562156805
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
      value: 82.37827653919395
    - type: cos_sim_spearman
      value: 83.4885552472602
    - type: euclidean_pearson
      value: 82.89377087926749
    - type: euclidean_spearman
      value: 83.4885552472602
    - type: manhattan_pearson
      value: 82.82440771787735
    - type: manhattan_spearman
      value: 83.41449537888975
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
      value: 78.7995043673964
    - type: cos_sim_spearman
      value: 80.57804447517638
    - type: euclidean_pearson
      value: 80.03013884278195
    - type: euclidean_spearman
      value: 80.57804447517638
    - type: manhattan_pearson
      value: 80.13406111544424
    - type: manhattan_spearman
      value: 80.65354602648962
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
      value: 83.63565989937278
    - type: cos_sim_spearman
      value: 84.4948593656943
    - type: euclidean_pearson
      value: 84.68743074820951
    - type: euclidean_spearman
      value: 84.4948593656943
    - type: manhattan_pearson
      value: 84.43639397781811
    - type: manhattan_spearman
      value: 84.32595552115242
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (en)
      config: en
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_pearson
      value: 65.06382649277246
    - type: cos_sim_spearman
      value: 66.28447782018655
    - type: euclidean_pearson
      value: 67.09895930908392
    - type: euclidean_spearman
      value: 66.28447782018655
    - type: manhattan_pearson
      value: 66.96342453888376
    - type: manhattan_spearman
      value: 66.33876259551842
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
      value: 78.43883428940346
    - type: cos_sim_spearman
      value: 79.18395553127085
    - type: euclidean_pearson
      value: 79.22986635457109
    - type: euclidean_spearman
      value: 79.18395553127085
    - type: manhattan_pearson
      value: 79.10921229934691
    - type: manhattan_spearman
      value: 79.02283553930171
  - task:
      type: STS
    dataset:
      type: PhilipMay/stsb_multi_mt
      name: MTEB STSBenchmarkMultilingualSTS (en)
      config: en
      split: test
      revision: 93d57ef91790589e3ce9c365164337a8a78b7632
    metrics:
    - type: cos_sim_pearson
      value: 78.43883433444418
    - type: cos_sim_spearman
      value: 79.18395553127085
    - type: euclidean_pearson
      value: 79.22986642351681
    - type: euclidean_spearman
      value: 79.18395553127085
    - type: manhattan_pearson
      value: 79.10921236746302
    - type: manhattan_spearman
      value: 79.02283553930171
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
      value: 76.9361627171417
    - type: mrr
      value: 93.06577046773126
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
      value: 50.693999999999996
    - type: map_at_10
      value: 59.784000000000006
    - type: map_at_100
      value: 60.443000000000005
    - type: map_at_1000
      value: 60.480000000000004
    - type: map_at_3
      value: 57.028
    - type: map_at_5
      value: 58.306999999999995
    - type: mrr_at_1
      value: 53.333
    - type: mrr_at_10
      value: 61.565000000000005
    - type: mrr_at_100
      value: 62.095
    - type: mrr_at_1000
      value: 62.131
    - type: mrr_at_3
      value: 59.721999999999994
    - type: mrr_at_5
      value: 60.589000000000006
    - type: ndcg_at_1
      value: 53.333
    - type: ndcg_at_10
      value: 64.512
    - type: ndcg_at_100
      value: 67.366
    - type: ndcg_at_1000
      value: 68.46799999999999
    - type: ndcg_at_3
      value: 59.748999999999995
    - type: ndcg_at_5
      value: 61.526
    - type: precision_at_1
      value: 53.333
    - type: precision_at_10
      value: 8.733
    - type: precision_at_100
      value: 1.027
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 23.222
    - type: precision_at_5
      value: 15.2
    - type: recall_at_1
      value: 50.693999999999996
    - type: recall_at_10
      value: 77.333
    - type: recall_at_100
      value: 90.10000000000001
    - type: recall_at_1000
      value: 99
    - type: recall_at_3
      value: 64.39399999999999
    - type: recall_at_5
      value: 68.7
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
      value: 99.81386138613861
    - type: cos_sim_ap
      value: 94.96375600031361
    - type: cos_sim_f1
      value: 90.36885245901641
    - type: cos_sim_precision
      value: 92.64705882352942
    - type: cos_sim_recall
      value: 88.2
    - type: dot_accuracy
      value: 99.81386138613861
    - type: dot_ap
      value: 94.96375600031361
    - type: dot_f1
      value: 90.36885245901641
    - type: dot_precision
      value: 92.64705882352942
    - type: dot_recall
      value: 88.2
    - type: euclidean_accuracy
      value: 99.81386138613861
    - type: euclidean_ap
      value: 94.96375600031361
    - type: euclidean_f1
      value: 90.36885245901641
    - type: euclidean_precision
      value: 92.64705882352942
    - type: euclidean_recall
      value: 88.2
    - type: manhattan_accuracy
      value: 99.81287128712871
    - type: manhattan_ap
      value: 94.92563500640084
    - type: manhattan_f1
      value: 90.27277406073082
    - type: manhattan_precision
      value: 93.00106044538707
    - type: manhattan_recall
      value: 87.7
    - type: max_accuracy
      value: 99.81386138613861
    - type: max_ap
      value: 94.96375600031361
    - type: max_f1
      value: 90.36885245901641
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
      value: 57.486984956276274
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
      value: 34.58453023612073
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
      value: 50.16317315282306
    - type: mrr
      value: 50.82617137764197
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
      value: 30.2927995133324
    - type: cos_sim_spearman
      value: 30.09648622523191
    - type: dot_pearson
      value: 30.29279853541771
    - type: dot_spearman
      value: 30.09648622523191
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
      value: 0.23500000000000001
    - type: map_at_10
      value: 2.01
    - type: map_at_100
      value: 12.064
    - type: map_at_1000
      value: 27.437
    - type: map_at_3
      value: 0.6649999999999999
    - type: map_at_5
      value: 1.0959999999999999
    - type: mrr_at_1
      value: 88
    - type: mrr_at_10
      value: 92.667
    - type: mrr_at_100
      value: 92.667
    - type: mrr_at_1000
      value: 92.667
    - type: mrr_at_3
      value: 91.667
    - type: mrr_at_5
      value: 92.667
    - type: ndcg_at_1
      value: 84
    - type: ndcg_at_10
      value: 79.431
    - type: ndcg_at_100
      value: 60.914
    - type: ndcg_at_1000
      value: 52.005
    - type: ndcg_at_3
      value: 82.285
    - type: ndcg_at_5
      value: 81.565
    - type: precision_at_1
      value: 88
    - type: precision_at_10
      value: 84.8
    - type: precision_at_100
      value: 62.32
    - type: precision_at_1000
      value: 23.014000000000003
    - type: precision_at_3
      value: 86.667
    - type: precision_at_5
      value: 87.2
    - type: recall_at_1
      value: 0.23500000000000001
    - type: recall_at_10
      value: 2.19
    - type: recall_at_100
      value: 14.904
    - type: recall_at_1000
      value: 47.875
    - type: recall_at_3
      value: 0.695
    - type: recall_at_5
      value: 1.165
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
      value: 3.639
    - type: map_at_10
      value: 14.184
    - type: map_at_100
      value: 20.61
    - type: map_at_1000
      value: 22.377
    - type: map_at_3
      value: 9.163
    - type: map_at_5
      value: 10.773000000000001
    - type: mrr_at_1
      value: 46.939
    - type: mrr_at_10
      value: 59.345000000000006
    - type: mrr_at_100
      value: 60.07599999999999
    - type: mrr_at_1000
      value: 60.07599999999999
    - type: mrr_at_3
      value: 55.782
    - type: mrr_at_5
      value: 58.231
    - type: ndcg_at_1
      value: 41.837
    - type: ndcg_at_10
      value: 32.789
    - type: ndcg_at_100
      value: 42.232
    - type: ndcg_at_1000
      value: 53.900999999999996
    - type: ndcg_at_3
      value: 41.963
    - type: ndcg_at_5
      value: 35.983
    - type: precision_at_1
      value: 46.939
    - type: precision_at_10
      value: 28.163
    - type: precision_at_100
      value: 8.102
    - type: precision_at_1000
      value: 1.59
    - type: precision_at_3
      value: 44.897999999999996
    - type: precision_at_5
      value: 34.694
    - type: recall_at_1
      value: 3.639
    - type: recall_at_10
      value: 19.308
    - type: recall_at_100
      value: 48.992000000000004
    - type: recall_at_1000
      value: 84.59400000000001
    - type: recall_at_3
      value: 9.956
    - type: recall_at_5
      value: 12.33
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
      value: 64.305
    - type: ap
      value: 11.330746746072599
    - type: f1
      value: 49.290704382387865
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
      value: 56.1941143180532
    - type: f1
      value: 56.40189765095578
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
      value: 36.28189332526842
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
      value: 83.1912737676581
    - type: cos_sim_ap
      value: 64.31536990146257
    - type: cos_sim_f1
      value: 61.095167030191696
    - type: cos_sim_precision
      value: 54.074375127006704
    - type: cos_sim_recall
      value: 70.21108179419525
    - type: dot_accuracy
      value: 83.1912737676581
    - type: dot_ap
      value: 64.31539216162541
    - type: dot_f1
      value: 61.095167030191696
    - type: dot_precision
      value: 54.074375127006704
    - type: dot_recall
      value: 70.21108179419525
    - type: euclidean_accuracy
      value: 83.1912737676581
    - type: euclidean_ap
      value: 64.31538391358727
    - type: euclidean_f1
      value: 61.095167030191696
    - type: euclidean_precision
      value: 54.074375127006704
    - type: euclidean_recall
      value: 70.21108179419525
    - type: manhattan_accuracy
      value: 83.07206294331525
    - type: manhattan_ap
      value: 64.14646315556838
    - type: manhattan_f1
      value: 61.194029850746254
    - type: manhattan_precision
      value: 54.166666666666664
    - type: manhattan_recall
      value: 70.31662269129288
    - type: max_accuracy
      value: 83.1912737676581
    - type: max_ap
      value: 64.31539216162541
    - type: max_f1
      value: 61.194029850746254
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
      value: 88.38242713548337
    - type: cos_sim_ap
      value: 84.70041255196017
    - type: cos_sim_f1
      value: 77.13222561986515
    - type: cos_sim_precision
      value: 73.95266690215472
    - type: cos_sim_recall
      value: 80.59747459193102
    - type: dot_accuracy
      value: 88.38242713548337
    - type: dot_ap
      value: 84.7004118720222
    - type: dot_f1
      value: 77.13222561986515
    - type: dot_precision
      value: 73.95266690215472
    - type: dot_recall
      value: 80.59747459193102
    - type: euclidean_accuracy
      value: 88.38242713548337
    - type: euclidean_ap
      value: 84.70041593996575
    - type: euclidean_f1
      value: 77.13222561986515
    - type: euclidean_precision
      value: 73.95266690215472
    - type: euclidean_recall
      value: 80.59747459193102
    - type: manhattan_accuracy
      value: 88.36108200411378
    - type: manhattan_ap
      value: 84.66897701572054
    - type: manhattan_f1
      value: 77.00707640360645
    - type: manhattan_precision
      value: 72.17695778062082
    - type: manhattan_recall
      value: 82.53002771789343
    - type: max_accuracy
      value: 88.38242713548337
    - type: max_ap
      value: 84.70041593996575
    - type: max_f1
      value: 77.13222561986515
  - task:
      type: Clustering
    dataset:
      type: jinaai/cities_wiki_clustering
      name: MTEB WikiCitiesClustering
      config: default
      split: test
      revision: ddc9ee9242fa65332597f70e967ecc38b9d734fa
    metrics:
    - type: v_measure
      value: 81.46426354153643
---
<h1 align="center">Snowflake's Arctic-embed-xs</h1>
<h4 align="center">
   <p>
       <a href=#news>News</a> |
       <a href=#models>Models</a> |
       <a href=#usage>Usage</a>  |
       <a href="#evaluation">Evaluation</a> |
       <a href="#contact">Contact</a> |
       <a href="#faq">FAQ</a>
       <a href="#license">License</a> |
       <a href="#acknowledgement">Acknowledgement</a>
   <p>
</h4>


## News

07/26/2024: Release preprint [[2407.18887] Embedding And Clustering Your Data Can Improve Contrastive Pretraining](https://arxiv.org/abs/2407.18887) on arXiv.

07/18/2024: Release of `snowflake-arctic-embed-m-v1.5`, capable of producing highly compressible embedding vectors that preserve quality even when squished as small as 128 bytes per vector. Details about the development of this model are available in the [launch post on the Snowflake engineering blog](https://www.snowflake.com/engineering-blog/arctic-embed-m-v1-5-enterprise-retrieval/).

05/10/2024: Release the [technical report on Arctic Embed](https://arxiv.org/abs/2405.05374)

04/16/2024: Release the ** snowflake-arctic-embed ** family of text embedding models. The releases are state-of-the-art for Retrieval quality at each of their representative size profiles. [Technical Report]() is coming shortly. For more details, please refer to our Github: [Arctic-Text-Embed](https://github.com/Snowflake-Labs/arctic-embed).


## Models


snowflake-arctic-embed is a suite of text embedding models that focuses on creating high-quality retrieval models optimized for performance.


The `snowflake-arctic-embedding` models achieve **state-of-the-art performance on the MTEB/BEIR leaderboard** for each of their size variants. Evaluation is performed using these [scripts](https://github.com/Snowflake-Labs/snowflake-arctic-embed/tree/main/src). As shown below, each class of model size achieves SOTA retrieval accuracy compared to other top models.


The models are trained by leveraging existing open-source text representation models, such as bert-base-uncased, and are trained in a multi-stage pipeline to optimize their retrieval performance. First, the models are trained with large batches of query-document pairs where negatives are derived in-batch—pretraining leverages about 400m samples of a mix of public datasets and proprietary web search data. Following pretraining models are further optimized with long training on a smaller dataset (about 1m samples) of triplets of query, positive document, and negative document derived from hard harmful mining. Mining of the negatives and data curation is crucial to retrieval accuracy. A detailed technical report can be found [here](https://arxiv.org/abs/2405.05374).


| Name                                                                    | MTEB Retrieval Score (NDCG @ 10) | Parameters (Millions) | Embedding Dimension |
| ----------------------------------------------------------------------- | -------------------------------- | --------------------- | ------------------- |
| [snowflake-arctic-embed-xs](https://huggingface.co/Snowflake/snowflake-arctic-embed-xs/)     | 50.15                            | 22                    | 384                 |
| [snowflake-arctic-embed-s](https://huggingface.co/Snowflake/snowflake-arctic-embed-s/)      | 51.98                            | 33                    | 384                 |
| [snowflake-arctic-embed-m](https://huggingface.co/Snowflake/snowflake-arctic-embed-m/)      | 54.90                            | 110                   | 768                 |
| [snowflake-arctic-embed-m-long](https://huggingface.co/Snowflake/snowflake-arctic-embed-m-long/) | 54.83                            | 137                   | 768                 |
| [snowflake-arctic-embed-l](https://huggingface.co/Snowflake/snowflake-arctic-embed-l/)      | 55.98                            | 335                   | 1024                |


Aside from being great open-source models, the largest model, [snowflake-arctic-embed-l](https://huggingface.co/Snowflake/snowflake-arctic-embed-l/), can serve as a natural replacement for closed-source embedding, as shown below.


| Model Name                                                         | MTEB Retrieval Score (NDCG @ 10) |
| ------------------------------------------------------------------ | -------------------------------- |
| [snowflake-arctic-embed-l](https://huggingface.co/Snowflake/snowflake-arctic-embed-l/) | 55.98                            |
| Google-gecko-text-embedding                                        | 55.7                             |
| text-embedding-3-large                                             | 55.44                            |
| Cohere-embed-english-v3.0                                          | 55.00                            |
| bge-large-en-v1.5                                                  | 54.29                            |


### [snowflake-arctic-embed-xs](https://huggingface.co/Snowflake/snowflake-arctic-embed-xs)


This tiny model packs quite the punch. Based on the [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model with only 22m parameters and 384 dimensions, this model should meet even the strictest latency/TCO budgets. Despite its size, its retrieval accuracy is closer to that of models with 100m paramers.


| Model Name                                                          | MTEB Retrieval Score (NDCG @ 10) |
| ------------------------------------------------------------------- | -------------------------------- |
| [snowflake-arctic-embed-xs](https://huggingface.co/Snowflake/snowflake-arctic-embed-xs/) | 50.15                            |
| GIST-all-MiniLM-L6-v2                                               | 45.12                            |
| gte-tiny                                                            | 44.92                            |
| all-MiniLM-L6-v2                                                    | 41.95                            |
| bge-micro-v2                                                        | 42.56                            |


### [snowflake-arctic-embed-s](https://huggingface.co/Snowflake/snowflake-arctic-embed-s)


Based on the [infloat/e5-small-unsupervised](https://huggingface.co/intfloat/e5-small-unsupervised) model, this small model does not trade off retrieval accuracy for its small size. With only 33m parameters and 384 dimensions, this model should easily allow scaling to large datasets.


| Model Name                                                         | MTEB Retrieval Score (NDCG @ 10) |
| ------------------------------------------------------------------ | -------------------------------- |
| [snowflake-arctic-embed-s](https://huggingface.co/Snowflake/snowflake-arctic-embed-s/) | 51.98                            |
| bge-small-en-v1.5                                                  | 51.68                            |
| Cohere-embed-english-light-v3.0                                    | 51.34                            |
| text-embedding-3-small                                             | 51.08                            |
| e5-small-v2                                                        | 49.04                            |


### [snowflake-arctic-embed-m](https://huggingface.co/Snowflake/snowflake-arctic-embed-m/)


Based on the [intfloat/e5-base-unsupervised](https://huggingface.co/intfloat/e5-base-unsupervised) model, this medium model is the workhorse that provides the best retrieval performance without slowing down inference.


| Model Name                                                         | MTEB Retrieval Score (NDCG @ 10) |
| ------------------------------------------------------------------ | -------------------------------- |
| [snowflake-arctic-embed-m](https://huggingface.co/Snowflake/snowflake-arctic-embed-m/) | 54.90                            |
| bge-base-en-v1.5                                                   | 53.25                            |
| nomic-embed-text-v1.5                                              | 53.25                            |
| GIST-Embedding-v0                                                  | 52.31                            |
| gte-base                                                           | 52.31                            |

### [snowflake-arctic-embed-m-long](https://huggingface.co/Snowflake/snowflake-arctic-embed-m-long/)


Based on the [nomic-embed-text-v1-unsupervised](https://huggingface.co/nomic-ai/nomic-embed-text-v1-unsupervised) model, this long-context variant of our medium-sized model is perfect for workloads that can be constrained by the regular 512 token context of our other models. Without the use of RPE, this model supports up to 2048 tokens. With RPE, it can scale to 8192!


| Model Name                                                         | MTEB Retrieval Score (NDCG @ 10) |
| ------------------------------------------------------------------ | -------------------------------- |
| [snowflake-arctic-embed-m-long](https://huggingface.co/Snowflake/snowflake-arctic-embed-m-long/) | 54.83                            |
| nomic-embed-text-v1.5                                              | 53.01                            |
| nomic-embed-text-v1                                                | 52.81                            |




### [snowflake-arctic-embed-l](https://huggingface.co/Snowflake/snowflake-arctic-embed-l/)


Based on the [intfloat/e5-large-unsupervised](https://huggingface.co/intfloat/e5-large-unsupervised) model, this large model is a direct drop-in for closed APIs and delivers the most accurate retrieval experience.


| Model Name                                                         | MTEB Retrieval Score (NDCG @ 10) |
| ------------------------------------------------------------------ | -------------------------------- |
| [snowflake-arctic-embed-l](https://huggingface.co/Snowflake/snowflake-arctic-embed-l/) | 55.98                            |
| UAE-Large-V1                                                       | 54.66                            |
| bge-large-en-v1.5                                                  | 54.29                            |
| mxbai-embed-large-v1                                               | 54.39                            |
| e5-Large-v2                                                        | 50.56                            |


## Usage

### Using Sentence Transformers

You can use the sentence-transformers package to use an snowflake-arctic-embed model, as shown below. 

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Snowflake/snowflake-arctic-embed-xs")

queries = ['what is snowflake?', 'Where can I get the best tacos?']
documents = ['The Data Cloud!', 'Mexico City of Course!']

query_embeddings = model.encode(queries, prompt_name="query")
document_embeddings = model.encode(documents)

scores = query_embeddings @ document_embeddings.T
for query, query_scores in zip(queries, scores):
    doc_score_pairs = list(zip(documents, query_scores))
    doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)
    # Output passages & scores
    print("Query:", query)
    for document, score in doc_score_pairs:
        print(score, document)
```
```
Query: what is snowflake?
0.57515126 The Data Cloud!
0.45798576 Mexico City of Course!
Query: Where can I get the best tacos?
0.5636022 Mexico City of Course!
0.5044898 The Data Cloud!
```

### Using Huggingface transformers


You can use the transformers package for a snowflake-arctic-embed model, as shown below. For optimal retrieval quality, use the CLS token to embed each text portion and use the query prefix below (just on the query).



```python
import torch
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Snowflake/snowflake-arctic-embed-xs')
model = AutoModel.from_pretrained('Snowflake/snowflake-arctic-embed-xs', add_pooling_layer=False)
model.eval()

query_prefix = 'Represent this sentence for searching relevant passages: '
queries  = ['what is snowflake?', 'Where can I get the best tacos?']
queries_with_prefix = ["{}{}".format(query_prefix, i) for i in queries]
query_tokens = tokenizer(queries_with_prefix, padding=True, truncation=True, return_tensors='pt', max_length=512)

documents = ['The Data Cloud!', 'Mexico City of Course!']
document_tokens =  tokenizer(documents, padding=True, truncation=True, return_tensors='pt', max_length=512)

# Compute token embeddings
with torch.no_grad():
    query_embeddings = model(**query_tokens)[0][:, 0]
    document_embeddings = model(**document_tokens)[0][:, 0]


# normalize embeddings
query_embeddings = torch.nn.functional.normalize(query_embeddings, p=2, dim=1)
document_embeddings = torch.nn.functional.normalize(document_embeddings, p=2, dim=1)

scores = torch.mm(query_embeddings, document_embeddings.transpose(0, 1))
for query, query_scores in zip(queries, scores):
    doc_score_pairs = list(zip(documents, query_scores))
    doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)
    #Output passages & scores
    print("Query:", query)
    for document, score in doc_score_pairs:
        print(score, document)
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
const extractor = await pipeline('feature-extraction', 'Snowflake/snowflake-arctic-embed-xs', {
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
console.log(similarities); // [0.5044895661144148, 0.5636021124426508]
```

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