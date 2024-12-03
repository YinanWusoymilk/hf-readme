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
      value: 91.31343283582089
    - type: ap
      value: 67.64251402604096
    - type: f1
      value: 87.53372530755692
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
      value: 97.497825
    - type: ap
      value: 96.30329547047529
    - type: f1
      value: 97.49769793778039
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
      value: 62.564
    - type: f1
      value: 60.975777935041066
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
      value: 36.486000000000004
    - type: map_at_10
      value: 54.842
    - type: map_at_100
      value: 55.206999999999994
    - type: map_at_1000
      value: 55.206999999999994
    - type: map_at_3
      value: 49.893
    - type: map_at_5
      value: 53.105000000000004
    - type: mrr_at_1
      value: 37.34
    - type: mrr_at_10
      value: 55.143
    - type: mrr_at_100
      value: 55.509
    - type: mrr_at_1000
      value: 55.509
    - type: mrr_at_3
      value: 50.212999999999994
    - type: mrr_at_5
      value: 53.432
    - type: ndcg_at_1
      value: 36.486000000000004
    - type: ndcg_at_10
      value: 64.273
    - type: ndcg_at_100
      value: 65.66199999999999
    - type: ndcg_at_1000
      value: 65.66199999999999
    - type: ndcg_at_3
      value: 54.352999999999994
    - type: ndcg_at_5
      value: 60.131
    - type: precision_at_1
      value: 36.486000000000004
    - type: precision_at_10
      value: 9.395000000000001
    - type: precision_at_100
      value: 0.996
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 22.428
    - type: precision_at_5
      value: 16.259
    - type: recall_at_1
      value: 36.486000000000004
    - type: recall_at_10
      value: 93.95400000000001
    - type: recall_at_100
      value: 99.644
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 67.283
    - type: recall_at_5
      value: 81.294
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
      value: 56.461169803700564
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
      value: 51.73600434466286
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
      value: 67.57827065898053
    - type: mrr
      value: 79.08136569493911
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
      value: 83.53324575999243
    - type: cos_sim_spearman
      value: 81.37173362822374
    - type: euclidean_pearson
      value: 82.19243335103444
    - type: euclidean_spearman
      value: 81.33679307304334
    - type: manhattan_pearson
      value: 82.38752665975699
    - type: manhattan_spearman
      value: 81.31510583189689
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
      value: 87.56818181818181
    - type: f1
      value: 87.25826722019875
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
      value: 50.09239610327673
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
      value: 46.64733054606282
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: f46a197baaae43b4f621051089b82a364682dfeb
    metrics:
    - type: map_at_1
      value: 33.997
    - type: map_at_10
      value: 48.176
    - type: map_at_100
      value: 49.82
    - type: map_at_1000
      value: 49.924
    - type: map_at_3
      value: 43.626
    - type: map_at_5
      value: 46.275
    - type: mrr_at_1
      value: 42.059999999999995
    - type: mrr_at_10
      value: 53.726
    - type: mrr_at_100
      value: 54.398
    - type: mrr_at_1000
      value: 54.416
    - type: mrr_at_3
      value: 50.714999999999996
    - type: mrr_at_5
      value: 52.639
    - type: ndcg_at_1
      value: 42.059999999999995
    - type: ndcg_at_10
      value: 55.574999999999996
    - type: ndcg_at_100
      value: 60.744
    - type: ndcg_at_1000
      value: 61.85699999999999
    - type: ndcg_at_3
      value: 49.363
    - type: ndcg_at_5
      value: 52.44
    - type: precision_at_1
      value: 42.059999999999995
    - type: precision_at_10
      value: 11.101999999999999
    - type: precision_at_100
      value: 1.73
    - type: precision_at_1000
      value: 0.218
    - type: precision_at_3
      value: 24.464
    - type: precision_at_5
      value: 18.026
    - type: recall_at_1
      value: 33.997
    - type: recall_at_10
      value: 70.35900000000001
    - type: recall_at_100
      value: 91.642
    - type: recall_at_1000
      value: 97.977
    - type: recall_at_3
      value: 52.76
    - type: recall_at_5
      value: 61.148
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
    metrics:
    - type: map_at_1
      value: 35.884
    - type: map_at_10
      value: 48.14
    - type: map_at_100
      value: 49.5
    - type: map_at_1000
      value: 49.63
    - type: map_at_3
      value: 44.646
    - type: map_at_5
      value: 46.617999999999995
    - type: mrr_at_1
      value: 44.458999999999996
    - type: mrr_at_10
      value: 53.751000000000005
    - type: mrr_at_100
      value: 54.37800000000001
    - type: mrr_at_1000
      value: 54.415
    - type: mrr_at_3
      value: 51.815
    - type: mrr_at_5
      value: 52.882
    - type: ndcg_at_1
      value: 44.458999999999996
    - type: ndcg_at_10
      value: 54.157
    - type: ndcg_at_100
      value: 58.362
    - type: ndcg_at_1000
      value: 60.178
    - type: ndcg_at_3
      value: 49.661
    - type: ndcg_at_5
      value: 51.74999999999999
    - type: precision_at_1
      value: 44.458999999999996
    - type: precision_at_10
      value: 10.248
    - type: precision_at_100
      value: 1.5890000000000002
    - type: precision_at_1000
      value: 0.207
    - type: precision_at_3
      value: 23.928
    - type: precision_at_5
      value: 16.878999999999998
    - type: recall_at_1
      value: 35.884
    - type: recall_at_10
      value: 64.798
    - type: recall_at_100
      value: 82.345
    - type: recall_at_1000
      value: 93.267
    - type: recall_at_3
      value: 51.847
    - type: recall_at_5
      value: 57.601
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
    metrics:
    - type: map_at_1
      value: 39.383
    - type: map_at_10
      value: 53.714
    - type: map_at_100
      value: 54.838
    - type: map_at_1000
      value: 54.87800000000001
    - type: map_at_3
      value: 50.114999999999995
    - type: map_at_5
      value: 52.153000000000006
    - type: mrr_at_1
      value: 45.016
    - type: mrr_at_10
      value: 56.732000000000006
    - type: mrr_at_100
      value: 57.411
    - type: mrr_at_1000
      value: 57.431
    - type: mrr_at_3
      value: 54.044000000000004
    - type: mrr_at_5
      value: 55.639
    - type: ndcg_at_1
      value: 45.016
    - type: ndcg_at_10
      value: 60.228
    - type: ndcg_at_100
      value: 64.277
    - type: ndcg_at_1000
      value: 65.07
    - type: ndcg_at_3
      value: 54.124
    - type: ndcg_at_5
      value: 57.147000000000006
    - type: precision_at_1
      value: 45.016
    - type: precision_at_10
      value: 9.937
    - type: precision_at_100
      value: 1.288
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: precision_at_3
      value: 24.471999999999998
    - type: precision_at_5
      value: 16.991
    - type: recall_at_1
      value: 39.383
    - type: recall_at_10
      value: 76.175
    - type: recall_at_100
      value: 93.02
    - type: recall_at_1000
      value: 98.60900000000001
    - type: recall_at_3
      value: 60.265
    - type: recall_at_5
      value: 67.46600000000001
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: 5003b3064772da1887988e05400cf3806fe491f2
    metrics:
    - type: map_at_1
      value: 27.426000000000002
    - type: map_at_10
      value: 37.397000000000006
    - type: map_at_100
      value: 38.61
    - type: map_at_1000
      value: 38.678000000000004
    - type: map_at_3
      value: 34.150999999999996
    - type: map_at_5
      value: 36.137
    - type: mrr_at_1
      value: 29.944
    - type: mrr_at_10
      value: 39.654
    - type: mrr_at_100
      value: 40.638000000000005
    - type: mrr_at_1000
      value: 40.691
    - type: mrr_at_3
      value: 36.817
    - type: mrr_at_5
      value: 38.524
    - type: ndcg_at_1
      value: 29.944
    - type: ndcg_at_10
      value: 43.094
    - type: ndcg_at_100
      value: 48.789
    - type: ndcg_at_1000
      value: 50.339999999999996
    - type: ndcg_at_3
      value: 36.984
    - type: ndcg_at_5
      value: 40.248
    - type: precision_at_1
      value: 29.944
    - type: precision_at_10
      value: 6.78
    - type: precision_at_100
      value: 1.024
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: precision_at_3
      value: 15.895000000000001
    - type: precision_at_5
      value: 11.39
    - type: recall_at_1
      value: 27.426000000000002
    - type: recall_at_10
      value: 58.464000000000006
    - type: recall_at_100
      value: 84.193
    - type: recall_at_1000
      value: 95.52000000000001
    - type: recall_at_3
      value: 42.172
    - type: recall_at_5
      value: 50.101
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
    metrics:
    - type: map_at_1
      value: 19.721
    - type: map_at_10
      value: 31.604
    - type: map_at_100
      value: 32.972
    - type: map_at_1000
      value: 33.077
    - type: map_at_3
      value: 27.218999999999998
    - type: map_at_5
      value: 29.53
    - type: mrr_at_1
      value: 25.0
    - type: mrr_at_10
      value: 35.843
    - type: mrr_at_100
      value: 36.785000000000004
    - type: mrr_at_1000
      value: 36.842000000000006
    - type: mrr_at_3
      value: 32.193
    - type: mrr_at_5
      value: 34.264
    - type: ndcg_at_1
      value: 25.0
    - type: ndcg_at_10
      value: 38.606
    - type: ndcg_at_100
      value: 44.272
    - type: ndcg_at_1000
      value: 46.527
    - type: ndcg_at_3
      value: 30.985000000000003
    - type: ndcg_at_5
      value: 34.43
    - type: precision_at_1
      value: 25.0
    - type: precision_at_10
      value: 7.811
    - type: precision_at_100
      value: 1.203
    - type: precision_at_1000
      value: 0.15
    - type: precision_at_3
      value: 15.423
    - type: precision_at_5
      value: 11.791
    - type: recall_at_1
      value: 19.721
    - type: recall_at_10
      value: 55.625
    - type: recall_at_100
      value: 79.34400000000001
    - type: recall_at_1000
      value: 95.208
    - type: recall_at_3
      value: 35.19
    - type: recall_at_5
      value: 43.626
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
    metrics:
    - type: map_at_1
      value: 33.784
    - type: map_at_10
      value: 47.522
    - type: map_at_100
      value: 48.949999999999996
    - type: map_at_1000
      value: 49.038
    - type: map_at_3
      value: 43.284
    - type: map_at_5
      value: 45.629
    - type: mrr_at_1
      value: 41.482
    - type: mrr_at_10
      value: 52.830999999999996
    - type: mrr_at_100
      value: 53.559999999999995
    - type: mrr_at_1000
      value: 53.588
    - type: mrr_at_3
      value: 50.016000000000005
    - type: mrr_at_5
      value: 51.614000000000004
    - type: ndcg_at_1
      value: 41.482
    - type: ndcg_at_10
      value: 54.569
    - type: ndcg_at_100
      value: 59.675999999999995
    - type: ndcg_at_1000
      value: 60.989000000000004
    - type: ndcg_at_3
      value: 48.187000000000005
    - type: ndcg_at_5
      value: 51.183
    - type: precision_at_1
      value: 41.482
    - type: precision_at_10
      value: 10.221
    - type: precision_at_100
      value: 1.486
    - type: precision_at_1000
      value: 0.17500000000000002
    - type: precision_at_3
      value: 23.548
    - type: precision_at_5
      value: 16.805
    - type: recall_at_1
      value: 33.784
    - type: recall_at_10
      value: 69.798
    - type: recall_at_100
      value: 90.098
    - type: recall_at_1000
      value: 98.176
    - type: recall_at_3
      value: 52.127
    - type: recall_at_5
      value: 59.861
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
    metrics:
    - type: map_at_1
      value: 28.038999999999998
    - type: map_at_10
      value: 41.904
    - type: map_at_100
      value: 43.36
    - type: map_at_1000
      value: 43.453
    - type: map_at_3
      value: 37.785999999999994
    - type: map_at_5
      value: 40.105000000000004
    - type: mrr_at_1
      value: 35.046
    - type: mrr_at_10
      value: 46.926
    - type: mrr_at_100
      value: 47.815000000000005
    - type: mrr_at_1000
      value: 47.849000000000004
    - type: mrr_at_3
      value: 44.273
    - type: mrr_at_5
      value: 45.774
    - type: ndcg_at_1
      value: 35.046
    - type: ndcg_at_10
      value: 48.937000000000005
    - type: ndcg_at_100
      value: 54.544000000000004
    - type: ndcg_at_1000
      value: 56.069
    - type: ndcg_at_3
      value: 42.858000000000004
    - type: ndcg_at_5
      value: 45.644
    - type: precision_at_1
      value: 35.046
    - type: precision_at_10
      value: 9.452
    - type: precision_at_100
      value: 1.429
    - type: precision_at_1000
      value: 0.173
    - type: precision_at_3
      value: 21.346999999999998
    - type: precision_at_5
      value: 15.342
    - type: recall_at_1
      value: 28.038999999999998
    - type: recall_at_10
      value: 64.59700000000001
    - type: recall_at_100
      value: 87.735
    - type: recall_at_1000
      value: 97.41300000000001
    - type: recall_at_3
      value: 47.368
    - type: recall_at_5
      value: 54.93900000000001
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
    metrics:
    - type: map_at_1
      value: 28.17291666666667
    - type: map_at_10
      value: 40.025749999999995
    - type: map_at_100
      value: 41.39208333333333
    - type: map_at_1000
      value: 41.499249999999996
    - type: map_at_3
      value: 36.347
    - type: map_at_5
      value: 38.41391666666667
    - type: mrr_at_1
      value: 33.65925
    - type: mrr_at_10
      value: 44.085499999999996
    - type: mrr_at_100
      value: 44.94116666666667
    - type: mrr_at_1000
      value: 44.9855
    - type: mrr_at_3
      value: 41.2815
    - type: mrr_at_5
      value: 42.91491666666666
    - type: ndcg_at_1
      value: 33.65925
    - type: ndcg_at_10
      value: 46.430833333333325
    - type: ndcg_at_100
      value: 51.761
    - type: ndcg_at_1000
      value: 53.50899999999999
    - type: ndcg_at_3
      value: 40.45133333333333
    - type: ndcg_at_5
      value: 43.31483333333334
    - type: precision_at_1
      value: 33.65925
    - type: precision_at_10
      value: 8.4995
    - type: precision_at_100
      value: 1.3210000000000004
    - type: precision_at_1000
      value: 0.16591666666666666
    - type: precision_at_3
      value: 19.165083333333335
    - type: precision_at_5
      value: 13.81816666666667
    - type: recall_at_1
      value: 28.17291666666667
    - type: recall_at_10
      value: 61.12624999999999
    - type: recall_at_100
      value: 83.97266666666667
    - type: recall_at_1000
      value: 95.66550000000001
    - type: recall_at_3
      value: 44.661249999999995
    - type: recall_at_5
      value: 51.983333333333334
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
    metrics:
    - type: map_at_1
      value: 24.681
    - type: map_at_10
      value: 34.892
    - type: map_at_100
      value: 35.996
    - type: map_at_1000
      value: 36.083
    - type: map_at_3
      value: 31.491999999999997
    - type: map_at_5
      value: 33.632
    - type: mrr_at_1
      value: 28.528
    - type: mrr_at_10
      value: 37.694
    - type: mrr_at_100
      value: 38.613
    - type: mrr_at_1000
      value: 38.668
    - type: mrr_at_3
      value: 34.714
    - type: mrr_at_5
      value: 36.616
    - type: ndcg_at_1
      value: 28.528
    - type: ndcg_at_10
      value: 40.703
    - type: ndcg_at_100
      value: 45.993
    - type: ndcg_at_1000
      value: 47.847
    - type: ndcg_at_3
      value: 34.622
    - type: ndcg_at_5
      value: 38.035999999999994
    - type: precision_at_1
      value: 28.528
    - type: precision_at_10
      value: 6.902
    - type: precision_at_100
      value: 1.0370000000000001
    - type: precision_at_1000
      value: 0.126
    - type: precision_at_3
      value: 15.798000000000002
    - type: precision_at_5
      value: 11.655999999999999
    - type: recall_at_1
      value: 24.681
    - type: recall_at_10
      value: 55.81
    - type: recall_at_100
      value: 79.785
    - type: recall_at_1000
      value: 92.959
    - type: recall_at_3
      value: 39.074
    - type: recall_at_5
      value: 47.568
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: 46989137a86843e03a6195de44b09deda022eec7
    metrics:
    - type: map_at_1
      value: 18.627
    - type: map_at_10
      value: 27.872000000000003
    - type: map_at_100
      value: 29.237999999999996
    - type: map_at_1000
      value: 29.363
    - type: map_at_3
      value: 24.751
    - type: map_at_5
      value: 26.521
    - type: mrr_at_1
      value: 23.021
    - type: mrr_at_10
      value: 31.924000000000003
    - type: mrr_at_100
      value: 32.922000000000004
    - type: mrr_at_1000
      value: 32.988
    - type: mrr_at_3
      value: 29.192
    - type: mrr_at_5
      value: 30.798
    - type: ndcg_at_1
      value: 23.021
    - type: ndcg_at_10
      value: 33.535
    - type: ndcg_at_100
      value: 39.732
    - type: ndcg_at_1000
      value: 42.201
    - type: ndcg_at_3
      value: 28.153
    - type: ndcg_at_5
      value: 30.746000000000002
    - type: precision_at_1
      value: 23.021
    - type: precision_at_10
      value: 6.459
    - type: precision_at_100
      value: 1.1320000000000001
    - type: precision_at_1000
      value: 0.153
    - type: precision_at_3
      value: 13.719000000000001
    - type: precision_at_5
      value: 10.193000000000001
    - type: recall_at_1
      value: 18.627
    - type: recall_at_10
      value: 46.463
    - type: recall_at_100
      value: 74.226
    - type: recall_at_1000
      value: 91.28500000000001
    - type: recall_at_3
      value: 31.357000000000003
    - type: recall_at_5
      value: 38.067
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
    metrics:
    - type: map_at_1
      value: 31.457
    - type: map_at_10
      value: 42.888
    - type: map_at_100
      value: 44.24
    - type: map_at_1000
      value: 44.327
    - type: map_at_3
      value: 39.588
    - type: map_at_5
      value: 41.423
    - type: mrr_at_1
      value: 37.126999999999995
    - type: mrr_at_10
      value: 47.083000000000006
    - type: mrr_at_100
      value: 47.997
    - type: mrr_at_1000
      value: 48.044
    - type: mrr_at_3
      value: 44.574000000000005
    - type: mrr_at_5
      value: 46.202
    - type: ndcg_at_1
      value: 37.126999999999995
    - type: ndcg_at_10
      value: 48.833
    - type: ndcg_at_100
      value: 54.327000000000005
    - type: ndcg_at_1000
      value: 56.011
    - type: ndcg_at_3
      value: 43.541999999999994
    - type: ndcg_at_5
      value: 46.127
    - type: precision_at_1
      value: 37.126999999999995
    - type: precision_at_10
      value: 8.376999999999999
    - type: precision_at_100
      value: 1.2309999999999999
    - type: precision_at_1000
      value: 0.146
    - type: precision_at_3
      value: 20.211000000000002
    - type: precision_at_5
      value: 14.16
    - type: recall_at_1
      value: 31.457
    - type: recall_at_10
      value: 62.369
    - type: recall_at_100
      value: 85.444
    - type: recall_at_1000
      value: 96.65599999999999
    - type: recall_at_3
      value: 47.961
    - type: recall_at_5
      value: 54.676
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
    metrics:
    - type: map_at_1
      value: 27.139999999999997
    - type: map_at_10
      value: 38.801
    - type: map_at_100
      value: 40.549
    - type: map_at_1000
      value: 40.802
    - type: map_at_3
      value: 35.05
    - type: map_at_5
      value: 36.884
    - type: mrr_at_1
      value: 33.004
    - type: mrr_at_10
      value: 43.864
    - type: mrr_at_100
      value: 44.667
    - type: mrr_at_1000
      value: 44.717
    - type: mrr_at_3
      value: 40.777
    - type: mrr_at_5
      value: 42.319
    - type: ndcg_at_1
      value: 33.004
    - type: ndcg_at_10
      value: 46.022
    - type: ndcg_at_100
      value: 51.542
    - type: ndcg_at_1000
      value: 53.742000000000004
    - type: ndcg_at_3
      value: 39.795
    - type: ndcg_at_5
      value: 42.272
    - type: precision_at_1
      value: 33.004
    - type: precision_at_10
      value: 9.012
    - type: precision_at_100
      value: 1.7770000000000001
    - type: precision_at_1000
      value: 0.26
    - type: precision_at_3
      value: 19.038
    - type: precision_at_5
      value: 13.675999999999998
    - type: recall_at_1
      value: 27.139999999999997
    - type: recall_at_10
      value: 60.961
    - type: recall_at_100
      value: 84.451
    - type: recall_at_1000
      value: 98.113
    - type: recall_at_3
      value: 43.001
    - type: recall_at_5
      value: 49.896
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
    metrics:
    - type: map_at_1
      value: 17.936
    - type: map_at_10
      value: 27.399
    - type: map_at_100
      value: 28.632
    - type: map_at_1000
      value: 28.738000000000003
    - type: map_at_3
      value: 24.456
    - type: map_at_5
      value: 26.06
    - type: mrr_at_1
      value: 19.224
    - type: mrr_at_10
      value: 28.998
    - type: mrr_at_100
      value: 30.11
    - type: mrr_at_1000
      value: 30.177
    - type: mrr_at_3
      value: 26.247999999999998
    - type: mrr_at_5
      value: 27.708
    - type: ndcg_at_1
      value: 19.224
    - type: ndcg_at_10
      value: 32.911
    - type: ndcg_at_100
      value: 38.873999999999995
    - type: ndcg_at_1000
      value: 41.277
    - type: ndcg_at_3
      value: 27.142
    - type: ndcg_at_5
      value: 29.755
    - type: precision_at_1
      value: 19.224
    - type: precision_at_10
      value: 5.6930000000000005
    - type: precision_at_100
      value: 0.9259999999999999
    - type: precision_at_1000
      value: 0.126
    - type: precision_at_3
      value: 12.138
    - type: precision_at_5
      value: 8.909
    - type: recall_at_1
      value: 17.936
    - type: recall_at_10
      value: 48.096
    - type: recall_at_100
      value: 75.389
    - type: recall_at_1000
      value: 92.803
    - type: recall_at_3
      value: 32.812999999999995
    - type: recall_at_5
      value: 38.851
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
      value: 22.076999999999998
    - type: map_at_10
      value: 35.44
    - type: map_at_100
      value: 37.651
    - type: map_at_1000
      value: 37.824999999999996
    - type: map_at_3
      value: 30.764999999999997
    - type: map_at_5
      value: 33.26
    - type: mrr_at_1
      value: 50.163000000000004
    - type: mrr_at_10
      value: 61.207
    - type: mrr_at_100
      value: 61.675000000000004
    - type: mrr_at_1000
      value: 61.692
    - type: mrr_at_3
      value: 58.60999999999999
    - type: mrr_at_5
      value: 60.307
    - type: ndcg_at_1
      value: 50.163000000000004
    - type: ndcg_at_10
      value: 45.882
    - type: ndcg_at_100
      value: 53.239999999999995
    - type: ndcg_at_1000
      value: 55.852000000000004
    - type: ndcg_at_3
      value: 40.514
    - type: ndcg_at_5
      value: 42.038
    - type: precision_at_1
      value: 50.163000000000004
    - type: precision_at_10
      value: 13.466000000000001
    - type: precision_at_100
      value: 2.164
    - type: precision_at_1000
      value: 0.266
    - type: precision_at_3
      value: 29.707
    - type: precision_at_5
      value: 21.694
    - type: recall_at_1
      value: 22.076999999999998
    - type: recall_at_10
      value: 50.193
    - type: recall_at_100
      value: 74.993
    - type: recall_at_1000
      value: 89.131
    - type: recall_at_3
      value: 35.472
    - type: recall_at_5
      value: 41.814
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
      value: 9.953
    - type: map_at_10
      value: 24.515
    - type: map_at_100
      value: 36.173
    - type: map_at_1000
      value: 38.351
    - type: map_at_3
      value: 16.592000000000002
    - type: map_at_5
      value: 20.036
    - type: mrr_at_1
      value: 74.25
    - type: mrr_at_10
      value: 81.813
    - type: mrr_at_100
      value: 82.006
    - type: mrr_at_1000
      value: 82.011
    - type: mrr_at_3
      value: 80.875
    - type: mrr_at_5
      value: 81.362
    - type: ndcg_at_1
      value: 62.5
    - type: ndcg_at_10
      value: 52.42
    - type: ndcg_at_100
      value: 56.808
    - type: ndcg_at_1000
      value: 63.532999999999994
    - type: ndcg_at_3
      value: 56.654
    - type: ndcg_at_5
      value: 54.18300000000001
    - type: precision_at_1
      value: 74.25
    - type: precision_at_10
      value: 42.699999999999996
    - type: precision_at_100
      value: 13.675
    - type: precision_at_1000
      value: 2.664
    - type: precision_at_3
      value: 60.5
    - type: precision_at_5
      value: 52.800000000000004
    - type: recall_at_1
      value: 9.953
    - type: recall_at_10
      value: 30.253999999999998
    - type: recall_at_100
      value: 62.516000000000005
    - type: recall_at_1000
      value: 84.163
    - type: recall_at_3
      value: 18.13
    - type: recall_at_5
      value: 22.771
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
      value: 79.455
    - type: f1
      value: 74.16798697647569
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
      value: 87.531
    - type: map_at_10
      value: 93.16799999999999
    - type: map_at_100
      value: 93.341
    - type: map_at_1000
      value: 93.349
    - type: map_at_3
      value: 92.444
    - type: map_at_5
      value: 92.865
    - type: mrr_at_1
      value: 94.014
    - type: mrr_at_10
      value: 96.761
    - type: mrr_at_100
      value: 96.762
    - type: mrr_at_1000
      value: 96.762
    - type: mrr_at_3
      value: 96.672
    - type: mrr_at_5
      value: 96.736
    - type: ndcg_at_1
      value: 94.014
    - type: ndcg_at_10
      value: 95.112
    - type: ndcg_at_100
      value: 95.578
    - type: ndcg_at_1000
      value: 95.68900000000001
    - type: ndcg_at_3
      value: 94.392
    - type: ndcg_at_5
      value: 94.72500000000001
    - type: precision_at_1
      value: 94.014
    - type: precision_at_10
      value: 11.065
    - type: precision_at_100
      value: 1.157
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: precision_at_3
      value: 35.259
    - type: precision_at_5
      value: 21.599
    - type: recall_at_1
      value: 87.531
    - type: recall_at_10
      value: 97.356
    - type: recall_at_100
      value: 98.965
    - type: recall_at_1000
      value: 99.607
    - type: recall_at_3
      value: 95.312
    - type: recall_at_5
      value: 96.295
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
      value: 32.055
    - type: map_at_10
      value: 53.114
    - type: map_at_100
      value: 55.235
    - type: map_at_1000
      value: 55.345
    - type: map_at_3
      value: 45.854
    - type: map_at_5
      value: 50.025
    - type: mrr_at_1
      value: 60.34
    - type: mrr_at_10
      value: 68.804
    - type: mrr_at_100
      value: 69.309
    - type: mrr_at_1000
      value: 69.32199999999999
    - type: mrr_at_3
      value: 66.40899999999999
    - type: mrr_at_5
      value: 67.976
    - type: ndcg_at_1
      value: 60.34
    - type: ndcg_at_10
      value: 62.031000000000006
    - type: ndcg_at_100
      value: 68.00500000000001
    - type: ndcg_at_1000
      value: 69.286
    - type: ndcg_at_3
      value: 56.355999999999995
    - type: ndcg_at_5
      value: 58.687
    - type: precision_at_1
      value: 60.34
    - type: precision_at_10
      value: 17.176
    - type: precision_at_100
      value: 2.36
    - type: precision_at_1000
      value: 0.259
    - type: precision_at_3
      value: 37.14
    - type: precision_at_5
      value: 27.809
    - type: recall_at_1
      value: 32.055
    - type: recall_at_10
      value: 70.91
    - type: recall_at_100
      value: 91.83
    - type: recall_at_1000
      value: 98.871
    - type: recall_at_3
      value: 51.202999999999996
    - type: recall_at_5
      value: 60.563
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
      value: 43.68
    - type: map_at_10
      value: 64.389
    - type: map_at_100
      value: 65.24
    - type: map_at_1000
      value: 65.303
    - type: map_at_3
      value: 61.309000000000005
    - type: map_at_5
      value: 63.275999999999996
    - type: mrr_at_1
      value: 87.36
    - type: mrr_at_10
      value: 91.12
    - type: mrr_at_100
      value: 91.227
    - type: mrr_at_1000
      value: 91.229
    - type: mrr_at_3
      value: 90.57600000000001
    - type: mrr_at_5
      value: 90.912
    - type: ndcg_at_1
      value: 87.36
    - type: ndcg_at_10
      value: 73.076
    - type: ndcg_at_100
      value: 75.895
    - type: ndcg_at_1000
      value: 77.049
    - type: ndcg_at_3
      value: 68.929
    - type: ndcg_at_5
      value: 71.28
    - type: precision_at_1
      value: 87.36
    - type: precision_at_10
      value: 14.741000000000001
    - type: precision_at_100
      value: 1.694
    - type: precision_at_1000
      value: 0.185
    - type: precision_at_3
      value: 43.043
    - type: precision_at_5
      value: 27.681
    - type: recall_at_1
      value: 43.68
    - type: recall_at_10
      value: 73.707
    - type: recall_at_100
      value: 84.7
    - type: recall_at_1000
      value: 92.309
    - type: recall_at_3
      value: 64.564
    - type: recall_at_5
      value: 69.203
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
      value: 96.75399999999999
    - type: ap
      value: 95.29389839242187
    - type: f1
      value: 96.75348377433475
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
      value: 25.176
    - type: map_at_10
      value: 38.598
    - type: map_at_100
      value: 39.707
    - type: map_at_1000
      value: 39.744
    - type: map_at_3
      value: 34.566
    - type: map_at_5
      value: 36.863
    - type: mrr_at_1
      value: 25.874000000000002
    - type: mrr_at_10
      value: 39.214
    - type: mrr_at_100
      value: 40.251
    - type: mrr_at_1000
      value: 40.281
    - type: mrr_at_3
      value: 35.291
    - type: mrr_at_5
      value: 37.545
    - type: ndcg_at_1
      value: 25.874000000000002
    - type: ndcg_at_10
      value: 45.98
    - type: ndcg_at_100
      value: 51.197
    - type: ndcg_at_1000
      value: 52.073
    - type: ndcg_at_3
      value: 37.785999999999994
    - type: ndcg_at_5
      value: 41.870000000000005
    - type: precision_at_1
      value: 25.874000000000002
    - type: precision_at_10
      value: 7.181
    - type: precision_at_100
      value: 0.979
    - type: precision_at_1000
      value: 0.106
    - type: precision_at_3
      value: 16.051000000000002
    - type: precision_at_5
      value: 11.713
    - type: recall_at_1
      value: 25.176
    - type: recall_at_10
      value: 68.67699999999999
    - type: recall_at_100
      value: 92.55
    - type: recall_at_1000
      value: 99.164
    - type: recall_at_3
      value: 46.372
    - type: recall_at_5
      value: 56.16
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
      value: 99.03784769721841
    - type: f1
      value: 98.97791641821495
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
      value: 91.88326493388054
    - type: f1
      value: 73.74809928034335
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
      value: 85.41358439811701
    - type: f1
      value: 83.503679460639
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
      value: 89.77135171486215
    - type: f1
      value: 88.89843747468366
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
      value: 46.22695362087359
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
      value: 44.132372165849425
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
      value: 33.35680810650402
    - type: mrr
      value: 34.72625715637218
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
      value: 7.165000000000001
    - type: map_at_10
      value: 15.424
    - type: map_at_100
      value: 20.28
    - type: map_at_1000
      value: 22.065
    - type: map_at_3
      value: 11.236
    - type: map_at_5
      value: 13.025999999999998
    - type: mrr_at_1
      value: 51.702999999999996
    - type: mrr_at_10
      value: 59.965
    - type: mrr_at_100
      value: 60.667
    - type: mrr_at_1000
      value: 60.702999999999996
    - type: mrr_at_3
      value: 58.772000000000006
    - type: mrr_at_5
      value: 59.267
    - type: ndcg_at_1
      value: 49.536
    - type: ndcg_at_10
      value: 40.6
    - type: ndcg_at_100
      value: 37.848
    - type: ndcg_at_1000
      value: 46.657
    - type: ndcg_at_3
      value: 46.117999999999995
    - type: ndcg_at_5
      value: 43.619
    - type: precision_at_1
      value: 51.393
    - type: precision_at_10
      value: 30.31
    - type: precision_at_100
      value: 9.972
    - type: precision_at_1000
      value: 2.329
    - type: precision_at_3
      value: 43.137
    - type: precision_at_5
      value: 37.585
    - type: recall_at_1
      value: 7.165000000000001
    - type: recall_at_10
      value: 19.689999999999998
    - type: recall_at_100
      value: 39.237
    - type: recall_at_1000
      value: 71.417
    - type: recall_at_3
      value: 12.247
    - type: recall_at_5
      value: 14.902999999999999
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
      value: 42.653999999999996
    - type: map_at_10
      value: 59.611999999999995
    - type: map_at_100
      value: 60.32300000000001
    - type: map_at_1000
      value: 60.336
    - type: map_at_3
      value: 55.584999999999994
    - type: map_at_5
      value: 58.19
    - type: mrr_at_1
      value: 47.683
    - type: mrr_at_10
      value: 62.06700000000001
    - type: mrr_at_100
      value: 62.537
    - type: mrr_at_1000
      value: 62.544999999999995
    - type: mrr_at_3
      value: 59.178
    - type: mrr_at_5
      value: 61.034
    - type: ndcg_at_1
      value: 47.654
    - type: ndcg_at_10
      value: 67.001
    - type: ndcg_at_100
      value: 69.73899999999999
    - type: ndcg_at_1000
      value: 69.986
    - type: ndcg_at_3
      value: 59.95700000000001
    - type: ndcg_at_5
      value: 64.025
    - type: precision_at_1
      value: 47.654
    - type: precision_at_10
      value: 10.367999999999999
    - type: precision_at_100
      value: 1.192
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 26.651000000000003
    - type: precision_at_5
      value: 18.459
    - type: recall_at_1
      value: 42.653999999999996
    - type: recall_at_10
      value: 86.619
    - type: recall_at_100
      value: 98.04899999999999
    - type: recall_at_1000
      value: 99.812
    - type: recall_at_3
      value: 68.987
    - type: recall_at_5
      value: 78.158
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
      value: 72.538
    - type: map_at_10
      value: 86.702
    - type: map_at_100
      value: 87.31
    - type: map_at_1000
      value: 87.323
    - type: map_at_3
      value: 83.87
    - type: map_at_5
      value: 85.682
    - type: mrr_at_1
      value: 83.31
    - type: mrr_at_10
      value: 89.225
    - type: mrr_at_100
      value: 89.30399999999999
    - type: mrr_at_1000
      value: 89.30399999999999
    - type: mrr_at_3
      value: 88.44300000000001
    - type: mrr_at_5
      value: 89.005
    - type: ndcg_at_1
      value: 83.32000000000001
    - type: ndcg_at_10
      value: 90.095
    - type: ndcg_at_100
      value: 91.12
    - type: ndcg_at_1000
      value: 91.179
    - type: ndcg_at_3
      value: 87.606
    - type: ndcg_at_5
      value: 89.031
    - type: precision_at_1
      value: 83.32000000000001
    - type: precision_at_10
      value: 13.641
    - type: precision_at_100
      value: 1.541
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 38.377
    - type: precision_at_5
      value: 25.162000000000003
    - type: recall_at_1
      value: 72.538
    - type: recall_at_10
      value: 96.47200000000001
    - type: recall_at_100
      value: 99.785
    - type: recall_at_1000
      value: 99.99900000000001
    - type: recall_at_3
      value: 89.278
    - type: recall_at_5
      value: 93.367
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
      value: 73.55219145406065
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
      value: 74.13437105242755
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
      value: 6.873
    - type: map_at_10
      value: 17.944
    - type: map_at_100
      value: 21.171
    - type: map_at_1000
      value: 21.528
    - type: map_at_3
      value: 12.415
    - type: map_at_5
      value: 15.187999999999999
    - type: mrr_at_1
      value: 33.800000000000004
    - type: mrr_at_10
      value: 46.455
    - type: mrr_at_100
      value: 47.378
    - type: mrr_at_1000
      value: 47.394999999999996
    - type: mrr_at_3
      value: 42.367
    - type: mrr_at_5
      value: 44.972
    - type: ndcg_at_1
      value: 33.800000000000004
    - type: ndcg_at_10
      value: 28.907
    - type: ndcg_at_100
      value: 39.695
    - type: ndcg_at_1000
      value: 44.582
    - type: ndcg_at_3
      value: 26.949
    - type: ndcg_at_5
      value: 23.988
    - type: precision_at_1
      value: 33.800000000000004
    - type: precision_at_10
      value: 15.079999999999998
    - type: precision_at_100
      value: 3.056
    - type: precision_at_1000
      value: 0.42100000000000004
    - type: precision_at_3
      value: 25.167
    - type: precision_at_5
      value: 21.26
    - type: recall_at_1
      value: 6.873
    - type: recall_at_10
      value: 30.568
    - type: recall_at_100
      value: 62.062
    - type: recall_at_1000
      value: 85.37700000000001
    - type: recall_at_3
      value: 15.312999999999999
    - type: recall_at_5
      value: 21.575
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
      value: 82.37009118256057
    - type: cos_sim_spearman
      value: 79.27986395671529
    - type: euclidean_pearson
      value: 79.18037715442115
    - type: euclidean_spearman
      value: 79.28004791561621
    - type: manhattan_pearson
      value: 79.34062972800541
    - type: manhattan_spearman
      value: 79.43106695543402
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
      value: 87.48474767383833
    - type: cos_sim_spearman
      value: 79.54505388752513
    - type: euclidean_pearson
      value: 83.43282704179565
    - type: euclidean_spearman
      value: 79.54579919925405
    - type: manhattan_pearson
      value: 83.77564492427952
    - type: manhattan_spearman
      value: 79.84558396989286
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
      value: 88.803698035802
    - type: cos_sim_spearman
      value: 88.83451367754881
    - type: euclidean_pearson
      value: 88.28939285711628
    - type: euclidean_spearman
      value: 88.83528996073112
    - type: manhattan_pearson
      value: 88.28017412671795
    - type: manhattan_spearman
      value: 88.9228828016344
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
      value: 85.27469288153428
    - type: cos_sim_spearman
      value: 83.87477064876288
    - type: euclidean_pearson
      value: 84.2601737035379
    - type: euclidean_spearman
      value: 83.87431082479074
    - type: manhattan_pearson
      value: 84.3621547772745
    - type: manhattan_spearman
      value: 84.12094375000423
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
      value: 88.12749863201587
    - type: cos_sim_spearman
      value: 88.54287568368565
    - type: euclidean_pearson
      value: 87.90429700607999
    - type: euclidean_spearman
      value: 88.5437689576261
    - type: manhattan_pearson
      value: 88.19276653356833
    - type: manhattan_spearman
      value: 88.99995393814679
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
      value: 85.68398747560902
    - type: cos_sim_spearman
      value: 86.48815303460574
    - type: euclidean_pearson
      value: 85.52356631237954
    - type: euclidean_spearman
      value: 86.486391949551
    - type: manhattan_pearson
      value: 85.67267981761788
    - type: manhattan_spearman
      value: 86.7073696332485
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
      value: 88.9057107443124
    - type: cos_sim_spearman
      value: 88.7312168757697
    - type: euclidean_pearson
      value: 88.72810439714794
    - type: euclidean_spearman
      value: 88.71976185854771
    - type: manhattan_pearson
      value: 88.50433745949111
    - type: manhattan_spearman
      value: 88.51726175544195
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
      value: 67.59391795109886
    - type: cos_sim_spearman
      value: 66.87613008631367
    - type: euclidean_pearson
      value: 69.23198488262217
    - type: euclidean_spearman
      value: 66.85427723013692
    - type: manhattan_pearson
      value: 69.50730124841084
    - type: manhattan_spearman
      value: 67.10404669820792
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
      value: 87.0820605344619
    - type: cos_sim_spearman
      value: 86.8518089863434
    - type: euclidean_pearson
      value: 86.31087134689284
    - type: euclidean_spearman
      value: 86.8518520517941
    - type: manhattan_pearson
      value: 86.47203796160612
    - type: manhattan_spearman
      value: 87.1080149734421
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
      value: 89.09255369305481
    - type: mrr
      value: 97.10323445617563
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
      value: 61.260999999999996
    - type: map_at_10
      value: 74.043
    - type: map_at_100
      value: 74.37700000000001
    - type: map_at_1000
      value: 74.384
    - type: map_at_3
      value: 71.222
    - type: map_at_5
      value: 72.875
    - type: mrr_at_1
      value: 64.333
    - type: mrr_at_10
      value: 74.984
    - type: mrr_at_100
      value: 75.247
    - type: mrr_at_1000
      value: 75.25500000000001
    - type: mrr_at_3
      value: 73.167
    - type: mrr_at_5
      value: 74.35000000000001
    - type: ndcg_at_1
      value: 64.333
    - type: ndcg_at_10
      value: 79.06
    - type: ndcg_at_100
      value: 80.416
    - type: ndcg_at_1000
      value: 80.55600000000001
    - type: ndcg_at_3
      value: 74.753
    - type: ndcg_at_5
      value: 76.97500000000001
    - type: precision_at_1
      value: 64.333
    - type: precision_at_10
      value: 10.567
    - type: precision_at_100
      value: 1.1199999999999999
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 29.889
    - type: precision_at_5
      value: 19.533
    - type: recall_at_1
      value: 61.260999999999996
    - type: recall_at_10
      value: 93.167
    - type: recall_at_100
      value: 99.0
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 81.667
    - type: recall_at_5
      value: 87.394
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
      value: 99.71980198019801
    - type: cos_sim_ap
      value: 92.81616007802704
    - type: cos_sim_f1
      value: 85.17548454688318
    - type: cos_sim_precision
      value: 89.43894389438944
    - type: cos_sim_recall
      value: 81.3
    - type: dot_accuracy
      value: 99.71980198019801
    - type: dot_ap
      value: 92.81398760591358
    - type: dot_f1
      value: 85.17548454688318
    - type: dot_precision
      value: 89.43894389438944
    - type: dot_recall
      value: 81.3
    - type: euclidean_accuracy
      value: 99.71980198019801
    - type: euclidean_ap
      value: 92.81560637245072
    - type: euclidean_f1
      value: 85.17548454688318
    - type: euclidean_precision
      value: 89.43894389438944
    - type: euclidean_recall
      value: 81.3
    - type: manhattan_accuracy
      value: 99.73069306930694
    - type: manhattan_ap
      value: 93.14005487480794
    - type: manhattan_f1
      value: 85.56263269639068
    - type: manhattan_precision
      value: 91.17647058823529
    - type: manhattan_recall
      value: 80.60000000000001
    - type: max_accuracy
      value: 99.73069306930694
    - type: max_ap
      value: 93.14005487480794
    - type: max_f1
      value: 85.56263269639068
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
      value: 79.86443362395185
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
      value: 49.40897096662564
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
      value: 55.66040806627947
    - type: mrr
      value: 56.58670475766064
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
      value: 31.51015090598575
    - type: cos_sim_spearman
      value: 31.35016454939226
    - type: dot_pearson
      value: 31.5150068731
    - type: dot_spearman
      value: 31.34790869023487
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
      value: 0.254
    - type: map_at_10
      value: 2.064
    - type: map_at_100
      value: 12.909
    - type: map_at_1000
      value: 31.761
    - type: map_at_3
      value: 0.738
    - type: map_at_5
      value: 1.155
    - type: mrr_at_1
      value: 96.0
    - type: mrr_at_10
      value: 98.0
    - type: mrr_at_100
      value: 98.0
    - type: mrr_at_1000
      value: 98.0
    - type: mrr_at_3
      value: 98.0
    - type: mrr_at_5
      value: 98.0
    - type: ndcg_at_1
      value: 93.0
    - type: ndcg_at_10
      value: 82.258
    - type: ndcg_at_100
      value: 64.34
    - type: ndcg_at_1000
      value: 57.912
    - type: ndcg_at_3
      value: 90.827
    - type: ndcg_at_5
      value: 86.79
    - type: precision_at_1
      value: 96.0
    - type: precision_at_10
      value: 84.8
    - type: precision_at_100
      value: 66.0
    - type: precision_at_1000
      value: 25.356
    - type: precision_at_3
      value: 94.667
    - type: precision_at_5
      value: 90.4
    - type: recall_at_1
      value: 0.254
    - type: recall_at_10
      value: 2.1950000000000003
    - type: recall_at_100
      value: 16.088
    - type: recall_at_1000
      value: 54.559000000000005
    - type: recall_at_3
      value: 0.75
    - type: recall_at_5
      value: 1.191
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
      value: 2.976
    - type: map_at_10
      value: 11.389000000000001
    - type: map_at_100
      value: 18.429000000000002
    - type: map_at_1000
      value: 20.113
    - type: map_at_3
      value: 6.483
    - type: map_at_5
      value: 8.770999999999999
    - type: mrr_at_1
      value: 40.816
    - type: mrr_at_10
      value: 58.118
    - type: mrr_at_100
      value: 58.489999999999995
    - type: mrr_at_1000
      value: 58.489999999999995
    - type: mrr_at_3
      value: 53.061
    - type: mrr_at_5
      value: 57.041
    - type: ndcg_at_1
      value: 40.816
    - type: ndcg_at_10
      value: 30.567
    - type: ndcg_at_100
      value: 42.44
    - type: ndcg_at_1000
      value: 53.480000000000004
    - type: ndcg_at_3
      value: 36.016
    - type: ndcg_at_5
      value: 34.257
    - type: precision_at_1
      value: 42.857
    - type: precision_at_10
      value: 25.714
    - type: precision_at_100
      value: 8.429
    - type: precision_at_1000
      value: 1.5939999999999999
    - type: precision_at_3
      value: 36.735
    - type: precision_at_5
      value: 33.878
    - type: recall_at_1
      value: 2.976
    - type: recall_at_10
      value: 17.854999999999997
    - type: recall_at_100
      value: 51.833
    - type: recall_at_1000
      value: 86.223
    - type: recall_at_3
      value: 7.887
    - type: recall_at_5
      value: 12.026
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
      value: 85.1174
    - type: ap
      value: 30.169441069345748
    - type: f1
      value: 69.79254701873245
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
      value: 72.58347481607245
    - type: f1
      value: 72.74877295564937
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
      value: 53.90586138221305
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
      value: 87.35769207844072
    - type: cos_sim_ap
      value: 77.9645072410354
    - type: cos_sim_f1
      value: 71.32352941176471
    - type: cos_sim_precision
      value: 66.5903890160183
    - type: cos_sim_recall
      value: 76.78100263852242
    - type: dot_accuracy
      value: 87.37557370209214
    - type: dot_ap
      value: 77.96250046429908
    - type: dot_f1
      value: 71.28932757557064
    - type: dot_precision
      value: 66.95249130938586
    - type: dot_recall
      value: 76.22691292875989
    - type: euclidean_accuracy
      value: 87.35173153722357
    - type: euclidean_ap
      value: 77.96520460741593
    - type: euclidean_f1
      value: 71.32470733210104
    - type: euclidean_precision
      value: 66.91329479768785
    - type: euclidean_recall
      value: 76.35883905013192
    - type: manhattan_accuracy
      value: 87.25636287774931
    - type: manhattan_ap
      value: 77.77752485611796
    - type: manhattan_f1
      value: 71.18148599269183
    - type: manhattan_precision
      value: 66.10859728506787
    - type: manhattan_recall
      value: 77.0976253298153
    - type: max_accuracy
      value: 87.37557370209214
    - type: max_ap
      value: 77.96520460741593
    - type: max_f1
      value: 71.32470733210104
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
      value: 89.38176737687739
    - type: cos_sim_ap
      value: 86.58811861657401
    - type: cos_sim_f1
      value: 79.09430644097604
    - type: cos_sim_precision
      value: 75.45085977911366
    - type: cos_sim_recall
      value: 83.10748383122882
    - type: dot_accuracy
      value: 89.38370784336554
    - type: dot_ap
      value: 86.58840606004333
    - type: dot_f1
      value: 79.10179860068133
    - type: dot_precision
      value: 75.44546153308643
    - type: dot_recall
      value: 83.13058207576223
    - type: euclidean_accuracy
      value: 89.38564830985369
    - type: euclidean_ap
      value: 86.58820721061164
    - type: euclidean_f1
      value: 79.09070942235888
    - type: euclidean_precision
      value: 75.38729937194697
    - type: euclidean_recall
      value: 83.17677856482906
    - type: manhattan_accuracy
      value: 89.40699344122326
    - type: manhattan_ap
      value: 86.60631843011362
    - type: manhattan_f1
      value: 79.14949970570925
    - type: manhattan_precision
      value: 75.78191039729502
    - type: manhattan_recall
      value: 82.83030489682784
    - type: max_accuracy
      value: 89.40699344122326
    - type: max_ap
      value: 86.60631843011362
    - type: max_f1
      value: 79.14949970570925
  - task:
      type: STS
    dataset:
      type: C-MTEB/AFQMC
      name: MTEB AFQMC
      config: default
      split: validation
      revision: b44c3b011063adb25877c13823db83bb193913c4
    metrics:
    - type: cos_sim_pearson
      value: 65.58442135663871
    - type: cos_sim_spearman
      value: 72.2538631361313
    - type: euclidean_pearson
      value: 70.97255486607429
    - type: euclidean_spearman
      value: 72.25374250228647
    - type: manhattan_pearson
      value: 70.83250199989911
    - type: manhattan_spearman
      value: 72.14819496536272
  - task:
      type: STS
    dataset:
      type: C-MTEB/ATEC
      name: MTEB ATEC
      config: default
      split: test
      revision: 0f319b1142f28d00e055a6770f3f726ae9b7d865
    metrics:
    - type: cos_sim_pearson
      value: 59.99478404929932
    - type: cos_sim_spearman
      value: 62.61836216999812
    - type: euclidean_pearson
      value: 66.86429811933593
    - type: euclidean_spearman
      value: 62.6183520374191
    - type: manhattan_pearson
      value: 66.8063778911633
    - type: manhattan_spearman
      value: 62.569607573241115
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (zh)
      config: zh
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 53.98400000000001
    - type: f1
      value: 51.21447361350723
  - task:
      type: STS
    dataset:
      type: C-MTEB/BQ
      name: MTEB BQ
      config: default
      split: test
      revision: e3dda5e115e487b39ec7e618c0c6a29137052a55
    metrics:
    - type: cos_sim_pearson
      value: 79.11941660686553
    - type: cos_sim_spearman
      value: 81.25029594540435
    - type: euclidean_pearson
      value: 82.06973504238826
    - type: euclidean_spearman
      value: 81.2501989488524
    - type: manhattan_pearson
      value: 82.10094630392753
    - type: manhattan_spearman
      value: 81.27987244392389
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/CLSClusteringP2P
      name: MTEB CLSClusteringP2P
      config: default
      split: test
      revision: 4b6227591c6c1a73bc76b1055f3b7f3588e72476
    metrics:
    - type: v_measure
      value: 47.07270168705156
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/CLSClusteringS2S
      name: MTEB CLSClusteringS2S
      config: default
      split: test
      revision: e458b3f5414b62b7f9f83499ac1f5497ae2e869f
    metrics:
    - type: v_measure
      value: 45.98511703185043
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/CMedQAv1-reranking
      name: MTEB CMedQAv1
      config: default
      split: test
      revision: 8d7f1e942507dac42dc58017c1a001c3717da7df
    metrics:
    - type: map
      value: 88.19895157194931
    - type: mrr
      value: 90.21424603174603
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/CMedQAv2-reranking
      name: MTEB CMedQAv2
      config: default
      split: test
      revision: 23d186750531a14a0357ca22cd92d712fd512ea0
    metrics:
    - type: map
      value: 88.03317320980119
    - type: mrr
      value: 89.9461507936508
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CmedqaRetrieval
      name: MTEB CmedqaRetrieval
      config: default
      split: dev
      revision: cd540c506dae1cf9e9a59c3e06f42030d54e7301
    metrics:
    - type: map_at_1
      value: 29.037000000000003
    - type: map_at_10
      value: 42.001
    - type: map_at_100
      value: 43.773
    - type: map_at_1000
      value: 43.878
    - type: map_at_3
      value: 37.637
    - type: map_at_5
      value: 40.034
    - type: mrr_at_1
      value: 43.136
    - type: mrr_at_10
      value: 51.158
    - type: mrr_at_100
      value: 52.083
    - type: mrr_at_1000
      value: 52.12
    - type: mrr_at_3
      value: 48.733
    - type: mrr_at_5
      value: 50.025
    - type: ndcg_at_1
      value: 43.136
    - type: ndcg_at_10
      value: 48.685
    - type: ndcg_at_100
      value: 55.513
    - type: ndcg_at_1000
      value: 57.242000000000004
    - type: ndcg_at_3
      value: 43.329
    - type: ndcg_at_5
      value: 45.438
    - type: precision_at_1
      value: 43.136
    - type: precision_at_10
      value: 10.56
    - type: precision_at_100
      value: 1.6129999999999998
    - type: precision_at_1000
      value: 0.184
    - type: precision_at_3
      value: 24.064
    - type: precision_at_5
      value: 17.269000000000002
    - type: recall_at_1
      value: 29.037000000000003
    - type: recall_at_10
      value: 59.245000000000005
    - type: recall_at_100
      value: 87.355
    - type: recall_at_1000
      value: 98.74000000000001
    - type: recall_at_3
      value: 42.99
    - type: recall_at_5
      value: 49.681999999999995
  - task:
      type: PairClassification
    dataset:
      type: C-MTEB/CMNLI
      name: MTEB Cmnli
      config: default
      split: validation
      revision: 41bc36f332156f7adc9e38f53777c959b2ae9766
    metrics:
    - type: cos_sim_accuracy
      value: 82.68190018039687
    - type: cos_sim_ap
      value: 90.18017125327886
    - type: cos_sim_f1
      value: 83.64080906868193
    - type: cos_sim_precision
      value: 79.7076890489303
    - type: cos_sim_recall
      value: 87.98223053542202
    - type: dot_accuracy
      value: 82.68190018039687
    - type: dot_ap
      value: 90.18782350103646
    - type: dot_f1
      value: 83.64242087729039
    - type: dot_precision
      value: 79.65313028764805
    - type: dot_recall
      value: 88.05237315875614
    - type: euclidean_accuracy
      value: 82.68190018039687
    - type: euclidean_ap
      value: 90.1801957900632
    - type: euclidean_f1
      value: 83.63636363636364
    - type: euclidean_precision
      value: 79.52772506852203
    - type: euclidean_recall
      value: 88.19265840542437
    - type: manhattan_accuracy
      value: 82.14070956103427
    - type: manhattan_ap
      value: 89.96178420101427
    - type: manhattan_f1
      value: 83.21087838578791
    - type: manhattan_precision
      value: 78.35605121850475
    - type: manhattan_recall
      value: 88.70703764320785
    - type: max_accuracy
      value: 82.68190018039687
    - type: max_ap
      value: 90.18782350103646
    - type: max_f1
      value: 83.64242087729039
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CovidRetrieval
      name: MTEB CovidRetrieval
      config: default
      split: dev
      revision: 1271c7809071a13532e05f25fb53511ffce77117
    metrics:
    - type: map_at_1
      value: 72.234
    - type: map_at_10
      value: 80.10000000000001
    - type: map_at_100
      value: 80.36
    - type: map_at_1000
      value: 80.363
    - type: map_at_3
      value: 78.315
    - type: map_at_5
      value: 79.607
    - type: mrr_at_1
      value: 72.392
    - type: mrr_at_10
      value: 80.117
    - type: mrr_at_100
      value: 80.36999999999999
    - type: mrr_at_1000
      value: 80.373
    - type: mrr_at_3
      value: 78.469
    - type: mrr_at_5
      value: 79.633
    - type: ndcg_at_1
      value: 72.392
    - type: ndcg_at_10
      value: 83.651
    - type: ndcg_at_100
      value: 84.749
    - type: ndcg_at_1000
      value: 84.83000000000001
    - type: ndcg_at_3
      value: 80.253
    - type: ndcg_at_5
      value: 82.485
    - type: precision_at_1
      value: 72.392
    - type: precision_at_10
      value: 9.557
    - type: precision_at_100
      value: 1.004
    - type: precision_at_1000
      value: 0.101
    - type: precision_at_3
      value: 28.732000000000003
    - type: precision_at_5
      value: 18.377
    - type: recall_at_1
      value: 72.234
    - type: recall_at_10
      value: 94.573
    - type: recall_at_100
      value: 99.368
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 85.669
    - type: recall_at_5
      value: 91.01700000000001
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/DuRetrieval
      name: MTEB DuRetrieval
      config: default
      split: dev
      revision: a1a333e290fe30b10f3f56498e3a0d911a693ced
    metrics:
    - type: map_at_1
      value: 26.173999999999996
    - type: map_at_10
      value: 80.04
    - type: map_at_100
      value: 82.94500000000001
    - type: map_at_1000
      value: 82.98100000000001
    - type: map_at_3
      value: 55.562999999999995
    - type: map_at_5
      value: 69.89800000000001
    - type: mrr_at_1
      value: 89.5
    - type: mrr_at_10
      value: 92.996
    - type: mrr_at_100
      value: 93.06400000000001
    - type: mrr_at_1000
      value: 93.065
    - type: mrr_at_3
      value: 92.658
    - type: mrr_at_5
      value: 92.84599999999999
    - type: ndcg_at_1
      value: 89.5
    - type: ndcg_at_10
      value: 87.443
    - type: ndcg_at_100
      value: 90.253
    - type: ndcg_at_1000
      value: 90.549
    - type: ndcg_at_3
      value: 85.874
    - type: ndcg_at_5
      value: 84.842
    - type: precision_at_1
      value: 89.5
    - type: precision_at_10
      value: 41.805
    - type: precision_at_100
      value: 4.827
    - type: precision_at_1000
      value: 0.49
    - type: precision_at_3
      value: 76.85
    - type: precision_at_5
      value: 64.8
    - type: recall_at_1
      value: 26.173999999999996
    - type: recall_at_10
      value: 89.101
    - type: recall_at_100
      value: 98.08099999999999
    - type: recall_at_1000
      value: 99.529
    - type: recall_at_3
      value: 57.902
    - type: recall_at_5
      value: 74.602
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/EcomRetrieval
      name: MTEB EcomRetrieval
      config: default
      split: dev
      revision: 687de13dc7294d6fd9be10c6945f9e8fec8166b9
    metrics:
    - type: map_at_1
      value: 56.10000000000001
    - type: map_at_10
      value: 66.15299999999999
    - type: map_at_100
      value: 66.625
    - type: map_at_1000
      value: 66.636
    - type: map_at_3
      value: 63.632999999999996
    - type: map_at_5
      value: 65.293
    - type: mrr_at_1
      value: 56.10000000000001
    - type: mrr_at_10
      value: 66.15299999999999
    - type: mrr_at_100
      value: 66.625
    - type: mrr_at_1000
      value: 66.636
    - type: mrr_at_3
      value: 63.632999999999996
    - type: mrr_at_5
      value: 65.293
    - type: ndcg_at_1
      value: 56.10000000000001
    - type: ndcg_at_10
      value: 71.146
    - type: ndcg_at_100
      value: 73.27799999999999
    - type: ndcg_at_1000
      value: 73.529
    - type: ndcg_at_3
      value: 66.09
    - type: ndcg_at_5
      value: 69.08999999999999
    - type: precision_at_1
      value: 56.10000000000001
    - type: precision_at_10
      value: 8.68
    - type: precision_at_100
      value: 0.964
    - type: precision_at_1000
      value: 0.098
    - type: precision_at_3
      value: 24.4
    - type: precision_at_5
      value: 16.1
    - type: recall_at_1
      value: 56.10000000000001
    - type: recall_at_10
      value: 86.8
    - type: recall_at_100
      value: 96.39999999999999
    - type: recall_at_1000
      value: 98.3
    - type: recall_at_3
      value: 73.2
    - type: recall_at_5
      value: 80.5
  - task:
      type: Classification
    dataset:
      type: C-MTEB/IFlyTek-classification
      name: MTEB IFlyTek
      config: default
      split: validation
      revision: 421605374b29664c5fc098418fe20ada9bd55f8a
    metrics:
    - type: accuracy
      value: 54.52096960369373
    - type: f1
      value: 40.930845295808695
  - task:
      type: Classification
    dataset:
      type: C-MTEB/JDReview-classification
      name: MTEB JDReview
      config: default
      split: test
      revision: b7c64bd89eb87f8ded463478346f76731f07bf8b
    metrics:
    - type: accuracy
      value: 86.51031894934334
    - type: ap
      value: 55.9516014323483
    - type: f1
      value: 81.54813679326381
  - task:
      type: STS
    dataset:
      type: C-MTEB/LCQMC
      name: MTEB LCQMC
      config: default
      split: test
      revision: 17f9b096f80380fce5ed12a9be8be7784b337daf
    metrics:
    - type: cos_sim_pearson
      value: 69.67437838574276
    - type: cos_sim_spearman
      value: 73.81314174653045
    - type: euclidean_pearson
      value: 72.63430276680275
    - type: euclidean_spearman
      value: 73.81358736777001
    - type: manhattan_pearson
      value: 72.58743833842829
    - type: manhattan_spearman
      value: 73.7590419009179
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/Mmarco-reranking
      name: MTEB MMarcoReranking
      config: default
      split: dev
      revision: None
    metrics:
    - type: map
      value: 31.648613483640254
    - type: mrr
      value: 30.37420634920635
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MMarcoRetrieval
      name: MTEB MMarcoRetrieval
      config: default
      split: dev
      revision: 539bbde593d947e2a124ba72651aafc09eb33fc2
    metrics:
    - type: map_at_1
      value: 73.28099999999999
    - type: map_at_10
      value: 81.977
    - type: map_at_100
      value: 82.222
    - type: map_at_1000
      value: 82.22699999999999
    - type: map_at_3
      value: 80.441
    - type: map_at_5
      value: 81.46600000000001
    - type: mrr_at_1
      value: 75.673
    - type: mrr_at_10
      value: 82.41000000000001
    - type: mrr_at_100
      value: 82.616
    - type: mrr_at_1000
      value: 82.621
    - type: mrr_at_3
      value: 81.094
    - type: mrr_at_5
      value: 81.962
    - type: ndcg_at_1
      value: 75.673
    - type: ndcg_at_10
      value: 85.15599999999999
    - type: ndcg_at_100
      value: 86.151
    - type: ndcg_at_1000
      value: 86.26899999999999
    - type: ndcg_at_3
      value: 82.304
    - type: ndcg_at_5
      value: 84.009
    - type: precision_at_1
      value: 75.673
    - type: precision_at_10
      value: 10.042
    - type: precision_at_100
      value: 1.052
    - type: precision_at_1000
      value: 0.106
    - type: precision_at_3
      value: 30.673000000000002
    - type: precision_at_5
      value: 19.326999999999998
    - type: recall_at_1
      value: 73.28099999999999
    - type: recall_at_10
      value: 94.446
    - type: recall_at_100
      value: 98.737
    - type: recall_at_1000
      value: 99.649
    - type: recall_at_3
      value: 86.984
    - type: recall_at_5
      value: 91.024
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (zh-CN)
      config: zh-CN
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 81.08607935440484
    - type: f1
      value: 78.24879986066307
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (zh-CN)
      config: zh-CN
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 86.05917955615332
    - type: f1
      value: 85.05279279434997
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MedicalRetrieval
      name: MTEB MedicalRetrieval
      config: default
      split: dev
      revision: 2039188fb5800a9803ba5048df7b76e6fb151fc6
    metrics:
    - type: map_at_1
      value: 56.2
    - type: map_at_10
      value: 62.57899999999999
    - type: map_at_100
      value: 63.154999999999994
    - type: map_at_1000
      value: 63.193
    - type: map_at_3
      value: 61.217
    - type: map_at_5
      value: 62.012
    - type: mrr_at_1
      value: 56.3
    - type: mrr_at_10
      value: 62.629000000000005
    - type: mrr_at_100
      value: 63.205999999999996
    - type: mrr_at_1000
      value: 63.244
    - type: mrr_at_3
      value: 61.267
    - type: mrr_at_5
      value: 62.062
    - type: ndcg_at_1
      value: 56.2
    - type: ndcg_at_10
      value: 65.592
    - type: ndcg_at_100
      value: 68.657
    - type: ndcg_at_1000
      value: 69.671
    - type: ndcg_at_3
      value: 62.808
    - type: ndcg_at_5
      value: 64.24499999999999
    - type: precision_at_1
      value: 56.2
    - type: precision_at_10
      value: 7.5
    - type: precision_at_100
      value: 0.899
    - type: precision_at_1000
      value: 0.098
    - type: precision_at_3
      value: 22.467000000000002
    - type: precision_at_5
      value: 14.180000000000001
    - type: recall_at_1
      value: 56.2
    - type: recall_at_10
      value: 75.0
    - type: recall_at_100
      value: 89.9
    - type: recall_at_1000
      value: 97.89999999999999
    - type: recall_at_3
      value: 67.4
    - type: recall_at_5
      value: 70.89999999999999
  - task:
      type: Classification
    dataset:
      type: C-MTEB/MultilingualSentiment-classification
      name: MTEB MultilingualSentiment
      config: default
      split: validation
      revision: 46958b007a63fdbf239b7672c25d0bea67b5ea1a
    metrics:
    - type: accuracy
      value: 76.87666666666667
    - type: f1
      value: 76.7317686219665
  - task:
      type: PairClassification
    dataset:
      type: C-MTEB/OCNLI
      name: MTEB Ocnli
      config: default
      split: validation
      revision: 66e76a618a34d6d565d5538088562851e6daa7ec
    metrics:
    - type: cos_sim_accuracy
      value: 79.64266377910124
    - type: cos_sim_ap
      value: 84.78274442344829
    - type: cos_sim_f1
      value: 81.16947472745292
    - type: cos_sim_precision
      value: 76.47058823529412
    - type: cos_sim_recall
      value: 86.48363252375924
    - type: dot_accuracy
      value: 79.64266377910124
    - type: dot_ap
      value: 84.7851404063692
    - type: dot_f1
      value: 81.16947472745292
    - type: dot_precision
      value: 76.47058823529412
    - type: dot_recall
      value: 86.48363252375924
    - type: euclidean_accuracy
      value: 79.64266377910124
    - type: euclidean_ap
      value: 84.78068373762378
    - type: euclidean_f1
      value: 81.14794656110837
    - type: euclidean_precision
      value: 76.35009310986965
    - type: euclidean_recall
      value: 86.58922914466737
    - type: manhattan_accuracy
      value: 79.48023822414727
    - type: manhattan_ap
      value: 84.72928897427576
    - type: manhattan_f1
      value: 81.32084770823064
    - type: manhattan_precision
      value: 76.24768946395564
    - type: manhattan_recall
      value: 87.11721224920802
    - type: max_accuracy
      value: 79.64266377910124
    - type: max_ap
      value: 84.7851404063692
    - type: max_f1
      value: 81.32084770823064
  - task:
      type: Classification
    dataset:
      type: C-MTEB/OnlineShopping-classification
      name: MTEB OnlineShopping
      config: default
      split: test
      revision: e610f2ebd179a8fda30ae534c3878750a96db120
    metrics:
    - type: accuracy
      value: 94.3
    - type: ap
      value: 92.8664032274438
    - type: f1
      value: 94.29311102997727
  - task:
      type: STS
    dataset:
      type: C-MTEB/PAWSX
      name: MTEB PAWSX
      config: default
      split: test
      revision: 9c6a90e430ac22b5779fb019a23e820b11a8b5e1
    metrics:
    - type: cos_sim_pearson
      value: 48.51392279882909
    - type: cos_sim_spearman
      value: 54.06338895994974
    - type: euclidean_pearson
      value: 52.58480559573412
    - type: euclidean_spearman
      value: 54.06417276612201
    - type: manhattan_pearson
      value: 52.69525121721343
    - type: manhattan_spearman
      value: 54.048147455389675
  - task:
      type: STS
    dataset:
      type: C-MTEB/QBQTC
      name: MTEB QBQTC
      config: default
      split: test
      revision: 790b0510dc52b1553e8c49f3d2afb48c0e5c48b7
    metrics:
    - type: cos_sim_pearson
      value: 29.728387290757325
    - type: cos_sim_spearman
      value: 31.366121633635284
    - type: euclidean_pearson
      value: 29.14588368552961
    - type: euclidean_spearman
      value: 31.36764411112844
    - type: manhattan_pearson
      value: 29.63517350523121
    - type: manhattan_spearman
      value: 31.94157020583762
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (zh)
      config: zh
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_pearson
      value: 63.64868296271406
    - type: cos_sim_spearman
      value: 66.12800618164744
    - type: euclidean_pearson
      value: 63.21405767340238
    - type: euclidean_spearman
      value: 66.12786567790748
    - type: manhattan_pearson
      value: 64.04300276525848
    - type: manhattan_spearman
      value: 66.5066857145652
  - task:
      type: STS
    dataset:
      type: C-MTEB/STSB
      name: MTEB STSB
      config: default
      split: test
      revision: 0cde68302b3541bb8b3c340dc0644b0b745b3dc0
    metrics:
    - type: cos_sim_pearson
      value: 81.2302623912794
    - type: cos_sim_spearman
      value: 81.16833673266562
    - type: euclidean_pearson
      value: 79.47647843876024
    - type: euclidean_spearman
      value: 81.16944349524972
    - type: manhattan_pearson
      value: 79.84947238492208
    - type: manhattan_spearman
      value: 81.64626599410026
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/T2Reranking
      name: MTEB T2Reranking
      config: default
      split: dev
      revision: 76631901a18387f85eaa53e5450019b87ad58ef9
    metrics:
    - type: map
      value: 67.80129586475687
    - type: mrr
      value: 77.77402311635554
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/T2Retrieval
      name: MTEB T2Retrieval
      config: default
      split: dev
      revision: 8731a845f1bf500a4f111cf1070785c793d10e64
    metrics:
    - type: map_at_1
      value: 28.666999999999998
    - type: map_at_10
      value: 81.063
    - type: map_at_100
      value: 84.504
    - type: map_at_1000
      value: 84.552
    - type: map_at_3
      value: 56.897
    - type: map_at_5
      value: 70.073
    - type: mrr_at_1
      value: 92.087
    - type: mrr_at_10
      value: 94.132
    - type: mrr_at_100
      value: 94.19800000000001
    - type: mrr_at_1000
      value: 94.19999999999999
    - type: mrr_at_3
      value: 93.78999999999999
    - type: mrr_at_5
      value: 94.002
    - type: ndcg_at_1
      value: 92.087
    - type: ndcg_at_10
      value: 87.734
    - type: ndcg_at_100
      value: 90.736
    - type: ndcg_at_1000
      value: 91.184
    - type: ndcg_at_3
      value: 88.78
    - type: ndcg_at_5
      value: 87.676
    - type: precision_at_1
      value: 92.087
    - type: precision_at_10
      value: 43.46
    - type: precision_at_100
      value: 5.07
    - type: precision_at_1000
      value: 0.518
    - type: precision_at_3
      value: 77.49000000000001
    - type: precision_at_5
      value: 65.194
    - type: recall_at_1
      value: 28.666999999999998
    - type: recall_at_10
      value: 86.632
    - type: recall_at_100
      value: 96.646
    - type: recall_at_1000
      value: 98.917
    - type: recall_at_3
      value: 58.333999999999996
    - type: recall_at_5
      value: 72.974
  - task:
      type: Classification
    dataset:
      type: C-MTEB/TNews-classification
      name: MTEB TNews
      config: default
      split: validation
      revision: 317f262bf1e6126357bbe89e875451e4b0938fe4
    metrics:
    - type: accuracy
      value: 52.971999999999994
    - type: f1
      value: 50.2898280984929
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/ThuNewsClusteringP2P
      name: MTEB ThuNewsClusteringP2P
      config: default
      split: test
      revision: 5798586b105c0434e4f0fe5e767abe619442cf93
    metrics:
    - type: v_measure
      value: 86.0797948663824
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/ThuNewsClusteringS2S
      name: MTEB ThuNewsClusteringS2S
      config: default
      split: test
      revision: 8a8b2caeda43f39e13c4bc5bea0f8a667896e10d
    metrics:
    - type: v_measure
      value: 85.10759092255017
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/VideoRetrieval
      name: MTEB VideoRetrieval
      config: default
      split: dev
      revision: 58c2597a5943a2ba48f4668c3b90d796283c5639
    metrics:
    - type: map_at_1
      value: 65.60000000000001
    - type: map_at_10
      value: 74.773
    - type: map_at_100
      value: 75.128
    - type: map_at_1000
      value: 75.136
    - type: map_at_3
      value: 73.05
    - type: map_at_5
      value: 74.13499999999999
    - type: mrr_at_1
      value: 65.60000000000001
    - type: mrr_at_10
      value: 74.773
    - type: mrr_at_100
      value: 75.128
    - type: mrr_at_1000
      value: 75.136
    - type: mrr_at_3
      value: 73.05
    - type: mrr_at_5
      value: 74.13499999999999
    - type: ndcg_at_1
      value: 65.60000000000001
    - type: ndcg_at_10
      value: 78.84299999999999
    - type: ndcg_at_100
      value: 80.40899999999999
    - type: ndcg_at_1000
      value: 80.57
    - type: ndcg_at_3
      value: 75.40599999999999
    - type: ndcg_at_5
      value: 77.351
    - type: precision_at_1
      value: 65.60000000000001
    - type: precision_at_10
      value: 9.139999999999999
    - type: precision_at_100
      value: 0.984
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 27.400000000000002
    - type: precision_at_5
      value: 17.380000000000003
    - type: recall_at_1
      value: 65.60000000000001
    - type: recall_at_10
      value: 91.4
    - type: recall_at_100
      value: 98.4
    - type: recall_at_1000
      value: 99.6
    - type: recall_at_3
      value: 82.19999999999999
    - type: recall_at_5
      value: 86.9
  - task:
      type: Classification
    dataset:
      type: C-MTEB/waimai-classification
      name: MTEB Waimai
      config: default
      split: test
      revision: 339287def212450dcaa9df8c22bf93e9980c7023
    metrics:
    - type: accuracy
      value: 89.47
    - type: ap
      value: 75.59561751845389
    - type: f1
      value: 87.95207751382563
  - dataset:
      config: default
      name: MTEB AlloProfClusteringP2P
      revision: 392ba3f5bcc8c51f578786c1fc3dae648662cb9b
      split: test
      type: lyon-nlp/alloprof
    metrics:
    - type: v_measure
      value: 76.05592323841036
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
      value: 64.51718058866508
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
      value: 73.08278490943373
    - type: mrr
      value: 74.66561454570449
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
      value: 38.912
    - type: map_at_10
      value: 52.437999999999995
    - type: map_at_100
      value: 53.38
    - type: map_at_1000
      value: 53.427
    - type: map_at_3
      value: 48.879
    - type: map_at_5
      value: 50.934000000000005
    - type: mrr_at_1
      value: 44.085
    - type: mrr_at_10
      value: 55.337
    - type: mrr_at_100
      value: 56.016999999999996
    - type: mrr_at_1000
      value: 56.043
    - type: mrr_at_3
      value: 52.55499999999999
    - type: mrr_at_5
      value: 54.20399999999999
    - type: ndcg_at_1
      value: 44.085
    - type: ndcg_at_10
      value: 58.876
    - type: ndcg_at_100
      value: 62.714000000000006
    - type: ndcg_at_1000
      value: 63.721000000000004
    - type: ndcg_at_3
      value: 52.444
    - type: ndcg_at_5
      value: 55.692
    - type: precision_at_1
      value: 44.085
    - type: precision_at_10
      value: 9.21
    - type: precision_at_100
      value: 1.164
    - type: precision_at_1000
      value: 0.128
    - type: precision_at_3
      value: 23.043
    - type: precision_at_5
      value: 15.898000000000001
    - type: recall_at_1
      value: 38.912
    - type: recall_at_10
      value: 75.577
    - type: recall_at_100
      value: 92.038
    - type: recall_at_1000
      value: 99.325
    - type: recall_at_3
      value: 58.592
    - type: recall_at_5
      value: 66.235
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
      value: 55.532000000000004
    - type: f1
      value: 52.5783943471605
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
      value: 8.108
    - type: map_at_10
      value: 14.710999999999999
    - type: map_at_100
      value: 15.891
    - type: map_at_1000
      value: 15.983
    - type: map_at_3
      value: 12.237
    - type: map_at_5
      value: 13.679
    - type: mrr_at_1
      value: 8.108
    - type: mrr_at_10
      value: 14.710999999999999
    - type: mrr_at_100
      value: 15.891
    - type: mrr_at_1000
      value: 15.983
    - type: mrr_at_3
      value: 12.237
    - type: mrr_at_5
      value: 13.679
    - type: ndcg_at_1
      value: 8.108
    - type: ndcg_at_10
      value: 18.796
    - type: ndcg_at_100
      value: 25.098
    - type: ndcg_at_1000
      value: 27.951999999999998
    - type: ndcg_at_3
      value: 13.712
    - type: ndcg_at_5
      value: 16.309
    - type: precision_at_1
      value: 8.108
    - type: precision_at_10
      value: 3.198
    - type: precision_at_100
      value: 0.626
    - type: precision_at_1000
      value: 0.086
    - type: precision_at_3
      value: 6.006
    - type: precision_at_5
      value: 4.865
    - type: recall_at_1
      value: 8.108
    - type: recall_at_10
      value: 31.982
    - type: recall_at_100
      value: 62.613
    - type: recall_at_1000
      value: 86.036
    - type: recall_at_3
      value: 18.018
    - type: recall_at_5
      value: 24.324
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
      value: 30.833269778867116
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
      value: 50.0281928004713
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
      value: 43.699961510636534
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
      value: 96.68963357344191
    - type: f1
      value: 96.45175170820961
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
      value: 87.46946445349202
    - type: f1
      value: 65.79860440988624
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
      value: 82.60663507109005
    - type: f1
      value: 77.20462646604777
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
      value: 60.19311264967803
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
      value: 63.6235764409785
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
      value: 81.65097511768661
    - type: f1
      value: 78.77796091490924
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
      value: 86.64425016812373
    - type: f1
      value: 85.4912728670017
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
      value: 35.913000000000004
    - type: map_at_10
      value: 48.147
    - type: map_at_100
      value: 48.91
    - type: map_at_1000
      value: 48.949
    - type: map_at_3
      value: 45.269999999999996
    - type: map_at_5
      value: 47.115
    - type: mrr_at_1
      value: 35.913000000000004
    - type: mrr_at_10
      value: 48.147
    - type: mrr_at_100
      value: 48.91
    - type: mrr_at_1000
      value: 48.949
    - type: mrr_at_3
      value: 45.269999999999996
    - type: mrr_at_5
      value: 47.115
    - type: ndcg_at_1
      value: 35.913000000000004
    - type: ndcg_at_10
      value: 54.03
    - type: ndcg_at_100
      value: 57.839
    - type: ndcg_at_1000
      value: 58.925000000000004
    - type: ndcg_at_3
      value: 48.217999999999996
    - type: ndcg_at_5
      value: 51.56699999999999
    - type: precision_at_1
      value: 35.913000000000004
    - type: precision_at_10
      value: 7.244000000000001
    - type: precision_at_100
      value: 0.9039999999999999
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_3
      value: 18.905
    - type: precision_at_5
      value: 12.981000000000002
    - type: recall_at_1
      value: 35.913000000000004
    - type: recall_at_10
      value: 72.441
    - type: recall_at_100
      value: 90.41799999999999
    - type: recall_at_1000
      value: 99.099
    - type: recall_at_3
      value: 56.716
    - type: recall_at_5
      value: 64.90599999999999
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
      value: 75.25
    - type: cos_sim_ap
      value: 80.86376001270014
    - type: cos_sim_f1
      value: 73.65945437441204
    - type: cos_sim_precision
      value: 64.02289452166802
    - type: cos_sim_recall
      value: 86.71096345514951
    - type: dot_accuracy
      value: 75.25
    - type: dot_ap
      value: 80.93686107633002
    - type: dot_f1
      value: 73.65945437441204
    - type: dot_precision
      value: 64.02289452166802
    - type: dot_recall
      value: 86.71096345514951
    - type: euclidean_accuracy
      value: 75.25
    - type: euclidean_ap
      value: 80.86379136218862
    - type: euclidean_f1
      value: 73.65945437441204
    - type: euclidean_precision
      value: 64.02289452166802
    - type: euclidean_recall
      value: 86.71096345514951
    - type: manhattan_accuracy
      value: 75.3
    - type: manhattan_ap
      value: 80.87826606097734
    - type: manhattan_f1
      value: 73.68421052631581
    - type: manhattan_precision
      value: 64.0
    - type: manhattan_recall
      value: 86.82170542635659
    - type: max_accuracy
      value: 75.3
    - type: max_ap
      value: 80.93686107633002
    - type: max_f1
      value: 73.68421052631581
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
      value: 81.42349425981143
    - type: cos_sim_spearman
      value: 78.90454327031226
    - type: euclidean_pearson
      value: 78.39086497435166
    - type: euclidean_spearman
      value: 78.9046133980509
    - type: manhattan_pearson
      value: 78.63743094286502
    - type: manhattan_spearman
      value: 79.12136348449269
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
      value: 81.452697919749
    - type: cos_sim_spearman
      value: 82.58116836039301
    - type: euclidean_pearson
      value: 81.04038478932786
    - type: euclidean_spearman
      value: 82.58116836039301
    - type: manhattan_pearson
      value: 81.37075396187771
    - type: manhattan_spearman
      value: 82.73678231355368
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
      value: 85.7419764013806
    - type: cos_sim_spearman
      value: 85.46085808849622
    - type: euclidean_pearson
      value: 83.70449639870063
    - type: euclidean_spearman
      value: 85.46159013076233
    - type: manhattan_pearson
      value: 83.95259510313929
    - type: manhattan_spearman
      value: 85.8029724659458
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
      value: 32.61063271753325
    - type: cos_sim_spearman
      value: 31.454589417353603
    - type: dot_pearson
      value: 32.6106288643431
    - type: dot_spearman
      value: 31.454589417353603
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
      value: 84.31666666666666
    - type: mrr
      value: 84.31666666666666
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
      value: 63.0
    - type: map_at_10
      value: 73.471
    - type: map_at_100
      value: 73.87
    - type: map_at_1000
      value: 73.87
    - type: map_at_3
      value: 70.5
    - type: map_at_5
      value: 73.05
    - type: mrr_at_1
      value: 63.0
    - type: mrr_at_10
      value: 73.471
    - type: mrr_at_100
      value: 73.87
    - type: mrr_at_1000
      value: 73.87
    - type: mrr_at_3
      value: 70.5
    - type: mrr_at_5
      value: 73.05
    - type: ndcg_at_1
      value: 63.0
    - type: ndcg_at_10
      value: 78.255
    - type: ndcg_at_100
      value: 79.88
    - type: ndcg_at_1000
      value: 79.88
    - type: ndcg_at_3
      value: 72.702
    - type: ndcg_at_5
      value: 77.264
    - type: precision_at_1
      value: 63.0
    - type: precision_at_10
      value: 9.3
    - type: precision_at_100
      value: 1.0
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 26.333000000000002
    - type: precision_at_5
      value: 18.0
    - type: recall_at_1
      value: 63.0
    - type: recall_at_10
      value: 93.0
    - type: recall_at_100
      value: 100.0
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 79.0
    - type: recall_at_5
      value: 90.0
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
      value: 40.338
    - type: map_at_10
      value: 61.927
    - type: map_at_100
      value: 63.361999999999995
    - type: map_at_1000
      value: 63.405
    - type: map_at_3
      value: 55.479
    - type: map_at_5
      value: 59.732
    - type: mrr_at_1
      value: 63.551
    - type: mrr_at_10
      value: 71.006
    - type: mrr_at_100
      value: 71.501
    - type: mrr_at_1000
      value: 71.509
    - type: mrr_at_3
      value: 69.07
    - type: mrr_at_5
      value: 70.165
    - type: ndcg_at_1
      value: 63.551
    - type: ndcg_at_10
      value: 68.297
    - type: ndcg_at_100
      value: 73.13199999999999
    - type: ndcg_at_1000
      value: 73.751
    - type: ndcg_at_3
      value: 62.999
    - type: ndcg_at_5
      value: 64.89
    - type: precision_at_1
      value: 63.551
    - type: precision_at_10
      value: 15.661
    - type: precision_at_100
      value: 1.9789999999999999
    - type: precision_at_1000
      value: 0.207
    - type: precision_at_3
      value: 38.273
    - type: precision_at_5
      value: 27.61
    - type: recall_at_1
      value: 40.338
    - type: recall_at_10
      value: 77.267
    - type: recall_at_100
      value: 95.892
    - type: recall_at_1000
      value: 99.75500000000001
    - type: recall_at_3
      value: 60.36
    - type: recall_at_5
      value: 68.825
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB 8TagsClustering
      revision: None
      split: test
      type: PL-MTEB/8tags-clustering
    metrics:
    - type: v_measure
      value: 51.36126303874126
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
      value: 67.13717693836979
    - type: f1
      value: 57.27609848003782
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
      value: 35.276999999999994
    - type: map_at_10
      value: 51.086
    - type: map_at_100
      value: 51.788000000000004
    - type: map_at_1000
      value: 51.791
    - type: map_at_3
      value: 46.147
    - type: map_at_5
      value: 49.078
    - type: mrr_at_1
      value: 35.917
    - type: mrr_at_10
      value: 51.315999999999995
    - type: mrr_at_100
      value: 52.018
    - type: mrr_at_1000
      value: 52.022
    - type: mrr_at_3
      value: 46.349000000000004
    - type: mrr_at_5
      value: 49.297000000000004
    - type: ndcg_at_1
      value: 35.276999999999994
    - type: ndcg_at_10
      value: 59.870999999999995
    - type: ndcg_at_100
      value: 62.590999999999994
    - type: ndcg_at_1000
      value: 62.661
    - type: ndcg_at_3
      value: 49.745
    - type: ndcg_at_5
      value: 55.067
    - type: precision_at_1
      value: 35.276999999999994
    - type: precision_at_10
      value: 8.791
    - type: precision_at_100
      value: 0.991
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 20.057
    - type: precision_at_5
      value: 14.637
    - type: recall_at_1
      value: 35.276999999999994
    - type: recall_at_10
      value: 87.909
    - type: recall_at_100
      value: 99.14699999999999
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 60.171
    - type: recall_at_5
      value: 73.18599999999999
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
      value: 78.03000000000002
    - type: ap
      value: 29.12548553897622
    - type: f1
      value: 66.54857118886073
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
      value: 89.0
    - type: cos_sim_ap
      value: 76.75437826834582
    - type: cos_sim_f1
      value: 66.4850136239782
    - type: cos_sim_precision
      value: 68.92655367231639
    - type: cos_sim_recall
      value: 64.21052631578948
    - type: dot_accuracy
      value: 89.0
    - type: dot_ap
      value: 76.75437826834582
    - type: dot_f1
      value: 66.4850136239782
    - type: dot_precision
      value: 68.92655367231639
    - type: dot_recall
      value: 64.21052631578948
    - type: euclidean_accuracy
      value: 89.0
    - type: euclidean_ap
      value: 76.75437826834582
    - type: euclidean_f1
      value: 66.4850136239782
    - type: euclidean_precision
      value: 68.92655367231639
    - type: euclidean_recall
      value: 64.21052631578948
    - type: manhattan_accuracy
      value: 89.0
    - type: manhattan_ap
      value: 76.66074220647083
    - type: manhattan_f1
      value: 66.47058823529412
    - type: manhattan_precision
      value: 75.33333333333333
    - type: manhattan_recall
      value: 59.473684210526315
    - type: max_accuracy
      value: 89.0
    - type: max_ap
      value: 76.75437826834582
    - type: max_f1
      value: 66.4850136239782
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
      value: 93.12903172428328
    - type: cos_sim_spearman
      value: 92.66381487060741
    - type: euclidean_pearson
      value: 90.37278396708922
    - type: euclidean_spearman
      value: 92.66381487060741
    - type: manhattan_pearson
      value: 90.32503296540962
    - type: manhattan_spearman
      value: 92.6902938354313
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
      value: 8.83
    - type: map_at_10
      value: 18.326
    - type: map_at_100
      value: 26.496
    - type: map_at_1000
      value: 28.455000000000002
    - type: map_at_3
      value: 12.933
    - type: map_at_5
      value: 15.168000000000001
    - type: mrr_at_1
      value: 66.0
    - type: mrr_at_10
      value: 72.76700000000001
    - type: mrr_at_100
      value: 73.203
    - type: mrr_at_1000
      value: 73.219
    - type: mrr_at_3
      value: 71.458
    - type: mrr_at_5
      value: 72.246
    - type: ndcg_at_1
      value: 55.375
    - type: ndcg_at_10
      value: 41.3
    - type: ndcg_at_100
      value: 45.891
    - type: ndcg_at_1000
      value: 52.905
    - type: ndcg_at_3
      value: 46.472
    - type: ndcg_at_5
      value: 43.734
    - type: precision_at_1
      value: 66.0
    - type: precision_at_10
      value: 33.074999999999996
    - type: precision_at_100
      value: 11.094999999999999
    - type: precision_at_1000
      value: 2.374
    - type: precision_at_3
      value: 48.583
    - type: precision_at_5
      value: 42.0
    - type: recall_at_1
      value: 8.83
    - type: recall_at_10
      value: 22.587
    - type: recall_at_100
      value: 50.61600000000001
    - type: recall_at_1000
      value: 73.559
    - type: recall_at_3
      value: 13.688
    - type: recall_at_5
      value: 16.855
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
      value: 20.587
    - type: map_at_10
      value: 33.095
    - type: map_at_100
      value: 35.24
    - type: map_at_1000
      value: 35.429
    - type: map_at_3
      value: 28.626
    - type: map_at_5
      value: 31.136999999999997
    - type: mrr_at_1
      value: 40.586
    - type: mrr_at_10
      value: 49.033
    - type: mrr_at_100
      value: 49.952999999999996
    - type: mrr_at_1000
      value: 49.992
    - type: mrr_at_3
      value: 46.553
    - type: mrr_at_5
      value: 48.035
    - type: ndcg_at_1
      value: 40.586
    - type: ndcg_at_10
      value: 41.046
    - type: ndcg_at_100
      value: 48.586
    - type: ndcg_at_1000
      value: 51.634
    - type: ndcg_at_3
      value: 36.773
    - type: ndcg_at_5
      value: 38.389
    - type: precision_at_1
      value: 40.586
    - type: precision_at_10
      value: 11.466
    - type: precision_at_100
      value: 1.909
    - type: precision_at_1000
      value: 0.245
    - type: precision_at_3
      value: 24.434
    - type: precision_at_5
      value: 18.426000000000002
    - type: recall_at_1
      value: 20.587
    - type: recall_at_10
      value: 47.986000000000004
    - type: recall_at_100
      value: 75.761
    - type: recall_at_1000
      value: 94.065
    - type: recall_at_3
      value: 33.339
    - type: recall_at_5
      value: 39.765
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
      value: 40.878
    - type: map_at_10
      value: 58.775999999999996
    - type: map_at_100
      value: 59.632
    - type: map_at_1000
      value: 59.707
    - type: map_at_3
      value: 56.074
    - type: map_at_5
      value: 57.629
    - type: mrr_at_1
      value: 81.756
    - type: mrr_at_10
      value: 86.117
    - type: mrr_at_100
      value: 86.299
    - type: mrr_at_1000
      value: 86.30600000000001
    - type: mrr_at_3
      value: 85.345
    - type: mrr_at_5
      value: 85.832
    - type: ndcg_at_1
      value: 81.756
    - type: ndcg_at_10
      value: 67.608
    - type: ndcg_at_100
      value: 70.575
    - type: ndcg_at_1000
      value: 71.99600000000001
    - type: ndcg_at_3
      value: 63.723
    - type: ndcg_at_5
      value: 65.70700000000001
    - type: precision_at_1
      value: 81.756
    - type: precision_at_10
      value: 13.619
    - type: precision_at_100
      value: 1.5939999999999999
    - type: precision_at_1000
      value: 0.178
    - type: precision_at_3
      value: 39.604
    - type: precision_at_5
      value: 25.332
    - type: recall_at_1
      value: 40.878
    - type: recall_at_10
      value: 68.096
    - type: recall_at_100
      value: 79.696
    - type: recall_at_1000
      value: 89.082
    - type: recall_at_3
      value: 59.406000000000006
    - type: recall_at_5
      value: 63.329
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
      value: 2.1839999999999997
    - type: map_at_10
      value: 11.346
    - type: map_at_100
      value: 30.325000000000003
    - type: map_at_1000
      value: 37.806
    - type: map_at_3
      value: 4.842
    - type: map_at_5
      value: 6.891
    - type: mrr_at_1
      value: 86.047
    - type: mrr_at_10
      value: 89.14699999999999
    - type: mrr_at_100
      value: 89.46600000000001
    - type: mrr_at_1000
      value: 89.46600000000001
    - type: mrr_at_3
      value: 89.14699999999999
    - type: mrr_at_5
      value: 89.14699999999999
    - type: ndcg_at_1
      value: 67.829
    - type: ndcg_at_10
      value: 62.222
    - type: ndcg_at_100
      value: 55.337
    - type: ndcg_at_1000
      value: 64.076
    - type: ndcg_at_3
      value: 68.12700000000001
    - type: ndcg_at_5
      value: 64.987
    - type: precision_at_1
      value: 86.047
    - type: precision_at_10
      value: 69.535
    - type: precision_at_100
      value: 32.93
    - type: precision_at_1000
      value: 6.6049999999999995
    - type: precision_at_3
      value: 79.845
    - type: precision_at_5
      value: 75.349
    - type: recall_at_1
      value: 2.1839999999999997
    - type: recall_at_10
      value: 12.866
    - type: recall_at_100
      value: 43.505
    - type: recall_at_1000
      value: 72.366
    - type: recall_at_3
      value: 4.947
    - type: recall_at_5
      value: 7.192
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
      value: 80.75319435104238
    - type: f1
      value: 77.58961444860606
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
      value: 85.54472091459313
    - type: f1
      value: 84.29498563572106
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
      value: 4.367
    - type: map_at_10
      value: 10.38
    - type: map_at_100
      value: 13.516
    - type: map_at_1000
      value: 14.982000000000001
    - type: map_at_3
      value: 7.367
    - type: map_at_5
      value: 8.59
    - type: mrr_at_1
      value: 41.486000000000004
    - type: mrr_at_10
      value: 48.886
    - type: mrr_at_100
      value: 49.657000000000004
    - type: mrr_at_1000
      value: 49.713
    - type: mrr_at_3
      value: 46.904
    - type: mrr_at_5
      value: 48.065000000000005
    - type: ndcg_at_1
      value: 40.402
    - type: ndcg_at_10
      value: 30.885
    - type: ndcg_at_100
      value: 28.393
    - type: ndcg_at_1000
      value: 37.428
    - type: ndcg_at_3
      value: 35.394999999999996
    - type: ndcg_at_5
      value: 33.391999999999996
    - type: precision_at_1
      value: 41.486000000000004
    - type: precision_at_10
      value: 23.437
    - type: precision_at_100
      value: 7.638
    - type: precision_at_1000
      value: 2.0389999999999997
    - type: precision_at_3
      value: 32.817
    - type: precision_at_5
      value: 28.915999999999997
    - type: recall_at_1
      value: 4.367
    - type: recall_at_10
      value: 14.655000000000001
    - type: recall_at_100
      value: 29.665999999999997
    - type: recall_at_1000
      value: 62.073
    - type: recall_at_3
      value: 8.51
    - type: recall_at_5
      value: 10.689
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
      value: 28.616000000000003
    - type: map_at_10
      value: 41.626000000000005
    - type: map_at_100
      value: 42.689
    - type: map_at_1000
      value: 42.733
    - type: map_at_3
      value: 37.729
    - type: map_at_5
      value: 39.879999999999995
    - type: mrr_at_1
      value: 32.068000000000005
    - type: mrr_at_10
      value: 44.029
    - type: mrr_at_100
      value: 44.87
    - type: mrr_at_1000
      value: 44.901
    - type: mrr_at_3
      value: 40.687
    - type: mrr_at_5
      value: 42.625
    - type: ndcg_at_1
      value: 32.068000000000005
    - type: ndcg_at_10
      value: 48.449999999999996
    - type: ndcg_at_100
      value: 53.13
    - type: ndcg_at_1000
      value: 54.186
    - type: ndcg_at_3
      value: 40.983999999999995
    - type: ndcg_at_5
      value: 44.628
    - type: precision_at_1
      value: 32.068000000000005
    - type: precision_at_10
      value: 7.9750000000000005
    - type: precision_at_100
      value: 1.061
    - type: precision_at_1000
      value: 0.116
    - type: precision_at_3
      value: 18.404999999999998
    - type: precision_at_5
      value: 13.111
    - type: recall_at_1
      value: 28.616000000000003
    - type: recall_at_10
      value: 66.956
    - type: recall_at_100
      value: 87.657
    - type: recall_at_1000
      value: 95.548
    - type: recall_at_3
      value: 47.453
    - type: recall_at_5
      value: 55.87800000000001
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
      value: 77.47589122111044
    - type: f1
      value: 66.6332277374775
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
      value: 86.4
    - type: cos_sim_ap
      value: 94.1044939667201
    - type: cos_sim_f1
      value: 88.78048780487805
    - type: cos_sim_precision
      value: 87.22044728434504
    - type: cos_sim_recall
      value: 90.39735099337747
    - type: dot_accuracy
      value: 86.4
    - type: dot_ap
      value: 94.1044939667201
    - type: dot_f1
      value: 88.78048780487805
    - type: dot_precision
      value: 87.22044728434504
    - type: dot_recall
      value: 90.39735099337747
    - type: euclidean_accuracy
      value: 86.4
    - type: euclidean_ap
      value: 94.1044939667201
    - type: euclidean_f1
      value: 88.78048780487805
    - type: euclidean_precision
      value: 87.22044728434504
    - type: euclidean_recall
      value: 90.39735099337747
    - type: manhattan_accuracy
      value: 86.4
    - type: manhattan_ap
      value: 94.11438365697387
    - type: manhattan_f1
      value: 88.77968877968877
    - type: manhattan_precision
      value: 87.84440842787681
    - type: manhattan_recall
      value: 89.73509933774835
    - type: max_accuracy
      value: 86.4
    - type: max_ap
      value: 94.11438365697387
    - type: max_f1
      value: 88.78048780487805
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
      value: 97.86641929499072
    - type: cos_sim_ap
      value: 99.36904211868182
    - type: cos_sim_f1
      value: 96.56203288490283
    - type: cos_sim_precision
      value: 94.72140762463343
    - type: cos_sim_recall
      value: 98.47560975609755
    - type: dot_accuracy
      value: 97.86641929499072
    - type: dot_ap
      value: 99.36904211868183
    - type: dot_f1
      value: 96.56203288490283
    - type: dot_precision
      value: 94.72140762463343
    - type: dot_recall
      value: 98.47560975609755
    - type: euclidean_accuracy
      value: 97.86641929499072
    - type: euclidean_ap
      value: 99.36904211868183
    - type: euclidean_f1
      value: 96.56203288490283
    - type: euclidean_precision
      value: 94.72140762463343
    - type: euclidean_recall
      value: 98.47560975609755
    - type: manhattan_accuracy
      value: 98.14471243042672
    - type: manhattan_ap
      value: 99.43359540492416
    - type: manhattan_f1
      value: 96.98795180722892
    - type: manhattan_precision
      value: 95.83333333333334
    - type: manhattan_recall
      value: 98.17073170731707
    - type: max_accuracy
      value: 98.14471243042672
    - type: max_ap
      value: 99.43359540492416
    - type: max_f1
      value: 96.98795180722892
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
      value: 89.39058171745152
    - type: f1
      value: 86.8552093529568
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
      value: 74.97975708502024
    - type: f1
      value: 58.73081628832407
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
      value: 64.917
    - type: map_at_10
      value: 78.74600000000001
    - type: map_at_100
      value: 79.501
    - type: map_at_1000
      value: 79.524
    - type: map_at_3
      value: 75.549
    - type: map_at_5
      value: 77.495
    - type: mrr_at_1
      value: 74.9
    - type: mrr_at_10
      value: 82.112
    - type: mrr_at_100
      value: 82.314
    - type: mrr_at_1000
      value: 82.317
    - type: mrr_at_3
      value: 80.745
    - type: mrr_at_5
      value: 81.607
    - type: ndcg_at_1
      value: 74.83999999999999
    - type: ndcg_at_10
      value: 83.214
    - type: ndcg_at_100
      value: 84.997
    - type: ndcg_at_1000
      value: 85.207
    - type: ndcg_at_3
      value: 79.547
    - type: ndcg_at_5
      value: 81.46600000000001
    - type: precision_at_1
      value: 74.83999999999999
    - type: precision_at_10
      value: 12.822
    - type: precision_at_100
      value: 1.506
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 34.903
    - type: precision_at_5
      value: 23.16
    - type: recall_at_1
      value: 64.917
    - type: recall_at_10
      value: 92.27199999999999
    - type: recall_at_100
      value: 98.715
    - type: recall_at_1000
      value: 99.854
    - type: recall_at_3
      value: 82.04599999999999
    - type: recall_at_5
      value: 87.2
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
      value: 3.51
    - type: map_at_10
      value: 9.046999999999999
    - type: map_at_100
      value: 10.823
    - type: map_at_1000
      value: 11.144
    - type: map_at_3
      value: 6.257
    - type: map_at_5
      value: 7.648000000000001
    - type: mrr_at_1
      value: 17.299999999999997
    - type: mrr_at_10
      value: 27.419
    - type: mrr_at_100
      value: 28.618
    - type: mrr_at_1000
      value: 28.685
    - type: mrr_at_3
      value: 23.817
    - type: mrr_at_5
      value: 25.927
    - type: ndcg_at_1
      value: 17.299999999999997
    - type: ndcg_at_10
      value: 16.084
    - type: ndcg_at_100
      value: 23.729
    - type: ndcg_at_1000
      value: 29.476999999999997
    - type: ndcg_at_3
      value: 14.327000000000002
    - type: ndcg_at_5
      value: 13.017999999999999
    - type: precision_at_1
      value: 17.299999999999997
    - type: precision_at_10
      value: 8.63
    - type: precision_at_100
      value: 1.981
    - type: precision_at_1000
      value: 0.336
    - type: precision_at_3
      value: 13.4
    - type: precision_at_5
      value: 11.700000000000001
    - type: recall_at_1
      value: 3.51
    - type: recall_at_10
      value: 17.518
    - type: recall_at_100
      value: 40.275
    - type: recall_at_1000
      value: 68.203
    - type: recall_at_3
      value: 8.155
    - type: recall_at_5
      value: 11.875
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
      value: 86.30248675091724
    - type: cos_sim_ap
      value: 83.6756734006714
    - type: cos_sim_f1
      value: 74.97367497367497
    - type: cos_sim_precision
      value: 73.91003460207612
    - type: cos_sim_recall
      value: 76.06837606837607
    - type: dot_accuracy
      value: 86.30248675091724
    - type: dot_ap
      value: 83.6756734006714
    - type: dot_f1
      value: 74.97367497367497
    - type: dot_precision
      value: 73.91003460207612
    - type: dot_recall
      value: 76.06837606837607
    - type: euclidean_accuracy
      value: 86.30248675091724
    - type: euclidean_ap
      value: 83.67566984333091
    - type: euclidean_f1
      value: 74.97367497367497
    - type: euclidean_precision
      value: 73.91003460207612
    - type: euclidean_recall
      value: 76.06837606837607
    - type: manhattan_accuracy
      value: 86.28210354667753
    - type: manhattan_ap
      value: 83.64216119130171
    - type: manhattan_f1
      value: 74.92152075340078
    - type: manhattan_precision
      value: 73.4107997265892
    - type: manhattan_recall
      value: 76.49572649572649
    - type: max_accuracy
      value: 86.30248675091724
    - type: max_ap
      value: 83.6756734006714
    - type: max_f1
      value: 74.97367497367497
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
      value: 82.23295940859121
    - type: cos_sim_spearman
      value: 78.89329160768719
    - type: euclidean_pearson
      value: 79.56019107076818
    - type: euclidean_spearman
      value: 78.89330209904084
    - type: manhattan_pearson
      value: 79.76098513973719
    - type: manhattan_spearman
      value: 79.05490162570123
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
      value: 37.732606308062486
    - type: cos_sim_spearman
      value: 41.01645667030284
    - type: euclidean_pearson
      value: 26.61722556367085
    - type: euclidean_spearman
      value: 41.01645667030284
    - type: manhattan_pearson
      value: 26.60917378970807
    - type: manhattan_spearman
      value: 41.51335727617614
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
      value: 54.31700000000001
    - type: map_at_10
      value: 65.564
    - type: map_at_100
      value: 66.062
    - type: map_at_1000
      value: 66.08699999999999
    - type: map_at_3
      value: 62.592999999999996
    - type: map_at_5
      value: 63.888
    - type: mrr_at_1
      value: 56.99999999999999
    - type: mrr_at_10
      value: 66.412
    - type: mrr_at_100
      value: 66.85900000000001
    - type: mrr_at_1000
      value: 66.88
    - type: mrr_at_3
      value: 64.22200000000001
    - type: mrr_at_5
      value: 65.206
    - type: ndcg_at_1
      value: 56.99999999999999
    - type: ndcg_at_10
      value: 70.577
    - type: ndcg_at_100
      value: 72.879
    - type: ndcg_at_1000
      value: 73.45
    - type: ndcg_at_3
      value: 65.5
    - type: ndcg_at_5
      value: 67.278
    - type: precision_at_1
      value: 56.99999999999999
    - type: precision_at_10
      value: 9.667
    - type: precision_at_100
      value: 1.083
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 26.0
    - type: precision_at_5
      value: 16.933
    - type: recall_at_1
      value: 54.31700000000001
    - type: recall_at_10
      value: 85.056
    - type: recall_at_100
      value: 95.667
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 71.0
    - type: recall_at_5
      value: 75.672
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
      value: 0.245
    - type: map_at_10
      value: 2.051
    - type: map_at_100
      value: 12.009
    - type: map_at_1000
      value: 27.448
    - type: map_at_3
      value: 0.721
    - type: map_at_5
      value: 1.13
    - type: mrr_at_1
      value: 88.0
    - type: mrr_at_10
      value: 93.0
    - type: mrr_at_100
      value: 93.0
    - type: mrr_at_1000
      value: 93.0
    - type: mrr_at_3
      value: 93.0
    - type: mrr_at_5
      value: 93.0
    - type: ndcg_at_1
      value: 85.0
    - type: ndcg_at_10
      value: 80.303
    - type: ndcg_at_100
      value: 61.23499999999999
    - type: ndcg_at_1000
      value: 52.978
    - type: ndcg_at_3
      value: 84.419
    - type: ndcg_at_5
      value: 82.976
    - type: precision_at_1
      value: 88.0
    - type: precision_at_10
      value: 83.39999999999999
    - type: precision_at_100
      value: 61.96
    - type: precision_at_1000
      value: 22.648
    - type: precision_at_3
      value: 89.333
    - type: precision_at_5
      value: 87.2
    - type: recall_at_1
      value: 0.245
    - type: recall_at_10
      value: 2.193
    - type: recall_at_100
      value: 14.938
    - type: recall_at_1000
      value: 48.563
    - type: recall_at_3
      value: 0.738
    - type: recall_at_5
      value: 1.173
    task:
      type: Retrieval
