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
- name: snowflake-arctic-m-long
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
      value: 78.4776119402985
    - type: ap
      value: 42.34374238166049
    - type: f1
      value: 72.51164234732224
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
      value: 78.7416
    - type: ap
      value: 73.12074819362377
    - type: f1
      value: 78.64057339708795
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
      value: 39.926
    - type: f1
      value: 39.35531993117573
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
      value: 34.851
    - type: map_at_10
      value: 51.473
    - type: map_at_100
      value: 52.103
    - type: map_at_1000
      value: 52.105000000000004
    - type: map_at_3
      value: 46.776
    - type: map_at_5
      value: 49.617
    - type: mrr_at_1
      value: 35.491
    - type: mrr_at_10
      value: 51.73799999999999
    - type: mrr_at_100
      value: 52.37500000000001
    - type: mrr_at_1000
      value: 52.378
    - type: mrr_at_3
      value: 46.965
    - type: mrr_at_5
      value: 49.878
    - type: ndcg_at_1
      value: 34.851
    - type: ndcg_at_10
      value: 60.364
    - type: ndcg_at_100
      value: 62.888999999999996
    - type: ndcg_at_1000
      value: 62.946000000000005
    - type: ndcg_at_3
      value: 50.807
    - type: ndcg_at_5
      value: 55.901
    - type: precision_at_1
      value: 34.851
    - type: precision_at_10
      value: 8.855
    - type: precision_at_100
      value: 0.992
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 20.839
    - type: precision_at_5
      value: 14.963999999999999
    - type: recall_at_1
      value: 34.851
    - type: recall_at_10
      value: 88.549
    - type: recall_at_100
      value: 99.21799999999999
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 62.517999999999994
    - type: recall_at_5
      value: 74.822
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
      value: 45.5554998405317
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
      value: 35.614248811397005
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
      value: 61.355489424753884
    - type: mrr
      value: 75.49443784900849
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
      value: 89.17311056578292
    - type: cos_sim_spearman
      value: 88.24237210809322
    - type: euclidean_pearson
      value: 87.3188065853646
    - type: euclidean_spearman
      value: 88.24237210809322
    - type: manhattan_pearson
      value: 86.89499710049658
    - type: manhattan_spearman
      value: 87.85441146091777
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
      value: 80.26298701298703
    - type: f1
      value: 79.68356764080303
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
      value: 20.923883720813706
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
      value: 36.16058801465044
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
      value: 30.1402356118627
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
      value: 35.612
    - type: map_at_10
      value: 47.117
    - type: map_at_100
      value: 48.711
    - type: map_at_1000
      value: 48.826
    - type: map_at_3
      value: 43.858999999999995
    - type: map_at_5
      value: 45.612
    - type: mrr_at_1
      value: 42.918
    - type: mrr_at_10
      value: 52.806
    - type: mrr_at_100
      value: 53.564
    - type: mrr_at_1000
      value: 53.596999999999994
    - type: mrr_at_3
      value: 50.453
    - type: mrr_at_5
      value: 51.841
    - type: ndcg_at_1
      value: 42.918
    - type: ndcg_at_10
      value: 53.291999999999994
    - type: ndcg_at_100
      value: 58.711999999999996
    - type: ndcg_at_1000
      value: 60.317
    - type: ndcg_at_3
      value: 48.855
    - type: ndcg_at_5
      value: 50.778
    - type: precision_at_1
      value: 42.918
    - type: precision_at_10
      value: 9.927999999999999
    - type: precision_at_100
      value: 1.592
    - type: precision_at_1000
      value: 0.201
    - type: precision_at_3
      value: 23.366999999999997
    - type: precision_at_5
      value: 16.366
    - type: recall_at_1
      value: 35.612
    - type: recall_at_10
      value: 64.671
    - type: recall_at_100
      value: 86.97
    - type: recall_at_1000
      value: 96.99600000000001
    - type: recall_at_3
      value: 51.37199999999999
    - type: recall_at_5
      value: 57.094
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
      value: 33.742
    - type: map_at_10
      value: 44.49
    - type: map_at_100
      value: 45.781
    - type: map_at_1000
      value: 45.902
    - type: map_at_3
      value: 41.453
    - type: map_at_5
      value: 43.251
    - type: mrr_at_1
      value: 42.357
    - type: mrr_at_10
      value: 50.463
    - type: mrr_at_100
      value: 51.17
    - type: mrr_at_1000
      value: 51.205999999999996
    - type: mrr_at_3
      value: 48.397
    - type: mrr_at_5
      value: 49.649
    - type: ndcg_at_1
      value: 42.357
    - type: ndcg_at_10
      value: 50.175000000000004
    - type: ndcg_at_100
      value: 54.491
    - type: ndcg_at_1000
      value: 56.282
    - type: ndcg_at_3
      value: 46.159
    - type: ndcg_at_5
      value: 48.226
    - type: precision_at_1
      value: 42.357
    - type: precision_at_10
      value: 9.382
    - type: precision_at_100
      value: 1.473
    - type: precision_at_1000
      value: 0.191
    - type: precision_at_3
      value: 22.187
    - type: precision_at_5
      value: 15.758
    - type: recall_at_1
      value: 33.742
    - type: recall_at_10
      value: 59.760999999999996
    - type: recall_at_100
      value: 77.89500000000001
    - type: recall_at_1000
      value: 89.005
    - type: recall_at_3
      value: 47.872
    - type: recall_at_5
      value: 53.559
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
      value: 43.883
    - type: map_at_10
      value: 56.464999999999996
    - type: map_at_100
      value: 57.394
    - type: map_at_1000
      value: 57.443999999999996
    - type: map_at_3
      value: 53.169
    - type: map_at_5
      value: 54.984
    - type: mrr_at_1
      value: 50.470000000000006
    - type: mrr_at_10
      value: 59.997
    - type: mrr_at_100
      value: 60.586
    - type: mrr_at_1000
      value: 60.61
    - type: mrr_at_3
      value: 57.837
    - type: mrr_at_5
      value: 59.019
    - type: ndcg_at_1
      value: 50.470000000000006
    - type: ndcg_at_10
      value: 62.134
    - type: ndcg_at_100
      value: 65.69500000000001
    - type: ndcg_at_1000
      value: 66.674
    - type: ndcg_at_3
      value: 56.916999999999994
    - type: ndcg_at_5
      value: 59.312
    - type: precision_at_1
      value: 50.470000000000006
    - type: precision_at_10
      value: 9.812
    - type: precision_at_100
      value: 1.25
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_3
      value: 25.119999999999997
    - type: precision_at_5
      value: 17.016000000000002
    - type: recall_at_1
      value: 43.883
    - type: recall_at_10
      value: 75.417
    - type: recall_at_100
      value: 90.545
    - type: recall_at_1000
      value: 97.44500000000001
    - type: recall_at_3
      value: 61.306000000000004
    - type: recall_at_5
      value: 67.244
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
      value: 29.813000000000002
    - type: map_at_10
      value: 38.627
    - type: map_at_100
      value: 39.735
    - type: map_at_1000
      value: 39.806000000000004
    - type: map_at_3
      value: 36.283
    - type: map_at_5
      value: 37.491
    - type: mrr_at_1
      value: 32.316
    - type: mrr_at_10
      value: 40.752
    - type: mrr_at_100
      value: 41.699000000000005
    - type: mrr_at_1000
      value: 41.749
    - type: mrr_at_3
      value: 38.531
    - type: mrr_at_5
      value: 39.706
    - type: ndcg_at_1
      value: 32.316
    - type: ndcg_at_10
      value: 43.524
    - type: ndcg_at_100
      value: 48.648
    - type: ndcg_at_1000
      value: 50.405
    - type: ndcg_at_3
      value: 38.928000000000004
    - type: ndcg_at_5
      value: 40.967
    - type: precision_at_1
      value: 32.316
    - type: precision_at_10
      value: 6.451999999999999
    - type: precision_at_100
      value: 0.9490000000000001
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 16.384
    - type: precision_at_5
      value: 11.006
    - type: recall_at_1
      value: 29.813000000000002
    - type: recall_at_10
      value: 56.562999999999995
    - type: recall_at_100
      value: 79.452
    - type: recall_at_1000
      value: 92.715
    - type: recall_at_3
      value: 43.985
    - type: recall_at_5
      value: 49.001
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
      value: 19.961000000000002
    - type: map_at_10
      value: 28.026
    - type: map_at_100
      value: 29.212
    - type: map_at_1000
      value: 29.332
    - type: map_at_3
      value: 25.296999999999997
    - type: map_at_5
      value: 26.832
    - type: mrr_at_1
      value: 24.627
    - type: mrr_at_10
      value: 33.045
    - type: mrr_at_100
      value: 33.944
    - type: mrr_at_1000
      value: 34.013
    - type: mrr_at_3
      value: 30.307000000000002
    - type: mrr_at_5
      value: 31.874000000000002
    - type: ndcg_at_1
      value: 24.627
    - type: ndcg_at_10
      value: 33.414
    - type: ndcg_at_100
      value: 39.061
    - type: ndcg_at_1000
      value: 41.795
    - type: ndcg_at_3
      value: 28.377000000000002
    - type: ndcg_at_5
      value: 30.781999999999996
    - type: precision_at_1
      value: 24.627
    - type: precision_at_10
      value: 6.02
    - type: precision_at_100
      value: 1.035
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: precision_at_3
      value: 13.516
    - type: precision_at_5
      value: 9.851
    - type: recall_at_1
      value: 19.961000000000002
    - type: recall_at_10
      value: 45.174
    - type: recall_at_100
      value: 69.69
    - type: recall_at_1000
      value: 89.24600000000001
    - type: recall_at_3
      value: 31.062
    - type: recall_at_5
      value: 37.193
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
      value: 32.080999999999996
    - type: map_at_10
      value: 42.177
    - type: map_at_100
      value: 43.431999999999995
    - type: map_at_1000
      value: 43.533
    - type: map_at_3
      value: 38.721
    - type: map_at_5
      value: 40.669
    - type: mrr_at_1
      value: 38.787
    - type: mrr_at_10
      value: 47.762
    - type: mrr_at_100
      value: 48.541000000000004
    - type: mrr_at_1000
      value: 48.581
    - type: mrr_at_3
      value: 45.123999999999995
    - type: mrr_at_5
      value: 46.639
    - type: ndcg_at_1
      value: 38.787
    - type: ndcg_at_10
      value: 48.094
    - type: ndcg_at_100
      value: 53.291
    - type: ndcg_at_1000
      value: 55.21
    - type: ndcg_at_3
      value: 42.721
    - type: ndcg_at_5
      value: 45.301
    - type: precision_at_1
      value: 38.787
    - type: precision_at_10
      value: 8.576
    - type: precision_at_100
      value: 1.306
    - type: precision_at_1000
      value: 0.164
    - type: precision_at_3
      value: 19.698
    - type: precision_at_5
      value: 14.013
    - type: recall_at_1
      value: 32.080999999999996
    - type: recall_at_10
      value: 59.948
    - type: recall_at_100
      value: 81.811
    - type: recall_at_1000
      value: 94.544
    - type: recall_at_3
      value: 44.903999999999996
    - type: recall_at_5
      value: 51.763999999999996
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
      value: 28.869
    - type: map_at_10
      value: 38.954
    - type: map_at_100
      value: 40.233000000000004
    - type: map_at_1000
      value: 40.332
    - type: map_at_3
      value: 35.585
    - type: map_at_5
      value: 37.476
    - type: mrr_at_1
      value: 35.959
    - type: mrr_at_10
      value: 44.800000000000004
    - type: mrr_at_100
      value: 45.609
    - type: mrr_at_1000
      value: 45.655
    - type: mrr_at_3
      value: 42.333
    - type: mrr_at_5
      value: 43.68
    - type: ndcg_at_1
      value: 35.959
    - type: ndcg_at_10
      value: 44.957
    - type: ndcg_at_100
      value: 50.275000000000006
    - type: ndcg_at_1000
      value: 52.29899999999999
    - type: ndcg_at_3
      value: 39.797
    - type: ndcg_at_5
      value: 42.128
    - type: precision_at_1
      value: 35.959
    - type: precision_at_10
      value: 8.185
    - type: precision_at_100
      value: 1.261
    - type: precision_at_1000
      value: 0.159
    - type: precision_at_3
      value: 18.988
    - type: precision_at_5
      value: 13.516
    - type: recall_at_1
      value: 28.869
    - type: recall_at_10
      value: 57.154
    - type: recall_at_100
      value: 79.764
    - type: recall_at_1000
      value: 93.515
    - type: recall_at_3
      value: 42.364000000000004
    - type: recall_at_5
      value: 48.756
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
      value: 29.31008333333333
    - type: map_at_10
      value: 38.81849999999999
    - type: map_at_100
      value: 40.05058333333334
    - type: map_at_1000
      value: 40.16116666666667
    - type: map_at_3
      value: 35.91441666666667
    - type: map_at_5
      value: 37.526583333333335
    - type: mrr_at_1
      value: 34.60066666666667
    - type: mrr_at_10
      value: 43.08858333333333
    - type: mrr_at_100
      value: 43.927749999999996
    - type: mrr_at_1000
      value: 43.97866666666667
    - type: mrr_at_3
      value: 40.72775
    - type: mrr_at_5
      value: 42.067249999999994
    - type: ndcg_at_1
      value: 34.60066666666667
    - type: ndcg_at_10
      value: 44.20841666666667
    - type: ndcg_at_100
      value: 49.32866666666667
    - type: ndcg_at_1000
      value: 51.373999999999995
    - type: ndcg_at_3
      value: 39.452083333333334
    - type: ndcg_at_5
      value: 41.67
    - type: precision_at_1
      value: 34.60066666666667
    - type: precision_at_10
      value: 7.616583333333334
    - type: precision_at_100
      value: 1.20175
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 17.992
    - type: precision_at_5
      value: 12.658416666666666
    - type: recall_at_1
      value: 29.31008333333333
    - type: recall_at_10
      value: 55.81900000000001
    - type: recall_at_100
      value: 78.06308333333334
    - type: recall_at_1000
      value: 92.10641666666668
    - type: recall_at_3
      value: 42.50166666666667
    - type: recall_at_5
      value: 48.26108333333333
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
      value: 26.773000000000003
    - type: map_at_10
      value: 34.13
    - type: map_at_100
      value: 35.113
    - type: map_at_1000
      value: 35.211
    - type: map_at_3
      value: 31.958
    - type: map_at_5
      value: 33.080999999999996
    - type: mrr_at_1
      value: 30.061
    - type: mrr_at_10
      value: 37.061
    - type: mrr_at_100
      value: 37.865
    - type: mrr_at_1000
      value: 37.939
    - type: mrr_at_3
      value: 34.995
    - type: mrr_at_5
      value: 36.092
    - type: ndcg_at_1
      value: 30.061
    - type: ndcg_at_10
      value: 38.391999999999996
    - type: ndcg_at_100
      value: 43.13
    - type: ndcg_at_1000
      value: 45.449
    - type: ndcg_at_3
      value: 34.411
    - type: ndcg_at_5
      value: 36.163000000000004
    - type: precision_at_1
      value: 30.061
    - type: precision_at_10
      value: 5.982
    - type: precision_at_100
      value: 0.911
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: precision_at_3
      value: 14.673
    - type: precision_at_5
      value: 10.030999999999999
    - type: recall_at_1
      value: 26.773000000000003
    - type: recall_at_10
      value: 48.445
    - type: recall_at_100
      value: 69.741
    - type: recall_at_1000
      value: 86.59
    - type: recall_at_3
      value: 37.576
    - type: recall_at_5
      value: 41.948
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
      value: 18.556
    - type: map_at_10
      value: 26.340999999999998
    - type: map_at_100
      value: 27.560000000000002
    - type: map_at_1000
      value: 27.685
    - type: map_at_3
      value: 24.136
    - type: map_at_5
      value: 25.34
    - type: mrr_at_1
      value: 22.368
    - type: mrr_at_10
      value: 30.192999999999998
    - type: mrr_at_100
      value: 31.183
    - type: mrr_at_1000
      value: 31.258000000000003
    - type: mrr_at_3
      value: 28.223
    - type: mrr_at_5
      value: 29.294999999999998
    - type: ndcg_at_1
      value: 22.368
    - type: ndcg_at_10
      value: 31.029
    - type: ndcg_at_100
      value: 36.768
    - type: ndcg_at_1000
      value: 39.572
    - type: ndcg_at_3
      value: 27.197
    - type: ndcg_at_5
      value: 28.912
    - type: precision_at_1
      value: 22.368
    - type: precision_at_10
      value: 5.606
    - type: precision_at_100
      value: 0.9979999999999999
    - type: precision_at_1000
      value: 0.14100000000000001
    - type: precision_at_3
      value: 12.892999999999999
    - type: precision_at_5
      value: 9.16
    - type: recall_at_1
      value: 18.556
    - type: recall_at_10
      value: 41.087
    - type: recall_at_100
      value: 66.92
    - type: recall_at_1000
      value: 86.691
    - type: recall_at_3
      value: 30.415
    - type: recall_at_5
      value: 34.813
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
      value: 29.953999999999997
    - type: map_at_10
      value: 39.633
    - type: map_at_100
      value: 40.923
    - type: map_at_1000
      value: 41.016000000000005
    - type: map_at_3
      value: 36.609
    - type: map_at_5
      value: 38.443
    - type: mrr_at_1
      value: 35.354
    - type: mrr_at_10
      value: 43.718
    - type: mrr_at_100
      value: 44.651999999999994
    - type: mrr_at_1000
      value: 44.696000000000005
    - type: mrr_at_3
      value: 41.154
    - type: mrr_at_5
      value: 42.730000000000004
    - type: ndcg_at_1
      value: 35.354
    - type: ndcg_at_10
      value: 44.933
    - type: ndcg_at_100
      value: 50.577000000000005
    - type: ndcg_at_1000
      value: 52.428
    - type: ndcg_at_3
      value: 39.833
    - type: ndcg_at_5
      value: 42.465
    - type: precision_at_1
      value: 35.354
    - type: precision_at_10
      value: 7.416
    - type: precision_at_100
      value: 1.157
    - type: precision_at_1000
      value: 0.14100000000000001
    - type: precision_at_3
      value: 17.817
    - type: precision_at_5
      value: 12.687000000000001
    - type: recall_at_1
      value: 29.953999999999997
    - type: recall_at_10
      value: 56.932
    - type: recall_at_100
      value: 80.93900000000001
    - type: recall_at_1000
      value: 93.582
    - type: recall_at_3
      value: 43.192
    - type: recall_at_5
      value: 49.757
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
      value: 27.85
    - type: map_at_10
      value: 37.68
    - type: map_at_100
      value: 39.295
    - type: map_at_1000
      value: 39.527
    - type: map_at_3
      value: 35.036
    - type: map_at_5
      value: 36.269
    - type: mrr_at_1
      value: 33.004
    - type: mrr_at_10
      value: 42.096000000000004
    - type: mrr_at_100
      value: 43.019
    - type: mrr_at_1000
      value: 43.071
    - type: mrr_at_3
      value: 39.987
    - type: mrr_at_5
      value: 40.995
    - type: ndcg_at_1
      value: 33.004
    - type: ndcg_at_10
      value: 43.461
    - type: ndcg_at_100
      value: 49.138
    - type: ndcg_at_1000
      value: 51.50900000000001
    - type: ndcg_at_3
      value: 39.317
    - type: ndcg_at_5
      value: 40.760999999999996
    - type: precision_at_1
      value: 33.004
    - type: precision_at_10
      value: 8.161999999999999
    - type: precision_at_100
      value: 1.583
    - type: precision_at_1000
      value: 0.245
    - type: precision_at_3
      value: 18.445
    - type: precision_at_5
      value: 12.885
    - type: recall_at_1
      value: 27.85
    - type: recall_at_10
      value: 54.419
    - type: recall_at_100
      value: 79.742
    - type: recall_at_1000
      value: 93.97
    - type: recall_at_3
      value: 42.149
    - type: recall_at_5
      value: 46.165
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
      value: 24.627
    - type: map_at_10
      value: 32.182
    - type: map_at_100
      value: 33.217999999999996
    - type: map_at_1000
      value: 33.32
    - type: map_at_3
      value: 28.866999999999997
    - type: map_at_5
      value: 30.871
    - type: mrr_at_1
      value: 26.987
    - type: mrr_at_10
      value: 34.37
    - type: mrr_at_100
      value: 35.301
    - type: mrr_at_1000
      value: 35.369
    - type: mrr_at_3
      value: 31.391999999999996
    - type: mrr_at_5
      value: 33.287
    - type: ndcg_at_1
      value: 26.987
    - type: ndcg_at_10
      value: 37.096000000000004
    - type: ndcg_at_100
      value: 42.158
    - type: ndcg_at_1000
      value: 44.548
    - type: ndcg_at_3
      value: 30.913
    - type: ndcg_at_5
      value: 34.245
    - type: precision_at_1
      value: 26.987
    - type: precision_at_10
      value: 5.878
    - type: precision_at_100
      value: 0.906
    - type: precision_at_1000
      value: 0.123
    - type: precision_at_3
      value: 12.815999999999999
    - type: precision_at_5
      value: 9.612
    - type: recall_at_1
      value: 24.627
    - type: recall_at_10
      value: 50.257
    - type: recall_at_100
      value: 73.288
    - type: recall_at_1000
      value: 90.97800000000001
    - type: recall_at_3
      value: 33.823
    - type: recall_at_5
      value: 41.839
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
      value: 17.343
    - type: map_at_10
      value: 28.59
    - type: map_at_100
      value: 30.591
    - type: map_at_1000
      value: 30.759999999999998
    - type: map_at_3
      value: 24.197
    - type: map_at_5
      value: 26.433
    - type: mrr_at_1
      value: 39.609
    - type: mrr_at_10
      value: 51.107
    - type: mrr_at_100
      value: 51.87199999999999
    - type: mrr_at_1000
      value: 51.894
    - type: mrr_at_3
      value: 48.154
    - type: mrr_at_5
      value: 49.939
    - type: ndcg_at_1
      value: 39.609
    - type: ndcg_at_10
      value: 38.329
    - type: ndcg_at_100
      value: 45.573
    - type: ndcg_at_1000
      value: 48.405
    - type: ndcg_at_3
      value: 32.506
    - type: ndcg_at_5
      value: 34.331
    - type: precision_at_1
      value: 39.609
    - type: precision_at_10
      value: 11.668000000000001
    - type: precision_at_100
      value: 1.9539999999999997
    - type: precision_at_1000
      value: 0.249
    - type: precision_at_3
      value: 23.952
    - type: precision_at_5
      value: 17.902
    - type: recall_at_1
      value: 17.343
    - type: recall_at_10
      value: 43.704
    - type: recall_at_100
      value: 68.363
    - type: recall_at_1000
      value: 84.04599999999999
    - type: recall_at_3
      value: 29.028
    - type: recall_at_5
      value: 35.022
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
      value: 9.934999999999999
    - type: map_at_10
      value: 22.081
    - type: map_at_100
      value: 32.036
    - type: map_at_1000
      value: 33.803
    - type: map_at_3
      value: 15.687999999999999
    - type: map_at_5
      value: 18.357
    - type: mrr_at_1
      value: 70.75
    - type: mrr_at_10
      value: 78.506
    - type: mrr_at_100
      value: 78.874
    - type: mrr_at_1000
      value: 78.88300000000001
    - type: mrr_at_3
      value: 77.667
    - type: mrr_at_5
      value: 78.342
    - type: ndcg_at_1
      value: 57.25
    - type: ndcg_at_10
      value: 45.286
    - type: ndcg_at_100
      value: 50.791
    - type: ndcg_at_1000
      value: 58.021
    - type: ndcg_at_3
      value: 49.504
    - type: ndcg_at_5
      value: 47.03
    - type: precision_at_1
      value: 70.75
    - type: precision_at_10
      value: 36.425000000000004
    - type: precision_at_100
      value: 11.953
    - type: precision_at_1000
      value: 2.248
    - type: precision_at_3
      value: 53.25
    - type: precision_at_5
      value: 46.150000000000006
    - type: recall_at_1
      value: 9.934999999999999
    - type: recall_at_10
      value: 27.592
    - type: recall_at_100
      value: 58.089
    - type: recall_at_1000
      value: 81.025
    - type: recall_at_3
      value: 17.048
    - type: recall_at_5
      value: 20.834
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
      value: 47.25999999999999
    - type: f1
      value: 43.83371155132253
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
      value: 73.68900000000001
    - type: map_at_10
      value: 82.878
    - type: map_at_100
      value: 83.084
    - type: map_at_1000
      value: 83.097
    - type: map_at_3
      value: 81.528
    - type: map_at_5
      value: 82.432
    - type: mrr_at_1
      value: 79.49300000000001
    - type: mrr_at_10
      value: 87.24300000000001
    - type: mrr_at_100
      value: 87.3
    - type: mrr_at_1000
      value: 87.301
    - type: mrr_at_3
      value: 86.359
    - type: mrr_at_5
      value: 87.01
    - type: ndcg_at_1
      value: 79.49300000000001
    - type: ndcg_at_10
      value: 86.894
    - type: ndcg_at_100
      value: 87.6
    - type: ndcg_at_1000
      value: 87.79299999999999
    - type: ndcg_at_3
      value: 84.777
    - type: ndcg_at_5
      value: 86.08
    - type: precision_at_1
      value: 79.49300000000001
    - type: precision_at_10
      value: 10.578
    - type: precision_at_100
      value: 1.117
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 32.592999999999996
    - type: precision_at_5
      value: 20.423
    - type: recall_at_1
      value: 73.68900000000001
    - type: recall_at_10
      value: 94.833
    - type: recall_at_100
      value: 97.554
    - type: recall_at_1000
      value: 98.672
    - type: recall_at_3
      value: 89.236
    - type: recall_at_5
      value: 92.461
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
      value: 20.59
    - type: map_at_10
      value: 34.089000000000006
    - type: map_at_100
      value: 35.796
    - type: map_at_1000
      value: 35.988
    - type: map_at_3
      value: 29.877
    - type: map_at_5
      value: 32.202999999999996
    - type: mrr_at_1
      value: 41.049
    - type: mrr_at_10
      value: 50.370000000000005
    - type: mrr_at_100
      value: 51.209
    - type: mrr_at_1000
      value: 51.247
    - type: mrr_at_3
      value: 48.122
    - type: mrr_at_5
      value: 49.326
    - type: ndcg_at_1
      value: 41.049
    - type: ndcg_at_10
      value: 42.163000000000004
    - type: ndcg_at_100
      value: 48.638999999999996
    - type: ndcg_at_1000
      value: 51.775000000000006
    - type: ndcg_at_3
      value: 38.435
    - type: ndcg_at_5
      value: 39.561
    - type: precision_at_1
      value: 41.049
    - type: precision_at_10
      value: 11.481
    - type: precision_at_100
      value: 1.8239999999999998
    - type: precision_at_1000
      value: 0.24
    - type: precision_at_3
      value: 25.257
    - type: precision_at_5
      value: 18.519
    - type: recall_at_1
      value: 20.59
    - type: recall_at_10
      value: 49.547999999999995
    - type: recall_at_100
      value: 73.676
    - type: recall_at_1000
      value: 92.269
    - type: recall_at_3
      value: 35.656
    - type: recall_at_5
      value: 41.455
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
      value: 39.932
    - type: map_at_10
      value: 64.184
    - type: map_at_100
      value: 65.06
    - type: map_at_1000
      value: 65.109
    - type: map_at_3
      value: 60.27
    - type: map_at_5
      value: 62.732
    - type: mrr_at_1
      value: 79.865
    - type: mrr_at_10
      value: 85.99799999999999
    - type: mrr_at_100
      value: 86.13
    - type: mrr_at_1000
      value: 86.13300000000001
    - type: mrr_at_3
      value: 85.136
    - type: mrr_at_5
      value: 85.69200000000001
    - type: ndcg_at_1
      value: 79.865
    - type: ndcg_at_10
      value: 72.756
    - type: ndcg_at_100
      value: 75.638
    - type: ndcg_at_1000
      value: 76.589
    - type: ndcg_at_3
      value: 67.38199999999999
    - type: ndcg_at_5
      value: 70.402
    - type: precision_at_1
      value: 79.865
    - type: precision_at_10
      value: 15.387999999999998
    - type: precision_at_100
      value: 1.7610000000000001
    - type: precision_at_1000
      value: 0.189
    - type: precision_at_3
      value: 43.394
    - type: precision_at_5
      value: 28.424
    - type: recall_at_1
      value: 39.932
    - type: recall_at_10
      value: 76.941
    - type: recall_at_100
      value: 88.062
    - type: recall_at_1000
      value: 94.396
    - type: recall_at_3
      value: 65.091
    - type: recall_at_5
      value: 71.06
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
      value: 71.7904
    - type: ap
      value: 65.82899456730257
    - type: f1
      value: 71.56611877410202
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
      value: 21.931
    - type: map_at_10
      value: 34.849999999999994
    - type: map_at_100
      value: 36.033
    - type: map_at_1000
      value: 36.08
    - type: map_at_3
      value: 30.842000000000002
    - type: map_at_5
      value: 33.229
    - type: mrr_at_1
      value: 22.55
    - type: mrr_at_10
      value: 35.436
    - type: mrr_at_100
      value: 36.563
    - type: mrr_at_1000
      value: 36.604
    - type: mrr_at_3
      value: 31.507
    - type: mrr_at_5
      value: 33.851
    - type: ndcg_at_1
      value: 22.55
    - type: ndcg_at_10
      value: 41.969
    - type: ndcg_at_100
      value: 47.576
    - type: ndcg_at_1000
      value: 48.731
    - type: ndcg_at_3
      value: 33.894000000000005
    - type: ndcg_at_5
      value: 38.133
    - type: precision_at_1
      value: 22.55
    - type: precision_at_10
      value: 6.660000000000001
    - type: precision_at_100
      value: 0.946
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 14.532
    - type: precision_at_5
      value: 10.865
    - type: recall_at_1
      value: 21.931
    - type: recall_at_10
      value: 63.841
    - type: recall_at_100
      value: 89.47699999999999
    - type: recall_at_1000
      value: 98.259
    - type: recall_at_3
      value: 42.063
    - type: recall_at_5
      value: 52.21
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
      value: 93.03921568627452
    - type: f1
      value: 92.56400672314416
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
      value: 63.515731874145
    - type: f1
      value: 44.922310875523216
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
      value: 77.57383966244727
    - type: f1
      value: 76.55222378218293
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
      value: 62.74836240280833
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
      value: 24.414348715238184
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
      value: 66.54673839946201
    - type: f1
      value: 64.61004101532164
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
      value: 73.11365164761264
    - type: f1
      value: 72.01684013680978
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
      value: 31.123671999617297
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
      value: 26.72684341430875
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
      value: 29.910228061734816
    - type: mrr
      value: 30.835255982532477
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
      value: 5.6770000000000005
    - type: map_at_10
      value: 13.15
    - type: map_at_100
      value: 16.205
    - type: map_at_1000
      value: 17.580000000000002
    - type: map_at_3
      value: 9.651
    - type: map_at_5
      value: 11.142000000000001
    - type: mrr_at_1
      value: 47.678
    - type: mrr_at_10
      value: 56.257000000000005
    - type: mrr_at_100
      value: 56.708000000000006
    - type: mrr_at_1000
      value: 56.751
    - type: mrr_at_3
      value: 54.128
    - type: mrr_at_5
      value: 55.181000000000004
    - type: ndcg_at_1
      value: 45.511
    - type: ndcg_at_10
      value: 35.867
    - type: ndcg_at_100
      value: 31.566
    - type: ndcg_at_1000
      value: 40.077
    - type: ndcg_at_3
      value: 41.9
    - type: ndcg_at_5
      value: 39.367999999999995
    - type: precision_at_1
      value: 47.678
    - type: precision_at_10
      value: 26.842
    - type: precision_at_100
      value: 7.991
    - type: precision_at_1000
      value: 2.0469999999999997
    - type: precision_at_3
      value: 39.938
    - type: precision_at_5
      value: 34.613
    - type: recall_at_1
      value: 5.6770000000000005
    - type: recall_at_10
      value: 17.119999999999997
    - type: recall_at_100
      value: 30.828
    - type: recall_at_1000
      value: 62.082
    - type: recall_at_3
      value: 10.456
    - type: recall_at_5
      value: 12.903999999999998
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
      value: 39.021
    - type: map_at_10
      value: 54.976
    - type: map_at_100
      value: 55.793000000000006
    - type: map_at_1000
      value: 55.811
    - type: map_at_3
      value: 50.759
    - type: map_at_5
      value: 53.429
    - type: mrr_at_1
      value: 43.308
    - type: mrr_at_10
      value: 57.118
    - type: mrr_at_100
      value: 57.69499999999999
    - type: mrr_at_1000
      value: 57.704
    - type: mrr_at_3
      value: 53.848
    - type: mrr_at_5
      value: 55.915000000000006
    - type: ndcg_at_1
      value: 43.308
    - type: ndcg_at_10
      value: 62.33800000000001
    - type: ndcg_at_100
      value: 65.61099999999999
    - type: ndcg_at_1000
      value: 65.995
    - type: ndcg_at_3
      value: 54.723
    - type: ndcg_at_5
      value: 59.026
    - type: precision_at_1
      value: 43.308
    - type: precision_at_10
      value: 9.803
    - type: precision_at_100
      value: 1.167
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 24.334
    - type: precision_at_5
      value: 17.144000000000002
    - type: recall_at_1
      value: 39.021
    - type: recall_at_10
      value: 82.37299999999999
    - type: recall_at_100
      value: 96.21499999999999
    - type: recall_at_1000
      value: 99.02499999999999
    - type: recall_at_3
      value: 63.031000000000006
    - type: recall_at_5
      value: 72.856
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
      value: 78.03289473684211
    - type: f1
      value: 77.89323745730803
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
      value: 100.0
    - type: cos_sim_f1
      value: 99.9490575649516
    - type: cos_sim_precision
      value: 100.0
    - type: cos_sim_recall
      value: 99.89816700610999
    - type: dot_accuracy
      value: 99.89816700610999
    - type: dot_ap
      value: 100.0
    - type: dot_f1
      value: 99.9490575649516
    - type: dot_precision
      value: 100.0
    - type: dot_recall
      value: 99.89816700610999
    - type: euclidean_accuracy
      value: 99.89816700610999
    - type: euclidean_ap
      value: 100.0
    - type: euclidean_f1
      value: 99.9490575649516
    - type: euclidean_precision
      value: 100.0
    - type: euclidean_recall
      value: 99.89816700610999
    - type: manhattan_accuracy
      value: 99.89816700610999
    - type: manhattan_ap
      value: 100.0
    - type: manhattan_f1
      value: 99.9490575649516
    - type: manhattan_precision
      value: 100.0
    - type: manhattan_recall
      value: 99.89816700610999
    - type: max_accuracy
      value: 99.89816700610999
    - type: max_ap
      value: 100.0
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
      value: 59.578879568280385
    - type: cos_sim_f1
      value: 62.50861474844934
    - type: cos_sim_precision
      value: 45.46365914786967
    - type: cos_sim_recall
      value: 100.0
    - type: dot_accuracy
      value: 61.75000000000001
    - type: dot_ap
      value: 59.57893088951573
    - type: dot_f1
      value: 62.50861474844934
    - type: dot_precision
      value: 45.46365914786967
    - type: dot_recall
      value: 100.0
    - type: euclidean_accuracy
      value: 61.75000000000001
    - type: euclidean_ap
      value: 59.578755624671686
    - type: euclidean_f1
      value: 62.50861474844934
    - type: euclidean_precision
      value: 45.46365914786967
    - type: euclidean_recall
      value: 100.0
    - type: manhattan_accuracy
      value: 61.75000000000001
    - type: manhattan_ap
      value: 59.58504334461159
    - type: manhattan_f1
      value: 62.50861474844934
    - type: manhattan_precision
      value: 45.46365914786967
    - type: manhattan_recall
      value: 100.0
    - type: max_accuracy
      value: 61.75000000000001
    - type: max_ap
      value: 59.58504334461159
    - type: max_f1
      value: 62.50861474844934
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
      value: 70.186
    - type: map_at_10
      value: 83.875
    - type: map_at_100
      value: 84.514
    - type: map_at_1000
      value: 84.53500000000001
    - type: map_at_3
      value: 80.926
    - type: map_at_5
      value: 82.797
    - type: mrr_at_1
      value: 80.82000000000001
    - type: mrr_at_10
      value: 87.068
    - type: mrr_at_100
      value: 87.178
    - type: mrr_at_1000
      value: 87.18
    - type: mrr_at_3
      value: 86.055
    - type: mrr_at_5
      value: 86.763
    - type: ndcg_at_1
      value: 80.84
    - type: ndcg_at_10
      value: 87.723
    - type: ndcg_at_100
      value: 88.98700000000001
    - type: ndcg_at_1000
      value: 89.13499999999999
    - type: ndcg_at_3
      value: 84.821
    - type: ndcg_at_5
      value: 86.441
    - type: precision_at_1
      value: 80.84
    - type: precision_at_10
      value: 13.270000000000001
    - type: precision_at_100
      value: 1.516
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 37.013
    - type: precision_at_5
      value: 24.37
    - type: recall_at_1
      value: 70.186
    - type: recall_at_10
      value: 94.948
    - type: recall_at_100
      value: 99.223
    - type: recall_at_1000
      value: 99.932
    - type: recall_at_3
      value: 86.57000000000001
    - type: recall_at_5
      value: 91.157
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
      value: 50.24198927949519
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
      value: 61.452073078765544
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
      value: 4.972
    - type: map_at_10
      value: 12.314
    - type: map_at_100
      value: 14.333000000000002
    - type: map_at_1000
      value: 14.628
    - type: map_at_3
      value: 8.972
    - type: map_at_5
      value: 10.724
    - type: mrr_at_1
      value: 24.4
    - type: mrr_at_10
      value: 35.257
    - type: mrr_at_100
      value: 36.297000000000004
    - type: mrr_at_1000
      value: 36.363
    - type: mrr_at_3
      value: 32.267
    - type: mrr_at_5
      value: 33.942
    - type: ndcg_at_1
      value: 24.4
    - type: ndcg_at_10
      value: 20.47
    - type: ndcg_at_100
      value: 28.111000000000004
    - type: ndcg_at_1000
      value: 33.499
    - type: ndcg_at_3
      value: 19.975
    - type: ndcg_at_5
      value: 17.293
    - type: precision_at_1
      value: 24.4
    - type: precision_at_10
      value: 10.440000000000001
    - type: precision_at_100
      value: 2.136
    - type: precision_at_1000
      value: 0.34299999999999997
    - type: precision_at_3
      value: 18.733
    - type: precision_at_5
      value: 15.120000000000001
    - type: recall_at_1
      value: 4.972
    - type: recall_at_10
      value: 21.157
    - type: recall_at_100
      value: 43.335
    - type: recall_at_1000
      value: 69.652
    - type: recall_at_3
      value: 11.417
    - type: recall_at_5
      value: 15.317
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
      value: 76.70295978506286
    - type: cos_sim_spearman
      value: 70.91162732446628
    - type: euclidean_pearson
      value: 73.25693688746031
    - type: euclidean_spearman
      value: 70.91162556180127
    - type: manhattan_pearson
      value: 73.27735004735767
    - type: manhattan_spearman
      value: 70.8856787022704
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
      value: 67.55878682646774
    - type: cos_sim_spearman
      value: 66.10824660353681
    - type: euclidean_pearson
      value: 64.93937270068541
    - type: euclidean_spearman
      value: 66.10824660353681
    - type: manhattan_pearson
      value: 64.96325555978984
    - type: manhattan_spearman
      value: 66.12052481638577
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
      value: 79.79979774019496
    - type: cos_sim_spearman
      value: 79.82293444619499
    - type: euclidean_pearson
      value: 79.4830436509311
    - type: euclidean_spearman
      value: 79.82293444619499
    - type: manhattan_pearson
      value: 79.49785594799296
    - type: manhattan_spearman
      value: 79.8280390479434
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
      value: 76.36839628231121
    - type: cos_sim_spearman
      value: 73.63809739428072
    - type: euclidean_pearson
      value: 74.93718121215906
    - type: euclidean_spearman
      value: 73.63810227650436
    - type: manhattan_pearson
      value: 74.8737197659424
    - type: manhattan_spearman
      value: 73.57534688126572
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
      value: 82.67482138157656
    - type: cos_sim_spearman
      value: 83.23485786963107
    - type: euclidean_pearson
      value: 82.50847772197369
    - type: euclidean_spearman
      value: 83.23485786963107
    - type: manhattan_pearson
      value: 82.48916218377576
    - type: manhattan_spearman
      value: 83.19756483500014
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
      value: 81.11626268793967
    - type: cos_sim_spearman
      value: 81.58184691061507
    - type: euclidean_pearson
      value: 80.65900869004938
    - type: euclidean_spearman
      value: 81.58184691061507
    - type: manhattan_pearson
      value: 80.67912306966772
    - type: manhattan_spearman
      value: 81.59957593393145
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
      value: 80.3140990821409
    - type: cos_sim_spearman
      value: 80.59196586367551
    - type: euclidean_pearson
      value: 80.73014029317672
    - type: euclidean_spearman
      value: 80.59196586367551
    - type: manhattan_pearson
      value: 80.5774325136987
    - type: manhattan_spearman
      value: 80.35102610546238
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
      value: 68.34450491529164
    - type: cos_sim_spearman
      value: 68.79451793414492
    - type: euclidean_pearson
      value: 68.75619738499324
    - type: euclidean_spearman
      value: 68.79451793414492
    - type: manhattan_pearson
      value: 68.75256119543882
    - type: manhattan_spearman
      value: 68.81836416978547
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
      value: 77.95580414975612
    - type: cos_sim_spearman
      value: 77.89671867168987
    - type: euclidean_pearson
      value: 77.61352097720862
    - type: euclidean_spearman
      value: 77.89671867168987
    - type: manhattan_pearson
      value: 77.65282228135632
    - type: manhattan_spearman
      value: 77.91730533156762
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
      value: 77.95580421496413
    - type: cos_sim_spearman
      value: 77.89671867168987
    - type: euclidean_pearson
      value: 77.61352107168794
    - type: euclidean_spearman
      value: 77.89671867168987
    - type: manhattan_pearson
      value: 77.65282237231794
    - type: manhattan_spearman
      value: 77.91730533156762
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
      value: 79.22928110092924
    - type: mrr
      value: 94.46700902583257
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
      value: 56.011
    - type: map_at_10
      value: 65.544
    - type: map_at_100
      value: 66.034
    - type: map_at_1000
      value: 66.065
    - type: map_at_3
      value: 63.077000000000005
    - type: map_at_5
      value: 64.354
    - type: mrr_at_1
      value: 59.0
    - type: mrr_at_10
      value: 66.74900000000001
    - type: mrr_at_100
      value: 67.176
    - type: mrr_at_1000
      value: 67.203
    - type: mrr_at_3
      value: 65.056
    - type: mrr_at_5
      value: 65.956
    - type: ndcg_at_1
      value: 59.0
    - type: ndcg_at_10
      value: 69.95599999999999
    - type: ndcg_at_100
      value: 72.27
    - type: ndcg_at_1000
      value: 73.066
    - type: ndcg_at_3
      value: 65.837
    - type: ndcg_at_5
      value: 67.633
    - type: precision_at_1
      value: 59.0
    - type: precision_at_10
      value: 9.333
    - type: precision_at_100
      value: 1.053
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 26.0
    - type: precision_at_5
      value: 16.866999999999997
    - type: recall_at_1
      value: 56.011
    - type: recall_at_10
      value: 82.133
    - type: recall_at_100
      value: 92.767
    - type: recall_at_1000
      value: 99.0
    - type: recall_at_3
      value: 70.95
    - type: recall_at_5
      value: 75.556
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
      value: 99.81584158415842
    - type: cos_sim_ap
      value: 94.67482871230736
    - type: cos_sim_f1
      value: 90.67201604814443
    - type: cos_sim_precision
      value: 90.94567404426559
    - type: cos_sim_recall
      value: 90.4
    - type: dot_accuracy
      value: 99.81584158415842
    - type: dot_ap
      value: 94.67482871230737
    - type: dot_f1
      value: 90.67201604814443
    - type: dot_precision
      value: 90.94567404426559
    - type: dot_recall
      value: 90.4
    - type: euclidean_accuracy
      value: 99.81584158415842
    - type: euclidean_ap
      value: 94.67482871230737
    - type: euclidean_f1
      value: 90.67201604814443
    - type: euclidean_precision
      value: 90.94567404426559
    - type: euclidean_recall
      value: 90.4
    - type: manhattan_accuracy
      value: 99.81188118811882
    - type: manhattan_ap
      value: 94.6409082219286
    - type: manhattan_f1
      value: 90.50949050949052
    - type: manhattan_precision
      value: 90.41916167664671
    - type: manhattan_recall
      value: 90.60000000000001
    - type: max_accuracy
      value: 99.81584158415842
    - type: max_ap
      value: 94.67482871230737
    - type: max_f1
      value: 90.67201604814443
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
      value: 62.63494511649264
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
      value: 37.165838327685755
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
      value: 51.384873075208084
    - type: mrr
      value: 52.196439181733304
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
      value: 32.13690355567596
    - type: cos_sim_spearman
      value: 31.38349778638125
    - type: dot_pearson
      value: 32.13689596691593
    - type: dot_spearman
      value: 31.38349778638125
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
      value: 0.26
    - type: map_at_10
      value: 2.08
    - type: map_at_100
      value: 12.598
    - type: map_at_1000
      value: 30.119
    - type: map_at_3
      value: 0.701
    - type: map_at_5
      value: 1.11
    - type: mrr_at_1
      value: 96.0
    - type: mrr_at_10
      value: 97.167
    - type: mrr_at_100
      value: 97.167
    - type: mrr_at_1000
      value: 97.167
    - type: mrr_at_3
      value: 96.667
    - type: mrr_at_5
      value: 97.167
    - type: ndcg_at_1
      value: 91.0
    - type: ndcg_at_10
      value: 81.69800000000001
    - type: ndcg_at_100
      value: 62.9
    - type: ndcg_at_1000
      value: 55.245999999999995
    - type: ndcg_at_3
      value: 86.397
    - type: ndcg_at_5
      value: 84.286
    - type: precision_at_1
      value: 96.0
    - type: precision_at_10
      value: 87.0
    - type: precision_at_100
      value: 64.86
    - type: precision_at_1000
      value: 24.512
    - type: precision_at_3
      value: 90.667
    - type: precision_at_5
      value: 88.8
    - type: recall_at_1
      value: 0.26
    - type: recall_at_10
      value: 2.238
    - type: recall_at_100
      value: 15.488
    - type: recall_at_1000
      value: 51.6
    - type: recall_at_3
      value: 0.716
    - type: recall_at_5
      value: 1.151
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
      value: 3.376
    - type: map_at_10
      value: 13.142000000000001
    - type: map_at_100
      value: 19.763
    - type: map_at_1000
      value: 21.319
    - type: map_at_3
      value: 6.805999999999999
    - type: map_at_5
      value: 8.952
    - type: mrr_at_1
      value: 46.939
    - type: mrr_at_10
      value: 61.082
    - type: mrr_at_100
      value: 61.45
    - type: mrr_at_1000
      value: 61.468999999999994
    - type: mrr_at_3
      value: 57.483
    - type: mrr_at_5
      value: 59.931999999999995
    - type: ndcg_at_1
      value: 44.897999999999996
    - type: ndcg_at_10
      value: 32.35
    - type: ndcg_at_100
      value: 42.719
    - type: ndcg_at_1000
      value: 53.30200000000001
    - type: ndcg_at_3
      value: 37.724999999999994
    - type: ndcg_at_5
      value: 34.79
    - type: precision_at_1
      value: 46.939
    - type: precision_at_10
      value: 28.366999999999997
    - type: precision_at_100
      value: 8.429
    - type: precision_at_1000
      value: 1.557
    - type: precision_at_3
      value: 38.095
    - type: precision_at_5
      value: 33.469
    - type: recall_at_1
      value: 3.376
    - type: recall_at_10
      value: 20.164
    - type: recall_at_100
      value: 50.668
    - type: recall_at_1000
      value: 83.159
    - type: recall_at_3
      value: 8.155
    - type: recall_at_5
      value: 11.872
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
      value: 66.739
    - type: ap
      value: 12.17931839228834
    - type: f1
      value: 51.05383188624636
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
      value: 56.72891907187323
    - type: f1
      value: 56.997614557150946
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
      value: 39.825318429345224
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
      value: 83.65619598259522
    - type: cos_sim_ap
      value: 66.17412885183877
    - type: cos_sim_f1
      value: 63.09125656951745
    - type: cos_sim_precision
      value: 57.63858577040594
    - type: cos_sim_recall
      value: 69.68337730870712
    - type: dot_accuracy
      value: 83.65619598259522
    - type: dot_ap
      value: 66.17413621964548
    - type: dot_f1
      value: 63.09125656951745
    - type: dot_precision
      value: 57.63858577040594
    - type: dot_recall
      value: 69.68337730870712
    - type: euclidean_accuracy
      value: 83.65619598259522
    - type: euclidean_ap
      value: 66.17412836413126
    - type: euclidean_f1
      value: 63.09125656951745
    - type: euclidean_precision
      value: 57.63858577040594
    - type: euclidean_recall
      value: 69.68337730870712
    - type: manhattan_accuracy
      value: 83.5548667819038
    - type: manhattan_ap
      value: 66.07998834521334
    - type: manhattan_f1
      value: 62.96433419721092
    - type: manhattan_precision
      value: 59.14676559239509
    - type: manhattan_recall
      value: 67.30870712401055
    - type: max_accuracy
      value: 83.65619598259522
    - type: max_ap
      value: 66.17413621964548
    - type: max_f1
      value: 63.09125656951745
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
      value: 88.55706911941631
    - type: cos_sim_ap
      value: 85.20971331546805
    - type: cos_sim_f1
      value: 77.28446050593702
    - type: cos_sim_precision
      value: 74.16135881104033
    - type: cos_sim_recall
      value: 80.6821681552202
    - type: dot_accuracy
      value: 88.55706911941631
    - type: dot_ap
      value: 85.2097154112633
    - type: dot_f1
      value: 77.28446050593702
    - type: dot_precision
      value: 74.16135881104033
    - type: dot_recall
      value: 80.6821681552202
    - type: euclidean_accuracy
      value: 88.55706911941631
    - type: euclidean_ap
      value: 85.20971719214488
    - type: euclidean_f1
      value: 77.28446050593702
    - type: euclidean_precision
      value: 74.16135881104033
    - type: euclidean_recall
      value: 80.6821681552202
    - type: manhattan_accuracy
      value: 88.52020025614158
    - type: manhattan_ap
      value: 85.17569799117058
    - type: manhattan_f1
      value: 77.27157773040933
    - type: manhattan_precision
      value: 72.79286638077734
    - type: manhattan_recall
      value: 82.33754234678165
    - type: max_accuracy
      value: 88.55706911941631
    - type: max_ap
      value: 85.20971719214488
    - type: max_f1
      value: 77.28446050593702
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
      value: 85.63474850264893
