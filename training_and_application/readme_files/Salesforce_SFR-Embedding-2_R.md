---
tags:
- mteb
- sentence-transformers
- transformers
model-index:
- name: Salesforce/SFR-Embedding-2_R
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
      value: 92.71641791044776
    - type: ap
      value: 69.47931007147756
    - type: f1
      value: 88.0252625393374
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
      value: 97.31075
    - type: ap
      value: 96.26693923450127
    - type: f1
      value: 97.31042448894502
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
      value: 61.040000000000006
    - type: f1
      value: 60.78646832640785
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
      value: 37.767
    - type: map_at_10
      value: 53.908
    - type: map_at_100
      value: 54.583000000000006
    - type: map_at_1000
      value: 54.583999999999996
    - type: map_at_20
      value: 54.50899999999999
    - type: map_at_3
      value: 49.514
    - type: map_at_5
      value: 52.059999999999995
    - type: mrr_at_1
      value: 38.26458036984353
    - type: mrr_at_10
      value: 54.120408001987066
    - type: mrr_at_100
      value: 54.780719904297406
    - type: mrr_at_1000
      value: 54.78174226698592
    - type: mrr_at_20
      value: 54.706604527160295
    - type: mrr_at_3
      value: 49.71550497866294
    - type: mrr_at_5
      value: 52.247510668563436
    - type: ndcg_at_1
      value: 37.767
    - type: ndcg_at_10
      value: 62.339999999999996
    - type: ndcg_at_100
      value: 64.89399999999999
    - type: ndcg_at_1000
      value: 64.914
    - type: ndcg_at_20
      value: 64.402
    - type: ndcg_at_3
      value: 53.33
    - type: ndcg_at_5
      value: 57.93899999999999
    - type: precision_at_1
      value: 37.767
    - type: precision_at_10
      value: 8.905000000000001
    - type: precision_at_100
      value: 0.9950000000000001
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.8469999999999995
    - type: precision_at_3
      value: 21.456
    - type: precision_at_5
      value: 15.121
    - type: recall_at_1
      value: 37.767
    - type: recall_at_10
      value: 89.047
    - type: recall_at_100
      value: 99.502
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_20
      value: 96.942
    - type: recall_at_3
      value: 64.36699999999999
    - type: recall_at_5
      value: 75.605
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
      value: 54.024325012036314
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
      value: 48.817300846601675
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
      value: 66.71478959728732
    - type: mrr
      value: 79.07202216066482
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
      value: 88.79517914982239
    - type: cos_sim_spearman
      value: 87.60440576436838
    - type: euclidean_pearson
      value: 87.75596873521118
    - type: euclidean_spearman
      value: 87.60440576436838
    - type: manhattan_pearson
      value: 87.74113773865973
    - type: manhattan_spearman
      value: 87.50560833247899
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
      value: 90.02272727272727
    - type: f1
      value: 89.96681880265936
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
      value: 50.75930389699286
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
      value: 46.57286439805565
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
    metrics:
    - type: map_at_1
      value: 28.056666666666665
    - type: map_at_10
      value: 39.61749999999999
    - type: map_at_100
      value: 41.00666666666666
    - type: map_at_1000
      value: 41.11358333333334
    - type: map_at_20
      value: 40.410250000000005
    - type: map_at_3
      value: 35.98591666666667
    - type: map_at_5
      value: 38.02
    - type: mrr_at_1
      value: 33.73950708467142
    - type: mrr_at_10
      value: 44.0987162763402
    - type: mrr_at_100
      value: 44.94302678553521
    - type: mrr_at_1000
      value: 44.98758207055161
    - type: mrr_at_20
      value: 44.61156907536121
    - type: mrr_at_3
      value: 41.247253732468415
    - type: mrr_at_5
      value: 42.84859071071954
    - type: ndcg_at_1
      value: 33.739666666666665
    - type: ndcg_at_10
      value: 46.10683333333334
    - type: ndcg_at_100
      value: 51.49275000000001
    - type: ndcg_at_1000
      value: 53.2585
    - type: ndcg_at_20
      value: 48.349
    - type: ndcg_at_3
      value: 40.12416666666667
    - type: ndcg_at_5
      value: 42.94783333333333
    - type: precision_at_1
      value: 33.739666666666665
    - type: precision_at_10
      value: 8.46025
    - type: precision_at_100
      value: 1.3215833333333333
    - type: precision_at_1000
      value: 0.16524999999999998
    - type: precision_at_20
      value: 4.9935833333333335
    - type: precision_at_3
      value: 19.00516666666667
    - type: precision_at_5
      value: 13.72141666666667
    - type: recall_at_1
      value: 28.056666666666665
    - type: recall_at_10
      value: 60.68825000000001
    - type: recall_at_100
      value: 83.74433333333334
    - type: recall_at_1000
      value: 95.62299999999999
    - type: recall_at_20
      value: 68.77641666666668
    - type: recall_at_3
      value: 44.06991666666667
    - type: recall_at_5
      value: 51.324999999999996
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
      value: 15.609
    - type: map_at_10
      value: 25.584
    - type: map_at_100
      value: 27.291999999999998
    - type: map_at_1000
      value: 27.471
    - type: map_at_20
      value: 26.497
    - type: map_at_3
      value: 21.61
    - type: map_at_5
      value: 23.76
    - type: mrr_at_1
      value: 34.98371335504886
    - type: mrr_at_10
      value: 45.73747479447807
    - type: mrr_at_100
      value: 46.4973410206458
    - type: mrr_at_1000
      value: 46.53372527933685
    - type: mrr_at_20
      value: 46.19978503202757
    - type: mrr_at_3
      value: 42.85559174809991
    - type: mrr_at_5
      value: 44.65038002171556
    - type: ndcg_at_1
      value: 34.984
    - type: ndcg_at_10
      value: 34.427
    - type: ndcg_at_100
      value: 40.908
    - type: ndcg_at_1000
      value: 44.118
    - type: ndcg_at_20
      value: 36.885
    - type: ndcg_at_3
      value: 29.09
    - type: ndcg_at_5
      value: 30.979
    - type: precision_at_1
      value: 34.984
    - type: precision_at_10
      value: 10.476
    - type: precision_at_100
      value: 1.748
    - type: precision_at_1000
      value: 0.23500000000000001
    - type: precision_at_20
      value: 6.313000000000001
    - type: precision_at_3
      value: 21.39
    - type: precision_at_5
      value: 16.378
    - type: recall_at_1
      value: 15.609
    - type: recall_at_10
      value: 39.619
    - type: recall_at_100
      value: 61.952
    - type: recall_at_1000
      value: 79.861
    - type: recall_at_20
      value: 46.489000000000004
    - type: recall_at_3
      value: 26.134
    - type: recall_at_5
      value: 31.955
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
      value: 10.482
    - type: map_at_10
      value: 25.155
    - type: map_at_100
      value: 36.606
    - type: map_at_1000
      value: 38.617000000000004
    - type: map_at_20
      value: 29.676000000000002
    - type: map_at_3
      value: 16.881
    - type: map_at_5
      value: 20.043
    - type: mrr_at_1
      value: 76.0
    - type: mrr_at_10
      value: 82.5610119047619
    - type: mrr_at_100
      value: 82.74795937825128
    - type: mrr_at_1000
      value: 82.75526942226163
    - type: mrr_at_20
      value: 82.70580357142858
    - type: mrr_at_3
      value: 81.41666666666667
    - type: mrr_at_5
      value: 82.26666666666667
    - type: ndcg_at_1
      value: 63.625
    - type: ndcg_at_10
      value: 51.214000000000006
    - type: ndcg_at_100
      value: 56.411
    - type: ndcg_at_1000
      value: 63.429
    - type: ndcg_at_20
      value: 50.595
    - type: ndcg_at_3
      value: 54.989
    - type: ndcg_at_5
      value: 52.589
    - type: precision_at_1
      value: 76.0
    - type: precision_at_10
      value: 41.975
    - type: precision_at_100
      value: 13.26
    - type: precision_at_1000
      value: 2.493
    - type: precision_at_20
      value: 32.15
    - type: precision_at_3
      value: 59.0
    - type: precision_at_5
      value: 51.24999999999999
    - type: recall_at_1
      value: 10.482
    - type: recall_at_10
      value: 31.075000000000003
    - type: recall_at_100
      value: 63.119
    - type: recall_at_1000
      value: 85.32300000000001
    - type: recall_at_20
      value: 40.345
    - type: recall_at_3
      value: 17.916
    - type: recall_at_5
      value: 22.475
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
      value: 93.36500000000001
    - type: f1
      value: 89.89541440183861
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
      value: 81.948
    - type: map_at_10
      value: 89.47500000000001
    - type: map_at_100
      value: 89.66199999999999
    - type: map_at_1000
      value: 89.671
    - type: map_at_20
      value: 89.582
    - type: map_at_3
      value: 88.646
    - type: map_at_5
      value: 89.19
    - type: mrr_at_1
      value: 88.23882388238825
    - type: mrr_at_10
      value: 93.2122736083131
    - type: mrr_at_100
      value: 93.23908769526588
    - type: mrr_at_1000
      value: 93.23932393435209
    - type: mrr_at_20
      value: 93.23217832106207
    - type: mrr_at_3
      value: 92.98679867986787
    - type: mrr_at_5
      value: 93.16906690669056
    - type: ndcg_at_1
      value: 88.239
    - type: ndcg_at_10
      value: 92.155
    - type: ndcg_at_100
      value: 92.735
    - type: ndcg_at_1000
      value: 92.866
    - type: ndcg_at_20
      value: 92.39699999999999
    - type: ndcg_at_3
      value: 91.188
    - type: ndcg_at_5
      value: 91.754
    - type: precision_at_1
      value: 88.239
    - type: precision_at_10
      value: 10.903
    - type: precision_at_100
      value: 1.147
    - type: precision_at_1000
      value: 0.117
    - type: precision_at_20
      value: 5.5440000000000005
    - type: precision_at_3
      value: 34.598
    - type: precision_at_5
      value: 21.302
    - type: recall_at_1
      value: 81.948
    - type: recall_at_10
      value: 96.518
    - type: recall_at_100
      value: 98.646
    - type: recall_at_1000
      value: 99.399
    - type: recall_at_20
      value: 97.262
    - type: recall_at_3
      value: 93.89800000000001
    - type: recall_at_5
      value: 95.38600000000001
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
      value: 32.033
    - type: map_at_10
      value: 53.55
    - type: map_at_100
      value: 55.672
    - type: map_at_1000
      value: 55.764
    - type: map_at_20
      value: 54.87800000000001
    - type: map_at_3
      value: 46.761
    - type: map_at_5
      value: 50.529
    - type: mrr_at_1
      value: 60.95679012345679
    - type: mrr_at_10
      value: 68.70835782872815
    - type: mrr_at_100
      value: 69.21918402444501
    - type: mrr_at_1000
      value: 69.23608783148705
    - type: mrr_at_20
      value: 69.07497388036454
    - type: mrr_at_3
      value: 66.76954732510285
    - type: mrr_at_5
      value: 67.95781893004109
    - type: ndcg_at_1
      value: 60.956999999999994
    - type: ndcg_at_10
      value: 61.766
    - type: ndcg_at_100
      value: 67.652
    - type: ndcg_at_1000
      value: 68.94500000000001
    - type: ndcg_at_20
      value: 64.48700000000001
    - type: ndcg_at_3
      value: 57.25
    - type: ndcg_at_5
      value: 58.64
    - type: precision_at_1
      value: 60.956999999999994
    - type: precision_at_10
      value: 17.083000000000002
    - type: precision_at_100
      value: 2.346
    - type: precision_at_1000
      value: 0.257
    - type: precision_at_20
      value: 9.807
    - type: precision_at_3
      value: 38.477
    - type: precision_at_5
      value: 27.962999999999997
    - type: recall_at_1
      value: 32.033
    - type: recall_at_10
      value: 69.44
    - type: recall_at_100
      value: 90.17500000000001
    - type: recall_at_1000
      value: 97.90100000000001
    - type: recall_at_20
      value: 77.629
    - type: recall_at_3
      value: 51.664
    - type: recall_at_5
      value: 59.565
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
      value: 42.741
    - type: map_at_10
      value: 74.811
    - type: map_at_100
      value: 75.508
    - type: map_at_1000
      value: 75.541
    - type: map_at_20
      value: 75.25699999999999
    - type: map_at_3
      value: 71.31
    - type: map_at_5
      value: 73.69
    - type: mrr_at_1
      value: 85.48278190411884
    - type: mrr_at_10
      value: 90.20347684425987
    - type: mrr_at_100
      value: 90.29734129342121
    - type: mrr_at_1000
      value: 90.30017606259217
    - type: mrr_at_20
      value: 90.27225310310567
    - type: mrr_at_3
      value: 89.67364393427842
    - type: mrr_at_5
      value: 90.02408282691847
    - type: ndcg_at_1
      value: 85.483
    - type: ndcg_at_10
      value: 81.361
    - type: ndcg_at_100
      value: 83.588
    - type: ndcg_at_1000
      value: 84.19
    - type: ndcg_at_20
      value: 82.42699999999999
    - type: ndcg_at_3
      value: 76.779
    - type: ndcg_at_5
      value: 79.581
    - type: precision_at_1
      value: 85.483
    - type: precision_at_10
      value: 17.113
    - type: precision_at_100
      value: 1.882
    - type: precision_at_1000
      value: 0.196
    - type: precision_at_20
      value: 8.899
    - type: precision_at_3
      value: 50.397999999999996
    - type: precision_at_5
      value: 32.443
    - type: recall_at_1
      value: 42.741
    - type: recall_at_10
      value: 85.564
    - type: recall_at_100
      value: 94.07799999999999
    - type: recall_at_1000
      value: 97.995
    - type: recall_at_20
      value: 88.98700000000001
    - type: recall_at_3
      value: 75.598
    - type: recall_at_5
      value: 81.107
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
      value: 96.80320000000002
    - type: ap
      value: 94.98856145360044
    - type: f1
      value: 96.80287885839178
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
      value: 22.539
    - type: map_at_10
      value: 35.109
    - type: map_at_100
      value: 36.287000000000006
    - type: map_at_1000
      value: 36.335
    - type: map_at_20
      value: 35.838
    - type: map_at_3
      value: 31.11
    - type: map_at_5
      value: 33.455
    - type: mrr_at_1
      value: 23.15186246418338
    - type: mrr_at_10
      value: 35.70532018920268
    - type: mrr_at_100
      value: 36.815167506137584
    - type: mrr_at_1000
      value: 36.85695349443505
    - type: mrr_at_20
      value: 36.39500867880642
    - type: mrr_at_3
      value: 31.81232091690535
    - type: mrr_at_5
      value: 34.096704871060155
    - type: ndcg_at_1
      value: 23.152
    - type: ndcg_at_10
      value: 42.181999999999995
    - type: ndcg_at_100
      value: 47.847
    - type: ndcg_at_1000
      value: 48.988
    - type: ndcg_at_20
      value: 44.767
    - type: ndcg_at_3
      value: 34.088
    - type: ndcg_at_5
      value: 38.257999999999996
    - type: precision_at_1
      value: 23.152
    - type: precision_at_10
      value: 6.678000000000001
    - type: precision_at_100
      value: 0.9530000000000001
    - type: precision_at_1000
      value: 0.105
    - type: precision_at_20
      value: 3.881
    - type: precision_at_3
      value: 14.518
    - type: precision_at_5
      value: 10.831
    - type: recall_at_1
      value: 22.539
    - type: recall_at_10
      value: 63.965
    - type: recall_at_100
      value: 90.129
    - type: recall_at_1000
      value: 98.721
    - type: recall_at_20
      value: 74.00999999999999
    - type: recall_at_3
      value: 42.004999999999995
    - type: recall_at_5
      value: 52.028
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
      value: 98.5750113999088
    - type: f1
      value: 98.41576079230245
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
      value: 91.29502963976289
    - type: f1
      value: 74.84400169335184
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
      value: 85.96839273705447
    - type: f1
      value: 82.43129186593926
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
      value: 90.60860793544047
    - type: f1
      value: 89.79415994859477
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
      value: 46.661892807041355
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
      value: 44.17598473858937
  - task:
      type: Reranking
    dataset:
      type: mteb/mind_small
      name: MTEB MindSmallReranking
      config: default
      split: test
      revision: 59042f120c80e8afa9cdbb224f67076cec0fc9a7
    metrics:
    - type: map
      value: 31.260919294024603
    - type: mrr
      value: 32.37049108835034
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
      value: 6.672000000000001
    - type: map_at_10
      value: 15.972
    - type: map_at_100
      value: 20.94
    - type: map_at_1000
      value: 22.877
    - type: map_at_20
      value: 17.986
    - type: map_at_3
      value: 11.161
    - type: map_at_5
      value: 13.293
    - type: mrr_at_1
      value: 53.56037151702786
    - type: mrr_at_10
      value: 61.915696103002595
    - type: mrr_at_100
      value: 62.4130902631107
    - type: mrr_at_1000
      value: 62.45228087711845
    - type: mrr_at_20
      value: 62.1983715004112
    - type: mrr_at_3
      value: 60.31991744066049
    - type: mrr_at_5
      value: 61.27966976264191
    - type: ndcg_at_1
      value: 50.929
    - type: ndcg_at_10
      value: 41.336
    - type: ndcg_at_100
      value: 38.586999999999996
    - type: ndcg_at_1000
      value: 48.155
    - type: ndcg_at_20
      value: 38.888
    - type: ndcg_at_3
      value: 47.0
    - type: ndcg_at_5
      value: 44.335
    - type: precision_at_1
      value: 53.251000000000005
    - type: precision_at_10
      value: 31.146
    - type: precision_at_100
      value: 10.040000000000001
    - type: precision_at_1000
      value: 2.432
    - type: precision_at_20
      value: 23.421
    - type: precision_at_3
      value: 45.098
    - type: precision_at_5
      value: 39.071
    - type: recall_at_1
      value: 6.672000000000001
    - type: recall_at_10
      value: 20.764
    - type: recall_at_100
      value: 40.759
    - type: recall_at_1000
      value: 75.015
    - type: recall_at_20
      value: 25.548
    - type: recall_at_3
      value: 12.328
    - type: recall_at_5
      value: 15.601999999999999
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
      value: 50.944
    - type: map_at_10
      value: 67.565
    - type: map_at_100
      value: 68.10300000000001
    - type: map_at_1000
      value: 68.109
    - type: map_at_20
      value: 67.973
    - type: map_at_3
      value: 64.176
    - type: map_at_5
      value: 66.39699999999999
    - type: mrr_at_1
      value: 57.01042873696408
    - type: mrr_at_10
      value: 69.76629605105849
    - type: mrr_at_100
      value: 70.09927347130204
    - type: mrr_at_1000
      value: 70.10309675839956
    - type: mrr_at_20
      value: 70.02288627712392
    - type: mrr_at_3
      value: 67.46813441483191
    - type: mrr_at_5
      value: 68.93105446118189
    - type: ndcg_at_1
      value: 57.010000000000005
    - type: ndcg_at_10
      value: 73.956
    - type: ndcg_at_100
      value: 75.90299999999999
    - type: ndcg_at_1000
      value: 76.03999999999999
    - type: ndcg_at_20
      value: 75.17
    - type: ndcg_at_3
      value: 68.13900000000001
    - type: ndcg_at_5
      value: 71.532
    - type: precision_at_1
      value: 57.010000000000005
    - type: precision_at_10
      value: 10.91
    - type: precision_at_100
      value: 1.2
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_20
      value: 5.753
    - type: precision_at_3
      value: 29.828
    - type: precision_at_5
      value: 19.971
    - type: recall_at_1
      value: 50.944
    - type: recall_at_10
      value: 90.754
    - type: recall_at_100
      value: 98.699
    - type: recall_at_1000
      value: 99.701
    - type: recall_at_20
      value: 95.148
    - type: recall_at_3
      value: 76.224
    - type: recall_at_5
      value: 83.872
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
      value: 71.856
    - type: map_at_10
      value: 86.077
    - type: map_at_100
      value: 86.696
    - type: map_at_1000
      value: 86.708
    - type: map_at_20
      value: 86.493
    - type: map_at_3
      value: 83.176
    - type: map_at_5
      value: 85.008
    - type: mrr_at_1
      value: 82.74000000000001
    - type: mrr_at_10
      value: 88.68947222222207
    - type: mrr_at_100
      value: 88.78196949571182
    - type: mrr_at_1000
      value: 88.78223256200576
    - type: mrr_at_20
      value: 88.76455636228219
    - type: mrr_at_3
      value: 87.85833333333316
    - type: mrr_at_5
      value: 88.43933333333311
    - type: ndcg_at_1
      value: 82.74000000000001
    - type: ndcg_at_10
      value: 89.583
    - type: ndcg_at_100
      value: 90.652
    - type: ndcg_at_1000
      value: 90.711
    - type: ndcg_at_20
      value: 90.203
    - type: ndcg_at_3
      value: 86.967
    - type: ndcg_at_5
      value: 88.43299999999999
    - type: precision_at_1
      value: 82.74000000000001
    - type: precision_at_10
      value: 13.617
    - type: precision_at_100
      value: 1.542
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_20
      value: 7.217999999999999
    - type: precision_at_3
      value: 38.163000000000004
    - type: precision_at_5
      value: 25.05
    - type: recall_at_1
      value: 71.856
    - type: recall_at_10
      value: 96.244
    - type: recall_at_100
      value: 99.773
    - type: recall_at_1000
      value: 99.99900000000001
    - type: recall_at_20
      value: 98.221
    - type: recall_at_3
      value: 88.715
    - type: recall_at_5
      value: 92.88499999999999
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
      value: 62.91969510127886
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
      value: 72.74201090913765
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
      value: 5.8229999999999995
    - type: map_at_10
      value: 15.152
    - type: map_at_100
      value: 17.936
    - type: map_at_1000
      value: 18.292
    - type: map_at_20
      value: 16.526
    - type: map_at_3
      value: 10.294
    - type: map_at_5
      value: 12.794
    - type: mrr_at_1
      value: 28.599999999999998
    - type: mrr_at_10
      value: 40.68206349206347
    - type: mrr_at_100
      value: 41.673752995361795
    - type: mrr_at_1000
      value: 41.71500072915374
    - type: mrr_at_20
      value: 41.28552805166964
    - type: mrr_at_3
      value: 36.84999999999998
    - type: mrr_at_5
      value: 39.19999999999995
    - type: ndcg_at_1
      value: 28.599999999999998
    - type: ndcg_at_10
      value: 24.866
    - type: ndcg_at_100
      value: 34.597
    - type: ndcg_at_1000
      value: 39.994
    - type: ndcg_at_20
      value: 28.309
    - type: ndcg_at_3
      value: 22.749
    - type: ndcg_at_5
      value: 20.502000000000002
    - type: precision_at_1
      value: 28.599999999999998
    - type: precision_at_10
      value: 13.089999999999998
    - type: precision_at_100
      value: 2.7119999999999997
    - type: precision_at_1000
      value: 0.39899999999999997
    - type: precision_at_20
      value: 8.53
    - type: precision_at_3
      value: 21.099999999999998
    - type: precision_at_5
      value: 18.22
    - type: recall_at_1
      value: 5.8229999999999995
    - type: recall_at_10
      value: 26.522000000000002
    - type: recall_at_100
      value: 55.003
    - type: recall_at_1000
      value: 80.977
    - type: recall_at_20
      value: 34.618
    - type: recall_at_3
      value: 12.848
    - type: recall_at_5
      value: 18.477
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
      value: 80.72562067620224
    - type: cos_sim_spearman
      value: 77.00710192931953
    - type: euclidean_pearson
      value: 78.65843289108192
    - type: euclidean_spearman
      value: 77.00710077709005
    - type: manhattan_pearson
      value: 78.48859522905846
    - type: manhattan_spearman
      value: 76.8213740840866
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
      value: 81.15015325911659
    - type: cos_sim_spearman
      value: 75.67268325741222
    - type: euclidean_pearson
      value: 75.54004763633206
    - type: euclidean_spearman
      value: 75.67262179635058
    - type: manhattan_pearson
      value: 75.80681616893116
    - type: manhattan_spearman
      value: 75.93721016401406
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
      value: 81.71651874476737
    - type: cos_sim_spearman
      value: 82.39667472464997
    - type: euclidean_pearson
      value: 82.28256504757712
    - type: euclidean_spearman
      value: 82.39663674872656
    - type: manhattan_pearson
      value: 82.3192873176068
    - type: manhattan_spearman
      value: 82.41915252757059
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
      value: 81.222967367593
    - type: cos_sim_spearman
      value: 79.92685877403252
    - type: euclidean_pearson
      value: 79.95053542861498
    - type: euclidean_spearman
      value: 79.9268858850991
    - type: manhattan_pearson
      value: 79.90485851323321
    - type: manhattan_spearman
      value: 79.93878025669312
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
      value: 85.27539130156643
    - type: cos_sim_spearman
      value: 85.81645767911826
    - type: euclidean_pearson
      value: 85.5488615685444
    - type: euclidean_spearman
      value: 85.81647022566916
    - type: manhattan_pearson
      value: 85.6358149547879
    - type: manhattan_spearman
      value: 85.96347118567043
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
      value: 83.43727336154858
    - type: cos_sim_spearman
      value: 84.50468882202796
    - type: euclidean_pearson
      value: 83.23576727105372
    - type: euclidean_spearman
      value: 84.50468882202796
    - type: manhattan_pearson
      value: 83.28843314503176
    - type: manhattan_spearman
      value: 84.60383766214322
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-en)
      config: en-en
      split: test
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
    metrics:
    - type: cos_sim_pearson
      value: 88.86589365166874
    - type: cos_sim_spearman
      value: 88.93117996163835
    - type: euclidean_pearson
      value: 89.12271565981082
    - type: euclidean_spearman
      value: 88.93117996163835
    - type: manhattan_pearson
      value: 88.94419759325545
    - type: manhattan_spearman
      value: 88.63073561731899
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
      value: 67.96578378422929
    - type: cos_sim_spearman
      value: 67.10257461424345
    - type: euclidean_pearson
      value: 67.51317866195149
    - type: euclidean_spearman
      value: 67.10257461424345
    - type: manhattan_pearson
      value: 67.74940912013754
    - type: manhattan_spearman
      value: 67.46694183937207
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
      value: 83.55433725920493
    - type: cos_sim_spearman
      value: 83.60373857254014
    - type: euclidean_pearson
      value: 83.08086082334839
    - type: euclidean_spearman
      value: 83.6036864776559
    - type: manhattan_pearson
      value: 83.2232267589246
    - type: manhattan_spearman
      value: 83.78923946962664
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
      value: 87.28566757174322
    - type: mrr
      value: 96.63827639317836
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
      value: 70.661
    - type: map_at_10
      value: 82.051
    - type: map_at_100
      value: 82.162
    - type: map_at_1000
      value: 82.167
    - type: map_at_20
      value: 82.122
    - type: map_at_3
      value: 79.919
    - type: map_at_5
      value: 81.368
    - type: mrr_at_1
      value: 74.33333333333333
    - type: mrr_at_10
      value: 82.98452380952381
    - type: mrr_at_100
      value: 83.09512420633841
    - type: mrr_at_1000
      value: 83.10026279387446
    - type: mrr_at_20
      value: 83.05460927960928
    - type: mrr_at_3
      value: 81.8888888888889
    - type: mrr_at_5
      value: 82.65555555555557
    - type: ndcg_at_1
      value: 74.333
    - type: ndcg_at_10
      value: 85.914
    - type: ndcg_at_100
      value: 86.473
    - type: ndcg_at_1000
      value: 86.602
    - type: ndcg_at_20
      value: 86.169
    - type: ndcg_at_3
      value: 83.047
    - type: ndcg_at_5
      value: 84.72
    - type: precision_at_1
      value: 74.333
    - type: precision_at_10
      value: 10.933
    - type: precision_at_100
      value: 1.1199999999999999
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_20
      value: 5.5169999999999995
    - type: precision_at_3
      value: 32.444
    - type: precision_at_5
      value: 20.8
    - type: recall_at_1
      value: 70.661
    - type: recall_at_10
      value: 96.333
    - type: recall_at_100
      value: 99.0
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 97.333
    - type: recall_at_3
      value: 88.64999999999999
    - type: recall_at_5
      value: 93.089
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
      value: 99.89108910891089
    - type: cos_sim_ap
      value: 97.61815451002174
    - type: cos_sim_f1
      value: 94.51097804391219
    - type: cos_sim_precision
      value: 94.32270916334662
    - type: cos_sim_recall
      value: 94.69999999999999
    - type: dot_accuracy
      value: 99.89108910891089
    - type: dot_ap
      value: 97.61815451002175
    - type: dot_f1
      value: 94.51097804391219
    - type: dot_precision
      value: 94.32270916334662
    - type: dot_recall
      value: 94.69999999999999
    - type: euclidean_accuracy
      value: 99.89108910891089
    - type: euclidean_ap
      value: 97.61815534251431
    - type: euclidean_f1
      value: 94.51097804391219
    - type: euclidean_precision
      value: 94.32270916334662
    - type: euclidean_recall
      value: 94.69999999999999
    - type: manhattan_accuracy
      value: 99.8940594059406
    - type: manhattan_ap
      value: 97.66124472227202
    - type: manhattan_f1
      value: 94.65267366316841
    - type: manhattan_precision
      value: 94.60539460539461
    - type: manhattan_recall
      value: 94.69999999999999
    - type: max_accuracy
      value: 99.8940594059406
    - type: max_ap
      value: 97.66124472227202
    - type: max_f1
      value: 94.65267366316841
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
      value: 76.482776391195
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
      value: 48.29023235124473
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
      value: 55.3190739691685
    - type: mrr
      value: 56.40441972243442
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
      value: 31.98570594378664
    - type: cos_sim_spearman
      value: 30.712965330802174
    - type: dot_pearson
      value: 31.98570540209124
    - type: dot_spearman
      value: 30.712965330802174
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
      value: 0.25
    - type: map_at_10
      value: 2.2640000000000002
    - type: map_at_100
      value: 14.447
    - type: map_at_1000
      value: 35.452
    - type: map_at_20
      value: 4.163
    - type: map_at_3
      value: 0.715
    - type: map_at_5
      value: 1.1780000000000002
    - type: mrr_at_1
      value: 94.0
    - type: mrr_at_10
      value: 96.66666666666667
    - type: mrr_at_100
      value: 96.66666666666667
    - type: mrr_at_1000
      value: 96.66666666666667
    - type: mrr_at_20
      value: 96.66666666666667
    - type: mrr_at_3
      value: 96.66666666666667
    - type: mrr_at_5
      value: 96.66666666666667
    - type: ndcg_at_1
      value: 92.0
    - type: ndcg_at_10
      value: 87.26899999999999
    - type: ndcg_at_100
      value: 68.586
    - type: ndcg_at_1000
      value: 61.056999999999995
    - type: ndcg_at_20
      value: 83.452
    - type: ndcg_at_3
      value: 90.11200000000001
    - type: ndcg_at_5
      value: 89.103
    - type: precision_at_1
      value: 94.0
    - type: precision_at_10
      value: 91.2
    - type: precision_at_100
      value: 70.12
    - type: precision_at_1000
      value: 26.773999999999997
    - type: precision_at_20
      value: 87.3
    - type: precision_at_3
      value: 92.667
    - type: precision_at_5
      value: 92.4
    - type: recall_at_1
      value: 0.25
    - type: recall_at_10
      value: 2.3970000000000002
    - type: recall_at_100
      value: 17.233999999999998
    - type: recall_at_1000
      value: 57.879000000000005
    - type: recall_at_20
      value: 4.508
    - type: recall_at_3
      value: 0.734
    - type: recall_at_5
      value: 1.2269999999999999
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
      value: 2.806
    - type: map_at_10
      value: 11.369
    - type: map_at_100
      value: 17.791
    - type: map_at_1000
      value: 19.363
    - type: map_at_20
      value: 14.038999999999998
    - type: map_at_3
      value: 5.817
    - type: map_at_5
      value: 8.331
    - type: mrr_at_1
      value: 36.734693877551024
    - type: mrr_at_10
      value: 53.355199222546155
    - type: mrr_at_100
      value: 53.648197984932665
    - type: mrr_at_1000
      value: 53.648197984932665
    - type: mrr_at_20
      value: 53.500971817298336
    - type: mrr_at_3
      value: 48.63945578231292
    - type: mrr_at_5
      value: 51.29251700680272
    - type: ndcg_at_1
      value: 35.714
    - type: ndcg_at_10
      value: 28.18
    - type: ndcg_at_100
      value: 39.22
    - type: ndcg_at_1000
      value: 50.807
    - type: ndcg_at_20
      value: 28.979
    - type: ndcg_at_3
      value: 31.114000000000004
    - type: ndcg_at_5
      value: 29.687
    - type: precision_at_1
      value: 36.735
    - type: precision_at_10
      value: 24.898
    - type: precision_at_100
      value: 7.918
    - type: precision_at_1000
      value: 1.5779999999999998
    - type: precision_at_20
      value: 18.878
    - type: precision_at_3
      value: 31.293
    - type: precision_at_5
      value: 29.387999999999998
    - type: recall_at_1
      value: 2.806
    - type: recall_at_10
      value: 17.776
    - type: recall_at_100
      value: 49.41
    - type: recall_at_1000
      value: 84.97200000000001
    - type: recall_at_20
      value: 26.589000000000002
    - type: recall_at_3
      value: 6.866999999999999
    - type: recall_at_5
      value: 10.964
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
      value: 91.1376953125
    - type: ap
      value: 40.51219896084815
    - type: f1
      value: 77.5195445434559
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
      value: 79.69722693831352
    - type: f1
      value: 80.02969178591319
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
      value: 66.42427742893598
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
      value: 87.81069321094355
    - type: cos_sim_ap
      value: 78.57014017906349
    - type: cos_sim_f1
      value: 72.38883143743536
    - type: cos_sim_precision
      value: 70.95793208312215
    - type: cos_sim_recall
      value: 73.87862796833772
    - type: dot_accuracy
      value: 87.81069321094355
    - type: dot_ap
      value: 78.5701399541226
    - type: dot_f1
      value: 72.38883143743536
    - type: dot_precision
      value: 70.95793208312215
    - type: dot_recall
      value: 73.87862796833772
    - type: euclidean_accuracy
      value: 87.81069321094355
    - type: euclidean_ap
      value: 78.57015336777854
    - type: euclidean_f1
      value: 72.38883143743536
    - type: euclidean_precision
      value: 70.95793208312215
    - type: euclidean_recall
      value: 73.87862796833772
    - type: manhattan_accuracy
      value: 87.57227156225785
    - type: manhattan_ap
      value: 78.19109731614216
    - type: manhattan_f1
      value: 71.87819856704198
    - type: manhattan_precision
      value: 69.77148534525584
    - type: manhattan_recall
      value: 74.1160949868074
    - type: max_accuracy
      value: 87.81069321094355
    - type: max_ap
      value: 78.57015336777854
    - type: max_f1
      value: 72.38883143743536
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
      value: 89.95032405790352
    - type: cos_sim_ap
      value: 88.03104739249996
    - type: cos_sim_f1
      value: 80.34377190070451
    - type: cos_sim_precision
      value: 77.11534376548892
    - type: cos_sim_recall
      value: 83.85432707114259
    - type: dot_accuracy
      value: 89.95032405790352
    - type: dot_ap
      value: 88.03105328515932
    - type: dot_f1
      value: 80.34377190070451
    - type: dot_precision
      value: 77.11534376548892
    - type: dot_recall
      value: 83.85432707114259
    - type: euclidean_accuracy
      value: 89.95032405790352
    - type: euclidean_ap
      value: 88.03105084564575
    - type: euclidean_f1
      value: 80.34377190070451
    - type: euclidean_precision
      value: 77.11534376548892
    - type: euclidean_recall
      value: 83.85432707114259
    - type: manhattan_accuracy
      value: 89.88046726433035
    - type: manhattan_ap
      value: 88.01484191858279
    - type: manhattan_f1
      value: 80.34005593993817
    - type: manhattan_precision
      value: 76.95290468133108
    - type: manhattan_recall
      value: 84.03911302740991
    - type: max_accuracy
      value: 89.95032405790352
    - type: max_ap
      value: 88.03105328515932
    - type: max_f1
      value: 80.34377190070451
