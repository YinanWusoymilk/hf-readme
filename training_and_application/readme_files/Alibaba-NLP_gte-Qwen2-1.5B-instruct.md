---
tags:
- mteb
- sentence-transformers
- transformers
- Qwen2
- sentence-similarity
license: apache-2.0
model-index:
- name: gte-qwen2-7B-instruct
  results:
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 83.98507462686567
    - type: ap
      value: 50.93015252587014
    - type: f1
      value: 78.50416599051215
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AmazonPolarityClassification
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
      split: test
      type: mteb/amazon_polarity
    metrics:
    - type: accuracy
      value: 96.61065
    - type: ap
      value: 94.89174052954196
    - type: f1
      value: 96.60942596940565
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonReviewsClassification (en)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 55.614000000000004
    - type: f1
      value: 54.90553480294904
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ArguAna
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
      split: test
      type: mteb/arguana
    metrics:
    - type: map_at_1
      value: 45.164
    - type: map_at_10
      value: 61.519
    - type: map_at_100
      value: 61.769
    - type: map_at_1000
      value: 61.769
    - type: map_at_3
      value: 57.443999999999996
    - type: map_at_5
      value: 60.058
    - type: mrr_at_1
      value: 46.088
    - type: mrr_at_10
      value: 61.861
    - type: mrr_at_100
      value: 62.117999999999995
    - type: mrr_at_1000
      value: 62.117999999999995
    - type: mrr_at_3
      value: 57.729
    - type: mrr_at_5
      value: 60.392
    - type: ndcg_at_1
      value: 45.164
    - type: ndcg_at_10
      value: 69.72
    - type: ndcg_at_100
      value: 70.719
    - type: ndcg_at_1000
      value: 70.719
    - type: ndcg_at_3
      value: 61.517999999999994
    - type: ndcg_at_5
      value: 66.247
    - type: precision_at_1
      value: 45.164
    - type: precision_at_10
      value: 9.545
    - type: precision_at_100
      value: 0.996
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 24.443
    - type: precision_at_5
      value: 16.97
    - type: recall_at_1
      value: 45.164
    - type: recall_at_10
      value: 95.448
    - type: recall_at_100
      value: 99.644
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 73.329
    - type: recall_at_5
      value: 84.851
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 50.511868162026175
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringS2S
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
      split: test
      type: mteb/arxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 45.007803189284004
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AskUbuntuDupQuestions
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
      split: test
      type: mteb/askubuntudupquestions-reranking
    metrics:
    - type: map
      value: 64.55292107723382
    - type: mrr
      value: 77.66158818097877
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB BIOSSES
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: cos_sim_pearson
      value: 85.65459047085452
    - type: cos_sim_spearman
      value: 82.10729255710761
    - type: euclidean_pearson
      value: 82.78079159312476
    - type: euclidean_spearman
      value: 80.50002701880933
    - type: manhattan_pearson
      value: 82.41372641383016
    - type: manhattan_spearman
      value: 80.57412509272639
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB Banking77Classification
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
      split: test
      type: mteb/banking77
    metrics:
    - type: accuracy
      value: 87.30844155844156
    - type: f1
      value: 87.25307322443255
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 43.20754608934859
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringS2S
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
      split: test
      type: mteb/biorxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 38.818037697335505
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CQADupstackAndroidRetrieval
      revision: f46a197baaae43b4f621051089b82a364682dfeb
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 35.423
    - type: map_at_10
      value: 47.198
    - type: map_at_100
      value: 48.899
    - type: map_at_1000
      value: 49.004
    - type: map_at_3
      value: 43.114999999999995
    - type: map_at_5
      value: 45.491
    - type: mrr_at_1
      value: 42.918
    - type: mrr_at_10
      value: 53.299
    - type: mrr_at_100
      value: 54.032000000000004
    - type: mrr_at_1000
      value: 54.055
    - type: mrr_at_3
      value: 50.453
    - type: mrr_at_5
      value: 52.205999999999996
    - type: ndcg_at_1
      value: 42.918
    - type: ndcg_at_10
      value: 53.98
    - type: ndcg_at_100
      value: 59.57
    - type: ndcg_at_1000
      value: 60.879000000000005
    - type: ndcg_at_3
      value: 48.224000000000004
    - type: ndcg_at_5
      value: 50.998
    - type: precision_at_1
      value: 42.918
    - type: precision_at_10
      value: 10.299999999999999
    - type: precision_at_100
      value: 1.687
    - type: precision_at_1000
      value: 0.211
    - type: precision_at_3
      value: 22.842000000000002
    - type: precision_at_5
      value: 16.681
    - type: recall_at_1
      value: 35.423
    - type: recall_at_10
      value: 66.824
    - type: recall_at_100
      value: 89.564
    - type: recall_at_1000
      value: 97.501
    - type: recall_at_3
      value: 50.365
    - type: recall_at_5
      value: 57.921
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackEnglishRetrieval
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 33.205
    - type: map_at_10
      value: 44.859
    - type: map_at_100
      value: 46.135
    - type: map_at_1000
      value: 46.259
    - type: map_at_3
      value: 41.839
    - type: map_at_5
      value: 43.662
    - type: mrr_at_1
      value: 41.146
    - type: mrr_at_10
      value: 50.621
    - type: mrr_at_100
      value: 51.207
    - type: mrr_at_1000
      value: 51.246
    - type: mrr_at_3
      value: 48.535000000000004
    - type: mrr_at_5
      value: 49.818
    - type: ndcg_at_1
      value: 41.146
    - type: ndcg_at_10
      value: 50.683
    - type: ndcg_at_100
      value: 54.82
    - type: ndcg_at_1000
      value: 56.69
    - type: ndcg_at_3
      value: 46.611000000000004
    - type: ndcg_at_5
      value: 48.66
    - type: precision_at_1
      value: 41.146
    - type: precision_at_10
      value: 9.439
    - type: precision_at_100
      value: 1.465
    - type: precision_at_1000
      value: 0.194
    - type: precision_at_3
      value: 22.59
    - type: precision_at_5
      value: 15.86
    - type: recall_at_1
      value: 33.205
    - type: recall_at_10
      value: 61.028999999999996
    - type: recall_at_100
      value: 78.152
    - type: recall_at_1000
      value: 89.59700000000001
    - type: recall_at_3
      value: 49.05
    - type: recall_at_5
      value: 54.836
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGamingRetrieval
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 41.637
    - type: map_at_10
      value: 55.162
    - type: map_at_100
      value: 56.142
    - type: map_at_1000
      value: 56.188
    - type: map_at_3
      value: 51.564
    - type: map_at_5
      value: 53.696
    - type: mrr_at_1
      value: 47.524
    - type: mrr_at_10
      value: 58.243
    - type: mrr_at_100
      value: 58.879999999999995
    - type: mrr_at_1000
      value: 58.9
    - type: mrr_at_3
      value: 55.69499999999999
    - type: mrr_at_5
      value: 57.284
    - type: ndcg_at_1
      value: 47.524
    - type: ndcg_at_10
      value: 61.305
    - type: ndcg_at_100
      value: 65.077
    - type: ndcg_at_1000
      value: 65.941
    - type: ndcg_at_3
      value: 55.422000000000004
    - type: ndcg_at_5
      value: 58.516
    - type: precision_at_1
      value: 47.524
    - type: precision_at_10
      value: 9.918000000000001
    - type: precision_at_100
      value: 1.276
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: precision_at_3
      value: 24.765
    - type: precision_at_5
      value: 17.204
    - type: recall_at_1
      value: 41.637
    - type: recall_at_10
      value: 76.185
    - type: recall_at_100
      value: 92.149
    - type: recall_at_1000
      value: 98.199
    - type: recall_at_3
      value: 60.856
    - type: recall_at_5
      value: 68.25099999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGisRetrieval
      revision: 5003b3064772da1887988e05400cf3806fe491f2
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 26.27
    - type: map_at_10
      value: 37.463
    - type: map_at_100
      value: 38.434000000000005
    - type: map_at_1000
      value: 38.509
    - type: map_at_3
      value: 34.226
    - type: map_at_5
      value: 36.161
    - type: mrr_at_1
      value: 28.588
    - type: mrr_at_10
      value: 39.383
    - type: mrr_at_100
      value: 40.23
    - type: mrr_at_1000
      value: 40.281
    - type: mrr_at_3
      value: 36.422
    - type: mrr_at_5
      value: 38.252
    - type: ndcg_at_1
      value: 28.588
    - type: ndcg_at_10
      value: 43.511
    - type: ndcg_at_100
      value: 48.274
    - type: ndcg_at_1000
      value: 49.975
    - type: ndcg_at_3
      value: 37.319
    - type: ndcg_at_5
      value: 40.568
    - type: precision_at_1
      value: 28.588
    - type: precision_at_10
      value: 6.893000000000001
    - type: precision_at_100
      value: 0.9900000000000001
    - type: precision_at_1000
      value: 0.117
    - type: precision_at_3
      value: 16.347
    - type: precision_at_5
      value: 11.661000000000001
    - type: recall_at_1
      value: 26.27
    - type: recall_at_10
      value: 60.284000000000006
    - type: recall_at_100
      value: 81.902
    - type: recall_at_1000
      value: 94.43
    - type: recall_at_3
      value: 43.537
    - type: recall_at_5
      value: 51.475
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackMathematicaRetrieval
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 18.168
    - type: map_at_10
      value: 28.410000000000004
    - type: map_at_100
      value: 29.78
    - type: map_at_1000
      value: 29.892999999999997
    - type: map_at_3
      value: 25.238
    - type: map_at_5
      value: 26.96
    - type: mrr_at_1
      value: 23.507
    - type: mrr_at_10
      value: 33.382
    - type: mrr_at_100
      value: 34.404
    - type: mrr_at_1000
      value: 34.467999999999996
    - type: mrr_at_3
      value: 30.637999999999998
    - type: mrr_at_5
      value: 32.199
    - type: ndcg_at_1
      value: 23.507
    - type: ndcg_at_10
      value: 34.571000000000005
    - type: ndcg_at_100
      value: 40.663
    - type: ndcg_at_1000
      value: 43.236000000000004
    - type: ndcg_at_3
      value: 29.053
    - type: ndcg_at_5
      value: 31.563999999999997
    - type: precision_at_1
      value: 23.507
    - type: precision_at_10
      value: 6.654
    - type: precision_at_100
      value: 1.113
    - type: precision_at_1000
      value: 0.146
    - type: precision_at_3
      value: 14.427999999999999
    - type: precision_at_5
      value: 10.498000000000001
    - type: recall_at_1
      value: 18.168
    - type: recall_at_10
      value: 48.443000000000005
    - type: recall_at_100
      value: 74.47
    - type: recall_at_1000
      value: 92.494
    - type: recall_at_3
      value: 33.379999999999995
    - type: recall_at_5
      value: 39.76
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackPhysicsRetrieval
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 32.39
    - type: map_at_10
      value: 44.479
    - type: map_at_100
      value: 45.977000000000004
    - type: map_at_1000
      value: 46.087
    - type: map_at_3
      value: 40.976
    - type: map_at_5
      value: 43.038
    - type: mrr_at_1
      value: 40.135
    - type: mrr_at_10
      value: 50.160000000000004
    - type: mrr_at_100
      value: 51.052
    - type: mrr_at_1000
      value: 51.087
    - type: mrr_at_3
      value: 47.818
    - type: mrr_at_5
      value: 49.171
    - type: ndcg_at_1
      value: 40.135
    - type: ndcg_at_10
      value: 50.731
    - type: ndcg_at_100
      value: 56.452000000000005
    - type: ndcg_at_1000
      value: 58.123000000000005
    - type: ndcg_at_3
      value: 45.507
    - type: ndcg_at_5
      value: 48.11
    - type: precision_at_1
      value: 40.135
    - type: precision_at_10
      value: 9.192
    - type: precision_at_100
      value: 1.397
    - type: precision_at_1000
      value: 0.169
    - type: precision_at_3
      value: 21.816
    - type: precision_at_5
      value: 15.476
    - type: recall_at_1
      value: 32.39
    - type: recall_at_10
      value: 63.597
    - type: recall_at_100
      value: 86.737
    - type: recall_at_1000
      value: 97.039
    - type: recall_at_3
      value: 48.906
    - type: recall_at_5
      value: 55.659000000000006
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackProgrammersRetrieval
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 28.397
    - type: map_at_10
      value: 39.871
    - type: map_at_100
      value: 41.309000000000005
    - type: map_at_1000
      value: 41.409
    - type: map_at_3
      value: 36.047000000000004
    - type: map_at_5
      value: 38.104
    - type: mrr_at_1
      value: 34.703
    - type: mrr_at_10
      value: 44.773
    - type: mrr_at_100
      value: 45.64
    - type: mrr_at_1000
      value: 45.678999999999995
    - type: mrr_at_3
      value: 41.705
    - type: mrr_at_5
      value: 43.406
    - type: ndcg_at_1
      value: 34.703
    - type: ndcg_at_10
      value: 46.271
    - type: ndcg_at_100
      value: 52.037
    - type: ndcg_at_1000
      value: 53.81700000000001
    - type: ndcg_at_3
      value: 39.966
    - type: ndcg_at_5
      value: 42.801
    - type: precision_at_1
      value: 34.703
    - type: precision_at_10
      value: 8.744
    - type: precision_at_100
      value: 1.348
    - type: precision_at_1000
      value: 0.167
    - type: precision_at_3
      value: 19.102
    - type: precision_at_5
      value: 13.836
    - type: recall_at_1
      value: 28.397
    - type: recall_at_10
      value: 60.299
    - type: recall_at_100
      value: 84.595
    - type: recall_at_1000
      value: 96.155
    - type: recall_at_3
      value: 43.065
    - type: recall_at_5
      value: 50.371
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 28.044333333333338
    - type: map_at_10
      value: 38.78691666666666
    - type: map_at_100
      value: 40.113
    - type: map_at_1000
      value: 40.22125
    - type: map_at_3
      value: 35.52966666666667
    - type: map_at_5
      value: 37.372749999999996
    - type: mrr_at_1
      value: 33.159083333333335
    - type: mrr_at_10
      value: 42.913583333333335
    - type: mrr_at_100
      value: 43.7845
    - type: mrr_at_1000
      value: 43.830333333333336
    - type: mrr_at_3
      value: 40.29816666666667
    - type: mrr_at_5
      value: 41.81366666666667
    - type: ndcg_at_1
      value: 33.159083333333335
    - type: ndcg_at_10
      value: 44.75750000000001
    - type: ndcg_at_100
      value: 50.13658333333334
    - type: ndcg_at_1000
      value: 52.037
    - type: ndcg_at_3
      value: 39.34258333333334
    - type: ndcg_at_5
      value: 41.93708333333333
    - type: precision_at_1
      value: 33.159083333333335
    - type: precision_at_10
      value: 7.952416666666667
    - type: precision_at_100
      value: 1.2571666666666668
    - type: precision_at_1000
      value: 0.16099999999999998
    - type: precision_at_3
      value: 18.303833333333337
    - type: precision_at_5
      value: 13.057083333333333
    - type: recall_at_1
      value: 28.044333333333338
    - type: recall_at_10
      value: 58.237249999999996
    - type: recall_at_100
      value: 81.35391666666666
    - type: recall_at_1000
      value: 94.21283333333334
    - type: recall_at_3
      value: 43.32341666666667
    - type: recall_at_5
      value: 49.94908333333333
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackStatsRetrieval
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 27.838
    - type: map_at_10
      value: 36.04
    - type: map_at_100
      value: 37.113
    - type: map_at_1000
      value: 37.204
    - type: map_at_3
      value: 33.585
    - type: map_at_5
      value: 34.845
    - type: mrr_at_1
      value: 30.982
    - type: mrr_at_10
      value: 39.105000000000004
    - type: mrr_at_100
      value: 39.98
    - type: mrr_at_1000
      value: 40.042
    - type: mrr_at_3
      value: 36.912
    - type: mrr_at_5
      value: 38.062000000000005
    - type: ndcg_at_1
      value: 30.982
    - type: ndcg_at_10
      value: 40.982
    - type: ndcg_at_100
      value: 46.092
    - type: ndcg_at_1000
      value: 48.25
    - type: ndcg_at_3
      value: 36.41
    - type: ndcg_at_5
      value: 38.379999999999995
    - type: precision_at_1
      value: 30.982
    - type: precision_at_10
      value: 6.534
    - type: precision_at_100
      value: 0.9820000000000001
    - type: precision_at_1000
      value: 0.124
    - type: precision_at_3
      value: 15.745999999999999
    - type: precision_at_5
      value: 10.828
    - type: recall_at_1
      value: 27.838
    - type: recall_at_10
      value: 52.971000000000004
    - type: recall_at_100
      value: 76.357
    - type: recall_at_1000
      value: 91.973
    - type: recall_at_3
      value: 40.157
    - type: recall_at_5
      value: 45.147999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackTexRetrieval
      revision: 46989137a86843e03a6195de44b09deda022eec7
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 19.059
    - type: map_at_10
      value: 27.454
    - type: map_at_100
      value: 28.736
    - type: map_at_1000
      value: 28.865000000000002
    - type: map_at_3
      value: 24.773999999999997
    - type: map_at_5
      value: 26.266000000000002
    - type: mrr_at_1
      value: 23.125
    - type: mrr_at_10
      value: 31.267
    - type: mrr_at_100
      value: 32.32
    - type: mrr_at_1000
      value: 32.394
    - type: mrr_at_3
      value: 28.894
    - type: mrr_at_5
      value: 30.281000000000002
    - type: ndcg_at_1
      value: 23.125
    - type: ndcg_at_10
      value: 32.588
    - type: ndcg_at_100
      value: 38.432
    - type: ndcg_at_1000
      value: 41.214
    - type: ndcg_at_3
      value: 27.938000000000002
    - type: ndcg_at_5
      value: 30.127
    - type: precision_at_1
      value: 23.125
    - type: precision_at_10
      value: 5.9639999999999995
    - type: precision_at_100
      value: 1.047
    - type: precision_at_1000
      value: 0.148
    - type: precision_at_3
      value: 13.294
    - type: precision_at_5
      value: 9.628
    - type: recall_at_1
      value: 19.059
    - type: recall_at_10
      value: 44.25
    - type: recall_at_100
      value: 69.948
    - type: recall_at_1000
      value: 89.35300000000001
    - type: recall_at_3
      value: 31.114000000000004
    - type: recall_at_5
      value: 36.846000000000004
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackUnixRetrieval
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 28.355999999999998
    - type: map_at_10
      value: 39.055
    - type: map_at_100
      value: 40.486
    - type: map_at_1000
      value: 40.571
    - type: map_at_3
      value: 35.69
    - type: map_at_5
      value: 37.605
    - type: mrr_at_1
      value: 33.302
    - type: mrr_at_10
      value: 42.986000000000004
    - type: mrr_at_100
      value: 43.957
    - type: mrr_at_1000
      value: 43.996
    - type: mrr_at_3
      value: 40.111999999999995
    - type: mrr_at_5
      value: 41.735
    - type: ndcg_at_1
      value: 33.302
    - type: ndcg_at_10
      value: 44.962999999999994
    - type: ndcg_at_100
      value: 50.917
    - type: ndcg_at_1000
      value: 52.622
    - type: ndcg_at_3
      value: 39.182
    - type: ndcg_at_5
      value: 41.939
    - type: precision_at_1
      value: 33.302
    - type: precision_at_10
      value: 7.779999999999999
    - type: precision_at_100
      value: 1.203
    - type: precision_at_1000
      value: 0.145
    - type: precision_at_3
      value: 18.035
    - type: precision_at_5
      value: 12.873000000000001
    - type: recall_at_1
      value: 28.355999999999998
    - type: recall_at_10
      value: 58.782000000000004
    - type: recall_at_100
      value: 84.02199999999999
    - type: recall_at_1000
      value: 95.511
    - type: recall_at_3
      value: 43.126999999999995
    - type: recall_at_5
      value: 50.14999999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWebmastersRetrieval
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 27.391
    - type: map_at_10
      value: 37.523
    - type: map_at_100
      value: 39.312000000000005
    - type: map_at_1000
      value: 39.54
    - type: map_at_3
      value: 34.231
    - type: map_at_5
      value: 36.062
    - type: mrr_at_1
      value: 32.016
    - type: mrr_at_10
      value: 41.747
    - type: mrr_at_100
      value: 42.812
    - type: mrr_at_1000
      value: 42.844
    - type: mrr_at_3
      value: 39.129999999999995
    - type: mrr_at_5
      value: 40.524
    - type: ndcg_at_1
      value: 32.016
    - type: ndcg_at_10
      value: 43.826
    - type: ndcg_at_100
      value: 50.373999999999995
    - type: ndcg_at_1000
      value: 52.318
    - type: ndcg_at_3
      value: 38.479
    - type: ndcg_at_5
      value: 40.944
    - type: precision_at_1
      value: 32.016
    - type: precision_at_10
      value: 8.280999999999999
    - type: precision_at_100
      value: 1.6760000000000002
    - type: precision_at_1000
      value: 0.25
    - type: precision_at_3
      value: 18.05
    - type: precision_at_5
      value: 13.083
    - type: recall_at_1
      value: 27.391
    - type: recall_at_10
      value: 56.928999999999995
    - type: recall_at_100
      value: 85.169
    - type: recall_at_1000
      value: 96.665
    - type: recall_at_3
      value: 42.264
    - type: recall_at_5
      value: 48.556
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWordpressRetrieval
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
      split: test
      type: BeIR/cqadupstack
    metrics:
    - type: map_at_1
      value: 18.398
    - type: map_at_10
      value: 27.929
    - type: map_at_100
      value: 29.032999999999998
    - type: map_at_1000
      value: 29.126
    - type: map_at_3
      value: 25.070999999999998
    - type: map_at_5
      value: 26.583000000000002
    - type: mrr_at_1
      value: 19.963
    - type: mrr_at_10
      value: 29.997
    - type: mrr_at_100
      value: 30.9
    - type: mrr_at_1000
      value: 30.972
    - type: mrr_at_3
      value: 27.264
    - type: mrr_at_5
      value: 28.826
    - type: ndcg_at_1
      value: 19.963
    - type: ndcg_at_10
      value: 33.678999999999995
    - type: ndcg_at_100
      value: 38.931
    - type: ndcg_at_1000
      value: 41.379
    - type: ndcg_at_3
      value: 28.000000000000004
    - type: ndcg_at_5
      value: 30.637999999999998
    - type: precision_at_1
      value: 19.963
    - type: precision_at_10
      value: 5.7299999999999995
    - type: precision_at_100
      value: 0.902
    - type: precision_at_1000
      value: 0.122
    - type: precision_at_3
      value: 12.631
    - type: precision_at_5
      value: 9.057
    - type: recall_at_1
      value: 18.398
    - type: recall_at_10
      value: 49.254
    - type: recall_at_100
      value: 73.182
    - type: recall_at_1000
      value: 91.637
    - type: recall_at_3
      value: 34.06
    - type: recall_at_5
      value: 40.416000000000004
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ClimateFEVER
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
      split: test
      type: mteb/climate-fever
    metrics:
    - type: map_at_1
      value: 19.681
    - type: map_at_10
      value: 32.741
    - type: map_at_100
      value: 34.811
    - type: map_at_1000
      value: 35.003
    - type: map_at_3
      value: 27.697
    - type: map_at_5
      value: 30.372
    - type: mrr_at_1
      value: 44.951
    - type: mrr_at_10
      value: 56.34400000000001
    - type: mrr_at_100
      value: 56.961
    - type: mrr_at_1000
      value: 56.987
    - type: mrr_at_3
      value: 53.681
    - type: mrr_at_5
      value: 55.407
    - type: ndcg_at_1
      value: 44.951
    - type: ndcg_at_10
      value: 42.905
    - type: ndcg_at_100
      value: 49.95
    - type: ndcg_at_1000
      value: 52.917
    - type: ndcg_at_3
      value: 36.815
    - type: ndcg_at_5
      value: 38.817
    - type: precision_at_1
      value: 44.951
    - type: precision_at_10
      value: 12.989999999999998
    - type: precision_at_100
      value: 2.068
    - type: precision_at_1000
      value: 0.263
    - type: precision_at_3
      value: 27.275
    - type: precision_at_5
      value: 20.365
    - type: recall_at_1
      value: 19.681
    - type: recall_at_10
      value: 48.272999999999996
    - type: recall_at_100
      value: 71.87400000000001
    - type: recall_at_1000
      value: 87.929
    - type: recall_at_3
      value: 32.653999999999996
    - type: recall_at_5
      value: 39.364
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: test
      type: mteb/dbpedia
    metrics:
    - type: map_at_1
      value: 10.231
    - type: map_at_10
      value: 22.338
    - type: map_at_100
      value: 31.927
    - type: map_at_1000
      value: 33.87
    - type: map_at_3
      value: 15.559999999999999
    - type: map_at_5
      value: 18.239
    - type: mrr_at_1
      value: 75.0
    - type: mrr_at_10
      value: 81.303
    - type: mrr_at_100
      value: 81.523
    - type: mrr_at_1000
      value: 81.53
    - type: mrr_at_3
      value: 80.083
    - type: mrr_at_5
      value: 80.758
    - type: ndcg_at_1
      value: 64.625
    - type: ndcg_at_10
      value: 48.687000000000005
    - type: ndcg_at_100
      value: 52.791
    - type: ndcg_at_1000
      value: 60.041999999999994
    - type: ndcg_at_3
      value: 53.757999999999996
    - type: ndcg_at_5
      value: 50.76500000000001
    - type: precision_at_1
      value: 75.0
    - type: precision_at_10
      value: 38.3
    - type: precision_at_100
      value: 12.025
    - type: precision_at_1000
      value: 2.3970000000000002
    - type: precision_at_3
      value: 55.417
    - type: precision_at_5
      value: 47.5
    - type: recall_at_1
      value: 10.231
    - type: recall_at_10
      value: 27.697
    - type: recall_at_100
      value: 57.409
    - type: recall_at_1000
      value: 80.547
    - type: recall_at_3
      value: 16.668
    - type: recall_at_5
      value: 20.552
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB EmotionClassification
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: test
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 61.365
    - type: f1
      value: 56.7540827912991
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FEVER
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
      split: test
      type: mteb/fever
    metrics:
    - type: map_at_1
      value: 83.479
    - type: map_at_10
      value: 88.898
    - type: map_at_100
      value: 89.11
    - type: map_at_1000
      value: 89.12400000000001
    - type: map_at_3
      value: 88.103
    - type: map_at_5
      value: 88.629
    - type: mrr_at_1
      value: 89.934
    - type: mrr_at_10
      value: 93.91000000000001
    - type: mrr_at_100
      value: 93.937
    - type: mrr_at_1000
      value: 93.938
    - type: mrr_at_3
      value: 93.62700000000001
    - type: mrr_at_5
      value: 93.84599999999999
    - type: ndcg_at_1
      value: 89.934
    - type: ndcg_at_10
      value: 91.574
    - type: ndcg_at_100
      value: 92.238
    - type: ndcg_at_1000
      value: 92.45
    - type: ndcg_at_3
      value: 90.586
    - type: ndcg_at_5
      value: 91.16300000000001
    - type: precision_at_1
      value: 89.934
    - type: precision_at_10
      value: 10.555
    - type: precision_at_100
      value: 1.1159999999999999
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 33.588
    - type: precision_at_5
      value: 20.642
    - type: recall_at_1
      value: 83.479
    - type: recall_at_10
      value: 94.971
    - type: recall_at_100
      value: 97.397
    - type: recall_at_1000
      value: 98.666
    - type: recall_at_3
      value: 92.24799999999999
    - type: recall_at_5
      value: 93.797
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA2018
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: test
      type: mteb/fiqa
    metrics:
    - type: map_at_1
      value: 27.16
    - type: map_at_10
      value: 45.593
    - type: map_at_100
      value: 47.762
    - type: map_at_1000
      value: 47.899
    - type: map_at_3
      value: 39.237
    - type: map_at_5
      value: 42.970000000000006
    - type: mrr_at_1
      value: 52.623
    - type: mrr_at_10
      value: 62.637
    - type: mrr_at_100
      value: 63.169
    - type: mrr_at_1000
      value: 63.185
    - type: mrr_at_3
      value: 59.928000000000004
    - type: mrr_at_5
      value: 61.702999999999996
    - type: ndcg_at_1
      value: 52.623
    - type: ndcg_at_10
      value: 54.701
    - type: ndcg_at_100
      value: 61.263
    - type: ndcg_at_1000
      value: 63.134
    - type: ndcg_at_3
      value: 49.265
    - type: ndcg_at_5
      value: 51.665000000000006
    - type: precision_at_1
      value: 52.623
    - type: precision_at_10
      value: 15.185
    - type: precision_at_100
      value: 2.202
    - type: precision_at_1000
      value: 0.254
    - type: precision_at_3
      value: 32.767
    - type: precision_at_5
      value: 24.722
    - type: recall_at_1
      value: 27.16
    - type: recall_at_10
      value: 63.309000000000005
    - type: recall_at_100
      value: 86.722
    - type: recall_at_1000
      value: 97.505
    - type: recall_at_3
      value: 45.045
    - type: recall_at_5
      value: 54.02400000000001
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
      split: test
      type: mteb/hotpotqa
    metrics:
    - type: map_at_1
      value: 42.573
    - type: map_at_10
      value: 59.373
    - type: map_at_100
      value: 60.292
    - type: map_at_1000
      value: 60.358999999999995
    - type: map_at_3
      value: 56.159000000000006
    - type: map_at_5
      value: 58.123999999999995
    - type: mrr_at_1
      value: 85.14500000000001
    - type: mrr_at_10
      value: 89.25999999999999
    - type: mrr_at_100
      value: 89.373
    - type: mrr_at_1000
      value: 89.377
    - type: mrr_at_3
      value: 88.618
    - type: mrr_at_5
      value: 89.036
    - type: ndcg_at_1
      value: 85.14500000000001
    - type: ndcg_at_10
      value: 68.95
    - type: ndcg_at_100
      value: 71.95
    - type: ndcg_at_1000
      value: 73.232
    - type: ndcg_at_3
      value: 64.546
    - type: ndcg_at_5
      value: 66.945
    - type: precision_at_1
      value: 85.14500000000001
    - type: precision_at_10
      value: 13.865
    - type: precision_at_100
      value: 1.619
    - type: precision_at_1000
      value: 0.179
    - type: precision_at_3
      value: 39.703
    - type: precision_at_5
      value: 25.718000000000004
    - type: recall_at_1
      value: 42.573
    - type: recall_at_10
      value: 69.325
    - type: recall_at_100
      value: 80.932
    - type: recall_at_1000
      value: 89.446
    - type: recall_at_3
      value: 59.553999999999995
    - type: recall_at_5
      value: 64.294
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ImdbClassification
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
      split: test
      type: mteb/imdb
    metrics:
    - type: accuracy
      value: 95.8336
    - type: ap
      value: 93.78862962194073
    - type: f1
      value: 95.83192650728371
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MSMARCO
      revision: c5a29a104738b98a9e76336939199e264163d4a0
      split: dev
      type: mteb/msmarco
    metrics:
    - type: map_at_1
      value: 23.075000000000003
    - type: map_at_10
      value: 36.102000000000004
    - type: map_at_100
      value: 37.257
    - type: map_at_1000
      value: 37.3
    - type: map_at_3
      value: 32.144
    - type: map_at_5
      value: 34.359
    - type: mrr_at_1
      value: 23.711
    - type: mrr_at_10
      value: 36.671
    - type: mrr_at_100
      value: 37.763999999999996
    - type: mrr_at_1000
      value: 37.801
    - type: mrr_at_3
      value: 32.775
    - type: mrr_at_5
      value: 34.977000000000004
    - type: ndcg_at_1
      value: 23.711
    - type: ndcg_at_10
      value: 43.361
    - type: ndcg_at_100
      value: 48.839
    - type: ndcg_at_1000
      value: 49.88
    - type: ndcg_at_3
      value: 35.269
    - type: ndcg_at_5
      value: 39.224
    - type: precision_at_1
      value: 23.711
    - type: precision_at_10
      value: 6.866999999999999
    - type: precision_at_100
      value: 0.96
    - type: precision_at_1000
      value: 0.105
    - type: precision_at_3
      value: 15.096000000000002
    - type: precision_at_5
      value: 11.083
    - type: recall_at_1
      value: 23.075000000000003
    - type: recall_at_10
      value: 65.756
    - type: recall_at_100
      value: 90.88199999999999
    - type: recall_at_1000
      value: 98.739
    - type: recall_at_3
      value: 43.691
    - type: recall_at_5
      value: 53.15800000000001
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB MTOPDomainClassification (en)
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: test
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 97.69493844049248
    - type: f1
      value: 97.55048089616261
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPIntentClassification (en)
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: test
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 88.75968992248062
    - type: f1
      value: 72.26321223399123
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveIntentClassification (en)
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 82.40080699394754
    - type: f1
      value: 79.62590029057968
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveScenarioClassification (en)
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 84.49562878278414
    - type: f1
      value: 84.0040193313333
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MedrxivClusteringP2P
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
      split: test
      type: mteb/medrxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 39.386760057101945
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MedrxivClusteringS2S
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
      split: test
      type: mteb/medrxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 37.89687154075537
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MindSmallReranking
      revision: 3bdac13927fdc888b903db93b2ffdbd90b295a69
      split: test
      type: mteb/mind_small
    metrics:
    - type: map
      value: 33.94151656057482
    - type: mrr
      value: 35.32684700746953
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB NFCorpus
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
      split: test
      type: mteb/nfcorpus
    metrics:
    - type: map_at_1
      value: 6.239999999999999
    - type: map_at_10
      value: 14.862
    - type: map_at_100
      value: 18.955
    - type: map_at_1000
      value: 20.694000000000003
    - type: map_at_3
      value: 10.683
    - type: map_at_5
      value: 12.674
    - type: mrr_at_1
      value: 50.15500000000001
    - type: mrr_at_10
      value: 59.697
    - type: mrr_at_100
      value: 60.095
    - type: mrr_at_1000
      value: 60.129999999999995
    - type: mrr_at_3
      value: 58.35900000000001
    - type: mrr_at_5
      value: 58.839
    - type: ndcg_at_1
      value: 48.452
    - type: ndcg_at_10
      value: 39.341
    - type: ndcg_at_100
      value: 35.866
    - type: ndcg_at_1000
      value: 45.111000000000004
    - type: ndcg_at_3
      value: 44.527
    - type: ndcg_at_5
      value: 42.946
    - type: precision_at_1
      value: 50.15500000000001
    - type: precision_at_10
      value: 29.536
    - type: precision_at_100
      value: 9.142
    - type: precision_at_1000
      value: 2.2849999999999997
    - type: precision_at_3
      value: 41.899
    - type: precision_at_5
      value: 37.647000000000006
    - type: recall_at_1
      value: 6.239999999999999
    - type: recall_at_10
      value: 19.278000000000002
    - type: recall_at_100
      value: 36.074
    - type: recall_at_1000
      value: 70.017
    - type: recall_at_3
      value: 12.066
    - type: recall_at_5
      value: 15.254000000000001
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NQ
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
      split: test
      type: mteb/nq
    metrics:
    - type: map_at_1
      value: 39.75
    - type: map_at_10
      value: 56.443
    - type: map_at_100
      value: 57.233999999999995
    - type: map_at_1000
      value: 57.249
    - type: map_at_3
      value: 52.032999999999994
    - type: map_at_5
      value: 54.937999999999995
    - type: mrr_at_1
      value: 44.728
    - type: mrr_at_10
      value: 58.939
    - type: mrr_at_100
      value: 59.489000000000004
    - type: mrr_at_1000
      value: 59.499
    - type: mrr_at_3
      value: 55.711999999999996
    - type: mrr_at_5
      value: 57.89
    - type: ndcg_at_1
      value: 44.728
    - type: ndcg_at_10
      value: 63.998999999999995
    - type: ndcg_at_100
      value: 67.077
    - type: ndcg_at_1000
      value: 67.40899999999999
    - type: ndcg_at_3
      value: 56.266000000000005
    - type: ndcg_at_5
      value: 60.88
    - type: precision_at_1
      value: 44.728
    - type: precision_at_10
      value: 10.09
    - type: precision_at_100
      value: 1.1809999999999998
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 25.145
    - type: precision_at_5
      value: 17.822
    - type: recall_at_1
      value: 39.75
    - type: recall_at_10
      value: 84.234
    - type: recall_at_100
      value: 97.055
    - type: recall_at_1000
      value: 99.517
    - type: recall_at_3
      value: 64.851
    - type: recall_at_5
      value: 75.343
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB QuoraRetrieval
      revision: None
      split: test
      type: mteb/quora
    metrics:
    - type: map_at_1
      value: 72.085
    - type: map_at_10
      value: 86.107
    - type: map_at_100
      value: 86.727
    - type: map_at_1000
      value: 86.74
    - type: map_at_3
      value: 83.21
    - type: map_at_5
      value: 85.06
    - type: mrr_at_1
      value: 82.94
    - type: mrr_at_10
      value: 88.845
    - type: mrr_at_100
      value: 88.926
    - type: mrr_at_1000
      value: 88.927
    - type: mrr_at_3
      value: 87.993
    - type: mrr_at_5
      value: 88.62299999999999
    - type: ndcg_at_1
      value: 82.97
    - type: ndcg_at_10
      value: 89.645
    - type: ndcg_at_100
      value: 90.717
    - type: ndcg_at_1000
      value: 90.78
    - type: ndcg_at_3
      value: 86.99900000000001
    - type: ndcg_at_5
      value: 88.52600000000001
    - type: precision_at_1
      value: 82.97
    - type: precision_at_10
      value: 13.569
    - type: precision_at_100
      value: 1.539
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 38.043
    - type: precision_at_5
      value: 24.992
    - type: recall_at_1
      value: 72.085
    - type: recall_at_10
      value: 96.262
    - type: recall_at_100
      value: 99.77000000000001
    - type: recall_at_1000
      value: 99.997
    - type: recall_at_3
      value: 88.652
    - type: recall_at_5
      value: 93.01899999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB RedditClustering
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
      split: test
      type: mteb/reddit-clustering
    metrics:
    - type: v_measure
      value: 55.82153952668092
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RedditClusteringP2P
      revision: 282350215ef01743dc01b456c7f5241fa8937f16
      split: test
      type: mteb/reddit-clustering-p2p
    metrics:
    - type: v_measure
      value: 62.094465801879295
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB SCIDOCS
      revision: None
      split: test
      type: mteb/scidocs
    metrics:
    - type: map_at_1
      value: 5.688
    - type: map_at_10
      value: 15.201999999999998
    - type: map_at_100
      value: 18.096
    - type: map_at_1000
      value: 18.481
    - type: map_at_3
      value: 10.734
    - type: map_at_5
      value: 12.94
    - type: mrr_at_1
      value: 28.000000000000004
    - type: mrr_at_10
      value: 41.101
    - type: mrr_at_100
      value: 42.202
    - type: mrr_at_1000
      value: 42.228
    - type: mrr_at_3
      value: 37.683
    - type: mrr_at_5
      value: 39.708
    - type: ndcg_at_1
      value: 28.000000000000004
    - type: ndcg_at_10
      value: 24.976000000000003
    - type: ndcg_at_100
      value: 35.129
    - type: ndcg_at_1000
      value: 40.77
    - type: ndcg_at_3
      value: 23.787
    - type: ndcg_at_5
      value: 20.816000000000003
    - type: precision_at_1
      value: 28.000000000000004
    - type: precision_at_10
      value: 13.04
    - type: precision_at_100
      value: 2.761
    - type: precision_at_1000
      value: 0.41000000000000003
    - type: precision_at_3
      value: 22.6
    - type: precision_at_5
      value: 18.52
    - type: recall_at_1
      value: 5.688
    - type: recall_at_10
      value: 26.43
    - type: recall_at_100
      value: 56.02
    - type: recall_at_1000
      value: 83.21
    - type: recall_at_3
      value: 13.752
    - type: recall_at_5
      value: 18.777
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SICK-R
      revision: a6ea5a8cab320b040a23452cc28066d9beae2cee
      split: test
      type: mteb/sickr-sts
    metrics:
    - type: cos_sim_pearson
      value: 85.15084859283178
    - type: cos_sim_spearman
      value: 80.49030614009419
    - type: euclidean_pearson
      value: 81.84574978672468
    - type: euclidean_spearman
      value: 79.89787150656818
    - type: manhattan_pearson
      value: 81.63076538567131
    - type: manhattan_spearman
      value: 79.69867352121841
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS12
      revision: a0d554a64d88156834ff5ae9920b964011b16384
      split: test
      type: mteb/sts12-sts
    metrics:
    - type: cos_sim_pearson
      value: 84.64097921490992
    - type: cos_sim_spearman
      value: 77.25370084896514
    - type: euclidean_pearson
      value: 82.71210826468788
    - type: euclidean_spearman
      value: 78.50445584994826
    - type: manhattan_pearson
      value: 82.92580164330298
    - type: manhattan_spearman
      value: 78.69686891301019
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS13
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
      split: test
      type: mteb/sts13-sts
    metrics:
    - type: cos_sim_pearson
      value: 87.24596417308994
    - type: cos_sim_spearman
      value: 87.79454220555091
    - type: euclidean_pearson
      value: 87.40242561671164
    - type: euclidean_spearman
      value: 88.25955597373556
    - type: manhattan_pearson
      value: 87.25160240485849
    - type: manhattan_spearman
      value: 88.155794979818
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS14
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
      split: test
      type: mteb/sts14-sts
    metrics:
    - type: cos_sim_pearson
      value: 84.44914233422564
    - type: cos_sim_spearman
      value: 82.91015471820322
    - type: euclidean_pearson
      value: 84.7206656630327
    - type: euclidean_spearman
      value: 83.86408872059216
    - type: manhattan_pearson
      value: 84.72816725158454
    - type: manhattan_spearman
      value: 84.01603388572788
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS15
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
      split: test
      type: mteb/sts15-sts
    metrics:
    - type: cos_sim_pearson
      value: 87.6168026237477
    - type: cos_sim_spearman
      value: 88.45414278092397
    - type: euclidean_pearson
      value: 88.57023240882022
    - type: euclidean_spearman
      value: 89.04102190922094
    - type: manhattan_pearson
      value: 88.66695535796354
    - type: manhattan_spearman
      value: 89.19898476680969
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS16
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
      split: test
      type: mteb/sts16-sts
    metrics:
    - type: cos_sim_pearson
      value: 84.27925826089424
    - type: cos_sim_spearman
      value: 85.45291099550461
    - type: euclidean_pearson
      value: 83.63853036580834
    - type: euclidean_spearman
      value: 84.33468035821484
    - type: manhattan_pearson
      value: 83.72778773251596
    - type: manhattan_spearman
      value: 84.51583132445376
    task:
      type: STS
  - dataset:
      config: en-en
      name: MTEB STS17 (en-en)
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cos_sim_pearson
      value: 89.67375185692552
    - type: cos_sim_spearman
      value: 90.32542469203855
    - type: euclidean_pearson
      value: 89.63513717951847
    - type: euclidean_spearman
      value: 89.87760271003745
    - type: manhattan_pearson
      value: 89.28381452982924
    - type: manhattan_spearman
      value: 89.53568197785721
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STS22 (en)
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cos_sim_pearson
      value: 66.24644693819846
    - type: cos_sim_spearman
      value: 66.09889420525377
    - type: euclidean_pearson
      value: 63.72551583520747
    - type: euclidean_spearman
      value: 63.01385470780679
    - type: manhattan_pearson
      value: 64.09258157214097
    - type: manhattan_spearman
      value: 63.080517752822594
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSBenchmark
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
      split: test
      type: mteb/stsbenchmark-sts
    metrics:
    - type: cos_sim_pearson
      value: 86.27321463839989
    - type: cos_sim_spearman
      value: 86.37572865993327
    - type: euclidean_pearson
      value: 86.36268020198149
    - type: euclidean_spearman
      value: 86.31089339478922
    - type: manhattan_pearson
      value: 86.4260445761947
    - type: manhattan_spearman
      value: 86.45885895320457
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SciDocsRR
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
      split: test
      type: mteb/scidocs-reranking
    metrics:
    - type: map
      value: 86.52456702387798
    - type: mrr
      value: 96.34556529164372
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SciFact
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
      split: test
      type: mteb/scifact
    metrics:
    - type: map_at_1
      value: 61.99400000000001
    - type: map_at_10
      value: 73.38799999999999
    - type: map_at_100
      value: 73.747
    - type: map_at_1000
      value: 73.75
    - type: map_at_3
      value: 70.04599999999999
    - type: map_at_5
      value: 72.095
    - type: mrr_at_1
      value: 65.0
    - type: mrr_at_10
      value: 74.42800000000001
    - type: mrr_at_100
      value: 74.722
    - type: mrr_at_1000
      value: 74.725
    - type: mrr_at_3
      value: 72.056
    - type: mrr_at_5
      value: 73.60600000000001
    - type: ndcg_at_1
      value: 65.0
    - type: ndcg_at_10
      value: 78.435
    - type: ndcg_at_100
      value: 79.922
    - type: ndcg_at_1000
      value: 80.00500000000001
    - type: ndcg_at_3
      value: 73.05199999999999
    - type: ndcg_at_5
      value: 75.98
    - type: precision_at_1
      value: 65.0
    - type: precision_at_10
      value: 10.5
    - type: precision_at_100
      value: 1.123
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 28.555999999999997
    - type: precision_at_5
      value: 19.0
    - type: recall_at_1
      value: 61.99400000000001
    - type: recall_at_10
      value: 92.72200000000001
    - type: recall_at_100
      value: 99.333
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 78.739
    - type: recall_at_5
      value: 85.828
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SprintDuplicateQuestions
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
      split: test
      type: mteb/sprintduplicatequestions-pairclassification
    metrics:
    - type: cos_sim_accuracy
      value: 99.79009900990098
    - type: cos_sim_ap
      value: 95.3203137438653
    - type: cos_sim_f1
      value: 89.12386706948641
    - type: cos_sim_precision
      value: 89.75659229208925
    - type: cos_sim_recall
      value: 88.5
    - type: dot_accuracy
      value: 99.67821782178218
    - type: dot_ap
      value: 89.94069840000675
    - type: dot_f1
      value: 83.45902463549521
    - type: dot_precision
      value: 83.9231547017189
    - type: dot_recall
      value: 83.0
    - type: euclidean_accuracy
      value: 99.78613861386138
    - type: euclidean_ap
      value: 95.10648259135526
    - type: euclidean_f1
      value: 88.77338877338877
    - type: euclidean_precision
      value: 92.42424242424242
    - type: euclidean_recall
      value: 85.39999999999999
    - type: manhattan_accuracy
      value: 99.7950495049505
    - type: manhattan_ap
      value: 95.29987661320946
    - type: manhattan_f1
      value: 89.21313183949972
    - type: manhattan_precision
      value: 93.14472252448314
    - type: manhattan_recall
      value: 85.6
    - type: max_accuracy
      value: 99.7950495049505
    - type: max_ap
      value: 95.3203137438653
    - type: max_f1
      value: 89.21313183949972
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB StackExchangeClustering
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
      split: test
      type: mteb/stackexchange-clustering
    metrics:
    - type: v_measure
      value: 67.65446577183913
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackExchangeClusteringP2P
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
      split: test
      type: mteb/stackexchange-clustering-p2p
    metrics:
    - type: v_measure
      value: 46.30749237193961
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackOverflowDupQuestions
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
      split: test
      type: mteb/stackoverflowdupquestions-reranking
    metrics:
    - type: map
      value: 54.91481849959949
    - type: mrr
      value: 55.853506175197346
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SummEval
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
      split: test
      type: mteb/summeval
    metrics:
    - type: cos_sim_pearson
      value: 30.08196549170419
    - type: cos_sim_spearman
      value: 31.16661390597077
    - type: dot_pearson
      value: 29.892258410943466
    - type: dot_spearman
      value: 30.51328811965085
    task:
      type: Summarization
  - dataset:
      config: default
      name: MTEB TRECCOVID
      revision: None
      split: test
      type: mteb/trec-covid
    metrics:
    - type: map_at_1
      value: 0.23900000000000002
    - type: map_at_10
      value: 2.173
    - type: map_at_100
      value: 14.24
    - type: map_at_1000
      value: 35.309000000000005
    - type: map_at_3
      value: 0.7100000000000001
    - type: map_at_5
      value: 1.163
    - type: mrr_at_1
      value: 92.0
    - type: mrr_at_10
      value: 96.0
    - type: mrr_at_100
      value: 96.0
    - type: mrr_at_1000
      value: 96.0
    - type: mrr_at_3
      value: 96.0
    - type: mrr_at_5
      value: 96.0
    - type: ndcg_at_1
      value: 90.0
    - type: ndcg_at_10
      value: 85.382
    - type: ndcg_at_100
      value: 68.03
    - type: ndcg_at_1000
      value: 61.021
    - type: ndcg_at_3
      value: 89.765
    - type: ndcg_at_5
      value: 88.444
    - type: precision_at_1
      value: 92.0
    - type: precision_at_10
      value: 88.0
    - type: precision_at_100
      value: 70.02000000000001
    - type: precision_at_1000
      value: 26.984
    - type: precision_at_3
      value: 94.0
    - type: precision_at_5
      value: 92.80000000000001
    - type: recall_at_1
      value: 0.23900000000000002
    - type: recall_at_10
      value: 2.313
    - type: recall_at_100
      value: 17.049
    - type: recall_at_1000
      value: 57.489999999999995
    - type: recall_at_3
      value: 0.737
    - type: recall_at_5
      value: 1.221
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Touche2020
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
      split: test
      type: mteb/touche2020
    metrics:
    - type: map_at_1
      value: 2.75
    - type: map_at_10
      value: 11.29
    - type: map_at_100
      value: 18.032999999999998
    - type: map_at_1000
      value: 19.746
    - type: map_at_3
      value: 6.555
    - type: map_at_5
      value: 8.706999999999999
    - type: mrr_at_1
      value: 34.694
    - type: mrr_at_10
      value: 50.55
    - type: mrr_at_100
      value: 51.659
    - type: mrr_at_1000
      value: 51.659
    - type: mrr_at_3
      value: 47.278999999999996
    - type: mrr_at_5
      value: 49.728
    - type: ndcg_at_1
      value: 32.653
    - type: ndcg_at_10
      value: 27.894000000000002
    - type: ndcg_at_100
      value: 39.769
    - type: ndcg_at_1000
      value: 51.495999999999995
    - type: ndcg_at_3
      value: 32.954
    - type: ndcg_at_5
      value: 31.502999999999997
    - type: precision_at_1
      value: 34.694
    - type: precision_at_10
      value: 23.265
    - type: precision_at_100
      value: 7.898
    - type: precision_at_1000
      value: 1.58
    - type: precision_at_3
      value: 34.694
    - type: precision_at_5
      value: 31.429000000000002
    - type: recall_at_1
      value: 2.75
    - type: recall_at_10
      value: 16.953
    - type: recall_at_100
      value: 48.68
    - type: recall_at_1000
      value: 85.18599999999999
    - type: recall_at_3
      value: 7.710999999999999
    - type: recall_at_5
      value: 11.484
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ToxicConversationsClassification
      revision: d7c0de2777da35d6aae2200a62c6e0e5af397c4c
      split: test
      type: mteb/toxic_conversations_50k
    metrics:
    - type: accuracy
      value: 82.66099999999999
    - type: ap
      value: 25.555698090238337
    - type: f1
      value: 66.48402012461622
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TweetSentimentExtractionClassification
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
      split: test
      type: mteb/tweet_sentiment_extraction
    metrics:
    - type: accuracy
      value: 72.94567062818335
    - type: f1
      value: 73.28139189595674
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TwentyNewsgroupsClustering
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
      split: test
      type: mteb/twentynewsgroups-clustering
    metrics:
    - type: v_measure
      value: 49.581627240203474
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB TwitterSemEval2015
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
      split: test
      type: mteb/twittersemeval2015-pairclassification
    metrics:
    - type: cos_sim_accuracy
      value: 87.78089050485785
    - type: cos_sim_ap
      value: 79.64487116574168
    - type: cos_sim_f1
      value: 72.46563021970964
    - type: cos_sim_precision
      value: 70.62359128474831
    - type: cos_sim_recall
      value: 74.40633245382587
    - type: dot_accuracy
      value: 86.2609524944865
    - type: dot_ap
      value: 75.513046857613
    - type: dot_f1
      value: 68.58213616489695
    - type: dot_precision
      value: 65.12455516014235
    - type: dot_recall
      value: 72.42744063324538
    - type: euclidean_accuracy
      value: 87.6080348095607
    - type: euclidean_ap
      value: 79.00204933649795
    - type: euclidean_f1
      value: 72.14495342605589
    - type: euclidean_precision
      value: 69.85421299728193
    - type: euclidean_recall
      value: 74.5910290237467
    - type: manhattan_accuracy
      value: 87.59611372712642
    - type: manhattan_ap
      value: 78.78523756706264
    - type: manhattan_f1
      value: 71.86499137718648
    - type: manhattan_precision
      value: 67.39833641404806
    - type: manhattan_recall
      value: 76.96569920844327
    - type: max_accuracy
      value: 87.78089050485785
    - type: max_ap
      value: 79.64487116574168
    - type: max_f1
      value: 72.46563021970964
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB TwitterURLCorpus
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
      split: test
      type: mteb/twitterurlcorpus-pairclassification
    metrics:
    - type: cos_sim_accuracy
      value: 89.98719292117825
    - type: cos_sim_ap
      value: 87.58146137353202
    - type: cos_sim_f1
      value: 80.28543232369239
    - type: cos_sim_precision
      value: 79.1735289714029
    - type: cos_sim_recall
      value: 81.42901139513397
    - type: dot_accuracy
      value: 88.9199363526992
    - type: dot_ap
      value: 84.98499998630417
    - type: dot_f1
      value: 78.21951400757969
    - type: dot_precision
      value: 75.58523624874336
    - type: dot_recall
      value: 81.04404065291038
    - type: euclidean_accuracy
      value: 89.77374160748244
    - type: euclidean_ap
      value: 87.35151562835209
    - type: euclidean_f1
      value: 79.92160922940393
    - type: euclidean_precision
      value: 76.88531587933979
    - type: euclidean_recall
      value: 83.20757622420696
    - type: manhattan_accuracy
      value: 89.72717041176699
    - type: manhattan_ap
      value: 87.34065592142515
    - type: manhattan_f1
      value: 79.85603419187943
    - type: manhattan_precision
      value: 77.82243332115455
    - type: manhattan_recall
      value: 81.99876809362489
    - type: max_accuracy
      value: 89.98719292117825
    - type: max_ap
      value: 87.58146137353202
    - type: max_f1
      value: 80.28543232369239
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB AFQMC
      revision: b44c3b011063adb25877c13823db83bb193913c4
      split: validation
      type: C-MTEB/AFQMC
    metrics:
    - type: cos_sim_pearson
      value: 53.45954203592337
    - type: cos_sim_spearman
      value: 58.42154680418638
    - type: euclidean_pearson
      value: 56.41543791722753
    - type: euclidean_spearman
      value: 58.39328016640146
    - type: manhattan_pearson
      value: 56.318510356833876
    - type: manhattan_spearman
      value: 58.28423447818184
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB ATEC
      revision: 0f319b1142f28d00e055a6770f3f726ae9b7d865
      split: test
      type: C-MTEB/ATEC
    metrics:
    - type: cos_sim_pearson
      value: 50.78356460675945
    - type: cos_sim_spearman
      value: 55.6530411663269
    - type: euclidean_pearson
      value: 56.50763660417816
    - type: euclidean_spearman
      value: 55.733823335669065
    - type: manhattan_pearson
      value: 56.45323093512866
    - type: manhattan_spearman
      value: 55.63248619032702
    task:
      type: STS
  - dataset:
      config: zh
      name: MTEB AmazonReviewsClassification (zh)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 47.209999999999994
    - type: f1
      value: 46.08892432018655
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BQ
      revision: e3dda5e115e487b39ec7e618c0c6a29137052a55
      split: test
      type: C-MTEB/BQ
    metrics:
    - type: cos_sim_pearson
      value: 70.25573992001478
    - type: cos_sim_spearman
      value: 73.85247134951433
    - type: euclidean_pearson
      value: 72.60033082168442
    - type: euclidean_spearman
      value: 73.72445893756499
    - type: manhattan_pearson
      value: 72.59932284620231
    - type: manhattan_spearman
      value: 73.68002490614583
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB CLSClusteringP2P
      revision: 4b6227591c6c1a73bc76b1055f3b7f3588e72476
      split: test
      type: C-MTEB/CLSClusteringP2P
    metrics:
    - type: v_measure
      value: 45.21317724305628
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CLSClusteringS2S
      revision: e458b3f5414b62b7f9f83499ac1f5497ae2e869f
      split: test
      type: C-MTEB/CLSClusteringS2S
    metrics:
    - type: v_measure
      value: 42.49825170976724
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CMedQAv1
      revision: 8d7f1e942507dac42dc58017c1a001c3717da7df
      split: test
      type: C-MTEB/CMedQAv1-reranking
    metrics:
    - type: map
      value: 88.15661686810597
    - type: mrr
      value: 90.11222222222223
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB CMedQAv2
      revision: 23d186750531a14a0357ca22cd92d712fd512ea0
      split: test
      type: C-MTEB/CMedQAv2-reranking
    metrics:
    - type: map
      value: 88.1204726064383
    - type: mrr
      value: 90.20142857142858
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB CmedqaRetrieval
      revision: cd540c506dae1cf9e9a59c3e06f42030d54e7301
      split: dev
      type: C-MTEB/CmedqaRetrieval
    metrics:
    - type: map_at_1
      value: 27.224999999999998
    - type: map_at_10
      value: 40.169
    - type: map_at_100
      value: 42.0
    - type: map_at_1000
      value: 42.109
    - type: map_at_3
      value: 35.76
    - type: map_at_5
      value: 38.221
    - type: mrr_at_1
      value: 40.56
    - type: mrr_at_10
      value: 49.118
    - type: mrr_at_100
      value: 50.092999999999996
    - type: mrr_at_1000
      value: 50.133
    - type: mrr_at_3
      value: 46.507
    - type: mrr_at_5
      value: 47.973
    - type: ndcg_at_1
      value: 40.56
    - type: ndcg_at_10
      value: 46.972
    - type: ndcg_at_100
      value: 54.04
    - type: ndcg_at_1000
      value: 55.862
    - type: ndcg_at_3
      value: 41.36
    - type: ndcg_at_5
      value: 43.704
    - type: precision_at_1
      value: 40.56
    - type: precision_at_10
      value: 10.302999999999999
    - type: precision_at_100
      value: 1.606
    - type: precision_at_1000
      value: 0.184
    - type: precision_at_3
      value: 23.064
    - type: precision_at_5
      value: 16.764000000000003
    - type: recall_at_1
      value: 27.224999999999998
    - type: recall_at_10
      value: 58.05200000000001
    - type: recall_at_100
      value: 87.092
    - type: recall_at_1000
      value: 99.099
    - type: recall_at_3
      value: 41.373
    - type: recall_at_5
      value: 48.453
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Cmnli
      revision: 41bc36f332156f7adc9e38f53777c959b2ae9766
      split: validation
      type: C-MTEB/CMNLI
    metrics:
    - type: cos_sim_accuracy
      value: 77.40228502705953
    - type: cos_sim_ap
      value: 86.22359172956327
    - type: cos_sim_f1
      value: 78.96328293736501
    - type: cos_sim_precision
      value: 73.36945615091311
    - type: cos_sim_recall
      value: 85.48047696983868
    - type: dot_accuracy
      value: 75.53818400481059
    - type: dot_ap
      value: 83.70164011305312
    - type: dot_f1
      value: 77.67298719348754
    - type: dot_precision
      value: 67.49482401656314
    - type: dot_recall
      value: 91.46598082768296
    - type: euclidean_accuracy
      value: 77.94347564642213
    - type: euclidean_ap
      value: 86.4652108728609
    - type: euclidean_f1
      value: 79.15555555555555
    - type: euclidean_precision
      value: 75.41816641964853
    - type: euclidean_recall
      value: 83.28267477203647
    - type: manhattan_accuracy
      value: 77.45039085989175
    - type: manhattan_ap
      value: 86.09986583900665
    - type: manhattan_f1
      value: 78.93669264438988
    - type: manhattan_precision
      value: 72.63261296660117
    - type: manhattan_recall
      value: 86.43909282207154
    - type: max_accuracy
      value: 77.94347564642213
    - type: max_ap
      value: 86.4652108728609
    - type: max_f1
      value: 79.15555555555555
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB CovidRetrieval
      revision: 1271c7809071a13532e05f25fb53511ffce77117
      split: dev
      type: C-MTEB/CovidRetrieval
    metrics:
    - type: map_at_1
      value: 69.336
    - type: map_at_10
      value: 77.16
    - type: map_at_100
      value: 77.47500000000001
    - type: map_at_1000
      value: 77.482
    - type: map_at_3
      value: 75.42999999999999
    - type: map_at_5
      value: 76.468
    - type: mrr_at_1
      value: 69.44200000000001
    - type: mrr_at_10
      value: 77.132
    - type: mrr_at_100
      value: 77.43299999999999
    - type: mrr_at_1000
      value: 77.44
    - type: mrr_at_3
      value: 75.395
    - type: mrr_at_5
      value: 76.459
    - type: ndcg_at_1
      value: 69.547
    - type: ndcg_at_10
      value: 80.794
    - type: ndcg_at_100
      value: 82.245
    - type: ndcg_at_1000
      value: 82.40899999999999
    - type: ndcg_at_3
      value: 77.303
    - type: ndcg_at_5
      value: 79.168
    - type: precision_at_1
      value: 69.547
    - type: precision_at_10
      value: 9.305
    - type: precision_at_100
      value: 0.9979999999999999
    - type: precision_at_1000
      value: 0.101
    - type: precision_at_3
      value: 27.749000000000002
    - type: precision_at_5
      value: 17.576
    - type: recall_at_1
      value: 69.336
    - type: recall_at_10
      value: 92.097
    - type: recall_at_100
      value: 98.736
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 82.64
    - type: recall_at_5
      value: 87.144
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DuRetrieval
      revision: a1a333e290fe30b10f3f56498e3a0d911a693ced
      split: dev
      type: C-MTEB/DuRetrieval
    metrics:
    - type: map_at_1
      value: 26.817999999999998
    - type: map_at_10
      value: 82.67
    - type: map_at_100
      value: 85.304
    - type: map_at_1000
      value: 85.334
    - type: map_at_3
      value: 57.336
    - type: map_at_5
      value: 72.474
    - type: mrr_at_1
      value: 91.45
    - type: mrr_at_10
      value: 94.272
    - type: mrr_at_100
      value: 94.318
    - type: mrr_at_1000
      value: 94.32000000000001
    - type: mrr_at_3
      value: 94.0
    - type: mrr_at_5
      value: 94.17699999999999
    - type: ndcg_at_1
      value: 91.45
    - type: ndcg_at_10
      value: 89.404
    - type: ndcg_at_100
      value: 91.724
    - type: ndcg_at_1000
      value: 91.973
    - type: ndcg_at_3
      value: 88.104
    - type: ndcg_at_5
      value: 87.25699999999999
    - type: precision_at_1
      value: 91.45
    - type: precision_at_10
      value: 42.585
    - type: precision_at_100
      value: 4.838
    - type: precision_at_1000
      value: 0.49
    - type: precision_at_3
      value: 78.8
    - type: precision_at_5
      value: 66.66
    - type: recall_at_1
      value: 26.817999999999998
    - type: recall_at_10
      value: 90.67
    - type: recall_at_100
      value: 98.36200000000001
    - type: recall_at_1000
      value: 99.583
    - type: recall_at_3
      value: 59.614999999999995
    - type: recall_at_5
      value: 77.05199999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB EcomRetrieval
      revision: 687de13dc7294d6fd9be10c6945f9e8fec8166b9
      split: dev
      type: C-MTEB/EcomRetrieval
    metrics:
    - type: map_at_1
      value: 47.699999999999996
    - type: map_at_10
      value: 57.589999999999996
    - type: map_at_100
      value: 58.226
    - type: map_at_1000
      value: 58.251
    - type: map_at_3
      value: 55.233
    - type: map_at_5
      value: 56.633
    - type: mrr_at_1
      value: 47.699999999999996
    - type: mrr_at_10
      value: 57.589999999999996
    - type: mrr_at_100
      value: 58.226
    - type: mrr_at_1000
      value: 58.251
    - type: mrr_at_3
      value: 55.233
    - type: mrr_at_5
      value: 56.633
    - type: ndcg_at_1
      value: 47.699999999999996
    - type: ndcg_at_10
      value: 62.505
    - type: ndcg_at_100
      value: 65.517
    - type: ndcg_at_1000
      value: 66.19800000000001
    - type: ndcg_at_3
      value: 57.643
    - type: ndcg_at_5
      value: 60.181
    - type: precision_at_1
      value: 47.699999999999996
    - type: precision_at_10
      value: 7.8
    - type: precision_at_100
      value: 0.919
    - type: precision_at_1000
      value: 0.097
    - type: precision_at_3
      value: 21.532999999999998
    - type: precision_at_5
      value: 14.16
    - type: recall_at_1
      value: 47.699999999999996
    - type: recall_at_10
      value: 78.0
    - type: recall_at_100
      value: 91.9
    - type: recall_at_1000
      value: 97.3
    - type: recall_at_3
      value: 64.60000000000001
    - type: recall_at_5
      value: 70.8
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB IFlyTek
      revision: 421605374b29664c5fc098418fe20ada9bd55f8a
      split: validation
      type: C-MTEB/IFlyTek-classification
    metrics:
    - type: accuracy
      value: 44.84801846864178
    - type: f1
      value: 37.47347897956339
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB JDReview
      revision: b7c64bd89eb87f8ded463478346f76731f07bf8b
      split: test
      type: C-MTEB/JDReview-classification
    metrics:
    - type: accuracy
      value: 85.81613508442777
    - type: ap
      value: 52.68244615477374
    - type: f1
      value: 80.0445640948843
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LCQMC
      revision: 17f9b096f80380fce5ed12a9be8be7784b337daf
      split: test
      type: C-MTEB/LCQMC
    metrics:
    - type: cos_sim_pearson
      value: 69.57786502217138
    - type: cos_sim_spearman
      value: 75.39106054489906
    - type: euclidean_pearson
      value: 73.72082954602402
    - type: euclidean_spearman
      value: 75.14421475913619
    - type: manhattan_pearson
      value: 73.62463076633642
    - type: manhattan_spearman
      value: 75.01301565104112
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB MMarcoReranking
      revision: None
      split: dev
      type: C-MTEB/Mmarco-reranking
    metrics:
    - type: map
      value: 29.143797057999134
    - type: mrr
      value: 28.08174603174603
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB MMarcoRetrieval
      revision: 539bbde593d947e2a124ba72651aafc09eb33fc2
      split: dev
      type: C-MTEB/MMarcoRetrieval
    metrics:
    - type: map_at_1
      value: 70.492
    - type: map_at_10
      value: 79.501
    - type: map_at_100
      value: 79.728
    - type: map_at_1000
      value: 79.735
    - type: map_at_3
      value: 77.77
    - type: map_at_5
      value: 78.851
    - type: mrr_at_1
      value: 72.822
    - type: mrr_at_10
      value: 80.001
    - type: mrr_at_100
      value: 80.19
    - type: mrr_at_1000
      value: 80.197
    - type: mrr_at_3
      value: 78.484
    - type: mrr_at_5
      value: 79.42099999999999
    - type: ndcg_at_1
      value: 72.822
    - type: ndcg_at_10
      value: 83.013
    - type: ndcg_at_100
      value: 84.013
    - type: ndcg_at_1000
      value: 84.20400000000001
    - type: ndcg_at_3
      value: 79.728
    - type: ndcg_at_5
      value: 81.542
    - type: precision_at_1
      value: 72.822
    - type: precision_at_10
      value: 9.917
    - type: precision_at_100
      value: 1.042
    - type: precision_at_1000
      value: 0.106
    - type: precision_at_3
      value: 29.847
    - type: precision_at_5
      value: 18.871
    - type: recall_at_1
      value: 70.492
    - type: recall_at_10
      value: 93.325
    - type: recall_at_100
      value: 97.822
    - type: recall_at_1000
      value: 99.319
    - type: recall_at_3
      value: 84.636
    - type: recall_at_5
      value: 88.93100000000001
    task:
      type: Retrieval
  - dataset:
      config: zh-CN
      name: MTEB MassiveIntentClassification (zh-CN)
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 76.88298587760592
    - type: f1
      value: 73.89001762017176
    task:
      type: Classification
  - dataset:
      config: zh-CN
      name: MTEB MassiveScenarioClassification (zh-CN)
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 80.76328177538669
    - type: f1
      value: 80.24718532423358
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MedicalRetrieval
      revision: 2039188fb5800a9803ba5048df7b76e6fb151fc6
      split: dev
      type: C-MTEB/MedicalRetrieval
    metrics:
    - type: map_at_1
      value: 49.6
    - type: map_at_10
      value: 55.620999999999995
    - type: map_at_100
      value: 56.204
    - type: map_at_1000
      value: 56.251
    - type: map_at_3
      value: 54.132999999999996
    - type: map_at_5
      value: 54.933
    - type: mrr_at_1
      value: 49.7
    - type: mrr_at_10
      value: 55.67100000000001
    - type: mrr_at_100
      value: 56.254000000000005
    - type: mrr_at_1000
      value: 56.301
    - type: mrr_at_3
      value: 54.18300000000001
    - type: mrr_at_5
      value: 54.983000000000004
    - type: ndcg_at_1
      value: 49.6
    - type: ndcg_at_10
      value: 58.645
    - type: ndcg_at_100
      value: 61.789
    - type: ndcg_at_1000
      value: 63.219
    - type: ndcg_at_3
      value: 55.567
    - type: ndcg_at_5
      value: 57.008
    - type: precision_at_1
      value: 49.6
    - type: precision_at_10
      value: 6.819999999999999
    - type: precision_at_100
      value: 0.836
    - type: precision_at_1000
      value: 0.095
    - type: precision_at_3
      value: 19.900000000000002
    - type: precision_at_5
      value: 12.64
    - type: recall_at_1
      value: 49.6
    - type: recall_at_10
      value: 68.2
    - type: recall_at_100
      value: 83.6
    - type: recall_at_1000
      value: 95.3
    - type: recall_at_3
      value: 59.699999999999996
    - type: recall_at_5
      value: 63.2
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB MultilingualSentiment
      revision: 46958b007a63fdbf239b7672c25d0bea67b5ea1a
      split: validation
      type: C-MTEB/MultilingualSentiment-classification
    metrics:
    - type: accuracy
      value: 74.45666666666666
    - type: f1
      value: 74.32582402190089
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB Ocnli
      revision: 66e76a618a34d6d565d5538088562851e6daa7ec
      split: validation
      type: C-MTEB/OCNLI
    metrics:
    - type: cos_sim_accuracy
      value: 80.67135896047645
    - type: cos_sim_ap
      value: 87.60421240712051
    - type: cos_sim_f1
      value: 82.1304131408661
    - type: cos_sim_precision
      value: 77.68361581920904
    - type: cos_sim_recall
      value: 87.11721224920802
    - type: dot_accuracy
      value: 79.04710341093666
    - type: dot_ap
      value: 85.6370059719336
    - type: dot_f1
      value: 80.763723150358
    - type: dot_precision
      value: 73.69337979094077
    - type: dot_recall
      value: 89.33474128827878
    - type: euclidean_accuracy
      value: 81.05035192203573
    - type: euclidean_ap
      value: 87.7880240053663
    - type: euclidean_f1
      value: 82.50244379276637
    - type: euclidean_precision
      value: 76.7970882620564
    - type: euclidean_recall
      value: 89.1235480464625
    - type: manhattan_accuracy
      value: 80.61721710882512
    - type: manhattan_ap
      value: 87.43568120591175
    - type: manhattan_f1
      value: 81.89526184538653
    - type: manhattan_precision
      value: 77.5992438563327
    - type: manhattan_recall
      value: 86.6948257655755
    - type: max_accuracy
      value: 81.05035192203573
    - type: max_ap
      value: 87.7880240053663
    - type: max_f1
      value: 82.50244379276637
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB OnlineShopping
      revision: e610f2ebd179a8fda30ae534c3878750a96db120
      split: test
      type: C-MTEB/OnlineShopping-classification
    metrics:
    - type: accuracy
      value: 93.5
    - type: ap
      value: 91.31357903446782
    - type: f1
      value: 93.48088994006616
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB PAWSX
      revision: 9c6a90e430ac22b5779fb019a23e820b11a8b5e1
      split: test
      type: C-MTEB/PAWSX
    metrics:
    - type: cos_sim_pearson
      value: 36.93293453538077
    - type: cos_sim_spearman
      value: 42.45972506308574
    - type: euclidean_pearson
      value: 42.34945133152159
    - type: euclidean_spearman
      value: 42.331610303674644
    - type: manhattan_pearson
      value: 42.31455070249498
    - type: manhattan_spearman
      value: 42.19887982891834
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB QBQTC
      revision: 790b0510dc52b1553e8c49f3d2afb48c0e5c48b7
      split: test
      type: C-MTEB/QBQTC
    metrics:
    - type: cos_sim_pearson
      value: 33.683290790043785
    - type: cos_sim_spearman
      value: 35.149171171202994
    - type: euclidean_pearson
      value: 32.33806561267862
    - type: euclidean_spearman
      value: 34.483576387347966
    - type: manhattan_pearson
      value: 32.47629754599608
    - type: manhattan_spearman
      value: 34.66434471867615
    task:
      type: STS
  - dataset:
      config: zh
      name: MTEB STS22 (zh)
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cos_sim_pearson
      value: 66.46322760516104
    - type: cos_sim_spearman
      value: 67.398478319726
    - type: euclidean_pearson
      value: 64.7223480293625
    - type: euclidean_spearman
      value: 66.83118568812951
    - type: manhattan_pearson
      value: 64.88440039828305
    - type: manhattan_spearman
      value: 66.80429458952257
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSB
      revision: 0cde68302b3541bb8b3c340dc0644b0b745b3dc0
      split: test
      type: C-MTEB/STSB
    metrics:
    - type: cos_sim_pearson
      value: 79.08991383232105
    - type: cos_sim_spearman
      value: 79.39715677296854
    - type: euclidean_pearson
      value: 78.63201279320496
    - type: euclidean_spearman
      value: 79.40262660785731
    - type: manhattan_pearson
      value: 78.98138363146906
    - type: manhattan_spearman
      value: 79.79968413014194
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB T2Reranking
      revision: 76631901a18387f85eaa53e5450019b87ad58ef9
      split: dev
      type: C-MTEB/T2Reranking
    metrics:
    - type: map
      value: 67.43289278789972
    - type: mrr
      value: 77.53012460908535
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB T2Retrieval
      revision: 8731a845f1bf500a4f111cf1070785c793d10e64
      split: dev
      type: C-MTEB/T2Retrieval
    metrics:
    - type: map_at_1
      value: 27.733999999999998
    - type: map_at_10
      value: 78.24799999999999
    - type: map_at_100
      value: 81.765
    - type: map_at_1000
      value: 81.824
    - type: map_at_3
      value: 54.92
    - type: map_at_5
      value: 67.61399999999999
    - type: mrr_at_1
      value: 90.527
    - type: mrr_at_10
      value: 92.843
    - type: mrr_at_100
      value: 92.927
    - type: mrr_at_1000
      value: 92.93
    - type: mrr_at_3
      value: 92.45100000000001
    - type: mrr_at_5
      value: 92.693
    - type: ndcg_at_1
      value: 90.527
    - type: ndcg_at_10
      value: 85.466
    - type: ndcg_at_100
      value: 88.846
    - type: ndcg_at_1000
      value: 89.415
    - type: ndcg_at_3
      value: 86.768
    - type: ndcg_at_5
      value: 85.46000000000001
    - type: precision_at_1
      value: 90.527
    - type: precision_at_10
      value: 42.488
    - type: precision_at_100
      value: 5.024
    - type: precision_at_1000
      value: 0.516
    - type: precision_at_3
      value: 75.907
    - type: precision_at_5
      value: 63.727000000000004
    - type: recall_at_1
      value: 27.733999999999998
    - type: recall_at_10
      value: 84.346
    - type: recall_at_100
      value: 95.536
    - type: recall_at_1000
      value: 98.42999999999999
    - type: recall_at_3
      value: 56.455
    - type: recall_at_5
      value: 70.755
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB TNews
      revision: 317f262bf1e6126357bbe89e875451e4b0938fe4
      split: validation
      type: C-MTEB/TNews-classification
    metrics:
    - type: accuracy
      value: 49.952000000000005
    - type: f1
      value: 48.264617195258054
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ThuNewsClusteringP2P
      revision: 5798586b105c0434e4f0fe5e767abe619442cf93
      split: test
      type: C-MTEB/ThuNewsClusteringP2P
    metrics:
    - type: v_measure
      value: 68.23769904483508
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ThuNewsClusteringS2S
      revision: 8a8b2caeda43f39e13c4bc5bea0f8a667896e10d
      split: test
      type: C-MTEB/ThuNewsClusteringS2S
    metrics:
    - type: v_measure
      value: 62.50294403136556
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB VideoRetrieval
      revision: 58c2597a5943a2ba48f4668c3b90d796283c5639
      split: dev
      type: C-MTEB/VideoRetrieval
    metrics:
    - type: map_at_1
      value: 54.0
    - type: map_at_10
      value: 63.668
    - type: map_at_100
      value: 64.217
    - type: map_at_1000
      value: 64.23100000000001
    - type: map_at_3
      value: 61.7
    - type: map_at_5
      value: 62.870000000000005
    - type: mrr_at_1
      value: 54.0
    - type: mrr_at_10
      value: 63.668
    - type: mrr_at_100
      value: 64.217
    - type: mrr_at_1000
      value: 64.23100000000001
    - type: mrr_at_3
      value: 61.7
    - type: mrr_at_5
      value: 62.870000000000005
    - type: ndcg_at_1
      value: 54.0
    - type: ndcg_at_10
      value: 68.11399999999999
    - type: ndcg_at_100
      value: 70.723
    - type: ndcg_at_1000
      value: 71.123
    - type: ndcg_at_3
      value: 64.074
    - type: ndcg_at_5
      value: 66.178
    - type: precision_at_1
      value: 54.0
    - type: precision_at_10
      value: 8.200000000000001
    - type: precision_at_100
      value: 0.941
    - type: precision_at_1000
      value: 0.097
    - type: precision_at_3
      value: 23.633000000000003
    - type: precision_at_5
      value: 15.2
    - type: recall_at_1
      value: 54.0
    - type: recall_at_10
      value: 82.0
    - type: recall_at_100
      value: 94.1
    - type: recall_at_1000
      value: 97.3
    - type: recall_at_3
      value: 70.89999999999999
    - type: recall_at_5
      value: 76.0
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Waimai
      revision: 339287def212450dcaa9df8c22bf93e9980c7023
      split: test
      type: C-MTEB/waimai-classification
    metrics:
    - type: accuracy
      value: 86.63000000000001
    - type: ap
      value: 69.99457882599567
    - type: f1
      value: 85.07735617998541
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB 8TagsClustering
      revision: None
      split: test
      type: PL-MTEB/8tags-clustering
    metrics:
    - type: v_measure
      value: 44.594104491193555
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AllegroReviews
      revision: None
      split: test
      type: PL-MTEB/allegro-reviews
    metrics:
    - type: accuracy
      value: 63.97614314115309
    - type: f1
      value: 52.15634261679283
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ArguAna-PL
      revision: 63fc86750af76253e8c760fc9e534bbf24d260a2
      split: test
      type: clarin-knext/arguana-pl
    metrics:
    - type: map_at_1
      value: 32.646
    - type: map_at_10
      value: 47.963
    - type: map_at_100
      value: 48.789
    - type: map_at_1000
      value: 48.797000000000004
    - type: map_at_3
      value: 43.196
    - type: map_at_5
      value: 46.016
    - type: mrr_at_1
      value: 33.073
    - type: mrr_at_10
      value: 48.126000000000005
    - type: mrr_at_100
      value: 48.946
    - type: mrr_at_1000
      value: 48.953
    - type: mrr_at_3
      value: 43.374
    - type: mrr_at_5
      value: 46.147
    - type: ndcg_at_1
      value: 32.646
    - type: ndcg_at_10
      value: 56.481
    - type: ndcg_at_100
      value: 59.922
    - type: ndcg_at_1000
      value: 60.07
    - type: ndcg_at_3
      value: 46.675
    - type: ndcg_at_5
      value: 51.76500000000001
    - type: precision_at_1
      value: 32.646
    - type: precision_at_10
      value: 8.371
    - type: precision_at_100
      value: 0.9860000000000001
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 18.919
    - type: precision_at_5
      value: 13.825999999999999
    - type: recall_at_1
      value: 32.646
    - type: recall_at_10
      value: 83.71300000000001
    - type: recall_at_100
      value: 98.578
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 56.757000000000005
    - type: recall_at_5
      value: 69.132
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CBD
      revision: None
      split: test
      type: PL-MTEB/cbd
    metrics:
    - type: accuracy
      value: 68.56
    - type: ap
      value: 23.310493680488513
    - type: f1
      value: 58.85369533105693
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CDSC-E
      revision: None
      split: test
      type: PL-MTEB/cdsce-pairclassification
    metrics:
    - type: cos_sim_accuracy
      value: 88.5
    - type: cos_sim_ap
      value: 72.42140924378361
    - type: cos_sim_f1
      value: 66.0919540229885
    - type: cos_sim_precision
      value: 72.78481012658227
    - type: cos_sim_recall
      value: 60.526315789473685
    - type: dot_accuracy
      value: 88.5
    - type: dot_ap
      value: 72.42140924378361
    - type: dot_f1
      value: 66.0919540229885
    - type: dot_precision
      value: 72.78481012658227
    - type: dot_recall
      value: 60.526315789473685
    - type: euclidean_accuracy
      value: 88.5
    - type: euclidean_ap
      value: 72.42140924378361
    - type: euclidean_f1
      value: 66.0919540229885
    - type: euclidean_precision
      value: 72.78481012658227
    - type: euclidean_recall
      value: 60.526315789473685
    - type: manhattan_accuracy
      value: 88.5
    - type: manhattan_ap
      value: 72.49745515311696
    - type: manhattan_f1
      value: 66.0968660968661
    - type: manhattan_precision
      value: 72.04968944099379
    - type: manhattan_recall
      value: 61.05263157894737
    - type: max_accuracy
      value: 88.5
    - type: max_ap
      value: 72.49745515311696
    - type: max_f1
      value: 66.0968660968661
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB CDSC-R
      revision: None
      split: test
      type: PL-MTEB/cdscr-sts
    metrics:
    - type: cos_sim_pearson
      value: 90.32269765590145
    - type: cos_sim_spearman
      value: 89.73666311491672
    - type: euclidean_pearson
      value: 88.2933868516544
    - type: euclidean_spearman
      value: 89.73666311491672
    - type: manhattan_pearson
      value: 88.33474590219448
    - type: manhattan_spearman
      value: 89.8548364866583
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB DBPedia-PL
      revision: 76afe41d9af165cc40999fcaa92312b8b012064a
      split: test
      type: clarin-knext/dbpedia-pl
    metrics:
    - type: map_at_1
      value: 7.632999999999999
    - type: map_at_10
      value: 16.426
    - type: map_at_100
      value: 22.651
    - type: map_at_1000
      value: 24.372
    - type: map_at_3
      value: 11.706
    - type: map_at_5
      value: 13.529
    - type: mrr_at_1
      value: 60.75000000000001
    - type: mrr_at_10
      value: 68.613
    - type: mrr_at_100
      value: 69.001
    - type: mrr_at_1000
      value: 69.021
    - type: mrr_at_3
      value: 67.0
    - type: mrr_at_5
      value: 67.925
    - type: ndcg_at_1
      value: 49.875
    - type: ndcg_at_10
      value: 36.978
    - type: ndcg_at_100
      value: 40.031
    - type: ndcg_at_1000
      value: 47.566
    - type: ndcg_at_3
      value: 41.148
    - type: ndcg_at_5
      value: 38.702
    - type: precision_at_1
      value: 60.75000000000001
    - type: precision_at_10
      value: 29.7
    - type: precision_at_100
      value: 9.278
    - type: precision_at_1000
      value: 2.099
    - type: precision_at_3
      value: 44.0
    - type: precision_at_5
      value: 37.6
    - type: recall_at_1
      value: 7.632999999999999
    - type: recall_at_10
      value: 22.040000000000003
    - type: recall_at_100
      value: 44.024
    - type: recall_at_1000
      value: 67.848
    - type: recall_at_3
      value: 13.093
    - type: recall_at_5
      value: 15.973
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA-PL
      revision: 2e535829717f8bf9dc829b7f911cc5bbd4e6608e
      split: test
      type: clarin-knext/fiqa-pl
    metrics:
    - type: map_at_1
      value: 15.473
    - type: map_at_10
      value: 24.579
    - type: map_at_100
      value: 26.387
    - type: map_at_1000
      value: 26.57
    - type: map_at_3
      value: 21.278
    - type: map_at_5
      value: 23.179
    - type: mrr_at_1
      value: 30.709999999999997
    - type: mrr_at_10
      value: 38.994
    - type: mrr_at_100
      value: 39.993
    - type: mrr_at_1000
      value: 40.044999999999995
    - type: mrr_at_3
      value: 36.342999999999996
    - type: mrr_at_5
      value: 37.846999999999994
    - type: ndcg_at_1
      value: 30.709999999999997
    - type: ndcg_at_10
      value: 31.608999999999998
    - type: ndcg_at_100
      value: 38.807
    - type: ndcg_at_1000
      value: 42.208
    - type: ndcg_at_3
      value: 28.086
    - type: ndcg_at_5
      value: 29.323
    - type: precision_at_1
      value: 30.709999999999997
    - type: precision_at_10
      value: 8.688
    - type: precision_at_100
      value: 1.608
    - type: precision_at_1000
      value: 0.22100000000000003
    - type: precision_at_3
      value: 18.724
    - type: precision_at_5
      value: 13.950999999999999
    - type: recall_at_1
      value: 15.473
    - type: recall_at_10
      value: 38.361000000000004
    - type: recall_at_100
      value: 65.2
    - type: recall_at_1000
      value: 85.789
    - type: recall_at_3
      value: 25.401
    - type: recall_at_5
      value: 30.875999999999998
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA-PL
      revision: a0bd479ac97b4ccb5bd6ce320c415d0bb4beb907
      split: test
      type: clarin-knext/hotpotqa-pl
    metrics:
    - type: map_at_1
      value: 38.096000000000004
    - type: map_at_10
      value: 51.44499999999999
    - type: map_at_100
      value: 52.325
    - type: map_at_1000
      value: 52.397000000000006
    - type: map_at_3
      value: 48.626999999999995
    - type: map_at_5
      value: 50.342
    - type: mrr_at_1
      value: 76.19200000000001
    - type: mrr_at_10
      value: 81.191
    - type: mrr_at_100
      value: 81.431
    - type: mrr_at_1000
      value: 81.443
    - type: mrr_at_3
      value: 80.30199999999999
    - type: mrr_at_5
      value: 80.85900000000001
    - type: ndcg_at_1
      value: 76.19200000000001
    - type: ndcg_at_10
      value: 60.9
    - type: ndcg_at_100
      value: 64.14699999999999
    - type: ndcg_at_1000
      value: 65.647
    - type: ndcg_at_3
      value: 56.818000000000005
    - type: ndcg_at_5
      value: 59.019999999999996
    - type: precision_at_1
      value: 76.19200000000001
    - type: precision_at_10
      value: 12.203
    - type: precision_at_100
      value: 1.478
    - type: precision_at_1000
      value: 0.168
    - type: precision_at_3
      value: 34.616
    - type: precision_at_5
      value: 22.515
    - type: recall_at_1
      value: 38.096000000000004
    - type: recall_at_10
      value: 61.013
    - type: recall_at_100
      value: 73.90299999999999
    - type: recall_at_1000
      value: 83.91
    - type: recall_at_3
      value: 51.92400000000001
    - type: recall_at_5
      value: 56.286
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB MSMARCO-PL
      revision: 8634c07806d5cce3a6138e260e59b81760a0a640
      split: test
      type: clarin-knext/msmarco-pl
    metrics:
    - type: map_at_1
      value: 1.548
    - type: map_at_10
      value: 11.049000000000001
    - type: map_at_100
      value: 28.874
    - type: map_at_1000
      value: 34.931
    - type: map_at_3
      value: 4.162
    - type: map_at_5
      value: 6.396
    - type: mrr_at_1
      value: 90.69800000000001
    - type: mrr_at_10
      value: 92.093
    - type: mrr_at_100
      value: 92.345
    - type: mrr_at_1000
      value: 92.345
    - type: mrr_at_3
      value: 91.86
    - type: mrr_at_5
      value: 91.86
    - type: ndcg_at_1
      value: 74.031
    - type: ndcg_at_10
      value: 63.978
    - type: ndcg_at_100
      value: 53.101
    - type: ndcg_at_1000
      value: 60.675999999999995
    - type: ndcg_at_3
      value: 71.421
    - type: ndcg_at_5
      value: 68.098
    - type: precision_at_1
      value: 90.69800000000001
    - type: precision_at_10
      value: 71.86
    - type: precision_at_100
      value: 31.395
    - type: precision_at_1000
      value: 5.981
    - type: precision_at_3
      value: 84.49600000000001
    - type: precision_at_5
      value: 79.07
    - type: recall_at_1
      value: 1.548
    - type: recall_at_10
      value: 12.149000000000001
    - type: recall_at_100
      value: 40.794999999999995
    - type: recall_at_1000
      value: 67.974
    - type: recall_at_3
      value: 4.244
    - type: recall_at_5
      value: 6.608
    task:
      type: Retrieval
  - dataset:
      config: pl
      name: MTEB MassiveIntentClassification (pl)
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 73.55413584398119
    - type: f1
      value: 69.65610882318181
    task:
      type: Classification
  - dataset:
      config: pl
      name: MTEB MassiveScenarioClassification (pl)
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 76.37188971082716
    - type: f1
      value: 75.64847309941361
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB NFCorpus-PL
      revision: 9a6f9567fda928260afed2de480d79c98bf0bec0
      split: test
      type: clarin-knext/nfcorpus-pl
    metrics:
    - type: map_at_1
      value: 4.919
    - type: map_at_10
      value: 10.834000000000001
    - type: map_at_100
      value: 13.38
    - type: map_at_1000
      value: 14.581
    - type: map_at_3
      value: 8.198
    - type: map_at_5
      value: 9.428
    - type: mrr_at_1
      value: 41.176
    - type: mrr_at_10
      value: 50.083
    - type: mrr_at_100
      value: 50.559
    - type: mrr_at_1000
      value: 50.604000000000006
    - type: mrr_at_3
      value: 47.936
    - type: mrr_at_5
      value: 49.407000000000004
    - type: ndcg_at_1
      value: 39.628
    - type: ndcg_at_10
      value: 30.098000000000003
    - type: ndcg_at_100
      value: 27.061
    - type: ndcg_at_1000
      value: 35.94
    - type: ndcg_at_3
      value: 35.135
    - type: ndcg_at_5
      value: 33.335
    - type: precision_at_1
      value: 41.176
    - type: precision_at_10
      value: 22.259999999999998
    - type: precision_at_100
      value: 6.712
    - type: precision_at_1000
      value: 1.9060000000000001
    - type: precision_at_3
      value: 33.23
    - type: precision_at_5
      value: 29.04
    - type: recall_at_1
      value: 4.919
    - type: recall_at_10
      value: 14.196
    - type: recall_at_100
      value: 26.948
    - type: recall_at_1000
      value: 59.211000000000006
    - type: recall_at_3
      value: 9.44
    - type: recall_at_5
      value: 11.569
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NQ-PL
      revision: f171245712cf85dd4700b06bef18001578d0ca8d
      split: test
      type: clarin-knext/nq-pl
    metrics:
    - type: map_at_1
      value: 25.35
    - type: map_at_10
      value: 37.884
    - type: map_at_100
      value: 38.955
    - type: map_at_1000
      value: 39.007999999999996
    - type: map_at_3
      value: 34.239999999999995
    - type: map_at_5
      value: 36.398
    - type: mrr_at_1
      value: 28.737000000000002
    - type: mrr_at_10
      value: 39.973
    - type: mrr_at_100
      value: 40.844
    - type: mrr_at_1000
      value: 40.885
    - type: mrr_at_3
      value: 36.901
    - type: mrr_at_5
      value: 38.721
    - type: ndcg_at_1
      value: 28.708
    - type: ndcg_at_10
      value: 44.204
    - type: ndcg_at_100
      value: 48.978
    - type: ndcg_at_1000
      value: 50.33
    - type: ndcg_at_3
      value: 37.36
    - type: ndcg_at_5
      value: 40.912
    - type: precision_at_1
      value: 28.708
    - type: precision_at_10
      value: 7.367
    - type: precision_at_100
      value: 1.0030000000000001
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 17.034
    - type: precision_at_5
      value: 12.293999999999999
    - type: recall_at_1
      value: 25.35
    - type: recall_at_10
      value: 61.411
    - type: recall_at_100
      value: 82.599
    - type: recall_at_1000
      value: 92.903
    - type: recall_at_3
      value: 43.728
    - type: recall_at_5
      value: 51.854
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB PAC
      revision: None
      split: test
      type: laugustyniak/abusive-clauses-pl
    metrics:
    - type: accuracy
      value: 69.04141326382856
    - type: ap
      value: 77.49422763833996
    - type: f1
      value: 66.73472657783407
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB PPC
      revision: None
      split: test
      type: PL-MTEB/ppc-pairclassification
    metrics:
    - type: cos_sim_accuracy
      value: 81.0
    - type: cos_sim_ap
      value: 91.47194213011349
    - type: cos_sim_f1
      value: 84.73767885532592
    - type: cos_sim_precision
      value: 81.49847094801224
    - type: cos_sim_recall
      value: 88.24503311258279
    - type: dot_accuracy
      value: 81.0
    - type: dot_ap
      value: 91.47194213011349
    - type: dot_f1
      value: 84.73767885532592
    - type: dot_precision
      value: 81.49847094801224
    - type: dot_recall
      value: 88.24503311258279
    - type: euclidean_accuracy
      value: 81.0
    - type: euclidean_ap
      value: 91.47194213011349
    - type: euclidean_f1
      value: 84.73767885532592
    - type: euclidean_precision
      value: 81.49847094801224
    - type: euclidean_recall
      value: 88.24503311258279
    - type: manhattan_accuracy
      value: 81.0
    - type: manhattan_ap
      value: 91.46464475050571
    - type: manhattan_f1
      value: 84.48687350835321
    - type: manhattan_precision
      value: 81.31699846860643
    - type: manhattan_recall
      value: 87.91390728476821
    - type: max_accuracy
      value: 81.0
    - type: max_ap
      value: 91.47194213011349
    - type: max_f1
      value: 84.73767885532592
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB PSC
      revision: None
      split: test
      type: PL-MTEB/psc-pairclassification
    metrics:
    - type: cos_sim_accuracy
      value: 97.6808905380334
    - type: cos_sim_ap
      value: 99.27948611836348
    - type: cos_sim_f1
      value: 96.15975422427034
    - type: cos_sim_precision
      value: 96.90402476780186
    - type: cos_sim_recall
      value: 95.42682926829268
    - type: dot_accuracy
      value: 97.6808905380334
    - type: dot_ap
      value: 99.2794861183635
    - type: dot_f1
      value: 96.15975422427034
    - type: dot_precision
      value: 96.90402476780186
    - type: dot_recall
      value: 95.42682926829268
    - type: euclidean_accuracy
      value: 97.6808905380334
    - type: euclidean_ap
      value: 99.2794861183635
    - type: euclidean_f1
      value: 96.15975422427034
    - type: euclidean_precision
      value: 96.90402476780186
    - type: euclidean_recall
      value: 95.42682926829268
    - type: manhattan_accuracy
      value: 97.6808905380334
    - type: manhattan_ap
      value: 99.28715055268721
    - type: manhattan_f1
      value: 96.14791987673343
    - type: manhattan_precision
      value: 97.19626168224299
    - type: manhattan_recall
      value: 95.1219512195122
    - type: max_accuracy
      value: 97.6808905380334
    - type: max_ap
      value: 99.28715055268721
    - type: max_f1
      value: 96.15975422427034
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB PolEmo2.0-IN
      revision: None
      split: test
      type: PL-MTEB/polemo2_in
    metrics:
    - type: accuracy
      value: 86.16343490304708
    - type: f1
      value: 83.3442579486744
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB PolEmo2.0-OUT
      revision: None
      split: test
      type: PL-MTEB/polemo2_out
    metrics:
    - type: accuracy
      value: 68.40080971659918
    - type: f1
      value: 53.13720751142237
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB Quora-PL
      revision: 0be27e93455051e531182b85e85e425aba12e9d4
      split: test
      type: clarin-knext/quora-pl
    metrics:
    - type: map_at_1
      value: 63.322
    - type: map_at_10
      value: 76.847
    - type: map_at_100
      value: 77.616
    - type: map_at_1000
      value: 77.644
    - type: map_at_3
      value: 73.624
    - type: map_at_5
      value: 75.603
    - type: mrr_at_1
      value: 72.88
    - type: mrr_at_10
      value: 80.376
    - type: mrr_at_100
      value: 80.604
    - type: mrr_at_1000
      value: 80.61
    - type: mrr_at_3
      value: 78.92
    - type: mrr_at_5
      value: 79.869
    - type: ndcg_at_1
      value: 72.89999999999999
    - type: ndcg_at_10
      value: 81.43
    - type: ndcg_at_100
      value: 83.394
    - type: ndcg_at_1000
      value: 83.685
    - type: ndcg_at_3
      value: 77.62599999999999
    - type: ndcg_at_5
      value: 79.656
    - type: precision_at_1
      value: 72.89999999999999
    - type: precision_at_10
      value: 12.548
    - type: precision_at_100
      value: 1.4869999999999999
    - type: precision_at_1000
      value: 0.155
    - type: precision_at_3
      value: 34.027
    - type: precision_at_5
      value: 22.654
    - type: recall_at_1
      value: 63.322
    - type: recall_at_10
      value: 90.664
    - type: recall_at_100
      value: 97.974
    - type: recall_at_1000
      value: 99.636
    - type: recall_at_3
      value: 80.067
    - type: recall_at_5
      value: 85.526
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SCIDOCS-PL
      revision: 45452b03f05560207ef19149545f168e596c9337
      split: test
      type: clarin-knext/scidocs-pl
    metrics:
    - type: map_at_1
      value: 3.95
    - type: map_at_10
      value: 9.658999999999999
    - type: map_at_100
      value: 11.384
    - type: map_at_1000
      value: 11.677
    - type: map_at_3
      value: 7.055
    - type: map_at_5
      value: 8.244
    - type: mrr_at_1
      value: 19.5
    - type: mrr_at_10
      value: 28.777
    - type: mrr_at_100
      value: 29.936
    - type: mrr_at_1000
      value: 30.009999999999998
    - type: mrr_at_3
      value: 25.55
    - type: mrr_at_5
      value: 27.284999999999997
    - type: ndcg_at_1
      value: 19.5
    - type: ndcg_at_10
      value: 16.589000000000002
    - type: ndcg_at_100
      value: 23.879
    - type: ndcg_at_1000
      value: 29.279
    - type: ndcg_at_3
      value: 15.719
    - type: ndcg_at_5
      value: 13.572000000000001
    - type: precision_at_1
      value: 19.5
    - type: precision_at_10
      value: 8.62
    - type: precision_at_100
      value: 1.924
    - type: precision_at_1000
      value: 0.322
    - type: precision_at_3
      value: 14.6
    - type: precision_at_5
      value: 11.78
    - type: recall_at_1
      value: 3.95
    - type: recall_at_10
      value: 17.477999999999998
    - type: recall_at_100
      value: 38.99
    - type: recall_at_1000
      value: 65.417
    - type: recall_at_3
      value: 8.883000000000001
    - type: recall_at_5
      value: 11.933
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SICK-E-PL
      revision: None
      split: test
      type: PL-MTEB/sicke-pl-pairclassification
    metrics:
    - type: cos_sim_accuracy
      value: 83.48960456583775
    - type: cos_sim_ap
      value: 76.31522115825375
    - type: cos_sim_f1
      value: 70.35573122529645
    - type: cos_sim_precision
      value: 70.9934735315446
    - type: cos_sim_recall
      value: 69.72934472934473
    - type: dot_accuracy
      value: 83.48960456583775
    - type: dot_ap
      value: 76.31522115825373
    - type: dot_f1
      value: 70.35573122529645
    - type: dot_precision
      value: 70.9934735315446
    - type: dot_recall
      value: 69.72934472934473
    - type: euclidean_accuracy
      value: 83.48960456583775
    - type: euclidean_ap
      value: 76.31522115825373
    - type: euclidean_f1
      value: 70.35573122529645
    - type: euclidean_precision
      value: 70.9934735315446
    - type: euclidean_recall
      value: 69.72934472934473
    - type: manhattan_accuracy
      value: 83.46922136159804
    - type: manhattan_ap
      value: 76.18474601388084
    - type: manhattan_f1
      value: 70.34779490856937
    - type: manhattan_precision
      value: 70.83032490974729
    - type: manhattan_recall
      value: 69.87179487179486
    - type: max_accuracy
      value: 83.48960456583775
    - type: max_ap
      value: 76.31522115825375
    - type: max_f1
      value: 70.35573122529645
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB SICK-R-PL
      revision: None
      split: test
      type: PL-MTEB/sickr-pl-sts
    metrics:
    - type: cos_sim_pearson
      value: 77.95374883876302
    - type: cos_sim_spearman
      value: 73.77630219171942
    - type: euclidean_pearson
      value: 75.81927069594934
    - type: euclidean_spearman
      value: 73.7763211303831
    - type: manhattan_pearson
      value: 76.03126859057528
    - type: manhattan_spearman
      value: 73.96528138013369
    task:
      type: STS
  - dataset:
      config: pl
      name: MTEB STS22 (pl)
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cos_sim_pearson
      value: 37.388282764841826
    - type: cos_sim_spearman
      value: 40.83477184710897
    - type: euclidean_pearson
      value: 26.754737044177805
    - type: euclidean_spearman
      value: 40.83477184710897
    - type: manhattan_pearson
      value: 26.760453110872458
    - type: manhattan_spearman
      value: 41.034477441383856
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SciFact-PL
      revision: 47932a35f045ef8ed01ba82bf9ff67f6e109207e
      split: test
      type: clarin-knext/scifact-pl
    metrics:
    - type: map_at_1
      value: 49.15
    - type: map_at_10
      value: 61.690999999999995
    - type: map_at_100
      value: 62.348000000000006
    - type: map_at_1000
      value: 62.38
    - type: map_at_3
      value: 58.824
    - type: map_at_5
      value: 60.662000000000006
    - type: mrr_at_1
      value: 51.333
    - type: mrr_at_10
      value: 62.731
    - type: mrr_at_100
      value: 63.245
    - type: mrr_at_1000
      value: 63.275000000000006
    - type: mrr_at_3
      value: 60.667
    - type: mrr_at_5
      value: 61.93300000000001
    - type: ndcg_at_1
      value: 51.333
    - type: ndcg_at_10
      value: 67.168
    - type: ndcg_at_100
      value: 69.833
    - type: ndcg_at_1000
      value: 70.56700000000001
    - type: ndcg_at_3
      value: 62.40599999999999
    - type: ndcg_at_5
      value: 65.029
    - type: precision_at_1
      value: 51.333
    - type: precision_at_10
      value: 9.333
    - type: precision_at_100
      value: 1.0699999999999998
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 25.333
    - type: precision_at_5
      value: 17.067
    - type: recall_at_1
      value: 49.15
    - type: recall_at_10
      value: 82.533
    - type: recall_at_100
      value: 94.167
    - type: recall_at_1000
      value: 99.667
    - type: recall_at_3
      value: 69.917
    - type: recall_at_5
      value: 76.356
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB TRECCOVID-PL
      revision: 81bcb408f33366c2a20ac54adafad1ae7e877fdd
      split: test
      type: clarin-knext/trec-covid-pl
    metrics:
    - type: map_at_1
      value: 0.261
    - type: map_at_10
      value: 2.1260000000000003
    - type: map_at_100
      value: 12.171999999999999
    - type: map_at_1000
      value: 26.884999999999998
    - type: map_at_3
      value: 0.695
    - type: map_at_5
      value: 1.134
    - type: mrr_at_1
      value: 96.0
    - type: mrr_at_10
      value: 96.952
    - type: mrr_at_100
      value: 96.952
    - type: mrr_at_1000
      value: 96.952
    - type: mrr_at_3
      value: 96.667
    - type: mrr_at_5
      value: 96.667
    - type: ndcg_at_1
      value: 92.0
    - type: ndcg_at_10
      value: 81.193
    - type: ndcg_at_100
      value: 61.129
    - type: ndcg_at_1000
      value: 51.157
    - type: ndcg_at_3
      value: 85.693
    - type: ndcg_at_5
      value: 84.129
    - type: precision_at_1
      value: 96.0
    - type: precision_at_10
      value: 85.39999999999999
    - type: precision_at_100
      value: 62.03999999999999
    - type: precision_at_1000
      value: 22.224
    - type: precision_at_3
      value: 88.0
    - type: precision_at_5
      value: 88.0
    - type: recall_at_1
      value: 0.261
    - type: recall_at_10
      value: 2.262
    - type: recall_at_100
      value: 14.981
    - type: recall_at_1000
      value: 46.837
    - type: recall_at_3
      value: 0.703
    - type: recall_at_5
      value: 1.172
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB AlloProfClusteringP2P
      revision: 392ba3f5bcc8c51f578786c1fc3dae648662cb9b
      split: test
      type: lyon-nlp/alloprof
    metrics:
    - type: v_measure
      value: 70.55290063940157
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AlloProfClusteringS2S
      revision: 392ba3f5bcc8c51f578786c1fc3dae648662cb9b
      split: test
      type: lyon-nlp/alloprof
    metrics:
    - type: v_measure
      value: 55.41500719337263
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AlloprofReranking
      revision: 666fdacebe0291776e86f29345663dfaf80a0db9
      split: test
      type: lyon-nlp/mteb-fr-reranking-alloprof-s2p
    metrics:
    - type: map
      value: 73.48697375332002
    - type: mrr
      value: 75.01836585523822
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB AlloprofRetrieval
      revision: 392ba3f5bcc8c51f578786c1fc3dae648662cb9b
      split: test
      type: lyon-nlp/alloprof
    metrics:
    - type: map_at_1
      value: 38.454
    - type: map_at_10
      value: 51.605000000000004
    - type: map_at_100
      value: 52.653000000000006
    - type: map_at_1000
      value: 52.697
    - type: map_at_3
      value: 48.304
    - type: map_at_5
      value: 50.073
    - type: mrr_at_1
      value: 43.307
    - type: mrr_at_10
      value: 54.400000000000006
    - type: mrr_at_100
      value: 55.147999999999996
    - type: mrr_at_1000
      value: 55.174
    - type: mrr_at_3
      value: 51.77
    - type: mrr_at_5
      value: 53.166999999999994
    - type: ndcg_at_1
      value: 43.307
    - type: ndcg_at_10
      value: 57.891000000000005
    - type: ndcg_at_100
      value: 62.161
    - type: ndcg_at_1000
      value: 63.083
    - type: ndcg_at_3
      value: 51.851
    - type: ndcg_at_5
      value: 54.605000000000004
    - type: precision_at_1
      value: 43.307
    - type: precision_at_10
      value: 9.033
    - type: precision_at_100
      value: 1.172
    - type: precision_at_1000
      value: 0.127
    - type: precision_at_3
      value: 22.798
    - type: precision_at_5
      value: 15.492
    - type: recall_at_1
      value: 38.454
    - type: recall_at_10
      value: 74.166
    - type: recall_at_100
      value: 92.43599999999999
    - type: recall_at_1000
      value: 99.071
    - type: recall_at_3
      value: 58.087
    - type: recall_at_5
      value: 64.568
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB AmazonReviewsClassification (fr)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 53.474
    - type: f1
      value: 50.38275392350236
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BSARDRetrieval
      revision: 5effa1b9b5fa3b0f9e12523e6e43e5f86a6e6d59
      split: test
      type: maastrichtlawtech/bsard
    metrics:
    - type: map_at_1
      value: 2.252
    - type: map_at_10
      value: 4.661
    - type: map_at_100
      value: 5.271
    - type: map_at_1000
      value: 5.3629999999999995
    - type: map_at_3
      value: 3.604
    - type: map_at_5
      value: 4.3020000000000005
    - type: mrr_at_1
      value: 2.252
    - type: mrr_at_10
      value: 4.661
    - type: mrr_at_100
      value: 5.271
    - type: mrr_at_1000
      value: 5.3629999999999995
    - type: mrr_at_3
      value: 3.604
    - type: mrr_at_5
      value: 4.3020000000000005
    - type: ndcg_at_1
      value: 2.252
    - type: ndcg_at_10
      value: 6.3020000000000005
    - type: ndcg_at_100
      value: 10.342
    - type: ndcg_at_1000
      value: 13.475999999999999
    - type: ndcg_at_3
      value: 4.0649999999999995
    - type: ndcg_at_5
      value: 5.344
    - type: precision_at_1
      value: 2.252
    - type: precision_at_10
      value: 1.171
    - type: precision_at_100
      value: 0.333
    - type: precision_at_1000
      value: 0.059000000000000004
    - type: precision_at_3
      value: 1.802
    - type: precision_at_5
      value: 1.712
    - type: recall_at_1
      value: 2.252
    - type: recall_at_10
      value: 11.712
    - type: recall_at_100
      value: 33.333
    - type: recall_at_1000
      value: 59.458999999999996
    - type: recall_at_3
      value: 5.405
    - type: recall_at_5
      value: 8.559
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HALClusteringS2S
      revision: e06ebbbb123f8144bef1a5d18796f3dec9ae2915
      split: test
      type: lyon-nlp/clustering-hal-s2s
    metrics:
    - type: v_measure
      value: 28.301882091023288
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MLSUMClusteringP2P
      revision: b5d54f8f3b61ae17845046286940f03c6bc79bc7
      split: test
      type: mlsum
    metrics:
    - type: v_measure
      value: 45.26992995191701
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MLSUMClusteringS2S
      revision: b5d54f8f3b61ae17845046286940f03c6bc79bc7
      split: test
      type: mlsum
    metrics:
    - type: v_measure
      value: 42.773174876871145
    task:
      type: Clustering
  - dataset:
      config: fr
      name: MTEB MTOPDomainClassification (fr)
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: test
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 93.47635452552458
    - type: f1
      value: 93.19922617577213
    task:
      type: Classification
  - dataset:
      config: fr
      name: MTEB MTOPIntentClassification (fr)
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: test
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 80.2317569683683
    - type: f1
      value: 56.18060418621901
    task:
      type: Classification
  - dataset:
      config: fra
      name: MTEB MasakhaNEWSClassification (fra)
      revision: 8ccc72e69e65f40c70e117d8b3c08306bb788b60
      split: test
      type: masakhane/masakhanews
    metrics:
    - type: accuracy
      value: 85.18957345971565
    - type: f1
      value: 80.829981537394
    task:
      type: Classification
  - dataset:
      config: fra
      name: MTEB MasakhaNEWSClusteringP2P (fra)
      revision: 8ccc72e69e65f40c70e117d8b3c08306bb788b60
      split: test
      type: masakhane/masakhanews
    metrics:
    - type: v_measure
      value: 71.04138999801822
    task:
      type: Clustering
  - dataset:
      config: fra
      name: MTEB MasakhaNEWSClusteringS2S (fra)
      revision: 8ccc72e69e65f40c70e117d8b3c08306bb788b60
      split: test
      type: masakhane/masakhanews
    metrics:
    - type: v_measure
      value: 71.7056263158008
    task:
      type: Clustering
  - dataset:
      config: fr
      name: MTEB MassiveIntentClassification (fr)
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 76.65097511768661
    - type: f1
      value: 73.82441070598712
    task:
      type: Classification
  - dataset:
      config: fr
      name: MTEB MassiveScenarioClassification (fr)
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 79.09885675857431
    - type: f1
      value: 78.28407777434224
    task:
      type: Classification
  - dataset:
      config: fr
      name: MTEB MintakaRetrieval (fr)
      revision: efa78cc2f74bbcd21eff2261f9e13aebe40b814e
      split: test
      type: jinaai/mintakaqa
    metrics:
    - type: map_at_1
      value: 25.307000000000002
    - type: map_at_10
      value: 36.723
    - type: map_at_100
      value: 37.713
    - type: map_at_1000
      value: 37.769000000000005
    - type: map_at_3
      value: 33.77
    - type: map_at_5
      value: 35.463
    - type: mrr_at_1
      value: 25.307000000000002
    - type: mrr_at_10
      value: 36.723
    - type: mrr_at_100
      value: 37.713
    - type: mrr_at_1000
      value: 37.769000000000005
    - type: mrr_at_3
      value: 33.77
    - type: mrr_at_5
      value: 35.463
    - type: ndcg_at_1
      value: 25.307000000000002
    - type: ndcg_at_10
      value: 42.559999999999995
    - type: ndcg_at_100
      value: 47.457
    - type: ndcg_at_1000
      value: 49.162
    - type: ndcg_at_3
      value: 36.461
    - type: ndcg_at_5
      value: 39.504
    - type: precision_at_1
      value: 25.307000000000002
    - type: precision_at_10
      value: 6.106
    - type: precision_at_100
      value: 0.8420000000000001
    - type: precision_at_1000
      value: 0.098
    - type: precision_at_3
      value: 14.741999999999999
    - type: precision_at_5
      value: 10.319
    - type: recall_at_1
      value: 25.307000000000002
    - type: recall_at_10
      value: 61.056999999999995
    - type: recall_at_100
      value: 84.152
    - type: recall_at_1000
      value: 98.03399999999999
    - type: recall_at_3
      value: 44.226
    - type: recall_at_5
      value: 51.597
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB OpusparcusPC (fr)
      revision: 9e9b1f8ef51616073f47f306f7f47dd91663f86a
      split: test
      type: GEM/opusparcus
    metrics:
    - type: cos_sim_accuracy
      value: 99.90069513406156
    - type: cos_sim_ap
      value: 100.0
    - type: cos_sim_f1
      value: 99.95032290114257
    - type: cos_sim_precision
      value: 100.0
    - type: cos_sim_recall
      value: 99.90069513406156
    - type: dot_accuracy
      value: 99.90069513406156
    - type: dot_ap
      value: 100.0
    - type: dot_f1
      value: 99.95032290114257
    - type: dot_precision
      value: 100.0
    - type: dot_recall
      value: 99.90069513406156
    - type: euclidean_accuracy
      value: 99.90069513406156
    - type: euclidean_ap
      value: 100.0
    - type: euclidean_f1
      value: 99.95032290114257
    - type: euclidean_precision
      value: 100.0
    - type: euclidean_recall
      value: 99.90069513406156
    - type: manhattan_accuracy
      value: 99.90069513406156
    - type: manhattan_ap
      value: 100.0
    - type: manhattan_f1
      value: 99.95032290114257
    - type: manhattan_precision
      value: 100.0
    - type: manhattan_recall
      value: 99.90069513406156
    - type: max_accuracy
      value: 99.90069513406156
    - type: max_ap
      value: 100.0
    - type: max_f1
      value: 99.95032290114257
    task:
      type: PairClassification
  - dataset:
      config: fr
      name: MTEB PawsX (fr)
      revision: 8a04d940a42cd40658986fdd8e3da561533a3646
      split: test
      type: paws-x
    metrics:
    - type: cos_sim_accuracy
      value: 70.8
    - type: cos_sim_ap
      value: 73.7671529695957
    - type: cos_sim_f1
      value: 68.80964339527875
    - type: cos_sim_precision
      value: 62.95955882352941
    - type: cos_sim_recall
      value: 75.85825027685493
    - type: dot_accuracy
      value: 70.8
    - type: dot_ap
      value: 73.78345265366947
    - type: dot_f1
      value: 68.80964339527875
    - type: dot_precision
      value: 62.95955882352941
    - type: dot_recall
      value: 75.85825027685493
    - type: euclidean_accuracy
      value: 70.8
    - type: euclidean_ap
      value: 73.7671529695957
    - type: euclidean_f1
      value: 68.80964339527875
    - type: euclidean_precision
      value: 62.95955882352941
    - type: euclidean_recall
      value: 75.85825027685493
    - type: manhattan_accuracy
      value: 70.75
    - type: manhattan_ap
      value: 73.78996383615953
    - type: manhattan_f1
      value: 68.79432624113475
    - type: manhattan_precision
      value: 63.39869281045751
    - type: manhattan_recall
      value: 75.1937984496124
    - type: max_accuracy
      value: 70.8
    - type: max_ap
      value: 73.78996383615953
    - type: max_f1
      value: 68.80964339527875
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB SICKFr
      revision: e077ab4cf4774a1e36d86d593b150422fafd8e8a
      split: test
      type: Lajavaness/SICK-fr
    metrics:
    - type: cos_sim_pearson
      value: 84.03253762760392
    - type: cos_sim_spearman
      value: 79.68280105762004
    - type: euclidean_pearson
      value: 80.98265050044444
    - type: euclidean_spearman
      value: 79.68233242682867
    - type: manhattan_pearson
      value: 80.9678911810704
    - type: manhattan_spearman
      value: 79.70264097683109
    task:
      type: STS
  - dataset:
      config: fr
      name: MTEB STS22 (fr)
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cos_sim_pearson
      value: 80.56896987572884
    - type: cos_sim_spearman
      value: 81.84352499523287
    - type: euclidean_pearson
      value: 80.40831759421305
    - type: euclidean_spearman
      value: 81.84352499523287
    - type: manhattan_pearson
      value: 80.74333857561238
    - type: manhattan_spearman
      value: 82.41503246733892
    task:
      type: STS
  - dataset:
      config: fr
      name: MTEB STSBenchmarkMultilingualSTS (fr)
      revision: 93d57ef91790589e3ce9c365164337a8a78b7632
      split: test
      type: stsb_multi_mt
    metrics:
    - type: cos_sim_pearson
      value: 82.71826762276979
    - type: cos_sim_spearman
      value: 82.25433354916042
    - type: euclidean_pearson
      value: 81.87115571724316
    - type: euclidean_spearman
      value: 82.25322342890107
    - type: manhattan_pearson
      value: 82.11174867527224
    - type: manhattan_spearman
      value: 82.55905365203084
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SummEvalFr
      revision: b385812de6a9577b6f4d0f88c6a6e35395a94054
      split: test
      type: lyon-nlp/summarization-summeval-fr-p2p
    metrics:
    - type: cos_sim_pearson
      value: 30.659441623392887
    - type: cos_sim_spearman
      value: 30.501134097353315
    - type: dot_pearson
      value: 30.659444768851056
    - type: dot_spearman
      value: 30.501134097353315
    task:
      type: Summarization
  - dataset:
      config: default
      name: MTEB SyntecReranking
      revision: b205c5084a0934ce8af14338bf03feb19499c84d
      split: test
      type: lyon-nlp/mteb-fr-reranking-syntec-s2p
    metrics:
    - type: map
      value: 94.03333333333333
    - type: mrr
      value: 94.03333333333333
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SyntecRetrieval
      revision: 77f7e271bf4a92b24fce5119f3486b583ca016ff
      split: test
      type: lyon-nlp/mteb-fr-retrieval-syntec-s2p
    metrics:
    - type: map_at_1
      value: 79.0
    - type: map_at_10
      value: 87.61
    - type: map_at_100
      value: 87.655
    - type: map_at_1000
      value: 87.655
    - type: map_at_3
      value: 87.167
    - type: map_at_5
      value: 87.36699999999999
    - type: mrr_at_1
      value: 79.0
    - type: mrr_at_10
      value: 87.61
    - type: mrr_at_100
      value: 87.655
    - type: mrr_at_1000
      value: 87.655
    - type: mrr_at_3
      value: 87.167
    - type: mrr_at_5
      value: 87.36699999999999
    - type: ndcg_at_1
      value: 79.0
    - type: ndcg_at_10
      value: 90.473
    - type: ndcg_at_100
      value: 90.694
    - type: ndcg_at_1000
      value: 90.694
    - type: ndcg_at_3
      value: 89.464
    - type: ndcg_at_5
      value: 89.851
    - type: precision_at_1
      value: 79.0
    - type: precision_at_10
      value: 9.9
    - type: precision_at_100
      value: 1.0
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 32.0
    - type: precision_at_5
      value: 19.400000000000002
    - type: recall_at_1
      value: 79.0
    - type: recall_at_10
      value: 99.0
    - type: recall_at_100
      value: 100.0
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 96.0
    - type: recall_at_5
      value: 97.0
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB XPQARetrieval (fr)
      revision: c99d599f0a6ab9b85b065da6f9d94f9cf731679f
      split: test
      type: jinaai/xpqa
    metrics:
    - type: map_at_1
      value: 39.395
    - type: map_at_10
      value: 59.123999999999995
    - type: map_at_100
      value: 60.704
    - type: map_at_1000
      value: 60.760000000000005
    - type: map_at_3
      value: 53.187
    - type: map_at_5
      value: 56.863
    - type: mrr_at_1
      value: 62.083
    - type: mrr_at_10
      value: 68.87299999999999
    - type: mrr_at_100
      value: 69.46900000000001
    - type: mrr_at_1000
      value: 69.48299999999999
    - type: mrr_at_3
      value: 66.8
    - type: mrr_at_5
      value: 67.928
    - type: ndcg_at_1
      value: 62.083
    - type: ndcg_at_10
      value: 65.583
    - type: ndcg_at_100
      value: 70.918
    - type: ndcg_at_1000
      value: 71.72800000000001
    - type: ndcg_at_3
      value: 60.428000000000004
    - type: ndcg_at_5
      value: 61.853
    - type: precision_at_1
      value: 62.083
    - type: precision_at_10
      value: 15.033
    - type: precision_at_100
      value: 1.9529999999999998
    - type: precision_at_1000
      value: 0.207
    - type: precision_at_3
      value: 36.315
    - type: precision_at_5
      value: 25.955000000000002
    - type: recall_at_1
      value: 39.395
    - type: recall_at_10
      value: 74.332
    - type: recall_at_100
      value: 94.729
    - type: recall_at_1000
      value: 99.75500000000001
    - type: recall_at_3
      value: 57.679
    - type: recall_at_5
      value: 65.036
    task:
      type: Retrieval
