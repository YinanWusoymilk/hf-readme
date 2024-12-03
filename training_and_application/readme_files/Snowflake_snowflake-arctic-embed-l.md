---
license: apache-2.0
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
- name: snowflake-arctic-embed-l
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
      value: 74.80597014925374
    - type: ap
      value: 37.911466766189875
    - type: f1
      value: 68.88606927542106
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
      value: 78.402275
    - type: ap
      value: 73.03294793248114
    - type: f1
      value: 78.3147786132161
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
      value: 36.717999999999996
    - type: f1
      value: 35.918044248787766
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
      value: 34.495
    - type: map_at_10
      value: 50.236000000000004
    - type: map_at_100
      value: 50.944
    - type: map_at_1000
      value: 50.94499999999999
    - type: map_at_3
      value: 45.341
    - type: map_at_5
      value: 48.286
    - type: mrr_at_1
      value: 35.135
    - type: mrr_at_10
      value: 50.471
    - type: mrr_at_100
      value: 51.185
    - type: mrr_at_1000
      value: 51.187000000000005
    - type: mrr_at_3
      value: 45.602
    - type: mrr_at_5
      value: 48.468
    - type: ndcg_at_1
      value: 34.495
    - type: ndcg_at_10
      value: 59.086000000000006
    - type: ndcg_at_100
      value: 61.937
    - type: ndcg_at_1000
      value: 61.966
    - type: ndcg_at_3
      value: 49.062
    - type: ndcg_at_5
      value: 54.367
    - type: precision_at_1
      value: 34.495
    - type: precision_at_10
      value: 8.734
    - type: precision_at_100
      value: 0.9939999999999999
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 19.962
    - type: precision_at_5
      value: 14.552000000000001
    - type: recall_at_1
      value: 34.495
    - type: recall_at_10
      value: 87.33999999999999
    - type: recall_at_100
      value: 99.431
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 59.885999999999996
    - type: recall_at_5
      value: 72.76
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
      value: 47.46440874635501
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
      value: 38.28720154213723
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
      value: 60.34614226394902
    - type: mrr
      value: 75.05628105351096
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
      value: 87.41072716728198
    - type: cos_sim_spearman
      value: 86.34534093114372
    - type: euclidean_pearson
      value: 85.34009667750838
    - type: euclidean_spearman
      value: 86.34534093114372
    - type: manhattan_pearson
      value: 85.2158833586889
    - type: manhattan_spearman
      value: 86.60920236509224
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
      value: 80.06493506493507
    - type: f1
      value: 79.28108600339833
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
      value: 20.545049432417287
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
      value: 37.54369718479804
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
      value: 32.64941588219162
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
      value: 37.264
    - type: map_at_10
      value: 49.43
    - type: map_at_100
      value: 50.967
    - type: map_at_1000
      value: 51.08200000000001
    - type: map_at_3
      value: 45.742
    - type: map_at_5
      value: 47.764
    - type: mrr_at_1
      value: 44.921
    - type: mrr_at_10
      value: 54.879999999999995
    - type: mrr_at_100
      value: 55.525000000000006
    - type: mrr_at_1000
      value: 55.565
    - type: mrr_at_3
      value: 52.480000000000004
    - type: mrr_at_5
      value: 53.86
    - type: ndcg_at_1
      value: 44.921
    - type: ndcg_at_10
      value: 55.664
    - type: ndcg_at_100
      value: 60.488
    - type: ndcg_at_1000
      value: 62.138000000000005
    - type: ndcg_at_3
      value: 50.797000000000004
    - type: ndcg_at_5
      value: 52.94799999999999
    - type: precision_at_1
      value: 44.921
    - type: precision_at_10
      value: 10.587
    - type: precision_at_100
      value: 1.629
    - type: precision_at_1000
      value: 0.203
    - type: precision_at_3
      value: 24.034
    - type: precision_at_5
      value: 17.224999999999998
    - type: recall_at_1
      value: 37.264
    - type: recall_at_10
      value: 67.15
    - type: recall_at_100
      value: 86.811
    - type: recall_at_1000
      value: 97.172
    - type: recall_at_3
      value: 53.15800000000001
    - type: recall_at_5
      value: 59.116
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
      value: 36.237
    - type: map_at_10
      value: 47.941
    - type: map_at_100
      value: 49.131
    - type: map_at_1000
      value: 49.26
    - type: map_at_3
      value: 44.561
    - type: map_at_5
      value: 46.28
    - type: mrr_at_1
      value: 45.605000000000004
    - type: mrr_at_10
      value: 54.039
    - type: mrr_at_100
      value: 54.653
    - type: mrr_at_1000
      value: 54.688
    - type: mrr_at_3
      value: 52.006
    - type: mrr_at_5
      value: 53.096
    - type: ndcg_at_1
      value: 45.605000000000004
    - type: ndcg_at_10
      value: 53.916
    - type: ndcg_at_100
      value: 57.745999999999995
    - type: ndcg_at_1000
      value: 59.492999999999995
    - type: ndcg_at_3
      value: 49.774
    - type: ndcg_at_5
      value: 51.434999999999995
    - type: precision_at_1
      value: 45.605000000000004
    - type: precision_at_10
      value: 10.229000000000001
    - type: precision_at_100
      value: 1.55
    - type: precision_at_1000
      value: 0.2
    - type: precision_at_3
      value: 24.098
    - type: precision_at_5
      value: 16.726
    - type: recall_at_1
      value: 36.237
    - type: recall_at_10
      value: 64.03
    - type: recall_at_100
      value: 80.423
    - type: recall_at_1000
      value: 91.03
    - type: recall_at_3
      value: 51.20400000000001
    - type: recall_at_5
      value: 56.298
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
      value: 47.278
    - type: map_at_10
      value: 59.757000000000005
    - type: map_at_100
      value: 60.67
    - type: map_at_1000
      value: 60.714
    - type: map_at_3
      value: 56.714
    - type: map_at_5
      value: 58.453
    - type: mrr_at_1
      value: 53.73
    - type: mrr_at_10
      value: 62.970000000000006
    - type: mrr_at_100
      value: 63.507999999999996
    - type: mrr_at_1000
      value: 63.53
    - type: mrr_at_3
      value: 60.909
    - type: mrr_at_5
      value: 62.172000000000004
    - type: ndcg_at_1
      value: 53.73
    - type: ndcg_at_10
      value: 64.97
    - type: ndcg_at_100
      value: 68.394
    - type: ndcg_at_1000
      value: 69.255
    - type: ndcg_at_3
      value: 60.228
    - type: ndcg_at_5
      value: 62.617999999999995
    - type: precision_at_1
      value: 53.73
    - type: precision_at_10
      value: 10.056
    - type: precision_at_100
      value: 1.265
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_3
      value: 26.332
    - type: precision_at_5
      value: 17.743000000000002
    - type: recall_at_1
      value: 47.278
    - type: recall_at_10
      value: 76.86500000000001
    - type: recall_at_100
      value: 91.582
    - type: recall_at_1000
      value: 97.583
    - type: recall_at_3
      value: 64.443
    - type: recall_at_5
      value: 70.283
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
      value: 29.702
    - type: map_at_10
      value: 39.463
    - type: map_at_100
      value: 40.508
    - type: map_at_1000
      value: 40.579
    - type: map_at_3
      value: 36.748999999999995
    - type: map_at_5
      value: 38.296
    - type: mrr_at_1
      value: 31.977
    - type: mrr_at_10
      value: 41.739
    - type: mrr_at_100
      value: 42.586
    - type: mrr_at_1000
      value: 42.636
    - type: mrr_at_3
      value: 39.096
    - type: mrr_at_5
      value: 40.695
    - type: ndcg_at_1
      value: 31.977
    - type: ndcg_at_10
      value: 44.855000000000004
    - type: ndcg_at_100
      value: 49.712
    - type: ndcg_at_1000
      value: 51.443000000000005
    - type: ndcg_at_3
      value: 39.585
    - type: ndcg_at_5
      value: 42.244
    - type: precision_at_1
      value: 31.977
    - type: precision_at_10
      value: 6.768000000000001
    - type: precision_at_100
      value: 0.9690000000000001
    - type: precision_at_1000
      value: 0.116
    - type: precision_at_3
      value: 16.761
    - type: precision_at_5
      value: 11.593
    - type: recall_at_1
      value: 29.702
    - type: recall_at_10
      value: 59.082
    - type: recall_at_100
      value: 80.92
    - type: recall_at_1000
      value: 93.728
    - type: recall_at_3
      value: 45.212
    - type: recall_at_5
      value: 51.449
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
      value: 21.336
    - type: map_at_10
      value: 30.137999999999998
    - type: map_at_100
      value: 31.385
    - type: map_at_1000
      value: 31.495
    - type: map_at_3
      value: 27.481
    - type: map_at_5
      value: 28.772
    - type: mrr_at_1
      value: 25.871
    - type: mrr_at_10
      value: 34.686
    - type: mrr_at_100
      value: 35.649
    - type: mrr_at_1000
      value: 35.705
    - type: mrr_at_3
      value: 32.09
    - type: mrr_at_5
      value: 33.52
    - type: ndcg_at_1
      value: 25.871
    - type: ndcg_at_10
      value: 35.617
    - type: ndcg_at_100
      value: 41.272999999999996
    - type: ndcg_at_1000
      value: 43.725
    - type: ndcg_at_3
      value: 30.653999999999996
    - type: ndcg_at_5
      value: 32.714
    - type: precision_at_1
      value: 25.871
    - type: precision_at_10
      value: 6.4799999999999995
    - type: precision_at_100
      value: 1.0699999999999998
    - type: precision_at_1000
      value: 0.13999999999999999
    - type: precision_at_3
      value: 14.469000000000001
    - type: precision_at_5
      value: 10.274
    - type: recall_at_1
      value: 21.336
    - type: recall_at_10
      value: 47.746
    - type: recall_at_100
      value: 71.773
    - type: recall_at_1000
      value: 89.05199999999999
    - type: recall_at_3
      value: 34.172999999999995
    - type: recall_at_5
      value: 39.397999999999996
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
      value: 34.424
    - type: map_at_10
      value: 45.647999999999996
    - type: map_at_100
      value: 46.907
    - type: map_at_1000
      value: 47.010999999999996
    - type: map_at_3
      value: 42.427
    - type: map_at_5
      value: 44.285000000000004
    - type: mrr_at_1
      value: 41.867
    - type: mrr_at_10
      value: 51.17699999999999
    - type: mrr_at_100
      value: 51.937
    - type: mrr_at_1000
      value: 51.975
    - type: mrr_at_3
      value: 48.941
    - type: mrr_at_5
      value: 50.322
    - type: ndcg_at_1
      value: 41.867
    - type: ndcg_at_10
      value: 51.534
    - type: ndcg_at_100
      value: 56.696999999999996
    - type: ndcg_at_1000
      value: 58.475
    - type: ndcg_at_3
      value: 46.835
    - type: ndcg_at_5
      value: 49.161
    - type: precision_at_1
      value: 41.867
    - type: precision_at_10
      value: 9.134
    - type: precision_at_100
      value: 1.362
    - type: precision_at_1000
      value: 0.17099999999999999
    - type: precision_at_3
      value: 22.073
    - type: precision_at_5
      value: 15.495999999999999
    - type: recall_at_1
      value: 34.424
    - type: recall_at_10
      value: 63.237
    - type: recall_at_100
      value: 84.774
    - type: recall_at_1000
      value: 95.987
    - type: recall_at_3
      value: 49.888
    - type: recall_at_5
      value: 55.940999999999995
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
      value: 30.72
    - type: map_at_10
      value: 41.327999999999996
    - type: map_at_100
      value: 42.651
    - type: map_at_1000
      value: 42.739
    - type: map_at_3
      value: 38.223
    - type: map_at_5
      value: 40.053
    - type: mrr_at_1
      value: 37.9
    - type: mrr_at_10
      value: 46.857
    - type: mrr_at_100
      value: 47.673
    - type: mrr_at_1000
      value: 47.711999999999996
    - type: mrr_at_3
      value: 44.292
    - type: mrr_at_5
      value: 45.845
    - type: ndcg_at_1
      value: 37.9
    - type: ndcg_at_10
      value: 47.105999999999995
    - type: ndcg_at_100
      value: 52.56999999999999
    - type: ndcg_at_1000
      value: 54.37800000000001
    - type: ndcg_at_3
      value: 42.282
    - type: ndcg_at_5
      value: 44.646
    - type: precision_at_1
      value: 37.9
    - type: precision_at_10
      value: 8.368
    - type: precision_at_100
      value: 1.283
    - type: precision_at_1000
      value: 0.16
    - type: precision_at_3
      value: 20.015
    - type: precision_at_5
      value: 14.132
    - type: recall_at_1
      value: 30.72
    - type: recall_at_10
      value: 58.826
    - type: recall_at_100
      value: 82.104
    - type: recall_at_1000
      value: 94.194
    - type: recall_at_3
      value: 44.962999999999994
    - type: recall_at_5
      value: 51.426
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
      value: 31.656583333333334
    - type: map_at_10
      value: 41.59883333333333
    - type: map_at_100
      value: 42.80350000000001
    - type: map_at_1000
      value: 42.91075
    - type: map_at_3
      value: 38.68908333333333
    - type: map_at_5
      value: 40.27733333333334
    - type: mrr_at_1
      value: 37.23483333333334
    - type: mrr_at_10
      value: 45.782000000000004
    - type: mrr_at_100
      value: 46.577083333333334
    - type: mrr_at_1000
      value: 46.62516666666667
    - type: mrr_at_3
      value: 43.480666666666664
    - type: mrr_at_5
      value: 44.79833333333333
    - type: ndcg_at_1
      value: 37.23483333333334
    - type: ndcg_at_10
      value: 46.971500000000006
    - type: ndcg_at_100
      value: 51.90125
    - type: ndcg_at_1000
      value: 53.86366666666667
    - type: ndcg_at_3
      value: 42.31791666666667
    - type: ndcg_at_5
      value: 44.458666666666666
    - type: precision_at_1
      value: 37.23483333333334
    - type: precision_at_10
      value: 8.044583333333332
    - type: precision_at_100
      value: 1.2334166666666666
    - type: precision_at_1000
      value: 0.15925
    - type: precision_at_3
      value: 19.240833333333327
    - type: precision_at_5
      value: 13.435083333333333
    - type: recall_at_1
      value: 31.656583333333334
    - type: recall_at_10
      value: 58.44758333333333
    - type: recall_at_100
      value: 79.93658333333332
    - type: recall_at_1000
      value: 93.32491666666668
    - type: recall_at_3
      value: 45.44266666666667
    - type: recall_at_5
      value: 50.99866666666666
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
      value: 28.247
    - type: map_at_10
      value: 35.443999999999996
    - type: map_at_100
      value: 36.578
    - type: map_at_1000
      value: 36.675999999999995
    - type: map_at_3
      value: 33.276
    - type: map_at_5
      value: 34.536
    - type: mrr_at_1
      value: 31.747999999999998
    - type: mrr_at_10
      value: 38.413000000000004
    - type: mrr_at_100
      value: 39.327
    - type: mrr_at_1000
      value: 39.389
    - type: mrr_at_3
      value: 36.401
    - type: mrr_at_5
      value: 37.543
    - type: ndcg_at_1
      value: 31.747999999999998
    - type: ndcg_at_10
      value: 39.646
    - type: ndcg_at_100
      value: 44.861000000000004
    - type: ndcg_at_1000
      value: 47.197
    - type: ndcg_at_3
      value: 35.764
    - type: ndcg_at_5
      value: 37.635999999999996
    - type: precision_at_1
      value: 31.747999999999998
    - type: precision_at_10
      value: 6.12
    - type: precision_at_100
      value: 0.942
    - type: precision_at_1000
      value: 0.123
    - type: precision_at_3
      value: 15.235000000000001
    - type: precision_at_5
      value: 10.491
    - type: recall_at_1
      value: 28.247
    - type: recall_at_10
      value: 49.456
    - type: recall_at_100
      value: 73.02499999999999
    - type: recall_at_1000
      value: 89.898
    - type: recall_at_3
      value: 38.653999999999996
    - type: recall_at_5
      value: 43.259
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
      value: 22.45
    - type: map_at_10
      value: 30.476999999999997
    - type: map_at_100
      value: 31.630999999999997
    - type: map_at_1000
      value: 31.755
    - type: map_at_3
      value: 27.989000000000004
    - type: map_at_5
      value: 29.410999999999998
    - type: mrr_at_1
      value: 26.979
    - type: mrr_at_10
      value: 34.316
    - type: mrr_at_100
      value: 35.272999999999996
    - type: mrr_at_1000
      value: 35.342
    - type: mrr_at_3
      value: 32.14
    - type: mrr_at_5
      value: 33.405
    - type: ndcg_at_1
      value: 26.979
    - type: ndcg_at_10
      value: 35.166
    - type: ndcg_at_100
      value: 40.583000000000006
    - type: ndcg_at_1000
      value: 43.282
    - type: ndcg_at_3
      value: 30.916
    - type: ndcg_at_5
      value: 32.973
    - type: precision_at_1
      value: 26.979
    - type: precision_at_10
      value: 6.132
    - type: precision_at_100
      value: 1.047
    - type: precision_at_1000
      value: 0.145
    - type: precision_at_3
      value: 14.360999999999999
    - type: precision_at_5
      value: 10.227
    - type: recall_at_1
      value: 22.45
    - type: recall_at_10
      value: 45.348
    - type: recall_at_100
      value: 69.484
    - type: recall_at_1000
      value: 88.628
    - type: recall_at_3
      value: 33.338
    - type: recall_at_5
      value: 38.746
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
      value: 32.123000000000005
    - type: map_at_10
      value: 41.778
    - type: map_at_100
      value: 42.911
    - type: map_at_1000
      value: 42.994
    - type: map_at_3
      value: 38.558
    - type: map_at_5
      value: 40.318
    - type: mrr_at_1
      value: 37.687
    - type: mrr_at_10
      value: 45.889
    - type: mrr_at_100
      value: 46.672999999999995
    - type: mrr_at_1000
      value: 46.72
    - type: mrr_at_3
      value: 43.33
    - type: mrr_at_5
      value: 44.734
    - type: ndcg_at_1
      value: 37.687
    - type: ndcg_at_10
      value: 47.258
    - type: ndcg_at_100
      value: 52.331
    - type: ndcg_at_1000
      value: 54.152
    - type: ndcg_at_3
      value: 41.857
    - type: ndcg_at_5
      value: 44.283
    - type: precision_at_1
      value: 37.687
    - type: precision_at_10
      value: 7.892
    - type: precision_at_100
      value: 1.183
    - type: precision_at_1000
      value: 0.14300000000000002
    - type: precision_at_3
      value: 18.781
    - type: precision_at_5
      value: 13.134
    - type: recall_at_1
      value: 32.123000000000005
    - type: recall_at_10
      value: 59.760000000000005
    - type: recall_at_100
      value: 81.652
    - type: recall_at_1000
      value: 94.401
    - type: recall_at_3
      value: 44.996
    - type: recall_at_5
      value: 51.184
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
      value: 33.196999999999996
    - type: map_at_10
      value: 42.012
    - type: map_at_100
      value: 43.663999999999994
    - type: map_at_1000
      value: 43.883
    - type: map_at_3
      value: 39.33
    - type: map_at_5
      value: 40.586
    - type: mrr_at_1
      value: 39.328
    - type: mrr_at_10
      value: 46.57
    - type: mrr_at_100
      value: 47.508
    - type: mrr_at_1000
      value: 47.558
    - type: mrr_at_3
      value: 44.532
    - type: mrr_at_5
      value: 45.58
    - type: ndcg_at_1
      value: 39.328
    - type: ndcg_at_10
      value: 47.337
    - type: ndcg_at_100
      value: 52.989
    - type: ndcg_at_1000
      value: 55.224
    - type: ndcg_at_3
      value: 43.362
    - type: ndcg_at_5
      value: 44.866
    - type: precision_at_1
      value: 39.328
    - type: precision_at_10
      value: 8.577
    - type: precision_at_100
      value: 1.5789999999999997
    - type: precision_at_1000
      value: 0.25
    - type: precision_at_3
      value: 19.697
    - type: precision_at_5
      value: 13.755
    - type: recall_at_1
      value: 33.196999999999996
    - type: recall_at_10
      value: 56.635000000000005
    - type: recall_at_100
      value: 81.882
    - type: recall_at_1000
      value: 95.342
    - type: recall_at_3
      value: 44.969
    - type: recall_at_5
      value: 49.266
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
      value: 26.901000000000003
    - type: map_at_10
      value: 35.77
    - type: map_at_100
      value: 36.638999999999996
    - type: map_at_1000
      value: 36.741
    - type: map_at_3
      value: 33.219
    - type: map_at_5
      value: 34.574
    - type: mrr_at_1
      value: 29.205
    - type: mrr_at_10
      value: 37.848
    - type: mrr_at_100
      value: 38.613
    - type: mrr_at_1000
      value: 38.682
    - type: mrr_at_3
      value: 35.551
    - type: mrr_at_5
      value: 36.808
    - type: ndcg_at_1
      value: 29.205
    - type: ndcg_at_10
      value: 40.589
    - type: ndcg_at_100
      value: 45.171
    - type: ndcg_at_1000
      value: 47.602
    - type: ndcg_at_3
      value: 35.760999999999996
    - type: ndcg_at_5
      value: 37.980000000000004
    - type: precision_at_1
      value: 29.205
    - type: precision_at_10
      value: 6.192
    - type: precision_at_100
      value: 0.922
    - type: precision_at_1000
      value: 0.123
    - type: precision_at_3
      value: 15.034
    - type: precision_at_5
      value: 10.424999999999999
    - type: recall_at_1
      value: 26.901000000000003
    - type: recall_at_10
      value: 53.236000000000004
    - type: recall_at_100
      value: 74.809
    - type: recall_at_1000
      value: 92.884
    - type: recall_at_3
      value: 40.314
    - type: recall_at_5
      value: 45.617999999999995
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
      value: 16.794999999999998
    - type: map_at_10
      value: 29.322
    - type: map_at_100
      value: 31.463
    - type: map_at_1000
      value: 31.643
    - type: map_at_3
      value: 24.517
    - type: map_at_5
      value: 27.237000000000002
    - type: mrr_at_1
      value: 37.655
    - type: mrr_at_10
      value: 50.952
    - type: mrr_at_100
      value: 51.581999999999994
    - type: mrr_at_1000
      value: 51.61
    - type: mrr_at_3
      value: 47.991
    - type: mrr_at_5
      value: 49.744
    - type: ndcg_at_1
      value: 37.655
    - type: ndcg_at_10
      value: 39.328
    - type: ndcg_at_100
      value: 46.358
    - type: ndcg_at_1000
      value: 49.245
    - type: ndcg_at_3
      value: 33.052
    - type: ndcg_at_5
      value: 35.407
    - type: precision_at_1
      value: 37.655
    - type: precision_at_10
      value: 12.202
    - type: precision_at_100
      value: 1.9789999999999999
    - type: precision_at_1000
      value: 0.252
    - type: precision_at_3
      value: 24.973
    - type: precision_at_5
      value: 19.075
    - type: recall_at_1
      value: 16.794999999999998
    - type: recall_at_10
      value: 45.716
    - type: recall_at_100
      value: 68.919
    - type: recall_at_1000
      value: 84.71600000000001
    - type: recall_at_3
      value: 30.135
    - type: recall_at_5
      value: 37.141999999999996
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
      value: 9.817
    - type: map_at_10
      value: 22.058
    - type: map_at_100
      value: 31.805
    - type: map_at_1000
      value: 33.562999999999995
    - type: map_at_3
      value: 15.537
    - type: map_at_5
      value: 18.199
    - type: mrr_at_1
      value: 72.75
    - type: mrr_at_10
      value: 79.804
    - type: mrr_at_100
      value: 80.089
    - type: mrr_at_1000
      value: 80.09100000000001
    - type: mrr_at_3
      value: 78.75
    - type: mrr_at_5
      value: 79.325
    - type: ndcg_at_1
      value: 59.875
    - type: ndcg_at_10
      value: 45.972
    - type: ndcg_at_100
      value: 51.092999999999996
    - type: ndcg_at_1000
      value: 58.048
    - type: ndcg_at_3
      value: 50.552
    - type: ndcg_at_5
      value: 47.672
    - type: precision_at_1
      value: 72.75
    - type: precision_at_10
      value: 37.05
    - type: precision_at_100
      value: 12.005
    - type: precision_at_1000
      value: 2.221
    - type: precision_at_3
      value: 54.083000000000006
    - type: precision_at_5
      value: 46.2
    - type: recall_at_1
      value: 9.817
    - type: recall_at_10
      value: 27.877000000000002
    - type: recall_at_100
      value: 57.974000000000004
    - type: recall_at_1000
      value: 80.085
    - type: recall_at_3
      value: 16.911
    - type: recall_at_5
      value: 20.689
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
      value: 46.464999999999996
    - type: f1
      value: 42.759588662873796
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
      value: 75.82900000000001
    - type: map_at_10
      value: 84.613
    - type: map_at_100
      value: 84.845
    - type: map_at_1000
      value: 84.855
    - type: map_at_3
      value: 83.498
    - type: map_at_5
      value: 84.29299999999999
    - type: mrr_at_1
      value: 81.69800000000001
    - type: mrr_at_10
      value: 88.84100000000001
    - type: mrr_at_100
      value: 88.887
    - type: mrr_at_1000
      value: 88.888
    - type: mrr_at_3
      value: 88.179
    - type: mrr_at_5
      value: 88.69200000000001
    - type: ndcg_at_1
      value: 81.69800000000001
    - type: ndcg_at_10
      value: 88.21799999999999
    - type: ndcg_at_100
      value: 88.961
    - type: ndcg_at_1000
      value: 89.131
    - type: ndcg_at_3
      value: 86.591
    - type: ndcg_at_5
      value: 87.666
    - type: precision_at_1
      value: 81.69800000000001
    - type: precision_at_10
      value: 10.615
    - type: precision_at_100
      value: 1.125
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 33.208
    - type: precision_at_5
      value: 20.681
    - type: recall_at_1
      value: 75.82900000000001
    - type: recall_at_10
      value: 94.97
    - type: recall_at_100
      value: 97.786
    - type: recall_at_1000
      value: 98.809
    - type: recall_at_3
      value: 90.625
    - type: recall_at_5
      value: 93.345
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
      value: 22.788
    - type: map_at_10
      value: 36.71
    - type: map_at_100
      value: 38.527
    - type: map_at_1000
      value: 38.701
    - type: map_at_3
      value: 32.318999999999996
    - type: map_at_5
      value: 34.809
    - type: mrr_at_1
      value: 44.444
    - type: mrr_at_10
      value: 52.868
    - type: mrr_at_100
      value: 53.52400000000001
    - type: mrr_at_1000
      value: 53.559999999999995
    - type: mrr_at_3
      value: 50.153999999999996
    - type: mrr_at_5
      value: 51.651
    - type: ndcg_at_1
      value: 44.444
    - type: ndcg_at_10
      value: 44.707
    - type: ndcg_at_100
      value: 51.174
    - type: ndcg_at_1000
      value: 53.996
    - type: ndcg_at_3
      value: 40.855999999999995
    - type: ndcg_at_5
      value: 42.113
    - type: precision_at_1
      value: 44.444
    - type: precision_at_10
      value: 12.021999999999998
    - type: precision_at_100
      value: 1.8950000000000002
    - type: precision_at_1000
      value: 0.241
    - type: precision_at_3
      value: 26.8
    - type: precision_at_5
      value: 19.66
    - type: recall_at_1
      value: 22.788
    - type: recall_at_10
      value: 51.793
    - type: recall_at_100
      value: 75.69500000000001
    - type: recall_at_1000
      value: 92.292
    - type: recall_at_3
      value: 37.375
    - type: recall_at_5
      value: 43.682
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
      value: 41.276
    - type: map_at_10
      value: 67.245
    - type: map_at_100
      value: 68.061
    - type: map_at_1000
      value: 68.11399999999999
    - type: map_at_3
      value: 63.693
    - type: map_at_5
      value: 65.90899999999999
    - type: mrr_at_1
      value: 82.552
    - type: mrr_at_10
      value: 87.741
    - type: mrr_at_100
      value: 87.868
    - type: mrr_at_1000
      value: 87.871
    - type: mrr_at_3
      value: 86.98599999999999
    - type: mrr_at_5
      value: 87.469
    - type: ndcg_at_1
      value: 82.552
    - type: ndcg_at_10
      value: 75.176
    - type: ndcg_at_100
      value: 77.902
    - type: ndcg_at_1000
      value: 78.852
    - type: ndcg_at_3
      value: 70.30499999999999
    - type: ndcg_at_5
      value: 73.00999999999999
    - type: precision_at_1
      value: 82.552
    - type: precision_at_10
      value: 15.765
    - type: precision_at_100
      value: 1.788
    - type: precision_at_1000
      value: 0.191
    - type: precision_at_3
      value: 45.375
    - type: precision_at_5
      value: 29.360999999999997
    - type: recall_at_1
      value: 41.276
    - type: recall_at_10
      value: 78.825
    - type: recall_at_100
      value: 89.41900000000001
    - type: recall_at_1000
      value: 95.625
    - type: recall_at_3
      value: 68.062
    - type: recall_at_5
      value: 73.40299999999999
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
      value: 72.876
    - type: ap
      value: 67.15477852410164
    - type: f1
      value: 72.65147370025373
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
      value: 21.748
    - type: map_at_10
      value: 34.626000000000005
    - type: map_at_100
      value: 35.813
    - type: map_at_1000
      value: 35.859
    - type: map_at_3
      value: 30.753000000000004
    - type: map_at_5
      value: 33.049
    - type: mrr_at_1
      value: 22.35
    - type: mrr_at_10
      value: 35.23
    - type: mrr_at_100
      value: 36.359
    - type: mrr_at_1000
      value: 36.399
    - type: mrr_at_3
      value: 31.436999999999998
    - type: mrr_at_5
      value: 33.687
    - type: ndcg_at_1
      value: 22.364
    - type: ndcg_at_10
      value: 41.677
    - type: ndcg_at_100
      value: 47.355999999999995
    - type: ndcg_at_1000
      value: 48.494
    - type: ndcg_at_3
      value: 33.85
    - type: ndcg_at_5
      value: 37.942
    - type: precision_at_1
      value: 22.364
    - type: precision_at_10
      value: 6.6000000000000005
    - type: precision_at_100
      value: 0.9450000000000001
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 14.527000000000001
    - type: precision_at_5
      value: 10.796999999999999
    - type: recall_at_1
      value: 21.748
    - type: recall_at_10
      value: 63.292
    - type: recall_at_100
      value: 89.427
    - type: recall_at_1000
      value: 98.13499999999999
    - type: recall_at_3
      value: 42.126000000000005
    - type: recall_at_5
      value: 51.968
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
      value: 92.62425900592795
    - type: f1
      value: 92.08497761553683
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
      value: 64.51436388508893
    - type: f1
      value: 45.884016531912906
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
      value: 76.57172995780591
    - type: f1
      value: 75.52979910878491
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
      value: 44.84052695201612
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
      value: 21.443971229936494
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
      value: 65.79354404841965
    - type: f1
      value: 63.17260074126185
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
      value: 71.09616677874916
    - type: f1
      value: 69.74285784421075
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
      value: 31.474709231086184
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
      value: 28.93630367824217
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
      value: 29.08234393834005
    - type: mrr
      value: 29.740466971605432
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
      value: 6.2059999999999995
    - type: map_at_10
      value: 14.442
    - type: map_at_100
      value: 18.005
    - type: map_at_1000
      value: 19.488
    - type: map_at_3
      value: 10.666
    - type: map_at_5
      value: 12.45
    - type: mrr_at_1
      value: 47.678
    - type: mrr_at_10
      value: 57.519
    - type: mrr_at_100
      value: 58.13700000000001
    - type: mrr_at_1000
      value: 58.167
    - type: mrr_at_3
      value: 55.779
    - type: mrr_at_5
      value: 56.940000000000005
    - type: ndcg_at_1
      value: 45.82
    - type: ndcg_at_10
      value: 37.651
    - type: ndcg_at_100
      value: 34.001999999999995
    - type: ndcg_at_1000
      value: 42.626
    - type: ndcg_at_3
      value: 43.961
    - type: ndcg_at_5
      value: 41.461
    - type: precision_at_1
      value: 47.678
    - type: precision_at_10
      value: 27.584999999999997
    - type: precision_at_100
      value: 8.455
    - type: precision_at_1000
      value: 2.118
    - type: precision_at_3
      value: 41.692
    - type: precision_at_5
      value: 36.161
    - type: recall_at_1
      value: 6.2059999999999995
    - type: recall_at_10
      value: 18.599
    - type: recall_at_100
      value: 33.608
    - type: recall_at_1000
      value: 65.429
    - type: recall_at_3
      value: 12.126000000000001
    - type: recall_at_5
      value: 14.902000000000001
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
      value: 39.117000000000004
    - type: map_at_10
      value: 55.535000000000004
    - type: map_at_100
      value: 56.32899999999999
    - type: map_at_1000
      value: 56.34400000000001
    - type: map_at_3
      value: 51.439
    - type: map_at_5
      value: 53.89699999999999
    - type: mrr_at_1
      value: 43.714
    - type: mrr_at_10
      value: 58.05200000000001
    - type: mrr_at_100
      value: 58.582
    - type: mrr_at_1000
      value: 58.592
    - type: mrr_at_3
      value: 54.896
    - type: mrr_at_5
      value: 56.874
    - type: ndcg_at_1
      value: 43.685
    - type: ndcg_at_10
      value: 63.108
    - type: ndcg_at_100
      value: 66.231
    - type: ndcg_at_1000
      value: 66.583
    - type: ndcg_at_3
      value: 55.659000000000006
    - type: ndcg_at_5
      value: 59.681
    - type: precision_at_1
      value: 43.685
    - type: precision_at_10
      value: 9.962
    - type: precision_at_100
      value: 1.174
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 24.961
    - type: precision_at_5
      value: 17.352
    - type: recall_at_1
      value: 39.117000000000004
    - type: recall_at_10
      value: 83.408
    - type: recall_at_100
      value: 96.553
    - type: recall_at_1000
      value: 99.136
    - type: recall_at_3
      value: 64.364
    - type: recall_at_5
      value: 73.573
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
      value: 78.87763157894737
    - type: f1
      value: 78.69611753876177
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
      value: 62
    - type: cos_sim_ap
      value: 62.26837791655737
    - type: cos_sim_f1
      value: 62.607449856733524
    - type: cos_sim_precision
      value: 46.36604774535809
    - type: cos_sim_recall
      value: 96.36163175303197
    - type: dot_accuracy
      value: 62
    - type: dot_ap
      value: 62.26736459439965
    - type: dot_f1
      value: 62.607449856733524
    - type: dot_precision
      value: 46.36604774535809
    - type: dot_recall
      value: 96.36163175303197
    - type: euclidean_accuracy
      value: 62
    - type: euclidean_ap
      value: 62.26826112548132
    - type: euclidean_f1
      value: 62.607449856733524
    - type: euclidean_precision
      value: 46.36604774535809
    - type: euclidean_recall
      value: 96.36163175303197
    - type: manhattan_accuracy
      value: 62
    - type: manhattan_ap
      value: 62.26223761507973
    - type: manhattan_f1
      value: 62.585034013605444
    - type: manhattan_precision
      value: 46.34146341463415
    - type: manhattan_recall
      value: 96.36163175303197
    - type: max_accuracy
      value: 62
    - type: max_ap
      value: 62.26837791655737
    - type: max_f1
      value: 62.607449856733524
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
      value: 69.90899999999999
    - type: map_at_10
      value: 83.56700000000001
    - type: map_at_100
      value: 84.19200000000001
    - type: map_at_1000
      value: 84.212
    - type: map_at_3
      value: 80.658
    - type: map_at_5
      value: 82.473
    - type: mrr_at_1
      value: 80.4
    - type: mrr_at_10
      value: 86.699
    - type: mrr_at_100
      value: 86.798
    - type: mrr_at_1000
      value: 86.80099999999999
    - type: mrr_at_3
      value: 85.677
    - type: mrr_at_5
      value: 86.354
    - type: ndcg_at_1
      value: 80.43
    - type: ndcg_at_10
      value: 87.41
    - type: ndcg_at_100
      value: 88.653
    - type: ndcg_at_1000
      value: 88.81599999999999
    - type: ndcg_at_3
      value: 84.516
    - type: ndcg_at_5
      value: 86.068
    - type: precision_at_1
      value: 80.43
    - type: precision_at_10
      value: 13.234000000000002
    - type: precision_at_100
      value: 1.513
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 36.93
    - type: precision_at_5
      value: 24.26
    - type: recall_at_1
      value: 69.90899999999999
    - type: recall_at_10
      value: 94.687
    - type: recall_at_100
      value: 98.96000000000001
    - type: recall_at_1000
      value: 99.79599999999999
    - type: recall_at_3
      value: 86.25699999999999
    - type: recall_at_5
      value: 90.70700000000001
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
      value: 46.02256865360266
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
      value: 62.43157528757563
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
      value: 12.982
    - type: map_at_100
      value: 15.031
    - type: map_at_1000
      value: 15.334
    - type: map_at_3
      value: 9.339
    - type: map_at_5
      value: 11.183
    - type: mrr_at_1
      value: 25.1
    - type: mrr_at_10
      value: 36.257
    - type: mrr_at_100
      value: 37.351
    - type: mrr_at_1000
      value: 37.409
    - type: mrr_at_3
      value: 33.050000000000004
    - type: mrr_at_5
      value: 35.205
    - type: ndcg_at_1
      value: 25.1
    - type: ndcg_at_10
      value: 21.361
    - type: ndcg_at_100
      value: 29.396
    - type: ndcg_at_1000
      value: 34.849999999999994
    - type: ndcg_at_3
      value: 20.704
    - type: ndcg_at_5
      value: 18.086
    - type: precision_at_1
      value: 25.1
    - type: precision_at_10
      value: 10.94
    - type: precision_at_100
      value: 2.257
    - type: precision_at_1000
      value: 0.358
    - type: precision_at_3
      value: 19.467000000000002
    - type: precision_at_5
      value: 15.98
    - type: recall_at_1
      value: 5.093
    - type: recall_at_10
      value: 22.177
    - type: recall_at_100
      value: 45.842
    - type: recall_at_1000
      value: 72.598
    - type: recall_at_3
      value: 11.833
    - type: recall_at_5
      value: 16.173000000000002
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
      value: 73.56535226754596
    - type: cos_sim_spearman
      value: 69.32425977603488
    - type: euclidean_pearson
      value: 71.32425703470898
    - type: euclidean_spearman
      value: 69.32425217267013
    - type: manhattan_pearson
      value: 71.25897281394246
    - type: manhattan_spearman
      value: 69.27132577049578
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
      value: 69.66387868726018
    - type: cos_sim_spearman
      value: 67.85470749045027
    - type: euclidean_pearson
      value: 66.62075098063795
    - type: euclidean_spearman
      value: 67.85470749045027
    - type: manhattan_pearson
      value: 66.61455061901262
    - type: manhattan_spearman
      value: 67.87229618498695
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
      value: 75.65731331392575
    - type: cos_sim_spearman
      value: 77.48991626780108
    - type: euclidean_pearson
      value: 77.19884738623692
    - type: euclidean_spearman
      value: 77.48985836619045
    - type: manhattan_pearson
      value: 77.0656684243772
    - type: manhattan_spearman
      value: 77.30289226582691
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
      value: 69.37003253666457
    - type: cos_sim_spearman
      value: 69.77157648098141
    - type: euclidean_pearson
      value: 69.39543876030432
    - type: euclidean_spearman
      value: 69.77157648098141
    - type: manhattan_pearson
      value: 69.29901600459745
    - type: manhattan_spearman
      value: 69.65074167527128
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
      value: 78.56777256540136
    - type: cos_sim_spearman
      value: 80.16458787843023
    - type: euclidean_pearson
      value: 80.16475730686916
    - type: euclidean_spearman
      value: 80.16458787843023
    - type: manhattan_pearson
      value: 80.12814463670401
    - type: manhattan_spearman
      value: 80.1357907984809
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
      value: 76.09572350919031
    - type: cos_sim_spearman
      value: 77.94490233429326
    - type: euclidean_pearson
      value: 78.36595251203524
    - type: euclidean_spearman
      value: 77.94490233429326
    - type: manhattan_pearson
      value: 78.41538768125166
    - type: manhattan_spearman
      value: 78.01244379569542
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
      value: 80.7843552187951
    - type: cos_sim_spearman
      value: 82.28085055047386
    - type: euclidean_pearson
      value: 82.37373672515267
    - type: euclidean_spearman
      value: 82.28085055047386
    - type: manhattan_pearson
      value: 82.39387241346917
    - type: manhattan_spearman
      value: 82.36503339515906
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
      value: 68.29963929962095
    - type: cos_sim_spearman
      value: 67.96868942546051
    - type: euclidean_pearson
      value: 68.93524903869285
    - type: euclidean_spearman
      value: 67.96868942546051
    - type: manhattan_pearson
      value: 68.79144468444811
    - type: manhattan_spearman
      value: 67.69311483884324
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
      value: 72.84789696700685
    - type: cos_sim_spearman
      value: 75.67875747588545
    - type: euclidean_pearson
      value: 75.07752300463038
    - type: euclidean_spearman
      value: 75.67875747588545
    - type: manhattan_pearson
      value: 74.97934248140928
    - type: manhattan_spearman
      value: 75.62525644178724
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
      value: 72.84789702519309
    - type: cos_sim_spearman
      value: 75.67875747588545
    - type: euclidean_pearson
      value: 75.07752310061133
    - type: euclidean_spearman
      value: 75.67875747588545
    - type: manhattan_pearson
      value: 74.97934257159595
    - type: manhattan_spearman
      value: 75.62525644178724
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
      value: 81.55557720431086
    - type: mrr
      value: 94.91178665198272
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
      value: 59.260999999999996
    - type: map_at_10
      value: 69.36099999999999
    - type: map_at_100
      value: 69.868
    - type: map_at_1000
      value: 69.877
    - type: map_at_3
      value: 66.617
    - type: map_at_5
      value: 68.061
    - type: mrr_at_1
      value: 62.333000000000006
    - type: mrr_at_10
      value: 70.533
    - type: mrr_at_100
      value: 70.966
    - type: mrr_at_1000
      value: 70.975
    - type: mrr_at_3
      value: 68.667
    - type: mrr_at_5
      value: 69.717
    - type: ndcg_at_1
      value: 62.333000000000006
    - type: ndcg_at_10
      value: 73.82300000000001
    - type: ndcg_at_100
      value: 76.122
    - type: ndcg_at_1000
      value: 76.374
    - type: ndcg_at_3
      value: 69.27499999999999
    - type: ndcg_at_5
      value: 71.33
    - type: precision_at_1
      value: 62.333000000000006
    - type: precision_at_10
      value: 9.8
    - type: precision_at_100
      value: 1.097
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 26.889000000000003
    - type: precision_at_5
      value: 17.599999999999998
    - type: recall_at_1
      value: 59.260999999999996
    - type: recall_at_10
      value: 86.2
    - type: recall_at_100
      value: 96.667
    - type: recall_at_1000
      value: 98.667
    - type: recall_at_3
      value: 74.006
    - type: recall_at_5
      value: 79.167
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
      value: 95.20169041096409
    - type: cos_sim_f1
      value: 90.76224129227664
    - type: cos_sim_precision
      value: 91.64118246687055
    - type: cos_sim_recall
      value: 89.9
    - type: dot_accuracy
      value: 99.81881188118813
    - type: dot_ap
      value: 95.20169041096409
    - type: dot_f1
      value: 90.76224129227664
    - type: dot_precision
      value: 91.64118246687055
    - type: dot_recall
      value: 89.9
    - type: euclidean_accuracy
      value: 99.81881188118813
    - type: euclidean_ap
      value: 95.2016904109641
    - type: euclidean_f1
      value: 90.76224129227664
    - type: euclidean_precision
      value: 91.64118246687055
    - type: euclidean_recall
      value: 89.9
    - type: manhattan_accuracy
      value: 99.81881188118813
    - type: manhattan_ap
      value: 95.22680188132777
    - type: manhattan_f1
      value: 90.79013588324108
    - type: manhattan_precision
      value: 91.38804457953394
    - type: manhattan_recall
      value: 90.2
    - type: max_accuracy
      value: 99.81881188118813
    - type: max_ap
      value: 95.22680188132777
    - type: max_f1
      value: 90.79013588324108
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
      value: 57.8638628701308
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
      value: 37.82028248106046
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
      value: 50.870860210170946
    - type: mrr
      value: 51.608084521687466
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
      value: 31.60384207444685
    - type: cos_sim_spearman
      value: 30.84047452209471
    - type: dot_pearson
      value: 31.60384104417333
    - type: dot_spearman
      value: 30.84047452209471
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
      value: 0.246
    - type: map_at_10
      value: 2.051
    - type: map_at_100
      value: 13.129
    - type: map_at_1000
      value: 31.56
    - type: map_at_3
      value: 0.681
    - type: map_at_5
      value: 1.105
    - type: mrr_at_1
      value: 94
    - type: mrr_at_10
      value: 97
    - type: mrr_at_100
      value: 97
    - type: mrr_at_1000
      value: 97
    - type: mrr_at_3
      value: 97
    - type: mrr_at_5
      value: 97
    - type: ndcg_at_1
      value: 87
    - type: ndcg_at_10
      value: 80.716
    - type: ndcg_at_100
      value: 63.83
    - type: ndcg_at_1000
      value: 56.215
    - type: ndcg_at_3
      value: 84.531
    - type: ndcg_at_5
      value: 84.777
    - type: precision_at_1
      value: 94
    - type: precision_at_10
      value: 84.6
    - type: precision_at_100
      value: 66.03999999999999
    - type: precision_at_1000
      value: 24.878
    - type: precision_at_3
      value: 88.667
    - type: precision_at_5
      value: 89.60000000000001
    - type: recall_at_1
      value: 0.246
    - type: recall_at_10
      value: 2.2079999999999997
    - type: recall_at_100
      value: 15.895999999999999
    - type: recall_at_1000
      value: 52.683
    - type: recall_at_3
      value: 0.7040000000000001
    - type: recall_at_5
      value: 1.163
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
      value: 3.852
    - type: map_at_10
      value: 14.316
    - type: map_at_100
      value: 20.982
    - type: map_at_1000
      value: 22.58
    - type: map_at_3
      value: 7.767
    - type: map_at_5
      value: 10.321
    - type: mrr_at_1
      value: 51.019999999999996
    - type: mrr_at_10
      value: 66.365
    - type: mrr_at_100
      value: 66.522
    - type: mrr_at_1000
      value: 66.522
    - type: mrr_at_3
      value: 62.925
    - type: mrr_at_5
      value: 64.762
    - type: ndcg_at_1
      value: 46.939
    - type: ndcg_at_10
      value: 34.516999999999996
    - type: ndcg_at_100
      value: 44.25
    - type: ndcg_at_1000
      value: 54.899
    - type: ndcg_at_3
      value: 40.203
    - type: ndcg_at_5
      value: 37.004
    - type: precision_at_1
      value: 51.019999999999996
    - type: precision_at_10
      value: 29.796
    - type: precision_at_100
      value: 8.633000000000001
    - type: precision_at_1000
      value: 1.584
    - type: precision_at_3
      value: 40.816
    - type: precision_at_5
      value: 35.918
    - type: recall_at_1
      value: 3.852
    - type: recall_at_10
      value: 20.891000000000002
    - type: recall_at_100
      value: 52.428
    - type: recall_at_1000
      value: 84.34899999999999
    - type: recall_at_3
      value: 8.834
    - type: recall_at_5
      value: 12.909
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
      value: 64.7092
    - type: ap
      value: 11.972915012305819
    - type: f1
      value: 49.91050149892115
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
      value: 56.737408036219584
    - type: f1
      value: 57.07235266246011
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
      value: 35.9147539025798
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
      value: 82.52369315133814
    - type: cos_sim_ap
      value: 62.34858091376534
    - type: cos_sim_f1
      value: 58.18225190839694
    - type: cos_sim_precision
      value: 53.09098824553766
    - type: cos_sim_recall
      value: 64.35356200527704
    - type: dot_accuracy
      value: 82.52369315133814
    - type: dot_ap
      value: 62.34857753814992
    - type: dot_f1
      value: 58.18225190839694
    - type: dot_precision
      value: 53.09098824553766
    - type: dot_recall
      value: 64.35356200527704
    - type: euclidean_accuracy
      value: 82.52369315133814
    - type: euclidean_ap
      value: 62.34857756663386
    - type: euclidean_f1
      value: 58.18225190839694
    - type: euclidean_precision
      value: 53.09098824553766
    - type: euclidean_recall
      value: 64.35356200527704
    - type: manhattan_accuracy
      value: 82.49389044525243
    - type: manhattan_ap
      value: 62.32245347238179
    - type: manhattan_f1
      value: 58.206309819213054
    - type: manhattan_precision
      value: 52.70704044511021
    - type: manhattan_recall
      value: 64.9868073878628
    - type: max_accuracy
      value: 82.52369315133814
    - type: max_ap
      value: 62.34858091376534
    - type: max_f1
      value: 58.206309819213054
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
      value: 88.34555827220863
    - type: cos_sim_ap
      value: 84.84152481680071
    - type: cos_sim_f1
      value: 76.860456739428
    - type: cos_sim_precision
      value: 72.21470150263978
    - type: cos_sim_recall
      value: 82.14505697566985
    - type: dot_accuracy
      value: 88.34555827220863
    - type: dot_ap
      value: 84.84152743322608
    - type: dot_f1
      value: 76.860456739428
    - type: dot_precision
      value: 72.21470150263978
    - type: dot_recall
      value: 82.14505697566985
    - type: euclidean_accuracy
      value: 88.34555827220863
    - type: euclidean_ap
      value: 84.84152589453169
    - type: euclidean_f1
      value: 76.860456739428
    - type: euclidean_precision
      value: 72.21470150263978
    - type: euclidean_recall
      value: 82.14505697566985
    - type: manhattan_accuracy
      value: 88.38242713548337
    - type: manhattan_ap
      value: 84.8112124970968
    - type: manhattan_f1
      value: 76.83599206057487
    - type: manhattan_precision
      value: 73.51244900829934
    - type: manhattan_recall
      value: 80.47428395441946
    - type: max_accuracy
      value: 88.38242713548337
    - type: max_ap
      value: 84.84152743322608
    - type: max_f1
      value: 76.860456739428
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
      value: 85.5314389263015
---
<h1 align="center">Snowflake's Arctic-embed-l</h1>
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

model = SentenceTransformer("Snowflake/snowflake-arctic-embed-l")

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
0.28976774 The Data Cloud!
0.19071159 Mexico City of Course!
Query: Where can I get the best tacos?
0.38650584 Mexico City of Course!
0.25145516 The Data Cloud!
```


### Using Huggingface transformers


You can use the transformers package to use an snowflake-arctic-embed model, as shown below. For optimal retrieval quality, use the CLS token to embed each text portion and use the query prefix below (just on the query).



```python
import torch
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Snowflake/snowflake-arctic-embed-l')
model = AutoModel.from_pretrained('Snowflake/snowflake-arctic-embed-l', add_pooling_layer=False)
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
const extractor = await pipeline('feature-extraction', 'Snowflake/snowflake-arctic-embed-l', {
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
console.log(similarities); // [0.25145517380846977, 0.3865060421197194]
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