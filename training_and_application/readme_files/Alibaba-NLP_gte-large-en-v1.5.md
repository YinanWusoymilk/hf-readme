---
datasets:
- allenai/c4
library_name: transformers
tags:
- sentence-transformers
- gte
- mteb
- transformers.js
- sentence-similarity
license: apache-2.0
language:
- en
model-index:
- name: gte-large-en-v1.5
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
      value: 73.01492537313432
    - type: ap
      value: 35.05341696659522
    - type: f1
      value: 66.71270310883853
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
      value: 93.97189999999999
    - type: ap
      value: 90.5952493948908
    - type: f1
      value: 93.95848137716877
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
      value: 54.196
    - type: f1
      value: 53.80122334012787
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
      value: 47.297
    - type: map_at_10
      value: 64.303
    - type: map_at_100
      value: 64.541
    - type: map_at_1000
      value: 64.541
    - type: map_at_3
      value: 60.728
    - type: map_at_5
      value: 63.114000000000004
    - type: mrr_at_1
      value: 48.435
    - type: mrr_at_10
      value: 64.657
    - type: mrr_at_100
      value: 64.901
    - type: mrr_at_1000
      value: 64.901
    - type: mrr_at_3
      value: 61.06
    - type: mrr_at_5
      value: 63.514
    - type: ndcg_at_1
      value: 47.297
    - type: ndcg_at_10
      value: 72.107
    - type: ndcg_at_100
      value: 72.963
    - type: ndcg_at_1000
      value: 72.963
    - type: ndcg_at_3
      value: 65.063
    - type: ndcg_at_5
      value: 69.352
    - type: precision_at_1
      value: 47.297
    - type: precision_at_10
      value: 9.623
    - type: precision_at_100
      value: 0.996
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 25.865
    - type: precision_at_5
      value: 17.596
    - type: recall_at_1
      value: 47.297
    - type: recall_at_10
      value: 96.23
    - type: recall_at_100
      value: 99.644
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 77.596
    - type: recall_at_5
      value: 87.98
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
      value: 48.467787861077475
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
      value: 43.39198391914257
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
      value: 63.12794820591384
    - type: mrr
      value: 75.9331442641692
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
      value: 87.85062993863319
    - type: cos_sim_spearman
      value: 85.39049989733459
    - type: euclidean_pearson
      value: 86.00222680278333
    - type: euclidean_spearman
      value: 85.45556162077396
    - type: manhattan_pearson
      value: 85.88769871785621
    - type: manhattan_spearman
      value: 85.11760211290839
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
      value: 87.32792207792208
    - type: f1
      value: 87.29132945999555
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
      value: 40.5779328301945
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
      value: 37.94425623865118
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
      value: 32.978
    - type: map_at_10
      value: 44.45
    - type: map_at_100
      value: 46.19
    - type: map_at_1000
      value: 46.303
    - type: map_at_3
      value: 40.849000000000004
    - type: map_at_5
      value: 42.55
    - type: mrr_at_1
      value: 40.629
    - type: mrr_at_10
      value: 50.848000000000006
    - type: mrr_at_100
      value: 51.669
    - type: mrr_at_1000
      value: 51.705
    - type: mrr_at_3
      value: 47.997
    - type: mrr_at_5
      value: 49.506
    - type: ndcg_at_1
      value: 40.629
    - type: ndcg_at_10
      value: 51.102000000000004
    - type: ndcg_at_100
      value: 57.159000000000006
    - type: ndcg_at_1000
      value: 58.669000000000004
    - type: ndcg_at_3
      value: 45.738
    - type: ndcg_at_5
      value: 47.632999999999996
    - type: precision_at_1
      value: 40.629
    - type: precision_at_10
      value: 9.700000000000001
    - type: precision_at_100
      value: 1.5970000000000002
    - type: precision_at_1000
      value: 0.202
    - type: precision_at_3
      value: 21.698
    - type: precision_at_5
      value: 15.393
    - type: recall_at_1
      value: 32.978
    - type: recall_at_10
      value: 63.711
    - type: recall_at_100
      value: 88.39399999999999
    - type: recall_at_1000
      value: 97.513
    - type: recall_at_3
      value: 48.025
    - type: recall_at_5
      value: 53.52
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
      value: 30.767
    - type: map_at_10
      value: 42.195
    - type: map_at_100
      value: 43.541999999999994
    - type: map_at_1000
      value: 43.673
    - type: map_at_3
      value: 38.561
    - type: map_at_5
      value: 40.532000000000004
    - type: mrr_at_1
      value: 38.79
    - type: mrr_at_10
      value: 48.021
    - type: mrr_at_100
      value: 48.735
    - type: mrr_at_1000
      value: 48.776
    - type: mrr_at_3
      value: 45.594
    - type: mrr_at_5
      value: 46.986
    - type: ndcg_at_1
      value: 38.79
    - type: ndcg_at_10
      value: 48.468
    - type: ndcg_at_100
      value: 53.037
    - type: ndcg_at_1000
      value: 55.001999999999995
    - type: ndcg_at_3
      value: 43.409
    - type: ndcg_at_5
      value: 45.654
    - type: precision_at_1
      value: 38.79
    - type: precision_at_10
      value: 9.452
    - type: precision_at_100
      value: 1.518
    - type: precision_at_1000
      value: 0.201
    - type: precision_at_3
      value: 21.21
    - type: precision_at_5
      value: 15.171999999999999
    - type: recall_at_1
      value: 30.767
    - type: recall_at_10
      value: 60.118
    - type: recall_at_100
      value: 79.271
    - type: recall_at_1000
      value: 91.43299999999999
    - type: recall_at_3
      value: 45.36
    - type: recall_at_5
      value: 51.705
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
      value: 40.007
    - type: map_at_10
      value: 53.529
    - type: map_at_100
      value: 54.602
    - type: map_at_1000
      value: 54.647
    - type: map_at_3
      value: 49.951
    - type: map_at_5
      value: 52.066
    - type: mrr_at_1
      value: 45.705
    - type: mrr_at_10
      value: 56.745000000000005
    - type: mrr_at_100
      value: 57.43899999999999
    - type: mrr_at_1000
      value: 57.462999999999994
    - type: mrr_at_3
      value: 54.25299999999999
    - type: mrr_at_5
      value: 55.842000000000006
    - type: ndcg_at_1
      value: 45.705
    - type: ndcg_at_10
      value: 59.809
    - type: ndcg_at_100
      value: 63.837999999999994
    - type: ndcg_at_1000
      value: 64.729
    - type: ndcg_at_3
      value: 53.994
    - type: ndcg_at_5
      value: 57.028
    - type: precision_at_1
      value: 45.705
    - type: precision_at_10
      value: 9.762
    - type: precision_at_100
      value: 1.275
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: precision_at_3
      value: 24.368000000000002
    - type: precision_at_5
      value: 16.84
    - type: recall_at_1
      value: 40.007
    - type: recall_at_10
      value: 75.017
    - type: recall_at_100
      value: 91.99000000000001
    - type: recall_at_1000
      value: 98.265
    - type: recall_at_3
      value: 59.704
    - type: recall_at_5
      value: 67.109
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
      value: 26.639000000000003
    - type: map_at_10
      value: 35.926
    - type: map_at_100
      value: 37.126999999999995
    - type: map_at_1000
      value: 37.202
    - type: map_at_3
      value: 32.989000000000004
    - type: map_at_5
      value: 34.465
    - type: mrr_at_1
      value: 28.475
    - type: mrr_at_10
      value: 37.7
    - type: mrr_at_100
      value: 38.753
    - type: mrr_at_1000
      value: 38.807
    - type: mrr_at_3
      value: 35.066
    - type: mrr_at_5
      value: 36.512
    - type: ndcg_at_1
      value: 28.475
    - type: ndcg_at_10
      value: 41.245
    - type: ndcg_at_100
      value: 46.814
    - type: ndcg_at_1000
      value: 48.571
    - type: ndcg_at_3
      value: 35.528999999999996
    - type: ndcg_at_5
      value: 38.066
    - type: precision_at_1
      value: 28.475
    - type: precision_at_10
      value: 6.497
    - type: precision_at_100
      value: 0.9650000000000001
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 15.065999999999999
    - type: precision_at_5
      value: 10.599
    - type: recall_at_1
      value: 26.639000000000003
    - type: recall_at_10
      value: 55.759
    - type: recall_at_100
      value: 80.913
    - type: recall_at_1000
      value: 93.929
    - type: recall_at_3
      value: 40.454
    - type: recall_at_5
      value: 46.439
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
      value: 15.767999999999999
    - type: map_at_10
      value: 24.811
    - type: map_at_100
      value: 26.064999999999998
    - type: map_at_1000
      value: 26.186999999999998
    - type: map_at_3
      value: 21.736
    - type: map_at_5
      value: 23.283
    - type: mrr_at_1
      value: 19.527
    - type: mrr_at_10
      value: 29.179
    - type: mrr_at_100
      value: 30.153999999999996
    - type: mrr_at_1000
      value: 30.215999999999998
    - type: mrr_at_3
      value: 26.223000000000003
    - type: mrr_at_5
      value: 27.733999999999998
    - type: ndcg_at_1
      value: 19.527
    - type: ndcg_at_10
      value: 30.786
    - type: ndcg_at_100
      value: 36.644
    - type: ndcg_at_1000
      value: 39.440999999999995
    - type: ndcg_at_3
      value: 24.958
    - type: ndcg_at_5
      value: 27.392
    - type: precision_at_1
      value: 19.527
    - type: precision_at_10
      value: 5.995
    - type: precision_at_100
      value: 1.03
    - type: precision_at_1000
      value: 0.14100000000000001
    - type: precision_at_3
      value: 12.520999999999999
    - type: precision_at_5
      value: 9.129
    - type: recall_at_1
      value: 15.767999999999999
    - type: recall_at_10
      value: 44.824000000000005
    - type: recall_at_100
      value: 70.186
    - type: recall_at_1000
      value: 89.934
    - type: recall_at_3
      value: 28.607
    - type: recall_at_5
      value: 34.836
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
      value: 31.952
    - type: map_at_10
      value: 44.438
    - type: map_at_100
      value: 45.778
    - type: map_at_1000
      value: 45.883
    - type: map_at_3
      value: 41.044000000000004
    - type: map_at_5
      value: 42.986000000000004
    - type: mrr_at_1
      value: 39.172000000000004
    - type: mrr_at_10
      value: 49.76
    - type: mrr_at_100
      value: 50.583999999999996
    - type: mrr_at_1000
      value: 50.621
    - type: mrr_at_3
      value: 47.353
    - type: mrr_at_5
      value: 48.739
    - type: ndcg_at_1
      value: 39.172000000000004
    - type: ndcg_at_10
      value: 50.760000000000005
    - type: ndcg_at_100
      value: 56.084
    - type: ndcg_at_1000
      value: 57.865
    - type: ndcg_at_3
      value: 45.663
    - type: ndcg_at_5
      value: 48.178
    - type: precision_at_1
      value: 39.172000000000004
    - type: precision_at_10
      value: 9.22
    - type: precision_at_100
      value: 1.387
    - type: precision_at_1000
      value: 0.17099999999999999
    - type: precision_at_3
      value: 21.976000000000003
    - type: precision_at_5
      value: 15.457
    - type: recall_at_1
      value: 31.952
    - type: recall_at_10
      value: 63.900999999999996
    - type: recall_at_100
      value: 85.676
    - type: recall_at_1000
      value: 97.03699999999999
    - type: recall_at_3
      value: 49.781
    - type: recall_at_5
      value: 56.330000000000005
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
      value: 25.332
    - type: map_at_10
      value: 36.874
    - type: map_at_100
      value: 38.340999999999994
    - type: map_at_1000
      value: 38.452
    - type: map_at_3
      value: 33.068
    - type: map_at_5
      value: 35.324
    - type: mrr_at_1
      value: 30.822
    - type: mrr_at_10
      value: 41.641
    - type: mrr_at_100
      value: 42.519
    - type: mrr_at_1000
      value: 42.573
    - type: mrr_at_3
      value: 38.413000000000004
    - type: mrr_at_5
      value: 40.542
    - type: ndcg_at_1
      value: 30.822
    - type: ndcg_at_10
      value: 43.414
    - type: ndcg_at_100
      value: 49.196
    - type: ndcg_at_1000
      value: 51.237
    - type: ndcg_at_3
      value: 37.230000000000004
    - type: ndcg_at_5
      value: 40.405
    - type: precision_at_1
      value: 30.822
    - type: precision_at_10
      value: 8.379
    - type: precision_at_100
      value: 1.315
    - type: precision_at_1000
      value: 0.168
    - type: precision_at_3
      value: 18.417
    - type: precision_at_5
      value: 13.744
    - type: recall_at_1
      value: 25.332
    - type: recall_at_10
      value: 57.774
    - type: recall_at_100
      value: 82.071
    - type: recall_at_1000
      value: 95.60600000000001
    - type: recall_at_3
      value: 40.722
    - type: recall_at_5
      value: 48.754999999999995
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
      value: 25.91033333333334
    - type: map_at_10
      value: 36.23225000000001
    - type: map_at_100
      value: 37.55766666666667
    - type: map_at_1000
      value: 37.672583333333336
    - type: map_at_3
      value: 32.95666666666667
    - type: map_at_5
      value: 34.73375
    - type: mrr_at_1
      value: 30.634
    - type: mrr_at_10
      value: 40.19449999999999
    - type: mrr_at_100
      value: 41.099250000000005
    - type: mrr_at_1000
      value: 41.15091666666667
    - type: mrr_at_3
      value: 37.4615
    - type: mrr_at_5
      value: 39.00216666666667
    - type: ndcg_at_1
      value: 30.634
    - type: ndcg_at_10
      value: 42.162166666666664
    - type: ndcg_at_100
      value: 47.60708333333333
    - type: ndcg_at_1000
      value: 49.68616666666666
    - type: ndcg_at_3
      value: 36.60316666666666
    - type: ndcg_at_5
      value: 39.15616666666668
    - type: precision_at_1
      value: 30.634
    - type: precision_at_10
      value: 7.6193333333333335
    - type: precision_at_100
      value: 1.2198333333333333
    - type: precision_at_1000
      value: 0.15975000000000003
    - type: precision_at_3
      value: 17.087
    - type: precision_at_5
      value: 12.298333333333334
    - type: recall_at_1
      value: 25.91033333333334
    - type: recall_at_10
      value: 55.67300000000001
    - type: recall_at_100
      value: 79.20608333333334
    - type: recall_at_1000
      value: 93.34866666666667
    - type: recall_at_3
      value: 40.34858333333333
    - type: recall_at_5
      value: 46.834083333333325
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
      value: 25.006
    - type: map_at_10
      value: 32.177
    - type: map_at_100
      value: 33.324999999999996
    - type: map_at_1000
      value: 33.419
    - type: map_at_3
      value: 29.952
    - type: map_at_5
      value: 31.095
    - type: mrr_at_1
      value: 28.066999999999997
    - type: mrr_at_10
      value: 34.995
    - type: mrr_at_100
      value: 35.978
    - type: mrr_at_1000
      value: 36.042
    - type: mrr_at_3
      value: 33.103
    - type: mrr_at_5
      value: 34.001
    - type: ndcg_at_1
      value: 28.066999999999997
    - type: ndcg_at_10
      value: 36.481
    - type: ndcg_at_100
      value: 42.022999999999996
    - type: ndcg_at_1000
      value: 44.377
    - type: ndcg_at_3
      value: 32.394
    - type: ndcg_at_5
      value: 34.108
    - type: precision_at_1
      value: 28.066999999999997
    - type: precision_at_10
      value: 5.736
    - type: precision_at_100
      value: 0.9259999999999999
    - type: precision_at_1000
      value: 0.12
    - type: precision_at_3
      value: 13.804
    - type: precision_at_5
      value: 9.508999999999999
    - type: recall_at_1
      value: 25.006
    - type: recall_at_10
      value: 46.972
    - type: recall_at_100
      value: 72.138
    - type: recall_at_1000
      value: 89.479
    - type: recall_at_3
      value: 35.793
    - type: recall_at_5
      value: 39.947
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
      value: 16.07
    - type: map_at_10
      value: 24.447
    - type: map_at_100
      value: 25.685999999999996
    - type: map_at_1000
      value: 25.813999999999997
    - type: map_at_3
      value: 21.634
    - type: map_at_5
      value: 23.133
    - type: mrr_at_1
      value: 19.580000000000002
    - type: mrr_at_10
      value: 28.127999999999997
    - type: mrr_at_100
      value: 29.119
    - type: mrr_at_1000
      value: 29.192
    - type: mrr_at_3
      value: 25.509999999999998
    - type: mrr_at_5
      value: 26.878
    - type: ndcg_at_1
      value: 19.580000000000002
    - type: ndcg_at_10
      value: 29.804000000000002
    - type: ndcg_at_100
      value: 35.555
    - type: ndcg_at_1000
      value: 38.421
    - type: ndcg_at_3
      value: 24.654999999999998
    - type: ndcg_at_5
      value: 26.881
    - type: precision_at_1
      value: 19.580000000000002
    - type: precision_at_10
      value: 5.736
    - type: precision_at_100
      value: 1.005
    - type: precision_at_1000
      value: 0.145
    - type: precision_at_3
      value: 12.033000000000001
    - type: precision_at_5
      value: 8.871
    - type: recall_at_1
      value: 16.07
    - type: recall_at_10
      value: 42.364000000000004
    - type: recall_at_100
      value: 68.01899999999999
    - type: recall_at_1000
      value: 88.122
    - type: recall_at_3
      value: 27.846
    - type: recall_at_5
      value: 33.638
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
      value: 26.365
    - type: map_at_10
      value: 36.591
    - type: map_at_100
      value: 37.730000000000004
    - type: map_at_1000
      value: 37.84
    - type: map_at_3
      value: 33.403
    - type: map_at_5
      value: 35.272999999999996
    - type: mrr_at_1
      value: 30.503999999999998
    - type: mrr_at_10
      value: 39.940999999999995
    - type: mrr_at_100
      value: 40.818
    - type: mrr_at_1000
      value: 40.876000000000005
    - type: mrr_at_3
      value: 37.065
    - type: mrr_at_5
      value: 38.814
    - type: ndcg_at_1
      value: 30.503999999999998
    - type: ndcg_at_10
      value: 42.185
    - type: ndcg_at_100
      value: 47.416000000000004
    - type: ndcg_at_1000
      value: 49.705
    - type: ndcg_at_3
      value: 36.568
    - type: ndcg_at_5
      value: 39.416000000000004
    - type: precision_at_1
      value: 30.503999999999998
    - type: precision_at_10
      value: 7.276000000000001
    - type: precision_at_100
      value: 1.118
    - type: precision_at_1000
      value: 0.14300000000000002
    - type: precision_at_3
      value: 16.729
    - type: precision_at_5
      value: 12.107999999999999
    - type: recall_at_1
      value: 26.365
    - type: recall_at_10
      value: 55.616
    - type: recall_at_100
      value: 78.129
    - type: recall_at_1000
      value: 93.95599999999999
    - type: recall_at_3
      value: 40.686
    - type: recall_at_5
      value: 47.668
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
      value: 22.750999999999998
    - type: map_at_10
      value: 33.446
    - type: map_at_100
      value: 35.235
    - type: map_at_1000
      value: 35.478
    - type: map_at_3
      value: 29.358
    - type: map_at_5
      value: 31.525
    - type: mrr_at_1
      value: 27.668
    - type: mrr_at_10
      value: 37.694
    - type: mrr_at_100
      value: 38.732
    - type: mrr_at_1000
      value: 38.779
    - type: mrr_at_3
      value: 34.223
    - type: mrr_at_5
      value: 36.08
    - type: ndcg_at_1
      value: 27.668
    - type: ndcg_at_10
      value: 40.557
    - type: ndcg_at_100
      value: 46.605999999999995
    - type: ndcg_at_1000
      value: 48.917
    - type: ndcg_at_3
      value: 33.677
    - type: ndcg_at_5
      value: 36.85
    - type: precision_at_1
      value: 27.668
    - type: precision_at_10
      value: 8.3
    - type: precision_at_100
      value: 1.6260000000000001
    - type: precision_at_1000
      value: 0.253
    - type: precision_at_3
      value: 16.008
    - type: precision_at_5
      value: 12.292
    - type: recall_at_1
      value: 22.750999999999998
    - type: recall_at_10
      value: 55.643
    - type: recall_at_100
      value: 82.151
    - type: recall_at_1000
      value: 95.963
    - type: recall_at_3
      value: 36.623
    - type: recall_at_5
      value: 44.708
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
      value: 17.288999999999998
    - type: map_at_10
      value: 25.903
    - type: map_at_100
      value: 27.071
    - type: map_at_1000
      value: 27.173000000000002
    - type: map_at_3
      value: 22.935
    - type: map_at_5
      value: 24.573
    - type: mrr_at_1
      value: 18.669
    - type: mrr_at_10
      value: 27.682000000000002
    - type: mrr_at_100
      value: 28.691
    - type: mrr_at_1000
      value: 28.761
    - type: mrr_at_3
      value: 24.738
    - type: mrr_at_5
      value: 26.392
    - type: ndcg_at_1
      value: 18.669
    - type: ndcg_at_10
      value: 31.335
    - type: ndcg_at_100
      value: 36.913000000000004
    - type: ndcg_at_1000
      value: 39.300000000000004
    - type: ndcg_at_3
      value: 25.423000000000002
    - type: ndcg_at_5
      value: 28.262999999999998
    - type: precision_at_1
      value: 18.669
    - type: precision_at_10
      value: 5.379
    - type: precision_at_100
      value: 0.876
    - type: precision_at_1000
      value: 0.11900000000000001
    - type: precision_at_3
      value: 11.214
    - type: precision_at_5
      value: 8.466
    - type: recall_at_1
      value: 17.288999999999998
    - type: recall_at_10
      value: 46.377
    - type: recall_at_100
      value: 71.53500000000001
    - type: recall_at_1000
      value: 88.947
    - type: recall_at_3
      value: 30.581999999999997
    - type: recall_at_5
      value: 37.354
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
      value: 21.795
    - type: map_at_10
      value: 37.614999999999995
    - type: map_at_100
      value: 40.037
    - type: map_at_1000
      value: 40.184999999999995
    - type: map_at_3
      value: 32.221
    - type: map_at_5
      value: 35.154999999999994
    - type: mrr_at_1
      value: 50.358000000000004
    - type: mrr_at_10
      value: 62.129
    - type: mrr_at_100
      value: 62.613
    - type: mrr_at_1000
      value: 62.62
    - type: mrr_at_3
      value: 59.272999999999996
    - type: mrr_at_5
      value: 61.138999999999996
    - type: ndcg_at_1
      value: 50.358000000000004
    - type: ndcg_at_10
      value: 48.362
    - type: ndcg_at_100
      value: 55.932
    - type: ndcg_at_1000
      value: 58.062999999999995
    - type: ndcg_at_3
      value: 42.111
    - type: ndcg_at_5
      value: 44.063
    - type: precision_at_1
      value: 50.358000000000004
    - type: precision_at_10
      value: 14.677999999999999
    - type: precision_at_100
      value: 2.2950000000000004
    - type: precision_at_1000
      value: 0.271
    - type: precision_at_3
      value: 31.77
    - type: precision_at_5
      value: 23.375
    - type: recall_at_1
      value: 21.795
    - type: recall_at_10
      value: 53.846000000000004
    - type: recall_at_100
      value: 78.952
    - type: recall_at_1000
      value: 90.41900000000001
    - type: recall_at_3
      value: 37.257
    - type: recall_at_5
      value: 44.661
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
      value: 9.728
    - type: map_at_10
      value: 22.691
    - type: map_at_100
      value: 31.734
    - type: map_at_1000
      value: 33.464
    - type: map_at_3
      value: 16.273
    - type: map_at_5
      value: 19.016
    - type: mrr_at_1
      value: 73.25
    - type: mrr_at_10
      value: 80.782
    - type: mrr_at_100
      value: 81.01899999999999
    - type: mrr_at_1000
      value: 81.021
    - type: mrr_at_3
      value: 79.583
    - type: mrr_at_5
      value: 80.146
    - type: ndcg_at_1
      value: 59.62499999999999
    - type: ndcg_at_10
      value: 46.304
    - type: ndcg_at_100
      value: 51.23
    - type: ndcg_at_1000
      value: 58.048
    - type: ndcg_at_3
      value: 51.541000000000004
    - type: ndcg_at_5
      value: 48.635
    - type: precision_at_1
      value: 73.25
    - type: precision_at_10
      value: 36.375
    - type: precision_at_100
      value: 11.53
    - type: precision_at_1000
      value: 2.23
    - type: precision_at_3
      value: 55.583000000000006
    - type: precision_at_5
      value: 47.15
    - type: recall_at_1
      value: 9.728
    - type: recall_at_10
      value: 28.793999999999997
    - type: recall_at_100
      value: 57.885
    - type: recall_at_1000
      value: 78.759
    - type: recall_at_3
      value: 17.79
    - type: recall_at_5
      value: 21.733
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
      value: 46.775
    - type: f1
      value: 41.89794273264891
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
      value: 85.378
    - type: map_at_10
      value: 91.51
    - type: map_at_100
      value: 91.666
    - type: map_at_1000
      value: 91.676
    - type: map_at_3
      value: 90.757
    - type: map_at_5
      value: 91.277
    - type: mrr_at_1
      value: 91.839
    - type: mrr_at_10
      value: 95.49
    - type: mrr_at_100
      value: 95.493
    - type: mrr_at_1000
      value: 95.493
    - type: mrr_at_3
      value: 95.345
    - type: mrr_at_5
      value: 95.47200000000001
    - type: ndcg_at_1
      value: 91.839
    - type: ndcg_at_10
      value: 93.806
    - type: ndcg_at_100
      value: 94.255
    - type: ndcg_at_1000
      value: 94.399
    - type: ndcg_at_3
      value: 93.027
    - type: ndcg_at_5
      value: 93.51
    - type: precision_at_1
      value: 91.839
    - type: precision_at_10
      value: 10.93
    - type: precision_at_100
      value: 1.1400000000000001
    - type: precision_at_1000
      value: 0.117
    - type: precision_at_3
      value: 34.873
    - type: precision_at_5
      value: 21.44
    - type: recall_at_1
      value: 85.378
    - type: recall_at_10
      value: 96.814
    - type: recall_at_100
      value: 98.386
    - type: recall_at_1000
      value: 99.21600000000001
    - type: recall_at_3
      value: 94.643
    - type: recall_at_5
      value: 95.976
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
      value: 32.190000000000005
    - type: map_at_10
      value: 53.605000000000004
    - type: map_at_100
      value: 55.550999999999995
    - type: map_at_1000
      value: 55.665
    - type: map_at_3
      value: 46.62
    - type: map_at_5
      value: 50.517999999999994
    - type: mrr_at_1
      value: 60.34
    - type: mrr_at_10
      value: 70.775
    - type: mrr_at_100
      value: 71.238
    - type: mrr_at_1000
      value: 71.244
    - type: mrr_at_3
      value: 68.72399999999999
    - type: mrr_at_5
      value: 69.959
    - type: ndcg_at_1
      value: 60.34
    - type: ndcg_at_10
      value: 63.226000000000006
    - type: ndcg_at_100
      value: 68.60300000000001
    - type: ndcg_at_1000
      value: 69.901
    - type: ndcg_at_3
      value: 58.048
    - type: ndcg_at_5
      value: 59.789
    - type: precision_at_1
      value: 60.34
    - type: precision_at_10
      value: 17.130000000000003
    - type: precision_at_100
      value: 2.29
    - type: precision_at_1000
      value: 0.256
    - type: precision_at_3
      value: 38.323
    - type: precision_at_5
      value: 27.87
    - type: recall_at_1
      value: 32.190000000000005
    - type: recall_at_10
      value: 73.041
    - type: recall_at_100
      value: 91.31
    - type: recall_at_1000
      value: 98.104
    - type: recall_at_3
      value: 53.70399999999999
    - type: recall_at_5
      value: 62.358999999999995
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
      value: 43.511
    - type: map_at_10
      value: 58.15
    - type: map_at_100
      value: 58.95399999999999
    - type: map_at_1000
      value: 59.018
    - type: map_at_3
      value: 55.31700000000001
    - type: map_at_5
      value: 57.04900000000001
    - type: mrr_at_1
      value: 87.022
    - type: mrr_at_10
      value: 91.32000000000001
    - type: mrr_at_100
      value: 91.401
    - type: mrr_at_1000
      value: 91.403
    - type: mrr_at_3
      value: 90.77
    - type: mrr_at_5
      value: 91.156
    - type: ndcg_at_1
      value: 87.022
    - type: ndcg_at_10
      value: 68.183
    - type: ndcg_at_100
      value: 70.781
    - type: ndcg_at_1000
      value: 72.009
    - type: ndcg_at_3
      value: 64.334
    - type: ndcg_at_5
      value: 66.449
    - type: precision_at_1
      value: 87.022
    - type: precision_at_10
      value: 13.406
    - type: precision_at_100
      value: 1.542
    - type: precision_at_1000
      value: 0.17099999999999999
    - type: precision_at_3
      value: 39.023
    - type: precision_at_5
      value: 25.080000000000002
    - type: recall_at_1
      value: 43.511
    - type: recall_at_10
      value: 67.02900000000001
    - type: recall_at_100
      value: 77.11
    - type: recall_at_1000
      value: 85.294
    - type: recall_at_3
      value: 58.535000000000004
    - type: recall_at_5
      value: 62.70099999999999
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
      value: 92.0996
    - type: ap
      value: 87.86206089096373
    - type: f1
      value: 92.07554547510763
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
      value: 23.179
    - type: map_at_10
      value: 35.86
    - type: map_at_100
      value: 37.025999999999996
    - type: map_at_1000
      value: 37.068
    - type: map_at_3
      value: 31.921
    - type: map_at_5
      value: 34.172000000000004
    - type: mrr_at_1
      value: 23.926
    - type: mrr_at_10
      value: 36.525999999999996
    - type: mrr_at_100
      value: 37.627
    - type: mrr_at_1000
      value: 37.665
    - type: mrr_at_3
      value: 32.653
    - type: mrr_at_5
      value: 34.897
    - type: ndcg_at_1
      value: 23.910999999999998
    - type: ndcg_at_10
      value: 42.927
    - type: ndcg_at_100
      value: 48.464
    - type: ndcg_at_1000
      value: 49.533
    - type: ndcg_at_3
      value: 34.910000000000004
    - type: ndcg_at_5
      value: 38.937
    - type: precision_at_1
      value: 23.910999999999998
    - type: precision_at_10
      value: 6.758
    - type: precision_at_100
      value: 0.9520000000000001
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 14.838000000000001
    - type: precision_at_5
      value: 10.934000000000001
    - type: recall_at_1
      value: 23.179
    - type: recall_at_10
      value: 64.622
    - type: recall_at_100
      value: 90.135
    - type: recall_at_1000
      value: 98.301
    - type: recall_at_3
      value: 42.836999999999996
    - type: recall_at_5
      value: 52.512
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
      value: 96.59598723210215
    - type: f1
      value: 96.41913500001952
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
      value: 82.89557683538533
    - type: f1
      value: 63.379319722356264
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
      value: 78.93745796906524
    - type: f1
      value: 75.71616541785902
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
      value: 81.41223940820443
    - type: f1
      value: 81.2877893719078
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
      value: 35.03682528325662
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
      value: 32.942529406124
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
      value: 31.459949660460317
    - type: mrr
      value: 32.70509582031616
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
      value: 6.497
    - type: map_at_10
      value: 13.843
    - type: map_at_100
      value: 17.713
    - type: map_at_1000
      value: 19.241
    - type: map_at_3
      value: 10.096
    - type: map_at_5
      value: 11.85
    - type: mrr_at_1
      value: 48.916
    - type: mrr_at_10
      value: 57.764
    - type: mrr_at_100
      value: 58.251
    - type: mrr_at_1000
      value: 58.282999999999994
    - type: mrr_at_3
      value: 55.623999999999995
    - type: mrr_at_5
      value: 57.018
    - type: ndcg_at_1
      value: 46.594
    - type: ndcg_at_10
      value: 36.945
    - type: ndcg_at_100
      value: 34.06
    - type: ndcg_at_1000
      value: 43.05
    - type: ndcg_at_3
      value: 41.738
    - type: ndcg_at_5
      value: 39.330999999999996
    - type: precision_at_1
      value: 48.916
    - type: precision_at_10
      value: 27.43
    - type: precision_at_100
      value: 8.616
    - type: precision_at_1000
      value: 2.155
    - type: precision_at_3
      value: 39.112
    - type: precision_at_5
      value: 33.808
    - type: recall_at_1
      value: 6.497
    - type: recall_at_10
      value: 18.163
    - type: recall_at_100
      value: 34.566
    - type: recall_at_1000
      value: 67.15
    - type: recall_at_3
      value: 11.100999999999999
    - type: recall_at_5
      value: 14.205000000000002
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
      value: 31.916
    - type: map_at_10
      value: 48.123
    - type: map_at_100
      value: 49.103
    - type: map_at_1000
      value: 49.131
    - type: map_at_3
      value: 43.711
    - type: map_at_5
      value: 46.323
    - type: mrr_at_1
      value: 36.181999999999995
    - type: mrr_at_10
      value: 50.617999999999995
    - type: mrr_at_100
      value: 51.329
    - type: mrr_at_1000
      value: 51.348000000000006
    - type: mrr_at_3
      value: 47.010999999999996
    - type: mrr_at_5
      value: 49.175000000000004
    - type: ndcg_at_1
      value: 36.181999999999995
    - type: ndcg_at_10
      value: 56.077999999999996
    - type: ndcg_at_100
      value: 60.037
    - type: ndcg_at_1000
      value: 60.63499999999999
    - type: ndcg_at_3
      value: 47.859
    - type: ndcg_at_5
      value: 52.178999999999995
    - type: precision_at_1
      value: 36.181999999999995
    - type: precision_at_10
      value: 9.284
    - type: precision_at_100
      value: 1.149
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 22.006999999999998
    - type: precision_at_5
      value: 15.695
    - type: recall_at_1
      value: 31.916
    - type: recall_at_10
      value: 77.771
    - type: recall_at_100
      value: 94.602
    - type: recall_at_1000
      value: 98.967
    - type: recall_at_3
      value: 56.528
    - type: recall_at_5
      value: 66.527
  - task:
      type: Retrieval
    dataset:
      type: mteb/quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 71.486
    - type: map_at_10
      value: 85.978
    - type: map_at_100
      value: 86.587
    - type: map_at_1000
      value: 86.598
    - type: map_at_3
      value: 83.04899999999999
    - type: map_at_5
      value: 84.857
    - type: mrr_at_1
      value: 82.32000000000001
    - type: mrr_at_10
      value: 88.64
    - type: mrr_at_100
      value: 88.702
    - type: mrr_at_1000
      value: 88.702
    - type: mrr_at_3
      value: 87.735
    - type: mrr_at_5
      value: 88.36
    - type: ndcg_at_1
      value: 82.34
    - type: ndcg_at_10
      value: 89.67
    - type: ndcg_at_100
      value: 90.642
    - type: ndcg_at_1000
      value: 90.688
    - type: ndcg_at_3
      value: 86.932
    - type: ndcg_at_5
      value: 88.408
    - type: precision_at_1
      value: 82.34
    - type: precision_at_10
      value: 13.675999999999998
    - type: precision_at_100
      value: 1.544
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 38.24
    - type: precision_at_5
      value: 25.068
    - type: recall_at_1
      value: 71.486
    - type: recall_at_10
      value: 96.844
    - type: recall_at_100
      value: 99.843
    - type: recall_at_1000
      value: 99.996
    - type: recall_at_3
      value: 88.92099999999999
    - type: recall_at_5
      value: 93.215
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
      value: 59.75758437908334
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
      value: 68.03497914092789
  - task:
      type: Retrieval
    dataset:
      type: mteb/scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 5.808
    - type: map_at_10
      value: 16.059
    - type: map_at_100
      value: 19.048000000000002
    - type: map_at_1000
      value: 19.43
    - type: map_at_3
      value: 10.953
    - type: map_at_5
      value: 13.363
    - type: mrr_at_1
      value: 28.7
    - type: mrr_at_10
      value: 42.436
    - type: mrr_at_100
      value: 43.599
    - type: mrr_at_1000
      value: 43.62
    - type: mrr_at_3
      value: 38.45
    - type: mrr_at_5
      value: 40.89
    - type: ndcg_at_1
      value: 28.7
    - type: ndcg_at_10
      value: 26.346000000000004
    - type: ndcg_at_100
      value: 36.758
    - type: ndcg_at_1000
      value: 42.113
    - type: ndcg_at_3
      value: 24.254
    - type: ndcg_at_5
      value: 21.506
    - type: precision_at_1
      value: 28.7
    - type: precision_at_10
      value: 13.969999999999999
    - type: precision_at_100
      value: 2.881
    - type: precision_at_1000
      value: 0.414
    - type: precision_at_3
      value: 22.933
    - type: precision_at_5
      value: 19.220000000000002
    - type: recall_at_1
      value: 5.808
    - type: recall_at_10
      value: 28.310000000000002
    - type: recall_at_100
      value: 58.475
    - type: recall_at_1000
      value: 84.072
    - type: recall_at_3
      value: 13.957
    - type: recall_at_5
      value: 19.515
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
      value: 82.39274129958557
    - type: cos_sim_spearman
      value: 79.78021235170053
    - type: euclidean_pearson
      value: 79.35335401300166
    - type: euclidean_spearman
      value: 79.7271870968275
    - type: manhattan_pearson
      value: 79.35256263340601
    - type: manhattan_spearman
      value: 79.76036386976321
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
      value: 83.99130429246708
    - type: cos_sim_spearman
      value: 73.88322811171203
    - type: euclidean_pearson
      value: 80.7569419170376
    - type: euclidean_spearman
      value: 73.82542155409597
    - type: manhattan_pearson
      value: 80.79468183847625
    - type: manhattan_spearman
      value: 73.87027144047784
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
      value: 84.88548789489907
    - type: cos_sim_spearman
      value: 85.07535893847255
    - type: euclidean_pearson
      value: 84.6637222061494
    - type: euclidean_spearman
      value: 85.14200626702456
    - type: manhattan_pearson
      value: 84.75327892344734
    - type: manhattan_spearman
      value: 85.24406181838596
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
      value: 82.88140039325008
    - type: cos_sim_spearman
      value: 79.61211268112362
    - type: euclidean_pearson
      value: 81.29639728816458
    - type: euclidean_spearman
      value: 79.51284578041442
    - type: manhattan_pearson
      value: 81.3381797137111
    - type: manhattan_spearman
      value: 79.55683684039808
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
      value: 85.16716737270485
    - type: cos_sim_spearman
      value: 86.14823841857738
    - type: euclidean_pearson
      value: 85.36325733440725
    - type: euclidean_spearman
      value: 86.04919691402029
    - type: manhattan_pearson
      value: 85.3147511385052
    - type: manhattan_spearman
      value: 86.00676205857764
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
      value: 80.34266645861588
    - type: cos_sim_spearman
      value: 81.59914035005882
    - type: euclidean_pearson
      value: 81.15053076245988
    - type: euclidean_spearman
      value: 81.52776915798489
    - type: manhattan_pearson
      value: 81.1819647418673
    - type: manhattan_spearman
      value: 81.57479527353556
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
      value: 89.38263326821439
    - type: cos_sim_spearman
      value: 89.10946308202642
    - type: euclidean_pearson
      value: 88.87831312540068
    - type: euclidean_spearman
      value: 89.03615865973664
    - type: manhattan_pearson
      value: 88.79835539970384
    - type: manhattan_spearman
      value: 88.9766156339753
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
      value: 70.1574915581685
    - type: cos_sim_spearman
      value: 70.59144980004054
    - type: euclidean_pearson
      value: 71.43246306918755
    - type: euclidean_spearman
      value: 70.5544189562984
    - type: manhattan_pearson
      value: 71.4071414609503
    - type: manhattan_spearman
      value: 70.31799126163712
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
      value: 83.36215796635351
    - type: cos_sim_spearman
      value: 83.07276756467208
    - type: euclidean_pearson
      value: 83.06690453635584
    - type: euclidean_spearman
      value: 82.9635366303289
    - type: manhattan_pearson
      value: 83.04994049700815
    - type: manhattan_spearman
      value: 82.98120125356036
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
      value: 86.92530011616722
    - type: mrr
      value: 96.21826793395421
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
      value: 65.75
    - type: map_at_10
      value: 77.701
    - type: map_at_100
      value: 78.005
    - type: map_at_1000
      value: 78.006
    - type: map_at_3
      value: 75.48
    - type: map_at_5
      value: 76.927
    - type: mrr_at_1
      value: 68.333
    - type: mrr_at_10
      value: 78.511
    - type: mrr_at_100
      value: 78.704
    - type: mrr_at_1000
      value: 78.704
    - type: mrr_at_3
      value: 77
    - type: mrr_at_5
      value: 78.083
    - type: ndcg_at_1
      value: 68.333
    - type: ndcg_at_10
      value: 82.42699999999999
    - type: ndcg_at_100
      value: 83.486
    - type: ndcg_at_1000
      value: 83.511
    - type: ndcg_at_3
      value: 78.96300000000001
    - type: ndcg_at_5
      value: 81.028
    - type: precision_at_1
      value: 68.333
    - type: precision_at_10
      value: 10.667
    - type: precision_at_100
      value: 1.127
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 31.333
    - type: precision_at_5
      value: 20.133000000000003
    - type: recall_at_1
      value: 65.75
    - type: recall_at_10
      value: 95.578
    - type: recall_at_100
      value: 99.833
    - type: recall_at_1000
      value: 100
    - type: recall_at_3
      value: 86.506
    - type: recall_at_5
      value: 91.75
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
      value: 99.75247524752476
    - type: cos_sim_ap
      value: 94.16065078045173
    - type: cos_sim_f1
      value: 87.22986247544205
    - type: cos_sim_precision
      value: 85.71428571428571
    - type: cos_sim_recall
      value: 88.8
    - type: dot_accuracy
      value: 99.74554455445545
    - type: dot_ap
      value: 93.90633887037264
    - type: dot_f1
      value: 86.9873417721519
    - type: dot_precision
      value: 88.1025641025641
    - type: dot_recall
      value: 85.9
    - type: euclidean_accuracy
      value: 99.75247524752476
    - type: euclidean_ap
      value: 94.17466319018055
    - type: euclidean_f1
      value: 87.3405299313052
    - type: euclidean_precision
      value: 85.74181117533719
    - type: euclidean_recall
      value: 89
    - type: manhattan_accuracy
      value: 99.75445544554455
    - type: manhattan_ap
      value: 94.27688371923577
    - type: manhattan_f1
      value: 87.74002954209749
    - type: manhattan_precision
      value: 86.42095053346266
    - type: manhattan_recall
      value: 89.1
    - type: max_accuracy
      value: 99.75445544554455
    - type: max_ap
      value: 94.27688371923577
    - type: max_f1
      value: 87.74002954209749
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
      value: 71.26500637517056
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
      value: 39.17507906280528
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
      value: 52.4848744828509
    - type: mrr
      value: 53.33678168236992
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
      value: 30.599864323827887
    - type: cos_sim_spearman
      value: 30.91116204665598
    - type: dot_pearson
      value: 30.82637894269936
    - type: dot_spearman
      value: 30.957573868416066
  - task:
      type: Retrieval
    dataset:
      type: mteb/trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 0.23600000000000002
    - type: map_at_10
      value: 1.892
    - type: map_at_100
      value: 11.586
    - type: map_at_1000
      value: 27.761999999999997
    - type: map_at_3
      value: 0.653
    - type: map_at_5
      value: 1.028
    - type: mrr_at_1
      value: 88
    - type: mrr_at_10
      value: 94
    - type: mrr_at_100
      value: 94
    - type: mrr_at_1000
      value: 94
    - type: mrr_at_3
      value: 94
    - type: mrr_at_5
      value: 94
    - type: ndcg_at_1
      value: 82
    - type: ndcg_at_10
      value: 77.48899999999999
    - type: ndcg_at_100
      value: 60.141
    - type: ndcg_at_1000
      value: 54.228
    - type: ndcg_at_3
      value: 82.358
    - type: ndcg_at_5
      value: 80.449
    - type: precision_at_1
      value: 88
    - type: precision_at_10
      value: 82.19999999999999
    - type: precision_at_100
      value: 61.760000000000005
    - type: precision_at_1000
      value: 23.684
    - type: precision_at_3
      value: 88
    - type: precision_at_5
      value: 85.6
    - type: recall_at_1
      value: 0.23600000000000002
    - type: recall_at_10
      value: 2.117
    - type: recall_at_100
      value: 14.985000000000001
    - type: recall_at_1000
      value: 51.107
    - type: recall_at_3
      value: 0.688
    - type: recall_at_5
      value: 1.1039999999999999
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
      value: 2.3040000000000003
    - type: map_at_10
      value: 9.025
    - type: map_at_100
      value: 15.312999999999999
    - type: map_at_1000
      value: 16.954
    - type: map_at_3
      value: 4.981
    - type: map_at_5
      value: 6.32
    - type: mrr_at_1
      value: 24.490000000000002
    - type: mrr_at_10
      value: 39.835
    - type: mrr_at_100
      value: 40.8
    - type: mrr_at_1000
      value: 40.8
    - type: mrr_at_3
      value: 35.034
    - type: mrr_at_5
      value: 37.687
    - type: ndcg_at_1
      value: 22.448999999999998
    - type: ndcg_at_10
      value: 22.545
    - type: ndcg_at_100
      value: 35.931999999999995
    - type: ndcg_at_1000
      value: 47.665
    - type: ndcg_at_3
      value: 23.311
    - type: ndcg_at_5
      value: 22.421
    - type: precision_at_1
      value: 24.490000000000002
    - type: precision_at_10
      value: 20.408
    - type: precision_at_100
      value: 7.815999999999999
    - type: precision_at_1000
      value: 1.553
    - type: precision_at_3
      value: 25.169999999999998
    - type: precision_at_5
      value: 23.265
    - type: recall_at_1
      value: 2.3040000000000003
    - type: recall_at_10
      value: 15.693999999999999
    - type: recall_at_100
      value: 48.917
    - type: recall_at_1000
      value: 84.964
    - type: recall_at_3
      value: 6.026
    - type: recall_at_5
      value: 9.066
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
      value: 82.6074
    - type: ap
      value: 23.187467098602013
    - type: f1
      value: 65.36829506379657
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
      value: 63.16355404640635
    - type: f1
      value: 63.534725639863346
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
      value: 50.91004094411276
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
      value: 86.55301901412649
    - type: cos_sim_ap
      value: 75.25312618556728
    - type: cos_sim_f1
      value: 68.76561719140429
    - type: cos_sim_precision
      value: 65.3061224489796
    - type: cos_sim_recall
      value: 72.61213720316623
    - type: dot_accuracy
      value: 86.29671574178936
    - type: dot_ap
      value: 75.11910195501207
    - type: dot_f1
      value: 68.44048376830045
    - type: dot_precision
      value: 66.12546125461255
    - type: dot_recall
      value: 70.92348284960423
    - type: euclidean_accuracy
      value: 86.5828217202122
    - type: euclidean_ap
      value: 75.22986344900924
    - type: euclidean_f1
      value: 68.81267797449549
    - type: euclidean_precision
      value: 64.8238861674831
    - type: euclidean_recall
      value: 73.3245382585752
    - type: manhattan_accuracy
      value: 86.61262442629791
    - type: manhattan_ap
      value: 75.24401608557328
    - type: manhattan_f1
      value: 68.80473982483257
    - type: manhattan_precision
      value: 67.21187720181177
    - type: manhattan_recall
      value: 70.47493403693932
    - type: max_accuracy
      value: 86.61262442629791
    - type: max_ap
      value: 75.25312618556728
    - type: max_f1
      value: 68.81267797449549
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
      value: 88.10688089416696
    - type: cos_sim_ap
      value: 84.17862178779863
    - type: cos_sim_f1
      value: 76.17305208781748
    - type: cos_sim_precision
      value: 71.31246641590543
    - type: cos_sim_recall
      value: 81.74468740375731
    - type: dot_accuracy
      value: 88.1844995536927
    - type: dot_ap
      value: 84.33816725235876
    - type: dot_f1
      value: 76.43554032918746
    - type: dot_precision
      value: 74.01557767200346
    - type: dot_recall
      value: 79.0190945488143
    - type: euclidean_accuracy
      value: 88.07001203089223
    - type: euclidean_ap
      value: 84.12267000814985
    - type: euclidean_f1
      value: 76.12232600180778
    - type: euclidean_precision
      value: 74.50604541433205
    - type: euclidean_recall
      value: 77.81028641823221
    - type: manhattan_accuracy
      value: 88.06419063142779
    - type: manhattan_ap
      value: 84.11648917164187
    - type: manhattan_f1
      value: 76.20579953925474
    - type: manhattan_precision
      value: 72.56772755762935
    - type: manhattan_recall
      value: 80.22790267939637
    - type: max_accuracy
      value: 88.1844995536927
    - type: max_ap
      value: 84.33816725235876
    - type: max_f1
      value: 76.43554032918746
