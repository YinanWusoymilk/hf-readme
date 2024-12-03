---
tags:
- mteb
- sentence-transformers
model-index:
- name: NV-Embed-v2
  results:
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 94.28358208955224
    - type: accuracy_stderr
      value: 0.40076780842082305
    - type: ap
      value: 76.49097318319616
    - type: ap_stderr
      value: 1.2418692675183929
    - type: f1
      value: 91.41982003001168
    - type: f1_stderr
      value: 0.5043921413093579
    - type: main_score
      value: 94.28358208955224
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
      value: 97.74185000000001
    - type: accuracy_stderr
      value: 0.07420471683120942
    - type: ap
      value: 96.4737144875525
    - type: ap_stderr
      value: 0.2977518241541558
    - type: f1
      value: 97.7417581594921
    - type: f1_stderr
      value: 0.07428763617010377
    - type: main_score
      value: 97.74185000000001
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
      value: 63.96000000000001
    - type: accuracy_stderr
      value: 1.815555011559825
    - type: f1
      value: 62.49361841640459
    - type: f1_stderr
      value: 2.829339314126457
    - type: main_score
      value: 63.96000000000001
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
      value: 46.515
    - type: map_at_10
      value: 62.392
    - type: map_at_100
      value: 62.732
    - type: map_at_1000
      value: 62.733000000000004
    - type: map_at_3
      value: 58.701
    - type: map_at_5
      value: 61.027
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 46.515
    - type: ndcg_at_10
      value: 70.074
    - type: ndcg_at_100
      value: 71.395
    - type: ndcg_at_1000
      value: 71.405
    - type: ndcg_at_3
      value: 62.643
    - type: ndcg_at_5
      value: 66.803
    - type: precision_at_1
      value: 46.515
    - type: precision_at_10
      value: 9.41
    - type: precision_at_100
      value: 0.996
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 24.68
    - type: precision_at_5
      value: 16.814
    - type: recall_at_1
      value: 46.515
    - type: recall_at_10
      value: 94.097
    - type: recall_at_100
      value: 99.57300000000001
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 74.03999999999999
    - type: recall_at_5
      value: 84.068
    - type: main_score
      value: 70.074
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 55.79933795955242
    - type: v_measure
      value: 55.79933795955242
    - type: v_measure_std
      value: 14.575108141916148
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringS2S
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
      split: test
      type: mteb/arxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 51.262845995850334
    - type: v_measure
      value: 51.262845995850334
    - type: v_measure_std
      value: 14.727824473104173
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
      value: 67.46477327480808
    - type: mrr
      value: 79.50160488941653
    - type: main_score
      value: 67.46477327480808
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB BIOSSES
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: cosine_pearson
      value: 89.74311007980987
    - type: cosine_spearman
      value: 87.41644967443246
    - type: manhattan_pearson
      value: 88.57457108347744
    - type: manhattan_spearman
      value: 87.59295972042997
    - type: euclidean_pearson
      value: 88.27108977118459
    - type: euclidean_spearman
      value: 87.41644967443246
    - type: main_score
      value: 87.41644967443246
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
      value: 92.41558441558443
    - type: accuracy_stderr
      value: 0.37701502251934443
    - type: f1
      value: 92.38130170447671
    - type: f1_stderr
      value: 0.39115151225617767
    - type: main_score
      value: 92.41558441558443
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 54.08649516394218
    - type: v_measure
      value: 54.08649516394218
    - type: v_measure_std
      value: 0.5303233693045373
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringS2S
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
      split: test
      type: mteb/biorxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 49.60352214167779
    - type: v_measure
      value: 49.60352214167779
    - type: v_measure_std
      value: 0.7176198612516721
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval
      revision: 46989137a86843e03a6195de44b09deda022eec7
      split: test
      type: CQADupstackRetrieval_is_a_combined_dataset
    metrics:
    - type: map_at_1
      value: 31.913249999999998
    - type: map_at_10
      value: 43.87733333333334
    - type: map_at_100
      value: 45.249916666666664
    - type: map_at_1000
      value: 45.350583333333326
    - type: map_at_3
      value: 40.316833333333335
    - type: map_at_5
      value: 42.317083333333336
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 38.30616666666667
    - type: ndcg_at_10
      value: 50.24175000000001
    - type: ndcg_at_100
      value: 55.345333333333336
    - type: ndcg_at_1000
      value: 56.91225000000001
    - type: ndcg_at_3
      value: 44.67558333333333
    - type: ndcg_at_5
      value: 47.32333333333334
    - type: precision_at_1
      value: 38.30616666666667
    - type: precision_at_10
      value: 9.007416666666666
    - type: precision_at_100
      value: 1.3633333333333333
    - type: precision_at_1000
      value: 0.16691666666666666
    - type: precision_at_3
      value: 20.895666666666667
    - type: precision_at_5
      value: 14.871666666666666
    - type: recall_at_1
      value: 31.913249999999998
    - type: recall_at_10
      value: 64.11891666666666
    - type: recall_at_100
      value: 85.91133333333333
    - type: recall_at_1000
      value: 96.28225
    - type: recall_at_3
      value: 48.54749999999999
    - type: recall_at_5
      value: 55.44283333333334
    - type: main_score
      value: 50.24175000000001
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
      value: 19.556
    - type: map_at_10
      value: 34.623
    - type: map_at_100
      value: 36.97
    - type: map_at_1000
      value: 37.123
    - type: map_at_3
      value: 28.904999999999998
    - type: map_at_5
      value: 31.955
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 44.104
    - type: ndcg_at_10
      value: 45.388
    - type: ndcg_at_100
      value: 52.793
    - type: ndcg_at_1000
      value: 55.108999999999995
    - type: ndcg_at_3
      value: 38.604
    - type: ndcg_at_5
      value: 40.806
    - type: precision_at_1
      value: 44.104
    - type: precision_at_10
      value: 14.143
    - type: precision_at_100
      value: 2.2190000000000003
    - type: precision_at_1000
      value: 0.266
    - type: precision_at_3
      value: 29.316
    - type: precision_at_5
      value: 21.98
    - type: recall_at_1
      value: 19.556
    - type: recall_at_10
      value: 52.120999999999995
    - type: recall_at_100
      value: 76.509
    - type: recall_at_1000
      value: 89.029
    - type: recall_at_3
      value: 34.919
    - type: recall_at_5
      value: 42.18
    - type: main_score
      value: 45.388
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
      value: 10.714
    - type: map_at_10
      value: 25.814999999999998
    - type: map_at_100
      value: 37.845
    - type: map_at_1000
      value: 39.974
    - type: map_at_3
      value: 17.201
    - type: map_at_5
      value: 21.062
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 66.0
    - type: ndcg_at_10
      value: 53.496
    - type: ndcg_at_100
      value: 58.053
    - type: ndcg_at_1000
      value: 64.886
    - type: ndcg_at_3
      value: 57.656
    - type: ndcg_at_5
      value: 55.900000000000006
    - type: precision_at_1
      value: 77.25
    - type: precision_at_10
      value: 43.65
    - type: precision_at_100
      value: 13.76
    - type: precision_at_1000
      value: 2.5940000000000003
    - type: precision_at_3
      value: 61.0
    - type: precision_at_5
      value: 54.65
    - type: recall_at_1
      value: 10.714
    - type: recall_at_10
      value: 31.173000000000002
    - type: recall_at_100
      value: 63.404
    - type: recall_at_1000
      value: 85.874
    - type: recall_at_3
      value: 18.249000000000002
    - type: recall_at_5
      value: 23.69
    - type: main_score
      value: 53.496
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
      value: 93.38499999999999
    - type: accuracy_stderr
      value: 0.13793114224133846
    - type: f1
      value: 90.12141028353496
    - type: f1_stderr
      value: 0.174640257706043
    - type: main_score
      value: 93.38499999999999
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
      value: 84.66900000000001
    - type: map_at_10
      value: 91.52799999999999
    - type: map_at_100
      value: 91.721
    - type: map_at_1000
      value: 91.73
    - type: map_at_3
      value: 90.752
    - type: map_at_5
      value: 91.262
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 91.20899999999999
    - type: ndcg_at_10
      value: 93.74900000000001
    - type: ndcg_at_100
      value: 94.279
    - type: ndcg_at_1000
      value: 94.408
    - type: ndcg_at_3
      value: 92.923
    - type: ndcg_at_5
      value: 93.376
    - type: precision_at_1
      value: 91.20899999999999
    - type: precision_at_10
      value: 11.059
    - type: precision_at_100
      value: 1.1560000000000001
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: precision_at_3
      value: 35.129
    - type: precision_at_5
      value: 21.617
    - type: recall_at_1
      value: 84.66900000000001
    - type: recall_at_10
      value: 97.03399999999999
    - type: recall_at_100
      value: 98.931
    - type: recall_at_1000
      value: 99.65899999999999
    - type: recall_at_3
      value: 94.76299999999999
    - type: recall_at_5
      value: 95.968
    - type: main_score
      value: 93.74900000000001
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
      value: 34.866
    - type: map_at_10
      value: 58.06099999999999
    - type: map_at_100
      value: 60.028999999999996
    - type: map_at_1000
      value: 60.119
    - type: map_at_3
      value: 51.304
    - type: map_at_5
      value: 55.054
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 64.815
    - type: ndcg_at_10
      value: 65.729
    - type: ndcg_at_100
      value: 71.14
    - type: ndcg_at_1000
      value: 72.336
    - type: ndcg_at_3
      value: 61.973
    - type: ndcg_at_5
      value: 62.858000000000004
    - type: precision_at_1
      value: 64.815
    - type: precision_at_10
      value: 17.87
    - type: precision_at_100
      value: 2.373
    - type: precision_at_1000
      value: 0.258
    - type: precision_at_3
      value: 41.152
    - type: precision_at_5
      value: 29.568
    - type: recall_at_1
      value: 34.866
    - type: recall_at_10
      value: 72.239
    - type: recall_at_100
      value: 91.19
    - type: recall_at_1000
      value: 98.154
    - type: recall_at_3
      value: 56.472
    - type: recall_at_5
      value: 63.157
    - type: main_score
      value: 65.729
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
      value: 44.651999999999994
    - type: map_at_10
      value: 79.95100000000001
    - type: map_at_100
      value: 80.51700000000001
    - type: map_at_1000
      value: 80.542
    - type: map_at_3
      value: 77.008
    - type: map_at_5
      value: 78.935
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 89.305
    - type: ndcg_at_10
      value: 85.479
    - type: ndcg_at_100
      value: 87.235
    - type: ndcg_at_1000
      value: 87.669
    - type: ndcg_at_3
      value: 81.648
    - type: ndcg_at_5
      value: 83.88600000000001
    - type: precision_at_1
      value: 89.305
    - type: precision_at_10
      value: 17.807000000000002
    - type: precision_at_100
      value: 1.9140000000000001
    - type: precision_at_1000
      value: 0.197
    - type: precision_at_3
      value: 53.756
    - type: precision_at_5
      value: 34.018
    - type: recall_at_1
      value: 44.651999999999994
    - type: recall_at_10
      value: 89.034
    - type: recall_at_100
      value: 95.719
    - type: recall_at_1000
      value: 98.535
    - type: recall_at_3
      value: 80.635
    - type: recall_at_5
      value: 85.044
    - type: main_score
      value: 85.479
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
      value: 97.1376
    - type: accuracy_stderr
      value: 0.04571914259913447
    - type: ap
      value: 95.92783808558808
    - type: ap_stderr
      value: 0.05063782483358255
    - type: f1
      value: 97.13755519177172
    - type: f1_stderr
      value: 0.04575943074086138
    - type: main_score
      value: 97.1376
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
      value: 0.0
    - type: map_at_10
      value: 38.342
    - type: map_at_100
      value: 0.0
    - type: map_at_1000
      value: 0.0
    - type: map_at_3
      value: 0.0
    - type: map_at_5
      value: 0.0
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 0.0
    - type: ndcg_at_10
      value: 45.629999999999995
    - type: ndcg_at_100
      value: 0.0
    - type: ndcg_at_1000
      value: 0.0
    - type: ndcg_at_3
      value: 0.0
    - type: ndcg_at_5
      value: 0.0
    - type: precision_at_1
      value: 0.0
    - type: precision_at_10
      value: 7.119000000000001
    - type: precision_at_100
      value: 0.0
    - type: precision_at_1000
      value: 0.0
    - type: precision_at_3
      value: 0.0
    - type: precision_at_5
      value: 0.0
    - type: recall_at_1
      value: 0.0
    - type: recall_at_10
      value: 67.972
    - type: recall_at_100
      value: 0.0
    - type: recall_at_1000
      value: 0.0
    - type: recall_at_3
      value: 0.0
    - type: recall_at_5
      value: 0.0
    - type: main_score
      value: 45.629999999999995
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
      value: 99.24988600091199
    - type: accuracy_stderr
      value: 0.04496826931900734
    - type: f1
      value: 99.15933275095276
    - type: f1_stderr
      value: 0.05565039139747446
    - type: main_score
      value: 99.24988600091199
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
      value: 94.3684450524396
    - type: accuracy_stderr
      value: 0.8436548701322188
    - type: f1
      value: 77.33022623133307
    - type: f1_stderr
      value: 0.9228425861187275
    - type: main_score
      value: 94.3684450524396
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
      value: 86.09616677874916
    - type: accuracy_stderr
      value: 0.9943208055590853
    - type: f1
      value: 83.4902056490062
    - type: f1_stderr
      value: 0.7626189310074184
    - type: main_score
      value: 86.09616677874916
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
      value: 92.17215870880968
    - type: accuracy_stderr
      value: 0.25949941333658166
    - type: f1
      value: 91.36757392422702
    - type: f1_stderr
      value: 0.29139507298154815
    - type: main_score
      value: 92.17215870880968
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MedrxivClusteringP2P
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
      split: test
      type: mteb/medrxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 46.09497344077905
    - type: v_measure
      value: 46.09497344077905
    - type: v_measure_std
      value: 1.44871520869784
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MedrxivClusteringS2S
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
      split: test
      type: mteb/medrxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 44.861049989560684
    - type: v_measure
      value: 44.861049989560684
    - type: v_measure_std
      value: 1.432199293162203
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
      value: 31.75936162919999
    - type: mrr
      value: 32.966812736541236
    - type: main_score
      value: 31.75936162919999
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
      value: 7.893999999999999
    - type: map_at_10
      value: 17.95
    - type: map_at_100
      value: 23.474
    - type: map_at_1000
      value: 25.412000000000003
    - type: map_at_3
      value: 12.884
    - type: map_at_5
      value: 15.171000000000001
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 55.728
    - type: ndcg_at_10
      value: 45.174
    - type: ndcg_at_100
      value: 42.18
    - type: ndcg_at_1000
      value: 50.793
    - type: ndcg_at_3
      value: 50.322
    - type: ndcg_at_5
      value: 48.244
    - type: precision_at_1
      value: 57.276
    - type: precision_at_10
      value: 33.437
    - type: precision_at_100
      value: 10.671999999999999
    - type: precision_at_1000
      value: 2.407
    - type: precision_at_3
      value: 46.646
    - type: precision_at_5
      value: 41.672
    - type: recall_at_1
      value: 7.893999999999999
    - type: recall_at_10
      value: 22.831000000000003
    - type: recall_at_100
      value: 43.818
    - type: recall_at_1000
      value: 75.009
    - type: recall_at_3
      value: 14.371
    - type: recall_at_5
      value: 17.752000000000002
    - type: main_score
      value: 45.174
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
      value: 49.351
    - type: map_at_10
      value: 66.682
    - type: map_at_100
      value: 67.179
    - type: map_at_1000
      value: 67.18499999999999
    - type: map_at_3
      value: 62.958999999999996
    - type: map_at_5
      value: 65.364
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 55.417
    - type: ndcg_at_10
      value: 73.568
    - type: ndcg_at_100
      value: 75.35
    - type: ndcg_at_1000
      value: 75.478
    - type: ndcg_at_3
      value: 67.201
    - type: ndcg_at_5
      value: 70.896
    - type: precision_at_1
      value: 55.417
    - type: precision_at_10
      value: 11.036999999999999
    - type: precision_at_100
      value: 1.204
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 29.654000000000003
    - type: precision_at_5
      value: 20.006
    - type: recall_at_1
      value: 49.351
    - type: recall_at_10
      value: 91.667
    - type: recall_at_100
      value: 98.89
    - type: recall_at_1000
      value: 99.812
    - type: recall_at_3
      value: 75.715
    - type: recall_at_5
      value: 84.072
    - type: main_score
      value: 73.568
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB QuoraRetrieval
      revision: e4e08e0b7dbe3c8700f0daef558ff32256715259
      split: test
      type: mteb/quora
    metrics:
    - type: map_at_1
      value: 71.358
    - type: map_at_10
      value: 85.474
    - type: map_at_100
      value: 86.101
    - type: map_at_1000
      value: 86.114
    - type: map_at_3
      value: 82.562
    - type: map_at_5
      value: 84.396
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 82.12
    - type: ndcg_at_10
      value: 89.035
    - type: ndcg_at_100
      value: 90.17399999999999
    - type: ndcg_at_1000
      value: 90.243
    - type: ndcg_at_3
      value: 86.32300000000001
    - type: ndcg_at_5
      value: 87.85
    - type: precision_at_1
      value: 82.12
    - type: precision_at_10
      value: 13.55
    - type: precision_at_100
      value: 1.54
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 37.89
    - type: precision_at_5
      value: 24.9
    - type: recall_at_1
      value: 71.358
    - type: recall_at_10
      value: 95.855
    - type: recall_at_100
      value: 99.711
    - type: recall_at_1000
      value: 99.994
    - type: recall_at_3
      value: 88.02
    - type: recall_at_5
      value: 92.378
    - type: main_score
      value: 89.035
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB RedditClustering
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
      split: test
      type: mteb/reddit-clustering
    metrics:
    - type: main_score
      value: 71.0984522742521
    - type: v_measure
      value: 71.0984522742521
    - type: v_measure_std
      value: 3.5668139917058044
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RedditClusteringP2P
      revision: 385e3cb46b4cfa89021f56c4380204149d0efe33
      split: test
      type: mteb/reddit-clustering-p2p
    metrics:
    - type: main_score
      value: 74.94499641904133
    - type: v_measure
      value: 74.94499641904133
    - type: v_measure_std
      value: 11.419672879389248
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB SCIDOCS
      revision: f8c2fcf00f625baaa80f62ec5bd9e1fff3b8ae88
      split: test
      type: mteb/scidocs
    metrics:
    - type: map_at_1
      value: 5.343
    - type: map_at_10
      value: 13.044
    - type: map_at_100
      value: 15.290999999999999
    - type: map_at_1000
      value: 15.609
    - type: map_at_3
      value: 9.227
    - type: map_at_5
      value: 11.158
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 26.3
    - type: ndcg_at_10
      value: 21.901
    - type: ndcg_at_100
      value: 30.316
    - type: ndcg_at_1000
      value: 35.547000000000004
    - type: ndcg_at_3
      value: 20.560000000000002
    - type: ndcg_at_5
      value: 18.187
    - type: precision_at_1
      value: 26.3
    - type: precision_at_10
      value: 11.34
    - type: precision_at_100
      value: 2.344
    - type: precision_at_1000
      value: 0.359
    - type: precision_at_3
      value: 18.967
    - type: precision_at_5
      value: 15.920000000000002
    - type: recall_at_1
      value: 5.343
    - type: recall_at_10
      value: 22.997
    - type: recall_at_100
      value: 47.562
    - type: recall_at_1000
      value: 72.94500000000001
    - type: recall_at_3
      value: 11.533
    - type: recall_at_5
      value: 16.148
    - type: main_score
      value: 21.901
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SICK-R
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
      split: test
      type: mteb/sickr-sts
    metrics:
    - type: cosine_pearson
      value: 87.3054603493591
    - type: cosine_spearman
      value: 82.14763206055602
    - type: manhattan_pearson
      value: 84.78737790237557
    - type: manhattan_spearman
      value: 81.88455356002758
    - type: euclidean_pearson
      value: 85.00668629311117
    - type: euclidean_spearman
      value: 82.14763037860851
    - type: main_score
      value: 82.14763206055602
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS12
      revision: a0d554a64d88156834ff5ae9920b964011b16384
      split: test
      type: mteb/sts12-sts
    metrics:
    - type: cosine_pearson
      value: 86.6911864687294
    - type: cosine_spearman
      value: 77.89286260403269
    - type: manhattan_pearson
      value: 82.87240347680857
    - type: manhattan_spearman
      value: 78.10055393740326
    - type: euclidean_pearson
      value: 82.72282535777123
    - type: euclidean_spearman
      value: 77.89256648406325
    - type: main_score
      value: 77.89286260403269
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS13
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
      split: test
      type: mteb/sts13-sts
    metrics:
    - type: cosine_pearson
      value: 87.7220832598633
    - type: cosine_spearman
      value: 88.30238972017452
    - type: manhattan_pearson
      value: 87.88214789140248
    - type: manhattan_spearman
      value: 88.24770220032391
    - type: euclidean_pearson
      value: 87.98610386257103
    - type: euclidean_spearman
      value: 88.30238972017452
    - type: main_score
      value: 88.30238972017452
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS14
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
      split: test
      type: mteb/sts14-sts
    metrics:
    - type: cosine_pearson
      value: 85.70614623247714
    - type: cosine_spearman
      value: 84.29920990970672
    - type: manhattan_pearson
      value: 84.9836190531721
    - type: manhattan_spearman
      value: 84.40933470597638
    - type: euclidean_pearson
      value: 84.96652336693347
    - type: euclidean_spearman
      value: 84.29920989531965
    - type: main_score
      value: 84.29920990970672
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS15
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
      split: test
      type: mteb/sts15-sts
    metrics:
    - type: cosine_pearson
      value: 88.4169972425264
    - type: cosine_spearman
      value: 89.03555007807218
    - type: manhattan_pearson
      value: 88.83068699455478
    - type: manhattan_spearman
      value: 89.21877175674125
    - type: euclidean_pearson
      value: 88.7251052947544
    - type: euclidean_spearman
      value: 89.03557389893083
    - type: main_score
      value: 89.03555007807218
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS16
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
      split: test
      type: mteb/sts16-sts
    metrics:
    - type: cosine_pearson
      value: 85.63830579034632
    - type: cosine_spearman
      value: 86.77353371581373
    - type: manhattan_pearson
      value: 86.24830492396637
    - type: manhattan_spearman
      value: 86.96754348626189
    - type: euclidean_pearson
      value: 86.09837038778359
    - type: euclidean_spearman
      value: 86.77353371581373
    - type: main_score
      value: 86.77353371581373
    task:
      type: STS
  - dataset:
      config: en-en
      name: MTEB STS17 (en-en)
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 91.2204675588959
    - type: cosine_spearman
      value: 90.66976712249057
    - type: manhattan_pearson
      value: 91.11007808242346
    - type: manhattan_spearman
      value: 90.51739232964488
    - type: euclidean_pearson
      value: 91.19588941007903
    - type: euclidean_spearman
      value: 90.66976712249057
    - type: main_score
      value: 90.66976712249057
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STS22 (en)
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 69.34416749707114
    - type: cosine_spearman
      value: 68.11632448161046
    - type: manhattan_pearson
      value: 68.99243488935281
    - type: manhattan_spearman
      value: 67.8398546438258
    - type: euclidean_pearson
      value: 69.06376010216088
    - type: euclidean_spearman
      value: 68.11632448161046
    - type: main_score
      value: 68.11632448161046
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSBenchmark
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
      split: test
      type: mteb/stsbenchmark-sts
    metrics:
    - type: cosine_pearson
      value: 88.10309739429758
    - type: cosine_spearman
      value: 88.40520383147418
    - type: manhattan_pearson
      value: 88.50753383813232
    - type: manhattan_spearman
      value: 88.66382629460927
    - type: euclidean_pearson
      value: 88.35050664609376
    - type: euclidean_spearman
      value: 88.40520383147418
    - type: main_score
      value: 88.40520383147418
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
      value: 87.58627126942797
    - type: mrr
      value: 97.01098103058887
    - type: main_score
      value: 87.58627126942797
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
      value: 62.883
    - type: map_at_10
      value: 75.371
    - type: map_at_100
      value: 75.66000000000001
    - type: map_at_1000
      value: 75.667
    - type: map_at_3
      value: 72.741
    - type: map_at_5
      value: 74.74
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 66.0
    - type: ndcg_at_10
      value: 80.12700000000001
    - type: ndcg_at_100
      value: 81.291
    - type: ndcg_at_1000
      value: 81.464
    - type: ndcg_at_3
      value: 76.19
    - type: ndcg_at_5
      value: 78.827
    - type: precision_at_1
      value: 66.0
    - type: precision_at_10
      value: 10.567
    - type: precision_at_100
      value: 1.117
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 30.333
    - type: precision_at_5
      value: 20.133000000000003
    - type: recall_at_1
      value: 62.883
    - type: recall_at_10
      value: 93.556
    - type: recall_at_100
      value: 98.667
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 83.322
    - type: recall_at_5
      value: 89.756
    - type: main_score
      value: 80.12700000000001
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
      value: 99.87524752475248
    - type: cos_sim_accuracy_threshold
      value: 74.86587762832642
    - type: cos_sim_ap
      value: 97.02222446606328
    - type: cos_sim_f1
      value: 93.66197183098592
    - type: cos_sim_f1_threshold
      value: 74.74223375320435
    - type: cos_sim_precision
      value: 94.23076923076923
    - type: cos_sim_recall
      value: 93.10000000000001
    - type: dot_accuracy
      value: 99.87524752475248
    - type: dot_accuracy_threshold
      value: 74.86587762832642
    - type: dot_ap
      value: 97.02222688043362
    - type: dot_f1
      value: 93.66197183098592
    - type: dot_f1_threshold
      value: 74.74223375320435
    - type: dot_precision
      value: 94.23076923076923
    - type: dot_recall
      value: 93.10000000000001
    - type: euclidean_accuracy
      value: 99.87524752475248
    - type: euclidean_accuracy_threshold
      value: 70.9000825881958
    - type: euclidean_ap
      value: 97.02222446606329
    - type: euclidean_f1
      value: 93.66197183098592
    - type: euclidean_f1_threshold
      value: 71.07426524162292
    - type: euclidean_precision
      value: 94.23076923076923
    - type: euclidean_recall
      value: 93.10000000000001
    - type: manhattan_accuracy
      value: 99.87623762376238
    - type: manhattan_accuracy_threshold
      value: 3588.5040283203125
    - type: manhattan_ap
      value: 97.09194643777883
    - type: manhattan_f1
      value: 93.7375745526839
    - type: manhattan_f1_threshold
      value: 3664.3760681152344
    - type: manhattan_precision
      value: 93.18181818181817
    - type: manhattan_recall
      value: 94.3
    - type: max_accuracy
      value: 99.87623762376238
    - type: max_ap
      value: 97.09194643777883
    - type: max_f1
      value: 93.7375745526839
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB StackExchangeClustering
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
      split: test
      type: mteb/stackexchange-clustering
    metrics:
    - type: main_score
      value: 82.10134099988541
    - type: v_measure
      value: 82.10134099988541
    - type: v_measure_std
      value: 2.7926349897769533
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackExchangeClusteringP2P
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
      split: test
      type: mteb/stackexchange-clustering-p2p
    metrics:
    - type: main_score
      value: 48.357450742397404
    - type: v_measure
      value: 48.357450742397404
    - type: v_measure_std
      value: 1.520118876440547
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
      value: 55.79277200802986
    - type: mrr
      value: 56.742517082590616
    - type: main_score
      value: 55.79277200802986
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SummEval
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
      split: test
      type: mteb/summeval
    metrics:
    - type: cosine_spearman
      value: 30.701215774712693
    - type: cosine_pearson
      value: 31.26740037278488
    - type: dot_spearman
      value: 30.701215774712693
    - type: dot_pearson
      value: 31.267404144879997
    - type: main_score
      value: 30.701215774712693
    task:
      type: Summarization
  - dataset:
      config: default
      name: MTEB TRECCOVID
      revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
      split: test
      type: mteb/trec-covid
    metrics:
    - type: map_at_1
      value: 0.23800000000000002
    - type: map_at_10
      value: 2.31
    - type: map_at_100
      value: 15.495000000000001
    - type: map_at_1000
      value: 38.829
    - type: map_at_3
      value: 0.72
    - type: map_at_5
      value: 1.185
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 91.0
    - type: ndcg_at_10
      value: 88.442
    - type: ndcg_at_100
      value: 71.39
    - type: ndcg_at_1000
      value: 64.153
    - type: ndcg_at_3
      value: 89.877
    - type: ndcg_at_5
      value: 89.562
    - type: precision_at_1
      value: 92.0
    - type: precision_at_10
      value: 92.60000000000001
    - type: precision_at_100
      value: 73.74000000000001
    - type: precision_at_1000
      value: 28.222
    - type: precision_at_3
      value: 94.0
    - type: precision_at_5
      value: 93.60000000000001
    - type: recall_at_1
      value: 0.23800000000000002
    - type: recall_at_10
      value: 2.428
    - type: recall_at_100
      value: 18.099999999999998
    - type: recall_at_1000
      value: 60.79599999999999
    - type: recall_at_3
      value: 0.749
    - type: recall_at_5
      value: 1.238
    - type: main_score
      value: 88.442
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
      value: 3.4939999999999998
    - type: map_at_10
      value: 12.531999999999998
    - type: map_at_100
      value: 19.147
    - type: map_at_1000
      value: 20.861
    - type: map_at_3
      value: 7.558
    - type: map_at_5
      value: 9.49
    - type: mrr_at_1
      value: 0.0
    - type: mrr_at_10
      value: 0.0
    - type: mrr_at_100
      value: 0.0
    - type: mrr_at_1000
      value: 0.0
    - type: mrr_at_3
      value: 0.0
    - type: mrr_at_5
      value: 0.0
    - type: ndcg_at_1
      value: 47.959
    - type: ndcg_at_10
      value: 31.781
    - type: ndcg_at_100
      value: 42.131
    - type: ndcg_at_1000
      value: 53.493
    - type: ndcg_at_3
      value: 39.204
    - type: ndcg_at_5
      value: 34.635
    - type: precision_at_1
      value: 48.980000000000004
    - type: precision_at_10
      value: 27.143
    - type: precision_at_100
      value: 8.224
    - type: precision_at_1000
      value: 1.584
    - type: precision_at_3
      value: 38.775999999999996
    - type: precision_at_5
      value: 33.061
    - type: recall_at_1
      value: 3.4939999999999998
    - type: recall_at_10
      value: 18.895
    - type: recall_at_100
      value: 50.192
    - type: recall_at_1000
      value: 85.167
    - type: recall_at_3
      value: 8.703
    - type: recall_at_5
      value: 11.824
    - type: main_score
      value: 31.781
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ToxicConversationsClassification
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
      split: test
      type: mteb/toxic_conversations_50k
    metrics:
    - type: accuracy
      value: 92.7402
    - type: accuracy_stderr
      value: 1.020764595781027
    - type: ap
      value: 44.38594756333084
    - type: ap_stderr
      value: 1.817150701258273
    - type: f1
      value: 79.95699280019547
    - type: f1_stderr
      value: 1.334582498702029
    - type: main_score
      value: 92.7402
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
      value: 80.86870401810978
    - type: accuracy_stderr
      value: 0.22688467782004712
    - type: f1
      value: 81.1829040745744
    - type: f1_stderr
      value: 0.19774920574849694
    - type: main_score
      value: 80.86870401810978
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TwentyNewsgroupsClustering
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
      split: test
      type: mteb/twentynewsgroups-clustering
    metrics:
    - type: main_score
      value: 64.82048869927482
    - type: v_measure
      value: 64.82048869927482
    - type: v_measure_std
      value: 0.9170394252450564
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
      value: 88.44251057996067
    - type: cos_sim_accuracy_threshold
      value: 70.2150285243988
    - type: cos_sim_ap
      value: 81.11422351199913
    - type: cos_sim_f1
      value: 73.71062868615887
    - type: cos_sim_f1_threshold
      value: 66.507488489151
    - type: cos_sim_precision
      value: 70.2799712849964
    - type: cos_sim_recall
      value: 77.4934036939314
    - type: dot_accuracy
      value: 88.44251057996067
    - type: dot_accuracy_threshold
      value: 70.2150285243988
    - type: dot_ap
      value: 81.11420529068658
    - type: dot_f1
      value: 73.71062868615887
    - type: dot_f1_threshold
      value: 66.50749444961548
    - type: dot_precision
      value: 70.2799712849964
    - type: dot_recall
      value: 77.4934036939314
    - type: euclidean_accuracy
      value: 88.44251057996067
    - type: euclidean_accuracy_threshold
      value: 77.18156576156616
    - type: euclidean_ap
      value: 81.11422421732487
    - type: euclidean_f1
      value: 73.71062868615887
    - type: euclidean_f1_threshold
      value: 81.84436559677124
    - type: euclidean_precision
      value: 70.2799712849964
    - type: euclidean_recall
      value: 77.4934036939314
    - type: manhattan_accuracy
      value: 88.26369434344639
    - type: manhattan_accuracy_threshold
      value: 3837.067413330078
    - type: manhattan_ap
      value: 80.81442360477725
    - type: manhattan_f1
      value: 73.39883099117024
    - type: manhattan_f1_threshold
      value: 4098.833847045898
    - type: manhattan_precision
      value: 69.41896024464832
    - type: manhattan_recall
      value: 77.86279683377309
    - type: max_accuracy
      value: 88.44251057996067
    - type: max_ap
      value: 81.11422421732487
    - type: max_f1
      value: 73.71062868615887
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
      value: 90.03182365040556
    - type: cos_sim_accuracy_threshold
      value: 64.46443796157837
    - type: cos_sim_ap
      value: 87.86649113691112
    - type: cos_sim_f1
      value: 80.45644844577821
    - type: cos_sim_f1_threshold
      value: 61.40774488449097
    - type: cos_sim_precision
      value: 77.54052702992216
    - type: cos_sim_recall
      value: 83.60024638127503
    - type: dot_accuracy
      value: 90.03182365040556
    - type: dot_accuracy_threshold
      value: 64.46444988250732
    - type: dot_ap
      value: 87.86649011954319
    - type: dot_f1
      value: 80.45644844577821
    - type: dot_f1_threshold
      value: 61.407750844955444
    - type: dot_precision
      value: 77.54052702992216
    - type: dot_recall
      value: 83.60024638127503
    - type: euclidean_accuracy
      value: 90.03182365040556
    - type: euclidean_accuracy_threshold
      value: 84.30368900299072
    - type: euclidean_ap
      value: 87.86649114275045
    - type: euclidean_f1
      value: 80.45644844577821
    - type: euclidean_f1_threshold
      value: 87.8547191619873
    - type: euclidean_precision
      value: 77.54052702992216
    - type: euclidean_recall
      value: 83.60024638127503
    - type: manhattan_accuracy
      value: 89.99883572010712
    - type: manhattan_accuracy_threshold
      value: 4206.838607788086
    - type: manhattan_ap
      value: 87.8600826607838
    - type: manhattan_f1
      value: 80.44054508120217
    - type: manhattan_f1_threshold
      value: 4372.755432128906
    - type: manhattan_precision
      value: 78.08219178082192
    - type: manhattan_recall
      value: 82.94579611949491
    - type: max_accuracy
      value: 90.03182365040556
    - type: max_ap
      value: 87.86649114275045
    - type: max_f1
      value: 80.45644844577821
    task:
      type: PairClassification