language:
- en
license: cc-by-nc-4.0
---

<h1 align="center">Salesforce/SFR-Embedding-2_R</h1>

**SFR-Embedding by Salesforce Research.**

The model is for **research purposes only**.

More technical details will be updated later. Meanwhile, please refer to our previous work [SFR-Embedding](https://blog.salesforceairesearch.com/sfr-embedded-mistral/) for details.


SFR-Embedding Team (∗indicates equal contributors, † indicates co-leaders).
* Rui Meng*
* Ye Liu*
* Tong Niu
* Shafiq Rayhan Joty
* Caiming Xiong †
* Yingbo Zhou †
* Semih Yavuz †

### Citation
```bibtex
@misc{SFR-embedding-2,
  title={SFR-Embedding-2: Advanced Text Embedding with Multi-stage Training},
  author={Rui Meng*, Ye Liu*, Shafiq Rayhan Joty, Caiming Xiong, Yingbo Zhou, Semih Yavuz},
  year={2024},
  url={https://huggingface.co/Salesforce/SFR-Embedding-2_R}
}
```


## How to run

#### Transformers
The models can be used as follows:
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
    get_detailed_instruct(task, 'How to bake a chocolate cake'),
    get_detailed_instruct(task, 'Symptoms of the flu')
]
# No need to add instruction for retrieval documents
passages = [
    "To bake a delicious chocolate cake, you'll need the following ingredients: all-purpose flour, sugar, cocoa powder, baking powder, baking soda, salt, eggs, milk, vegetable oil, and vanilla extract. Start by preheating your oven to 350°F (175°C). In a mixing bowl, combine the dry ingredients (flour, sugar, cocoa powder, baking powder, baking soda, and salt). In a separate bowl, whisk together the wet ingredients (eggs, milk, vegetable oil, and vanilla extract). Gradually add the wet mixture to the dry ingredients, stirring until well combined. Pour the batter into a greased cake pan and bake for 30-35 minutes. Let it cool before frosting with your favorite chocolate frosting. Enjoy your homemade chocolate cake!",
    "The flu, or influenza, is an illness caused by influenza viruses. Common symptoms of the flu include a high fever, chills, cough, sore throat, runny or stuffy nose, body aches, headache, fatigue, and sometimes nausea and vomiting. These symptoms can come on suddenly and are usually more severe than the common cold. It's important to get plenty of rest, stay hydrated, and consult a healthcare professional if you suspect you have the flu. In some cases, antiviral medications can help alleviate symptoms and reduce the duration of the illness."
]

