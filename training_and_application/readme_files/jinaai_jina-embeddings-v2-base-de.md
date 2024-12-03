---
tags:
  - sentence-transformers
  - feature-extraction
  - sentence-similarity
  - mteb
  - transformers
  - transformers.js
language:
  - de
  - en
inference: false
license: apache-2.0
model-index:
- name: jina-embeddings-v2-base-de
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
      value: 73.76119402985076
    - type: ap
      value: 35.99577188521176
    - type: f1
      value: 67.50397431543269
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (de)
      config: de
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 68.9186295503212
    - type: ap
      value: 79.73307115840507
    - type: f1
      value: 66.66245744831339
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
      value: 77.52215
    - type: ap
      value: 71.85051037177416
    - type: f1
      value: 77.4171096157774
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
      value: 38.498
    - type: f1
      value: 38.058193386555956
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (de)
      config: de
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 37.717999999999996
    - type: f1
      value: 37.22674371574757
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
      value: 25.319999999999997
    - type: map_at_10
      value: 40.351
    - type: map_at_100
      value: 41.435
    - type: map_at_1000
      value: 41.443000000000005
    - type: map_at_3
      value: 35.266
    - type: map_at_5
      value: 37.99
    - type: mrr_at_1
      value: 25.746999999999996
    - type: mrr_at_10
      value: 40.515
    - type: mrr_at_100
      value: 41.606
    - type: mrr_at_1000
      value: 41.614000000000004
    - type: mrr_at_3
      value: 35.42
    - type: mrr_at_5
      value: 38.112
    - type: ndcg_at_1
      value: 25.319999999999997
    - type: ndcg_at_10
      value: 49.332
    - type: ndcg_at_100
      value: 53.909
    - type: ndcg_at_1000
      value: 54.089
    - type: ndcg_at_3
      value: 38.705
    - type: ndcg_at_5
      value: 43.606
    - type: precision_at_1
      value: 25.319999999999997
    - type: precision_at_10
      value: 7.831
    - type: precision_at_100
      value: 0.9820000000000001
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 16.24
    - type: precision_at_5
      value: 12.119
    - type: recall_at_1
      value: 25.319999999999997
    - type: recall_at_10
      value: 78.307
    - type: recall_at_100
      value: 98.222
    - type: recall_at_1000
      value: 99.57300000000001
    - type: recall_at_3
      value: 48.72
    - type: recall_at_5
      value: 60.597
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
      value: 41.43100588255654
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
      value: 32.08988904593667
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
      value: 60.55514765595906
    - type: mrr
      value: 73.51393835465858
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
      value: 79.6723823121172
    - type: cos_sim_spearman
      value: 76.90596922214986
    - type: euclidean_pearson
      value: 77.87910737957918
    - type: euclidean_spearman
      value: 76.66319260598262
    - type: manhattan_pearson
      value: 77.37039493457965
    - type: manhattan_spearman
      value: 76.09872191280964
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
      value: 98.97703549060543
    - type: f1
      value: 98.86569241475296
    - type: precision
      value: 98.81002087682673
    - type: recall
      value: 98.97703549060543
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
      value: 83.93506493506493
    - type: f1
      value: 83.91014949949302
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
      value: 34.970675877585144
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
      value: 28.779230269190954
  - task:
      type: Clustering
    dataset:
      type: slvnwhrl/blurbs-clustering-p2p
      name: MTEB BlurbsClusteringP2P
      config: default
      split: test
      revision: a2dd5b02a77de3466a3eaa98ae586b5610314496
    metrics:
    - type: v_measure
      value: 35.490175601567216
  - task:
      type: Clustering
    dataset:
      type: slvnwhrl/blurbs-clustering-s2s
      name: MTEB BlurbsClusteringS2S
      config: default
      split: test
      revision: 9bfff9a7f8f6dc6ffc9da71c48dd48b68696471d
    metrics:
    - type: v_measure
      value: 16.16638280560168
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
      value: 30.830999999999996
    - type: map_at_10
      value: 41.355
    - type: map_at_100
      value: 42.791000000000004
    - type: map_at_1000
      value: 42.918
    - type: map_at_3
      value: 38.237
    - type: map_at_5
      value: 40.066
    - type: mrr_at_1
      value: 38.484
    - type: mrr_at_10
      value: 47.593
    - type: mrr_at_100
      value: 48.388
    - type: mrr_at_1000
      value: 48.439
    - type: mrr_at_3
      value: 45.279
    - type: mrr_at_5
      value: 46.724
    - type: ndcg_at_1
      value: 38.484
    - type: ndcg_at_10
      value: 47.27
    - type: ndcg_at_100
      value: 52.568000000000005
    - type: ndcg_at_1000
      value: 54.729000000000006
    - type: ndcg_at_3
      value: 43.061
    - type: ndcg_at_5
      value: 45.083
    - type: precision_at_1
      value: 38.484
    - type: precision_at_10
      value: 8.927
    - type: precision_at_100
      value: 1.425
    - type: precision_at_1000
      value: 0.19
    - type: precision_at_3
      value: 20.791999999999998
    - type: precision_at_5
      value: 14.85
    - type: recall_at_1
      value: 30.830999999999996
    - type: recall_at_10
      value: 57.87799999999999
    - type: recall_at_100
      value: 80.124
    - type: recall_at_1000
      value: 94.208
    - type: recall_at_3
      value: 45.083
    - type: recall_at_5
      value: 51.154999999999994
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
      value: 25.782
    - type: map_at_10
      value: 34.492
    - type: map_at_100
      value: 35.521
    - type: map_at_1000
      value: 35.638
    - type: map_at_3
      value: 31.735999999999997
    - type: map_at_5
      value: 33.339
    - type: mrr_at_1
      value: 32.357
    - type: mrr_at_10
      value: 39.965
    - type: mrr_at_100
      value: 40.644000000000005
    - type: mrr_at_1000
      value: 40.695
    - type: mrr_at_3
      value: 37.739
    - type: mrr_at_5
      value: 39.061
    - type: ndcg_at_1
      value: 32.357
    - type: ndcg_at_10
      value: 39.644
    - type: ndcg_at_100
      value: 43.851
    - type: ndcg_at_1000
      value: 46.211999999999996
    - type: ndcg_at_3
      value: 35.675000000000004
    - type: ndcg_at_5
      value: 37.564
    - type: precision_at_1
      value: 32.357
    - type: precision_at_10
      value: 7.344
    - type: precision_at_100
      value: 1.201
    - type: precision_at_1000
      value: 0.168
    - type: precision_at_3
      value: 17.155
    - type: precision_at_5
      value: 12.166
    - type: recall_at_1
      value: 25.782
    - type: recall_at_10
      value: 49.132999999999996
    - type: recall_at_100
      value: 67.24
    - type: recall_at_1000
      value: 83.045
    - type: recall_at_3
      value: 37.021
    - type: recall_at_5
      value: 42.548
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
      value: 35.778999999999996
    - type: map_at_10
      value: 47.038000000000004
    - type: map_at_100
      value: 48.064
    - type: map_at_1000
      value: 48.128
    - type: map_at_3
      value: 44.186
    - type: map_at_5
      value: 45.788000000000004
    - type: mrr_at_1
      value: 41.254000000000005
    - type: mrr_at_10
      value: 50.556999999999995
    - type: mrr_at_100
      value: 51.296
    - type: mrr_at_1000
      value: 51.331
    - type: mrr_at_3
      value: 48.318
    - type: mrr_at_5
      value: 49.619
    - type: ndcg_at_1
      value: 41.254000000000005
    - type: ndcg_at_10
      value: 52.454
    - type: ndcg_at_100
      value: 56.776
    - type: ndcg_at_1000
      value: 58.181000000000004
    - type: ndcg_at_3
      value: 47.713
    - type: ndcg_at_5
      value: 49.997
    - type: precision_at_1
      value: 41.254000000000005
    - type: precision_at_10
      value: 8.464
    - type: precision_at_100
      value: 1.157
    - type: precision_at_1000
      value: 0.133
    - type: precision_at_3
      value: 21.526
    - type: precision_at_5
      value: 14.696000000000002
    - type: recall_at_1
      value: 35.778999999999996
    - type: recall_at_10
      value: 64.85300000000001
    - type: recall_at_100
      value: 83.98400000000001
    - type: recall_at_1000
      value: 94.18299999999999
    - type: recall_at_3
      value: 51.929
    - type: recall_at_5
      value: 57.666
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
      value: 21.719
    - type: map_at_10
      value: 29.326999999999998
    - type: map_at_100
      value: 30.314000000000004
    - type: map_at_1000
      value: 30.397000000000002
    - type: map_at_3
      value: 27.101
    - type: map_at_5
      value: 28.141
    - type: mrr_at_1
      value: 23.503
    - type: mrr_at_10
      value: 31.225
    - type: mrr_at_100
      value: 32.096000000000004
    - type: mrr_at_1000
      value: 32.159
    - type: mrr_at_3
      value: 29.076999999999998
    - type: mrr_at_5
      value: 30.083
    - type: ndcg_at_1
      value: 23.503
    - type: ndcg_at_10
      value: 33.842
    - type: ndcg_at_100
      value: 39.038000000000004
    - type: ndcg_at_1000
      value: 41.214
    - type: ndcg_at_3
      value: 29.347
    - type: ndcg_at_5
      value: 31.121
    - type: precision_at_1
      value: 23.503
    - type: precision_at_10
      value: 5.266
    - type: precision_at_100
      value: 0.831
    - type: precision_at_1000
      value: 0.106
    - type: precision_at_3
      value: 12.504999999999999
    - type: precision_at_5
      value: 8.565000000000001
    - type: recall_at_1
      value: 21.719
    - type: recall_at_10
      value: 46.024
    - type: recall_at_100
      value: 70.78999999999999
    - type: recall_at_1000
      value: 87.022
    - type: recall_at_3
      value: 33.64
    - type: recall_at_5
      value: 37.992
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
      value: 15.601
    - type: map_at_10
      value: 22.054000000000002
    - type: map_at_100
      value: 23.177
    - type: map_at_1000
      value: 23.308
    - type: map_at_3
      value: 19.772000000000002
    - type: map_at_5
      value: 21.055
    - type: mrr_at_1
      value: 19.403000000000002
    - type: mrr_at_10
      value: 26.409
    - type: mrr_at_100
      value: 27.356
    - type: mrr_at_1000
      value: 27.441
    - type: mrr_at_3
      value: 24.108999999999998
    - type: mrr_at_5
      value: 25.427
    - type: ndcg_at_1
      value: 19.403000000000002
    - type: ndcg_at_10
      value: 26.474999999999998
    - type: ndcg_at_100
      value: 32.086
    - type: ndcg_at_1000
      value: 35.231
    - type: ndcg_at_3
      value: 22.289
    - type: ndcg_at_5
      value: 24.271
    - type: precision_at_1
      value: 19.403000000000002
    - type: precision_at_10
      value: 4.813
    - type: precision_at_100
      value: 0.8869999999999999
    - type: precision_at_1000
      value: 0.13
    - type: precision_at_3
      value: 10.531
    - type: precision_at_5
      value: 7.710999999999999
    - type: recall_at_1
      value: 15.601
    - type: recall_at_10
      value: 35.916
    - type: recall_at_100
      value: 60.8
    - type: recall_at_1000
      value: 83.245
    - type: recall_at_3
      value: 24.321
    - type: recall_at_5
      value: 29.372999999999998
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
      value: 25.522
    - type: map_at_10
      value: 34.854
    - type: map_at_100
      value: 36.269
    - type: map_at_1000
      value: 36.387
    - type: map_at_3
      value: 32.187
    - type: map_at_5
      value: 33.692
    - type: mrr_at_1
      value: 31.375999999999998
    - type: mrr_at_10
      value: 40.471000000000004
    - type: mrr_at_100
      value: 41.481
    - type: mrr_at_1000
      value: 41.533
    - type: mrr_at_3
      value: 38.274
    - type: mrr_at_5
      value: 39.612
    - type: ndcg_at_1
      value: 31.375999999999998
    - type: ndcg_at_10
      value: 40.298
    - type: ndcg_at_100
      value: 46.255
    - type: ndcg_at_1000
      value: 48.522
    - type: ndcg_at_3
      value: 36.049
    - type: ndcg_at_5
      value: 38.095
    - type: precision_at_1
      value: 31.375999999999998
    - type: precision_at_10
      value: 7.305000000000001
    - type: precision_at_100
      value: 1.201
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 17.132
    - type: precision_at_5
      value: 12.107999999999999
    - type: recall_at_1
      value: 25.522
    - type: recall_at_10
      value: 50.988
    - type: recall_at_100
      value: 76.005
    - type: recall_at_1000
      value: 91.11200000000001
    - type: recall_at_3
      value: 38.808
    - type: recall_at_5
      value: 44.279
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
      value: 24.615000000000002
    - type: map_at_10
      value: 32.843
    - type: map_at_100
      value: 34.172999999999995
    - type: map_at_1000
      value: 34.286
    - type: map_at_3
      value: 30.125
    - type: map_at_5
      value: 31.495
    - type: mrr_at_1
      value: 30.023
    - type: mrr_at_10
      value: 38.106
    - type: mrr_at_100
      value: 39.01
    - type: mrr_at_1000
      value: 39.071
    - type: mrr_at_3
      value: 35.674
    - type: mrr_at_5
      value: 36.924
    - type: ndcg_at_1
      value: 30.023
    - type: ndcg_at_10
      value: 38.091
    - type: ndcg_at_100
      value: 43.771
    - type: ndcg_at_1000
      value: 46.315
    - type: ndcg_at_3
      value: 33.507
    - type: ndcg_at_5
      value: 35.304
    - type: precision_at_1
      value: 30.023
    - type: precision_at_10
      value: 6.837999999999999
    - type: precision_at_100
      value: 1.124
    - type: precision_at_1000
      value: 0.152
    - type: precision_at_3
      value: 15.562999999999999
    - type: precision_at_5
      value: 10.936
    - type: recall_at_1
      value: 24.615000000000002
    - type: recall_at_10
      value: 48.691
    - type: recall_at_100
      value: 72.884
    - type: recall_at_1000
      value: 90.387
    - type: recall_at_3
      value: 35.659
    - type: recall_at_5
      value: 40.602
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
      value: 23.223666666666666
    - type: map_at_10
      value: 31.338166666666673
    - type: map_at_100
      value: 32.47358333333333
    - type: map_at_1000
      value: 32.5955
    - type: map_at_3
      value: 28.84133333333333
    - type: map_at_5
      value: 30.20808333333333
    - type: mrr_at_1
      value: 27.62483333333333
    - type: mrr_at_10
      value: 35.385916666666674
    - type: mrr_at_100
      value: 36.23325
    - type: mrr_at_1000
      value: 36.29966666666667
    - type: mrr_at_3
      value: 33.16583333333333
    - type: mrr_at_5
      value: 34.41983333333334
    - type: ndcg_at_1
      value: 27.62483333333333
    - type: ndcg_at_10
      value: 36.222
    - type: ndcg_at_100
      value: 41.29491666666666
    - type: ndcg_at_1000
      value: 43.85508333333333
    - type: ndcg_at_3
      value: 31.95116666666667
    - type: ndcg_at_5
      value: 33.88541666666667
    - type: precision_at_1
      value: 27.62483333333333
    - type: precision_at_10
      value: 6.339916666666667
    - type: precision_at_100
      value: 1.0483333333333333
    - type: precision_at_1000
      value: 0.14608333333333334
    - type: precision_at_3
      value: 14.726500000000003
    - type: precision_at_5
      value: 10.395
    - type: recall_at_1
      value: 23.223666666666666
    - type: recall_at_10
      value: 46.778999999999996
    - type: recall_at_100
      value: 69.27141666666667
    - type: recall_at_1000
      value: 87.27383333333334
    - type: recall_at_3
      value: 34.678749999999994
    - type: recall_at_5
      value: 39.79900000000001
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
      value: 21.677
    - type: map_at_10
      value: 27.828000000000003
    - type: map_at_100
      value: 28.538999999999998
    - type: map_at_1000
      value: 28.64
    - type: map_at_3
      value: 26.105
    - type: map_at_5
      value: 27.009
    - type: mrr_at_1
      value: 24.387
    - type: mrr_at_10
      value: 30.209999999999997
    - type: mrr_at_100
      value: 30.953000000000003
    - type: mrr_at_1000
      value: 31.029
    - type: mrr_at_3
      value: 28.707
    - type: mrr_at_5
      value: 29.610999999999997
    - type: ndcg_at_1
      value: 24.387
    - type: ndcg_at_10
      value: 31.378
    - type: ndcg_at_100
      value: 35.249
    - type: ndcg_at_1000
      value: 37.923
    - type: ndcg_at_3
      value: 28.213
    - type: ndcg_at_5
      value: 29.658
    - type: precision_at_1
      value: 24.387
    - type: precision_at_10
      value: 4.8309999999999995
    - type: precision_at_100
      value: 0.73
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 12.168
    - type: precision_at_5
      value: 8.251999999999999
    - type: recall_at_1
      value: 21.677
    - type: recall_at_10
      value: 40.069
    - type: recall_at_100
      value: 58.077
    - type: recall_at_1000
      value: 77.97
    - type: recall_at_3
      value: 31.03
    - type: recall_at_5
      value: 34.838
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
      value: 14.484
    - type: map_at_10
      value: 20.355
    - type: map_at_100
      value: 21.382
    - type: map_at_1000
      value: 21.511
    - type: map_at_3
      value: 18.448
    - type: map_at_5
      value: 19.451999999999998
    - type: mrr_at_1
      value: 17.584
    - type: mrr_at_10
      value: 23.825
    - type: mrr_at_100
      value: 24.704
    - type: mrr_at_1000
      value: 24.793000000000003
    - type: mrr_at_3
      value: 21.92
    - type: mrr_at_5
      value: 22.97
    - type: ndcg_at_1
      value: 17.584
    - type: ndcg_at_10
      value: 24.315
    - type: ndcg_at_100
      value: 29.354999999999997
    - type: ndcg_at_1000
      value: 32.641999999999996
    - type: ndcg_at_3
      value: 20.802
    - type: ndcg_at_5
      value: 22.335
    - type: precision_at_1
      value: 17.584
    - type: precision_at_10
      value: 4.443
    - type: precision_at_100
      value: 0.8160000000000001
    - type: precision_at_1000
      value: 0.128
    - type: precision_at_3
      value: 9.807
    - type: precision_at_5
      value: 7.0889999999999995
    - type: recall_at_1
      value: 14.484
    - type: recall_at_10
      value: 32.804
    - type: recall_at_100
      value: 55.679
    - type: recall_at_1000
      value: 79.63
    - type: recall_at_3
      value: 22.976
    - type: recall_at_5
      value: 26.939
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
      value: 22.983999999999998
    - type: map_at_10
      value: 30.812
    - type: map_at_100
      value: 31.938
    - type: map_at_1000
      value: 32.056000000000004
    - type: map_at_3
      value: 28.449999999999996
    - type: map_at_5
      value: 29.542
    - type: mrr_at_1
      value: 27.145999999999997
    - type: mrr_at_10
      value: 34.782999999999994
    - type: mrr_at_100
      value: 35.699
    - type: mrr_at_1000
      value: 35.768
    - type: mrr_at_3
      value: 32.572
    - type: mrr_at_5
      value: 33.607
    - type: ndcg_at_1
      value: 27.145999999999997
    - type: ndcg_at_10
      value: 35.722
    - type: ndcg_at_100
      value: 40.964
    - type: ndcg_at_1000
      value: 43.598
    - type: ndcg_at_3
      value: 31.379
    - type: ndcg_at_5
      value: 32.924
    - type: precision_at_1
      value: 27.145999999999997
    - type: precision_at_10
      value: 6.063000000000001
    - type: precision_at_100
      value: 0.9730000000000001
    - type: precision_at_1000
      value: 0.13
    - type: precision_at_3
      value: 14.366000000000001
    - type: precision_at_5
      value: 9.776
    - type: recall_at_1
      value: 22.983999999999998
    - type: recall_at_10
      value: 46.876
    - type: recall_at_100
      value: 69.646
    - type: recall_at_1000
      value: 88.305
    - type: recall_at_3
      value: 34.471000000000004
    - type: recall_at_5
      value: 38.76
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
      value: 23.017000000000003
    - type: map_at_10
      value: 31.049
    - type: map_at_100
      value: 32.582
    - type: map_at_1000
      value: 32.817
    - type: map_at_3
      value: 28.303
    - type: map_at_5
      value: 29.854000000000003
    - type: mrr_at_1
      value: 27.866000000000003
    - type: mrr_at_10
      value: 35.56
    - type: mrr_at_100
      value: 36.453
    - type: mrr_at_1000
      value: 36.519
    - type: mrr_at_3
      value: 32.938
    - type: mrr_at_5
      value: 34.391
    - type: ndcg_at_1
      value: 27.866000000000003
    - type: ndcg_at_10
      value: 36.506
    - type: ndcg_at_100
      value: 42.344
    - type: ndcg_at_1000
      value: 45.213
    - type: ndcg_at_3
      value: 31.805
    - type: ndcg_at_5
      value: 33.933
    - type: precision_at_1
      value: 27.866000000000003
    - type: precision_at_10
      value: 7.016
    - type: precision_at_100
      value: 1.468
    - type: precision_at_1000
      value: 0.23900000000000002
    - type: precision_at_3
      value: 14.822
    - type: precision_at_5
      value: 10.791
    - type: recall_at_1
      value: 23.017000000000003
    - type: recall_at_10
      value: 47.053
    - type: recall_at_100
      value: 73.177
    - type: recall_at_1000
      value: 91.47800000000001
    - type: recall_at_3
      value: 33.675
    - type: recall_at_5
      value: 39.36
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
      value: 16.673
    - type: map_at_10
      value: 24.051000000000002
    - type: map_at_100
      value: 24.933
    - type: map_at_1000
      value: 25.06
    - type: map_at_3
      value: 21.446
    - type: map_at_5
      value: 23.064
    - type: mrr_at_1
      value: 18.115000000000002
    - type: mrr_at_10
      value: 25.927
    - type: mrr_at_100
      value: 26.718999999999998
    - type: mrr_at_1000
      value: 26.817999999999998
    - type: mrr_at_3
      value: 23.383000000000003
    - type: mrr_at_5
      value: 25.008999999999997
    - type: ndcg_at_1
      value: 18.115000000000002
    - type: ndcg_at_10
      value: 28.669
    - type: ndcg_at_100
      value: 33.282000000000004
    - type: ndcg_at_1000
      value: 36.481
    - type: ndcg_at_3
      value: 23.574
    - type: ndcg_at_5
      value: 26.340000000000003
    - type: precision_at_1
      value: 18.115000000000002
    - type: precision_at_10
      value: 4.769
    - type: precision_at_100
      value: 0.767
    - type: precision_at_1000
      value: 0.116
    - type: precision_at_3
      value: 10.351
    - type: precision_at_5
      value: 7.8
    - type: recall_at_1
      value: 16.673
    - type: recall_at_10
      value: 41.063
    - type: recall_at_100
      value: 62.851
    - type: recall_at_1000
      value: 86.701
    - type: recall_at_3
      value: 27.532
    - type: recall_at_5
      value: 34.076
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
      value: 8.752
    - type: map_at_10
      value: 15.120000000000001
    - type: map_at_100
      value: 16.678
    - type: map_at_1000
      value: 16.854
    - type: map_at_3
      value: 12.603
    - type: map_at_5
      value: 13.918
    - type: mrr_at_1
      value: 19.283
    - type: mrr_at_10
      value: 29.145
    - type: mrr_at_100
      value: 30.281000000000002
    - type: mrr_at_1000
      value: 30.339
    - type: mrr_at_3
      value: 26.069
    - type: mrr_at_5
      value: 27.864
    - type: ndcg_at_1
      value: 19.283
    - type: ndcg_at_10
      value: 21.804000000000002
    - type: ndcg_at_100
      value: 28.576
    - type: ndcg_at_1000
      value: 32.063
    - type: ndcg_at_3
      value: 17.511
    - type: ndcg_at_5
      value: 19.112000000000002
    - type: precision_at_1
      value: 19.283
    - type: precision_at_10
      value: 6.873
    - type: precision_at_100
      value: 1.405
    - type: precision_at_1000
      value: 0.20500000000000002
    - type: precision_at_3
      value: 13.16
    - type: precision_at_5
      value: 10.189
    - type: recall_at_1
      value: 8.752
    - type: recall_at_10
      value: 27.004
    - type: recall_at_100
      value: 50.648
    - type: recall_at_1000
      value: 70.458
    - type: recall_at_3
      value: 16.461000000000002
    - type: recall_at_5
      value: 20.973
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
      value: 6.81
    - type: map_at_10
      value: 14.056
    - type: map_at_100
      value: 18.961
    - type: map_at_1000
      value: 20.169
    - type: map_at_3
      value: 10.496
    - type: map_at_5
      value: 11.952
    - type: mrr_at_1
      value: 53.5
    - type: mrr_at_10
      value: 63.479
    - type: mrr_at_100
      value: 63.971999999999994
    - type: mrr_at_1000
      value: 63.993
    - type: mrr_at_3
      value: 61.541999999999994
    - type: mrr_at_5
      value: 62.778999999999996
    - type: ndcg_at_1
      value: 42.25
    - type: ndcg_at_10
      value: 31.471
    - type: ndcg_at_100
      value: 35.115
    - type: ndcg_at_1000
      value: 42.408
    - type: ndcg_at_3
      value: 35.458
    - type: ndcg_at_5
      value: 32.973
    - type: precision_at_1
      value: 53.5
    - type: precision_at_10
      value: 24.85
    - type: precision_at_100
      value: 7.79
    - type: precision_at_1000
      value: 1.599
    - type: precision_at_3
      value: 38.667
    - type: precision_at_5
      value: 31.55
    - type: recall_at_1
      value: 6.81
    - type: recall_at_10
      value: 19.344
    - type: recall_at_100
      value: 40.837
    - type: recall_at_1000
      value: 64.661
    - type: recall_at_3
      value: 11.942
    - type: recall_at_5
      value: 14.646
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
      value: 44.64499999999999
    - type: f1
      value: 39.39106911352714
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
      value: 48.196
    - type: map_at_10
      value: 61.404
    - type: map_at_100
      value: 61.846000000000004
    - type: map_at_1000
      value: 61.866
    - type: map_at_3
      value: 58.975
    - type: map_at_5
      value: 60.525
    - type: mrr_at_1
      value: 52.025
    - type: mrr_at_10
      value: 65.43299999999999
    - type: mrr_at_100
      value: 65.80799999999999
    - type: mrr_at_1000
      value: 65.818
    - type: mrr_at_3
      value: 63.146
    - type: mrr_at_5
      value: 64.64
    - type: ndcg_at_1
      value: 52.025
    - type: ndcg_at_10
      value: 67.889
    - type: ndcg_at_100
      value: 69.864
    - type: ndcg_at_1000
      value: 70.337
    - type: ndcg_at_3
      value: 63.315
    - type: ndcg_at_5
      value: 65.91799999999999
    - type: precision_at_1
      value: 52.025
    - type: precision_at_10
      value: 9.182
    - type: precision_at_100
      value: 1.027
    - type: precision_at_1000
      value: 0.108
    - type: precision_at_3
      value: 25.968000000000004
    - type: precision_at_5
      value: 17.006
    - type: recall_at_1
      value: 48.196
    - type: recall_at_10
      value: 83.885
    - type: recall_at_100
      value: 92.671
    - type: recall_at_1000
      value: 96.018
    - type: recall_at_3
      value: 71.59
    - type: recall_at_5
      value: 77.946
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
      value: 15.193000000000001
    - type: map_at_10
      value: 25.168000000000003
    - type: map_at_100
      value: 27.017000000000003
    - type: map_at_1000
      value: 27.205000000000002
    - type: map_at_3
      value: 21.746
    - type: map_at_5
      value: 23.579
    - type: mrr_at_1
      value: 31.635999999999996
    - type: mrr_at_10
      value: 40.077
    - type: mrr_at_100
      value: 41.112
    - type: mrr_at_1000
      value: 41.160999999999994
    - type: mrr_at_3
      value: 37.937
    - type: mrr_at_5
      value: 39.18
    - type: ndcg_at_1
      value: 31.635999999999996
    - type: ndcg_at_10
      value: 32.298
    - type: ndcg_at_100
      value: 39.546
    - type: ndcg_at_1000
      value: 42.88
    - type: ndcg_at_3
      value: 29.221999999999998
    - type: ndcg_at_5
      value: 30.069000000000003
    - type: precision_at_1
      value: 31.635999999999996
    - type: precision_at_10
      value: 9.367
    - type: precision_at_100
      value: 1.645
    - type: precision_at_1000
      value: 0.22399999999999998
    - type: precision_at_3
      value: 20.01
    - type: precision_at_5
      value: 14.753
    - type: recall_at_1
      value: 15.193000000000001
    - type: recall_at_10
      value: 38.214999999999996
    - type: recall_at_100
      value: 65.95
    - type: recall_at_1000
      value: 85.85300000000001
    - type: recall_at_3
      value: 26.357000000000003
    - type: recall_at_5
      value: 31.319999999999997
  - task:
      type: Retrieval
    dataset:
      type: jinaai/ger_da_lir
      name: MTEB GerDaLIR
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 10.363
    - type: map_at_10
      value: 16.222
    - type: map_at_100
      value: 17.28
    - type: map_at_1000
      value: 17.380000000000003
    - type: map_at_3
      value: 14.054
    - type: map_at_5
      value: 15.203
    - type: mrr_at_1
      value: 11.644
    - type: mrr_at_10
      value: 17.625
    - type: mrr_at_100
      value: 18.608
    - type: mrr_at_1000
      value: 18.695999999999998
    - type: mrr_at_3
      value: 15.481
    - type: mrr_at_5
      value: 16.659
    - type: ndcg_at_1
      value: 11.628
    - type: ndcg_at_10
      value: 20.028000000000002
    - type: ndcg_at_100
      value: 25.505
    - type: ndcg_at_1000
      value: 28.288000000000004
    - type: ndcg_at_3
      value: 15.603
    - type: ndcg_at_5
      value: 17.642
    - type: precision_at_1
      value: 11.628
    - type: precision_at_10
      value: 3.5589999999999997
    - type: precision_at_100
      value: 0.664
    - type: precision_at_1000
      value: 0.092
    - type: precision_at_3
      value: 7.109999999999999
    - type: precision_at_5
      value: 5.401
    - type: recall_at_1
      value: 10.363
    - type: recall_at_10
      value: 30.586000000000002
    - type: recall_at_100
      value: 56.43
    - type: recall_at_1000
      value: 78.142
    - type: recall_at_3
      value: 18.651
    - type: recall_at_5
      value: 23.493
  - task:
      type: Retrieval
    dataset:
      type: deepset/germandpr
      name: MTEB GermanDPR
      config: default
      split: test
      revision: 5129d02422a66be600ac89cd3e8531b4f97d347d
    metrics:
    - type: map_at_1
      value: 60.78
    - type: map_at_10
      value: 73.91499999999999
    - type: map_at_100
      value: 74.089
    - type: map_at_1000
      value: 74.09400000000001
    - type: map_at_3
      value: 71.87
    - type: map_at_5
      value: 73.37700000000001
    - type: mrr_at_1
      value: 60.78
    - type: mrr_at_10
      value: 73.91499999999999
    - type: mrr_at_100
      value: 74.089
    - type: mrr_at_1000
      value: 74.09400000000001
    - type: mrr_at_3
      value: 71.87
    - type: mrr_at_5
      value: 73.37700000000001
    - type: ndcg_at_1
      value: 60.78
    - type: ndcg_at_10
      value: 79.35600000000001
    - type: ndcg_at_100
      value: 80.077
    - type: ndcg_at_1000
      value: 80.203
    - type: ndcg_at_3
      value: 75.393
    - type: ndcg_at_5
      value: 78.077
    - type: precision_at_1
      value: 60.78
    - type: precision_at_10
      value: 9.59
    - type: precision_at_100
      value: 0.9900000000000001
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 28.52
    - type: precision_at_5
      value: 18.4
    - type: recall_at_1
      value: 60.78
    - type: recall_at_10
      value: 95.902
    - type: recall_at_100
      value: 99.024
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 85.56099999999999
    - type: recall_at_5
      value: 92.0
  - task:
      type: STS
    dataset:
      type: jinaai/german-STSbenchmark
      name: MTEB GermanSTSBenchmark
      config: default
      split: test
      revision: 49d9b423b996fea62b483f9ee6dfb5ec233515ca
    metrics:
    - type: cos_sim_pearson
      value: 88.49524420894356
    - type: cos_sim_spearman
      value: 88.32407839427714
    - type: euclidean_pearson
      value: 87.25098779877104
    - type: euclidean_spearman
      value: 88.22738098593608
    - type: manhattan_pearson
      value: 87.23872691839607
    - type: manhattan_spearman
      value: 88.2002968380165
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
      value: 31.81
    - type: map_at_10
      value: 46.238
    - type: map_at_100
      value: 47.141
    - type: map_at_1000
      value: 47.213
    - type: map_at_3
      value: 43.248999999999995
    - type: map_at_5
      value: 45.078
    - type: mrr_at_1
      value: 63.619
    - type: mrr_at_10
      value: 71.279
    - type: mrr_at_100
      value: 71.648
    - type: mrr_at_1000
      value: 71.665
    - type: mrr_at_3
      value: 69.76599999999999
    - type: mrr_at_5
      value: 70.743
    - type: ndcg_at_1
      value: 63.619
    - type: ndcg_at_10
      value: 55.38999999999999
    - type: ndcg_at_100
      value: 58.80800000000001
    - type: ndcg_at_1000
      value: 60.331999999999994
    - type: ndcg_at_3
      value: 50.727
    - type: ndcg_at_5
      value: 53.284
    - type: precision_at_1
      value: 63.619
    - type: precision_at_10
      value: 11.668000000000001
    - type: precision_at_100
      value: 1.434
    - type: precision_at_1000
      value: 0.164
    - type: precision_at_3
      value: 32.001000000000005
    - type: precision_at_5
      value: 21.223
    - type: recall_at_1
      value: 31.81
    - type: recall_at_10
      value: 58.339
    - type: recall_at_100
      value: 71.708
    - type: recall_at_1000
      value: 81.85
    - type: recall_at_3
      value: 48.001
    - type: recall_at_5
      value: 53.059
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
      value: 68.60640000000001
    - type: ap
      value: 62.84296904042086
    - type: f1
      value: 68.50643633327537
  - task:
      type: Reranking
    dataset:
      type: jinaai/miracl
      name: MTEB MIRACL
      config: default
      split: test
      revision: 8741c3b61cd36ed9ca1b3d4203543a41793239e2
    metrics:
    - type: map
      value: 64.29704335389768
    - type: mrr
      value: 72.11962197159565
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
      value: 89.3844049247606
    - type: f1
      value: 89.2124328528015
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (de)
      config: de
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 88.36855452240067
    - type: f1
      value: 87.35458822097442
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
      value: 66.48654810761514
    - type: f1
      value: 50.07229882504409
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (de)
      config: de
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 63.832065370526905
    - type: f1
      value: 46.283579383385806
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (de)
      config: de
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 63.89038332212509
    - type: f1
      value: 61.86279849685129
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
      value: 69.11230665770006
    - type: f1
      value: 67.44780095350535
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (de)
      config: de
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 71.25084061869536
    - type: f1
      value: 71.43965023016408
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
      value: 73.73907195696032
    - type: f1
      value: 73.69920814839061
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
      value: 31.32577306498249
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
      value: 28.759349326367783
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
      value: 30.401342674703425
    - type: mrr
      value: 31.384379585660987
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
      value: 4.855
    - type: map_at_10
      value: 10.01
    - type: map_at_100
      value: 12.461
    - type: map_at_1000
      value: 13.776
    - type: map_at_3
      value: 7.252
    - type: map_at_5
      value: 8.679
    - type: mrr_at_1
      value: 41.176
    - type: mrr_at_10
      value: 49.323
    - type: mrr_at_100
      value: 49.954
    - type: mrr_at_1000
      value: 49.997
    - type: mrr_at_3
      value: 46.904
    - type: mrr_at_5
      value: 48.375
    - type: ndcg_at_1
      value: 39.318999999999996
    - type: ndcg_at_10
      value: 28.607
    - type: ndcg_at_100
      value: 26.554
    - type: ndcg_at_1000
      value: 35.731
    - type: ndcg_at_3
      value: 32.897999999999996
    - type: ndcg_at_5
      value: 31.53
    - type: precision_at_1
      value: 41.176
    - type: precision_at_10
      value: 20.867
    - type: precision_at_100
      value: 6.796
    - type: precision_at_1000
      value: 1.983
    - type: precision_at_3
      value: 30.547
    - type: precision_at_5
      value: 27.245
    - type: recall_at_1
      value: 4.855
    - type: recall_at_10
      value: 14.08
    - type: recall_at_100
      value: 28.188000000000002
    - type: recall_at_1000
      value: 60.07900000000001
    - type: recall_at_3
      value: 7.947
    - type: recall_at_5
      value: 10.786
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
      value: 26.906999999999996
    - type: map_at_10
      value: 41.147
    - type: map_at_100
      value: 42.269
    - type: map_at_1000
      value: 42.308
    - type: map_at_3
      value: 36.638999999999996
    - type: map_at_5
      value: 39.285
    - type: mrr_at_1
      value: 30.359
    - type: mrr_at_10
      value: 43.607
    - type: mrr_at_100
      value: 44.454
    - type: mrr_at_1000
      value: 44.481
    - type: mrr_at_3
      value: 39.644
    - type: mrr_at_5
      value: 42.061
    - type: ndcg_at_1
      value: 30.330000000000002
    - type: ndcg_at_10
      value: 48.899
    - type: ndcg_at_100
      value: 53.612
    - type: ndcg_at_1000
      value: 54.51200000000001
    - type: ndcg_at_3
      value: 40.262
    - type: ndcg_at_5
      value: 44.787
    - type: precision_at_1
      value: 30.330000000000002
    - type: precision_at_10
      value: 8.323
    - type: precision_at_100
      value: 1.0959999999999999
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: precision_at_3
      value: 18.395
    - type: precision_at_5
      value: 13.627
    - type: recall_at_1
      value: 26.906999999999996
    - type: recall_at_10
      value: 70.215
    - type: recall_at_100
      value: 90.61200000000001
    - type: recall_at_1000
      value: 97.294
    - type: recall_at_3
      value: 47.784
    - type: recall_at_5
      value: 58.251
  - task:
      type: PairClassification
    dataset:
      type: paws-x
      name: MTEB PawsX
      config: default
      split: test
      revision: 8a04d940a42cd40658986fdd8e3da561533a3646
    metrics:
    - type: cos_sim_accuracy
      value: 60.5
    - type: cos_sim_ap
      value: 57.606096528877494
    - type: cos_sim_f1
      value: 62.24240307369892
    - type: cos_sim_precision
      value: 45.27439024390244
    - type: cos_sim_recall
      value: 99.55307262569832
    - type: dot_accuracy
      value: 57.699999999999996
    - type: dot_ap
      value: 51.289351057160616
    - type: dot_f1
      value: 62.25953130465197
    - type: dot_precision
      value: 45.31568228105906
    - type: dot_recall
      value: 99.4413407821229
    - type: euclidean_accuracy
      value: 60.45
    - type: euclidean_ap
      value: 57.616461421424034
    - type: euclidean_f1
      value: 62.313697657913416
    - type: euclidean_precision
      value: 45.657826313052524
    - type: euclidean_recall
      value: 98.10055865921787
    - type: manhattan_accuracy
      value: 60.3
    - type: manhattan_ap
      value: 57.580565271667325
    - type: manhattan_f1
      value: 62.24240307369892
    - type: manhattan_precision
      value: 45.27439024390244
    - type: manhattan_recall
      value: 99.55307262569832
    - type: max_accuracy
      value: 60.5
    - type: max_ap
      value: 57.616461421424034
    - type: max_f1
      value: 62.313697657913416
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
      value: 70.21300000000001
    - type: map_at_10
      value: 84.136
    - type: map_at_100
      value: 84.796
    - type: map_at_1000
      value: 84.812
    - type: map_at_3
      value: 81.182
    - type: map_at_5
      value: 83.027
    - type: mrr_at_1
      value: 80.91000000000001
    - type: mrr_at_10
      value: 87.155
    - type: mrr_at_100
      value: 87.27000000000001
    - type: mrr_at_1000
      value: 87.271
    - type: mrr_at_3
      value: 86.158
    - type: mrr_at_5
      value: 86.828
    - type: ndcg_at_1
      value: 80.88
    - type: ndcg_at_10
      value: 87.926
    - type: ndcg_at_100
      value: 89.223
    - type: ndcg_at_1000
      value: 89.321
    - type: ndcg_at_3
      value: 85.036
    - type: ndcg_at_5
      value: 86.614
    - type: precision_at_1
      value: 80.88
    - type: precision_at_10
      value: 13.350000000000001
    - type: precision_at_100
      value: 1.5310000000000001
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 37.173
    - type: precision_at_5
      value: 24.476
    - type: recall_at_1
      value: 70.21300000000001
    - type: recall_at_10
      value: 95.12
    - type: recall_at_100
      value: 99.535
    - type: recall_at_1000
      value: 99.977
    - type: recall_at_3
      value: 86.833
    - type: recall_at_5
      value: 91.26100000000001
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
      value: 47.754688783184875
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
      value: 54.875736374329364
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
      value: 3.773
    - type: map_at_10
      value: 9.447
    - type: map_at_100
      value: 11.1
    - type: map_at_1000
      value: 11.37
    - type: map_at_3
      value: 6.787
    - type: map_at_5
      value: 8.077
    - type: mrr_at_1
      value: 18.5
    - type: mrr_at_10
      value: 28.227000000000004
    - type: mrr_at_100
      value: 29.445
    - type: mrr_at_1000
      value: 29.515
    - type: mrr_at_3
      value: 25.2
    - type: mrr_at_5
      value: 27.055
    - type: ndcg_at_1
      value: 18.5
    - type: ndcg_at_10
      value: 16.29
    - type: ndcg_at_100
      value: 23.250999999999998
    - type: ndcg_at_1000
      value: 28.445999999999998
    - type: ndcg_at_3
      value: 15.376000000000001
    - type: ndcg_at_5
      value: 13.528
    - type: precision_at_1
      value: 18.5
    - type: precision_at_10
      value: 8.51
    - type: precision_at_100
      value: 1.855
    - type: precision_at_1000
      value: 0.311
    - type: precision_at_3
      value: 14.533
    - type: precision_at_5
      value: 12.0
    - type: recall_at_1
      value: 3.773
    - type: recall_at_10
      value: 17.282
    - type: recall_at_100
      value: 37.645
    - type: recall_at_1000
      value: 63.138000000000005
    - type: recall_at_3
      value: 8.853
    - type: recall_at_5
      value: 12.168
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
      value: 85.32789517976525
    - type: cos_sim_spearman
      value: 80.32750384145629
    - type: euclidean_pearson
      value: 81.5025131452508
    - type: euclidean_spearman
      value: 80.24797115147175
    - type: manhattan_pearson
      value: 81.51634463412002
    - type: manhattan_spearman
      value: 80.24614721495055
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
      value: 88.47050448992432
    - type: cos_sim_spearman
      value: 80.58919997743621
    - type: euclidean_pearson
      value: 85.83258918113664
    - type: euclidean_spearman
      value: 80.97441389240902
    - type: manhattan_pearson
      value: 85.7798262013878
    - type: manhattan_spearman
      value: 80.97208703064196
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
      value: 85.95341439711532
    - type: cos_sim_spearman
      value: 86.59127484634989
    - type: euclidean_pearson
      value: 85.57850603454227
    - type: euclidean_spearman
      value: 86.47130477363419
    - type: manhattan_pearson
      value: 85.59387925447652
    - type: manhattan_spearman
      value: 86.50665427391583
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
      value: 85.39810909161844
    - type: cos_sim_spearman
      value: 82.98595295546008
    - type: euclidean_pearson
      value: 84.04681129969951
    - type: euclidean_spearman
      value: 82.98197460689866
    - type: manhattan_pearson
      value: 83.9918798171185
    - type: manhattan_spearman
      value: 82.91148131768082
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
      value: 88.02072712147692
    - type: cos_sim_spearman
      value: 88.78821332623012
    - type: euclidean_pearson
      value: 88.12132045572747
    - type: euclidean_spearman
      value: 88.74273451067364
    - type: manhattan_pearson
      value: 88.05431550059166
    - type: manhattan_spearman
      value: 88.67610233020723
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
      value: 82.96134704624787
    - type: cos_sim_spearman
      value: 84.44062976314666
    - type: euclidean_pearson
      value: 84.03642536310323
    - type: euclidean_spearman
      value: 84.4535014579785
    - type: manhattan_pearson
      value: 83.92874228901483
    - type: manhattan_spearman
      value: 84.33634314951631
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-de)
      config: en-de
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 87.3154168064887
    - type: cos_sim_spearman
      value: 86.72393652571682
    - type: euclidean_pearson
      value: 86.04193246174164
    - type: euclidean_spearman
      value: 86.30482896608093
    - type: manhattan_pearson
      value: 85.95524084651859
    - type: manhattan_spearman
      value: 86.06031431994282
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
      value: 89.91079682750804
    - type: cos_sim_spearman
      value: 89.30961836617064
    - type: euclidean_pearson
      value: 88.86249564158628
    - type: euclidean_spearman
      value: 89.04772899592396
    - type: manhattan_pearson
      value: 88.85579791315043
    - type: manhattan_spearman
      value: 88.94190462541333
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
      value: 67.00558145551088
    - type: cos_sim_spearman
      value: 67.96601170393878
    - type: euclidean_pearson
      value: 67.87627043214336
    - type: euclidean_spearman
      value: 66.76402572303859
    - type: manhattan_pearson
      value: 67.88306560555452
    - type: manhattan_spearman
      value: 66.6273862035506
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de)
      config: de
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 50.83759332748726
    - type: cos_sim_spearman
      value: 59.066344562858006
    - type: euclidean_pearson
      value: 50.08955848154131
    - type: euclidean_spearman
      value: 58.36517305855221
    - type: manhattan_pearson
      value: 50.05257267223111
    - type: manhattan_spearman
      value: 58.37570252804986
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de-en)
      config: de-en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 59.22749007956492
    - type: cos_sim_spearman
      value: 55.97282077657827
    - type: euclidean_pearson
      value: 62.10661533695752
    - type: euclidean_spearman
      value: 53.62780854854067
    - type: manhattan_pearson
      value: 62.37138085709719
    - type: manhattan_spearman
      value: 54.17556356828155
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
      value: 87.91145397065878
    - type: cos_sim_spearman
      value: 88.13960018389005
    - type: euclidean_pearson
      value: 87.67618876224006
    - type: euclidean_spearman
      value: 87.99119480810556
    - type: manhattan_pearson
      value: 87.67920297334753
    - type: manhattan_spearman
      value: 87.99113250064492
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
      value: 78.09133563707582
    - type: mrr
      value: 93.2415288052543
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
      value: 47.760999999999996
    - type: map_at_10
      value: 56.424
    - type: map_at_100
      value: 57.24399999999999
    - type: map_at_1000
      value: 57.278
    - type: map_at_3
      value: 53.68000000000001
    - type: map_at_5
      value: 55.442
    - type: mrr_at_1
      value: 50.666999999999994
    - type: mrr_at_10
      value: 58.012
    - type: mrr_at_100
      value: 58.736
    - type: mrr_at_1000
      value: 58.769000000000005
    - type: mrr_at_3
      value: 56.056
    - type: mrr_at_5
      value: 57.321999999999996
    - type: ndcg_at_1
      value: 50.666999999999994
    - type: ndcg_at_10
      value: 60.67700000000001
    - type: ndcg_at_100
      value: 64.513
    - type: ndcg_at_1000
      value: 65.62400000000001
    - type: ndcg_at_3
      value: 56.186
    - type: ndcg_at_5
      value: 58.692
    - type: precision_at_1
      value: 50.666999999999994
    - type: precision_at_10
      value: 8.200000000000001
    - type: precision_at_100
      value: 1.023
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 21.889
    - type: precision_at_5
      value: 14.866999999999999
    - type: recall_at_1
      value: 47.760999999999996
    - type: recall_at_10
      value: 72.006
    - type: recall_at_100
      value: 89.767
    - type: recall_at_1000
      value: 98.833
    - type: recall_at_3
      value: 60.211000000000006
    - type: recall_at_5
      value: 66.3
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
      value: 99.79009900990098
    - type: cos_sim_ap
      value: 94.86690691995835
    - type: cos_sim_f1
      value: 89.37875751503007
    - type: cos_sim_precision
      value: 89.5582329317269
    - type: cos_sim_recall
      value: 89.2
    - type: dot_accuracy
      value: 99.76336633663367
    - type: dot_ap
      value: 94.26453740761586
    - type: dot_f1
      value: 88.00783162016641
    - type: dot_precision
      value: 86.19367209971237
    - type: dot_recall
      value: 89.9
    - type: euclidean_accuracy
      value: 99.7940594059406
    - type: euclidean_ap
      value: 94.85459757524379
    - type: euclidean_f1
      value: 89.62779156327544
    - type: euclidean_precision
      value: 88.96551724137932
    - type: euclidean_recall
      value: 90.3
    - type: manhattan_accuracy
      value: 99.79009900990098
    - type: manhattan_ap
      value: 94.76971336654465
    - type: manhattan_f1
      value: 89.35323383084577
    - type: manhattan_precision
      value: 88.91089108910892
    - type: manhattan_recall
      value: 89.8
    - type: max_accuracy
      value: 99.7940594059406
    - type: max_ap
      value: 94.86690691995835
    - type: max_f1
      value: 89.62779156327544
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
      value: 55.38197670064987
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
      value: 33.08330158937971
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
      value: 49.50367079063226
    - type: mrr
      value: 50.30444943128768
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
      value: 30.37739520909561
    - type: cos_sim_spearman
      value: 31.548500943973913
    - type: dot_pearson
      value: 29.983610104303
    - type: dot_spearman
      value: 29.90185869098618
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
      value: 0.198
    - type: map_at_10
      value: 1.5810000000000002
    - type: map_at_100
      value: 9.064
    - type: map_at_1000
      value: 22.161
    - type: map_at_3
      value: 0.536
    - type: map_at_5
      value: 0.8370000000000001
    - type: mrr_at_1
      value: 80.0
    - type: mrr_at_10
      value: 86.75
    - type: mrr_at_100
      value: 86.799
    - type: mrr_at_1000
      value: 86.799
    - type: mrr_at_3
      value: 85.0
    - type: mrr_at_5
      value: 86.5
    - type: ndcg_at_1
      value: 73.0
    - type: ndcg_at_10
      value: 65.122
    - type: ndcg_at_100
      value: 51.853
    - type: ndcg_at_1000
      value: 47.275
    - type: ndcg_at_3
      value: 66.274
    - type: ndcg_at_5
      value: 64.826
    - type: precision_at_1
      value: 80.0
    - type: precision_at_10
      value: 70.19999999999999
    - type: precision_at_100
      value: 53.480000000000004
    - type: precision_at_1000
      value: 20.946
    - type: precision_at_3
      value: 71.333
    - type: precision_at_5
      value: 70.0
    - type: recall_at_1
      value: 0.198
    - type: recall_at_10
      value: 1.884
    - type: recall_at_100
      value: 12.57
    - type: recall_at_1000
      value: 44.208999999999996
    - type: recall_at_3
      value: 0.5890000000000001
    - type: recall_at_5
      value: 0.95
  - task:
      type: Clustering
    dataset:
      type: slvnwhrl/tenkgnad-clustering-p2p
      name: MTEB TenKGnadClusteringP2P
      config: default
      split: test
      revision: 5c59e41555244b7e45c9a6be2d720ab4bafae558
    metrics:
    - type: v_measure
      value: 42.84199261133083
  - task:
      type: Clustering
    dataset:
      type: slvnwhrl/tenkgnad-clustering-s2s
      name: MTEB TenKGnadClusteringS2S
      config: default
      split: test
      revision: 6cddbe003f12b9b140aec477b583ac4191f01786
    metrics:
    - type: v_measure
      value: 23.689557114798838
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
      value: 1.941
    - type: map_at_10
      value: 8.222
    - type: map_at_100
      value: 14.277999999999999
    - type: map_at_1000
      value: 15.790000000000001
    - type: map_at_3
      value: 4.4670000000000005
    - type: map_at_5
      value: 5.762
    - type: mrr_at_1
      value: 24.490000000000002
    - type: mrr_at_10
      value: 38.784
    - type: mrr_at_100
      value: 39.724
    - type: mrr_at_1000
      value: 39.724
    - type: mrr_at_3
      value: 33.333
    - type: mrr_at_5
      value: 37.415
    - type: ndcg_at_1
      value: 22.448999999999998
    - type: ndcg_at_10
      value: 21.026
    - type: ndcg_at_100
      value: 33.721000000000004
    - type: ndcg_at_1000
      value: 45.045
    - type: ndcg_at_3
      value: 20.053
    - type: ndcg_at_5
      value: 20.09
    - type: precision_at_1
      value: 24.490000000000002
    - type: precision_at_10
      value: 19.796
    - type: precision_at_100
      value: 7.469
    - type: precision_at_1000
      value: 1.48
    - type: precision_at_3
      value: 21.769
    - type: precision_at_5
      value: 21.224
    - type: recall_at_1
      value: 1.941
    - type: recall_at_10
      value: 14.915999999999999
    - type: recall_at_100
      value: 46.155
    - type: recall_at_1000
      value: 80.664
    - type: recall_at_3
      value: 5.629
    - type: recall_at_5
      value: 8.437
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
      value: 69.64800000000001
    - type: ap
      value: 12.914826731261094
    - type: f1
      value: 53.05213503422915
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
      value: 60.427277872099594
    - type: f1
      value: 60.78292007556828
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
      value: 40.48134168406559
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
      value: 84.79465935506944
    - type: cos_sim_ap
      value: 70.24589055290592
    - type: cos_sim_f1
      value: 65.0994575045208
    - type: cos_sim_precision
      value: 63.76518218623482
    - type: cos_sim_recall
      value: 66.49076517150397
    - type: dot_accuracy
      value: 84.63968528342374
    - type: dot_ap
      value: 69.84683095084355
    - type: dot_f1
      value: 64.50606169727523
    - type: dot_precision
      value: 59.1719885487778
    - type: dot_recall
      value: 70.89709762532982
    - type: euclidean_accuracy
      value: 84.76485664898374
    - type: euclidean_ap
      value: 70.20556438685551
    - type: euclidean_f1
      value: 65.06796614516543
    - type: euclidean_precision
      value: 63.29840319361277
    - type: euclidean_recall
      value: 66.93931398416886
    - type: manhattan_accuracy
      value: 84.72313286046374
    - type: manhattan_ap
      value: 70.17151475534308
    - type: manhattan_f1
      value: 65.31379180759113
    - type: manhattan_precision
      value: 62.17505366086334
    - type: manhattan_recall
      value: 68.7862796833773
    - type: max_accuracy
      value: 84.79465935506944
    - type: max_ap
      value: 70.24589055290592
    - type: max_f1
      value: 65.31379180759113
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
      value: 88.95874568246207
    - type: cos_sim_ap
      value: 85.82517548264127
    - type: cos_sim_f1
      value: 78.22288041466125
    - type: cos_sim_precision
      value: 75.33875338753387
    - type: cos_sim_recall
      value: 81.33661841700031
    - type: dot_accuracy
      value: 88.836496293709
    - type: dot_ap
      value: 85.53430720252186
    - type: dot_f1
      value: 78.10616085869725
    - type: dot_precision
      value: 74.73269555430501
    - type: dot_recall
      value: 81.79858330766862
    - type: euclidean_accuracy
      value: 88.92769821865176
    - type: euclidean_ap
      value: 85.65904346964223
    - type: euclidean_f1
      value: 77.98774074208407
    - type: euclidean_precision
      value: 73.72282795035315
    - type: euclidean_recall
      value: 82.77640899291654
    - type: manhattan_accuracy
      value: 88.86366282454303
    - type: manhattan_ap
      value: 85.61599642231819
    - type: manhattan_f1
      value: 78.01480509061737
    - type: manhattan_precision
      value: 74.10460685833044
    - type: manhattan_recall
      value: 82.36064059131506
    - type: max_accuracy
      value: 88.95874568246207
    - type: max_ap
      value: 85.82517548264127
    - type: max_f1
      value: 78.22288041466125
  - task:
      type: Retrieval
    dataset:
      type: None
      name: MTEB WikiCLIR
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 3.9539999999999997
    - type: map_at_10
      value: 7.407
    - type: map_at_100
      value: 8.677999999999999
    - type: map_at_1000
      value: 9.077
    - type: map_at_3
      value: 5.987
    - type: map_at_5
      value: 6.6979999999999995
    - type: mrr_at_1
      value: 35.65
    - type: mrr_at_10
      value: 45.097
    - type: mrr_at_100
      value: 45.83
    - type: mrr_at_1000
      value: 45.871
    - type: mrr_at_3
      value: 42.63
    - type: mrr_at_5
      value: 44.104
    - type: ndcg_at_1
      value: 29.215000000000003
    - type: ndcg_at_10
      value: 22.694
    - type: ndcg_at_100
      value: 22.242
    - type: ndcg_at_1000
      value: 27.069
    - type: ndcg_at_3
      value: 27.641
    - type: ndcg_at_5
      value: 25.503999999999998
    - type: precision_at_1
      value: 35.65
    - type: precision_at_10
      value: 12.795000000000002
    - type: precision_at_100
      value: 3.354
    - type: precision_at_1000
      value: 0.743
    - type: precision_at_3
      value: 23.403
    - type: precision_at_5
      value: 18.474
    - type: recall_at_1
      value: 3.9539999999999997
    - type: recall_at_10
      value: 11.301
    - type: recall_at_100
      value: 22.919999999999998
    - type: recall_at_1000
      value: 40.146
    - type: recall_at_3
      value: 7.146
    - type: recall_at_5
      value: 8.844000000000001
  - task:
      type: Retrieval
    dataset:
      type: jinaai/xmarket_de
      name: MTEB XMarket
      config: default
      split: test
      revision: 2336818db4c06570fcdf263e1bcb9993b786f67a
    metrics:
    - type: map_at_1
      value: 4.872
    - type: map_at_10
      value: 10.658
    - type: map_at_100
      value: 13.422999999999998
    - type: map_at_1000
      value: 14.245
    - type: map_at_3
      value: 7.857
    - type: map_at_5
      value: 9.142999999999999
    - type: mrr_at_1
      value: 16.744999999999997
    - type: mrr_at_10
      value: 24.416
    - type: mrr_at_100
      value: 25.432
    - type: mrr_at_1000
      value: 25.502999999999997
    - type: mrr_at_3
      value: 22.096
    - type: mrr_at_5
      value: 23.421
    - type: ndcg_at_1
      value: 16.695999999999998
    - type: ndcg_at_10
      value: 18.66
    - type: ndcg_at_100
      value: 24.314
    - type: ndcg_at_1000
      value: 29.846
    - type: ndcg_at_3
      value: 17.041999999999998
    - type: ndcg_at_5
      value: 17.585
    - type: precision_at_1
      value: 16.695999999999998
    - type: precision_at_10
      value: 10.374
    - type: precision_at_100
      value: 3.988
    - type: precision_at_1000
      value: 1.1860000000000002
    - type: precision_at_3
      value: 14.21
    - type: precision_at_5
      value: 12.623000000000001
    - type: recall_at_1
      value: 4.872
    - type: recall_at_10
      value: 18.624
    - type: recall_at_100
      value: 40.988
    - type: recall_at_1000
      value: 65.33
    - type: recall_at_3
      value: 10.162
    - type: recall_at_5
      value: 13.517999999999999