language:
- en
license: cc-by-nc-4.0
library_name: transformers
---
## Introduction
We present NV-Embed-v2, a generalist embedding model that ranks No. 1 on the Massive Text Embedding Benchmark ([MTEB benchmark](https://huggingface.co/spaces/mteb/leaderboard))(as of Aug 30, 2024) with a score of 72.31 across 56 text embedding tasks. It also holds the No. 1 in the retrieval sub-category (a score of 62.65 across 15 tasks) in the leaderboard, which is essential to the development of RAG technology.

NV-Embed-v2 presents several new designs, including having the LLM attend to latent vectors for better pooled embedding output, and demonstrating a two-staged instruction tuning method to enhance the accuracy of both retrieval and non-retrieval tasks. Additionally, NV-Embed-v2 incorporates a novel hard-negative mining methods that take into account the positive relevance score for better false negatives removal.

For more technical details, refer to our paper: [NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models](https://arxiv.org/pdf/2405.17428).

## Model Details
- Base Decoder-only LLM: [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)
- Pooling Type: Latent-Attention
- Embedding Dimension: 4096

## How to use

Here is an example of how to encode queries and passages using Huggingface-transformer and Sentence-transformer. Please find the required package version [here](https://huggingface.co/nvidia/NV-Embed-v2#2-required-packages).

### Usage (HuggingFace Transformers)

```python
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

# Each query needs to be accompanied by an corresponding instruction describing the task.
task_name_to_instruct = {"example": "Given a question, retrieve passages that answer the question",}

query_prefix = "Instruct: "+task_name_to_instruct["example"]+"\nQuery: "
queries = [
    'are judo throws allowed in wrestling?', 
    'how to become a radiology technician in michigan?'
    ]

# No instruction needed for retrieval passages
passage_prefix = ""
passages = [
    "Since you're reading this, you are probably someone from a judo background or someone who is just wondering how judo techniques can be applied under wrestling rules. So without further ado, let's get to the question. Are Judo throws allowed in wrestling? Yes, judo throws are allowed in freestyle and folkstyle wrestling. You only need to be careful to follow the slam rules when executing judo throws. In wrestling, a slam is lifting and returning an opponent to the mat with unnecessary force.",
    "Below are the basic steps to becoming a radiologic technologist in Michigan:Earn a high school diploma. As with most careers in health care, a high school education is the first step to finding entry-level employment. Taking classes in math and science, such as anatomy, biology, chemistry, physiology, and physics, can help prepare students for their college studies and future careers.Earn an associate degree. Entry-level radiologic positions typically require at least an Associate of Applied Science. Before enrolling in one of these degree programs, students should make sure it has been properly accredited by the Joint Review Committee on Education in Radiologic Technology (JRCERT).Get licensed or certified in the state of Michigan."
]

# load model with tokenizer
model = AutoModel.from_pretrained('nvidia/NV-Embed-v2', trust_remote_code=True)

# get the embeddings
max_length = 32768
query_embeddings = model.encode(queries, instruction=query_prefix, max_length=max_length)
passage_embeddings = model.encode(passages, instruction=passage_prefix, max_length=max_length)

# normalize embeddings
query_embeddings = F.normalize(query_embeddings, p=2, dim=1)
passage_embeddings = F.normalize(passage_embeddings, p=2, dim=1)

# get the embeddings with DataLoader (spliting the datasets into multiple mini-batches)
# batch_size=2
# query_embeddings = model._do_encode(queries, batch_size=batch_size, instruction=query_prefix, max_length=max_length, num_workers=32, return_numpy=True)
# passage_embeddings = model._do_encode(passages, batch_size=batch_size, instruction=passage_prefix, max_length=max_length, num_workers=32, return_numpy=True)

scores = (query_embeddings @ passage_embeddings.T) * 100
print(scores.tolist())
# [[87.42693328857422, 0.46283677220344543], [0.965264618396759, 86.03721618652344]]
```


### Usage (Sentence-Transformers)

```python
import torch
from sentence_transformers import SentenceTransformer

# Each query needs to be accompanied by an corresponding instruction describing the task.
task_name_to_instruct = {"example": "Given a question, retrieve passages that answer the question",}

query_prefix = "Instruct: "+task_name_to_instruct["example"]+"\nQuery: "
queries = [
    'are judo throws allowed in wrestling?', 
    'how to become a radiology technician in michigan?'
    ]

# No instruction needed for retrieval passages
passages = [
    "Since you're reading this, you are probably someone from a judo background or someone who is just wondering how judo techniques can be applied under wrestling rules. So without further ado, let's get to the question. Are Judo throws allowed in wrestling? Yes, judo throws are allowed in freestyle and folkstyle wrestling. You only need to be careful to follow the slam rules when executing judo throws. In wrestling, a slam is lifting and returning an opponent to the mat with unnecessary force.",
    "Below are the basic steps to becoming a radiologic technologist in Michigan:Earn a high school diploma. As with most careers in health care, a high school education is the first step to finding entry-level employment. Taking classes in math and science, such as anatomy, biology, chemistry, physiology, and physics, can help prepare students for their college studies and future careers.Earn an associate degree. Entry-level radiologic positions typically require at least an Associate of Applied Science. Before enrolling in one of these degree programs, students should make sure it has been properly accredited by the Joint Review Committee on Education in Radiologic Technology (JRCERT).Get licensed or certified in the state of Michigan."
]

# load model with tokenizer
model = SentenceTransformer('nvidia/NV-Embed-v2', trust_remote_code=True)
model.max_seq_length = 32768
model.tokenizer.padding_side="right"

def add_eos(input_examples):
  input_examples = [input_example + model.tokenizer.eos_token for input_example in input_examples]
  return input_examples

# get the embeddings
batch_size = 2
query_embeddings = model.encode(add_eos(queries), batch_size=batch_size, prompt=query_prefix, normalize_embeddings=True)
passage_embeddings = model.encode(add_eos(passages), batch_size=batch_size, normalize_embeddings=True)

scores = (query_embeddings @ passage_embeddings.T) * 100
print(scores.tolist())
```

## License
This model should not be used for any commercial purpose. Refer the [license](https://spdx.org/licenses/CC-BY-NC-4.0) for the detailed terms.

For commercial purpose, we recommend you to use the models of [NeMo Retriever Microservices (NIMs)](https://build.nvidia.com/explore/retrieval).


## Correspondence to
Chankyu Lee (chankyul@nvidia.com), Wei Ping (wping@nvidia.com)


## Citation
If you find this code useful in your research, please consider citing:

```bibtex
@article{lee2024nv,
  title={NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models},
  author={Lee, Chankyu and Roy, Rajarshi and Xu, Mengyao and Raiman, Jonathan and Shoeybi, Mohammad and Catanzaro, Bryan and Ping, Wei},
  journal={arXiv preprint arXiv:2405.17428},
  year={2024}
}
```
```bibtex
@article{moreira2024nv,
  title={NV-Retriever: Improving text embedding models with effective hard-negative mining},
  author={Moreira, Gabriel de Souza P and Osmulski, Radek and Xu, Mengyao and Ak, Ronay and Schifferer, Benedikt and Oldridge, Even},
  journal={arXiv preprint arXiv:2407.15831},
  year={2024}
}
```


## Troubleshooting

#### 1. Instruction template for MTEB benchmarks

For MTEB sub-tasks for retrieval, STS, summarization, please use the instruction prefix template in [instructions.json](https://huggingface.co/nvidia/NV-Embed-v2/blob/main/instructions.json). For classification, clustering and reranking, please use the instructions provided in Table. 7 in [NV-Embed paper](https://arxiv.org/pdf/2405.17428).

#### 2. Required Packages

If you have trouble, try installing the python packages as below
```python
pip uninstall -y transformer-engine
pip install torch==2.2.0
pip install transformers==4.42.4
pip install flash-attn==2.2.0
pip install sentence-transformers==2.7.0
```

#### 3. How to enable Multi-GPU (Note, this is the case for HuggingFace Transformers)
```python
from transformers import AutoModel
from torch.nn import DataParallel

embedding_model = AutoModel.from_pretrained("nvidia/NV-Embed-v2")
for module_key, module in embedding_model._modules.items():
    embedding_model._modules[module_key] = DataParallel(module)
```

#### 4. Fixing "nvidia/NV-Embed-v2 is not the path to a directory containing a file named config.json"

Switch to your local model path，and open config.json and change the value of **"_name_or_path"** and replace it with your local model path.


#### 5. Access to model nvidia/NV-Embed-v2 is restricted. You must be authenticated to access it

Use your huggingface access [token](https://huggingface.co/settings/tokens) to execute *"huggingface-cli login"*.

#### 6. How to resolve slight mismatch in Sentence transformer results.

A slight mismatch in the Sentence Transformer implementation is caused by a discrepancy in the calculation of the instruction prefix length within the Sentence Transformer package.

To fix this issue, you need to build the Sentence Transformer package from source, making the necessary modification in this [line](https://github.com/UKPLab/sentence-transformers/blob/v2.7-release/sentence_transformers/SentenceTransformer.py#L353) as below.
```python
git clone https://github.com/UKPLab/sentence-transformers.git
cd sentence-transformers
git checkout v2.7-release
# Modify L353 in SentenceTransformer.py to **'extra_features["prompt_length"] = tokenized_prompt["input_ids"].shape[-1]'**.
pip install -e .
```
