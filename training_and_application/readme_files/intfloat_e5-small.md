---
tags:
- mteb
- Sentence Transformers
- sentence-similarity
- sentence-transformers
model-index:
- name: e5-small
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
      value: 76.22388059701493
    - type: ap
      value: 40.27466219523129
    - type: f1
      value: 70.60533006025108
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
      value: 87.525775
    - type: ap
      value: 83.51063993897611
    - type: f1
      value: 87.49342736805572
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
      value: 42.611999999999995
    - type: f1
      value: 42.05088045932892
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
      value: 23.826
    - type: map_at_10
      value: 38.269
    - type: map_at_100
      value: 39.322
    - type: map_at_1000
      value: 39.344
    - type: map_at_3
      value: 33.428000000000004
    - type: map_at_5
      value: 36.063
    - type: mrr_at_1
      value: 24.253
    - type: mrr_at_10
      value: 38.425
    - type: mrr_at_100
      value: 39.478
    - type: mrr_at_1000
      value: 39.5
    - type: mrr_at_3
      value: 33.606
    - type: mrr_at_5
      value: 36.195
    - type: ndcg_at_1
      value: 23.826
    - type: ndcg_at_10
      value: 46.693
    - type: ndcg_at_100
      value: 51.469
    - type: ndcg_at_1000
      value: 52.002
    - type: ndcg_at_3
      value: 36.603
    - type: ndcg_at_5
      value: 41.365
    - type: precision_at_1
      value: 23.826
    - type: precision_at_10
      value: 7.383000000000001
    - type: precision_at_100
      value: 0.9530000000000001
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_3
      value: 15.268
    - type: precision_at_5
      value: 11.479000000000001
    - type: recall_at_1
      value: 23.826
    - type: recall_at_10
      value: 73.82600000000001
    - type: recall_at_100
      value: 95.306
    - type: recall_at_1000
      value: 99.431
    - type: recall_at_3
      value: 45.804
    - type: recall_at_5
      value: 57.397
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
      value: 44.13995374767436
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
      value: 37.13950072624313
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
      value: 59.35843292105327
    - type: mrr
      value: 73.72312359846987
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
      value: 84.55140418324174
    - type: cos_sim_spearman
      value: 84.21637675860022
    - type: euclidean_pearson
      value: 81.26069614610006
    - type: euclidean_spearman
      value: 83.25069210421785
    - type: manhattan_pearson
      value: 80.17441422581014
    - type: manhattan_spearman
      value: 81.87596198487877
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
      value: 81.87337662337661
    - type: f1
      value: 81.76647866926402
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
      value: 35.80600542614507
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
      value: 31.86321613256603
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
      value: 32.054
    - type: map_at_10
      value: 40.699999999999996
    - type: map_at_100
      value: 41.818
    - type: map_at_1000
      value: 41.959999999999994
    - type: map_at_3
      value: 37.742
    - type: map_at_5
      value: 39.427
    - type: mrr_at_1
      value: 38.769999999999996
    - type: mrr_at_10
      value: 46.150000000000006
    - type: mrr_at_100
      value: 46.865
    - type: mrr_at_1000
      value: 46.925
    - type: mrr_at_3
      value: 43.705
    - type: mrr_at_5
      value: 45.214999999999996
    - type: ndcg_at_1
      value: 38.769999999999996
    - type: ndcg_at_10
      value: 45.778
    - type: ndcg_at_100
      value: 50.38
    - type: ndcg_at_1000
      value: 52.922999999999995
    - type: ndcg_at_3
      value: 41.597
    - type: ndcg_at_5
      value: 43.631
    - type: precision_at_1
      value: 38.769999999999996
    - type: precision_at_10
      value: 8.269
    - type: precision_at_100
      value: 1.278
    - type: precision_at_1000
      value: 0.178
    - type: precision_at_3
      value: 19.266
    - type: precision_at_5
      value: 13.705
    - type: recall_at_1
      value: 32.054
    - type: recall_at_10
      value: 54.947
    - type: recall_at_100
      value: 74.79599999999999
    - type: recall_at_1000
      value: 91.40899999999999
    - type: recall_at_3
      value: 42.431000000000004
    - type: recall_at_5
      value: 48.519
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
      value: 29.035
    - type: map_at_10
      value: 38.007000000000005
    - type: map_at_100
      value: 39.125
    - type: map_at_1000
      value: 39.251999999999995
    - type: map_at_3
      value: 35.77
    - type: map_at_5
      value: 37.057
    - type: mrr_at_1
      value: 36.497
    - type: mrr_at_10
      value: 44.077
    - type: mrr_at_100
      value: 44.743
    - type: mrr_at_1000
      value: 44.79
    - type: mrr_at_3
      value: 42.123
    - type: mrr_at_5
      value: 43.308
    - type: ndcg_at_1
      value: 36.497
    - type: ndcg_at_10
      value: 42.986000000000004
    - type: ndcg_at_100
      value: 47.323
    - type: ndcg_at_1000
      value: 49.624
    - type: ndcg_at_3
      value: 39.805
    - type: ndcg_at_5
      value: 41.286
    - type: precision_at_1
      value: 36.497
    - type: precision_at_10
      value: 7.8340000000000005
    - type: precision_at_100
      value: 1.269
    - type: precision_at_1000
      value: 0.178
    - type: precision_at_3
      value: 19.023
    - type: precision_at_5
      value: 13.248
    - type: recall_at_1
      value: 29.035
    - type: recall_at_10
      value: 51.06
    - type: recall_at_100
      value: 69.64099999999999
    - type: recall_at_1000
      value: 84.49
    - type: recall_at_3
      value: 41.333999999999996
    - type: recall_at_5
      value: 45.663
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
      value: 37.239
    - type: map_at_10
      value: 47.873
    - type: map_at_100
      value: 48.842999999999996
    - type: map_at_1000
      value: 48.913000000000004
    - type: map_at_3
      value: 45.050000000000004
    - type: map_at_5
      value: 46.498
    - type: mrr_at_1
      value: 42.508
    - type: mrr_at_10
      value: 51.44
    - type: mrr_at_100
      value: 52.087
    - type: mrr_at_1000
      value: 52.129999999999995
    - type: mrr_at_3
      value: 49.164
    - type: mrr_at_5
      value: 50.343
    - type: ndcg_at_1
      value: 42.508
    - type: ndcg_at_10
      value: 53.31399999999999
    - type: ndcg_at_100
      value: 57.245000000000005
    - type: ndcg_at_1000
      value: 58.794000000000004
    - type: ndcg_at_3
      value: 48.295
    - type: ndcg_at_5
      value: 50.415
    - type: precision_at_1
      value: 42.508
    - type: precision_at_10
      value: 8.458
    - type: precision_at_100
      value: 1.133
    - type: precision_at_1000
      value: 0.132
    - type: precision_at_3
      value: 21.191
    - type: precision_at_5
      value: 14.307
    - type: recall_at_1
      value: 37.239
    - type: recall_at_10
      value: 65.99000000000001
    - type: recall_at_100
      value: 82.99499999999999
    - type: recall_at_1000
      value: 94.128
    - type: recall_at_3
      value: 52.382
    - type: recall_at_5
      value: 57.648999999999994
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
      value: 23.039
    - type: map_at_10
      value: 29.694
    - type: map_at_100
      value: 30.587999999999997
    - type: map_at_1000
      value: 30.692999999999998
    - type: map_at_3
      value: 27.708
    - type: map_at_5
      value: 28.774
    - type: mrr_at_1
      value: 24.633
    - type: mrr_at_10
      value: 31.478
    - type: mrr_at_100
      value: 32.299
    - type: mrr_at_1000
      value: 32.381
    - type: mrr_at_3
      value: 29.435
    - type: mrr_at_5
      value: 30.446
    - type: ndcg_at_1
      value: 24.633
    - type: ndcg_at_10
      value: 33.697
    - type: ndcg_at_100
      value: 38.080000000000005
    - type: ndcg_at_1000
      value: 40.812
    - type: ndcg_at_3
      value: 29.654000000000003
    - type: ndcg_at_5
      value: 31.474000000000004
    - type: precision_at_1
      value: 24.633
    - type: precision_at_10
      value: 5.0729999999999995
    - type: precision_at_100
      value: 0.753
    - type: precision_at_1000
      value: 0.10300000000000001
    - type: precision_at_3
      value: 12.279
    - type: precision_at_5
      value: 8.452
    - type: recall_at_1
      value: 23.039
    - type: recall_at_10
      value: 44.275999999999996
    - type: recall_at_100
      value: 64.4
    - type: recall_at_1000
      value: 85.135
    - type: recall_at_3
      value: 33.394
    - type: recall_at_5
      value: 37.687
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
      value: 13.594999999999999
    - type: map_at_10
      value: 19.933999999999997
    - type: map_at_100
      value: 20.966
    - type: map_at_1000
      value: 21.087
    - type: map_at_3
      value: 17.749000000000002
    - type: map_at_5
      value: 19.156000000000002
    - type: mrr_at_1
      value: 17.662
    - type: mrr_at_10
      value: 24.407
    - type: mrr_at_100
      value: 25.385
    - type: mrr_at_1000
      value: 25.465
    - type: mrr_at_3
      value: 22.056
    - type: mrr_at_5
      value: 23.630000000000003
    - type: ndcg_at_1
      value: 17.662
    - type: ndcg_at_10
      value: 24.391
    - type: ndcg_at_100
      value: 29.681
    - type: ndcg_at_1000
      value: 32.923
    - type: ndcg_at_3
      value: 20.271
    - type: ndcg_at_5
      value: 22.621
    - type: precision_at_1
      value: 17.662
    - type: precision_at_10
      value: 4.44
    - type: precision_at_100
      value: 0.8200000000000001
    - type: precision_at_1000
      value: 0.125
    - type: precision_at_3
      value: 9.577
    - type: precision_at_5
      value: 7.313
    - type: recall_at_1
      value: 13.594999999999999
    - type: recall_at_10
      value: 33.976
    - type: recall_at_100
      value: 57.43000000000001
    - type: recall_at_1000
      value: 80.958
    - type: recall_at_3
      value: 22.897000000000002
    - type: recall_at_5
      value: 28.714000000000002
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
      value: 26.683
    - type: map_at_10
      value: 35.068
    - type: map_at_100
      value: 36.311
    - type: map_at_1000
      value: 36.436
    - type: map_at_3
      value: 32.371
    - type: map_at_5
      value: 33.761
    - type: mrr_at_1
      value: 32.435
    - type: mrr_at_10
      value: 40.721000000000004
    - type: mrr_at_100
      value: 41.535
    - type: mrr_at_1000
      value: 41.593
    - type: mrr_at_3
      value: 38.401999999999994
    - type: mrr_at_5
      value: 39.567
    - type: ndcg_at_1
      value: 32.435
    - type: ndcg_at_10
      value: 40.538000000000004
    - type: ndcg_at_100
      value: 45.963
    - type: ndcg_at_1000
      value: 48.400999999999996
    - type: ndcg_at_3
      value: 36.048
    - type: ndcg_at_5
      value: 37.899
    - type: precision_at_1
      value: 32.435
    - type: precision_at_10
      value: 7.1129999999999995
    - type: precision_at_100
      value: 1.162
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 16.683
    - type: precision_at_5
      value: 11.684
    - type: recall_at_1
      value: 26.683
    - type: recall_at_10
      value: 51.517
    - type: recall_at_100
      value: 74.553
    - type: recall_at_1000
      value: 90.649
    - type: recall_at_3
      value: 38.495000000000005
    - type: recall_at_5
      value: 43.495
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
      value: 24.186
    - type: map_at_10
      value: 31.972
    - type: map_at_100
      value: 33.117000000000004
    - type: map_at_1000
      value: 33.243
    - type: map_at_3
      value: 29.423
    - type: map_at_5
      value: 30.847
    - type: mrr_at_1
      value: 29.794999999999998
    - type: mrr_at_10
      value: 36.767
    - type: mrr_at_100
      value: 37.645
    - type: mrr_at_1000
      value: 37.716
    - type: mrr_at_3
      value: 34.513
    - type: mrr_at_5
      value: 35.791000000000004
    - type: ndcg_at_1
      value: 29.794999999999998
    - type: ndcg_at_10
      value: 36.786
    - type: ndcg_at_100
      value: 41.94
    - type: ndcg_at_1000
      value: 44.830999999999996
    - type: ndcg_at_3
      value: 32.504
    - type: ndcg_at_5
      value: 34.404
    - type: precision_at_1
      value: 29.794999999999998
    - type: precision_at_10
      value: 6.518
    - type: precision_at_100
      value: 1.0659999999999998
    - type: precision_at_1000
      value: 0.149
    - type: precision_at_3
      value: 15.296999999999999
    - type: precision_at_5
      value: 10.731
    - type: recall_at_1
      value: 24.186
    - type: recall_at_10
      value: 46.617
    - type: recall_at_100
      value: 68.75
    - type: recall_at_1000
      value: 88.864
    - type: recall_at_3
      value: 34.199
    - type: recall_at_5
      value: 39.462
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
      value: 24.22083333333333
    - type: map_at_10
      value: 31.606666666666662
    - type: map_at_100
      value: 32.6195
    - type: map_at_1000
      value: 32.739999999999995
    - type: map_at_3
      value: 29.37825
    - type: map_at_5
      value: 30.596083333333336
    - type: mrr_at_1
      value: 28.607916666666668
    - type: mrr_at_10
      value: 35.54591666666666
    - type: mrr_at_100
      value: 36.33683333333333
    - type: mrr_at_1000
      value: 36.40624999999999
    - type: mrr_at_3
      value: 33.526250000000005
    - type: mrr_at_5
      value: 34.6605
    - type: ndcg_at_1
      value: 28.607916666666668
    - type: ndcg_at_10
      value: 36.07966666666667
    - type: ndcg_at_100
      value: 40.73308333333333
    - type: ndcg_at_1000
      value: 43.40666666666666
    - type: ndcg_at_3
      value: 32.23525
    - type: ndcg_at_5
      value: 33.97083333333333
    - type: precision_at_1
      value: 28.607916666666668
    - type: precision_at_10
      value: 6.120333333333335
    - type: precision_at_100
      value: 0.9921666666666668
    - type: precision_at_1000
      value: 0.14091666666666666
    - type: precision_at_3
      value: 14.54975
    - type: precision_at_5
      value: 10.153166666666667
    - type: recall_at_1
      value: 24.22083333333333
    - type: recall_at_10
      value: 45.49183333333334
    - type: recall_at_100
      value: 66.28133333333332
    - type: recall_at_1000
      value: 85.16541666666667
    - type: recall_at_3
      value: 34.6485
    - type: recall_at_5
      value: 39.229749999999996
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
      value: 21.842
    - type: map_at_10
      value: 27.573999999999998
    - type: map_at_100
      value: 28.410999999999998
    - type: map_at_1000
      value: 28.502
    - type: map_at_3
      value: 25.921
    - type: map_at_5
      value: 26.888
    - type: mrr_at_1
      value: 24.08
    - type: mrr_at_10
      value: 29.915999999999997
    - type: mrr_at_100
      value: 30.669
    - type: mrr_at_1000
      value: 30.746000000000002
    - type: mrr_at_3
      value: 28.349000000000004
    - type: mrr_at_5
      value: 29.246
    - type: ndcg_at_1
      value: 24.08
    - type: ndcg_at_10
      value: 30.898999999999997
    - type: ndcg_at_100
      value: 35.272999999999996
    - type: ndcg_at_1000
      value: 37.679
    - type: ndcg_at_3
      value: 27.881
    - type: ndcg_at_5
      value: 29.432000000000002
    - type: precision_at_1
      value: 24.08
    - type: precision_at_10
      value: 4.678
    - type: precision_at_100
      value: 0.744
    - type: precision_at_1000
      value: 0.10300000000000001
    - type: precision_at_3
      value: 11.860999999999999
    - type: precision_at_5
      value: 8.16
    - type: recall_at_1
      value: 21.842
    - type: recall_at_10
      value: 38.66
    - type: recall_at_100
      value: 59.169000000000004
    - type: recall_at_1000
      value: 76.887
    - type: recall_at_3
      value: 30.532999999999998
    - type: recall_at_5
      value: 34.354
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
      value: 17.145
    - type: map_at_10
      value: 22.729
    - type: map_at_100
      value: 23.574
    - type: map_at_1000
      value: 23.695
    - type: map_at_3
      value: 21.044
    - type: map_at_5
      value: 21.981
    - type: mrr_at_1
      value: 20.888
    - type: mrr_at_10
      value: 26.529000000000003
    - type: mrr_at_100
      value: 27.308
    - type: mrr_at_1000
      value: 27.389000000000003
    - type: mrr_at_3
      value: 24.868000000000002
    - type: mrr_at_5
      value: 25.825
    - type: ndcg_at_1
      value: 20.888
    - type: ndcg_at_10
      value: 26.457000000000004
    - type: ndcg_at_100
      value: 30.764000000000003
    - type: ndcg_at_1000
      value: 33.825
    - type: ndcg_at_3
      value: 23.483999999999998
    - type: ndcg_at_5
      value: 24.836
    - type: precision_at_1
      value: 20.888
    - type: precision_at_10
      value: 4.58
    - type: precision_at_100
      value: 0.784
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 10.874
    - type: precision_at_5
      value: 7.639
    - type: recall_at_1
      value: 17.145
    - type: recall_at_10
      value: 33.938
    - type: recall_at_100
      value: 53.672
    - type: recall_at_1000
      value: 76.023
    - type: recall_at_3
      value: 25.363000000000003
    - type: recall_at_5
      value: 29.023
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
      value: 24.275
    - type: map_at_10
      value: 30.438
    - type: map_at_100
      value: 31.489
    - type: map_at_1000
      value: 31.601000000000003
    - type: map_at_3
      value: 28.647
    - type: map_at_5
      value: 29.660999999999998
    - type: mrr_at_1
      value: 28.077999999999996
    - type: mrr_at_10
      value: 34.098
    - type: mrr_at_100
      value: 35.025
    - type: mrr_at_1000
      value: 35.109
    - type: mrr_at_3
      value: 32.4
    - type: mrr_at_5
      value: 33.379999999999995
    - type: ndcg_at_1
      value: 28.077999999999996
    - type: ndcg_at_10
      value: 34.271
    - type: ndcg_at_100
      value: 39.352
    - type: ndcg_at_1000
      value: 42.199
    - type: ndcg_at_3
      value: 30.978
    - type: ndcg_at_5
      value: 32.498
    - type: precision_at_1
      value: 28.077999999999996
    - type: precision_at_10
      value: 5.345
    - type: precision_at_100
      value: 0.897
    - type: precision_at_1000
      value: 0.125
    - type: precision_at_3
      value: 13.526
    - type: precision_at_5
      value: 9.16
    - type: recall_at_1
      value: 24.275
    - type: recall_at_10
      value: 42.362
    - type: recall_at_100
      value: 64.461
    - type: recall_at_1000
      value: 84.981
    - type: recall_at_3
      value: 33.249
    - type: recall_at_5
      value: 37.214999999999996
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
      value: 22.358
    - type: map_at_10
      value: 30.062
    - type: map_at_100
      value: 31.189
    - type: map_at_1000
      value: 31.386999999999997
    - type: map_at_3
      value: 27.672
    - type: map_at_5
      value: 28.76
    - type: mrr_at_1
      value: 26.877000000000002
    - type: mrr_at_10
      value: 33.948
    - type: mrr_at_100
      value: 34.746
    - type: mrr_at_1000
      value: 34.816
    - type: mrr_at_3
      value: 31.884
    - type: mrr_at_5
      value: 33.001000000000005
    - type: ndcg_at_1
      value: 26.877000000000002
    - type: ndcg_at_10
      value: 34.977000000000004
    - type: ndcg_at_100
      value: 39.753
    - type: ndcg_at_1000
      value: 42.866
    - type: ndcg_at_3
      value: 30.956
    - type: ndcg_at_5
      value: 32.381
    - type: precision_at_1
      value: 26.877000000000002
    - type: precision_at_10
      value: 6.7
    - type: precision_at_100
      value: 1.287
    - type: precision_at_1000
      value: 0.215
    - type: precision_at_3
      value: 14.360999999999999
    - type: precision_at_5
      value: 10.119
    - type: recall_at_1
      value: 22.358
    - type: recall_at_10
      value: 44.183
    - type: recall_at_100
      value: 67.14
    - type: recall_at_1000
      value: 87.53999999999999
    - type: recall_at_3
      value: 32.79
    - type: recall_at_5
      value: 36.829
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
      value: 19.198999999999998
    - type: map_at_10
      value: 25.229000000000003
    - type: map_at_100
      value: 26.003
    - type: map_at_1000
      value: 26.111
    - type: map_at_3
      value: 23.442
    - type: map_at_5
      value: 24.343
    - type: mrr_at_1
      value: 21.072
    - type: mrr_at_10
      value: 27.02
    - type: mrr_at_100
      value: 27.735
    - type: mrr_at_1000
      value: 27.815
    - type: mrr_at_3
      value: 25.416
    - type: mrr_at_5
      value: 26.173999999999996
    - type: ndcg_at_1
      value: 21.072
    - type: ndcg_at_10
      value: 28.862
    - type: ndcg_at_100
      value: 33.043
    - type: ndcg_at_1000
      value: 36.003
    - type: ndcg_at_3
      value: 25.35
    - type: ndcg_at_5
      value: 26.773000000000003
    - type: precision_at_1
      value: 21.072
    - type: precision_at_10
      value: 4.436
    - type: precision_at_100
      value: 0.713
    - type: precision_at_1000
      value: 0.106
    - type: precision_at_3
      value: 10.659
    - type: precision_at_5
      value: 7.32
    - type: recall_at_1
      value: 19.198999999999998
    - type: recall_at_10
      value: 38.376
    - type: recall_at_100
      value: 58.36900000000001
    - type: recall_at_1000
      value: 80.92099999999999
    - type: recall_at_3
      value: 28.715000000000003
    - type: recall_at_5
      value: 32.147
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
      value: 5.9319999999999995
    - type: map_at_10
      value: 10.483
    - type: map_at_100
      value: 11.97
    - type: map_at_1000
      value: 12.171999999999999
    - type: map_at_3
      value: 8.477
    - type: map_at_5
      value: 9.495000000000001
    - type: mrr_at_1
      value: 13.094
    - type: mrr_at_10
      value: 21.282
    - type: mrr_at_100
      value: 22.556
    - type: mrr_at_1000
      value: 22.628999999999998
    - type: mrr_at_3
      value: 18.218999999999998
    - type: mrr_at_5
      value: 19.900000000000002
    - type: ndcg_at_1
      value: 13.094
    - type: ndcg_at_10
      value: 15.811
    - type: ndcg_at_100
      value: 23.035
    - type: ndcg_at_1000
      value: 27.089999999999996
    - type: ndcg_at_3
      value: 11.905000000000001
    - type: ndcg_at_5
      value: 13.377
    - type: precision_at_1
      value: 13.094
    - type: precision_at_10
      value: 5.225
    - type: precision_at_100
      value: 1.2970000000000002
    - type: precision_at_1000
      value: 0.203
    - type: precision_at_3
      value: 8.86
    - type: precision_at_5
      value: 7.309
    - type: recall_at_1
      value: 5.9319999999999995
    - type: recall_at_10
      value: 20.305
    - type: recall_at_100
      value: 46.314
    - type: recall_at_1000
      value: 69.612
    - type: recall_at_3
      value: 11.21
    - type: recall_at_5
      value: 14.773
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
      value: 8.674
    - type: map_at_10
      value: 17.822
    - type: map_at_100
      value: 24.794
    - type: map_at_1000
      value: 26.214
    - type: map_at_3
      value: 12.690999999999999
    - type: map_at_5
      value: 15.033
    - type: mrr_at_1
      value: 61.75000000000001
    - type: mrr_at_10
      value: 71.58
    - type: mrr_at_100
      value: 71.923
    - type: mrr_at_1000
      value: 71.932
    - type: mrr_at_3
      value: 70.125
    - type: mrr_at_5
      value: 71.038
    - type: ndcg_at_1
      value: 51
    - type: ndcg_at_10
      value: 38.637
    - type: ndcg_at_100
      value: 42.398
    - type: ndcg_at_1000
      value: 48.962
    - type: ndcg_at_3
      value: 43.29
    - type: ndcg_at_5
      value: 40.763
    - type: precision_at_1
      value: 61.75000000000001
    - type: precision_at_10
      value: 30.125
    - type: precision_at_100
      value: 9.53
    - type: precision_at_1000
      value: 1.9619999999999997
    - type: precision_at_3
      value: 45.583
    - type: precision_at_5
      value: 38.95
    - type: recall_at_1
      value: 8.674
    - type: recall_at_10
      value: 23.122
    - type: recall_at_100
      value: 47.46
    - type: recall_at_1000
      value: 67.662
    - type: recall_at_3
      value: 13.946
    - type: recall_at_5
      value: 17.768
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
      value: 46.86000000000001
    - type: f1
      value: 41.343580452760776
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
      value: 36.609
    - type: map_at_10
      value: 47.552
    - type: map_at_100
      value: 48.283
    - type: map_at_1000
      value: 48.321
    - type: map_at_3
      value: 44.869
    - type: map_at_5
      value: 46.509
    - type: mrr_at_1
      value: 39.214
    - type: mrr_at_10
      value: 50.434999999999995
    - type: mrr_at_100
      value: 51.122
    - type: mrr_at_1000
      value: 51.151
    - type: mrr_at_3
      value: 47.735
    - type: mrr_at_5
      value: 49.394
    - type: ndcg_at_1
      value: 39.214
    - type: ndcg_at_10
      value: 53.52400000000001
    - type: ndcg_at_100
      value: 56.997
    - type: ndcg_at_1000
      value: 57.975
    - type: ndcg_at_3
      value: 48.173
    - type: ndcg_at_5
      value: 51.05800000000001
    - type: precision_at_1
      value: 39.214
    - type: precision_at_10
      value: 7.573
    - type: precision_at_100
      value: 0.9440000000000001
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 19.782
    - type: precision_at_5
      value: 13.453000000000001
    - type: recall_at_1
      value: 36.609
    - type: recall_at_10
      value: 69.247
    - type: recall_at_100
      value: 84.99600000000001
    - type: recall_at_1000
      value: 92.40899999999999
    - type: recall_at_3
      value: 54.856
    - type: recall_at_5
      value: 61.797000000000004
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
      value: 16.466
    - type: map_at_10
      value: 27.060000000000002
    - type: map_at_100
      value: 28.511999999999997
    - type: map_at_1000
      value: 28.693
    - type: map_at_3
      value: 22.777
    - type: map_at_5
      value: 25.086000000000002
    - type: mrr_at_1
      value: 32.716
    - type: mrr_at_10
      value: 41.593999999999994
    - type: mrr_at_100
      value: 42.370000000000005
    - type: mrr_at_1000
      value: 42.419000000000004
    - type: mrr_at_3
      value: 38.143
    - type: mrr_at_5
      value: 40.288000000000004
    - type: ndcg_at_1
      value: 32.716
    - type: ndcg_at_10
      value: 34.795
    - type: ndcg_at_100
      value: 40.58
    - type: ndcg_at_1000
      value: 43.993
    - type: ndcg_at_3
      value: 29.573
    - type: ndcg_at_5
      value: 31.583
    - type: precision_at_1
      value: 32.716
    - type: precision_at_10
      value: 9.937999999999999
    - type: precision_at_100
      value: 1.585
    - type: precision_at_1000
      value: 0.22
    - type: precision_at_3
      value: 19.496
    - type: precision_at_5
      value: 15.247
    - type: recall_at_1
      value: 16.466
    - type: recall_at_10
      value: 42.886
    - type: recall_at_100
      value: 64.724
    - type: recall_at_1000
      value: 85.347
    - type: recall_at_3
      value: 26.765
    - type: recall_at_5
      value: 33.603
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
      value: 33.025
    - type: map_at_10
      value: 47.343
    - type: map_at_100
      value: 48.207
    - type: map_at_1000
      value: 48.281
    - type: map_at_3
      value: 44.519
    - type: map_at_5
      value: 46.217000000000006
    - type: mrr_at_1
      value: 66.05
    - type: mrr_at_10
      value: 72.94699999999999
    - type: mrr_at_100
      value: 73.289
    - type: mrr_at_1000
      value: 73.30499999999999
    - type: mrr_at_3
      value: 71.686
    - type: mrr_at_5
      value: 72.491
    - type: ndcg_at_1
      value: 66.05
    - type: ndcg_at_10
      value: 56.338
    - type: ndcg_at_100
      value: 59.599999999999994
    - type: ndcg_at_1000
      value: 61.138000000000005
    - type: ndcg_at_3
      value: 52.034000000000006
    - type: ndcg_at_5
      value: 54.352000000000004
    - type: precision_at_1
      value: 66.05
    - type: precision_at_10
      value: 11.693000000000001
    - type: precision_at_100
      value: 1.425
    - type: precision_at_1000
      value: 0.163
    - type: precision_at_3
      value: 32.613
    - type: precision_at_5
      value: 21.401999999999997
    - type: recall_at_1
      value: 33.025
    - type: recall_at_10
      value: 58.467
    - type: recall_at_100
      value: 71.242
    - type: recall_at_1000
      value: 81.452
    - type: recall_at_3
      value: 48.92
    - type: recall_at_5
      value: 53.504
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
      value: 75.5492
    - type: ap
      value: 69.42911637216271
    - type: f1
      value: 75.39113704261024
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
      value: 23.173
    - type: map_at_10
      value: 35.453
    - type: map_at_100
      value: 36.573
    - type: map_at_1000
      value: 36.620999999999995
    - type: map_at_3
      value: 31.655
    - type: map_at_5
      value: 33.823
    - type: mrr_at_1
      value: 23.868000000000002
    - type: mrr_at_10
      value: 36.085
    - type: mrr_at_100
      value: 37.15
    - type: mrr_at_1000
      value: 37.193
    - type: mrr_at_3
      value: 32.376
    - type: mrr_at_5
      value: 34.501
    - type: ndcg_at_1
      value: 23.854
    - type: ndcg_at_10
      value: 42.33
    - type: ndcg_at_100
      value: 47.705999999999996
    - type: ndcg_at_1000
      value: 48.91
    - type: ndcg_at_3
      value: 34.604
    - type: ndcg_at_5
      value: 38.473
    - type: precision_at_1
      value: 23.854
    - type: precision_at_10
      value: 6.639
    - type: precision_at_100
      value: 0.932
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 14.685
    - type: precision_at_5
      value: 10.782
    - type: recall_at_1
      value: 23.173
    - type: recall_at_10
      value: 63.441
    - type: recall_at_100
      value: 88.25
    - type: recall_at_1000
      value: 97.438
    - type: recall_at_3
      value: 42.434
    - type: recall_at_5
      value: 51.745
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
      value: 92.05426356589147
    - type: f1
      value: 91.88068588063942
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
      value: 73.23985408116735
    - type: f1
      value: 55.858906745287506
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
      value: 72.21923335574984
    - type: f1
      value: 70.0174116204253
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
      value: 75.77673167451245
    - type: f1
      value: 75.44811354778666
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
      value: 31.340414710728737
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
      value: 28.196676760061578
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
      value: 29.564149683482206
    - type: mrr
      value: 30.28995474250486
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
      value: 5.93
    - type: map_at_10
      value: 12.828000000000001
    - type: map_at_100
      value: 15.501000000000001
    - type: map_at_1000
      value: 16.791
    - type: map_at_3
      value: 9.727
    - type: map_at_5
      value: 11.318999999999999
    - type: mrr_at_1
      value: 47.678
    - type: mrr_at_10
      value: 55.893
    - type: mrr_at_100
      value: 56.491
    - type: mrr_at_1000
      value: 56.53
    - type: mrr_at_3
      value: 54.386
    - type: mrr_at_5
      value: 55.516
    - type: ndcg_at_1
      value: 45.975
    - type: ndcg_at_10
      value: 33.928999999999995
    - type: ndcg_at_100
      value: 30.164
    - type: ndcg_at_1000
      value: 38.756
    - type: ndcg_at_3
      value: 41.077000000000005
    - type: ndcg_at_5
      value: 38.415
    - type: precision_at_1
      value: 47.678
    - type: precision_at_10
      value: 24.365000000000002
    - type: precision_at_100
      value: 7.344
    - type: precision_at_1000
      value: 1.994
    - type: precision_at_3
      value: 38.184000000000005
    - type: precision_at_5
      value: 33.003
    - type: recall_at_1
      value: 5.93
    - type: recall_at_10
      value: 16.239
    - type: recall_at_100
      value: 28.782999999999998
    - type: recall_at_1000
      value: 60.11
    - type: recall_at_3
      value: 10.700999999999999
    - type: recall_at_5
      value: 13.584
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
      value: 36.163000000000004
    - type: map_at_10
      value: 51.520999999999994
    - type: map_at_100
      value: 52.449
    - type: map_at_1000
      value: 52.473000000000006
    - type: map_at_3
      value: 47.666
    - type: map_at_5
      value: 50.043000000000006
    - type: mrr_at_1
      value: 40.266999999999996
    - type: mrr_at_10
      value: 54.074
    - type: mrr_at_100
      value: 54.722
    - type: mrr_at_1000
      value: 54.739000000000004
    - type: mrr_at_3
      value: 51.043000000000006
    - type: mrr_at_5
      value: 52.956
    - type: ndcg_at_1
      value: 40.238
    - type: ndcg_at_10
      value: 58.73199999999999
    - type: ndcg_at_100
      value: 62.470000000000006
    - type: ndcg_at_1000
      value: 63.083999999999996
    - type: ndcg_at_3
      value: 51.672
    - type: ndcg_at_5
      value: 55.564
    - type: precision_at_1
      value: 40.238
    - type: precision_at_10
      value: 9.279
    - type: precision_at_100
      value: 1.139
    - type: precision_at_1000
      value: 0.12
    - type: precision_at_3
      value: 23.078000000000003
    - type: precision_at_5
      value: 16.176
    - type: recall_at_1
      value: 36.163000000000004
    - type: recall_at_10
      value: 77.88199999999999
    - type: recall_at_100
      value: 93.83399999999999
    - type: recall_at_1000
      value: 98.465
    - type: recall_at_3
      value: 59.857000000000006
    - type: recall_at_5
      value: 68.73599999999999
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
      value: 70.344
    - type: map_at_10
      value: 83.907
    - type: map_at_100
      value: 84.536
    - type: map_at_1000
      value: 84.557
    - type: map_at_3
      value: 80.984
    - type: map_at_5
      value: 82.844
    - type: mrr_at_1
      value: 81.02000000000001
    - type: mrr_at_10
      value: 87.158
    - type: mrr_at_100
      value: 87.268
    - type: mrr_at_1000
      value: 87.26899999999999
    - type: mrr_at_3
      value: 86.17
    - type: mrr_at_5
      value: 86.87
    - type: ndcg_at_1
      value: 81.02000000000001
    - type: ndcg_at_10
      value: 87.70700000000001
    - type: ndcg_at_100
      value: 89.004
    - type: ndcg_at_1000
      value: 89.139
    - type: ndcg_at_3
      value: 84.841
    - type: ndcg_at_5
      value: 86.455
    - type: precision_at_1
      value: 81.02000000000001
    - type: precision_at_10
      value: 13.248999999999999
    - type: precision_at_100
      value: 1.516
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 36.963
    - type: precision_at_5
      value: 24.33
    - type: recall_at_1
      value: 70.344
    - type: recall_at_10
      value: 94.75099999999999
    - type: recall_at_100
      value: 99.30499999999999
    - type: recall_at_1000
      value: 99.928
    - type: recall_at_3
      value: 86.506
    - type: recall_at_5
      value: 91.083
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
      value: 42.873718018378305
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
      value: 56.39477366450528
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
      value: 3.868
    - type: map_at_10
      value: 9.611
    - type: map_at_100
      value: 11.087
    - type: map_at_1000
      value: 11.332
    - type: map_at_3
      value: 6.813
    - type: map_at_5
      value: 8.233
    - type: mrr_at_1
      value: 19
    - type: mrr_at_10
      value: 28.457
    - type: mrr_at_100
      value: 29.613
    - type: mrr_at_1000
      value: 29.695
    - type: mrr_at_3
      value: 25.55
    - type: mrr_at_5
      value: 27.29
    - type: ndcg_at_1
      value: 19
    - type: ndcg_at_10
      value: 16.419
    - type: ndcg_at_100
      value: 22.817999999999998
    - type: ndcg_at_1000
      value: 27.72
    - type: ndcg_at_3
      value: 15.379000000000001
    - type: ndcg_at_5
      value: 13.645
    - type: precision_at_1
      value: 19
    - type: precision_at_10
      value: 8.540000000000001
    - type: precision_at_100
      value: 1.7819999999999998
    - type: precision_at_1000
      value: 0.297
    - type: precision_at_3
      value: 14.267
    - type: precision_at_5
      value: 12.04
    - type: recall_at_1
      value: 3.868
    - type: recall_at_10
      value: 17.288
    - type: recall_at_100
      value: 36.144999999999996
    - type: recall_at_1000
      value: 60.199999999999996
    - type: recall_at_3
      value: 8.688
    - type: recall_at_5
      value: 12.198
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
      value: 83.96614722598582
    - type: cos_sim_spearman
      value: 78.9003023008781
    - type: euclidean_pearson
      value: 81.01829384436505
    - type: euclidean_spearman
      value: 78.93248416788914
    - type: manhattan_pearson
      value: 81.1665428926402
    - type: manhattan_spearman
      value: 78.93264116287453
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
      value: 83.54613363895993
    - type: cos_sim_spearman
      value: 75.1883451602451
    - type: euclidean_pearson
      value: 79.70320886899894
    - type: euclidean_spearman
      value: 74.5917140136796
    - type: manhattan_pearson
      value: 79.82157067185999
    - type: manhattan_spearman
      value: 74.74185720594735
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
      value: 81.30430156721782
    - type: cos_sim_spearman
      value: 81.79962989974364
    - type: euclidean_pearson
      value: 80.89058823224924
    - type: euclidean_spearman
      value: 81.35929372984597
    - type: manhattan_pearson
      value: 81.12204370487478
    - type: manhattan_spearman
      value: 81.6248963282232
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
      value: 81.13064504403134
    - type: cos_sim_spearman
      value: 78.48371403924872
    - type: euclidean_pearson
      value: 80.16794919665591
    - type: euclidean_spearman
      value: 78.29216082221699
    - type: manhattan_pearson
      value: 80.22308565207301
    - type: manhattan_spearman
      value: 78.37829229948022
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
      value: 86.52918899541099
    - type: cos_sim_spearman
      value: 87.49276894673142
    - type: euclidean_pearson
      value: 86.77440570164254
    - type: euclidean_spearman
      value: 87.5753295736756
    - type: manhattan_pearson
      value: 86.86098573892133
    - type: manhattan_spearman
      value: 87.65848591821947
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
      value: 82.86805307244882
    - type: cos_sim_spearman
      value: 84.58066253757511
    - type: euclidean_pearson
      value: 84.38377000876991
    - type: euclidean_spearman
      value: 85.1837278784528
    - type: manhattan_pearson
      value: 84.41903291363842
    - type: manhattan_spearman
      value: 85.19023736251052
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
      value: 86.77218560282436
    - type: cos_sim_spearman
      value: 87.94243515296604
    - type: euclidean_pearson
      value: 88.22800939214864
    - type: euclidean_spearman
      value: 87.91106839439841
    - type: manhattan_pearson
      value: 88.17063269848741
    - type: manhattan_spearman
      value: 87.72751904126062
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
      value: 60.40731554300387
    - type: cos_sim_spearman
      value: 63.76300532966479
    - type: euclidean_pearson
      value: 62.94727878229085
    - type: euclidean_spearman
      value: 63.678039531461216
    - type: manhattan_pearson
      value: 63.00661039863549
    - type: manhattan_spearman
      value: 63.6282591984376
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
      value: 84.92731569745344
    - type: cos_sim_spearman
      value: 86.36336704300167
    - type: euclidean_pearson
      value: 86.09122224841195
    - type: euclidean_spearman
      value: 86.2116149319238
    - type: manhattan_pearson
      value: 86.07879456717032
    - type: manhattan_spearman
      value: 86.2022069635119
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
      value: 79.75976311752326
    - type: mrr
      value: 94.15782837351466
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
      value: 51.193999999999996
    - type: map_at_10
      value: 61.224999999999994
    - type: map_at_100
      value: 62.031000000000006
    - type: map_at_1000
      value: 62.066
    - type: map_at_3
      value: 59.269000000000005
    - type: map_at_5
      value: 60.159
    - type: mrr_at_1
      value: 53.667
    - type: mrr_at_10
      value: 62.74999999999999
    - type: mrr_at_100
      value: 63.39399999999999
    - type: mrr_at_1000
      value: 63.425
    - type: mrr_at_3
      value: 61.389
    - type: mrr_at_5
      value: 61.989000000000004
    - type: ndcg_at_1
      value: 53.667
    - type: ndcg_at_10
      value: 65.596
    - type: ndcg_at_100
      value: 68.906
    - type: ndcg_at_1000
      value: 69.78999999999999
    - type: ndcg_at_3
      value: 62.261
    - type: ndcg_at_5
      value: 63.453
    - type: precision_at_1
      value: 53.667
    - type: precision_at_10
      value: 8.667
    - type: precision_at_100
      value: 1.04
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: precision_at_3
      value: 24.556
    - type: precision_at_5
      value: 15.6
    - type: recall_at_1
      value: 51.193999999999996
    - type: recall_at_10
      value: 77.156
    - type: recall_at_100
      value: 91.43299999999999
    - type: recall_at_1000
      value: 98.333
    - type: recall_at_3
      value: 67.994
    - type: recall_at_5
      value: 71.14399999999999
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
      value: 99.81485148514851
    - type: cos_sim_ap
      value: 95.28896513388551
    - type: cos_sim_f1
      value: 90.43478260869566
    - type: cos_sim_precision
      value: 92.56544502617801
    - type: cos_sim_recall
      value: 88.4
    - type: dot_accuracy
      value: 99.30594059405941
    - type: dot_ap
      value: 61.6432597455472
    - type: dot_f1
      value: 59.46481665014866
    - type: dot_precision
      value: 58.93909626719057
    - type: dot_recall
      value: 60
    - type: euclidean_accuracy
      value: 99.81980198019802
    - type: euclidean_ap
      value: 95.21411049527
    - type: euclidean_f1
      value: 91.06090373280944
    - type: euclidean_precision
      value: 89.47876447876449
    - type: euclidean_recall
      value: 92.7
    - type: manhattan_accuracy
      value: 99.81782178217821
    - type: manhattan_ap
      value: 95.32449994414968
    - type: manhattan_f1
      value: 90.86395233366436
    - type: manhattan_precision
      value: 90.23668639053254
    - type: manhattan_recall
      value: 91.5
    - type: max_accuracy
      value: 99.81980198019802
    - type: max_ap
      value: 95.32449994414968
    - type: max_f1
      value: 91.06090373280944
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
      value: 59.08045614613064
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
      value: 30.297802606804748
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
      value: 49.12801740706292
    - type: mrr
      value: 50.05592956879722
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
      value: 31.523347880124497
    - type: cos_sim_spearman
      value: 31.388214436391014
    - type: dot_pearson
      value: 24.55403435439901
    - type: dot_spearman
      value: 23.50153210841191
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
      value: 0.243
    - type: map_at_10
      value: 1.886
    - type: map_at_100
      value: 10.040000000000001
    - type: map_at_1000
      value: 23.768
    - type: map_at_3
      value: 0.674
    - type: map_at_5
      value: 1.079
    - type: mrr_at_1
      value: 88
    - type: mrr_at_10
      value: 93.667
    - type: mrr_at_100
      value: 93.667
    - type: mrr_at_1000
      value: 93.667
    - type: mrr_at_3
      value: 93.667
    - type: mrr_at_5
      value: 93.667
    - type: ndcg_at_1
      value: 83
    - type: ndcg_at_10
      value: 76.777
    - type: ndcg_at_100
      value: 55.153
    - type: ndcg_at_1000
      value: 47.912
    - type: ndcg_at_3
      value: 81.358
    - type: ndcg_at_5
      value: 80.74799999999999
    - type: precision_at_1
      value: 88
    - type: precision_at_10
      value: 80.80000000000001
    - type: precision_at_100
      value: 56.02
    - type: precision_at_1000
      value: 21.51
    - type: precision_at_3
      value: 86
    - type: precision_at_5
      value: 86
    - type: recall_at_1
      value: 0.243
    - type: recall_at_10
      value: 2.0869999999999997
    - type: recall_at_100
      value: 13.014000000000001
    - type: recall_at_1000
      value: 44.433
    - type: recall_at_3
      value: 0.6910000000000001
    - type: recall_at_5
      value: 1.1440000000000001
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
      value: 3.066
    - type: map_at_10
      value: 10.615
    - type: map_at_100
      value: 16.463
    - type: map_at_1000
      value: 17.815
    - type: map_at_3
      value: 5.7860000000000005
    - type: map_at_5
      value: 7.353999999999999
    - type: mrr_at_1
      value: 38.775999999999996
    - type: mrr_at_10
      value: 53.846000000000004
    - type: mrr_at_100
      value: 54.37
    - type: mrr_at_1000
      value: 54.37
    - type: mrr_at_3
      value: 48.980000000000004
    - type: mrr_at_5
      value: 51.735
    - type: ndcg_at_1
      value: 34.694
    - type: ndcg_at_10
      value: 26.811
    - type: ndcg_at_100
      value: 37.342999999999996
    - type: ndcg_at_1000
      value: 47.964
    - type: ndcg_at_3
      value: 30.906
    - type: ndcg_at_5
      value: 27.77
    - type: precision_at_1
      value: 38.775999999999996
    - type: precision_at_10
      value: 23.878
    - type: precision_at_100
      value: 7.632999999999999
    - type: precision_at_1000
      value: 1.469
    - type: precision_at_3
      value: 31.973000000000003
    - type: precision_at_5
      value: 26.939
    - type: recall_at_1
      value: 3.066
    - type: recall_at_10
      value: 17.112
    - type: recall_at_100
      value: 47.723
    - type: recall_at_1000
      value: 79.50500000000001
    - type: recall_at_3
      value: 6.825
    - type: recall_at_5
      value: 9.584
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
      value: 72.76460000000002
    - type: ap
      value: 14.944240012137053
    - type: f1
      value: 55.89805777266571
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
      value: 63.30503678551217
    - type: f1
      value: 63.57492701921179
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
      value: 37.51066495006874
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
      value: 86.07021517553794
    - type: cos_sim_ap
      value: 74.15520712370555
    - type: cos_sim_f1
      value: 68.64321608040201
    - type: cos_sim_precision
      value: 65.51558752997602
    - type: cos_sim_recall
      value: 72.0844327176781
    - type: dot_accuracy
      value: 80.23484532395541
    - type: dot_ap
      value: 54.298763810214176
    - type: dot_f1
      value: 53.22254659779924
    - type: dot_precision
      value: 46.32525410476936
    - type: dot_recall
      value: 62.532981530343015
    - type: euclidean_accuracy
      value: 86.04637301066937
    - type: euclidean_ap
      value: 73.85333854233123
    - type: euclidean_f1
      value: 68.77723660599845
    - type: euclidean_precision
      value: 66.87437686939182
    - type: euclidean_recall
      value: 70.79155672823218
    - type: manhattan_accuracy
      value: 85.98676759849795
    - type: manhattan_ap
      value: 73.56016090035973
    - type: manhattan_f1
      value: 68.48878539036647
    - type: manhattan_precision
      value: 63.9505607690547
    - type: manhattan_recall
      value: 73.7203166226913
    - type: max_accuracy
      value: 86.07021517553794
    - type: max_ap
      value: 74.15520712370555
    - type: max_f1
      value: 68.77723660599845
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
      value: 88.92769821865176
    - type: cos_sim_ap
      value: 85.78879502899773
    - type: cos_sim_f1
      value: 78.14414083990464
    - type: cos_sim_precision
      value: 74.61651607480563
    - type: cos_sim_recall
      value: 82.0218663381583
    - type: dot_accuracy
      value: 84.95750378390964
    - type: dot_ap
      value: 75.80219641857563
    - type: dot_f1
      value: 70.13966179585681
    - type: dot_precision
      value: 65.71140262361251
    - type: dot_recall
      value: 75.20788420080073
    - type: euclidean_accuracy
      value: 88.93546008460433
    - type: euclidean_ap
      value: 85.72056428301667
    - type: euclidean_f1
      value: 78.14387902598124
    - type: euclidean_precision
      value: 75.3376688344172
    - type: euclidean_recall
      value: 81.16723129042192
    - type: manhattan_accuracy
      value: 88.96262661543835
    - type: manhattan_ap
      value: 85.76605136314335
    - type: manhattan_f1
      value: 78.26696165191743
    - type: manhattan_precision
      value: 75.0990659496179
    - type: manhattan_recall
      value: 81.71388974437943
    - type: max_accuracy
      value: 88.96262661543835
    - type: max_ap
      value: 85.78879502899773
    - type: max_f1
      value: 78.26696165191743