---

## gte-Qwen2-7B-instruct

**gte-Qwen2-7B-instruct** is the latest model in the gte (General Text Embedding) model family that ranks **No.1** in both English and Chinese evaluations on the Massive Text Embedding Benchmark [MTEB benchmark](https://huggingface.co/spaces/mteb/leaderboard) (as of June 16, 2024).

Recently, the [**Qwen team**](https://huggingface.co/Qwen) released the Qwen2 series models, and we have trained the **gte-Qwen2-7B-instruct** model based on the [Qwen2-7B](https://huggingface.co/Qwen/Qwen2-7B) LLM model. Compared to the [gte-Qwen1.5-7B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen1.5-7B-instruct) model, the **gte-Qwen2-7B-instruct** model uses the same training data and training strategies during the finetuning stage, with the only difference being the upgraded base model to Qwen2-7B. Considering the improvements in the Qwen2 series models compared to the Qwen1.5 series, we can also expect consistent performance enhancements in the embedding models.

The model incorporates several key advancements:

- Integration of bidirectional attention mechanisms, enriching its contextual understanding.
- Instruction tuning, applied solely on the query side for streamlined efficiency
- Comprehensive training across a vast, multilingual text corpus spanning diverse domains and scenarios. This training leverages both weakly supervised and supervised data, ensuring the model's applicability across numerous languages and a wide array of downstream tasks.


## Model Information
- Model Size: 7B
- Embedding Dimension: 3584
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

model = SentenceTransformer("Alibaba-NLP/gte-Qwen2-7B-instruct", trust_remote_code=True)
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

tokenizer = AutoTokenizer.from_pretrained('Alibaba-NLP/gte-Qwen2-7B-instruct', trust_remote_code=True)
model = AutoModel.from_pretrained('Alibaba-NLP/gte-Qwen2-7B-instruct', trust_remote_code=True)

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

You can use the [scripts/eval_mteb.py](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct/blob/main/scripts/eval_mteb.py) to reproduce the following result of **gte-Qwen2-7B-instruct** on MTEB(English)/C-MTEB(Chinese):

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
| gte-Qwen2-1.5B-instruc(https://huggingface.co/Alibaba-NLP/gte-Qwen2-1.5B-instruct) | 67.16 | 67.65  | 66.60 | 64.04 |

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