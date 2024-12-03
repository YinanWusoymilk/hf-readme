---
tags:
- mteb
model-index:
- name: piccolo-embedding_mixed2
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
      value: 56.918538280469875
    - type: cos_sim_spearman
      value: 60.95597435855258
    - type: euclidean_pearson
      value: 59.73821610051437
    - type: euclidean_spearman
      value: 60.956778530262454
    - type: manhattan_pearson
      value: 59.739675774225475
    - type: manhattan_spearman
      value: 60.95243600302903
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
      value: 56.79417977023184
    - type: cos_sim_spearman
      value: 58.80984726256814
    - type: euclidean_pearson
      value: 63.42225182281334
    - type: euclidean_spearman
      value: 58.80957930593542
    - type: manhattan_pearson
      value: 63.41128425333986
    - type: manhattan_spearman
      value: 58.80784321716389
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
      value: 50.074000000000005
    - type: f1
      value: 47.11468271375511
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
      value: 73.3412976021806
    - type: cos_sim_spearman
      value: 75.0799965464816
    - type: euclidean_pearson
      value: 73.7874729086686
    - type: euclidean_spearman
      value: 75.07910973646369
    - type: manhattan_pearson
      value: 73.7716616949607
    - type: manhattan_spearman
      value: 75.06089549008017
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
      value: 60.4206935177474
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
      value: 49.53654617222264
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
      value: 90.96386786978509
    - type: mrr
      value: 92.8897619047619
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
      value: 90.41014127763198
    - type: mrr
      value: 92.45039682539682
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
      value: 26.901999999999997
    - type: map_at_10
      value: 40.321
    - type: map_at_100
      value: 42.176
    - type: map_at_1000
      value: 42.282
    - type: map_at_3
      value: 35.882
    - type: map_at_5
      value: 38.433
    - type: mrr_at_1
      value: 40.910000000000004
    - type: mrr_at_10
      value: 49.309999999999995
    - type: mrr_at_100
      value: 50.239
    - type: mrr_at_1000
      value: 50.278
    - type: mrr_at_3
      value: 46.803
    - type: mrr_at_5
      value: 48.137
    - type: ndcg_at_1
      value: 40.785
    - type: ndcg_at_10
      value: 47.14
    - type: ndcg_at_100
      value: 54.156000000000006
    - type: ndcg_at_1000
      value: 55.913999999999994
    - type: ndcg_at_3
      value: 41.669
    - type: ndcg_at_5
      value: 43.99
    - type: precision_at_1
      value: 40.785
    - type: precision_at_10
      value: 10.493
    - type: precision_at_100
      value: 1.616
    - type: precision_at_1000
      value: 0.184
    - type: precision_at_3
      value: 23.723
    - type: precision_at_5
      value: 17.249
    - type: recall_at_1
      value: 26.901999999999997
    - type: recall_at_10
      value: 58.25
    - type: recall_at_100
      value: 87.10900000000001
    - type: recall_at_1000
      value: 98.804
    - type: recall_at_3
      value: 41.804
    - type: recall_at_5
      value: 48.884
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
      value: 86.42212868310283
    - type: cos_sim_ap
      value: 92.83788702972741
    - type: cos_sim_f1
      value: 87.08912233141307
    - type: cos_sim_precision
      value: 84.24388111888112
    - type: cos_sim_recall
      value: 90.13327098433481
    - type: dot_accuracy
      value: 86.44618159951895
    - type: dot_ap
      value: 92.81146275060858
    - type: dot_f1
      value: 87.06857911250562
    - type: dot_precision
      value: 83.60232408005164
    - type: dot_recall
      value: 90.83469721767594
    - type: euclidean_accuracy
      value: 86.42212868310283
    - type: euclidean_ap
      value: 92.83805700492603
    - type: euclidean_f1
      value: 87.08803611738148
    - type: euclidean_precision
      value: 84.18066768492254
    - type: euclidean_recall
      value: 90.20341360766892
    - type: manhattan_accuracy
      value: 86.28983764281419
    - type: manhattan_ap
      value: 92.82818970981005
    - type: manhattan_f1
      value: 87.12625521832335
    - type: manhattan_precision
      value: 84.19101613606628
    - type: manhattan_recall
      value: 90.27355623100304
    - type: max_accuracy
      value: 86.44618159951895
    - type: max_ap
      value: 92.83805700492603
    - type: max_f1
      value: 87.12625521832335
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
      value: 79.215
    - type: map_at_10
      value: 86.516
    - type: map_at_100
      value: 86.6
    - type: map_at_1000
      value: 86.602
    - type: map_at_3
      value: 85.52
    - type: map_at_5
      value: 86.136
    - type: mrr_at_1
      value: 79.663
    - type: mrr_at_10
      value: 86.541
    - type: mrr_at_100
      value: 86.625
    - type: mrr_at_1000
      value: 86.627
    - type: mrr_at_3
      value: 85.564
    - type: mrr_at_5
      value: 86.15899999999999
    - type: ndcg_at_1
      value: 79.663
    - type: ndcg_at_10
      value: 89.399
    - type: ndcg_at_100
      value: 89.727
    - type: ndcg_at_1000
      value: 89.781
    - type: ndcg_at_3
      value: 87.402
    - type: ndcg_at_5
      value: 88.479
    - type: precision_at_1
      value: 79.663
    - type: precision_at_10
      value: 9.926
    - type: precision_at_100
      value: 1.006
    - type: precision_at_1000
      value: 0.101
    - type: precision_at_3
      value: 31.226
    - type: precision_at_5
      value: 19.283
    - type: recall_at_1
      value: 79.215
    - type: recall_at_10
      value: 98.209
    - type: recall_at_100
      value: 99.579
    - type: recall_at_1000
      value: 100
    - type: recall_at_3
      value: 92.703
    - type: recall_at_5
      value: 95.364
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
      value: 27.391
    - type: map_at_10
      value: 82.82000000000001
    - type: map_at_100
      value: 85.5
    - type: map_at_1000
      value: 85.533
    - type: map_at_3
      value: 57.802
    - type: map_at_5
      value: 72.82600000000001
    - type: mrr_at_1
      value: 92.80000000000001
    - type: mrr_at_10
      value: 94.83500000000001
    - type: mrr_at_100
      value: 94.883
    - type: mrr_at_1000
      value: 94.884
    - type: mrr_at_3
      value: 94.542
    - type: mrr_at_5
      value: 94.729
    - type: ndcg_at_1
      value: 92.7
    - type: ndcg_at_10
      value: 89.435
    - type: ndcg_at_100
      value: 91.78699999999999
    - type: ndcg_at_1000
      value: 92.083
    - type: ndcg_at_3
      value: 88.595
    - type: ndcg_at_5
      value: 87.53
    - type: precision_at_1
      value: 92.7
    - type: precision_at_10
      value: 42.4
    - type: precision_at_100
      value: 4.823
    - type: precision_at_1000
      value: 0.48900000000000005
    - type: precision_at_3
      value: 79.133
    - type: precision_at_5
      value: 66.8
    - type: recall_at_1
      value: 27.391
    - type: recall_at_10
      value: 90.069
    - type: recall_at_100
      value: 97.875
    - type: recall_at_1000
      value: 99.436
    - type: recall_at_3
      value: 59.367999999999995
    - type: recall_at_5
      value: 76.537
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
      value: 54.800000000000004
    - type: map_at_10
      value: 65.289
    - type: map_at_100
      value: 65.845
    - type: map_at_1000
      value: 65.853
    - type: map_at_3
      value: 62.766999999999996
    - type: map_at_5
      value: 64.252
    - type: mrr_at_1
      value: 54.800000000000004
    - type: mrr_at_10
      value: 65.255
    - type: mrr_at_100
      value: 65.81700000000001
    - type: mrr_at_1000
      value: 65.824
    - type: mrr_at_3
      value: 62.683
    - type: mrr_at_5
      value: 64.248
    - type: ndcg_at_1
      value: 54.800000000000004
    - type: ndcg_at_10
      value: 70.498
    - type: ndcg_at_100
      value: 72.82300000000001
    - type: ndcg_at_1000
      value: 73.053
    - type: ndcg_at_3
      value: 65.321
    - type: ndcg_at_5
      value: 67.998
    - type: precision_at_1
      value: 54.800000000000004
    - type: precision_at_10
      value: 8.690000000000001
    - type: precision_at_100
      value: 0.97
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_3
      value: 24.233
    - type: precision_at_5
      value: 15.840000000000002
    - type: recall_at_1
      value: 54.800000000000004
    - type: recall_at_10
      value: 86.9
    - type: recall_at_100
      value: 97
    - type: recall_at_1000
      value: 98.9
    - type: recall_at_3
      value: 72.7
    - type: recall_at_5
      value: 79.2
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
      value: 51.758368603308966
    - type: f1
      value: 40.249503783871596
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
      value: 89.08067542213884
    - type: ap
      value: 60.31281895139249
    - type: f1
      value: 84.20883153932607
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
      value: 74.04193577551248
    - type: cos_sim_spearman
      value: 79.81875884845549
    - type: euclidean_pearson
      value: 80.02581187503708
    - type: euclidean_spearman
      value: 79.81877215060574
    - type: manhattan_pearson
      value: 80.01767830530258
    - type: manhattan_spearman
      value: 79.81178852172727
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
      value: 39.90939429947956
    - type: mrr
      value: 39.71071428571429
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
      value: 68.485
    - type: map_at_10
      value: 78.27199999999999
    - type: map_at_100
      value: 78.54100000000001
    - type: map_at_1000
      value: 78.546
    - type: map_at_3
      value: 76.339
    - type: map_at_5
      value: 77.61099999999999
    - type: mrr_at_1
      value: 70.80199999999999
    - type: mrr_at_10
      value: 78.901
    - type: mrr_at_100
      value: 79.12400000000001
    - type: mrr_at_1000
      value: 79.128
    - type: mrr_at_3
      value: 77.237
    - type: mrr_at_5
      value: 78.323
    - type: ndcg_at_1
      value: 70.759
    - type: ndcg_at_10
      value: 82.191
    - type: ndcg_at_100
      value: 83.295
    - type: ndcg_at_1000
      value: 83.434
    - type: ndcg_at_3
      value: 78.57600000000001
    - type: ndcg_at_5
      value: 80.715
    - type: precision_at_1
      value: 70.759
    - type: precision_at_10
      value: 9.951
    - type: precision_at_100
      value: 1.049
    - type: precision_at_1000
      value: 0.106
    - type: precision_at_3
      value: 29.660999999999998
    - type: precision_at_5
      value: 18.94
    - type: recall_at_1
      value: 68.485
    - type: recall_at_10
      value: 93.65
    - type: recall_at_100
      value: 98.434
    - type: recall_at_1000
      value: 99.522
    - type: recall_at_3
      value: 84.20100000000001
    - type: recall_at_5
      value: 89.261
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
      value: 77.45460659045055
    - type: f1
      value: 73.84987702455533
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
      value: 85.29926025554808
    - type: f1
      value: 84.40636286569843
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
      value: 57.599999999999994
    - type: map_at_10
      value: 64.691
    - type: map_at_100
      value: 65.237
    - type: map_at_1000
      value: 65.27
    - type: map_at_3
      value: 62.733000000000004
    - type: map_at_5
      value: 63.968
    - type: mrr_at_1
      value: 58.099999999999994
    - type: mrr_at_10
      value: 64.952
    - type: mrr_at_100
      value: 65.513
    - type: mrr_at_1000
      value: 65.548
    - type: mrr_at_3
      value: 63
    - type: mrr_at_5
      value: 64.235
    - type: ndcg_at_1
      value: 57.599999999999994
    - type: ndcg_at_10
      value: 68.19
    - type: ndcg_at_100
      value: 70.98400000000001
    - type: ndcg_at_1000
      value: 71.811
    - type: ndcg_at_3
      value: 64.276
    - type: ndcg_at_5
      value: 66.47999999999999
    - type: precision_at_1
      value: 57.599999999999994
    - type: precision_at_10
      value: 7.920000000000001
    - type: precision_at_100
      value: 0.9259999999999999
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_3
      value: 22.900000000000002
    - type: precision_at_5
      value: 14.799999999999999
    - type: recall_at_1
      value: 57.599999999999994
    - type: recall_at_10
      value: 79.2
    - type: recall_at_100
      value: 92.60000000000001
    - type: recall_at_1000
      value: 99
    - type: recall_at_3
      value: 68.7
    - type: recall_at_5
      value: 74
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
      value: 79.45
    - type: f1
      value: 79.25610578280538
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
      value: 85.43584190579317
    - type: cos_sim_ap
      value: 90.89979725191012
    - type: cos_sim_f1
      value: 86.48383937316358
    - type: cos_sim_precision
      value: 80.6392694063927
    - type: cos_sim_recall
      value: 93.24181626187962
    - type: dot_accuracy
      value: 85.38170005414185
    - type: dot_ap
      value: 90.87532457866699
    - type: dot_f1
      value: 86.48383937316358
    - type: dot_precision
      value: 80.6392694063927
    - type: dot_recall
      value: 93.24181626187962
    - type: euclidean_accuracy
      value: 85.43584190579317
    - type: euclidean_ap
      value: 90.90126652086121
    - type: euclidean_f1
      value: 86.48383937316358
    - type: euclidean_precision
      value: 80.6392694063927
    - type: euclidean_recall
      value: 93.24181626187962
    - type: manhattan_accuracy
      value: 85.43584190579317
    - type: manhattan_ap
      value: 90.87896997853466
    - type: manhattan_f1
      value: 86.47581441263573
    - type: manhattan_precision
      value: 81.18628359592215
    - type: manhattan_recall
      value: 92.5026399155227
    - type: max_accuracy
      value: 85.43584190579317
    - type: max_ap
      value: 90.90126652086121
    - type: max_f1
      value: 86.48383937316358
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
      value: 94.9
    - type: ap
      value: 93.1468223150745
    - type: f1
      value: 94.88918689508299
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
      value: 40.4831743182905
    - type: cos_sim_spearman
      value: 47.4163675550491
    - type: euclidean_pearson
      value: 46.456319899274924
    - type: euclidean_spearman
      value: 47.41567079730661
    - type: manhattan_pearson
      value: 46.48561639930895
    - type: manhattan_spearman
      value: 47.447721653461215
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
      value: 42.96423587663398
    - type: cos_sim_spearman
      value: 45.13742225167858
    - type: euclidean_pearson
      value: 39.275452114075435
    - type: euclidean_spearman
      value: 45.137763540967406
    - type: manhattan_pearson
      value: 39.24797626417764
    - type: manhattan_spearman
      value: 45.13817773119268
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
      value: 66.26687809086202
    - type: cos_sim_spearman
      value: 66.9569145816897
    - type: euclidean_pearson
      value: 65.72390780809788
    - type: euclidean_spearman
      value: 66.95406938095539
    - type: manhattan_pearson
      value: 65.6220809000381
    - type: manhattan_spearman
      value: 66.88531036320953
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
      value: 80.30831700726195
    - type: cos_sim_spearman
      value: 82.05184068558792
    - type: euclidean_pearson
      value: 81.73198597791563
    - type: euclidean_spearman
      value: 82.05326103582206
    - type: manhattan_pearson
      value: 81.70886400949136
    - type: manhattan_spearman
      value: 82.03473274756037
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
      value: 69.03398835347575
    - type: mrr
      value: 79.9212528613341
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
      value: 27.515
    - type: map_at_10
      value: 77.40599999999999
    - type: map_at_100
      value: 81.087
    - type: map_at_1000
      value: 81.148
    - type: map_at_3
      value: 54.327000000000005
    - type: map_at_5
      value: 66.813
    - type: mrr_at_1
      value: 89.764
    - type: mrr_at_10
      value: 92.58
    - type: mrr_at_100
      value: 92.663
    - type: mrr_at_1000
      value: 92.666
    - type: mrr_at_3
      value: 92.15299999999999
    - type: mrr_at_5
      value: 92.431
    - type: ndcg_at_1
      value: 89.777
    - type: ndcg_at_10
      value: 85.013
    - type: ndcg_at_100
      value: 88.62100000000001
    - type: ndcg_at_1000
      value: 89.184
    - type: ndcg_at_3
      value: 86.19200000000001
    - type: ndcg_at_5
      value: 84.909
    - type: precision_at_1
      value: 89.777
    - type: precision_at_10
      value: 42.218
    - type: precision_at_100
      value: 5.032
    - type: precision_at_1000
      value: 0.517
    - type: precision_at_3
      value: 75.335
    - type: precision_at_5
      value: 63.199000000000005
    - type: recall_at_1
      value: 27.515
    - type: recall_at_10
      value: 84.258
    - type: recall_at_100
      value: 95.908
    - type: recall_at_1000
      value: 98.709
    - type: recall_at_3
      value: 56.189
    - type: recall_at_5
      value: 70.50800000000001
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
      value: 54.635999999999996
    - type: f1
      value: 52.63073912739558
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
      value: 78.75676284855221
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
      value: 71.95583733802839
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
      value: 64.9
    - type: map_at_10
      value: 75.622
    - type: map_at_100
      value: 75.93900000000001
    - type: map_at_1000
      value: 75.93900000000001
    - type: map_at_3
      value: 73.933
    - type: map_at_5
      value: 74.973
    - type: mrr_at_1
      value: 65
    - type: mrr_at_10
      value: 75.676
    - type: mrr_at_100
      value: 75.994
    - type: mrr_at_1000
      value: 75.994
    - type: mrr_at_3
      value: 74.05000000000001
    - type: mrr_at_5
      value: 75.03999999999999
    - type: ndcg_at_1
      value: 64.9
    - type: ndcg_at_10
      value: 80.08999999999999
    - type: ndcg_at_100
      value: 81.44500000000001
    - type: ndcg_at_1000
      value: 81.45599999999999
    - type: ndcg_at_3
      value: 76.688
    - type: ndcg_at_5
      value: 78.53
    - type: precision_at_1
      value: 64.9
    - type: precision_at_10
      value: 9.379999999999999
    - type: precision_at_100
      value: 0.997
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 28.199999999999996
    - type: precision_at_5
      value: 17.8
    - type: recall_at_1
      value: 64.9
    - type: recall_at_10
      value: 93.8
    - type: recall_at_100
      value: 99.7
    - type: recall_at_1000
      value: 99.8
    - type: recall_at_3
      value: 84.6
    - type: recall_at_5
      value: 89
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
      value: 89.34
    - type: ap
      value: 75.20638024616892
    - type: f1
      value: 87.88648489072128
library_name: sentence-transformers
---
# xiaobu-embedding-v2

基于piccolo-embedding[1]，主要改动如下：   
  - 合成数据替换为xiaobu-embedding-v1[2]所积累数据  
  - 在circle_loss[3]视角下统一处理CMTEB的6类问题，最大优势是可充分利用原始数据集中的多个正例，其次是可一定程度上避免考虑多个不同loss之间的权重问题  

## Usage (Sentence-Transformers)

```
pip install -U sentence-transformers
```
相似度计算：
```python
from sentence_transformers import SentenceTransformer
sentences_1 = ["样例数据-1", "样例数据-2"]
sentences_2 = ["样例数据-3", "样例数据-4"]
model = SentenceTransformer('lier007/xiaobu-embedding-v2')
embeddings_1 = model.encode(sentences_1, normalize_embeddings=True)
embeddings_2 = model.encode(sentences_2, normalize_embeddings=True)
similarity = embeddings_1 @ embeddings_2.T
print(similarity)
```


## Reference
1. https://github.com/hjq133/piccolo-embedding
2. https://huggingface.co/lier007/xiaobu-embedding
3. https://arxiv.org/abs/2002.10857