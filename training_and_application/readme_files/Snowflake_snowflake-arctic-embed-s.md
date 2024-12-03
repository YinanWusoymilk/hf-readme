---
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
- name: snowflake-snowflake-arctic-embed-s
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
      value: 71.17910447761193
    - type: ap
      value: 33.15833652904991
    - type: f1
      value: 64.86214791591543
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
      value: 78.750325
    - type: ap
      value: 72.83242788470943
    - type: f1
      value: 78.63968044029453
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
      value: 38.264
    - type: f1
      value: 37.140269688532825
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
      value: 32.646
    - type: map_at_10
      value: 48.372
    - type: map_at_100
      value: 49.207
    - type: map_at_1000
      value: 49.214
    - type: map_at_3
      value: 43.611
    - type: map_at_5
      value: 46.601
    - type: mrr_at_1
      value: 33.144
    - type: mrr_at_10
      value: 48.557
    - type: mrr_at_100
      value: 49.385
    - type: mrr_at_1000
      value: 49.392
    - type: mrr_at_3
      value: 43.777
    - type: mrr_at_5
      value: 46.792
    - type: ndcg_at_1
      value: 32.646
    - type: ndcg_at_10
      value: 56.874
    - type: ndcg_at_100
      value: 60.307
    - type: ndcg_at_1000
      value: 60.465999999999994
    - type: ndcg_at_3
      value: 47.339999999999996
    - type: ndcg_at_5
      value: 52.685
    - type: precision_at_1
      value: 32.646
    - type: precision_at_10
      value: 8.378
    - type: precision_at_100
      value: 0.984
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 19.393
    - type: precision_at_5
      value: 14.210999999999999
    - type: recall_at_1
      value: 32.646
    - type: recall_at_10
      value: 83.784
    - type: recall_at_100
      value: 98.43499999999999
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 58.179
    - type: recall_at_5
      value: 71.053
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
      value: 44.94353025039141
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
      value: 35.870836103029156
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
      value: 61.149290266979236
    - type: mrr
      value: 73.8448093919008
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
      value: 87.055571064151
    - type: cos_sim_spearman
      value: 86.2652186235749
    - type: euclidean_pearson
      value: 85.82039272282503
    - type: euclidean_spearman
      value: 86.2652186235749
    - type: manhattan_pearson
      value: 85.95825392094812
    - type: manhattan_spearman
      value: 86.6742640885316
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
      value: 79.11688311688312
    - type: f1
      value: 78.28328901613885
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
      value: 19.147523589859325
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
      value: 35.68369864124274
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
      value: 30.474958792950872
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
      value: 33.183
    - type: map_at_10
      value: 43.989
    - type: map_at_100
      value: 45.389
    - type: map_at_1000
      value: 45.517
    - type: map_at_3
      value: 40.275
    - type: map_at_5
      value: 42.306
    - type: mrr_at_1
      value: 40.486
    - type: mrr_at_10
      value: 49.62
    - type: mrr_at_100
      value: 50.351
    - type: mrr_at_1000
      value: 50.393
    - type: mrr_at_3
      value: 46.805
    - type: mrr_at_5
      value: 48.429
    - type: ndcg_at_1
      value: 40.486
    - type: ndcg_at_10
      value: 50.249
    - type: ndcg_at_100
      value: 55.206
    - type: ndcg_at_1000
      value: 57.145
    - type: ndcg_at_3
      value: 44.852
    - type: ndcg_at_5
      value: 47.355000000000004
    - type: precision_at_1
      value: 40.486
    - type: precision_at_10
      value: 9.571
    - type: precision_at_100
      value: 1.4949999999999999
    - type: precision_at_1000
      value: 0.196
    - type: precision_at_3
      value: 21.173000000000002
    - type: precision_at_5
      value: 15.622
    - type: recall_at_1
      value: 33.183
    - type: recall_at_10
      value: 62.134
    - type: recall_at_100
      value: 82.73
    - type: recall_at_1000
      value: 94.93599999999999
    - type: recall_at_3
      value: 46.497
    - type: recall_at_5
      value: 53.199
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
      value: 32.862
    - type: map_at_10
      value: 42.439
    - type: map_at_100
      value: 43.736999999999995
    - type: map_at_1000
      value: 43.864
    - type: map_at_3
      value: 39.67
    - type: map_at_5
      value: 41.202
    - type: mrr_at_1
      value: 40.892
    - type: mrr_at_10
      value: 48.61
    - type: mrr_at_100
      value: 49.29
    - type: mrr_at_1000
      value: 49.332
    - type: mrr_at_3
      value: 46.688
    - type: mrr_at_5
      value: 47.803000000000004
    - type: ndcg_at_1
      value: 40.892
    - type: ndcg_at_10
      value: 47.797
    - type: ndcg_at_100
      value: 52.17699999999999
    - type: ndcg_at_1000
      value: 54.127
    - type: ndcg_at_3
      value: 44.189
    - type: ndcg_at_5
      value: 45.821
    - type: precision_at_1
      value: 40.892
    - type: precision_at_10
      value: 8.841000000000001
    - type: precision_at_100
      value: 1.419
    - type: precision_at_1000
      value: 0.188
    - type: precision_at_3
      value: 21.104
    - type: precision_at_5
      value: 14.777000000000001
    - type: recall_at_1
      value: 32.862
    - type: recall_at_10
      value: 56.352999999999994
    - type: recall_at_100
      value: 74.795
    - type: recall_at_1000
      value: 86.957
    - type: recall_at_3
      value: 45.269999999999996
    - type: recall_at_5
      value: 50.053000000000004
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
      value: 42.998999999999995
    - type: map_at_10
      value: 54.745
    - type: map_at_100
      value: 55.650999999999996
    - type: map_at_1000
      value: 55.703
    - type: map_at_3
      value: 51.67
    - type: map_at_5
      value: 53.503
    - type: mrr_at_1
      value: 49.028
    - type: mrr_at_10
      value: 58.172000000000004
    - type: mrr_at_100
      value: 58.744
    - type: mrr_at_1000
      value: 58.769000000000005
    - type: mrr_at_3
      value: 55.977
    - type: mrr_at_5
      value: 57.38799999999999
    - type: ndcg_at_1
      value: 49.028
    - type: ndcg_at_10
      value: 60.161
    - type: ndcg_at_100
      value: 63.806
    - type: ndcg_at_1000
      value: 64.821
    - type: ndcg_at_3
      value: 55.199
    - type: ndcg_at_5
      value: 57.830999999999996
    - type: precision_at_1
      value: 49.028
    - type: precision_at_10
      value: 9.455
    - type: precision_at_100
      value: 1.216
    - type: precision_at_1000
      value: 0.135
    - type: precision_at_3
      value: 24.242
    - type: precision_at_5
      value: 16.614
    - type: recall_at_1
      value: 42.998999999999995
    - type: recall_at_10
      value: 72.542
    - type: recall_at_100
      value: 88.605
    - type: recall_at_1000
      value: 95.676
    - type: recall_at_3
      value: 59.480999999999995
    - type: recall_at_5
      value: 65.886
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
      value: 27.907
    - type: map_at_10
      value: 35.975
    - type: map_at_100
      value: 36.985
    - type: map_at_1000
      value: 37.063
    - type: map_at_3
      value: 33.467999999999996
    - type: map_at_5
      value: 34.749
    - type: mrr_at_1
      value: 30.056
    - type: mrr_at_10
      value: 38.047
    - type: mrr_at_100
      value: 38.932
    - type: mrr_at_1000
      value: 38.991
    - type: mrr_at_3
      value: 35.705999999999996
    - type: mrr_at_5
      value: 36.966
    - type: ndcg_at_1
      value: 30.056
    - type: ndcg_at_10
      value: 40.631
    - type: ndcg_at_100
      value: 45.564
    - type: ndcg_at_1000
      value: 47.685
    - type: ndcg_at_3
      value: 35.748000000000005
    - type: ndcg_at_5
      value: 37.921
    - type: precision_at_1
      value: 30.056
    - type: precision_at_10
      value: 6.079
    - type: precision_at_100
      value: 0.898
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 14.727
    - type: precision_at_5
      value: 10.056
    - type: recall_at_1
      value: 27.907
    - type: recall_at_10
      value: 52.981
    - type: recall_at_100
      value: 75.53999999999999
    - type: recall_at_1000
      value: 91.759
    - type: recall_at_3
      value: 39.878
    - type: recall_at_5
      value: 45.077
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
      value: 16.764000000000003
    - type: map_at_10
      value: 24.294
    - type: map_at_100
      value: 25.507999999999996
    - type: map_at_1000
      value: 25.64
    - type: map_at_3
      value: 21.807000000000002
    - type: map_at_5
      value: 23.21
    - type: mrr_at_1
      value: 20.771
    - type: mrr_at_10
      value: 28.677000000000003
    - type: mrr_at_100
      value: 29.742
    - type: mrr_at_1000
      value: 29.816
    - type: mrr_at_3
      value: 26.327
    - type: mrr_at_5
      value: 27.639000000000003
    - type: ndcg_at_1
      value: 20.771
    - type: ndcg_at_10
      value: 29.21
    - type: ndcg_at_100
      value: 34.788000000000004
    - type: ndcg_at_1000
      value: 37.813
    - type: ndcg_at_3
      value: 24.632
    - type: ndcg_at_5
      value: 26.801000000000002
    - type: precision_at_1
      value: 20.771
    - type: precision_at_10
      value: 5.373
    - type: precision_at_100
      value: 0.923
    - type: precision_at_1000
      value: 0.133
    - type: precision_at_3
      value: 12.065
    - type: precision_at_5
      value: 8.706
    - type: recall_at_1
      value: 16.764000000000003
    - type: recall_at_10
      value: 40.072
    - type: recall_at_100
      value: 63.856
    - type: recall_at_1000
      value: 85.141
    - type: recall_at_3
      value: 27.308
    - type: recall_at_5
      value: 32.876
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
      value: 31.194
    - type: map_at_10
      value: 40.731
    - type: map_at_100
      value: 42.073
    - type: map_at_1000
      value: 42.178
    - type: map_at_3
      value: 37.726
    - type: map_at_5
      value: 39.474
    - type: mrr_at_1
      value: 37.729
    - type: mrr_at_10
      value: 46.494
    - type: mrr_at_100
      value: 47.368
    - type: mrr_at_1000
      value: 47.407
    - type: mrr_at_3
      value: 44.224999999999994
    - type: mrr_at_5
      value: 45.582
    - type: ndcg_at_1
      value: 37.729
    - type: ndcg_at_10
      value: 46.312999999999995
    - type: ndcg_at_100
      value: 51.915
    - type: ndcg_at_1000
      value: 53.788000000000004
    - type: ndcg_at_3
      value: 41.695
    - type: ndcg_at_5
      value: 43.956
    - type: precision_at_1
      value: 37.729
    - type: precision_at_10
      value: 8.181
    - type: precision_at_100
      value: 1.275
    - type: precision_at_1000
      value: 0.16199999999999998
    - type: precision_at_3
      value: 19.41
    - type: precision_at_5
      value: 13.648
    - type: recall_at_1
      value: 31.194
    - type: recall_at_10
      value: 57.118
    - type: recall_at_100
      value: 80.759
    - type: recall_at_1000
      value: 92.779
    - type: recall_at_3
      value: 44.083
    - type: recall_at_5
      value: 50.044999999999995
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
      value: 28.047
    - type: map_at_10
      value: 37.79
    - type: map_at_100
      value: 39.145
    - type: map_at_1000
      value: 39.254
    - type: map_at_3
      value: 34.857
    - type: map_at_5
      value: 36.545
    - type: mrr_at_1
      value: 35.388
    - type: mrr_at_10
      value: 43.475
    - type: mrr_at_100
      value: 44.440000000000005
    - type: mrr_at_1000
      value: 44.494
    - type: mrr_at_3
      value: 41.286
    - type: mrr_at_5
      value: 42.673
    - type: ndcg_at_1
      value: 35.388
    - type: ndcg_at_10
      value: 43.169000000000004
    - type: ndcg_at_100
      value: 48.785000000000004
    - type: ndcg_at_1000
      value: 51.029
    - type: ndcg_at_3
      value: 38.801
    - type: ndcg_at_5
      value: 40.9
    - type: precision_at_1
      value: 35.388
    - type: precision_at_10
      value: 7.7509999999999994
    - type: precision_at_100
      value: 1.212
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 18.455
    - type: precision_at_5
      value: 13.014000000000001
    - type: recall_at_1
      value: 28.047
    - type: recall_at_10
      value: 53.53099999999999
    - type: recall_at_100
      value: 77.285
    - type: recall_at_1000
      value: 92.575
    - type: recall_at_3
      value: 40.949000000000005
    - type: recall_at_5
      value: 46.742
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
      value: 28.131999999999994
    - type: map_at_10
      value: 36.93333333333334
    - type: map_at_100
      value: 38.117250000000006
    - type: map_at_1000
      value: 38.23275
    - type: map_at_3
      value: 34.19708333333333
    - type: map_at_5
      value: 35.725166666666674
    - type: mrr_at_1
      value: 33.16116666666667
    - type: mrr_at_10
      value: 41.057833333333335
    - type: mrr_at_100
      value: 41.90033333333333
    - type: mrr_at_1000
      value: 41.95625
    - type: mrr_at_3
      value: 38.757333333333335
    - type: mrr_at_5
      value: 40.097333333333324
    - type: ndcg_at_1
      value: 33.16116666666667
    - type: ndcg_at_10
      value: 42.01983333333333
    - type: ndcg_at_100
      value: 46.99916666666667
    - type: ndcg_at_1000
      value: 49.21783333333334
    - type: ndcg_at_3
      value: 37.479916666666654
    - type: ndcg_at_5
      value: 39.6355
    - type: precision_at_1
      value: 33.16116666666667
    - type: precision_at_10
      value: 7.230249999999999
    - type: precision_at_100
      value: 1.1411666666666667
    - type: precision_at_1000
      value: 0.1520833333333333
    - type: precision_at_3
      value: 17.028166666666667
    - type: precision_at_5
      value: 12.046999999999999
    - type: recall_at_1
      value: 28.131999999999994
    - type: recall_at_10
      value: 52.825500000000005
    - type: recall_at_100
      value: 74.59608333333333
    - type: recall_at_1000
      value: 89.87916666666668
    - type: recall_at_3
      value: 40.13625
    - type: recall_at_5
      value: 45.699999999999996
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
      value: 24.773999999999997
    - type: map_at_10
      value: 31.997999999999998
    - type: map_at_100
      value: 32.857
    - type: map_at_1000
      value: 32.957
    - type: map_at_3
      value: 30.041
    - type: map_at_5
      value: 31.119000000000003
    - type: mrr_at_1
      value: 27.607
    - type: mrr_at_10
      value: 34.538000000000004
    - type: mrr_at_100
      value: 35.308
    - type: mrr_at_1000
      value: 35.375
    - type: mrr_at_3
      value: 32.643
    - type: mrr_at_5
      value: 33.755
    - type: ndcg_at_1
      value: 27.607
    - type: ndcg_at_10
      value: 36.035000000000004
    - type: ndcg_at_100
      value: 40.351
    - type: ndcg_at_1000
      value: 42.684
    - type: ndcg_at_3
      value: 32.414
    - type: ndcg_at_5
      value: 34.11
    - type: precision_at_1
      value: 27.607
    - type: precision_at_10
      value: 5.6129999999999995
    - type: precision_at_100
      value: 0.8370000000000001
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 13.957
    - type: precision_at_5
      value: 9.571
    - type: recall_at_1
      value: 24.773999999999997
    - type: recall_at_10
      value: 45.717
    - type: recall_at_100
      value: 65.499
    - type: recall_at_1000
      value: 82.311
    - type: recall_at_3
      value: 35.716
    - type: recall_at_5
      value: 40.007999999999996
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
      value: 19.227
    - type: map_at_10
      value: 26.649
    - type: map_at_100
      value: 27.711999999999996
    - type: map_at_1000
      value: 27.837
    - type: map_at_3
      value: 24.454
    - type: map_at_5
      value: 25.772000000000002
    - type: mrr_at_1
      value: 23.433999999999997
    - type: mrr_at_10
      value: 30.564999999999998
    - type: mrr_at_100
      value: 31.44
    - type: mrr_at_1000
      value: 31.513999999999996
    - type: mrr_at_3
      value: 28.435
    - type: mrr_at_5
      value: 29.744999999999997
    - type: ndcg_at_1
      value: 23.433999999999997
    - type: ndcg_at_10
      value: 31.104
    - type: ndcg_at_100
      value: 36.172
    - type: ndcg_at_1000
      value: 39.006
    - type: ndcg_at_3
      value: 27.248
    - type: ndcg_at_5
      value: 29.249000000000002
    - type: precision_at_1
      value: 23.433999999999997
    - type: precision_at_10
      value: 5.496
    - type: precision_at_100
      value: 0.9490000000000001
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_3
      value: 12.709000000000001
    - type: precision_at_5
      value: 9.209
    - type: recall_at_1
      value: 19.227
    - type: recall_at_10
      value: 40.492
    - type: recall_at_100
      value: 63.304
    - type: recall_at_1000
      value: 83.45
    - type: recall_at_3
      value: 29.713
    - type: recall_at_5
      value: 34.82
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
      value: 29.199
    - type: map_at_10
      value: 37.617
    - type: map_at_100
      value: 38.746
    - type: map_at_1000
      value: 38.851
    - type: map_at_3
      value: 34.882000000000005
    - type: map_at_5
      value: 36.571999999999996
    - type: mrr_at_1
      value: 33.489000000000004
    - type: mrr_at_10
      value: 41.089999999999996
    - type: mrr_at_100
      value: 41.965
    - type: mrr_at_1000
      value: 42.028
    - type: mrr_at_3
      value: 38.666
    - type: mrr_at_5
      value: 40.159
    - type: ndcg_at_1
      value: 33.489000000000004
    - type: ndcg_at_10
      value: 42.487
    - type: ndcg_at_100
      value: 47.552
    - type: ndcg_at_1000
      value: 49.774
    - type: ndcg_at_3
      value: 37.623
    - type: ndcg_at_5
      value: 40.184999999999995
    - type: precision_at_1
      value: 33.489000000000004
    - type: precision_at_10
      value: 6.94
    - type: precision_at_100
      value: 1.0699999999999998
    - type: precision_at_1000
      value: 0.136
    - type: precision_at_3
      value: 16.667
    - type: precision_at_5
      value: 11.922
    - type: recall_at_1
      value: 29.199
    - type: recall_at_10
      value: 53.689
    - type: recall_at_100
      value: 75.374
    - type: recall_at_1000
      value: 90.64999999999999
    - type: recall_at_3
      value: 40.577999999999996
    - type: recall_at_5
      value: 46.909
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
      value: 27.206999999999997
    - type: map_at_10
      value: 36.146
    - type: map_at_100
      value: 37.759
    - type: map_at_1000
      value: 37.979
    - type: map_at_3
      value: 32.967999999999996
    - type: map_at_5
      value: 34.809
    - type: mrr_at_1
      value: 32.806000000000004
    - type: mrr_at_10
      value: 40.449
    - type: mrr_at_100
      value: 41.404999999999994
    - type: mrr_at_1000
      value: 41.457
    - type: mrr_at_3
      value: 37.614999999999995
    - type: mrr_at_5
      value: 39.324999999999996
    - type: ndcg_at_1
      value: 32.806000000000004
    - type: ndcg_at_10
      value: 41.911
    - type: ndcg_at_100
      value: 47.576
    - type: ndcg_at_1000
      value: 50.072
    - type: ndcg_at_3
      value: 36.849
    - type: ndcg_at_5
      value: 39.475
    - type: precision_at_1
      value: 32.806000000000004
    - type: precision_at_10
      value: 8.103
    - type: precision_at_100
      value: 1.557
    - type: precision_at_1000
      value: 0.242
    - type: precision_at_3
      value: 17.26
    - type: precision_at_5
      value: 12.885
    - type: recall_at_1
      value: 27.206999999999997
    - type: recall_at_10
      value: 52.56999999999999
    - type: recall_at_100
      value: 78.302
    - type: recall_at_1000
      value: 94.121
    - type: recall_at_3
      value: 38.317
    - type: recall_at_5
      value: 45.410000000000004
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
      value: 24.221
    - type: map_at_10
      value: 30.826999999999998
    - type: map_at_100
      value: 31.845000000000002
    - type: map_at_1000
      value: 31.95
    - type: map_at_3
      value: 28.547
    - type: map_at_5
      value: 29.441
    - type: mrr_at_1
      value: 26.247999999999998
    - type: mrr_at_10
      value: 32.957
    - type: mrr_at_100
      value: 33.819
    - type: mrr_at_1000
      value: 33.899
    - type: mrr_at_3
      value: 30.714999999999996
    - type: mrr_at_5
      value: 31.704
    - type: ndcg_at_1
      value: 26.247999999999998
    - type: ndcg_at_10
      value: 35.171
    - type: ndcg_at_100
      value: 40.098
    - type: ndcg_at_1000
      value: 42.67
    - type: ndcg_at_3
      value: 30.508999999999997
    - type: ndcg_at_5
      value: 32.022
    - type: precision_at_1
      value: 26.247999999999998
    - type: precision_at_10
      value: 5.36
    - type: precision_at_100
      value: 0.843
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 12.568999999999999
    - type: precision_at_5
      value: 8.540000000000001
    - type: recall_at_1
      value: 24.221
    - type: recall_at_10
      value: 46.707
    - type: recall_at_100
      value: 69.104
    - type: recall_at_1000
      value: 88.19500000000001
    - type: recall_at_3
      value: 33.845
    - type: recall_at_5
      value: 37.375
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
      value: 13.624
    - type: map_at_10
      value: 22.557
    - type: map_at_100
      value: 24.367
    - type: map_at_1000
      value: 24.54
    - type: map_at_3
      value: 18.988
    - type: map_at_5
      value: 20.785999999999998
    - type: mrr_at_1
      value: 30.619000000000003
    - type: mrr_at_10
      value: 42.019
    - type: mrr_at_100
      value: 42.818
    - type: mrr_at_1000
      value: 42.856
    - type: mrr_at_3
      value: 38.578
    - type: mrr_at_5
      value: 40.669
    - type: ndcg_at_1
      value: 30.619000000000003
    - type: ndcg_at_10
      value: 31.252999999999997
    - type: ndcg_at_100
      value: 38.238
    - type: ndcg_at_1000
      value: 41.368
    - type: ndcg_at_3
      value: 25.843
    - type: ndcg_at_5
      value: 27.638
    - type: precision_at_1
      value: 30.619000000000003
    - type: precision_at_10
      value: 9.687
    - type: precision_at_100
      value: 1.718
    - type: precision_at_1000
      value: 0.22999999999999998
    - type: precision_at_3
      value: 18.849
    - type: precision_at_5
      value: 14.463000000000001
    - type: recall_at_1
      value: 13.624
    - type: recall_at_10
      value: 36.693999999999996
    - type: recall_at_100
      value: 60.9
    - type: recall_at_1000
      value: 78.46
    - type: recall_at_3
      value: 23.354
    - type: recall_at_5
      value: 28.756999999999998
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
      value: 9.077
    - type: map_at_10
      value: 19.813
    - type: map_at_100
      value: 27.822999999999997
    - type: map_at_1000
      value: 29.485
    - type: map_at_3
      value: 14.255999999999998
    - type: map_at_5
      value: 16.836000000000002
    - type: mrr_at_1
      value: 69.25
    - type: mrr_at_10
      value: 77.059
    - type: mrr_at_100
      value: 77.41
    - type: mrr_at_1000
      value: 77.416
    - type: mrr_at_3
      value: 75.625
    - type: mrr_at_5
      value: 76.512
    - type: ndcg_at_1
      value: 55.75
    - type: ndcg_at_10
      value: 41.587
    - type: ndcg_at_100
      value: 46.048
    - type: ndcg_at_1000
      value: 53.172
    - type: ndcg_at_3
      value: 46.203
    - type: ndcg_at_5
      value: 43.696
    - type: precision_at_1
      value: 69.25
    - type: precision_at_10
      value: 32.95
    - type: precision_at_100
      value: 10.555
    - type: precision_at_1000
      value: 2.136
    - type: precision_at_3
      value: 49.667
    - type: precision_at_5
      value: 42.5
    - type: recall_at_1
      value: 9.077
    - type: recall_at_10
      value: 25.249
    - type: recall_at_100
      value: 51.964
    - type: recall_at_1000
      value: 74.51
    - type: recall_at_3
      value: 15.584000000000001
    - type: recall_at_5
      value: 19.717000000000002
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
      value: 45.769999999999996
    - type: f1
      value: 41.64144711933962
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
      value: 67.098
    - type: map_at_10
      value: 77.69800000000001
    - type: map_at_100
      value: 77.947
    - type: map_at_1000
      value: 77.961
    - type: map_at_3
      value: 76.278
    - type: map_at_5
      value: 77.217
    - type: mrr_at_1
      value: 72.532
    - type: mrr_at_10
      value: 82.41199999999999
    - type: mrr_at_100
      value: 82.527
    - type: mrr_at_1000
      value: 82.529
    - type: mrr_at_3
      value: 81.313
    - type: mrr_at_5
      value: 82.069
    - type: ndcg_at_1
      value: 72.532
    - type: ndcg_at_10
      value: 82.488
    - type: ndcg_at_100
      value: 83.382
    - type: ndcg_at_1000
      value: 83.622
    - type: ndcg_at_3
      value: 80.101
    - type: ndcg_at_5
      value: 81.52199999999999
    - type: precision_at_1
      value: 72.532
    - type: precision_at_10
      value: 10.203
    - type: precision_at_100
      value: 1.082
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 31.308000000000003
    - type: precision_at_5
      value: 19.652
    - type: recall_at_1
      value: 67.098
    - type: recall_at_10
      value: 92.511
    - type: recall_at_100
      value: 96.06099999999999
    - type: recall_at_1000
      value: 97.548
    - type: recall_at_3
      value: 86.105
    - type: recall_at_5
      value: 89.661
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
      value: 18.681
    - type: map_at_10
      value: 31.739
    - type: map_at_100
      value: 33.503
    - type: map_at_1000
      value: 33.69
    - type: map_at_3
      value: 27.604
    - type: map_at_5
      value: 29.993
    - type: mrr_at_1
      value: 37.5
    - type: mrr_at_10
      value: 46.933
    - type: mrr_at_100
      value: 47.771
    - type: mrr_at_1000
      value: 47.805
    - type: mrr_at_3
      value: 44.239
    - type: mrr_at_5
      value: 45.766
    - type: ndcg_at_1
      value: 37.5
    - type: ndcg_at_10
      value: 39.682
    - type: ndcg_at_100
      value: 46.127
    - type: ndcg_at_1000
      value: 48.994
    - type: ndcg_at_3
      value: 35.655
    - type: ndcg_at_5
      value: 37.036
    - type: precision_at_1
      value: 37.5
    - type: precision_at_10
      value: 11.08
    - type: precision_at_100
      value: 1.765
    - type: precision_at_1000
      value: 0.22999999999999998
    - type: precision_at_3
      value: 23.919999999999998
    - type: precision_at_5
      value: 17.809
    - type: recall_at_1
      value: 18.681
    - type: recall_at_10
      value: 47.548
    - type: recall_at_100
      value: 71.407
    - type: recall_at_1000
      value: 87.805
    - type: recall_at_3
      value: 32.979
    - type: recall_at_5
      value: 39.192
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
      value: 38.257999999999996
    - type: map_at_10
      value: 57.605
    - type: map_at_100
      value: 58.50300000000001
    - type: map_at_1000
      value: 58.568
    - type: map_at_3
      value: 54.172
    - type: map_at_5
      value: 56.323
    - type: mrr_at_1
      value: 76.51599999999999
    - type: mrr_at_10
      value: 82.584
    - type: mrr_at_100
      value: 82.78
    - type: mrr_at_1000
      value: 82.787
    - type: mrr_at_3
      value: 81.501
    - type: mrr_at_5
      value: 82.185
    - type: ndcg_at_1
      value: 76.51599999999999
    - type: ndcg_at_10
      value: 66.593
    - type: ndcg_at_100
      value: 69.699
    - type: ndcg_at_1000
      value: 70.953
    - type: ndcg_at_3
      value: 61.673
    - type: ndcg_at_5
      value: 64.42
    - type: precision_at_1
      value: 76.51599999999999
    - type: precision_at_10
      value: 13.857
    - type: precision_at_100
      value: 1.628
    - type: precision_at_1000
      value: 0.179
    - type: precision_at_3
      value: 38.956
    - type: precision_at_5
      value: 25.541999999999998
    - type: recall_at_1
      value: 38.257999999999996
    - type: recall_at_10
      value: 69.284
    - type: recall_at_100
      value: 81.391
    - type: recall_at_1000
      value: 89.689
    - type: recall_at_3
      value: 58.433
    - type: recall_at_5
      value: 63.856
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
      value: 69.48679999999999
    - type: ap
      value: 63.97638838971138
    - type: f1
      value: 69.22731638841675
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
      value: 20.916999999999998
    - type: map_at_10
      value: 32.929
    - type: map_at_100
      value: 34.1
    - type: map_at_1000
      value: 34.152
    - type: map_at_3
      value: 29.065
    - type: map_at_5
      value: 31.287
    - type: mrr_at_1
      value: 21.562
    - type: mrr_at_10
      value: 33.533
    - type: mrr_at_100
      value: 34.644000000000005
    - type: mrr_at_1000
      value: 34.69
    - type: mrr_at_3
      value: 29.735
    - type: mrr_at_5
      value: 31.928
    - type: ndcg_at_1
      value: 21.562
    - type: ndcg_at_10
      value: 39.788000000000004
    - type: ndcg_at_100
      value: 45.434999999999995
    - type: ndcg_at_1000
      value: 46.75
    - type: ndcg_at_3
      value: 31.942999999999998
    - type: ndcg_at_5
      value: 35.888
    - type: precision_at_1
      value: 21.562
    - type: precision_at_10
      value: 6.348
    - type: precision_at_100
      value: 0.918
    - type: precision_at_1000
      value: 0.10300000000000001
    - type: precision_at_3
      value: 13.682
    - type: precision_at_5
      value: 10.189
    - type: recall_at_1
      value: 20.916999999999998
    - type: recall_at_10
      value: 60.926
    - type: recall_at_100
      value: 87.03800000000001
    - type: recall_at_1000
      value: 97.085
    - type: recall_at_3
      value: 39.637
    - type: recall_at_5
      value: 49.069
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
      value: 90.93935248518011
    - type: f1
      value: 90.56439321844506
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
      value: 58.62517099863203
    - type: f1
      value: 40.69925681703197
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
      value: 76.29746835443039
    - type: f1
      value: 75.31702672039506
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
      value: 43.05495067062023
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
      value: 19.625272848173843
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
      value: 64.76126429051781
    - type: f1
      value: 62.60284261265268
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
      value: 70.05043712172159
    - type: f1
      value: 69.08340521169049
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
      value: 30.78969229005989
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
      value: 27.954325178520335
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
      value: 30.601827413968596
    - type: mrr
      value: 31.515372019474196
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
      value: 5.4559999999999995
    - type: map_at_10
      value: 12.039
    - type: map_at_100
      value: 14.804999999999998
    - type: map_at_1000
      value: 16.081
    - type: map_at_3
      value: 8.996
    - type: map_at_5
      value: 10.357
    - type: mrr_at_1
      value: 45.82
    - type: mrr_at_10
      value: 53.583999999999996
    - type: mrr_at_100
      value: 54.330999999999996
    - type: mrr_at_1000
      value: 54.366
    - type: mrr_at_3
      value: 52.166999999999994
    - type: mrr_at_5
      value: 52.971999999999994
    - type: ndcg_at_1
      value: 44.427
    - type: ndcg_at_10
      value: 32.536
    - type: ndcg_at_100
      value: 29.410999999999998
    - type: ndcg_at_1000
      value: 38.012
    - type: ndcg_at_3
      value: 38.674
    - type: ndcg_at_5
      value: 36.107
    - type: precision_at_1
      value: 45.82
    - type: precision_at_10
      value: 23.591
    - type: precision_at_100
      value: 7.35
    - type: precision_at_1000
      value: 1.9769999999999999
    - type: precision_at_3
      value: 36.016999999999996
    - type: precision_at_5
      value: 30.959999999999997
    - type: recall_at_1
      value: 5.4559999999999995
    - type: recall_at_10
      value: 15.387
    - type: recall_at_100
      value: 28.754999999999995
    - type: recall_at_1000
      value: 59.787
    - type: recall_at_3
      value: 10.137
    - type: recall_at_5
      value: 12.200999999999999
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
      value: 32.609
    - type: map_at_10
      value: 48.522
    - type: map_at_100
      value: 49.468
    - type: map_at_1000
      value: 49.497
    - type: map_at_3
      value: 44.327
    - type: map_at_5
      value: 46.937
    - type: mrr_at_1
      value: 36.616
    - type: mrr_at_10
      value: 50.943000000000005
    - type: mrr_at_100
      value: 51.626000000000005
    - type: mrr_at_1000
      value: 51.647
    - type: mrr_at_3
      value: 47.532999999999994
    - type: mrr_at_5
      value: 49.714000000000006
    - type: ndcg_at_1
      value: 36.586999999999996
    - type: ndcg_at_10
      value: 56.19499999999999
    - type: ndcg_at_100
      value: 60.014
    - type: ndcg_at_1000
      value: 60.707
    - type: ndcg_at_3
      value: 48.486000000000004
    - type: ndcg_at_5
      value: 52.791999999999994
    - type: precision_at_1
      value: 36.586999999999996
    - type: precision_at_10
      value: 9.139999999999999
    - type: precision_at_100
      value: 1.129
    - type: precision_at_1000
      value: 0.11900000000000001
    - type: precision_at_3
      value: 22.171
    - type: precision_at_5
      value: 15.787999999999998
    - type: recall_at_1
      value: 32.609
    - type: recall_at_10
      value: 77.011
    - type: recall_at_100
      value: 93.202
    - type: recall_at_1000
      value: 98.344
    - type: recall_at_3
      value: 57.286
    - type: recall_at_5
      value: 67.181
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
      value: 77.4421052631579
    - type: f1
      value: 77.23976860913628
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
      value: 100
    - type: cos_sim_f1
      value: 99.9490575649516
    - type: cos_sim_precision
      value: 100
    - type: cos_sim_recall
      value: 99.89816700610999
    - type: dot_accuracy
      value: 99.89816700610999
    - type: dot_ap
      value: 100
    - type: dot_f1
      value: 99.9490575649516
    - type: dot_precision
      value: 100
    - type: dot_recall
      value: 99.89816700610999
    - type: euclidean_accuracy
      value: 99.89816700610999
    - type: euclidean_ap
      value: 100
    - type: euclidean_f1
      value: 99.9490575649516
    - type: euclidean_precision
      value: 100
    - type: euclidean_recall
      value: 99.89816700610999
    - type: manhattan_accuracy
      value: 99.89816700610999
    - type: manhattan_ap
      value: 100
    - type: manhattan_f1
      value: 99.9490575649516
    - type: manhattan_precision
      value: 100
    - type: manhattan_recall
      value: 99.89816700610999
    - type: max_accuracy
      value: 99.89816700610999
    - type: max_ap
      value: 100
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
      value: 61.25000000000001
    - type: cos_sim_ap
      value: 59.23166242799505
    - type: cos_sim_f1
      value: 62.53016201309893
    - type: cos_sim_precision
      value: 45.486459378134406
    - type: cos_sim_recall
      value: 100
    - type: dot_accuracy
      value: 61.25000000000001
    - type: dot_ap
      value: 59.23109306756652
    - type: dot_f1
      value: 62.53016201309893
    - type: dot_precision
      value: 45.486459378134406
    - type: dot_recall
      value: 100
    - type: euclidean_accuracy
      value: 61.25000000000001
    - type: euclidean_ap
      value: 59.23166242799505
    - type: euclidean_f1
      value: 62.53016201309893
    - type: euclidean_precision
      value: 45.486459378134406
    - type: euclidean_recall
      value: 100
    - type: manhattan_accuracy
      value: 61.25000000000001
    - type: manhattan_ap
      value: 59.23015114712089
    - type: manhattan_f1
      value: 62.50861474844934
    - type: manhattan_precision
      value: 45.46365914786967
    - type: manhattan_recall
      value: 100
    - type: max_accuracy
      value: 61.25000000000001
    - type: max_ap
      value: 59.23166242799505
    - type: max_f1
      value: 62.53016201309893
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
      value: 69.919
    - type: map_at_10
      value: 83.636
    - type: map_at_100
      value: 84.27
    - type: map_at_1000
      value: 84.289
    - type: map_at_3
      value: 80.744
    - type: map_at_5
      value: 82.509
    - type: mrr_at_1
      value: 80.52
    - type: mrr_at_10
      value: 86.751
    - type: mrr_at_100
      value: 86.875
    - type: mrr_at_1000
      value: 86.876
    - type: mrr_at_3
      value: 85.798
    - type: mrr_at_5
      value: 86.414
    - type: ndcg_at_1
      value: 80.53
    - type: ndcg_at_10
      value: 87.465
    - type: ndcg_at_100
      value: 88.762
    - type: ndcg_at_1000
      value: 88.90599999999999
    - type: ndcg_at_3
      value: 84.634
    - type: ndcg_at_5
      value: 86.09400000000001
    - type: precision_at_1
      value: 80.53
    - type: precision_at_10
      value: 13.263
    - type: precision_at_100
      value: 1.517
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 36.973
    - type: precision_at_5
      value: 24.25
    - type: recall_at_1
      value: 69.919
    - type: recall_at_10
      value: 94.742
    - type: recall_at_100
      value: 99.221
    - type: recall_at_1000
      value: 99.917
    - type: recall_at_3
      value: 86.506
    - type: recall_at_5
      value: 90.736
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
      value: 50.47309147963901
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
      value: 60.53779561923047
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
      value: 4.843
    - type: map_at_10
      value: 11.664
    - type: map_at_100
      value: 13.499
    - type: map_at_1000
      value: 13.771
    - type: map_at_3
      value: 8.602
    - type: map_at_5
      value: 10.164
    - type: mrr_at_1
      value: 23.9
    - type: mrr_at_10
      value: 34.018
    - type: mrr_at_100
      value: 35.099000000000004
    - type: mrr_at_1000
      value: 35.162
    - type: mrr_at_3
      value: 31.233
    - type: mrr_at_5
      value: 32.793
    - type: ndcg_at_1
      value: 23.9
    - type: ndcg_at_10
      value: 19.42
    - type: ndcg_at_100
      value: 26.715
    - type: ndcg_at_1000
      value: 31.776
    - type: ndcg_at_3
      value: 19.165
    - type: ndcg_at_5
      value: 16.46
    - type: precision_at_1
      value: 23.9
    - type: precision_at_10
      value: 9.82
    - type: precision_at_100
      value: 2.0340000000000003
    - type: precision_at_1000
      value: 0.325
    - type: precision_at_3
      value: 17.767
    - type: precision_at_5
      value: 14.24
    - type: recall_at_1
      value: 4.843
    - type: recall_at_10
      value: 19.895
    - type: recall_at_100
      value: 41.302
    - type: recall_at_1000
      value: 66.077
    - type: recall_at_3
      value: 10.803
    - type: recall_at_5
      value: 14.418000000000001
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
      value: 76.94120735638143
    - type: cos_sim_spearman
      value: 69.66114097154585
    - type: euclidean_pearson
      value: 73.11242035696426
    - type: euclidean_spearman
      value: 69.66114271982464
    - type: manhattan_pearson
      value: 73.07993034858605
    - type: manhattan_spearman
      value: 69.6457893357314
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
      value: 74.72893353272778
    - type: cos_sim_spearman
      value: 68.78540928870311
    - type: euclidean_pearson
      value: 71.13907970605574
    - type: euclidean_spearman
      value: 68.78540928870311
    - type: manhattan_pearson
      value: 71.02709590547859
    - type: manhattan_spearman
      value: 68.71685896660532
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
      value: 79.30142652684971
    - type: cos_sim_spearman
      value: 79.61879435615303
    - type: euclidean_pearson
      value: 79.08730432883864
    - type: euclidean_spearman
      value: 79.61879435615303
    - type: manhattan_pearson
      value: 78.99621073156322
    - type: manhattan_spearman
      value: 79.53806342308278
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
      value: 78.99585233036139
    - type: cos_sim_spearman
      value: 75.57574519760183
    - type: euclidean_pearson
      value: 77.33835658613162
    - type: euclidean_spearman
      value: 75.57573873503655
    - type: manhattan_pearson
      value: 77.12175044789362
    - type: manhattan_spearman
      value: 75.41293517634836
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
      value: 83.9694268253376
    - type: cos_sim_spearman
      value: 84.64256921939338
    - type: euclidean_pearson
      value: 83.92322958711
    - type: euclidean_spearman
      value: 84.64257976421872
    - type: manhattan_pearson
      value: 83.93503107204337
    - type: manhattan_spearman
      value: 84.63611608236032
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
      value: 81.09041419790253
    - type: cos_sim_spearman
      value: 82.39869157752557
    - type: euclidean_pearson
      value: 82.04595698258301
    - type: euclidean_spearman
      value: 82.39869157752557
    - type: manhattan_pearson
      value: 81.97581168053004
    - type: manhattan_spearman
      value: 82.34255320578193
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
      value: 86.35210432821825
    - type: cos_sim_spearman
      value: 86.73200885328937
    - type: euclidean_pearson
      value: 86.8527089168747
    - type: euclidean_spearman
      value: 86.73200885328937
    - type: manhattan_pearson
      value: 86.95671235295457
    - type: manhattan_spearman
      value: 86.77713700838545
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
      value: 68.91106612960657
    - type: cos_sim_spearman
      value: 69.48524490302286
    - type: euclidean_pearson
      value: 70.51347841618035
    - type: euclidean_spearman
      value: 69.48524490302286
    - type: manhattan_pearson
      value: 70.31770181334245
    - type: manhattan_spearman
      value: 69.12494700138238
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
      value: 81.54104342761988
    - type: cos_sim_spearman
      value: 81.18789220331483
    - type: euclidean_pearson
      value: 81.5895544590969
    - type: euclidean_spearman
      value: 81.18789220331483
    - type: manhattan_pearson
      value: 81.4738562449809
    - type: manhattan_spearman
      value: 81.06565101416024
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
      value: 81.54104346197056
    - type: cos_sim_spearman
      value: 81.18789220331483
    - type: euclidean_pearson
      value: 81.58955451690102
    - type: euclidean_spearman
      value: 81.18789220331483
    - type: manhattan_pearson
      value: 81.47385630064072
    - type: manhattan_spearman
      value: 81.06565101416024
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
      value: 79.34107964300796
    - type: mrr
      value: 94.01917889662987
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
      value: 55.928
    - type: map_at_10
      value: 65.443
    - type: map_at_100
      value: 66.067
    - type: map_at_1000
      value: 66.091
    - type: map_at_3
      value: 62.629999999999995
    - type: map_at_5
      value: 64.35
    - type: mrr_at_1
      value: 59
    - type: mrr_at_10
      value: 66.845
    - type: mrr_at_100
      value: 67.31899999999999
    - type: mrr_at_1000
      value: 67.342
    - type: mrr_at_3
      value: 64.61099999999999
    - type: mrr_at_5
      value: 66.044
    - type: ndcg_at_1
      value: 59
    - type: ndcg_at_10
      value: 69.921
    - type: ndcg_at_100
      value: 72.365
    - type: ndcg_at_1000
      value: 73.055
    - type: ndcg_at_3
      value: 65.086
    - type: ndcg_at_5
      value: 67.62700000000001
    - type: precision_at_1
      value: 59
    - type: precision_at_10
      value: 9.3
    - type: precision_at_100
      value: 1.057
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: precision_at_3
      value: 25.333
    - type: precision_at_5
      value: 16.866999999999997
    - type: recall_at_1
      value: 55.928
    - type: recall_at_10
      value: 82.289
    - type: recall_at_100
      value: 92.833
    - type: recall_at_1000
      value: 98.333
    - type: recall_at_3
      value: 69.172
    - type: recall_at_5
      value: 75.628
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
      value: 99.81881188118813
    - type: cos_sim_ap
      value: 95.2776439040401
    - type: cos_sim_f1
      value: 90.74355083459787
    - type: cos_sim_precision
      value: 91.81166837256909
    - type: cos_sim_recall
      value: 89.7
    - type: dot_accuracy
      value: 99.81881188118813
    - type: dot_ap
      value: 95.27764092100406
    - type: dot_f1
      value: 90.74355083459787
    - type: dot_precision
      value: 91.81166837256909
    - type: dot_recall
      value: 89.7
    - type: euclidean_accuracy
      value: 99.81881188118813
    - type: euclidean_ap
      value: 95.27764091101388
    - type: euclidean_f1
      value: 90.74355083459787
    - type: euclidean_precision
      value: 91.81166837256909
    - type: euclidean_recall
      value: 89.7
    - type: manhattan_accuracy
      value: 99.82079207920792
    - type: manhattan_ap
      value: 95.25081634689418
    - type: manhattan_f1
      value: 90.75114971895759
    - type: manhattan_precision
      value: 92.78996865203762
    - type: manhattan_recall
      value: 88.8
    - type: max_accuracy
      value: 99.82079207920792
    - type: max_ap
      value: 95.2776439040401
    - type: max_f1
      value: 90.75114971895759
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
      value: 60.69855369728728
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
      value: 33.98191834367251
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
      value: 50.156163330429614
    - type: mrr
      value: 50.90145148968678
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
      value: 31.16938079808134
    - type: cos_sim_spearman
      value: 31.74655874538245
    - type: dot_pearson
      value: 31.169380299671705
    - type: dot_spearman
      value: 31.74655874538245
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
      value: 0.252
    - type: map_at_10
      value: 2.009
    - type: map_at_100
      value: 11.611
    - type: map_at_1000
      value: 27.811999999999998
    - type: map_at_3
      value: 0.685
    - type: map_at_5
      value: 1.08
    - type: mrr_at_1
      value: 94
    - type: mrr_at_10
      value: 97
    - type: mrr_at_100
      value: 97
    - type: mrr_at_1000
      value: 97
    - type: mrr_at_3
      value: 97
    - type: mrr_at_5
      value: 97
    - type: ndcg_at_1
      value: 88
    - type: ndcg_at_10
      value: 81.388
    - type: ndcg_at_100
      value: 60.629
    - type: ndcg_at_1000
      value: 52.38
    - type: ndcg_at_3
      value: 86.827
    - type: ndcg_at_5
      value: 84.597
    - type: precision_at_1
      value: 94
    - type: precision_at_10
      value: 85.8
    - type: precision_at_100
      value: 62.419999999999995
    - type: precision_at_1000
      value: 23.31
    - type: precision_at_3
      value: 90.667
    - type: precision_at_5
      value: 88.4
    - type: recall_at_1
      value: 0.252
    - type: recall_at_10
      value: 2.164
    - type: recall_at_100
      value: 14.613999999999999
    - type: recall_at_1000
      value: 48.730000000000004
    - type: recall_at_3
      value: 0.7020000000000001
    - type: recall_at_5
      value: 1.122
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
      value: 3.476
    - type: map_at_10
      value: 13.442000000000002
    - type: map_at_100
      value: 20.618
    - type: map_at_1000
      value: 22.175
    - type: map_at_3
      value: 6.968000000000001
    - type: map_at_5
      value: 9.214
    - type: mrr_at_1
      value: 44.897999999999996
    - type: mrr_at_10
      value: 56.77100000000001
    - type: mrr_at_100
      value: 57.226
    - type: mrr_at_1000
      value: 57.226
    - type: mrr_at_3
      value: 52.381
    - type: mrr_at_5
      value: 54.523999999999994
    - type: ndcg_at_1
      value: 42.857
    - type: ndcg_at_10
      value: 32.507999999999996
    - type: ndcg_at_100
      value: 43.614000000000004
    - type: ndcg_at_1000
      value: 53.82
    - type: ndcg_at_3
      value: 36.818
    - type: ndcg_at_5
      value: 33.346
    - type: precision_at_1
      value: 44.897999999999996
    - type: precision_at_10
      value: 28.571
    - type: precision_at_100
      value: 8.652999999999999
    - type: precision_at_1000
      value: 1.5709999999999997
    - type: precision_at_3
      value: 38.095
    - type: precision_at_5
      value: 32.245000000000005
    - type: recall_at_1
      value: 3.476
    - type: recall_at_10
      value: 20.827
    - type: recall_at_100
      value: 53.04299999999999
    - type: recall_at_1000
      value: 84.221
    - type: recall_at_3
      value: 8.200000000000001
    - type: recall_at_5
      value: 11.651
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
      value: 61.96360000000001
    - type: ap
      value: 11.256160324436445
    - type: f1
      value: 48.07712827691349
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
      value: 58.90492359932088
    - type: f1
      value: 59.12542417513503
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
      value: 38.284935353315355
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
      value: 83.4714192048638
    - type: cos_sim_ap
      value: 65.77588263185375
    - type: cos_sim_f1
      value: 62.459508098380326
    - type: cos_sim_precision
      value: 57.27172717271727
    - type: cos_sim_recall
      value: 68.68073878627968
    - type: dot_accuracy
      value: 83.4714192048638
    - type: dot_ap
      value: 65.77588818364636
    - type: dot_f1
      value: 62.459508098380326
    - type: dot_precision
      value: 57.27172717271727
    - type: dot_recall
      value: 68.68073878627968
    - type: euclidean_accuracy
      value: 83.4714192048638
    - type: euclidean_ap
      value: 65.77587693431595
    - type: euclidean_f1
      value: 62.459508098380326
    - type: euclidean_precision
      value: 57.27172717271727
    - type: euclidean_recall
      value: 68.68073878627968
    - type: manhattan_accuracy
      value: 83.47737974608094
    - type: manhattan_ap
      value: 65.65957745829654
    - type: manhattan_f1
      value: 62.22760290556902
    - type: manhattan_precision
      value: 57.494407158836694
    - type: manhattan_recall
      value: 67.81002638522428
    - type: max_accuracy
      value: 83.47737974608094
    - type: max_ap
      value: 65.77588818364636
    - type: max_f1
      value: 62.459508098380326
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
      value: 88.64244964489463
    - type: cos_sim_ap
      value: 85.154122301394
    - type: cos_sim_f1
      value: 77.45617911327146
    - type: cos_sim_precision
      value: 74.23066064370413
    - type: cos_sim_recall
      value: 80.97474591931014
    - type: dot_accuracy
      value: 88.64244964489463
    - type: dot_ap
      value: 85.15411965587543
    - type: dot_f1
      value: 77.45617911327146
    - type: dot_precision
      value: 74.23066064370413
    - type: dot_recall
      value: 80.97474591931014
    - type: euclidean_accuracy
      value: 88.64244964489463
    - type: euclidean_ap
      value: 85.15414684113986
    - type: euclidean_f1
      value: 77.45617911327146
    - type: euclidean_precision
      value: 74.23066064370413
    - type: euclidean_recall
      value: 80.97474591931014
    - type: manhattan_accuracy
      value: 88.57841425078588
    - type: manhattan_ap
      value: 85.12472268567576
    - type: manhattan_f1
      value: 77.39497339937627
    - type: manhattan_precision
      value: 73.92584285413892
    - type: manhattan_recall
      value: 81.20572836464429
    - type: max_accuracy
      value: 88.64244964489463
    - type: max_ap
      value: 85.15414684113986
    - type: max_f1
      value: 77.45617911327146
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
      value: 79.58576208710117
license: apache-2.0
---
<h1 align="center">Snowflake's Arctic-embed-s</h1>
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

model = SentenceTransformer("Snowflake/snowflake-arctic-embed-s")

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
0.533809 The Data Cloud!
0.49207097 Mexico City of Course!
Query: Where can I get the best tacos?
0.56592476 Mexico City of Course!
0.48255116 The Data Cloud!
```

### Using Huggingface transformers


You can use the transformers package to use an snowflake-arctic-embed model, as shown below. For optimal retrieval quality, use the CLS token to embed each text portion and use the query prefix below (just on the query).



```python
import torch
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Snowflake/snowflake-arctic-embed-s')
model = AutoModel.from_pretrained('Snowflake/snowflake-arctic-embed-s', add_pooling_layer=False)
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

### Using Transformers.js

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@xenova/transformers) by running:
```bash
npm i @xenova/transformers
```

You can then use the model to compute embeddings as follows:

```js
import { pipeline, dot } from '@xenova/transformers';

// Create feature extraction pipeline
const extractor = await pipeline('feature-extraction', 'Snowflake/snowflake-arctic-embed-s', {
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
console.log(similarities); // [0.48255123876493394, 0.5659250100112143]
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