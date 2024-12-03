---
pipeline_tag: text-generation
inference: true
license: apache-2.0
datasets:
- GritLM/tulu2
tags:
- mteb
model-index:
- name: GritLM-7B
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
      value: 81.17910447761194
    - type: ap
      value: 46.26260671758199
    - type: f1
      value: 75.44565719934167
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
      value: 96.5161
    - type: ap
      value: 94.79131981460425
    - type: f1
      value: 96.51506148413065
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
      value: 57.806000000000004
    - type: f1
      value: 56.78350156257903
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
      value: 38.478
    - type: map_at_10
      value: 54.955
    - type: map_at_100
      value: 54.955
    - type: map_at_1000
      value: 54.955
    - type: map_at_3
      value: 50.888999999999996
    - type: map_at_5
      value: 53.349999999999994
    - type: mrr_at_1
      value: 39.757999999999996
    - type: mrr_at_10
      value: 55.449000000000005
    - type: mrr_at_100
      value: 55.449000000000005
    - type: mrr_at_1000
      value: 55.449000000000005
    - type: mrr_at_3
      value: 51.37500000000001
    - type: mrr_at_5
      value: 53.822
    - type: ndcg_at_1
      value: 38.478
    - type: ndcg_at_10
      value: 63.239999999999995
    - type: ndcg_at_100
      value: 63.239999999999995
    - type: ndcg_at_1000
      value: 63.239999999999995
    - type: ndcg_at_3
      value: 54.935
    - type: ndcg_at_5
      value: 59.379000000000005
    - type: precision_at_1
      value: 38.478
    - type: precision_at_10
      value: 8.933
    - type: precision_at_100
      value: 0.893
    - type: precision_at_1000
      value: 0.089
    - type: precision_at_3
      value: 22.214
    - type: precision_at_5
      value: 15.491
    - type: recall_at_1
      value: 38.478
    - type: recall_at_10
      value: 89.331
    - type: recall_at_100
      value: 89.331
    - type: recall_at_1000
      value: 89.331
    - type: recall_at_3
      value: 66.643
    - type: recall_at_5
      value: 77.45400000000001
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
      value: 51.67144081472449
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
      value: 48.11256154264126
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
      value: 67.33801955487878
    - type: mrr
      value: 80.71549487754474
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
      value: 88.1935203751726
    - type: cos_sim_spearman
      value: 86.35497970498659
    - type: euclidean_pearson
      value: 85.46910708503744
    - type: euclidean_spearman
      value: 85.13928935405485
    - type: manhattan_pearson
      value: 85.68373836333303
    - type: manhattan_spearman
      value: 85.40013867117746
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
      value: 88.46753246753248
    - type: f1
      value: 88.43006344981134
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
      value: 40.86793640310432
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
      value: 39.80291334130727
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
      value: 38.421
    - type: map_at_10
      value: 52.349000000000004
    - type: map_at_100
      value: 52.349000000000004
    - type: map_at_1000
      value: 52.349000000000004
    - type: map_at_3
      value: 48.17
    - type: map_at_5
      value: 50.432
    - type: mrr_at_1
      value: 47.353
    - type: mrr_at_10
      value: 58.387
    - type: mrr_at_100
      value: 58.387
    - type: mrr_at_1000
      value: 58.387
    - type: mrr_at_3
      value: 56.199
    - type: mrr_at_5
      value: 57.487
    - type: ndcg_at_1
      value: 47.353
    - type: ndcg_at_10
      value: 59.202
    - type: ndcg_at_100
      value: 58.848
    - type: ndcg_at_1000
      value: 58.831999999999994
    - type: ndcg_at_3
      value: 54.112
    - type: ndcg_at_5
      value: 56.312
    - type: precision_at_1
      value: 47.353
    - type: precision_at_10
      value: 11.459
    - type: precision_at_100
      value: 1.146
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 26.133
    - type: precision_at_5
      value: 18.627
    - type: recall_at_1
      value: 38.421
    - type: recall_at_10
      value: 71.89
    - type: recall_at_100
      value: 71.89
    - type: recall_at_1000
      value: 71.89
    - type: recall_at_3
      value: 56.58
    - type: recall_at_5
      value: 63.125
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
      value: 38.025999999999996
    - type: map_at_10
      value: 50.590999999999994
    - type: map_at_100
      value: 51.99700000000001
    - type: map_at_1000
      value: 52.11599999999999
    - type: map_at_3
      value: 47.435
    - type: map_at_5
      value: 49.236000000000004
    - type: mrr_at_1
      value: 48.28
    - type: mrr_at_10
      value: 56.814
    - type: mrr_at_100
      value: 57.446
    - type: mrr_at_1000
      value: 57.476000000000006
    - type: mrr_at_3
      value: 54.958
    - type: mrr_at_5
      value: 56.084999999999994
    - type: ndcg_at_1
      value: 48.28
    - type: ndcg_at_10
      value: 56.442
    - type: ndcg_at_100
      value: 60.651999999999994
    - type: ndcg_at_1000
      value: 62.187000000000005
    - type: ndcg_at_3
      value: 52.866
    - type: ndcg_at_5
      value: 54.515
    - type: precision_at_1
      value: 48.28
    - type: precision_at_10
      value: 10.586
    - type: precision_at_100
      value: 1.6310000000000002
    - type: precision_at_1000
      value: 0.20600000000000002
    - type: precision_at_3
      value: 25.945
    - type: precision_at_5
      value: 18.076
    - type: recall_at_1
      value: 38.025999999999996
    - type: recall_at_10
      value: 66.11399999999999
    - type: recall_at_100
      value: 83.339
    - type: recall_at_1000
      value: 92.413
    - type: recall_at_3
      value: 54.493
    - type: recall_at_5
      value: 59.64699999999999
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
      value: 47.905
    - type: map_at_10
      value: 61.58
    - type: map_at_100
      value: 62.605
    - type: map_at_1000
      value: 62.637
    - type: map_at_3
      value: 58.074000000000005
    - type: map_at_5
      value: 60.260000000000005
    - type: mrr_at_1
      value: 54.42
    - type: mrr_at_10
      value: 64.847
    - type: mrr_at_100
      value: 65.403
    - type: mrr_at_1000
      value: 65.41900000000001
    - type: mrr_at_3
      value: 62.675000000000004
    - type: mrr_at_5
      value: 64.101
    - type: ndcg_at_1
      value: 54.42
    - type: ndcg_at_10
      value: 67.394
    - type: ndcg_at_100
      value: 70.846
    - type: ndcg_at_1000
      value: 71.403
    - type: ndcg_at_3
      value: 62.025
    - type: ndcg_at_5
      value: 65.032
    - type: precision_at_1
      value: 54.42
    - type: precision_at_10
      value: 10.646
    - type: precision_at_100
      value: 1.325
    - type: precision_at_1000
      value: 0.13999999999999999
    - type: precision_at_3
      value: 27.398
    - type: precision_at_5
      value: 18.796
    - type: recall_at_1
      value: 47.905
    - type: recall_at_10
      value: 80.84599999999999
    - type: recall_at_100
      value: 95.078
    - type: recall_at_1000
      value: 98.878
    - type: recall_at_3
      value: 67.05600000000001
    - type: recall_at_5
      value: 74.261
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
      value: 30.745
    - type: map_at_10
      value: 41.021
    - type: map_at_100
      value: 41.021
    - type: map_at_1000
      value: 41.021
    - type: map_at_3
      value: 37.714999999999996
    - type: map_at_5
      value: 39.766
    - type: mrr_at_1
      value: 33.559
    - type: mrr_at_10
      value: 43.537
    - type: mrr_at_100
      value: 43.537
    - type: mrr_at_1000
      value: 43.537
    - type: mrr_at_3
      value: 40.546
    - type: mrr_at_5
      value: 42.439
    - type: ndcg_at_1
      value: 33.559
    - type: ndcg_at_10
      value: 46.781
    - type: ndcg_at_100
      value: 46.781
    - type: ndcg_at_1000
      value: 46.781
    - type: ndcg_at_3
      value: 40.516000000000005
    - type: ndcg_at_5
      value: 43.957
    - type: precision_at_1
      value: 33.559
    - type: precision_at_10
      value: 7.198
    - type: precision_at_100
      value: 0.72
    - type: precision_at_1000
      value: 0.07200000000000001
    - type: precision_at_3
      value: 17.1
    - type: precision_at_5
      value: 12.316
    - type: recall_at_1
      value: 30.745
    - type: recall_at_10
      value: 62.038000000000004
    - type: recall_at_100
      value: 62.038000000000004
    - type: recall_at_1000
      value: 62.038000000000004
    - type: recall_at_3
      value: 45.378
    - type: recall_at_5
      value: 53.580000000000005
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
      value: 19.637999999999998
    - type: map_at_10
      value: 31.05
    - type: map_at_100
      value: 31.05
    - type: map_at_1000
      value: 31.05
    - type: map_at_3
      value: 27.628000000000004
    - type: map_at_5
      value: 29.767
    - type: mrr_at_1
      value: 25.0
    - type: mrr_at_10
      value: 36.131
    - type: mrr_at_100
      value: 36.131
    - type: mrr_at_1000
      value: 36.131
    - type: mrr_at_3
      value: 33.333
    - type: mrr_at_5
      value: 35.143
    - type: ndcg_at_1
      value: 25.0
    - type: ndcg_at_10
      value: 37.478
    - type: ndcg_at_100
      value: 37.469
    - type: ndcg_at_1000
      value: 37.469
    - type: ndcg_at_3
      value: 31.757999999999996
    - type: ndcg_at_5
      value: 34.821999999999996
    - type: precision_at_1
      value: 25.0
    - type: precision_at_10
      value: 7.188999999999999
    - type: precision_at_100
      value: 0.719
    - type: precision_at_1000
      value: 0.07200000000000001
    - type: precision_at_3
      value: 15.837000000000002
    - type: precision_at_5
      value: 11.841
    - type: recall_at_1
      value: 19.637999999999998
    - type: recall_at_10
      value: 51.836000000000006
    - type: recall_at_100
      value: 51.836000000000006
    - type: recall_at_1000
      value: 51.836000000000006
    - type: recall_at_3
      value: 36.384
    - type: recall_at_5
      value: 43.964
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
      value: 34.884
    - type: map_at_10
      value: 47.88
    - type: map_at_100
      value: 47.88
    - type: map_at_1000
      value: 47.88
    - type: map_at_3
      value: 43.85
    - type: map_at_5
      value: 46.414
    - type: mrr_at_1
      value: 43.022
    - type: mrr_at_10
      value: 53.569
    - type: mrr_at_100
      value: 53.569
    - type: mrr_at_1000
      value: 53.569
    - type: mrr_at_3
      value: 51.075
    - type: mrr_at_5
      value: 52.725
    - type: ndcg_at_1
      value: 43.022
    - type: ndcg_at_10
      value: 54.461000000000006
    - type: ndcg_at_100
      value: 54.388000000000005
    - type: ndcg_at_1000
      value: 54.388000000000005
    - type: ndcg_at_3
      value: 48.864999999999995
    - type: ndcg_at_5
      value: 52.032000000000004
    - type: precision_at_1
      value: 43.022
    - type: precision_at_10
      value: 9.885
    - type: precision_at_100
      value: 0.988
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_3
      value: 23.612
    - type: precision_at_5
      value: 16.997
    - type: recall_at_1
      value: 34.884
    - type: recall_at_10
      value: 68.12899999999999
    - type: recall_at_100
      value: 68.12899999999999
    - type: recall_at_1000
      value: 68.12899999999999
    - type: recall_at_3
      value: 52.428
    - type: recall_at_5
      value: 60.662000000000006
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
      value: 31.588
    - type: map_at_10
      value: 43.85
    - type: map_at_100
      value: 45.317
    - type: map_at_1000
      value: 45.408
    - type: map_at_3
      value: 39.73
    - type: map_at_5
      value: 42.122
    - type: mrr_at_1
      value: 38.927
    - type: mrr_at_10
      value: 49.582
    - type: mrr_at_100
      value: 50.39
    - type: mrr_at_1000
      value: 50.426
    - type: mrr_at_3
      value: 46.518
    - type: mrr_at_5
      value: 48.271
    - type: ndcg_at_1
      value: 38.927
    - type: ndcg_at_10
      value: 50.605999999999995
    - type: ndcg_at_100
      value: 56.22200000000001
    - type: ndcg_at_1000
      value: 57.724
    - type: ndcg_at_3
      value: 44.232
    - type: ndcg_at_5
      value: 47.233999999999995
    - type: precision_at_1
      value: 38.927
    - type: precision_at_10
      value: 9.429
    - type: precision_at_100
      value: 1.435
    - type: precision_at_1000
      value: 0.172
    - type: precision_at_3
      value: 21.271
    - type: precision_at_5
      value: 15.434000000000001
    - type: recall_at_1
      value: 31.588
    - type: recall_at_10
      value: 64.836
    - type: recall_at_100
      value: 88.066
    - type: recall_at_1000
      value: 97.748
    - type: recall_at_3
      value: 47.128
    - type: recall_at_5
      value: 54.954
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
      value: 31.956083333333336
    - type: map_at_10
      value: 43.33483333333333
    - type: map_at_100
      value: 44.64883333333333
    - type: map_at_1000
      value: 44.75
    - type: map_at_3
      value: 39.87741666666666
    - type: map_at_5
      value: 41.86766666666667
    - type: mrr_at_1
      value: 38.06341666666667
    - type: mrr_at_10
      value: 47.839666666666666
    - type: mrr_at_100
      value: 48.644000000000005
    - type: mrr_at_1000
      value: 48.68566666666667
    - type: mrr_at_3
      value: 45.26358333333334
    - type: mrr_at_5
      value: 46.790000000000006
    - type: ndcg_at_1
      value: 38.06341666666667
    - type: ndcg_at_10
      value: 49.419333333333334
    - type: ndcg_at_100
      value: 54.50166666666667
    - type: ndcg_at_1000
      value: 56.161166666666674
    - type: ndcg_at_3
      value: 43.982416666666666
    - type: ndcg_at_5
      value: 46.638083333333334
    - type: precision_at_1
      value: 38.06341666666667
    - type: precision_at_10
      value: 8.70858333333333
    - type: precision_at_100
      value: 1.327
    - type: precision_at_1000
      value: 0.165
    - type: precision_at_3
      value: 20.37816666666667
    - type: precision_at_5
      value: 14.516333333333334
    - type: recall_at_1
      value: 31.956083333333336
    - type: recall_at_10
      value: 62.69458333333334
    - type: recall_at_100
      value: 84.46433333333334
    - type: recall_at_1000
      value: 95.58449999999999
    - type: recall_at_3
      value: 47.52016666666666
    - type: recall_at_5
      value: 54.36066666666666
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
      value: 28.912
    - type: map_at_10
      value: 38.291
    - type: map_at_100
      value: 39.44
    - type: map_at_1000
      value: 39.528
    - type: map_at_3
      value: 35.638
    - type: map_at_5
      value: 37.218
    - type: mrr_at_1
      value: 32.822
    - type: mrr_at_10
      value: 41.661
    - type: mrr_at_100
      value: 42.546
    - type: mrr_at_1000
      value: 42.603
    - type: mrr_at_3
      value: 39.238
    - type: mrr_at_5
      value: 40.726
    - type: ndcg_at_1
      value: 32.822
    - type: ndcg_at_10
      value: 43.373
    - type: ndcg_at_100
      value: 48.638
    - type: ndcg_at_1000
      value: 50.654999999999994
    - type: ndcg_at_3
      value: 38.643
    - type: ndcg_at_5
      value: 41.126000000000005
    - type: precision_at_1
      value: 32.822
    - type: precision_at_10
      value: 6.8709999999999996
    - type: precision_at_100
      value: 1.032
    - type: precision_at_1000
      value: 0.128
    - type: precision_at_3
      value: 16.82
    - type: precision_at_5
      value: 11.718
    - type: recall_at_1
      value: 28.912
    - type: recall_at_10
      value: 55.376999999999995
    - type: recall_at_100
      value: 79.066
    - type: recall_at_1000
      value: 93.664
    - type: recall_at_3
      value: 42.569
    - type: recall_at_5
      value: 48.719
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
      value: 22.181
    - type: map_at_10
      value: 31.462
    - type: map_at_100
      value: 32.73
    - type: map_at_1000
      value: 32.848
    - type: map_at_3
      value: 28.57
    - type: map_at_5
      value: 30.182
    - type: mrr_at_1
      value: 27.185
    - type: mrr_at_10
      value: 35.846000000000004
    - type: mrr_at_100
      value: 36.811
    - type: mrr_at_1000
      value: 36.873
    - type: mrr_at_3
      value: 33.437
    - type: mrr_at_5
      value: 34.813
    - type: ndcg_at_1
      value: 27.185
    - type: ndcg_at_10
      value: 36.858000000000004
    - type: ndcg_at_100
      value: 42.501
    - type: ndcg_at_1000
      value: 44.945
    - type: ndcg_at_3
      value: 32.066
    - type: ndcg_at_5
      value: 34.29
    - type: precision_at_1
      value: 27.185
    - type: precision_at_10
      value: 6.752
    - type: precision_at_100
      value: 1.111
    - type: precision_at_1000
      value: 0.151
    - type: precision_at_3
      value: 15.290000000000001
    - type: precision_at_5
      value: 11.004999999999999
    - type: recall_at_1
      value: 22.181
    - type: recall_at_10
      value: 48.513
    - type: recall_at_100
      value: 73.418
    - type: recall_at_1000
      value: 90.306
    - type: recall_at_3
      value: 35.003
    - type: recall_at_5
      value: 40.876000000000005
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
      value: 33.934999999999995
    - type: map_at_10
      value: 44.727
    - type: map_at_100
      value: 44.727
    - type: map_at_1000
      value: 44.727
    - type: map_at_3
      value: 40.918
    - type: map_at_5
      value: 42.961
    - type: mrr_at_1
      value: 39.646
    - type: mrr_at_10
      value: 48.898
    - type: mrr_at_100
      value: 48.898
    - type: mrr_at_1000
      value: 48.898
    - type: mrr_at_3
      value: 45.896
    - type: mrr_at_5
      value: 47.514
    - type: ndcg_at_1
      value: 39.646
    - type: ndcg_at_10
      value: 50.817
    - type: ndcg_at_100
      value: 50.803
    - type: ndcg_at_1000
      value: 50.803
    - type: ndcg_at_3
      value: 44.507999999999996
    - type: ndcg_at_5
      value: 47.259
    - type: precision_at_1
      value: 39.646
    - type: precision_at_10
      value: 8.759
    - type: precision_at_100
      value: 0.876
    - type: precision_at_1000
      value: 0.08800000000000001
    - type: precision_at_3
      value: 20.274
    - type: precision_at_5
      value: 14.366000000000001
    - type: recall_at_1
      value: 33.934999999999995
    - type: recall_at_10
      value: 65.037
    - type: recall_at_100
      value: 65.037
    - type: recall_at_1000
      value: 65.037
    - type: recall_at_3
      value: 47.439
    - type: recall_at_5
      value: 54.567
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
      value: 32.058
    - type: map_at_10
      value: 43.137
    - type: map_at_100
      value: 43.137
    - type: map_at_1000
      value: 43.137
    - type: map_at_3
      value: 39.882
    - type: map_at_5
      value: 41.379
    - type: mrr_at_1
      value: 38.933
    - type: mrr_at_10
      value: 48.344
    - type: mrr_at_100
      value: 48.344
    - type: mrr_at_1000
      value: 48.344
    - type: mrr_at_3
      value: 45.652
    - type: mrr_at_5
      value: 46.877
    - type: ndcg_at_1
      value: 38.933
    - type: ndcg_at_10
      value: 49.964
    - type: ndcg_at_100
      value: 49.242000000000004
    - type: ndcg_at_1000
      value: 49.222
    - type: ndcg_at_3
      value: 44.605
    - type: ndcg_at_5
      value: 46.501999999999995
    - type: precision_at_1
      value: 38.933
    - type: precision_at_10
      value: 9.427000000000001
    - type: precision_at_100
      value: 0.943
    - type: precision_at_1000
      value: 0.094
    - type: precision_at_3
      value: 20.685000000000002
    - type: precision_at_5
      value: 14.585
    - type: recall_at_1
      value: 32.058
    - type: recall_at_10
      value: 63.074
    - type: recall_at_100
      value: 63.074
    - type: recall_at_1000
      value: 63.074
    - type: recall_at_3
      value: 47.509
    - type: recall_at_5
      value: 52.455
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
      value: 26.029000000000003
    - type: map_at_10
      value: 34.646
    - type: map_at_100
      value: 34.646
    - type: map_at_1000
      value: 34.646
    - type: map_at_3
      value: 31.456
    - type: map_at_5
      value: 33.138
    - type: mrr_at_1
      value: 28.281
    - type: mrr_at_10
      value: 36.905
    - type: mrr_at_100
      value: 36.905
    - type: mrr_at_1000
      value: 36.905
    - type: mrr_at_3
      value: 34.011
    - type: mrr_at_5
      value: 35.638
    - type: ndcg_at_1
      value: 28.281
    - type: ndcg_at_10
      value: 40.159
    - type: ndcg_at_100
      value: 40.159
    - type: ndcg_at_1000
      value: 40.159
    - type: ndcg_at_3
      value: 33.995
    - type: ndcg_at_5
      value: 36.836999999999996
    - type: precision_at_1
      value: 28.281
    - type: precision_at_10
      value: 6.358999999999999
    - type: precision_at_100
      value: 0.636
    - type: precision_at_1000
      value: 0.064
    - type: precision_at_3
      value: 14.233
    - type: precision_at_5
      value: 10.314
    - type: recall_at_1
      value: 26.029000000000003
    - type: recall_at_10
      value: 55.08
    - type: recall_at_100
      value: 55.08
    - type: recall_at_1000
      value: 55.08
    - type: recall_at_3
      value: 38.487
    - type: recall_at_5
      value: 45.308
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
      value: 12.842999999999998
    - type: map_at_10
      value: 22.101000000000003
    - type: map_at_100
      value: 24.319
    - type: map_at_1000
      value: 24.51
    - type: map_at_3
      value: 18.372
    - type: map_at_5
      value: 20.323
    - type: mrr_at_1
      value: 27.948
    - type: mrr_at_10
      value: 40.321
    - type: mrr_at_100
      value: 41.262
    - type: mrr_at_1000
      value: 41.297
    - type: mrr_at_3
      value: 36.558
    - type: mrr_at_5
      value: 38.824999999999996
    - type: ndcg_at_1
      value: 27.948
    - type: ndcg_at_10
      value: 30.906
    - type: ndcg_at_100
      value: 38.986
    - type: ndcg_at_1000
      value: 42.136
    - type: ndcg_at_3
      value: 24.911
    - type: ndcg_at_5
      value: 27.168999999999997
    - type: precision_at_1
      value: 27.948
    - type: precision_at_10
      value: 9.798
    - type: precision_at_100
      value: 1.8399999999999999
    - type: precision_at_1000
      value: 0.243
    - type: precision_at_3
      value: 18.328
    - type: precision_at_5
      value: 14.502
    - type: recall_at_1
      value: 12.842999999999998
    - type: recall_at_10
      value: 37.245
    - type: recall_at_100
      value: 64.769
    - type: recall_at_1000
      value: 82.055
    - type: recall_at_3
      value: 23.159
    - type: recall_at_5
      value: 29.113
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
      value: 8.934000000000001
    - type: map_at_10
      value: 21.915000000000003
    - type: map_at_100
      value: 21.915000000000003
    - type: map_at_1000
      value: 21.915000000000003
    - type: map_at_3
      value: 14.623
    - type: map_at_5
      value: 17.841
    - type: mrr_at_1
      value: 71.25
    - type: mrr_at_10
      value: 78.994
    - type: mrr_at_100
      value: 78.994
    - type: mrr_at_1000
      value: 78.994
    - type: mrr_at_3
      value: 77.208
    - type: mrr_at_5
      value: 78.55799999999999
    - type: ndcg_at_1
      value: 60.62499999999999
    - type: ndcg_at_10
      value: 46.604
    - type: ndcg_at_100
      value: 35.653
    - type: ndcg_at_1000
      value: 35.531
    - type: ndcg_at_3
      value: 50.605
    - type: ndcg_at_5
      value: 48.730000000000004
    - type: precision_at_1
      value: 71.25
    - type: precision_at_10
      value: 37.75
    - type: precision_at_100
      value: 3.775
    - type: precision_at_1000
      value: 0.377
    - type: precision_at_3
      value: 54.417
    - type: precision_at_5
      value: 48.15
    - type: recall_at_1
      value: 8.934000000000001
    - type: recall_at_10
      value: 28.471000000000004
    - type: recall_at_100
      value: 28.471000000000004
    - type: recall_at_1000
      value: 28.471000000000004
    - type: recall_at_3
      value: 16.019
    - type: recall_at_5
      value: 21.410999999999998
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
      value: 52.81
    - type: f1
      value: 47.987573380720114
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
      value: 66.81899999999999
    - type: map_at_10
      value: 78.034
    - type: map_at_100
      value: 78.034
    - type: map_at_1000
      value: 78.034
    - type: map_at_3
      value: 76.43100000000001
    - type: map_at_5
      value: 77.515
    - type: mrr_at_1
      value: 71.542
    - type: mrr_at_10
      value: 81.638
    - type: mrr_at_100
      value: 81.638
    - type: mrr_at_1000
      value: 81.638
    - type: mrr_at_3
      value: 80.403
    - type: mrr_at_5
      value: 81.256
    - type: ndcg_at_1
      value: 71.542
    - type: ndcg_at_10
      value: 82.742
    - type: ndcg_at_100
      value: 82.741
    - type: ndcg_at_1000
      value: 82.741
    - type: ndcg_at_3
      value: 80.039
    - type: ndcg_at_5
      value: 81.695
    - type: precision_at_1
      value: 71.542
    - type: precision_at_10
      value: 10.387
    - type: precision_at_100
      value: 1.039
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 31.447999999999997
    - type: precision_at_5
      value: 19.91
    - type: recall_at_1
      value: 66.81899999999999
    - type: recall_at_10
      value: 93.372
    - type: recall_at_100
      value: 93.372
    - type: recall_at_1000
      value: 93.372
    - type: recall_at_3
      value: 86.33
    - type: recall_at_5
      value: 90.347
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
      value: 31.158
    - type: map_at_10
      value: 52.017
    - type: map_at_100
      value: 54.259
    - type: map_at_1000
      value: 54.367
    - type: map_at_3
      value: 45.738
    - type: map_at_5
      value: 49.283
    - type: mrr_at_1
      value: 57.87
    - type: mrr_at_10
      value: 66.215
    - type: mrr_at_100
      value: 66.735
    - type: mrr_at_1000
      value: 66.75
    - type: mrr_at_3
      value: 64.043
    - type: mrr_at_5
      value: 65.116
    - type: ndcg_at_1
      value: 57.87
    - type: ndcg_at_10
      value: 59.946999999999996
    - type: ndcg_at_100
      value: 66.31099999999999
    - type: ndcg_at_1000
      value: 67.75999999999999
    - type: ndcg_at_3
      value: 55.483000000000004
    - type: ndcg_at_5
      value: 56.891000000000005
    - type: precision_at_1
      value: 57.87
    - type: precision_at_10
      value: 16.497
    - type: precision_at_100
      value: 2.321
    - type: precision_at_1000
      value: 0.258
    - type: precision_at_3
      value: 37.14
    - type: precision_at_5
      value: 27.067999999999998
    - type: recall_at_1
      value: 31.158
    - type: recall_at_10
      value: 67.381
    - type: recall_at_100
      value: 89.464
    - type: recall_at_1000
      value: 97.989
    - type: recall_at_3
      value: 50.553000000000004
    - type: recall_at_5
      value: 57.824
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
      value: 42.073
    - type: map_at_10
      value: 72.418
    - type: map_at_100
      value: 73.175
    - type: map_at_1000
      value: 73.215
    - type: map_at_3
      value: 68.791
    - type: map_at_5
      value: 71.19
    - type: mrr_at_1
      value: 84.146
    - type: mrr_at_10
      value: 88.994
    - type: mrr_at_100
      value: 89.116
    - type: mrr_at_1000
      value: 89.12
    - type: mrr_at_3
      value: 88.373
    - type: mrr_at_5
      value: 88.82
    - type: ndcg_at_1
      value: 84.146
    - type: ndcg_at_10
      value: 79.404
    - type: ndcg_at_100
      value: 81.83200000000001
    - type: ndcg_at_1000
      value: 82.524
    - type: ndcg_at_3
      value: 74.595
    - type: ndcg_at_5
      value: 77.474
    - type: precision_at_1
      value: 84.146
    - type: precision_at_10
      value: 16.753999999999998
    - type: precision_at_100
      value: 1.8599999999999999
    - type: precision_at_1000
      value: 0.19499999999999998
    - type: precision_at_3
      value: 48.854
    - type: precision_at_5
      value: 31.579
    - type: recall_at_1
      value: 42.073
    - type: recall_at_10
      value: 83.768
    - type: recall_at_100
      value: 93.018
    - type: recall_at_1000
      value: 97.481
    - type: recall_at_3
      value: 73.282
    - type: recall_at_5
      value: 78.947
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
      value: 94.9968
    - type: ap
      value: 92.93892195862824
    - type: f1
      value: 94.99327998213761
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
      value: 21.698
    - type: map_at_10
      value: 34.585
    - type: map_at_100
      value: 35.782000000000004
    - type: map_at_1000
      value: 35.825
    - type: map_at_3
      value: 30.397999999999996
    - type: map_at_5
      value: 32.72
    - type: mrr_at_1
      value: 22.192
    - type: mrr_at_10
      value: 35.085
    - type: mrr_at_100
      value: 36.218
    - type: mrr_at_1000
      value: 36.256
    - type: mrr_at_3
      value: 30.986000000000004
    - type: mrr_at_5
      value: 33.268
    - type: ndcg_at_1
      value: 22.192
    - type: ndcg_at_10
      value: 41.957
    - type: ndcg_at_100
      value: 47.658
    - type: ndcg_at_1000
      value: 48.697
    - type: ndcg_at_3
      value: 33.433
    - type: ndcg_at_5
      value: 37.551
    - type: precision_at_1
      value: 22.192
    - type: precision_at_10
      value: 6.781
    - type: precision_at_100
      value: 0.963
    - type: precision_at_1000
      value: 0.105
    - type: precision_at_3
      value: 14.365
    - type: precision_at_5
      value: 10.713000000000001
    - type: recall_at_1
      value: 21.698
    - type: recall_at_10
      value: 64.79
    - type: recall_at_100
      value: 91.071
    - type: recall_at_1000
      value: 98.883
    - type: recall_at_3
      value: 41.611
    - type: recall_at_5
      value: 51.459999999999994
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
      value: 96.15823073415413
    - type: f1
      value: 96.00362034963248
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
      value: 87.12722298221614
    - type: f1
      value: 70.46888967516227
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
      value: 80.77673167451245
    - type: f1
      value: 77.60202561132175
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
      value: 82.09145931405514
    - type: f1
      value: 81.7701921473406
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
      value: 36.52153488185864
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
      value: 36.80090398444147
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
      value: 31.807141746058605
    - type: mrr
      value: 32.85025611455029
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
      value: 6.920999999999999
    - type: map_at_10
      value: 16.049
    - type: map_at_100
      value: 16.049
    - type: map_at_1000
      value: 16.049
    - type: map_at_3
      value: 11.865
    - type: map_at_5
      value: 13.657
    - type: mrr_at_1
      value: 53.87
    - type: mrr_at_10
      value: 62.291
    - type: mrr_at_100
      value: 62.291
    - type: mrr_at_1000
      value: 62.291
    - type: mrr_at_3
      value: 60.681
    - type: mrr_at_5
      value: 61.61
    - type: ndcg_at_1
      value: 51.23799999999999
    - type: ndcg_at_10
      value: 40.892
    - type: ndcg_at_100
      value: 26.951999999999998
    - type: ndcg_at_1000
      value: 26.474999999999998
    - type: ndcg_at_3
      value: 46.821
    - type: ndcg_at_5
      value: 44.333
    - type: precision_at_1
      value: 53.251000000000005
    - type: precision_at_10
      value: 30.124000000000002
    - type: precision_at_100
      value: 3.012
    - type: precision_at_1000
      value: 0.301
    - type: precision_at_3
      value: 43.55
    - type: precision_at_5
      value: 38.266
    - type: recall_at_1
      value: 6.920999999999999
    - type: recall_at_10
      value: 20.852
    - type: recall_at_100
      value: 20.852
    - type: recall_at_1000
      value: 20.852
    - type: recall_at_3
      value: 13.628000000000002
    - type: recall_at_5
      value: 16.273
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
      value: 46.827999999999996
    - type: map_at_10
      value: 63.434000000000005
    - type: map_at_100
      value: 63.434000000000005
    - type: map_at_1000
      value: 63.434000000000005
    - type: map_at_3
      value: 59.794000000000004
    - type: map_at_5
      value: 62.08
    - type: mrr_at_1
      value: 52.288999999999994
    - type: mrr_at_10
      value: 65.95
    - type: mrr_at_100
      value: 65.95
    - type: mrr_at_1000
      value: 65.95
    - type: mrr_at_3
      value: 63.413
    - type: mrr_at_5
      value: 65.08
    - type: ndcg_at_1
      value: 52.288999999999994
    - type: ndcg_at_10
      value: 70.301
    - type: ndcg_at_100
      value: 70.301
    - type: ndcg_at_1000
      value: 70.301
    - type: ndcg_at_3
      value: 63.979
    - type: ndcg_at_5
      value: 67.582
    - type: precision_at_1
      value: 52.288999999999994
    - type: precision_at_10
      value: 10.576
    - type: precision_at_100
      value: 1.058
    - type: precision_at_1000
      value: 0.106
    - type: precision_at_3
      value: 28.177000000000003
    - type: precision_at_5
      value: 19.073
    - type: recall_at_1
      value: 46.827999999999996
    - type: recall_at_10
      value: 88.236
    - type: recall_at_100
      value: 88.236
    - type: recall_at_1000
      value: 88.236
    - type: recall_at_3
      value: 72.371
    - type: recall_at_5
      value: 80.56
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
      value: 71.652
    - type: map_at_10
      value: 85.953
    - type: map_at_100
      value: 85.953
    - type: map_at_1000
      value: 85.953
    - type: map_at_3
      value: 83.05399999999999
    - type: map_at_5
      value: 84.89
    - type: mrr_at_1
      value: 82.42
    - type: mrr_at_10
      value: 88.473
    - type: mrr_at_100
      value: 88.473
    - type: mrr_at_1000
      value: 88.473
    - type: mrr_at_3
      value: 87.592
    - type: mrr_at_5
      value: 88.211
    - type: ndcg_at_1
      value: 82.44
    - type: ndcg_at_10
      value: 89.467
    - type: ndcg_at_100
      value: 89.33
    - type: ndcg_at_1000
      value: 89.33
    - type: ndcg_at_3
      value: 86.822
    - type: ndcg_at_5
      value: 88.307
    - type: precision_at_1
      value: 82.44
    - type: precision_at_10
      value: 13.616
    - type: precision_at_100
      value: 1.362
    - type: precision_at_1000
      value: 0.136
    - type: precision_at_3
      value: 38.117000000000004
    - type: precision_at_5
      value: 25.05
    - type: recall_at_1
      value: 71.652
    - type: recall_at_10
      value: 96.224
    - type: recall_at_100
      value: 96.224
    - type: recall_at_1000
      value: 96.224
    - type: recall_at_3
      value: 88.571
    - type: recall_at_5
      value: 92.812
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
      value: 61.295010338050474
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
      value: 67.26380819328142
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
      value: 5.683
    - type: map_at_10
      value: 14.924999999999999
    - type: map_at_100
      value: 17.532
    - type: map_at_1000
      value: 17.875
    - type: map_at_3
      value: 10.392
    - type: map_at_5
      value: 12.592
    - type: mrr_at_1
      value: 28.000000000000004
    - type: mrr_at_10
      value: 39.951
    - type: mrr_at_100
      value: 41.025
    - type: mrr_at_1000
      value: 41.056
    - type: mrr_at_3
      value: 36.317
    - type: mrr_at_5
      value: 38.412
    - type: ndcg_at_1
      value: 28.000000000000004
    - type: ndcg_at_10
      value: 24.410999999999998
    - type: ndcg_at_100
      value: 33.79
    - type: ndcg_at_1000
      value: 39.035
    - type: ndcg_at_3
      value: 22.845
    - type: ndcg_at_5
      value: 20.080000000000002
    - type: precision_at_1
      value: 28.000000000000004
    - type: precision_at_10
      value: 12.790000000000001
    - type: precision_at_100
      value: 2.633
    - type: precision_at_1000
      value: 0.388
    - type: precision_at_3
      value: 21.367
    - type: precision_at_5
      value: 17.7
    - type: recall_at_1
      value: 5.683
    - type: recall_at_10
      value: 25.91
    - type: recall_at_100
      value: 53.443
    - type: recall_at_1000
      value: 78.73
    - type: recall_at_3
      value: 13.003
    - type: recall_at_5
      value: 17.932000000000002
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
      value: 84.677978681023
    - type: cos_sim_spearman
      value: 83.13093441058189
    - type: euclidean_pearson
      value: 83.35535759341572
    - type: euclidean_spearman
      value: 83.42583744219611
    - type: manhattan_pearson
      value: 83.2243124045889
    - type: manhattan_spearman
      value: 83.39801618652632
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
      value: 81.68960206569666
    - type: cos_sim_spearman
      value: 77.3368966488535
    - type: euclidean_pearson
      value: 77.62828980560303
    - type: euclidean_spearman
      value: 76.77951481444651
    - type: manhattan_pearson
      value: 77.88637240839041
    - type: manhattan_spearman
      value: 77.22157841466188
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
      value: 84.18745821650724
    - type: cos_sim_spearman
      value: 85.04423285574542
    - type: euclidean_pearson
      value: 85.46604816931023
    - type: euclidean_spearman
      value: 85.5230593932974
    - type: manhattan_pearson
      value: 85.57912805986261
    - type: manhattan_spearman
      value: 85.65955905111873
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
      value: 83.6715333300355
    - type: cos_sim_spearman
      value: 82.9058522514908
    - type: euclidean_pearson
      value: 83.9640357424214
    - type: euclidean_spearman
      value: 83.60415457472637
    - type: manhattan_pearson
      value: 84.05621005853469
    - type: manhattan_spearman
      value: 83.87077724707746
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
      value: 87.82422928098886
    - type: cos_sim_spearman
      value: 88.12660311894628
    - type: euclidean_pearson
      value: 87.50974805056555
    - type: euclidean_spearman
      value: 87.91957275596677
    - type: manhattan_pearson
      value: 87.74119404878883
    - type: manhattan_spearman
      value: 88.2808922165719
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
      value: 84.80605838552093
    - type: cos_sim_spearman
      value: 86.24123388765678
    - type: euclidean_pearson
      value: 85.32648347339814
    - type: euclidean_spearman
      value: 85.60046671950158
    - type: manhattan_pearson
      value: 85.53800168487811
    - type: manhattan_spearman
      value: 85.89542420480763
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
      value: 89.87540978988132
    - type: cos_sim_spearman
      value: 90.12715295099461
    - type: euclidean_pearson
      value: 91.61085993525275
    - type: euclidean_spearman
      value: 91.31835942311758
    - type: manhattan_pearson
      value: 91.57500202032934
    - type: manhattan_spearman
      value: 91.1790925526635
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
      value: 69.87136205329556
    - type: cos_sim_spearman
      value: 68.6253154635078
    - type: euclidean_pearson
      value: 68.91536015034222
    - type: euclidean_spearman
      value: 67.63744649352542
    - type: manhattan_pearson
      value: 69.2000713045275
    - type: manhattan_spearman
      value: 68.16002901587316
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
      value: 85.21849551039082
    - type: cos_sim_spearman
      value: 85.6392959372461
    - type: euclidean_pearson
      value: 85.92050852609488
    - type: euclidean_spearman
      value: 85.97205649009734
    - type: manhattan_pearson
      value: 86.1031154802254
    - type: manhattan_spearman
      value: 86.26791155517466
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
      value: 86.83953958636627
    - type: mrr
      value: 96.71167612344082
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
      value: 64.994
    - type: map_at_10
      value: 74.763
    - type: map_at_100
      value: 75.127
    - type: map_at_1000
      value: 75.143
    - type: map_at_3
      value: 71.824
    - type: map_at_5
      value: 73.71
    - type: mrr_at_1
      value: 68.333
    - type: mrr_at_10
      value: 75.749
    - type: mrr_at_100
      value: 75.922
    - type: mrr_at_1000
      value: 75.938
    - type: mrr_at_3
      value: 73.556
    - type: mrr_at_5
      value: 74.739
    - type: ndcg_at_1
      value: 68.333
    - type: ndcg_at_10
      value: 79.174
    - type: ndcg_at_100
      value: 80.41
    - type: ndcg_at_1000
      value: 80.804
    - type: ndcg_at_3
      value: 74.361
    - type: ndcg_at_5
      value: 76.861
    - type: precision_at_1
      value: 68.333
    - type: precision_at_10
      value: 10.333
    - type: precision_at_100
      value: 1.0999999999999999
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 28.778
    - type: precision_at_5
      value: 19.067
    - type: recall_at_1
      value: 64.994
    - type: recall_at_10
      value: 91.822
    - type: recall_at_100
      value: 97.0
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 78.878
    - type: recall_at_5
      value: 85.172
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
      value: 99.72079207920792
    - type: cos_sim_ap
      value: 93.00265215525152
    - type: cos_sim_f1
      value: 85.06596306068602
    - type: cos_sim_precision
      value: 90.05586592178771
    - type: cos_sim_recall
      value: 80.60000000000001
    - type: dot_accuracy
      value: 99.66039603960397
    - type: dot_ap
      value: 91.22371407479089
    - type: dot_f1
      value: 82.34693877551021
    - type: dot_precision
      value: 84.0625
    - type: dot_recall
      value: 80.7
    - type: euclidean_accuracy
      value: 99.71881188118812
    - type: euclidean_ap
      value: 92.88449963304728
    - type: euclidean_f1
      value: 85.19480519480518
    - type: euclidean_precision
      value: 88.64864864864866
    - type: euclidean_recall
      value: 82.0
    - type: manhattan_accuracy
      value: 99.73267326732673
    - type: manhattan_ap
      value: 93.23055393056883
    - type: manhattan_f1
      value: 85.88957055214725
    - type: manhattan_precision
      value: 87.86610878661088
    - type: manhattan_recall
      value: 84.0
    - type: max_accuracy
      value: 99.73267326732673
    - type: max_ap
      value: 93.23055393056883
    - type: max_f1
      value: 85.88957055214725
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
      value: 77.3305735900358
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
      value: 41.32967136540674
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
      value: 55.95514866379359
    - type: mrr
      value: 56.95423245055598
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
      value: 30.783007208997144
    - type: cos_sim_spearman
      value: 30.373444721540533
    - type: dot_pearson
      value: 29.210604111143905
    - type: dot_spearman
      value: 29.98809758085659
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
      value: 0.234
    - type: map_at_10
      value: 1.894
    - type: map_at_100
      value: 1.894
    - type: map_at_1000
      value: 1.894
    - type: map_at_3
      value: 0.636
    - type: map_at_5
      value: 1.0
    - type: mrr_at_1
      value: 88.0
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
      value: 85.0
    - type: ndcg_at_10
      value: 74.798
    - type: ndcg_at_100
      value: 16.462
    - type: ndcg_at_1000
      value: 7.0889999999999995
    - type: ndcg_at_3
      value: 80.754
    - type: ndcg_at_5
      value: 77.319
    - type: precision_at_1
      value: 88.0
    - type: precision_at_10
      value: 78.0
    - type: precision_at_100
      value: 7.8
    - type: precision_at_1000
      value: 0.7799999999999999
    - type: precision_at_3
      value: 83.333
    - type: precision_at_5
      value: 80.80000000000001
    - type: recall_at_1
      value: 0.234
    - type: recall_at_10
      value: 2.093
    - type: recall_at_100
      value: 2.093
    - type: recall_at_1000
      value: 2.093
    - type: recall_at_3
      value: 0.662
    - type: recall_at_5
      value: 1.0739999999999998
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
      value: 2.703
    - type: map_at_10
      value: 10.866000000000001
    - type: map_at_100
      value: 10.866000000000001
    - type: map_at_1000
      value: 10.866000000000001
    - type: map_at_3
      value: 5.909
    - type: map_at_5
      value: 7.35
    - type: mrr_at_1
      value: 36.735
    - type: mrr_at_10
      value: 53.583000000000006
    - type: mrr_at_100
      value: 53.583000000000006
    - type: mrr_at_1000
      value: 53.583000000000006
    - type: mrr_at_3
      value: 49.32
    - type: mrr_at_5
      value: 51.769
    - type: ndcg_at_1
      value: 34.694
    - type: ndcg_at_10
      value: 27.926000000000002
    - type: ndcg_at_100
      value: 22.701
    - type: ndcg_at_1000
      value: 22.701
    - type: ndcg_at_3
      value: 32.073
    - type: ndcg_at_5
      value: 28.327999999999996
    - type: precision_at_1
      value: 36.735
    - type: precision_at_10
      value: 24.694
    - type: precision_at_100
      value: 2.469
    - type: precision_at_1000
      value: 0.247
    - type: precision_at_3
      value: 31.973000000000003
    - type: precision_at_5
      value: 26.939
    - type: recall_at_1
      value: 2.703
    - type: recall_at_10
      value: 17.702
    - type: recall_at_100
      value: 17.702
    - type: recall_at_1000
      value: 17.702
    - type: recall_at_3
      value: 7.208
    - type: recall_at_5
      value: 9.748999999999999
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
      value: 70.79960000000001
    - type: ap
      value: 15.467565415565815
    - type: f1
      value: 55.28639823443618
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
      value: 64.7792869269949
    - type: f1
      value: 65.08597154774318
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
      value: 55.70352297774293
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
      value: 88.27561542588067
    - type: cos_sim_ap
      value: 81.08262141256193
    - type: cos_sim_f1
      value: 73.82341501361338
    - type: cos_sim_precision
      value: 72.5720112159062
    - type: cos_sim_recall
      value: 75.11873350923483
    - type: dot_accuracy
      value: 86.66030875603504
    - type: dot_ap
      value: 76.6052349228621
    - type: dot_f1
      value: 70.13897280966768
    - type: dot_precision
      value: 64.70457079152732
    - type: dot_recall
      value: 76.56992084432717
    - type: euclidean_accuracy
      value: 88.37098408535495
    - type: euclidean_ap
      value: 81.12515230092113
    - type: euclidean_f1
      value: 74.10338225909379
    - type: euclidean_precision
      value: 71.76761433868974
    - type: euclidean_recall
      value: 76.59630606860158
    - type: manhattan_accuracy
      value: 88.34118137926924
    - type: manhattan_ap
      value: 80.95751834536561
    - type: manhattan_f1
      value: 73.9119496855346
    - type: manhattan_precision
      value: 70.625
    - type: manhattan_recall
      value: 77.5197889182058
    - type: max_accuracy
      value: 88.37098408535495
    - type: max_ap
      value: 81.12515230092113
    - type: max_f1
      value: 74.10338225909379
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
      value: 89.79896767182831
    - type: cos_sim_ap
      value: 87.40071784061065
    - type: cos_sim_f1
      value: 79.87753144712087
    - type: cos_sim_precision
      value: 76.67304015296367
    - type: cos_sim_recall
      value: 83.3615645210964
    - type: dot_accuracy
      value: 88.95486474948578
    - type: dot_ap
      value: 86.00227979119943
    - type: dot_f1
      value: 78.54601474525914
    - type: dot_precision
      value: 75.00525394045535
    - type: dot_recall
      value: 82.43763473975977
    - type: euclidean_accuracy
      value: 89.7892653393876
    - type: euclidean_ap
      value: 87.42174706480819
    - type: euclidean_f1
      value: 80.07283321194465
    - type: euclidean_precision
      value: 75.96738529574351
    - type: euclidean_recall
      value: 84.6473668001232
    - type: manhattan_accuracy
      value: 89.8474793340319
    - type: manhattan_ap
      value: 87.47814292587448
    - type: manhattan_f1
      value: 80.15461150280949
    - type: manhattan_precision
      value: 74.88798234468
    - type: manhattan_recall
      value: 86.21804742839544
    - type: max_accuracy
      value: 89.8474793340319
    - type: max_ap
      value: 87.47814292587448
    - type: max_f1
      value: 80.15461150280949
