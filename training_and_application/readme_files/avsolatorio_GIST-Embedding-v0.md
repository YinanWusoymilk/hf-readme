---
language:
- en
library_name: sentence-transformers
license: mit
pipeline_tag: sentence-similarity
tags:
  - feature-extraction
  - mteb
  - sentence-similarity
  - sentence-transformers

model-index:
- name: GIST-Embedding-v0
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
      value: 75.95522388059702
    - type: ap
      value: 38.940434354439276
    - type: f1
      value: 69.88686275888114
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
      value: 93.51357499999999
    - type: ap
      value: 90.30414241486682
    - type: f1
      value: 93.50552829047328
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
      value: 50.446000000000005
    - type: f1
      value: 49.76432659699279
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
      value: 38.265
    - type: map_at_10
      value: 54.236
    - type: map_at_100
      value: 54.81399999999999
    - type: map_at_1000
      value: 54.81700000000001
    - type: map_at_3
      value: 49.881
    - type: map_at_5
      value: 52.431000000000004
    - type: mrr_at_1
      value: 38.265
    - type: mrr_at_10
      value: 54.152
    - type: mrr_at_100
      value: 54.730000000000004
    - type: mrr_at_1000
      value: 54.733
    - type: mrr_at_3
      value: 49.644
    - type: mrr_at_5
      value: 52.32599999999999
    - type: ndcg_at_1
      value: 38.265
    - type: ndcg_at_10
      value: 62.62
    - type: ndcg_at_100
      value: 64.96600000000001
    - type: ndcg_at_1000
      value: 65.035
    - type: ndcg_at_3
      value: 53.691
    - type: ndcg_at_5
      value: 58.303000000000004
    - type: precision_at_1
      value: 38.265
    - type: precision_at_10
      value: 8.919
    - type: precision_at_100
      value: 0.991
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 21.573999999999998
    - type: precision_at_5
      value: 15.192
    - type: recall_at_1
      value: 38.265
    - type: recall_at_10
      value: 89.189
    - type: recall_at_100
      value: 99.14699999999999
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 64.723
    - type: recall_at_5
      value: 75.96000000000001
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
      value: 48.287087887491744
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
      value: 42.74244928943812
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
      value: 62.68814324295771
    - type: mrr
      value: 75.46266983247591
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
      value: 90.45240209600391
    - type: cos_sim_spearman
      value: 87.95079919934645
    - type: euclidean_pearson
      value: 88.93438602492702
    - type: euclidean_spearman
      value: 88.28152962682988
    - type: manhattan_pearson
      value: 88.92193964325268
    - type: manhattan_spearman
      value: 88.21466063329498
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (de-en)
      config: de-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: accuracy
      value: 15.605427974947808
    - type: f1
      value: 14.989877233698866
    - type: precision
      value: 14.77906814441261
    - type: recall
      value: 15.605427974947808
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (fr-en)
      config: fr-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: accuracy
      value: 33.38102575390711
    - type: f1
      value: 32.41704114719127
    - type: precision
      value: 32.057363829835964
    - type: recall
      value: 33.38102575390711
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (ru-en)
      config: ru-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: accuracy
      value: 0.1939729823346034
    - type: f1
      value: 0.17832215223820772
    - type: precision
      value: 0.17639155671715423
    - type: recall
      value: 0.1939729823346034
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (zh-en)
      config: zh-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: accuracy
      value: 3.0542390731964195
    - type: f1
      value: 2.762857644374232
    - type: precision
      value: 2.6505178163945935
    - type: recall
      value: 3.0542390731964195
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
      value: 87.29545454545453
    - type: f1
      value: 87.26415991342238
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
      value: 39.035319537839484
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
      value: 36.667313307057285
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
      value: 33.979
    - type: map_at_10
      value: 46.275
    - type: map_at_100
      value: 47.975
    - type: map_at_1000
      value: 48.089
    - type: map_at_3
      value: 42.507
    - type: map_at_5
      value: 44.504
    - type: mrr_at_1
      value: 42.346000000000004
    - type: mrr_at_10
      value: 53.013
    - type: mrr_at_100
      value: 53.717000000000006
    - type: mrr_at_1000
      value: 53.749
    - type: mrr_at_3
      value: 50.405
    - type: mrr_at_5
      value: 51.915
    - type: ndcg_at_1
      value: 42.346000000000004
    - type: ndcg_at_10
      value: 53.179
    - type: ndcg_at_100
      value: 58.458
    - type: ndcg_at_1000
      value: 60.057
    - type: ndcg_at_3
      value: 48.076
    - type: ndcg_at_5
      value: 50.283
    - type: precision_at_1
      value: 42.346000000000004
    - type: precision_at_10
      value: 10.386
    - type: precision_at_100
      value: 1.635
    - type: precision_at_1000
      value: 0.20600000000000002
    - type: precision_at_3
      value: 23.413999999999998
    - type: precision_at_5
      value: 16.624
    - type: recall_at_1
      value: 33.979
    - type: recall_at_10
      value: 65.553
    - type: recall_at_100
      value: 87.18599999999999
    - type: recall_at_1000
      value: 97.25200000000001
    - type: recall_at_3
      value: 50.068999999999996
    - type: recall_at_5
      value: 56.882
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
      value: 31.529
    - type: map_at_10
      value: 42.219
    - type: map_at_100
      value: 43.408
    - type: map_at_1000
      value: 43.544
    - type: map_at_3
      value: 39.178000000000004
    - type: map_at_5
      value: 40.87
    - type: mrr_at_1
      value: 39.873
    - type: mrr_at_10
      value: 48.25
    - type: mrr_at_100
      value: 48.867
    - type: mrr_at_1000
      value: 48.908
    - type: mrr_at_3
      value: 46.03
    - type: mrr_at_5
      value: 47.355000000000004
    - type: ndcg_at_1
      value: 39.873
    - type: ndcg_at_10
      value: 47.933
    - type: ndcg_at_100
      value: 52.156000000000006
    - type: ndcg_at_1000
      value: 54.238
    - type: ndcg_at_3
      value: 43.791999999999994
    - type: ndcg_at_5
      value: 45.678999999999995
    - type: precision_at_1
      value: 39.873
    - type: precision_at_10
      value: 9.032
    - type: precision_at_100
      value: 1.419
    - type: precision_at_1000
      value: 0.192
    - type: precision_at_3
      value: 21.231
    - type: precision_at_5
      value: 14.981
    - type: recall_at_1
      value: 31.529
    - type: recall_at_10
      value: 57.925000000000004
    - type: recall_at_100
      value: 75.89
    - type: recall_at_1000
      value: 89.007
    - type: recall_at_3
      value: 45.363
    - type: recall_at_5
      value: 50.973
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
      value: 41.289
    - type: map_at_10
      value: 54.494
    - type: map_at_100
      value: 55.494
    - type: map_at_1000
      value: 55.545
    - type: map_at_3
      value: 51.20099999999999
    - type: map_at_5
      value: 53.147
    - type: mrr_at_1
      value: 47.335
    - type: mrr_at_10
      value: 57.772
    - type: mrr_at_100
      value: 58.428000000000004
    - type: mrr_at_1000
      value: 58.453
    - type: mrr_at_3
      value: 55.434000000000005
    - type: mrr_at_5
      value: 56.8
    - type: ndcg_at_1
      value: 47.335
    - type: ndcg_at_10
      value: 60.382999999999996
    - type: ndcg_at_100
      value: 64.294
    - type: ndcg_at_1000
      value: 65.211
    - type: ndcg_at_3
      value: 55.098
    - type: ndcg_at_5
      value: 57.776
    - type: precision_at_1
      value: 47.335
    - type: precision_at_10
      value: 9.724
    - type: precision_at_100
      value: 1.26
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_3
      value: 24.786
    - type: precision_at_5
      value: 16.977999999999998
    - type: recall_at_1
      value: 41.289
    - type: recall_at_10
      value: 74.36399999999999
    - type: recall_at_100
      value: 91.19800000000001
    - type: recall_at_1000
      value: 97.508
    - type: recall_at_3
      value: 60.285
    - type: recall_at_5
      value: 66.814
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
      value: 28.816999999999997
    - type: map_at_10
      value: 37.856
    - type: map_at_100
      value: 38.824
    - type: map_at_1000
      value: 38.902
    - type: map_at_3
      value: 34.982
    - type: map_at_5
      value: 36.831
    - type: mrr_at_1
      value: 31.073
    - type: mrr_at_10
      value: 39.985
    - type: mrr_at_100
      value: 40.802
    - type: mrr_at_1000
      value: 40.861999999999995
    - type: mrr_at_3
      value: 37.419999999999995
    - type: mrr_at_5
      value: 39.104
    - type: ndcg_at_1
      value: 31.073
    - type: ndcg_at_10
      value: 42.958
    - type: ndcg_at_100
      value: 47.671
    - type: ndcg_at_1000
      value: 49.633
    - type: ndcg_at_3
      value: 37.602000000000004
    - type: ndcg_at_5
      value: 40.688
    - type: precision_at_1
      value: 31.073
    - type: precision_at_10
      value: 6.531000000000001
    - type: precision_at_100
      value: 0.932
    - type: precision_at_1000
      value: 0.11399999999999999
    - type: precision_at_3
      value: 15.857
    - type: precision_at_5
      value: 11.209
    - type: recall_at_1
      value: 28.816999999999997
    - type: recall_at_10
      value: 56.538999999999994
    - type: recall_at_100
      value: 78.17699999999999
    - type: recall_at_1000
      value: 92.92200000000001
    - type: recall_at_3
      value: 42.294
    - type: recall_at_5
      value: 49.842999999999996
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
      value: 18.397
    - type: map_at_10
      value: 27.256999999999998
    - type: map_at_100
      value: 28.541
    - type: map_at_1000
      value: 28.658
    - type: map_at_3
      value: 24.565
    - type: map_at_5
      value: 26.211000000000002
    - type: mrr_at_1
      value: 22.761
    - type: mrr_at_10
      value: 32.248
    - type: mrr_at_100
      value: 33.171
    - type: mrr_at_1000
      value: 33.227000000000004
    - type: mrr_at_3
      value: 29.498
    - type: mrr_at_5
      value: 31.246000000000002
    - type: ndcg_at_1
      value: 22.761
    - type: ndcg_at_10
      value: 32.879999999999995
    - type: ndcg_at_100
      value: 38.913
    - type: ndcg_at_1000
      value: 41.504999999999995
    - type: ndcg_at_3
      value: 27.988000000000003
    - type: ndcg_at_5
      value: 30.548
    - type: precision_at_1
      value: 22.761
    - type: precision_at_10
      value: 6.045
    - type: precision_at_100
      value: 1.044
    - type: precision_at_1000
      value: 0.13999999999999999
    - type: precision_at_3
      value: 13.433
    - type: precision_at_5
      value: 9.925
    - type: recall_at_1
      value: 18.397
    - type: recall_at_10
      value: 45.14
    - type: recall_at_100
      value: 71.758
    - type: recall_at_1000
      value: 89.854
    - type: recall_at_3
      value: 31.942999999999998
    - type: recall_at_5
      value: 38.249
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
      value: 30.604
    - type: map_at_10
      value: 42.132
    - type: map_at_100
      value: 43.419000000000004
    - type: map_at_1000
      value: 43.527
    - type: map_at_3
      value: 38.614
    - type: map_at_5
      value: 40.705000000000005
    - type: mrr_at_1
      value: 37.824999999999996
    - type: mrr_at_10
      value: 47.696
    - type: mrr_at_100
      value: 48.483
    - type: mrr_at_1000
      value: 48.53
    - type: mrr_at_3
      value: 45.123999999999995
    - type: mrr_at_5
      value: 46.635
    - type: ndcg_at_1
      value: 37.824999999999996
    - type: ndcg_at_10
      value: 48.421
    - type: ndcg_at_100
      value: 53.568000000000005
    - type: ndcg_at_1000
      value: 55.574999999999996
    - type: ndcg_at_3
      value: 42.89
    - type: ndcg_at_5
      value: 45.683
    - type: precision_at_1
      value: 37.824999999999996
    - type: precision_at_10
      value: 8.758000000000001
    - type: precision_at_100
      value: 1.319
    - type: precision_at_1000
      value: 0.168
    - type: precision_at_3
      value: 20.244
    - type: precision_at_5
      value: 14.533
    - type: recall_at_1
      value: 30.604
    - type: recall_at_10
      value: 61.605
    - type: recall_at_100
      value: 82.787
    - type: recall_at_1000
      value: 95.78
    - type: recall_at_3
      value: 46.303
    - type: recall_at_5
      value: 53.351000000000006
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
      value: 26.262999999999998
    - type: map_at_10
      value: 36.858999999999995
    - type: map_at_100
      value: 38.241
    - type: map_at_1000
      value: 38.346999999999994
    - type: map_at_3
      value: 33.171
    - type: map_at_5
      value: 35.371
    - type: mrr_at_1
      value: 32.42
    - type: mrr_at_10
      value: 42.361
    - type: mrr_at_100
      value: 43.219
    - type: mrr_at_1000
      value: 43.271
    - type: mrr_at_3
      value: 39.593
    - type: mrr_at_5
      value: 41.248000000000005
    - type: ndcg_at_1
      value: 32.42
    - type: ndcg_at_10
      value: 43.081
    - type: ndcg_at_100
      value: 48.837
    - type: ndcg_at_1000
      value: 50.954
    - type: ndcg_at_3
      value: 37.413000000000004
    - type: ndcg_at_5
      value: 40.239000000000004
    - type: precision_at_1
      value: 32.42
    - type: precision_at_10
      value: 8.071
    - type: precision_at_100
      value: 1.272
    - type: precision_at_1000
      value: 0.163
    - type: precision_at_3
      value: 17.922
    - type: precision_at_5
      value: 13.311
    - type: recall_at_1
      value: 26.262999999999998
    - type: recall_at_10
      value: 56.062999999999995
    - type: recall_at_100
      value: 80.636
    - type: recall_at_1000
      value: 94.707
    - type: recall_at_3
      value: 40.425
    - type: recall_at_5
      value: 47.663
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
      value: 27.86616666666667
    - type: map_at_10
      value: 37.584999999999994
    - type: map_at_100
      value: 38.80291666666667
    - type: map_at_1000
      value: 38.91358333333333
    - type: map_at_3
      value: 34.498
    - type: map_at_5
      value: 36.269999999999996
    - type: mrr_at_1
      value: 33.07566666666667
    - type: mrr_at_10
      value: 41.92366666666666
    - type: mrr_at_100
      value: 42.73516666666667
    - type: mrr_at_1000
      value: 42.785666666666664
    - type: mrr_at_3
      value: 39.39075
    - type: mrr_at_5
      value: 40.89133333333334
    - type: ndcg_at_1
      value: 33.07566666666667
    - type: ndcg_at_10
      value: 43.19875
    - type: ndcg_at_100
      value: 48.32083333333334
    - type: ndcg_at_1000
      value: 50.418000000000006
    - type: ndcg_at_3
      value: 38.10308333333333
    - type: ndcg_at_5
      value: 40.5985
    - type: precision_at_1
      value: 33.07566666666667
    - type: precision_at_10
      value: 7.581916666666666
    - type: precision_at_100
      value: 1.1975
    - type: precision_at_1000
      value: 0.15699999999999997
    - type: precision_at_3
      value: 17.49075
    - type: precision_at_5
      value: 12.5135
    - type: recall_at_1
      value: 27.86616666666667
    - type: recall_at_10
      value: 55.449749999999995
    - type: recall_at_100
      value: 77.92516666666666
    - type: recall_at_1000
      value: 92.31358333333333
    - type: recall_at_3
      value: 41.324416666666664
    - type: recall_at_5
      value: 47.72533333333333
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
      value: 26.648
    - type: map_at_10
      value: 33.155
    - type: map_at_100
      value: 34.149
    - type: map_at_1000
      value: 34.239000000000004
    - type: map_at_3
      value: 30.959999999999997
    - type: map_at_5
      value: 32.172
    - type: mrr_at_1
      value: 30.061
    - type: mrr_at_10
      value: 36.229
    - type: mrr_at_100
      value: 37.088
    - type: mrr_at_1000
      value: 37.15
    - type: mrr_at_3
      value: 34.254
    - type: mrr_at_5
      value: 35.297
    - type: ndcg_at_1
      value: 30.061
    - type: ndcg_at_10
      value: 37.247
    - type: ndcg_at_100
      value: 42.093
    - type: ndcg_at_1000
      value: 44.45
    - type: ndcg_at_3
      value: 33.211
    - type: ndcg_at_5
      value: 35.083999999999996
    - type: precision_at_1
      value: 30.061
    - type: precision_at_10
      value: 5.7059999999999995
    - type: precision_at_100
      value: 0.8880000000000001
    - type: precision_at_1000
      value: 0.116
    - type: precision_at_3
      value: 13.957
    - type: precision_at_5
      value: 9.663
    - type: recall_at_1
      value: 26.648
    - type: recall_at_10
      value: 46.85
    - type: recall_at_100
      value: 68.87
    - type: recall_at_1000
      value: 86.508
    - type: recall_at_3
      value: 35.756
    - type: recall_at_5
      value: 40.376
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
      value: 19.058
    - type: map_at_10
      value: 26.722
    - type: map_at_100
      value: 27.863
    - type: map_at_1000
      value: 27.988000000000003
    - type: map_at_3
      value: 24.258
    - type: map_at_5
      value: 25.531
    - type: mrr_at_1
      value: 23.09
    - type: mrr_at_10
      value: 30.711
    - type: mrr_at_100
      value: 31.628
    - type: mrr_at_1000
      value: 31.702
    - type: mrr_at_3
      value: 28.418
    - type: mrr_at_5
      value: 29.685
    - type: ndcg_at_1
      value: 23.09
    - type: ndcg_at_10
      value: 31.643
    - type: ndcg_at_100
      value: 37.047999999999995
    - type: ndcg_at_1000
      value: 39.896
    - type: ndcg_at_3
      value: 27.189999999999998
    - type: ndcg_at_5
      value: 29.112
    - type: precision_at_1
      value: 23.09
    - type: precision_at_10
      value: 5.743
    - type: precision_at_100
      value: 1
    - type: precision_at_1000
      value: 0.14300000000000002
    - type: precision_at_3
      value: 12.790000000000001
    - type: precision_at_5
      value: 9.195
    - type: recall_at_1
      value: 19.058
    - type: recall_at_10
      value: 42.527
    - type: recall_at_100
      value: 66.833
    - type: recall_at_1000
      value: 87.008
    - type: recall_at_3
      value: 29.876
    - type: recall_at_5
      value: 34.922
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
      value: 28.066999999999997
    - type: map_at_10
      value: 37.543
    - type: map_at_100
      value: 38.725
    - type: map_at_1000
      value: 38.815
    - type: map_at_3
      value: 34.488
    - type: map_at_5
      value: 36.222
    - type: mrr_at_1
      value: 33.116
    - type: mrr_at_10
      value: 41.743
    - type: mrr_at_100
      value: 42.628
    - type: mrr_at_1000
      value: 42.675999999999995
    - type: mrr_at_3
      value: 39.241
    - type: mrr_at_5
      value: 40.622
    - type: ndcg_at_1
      value: 33.116
    - type: ndcg_at_10
      value: 43.089
    - type: ndcg_at_100
      value: 48.61
    - type: ndcg_at_1000
      value: 50.585
    - type: ndcg_at_3
      value: 37.816
    - type: ndcg_at_5
      value: 40.256
    - type: precision_at_1
      value: 33.116
    - type: precision_at_10
      value: 7.313
    - type: precision_at_100
      value: 1.1320000000000001
    - type: precision_at_1000
      value: 0.14200000000000002
    - type: precision_at_3
      value: 17.102
    - type: precision_at_5
      value: 12.09
    - type: recall_at_1
      value: 28.066999999999997
    - type: recall_at_10
      value: 55.684
    - type: recall_at_100
      value: 80.092
    - type: recall_at_1000
      value: 93.605
    - type: recall_at_3
      value: 41.277
    - type: recall_at_5
      value: 47.46
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
      value: 27.094
    - type: map_at_10
      value: 35.939
    - type: map_at_100
      value: 37.552
    - type: map_at_1000
      value: 37.771
    - type: map_at_3
      value: 32.414
    - type: map_at_5
      value: 34.505
    - type: mrr_at_1
      value: 32.609
    - type: mrr_at_10
      value: 40.521
    - type: mrr_at_100
      value: 41.479
    - type: mrr_at_1000
      value: 41.524
    - type: mrr_at_3
      value: 37.451
    - type: mrr_at_5
      value: 39.387
    - type: ndcg_at_1
      value: 32.609
    - type: ndcg_at_10
      value: 41.83
    - type: ndcg_at_100
      value: 47.763
    - type: ndcg_at_1000
      value: 50.102999999999994
    - type: ndcg_at_3
      value: 36.14
    - type: ndcg_at_5
      value: 39.153999999999996
    - type: precision_at_1
      value: 32.609
    - type: precision_at_10
      value: 7.925
    - type: precision_at_100
      value: 1.591
    - type: precision_at_1000
      value: 0.246
    - type: precision_at_3
      value: 16.337
    - type: precision_at_5
      value: 12.411
    - type: recall_at_1
      value: 27.094
    - type: recall_at_10
      value: 53.32900000000001
    - type: recall_at_100
      value: 79.52
    - type: recall_at_1000
      value: 93.958
    - type: recall_at_3
      value: 37.773
    - type: recall_at_5
      value: 45.321
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
      value: 22.649
    - type: map_at_10
      value: 30.569000000000003
    - type: map_at_100
      value: 31.444
    - type: map_at_1000
      value: 31.538
    - type: map_at_3
      value: 27.638
    - type: map_at_5
      value: 29.171000000000003
    - type: mrr_at_1
      value: 24.399
    - type: mrr_at_10
      value: 32.555
    - type: mrr_at_100
      value: 33.312000000000005
    - type: mrr_at_1000
      value: 33.376
    - type: mrr_at_3
      value: 29.820999999999998
    - type: mrr_at_5
      value: 31.402
    - type: ndcg_at_1
      value: 24.399
    - type: ndcg_at_10
      value: 35.741
    - type: ndcg_at_100
      value: 40.439
    - type: ndcg_at_1000
      value: 42.809000000000005
    - type: ndcg_at_3
      value: 30.020999999999997
    - type: ndcg_at_5
      value: 32.68
    - type: precision_at_1
      value: 24.399
    - type: precision_at_10
      value: 5.749
    - type: precision_at_100
      value: 0.878
    - type: precision_at_1000
      value: 0.117
    - type: precision_at_3
      value: 12.815999999999999
    - type: precision_at_5
      value: 9.242
    - type: recall_at_1
      value: 22.649
    - type: recall_at_10
      value: 49.818
    - type: recall_at_100
      value: 72.155
    - type: recall_at_1000
      value: 89.654
    - type: recall_at_3
      value: 34.528999999999996
    - type: recall_at_5
      value: 40.849999999999994
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
      value: 13.587
    - type: map_at_10
      value: 23.021
    - type: map_at_100
      value: 25.095
    - type: map_at_1000
      value: 25.295
    - type: map_at_3
      value: 19.463
    - type: map_at_5
      value: 21.389
    - type: mrr_at_1
      value: 29.576999999999998
    - type: mrr_at_10
      value: 41.44
    - type: mrr_at_100
      value: 42.497
    - type: mrr_at_1000
      value: 42.529
    - type: mrr_at_3
      value: 38.284
    - type: mrr_at_5
      value: 40.249
    - type: ndcg_at_1
      value: 29.576999999999998
    - type: ndcg_at_10
      value: 31.491000000000003
    - type: ndcg_at_100
      value: 39.352
    - type: ndcg_at_1000
      value: 42.703
    - type: ndcg_at_3
      value: 26.284999999999997
    - type: ndcg_at_5
      value: 28.218
    - type: precision_at_1
      value: 29.576999999999998
    - type: precision_at_10
      value: 9.713
    - type: precision_at_100
      value: 1.8079999999999998
    - type: precision_at_1000
      value: 0.243
    - type: precision_at_3
      value: 19.608999999999998
    - type: precision_at_5
      value: 14.957999999999998
    - type: recall_at_1
      value: 13.587
    - type: recall_at_10
      value: 37.001
    - type: recall_at_100
      value: 63.617999999999995
    - type: recall_at_1000
      value: 82.207
    - type: recall_at_3
      value: 24.273
    - type: recall_at_5
      value: 29.813000000000002
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
      value: 9.98
    - type: map_at_10
      value: 20.447000000000003
    - type: map_at_100
      value: 29.032999999999998
    - type: map_at_1000
      value: 30.8
    - type: map_at_3
      value: 15.126999999999999
    - type: map_at_5
      value: 17.327
    - type: mrr_at_1
      value: 71.25
    - type: mrr_at_10
      value: 78.014
    - type: mrr_at_100
      value: 78.303
    - type: mrr_at_1000
      value: 78.309
    - type: mrr_at_3
      value: 76.375
    - type: mrr_at_5
      value: 77.58699999999999
    - type: ndcg_at_1
      value: 57.99999999999999
    - type: ndcg_at_10
      value: 41.705
    - type: ndcg_at_100
      value: 47.466
    - type: ndcg_at_1000
      value: 55.186
    - type: ndcg_at_3
      value: 47.089999999999996
    - type: ndcg_at_5
      value: 43.974000000000004
    - type: precision_at_1
      value: 71.25
    - type: precision_at_10
      value: 32.65
    - type: precision_at_100
      value: 10.89
    - type: precision_at_1000
      value: 2.197
    - type: precision_at_3
      value: 50.5
    - type: precision_at_5
      value: 42.199999999999996
    - type: recall_at_1
      value: 9.98
    - type: recall_at_10
      value: 25.144
    - type: recall_at_100
      value: 53.754999999999995
    - type: recall_at_1000
      value: 78.56400000000001
    - type: recall_at_3
      value: 15.964
    - type: recall_at_5
      value: 19.186
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
      value: 54.67999999999999
    - type: f1
      value: 49.48247525503583
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
      value: 74.798
    - type: map_at_10
      value: 82.933
    - type: map_at_100
      value: 83.157
    - type: map_at_1000
      value: 83.173
    - type: map_at_3
      value: 81.80199999999999
    - type: map_at_5
      value: 82.55
    - type: mrr_at_1
      value: 80.573
    - type: mrr_at_10
      value: 87.615
    - type: mrr_at_100
      value: 87.69
    - type: mrr_at_1000
      value: 87.69200000000001
    - type: mrr_at_3
      value: 86.86399999999999
    - type: mrr_at_5
      value: 87.386
    - type: ndcg_at_1
      value: 80.573
    - type: ndcg_at_10
      value: 86.64500000000001
    - type: ndcg_at_100
      value: 87.407
    - type: ndcg_at_1000
      value: 87.68299999999999
    - type: ndcg_at_3
      value: 84.879
    - type: ndcg_at_5
      value: 85.921
    - type: precision_at_1
      value: 80.573
    - type: precision_at_10
      value: 10.348
    - type: precision_at_100
      value: 1.093
    - type: precision_at_1000
      value: 0.11399999999999999
    - type: precision_at_3
      value: 32.268
    - type: precision_at_5
      value: 20.084
    - type: recall_at_1
      value: 74.798
    - type: recall_at_10
      value: 93.45400000000001
    - type: recall_at_100
      value: 96.42500000000001
    - type: recall_at_1000
      value: 98.158
    - type: recall_at_3
      value: 88.634
    - type: recall_at_5
      value: 91.295
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
      value: 20.567
    - type: map_at_10
      value: 32.967999999999996
    - type: map_at_100
      value: 35.108
    - type: map_at_1000
      value: 35.272999999999996
    - type: map_at_3
      value: 28.701999999999998
    - type: map_at_5
      value: 31.114000000000004
    - type: mrr_at_1
      value: 40.432
    - type: mrr_at_10
      value: 48.956
    - type: mrr_at_100
      value: 49.832
    - type: mrr_at_1000
      value: 49.87
    - type: mrr_at_3
      value: 46.759
    - type: mrr_at_5
      value: 47.886
    - type: ndcg_at_1
      value: 40.432
    - type: ndcg_at_10
      value: 40.644000000000005
    - type: ndcg_at_100
      value: 48.252
    - type: ndcg_at_1000
      value: 51.099000000000004
    - type: ndcg_at_3
      value: 36.992000000000004
    - type: ndcg_at_5
      value: 38.077
    - type: precision_at_1
      value: 40.432
    - type: precision_at_10
      value: 11.296000000000001
    - type: precision_at_100
      value: 1.9009999999999998
    - type: precision_at_1000
      value: 0.241
    - type: precision_at_3
      value: 24.537
    - type: precision_at_5
      value: 17.963
    - type: recall_at_1
      value: 20.567
    - type: recall_at_10
      value: 47.052
    - type: recall_at_100
      value: 75.21600000000001
    - type: recall_at_1000
      value: 92.285
    - type: recall_at_3
      value: 33.488
    - type: recall_at_5
      value: 39.334
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
      value: 38.196999999999996
    - type: map_at_10
      value: 60.697
    - type: map_at_100
      value: 61.624
    - type: map_at_1000
      value: 61.692
    - type: map_at_3
      value: 57.421
    - type: map_at_5
      value: 59.455000000000005
    - type: mrr_at_1
      value: 76.39399999999999
    - type: mrr_at_10
      value: 82.504
    - type: mrr_at_100
      value: 82.71300000000001
    - type: mrr_at_1000
      value: 82.721
    - type: mrr_at_3
      value: 81.494
    - type: mrr_at_5
      value: 82.137
    - type: ndcg_at_1
      value: 76.39399999999999
    - type: ndcg_at_10
      value: 68.92200000000001
    - type: ndcg_at_100
      value: 72.13199999999999
    - type: ndcg_at_1000
      value: 73.392
    - type: ndcg_at_3
      value: 64.226
    - type: ndcg_at_5
      value: 66.815
    - type: precision_at_1
      value: 76.39399999999999
    - type: precision_at_10
      value: 14.442
    - type: precision_at_100
      value: 1.694
    - type: precision_at_1000
      value: 0.186
    - type: precision_at_3
      value: 41.211
    - type: precision_at_5
      value: 26.766000000000002
    - type: recall_at_1
      value: 38.196999999999996
    - type: recall_at_10
      value: 72.208
    - type: recall_at_100
      value: 84.71300000000001
    - type: recall_at_1000
      value: 92.971
    - type: recall_at_3
      value: 61.816
    - type: recall_at_5
      value: 66.914
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
      value: 89.6556
    - type: ap
      value: 85.27600392682054
    - type: f1
      value: 89.63353655386406
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
      value: 21.482
    - type: map_at_10
      value: 33.701
    - type: map_at_100
      value: 34.861
    - type: map_at_1000
      value: 34.914
    - type: map_at_3
      value: 29.793999999999997
    - type: map_at_5
      value: 32.072
    - type: mrr_at_1
      value: 22.163
    - type: mrr_at_10
      value: 34.371
    - type: mrr_at_100
      value: 35.471000000000004
    - type: mrr_at_1000
      value: 35.518
    - type: mrr_at_3
      value: 30.554
    - type: mrr_at_5
      value: 32.799
    - type: ndcg_at_1
      value: 22.163
    - type: ndcg_at_10
      value: 40.643
    - type: ndcg_at_100
      value: 46.239999999999995
    - type: ndcg_at_1000
      value: 47.526
    - type: ndcg_at_3
      value: 32.714999999999996
    - type: ndcg_at_5
      value: 36.791000000000004
    - type: precision_at_1
      value: 22.163
    - type: precision_at_10
      value: 6.4799999999999995
    - type: precision_at_100
      value: 0.928
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 14.002
    - type: precision_at_5
      value: 10.453
    - type: recall_at_1
      value: 21.482
    - type: recall_at_10
      value: 61.953
    - type: recall_at_100
      value: 87.86500000000001
    - type: recall_at_1000
      value: 97.636
    - type: recall_at_3
      value: 40.441
    - type: recall_at_5
      value: 50.27
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
      value: 95.3032375740994
    - type: f1
      value: 95.01515022686607
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
      value: 78.10077519379846
    - type: f1
      value: 58.240739725625644
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
      value: 76.0053799596503
    - type: f1
      value: 74.11733965804146
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
      value: 79.64021519838602
    - type: f1
      value: 79.8513960091438
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
      value: 33.92425767945184
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
      value: 32.249612382060754
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
      value: 32.35584955492918
    - type: mrr
      value: 33.545865224584674
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
      value: 6.978
    - type: map_at_10
      value: 14.749
    - type: map_at_100
      value: 19.192
    - type: map_at_1000
      value: 20.815
    - type: map_at_3
      value: 10.927000000000001
    - type: map_at_5
      value: 12.726
    - type: mrr_at_1
      value: 49.536
    - type: mrr_at_10
      value: 57.806999999999995
    - type: mrr_at_100
      value: 58.373
    - type: mrr_at_1000
      value: 58.407
    - type: mrr_at_3
      value: 55.779
    - type: mrr_at_5
      value: 57.095
    - type: ndcg_at_1
      value: 46.749
    - type: ndcg_at_10
      value: 37.644
    - type: ndcg_at_100
      value: 35.559000000000005
    - type: ndcg_at_1000
      value: 44.375
    - type: ndcg_at_3
      value: 43.354
    - type: ndcg_at_5
      value: 41.022999999999996
    - type: precision_at_1
      value: 48.607
    - type: precision_at_10
      value: 28.08
    - type: precision_at_100
      value: 9.155000000000001
    - type: precision_at_1000
      value: 2.2270000000000003
    - type: precision_at_3
      value: 40.764
    - type: precision_at_5
      value: 35.728
    - type: recall_at_1
      value: 6.978
    - type: recall_at_10
      value: 17.828
    - type: recall_at_100
      value: 36.010999999999996
    - type: recall_at_1000
      value: 68.34700000000001
    - type: recall_at_3
      value: 11.645999999999999
    - type: recall_at_5
      value: 14.427000000000001
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
      value: 30.219
    - type: map_at_10
      value: 45.633
    - type: map_at_100
      value: 46.752
    - type: map_at_1000
      value: 46.778999999999996
    - type: map_at_3
      value: 41.392
    - type: map_at_5
      value: 43.778
    - type: mrr_at_1
      value: 34.327999999999996
    - type: mrr_at_10
      value: 48.256
    - type: mrr_at_100
      value: 49.076
    - type: mrr_at_1000
      value: 49.092999999999996
    - type: mrr_at_3
      value: 44.786
    - type: mrr_at_5
      value: 46.766000000000005
    - type: ndcg_at_1
      value: 34.299
    - type: ndcg_at_10
      value: 53.434000000000005
    - type: ndcg_at_100
      value: 58.03
    - type: ndcg_at_1000
      value: 58.633
    - type: ndcg_at_3
      value: 45.433
    - type: ndcg_at_5
      value: 49.379
    - type: precision_at_1
      value: 34.299
    - type: precision_at_10
      value: 8.911
    - type: precision_at_100
      value: 1.145
    - type: precision_at_1000
      value: 0.12
    - type: precision_at_3
      value: 20.896
    - type: precision_at_5
      value: 14.832
    - type: recall_at_1
      value: 30.219
    - type: recall_at_10
      value: 74.59400000000001
    - type: recall_at_100
      value: 94.392
    - type: recall_at_1000
      value: 98.832
    - type: recall_at_3
      value: 53.754000000000005
    - type: recall_at_5
      value: 62.833000000000006
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
      value: 71.139
    - type: map_at_10
      value: 85.141
    - type: map_at_100
      value: 85.78099999999999
    - type: map_at_1000
      value: 85.795
    - type: map_at_3
      value: 82.139
    - type: map_at_5
      value: 84.075
    - type: mrr_at_1
      value: 81.98
    - type: mrr_at_10
      value: 88.056
    - type: mrr_at_100
      value: 88.152
    - type: mrr_at_1000
      value: 88.152
    - type: mrr_at_3
      value: 87.117
    - type: mrr_at_5
      value: 87.78099999999999
    - type: ndcg_at_1
      value: 82.02000000000001
    - type: ndcg_at_10
      value: 88.807
    - type: ndcg_at_100
      value: 89.99000000000001
    - type: ndcg_at_1000
      value: 90.068
    - type: ndcg_at_3
      value: 85.989
    - type: ndcg_at_5
      value: 87.627
    - type: precision_at_1
      value: 82.02000000000001
    - type: precision_at_10
      value: 13.472999999999999
    - type: precision_at_100
      value: 1.534
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 37.553
    - type: precision_at_5
      value: 24.788
    - type: recall_at_1
      value: 71.139
    - type: recall_at_10
      value: 95.707
    - type: recall_at_100
      value: 99.666
    - type: recall_at_1000
      value: 99.983
    - type: recall_at_3
      value: 87.64699999999999
    - type: recall_at_5
      value: 92.221
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
      value: 59.11035509193503
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
      value: 62.44241881422526
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
      value: 5.122999999999999
    - type: map_at_10
      value: 14.45
    - type: map_at_100
      value: 17.108999999999998
    - type: map_at_1000
      value: 17.517
    - type: map_at_3
      value: 10.213999999999999
    - type: map_at_5
      value: 12.278
    - type: mrr_at_1
      value: 25.3
    - type: mrr_at_10
      value: 37.791999999999994
    - type: mrr_at_100
      value: 39.086
    - type: mrr_at_1000
      value: 39.121
    - type: mrr_at_3
      value: 34.666999999999994
    - type: mrr_at_5
      value: 36.472
    - type: ndcg_at_1
      value: 25.3
    - type: ndcg_at_10
      value: 23.469
    - type: ndcg_at_100
      value: 33.324
    - type: ndcg_at_1000
      value: 39.357
    - type: ndcg_at_3
      value: 22.478
    - type: ndcg_at_5
      value: 19.539
    - type: precision_at_1
      value: 25.3
    - type: precision_at_10
      value: 12.3
    - type: precision_at_100
      value: 2.654
    - type: precision_at_1000
      value: 0.40800000000000003
    - type: precision_at_3
      value: 21.667
    - type: precision_at_5
      value: 17.5
    - type: recall_at_1
      value: 5.122999999999999
    - type: recall_at_10
      value: 24.937
    - type: recall_at_100
      value: 53.833
    - type: recall_at_1000
      value: 82.85
    - type: recall_at_3
      value: 13.178
    - type: recall_at_5
      value: 17.747
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
      value: 86.76549431206278
    - type: cos_sim_spearman
      value: 81.28563534883214
    - type: euclidean_pearson
      value: 84.17180713818567
    - type: euclidean_spearman
      value: 81.1684082302606
    - type: manhattan_pearson
      value: 84.12189753972959
    - type: manhattan_spearman
      value: 81.1134998997958
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
      value: 85.75137587182017
    - type: cos_sim_spearman
      value: 76.155337187325
    - type: euclidean_pearson
      value: 83.54551546726665
    - type: euclidean_spearman
      value: 76.30324990565346
    - type: manhattan_pearson
      value: 83.52192617483797
    - type: manhattan_spearman
      value: 76.30017227216015
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
      value: 87.13890050398628
    - type: cos_sim_spearman
      value: 87.84898360302155
    - type: euclidean_pearson
      value: 86.89491809082031
    - type: euclidean_spearman
      value: 87.99935689905651
    - type: manhattan_pearson
      value: 86.86526424376366
    - type: manhattan_spearman
      value: 87.96850732980495
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
      value: 86.01978753231558
    - type: cos_sim_spearman
      value: 83.38989083933329
    - type: euclidean_pearson
      value: 85.28405032045376
    - type: euclidean_spearman
      value: 83.51703914276501
    - type: manhattan_pearson
      value: 85.25775133078966
    - type: manhattan_spearman
      value: 83.52815667821727
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
      value: 88.28482294437876
    - type: cos_sim_spearman
      value: 89.42976214499576
    - type: euclidean_pearson
      value: 88.72677957272468
    - type: euclidean_spearman
      value: 89.30001736116229
    - type: manhattan_pearson
      value: 88.64119331622562
    - type: manhattan_spearman
      value: 89.21771022634893
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
      value: 83.79810159351987
    - type: cos_sim_spearman
      value: 85.34918402034273
    - type: euclidean_pearson
      value: 84.76058606229002
    - type: euclidean_spearman
      value: 85.45159829941214
    - type: manhattan_pearson
      value: 84.73926491888156
    - type: manhattan_spearman
      value: 85.42568221985898
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
      value: 88.92796712570272
    - type: cos_sim_spearman
      value: 88.58925922945812
    - type: euclidean_pearson
      value: 88.97231215531797
    - type: euclidean_spearman
      value: 88.27036385068719
    - type: manhattan_pearson
      value: 88.95761469412228
    - type: manhattan_spearman
      value: 88.23980432487681
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
      value: 66.85679810182282
    - type: cos_sim_spearman
      value: 67.80696709003128
    - type: euclidean_pearson
      value: 68.77524185947989
    - type: euclidean_spearman
      value: 68.032438075422
    - type: manhattan_pearson
      value: 68.60489100404182
    - type: manhattan_spearman
      value: 67.75418889226138
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
      value: 86.33287880999367
    - type: cos_sim_spearman
      value: 87.32401087204754
    - type: euclidean_pearson
      value: 87.27961069148029
    - type: euclidean_spearman
      value: 87.3547683085868
    - type: manhattan_pearson
      value: 87.24405442789622
    - type: manhattan_spearman
      value: 87.32896271166672
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
      value: 87.71553665286558
    - type: mrr
      value: 96.42436176749902
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
      value: 61.094
    - type: map_at_10
      value: 71.066
    - type: map_at_100
      value: 71.608
    - type: map_at_1000
      value: 71.629
    - type: map_at_3
      value: 68.356
    - type: map_at_5
      value: 70.15
    - type: mrr_at_1
      value: 64
    - type: mrr_at_10
      value: 71.82300000000001
    - type: mrr_at_100
      value: 72.251
    - type: mrr_at_1000
      value: 72.269
    - type: mrr_at_3
      value: 69.833
    - type: mrr_at_5
      value: 71.11699999999999
    - type: ndcg_at_1
      value: 64
    - type: ndcg_at_10
      value: 75.286
    - type: ndcg_at_100
      value: 77.40700000000001
    - type: ndcg_at_1000
      value: 77.806
    - type: ndcg_at_3
      value: 70.903
    - type: ndcg_at_5
      value: 73.36399999999999
    - type: precision_at_1
      value: 64
    - type: precision_at_10
      value: 9.9
    - type: precision_at_100
      value: 1.093
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 27.667
    - type: precision_at_5
      value: 18.333
    - type: recall_at_1
      value: 61.094
    - type: recall_at_10
      value: 87.256
    - type: recall_at_100
      value: 96.5
    - type: recall_at_1000
      value: 99.333
    - type: recall_at_3
      value: 75.6
    - type: recall_at_5
      value: 81.789
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
      value: 99.82871287128712
    - type: cos_sim_ap
      value: 95.9325677692287
    - type: cos_sim_f1
      value: 91.13924050632912
    - type: cos_sim_precision
      value: 92.3076923076923
    - type: cos_sim_recall
      value: 90
    - type: dot_accuracy
      value: 99.7980198019802
    - type: dot_ap
      value: 94.56107207796
    - type: dot_f1
      value: 89.41908713692946
    - type: dot_precision
      value: 92.88793103448276
    - type: dot_recall
      value: 86.2
    - type: euclidean_accuracy
      value: 99.82871287128712
    - type: euclidean_ap
      value: 95.94390332507025
    - type: euclidean_f1
      value: 91.17797042325346
    - type: euclidean_precision
      value: 93.02809573361083
    - type: euclidean_recall
      value: 89.4
    - type: manhattan_accuracy
      value: 99.82871287128712
    - type: manhattan_ap
      value: 95.97587114452257
    - type: manhattan_f1
      value: 91.25821121778675
    - type: manhattan_precision
      value: 92.23697650663942
    - type: manhattan_recall
      value: 90.3
    - type: max_accuracy
      value: 99.82871287128712
    - type: max_ap
      value: 95.97587114452257
    - type: max_f1
      value: 91.25821121778675
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
      value: 66.13974351708839
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
      value: 35.594544722932234
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
      value: 54.718738983377726
    - type: mrr
      value: 55.61655154486037
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
      value: 30.37028359646597
    - type: cos_sim_spearman
      value: 30.866534307244443
    - type: dot_pearson
      value: 29.89037691541816
    - type: dot_spearman
      value: 29.941267567971718
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
      value: 0.20400000000000001
    - type: map_at_10
      value: 1.7340000000000002
    - type: map_at_100
      value: 9.966
    - type: map_at_1000
      value: 25.119000000000003
    - type: map_at_3
      value: 0.596
    - type: map_at_5
      value: 0.941
    - type: mrr_at_1
      value: 76
    - type: mrr_at_10
      value: 85.85199999999999
    - type: mrr_at_100
      value: 85.85199999999999
    - type: mrr_at_1000
      value: 85.85199999999999
    - type: mrr_at_3
      value: 84.667
    - type: mrr_at_5
      value: 85.56700000000001
    - type: ndcg_at_1
      value: 71
    - type: ndcg_at_10
      value: 69.60300000000001
    - type: ndcg_at_100
      value: 54.166000000000004
    - type: ndcg_at_1000
      value: 51.085
    - type: ndcg_at_3
      value: 71.95
    - type: ndcg_at_5
      value: 71.17599999999999
    - type: precision_at_1
      value: 76
    - type: precision_at_10
      value: 74.2
    - type: precision_at_100
      value: 55.96
    - type: precision_at_1000
      value: 22.584
    - type: precision_at_3
      value: 77.333
    - type: precision_at_5
      value: 75.6
    - type: recall_at_1
      value: 0.20400000000000001
    - type: recall_at_10
      value: 1.992
    - type: recall_at_100
      value: 13.706999999999999
    - type: recall_at_1000
      value: 48.732
    - type: recall_at_3
      value: 0.635
    - type: recall_at_5
      value: 1.034
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (sqi-eng)
      config: sqi-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 8
    - type: f1
      value: 6.298401229470593
    - type: precision
      value: 5.916991709050532
    - type: recall
      value: 8
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (fry-eng)
      config: fry-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 17.341040462427745
    - type: f1
      value: 14.621650026274303
    - type: precision
      value: 13.9250609139035
    - type: recall
      value: 17.341040462427745
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kur-eng)
      config: kur-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 8.536585365853659
    - type: f1
      value: 6.30972482801751
    - type: precision
      value: 5.796517326875398
    - type: recall
      value: 8.536585365853659
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tur-eng)
      config: tur-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 6.4
    - type: f1
      value: 4.221126743626743
    - type: precision
      value: 3.822815143403898
    - type: recall
      value: 6.4
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (deu-eng)
      config: deu-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 19.8
    - type: f1
      value: 18.13768093781855
    - type: precision
      value: 17.54646004378763
    - type: recall
      value: 19.8
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nld-eng)
      config: nld-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 13.700000000000001
    - type: f1
      value: 12.367662337662336
    - type: precision
      value: 11.934237966189185
    - type: recall
      value: 13.700000000000001
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ron-eng)
      config: ron-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 14.299999999999999
    - type: f1
      value: 10.942180289268338
    - type: precision
      value: 10.153968847262192
    - type: recall
      value: 14.299999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ang-eng)
      config: ang-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 22.388059701492537
    - type: f1
      value: 17.00157733660433
    - type: precision
      value: 15.650551589876702
    - type: recall
      value: 22.388059701492537
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ido-eng)
      config: ido-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 22
    - type: f1
      value: 17.4576947358322
    - type: precision
      value: 16.261363669827777
    - type: recall
      value: 22
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (jav-eng)
      config: jav-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 8.292682926829269
    - type: f1
      value: 5.544048456005624
    - type: precision
      value: 5.009506603002538
    - type: recall
      value: 8.292682926829269
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (isl-eng)
      config: isl-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 5.4
    - type: f1
      value: 4.148897174789229
    - type: precision
      value: 3.862217259449564
    - type: recall
      value: 5.4
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (slv-eng)
      config: slv-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 5.5893074119076545
    - type: f1
      value: 4.375041810373159
    - type: precision
      value: 4.181207113088141
    - type: recall
      value: 5.5893074119076545
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cym-eng)
      config: cym-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 8.17391304347826
    - type: f1
      value: 6.448011891490153
    - type: precision
      value: 5.9719116632160105
    - type: recall
      value: 8.17391304347826
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kaz-eng)
      config: kaz-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.8695652173913043
    - type: f1
      value: 0.582815734989648
    - type: precision
      value: 0.5580885233059146
    - type: recall
      value: 0.8695652173913043
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (est-eng)
      config: est-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 5.1
    - type: f1
      value: 3.5000615825615826
    - type: precision
      value: 3.2073523577994707
    - type: recall
      value: 5.1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (heb-eng)
      config: heb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.3
    - type: f1
      value: 0.10109884927372195
    - type: precision
      value: 0.10055127118392897
    - type: recall
      value: 0.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (gla-eng)
      config: gla-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 3.8600723763570564
    - type: f1
      value: 2.8177402725050493
    - type: precision
      value: 2.5662687819699213
    - type: recall
      value: 3.8600723763570564
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mar-eng)
      config: mar-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0
    - type: f1
      value: 0
    - type: precision
      value: 0
    - type: recall
      value: 0
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (lat-eng)
      config: lat-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 15.299999999999999
    - type: f1
      value: 11.377964359824292
    - type: precision
      value: 10.361140908892764
    - type: recall
      value: 15.299999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (bel-eng)
      config: bel-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 1.3
    - type: f1
      value: 0.9600820232399179
    - type: precision
      value: 0.9151648856810397
    - type: recall
      value: 1.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (pms-eng)
      config: pms-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 14.095238095238095
    - type: f1
      value: 11.40081541819044
    - type: precision
      value: 10.645867976820359
    - type: recall
      value: 14.095238095238095
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (gle-eng)
      config: gle-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 4
    - type: f1
      value: 2.3800704501963432
    - type: precision
      value: 2.0919368034607455
    - type: recall
      value: 4
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (pes-eng)
      config: pes-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.3
    - type: f1
      value: 0.2002053388090349
    - type: precision
      value: 0.2001027749229188
    - type: recall
      value: 0.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nob-eng)
      config: nob-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 11.700000000000001
    - type: f1
      value: 10.29755634495992
    - type: precision
      value: 9.876637220292393
    - type: recall
      value: 11.700000000000001
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (bul-eng)
      config: bul-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 1.7000000000000002
    - type: f1
      value: 0.985815849620051
    - type: precision
      value: 0.8884689922480621
    - type: recall
      value: 1.7000000000000002
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cbk-eng)
      config: cbk-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 17.599999999999998
    - type: f1
      value: 14.086312656126182
    - type: precision
      value: 13.192360560816125
    - type: recall
      value: 17.599999999999998
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hun-eng)
      config: hun-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 6.1
    - type: f1
      value: 4.683795729173087
    - type: precision
      value: 4.31687579027912
    - type: recall
      value: 6.1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (uig-eng)
      config: uig-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.4
    - type: f1
      value: 0.20966666666666667
    - type: precision
      value: 0.20500700280112047
    - type: recall
      value: 0.4
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (rus-eng)
      config: rus-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.6
    - type: f1
      value: 0.2454665118079752
    - type: precision
      value: 0.2255125167991618
    - type: recall
      value: 0.6
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (spa-eng)
      config: spa-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 21
    - type: f1
      value: 18.965901242066018
    - type: precision
      value: 18.381437375171
    - type: recall
      value: 21
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hye-eng)
      config: hye-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.5390835579514826
    - type: f1
      value: 0.4048898457205192
    - type: precision
      value: 0.4046018763809678
    - type: recall
      value: 0.5390835579514826
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tel-eng)
      config: tel-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 1.282051282051282
    - type: f1
      value: 0.5098554872310529
    - type: precision
      value: 0.4715099715099715
    - type: recall
      value: 1.282051282051282
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (afr-eng)
      config: afr-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 10.7
    - type: f1
      value: 8.045120643200706
    - type: precision
      value: 7.387598023074453
    - type: recall
      value: 10.7
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mon-eng)
      config: mon-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 2.272727272727273
    - type: f1
      value: 1.44184724004356
    - type: precision
      value: 1.4082306862044767
    - type: recall
      value: 2.272727272727273
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (arz-eng)
      config: arz-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.20964360587002098
    - type: f1
      value: 0.001335309591528796
    - type: precision
      value: 0.0006697878781789807
    - type: recall
      value: 0.20964360587002098
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hrv-eng)
      config: hrv-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 7.1
    - type: f1
      value: 5.522254020507502
    - type: precision
      value: 5.081849426723903
    - type: recall
      value: 7.1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nov-eng)
      config: nov-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 36.57587548638132
    - type: f1
      value: 30.325515383881147
    - type: precision
      value: 28.59255854392041
    - type: recall
      value: 36.57587548638132
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (gsw-eng)
      config: gsw-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 16.23931623931624
    - type: f1
      value: 13.548783761549718
    - type: precision
      value: 13.0472896359184
    - type: recall
      value: 16.23931623931624
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nds-eng)
      config: nds-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 16.3
    - type: f1
      value: 13.3418584934734
    - type: precision
      value: 12.506853047473756
    - type: recall
      value: 16.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ukr-eng)
      config: ukr-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 1
    - type: f1
      value: 0.7764001197963462
    - type: precision
      value: 0.7551049317943337
    - type: recall
      value: 1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (uzb-eng)
      config: uzb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 3.9719626168224296
    - type: f1
      value: 3.190729401654313
    - type: precision
      value: 3.001159168296747
    - type: recall
      value: 3.9719626168224296
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (lit-eng)
      config: lit-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 3.4000000000000004
    - type: f1
      value: 2.4847456001574653
    - type: precision
      value: 2.308739271803959
    - type: recall
      value: 3.4000000000000004
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ina-eng)
      config: ina-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 36.9
    - type: f1
      value: 31.390407955063697
    - type: precision
      value: 29.631294298308614
    - type: recall
      value: 36.9
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (lfn-eng)
      config: lfn-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 14.2
    - type: f1
      value: 12.551591810861895
    - type: precision
      value: 12.100586917562724
    - type: recall
      value: 14.2
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (zsm-eng)
      config: zsm-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 9.2
    - type: f1
      value: 7.5561895648211435
    - type: precision
      value: 7.177371101110253
    - type: recall
      value: 9.2
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ita-eng)
      config: ita-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 21.2
    - type: f1
      value: 18.498268429117875
    - type: precision
      value: 17.693915156965357
    - type: recall
      value: 21.2
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cmn-eng)
      config: cmn-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 4.2
    - type: f1
      value: 2.886572782530936
    - type: precision
      value: 2.5806792595351915
    - type: recall
      value: 4.2
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (lvs-eng)
      config: lvs-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 6.800000000000001
    - type: f1
      value: 4.881091920308238
    - type: precision
      value: 4.436731163345769
    - type: recall
      value: 6.800000000000001
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (glg-eng)
      config: glg-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 22.1
    - type: f1
      value: 18.493832677140738
    - type: precision
      value: 17.52055858924503
    - type: recall
      value: 22.1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ceb-eng)
      config: ceb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 6
    - type: f1
      value: 4.58716840215435
    - type: precision
      value: 4.303119297298687
    - type: recall
      value: 6
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (bre-eng)
      config: bre-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 5.5
    - type: f1
      value: 3.813678559437776
    - type: precision
      value: 3.52375763382276
    - type: recall
      value: 5.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ben-eng)
      config: ben-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.2
    - type: f1
      value: 0.06701509872241579
    - type: precision
      value: 0.05017452006980803
    - type: recall
      value: 0.2
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (swg-eng)
      config: swg-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 12.5
    - type: f1
      value: 9.325396825396826
    - type: precision
      value: 8.681972789115646
    - type: recall
      value: 12.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (arq-eng)
      config: arq-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.43907793633369924
    - type: f1
      value: 0.26369680618309754
    - type: precision
      value: 0.24710650393580552
    - type: recall
      value: 0.43907793633369924
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kab-eng)
      config: kab-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 1.7000000000000002
    - type: f1
      value: 1.0240727731562105
    - type: precision
      value: 0.9379457073996874
    - type: recall
      value: 1.7000000000000002
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (fra-eng)
      config: fra-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 24.6
    - type: f1
      value: 21.527732683982684
    - type: precision
      value: 20.460911398969852
    - type: recall
      value: 24.6
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (por-eng)
      config: por-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 23.400000000000002
    - type: f1
      value: 18.861948871033608
    - type: precision
      value: 17.469730524988158
    - type: recall
      value: 23.400000000000002
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tat-eng)
      config: tat-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 1.3
    - type: f1
      value: 0.8081609699284277
    - type: precision
      value: 0.8041232161030668
    - type: recall
      value: 1.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (oci-eng)
      config: oci-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 14.399999999999999
    - type: f1
      value: 11.982642360594898
    - type: precision
      value: 11.423911681034546
    - type: recall
      value: 14.399999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (pol-eng)
      config: pol-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 8.7
    - type: f1
      value: 6.565099922088448
    - type: precision
      value: 6.009960806394631
    - type: recall
      value: 8.7
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (war-eng)
      config: war-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 7.1
    - type: f1
      value: 5.483244116053285
    - type: precision
      value: 5.08036675810842
    - type: recall
      value: 7.1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (aze-eng)
      config: aze-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 4.3999999999999995
    - type: f1
      value: 3.2643948695904146
    - type: precision
      value: 3.031506651474311
    - type: recall
      value: 4.3999999999999995
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (vie-eng)
      config: vie-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 7.1
    - type: f1
      value: 5.2787766765398345
    - type: precision
      value: 4.883891459552525
    - type: recall
      value: 7.1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nno-eng)
      config: nno-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 8.5
    - type: f1
      value: 7.022436974789914
    - type: precision
      value: 6.517919923571304
    - type: recall
      value: 8.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cha-eng)
      config: cha-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 17.51824817518248
    - type: f1
      value: 14.159211038143834
    - type: precision
      value: 13.419131771033424
    - type: recall
      value: 17.51824817518248
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mhr-eng)
      config: mhr-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.3
    - type: f1
      value: 0.1008802791411487
    - type: precision
      value: 0.10044111373948113
    - type: recall
      value: 0.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (dan-eng)
      config: dan-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 11.3
    - type: f1
      value: 10.0642631078894
    - type: precision
      value: 9.714481189937882
    - type: recall
      value: 11.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ell-eng)
      config: ell-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.7000000000000001
    - type: f1
      value: 0.5023625310859353
    - type: precision
      value: 0.5011883541295307
    - type: recall
      value: 0.7000000000000001
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (amh-eng)
      config: amh-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 1.7857142857142856
    - type: f1
      value: 0.6731500547238763
    - type: precision
      value: 0.6364087301587301
    - type: recall
      value: 1.7857142857142856
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (pam-eng)
      config: pam-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 7.000000000000001
    - type: f1
      value: 4.850226809905071
    - type: precision
      value: 4.3549672188068485
    - type: recall
      value: 7.000000000000001
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hsb-eng)
      config: hsb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 5.383022774327122
    - type: f1
      value: 4.080351427081423
    - type: precision
      value: 3.7431771127423294
    - type: recall
      value: 5.383022774327122
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (srp-eng)
      config: srp-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 3.9
    - type: f1
      value: 2.975065835065835
    - type: precision
      value: 2.7082951373488764
    - type: recall
      value: 3.9
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (epo-eng)
      config: epo-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 13.8
    - type: f1
      value: 10.976459812917616
    - type: precision
      value: 10.214566903851944
    - type: recall
      value: 13.8
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kzj-eng)
      config: kzj-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 4.9
    - type: f1
      value: 3.5998112099809334
    - type: precision
      value: 3.391430386128988
    - type: recall
      value: 4.9
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (awa-eng)
      config: awa-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 2.1645021645021645
    - type: f1
      value: 0.28969205674033943
    - type: precision
      value: 0.1648931376979724
    - type: recall
      value: 2.1645021645021645
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (fao-eng)
      config: fao-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 9.541984732824428
    - type: f1
      value: 8.129327179123026
    - type: precision
      value: 7.860730567672363
    - type: recall
      value: 9.541984732824428
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mal-eng)
      config: mal-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.5822416302765648
    - type: f1
      value: 0.3960292169899156
    - type: precision
      value: 0.36794436357755134
    - type: recall
      value: 0.5822416302765648
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ile-eng)
      config: ile-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 25.900000000000002
    - type: f1
      value: 20.98162273769728
    - type: precision
      value: 19.591031936732236
    - type: recall
      value: 25.900000000000002
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (bos-eng)
      config: bos-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 9.322033898305085
    - type: f1
      value: 7.1764632211739166
    - type: precision
      value: 6.547619047619047
    - type: recall
      value: 9.322033898305085
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cor-eng)
      config: cor-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 4.3999999999999995
    - type: f1
      value: 3.0484795026022216
    - type: precision
      value: 2.8132647991077686
    - type: recall
      value: 4.3999999999999995
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cat-eng)
      config: cat-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 18.8
    - type: f1
      value: 15.52276497119774
    - type: precision
      value: 14.63296284434154
    - type: recall
      value: 18.8
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (eus-eng)
      config: eus-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 10
    - type: f1
      value: 7.351901305737391
    - type: precision
      value: 6.759061952118555
    - type: recall
      value: 10
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (yue-eng)
      config: yue-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 3.1
    - type: f1
      value: 2.1527437641723353
    - type: precision
      value: 2.0008336640383417
    - type: recall
      value: 3.1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (swe-eng)
      config: swe-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 10.6
    - type: f1
      value: 8.471815215313617
    - type: precision
      value: 7.942319409218233
    - type: recall
      value: 10.6
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (dtp-eng)
      config: dtp-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 4.3
    - type: f1
      value: 2.7338036427188244
    - type: precision
      value: 2.5492261384839052
    - type: recall
      value: 4.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kat-eng)
      config: kat-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.40214477211796246
    - type: f1
      value: 0.28150134048257375
    - type: precision
      value: 0.2751516861859743
    - type: recall
      value: 0.40214477211796246
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (jpn-eng)
      config: jpn-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 3
    - type: f1
      value: 1.5834901411814404
    - type: precision
      value: 1.3894010894944848
    - type: recall
      value: 3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (csb-eng)
      config: csb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 7.905138339920949
    - type: f1
      value: 6.6397047981096735
    - type: precision
      value: 6.32664437012263
    - type: recall
      value: 7.905138339920949
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (xho-eng)
      config: xho-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 3.5211267605633805
    - type: f1
      value: 2.173419196807775
    - type: precision
      value: 2.14388897487489
    - type: recall
      value: 3.5211267605633805
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (orv-eng)
      config: orv-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.23952095808383234
    - type: f1
      value: 0.001262128032547595
    - type: precision
      value: 0.0006327654461278806
    - type: recall
      value: 0.23952095808383234
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ind-eng)
      config: ind-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 10.4
    - type: f1
      value: 8.370422351826372
    - type: precision
      value: 7.943809523809523
    - type: recall
      value: 10.4
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tuk-eng)
      config: tuk-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 5.41871921182266
    - type: f1
      value: 3.4763895108722696
    - type: precision
      value: 3.1331846246882176
    - type: recall
      value: 5.41871921182266
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (max-eng)
      config: max-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 9.15492957746479
    - type: f1
      value: 7.267458920187794
    - type: precision
      value: 6.893803787858966
    - type: recall
      value: 9.15492957746479
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (swh-eng)
      config: swh-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 9.487179487179487
    - type: f1
      value: 6.902767160316073
    - type: precision
      value: 6.450346503818517
    - type: recall
      value: 9.487179487179487
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hin-eng)
      config: hin-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.1
    - type: f1
      value: 0.0002042900919305414
    - type: precision
      value: 0.00010224948875255625
    - type: recall
      value: 0.1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (dsb-eng)
      config: dsb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 5.010438413361169
    - type: f1
      value: 3.8116647214505277
    - type: precision
      value: 3.5454644309619634
    - type: recall
      value: 5.010438413361169
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ber-eng)
      config: ber-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 6.2
    - type: f1
      value: 5.213158915433869
    - type: precision
      value: 5.080398110661268
    - type: recall
      value: 6.2
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tam-eng)
      config: tam-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.9771986970684038
    - type: f1
      value: 0.5061388123277374
    - type: precision
      value: 0.43431053203040165
    - type: recall
      value: 0.9771986970684038
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (slk-eng)
      config: slk-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 7.3
    - type: f1
      value: 5.6313180921027755
    - type: precision
      value: 5.303887400540395
    - type: recall
      value: 7.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tgl-eng)
      config: tgl-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 3.5999999999999996
    - type: f1
      value: 3.2180089485458607
    - type: precision
      value: 3.1006756756756753
    - type: recall
      value: 3.5999999999999996
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ast-eng)
      config: ast-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 22.04724409448819
    - type: f1
      value: 17.92525934258218
    - type: precision
      value: 16.48251629836593
    - type: recall
      value: 22.04724409448819
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mkd-eng)
      config: mkd-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.5
    - type: f1
      value: 0.1543743186232414
    - type: precision
      value: 0.13554933572174951
    - type: recall
      value: 0.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (khm-eng)
      config: khm-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.8310249307479225
    - type: f1
      value: 0.5102255597841558
    - type: precision
      value: 0.4859595744731704
    - type: recall
      value: 0.8310249307479225
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ces-eng)
      config: ces-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 6.9
    - type: f1
      value: 4.7258390633390635
    - type: precision
      value: 4.288366570275279
    - type: recall
      value: 6.9
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tzl-eng)
      config: tzl-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 17.307692307692307
    - type: f1
      value: 14.763313609467454
    - type: precision
      value: 14.129273504273504
    - type: recall
      value: 17.307692307692307
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (urd-eng)
      config: urd-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.3
    - type: f1
      value: 0.0022196828248667185
    - type: precision
      value: 0.0011148527298850575
    - type: recall
      value: 0.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ara-eng)
      config: ara-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.3
    - type: f1
      value: 0.3
    - type: precision
      value: 0.3
    - type: recall
      value: 0.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kor-eng)
      config: kor-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.6
    - type: f1
      value: 0.500206611570248
    - type: precision
      value: 0.5001034126163392
    - type: recall
      value: 0.6
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (yid-eng)
      config: yid-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.4716981132075472
    - type: f1
      value: 0.2953377695417789
    - type: precision
      value: 0.2754210459668228
    - type: recall
      value: 0.4716981132075472
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (fin-eng)
      config: fin-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 4.3999999999999995
    - type: f1
      value: 3.6228414442700156
    - type: precision
      value: 3.4318238993710692
    - type: recall
      value: 4.3999999999999995
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tha-eng)
      config: tha-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 1.2773722627737227
    - type: f1
      value: 1.0043318098096732
    - type: precision
      value: 0.9735777358593729
    - type: recall
      value: 1.2773722627737227
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (wuu-eng)
      config: wuu-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 3.9
    - type: f1
      value: 2.6164533097276226
    - type: precision
      value: 2.3558186153594085
    - type: recall
      value: 3.9
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
      value: 1.5779999999999998
    - type: map_at_10
      value: 8.339
    - type: map_at_100
      value: 14.601
    - type: map_at_1000
      value: 16.104
    - type: map_at_3
      value: 4.06
    - type: map_at_5
      value: 6.049
    - type: mrr_at_1
      value: 18.367
    - type: mrr_at_10
      value: 35.178
    - type: mrr_at_100
      value: 36.464999999999996
    - type: mrr_at_1000
      value: 36.464999999999996
    - type: mrr_at_3
      value: 29.932
    - type: mrr_at_5
      value: 34.32
    - type: ndcg_at_1
      value: 16.326999999999998
    - type: ndcg_at_10
      value: 20.578
    - type: ndcg_at_100
      value: 34.285
    - type: ndcg_at_1000
      value: 45.853
    - type: ndcg_at_3
      value: 19.869999999999997
    - type: ndcg_at_5
      value: 22.081999999999997
    - type: precision_at_1
      value: 18.367
    - type: precision_at_10
      value: 19.796
    - type: precision_at_100
      value: 7.714
    - type: precision_at_1000
      value: 1.547
    - type: precision_at_3
      value: 23.128999999999998
    - type: precision_at_5
      value: 24.898
    - type: recall_at_1
      value: 1.5779999999999998
    - type: recall_at_10
      value: 14.801
    - type: recall_at_100
      value: 48.516999999999996
    - type: recall_at_1000
      value: 83.30300000000001
    - type: recall_at_3
      value: 5.267
    - type: recall_at_5
      value: 9.415999999999999
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
      value: 72.4186
    - type: ap
      value: 14.536282543597242
    - type: f1
      value: 55.47661372005608
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
      value: 59.318053197509904
    - type: f1
      value: 59.68272481532353
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
      value: 52.155753554312
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
      value: 86.99409906419503
    - type: cos_sim_ap
      value: 76.91824322304332
    - type: cos_sim_f1
      value: 70.97865694950546
    - type: cos_sim_precision
      value: 70.03081664098613
    - type: cos_sim_recall
      value: 71.95250659630607
    - type: dot_accuracy
      value: 85.37879239434942
    - type: dot_ap
      value: 71.86454698478344
    - type: dot_f1
      value: 66.48115355426259
    - type: dot_precision
      value: 63.84839650145773
    - type: dot_recall
      value: 69.34036939313984
    - type: euclidean_accuracy
      value: 87.00005960541218
    - type: euclidean_ap
      value: 76.9165913835565
    - type: euclidean_f1
      value: 71.23741557283039
    - type: euclidean_precision
      value: 68.89327088982007
    - type: euclidean_recall
      value: 73.7467018469657
    - type: manhattan_accuracy
      value: 87.06562555880075
    - type: manhattan_ap
      value: 76.85445703747546
    - type: manhattan_f1
      value: 70.95560571858539
    - type: manhattan_precision
      value: 67.61472275334609
    - type: manhattan_recall
      value: 74.64379947229551
    - type: max_accuracy
      value: 87.06562555880075
    - type: max_ap
      value: 76.91824322304332
    - type: max_f1
      value: 71.23741557283039
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
      value: 88.93934101758063
    - type: cos_sim_ap
      value: 86.1071528049007
    - type: cos_sim_f1
      value: 78.21588263552714
    - type: cos_sim_precision
      value: 75.20073900376609
    - type: cos_sim_recall
      value: 81.48290729904527
    - type: dot_accuracy
      value: 88.2504754142896
    - type: dot_ap
      value: 84.19709379723844
    - type: dot_f1
      value: 76.92307692307693
    - type: dot_precision
      value: 71.81969949916528
    - type: dot_recall
      value: 82.80720665229443
    - type: euclidean_accuracy
      value: 88.97232894787906
    - type: euclidean_ap
      value: 86.02763993294909
    - type: euclidean_f1
      value: 78.18372741427383
    - type: euclidean_precision
      value: 73.79861918107868
    - type: euclidean_recall
      value: 83.12288266091777
    - type: manhattan_accuracy
      value: 88.86948422400745
    - type: manhattan_ap
      value: 86.0009157821563
    - type: manhattan_f1
      value: 78.10668017659404
    - type: manhattan_precision
      value: 73.68564795848695
    - type: manhattan_recall
      value: 83.09208500153989
    - type: max_accuracy
      value: 88.97232894787906
    - type: max_ap
      value: 86.1071528049007
    - type: max_f1
      value: 78.21588263552714
