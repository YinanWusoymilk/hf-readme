---
tags:
- mteb
- sentence-transformers
- transformers
model-index:
- name: SFR-Embedding-Mistral
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
      value: 77.92537313432834
    - type: ap
      value: 40.86767661556651
    - type: f1
      value: 71.65758897929837
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
      value: 95.967
    - type: ap
      value: 94.46300829592593
    - type: f1
      value: 95.96507173189292
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
      value: 54.352000000000004
    - type: f1
      value: 53.636682615380174
  - task:
      type: Retrieval
    dataset:
      type: arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 43.314
    - type: ndcg_at_2
      value: 54.757
    - type: ndcg_at_3
      value: 58.84700000000001
    - type: ndcg_at_5
      value: 63.634
    - type: ndcg_at_7
      value: 65.741
    - type: ndcg_at_10
      value: 67.171
    - type: ndcg_at_20
      value: 68.585
    - type: ndcg_at_30
      value: 68.81
    - type: ndcg_at_50
      value: 68.932
    - type: ndcg_at_70
      value: 68.992
    - type: ndcg_at_100
      value: 69.014
    - type: ndcg_at_200
      value: 69.014
    - type: ndcg_at_300
      value: 69.014
    - type: ndcg_at_500
      value: 69.014
    - type: ndcg_at_700
      value: 69.014
    - type: ndcg_at_1000
      value: 69.014
    - type: map_at_1
      value: 43.314
    - type: map_at_2
      value: 52.383
    - type: map_at_3
      value: 55.108999999999995
    - type: map_at_5
      value: 57.772999999999996
    - type: map_at_7
      value: 58.718
    - type: map_at_10
      value: 59.256
    - type: map_at_20
      value: 59.668
    - type: map_at_30
      value: 59.709999999999994
    - type: map_at_50
      value: 59.727
    - type: map_at_70
      value: 59.733999999999995
    - type: map_at_100
      value: 59.73500000000001
    - type: map_at_200
      value: 59.73500000000001
    - type: map_at_300
      value: 59.73500000000001
    - type: map_at_500
      value: 59.73500000000001
    - type: map_at_700
      value: 59.73500000000001
    - type: map_at_1000
      value: 59.73500000000001
    - type: recall_at_1
      value: 43.314
    - type: recall_at_2
      value: 61.451
    - type: recall_at_3
      value: 69.63000000000001
    - type: recall_at_5
      value: 81.223
    - type: recall_at_7
      value: 87.33999999999999
    - type: recall_at_10
      value: 92.034
    - type: recall_at_20
      value: 97.44
    - type: recall_at_30
      value: 98.506
    - type: recall_at_50
      value: 99.14699999999999
    - type: recall_at_70
      value: 99.502
    - type: recall_at_100
      value: 99.644
    - type: recall_at_200
      value: 99.644
    - type: recall_at_300
      value: 99.644
    - type: recall_at_500
      value: 99.644
    - type: recall_at_700
      value: 99.644
    - type: recall_at_1000
      value: 99.644
    - type: precision_at_1
      value: 43.314
    - type: precision_at_2
      value: 30.725
    - type: precision_at_3
      value: 23.21
    - type: precision_at_5
      value: 16.245
    - type: precision_at_7
      value: 12.477
    - type: precision_at_10
      value: 9.203
    - type: precision_at_20
      value: 4.872
    - type: precision_at_30
      value: 3.2840000000000003
    - type: precision_at_50
      value: 1.983
    - type: precision_at_70
      value: 1.421
    - type: precision_at_100
      value: 0.996
    - type: precision_at_200
      value: 0.498
    - type: precision_at_300
      value: 0.332
    - type: precision_at_500
      value: 0.199
    - type: precision_at_700
      value: 0.14200000000000002
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 44.666
    - type: mrr_at_2
      value: 52.418
    - type: mrr_at_3
      value: 55.595000000000006
    - type: mrr_at_5
      value: 58.205
    - type: mrr_at_7
      value: 59.202999999999996
    - type: mrr_at_10
      value: 59.727
    - type: mrr_at_20
      value: 60.133
    - type: mrr_at_30
      value: 60.178
    - type: mrr_at_50
      value: 60.192
    - type: mrr_at_70
      value: 60.19799999999999
    - type: mrr_at_100
      value: 60.199999999999996
    - type: mrr_at_200
      value: 60.199999999999996
    - type: mrr_at_300
      value: 60.199999999999996
    - type: mrr_at_500
      value: 60.199999999999996
    - type: mrr_at_700
      value: 60.199999999999996
    - type: mrr_at_1000
      value: 60.199999999999996
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
      value: 52.07508593014336
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
      value: 47.381339333240675
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
      value: 67.58376647859171
    - type: mrr
      value: 80.56885635140483
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
      value: 88.40107280274783
    - type: cos_sim_spearman
      value: 86.07003345325681
    - type: euclidean_pearson
      value: 87.1726034325395
    - type: euclidean_spearman
      value: 86.07003345325681
    - type: manhattan_pearson
      value: 87.25660625029772
    - type: manhattan_spearman
      value: 86.3808839096893
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
      value: 88.81168831168831
    - type: f1
      value: 88.76514496560141
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
      value: 43.9382520874344
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
      value: 41.14351847240913
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 34.51166666666667
    - type: ndcg_at_2
      value: 38.51591666666667
    - type: ndcg_at_3
      value: 40.95083333333333
    - type: ndcg_at_5
      value: 43.580666666666666
    - type: ndcg_at_7
      value: 45.0625
    - type: ndcg_at_10
      value: 46.49083333333333
    - type: ndcg_at_20
      value: 48.731333333333325
    - type: ndcg_at_30
      value: 49.78666666666667
    - type: ndcg_at_50
      value: 50.84049999999999
    - type: ndcg_at_70
      value: 51.393750000000004
    - type: ndcg_at_100
      value: 51.883333333333326
    - type: ndcg_at_200
      value: 52.65225
    - type: ndcg_at_300
      value: 52.98241666666669
    - type: ndcg_at_500
      value: 53.28541666666668
    - type: ndcg_at_700
      value: 53.49241666666668
    - type: ndcg_at_1000
      value: 53.63758333333334
    - type: map_at_1
      value: 29.10075
    - type: map_at_2
      value: 34.636500000000005
    - type: map_at_3
      value: 36.92033333333333
    - type: map_at_5
      value: 38.81641666666666
    - type: map_at_7
      value: 39.635416666666664
    - type: map_at_10
      value: 40.294583333333335
    - type: map_at_20
      value: 41.07574999999999
    - type: map_at_30
      value: 41.333
    - type: map_at_50
      value: 41.529333333333334
    - type: map_at_70
      value: 41.606833333333334
    - type: map_at_100
      value: 41.66224999999999
    - type: map_at_200
      value: 41.72691666666666
    - type: map_at_300
      value: 41.746583333333334
    - type: map_at_500
      value: 41.75983333333333
    - type: map_at_700
      value: 41.76558333333333
    - type: map_at_1000
      value: 41.769000000000005
    - type: recall_at_1
      value: 29.10075
    - type: recall_at_2
      value: 39.07658333333333
    - type: recall_at_3
      value: 44.93591666666667
    - type: recall_at_5
      value: 51.66883333333333
    - type: recall_at_7
      value: 55.881000000000014
    - type: recall_at_10
      value: 60.34691666666667
    - type: recall_at_20
      value: 68.44016666666667
    - type: recall_at_30
      value: 72.90766666666667
    - type: recall_at_50
      value: 77.843
    - type: recall_at_70
      value: 80.70366666666668
    - type: recall_at_100
      value: 83.42866666666667
    - type: recall_at_200
      value: 88.06816666666668
    - type: recall_at_300
      value: 90.249
    - type: recall_at_500
      value: 92.37616666666668
    - type: recall_at_700
      value: 93.978
    - type: recall_at_1000
      value: 95.12791666666666
    - type: precision_at_1
      value: 34.51166666666667
    - type: precision_at_2
      value: 24.326333333333327
    - type: precision_at_3
      value: 19.099249999999998
    - type: precision_at_5
      value: 13.672666666666666
    - type: precision_at_7
      value: 10.772
    - type: precision_at_10
      value: 8.302166666666668
    - type: precision_at_20
      value: 4.8960833333333325
    - type: precision_at_30
      value: 3.551083333333333
    - type: precision_at_50
      value: 2.3386666666666662
    - type: precision_at_70
      value: 1.7605833333333334
    - type: precision_at_100
      value: 1.2965
    - type: precision_at_200
      value: 0.7106666666666668
    - type: precision_at_300
      value: 0.4955
    - type: precision_at_500
      value: 0.3106666666666667
    - type: precision_at_700
      value: 0.22791666666666668
    - type: precision_at_1000
      value: 0.1635833333333333
    - type: mrr_at_1
      value: 34.51166666666667
    - type: mrr_at_2
      value: 39.954249999999995
    - type: mrr_at_3
      value: 41.93741666666668
    - type: mrr_at_5
      value: 43.487166666666674
    - type: mrr_at_7
      value: 44.14983333333333
    - type: mrr_at_10
      value: 44.62766666666666
    - type: mrr_at_20
      value: 45.15291666666668
    - type: mrr_at_30
      value: 45.317
    - type: mrr_at_50
      value: 45.42875
    - type: mrr_at_70
      value: 45.46966666666667
    - type: mrr_at_100
      value: 45.49716666666667
    - type: mrr_at_200
      value: 45.525166666666664
    - type: mrr_at_300
      value: 45.53233333333335
    - type: mrr_at_500
      value: 45.5365
    - type: mrr_at_700
      value: 45.538583333333335
    - type: mrr_at_1000
      value: 45.539583333333326
  - task:
      type: Retrieval
    dataset:
      type: climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 35.179
    - type: ndcg_at_2
      value: 31.243
    - type: ndcg_at_3
      value: 30.562
    - type: ndcg_at_5
      value: 32.409
    - type: ndcg_at_7
      value: 34.525
    - type: ndcg_at_10
      value: 36.415
    - type: ndcg_at_20
      value: 39.443
    - type: ndcg_at_30
      value: 40.796
    - type: ndcg_at_50
      value: 42.16
    - type: ndcg_at_70
      value: 42.971
    - type: ndcg_at_100
      value: 43.691
    - type: ndcg_at_200
      value: 45.004
    - type: ndcg_at_300
      value: 45.527
    - type: ndcg_at_500
      value: 46.072
    - type: ndcg_at_700
      value: 46.387
    - type: ndcg_at_1000
      value: 46.663
    - type: map_at_1
      value: 15.692
    - type: map_at_2
      value: 20.116
    - type: map_at_3
      value: 22.6
    - type: map_at_5
      value: 24.701
    - type: map_at_7
      value: 25.934
    - type: map_at_10
      value: 26.843
    - type: map_at_20
      value: 27.975
    - type: map_at_30
      value: 28.372000000000003
    - type: map_at_50
      value: 28.671000000000003
    - type: map_at_70
      value: 28.803
    - type: map_at_100
      value: 28.895
    - type: map_at_200
      value: 29.011
    - type: map_at_300
      value: 29.042
    - type: map_at_500
      value: 29.065
    - type: map_at_700
      value: 29.075
    - type: map_at_1000
      value: 29.081000000000003
    - type: recall_at_1
      value: 15.692
    - type: recall_at_2
      value: 22.602
    - type: recall_at_3
      value: 27.814
    - type: recall_at_5
      value: 33.756
    - type: recall_at_7
      value: 38.073
    - type: recall_at_10
      value: 42.553000000000004
    - type: recall_at_20
      value: 51.121
    - type: recall_at_30
      value: 55.523999999999994
    - type: recall_at_50
      value: 60.586
    - type: recall_at_70
      value: 63.94
    - type: recall_at_100
      value: 67.134
    - type: recall_at_200
      value: 73.543
    - type: recall_at_300
      value: 76.372
    - type: recall_at_500
      value: 79.60199999999999
    - type: recall_at_700
      value: 81.536
    - type: recall_at_1000
      value: 83.37400000000001
    - type: precision_at_1
      value: 35.179
    - type: precision_at_2
      value: 27.199
    - type: precision_at_3
      value: 22.953000000000003
    - type: precision_at_5
      value: 17.224999999999998
    - type: precision_at_7
      value: 14.238999999999999
    - type: precision_at_10
      value: 11.303
    - type: precision_at_20
      value: 6.954000000000001
    - type: precision_at_30
      value: 5.116
    - type: precision_at_50
      value: 3.395
    - type: precision_at_70
      value: 2.579
    - type: precision_at_100
      value: 1.9109999999999998
    - type: precision_at_200
      value: 1.065
    - type: precision_at_300
      value: 0.743
    - type: precision_at_500
      value: 0.46699999999999997
    - type: precision_at_700
      value: 0.344
    - type: precision_at_1000
      value: 0.247
    - type: mrr_at_1
      value: 35.179
    - type: mrr_at_2
      value: 41.792
    - type: mrr_at_3
      value: 44.484
    - type: mrr_at_5
      value: 46.39
    - type: mrr_at_7
      value: 47.125
    - type: mrr_at_10
      value: 47.711999999999996
    - type: mrr_at_20
      value: 48.214
    - type: mrr_at_30
      value: 48.325
    - type: mrr_at_50
      value: 48.392
    - type: mrr_at_70
      value: 48.418
    - type: mrr_at_100
      value: 48.44
    - type: mrr_at_200
      value: 48.46
    - type: mrr_at_300
      value: 48.461999999999996
    - type: mrr_at_500
      value: 48.466
    - type: mrr_at_700
      value: 48.466
    - type: mrr_at_1000
      value: 48.467
  - task:
      type: Retrieval
    dataset:
      type: dbpedia-entity
      name: MTEB DBPedia
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 62.375
    - type: ndcg_at_2
      value: 56.286
    - type: ndcg_at_3
      value: 53.665
    - type: ndcg_at_5
      value: 51.139
    - type: ndcg_at_7
      value: 49.873
    - type: ndcg_at_10
      value: 49.056
    - type: ndcg_at_20
      value: 48.783
    - type: ndcg_at_30
      value: 49.166
    - type: ndcg_at_50
      value: 51.141999999999996
    - type: ndcg_at_70
      value: 52.774
    - type: ndcg_at_100
      value: 54.403
    - type: ndcg_at_200
      value: 57.419
    - type: ndcg_at_300
      value: 58.778
    - type: ndcg_at_500
      value: 60.228
    - type: ndcg_at_700
      value: 61.07599999999999
    - type: ndcg_at_1000
      value: 61.846000000000004
    - type: map_at_1
      value: 10.359
    - type: map_at_2
      value: 14.446
    - type: map_at_3
      value: 16.689
    - type: map_at_5
      value: 20.096
    - type: map_at_7
      value: 22.247
    - type: map_at_10
      value: 24.468999999999998
    - type: map_at_20
      value: 28.938000000000002
    - type: map_at_30
      value: 31.134
    - type: map_at_50
      value: 33.403
    - type: map_at_70
      value: 34.486
    - type: map_at_100
      value: 35.337
    - type: map_at_200
      value: 36.364999999999995
    - type: map_at_300
      value: 36.735
    - type: map_at_500
      value: 37.057
    - type: map_at_700
      value: 37.225
    - type: map_at_1000
      value: 37.379
    - type: recall_at_1
      value: 10.359
    - type: recall_at_2
      value: 14.945
    - type: recall_at_3
      value: 17.694
    - type: recall_at_5
      value: 22.677
    - type: recall_at_7
      value: 26.131
    - type: recall_at_10
      value: 30.053
    - type: recall_at_20
      value: 39.518
    - type: recall_at_30
      value: 44.925
    - type: recall_at_50
      value: 52.154
    - type: recall_at_70
      value: 56.729
    - type: recall_at_100
      value: 61.18900000000001
    - type: recall_at_200
      value: 70.407
    - type: recall_at_300
      value: 74.412
    - type: recall_at_500
      value: 78.891
    - type: recall_at_700
      value: 81.74
    - type: recall_at_1000
      value: 84.253
    - type: precision_at_1
      value: 75
    - type: precision_at_2
      value: 64.125
    - type: precision_at_3
      value: 57.833
    - type: precision_at_5
      value: 50.24999999999999
    - type: precision_at_7
      value: 44.75
    - type: precision_at_10
      value: 39.75
    - type: precision_at_20
      value: 30.412
    - type: precision_at_30
      value: 25.141999999999996
    - type: precision_at_50
      value: 19.2
    - type: precision_at_70
      value: 15.729000000000001
    - type: precision_at_100
      value: 12.552
    - type: precision_at_200
      value: 7.866
    - type: precision_at_300
      value: 5.9270000000000005
    - type: precision_at_500
      value: 4.1129999999999995
    - type: precision_at_700
      value: 3.2460000000000004
    - type: precision_at_1000
      value: 2.5260000000000002
    - type: mrr_at_1
      value: 75
    - type: mrr_at_2
      value: 78.625
    - type: mrr_at_3
      value: 79.708
    - type: mrr_at_5
      value: 80.446
    - type: mrr_at_7
      value: 80.862
    - type: mrr_at_10
      value: 81.161
    - type: mrr_at_20
      value: 81.3
    - type: mrr_at_30
      value: 81.348
    - type: mrr_at_50
      value: 81.361
    - type: mrr_at_70
      value: 81.361
    - type: mrr_at_100
      value: 81.361
    - type: mrr_at_200
      value: 81.367
    - type: mrr_at_300
      value: 81.367
    - type: mrr_at_500
      value: 81.368
    - type: mrr_at_700
      value: 81.368
    - type: mrr_at_1000
      value: 81.368
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
      value: 50.239999999999995
    - type: f1
      value: 46.42361822342044
  - task:
      type: Retrieval
    dataset:
      type: fever
      name: MTEB FEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 83.723
    - type: ndcg_at_2
      value: 86.777
    - type: ndcg_at_3
      value: 87.997
    - type: ndcg_at_5
      value: 88.864
    - type: ndcg_at_7
      value: 89.143
    - type: ndcg_at_10
      value: 89.349
    - type: ndcg_at_20
      value: 89.709
    - type: ndcg_at_30
      value: 89.82900000000001
    - type: ndcg_at_50
      value: 89.923
    - type: ndcg_at_70
      value: 89.982
    - type: ndcg_at_100
      value: 90.026
    - type: ndcg_at_200
      value: 90.10000000000001
    - type: ndcg_at_300
      value: 90.12599999999999
    - type: ndcg_at_500
      value: 90.17399999999999
    - type: ndcg_at_700
      value: 90.19
    - type: ndcg_at_1000
      value: 90.208
    - type: map_at_1
      value: 77.64999999999999
    - type: map_at_2
      value: 83.769
    - type: map_at_3
      value: 85.041
    - type: map_at_5
      value: 85.736
    - type: map_at_7
      value: 85.924
    - type: map_at_10
      value: 86.032
    - type: map_at_20
      value: 86.177
    - type: map_at_30
      value: 86.213
    - type: map_at_50
      value: 86.233
    - type: map_at_70
      value: 86.24300000000001
    - type: map_at_100
      value: 86.249
    - type: map_at_200
      value: 86.256
    - type: map_at_300
      value: 86.258
    - type: map_at_500
      value: 86.26
    - type: map_at_700
      value: 86.26
    - type: map_at_1000
      value: 86.261
    - type: recall_at_1
      value: 77.64999999999999
    - type: recall_at_2
      value: 88.53999999999999
    - type: recall_at_3
      value: 91.696
    - type: recall_at_5
      value: 93.916
    - type: recall_at_7
      value: 94.731
    - type: recall_at_10
      value: 95.318
    - type: recall_at_20
      value: 96.507
    - type: recall_at_30
      value: 96.956
    - type: recall_at_50
      value: 97.34899999999999
    - type: recall_at_70
      value: 97.61
    - type: recall_at_100
      value: 97.83
    - type: recall_at_200
      value: 98.223
    - type: recall_at_300
      value: 98.374
    - type: recall_at_500
      value: 98.67899999999999
    - type: recall_at_700
      value: 98.787
    - type: recall_at_1000
      value: 98.919
    - type: precision_at_1
      value: 83.723
    - type: precision_at_2
      value: 48.425000000000004
    - type: precision_at_3
      value: 33.638
    - type: precision_at_5
      value: 20.843
    - type: precision_at_7
      value: 15.079
    - type: precision_at_10
      value: 10.674999999999999
    - type: precision_at_20
      value: 5.457999999999999
    - type: precision_at_30
      value: 3.6740000000000004
    - type: precision_at_50
      value: 2.2239999999999998
    - type: precision_at_70
      value: 1.599
    - type: precision_at_100
      value: 1.125
    - type: precision_at_200
      value: 0.5680000000000001
    - type: precision_at_300
      value: 0.38
    - type: precision_at_500
      value: 0.22999999999999998
    - type: precision_at_700
      value: 0.165
    - type: precision_at_1000
      value: 0.116
    - type: mrr_at_1
      value: 83.723
    - type: mrr_at_2
      value: 88.794
    - type: mrr_at_3
      value: 89.679
    - type: mrr_at_5
      value: 90.049
    - type: mrr_at_7
      value: 90.129
    - type: mrr_at_10
      value: 90.167
    - type: mrr_at_20
      value: 90.208
    - type: mrr_at_30
      value: 90.214
    - type: mrr_at_50
      value: 90.217
    - type: mrr_at_70
      value: 90.218
    - type: mrr_at_100
      value: 90.21900000000001
    - type: mrr_at_200
      value: 90.21900000000001
    - type: mrr_at_300
      value: 90.21900000000001
    - type: mrr_at_500
      value: 90.21900000000001
    - type: mrr_at_700
      value: 90.21900000000001
    - type: mrr_at_1000
      value: 90.21900000000001
  - task:
      type: Retrieval
    dataset:
      type: fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 59.721999999999994
    - type: ndcg_at_2
      value: 56.85
    - type: ndcg_at_3
      value: 56.462999999999994
    - type: ndcg_at_5
      value: 57.75599999999999
    - type: ndcg_at_7
      value: 59.109
    - type: ndcg_at_10
      value: 60.402
    - type: ndcg_at_20
      value: 63.071999999999996
    - type: ndcg_at_30
      value: 64.302
    - type: ndcg_at_50
      value: 65.619
    - type: ndcg_at_70
      value: 66.161
    - type: ndcg_at_100
      value: 66.645
    - type: ndcg_at_200
      value: 67.353
    - type: ndcg_at_300
      value: 67.646
    - type: ndcg_at_500
      value: 67.852
    - type: ndcg_at_700
      value: 67.974
    - type: ndcg_at_1000
      value: 68.084
    - type: map_at_1
      value: 31.56
    - type: map_at_2
      value: 42.093
    - type: map_at_3
      value: 46.177
    - type: map_at_5
      value: 49.78
    - type: map_at_7
      value: 51.410999999999994
    - type: map_at_10
      value: 52.524
    - type: map_at_20
      value: 53.815000000000005
    - type: map_at_30
      value: 54.201
    - type: map_at_50
      value: 54.531
    - type: map_at_70
      value: 54.625
    - type: map_at_100
      value: 54.686
    - type: map_at_200
      value: 54.757999999999996
    - type: map_at_300
      value: 54.776
    - type: map_at_500
      value: 54.786
    - type: map_at_700
      value: 54.790000000000006
    - type: map_at_1000
      value: 54.793000000000006
    - type: recall_at_1
      value: 31.56
    - type: recall_at_2
      value: 44.858
    - type: recall_at_3
      value: 51.11
    - type: recall_at_5
      value: 58.394
    - type: recall_at_7
      value: 63.001
    - type: recall_at_10
      value: 66.81200000000001
    - type: recall_at_20
      value: 74.901
    - type: recall_at_30
      value: 79.218
    - type: recall_at_50
      value: 84.49
    - type: recall_at_70
      value: 87.003
    - type: recall_at_100
      value: 89.345
    - type: recall_at_200
      value: 93.173
    - type: recall_at_300
      value: 94.906
    - type: recall_at_500
      value: 96.223
    - type: recall_at_700
      value: 97.043
    - type: recall_at_1000
      value: 97.785
    - type: precision_at_1
      value: 59.721999999999994
    - type: precision_at_2
      value: 46.682
    - type: precision_at_3
      value: 37.602999999999994
    - type: precision_at_5
      value: 27.500000000000004
    - type: precision_at_7
      value: 21.847
    - type: precision_at_10
      value: 16.667
    - type: precision_at_20
      value: 9.545
    - type: precision_at_30
      value: 6.795
    - type: precision_at_50
      value: 4.38
    - type: precision_at_70
      value: 3.221
    - type: precision_at_100
      value: 2.319
    - type: precision_at_200
      value: 1.2149999999999999
    - type: precision_at_300
      value: 0.827
    - type: precision_at_500
      value: 0.504
    - type: precision_at_700
      value: 0.364
    - type: precision_at_1000
      value: 0.257
    - type: mrr_at_1
      value: 59.721999999999994
    - type: mrr_at_2
      value: 64.506
    - type: mrr_at_3
      value: 65.792
    - type: mrr_at_5
      value: 66.965
    - type: mrr_at_7
      value: 67.34700000000001
    - type: mrr_at_10
      value: 67.57
    - type: mrr_at_20
      value: 67.896
    - type: mrr_at_30
      value: 68.008
    - type: mrr_at_50
      value: 68.083
    - type: mrr_at_70
      value: 68.105
    - type: mrr_at_100
      value: 68.116
    - type: mrr_at_200
      value: 68.12700000000001
    - type: mrr_at_300
      value: 68.13
    - type: mrr_at_500
      value: 68.132
    - type: mrr_at_700
      value: 68.133
    - type: mrr_at_1000
      value: 68.133
  - task:
      type: Retrieval
    dataset:
      type: hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 81.796
    - type: ndcg_at_2
      value: 67.999
    - type: ndcg_at_3
      value: 72.15599999999999
    - type: ndcg_at_5
      value: 74.99900000000001
    - type: ndcg_at_7
      value: 76.179
    - type: ndcg_at_10
      value: 77.022
    - type: ndcg_at_20
      value: 78.173
    - type: ndcg_at_30
      value: 78.648
    - type: ndcg_at_50
      value: 79.104
    - type: ndcg_at_70
      value: 79.335
    - type: ndcg_at_100
      value: 79.56
    - type: ndcg_at_200
      value: 79.911
    - type: ndcg_at_300
      value: 80.045
    - type: ndcg_at_500
      value: 80.19500000000001
    - type: ndcg_at_700
      value: 80.281
    - type: ndcg_at_1000
      value: 80.35
    - type: map_at_1
      value: 40.898
    - type: map_at_2
      value: 62.016000000000005
    - type: map_at_3
      value: 66.121
    - type: map_at_5
      value: 68.471
    - type: map_at_7
      value: 69.261
    - type: map_at_10
      value: 69.738
    - type: map_at_20
      value: 70.208
    - type: map_at_30
      value: 70.343
    - type: map_at_50
      value: 70.43700000000001
    - type: map_at_70
      value: 70.47099999999999
    - type: map_at_100
      value: 70.498
    - type: map_at_200
      value: 70.526
    - type: map_at_300
      value: 70.533
    - type: map_at_500
      value: 70.538
    - type: map_at_700
      value: 70.541
    - type: map_at_1000
      value: 70.542
    - type: recall_at_1
      value: 40.898
    - type: recall_at_2
      value: 63.964
    - type: recall_at_3
      value: 70.743
    - type: recall_at_5
      value: 76.36699999999999
    - type: recall_at_7
      value: 79.142
    - type: recall_at_10
      value: 81.404
    - type: recall_at_20
      value: 85.111
    - type: recall_at_30
      value: 86.92800000000001
    - type: recall_at_50
      value: 88.899
    - type: recall_at_70
      value: 90.01400000000001
    - type: recall_at_100
      value: 91.19500000000001
    - type: recall_at_200
      value: 93.234
    - type: recall_at_300
      value: 94.105
    - type: recall_at_500
      value: 95.159
    - type: recall_at_700
      value: 95.8
    - type: recall_at_1000
      value: 96.34700000000001
    - type: precision_at_1
      value: 81.796
    - type: precision_at_2
      value: 63.964
    - type: precision_at_3
      value: 47.162
    - type: precision_at_5
      value: 30.547
    - type: precision_at_7
      value: 22.612
    - type: precision_at_10
      value: 16.281000000000002
    - type: precision_at_20
      value: 8.511000000000001
    - type: precision_at_30
      value: 5.795
    - type: precision_at_50
      value: 3.556
    - type: precision_at_70
      value: 2.572
    - type: precision_at_100
      value: 1.8239999999999998
    - type: precision_at_200
      value: 0.932
    - type: precision_at_300
      value: 0.627
    - type: precision_at_500
      value: 0.381
    - type: precision_at_700
      value: 0.27399999999999997
    - type: precision_at_1000
      value: 0.193
    - type: mrr_at_1
      value: 81.796
    - type: mrr_at_2
      value: 85.69200000000001
    - type: mrr_at_3
      value: 86.52
    - type: mrr_at_5
      value: 86.973
    - type: mrr_at_7
      value: 87.13300000000001
    - type: mrr_at_10
      value: 87.208
    - type: mrr_at_20
      value: 87.303
    - type: mrr_at_30
      value: 87.32799999999999
    - type: mrr_at_50
      value: 87.347
    - type: mrr_at_70
      value: 87.35199999999999
    - type: mrr_at_100
      value: 87.355
    - type: mrr_at_200
      value: 87.357
    - type: mrr_at_300
      value: 87.357
    - type: mrr_at_500
      value: 87.358
    - type: mrr_at_700
      value: 87.358
    - type: mrr_at_1000
      value: 87.358
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
      value: 94.79200000000002
    - type: ap
      value: 92.54484356773553
    - type: f1
      value: 94.78965313682525
  - task:
      type: Retrieval
    dataset:
      type: msmarco
      name: MTEB MSMARCO
      config: default
      split: dev
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 24.398
    - type: ndcg_at_2
      value: 31.336000000000002
    - type: ndcg_at_3
      value: 35.266999999999996
    - type: ndcg_at_5
      value: 39.356
    - type: ndcg_at_7
      value: 41.562
    - type: ndcg_at_10
      value: 43.408
    - type: ndcg_at_20
      value: 46.107
    - type: ndcg_at_30
      value: 47.164
    - type: ndcg_at_50
      value: 48.126000000000005
    - type: ndcg_at_70
      value: 48.626999999999995
    - type: ndcg_at_100
      value: 49.043
    - type: ndcg_at_200
      value: 49.575
    - type: ndcg_at_300
      value: 49.794
    - type: ndcg_at_500
      value: 49.942
    - type: ndcg_at_700
      value: 50.014
    - type: ndcg_at_1000
      value: 50.077000000000005
    - type: map_at_1
      value: 23.723
    - type: map_at_2
      value: 29.593000000000004
    - type: map_at_3
      value: 32.273
    - type: map_at_5
      value: 34.587
    - type: map_at_7
      value: 35.589999999999996
    - type: map_at_10
      value: 36.296
    - type: map_at_20
      value: 37.059999999999995
    - type: map_at_30
      value: 37.265
    - type: map_at_50
      value: 37.402
    - type: map_at_70
      value: 37.454
    - type: map_at_100
      value: 37.486999999999995
    - type: map_at_200
      value: 37.516
    - type: map_at_300
      value: 37.524
    - type: map_at_500
      value: 37.528
    - type: map_at_700
      value: 37.529
    - type: map_at_1000
      value: 37.53
    - type: recall_at_1
      value: 23.723
    - type: recall_at_2
      value: 35.355
    - type: recall_at_3
      value: 43.22
    - type: recall_at_5
      value: 53.025
    - type: recall_at_7
      value: 59.327
    - type: recall_at_10
      value: 65.302
    - type: recall_at_20
      value: 75.765
    - type: recall_at_30
      value: 80.632
    - type: recall_at_50
      value: 85.63499999999999
    - type: recall_at_70
      value: 88.554
    - type: recall_at_100
      value: 91.16300000000001
    - type: recall_at_200
      value: 94.85
    - type: recall_at_300
      value: 96.532
    - type: recall_at_500
      value: 97.751
    - type: recall_at_700
      value: 98.383
    - type: recall_at_1000
      value: 98.97
    - type: precision_at_1
      value: 24.398
    - type: precision_at_2
      value: 18.274
    - type: precision_at_3
      value: 14.951999999999998
    - type: precision_at_5
      value: 11.052
    - type: precision_at_7
      value: 8.84
    - type: precision_at_10
      value: 6.8309999999999995
    - type: precision_at_20
      value: 3.978
    - type: precision_at_30
      value: 2.827
    - type: precision_at_50
      value: 1.807
    - type: precision_at_70
      value: 1.336
    - type: precision_at_100
      value: 0.964
    - type: precision_at_200
      value: 0.502
    - type: precision_at_300
      value: 0.34099999999999997
    - type: precision_at_500
      value: 0.208
    - type: precision_at_700
      value: 0.15
    - type: precision_at_1000
      value: 0.105
    - type: mrr_at_1
      value: 24.398
    - type: mrr_at_2
      value: 30.351
    - type: mrr_at_3
      value: 33.001000000000005
    - type: mrr_at_5
      value: 35.228
    - type: mrr_at_7
      value: 36.223
    - type: mrr_at_10
      value: 36.903999999999996
    - type: mrr_at_20
      value: 37.631
    - type: mrr_at_30
      value: 37.830000000000005
    - type: mrr_at_50
      value: 37.955
    - type: mrr_at_70
      value: 38.003
    - type: mrr_at_100
      value: 38.033
    - type: mrr_at_200
      value: 38.059
    - type: mrr_at_300
      value: 38.066
    - type: mrr_at_500
      value: 38.068999999999996
    - type: mrr_at_700
      value: 38.07
    - type: mrr_at_1000
      value: 38.07
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
      value: 96.35658914728683
    - type: f1
      value: 96.15039630903114
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
      value: 86.29730962152303
    - type: f1
      value: 71.12166316567485
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
      value: 79.98991257565568
    - type: f1
      value: 77.41680115095276
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
      value: 82.1990585070612
    - type: f1
      value: 82.23719179179362
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
      value: 40.03019554933584
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
      value: 38.999760551497815
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
      value: 32.72383151953079
    - type: mrr
      value: 33.93989699030721
  - task:
      type: Retrieval
    dataset:
      type: nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 51.858000000000004
    - type: ndcg_at_2
      value: 49.675999999999995
    - type: ndcg_at_3
      value: 47.519
    - type: ndcg_at_5
      value: 45.198
    - type: ndcg_at_7
      value: 43.504
    - type: ndcg_at_10
      value: 41.88
    - type: ndcg_at_20
      value: 39.122
    - type: ndcg_at_30
      value: 37.95
    - type: ndcg_at_50
      value: 37.602999999999994
    - type: ndcg_at_70
      value: 37.836
    - type: ndcg_at_100
      value: 38.493
    - type: ndcg_at_200
      value: 40.187
    - type: ndcg_at_300
      value: 41.524
    - type: ndcg_at_500
      value: 43.657000000000004
    - type: ndcg_at_700
      value: 45.234
    - type: ndcg_at_1000
      value: 47.047
    - type: map_at_1
      value: 6.392
    - type: map_at_2
      value: 10.113
    - type: map_at_3
      value: 11.543000000000001
    - type: map_at_5
      value: 13.729
    - type: map_at_7
      value: 14.985000000000001
    - type: map_at_10
      value: 16.217000000000002
    - type: map_at_20
      value: 18.106
    - type: map_at_30
      value: 18.878
    - type: map_at_50
      value: 19.822
    - type: map_at_70
      value: 20.352999999999998
    - type: map_at_100
      value: 20.827
    - type: map_at_200
      value: 21.512
    - type: map_at_300
      value: 21.826
    - type: map_at_500
      value: 22.155
    - type: map_at_700
      value: 22.349
    - type: map_at_1000
      value: 22.531000000000002
    - type: recall_at_1
      value: 6.392
    - type: recall_at_2
      value: 11.215
    - type: recall_at_3
      value: 13.231000000000002
    - type: recall_at_5
      value: 16.66
    - type: recall_at_7
      value: 18.802
    - type: recall_at_10
      value: 21.185000000000002
    - type: recall_at_20
      value: 25.35
    - type: recall_at_30
      value: 27.91
    - type: recall_at_50
      value: 32.845
    - type: recall_at_70
      value: 35.789
    - type: recall_at_100
      value: 39.247
    - type: recall_at_200
      value: 46.655
    - type: recall_at_300
      value: 51.43299999999999
    - type: recall_at_500
      value: 59.472
    - type: recall_at_700
      value: 64.742
    - type: recall_at_1000
      value: 70.97099999999999
    - type: precision_at_1
      value: 53.559999999999995
    - type: precision_at_2
      value: 48.762
    - type: precision_at_3
      value: 44.169000000000004
    - type: precision_at_5
      value: 39.071
    - type: precision_at_7
      value: 35.161
    - type: precision_at_10
      value: 31.238
    - type: precision_at_20
      value: 23.064999999999998
    - type: precision_at_30
      value: 18.844
    - type: precision_at_50
      value: 14.601
    - type: precision_at_70
      value: 12.088000000000001
    - type: precision_at_100
      value: 9.844999999999999
    - type: precision_at_200
      value: 6.358
    - type: precision_at_300
      value: 4.915
    - type: precision_at_500
      value: 3.531
    - type: precision_at_700
      value: 2.8649999999999998
    - type: precision_at_1000
      value: 2.289
    - type: mrr_at_1
      value: 54.17999999999999
    - type: mrr_at_2
      value: 59.288
    - type: mrr_at_3
      value: 60.836
    - type: mrr_at_5
      value: 62.275999999999996
    - type: mrr_at_7
      value: 62.688
    - type: mrr_at_10
      value: 62.865
    - type: mrr_at_20
      value: 63.11
    - type: mrr_at_30
      value: 63.193999999999996
    - type: mrr_at_50
      value: 63.258
    - type: mrr_at_70
      value: 63.278
    - type: mrr_at_100
      value: 63.297000000000004
    - type: mrr_at_200
      value: 63.315999999999995
    - type: mrr_at_300
      value: 63.318
    - type: mrr_at_500
      value: 63.32299999999999
    - type: mrr_at_700
      value: 63.324000000000005
    - type: mrr_at_1000
      value: 63.324999999999996
  - task:
      type: Retrieval
    dataset:
      type: nq
      name: MTEB NQ
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 50.897999999999996
    - type: ndcg_at_2
      value: 59.126
    - type: ndcg_at_3
      value: 63.093999999999994
    - type: ndcg_at_5
      value: 67.197
    - type: ndcg_at_7
      value: 68.719
    - type: ndcg_at_10
      value: 69.915
    - type: ndcg_at_20
      value: 71.229
    - type: ndcg_at_30
      value: 71.667
    - type: ndcg_at_50
      value: 71.98
    - type: ndcg_at_70
      value: 72.127
    - type: ndcg_at_100
      value: 72.217
    - type: ndcg_at_200
      value: 72.319
    - type: ndcg_at_300
      value: 72.347
    - type: ndcg_at_500
      value: 72.37
    - type: ndcg_at_700
      value: 72.379
    - type: ndcg_at_1000
      value: 72.381
    - type: map_at_1
      value: 45.297
    - type: map_at_2
      value: 55.596000000000004
    - type: map_at_3
      value: 58.724
    - type: map_at_5
      value: 61.387
    - type: map_at_7
      value: 62.173
    - type: map_at_10
      value: 62.69
    - type: map_at_20
      value: 63.125
    - type: map_at_30
      value: 63.223
    - type: map_at_50
      value: 63.27700000000001
    - type: map_at_70
      value: 63.295
    - type: map_at_100
      value: 63.303
    - type: map_at_200
      value: 63.31
    - type: map_at_300
      value: 63.31099999999999
    - type: map_at_500
      value: 63.312000000000005
    - type: map_at_700
      value: 63.312000000000005
    - type: map_at_1000
      value: 63.312000000000005
    - type: recall_at_1
      value: 45.297
    - type: recall_at_2
      value: 63.866
    - type: recall_at_3
      value: 71.898
    - type: recall_at_5
      value: 81.16600000000001
    - type: recall_at_7
      value: 85.301
    - type: recall_at_10
      value: 88.94800000000001
    - type: recall_at_20
      value: 93.719
    - type: recall_at_30
      value: 95.628
    - type: recall_at_50
      value: 97.14699999999999
    - type: recall_at_70
      value: 97.955
    - type: recall_at_100
      value: 98.48599999999999
    - type: recall_at_200
      value: 99.157
    - type: recall_at_300
      value: 99.355
    - type: recall_at_500
      value: 99.53699999999999
    - type: recall_at_700
      value: 99.62299999999999
    - type: recall_at_1000
      value: 99.638
    - type: precision_at_1
      value: 50.897999999999996
    - type: precision_at_2
      value: 36.703
    - type: precision_at_3
      value: 27.926000000000002
    - type: precision_at_5
      value: 19.276
    - type: precision_at_7
      value: 14.533999999999999
    - type: precision_at_10
      value: 10.678
    - type: precision_at_20
      value: 5.663
    - type: precision_at_30
      value: 3.8600000000000003
    - type: precision_at_50
      value: 2.358
    - type: precision_at_70
      value: 1.7000000000000002
    - type: precision_at_100
      value: 1.198
    - type: precision_at_200
      value: 0.603
    - type: precision_at_300
      value: 0.40299999999999997
    - type: precision_at_500
      value: 0.242
    - type: precision_at_700
      value: 0.173
    - type: precision_at_1000
      value: 0.121
    - type: mrr_at_1
      value: 50.897999999999996
    - type: mrr_at_2
      value: 59.994
    - type: mrr_at_3
      value: 62.553000000000004
    - type: mrr_at_5
      value: 64.307
    - type: mrr_at_7
      value: 64.864
    - type: mrr_at_10
      value: 65.22200000000001
    - type: mrr_at_20
      value: 65.499
    - type: mrr_at_30
      value: 65.561
    - type: mrr_at_50
      value: 65.592
    - type: mrr_at_70
      value: 65.602
    - type: mrr_at_100
      value: 65.607
    - type: mrr_at_200
      value: 65.61099999999999
    - type: mrr_at_300
      value: 65.61200000000001
    - type: mrr_at_500
      value: 65.61200000000001
    - type: mrr_at_700
      value: 65.61200000000001
    - type: mrr_at_1000
      value: 65.61200000000001
  - task:
      type: Retrieval
    dataset:
      type: quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 82.96
    - type: ndcg_at_2
      value: 85.614
    - type: ndcg_at_3
      value: 87.19
    - type: ndcg_at_5
      value: 88.654
    - type: ndcg_at_7
      value: 89.287
    - type: ndcg_at_10
      value: 89.785
    - type: ndcg_at_20
      value: 90.384
    - type: ndcg_at_30
      value: 90.589
    - type: ndcg_at_50
      value: 90.738
    - type: ndcg_at_70
      value: 90.789
    - type: ndcg_at_100
      value: 90.824
    - type: ndcg_at_200
      value: 90.869
    - type: ndcg_at_300
      value: 90.881
    - type: ndcg_at_500
      value: 90.886
    - type: ndcg_at_700
      value: 90.889
    - type: ndcg_at_1000
      value: 90.889
    - type: map_at_1
      value: 72.152
    - type: map_at_2
      value: 80.818
    - type: map_at_3
      value: 83.462
    - type: map_at_5
      value: 85.286
    - type: map_at_7
      value: 85.921
    - type: map_at_10
      value: 86.334
    - type: map_at_20
      value: 86.737
    - type: map_at_30
      value: 86.847
    - type: map_at_50
      value: 86.911
    - type: map_at_70
      value: 86.932
    - type: map_at_100
      value: 86.943
    - type: map_at_200
      value: 86.953
    - type: map_at_300
      value: 86.955
    - type: map_at_500
      value: 86.956
    - type: map_at_700
      value: 86.956
    - type: map_at_1000
      value: 86.956
    - type: recall_at_1
      value: 72.152
    - type: recall_at_2
      value: 84.129
    - type: recall_at_3
      value: 88.87
    - type: recall_at_5
      value: 93.067
    - type: recall_at_7
      value: 94.882
    - type: recall_at_10
      value: 96.353
    - type: recall_at_20
      value: 98.26700000000001
    - type: recall_at_30
      value: 98.92999999999999
    - type: recall_at_50
      value: 99.441
    - type: recall_at_70
      value: 99.619
    - type: recall_at_100
      value: 99.748
    - type: recall_at_200
      value: 99.911
    - type: recall_at_300
      value: 99.956
    - type: recall_at_500
      value: 99.98
    - type: recall_at_700
      value: 99.991
    - type: recall_at_1000
      value: 99.996
    - type: precision_at_1
      value: 82.96
    - type: precision_at_2
      value: 52.175000000000004
    - type: precision_at_3
      value: 38.223
    - type: precision_at_5
      value: 25.056
    - type: precision_at_7
      value: 18.717
    - type: precision_at_10
      value: 13.614999999999998
    - type: precision_at_20
      value: 7.208
    - type: precision_at_30
      value: 4.928
    - type: precision_at_50
      value: 3.024
    - type: precision_at_70
      value: 2.183
    - type: precision_at_100
      value: 1.54
    - type: precision_at_200
      value: 0.779
    - type: precision_at_300
      value: 0.521
    - type: precision_at_500
      value: 0.313
    - type: precision_at_700
      value: 0.22399999999999998
    - type: precision_at_1000
      value: 0.157
    - type: mrr_at_1
      value: 82.96
    - type: mrr_at_2
      value: 87.005
    - type: mrr_at_3
      value: 88.07199999999999
    - type: mrr_at_5
      value: 88.634
    - type: mrr_at_7
      value: 88.793
    - type: mrr_at_10
      value: 88.87899999999999
    - type: mrr_at_20
      value: 88.94999999999999
    - type: mrr_at_30
      value: 88.96
    - type: mrr_at_50
      value: 88.965
    - type: mrr_at_70
      value: 88.966
    - type: mrr_at_100
      value: 88.967
    - type: mrr_at_200
      value: 88.967
    - type: mrr_at_300
      value: 88.967
    - type: mrr_at_500
      value: 88.967
    - type: mrr_at_700
      value: 88.967
    - type: mrr_at_1000
      value: 88.967
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
      value: 59.90388554491155
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
      value: 67.64232539036783
  - task:
      type: Retrieval
    dataset:
      type: scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 22.6
    - type: ndcg_at_2
      value: 20.355999999999998
    - type: ndcg_at_3
      value: 18.536
    - type: ndcg_at_5
      value: 16.523
    - type: ndcg_at_7
      value: 17.979
    - type: ndcg_at_10
      value: 19.908
    - type: ndcg_at_20
      value: 22.887
    - type: ndcg_at_30
      value: 24.43
    - type: ndcg_at_50
      value: 25.959
    - type: ndcg_at_70
      value: 26.989
    - type: ndcg_at_100
      value: 27.977
    - type: ndcg_at_200
      value: 29.831000000000003
    - type: ndcg_at_300
      value: 30.787
    - type: ndcg_at_500
      value: 31.974999999999998
    - type: ndcg_at_700
      value: 32.554
    - type: ndcg_at_1000
      value: 33.277
    - type: map_at_1
      value: 4.593
    - type: map_at_2
      value: 6.923
    - type: map_at_3
      value: 8.3
    - type: map_at_5
      value: 10.072000000000001
    - type: map_at_7
      value: 10.782
    - type: map_at_10
      value: 11.72
    - type: map_at_20
      value: 12.838
    - type: map_at_30
      value: 13.257
    - type: map_at_50
      value: 13.569
    - type: map_at_70
      value: 13.733
    - type: map_at_100
      value: 13.858999999999998
    - type: map_at_200
      value: 14.018
    - type: map_at_300
      value: 14.072999999999999
    - type: map_at_500
      value: 14.126
    - type: map_at_700
      value: 14.145
    - type: map_at_1000
      value: 14.161999999999999
    - type: recall_at_1
      value: 4.593
    - type: recall_at_2
      value: 7.997999999999999
    - type: recall_at_3
      value: 10.563
    - type: recall_at_5
      value: 14.907
    - type: recall_at_7
      value: 17.4
    - type: recall_at_10
      value: 21.18
    - type: recall_at_20
      value: 28.144999999999996
    - type: recall_at_30
      value: 32.462
    - type: recall_at_50
      value: 37.267
    - type: recall_at_70
      value: 40.875
    - type: recall_at_100
      value: 44.641999999999996
    - type: recall_at_200
      value: 52.573
    - type: recall_at_300
      value: 57.089999999999996
    - type: recall_at_500
      value: 63.14300000000001
    - type: recall_at_700
      value: 66.313
    - type: recall_at_1000
      value: 70.458
    - type: precision_at_1
      value: 22.6
    - type: precision_at_2
      value: 19.7
    - type: precision_at_3
      value: 17.333000000000002
    - type: precision_at_5
      value: 14.680000000000001
    - type: precision_at_7
      value: 12.243
    - type: precision_at_10
      value: 10.440000000000001
    - type: precision_at_20
      value: 6.944999999999999
    - type: precision_at_30
      value: 5.333
    - type: precision_at_50
      value: 3.678
    - type: precision_at_70
      value: 2.881
    - type: precision_at_100
      value: 2.2030000000000003
    - type: precision_at_200
      value: 1.295
    - type: precision_at_300
      value: 0.9369999999999999
    - type: precision_at_500
      value: 0.622
    - type: precision_at_700
      value: 0.466
    - type: precision_at_1000
      value: 0.347
    - type: mrr_at_1
      value: 22.6
    - type: mrr_at_2
      value: 27.900000000000002
    - type: mrr_at_3
      value: 30.067
    - type: mrr_at_5
      value: 32.207
    - type: mrr_at_7
      value: 33.004
    - type: mrr_at_10
      value: 33.596
    - type: mrr_at_20
      value: 34.268
    - type: mrr_at_30
      value: 34.492
    - type: mrr_at_50
      value: 34.628
    - type: mrr_at_70
      value: 34.681
    - type: mrr_at_100
      value: 34.717
    - type: mrr_at_200
      value: 34.757
    - type: mrr_at_300
      value: 34.768
    - type: mrr_at_500
      value: 34.772
    - type: mrr_at_700
      value: 34.774
    - type: mrr_at_1000
      value: 34.775
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
      value: 86.90122745229677
    - type: cos_sim_spearman
      value: 82.92294737327579
    - type: euclidean_pearson
      value: 84.08979655773187
    - type: euclidean_spearman
      value: 82.92294657285412
    - type: manhattan_pearson
      value: 84.09347480531832
    - type: manhattan_spearman
      value: 82.91564613948087
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
      value: 87.01218713698583
    - type: cos_sim_spearman
      value: 79.46865215168464
    - type: euclidean_pearson
      value: 83.22621889891909
    - type: euclidean_spearman
      value: 79.46853821709514
    - type: manhattan_pearson
      value: 83.69962580788805
    - type: manhattan_spearman
      value: 79.9561593356932
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
      value: 88.98438696342964
    - type: cos_sim_spearman
      value: 89.15419511870839
    - type: euclidean_pearson
      value: 88.49646141802894
    - type: euclidean_spearman
      value: 89.15419503946019
    - type: manhattan_pearson
      value: 88.6420585616327
    - type: manhattan_spearman
      value: 89.42648950757743
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
      value: 87.30772547759544
    - type: cos_sim_spearman
      value: 84.93199878424691
    - type: euclidean_pearson
      value: 86.16266630395455
    - type: euclidean_spearman
      value: 84.93198798543634
    - type: manhattan_pearson
      value: 86.14285723189803
    - type: manhattan_spearman
      value: 85.0361672522687
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
      value: 90.21342071197127
    - type: cos_sim_spearman
      value: 90.7407512744838
    - type: euclidean_pearson
      value: 90.1517933113061
    - type: euclidean_spearman
      value: 90.74075125431919
    - type: manhattan_pearson
      value: 90.17963034676193
    - type: manhattan_spearman
      value: 90.88999275865135
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
      value: 86.82518054100498
    - type: cos_sim_spearman
      value: 87.81570533154735
    - type: euclidean_pearson
      value: 86.91684561573618
    - type: euclidean_spearman
      value: 87.81570533154735
    - type: manhattan_pearson
      value: 86.98311935744032
    - type: manhattan_spearman
      value: 87.9594667151966
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
      value: 92.09578436612053
    - type: cos_sim_spearman
      value: 92.01519349090438
    - type: euclidean_pearson
      value: 92.07113635890894
    - type: euclidean_spearman
      value: 92.01519349090438
    - type: manhattan_pearson
      value: 91.89343820765625
    - type: manhattan_spearman
      value: 91.7443476810177
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
      value: 69.29997751464549
    - type: cos_sim_spearman
      value: 68.36425436812782
    - type: euclidean_pearson
      value: 69.81381677661783
    - type: euclidean_spearman
      value: 68.36425436812782
    - type: manhattan_pearson
      value: 69.92823397008026
    - type: manhattan_spearman
      value: 68.35770640039254
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
      value: 88.39126315452359
    - type: cos_sim_spearman
      value: 88.99708463265337
    - type: euclidean_pearson
      value: 88.60793820038607
    - type: euclidean_spearman
      value: 88.99708463265337
    - type: manhattan_pearson
      value: 88.69860633571047
    - type: manhattan_spearman
      value: 89.20094593888012
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
      value: 86.58028062818582
    - type: mrr
      value: 96.53586790841693
  - task:
      type: Retrieval
    dataset:
      type: scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 66.333
    - type: ndcg_at_2
      value: 70.655
    - type: ndcg_at_3
      value: 72.801
    - type: ndcg_at_5
      value: 75.793
    - type: ndcg_at_7
      value: 76.946
    - type: ndcg_at_10
      value: 77.66199999999999
    - type: ndcg_at_20
      value: 78.786
    - type: ndcg_at_30
      value: 79.066
    - type: ndcg_at_50
      value: 79.255
    - type: ndcg_at_70
      value: 79.423
    - type: ndcg_at_100
      value: 79.476
    - type: ndcg_at_200
      value: 79.65299999999999
    - type: ndcg_at_300
      value: 79.696
    - type: ndcg_at_500
      value: 79.73599999999999
    - type: ndcg_at_700
      value: 79.77199999999999
    - type: ndcg_at_1000
      value: 79.77199999999999
    - type: map_at_1
      value: 63.383
    - type: map_at_2
      value: 68.144
    - type: map_at_3
      value: 70.19800000000001
    - type: map_at_5
      value: 72.38
    - type: map_at_7
      value: 72.955
    - type: map_at_10
      value: 73.312
    - type: map_at_20
      value: 73.678
    - type: map_at_30
      value: 73.72800000000001
    - type: map_at_50
      value: 73.75500000000001
    - type: map_at_70
      value: 73.771
    - type: map_at_100
      value: 73.776
    - type: map_at_200
      value: 73.783
    - type: map_at_300
      value: 73.784
    - type: map_at_500
      value: 73.785
    - type: map_at_700
      value: 73.786
    - type: map_at_1000
      value: 73.786
    - type: recall_at_1
      value: 63.383
    - type: recall_at_2
      value: 72.283
    - type: recall_at_3
      value: 77.183
    - type: recall_at_5
      value: 84.56099999999999
    - type: recall_at_7
      value: 87.67200000000001
    - type: recall_at_10
      value: 89.822
    - type: recall_at_20
      value: 94
    - type: recall_at_30
      value: 95.333
    - type: recall_at_50
      value: 96.333
    - type: recall_at_70
      value: 97.333
    - type: recall_at_100
      value: 97.667
    - type: recall_at_200
      value: 99
    - type: recall_at_300
      value: 99.333
    - type: recall_at_500
      value: 99.667
    - type: recall_at_700
      value: 100
    - type: recall_at_1000
      value: 100
    - type: precision_at_1
      value: 66.333
    - type: precision_at_2
      value: 38.667
    - type: precision_at_3
      value: 28.111000000000004
    - type: precision_at_5
      value: 18.933
    - type: precision_at_7
      value: 14.094999999999999
    - type: precision_at_10
      value: 10.167
    - type: precision_at_20
      value: 5.35
    - type: precision_at_30
      value: 3.611
    - type: precision_at_50
      value: 2.1870000000000003
    - type: precision_at_70
      value: 1.576
    - type: precision_at_100
      value: 1.107
    - type: precision_at_200
      value: 0.5599999999999999
    - type: precision_at_300
      value: 0.374
    - type: precision_at_500
      value: 0.22499999999999998
    - type: precision_at_700
      value: 0.161
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: mrr_at_1
      value: 66.333
    - type: mrr_at_2
      value: 70.833
    - type: mrr_at_3
      value: 72.167
    - type: mrr_at_5
      value: 73.6
    - type: mrr_at_7
      value: 74.084
    - type: mrr_at_10
      value: 74.283
    - type: mrr_at_20
      value: 74.54499999999999
    - type: mrr_at_30
      value: 74.59599999999999
    - type: mrr_at_50
      value: 74.622
    - type: mrr_at_70
      value: 74.639
    - type: mrr_at_100
      value: 74.643
    - type: mrr_at_200
      value: 74.65
    - type: mrr_at_300
      value: 74.652
    - type: mrr_at_500
      value: 74.653
    - type: mrr_at_700
      value: 74.653
    - type: mrr_at_1000
      value: 74.653
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
      value: 99.84554455445544
    - type: cos_sim_ap
      value: 96.31178339136798
    - type: cos_sim_f1
      value: 92.1921921921922
    - type: cos_sim_precision
      value: 92.28456913827655
    - type: cos_sim_recall
      value: 92.10000000000001
    - type: dot_accuracy
      value: 99.84554455445544
    - type: dot_ap
      value: 96.31178339136797
    - type: dot_f1
      value: 92.1921921921922
    - type: dot_precision
      value: 92.28456913827655
    - type: dot_recall
      value: 92.10000000000001
    - type: euclidean_accuracy
      value: 99.84554455445544
    - type: euclidean_ap
      value: 96.31178339136798
    - type: euclidean_f1
      value: 92.1921921921922
    - type: euclidean_precision
      value: 92.28456913827655
    - type: euclidean_recall
      value: 92.10000000000001
    - type: manhattan_accuracy
      value: 99.84752475247525
    - type: manhattan_ap
      value: 96.4591954606088
    - type: manhattan_f1
      value: 92.25352112676056
    - type: manhattan_precision
      value: 92.81376518218623
    - type: manhattan_recall
      value: 91.7
    - type: max_accuracy
      value: 99.84752475247525
    - type: max_ap
      value: 96.4591954606088
    - type: max_f1
      value: 92.25352112676056
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
      value: 74.24659759283294
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
      value: 46.77690051260451
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
      value: 55.68436757803185
    - type: mrr
      value: 56.82157711569475
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
      value: 31.652482405629843
    - type: cos_sim_spearman
      value: 31.16341822347735
    - type: dot_pearson
      value: 31.652479892699837
    - type: dot_spearman
      value: 31.16341822347735
  - task:
      type: Retrieval
    dataset:
      type: trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 92
    - type: ndcg_at_2
      value: 90.839
    - type: ndcg_at_3
      value: 90.642
    - type: ndcg_at_5
      value: 90.348
    - type: ndcg_at_7
      value: 89.015
    - type: ndcg_at_10
      value: 87.599
    - type: ndcg_at_20
      value: 84.434
    - type: ndcg_at_30
      value: 81.655
    - type: ndcg_at_50
      value: 77.278
    - type: ndcg_at_70
      value: 73.957
    - type: ndcg_at_100
      value: 69.56
    - type: ndcg_at_200
      value: 60.724000000000004
    - type: ndcg_at_300
      value: 57.245000000000005
    - type: ndcg_at_500
      value: 56.316
    - type: ndcg_at_700
      value: 58.399
    - type: ndcg_at_1000
      value: 62.21600000000001
    - type: map_at_1
      value: 0.247
    - type: map_at_2
      value: 0.488
    - type: map_at_3
      value: 0.7230000000000001
    - type: map_at_5
      value: 1.204
    - type: map_at_7
      value: 1.6500000000000001
    - type: map_at_10
      value: 2.292
    - type: map_at_20
      value: 4.274
    - type: map_at_30
      value: 6.027
    - type: map_at_50
      value: 9.083
    - type: map_at_70
      value: 11.751000000000001
    - type: map_at_100
      value: 14.912
    - type: map_at_200
      value: 22.213
    - type: map_at_300
      value: 26.667999999999996
    - type: map_at_500
      value: 31.556
    - type: map_at_700
      value: 34.221000000000004
    - type: map_at_1000
      value: 36.443999999999996
    - type: recall_at_1
      value: 0.247
    - type: recall_at_2
      value: 0.49899999999999994
    - type: recall_at_3
      value: 0.742
    - type: recall_at_5
      value: 1.247
    - type: recall_at_7
      value: 1.722
    - type: recall_at_10
      value: 2.405
    - type: recall_at_20
      value: 4.583
    - type: recall_at_30
      value: 6.587999999999999
    - type: recall_at_50
      value: 10.188
    - type: recall_at_70
      value: 13.496
    - type: recall_at_100
      value: 17.578
    - type: recall_at_200
      value: 28.158
    - type: recall_at_300
      value: 35.532000000000004
    - type: recall_at_500
      value: 45.31
    - type: recall_at_700
      value: 51.822
    - type: recall_at_1000
      value: 58.53
    - type: precision_at_1
      value: 96
    - type: precision_at_2
      value: 96
    - type: precision_at_3
      value: 95.333
    - type: precision_at_5
      value: 94.8
    - type: precision_at_7
      value: 93.429
    - type: precision_at_10
      value: 91.4
    - type: precision_at_20
      value: 87.7
    - type: precision_at_30
      value: 84.867
    - type: precision_at_50
      value: 80.24
    - type: precision_at_70
      value: 76.371
    - type: precision_at_100
      value: 71.08
    - type: precision_at_200
      value: 59.4
    - type: precision_at_300
      value: 51.459999999999994
    - type: precision_at_500
      value: 40.644000000000005
    - type: precision_at_700
      value: 33.889
    - type: precision_at_1000
      value: 27.250000000000004
    - type: mrr_at_1
      value: 96
    - type: mrr_at_2
      value: 98
    - type: mrr_at_3
      value: 98
    - type: mrr_at_5
      value: 98
    - type: mrr_at_7
      value: 98
    - type: mrr_at_10
      value: 98
    - type: mrr_at_20
      value: 98
    - type: mrr_at_30
      value: 98
    - type: mrr_at_50
      value: 98
    - type: mrr_at_70
      value: 98
    - type: mrr_at_100
      value: 98
    - type: mrr_at_200
      value: 98
    - type: mrr_at_300
      value: 98
    - type: mrr_at_500
      value: 98
    - type: mrr_at_700
      value: 98
    - type: mrr_at_1000
      value: 98
  - task:
      type: Retrieval
    dataset:
      type: webis-touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_1
      value: 43.878
    - type: ndcg_at_2
      value: 37.956
    - type: ndcg_at_3
      value: 35.053
    - type: ndcg_at_5
      value: 32.59
    - type: ndcg_at_7
      value: 30.226
    - type: ndcg_at_10
      value: 29.005
    - type: ndcg_at_20
      value: 30.11
    - type: ndcg_at_30
      value: 32.019999999999996
    - type: ndcg_at_50
      value: 34.354
    - type: ndcg_at_70
      value: 36.665
    - type: ndcg_at_100
      value: 38.888
    - type: ndcg_at_200
      value: 43.435
    - type: ndcg_at_300
      value: 45.795
    - type: ndcg_at_500
      value: 48.699999999999996
    - type: ndcg_at_700
      value: 50.242
    - type: ndcg_at_1000
      value: 51.529
    - type: map_at_1
      value: 3.521
    - type: map_at_2
      value: 5.309
    - type: map_at_3
      value: 6.576
    - type: map_at_5
      value: 8.97
    - type: map_at_7
      value: 10.194
    - type: map_at_10
      value: 11.949
    - type: map_at_20
      value: 14.686
    - type: map_at_30
      value: 15.8
    - type: map_at_50
      value: 16.59
    - type: map_at_70
      value: 17.2
    - type: map_at_100
      value: 17.765
    - type: map_at_200
      value: 18.636
    - type: map_at_300
      value: 18.972
    - type: map_at_500
      value: 19.301
    - type: map_at_700
      value: 19.445
    - type: map_at_1000
      value: 19.546
    - type: recall_at_1
      value: 3.521
    - type: recall_at_2
      value: 5.848
    - type: recall_at_3
      value: 7.657
    - type: recall_at_5
      value: 11.368
    - type: recall_at_7
      value: 13.748
    - type: recall_at_10
      value: 18.061
    - type: recall_at_20
      value: 26.844
    - type: recall_at_30
      value: 31.186000000000003
    - type: recall_at_50
      value: 35.951
    - type: recall_at_70
      value: 40.961999999999996
    - type: recall_at_100
      value: 46.743
    - type: recall_at_200
      value: 58.483
    - type: recall_at_300
      value: 65.973
    - type: recall_at_500
      value: 75.233
    - type: recall_at_700
      value: 80.472
    - type: recall_at_1000
      value: 85.02
    - type: precision_at_1
      value: 46.939
    - type: precision_at_2
      value: 38.775999999999996
    - type: precision_at_3
      value: 34.694
    - type: precision_at_5
      value: 31.429000000000002
    - type: precision_at_7
      value: 27.697
    - type: precision_at_10
      value: 24.490000000000002
    - type: precision_at_20
      value: 18.776
    - type: precision_at_30
      value: 15.034
    - type: precision_at_50
      value: 10.857
    - type: precision_at_70
      value: 9.096
    - type: precision_at_100
      value: 7.51
    - type: precision_at_200
      value: 4.929
    - type: precision_at_300
      value: 3.7760000000000002
    - type: precision_at_500
      value: 2.6780000000000004
    - type: precision_at_700
      value: 2.085
    - type: precision_at_1000
      value: 1.5709999999999997
    - type: mrr_at_1
      value: 46.939
    - type: mrr_at_2
      value: 55.102
    - type: mrr_at_3
      value: 57.823
    - type: mrr_at_5
      value: 60.68
    - type: mrr_at_7
      value: 60.972
    - type: mrr_at_10
      value: 61.199000000000005
    - type: mrr_at_20
      value: 61.831
    - type: mrr_at_30
      value: 61.831
    - type: mrr_at_50
      value: 61.873
    - type: mrr_at_70
      value: 61.873
    - type: mrr_at_100
      value: 61.873
    - type: mrr_at_200
      value: 61.873
    - type: mrr_at_300
      value: 61.873
    - type: mrr_at_500
      value: 61.873
    - type: mrr_at_700
      value: 61.873
    - type: mrr_at_1000
      value: 61.873
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
      value: 69.3294
    - type: ap
      value: 14.561333393364736
    - type: f1
      value: 53.992309820496466
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
      value: 63.63893604980192
    - type: f1
      value: 63.92959380489434
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
      value: 56.270879258659775
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
      value: 88.71073493473207
    - type: cos_sim_ap
      value: 81.52392540284202
    - type: cos_sim_f1
      value: 74.71162377994676
    - type: cos_sim_precision
      value: 71.89558428885094
    - type: cos_sim_recall
      value: 77.75725593667546
    - type: dot_accuracy
      value: 88.71073493473207
    - type: dot_ap
      value: 81.52394754041109
    - type: dot_f1
      value: 74.71162377994676
    - type: dot_precision
      value: 71.89558428885094
    - type: dot_recall
      value: 77.75725593667546
    - type: euclidean_accuracy
      value: 88.71073493473207
    - type: euclidean_ap
      value: 81.52392035435321
    - type: euclidean_f1
      value: 74.71162377994676
    - type: euclidean_precision
      value: 71.89558428885094
    - type: euclidean_recall
      value: 77.75725593667546
    - type: manhattan_accuracy
      value: 88.47231328604637
    - type: manhattan_ap
      value: 81.22907439267321
    - type: manhattan_f1
      value: 74.3351571446749
    - type: manhattan_precision
      value: 71.78667977390022
    - type: manhattan_recall
      value: 77.0712401055409
    - type: max_accuracy
      value: 88.71073493473207
    - type: max_ap
      value: 81.52394754041109
    - type: max_f1
      value: 74.71162377994676
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
      value: 89.85136026700819
    - type: cos_sim_ap
      value: 87.7768002924216
    - type: cos_sim_f1
      value: 80.358908624794
    - type: cos_sim_precision
      value: 76.62918209122023
    - type: cos_sim_recall
      value: 84.47028025870034
    - type: dot_accuracy
      value: 89.85136026700819
    - type: dot_ap
      value: 87.77680027889778
    - type: dot_f1
      value: 80.358908624794
    - type: dot_precision
      value: 76.62918209122023
    - type: dot_recall
      value: 84.47028025870034
    - type: euclidean_accuracy
      value: 89.85136026700819
    - type: euclidean_ap
      value: 87.77680174697751
    - type: euclidean_f1
      value: 80.358908624794
    - type: euclidean_precision
      value: 76.62918209122023
    - type: euclidean_recall
      value: 84.47028025870034
    - type: manhattan_accuracy
      value: 89.86300306593705
    - type: manhattan_ap
      value: 87.78613271895861
    - type: manhattan_f1
      value: 80.31831016905645
    - type: manhattan_precision
      value: 76.68230516070304
    - type: manhattan_recall
      value: 84.3162919618109
    - type: max_accuracy
      value: 89.86300306593705
    - type: max_ap
      value: 87.78613271895861
    - type: max_f1
      value: 80.358908624794
