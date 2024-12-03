---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- mteb
model-index:
- name: bge_micro
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
      value: 67.76119402985074
    - type: ap
      value: 29.637849284211114
    - type: f1
      value: 61.31181187111905
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
      value: 79.7547
    - type: ap
      value: 74.21401629809145
    - type: f1
      value: 79.65319615433783
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
      value: 37.452000000000005
    - type: f1
      value: 37.0245198854966
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
      value: 31.152
    - type: map_at_10
      value: 46.702
    - type: map_at_100
      value: 47.563
    - type: map_at_1000
      value: 47.567
    - type: map_at_3
      value: 42.058
    - type: map_at_5
      value: 44.608
    - type: mrr_at_1
      value: 32.006
    - type: mrr_at_10
      value: 47.064
    - type: mrr_at_100
      value: 47.910000000000004
    - type: mrr_at_1000
      value: 47.915
    - type: mrr_at_3
      value: 42.283
    - type: mrr_at_5
      value: 44.968
    - type: ndcg_at_1
      value: 31.152
    - type: ndcg_at_10
      value: 55.308
    - type: ndcg_at_100
      value: 58.965
    - type: ndcg_at_1000
      value: 59.067
    - type: ndcg_at_3
      value: 45.698
    - type: ndcg_at_5
      value: 50.296
    - type: precision_at_1
      value: 31.152
    - type: precision_at_10
      value: 8.279
    - type: precision_at_100
      value: 0.987
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 18.753
    - type: precision_at_5
      value: 13.485
    - type: recall_at_1
      value: 31.152
    - type: recall_at_10
      value: 82.788
    - type: recall_at_100
      value: 98.72
    - type: recall_at_1000
      value: 99.502
    - type: recall_at_3
      value: 56.259
    - type: recall_at_5
      value: 67.425
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
      value: 44.52692241938116
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
      value: 33.245710292773595
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
      value: 58.08493637155168
    - type: mrr
      value: 71.94378490084861
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
      value: 84.1602804378326
    - type: cos_sim_spearman
      value: 82.92478106365587
    - type: euclidean_pearson
      value: 82.27930167277077
    - type: euclidean_spearman
      value: 82.18560759458093
    - type: manhattan_pearson
      value: 82.34277425888187
    - type: manhattan_spearman
      value: 81.72776583704467
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
      value: 81.17207792207792
    - type: f1
      value: 81.09893836310513
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
      value: 36.109308463095516
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
      value: 28.06048212317168
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
      value: 28.233999999999998
    - type: map_at_10
      value: 38.092999999999996
    - type: map_at_100
      value: 39.473
    - type: map_at_1000
      value: 39.614
    - type: map_at_3
      value: 34.839
    - type: map_at_5
      value: 36.523
    - type: mrr_at_1
      value: 35.193000000000005
    - type: mrr_at_10
      value: 44.089
    - type: mrr_at_100
      value: 44.927
    - type: mrr_at_1000
      value: 44.988
    - type: mrr_at_3
      value: 41.559000000000005
    - type: mrr_at_5
      value: 43.162
    - type: ndcg_at_1
      value: 35.193000000000005
    - type: ndcg_at_10
      value: 44.04
    - type: ndcg_at_100
      value: 49.262
    - type: ndcg_at_1000
      value: 51.847
    - type: ndcg_at_3
      value: 39.248
    - type: ndcg_at_5
      value: 41.298
    - type: precision_at_1
      value: 35.193000000000005
    - type: precision_at_10
      value: 8.555
    - type: precision_at_100
      value: 1.3820000000000001
    - type: precision_at_1000
      value: 0.189
    - type: precision_at_3
      value: 19.123
    - type: precision_at_5
      value: 13.648
    - type: recall_at_1
      value: 28.233999999999998
    - type: recall_at_10
      value: 55.094
    - type: recall_at_100
      value: 76.85300000000001
    - type: recall_at_1000
      value: 94.163
    - type: recall_at_3
      value: 40.782000000000004
    - type: recall_at_5
      value: 46.796
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
      value: 21.538
    - type: map_at_10
      value: 28.449
    - type: map_at_100
      value: 29.471000000000004
    - type: map_at_1000
      value: 29.599999999999998
    - type: map_at_3
      value: 26.371
    - type: map_at_5
      value: 27.58
    - type: mrr_at_1
      value: 26.815
    - type: mrr_at_10
      value: 33.331
    - type: mrr_at_100
      value: 34.114
    - type: mrr_at_1000
      value: 34.182
    - type: mrr_at_3
      value: 31.561
    - type: mrr_at_5
      value: 32.608
    - type: ndcg_at_1
      value: 26.815
    - type: ndcg_at_10
      value: 32.67
    - type: ndcg_at_100
      value: 37.039
    - type: ndcg_at_1000
      value: 39.769
    - type: ndcg_at_3
      value: 29.523
    - type: ndcg_at_5
      value: 31.048
    - type: precision_at_1
      value: 26.815
    - type: precision_at_10
      value: 5.955
    - type: precision_at_100
      value: 1.02
    - type: precision_at_1000
      value: 0.152
    - type: precision_at_3
      value: 14.033999999999999
    - type: precision_at_5
      value: 9.911
    - type: recall_at_1
      value: 21.538
    - type: recall_at_10
      value: 40.186
    - type: recall_at_100
      value: 58.948
    - type: recall_at_1000
      value: 77.158
    - type: recall_at_3
      value: 30.951
    - type: recall_at_5
      value: 35.276
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
      value: 35.211999999999996
    - type: map_at_10
      value: 46.562
    - type: map_at_100
      value: 47.579
    - type: map_at_1000
      value: 47.646
    - type: map_at_3
      value: 43.485
    - type: map_at_5
      value: 45.206
    - type: mrr_at_1
      value: 40.627
    - type: mrr_at_10
      value: 49.928
    - type: mrr_at_100
      value: 50.647
    - type: mrr_at_1000
      value: 50.685
    - type: mrr_at_3
      value: 47.513
    - type: mrr_at_5
      value: 48.958
    - type: ndcg_at_1
      value: 40.627
    - type: ndcg_at_10
      value: 52.217
    - type: ndcg_at_100
      value: 56.423
    - type: ndcg_at_1000
      value: 57.821999999999996
    - type: ndcg_at_3
      value: 46.949000000000005
    - type: ndcg_at_5
      value: 49.534
    - type: precision_at_1
      value: 40.627
    - type: precision_at_10
      value: 8.476
    - type: precision_at_100
      value: 1.15
    - type: precision_at_1000
      value: 0.132
    - type: precision_at_3
      value: 21.003
    - type: precision_at_5
      value: 14.469999999999999
    - type: recall_at_1
      value: 35.211999999999996
    - type: recall_at_10
      value: 65.692
    - type: recall_at_100
      value: 84.011
    - type: recall_at_1000
      value: 94.03099999999999
    - type: recall_at_3
      value: 51.404
    - type: recall_at_5
      value: 57.882
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
      value: 22.09
    - type: map_at_10
      value: 29.516
    - type: map_at_100
      value: 30.462
    - type: map_at_1000
      value: 30.56
    - type: map_at_3
      value: 26.945000000000004
    - type: map_at_5
      value: 28.421999999999997
    - type: mrr_at_1
      value: 23.616
    - type: mrr_at_10
      value: 31.221
    - type: mrr_at_100
      value: 32.057
    - type: mrr_at_1000
      value: 32.137
    - type: mrr_at_3
      value: 28.738000000000003
    - type: mrr_at_5
      value: 30.156
    - type: ndcg_at_1
      value: 23.616
    - type: ndcg_at_10
      value: 33.97
    - type: ndcg_at_100
      value: 38.806000000000004
    - type: ndcg_at_1000
      value: 41.393
    - type: ndcg_at_3
      value: 28.908
    - type: ndcg_at_5
      value: 31.433
    - type: precision_at_1
      value: 23.616
    - type: precision_at_10
      value: 5.299
    - type: precision_at_100
      value: 0.812
    - type: precision_at_1000
      value: 0.107
    - type: precision_at_3
      value: 12.015
    - type: precision_at_5
      value: 8.701
    - type: recall_at_1
      value: 22.09
    - type: recall_at_10
      value: 46.089999999999996
    - type: recall_at_100
      value: 68.729
    - type: recall_at_1000
      value: 88.435
    - type: recall_at_3
      value: 32.584999999999994
    - type: recall_at_5
      value: 38.550000000000004
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
      value: 15.469
    - type: map_at_10
      value: 22.436
    - type: map_at_100
      value: 23.465
    - type: map_at_1000
      value: 23.608999999999998
    - type: map_at_3
      value: 19.716
    - type: map_at_5
      value: 21.182000000000002
    - type: mrr_at_1
      value: 18.905
    - type: mrr_at_10
      value: 26.55
    - type: mrr_at_100
      value: 27.46
    - type: mrr_at_1000
      value: 27.553
    - type: mrr_at_3
      value: 23.921999999999997
    - type: mrr_at_5
      value: 25.302999999999997
    - type: ndcg_at_1
      value: 18.905
    - type: ndcg_at_10
      value: 27.437
    - type: ndcg_at_100
      value: 32.555
    - type: ndcg_at_1000
      value: 35.885
    - type: ndcg_at_3
      value: 22.439
    - type: ndcg_at_5
      value: 24.666
    - type: precision_at_1
      value: 18.905
    - type: precision_at_10
      value: 5.2490000000000006
    - type: precision_at_100
      value: 0.889
    - type: precision_at_1000
      value: 0.131
    - type: precision_at_3
      value: 10.862
    - type: precision_at_5
      value: 8.085
    - type: recall_at_1
      value: 15.469
    - type: recall_at_10
      value: 38.706
    - type: recall_at_100
      value: 61.242
    - type: recall_at_1000
      value: 84.84
    - type: recall_at_3
      value: 24.973
    - type: recall_at_5
      value: 30.603
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
      value: 24.918000000000003
    - type: map_at_10
      value: 34.296
    - type: map_at_100
      value: 35.632000000000005
    - type: map_at_1000
      value: 35.748999999999995
    - type: map_at_3
      value: 31.304
    - type: map_at_5
      value: 33.166000000000004
    - type: mrr_at_1
      value: 30.703000000000003
    - type: mrr_at_10
      value: 39.655
    - type: mrr_at_100
      value: 40.569
    - type: mrr_at_1000
      value: 40.621
    - type: mrr_at_3
      value: 37.023
    - type: mrr_at_5
      value: 38.664
    - type: ndcg_at_1
      value: 30.703000000000003
    - type: ndcg_at_10
      value: 39.897
    - type: ndcg_at_100
      value: 45.777
    - type: ndcg_at_1000
      value: 48.082
    - type: ndcg_at_3
      value: 35.122
    - type: ndcg_at_5
      value: 37.691
    - type: precision_at_1
      value: 30.703000000000003
    - type: precision_at_10
      value: 7.305000000000001
    - type: precision_at_100
      value: 1.208
    - type: precision_at_1000
      value: 0.159
    - type: precision_at_3
      value: 16.811
    - type: precision_at_5
      value: 12.203999999999999
    - type: recall_at_1
      value: 24.918000000000003
    - type: recall_at_10
      value: 51.31
    - type: recall_at_100
      value: 76.534
    - type: recall_at_1000
      value: 91.911
    - type: recall_at_3
      value: 37.855
    - type: recall_at_5
      value: 44.493
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
      value: 22.416
    - type: map_at_10
      value: 30.474
    - type: map_at_100
      value: 31.759999999999998
    - type: map_at_1000
      value: 31.891000000000002
    - type: map_at_3
      value: 27.728
    - type: map_at_5
      value: 29.247
    - type: mrr_at_1
      value: 28.881
    - type: mrr_at_10
      value: 36.418
    - type: mrr_at_100
      value: 37.347
    - type: mrr_at_1000
      value: 37.415
    - type: mrr_at_3
      value: 33.942
    - type: mrr_at_5
      value: 35.386
    - type: ndcg_at_1
      value: 28.881
    - type: ndcg_at_10
      value: 35.812
    - type: ndcg_at_100
      value: 41.574
    - type: ndcg_at_1000
      value: 44.289
    - type: ndcg_at_3
      value: 31.239
    - type: ndcg_at_5
      value: 33.302
    - type: precision_at_1
      value: 28.881
    - type: precision_at_10
      value: 6.598
    - type: precision_at_100
      value: 1.1079999999999999
    - type: precision_at_1000
      value: 0.151
    - type: precision_at_3
      value: 14.954
    - type: precision_at_5
      value: 10.776
    - type: recall_at_1
      value: 22.416
    - type: recall_at_10
      value: 46.243
    - type: recall_at_100
      value: 71.352
    - type: recall_at_1000
      value: 90.034
    - type: recall_at_3
      value: 32.873000000000005
    - type: recall_at_5
      value: 38.632
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
      value: 22.528166666666667
    - type: map_at_10
      value: 30.317833333333333
    - type: map_at_100
      value: 31.44108333333333
    - type: map_at_1000
      value: 31.566666666666666
    - type: map_at_3
      value: 27.84425
    - type: map_at_5
      value: 29.233333333333334
    - type: mrr_at_1
      value: 26.75733333333333
    - type: mrr_at_10
      value: 34.24425
    - type: mrr_at_100
      value: 35.11375
    - type: mrr_at_1000
      value: 35.184333333333335
    - type: mrr_at_3
      value: 32.01225
    - type: mrr_at_5
      value: 33.31225
    - type: ndcg_at_1
      value: 26.75733333333333
    - type: ndcg_at_10
      value: 35.072583333333334
    - type: ndcg_at_100
      value: 40.13358333333334
    - type: ndcg_at_1000
      value: 42.81825
    - type: ndcg_at_3
      value: 30.79275000000001
    - type: ndcg_at_5
      value: 32.822
    - type: precision_at_1
      value: 26.75733333333333
    - type: precision_at_10
      value: 6.128083333333334
    - type: precision_at_100
      value: 1.019
    - type: precision_at_1000
      value: 0.14391666666666664
    - type: precision_at_3
      value: 14.129916666666665
    - type: precision_at_5
      value: 10.087416666666668
    - type: recall_at_1
      value: 22.528166666666667
    - type: recall_at_10
      value: 45.38341666666667
    - type: recall_at_100
      value: 67.81791666666668
    - type: recall_at_1000
      value: 86.71716666666666
    - type: recall_at_3
      value: 33.38741666666667
    - type: recall_at_5
      value: 38.62041666666667
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
      value: 21.975
    - type: map_at_10
      value: 28.144999999999996
    - type: map_at_100
      value: 28.994999999999997
    - type: map_at_1000
      value: 29.086000000000002
    - type: map_at_3
      value: 25.968999999999998
    - type: map_at_5
      value: 27.321
    - type: mrr_at_1
      value: 25
    - type: mrr_at_10
      value: 30.822
    - type: mrr_at_100
      value: 31.647
    - type: mrr_at_1000
      value: 31.712
    - type: mrr_at_3
      value: 28.860000000000003
    - type: mrr_at_5
      value: 30.041
    - type: ndcg_at_1
      value: 25
    - type: ndcg_at_10
      value: 31.929999999999996
    - type: ndcg_at_100
      value: 36.258
    - type: ndcg_at_1000
      value: 38.682
    - type: ndcg_at_3
      value: 27.972
    - type: ndcg_at_5
      value: 30.089
    - type: precision_at_1
      value: 25
    - type: precision_at_10
      value: 4.923
    - type: precision_at_100
      value: 0.767
    - type: precision_at_1000
      value: 0.106
    - type: precision_at_3
      value: 11.860999999999999
    - type: precision_at_5
      value: 8.466
    - type: recall_at_1
      value: 21.975
    - type: recall_at_10
      value: 41.102
    - type: recall_at_100
      value: 60.866
    - type: recall_at_1000
      value: 78.781
    - type: recall_at_3
      value: 30.268
    - type: recall_at_5
      value: 35.552
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
      value: 15.845999999999998
    - type: map_at_10
      value: 21.861
    - type: map_at_100
      value: 22.798
    - type: map_at_1000
      value: 22.925
    - type: map_at_3
      value: 19.922
    - type: map_at_5
      value: 21.054000000000002
    - type: mrr_at_1
      value: 19.098000000000003
    - type: mrr_at_10
      value: 25.397
    - type: mrr_at_100
      value: 26.246000000000002
    - type: mrr_at_1000
      value: 26.33
    - type: mrr_at_3
      value: 23.469
    - type: mrr_at_5
      value: 24.646
    - type: ndcg_at_1
      value: 19.098000000000003
    - type: ndcg_at_10
      value: 25.807999999999996
    - type: ndcg_at_100
      value: 30.445
    - type: ndcg_at_1000
      value: 33.666000000000004
    - type: ndcg_at_3
      value: 22.292
    - type: ndcg_at_5
      value: 24.075
    - type: precision_at_1
      value: 19.098000000000003
    - type: precision_at_10
      value: 4.58
    - type: precision_at_100
      value: 0.8099999999999999
    - type: precision_at_1000
      value: 0.126
    - type: precision_at_3
      value: 10.346
    - type: precision_at_5
      value: 7.542999999999999
    - type: recall_at_1
      value: 15.845999999999998
    - type: recall_at_10
      value: 34.172999999999995
    - type: recall_at_100
      value: 55.24099999999999
    - type: recall_at_1000
      value: 78.644
    - type: recall_at_3
      value: 24.401
    - type: recall_at_5
      value: 28.938000000000002
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
      value: 22.974
    - type: map_at_10
      value: 30.108
    - type: map_at_100
      value: 31.208000000000002
    - type: map_at_1000
      value: 31.330999999999996
    - type: map_at_3
      value: 27.889999999999997
    - type: map_at_5
      value: 29.023
    - type: mrr_at_1
      value: 26.493
    - type: mrr_at_10
      value: 33.726
    - type: mrr_at_100
      value: 34.622
    - type: mrr_at_1000
      value: 34.703
    - type: mrr_at_3
      value: 31.575999999999997
    - type: mrr_at_5
      value: 32.690999999999995
    - type: ndcg_at_1
      value: 26.493
    - type: ndcg_at_10
      value: 34.664
    - type: ndcg_at_100
      value: 39.725
    - type: ndcg_at_1000
      value: 42.648
    - type: ndcg_at_3
      value: 30.447999999999997
    - type: ndcg_at_5
      value: 32.145
    - type: precision_at_1
      value: 26.493
    - type: precision_at_10
      value: 5.7090000000000005
    - type: precision_at_100
      value: 0.9199999999999999
    - type: precision_at_1000
      value: 0.129
    - type: precision_at_3
      value: 13.464
    - type: precision_at_5
      value: 9.384
    - type: recall_at_1
      value: 22.974
    - type: recall_at_10
      value: 45.097
    - type: recall_at_100
      value: 66.908
    - type: recall_at_1000
      value: 87.495
    - type: recall_at_3
      value: 33.338
    - type: recall_at_5
      value: 37.499
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
      value: 22.408
    - type: map_at_10
      value: 29.580000000000002
    - type: map_at_100
      value: 31.145
    - type: map_at_1000
      value: 31.369000000000003
    - type: map_at_3
      value: 27.634999999999998
    - type: map_at_5
      value: 28.766000000000002
    - type: mrr_at_1
      value: 27.272999999999996
    - type: mrr_at_10
      value: 33.93
    - type: mrr_at_100
      value: 34.963
    - type: mrr_at_1000
      value: 35.031
    - type: mrr_at_3
      value: 32.016
    - type: mrr_at_5
      value: 33.221000000000004
    - type: ndcg_at_1
      value: 27.272999999999996
    - type: ndcg_at_10
      value: 33.993
    - type: ndcg_at_100
      value: 40.333999999999996
    - type: ndcg_at_1000
      value: 43.361
    - type: ndcg_at_3
      value: 30.918
    - type: ndcg_at_5
      value: 32.552
    - type: precision_at_1
      value: 27.272999999999996
    - type: precision_at_10
      value: 6.285
    - type: precision_at_100
      value: 1.389
    - type: precision_at_1000
      value: 0.232
    - type: precision_at_3
      value: 14.427000000000001
    - type: precision_at_5
      value: 10.356
    - type: recall_at_1
      value: 22.408
    - type: recall_at_10
      value: 41.318
    - type: recall_at_100
      value: 70.539
    - type: recall_at_1000
      value: 90.197
    - type: recall_at_3
      value: 32.513
    - type: recall_at_5
      value: 37
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
      value: 17.258000000000003
    - type: map_at_10
      value: 24.294
    - type: map_at_100
      value: 25.305
    - type: map_at_1000
      value: 25.419999999999998
    - type: map_at_3
      value: 22.326999999999998
    - type: map_at_5
      value: 23.31
    - type: mrr_at_1
      value: 18.484
    - type: mrr_at_10
      value: 25.863999999999997
    - type: mrr_at_100
      value: 26.766000000000002
    - type: mrr_at_1000
      value: 26.855
    - type: mrr_at_3
      value: 23.968
    - type: mrr_at_5
      value: 24.911
    - type: ndcg_at_1
      value: 18.484
    - type: ndcg_at_10
      value: 28.433000000000003
    - type: ndcg_at_100
      value: 33.405
    - type: ndcg_at_1000
      value: 36.375
    - type: ndcg_at_3
      value: 24.455
    - type: ndcg_at_5
      value: 26.031
    - type: precision_at_1
      value: 18.484
    - type: precision_at_10
      value: 4.603
    - type: precision_at_100
      value: 0.773
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 10.659
    - type: precision_at_5
      value: 7.505000000000001
    - type: recall_at_1
      value: 17.258000000000003
    - type: recall_at_10
      value: 39.589999999999996
    - type: recall_at_100
      value: 62.592000000000006
    - type: recall_at_1000
      value: 84.917
    - type: recall_at_3
      value: 28.706
    - type: recall_at_5
      value: 32.224000000000004
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
      value: 10.578999999999999
    - type: map_at_10
      value: 17.642
    - type: map_at_100
      value: 19.451
    - type: map_at_1000
      value: 19.647000000000002
    - type: map_at_3
      value: 14.618
    - type: map_at_5
      value: 16.145
    - type: mrr_at_1
      value: 23.322000000000003
    - type: mrr_at_10
      value: 34.204
    - type: mrr_at_100
      value: 35.185
    - type: mrr_at_1000
      value: 35.235
    - type: mrr_at_3
      value: 30.847
    - type: mrr_at_5
      value: 32.824
    - type: ndcg_at_1
      value: 23.322000000000003
    - type: ndcg_at_10
      value: 25.352999999999998
    - type: ndcg_at_100
      value: 32.574
    - type: ndcg_at_1000
      value: 36.073
    - type: ndcg_at_3
      value: 20.318
    - type: ndcg_at_5
      value: 22.111
    - type: precision_at_1
      value: 23.322000000000003
    - type: precision_at_10
      value: 8.02
    - type: precision_at_100
      value: 1.5730000000000002
    - type: precision_at_1000
      value: 0.22200000000000003
    - type: precision_at_3
      value: 15.049000000000001
    - type: precision_at_5
      value: 11.87
    - type: recall_at_1
      value: 10.578999999999999
    - type: recall_at_10
      value: 30.964999999999996
    - type: recall_at_100
      value: 55.986000000000004
    - type: recall_at_1000
      value: 75.565
    - type: recall_at_3
      value: 18.686
    - type: recall_at_5
      value: 23.629
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
      value: 7.327
    - type: map_at_10
      value: 14.904
    - type: map_at_100
      value: 20.29
    - type: map_at_1000
      value: 21.42
    - type: map_at_3
      value: 10.911
    - type: map_at_5
      value: 12.791
    - type: mrr_at_1
      value: 57.25
    - type: mrr_at_10
      value: 66.62700000000001
    - type: mrr_at_100
      value: 67.035
    - type: mrr_at_1000
      value: 67.052
    - type: mrr_at_3
      value: 64.833
    - type: mrr_at_5
      value: 65.908
    - type: ndcg_at_1
      value: 43.75
    - type: ndcg_at_10
      value: 32.246
    - type: ndcg_at_100
      value: 35.774
    - type: ndcg_at_1000
      value: 42.872
    - type: ndcg_at_3
      value: 36.64
    - type: ndcg_at_5
      value: 34.487
    - type: precision_at_1
      value: 57.25
    - type: precision_at_10
      value: 25.924999999999997
    - type: precision_at_100
      value: 7.670000000000001
    - type: precision_at_1000
      value: 1.599
    - type: precision_at_3
      value: 41.167
    - type: precision_at_5
      value: 34.65
    - type: recall_at_1
      value: 7.327
    - type: recall_at_10
      value: 19.625
    - type: recall_at_100
      value: 41.601
    - type: recall_at_1000
      value: 65.117
    - type: recall_at_3
      value: 12.308
    - type: recall_at_5
      value: 15.437999999999999
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
      value: 44.53
    - type: f1
      value: 39.39884255816736
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
      value: 58.913000000000004
    - type: map_at_10
      value: 69.592
    - type: map_at_100
      value: 69.95599999999999
    - type: map_at_1000
      value: 69.973
    - type: map_at_3
      value: 67.716
    - type: map_at_5
      value: 68.899
    - type: mrr_at_1
      value: 63.561
    - type: mrr_at_10
      value: 74.2
    - type: mrr_at_100
      value: 74.468
    - type: mrr_at_1000
      value: 74.47500000000001
    - type: mrr_at_3
      value: 72.442
    - type: mrr_at_5
      value: 73.58
    - type: ndcg_at_1
      value: 63.561
    - type: ndcg_at_10
      value: 74.988
    - type: ndcg_at_100
      value: 76.52799999999999
    - type: ndcg_at_1000
      value: 76.88000000000001
    - type: ndcg_at_3
      value: 71.455
    - type: ndcg_at_5
      value: 73.42699999999999
    - type: precision_at_1
      value: 63.561
    - type: precision_at_10
      value: 9.547
    - type: precision_at_100
      value: 1.044
    - type: precision_at_1000
      value: 0.109
    - type: precision_at_3
      value: 28.143
    - type: precision_at_5
      value: 18.008
    - type: recall_at_1
      value: 58.913000000000004
    - type: recall_at_10
      value: 87.18
    - type: recall_at_100
      value: 93.852
    - type: recall_at_1000
      value: 96.256
    - type: recall_at_3
      value: 77.55199999999999
    - type: recall_at_5
      value: 82.42399999999999
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
      value: 11.761000000000001
    - type: map_at_10
      value: 19.564999999999998
    - type: map_at_100
      value: 21.099
    - type: map_at_1000
      value: 21.288999999999998
    - type: map_at_3
      value: 16.683999999999997
    - type: map_at_5
      value: 18.307000000000002
    - type: mrr_at_1
      value: 23.302
    - type: mrr_at_10
      value: 30.979
    - type: mrr_at_100
      value: 32.121
    - type: mrr_at_1000
      value: 32.186
    - type: mrr_at_3
      value: 28.549000000000003
    - type: mrr_at_5
      value: 30.038999999999998
    - type: ndcg_at_1
      value: 23.302
    - type: ndcg_at_10
      value: 25.592
    - type: ndcg_at_100
      value: 32.416
    - type: ndcg_at_1000
      value: 36.277
    - type: ndcg_at_3
      value: 22.151
    - type: ndcg_at_5
      value: 23.483999999999998
    - type: precision_at_1
      value: 23.302
    - type: precision_at_10
      value: 7.377000000000001
    - type: precision_at_100
      value: 1.415
    - type: precision_at_1000
      value: 0.212
    - type: precision_at_3
      value: 14.712
    - type: precision_at_5
      value: 11.358
    - type: recall_at_1
      value: 11.761000000000001
    - type: recall_at_10
      value: 31.696
    - type: recall_at_100
      value: 58.01500000000001
    - type: recall_at_1000
      value: 81.572
    - type: recall_at_3
      value: 20.742
    - type: recall_at_5
      value: 25.707
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
      value: 32.275
    - type: map_at_10
      value: 44.712
    - type: map_at_100
      value: 45.621
    - type: map_at_1000
      value: 45.698
    - type: map_at_3
      value: 42.016999999999996
    - type: map_at_5
      value: 43.659
    - type: mrr_at_1
      value: 64.551
    - type: mrr_at_10
      value: 71.58099999999999
    - type: mrr_at_100
      value: 71.952
    - type: mrr_at_1000
      value: 71.96900000000001
    - type: mrr_at_3
      value: 70.236
    - type: mrr_at_5
      value: 71.051
    - type: ndcg_at_1
      value: 64.551
    - type: ndcg_at_10
      value: 53.913999999999994
    - type: ndcg_at_100
      value: 57.421
    - type: ndcg_at_1000
      value: 59.06
    - type: ndcg_at_3
      value: 49.716
    - type: ndcg_at_5
      value: 51.971999999999994
    - type: precision_at_1
      value: 64.551
    - type: precision_at_10
      value: 11.110000000000001
    - type: precision_at_100
      value: 1.388
    - type: precision_at_1000
      value: 0.161
    - type: precision_at_3
      value: 30.822
    - type: precision_at_5
      value: 20.273
    - type: recall_at_1
      value: 32.275
    - type: recall_at_10
      value: 55.55
    - type: recall_at_100
      value: 69.38600000000001
    - type: recall_at_1000
      value: 80.35799999999999
    - type: recall_at_3
      value: 46.232
    - type: recall_at_5
      value: 50.682
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
      value: 76.4604
    - type: ap
      value: 70.40498168422701
    - type: f1
      value: 76.38572688476046
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
      value: 15.065999999999999
    - type: map_at_10
      value: 25.058000000000003
    - type: map_at_100
      value: 26.268
    - type: map_at_1000
      value: 26.344
    - type: map_at_3
      value: 21.626
    - type: map_at_5
      value: 23.513
    - type: mrr_at_1
      value: 15.501000000000001
    - type: mrr_at_10
      value: 25.548
    - type: mrr_at_100
      value: 26.723000000000003
    - type: mrr_at_1000
      value: 26.793
    - type: mrr_at_3
      value: 22.142
    - type: mrr_at_5
      value: 24.024
    - type: ndcg_at_1
      value: 15.501000000000001
    - type: ndcg_at_10
      value: 31.008000000000003
    - type: ndcg_at_100
      value: 37.08
    - type: ndcg_at_1000
      value: 39.102
    - type: ndcg_at_3
      value: 23.921999999999997
    - type: ndcg_at_5
      value: 27.307
    - type: precision_at_1
      value: 15.501000000000001
    - type: precision_at_10
      value: 5.155
    - type: precision_at_100
      value: 0.822
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_3
      value: 10.363
    - type: precision_at_5
      value: 7.917000000000001
    - type: recall_at_1
      value: 15.065999999999999
    - type: recall_at_10
      value: 49.507
    - type: recall_at_100
      value: 78.118
    - type: recall_at_1000
      value: 93.881
    - type: recall_at_3
      value: 30.075000000000003
    - type: recall_at_5
      value: 38.222
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
      value: 90.6703146374829
    - type: f1
      value: 90.1258004293966
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
      value: 68.29229366165072
    - type: f1
      value: 50.016194478997875
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
      value: 68.57767316745124
    - type: f1
      value: 67.16194062146954
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
      value: 73.92064559515804
    - type: f1
      value: 73.6680729569968
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
      value: 31.56335607367883
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
      value: 28.131807833734268
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
      value: 31.07390328719844
    - type: mrr
      value: 32.117370992867905
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
      value: 5.274
    - type: map_at_10
      value: 11.489
    - type: map_at_100
      value: 14.518
    - type: map_at_1000
      value: 15.914
    - type: map_at_3
      value: 8.399
    - type: map_at_5
      value: 9.889000000000001
    - type: mrr_at_1
      value: 42.724000000000004
    - type: mrr_at_10
      value: 51.486
    - type: mrr_at_100
      value: 51.941
    - type: mrr_at_1000
      value: 51.99
    - type: mrr_at_3
      value: 49.278
    - type: mrr_at_5
      value: 50.485
    - type: ndcg_at_1
      value: 39.938
    - type: ndcg_at_10
      value: 31.862000000000002
    - type: ndcg_at_100
      value: 29.235
    - type: ndcg_at_1000
      value: 37.802
    - type: ndcg_at_3
      value: 35.754999999999995
    - type: ndcg_at_5
      value: 34.447
    - type: precision_at_1
      value: 42.105
    - type: precision_at_10
      value: 23.901
    - type: precision_at_100
      value: 7.715
    - type: precision_at_1000
      value: 2.045
    - type: precision_at_3
      value: 33.437
    - type: precision_at_5
      value: 29.782999999999998
    - type: recall_at_1
      value: 5.274
    - type: recall_at_10
      value: 15.351
    - type: recall_at_100
      value: 29.791
    - type: recall_at_1000
      value: 60.722
    - type: recall_at_3
      value: 9.411
    - type: recall_at_5
      value: 12.171999999999999
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
      value: 16.099
    - type: map_at_10
      value: 27.913
    - type: map_at_100
      value: 29.281000000000002
    - type: map_at_1000
      value: 29.343999999999998
    - type: map_at_3
      value: 23.791
    - type: map_at_5
      value: 26.049
    - type: mrr_at_1
      value: 18.337
    - type: mrr_at_10
      value: 29.953999999999997
    - type: mrr_at_100
      value: 31.080999999999996
    - type: mrr_at_1000
      value: 31.130000000000003
    - type: mrr_at_3
      value: 26.168000000000003
    - type: mrr_at_5
      value: 28.277
    - type: ndcg_at_1
      value: 18.308
    - type: ndcg_at_10
      value: 34.938
    - type: ndcg_at_100
      value: 41.125
    - type: ndcg_at_1000
      value: 42.708
    - type: ndcg_at_3
      value: 26.805
    - type: ndcg_at_5
      value: 30.686999999999998
    - type: precision_at_1
      value: 18.308
    - type: precision_at_10
      value: 6.476999999999999
    - type: precision_at_100
      value: 0.9939999999999999
    - type: precision_at_1000
      value: 0.11399999999999999
    - type: precision_at_3
      value: 12.784999999999998
    - type: precision_at_5
      value: 9.878
    - type: recall_at_1
      value: 16.099
    - type: recall_at_10
      value: 54.63
    - type: recall_at_100
      value: 82.24900000000001
    - type: recall_at_1000
      value: 94.242
    - type: recall_at_3
      value: 33.174
    - type: recall_at_5
      value: 42.164
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
      value: 67.947
    - type: map_at_10
      value: 81.499
    - type: map_at_100
      value: 82.17
    - type: map_at_1000
      value: 82.194
    - type: map_at_3
      value: 78.567
    - type: map_at_5
      value: 80.34400000000001
    - type: mrr_at_1
      value: 78.18
    - type: mrr_at_10
      value: 85.05
    - type: mrr_at_100
      value: 85.179
    - type: mrr_at_1000
      value: 85.181
    - type: mrr_at_3
      value: 83.91
    - type: mrr_at_5
      value: 84.638
    - type: ndcg_at_1
      value: 78.2
    - type: ndcg_at_10
      value: 85.715
    - type: ndcg_at_100
      value: 87.2
    - type: ndcg_at_1000
      value: 87.39
    - type: ndcg_at_3
      value: 82.572
    - type: ndcg_at_5
      value: 84.176
    - type: precision_at_1
      value: 78.2
    - type: precision_at_10
      value: 12.973
    - type: precision_at_100
      value: 1.5010000000000001
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 35.949999999999996
    - type: precision_at_5
      value: 23.62
    - type: recall_at_1
      value: 67.947
    - type: recall_at_10
      value: 93.804
    - type: recall_at_100
      value: 98.971
    - type: recall_at_1000
      value: 99.91600000000001
    - type: recall_at_3
      value: 84.75399999999999
    - type: recall_at_5
      value: 89.32
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
      value: 45.457201684255104
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
      value: 55.162226937477875
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
      value: 4.173
    - type: map_at_10
      value: 10.463000000000001
    - type: map_at_100
      value: 12.278
    - type: map_at_1000
      value: 12.572
    - type: map_at_3
      value: 7.528
    - type: map_at_5
      value: 8.863
    - type: mrr_at_1
      value: 20.599999999999998
    - type: mrr_at_10
      value: 30.422
    - type: mrr_at_100
      value: 31.6
    - type: mrr_at_1000
      value: 31.663000000000004
    - type: mrr_at_3
      value: 27.400000000000002
    - type: mrr_at_5
      value: 29.065
    - type: ndcg_at_1
      value: 20.599999999999998
    - type: ndcg_at_10
      value: 17.687
    - type: ndcg_at_100
      value: 25.172
    - type: ndcg_at_1000
      value: 30.617
    - type: ndcg_at_3
      value: 16.81
    - type: ndcg_at_5
      value: 14.499
    - type: precision_at_1
      value: 20.599999999999998
    - type: precision_at_10
      value: 9.17
    - type: precision_at_100
      value: 2.004
    - type: precision_at_1000
      value: 0.332
    - type: precision_at_3
      value: 15.6
    - type: precision_at_5
      value: 12.58
    - type: recall_at_1
      value: 4.173
    - type: recall_at_10
      value: 18.575
    - type: recall_at_100
      value: 40.692
    - type: recall_at_1000
      value: 67.467
    - type: recall_at_3
      value: 9.488000000000001
    - type: recall_at_5
      value: 12.738
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
      value: 81.12603499315416
    - type: cos_sim_spearman
      value: 73.62060290948378
    - type: euclidean_pearson
      value: 78.14083565781135
    - type: euclidean_spearman
      value: 73.16840437541543
    - type: manhattan_pearson
      value: 77.92017261109734
    - type: manhattan_spearman
      value: 72.8805059949965
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
      value: 79.75955377133172
    - type: cos_sim_spearman
      value: 71.8872633964069
    - type: euclidean_pearson
      value: 76.31922068538256
    - type: euclidean_spearman
      value: 70.86449661855376
    - type: manhattan_pearson
      value: 76.47852229730407
    - type: manhattan_spearman
      value: 70.99367421984789
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
      value: 78.80762722908158
    - type: cos_sim_spearman
      value: 79.84588978756372
    - type: euclidean_pearson
      value: 79.8216849781164
    - type: euclidean_spearman
      value: 80.22647061695481
    - type: manhattan_pearson
      value: 79.56604194112572
    - type: manhattan_spearman
      value: 79.96495189862462
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
      value: 80.1012718092742
    - type: cos_sim_spearman
      value: 76.86011381793661
    - type: euclidean_pearson
      value: 79.94426039862019
    - type: euclidean_spearman
      value: 77.36751135465131
    - type: manhattan_pearson
      value: 79.87959373304288
    - type: manhattan_spearman
      value: 77.37717129004746
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
      value: 83.90618420346104
    - type: cos_sim_spearman
      value: 84.77290791243722
    - type: euclidean_pearson
      value: 84.64732258073293
    - type: euclidean_spearman
      value: 85.21053649543357
    - type: manhattan_pearson
      value: 84.61616883522647
    - type: manhattan_spearman
      value: 85.19803126766931
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
      value: 80.52192114059063
    - type: cos_sim_spearman
      value: 81.9103244827937
    - type: euclidean_pearson
      value: 80.99375176138985
    - type: euclidean_spearman
      value: 81.540250641079
    - type: manhattan_pearson
      value: 80.84979573396426
    - type: manhattan_spearman
      value: 81.3742591621492
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
      value: 85.82166001234197
    - type: cos_sim_spearman
      value: 86.81857495659123
    - type: euclidean_pearson
      value: 85.72798403202849
    - type: euclidean_spearman
      value: 85.70482438950965
    - type: manhattan_pearson
      value: 85.51579093130357
    - type: manhattan_spearman
      value: 85.41233705379751
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
      value: 64.48071151079803
    - type: cos_sim_spearman
      value: 65.37838108084044
    - type: euclidean_pearson
      value: 64.67378947096257
    - type: euclidean_spearman
      value: 65.39187147219869
    - type: manhattan_pearson
      value: 65.35487466133208
    - type: manhattan_spearman
      value: 65.51328499442272
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
      value: 82.64702367823314
    - type: cos_sim_spearman
      value: 82.49732953181818
    - type: euclidean_pearson
      value: 83.05996062475664
    - type: euclidean_spearman
      value: 82.28159546751176
    - type: manhattan_pearson
      value: 82.98305503664952
    - type: manhattan_spearman
      value: 82.18405771943928
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
      value: 78.5744649318696
    - type: mrr
      value: 93.35386291268645
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
      value: 52.093999999999994
    - type: map_at_10
      value: 61.646
    - type: map_at_100
      value: 62.197
    - type: map_at_1000
      value: 62.22800000000001
    - type: map_at_3
      value: 58.411
    - type: map_at_5
      value: 60.585
    - type: mrr_at_1
      value: 55.00000000000001
    - type: mrr_at_10
      value: 62.690999999999995
    - type: mrr_at_100
      value: 63.139
    - type: mrr_at_1000
      value: 63.166999999999994
    - type: mrr_at_3
      value: 60.111000000000004
    - type: mrr_at_5
      value: 61.778
    - type: ndcg_at_1
      value: 55.00000000000001
    - type: ndcg_at_10
      value: 66.271
    - type: ndcg_at_100
      value: 68.879
    - type: ndcg_at_1000
      value: 69.722
    - type: ndcg_at_3
      value: 60.672000000000004
    - type: ndcg_at_5
      value: 63.929
    - type: precision_at_1
      value: 55.00000000000001
    - type: precision_at_10
      value: 9
    - type: precision_at_100
      value: 1.043
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: precision_at_3
      value: 23.555999999999997
    - type: precision_at_5
      value: 16.2
    - type: recall_at_1
      value: 52.093999999999994
    - type: recall_at_10
      value: 79.567
    - type: recall_at_100
      value: 91.60000000000001
    - type: recall_at_1000
      value: 98.333
    - type: recall_at_3
      value: 64.633
    - type: recall_at_5
      value: 72.68299999999999
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
      value: 99.83267326732673
    - type: cos_sim_ap
      value: 95.77995366495178
    - type: cos_sim_f1
      value: 91.51180311401306
    - type: cos_sim_precision
      value: 91.92734611503532
    - type: cos_sim_recall
      value: 91.10000000000001
    - type: dot_accuracy
      value: 99.63366336633663
    - type: dot_ap
      value: 88.53996286967461
    - type: dot_f1
      value: 81.06537530266343
    - type: dot_precision
      value: 78.59154929577464
    - type: dot_recall
      value: 83.7
    - type: euclidean_accuracy
      value: 99.82376237623762
    - type: euclidean_ap
      value: 95.53192209281187
    - type: euclidean_f1
      value: 91.19683481701286
    - type: euclidean_precision
      value: 90.21526418786692
    - type: euclidean_recall
      value: 92.2
    - type: manhattan_accuracy
      value: 99.82376237623762
    - type: manhattan_ap
      value: 95.55642082191741
    - type: manhattan_f1
      value: 91.16186693147964
    - type: manhattan_precision
      value: 90.53254437869822
    - type: manhattan_recall
      value: 91.8
    - type: max_accuracy
      value: 99.83267326732673
    - type: max_ap
      value: 95.77995366495178
    - type: max_f1
      value: 91.51180311401306
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
      value: 54.508462134213474
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
      value: 34.06549765184959
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
      value: 49.43129549466616
    - type: mrr
      value: 50.20613169510227
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
      value: 30.069516173193044
    - type: cos_sim_spearman
      value: 29.872498354017353
    - type: dot_pearson
      value: 28.80761257516063
    - type: dot_spearman
      value: 28.397422678527708
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
      value: 0.169
    - type: map_at_10
      value: 1.208
    - type: map_at_100
      value: 5.925
    - type: map_at_1000
      value: 14.427000000000001
    - type: map_at_3
      value: 0.457
    - type: map_at_5
      value: 0.716
    - type: mrr_at_1
      value: 64
    - type: mrr_at_10
      value: 74.075
    - type: mrr_at_100
      value: 74.303
    - type: mrr_at_1000
      value: 74.303
    - type: mrr_at_3
      value: 71
    - type: mrr_at_5
      value: 72.89999999999999
    - type: ndcg_at_1
      value: 57.99999999999999
    - type: ndcg_at_10
      value: 50.376
    - type: ndcg_at_100
      value: 38.582
    - type: ndcg_at_1000
      value: 35.663
    - type: ndcg_at_3
      value: 55.592
    - type: ndcg_at_5
      value: 53.647999999999996
    - type: precision_at_1
      value: 64
    - type: precision_at_10
      value: 53.2
    - type: precision_at_100
      value: 39.6
    - type: precision_at_1000
      value: 16.218
    - type: precision_at_3
      value: 59.333000000000006
    - type: precision_at_5
      value: 57.599999999999994
    - type: recall_at_1
      value: 0.169
    - type: recall_at_10
      value: 1.423
    - type: recall_at_100
      value: 9.049999999999999
    - type: recall_at_1000
      value: 34.056999999999995
    - type: recall_at_3
      value: 0.48700000000000004
    - type: recall_at_5
      value: 0.792
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
      value: 1.319
    - type: map_at_10
      value: 7.112
    - type: map_at_100
      value: 12.588
    - type: map_at_1000
      value: 14.056
    - type: map_at_3
      value: 2.8049999999999997
    - type: map_at_5
      value: 4.68
    - type: mrr_at_1
      value: 18.367
    - type: mrr_at_10
      value: 33.94
    - type: mrr_at_100
      value: 35.193000000000005
    - type: mrr_at_1000
      value: 35.193000000000005
    - type: mrr_at_3
      value: 29.932
    - type: mrr_at_5
      value: 32.279
    - type: ndcg_at_1
      value: 15.306000000000001
    - type: ndcg_at_10
      value: 18.096
    - type: ndcg_at_100
      value: 30.512
    - type: ndcg_at_1000
      value: 42.148
    - type: ndcg_at_3
      value: 17.034
    - type: ndcg_at_5
      value: 18.509
    - type: precision_at_1
      value: 18.367
    - type: precision_at_10
      value: 18.776
    - type: precision_at_100
      value: 7.02
    - type: precision_at_1000
      value: 1.467
    - type: precision_at_3
      value: 19.048000000000002
    - type: precision_at_5
      value: 22.041
    - type: recall_at_1
      value: 1.319
    - type: recall_at_10
      value: 13.748
    - type: recall_at_100
      value: 43.972
    - type: recall_at_1000
      value: 79.557
    - type: recall_at_3
      value: 4.042
    - type: recall_at_5
      value: 7.742
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
      value: 70.2282
    - type: ap
      value: 13.995763859570426
    - type: f1
      value: 54.08126256731344
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
      value: 57.64006791171477
    - type: f1
      value: 57.95841320748957
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
      value: 40.19267841788564
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
      value: 83.96614412588663
    - type: cos_sim_ap
      value: 67.75985678572738
    - type: cos_sim_f1
      value: 64.04661542276222
    - type: cos_sim_precision
      value: 60.406922357343305
    - type: cos_sim_recall
      value: 68.15303430079156
    - type: dot_accuracy
      value: 79.5732252488526
    - type: dot_ap
      value: 51.30562107572645
    - type: dot_f1
      value: 53.120759837177744
    - type: dot_precision
      value: 46.478037198258804
    - type: dot_recall
      value: 61.97889182058047
    - type: euclidean_accuracy
      value: 84.00786791440663
    - type: euclidean_ap
      value: 67.58930214486998
    - type: euclidean_f1
      value: 64.424821579775
    - type: euclidean_precision
      value: 59.4817958454322
    - type: euclidean_recall
      value: 70.26385224274406
    - type: manhattan_accuracy
      value: 83.87673600762949
    - type: manhattan_ap
      value: 67.4250981523309
    - type: manhattan_f1
      value: 64.10286658015808
    - type: manhattan_precision
      value: 57.96885001066781
    - type: manhattan_recall
      value: 71.68865435356201
    - type: max_accuracy
      value: 84.00786791440663
    - type: max_ap
      value: 67.75985678572738
    - type: max_f1
      value: 64.424821579775
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
      value: 88.41347459929368
    - type: cos_sim_ap
      value: 84.89261930113058
    - type: cos_sim_f1
      value: 77.13677607258877
    - type: cos_sim_precision
      value: 74.88581164358733
    - type: cos_sim_recall
      value: 79.52725592854944
    - type: dot_accuracy
      value: 86.32359219156285
    - type: dot_ap
      value: 79.29794992131094
    - type: dot_f1
      value: 72.84356337679777
    - type: dot_precision
      value: 67.31761478675462
    - type: dot_recall
      value: 79.35786880197105
    - type: euclidean_accuracy
      value: 88.33585593976791
    - type: euclidean_ap
      value: 84.73257641312746
    - type: euclidean_f1
      value: 76.83529582788195
    - type: euclidean_precision
      value: 72.76294052863436
    - type: euclidean_recall
      value: 81.3905143209116
    - type: manhattan_accuracy
      value: 88.3086894089339
    - type: manhattan_ap
      value: 84.66304891729399
    - type: manhattan_f1
      value: 76.8181650632165
    - type: manhattan_precision
      value: 73.6864436744219
    - type: manhattan_recall
      value: 80.22790267939637
    - type: max_accuracy
      value: 88.41347459929368
    - type: max_ap
      value: 84.89261930113058
    - type: max_f1
      value: 77.13677607258877
license: mit
---

# bge-micro-v2

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search.

Distilled in a 2-step training process (bge-micro was step 1) from `BAAI/bge-small-en-v1.5`.

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('{MODEL_NAME}')
embeddings = model.encode(sentences)
print(embeddings)
```



## Usage (HuggingFace Transformers)
Without [sentence-transformers](https://www.SBERT.net), you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.

```python
from transformers import AutoTokenizer, AutoModel
import torch


#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('{MODEL_NAME}')
model = AutoModel.from_pretrained('{MODEL_NAME}')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, mean pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)
```



## Evaluation Results

<!--- Describe how your model was evaluated -->

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name={MODEL_NAME})



## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->