---
<h1 align="center">GIST Embedding v0</h1>

*GISTEmbed: Guided In-sample Selection of Training Negatives for Text Embedding Fine-tuning*

The model is fine-tuned on top of the [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5) using the [MEDI dataset](https://github.com/xlang-ai/instructor-embedding.git) augmented with mined triplets from the [MTEB Classification](https://huggingface.co/mteb) training dataset (excluding data from the Amazon Polarity Classification task).

The model does not require any instruction for generating embeddings. This means that queries for retrieval tasks can be directly encoded without crafting instructions.

Technical paper: [GISTEmbed: Guided In-sample Selection of Training Negatives for Text Embedding Fine-tuning](https://arxiv.org/abs/2402.16829)


# Data

The dataset used is a compilation of the MEDI and MTEB Classification training datasets. Third-party datasets may be subject to additional terms and conditions under their associated licenses. A HuggingFace Dataset version of the compiled dataset, and the specific revision used to train the model, is available:

- Dataset: [avsolatorio/medi-data-mteb_avs_triplets](https://huggingface.co/datasets/avsolatorio/medi-data-mteb_avs_triplets)
- Revision: 238a0499b6e6b690cc64ea56fde8461daa8341bb

The dataset contains a `task_type` key, which can be used to select only the mteb classification tasks (prefixed with `mteb_`).

The **MEDI Dataset** is published in the following paper: [One Embedder, Any Task: Instruction-Finetuned Text Embeddings](https://arxiv.org/abs/2212.09741).

The MTEB Benchmark results of the GIST embedding model, compared with the base model, suggest that the fine-tuning dataset has perturbed the model considerably, which resulted in significant improvements in certain tasks while adversely degrading performance in some.

The retrieval performance for the TRECCOVID task is of note. The fine-tuning dataset does not contain significant knowledge about COVID-19, which could have caused the observed performance degradation. We found some evidence, detailed in the paper, that thematic coverage of the fine-tuning data can affect downstream performance.

# Usage

The model can be easily loaded using the Sentence Transformers library.

```Python
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer

revision = None  # Replace with the specific revision to ensure reproducibility if the model is updated.

model = SentenceTransformer("avsolatorio/GIST-Embedding-v0", revision=revision)

texts = [
    "Illustration of the REaLTabFormer model. The left block shows the non-relational tabular data model using GPT-2 with a causal LM head. In contrast, the right block shows how a relational dataset's child table is modeled using a sequence-to-sequence (Seq2Seq) model. The Seq2Seq model uses the observations in the parent table to condition the generation of the observations in the child table. The trained GPT-2 model on the parent table, with weights frozen, is also used as the encoder in the Seq2Seq model.",
    "Predicting human mobility holds significant practical value, with applications ranging from enhancing disaster risk planning to simulating epidemic spread. In this paper, we present the GeoFormer, a decoder-only transformer model adapted from the GPT architecture to forecast human mobility.",
    "As the economies of Southeast Asia continue adopting digital technologies, policy makers increasingly ask how to prepare the workforce for emerging labor demands. However, little is known about the skills that workers need to adapt to these changes"
]

# Compute embeddings
embeddings = model.encode(texts, convert_to_tensor=True)

# Compute cosine-similarity for each pair of sentences
scores = F.cosine_similarity(embeddings.unsqueeze(1), embeddings.unsqueeze(0), dim=-1)

print(scores.cpu().numpy())
```

# Training Parameters

Below are the training parameters used to fine-tune the model:

```
Epochs = 80
Warmup ratio = 0.1
Learning rate = 5e-6
Batch size = 32
Checkpoint step = 103500
Contrastive loss temperature = 0.01
```


# Evaluation

The model was evaluated using the [MTEB Evaluation](https://huggingface.co/mteb) suite.


# Citation

Please cite our work if you use GISTEmbed or the datasets we published in your projects or research. 🤗

```
@article{solatorio2024gistembed,
    title={GISTEmbed: Guided In-sample Selection of Training Negatives for Text Embedding Fine-tuning},
    author={Aivin V. Solatorio},
    journal={arXiv preprint arXiv:2402.16829},
    year={2024},
    URL={https://arxiv.org/abs/2402.16829}
    eprint={2402.16829},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

# Acknowledgements

This work is supported by the "KCP IV - Exploring Data Use in the Development Economics Literature using Large Language Models (AI and LLMs)" project funded by the [Knowledge for Change Program (KCP)](https://www.worldbank.org/en/programs/knowledge-for-change) of the World Bank - RA-P503405-RESE-TF0C3444.

The findings, interpretations, and conclusions expressed in this material are entirely those of the authors. They do not necessarily represent the views of the International Bank for Reconstruction and Development/World Bank and its affiliated organizations, or those of the Executive Directors of the World Bank or the governments they represent.