---

<!-- **English** | [中文](./README_zh.md) -->

# gte-large-en-v1.5

We introduce `gte-v1.5` series, upgraded `gte` embeddings that support the context length of up to **8192**, while further enhancing model performance.
The models are built upon the `transformer++` encoder [backbone](https://huggingface.co/Alibaba-NLP/new-impl) (BERT + RoPE + GLU).

The `gte-v1.5` series achieve state-of-the-art scores on the MTEB benchmark within the same model size category and prodvide competitive on the LoCo long-context retrieval tests (refer to [Evaluation](#evaluation)).

We also present the [`gte-Qwen1.5-7B-instruct`](https://huggingface.co/Alibaba-NLP/gte-Qwen1.5-7B-instruct),
a SOTA instruction-tuned multi-lingual embedding model that ranked 2nd in MTEB and 1st in C-MTEB.

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Institute for Intelligent Computing, Alibaba Group
- **Model type:** Text Embeddings
- **Paper:** [mGTE: Generalized Long-Context Text Representation and Reranking
Models for Multilingual Text Retrieval](https://arxiv.org/pdf/2407.19669)

<!-- - **Demo [optional]:** [More Information Needed] -->

### Model list

| Models | Language | Model Size | Max Seq. Length | Dimension | MTEB-en | LoCo |
|:-----: | :-----: |:-----: |:-----: |:-----: | :-----: | :-----: |
|[`gte-Qwen1.5-7B-instruct`](https://huggingface.co/Alibaba-NLP/gte-Qwen1.5-7B-instruct)| Multiple | 7720 | 32768 | 4096 | 67.34 | 87.57 |
|[`gte-large-en-v1.5`](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5) | English | 434 | 8192 | 1024 | 65.39 | 86.71 |
|[`gte-base-en-v1.5`](https://huggingface.co/Alibaba-NLP/gte-base-en-v1.5) | English | 137 | 8192 | 768 | 64.11 | 87.44 |


## How to Get Started with the Model

Use the code below to get started with the model.

```python
# Requires transformers>=4.36.0

import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer

input_texts = [
    "what is the capital of China?",
    "how to implement quick sort in python?",
    "Beijing",
    "sorting algorithms"
]

model_path = 'Alibaba-NLP/gte-large-en-v1.5'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True)

# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=8192, padding=True, truncation=True, return_tensors='pt')

outputs = model(**batch_dict)
embeddings = outputs.last_hidden_state[:, 0]
 
# (Optionally) normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:1] @ embeddings[1:].T) * 100
print(scores.tolist())
```

**It is recommended to install xformers and enable unpadding for acceleration, refer to [enable-unpadding-and-xformers](https://huggingface.co/Alibaba-NLP/new-impl#recommendation-enable-unpadding-and-acceleration-with-xformers).**


Use with sentence-transformers:

```python
# Requires sentence_transformers>=2.7.0

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

sentences = ['That is a happy person', 'That is a very happy person']

model = SentenceTransformer('Alibaba-NLP/gte-large-en-v1.5', trust_remote_code=True)
embeddings = model.encode(sentences)
print(cos_sim(embeddings[0], embeddings[1]))
```

Use with `transformers.js`:

```js
// npm i @xenova/transformers
import { pipeline, dot } from '@xenova/transformers';

// Create feature extraction pipeline
const extractor = await pipeline('feature-extraction', 'Alibaba-NLP/gte-large-en-v1.5', {
    quantized: false, // Comment out this line to use the quantized version
});

// Generate sentence embeddings
const sentences = [
    "what is the capital of China?",
    "how to implement quick sort in python?",
    "Beijing",
    "sorting algorithms"
]
const output = await extractor(sentences, { normalize: true, pooling: 'cls' });

// Compute similarity scores
const [source_embeddings, ...document_embeddings ] = output.tolist();
const similarities = document_embeddings.map(x => 100 * dot(source_embeddings, x));
console.log(similarities); // [41.86354093370361, 77.07076371259589, 37.02981979677899]
```

## Training Details

### Training Data

- Masked language modeling (MLM): `c4-en`
- Weak-supervised contrastive pre-training (CPT): [GTE](https://arxiv.org/pdf/2308.03281.pdf) pre-training data
- Supervised contrastive fine-tuning: [GTE](https://arxiv.org/pdf/2308.03281.pdf) fine-tuning data

### Training Procedure 

To enable the backbone model to support a context length of 8192, we adopted a multi-stage training strategy.
The model first undergoes preliminary MLM pre-training on shorter lengths.
And then, we resample the data, reducing the proportion of short texts, and continue the MLM pre-training.

The entire training process is as follows:
- MLM-512: lr 2e-4, mlm_probability 0.3, batch_size 4096, num_steps 300000, rope_base 10000
- MLM-2048: lr 5e-5, mlm_probability 0.3, batch_size 4096, num_steps 30000, rope_base 10000
- [MLM-8192](https://huggingface.co/Alibaba-NLP/gte-en-mlm-large): lr 5e-5, mlm_probability 0.3, batch_size 1024, num_steps 30000, rope_base 160000
- CPT: max_len 512, lr 5e-5, batch_size 28672, num_steps 100000
- Fine-tuning: TODO


## Evaluation


### MTEB

The results of other models are retrieved from [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard).

The gte evaluation setting: `mteb==1.2.0, fp16 auto mix precision, max_length=8192`, and set ntk scaling factor to 2 (equivalent to rope_base * 2).

| Model Name | Param Size (M) | Dimension | Sequence Length | Average (56) | Class. (12) | Clust. (11) | Pair Class. (3) | Reran. (4) | Retr. (15) | STS (10) | Summ. (1) |
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**gte-large-en-v1.5**](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5) | 409 | 1024 | 8192 | **65.39** | 77.75 | 47.95 | 84.63 | 58.50 | 57.91 | 81.43 | 30.91 |
| [mxbai-embed-large-v1](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1) | 335 | 1024 | 512 | 64.68 | 75.64 | 46.71 | 87.2 | 60.11 | 54.39 | 85 | 32.71 |
| [multilingual-e5-large-instruct](https://huggingface.co/intfloat/multilingual-e5-large-instruct) | 560 | 1024 | 514 | 64.41 | 77.56 | 47.1 | 86.19 | 58.58 | 52.47 | 84.78 | 30.39 |
| [bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5)| 335 | 1024 | 512 | 64.23 | 75.97 | 46.08 | 87.12 | 60.03 | 54.29 | 83.11 | 31.61 |
| [**gte-base-en-v1.5**](https://huggingface.co/Alibaba-NLP/gte-base-en-v1.5) | 137 | 768 | 8192 | **64.11** | 77.17 | 46.82 | 85.33 | 57.66 | 54.09 | 81.97 | 31.17 |
| [bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5)| 109 | 768 | 512 | 63.55 | 75.53 | 45.77 | 86.55 | 58.86 | 53.25 | 82.4 | 31.07 |


### LoCo

| Model Name |  Dimension | Sequence Length | Average (5) | QsmsumRetrieval | SummScreenRetrieval | QasperAbastractRetrieval | QasperTitleRetrieval |  GovReportRetrieval |
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [gte-qwen1.5-7b](https://huggingface.co/Alibaba-NLP/gte-qwen1.5-7b) | 4096 | 32768 |  87.57 | 49.37 | 93.10 | 99.67 | 97.54 | 98.21 | 
| [gte-large-v1.5](https://huggingface.co/Alibaba-NLP/gte-large-v1.5) |1024 | 8192 | 86.71 | 44.55 | 92.61 | 99.82 | 97.81 | 98.74 |
| [gte-base-v1.5](https://huggingface.co/Alibaba-NLP/gte-base-v1.5) | 768 | 8192 | 87.44 | 49.91  | 91.78 | 99.82 | 97.13 | 98.58 |



## Citation

If you find our paper or models helpful, please consider citing them as follows:

```
@article{zhang2024mgte,
  title={mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual Text Retrieval},
  author={Zhang, Xin and Zhang, Yanzhao and Long, Dingkun and Xie, Wen and Dai, Ziqi and Tang, Jialong and Lin, Huan and Yang, Baosong and Xie, Pengjun and Huang, Fei and others},
  journal={arXiv preprint arXiv:2407.19669},
  year={2024}
}

@article{li2023towards,
  title={Towards general text embeddings with multi-stage contrastive learning},
  author={Li, Zehan and Zhang, Xin and Zhang, Yanzhao and Long, Dingkun and Xie, Pengjun and Zhang, Meishan},
  journal={arXiv preprint arXiv:2308.03281},
  year={2023}
}
```