---
<h1 align="center">Snowflake's Arctic-embed-m-long</h1>
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

model = SentenceTransformer("Snowflake/snowflake-arctic-embed-m-long", trust_remote_code=True)

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
0.46484852 The Data Cloud!
0.3758855 Mexico City of Course!
Query: Where can I get the best tacos?
0.42407742 Mexico City of Course!
0.36740506 The Data Cloud!
```

### Using Huggingface transformers


You can use the transformers package to use an snowflake-arctic-embed model, as shown below. For optimal retrieval quality, use the CLS token to embed each text portion and use the query prefix below (just on the query).



```python
import torch
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Snowflake/snowflake-arctic-embed-m-long')
model = AutoModel.from_pretrained('Snowflake/snowflake-arctic-embed-m-long', trust_remote_code=True, add_pooling_layer=False, safe_serialization=True)
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


If you use the long context model with more than 2048 tokens, ensure that you initialize the model like below instead. This will use [RPE](https://arxiv.org/abs/2104.09864) to allow up to 8192 tokens.


``` py
model = AutoModel.from_pretrained('Snowflake/snowflake-arctic-embed-m-long', trust_remote_code=True, safe_serialization=True, rotary_scaling_factor=2)
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
const extractor = await pipeline('feature-extraction', 'Snowflake/snowflake-arctic-embed-m-long', {
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
console.log(similarities); // [0.36740492125676116, 0.42407774292046635]
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