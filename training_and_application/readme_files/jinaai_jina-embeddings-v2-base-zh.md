---
tags:
  - sentence-transformers
  - feature-extraction
  - sentence-similarity
  - mteb
  - transformers
  - transformers.js
inference: false
license: apache-2.0
language:
- en
- zh
model-index:
- name: jina-embeddings-v2-base-zh
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
      value: 48.51403119231363
    - type: cos_sim_spearman
      value: 50.5928547846445
    - type: euclidean_pearson
      value: 48.750436310559074
    - type: euclidean_spearman
      value: 50.50950238691385
    - type: manhattan_pearson
      value: 48.7866189440328
    - type: manhattan_spearman
      value: 50.58692402017165
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
      value: 50.25985700105725
    - type: cos_sim_spearman
      value: 51.28815934593989
    - type: euclidean_pearson
      value: 52.70329248799904
    - type: euclidean_spearman
      value: 50.94101139559258
    - type: manhattan_pearson
      value: 52.6647237400892
    - type: manhattan_spearman
      value: 50.922441325406176
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
      value: 34.944
    - type: f1
      value: 34.06478860660109
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
      value: 65.15667035488342
    - type: cos_sim_spearman
      value: 66.07110142081
    - type: euclidean_pearson
      value: 60.447598102249714
    - type: euclidean_spearman
      value: 61.826575796578766
    - type: manhattan_pearson
      value: 60.39364279354984
    - type: manhattan_spearman
      value: 61.78743491223281
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
      value: 39.96714175391701
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
      value: 38.39863566717934
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
      value: 83.63680381780644
    - type: mrr
      value: 86.16476190476192
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
      value: 83.74350667859487
    - type: mrr
      value: 86.10388888888889
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
      value: 22.072
    - type: map_at_10
      value: 32.942
    - type: map_at_100
      value: 34.768
    - type: map_at_1000
      value: 34.902
    - type: map_at_3
      value: 29.357
    - type: map_at_5
      value: 31.236000000000004
    - type: mrr_at_1
      value: 34.259
    - type: mrr_at_10
      value: 41.957
    - type: mrr_at_100
      value: 42.982
    - type: mrr_at_1000
      value: 43.042
    - type: mrr_at_3
      value: 39.722
    - type: mrr_at_5
      value: 40.898
    - type: ndcg_at_1
      value: 34.259
    - type: ndcg_at_10
      value: 39.153
    - type: ndcg_at_100
      value: 46.493
    - type: ndcg_at_1000
      value: 49.01
    - type: ndcg_at_3
      value: 34.636
    - type: ndcg_at_5
      value: 36.278
    - type: precision_at_1
      value: 34.259
    - type: precision_at_10
      value: 8.815000000000001
    - type: precision_at_100
      value: 1.474
    - type: precision_at_1000
      value: 0.179
    - type: precision_at_3
      value: 19.73
    - type: precision_at_5
      value: 14.174000000000001
    - type: recall_at_1
      value: 22.072
    - type: recall_at_10
      value: 48.484
    - type: recall_at_100
      value: 79.035
    - type: recall_at_1000
      value: 96.15
    - type: recall_at_3
      value: 34.607
    - type: recall_at_5
      value: 40.064
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
      value: 76.7047504509922
    - type: cos_sim_ap
      value: 85.26649874800871
    - type: cos_sim_f1
      value: 78.13528724646915
    - type: cos_sim_precision
      value: 71.57587548638132
    - type: cos_sim_recall
      value: 86.01823708206688
    - type: dot_accuracy
      value: 70.13830426939266
    - type: dot_ap
      value: 77.01510412382171
    - type: dot_f1
      value: 73.56710042713817
    - type: dot_precision
      value: 63.955094991364426
    - type: dot_recall
      value: 86.57937806873977
    - type: euclidean_accuracy
      value: 75.53818400481059
    - type: euclidean_ap
      value: 84.34668448241264
    - type: euclidean_f1
      value: 77.51741608613047
    - type: euclidean_precision
      value: 70.65614777756399
    - type: euclidean_recall
      value: 85.85457096095394
    - type: manhattan_accuracy
      value: 75.49007817197835
    - type: manhattan_ap
      value: 84.40297506704299
    - type: manhattan_f1
      value: 77.63185324160932
    - type: manhattan_precision
      value: 70.03949595636637
    - type: manhattan_recall
      value: 87.07037643207856
    - type: max_accuracy
      value: 76.7047504509922
    - type: max_ap
      value: 85.26649874800871
    - type: max_f1
      value: 78.13528724646915
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
      value: 69.178
    - type: map_at_10
      value: 77.523
    - type: map_at_100
      value: 77.793
    - type: map_at_1000
      value: 77.79899999999999
    - type: map_at_3
      value: 75.878
    - type: map_at_5
      value: 76.849
    - type: mrr_at_1
      value: 69.44200000000001
    - type: mrr_at_10
      value: 77.55
    - type: mrr_at_100
      value: 77.819
    - type: mrr_at_1000
      value: 77.826
    - type: mrr_at_3
      value: 75.957
    - type: mrr_at_5
      value: 76.916
    - type: ndcg_at_1
      value: 69.44200000000001
    - type: ndcg_at_10
      value: 81.217
    - type: ndcg_at_100
      value: 82.45
    - type: ndcg_at_1000
      value: 82.636
    - type: ndcg_at_3
      value: 77.931
    - type: ndcg_at_5
      value: 79.655
    - type: precision_at_1
      value: 69.44200000000001
    - type: precision_at_10
      value: 9.357
    - type: precision_at_100
      value: 0.993
    - type: precision_at_1000
      value: 0.101
    - type: precision_at_3
      value: 28.1
    - type: precision_at_5
      value: 17.724
    - type: recall_at_1
      value: 69.178
    - type: recall_at_10
      value: 92.624
    - type: recall_at_100
      value: 98.209
    - type: recall_at_1000
      value: 99.684
    - type: recall_at_3
      value: 83.772
    - type: recall_at_5
      value: 87.882
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
      value: 25.163999999999998
    - type: map_at_10
      value: 76.386
    - type: map_at_100
      value: 79.339
    - type: map_at_1000
      value: 79.39500000000001
    - type: map_at_3
      value: 52.959
    - type: map_at_5
      value: 66.59
    - type: mrr_at_1
      value: 87.9
    - type: mrr_at_10
      value: 91.682
    - type: mrr_at_100
      value: 91.747
    - type: mrr_at_1000
      value: 91.751
    - type: mrr_at_3
      value: 91.267
    - type: mrr_at_5
      value: 91.527
    - type: ndcg_at_1
      value: 87.9
    - type: ndcg_at_10
      value: 84.569
    - type: ndcg_at_100
      value: 87.83800000000001
    - type: ndcg_at_1000
      value: 88.322
    - type: ndcg_at_3
      value: 83.473
    - type: ndcg_at_5
      value: 82.178
    - type: precision_at_1
      value: 87.9
    - type: precision_at_10
      value: 40.605000000000004
    - type: precision_at_100
      value: 4.752
    - type: precision_at_1000
      value: 0.488
    - type: precision_at_3
      value: 74.9
    - type: precision_at_5
      value: 62.96000000000001
    - type: recall_at_1
      value: 25.163999999999998
    - type: recall_at_10
      value: 85.97399999999999
    - type: recall_at_100
      value: 96.63000000000001
    - type: recall_at_1000
      value: 99.016
    - type: recall_at_3
      value: 55.611999999999995
    - type: recall_at_5
      value: 71.936
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
      value: 48.6
    - type: map_at_10
      value: 58.831
    - type: map_at_100
      value: 59.427
    - type: map_at_1000
      value: 59.44199999999999
    - type: map_at_3
      value: 56.383
    - type: map_at_5
      value: 57.753
    - type: mrr_at_1
      value: 48.6
    - type: mrr_at_10
      value: 58.831
    - type: mrr_at_100
      value: 59.427
    - type: mrr_at_1000
      value: 59.44199999999999
    - type: mrr_at_3
      value: 56.383
    - type: mrr_at_5
      value: 57.753
    - type: ndcg_at_1
      value: 48.6
    - type: ndcg_at_10
      value: 63.951
    - type: ndcg_at_100
      value: 66.72200000000001
    - type: ndcg_at_1000
      value: 67.13900000000001
    - type: ndcg_at_3
      value: 58.882
    - type: ndcg_at_5
      value: 61.373
    - type: precision_at_1
      value: 48.6
    - type: precision_at_10
      value: 8.01
    - type: precision_at_100
      value: 0.928
    - type: precision_at_1000
      value: 0.096
    - type: precision_at_3
      value: 22.033
    - type: precision_at_5
      value: 14.44
    - type: recall_at_1
      value: 48.6
    - type: recall_at_10
      value: 80.10000000000001
    - type: recall_at_100
      value: 92.80000000000001
    - type: recall_at_1000
      value: 96.1
    - type: recall_at_3
      value: 66.10000000000001
    - type: recall_at_5
      value: 72.2
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
      value: 47.36437091188918
    - type: f1
      value: 36.60946954228577
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
      value: 79.5684803001876
    - type: ap
      value: 42.671935929201524
    - type: f1
      value: 73.31912729103752
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
      value: 68.62670112113864
    - type: cos_sim_spearman
      value: 75.74009123170768
    - type: euclidean_pearson
      value: 73.93002595958237
    - type: euclidean_spearman
      value: 75.35222935003587
    - type: manhattan_pearson
      value: 73.89870445158144
    - type: manhattan_spearman
      value: 75.31714936339398
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
      value: 31.5372713650176
    - type: mrr
      value: 30.163095238095238
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
      value: 65.054
    - type: map_at_10
      value: 74.156
    - type: map_at_100
      value: 74.523
    - type: map_at_1000
      value: 74.535
    - type: map_at_3
      value: 72.269
    - type: map_at_5
      value: 73.41
    - type: mrr_at_1
      value: 67.24900000000001
    - type: mrr_at_10
      value: 74.78399999999999
    - type: mrr_at_100
      value: 75.107
    - type: mrr_at_1000
      value: 75.117
    - type: mrr_at_3
      value: 73.13499999999999
    - type: mrr_at_5
      value: 74.13499999999999
    - type: ndcg_at_1
      value: 67.24900000000001
    - type: ndcg_at_10
      value: 77.96300000000001
    - type: ndcg_at_100
      value: 79.584
    - type: ndcg_at_1000
      value: 79.884
    - type: ndcg_at_3
      value: 74.342
    - type: ndcg_at_5
      value: 76.278
    - type: precision_at_1
      value: 67.24900000000001
    - type: precision_at_10
      value: 9.466
    - type: precision_at_100
      value: 1.027
    - type: precision_at_1000
      value: 0.105
    - type: precision_at_3
      value: 27.955999999999996
    - type: precision_at_5
      value: 17.817
    - type: recall_at_1
      value: 65.054
    - type: recall_at_10
      value: 89.113
    - type: recall_at_100
      value: 96.369
    - type: recall_at_1000
      value: 98.714
    - type: recall_at_3
      value: 79.45400000000001
    - type: recall_at_5
      value: 84.06
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
      value: 68.1977135171486
    - type: f1
      value: 67.23114308718404
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
      value: 71.92669804976462
    - type: f1
      value: 72.90628475628779
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
      value: 49.2
    - type: map_at_10
      value: 54.539
    - type: map_at_100
      value: 55.135
    - type: map_at_1000
      value: 55.19199999999999
    - type: map_at_3
      value: 53.383
    - type: map_at_5
      value: 54.142999999999994
    - type: mrr_at_1
      value: 49.2
    - type: mrr_at_10
      value: 54.539
    - type: mrr_at_100
      value: 55.135999999999996
    - type: mrr_at_1000
      value: 55.19199999999999
    - type: mrr_at_3
      value: 53.383
    - type: mrr_at_5
      value: 54.142999999999994
    - type: ndcg_at_1
      value: 49.2
    - type: ndcg_at_10
      value: 57.123000000000005
    - type: ndcg_at_100
      value: 60.21300000000001
    - type: ndcg_at_1000
      value: 61.915
    - type: ndcg_at_3
      value: 54.772
    - type: ndcg_at_5
      value: 56.157999999999994
    - type: precision_at_1
      value: 49.2
    - type: precision_at_10
      value: 6.52
    - type: precision_at_100
      value: 0.8009999999999999
    - type: precision_at_1000
      value: 0.094
    - type: precision_at_3
      value: 19.6
    - type: precision_at_5
      value: 12.44
    - type: recall_at_1
      value: 49.2
    - type: recall_at_10
      value: 65.2
    - type: recall_at_100
      value: 80.10000000000001
    - type: recall_at_1000
      value: 93.89999999999999
    - type: recall_at_3
      value: 58.8
    - type: recall_at_5
      value: 62.2
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
      value: 63.29333333333334
    - type: f1
      value: 63.03293854259612
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
      value: 75.69030860855442
    - type: cos_sim_ap
      value: 80.6157833772759
    - type: cos_sim_f1
      value: 77.87524366471735
    - type: cos_sim_precision
      value: 72.3076923076923
    - type: cos_sim_recall
      value: 84.37170010559663
    - type: dot_accuracy
      value: 67.78559826746074
    - type: dot_ap
      value: 72.00871467527499
    - type: dot_f1
      value: 72.58722247394654
    - type: dot_precision
      value: 63.57142857142857
    - type: dot_recall
      value: 84.58289334741288
    - type: euclidean_accuracy
      value: 75.20303194369248
    - type: euclidean_ap
      value: 80.98587256415605
    - type: euclidean_f1
      value: 77.26396917148362
    - type: euclidean_precision
      value: 71.03631532329496
    - type: euclidean_recall
      value: 84.68848996832101
    - type: manhattan_accuracy
      value: 75.20303194369248
    - type: manhattan_ap
      value: 80.93460699513219
    - type: manhattan_f1
      value: 77.124773960217
    - type: manhattan_precision
      value: 67.43083003952569
    - type: manhattan_recall
      value: 90.07391763463569
    - type: max_accuracy
      value: 75.69030860855442
    - type: max_ap
      value: 80.98587256415605
    - type: max_f1
      value: 77.87524366471735
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
      value: 87.00000000000001
    - type: ap
      value: 83.24372135949511
    - type: f1
      value: 86.95554191530607
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
      value: 37.57616811591219
    - type: cos_sim_spearman
      value: 41.490259084930045
    - type: euclidean_pearson
      value: 38.9155043692188
    - type: euclidean_spearman
      value: 39.16056534305623
    - type: manhattan_pearson
      value: 38.76569892264335
    - type: manhattan_spearman
      value: 38.99891685590743
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
      value: 35.44858610359665
    - type: cos_sim_spearman
      value: 38.11128146262466
    - type: euclidean_pearson
      value: 31.928644189822457
    - type: euclidean_spearman
      value: 34.384936631696554
    - type: manhattan_pearson
      value: 31.90586687414376
    - type: manhattan_spearman
      value: 34.35770153777186
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
      value: 66.54931957553592
    - type: cos_sim_spearman
      value: 69.25068863016632
    - type: euclidean_pearson
      value: 50.26525596106869
    - type: euclidean_spearman
      value: 63.83352741910006
    - type: manhattan_pearson
      value: 49.98798282198196
    - type: manhattan_spearman
      value: 63.87649521907841
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
      value: 82.52782476625825
    - type: cos_sim_spearman
      value: 82.55618986168398
    - type: euclidean_pearson
      value: 78.48190631687673
    - type: euclidean_spearman
      value: 78.39479731354655
    - type: manhattan_pearson
      value: 78.51176592165885
    - type: manhattan_spearman
      value: 78.42363787303265
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
      value: 67.36693873615643
    - type: mrr
      value: 77.83847701797939
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
      value: 25.795
    - type: map_at_10
      value: 72.258
    - type: map_at_100
      value: 76.049
    - type: map_at_1000
      value: 76.134
    - type: map_at_3
      value: 50.697
    - type: map_at_5
      value: 62.324999999999996
    - type: mrr_at_1
      value: 86.634
    - type: mrr_at_10
      value: 89.792
    - type: mrr_at_100
      value: 89.91900000000001
    - type: mrr_at_1000
      value: 89.923
    - type: mrr_at_3
      value: 89.224
    - type: mrr_at_5
      value: 89.608
    - type: ndcg_at_1
      value: 86.634
    - type: ndcg_at_10
      value: 80.589
    - type: ndcg_at_100
      value: 84.812
    - type: ndcg_at_1000
      value: 85.662
    - type: ndcg_at_3
      value: 82.169
    - type: ndcg_at_5
      value: 80.619
    - type: precision_at_1
      value: 86.634
    - type: precision_at_10
      value: 40.389
    - type: precision_at_100
      value: 4.93
    - type: precision_at_1000
      value: 0.513
    - type: precision_at_3
      value: 72.104
    - type: precision_at_5
      value: 60.425
    - type: recall_at_1
      value: 25.795
    - type: recall_at_10
      value: 79.565
    - type: recall_at_100
      value: 93.24799999999999
    - type: recall_at_1000
      value: 97.595
    - type: recall_at_3
      value: 52.583999999999996
    - type: recall_at_5
      value: 66.175
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
      value: 47.648999999999994
    - type: f1
      value: 46.28925837008413
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
      value: 54.07641891287953
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
      value: 53.423702062353954
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
      value: 55.7
    - type: map_at_10
      value: 65.923
    - type: map_at_100
      value: 66.42
    - type: map_at_1000
      value: 66.431
    - type: map_at_3
      value: 63.9
    - type: map_at_5
      value: 65.225
    - type: mrr_at_1
      value: 55.60000000000001
    - type: mrr_at_10
      value: 65.873
    - type: mrr_at_100
      value: 66.36999999999999
    - type: mrr_at_1000
      value: 66.381
    - type: mrr_at_3
      value: 63.849999999999994
    - type: mrr_at_5
      value: 65.17500000000001
    - type: ndcg_at_1
      value: 55.7
    - type: ndcg_at_10
      value: 70.621
    - type: ndcg_at_100
      value: 72.944
    - type: ndcg_at_1000
      value: 73.25399999999999
    - type: ndcg_at_3
      value: 66.547
    - type: ndcg_at_5
      value: 68.93599999999999
    - type: precision_at_1
      value: 55.7
    - type: precision_at_10
      value: 8.52
    - type: precision_at_100
      value: 0.958
    - type: precision_at_1000
      value: 0.098
    - type: precision_at_3
      value: 24.733
    - type: precision_at_5
      value: 16
    - type: recall_at_1
      value: 55.7
    - type: recall_at_10
      value: 85.2
    - type: recall_at_100
      value: 95.8
    - type: recall_at_1000
      value: 98.3
    - type: recall_at_3
      value: 74.2
    - type: recall_at_5
      value: 80
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
      value: 84.54
    - type: ap
      value: 66.13603199670062
    - type: f1
      value: 82.61420654584116