---

# Model Summary

> GritLM is a generative representational instruction tuned language model. It unifies text representation (embedding) and text generation into a single model achieving state-of-the-art performance on both types of tasks.

- **Repository:** [ContextualAI/gritlm](https://github.com/ContextualAI/gritlm)
- **Paper:** https://arxiv.org/abs/2402.09906
- **Logs:** https://wandb.ai/muennighoff/gritlm/runs/0uui712t/overview
- **Script:** https://github.com/ContextualAI/gritlm/blob/main/scripts/training/train_gritlm_7b.sh

| Model | Description |
|-------|-------------|
| [GritLM 7B](https://hf.co/GritLM/GritLM-7B) | Mistral 7B finetuned using GRIT |
| [GritLM 8x7B](https://hf.co/GritLM/GritLM-8x7B) | Mixtral 8x7B finetuned using GRIT |

# Use

The model usage is documented [here](https://github.com/ContextualAI/gritlm?tab=readme-ov-file#inference).

# Citation

```bibtex
@misc{muennighoff2024generative,
      title={Generative Representational Instruction Tuning}, 
      author={Niklas Muennighoff and Hongjin Su and Liang Wang and Nan Yang and Furu Wei and Tao Yu and Amanpreet Singh and Douwe Kiela},
      year={2024},
      eprint={2402.09906},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```