language:
- en
license: cc-by-nc-4.0
---

<h1 align="center">Salesforce/SFR-Embedding-Mistral</h1>

**SFR-Embedding by Salesforce Research.**

The model is trained on top of [E5-mistral-7b-instruct](https://huggingface.co/intfloat/e5-mistral-7b-instruct) and [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1).

This project is for research purposes only. Third-party datasets may be subject to additional terms and conditions under their associated licenses. Please refer to specific papers for more details:
- [MTEB benchmark](https://arxiv.org/abs/2210.07316)
- [Mistral](https://arxiv.org/abs/2310.06825)
- [E5-mistral-7b-instruct](https://arxiv.org/pdf/2401.00368.pdf)

More technical details will be updated later.

## How to run

### Transformers
The models can be used as follows:
```python
import torch
import torch.nn.functional as F
from torch import Tensor
from transformers import AutoTokenizer, AutoModel

def last_token_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    left_padding = (attention_mask[:, -1].sum() == attention_mask.shape[0])
    if left_padding:
        return last_hidden_states[:, -1]
    else:
        sequence_lengths = attention_mask.sum(dim=1) - 1
        batch_size = last_hidden_states.shape[0]
        return last_hidden_states[torch.arange(batch_size, device=last_hidden_states.device), sequence_lengths]

def get_detailed_instruct(task_description: str, query: str) -> str:
    return f'Instruct: {task_description}\nQuery: {query}'

# Each query must come with a one-sentence instruction that describes the task
task = 'Given a web search query, retrieve relevant passages that answer the query'
queries = [
    get_detailed_instruct(task, 'How to bake a chocolate cake'),
    get_detailed_instruct(task, 'Symptoms of the flu')
]
# No need to add instruction for retrieval documents
passages = [
    "To bake a delicious chocolate cake, you'll need the following ingredients: all-purpose flour, sugar, cocoa powder, baking powder, baking soda, salt, eggs, milk, vegetable oil, and vanilla extract. Start by preheating your oven to 350°F (175°C). In a mixing bowl, combine the dry ingredients (flour, sugar, cocoa powder, baking powder, baking soda, and salt). In a separate bowl, whisk together the wet ingredients (eggs, milk, vegetable oil, and vanilla extract). Gradually add the wet mixture to the dry ingredients, stirring until well combined. Pour the batter into a greased cake pan and bake for 30-35 minutes. Let it cool before frosting with your favorite chocolate frosting. Enjoy your homemade chocolate cake!",
    "The flu, or influenza, is an illness caused by influenza viruses. Common symptoms of the flu include a high fever, chills, cough, sore throat, runny or stuffy nose, body aches, headache, fatigue, and sometimes nausea and vomiting. These symptoms can come on suddenly and are usually more severe than the common cold. It's important to get plenty of rest, stay hydrated, and consult a healthcare professional if you suspect you have the flu. In some cases, antiviral medications can help alleviate symptoms and reduce the duration of the illness."
]

# load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('Salesforce/SFR-Embedding-Mistral')
model = AutoModel.from_pretrained('Salesforce/SFR-Embedding-Mistral')

# get the embeddings
max_length = 4096
input_texts = queries + passages
batch_dict = tokenizer(input_texts, max_length=max_length, padding=True, truncation=True, return_tensors="pt")
outputs = model(**batch_dict)
embeddings = last_token_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

# normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:2] @ embeddings[2:].T) * 100
print(scores.tolist())
# [[86.7153549194336, 36.64569091796875], [35.00493621826172, 82.0738525390625]]
```

### Sentence Transformers
```python

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("Salesforce/SFR-Embedding-Mistral")

def get_detailed_instruct(task_description: str, query: str) -> str:
    return f'Instruct: {task_description}\nQuery: {query}'

# Each query must come with a one-sentence instruction that describes the task
task = 'Given a web search query, retrieve relevant passages that answer the query'
queries = [
    get_detailed_instruct(task, 'How to bake a chocolate cake'),
    get_detailed_instruct(task, 'Symptoms of the flu')
]
# No need to add instruction for retrieval documents
passages = [
    "To bake a delicious chocolate cake, you'll need the following ingredients: all-purpose flour, sugar, cocoa powder, baking powder, baking soda, salt, eggs, milk, vegetable oil, and vanilla extract. Start by preheating your oven to 350°F (175°C). In a mixing bowl, combine the dry ingredients (flour, sugar, cocoa powder, baking powder, baking soda, and salt). In a separate bowl, whisk together the wet ingredients (eggs, milk, vegetable oil, and vanilla extract). Gradually add the wet mixture to the dry ingredients, stirring until well combined. Pour the batter into a greased cake pan and bake for 30-35 minutes. Let it cool before frosting with your favorite chocolate frosting. Enjoy your homemade chocolate cake!",
    "The flu, or influenza, is an illness caused by influenza viruses. Common symptoms of the flu include a high fever, chills, cough, sore throat, runny or stuffy nose, body aches, headache, fatigue, and sometimes nausea and vomiting. These symptoms can come on suddenly and are usually more severe than the common cold. It's important to get plenty of rest, stay hydrated, and consult a healthcare professional if you suspect you have the flu. In some cases, antiviral medications can help alleviate symptoms and reduce the duration of the illness."
]

embeddings = model.encode(queries + passages)
scores = util.cos_sim(embeddings[:2], embeddings[2:]) * 100
print(scores.tolist())
# [[86.71537780761719, 36.645721435546875], [35.00497055053711, 82.07388305664062]]
```

### MTEB Benchmark Evaluation
Check out [unilm/e5](https://github.com/microsoft/unilm/tree/master/e5) to reproduce evaluation results on the [BEIR](https://arxiv.org/abs/2104.08663) and [MTEB](https://arxiv.org/abs/2210.07316) benchmark.


SFR-Embedding Team (∗indicates lead contributors).
* Rui Meng*
* Ye Liu*
* Shafiq Rayhan Joty
* Caiming Xiong
* Yingbo Zhou
* Semih Yavuz

### Citation
```bibtex
@misc{SFRAIResearch2024,
  title={SFR-Embedding-Mistral:Enhance Text Retrieval with Transfer Learning},
  author={Rui Meng, Ye Liu, Shafiq Rayhan Joty, Caiming Xiong, Yingbo Zhou, Semih Yavuz},
  howpublished={Salesforce AI Research Blog},
  year={2024},
  url={https://blog.salesforceairesearch.com/sfr-embedded-mistral/}
}
```