---
<!-- TODO: add evaluation results here -->
<br><br>

<p align="center">
<img src="https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/603763514de52ff951d89793/AFoybzd5lpBQXEBrQHuTt.png?w=200&h=200&f=face" alt="Finetuner logo: Finetuner helps you to create experiments in order to improve embeddings on search tasks. It accompanies you to deliver the last mile of performance-tuning for neural search applications." width="150px">
</p>


<p align="center">
<b>The text embedding set trained by <a href="https://jina.ai/"><b>Jina AI</b></a>.</b>
</p>

## Quick Start

The easiest way to starting using `jina-embeddings-v2-base-zh` is to use Jina AI's [Embedding API](https://jina.ai/embeddings/).

## Intended Usage & Model Info

`jina-embeddings-v2-base-zh` is a Chinese/English bilingual text **embedding model** supporting **8192 sequence length**.
It is based on a BERT architecture (JinaBERT) that supports the symmetric bidirectional variant of [ALiBi](https://arxiv.org/abs/2108.12409) to allow longer sequence length.
We have designed it for high performance in mono-lingual & cross-lingual applications and trained it specifically to support mixed Chinese-English input without bias. 
Additionally, we provide the following embedding models:

`jina-embeddings-v2-base-zh` 是支持中英双语的**文本向量**模型，它支持长达**8192字符**的文本编码。
该模型的研发基于BERT架构(JinaBERT)，JinaBERT是在BERT架构基础上的改进，首次将[ALiBi](https://arxiv.org/abs/2108.12409)应用到编码器架构中以支持更长的序列。
不同于以往的单语言/多语言向量模型，我们设计双语模型来更好的支持单语言（中搜中）以及跨语言（中搜英）文档检索。
除此之外，我们也提供其它向量模型:

- [`jina-embeddings-v2-small-en`](https://huggingface.co/jinaai/jina-embeddings-v2-small-en): 33 million parameters.
- [`jina-embeddings-v2-base-en`](https://huggingface.co/jinaai/jina-embeddings-v2-base-en): 137 million parameters.
- [`jina-embeddings-v2-base-zh`](https://huggingface.co/jinaai/jina-embeddings-v2-base-zh): 161 million parameters Chinese-English Bilingual embeddings **(you are here)**.
- [`jina-embeddings-v2-base-de`](https://huggingface.co/jinaai/jina-embeddings-v2-base-de): 161 million parameters German-English Bilingual embeddings.
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

sentences = ['How is the weather today?', '今天天气怎么样?']

tokenizer = AutoTokenizer.from_pretrained('jinaai/jina-embeddings-v2-base-zh')
model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-zh', trust_remote_code=True, torch_dtype=torch.bfloat16)

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
model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-zh', trust_remote_code=True, torch_dtype=torch.bfloat16)
embeddings = model.encode(['How is the weather today?', '今天天气怎么样?'])
print(cos_sim(embeddings[0], embeddings[1]))
```

If you only want to handle shorter sequence, such as 2k, pass the `max_length` parameter to the `encode` function:

```python
embeddings = model.encode(
    ['Very long ... document'],
    max_length=2048
)
```

If you want to use the model together with the [sentence-transformers package](https://github.com/UKPLab/sentence-transformers/), make sure that you have installed the latest release and set `trust_remote_code=True` as well:

```python
!pip install -U sentence-transformers
from sentence_transformers import SentenceTransformer
from numpy.linalg import norm

cos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))
model = SentenceTransformer('jinaai/jina-embeddings-v2-base-zh', trust_remote_code=True)
embeddings = model.encode(['How is the weather today?', '今天天气怎么样?'])
print(cos_sim(embeddings[0], embeddings[1]))
```

Using the its latest release (v2.3.0) sentence-transformers also supports Jina embeddings (Please make sure that you are logged into huggingface as well):

```python
!pip install -U sentence-transformers
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer(
    "jinaai/jina-embeddings-v2-base-zh", # switch to en/zh for English or Chinese
    trust_remote_code=True
)

# control your input sequence length up to 8192
model.max_seq_length = 1024

embeddings = model.encode([
    'How is the weather today?',
    '今天天气怎么样?'
])
print(cos_sim(embeddings[0], embeddings[1]))
```

## Alternatives to Using Transformers Package

1. _Managed SaaS_: Get started with a free key on Jina AI's [Embedding API](https://jina.ai/embeddings/). 
2. _Private and high-performance deployment_: Get started by picking from our suite of models and deploy them on [AWS Sagemaker](https://aws.amazon.com/marketplace/seller-profile?id=seller-stch2ludm6vgy).

## Use Jina Embeddings for RAG

According to the latest blog post from [LLamaIndex](https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83),

> In summary, to achieve the peak performance in both hit rate and MRR, the combination of OpenAI or JinaAI-Base embeddings with the CohereRerank/bge-reranker-large reranker stands out.

<img src="https://miro.medium.com/v2/resize:fit:4800/format:webp/1*ZP2RVejCZovF3FDCg-Bx3A.png" width="780px">

## Trouble Shooting

**Loading of Model Code failed**

If you forgot to pass the `trust_remote_code=True` flag when calling `AutoModel.from_pretrained` or initializing the model via the `SentenceTransformer` class, you will receive an error that the model weights could not be initialized.
This is caused by tranformers falling back to creating a default BERT model, instead of a jina-embedding model:

```bash
Some weights of the model checkpoint at jinaai/jina-embeddings-v2-base-zh were not used when initializing BertModel: ['encoder.layer.2.mlp.layernorm.weight', 'encoder.layer.3.mlp.layernorm.weight', 'encoder.layer.10.mlp.wo.bias', 'encoder.layer.5.mlp.wo.bias', 'encoder.layer.2.mlp.layernorm.bias', 'encoder.layer.1.mlp.gated_layers.weight', 'encoder.layer.5.mlp.gated_layers.weight', 'encoder.layer.8.mlp.layernorm.bias', ...
```

**User is not logged into Huggingface**

The model is only availabe under [gated access](https://huggingface.co/docs/hub/models-gated).
This means you need to be logged into huggingface load load it.
If you receive the following error, you need to provide an access token, either by using the huggingface-cli or providing the token via an environment variable as described above:
```bash
OSError: jinaai/jina-embeddings-v2-base-zh is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'
If this is a private repository, make sure to pass a token having permission to this repo with `use_auth_token` or log in with `huggingface-cli login` and pass `use_auth_token=True`.
```

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