---
<!-- TODO: add evaluation results here -->
<br><br>

<p align="center">
<img src="https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/603763514de52ff951d89793/AFoybzd5lpBQXEBrQHuTt.png?w=200&h=200&f=face" alt="Jina AI logo: Jina AI is your Portal to Multimodal AI" width="150px">
</p>


<p align="center">
<b>The text embedding set trained by <a href="https://jina.ai/"><b>Jina AI</b></a>.</b>
</p>

## Quick Start

The easiest way to starting using `jina-embeddings-v2-base-de` is to use Jina AI's [Embedding API](https://jina.ai/embeddings/).

## Intended Usage & Model Info

`jina-embeddings-v2-base-de` is a German/English bilingual text **embedding model** supporting **8192 sequence length**.
It is based on a BERT architecture (JinaBERT) that supports the symmetric bidirectional variant of [ALiBi](https://arxiv.org/abs/2108.12409) to allow longer sequence length.
We have designed it for high performance in mono-lingual & cross-lingual applications and trained it specifically to support mixed German-English input without bias. 
Additionally, we provide the following embedding models:

`jina-embeddings-v2-base-de` ist ein zweisprachiges **Text Embedding Modell** für Deutsch und Englisch,
welches Texteingaben mit einer Länge von bis zu **8192 Token unterstützt**.
Es basiert auf der adaptierten Bert-Modell-Architektur JinaBERT,
welche mithilfe einer symmetrische Variante von [ALiBi](https://arxiv.org/abs/2108.12409) längere Eingabetexte erlaubt.
Wir haben, das Model für hohe Performance in einsprachigen und cross-lingual Anwendungen entwickelt und speziell darauf trainiert,
gemischte deutsch-englische Eingaben ohne einen Bias zu kodieren.
Des Weiteren stellen wir folgende Embedding-Modelle bereit:

- [`jina-embeddings-v2-small-en`](https://huggingface.co/jinaai/jina-embeddings-v2-small-en): 33 million parameters.
- [`jina-embeddings-v2-base-en`](https://huggingface.co/jinaai/jina-embeddings-v2-base-en): 137 million parameters.
- [`jina-embeddings-v2-base-zh`](https://huggingface.co/jinaai/jina-embeddings-v2-base-zh): 161 million parameters Chinese-English Bilingual embeddings.
- [`jina-embeddings-v2-base-de`](https://huggingface.co/jinaai/jina-embeddings-v2-base-de): 161 million parameters German-English Bilingual embeddings **(you are here)**.
- [`jina-embeddings-v2-base-es`](): Spanish-English Bilingual embeddings (soon).
- [`jina-embeddings-v2-base-code`](https://huggingface.co/jinaai/jina-embeddings-v2-base-code): 161 million parameters code embeddings.

## Data & Parameters

The data and training details are described in this [technical report](https://arxiv.org/abs/2402.17016).

## Usage

**<details><summary>Please apply mean pooling when integrating the model.</summary>**
<p>

### Why mean pooling?

`mean poooling` takes all token embeddings from model output and averaging them at sentence/paragraph level.
It has been proved to be the most effective way to produce high-quality sentence embeddings.
We offer an `encode` function to deal with this.

However, if you would like to do it without using the default `encode` function:

```python
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

sentences = ['How is the weather today?', 'What is the current weather like today?']

tokenizer = AutoTokenizer.from_pretrained('jinaai/jina-embeddings-v2-base-de')
model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-de', trust_remote_code=True, torch_dtype=torch.bfloat16)

encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

with torch.no_grad():
    model_output = model(**encoded_input)

embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
embeddings = F.normalize(embeddings, p=2, dim=1)
```

</p>
</details>

You can use Jina Embedding models directly from transformers package.

```python
!pip install transformers
import torch
from transformers import AutoModel
from numpy.linalg import norm

cos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))
model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-de', trust_remote_code=True, torch_dtype=torch.bfloat16)
embeddings = model.encode(['How is the weather today?', 'Wie ist das Wetter heute?'])
print(cos_sim(embeddings[0], embeddings[1]))
```

If you only want to handle shorter sequence, such as 2k, pass the `max_length` parameter to the `encode` function:

```python
embeddings = model.encode(
    ['Very long ... document'],
    max_length=2048
)
```

Using the its latest release (v2.3.0) sentence-transformers also supports Jina embeddings (Please make sure that you are logged into huggingface as well):

```python
!pip install -U sentence-transformers
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer(
    "jinaai/jina-embeddings-v2-base-de", # switch to en/zh for English or Chinese
    trust_remote_code=True
)

# control your input sequence length up to 8192
model.max_seq_length = 1024

embeddings = model.encode([
    'How is the weather today?',
    'Wie ist das Wetter heute?'
])
print(cos_sim(embeddings[0], embeddings[1]))
```

## Alternatives to Using Transformers Package

1. _Managed SaaS_: Get started with a free key on Jina AI's [Embedding API](https://jina.ai/embeddings/). 
2. _Private and high-performance deployment_: Get started by picking from our suite of models and deploy them on [AWS Sagemaker](https://aws.amazon.com/marketplace/seller-profile?id=seller-stch2ludm6vgy).

## Benchmark Results

We evaluated our Bilingual model on all German and English evaluation tasks availble on the [MTEB benchmark](https://huggingface.co/blog/mteb). In addition, we evaluated the models agains a couple of other German, English, and multilingual models on additional German evaluation tasks:

<img src="de_evaluation_results.png" width="780px">

## Use Jina Embeddings for RAG

According to the latest blog post from [LLamaIndex](https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83),

> In summary, to achieve the peak performance in both hit rate and MRR, the combination of OpenAI or JinaAI-Base embeddings with the CohereRerank/bge-reranker-large reranker stands out.

<img src="https://miro.medium.com/v2/resize:fit:4800/format:webp/1*ZP2RVejCZovF3FDCg-Bx3A.png" width="780px">

## Contact

Join our [Discord community](https://discord.jina.ai) and chat with other community members about ideas.

## Citation

If you find Jina Embeddings useful in your research, please cite the following paper:

```
@article{mohr2024multi,
  title={Multi-Task Contrastive Learning for 8192-Token Bilingual Text Embeddings},
  author={Mohr, Isabelle and Krimmel, Markus and Sturua, Saba and Akram, Mohammad Kalim and Koukounas, Andreas and G{\"u}nther, Michael and Mastrapas, Georgios and Ravishankar, Vinit and Mart{\'\i}nez, Joan Fontanals and Wang, Feng and others},
  journal={arXiv preprint arXiv:2402.17016},
  year={2024}
}
```