---

## gte-Qwen2-1.5B-instruct

**gte-Qwen2-1.5B-instruct** is the latest model in the gte (General Text Embedding) model family. The model is built on [Qwen2-1.5B](https://huggingface.co/Qwen/Qwen2-1.5B) LLM model and use the same training data and strategies as the [gte-Qwen2-7B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct) model. 

The model incorporates several key advancements:

- Integration of bidirectional attention mechanisms, enriching its contextual understanding.
- Instruction tuning, applied solely on the query side for streamlined efficiency
- Comprehensive training across a vast, multilingual text corpus spanning diverse domains and scenarios. This training leverages both weakly supervised and supervised data, ensuring the model's applicability across numerous languages and a wide array of downstream tasks.


## Model Information
- Model Size: 1.5B 
- Embedding Dimension: 1536
- Max Input Tokens: 32k

## Requirements
```
transformers>=4.39.2
flash_attn>=2.5.6
```
## Usage 

### Sentence Transformers

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Alibaba-NLP/gte-Qwen2-1.5B-instruct", trust_remote_code=True)
# In case you want to reduce the maximum length:
model.max_seq_length = 8192

queries = [
    "how much protein should a female eat",
    "summit define",
]
documents = [
    "As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 is 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or training for a marathon. Check out the chart below to see how much protein you should be eating each day.",
    "Definition of summit for English Language Learners. : 1  the highest point of a mountain : the top of a mountain. : 2  the highest level. : 3  a meeting or series of meetings between the leaders of two or more governments.",
]

query_embeddings = model.encode(queries, prompt_name="query")
document_embeddings = model.encode(documents)

scores = (query_embeddings @ document_embeddings.T) * 100
print(scores.tolist())
```

Observe the [config_sentence_transformers.json](config_sentence_transformers.json) to see all pre-built prompt names. Otherwise, you can use `model.encode(queries, prompt="Instruct: ...\nQuery: "` to use a custom prompt of your choice.

### Transformers

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
    get_detailed_instruct(task, 'how much protein should a female eat'),
    get_detailed_instruct(task, 'summit define')
]
# No need to add instruction for retrieval documents
documents = [
    "As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 is 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or training for a marathon. Check out the chart below to see how much protein you should be eating each day.",
    "Definition of summit for English Language Learners. : 1  the highest point of a mountain : the top of a mountain. : 2  the highest level. : 3  a meeting or series of meetings between the leaders of two or more governments."
]
input_texts = queries + documents

tokenizer = AutoTokenizer.from_pretrained('Alibaba-NLP/gte-Qwen2-1.5B-instruct', trust_remote_code=True)
model = AutoModel.from_pretrained('Alibaba-NLP/gte-Qwen2-1.5B-instruct', trust_remote_code=True)

max_length = 8192

# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=max_length, padding=True, truncation=True, return_tensors='pt')
outputs = model(**batch_dict)
embeddings = last_token_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

# normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:2] @ embeddings[2:].T) * 100
print(scores.tolist())
```

## Evaluation

### MTEB & C-MTEB

You can use the [scripts/eval_mteb.py](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct/blob/main/scripts/eval_mteb.py) to reproduce the following result of **gte-Qwen2-1.5B-instruct** on MTEB(English)/C-MTEB(Chinese):

| Model Name | MTEB(56)  | C-MTEB(35) | MTEB-fr(26) | MTEB-pl(26) | 
|:----:|:---------:|:----------:|:----------:|:----------:|
| [bge-base-en-1.5](https://huggingface.co/BAAI/bge-base-en-v1.5) |   64.23   |     -      |  - | - |
| [bge-large-en-1.5](https://huggingface.co/BAAI/bge-large-en-v1.5) |   63.55   |     -      | - | - |
| [gte-large-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5) |   65.39   |     -      |  - | - |
| [gte-base-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5) |   64.11   |     -      |  - | - |
| [mxbai-embed-large-v1](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1) |   64.68   |     -      |  - | - |
| [acge_text_embedding](https://huggingface.co/aspire/acge_text_embedding) |     -     |   69.07    |   - | - |
| [stella-mrl-large-zh-v3.5-1792d](https://huggingface.co/infgrad/stella-mrl-large-zh-v3.5-1792d) |     -     |   68.55    |  - | - |
| [gte-large-zh](https://huggingface.co/thenlper/gte-large-zh) |     -     |   66.72    |  - | - |
| [multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base) |   59.45   |   56.21    |   - | - |
| [multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large) |   61.50   |   58.81    |   - | - |
| [e5-mistral-7b-instruct](https://huggingface.co/intfloat/e5-mistral-7b-instruct) |   66.63   |   60.81    |   - | - |
| [gte-Qwen1.5-7B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen1.5-7B-instruct) |   67.34   |   69.52    |  - | - |
| [NV-Embed-v1](https://huggingface.co/nvidia/NV-Embed-v1) |   69.32   |     -      |  - | - |
| [**gte-Qwen2-7B-instruct**](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct) | **70.24** | **72.05**  | **68.25**   | **67.86** |
| [**gte-Qwen2-1.5B-instruct**](https://huggingface.co/Alibaba-NLP/gte-Qwen2-1.5B-instruct) | **67.16** | **67.65**  | **66.60** | **64.04** |

### GTE Models

The gte series models have consistently released two types of models: encoder-only models (based on the BERT architecture) and decode-only models (based on the LLM architecture). 

|                                        Models                                         | Language | Max Sequence Length | Dimension | Model Size (Memory Usage, fp32) |
|:-------------------------------------------------------------------------------------:|:--------:|:-----: |:---------:|:-------------------------------:|
|             [GTE-large-zh](https://huggingface.co/thenlper/gte-large-zh)              | Chinese  | 512 |   1024    |             1.25GB              |
|              [GTE-base-zh](https://huggingface.co/thenlper/gte-base-zh)               | Chinese  | 512 |    512    |             0.41GB              |
|             [GTE-small-zh](https://huggingface.co/thenlper/gte-small-zh)              | Chinese  | 512 |    512    |             0.12GB              |
|                [GTE-large](https://huggingface.co/thenlper/gte-large)                 | English  | 512 |   1024    |             1.25GB              |
|                 [GTE-base](https://huggingface.co/thenlper/gte-base)                  | English  | 512 |    512    |             0.21GB              |
|                [GTE-small](https://huggingface.co/thenlper/gte-small)                 | English  | 512 |    384    |             0.10GB              |
|       [GTE-large-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5)       | English | 8192 |   1024    |             1.74GB              |
|        [GTE-base-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-base-en-v1.5)        | English | 8192 |    768    |             0.51GB              |
| [GTE-Qwen1.5-7B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen1.5-7B-instruct) | Multilingual | 32000 | 4096 | 26.45GB |
|   [GTE-Qwen2-7B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct)   | Multilingual | 32000 | 3584 | 26.45GB |
|   [GTE-Qwen2-1.5B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-1.5B-instruct)   | Multilingual | 32000 | 1536 | 6.62GB |


## Cloud API Services

In addition to the open-source [GTE](https://huggingface.co/collections/Alibaba-NLP/gte-models-6680f0b13f885cb431e6d469) series models, GTE series models are also available as commercial API services on Alibaba Cloud.

- [Embedding Models](https://help.aliyun.com/zh/model-studio/developer-reference/general-text-embedding/): Rhree versions of the text embedding models are available: text-embedding-v1/v2/v3, with v3 being the latest API service.
- [ReRank Models](https://help.aliyun.com/zh/model-studio/developer-reference/general-text-sorting-model/): The gte-rerank model service is available.

Note that the models behind the commercial APIs are not entirely identical to the open-source models.

## Citation

If you find our paper or models helpful, please consider cite:

```
@article{li2023towards,
  title={Towards general text embeddings with multi-stage contrastive learning},
  author={Li, Zehan and Zhang, Xin and Zhang, Yanzhao and Long, Dingkun and Xie, Pengjun and Zhang, Meishan},
  journal={arXiv preprint arXiv:2308.03281},
  year={2023}
}
```