# load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('Salesforce/SFR-Embedding-2_R')
model = AutoModel.from_pretrained('Salesforce/SFR-Embedding-2_R')

# get the embeddings
max_length = 4096
input_texts = queries + passages
batch_dict = tokenizer(input_texts, max_length=max_length, padding=True, truncation=True, return_tensors="pt")
outputs = model(**batch_dict)
embeddings = last_token_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

# normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:2] @ embeddings[2:].T) * 100
print(scores.tolist())
# [[40.132083892822266, 25.032529830932617], [15.006855010986328, 39.93733215332031]]
```

### Sentence Transformers
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Salesforce/SFR-Embedding-2_R")

def get_detailed_instruct(task_description: str, query: str) -> str:
    return f'Instruct: {task_description}\nQuery: {query}'

# Each query must come with a one-sentence instruction that describes the task
task = 'Given a web search query, retrieve relevant passages that answer the query'
queries = [
    get_detailed_instruct(task, 'How to bake a chocolate cake'),
    get_detailed_instruct(task, 'Symptoms of the flu')
]
# No need to add instruction for retrieval documents
passages = [
    "To bake a delicious chocolate cake, you'll need the following ingredients: all-purpose flour, sugar, cocoa powder, baking powder, baking soda, salt, eggs, milk, vegetable oil, and vanilla extract. Start by preheating your oven to 350°F (175°C). In a mixing bowl, combine the dry ingredients (flour, sugar, cocoa powder, baking powder, baking soda, and salt). In a separate bowl, whisk together the wet ingredients (eggs, milk, vegetable oil, and vanilla extract). Gradually add the wet mixture to the dry ingredients, stirring until well combined. Pour the batter into a greased cake pan and bake for 30-35 minutes. Let it cool before frosting with your favorite chocolate frosting. Enjoy your homemade chocolate cake!",
    "The flu, or influenza, is an illness caused by influenza viruses. Common symptoms of the flu include a high fever, chills, cough, sore throat, runny or stuffy nose, body aches, headache, fatigue, and sometimes nausea and vomiting. These symptoms can come on suddenly and are usually more severe than the common cold. It's important to get plenty of rest, stay hydrated, and consult a healthcare professional if you suspect you have the flu. In some cases, antiviral medications can help alleviate symptoms and reduce the duration of the illness."
]

embeddings = model.encode(queries + passages)
scores = model.similarity(embeddings[:2], embeddings[2:]) * 100
print(scores.tolist())
# [[40.13203811645508, 25.032546997070312], [15.00684642791748, 39.937339782714844]]
```





