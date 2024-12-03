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
- name: snowflake-arctic-embed-m
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
      value: 76.80597014925374
    - type: ap
      value: 39.31198155789558
    - type: f1
      value: 70.48198448222148
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
      value: 82.831525
    - type: ap
      value: 77.4474050181638
    - type: f1
      value: 82.77204845110204
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
      value: 38.93000000000001
    - type: f1
      value: 37.98013371053459
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
      value: 31.223
    - type: map_at_10
      value: 47.43
    - type: map_at_100
      value: 48.208
    - type: map_at_1000
      value: 48.211
    - type: map_at_3
      value: 42.579
    - type: map_at_5
      value: 45.263999999999996
    - type: mrr_at_1
      value: 31.65
    - type: mrr_at_10
      value: 47.573
    - type: mrr_at_100
      value: 48.359
    - type: mrr_at_1000
      value: 48.362
    - type: mrr_at_3
      value: 42.734
    - type: mrr_at_5
      value: 45.415
    - type: ndcg_at_1
      value: 31.223
    - type: ndcg_at_10
      value: 56.436
    - type: ndcg_at_100
      value: 59.657000000000004
    - type: ndcg_at_1000
      value: 59.731
    - type: ndcg_at_3
      value: 46.327
    - type: ndcg_at_5
      value: 51.178000000000004
    - type: precision_at_1
      value: 31.223
    - type: precision_at_10
      value: 8.527999999999999
    - type: precision_at_100
      value: 0.991
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 19.061
    - type: precision_at_5
      value: 13.797999999999998
    - type: recall_at_1
      value: 31.223
    - type: recall_at_10
      value: 85.277
    - type: recall_at_100
      value: 99.075
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 57.18299999999999
    - type: recall_at_5
      value: 68.99
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
      value: 47.23625429411296
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
      value: 37.433880471403654
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
      value: 60.53175025582013
    - type: mrr
      value: 74.51160796728664
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
      value: 88.93746103286769
    - type: cos_sim_spearman
      value: 86.62245567912619
    - type: euclidean_pearson
      value: 87.154173907501
    - type: euclidean_spearman
      value: 86.62245567912619
    - type: manhattan_pearson
      value: 87.17682026633462
    - type: manhattan_spearman
      value: 86.74775973908348
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
      value: 80.33766233766232
    - type: f1
      value: 79.64931422442245
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
      value: 19.116028913890613
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
      value: 36.966921852810174
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
      value: 31.98019698537654
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
      value: 34.079
    - type: map_at_10
      value: 46.35
    - type: map_at_100
      value: 47.785
    - type: map_at_1000
      value: 47.903
    - type: map_at_3
      value: 42.620999999999995
    - type: map_at_5
      value: 44.765
    - type: mrr_at_1
      value: 41.345
    - type: mrr_at_10
      value: 52.032000000000004
    - type: mrr_at_100
      value: 52.690000000000005
    - type: mrr_at_1000
      value: 52.727999999999994
    - type: mrr_at_3
      value: 49.428
    - type: mrr_at_5
      value: 51.093999999999994
    - type: ndcg_at_1
      value: 41.345
    - type: ndcg_at_10
      value: 53.027
    - type: ndcg_at_100
      value: 57.962
    - type: ndcg_at_1000
      value: 59.611999999999995
    - type: ndcg_at_3
      value: 47.687000000000005
    - type: ndcg_at_5
      value: 50.367
    - type: precision_at_1
      value: 41.345
    - type: precision_at_10
      value: 10.157
    - type: precision_at_100
      value: 1.567
    - type: precision_at_1000
      value: 0.199
    - type: precision_at_3
      value: 23.081
    - type: precision_at_5
      value: 16.738
    - type: recall_at_1
      value: 34.079
    - type: recall_at_10
      value: 65.93900000000001
    - type: recall_at_100
      value: 86.42699999999999
    - type: recall_at_1000
      value: 96.61
    - type: recall_at_3
      value: 50.56699999999999
    - type: recall_at_5
      value: 57.82000000000001
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
      value: 33.289
    - type: map_at_10
      value: 43.681
    - type: map_at_100
      value: 45.056000000000004
    - type: map_at_1000
      value: 45.171
    - type: map_at_3
      value: 40.702
    - type: map_at_5
      value: 42.292
    - type: mrr_at_1
      value: 41.146
    - type: mrr_at_10
      value: 49.604
    - type: mrr_at_100
      value: 50.28399999999999
    - type: mrr_at_1000
      value: 50.322
    - type: mrr_at_3
      value: 47.611
    - type: mrr_at_5
      value: 48.717
    - type: ndcg_at_1
      value: 41.146
    - type: ndcg_at_10
      value: 49.43
    - type: ndcg_at_100
      value: 54.01899999999999
    - type: ndcg_at_1000
      value: 55.803000000000004
    - type: ndcg_at_3
      value: 45.503
    - type: ndcg_at_5
      value: 47.198
    - type: precision_at_1
      value: 41.146
    - type: precision_at_10
      value: 9.268
    - type: precision_at_100
      value: 1.4749999999999999
    - type: precision_at_1000
      value: 0.19
    - type: precision_at_3
      value: 21.932
    - type: precision_at_5
      value: 15.389
    - type: recall_at_1
      value: 33.289
    - type: recall_at_10
      value: 59.209999999999994
    - type: recall_at_100
      value: 78.676
    - type: recall_at_1000
      value: 89.84100000000001
    - type: recall_at_3
      value: 47.351
    - type: recall_at_5
      value: 52.178999999999995
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
      value: 44.483
    - type: map_at_10
      value: 56.862
    - type: map_at_100
      value: 57.901
    - type: map_at_1000
      value: 57.948
    - type: map_at_3
      value: 53.737
    - type: map_at_5
      value: 55.64
    - type: mrr_at_1
      value: 50.658
    - type: mrr_at_10
      value: 60.281
    - type: mrr_at_100
      value: 60.946
    - type: mrr_at_1000
      value: 60.967000000000006
    - type: mrr_at_3
      value: 58.192
    - type: mrr_at_5
      value: 59.531
    - type: ndcg_at_1
      value: 50.658
    - type: ndcg_at_10
      value: 62.339
    - type: ndcg_at_100
      value: 66.28399999999999
    - type: ndcg_at_1000
      value: 67.166
    - type: ndcg_at_3
      value: 57.458
    - type: ndcg_at_5
      value: 60.112
    - type: precision_at_1
      value: 50.658
    - type: precision_at_10
      value: 9.762
    - type: precision_at_100
      value: 1.26
    - type: precision_at_1000
      value: 0.13799999999999998
    - type: precision_at_3
      value: 25.329
    - type: precision_at_5
      value: 17.254
    - type: recall_at_1
      value: 44.483
    - type: recall_at_10
      value: 74.819
    - type: recall_at_100
      value: 91.702
    - type: recall_at_1000
      value: 97.84
    - type: recall_at_3
      value: 62.13999999999999
    - type: recall_at_5
      value: 68.569
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
      value: 26.489
    - type: map_at_10
      value: 37.004999999999995
    - type: map_at_100
      value: 38.001000000000005
    - type: map_at_1000
      value: 38.085
    - type: map_at_3
      value: 34.239999999999995
    - type: map_at_5
      value: 35.934
    - type: mrr_at_1
      value: 28.362
    - type: mrr_at_10
      value: 38.807
    - type: mrr_at_100
      value: 39.671
    - type: mrr_at_1000
      value: 39.736
    - type: mrr_at_3
      value: 36.29
    - type: mrr_at_5
      value: 37.906
    - type: ndcg_at_1
      value: 28.362
    - type: ndcg_at_10
      value: 42.510999999999996
    - type: ndcg_at_100
      value: 47.226
    - type: ndcg_at_1000
      value: 49.226
    - type: ndcg_at_3
      value: 37.295
    - type: ndcg_at_5
      value: 40.165
    - type: precision_at_1
      value: 28.362
    - type: precision_at_10
      value: 6.633
    - type: precision_at_100
      value: 0.9490000000000001
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 16.234
    - type: precision_at_5
      value: 11.434999999999999
    - type: recall_at_1
      value: 26.489
    - type: recall_at_10
      value: 57.457
    - type: recall_at_100
      value: 78.712
    - type: recall_at_1000
      value: 93.565
    - type: recall_at_3
      value: 43.748
    - type: recall_at_5
      value: 50.589
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
      value: 12.418999999999999
    - type: map_at_10
      value: 22.866
    - type: map_at_100
      value: 24.365000000000002
    - type: map_at_1000
      value: 24.479
    - type: map_at_3
      value: 19.965
    - type: map_at_5
      value: 21.684
    - type: mrr_at_1
      value: 14.677000000000001
    - type: mrr_at_10
      value: 26.316
    - type: mrr_at_100
      value: 27.514
    - type: mrr_at_1000
      value: 27.57
    - type: mrr_at_3
      value: 23.3
    - type: mrr_at_5
      value: 25.191000000000003
    - type: ndcg_at_1
      value: 14.677000000000001
    - type: ndcg_at_10
      value: 28.875
    - type: ndcg_at_100
      value: 35.607
    - type: ndcg_at_1000
      value: 38.237
    - type: ndcg_at_3
      value: 23.284
    - type: ndcg_at_5
      value: 26.226
    - type: precision_at_1
      value: 14.677000000000001
    - type: precision_at_10
      value: 5.771
    - type: precision_at_100
      value: 1.058
    - type: precision_at_1000
      value: 0.14200000000000002
    - type: precision_at_3
      value: 11.940000000000001
    - type: precision_at_5
      value: 9.229
    - type: recall_at_1
      value: 12.418999999999999
    - type: recall_at_10
      value: 43.333
    - type: recall_at_100
      value: 71.942
    - type: recall_at_1000
      value: 90.67399999999999
    - type: recall_at_3
      value: 28.787000000000003
    - type: recall_at_5
      value: 35.638
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
      value: 31.686999999999998
    - type: map_at_10
      value: 42.331
    - type: map_at_100
      value: 43.655
    - type: map_at_1000
      value: 43.771
    - type: map_at_3
      value: 38.944
    - type: map_at_5
      value: 40.991
    - type: mrr_at_1
      value: 37.921
    - type: mrr_at_10
      value: 47.534
    - type: mrr_at_100
      value: 48.362
    - type: mrr_at_1000
      value: 48.405
    - type: mrr_at_3
      value: 44.995000000000005
    - type: mrr_at_5
      value: 46.617
    - type: ndcg_at_1
      value: 37.921
    - type: ndcg_at_10
      value: 48.236000000000004
    - type: ndcg_at_100
      value: 53.705000000000005
    - type: ndcg_at_1000
      value: 55.596000000000004
    - type: ndcg_at_3
      value: 43.11
    - type: ndcg_at_5
      value: 45.862
    - type: precision_at_1
      value: 37.921
    - type: precision_at_10
      value: 8.643
    - type: precision_at_100
      value: 1.336
    - type: precision_at_1000
      value: 0.166
    - type: precision_at_3
      value: 20.308
    - type: precision_at_5
      value: 14.514
    - type: recall_at_1
      value: 31.686999999999998
    - type: recall_at_10
      value: 60.126999999999995
    - type: recall_at_100
      value: 83.10600000000001
    - type: recall_at_1000
      value: 95.15
    - type: recall_at_3
      value: 46.098
    - type: recall_at_5
      value: 53.179
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
      value: 28.686
    - type: map_at_10
      value: 39.146
    - type: map_at_100
      value: 40.543
    - type: map_at_1000
      value: 40.644999999999996
    - type: map_at_3
      value: 36.195
    - type: map_at_5
      value: 37.919000000000004
    - type: mrr_at_1
      value: 35.160000000000004
    - type: mrr_at_10
      value: 44.711
    - type: mrr_at_100
      value: 45.609
    - type: mrr_at_1000
      value: 45.655
    - type: mrr_at_3
      value: 42.409
    - type: mrr_at_5
      value: 43.779
    - type: ndcg_at_1
      value: 35.160000000000004
    - type: ndcg_at_10
      value: 44.977000000000004
    - type: ndcg_at_100
      value: 50.663000000000004
    - type: ndcg_at_1000
      value: 52.794
    - type: ndcg_at_3
      value: 40.532000000000004
    - type: ndcg_at_5
      value: 42.641
    - type: precision_at_1
      value: 35.160000000000004
    - type: precision_at_10
      value: 8.014000000000001
    - type: precision_at_100
      value: 1.269
    - type: precision_at_1000
      value: 0.163
    - type: precision_at_3
      value: 19.444
    - type: precision_at_5
      value: 13.653
    - type: recall_at_1
      value: 28.686
    - type: recall_at_10
      value: 56.801
    - type: recall_at_100
      value: 80.559
    - type: recall_at_1000
      value: 95.052
    - type: recall_at_3
      value: 43.675999999999995
    - type: recall_at_5
      value: 49.703
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
      value: 28.173833333333338
    - type: map_at_10
      value: 38.202083333333334
    - type: map_at_100
      value: 39.47475
    - type: map_at_1000
      value: 39.586499999999994
    - type: map_at_3
      value: 35.17308333333334
    - type: map_at_5
      value: 36.914
    - type: mrr_at_1
      value: 32.92958333333333
    - type: mrr_at_10
      value: 42.16758333333333
    - type: mrr_at_100
      value: 43.04108333333333
    - type: mrr_at_1000
      value: 43.092499999999994
    - type: mrr_at_3
      value: 39.69166666666666
    - type: mrr_at_5
      value: 41.19458333333333
    - type: ndcg_at_1
      value: 32.92958333333333
    - type: ndcg_at_10
      value: 43.80583333333333
    - type: ndcg_at_100
      value: 49.060916666666664
    - type: ndcg_at_1000
      value: 51.127250000000004
    - type: ndcg_at_3
      value: 38.80383333333333
    - type: ndcg_at_5
      value: 41.29658333333333
    - type: precision_at_1
      value: 32.92958333333333
    - type: precision_at_10
      value: 7.655666666666666
    - type: precision_at_100
      value: 1.2094166666666668
    - type: precision_at_1000
      value: 0.15750000000000003
    - type: precision_at_3
      value: 17.87975
    - type: precision_at_5
      value: 12.741833333333332
    - type: recall_at_1
      value: 28.173833333333338
    - type: recall_at_10
      value: 56.219249999999995
    - type: recall_at_100
      value: 79.01416666666665
    - type: recall_at_1000
      value: 93.13425000000001
    - type: recall_at_3
      value: 42.39241666666667
    - type: recall_at_5
      value: 48.764833333333335
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
      value: 25.625999999999998
    - type: map_at_10
      value: 32.808
    - type: map_at_100
      value: 33.951
    - type: map_at_1000
      value: 34.052
    - type: map_at_3
      value: 30.536
    - type: map_at_5
      value: 31.77
    - type: mrr_at_1
      value: 28.374
    - type: mrr_at_10
      value: 35.527
    - type: mrr_at_100
      value: 36.451
    - type: mrr_at_1000
      value: 36.522
    - type: mrr_at_3
      value: 33.410000000000004
    - type: mrr_at_5
      value: 34.537
    - type: ndcg_at_1
      value: 28.374
    - type: ndcg_at_10
      value: 37.172
    - type: ndcg_at_100
      value: 42.474000000000004
    - type: ndcg_at_1000
      value: 44.853
    - type: ndcg_at_3
      value: 32.931
    - type: ndcg_at_5
      value: 34.882999999999996
    - type: precision_at_1
      value: 28.374
    - type: precision_at_10
      value: 5.813
    - type: precision_at_100
      value: 0.928
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 14.008000000000001
    - type: precision_at_5
      value: 9.754999999999999
    - type: recall_at_1
      value: 25.625999999999998
    - type: recall_at_10
      value: 47.812
    - type: recall_at_100
      value: 71.61800000000001
    - type: recall_at_1000
      value: 88.881
    - type: recall_at_3
      value: 35.876999999999995
    - type: recall_at_5
      value: 40.839
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
      value: 18.233
    - type: map_at_10
      value: 26.375999999999998
    - type: map_at_100
      value: 27.575
    - type: map_at_1000
      value: 27.706999999999997
    - type: map_at_3
      value: 23.619
    - type: map_at_5
      value: 25.217
    - type: mrr_at_1
      value: 22.023
    - type: mrr_at_10
      value: 30.122
    - type: mrr_at_100
      value: 31.083
    - type: mrr_at_1000
      value: 31.163999999999998
    - type: mrr_at_3
      value: 27.541
    - type: mrr_at_5
      value: 29.061999999999998
    - type: ndcg_at_1
      value: 22.023
    - type: ndcg_at_10
      value: 31.476
    - type: ndcg_at_100
      value: 37.114000000000004
    - type: ndcg_at_1000
      value: 39.981
    - type: ndcg_at_3
      value: 26.538
    - type: ndcg_at_5
      value: 29.016
    - type: precision_at_1
      value: 22.023
    - type: precision_at_10
      value: 5.819
    - type: precision_at_100
      value: 1.018
    - type: precision_at_1000
      value: 0.14300000000000002
    - type: precision_at_3
      value: 12.583
    - type: precision_at_5
      value: 9.36
    - type: recall_at_1
      value: 18.233
    - type: recall_at_10
      value: 43.029
    - type: recall_at_100
      value: 68.253
    - type: recall_at_1000
      value: 88.319
    - type: recall_at_3
      value: 29.541
    - type: recall_at_5
      value: 35.783
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
      value: 28.923
    - type: map_at_10
      value: 39.231
    - type: map_at_100
      value: 40.483000000000004
    - type: map_at_1000
      value: 40.575
    - type: map_at_3
      value: 35.94
    - type: map_at_5
      value: 37.683
    - type: mrr_at_1
      value: 33.955
    - type: mrr_at_10
      value: 43.163000000000004
    - type: mrr_at_100
      value: 44.054
    - type: mrr_at_1000
      value: 44.099
    - type: mrr_at_3
      value: 40.361000000000004
    - type: mrr_at_5
      value: 41.905
    - type: ndcg_at_1
      value: 33.955
    - type: ndcg_at_10
      value: 45.068000000000005
    - type: ndcg_at_100
      value: 50.470000000000006
    - type: ndcg_at_1000
      value: 52.349000000000004
    - type: ndcg_at_3
      value: 39.298
    - type: ndcg_at_5
      value: 41.821999999999996
    - type: precision_at_1
      value: 33.955
    - type: precision_at_10
      value: 7.649
    - type: precision_at_100
      value: 1.173
    - type: precision_at_1000
      value: 0.14200000000000002
    - type: precision_at_3
      value: 17.817
    - type: precision_at_5
      value: 12.537
    - type: recall_at_1
      value: 28.923
    - type: recall_at_10
      value: 58.934
    - type: recall_at_100
      value: 81.809
    - type: recall_at_1000
      value: 94.71300000000001
    - type: recall_at_3
      value: 42.975
    - type: recall_at_5
      value: 49.501
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
      value: 28.596
    - type: map_at_10
      value: 38.735
    - type: map_at_100
      value: 40.264
    - type: map_at_1000
      value: 40.48
    - type: map_at_3
      value: 35.394999999999996
    - type: map_at_5
      value: 37.099
    - type: mrr_at_1
      value: 33.992
    - type: mrr_at_10
      value: 43.076
    - type: mrr_at_100
      value: 44.005
    - type: mrr_at_1000
      value: 44.043
    - type: mrr_at_3
      value: 40.415
    - type: mrr_at_5
      value: 41.957
    - type: ndcg_at_1
      value: 33.992
    - type: ndcg_at_10
      value: 44.896
    - type: ndcg_at_100
      value: 50.44499999999999
    - type: ndcg_at_1000
      value: 52.675000000000004
    - type: ndcg_at_3
      value: 39.783
    - type: ndcg_at_5
      value: 41.997
    - type: precision_at_1
      value: 33.992
    - type: precision_at_10
      value: 8.498
    - type: precision_at_100
      value: 1.585
    - type: precision_at_1000
      value: 0.248
    - type: precision_at_3
      value: 18.511
    - type: precision_at_5
      value: 13.241
    - type: recall_at_1
      value: 28.596
    - type: recall_at_10
      value: 56.885
    - type: recall_at_100
      value: 82.306
    - type: recall_at_1000
      value: 95.813
    - type: recall_at_3
      value: 42.168
    - type: recall_at_5
      value: 48.32
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
      value: 25.576
    - type: map_at_10
      value: 33.034
    - type: map_at_100
      value: 34.117999999999995
    - type: map_at_1000
      value: 34.222
    - type: map_at_3
      value: 30.183
    - type: map_at_5
      value: 31.974000000000004
    - type: mrr_at_1
      value: 27.542
    - type: mrr_at_10
      value: 34.838
    - type: mrr_at_100
      value: 35.824
    - type: mrr_at_1000
      value: 35.899
    - type: mrr_at_3
      value: 32.348
    - type: mrr_at_5
      value: 34.039
    - type: ndcg_at_1
      value: 27.542
    - type: ndcg_at_10
      value: 37.663000000000004
    - type: ndcg_at_100
      value: 42.762
    - type: ndcg_at_1000
      value: 45.235
    - type: ndcg_at_3
      value: 32.227
    - type: ndcg_at_5
      value: 35.27
    - type: precision_at_1
      value: 27.542
    - type: precision_at_10
      value: 5.840999999999999
    - type: precision_at_100
      value: 0.895
    - type: precision_at_1000
      value: 0.123
    - type: precision_at_3
      value: 13.370000000000001
    - type: precision_at_5
      value: 9.797
    - type: recall_at_1
      value: 25.576
    - type: recall_at_10
      value: 50.285000000000004
    - type: recall_at_100
      value: 73.06
    - type: recall_at_1000
      value: 91.15299999999999
    - type: recall_at_3
      value: 35.781
    - type: recall_at_5
      value: 43.058
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
      value: 17.061
    - type: map_at_10
      value: 29.464000000000002
    - type: map_at_100
      value: 31.552999999999997
    - type: map_at_1000
      value: 31.707
    - type: map_at_3
      value: 24.834999999999997
    - type: map_at_5
      value: 27.355
    - type: mrr_at_1
      value: 38.958
    - type: mrr_at_10
      value: 51.578
    - type: mrr_at_100
      value: 52.262
    - type: mrr_at_1000
      value: 52.283
    - type: mrr_at_3
      value: 48.599
    - type: mrr_at_5
      value: 50.404
    - type: ndcg_at_1
      value: 38.958
    - type: ndcg_at_10
      value: 39.367999999999995
    - type: ndcg_at_100
      value: 46.521
    - type: ndcg_at_1000
      value: 49.086999999999996
    - type: ndcg_at_3
      value: 33.442
    - type: ndcg_at_5
      value: 35.515
    - type: precision_at_1
      value: 38.958
    - type: precision_at_10
      value: 12.110999999999999
    - type: precision_at_100
      value: 1.982
    - type: precision_at_1000
      value: 0.247
    - type: precision_at_3
      value: 25.102999999999998
    - type: precision_at_5
      value: 18.971
    - type: recall_at_1
      value: 17.061
    - type: recall_at_10
      value: 45.198
    - type: recall_at_100
      value: 69.18900000000001
    - type: recall_at_1000
      value: 83.38499999999999
    - type: recall_at_3
      value: 30.241
    - type: recall_at_5
      value: 36.851
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
      value: 9.398
    - type: map_at_10
      value: 21.421
    - type: map_at_100
      value: 31.649
    - type: map_at_1000
      value: 33.469
    - type: map_at_3
      value: 15.310000000000002
    - type: map_at_5
      value: 17.946
    - type: mrr_at_1
      value: 71
    - type: mrr_at_10
      value: 78.92099999999999
    - type: mrr_at_100
      value: 79.225
    - type: mrr_at_1000
      value: 79.23
    - type: mrr_at_3
      value: 77.792
    - type: mrr_at_5
      value: 78.467
    - type: ndcg_at_1
      value: 57.99999999999999
    - type: ndcg_at_10
      value: 44.733000000000004
    - type: ndcg_at_100
      value: 50.646
    - type: ndcg_at_1000
      value: 57.903999999999996
    - type: ndcg_at_3
      value: 49.175999999999995
    - type: ndcg_at_5
      value: 46.800999999999995
    - type: precision_at_1
      value: 71
    - type: precision_at_10
      value: 36.25
    - type: precision_at_100
      value: 12.135
    - type: precision_at_1000
      value: 2.26
    - type: precision_at_3
      value: 52.75
    - type: precision_at_5
      value: 45.65
    - type: recall_at_1
      value: 9.398
    - type: recall_at_10
      value: 26.596999999999998
    - type: recall_at_100
      value: 57.943
    - type: recall_at_1000
      value: 81.147
    - type: recall_at_3
      value: 16.634
    - type: recall_at_5
      value: 20.7
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
      value: 46.535000000000004
    - type: f1
      value: 42.53702746452163
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
      value: 77.235
    - type: map_at_10
      value: 85.504
    - type: map_at_100
      value: 85.707
    - type: map_at_1000
      value: 85.718
    - type: map_at_3
      value: 84.425
    - type: map_at_5
      value: 85.13
    - type: mrr_at_1
      value: 83.363
    - type: mrr_at_10
      value: 89.916
    - type: mrr_at_100
      value: 89.955
    - type: mrr_at_1000
      value: 89.956
    - type: mrr_at_3
      value: 89.32600000000001
    - type: mrr_at_5
      value: 89.79
    - type: ndcg_at_1
      value: 83.363
    - type: ndcg_at_10
      value: 89.015
    - type: ndcg_at_100
      value: 89.649
    - type: ndcg_at_1000
      value: 89.825
    - type: ndcg_at_3
      value: 87.45100000000001
    - type: ndcg_at_5
      value: 88.39399999999999
    - type: precision_at_1
      value: 83.363
    - type: precision_at_10
      value: 10.659
    - type: precision_at_100
      value: 1.122
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 33.338
    - type: precision_at_5
      value: 20.671999999999997
    - type: recall_at_1
      value: 77.235
    - type: recall_at_10
      value: 95.389
    - type: recall_at_100
      value: 97.722
    - type: recall_at_1000
      value: 98.744
    - type: recall_at_3
      value: 91.19800000000001
    - type: recall_at_5
      value: 93.635
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
      value: 20.835
    - type: map_at_10
      value: 34.459
    - type: map_at_100
      value: 36.335
    - type: map_at_1000
      value: 36.518
    - type: map_at_3
      value: 30.581000000000003
    - type: map_at_5
      value: 32.859
    - type: mrr_at_1
      value: 40.894999999999996
    - type: mrr_at_10
      value: 50.491
    - type: mrr_at_100
      value: 51.243
    - type: mrr_at_1000
      value: 51.286
    - type: mrr_at_3
      value: 47.994
    - type: mrr_at_5
      value: 49.429
    - type: ndcg_at_1
      value: 40.894999999999996
    - type: ndcg_at_10
      value: 42.403
    - type: ndcg_at_100
      value: 48.954
    - type: ndcg_at_1000
      value: 51.961
    - type: ndcg_at_3
      value: 39.11
    - type: ndcg_at_5
      value: 40.152
    - type: precision_at_1
      value: 40.894999999999996
    - type: precision_at_10
      value: 11.466
    - type: precision_at_100
      value: 1.833
    - type: precision_at_1000
      value: 0.23700000000000002
    - type: precision_at_3
      value: 25.874000000000002
    - type: precision_at_5
      value: 19.012
    - type: recall_at_1
      value: 20.835
    - type: recall_at_10
      value: 49.535000000000004
    - type: recall_at_100
      value: 73.39099999999999
    - type: recall_at_1000
      value: 91.01599999999999
    - type: recall_at_3
      value: 36.379
    - type: recall_at_5
      value: 42.059999999999995
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
      value: 40.945
    - type: map_at_10
      value: 65.376
    - type: map_at_100
      value: 66.278
    - type: map_at_1000
      value: 66.33
    - type: map_at_3
      value: 61.753
    - type: map_at_5
      value: 64.077
    - type: mrr_at_1
      value: 81.891
    - type: mrr_at_10
      value: 87.256
    - type: mrr_at_100
      value: 87.392
    - type: mrr_at_1000
      value: 87.395
    - type: mrr_at_3
      value: 86.442
    - type: mrr_at_5
      value: 86.991
    - type: ndcg_at_1
      value: 81.891
    - type: ndcg_at_10
      value: 73.654
    - type: ndcg_at_100
      value: 76.62299999999999
    - type: ndcg_at_1000
      value: 77.60000000000001
    - type: ndcg_at_3
      value: 68.71199999999999
    - type: ndcg_at_5
      value: 71.563
    - type: precision_at_1
      value: 81.891
    - type: precision_at_10
      value: 15.409
    - type: precision_at_100
      value: 1.77
    - type: precision_at_1000
      value: 0.19
    - type: precision_at_3
      value: 44.15
    - type: precision_at_5
      value: 28.732000000000003
    - type: recall_at_1
      value: 40.945
    - type: recall_at_10
      value: 77.04299999999999
    - type: recall_at_100
      value: 88.508
    - type: recall_at_1000
      value: 94.943
    - type: recall_at_3
      value: 66.226
    - type: recall_at_5
      value: 71.83
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
      value: 74.08200000000001
    - type: ap
      value: 68.10929101713998
    - type: f1
      value: 73.98447117652009
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
      value: 21.729000000000003
    - type: map_at_10
      value: 34.602
    - type: map_at_100
      value: 35.756
    - type: map_at_1000
      value: 35.803000000000004
    - type: map_at_3
      value: 30.619000000000003
    - type: map_at_5
      value: 32.914
    - type: mrr_at_1
      value: 22.364
    - type: mrr_at_10
      value: 35.183
    - type: mrr_at_100
      value: 36.287000000000006
    - type: mrr_at_1000
      value: 36.327999999999996
    - type: mrr_at_3
      value: 31.258000000000003
    - type: mrr_at_5
      value: 33.542
    - type: ndcg_at_1
      value: 22.364
    - type: ndcg_at_10
      value: 41.765
    - type: ndcg_at_100
      value: 47.293
    - type: ndcg_at_1000
      value: 48.457
    - type: ndcg_at_3
      value: 33.676
    - type: ndcg_at_5
      value: 37.783
    - type: precision_at_1
      value: 22.364
    - type: precision_at_10
      value: 6.662
    - type: precision_at_100
      value: 0.943
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 14.435999999999998
    - type: precision_at_5
      value: 10.764999999999999
    - type: recall_at_1
      value: 21.729000000000003
    - type: recall_at_10
      value: 63.815999999999995
    - type: recall_at_100
      value: 89.265
    - type: recall_at_1000
      value: 98.149
    - type: recall_at_3
      value: 41.898
    - type: recall_at_5
      value: 51.76500000000001
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
      value: 92.73141814865483
    - type: f1
      value: 92.17518476408004
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
      value: 65.18011855905152
    - type: f1
      value: 46.70999638311856
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
      value: 75.24261603375525
    - type: f1
      value: 74.07895183913367
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
      value: 28.43855875387446
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
      value: 29.05331990256969
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
      value: 66.92333557498318
    - type: f1
      value: 64.29789389602692
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
      value: 72.74714189643578
    - type: f1
      value: 71.672585608315
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
      value: 31.503564225501613
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
      value: 28.410225127136457
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
      value: 29.170019896091908
    - type: mrr
      value: 29.881276831500976
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
      value: 6.544
    - type: map_at_10
      value: 14.116999999999999
    - type: map_at_100
      value: 17.522
    - type: map_at_1000
      value: 19
    - type: map_at_3
      value: 10.369
    - type: map_at_5
      value: 12.189
    - type: mrr_at_1
      value: 47.988
    - type: mrr_at_10
      value: 56.84
    - type: mrr_at_100
      value: 57.367000000000004
    - type: mrr_at_1000
      value: 57.403000000000006
    - type: mrr_at_3
      value: 54.592
    - type: mrr_at_5
      value: 56.233
    - type: ndcg_at_1
      value: 45.82
    - type: ndcg_at_10
      value: 36.767
    - type: ndcg_at_100
      value: 33.356
    - type: ndcg_at_1000
      value: 42.062
    - type: ndcg_at_3
      value: 42.15
    - type: ndcg_at_5
      value: 40.355000000000004
    - type: precision_at_1
      value: 47.988
    - type: precision_at_10
      value: 27.121000000000002
    - type: precision_at_100
      value: 8.455
    - type: precision_at_1000
      value: 2.103
    - type: precision_at_3
      value: 39.628
    - type: precision_at_5
      value: 35.356
    - type: recall_at_1
      value: 6.544
    - type: recall_at_10
      value: 17.928
    - type: recall_at_100
      value: 32.843
    - type: recall_at_1000
      value: 65.752
    - type: recall_at_3
      value: 11.297
    - type: recall_at_5
      value: 14.357000000000001
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
      value: 39.262
    - type: map_at_10
      value: 55.095000000000006
    - type: map_at_100
      value: 55.93900000000001
    - type: map_at_1000
      value: 55.955999999999996
    - type: map_at_3
      value: 50.93
    - type: map_at_5
      value: 53.491
    - type: mrr_at_1
      value: 43.598
    - type: mrr_at_10
      value: 57.379999999999995
    - type: mrr_at_100
      value: 57.940999999999995
    - type: mrr_at_1000
      value: 57.952000000000005
    - type: mrr_at_3
      value: 53.998000000000005
    - type: mrr_at_5
      value: 56.128
    - type: ndcg_at_1
      value: 43.598
    - type: ndcg_at_10
      value: 62.427
    - type: ndcg_at_100
      value: 65.759
    - type: ndcg_at_1000
      value: 66.133
    - type: ndcg_at_3
      value: 54.745999999999995
    - type: ndcg_at_5
      value: 58.975
    - type: precision_at_1
      value: 43.598
    - type: precision_at_10
      value: 9.789
    - type: precision_at_100
      value: 1.171
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 24.295
    - type: precision_at_5
      value: 17.028
    - type: recall_at_1
      value: 39.262
    - type: recall_at_10
      value: 82.317
    - type: recall_at_100
      value: 96.391
    - type: recall_at_1000
      value: 99.116
    - type: recall_at_3
      value: 62.621
    - type: recall_at_5
      value: 72.357
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
      value: 78.17500000000001
    - type: f1
      value: 78.01940892857273
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
      value: 61
    - type: cos_sim_ap
      value: 59.630757252602464
    - type: cos_sim_f1
      value: 62.37521514629949
    - type: cos_sim_precision
      value: 45.34534534534534
    - type: cos_sim_recall
      value: 99.88974641675854
    - type: dot_accuracy
      value: 61
    - type: dot_ap
      value: 59.631527308059006
    - type: dot_f1
      value: 62.37521514629949
    - type: dot_precision
      value: 45.34534534534534
    - type: dot_recall
      value: 99.88974641675854
    - type: euclidean_accuracy
      value: 61
    - type: euclidean_ap
      value: 59.630757252602464
    - type: euclidean_f1
      value: 62.37521514629949
    - type: euclidean_precision
      value: 45.34534534534534
    - type: euclidean_recall
      value: 99.88974641675854
    - type: manhattan_accuracy
      value: 60.9
    - type: manhattan_ap
      value: 59.613947780462254
    - type: manhattan_f1
      value: 62.37521514629949
    - type: manhattan_precision
      value: 45.34534534534534
    - type: manhattan_recall
      value: 99.88974641675854
    - type: max_accuracy
      value: 61
    - type: max_ap
      value: 59.631527308059006
    - type: max_f1
      value: 62.37521514629949
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
      value: 69.963
    - type: map_at_10
      value: 83.59400000000001
    - type: map_at_100
      value: 84.236
    - type: map_at_1000
      value: 84.255
    - type: map_at_3
      value: 80.69800000000001
    - type: map_at_5
      value: 82.568
    - type: mrr_at_1
      value: 80.58999999999999
    - type: mrr_at_10
      value: 86.78200000000001
    - type: mrr_at_100
      value: 86.89099999999999
    - type: mrr_at_1000
      value: 86.893
    - type: mrr_at_3
      value: 85.757
    - type: mrr_at_5
      value: 86.507
    - type: ndcg_at_1
      value: 80.60000000000001
    - type: ndcg_at_10
      value: 87.41799999999999
    - type: ndcg_at_100
      value: 88.723
    - type: ndcg_at_1000
      value: 88.875
    - type: ndcg_at_3
      value: 84.565
    - type: ndcg_at_5
      value: 86.236
    - type: precision_at_1
      value: 80.60000000000001
    - type: precision_at_10
      value: 13.239
    - type: precision_at_100
      value: 1.5150000000000001
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 36.947
    - type: precision_at_5
      value: 24.354
    - type: recall_at_1
      value: 69.963
    - type: recall_at_10
      value: 94.553
    - type: recall_at_100
      value: 99.104
    - type: recall_at_1000
      value: 99.872
    - type: recall_at_3
      value: 86.317
    - type: recall_at_5
      value: 91.023
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
      value: 47.52890410998761
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
      value: 62.760692287940486
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
      value: 5.093
    - type: map_at_10
      value: 12.695
    - type: map_at_100
      value: 14.824000000000002
    - type: map_at_1000
      value: 15.123000000000001
    - type: map_at_3
      value: 8.968
    - type: map_at_5
      value: 10.828
    - type: mrr_at_1
      value: 25.1
    - type: mrr_at_10
      value: 35.894999999999996
    - type: mrr_at_100
      value: 36.966
    - type: mrr_at_1000
      value: 37.019999999999996
    - type: mrr_at_3
      value: 32.467
    - type: mrr_at_5
      value: 34.416999999999994
    - type: ndcg_at_1
      value: 25.1
    - type: ndcg_at_10
      value: 21.096999999999998
    - type: ndcg_at_100
      value: 29.202
    - type: ndcg_at_1000
      value: 34.541
    - type: ndcg_at_3
      value: 19.875
    - type: ndcg_at_5
      value: 17.497
    - type: precision_at_1
      value: 25.1
    - type: precision_at_10
      value: 10.9
    - type: precision_at_100
      value: 2.255
    - type: precision_at_1000
      value: 0.35400000000000004
    - type: precision_at_3
      value: 18.367
    - type: precision_at_5
      value: 15.299999999999999
    - type: recall_at_1
      value: 5.093
    - type: recall_at_10
      value: 22.092
    - type: recall_at_100
      value: 45.778
    - type: recall_at_1000
      value: 71.985
    - type: recall_at_3
      value: 11.167
    - type: recall_at_5
      value: 15.501999999999999
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
      value: 74.04386981759481
    - type: cos_sim_spearman
      value: 69.12484963763646
    - type: euclidean_pearson
      value: 71.49384353291062
    - type: euclidean_spearman
      value: 69.12484548317074
    - type: manhattan_pearson
      value: 71.49828173987272
    - type: manhattan_spearman
      value: 69.08350274367014
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
      value: 66.95372527615659
    - type: cos_sim_spearman
      value: 66.96821894433991
    - type: euclidean_pearson
      value: 64.675348002074
    - type: euclidean_spearman
      value: 66.96821894433991
    - type: manhattan_pearson
      value: 64.5965887073831
    - type: manhattan_spearman
      value: 66.88569076794741
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
      value: 77.34698437961983
    - type: cos_sim_spearman
      value: 79.1153001117325
    - type: euclidean_pearson
      value: 78.53562874696966
    - type: euclidean_spearman
      value: 79.11530018205724
    - type: manhattan_pearson
      value: 78.46484988944093
    - type: manhattan_spearman
      value: 79.01416027493104
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
      value: 68.81220371935373
    - type: cos_sim_spearman
      value: 68.50538405089604
    - type: euclidean_pearson
      value: 68.69204272683749
    - type: euclidean_spearman
      value: 68.50534223912419
    - type: manhattan_pearson
      value: 68.67300120149523
    - type: manhattan_spearman
      value: 68.45404301623115
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
      value: 78.2464678879813
    - type: cos_sim_spearman
      value: 79.92003940566667
    - type: euclidean_pearson
      value: 79.8080778793964
    - type: euclidean_spearman
      value: 79.92003940566667
    - type: manhattan_pearson
      value: 79.80153621444681
    - type: manhattan_spearman
      value: 79.91293261418134
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
      value: 76.31179207708662
    - type: cos_sim_spearman
      value: 78.65597349856115
    - type: euclidean_pearson
      value: 78.76937027472678
    - type: euclidean_spearman
      value: 78.65597349856115
    - type: manhattan_pearson
      value: 78.77129513300605
    - type: manhattan_spearman
      value: 78.62640467680775
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
      value: 79.43158429552561
    - type: cos_sim_spearman
      value: 81.46108646565362
    - type: euclidean_pearson
      value: 81.47071791452292
    - type: euclidean_spearman
      value: 81.46108646565362
    - type: manhattan_pearson
      value: 81.56920643846031
    - type: manhattan_spearman
      value: 81.42226241399516
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
      value: 66.89546474141514
    - type: cos_sim_spearman
      value: 65.8393752170531
    - type: euclidean_pearson
      value: 67.2580522762307
    - type: euclidean_spearman
      value: 65.8393752170531
    - type: manhattan_pearson
      value: 67.45157729300522
    - type: manhattan_spearman
      value: 66.19470854403802
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
      value: 71.39566306334434
    - type: cos_sim_spearman
      value: 74.0981396086974
    - type: euclidean_pearson
      value: 73.7834496259745
    - type: euclidean_spearman
      value: 74.09803741302046
    - type: manhattan_pearson
      value: 73.79958138780945
    - type: manhattan_spearman
      value: 74.09894837555905
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
      value: 71.39566311006806
    - type: cos_sim_spearman
      value: 74.0981396086974
    - type: euclidean_pearson
      value: 73.78344970897099
    - type: euclidean_spearman
      value: 74.09803741302046
    - type: manhattan_pearson
      value: 73.79958147136705
    - type: manhattan_spearman
      value: 74.09894837555905
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
      value: 80.81059564334683
    - type: mrr
      value: 94.62696617108381
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
      value: 57.760999999999996
    - type: map_at_10
      value: 68.614
    - type: map_at_100
      value: 69.109
    - type: map_at_1000
      value: 69.134
    - type: map_at_3
      value: 65.735
    - type: map_at_5
      value: 67.42099999999999
    - type: mrr_at_1
      value: 60.667
    - type: mrr_at_10
      value: 69.94200000000001
    - type: mrr_at_100
      value: 70.254
    - type: mrr_at_1000
      value: 70.28
    - type: mrr_at_3
      value: 67.72200000000001
    - type: mrr_at_5
      value: 69.18900000000001
    - type: ndcg_at_1
      value: 60.667
    - type: ndcg_at_10
      value: 73.548
    - type: ndcg_at_100
      value: 75.381
    - type: ndcg_at_1000
      value: 75.991
    - type: ndcg_at_3
      value: 68.685
    - type: ndcg_at_5
      value: 71.26
    - type: precision_at_1
      value: 60.667
    - type: precision_at_10
      value: 9.833
    - type: precision_at_100
      value: 1.08
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 26.889000000000003
    - type: precision_at_5
      value: 17.8
    - type: recall_at_1
      value: 57.760999999999996
    - type: recall_at_10
      value: 87.13300000000001
    - type: recall_at_100
      value: 95
    - type: recall_at_1000
      value: 99.667
    - type: recall_at_3
      value: 74.211
    - type: recall_at_5
      value: 80.63900000000001
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
      value: 99.81881188118813
    - type: cos_sim_ap
      value: 95.21196473745837
    - type: cos_sim_f1
      value: 90.69767441860465
    - type: cos_sim_precision
      value: 91.71779141104295
    - type: cos_sim_recall
      value: 89.7
    - type: dot_accuracy
      value: 99.81881188118813
    - type: dot_ap
      value: 95.21196473745837
    - type: dot_f1
      value: 90.69767441860465
    - type: dot_precision
      value: 91.71779141104295
    - type: dot_recall
      value: 89.7
    - type: euclidean_accuracy
      value: 99.81881188118813
    - type: euclidean_ap
      value: 95.21196473745839
    - type: euclidean_f1
      value: 90.69767441860465
    - type: euclidean_precision
      value: 91.71779141104295
    - type: euclidean_recall
      value: 89.7
    - type: manhattan_accuracy
      value: 99.81287128712871
    - type: manhattan_ap
      value: 95.16667174835017
    - type: manhattan_f1
      value: 90.41095890410959
    - type: manhattan_precision
      value: 91.7610710607621
    - type: manhattan_recall
      value: 89.1
    - type: max_accuracy
      value: 99.81881188118813
    - type: max_ap
      value: 95.21196473745839
    - type: max_f1
      value: 90.69767441860465
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
      value: 59.54942204515638
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
      value: 39.42892282672948
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
      value: 51.189033075914324
    - type: mrr
      value: 51.97014790764791
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
      value: 30.09466569775977
    - type: cos_sim_spearman
      value: 30.31058660775912
    - type: dot_pearson
      value: 30.09466438861689
    - type: dot_spearman
      value: 30.31058660775912
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
      value: 0.253
    - type: map_at_10
      value: 2.07
    - type: map_at_100
      value: 12.679000000000002
    - type: map_at_1000
      value: 30.412
    - type: map_at_3
      value: 0.688
    - type: map_at_5
      value: 1.079
    - type: mrr_at_1
      value: 96
    - type: mrr_at_10
      value: 98
    - type: mrr_at_100
      value: 98
    - type: mrr_at_1000
      value: 98
    - type: mrr_at_3
      value: 98
    - type: mrr_at_5
      value: 98
    - type: ndcg_at_1
      value: 89
    - type: ndcg_at_10
      value: 79.646
    - type: ndcg_at_100
      value: 62.217999999999996
    - type: ndcg_at_1000
      value: 55.13400000000001
    - type: ndcg_at_3
      value: 83.458
    - type: ndcg_at_5
      value: 80.982
    - type: precision_at_1
      value: 96
    - type: precision_at_10
      value: 84.6
    - type: precision_at_100
      value: 64.34
    - type: precision_at_1000
      value: 24.534
    - type: precision_at_3
      value: 88.667
    - type: precision_at_5
      value: 85.6
    - type: recall_at_1
      value: 0.253
    - type: recall_at_10
      value: 2.253
    - type: recall_at_100
      value: 15.606
    - type: recall_at_1000
      value: 51.595
    - type: recall_at_3
      value: 0.7100000000000001
    - type: recall_at_5
      value: 1.139
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
      value: 3.0540000000000003
    - type: map_at_10
      value: 13.078999999999999
    - type: map_at_100
      value: 19.468
    - type: map_at_1000
      value: 21.006
    - type: map_at_3
      value: 6.8629999999999995
    - type: map_at_5
      value: 9.187
    - type: mrr_at_1
      value: 42.857
    - type: mrr_at_10
      value: 56.735
    - type: mrr_at_100
      value: 57.352000000000004
    - type: mrr_at_1000
      value: 57.352000000000004
    - type: mrr_at_3
      value: 52.721
    - type: mrr_at_5
      value: 54.66
    - type: ndcg_at_1
      value: 38.775999999999996
    - type: ndcg_at_10
      value: 31.469
    - type: ndcg_at_100
      value: 42.016999999999996
    - type: ndcg_at_1000
      value: 52.60399999999999
    - type: ndcg_at_3
      value: 35.894
    - type: ndcg_at_5
      value: 33.873
    - type: precision_at_1
      value: 42.857
    - type: precision_at_10
      value: 27.346999999999998
    - type: precision_at_100
      value: 8.327
    - type: precision_at_1000
      value: 1.551
    - type: precision_at_3
      value: 36.735
    - type: precision_at_5
      value: 33.469
    - type: recall_at_1
      value: 3.0540000000000003
    - type: recall_at_10
      value: 19.185
    - type: recall_at_100
      value: 51.056000000000004
    - type: recall_at_1000
      value: 82.814
    - type: recall_at_3
      value: 7.961
    - type: recall_at_5
      value: 11.829
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
      value: 64.9346
    - type: ap
      value: 12.121605736777527
    - type: f1
      value: 50.169902005887955
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
      value: 56.72608941709111
    - type: f1
      value: 57.0702928875253
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
      value: 37.72671554400943
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
      value: 82.84556237706384
    - type: cos_sim_ap
      value: 63.28364215788651
    - type: cos_sim_f1
      value: 60.00000000000001
    - type: cos_sim_precision
      value: 54.45161290322581
    - type: cos_sim_recall
      value: 66.80738786279683
    - type: dot_accuracy
      value: 82.84556237706384
    - type: dot_ap
      value: 63.28364302860433
    - type: dot_f1
      value: 60.00000000000001
    - type: dot_precision
      value: 54.45161290322581
    - type: dot_recall
      value: 66.80738786279683
    - type: euclidean_accuracy
      value: 82.84556237706384
    - type: euclidean_ap
      value: 63.28363625097978
    - type: euclidean_f1
      value: 60.00000000000001
    - type: euclidean_precision
      value: 54.45161290322581
    - type: euclidean_recall
      value: 66.80738786279683
    - type: manhattan_accuracy
      value: 82.86940454193241
    - type: manhattan_ap
      value: 63.244773709836764
    - type: manhattan_f1
      value: 60.12680942696495
    - type: manhattan_precision
      value: 55.00109433136353
    - type: manhattan_recall
      value: 66.3060686015831
    - type: max_accuracy
      value: 82.86940454193241
    - type: max_ap
      value: 63.28364302860433
    - type: max_f1
      value: 60.12680942696495
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
      value: 88.32033220786278
    - type: cos_sim_ap
      value: 84.71928176006863
    - type: cos_sim_f1
      value: 76.51483333969684
    - type: cos_sim_precision
      value: 75.89184276300841
    - type: cos_sim_recall
      value: 77.14813674160764
    - type: dot_accuracy
      value: 88.32033220786278
    - type: dot_ap
      value: 84.71928330149228
    - type: dot_f1
      value: 76.51483333969684
    - type: dot_precision
      value: 75.89184276300841
    - type: dot_recall
      value: 77.14813674160764
    - type: euclidean_accuracy
      value: 88.32033220786278
    - type: euclidean_ap
      value: 84.71928045384345
    - type: euclidean_f1
      value: 76.51483333969684
    - type: euclidean_precision
      value: 75.89184276300841
    - type: euclidean_recall
      value: 77.14813674160764
    - type: manhattan_accuracy
      value: 88.27570147863545
    - type: manhattan_ap
      value: 84.68523541579755
    - type: manhattan_f1
      value: 76.51512269355146
    - type: manhattan_precision
      value: 75.62608107091825
    - type: manhattan_recall
      value: 77.42531567600862
    - type: max_accuracy
      value: 88.32033220786278
    - type: max_ap
      value: 84.71928330149228
    - type: max_f1
      value: 76.51512269355146
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
      value: 85.30624598674467
