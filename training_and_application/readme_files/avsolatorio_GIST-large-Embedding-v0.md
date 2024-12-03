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
- name: GIST-large-Embedding-v0
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
      value: 75.5820895522388
    - type: ap
      value: 38.32190121241783
    - type: f1
      value: 69.44777155231054
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
      value: 93.40514999999998
    - type: ap
      value: 90.2011565132406
    - type: f1
      value: 93.39486246843605
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
      value: 49.05999999999999
    - type: f1
      value: 48.58702718571088
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
      value: 38.407000000000004
    - type: map_at_10
      value: 54.822
    - type: map_at_100
      value: 55.387
    - type: map_at_1000
      value: 55.388999999999996
    - type: map_at_3
      value: 50.308
    - type: map_at_5
      value: 53.199
    - type: mrr_at_1
      value: 39.900000000000006
    - type: mrr_at_10
      value: 55.385
    - type: mrr_at_100
      value: 55.936
    - type: mrr_at_1000
      value: 55.93900000000001
    - type: mrr_at_3
      value: 50.853
    - type: mrr_at_5
      value: 53.738
    - type: ndcg_at_1
      value: 38.407000000000004
    - type: ndcg_at_10
      value: 63.38
    - type: ndcg_at_100
      value: 65.52900000000001
    - type: ndcg_at_1000
      value: 65.58800000000001
    - type: ndcg_at_3
      value: 54.26
    - type: ndcg_at_5
      value: 59.488
    - type: precision_at_1
      value: 38.407000000000004
    - type: precision_at_10
      value: 9.04
    - type: precision_at_100
      value: 0.992
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 21.906
    - type: precision_at_5
      value: 15.690000000000001
    - type: recall_at_1
      value: 38.407000000000004
    - type: recall_at_10
      value: 90.398
    - type: recall_at_100
      value: 99.21799999999999
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 65.718
    - type: recall_at_5
      value: 78.45
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
      value: 48.49766333679089
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
      value: 42.57731111438094
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
      value: 64.70120072857361
    - type: mrr
      value: 77.86714593501297
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
      value: 90.73821860690765
    - type: cos_sim_spearman
      value: 89.17070651383446
    - type: euclidean_pearson
      value: 88.28303958293029
    - type: euclidean_spearman
      value: 88.81889126856979
    - type: manhattan_pearson
      value: 88.09080621828731
    - type: manhattan_spearman
      value: 88.55924679817751
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
      value: 88.10064935064933
    - type: f1
      value: 88.08460758973867
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
      value: 39.338228337929976
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
      value: 36.179156232378226
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
      value: 33.440999999999995
    - type: map_at_10
      value: 45.495000000000005
    - type: map_at_100
      value: 47.132000000000005
    - type: map_at_1000
      value: 47.253
    - type: map_at_3
      value: 41.766
    - type: map_at_5
      value: 43.873
    - type: mrr_at_1
      value: 40.772999999999996
    - type: mrr_at_10
      value: 51.627
    - type: mrr_at_100
      value: 52.364
    - type: mrr_at_1000
      value: 52.397000000000006
    - type: mrr_at_3
      value: 48.951
    - type: mrr_at_5
      value: 50.746
    - type: ndcg_at_1
      value: 40.772999999999996
    - type: ndcg_at_10
      value: 52.306
    - type: ndcg_at_100
      value: 57.753
    - type: ndcg_at_1000
      value: 59.36900000000001
    - type: ndcg_at_3
      value: 47.177
    - type: ndcg_at_5
      value: 49.71
    - type: precision_at_1
      value: 40.772999999999996
    - type: precision_at_10
      value: 10.129000000000001
    - type: precision_at_100
      value: 1.617
    - type: precision_at_1000
      value: 0.208
    - type: precision_at_3
      value: 22.985
    - type: precision_at_5
      value: 16.652
    - type: recall_at_1
      value: 33.440999999999995
    - type: recall_at_10
      value: 65.121
    - type: recall_at_100
      value: 87.55199999999999
    - type: recall_at_1000
      value: 97.41300000000001
    - type: recall_at_3
      value: 49.958999999999996
    - type: recall_at_5
      value: 57.14900000000001
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
      value: 32.126
    - type: map_at_10
      value: 42.856
    - type: map_at_100
      value: 44.134
    - type: map_at_1000
      value: 44.274
    - type: map_at_3
      value: 39.594
    - type: map_at_5
      value: 41.504999999999995
    - type: mrr_at_1
      value: 40.127
    - type: mrr_at_10
      value: 48.736000000000004
    - type: mrr_at_100
      value: 49.303999999999995
    - type: mrr_at_1000
      value: 49.356
    - type: mrr_at_3
      value: 46.263
    - type: mrr_at_5
      value: 47.878
    - type: ndcg_at_1
      value: 40.127
    - type: ndcg_at_10
      value: 48.695
    - type: ndcg_at_100
      value: 52.846000000000004
    - type: ndcg_at_1000
      value: 54.964
    - type: ndcg_at_3
      value: 44.275
    - type: ndcg_at_5
      value: 46.54
    - type: precision_at_1
      value: 40.127
    - type: precision_at_10
      value: 9.229
    - type: precision_at_100
      value: 1.473
    - type: precision_at_1000
      value: 0.19499999999999998
    - type: precision_at_3
      value: 21.444
    - type: precision_at_5
      value: 15.389
    - type: recall_at_1
      value: 32.126
    - type: recall_at_10
      value: 58.971
    - type: recall_at_100
      value: 76.115
    - type: recall_at_1000
      value: 89.556
    - type: recall_at_3
      value: 45.891
    - type: recall_at_5
      value: 52.242
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
      value: 41.312
    - type: map_at_10
      value: 54.510000000000005
    - type: map_at_100
      value: 55.544000000000004
    - type: map_at_1000
      value: 55.593
    - type: map_at_3
      value: 50.859
    - type: map_at_5
      value: 52.839999999999996
    - type: mrr_at_1
      value: 47.147
    - type: mrr_at_10
      value: 57.678
    - type: mrr_at_100
      value: 58.287
    - type: mrr_at_1000
      value: 58.312
    - type: mrr_at_3
      value: 55.025999999999996
    - type: mrr_at_5
      value: 56.55
    - type: ndcg_at_1
      value: 47.147
    - type: ndcg_at_10
      value: 60.672000000000004
    - type: ndcg_at_100
      value: 64.411
    - type: ndcg_at_1000
      value: 65.35499999999999
    - type: ndcg_at_3
      value: 54.643
    - type: ndcg_at_5
      value: 57.461
    - type: precision_at_1
      value: 47.147
    - type: precision_at_10
      value: 9.881
    - type: precision_at_100
      value: 1.27
    - type: precision_at_1000
      value: 0.13799999999999998
    - type: precision_at_3
      value: 24.556
    - type: precision_at_5
      value: 16.814999999999998
    - type: recall_at_1
      value: 41.312
    - type: recall_at_10
      value: 75.62299999999999
    - type: recall_at_100
      value: 91.388
    - type: recall_at_1000
      value: 98.08
    - type: recall_at_3
      value: 59.40299999999999
    - type: recall_at_5
      value: 66.43900000000001
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
      value: 27.609
    - type: map_at_10
      value: 37.614
    - type: map_at_100
      value: 38.584
    - type: map_at_1000
      value: 38.652
    - type: map_at_3
      value: 34.731
    - type: map_at_5
      value: 36.308
    - type: mrr_at_1
      value: 29.944
    - type: mrr_at_10
      value: 39.829
    - type: mrr_at_100
      value: 40.659
    - type: mrr_at_1000
      value: 40.709
    - type: mrr_at_3
      value: 37.269000000000005
    - type: mrr_at_5
      value: 38.625
    - type: ndcg_at_1
      value: 29.944
    - type: ndcg_at_10
      value: 43.082
    - type: ndcg_at_100
      value: 47.857
    - type: ndcg_at_1000
      value: 49.612
    - type: ndcg_at_3
      value: 37.578
    - type: ndcg_at_5
      value: 40.135
    - type: precision_at_1
      value: 29.944
    - type: precision_at_10
      value: 6.678000000000001
    - type: precision_at_100
      value: 0.951
    - type: precision_at_1000
      value: 0.11399999999999999
    - type: precision_at_3
      value: 16.045
    - type: precision_at_5
      value: 11.073
    - type: recall_at_1
      value: 27.609
    - type: recall_at_10
      value: 57.718
    - type: recall_at_100
      value: 79.768
    - type: recall_at_1000
      value: 92.868
    - type: recall_at_3
      value: 42.876
    - type: recall_at_5
      value: 49.104
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
      value: 18.071
    - type: map_at_10
      value: 27.471
    - type: map_at_100
      value: 28.71
    - type: map_at_1000
      value: 28.833
    - type: map_at_3
      value: 24.698
    - type: map_at_5
      value: 26.461000000000002
    - type: mrr_at_1
      value: 22.387999999999998
    - type: mrr_at_10
      value: 32.522
    - type: mrr_at_100
      value: 33.393
    - type: mrr_at_1000
      value: 33.455
    - type: mrr_at_3
      value: 29.830000000000002
    - type: mrr_at_5
      value: 31.472
    - type: ndcg_at_1
      value: 22.387999999999998
    - type: ndcg_at_10
      value: 33.278999999999996
    - type: ndcg_at_100
      value: 39.043
    - type: ndcg_at_1000
      value: 41.763
    - type: ndcg_at_3
      value: 28.310999999999996
    - type: ndcg_at_5
      value: 31.007
    - type: precision_at_1
      value: 22.387999999999998
    - type: precision_at_10
      value: 6.157
    - type: precision_at_100
      value: 1.042
    - type: precision_at_1000
      value: 0.14200000000000002
    - type: precision_at_3
      value: 13.972000000000001
    - type: precision_at_5
      value: 10.274
    - type: recall_at_1
      value: 18.071
    - type: recall_at_10
      value: 46.025
    - type: recall_at_100
      value: 71.153
    - type: recall_at_1000
      value: 90.232
    - type: recall_at_3
      value: 32.311
    - type: recall_at_5
      value: 39.296
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
      value: 30.813000000000002
    - type: map_at_10
      value: 42.594
    - type: map_at_100
      value: 43.949
    - type: map_at_1000
      value: 44.052
    - type: map_at_3
      value: 39.1
    - type: map_at_5
      value: 41.111
    - type: mrr_at_1
      value: 37.824999999999996
    - type: mrr_at_10
      value: 48.06
    - type: mrr_at_100
      value: 48.91
    - type: mrr_at_1000
      value: 48.946
    - type: mrr_at_3
      value: 45.509
    - type: mrr_at_5
      value: 47.073
    - type: ndcg_at_1
      value: 37.824999999999996
    - type: ndcg_at_10
      value: 48.882
    - type: ndcg_at_100
      value: 54.330999999999996
    - type: ndcg_at_1000
      value: 56.120999999999995
    - type: ndcg_at_3
      value: 43.529
    - type: ndcg_at_5
      value: 46.217999999999996
    - type: precision_at_1
      value: 37.824999999999996
    - type: precision_at_10
      value: 8.845
    - type: precision_at_100
      value: 1.34
    - type: precision_at_1000
      value: 0.168
    - type: precision_at_3
      value: 20.757
    - type: precision_at_5
      value: 14.802999999999999
    - type: recall_at_1
      value: 30.813000000000002
    - type: recall_at_10
      value: 61.895999999999994
    - type: recall_at_100
      value: 84.513
    - type: recall_at_1000
      value: 95.817
    - type: recall_at_3
      value: 47.099000000000004
    - type: recall_at_5
      value: 54.031
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
      value: 25.735999999999997
    - type: map_at_10
      value: 36.799
    - type: map_at_100
      value: 38.246
    - type: map_at_1000
      value: 38.353
    - type: map_at_3
      value: 33.133
    - type: map_at_5
      value: 34.954
    - type: mrr_at_1
      value: 31.849
    - type: mrr_at_10
      value: 41.928
    - type: mrr_at_100
      value: 42.846000000000004
    - type: mrr_at_1000
      value: 42.894
    - type: mrr_at_3
      value: 39.117000000000004
    - type: mrr_at_5
      value: 40.521
    - type: ndcg_at_1
      value: 31.849
    - type: ndcg_at_10
      value: 43.143
    - type: ndcg_at_100
      value: 48.963
    - type: ndcg_at_1000
      value: 51.041000000000004
    - type: ndcg_at_3
      value: 37.218
    - type: ndcg_at_5
      value: 39.542
    - type: precision_at_1
      value: 31.849
    - type: precision_at_10
      value: 8.231
    - type: precision_at_100
      value: 1.277
    - type: precision_at_1000
      value: 0.164
    - type: precision_at_3
      value: 18.037
    - type: precision_at_5
      value: 12.945
    - type: recall_at_1
      value: 25.735999999999997
    - type: recall_at_10
      value: 56.735
    - type: recall_at_100
      value: 81.04
    - type: recall_at_1000
      value: 94.845
    - type: recall_at_3
      value: 40.239999999999995
    - type: recall_at_5
      value: 46.378
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
      value: 27.580333333333336
    - type: map_at_10
      value: 37.70558333333334
    - type: map_at_100
      value: 38.94941666666667
    - type: map_at_1000
      value: 39.062083333333334
    - type: map_at_3
      value: 34.63333333333334
    - type: map_at_5
      value: 36.35241666666666
    - type: mrr_at_1
      value: 32.64866666666667
    - type: mrr_at_10
      value: 42.018499999999996
    - type: mrr_at_100
      value: 42.83391666666666
    - type: mrr_at_1000
      value: 42.884166666666665
    - type: mrr_at_3
      value: 39.476499999999994
    - type: mrr_at_5
      value: 40.96983333333334
    - type: ndcg_at_1
      value: 32.64866666666667
    - type: ndcg_at_10
      value: 43.43866666666667
    - type: ndcg_at_100
      value: 48.569833333333335
    - type: ndcg_at_1000
      value: 50.6495
    - type: ndcg_at_3
      value: 38.327166666666656
    - type: ndcg_at_5
      value: 40.76941666666667
    - type: precision_at_1
      value: 32.64866666666667
    - type: precision_at_10
      value: 7.652333333333332
    - type: precision_at_100
      value: 1.2066666666666666
    - type: precision_at_1000
      value: 0.15841666666666668
    - type: precision_at_3
      value: 17.75108333333333
    - type: precision_at_5
      value: 12.641916666666669
    - type: recall_at_1
      value: 27.580333333333336
    - type: recall_at_10
      value: 56.02591666666667
    - type: recall_at_100
      value: 78.317
    - type: recall_at_1000
      value: 92.52608333333332
    - type: recall_at_3
      value: 41.84283333333333
    - type: recall_at_5
      value: 48.105666666666664
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
      value: 27.876
    - type: map_at_10
      value: 34.521
    - type: map_at_100
      value: 35.581
    - type: map_at_1000
      value: 35.674
    - type: map_at_3
      value: 32.501000000000005
    - type: map_at_5
      value: 33.602
    - type: mrr_at_1
      value: 31.441999999999997
    - type: mrr_at_10
      value: 37.669999999999995
    - type: mrr_at_100
      value: 38.523
    - type: mrr_at_1000
      value: 38.59
    - type: mrr_at_3
      value: 35.762
    - type: mrr_at_5
      value: 36.812
    - type: ndcg_at_1
      value: 31.441999999999997
    - type: ndcg_at_10
      value: 38.46
    - type: ndcg_at_100
      value: 43.479
    - type: ndcg_at_1000
      value: 45.858
    - type: ndcg_at_3
      value: 34.668
    - type: ndcg_at_5
      value: 36.416
    - type: precision_at_1
      value: 31.441999999999997
    - type: precision_at_10
      value: 5.782
    - type: precision_at_100
      value: 0.91
    - type: precision_at_1000
      value: 0.11900000000000001
    - type: precision_at_3
      value: 14.417
    - type: precision_at_5
      value: 9.876999999999999
    - type: recall_at_1
      value: 27.876
    - type: recall_at_10
      value: 47.556
    - type: recall_at_100
      value: 70.39699999999999
    - type: recall_at_1000
      value: 87.969
    - type: recall_at_3
      value: 37.226
    - type: recall_at_5
      value: 41.43
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
      value: 18.854000000000003
    - type: map_at_10
      value: 26.632
    - type: map_at_100
      value: 27.849
    - type: map_at_1000
      value: 27.977
    - type: map_at_3
      value: 24.089
    - type: map_at_5
      value: 25.477
    - type: mrr_at_1
      value: 22.987
    - type: mrr_at_10
      value: 30.781999999999996
    - type: mrr_at_100
      value: 31.746000000000002
    - type: mrr_at_1000
      value: 31.818
    - type: mrr_at_3
      value: 28.43
    - type: mrr_at_5
      value: 29.791
    - type: ndcg_at_1
      value: 22.987
    - type: ndcg_at_10
      value: 31.585
    - type: ndcg_at_100
      value: 37.32
    - type: ndcg_at_1000
      value: 40.072
    - type: ndcg_at_3
      value: 27.058
    - type: ndcg_at_5
      value: 29.137999999999998
    - type: precision_at_1
      value: 22.987
    - type: precision_at_10
      value: 5.76
    - type: precision_at_100
      value: 1.018
    - type: precision_at_1000
      value: 0.14400000000000002
    - type: precision_at_3
      value: 12.767000000000001
    - type: precision_at_5
      value: 9.257
    - type: recall_at_1
      value: 18.854000000000003
    - type: recall_at_10
      value: 42.349
    - type: recall_at_100
      value: 68.15299999999999
    - type: recall_at_1000
      value: 87.44
    - type: recall_at_3
      value: 29.715999999999998
    - type: recall_at_5
      value: 35.085
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
      value: 28.094
    - type: map_at_10
      value: 38.22
    - type: map_at_100
      value: 39.352
    - type: map_at_1000
      value: 39.452
    - type: map_at_3
      value: 35.339
    - type: map_at_5
      value: 36.78
    - type: mrr_at_1
      value: 33.022
    - type: mrr_at_10
      value: 42.466
    - type: mrr_at_100
      value: 43.3
    - type: mrr_at_1000
      value: 43.356
    - type: mrr_at_3
      value: 40.159
    - type: mrr_at_5
      value: 41.272999999999996
    - type: ndcg_at_1
      value: 33.022
    - type: ndcg_at_10
      value: 43.976
    - type: ndcg_at_100
      value: 49.008
    - type: ndcg_at_1000
      value: 51.154999999999994
    - type: ndcg_at_3
      value: 38.891
    - type: ndcg_at_5
      value: 40.897
    - type: precision_at_1
      value: 33.022
    - type: precision_at_10
      value: 7.396999999999999
    - type: precision_at_100
      value: 1.1199999999999999
    - type: precision_at_1000
      value: 0.14200000000000002
    - type: precision_at_3
      value: 17.724
    - type: precision_at_5
      value: 12.239
    - type: recall_at_1
      value: 28.094
    - type: recall_at_10
      value: 57.162
    - type: recall_at_100
      value: 78.636
    - type: recall_at_1000
      value: 93.376
    - type: recall_at_3
      value: 43.328
    - type: recall_at_5
      value: 48.252
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
      value: 24.937
    - type: map_at_10
      value: 34.82
    - type: map_at_100
      value: 36.405
    - type: map_at_1000
      value: 36.626
    - type: map_at_3
      value: 31.548
    - type: map_at_5
      value: 33.355000000000004
    - type: mrr_at_1
      value: 30.435000000000002
    - type: mrr_at_10
      value: 39.946
    - type: mrr_at_100
      value: 40.873
    - type: mrr_at_1000
      value: 40.910000000000004
    - type: mrr_at_3
      value: 37.088
    - type: mrr_at_5
      value: 38.808
    - type: ndcg_at_1
      value: 30.435000000000002
    - type: ndcg_at_10
      value: 41.25
    - type: ndcg_at_100
      value: 47.229
    - type: ndcg_at_1000
      value: 49.395
    - type: ndcg_at_3
      value: 35.801
    - type: ndcg_at_5
      value: 38.457
    - type: precision_at_1
      value: 30.435000000000002
    - type: precision_at_10
      value: 8.083
    - type: precision_at_100
      value: 1.601
    - type: precision_at_1000
      value: 0.247
    - type: precision_at_3
      value: 17.061999999999998
    - type: precision_at_5
      value: 12.767000000000001
    - type: recall_at_1
      value: 24.937
    - type: recall_at_10
      value: 53.905
    - type: recall_at_100
      value: 80.607
    - type: recall_at_1000
      value: 93.728
    - type: recall_at_3
      value: 38.446000000000005
    - type: recall_at_5
      value: 45.188
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
      value: 22.095000000000002
    - type: map_at_10
      value: 30.935000000000002
    - type: map_at_100
      value: 31.907000000000004
    - type: map_at_1000
      value: 32.006
    - type: map_at_3
      value: 28.242
    - type: map_at_5
      value: 29.963
    - type: mrr_at_1
      value: 23.845
    - type: mrr_at_10
      value: 32.978
    - type: mrr_at_100
      value: 33.802
    - type: mrr_at_1000
      value: 33.867000000000004
    - type: mrr_at_3
      value: 30.314000000000004
    - type: mrr_at_5
      value: 32.089
    - type: ndcg_at_1
      value: 23.845
    - type: ndcg_at_10
      value: 35.934
    - type: ndcg_at_100
      value: 40.598
    - type: ndcg_at_1000
      value: 43.089
    - type: ndcg_at_3
      value: 30.776999999999997
    - type: ndcg_at_5
      value: 33.711999999999996
    - type: precision_at_1
      value: 23.845
    - type: precision_at_10
      value: 5.656
    - type: precision_at_100
      value: 0.861
    - type: precision_at_1000
      value: 0.12
    - type: precision_at_3
      value: 13.247
    - type: precision_at_5
      value: 9.612
    - type: recall_at_1
      value: 22.095000000000002
    - type: recall_at_10
      value: 49.25
    - type: recall_at_100
      value: 70.482
    - type: recall_at_1000
      value: 88.98899999999999
    - type: recall_at_3
      value: 35.619
    - type: recall_at_5
      value: 42.674
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
      value: 14.154
    - type: map_at_10
      value: 24.654999999999998
    - type: map_at_100
      value: 26.723999999999997
    - type: map_at_1000
      value: 26.912000000000003
    - type: map_at_3
      value: 20.4
    - type: map_at_5
      value: 22.477
    - type: mrr_at_1
      value: 32.117000000000004
    - type: mrr_at_10
      value: 44.590999999999994
    - type: mrr_at_100
      value: 45.425
    - type: mrr_at_1000
      value: 45.456
    - type: mrr_at_3
      value: 41.281
    - type: mrr_at_5
      value: 43.219
    - type: ndcg_at_1
      value: 32.117000000000004
    - type: ndcg_at_10
      value: 33.994
    - type: ndcg_at_100
      value: 41.438
    - type: ndcg_at_1000
      value: 44.611000000000004
    - type: ndcg_at_3
      value: 27.816000000000003
    - type: ndcg_at_5
      value: 29.816
    - type: precision_at_1
      value: 32.117000000000004
    - type: precision_at_10
      value: 10.756
    - type: precision_at_100
      value: 1.8679999999999999
    - type: precision_at_1000
      value: 0.246
    - type: precision_at_3
      value: 20.803
    - type: precision_at_5
      value: 15.987000000000002
    - type: recall_at_1
      value: 14.154
    - type: recall_at_10
      value: 40.489999999999995
    - type: recall_at_100
      value: 65.635
    - type: recall_at_1000
      value: 83.276
    - type: recall_at_3
      value: 25.241000000000003
    - type: recall_at_5
      value: 31.211
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
      value: 9.332
    - type: map_at_10
      value: 20.462
    - type: map_at_100
      value: 29.473
    - type: map_at_1000
      value: 31.215
    - type: map_at_3
      value: 14.466999999999999
    - type: map_at_5
      value: 16.922
    - type: mrr_at_1
      value: 69.5
    - type: mrr_at_10
      value: 77.039
    - type: mrr_at_100
      value: 77.265
    - type: mrr_at_1000
      value: 77.271
    - type: mrr_at_3
      value: 75.5
    - type: mrr_at_5
      value: 76.4
    - type: ndcg_at_1
      value: 57.125
    - type: ndcg_at_10
      value: 42.958
    - type: ndcg_at_100
      value: 48.396
    - type: ndcg_at_1000
      value: 55.897
    - type: ndcg_at_3
      value: 47.188
    - type: ndcg_at_5
      value: 44.376
    - type: precision_at_1
      value: 69.5
    - type: precision_at_10
      value: 34.5
    - type: precision_at_100
      value: 11.18
    - type: precision_at_1000
      value: 2.13
    - type: precision_at_3
      value: 51.083
    - type: precision_at_5
      value: 43.1
    - type: recall_at_1
      value: 9.332
    - type: recall_at_10
      value: 26.422
    - type: recall_at_100
      value: 56.098000000000006
    - type: recall_at_1000
      value: 79.66
    - type: recall_at_3
      value: 15.703
    - type: recall_at_5
      value: 19.644000000000002
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
      value: 54.72
    - type: f1
      value: 49.67819606587526
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
      value: 74.97
    - type: map_at_10
      value: 82.956
    - type: map_at_100
      value: 83.193
    - type: map_at_1000
      value: 83.208
    - type: map_at_3
      value: 81.837
    - type: map_at_5
      value: 82.57
    - type: mrr_at_1
      value: 80.783
    - type: mrr_at_10
      value: 87.546
    - type: mrr_at_100
      value: 87.627
    - type: mrr_at_1000
      value: 87.63
    - type: mrr_at_3
      value: 86.79400000000001
    - type: mrr_at_5
      value: 87.32799999999999
    - type: ndcg_at_1
      value: 80.783
    - type: ndcg_at_10
      value: 86.54899999999999
    - type: ndcg_at_100
      value: 87.355
    - type: ndcg_at_1000
      value: 87.629
    - type: ndcg_at_3
      value: 84.82
    - type: ndcg_at_5
      value: 85.83800000000001
    - type: precision_at_1
      value: 80.783
    - type: precision_at_10
      value: 10.327
    - type: precision_at_100
      value: 1.094
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 32.218
    - type: precision_at_5
      value: 20.012
    - type: recall_at_1
      value: 74.97
    - type: recall_at_10
      value: 93.072
    - type: recall_at_100
      value: 96.218
    - type: recall_at_1000
      value: 97.991
    - type: recall_at_3
      value: 88.357
    - type: recall_at_5
      value: 90.983
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
      value: 21.12
    - type: map_at_10
      value: 35.908
    - type: map_at_100
      value: 37.895
    - type: map_at_1000
      value: 38.068000000000005
    - type: map_at_3
      value: 31.189
    - type: map_at_5
      value: 33.908
    - type: mrr_at_1
      value: 42.901
    - type: mrr_at_10
      value: 52.578
    - type: mrr_at_100
      value: 53.308
    - type: mrr_at_1000
      value: 53.342
    - type: mrr_at_3
      value: 50.385999999999996
    - type: mrr_at_5
      value: 51.62799999999999
    - type: ndcg_at_1
      value: 42.901
    - type: ndcg_at_10
      value: 44.302
    - type: ndcg_at_100
      value: 51.132999999999996
    - type: ndcg_at_1000
      value: 53.848
    - type: ndcg_at_3
      value: 40.464
    - type: ndcg_at_5
      value: 41.743
    - type: precision_at_1
      value: 42.901
    - type: precision_at_10
      value: 12.423
    - type: precision_at_100
      value: 1.968
    - type: precision_at_1000
      value: 0.246
    - type: precision_at_3
      value: 27.622999999999998
    - type: precision_at_5
      value: 20.278
    - type: recall_at_1
      value: 21.12
    - type: recall_at_10
      value: 52.091
    - type: recall_at_100
      value: 77.062
    - type: recall_at_1000
      value: 93.082
    - type: recall_at_3
      value: 37.223
    - type: recall_at_5
      value: 43.826
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
      value: 38.940000000000005
    - type: map_at_10
      value: 62.239999999999995
    - type: map_at_100
      value: 63.141000000000005
    - type: map_at_1000
      value: 63.205999999999996
    - type: map_at_3
      value: 58.738
    - type: map_at_5
      value: 60.924
    - type: mrr_at_1
      value: 77.88000000000001
    - type: mrr_at_10
      value: 83.7
    - type: mrr_at_100
      value: 83.882
    - type: mrr_at_1000
      value: 83.889
    - type: mrr_at_3
      value: 82.748
    - type: mrr_at_5
      value: 83.381
    - type: ndcg_at_1
      value: 77.88000000000001
    - type: ndcg_at_10
      value: 70.462
    - type: ndcg_at_100
      value: 73.564
    - type: ndcg_at_1000
      value: 74.78099999999999
    - type: ndcg_at_3
      value: 65.524
    - type: ndcg_at_5
      value: 68.282
    - type: precision_at_1
      value: 77.88000000000001
    - type: precision_at_10
      value: 14.81
    - type: precision_at_100
      value: 1.7229999999999999
    - type: precision_at_1000
      value: 0.188
    - type: precision_at_3
      value: 42.083999999999996
    - type: precision_at_5
      value: 27.43
    - type: recall_at_1
      value: 38.940000000000005
    - type: recall_at_10
      value: 74.051
    - type: recall_at_100
      value: 86.158
    - type: recall_at_1000
      value: 94.146
    - type: recall_at_3
      value: 63.126000000000005
    - type: recall_at_5
      value: 68.575
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
      value: 91.23440000000001
    - type: ap
      value: 87.33490392265892
    - type: f1
      value: 91.21374626021836
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
      value: 22.137999999999998
    - type: map_at_10
      value: 34.471000000000004
    - type: map_at_100
      value: 35.634
    - type: map_at_1000
      value: 35.685
    - type: map_at_3
      value: 30.587999999999997
    - type: map_at_5
      value: 32.812999999999995
    - type: mrr_at_1
      value: 22.736
    - type: mrr_at_10
      value: 35.092
    - type: mrr_at_100
      value: 36.193999999999996
    - type: mrr_at_1000
      value: 36.238
    - type: mrr_at_3
      value: 31.28
    - type: mrr_at_5
      value: 33.498
    - type: ndcg_at_1
      value: 22.736
    - type: ndcg_at_10
      value: 41.388999999999996
    - type: ndcg_at_100
      value: 46.967999999999996
    - type: ndcg_at_1000
      value: 48.178
    - type: ndcg_at_3
      value: 33.503
    - type: ndcg_at_5
      value: 37.484
    - type: precision_at_1
      value: 22.736
    - type: precision_at_10
      value: 6.54
    - type: precision_at_100
      value: 0.9339999999999999
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 14.249999999999998
    - type: precision_at_5
      value: 10.562000000000001
    - type: recall_at_1
      value: 22.137999999999998
    - type: recall_at_10
      value: 62.629999999999995
    - type: recall_at_100
      value: 88.375
    - type: recall_at_1000
      value: 97.529
    - type: recall_at_3
      value: 41.245
    - type: recall_at_5
      value: 50.808
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
      value: 95.25079799361606
    - type: f1
      value: 95.00726023695032
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
      value: 78.23757409940721
    - type: f1
      value: 58.534958803195714
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
      value: 76.20040349697378
    - type: f1
      value: 74.31261149784696
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
      value: 79.35104236718227
    - type: f1
      value: 79.7373049864316
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
      value: 34.478828180753126
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
      value: 32.25696147904426
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
      value: 32.82488548405117
    - type: mrr
      value: 34.066706809031096
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
      value: 6.557
    - type: map_at_10
      value: 15.055
    - type: map_at_100
      value: 19.575
    - type: map_at_1000
      value: 21.267
    - type: map_at_3
      value: 10.86
    - type: map_at_5
      value: 12.83
    - type: mrr_at_1
      value: 50.464
    - type: mrr_at_10
      value: 59.050999999999995
    - type: mrr_at_100
      value: 59.436
    - type: mrr_at_1000
      value: 59.476
    - type: mrr_at_3
      value: 56.811
    - type: mrr_at_5
      value: 58.08
    - type: ndcg_at_1
      value: 47.988
    - type: ndcg_at_10
      value: 38.645
    - type: ndcg_at_100
      value: 36.339
    - type: ndcg_at_1000
      value: 45.279
    - type: ndcg_at_3
      value: 43.35
    - type: ndcg_at_5
      value: 41.564
    - type: precision_at_1
      value: 49.845
    - type: precision_at_10
      value: 28.544999999999998
    - type: precision_at_100
      value: 9.322
    - type: precision_at_1000
      value: 2.258
    - type: precision_at_3
      value: 40.144000000000005
    - type: precision_at_5
      value: 35.913000000000004
    - type: recall_at_1
      value: 6.557
    - type: recall_at_10
      value: 19.5
    - type: recall_at_100
      value: 37.153999999999996
    - type: recall_at_1000
      value: 69.581
    - type: recall_at_3
      value: 12.133
    - type: recall_at_5
      value: 15.43
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
      value: 31.740000000000002
    - type: map_at_10
      value: 48.150999999999996
    - type: map_at_100
      value: 49.125
    - type: map_at_1000
      value: 49.149
    - type: map_at_3
      value: 43.645
    - type: map_at_5
      value: 46.417
    - type: mrr_at_1
      value: 35.892
    - type: mrr_at_10
      value: 50.524
    - type: mrr_at_100
      value: 51.232
    - type: mrr_at_1000
      value: 51.24999999999999
    - type: mrr_at_3
      value: 46.852
    - type: mrr_at_5
      value: 49.146
    - type: ndcg_at_1
      value: 35.892
    - type: ndcg_at_10
      value: 56.08800000000001
    - type: ndcg_at_100
      value: 60.077000000000005
    - type: ndcg_at_1000
      value: 60.632
    - type: ndcg_at_3
      value: 47.765
    - type: ndcg_at_5
      value: 52.322
    - type: precision_at_1
      value: 35.892
    - type: precision_at_10
      value: 9.296
    - type: precision_at_100
      value: 1.154
    - type: precision_at_1000
      value: 0.12
    - type: precision_at_3
      value: 21.92
    - type: precision_at_5
      value: 15.781999999999998
    - type: recall_at_1
      value: 31.740000000000002
    - type: recall_at_10
      value: 77.725
    - type: recall_at_100
      value: 94.841
    - type: recall_at_1000
      value: 99.003
    - type: recall_at_3
      value: 56.407
    - type: recall_at_5
      value: 66.848
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
      value: 71.429
    - type: map_at_10
      value: 85.42699999999999
    - type: map_at_100
      value: 86.063
    - type: map_at_1000
      value: 86.077
    - type: map_at_3
      value: 82.573
    - type: map_at_5
      value: 84.371
    - type: mrr_at_1
      value: 82.34
    - type: mrr_at_10
      value: 88.247
    - type: mrr_at_100
      value: 88.357
    - type: mrr_at_1000
      value: 88.357
    - type: mrr_at_3
      value: 87.38
    - type: mrr_at_5
      value: 87.981
    - type: ndcg_at_1
      value: 82.34
    - type: ndcg_at_10
      value: 88.979
    - type: ndcg_at_100
      value: 90.18599999999999
    - type: ndcg_at_1000
      value: 90.254
    - type: ndcg_at_3
      value: 86.378
    - type: ndcg_at_5
      value: 87.821
    - type: precision_at_1
      value: 82.34
    - type: precision_at_10
      value: 13.482
    - type: precision_at_100
      value: 1.537
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 37.852999999999994
    - type: precision_at_5
      value: 24.798000000000002
    - type: recall_at_1
      value: 71.429
    - type: recall_at_10
      value: 95.64099999999999
    - type: recall_at_100
      value: 99.723
    - type: recall_at_1000
      value: 99.98
    - type: recall_at_3
      value: 88.011
    - type: recall_at_5
      value: 92.246
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
      value: 60.62148584103299
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
      value: 63.2923987272903
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
      value: 5.128
    - type: map_at_10
      value: 14.63
    - type: map_at_100
      value: 17.285
    - type: map_at_1000
      value: 17.676
    - type: map_at_3
      value: 9.993
    - type: map_at_5
      value: 12.286999999999999
    - type: mrr_at_1
      value: 25.4
    - type: mrr_at_10
      value: 38.423
    - type: mrr_at_100
      value: 39.497
    - type: mrr_at_1000
      value: 39.531
    - type: mrr_at_3
      value: 34.9
    - type: mrr_at_5
      value: 37.01
    - type: ndcg_at_1
      value: 25.4
    - type: ndcg_at_10
      value: 24.062
    - type: ndcg_at_100
      value: 33.823
    - type: ndcg_at_1000
      value: 39.663
    - type: ndcg_at_3
      value: 22.246
    - type: ndcg_at_5
      value: 19.761
    - type: precision_at_1
      value: 25.4
    - type: precision_at_10
      value: 12.85
    - type: precision_at_100
      value: 2.71
    - type: precision_at_1000
      value: 0.41000000000000003
    - type: precision_at_3
      value: 21.4
    - type: precision_at_5
      value: 17.86
    - type: recall_at_1
      value: 5.128
    - type: recall_at_10
      value: 26.06
    - type: recall_at_100
      value: 54.993
    - type: recall_at_1000
      value: 83.165
    - type: recall_at_3
      value: 13.003
    - type: recall_at_5
      value: 18.117
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
      value: 87.5466779326323
    - type: cos_sim_spearman
      value: 82.79782085421951
    - type: euclidean_pearson
      value: 84.76929982677339
    - type: euclidean_spearman
      value: 82.51802536005597
    - type: manhattan_pearson
      value: 84.76736312526177
    - type: manhattan_spearman
      value: 82.50799656335593
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
      value: 86.40486308108694
    - type: cos_sim_spearman
      value: 77.12670500926937
    - type: euclidean_pearson
      value: 85.23836845503847
    - type: euclidean_spearman
      value: 78.41475117006176
    - type: manhattan_pearson
      value: 85.24302039610805
    - type: manhattan_spearman
      value: 78.4053162562707
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
      value: 88.83570289087565
    - type: cos_sim_spearman
      value: 89.28563503553643
    - type: euclidean_pearson
      value: 87.77516003996445
    - type: euclidean_spearman
      value: 88.8656149534085
    - type: manhattan_pearson
      value: 87.75568872417946
    - type: manhattan_spearman
      value: 88.80445489340585
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
      value: 86.776406555485
    - type: cos_sim_spearman
      value: 83.8288465070091
    - type: euclidean_pearson
      value: 85.37827999808123
    - type: euclidean_spearman
      value: 84.11079529992739
    - type: manhattan_pearson
      value: 85.35336495689121
    - type: manhattan_spearman
      value: 84.08618492649347
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
      value: 88.57644404820684
    - type: cos_sim_spearman
      value: 89.69728364350713
    - type: euclidean_pearson
      value: 88.28202320389443
    - type: euclidean_spearman
      value: 88.9560567319321
    - type: manhattan_pearson
      value: 88.29461100044172
    - type: manhattan_spearman
      value: 88.96030920678558
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
      value: 85.05211938460621
    - type: cos_sim_spearman
      value: 86.43413865667489
    - type: euclidean_pearson
      value: 85.62760689259562
    - type: euclidean_spearman
      value: 86.28867831982394
    - type: manhattan_pearson
      value: 85.60828879163458
    - type: manhattan_spearman
      value: 86.27823731462473
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
      value: 90.00254140466377
    - type: cos_sim_spearman
      value: 89.66118745178284
    - type: euclidean_pearson
      value: 89.46985446236553
    - type: euclidean_spearman
      value: 88.92649032371526
    - type: manhattan_pearson
      value: 89.49600028180247
    - type: manhattan_spearman
      value: 88.86948431519099
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
      value: 68.93578321067938
    - type: cos_sim_spearman
      value: 69.60639595839257
    - type: euclidean_pearson
      value: 70.33485090574897
    - type: euclidean_spearman
      value: 69.03380379185452
    - type: manhattan_pearson
      value: 70.42097254943839
    - type: manhattan_spearman
      value: 69.25296348304255
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
      value: 87.29588700755069
    - type: cos_sim_spearman
      value: 88.30389489193672
    - type: euclidean_pearson
      value: 87.60349838180346
    - type: euclidean_spearman
      value: 87.91041868311692
    - type: manhattan_pearson
      value: 87.59373630607907
    - type: manhattan_spearman
      value: 87.88690174001724
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
      value: 87.8030655700857
    - type: mrr
      value: 96.3950637234951
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
      value: 60.028000000000006
    - type: map_at_10
      value: 69.855
    - type: map_at_100
      value: 70.257
    - type: map_at_1000
      value: 70.283
    - type: map_at_3
      value: 66.769
    - type: map_at_5
      value: 68.679
    - type: mrr_at_1
      value: 62.666999999999994
    - type: mrr_at_10
      value: 70.717
    - type: mrr_at_100
      value: 71.00800000000001
    - type: mrr_at_1000
      value: 71.033
    - type: mrr_at_3
      value: 68.389
    - type: mrr_at_5
      value: 69.939
    - type: ndcg_at_1
      value: 62.666999999999994
    - type: ndcg_at_10
      value: 74.715
    - type: ndcg_at_100
      value: 76.364
    - type: ndcg_at_1000
      value: 76.89399999999999
    - type: ndcg_at_3
      value: 69.383
    - type: ndcg_at_5
      value: 72.322
    - type: precision_at_1
      value: 62.666999999999994
    - type: precision_at_10
      value: 10.067
    - type: precision_at_100
      value: 1.09
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 27.111
    - type: precision_at_5
      value: 18.267
    - type: recall_at_1
      value: 60.028000000000006
    - type: recall_at_10
      value: 88.822
    - type: recall_at_100
      value: 96.167
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 74.367
    - type: recall_at_5
      value: 81.661
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
      value: 96.54482863244152
    - type: cos_sim_f1
      value: 92.13709677419355
    - type: cos_sim_precision
      value: 92.88617886178862
    - type: cos_sim_recall
      value: 91.4
    - type: dot_accuracy
      value: 99.76039603960396
    - type: dot_ap
      value: 93.20115278887057
    - type: dot_f1
      value: 87.92079207920793
    - type: dot_precision
      value: 87.05882352941177
    - type: dot_recall
      value: 88.8
    - type: euclidean_accuracy
      value: 99.84950495049505
    - type: euclidean_ap
      value: 96.53268343961348
    - type: euclidean_f1
      value: 92.23697650663942
    - type: euclidean_precision
      value: 94.258872651357
    - type: euclidean_recall
      value: 90.3
    - type: manhattan_accuracy
      value: 99.85346534653465
    - type: manhattan_ap
      value: 96.54495433438355
    - type: manhattan_f1
      value: 92.51012145748987
    - type: manhattan_precision
      value: 93.64754098360656
    - type: manhattan_recall
      value: 91.4
    - type: max_accuracy
      value: 99.85346534653465
    - type: max_ap
      value: 96.54495433438355
    - type: max_f1
      value: 92.51012145748987
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
      value: 66.46940443952006
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
      value: 36.396194493841584
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
      value: 54.881717673695555
    - type: mrr
      value: 55.73439224174519
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
      value: 31.438177268254087
    - type: cos_sim_spearman
      value: 30.96177698848688
    - type: dot_pearson
      value: 30.513850376431435
    - type: dot_spearman
      value: 29.932421046509706
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
      value: 0.21
    - type: map_at_10
      value: 1.727
    - type: map_at_100
      value: 9.881
    - type: map_at_1000
      value: 24.245
    - type: map_at_3
      value: 0.615
    - type: map_at_5
      value: 0.966
    - type: mrr_at_1
      value: 78.0
    - type: mrr_at_10
      value: 87.333
    - type: mrr_at_100
      value: 87.333
    - type: mrr_at_1000
      value: 87.333
    - type: mrr_at_3
      value: 86.333
    - type: mrr_at_5
      value: 87.333
    - type: ndcg_at_1
      value: 74.0
    - type: ndcg_at_10
      value: 69.12700000000001
    - type: ndcg_at_100
      value: 53.893
    - type: ndcg_at_1000
      value: 49.639
    - type: ndcg_at_3
      value: 74.654
    - type: ndcg_at_5
      value: 73.232
    - type: precision_at_1
      value: 78.0
    - type: precision_at_10
      value: 72.8
    - type: precision_at_100
      value: 55.42
    - type: precision_at_1000
      value: 21.73
    - type: precision_at_3
      value: 79.333
    - type: precision_at_5
      value: 77.2
    - type: recall_at_1
      value: 0.21
    - type: recall_at_10
      value: 1.9709999999999999
    - type: recall_at_100
      value: 13.555
    - type: recall_at_1000
      value: 46.961999999999996
    - type: recall_at_3
      value: 0.66
    - type: recall_at_5
      value: 1.052
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
      value: 2.456
    - type: map_at_10
      value: 9.426
    - type: map_at_100
      value: 16.066
    - type: map_at_1000
      value: 17.652
    - type: map_at_3
      value: 5.2459999999999996
    - type: map_at_5
      value: 6.5360000000000005
    - type: mrr_at_1
      value: 34.694
    - type: mrr_at_10
      value: 47.666
    - type: mrr_at_100
      value: 48.681999999999995
    - type: mrr_at_1000
      value: 48.681999999999995
    - type: mrr_at_3
      value: 43.878
    - type: mrr_at_5
      value: 46.224
    - type: ndcg_at_1
      value: 31.633
    - type: ndcg_at_10
      value: 23.454
    - type: ndcg_at_100
      value: 36.616
    - type: ndcg_at_1000
      value: 48.596000000000004
    - type: ndcg_at_3
      value: 28.267999999999997
    - type: ndcg_at_5
      value: 25.630999999999997
    - type: precision_at_1
      value: 34.694
    - type: precision_at_10
      value: 20.204
    - type: precision_at_100
      value: 7.754999999999999
    - type: precision_at_1000
      value: 1.5709999999999997
    - type: precision_at_3
      value: 29.252
    - type: precision_at_5
      value: 24.898
    - type: recall_at_1
      value: 2.456
    - type: recall_at_10
      value: 14.951
    - type: recall_at_100
      value: 48.399
    - type: recall_at_1000
      value: 85.077
    - type: recall_at_3
      value: 6.1370000000000005
    - type: recall_at_5
      value: 8.671
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
      value: 71.86240000000001
    - type: ap
      value: 14.678570078747494
    - type: f1
      value: 55.295967793934445
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
      value: 59.17374080362195
    - type: f1
      value: 59.54410874861454
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
      value: 51.91227822485289
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
      value: 87.12523097097217
    - type: cos_sim_ap
      value: 77.59606075943269
    - type: cos_sim_f1
      value: 71.11395646606915
    - type: cos_sim_precision
      value: 69.07960199004975
    - type: cos_sim_recall
      value: 73.27176781002639
    - type: dot_accuracy
      value: 84.68736961316088
    - type: dot_ap
      value: 68.47167450741459
    - type: dot_f1
      value: 64.42152354914874
    - type: dot_precision
      value: 60.887949260042284
    - type: dot_recall
      value: 68.3905013192612
    - type: euclidean_accuracy
      value: 86.88084878106932
    - type: euclidean_ap
      value: 77.27351204978599
    - type: euclidean_f1
      value: 70.99179716629381
    - type: euclidean_precision
      value: 67.10526315789474
    - type: euclidean_recall
      value: 75.35620052770449
    - type: manhattan_accuracy
      value: 86.83316445133218
    - type: manhattan_ap
      value: 77.21835357308716
    - type: manhattan_f1
      value: 71.05587004676349
    - type: manhattan_precision
      value: 66.58210332103322
    - type: manhattan_recall
      value: 76.17414248021109
    - type: max_accuracy
      value: 87.12523097097217
    - type: max_ap
      value: 77.59606075943269
    - type: max_f1
      value: 71.11395646606915
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
      value: 88.97232894787906
    - type: cos_sim_ap
      value: 85.9613736469497
    - type: cos_sim_f1
      value: 78.40216655382532
    - type: cos_sim_precision
      value: 72.97512437810946
    - type: cos_sim_recall
      value: 84.70126270403449
    - type: dot_accuracy
      value: 88.04866689952264
    - type: dot_ap
      value: 83.15465089499936
    - type: dot_f1
      value: 76.32698287879329
    - type: dot_precision
      value: 71.23223697378077
    - type: dot_recall
      value: 82.20665229442562
    - type: euclidean_accuracy
      value: 88.67543757519307
    - type: euclidean_ap
      value: 85.4524355531532
    - type: euclidean_f1
      value: 77.78729106950081
    - type: euclidean_precision
      value: 75.3009009009009
    - type: euclidean_recall
      value: 80.44348629504158
    - type: manhattan_accuracy
      value: 88.65991384328792
    - type: manhattan_ap
      value: 85.43109069046837
    - type: manhattan_f1
      value: 77.72639551396425
    - type: manhattan_precision
      value: 73.73402417962004
    - type: manhattan_recall
      value: 82.17585463504774
    - type: max_accuracy
      value: 88.97232894787906
    - type: max_ap
      value: 85.9613736469497
    - type: max_f1
      value: 78.40216655382532
---
<h1 align="center">GIST Large Embedding v0</h1>

*GISTEmbed: Guided In-sample Selection of Training Negatives for Text Embedding Fine-tuning*

The model is fine-tuned on top of the [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5) using the [MEDI dataset](https://github.com/xlang-ai/instructor-embedding.git) augmented with mined triplets from the [MTEB Classification](https://huggingface.co/mteb) training dataset (excluding data from the Amazon Polarity Classification task).

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

model = SentenceTransformer("avsolatorio/GIST-large-Embedding-v0", revision=revision)

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
Epochs = 40
Warmup ratio = 0.1
Learning rate = 5e-6
Batch size = 16
Checkpoint step = 171000
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