language:
- en
license: mit
---

# E5-small

**News (May 2023): please switch to [e5-small-v2](https://huggingface.co/intfloat/e5-small-v2), which has better performance and same method of usage.**

[Text Embeddings by Weakly-Supervised Contrastive Pre-training](https://arxiv.org/pdf/2212.03533.pdf).
Liang Wang, Nan Yang, Xiaolong Huang, Binxing Jiao, Linjun Yang, Daxin Jiang, Rangan Majumder, Furu Wei, arXiv 2022

This model has 12 layers and the embedding size is 384.

## Usage

Below is an example to encode queries and passages from the MS-MARCO passage ranking dataset.

```python
import torch.nn.functional as F

from torch import Tensor
from transformers import AutoTokenizer, AutoModel


def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]


# Each input text should start with "query: " or "passage: ".
# For tasks other than retrieval, you can simply use the "query: " prefix.
input_texts = ['query: how much protein should a female eat',
               'query: summit define',
               "passage: As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 is 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or training for a marathon. Check out the chart below to see how much protein you should be eating each day.",
               "passage: Definition of summit for English Language Learners. : 1  the highest point of a mountain : the top of a mountain. : 2  the highest level. : 3  a meeting or series of meetings between the leaders of two or more governments."]

tokenizer = AutoTokenizer.from_pretrained('intfloat/e5-small')
model = AutoModel.from_pretrained('intfloat/e5-small')

# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt')

outputs = model(**batch_dict)
embeddings = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

# normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:2] @ embeddings[2:].T) * 100
print(scores.tolist())
```

## Training Details

Please refer to our paper at [https://arxiv.org/pdf/2212.03533.pdf](https://arxiv.org/pdf/2212.03533.pdf).

## Benchmark Evaluation

Check out [unilm/e5](https://github.com/microsoft/unilm/tree/master/e5) to reproduce evaluation results 
on the [BEIR](https://arxiv.org/abs/2104.08663) and [MTEB benchmark](https://arxiv.org/abs/2210.07316).

## Support for Sentence Transformers

Below is an example for usage with sentence_transformers.
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('intfloat/e5-small')
input_texts = [
    'query: how much protein should a female eat',
    'query: summit define',
    "passage: As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 is 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or training for a marathon. Check out the chart below to see how much protein you should be eating each day.",
    "passage: Definition of summit for English Language Learners. : 1  the highest point of a mountain : the top of a mountain. : 2  the highest level. : 3  a meeting or series of meetings between the leaders of two or more governments."
]
embeddings = model.encode(input_texts, normalize_embeddings=True)
```

Package requirements

`pip install sentence_transformers~=2.2.2`

Contributors: [michaelfeil](https://huggingface.co/michaelfeil)

## FAQ

**1. Do I need to add the prefix "query: " and "passage: " to input texts?**

Yes, this is how the model is trained, otherwise you will see a performance degradation.

Here are some rules of thumb:
- Use "query: " and "passage: " correspondingly for asymmetric tasks such as passage retrieval in open QA, ad-hoc information retrieval.

- Use "query: " prefix for symmetric tasks such as semantic similarity, paraphrase retrieval.

- Use "query: " prefix if you want to use embeddings as features, such as linear probing classification, clustering.

**2. Why are my reproduced results slightly different from reported in the model card?**

Different versions of `transformers` and `pytorch` could cause negligible but non-zero performance differences.

**3. Why does the cosine similarity scores distribute around 0.7 to 1.0?**

This is a known and expected behavior as we use a low temperature 0.01 for InfoNCE contrastive loss. 

For text embedding tasks like text retrieval or semantic similarity, 
what matters is the relative order of the scores instead of the absolute values, 
so this should not be an issue.

## Citation

If you find our paper or models helpful, please consider cite as follows:

```
@article{wang2022text,
  title={Text Embeddings by Weakly-Supervised Contrastive Pre-training},
  author={Wang, Liang and Yang, Nan and Huang, Xiaolong and Jiao, Binxing and Yang, Linjun and Jiang, Daxin and Majumder, Rangan and Wei, Furu},
  journal={arXiv preprint arXiv:2212.03533},
  year={2022}
}
```

## Limitations

This model only works for English texts. Long texts will be truncated to at most 512 tokens.