license: apache-2.0
---
<h1 align="center">Snowflake's Arctic-embed-m</h1>
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


Based on the [intfloat/e5-small-unsupervised](https://huggingface.co/intfloat/e5-small-unsupervised) model, this small model does not trade off retrieval accuracy for its small size. With only 33m parameters and 384 dimensions, this model should easily allow scaling to large datasets.


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


Based on the [nomic-ai/nomic-embed-text-v1-unsupervised](https://huggingface.co/nomic-ai/nomic-embed-text-v1-unsupervised) model, this long-context variant of our medium-sized model is perfect for workloads that can be constrained by the regular 512 token context of our other models. Without the use of RPE, this model supports up to 2048 tokens. With RPE, it can scale to 8192!


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

model = SentenceTransformer("Snowflake/snowflake-arctic-embed-m")

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
0.20051965 The Data Cloud!
0.07660701 Mexico City of Course!
Query: Where can I get the best tacos?
0.24481852 Mexico City of Course!
0.15664819 The Data Cloud!
```

### Using Huggingface transformers


You can use the transformers package to use an snowflake-arctic-embed model, as shown below. For optimal retrieval quality, use the CLS token to embed each text portion and use the query prefix below (just on the query).



```python
import torch
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Snowflake/snowflake-arctic-embed-m')
model = AutoModel.from_pretrained('Snowflake/snowflake-arctic-embed-m', add_pooling_layer=False)
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
const extractor = await pipeline('feature-extraction', 'Snowflake/snowflake-arctic-embed-m', {
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
