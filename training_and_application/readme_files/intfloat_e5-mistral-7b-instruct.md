---
tags:
- mteb
- sentence-transformers
- transformers
model-index:
- name: e5-mistral-7b-instruct
  results:
  - task:
      type: STS
    dataset:
      type: C-MTEB/AFQMC
      name: MTEB AFQMC
      config: default
      split: validation
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 37.863226091673866
    - type: cos_sim_spearman
      value: 38.98733013335281
    - type: euclidean_pearson
      value: 37.51783380497874
    - type: euclidean_spearman
      value: 38.98733012753365
    - type: manhattan_pearson
      value: 37.26706888081721
    - type: manhattan_spearman
      value: 38.709750161903834
  - task:
      type: STS
    dataset:
      type: C-MTEB/ATEC
      name: MTEB ATEC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 43.33924583134623
    - type: cos_sim_spearman
      value: 42.84316155158754
    - type: euclidean_pearson
      value: 45.62709879515238
    - type: euclidean_spearman
      value: 42.843155921732404
    - type: manhattan_pearson
      value: 45.4786950991229
    - type: manhattan_spearman
      value: 42.657334751855984
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
      value: 78.68656716417911
    - type: ap
      value: 41.71522322900398
    - type: f1
      value: 72.37207703532552
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
      value: 74.04710920770879
    - type: ap
      value: 83.42622221864045
    - type: f1
      value: 72.14388257905772
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (en-ext)
      config: en-ext
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 77.93103448275862
    - type: ap
      value: 26.039284760509513
    - type: f1
      value: 64.81092954450712
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (ja)
      config: ja
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 77.21627408993577
    - type: ap
      value: 24.876490553983036
    - type: f1
      value: 63.8773359684989
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
      value: 95.90679999999999
    - type: ap
      value: 94.32357863164454
    - type: f1
      value: 95.90485634708557
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
      value: 55.786
    - type: f1
      value: 55.31211995815146
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
      value: 53.26
    - type: f1
      value: 52.156230111544986
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (es)
      config: es
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 50.33
    - type: f1
      value: 49.195023008878145
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (fr)
      config: fr
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 49.3
    - type: f1
      value: 48.434470184108
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (ja)
      config: ja
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 48.68599999999999
    - type: f1
      value: 47.62681775202072
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
      value: 46.238
    - type: f1
      value: 45.014030559653705
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
      value: 36.486000000000004
    - type: map_at_10
      value: 53.076
    - type: map_at_100
      value: 53.657999999999994
    - type: map_at_1000
      value: 53.659
    - type: map_at_3
      value: 48.234
    - type: map_at_5
      value: 51.121
    - type: mrr_at_1
      value: 37.269000000000005
    - type: mrr_at_10
      value: 53.335
    - type: mrr_at_100
      value: 53.916
    - type: mrr_at_1000
      value: 53.918
    - type: mrr_at_3
      value: 48.518
    - type: mrr_at_5
      value: 51.406
    - type: ndcg_at_1
      value: 36.486000000000004
    - type: ndcg_at_10
      value: 61.882000000000005
    - type: ndcg_at_100
      value: 64.165
    - type: ndcg_at_1000
      value: 64.203
    - type: ndcg_at_3
      value: 52.049
    - type: ndcg_at_5
      value: 57.199
    - type: precision_at_1
      value: 36.486000000000004
    - type: precision_at_10
      value: 8.982999999999999
    - type: precision_at_100
      value: 0.9939999999999999
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 21.029
    - type: precision_at_5
      value: 15.092
    - type: recall_at_1
      value: 36.486000000000004
    - type: recall_at_10
      value: 89.82900000000001
    - type: recall_at_100
      value: 99.36
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 63.087
    - type: recall_at_5
      value: 75.46199999999999
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
      value: 50.45119266859667
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
      value: 45.4958298992051
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
      value: 66.98177472838887
    - type: mrr
      value: 79.91854636591478
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
      value: 87.67086498650698
    - type: cos_sim_spearman
      value: 85.54773239564638
    - type: euclidean_pearson
      value: 86.48229161588425
    - type: euclidean_spearman
      value: 85.54773239564638
    - type: manhattan_pearson
      value: 86.67533327742343
    - type: manhattan_spearman
      value: 85.76099026691983
  - task:
      type: STS
    dataset:
      type: C-MTEB/BQ
      name: MTEB BQ
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 50.31998888922809
    - type: cos_sim_spearman
      value: 50.6369940530675
    - type: euclidean_pearson
      value: 50.055544636296055
    - type: euclidean_spearman
      value: 50.63699405154838
    - type: manhattan_pearson
      value: 50.00739378036807
    - type: manhattan_spearman
      value: 50.607237418676945
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
      value: 99.5615866388309
    - type: f1
      value: 99.49895615866389
    - type: precision
      value: 99.46764091858039
    - type: recall
      value: 99.5615866388309
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
      value: 99.19656614571869
    - type: f1
      value: 99.08650671362535
    - type: precision
      value: 99.0314769975787
    - type: recall
      value: 99.19656614571869
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
      value: 98.0256321440942
    - type: f1
      value: 97.83743216718624
    - type: precision
      value: 97.74390947927492
    - type: recall
      value: 98.0256321440942
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
      value: 99.26276987888363
    - type: f1
      value: 99.22766368264
    - type: precision
      value: 99.21011058451816
    - type: recall
      value: 99.26276987888363
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
      value: 88.22727272727272
    - type: f1
      value: 88.17411732496673
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
      value: 43.530637846246975
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
      value: 40.23505728593893
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/CLSClusteringP2P
      name: MTEB CLSClusteringP2P
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 44.419028279451275
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/CLSClusteringS2S
      name: MTEB CLSClusteringS2S
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 42.5820277929776
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/CMedQAv1-reranking
      name: MTEB CMedQAv1
      config: default
      split: test
      revision: None
    metrics:
    - type: map
      value: 77.67811726152972
    - type: mrr
      value: 80.99003968253969
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/CMedQAv2-reranking
      name: MTEB CMedQAv2
      config: default
      split: test
      revision: None
    metrics:
    - type: map
      value: 78.66055354534922
    - type: mrr
      value: 81.66119047619047
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
      value: 27.162333333333333
    - type: map_at_10
      value: 37.22291666666667
    - type: map_at_100
      value: 38.56733333333333
    - type: map_at_1000
      value: 38.684250000000006
    - type: map_at_3
      value: 34.22858333333333
    - type: map_at_5
      value: 35.852500000000006
    - type: mrr_at_1
      value: 32.459833333333336
    - type: mrr_at_10
      value: 41.65358333333333
    - type: mrr_at_100
      value: 42.566916666666664
    - type: mrr_at_1000
      value: 42.61766666666667
    - type: mrr_at_3
      value: 39.210499999999996
    - type: mrr_at_5
      value: 40.582166666666666
    - type: ndcg_at_1
      value: 32.459833333333336
    - type: ndcg_at_10
      value: 42.96758333333333
    - type: ndcg_at_100
      value: 48.5065
    - type: ndcg_at_1000
      value: 50.556583333333336
    - type: ndcg_at_3
      value: 38.004416666666664
    - type: ndcg_at_5
      value: 40.25916666666667
    - type: precision_at_1
      value: 32.459833333333336
    - type: precision_at_10
      value: 7.664583333333333
    - type: precision_at_100
      value: 1.2349999999999999
    - type: precision_at_1000
      value: 0.15966666666666668
    - type: precision_at_3
      value: 17.731166666666663
    - type: precision_at_5
      value: 12.575333333333335
    - type: recall_at_1
      value: 27.162333333333333
    - type: recall_at_10
      value: 55.44158333333334
    - type: recall_at_100
      value: 79.56966666666666
    - type: recall_at_1000
      value: 93.45224999999999
    - type: recall_at_3
      value: 41.433083333333336
    - type: recall_at_5
      value: 47.31108333333333
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
      value: 16.539
    - type: map_at_10
      value: 28.494999999999997
    - type: map_at_100
      value: 30.568
    - type: map_at_1000
      value: 30.741000000000003
    - type: map_at_3
      value: 23.846999999999998
    - type: map_at_5
      value: 26.275
    - type: mrr_at_1
      value: 37.394
    - type: mrr_at_10
      value: 50.068
    - type: mrr_at_100
      value: 50.727
    - type: mrr_at_1000
      value: 50.751000000000005
    - type: mrr_at_3
      value: 46.938
    - type: mrr_at_5
      value: 48.818
    - type: ndcg_at_1
      value: 37.394
    - type: ndcg_at_10
      value: 38.349
    - type: ndcg_at_100
      value: 45.512
    - type: ndcg_at_1000
      value: 48.321
    - type: ndcg_at_3
      value: 32.172
    - type: ndcg_at_5
      value: 34.265
    - type: precision_at_1
      value: 37.394
    - type: precision_at_10
      value: 11.927999999999999
    - type: precision_at_100
      value: 1.966
    - type: precision_at_1000
      value: 0.25
    - type: precision_at_3
      value: 24.126
    - type: precision_at_5
      value: 18.306
    - type: recall_at_1
      value: 16.539
    - type: recall_at_10
      value: 44.504
    - type: recall_at_100
      value: 68.605
    - type: recall_at_1000
      value: 84.1
    - type: recall_at_3
      value: 29.008
    - type: recall_at_5
      value: 35.58
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CmedqaRetrieval
      name: MTEB CmedqaRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 19.482
    - type: map_at_10
      value: 28.622999999999998
    - type: map_at_100
      value: 30.262
    - type: map_at_1000
      value: 30.432
    - type: map_at_3
      value: 25.647
    - type: map_at_5
      value: 27.128000000000004
    - type: mrr_at_1
      value: 30.408
    - type: mrr_at_10
      value: 37.188
    - type: mrr_at_100
      value: 38.196000000000005
    - type: mrr_at_1000
      value: 38.273
    - type: mrr_at_3
      value: 35.067
    - type: mrr_at_5
      value: 36.124
    - type: ndcg_at_1
      value: 30.408
    - type: ndcg_at_10
      value: 34.215
    - type: ndcg_at_100
      value: 41.349999999999994
    - type: ndcg_at_1000
      value: 44.689
    - type: ndcg_at_3
      value: 30.264999999999997
    - type: ndcg_at_5
      value: 31.572
    - type: precision_at_1
      value: 30.408
    - type: precision_at_10
      value: 7.6770000000000005
    - type: precision_at_100
      value: 1.352
    - type: precision_at_1000
      value: 0.178
    - type: precision_at_3
      value: 17.213
    - type: precision_at_5
      value: 12.198
    - type: recall_at_1
      value: 19.482
    - type: recall_at_10
      value: 42.368
    - type: recall_at_100
      value: 72.694
    - type: recall_at_1000
      value: 95.602
    - type: recall_at_3
      value: 30.101
    - type: recall_at_5
      value: 34.708
  - task:
      type: PairClassification
    dataset:
      type: C-MTEB/CMNLI
      name: MTEB Cmnli
      config: default
      split: validation
      revision: None
    metrics:
    - type: cos_sim_accuracy
      value: 71.16055321707758
    - type: cos_sim_ap
      value: 80.21073839711723
    - type: cos_sim_f1
      value: 72.9740932642487
    - type: cos_sim_precision
      value: 65.53136050623488
    - type: cos_sim_recall
      value: 82.3240589198036
    - type: dot_accuracy
      value: 71.16055321707758
    - type: dot_ap
      value: 80.212299264122
    - type: dot_f1
      value: 72.9740932642487
    - type: dot_precision
      value: 65.53136050623488
    - type: dot_recall
      value: 82.3240589198036
    - type: euclidean_accuracy
      value: 71.16055321707758
    - type: euclidean_ap
      value: 80.21076298680417
    - type: euclidean_f1
      value: 72.9740932642487
    - type: euclidean_precision
      value: 65.53136050623488
    - type: euclidean_recall
      value: 82.3240589198036
    - type: manhattan_accuracy
      value: 70.71557426337944
    - type: manhattan_ap
      value: 79.93448977199749
    - type: manhattan_f1
      value: 72.83962726826877
    - type: manhattan_precision
      value: 62.7407908077053
    - type: manhattan_recall
      value: 86.81318681318682
    - type: max_accuracy
      value: 71.16055321707758
    - type: max_ap
      value: 80.212299264122
    - type: max_f1
      value: 72.9740932642487
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CovidRetrieval
      name: MTEB CovidRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 60.643
    - type: map_at_10
      value: 69.011
    - type: map_at_100
      value: 69.533
    - type: map_at_1000
      value: 69.545
    - type: map_at_3
      value: 67.167
    - type: map_at_5
      value: 68.12700000000001
    - type: mrr_at_1
      value: 60.801
    - type: mrr_at_10
      value: 69.111
    - type: mrr_at_100
      value: 69.6
    - type: mrr_at_1000
      value: 69.611
    - type: mrr_at_3
      value: 67.229
    - type: mrr_at_5
      value: 68.214
    - type: ndcg_at_1
      value: 60.801
    - type: ndcg_at_10
      value: 73.128
    - type: ndcg_at_100
      value: 75.614
    - type: ndcg_at_1000
      value: 75.92
    - type: ndcg_at_3
      value: 69.261
    - type: ndcg_at_5
      value: 70.973
    - type: precision_at_1
      value: 60.801
    - type: precision_at_10
      value: 8.662
    - type: precision_at_100
      value: 0.9860000000000001
    - type: precision_at_1000
      value: 0.101
    - type: precision_at_3
      value: 25.149
    - type: precision_at_5
      value: 15.953999999999999
    - type: recall_at_1
      value: 60.643
    - type: recall_at_10
      value: 85.959
    - type: recall_at_100
      value: 97.576
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 75.184
    - type: recall_at_5
      value: 79.32000000000001
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
      value: 10.183
    - type: map_at_10
      value: 23.958
    - type: map_at_100
      value: 34.354
    - type: map_at_1000
      value: 36.442
    - type: map_at_3
      value: 16.345000000000002
    - type: map_at_5
      value: 19.647000000000002
    - type: mrr_at_1
      value: 74.25
    - type: mrr_at_10
      value: 80.976
    - type: mrr_at_100
      value: 81.256
    - type: mrr_at_1000
      value: 81.262
    - type: mrr_at_3
      value: 79.958
    - type: mrr_at_5
      value: 80.37100000000001
    - type: ndcg_at_1
      value: 62.0
    - type: ndcg_at_10
      value: 48.894999999999996
    - type: ndcg_at_100
      value: 53.867
    - type: ndcg_at_1000
      value: 61.304
    - type: ndcg_at_3
      value: 53.688
    - type: ndcg_at_5
      value: 50.900999999999996
    - type: precision_at_1
      value: 74.25
    - type: precision_at_10
      value: 39.525
    - type: precision_at_100
      value: 12.323
    - type: precision_at_1000
      value: 2.539
    - type: precision_at_3
      value: 57.49999999999999
    - type: precision_at_5
      value: 49.1
    - type: recall_at_1
      value: 10.183
    - type: recall_at_10
      value: 29.296
    - type: recall_at_100
      value: 60.394999999999996
    - type: recall_at_1000
      value: 83.12
    - type: recall_at_3
      value: 17.495
    - type: recall_at_5
      value: 22.235
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/DuRetrieval
      name: MTEB DuRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 26.613999999999997
    - type: map_at_10
      value: 79.77300000000001
    - type: map_at_100
      value: 82.71
    - type: map_at_1000
      value: 82.75
    - type: map_at_3
      value: 55.92700000000001
    - type: map_at_5
      value: 70.085
    - type: mrr_at_1
      value: 90.7
    - type: mrr_at_10
      value: 93.438
    - type: mrr_at_100
      value: 93.504
    - type: mrr_at_1000
      value: 93.50699999999999
    - type: mrr_at_3
      value: 93.125
    - type: mrr_at_5
      value: 93.34
    - type: ndcg_at_1
      value: 90.7
    - type: ndcg_at_10
      value: 87.023
    - type: ndcg_at_100
      value: 90.068
    - type: ndcg_at_1000
      value: 90.43299999999999
    - type: ndcg_at_3
      value: 86.339
    - type: ndcg_at_5
      value: 85.013
    - type: precision_at_1
      value: 90.7
    - type: precision_at_10
      value: 41.339999999999996
    - type: precision_at_100
      value: 4.806
    - type: precision_at_1000
      value: 0.48900000000000005
    - type: precision_at_3
      value: 76.983
    - type: precision_at_5
      value: 64.69
    - type: recall_at_1
      value: 26.613999999999997
    - type: recall_at_10
      value: 87.681
    - type: recall_at_100
      value: 97.44699999999999
    - type: recall_at_1000
      value: 99.348
    - type: recall_at_3
      value: 57.809999999999995
    - type: recall_at_5
      value: 74.258
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/EcomRetrieval
      name: MTEB EcomRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 30.9
    - type: map_at_10
      value: 40.467
    - type: map_at_100
      value: 41.423
    - type: map_at_1000
      value: 41.463
    - type: map_at_3
      value: 37.25
    - type: map_at_5
      value: 39.31
    - type: mrr_at_1
      value: 30.9
    - type: mrr_at_10
      value: 40.467
    - type: mrr_at_100
      value: 41.423
    - type: mrr_at_1000
      value: 41.463
    - type: mrr_at_3
      value: 37.25
    - type: mrr_at_5
      value: 39.31
    - type: ndcg_at_1
      value: 30.9
    - type: ndcg_at_10
      value: 45.957
    - type: ndcg_at_100
      value: 50.735
    - type: ndcg_at_1000
      value: 51.861999999999995
    - type: ndcg_at_3
      value: 39.437
    - type: ndcg_at_5
      value: 43.146
    - type: precision_at_1
      value: 30.9
    - type: precision_at_10
      value: 6.35
    - type: precision_at_100
      value: 0.861
    - type: precision_at_1000
      value: 0.095
    - type: precision_at_3
      value: 15.267
    - type: precision_at_5
      value: 10.96
    - type: recall_at_1
      value: 30.9
    - type: recall_at_10
      value: 63.5
    - type: recall_at_100
      value: 86.1
    - type: recall_at_1000
      value: 95.1
    - type: recall_at_3
      value: 45.800000000000004
    - type: recall_at_5
      value: 54.800000000000004
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
      value: 49.765
    - type: f1
      value: 45.93242203574485
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
      value: 75.138
    - type: map_at_10
      value: 84.21300000000001
    - type: map_at_100
      value: 84.43
    - type: map_at_1000
      value: 84.441
    - type: map_at_3
      value: 83.071
    - type: map_at_5
      value: 83.853
    - type: mrr_at_1
      value: 80.948
    - type: mrr_at_10
      value: 88.175
    - type: mrr_at_100
      value: 88.24
    - type: mrr_at_1000
      value: 88.241
    - type: mrr_at_3
      value: 87.516
    - type: mrr_at_5
      value: 87.997
    - type: ndcg_at_1
      value: 80.948
    - type: ndcg_at_10
      value: 87.84100000000001
    - type: ndcg_at_100
      value: 88.576
    - type: ndcg_at_1000
      value: 88.75699999999999
    - type: ndcg_at_3
      value: 86.176
    - type: ndcg_at_5
      value: 87.214
    - type: precision_at_1
      value: 80.948
    - type: precision_at_10
      value: 10.632
    - type: precision_at_100
      value: 1.123
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 33.193
    - type: precision_at_5
      value: 20.663
    - type: recall_at_1
      value: 75.138
    - type: recall_at_10
      value: 94.89699999999999
    - type: recall_at_100
      value: 97.751
    - type: recall_at_1000
      value: 98.833
    - type: recall_at_3
      value: 90.455
    - type: recall_at_5
      value: 93.085
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
      value: 29.45
    - type: map_at_10
      value: 48.596000000000004
    - type: map_at_100
      value: 50.70400000000001
    - type: map_at_1000
      value: 50.83800000000001
    - type: map_at_3
      value: 42.795
    - type: map_at_5
      value: 46.085
    - type: mrr_at_1
      value: 56.172999999999995
    - type: mrr_at_10
      value: 64.35300000000001
    - type: mrr_at_100
      value: 64.947
    - type: mrr_at_1000
      value: 64.967
    - type: mrr_at_3
      value: 62.653999999999996
    - type: mrr_at_5
      value: 63.534
    - type: ndcg_at_1
      value: 56.172999999999995
    - type: ndcg_at_10
      value: 56.593
    - type: ndcg_at_100
      value: 62.942
    - type: ndcg_at_1000
      value: 64.801
    - type: ndcg_at_3
      value: 53.024
    - type: ndcg_at_5
      value: 53.986999999999995
    - type: precision_at_1
      value: 56.172999999999995
    - type: precision_at_10
      value: 15.494
    - type: precision_at_100
      value: 2.222
    - type: precision_at_1000
      value: 0.254
    - type: precision_at_3
      value: 35.185
    - type: precision_at_5
      value: 25.556
    - type: recall_at_1
      value: 29.45
    - type: recall_at_10
      value: 62.882000000000005
    - type: recall_at_100
      value: 85.56099999999999
    - type: recall_at_1000
      value: 96.539
    - type: recall_at_3
      value: 47.911
    - type: recall_at_5
      value: 54.52
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
      value: 39.581
    - type: map_at_10
      value: 68.401
    - type: map_at_100
      value: 69.207
    - type: map_at_1000
      value: 69.25200000000001
    - type: map_at_3
      value: 64.689
    - type: map_at_5
      value: 67.158
    - type: mrr_at_1
      value: 79.163
    - type: mrr_at_10
      value: 85.22999999999999
    - type: mrr_at_100
      value: 85.386
    - type: mrr_at_1000
      value: 85.39099999999999
    - type: mrr_at_3
      value: 84.432
    - type: mrr_at_5
      value: 84.952
    - type: ndcg_at_1
      value: 79.163
    - type: ndcg_at_10
      value: 75.721
    - type: ndcg_at_100
      value: 78.411
    - type: ndcg_at_1000
      value: 79.23599999999999
    - type: ndcg_at_3
      value: 70.68799999999999
    - type: ndcg_at_5
      value: 73.694
    - type: precision_at_1
      value: 79.163
    - type: precision_at_10
      value: 16.134
    - type: precision_at_100
      value: 1.821
    - type: precision_at_1000
      value: 0.193
    - type: precision_at_3
      value: 46.446
    - type: precision_at_5
      value: 30.242
    - type: recall_at_1
      value: 39.581
    - type: recall_at_10
      value: 80.66799999999999
    - type: recall_at_100
      value: 91.033
    - type: recall_at_1000
      value: 96.408
    - type: recall_at_3
      value: 69.669
    - type: recall_at_5
      value: 75.604
  - task:
      type: Classification
    dataset:
      type: C-MTEB/IFlyTek-classification
      name: MTEB IFlyTek
      config: default
      split: validation
      revision: None
    metrics:
    - type: accuracy
      value: 45.04809542131589
    - type: f1
      value: 37.01181779071118
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
      value: 94.78120000000001
    - type: ap
      value: 92.52931921594387
    - type: f1
      value: 94.77902110732532
  - task:
      type: Classification
    dataset:
      type: C-MTEB/JDReview-classification
      name: MTEB JDReview
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 85.81613508442777
    - type: ap
      value: 52.430320593468394
    - type: f1
      value: 79.95467268178068
  - task:
      type: STS
    dataset:
      type: C-MTEB/LCQMC
      name: MTEB LCQMC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 71.05801751913393
    - type: cos_sim_spearman
      value: 75.47954644971965
    - type: euclidean_pearson
      value: 74.27472296759713
    - type: euclidean_spearman
      value: 75.47954201369866
    - type: manhattan_pearson
      value: 74.30508190186474
    - type: manhattan_spearman
      value: 75.51326518159436
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
      value: 24.21110921666315
    - type: mrr
      value: 22.863492063492064
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MMarcoRetrieval
      name: MTEB MMarcoRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 61.38400000000001
    - type: map_at_10
      value: 70.895
    - type: map_at_100
      value: 71.314
    - type: map_at_1000
      value: 71.331
    - type: map_at_3
      value: 69.016
    - type: map_at_5
      value: 70.179
    - type: mrr_at_1
      value: 63.481
    - type: mrr_at_10
      value: 71.543
    - type: mrr_at_100
      value: 71.91300000000001
    - type: mrr_at_1000
      value: 71.928
    - type: mrr_at_3
      value: 69.90899999999999
    - type: mrr_at_5
      value: 70.907
    - type: ndcg_at_1
      value: 63.481
    - type: ndcg_at_10
      value: 74.833
    - type: ndcg_at_100
      value: 76.705
    - type: ndcg_at_1000
      value: 77.13600000000001
    - type: ndcg_at_3
      value: 71.236
    - type: ndcg_at_5
      value: 73.199
    - type: precision_at_1
      value: 63.481
    - type: precision_at_10
      value: 9.179
    - type: precision_at_100
      value: 1.011
    - type: precision_at_1000
      value: 0.105
    - type: precision_at_3
      value: 27.044
    - type: precision_at_5
      value: 17.272000000000002
    - type: recall_at_1
      value: 61.38400000000001
    - type: recall_at_10
      value: 86.318
    - type: recall_at_100
      value: 94.786
    - type: recall_at_1000
      value: 98.14500000000001
    - type: recall_at_3
      value: 76.717
    - type: recall_at_5
      value: 81.416
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
      value: 23.363999999999997
    - type: map_at_10
      value: 36.022
    - type: map_at_100
      value: 37.229
    - type: map_at_1000
      value: 37.274
    - type: map_at_3
      value: 32.131
    - type: map_at_5
      value: 34.391
    - type: mrr_at_1
      value: 24.069
    - type: mrr_at_10
      value: 36.620000000000005
    - type: mrr_at_100
      value: 37.769999999999996
    - type: mrr_at_1000
      value: 37.809
    - type: mrr_at_3
      value: 32.846
    - type: mrr_at_5
      value: 35.02
    - type: ndcg_at_1
      value: 24.069
    - type: ndcg_at_10
      value: 43.056
    - type: ndcg_at_100
      value: 48.754
    - type: ndcg_at_1000
      value: 49.829
    - type: ndcg_at_3
      value: 35.167
    - type: ndcg_at_5
      value: 39.168
    - type: precision_at_1
      value: 24.069
    - type: precision_at_10
      value: 6.762
    - type: precision_at_100
      value: 0.96
    - type: precision_at_1000
      value: 0.105
    - type: precision_at_3
      value: 14.957
    - type: precision_at_5
      value: 11.023
    - type: recall_at_1
      value: 23.363999999999997
    - type: recall_at_10
      value: 64.696
    - type: recall_at_100
      value: 90.795
    - type: recall_at_1000
      value: 98.892
    - type: recall_at_3
      value: 43.247
    - type: recall_at_5
      value: 52.86300000000001
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
      value: 96.11947104423166
    - type: f1
      value: 95.89561841159332
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
      value: 92.97548605240912
    - type: f1
      value: 92.17133696717212
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (es)
      config: es
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 93.37224816544364
    - type: f1
      value: 93.19978829237863
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (fr)
      config: fr
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 91.28719072972127
    - type: f1
      value: 91.28448045979604
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (hi)
      config: hi
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 88.8131946934385
    - type: f1
      value: 88.27883019362747
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (th)
      config: th
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 85.52260397830018
    - type: f1
      value: 85.15528226728568
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
      value: 86.10807113543093
    - type: f1
      value: 70.88498219072167
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
      value: 77.77120315581854
    - type: f1
      value: 57.97153920153224
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (es)
      config: es
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 79.93995997331554
    - type: f1
      value: 58.839203810064866
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (fr)
      config: fr
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 77.801440651425
    - type: f1
      value: 58.68009647839332
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (hi)
      config: hi
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 72.90785227680172
    - type: f1
      value: 49.83760954655788
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (th)
      config: th
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 73.24050632911391
    - type: f1
      value: 52.0562553541082
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (af)
      config: af
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 66.47948890383321
    - type: f1
      value: 63.334877563135485
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (am)
      config: am
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 44.2871553463349
    - type: f1
      value: 43.17658050605427
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ar)
      config: ar
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 63.174176193678555
    - type: f1
      value: 59.236659587042425
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (az)
      config: az
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 64.226630800269
    - type: f1
      value: 60.951842696956184
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (bn)
      config: bn
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 64.94283792871555
    - type: f1
      value: 61.40057652844215
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (cy)
      config: cy
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 55.480833893745796
    - type: f1
      value: 52.5298332072816
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (da)
      config: da
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 72.52858103564223
    - type: f1
      value: 69.3770851919204
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
      value: 74.09213180901143
    - type: f1
      value: 71.13518469365879
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (el)
      config: el
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 68.31203765971756
    - type: f1
      value: 66.05906970865144
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
      value: 80.57162071284465
    - type: f1
      value: 77.7866172598823
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (es)
      config: es
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 75.09414929388029
    - type: f1
      value: 72.5712594833695
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (fa)
      config: fa
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 72.20914593140553
    - type: f1
      value: 68.90619124909186
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (fi)
      config: fi
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 68.74243443174176
    - type: f1
      value: 64.72743141749955
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (fr)
      config: fr
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 75.11096166778749
    - type: f1
      value: 72.61849933064694
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (he)
      config: he
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 66.22394082044384
    - type: f1
      value: 62.43648797607235
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (hi)
      config: hi
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 69.44855413584399
    - type: f1
      value: 66.56851670913659
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (hu)
      config: hu
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 69.4149293880296
    - type: f1
      value: 66.12960877904776
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (hy)
      config: hy
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 56.916610625420304
    - type: f1
      value: 54.02534600927991
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (id)
      config: id
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 72.71351714862138
    - type: f1
      value: 69.70227985126316
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (is)
      config: is
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 59.91257565568257
    - type: f1
      value: 57.06811572144974
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (it)
      config: it
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 75.25218560860793
    - type: f1
      value: 72.48057563104247
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ja)
      config: ja
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 76.35507733691998
    - type: f1
      value: 73.03024649541128
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (jv)
      config: jv
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 57.918628110289184
    - type: f1
      value: 54.75590124456177
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ka)
      config: ka
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 52.548755884330866
    - type: f1
      value: 51.5356975360209
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (km)
      config: km
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 46.44922663080027
    - type: f1
      value: 44.561114416830975
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (kn)
      config: kn
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 53.95763281775386
    - type: f1
      value: 50.68367245122476
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ko)
      config: ko
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 74.20645595158035
    - type: f1
      value: 71.78450093258185
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (lv)
      config: lv
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 59.226630800269
    - type: f1
      value: 57.53988988993337
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ml)
      config: ml
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 51.44922663080027
    - type: f1
      value: 48.58809018065056
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (mn)
      config: mn
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 51.3752521856086
    - type: f1
      value: 49.91373941436425
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ms)
      config: ms
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 69.85205110961668
    - type: f1
      value: 67.05660019588582
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (my)
      config: my
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 49.1492938802959
    - type: f1
      value: 46.717578025393195
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (nb)
      config: nb
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 70.93140551445865
    - type: f1
      value: 67.45406609372205
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (nl)
      config: nl
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 74.82851378614662
    - type: f1
      value: 71.15951964393868
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (pl)
      config: pl
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 74.84868863483524
    - type: f1
      value: 71.76056802364877
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (pt)
      config: pt
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 75.27236045729657
    - type: f1
      value: 72.48733090101163
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ro)
      config: ro
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 69.63012777404168
    - type: f1
      value: 66.56444015346203
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ru)
      config: ru
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 76.62743779421655
    - type: f1
      value: 73.82720656992142
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (sl)
      config: sl
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 67.15198386012105
    - type: f1
      value: 64.41418309797744
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (sq)
      config: sq
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 58.8399462004035
    - type: f1
      value: 56.050989519693886
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (sv)
      config: sv
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 73.86684599865501
    - type: f1
      value: 70.80682480844303
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (sw)
      config: sw
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 57.36718224613316
    - type: f1
      value: 54.998746471013774
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ta)
      config: ta
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 53.150638870208475
    - type: f1
      value: 49.79179342620099
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (te)
      config: te
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 51.50638870208473
    - type: f1
      value: 49.778960742003555
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (th)
      config: th
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 66.906523201076
    - type: f1
      value: 66.75784022138245
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (tl)
      config: tl
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 68.73234700739744
    - type: f1
      value: 65.75016141148413
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (tr)
      config: tr
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 72.06792199058508
    - type: f1
      value: 67.90334782594083
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ur)
      config: ur
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 62.09145931405515
    - type: f1
      value: 58.88703095210731
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (vi)
      config: vi
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 71.17014122394083
    - type: f1
      value: 68.43676277921544
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
      value: 74.99327505043712
    - type: f1
      value: 72.26813373392943
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (zh-TW)
      config: zh-TW
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 71.13987895090787
    - type: f1
      value: 70.29309514467575
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (af)
      config: af
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 73.37256220578345
    - type: f1
      value: 72.56456170538992
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (am)
      config: am
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 47.205783456624076
    - type: f1
      value: 45.905999859074434
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ar)
      config: ar
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 69.8352387357095
    - type: f1
      value: 69.43553987525273
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (az)
      config: az
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 67.00403496973773
    - type: f1
      value: 65.97477215779143
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (bn)
      config: bn
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 68.04976462676531
    - type: f1
      value: 67.24581993778398
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (cy)
      config: cy
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 61.882985877605925
    - type: f1
      value: 59.995293199988794
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (da)
      config: da
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 76.75857431069267
    - type: f1
      value: 76.52031675299841
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
      value: 79.03496973772697
    - type: f1
      value: 79.25548063175344
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (el)
      config: el
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 72.96570275722931
    - type: f1
      value: 72.19110435289122
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
      value: 82.38735709482178
    - type: f1
      value: 82.34495627619785
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (es)
      config: es
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 78.83994620040352
    - type: f1
      value: 78.91526355393667
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (fa)
      config: fa
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 76.7350369872226
    - type: f1
      value: 75.919437344927
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (fi)
      config: fi
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 71.21721587088096
    - type: f1
      value: 70.82973286243262
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (fr)
      config: fr
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 78.59784801613988
    - type: f1
      value: 78.47383161087423
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (he)
      config: he
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 69.64021519838602
    - type: f1
      value: 68.45118053027653
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (hi)
      config: hi
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 73.51042367182245
    - type: f1
      value: 72.90013022879003
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (hu)
      config: hu
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 74.0551445864156
    - type: f1
      value: 73.45871761713292
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (hy)
      config: hy
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 59.54606590450571
    - type: f1
      value: 57.72711794953869
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (id)
      config: id
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 77.40753194351042
    - type: f1
      value: 76.8157455506521
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (is)
      config: is
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 66.58372562205783
    - type: f1
      value: 65.2654868709758
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (it)
      config: it
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 78.39273705447208
    - type: f1
      value: 78.3592956594837
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ja)
      config: ja
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 79.62004034969739
    - type: f1
      value: 79.78673754501855
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (jv)
      config: jv
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 64.29051782111634
    - type: f1
      value: 63.12502587609454
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ka)
      config: ka
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 57.51849361129791
    - type: f1
      value: 56.32320906403241
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (km)
      config: km
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 52.41761936785474
    - type: f1
      value: 49.113762010098306
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (kn)
      config: kn
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 58.547410894418284
    - type: f1
      value: 56.87580674198118
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ko)
      config: ko
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 78.89038332212507
    - type: f1
      value: 79.09210140529848
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (lv)
      config: lv
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 63.503698722259585
    - type: f1
      value: 61.45718858568352
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ml)
      config: ml
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 54.02824478816408
    - type: f1
      value: 52.732738981386504
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (mn)
      config: mn
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 54.23671822461331
    - type: f1
      value: 52.688080372545286
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ms)
      config: ms
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 75.5312710154674
    - type: f1
      value: 74.59368478550698
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (my)
      config: my
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 52.192333557498316
    - type: f1
      value: 50.18302290152229
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (nb)
      config: nb
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 75.6960322797579
    - type: f1
      value: 75.25331182714856
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (nl)
      config: nl
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 78.47679892400808
    - type: f1
      value: 78.24044732352424
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (pl)
      config: pl
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 77.36718224613315
    - type: f1
      value: 77.2714452985389
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (pt)
      config: pt
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 77.96234028244788
    - type: f1
      value: 78.21282127011372
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ro)
      config: ro
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 73.19435104236717
    - type: f1
      value: 73.1963711292812
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ru)
      config: ru
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 80.52118359112306
    - type: f1
      value: 80.4179964390288
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (sl)
      config: sl
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 73.65837256220577
    - type: f1
      value: 73.07156989634905
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (sq)
      config: sq
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 64.02824478816409
    - type: f1
      value: 62.972399027713664
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (sv)
      config: sv
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 78.87020847343645
    - type: f1
      value: 78.224240866849
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (sw)
      config: sw
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 64.6570275722932
    - type: f1
      value: 63.274871811412545
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ta)
      config: ta
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 57.760591795561524
    - type: f1
      value: 56.73711528075771
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (te)
      config: te
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 57.26967047747142
    - type: f1
      value: 55.74735330863165
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (th)
      config: th
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 72.46133154001345
    - type: f1
      value: 71.9644168952811
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (tl)
      config: tl
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 73.70880968392737
    - type: f1
      value: 73.61543141070884
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (tr)
      config: tr
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 75.0437121721587
    - type: f1
      value: 74.83359868879921
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ur)
      config: ur
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 67.05110961667788
    - type: f1
      value: 66.25869819274315
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (vi)
      config: vi
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 75.52118359112306
    - type: f1
      value: 75.92098546052303
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
      value: 79.92938802958977
    - type: f1
      value: 79.79833572573796
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (zh-TW)
      config: zh-TW
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 76.86617350369872
    - type: f1
      value: 77.42645654909516
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MedicalRetrieval
      name: MTEB MedicalRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 44.6
    - type: map_at_10
      value: 50.019000000000005
    - type: map_at_100
      value: 50.611
    - type: map_at_1000
      value: 50.67
    - type: map_at_3
      value: 48.699999999999996
    - type: map_at_5
      value: 49.455
    - type: mrr_at_1
      value: 44.800000000000004
    - type: mrr_at_10
      value: 50.119
    - type: mrr_at_100
      value: 50.711
    - type: mrr_at_1000
      value: 50.77
    - type: mrr_at_3
      value: 48.8
    - type: mrr_at_5
      value: 49.555
    - type: ndcg_at_1
      value: 44.6
    - type: ndcg_at_10
      value: 52.754
    - type: ndcg_at_100
      value: 55.935
    - type: ndcg_at_1000
      value: 57.607
    - type: ndcg_at_3
      value: 50.012
    - type: ndcg_at_5
      value: 51.393
    - type: precision_at_1
      value: 44.6
    - type: precision_at_10
      value: 6.140000000000001
    - type: precision_at_100
      value: 0.77
    - type: precision_at_1000
      value: 0.09
    - type: precision_at_3
      value: 17.933
    - type: precision_at_5
      value: 11.44
    - type: recall_at_1
      value: 44.6
    - type: recall_at_10
      value: 61.4
    - type: recall_at_100
      value: 77.0
    - type: recall_at_1000
      value: 90.4
    - type: recall_at_3
      value: 53.800000000000004
    - type: recall_at_5
      value: 57.199999999999996
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
      value: 38.192667527616315
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
      value: 37.44738902946689
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
      value: 32.59661273103955
    - type: mrr
      value: 33.82024242497473
  - task:
      type: Classification
    dataset:
      type: C-MTEB/MultilingualSentiment-classification
      name: MTEB MultilingualSentiment
      config: default
      split: validation
      revision: None
    metrics:
    - type: accuracy
      value: 73.31333333333335
    - type: f1
      value: 73.0873466527602
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
      value: 5.471
    - type: map_at_10
      value: 14.142
    - type: map_at_100
      value: 18.179000000000002
    - type: map_at_1000
      value: 19.772000000000002
    - type: map_at_3
      value: 9.716
    - type: map_at_5
      value: 11.763
    - type: mrr_at_1
      value: 51.393
    - type: mrr_at_10
      value: 58.814
    - type: mrr_at_100
      value: 59.330000000000005
    - type: mrr_at_1000
      value: 59.35
    - type: mrr_at_3
      value: 56.398
    - type: mrr_at_5
      value: 58.038999999999994
    - type: ndcg_at_1
      value: 49.69
    - type: ndcg_at_10
      value: 38.615
    - type: ndcg_at_100
      value: 35.268
    - type: ndcg_at_1000
      value: 43.745
    - type: ndcg_at_3
      value: 43.187
    - type: ndcg_at_5
      value: 41.528999999999996
    - type: precision_at_1
      value: 51.083999999999996
    - type: precision_at_10
      value: 29.474
    - type: precision_at_100
      value: 9.167
    - type: precision_at_1000
      value: 2.2089999999999996
    - type: precision_at_3
      value: 40.351
    - type: precision_at_5
      value: 36.285000000000004
    - type: recall_at_1
      value: 5.471
    - type: recall_at_10
      value: 19.242
    - type: recall_at_100
      value: 37.14
    - type: recall_at_1000
      value: 68.35900000000001
    - type: recall_at_3
      value: 10.896
    - type: recall_at_5
      value: 14.75
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
      value: 39.499
    - type: map_at_10
      value: 55.862
    - type: map_at_100
      value: 56.667
    - type: map_at_1000
      value: 56.684999999999995
    - type: map_at_3
      value: 51.534
    - type: map_at_5
      value: 54.2
    - type: mrr_at_1
      value: 44.351
    - type: mrr_at_10
      value: 58.567
    - type: mrr_at_100
      value: 59.099000000000004
    - type: mrr_at_1000
      value: 59.109
    - type: mrr_at_3
      value: 55.218999999999994
    - type: mrr_at_5
      value: 57.391999999999996
    - type: ndcg_at_1
      value: 44.322
    - type: ndcg_at_10
      value: 63.535
    - type: ndcg_at_100
      value: 66.654
    - type: ndcg_at_1000
      value: 66.991
    - type: ndcg_at_3
      value: 55.701
    - type: ndcg_at_5
      value: 60.06700000000001
    - type: precision_at_1
      value: 44.322
    - type: precision_at_10
      value: 10.026
    - type: precision_at_100
      value: 1.18
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 24.865000000000002
    - type: precision_at_5
      value: 17.48
    - type: recall_at_1
      value: 39.499
    - type: recall_at_10
      value: 84.053
    - type: recall_at_100
      value: 97.11
    - type: recall_at_1000
      value: 99.493
    - type: recall_at_3
      value: 64.091
    - type: recall_at_5
      value: 74.063
  - task:
      type: PairClassification
    dataset:
      type: C-MTEB/OCNLI
      name: MTEB Ocnli
      config: default
      split: validation
      revision: None
    metrics:
    - type: cos_sim_accuracy
      value: 61.18029236599891
    - type: cos_sim_ap
      value: 64.18398769398412
    - type: cos_sim_f1
      value: 67.96347757046446
    - type: cos_sim_precision
      value: 54.4529262086514
    - type: cos_sim_recall
      value: 90.3907074973601
    - type: dot_accuracy
      value: 61.18029236599891
    - type: dot_ap
      value: 64.18393484706077
    - type: dot_f1
      value: 67.96347757046446
    - type: dot_precision
      value: 54.4529262086514
    - type: dot_recall
      value: 90.3907074973601
    - type: euclidean_accuracy
      value: 61.18029236599891
    - type: euclidean_ap
      value: 64.18395024821486
    - type: euclidean_f1
      value: 67.96347757046446
    - type: euclidean_precision
      value: 54.4529262086514
    - type: euclidean_recall
      value: 90.3907074973601
    - type: manhattan_accuracy
      value: 61.451001624255554
    - type: manhattan_ap
      value: 64.38232708763513
    - type: manhattan_f1
      value: 68.05860805860804
    - type: manhattan_precision
      value: 52.10319685922602
    - type: manhattan_recall
      value: 98.09926082365365
    - type: max_accuracy
      value: 61.451001624255554
    - type: max_ap
      value: 64.38232708763513
    - type: max_f1
      value: 68.05860805860804
  - task:
      type: Classification
    dataset:
      type: C-MTEB/OnlineShopping-classification
      name: MTEB OnlineShopping
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 92.19000000000001
    - type: ap
      value: 89.73918431886767
    - type: f1
      value: 92.17175032574507
  - task:
      type: STS
    dataset:
      type: C-MTEB/PAWSX
      name: MTEB PAWSX
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 15.079320253752224
    - type: cos_sim_spearman
      value: 16.813772504404263
    - type: euclidean_pearson
      value: 19.476541162041762
    - type: euclidean_spearman
      value: 16.813772498098782
    - type: manhattan_pearson
      value: 19.497429832915277
    - type: manhattan_spearman
      value: 16.869600674180607
  - task:
      type: STS
    dataset:
      type: C-MTEB/QBQTC
      name: MTEB QBQTC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 30.36139599797913
    - type: cos_sim_spearman
      value: 31.80296402851347
    - type: euclidean_pearson
      value: 30.10387888252793
    - type: euclidean_spearman
      value: 31.80297780103808
    - type: manhattan_pearson
      value: 30.86720382849436
    - type: manhattan_spearman
      value: 32.70491131366606
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
      value: 71.911
    - type: map_at_10
      value: 86.087
    - type: map_at_100
      value: 86.701
    - type: map_at_1000
      value: 86.715
    - type: map_at_3
      value: 83.231
    - type: map_at_5
      value: 85.051
    - type: mrr_at_1
      value: 82.75
    - type: mrr_at_10
      value: 88.759
    - type: mrr_at_100
      value: 88.844
    - type: mrr_at_1000
      value: 88.844
    - type: mrr_at_3
      value: 87.935
    - type: mrr_at_5
      value: 88.504
    - type: ndcg_at_1
      value: 82.75
    - type: ndcg_at_10
      value: 89.605
    - type: ndcg_at_100
      value: 90.664
    - type: ndcg_at_1000
      value: 90.733
    - type: ndcg_at_3
      value: 87.03
    - type: ndcg_at_5
      value: 88.473
    - type: precision_at_1
      value: 82.75
    - type: precision_at_10
      value: 13.575000000000001
    - type: precision_at_100
      value: 1.539
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 38.153
    - type: precision_at_5
      value: 25.008000000000003
    - type: recall_at_1
      value: 71.911
    - type: recall_at_10
      value: 96.261
    - type: recall_at_100
      value: 99.72800000000001
    - type: recall_at_1000
      value: 99.993
    - type: recall_at_3
      value: 88.762
    - type: recall_at_5
      value: 92.949
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
      value: 57.711581165572376
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
      value: 66.48938885750297
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
      value: 3.7379999999999995
    - type: map_at_10
      value: 9.261
    - type: map_at_100
      value: 11.001
    - type: map_at_1000
      value: 11.262
    - type: map_at_3
      value: 6.816
    - type: map_at_5
      value: 8.0
    - type: mrr_at_1
      value: 18.4
    - type: mrr_at_10
      value: 28.755999999999997
    - type: mrr_at_100
      value: 29.892000000000003
    - type: mrr_at_1000
      value: 29.961
    - type: mrr_at_3
      value: 25.467000000000002
    - type: mrr_at_5
      value: 27.332
    - type: ndcg_at_1
      value: 18.4
    - type: ndcg_at_10
      value: 16.296
    - type: ndcg_at_100
      value: 23.52
    - type: ndcg_at_1000
      value: 28.504
    - type: ndcg_at_3
      value: 15.485
    - type: ndcg_at_5
      value: 13.471
    - type: precision_at_1
      value: 18.4
    - type: precision_at_10
      value: 8.469999999999999
    - type: precision_at_100
      value: 1.8950000000000002
    - type: precision_at_1000
      value: 0.309
    - type: precision_at_3
      value: 14.6
    - type: precision_at_5
      value: 11.84
    - type: recall_at_1
      value: 3.7379999999999995
    - type: recall_at_10
      value: 17.185
    - type: recall_at_100
      value: 38.397
    - type: recall_at_1000
      value: 62.798
    - type: recall_at_3
      value: 8.896999999999998
    - type: recall_at_5
      value: 12.021999999999998
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
      value: 86.43977757480083
    - type: cos_sim_spearman
      value: 82.64182475199533
    - type: euclidean_pearson
      value: 83.71756009999591
    - type: euclidean_spearman
      value: 82.64182331395057
    - type: manhattan_pearson
      value: 83.8028936913025
    - type: manhattan_spearman
      value: 82.71024597804252
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
      value: 86.85653060698912
    - type: cos_sim_spearman
      value: 79.65598885228324
    - type: euclidean_pearson
      value: 83.1205137628455
    - type: euclidean_spearman
      value: 79.65629387709038
    - type: manhattan_pearson
      value: 83.71108853545837
    - type: manhattan_spearman
      value: 80.25617619716708
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
      value: 88.22921688565664
    - type: cos_sim_spearman
      value: 88.42662103041957
    - type: euclidean_pearson
      value: 87.91679798473325
    - type: euclidean_spearman
      value: 88.42662103041957
    - type: manhattan_pearson
      value: 88.16927537961303
    - type: manhattan_spearman
      value: 88.81581680062541
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
      value: 86.77261424554293
    - type: cos_sim_spearman
      value: 84.53930146434155
    - type: euclidean_pearson
      value: 85.67420491389697
    - type: euclidean_spearman
      value: 84.53929771783851
    - type: manhattan_pearson
      value: 85.74306784515618
    - type: manhattan_spearman
      value: 84.7399304675314
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
      value: 89.86138395166455
    - type: cos_sim_spearman
      value: 90.42577823022054
    - type: euclidean_pearson
      value: 89.8787763797515
    - type: euclidean_spearman
      value: 90.42577823022054
    - type: manhattan_pearson
      value: 89.9592937492158
    - type: manhattan_spearman
      value: 90.63535505335524
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
      value: 86.5176674585941
    - type: cos_sim_spearman
      value: 87.6842917085397
    - type: euclidean_pearson
      value: 86.70213081520711
    - type: euclidean_spearman
      value: 87.6842917085397
    - type: manhattan_pearson
      value: 86.83702628983627
    - type: manhattan_spearman
      value: 87.87791000374443
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (ko-ko)
      config: ko-ko
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 83.86395454805867
    - type: cos_sim_spearman
      value: 83.69454595252267
    - type: euclidean_pearson
      value: 83.04743892608313
    - type: euclidean_spearman
      value: 83.69454026433006
    - type: manhattan_pearson
      value: 83.4032095553322
    - type: manhattan_spearman
      value: 84.11527379013802
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (ar-ar)
      config: ar-ar
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 81.80249894729546
    - type: cos_sim_spearman
      value: 81.87004960533409
    - type: euclidean_pearson
      value: 80.0392760044179
    - type: euclidean_spearman
      value: 81.87004960533409
    - type: manhattan_pearson
      value: 80.38096542355912
    - type: manhattan_spearman
      value: 82.40774679630341
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-ar)
      config: en-ar
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 77.6158201787172
    - type: cos_sim_spearman
      value: 77.934651044009
    - type: euclidean_pearson
      value: 77.7874683895269
    - type: euclidean_spearman
      value: 77.934651044009
    - type: manhattan_pearson
      value: 78.36151849193052
    - type: manhattan_spearman
      value: 78.52439586349938
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
      value: 87.04363311392207
    - type: cos_sim_spearman
      value: 87.30483659369973
    - type: euclidean_pearson
      value: 87.62634489502616
    - type: euclidean_spearman
      value: 87.30483659369973
    - type: manhattan_pearson
      value: 88.02340837141445
    - type: manhattan_spearman
      value: 87.55012003294
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
      value: 91.69172851958248
    - type: cos_sim_spearman
      value: 91.7546879482416
    - type: euclidean_pearson
      value: 91.84843039183963
    - type: euclidean_spearman
      value: 91.7546879482416
    - type: manhattan_pearson
      value: 91.72325753804357
    - type: manhattan_spearman
      value: 91.55330259513397
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-tr)
      config: en-tr
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 73.95572901084864
    - type: cos_sim_spearman
      value: 72.56217821552626
    - type: euclidean_pearson
      value: 74.24242980323574
    - type: euclidean_spearman
      value: 72.56217821552626
    - type: manhattan_pearson
      value: 74.57473362519922
    - type: manhattan_spearman
      value: 72.76048826648497
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (es-en)
      config: es-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 86.93329396008296
    - type: cos_sim_spearman
      value: 88.2406635486219
    - type: euclidean_pearson
      value: 87.49687343908533
    - type: euclidean_spearman
      value: 88.2406635486219
    - type: manhattan_pearson
      value: 88.14088309231084
    - type: manhattan_spearman
      value: 88.93314020908534
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (es-es)
      config: es-es
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 88.70124451546057
    - type: cos_sim_spearman
      value: 87.45988160052252
    - type: euclidean_pearson
      value: 88.44395505247728
    - type: euclidean_spearman
      value: 87.45988160052252
    - type: manhattan_pearson
      value: 88.69269783495425
    - type: manhattan_spearman
      value: 87.65383425621
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (fr-en)
      config: fr-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 87.64109149761346
    - type: cos_sim_spearman
      value: 88.06459637689733
    - type: euclidean_pearson
      value: 88.02313315797703
    - type: euclidean_spearman
      value: 88.06459637689733
    - type: manhattan_pearson
      value: 88.28328539133253
    - type: manhattan_spearman
      value: 88.06605708379142
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (it-en)
      config: it-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 88.9040028177525
    - type: cos_sim_spearman
      value: 89.68152202933464
    - type: euclidean_pearson
      value: 89.23684469601253
    - type: euclidean_spearman
      value: 89.68152202933464
    - type: manhattan_pearson
      value: 89.59504307277454
    - type: manhattan_spearman
      value: 89.88060100313582
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (nl-en)
      config: nl-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 87.69891585325125
    - type: cos_sim_spearman
      value: 88.25252785071736
    - type: euclidean_pearson
      value: 87.99932873748662
    - type: euclidean_spearman
      value: 88.25252785071736
    - type: manhattan_pearson
      value: 88.26959683009446
    - type: manhattan_spearman
      value: 88.32583227300715
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
      value: 67.53235909794135
    - type: cos_sim_spearman
      value: 66.97521740529574
    - type: euclidean_pearson
      value: 68.19502223613912
    - type: euclidean_spearman
      value: 66.97521740529574
    - type: manhattan_pearson
      value: 68.39070714774539
    - type: manhattan_spearman
      value: 67.1072812364868
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
      value: 43.715742021204775
    - type: cos_sim_spearman
      value: 49.12255971271453
    - type: euclidean_pearson
      value: 40.76848562610837
    - type: euclidean_spearman
      value: 49.12255971271453
    - type: manhattan_pearson
      value: 40.92204625614112
    - type: manhattan_spearman
      value: 49.23333793661129
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (es)
      config: es
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 63.35268345563588
    - type: cos_sim_spearman
      value: 66.99661626042061
    - type: euclidean_pearson
      value: 65.85589122857066
    - type: euclidean_spearman
      value: 66.99661626042061
    - type: manhattan_pearson
      value: 66.78454301512294
    - type: manhattan_spearman
      value: 67.17570330149233
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (pl)
      config: pl
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 33.36599908204445
    - type: cos_sim_spearman
      value: 39.20768331939503
    - type: euclidean_pearson
      value: 22.16066769530468
    - type: euclidean_spearman
      value: 39.20768331939503
    - type: manhattan_pearson
      value: 22.386053195546022
    - type: manhattan_spearman
      value: 39.70172817465986
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (tr)
      config: tr
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 63.06813956986753
    - type: cos_sim_spearman
      value: 68.72065117995668
    - type: euclidean_pearson
      value: 66.97373456344194
    - type: euclidean_spearman
      value: 68.72065117995668
    - type: manhattan_pearson
      value: 67.34907265771595
    - type: manhattan_spearman
      value: 68.73705769957843
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (ar)
      config: ar
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 47.17664865207108
    - type: cos_sim_spearman
      value: 54.115568323148864
    - type: euclidean_pearson
      value: 48.56418162879182
    - type: euclidean_spearman
      value: 54.115568323148864
    - type: manhattan_pearson
      value: 48.85951643453165
    - type: manhattan_spearman
      value: 54.13599784169052
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (ru)
      config: ru
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 55.87514136275987
    - type: cos_sim_spearman
      value: 60.82923573674973
    - type: euclidean_pearson
      value: 53.724183308215615
    - type: euclidean_spearman
      value: 60.82923573674973
    - type: manhattan_pearson
      value: 53.954305573102445
    - type: manhattan_spearman
      value: 60.957483900644526
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (zh)
      config: zh
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 59.55001413648593
    - type: cos_sim_spearman
      value: 63.395777040381276
    - type: euclidean_pearson
      value: 59.869972550293305
    - type: euclidean_spearman
      value: 63.395777040381276
    - type: manhattan_pearson
      value: 61.16195496847885
    - type: manhattan_spearman
      value: 63.41968682525581
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (fr)
      config: fr
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 79.13334972675852
    - type: cos_sim_spearman
      value: 79.86263136371802
    - type: euclidean_pearson
      value: 78.2433603592541
    - type: euclidean_spearman
      value: 79.86263136371802
    - type: manhattan_pearson
      value: 78.87337106318412
    - type: manhattan_spearman
      value: 80.31230584758441
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
      value: 63.559700748242356
    - type: cos_sim_spearman
      value: 60.92342109509558
    - type: euclidean_pearson
      value: 66.07256437521119
    - type: euclidean_spearman
      value: 60.92342109509558
    - type: manhattan_pearson
      value: 67.72769744612663
    - type: manhattan_spearman
      value: 59.64714507774168
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (es-en)
      config: es-en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 73.93491616145891
    - type: cos_sim_spearman
      value: 75.84242594400156
    - type: euclidean_pearson
      value: 74.87279745626121
    - type: euclidean_spearman
      value: 75.84242594400156
    - type: manhattan_pearson
      value: 76.47764144677505
    - type: manhattan_spearman
      value: 77.08411157845183
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (it)
      config: it
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 72.75624124540954
    - type: cos_sim_spearman
      value: 75.8667941654703
    - type: euclidean_pearson
      value: 73.74314588451925
    - type: euclidean_spearman
      value: 75.8667941654703
    - type: manhattan_pearson
      value: 73.99641425871518
    - type: manhattan_spearman
      value: 76.1982840205817
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (pl-en)
      config: pl-en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 75.20898141298767
    - type: cos_sim_spearman
      value: 73.18060375331436
    - type: euclidean_pearson
      value: 75.44489280944619
    - type: euclidean_spearman
      value: 73.18060375331436
    - type: manhattan_pearson
      value: 75.65451039552286
    - type: manhattan_spearman
      value: 72.97744006123156
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (zh-en)
      config: zh-en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 72.04278252247816
    - type: cos_sim_spearman
      value: 71.8846446821539
    - type: euclidean_pearson
      value: 73.16043307050612
    - type: euclidean_spearman
      value: 71.8846446821539
    - type: manhattan_pearson
      value: 74.76905116839777
    - type: manhattan_spearman
      value: 72.66237093518471
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (es-it)
      config: es-it
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 71.71033173838558
    - type: cos_sim_spearman
      value: 75.043122881885
    - type: euclidean_pearson
      value: 72.77579680345087
    - type: euclidean_spearman
      value: 75.043122881885
    - type: manhattan_pearson
      value: 72.99901534854922
    - type: manhattan_spearman
      value: 75.15418335015957
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de-fr)
      config: de-fr
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 55.75733447190482
    - type: cos_sim_spearman
      value: 61.38968334176681
    - type: euclidean_pearson
      value: 55.479231520643744
    - type: euclidean_spearman
      value: 61.38968334176681
    - type: manhattan_pearson
      value: 56.05230571465244
    - type: manhattan_spearman
      value: 62.69383054007398
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de-pl)
      config: de-pl
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 41.72244325050302
    - type: cos_sim_spearman
      value: 54.47476909084119
    - type: euclidean_pearson
      value: 43.94629756436873
    - type: euclidean_spearman
      value: 54.47476909084119
    - type: manhattan_pearson
      value: 46.36533046394657
    - type: manhattan_spearman
      value: 54.87509243633636
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (fr-pl)
      config: fr-pl
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 70.75183711835146
    - type: cos_sim_spearman
      value: 84.51542547285167
    - type: euclidean_pearson
      value: 71.84188960126669
    - type: euclidean_spearman
      value: 84.51542547285167
    - type: manhattan_pearson
      value: 73.94847166379994
    - type: manhattan_spearman
      value: 84.51542547285167
  - task:
      type: STS
    dataset:
      type: C-MTEB/STSB
      name: MTEB STSB
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 81.78690149086131
    - type: cos_sim_spearman
      value: 81.81202616916873
    - type: euclidean_pearson
      value: 80.98792254251062
    - type: euclidean_spearman
      value: 81.81202616916873
    - type: manhattan_pearson
      value: 81.46953021346732
    - type: manhattan_spearman
      value: 82.34259562492315
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
      value: 87.68273341294419
    - type: cos_sim_spearman
      value: 88.59927164210958
    - type: euclidean_pearson
      value: 88.10745681818025
    - type: euclidean_spearman
      value: 88.59927164210958
    - type: manhattan_pearson
      value: 88.25166703784649
    - type: manhattan_spearman
      value: 88.85343247873482
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
      value: 86.3340463345719
    - type: mrr
      value: 96.5182611506141
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
      value: 60.967000000000006
    - type: map_at_10
      value: 71.873
    - type: map_at_100
      value: 72.271
    - type: map_at_1000
      value: 72.292
    - type: map_at_3
      value: 69.006
    - type: map_at_5
      value: 70.856
    - type: mrr_at_1
      value: 63.666999999999994
    - type: mrr_at_10
      value: 72.929
    - type: mrr_at_100
      value: 73.26
    - type: mrr_at_1000
      value: 73.282
    - type: mrr_at_3
      value: 71.111
    - type: mrr_at_5
      value: 72.328
    - type: ndcg_at_1
      value: 63.666999999999994
    - type: ndcg_at_10
      value: 76.414
    - type: ndcg_at_100
      value: 78.152
    - type: ndcg_at_1000
      value: 78.604
    - type: ndcg_at_3
      value: 71.841
    - type: ndcg_at_5
      value: 74.435
    - type: precision_at_1
      value: 63.666999999999994
    - type: precision_at_10
      value: 10.067
    - type: precision_at_100
      value: 1.097
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 27.667
    - type: precision_at_5
      value: 18.467
    - type: recall_at_1
      value: 60.967000000000006
    - type: recall_at_10
      value: 88.922
    - type: recall_at_100
      value: 96.667
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_3
      value: 77.228
    - type: recall_at_5
      value: 83.428
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
      value: 99.82277227722773
    - type: cos_sim_ap
      value: 95.66279851444406
    - type: cos_sim_f1
      value: 90.9367088607595
    - type: cos_sim_precision
      value: 92.1025641025641
    - type: cos_sim_recall
      value: 89.8
    - type: dot_accuracy
      value: 99.82277227722773
    - type: dot_ap
      value: 95.66279851444406
    - type: dot_f1
      value: 90.9367088607595
    - type: dot_precision
      value: 92.1025641025641
    - type: dot_recall
      value: 89.8
    - type: euclidean_accuracy
      value: 99.82277227722773
    - type: euclidean_ap
      value: 95.66279851444406
    - type: euclidean_f1
      value: 90.9367088607595
    - type: euclidean_precision
      value: 92.1025641025641
    - type: euclidean_recall
      value: 89.8
    - type: manhattan_accuracy
      value: 99.82673267326733
    - type: manhattan_ap
      value: 95.86094873177069
    - type: manhattan_f1
      value: 91.26788357178096
    - type: manhattan_precision
      value: 90.06815968841285
    - type: manhattan_recall
      value: 92.5
    - type: max_accuracy
      value: 99.82673267326733
    - type: max_ap
      value: 95.86094873177069
    - type: max_f1
      value: 91.26788357178096
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
      value: 73.09533925852372
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
      value: 45.90745648090035
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
      value: 54.91147686504404
    - type: mrr
      value: 56.03900082760377
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
      value: 31.46908662038217
    - type: cos_sim_spearman
      value: 31.40325730367437
    - type: dot_pearson
      value: 31.469083969291894
    - type: dot_spearman
      value: 31.40325730367437
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/T2Reranking
      name: MTEB T2Reranking
      config: default
      split: dev
      revision: None
    metrics:
    - type: map
      value: 66.90300783402137
    - type: mrr
      value: 77.06451972574179
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/T2Retrieval
      name: MTEB T2Retrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 25.82
    - type: map_at_10
      value: 72.32300000000001
    - type: map_at_100
      value: 76.198
    - type: map_at_1000
      value: 76.281
    - type: map_at_3
      value: 50.719
    - type: map_at_5
      value: 62.326
    - type: mrr_at_1
      value: 86.599
    - type: mrr_at_10
      value: 89.751
    - type: mrr_at_100
      value: 89.876
    - type: mrr_at_1000
      value: 89.88000000000001
    - type: mrr_at_3
      value: 89.151
    - type: mrr_at_5
      value: 89.519
    - type: ndcg_at_1
      value: 86.599
    - type: ndcg_at_10
      value: 80.676
    - type: ndcg_at_100
      value: 85.03
    - type: ndcg_at_1000
      value: 85.854
    - type: ndcg_at_3
      value: 82.057
    - type: ndcg_at_5
      value: 80.537
    - type: precision_at_1
      value: 86.599
    - type: precision_at_10
      value: 40.373
    - type: precision_at_100
      value: 4.95
    - type: precision_at_1000
      value: 0.514
    - type: precision_at_3
      value: 71.918
    - type: precision_at_5
      value: 60.246
    - type: recall_at_1
      value: 25.82
    - type: recall_at_10
      value: 79.905
    - type: recall_at_100
      value: 93.88499999999999
    - type: recall_at_1000
      value: 98.073
    - type: recall_at_3
      value: 52.623
    - type: recall_at_5
      value: 66.233
  - task:
      type: Classification
    dataset:
      type: C-MTEB/TNews-classification
      name: MTEB TNews
      config: default
      split: validation
      revision: None
    metrics:
    - type: accuracy
      value: 47.050000000000004
    - type: f1
      value: 45.704071498353294
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
      value: 0.243
    - type: map_at_10
      value: 2.278
    - type: map_at_100
      value: 14.221
    - type: map_at_1000
      value: 33.474
    - type: map_at_3
      value: 0.7270000000000001
    - type: map_at_5
      value: 1.183
    - type: mrr_at_1
      value: 94.0
    - type: mrr_at_10
      value: 97.0
    - type: mrr_at_100
      value: 97.0
    - type: mrr_at_1000
      value: 97.0
    - type: mrr_at_3
      value: 97.0
    - type: mrr_at_5
      value: 97.0
    - type: ndcg_at_1
      value: 90.0
    - type: ndcg_at_10
      value: 87.249
    - type: ndcg_at_100
      value: 67.876
    - type: ndcg_at_1000
      value: 59.205
    - type: ndcg_at_3
      value: 90.12299999999999
    - type: ndcg_at_5
      value: 89.126
    - type: precision_at_1
      value: 94.0
    - type: precision_at_10
      value: 90.8
    - type: precision_at_100
      value: 69.28
    - type: precision_at_1000
      value: 25.85
    - type: precision_at_3
      value: 94.667
    - type: precision_at_5
      value: 92.80000000000001
    - type: recall_at_1
      value: 0.243
    - type: recall_at_10
      value: 2.392
    - type: recall_at_100
      value: 16.982
    - type: recall_at_1000
      value: 55.214
    - type: recall_at_3
      value: 0.745
    - type: recall_at_5
      value: 1.2229999999999999
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
      value: 70.5
    - type: f1
      value: 67.05501804646966
    - type: precision
      value: 65.73261904761904
    - type: recall
      value: 70.5
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
      value: 75.14450867052022
    - type: f1
      value: 70.98265895953759
    - type: precision
      value: 69.26782273603082
    - type: recall
      value: 75.14450867052022
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
      value: 33.170731707317074
    - type: f1
      value: 29.92876500193573
    - type: precision
      value: 28.669145894755648
    - type: recall
      value: 33.170731707317074
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
      value: 95.5
    - type: f1
      value: 94.13333333333333
    - type: precision
      value: 93.46666666666667
    - type: recall
      value: 95.5
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
      value: 99.6
    - type: f1
      value: 99.46666666666665
    - type: precision
      value: 99.4
    - type: recall
      value: 99.6
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
      value: 97.2
    - type: f1
      value: 96.39999999999999
    - type: precision
      value: 96.0
    - type: recall
      value: 97.2
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
      value: 94.5
    - type: f1
      value: 92.99666666666667
    - type: precision
      value: 92.31666666666666
    - type: recall
      value: 94.5
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
      value: 85.82089552238806
    - type: f1
      value: 81.59203980099502
    - type: precision
      value: 79.60199004975124
    - type: recall
      value: 85.82089552238806
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
      value: 79.5
    - type: f1
      value: 75.11246031746032
    - type: precision
      value: 73.38734126984127
    - type: recall
      value: 79.5
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
      value: 44.390243902439025
    - type: f1
      value: 38.48896631823461
    - type: precision
      value: 36.57220286488579
    - type: recall
      value: 44.390243902439025
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
      value: 90.2
    - type: f1
      value: 87.57333333333334
    - type: precision
      value: 86.34166666666665
    - type: recall
      value: 90.2
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
      value: 88.82138517618469
    - type: f1
      value: 85.98651854423423
    - type: precision
      value: 84.79257073424753
    - type: recall
      value: 88.82138517618469
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
      value: 77.04347826086956
    - type: f1
      value: 72.32108147606868
    - type: precision
      value: 70.37207357859532
    - type: recall
      value: 77.04347826086956
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
      value: 53.04347826086957
    - type: f1
      value: 46.88868184955141
    - type: precision
      value: 44.71730105643149
    - type: recall
      value: 53.04347826086957
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
      value: 68.0
    - type: f1
      value: 62.891813186813195
    - type: precision
      value: 61.037906162464985
    - type: recall
      value: 68.0
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
      value: 86.3
    - type: f1
      value: 82.82000000000001
    - type: precision
      value: 81.25690476190475
    - type: recall
      value: 86.3
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
      value: 68.87816646562122
    - type: f1
      value: 63.53054933272062
    - type: precision
      value: 61.47807816331196
    - type: recall
      value: 68.87816646562122
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
      value: 74.4
    - type: f1
      value: 68.99388888888889
    - type: precision
      value: 66.81035714285713
    - type: recall
      value: 74.4
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
      value: 90.5
    - type: f1
      value: 87.93666666666667
    - type: precision
      value: 86.825
    - type: recall
      value: 90.5
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
      value: 90.7
    - type: f1
      value: 88.09
    - type: precision
      value: 86.85833333333333
    - type: recall
      value: 90.7
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
      value: 67.61904761904762
    - type: f1
      value: 62.30239247214037
    - type: precision
      value: 60.340702947845806
    - type: recall
      value: 67.61904761904762
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
      value: 77.9
    - type: f1
      value: 73.81285714285714
    - type: precision
      value: 72.21570818070818
    - type: recall
      value: 77.9
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
      value: 91.8
    - type: f1
      value: 89.66666666666667
    - type: precision
      value: 88.66666666666666
    - type: recall
      value: 91.8
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
      value: 97.6
    - type: f1
      value: 96.85666666666665
    - type: precision
      value: 96.50833333333333
    - type: recall
      value: 97.6
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
      value: 95.39999999999999
    - type: f1
      value: 93.98333333333333
    - type: precision
      value: 93.30000000000001
    - type: recall
      value: 95.39999999999999
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
      value: 85.0
    - type: f1
      value: 81.31538461538462
    - type: precision
      value: 79.70666666666666
    - type: recall
      value: 85.0
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
      value: 91.60000000000001
    - type: f1
      value: 89.81888888888888
    - type: precision
      value: 89.08583333333333
    - type: recall
      value: 91.60000000000001
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
      value: 44.3
    - type: f1
      value: 38.8623088023088
    - type: precision
      value: 37.03755623461505
    - type: recall
      value: 44.3
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
      value: 95.19999999999999
    - type: f1
      value: 93.75
    - type: precision
      value: 93.05
    - type: recall
      value: 95.19999999999999
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
      value: 99.1
    - type: f1
      value: 98.8
    - type: precision
      value: 98.65
    - type: recall
      value: 99.1
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
      value: 69.6765498652291
    - type: f1
      value: 63.991785393402644
    - type: precision
      value: 61.7343729944808
    - type: recall
      value: 69.6765498652291
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
      value: 50.0
    - type: f1
      value: 42.79341029341029
    - type: precision
      value: 40.25098358431692
    - type: recall
      value: 50.0
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
      value: 89.7
    - type: f1
      value: 87.19023809523809
    - type: precision
      value: 86.12595238095237
    - type: recall
      value: 89.7
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
      value: 42.72727272727273
    - type: f1
      value: 37.78789518562245
    - type: precision
      value: 36.24208471267295
    - type: recall
      value: 42.72727272727273
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
      value: 75.26205450733752
    - type: f1
      value: 70.72842833849123
    - type: precision
      value: 68.93256464011182
    - type: recall
      value: 75.26205450733752
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
      value: 95.19999999999999
    - type: f1
      value: 93.96666666666668
    - type: precision
      value: 93.42
    - type: recall
      value: 95.19999999999999
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
      value: 76.26459143968872
    - type: f1
      value: 72.40190419178747
    - type: precision
      value: 70.84954604409856
    - type: recall
      value: 76.26459143968872
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
      value: 59.82905982905983
    - type: f1
      value: 52.2100122100122
    - type: precision
      value: 49.52516619183286
    - type: recall
      value: 59.82905982905983
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
      value: 81.69999999999999
    - type: f1
      value: 77.41714285714286
    - type: precision
      value: 75.64833333333334
    - type: recall
      value: 81.69999999999999
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
      value: 95.5
    - type: f1
      value: 94.45
    - type: precision
      value: 93.93333333333334
    - type: recall
      value: 95.5
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
      value: 58.41121495327103
    - type: f1
      value: 52.73495974430554
    - type: precision
      value: 50.717067200712066
    - type: recall
      value: 58.41121495327103
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
      value: 73.3
    - type: f1
      value: 69.20371794871795
    - type: precision
      value: 67.6597557997558
    - type: recall
      value: 73.3
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
      value: 96.5
    - type: f1
      value: 95.51666666666667
    - type: precision
      value: 95.05
    - type: recall
      value: 96.5
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
      value: 78.4
    - type: f1
      value: 73.88856643356644
    - type: precision
      value: 72.01373015873016
    - type: recall
      value: 78.4
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
      value: 95.3
    - type: f1
      value: 94.09666666666668
    - type: precision
      value: 93.53333333333332
    - type: recall
      value: 95.3
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
      value: 93.7
    - type: f1
      value: 91.94
    - type: precision
      value: 91.10833333333333
    - type: recall
      value: 93.7
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
      value: 96.8
    - type: f1
      value: 95.89999999999999
    - type: precision
      value: 95.46666666666668
    - type: recall
      value: 96.8
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
      value: 70.5
    - type: f1
      value: 66.00635642135641
    - type: precision
      value: 64.36345238095238
    - type: recall
      value: 70.5
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
      value: 92.4
    - type: f1
      value: 90.44388888888889
    - type: precision
      value: 89.5767857142857
    - type: recall
      value: 92.4
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
      value: 48.0
    - type: f1
      value: 43.15372775372776
    - type: precision
      value: 41.53152510162313
    - type: recall
      value: 48.0
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
      value: 16.7
    - type: f1
      value: 14.198431372549017
    - type: precision
      value: 13.411765873015872
    - type: recall
      value: 16.7
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
      value: 85.7
    - type: f1
      value: 81.81666666666666
    - type: precision
      value: 80.10833333333332
    - type: recall
      value: 85.7
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
      value: 69.64285714285714
    - type: f1
      value: 64.745670995671
    - type: precision
      value: 62.916666666666664
    - type: recall
      value: 69.64285714285714
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
      value: 54.665203073545555
    - type: f1
      value: 48.55366630916923
    - type: precision
      value: 46.35683318998357
    - type: recall
      value: 54.665203073545555
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
      value: 4.8
    - type: f1
      value: 3.808587223587223
    - type: precision
      value: 3.5653174603174604
    - type: recall
      value: 4.8
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
      value: 96.6
    - type: f1
      value: 95.77333333333333
    - type: precision
      value: 95.39166666666667
    - type: recall
      value: 96.6
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
      value: 95.39999999999999
    - type: f1
      value: 94.44
    - type: precision
      value: 93.975
    - type: recall
      value: 95.39999999999999
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
      value: 42.0
    - type: f1
      value: 37.024908424908425
    - type: precision
      value: 35.365992063492065
    - type: recall
      value: 42.0
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
      value: 66.7
    - type: f1
      value: 62.20460835058661
    - type: precision
      value: 60.590134587634594
    - type: recall
      value: 66.7
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
      value: 97.3
    - type: f1
      value: 96.46666666666667
    - type: precision
      value: 96.06666666666668
    - type: recall
      value: 97.3
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
      value: 47.3
    - type: f1
      value: 41.96905408317173
    - type: precision
      value: 40.18741402116402
    - type: recall
      value: 47.3
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
      value: 80.2
    - type: f1
      value: 76.22690476190476
    - type: precision
      value: 74.63539682539682
    - type: recall
      value: 80.2
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
      value: 96.0
    - type: f1
      value: 94.83333333333333
    - type: precision
      value: 94.26666666666668
    - type: recall
      value: 96.0
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
      value: 89.7
    - type: f1
      value: 87.24333333333334
    - type: precision
      value: 86.17
    - type: recall
      value: 89.7
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
      value: 50.36496350364964
    - type: f1
      value: 44.795520780922246
    - type: precision
      value: 43.09002433090024
    - type: recall
      value: 50.36496350364964
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
      value: 18.8
    - type: f1
      value: 16.242864357864356
    - type: precision
      value: 15.466596638655464
    - type: recall
      value: 18.8
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
      value: 95.19999999999999
    - type: f1
      value: 93.92333333333333
    - type: precision
      value: 93.30833333333332
    - type: recall
      value: 95.19999999999999
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
      value: 93.4
    - type: f1
      value: 91.42333333333333
    - type: precision
      value: 90.50833333333334
    - type: recall
      value: 93.4
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
      value: 26.190476190476193
    - type: f1
      value: 22.05208151636723
    - type: precision
      value: 21.09292328042328
    - type: recall
      value: 26.190476190476193
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
      value: 17.2
    - type: f1
      value: 14.021009731460952
    - type: precision
      value: 13.1389886698243
    - type: recall
      value: 17.2
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
      value: 78.67494824016563
    - type: f1
      value: 74.24430641821947
    - type: precision
      value: 72.50747642051991
    - type: recall
      value: 78.67494824016563
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
      value: 94.19999999999999
    - type: f1
      value: 92.54
    - type: precision
      value: 91.75833333333334
    - type: recall
      value: 94.19999999999999
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
      value: 90.2
    - type: f1
      value: 87.78666666666666
    - type: precision
      value: 86.69833333333334
    - type: recall
      value: 90.2
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
      value: 14.7
    - type: f1
      value: 12.19206214842218
    - type: precision
      value: 11.526261904761904
    - type: recall
      value: 14.7
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
      value: 73.16017316017316
    - type: f1
      value: 67.44858316286889
    - type: precision
      value: 65.23809523809523
    - type: recall
      value: 73.16017316017316
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
      value: 75.19083969465649
    - type: f1
      value: 70.33078880407125
    - type: precision
      value: 68.3969465648855
    - type: recall
      value: 75.19083969465649
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
      value: 62.154294032023294
    - type: f1
      value: 55.86030821838681
    - type: precision
      value: 53.53509623160277
    - type: recall
      value: 62.154294032023294
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
      value: 86.8
    - type: f1
      value: 83.9652380952381
    - type: precision
      value: 82.84242424242424
    - type: recall
      value: 86.8
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
      value: 93.50282485875707
    - type: f1
      value: 91.54425612052731
    - type: precision
      value: 90.65442561205272
    - type: recall
      value: 93.50282485875707
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
      value: 11.4
    - type: f1
      value: 9.189775870222714
    - type: precision
      value: 8.66189886502811
    - type: recall
      value: 11.4
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
      value: 93.4
    - type: f1
      value: 91.88666666666666
    - type: precision
      value: 91.21444444444444
    - type: recall
      value: 93.4
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
      value: 46.0
    - type: f1
      value: 40.51069226095542
    - type: precision
      value: 38.57804926010808
    - type: recall
      value: 46.0
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
      value: 91.0
    - type: f1
      value: 89.11333333333333
    - type: precision
      value: 88.27000000000001
    - type: recall
      value: 91.0
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
      value: 94.39999999999999
    - type: f1
      value: 92.95
    - type: precision
      value: 92.27000000000001
    - type: recall
      value: 94.39999999999999
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
      value: 14.2
    - type: f1
      value: 11.73701698770113
    - type: precision
      value: 11.079207014736676
    - type: recall
      value: 14.2
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
      value: 65.14745308310992
    - type: f1
      value: 59.665707393589415
    - type: precision
      value: 57.560853653346946
    - type: recall
      value: 65.14745308310992
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
      value: 95.39999999999999
    - type: f1
      value: 94.0
    - type: precision
      value: 93.33333333333333
    - type: recall
      value: 95.39999999999999
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
      value: 69.56521739130434
    - type: f1
      value: 62.92490118577074
    - type: precision
      value: 60.27009222661397
    - type: recall
      value: 69.56521739130434
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
      value: 40.140845070422536
    - type: f1
      value: 35.96411804158283
    - type: precision
      value: 34.89075869357559
    - type: recall
      value: 40.140845070422536
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
      value: 65.86826347305389
    - type: f1
      value: 59.646248628284546
    - type: precision
      value: 57.22982606216139
    - type: recall
      value: 65.86826347305389
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
      value: 94.89999999999999
    - type: f1
      value: 93.48333333333333
    - type: precision
      value: 92.83666666666667
    - type: recall
      value: 94.89999999999999
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
      value: 47.783251231527096
    - type: f1
      value: 42.006447302013804
    - type: precision
      value: 40.12747105111637
    - type: recall
      value: 47.783251231527096
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
      value: 69.71830985915493
    - type: f1
      value: 64.80266212660578
    - type: precision
      value: 63.08098591549296
    - type: recall
      value: 69.71830985915493
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
      value: 67.94871794871796
    - type: f1
      value: 61.59912309912309
    - type: precision
      value: 59.17338217338218
    - type: recall
      value: 67.94871794871796
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
      value: 96.39999999999999
    - type: f1
      value: 95.28333333333335
    - type: precision
      value: 94.75
    - type: recall
      value: 96.39999999999999
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
      value: 70.14613778705638
    - type: f1
      value: 65.4349338900487
    - type: precision
      value: 63.57599255302805
    - type: recall
      value: 70.14613778705638
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
      value: 9.2
    - type: f1
      value: 7.622184434339607
    - type: precision
      value: 7.287048159682417
    - type: recall
      value: 9.2
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
      value: 77.85016286644951
    - type: f1
      value: 72.83387622149837
    - type: precision
      value: 70.58450959102424
    - type: recall
      value: 77.85016286644951
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
      value: 90.8
    - type: f1
      value: 88.84333333333333
    - type: precision
      value: 87.96666666666665
    - type: recall
      value: 90.8
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
      value: 94.6
    - type: f1
      value: 93.14
    - type: precision
      value: 92.49833333333333
    - type: recall
      value: 94.6
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
      value: 84.25196850393701
    - type: f1
      value: 80.94488188976378
    - type: precision
      value: 79.65879265091863
    - type: recall
      value: 84.25196850393701
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
      value: 89.5
    - type: f1
      value: 86.89666666666666
    - type: precision
      value: 85.7
    - type: recall
      value: 89.5
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
      value: 42.797783933518005
    - type: f1
      value: 37.30617360155193
    - type: precision
      value: 35.34933825792552
    - type: recall
      value: 42.797783933518005
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
      value: 96.1
    - type: f1
      value: 94.93333333333332
    - type: precision
      value: 94.38333333333333
    - type: recall
      value: 96.1
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
      value: 54.807692307692314
    - type: f1
      value: 49.506903353057204
    - type: precision
      value: 47.54807692307693
    - type: recall
      value: 54.807692307692314
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
      value: 87.1
    - type: f1
      value: 83.61857142857143
    - type: precision
      value: 81.975
    - type: recall
      value: 87.1
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
      value: 91.10000000000001
    - type: f1
      value: 88.76333333333332
    - type: precision
      value: 87.67
    - type: recall
      value: 91.10000000000001
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
      value: 93.10000000000001
    - type: f1
      value: 91.28999999999999
    - type: precision
      value: 90.44500000000001
    - type: recall
      value: 93.10000000000001
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
      value: 39.97641509433962
    - type: f1
      value: 33.12271889998028
    - type: precision
      value: 30.95185381542554
    - type: recall
      value: 39.97641509433962
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
      value: 92.60000000000001
    - type: f1
      value: 90.69
    - type: precision
      value: 89.84500000000001
    - type: recall
      value: 92.60000000000001
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
      value: 95.07299270072993
    - type: f1
      value: 93.64355231143554
    - type: precision
      value: 92.94403892944038
    - type: recall
      value: 95.07299270072993
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
      value: 91.9
    - type: f1
      value: 89.61333333333333
    - type: precision
      value: 88.53333333333333
    - type: recall
      value: 91.9
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/ThuNewsClusteringP2P
      name: MTEB ThuNewsClusteringP2P
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 64.68478289806511
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/ThuNewsClusteringS2S
      name: MTEB ThuNewsClusteringS2S
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 57.53010296184097
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
      value: 2.519
    - type: map_at_10
      value: 10.31
    - type: map_at_100
      value: 16.027
    - type: map_at_1000
      value: 17.827
    - type: map_at_3
      value: 5.721
    - type: map_at_5
      value: 7.7829999999999995
    - type: mrr_at_1
      value: 34.694
    - type: mrr_at_10
      value: 52.642999999999994
    - type: mrr_at_100
      value: 53.366
    - type: mrr_at_1000
      value: 53.366
    - type: mrr_at_3
      value: 48.638999999999996
    - type: mrr_at_5
      value: 50.578
    - type: ndcg_at_1
      value: 31.633
    - type: ndcg_at_10
      value: 26.394000000000002
    - type: ndcg_at_100
      value: 36.41
    - type: ndcg_at_1000
      value: 49.206
    - type: ndcg_at_3
      value: 31.694
    - type: ndcg_at_5
      value: 29.529
    - type: precision_at_1
      value: 34.694
    - type: precision_at_10
      value: 23.469
    - type: precision_at_100
      value: 7.286
    - type: precision_at_1000
      value: 1.5610000000000002
    - type: precision_at_3
      value: 34.014
    - type: precision_at_5
      value: 29.796
    - type: recall_at_1
      value: 2.519
    - type: recall_at_10
      value: 17.091
    - type: recall_at_100
      value: 45.429
    - type: recall_at_1000
      value: 84.621
    - type: recall_at_3
      value: 7.208
    - type: recall_at_5
      value: 10.523
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
      value: 69.58659999999999
    - type: ap
      value: 14.735696532619
    - type: f1
      value: 54.23517220069903
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
      value: 63.723825693265425
    - type: f1
      value: 64.02405729449103
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
      value: 54.310161547491006
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
      value: 88.77630088812064
    - type: cos_sim_ap
      value: 81.61725457333809
    - type: cos_sim_f1
      value: 74.91373801916932
    - type: cos_sim_precision
      value: 72.63940520446097
    - type: cos_sim_recall
      value: 77.33509234828496
    - type: dot_accuracy
      value: 88.77630088812064
    - type: dot_ap
      value: 81.61725317476251
    - type: dot_f1
      value: 74.91373801916932
    - type: dot_precision
      value: 72.63940520446097
    - type: dot_recall
      value: 77.33509234828496
    - type: euclidean_accuracy
      value: 88.77630088812064
    - type: euclidean_ap
      value: 81.61724596869566
    - type: euclidean_f1
      value: 74.91373801916932
    - type: euclidean_precision
      value: 72.63940520446097
    - type: euclidean_recall
      value: 77.33509234828496
    - type: manhattan_accuracy
      value: 88.67497168742922
    - type: manhattan_ap
      value: 81.430251048948
    - type: manhattan_f1
      value: 74.79593118171543
    - type: manhattan_precision
      value: 71.3635274382938
    - type: manhattan_recall
      value: 78.57519788918206
    - type: max_accuracy
      value: 88.77630088812064
    - type: max_ap
      value: 81.61725457333809
    - type: max_f1
      value: 74.91373801916932
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
      value: 87.74656687446567
    - type: cos_sim_f1
      value: 80.3221673073403
    - type: cos_sim_precision
      value: 76.56871640957633
    - type: cos_sim_recall
      value: 84.46258084385587
    - type: dot_accuracy
      value: 89.85136026700819
    - type: dot_ap
      value: 87.74656471395072
    - type: dot_f1
      value: 80.3221673073403
    - type: dot_precision
      value: 76.56871640957633
    - type: dot_recall
      value: 84.46258084385587
    - type: euclidean_accuracy
      value: 89.85136026700819
    - type: euclidean_ap
      value: 87.74656885754466
    - type: euclidean_f1
      value: 80.3221673073403
    - type: euclidean_precision
      value: 76.56871640957633
    - type: euclidean_recall
      value: 84.46258084385587
    - type: manhattan_accuracy
      value: 89.86300306593705
    - type: manhattan_ap
      value: 87.78807479093082
    - type: manhattan_f1
      value: 80.31663429471911
    - type: manhattan_precision
      value: 76.63472970137772
    - type: manhattan_recall
      value: 84.3701878657222
    - type: max_accuracy
      value: 89.86300306593705
    - type: max_ap
      value: 87.78807479093082
    - type: max_f1
      value: 80.3221673073403
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/VideoRetrieval
      name: MTEB VideoRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 32.4
    - type: map_at_10
      value: 40.961999999999996
    - type: map_at_100
      value: 41.660000000000004
    - type: map_at_1000
      value: 41.721000000000004
    - type: map_at_3
      value: 38.550000000000004
    - type: map_at_5
      value: 40.06
    - type: mrr_at_1
      value: 32.4
    - type: mrr_at_10
      value: 40.961999999999996
    - type: mrr_at_100
      value: 41.660000000000004
    - type: mrr_at_1000
      value: 41.721000000000004
    - type: mrr_at_3
      value: 38.550000000000004
    - type: mrr_at_5
      value: 40.06
    - type: ndcg_at_1
      value: 32.4
    - type: ndcg_at_10
      value: 45.388
    - type: ndcg_at_100
      value: 49.012
    - type: ndcg_at_1000
      value: 50.659
    - type: ndcg_at_3
      value: 40.47
    - type: ndcg_at_5
      value: 43.232
    - type: precision_at_1
      value: 32.4
    - type: precision_at_10
      value: 5.94
    - type: precision_at_100
      value: 0.769
    - type: precision_at_1000
      value: 0.09
    - type: precision_at_3
      value: 15.333
    - type: precision_at_5
      value: 10.56
    - type: recall_at_1
      value: 32.4
    - type: recall_at_10
      value: 59.4
    - type: recall_at_100
      value: 76.9
    - type: recall_at_1000
      value: 90.0
    - type: recall_at_3
      value: 46.0
    - type: recall_at_5
      value: 52.800000000000004
  - task:
      type: Classification
    dataset:
      type: C-MTEB/waimai-classification
      name: MTEB Waimai
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 86.94000000000001
    - type: ap
      value: 70.57373468481975
    - type: f1
      value: 85.26264784928323
