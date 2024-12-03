---
tags:
- mteb
- transformers
- sentence-transformers
model-index:
- name: cde-small-v1
  results:
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 87.02985074626866
    - type: ap
      value: 56.706190238632956
    - type: ap_weighted
      value: 56.706190238632956
    - type: f1
      value: 81.93161953007674
    - type: f1_weighted
      value: 87.7650174177188
    - type: main_score
      value: 87.02985074626866
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AmazonPolarityClassification (default)
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
      split: test
      type: mteb/amazon_polarity
    metrics:
    - type: accuracy
      value: 94.664175
    - type: ap
      value: 91.68668057762052
    - type: ap_weighted
      value: 91.68668057762052
    - type: f1
      value: 94.65859470333152
    - type: f1_weighted
      value: 94.65859470333152
    - type: main_score
      value: 94.664175
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
      value: 55.762
    - type: f1
      value: 55.06427827477677
    - type: f1_weighted
      value: 55.06427827477677
    - type: main_score
      value: 55.762
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ArguAna (default)
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
      split: test
      type: mteb/arguana
    metrics:
    - type: main_score
      value: 71.99600000000001
    - type: map_at_1
      value: 49.004
    - type: map_at_10
      value: 64.741
    - type: map_at_100
      value: 65.045
    - type: map_at_1000
      value: 65.048
    - type: map_at_20
      value: 64.999
    - type: map_at_3
      value: 61.344
    - type: map_at_5
      value: 63.595
    - type: mrr_at_1
      value: 50.71123755334281
    - type: mrr_at_10
      value: 65.32688703741336
    - type: mrr_at_100
      value: 65.63793917015693
    - type: mrr_at_1000
      value: 65.64038101143724
    - type: mrr_at_20
      value: 65.59178002869953
    - type: mrr_at_3
      value: 61.960644855381695
    - type: mrr_at_5
      value: 64.12636320531058
    - type: nauc_map_at_1000_diff1
      value: 15.961240220366024
    - type: nauc_map_at_1000_max
      value: -7.44765810583741
    - type: nauc_map_at_1000_std
      value: -17.07167824225605
    - type: nauc_map_at_100_diff1
      value: 15.965616911760689
    - type: nauc_map_at_100_max
      value: -7.440609797442297
    - type: nauc_map_at_100_std
      value: -17.069175070766125
    - type: nauc_map_at_10_diff1
      value: 16.0053641689455
    - type: nauc_map_at_10_max
      value: -7.292003400856069
    - type: nauc_map_at_10_std
      value: -17.21891231777586
    - type: nauc_map_at_1_diff1
      value: 16.775859614223965
    - type: nauc_map_at_1_max
      value: -10.812150486389175
    - type: nauc_map_at_1_std
      value: -18.447209756110635
    - type: nauc_map_at_20_diff1
      value: 16.00477985164213
    - type: nauc_map_at_20_max
      value: -7.344399709169316
    - type: nauc_map_at_20_std
      value: -17.011815937847548
    - type: nauc_map_at_3_diff1
      value: 15.730294091913994
    - type: nauc_map_at_3_max
      value: -7.13902722192326
    - type: nauc_map_at_3_std
      value: -16.846251134000045
    - type: nauc_map_at_5_diff1
      value: 15.952653874864062
    - type: nauc_map_at_5_max
      value: -6.730509527119155
    - type: nauc_map_at_5_std
      value: -16.586379153220353
    - type: nauc_mrr_at_1000_diff1
      value: 10.221278338563085
    - type: nauc_mrr_at_1000_max
      value: -10.513831642963527
    - type: nauc_mrr_at_1000_std
      value: -16.340880407651863
    - type: nauc_mrr_at_100_diff1
      value: 10.226217465992063
    - type: nauc_mrr_at_100_max
      value: -10.506478667638874
    - type: nauc_mrr_at_100_std
      value: -16.33847358633176
    - type: nauc_mrr_at_10_diff1
      value: 10.293491655887369
    - type: nauc_mrr_at_10_max
      value: -10.357229664747909
    - type: nauc_mrr_at_10_std
      value: -16.496874845739885
    - type: nauc_mrr_at_1_diff1
      value: 12.049863016253427
    - type: nauc_mrr_at_1_max
      value: -11.968579522299635
    - type: nauc_mrr_at_1_std
      value: -16.65245790056632
    - type: nauc_mrr_at_20_diff1
      value: 10.276109067921565
    - type: nauc_mrr_at_20_max
      value: -10.404100283652397
    - type: nauc_mrr_at_20_std
      value: -16.282098762560164
    - type: nauc_mrr_at_3_diff1
      value: 10.338008940592475
    - type: nauc_mrr_at_3_max
      value: -10.123508259477648
    - type: nauc_mrr_at_3_std
      value: -16.218834894850918
    - type: nauc_mrr_at_5_diff1
      value: 10.114375457049043
    - type: nauc_mrr_at_5_max
      value: -9.987361588255437
    - type: nauc_mrr_at_5_std
      value: -15.723897501895118
    - type: nauc_ndcg_at_1000_diff1
      value: 16.00889445347496
    - type: nauc_ndcg_at_1000_max
      value: -6.746746500535893
    - type: nauc_ndcg_at_1000_std
      value: -16.567047531839382
    - type: nauc_ndcg_at_100_diff1
      value: 16.10719535312808
    - type: nauc_ndcg_at_100_max
      value: -6.59354665730934
    - type: nauc_ndcg_at_100_std
      value: -16.513298001700566
    - type: nauc_ndcg_at_10_diff1
      value: 16.396485814351973
    - type: nauc_ndcg_at_10_max
      value: -5.7111859345525895
    - type: nauc_ndcg_at_10_std
      value: -17.13416103510026
    - type: nauc_ndcg_at_1_diff1
      value: 16.775859614223965
    - type: nauc_ndcg_at_1_max
      value: -10.812150486389175
    - type: nauc_ndcg_at_1_std
      value: -18.447209756110635
    - type: nauc_ndcg_at_20_diff1
      value: 16.414235526534497
    - type: nauc_ndcg_at_20_max
      value: -5.890463457153039
    - type: nauc_ndcg_at_20_std
      value: -16.124783371499017
    - type: nauc_ndcg_at_3_diff1
      value: 15.683431770601713
    - type: nauc_ndcg_at_3_max
      value: -5.546675513691499
    - type: nauc_ndcg_at_3_std
      value: -15.973244504586676
    - type: nauc_ndcg_at_5_diff1
      value: 16.193847874581166
    - type: nauc_ndcg_at_5_max
      value: -4.471638454091411
    - type: nauc_ndcg_at_5_std
      value: -15.517824617814629
    - type: nauc_precision_at_1000_diff1
      value: 3.170440311533737
    - type: nauc_precision_at_1000_max
      value: 25.521992526080666
    - type: nauc_precision_at_1000_std
      value: 68.4373013145641
    - type: nauc_precision_at_100_diff1
      value: 30.283338663457897
    - type: nauc_precision_at_100_max
      value: 44.33747104624998
    - type: nauc_precision_at_100_std
      value: 42.28887350925609
    - type: nauc_precision_at_10_diff1
      value: 23.390956301235633
    - type: nauc_precision_at_10_max
      value: 15.468288261126773
    - type: nauc_precision_at_10_std
      value: -18.2942744669977
    - type: nauc_precision_at_1_diff1
      value: 16.775859614223965
    - type: nauc_precision_at_1_max
      value: -10.812150486389175
    - type: nauc_precision_at_1_std
      value: -18.447209756110635
    - type: nauc_precision_at_20_diff1
      value: 37.14254275219614
    - type: nauc_precision_at_20_max
      value: 46.984729023754824
    - type: nauc_precision_at_20_std
      value: 22.763524786900717
    - type: nauc_precision_at_3_diff1
      value: 15.651406928218881
    - type: nauc_precision_at_3_max
      value: 0.7775458885343681
    - type: nauc_precision_at_3_std
      value: -12.438132482295773
    - type: nauc_precision_at_5_diff1
      value: 18.10074574210355
    - type: nauc_precision_at_5_max
      value: 9.373350504221532
    - type: nauc_precision_at_5_std
      value: -9.13125987784625
    - type: nauc_recall_at_1000_diff1
      value: 3.1704403115262325
    - type: nauc_recall_at_1000_max
      value: 25.521992526077756
    - type: nauc_recall_at_1000_std
      value: 68.4373013145603
    - type: nauc_recall_at_100_diff1
      value: 30.283338663455616
    - type: nauc_recall_at_100_max
      value: 44.337471046250556
    - type: nauc_recall_at_100_std
      value: 42.28887350925341
    - type: nauc_recall_at_10_diff1
      value: 23.390956301235168
    - type: nauc_recall_at_10_max
      value: 15.468288261126578
    - type: nauc_recall_at_10_std
      value: -18.294274466997873
    - type: nauc_recall_at_1_diff1
      value: 16.775859614223965
    - type: nauc_recall_at_1_max
      value: -10.812150486389175
    - type: nauc_recall_at_1_std
      value: -18.447209756110635
    - type: nauc_recall_at_20_diff1
      value: 37.14254275219513
    - type: nauc_recall_at_20_max
      value: 46.98472902375421
    - type: nauc_recall_at_20_std
      value: 22.763524786899644
    - type: nauc_recall_at_3_diff1
      value: 15.65140692821902
    - type: nauc_recall_at_3_max
      value: 0.7775458885343522
    - type: nauc_recall_at_3_std
      value: -12.43813248229578
    - type: nauc_recall_at_5_diff1
      value: 18.10074574210355
    - type: nauc_recall_at_5_max
      value: 9.373350504221595
    - type: nauc_recall_at_5_std
      value: -9.131259877846116
    - type: ndcg_at_1
      value: 49.004
    - type: ndcg_at_10
      value: 71.99600000000001
    - type: ndcg_at_100
      value: 73.173
    - type: ndcg_at_1000
      value: 73.214
    - type: ndcg_at_20
      value: 72.91
    - type: ndcg_at_3
      value: 65.21900000000001
    - type: ndcg_at_5
      value: 69.284
    - type: precision_at_1
      value: 49.004
    - type: precision_at_10
      value: 9.452
    - type: precision_at_100
      value: 0.9939999999999999
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.904
    - type: precision_at_3
      value: 25.462
    - type: precision_at_5
      value: 17.255000000000003
    - type: recall_at_1
      value: 49.004
    - type: recall_at_10
      value: 94.523
    - type: recall_at_100
      value: 99.36
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_20
      value: 98.08
    - type: recall_at_3
      value: 76.387
    - type: recall_at_5
      value: 86.273
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P (default)
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 48.629569816593516
    - type: v_measure
      value: 48.629569816593516
    - type: v_measure_std
      value: 14.01810149072028
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringS2S (default)
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
      split: test
      type: mteb/arxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 40.52366904677561
    - type: v_measure
      value: 40.52366904677561
    - type: v_measure_std
      value: 14.375876773823757
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AskUbuntuDupQuestions (default)
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
      split: test
      type: mteb/askubuntudupquestions-reranking
    metrics:
    - type: main_score
      value: 61.27347206107508
    - type: map
      value: 61.27347206107508
    - type: mrr
      value: 74.49105219188321
    - type: nAUC_map_diff1
      value: 13.442645655149457
    - type: nAUC_map_max
      value: 25.013363268430027
    - type: nAUC_map_std
      value: 17.60175231611674
    - type: nAUC_mrr_diff1
      value: 25.217675209249435
    - type: nAUC_mrr_max
      value: 32.37381560372622
    - type: nAUC_mrr_std
      value: 22.584922632508412
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB BIOSSES (default)
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: cosine_pearson
      value: 89.09452267906886
    - type: cosine_spearman
      value: 86.73450642504955
    - type: euclidean_pearson
      value: 87.1275130552617
    - type: euclidean_spearman
      value: 86.93812552248012
    - type: main_score
      value: 86.73450642504955
    - type: manhattan_pearson
      value: 86.79403606129864
    - type: manhattan_spearman
      value: 86.76824213349957
    - type: pearson
      value: 89.09452267906886
    - type: spearman
      value: 86.73450642504955
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB Banking77Classification (default)
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
      split: test
      type: mteb/banking77
    metrics:
    - type: accuracy
      value: 88.58116883116884
    - type: f1
      value: 88.54536316207125
    - type: f1_weighted
      value: 88.54536316207125
    - type: main_score
      value: 88.58116883116884
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P (default)
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 44.89554099528695
    - type: v_measure
      value: 44.89554099528695
    - type: v_measure_std
      value: 0.6101675839696261
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringS2S (default)
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
      split: test
      type: mteb/biorxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 37.89775676199564
    - type: v_measure
      value: 37.89775676199564
    - type: v_measure_std
      value: 0.6980439644171996
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CQADupstackAndroidRetrieval (default)
      revision: f46a197baaae43b4f621051089b82a364682dfeb
      split: test
      type: mteb/cqadupstack-android
    metrics:
    - type: main_score
      value: 49.239
    - type: map_at_1
      value: 31.407
    - type: map_at_10
      value: 42.788
    - type: map_at_100
      value: 44.163999999999994
    - type: map_at_1000
      value: 44.285000000000004
    - type: map_at_20
      value: 43.531
    - type: map_at_3
      value: 39.381
    - type: map_at_5
      value: 41.296
    - type: mrr_at_1
      value: 38.91273247496424
    - type: mrr_at_10
      value: 48.82553307446011
    - type: mrr_at_100
      value: 49.5278584841276
    - type: mrr_at_1000
      value: 49.56897938168851
    - type: mrr_at_20
      value: 49.27034318525701
    - type: mrr_at_3
      value: 46.423462088698145
    - type: mrr_at_5
      value: 47.83261802575108
    - type: nauc_map_at_1000_diff1
      value: 51.50772644391144
    - type: nauc_map_at_1000_max
      value: 39.57698592158747
    - type: nauc_map_at_1000_std
      value: -5.092734127689174
    - type: nauc_map_at_100_diff1
      value: 51.51650908644926
    - type: nauc_map_at_100_max
      value: 39.579607215550325
    - type: nauc_map_at_100_std
      value: -5.112306014245407
    - type: nauc_map_at_10_diff1
      value: 51.80732269410239
    - type: nauc_map_at_10_max
      value: 39.312012392020854
    - type: nauc_map_at_10_std
      value: -5.844192947783184
    - type: nauc_map_at_1_diff1
      value: 58.51885994004338
    - type: nauc_map_at_1_max
      value: 35.306905646597656
    - type: nauc_map_at_1_std
      value: -6.4627870729629455
    - type: nauc_map_at_20_diff1
      value: 51.560698537725294
    - type: nauc_map_at_20_max
      value: 39.40865218451427
    - type: nauc_map_at_20_std
      value: -5.46140640509653
    - type: nauc_map_at_3_diff1
      value: 52.845784777873305
    - type: nauc_map_at_3_max
      value: 38.55976877563459
    - type: nauc_map_at_3_std
      value: -5.72430771104222
    - type: nauc_map_at_5_diff1
      value: 52.29343919325049
    - type: nauc_map_at_5_max
      value: 38.98194700024613
    - type: nauc_map_at_5_std
      value: -6.062278166282727
    - type: nauc_mrr_at_1000_diff1
      value: 48.824012243253904
    - type: nauc_mrr_at_1000_max
      value: 40.36119735345816
    - type: nauc_mrr_at_1000_std
      value: -4.371172318529068
    - type: nauc_mrr_at_100_diff1
      value: 48.80142209066577
    - type: nauc_mrr_at_100_max
      value: 40.35371141231279
    - type: nauc_mrr_at_100_std
      value: -4.382000140837231
    - type: nauc_mrr_at_10_diff1
      value: 48.89408963706152
    - type: nauc_mrr_at_10_max
      value: 40.48043029859513
    - type: nauc_mrr_at_10_std
      value: -4.5927306729163835
    - type: nauc_mrr_at_1_diff1
      value: 53.18491414251319
    - type: nauc_mrr_at_1_max
      value: 38.43746618754316
    - type: nauc_mrr_at_1_std
      value: -6.2489159406458965
    - type: nauc_mrr_at_20_diff1
      value: 48.763867640789634
    - type: nauc_mrr_at_20_max
      value: 40.369114351255135
    - type: nauc_mrr_at_20_std
      value: -4.400065130027329
    - type: nauc_mrr_at_3_diff1
      value: 48.87375252127912
    - type: nauc_mrr_at_3_max
      value: 40.810763259212116
    - type: nauc_mrr_at_3_std
      value: -3.4938483699692657
    - type: nauc_mrr_at_5_diff1
      value: 49.186967577714285
    - type: nauc_mrr_at_5_max
      value: 40.48882253846611
    - type: nauc_mrr_at_5_std
      value: -4.621076155915746
    - type: nauc_ndcg_at_1000_diff1
      value: 49.24642669558249
    - type: nauc_ndcg_at_1000_max
      value: 41.00404222082434
    - type: nauc_ndcg_at_1000_std
      value: -2.7356065308278392
    - type: nauc_ndcg_at_100_diff1
      value: 48.92939354546236
    - type: nauc_ndcg_at_100_max
      value: 40.972699158281586
    - type: nauc_ndcg_at_100_std
      value: -3.0561983632108776
    - type: nauc_ndcg_at_10_diff1
      value: 49.60179215238792
    - type: nauc_ndcg_at_10_max
      value: 40.89678771623847
    - type: nauc_ndcg_at_10_std
      value: -5.096633756025252
    - type: nauc_ndcg_at_1_diff1
      value: 53.18491414251319
    - type: nauc_ndcg_at_1_max
      value: 38.43746618754316
    - type: nauc_ndcg_at_1_std
      value: -6.2489159406458965
    - type: nauc_ndcg_at_20_diff1
      value: 48.826483305583984
    - type: nauc_ndcg_at_20_max
      value: 40.592200374154466
    - type: nauc_ndcg_at_20_std
      value: -4.185196398682058
    - type: nauc_ndcg_at_3_diff1
      value: 49.9798291819845
    - type: nauc_ndcg_at_3_max
      value: 40.50211559049151
    - type: nauc_ndcg_at_3_std
      value: -3.9606100546649
    - type: nauc_ndcg_at_5_diff1
      value: 50.222364976292454
    - type: nauc_ndcg_at_5_max
      value: 40.477461845726694
    - type: nauc_ndcg_at_5_std
      value: -5.025922873253527
    - type: nauc_precision_at_1000_diff1
      value: -24.208256297106363
    - type: nauc_precision_at_1000_max
      value: -10.21103761078881
    - type: nauc_precision_at_1000_std
      value: -0.06753142735419307
    - type: nauc_precision_at_100_diff1
      value: -15.392095697703853
    - type: nauc_precision_at_100_max
      value: 3.3764259600400375
    - type: nauc_precision_at_100_std
      value: 7.032273000803224
    - type: nauc_precision_at_10_diff1
      value: 8.050911372676126
    - type: nauc_precision_at_10_max
      value: 26.426542125643365
    - type: nauc_precision_at_10_std
      value: 2.3142807003880423
    - type: nauc_precision_at_1_diff1
      value: 53.18491414251319
    - type: nauc_precision_at_1_max
      value: 38.43746618754316
    - type: nauc_precision_at_1_std
      value: -6.2489159406458965
    - type: nauc_precision_at_20_diff1
      value: -2.4038370945777605
    - type: nauc_precision_at_20_max
      value: 18.29255413962441
    - type: nauc_precision_at_20_std
      value: 6.963786700698579
    - type: nauc_precision_at_3_diff1
      value: 27.590923102137978
    - type: nauc_precision_at_3_max
      value: 36.809716569640635
    - type: nauc_precision_at_3_std
      value: -0.4588749991090731
    - type: nauc_precision_at_5_diff1
      value: 18.31451430104417
    - type: nauc_precision_at_5_max
      value: 31.76792278657563
    - type: nauc_precision_at_5_std
      value: -0.23205753470623663
    - type: nauc_recall_at_1000_diff1
      value: 38.6186488416617
    - type: nauc_recall_at_1000_max
      value: 58.02448766170835
    - type: nauc_recall_at_1000_std
      value: 43.005151313404625
    - type: nauc_recall_at_100_diff1
      value: 36.14901358957452
    - type: nauc_recall_at_100_max
      value: 42.97412072448754
    - type: nauc_recall_at_100_std
      value: 8.434723462734665
    - type: nauc_recall_at_10_diff1
      value: 42.953316965307245
    - type: nauc_recall_at_10_max
      value: 40.54865147159118
    - type: nauc_recall_at_10_std
      value: -4.9425741693714125
    - type: nauc_recall_at_1_diff1
      value: 58.51885994004338
    - type: nauc_recall_at_1_max
      value: 35.306905646597656
    - type: nauc_recall_at_1_std
      value: -6.4627870729629455
    - type: nauc_recall_at_20_diff1
      value: 38.27628659312007
    - type: nauc_recall_at_20_max
      value: 39.50607176714142
    - type: nauc_recall_at_20_std
      value: -1.002089290215587
    - type: nauc_recall_at_3_diff1
      value: 47.263415527062676
    - type: nauc_recall_at_3_max
      value: 40.82836525135613
    - type: nauc_recall_at_3_std
      value: -2.2314232915782504
    - type: nauc_recall_at_5_diff1
      value: 46.13867315478644
    - type: nauc_recall_at_5_max
      value: 39.93028001594826
    - type: nauc_recall_at_5_std
      value: -4.809283400175646
    - type: ndcg_at_1
      value: 38.913
    - type: ndcg_at_10
      value: 49.239
    - type: ndcg_at_100
      value: 54.325
    - type: ndcg_at_1000
      value: 56.226
    - type: ndcg_at_20
      value: 51.212999999999994
    - type: ndcg_at_3
      value: 44.559
    - type: ndcg_at_5
      value: 46.69
    - type: precision_at_1
      value: 38.913
    - type: precision_at_10
      value: 9.227
    - type: precision_at_100
      value: 1.4909999999999999
    - type: precision_at_1000
      value: 0.197
    - type: precision_at_20
      value: 5.494000000000001
    - type: precision_at_3
      value: 21.65
    - type: precision_at_5
      value: 15.336
    - type: recall_at_1
      value: 31.407
    - type: recall_at_10
      value: 61.961999999999996
    - type: recall_at_100
      value: 82.993
    - type: recall_at_1000
      value: 94.887
    - type: recall_at_20
      value: 68.771
    - type: recall_at_3
      value: 47.77
    - type: recall_at_5
      value: 53.895
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackEnglishRetrieval (default)
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
      split: test
      type: mteb/cqadupstack-english
    metrics:
    - type: main_score
      value: 44.391000000000005
    - type: map_at_1
      value: 29.157
    - type: map_at_10
      value: 38.723
    - type: map_at_100
      value: 39.864
    - type: map_at_1000
      value: 39.995999999999995
    - type: map_at_20
      value: 39.287
    - type: map_at_3
      value: 35.751
    - type: map_at_5
      value: 37.373
    - type: mrr_at_1
      value: 36.81528662420382
    - type: mrr_at_10
      value: 44.82939035486806
    - type: mrr_at_100
      value: 45.437834419775484
    - type: mrr_at_1000
      value: 45.48695197590834
    - type: mrr_at_20
      value: 45.15519263295387
    - type: mrr_at_3
      value: 42.55838641188959
    - type: mrr_at_5
      value: 43.87685774946922
    - type: nauc_map_at_1000_diff1
      value: 51.086880931657944
    - type: nauc_map_at_1000_max
      value: 36.870501109568856
    - type: nauc_map_at_1000_std
      value: -9.041748740450098
    - type: nauc_map_at_100_diff1
      value: 51.13349280885669
    - type: nauc_map_at_100_max
      value: 36.81376788959824
    - type: nauc_map_at_100_std
      value: -9.168817557968493
    - type: nauc_map_at_10_diff1
      value: 51.43767101896258
    - type: nauc_map_at_10_max
      value: 36.13512723388837
    - type: nauc_map_at_10_std
      value: -10.340353132146591
    - type: nauc_map_at_1_diff1
      value: 57.97216876426843
    - type: nauc_map_at_1_max
      value: 32.093932122348804
    - type: nauc_map_at_1_std
      value: -12.44326469749823
    - type: nauc_map_at_20_diff1
      value: 51.35742644989209
    - type: nauc_map_at_20_max
      value: 36.362008583908754
    - type: nauc_map_at_20_std
      value: -9.925604455959942
    - type: nauc_map_at_3_diff1
      value: 52.97191265890149
    - type: nauc_map_at_3_max
      value: 35.216095114265
    - type: nauc_map_at_3_std
      value: -11.505843284384989
    - type: nauc_map_at_5_diff1
      value: 52.13435748405322
    - type: nauc_map_at_5_max
      value: 35.63014323147684
    - type: nauc_map_at_5_std
      value: -11.15253714131609
    - type: nauc_mrr_at_1000_diff1
      value: 49.806361508243526
    - type: nauc_mrr_at_1000_max
      value: 39.60825242174082
    - type: nauc_mrr_at_1000_std
      value: -4.581320333963986
    - type: nauc_mrr_at_100_diff1
      value: 49.794023465886575
    - type: nauc_mrr_at_100_max
      value: 39.606036503563935
    - type: nauc_mrr_at_100_std
      value: -4.580524433129927
    - type: nauc_mrr_at_10_diff1
      value: 49.62511317783946
    - type: nauc_mrr_at_10_max
      value: 39.524849843022054
    - type: nauc_mrr_at_10_std
      value: -4.784364837521214
    - type: nauc_mrr_at_1_diff1
      value: 55.03485605539673
    - type: nauc_mrr_at_1_max
      value: 38.26074360694823
    - type: nauc_mrr_at_1_std
      value: -6.990940922024673
    - type: nauc_mrr_at_20_diff1
      value: 49.77823031843402
    - type: nauc_mrr_at_20_max
      value: 39.62943812120721
    - type: nauc_mrr_at_20_std
      value: -4.664971744136187
    - type: nauc_mrr_at_3_diff1
      value: 50.60933103133387
    - type: nauc_mrr_at_3_max
      value: 39.920174010377444
    - type: nauc_mrr_at_3_std
      value: -5.404917304425809
    - type: nauc_mrr_at_5_diff1
      value: 50.137405938227886
    - type: nauc_mrr_at_5_max
      value: 39.7046033416223
    - type: nauc_mrr_at_5_std
      value: -4.9683994219777965
    - type: nauc_ndcg_at_1000_diff1
      value: 48.26320826156127
    - type: nauc_ndcg_at_1000_max
      value: 39.11158925773445
    - type: nauc_ndcg_at_1000_std
      value: -3.958164717220878
    - type: nauc_ndcg_at_100_diff1
      value: 48.29325255469789
    - type: nauc_ndcg_at_100_max
      value: 39.00224428862792
    - type: nauc_ndcg_at_100_std
      value: -4.739309326434606
    - type: nauc_ndcg_at_10_diff1
      value: 48.62405764367444
    - type: nauc_ndcg_at_10_max
      value: 38.04015783804633
    - type: nauc_ndcg_at_10_std
      value: -7.379427256377835
    - type: nauc_ndcg_at_1_diff1
      value: 55.03485605539673
    - type: nauc_ndcg_at_1_max
      value: 38.26074360694823
    - type: nauc_ndcg_at_1_std
      value: -6.990940922024673
    - type: nauc_ndcg_at_20_diff1
      value: 48.793146636748155
    - type: nauc_ndcg_at_20_max
      value: 38.188247609309734
    - type: nauc_ndcg_at_20_std
      value: -6.893163590780488
    - type: nauc_ndcg_at_3_diff1
      value: 49.72527867128085
    - type: nauc_ndcg_at_3_max
      value: 38.397771643337876
    - type: nauc_ndcg_at_3_std
      value: -7.396734926261662
    - type: nauc_ndcg_at_5_diff1
      value: 49.45897046963514
    - type: nauc_ndcg_at_5_max
      value: 38.00788817919171
    - type: nauc_ndcg_at_5_std
      value: -7.98773024373368
    - type: nauc_precision_at_1000_diff1
      value: -15.203088093712378
    - type: nauc_precision_at_1000_max
      value: 13.932931359528938
    - type: nauc_precision_at_1000_std
      value: 28.443903216719125
    - type: nauc_precision_at_100_diff1
      value: -9.833515062825485
    - type: nauc_precision_at_100_max
      value: 25.501133048619252
    - type: nauc_precision_at_100_std
      value: 29.28522368814619
    - type: nauc_precision_at_10_diff1
      value: 11.048052024883837
    - type: nauc_precision_at_10_max
      value: 35.12225756686281
    - type: nauc_precision_at_10_std
      value: 13.549314875239492
    - type: nauc_precision_at_1_diff1
      value: 55.03485605539673
    - type: nauc_precision_at_1_max
      value: 38.26074360694823
    - type: nauc_precision_at_1_std
      value: -6.990940922024673
    - type: nauc_precision_at_20_diff1
      value: 3.6119660166254564
    - type: nauc_precision_at_20_max
      value: 31.80991909502872
    - type: nauc_precision_at_20_std
      value: 19.289172474937768
    - type: nauc_precision_at_3_diff1
      value: 30.93845075141858
    - type: nauc_precision_at_3_max
      value: 41.2363485550859
    - type: nauc_precision_at_3_std
      value: 3.304016059128308
    - type: nauc_precision_at_5_diff1
      value: 22.383511628600537
    - type: nauc_precision_at_5_max
      value: 38.3094647733712
    - type: nauc_precision_at_5_std
      value: 7.010497480008379
    - type: nauc_recall_at_1000_diff1
      value: 31.611750140993035
    - type: nauc_recall_at_1000_max
      value: 42.982693130692894
    - type: nauc_recall_at_1000_std
      value: 25.50352029753317
    - type: nauc_recall_at_100_diff1
      value: 36.466866132011525
    - type: nauc_recall_at_100_max
      value: 39.8896195569174
    - type: nauc_recall_at_100_std
      value: 8.056466272308052
    - type: nauc_recall_at_10_diff1
      value: 40.55869867748143
    - type: nauc_recall_at_10_max
      value: 35.35219000254458
    - type: nauc_recall_at_10_std
      value: -6.935500599977123
    - type: nauc_recall_at_1_diff1
      value: 57.97216876426843
    - type: nauc_recall_at_1_max
      value: 32.093932122348804
    - type: nauc_recall_at_1_std
      value: -12.44326469749823
    - type: nauc_recall_at_20_diff1
      value: 40.699604166249046
    - type: nauc_recall_at_20_max
      value: 36.441366652406835
    - type: nauc_recall_at_20_std
      value: -4.519436682877613
    - type: nauc_recall_at_3_diff1
      value: 47.15019730046201
    - type: nauc_recall_at_3_max
      value: 35.1649979105234
    - type: nauc_recall_at_3_std
      value: -10.908395079450377
    - type: nauc_recall_at_5_diff1
      value: 44.535088248003156
    - type: nauc_recall_at_5_max
      value: 34.89949777715303
    - type: nauc_recall_at_5_std
      value: -10.361237744830412
    - type: ndcg_at_1
      value: 36.815
    - type: ndcg_at_10
      value: 44.391000000000005
    - type: ndcg_at_100
      value: 48.515
    - type: ndcg_at_1000
      value: 50.76199999999999
    - type: ndcg_at_20
      value: 45.788000000000004
    - type: ndcg_at_3
      value: 40.178000000000004
    - type: ndcg_at_5
      value: 42.045
    - type: precision_at_1
      value: 36.815
    - type: precision_at_10
      value: 8.408
    - type: precision_at_100
      value: 1.343
    - type: precision_at_1000
      value: 0.182
    - type: precision_at_20
      value: 4.873
    - type: precision_at_3
      value: 19.299
    - type: precision_at_5
      value: 13.758000000000001
    - type: recall_at_1
      value: 29.157
    - type: recall_at_10
      value: 54.214
    - type: recall_at_100
      value: 71.929
    - type: recall_at_1000
      value: 86.533
    - type: recall_at_20
      value: 59.421
    - type: recall_at_3
      value: 41.569
    - type: recall_at_5
      value: 46.791
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGamingRetrieval (default)
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
      split: test
      type: mteb/cqadupstack-gaming
    metrics:
    - type: main_score
      value: 59.03699999999999
    - type: map_at_1
      value: 41.476
    - type: map_at_10
      value: 53.400000000000006
    - type: map_at_100
      value: 54.452999999999996
    - type: map_at_1000
      value: 54.504
    - type: map_at_20
      value: 54.045
    - type: map_at_3
      value: 50.153999999999996
    - type: map_at_5
      value: 52.079
    - type: mrr_at_1
      value: 46.95924764890282
    - type: mrr_at_10
      value: 56.68495297805642
    - type: mrr_at_100
      value: 57.34582096937295
    - type: mrr_at_1000
      value: 57.37100347158495
    - type: mrr_at_20
      value: 57.10508892444508
    - type: mrr_at_3
      value: 54.242424242424235
    - type: mrr_at_5
      value: 55.76593521421108
    - type: nauc_map_at_1000_diff1
      value: 53.36527106664
    - type: nauc_map_at_1000_max
      value: 43.486776333687835
    - type: nauc_map_at_1000_std
      value: -5.509558143849234
    - type: nauc_map_at_100_diff1
      value: 53.34097797467696
    - type: nauc_map_at_100_max
      value: 43.476003610937234
    - type: nauc_map_at_100_std
      value: -5.520166623777559
    - type: nauc_map_at_10_diff1
      value: 53.432351035276746
    - type: nauc_map_at_10_max
      value: 42.75788423195968
    - type: nauc_map_at_10_std
      value: -6.504192409274652
    - type: nauc_map_at_1_diff1
      value: 57.34963186677463
    - type: nauc_map_at_1_max
      value: 36.95146202384373
    - type: nauc_map_at_1_std
      value: -9.460645936916988
    - type: nauc_map_at_20_diff1
      value: 53.29779847033195
    - type: nauc_map_at_20_max
      value: 43.22342023309121
    - type: nauc_map_at_20_std
      value: -5.953002390034157
    - type: nauc_map_at_3_diff1
      value: 54.09550124289603
    - type: nauc_map_at_3_max
      value: 41.09664412682725
    - type: nauc_map_at_3_std
      value: -8.797917588156473
    - type: nauc_map_at_5_diff1
      value: 53.47735307728038
    - type: nauc_map_at_5_max
      value: 42.1420557369995
    - type: nauc_map_at_5_std
      value: -6.982023249979087
    - type: nauc_mrr_at_1000_diff1
      value: 53.84548396450655
    - type: nauc_mrr_at_1000_max
      value: 45.70711475929243
    - type: nauc_mrr_at_1000_std
      value: -3.572519075485509
    - type: nauc_mrr_at_100_diff1
      value: 53.831585937143345
    - type: nauc_mrr_at_100_max
      value: 45.71866605712688
    - type: nauc_mrr_at_100_std
      value: -3.5531077992494087
    - type: nauc_mrr_at_10_diff1
      value: 53.77550386915942
    - type: nauc_mrr_at_10_max
      value: 45.61906078824265
    - type: nauc_mrr_at_10_std
      value: -3.7647971491069567
    - type: nauc_mrr_at_1_diff1
      value: 57.59578262230993
    - type: nauc_mrr_at_1_max
      value: 43.132298775083996
    - type: nauc_mrr_at_1_std
      value: -6.820570895500843
    - type: nauc_mrr_at_20_diff1
      value: 53.757844034161984
    - type: nauc_mrr_at_20_max
      value: 45.67787807420582
    - type: nauc_mrr_at_20_std
      value: -3.6741549159529816
    - type: nauc_mrr_at_3_diff1
      value: 54.41366916196891
    - type: nauc_mrr_at_3_max
      value: 45.48753195460355
    - type: nauc_mrr_at_3_std
      value: -4.536347261239106
    - type: nauc_mrr_at_5_diff1
      value: 53.81844478829885
    - type: nauc_mrr_at_5_max
      value: 45.77186226917752
    - type: nauc_mrr_at_5_std
      value: -3.560088004877736
    - type: nauc_ndcg_at_1000_diff1
      value: 52.474274223239945
    - type: nauc_ndcg_at_1000_max
      value: 45.88297620389939
    - type: nauc_ndcg_at_1000_std
      value: -2.236689460240769
    - type: nauc_ndcg_at_100_diff1
      value: 51.99537297728399
    - type: nauc_ndcg_at_100_max
      value: 46.162105938598245
    - type: nauc_ndcg_at_100_std
      value: -1.636252027390496
    - type: nauc_ndcg_at_10_diff1
      value: 51.981635840094334
    - type: nauc_ndcg_at_10_max
      value: 44.72098290105285
    - type: nauc_ndcg_at_10_std
      value: -4.26133599970984
    - type: nauc_ndcg_at_1_diff1
      value: 57.43124530432752
    - type: nauc_ndcg_at_1_max
      value: 42.987773648572045
    - type: nauc_ndcg_at_1_std
      value: -6.975930064288375
    - type: nauc_ndcg_at_20_diff1
      value: 51.709989593496665
    - type: nauc_ndcg_at_20_max
      value: 45.35511346806507
    - type: nauc_ndcg_at_20_std
      value: -3.441945043133369
    - type: nauc_ndcg_at_3_diff1
      value: 52.83956836083957
    - type: nauc_ndcg_at_3_max
      value: 43.14243257908553
    - type: nauc_ndcg_at_3_std
      value: -6.906786756066083
    - type: nauc_ndcg_at_5_diff1
      value: 51.92395247597085
    - type: nauc_ndcg_at_5_max
      value: 44.28584104560978
    - type: nauc_ndcg_at_5_std
      value: -4.432556679370336
    - type: nauc_precision_at_1000_diff1
      value: -10.137271271355312
    - type: nauc_precision_at_1000_max
      value: 21.053415390964915
    - type: nauc_precision_at_1000_std
      value: 31.437645188936003
    - type: nauc_precision_at_100_diff1
      value: -5.869005161223761
    - type: nauc_precision_at_100_max
      value: 28.74652505762229
    - type: nauc_precision_at_100_std
      value: 33.42249624017563
    - type: nauc_precision_at_10_diff1
      value: 14.075300860742587
    - type: nauc_precision_at_10_max
      value: 36.90717719533496
    - type: nauc_precision_at_10_std
      value: 15.27522825163519
    - type: nauc_precision_at_1_diff1
      value: 57.43124530432752
    - type: nauc_precision_at_1_max
      value: 42.987773648572045
    - type: nauc_precision_at_1_std
      value: -6.975930064288375
    - type: nauc_precision_at_20_diff1
      value: 4.831146517476065
    - type: nauc_precision_at_20_max
      value: 34.600390709037775
    - type: nauc_precision_at_20_std
      value: 21.879191470976977
    - type: nauc_precision_at_3_diff1
      value: 33.75586535854295
    - type: nauc_precision_at_3_max
      value: 41.8963728460937
    - type: nauc_precision_at_3_std
      value: 0.30853391781218725
    - type: nauc_precision_at_5_diff1
      value: 23.619374234162443
    - type: nauc_precision_at_5_max
      value: 40.26315749312306
    - type: nauc_precision_at_5_std
      value: 9.496779653807806
    - type: nauc_recall_at_1000_diff1
      value: 39.650899433995065
    - type: nauc_recall_at_1000_max
      value: 65.95997046182639
    - type: nauc_recall_at_1000_std
      value: 41.52010213404674
    - type: nauc_recall_at_100_diff1
      value: 37.021652104886904
    - type: nauc_recall_at_100_max
      value: 57.901229136609636
    - type: nauc_recall_at_100_std
      value: 27.173492395498428
    - type: nauc_recall_at_10_diff1
      value: 44.29968361744853
    - type: nauc_recall_at_10_max
      value: 44.18295286662639
    - type: nauc_recall_at_10_std
      value: -1.5721790203147754
    - type: nauc_recall_at_1_diff1
      value: 57.34963186677463
    - type: nauc_recall_at_1_max
      value: 36.95146202384373
    - type: nauc_recall_at_1_std
      value: -9.460645936916988
    - type: nauc_recall_at_20_diff1
      value: 41.603580598985126
    - type: nauc_recall_at_20_max
      value: 47.702934198286876
    - type: nauc_recall_at_20_std
      value: 3.019298754051616
    - type: nauc_recall_at_3_diff1
      value: 49.02194332102533
    - type: nauc_recall_at_3_max
      value: 41.38275177493884
    - type: nauc_recall_at_3_std
      value: -8.055685087264179
    - type: nauc_recall_at_5_diff1
      value: 45.213060998923496
    - type: nauc_recall_at_5_max
      value: 43.53976038303946
    - type: nauc_recall_at_5_std
      value: -1.7312187150046634
    - type: ndcg_at_1
      value: 47.022000000000006
    - type: ndcg_at_10
      value: 59.03699999999999
    - type: ndcg_at_100
      value: 63.077000000000005
    - type: ndcg_at_1000
      value: 64.098
    - type: ndcg_at_20
      value: 60.84
    - type: ndcg_at_3
      value: 53.657999999999994
    - type: ndcg_at_5
      value: 56.501000000000005
    - type: precision_at_1
      value: 47.022000000000006
    - type: precision_at_10
      value: 9.342
    - type: precision_at_100
      value: 1.2309999999999999
    - type: precision_at_1000
      value: 0.136
    - type: precision_at_20
      value: 5.232
    - type: precision_at_3
      value: 23.552999999999997
    - type: precision_at_5
      value: 16.250999999999998
    - type: recall_at_1
      value: 41.476
    - type: recall_at_10
      value: 72.283
    - type: recall_at_100
      value: 89.545
    - type: recall_at_1000
      value: 96.798
    - type: recall_at_20
      value: 78.84100000000001
    - type: recall_at_3
      value: 58.114
    - type: recall_at_5
      value: 65.007
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGisRetrieval (default)
      revision: 5003b3064772da1887988e05400cf3806fe491f2
      split: test
      type: mteb/cqadupstack-gis
    metrics:
    - type: main_score
      value: 37.673
    - type: map_at_1
      value: 25.324
    - type: map_at_10
      value: 33.17
    - type: map_at_100
      value: 34.095
    - type: map_at_1000
      value: 34.182
    - type: map_at_20
      value: 33.654
    - type: map_at_3
      value: 30.879
    - type: map_at_5
      value: 32.26
    - type: mrr_at_1
      value: 27.34463276836158
    - type: mrr_at_10
      value: 35.2258541834813
    - type: mrr_at_100
      value: 36.00404498547979
    - type: mrr_at_1000
      value: 36.07566444493976
    - type: mrr_at_20
      value: 35.63110644891617
    - type: mrr_at_3
      value: 32.95668549905838
    - type: mrr_at_5
      value: 34.25612052730697
    - type: nauc_map_at_1000_diff1
      value: 46.058990680271485
    - type: nauc_map_at_1000_max
      value: 28.600543996662374
    - type: nauc_map_at_1000_std
      value: -3.8218348925653505
    - type: nauc_map_at_100_diff1
      value: 46.04742556273763
    - type: nauc_map_at_100_max
      value: 28.58845010683153
    - type: nauc_map_at_100_std
      value: -3.8241454424665746
    - type: nauc_map_at_10_diff1
      value: 46.318380971509015
    - type: nauc_map_at_10_max
      value: 28.445154969629815
    - type: nauc_map_at_10_std
      value: -4.668418336182435
    - type: nauc_map_at_1_diff1
      value: 50.84712517695217
    - type: nauc_map_at_1_max
      value: 24.956820608742856
    - type: nauc_map_at_1_std
      value: -7.408652214171463
    - type: nauc_map_at_20_diff1
      value: 46.02082882551024
    - type: nauc_map_at_20_max
      value: 28.71729950175136
    - type: nauc_map_at_20_std
      value: -3.8899400482521864
    - type: nauc_map_at_3_diff1
      value: 47.017578094263065
    - type: nauc_map_at_3_max
      value: 27.57393258045568
    - type: nauc_map_at_3_std
      value: -5.578535499711579
    - type: nauc_map_at_5_diff1
      value: 46.64174901816308
    - type: nauc_map_at_5_max
      value: 28.12934751037357
    - type: nauc_map_at_5_std
      value: -4.623605944585039
    - type: nauc_mrr_at_1000_diff1
      value: 44.80745580850706
    - type: nauc_mrr_at_1000_max
      value: 30.08660965092525
    - type: nauc_mrr_at_1000_std
      value: -1.8483739575689273
    - type: nauc_mrr_at_100_diff1
      value: 44.79929065561873
    - type: nauc_mrr_at_100_max
      value: 30.068319004487208
    - type: nauc_mrr_at_100_std
      value: -1.8439865469408845
    - type: nauc_mrr_at_10_diff1
      value: 45.04202172389592
    - type: nauc_mrr_at_10_max
      value: 30.006082516512294
    - type: nauc_mrr_at_10_std
      value: -2.4476357227718673
    - type: nauc_mrr_at_1_diff1
      value: 49.710330210449705
    - type: nauc_mrr_at_1_max
      value: 27.652926800227444
    - type: nauc_mrr_at_1_std
      value: -4.963221847243473
    - type: nauc_mrr_at_20_diff1
      value: 44.74348822631581
    - type: nauc_mrr_at_20_max
      value: 30.232310892837866
    - type: nauc_mrr_at_20_std
      value: -1.8627482467585263
    - type: nauc_mrr_at_3_diff1
      value: 45.63996732955718
    - type: nauc_mrr_at_3_max
      value: 29.71071543929027
    - type: nauc_mrr_at_3_std
      value: -2.9488868732728264
    - type: nauc_mrr_at_5_diff1
      value: 45.31282418942023
    - type: nauc_mrr_at_5_max
      value: 29.59225270015164
    - type: nauc_mrr_at_5_std
      value: -2.571596169990907
    - type: nauc_ndcg_at_1000_diff1
      value: 43.44153526801899
    - type: nauc_ndcg_at_1000_max
      value: 30.264809827186745
    - type: nauc_ndcg_at_1000_std
      value: -0.3673459026557417
    - type: nauc_ndcg_at_100_diff1
      value: 42.9260780049435
    - type: nauc_ndcg_at_100_max
      value: 29.971290021267254
    - type: nauc_ndcg_at_100_std
      value: 0.07223943237736839
    - type: nauc_ndcg_at_10_diff1
      value: 43.89936991271991
    - type: nauc_ndcg_at_10_max
      value: 29.883246789724915
    - type: nauc_ndcg_at_10_std
      value: -2.842441401911265
    - type: nauc_ndcg_at_1_diff1
      value: 50.14865712693543
    - type: nauc_ndcg_at_1_max
      value: 27.111609058341863
    - type: nauc_ndcg_at_1_std
      value: -5.5675174385570925
    - type: nauc_ndcg_at_20_diff1
      value: 42.84709307426253
    - type: nauc_ndcg_at_20_max
      value: 30.76378099168594
    - type: nauc_ndcg_at_20_std
      value: -0.42561135386508475
    - type: nauc_ndcg_at_3_diff1
      value: 45.4326566931524
    - type: nauc_ndcg_at_3_max
      value: 28.61889737624481
    - type: nauc_ndcg_at_3_std
      value: -4.348200281698876
    - type: nauc_ndcg_at_5_diff1
      value: 44.630092727271034
    - type: nauc_ndcg_at_5_max
      value: 29.04891878562973
    - type: nauc_ndcg_at_5_std
      value: -2.8900608482934165
    - type: nauc_precision_at_1000_diff1
      value: 1.563823692486198
    - type: nauc_precision_at_1000_max
      value: 18.07524759715147
    - type: nauc_precision_at_1000_std
      value: 10.75651488435518
    - type: nauc_precision_at_100_diff1
      value: 15.84032553897459
    - type: nauc_precision_at_100_max
      value: 26.9982332859951
    - type: nauc_precision_at_100_std
      value: 13.809307316031362
    - type: nauc_precision_at_10_diff1
      value: 33.44005568824001
    - type: nauc_precision_at_10_max
      value: 35.31365313654245
    - type: nauc_precision_at_10_std
      value: 2.1516208493844817
    - type: nauc_precision_at_1_diff1
      value: 50.14865712693543
    - type: nauc_precision_at_1_max
      value: 27.111609058341863
    - type: nauc_precision_at_1_std
      value: -5.5675174385570925
    - type: nauc_precision_at_20_diff1
      value: 26.453560867406594
    - type: nauc_precision_at_20_max
      value: 36.754320258234735
    - type: nauc_precision_at_20_std
      value: 10.960004664156314
    - type: nauc_precision_at_3_diff1
      value: 39.5339842087826
    - type: nauc_precision_at_3_max
      value: 32.43079763654043
    - type: nauc_precision_at_3_std
      value: -1.1149107052174205
    - type: nauc_precision_at_5_diff1
      value: 36.75997042257077
    - type: nauc_precision_at_5_max
      value: 32.936394052992256
    - type: nauc_precision_at_5_std
      value: 2.253739058194602
    - type: nauc_recall_at_1000_diff1
      value: 26.620883791876672
    - type: nauc_recall_at_1000_max
      value: 40.036249354126255
    - type: nauc_recall_at_1000_std
      value: 24.67019914079094
    - type: nauc_recall_at_100_diff1
      value: 29.06050311303032
    - type: nauc_recall_at_100_max
      value: 31.719103788027674
    - type: nauc_recall_at_100_std
      value: 16.517714390661105
    - type: nauc_recall_at_10_diff1
      value: 36.292924258716106
    - type: nauc_recall_at_10_max
      value: 32.02173242085442
    - type: nauc_recall_at_10_std
      value: 1.016713326361783
    - type: nauc_recall_at_1_diff1
      value: 50.84712517695217
    - type: nauc_recall_at_1_max
      value: 24.956820608742856
    - type: nauc_recall_at_1_std
      value: -7.408652214171463
    - type: nauc_recall_at_20_diff1
      value: 31.875810510992398
    - type: nauc_recall_at_20_max
      value: 35.1225435012755
    - type: nauc_recall_at_20_std
      value: 10.08081240374867
    - type: nauc_recall_at_3_diff1
      value: 41.31843254728666
    - type: nauc_recall_at_3_max
      value: 29.083015930837323
    - type: nauc_recall_at_3_std
      value: -2.6812306676938906
    - type: nauc_recall_at_5_diff1
      value: 38.74912094651174
    - type: nauc_recall_at_5_max
      value: 29.713413529317663
    - type: nauc_recall_at_5_std
      value: 0.6429485746621083
    - type: ndcg_at_1
      value: 27.232
    - type: ndcg_at_10
      value: 37.673
    - type: ndcg_at_100
      value: 42.379
    - type: ndcg_at_1000
      value: 44.664
    - type: ndcg_at_20
      value: 39.282000000000004
    - type: ndcg_at_3
      value: 33.178999999999995
    - type: ndcg_at_5
      value: 35.481
    - type: precision_at_1
      value: 27.232
    - type: precision_at_10
      value: 5.593
    - type: precision_at_100
      value: 0.845
    - type: precision_at_1000
      value: 0.108
    - type: precision_at_20
      value: 3.1809999999999996
    - type: precision_at_3
      value: 13.898
    - type: precision_at_5
      value: 9.605
    - type: recall_at_1
      value: 25.324
    - type: recall_at_10
      value: 49.66
    - type: recall_at_100
      value: 71.702
    - type: recall_at_1000
      value: 88.884
    - type: recall_at_20
      value: 55.63399999999999
    - type: recall_at_3
      value: 37.557
    - type: recall_at_5
      value: 43.086
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackMathematicaRetrieval (default)
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
      split: test
      type: mteb/cqadupstack-mathematica
    metrics:
    - type: main_score
      value: 27.683000000000003
    - type: map_at_1
      value: 15.440000000000001
    - type: map_at_10
      value: 22.708000000000002
    - type: map_at_100
      value: 23.891000000000002
    - type: map_at_1000
      value: 24.009
    - type: map_at_20
      value: 23.362
    - type: map_at_3
      value: 20.173
    - type: map_at_5
      value: 21.512999999999998
    - type: mrr_at_1
      value: 19.154228855721392
    - type: mrr_at_10
      value: 27.14907604832978
    - type: mrr_at_100
      value: 28.134401799106946
    - type: mrr_at_1000
      value: 28.210652971960727
    - type: mrr_at_20
      value: 27.743116715423334
    - type: mrr_at_3
      value: 24.64759535655058
    - type: mrr_at_5
      value: 26.0530679933665
    - type: nauc_map_at_1000_diff1
      value: 26.45225395954919
    - type: nauc_map_at_1000_max
      value: 18.88821201176001
    - type: nauc_map_at_1000_std
      value: -6.743073428818526
    - type: nauc_map_at_100_diff1
      value: 26.46163797092885
    - type: nauc_map_at_100_max
      value: 18.91020517272631
    - type: nauc_map_at_100_std
      value: -6.715512753190824
    - type: nauc_map_at_10_diff1
      value: 25.93830061738008
    - type: nauc_map_at_10_max
      value: 18.230821464212788
    - type: nauc_map_at_10_std
      value: -7.723714557953293
    - type: nauc_map_at_1_diff1
      value: 32.6143819833978
    - type: nauc_map_at_1_max
      value: 18.229434406703447
    - type: nauc_map_at_1_std
      value: -8.826503266807608
    - type: nauc_map_at_20_diff1
      value: 26.267375356189532
    - type: nauc_map_at_20_max
      value: 18.74372577827996
    - type: nauc_map_at_20_std
      value: -7.1213741256387495
    - type: nauc_map_at_3_diff1
      value: 26.502658255222222
    - type: nauc_map_at_3_max
      value: 17.34676548965769
    - type: nauc_map_at_3_std
      value: -8.661705532483479
    - type: nauc_map_at_5_diff1
      value: 25.947975266973
    - type: nauc_map_at_5_max
      value: 18.26579025252041
    - type: nauc_map_at_5_std
      value: -7.988152286698193
    - type: nauc_mrr_at_1000_diff1
      value: 27.43240261182634
    - type: nauc_mrr_at_1000_max
      value: 19.59851548113691
    - type: nauc_mrr_at_1000_std
      value: -5.8659045748819505
    - type: nauc_mrr_at_100_diff1
      value: 27.42860371902458
    - type: nauc_mrr_at_100_max
      value: 19.61291439961396
    - type: nauc_mrr_at_100_std
      value: -5.840170365425997
    - type: nauc_mrr_at_10_diff1
      value: 26.996629286135576
    - type: nauc_mrr_at_10_max
      value: 19.09125992187832
    - type: nauc_mrr_at_10_std
      value: -6.401949732007706
    - type: nauc_mrr_at_1_diff1
      value: 33.20355103883785
    - type: nauc_mrr_at_1_max
      value: 18.84271700427976
    - type: nauc_mrr_at_1_std
      value: -6.846362536084065
    - type: nauc_mrr_at_20_diff1
      value: 27.342295700872445
    - type: nauc_mrr_at_20_max
      value: 19.59730195635629
    - type: nauc_mrr_at_20_std
      value: -6.045183866074472
    - type: nauc_mrr_at_3_diff1
      value: 27.921898978571868
    - type: nauc_mrr_at_3_max
      value: 19.028747822887816
    - type: nauc_mrr_at_3_std
      value: -6.651966049443023
    - type: nauc_mrr_at_5_diff1
      value: 27.280695824148392
    - type: nauc_mrr_at_5_max
      value: 19.430798343725524
    - type: nauc_mrr_at_5_std
      value: -6.747383339145715
    - type: nauc_ndcg_at_1000_diff1
      value: 25.38902736172073
    - type: nauc_ndcg_at_1000_max
      value: 20.45917423943934
    - type: nauc_ndcg_at_1000_std
      value: -3.2757947022252076
    - type: nauc_ndcg_at_100_diff1
      value: 25.732803165259238
    - type: nauc_ndcg_at_100_max
      value: 20.836040539884642
    - type: nauc_ndcg_at_100_std
      value: -2.9535785746014396
    - type: nauc_ndcg_at_10_diff1
      value: 23.946041122415746
    - type: nauc_ndcg_at_10_max
      value: 18.62752297015455
    - type: nauc_ndcg_at_10_std
      value: -6.405272980276195
    - type: nauc_ndcg_at_1_diff1
      value: 33.20355103883785
    - type: nauc_ndcg_at_1_max
      value: 18.84271700427976
    - type: nauc_ndcg_at_1_std
      value: -6.846362536084065
    - type: nauc_ndcg_at_20_diff1
      value: 24.77178243398418
    - type: nauc_ndcg_at_20_max
      value: 20.27057276120682
    - type: nauc_ndcg_at_20_std
      value: -4.789054638686646
    - type: nauc_ndcg_at_3_diff1
      value: 25.93797698971861
    - type: nauc_ndcg_at_3_max
      value: 17.7626073837572
    - type: nauc_ndcg_at_3_std
      value: -8.049324539903097
    - type: nauc_ndcg_at_5_diff1
      value: 24.628424554881647
    - type: nauc_ndcg_at_5_max
      value: 18.989213649165613
    - type: nauc_ndcg_at_5_std
      value: -7.173452770970873
    - type: nauc_precision_at_1000_diff1
      value: 5.456508320365408
    - type: nauc_precision_at_1000_max
      value: 4.8136815217087205
    - type: nauc_precision_at_1000_std
      value: 4.947456448109757
    - type: nauc_precision_at_100_diff1
      value: 16.260577000896543
    - type: nauc_precision_at_100_max
      value: 16.7039900850556
    - type: nauc_precision_at_100_std
      value: 9.11227641718042
    - type: nauc_precision_at_10_diff1
      value: 16.365122567702535
    - type: nauc_precision_at_10_max
      value: 17.065003280187348
    - type: nauc_precision_at_10_std
      value: -2.229290931287804
    - type: nauc_precision_at_1_diff1
      value: 33.20355103883785
    - type: nauc_precision_at_1_max
      value: 18.84271700427976
    - type: nauc_precision_at_1_std
      value: -6.846362536084065
    - type: nauc_precision_at_20_diff1
      value: 16.91214381595962
    - type: nauc_precision_at_20_max
      value: 19.58308083494222
    - type: nauc_precision_at_20_std
      value: 2.253335365165219
    - type: nauc_precision_at_3_diff1
      value: 19.85085379824151
    - type: nauc_precision_at_3_max
      value: 16.27352732420782
    - type: nauc_precision_at_3_std
      value: -7.201882607059234
    - type: nauc_precision_at_5_diff1
      value: 17.966240404329092
    - type: nauc_precision_at_5_max
      value: 18.231425958226044
    - type: nauc_precision_at_5_std
      value: -4.043751510938105
    - type: nauc_recall_at_1000_diff1
      value: 13.957143176090353
    - type: nauc_recall_at_1000_max
      value: 25.052247631159652
    - type: nauc_recall_at_1000_std
      value: 17.326355613640054
    - type: nauc_recall_at_100_diff1
      value: 21.440869340994407
    - type: nauc_recall_at_100_max
      value: 24.311867728047343
    - type: nauc_recall_at_100_std
      value: 9.336321796584325
    - type: nauc_recall_at_10_diff1
      value: 16.696814266222432
    - type: nauc_recall_at_10_max
      value: 17.145710052014486
    - type: nauc_recall_at_10_std
      value: -4.135339167818864
    - type: nauc_recall_at_1_diff1
      value: 32.6143819833978
    - type: nauc_recall_at_1_max
      value: 18.229434406703447
    - type: nauc_recall_at_1_std
      value: -8.826503266807608
    - type: nauc_recall_at_20_diff1
      value: 18.34311797149379
    - type: nauc_recall_at_20_max
      value: 21.832943514273143
    - type: nauc_recall_at_20_std
      value: 0.8894706565637946
    - type: nauc_recall_at_3_diff1
      value: 20.992985988081557
    - type: nauc_recall_at_3_max
      value: 16.255791972442506
    - type: nauc_recall_at_3_std
      value: -7.097037821828232
    - type: nauc_recall_at_5_diff1
      value: 18.60326978035633
    - type: nauc_recall_at_5_max
      value: 18.615371576760275
    - type: nauc_recall_at_5_std
      value: -6.049891295196573
    - type: ndcg_at_1
      value: 19.154
    - type: ndcg_at_10
      value: 27.683000000000003
    - type: ndcg_at_100
      value: 33.213
    - type: ndcg_at_1000
      value: 36.141
    - type: ndcg_at_20
      value: 29.854999999999997
    - type: ndcg_at_3
      value: 22.987
    - type: ndcg_at_5
      value: 25.106
    - type: precision_at_1
      value: 19.154
    - type: precision_at_10
      value: 5.224
    - type: precision_at_100
      value: 0.919
    - type: precision_at_1000
      value: 0.13
    - type: precision_at_20
      value: 3.215
    - type: precision_at_3
      value: 11.318
    - type: precision_at_5
      value: 8.383000000000001
    - type: recall_at_1
      value: 15.440000000000001
    - type: recall_at_10
      value: 38.734
    - type: recall_at_100
      value: 62.576
    - type: recall_at_1000
      value: 83.541
    - type: recall_at_20
      value: 46.45
    - type: recall_at_3
      value: 25.438
    - type: recall_at_5
      value: 30.891000000000002
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackPhysicsRetrieval (default)
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
      split: test
      type: mteb/cqadupstack-physics
    metrics:
    - type: main_score
      value: 45.196999999999996
    - type: map_at_1
      value: 29.438
    - type: map_at_10
      value: 39.497
    - type: map_at_100
      value: 40.757
    - type: map_at_1000
      value: 40.865
    - type: map_at_20
      value: 40.21
    - type: map_at_3
      value: 36.649
    - type: map_at_5
      value: 38.278
    - type: mrr_at_1
      value: 35.514918190567855
    - type: mrr_at_10
      value: 44.939158531555066
    - type: mrr_at_100
      value: 45.71399223764184
    - type: mrr_at_1000
      value: 45.767047236444185
    - type: mrr_at_20
      value: 45.40064162616659
    - type: mrr_at_3
      value: 42.49278152069297
    - type: mrr_at_5
      value: 43.999037536092395
    - type: nauc_map_at_1000_diff1
      value: 48.2911083967695
    - type: nauc_map_at_1000_max
      value: 33.0567223033294
    - type: nauc_map_at_1000_std
      value: -7.5831018828087435
    - type: nauc_map_at_100_diff1
      value: 48.266195527072156
    - type: nauc_map_at_100_max
      value: 33.03915960499412
    - type: nauc_map_at_100_std
      value: -7.606925986310037
    - type: nauc_map_at_10_diff1
      value: 48.328320797346294
    - type: nauc_map_at_10_max
      value: 32.7070148720631
    - type: nauc_map_at_10_std
      value: -8.512811841258646
    - type: nauc_map_at_1_diff1
      value: 52.88608162356222
    - type: nauc_map_at_1_max
      value: 31.24794941358492
    - type: nauc_map_at_1_std
      value: -11.706848009285954
    - type: nauc_map_at_20_diff1
      value: 48.2969260156472
    - type: nauc_map_at_20_max
      value: 32.86081996380274
    - type: nauc_map_at_20_std
      value: -8.020958942798524
    - type: nauc_map_at_3_diff1
      value: 48.743817641945114
    - type: nauc_map_at_3_max
      value: 32.605458230621856
    - type: nauc_map_at_3_std
      value: -8.638274842287737
    - type: nauc_map_at_5_diff1
      value: 48.78806923732555
    - type: nauc_map_at_5_max
      value: 32.61566250570677
    - type: nauc_map_at_5_std
      value: -8.780064299161241
    - type: nauc_mrr_at_1000_diff1
      value: 48.402407250061934
    - type: nauc_mrr_at_1000_max
      value: 32.73963018253408
    - type: nauc_mrr_at_1000_std
      value: -7.600714897746363
    - type: nauc_mrr_at_100_diff1
      value: 48.38722402499983
    - type: nauc_mrr_at_100_max
      value: 32.74291939054888
    - type: nauc_mrr_at_100_std
      value: -7.584196436282831
    - type: nauc_mrr_at_10_diff1
      value: 48.324992370558576
    - type: nauc_mrr_at_10_max
      value: 32.65326566012142
    - type: nauc_mrr_at_10_std
      value: -7.960957871756174
    - type: nauc_mrr_at_1_diff1
      value: 52.51790849738347
    - type: nauc_mrr_at_1_max
      value: 31.979743734335504
    - type: nauc_mrr_at_1_std
      value: -11.101383949942232
    - type: nauc_mrr_at_20_diff1
      value: 48.375346158446725
    - type: nauc_mrr_at_20_max
      value: 32.73895555822591
    - type: nauc_mrr_at_20_std
      value: -7.642914670396977
    - type: nauc_mrr_at_3_diff1
      value: 48.83160990949774
    - type: nauc_mrr_at_3_max
      value: 32.80880922901924
    - type: nauc_mrr_at_3_std
      value: -7.760362168094019
    - type: nauc_mrr_at_5_diff1
      value: 48.60255139323125
    - type: nauc_mrr_at_5_max
      value: 32.72728351371156
    - type: nauc_mrr_at_5_std
      value: -8.038189749481258
    - type: nauc_ndcg_at_1000_diff1
      value: 46.67101320125475
    - type: nauc_ndcg_at_1000_max
      value: 34.0504701772667
    - type: nauc_ndcg_at_1000_std
      value: -4.032878112637376
    - type: nauc_ndcg_at_100_diff1
      value: 46.248748827447265
    - type: nauc_ndcg_at_100_max
      value: 33.74751928599088
    - type: nauc_ndcg_at_100_std
      value: -3.991862266355337
    - type: nauc_ndcg_at_10_diff1
      value: 46.46100196084458
    - type: nauc_ndcg_at_10_max
      value: 32.807685888284794
    - type: nauc_ndcg_at_10_std
      value: -7.457478747984192
    - type: nauc_ndcg_at_1_diff1
      value: 52.51790849738347
    - type: nauc_ndcg_at_1_max
      value: 31.979743734335504
    - type: nauc_ndcg_at_1_std
      value: -11.101383949942232
    - type: nauc_ndcg_at_20_diff1
      value: 46.410656199509944
    - type: nauc_ndcg_at_20_max
      value: 33.1581309808876
    - type: nauc_ndcg_at_20_std
      value: -5.99183846380811
    - type: nauc_ndcg_at_3_diff1
      value: 47.26764972559635
    - type: nauc_ndcg_at_3_max
      value: 33.08614197399897
    - type: nauc_ndcg_at_3_std
      value: -7.0742507391341345
    - type: nauc_ndcg_at_5_diff1
      value: 47.35898227835041
    - type: nauc_ndcg_at_5_max
      value: 32.84468179240444
    - type: nauc_ndcg_at_5_std
      value: -7.714927192881523
    - type: nauc_precision_at_1000_diff1
      value: -9.52692395683019
    - type: nauc_precision_at_1000_max
      value: 7.374303479576268
    - type: nauc_precision_at_1000_std
      value: 20.79761650113592
    - type: nauc_precision_at_100_diff1
      value: -0.5511806256392863
    - type: nauc_precision_at_100_max
      value: 14.260122126630634
    - type: nauc_precision_at_100_std
      value: 20.84530821188996
    - type: nauc_precision_at_10_diff1
      value: 19.572115874106533
    - type: nauc_precision_at_10_max
      value: 24.556082924046027
    - type: nauc_precision_at_10_std
      value: 5.323857400679805
    - type: nauc_precision_at_1_diff1
      value: 52.51790849738347
    - type: nauc_precision_at_1_max
      value: 31.979743734335504
    - type: nauc_precision_at_1_std
      value: -11.101383949942232
    - type: nauc_precision_at_20_diff1
      value: 12.356576945971826
    - type: nauc_precision_at_20_max
      value: 21.121689225096056
    - type: nauc_precision_at_20_std
      value: 12.177075559439556
    - type: nauc_precision_at_3_diff1
      value: 33.671667659871865
    - type: nauc_precision_at_3_max
      value: 30.98143183174062
    - type: nauc_precision_at_3_std
      value: 0.520604608152502
    - type: nauc_precision_at_5_diff1
      value: 30.06980809430162
    - type: nauc_precision_at_5_max
      value: 28.454115294663602
    - type: nauc_precision_at_5_std
      value: 0.8596400708828538
    - type: nauc_recall_at_1000_diff1
      value: 24.965587031650884
    - type: nauc_recall_at_1000_max
      value: 40.72840120992986
    - type: nauc_recall_at_1000_std
      value: 38.76857796467627
    - type: nauc_recall_at_100_diff1
      value: 32.790892696170374
    - type: nauc_recall_at_100_max
      value: 32.970070123139564
    - type: nauc_recall_at_100_std
      value: 14.657654854897062
    - type: nauc_recall_at_10_diff1
      value: 38.309181873423476
    - type: nauc_recall_at_10_max
      value: 30.28707855794435
    - type: nauc_recall_at_10_std
      value: -5.568997608502203
    - type: nauc_recall_at_1_diff1
      value: 52.88608162356222
    - type: nauc_recall_at_1_max
      value: 31.24794941358492
    - type: nauc_recall_at_1_std
      value: -11.706848009285954
    - type: nauc_recall_at_20_diff1
      value: 37.44816940285688
    - type: nauc_recall_at_20_max
      value: 31.24736990052554
    - type: nauc_recall_at_20_std
      value: -0.17027260910961897
    - type: nauc_recall_at_3_diff1
      value: 42.921582034772726
    - type: nauc_recall_at_3_max
      value: 31.861184780950513
    - type: nauc_recall_at_3_std
      value: -6.209754089638474
    - type: nauc_recall_at_5_diff1
      value: 41.74803396821156
    - type: nauc_recall_at_5_max
      value: 31.13023590637421
    - type: nauc_recall_at_5_std
      value: -6.608370086504567
    - type: ndcg_at_1
      value: 35.515
    - type: ndcg_at_10
      value: 45.196999999999996
    - type: ndcg_at_100
      value: 50.38399999999999
    - type: ndcg_at_1000
      value: 52.596
    - type: ndcg_at_20
      value: 47.233000000000004
    - type: ndcg_at_3
      value: 40.573
    - type: ndcg_at_5
      value: 42.853
    - type: precision_at_1
      value: 35.515
    - type: precision_at_10
      value: 8.017000000000001
    - type: precision_at_100
      value: 1.237
    - type: precision_at_1000
      value: 0.159
    - type: precision_at_20
      value: 4.687
    - type: precision_at_3
      value: 18.961
    - type: precision_at_5
      value: 13.34
    - type: recall_at_1
      value: 29.438
    - type: recall_at_10
      value: 56.603
    - type: recall_at_100
      value: 78.281
    - type: recall_at_1000
      value: 93.172
    - type: recall_at_20
      value: 63.571
    - type: recall_at_3
      value: 43.763000000000005
    - type: recall_at_5
      value: 49.717
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackProgrammersRetrieval (default)
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
      split: test
      type: mteb/cqadupstack-programmers
    metrics:
    - type: main_score
      value: 41.967999999999996
    - type: map_at_1
      value: 27.991
    - type: map_at_10
      value: 36.815
    - type: map_at_100
      value: 38.14
    - type: map_at_1000
      value: 38.257999999999996
    - type: map_at_20
      value: 37.561
    - type: map_at_3
      value: 34.094
    - type: map_at_5
      value: 35.557
    - type: mrr_at_1
      value: 34.817351598173516
    - type: mrr_at_10
      value: 42.56500507356672
    - type: mrr_at_100
      value: 43.460463999764066
    - type: mrr_at_1000
      value: 43.52348583643295
    - type: mrr_at_20
      value: 43.11992252647868
    - type: mrr_at_3
      value: 40.20167427701675
    - type: mrr_at_5
      value: 41.45738203957382
    - type: nauc_map_at_1000_diff1
      value: 41.67048775212967
    - type: nauc_map_at_1000_max
      value: 43.99159244124849
    - type: nauc_map_at_1000_std
      value: 2.573128018829387
    - type: nauc_map_at_100_diff1
      value: 41.674051168864544
    - type: nauc_map_at_100_max
      value: 43.98147916359051
    - type: nauc_map_at_100_std
      value: 2.5254111056725157
    - type: nauc_map_at_10_diff1
      value: 41.7125704403198
    - type: nauc_map_at_10_max
      value: 43.474100183989364
    - type: nauc_map_at_10_std
      value: 1.6477791314522445
    - type: nauc_map_at_1_diff1
      value: 48.1867206901292
    - type: nauc_map_at_1_max
      value: 40.525641468978996
    - type: nauc_map_at_1_std
      value: -0.7568533902855162
    - type: nauc_map_at_20_diff1
      value: 41.64339598055937
    - type: nauc_map_at_20_max
      value: 43.62356989148736
    - type: nauc_map_at_20_std
      value: 2.087731774178381
    - type: nauc_map_at_3_diff1
      value: 43.473195638597325
    - type: nauc_map_at_3_max
      value: 42.94377216167118
    - type: nauc_map_at_3_std
      value: 0.2505945238603998
    - type: nauc_map_at_5_diff1
      value: 42.39542158097317
    - type: nauc_map_at_5_max
      value: 43.67892698262521
    - type: nauc_map_at_5_std
      value: 0.9895905882223653
    - type: nauc_mrr_at_1000_diff1
      value: 41.09671003865924
    - type: nauc_mrr_at_1000_max
      value: 46.28436379929593
    - type: nauc_mrr_at_1000_std
      value: 4.354037919152363
    - type: nauc_mrr_at_100_diff1
      value: 41.09244756994191
    - type: nauc_mrr_at_100_max
      value: 46.29034043110901
    - type: nauc_mrr_at_100_std
      value: 4.351726070204726
    - type: nauc_mrr_at_10_diff1
      value: 40.977946444819096
    - type: nauc_mrr_at_10_max
      value: 46.10718374892125
    - type: nauc_mrr_at_10_std
      value: 4.18336707456262
    - type: nauc_mrr_at_1_diff1
      value: 45.599332453292675
    - type: nauc_mrr_at_1_max
      value: 45.84726261326186
    - type: nauc_mrr_at_1_std
      value: 2.4345971000548854
    - type: nauc_mrr_at_20_diff1
      value: 40.95961993815576
    - type: nauc_mrr_at_20_max
      value: 46.18592650660265
    - type: nauc_mrr_at_20_std
      value: 4.305161755438331
    - type: nauc_mrr_at_3_diff1
      value: 42.32692907673492
    - type: nauc_mrr_at_3_max
      value: 46.26011359406279
    - type: nauc_mrr_at_3_std
      value: 2.948567577936104
    - type: nauc_mrr_at_5_diff1
      value: 41.34052580040367
    - type: nauc_mrr_at_5_max
      value: 46.34383226431204
    - type: nauc_mrr_at_5_std
      value: 3.633823850306508
    - type: nauc_ndcg_at_1000_diff1
      value: 39.93215369321293
    - type: nauc_ndcg_at_1000_max
      value: 45.687802170808574
    - type: nauc_ndcg_at_1000_std
      value: 6.430986118631789
    - type: nauc_ndcg_at_100_diff1
      value: 39.684859990483915
    - type: nauc_ndcg_at_100_max
      value: 45.80031091479213
    - type: nauc_ndcg_at_100_std
      value: 6.36066573145881
    - type: nauc_ndcg_at_10_diff1
      value: 39.23880630958678
    - type: nauc_ndcg_at_10_max
      value: 43.80038181935968
    - type: nauc_ndcg_at_10_std
      value: 3.3533556819103074
    - type: nauc_ndcg_at_1_diff1
      value: 45.94736367846991
    - type: nauc_ndcg_at_1_max
      value: 46.105763729560294
    - type: nauc_ndcg_at_1_std
      value: 2.5515460950343622
    - type: nauc_ndcg_at_20_diff1
      value: 39.077143576829634
    - type: nauc_ndcg_at_20_max
      value: 44.175755846357006
    - type: nauc_ndcg_at_20_std
      value: 4.5499430823825
    - type: nauc_ndcg_at_3_diff1
      value: 41.55043893779763
    - type: nauc_ndcg_at_3_max
      value: 44.369396288268
    - type: nauc_ndcg_at_3_std
      value: 1.8135062317910333
    - type: nauc_ndcg_at_5_diff1
      value: 40.27727274546977
    - type: nauc_ndcg_at_5_max
      value: 44.58055714919917
    - type: nauc_ndcg_at_5_std
      value: 2.3858438655025895
    - type: nauc_precision_at_1000_diff1
      value: -15.82921590565681
    - type: nauc_precision_at_1000_max
      value: 5.3200324911551276
    - type: nauc_precision_at_1000_std
      value: 17.059441605068066
    - type: nauc_precision_at_100_diff1
      value: -3.477661270951154
    - type: nauc_precision_at_100_max
      value: 23.102213467508363
    - type: nauc_precision_at_100_std
      value: 22.61050030511951
    - type: nauc_precision_at_10_diff1
      value: 13.022774804120216
    - type: nauc_precision_at_10_max
      value: 38.41004452998074
    - type: nauc_precision_at_10_std
      value: 15.569153607416283
    - type: nauc_precision_at_1_diff1
      value: 45.94736367846991
    - type: nauc_precision_at_1_max
      value: 46.105763729560294
    - type: nauc_precision_at_1_std
      value: 2.5515460950343622
    - type: nauc_precision_at_20_diff1
      value: 6.552231339783917
    - type: nauc_precision_at_20_max
      value: 33.144348451578914
    - type: nauc_precision_at_20_std
      value: 19.55599724769983
    - type: nauc_precision_at_3_diff1
      value: 28.52937551899466
    - type: nauc_precision_at_3_max
      value: 45.2056127705799
    - type: nauc_precision_at_3_std
      value: 7.5353087497146785
    - type: nauc_precision_at_5_diff1
      value: 21.680390063172492
    - type: nauc_precision_at_5_max
      value: 44.075542142279645
    - type: nauc_precision_at_5_std
      value: 10.933211341141087
    - type: nauc_recall_at_1000_diff1
      value: 31.550619753305593
    - type: nauc_recall_at_1000_max
      value: 49.1096811911254
    - type: nauc_recall_at_1000_std
      value: 39.51532818925666
    - type: nauc_recall_at_100_diff1
      value: 30.696662503429863
    - type: nauc_recall_at_100_max
      value: 47.21608565384206
    - type: nauc_recall_at_100_std
      value: 20.894556840831438
    - type: nauc_recall_at_10_diff1
      value: 30.61623779072834
    - type: nauc_recall_at_10_max
      value: 38.964392138468114
    - type: nauc_recall_at_10_std
      value: 5.00024473264126
    - type: nauc_recall_at_1_diff1
      value: 48.1867206901292
    - type: nauc_recall_at_1_max
      value: 40.525641468978996
    - type: nauc_recall_at_1_std
      value: -0.7568533902855162
    - type: nauc_recall_at_20_diff1
      value: 29.07251333097125
    - type: nauc_recall_at_20_max
      value: 39.03312242614524
    - type: nauc_recall_at_20_std
      value: 8.959922224970903
    - type: nauc_recall_at_3_diff1
      value: 38.724975690747826
    - type: nauc_recall_at_3_max
      value: 41.3025635407677
    - type: nauc_recall_at_3_std
      value: 0.6484284398052167
    - type: nauc_recall_at_5_diff1
      value: 34.09423664395091
    - type: nauc_recall_at_5_max
      value: 41.34844327450573
    - type: nauc_recall_at_5_std
      value: 2.3349428535301424
    - type: ndcg_at_1
      value: 34.703
    - type: ndcg_at_10
      value: 41.967999999999996
    - type: ndcg_at_100
      value: 47.607
    - type: ndcg_at_1000
      value: 49.984
    - type: ndcg_at_20
      value: 44.285000000000004
    - type: ndcg_at_3
      value: 37.582
    - type: ndcg_at_5
      value: 39.454
    - type: precision_at_1
      value: 34.703
    - type: precision_at_10
      value: 7.306
    - type: precision_at_100
      value: 1.191
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_20
      value: 4.406000000000001
    - type: precision_at_3
      value: 17.541999999999998
    - type: precision_at_5
      value: 12.26
    - type: recall_at_1
      value: 27.991
    - type: recall_at_10
      value: 52.016
    - type: recall_at_100
      value: 75.807
    - type: recall_at_1000
      value: 91.84400000000001
    - type: recall_at_20
      value: 60.171
    - type: recall_at_3
      value: 39.268
    - type: recall_at_5
      value: 44.548
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval (default)
      revision: CQADupstackRetrieval_is_a_combined_dataset
      split: test
      type: CQADupstackRetrieval_is_a_combined_dataset
    metrics:
    - type: main_score
      value: 39.80483333333333
    - type: ndcg_at_10
      value: 39.80483333333333
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackStatsRetrieval (default)
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
      split: test
      type: mteb/cqadupstack-stats
    metrics:
    - type: main_score
      value: 34.888999999999996
    - type: map_at_1
      value: 24.257
    - type: map_at_10
      value: 30.85
    - type: map_at_100
      value: 31.653
    - type: map_at_1000
      value: 31.744
    - type: map_at_20
      value: 31.235000000000003
    - type: map_at_3
      value: 28.742
    - type: map_at_5
      value: 29.743000000000002
    - type: mrr_at_1
      value: 26.68711656441718
    - type: mrr_at_10
      value: 33.22828415619827
    - type: mrr_at_100
      value: 33.9510074708967
    - type: mrr_at_1000
      value: 34.019092955305204
    - type: mrr_at_20
      value: 33.600871234124
    - type: mrr_at_3
      value: 31.160531697341508
    - type: mrr_at_5
      value: 32.14212678936605
    - type: nauc_map_at_1000_diff1
      value: 52.717440487225275
    - type: nauc_map_at_1000_max
      value: 44.60170963845081
    - type: nauc_map_at_1000_std
      value: -3.1996706483359136
    - type: nauc_map_at_100_diff1
      value: 52.71189673586013
    - type: nauc_map_at_100_max
      value: 44.57163638567482
    - type: nauc_map_at_100_std
      value: -3.2345902627286436
    - type: nauc_map_at_10_diff1
      value: 53.02449930693637
    - type: nauc_map_at_10_max
      value: 44.35369795372346
    - type: nauc_map_at_10_std
      value: -3.8104783477282513
    - type: nauc_map_at_1_diff1
      value: 61.69412555489549
    - type: nauc_map_at_1_max
      value: 45.687572761686425
    - type: nauc_map_at_1_std
      value: -5.706950124921224
    - type: nauc_map_at_20_diff1
      value: 52.762382597962855
    - type: nauc_map_at_20_max
      value: 44.42527816578249
    - type: nauc_map_at_20_std
      value: -3.62442115557958
    - type: nauc_map_at_3_diff1
      value: 54.218133325934595
    - type: nauc_map_at_3_max
      value: 43.886110491155
    - type: nauc_map_at_3_std
      value: -5.373779809729606
    - type: nauc_map_at_5_diff1
      value: 53.87314356227072
    - type: nauc_map_at_5_max
      value: 44.19838867906011
    - type: nauc_map_at_5_std
      value: -4.657996273921579
    - type: nauc_mrr_at_1000_diff1
      value: 52.608759486406065
    - type: nauc_mrr_at_1000_max
      value: 46.43225035608919
    - type: nauc_mrr_at_1000_std
      value: -1.0825740469149292
    - type: nauc_mrr_at_100_diff1
      value: 52.59290039623913
    - type: nauc_mrr_at_100_max
      value: 46.43031739568791
    - type: nauc_mrr_at_100_std
      value: -1.110101172332684
    - type: nauc_mrr_at_10_diff1
      value: 52.860476269889055
    - type: nauc_mrr_at_10_max
      value: 46.48418329087753
    - type: nauc_mrr_at_10_std
      value: -1.3374238019386193
    - type: nauc_mrr_at_1_diff1
      value: 61.441947428807666
    - type: nauc_mrr_at_1_max
      value: 48.54756533074311
    - type: nauc_mrr_at_1_std
      value: -2.3680485432053135
    - type: nauc_mrr_at_20_diff1
      value: 52.665535367800906
    - type: nauc_mrr_at_20_max
      value: 46.41185879304558
    - type: nauc_mrr_at_20_std
      value: -1.3444595758714797
    - type: nauc_mrr_at_3_diff1
      value: 54.172851649909134
    - type: nauc_mrr_at_3_max
      value: 46.15833772250591
    - type: nauc_mrr_at_3_std
      value: -2.6730529379570642
    - type: nauc_mrr_at_5_diff1
      value: 53.723702014945175
    - type: nauc_mrr_at_5_max
      value: 46.297316686693016
    - type: nauc_mrr_at_5_std
      value: -2.159788610857334
    - type: nauc_ndcg_at_1000_diff1
      value: 48.49475884804671
    - type: nauc_ndcg_at_1000_max
      value: 45.2504813678727
    - type: nauc_ndcg_at_1000_std
      value: 1.3660441371017331
    - type: nauc_ndcg_at_100_diff1
      value: 48.328439839293004
    - type: nauc_ndcg_at_100_max
      value: 45.1976848279064
    - type: nauc_ndcg_at_100_std
      value: 0.984414559030773
    - type: nauc_ndcg_at_10_diff1
      value: 49.57495706841805
    - type: nauc_ndcg_at_10_max
      value: 44.32422841398523
    - type: nauc_ndcg_at_10_std
      value: -1.8938863954712948
    - type: nauc_ndcg_at_1_diff1
      value: 61.441947428807666
    - type: nauc_ndcg_at_1_max
      value: 48.54756533074311
    - type: nauc_ndcg_at_1_std
      value: -2.3680485432053135
    - type: nauc_ndcg_at_20_diff1
      value: 48.698704369155664
    - type: nauc_ndcg_at_20_max
      value: 44.32085785234671
    - type: nauc_ndcg_at_20_std
      value: -1.5370200957389617
    - type: nauc_ndcg_at_3_diff1
      value: 51.87602761155865
    - type: nauc_ndcg_at_3_max
      value: 43.836423952288946
    - type: nauc_ndcg_at_3_std
      value: -4.519331726990856
    - type: nauc_ndcg_at_5_diff1
      value: 51.536849644847216
    - type: nauc_ndcg_at_5_max
      value: 44.05267508410536
    - type: nauc_ndcg_at_5_std
      value: -3.7646800644981484
    - type: nauc_precision_at_1000_diff1
      value: -3.114425136121477
    - type: nauc_precision_at_1000_max
      value: 21.219654091584214
    - type: nauc_precision_at_1000_std
      value: 23.620715661080197
    - type: nauc_precision_at_100_diff1
      value: 13.781387623485253
    - type: nauc_precision_at_100_max
      value: 37.7816424452238
    - type: nauc_precision_at_100_std
      value: 24.719409110027726
    - type: nauc_precision_at_10_diff1
      value: 29.300018648484276
    - type: nauc_precision_at_10_max
      value: 42.111386830242296
    - type: nauc_precision_at_10_std
      value: 10.14768426081145
    - type: nauc_precision_at_1_diff1
      value: 61.441947428807666
    - type: nauc_precision_at_1_max
      value: 48.54756533074311
    - type: nauc_precision_at_1_std
      value: -2.3680485432053135
    - type: nauc_precision_at_20_diff1
      value: 24.056049155242437
    - type: nauc_precision_at_20_max
      value: 41.1201344685915
    - type: nauc_precision_at_20_std
      value: 12.97512554259156
    - type: nauc_precision_at_3_diff1
      value: 40.917570494530224
    - type: nauc_precision_at_3_max
      value: 42.15043236961856
    - type: nauc_precision_at_3_std
      value: -0.589880165120388
    - type: nauc_precision_at_5_diff1
      value: 36.58196834265981
    - type: nauc_precision_at_5_max
      value: 41.630431483145955
    - type: nauc_precision_at_5_std
      value: 2.792434474028848
    - type: nauc_recall_at_1000_diff1
      value: 22.038599119727685
    - type: nauc_recall_at_1000_max
      value: 40.92494951502034
    - type: nauc_recall_at_1000_std
      value: 30.098168212129906
    - type: nauc_recall_at_100_diff1
      value: 30.27278930698841
    - type: nauc_recall_at_100_max
      value: 43.08655404016066
    - type: nauc_recall_at_100_std
      value: 16.415020332792015
    - type: nauc_recall_at_10_diff1
      value: 38.75370707674917
    - type: nauc_recall_at_10_max
      value: 40.98674256815627
    - type: nauc_recall_at_10_std
      value: 1.4170954879979862
    - type: nauc_recall_at_1_diff1
      value: 61.69412555489549
    - type: nauc_recall_at_1_max
      value: 45.687572761686425
    - type: nauc_recall_at_1_std
      value: -5.706950124921224
    - type: nauc_recall_at_20_diff1
      value: 34.95998605858319
    - type: nauc_recall_at_20_max
      value: 40.10527957275843
    - type: nauc_recall_at_20_std
      value: 2.1856254846998895
    - type: nauc_recall_at_3_diff1
      value: 46.10618270844218
    - type: nauc_recall_at_3_max
      value: 39.94724438255762
    - type: nauc_recall_at_3_std
      value: -6.261263180948628
    - type: nauc_recall_at_5_diff1
      value: 45.37034670682598
    - type: nauc_recall_at_5_max
      value: 40.996211974958655
    - type: nauc_recall_at_5_std
      value: -3.8795589504838945
    - type: ndcg_at_1
      value: 26.687
    - type: ndcg_at_10
      value: 34.888999999999996
    - type: ndcg_at_100
      value: 38.967
    - type: ndcg_at_1000
      value: 41.408
    - type: ndcg_at_20
      value: 36.202
    - type: ndcg_at_3
      value: 30.763
    - type: ndcg_at_5
      value: 32.369
    - type: precision_at_1
      value: 26.687
    - type: precision_at_10
      value: 5.428999999999999
    - type: precision_at_100
      value: 0.8099999999999999
    - type: precision_at_1000
      value: 0.11
    - type: precision_at_20
      value: 3.0669999999999997
    - type: precision_at_3
      value: 12.883
    - type: precision_at_5
      value: 8.895999999999999
    - type: recall_at_1
      value: 24.257
    - type: recall_at_10
      value: 45.013999999999996
    - type: recall_at_100
      value: 63.55800000000001
    - type: recall_at_1000
      value: 81.649
    - type: recall_at_20
      value: 49.786
    - type: recall_at_3
      value: 33.623
    - type: recall_at_5
      value: 37.489
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackTexRetrieval (default)
      revision: 46989137a86843e03a6195de44b09deda022eec7
      split: test
      type: mteb/cqadupstack-tex
    metrics:
    - type: main_score
      value: 27.174
    - type: map_at_1
      value: 16.683
    - type: map_at_10
      value: 22.965
    - type: map_at_100
      value: 23.954
    - type: map_at_1000
      value: 24.078
    - type: map_at_20
      value: 23.49
    - type: map_at_3
      value: 20.918999999999997
    - type: map_at_5
      value: 22.027
    - type: mrr_at_1
      value: 19.92429456297316
    - type: mrr_at_10
      value: 26.551319656102862
    - type: mrr_at_100
      value: 27.428968210944316
    - type: mrr_at_1000
      value: 27.510501144435317
    - type: mrr_at_20
      value: 27.051813881383698
    - type: mrr_at_3
      value: 24.483826565726083
    - type: mrr_at_5
      value: 25.624569855471435
    - type: nauc_map_at_1000_diff1
      value: 39.70294552750383
    - type: nauc_map_at_1000_max
      value: 31.317466455201227
    - type: nauc_map_at_1000_std
      value: -1.762559086629105
    - type: nauc_map_at_100_diff1
      value: 39.71390899838813
    - type: nauc_map_at_100_max
      value: 31.29204970199068
    - type: nauc_map_at_100_std
      value: -1.791535537876596
    - type: nauc_map_at_10_diff1
      value: 40.01482969019678
    - type: nauc_map_at_10_max
      value: 31.23314156393745
    - type: nauc_map_at_10_std
      value: -2.3274535397042513
    - type: nauc_map_at_1_diff1
      value: 46.72895932959986
    - type: nauc_map_at_1_max
      value: 29.819875651168548
    - type: nauc_map_at_1_std
      value: -3.6639434506444912
    - type: nauc_map_at_20_diff1
      value: 39.79895580803141
    - type: nauc_map_at_20_max
      value: 31.18209733793537
    - type: nauc_map_at_20_std
      value: -2.052399285243834
    - type: nauc_map_at_3_diff1
      value: 41.98314483627424
    - type: nauc_map_at_3_max
      value: 31.410399587944422
    - type: nauc_map_at_3_std
      value: -3.1256987241100957
    - type: nauc_map_at_5_diff1
      value: 40.68955549018378
    - type: nauc_map_at_5_max
      value: 31.529138053527888
    - type: nauc_map_at_5_std
      value: -2.5106031609548727
    - type: nauc_mrr_at_1000_diff1
      value: 38.843425454050774
    - type: nauc_mrr_at_1000_max
      value: 32.080747972542476
    - type: nauc_mrr_at_1000_std
      value: -1.8813140227198037
    - type: nauc_mrr_at_100_diff1
      value: 38.844774433232246
    - type: nauc_mrr_at_100_max
      value: 32.07767547525176
    - type: nauc_mrr_at_100_std
      value: -1.8853968240347412
    - type: nauc_mrr_at_10_diff1
      value: 38.9943638829038
    - type: nauc_mrr_at_10_max
      value: 32.113199636613224
    - type: nauc_mrr_at_10_std
      value: -2.2808765253620997
    - type: nauc_mrr_at_1_diff1
      value: 45.204551111582504
    - type: nauc_mrr_at_1_max
      value: 31.33271495263982
    - type: nauc_mrr_at_1_std
      value: -4.310808417520686
    - type: nauc_mrr_at_20_diff1
      value: 38.809653957002475
    - type: nauc_mrr_at_20_max
      value: 32.00087958077687
    - type: nauc_mrr_at_20_std
      value: -2.077240815930647
    - type: nauc_mrr_at_3_diff1
      value: 40.640559615359884
    - type: nauc_mrr_at_3_max
      value: 32.499874311042085
    - type: nauc_mrr_at_3_std
      value: -3.0250204118059623
    - type: nauc_mrr_at_5_diff1
      value: 39.730384199123904
    - type: nauc_mrr_at_5_max
      value: 32.54797498951286
    - type: nauc_mrr_at_5_std
      value: -2.483752446190051
    - type: nauc_ndcg_at_1000_diff1
      value: 35.67309434839137
    - type: nauc_ndcg_at_1000_max
      value: 31.968665383689366
    - type: nauc_ndcg_at_1000_std
      value: 1.8902841143765996
    - type: nauc_ndcg_at_100_diff1
      value: 35.532320541105456
    - type: nauc_ndcg_at_100_max
      value: 31.39262363611392
    - type: nauc_ndcg_at_100_std
      value: 1.3738974219360591
    - type: nauc_ndcg_at_10_diff1
      value: 36.89304493982828
    - type: nauc_ndcg_at_10_max
      value: 31.413699188823262
    - type: nauc_ndcg_at_10_std
      value: -1.4406496834360265
    - type: nauc_ndcg_at_1_diff1
      value: 45.204551111582504
    - type: nauc_ndcg_at_1_max
      value: 31.33271495263982
    - type: nauc_ndcg_at_1_std
      value: -4.310808417520686
    - type: nauc_ndcg_at_20_diff1
      value: 36.10603668893203
    - type: nauc_ndcg_at_20_max
      value: 31.08596071268814
    - type: nauc_ndcg_at_20_std
      value: -0.5716127582631676
    - type: nauc_ndcg_at_3_diff1
      value: 40.3406275054372
    - type: nauc_ndcg_at_3_max
      value: 32.30746163378498
    - type: nauc_ndcg_at_3_std
      value: -2.9826906381184086
    - type: nauc_ndcg_at_5_diff1
      value: 38.435436080533805
    - type: nauc_ndcg_at_5_max
      value: 32.28159769507487
    - type: nauc_ndcg_at_5_std
      value: -1.896502637808091
    - type: nauc_precision_at_1000_diff1
      value: -1.3272380913114576
    - type: nauc_precision_at_1000_max
      value: 16.97452439042005
    - type: nauc_precision_at_1000_std
      value: 6.727514561355023
    - type: nauc_precision_at_100_diff1
      value: 9.050886288633748
    - type: nauc_precision_at_100_max
      value: 22.793531578995857
    - type: nauc_precision_at_100_std
      value: 9.041251836945914
    - type: nauc_precision_at_10_diff1
      value: 23.58024783123664
    - type: nauc_precision_at_10_max
      value: 30.911229044947746
    - type: nauc_precision_at_10_std
      value: 0.49206924465533297
    - type: nauc_precision_at_1_diff1
      value: 45.204551111582504
    - type: nauc_precision_at_1_max
      value: 31.33271495263982
    - type: nauc_precision_at_1_std
      value: -4.310808417520686
    - type: nauc_precision_at_20_diff1
      value: 18.72722750869453
    - type: nauc_precision_at_20_max
      value: 28.168309388621456
    - type: nauc_precision_at_20_std
      value: 3.5580796098534906
    - type: nauc_precision_at_3_diff1
      value: 34.21934456307853
    - type: nauc_precision_at_3_max
      value: 34.50963041596628
    - type: nauc_precision_at_3_std
      value: -2.1474684485851876
    - type: nauc_precision_at_5_diff1
      value: 29.967346999613596
    - type: nauc_precision_at_5_max
      value: 33.958476515854954
    - type: nauc_precision_at_5_std
      value: -0.45778793347456004
    - type: nauc_recall_at_1000_diff1
      value: 12.06453658572338
    - type: nauc_recall_at_1000_max
      value: 30.788667195142633
    - type: nauc_recall_at_1000_std
      value: 27.271269189751713
    - type: nauc_recall_at_100_diff1
      value: 19.6231994553196
    - type: nauc_recall_at_100_max
      value: 27.00238503628109
    - type: nauc_recall_at_100_std
      value: 13.294514312384601
    - type: nauc_recall_at_10_diff1
      value: 27.755272572613222
    - type: nauc_recall_at_10_max
      value: 28.332855891388125
    - type: nauc_recall_at_10_std
      value: 0.8241434995618968
    - type: nauc_recall_at_1_diff1
      value: 46.72895932959986
    - type: nauc_recall_at_1_max
      value: 29.819875651168548
    - type: nauc_recall_at_1_std
      value: -3.6639434506444912
    - type: nauc_recall_at_20_diff1
      value: 24.731671276025146
    - type: nauc_recall_at_20_max
      value: 26.949426211227795
    - type: nauc_recall_at_20_std
      value: 3.412457763382852
    - type: nauc_recall_at_3_diff1
      value: 36.38111388907899
    - type: nauc_recall_at_3_max
      value: 31.47754397495634
    - type: nauc_recall_at_3_std
      value: -2.1874715383733956
    - type: nauc_recall_at_5_diff1
      value: 31.68529930399809
    - type: nauc_recall_at_5_max
      value: 31.090941464639744
    - type: nauc_recall_at_5_std
      value: -0.1674878655815559
    - type: ndcg_at_1
      value: 19.924
    - type: ndcg_at_10
      value: 27.174
    - type: ndcg_at_100
      value: 32.065
    - type: ndcg_at_1000
      value: 35.106
    - type: ndcg_at_20
      value: 28.939999999999998
    - type: ndcg_at_3
      value: 23.372999999999998
    - type: ndcg_at_5
      value: 25.096
    - type: precision_at_1
      value: 19.924
    - type: precision_at_10
      value: 4.855
    - type: precision_at_100
      value: 0.857
    - type: precision_at_1000
      value: 0.129
    - type: precision_at_20
      value: 2.94
    - type: precision_at_3
      value: 10.897
    - type: precision_at_5
      value: 7.7909999999999995
    - type: recall_at_1
      value: 16.683
    - type: recall_at_10
      value: 36.276
    - type: recall_at_100
      value: 58.437
    - type: recall_at_1000
      value: 80.35900000000001
    - type: recall_at_20
      value: 42.79
    - type: recall_at_3
      value: 25.663999999999998
    - type: recall_at_5
      value: 30.213
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackUnixRetrieval (default)
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
      split: test
      type: mteb/cqadupstack-unix
    metrics:
    - type: main_score
      value: 38.34
    - type: map_at_1
      value: 25.924999999999997
    - type: map_at_10
      value: 33.53
    - type: map_at_100
      value: 34.635
    - type: map_at_1000
      value: 34.739
    - type: map_at_20
      value: 34.117999999999995
    - type: map_at_3
      value: 30.94
    - type: map_at_5
      value: 32.411
    - type: mrr_at_1
      value: 30.223880597014922
    - type: mrr_at_10
      value: 37.598873193556024
    - type: mrr_at_100
      value: 38.48001202116003
    - type: mrr_at_1000
      value: 38.53998687212744
    - type: mrr_at_20
      value: 38.0922428291824
    - type: mrr_at_3
      value: 35.26119402985074
    - type: mrr_at_5
      value: 36.627798507462686
    - type: nauc_map_at_1000_diff1
      value: 48.99658121611321
    - type: nauc_map_at_1000_max
      value: 43.36514689969973
    - type: nauc_map_at_1000_std
      value: 1.2743138438292323
    - type: nauc_map_at_100_diff1
      value: 49.00383839256485
    - type: nauc_map_at_100_max
      value: 43.34421843813268
    - type: nauc_map_at_100_std
      value: 1.2381577394429648
    - type: nauc_map_at_10_diff1
      value: 48.976968357570804
    - type: nauc_map_at_10_max
      value: 43.21656545934543
    - type: nauc_map_at_10_std
      value: 0.8806229946576106
    - type: nauc_map_at_1_diff1
      value: 54.79429701172901
    - type: nauc_map_at_1_max
      value: 44.94497297225627
    - type: nauc_map_at_1_std
      value: 0.3424876477921997
    - type: nauc_map_at_20_diff1
      value: 49.05500453067965
    - type: nauc_map_at_20_max
      value: 43.313867184227114
    - type: nauc_map_at_20_std
      value: 1.0599077751868857
    - type: nauc_map_at_3_diff1
      value: 50.202191345168735
    - type: nauc_map_at_3_max
      value: 43.16428713411531
    - type: nauc_map_at_3_std
      value: 0.33035782399351366
    - type: nauc_map_at_5_diff1
      value: 49.43896179760421
    - type: nauc_map_at_5_max
      value: 43.36309937252455
    - type: nauc_map_at_5_std
      value: 0.6152011411226946
    - type: nauc_mrr_at_1000_diff1
      value: 48.359023685110486
    - type: nauc_mrr_at_1000_max
      value: 42.5315010808791
    - type: nauc_mrr_at_1000_std
      value: 0.5920431228924952
    - type: nauc_mrr_at_100_diff1
      value: 48.33949213883611
    - type: nauc_mrr_at_100_max
      value: 42.501697399914725
    - type: nauc_mrr_at_100_std
      value: 0.5683233598385363
    - type: nauc_mrr_at_10_diff1
      value: 48.17405374349975
    - type: nauc_mrr_at_10_max
      value: 42.36829702421452
    - type: nauc_mrr_at_10_std
      value: 0.3918636512799242
    - type: nauc_mrr_at_1_diff1
      value: 54.41613067936997
    - type: nauc_mrr_at_1_max
      value: 44.91551488557509
    - type: nauc_mrr_at_1_std
      value: -0.7697411188700982
    - type: nauc_mrr_at_20_diff1
      value: 48.29085774083497
    - type: nauc_mrr_at_20_max
      value: 42.46692350994534
    - type: nauc_mrr_at_20_std
      value: 0.49667689004854476
    - type: nauc_mrr_at_3_diff1
      value: 49.32403876113614
    - type: nauc_mrr_at_3_max
      value: 42.420974899262816
    - type: nauc_mrr_at_3_std
      value: -0.17054785857862576
    - type: nauc_mrr_at_5_diff1
      value: 48.5386866012484
    - type: nauc_mrr_at_5_max
      value: 42.49752447209939
    - type: nauc_mrr_at_5_std
      value: -0.030068724695007015
    - type: nauc_ndcg_at_1000_diff1
      value: 46.482903430093685
    - type: nauc_ndcg_at_1000_max
      value: 43.18727440958746
    - type: nauc_ndcg_at_1000_std
      value: 3.8397045352936874
    - type: nauc_ndcg_at_100_diff1
      value: 46.272241119098105
    - type: nauc_ndcg_at_100_max
      value: 42.44044067518221
    - type: nauc_ndcg_at_100_std
      value: 3.0744093549329374
    - type: nauc_ndcg_at_10_diff1
      value: 46.35820553525149
    - type: nauc_ndcg_at_10_max
      value: 42.05754989284268
    - type: nauc_ndcg_at_10_std
      value: 1.6140781134179982
    - type: nauc_ndcg_at_1_diff1
      value: 54.41613067936997
    - type: nauc_ndcg_at_1_max
      value: 44.91551488557509
    - type: nauc_ndcg_at_1_std
      value: -0.7697411188700982
    - type: nauc_ndcg_at_20_diff1
      value: 46.56173859192192
    - type: nauc_ndcg_at_20_max
      value: 42.39990803441754
    - type: nauc_ndcg_at_20_std
      value: 2.2301958940613518
    - type: nauc_ndcg_at_3_diff1
      value: 48.45451921294981
    - type: nauc_ndcg_at_3_max
      value: 42.1519683087422
    - type: nauc_ndcg_at_3_std
      value: 0.43355376702150983
    - type: nauc_ndcg_at_5_diff1
      value: 47.329516258529
    - type: nauc_ndcg_at_5_max
      value: 42.39325493165628
    - type: nauc_ndcg_at_5_std
      value: 0.8719863795035224
    - type: nauc_precision_at_1000_diff1
      value: -10.427395700183098
    - type: nauc_precision_at_1000_max
      value: 1.3695831886594074
    - type: nauc_precision_at_1000_std
      value: 5.396211335976429
    - type: nauc_precision_at_100_diff1
      value: 4.170216285720574
    - type: nauc_precision_at_100_max
      value: 14.393676436386233
    - type: nauc_precision_at_100_std
      value: 7.356250144868687
    - type: nauc_precision_at_10_diff1
      value: 25.406793843503
    - type: nauc_precision_at_10_max
      value: 30.469137431378485
    - type: nauc_precision_at_10_std
      value: 4.262031333274362
    - type: nauc_precision_at_1_diff1
      value: 54.41613067936997
    - type: nauc_precision_at_1_max
      value: 44.91551488557509
    - type: nauc_precision_at_1_std
      value: -0.7697411188700982
    - type: nauc_precision_at_20_diff1
      value: 20.989784339763254
    - type: nauc_precision_at_20_max
      value: 27.616892902118735
    - type: nauc_precision_at_20_std
      value: 5.021785061675381
    - type: nauc_precision_at_3_diff1
      value: 39.66665542900266
    - type: nauc_precision_at_3_max
      value: 37.76686222170862
    - type: nauc_precision_at_3_std
      value: 1.04925540752191
    - type: nauc_precision_at_5_diff1
      value: 32.88141076318413
    - type: nauc_precision_at_5_max
      value: 35.90401974619475
    - type: nauc_precision_at_5_std
      value: 2.2695242286100408
    - type: nauc_recall_at_1000_diff1
      value: 30.248973513875526
    - type: nauc_recall_at_1000_max
      value: 48.439331789791325
    - type: nauc_recall_at_1000_std
      value: 38.857189673518135
    - type: nauc_recall_at_100_diff1
      value: 33.090255913758874
    - type: nauc_recall_at_100_max
      value: 35.45818452208663
    - type: nauc_recall_at_100_std
      value: 12.58439358264515
    - type: nauc_recall_at_10_diff1
      value: 37.462082402733785
    - type: nauc_recall_at_10_max
      value: 36.99065942533105
    - type: nauc_recall_at_10_std
      value: 3.948587023033947
    - type: nauc_recall_at_1_diff1
      value: 54.79429701172901
    - type: nauc_recall_at_1_max
      value: 44.94497297225627
    - type: nauc_recall_at_1_std
      value: 0.3424876477921997
    - type: nauc_recall_at_20_diff1
      value: 37.34159405112872
    - type: nauc_recall_at_20_max
      value: 37.50873448555206
    - type: nauc_recall_at_20_std
      value: 6.669489660177887
    - type: nauc_recall_at_3_diff1
      value: 43.751405924588184
    - type: nauc_recall_at_3_max
      value: 38.5280847003097
    - type: nauc_recall_at_3_std
      value: 0.8234291612745726
    - type: nauc_recall_at_5_diff1
      value: 40.75537181461394
    - type: nauc_recall_at_5_max
      value: 38.64761171801593
    - type: nauc_recall_at_5_std
      value: 1.9783778065563666
    - type: ndcg_at_1
      value: 30.224
    - type: ndcg_at_10
      value: 38.34
    - type: ndcg_at_100
      value: 43.564
    - type: ndcg_at_1000
      value: 45.888
    - type: ndcg_at_20
      value: 40.285
    - type: ndcg_at_3
      value: 33.613
    - type: ndcg_at_5
      value: 35.868
    - type: precision_at_1
      value: 30.224
    - type: precision_at_10
      value: 6.343
    - type: precision_at_100
      value: 1.0030000000000001
    - type: precision_at_1000
      value: 0.131
    - type: precision_at_20
      value: 3.689
    - type: precision_at_3
      value: 14.832
    - type: precision_at_5
      value: 10.504
    - type: recall_at_1
      value: 25.924999999999997
    - type: recall_at_10
      value: 49.01
    - type: recall_at_100
      value: 71.935
    - type: recall_at_1000
      value: 88.191
    - type: recall_at_20
      value: 56.076
    - type: recall_at_3
      value: 36.344
    - type: recall_at_5
      value: 41.942
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWebmastersRetrieval (default)
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
      split: test
      type: mteb/cqadupstack-webmasters
    metrics:
    - type: main_score
      value: 39.007
    - type: map_at_1
      value: 25.195
    - type: map_at_10
      value: 33.29
    - type: map_at_100
      value: 34.919
    - type: map_at_1000
      value: 35.132999999999996
    - type: map_at_20
      value: 34.184
    - type: map_at_3
      value: 30.501
    - type: map_at_5
      value: 31.917
    - type: mrr_at_1
      value: 30.237154150197625
    - type: mrr_at_10
      value: 37.97901373988331
    - type: mrr_at_100
      value: 38.89357624578056
    - type: mrr_at_1000
      value: 38.96172508462875
    - type: mrr_at_20
      value: 38.489908488593
    - type: mrr_at_3
      value: 35.44137022397892
    - type: mrr_at_5
      value: 36.755599472990774
    - type: nauc_map_at_1000_diff1
      value: 54.52234288345771
    - type: nauc_map_at_1000_max
      value: 37.02933259777875
    - type: nauc_map_at_1000_std
      value: -1.8802414735497839
    - type: nauc_map_at_100_diff1
      value: 54.592085424308564
    - type: nauc_map_at_100_max
      value: 37.13861558972853
    - type: nauc_map_at_100_std
      value: -1.8864900602925623
    - type: nauc_map_at_10_diff1
      value: 55.32701084932018
    - type: nauc_map_at_10_max
      value: 36.97158176818064
    - type: nauc_map_at_10_std
      value: -3.364570079568588
    - type: nauc_map_at_1_diff1
      value: 62.56234442022803
    - type: nauc_map_at_1_max
      value: 37.725553737446866
    - type: nauc_map_at_1_std
      value: -5.9573495367577705
    - type: nauc_map_at_20_diff1
      value: 54.92567471295049
    - type: nauc_map_at_20_max
      value: 36.980006282091985
    - type: nauc_map_at_20_std
      value: -2.7416738048891243
    - type: nauc_map_at_3_diff1
      value: 57.6202035201006
    - type: nauc_map_at_3_max
      value: 36.85083307496426
    - type: nauc_map_at_3_std
      value: -4.929088209082444
    - type: nauc_map_at_5_diff1
      value: 56.43034014992742
    - type: nauc_map_at_5_max
      value: 36.65006798835753
    - type: nauc_map_at_5_std
      value: -4.776147213332607
    - type: nauc_mrr_at_1000_diff1
      value: 51.91684536214369
    - type: nauc_mrr_at_1000_max
      value: 35.50047477073224
    - type: nauc_mrr_at_1000_std
      value: -0.9638166168094422
    - type: nauc_mrr_at_100_diff1
      value: 51.89735751581897
    - type: nauc_mrr_at_100_max
      value: 35.48371938892366
    - type: nauc_mrr_at_100_std
      value: -0.9444977007097576
    - type: nauc_mrr_at_10_diff1
      value: 51.82990105533963
    - type: nauc_mrr_at_10_max
      value: 35.41678096580625
    - type: nauc_mrr_at_10_std
      value: -1.2998439543197369
    - type: nauc_mrr_at_1_diff1
      value: 57.36601705972182
    - type: nauc_mrr_at_1_max
      value: 36.90602990003092
    - type: nauc_mrr_at_1_std
      value: -3.4080880251307044
    - type: nauc_mrr_at_20_diff1
      value: 51.8613947241447
    - type: nauc_mrr_at_20_max
      value: 35.42345819928662
    - type: nauc_mrr_at_20_std
      value: -1.093870308993923
    - type: nauc_mrr_at_3_diff1
      value: 53.01993009463089
    - type: nauc_mrr_at_3_max
      value: 35.822666497908806
    - type: nauc_mrr_at_3_std
      value: -2.1165600076512474
    - type: nauc_mrr_at_5_diff1
      value: 52.34611304656942
    - type: nauc_mrr_at_5_max
      value: 35.49696929205688
    - type: nauc_mrr_at_5_std
      value: -2.0955274926266982
    - type: nauc_ndcg_at_1000_diff1
      value: 51.41120348218975
    - type: nauc_ndcg_at_1000_max
      value: 36.685342768279675
    - type: nauc_ndcg_at_1000_std
      value: 1.7205313748343651
    - type: nauc_ndcg_at_100_diff1
      value: 50.93701708514895
    - type: nauc_ndcg_at_100_max
      value: 36.162627377243275
    - type: nauc_ndcg_at_100_std
      value: 1.7640807675244328
    - type: nauc_ndcg_at_10_diff1
      value: 50.63098923593871
    - type: nauc_ndcg_at_10_max
      value: 35.34361464083639
    - type: nauc_ndcg_at_10_std
      value: -0.9402862458857915
    - type: nauc_ndcg_at_1_diff1
      value: 57.36601705972182
    - type: nauc_ndcg_at_1_max
      value: 36.90602990003092
    - type: nauc_ndcg_at_1_std
      value: -3.4080880251307044
    - type: nauc_ndcg_at_20_diff1
      value: 50.73961693837964
    - type: nauc_ndcg_at_20_max
      value: 35.01998564289338
    - type: nauc_ndcg_at_20_std
      value: -0.5241446967120867
    - type: nauc_ndcg_at_3_diff1
      value: 53.23302956511971
    - type: nauc_ndcg_at_3_max
      value: 35.708980757056295
    - type: nauc_ndcg_at_3_std
      value: -3.017125347557592
    - type: nauc_ndcg_at_5_diff1
      value: 52.335636773583396
    - type: nauc_ndcg_at_5_max
      value: 35.34227057005852
    - type: nauc_ndcg_at_5_std
      value: -2.9708664518544508
    - type: nauc_precision_at_1000_diff1
      value: -18.554677236277232
    - type: nauc_precision_at_1000_max
      value: -15.659740900843067
    - type: nauc_precision_at_1000_std
      value: 8.228155770924415
    - type: nauc_precision_at_100_diff1
      value: -12.195998995692928
    - type: nauc_precision_at_100_max
      value: -0.5888781565639164
    - type: nauc_precision_at_100_std
      value: 19.312752223375448
    - type: nauc_precision_at_10_diff1
      value: 12.921470127228105
    - type: nauc_precision_at_10_max
      value: 21.317929458256238
    - type: nauc_precision_at_10_std
      value: 13.148202187911012
    - type: nauc_precision_at_1_diff1
      value: 57.36601705972182
    - type: nauc_precision_at_1_max
      value: 36.90602990003092
    - type: nauc_precision_at_1_std
      value: -3.4080880251307044
    - type: nauc_precision_at_20_diff1
      value: 2.4696353004069906
    - type: nauc_precision_at_20_max
      value: 14.284343093524058
    - type: nauc_precision_at_20_std
      value: 17.480976091077217
    - type: nauc_precision_at_3_diff1
      value: 35.82856720298558
    - type: nauc_precision_at_3_max
      value: 29.613454822718143
    - type: nauc_precision_at_3_std
      value: 0.38030095211645343
    - type: nauc_precision_at_5_diff1
      value: 27.632641276435354
    - type: nauc_precision_at_5_max
      value: 27.238425775328967
    - type: nauc_precision_at_5_std
      value: 3.152744091929671
    - type: nauc_recall_at_1000_diff1
      value: 33.28570370310322
    - type: nauc_recall_at_1000_max
      value: 44.315453433115785
    - type: nauc_recall_at_1000_std
      value: 43.371884128363
    - type: nauc_recall_at_100_diff1
      value: 35.77059425104567
    - type: nauc_recall_at_100_max
      value: 31.48054575812204
    - type: nauc_recall_at_100_std
      value: 17.639416832754303
    - type: nauc_recall_at_10_diff1
      value: 40.179789202687914
    - type: nauc_recall_at_10_max
      value: 30.466946546206923
    - type: nauc_recall_at_10_std
      value: 0.8385433327977754
    - type: nauc_recall_at_1_diff1
      value: 62.56234442022803
    - type: nauc_recall_at_1_max
      value: 37.725553737446866
    - type: nauc_recall_at_1_std
      value: -5.9573495367577705
    - type: nauc_recall_at_20_diff1
      value: 38.70371818511684
    - type: nauc_recall_at_20_max
      value: 28.305350175132567
    - type: nauc_recall_at_20_std
      value: 3.8854966962347746
    - type: nauc_recall_at_3_diff1
      value: 51.22347884414916
    - type: nauc_recall_at_3_max
      value: 33.21612425601433
    - type: nauc_recall_at_3_std
      value: -4.48370860005988
    - type: nauc_recall_at_5_diff1
      value: 46.848014408337676
    - type: nauc_recall_at_5_max
      value: 31.254476917525555
    - type: nauc_recall_at_5_std
      value: -4.903427133365656
    - type: ndcg_at_1
      value: 30.237000000000002
    - type: ndcg_at_10
      value: 39.007
    - type: ndcg_at_100
      value: 44.585
    - type: ndcg_at_1000
      value: 47.464
    - type: ndcg_at_20
      value: 41.278999999999996
    - type: ndcg_at_3
      value: 34.472
    - type: ndcg_at_5
      value: 36.315
    - type: precision_at_1
      value: 30.237000000000002
    - type: precision_at_10
      value: 7.51
    - type: precision_at_100
      value: 1.478
    - type: precision_at_1000
      value: 0.234
    - type: precision_at_20
      value: 4.7829999999999995
    - type: precision_at_3
      value: 16.14
    - type: precision_at_5
      value: 11.462
    - type: recall_at_1
      value: 25.195
    - type: recall_at_10
      value: 49.507
    - type: recall_at_100
      value: 74.083
    - type: recall_at_1000
      value: 92.899
    - type: recall_at_20
      value: 58.291000000000004
    - type: recall_at_3
      value: 36.167
    - type: recall_at_5
      value: 41.749
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWordpressRetrieval (default)
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
      split: test
      type: mteb/cqadupstack-wordpress
    metrics:
    - type: main_score
      value: 33.06
    - type: map_at_1
      value: 22.683
    - type: map_at_10
      value: 29.115000000000002
    - type: map_at_100
      value: 30.035
    - type: map_at_1000
      value: 30.141000000000002
    - type: map_at_20
      value: 29.585
    - type: map_at_3
      value: 27.436
    - type: map_at_5
      value: 28.186
    - type: mrr_at_1
      value: 24.953789279112755
    - type: mrr_at_10
      value: 31.512190828272157
    - type: mrr_at_100
      value: 32.30661079835987
    - type: mrr_at_1000
      value: 32.388485948646846
    - type: mrr_at_20
      value: 31.898454977555428
    - type: mrr_at_3
      value: 29.852125693160815
    - type: mrr_at_5
      value: 30.64695009242144
    - type: nauc_map_at_1000_diff1
      value: 41.37097481409692
    - type: nauc_map_at_1000_max
      value: 21.819472065390062
    - type: nauc_map_at_1000_std
      value: -5.511851233031371
    - type: nauc_map_at_100_diff1
      value: 41.38580981484577
    - type: nauc_map_at_100_max
      value: 21.796410887298222
    - type: nauc_map_at_100_std
      value: -5.56736379242138
    - type: nauc_map_at_10_diff1
      value: 41.63629903410976
    - type: nauc_map_at_10_max
      value: 21.90371149884218
    - type: nauc_map_at_10_std
      value: -6.152274677121426
    - type: nauc_map_at_1_diff1
      value: 45.84841941041374
    - type: nauc_map_at_1_max
      value: 20.461574274794568
    - type: nauc_map_at_1_std
      value: -7.769870515581234
    - type: nauc_map_at_20_diff1
      value: 41.616159838791376
    - type: nauc_map_at_20_max
      value: 21.879572436615728
    - type: nauc_map_at_20_std
      value: -6.001760143925003
    - type: nauc_map_at_3_diff1
      value: 42.690213994915474
    - type: nauc_map_at_3_max
      value: 21.35340820982141
    - type: nauc_map_at_3_std
      value: -6.118720026868332
    - type: nauc_map_at_5_diff1
      value: 42.107817663484575
    - type: nauc_map_at_5_max
      value: 22.02508826703247
    - type: nauc_map_at_5_std
      value: -5.655849953120985
    - type: nauc_mrr_at_1000_diff1
      value: 39.66954612386224
    - type: nauc_mrr_at_1000_max
      value: 22.150137067327954
    - type: nauc_mrr_at_1000_std
      value: -4.798006812425386
    - type: nauc_mrr_at_100_diff1
      value: 39.66409024535208
    - type: nauc_mrr_at_100_max
      value: 22.121525365416538
    - type: nauc_mrr_at_100_std
      value: -4.806603240713894
    - type: nauc_mrr_at_10_diff1
      value: 39.87117352487735
    - type: nauc_mrr_at_10_max
      value: 22.298568726426076
    - type: nauc_mrr_at_10_std
      value: -5.1451772190015195
    - type: nauc_mrr_at_1_diff1
      value: 43.86075692062394
    - type: nauc_mrr_at_1_max
      value: 20.51270620979276
    - type: nauc_mrr_at_1_std
      value: -7.589704558075294
    - type: nauc_mrr_at_20_diff1
      value: 39.820424398881215
    - type: nauc_mrr_at_20_max
      value: 22.173944895852095
    - type: nauc_mrr_at_20_std
      value: -5.0727540461865335
    - type: nauc_mrr_at_3_diff1
      value: 40.73278435693193
    - type: nauc_mrr_at_3_max
      value: 21.930995553135812
    - type: nauc_mrr_at_3_std
      value: -5.980722775097277
    - type: nauc_mrr_at_5_diff1
      value: 39.89679395564144
    - type: nauc_mrr_at_5_max
      value: 22.02821777103734
    - type: nauc_mrr_at_5_std
      value: -5.072135508421082
    - type: nauc_ndcg_at_1000_diff1
      value: 37.957587605367785
    - type: nauc_ndcg_at_1000_max
      value: 22.362257192820255
    - type: nauc_ndcg_at_1000_std
      value: -1.7757428668228084
    - type: nauc_ndcg_at_100_diff1
      value: 37.908544407246104
    - type: nauc_ndcg_at_100_max
      value: 21.536623476432354
    - type: nauc_ndcg_at_100_std
      value: -2.678355870833651
    - type: nauc_ndcg_at_10_diff1
      value: 39.36845261271005
    - type: nauc_ndcg_at_10_max
      value: 22.3150793248212
    - type: nauc_ndcg_at_10_std
      value: -5.646375413170874
    - type: nauc_ndcg_at_1_diff1
      value: 43.86075692062394
    - type: nauc_ndcg_at_1_max
      value: 20.51270620979276
    - type: nauc_ndcg_at_1_std
      value: -7.589704558075294
    - type: nauc_ndcg_at_20_diff1
      value: 39.30711049883703
    - type: nauc_ndcg_at_20_max
      value: 21.935544953883415
    - type: nauc_ndcg_at_20_std
      value: -5.20402304183158
    - type: nauc_ndcg_at_3_diff1
      value: 41.113286498750305
    - type: nauc_ndcg_at_3_max
      value: 21.635397999914282
    - type: nauc_ndcg_at_3_std
      value: -5.72866713630757
    - type: nauc_ndcg_at_5_diff1
      value: 40.06783309225114
    - type: nauc_ndcg_at_5_max
      value: 22.416356942701672
    - type: nauc_ndcg_at_5_std
      value: -4.886519038213331
    - type: nauc_precision_at_1000_diff1
      value: -17.52292838463402
    - type: nauc_precision_at_1000_max
      value: -5.389818321213827
    - type: nauc_precision_at_1000_std
      value: 26.772552854570375
    - type: nauc_precision_at_100_diff1
      value: 3.543169641476175
    - type: nauc_precision_at_100_max
      value: 9.574510694378198
    - type: nauc_precision_at_100_std
      value: 17.92832693421059
    - type: nauc_precision_at_10_diff1
      value: 24.894375565187694
    - type: nauc_precision_at_10_max
      value: 22.273016884986628
    - type: nauc_precision_at_10_std
      value: -0.32355612520474136
    - type: nauc_precision_at_1_diff1
      value: 43.86075692062394
    - type: nauc_precision_at_1_max
      value: 20.51270620979276
    - type: nauc_precision_at_1_std
      value: -7.589704558075294
    - type: nauc_precision_at_20_diff1
      value: 21.29826064932648
    - type: nauc_precision_at_20_max
      value: 19.79498027543001
    - type: nauc_precision_at_20_std
      value: 2.804941576632282
    - type: nauc_precision_at_3_diff1
      value: 33.72177316592598
    - type: nauc_precision_at_3_max
      value: 22.691241202228518
    - type: nauc_precision_at_3_std
      value: -2.7085967541341853
    - type: nauc_precision_at_5_diff1
      value: 30.51704379057159
    - type: nauc_precision_at_5_max
      value: 24.287775910544436
    - type: nauc_precision_at_5_std
      value: 0.6318618555538418
    - type: nauc_recall_at_1000_diff1
      value: 16.14163529457628
    - type: nauc_recall_at_1000_max
      value: 30.255937330833625
    - type: nauc_recall_at_1000_std
      value: 34.82149396857235
    - type: nauc_recall_at_100_diff1
      value: 24.81738199141423
    - type: nauc_recall_at_100_max
      value: 17.622405730191517
    - type: nauc_recall_at_100_std
      value: 9.943278532212068
    - type: nauc_recall_at_10_diff1
      value: 34.03447281460739
    - type: nauc_recall_at_10_max
      value: 22.077681180504047
    - type: nauc_recall_at_10_std
      value: -5.772153803762581
    - type: nauc_recall_at_1_diff1
      value: 45.84841941041374
    - type: nauc_recall_at_1_max
      value: 20.461574274794568
    - type: nauc_recall_at_1_std
      value: -7.769870515581234
    - type: nauc_recall_at_20_diff1
      value: 33.91749085377916
    - type: nauc_recall_at_20_max
      value: 20.226869969726543
    - type: nauc_recall_at_20_std
      value: -4.369285076602888
    - type: nauc_recall_at_3_diff1
      value: 38.25575445199975
    - type: nauc_recall_at_3_max
      value: 21.402983769895837
    - type: nauc_recall_at_3_std
      value: -5.96278802416301
    - type: nauc_recall_at_5_diff1
      value: 36.17314539524256
    - type: nauc_recall_at_5_max
      value: 23.115551795773314
    - type: nauc_recall_at_5_std
      value: -3.8407187471333697
    - type: ndcg_at_1
      value: 24.954
    - type: ndcg_at_10
      value: 33.06
    - type: ndcg_at_100
      value: 37.751000000000005
    - type: ndcg_at_1000
      value: 40.477000000000004
    - type: ndcg_at_20
      value: 34.587
    - type: ndcg_at_3
      value: 29.666999999999998
    - type: ndcg_at_5
      value: 30.929000000000002
    - type: precision_at_1
      value: 24.954
    - type: precision_at_10
      value: 4.972
    - type: precision_at_100
      value: 0.799
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_20
      value: 2.874
    - type: precision_at_3
      value: 12.446
    - type: precision_at_5
      value: 8.244
    - type: recall_at_1
      value: 22.683
    - type: recall_at_10
      value: 42.775
    - type: recall_at_100
      value: 65.05300000000001
    - type: recall_at_1000
      value: 85.251
    - type: recall_at_20
      value: 48.512
    - type: recall_at_3
      value: 33.423
    - type: recall_at_5
      value: 36.571
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ClimateFEVER (default)
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
      split: test
      type: mteb/climate-fever
    metrics:
    - type: main_score
      value: 25.713
    - type: map_at_1
      value: 10.995000000000001
    - type: map_at_10
      value: 18.183
    - type: map_at_100
      value: 19.758
    - type: map_at_1000
      value: 19.93
    - type: map_at_20
      value: 19.023
    - type: map_at_3
      value: 15.126999999999999
    - type: map_at_5
      value: 16.521
    - type: mrr_at_1
      value: 23.908794788273617
    - type: mrr_at_10
      value: 34.419626699756996
    - type: mrr_at_100
      value: 35.42205880765744
    - type: mrr_at_1000
      value: 35.465636585855435
    - type: mrr_at_20
      value: 35.04560320193987
    - type: mrr_at_3
      value: 31.31378935939197
    - type: mrr_at_5
      value: 32.98154180238871
    - type: nauc_map_at_1000_diff1
      value: 30.808649871031978
    - type: nauc_map_at_1000_max
      value: 38.44733700268257
    - type: nauc_map_at_1000_std
      value: 24.83849154952647
    - type: nauc_map_at_100_diff1
      value: 30.817681439188565
    - type: nauc_map_at_100_max
      value: 38.38165009049118
    - type: nauc_map_at_100_std
      value: 24.75945437667734
    - type: nauc_map_at_10_diff1
      value: 31.016072728955457
    - type: nauc_map_at_10_max
      value: 37.78482154934025
    - type: nauc_map_at_10_std
      value: 22.73087477402899
    - type: nauc_map_at_1_diff1
      value: 38.13786017193742
    - type: nauc_map_at_1_max
      value: 34.897924276187446
    - type: nauc_map_at_1_std
      value: 15.197914019142733
    - type: nauc_map_at_20_diff1
      value: 30.93811389613207
    - type: nauc_map_at_20_max
      value: 38.018621558175084
    - type: nauc_map_at_20_std
      value: 23.87402074626538
    - type: nauc_map_at_3_diff1
      value: 32.694558487234204
    - type: nauc_map_at_3_max
      value: 37.452175644150344
    - type: nauc_map_at_3_std
      value: 20.06796990357737
    - type: nauc_map_at_5_diff1
      value: 31.654957870346784
    - type: nauc_map_at_5_max
      value: 37.04115114192235
    - type: nauc_map_at_5_std
      value: 21.129693545324375
    - type: nauc_mrr_at_1000_diff1
      value: 29.802772421913403
    - type: nauc_mrr_at_1000_max
      value: 38.000278050301176
    - type: nauc_mrr_at_1000_std
      value: 23.48992856904152
    - type: nauc_mrr_at_100_diff1
      value: 29.788014379597026
    - type: nauc_mrr_at_100_max
      value: 38.0070275486147
    - type: nauc_mrr_at_100_std
      value: 23.522736661530086
    - type: nauc_mrr_at_10_diff1
      value: 29.5812602078958
    - type: nauc_mrr_at_10_max
      value: 37.73314132006107
    - type: nauc_mrr_at_10_std
      value: 23.34339817425411
    - type: nauc_mrr_at_1_diff1
      value: 36.24696165314146
    - type: nauc_mrr_at_1_max
      value: 36.63498565688475
    - type: nauc_mrr_at_1_std
      value: 16.627906626261446
    - type: nauc_mrr_at_20_diff1
      value: 29.765297131181562
    - type: nauc_mrr_at_20_max
      value: 37.8739248069123
    - type: nauc_mrr_at_20_std
      value: 23.44526626055555
    - type: nauc_mrr_at_3_diff1
      value: 30.428492046004795
    - type: nauc_mrr_at_3_max
      value: 37.917848006886125
    - type: nauc_mrr_at_3_std
      value: 21.90161780585706
    - type: nauc_mrr_at_5_diff1
      value: 29.93977431566972
    - type: nauc_mrr_at_5_max
      value: 37.69690203746751
    - type: nauc_mrr_at_5_std
      value: 22.75274068799061
    - type: nauc_ndcg_at_1000_diff1
      value: 27.523183792167266
    - type: nauc_ndcg_at_1000_max
      value: 40.93757048012577
    - type: nauc_ndcg_at_1000_std
      value: 32.30396817658341
    - type: nauc_ndcg_at_100_diff1
      value: 27.454763301587064
    - type: nauc_ndcg_at_100_max
      value: 40.45039618287942
    - type: nauc_ndcg_at_100_std
      value: 31.795801743619663
    - type: nauc_ndcg_at_10_diff1
      value: 28.012456489936806
    - type: nauc_ndcg_at_10_max
      value: 38.045278212869825
    - type: nauc_ndcg_at_10_std
      value: 25.963041085823978
    - type: nauc_ndcg_at_1_diff1
      value: 35.99513984271449
    - type: nauc_ndcg_at_1_max
      value: 36.62771507516844
    - type: nauc_ndcg_at_1_std
      value: 16.726124822038052
    - type: nauc_ndcg_at_20_diff1
      value: 28.012111240688963
    - type: nauc_ndcg_at_20_max
      value: 38.667107321330555
    - type: nauc_ndcg_at_20_std
      value: 28.198245721076976
    - type: nauc_ndcg_at_3_diff1
      value: 30.33073102826854
    - type: nauc_ndcg_at_3_max
      value: 37.995789997615354
    - type: nauc_ndcg_at_3_std
      value: 22.304331918813876
    - type: nauc_ndcg_at_5_diff1
      value: 29.141028641237632
    - type: nauc_ndcg_at_5_max
      value: 37.2113360591228
    - type: nauc_ndcg_at_5_std
      value: 23.53066714165745
    - type: nauc_precision_at_1000_diff1
      value: -1.0646702024743917
    - type: nauc_precision_at_1000_max
      value: 19.304218995700534
    - type: nauc_precision_at_1000_std
      value: 31.73840122818843
    - type: nauc_precision_at_100_diff1
      value: 5.427804568412734
    - type: nauc_precision_at_100_max
      value: 27.90881278884377
    - type: nauc_precision_at_100_std
      value: 38.45326235114876
    - type: nauc_precision_at_10_diff1
      value: 14.252021242340863
    - type: nauc_precision_at_10_max
      value: 32.047078663067914
    - type: nauc_precision_at_10_std
      value: 30.621835328899426
    - type: nauc_precision_at_1_diff1
      value: 35.99513984271449
    - type: nauc_precision_at_1_max
      value: 36.62771507516844
    - type: nauc_precision_at_1_std
      value: 16.726124822038052
    - type: nauc_precision_at_20_diff1
      value: 12.017354269524972
    - type: nauc_precision_at_20_max
      value: 29.906152963561322
    - type: nauc_precision_at_20_std
      value: 33.764105037332264
    - type: nauc_precision_at_3_diff1
      value: 23.486354895398577
    - type: nauc_precision_at_3_max
      value: 38.45096435794749
    - type: nauc_precision_at_3_std
      value: 26.636452479567645
    - type: nauc_precision_at_5_diff1
      value: 19.574760607896973
    - type: nauc_precision_at_5_max
      value: 34.51474571826715
    - type: nauc_precision_at_5_std
      value: 28.514859235740904
    - type: nauc_recall_at_1000_diff1
      value: 12.801905007251246
    - type: nauc_recall_at_1000_max
      value: 37.49463996225108
    - type: nauc_recall_at_1000_std
      value: 45.46087045204742
    - type: nauc_recall_at_100_diff1
      value: 15.082886168560034
    - type: nauc_recall_at_100_max
      value: 35.720813725614
    - type: nauc_recall_at_100_std
      value: 39.876934524809215
    - type: nauc_recall_at_10_diff1
      value: 20.08086437796489
    - type: nauc_recall_at_10_max
      value: 33.418507169063815
    - type: nauc_recall_at_10_std
      value: 27.309080075299562
    - type: nauc_recall_at_1_diff1
      value: 38.13786017193742
    - type: nauc_recall_at_1_max
      value: 34.897924276187446
    - type: nauc_recall_at_1_std
      value: 15.197914019142733
    - type: nauc_recall_at_20_diff1
      value: 18.984980462200134
    - type: nauc_recall_at_20_max
      value: 32.95474022914299
    - type: nauc_recall_at_20_std
      value: 30.77553423574554
    - type: nauc_recall_at_3_diff1
      value: 26.670776366276865
    - type: nauc_recall_at_3_max
      value: 37.07230392845629
    - type: nauc_recall_at_3_std
      value: 23.385309818709757
    - type: nauc_recall_at_5_diff1
      value: 23.45569235165577
    - type: nauc_recall_at_5_max
      value: 34.014688386664524
    - type: nauc_recall_at_5_std
      value: 24.50194439244803
    - type: ndcg_at_1
      value: 23.974
    - type: ndcg_at_10
      value: 25.713
    - type: ndcg_at_100
      value: 32.349
    - type: ndcg_at_1000
      value: 35.615
    - type: ndcg_at_20
      value: 28.28
    - type: ndcg_at_3
      value: 20.761
    - type: ndcg_at_5
      value: 22.225
    - type: precision_at_1
      value: 23.974
    - type: precision_at_10
      value: 8.052
    - type: precision_at_100
      value: 1.5110000000000001
    - type: precision_at_1000
      value: 0.211
    - type: precision_at_20
      value: 5.106999999999999
    - type: precision_at_3
      value: 15.157000000000002
    - type: precision_at_5
      value: 11.557
    - type: recall_at_1
      value: 10.995000000000001
    - type: recall_at_10
      value: 31.05
    - type: recall_at_100
      value: 54.233
    - type: recall_at_1000
      value: 72.75500000000001
    - type: recall_at_20
      value: 38.442
    - type: recall_at_3
      value: 18.839
    - type: recall_at_5
      value: 23.26
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia (default)
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: test
      type: mteb/dbpedia
    metrics:
    - type: main_score
      value: 40.091
    - type: map_at_1
      value: 8.112
    - type: map_at_10
      value: 18.911
    - type: map_at_100
      value: 27.29
    - type: map_at_1000
      value: 28.749000000000002
    - type: map_at_20
      value: 22.187
    - type: map_at_3
      value: 13.177
    - type: map_at_5
      value: 15.723999999999998
    - type: mrr_at_1
      value: 64.75
    - type: mrr_at_10
      value: 73.0328373015873
    - type: mrr_at_100
      value: 73.3904467983012
    - type: mrr_at_1000
      value: 73.40582528487944
    - type: mrr_at_20
      value: 73.25613317925624
    - type: mrr_at_3
      value: 71.58333333333333
    - type: mrr_at_5
      value: 72.52083333333333
    - type: nauc_map_at_1000_diff1
      value: 30.326073419291667
    - type: nauc_map_at_1000_max
      value: 41.2485655499243
    - type: nauc_map_at_1000_std
      value: 34.68797882732488
    - type: nauc_map_at_100_diff1
      value: 30.250567651424635
    - type: nauc_map_at_100_max
      value: 39.591743243203275
    - type: nauc_map_at_100_std
      value: 32.14962028433263
    - type: nauc_map_at_10_diff1
      value: 28.30330426974147
    - type: nauc_map_at_10_max
      value: 24.685858800003153
    - type: nauc_map_at_10_std
      value: 6.991461788881313
    - type: nauc_map_at_1_diff1
      value: 37.84825245885128
    - type: nauc_map_at_1_max
      value: 10.784383140794167
    - type: nauc_map_at_1_std
      value: -12.413788028731759
    - type: nauc_map_at_20_diff1
      value: 30.56644002866712
    - type: nauc_map_at_20_max
      value: 32.09850095008104
    - type: nauc_map_at_20_std
      value: 17.68312732143373
    - type: nauc_map_at_3_diff1
      value: 26.94636553986902
    - type: nauc_map_at_3_max
      value: 13.716258156642672
    - type: nauc_map_at_3_std
      value: -7.919396887763491
    - type: nauc_map_at_5_diff1
      value: 26.703766272524305
    - type: nauc_map_at_5_max
      value: 18.493432579075815
    - type: nauc_map_at_5_std
      value: -1.7953102028408285
    - type: nauc_mrr_at_1000_diff1
      value: 56.5585700690547
    - type: nauc_mrr_at_1000_max
      value: 68.59723304665478
    - type: nauc_mrr_at_1000_std
      value: 41.65741817361127
    - type: nauc_mrr_at_100_diff1
      value: 56.56488475063903
    - type: nauc_mrr_at_100_max
      value: 68.59436880973041
    - type: nauc_mrr_at_100_std
      value: 41.64008885243909
    - type: nauc_mrr_at_10_diff1
      value: 56.57992847970396
    - type: nauc_mrr_at_10_max
      value: 68.54809322422658
    - type: nauc_mrr_at_10_std
      value: 41.637196787701605
    - type: nauc_mrr_at_1_diff1
      value: 59.49013430944212
    - type: nauc_mrr_at_1_max
      value: 67.51266363522255
    - type: nauc_mrr_at_1_std
      value: 39.159077933489094
    - type: nauc_mrr_at_20_diff1
      value: 56.322141799066195
    - type: nauc_mrr_at_20_max
      value: 68.41241085079113
    - type: nauc_mrr_at_20_std
      value: 41.74023776153815
    - type: nauc_mrr_at_3_diff1
      value: 56.43465566121455
    - type: nauc_mrr_at_3_max
      value: 69.32027688455301
    - type: nauc_mrr_at_3_std
      value: 42.35441414676036
    - type: nauc_mrr_at_5_diff1
      value: 56.185426652218126
    - type: nauc_mrr_at_5_max
      value: 68.68507625781251
    - type: nauc_mrr_at_5_std
      value: 42.227673261247816
    - type: nauc_ndcg_at_1000_diff1
      value: 38.452991805224926
    - type: nauc_ndcg_at_1000_max
      value: 55.49295294630129
    - type: nauc_ndcg_at_1000_std
      value: 47.669258273236046
    - type: nauc_ndcg_at_100_diff1
      value: 37.94112950003329
    - type: nauc_ndcg_at_100_max
      value: 50.68816850295493
    - type: nauc_ndcg_at_100_std
      value: 40.72315230606931
    - type: nauc_ndcg_at_10_diff1
      value: 38.47467764455152
    - type: nauc_ndcg_at_10_max
      value: 49.25673297040027
    - type: nauc_ndcg_at_10_std
      value: 36.76815739343767
    - type: nauc_ndcg_at_1_diff1
      value: 54.434593584664995
    - type: nauc_ndcg_at_1_max
      value: 57.61369658753043
    - type: nauc_ndcg_at_1_std
      value: 33.10284117958805
    - type: nauc_ndcg_at_20_diff1
      value: 38.3053661549299
    - type: nauc_ndcg_at_20_max
      value: 49.26702623701029
    - type: nauc_ndcg_at_20_std
      value: 36.78366426340987
    - type: nauc_ndcg_at_3_diff1
      value: 38.34783510078573
    - type: nauc_ndcg_at_3_max
      value: 51.181351973892085
    - type: nauc_ndcg_at_3_std
      value: 35.13771937716931
    - type: nauc_ndcg_at_5_diff1
      value: 38.73137682217783
    - type: nauc_ndcg_at_5_max
      value: 51.289826741923875
    - type: nauc_ndcg_at_5_std
      value: 36.76670998246709
    - type: nauc_precision_at_1000_diff1
      value: -8.37698697546597
    - type: nauc_precision_at_1000_max
      value: 4.649648259545355
    - type: nauc_precision_at_1000_std
      value: 15.100762512885371
    - type: nauc_precision_at_100_diff1
      value: 4.538510496829277
    - type: nauc_precision_at_100_max
      value: 33.573044920932965
    - type: nauc_precision_at_100_std
      value: 50.15177354474223
    - type: nauc_precision_at_10_diff1
      value: 16.03217990213501
    - type: nauc_precision_at_10_max
      value: 45.22978979054545
    - type: nauc_precision_at_10_std
      value: 53.103286665555295
    - type: nauc_precision_at_1_diff1
      value: 59.49013430944212
    - type: nauc_precision_at_1_max
      value: 67.51266363522255
    - type: nauc_precision_at_1_std
      value: 39.159077933489094
    - type: nauc_precision_at_20_diff1
      value: 13.705605238285958
    - type: nauc_precision_at_20_max
      value: 44.08365262009368
    - type: nauc_precision_at_20_std
      value: 56.050420219607155
    - type: nauc_precision_at_3_diff1
      value: 21.409861522316014
    - type: nauc_precision_at_3_max
      value: 48.93702948445578
    - type: nauc_precision_at_3_std
      value: 42.8419067771303
    - type: nauc_precision_at_5_diff1
      value: 20.1310639195609
    - type: nauc_precision_at_5_max
      value: 49.59134352761235
    - type: nauc_precision_at_5_std
      value: 48.98546957350543
    - type: nauc_recall_at_1000_diff1
      value: 27.181172941984112
    - type: nauc_recall_at_1000_max
      value: 49.20832060504127
    - type: nauc_recall_at_1000_std
      value: 50.58754027710416
    - type: nauc_recall_at_100_diff1
      value: 25.831239736658713
    - type: nauc_recall_at_100_max
      value: 37.92978899965714
    - type: nauc_recall_at_100_std
      value: 32.84155059838547
    - type: nauc_recall_at_10_diff1
      value: 21.03971256731199
    - type: nauc_recall_at_10_max
      value: 16.34542184400448
    - type: nauc_recall_at_10_std
      value: 1.624004078039708
    - type: nauc_recall_at_1_diff1
      value: 37.84825245885128
    - type: nauc_recall_at_1_max
      value: 10.784383140794167
    - type: nauc_recall_at_1_std
      value: -12.413788028731759
    - type: nauc_recall_at_20_diff1
      value: 23.612410438391652
    - type: nauc_recall_at_20_max
      value: 24.731496668584725
    - type: nauc_recall_at_20_std
      value: 11.94162779763853
    - type: nauc_recall_at_3_diff1
      value: 21.124250217970754
    - type: nauc_recall_at_3_max
      value: 9.581953839031879
    - type: nauc_recall_at_3_std
      value: -9.955224094610848
    - type: nauc_recall_at_5_diff1
      value: 20.272821143755714
    - type: nauc_recall_at_5_max
      value: 12.80122421686649
    - type: nauc_recall_at_5_std
      value: -4.822509659730001
    - type: ndcg_at_1
      value: 52.87500000000001
    - type: ndcg_at_10
      value: 40.091
    - type: ndcg_at_100
      value: 45.007999999999996
    - type: ndcg_at_1000
      value: 51.522
    - type: ndcg_at_20
      value: 39.953
    - type: ndcg_at_3
      value: 44.627
    - type: ndcg_at_5
      value: 41.748000000000005
    - type: precision_at_1
      value: 64.75
    - type: precision_at_10
      value: 32.324999999999996
    - type: precision_at_100
      value: 10.583
    - type: precision_at_1000
      value: 1.992
    - type: precision_at_20
      value: 25.15
    - type: precision_at_3
      value: 48.5
    - type: precision_at_5
      value: 40.8
    - type: recall_at_1
      value: 8.112
    - type: recall_at_10
      value: 24.769
    - type: recall_at_100
      value: 51.92400000000001
    - type: recall_at_1000
      value: 72.60799999999999
    - type: recall_at_20
      value: 32.085
    - type: recall_at_3
      value: 14.707999999999998
    - type: recall_at_5
      value: 18.881
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB EmotionClassification (default)
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: test
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 74.88499999999999
    - type: f1
      value: 69.55769956653745
    - type: f1_weighted
      value: 75.98938892167276
    - type: main_score
      value: 74.88499999999999
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FEVER (default)
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
      split: test
      type: mteb/fever
    metrics:
    - type: main_score
      value: 86.088
    - type: map_at_1
      value: 74.21
    - type: map_at_10
      value: 82.238
    - type: map_at_100
      value: 82.467
    - type: map_at_1000
      value: 82.48
    - type: map_at_20
      value: 82.38
    - type: map_at_3
      value: 81.178
    - type: map_at_5
      value: 81.882
    - type: mrr_at_1
      value: 80.04800480048004
    - type: mrr_at_10
      value: 87.28162697222103
    - type: mrr_at_100
      value: 87.36425501689853
    - type: mrr_at_1000
      value: 87.36494888408146
    - type: mrr_at_20
      value: 87.33488767030532
    - type: mrr_at_3
      value: 86.5011501150115
    - type: mrr_at_5
      value: 87.04345434543454
    - type: nauc_map_at_1000_diff1
      value: 46.86807158039652
    - type: nauc_map_at_1000_max
      value: 17.537735239936584
    - type: nauc_map_at_1000_std
      value: -6.180991548000637
    - type: nauc_map_at_100_diff1
      value: 46.840981153123515
    - type: nauc_map_at_100_max
      value: 17.51241604543591
    - type: nauc_map_at_100_std
      value: -6.19572402233368
    - type: nauc_map_at_10_diff1
      value: 46.63164937877156
    - type: nauc_map_at_10_max
      value: 17.396231277218714
    - type: nauc_map_at_10_std
      value: -6.328960389468633
    - type: nauc_map_at_1_diff1
      value: 51.91442444295392
    - type: nauc_map_at_1_max
      value: 14.772868336313651
    - type: nauc_map_at_1_std
      value: -7.924628073687737
    - type: nauc_map_at_20_diff1
      value: 46.78996154399
    - type: nauc_map_at_20_max
      value: 17.52594082408568
    - type: nauc_map_at_20_std
      value: -6.2535816636418255
    - type: nauc_map_at_3_diff1
      value: 46.86720061616425
    - type: nauc_map_at_3_max
      value: 17.17282268255638
    - type: nauc_map_at_3_std
      value: -7.100454400283953
    - type: nauc_map_at_5_diff1
      value: 46.743320728340485
    - type: nauc_map_at_5_max
      value: 17.22026822962506
    - type: nauc_map_at_5_std
      value: -6.593983297795947
    - type: nauc_mrr_at_1000_diff1
      value: 64.22963921921831
    - type: nauc_mrr_at_1000_max
      value: 22.50147928007347
    - type: nauc_mrr_at_1000_std
      value: -10.753338651031981
    - type: nauc_mrr_at_100_diff1
      value: 64.22599646741416
    - type: nauc_mrr_at_100_max
      value: 22.49976292804203
    - type: nauc_mrr_at_100_std
      value: -10.753324625089736
    - type: nauc_mrr_at_10_diff1
      value: 64.24857003564016
    - type: nauc_mrr_at_10_max
      value: 22.721448283312323
    - type: nauc_mrr_at_10_std
      value: -10.698659951469375
    - type: nauc_mrr_at_1_diff1
      value: 65.80017393845672
    - type: nauc_mrr_at_1_max
      value: 19.56658619771462
    - type: nauc_mrr_at_1_std
      value: -10.691529848056236
    - type: nauc_mrr_at_20_diff1
      value: 64.22606211105564
    - type: nauc_mrr_at_20_max
      value: 22.60630203277465
    - type: nauc_mrr_at_20_std
      value: -10.698352035527936
    - type: nauc_mrr_at_3_diff1
      value: 64.03189495070804
    - type: nauc_mrr_at_3_max
      value: 23.197599099302078
    - type: nauc_mrr_at_3_std
      value: -10.941260656610341
    - type: nauc_mrr_at_5_diff1
      value: 64.21946450636831
    - type: nauc_mrr_at_5_max
      value: 22.869883457504613
    - type: nauc_mrr_at_5_std
      value: -10.773375222905306
    - type: nauc_ndcg_at_1000_diff1
      value: 48.18634946007256
    - type: nauc_ndcg_at_1000_max
      value: 19.635685645181443
    - type: nauc_ndcg_at_1000_std
      value: -5.008615485203909
    - type: nauc_ndcg_at_100_diff1
      value: 47.460702424024646
    - type: nauc_ndcg_at_100_max
      value: 19.197829510466093
    - type: nauc_ndcg_at_100_std
      value: -5.141098235552701
    - type: nauc_ndcg_at_10_diff1
      value: 46.75967320832195
    - type: nauc_ndcg_at_10_max
      value: 19.162998560532944
    - type: nauc_ndcg_at_10_std
      value: -5.680454888720109
    - type: nauc_ndcg_at_1_diff1
      value: 65.80017393845672
    - type: nauc_ndcg_at_1_max
      value: 19.56658619771462
    - type: nauc_ndcg_at_1_std
      value: -10.691529848056236
    - type: nauc_ndcg_at_20_diff1
      value: 47.15063801450417
    - type: nauc_ndcg_at_20_max
      value: 19.387976860064036
    - type: nauc_ndcg_at_20_std
      value: -5.434429887556901
    - type: nauc_ndcg_at_3_diff1
      value: 48.48013879703285
    - type: nauc_ndcg_at_3_max
      value: 19.563845683013074
    - type: nauc_ndcg_at_3_std
      value: -7.306366856511263
    - type: nauc_ndcg_at_5_diff1
      value: 47.4477936851643
    - type: nauc_ndcg_at_5_max
      value: 19.12745930840238
    - type: nauc_ndcg_at_5_std
      value: -6.338914655492511
    - type: nauc_precision_at_1000_diff1
      value: -4.975768805829236
    - type: nauc_precision_at_1000_max
      value: 10.078421203817527
    - type: nauc_precision_at_1000_std
      value: 10.15753365579419
    - type: nauc_precision_at_100_diff1
      value: -7.411336519288538
    - type: nauc_precision_at_100_max
      value: 11.116507499213043
    - type: nauc_precision_at_100_std
      value: 11.608241877542543
    - type: nauc_precision_at_10_diff1
      value: 2.6403449208341274
    - type: nauc_precision_at_10_max
      value: 20.668398953238633
    - type: nauc_precision_at_10_std
      value: 7.433281722501917
    - type: nauc_precision_at_1_diff1
      value: 65.80017393845672
    - type: nauc_precision_at_1_max
      value: 19.56658619771462
    - type: nauc_precision_at_1_std
      value: -10.691529848056236
    - type: nauc_precision_at_20_diff1
      value: -1.286553967637511
    - type: nauc_precision_at_20_max
      value: 17.30405603464926
    - type: nauc_precision_at_20_std
      value: 9.234773655809756
    - type: nauc_precision_at_3_diff1
      value: 31.364166410646675
    - type: nauc_precision_at_3_max
      value: 26.397101881343527
    - type: nauc_precision_at_3_std
      value: -5.0543954546843946
    - type: nauc_precision_at_5_diff1
      value: 17.1466778085294
    - type: nauc_precision_at_5_max
      value: 23.18905254179433
    - type: nauc_precision_at_5_std
      value: 1.6051724821489612
    - type: nauc_recall_at_1000_diff1
      value: -3.9377049069087935
    - type: nauc_recall_at_1000_max
      value: 27.168346654704095
    - type: nauc_recall_at_1000_std
      value: 38.58463265497753
    - type: nauc_recall_at_100_diff1
      value: -1.886570080947599
    - type: nauc_recall_at_100_max
      value: 16.12930964320666
    - type: nauc_recall_at_100_std
      value: 21.616391259129152
    - type: nauc_recall_at_10_diff1
      value: 15.941506685002588
    - type: nauc_recall_at_10_max
      value: 19.141995524332728
    - type: nauc_recall_at_10_std
      value: 5.860480767168416
    - type: nauc_recall_at_1_diff1
      value: 51.91442444295392
    - type: nauc_recall_at_1_max
      value: 14.772868336313651
    - type: nauc_recall_at_1_std
      value: -7.924628073687737
    - type: nauc_recall_at_20_diff1
      value: 11.583722825668058
    - type: nauc_recall_at_20_max
      value: 19.867221612869876
    - type: nauc_recall_at_20_std
      value: 10.141960757453084
    - type: nauc_recall_at_3_diff1
      value: 32.30936424972365
    - type: nauc_recall_at_3_max
      value: 20.11705236473992
    - type: nauc_recall_at_3_std
      value: -3.525144821962635
    - type: nauc_recall_at_5_diff1
      value: 25.68392975410304
    - type: nauc_recall_at_5_max
      value: 19.221295609032595
    - type: nauc_recall_at_5_std
      value: 0.576160647152633
    - type: ndcg_at_1
      value: 80.048
    - type: ndcg_at_10
      value: 86.088
    - type: ndcg_at_100
      value: 86.911
    - type: ndcg_at_1000
      value: 87.125
    - type: ndcg_at_20
      value: 86.468
    - type: ndcg_at_3
      value: 84.375
    - type: ndcg_at_5
      value: 85.384
    - type: precision_at_1
      value: 80.048
    - type: precision_at_10
      value: 10.236
    - type: precision_at_100
      value: 1.085
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_20
      value: 5.2330000000000005
    - type: precision_at_3
      value: 32.078
    - type: precision_at_5
      value: 19.895
    - type: recall_at_1
      value: 74.21
    - type: recall_at_10
      value: 93.077
    - type: recall_at_100
      value: 96.348
    - type: recall_at_1000
      value: 97.65700000000001
    - type: recall_at_20
      value: 94.36099999999999
    - type: recall_at_3
      value: 88.337
    - type: recall_at_5
      value: 90.948
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA2018 (default)
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: test
      type: mteb/fiqa
    metrics:
    - type: main_score
      value: 45.405
    - type: map_at_1
      value: 22.325
    - type: map_at_10
      value: 36.975
    - type: map_at_100
      value: 38.846000000000004
    - type: map_at_1000
      value: 39.012
    - type: map_at_20
      value: 37.958999999999996
    - type: map_at_3
      value: 32.208
    - type: map_at_5
      value: 34.928
    - type: mrr_at_1
      value: 44.29012345679013
    - type: mrr_at_10
      value: 54.02030668234372
    - type: mrr_at_100
      value: 54.72897336245347
    - type: mrr_at_1000
      value: 54.76320283944561
    - type: mrr_at_20
      value: 54.50419077165938
    - type: mrr_at_3
      value: 51.41460905349795
    - type: mrr_at_5
      value: 53.11213991769548
    - type: nauc_map_at_1000_diff1
      value: 42.33950505310022
    - type: nauc_map_at_1000_max
      value: 32.814158723141745
    - type: nauc_map_at_1000_std
      value: -4.5297230544932825
    - type: nauc_map_at_100_diff1
      value: 42.316327406548695
    - type: nauc_map_at_100_max
      value: 32.706900013479725
    - type: nauc_map_at_100_std
      value: -4.564571222935577
    - type: nauc_map_at_10_diff1
      value: 42.17734361420548
    - type: nauc_map_at_10_max
      value: 31.527366385827854
    - type: nauc_map_at_10_std
      value: -5.559289874353945
    - type: nauc_map_at_1_diff1
      value: 47.33003471166015
    - type: nauc_map_at_1_max
      value: 21.535228737020457
    - type: nauc_map_at_1_std
      value: -11.649016586524858
    - type: nauc_map_at_20_diff1
      value: 42.11015618170868
    - type: nauc_map_at_20_max
      value: 32.18582282622051
    - type: nauc_map_at_20_std
      value: -5.042968429993695
    - type: nauc_map_at_3_diff1
      value: 43.26686524198236
    - type: nauc_map_at_3_max
      value: 28.849395895564083
    - type: nauc_map_at_3_std
      value: -6.976952334117308
    - type: nauc_map_at_5_diff1
      value: 42.95893517901293
    - type: nauc_map_at_5_max
      value: 30.871999781837612
    - type: nauc_map_at_5_std
      value: -6.149645006139908
    - type: nauc_mrr_at_1000_diff1
      value: 51.23708914241626
    - type: nauc_mrr_at_1000_max
      value: 40.298960389709
    - type: nauc_mrr_at_1000_std
      value: -5.188577391773796
    - type: nauc_mrr_at_100_diff1
      value: 51.24001351681103
    - type: nauc_mrr_at_100_max
      value: 40.318755039260886
    - type: nauc_mrr_at_100_std
      value: -5.164744512057911
    - type: nauc_mrr_at_10_diff1
      value: 51.116323465364566
    - type: nauc_mrr_at_10_max
      value: 40.18322650792177
    - type: nauc_mrr_at_10_std
      value: -5.42707335446156
    - type: nauc_mrr_at_1_diff1
      value: 54.623685354463625
    - type: nauc_mrr_at_1_max
      value: 38.52800456113852
    - type: nauc_mrr_at_1_std
      value: -8.561342078884513
    - type: nauc_mrr_at_20_diff1
      value: 51.082878864924076
    - type: nauc_mrr_at_20_max
      value: 40.25224355621811
    - type: nauc_mrr_at_20_std
      value: -5.1386035874860925
    - type: nauc_mrr_at_3_diff1
      value: 51.28771495504919
    - type: nauc_mrr_at_3_max
      value: 40.167661702884644
    - type: nauc_mrr_at_3_std
      value: -6.672938174195537
    - type: nauc_mrr_at_5_diff1
      value: 51.386811950131026
    - type: nauc_mrr_at_5_max
      value: 40.29452825209631
    - type: nauc_mrr_at_5_std
      value: -6.134184637482388
    - type: nauc_ndcg_at_1000_diff1
      value: 44.46948002237412
    - type: nauc_ndcg_at_1000_max
      value: 37.882877667376576
    - type: nauc_ndcg_at_1000_std
      value: -0.2441149985965938
    - type: nauc_ndcg_at_100_diff1
      value: 43.96014037390138
    - type: nauc_ndcg_at_100_max
      value: 36.96423036666587
    - type: nauc_ndcg_at_100_std
      value: 0.21228554480998071
    - type: nauc_ndcg_at_10_diff1
      value: 42.889923047150226
    - type: nauc_ndcg_at_10_max
      value: 33.95406097914127
    - type: nauc_ndcg_at_10_std
      value: -3.3077129078149796
    - type: nauc_ndcg_at_1_diff1
      value: 54.623685354463625
    - type: nauc_ndcg_at_1_max
      value: 38.52800456113852
    - type: nauc_ndcg_at_1_std
      value: -8.561342078884513
    - type: nauc_ndcg_at_20_diff1
      value: 42.806846626799626
    - type: nauc_ndcg_at_20_max
      value: 35.01566424207401
    - type: nauc_ndcg_at_20_std
      value: -2.01466646308545
    - type: nauc_ndcg_at_3_diff1
      value: 43.29070711758635
    - type: nauc_ndcg_at_3_max
      value: 35.81474510295669
    - type: nauc_ndcg_at_3_std
      value: -4.937712863159993
    - type: nauc_ndcg_at_5_diff1
      value: 43.533204764747346
    - type: nauc_ndcg_at_5_max
      value: 34.67200578229001
    - type: nauc_ndcg_at_5_std
      value: -4.220153646752217
    - type: nauc_precision_at_1000_diff1
      value: -0.24162611684046686
    - type: nauc_precision_at_1000_max
      value: 26.610031730319122
    - type: nauc_precision_at_1000_std
      value: 12.85473387814076
    - type: nauc_precision_at_100_diff1
      value: 6.593767812518609
    - type: nauc_precision_at_100_max
      value: 32.89478475065496
    - type: nauc_precision_at_100_std
      value: 16.66995461135905
    - type: nauc_precision_at_10_diff1
      value: 17.48446148168886
    - type: nauc_precision_at_10_max
      value: 36.54732448382068
    - type: nauc_precision_at_10_std
      value: 6.7478320020402
    - type: nauc_precision_at_1_diff1
      value: 54.623685354463625
    - type: nauc_precision_at_1_max
      value: 38.52800456113852
    - type: nauc_precision_at_1_std
      value: -8.561342078884513
    - type: nauc_precision_at_20_diff1
      value: 13.039974734569537
    - type: nauc_precision_at_20_max
      value: 36.49695572253983
    - type: nauc_precision_at_20_std
      value: 10.476938728091008
    - type: nauc_precision_at_3_diff1
      value: 30.19928557150241
    - type: nauc_precision_at_3_max
      value: 38.897101267116554
    - type: nauc_precision_at_3_std
      value: 1.121533090916794
    - type: nauc_precision_at_5_diff1
      value: 25.33029636435617
    - type: nauc_precision_at_5_max
      value: 39.59677600835699
    - type: nauc_precision_at_5_std
      value: 3.4416095155763244
    - type: nauc_recall_at_1000_diff1
      value: 34.823080033440434
    - type: nauc_recall_at_1000_max
      value: 43.87066795154745
    - type: nauc_recall_at_1000_std
      value: 42.23182031662749
    - type: nauc_recall_at_100_diff1
      value: 30.70809572521992
    - type: nauc_recall_at_100_max
      value: 31.598064007837852
    - type: nauc_recall_at_100_std
      value: 20.758185821213164
    - type: nauc_recall_at_10_diff1
      value: 30.674660204386957
    - type: nauc_recall_at_10_max
      value: 25.13675931430177
    - type: nauc_recall_at_10_std
      value: 1.1493152709013974
    - type: nauc_recall_at_1_diff1
      value: 47.33003471166015
    - type: nauc_recall_at_1_max
      value: 21.535228737020457
    - type: nauc_recall_at_1_std
      value: -11.649016586524858
    - type: nauc_recall_at_20_diff1
      value: 28.60023313868174
    - type: nauc_recall_at_20_max
      value: 26.576577612640655
    - type: nauc_recall_at_20_std
      value: 6.331498880910594
    - type: nauc_recall_at_3_diff1
      value: 36.61359637854836
    - type: nauc_recall_at_3_max
      value: 26.205709444189345
    - type: nauc_recall_at_3_std
      value: -4.41772315378875
    - type: nauc_recall_at_5_diff1
      value: 34.721622588958894
    - type: nauc_recall_at_5_max
      value: 26.870375540274104
    - type: nauc_recall_at_5_std
      value: -1.2959303042762926
    - type: ndcg_at_1
      value: 44.29
    - type: ndcg_at_10
      value: 45.405
    - type: ndcg_at_100
      value: 52.027
    - type: ndcg_at_1000
      value: 54.688
    - type: ndcg_at_20
      value: 47.967999999999996
    - type: ndcg_at_3
      value: 41.496
    - type: ndcg_at_5
      value: 42.902
    - type: precision_at_1
      value: 44.29
    - type: precision_at_10
      value: 12.469
    - type: precision_at_100
      value: 1.9349999999999998
    - type: precision_at_1000
      value: 0.243
    - type: precision_at_20
      value: 7.323
    - type: precision_at_3
      value: 27.622999999999998
    - type: precision_at_5
      value: 20.34
    - type: recall_at_1
      value: 22.325
    - type: recall_at_10
      value: 52.788999999999994
    - type: recall_at_100
      value: 77.274
    - type: recall_at_1000
      value: 92.94
    - type: recall_at_20
      value: 60.714
    - type: recall_at_3
      value: 37.502
    - type: recall_at_5
      value: 44.808
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA (default)
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
      split: test
      type: mteb/hotpotqa
    metrics:
    - type: main_score
      value: 66.661
    - type: map_at_1
      value: 41.418
    - type: map_at_10
      value: 57.086999999999996
    - type: map_at_100
      value: 57.888
    - type: map_at_1000
      value: 57.955
    - type: map_at_20
      value: 57.544
    - type: map_at_3
      value: 54.112
    - type: map_at_5
      value: 55.942
    - type: mrr_at_1
      value: 82.79540850776502
    - type: mrr_at_10
      value: 87.24545298650632
    - type: mrr_at_100
      value: 87.3943716521154
    - type: mrr_at_1000
      value: 87.40052014901985
    - type: mrr_at_20
      value: 87.3376988773675
    - type: mrr_at_3
      value: 86.54287643484132
    - type: mrr_at_5
      value: 87.0162052667117
    - type: nauc_map_at_1000_diff1
      value: 13.347058320450778
    - type: nauc_map_at_1000_max
      value: 19.172918193696585
    - type: nauc_map_at_1000_std
      value: 1.6085652199402172
    - type: nauc_map_at_100_diff1
      value: 13.309459563369677
    - type: nauc_map_at_100_max
      value: 19.142490361521045
    - type: nauc_map_at_100_std
      value: 1.5997757026480046
    - type: nauc_map_at_10_diff1
      value: 13.821467981397284
    - type: nauc_map_at_10_max
      value: 19.47388049912085
    - type: nauc_map_at_10_std
      value: 0.7945082440633815
    - type: nauc_map_at_1_diff1
      value: 80.17822133984255
    - type: nauc_map_at_1_max
      value: 56.93232002015388
    - type: nauc_map_at_1_std
      value: -9.565010407038201
    - type: nauc_map_at_20_diff1
      value: 13.447193497393146
    - type: nauc_map_at_20_max
      value: 19.208078541028097
    - type: nauc_map_at_20_std
      value: 1.2699537557176803
    - type: nauc_map_at_3_diff1
      value: 16.854345839107967
    - type: nauc_map_at_3_max
      value: 21.648192526975727
    - type: nauc_map_at_3_std
      value: -0.6137487567045511
    - type: nauc_map_at_5_diff1
      value: 14.543663008536509
    - type: nauc_map_at_5_max
      value: 20.155541895741532
    - type: nauc_map_at_5_std
      value: 0.25148082760110224
    - type: nauc_mrr_at_1000_diff1
      value: 79.11825919796162
    - type: nauc_mrr_at_1000_max
      value: 60.10563640048739
    - type: nauc_mrr_at_1000_std
      value: -6.726621618014327
    - type: nauc_mrr_at_100_diff1
      value: 79.11854278578646
    - type: nauc_mrr_at_100_max
      value: 60.11377258817985
    - type: nauc_mrr_at_100_std
      value: -6.704065951576038
    - type: nauc_mrr_at_10_diff1
      value: 79.07961808239499
    - type: nauc_mrr_at_10_max
      value: 60.2138079214177
    - type: nauc_mrr_at_10_std
      value: -6.74779578820509
    - type: nauc_mrr_at_1_diff1
      value: 80.25371155548501
    - type: nauc_mrr_at_1_max
      value: 57.01027352172217
    - type: nauc_mrr_at_1_std
      value: -9.682353752598317
    - type: nauc_mrr_at_20_diff1
      value: 79.08786670986484
    - type: nauc_mrr_at_20_max
      value: 60.139471646688925
    - type: nauc_mrr_at_20_std
      value: -6.720404576075471
    - type: nauc_mrr_at_3_diff1
      value: 78.93741620023842
    - type: nauc_mrr_at_3_max
      value: 60.31902114928829
    - type: nauc_mrr_at_3_std
      value: -7.066082480981481
    - type: nauc_mrr_at_5_diff1
      value: 79.06255305350973
    - type: nauc_mrr_at_5_max
      value: 60.344631571197546
    - type: nauc_mrr_at_5_std
      value: -6.788165280997917
    - type: nauc_ndcg_at_1000_diff1
      value: 17.006951693217548
    - type: nauc_ndcg_at_1000_max
      value: 21.854859924097646
    - type: nauc_ndcg_at_1000_std
      value: 4.70138835806943
    - type: nauc_ndcg_at_100_diff1
      value: 16.195007796313384
    - type: nauc_ndcg_at_100_max
      value: 21.264332841663858
    - type: nauc_ndcg_at_100_std
      value: 4.620999926841355
    - type: nauc_ndcg_at_10_diff1
      value: 18.327522629298294
    - type: nauc_ndcg_at_10_max
      value: 22.686509071566917
    - type: nauc_ndcg_at_10_std
      value: 1.5527071297942836
    - type: nauc_ndcg_at_1_diff1
      value: 80.17822133984255
    - type: nauc_ndcg_at_1_max
      value: 56.93232002015388
    - type: nauc_ndcg_at_1_std
      value: -9.565010407038201
    - type: nauc_ndcg_at_20_diff1
      value: 17.11074173500959
    - type: nauc_ndcg_at_20_max
      value: 21.81160814631424
    - type: nauc_ndcg_at_20_std
      value: 2.858829825220597
    - type: nauc_ndcg_at_3_diff1
      value: 23.797089205140068
    - type: nauc_ndcg_at_3_max
      value: 26.659269305908296
    - type: nauc_ndcg_at_3_std
      value: -0.7545654502076451
    - type: nauc_ndcg_at_5_diff1
      value: 20.067483031938934
    - type: nauc_ndcg_at_5_max
      value: 24.23026610511652
    - type: nauc_ndcg_at_5_std
      value: 0.5097749208107711
    - type: nauc_precision_at_1000_diff1
      value: -21.807728330326697
    - type: nauc_precision_at_1000_max
      value: -2.9835997103120344
    - type: nauc_precision_at_1000_std
      value: 25.81739799194849
    - type: nauc_precision_at_100_diff1
      value: -16.05478872817429
    - type: nauc_precision_at_100_max
      value: 0.2665969008515287
    - type: nauc_precision_at_100_std
      value: 19.352798394287323
    - type: nauc_precision_at_10_diff1
      value: -3.3507602135961037
    - type: nauc_precision_at_10_max
      value: 8.867034772304718
    - type: nauc_precision_at_10_std
      value: 6.545361194526079
    - type: nauc_precision_at_1_diff1
      value: 80.17822133984255
    - type: nauc_precision_at_1_max
      value: 56.93232002015388
    - type: nauc_precision_at_1_std
      value: -9.565010407038201
    - type: nauc_precision_at_20_diff1
      value: -7.902542409127802
    - type: nauc_precision_at_20_max
      value: 5.62428878283396
    - type: nauc_precision_at_20_std
      value: 10.592045512127914
    - type: nauc_precision_at_3_diff1
      value: 8.132713424441485
    - type: nauc_precision_at_3_max
      value: 17.99416677485544
    - type: nauc_precision_at_3_std
      value: 1.9785114664304215
    - type: nauc_precision_at_5_diff1
      value: 1.38596734740728
    - type: nauc_precision_at_5_max
      value: 13.214138500817723
    - type: nauc_precision_at_5_std
      value: 4.15378198762281
    - type: nauc_recall_at_1000_diff1
      value: -21.807728330326455
    - type: nauc_recall_at_1000_max
      value: -2.9835997103117293
    - type: nauc_recall_at_1000_std
      value: 25.8173979919487
    - type: nauc_recall_at_100_diff1
      value: -16.054788728174266
    - type: nauc_recall_at_100_max
      value: 0.26659690085157123
    - type: nauc_recall_at_100_std
      value: 19.35279839428729
    - type: nauc_recall_at_10_diff1
      value: -3.350760213596107
    - type: nauc_recall_at_10_max
      value: 8.86703477230471
    - type: nauc_recall_at_10_std
      value: 6.5453611945261505
    - type: nauc_recall_at_1_diff1
      value: 80.17822133984255
    - type: nauc_recall_at_1_max
      value: 56.93232002015388
    - type: nauc_recall_at_1_std
      value: -9.565010407038201
    - type: nauc_recall_at_20_diff1
      value: -7.902542409127704
    - type: nauc_recall_at_20_max
      value: 5.6242887828340375
    - type: nauc_recall_at_20_std
      value: 10.592045512127953
    - type: nauc_recall_at_3_diff1
      value: 8.132713424441446
    - type: nauc_recall_at_3_max
      value: 17.99416677485538
    - type: nauc_recall_at_3_std
      value: 1.9785114664303751
    - type: nauc_recall_at_5_diff1
      value: 1.3859673474071779
    - type: nauc_recall_at_5_max
      value: 13.214138500817668
    - type: nauc_recall_at_5_std
      value: 4.153781987622754
    - type: ndcg_at_1
      value: 82.836
    - type: ndcg_at_10
      value: 66.661
    - type: ndcg_at_100
      value: 69.42399999999999
    - type: ndcg_at_1000
      value: 70.722
    - type: ndcg_at_20
      value: 67.777
    - type: ndcg_at_3
      value: 62.517
    - type: ndcg_at_5
      value: 64.79700000000001
    - type: precision_at_1
      value: 82.836
    - type: precision_at_10
      value: 13.350000000000001
    - type: precision_at_100
      value: 1.552
    - type: precision_at_1000
      value: 0.172
    - type: precision_at_20
      value: 7.034
    - type: precision_at_3
      value: 38.375
    - type: precision_at_5
      value: 24.829
    - type: recall_at_1
      value: 41.418
    - type: recall_at_10
      value: 66.752
    - type: recall_at_100
      value: 77.576
    - type: recall_at_1000
      value: 86.199
    - type: recall_at_20
      value: 70.338
    - type: recall_at_3
      value: 57.562000000000005
    - type: recall_at_5
      value: 62.073
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ImdbClassification (default)
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
      split: test
      type: mteb/imdb
    metrics:
    - type: accuracy
      value: 93.58840000000001
    - type: ap
      value: 90.234834378287
    - type: ap_weighted
      value: 90.234834378287
    - type: f1
      value: 93.58346966422063
    - type: f1_weighted
      value: 93.58346966422063
    - type: main_score
      value: 93.58840000000001
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MSMARCO (default)
      revision: c5a29a104738b98a9e76336939199e264163d4a0
      split: dev
      type: mteb/msmarco
    metrics:
    - type: main_score
      value: 41.48
    - type: map_at_1
      value: 22.078999999999997
    - type: map_at_10
      value: 34.416000000000004
    - type: map_at_100
      value: 35.541
    - type: map_at_1000
      value: 35.592
    - type: map_at_20
      value: 35.106
    - type: map_at_3
      value: 30.470000000000002
    - type: map_at_5
      value: 32.774
    - type: mrr_at_1
      value: 22.693409742120345
    - type: mrr_at_10
      value: 35.02055760221949
    - type: mrr_at_100
      value: 36.07282466487795
    - type: mrr_at_1000
      value: 36.11725121701468
    - type: mrr_at_20
      value: 35.667140877547986
    - type: mrr_at_3
      value: 31.122254059216814
    - type: mrr_at_5
      value: 33.40592168099331
    - type: nauc_map_at_1000_diff1
      value: 33.00333472064972
    - type: nauc_map_at_1000_max
      value: 5.156444947074947
    - type: nauc_map_at_1000_std
      value: -23.103939979826375
    - type: nauc_map_at_100_diff1
      value: 32.99943906977456
    - type: nauc_map_at_100_max
      value: 5.156792638157342
    - type: nauc_map_at_100_std
      value: -23.09927789432014
    - type: nauc_map_at_10_diff1
      value: 32.93427060211673
    - type: nauc_map_at_10_max
      value: 5.009847068055439
    - type: nauc_map_at_10_std
      value: -23.69229778425936
    - type: nauc_map_at_1_diff1
      value: 35.879541770806426
    - type: nauc_map_at_1_max
      value: 4.037000551161811
    - type: nauc_map_at_1_std
      value: -21.066913542507095
    - type: nauc_map_at_20_diff1
      value: 32.94459306136245
    - type: nauc_map_at_20_max
      value: 5.08450123260384
    - type: nauc_map_at_20_std
      value: -23.367858842401674
    - type: nauc_map_at_3_diff1
      value: 33.186734646971495
    - type: nauc_map_at_3_max
      value: 4.52958372002426
    - type: nauc_map_at_3_std
      value: -23.407182657661863
    - type: nauc_map_at_5_diff1
      value: 33.09447602825229
    - type: nauc_map_at_5_max
      value: 4.8295482352066275
    - type: nauc_map_at_5_std
      value: -23.977226416616457
    - type: nauc_mrr_at_1000_diff1
      value: 32.90248885790994
    - type: nauc_mrr_at_1000_max
      value: 5.345915497836417
    - type: nauc_mrr_at_1000_std
      value: -22.775176728644926
    - type: nauc_mrr_at_100_diff1
      value: 32.89830733234614
    - type: nauc_mrr_at_100_max
      value: 5.354794932204688
    - type: nauc_mrr_at_100_std
      value: -22.76281634843283
    - type: nauc_mrr_at_10_diff1
      value: 32.85362740239939
    - type: nauc_mrr_at_10_max
      value: 5.22277263020967
    - type: nauc_mrr_at_10_std
      value: -23.29890783663585
    - type: nauc_mrr_at_1_diff1
      value: 35.8004961400585
    - type: nauc_mrr_at_1_max
      value: 4.07480515690297
    - type: nauc_mrr_at_1_std
      value: -21.157419860722133
    - type: nauc_mrr_at_20_diff1
      value: 32.831058277421675
    - type: nauc_mrr_at_20_max
      value: 5.30231502729234
    - type: nauc_mrr_at_20_std
      value: -22.995188734787643
    - type: nauc_mrr_at_3_diff1
      value: 33.06512398614513
    - type: nauc_mrr_at_3_max
      value: 4.6832127086497675
    - type: nauc_mrr_at_3_std
      value: -23.185466086324016
    - type: nauc_mrr_at_5_diff1
      value: 32.95656016095678
    - type: nauc_mrr_at_5_max
      value: 5.0055516099566475
    - type: nauc_mrr_at_5_std
      value: -23.648076417104612
    - type: nauc_ndcg_at_1000_diff1
      value: 32.23911068627994
    - type: nauc_ndcg_at_1000_max
      value: 6.340890121521923
    - type: nauc_ndcg_at_1000_std
      value: -21.64542687396577
    - type: nauc_ndcg_at_100_diff1
      value: 32.11878167303473
    - type: nauc_ndcg_at_100_max
      value: 6.597128552520879
    - type: nauc_ndcg_at_100_std
      value: -21.03041945862791
    - type: nauc_ndcg_at_10_diff1
      value: 31.78511231016483
    - type: nauc_ndcg_at_10_max
      value: 5.784417481640047
    - type: nauc_ndcg_at_10_std
      value: -24.161027978905647
    - type: nauc_ndcg_at_1_diff1
      value: 35.74394132968329
    - type: nauc_ndcg_at_1_max
      value: 4.0476454646619215
    - type: nauc_ndcg_at_1_std
      value: -21.16866068260486
    - type: nauc_ndcg_at_20_diff1
      value: 31.722628551526604
    - type: nauc_ndcg_at_20_max
      value: 6.085473579598258
    - type: nauc_ndcg_at_20_std
      value: -23.01301453978275
    - type: nauc_ndcg_at_3_diff1
      value: 32.38743175334077
    - type: nauc_ndcg_at_3_max
      value: 4.708074286110014
    - type: nauc_ndcg_at_3_std
      value: -24.005841131351065
    - type: nauc_ndcg_at_5_diff1
      value: 32.19107640366649
    - type: nauc_ndcg_at_5_max
      value: 5.248392125691872
    - type: nauc_ndcg_at_5_std
      value: -24.9544454485758
    - type: nauc_precision_at_1000_diff1
      value: -2.0283123762593203
    - type: nauc_precision_at_1000_max
      value: 14.569550330630554
    - type: nauc_precision_at_1000_std
      value: 18.01811212416059
    - type: nauc_precision_at_100_diff1
      value: 14.463485381374719
    - type: nauc_precision_at_100_max
      value: 16.06415646423591
    - type: nauc_precision_at_100_std
      value: 8.987627462107199
    - type: nauc_precision_at_10_diff1
      value: 25.530846925228666
    - type: nauc_precision_at_10_max
      value: 8.075830710803086
    - type: nauc_precision_at_10_std
      value: -24.00010341583341
    - type: nauc_precision_at_1_diff1
      value: 35.74394132968329
    - type: nauc_precision_at_1_max
      value: 4.0476454646619215
    - type: nauc_precision_at_1_std
      value: -21.16866068260486
    - type: nauc_precision_at_20_diff1
      value: 22.490315165998652
    - type: nauc_precision_at_20_max
      value: 9.695438542678712
    - type: nauc_precision_at_20_std
      value: -16.779150840743586
    - type: nauc_precision_at_3_diff1
      value: 29.653053865297718
    - type: nauc_precision_at_3_max
      value: 4.956580341717329
    - type: nauc_precision_at_3_std
      value: -25.716768027801912
    - type: nauc_precision_at_5_diff1
      value: 28.466584677280675
    - type: nauc_precision_at_5_max
      value: 6.035813186905091
    - type: nauc_precision_at_5_std
      value: -27.40096435134959
    - type: nauc_recall_at_1000_diff1
      value: 16.188777617075157
    - type: nauc_recall_at_1000_max
      value: 45.1160674872711
    - type: nauc_recall_at_1000_std
      value: 50.8993030763505
    - type: nauc_recall_at_100_diff1
      value: 26.462748511423666
    - type: nauc_recall_at_100_max
      value: 20.17057177381908
    - type: nauc_recall_at_100_std
      value: 6.567222385661084
    - type: nauc_recall_at_10_diff1
      value: 27.694042744869897
    - type: nauc_recall_at_10_max
      value: 8.193922397003126
    - type: nauc_recall_at_10_std
      value: -25.428481461107726
    - type: nauc_recall_at_1_diff1
      value: 35.879541770806426
    - type: nauc_recall_at_1_max
      value: 4.037000551161811
    - type: nauc_recall_at_1_std
      value: -21.066913542507095
    - type: nauc_recall_at_20_diff1
      value: 26.412542837917503
    - type: nauc_recall_at_20_max
      value: 10.119778040160208
    - type: nauc_recall_at_20_std
      value: -20.353583276762542
    - type: nauc_recall_at_3_diff1
      value: 30.1723792933633
    - type: nauc_recall_at_3_max
      value: 4.991021506511908
    - type: nauc_recall_at_3_std
      value: -25.61028187578253
    - type: nauc_recall_at_5_diff1
      value: 29.546460816157307
    - type: nauc_recall_at_5_max
      value: 6.257065735729789
    - type: nauc_recall_at_5_std
      value: -27.757268209659046
    - type: ndcg_at_1
      value: 22.708000000000002
    - type: ndcg_at_10
      value: 41.48
    - type: ndcg_at_100
      value: 46.894999999999996
    - type: ndcg_at_1000
      value: 48.14
    - type: ndcg_at_20
      value: 43.918
    - type: ndcg_at_3
      value: 33.423
    - type: ndcg_at_5
      value: 37.553
    - type: precision_at_1
      value: 22.708000000000002
    - type: precision_at_10
      value: 6.6049999999999995
    - type: precision_at_100
      value: 0.9329999999999999
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_20
      value: 3.811
    - type: precision_at_3
      value: 14.283999999999999
    - type: precision_at_5
      value: 10.685
    - type: recall_at_1
      value: 22.078999999999997
    - type: recall_at_10
      value: 63.269
    - type: recall_at_100
      value: 88.318
    - type: recall_at_1000
      value: 97.80799999999999
    - type: recall_at_20
      value: 72.741
    - type: recall_at_3
      value: 41.347
    - type: recall_at_5
      value: 51.271
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
      value: 96.0373917008664
    - type: f1
      value: 95.77672920037678
    - type: f1_weighted
      value: 96.06299804062722
    - type: main_score
      value: 96.0373917008664
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
      value: 89.1655266757866
    - type: f1
      value: 71.6595596649587
    - type: f1_weighted
      value: 90.44597470884298
    - type: main_score
      value: 89.1655266757866
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveIntentClassification (en)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 76.60390047074647
    - type: f1
      value: 74.0382414657559
    - type: f1_weighted
      value: 76.53055023019932
    - type: main_score
      value: 76.60390047074647
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveScenarioClassification (en)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 78.93073301950236
    - type: f1
      value: 78.58195068346751
    - type: f1_weighted
      value: 78.86975899493798
    - type: main_score
      value: 78.93073301950236
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MedrxivClusteringP2P (default)
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
      split: test
      type: mteb/medrxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 37.66500681777215
    - type: v_measure
      value: 37.66500681777215
    - type: v_measure_std
      value: 1.4953449515069268
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MedrxivClusteringS2S (default)
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
      split: test
      type: mteb/medrxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 35.51021437644991
    - type: v_measure
      value: 35.51021437644991
    - type: v_measure_std
      value: 1.3321174913629759
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MindSmallReranking (default)
      revision: 59042f120c80e8afa9cdbb224f67076cec0fc9a7
      split: test
      type: mteb/mind_small
    metrics:
    - type: main_score
      value: 30.10020452046386
    - type: map
      value: 30.10020452046386
    - type: mrr
      value: 31.096861019258043
    - type: nAUC_map_diff1
      value: 12.853085612418742
    - type: nAUC_map_max
      value: -20.97077158351351
    - type: nAUC_map_std
      value: -2.459841546804226
    - type: nAUC_mrr_diff1
      value: 12.08750595893558
    - type: nAUC_mrr_max
      value: -15.502813020230475
    - type: nAUC_mrr_std
      value: -0.8069966088331175
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB NFCorpus (default)
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
      split: test
      type: mteb/nfcorpus
    metrics:
    - type: main_score
      value: 34.725
    - type: map_at_1
      value: 5.901
    - type: map_at_10
      value: 12.992999999999999
    - type: map_at_100
      value: 16.402
    - type: map_at_1000
      value: 17.896
    - type: map_at_20
      value: 14.411
    - type: map_at_3
      value: 9.3
    - type: map_at_5
      value: 10.906
    - type: mrr_at_1
      value: 46.13003095975232
    - type: mrr_at_10
      value: 54.67123691581895
    - type: mrr_at_100
      value: 55.13154466663215
    - type: mrr_at_1000
      value: 55.18028030923489
    - type: mrr_at_20
      value: 54.89203403371564
    - type: mrr_at_3
      value: 52.47678018575851
    - type: mrr_at_5
      value: 54.10216718266254
    - type: nauc_map_at_1000_diff1
      value: 26.097980547292376
    - type: nauc_map_at_1000_max
      value: 31.716612190607847
    - type: nauc_map_at_1000_std
      value: 10.484226609845875
    - type: nauc_map_at_100_diff1
      value: 26.903184213500687
    - type: nauc_map_at_100_max
      value: 30.254077338590847
    - type: nauc_map_at_100_std
      value: 5.721213154053636
    - type: nauc_map_at_10_diff1
      value: 30.41995975934737
    - type: nauc_map_at_10_max
      value: 23.720851152044826
    - type: nauc_map_at_10_std
      value: -6.968119243629756
    - type: nauc_map_at_1_diff1
      value: 45.91087927776542
    - type: nauc_map_at_1_max
      value: 11.368756627277754
    - type: nauc_map_at_1_std
      value: -21.987291617576854
    - type: nauc_map_at_20_diff1
      value: 28.907069629931854
    - type: nauc_map_at_20_max
      value: 26.70846407056094
    - type: nauc_map_at_20_std
      value: -1.9126005785897775
    - type: nauc_map_at_3_diff1
      value: 38.73155355719495
    - type: nauc_map_at_3_max
      value: 17.769925571726496
    - type: nauc_map_at_3_std
      value: -15.240426410962574
    - type: nauc_map_at_5_diff1
      value: 34.6278617589197
    - type: nauc_map_at_5_max
      value: 20.54601986245645
    - type: nauc_map_at_5_std
      value: -11.566817873968779
    - type: nauc_mrr_at_1000_diff1
      value: 36.64991509982144
    - type: nauc_mrr_at_1000_max
      value: 49.697173212531744
    - type: nauc_mrr_at_1000_std
      value: 26.86511696261478
    - type: nauc_mrr_at_100_diff1
      value: 36.68743394598715
    - type: nauc_mrr_at_100_max
      value: 49.744202083676264
    - type: nauc_mrr_at_100_std
      value: 26.90232555840209
    - type: nauc_mrr_at_10_diff1
      value: 36.47029954847764
    - type: nauc_mrr_at_10_max
      value: 49.439023284006
    - type: nauc_mrr_at_10_std
      value: 26.690706480930444
    - type: nauc_mrr_at_1_diff1
      value: 36.59190142546215
    - type: nauc_mrr_at_1_max
      value: 41.74235868276634
    - type: nauc_mrr_at_1_std
      value: 18.414274177675807
    - type: nauc_mrr_at_20_diff1
      value: 36.681072119690086
    - type: nauc_mrr_at_20_max
      value: 49.800936007548934
    - type: nauc_mrr_at_20_std
      value: 26.961504252981683
    - type: nauc_mrr_at_3_diff1
      value: 36.63303178691115
    - type: nauc_mrr_at_3_max
      value: 48.628730526802904
    - type: nauc_mrr_at_3_std
      value: 25.157181938589225
    - type: nauc_mrr_at_5_diff1
      value: 36.41948638139246
    - type: nauc_mrr_at_5_max
      value: 49.180007480727134
    - type: nauc_mrr_at_5_std
      value: 26.145567865350543
    - type: nauc_ndcg_at_1000_diff1
      value: 26.257313381009283
    - type: nauc_ndcg_at_1000_max
      value: 46.45094846583072
    - type: nauc_ndcg_at_1000_std
      value: 30.74855470405661
    - type: nauc_ndcg_at_100_diff1
      value: 25.337713280261774
    - type: nauc_ndcg_at_100_max
      value: 42.51314175786316
    - type: nauc_ndcg_at_100_std
      value: 25.717600091835052
    - type: nauc_ndcg_at_10_diff1
      value: 27.28963504973803
    - type: nauc_ndcg_at_10_max
      value: 45.07020624629025
    - type: nauc_ndcg_at_10_std
      value: 29.017215904691902
    - type: nauc_ndcg_at_1_diff1
      value: 39.69547779212674
    - type: nauc_ndcg_at_1_max
      value: 39.944550572400225
    - type: nauc_ndcg_at_1_std
      value: 17.27308663512775
    - type: nauc_ndcg_at_20_diff1
      value: 26.88029364873597
    - type: nauc_ndcg_at_20_max
      value: 43.89319625918324
    - type: nauc_ndcg_at_20_std
      value: 29.182590252122804
    - type: nauc_ndcg_at_3_diff1
      value: 32.49288862835273
    - type: nauc_ndcg_at_3_max
      value: 45.57318753977976
    - type: nauc_ndcg_at_3_std
      value: 23.953534500127557
    - type: nauc_ndcg_at_5_diff1
      value: 29.578845399866545
    - type: nauc_ndcg_at_5_max
      value: 46.601862971633544
    - type: nauc_ndcg_at_5_std
      value: 27.55565792973463
    - type: nauc_precision_at_1000_diff1
      value: -4.397392180783799
    - type: nauc_precision_at_1000_max
      value: 17.406927055459345
    - type: nauc_precision_at_1000_std
      value: 47.8835834302276
    - type: nauc_precision_at_100_diff1
      value: -3.582470870457778
    - type: nauc_precision_at_100_max
      value: 30.6298826448415
    - type: nauc_precision_at_100_std
      value: 55.54858727751579
    - type: nauc_precision_at_10_diff1
      value: 6.591245947478634
    - type: nauc_precision_at_10_max
      value: 44.36069671353394
    - type: nauc_precision_at_10_std
      value: 45.85949796089425
    - type: nauc_precision_at_1_diff1
      value: 39.90620183792372
    - type: nauc_precision_at_1_max
      value: 41.93832955553217
    - type: nauc_precision_at_1_std
      value: 17.78208215842155
    - type: nauc_precision_at_20_diff1
      value: 3.1763559888676305
    - type: nauc_precision_at_20_max
      value: 40.19013491290661
    - type: nauc_precision_at_20_std
      value: 50.30896997510246
    - type: nauc_precision_at_3_diff1
      value: 21.346541990363338
    - type: nauc_precision_at_3_max
      value: 46.358486907663234
    - type: nauc_precision_at_3_std
      value: 30.30796100013066
    - type: nauc_precision_at_5_diff1
      value: 13.764960158282511
    - type: nauc_precision_at_5_max
      value: 47.38189520644064
    - type: nauc_precision_at_5_std
      value: 38.83370975791448
    - type: nauc_recall_at_1000_diff1
      value: 3.111013627981912
    - type: nauc_recall_at_1000_max
      value: 17.453303474327654
    - type: nauc_recall_at_1000_std
      value: 16.831446977812252
    - type: nauc_recall_at_100_diff1
      value: 16.59425078697382
    - type: nauc_recall_at_100_max
      value: 25.400896109980174
    - type: nauc_recall_at_100_std
      value: 10.794971059479254
    - type: nauc_recall_at_10_diff1
      value: 23.63271460212068
    - type: nauc_recall_at_10_max
      value: 20.991264958049598
    - type: nauc_recall_at_10_std
      value: -6.022250169253036
    - type: nauc_recall_at_1_diff1
      value: 45.91087927776542
    - type: nauc_recall_at_1_max
      value: 11.368756627277754
    - type: nauc_recall_at_1_std
      value: -21.987291617576854
    - type: nauc_recall_at_20_diff1
      value: 22.615984500854555
    - type: nauc_recall_at_20_max
      value: 23.637250829352997
    - type: nauc_recall_at_20_std
      value: 0.41128528477486354
    - type: nauc_recall_at_3_diff1
      value: 37.308271400820985
    - type: nauc_recall_at_3_max
      value: 18.63584930406467
    - type: nauc_recall_at_3_std
      value: -13.472251033244428
    - type: nauc_recall_at_5_diff1
      value: 31.142005435540852
    - type: nauc_recall_at_5_max
      value: 20.5834454794761
    - type: nauc_recall_at_5_std
      value: -9.81034234508067
    - type: ndcg_at_1
      value: 42.879
    - type: ndcg_at_10
      value: 34.725
    - type: ndcg_at_100
      value: 31.798
    - type: ndcg_at_1000
      value: 40.486
    - type: ndcg_at_20
      value: 32.535
    - type: ndcg_at_3
      value: 38.97
    - type: ndcg_at_5
      value: 37.602000000000004
    - type: precision_at_1
      value: 44.891999999999996
    - type: precision_at_10
      value: 26.192
    - type: precision_at_100
      value: 8.241
    - type: precision_at_1000
      value: 2.085
    - type: precision_at_20
      value: 19.52
    - type: precision_at_3
      value: 36.842000000000006
    - type: precision_at_5
      value: 33.312999999999995
    - type: recall_at_1
      value: 5.901
    - type: recall_at_10
      value: 17.171
    - type: recall_at_100
      value: 31.709
    - type: recall_at_1000
      value: 63.589
    - type: recall_at_20
      value: 20.782999999999998
    - type: recall_at_3
      value: 10.194
    - type: recall_at_5
      value: 12.934999999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NQ (default)
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
      split: test
      type: mteb/nq
    metrics:
    - type: main_score
      value: 59.951
    - type: map_at_1
      value: 36.718
    - type: map_at_10
      value: 52.518
    - type: map_at_100
      value: 53.373000000000005
    - type: map_at_1000
      value: 53.400000000000006
    - type: map_at_20
      value: 53.11
    - type: map_at_3
      value: 48.606
    - type: map_at_5
      value: 50.922999999999995
    - type: mrr_at_1
      value: 41.22247972190035
    - type: mrr_at_10
      value: 55.10211471610661
    - type: mrr_at_100
      value: 55.690424468447944
    - type: mrr_at_1000
      value: 55.709587669000626
    - type: mrr_at_20
      value: 55.51307514935747
    - type: mrr_at_3
      value: 52.10023174971031
    - type: mrr_at_5
      value: 53.85139049826188
    - type: nauc_map_at_1000_diff1
      value: 36.084432495766244
    - type: nauc_map_at_1000_max
      value: 32.106683448614696
    - type: nauc_map_at_1000_std
      value: 0.28114600458421135
    - type: nauc_map_at_100_diff1
      value: 36.076754155834685
    - type: nauc_map_at_100_max
      value: 32.124501222653386
    - type: nauc_map_at_100_std
      value: 0.3074172933687319
    - type: nauc_map_at_10_diff1
      value: 35.95846264899338
    - type: nauc_map_at_10_max
      value: 32.268962480678645
    - type: nauc_map_at_10_std
      value: -0.10550275250265802
    - type: nauc_map_at_1_diff1
      value: 39.29370524773578
    - type: nauc_map_at_1_max
      value: 25.991296131217062
    - type: nauc_map_at_1_std
      value: -2.5540466996583753
    - type: nauc_map_at_20_diff1
      value: 35.98377971994357
    - type: nauc_map_at_20_max
      value: 32.15683504409824
    - type: nauc_map_at_20_std
      value: 0.19145693127134786
    - type: nauc_map_at_3_diff1
      value: 36.0944254890347
    - type: nauc_map_at_3_max
      value: 30.2128510665515
    - type: nauc_map_at_3_std
      value: -1.9611081461308983
    - type: nauc_map_at_5_diff1
      value: 36.00156289591984
    - type: nauc_map_at_5_max
      value: 31.56149465902775
    - type: nauc_map_at_5_std
      value: -0.8373235686244762
    - type: nauc_mrr_at_1000_diff1
      value: 36.09152753153953
    - type: nauc_mrr_at_1000_max
      value: 32.43454228496553
    - type: nauc_mrr_at_1000_std
      value: 1.8517892571605596
    - type: nauc_mrr_at_100_diff1
      value: 36.09112009133751
    - type: nauc_mrr_at_100_max
      value: 32.44951869408173
    - type: nauc_mrr_at_100_std
      value: 1.8714844618486277
    - type: nauc_mrr_at_10_diff1
      value: 35.930421137614914
    - type: nauc_mrr_at_10_max
      value: 32.65451978743636
    - type: nauc_mrr_at_10_std
      value: 1.7723190829619009
    - type: nauc_mrr_at_1_diff1
      value: 39.396024242346954
    - type: nauc_mrr_at_1_max
      value: 28.132740347350953
    - type: nauc_mrr_at_1_std
      value: -0.5935576215439111
    - type: nauc_mrr_at_20_diff1
      value: 35.99903536497898
    - type: nauc_mrr_at_20_max
      value: 32.50256539352071
    - type: nauc_mrr_at_20_std
      value: 1.8829977887370852
    - type: nauc_mrr_at_3_diff1
      value: 35.91812477028109
    - type: nauc_mrr_at_3_max
      value: 31.595134192404796
    - type: nauc_mrr_at_3_std
      value: 0.6749658339604261
    - type: nauc_mrr_at_5_diff1
      value: 35.90541524153257
    - type: nauc_mrr_at_5_max
      value: 32.375076970871106
    - type: nauc_mrr_at_5_std
      value: 1.4530009988326982
    - type: nauc_ndcg_at_1000_diff1
      value: 35.52189976546703
    - type: nauc_ndcg_at_1000_max
      value: 33.97534043055662
    - type: nauc_ndcg_at_1000_std
      value: 2.7358127566748025
    - type: nauc_ndcg_at_100_diff1
      value: 35.32967760887528
    - type: nauc_ndcg_at_100_max
      value: 34.51536712950666
    - type: nauc_ndcg_at_100_std
      value: 3.561484184520643
    - type: nauc_ndcg_at_10_diff1
      value: 34.63981443982384
    - type: nauc_ndcg_at_10_max
      value: 35.2466755214177
    - type: nauc_ndcg_at_10_std
      value: 2.163469830591493
    - type: nauc_ndcg_at_1_diff1
      value: 39.47234805254548
    - type: nauc_ndcg_at_1_max
      value: 27.949377920983448
    - type: nauc_ndcg_at_1_std
      value: -0.7016496183295023
    - type: nauc_ndcg_at_20_diff1
      value: 34.77193782885647
    - type: nauc_ndcg_at_20_max
      value: 34.79563187118757
    - type: nauc_ndcg_at_20_std
      value: 3.0333339734937326
    - type: nauc_ndcg_at_3_diff1
      value: 34.84410905343334
    - type: nauc_ndcg_at_3_max
      value: 31.53857235413653
    - type: nauc_ndcg_at_3_std
      value: -1.2121011083371147
    - type: nauc_ndcg_at_5_diff1
      value: 34.70655373953545
    - type: nauc_ndcg_at_5_max
      value: 33.692790095442994
    - type: nauc_ndcg_at_5_std
      value: 0.6612260001056149
    - type: nauc_precision_at_1000_diff1
      value: -6.531497758654776
    - type: nauc_precision_at_1000_max
      value: 6.592383443768815
    - type: nauc_precision_at_1000_std
      value: 15.266065986503547
    - type: nauc_precision_at_100_diff1
      value: -2.0738709139302003
    - type: nauc_precision_at_100_max
      value: 15.324594432362842
    - type: nauc_precision_at_100_std
      value: 20.825895623533857
    - type: nauc_precision_at_10_diff1
      value: 9.98637582589397
    - type: nauc_precision_at_10_max
      value: 30.50457748285925
    - type: nauc_precision_at_10_std
      value: 13.73313229149034
    - type: nauc_precision_at_1_diff1
      value: 39.47234805254548
    - type: nauc_precision_at_1_max
      value: 27.949377920983448
    - type: nauc_precision_at_1_std
      value: -0.7016496183295023
    - type: nauc_precision_at_20_diff1
      value: 4.338247023429635
    - type: nauc_precision_at_20_max
      value: 23.76589815146598
    - type: nauc_precision_at_20_std
      value: 17.322633618978386
    - type: nauc_precision_at_3_diff1
      value: 23.17326950999716
    - type: nauc_precision_at_3_max
      value: 31.075717350827293
    - type: nauc_precision_at_3_std
      value: 2.762436540576557
    - type: nauc_precision_at_5_diff1
      value: 17.362008096246633
    - type: nauc_precision_at_5_max
      value: 32.08805696305664
    - type: nauc_precision_at_5_std
      value: 8.12524167169048
    - type: nauc_recall_at_1000_diff1
      value: 34.18415215294108
    - type: nauc_recall_at_1000_max
      value: 79.77930971993527
    - type: nauc_recall_at_1000_std
      value: 70.27189175741741
    - type: nauc_recall_at_100_diff1
      value: 28.249629521143465
    - type: nauc_recall_at_100_max
      value: 62.21529072406605
    - type: nauc_recall_at_100_std
      value: 46.23141649265807
    - type: nauc_recall_at_10_diff1
      value: 27.302420328273612
    - type: nauc_recall_at_10_max
      value: 47.57999826869166
    - type: nauc_recall_at_10_std
      value: 9.807109630878386
    - type: nauc_recall_at_1_diff1
      value: 39.29370524773578
    - type: nauc_recall_at_1_max
      value: 25.991296131217062
    - type: nauc_recall_at_1_std
      value: -2.5540466996583753
    - type: nauc_recall_at_20_diff1
      value: 26.264363964930997
    - type: nauc_recall_at_20_max
      value: 49.762297304442136
    - type: nauc_recall_at_20_std
      value: 18.650695925686502
    - type: nauc_recall_at_3_diff1
      value: 29.95231482486556
    - type: nauc_recall_at_3_max
      value: 33.054441143791394
    - type: nauc_recall_at_3_std
      value: -1.4133288694811754
    - type: nauc_recall_at_5_diff1
      value: 28.978660648633802
    - type: nauc_recall_at_5_max
      value: 38.844300548161186
    - type: nauc_recall_at_5_std
      value: 3.19644809086287
    - type: ndcg_at_1
      value: 41.193999999999996
    - type: ndcg_at_10
      value: 59.951
    - type: ndcg_at_100
      value: 63.343
    - type: ndcg_at_1000
      value: 63.941
    - type: ndcg_at_20
      value: 61.781
    - type: ndcg_at_3
      value: 52.756
    - type: ndcg_at_5
      value: 56.486999999999995
    - type: precision_at_1
      value: 41.193999999999996
    - type: precision_at_10
      value: 9.528
    - type: precision_at_100
      value: 1.145
    - type: precision_at_1000
      value: 0.12
    - type: precision_at_20
      value: 5.206
    - type: precision_at_3
      value: 23.696
    - type: precision_at_5
      value: 16.419
    - type: recall_at_1
      value: 36.718
    - type: recall_at_10
      value: 79.84
    - type: recall_at_100
      value: 94.228
    - type: recall_at_1000
      value: 98.648
    - type: recall_at_20
      value: 86.542
    - type: recall_at_3
      value: 61.31999999999999
    - type: recall_at_5
      value: 69.836
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB QuoraRetrieval (default)
      revision: e4e08e0b7dbe3c8700f0daef558ff32256715259
      split: test
      type: mteb/quora
    metrics:
    - type: main_score
      value: 89.838
    - type: map_at_1
      value: 72.44500000000001
    - type: map_at_10
      value: 86.332
    - type: map_at_100
      value: 86.936
    - type: map_at_1000
      value: 86.95
    - type: map_at_20
      value: 86.72999999999999
    - type: map_at_3
      value: 83.417
    - type: map_at_5
      value: 85.292
    - type: mrr_at_1
      value: 83.5
    - type: mrr_at_10
      value: 89.20519444444444
    - type: mrr_at_100
      value: 89.2819086258491
    - type: mrr_at_1000
      value: 89.28214505128291
    - type: mrr_at_20
      value: 89.26673258007042
    - type: mrr_at_3
      value: 88.36
    - type: mrr_at_5
      value: 88.95100000000001
    - type: nauc_map_at_1000_diff1
      value: 76.90740671940051
    - type: nauc_map_at_1000_max
      value: 36.46444946338708
    - type: nauc_map_at_1000_std
      value: -56.60380240532508
    - type: nauc_map_at_100_diff1
      value: 76.91112078761572
    - type: nauc_map_at_100_max
      value: 36.45304363618243
    - type: nauc_map_at_100_std
      value: -56.67988410741111
    - type: nauc_map_at_10_diff1
      value: 77.09598611046616
    - type: nauc_map_at_10_max
      value: 35.96689922341558
    - type: nauc_map_at_10_std
      value: -58.68604909203303
    - type: nauc_map_at_1_diff1
      value: 80.37641963929528
    - type: nauc_map_at_1_max
      value: 27.046973659136057
    - type: nauc_map_at_1_std
      value: -49.41187376826384
    - type: nauc_map_at_20_diff1
      value: 76.9541622063172
    - type: nauc_map_at_20_max
      value: 36.29817666157097
    - type: nauc_map_at_20_std
      value: -57.58995860118392
    - type: nauc_map_at_3_diff1
      value: 77.79036430390953
    - type: nauc_map_at_3_max
      value: 33.23673927645347
    - type: nauc_map_at_3_std
      value: -60.10156884287652
    - type: nauc_map_at_5_diff1
      value: 77.33636903512307
    - type: nauc_map_at_5_max
      value: 35.003919992106006
    - type: nauc_map_at_5_std
      value: -59.97787405958172
    - type: nauc_mrr_at_1000_diff1
      value: 77.73000572331905
    - type: nauc_mrr_at_1000_max
      value: 38.561364157585324
    - type: nauc_mrr_at_1000_std
      value: -53.44976098044828
    - type: nauc_mrr_at_100_diff1
      value: 77.72981689727108
    - type: nauc_mrr_at_100_max
      value: 38.561425387623785
    - type: nauc_mrr_at_100_std
      value: -53.45033750871979
    - type: nauc_mrr_at_10_diff1
      value: 77.71709626439586
    - type: nauc_mrr_at_10_max
      value: 38.624900686387214
    - type: nauc_mrr_at_10_std
      value: -53.58765986161691
    - type: nauc_mrr_at_1_diff1
      value: 78.37565253706408
    - type: nauc_mrr_at_1_max
      value: 38.23888076842768
    - type: nauc_mrr_at_1_std
      value: -50.20603764579538
    - type: nauc_mrr_at_20_diff1
      value: 77.7306939391157
    - type: nauc_mrr_at_20_max
      value: 38.59165749191751
    - type: nauc_mrr_at_20_std
      value: -53.48812024214872
    - type: nauc_mrr_at_3_diff1
      value: 77.54353349806524
    - type: nauc_mrr_at_3_max
      value: 38.713759549229785
    - type: nauc_mrr_at_3_std
      value: -53.94582165002703
    - type: nauc_mrr_at_5_diff1
      value: 77.70283049254654
    - type: nauc_mrr_at_5_max
      value: 38.716317005111215
    - type: nauc_mrr_at_5_std
      value: -53.92085356926888
    - type: nauc_ndcg_at_1000_diff1
      value: 76.89855290894926
    - type: nauc_ndcg_at_1000_max
      value: 37.772216233524325
    - type: nauc_ndcg_at_1000_std
      value: -54.86144177114646
    - type: nauc_ndcg_at_100_diff1
      value: 76.90257905740786
    - type: nauc_ndcg_at_100_max
      value: 37.739876618823274
    - type: nauc_ndcg_at_100_std
      value: -55.18253534518033
    - type: nauc_ndcg_at_10_diff1
      value: 76.82906119719216
    - type: nauc_ndcg_at_10_max
      value: 37.09739956129085
    - type: nauc_ndcg_at_10_std
      value: -58.49646829288816
    - type: nauc_ndcg_at_1_diff1
      value: 78.37565253706408
    - type: nauc_ndcg_at_1_max
      value: 38.335351847985045
    - type: nauc_ndcg_at_1_std
      value: -50.212302001610745
    - type: nauc_ndcg_at_20_diff1
      value: 76.86843611975287
    - type: nauc_ndcg_at_20_max
      value: 37.38859864360577
    - type: nauc_ndcg_at_20_std
      value: -57.243383699901386
    - type: nauc_ndcg_at_3_diff1
      value: 76.43700144403104
    - type: nauc_ndcg_at_3_max
      value: 35.849266604568456
    - type: nauc_ndcg_at_3_std
      value: -58.26941196366757
    - type: nauc_ndcg_at_5_diff1
      value: 76.65368894551763
    - type: nauc_ndcg_at_5_max
      value: 36.67820873138469
    - type: nauc_ndcg_at_5_std
      value: -59.167875261562884
    - type: nauc_precision_at_1000_diff1
      value: -44.61035236776975
    - type: nauc_precision_at_1000_max
      value: -6.9906519553038535
    - type: nauc_precision_at_1000_std
      value: 45.26673634956755
    - type: nauc_precision_at_100_diff1
      value: -44.471568524106466
    - type: nauc_precision_at_100_max
      value: -6.513827405878257
    - type: nauc_precision_at_100_std
      value: 43.61461800235919
    - type: nauc_precision_at_10_diff1
      value: -40.63269213674181
    - type: nauc_precision_at_10_max
      value: -2.176686756124717
    - type: nauc_precision_at_10_std
      value: 29.834023361852225
    - type: nauc_precision_at_1_diff1
      value: 78.37565253706408
    - type: nauc_precision_at_1_max
      value: 38.335351847985045
    - type: nauc_precision_at_1_std
      value: -50.212302001610745
    - type: nauc_precision_at_20_diff1
      value: -43.166138321174
    - type: nauc_precision_at_20_max
      value: -4.551647757465525
    - type: nauc_precision_at_20_std
      value: 36.236925649882664
    - type: nauc_precision_at_3_diff1
      value: -22.241887562444298
    - type: nauc_precision_at_3_max
      value: 6.147594412705473
    - type: nauc_precision_at_3_std
      value: 6.206594648276548
    - type: nauc_precision_at_5_diff1
      value: -33.948204035499955
    - type: nauc_precision_at_5_max
      value: 1.551952866668139
    - type: nauc_precision_at_5_std
      value: 19.086692514199573
    - type: nauc_recall_at_1000_diff1
      value: 56.00550359595701
    - type: nauc_recall_at_1000_max
      value: 0.25076313433895114
    - type: nauc_recall_at_1000_std
      value: -19.767447908090993
    - type: nauc_recall_at_100_diff1
      value: 71.09157100014333
    - type: nauc_recall_at_100_max
      value: 36.803937541332566
    - type: nauc_recall_at_100_std
      value: -68.4065523296009
    - type: nauc_recall_at_10_diff1
      value: 72.74150240606814
    - type: nauc_recall_at_10_max
      value: 34.20323841659202
    - type: nauc_recall_at_10_std
      value: -81.23057156799683
    - type: nauc_recall_at_1_diff1
      value: 80.37641963929528
    - type: nauc_recall_at_1_max
      value: 27.046973659136057
    - type: nauc_recall_at_1_std
      value: -49.41187376826384
    - type: nauc_recall_at_20_diff1
      value: 72.23679243300582
    - type: nauc_recall_at_20_max
      value: 35.472624896485584
    - type: nauc_recall_at_20_std
      value: -83.96453691324263
    - type: nauc_recall_at_3_diff1
      value: 74.4436126143353
    - type: nauc_recall_at_3_max
      value: 30.220293116530584
    - type: nauc_recall_at_3_std
      value: -68.23230306181532
    - type: nauc_recall_at_5_diff1
      value: 72.89682914794618
    - type: nauc_recall_at_5_max
      value: 32.220311115253786
    - type: nauc_recall_at_5_std
      value: -74.53623789048245
    - type: ndcg_at_1
      value: 83.5
    - type: ndcg_at_10
      value: 89.838
    - type: ndcg_at_100
      value: 90.879
    - type: ndcg_at_1000
      value: 90.955
    - type: ndcg_at_20
      value: 90.422
    - type: ndcg_at_3
      value: 87.21799999999999
    - type: ndcg_at_5
      value: 88.727
    - type: precision_at_1
      value: 83.5
    - type: precision_at_10
      value: 13.571
    - type: precision_at_100
      value: 1.5350000000000001
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_20
      value: 7.175
    - type: precision_at_3
      value: 38.12
    - type: precision_at_5
      value: 25.041999999999998
    - type: recall_at_1
      value: 72.44500000000001
    - type: recall_at_10
      value: 96.298
    - type: recall_at_100
      value: 99.696
    - type: recall_at_1000
      value: 99.98599999999999
    - type: recall_at_20
      value: 98.15700000000001
    - type: recall_at_3
      value: 88.633
    - type: recall_at_5
      value: 92.985
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB RedditClustering (default)
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
      split: test
      type: mteb/reddit-clustering
    metrics:
    - type: main_score
      value: 59.36225093784713
    - type: v_measure
      value: 59.36225093784713
    - type: v_measure_std
      value: 3.9911509588570393
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RedditClusteringP2P (default)
      revision: 385e3cb46b4cfa89021f56c4380204149d0efe33
      split: test
      type: mteb/reddit-clustering-p2p
    metrics:
    - type: main_score
      value: 64.46282036246124
    - type: v_measure
      value: 64.46282036246124
    - type: v_measure_std
      value: 12.49196304240264
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB SCIDOCS (default)
      revision: f8c2fcf00f625baaa80f62ec5bd9e1fff3b8ae88
      split: test
      type: mteb/scidocs
    metrics:
    - type: main_score
      value: 21.781
    - type: map_at_1
      value: 5.103
    - type: map_at_10
      value: 13.152
    - type: map_at_100
      value: 15.421000000000001
    - type: map_at_1000
      value: 15.738
    - type: map_at_20
      value: 14.313
    - type: map_at_3
      value: 9.277000000000001
    - type: map_at_5
      value: 11.079
    - type: mrr_at_1
      value: 25.2
    - type: mrr_at_10
      value: 36.30464285714286
    - type: mrr_at_100
      value: 37.37083205414486
    - type: mrr_at_1000
      value: 37.41889994963302
    - type: mrr_at_20
      value: 36.99006600941199
    - type: mrr_at_3
      value: 33.11666666666667
    - type: mrr_at_5
      value: 34.971666666666664
    - type: nauc_map_at_1000_diff1
      value: 13.3829110188465
    - type: nauc_map_at_1000_max
      value: 26.200548089249203
    - type: nauc_map_at_1000_std
      value: 15.782390299656376
    - type: nauc_map_at_100_diff1
      value: 13.434823562595197
    - type: nauc_map_at_100_max
      value: 26.19757227269967
    - type: nauc_map_at_100_std
      value: 15.666149403001597
    - type: nauc_map_at_10_diff1
      value: 13.136752265014085
    - type: nauc_map_at_10_max
      value: 24.37704176159032
    - type: nauc_map_at_10_std
      value: 11.875468320642725
    - type: nauc_map_at_1_diff1
      value: 23.91080785158353
    - type: nauc_map_at_1_max
      value: 21.714915496600813
    - type: nauc_map_at_1_std
      value: 4.523659534794796
    - type: nauc_map_at_20_diff1
      value: 13.08994175195148
    - type: nauc_map_at_20_max
      value: 25.564250916023035
    - type: nauc_map_at_20_std
      value: 13.758854620282229
    - type: nauc_map_at_3_diff1
      value: 15.629634284012711
    - type: nauc_map_at_3_max
      value: 20.94416328947656
    - type: nauc_map_at_3_std
      value: 5.443733090008665
    - type: nauc_map_at_5_diff1
      value: 13.717844004379067
    - type: nauc_map_at_5_max
      value: 21.93083811259854
    - type: nauc_map_at_5_std
      value: 7.496869394816883
    - type: nauc_mrr_at_1000_diff1
      value: 19.466105991639516
    - type: nauc_mrr_at_1000_max
      value: 23.857199036893714
    - type: nauc_mrr_at_1000_std
      value: 10.400833057932964
    - type: nauc_mrr_at_100_diff1
      value: 19.45377482442327
    - type: nauc_mrr_at_100_max
      value: 23.86931198998342
    - type: nauc_mrr_at_100_std
      value: 10.43160252915245
    - type: nauc_mrr_at_10_diff1
      value: 19.595100505906498
    - type: nauc_mrr_at_10_max
      value: 23.828564831729913
    - type: nauc_mrr_at_10_std
      value: 10.158332218550582
    - type: nauc_mrr_at_1_diff1
      value: 23.639623316387265
    - type: nauc_mrr_at_1_max
      value: 21.91276584516334
    - type: nauc_mrr_at_1_std
      value: 4.555063005377011
    - type: nauc_mrr_at_20_diff1
      value: 19.42312083502562
    - type: nauc_mrr_at_20_max
      value: 23.998031015425354
    - type: nauc_mrr_at_20_std
      value: 10.507801798326819
    - type: nauc_mrr_at_3_diff1
      value: 20.50499706447941
    - type: nauc_mrr_at_3_max
      value: 22.89975536944602
    - type: nauc_mrr_at_3_std
      value: 8.976243818880809
    - type: nauc_mrr_at_5_diff1
      value: 19.59735376368769
    - type: nauc_mrr_at_5_max
      value: 23.079995863526243
    - type: nauc_mrr_at_5_std
      value: 9.558077494050336
    - type: nauc_ndcg_at_1000_diff1
      value: 13.411221925319488
    - type: nauc_ndcg_at_1000_max
      value: 28.874659943874605
    - type: nauc_ndcg_at_1000_std
      value: 22.92179424488089
    - type: nauc_ndcg_at_100_diff1
      value: 14.177059117246053
    - type: nauc_ndcg_at_100_max
      value: 29.49863202457167
    - type: nauc_ndcg_at_100_std
      value: 23.415432542915244
    - type: nauc_ndcg_at_10_diff1
      value: 14.034714269886518
    - type: nauc_ndcg_at_10_max
      value: 26.529324449228014
    - type: nauc_ndcg_at_10_std
      value: 15.0835036529515
    - type: nauc_ndcg_at_1_diff1
      value: 23.639623316387265
    - type: nauc_ndcg_at_1_max
      value: 21.91276584516334
    - type: nauc_ndcg_at_1_std
      value: 4.555063005377011
    - type: nauc_ndcg_at_20_diff1
      value: 13.639153726908837
    - type: nauc_ndcg_at_20_max
      value: 28.34934989257701
    - type: nauc_ndcg_at_20_std
      value: 18.346102705103505
    - type: nauc_ndcg_at_3_diff1
      value: 16.310949228363334
    - type: nauc_ndcg_at_3_max
      value: 21.96244399696209
    - type: nauc_ndcg_at_3_std
      value: 7.79248819842006
    - type: nauc_ndcg_at_5_diff1
      value: 14.630417187709366
    - type: nauc_ndcg_at_5_max
      value: 23.28452419937793
    - type: nauc_ndcg_at_5_std
      value: 10.132485346479228
    - type: nauc_precision_at_1000_diff1
      value: 0.4617378903286949
    - type: nauc_precision_at_1000_max
      value: 23.084163863883607
    - type: nauc_precision_at_1000_std
      value: 34.74028918125758
    - type: nauc_precision_at_100_diff1
      value: 7.744924657665058
    - type: nauc_precision_at_100_max
      value: 28.822902541968237
    - type: nauc_precision_at_100_std
      value: 35.872958881610344
    - type: nauc_precision_at_10_diff1
      value: 9.242022361674694
    - type: nauc_precision_at_10_max
      value: 27.707443555826906
    - type: nauc_precision_at_10_std
      value: 20.465290637452664
    - type: nauc_precision_at_1_diff1
      value: 23.639623316387265
    - type: nauc_precision_at_1_max
      value: 21.91276584516334
    - type: nauc_precision_at_1_std
      value: 4.555063005377011
    - type: nauc_precision_at_20_diff1
      value: 7.901785657316664
    - type: nauc_precision_at_20_max
      value: 29.678603802205057
    - type: nauc_precision_at_20_std
      value: 25.65946048724345
    - type: nauc_precision_at_3_diff1
      value: 13.650585769886394
    - type: nauc_precision_at_3_max
      value: 22.03045956299473
    - type: nauc_precision_at_3_std
      value: 9.155456520493106
    - type: nauc_precision_at_5_diff1
      value: 10.200134466214287
    - type: nauc_precision_at_5_max
      value: 23.308672947117167
    - type: nauc_precision_at_5_std
      value: 12.695862040385645
    - type: nauc_recall_at_1000_diff1
      value: 1.7286393025447204
    - type: nauc_recall_at_1000_max
      value: 23.322719223507704
    - type: nauc_recall_at_1000_std
      value: 36.358257876511956
    - type: nauc_recall_at_100_diff1
      value: 8.230846619688952
    - type: nauc_recall_at_100_max
      value: 28.880569830494963
    - type: nauc_recall_at_100_std
      value: 36.29115706966346
    - type: nauc_recall_at_10_diff1
      value: 9.362248846760513
    - type: nauc_recall_at_10_max
      value: 27.475538879580885
    - type: nauc_recall_at_10_std
      value: 20.314461649538373
    - type: nauc_recall_at_1_diff1
      value: 23.91080785158353
    - type: nauc_recall_at_1_max
      value: 21.714915496600813
    - type: nauc_recall_at_1_std
      value: 4.523659534794796
    - type: nauc_recall_at_20_diff1
      value: 8.140101636033602
    - type: nauc_recall_at_20_max
      value: 29.59131501693498
    - type: nauc_recall_at_20_std
      value: 25.876120433055316
    - type: nauc_recall_at_3_diff1
      value: 13.725759049941843
    - type: nauc_recall_at_3_max
      value: 21.75055584058006
    - type: nauc_recall_at_3_std
      value: 8.965766944507815
    - type: nauc_recall_at_5_diff1
      value: 10.366069494614596
    - type: nauc_recall_at_5_max
      value: 23.031784865881054
    - type: nauc_recall_at_5_std
      value: 12.411188897743521
    - type: ndcg_at_1
      value: 25.2
    - type: ndcg_at_10
      value: 21.781
    - type: ndcg_at_100
      value: 30.273
    - type: ndcg_at_1000
      value: 35.768
    - type: ndcg_at_20
      value: 24.967
    - type: ndcg_at_3
      value: 20.580000000000002
    - type: ndcg_at_5
      value: 17.926000000000002
    - type: precision_at_1
      value: 25.2
    - type: precision_at_10
      value: 11.4
    - type: precision_at_100
      value: 2.359
    - type: precision_at_1000
      value: 0.368
    - type: precision_at_20
      value: 7.545
    - type: precision_at_3
      value: 19.3
    - type: precision_at_5
      value: 15.78
    - type: recall_at_1
      value: 5.103
    - type: recall_at_10
      value: 23.083000000000002
    - type: recall_at_100
      value: 47.882999999999996
    - type: recall_at_1000
      value: 74.783
    - type: recall_at_20
      value: 30.592000000000002
    - type: recall_at_3
      value: 11.753
    - type: recall_at_5
      value: 15.983
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SICK-R (default)
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
      split: test
      type: mteb/sickr-sts
    metrics:
    - type: cosine_pearson
      value: 83.9841377195369
    - type: cosine_spearman
      value: 77.44919890597407
    - type: euclidean_pearson
      value: 81.21238548422511
    - type: euclidean_spearman
      value: 76.94405730272983
    - type: main_score
      value: 77.44919890597407
    - type: manhattan_pearson
      value: 81.16824677968528
    - type: manhattan_spearman
      value: 76.94296468591867
    - type: pearson
      value: 83.9841377195369
    - type: spearman
      value: 77.44919890597407
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS12 (default)
      revision: a0d554a64d88156834ff5ae9920b964011b16384
      split: test
      type: mteb/sts12-sts
    metrics:
    - type: cosine_pearson
      value: 81.36071984442052
    - type: cosine_spearman
      value: 74.2212823495219
    - type: euclidean_pearson
      value: 78.31139429452078
    - type: euclidean_spearman
      value: 74.02790834412275
    - type: main_score
      value: 74.2212823495219
    - type: manhattan_pearson
      value: 78.26141328104697
    - type: manhattan_spearman
      value: 74.02545007676329
    - type: pearson
      value: 81.36071984442052
    - type: spearman
      value: 74.2212823495219
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS13 (default)
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
      split: test
      type: mteb/sts13-sts
    metrics:
    - type: cosine_pearson
      value: 85.49925337918731
    - type: cosine_spearman
      value: 86.12368715292688
    - type: euclidean_pearson
      value: 85.71147581542367
    - type: euclidean_spearman
      value: 86.64112317821541
    - type: main_score
      value: 86.12368715292688
    - type: manhattan_pearson
      value: 85.58242941611371
    - type: manhattan_spearman
      value: 86.51041533466731
    - type: pearson
      value: 85.49925337918731
    - type: spearman
      value: 86.12368715292688
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS14 (default)
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
      split: test
      type: mteb/sts14-sts
    metrics:
    - type: cosine_pearson
      value: 82.24735192639226
    - type: cosine_spearman
      value: 78.88155361224834
    - type: euclidean_pearson
      value: 80.52048132030517
    - type: euclidean_spearman
      value: 78.1335955670817
    - type: main_score
      value: 78.88155361224834
    - type: manhattan_pearson
      value: 80.48178866605353
    - type: manhattan_spearman
      value: 78.08994918255844
    - type: pearson
      value: 82.24735192639226
    - type: spearman
      value: 78.88155361224834
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS15 (default)
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
      split: test
      type: mteb/sts15-sts
    metrics:
    - type: cosine_pearson
      value: 86.27381322229758
    - type: cosine_spearman
      value: 87.5038962579188
    - type: euclidean_pearson
      value: 86.7575259976948
    - type: euclidean_spearman
      value: 87.3358778981031
    - type: main_score
      value: 87.5038962579188
    - type: manhattan_pearson
      value: 86.72177109814491
    - type: manhattan_spearman
      value: 87.30593609243358
    - type: pearson
      value: 86.27381322229758
    - type: spearman
      value: 87.5038962579188
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS16 (default)
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
      split: test
      type: mteb/sts16-sts
    metrics:
    - type: cosine_pearson
      value: 82.90364706517789
    - type: cosine_spearman
      value: 84.25854334490232
    - type: euclidean_pearson
      value: 83.30065780824273
    - type: euclidean_spearman
      value: 84.17467271748362
    - type: main_score
      value: 84.25854334490232
    - type: manhattan_pearson
      value: 83.21239264085494
    - type: manhattan_spearman
      value: 84.05456832118482
    - type: pearson
      value: 82.90364706517789
    - type: spearman
      value: 84.25854334490232
    task:
      type: STS
  - dataset:
      config: en-en
      name: MTEB STS17 (en-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 88.88258729094343
    - type: cosine_spearman
      value: 89.68436656381257
    - type: euclidean_pearson
      value: 88.23417725579127
    - type: euclidean_spearman
      value: 87.96688277361433
    - type: main_score
      value: 89.68436656381257
    - type: manhattan_pearson
      value: 88.07673471897155
    - type: manhattan_spearman
      value: 87.7976329721765
    - type: pearson
      value: 88.88258729094343
    - type: spearman
      value: 89.68436656381257
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STS22 (en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 65.24627744968292
    - type: cosine_spearman
      value: 65.96283849168346
    - type: euclidean_pearson
      value: 66.2111925054528
    - type: euclidean_spearman
      value: 65.83563143944401
    - type: main_score
      value: 65.96283849168346
    - type: manhattan_pearson
      value: 66.25664281582083
    - type: manhattan_spearman
      value: 65.8830797513158
    - type: pearson
      value: 65.24627744968292
    - type: spearman
      value: 65.96283849168346
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSBenchmark (default)
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
      split: test
      type: mteb/stsbenchmark-sts
    metrics:
    - type: cosine_pearson
      value: 85.57515090752183
    - type: cosine_spearman
      value: 85.54441587714372
    - type: euclidean_pearson
      value: 85.53938106211463
    - type: euclidean_spearman
      value: 85.28473579067878
    - type: main_score
      value: 85.54441587714372
    - type: manhattan_pearson
      value: 85.51025100057596
    - type: manhattan_spearman
      value: 85.260887707662
    - type: pearson
      value: 85.57515090752183
    - type: spearman
      value: 85.54441587714372
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SciDocsRR (default)
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
      split: test
      type: mteb/scidocs-reranking
    metrics:
    - type: main_score
      value: 82.9058801876062
    - type: map
      value: 82.9058801876062
    - type: mrr
      value: 95.256220721907
    - type: nAUC_map_diff1
      value: 0.13078953297011875
    - type: nAUC_map_max
      value: 59.173980738758026
    - type: nAUC_map_std
      value: 73.35735418975649
    - type: nAUC_mrr_diff1
      value: 46.534353907114514
    - type: nAUC_mrr_max
      value: 89.56255914950661
    - type: nAUC_mrr_std
      value: 85.6716185155955
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SciFact (default)
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
      split: test
      type: mteb/scifact
    metrics:
    - type: main_score
      value: 71.844
    - type: map_at_1
      value: 57.278
    - type: map_at_10
      value: 67.109
    - type: map_at_100
      value: 67.66499999999999
    - type: map_at_1000
      value: 67.685
    - type: map_at_20
      value: 67.482
    - type: map_at_3
      value: 64.16199999999999
    - type: map_at_5
      value: 65.82900000000001
    - type: mrr_at_1
      value: 60.0
    - type: mrr_at_10
      value: 68.19960317460317
    - type: mrr_at_100
      value: 68.62748949394921
    - type: mrr_at_1000
      value: 68.64515905414915
    - type: mrr_at_20
      value: 68.472601010101
    - type: mrr_at_3
      value: 66.0
    - type: mrr_at_5
      value: 67.21666666666667
    - type: nauc_map_at_1000_diff1
      value: 70.04313292027558
    - type: nauc_map_at_1000_max
      value: 57.24529193476731
    - type: nauc_map_at_1000_std
      value: -4.8888921470785585
    - type: nauc_map_at_100_diff1
      value: 70.04624674117014
    - type: nauc_map_at_100_max
      value: 57.25302539508853
    - type: nauc_map_at_100_std
      value: -4.907703072069842
    - type: nauc_map_at_10_diff1
      value: 70.06943109940849
    - type: nauc_map_at_10_max
      value: 57.39452715929109
    - type: nauc_map_at_10_std
      value: -4.743417671263566
    - type: nauc_map_at_1_diff1
      value: 76.61111479875207
    - type: nauc_map_at_1_max
      value: 52.822124992902374
    - type: nauc_map_at_1_std
      value: -7.6071857283495445
    - type: nauc_map_at_20_diff1
      value: 69.95251393140202
    - type: nauc_map_at_20_max
      value: 57.328356768833146
    - type: nauc_map_at_20_std
      value: -4.871357691032887
    - type: nauc_map_at_3_diff1
      value: 69.71499509001714
    - type: nauc_map_at_3_max
      value: 53.645107897260026
    - type: nauc_map_at_3_std
      value: -7.908850295935557
    - type: nauc_map_at_5_diff1
      value: 69.7531280646943
    - type: nauc_map_at_5_max
      value: 55.71038914997073
    - type: nauc_map_at_5_std
      value: -6.7813041970848476
    - type: nauc_mrr_at_1000_diff1
      value: 69.61840192382927
    - type: nauc_mrr_at_1000_max
      value: 58.419734360225696
    - type: nauc_mrr_at_1000_std
      value: -1.8503761885586425
    - type: nauc_mrr_at_100_diff1
      value: 69.6153571701724
    - type: nauc_mrr_at_100_max
      value: 58.422378816414565
    - type: nauc_mrr_at_100_std
      value: -1.8731915889302972
    - type: nauc_mrr_at_10_diff1
      value: 69.5874772943516
    - type: nauc_mrr_at_10_max
      value: 58.78121978366665
    - type: nauc_mrr_at_10_std
      value: -1.2843146465927913
    - type: nauc_mrr_at_1_diff1
      value: 74.35688136934793
    - type: nauc_mrr_at_1_max
      value: 57.487384980706416
    - type: nauc_mrr_at_1_std
      value: -1.3005837538340144
    - type: nauc_mrr_at_20_diff1
      value: 69.53988639045606
    - type: nauc_mrr_at_20_max
      value: 58.49631860342686
    - type: nauc_mrr_at_20_std
      value: -1.7220227513588833
    - type: nauc_mrr_at_3_diff1
      value: 68.94320178615871
    - type: nauc_mrr_at_3_max
      value: 56.60856449749424
    - type: nauc_mrr_at_3_std
      value: -3.3432894595086866
    - type: nauc_mrr_at_5_diff1
      value: 68.94240340867633
    - type: nauc_mrr_at_5_max
      value: 58.27068018852665
    - type: nauc_mrr_at_5_std
      value: -2.320192066949136
    - type: nauc_ndcg_at_1000_diff1
      value: 69.15093538086137
    - type: nauc_ndcg_at_1000_max
      value: 58.6801221127507
    - type: nauc_ndcg_at_1000_std
      value: -3.002038837722594
    - type: nauc_ndcg_at_100_diff1
      value: 69.11507044508373
    - type: nauc_ndcg_at_100_max
      value: 58.843490113137605
    - type: nauc_ndcg_at_100_std
      value: -3.2810475322338566
    - type: nauc_ndcg_at_10_diff1
      value: 68.71920945656667
    - type: nauc_ndcg_at_10_max
      value: 60.13600198034469
    - type: nauc_ndcg_at_10_std
      value: -1.6190106644777749
    - type: nauc_ndcg_at_1_diff1
      value: 74.35688136934793
    - type: nauc_ndcg_at_1_max
      value: 57.487384980706416
    - type: nauc_ndcg_at_1_std
      value: -1.3005837538340144
    - type: nauc_ndcg_at_20_diff1
      value: 68.33714726670162
    - type: nauc_ndcg_at_20_max
      value: 59.45907982196103
    - type: nauc_ndcg_at_20_std
      value: -2.5953063304797754
    - type: nauc_ndcg_at_3_diff1
      value: 67.33605891922716
    - type: nauc_ndcg_at_3_max
      value: 55.01142849375101
    - type: nauc_ndcg_at_3_std
      value: -6.5632981093508205
    - type: nauc_ndcg_at_5_diff1
      value: 67.59450950578172
    - type: nauc_ndcg_at_5_max
      value: 57.50106057747294
    - type: nauc_ndcg_at_5_std
      value: -5.415038422866616
    - type: nauc_precision_at_1000_diff1
      value: -33.21156082089814
    - type: nauc_precision_at_1000_max
      value: 19.132732038554398
    - type: nauc_precision_at_1000_std
      value: 44.091281225705714
    - type: nauc_precision_at_100_diff1
      value: -20.015823755259245
    - type: nauc_precision_at_100_max
      value: 26.507243354636085
    - type: nauc_precision_at_100_std
      value: 37.87274756817076
    - type: nauc_precision_at_10_diff1
      value: 8.35057694800983
    - type: nauc_precision_at_10_max
      value: 49.60611953844157
    - type: nauc_precision_at_10_std
      value: 32.18410475820039
    - type: nauc_precision_at_1_diff1
      value: 74.35688136934793
    - type: nauc_precision_at_1_max
      value: 57.487384980706416
    - type: nauc_precision_at_1_std
      value: -1.3005837538340144
    - type: nauc_precision_at_20_diff1
      value: -3.0872665961524612
    - type: nauc_precision_at_20_max
      value: 40.5565038905005
    - type: nauc_precision_at_20_std
      value: 32.15291813716766
    - type: nauc_precision_at_3_diff1
      value: 34.627722605371545
    - type: nauc_precision_at_3_max
      value: 49.65219072739979
    - type: nauc_precision_at_3_std
      value: 7.7588985130719434
    - type: nauc_precision_at_5_diff1
      value: 22.06911561993657
    - type: nauc_precision_at_5_max
      value: 49.09578970278826
    - type: nauc_precision_at_5_std
      value: 16.038789872070705
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_100_diff1
      value: 64.77257569694551
    - type: nauc_recall_at_100_max
      value: 65.07269574496497
    - type: nauc_recall_at_100_std
      value: -10.979947534569218
    - type: nauc_recall_at_10_diff1
      value: 62.14297161941494
    - type: nauc_recall_at_10_max
      value: 70.41353364022896
    - type: nauc_recall_at_10_std
      value: 9.172932719542075
    - type: nauc_recall_at_1_diff1
      value: 76.61111479875207
    - type: nauc_recall_at_1_max
      value: 52.822124992902374
    - type: nauc_recall_at_1_std
      value: -7.6071857283495445
    - type: nauc_recall_at_20_diff1
      value: 57.631464811333224
    - type: nauc_recall_at_20_max
      value: 67.83558221740536
    - type: nauc_recall_at_20_std
      value: 3.110691973832695
    - type: nauc_recall_at_3_diff1
      value: 60.39078444139112
    - type: nauc_recall_at_3_max
      value: 51.122425596651574
    - type: nauc_recall_at_3_std
      value: -10.307895490015559
    - type: nauc_recall_at_5_diff1
      value: 59.703727953513145
    - type: nauc_recall_at_5_max
      value: 59.81893786534298
    - type: nauc_recall_at_5_std
      value: -6.231017907901268
    - type: ndcg_at_1
      value: 60.0
    - type: ndcg_at_10
      value: 71.844
    - type: ndcg_at_100
      value: 74.278
    - type: ndcg_at_1000
      value: 74.74199999999999
    - type: ndcg_at_20
      value: 72.99
    - type: ndcg_at_3
      value: 66.721
    - type: ndcg_at_5
      value: 69.137
    - type: precision_at_1
      value: 60.0
    - type: precision_at_10
      value: 9.6
    - type: precision_at_100
      value: 1.093
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_20
      value: 5.067
    - type: precision_at_3
      value: 26.111
    - type: precision_at_5
      value: 17.267
    - type: recall_at_1
      value: 57.278
    - type: recall_at_10
      value: 85.344
    - type: recall_at_100
      value: 96.5
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 89.589
    - type: recall_at_3
      value: 71.45
    - type: recall_at_5
      value: 77.361
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SprintDuplicateQuestions (default)
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
      split: test
      type: mteb/sprintduplicatequestions-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 99.8019801980198
    - type: cosine_accuracy_threshold
      value: 74.77510571479797
    - type: cosine_ap
      value: 95.30006120252773
    - type: cosine_f1
      value: 89.75265017667844
    - type: cosine_f1_threshold
      value: 72.93492555618286
    - type: cosine_precision
      value: 90.62181447502549
    - type: cosine_recall
      value: 88.9
    - type: dot_accuracy
      value: 99.74554455445545
    - type: dot_accuracy_threshold
      value: 794.2790985107422
    - type: dot_ap
      value: 93.33073289508414
    - type: dot_f1
      value: 87.11779448621553
    - type: dot_f1_threshold
      value: 793.5191631317139
    - type: dot_precision
      value: 87.33668341708542
    - type: dot_recall
      value: 86.9
    - type: euclidean_accuracy
      value: 99.7960396039604
    - type: euclidean_accuracy_threshold
      value: 238.72876167297363
    - type: euclidean_ap
      value: 95.04815354196363
    - type: euclidean_f1
      value: 89.53252032520325
    - type: euclidean_f1_threshold
      value: 241.42813682556152
    - type: euclidean_precision
      value: 91.01239669421489
    - type: euclidean_recall
      value: 88.1
    - type: main_score
      value: 95.30006120252773
    - type: manhattan_accuracy
      value: 99.7960396039604
    - type: manhattan_accuracy_threshold
      value: 5224.44953918457
    - type: manhattan_ap
      value: 95.02798265540767
    - type: manhattan_f1
      value: 89.4552723638181
    - type: manhattan_f1_threshold
      value: 5434.450531005859
    - type: manhattan_precision
      value: 89.41058941058941
    - type: manhattan_recall
      value: 89.5
    - type: max_accuracy
      value: 99.8019801980198
    - type: max_ap
      value: 95.30006120252773
    - type: max_f1
      value: 89.75265017667844
    - type: max_precision
      value: 91.01239669421489
    - type: max_recall
      value: 89.5
    - type: similarity_accuracy
      value: 99.8019801980198
    - type: similarity_accuracy_threshold
      value: 74.77510571479797
    - type: similarity_ap
      value: 95.30006120252773
    - type: similarity_f1
      value: 89.75265017667844
    - type: similarity_f1_threshold
      value: 72.93492555618286
    - type: similarity_precision
      value: 90.62181447502549
    - type: similarity_recall
      value: 88.9
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB StackExchangeClustering (default)
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
      split: test
      type: mteb/stackexchange-clustering
    metrics:
    - type: main_score
      value: 66.76593843797666
    - type: v_measure
      value: 66.76593843797666
    - type: v_measure_std
      value: 3.5421488096435416
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackExchangeClusteringP2P (default)
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
      split: test
      type: mteb/stackexchange-clustering-p2p
    metrics:
    - type: main_score
      value: 38.90007255920144
    - type: v_measure
      value: 38.90007255920144
    - type: v_measure_std
      value: 1.440894289494648
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackOverflowDupQuestions (default)
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
      split: test
      type: mteb/stackoverflowdupquestions-reranking
    metrics:
    - type: main_score
      value: 52.71807785910519
    - type: map
      value: 52.71807785910519
    - type: mrr
      value: 53.51011427298192
    - type: nAUC_map_diff1
      value: 38.489341755206404
    - type: nAUC_map_max
      value: 12.810459097227756
    - type: nAUC_map_std
      value: 10.001723368468545
    - type: nAUC_mrr_diff1
      value: 38.1795784067288
    - type: nAUC_mrr_max
      value: 13.876071274342735
    - type: nAUC_mrr_std
      value: 10.809361649584433
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SummEval (default)
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
      split: test
      type: mteb/summeval
    metrics:
    - type: cosine_pearson
      value: 31.51422308323083
    - type: cosine_spearman
      value: 31.22821719703179
    - type: dot_pearson
      value: 30.692806438778554
    - type: dot_spearman
      value: 30.440095026481913
    - type: main_score
      value: 31.22821719703179
    - type: pearson
      value: 31.51422308323083
    - type: spearman
      value: 31.22821719703179
    task:
      type: Summarization
  - dataset:
      config: default
      name: MTEB TRECCOVID (default)
      revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
      split: test
      type: mteb/trec-covid
    metrics:
    - type: main_score
      value: 79.38199999999999
    - type: map_at_1
      value: 0.258
    - type: map_at_10
      value: 2.077
    - type: map_at_100
      value: 12.062000000000001
    - type: map_at_1000
      value: 28.717
    - type: map_at_20
      value: 3.6630000000000003
    - type: map_at_3
      value: 0.7040000000000001
    - type: map_at_5
      value: 1.114
    - type: mrr_at_1
      value: 96.0
    - type: mrr_at_10
      value: 97.66666666666667
    - type: mrr_at_100
      value: 97.66666666666667
    - type: mrr_at_1000
      value: 97.66666666666667
    - type: mrr_at_20
      value: 97.66666666666667
    - type: mrr_at_3
      value: 97.66666666666667
    - type: mrr_at_5
      value: 97.66666666666667
    - type: nauc_map_at_1000_diff1
      value: -19.606457542469276
    - type: nauc_map_at_1000_max
      value: 62.23126542837836
    - type: nauc_map_at_1000_std
      value: 78.11491433681955
    - type: nauc_map_at_100_diff1
      value: 1.056950862100428
    - type: nauc_map_at_100_max
      value: 43.14707718269215
    - type: nauc_map_at_100_std
      value: 54.99119932336741
    - type: nauc_map_at_10_diff1
      value: 31.26313513848752
    - type: nauc_map_at_10_max
      value: 18.729050164831303
    - type: nauc_map_at_10_std
      value: 12.501346100150942
    - type: nauc_map_at_1_diff1
      value: 50.67428371303766
    - type: nauc_map_at_1_max
      value: 8.26350705716926
    - type: nauc_map_at_1_std
      value: -2.802747360156509
    - type: nauc_map_at_20_diff1
      value: 23.85177292094862
    - type: nauc_map_at_20_max
      value: 24.907498374862385
    - type: nauc_map_at_20_std
      value: 23.15361092830954
    - type: nauc_map_at_3_diff1
      value: 44.34113488392741
    - type: nauc_map_at_3_max
      value: 16.13816628219856
    - type: nauc_map_at_3_std
      value: 1.64493293742063
    - type: nauc_map_at_5_diff1
      value: 43.35667417997146
    - type: nauc_map_at_5_max
      value: 16.651525778549175
    - type: nauc_map_at_5_std
      value: 5.344297729807275
    - type: nauc_mrr_at_1000_diff1
      value: 65.01934106976137
    - type: nauc_mrr_at_1000_max
      value: 74.5231425903695
    - type: nauc_mrr_at_1000_std
      value: 84.12698412698381
    - type: nauc_mrr_at_100_diff1
      value: 65.01934106976137
    - type: nauc_mrr_at_100_max
      value: 74.5231425903695
    - type: nauc_mrr_at_100_std
      value: 84.12698412698381
    - type: nauc_mrr_at_10_diff1
      value: 65.01934106976137
    - type: nauc_mrr_at_10_max
      value: 74.5231425903695
    - type: nauc_mrr_at_10_std
      value: 84.12698412698381
    - type: nauc_mrr_at_1_diff1
      value: 63.81886087768457
    - type: nauc_mrr_at_1_max
      value: 77.70774976657333
    - type: nauc_mrr_at_1_std
      value: 86.11111111111124
    - type: nauc_mrr_at_20_diff1
      value: 65.01934106976137
    - type: nauc_mrr_at_20_max
      value: 74.5231425903695
    - type: nauc_mrr_at_20_std
      value: 84.12698412698381
    - type: nauc_mrr_at_3_diff1
      value: 65.01934106976137
    - type: nauc_mrr_at_3_max
      value: 74.5231425903695
    - type: nauc_mrr_at_3_std
      value: 84.12698412698381
    - type: nauc_mrr_at_5_diff1
      value: 65.01934106976137
    - type: nauc_mrr_at_5_max
      value: 74.5231425903695
    - type: nauc_mrr_at_5_std
      value: 84.12698412698381
    - type: nauc_ndcg_at_1000_diff1
      value: -12.207934630430895
    - type: nauc_ndcg_at_1000_max
      value: 63.27131989733247
    - type: nauc_ndcg_at_1000_std
      value: 77.77862783776057
    - type: nauc_ndcg_at_100_diff1
      value: -31.139043418906777
    - type: nauc_ndcg_at_100_max
      value: 56.29288690229761
    - type: nauc_ndcg_at_100_std
      value: 80.54207709212822
    - type: nauc_ndcg_at_10_diff1
      value: -21.623075757241335
    - type: nauc_ndcg_at_10_max
      value: 42.00930185115019
    - type: nauc_ndcg_at_10_std
      value: 63.90085820733794
    - type: nauc_ndcg_at_1_diff1
      value: 27.03957293721711
    - type: nauc_ndcg_at_1_max
      value: 18.687865072917816
    - type: nauc_ndcg_at_1_std
      value: 40.65606746354093
    - type: nauc_ndcg_at_20_diff1
      value: -27.059567337111528
    - type: nauc_ndcg_at_20_max
      value: 44.873490488692845
    - type: nauc_ndcg_at_20_std
      value: 68.27056244238835
    - type: nauc_ndcg_at_3_diff1
      value: -2.2768439107759253
    - type: nauc_ndcg_at_3_max
      value: 33.16972612805963
    - type: nauc_ndcg_at_3_std
      value: 49.35785810423734
    - type: nauc_ndcg_at_5_diff1
      value: -8.380892599544165
    - type: nauc_ndcg_at_5_max
      value: 39.7045491756542
    - type: nauc_ndcg_at_5_std
      value: 56.662696632820044
    - type: nauc_precision_at_1000_diff1
      value: -39.853246552685256
    - type: nauc_precision_at_1000_max
      value: 45.82687391914263
    - type: nauc_precision_at_1000_std
      value: 51.6573155072073
    - type: nauc_precision_at_100_diff1
      value: -35.334152199143055
    - type: nauc_precision_at_100_max
      value: 57.74163988146608
    - type: nauc_precision_at_100_std
      value: 78.83424294782806
    - type: nauc_precision_at_10_diff1
      value: -29.572269138136193
    - type: nauc_precision_at_10_max
      value: 45.16249504588279
    - type: nauc_precision_at_10_std
      value: 63.92716685466912
    - type: nauc_precision_at_1_diff1
      value: 63.81886087768457
    - type: nauc_precision_at_1_max
      value: 77.70774976657333
    - type: nauc_precision_at_1_std
      value: 86.11111111111124
    - type: nauc_precision_at_20_diff1
      value: -31.155129521710613
    - type: nauc_precision_at_20_max
      value: 46.072522169609606
    - type: nauc_precision_at_20_std
      value: 64.29857883516294
    - type: nauc_precision_at_3_diff1
      value: -5.644268209909603
    - type: nauc_precision_at_3_max
      value: 54.62437037830888
    - type: nauc_precision_at_3_std
      value: 52.27021040974535
    - type: nauc_precision_at_5_diff1
      value: -15.560278135078049
    - type: nauc_precision_at_5_max
      value: 50.21344816658272
    - type: nauc_precision_at_5_std
      value: 58.94711332326674
    - type: nauc_recall_at_1000_diff1
      value: -8.016557237167058
    - type: nauc_recall_at_1000_max
      value: 58.857938362714165
    - type: nauc_recall_at_1000_std
      value: 66.83850522737738
    - type: nauc_recall_at_100_diff1
      value: 15.447588986377317
    - type: nauc_recall_at_100_max
      value: 37.515788055189084
    - type: nauc_recall_at_100_std
      value: 42.326000614078026
    - type: nauc_recall_at_10_diff1
      value: 34.99067421432679
    - type: nauc_recall_at_10_max
      value: 13.792789030946933
    - type: nauc_recall_at_10_std
      value: 7.066206327262477
    - type: nauc_recall_at_1_diff1
      value: 50.67428371303766
    - type: nauc_recall_at_1_max
      value: 8.26350705716926
    - type: nauc_recall_at_1_std
      value: -2.802747360156509
    - type: nauc_recall_at_20_diff1
      value: 31.277397618992136
    - type: nauc_recall_at_20_max
      value: 20.296127261717054
    - type: nauc_recall_at_20_std
      value: 16.117931287068437
    - type: nauc_recall_at_3_diff1
      value: 46.303571802817025
    - type: nauc_recall_at_3_max
      value: 14.03073426897129
    - type: nauc_recall_at_3_std
      value: -0.39592906337357797
    - type: nauc_recall_at_5_diff1
      value: 45.51206018811467
    - type: nauc_recall_at_5_max
      value: 12.263182926616867
    - type: nauc_recall_at_5_std
      value: 1.5451403387758214
    - type: ndcg_at_1
      value: 87.0
    - type: ndcg_at_10
      value: 79.38199999999999
    - type: ndcg_at_100
      value: 59.941
    - type: ndcg_at_1000
      value: 53.581999999999994
    - type: ndcg_at_20
      value: 74.244
    - type: ndcg_at_3
      value: 84.05
    - type: ndcg_at_5
      value: 82.328
    - type: precision_at_1
      value: 96.0
    - type: precision_at_10
      value: 85.2
    - type: precision_at_100
      value: 61.519999999999996
    - type: precision_at_1000
      value: 23.328
    - type: precision_at_20
      value: 78.4
    - type: precision_at_3
      value: 90.667
    - type: precision_at_5
      value: 88.4
    - type: recall_at_1
      value: 0.258
    - type: recall_at_10
      value: 2.225
    - type: recall_at_100
      value: 15.190999999999999
    - type: recall_at_1000
      value: 50.656
    - type: recall_at_20
      value: 4.063
    - type: recall_at_3
      value: 0.722
    - type: recall_at_5
      value: 1.168
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Touche2020 (default)
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
      split: test
      type: mteb/touche2020
    metrics:
    - type: main_score
      value: 24.254
    - type: map_at_1
      value: 2.355
    - type: map_at_10
      value: 9.554
    - type: map_at_100
      value: 14.856
    - type: map_at_1000
      value: 16.320999999999998
    - type: map_at_20
      value: 11.594
    - type: map_at_3
      value: 5.624
    - type: map_at_5
      value: 6.948
    - type: mrr_at_1
      value: 28.57142857142857
    - type: mrr_at_10
      value: 45.30855199222546
    - type: mrr_at_100
      value: 46.29196367191565
    - type: mrr_at_1000
      value: 46.31499833524485
    - type: mrr_at_20
      value: 46.113797167218536
    - type: mrr_at_3
      value: 42.17687074829932
    - type: mrr_at_5
      value: 43.70748299319728
    - type: nauc_map_at_1000_diff1
      value: 16.20923402096991
    - type: nauc_map_at_1000_max
      value: -1.0790035381754648
    - type: nauc_map_at_1000_std
      value: 7.195462252108266
    - type: nauc_map_at_100_diff1
      value: 18.389136986949936
    - type: nauc_map_at_100_max
      value: -2.05569038009456
    - type: nauc_map_at_100_std
      value: 2.571693024788773
    - type: nauc_map_at_10_diff1
      value: 21.066136452964642
    - type: nauc_map_at_10_max
      value: 1.5731034935019352
    - type: nauc_map_at_10_std
      value: -10.470562156435545
    - type: nauc_map_at_1_diff1
      value: 18.809274247757674
    - type: nauc_map_at_1_max
      value: -8.68104031396317
    - type: nauc_map_at_1_std
      value: -30.619138463973307
    - type: nauc_map_at_20_diff1
      value: 23.36148432932364
    - type: nauc_map_at_20_max
      value: -0.38560029617230923
    - type: nauc_map_at_20_std
      value: -6.8825311118744485
    - type: nauc_map_at_3_diff1
      value: 18.9370153117886
    - type: nauc_map_at_3_max
      value: 2.2032967783435375
    - type: nauc_map_at_3_std
      value: -12.532694022066659
    - type: nauc_map_at_5_diff1
      value: 21.434904521858602
    - type: nauc_map_at_5_max
      value: 6.094611630406942
    - type: nauc_map_at_5_std
      value: -12.492795788667474
    - type: nauc_mrr_at_1000_diff1
      value: 11.961046636239269
    - type: nauc_mrr_at_1000_max
      value: -15.748297693665677
    - type: nauc_mrr_at_1000_std
      value: -12.067130971523385
    - type: nauc_mrr_at_100_diff1
      value: 11.95534277650038
    - type: nauc_mrr_at_100_max
      value: -15.684486171307041
    - type: nauc_mrr_at_100_std
      value: -11.98247014226321
    - type: nauc_mrr_at_10_diff1
      value: 12.191520381511925
    - type: nauc_mrr_at_10_max
      value: -16.510285123987302
    - type: nauc_mrr_at_10_std
      value: -11.93784570526233
    - type: nauc_mrr_at_1_diff1
      value: 18.162553375605516
    - type: nauc_mrr_at_1_max
      value: -18.920009881475387
    - type: nauc_mrr_at_1_std
      value: -31.201005281857086
    - type: nauc_mrr_at_20_diff1
      value: 11.85035482221006
    - type: nauc_mrr_at_20_max
      value: -16.18704935368085
    - type: nauc_mrr_at_20_std
      value: -11.424991900511088
    - type: nauc_mrr_at_3_diff1
      value: 14.733201594965836
    - type: nauc_mrr_at_3_max
      value: -11.75899459749356
    - type: nauc_mrr_at_3_std
      value: -11.499870896820976
    - type: nauc_mrr_at_5_diff1
      value: 12.874017458219845
    - type: nauc_mrr_at_5_max
      value: -13.642689819875791
    - type: nauc_mrr_at_5_std
      value: -11.64117086557618
    - type: nauc_ndcg_at_1000_diff1
      value: -6.849400123979281
    - type: nauc_ndcg_at_1000_max
      value: -3.8209628417621393
    - type: nauc_ndcg_at_1000_std
      value: 31.393629472927504
    - type: nauc_ndcg_at_100_diff1
      value: 5.4656320972286485
    - type: nauc_ndcg_at_100_max
      value: -11.571250999652408
    - type: nauc_ndcg_at_100_std
      value: 16.5511179303082
    - type: nauc_ndcg_at_10_diff1
      value: 9.553502614400788
    - type: nauc_ndcg_at_10_max
      value: -14.08266102380929
    - type: nauc_ndcg_at_10_std
      value: -5.404201943794988
    - type: nauc_ndcg_at_1_diff1
      value: 11.37824691229176
    - type: nauc_ndcg_at_1_max
      value: -21.31215334708879
    - type: nauc_ndcg_at_1_std
      value: -29.749958184219334
    - type: nauc_ndcg_at_20_diff1
      value: 13.396975021395857
    - type: nauc_ndcg_at_20_max
      value: -14.5189405742469
    - type: nauc_ndcg_at_20_std
      value: -1.6276921520570502
    - type: nauc_ndcg_at_3_diff1
      value: 2.3132968948746226
    - type: nauc_ndcg_at_3_max
      value: -11.351646560904848
    - type: nauc_ndcg_at_3_std
      value: -0.15036952995361091
    - type: nauc_ndcg_at_5_diff1
      value: 6.214320727021392
    - type: nauc_ndcg_at_5_max
      value: -9.797994041679638
    - type: nauc_ndcg_at_5_std
      value: -3.3742904276844223
    - type: nauc_precision_at_1000_diff1
      value: -32.78708155144845
    - type: nauc_precision_at_1000_max
      value: 34.81622247650308
    - type: nauc_precision_at_1000_std
      value: 47.996245254718744
    - type: nauc_precision_at_100_diff1
      value: -10.867559709952797
    - type: nauc_precision_at_100_max
      value: 6.681915188055671
    - type: nauc_precision_at_100_std
      value: 61.989390090979356
    - type: nauc_precision_at_10_diff1
      value: 6.511211593484189
    - type: nauc_precision_at_10_max
      value: -16.842566662697454
    - type: nauc_precision_at_10_std
      value: 5.002600740433903
    - type: nauc_precision_at_1_diff1
      value: 18.162553375605516
    - type: nauc_precision_at_1_max
      value: -18.920009881475387
    - type: nauc_precision_at_1_std
      value: -31.201005281857086
    - type: nauc_precision_at_20_diff1
      value: 9.640744611970522
    - type: nauc_precision_at_20_max
      value: -18.27653996056668
    - type: nauc_precision_at_20_std
      value: 22.021814503656543
    - type: nauc_precision_at_3_diff1
      value: 6.916201107284145
    - type: nauc_precision_at_3_max
      value: -0.039381527098944095
    - type: nauc_precision_at_3_std
      value: 9.096821181866671
    - type: nauc_precision_at_5_diff1
      value: 9.032683328748616
    - type: nauc_precision_at_5_max
      value: -3.5989814795848223
    - type: nauc_precision_at_5_std
      value: 2.506947866544208
    - type: nauc_recall_at_1000_diff1
      value: -27.92405572104993
    - type: nauc_recall_at_1000_max
      value: 14.256848434706395
    - type: nauc_recall_at_1000_std
      value: 69.3546817240148
    - type: nauc_recall_at_100_diff1
      value: 6.613753533249129
    - type: nauc_recall_at_100_max
      value: -8.405822616363144
    - type: nauc_recall_at_100_std
      value: 29.430588706591397
    - type: nauc_recall_at_10_diff1
      value: 18.481730784371077
    - type: nauc_recall_at_10_max
      value: -7.763172381505888
    - type: nauc_recall_at_10_std
      value: -7.48570052741164
    - type: nauc_recall_at_1_diff1
      value: 18.809274247757674
    - type: nauc_recall_at_1_max
      value: -8.68104031396317
    - type: nauc_recall_at_1_std
      value: -30.619138463973307
    - type: nauc_recall_at_20_diff1
      value: 20.639977762281493
    - type: nauc_recall_at_20_max
      value: -11.301201172125623
    - type: nauc_recall_at_20_std
      value: 0.38755705583239786
    - type: nauc_recall_at_3_diff1
      value: 18.279383297820562
    - type: nauc_recall_at_3_max
      value: 5.287795698059438
    - type: nauc_recall_at_3_std
      value: -3.7312167565958316
    - type: nauc_recall_at_5_diff1
      value: 21.115852302465356
    - type: nauc_recall_at_5_max
      value: 5.318139212101227
    - type: nauc_recall_at_5_std
      value: -7.792885381250281
    - type: ndcg_at_1
      value: 25.509999999999998
    - type: ndcg_at_10
      value: 24.254
    - type: ndcg_at_100
      value: 34.660000000000004
    - type: ndcg_at_1000
      value: 45.798
    - type: ndcg_at_20
      value: 24.988
    - type: ndcg_at_3
      value: 29.273
    - type: ndcg_at_5
      value: 25.453
    - type: precision_at_1
      value: 28.571
    - type: precision_at_10
      value: 21.02
    - type: precision_at_100
      value: 7.122000000000001
    - type: precision_at_1000
      value: 1.435
    - type: precision_at_20
      value: 16.326999999999998
    - type: precision_at_3
      value: 31.293
    - type: precision_at_5
      value: 24.898
    - type: recall_at_1
      value: 2.355
    - type: recall_at_10
      value: 15.397
    - type: recall_at_100
      value: 43.647000000000006
    - type: recall_at_1000
      value: 77.089
    - type: recall_at_20
      value: 22.792
    - type: recall_at_3
      value: 6.847
    - type: recall_at_5
      value: 9.136
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ToxicConversationsClassification (default)
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
      split: test
      type: mteb/toxic_conversations_50k
    metrics:
    - type: accuracy
      value: 72.7734375
    - type: ap
      value: 15.655230461083708
    - type: ap_weighted
      value: 15.655230461083708
    - type: f1
      value: 56.31497978454638
    - type: f1_weighted
      value: 78.70509613747345
    - type: main_score
      value: 72.7734375
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TweetSentimentExtractionClassification (default)
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
      split: test
      type: mteb/tweet_sentiment_extraction
    metrics:
    - type: accuracy
      value: 72.56366723259762
    - type: f1
      value: 72.90413275122202
    - type: f1_weighted
      value: 72.19948169084057
    - type: main_score
      value: 72.56366723259762
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TwentyNewsgroupsClustering (default)
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
      split: test
      type: mteb/twentynewsgroups-clustering
    metrics:
    - type: main_score
      value: 56.90970017457857
    - type: v_measure
      value: 56.90970017457857
    - type: v_measure_std
      value: 1.5885885070403738
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB TwitterSemEval2015 (default)
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
      split: test
      type: mteb/twittersemeval2015-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 85.7006616200751
    - type: cosine_accuracy_threshold
      value: 75.78572630882263
    - type: cosine_ap
      value: 72.87577990245127
    - type: cosine_f1
      value: 67.36422521175885
    - type: cosine_f1_threshold
      value: 70.15678882598877
    - type: cosine_precision
      value: 63.80368098159509
    - type: cosine_recall
      value: 71.34564643799473
    - type: dot_accuracy
      value: 83.60851165285807
    - type: dot_accuracy_threshold
      value: 744.7918891906738
    - type: dot_ap
      value: 64.82619159813649
    - type: dot_f1
      value: 62.62379263968699
    - type: dot_f1_threshold
      value: 696.7735290527344
    - type: dot_precision
      value: 58.350421508316245
    - type: dot_recall
      value: 67.57255936675462
    - type: euclidean_accuracy
      value: 85.84371460928652
    - type: euclidean_accuracy_threshold
      value: 220.4747200012207
    - type: euclidean_ap
      value: 72.47837433257799
    - type: euclidean_f1
      value: 67.2811059907834
    - type: euclidean_f1_threshold
      value: 240.81902503967285
    - type: euclidean_precision
      value: 65.34062655395326
    - type: euclidean_recall
      value: 69.34036939313984
    - type: main_score
      value: 72.87577990245127
    - type: manhattan_accuracy
      value: 85.83179352685224
    - type: manhattan_accuracy_threshold
      value: 4910.404205322266
    - type: manhattan_ap
      value: 72.44111617709422
    - type: manhattan_f1
      value: 67.09989806320081
    - type: manhattan_f1_threshold
      value: 5333.793640136719
    - type: manhattan_precision
      value: 64.88417939871857
    - type: manhattan_recall
      value: 69.47229551451187
    - type: max_accuracy
      value: 85.84371460928652
    - type: max_ap
      value: 72.87577990245127
    - type: max_f1
      value: 67.36422521175885
    - type: max_precision
      value: 65.34062655395326
    - type: max_recall
      value: 71.34564643799473
    - type: similarity_accuracy
      value: 85.7006616200751
    - type: similarity_accuracy_threshold
      value: 75.78572630882263
    - type: similarity_ap
      value: 72.87577990245127
    - type: similarity_f1
      value: 67.36422521175885
    - type: similarity_f1_threshold
      value: 70.15678882598877
    - type: similarity_precision
      value: 63.80368098159509
    - type: similarity_recall
      value: 71.34564643799473
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB TwitterURLCorpus (default)
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
      split: test
      type: mteb/twitterurlcorpus-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 88.88112702293631
    - type: cosine_accuracy_threshold
      value: 71.48405313491821
    - type: cosine_ap
      value: 85.88088882163336
    - type: cosine_f1
      value: 78.2251744598276
    - type: cosine_f1_threshold
      value: 70.09605169296265
    - type: cosine_precision
      value: 75.8997755087262
    - type: cosine_recall
      value: 80.69756698490914
    - type: dot_accuracy
      value: 88.04672643303451
    - type: dot_accuracy_threshold
      value: 700.6264686584473
    - type: dot_ap
      value: 83.52072844458456
    - type: dot_f1
      value: 76.24239256244634
    - type: dot_f1_threshold
      value: 664.9115562438965
    - type: dot_precision
      value: 74.0123233055455
    - type: dot_recall
      value: 78.61102556205728
    - type: euclidean_accuracy
      value: 88.72588970388482
    - type: euclidean_accuracy_threshold
      value: 226.53303146362305
    - type: euclidean_ap
      value: 85.51788295919707
    - type: euclidean_f1
      value: 77.73453426739316
    - type: euclidean_f1_threshold
      value: 238.7503147125244
    - type: euclidean_precision
      value: 74.94818097348296
    - type: euclidean_recall
      value: 80.73606405913151
    - type: main_score
      value: 85.88088882163336
    - type: manhattan_accuracy
      value: 88.68902084061008
    - type: manhattan_accuracy_threshold
      value: 5034.079742431641
    - type: manhattan_ap
      value: 85.49952903626239
    - type: manhattan_f1
      value: 77.74326743888625
    - type: manhattan_f1_threshold
      value: 5334.531021118164
    - type: manhattan_precision
      value: 73.98289171708741
    - type: manhattan_recall
      value: 81.90637511549123
    - type: max_accuracy
      value: 88.88112702293631
    - type: max_ap
      value: 85.88088882163336
    - type: max_f1
      value: 78.2251744598276
    - type: max_precision
      value: 75.8997755087262
    - type: max_recall
      value: 81.90637511549123
    - type: similarity_accuracy
      value: 88.88112702293631
    - type: similarity_accuracy_threshold
      value: 71.48405313491821
    - type: similarity_ap
      value: 85.88088882163336
    - type: similarity_f1
      value: 78.2251744598276
    - type: similarity_f1_threshold
      value: 70.09605169296265
    - type: similarity_precision
      value: 75.8997755087262
    - type: similarity_recall
      value: 80.69756698490914
    task:
      type: PairClassification
---
# Contextual Document Embeddings (CDE)

Our new model that naturally integrates "context tokens" into the embedding process. As of October 1st, 2024, `cde-small-v1` is the best small model (under 400M params) on the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) for text embedding models, with an average score of 65.00.

👉  <b><a href="https://colab.research.google.com/drive/1r8xwbp7_ySL9lP-ve4XMJAHjidB9UkbL?usp=sharing">Try on Colab</a></b>
<br>
👉  <b><a href="https://arxiv.org/abs/2410.02525">Contextual Document Embeddings (ArXiv)</a></b>

![CDE Overview Figure](https://i.imgur.com/LyXJZjM.png)

<br>
<hr>

# How to use `cde-small-v1`

Our embedding model needs to be used in *two stages*. The first stage is to gather some dataset information by embedding a subset of the corpus using our "first-stage" model. The second stage is to actually embed queries and documents, conditioning on the corpus information from the first stage. Note that we can do the first stage part offline and only use the second-stage weights at inference time.

## With Sentence Transformers

<details open="">
<summary>Click to learn how to use cde-small-v1 with Sentence Transformers</summary>

### Loading the model

Our model can be loaded using `sentence-transformers` out-of-the-box with "trust remote code" enabled:
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("jxm/cde-small-v1", trust_remote_code=True)
```

#### Note on prefixes

*Nota bene*: Like all state-of-the-art embedding models, our model was trained with task-specific prefixes. To do retrieval, you can use `prompt_name="query"` and `prompt_name="document"` in the `encode` method of the model when embedding queries and documents, respectively.

### First stage

```python
minicorpus_size = model[0].config.transductive_corpus_size
minicorpus_docs = [ ... ] # Put some strings here that are representative of your corpus, for example by calling random.sample(corpus, k=minicorpus_size)
assert len(minicorpus_docs) == minicorpus_size # You must use exactly this many documents in the minicorpus. You can oversample if your corpus is smaller.

dataset_embeddings = model.encode(
    minicorpus_docs,
    prompt_name="document",
    convert_to_tensor=True
)
```

### Running the second stage

Now that we have obtained "dataset embeddings" we can embed documents and queries like normal. Remember to use the document prompt for documents:

```python
docs = [...]
queries = [...]

doc_embeddings = model.encode(
    docs,
    prompt_name="document",
    dataset_embeddings=dataset_embeddings,
    convert_to_tensor=True,
)
query_embeddings = model.encode(
    queries,
    prompt_name="query",
    dataset_embeddings=dataset_embeddings,
    convert_to_tensor=True,
) 
```

these embeddings can be compared using cosine similarity via `model.similarity`:
```python
similarities = model.similarity(query_embeddings, doc_embeddings)
topk_values, topk_indices = similarities.topk(5)
```

<details>
<summary>Click here for a full copy-paste ready example</summary>

```python
from sentence_transformers import SentenceTransformer
from datasets import load_dataset

# 1. Load the Sentence Transformer model
model = SentenceTransformer("jxm/cde-small-v1", trust_remote_code=True)
context_docs_size = model[0].config.transductive_corpus_size  # 512

# 2. Load the dataset: context dataset, docs, and queries
dataset = load_dataset("sentence-transformers/natural-questions", split="train")
dataset.shuffle(seed=42)
# 10 queries, 512 context docs, 500 docs
queries = dataset["query"][:10]
docs = dataset["answer"][:2000]
context_docs = dataset["answer"][-context_docs_size:] # Last 512 docs

# 3. First stage: embed the context docs
dataset_embeddings = model.encode(
    context_docs,
    prompt_name="document",
    convert_to_tensor=True,
)

# 4. Second stage: embed the docs and queries
doc_embeddings = model.encode(
    docs,
    prompt_name="document",
    dataset_embeddings=dataset_embeddings,
    convert_to_tensor=True,
)
query_embeddings = model.encode(
    queries,
    prompt_name="query",
    dataset_embeddings=dataset_embeddings,
    convert_to_tensor=True,
)

# 5. Compute the similarity between the queries and docs
similarities = model.similarity(query_embeddings, doc_embeddings)
topk_values, topk_indices = similarities.topk(5)
print(topk_values)
print(topk_indices)

"""
tensor([[0.5495, 0.5426, 0.5423, 0.5292, 0.5286],
        [0.6357, 0.6334, 0.6177, 0.5862, 0.5794],
        [0.7648, 0.5452, 0.5000, 0.4959, 0.4881],
        [0.6802, 0.5225, 0.5178, 0.5160, 0.5075],
        [0.6947, 0.5843, 0.5619, 0.5344, 0.5298],
        [0.7742, 0.7742, 0.7742, 0.7231, 0.6224],
        [0.8853, 0.6667, 0.5829, 0.5795, 0.5769],
        [0.6911, 0.6127, 0.6003, 0.5986, 0.5936],
        [0.6796, 0.6053, 0.6000, 0.5911, 0.5884],
        [0.7624, 0.5589, 0.5428, 0.5278, 0.5275]], device='cuda:0')
tensor([[   0,  296,  234, 1651, 1184],
        [1542,  466,  438, 1207, 1911],
        [   2, 1562,  632, 1852,  382],
        [   3,  694,  932, 1765,  662],
        [   4,   35,  747,   26,  432],
        [ 534,  175,    5, 1495,  575],
        [   6, 1802, 1875,  747,   21],
        [   7, 1913, 1936,  640,    6],
        [   8,  747,  167, 1318, 1743],
        [   9, 1583, 1145,  219,  357]], device='cuda:0')
"""
# As you can see, almost every query_i has document_i as the most similar document.

# 6. Print the top-k results
for query_idx, top_doc_idx in enumerate(topk_indices[:, 0]):
    print(f"Query {query_idx}: {queries[query_idx]}")
    print(f"Top Document: {docs[top_doc_idx]}")
    print()
"""
Query 0: when did richmond last play in a preliminary final
Top Document: Richmond Football Club Richmond began 2017 with 5 straight wins, a feat it had not achieved since 1995. A series of close losses hampered the Tigers throughout the middle of the season, including a 5-point loss to the Western Bulldogs, 2-point loss to Fremantle, and a 3-point loss to the Giants. Richmond ended the season strongly with convincing victories over Fremantle and St Kilda in the final two rounds, elevating the club to 3rd on the ladder. Richmond's first final of the season against the Cats at the MCG attracted a record qualifying final crowd of 95,028; the Tigers won by 51 points. Having advanced to the first preliminary finals for the first time since 2001, Richmond defeated Greater Western Sydney by 36 points in front of a crowd of 94,258 to progress to the Grand Final against Adelaide, their first Grand Final appearance since 1982. The attendance was 100,021, the largest crowd to a grand final since 1986. The Crows led at quarter time and led by as many as 13, but the Tigers took over the game as it progressed and scored seven straight goals at one point. They eventually would win by 48 points – 16.12 (108) to Adelaide's 8.12 (60) – to end their 37-year flag drought.[22] Dustin Martin also became the first player to win a Premiership medal, the Brownlow Medal and the Norm Smith Medal in the same season, while Damien Hardwick was named AFL Coaches Association Coach of the Year. Richmond's jump from 13th to premiers also marked the biggest jump from one AFL season to the next.

Query 1: who sang what in the world's come over you
Top Document: Life's What You Make It (Talk Talk song) "Life's What You Make It" is a song by the English band Talk Talk. It was released as a single in 1986, the first from the band's album The Colour of Spring. The single was a hit in the UK, peaking at No. 16, and charted in numerous other countries, often reaching the Top 20.

Query 2: who produces the most wool in the world
Top Document: Wool Global wool production is about 2 million tonnes per year, of which 60% goes into apparel. Wool comprises ca 3% of the global textile market, but its value is higher owing to dying and other modifications of the material.[1] Australia is a leading producer of wool which is mostly from Merino sheep but has been eclipsed by China in terms of total weight.[30] New Zealand (2016) is the third-largest producer of wool, and the largest producer of crossbred wool. Breeds such as Lincoln, Romney, Drysdale, and Elliotdale produce coarser fibers, and wool from these sheep is usually used for making carpets.

Query 3: where does alaska the last frontier take place
Top Document: Alaska: The Last Frontier Alaska: The Last Frontier is an American reality cable television series on the Discovery Channel, currently in its 7th season of broadcast. The show documents the extended Kilcher family, descendants of Swiss immigrants and Alaskan pioneers, Yule and Ruth Kilcher, at their homestead 11 miles outside of Homer.[1] By living without plumbing or modern heating, the clan chooses to subsist by farming, hunting and preparing for the long winters.[2] The Kilcher family are relatives of the singer Jewel,[1][3] who has appeared on the show.[4]

Query 4: a day to remember all i want cameos
Top Document: All I Want (A Day to Remember song) The music video for the song, which was filmed in October 2010,[4] was released on January 6, 2011.[5] It features cameos of numerous popular bands and musicians. The cameos are: Tom Denney (A Day to Remember's former guitarist), Pete Wentz, Winston McCall of Parkway Drive, The Devil Wears Prada, Bring Me the Horizon, Sam Carter of Architects, Tim Lambesis of As I Lay Dying, Silverstein, Andrew WK, August Burns Red, Seventh Star, Matt Heafy of Trivium, Vic Fuentes of Pierce the Veil, Mike Herrera of MxPx, and Set Your Goals.[5] Rock Sound called the video "quite excellent".[5]

Query 5: what does the red stripes mean on the american flag
Top Document: Flag of the United States The flag of the United States of America, often referred to as the American flag, is the national flag of the United States. It consists of thirteen equal horizontal stripes of red (top and bottom) alternating with white, with a blue rectangle in the canton (referred to specifically as the "union") bearing fifty small, white, five-pointed stars arranged in nine offset horizontal rows, where rows of six stars (top and bottom) alternate with rows of five stars. The 50 stars on the flag represent the 50 states of the United States of America, and the 13 stripes represent the thirteen British colonies that declared independence from the Kingdom of Great Britain, and became the first states in the U.S.[1] Nicknames for the flag include The Stars and Stripes,[2] Old Glory,[3] and The Star-Spangled Banner.

Query 6: where did they film diary of a wimpy kid
Top Document: Diary of a Wimpy Kid (film) Filming of Diary of a Wimpy Kid was in Vancouver and wrapped up on October 16, 2009.

Query 7: where was beasts of the southern wild filmed
Top Document: Beasts of the Southern Wild The film's fictional setting, "Isle de Charles Doucet", known to its residents as the Bathtub, was inspired by several isolated and independent fishing communities threatened by erosion, hurricanes and rising sea levels in Louisiana's Terrebonne Parish, most notably the rapidly eroding Isle de Jean Charles. It was filmed in Terrebonne Parish town Montegut.[5]

Query 8: what part of the country are you likely to find the majority of the mollisols
Top Document: Mollisol Mollisols occur in savannahs and mountain valleys (such as Central Asia, or the North American Great Plains). These environments have historically been strongly influenced by fire and abundant pedoturbation from organisms such as ants and earthworms. It was estimated that in 2003, only 14 to 26 percent of grassland ecosystems still remained in a relatively natural state (that is, they were not used for agriculture due to the fertility of the A horizon). Globally, they represent ~7% of ice-free land area. As the world's most agriculturally productive soil order, the Mollisols represent one of the more economically important soil orders.

Query 9: when did fosters home for imaginary friends start
Top Document: Foster's Home for Imaginary Friends McCracken conceived the series after adopting two dogs from an animal shelter and applying the concept to imaginary friends. The show first premiered on Cartoon Network on August 13, 2004, as a 90-minute television film. On August 20, it began its normal run of twenty-to-thirty-minute episodes on Fridays, at 7 pm. The series finished its run on May 3, 2009, with a total of six seasons and seventy-nine episodes. McCracken left Cartoon Network shortly after the series ended. Reruns have aired on Boomerang from August 11, 2012 to November 3, 2013 and again from June 1, 2014 to April 3, 2017.
"""
```

</details>

</details>

## With Transformers

<details>
<summary>Click to learn how to use cde-small-v1 with Transformers</summary>

### Loading the model

Our model can be loaded using `transformers` out-of-the-box with "trust remote code" enabled. We use the default BERT uncased tokenizer:
```python
import transformers

model = transformers.AutoModel.from_pretrained("jxm/cde-small-v1", trust_remote_code=True)
tokenizer = transformers.AutoTokenizer.from_pretrained("bert-base-uncased")
```

#### Note on prefixes

*Nota bene*: Like all state-of-the-art embedding models, our model was trained with task-specific prefixes. To do retrieval, you can prepend the following strings to queries & documents:

```python
query_prefix = "search_query: "
document_prefix = "search_document: "
```

### First stage

```python
minicorpus_size = model.config.transductive_corpus_size
minicorpus_docs = [ ... ] # Put some strings here that are representative of your corpus, for example by calling random.sample(corpus, k=minicorpus_size)
assert len(minicorpus_docs) == minicorpus_size # You must use exactly this many documents in the minicorpus. You can oversample if your corpus is smaller.
minicorpus_docs = tokenizer(
    [document_prefix + doc for doc in minicorpus_docs],
    truncation=True,
    padding=True,
    max_length=512,
    return_tensors="pt"
).to(model.device)
import torch
from tqdm.autonotebook import tqdm

batch_size = 32

dataset_embeddings = []
for i in tqdm(range(0, len(minicorpus_docs["input_ids"]), batch_size)):
    minicorpus_docs_batch = {k: v[i:i+batch_size] for k,v in minicorpus_docs.items()}
    with torch.no_grad():
        dataset_embeddings.append(
            model.first_stage_model(**minicorpus_docs_batch)
        )

dataset_embeddings = torch.cat(dataset_embeddings)
```

### Running the second stage

Now that we have obtained "dataset embeddings" we can embed documents and queries like normal. Remember to use the document prefix for documents:
```python
docs = tokenizer(
    [document_prefix + doc for doc in docs],
    truncation=True,
    padding=True,
    max_length=512,
    return_tensors="pt"
).to(model.device)

with torch.no_grad():
  doc_embeddings = model.second_stage_model(
      input_ids=docs["input_ids"],
      attention_mask=docs["attention_mask"],
      dataset_embeddings=dataset_embeddings,
  )
doc_embeddings /= doc_embeddings.norm(p=2, dim=1, keepdim=True)
```

and the query prefix for queries:
```python
queries = queries.select(range(16))["text"]
queries = tokenizer(
    [query_prefix + query for query in queries],
    truncation=True,
    padding=True,
    max_length=512,
    return_tensors="pt"
).to(model.device)

with torch.no_grad():
  query_embeddings = model.second_stage_model(
      input_ids=queries["input_ids"],
      attention_mask=queries["attention_mask"],
      dataset_embeddings=dataset_embeddings,
  )
query_embeddings /= query_embeddings.norm(p=2, dim=1, keepdim=True)
```

these embeddings can be compared using dot product, since they're normalized.

</details>

### What if I don't know what my corpus will be ahead of time?

If you can't obtain corpus information ahead of time, you still have to pass *something* as the dataset embeddings; our model will work fine in this case, but not quite as well; without corpus information, our model performance drops from 65.0 to 63.8 on MTEB. We provide [some random strings](https://huggingface.co/jxm/cde-small-v1/resolve/main/random_strings.txt) that worked well for us that can be used as a substitute for corpus sampling.

### Colab demo

We've set up a short demo in a Colab notebook showing how you might use our model:
[Try our model in Colab:](https://colab.research.google.com/drive/1r8xwbp7_ySL9lP-ve4XMJAHjidB9UkbL?usp=sharing)

### Acknowledgments

Early experiments on CDE were done with support from [Nomic](https://www.nomic.ai/) and [Hyperbolic](https://hyperbolic.xyz/). We're especially indebted to Nomic for [open-sourcing their efficient BERT implementation and contrastive pre-training data](https://www.nomic.ai/blog/posts/nomic-embed-text-v1), which proved vital in the development of CDE.

### Cite us

Used our model, method, or architecture? Want to cite us? Here's the ArXiv citation information:
```
@misc{morris2024contextualdocumentembeddings,
      title={Contextual Document Embeddings}, 
      author={John X. Morris and Alexander M. Rush},
      year={2024},
      eprint={2410.02525},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.02525}, 
}
```
