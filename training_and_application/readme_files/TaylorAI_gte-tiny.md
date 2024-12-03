---
model-index:
- name: gte_tiny
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
      value: 71.76119402985076
    - type: ap
      value: 34.63659287952359
    - type: f1
      value: 65.88939512571113
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
      value: 86.61324999999998
    - type: ap
      value: 81.7476302802319
    - type: f1
      value: 86.5863470912001
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
      value: 42.61000000000001
    - type: f1
      value: 42.2217180000715
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
      value: 28.377999999999997
    - type: map_at_10
      value: 44.565
    - type: map_at_100
      value: 45.48
    - type: map_at_1000
      value: 45.487
    - type: map_at_3
      value: 39.841
    - type: map_at_5
      value: 42.284
    - type: mrr_at_1
      value: 29.445
    - type: mrr_at_10
      value: 44.956
    - type: mrr_at_100
      value: 45.877
    - type: mrr_at_1000
      value: 45.884
    - type: mrr_at_3
      value: 40.209
    - type: mrr_at_5
      value: 42.719
    - type: ndcg_at_1
      value: 28.377999999999997
    - type: ndcg_at_10
      value: 53.638
    - type: ndcg_at_100
      value: 57.354000000000006
    - type: ndcg_at_1000
      value: 57.513000000000005
    - type: ndcg_at_3
      value: 43.701
    - type: ndcg_at_5
      value: 48.114000000000004
    - type: precision_at_1
      value: 28.377999999999997
    - type: precision_at_10
      value: 8.272
    - type: precision_at_100
      value: 0.984
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 18.303
    - type: precision_at_5
      value: 13.129
    - type: recall_at_1
      value: 28.377999999999997
    - type: recall_at_10
      value: 82.717
    - type: recall_at_100
      value: 98.43499999999999
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 54.908
    - type: recall_at_5
      value: 65.647
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
      value: 46.637318326729876
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
      value: 36.01134479855804
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
      value: 59.82917555338909
    - type: mrr
      value: 74.7888361254012
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
      value: 87.1657730995964
    - type: cos_sim_spearman
      value: 86.62787748941281
    - type: euclidean_pearson
      value: 85.48127914481798
    - type: euclidean_spearman
      value: 86.48148861167424
    - type: manhattan_pearson
      value: 85.07496934780823
    - type: manhattan_spearman
      value: 86.39473964708843
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
      value: 81.73051948051948
    - type: f1
      value: 81.66368364988331
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
      value: 39.18623707448217
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
      value: 32.12697757150375
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
      value: 29.160000000000004
    - type: map_at_10
      value: 40.474
    - type: map_at_100
      value: 41.905
    - type: map_at_1000
      value: 42.041000000000004
    - type: map_at_3
      value: 37.147000000000006
    - type: map_at_5
      value: 38.873999999999995
    - type: mrr_at_1
      value: 36.91
    - type: mrr_at_10
      value: 46.495999999999995
    - type: mrr_at_100
      value: 47.288000000000004
    - type: mrr_at_1000
      value: 47.339999999999996
    - type: mrr_at_3
      value: 43.777
    - type: mrr_at_5
      value: 45.257999999999996
    - type: ndcg_at_1
      value: 36.91
    - type: ndcg_at_10
      value: 46.722
    - type: ndcg_at_100
      value: 51.969
    - type: ndcg_at_1000
      value: 54.232
    - type: ndcg_at_3
      value: 41.783
    - type: ndcg_at_5
      value: 43.797000000000004
    - type: precision_at_1
      value: 36.91
    - type: precision_at_10
      value: 9.013
    - type: precision_at_100
      value: 1.455
    - type: precision_at_1000
      value: 0.193
    - type: precision_at_3
      value: 20.124
    - type: precision_at_5
      value: 14.363000000000001
    - type: recall_at_1
      value: 29.160000000000004
    - type: recall_at_10
      value: 58.521
    - type: recall_at_100
      value: 80.323
    - type: recall_at_1000
      value: 95.13000000000001
    - type: recall_at_3
      value: 44.205
    - type: recall_at_5
      value: 49.97
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
      value: 27.750000000000004
    - type: map_at_10
      value: 36.39
    - type: map_at_100
      value: 37.5
    - type: map_at_1000
      value: 37.625
    - type: map_at_3
      value: 33.853
    - type: map_at_5
      value: 35.397
    - type: mrr_at_1
      value: 34.14
    - type: mrr_at_10
      value: 41.841
    - type: mrr_at_100
      value: 42.469
    - type: mrr_at_1000
      value: 42.521
    - type: mrr_at_3
      value: 39.724
    - type: mrr_at_5
      value: 40.955999999999996
    - type: ndcg_at_1
      value: 34.14
    - type: ndcg_at_10
      value: 41.409
    - type: ndcg_at_100
      value: 45.668
    - type: ndcg_at_1000
      value: 47.916
    - type: ndcg_at_3
      value: 37.836
    - type: ndcg_at_5
      value: 39.650999999999996
    - type: precision_at_1
      value: 34.14
    - type: precision_at_10
      value: 7.739
    - type: precision_at_100
      value: 1.2630000000000001
    - type: precision_at_1000
      value: 0.173
    - type: precision_at_3
      value: 18.217
    - type: precision_at_5
      value: 12.854
    - type: recall_at_1
      value: 27.750000000000004
    - type: recall_at_10
      value: 49.882
    - type: recall_at_100
      value: 68.556
    - type: recall_at_1000
      value: 83.186
    - type: recall_at_3
      value: 39.047
    - type: recall_at_5
      value: 44.458
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
      value: 36.879
    - type: map_at_10
      value: 48.878
    - type: map_at_100
      value: 49.918
    - type: map_at_1000
      value: 49.978
    - type: map_at_3
      value: 45.867999999999995
    - type: map_at_5
      value: 47.637
    - type: mrr_at_1
      value: 42.696
    - type: mrr_at_10
      value: 52.342
    - type: mrr_at_100
      value: 53.044000000000004
    - type: mrr_at_1000
      value: 53.077
    - type: mrr_at_3
      value: 50.01
    - type: mrr_at_5
      value: 51.437
    - type: ndcg_at_1
      value: 42.696
    - type: ndcg_at_10
      value: 54.469
    - type: ndcg_at_100
      value: 58.664
    - type: ndcg_at_1000
      value: 59.951
    - type: ndcg_at_3
      value: 49.419999999999995
    - type: ndcg_at_5
      value: 52.007000000000005
    - type: precision_at_1
      value: 42.696
    - type: precision_at_10
      value: 8.734
    - type: precision_at_100
      value: 1.1769999999999998
    - type: precision_at_1000
      value: 0.133
    - type: precision_at_3
      value: 22.027
    - type: precision_at_5
      value: 15.135000000000002
    - type: recall_at_1
      value: 36.879
    - type: recall_at_10
      value: 67.669
    - type: recall_at_100
      value: 85.822
    - type: recall_at_1000
      value: 95.092
    - type: recall_at_3
      value: 54.157999999999994
    - type: recall_at_5
      value: 60.436
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
      value: 22.942
    - type: map_at_10
      value: 31.741999999999997
    - type: map_at_100
      value: 32.721000000000004
    - type: map_at_1000
      value: 32.809
    - type: map_at_3
      value: 29.17
    - type: map_at_5
      value: 30.714000000000002
    - type: mrr_at_1
      value: 24.746000000000002
    - type: mrr_at_10
      value: 33.517
    - type: mrr_at_100
      value: 34.451
    - type: mrr_at_1000
      value: 34.522000000000006
    - type: mrr_at_3
      value: 31.148999999999997
    - type: mrr_at_5
      value: 32.606
    - type: ndcg_at_1
      value: 24.746000000000002
    - type: ndcg_at_10
      value: 36.553000000000004
    - type: ndcg_at_100
      value: 41.53
    - type: ndcg_at_1000
      value: 43.811
    - type: ndcg_at_3
      value: 31.674000000000003
    - type: ndcg_at_5
      value: 34.241
    - type: precision_at_1
      value: 24.746000000000002
    - type: precision_at_10
      value: 5.684
    - type: precision_at_100
      value: 0.859
    - type: precision_at_1000
      value: 0.109
    - type: precision_at_3
      value: 13.597000000000001
    - type: precision_at_5
      value: 9.672
    - type: recall_at_1
      value: 22.942
    - type: recall_at_10
      value: 49.58
    - type: recall_at_100
      value: 72.614
    - type: recall_at_1000
      value: 89.89200000000001
    - type: recall_at_3
      value: 36.552
    - type: recall_at_5
      value: 42.702
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
      value: 15.345
    - type: map_at_10
      value: 22.428
    - type: map_at_100
      value: 23.756
    - type: map_at_1000
      value: 23.872
    - type: map_at_3
      value: 20.212
    - type: map_at_5
      value: 21.291
    - type: mrr_at_1
      value: 19.279
    - type: mrr_at_10
      value: 27.1
    - type: mrr_at_100
      value: 28.211000000000002
    - type: mrr_at_1000
      value: 28.279
    - type: mrr_at_3
      value: 24.813
    - type: mrr_at_5
      value: 25.889
    - type: ndcg_at_1
      value: 19.279
    - type: ndcg_at_10
      value: 27.36
    - type: ndcg_at_100
      value: 33.499
    - type: ndcg_at_1000
      value: 36.452
    - type: ndcg_at_3
      value: 23.233999999999998
    - type: ndcg_at_5
      value: 24.806
    - type: precision_at_1
      value: 19.279
    - type: precision_at_10
      value: 5.149
    - type: precision_at_100
      value: 0.938
    - type: precision_at_1000
      value: 0.133
    - type: precision_at_3
      value: 11.360000000000001
    - type: precision_at_5
      value: 8.035
    - type: recall_at_1
      value: 15.345
    - type: recall_at_10
      value: 37.974999999999994
    - type: recall_at_100
      value: 64.472
    - type: recall_at_1000
      value: 85.97200000000001
    - type: recall_at_3
      value: 26.203
    - type: recall_at_5
      value: 30.485
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
      value: 26.362000000000002
    - type: map_at_10
      value: 36.406
    - type: map_at_100
      value: 37.726
    - type: map_at_1000
      value: 37.84
    - type: map_at_3
      value: 33.425
    - type: map_at_5
      value: 35.043
    - type: mrr_at_1
      value: 32.146
    - type: mrr_at_10
      value: 41.674
    - type: mrr_at_100
      value: 42.478
    - type: mrr_at_1000
      value: 42.524
    - type: mrr_at_3
      value: 38.948
    - type: mrr_at_5
      value: 40.415
    - type: ndcg_at_1
      value: 32.146
    - type: ndcg_at_10
      value: 42.374
    - type: ndcg_at_100
      value: 47.919
    - type: ndcg_at_1000
      value: 50.013
    - type: ndcg_at_3
      value: 37.29
    - type: ndcg_at_5
      value: 39.531
    - type: precision_at_1
      value: 32.146
    - type: precision_at_10
      value: 7.767
    - type: precision_at_100
      value: 1.236
    - type: precision_at_1000
      value: 0.16
    - type: precision_at_3
      value: 17.965999999999998
    - type: precision_at_5
      value: 12.742999999999999
    - type: recall_at_1
      value: 26.362000000000002
    - type: recall_at_10
      value: 54.98800000000001
    - type: recall_at_100
      value: 78.50200000000001
    - type: recall_at_1000
      value: 92.146
    - type: recall_at_3
      value: 40.486
    - type: recall_at_5
      value: 46.236
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
      value: 24.417
    - type: map_at_10
      value: 33.161
    - type: map_at_100
      value: 34.357
    - type: map_at_1000
      value: 34.473
    - type: map_at_3
      value: 30.245
    - type: map_at_5
      value: 31.541999999999998
    - type: mrr_at_1
      value: 29.909000000000002
    - type: mrr_at_10
      value: 38.211
    - type: mrr_at_100
      value: 39.056999999999995
    - type: mrr_at_1000
      value: 39.114
    - type: mrr_at_3
      value: 35.769
    - type: mrr_at_5
      value: 36.922
    - type: ndcg_at_1
      value: 29.909000000000002
    - type: ndcg_at_10
      value: 38.694
    - type: ndcg_at_100
      value: 44.057
    - type: ndcg_at_1000
      value: 46.6
    - type: ndcg_at_3
      value: 33.822
    - type: ndcg_at_5
      value: 35.454
    - type: precision_at_1
      value: 29.909000000000002
    - type: precision_at_10
      value: 7.180000000000001
    - type: precision_at_100
      value: 1.153
    - type: precision_at_1000
      value: 0.155
    - type: precision_at_3
      value: 16.134
    - type: precision_at_5
      value: 11.256
    - type: recall_at_1
      value: 24.417
    - type: recall_at_10
      value: 50.260000000000005
    - type: recall_at_100
      value: 73.55699999999999
    - type: recall_at_1000
      value: 91.216
    - type: recall_at_3
      value: 35.971
    - type: recall_at_5
      value: 40.793
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
      value: 24.266916666666663
    - type: map_at_10
      value: 32.75025
    - type: map_at_100
      value: 33.91341666666667
    - type: map_at_1000
      value: 34.031749999999995
    - type: map_at_3
      value: 30.166416666666674
    - type: map_at_5
      value: 31.577000000000005
    - type: mrr_at_1
      value: 28.828166666666664
    - type: mrr_at_10
      value: 36.80991666666667
    - type: mrr_at_100
      value: 37.67075
    - type: mrr_at_1000
      value: 37.733
    - type: mrr_at_3
      value: 34.513416666666664
    - type: mrr_at_5
      value: 35.788
    - type: ndcg_at_1
      value: 28.828166666666664
    - type: ndcg_at_10
      value: 37.796
    - type: ndcg_at_100
      value: 42.94783333333333
    - type: ndcg_at_1000
      value: 45.38908333333333
    - type: ndcg_at_3
      value: 33.374750000000006
    - type: ndcg_at_5
      value: 35.379666666666665
    - type: precision_at_1
      value: 28.828166666666664
    - type: precision_at_10
      value: 6.615749999999999
    - type: precision_at_100
      value: 1.0848333333333333
    - type: precision_at_1000
      value: 0.1484166666666667
    - type: precision_at_3
      value: 15.347833333333332
    - type: precision_at_5
      value: 10.848916666666666
    - type: recall_at_1
      value: 24.266916666666663
    - type: recall_at_10
      value: 48.73458333333333
    - type: recall_at_100
      value: 71.56341666666667
    - type: recall_at_1000
      value: 88.63091666666668
    - type: recall_at_3
      value: 36.31208333333333
    - type: recall_at_5
      value: 41.55633333333333
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
      value: 23.497
    - type: map_at_10
      value: 30.249
    - type: map_at_100
      value: 30.947000000000003
    - type: map_at_1000
      value: 31.049
    - type: map_at_3
      value: 28.188000000000002
    - type: map_at_5
      value: 29.332
    - type: mrr_at_1
      value: 26.687
    - type: mrr_at_10
      value: 33.182
    - type: mrr_at_100
      value: 33.794999999999995
    - type: mrr_at_1000
      value: 33.873
    - type: mrr_at_3
      value: 31.263
    - type: mrr_at_5
      value: 32.428000000000004
    - type: ndcg_at_1
      value: 26.687
    - type: ndcg_at_10
      value: 34.252
    - type: ndcg_at_100
      value: 38.083
    - type: ndcg_at_1000
      value: 40.682
    - type: ndcg_at_3
      value: 30.464999999999996
    - type: ndcg_at_5
      value: 32.282
    - type: precision_at_1
      value: 26.687
    - type: precision_at_10
      value: 5.2909999999999995
    - type: precision_at_100
      value: 0.788
    - type: precision_at_1000
      value: 0.109
    - type: precision_at_3
      value: 13.037
    - type: precision_at_5
      value: 9.049
    - type: recall_at_1
      value: 23.497
    - type: recall_at_10
      value: 43.813
    - type: recall_at_100
      value: 61.88399999999999
    - type: recall_at_1000
      value: 80.926
    - type: recall_at_3
      value: 33.332
    - type: recall_at_5
      value: 37.862
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
      value: 16.073
    - type: map_at_10
      value: 22.705000000000002
    - type: map_at_100
      value: 23.703
    - type: map_at_1000
      value: 23.833
    - type: map_at_3
      value: 20.593
    - type: map_at_5
      value: 21.7
    - type: mrr_at_1
      value: 19.683
    - type: mrr_at_10
      value: 26.39
    - type: mrr_at_100
      value: 27.264
    - type: mrr_at_1000
      value: 27.349
    - type: mrr_at_3
      value: 24.409
    - type: mrr_at_5
      value: 25.474000000000004
    - type: ndcg_at_1
      value: 19.683
    - type: ndcg_at_10
      value: 27.014
    - type: ndcg_at_100
      value: 31.948
    - type: ndcg_at_1000
      value: 35.125
    - type: ndcg_at_3
      value: 23.225
    - type: ndcg_at_5
      value: 24.866
    - type: precision_at_1
      value: 19.683
    - type: precision_at_10
      value: 4.948
    - type: precision_at_100
      value: 0.876
    - type: precision_at_1000
      value: 0.133
    - type: precision_at_3
      value: 10.943
    - type: precision_at_5
      value: 7.86
    - type: recall_at_1
      value: 16.073
    - type: recall_at_10
      value: 36.283
    - type: recall_at_100
      value: 58.745999999999995
    - type: recall_at_1000
      value: 81.711
    - type: recall_at_3
      value: 25.637
    - type: recall_at_5
      value: 29.919
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
      value: 25.776
    - type: map_at_10
      value: 33.317
    - type: map_at_100
      value: 34.437
    - type: map_at_1000
      value: 34.54
    - type: map_at_3
      value: 30.706
    - type: map_at_5
      value: 32.202999999999996
    - type: mrr_at_1
      value: 30.224
    - type: mrr_at_10
      value: 37.34
    - type: mrr_at_100
      value: 38.268
    - type: mrr_at_1000
      value: 38.335
    - type: mrr_at_3
      value: 35.075
    - type: mrr_at_5
      value: 36.348
    - type: ndcg_at_1
      value: 30.224
    - type: ndcg_at_10
      value: 38.083
    - type: ndcg_at_100
      value: 43.413000000000004
    - type: ndcg_at_1000
      value: 45.856
    - type: ndcg_at_3
      value: 33.437
    - type: ndcg_at_5
      value: 35.661
    - type: precision_at_1
      value: 30.224
    - type: precision_at_10
      value: 6.1850000000000005
    - type: precision_at_100
      value: 1.0030000000000001
    - type: precision_at_1000
      value: 0.132
    - type: precision_at_3
      value: 14.646
    - type: precision_at_5
      value: 10.428999999999998
    - type: recall_at_1
      value: 25.776
    - type: recall_at_10
      value: 48.787000000000006
    - type: recall_at_100
      value: 72.04899999999999
    - type: recall_at_1000
      value: 89.339
    - type: recall_at_3
      value: 36.192
    - type: recall_at_5
      value: 41.665
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
      value: 23.156
    - type: map_at_10
      value: 30.886000000000003
    - type: map_at_100
      value: 32.551
    - type: map_at_1000
      value: 32.769
    - type: map_at_3
      value: 28.584
    - type: map_at_5
      value: 29.959999999999997
    - type: mrr_at_1
      value: 28.260999999999996
    - type: mrr_at_10
      value: 35.555
    - type: mrr_at_100
      value: 36.687
    - type: mrr_at_1000
      value: 36.742999999999995
    - type: mrr_at_3
      value: 33.531
    - type: mrr_at_5
      value: 34.717
    - type: ndcg_at_1
      value: 28.260999999999996
    - type: ndcg_at_10
      value: 36.036
    - type: ndcg_at_100
      value: 42.675000000000004
    - type: ndcg_at_1000
      value: 45.303
    - type: ndcg_at_3
      value: 32.449
    - type: ndcg_at_5
      value: 34.293
    - type: precision_at_1
      value: 28.260999999999996
    - type: precision_at_10
      value: 6.837999999999999
    - type: precision_at_100
      value: 1.4569999999999999
    - type: precision_at_1000
      value: 0.23500000000000001
    - type: precision_at_3
      value: 15.217
    - type: precision_at_5
      value: 11.028
    - type: recall_at_1
      value: 23.156
    - type: recall_at_10
      value: 45.251999999999995
    - type: recall_at_100
      value: 75.339
    - type: recall_at_1000
      value: 91.56
    - type: recall_at_3
      value: 34.701
    - type: recall_at_5
      value: 39.922999999999995
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
      value: 19.846
    - type: map_at_10
      value: 26.367
    - type: map_at_100
      value: 27.439999999999998
    - type: map_at_1000
      value: 27.552
    - type: map_at_3
      value: 24.006
    - type: map_at_5
      value: 25.230999999999998
    - type: mrr_at_1
      value: 21.257
    - type: mrr_at_10
      value: 28.071
    - type: mrr_at_100
      value: 29.037000000000003
    - type: mrr_at_1000
      value: 29.119
    - type: mrr_at_3
      value: 25.692999999999998
    - type: mrr_at_5
      value: 27.006000000000004
    - type: ndcg_at_1
      value: 21.257
    - type: ndcg_at_10
      value: 30.586000000000002
    - type: ndcg_at_100
      value: 35.949
    - type: ndcg_at_1000
      value: 38.728
    - type: ndcg_at_3
      value: 25.862000000000002
    - type: ndcg_at_5
      value: 27.967
    - type: precision_at_1
      value: 21.257
    - type: precision_at_10
      value: 4.861
    - type: precision_at_100
      value: 0.8130000000000001
    - type: precision_at_1000
      value: 0.116
    - type: precision_at_3
      value: 10.906
    - type: precision_at_5
      value: 7.763000000000001
    - type: recall_at_1
      value: 19.846
    - type: recall_at_10
      value: 41.805
    - type: recall_at_100
      value: 66.89699999999999
    - type: recall_at_1000
      value: 87.401
    - type: recall_at_3
      value: 29.261
    - type: recall_at_5
      value: 34.227000000000004
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
      value: 10.333
    - type: map_at_10
      value: 17.14
    - type: map_at_100
      value: 18.878
    - type: map_at_1000
      value: 19.067
    - type: map_at_3
      value: 14.123
    - type: map_at_5
      value: 15.699
    - type: mrr_at_1
      value: 23.192
    - type: mrr_at_10
      value: 33.553
    - type: mrr_at_100
      value: 34.553
    - type: mrr_at_1000
      value: 34.603
    - type: mrr_at_3
      value: 29.848000000000003
    - type: mrr_at_5
      value: 32.18
    - type: ndcg_at_1
      value: 23.192
    - type: ndcg_at_10
      value: 24.707
    - type: ndcg_at_100
      value: 31.701
    - type: ndcg_at_1000
      value: 35.260999999999996
    - type: ndcg_at_3
      value: 19.492
    - type: ndcg_at_5
      value: 21.543
    - type: precision_at_1
      value: 23.192
    - type: precision_at_10
      value: 7.824000000000001
    - type: precision_at_100
      value: 1.52
    - type: precision_at_1000
      value: 0.218
    - type: precision_at_3
      value: 14.180000000000001
    - type: precision_at_5
      value: 11.530999999999999
    - type: recall_at_1
      value: 10.333
    - type: recall_at_10
      value: 30.142999999999997
    - type: recall_at_100
      value: 54.298
    - type: recall_at_1000
      value: 74.337
    - type: recall_at_3
      value: 17.602999999999998
    - type: recall_at_5
      value: 22.938
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
      value: 8.03
    - type: map_at_10
      value: 17.345
    - type: map_at_100
      value: 23.462
    - type: map_at_1000
      value: 24.77
    - type: map_at_3
      value: 12.714
    - type: map_at_5
      value: 14.722
    - type: mrr_at_1
      value: 61.0
    - type: mrr_at_10
      value: 69.245
    - type: mrr_at_100
      value: 69.715
    - type: mrr_at_1000
      value: 69.719
    - type: mrr_at_3
      value: 67.583
    - type: mrr_at_5
      value: 68.521
    - type: ndcg_at_1
      value: 47.625
    - type: ndcg_at_10
      value: 35.973
    - type: ndcg_at_100
      value: 39.875
    - type: ndcg_at_1000
      value: 46.922000000000004
    - type: ndcg_at_3
      value: 40.574
    - type: ndcg_at_5
      value: 38.18
    - type: precision_at_1
      value: 61.0
    - type: precision_at_10
      value: 29.049999999999997
    - type: precision_at_100
      value: 8.828
    - type: precision_at_1000
      value: 1.8290000000000002
    - type: precision_at_3
      value: 45.333
    - type: precision_at_5
      value: 37.9
    - type: recall_at_1
      value: 8.03
    - type: recall_at_10
      value: 22.334
    - type: recall_at_100
      value: 45.919
    - type: recall_at_1000
      value: 68.822
    - type: recall_at_3
      value: 14.038999999999998
    - type: recall_at_5
      value: 17.118
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
      value: 44.714999999999996
    - type: f1
      value: 39.83929362259356
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
      value: 52.242999999999995
    - type: map_at_10
      value: 64.087
    - type: map_at_100
      value: 64.549
    - type: map_at_1000
      value: 64.567
    - type: map_at_3
      value: 61.667
    - type: map_at_5
      value: 63.266
    - type: mrr_at_1
      value: 56.271
    - type: mrr_at_10
      value: 68.146
    - type: mrr_at_100
      value: 68.524
    - type: mrr_at_1000
      value: 68.53200000000001
    - type: mrr_at_3
      value: 65.869
    - type: mrr_at_5
      value: 67.37100000000001
    - type: ndcg_at_1
      value: 56.271
    - type: ndcg_at_10
      value: 70.109
    - type: ndcg_at_100
      value: 72.09
    - type: ndcg_at_1000
      value: 72.479
    - type: ndcg_at_3
      value: 65.559
    - type: ndcg_at_5
      value: 68.242
    - type: precision_at_1
      value: 56.271
    - type: precision_at_10
      value: 9.286999999999999
    - type: precision_at_100
      value: 1.039
    - type: precision_at_1000
      value: 0.109
    - type: precision_at_3
      value: 26.308
    - type: precision_at_5
      value: 17.291
    - type: recall_at_1
      value: 52.242999999999995
    - type: recall_at_10
      value: 84.71
    - type: recall_at_100
      value: 93.309
    - type: recall_at_1000
      value: 96.013
    - type: recall_at_3
      value: 72.554
    - type: recall_at_5
      value: 79.069
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
      value: 14.346
    - type: map_at_10
      value: 24.552
    - type: map_at_100
      value: 26.161
    - type: map_at_1000
      value: 26.345000000000002
    - type: map_at_3
      value: 21.208
    - type: map_at_5
      value: 22.959
    - type: mrr_at_1
      value: 29.166999999999998
    - type: mrr_at_10
      value: 38.182
    - type: mrr_at_100
      value: 39.22
    - type: mrr_at_1000
      value: 39.263
    - type: mrr_at_3
      value: 35.983
    - type: mrr_at_5
      value: 37.14
    - type: ndcg_at_1
      value: 29.166999999999998
    - type: ndcg_at_10
      value: 31.421
    - type: ndcg_at_100
      value: 38.129999999999995
    - type: ndcg_at_1000
      value: 41.569
    - type: ndcg_at_3
      value: 28.172000000000004
    - type: ndcg_at_5
      value: 29.029
    - type: precision_at_1
      value: 29.166999999999998
    - type: precision_at_10
      value: 8.997
    - type: precision_at_100
      value: 1.5709999999999997
    - type: precision_at_1000
      value: 0.22
    - type: precision_at_3
      value: 19.187
    - type: precision_at_5
      value: 13.980999999999998
    - type: recall_at_1
      value: 14.346
    - type: recall_at_10
      value: 37.963
    - type: recall_at_100
      value: 63.43299999999999
    - type: recall_at_1000
      value: 84.057
    - type: recall_at_3
      value: 26.119999999999997
    - type: recall_at_5
      value: 30.988
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
      value: 33.059
    - type: map_at_10
      value: 46.421
    - type: map_at_100
      value: 47.323
    - type: map_at_1000
      value: 47.403
    - type: map_at_3
      value: 43.553999999999995
    - type: map_at_5
      value: 45.283
    - type: mrr_at_1
      value: 66.117
    - type: mrr_at_10
      value: 73.10900000000001
    - type: mrr_at_100
      value: 73.444
    - type: mrr_at_1000
      value: 73.46000000000001
    - type: mrr_at_3
      value: 71.70400000000001
    - type: mrr_at_5
      value: 72.58099999999999
    - type: ndcg_at_1
      value: 66.117
    - type: ndcg_at_10
      value: 55.696999999999996
    - type: ndcg_at_100
      value: 59.167
    - type: ndcg_at_1000
      value: 60.809000000000005
    - type: ndcg_at_3
      value: 51.243
    - type: ndcg_at_5
      value: 53.627
    - type: precision_at_1
      value: 66.117
    - type: precision_at_10
      value: 11.538
    - type: precision_at_100
      value: 1.429
    - type: precision_at_1000
      value: 0.165
    - type: precision_at_3
      value: 31.861
    - type: precision_at_5
      value: 20.997
    - type: recall_at_1
      value: 33.059
    - type: recall_at_10
      value: 57.691
    - type: recall_at_100
      value: 71.458
    - type: recall_at_1000
      value: 82.35
    - type: recall_at_3
      value: 47.792
    - type: recall_at_5
      value: 52.492000000000004
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
      value: 80.544
    - type: ap
      value: 74.69592367984956
    - type: f1
      value: 80.51138138449883
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
      value: 17.095
    - type: map_at_10
      value: 28.038999999999998
    - type: map_at_100
      value: 29.246
    - type: map_at_1000
      value: 29.311
    - type: map_at_3
      value: 24.253
    - type: map_at_5
      value: 26.442
    - type: mrr_at_1
      value: 17.535999999999998
    - type: mrr_at_10
      value: 28.53
    - type: mrr_at_100
      value: 29.697000000000003
    - type: mrr_at_1000
      value: 29.755
    - type: mrr_at_3
      value: 24.779999999999998
    - type: mrr_at_5
      value: 26.942
    - type: ndcg_at_1
      value: 17.549999999999997
    - type: ndcg_at_10
      value: 34.514
    - type: ndcg_at_100
      value: 40.497
    - type: ndcg_at_1000
      value: 42.17
    - type: ndcg_at_3
      value: 26.764
    - type: ndcg_at_5
      value: 30.678
    - type: precision_at_1
      value: 17.549999999999997
    - type: precision_at_10
      value: 5.692
    - type: precision_at_100
      value: 0.8699999999999999
    - type: precision_at_1000
      value: 0.101
    - type: precision_at_3
      value: 11.562
    - type: precision_at_5
      value: 8.917
    - type: recall_at_1
      value: 17.095
    - type: recall_at_10
      value: 54.642
    - type: recall_at_100
      value: 82.652
    - type: recall_at_1000
      value: 95.555
    - type: recall_at_3
      value: 33.504
    - type: recall_at_5
      value: 42.925000000000004
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
      value: 91.75558595531236
    - type: f1
      value: 91.25979279648296
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
      value: 69.90424076607387
    - type: f1
      value: 52.067408707562244
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
      value: 70.13449899125757
    - type: f1
      value: 67.62456762910598
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
      value: 74.862138533961
    - type: f1
      value: 74.66457222091381
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
      value: 34.10761942610792
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
      value: 31.673172170578408
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
      value: 32.058704977250315
    - type: mrr
      value: 33.24327760839221
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
      value: 5.163
    - type: map_at_10
      value: 11.652999999999999
    - type: map_at_100
      value: 14.849
    - type: map_at_1000
      value: 16.253999999999998
    - type: map_at_3
      value: 8.616999999999999
    - type: map_at_5
      value: 10.100000000000001
    - type: mrr_at_1
      value: 44.272
    - type: mrr_at_10
      value: 52.25
    - type: mrr_at_100
      value: 52.761
    - type: mrr_at_1000
      value: 52.811
    - type: mrr_at_3
      value: 50.31
    - type: mrr_at_5
      value: 51.347
    - type: ndcg_at_1
      value: 42.105
    - type: ndcg_at_10
      value: 32.044
    - type: ndcg_at_100
      value: 29.763
    - type: ndcg_at_1000
      value: 38.585
    - type: ndcg_at_3
      value: 36.868
    - type: ndcg_at_5
      value: 35.154999999999994
    - type: precision_at_1
      value: 43.653
    - type: precision_at_10
      value: 23.622
    - type: precision_at_100
      value: 7.7490000000000006
    - type: precision_at_1000
      value: 2.054
    - type: precision_at_3
      value: 34.262
    - type: precision_at_5
      value: 30.154999999999998
    - type: recall_at_1
      value: 5.163
    - type: recall_at_10
      value: 15.478
    - type: recall_at_100
      value: 30.424
    - type: recall_at_1000
      value: 62.67
    - type: recall_at_3
      value: 9.615
    - type: recall_at_5
      value: 12.369
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
      value: 21.618000000000002
    - type: map_at_10
      value: 35.465
    - type: map_at_100
      value: 36.712
    - type: map_at_1000
      value: 36.757
    - type: map_at_3
      value: 31.189
    - type: map_at_5
      value: 33.537
    - type: mrr_at_1
      value: 24.305
    - type: mrr_at_10
      value: 37.653
    - type: mrr_at_100
      value: 38.662
    - type: mrr_at_1000
      value: 38.694
    - type: mrr_at_3
      value: 33.889
    - type: mrr_at_5
      value: 35.979
    - type: ndcg_at_1
      value: 24.305
    - type: ndcg_at_10
      value: 43.028
    - type: ndcg_at_100
      value: 48.653999999999996
    - type: ndcg_at_1000
      value: 49.733
    - type: ndcg_at_3
      value: 34.768
    - type: ndcg_at_5
      value: 38.753
    - type: precision_at_1
      value: 24.305
    - type: precision_at_10
      value: 7.59
    - type: precision_at_100
      value: 1.076
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: precision_at_3
      value: 16.271
    - type: precision_at_5
      value: 12.068
    - type: recall_at_1
      value: 21.618000000000002
    - type: recall_at_10
      value: 63.977
    - type: recall_at_100
      value: 89.03999999999999
    - type: recall_at_1000
      value: 97.10600000000001
    - type: recall_at_3
      value: 42.422
    - type: recall_at_5
      value: 51.629000000000005
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
      value: 69.405
    - type: map_at_10
      value: 83.05
    - type: map_at_100
      value: 83.684
    - type: map_at_1000
      value: 83.70400000000001
    - type: map_at_3
      value: 80.08800000000001
    - type: map_at_5
      value: 81.937
    - type: mrr_at_1
      value: 79.85
    - type: mrr_at_10
      value: 86.369
    - type: mrr_at_100
      value: 86.48599999999999
    - type: mrr_at_1000
      value: 86.48700000000001
    - type: mrr_at_3
      value: 85.315
    - type: mrr_at_5
      value: 86.044
    - type: ndcg_at_1
      value: 79.86999999999999
    - type: ndcg_at_10
      value: 87.04499999999999
    - type: ndcg_at_100
      value: 88.373
    - type: ndcg_at_1000
      value: 88.531
    - type: ndcg_at_3
      value: 84.04
    - type: ndcg_at_5
      value: 85.684
    - type: precision_at_1
      value: 79.86999999999999
    - type: precision_at_10
      value: 13.183
    - type: precision_at_100
      value: 1.51
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 36.67
    - type: precision_at_5
      value: 24.12
    - type: recall_at_1
      value: 69.405
    - type: recall_at_10
      value: 94.634
    - type: recall_at_100
      value: 99.214
    - type: recall_at_1000
      value: 99.958
    - type: recall_at_3
      value: 85.992
    - type: recall_at_5
      value: 90.656
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
      value: 50.191676323145465
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
      value: 56.4874020363744
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
      value: 4.228
    - type: map_at_10
      value: 11.245
    - type: map_at_100
      value: 13.353000000000002
    - type: map_at_1000
      value: 13.665
    - type: map_at_3
      value: 7.779999999999999
    - type: map_at_5
      value: 9.405
    - type: mrr_at_1
      value: 20.9
    - type: mrr_at_10
      value: 31.657999999999998
    - type: mrr_at_100
      value: 32.769999999999996
    - type: mrr_at_1000
      value: 32.833
    - type: mrr_at_3
      value: 28.333000000000002
    - type: mrr_at_5
      value: 30.043
    - type: ndcg_at_1
      value: 20.9
    - type: ndcg_at_10
      value: 19.073
    - type: ndcg_at_100
      value: 27.055
    - type: ndcg_at_1000
      value: 32.641
    - type: ndcg_at_3
      value: 17.483999999999998
    - type: ndcg_at_5
      value: 15.42
    - type: precision_at_1
      value: 20.9
    - type: precision_at_10
      value: 10.17
    - type: precision_at_100
      value: 2.162
    - type: precision_at_1000
      value: 0.35100000000000003
    - type: precision_at_3
      value: 16.467000000000002
    - type: precision_at_5
      value: 13.68
    - type: recall_at_1
      value: 4.228
    - type: recall_at_10
      value: 20.573
    - type: recall_at_100
      value: 43.887
    - type: recall_at_1000
      value: 71.22
    - type: recall_at_3
      value: 10.023
    - type: recall_at_5
      value: 13.873
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
      value: 82.77965135067481
    - type: cos_sim_spearman
      value: 75.85121335808076
    - type: euclidean_pearson
      value: 80.09115175262697
    - type: euclidean_spearman
      value: 75.72249155647123
    - type: manhattan_pearson
      value: 79.89723577351782
    - type: manhattan_spearman
      value: 75.49855259442387
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
      value: 80.46084116030949
    - type: cos_sim_spearman
      value: 72.57579204392951
    - type: euclidean_pearson
      value: 76.39020830763684
    - type: euclidean_spearman
      value: 72.3718627025895
    - type: manhattan_pearson
      value: 76.6148833027359
    - type: manhattan_spearman
      value: 72.57570008442319
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
      value: 80.43678068337017
    - type: cos_sim_spearman
      value: 82.38941154076062
    - type: euclidean_pearson
      value: 81.59260573633661
    - type: euclidean_spearman
      value: 82.31144262574114
    - type: manhattan_pearson
      value: 81.43266909137056
    - type: manhattan_spearman
      value: 82.14704293004861
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
      value: 80.73713431763163
    - type: cos_sim_spearman
      value: 77.97860512809388
    - type: euclidean_pearson
      value: 80.35755041527027
    - type: euclidean_spearman
      value: 78.021703511412
    - type: manhattan_pearson
      value: 80.24440317109162
    - type: manhattan_spearman
      value: 77.93165415697575
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
      value: 85.15111852351204
    - type: cos_sim_spearman
      value: 86.54032447238258
    - type: euclidean_pearson
      value: 86.14157021537433
    - type: euclidean_spearman
      value: 86.67537291929713
    - type: manhattan_pearson
      value: 86.081041854808
    - type: manhattan_spearman
      value: 86.61561701560558
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
      value: 81.34532445104026
    - type: cos_sim_spearman
      value: 83.31325001474116
    - type: euclidean_pearson
      value: 82.81892375201032
    - type: euclidean_spearman
      value: 83.4521695148055
    - type: manhattan_pearson
      value: 82.72503790526163
    - type: manhattan_spearman
      value: 83.37833652941349
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
      value: 87.25463453839801
    - type: cos_sim_spearman
      value: 88.27655263515948
    - type: euclidean_pearson
      value: 88.0248334411439
    - type: euclidean_spearman
      value: 88.18141448876868
    - type: manhattan_pearson
      value: 87.8080451127279
    - type: manhattan_spearman
      value: 88.01028114423058
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
      value: 63.57551045355218
    - type: cos_sim_spearman
      value: 66.67614095126629
    - type: euclidean_pearson
      value: 66.0787243112528
    - type: euclidean_spearman
      value: 66.83660560636939
    - type: manhattan_pearson
      value: 66.74684019662031
    - type: manhattan_spearman
      value: 67.11761598074368
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
      value: 83.70881496766829
    - type: cos_sim_spearman
      value: 84.37803542941634
    - type: euclidean_pearson
      value: 84.84501245857096
    - type: euclidean_spearman
      value: 84.47088079741476
    - type: manhattan_pearson
      value: 84.77244090794765
    - type: manhattan_spearman
      value: 84.43307343706205
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
      value: 81.53946254759089
    - type: mrr
      value: 94.68259953554072
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
      value: 51.817
    - type: map_at_10
      value: 62.339999999999996
    - type: map_at_100
      value: 62.88
    - type: map_at_1000
      value: 62.909000000000006
    - type: map_at_3
      value: 59.004
    - type: map_at_5
      value: 60.906000000000006
    - type: mrr_at_1
      value: 54.333
    - type: mrr_at_10
      value: 63.649
    - type: mrr_at_100
      value: 64.01
    - type: mrr_at_1000
      value: 64.039
    - type: mrr_at_3
      value: 61.056
    - type: mrr_at_5
      value: 62.639
    - type: ndcg_at_1
      value: 54.333
    - type: ndcg_at_10
      value: 67.509
    - type: ndcg_at_100
      value: 69.69999999999999
    - type: ndcg_at_1000
      value: 70.613
    - type: ndcg_at_3
      value: 61.729
    - type: ndcg_at_5
      value: 64.696
    - type: precision_at_1
      value: 54.333
    - type: precision_at_10
      value: 9.2
    - type: precision_at_100
      value: 1.043
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 24.0
    - type: precision_at_5
      value: 16.2
    - type: recall_at_1
      value: 51.817
    - type: recall_at_10
      value: 82.056
    - type: recall_at_100
      value: 91.667
    - type: recall_at_1000
      value: 99.0
    - type: recall_at_3
      value: 66.717
    - type: recall_at_5
      value: 74.17200000000001
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
      value: 99.82475247524752
    - type: cos_sim_ap
      value: 95.4781199603258
    - type: cos_sim_f1
      value: 91.16186693147964
    - type: cos_sim_precision
      value: 90.53254437869822
    - type: cos_sim_recall
      value: 91.8
    - type: dot_accuracy
      value: 99.75049504950495
    - type: dot_ap
      value: 93.05183539809457
    - type: dot_f1
      value: 87.31117824773412
    - type: dot_precision
      value: 87.93103448275862
    - type: dot_recall
      value: 86.7
    - type: euclidean_accuracy
      value: 99.82475247524752
    - type: euclidean_ap
      value: 95.38547978154382
    - type: euclidean_f1
      value: 91.16325511732403
    - type: euclidean_precision
      value: 91.02691924227318
    - type: euclidean_recall
      value: 91.3
    - type: manhattan_accuracy
      value: 99.82574257425742
    - type: manhattan_ap
      value: 95.47237521890308
    - type: manhattan_f1
      value: 91.27849355797821
    - type: manhattan_precision
      value: 90.47151277013754
    - type: manhattan_recall
      value: 92.10000000000001
    - type: max_accuracy
      value: 99.82574257425742
    - type: max_ap
      value: 95.4781199603258
    - type: max_f1
      value: 91.27849355797821
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
      value: 57.542169376331245
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
      value: 35.74399302634387
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
      value: 49.65076347632749
    - type: mrr
      value: 50.418099057804945
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
      value: 29.73997756592847
    - type: cos_sim_spearman
      value: 29.465208011593308
    - type: dot_pearson
      value: 24.83735342474541
    - type: dot_spearman
      value: 26.005180528584855
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
      value: 0.208
    - type: map_at_10
      value: 1.434
    - type: map_at_100
      value: 7.829
    - type: map_at_1000
      value: 19.807
    - type: map_at_3
      value: 0.549
    - type: map_at_5
      value: 0.8330000000000001
    - type: mrr_at_1
      value: 78.0
    - type: mrr_at_10
      value: 85.35199999999999
    - type: mrr_at_100
      value: 85.673
    - type: mrr_at_1000
      value: 85.673
    - type: mrr_at_3
      value: 84.667
    - type: mrr_at_5
      value: 85.06700000000001
    - type: ndcg_at_1
      value: 72.0
    - type: ndcg_at_10
      value: 59.214999999999996
    - type: ndcg_at_100
      value: 44.681
    - type: ndcg_at_1000
      value: 43.035000000000004
    - type: ndcg_at_3
      value: 66.53099999999999
    - type: ndcg_at_5
      value: 63.23
    - type: precision_at_1
      value: 78.0
    - type: precision_at_10
      value: 62.4
    - type: precision_at_100
      value: 45.76
    - type: precision_at_1000
      value: 19.05
    - type: precision_at_3
      value: 71.333
    - type: precision_at_5
      value: 67.2
    - type: recall_at_1
      value: 0.208
    - type: recall_at_10
      value: 1.6580000000000001
    - type: recall_at_100
      value: 11.324
    - type: recall_at_1000
      value: 41.537
    - type: recall_at_3
      value: 0.579
    - type: recall_at_5
      value: 0.8959999999999999
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
      value: 2.442
    - type: map_at_10
      value: 8.863
    - type: map_at_100
      value: 14.606
    - type: map_at_1000
      value: 16.258
    - type: map_at_3
      value: 4.396
    - type: map_at_5
      value: 6.199000000000001
    - type: mrr_at_1
      value: 30.612000000000002
    - type: mrr_at_10
      value: 43.492
    - type: mrr_at_100
      value: 44.557
    - type: mrr_at_1000
      value: 44.557
    - type: mrr_at_3
      value: 40.816
    - type: mrr_at_5
      value: 42.143
    - type: ndcg_at_1
      value: 25.509999999999998
    - type: ndcg_at_10
      value: 22.076
    - type: ndcg_at_100
      value: 34.098
    - type: ndcg_at_1000
      value: 46.265
    - type: ndcg_at_3
      value: 24.19
    - type: ndcg_at_5
      value: 23.474
    - type: precision_at_1
      value: 30.612000000000002
    - type: precision_at_10
      value: 19.796
    - type: precision_at_100
      value: 7.286
    - type: precision_at_1000
      value: 1.5310000000000001
    - type: precision_at_3
      value: 25.85
    - type: precision_at_5
      value: 24.490000000000002
    - type: recall_at_1
      value: 2.442
    - type: recall_at_10
      value: 15.012
    - type: recall_at_100
      value: 45.865
    - type: recall_at_1000
      value: 82.958
    - type: recall_at_3
      value: 5.731
    - type: recall_at_5
      value: 9.301
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
      value: 70.974
    - type: ap
      value: 14.534996211286682
    - type: f1
      value: 54.785946183399005
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
      value: 58.56819468024901
    - type: f1
      value: 58.92391487111204
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
      value: 43.273202335218194
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
      value: 84.37742146986946
    - type: cos_sim_ap
      value: 68.1684129575579
    - type: cos_sim_f1
      value: 64.93475108748189
    - type: cos_sim_precision
      value: 59.89745876058849
    - type: cos_sim_recall
      value: 70.89709762532982
    - type: dot_accuracy
      value: 80.49710913750968
    - type: dot_ap
      value: 54.699790073944186
    - type: dot_f1
      value: 54.45130013221684
    - type: dot_precision
      value: 46.74612183125236
    - type: dot_recall
      value: 65.19788918205805
    - type: euclidean_accuracy
      value: 84.5085533766466
    - type: euclidean_ap
      value: 68.38835695236224
    - type: euclidean_f1
      value: 65.3391121002694
    - type: euclidean_precision
      value: 58.75289656625237
    - type: euclidean_recall
      value: 73.58839050131925
    - type: manhattan_accuracy
      value: 84.40126363473803
    - type: manhattan_ap
      value: 68.09539181555348
    - type: manhattan_f1
      value: 64.99028182701653
    - type: manhattan_precision
      value: 60.22062134173795
    - type: manhattan_recall
      value: 70.58047493403694
    - type: max_accuracy
      value: 84.5085533766466
    - type: max_ap
      value: 68.38835695236224
    - type: max_f1
      value: 65.3391121002694
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
      value: 88.34167733923235
    - type: cos_sim_ap
      value: 84.84136381147736
    - type: cos_sim_f1
      value: 77.01434980904001
    - type: cos_sim_precision
      value: 74.27937915742794
    - type: cos_sim_recall
      value: 79.95842315983985
    - type: dot_accuracy
      value: 85.06422944075756
    - type: dot_ap
      value: 76.49446747522325
    - type: dot_f1
      value: 71.11606520830432
    - type: dot_precision
      value: 64.93638676844785
    - type: dot_recall
      value: 78.59562673236834
    - type: euclidean_accuracy
      value: 88.45810532852097
    - type: euclidean_ap
      value: 84.91526721863501
    - type: euclidean_f1
      value: 77.04399001750662
    - type: euclidean_precision
      value: 74.62298867162133
    - type: euclidean_recall
      value: 79.62734832152756
    - type: manhattan_accuracy
      value: 88.46004579500912
    - type: manhattan_ap
      value: 84.81590026238194
    - type: manhattan_f1
      value: 76.97804626491822
    - type: manhattan_precision
      value: 73.79237288135593
    - type: manhattan_recall
      value: 80.45118570988605
    - type: max_accuracy
      value: 88.46004579500912
    - type: max_ap
      value: 84.91526721863501
    - type: max_f1
      value: 77.04399001750662

pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- mteb

---

# {gte-tiny}

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search. 
It is distilled from `thenlper/gte-small`, with comparable (slightly worse) performance at around half the size.

<!--- Describe your model here -->

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