language:
- en
license: mit
---

## E5-mistral-7b-instruct

[Improving Text Embeddings with Large Language Models](https://arxiv.org/pdf/2401.00368.pdf). Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang, Rangan Majumder, Furu Wei, arXiv 2024

This model has 32 layers and the embedding size is 4096.

## Usage

Below is an example to encode queries and passages from the MS-MARCO passage ranking dataset.

### Sentence Transformers

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("intfloat/e5-mistral-7b-instruct")
# In case you want to reduce the maximum sequence length:
model.max_seq_length = 4096

queries = [
    "how much protein should a female eat",
    "summit define",
]
documents = [
    "As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 is 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or training for a marathon. Check out the chart below to see how much protein you should be eating each day.",
    "Definition of summit for English Language Learners. : 1  the highest point of a mountain : the top of a mountain. : 2  the highest level. : 3  a meeting or series of meetings between the leaders of two or more governments."
]

query_embeddings = model.encode(queries, prompt_name="web_search_query")
document_embeddings = model.encode(documents)

scores = (query_embeddings @ document_embeddings.T) * 100
print(scores.tolist())
```

Have a look at [config_sentence_transformers.json](config_sentence_transformers.json) for the prompts that are pre-configured, such as `web_search_query`, `sts_query`, and `summarization_query`. Additionally, check out [unilm/e5/utils.py](https://github.com/microsoft/unilm/blob/9c0f1ff7ca53431fe47d2637dfe253643d94185b/e5/utils.py#L106) for prompts we used for evaluation. You can use these via e.g. `model.encode(queries, prompt="Instruct: Given a claim, find documents that refute the claim\nQuery: ")`.


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

tokenizer = AutoTokenizer.from_pretrained('intfloat/e5-mistral-7b-instruct')
model = AutoModel.from_pretrained('intfloat/e5-mistral-7b-instruct')

max_length = 4096
# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=max_length, padding=True, truncation=True, return_tensors='pt')

outputs = model(**batch_dict)
embeddings = last_token_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

# normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:2] @ embeddings[2:].T) * 100
print(scores.tolist())
```

## Supported Languages

This model is initialized from [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)
and fine-tuned on a mixture of multilingual datasets.
As a result, it has some multilingual capability.
However, since Mistral-7B-v0.1 is mainly trained on English data, we recommend using this model for English only.
For multilingual use cases, please refer to [multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large).

## MTEB Benchmark Evaluation

Check out [unilm/e5](https://github.com/microsoft/unilm/tree/master/e5) to reproduce evaluation results 
on the [BEIR](https://arxiv.org/abs/2104.08663) and [MTEB benchmark](https://arxiv.org/abs/2210.07316).

## FAQ

**1. Do I need to add instructions to the query?**

Yes, this is how the model is trained, otherwise you will see a performance degradation.
The task definition should be a one-sentence instruction that describes the task.
This is a way to customize text embeddings for different scenarios through natural language instructions.

Please check out [unilm/e5/utils.py](https://github.com/microsoft/unilm/blob/9c0f1ff7ca53431fe47d2637dfe253643d94185b/e5/utils.py#L106) for instructions we used for evaluation.

On the other hand, there is no need to add instructions to the document side.

**2. Why are my reproduced results slightly different from reported in the model card?**

Different versions of `transformers` and `pytorch` could cause negligible but non-zero performance differences.

**3. Where are the LoRA-only weights?**

You can find the LoRA-only weights at [https://huggingface.co/intfloat/e5-mistral-7b-instruct/tree/main/lora](https://huggingface.co/intfloat/e5-mistral-7b-instruct/tree/main/lora).

## Citation

If you find our paper or models helpful, please consider cite as follows:

```bibtex
@article{wang2023improving,
  title={Improving Text Embeddings with Large Language Models},
  author={Wang, Liang and Yang, Nan and Huang, Xiaolong and Yang, Linjun and Majumder, Rangan and Wei, Furu},
  journal={arXiv preprint arXiv:2401.00368},
  year={2023}
}

@article{wang2022text,
  title={Text Embeddings by Weakly-Supervised Contrastive Pre-training},
  author={Wang, Liang and Yang, Nan and Huang, Xiaolong and Jiao, Binxing and Yang, Linjun and Jiang, Daxin and Majumder, Rangan and Wei, Furu},
  journal={arXiv preprint arXiv:2212.03533},
  year={2022}
}
```

## Limitations

Using this model for inputs longer than 4096 tokens is not recommended.

This model's multilingual capability is still inferior to [multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large) for some cases.

