---
language:
- ru

pipeline_tag: sentence-similarity

tags:
- russian
- pretraining
- embeddings
- tiny
- feature-extraction
- sentence-similarity
- sentence-transformers
- transformers
- mteb

datasets:
- IlyaGusev/gazeta
- zloelias/lenta-ru

license: mit
base_model: cointegrated/rubert-tiny2
model-index:
- name: sergeyzh/rubert-tiny-turbo
  results:
  - dataset:
      config: default
      name: MTEB AILACasedocs (default)
      revision: 4106e6bcc72e0698d714ea8b101355e3e238431a
      split: test
      type: mteb/AILA_casedocs
    metrics:
    - type: main_score
      value: 7.432999999999999
    - type: map_at_1
      value: 0.604
    - type: map_at_10
      value: 3.8989999999999996
    - type: map_at_100
      value: 7.89
    - type: map_at_1000
      value: 8.417
    - type: map_at_20
      value: 5.007000000000001
    - type: map_at_3
      value: 2.688
    - type: map_at_5
      value: 3.0380000000000003
    - type: mrr_at_1
      value: 6.0
    - type: mrr_at_10
      value: 11.799999999999999
    - type: mrr_at_100
      value: 14.417998426795965
    - type: mrr_at_1000
      value: 14.474056627618499
    - type: mrr_at_20
      value: 13.017532467532467
    - type: mrr_at_3
      value: 10.333333333333334
    - type: mrr_at_5
      value: 10.733333333333333
    - type: nauc_map_at_1000_diff1
      value: -18.649405381116548
    - type: nauc_map_at_1000_max
      value: 53.92467833877199
    - type: nauc_map_at_1000_std
      value: -37.567628121407296
    - type: nauc_map_at_100_diff1
      value: -19.053926237591206
    - type: nauc_map_at_100_max
      value: 53.442907236002725
    - type: nauc_map_at_100_std
      value: -37.310817568902884
    - type: nauc_map_at_10_diff1
      value: -13.464050841785403
    - type: nauc_map_at_10_max
      value: 48.093886298979946
    - type: nauc_map_at_10_std
      value: -34.85388157835729
    - type: nauc_map_at_1_diff1
      value: -13.741863044507388
    - type: nauc_map_at_1_max
      value: 88.80266056441289
    - type: nauc_map_at_1_std
      value: -52.44805080502242
    - type: nauc_map_at_20_diff1
      value: -14.561491138058782
    - type: nauc_map_at_20_max
      value: 48.97477701904
    - type: nauc_map_at_20_std
      value: -31.218577996781537
    - type: nauc_map_at_3_diff1
      value: -15.370170931276068
    - type: nauc_map_at_3_max
      value: 53.443631887225486
    - type: nauc_map_at_3_std
      value: -40.92344513873499
    - type: nauc_map_at_5_diff1
      value: -12.899827975508286
    - type: nauc_map_at_5_max
      value: 56.55724779187716
    - type: nauc_map_at_5_std
      value: -38.50107328981899
    - type: nauc_mrr_at_1000_diff1
      value: -20.480388426956775
    - type: nauc_mrr_at_1000_max
      value: 59.34434186773745
    - type: nauc_mrr_at_1000_std
      value: -38.78219708358511
    - type: nauc_mrr_at_100_diff1
      value: -20.733217227513638
    - type: nauc_mrr_at_100_max
      value: 59.338571965753026
    - type: nauc_mrr_at_100_std
      value: -38.905241386083524
    - type: nauc_mrr_at_10_diff1
      value: -23.191503817950903
    - type: nauc_mrr_at_10_max
      value: 59.40585262343663
    - type: nauc_mrr_at_10_std
      value: -39.558082853802894
    - type: nauc_mrr_at_1_diff1
      value: -18.978624452195685
    - type: nauc_mrr_at_1_max
      value: 88.73088274751811
    - type: nauc_mrr_at_1_std
      value: -52.46400143099903
    - type: nauc_mrr_at_20_diff1
      value: -20.110327257289537
    - type: nauc_mrr_at_20_max
      value: 57.24590011894607
    - type: nauc_mrr_at_20_std
      value: -36.76057923211494
    - type: nauc_mrr_at_3_diff1
      value: -20.292924276357084
    - type: nauc_mrr_at_3_max
      value: 62.92624417852826
    - type: nauc_mrr_at_3_std
      value: -42.31284612573441
    - type: nauc_mrr_at_5_diff1
      value: -22.088780368608298
    - type: nauc_mrr_at_5_max
      value: 61.62928734634482
    - type: nauc_mrr_at_5_std
      value: -38.47155384792127
    - type: nauc_ndcg_at_1000_diff1
      value: -21.96644342707332
    - type: nauc_ndcg_at_1000_max
      value: 54.04115629470727
    - type: nauc_ndcg_at_1000_std
      value: -38.60954619686922
    - type: nauc_ndcg_at_100_diff1
      value: -28.508933576201116
    - type: nauc_ndcg_at_100_max
      value: 53.62925134001747
    - type: nauc_ndcg_at_100_std
      value: -41.66742945815351
    - type: nauc_ndcg_at_10_diff1
      value: -19.22314681419278
    - type: nauc_ndcg_at_10_max
      value: 44.88305374351992
    - type: nauc_ndcg_at_10_std
      value: -32.86086137849654
    - type: nauc_ndcg_at_1_diff1
      value: -18.978624452195685
    - type: nauc_ndcg_at_1_max
      value: 88.73088274751811
    - type: nauc_ndcg_at_1_std
      value: -52.46400143099903
    - type: nauc_ndcg_at_20_diff1
      value: -14.037813797353552
    - type: nauc_ndcg_at_20_max
      value: 43.01748289241327
    - type: nauc_ndcg_at_20_std
      value: -23.548077008049674
    - type: nauc_ndcg_at_3_diff1
      value: -19.9659903984576
    - type: nauc_ndcg_at_3_max
      value: 64.99817864354436
    - type: nauc_ndcg_at_3_std
      value: -45.246163550721796
    - type: nauc_ndcg_at_5_diff1
      value: -20.389688306447788
    - type: nauc_ndcg_at_5_max
      value: 61.370293646369454
    - type: nauc_ndcg_at_5_std
      value: -39.9134710853091
    - type: nauc_precision_at_1000_diff1
      value: -26.69952361901621
    - type: nauc_precision_at_1000_max
      value: 46.40932456102013
    - type: nauc_precision_at_1000_std
      value: -37.38094677778857
    - type: nauc_precision_at_100_diff1
      value: -29.692268260058146
    - type: nauc_precision_at_100_max
      value: 49.265913223173584
    - type: nauc_precision_at_100_std
      value: -41.45888232985447
    - type: nauc_precision_at_10_diff1
      value: -20.974428245377048
    - type: nauc_precision_at_10_max
      value: 53.924262890679564
    - type: nauc_precision_at_10_std
      value: -35.74456192649867
    - type: nauc_precision_at_1_diff1
      value: -18.978624452195685
    - type: nauc_precision_at_1_max
      value: 88.73088274751811
    - type: nauc_precision_at_1_std
      value: -52.46400143099903
    - type: nauc_precision_at_20_diff1
      value: -23.03848763224966
    - type: nauc_precision_at_20_max
      value: 51.19001778609016
    - type: nauc_precision_at_20_std
      value: -33.25265416139501
    - type: nauc_precision_at_3_diff1
      value: -19.497362250879267
    - type: nauc_precision_at_3_max
      value: 64.71277842907384
    - type: nauc_precision_at_3_std
      value: -44.512016412661204
    - type: nauc_precision_at_5_diff1
      value: -18.918918918918912
    - type: nauc_precision_at_5_max
      value: 64.89456489456494
    - type: nauc_precision_at_5_std
      value: -37.37960880818024
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_100_diff1
      value: -44.51937508102329
    - type: nauc_recall_at_100_max
      value: 25.75429602376942
    - type: nauc_recall_at_100_std
      value: -33.30783195688129
    - type: nauc_recall_at_10_diff1
      value: -18.776401920240275
    - type: nauc_recall_at_10_max
      value: 23.00791681188562
    - type: nauc_recall_at_10_std
      value: -21.576198296256532
    - type: nauc_recall_at_1_diff1
      value: -13.741863044507388
    - type: nauc_recall_at_1_max
      value: 88.80266056441289
    - type: nauc_recall_at_1_std
      value: -52.44805080502242
    - type: nauc_recall_at_20_diff1
      value: -3.8724115673803343
    - type: nauc_recall_at_20_max
      value: 21.50124528790692
    - type: nauc_recall_at_20_std
      value: -1.6719812367243132
    - type: nauc_recall_at_3_diff1
      value: -20.21079163108882
    - type: nauc_recall_at_3_max
      value: 42.152167178196684
    - type: nauc_recall_at_3_std
      value: -36.258746145318526
    - type: nauc_recall_at_5_diff1
      value: -22.10269915203519
    - type: nauc_recall_at_5_max
      value: 43.30767031613079
    - type: nauc_recall_at_5_std
      value: -27.398704255640478
    - type: ndcg_at_1
      value: 6.0
    - type: ndcg_at_10
      value: 7.432999999999999
    - type: ndcg_at_100
      value: 26.354
    - type: ndcg_at_1000
      value: 30.558000000000003
    - type: ndcg_at_20
      value: 11.143
    - type: ndcg_at_3
      value: 7.979
    - type: ndcg_at_5
      value: 6.81
    - type: precision_at_1
      value: 6.0
    - type: precision_at_10
      value: 4.2
    - type: precision_at_100
      value: 3.1199999999999997
    - type: precision_at_1000
      value: 0.38999999999999996
    - type: precision_at_20
      value: 4.2
    - type: precision_at_3
      value: 8.0
    - type: precision_at_5
      value: 5.6000000000000005
    - type: recall_at_1
      value: 0.604
    - type: recall_at_10
      value: 9.678
    - type: recall_at_100
      value: 78.645
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 20.79
    - type: recall_at_3
      value: 4.261
    - type: recall_at_5
      value: 5.011
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB AILAStatutes (default)
      revision: ebfcd844eadd3d667efa3c57fc5c8c87f5c2867e
      split: test
      type: mteb/AILA_statutes
    metrics:
    - type: main_score
      value: 13.624
    - type: map_at_1
      value: 1.7999999999999998
    - type: map_at_10
      value: 6.41
    - type: map_at_100
      value: 11.995000000000001
    - type: map_at_1000
      value: 11.995000000000001
    - type: map_at_20
      value: 7.33
    - type: map_at_3
      value: 4.089
    - type: map_at_5
      value: 5.192
    - type: mrr_at_1
      value: 8.0
    - type: mrr_at_10
      value: 20.935714285714287
    - type: mrr_at_100
      value: 23.02755974294914
    - type: mrr_at_1000
      value: 23.02755974294914
    - type: mrr_at_20
      value: 22.1038126476207
    - type: mrr_at_3
      value: 15.333333333333332
    - type: mrr_at_5
      value: 19.533333333333335
    - type: nauc_map_at_1000_diff1
      value: 5.278882422253006
    - type: nauc_map_at_1000_max
      value: 3.7333073133608896
    - type: nauc_map_at_1000_std
      value: -4.5637189871999775
    - type: nauc_map_at_100_diff1
      value: 5.278882422253006
    - type: nauc_map_at_100_max
      value: 3.7333073133608896
    - type: nauc_map_at_100_std
      value: -4.5637189871999775
    - type: nauc_map_at_10_diff1
      value: 8.570212263630141
    - type: nauc_map_at_10_max
      value: -6.6489980060039295
    - type: nauc_map_at_10_std
      value: -12.162352126704402
    - type: nauc_map_at_1_diff1
      value: 7.476969859583216
    - type: nauc_map_at_1_max
      value: -26.629997316876853
    - type: nauc_map_at_1_std
      value: -23.469874489461308
    - type: nauc_map_at_20_diff1
      value: 7.222345063366828
    - type: nauc_map_at_20_max
      value: -2.5103197323267223
    - type: nauc_map_at_20_std
      value: -10.997015623527455
    - type: nauc_map_at_3_diff1
      value: 14.924734426277178
    - type: nauc_map_at_3_max
      value: -11.92937537932614
    - type: nauc_map_at_3_std
      value: -4.9319666083973255
    - type: nauc_map_at_5_diff1
      value: 8.080773945621521
    - type: nauc_map_at_5_max
      value: -3.8175754142607836
    - type: nauc_map_at_5_std
      value: -4.541639774033337
    - type: nauc_mrr_at_1000_diff1
      value: 2.4122089783406646
    - type: nauc_mrr_at_1000_max
      value: -15.876004562207497
    - type: nauc_mrr_at_1000_std
      value: -12.985028057822372
    - type: nauc_mrr_at_100_diff1
      value: 2.4122089783406646
    - type: nauc_mrr_at_100_max
      value: -15.876004562207497
    - type: nauc_mrr_at_100_std
      value: -12.985028057822372
    - type: nauc_mrr_at_10_diff1
      value: 0.2857311186354727
    - type: nauc_mrr_at_10_max
      value: -14.63697545190418
    - type: nauc_mrr_at_10_std
      value: -12.056570964159198
    - type: nauc_mrr_at_1_diff1
      value: 6.868795277703242
    - type: nauc_mrr_at_1_max
      value: -24.845720418567222
    - type: nauc_mrr_at_1_std
      value: -20.686879527770337
    - type: nauc_mrr_at_20_diff1
      value: 1.8452171261188577
    - type: nauc_mrr_at_20_max
      value: -15.538023663956924
    - type: nauc_mrr_at_20_std
      value: -13.690749771450164
    - type: nauc_mrr_at_3_diff1
      value: 10.557261573838256
    - type: nauc_mrr_at_3_max
      value: -20.946427791765498
    - type: nauc_mrr_at_3_std
      value: -9.815750025468983
    - type: nauc_mrr_at_5_diff1
      value: 4.101442020672411
    - type: nauc_mrr_at_5_max
      value: -14.963605604722682
    - type: nauc_mrr_at_5_std
      value: -9.917384084595511
    - type: nauc_ndcg_at_1000_diff1
      value: 0.04370368246080858
    - type: nauc_ndcg_at_1000_max
      value: -0.818088536466922
    - type: nauc_ndcg_at_1000_std
      value: -4.74569960455296
    - type: nauc_ndcg_at_100_diff1
      value: 0.04370368246080858
    - type: nauc_ndcg_at_100_max
      value: -0.818088536466922
    - type: nauc_ndcg_at_100_std
      value: -4.74569960455296
    - type: nauc_ndcg_at_10_diff1
      value: 1.2847289677534977
    - type: nauc_ndcg_at_10_max
      value: -6.3756503900224955
    - type: nauc_ndcg_at_10_std
      value: -12.98730478286347
    - type: nauc_ndcg_at_1_diff1
      value: 6.868795277703242
    - type: nauc_ndcg_at_1_max
      value: -24.845720418567222
    - type: nauc_ndcg_at_1_std
      value: -20.686879527770337
    - type: nauc_ndcg_at_20_diff1
      value: 0.777375339231765
    - type: nauc_ndcg_at_20_max
      value: -0.9649148688381876
    - type: nauc_ndcg_at_20_std
      value: -14.374528790697976
    - type: nauc_ndcg_at_3_diff1
      value: 11.34233767766492
    - type: nauc_ndcg_at_3_max
      value: -13.185097340604685
    - type: nauc_ndcg_at_3_std
      value: -1.42817114044502
    - type: nauc_ndcg_at_5_diff1
      value: 3.6861855424314394
    - type: nauc_ndcg_at_5_max
      value: -3.8049446945965877
    - type: nauc_ndcg_at_5_std
      value: -3.627047155464453
    - type: nauc_precision_at_1000_diff1
      value: -23.534146832293555
    - type: nauc_precision_at_1000_max
      value: 7.621521743107654
    - type: nauc_precision_at_1000_std
      value: 31.79231993560317
    - type: nauc_precision_at_100_diff1
      value: -23.534146832293136
    - type: nauc_precision_at_100_max
      value: 7.6215217431077615
    - type: nauc_precision_at_100_std
      value: 31.792319935603174
    - type: nauc_precision_at_10_diff1
      value: -9.295902835532825
    - type: nauc_precision_at_10_max
      value: -3.516562838357381
    - type: nauc_precision_at_10_std
      value: -9.542266229384722
    - type: nauc_precision_at_1_diff1
      value: 6.868795277703242
    - type: nauc_precision_at_1_max
      value: -24.845720418567222
    - type: nauc_precision_at_1_std
      value: -20.686879527770337
    - type: nauc_precision_at_20_diff1
      value: -9.74438544160727
    - type: nauc_precision_at_20_max
      value: 8.895012105242024
    - type: nauc_precision_at_20_std
      value: -10.653950589210957
    - type: nauc_precision_at_3_diff1
      value: 8.920936116382022
    - type: nauc_precision_at_3_max
      value: -10.246679316888065
    - type: nauc_precision_at_3_std
      value: 5.611638203668553
    - type: nauc_precision_at_5_diff1
      value: -8.265025821338345
    - type: nauc_precision_at_5_max
      value: 7.359630809801093
    - type: nauc_precision_at_5_std
      value: 7.003625975167535
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_100_diff1
      value: .nan
    - type: nauc_recall_at_100_max
      value: .nan
    - type: nauc_recall_at_100_std
      value: .nan
    - type: nauc_recall_at_10_diff1
      value: -1.798034642140945
    - type: nauc_recall_at_10_max
      value: 0.6924952930762724
    - type: nauc_recall_at_10_std
      value: -13.706398349868037
    - type: nauc_recall_at_1_diff1
      value: 7.476969859583216
    - type: nauc_recall_at_1_max
      value: -26.629997316876853
    - type: nauc_recall_at_1_std
      value: -23.469874489461308
    - type: nauc_recall_at_20_diff1
      value: -2.659819202817919
    - type: nauc_recall_at_20_max
      value: 10.517274540935807
    - type: nauc_recall_at_20_std
      value: -14.235421011543991
    - type: nauc_recall_at_3_diff1
      value: 15.662853297442803
    - type: nauc_recall_at_3_max
      value: -11.663877606927189
    - type: nauc_recall_at_3_std
      value: -2.341470241427359
    - type: nauc_recall_at_5_diff1
      value: 2.273326115596832
    - type: nauc_recall_at_5_max
      value: 2.8669632025879537
    - type: nauc_recall_at_5_std
      value: -0.3450165007891684
    - type: ndcg_at_1
      value: 8.0
    - type: ndcg_at_10
      value: 13.624
    - type: ndcg_at_100
      value: 38.109
    - type: ndcg_at_1000
      value: 38.109
    - type: ndcg_at_20
      value: 16.907
    - type: ndcg_at_3
      value: 9.45
    - type: ndcg_at_5
      value: 10.598
    - type: precision_at_1
      value: 8.0
    - type: precision_at_10
      value: 7.3999999999999995
    - type: precision_at_100
      value: 4.34
    - type: precision_at_1000
      value: 0.434
    - type: precision_at_20
      value: 5.5
    - type: precision_at_3
      value: 10.0
    - type: precision_at_5
      value: 10.0
    - type: recall_at_1
      value: 1.7999999999999998
    - type: recall_at_10
      value: 18.333
    - type: recall_at_100
      value: 100.0
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 26.333000000000002
    - type: recall_at_3
      value: 7.867
    - type: recall_at_5
      value: 12.333
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ARCChallenge (default)
      revision: c481e0da3dcbbad8bce7721dea9085b74320a0a3
      split: test
      type: RAR-b/ARC-Challenge
    metrics:
    - type: main_score
      value: 3.8449999999999998
    - type: map_at_1
      value: 1.536
    - type: map_at_10
      value: 2.902
    - type: map_at_100
      value: 3.2259999999999995
    - type: map_at_1000
      value: 3.309
    - type: map_at_20
      value: 3.061
    - type: map_at_3
      value: 2.204
    - type: map_at_5
      value: 2.656
    - type: mrr_at_1
      value: 1.5358361774744027
    - type: mrr_at_10
      value: 2.902107373097134
    - type: mrr_at_100
      value: 3.2259697277173585
    - type: mrr_at_1000
      value: 3.309141234079007
    - type: mrr_at_20
      value: 3.0608339226581975
    - type: mrr_at_3
      value: 2.204209328782707
    - type: mrr_at_5
      value: 2.6564277588168363
    - type: nauc_map_at_1000_diff1
      value: 6.6349335671175
    - type: nauc_map_at_1000_max
      value: 10.045752081479547
    - type: nauc_map_at_1000_std
      value: 5.17373675499246
    - type: nauc_map_at_100_diff1
      value: 6.6240618235225135
    - type: nauc_map_at_100_max
      value: 10.244151375429777
    - type: nauc_map_at_100_std
      value: 5.305639061848512
    - type: nauc_map_at_10_diff1
      value: 7.5024069352343
    - type: nauc_map_at_10_max
      value: 11.928684625428838
    - type: nauc_map_at_10_std
      value: 5.016380398843673
    - type: nauc_map_at_1_diff1
      value: 17.26912687174127
    - type: nauc_map_at_1_max
      value: 6.265273970269121
    - type: nauc_map_at_1_std
      value: -4.8796731336600825
    - type: nauc_map_at_20_diff1
      value: 7.120932496690847
    - type: nauc_map_at_20_max
      value: 11.15762860873897
    - type: nauc_map_at_20_std
      value: 5.342837705336892
    - type: nauc_map_at_3_diff1
      value: 7.138259469017607
    - type: nauc_map_at_3_max
      value: 8.348409228816523
    - type: nauc_map_at_3_std
      value: 6.767314043423357
    - type: nauc_map_at_5_diff1
      value: 7.239963996009633
    - type: nauc_map_at_5_max
      value: 11.068225118567208
    - type: nauc_map_at_5_std
      value: 5.0851302044955835
    - type: nauc_mrr_at_1000_diff1
      value: 6.6349335671175
    - type: nauc_mrr_at_1000_max
      value: 10.045752081479547
    - type: nauc_mrr_at_1000_std
      value: 5.17373675499246
    - type: nauc_mrr_at_100_diff1
      value: 6.6240618235225135
    - type: nauc_mrr_at_100_max
      value: 10.244151375429777
    - type: nauc_mrr_at_100_std
      value: 5.305639061848512
    - type: nauc_mrr_at_10_diff1
      value: 7.5024069352343
    - type: nauc_mrr_at_10_max
      value: 11.928684625428838
    - type: nauc_mrr_at_10_std
      value: 5.016380398843673
    - type: nauc_mrr_at_1_diff1
      value: 17.26912687174127
    - type: nauc_mrr_at_1_max
      value: 6.265273970269121
    - type: nauc_mrr_at_1_std
      value: -4.8796731336600825
    - type: nauc_mrr_at_20_diff1
      value: 7.120932496690847
    - type: nauc_mrr_at_20_max
      value: 11.15762860873897
    - type: nauc_mrr_at_20_std
      value: 5.342837705336892
    - type: nauc_mrr_at_3_diff1
      value: 7.138259469017607
    - type: nauc_mrr_at_3_max
      value: 8.348409228816523
    - type: nauc_mrr_at_3_std
      value: 6.767314043423357
    - type: nauc_mrr_at_5_diff1
      value: 7.239963996009633
    - type: nauc_mrr_at_5_max
      value: 11.068225118567208
    - type: nauc_mrr_at_5_std
      value: 5.0851302044955835
    - type: nauc_ndcg_at_1000_diff1
      value: 3.49547273108029
    - type: nauc_ndcg_at_1000_max
      value: 4.987679792326471
    - type: nauc_ndcg_at_1000_std
      value: 4.792386661474078
    - type: nauc_ndcg_at_100_diff1
      value: 3.423765430486521
    - type: nauc_ndcg_at_100_max
      value: 7.215346434617728
    - type: nauc_ndcg_at_100_std
      value: 6.1334416812657055
    - type: nauc_ndcg_at_10_diff1
      value: 6.211453661355799
    - type: nauc_ndcg_at_10_max
      value: 13.686949611790244
    - type: nauc_ndcg_at_10_std
      value: 5.334521959588366
    - type: nauc_ndcg_at_1_diff1
      value: 17.26912687174127
    - type: nauc_ndcg_at_1_max
      value: 6.265273970269121
    - type: nauc_ndcg_at_1_std
      value: -4.8796731336600825
    - type: nauc_ndcg_at_20_diff1
      value: 5.269692894653953
    - type: nauc_ndcg_at_20_max
      value: 11.466483119515134
    - type: nauc_ndcg_at_20_std
      value: 6.208531132010362
    - type: nauc_ndcg_at_3_diff1
      value: 4.841534563021528
    - type: nauc_ndcg_at_3_max
      value: 8.715299190678648
    - type: nauc_ndcg_at_3_std
      value: 8.889648909403514
    - type: nauc_ndcg_at_5_diff1
      value: 5.5149763431777385
    - type: nauc_ndcg_at_5_max
      value: 12.41579830649011
    - type: nauc_ndcg_at_5_std
      value: 5.8568738487427865
    - type: nauc_precision_at_1000_diff1
      value: 1.0890041942217588
    - type: nauc_precision_at_1000_max
      value: -1.074889035912781
    - type: nauc_precision_at_1000_std
      value: 3.7386321369399207
    - type: nauc_precision_at_100_diff1
      value: 0.24898034725209317
    - type: nauc_precision_at_100_max
      value: 2.6625432444853345
    - type: nauc_precision_at_100_std
      value: 6.760865885892171
    - type: nauc_precision_at_10_diff1
      value: 4.728605530960451
    - type: nauc_precision_at_10_max
      value: 16.098011324014156
    - type: nauc_precision_at_10_std
      value: 5.294918338481019
    - type: nauc_precision_at_1_diff1
      value: 17.26912687174127
    - type: nauc_precision_at_1_max
      value: 6.265273970269121
    - type: nauc_precision_at_1_std
      value: -4.8796731336600825
    - type: nauc_precision_at_20_diff1
      value: 3.1605384012118063
    - type: nauc_precision_at_20_max
      value: 11.228945826678288
    - type: nauc_precision_at_20_std
      value: 7.0587619686895975
    - type: nauc_precision_at_3_diff1
      value: 0.15384889210192554
    - type: nauc_precision_at_3_max
      value: 9.441612052649862
    - type: nauc_precision_at_3_std
      value: 13.110663421557597
    - type: nauc_precision_at_5_diff1
      value: 2.9177590765544803
    - type: nauc_precision_at_5_max
      value: 14.583883090410385
    - type: nauc_precision_at_5_std
      value: 6.761154902844139
    - type: nauc_recall_at_1000_diff1
      value: 1.0890041942217838
    - type: nauc_recall_at_1000_max
      value: -1.0748890359127414
    - type: nauc_recall_at_1000_std
      value: 3.7386321369399447
    - type: nauc_recall_at_100_diff1
      value: 0.2489803472520955
    - type: nauc_recall_at_100_max
      value: 2.6625432444853385
    - type: nauc_recall_at_100_std
      value: 6.7608658858921835
    - type: nauc_recall_at_10_diff1
      value: 4.728605530960435
    - type: nauc_recall_at_10_max
      value: 16.09801132401412
    - type: nauc_recall_at_10_std
      value: 5.294918338481006
    - type: nauc_recall_at_1_diff1
      value: 17.26912687174127
    - type: nauc_recall_at_1_max
      value: 6.265273970269121
    - type: nauc_recall_at_1_std
      value: -4.8796731336600825
    - type: nauc_recall_at_20_diff1
      value: 3.1605384012117814
    - type: nauc_recall_at_20_max
      value: 11.22894582667827
    - type: nauc_recall_at_20_std
      value: 7.0587619686895655
    - type: nauc_recall_at_3_diff1
      value: 0.15384889210195152
    - type: nauc_recall_at_3_max
      value: 9.441612052649868
    - type: nauc_recall_at_3_std
      value: 13.110663421557629
    - type: nauc_recall_at_5_diff1
      value: 2.917759076554466
    - type: nauc_recall_at_5_max
      value: 14.583883090410346
    - type: nauc_recall_at_5_std
      value: 6.761154902844119
    - type: ndcg_at_1
      value: 1.536
    - type: ndcg_at_10
      value: 3.8449999999999998
    - type: ndcg_at_100
      value: 5.772
    - type: ndcg_at_1000
      value: 8.509
    - type: ndcg_at_20
      value: 4.426
    - type: ndcg_at_3
      value: 2.447
    - type: ndcg_at_5
      value: 3.258
    - type: precision_at_1
      value: 1.536
    - type: precision_at_10
      value: 0.6910000000000001
    - type: precision_at_100
      value: 0.168
    - type: precision_at_1000
      value: 0.04
    - type: precision_at_20
      value: 0.461
    - type: precision_at_3
      value: 1.052
    - type: precision_at_5
      value: 1.024
    - type: recall_at_1
      value: 1.536
    - type: recall_at_10
      value: 6.9110000000000005
    - type: recall_at_100
      value: 16.808999999999997
    - type: recall_at_1000
      value: 39.505
    - type: recall_at_20
      value: 9.215
    - type: recall_at_3
      value: 3.157
    - type: recall_at_5
      value: 5.119
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB AlphaNLI (default)
      revision: 303f40ef3d50918d3dc43577d33f2f7344ad72c1
      split: test
      type: RAR-b/alphanli
    metrics:
    - type: main_score
      value: 14.155000000000001
    - type: map_at_1
      value: 8.616
    - type: map_at_10
      value: 12.151
    - type: map_at_100
      value: 12.713
    - type: map_at_1000
      value: 12.790000000000001
    - type: map_at_20
      value: 12.478
    - type: map_at_3
      value: 10.955
    - type: map_at_5
      value: 11.68
    - type: mrr_at_1
      value: 8.616187989556137
    - type: mrr_at_10
      value: 12.151197728873969
    - type: mrr_at_100
      value: 12.713435989405935
    - type: mrr_at_1000
      value: 12.789534083463522
    - type: mrr_at_20
      value: 12.478389119397455
    - type: mrr_at_3
      value: 10.955178416013926
    - type: mrr_at_5
      value: 11.679721496953876
    - type: nauc_map_at_1000_diff1
      value: 38.986525912703435
    - type: nauc_map_at_1000_max
      value: 12.219692225747707
    - type: nauc_map_at_1000_std
      value: 1.2585343212684903
    - type: nauc_map_at_100_diff1
      value: 39.02868722054371
    - type: nauc_map_at_100_max
      value: 12.248003227250122
    - type: nauc_map_at_100_std
      value: 1.2163208553030314
    - type: nauc_map_at_10_diff1
      value: 40.110717683039525
    - type: nauc_map_at_10_max
      value: 12.78605835422205
    - type: nauc_map_at_10_std
      value: 0.6481692151906001
    - type: nauc_map_at_1_diff1
      value: 48.456097345786745
    - type: nauc_map_at_1_max
      value: 14.981869102701411
    - type: nauc_map_at_1_std
      value: -3.0707717911327226
    - type: nauc_map_at_20_diff1
      value: 39.42161381753684
    - type: nauc_map_at_20_max
      value: 12.341429085851182
    - type: nauc_map_at_20_std
      value: 0.8391480542456798
    - type: nauc_map_at_3_diff1
      value: 42.64699229741736
    - type: nauc_map_at_3_max
      value: 13.681396294884618
    - type: nauc_map_at_3_std
      value: -1.3518984290812146
    - type: nauc_map_at_5_diff1
      value: 41.32077190616691
    - type: nauc_map_at_5_max
      value: 13.136429689834436
    - type: nauc_map_at_5_std
      value: 0.32856286589434136
    - type: nauc_mrr_at_1000_diff1
      value: 38.98652591920884
    - type: nauc_mrr_at_1000_max
      value: 12.219692104355413
    - type: nauc_mrr_at_1000_std
      value: 1.2585339367622461
    - type: nauc_mrr_at_100_diff1
      value: 39.02868722054371
    - type: nauc_mrr_at_100_max
      value: 12.248003227250122
    - type: nauc_mrr_at_100_std
      value: 1.2163208553030314
    - type: nauc_mrr_at_10_diff1
      value: 40.110717683039525
    - type: nauc_mrr_at_10_max
      value: 12.78605835422205
    - type: nauc_mrr_at_10_std
      value: 0.6481692151906001
    - type: nauc_mrr_at_1_diff1
      value: 48.456097345786745
    - type: nauc_mrr_at_1_max
      value: 14.981869102701411
    - type: nauc_mrr_at_1_std
      value: -3.0707717911327226
    - type: nauc_mrr_at_20_diff1
      value: 39.42161381753684
    - type: nauc_mrr_at_20_max
      value: 12.341429085851182
    - type: nauc_mrr_at_20_std
      value: 0.8391480542456798
    - type: nauc_mrr_at_3_diff1
      value: 42.64699229741736
    - type: nauc_mrr_at_3_max
      value: 13.681396294884618
    - type: nauc_mrr_at_3_std
      value: -1.3518984290812146
    - type: nauc_mrr_at_5_diff1
      value: 41.32077190616691
    - type: nauc_mrr_at_5_max
      value: 13.136429689834436
    - type: nauc_mrr_at_5_std
      value: 0.32856286589434136
    - type: nauc_ndcg_at_1000_diff1
      value: 31.611075970442926
    - type: nauc_ndcg_at_1000_max
      value: 9.936393145930218
    - type: nauc_ndcg_at_1000_std
      value: 6.71067891152211
    - type: nauc_ndcg_at_100_diff1
      value: 32.58290081795884
    - type: nauc_ndcg_at_100_max
      value: 9.842659588765363
    - type: nauc_ndcg_at_100_std
      value: 5.498554329517975
    - type: nauc_ndcg_at_10_diff1
      value: 36.75293874754393
    - type: nauc_ndcg_at_10_max
      value: 11.803286140726776
    - type: nauc_ndcg_at_10_std
      value: 2.5976940855692074
    - type: nauc_ndcg_at_1_diff1
      value: 48.456097345786745
    - type: nauc_ndcg_at_1_max
      value: 14.981869102701411
    - type: nauc_ndcg_at_1_std
      value: -3.0707717911327226
    - type: nauc_ndcg_at_20_diff1
      value: 34.638144952713866
    - type: nauc_ndcg_at_20_max
      value: 10.449640737261305
    - type: nauc_ndcg_at_20_std
      value: 3.2195824007114675
    - type: nauc_ndcg_at_3_diff1
      value: 41.24511499401773
    - type: nauc_ndcg_at_3_max
      value: 13.384003644595388
    - type: nauc_ndcg_at_3_std
      value: -0.7628562047692254
    - type: nauc_ndcg_at_5_diff1
      value: 39.2155849544026
    - type: nauc_ndcg_at_5_max
      value: 12.577199638671265
    - type: nauc_ndcg_at_5_std
      value: 2.0185641778476127
    - type: nauc_precision_at_1000_diff1
      value: 11.879578040836442
    - type: nauc_precision_at_1000_max
      value: 5.358855936542234
    - type: nauc_precision_at_1000_std
      value: 23.471172109373907
    - type: nauc_precision_at_100_diff1
      value: 18.24569021314919
    - type: nauc_precision_at_100_max
      value: 4.309548949123852
    - type: nauc_precision_at_100_std
      value: 15.884619703445772
    - type: nauc_precision_at_10_diff1
      value: 29.512994402519226
    - type: nauc_precision_at_10_max
      value: 9.634695132770453
    - type: nauc_precision_at_10_std
      value: 6.795536654948908
    - type: nauc_precision_at_1_diff1
      value: 48.456097345786745
    - type: nauc_precision_at_1_max
      value: 14.981869102701411
    - type: nauc_precision_at_1_std
      value: -3.0707717911327226
    - type: nauc_precision_at_20_diff1
      value: 24.18871405534599
    - type: nauc_precision_at_20_max
      value: 6.090279031407053
    - type: nauc_precision_at_20_std
      value: 8.291882200513058
    - type: nauc_precision_at_3_diff1
      value: 37.926451300682054
    - type: nauc_precision_at_3_max
      value: 12.684618853985219
    - type: nauc_precision_at_3_std
      value: 0.6806740647349011
    - type: nauc_precision_at_5_diff1
      value: 34.550519136938384
    - type: nauc_precision_at_5_max
      value: 11.344674575354038
    - type: nauc_precision_at_5_std
      value: 5.985578706127787
    - type: nauc_recall_at_1000_diff1
      value: 11.879578040836519
    - type: nauc_recall_at_1000_max
      value: 5.358855936542304
    - type: nauc_recall_at_1000_std
      value: 23.47117210937398
    - type: nauc_recall_at_100_diff1
      value: 18.245690213149167
    - type: nauc_recall_at_100_max
      value: 4.3095489491238155
    - type: nauc_recall_at_100_std
      value: 15.88461970344576
    - type: nauc_recall_at_10_diff1
      value: 29.512994402519215
    - type: nauc_recall_at_10_max
      value: 9.634695132770442
    - type: nauc_recall_at_10_std
      value: 6.795536654948889
    - type: nauc_recall_at_1_diff1
      value: 48.456097345786745
    - type: nauc_recall_at_1_max
      value: 14.981869102701411
    - type: nauc_recall_at_1_std
      value: -3.0707717911327226
    - type: nauc_recall_at_20_diff1
      value: 24.188714055346
    - type: nauc_recall_at_20_max
      value: 6.09027903140705
    - type: nauc_recall_at_20_std
      value: 8.291882200513056
    - type: nauc_recall_at_3_diff1
      value: 37.92645130068206
    - type: nauc_recall_at_3_max
      value: 12.684618853985235
    - type: nauc_recall_at_3_std
      value: 0.6806740647349308
    - type: nauc_recall_at_5_diff1
      value: 34.55051913693838
    - type: nauc_recall_at_5_max
      value: 11.344674575354015
    - type: nauc_recall_at_5_std
      value: 5.985578706127789
    - type: ndcg_at_1
      value: 8.616
    - type: ndcg_at_10
      value: 14.155000000000001
    - type: ndcg_at_100
      value: 17.102
    - type: ndcg_at_1000
      value: 19.631
    - type: ndcg_at_20
      value: 15.344
    - type: ndcg_at_3
      value: 11.728
    - type: ndcg_at_5
      value: 13.025999999999998
    - type: precision_at_1
      value: 8.616
    - type: precision_at_10
      value: 2.056
    - type: precision_at_100
      value: 0.349
    - type: precision_at_1000
      value: 0.055999999999999994
    - type: precision_at_20
      value: 1.2630000000000001
    - type: precision_at_3
      value: 4.656
    - type: precision_at_5
      value: 3.42
    - type: recall_at_1
      value: 8.616
    - type: recall_at_10
      value: 20.561
    - type: recall_at_100
      value: 34.855999999999995
    - type: recall_at_1000
      value: 55.875
    - type: recall_at_20
      value: 25.261
    - type: recall_at_3
      value: 13.969000000000001
    - type: recall_at_5
      value: 17.102
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB AmazonPolarityClassification (default)
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
      split: test
      type: mteb/amazon_polarity
    metrics:
    - type: accuracy
      value: 68.359575
    - type: ap
      value: 63.04430514461716
    - type: ap_weighted
      value: 63.04430514461716
    - type: f1
      value: 68.12645282836293
    - type: f1_weighted
      value: 68.12645282836293
    - type: main_score
      value: 68.359575
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
      value: 32.031
    - type: map_at_1
      value: 15.363
    - type: map_at_10
      value: 25.629999999999995
    - type: map_at_100
      value: 26.851999999999997
    - type: map_at_1000
      value: 26.916
    - type: map_at_20
      value: 26.401999999999997
    - type: map_at_3
      value: 21.764
    - type: map_at_5
      value: 23.798
    - type: mrr_at_1
      value: 15.647226173541965
    - type: mrr_at_10
      value: 25.74270699270699
    - type: mrr_at_100
      value: 26.95759156481371
    - type: mrr_at_1000
      value: 27.02192945787223
    - type: mrr_at_20
      value: 26.50752832488611
    - type: mrr_at_3
      value: 21.894262683736372
    - type: mrr_at_5
      value: 23.889284020862938
    - type: nauc_map_at_1000_diff1
      value: 9.717094498857836
    - type: nauc_map_at_1000_max
      value: 0.006128824635771366
    - type: nauc_map_at_1000_std
      value: 9.951724867994008
    - type: nauc_map_at_100_diff1
      value: 9.720746167116648
    - type: nauc_map_at_100_max
      value: 0.03921480687966482
    - type: nauc_map_at_100_std
      value: 10.01422840642898
    - type: nauc_map_at_10_diff1
      value: 9.629884802439925
    - type: nauc_map_at_10_max
      value: -0.18895622006721804
    - type: nauc_map_at_10_std
      value: 8.801754758016564
    - type: nauc_map_at_1_diff1
      value: 10.255415606776134
    - type: nauc_map_at_1_max
      value: -2.7429221309654044
    - type: nauc_map_at_1_std
      value: 6.866297123270523
    - type: nauc_map_at_20_diff1
      value: 9.707948736975794
    - type: nauc_map_at_20_max
      value: 0.01892213753638095
    - type: nauc_map_at_20_std
      value: 9.681790764357237
    - type: nauc_map_at_3_diff1
      value: 8.344213156710568
    - type: nauc_map_at_3_max
      value: -2.0132121856529483
    - type: nauc_map_at_3_std
      value: 8.554071405515435
    - type: nauc_map_at_5_diff1
      value: 9.14495583661473
    - type: nauc_map_at_5_max
      value: -1.379873148644914
    - type: nauc_map_at_5_std
      value: 9.044652095982553
    - type: nauc_mrr_at_1000_diff1
      value: 8.520276824384093
    - type: nauc_mrr_at_1000_max
      value: -0.41053299382643904
    - type: nauc_mrr_at_1000_std
      value: 9.770616411797125
    - type: nauc_mrr_at_100_diff1
      value: 8.526357726757498
    - type: nauc_mrr_at_100_max
      value: -0.37675957362198204
    - type: nauc_mrr_at_100_std
      value: 9.833172972935825
    - type: nauc_mrr_at_10_diff1
      value: 8.504469942302443
    - type: nauc_mrr_at_10_max
      value: -0.5555290478828475
    - type: nauc_mrr_at_10_std
      value: 8.67347986151777
    - type: nauc_mrr_at_1_diff1
      value: 8.924965691375194
    - type: nauc_mrr_at_1_max
      value: -2.472212128016505
    - type: nauc_mrr_at_1_std
      value: 6.727737069169365
    - type: nauc_mrr_at_20_diff1
      value: 8.527008337552795
    - type: nauc_mrr_at_20_max
      value: -0.39130673567011953
    - type: nauc_mrr_at_20_std
      value: 9.504234612175194
    - type: nauc_mrr_at_3_diff1
      value: 7.028185998793612
    - type: nauc_mrr_at_3_max
      value: -2.531551924396665
    - type: nauc_mrr_at_3_std
      value: 8.36654956798548
    - type: nauc_mrr_at_5_diff1
      value: 7.946200662893088
    - type: nauc_mrr_at_5_max
      value: -1.8450232157342275
    - type: nauc_mrr_at_5_std
      value: 8.855536533297968
    - type: nauc_ndcg_at_1000_diff1
      value: 10.148046270962398
    - type: nauc_ndcg_at_1000_max
      value: 1.696424601847897
    - type: nauc_ndcg_at_1000_std
      value: 13.134595506556405
    - type: nauc_ndcg_at_100_diff1
      value: 10.478061817612778
    - type: nauc_ndcg_at_100_max
      value: 2.790758084465661
    - type: nauc_ndcg_at_100_std
      value: 14.964733623242607
    - type: nauc_ndcg_at_10_diff1
      value: 10.372927964606154
    - type: nauc_ndcg_at_10_max
      value: 1.9588405301435734
    - type: nauc_ndcg_at_10_std
      value: 9.558148538160015
    - type: nauc_ndcg_at_1_diff1
      value: 10.255415606776134
    - type: nauc_ndcg_at_1_max
      value: -2.7429221309654044
    - type: nauc_ndcg_at_1_std
      value: 6.866297123270523
    - type: nauc_ndcg_at_20_diff1
      value: 10.807055510827903
    - type: nauc_ndcg_at_20_max
      value: 2.873981784514884
    - type: nauc_ndcg_at_20_std
      value: 12.684265114648849
    - type: nauc_ndcg_at_3_diff1
      value: 7.99043332908002
    - type: nauc_ndcg_at_3_max
      value: -1.7537467389545258
    - type: nauc_ndcg_at_3_std
      value: 9.282365459725794
    - type: nauc_ndcg_at_5_diff1
      value: 9.291919447241343
    - type: nauc_ndcg_at_5_max
      value: -0.6986840661830845
    - type: nauc_ndcg_at_5_std
      value: 10.155119795280289
    - type: nauc_precision_at_1000_diff1
      value: 5.534567864242971
    - type: nauc_precision_at_1000_max
      value: 9.529106078051697
    - type: nauc_precision_at_1000_std
      value: 62.0873447350283
    - type: nauc_precision_at_100_diff1
      value: 13.636774071684679
    - type: nauc_precision_at_100_max
      value: 17.905397264353912
    - type: nauc_precision_at_100_std
      value: 49.22170039944941
    - type: nauc_precision_at_10_diff1
      value: 12.676219389202528
    - type: nauc_precision_at_10_max
      value: 8.164707652448252
    - type: nauc_precision_at_10_std
      value: 11.361740427515855
    - type: nauc_precision_at_1_diff1
      value: 10.255415606776134
    - type: nauc_precision_at_1_max
      value: -2.7429221309654044
    - type: nauc_precision_at_1_std
      value: 6.866297123270523
    - type: nauc_precision_at_20_diff1
      value: 15.006293628353006
    - type: nauc_precision_at_20_max
      value: 12.931321039045368
    - type: nauc_precision_at_20_std
      value: 23.758750045585586
    - type: nauc_precision_at_3_diff1
      value: 7.18325478518931
    - type: nauc_precision_at_3_max
      value: -1.1161637595134446
    - type: nauc_precision_at_3_std
      value: 11.09645301286272
    - type: nauc_precision_at_5_diff1
      value: 9.780765614595015
    - type: nauc_precision_at_5_max
      value: 1.0082157901430149
    - type: nauc_precision_at_5_std
      value: 12.92929121494741
    - type: nauc_recall_at_1000_diff1
      value: 5.534567864242688
    - type: nauc_recall_at_1000_max
      value: 9.529106078051411
    - type: nauc_recall_at_1000_std
      value: 62.08734473502826
    - type: nauc_recall_at_100_diff1
      value: 13.63677407168474
    - type: nauc_recall_at_100_max
      value: 17.905397264353898
    - type: nauc_recall_at_100_std
      value: 49.2217003994493
    - type: nauc_recall_at_10_diff1
      value: 12.676219389202512
    - type: nauc_recall_at_10_max
      value: 8.164707652448225
    - type: nauc_recall_at_10_std
      value: 11.361740427515835
    - type: nauc_recall_at_1_diff1
      value: 10.255415606776134
    - type: nauc_recall_at_1_max
      value: -2.7429221309654044
    - type: nauc_recall_at_1_std
      value: 6.866297123270523
    - type: nauc_recall_at_20_diff1
      value: 15.006293628353069
    - type: nauc_recall_at_20_max
      value: 12.931321039045434
    - type: nauc_recall_at_20_std
      value: 23.75875004558557
    - type: nauc_recall_at_3_diff1
      value: 7.183254785189315
    - type: nauc_recall_at_3_max
      value: -1.1161637595134306
    - type: nauc_recall_at_3_std
      value: 11.096453012862733
    - type: nauc_recall_at_5_diff1
      value: 9.780765614595012
    - type: nauc_recall_at_5_max
      value: 1.008215790143006
    - type: nauc_recall_at_5_std
      value: 12.929291214947403
    - type: ndcg_at_1
      value: 15.363
    - type: ndcg_at_10
      value: 32.031
    - type: ndcg_at_100
      value: 38.122
    - type: ndcg_at_1000
      value: 39.864
    - type: ndcg_at_20
      value: 34.849999999999994
    - type: ndcg_at_3
      value: 23.965
    - type: ndcg_at_5
      value: 27.659
    - type: precision_at_1
      value: 15.363
    - type: precision_at_10
      value: 5.277
    - type: precision_at_100
      value: 0.8170000000000001
    - type: precision_at_1000
      value: 0.095
    - type: precision_at_20
      value: 3.197
    - type: precision_at_3
      value: 10.123
    - type: precision_at_5
      value: 7.881
    - type: recall_at_1
      value: 15.363
    - type: recall_at_10
      value: 52.774
    - type: recall_at_100
      value: 81.65
    - type: recall_at_1000
      value: 95.448
    - type: recall_at_20
      value: 63.94
    - type: recall_at_3
      value: 30.37
    - type: recall_at_5
      value: 39.403
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArxivClassification (default)
      revision: f9bd92144ed76200d6eb3ce73a8bd4eba9ffdc85
      split: test
      type: ccdv/arxiv-classification
    metrics:
    - type: accuracy
      value: 43.611999999999995
    - type: f1
      value: 40.930383763906484
    - type: f1_weighted
      value: 41.404367816744276
    - type: main_score
      value: 43.611999999999995
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P (default)
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 24.827354215343842
    - type: v_measure
      value: 24.827354215343842
    - type: v_measure_std
      value: 14.761042346861815
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P.v2 (default)
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 29.14326814807588
    - type: v_measure
      value: 29.14326814807588
    - type: v_measure_std
      value: 16.354623518770328
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
      value: 16.681456170594032
    - type: v_measure
      value: 16.681456170594032
    - type: v_measure_std
      value: 15.806408628434077
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB Banking77Classification (default)
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
      split: test
      type: mteb/banking77
    metrics:
    - type: accuracy
      value: 59.86363636363635
    - type: f1
      value: 58.3300719763065
    - type: f1_weighted
      value: 58.3300719763065
    - type: main_score
      value: 59.86363636363635
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BigPatentClustering (default)
      revision: 62d5330920bca426ce9d3c76ea914f15fc83e891
      split: test
      type: jinaai/big-patent-clustering
    metrics:
    - type: main_score
      value: 17.208517091148714
    - type: v_measure
      value: 17.208517091148714
    - type: v_measure_std
      value: 0.698644666463382
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P (default)
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 19.998032819841395
    - type: v_measure
      value: 19.998032819841395
    - type: v_measure_std
      value: 0.7272995954630507
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
      value: 12.672050490076508
    - type: v_measure
      value: 12.672050490076508
    - type: v_measure_std
      value: 0.7252965151579489
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CEDRClassification (default)
      revision: c0ba03d058e3e1b2f3fd20518875a4563dd12db4
      split: test
      type: ai-forever/cedr-classification
    metrics:
    - type: accuracy
      value: 38.95324123273113
    - type: f1
      value: 30.695742042129776
    - type: lrap
      value: 64.53134962805646
    - type: main_score
      value: 38.95324123273113
    task:
      type: MultilabelClassification
  - dataset:
      config: default
      name: MTEB CPUSpeedTask (default)
      revision: '1.0'
      split: test
      type: 'CPUSpeedTask'
    metrics:
    - type: avg_words_per_sec
      value: 1171249.8059068616
    - type: main_score
      value: 1171249.8059068616
    - type: physical_cores
      value: 3600
    - type: time_mean
      value: 31.018148149762837
    - type: time_std
      value: 10.887230129351211
    - type: total_cores
      value: 7200
    task:
      type: Speed
  - dataset:
      config: default
      name: MTEB CQADupstackAndroidRetrieval (default)
      revision: f46a197baaae43b4f621051089b82a364682dfeb
      split: test
      type: mteb/cqadupstack-android
    metrics:
    - type: main_score
      value: 27.686
    - type: map_at_1
      value: 17.864
    - type: map_at_10
      value: 23.842
    - type: map_at_100
      value: 24.648999999999997
    - type: map_at_1000
      value: 24.771
    - type: map_at_20
      value: 24.277
    - type: map_at_3
      value: 21.938
    - type: map_at_5
      value: 23.058999999999997
    - type: mrr_at_1
      value: 21.888412017167383
    - type: mrr_at_10
      value: 27.934691282330764
    - type: mrr_at_100
      value: 28.58815942555481
    - type: mrr_at_1000
      value: 28.669575168001604
    - type: mrr_at_20
      value: 28.259041893075693
    - type: mrr_at_3
      value: 25.96566523605151
    - type: mrr_at_5
      value: 27.145922746781114
    - type: nauc_map_at_1000_diff1
      value: 38.9362657863528
    - type: nauc_map_at_1000_max
      value: 26.39064664437522
    - type: nauc_map_at_1000_std
      value: -0.3507878980807277
    - type: nauc_map_at_100_diff1
      value: 38.9305380779697
    - type: nauc_map_at_100_max
      value: 26.37667481671251
    - type: nauc_map_at_100_std
      value: -0.4107785241043359
    - type: nauc_map_at_10_diff1
      value: 38.90352635552967
    - type: nauc_map_at_10_max
      value: 26.04843561328241
    - type: nauc_map_at_10_std
      value: -1.0213929777227249
    - type: nauc_map_at_1_diff1
      value: 44.891250111700664
    - type: nauc_map_at_1_max
      value: 27.415379429330695
    - type: nauc_map_at_1_std
      value: -2.083016588225919
    - type: nauc_map_at_20_diff1
      value: 38.94728598104626
    - type: nauc_map_at_20_max
      value: 26.321985371933916
    - type: nauc_map_at_20_std
      value: -0.6740389120283213
    - type: nauc_map_at_3_diff1
      value: 40.75408309900131
    - type: nauc_map_at_3_max
      value: 26.81466083992981
    - type: nauc_map_at_3_std
      value: -1.3446416472047542
    - type: nauc_map_at_5_diff1
      value: 39.55391899732806
    - type: nauc_map_at_5_max
      value: 26.73952942989369
    - type: nauc_map_at_5_std
      value: -0.9241166864360354
    - type: nauc_mrr_at_1000_diff1
      value: 37.49322259212407
    - type: nauc_mrr_at_1000_max
      value: 26.791861376982645
    - type: nauc_mrr_at_1000_std
      value: -0.12058632966589165
    - type: nauc_mrr_at_100_diff1
      value: 37.47912707778518
    - type: nauc_mrr_at_100_max
      value: 26.780040228801354
    - type: nauc_mrr_at_100_std
      value: -0.13375233513915044
    - type: nauc_mrr_at_10_diff1
      value: 37.44982182358103
    - type: nauc_mrr_at_10_max
      value: 26.579194370161574
    - type: nauc_mrr_at_10_std
      value: -0.5519796223426987
    - type: nauc_mrr_at_1_diff1
      value: 43.78241372037574
    - type: nauc_mrr_at_1_max
      value: 29.62575208874629
    - type: nauc_mrr_at_1_std
      value: -0.7403872780711277
    - type: nauc_mrr_at_20_diff1
      value: 37.413002156119
    - type: nauc_mrr_at_20_max
      value: 26.71157844066263
    - type: nauc_mrr_at_20_std
      value: -0.3418018168926074
    - type: nauc_mrr_at_3_diff1
      value: 39.36718212836755
    - type: nauc_mrr_at_3_max
      value: 27.755919798148643
    - type: nauc_mrr_at_3_std
      value: -0.5118015715447669
    - type: nauc_mrr_at_5_diff1
      value: 38.108343388995614
    - type: nauc_mrr_at_5_max
      value: 27.255156457755536
    - type: nauc_mrr_at_5_std
      value: -0.33152296202161974
    - type: nauc_ndcg_at_1000_diff1
      value: 35.45874849790142
    - type: nauc_ndcg_at_1000_max
      value: 26.06624958789977
    - type: nauc_ndcg_at_1000_std
      value: 2.8510315350747746
    - type: nauc_ndcg_at_100_diff1
      value: 35.22563491603818
    - type: nauc_ndcg_at_100_max
      value: 25.482125642505167
    - type: nauc_ndcg_at_100_std
      value: 1.7230614371120136
    - type: nauc_ndcg_at_10_diff1
      value: 35.442027092978336
    - type: nauc_ndcg_at_10_max
      value: 24.43872310681677
    - type: nauc_ndcg_at_10_std
      value: -0.8836727526012238
    - type: nauc_ndcg_at_1_diff1
      value: 43.78241372037574
    - type: nauc_ndcg_at_1_max
      value: 29.62575208874629
    - type: nauc_ndcg_at_1_std
      value: -0.7403872780711277
    - type: nauc_ndcg_at_20_diff1
      value: 35.532620958116226
    - type: nauc_ndcg_at_20_max
      value: 24.9995407161472
    - type: nauc_ndcg_at_20_std
      value: 0.09407090543637946
    - type: nauc_ndcg_at_3_diff1
      value: 38.771875097129474
    - type: nauc_ndcg_at_3_max
      value: 26.88398760762366
    - type: nauc_ndcg_at_3_std
      value: -0.7925347887124169
    - type: nauc_ndcg_at_5_diff1
      value: 36.83295698854961
    - type: nauc_ndcg_at_5_max
      value: 26.254070953306602
    - type: nauc_ndcg_at_5_std
      value: -0.5384138224839687
    - type: nauc_precision_at_1000_diff1
      value: 3.830797202509721
    - type: nauc_precision_at_1000_max
      value: 11.845342201460761
    - type: nauc_precision_at_1000_std
      value: 9.148785863457954
    - type: nauc_precision_at_100_diff1
      value: 13.997075774954821
    - type: nauc_precision_at_100_max
      value: 21.8795221100872
    - type: nauc_precision_at_100_std
      value: 8.373324931296871
    - type: nauc_precision_at_10_diff1
      value: 22.14226604167402
    - type: nauc_precision_at_10_max
      value: 21.908333662820144
    - type: nauc_precision_at_10_std
      value: 2.023219601124639
    - type: nauc_precision_at_1_diff1
      value: 43.78241372037574
    - type: nauc_precision_at_1_max
      value: 29.62575208874629
    - type: nauc_precision_at_1_std
      value: -0.7403872780711277
    - type: nauc_precision_at_20_diff1
      value: 20.193510781013575
    - type: nauc_precision_at_20_max
      value: 21.47063363375231
    - type: nauc_precision_at_20_std
      value: 5.073093391207243
    - type: nauc_precision_at_3_diff1
      value: 33.320150724486965
    - type: nauc_precision_at_3_max
      value: 28.42063777288856
    - type: nauc_precision_at_3_std
      value: 1.3535730617388522
    - type: nauc_precision_at_5_diff1
      value: 26.972979755151126
    - type: nauc_precision_at_5_max
      value: 27.35114981308005
    - type: nauc_precision_at_5_std
      value: 1.5457768965552783
    - type: nauc_recall_at_1000_diff1
      value: 19.86231350512352
    - type: nauc_recall_at_1000_max
      value: 24.527676453832008
    - type: nauc_recall_at_1000_std
      value: 22.21772883429467
    - type: nauc_recall_at_100_diff1
      value: 23.132801377646004
    - type: nauc_recall_at_100_max
      value: 20.988835029134467
    - type: nauc_recall_at_100_std
      value: 8.793975445583824
    - type: nauc_recall_at_10_diff1
      value: 25.796766681233457
    - type: nauc_recall_at_10_max
      value: 17.634361086885264
    - type: nauc_recall_at_10_std
      value: -0.4776257668185774
    - type: nauc_recall_at_1_diff1
      value: 44.891250111700664
    - type: nauc_recall_at_1_max
      value: 27.415379429330695
    - type: nauc_recall_at_1_std
      value: -2.083016588225919
    - type: nauc_recall_at_20_diff1
      value: 25.714655008602115
    - type: nauc_recall_at_20_max
      value: 19.791963050086874
    - type: nauc_recall_at_20_std
      value: 1.9596491600238453
    - type: nauc_recall_at_3_diff1
      value: 34.63094367351514
    - type: nauc_recall_at_3_max
      value: 23.49028309758934
    - type: nauc_recall_at_3_std
      value: -0.8832533681499335
    - type: nauc_recall_at_5_diff1
      value: 30.296413916201175
    - type: nauc_recall_at_5_max
      value: 22.27559868081795
    - type: nauc_recall_at_5_std
      value: 0.7320693658757037
    - type: ndcg_at_1
      value: 21.887999999999998
    - type: ndcg_at_10
      value: 27.686
    - type: ndcg_at_100
      value: 31.363999999999997
    - type: ndcg_at_1000
      value: 34.605000000000004
    - type: ndcg_at_20
      value: 28.93
    - type: ndcg_at_3
      value: 24.576999999999998
    - type: ndcg_at_5
      value: 26.144000000000002
    - type: precision_at_1
      value: 21.887999999999998
    - type: precision_at_10
      value: 5.0360000000000005
    - type: precision_at_100
      value: 0.828
    - type: precision_at_1000
      value: 0.135
    - type: precision_at_20
      value: 2.9690000000000003
    - type: precision_at_3
      value: 11.445
    - type: precision_at_5
      value: 8.269
    - type: recall_at_1
      value: 17.864
    - type: recall_at_10
      value: 34.977999999999994
    - type: recall_at_100
      value: 51.366
    - type: recall_at_1000
      value: 74.505
    - type: recall_at_20
      value: 39.587
    - type: recall_at_3
      value: 25.856
    - type: recall_at_5
      value: 30.215999999999998
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
      value: 17.534
    - type: map_at_1
      value: 11.354000000000001
    - type: map_at_10
      value: 14.847
    - type: map_at_100
      value: 15.49
    - type: map_at_1000
      value: 15.588
    - type: map_at_20
      value: 15.17
    - type: map_at_3
      value: 13.501
    - type: map_at_5
      value: 14.221
    - type: mrr_at_1
      value: 14.26751592356688
    - type: mrr_at_10
      value: 18.05727428975836
    - type: mrr_at_100
      value: 18.690847238016758
    - type: mrr_at_1000
      value: 18.764726106731445
    - type: mrr_at_20
      value: 18.395670843598797
    - type: mrr_at_3
      value: 16.64543524416137
    - type: mrr_at_5
      value: 17.333333333333336
    - type: nauc_map_at_1000_diff1
      value: 43.301676769305494
    - type: nauc_map_at_1000_max
      value: 16.06805541449501
    - type: nauc_map_at_1000_std
      value: 12.507510564248166
    - type: nauc_map_at_100_diff1
      value: 43.34383366787733
    - type: nauc_map_at_100_max
      value: 16.049871088358675
    - type: nauc_map_at_100_std
      value: 12.45712935804974
    - type: nauc_map_at_10_diff1
      value: 43.688675805930785
    - type: nauc_map_at_10_max
      value: 16.41613903348705
    - type: nauc_map_at_10_std
      value: 12.219643122219239
    - type: nauc_map_at_1_diff1
      value: 50.609096395200005
    - type: nauc_map_at_1_max
      value: 18.78413464500168
    - type: nauc_map_at_1_std
      value: 10.90744028944332
    - type: nauc_map_at_20_diff1
      value: 43.49084704145287
    - type: nauc_map_at_20_max
      value: 16.182371186268703
    - type: nauc_map_at_20_std
      value: 12.299197289134225
    - type: nauc_map_at_3_diff1
      value: 45.751823982563266
    - type: nauc_map_at_3_max
      value: 17.192711563068457
    - type: nauc_map_at_3_std
      value: 11.16466159721384
    - type: nauc_map_at_5_diff1
      value: 44.53444696379338
    - type: nauc_map_at_5_max
      value: 16.559164547974103
    - type: nauc_map_at_5_std
      value: 11.928445405766698
    - type: nauc_mrr_at_1000_diff1
      value: 42.29550571785051
    - type: nauc_mrr_at_1000_max
      value: 15.642122643175679
    - type: nauc_mrr_at_1000_std
      value: 12.21491820640565
    - type: nauc_mrr_at_100_diff1
      value: 42.301744065140404
    - type: nauc_mrr_at_100_max
      value: 15.61733477074953
    - type: nauc_mrr_at_100_std
      value: 12.181221737579532
    - type: nauc_mrr_at_10_diff1
      value: 42.670586100296646
    - type: nauc_mrr_at_10_max
      value: 15.926109333510835
    - type: nauc_mrr_at_10_std
      value: 12.192068681943583
    - type: nauc_mrr_at_1_diff1
      value: 51.89198697276755
    - type: nauc_mrr_at_1_max
      value: 19.325504911863643
    - type: nauc_mrr_at_1_std
      value: 12.282190963023766
    - type: nauc_mrr_at_20_diff1
      value: 42.39065015069134
    - type: nauc_mrr_at_20_max
      value: 15.693533741719229
    - type: nauc_mrr_at_20_std
      value: 12.145452140370937
    - type: nauc_mrr_at_3_diff1
      value: 44.715851634047944
    - type: nauc_mrr_at_3_max
      value: 16.790849616314052
    - type: nauc_mrr_at_3_std
      value: 12.056098541376208
    - type: nauc_mrr_at_5_diff1
      value: 43.87033674228477
    - type: nauc_mrr_at_5_max
      value: 16.270118452872623
    - type: nauc_mrr_at_5_std
      value: 12.268005300025886
    - type: nauc_ndcg_at_1000_diff1
      value: 38.01640412131576
    - type: nauc_ndcg_at_1000_max
      value: 14.409491835566401
    - type: nauc_ndcg_at_1000_std
      value: 14.292607075384597
    - type: nauc_ndcg_at_100_diff1
      value: 38.57310899261012
    - type: nauc_ndcg_at_100_max
      value: 13.847832990597306
    - type: nauc_ndcg_at_100_std
      value: 13.318671226615844
    - type: nauc_ndcg_at_10_diff1
      value: 40.02384031953078
    - type: nauc_ndcg_at_10_max
      value: 15.18313865997875
    - type: nauc_ndcg_at_10_std
      value: 12.662598128357672
    - type: nauc_ndcg_at_1_diff1
      value: 51.89198697276755
    - type: nauc_ndcg_at_1_max
      value: 19.325504911863643
    - type: nauc_ndcg_at_1_std
      value: 12.282190963023766
    - type: nauc_ndcg_at_20_diff1
      value: 39.357302335202725
    - type: nauc_ndcg_at_20_max
      value: 14.497857343754966
    - type: nauc_ndcg_at_20_std
      value: 12.630113736826498
    - type: nauc_ndcg_at_3_diff1
      value: 43.58418967840297
    - type: nauc_ndcg_at_3_max
      value: 16.597491536723943
    - type: nauc_ndcg_at_3_std
      value: 11.650784883274328
    - type: nauc_ndcg_at_5_diff1
      value: 42.02130435072668
    - type: nauc_ndcg_at_5_max
      value: 15.627518090215247
    - type: nauc_ndcg_at_5_std
      value: 12.533489817270919
    - type: nauc_precision_at_1000_diff1
      value: 3.679521880714478
    - type: nauc_precision_at_1000_max
      value: 0.7919025640437954
    - type: nauc_precision_at_1000_std
      value: 11.047727940811521
    - type: nauc_precision_at_100_diff1
      value: 19.4078130462856
    - type: nauc_precision_at_100_max
      value: 4.3715506402771425
    - type: nauc_precision_at_100_std
      value: 16.956899011609643
    - type: nauc_precision_at_10_diff1
      value: 28.437045098011527
    - type: nauc_precision_at_10_max
      value: 11.734386703789056
    - type: nauc_precision_at_10_std
      value: 15.714063626213687
    - type: nauc_precision_at_1_diff1
      value: 51.89198697276755
    - type: nauc_precision_at_1_max
      value: 19.325504911863643
    - type: nauc_precision_at_1_std
      value: 12.282190963023766
    - type: nauc_precision_at_20_diff1
      value: 26.61622384998239
    - type: nauc_precision_at_20_max
      value: 9.031660188586937
    - type: nauc_precision_at_20_std
      value: 16.20337620782593
    - type: nauc_precision_at_3_diff1
      value: 38.065037328678045
    - type: nauc_precision_at_3_max
      value: 15.242914979757064
    - type: nauc_precision_at_3_std
      value: 13.448074137354654
    - type: nauc_precision_at_5_diff1
      value: 34.74896073477683
    - type: nauc_precision_at_5_max
      value: 13.347547367557508
    - type: nauc_precision_at_5_std
      value: 15.211527933339694
    - type: nauc_recall_at_1000_diff1
      value: 22.478800979463685
    - type: nauc_recall_at_1000_max
      value: 11.13145140021939
    - type: nauc_recall_at_1000_std
      value: 20.050008624461874
    - type: nauc_recall_at_100_diff1
      value: 25.988786568304555
    - type: nauc_recall_at_100_max
      value: 8.089785168176974
    - type: nauc_recall_at_100_std
      value: 14.262619130209112
    - type: nauc_recall_at_10_diff1
      value: 30.866722162291687
    - type: nauc_recall_at_10_max
      value: 12.14019760016012
    - type: nauc_recall_at_10_std
      value: 12.8097154636935
    - type: nauc_recall_at_1_diff1
      value: 50.609096395200005
    - type: nauc_recall_at_1_max
      value: 18.78413464500168
    - type: nauc_recall_at_1_std
      value: 10.90744028944332
    - type: nauc_recall_at_20_diff1
      value: 28.832935090203225
    - type: nauc_recall_at_20_max
      value: 10.309594281852648
    - type: nauc_recall_at_20_std
      value: 12.251157275647977
    - type: nauc_recall_at_3_diff1
      value: 40.105712098235315
    - type: nauc_recall_at_3_max
      value: 15.165723469178264
    - type: nauc_recall_at_3_std
      value: 10.99744165240917
    - type: nauc_recall_at_5_diff1
      value: 36.09241435581379
    - type: nauc_recall_at_5_max
      value: 13.032542349570054
    - type: nauc_recall_at_5_std
      value: 12.802627519053681
    - type: ndcg_at_1
      value: 14.268
    - type: ndcg_at_10
      value: 17.534
    - type: ndcg_at_100
      value: 20.78
    - type: ndcg_at_1000
      value: 23.526
    - type: ndcg_at_20
      value: 18.567
    - type: ndcg_at_3
      value: 15.218000000000002
    - type: ndcg_at_5
      value: 16.164
    - type: precision_at_1
      value: 14.268
    - type: precision_at_10
      value: 3.312
    - type: precision_at_100
      value: 0.603
    - type: precision_at_1000
      value: 0.105
    - type: precision_at_20
      value: 1.9869999999999999
    - type: precision_at_3
      value: 7.219
    - type: precision_at_5
      value: 5.1209999999999996
    - type: recall_at_1
      value: 11.354000000000001
    - type: recall_at_10
      value: 22.511
    - type: recall_at_100
      value: 37.24
    - type: recall_at_1000
      value: 56.718
    - type: recall_at_20
      value: 26.362999999999996
    - type: recall_at_3
      value: 15.53
    - type: recall_at_5
      value: 18.322
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
      value: 29.03
    - type: map_at_1
      value: 19.307
    - type: map_at_10
      value: 25.453
    - type: map_at_100
      value: 26.33
    - type: map_at_1000
      value: 26.419999999999998
    - type: map_at_20
      value: 25.896
    - type: map_at_3
      value: 23.572000000000003
    - type: map_at_5
      value: 24.694
    - type: mrr_at_1
      value: 22.00626959247649
    - type: mrr_at_10
      value: 27.87858884410605
    - type: mrr_at_100
      value: 28.652814969242712
    - type: mrr_at_1000
      value: 28.725946491824235
    - type: mrr_at_20
      value: 28.276271334002978
    - type: mrr_at_3
      value: 25.997910135841156
    - type: mrr_at_5
      value: 27.11703239289442
    - type: nauc_map_at_1000_diff1
      value: 43.50604073464055
    - type: nauc_map_at_1000_max
      value: 30.480004310005544
    - type: nauc_map_at_1000_std
      value: 0.18281635239684302
    - type: nauc_map_at_100_diff1
      value: 43.51057034900177
    - type: nauc_map_at_100_max
      value: 30.463453039114537
    - type: nauc_map_at_100_std
      value: 0.1392213813651391
    - type: nauc_map_at_10_diff1
      value: 43.680704548271024
    - type: nauc_map_at_10_max
      value: 30.639431323648626
    - type: nauc_map_at_10_std
      value: -0.17722097946115797
    - type: nauc_map_at_1_diff1
      value: 49.51121570705665
    - type: nauc_map_at_1_max
      value: 31.820851746100594
    - type: nauc_map_at_1_std
      value: -2.635315036488275
    - type: nauc_map_at_20_diff1
      value: 43.519636427140746
    - type: nauc_map_at_20_max
      value: 30.479309603785193
    - type: nauc_map_at_20_std
      value: -0.04034004401117608
    - type: nauc_map_at_3_diff1
      value: 44.660054248758726
    - type: nauc_map_at_3_max
      value: 30.35371167828995
    - type: nauc_map_at_3_std
      value: -1.4381463631334364
    - type: nauc_map_at_5_diff1
      value: 44.14458335553869
    - type: nauc_map_at_5_max
      value: 30.49464687257249
    - type: nauc_map_at_5_std
      value: -0.7069576298198817
    - type: nauc_mrr_at_1000_diff1
      value: 43.49091070845857
    - type: nauc_mrr_at_1000_max
      value: 30.904217260073207
    - type: nauc_mrr_at_1000_std
      value: 0.6030969099528762
    - type: nauc_mrr_at_100_diff1
      value: 43.48206732167152
    - type: nauc_mrr_at_100_max
      value: 30.885805566023013
    - type: nauc_mrr_at_100_std
      value: 0.5769328589498474
    - type: nauc_mrr_at_10_diff1
      value: 43.55457392824764
    - type: nauc_mrr_at_10_max
      value: 31.139789286663294
    - type: nauc_mrr_at_10_std
      value: 0.39137312166360116
    - type: nauc_mrr_at_1_diff1
      value: 49.7476817055079
    - type: nauc_mrr_at_1_max
      value: 33.35487810786589
    - type: nauc_mrr_at_1_std
      value: -2.335419312527886
    - type: nauc_mrr_at_20_diff1
      value: 43.48827825669483
    - type: nauc_mrr_at_20_max
      value: 30.983317516254566
    - type: nauc_mrr_at_20_std
      value: 0.4846694988872726
    - type: nauc_mrr_at_3_diff1
      value: 44.66661877146986
    - type: nauc_mrr_at_3_max
      value: 31.31121111690094
    - type: nauc_mrr_at_3_std
      value: -0.5970753554262374
    - type: nauc_mrr_at_5_diff1
      value: 44.05287141220467
    - type: nauc_mrr_at_5_max
      value: 31.185044083863524
    - type: nauc_mrr_at_5_std
      value: 0.03276041839131263
    - type: nauc_ndcg_at_1000_diff1
      value: 40.64648189672279
    - type: nauc_ndcg_at_1000_max
      value: 29.851206560241867
    - type: nauc_ndcg_at_1000_std
      value: 3.7885804314712423
    - type: nauc_ndcg_at_100_diff1
      value: 40.54660606744312
    - type: nauc_ndcg_at_100_max
      value: 29.52262097274987
    - type: nauc_ndcg_at_100_std
      value: 3.1313695052884087
    - type: nauc_ndcg_at_10_diff1
      value: 41.189151331147364
    - type: nauc_ndcg_at_10_max
      value: 30.257730735981376
    - type: nauc_ndcg_at_10_std
      value: 1.483283884208919
    - type: nauc_ndcg_at_1_diff1
      value: 49.7476817055079
    - type: nauc_ndcg_at_1_max
      value: 33.35487810786589
    - type: nauc_ndcg_at_1_std
      value: -2.335419312527886
    - type: nauc_ndcg_at_20_diff1
      value: 40.69940555374264
    - type: nauc_ndcg_at_20_max
      value: 29.67596434757782
    - type: nauc_ndcg_at_20_std
      value: 1.8670302698321029
    - type: nauc_ndcg_at_3_diff1
      value: 43.313981749068034
    - type: nauc_ndcg_at_3_max
      value: 29.92612987963682
    - type: nauc_ndcg_at_3_std
      value: -0.7629159307364975
    - type: nauc_ndcg_at_5_diff1
      value: 42.25367609444526
    - type: nauc_ndcg_at_5_max
      value: 30.011822025139217
    - type: nauc_ndcg_at_5_std
      value: 0.4228958959339596
    - type: nauc_precision_at_1000_diff1
      value: 6.294045364733051
    - type: nauc_precision_at_1000_max
      value: 13.003287301353916
    - type: nauc_precision_at_1000_std
      value: 19.672009407091075
    - type: nauc_precision_at_100_diff1
      value: 18.900847000430282
    - type: nauc_precision_at_100_max
      value: 19.89805341000471
    - type: nauc_precision_at_100_std
      value: 14.097381220216437
    - type: nauc_precision_at_10_diff1
      value: 32.019287482758315
    - type: nauc_precision_at_10_max
      value: 28.868719930088588
    - type: nauc_precision_at_10_std
      value: 7.067713684120723
    - type: nauc_precision_at_1_diff1
      value: 49.7476817055079
    - type: nauc_precision_at_1_max
      value: 33.35487810786589
    - type: nauc_precision_at_1_std
      value: -2.335419312527886
    - type: nauc_precision_at_20_diff1
      value: 27.442952211039866
    - type: nauc_precision_at_20_max
      value: 25.51570310142488
    - type: nauc_precision_at_20_std
      value: 8.001107746535538
    - type: nauc_precision_at_3_diff1
      value: 38.33881569586195
    - type: nauc_precision_at_3_max
      value: 28.995385801766826
    - type: nauc_precision_at_3_std
      value: 0.46426597601937036
    - type: nauc_precision_at_5_diff1
      value: 35.93052673151141
    - type: nauc_precision_at_5_max
      value: 28.77086703745561
    - type: nauc_precision_at_5_std
      value: 3.020792681159482
    - type: nauc_recall_at_1000_diff1
      value: 27.413733064523722
    - type: nauc_recall_at_1000_max
      value: 25.640071347285847
    - type: nauc_recall_at_1000_std
      value: 23.024726525628747
    - type: nauc_recall_at_100_diff1
      value: 30.238748775488382
    - type: nauc_recall_at_100_max
      value: 24.83445535706549
    - type: nauc_recall_at_100_std
      value: 13.213229148027994
    - type: nauc_recall_at_10_diff1
      value: 33.660824128432765
    - type: nauc_recall_at_10_max
      value: 28.239711759937826
    - type: nauc_recall_at_10_std
      value: 5.259078451819804
    - type: nauc_recall_at_1_diff1
      value: 49.51121570705665
    - type: nauc_recall_at_1_max
      value: 31.820851746100594
    - type: nauc_recall_at_1_std
      value: -2.635315036488275
    - type: nauc_recall_at_20_diff1
      value: 31.77661434800746
    - type: nauc_recall_at_20_max
      value: 25.949306594350592
    - type: nauc_recall_at_20_std
      value: 6.611875576453824
    - type: nauc_recall_at_3_diff1
      value: 39.16095910728281
    - type: nauc_recall_at_3_max
      value: 27.64955581506583
    - type: nauc_recall_at_3_std
      value: 0.10121363216139175
    - type: nauc_recall_at_5_diff1
      value: 36.32968291714543
    - type: nauc_recall_at_5_max
      value: 27.325678767283694
    - type: nauc_recall_at_5_std
      value: 2.653663972529844
    - type: ndcg_at_1
      value: 22.006
    - type: ndcg_at_10
      value: 29.03
    - type: ndcg_at_100
      value: 33.318999999999996
    - type: ndcg_at_1000
      value: 35.89
    - type: ndcg_at_20
      value: 30.503999999999998
    - type: ndcg_at_3
      value: 25.348
    - type: ndcg_at_5
      value: 27.267000000000003
    - type: precision_at_1
      value: 22.006
    - type: precision_at_10
      value: 4.627
    - type: precision_at_100
      value: 0.744
    - type: precision_at_1000
      value: 0.10300000000000001
    - type: precision_at_20
      value: 2.702
    - type: precision_at_3
      value: 11.033999999999999
    - type: precision_at_5
      value: 7.861999999999999
    - type: recall_at_1
      value: 19.307
    - type: recall_at_10
      value: 37.624
    - type: recall_at_100
      value: 56.997
    - type: recall_at_1000
      value: 76.62299999999999
    - type: recall_at_20
      value: 43.086
    - type: recall_at_3
      value: 27.724
    - type: recall_at_5
      value: 32.421
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
      value: 14.097000000000001
    - type: map_at_1
      value: 9.109
    - type: map_at_10
      value: 12.062000000000001
    - type: map_at_100
      value: 12.603
    - type: map_at_1000
      value: 12.690000000000001
    - type: map_at_20
      value: 12.335
    - type: map_at_3
      value: 10.882
    - type: map_at_5
      value: 11.445
    - type: mrr_at_1
      value: 9.6045197740113
    - type: mrr_at_10
      value: 13.001390009864586
    - type: mrr_at_100
      value: 13.541388076434767
    - type: mrr_at_1000
      value: 13.622995527273426
    - type: mrr_at_20
      value: 13.261213704134942
    - type: mrr_at_3
      value: 11.75141242937853
    - type: mrr_at_5
      value: 12.3728813559322
    - type: nauc_map_at_1000_diff1
      value: 41.25399941751793
    - type: nauc_map_at_1000_max
      value: 17.60637208770784
    - type: nauc_map_at_1000_std
      value: 3.8997877056955876
    - type: nauc_map_at_100_diff1
      value: 41.3047772590663
    - type: nauc_map_at_100_max
      value: 17.593792209003684
    - type: nauc_map_at_100_std
      value: 3.8624300256381883
    - type: nauc_map_at_10_diff1
      value: 41.918994248720736
    - type: nauc_map_at_10_max
      value: 17.523107069845093
    - type: nauc_map_at_10_std
      value: 3.3289332906481333
    - type: nauc_map_at_1_diff1
      value: 50.853111369434835
    - type: nauc_map_at_1_max
      value: 20.441039981572366
    - type: nauc_map_at_1_std
      value: 2.9730312951046747
    - type: nauc_map_at_20_diff1
      value: 41.676967823092156
    - type: nauc_map_at_20_max
      value: 17.611142954564
    - type: nauc_map_at_20_std
      value: 3.7507161629892516
    - type: nauc_map_at_3_diff1
      value: 45.15865999101332
    - type: nauc_map_at_3_max
      value: 17.51828209554345
    - type: nauc_map_at_3_std
      value: 3.125254352308741
    - type: nauc_map_at_5_diff1
      value: 43.518873099840164
    - type: nauc_map_at_5_max
      value: 18.096843812930256
    - type: nauc_map_at_5_std
      value: 3.501264664850646
    - type: nauc_mrr_at_1000_diff1
      value: 39.65049616843269
    - type: nauc_mrr_at_1000_max
      value: 18.992312109540187
    - type: nauc_mrr_at_1000_std
      value: 3.8630526743174602
    - type: nauc_mrr_at_100_diff1
      value: 39.67790321701619
    - type: nauc_mrr_at_100_max
      value: 18.99280796073833
    - type: nauc_mrr_at_100_std
      value: 3.831281556686595
    - type: nauc_mrr_at_10_diff1
      value: 40.40664164207995
    - type: nauc_mrr_at_10_max
      value: 18.9789911833429
    - type: nauc_mrr_at_10_std
      value: 3.389250639709206
    - type: nauc_mrr_at_1_diff1
      value: 48.90268334274423
    - type: nauc_mrr_at_1_max
      value: 22.148416208142038
    - type: nauc_mrr_at_1_std
      value: 3.482278486678414
    - type: nauc_mrr_at_20_diff1
      value: 40.12944011033672
    - type: nauc_mrr_at_20_max
      value: 19.01229852858854
    - type: nauc_mrr_at_20_std
      value: 3.721020072685762
    - type: nauc_mrr_at_3_diff1
      value: 43.53442474531623
    - type: nauc_mrr_at_3_max
      value: 18.98665230786941
    - type: nauc_mrr_at_3_std
      value: 3.141188860380207
    - type: nauc_mrr_at_5_diff1
      value: 41.792381222269306
    - type: nauc_mrr_at_5_max
      value: 19.564109785495027
    - type: nauc_mrr_at_5_std
      value: 3.447599289829289
    - type: nauc_ndcg_at_1000_diff1
      value: 33.75036088168543
    - type: nauc_ndcg_at_1000_max
      value: 17.552395174719724
    - type: nauc_ndcg_at_1000_std
      value: 6.019653809238646
    - type: nauc_ndcg_at_100_diff1
      value: 34.46011549407109
    - type: nauc_ndcg_at_100_max
      value: 17.261093331357706
    - type: nauc_ndcg_at_100_std
      value: 5.4268706575162104
    - type: nauc_ndcg_at_10_diff1
      value: 37.83747527779143
    - type: nauc_ndcg_at_10_max
      value: 17.044974102007092
    - type: nauc_ndcg_at_10_std
      value: 3.5111959818349603
    - type: nauc_ndcg_at_1_diff1
      value: 48.90268334274423
    - type: nauc_ndcg_at_1_max
      value: 22.148416208142038
    - type: nauc_ndcg_at_1_std
      value: 3.482278486678414
    - type: nauc_ndcg_at_20_diff1
      value: 37.138695182061525
    - type: nauc_ndcg_at_20_max
      value: 17.22387592023126
    - type: nauc_ndcg_at_20_std
      value: 4.770921048488158
    - type: nauc_ndcg_at_3_diff1
      value: 43.268967346255074
    - type: nauc_ndcg_at_3_max
      value: 17.20602008989898
    - type: nauc_ndcg_at_3_std
      value: 3.19589477459749
    - type: nauc_ndcg_at_5_diff1
      value: 40.7884752761726
    - type: nauc_ndcg_at_5_max
      value: 18.121892702668045
    - type: nauc_ndcg_at_5_std
      value: 3.8369089974368573
    - type: nauc_precision_at_1000_diff1
      value: 7.089909563758634
    - type: nauc_precision_at_1000_max
      value: 19.071511820051107
    - type: nauc_precision_at_1000_std
      value: 8.71710715708378
    - type: nauc_precision_at_100_diff1
      value: 17.577598014207858
    - type: nauc_precision_at_100_max
      value: 18.757305391811315
    - type: nauc_precision_at_100_std
      value: 8.571496733416154
    - type: nauc_precision_at_10_diff1
      value: 28.943153297767832
    - type: nauc_precision_at_10_max
      value: 16.38624587520458
    - type: nauc_precision_at_10_std
      value: 3.437574061625469
    - type: nauc_precision_at_1_diff1
      value: 48.90268334274423
    - type: nauc_precision_at_1_max
      value: 22.148416208142038
    - type: nauc_precision_at_1_std
      value: 3.482278486678414
    - type: nauc_precision_at_20_diff1
      value: 26.474908278743044
    - type: nauc_precision_at_20_max
      value: 16.47527151110289
    - type: nauc_precision_at_20_std
      value: 7.5305698853598
    - type: nauc_precision_at_3_diff1
      value: 39.54288018891221
    - type: nauc_precision_at_3_max
      value: 17.284449255178835
    - type: nauc_precision_at_3_std
      value: 2.8714843759024866
    - type: nauc_precision_at_5_diff1
      value: 34.480901699228006
    - type: nauc_precision_at_5_max
      value: 19.44159427138771
    - type: nauc_precision_at_5_std
      value: 3.9140233563987525
    - type: nauc_recall_at_1000_diff1
      value: 14.656193188687894
    - type: nauc_recall_at_1000_max
      value: 15.810571367218888
    - type: nauc_recall_at_1000_std
      value: 12.334573972835202
    - type: nauc_recall_at_100_diff1
      value: 18.594617672285707
    - type: nauc_recall_at_100_max
      value: 15.15863525459292
    - type: nauc_recall_at_100_std
      value: 9.115505114921058
    - type: nauc_recall_at_10_diff1
      value: 29.13269929764077
    - type: nauc_recall_at_10_max
      value: 15.059218016523301
    - type: nauc_recall_at_10_std
      value: 3.7696923586295137
    - type: nauc_recall_at_1_diff1
      value: 50.853111369434835
    - type: nauc_recall_at_1_max
      value: 20.441039981572366
    - type: nauc_recall_at_1_std
      value: 2.9730312951046747
    - type: nauc_recall_at_20_diff1
      value: 27.544653538434776
    - type: nauc_recall_at_20_max
      value: 15.420518066694445
    - type: nauc_recall_at_20_std
      value: 7.101778539671523
    - type: nauc_recall_at_3_diff1
      value: 40.00397565193035
    - type: nauc_recall_at_3_max
      value: 14.717415584208013
    - type: nauc_recall_at_3_std
      value: 3.658957442260116
    - type: nauc_recall_at_5_diff1
      value: 35.35853159550963
    - type: nauc_recall_at_5_max
      value: 17.049909921279315
    - type: nauc_recall_at_5_std
      value: 4.839540342554651
    - type: ndcg_at_1
      value: 9.605
    - type: ndcg_at_10
      value: 14.097000000000001
    - type: ndcg_at_100
      value: 17.098
    - type: ndcg_at_1000
      value: 19.948
    - type: ndcg_at_20
      value: 15.043999999999999
    - type: ndcg_at_3
      value: 11.683
    - type: ndcg_at_5
      value: 12.656999999999998
    - type: precision_at_1
      value: 9.605
    - type: precision_at_10
      value: 2.215
    - type: precision_at_100
      value: 0.395
    - type: precision_at_1000
      value: 0.068
    - type: precision_at_20
      value: 1.322
    - type: precision_at_3
      value: 4.859
    - type: precision_at_5
      value: 3.435
    - type: recall_at_1
      value: 9.109
    - type: recall_at_10
      value: 19.618
    - type: recall_at_100
      value: 34.056
    - type: recall_at_1000
      value: 56.75599999999999
    - type: recall_at_20
      value: 23.168
    - type: recall_at_3
      value: 12.982
    - type: recall_at_5
      value: 15.315000000000001
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
      value: 8.895
    - type: map_at_1
      value: 4.444
    - type: map_at_10
      value: 6.789000000000001
    - type: map_at_100
      value: 7.362
    - type: map_at_1000
      value: 7.455
    - type: map_at_20
      value: 7.112
    - type: map_at_3
      value: 5.819
    - type: map_at_5
      value: 6.237
    - type: mrr_at_1
      value: 5.970149253731343
    - type: mrr_at_10
      value: 8.807500197425577
    - type: mrr_at_100
      value: 9.458867441952432
    - type: mrr_at_1000
      value: 9.550029897135536
    - type: mrr_at_20
      value: 9.191142267117858
    - type: mrr_at_3
      value: 7.669983416252076
    - type: mrr_at_5
      value: 8.229684908789391
    - type: nauc_map_at_1000_diff1
      value: 14.923575664521396
    - type: nauc_map_at_1000_max
      value: 14.637382629018258
    - type: nauc_map_at_1000_std
      value: 7.583317007693739
    - type: nauc_map_at_100_diff1
      value: 14.914938787317187
    - type: nauc_map_at_100_max
      value: 14.57831256590049
    - type: nauc_map_at_100_std
      value: 7.481458525605025
    - type: nauc_map_at_10_diff1
      value: 15.009158630868363
    - type: nauc_map_at_10_max
      value: 14.587168521042992
    - type: nauc_map_at_10_std
      value: 6.30675561821182
    - type: nauc_map_at_1_diff1
      value: 23.073067396533048
    - type: nauc_map_at_1_max
      value: 22.526518534617583
    - type: nauc_map_at_1_std
      value: 3.2886460233623356
    - type: nauc_map_at_20_diff1
      value: 14.55856812493529
    - type: nauc_map_at_20_max
      value: 14.445922336763791
    - type: nauc_map_at_20_std
      value: 7.0979435052536815
    - type: nauc_map_at_3_diff1
      value: 17.401011477759774
    - type: nauc_map_at_3_max
      value: 16.448773676590882
    - type: nauc_map_at_3_std
      value: 4.181405616554917
    - type: nauc_map_at_5_diff1
      value: 15.690380485853476
    - type: nauc_map_at_5_max
      value: 15.435047584962474
    - type: nauc_map_at_5_std
      value: 5.232971650136294
    - type: nauc_mrr_at_1000_diff1
      value: 15.064019296100401
    - type: nauc_mrr_at_1000_max
      value: 15.23275181655676
    - type: nauc_mrr_at_1000_std
      value: 6.62512228446261
    - type: nauc_mrr_at_100_diff1
      value: 15.04422899632206
    - type: nauc_mrr_at_100_max
      value: 15.180132969802102
    - type: nauc_mrr_at_100_std
      value: 6.569986365469756
    - type: nauc_mrr_at_10_diff1
      value: 15.513288408498664
    - type: nauc_mrr_at_10_max
      value: 15.639652887265692
    - type: nauc_mrr_at_10_std
      value: 6.08058172017529
    - type: nauc_mrr_at_1_diff1
      value: 23.174960802057807
    - type: nauc_mrr_at_1_max
      value: 23.10505027161953
    - type: nauc_mrr_at_1_std
      value: 5.000535690775217
    - type: nauc_mrr_at_20_diff1
      value: 14.944086344466943
    - type: nauc_mrr_at_20_max
      value: 15.058772912777219
    - type: nauc_mrr_at_20_std
      value: 6.406714993528487
    - type: nauc_mrr_at_3_diff1
      value: 16.945928540219413
    - type: nauc_mrr_at_3_max
      value: 16.999490982460667
    - type: nauc_mrr_at_3_std
      value: 4.2783371592240185
    - type: nauc_mrr_at_5_diff1
      value: 15.724845028203049
    - type: nauc_mrr_at_5_max
      value: 16.374268642724658
    - type: nauc_mrr_at_5_std
      value: 4.955417882432664
    - type: nauc_ndcg_at_1000_diff1
      value: 12.64441384439761
    - type: nauc_ndcg_at_1000_max
      value: 12.544144311249642
    - type: nauc_ndcg_at_1000_std
      value: 12.203401112537147
    - type: nauc_ndcg_at_100_diff1
      value: 12.856101621820079
    - type: nauc_ndcg_at_100_max
      value: 12.15851341921588
    - type: nauc_ndcg_at_100_std
      value: 11.352600283831114
    - type: nauc_ndcg_at_10_diff1
      value: 12.453755697243285
    - type: nauc_ndcg_at_10_max
      value: 11.750014509834587
    - type: nauc_ndcg_at_10_std
      value: 8.203127809929466
    - type: nauc_ndcg_at_1_diff1
      value: 23.174960802057807
    - type: nauc_ndcg_at_1_max
      value: 23.10505027161953
    - type: nauc_ndcg_at_1_std
      value: 5.000535690775217
    - type: nauc_ndcg_at_20_diff1
      value: 11.324071030247564
    - type: nauc_ndcg_at_20_max
      value: 11.094964112045453
    - type: nauc_ndcg_at_20_std
      value: 9.840879835834757
    - type: nauc_ndcg_at_3_diff1
      value: 15.323525692434862
    - type: nauc_ndcg_at_3_max
      value: 14.559998492898632
    - type: nauc_ndcg_at_3_std
      value: 4.027895180138566
    - type: nauc_ndcg_at_5_diff1
      value: 13.165086940669635
    - type: nauc_ndcg_at_5_max
      value: 13.32440977723948
    - type: nauc_ndcg_at_5_std
      value: 5.813837007263122
    - type: nauc_precision_at_1000_diff1
      value: 0.8928955587806005
    - type: nauc_precision_at_1000_max
      value: 4.446218508931589
    - type: nauc_precision_at_1000_std
      value: 5.877977195844953
    - type: nauc_precision_at_100_diff1
      value: 8.33525852681901
    - type: nauc_precision_at_100_max
      value: 7.830647914480539
    - type: nauc_precision_at_100_std
      value: 14.216797498501176
    - type: nauc_precision_at_10_diff1
      value: 7.765203936267145
    - type: nauc_precision_at_10_max
      value: 7.141939768201643
    - type: nauc_precision_at_10_std
      value: 9.60008810493683
    - type: nauc_precision_at_1_diff1
      value: 23.174960802057807
    - type: nauc_precision_at_1_max
      value: 23.10505027161953
    - type: nauc_precision_at_1_std
      value: 5.000535690775217
    - type: nauc_precision_at_20_diff1
      value: 4.810680914106181
    - type: nauc_precision_at_20_max
      value: 4.6628595108449655
    - type: nauc_precision_at_20_std
      value: 12.601430694735827
    - type: nauc_precision_at_3_diff1
      value: 13.474943796383625
    - type: nauc_precision_at_3_max
      value: 11.709775106648399
    - type: nauc_precision_at_3_std
      value: 3.207743252795555
    - type: nauc_precision_at_5_diff1
      value: 9.95810736829039
    - type: nauc_precision_at_5_max
      value: 10.456953224514239
    - type: nauc_precision_at_5_std
      value: 5.623208634930042
    - type: nauc_recall_at_1000_diff1
      value: 9.834451295472817
    - type: nauc_recall_at_1000_max
      value: 9.848949382055148
    - type: nauc_recall_at_1000_std
      value: 20.975606313150834
    - type: nauc_recall_at_100_diff1
      value: 10.217335772749356
    - type: nauc_recall_at_100_max
      value: 9.152943313782552
    - type: nauc_recall_at_100_std
      value: 17.31335628449071
    - type: nauc_recall_at_10_diff1
      value: 7.002474541545711
    - type: nauc_recall_at_10_max
      value: 5.600453872340962
    - type: nauc_recall_at_10_std
      value: 11.697537334063615
    - type: nauc_recall_at_1_diff1
      value: 23.073067396533048
    - type: nauc_recall_at_1_max
      value: 22.526518534617583
    - type: nauc_recall_at_1_std
      value: 3.2886460233623356
    - type: nauc_recall_at_20_diff1
      value: 5.418370604760854
    - type: nauc_recall_at_20_max
      value: 5.4952006102593085
    - type: nauc_recall_at_20_std
      value: 14.413914588580981
    - type: nauc_recall_at_3_diff1
      value: 12.321251599365478
    - type: nauc_recall_at_3_max
      value: 10.062822926598114
    - type: nauc_recall_at_3_std
      value: 5.2675756103944735
    - type: nauc_recall_at_5_diff1
      value: 7.540388296514483
    - type: nauc_recall_at_5_max
      value: 7.803110889019699
    - type: nauc_recall_at_5_std
      value: 8.317325637513246
    - type: ndcg_at_1
      value: 5.970000000000001
    - type: ndcg_at_10
      value: 8.895
    - type: ndcg_at_100
      value: 11.964
    - type: ndcg_at_1000
      value: 14.860000000000001
    - type: ndcg_at_20
      value: 10.104000000000001
    - type: ndcg_at_3
      value: 6.859999999999999
    - type: ndcg_at_5
      value: 7.573
    - type: precision_at_1
      value: 5.970000000000001
    - type: precision_at_10
      value: 1.779
    - type: precision_at_100
      value: 0.384
    - type: precision_at_1000
      value: 0.073
    - type: precision_at_20
      value: 1.2189999999999999
    - type: precision_at_3
      value: 3.4000000000000004
    - type: precision_at_5
      value: 2.537
    - type: recall_at_1
      value: 4.444
    - type: recall_at_10
      value: 13.751
    - type: recall_at_100
      value: 27.537
    - type: recall_at_1000
      value: 49.079
    - type: recall_at_20
      value: 18.182000000000002
    - type: recall_at_3
      value: 7.731000000000001
    - type: recall_at_5
      value: 9.636
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
      value: 19.902
    - type: map_at_1
      value: 12.928999999999998
    - type: map_at_10
      value: 16.833000000000002
    - type: map_at_100
      value: 17.615
    - type: map_at_1000
      value: 17.732
    - type: map_at_20
      value: 17.207
    - type: map_at_3
      value: 15.463
    - type: map_at_5
      value: 16.128999999999998
    - type: mrr_at_1
      value: 15.976900866217516
    - type: mrr_at_10
      value: 20.444757627144526
    - type: mrr_at_100
      value: 21.18213748325402
    - type: mrr_at_1000
      value: 21.25972081056743
    - type: mrr_at_20
      value: 20.799603260475223
    - type: mrr_at_3
      value: 18.928456849534818
    - type: mrr_at_5
      value: 19.72248957330767
    - type: nauc_map_at_1000_diff1
      value: 41.27196577011274
    - type: nauc_map_at_1000_max
      value: 30.04254002251132
    - type: nauc_map_at_1000_std
      value: 6.570333369920046
    - type: nauc_map_at_100_diff1
      value: 41.27551384135304
    - type: nauc_map_at_100_max
      value: 29.99043897557097
    - type: nauc_map_at_100_std
      value: 6.472408363055328
    - type: nauc_map_at_10_diff1
      value: 41.85444301121017
    - type: nauc_map_at_10_max
      value: 29.81212191843452
    - type: nauc_map_at_10_std
      value: 5.93398567449617
    - type: nauc_map_at_1_diff1
      value: 46.839384517121886
    - type: nauc_map_at_1_max
      value: 33.10314951759653
    - type: nauc_map_at_1_std
      value: 3.473962823858065
    - type: nauc_map_at_20_diff1
      value: 41.4328465682072
    - type: nauc_map_at_20_max
      value: 29.97742898678745
    - type: nauc_map_at_20_std
      value: 6.104796006386177
    - type: nauc_map_at_3_diff1
      value: 43.02691416463743
    - type: nauc_map_at_3_max
      value: 30.42366456898119
    - type: nauc_map_at_3_std
      value: 5.155164523235761
    - type: nauc_map_at_5_diff1
      value: 42.50855309235288
    - type: nauc_map_at_5_max
      value: 30.268005050849005
    - type: nauc_map_at_5_std
      value: 5.5087675809592955
    - type: nauc_mrr_at_1000_diff1
      value: 39.918304151052496
    - type: nauc_mrr_at_1000_max
      value: 32.3633242335842
    - type: nauc_mrr_at_1000_std
      value: 9.821534513339788
    - type: nauc_mrr_at_100_diff1
      value: 39.88894200397407
    - type: nauc_mrr_at_100_max
      value: 32.35005140436353
    - type: nauc_mrr_at_100_std
      value: 9.798405855994671
    - type: nauc_mrr_at_10_diff1
      value: 40.398911825307096
    - type: nauc_mrr_at_10_max
      value: 32.431125056382164
    - type: nauc_mrr_at_10_std
      value: 9.607804963814376
    - type: nauc_mrr_at_1_diff1
      value: 44.710224260402306
    - type: nauc_mrr_at_1_max
      value: 34.810999361965784
    - type: nauc_mrr_at_1_std
      value: 6.666781318158904
    - type: nauc_mrr_at_20_diff1
      value: 40.00961756059491
    - type: nauc_mrr_at_20_max
      value: 32.37658164628154
    - type: nauc_mrr_at_20_std
      value: 9.668733699272558
    - type: nauc_mrr_at_3_diff1
      value: 41.57115214419929
    - type: nauc_mrr_at_3_max
      value: 32.68793918495075
    - type: nauc_mrr_at_3_std
      value: 9.040233893300375
    - type: nauc_mrr_at_5_diff1
      value: 41.06814071330848
    - type: nauc_mrr_at_5_max
      value: 32.8245640568574
    - type: nauc_mrr_at_5_std
      value: 9.58857119627648
    - type: nauc_ndcg_at_1000_diff1
      value: 36.80739838454769
    - type: nauc_ndcg_at_1000_max
      value: 29.789668331458618
    - type: nauc_ndcg_at_1000_std
      value: 11.39764916900706
    - type: nauc_ndcg_at_100_diff1
      value: 37.11213770959871
    - type: nauc_ndcg_at_100_max
      value: 29.081591038980903
    - type: nauc_ndcg_at_100_std
      value: 10.108782506088897
    - type: nauc_ndcg_at_10_diff1
      value: 39.5849935712723
    - type: nauc_ndcg_at_10_max
      value: 28.96898719826389
    - type: nauc_ndcg_at_10_std
      value: 7.961681263212508
    - type: nauc_ndcg_at_1_diff1
      value: 44.710224260402306
    - type: nauc_ndcg_at_1_max
      value: 34.810999361965784
    - type: nauc_ndcg_at_1_std
      value: 6.666781318158904
    - type: nauc_ndcg_at_20_diff1
      value: 38.12032626231077
    - type: nauc_ndcg_at_20_max
      value: 29.18302919363044
    - type: nauc_ndcg_at_20_std
      value: 8.263802202822081
    - type: nauc_ndcg_at_3_diff1
      value: 41.69966283174317
    - type: nauc_ndcg_at_3_max
      value: 30.929246645213066
    - type: nauc_ndcg_at_3_std
      value: 7.216761468782046
    - type: nauc_ndcg_at_5_diff1
      value: 41.01584530945962
    - type: nauc_ndcg_at_5_max
      value: 30.289879950898214
    - type: nauc_ndcg_at_5_std
      value: 7.4367837578277936
    - type: nauc_precision_at_1000_diff1
      value: 5.296272992814253
    - type: nauc_precision_at_1000_max
      value: 19.76310705995752
    - type: nauc_precision_at_1000_std
      value: 24.704985621130156
    - type: nauc_precision_at_100_diff1
      value: 16.46333749868499
    - type: nauc_precision_at_100_max
      value: 26.043739871376527
    - type: nauc_precision_at_100_std
      value: 26.092651162394155
    - type: nauc_precision_at_10_diff1
      value: 30.365327315976653
    - type: nauc_precision_at_10_max
      value: 28.924585920344946
    - type: nauc_precision_at_10_std
      value: 17.70407674779879
    - type: nauc_precision_at_1_diff1
      value: 44.710224260402306
    - type: nauc_precision_at_1_max
      value: 34.810999361965784
    - type: nauc_precision_at_1_std
      value: 6.666781318158904
    - type: nauc_precision_at_20_diff1
      value: 24.315922316558428
    - type: nauc_precision_at_20_max
      value: 28.874260987195967
    - type: nauc_precision_at_20_std
      value: 19.72374746122734
    - type: nauc_precision_at_3_diff1
      value: 37.37798681409137
    - type: nauc_precision_at_3_max
      value: 32.308460896865824
    - type: nauc_precision_at_3_std
      value: 12.279945415003562
    - type: nauc_precision_at_5_diff1
      value: 35.30318091103882
    - type: nauc_precision_at_5_max
      value: 31.820548127213062
    - type: nauc_precision_at_5_std
      value: 14.503599559616163
    - type: nauc_recall_at_1000_diff1
      value: 19.795948815823216
    - type: nauc_recall_at_1000_max
      value: 24.278386660959896
    - type: nauc_recall_at_1000_std
      value: 22.837222421253944
    - type: nauc_recall_at_100_diff1
      value: 24.472612415292573
    - type: nauc_recall_at_100_max
      value: 21.91143710710276
    - type: nauc_recall_at_100_std
      value: 15.053133349737896
    - type: nauc_recall_at_10_diff1
      value: 33.4020176737161
    - type: nauc_recall_at_10_max
      value: 23.033614175897377
    - type: nauc_recall_at_10_std
      value: 8.767203112156356
    - type: nauc_recall_at_1_diff1
      value: 46.839384517121886
    - type: nauc_recall_at_1_max
      value: 33.10314951759653
    - type: nauc_recall_at_1_std
      value: 3.473962823858065
    - type: nauc_recall_at_20_diff1
      value: 28.830072771517113
    - type: nauc_recall_at_20_max
      value: 23.489066180696092
    - type: nauc_recall_at_20_std
      value: 9.12579757868168
    - type: nauc_recall_at_3_diff1
      value: 39.908834198934215
    - type: nauc_recall_at_3_max
      value: 27.068809545101175
    - type: nauc_recall_at_3_std
      value: 6.530892914334164
    - type: nauc_recall_at_5_diff1
      value: 37.48709101560424
    - type: nauc_recall_at_5_max
      value: 26.081573648351025
    - type: nauc_recall_at_5_std
      value: 7.183952029055236
    - type: ndcg_at_1
      value: 15.977
    - type: ndcg_at_10
      value: 19.902
    - type: ndcg_at_100
      value: 24.086
    - type: ndcg_at_1000
      value: 27.01
    - type: ndcg_at_20
      value: 21.175
    - type: ndcg_at_3
      value: 17.330000000000002
    - type: ndcg_at_5
      value: 18.342
    - type: precision_at_1
      value: 15.977
    - type: precision_at_10
      value: 3.542
    - type: precision_at_100
      value: 0.679
    - type: precision_at_1000
      value: 0.109
    - type: precision_at_20
      value: 2.161
    - type: precision_at_3
      value: 8.053
    - type: precision_at_5
      value: 5.679
    - type: recall_at_1
      value: 12.928999999999998
    - type: recall_at_10
      value: 25.916
    - type: recall_at_100
      value: 44.836
    - type: recall_at_1000
      value: 65.22200000000001
    - type: recall_at_20
      value: 30.493
    - type: recall_at_3
      value: 18.241
    - type: recall_at_5
      value: 21.078
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
      value: 15.862000000000002
    - type: map_at_1
      value: 9.831
    - type: map_at_10
      value: 13.256
    - type: map_at_100
      value: 14.008000000000001
    - type: map_at_1000
      value: 14.113000000000001
    - type: map_at_20
      value: 13.636999999999999
    - type: map_at_3
      value: 11.814
    - type: map_at_5
      value: 12.583
    - type: mrr_at_1
      value: 11.757990867579908
    - type: mrr_at_10
      value: 15.494808654055237
    - type: mrr_at_100
      value: 16.291820589502283
    - type: mrr_at_1000
      value: 16.374533932974945
    - type: mrr_at_20
      value: 15.933671804388336
    - type: mrr_at_3
      value: 13.83181126331811
    - type: mrr_at_5
      value: 14.6765601217656
    - type: nauc_map_at_1000_diff1
      value: 33.93453741920144
    - type: nauc_map_at_1000_max
      value: 15.653730492995432
    - type: nauc_map_at_1000_std
      value: 7.8758696471921175
    - type: nauc_map_at_100_diff1
      value: 33.93938109119093
    - type: nauc_map_at_100_max
      value: 15.600263725191917
    - type: nauc_map_at_100_std
      value: 7.765619322590685
    - type: nauc_map_at_10_diff1
      value: 34.54464331832195
    - type: nauc_map_at_10_max
      value: 15.612792960561228
    - type: nauc_map_at_10_std
      value: 6.7557841221613915
    - type: nauc_map_at_1_diff1
      value: 40.25943612185486
    - type: nauc_map_at_1_max
      value: 17.181254846998176
    - type: nauc_map_at_1_std
      value: 4.311873998223975
    - type: nauc_map_at_20_diff1
      value: 34.286604224077294
    - type: nauc_map_at_20_max
      value: 15.557596686810724
    - type: nauc_map_at_20_std
      value: 7.278138397108883
    - type: nauc_map_at_3_diff1
      value: 36.73973255367738
    - type: nauc_map_at_3_max
      value: 16.83994296407283
    - type: nauc_map_at_3_std
      value: 6.223159115827186
    - type: nauc_map_at_5_diff1
      value: 35.141424690409735
    - type: nauc_map_at_5_max
      value: 15.992920926050328
    - type: nauc_map_at_5_std
      value: 6.351250600055855
    - type: nauc_mrr_at_1000_diff1
      value: 34.73310032530598
    - type: nauc_mrr_at_1000_max
      value: 19.015226556944313
    - type: nauc_mrr_at_1000_std
      value: 9.222546150737514
    - type: nauc_mrr_at_100_diff1
      value: 34.726753216593245
    - type: nauc_mrr_at_100_max
      value: 18.99769748963775
    - type: nauc_mrr_at_100_std
      value: 9.174113672327863
    - type: nauc_mrr_at_10_diff1
      value: 35.44871459634613
    - type: nauc_mrr_at_10_max
      value: 19.123376102993888
    - type: nauc_mrr_at_10_std
      value: 8.400683156036651
    - type: nauc_mrr_at_1_diff1
      value: 41.66420742315266
    - type: nauc_mrr_at_1_max
      value: 20.29699577568541
    - type: nauc_mrr_at_1_std
      value: 6.552893551004773
    - type: nauc_mrr_at_20_diff1
      value: 34.97080168567599
    - type: nauc_mrr_at_20_max
      value: 18.93820346421597
    - type: nauc_mrr_at_20_std
      value: 8.88369463529979
    - type: nauc_mrr_at_3_diff1
      value: 37.82881961939195
    - type: nauc_mrr_at_3_max
      value: 20.23353217486363
    - type: nauc_mrr_at_3_std
      value: 8.335430576995872
    - type: nauc_mrr_at_5_diff1
      value: 36.39194951225287
    - type: nauc_mrr_at_5_max
      value: 19.51895403281475
    - type: nauc_mrr_at_5_std
      value: 8.109986680725223
    - type: nauc_ndcg_at_1000_diff1
      value: 29.082397825054134
    - type: nauc_ndcg_at_1000_max
      value: 16.79542535678252
    - type: nauc_ndcg_at_1000_std
      value: 13.862883511514385
    - type: nauc_ndcg_at_100_diff1
      value: 29.052598252998568
    - type: nauc_ndcg_at_100_max
      value: 15.498427568714371
    - type: nauc_ndcg_at_100_std
      value: 11.726792940214132
    - type: nauc_ndcg_at_10_diff1
      value: 32.1345507923688
    - type: nauc_ndcg_at_10_max
      value: 15.522253057572243
    - type: nauc_ndcg_at_10_std
      value: 8.033462171395978
    - type: nauc_ndcg_at_1_diff1
      value: 41.66420742315266
    - type: nauc_ndcg_at_1_max
      value: 20.29699577568541
    - type: nauc_ndcg_at_1_std
      value: 6.552893551004773
    - type: nauc_ndcg_at_20_diff1
      value: 30.9118537718024
    - type: nauc_ndcg_at_20_max
      value: 15.015691320922405
    - type: nauc_ndcg_at_20_std
      value: 9.48348066099931
    - type: nauc_ndcg_at_3_diff1
      value: 36.00136268031041
    - type: nauc_ndcg_at_3_max
      value: 18.106666639494865
    - type: nauc_ndcg_at_3_std
      value: 7.641902435989431
    - type: nauc_ndcg_at_5_diff1
      value: 33.39201547133596
    - type: nauc_ndcg_at_5_max
      value: 16.476689691452638
    - type: nauc_ndcg_at_5_std
      value: 7.369674781372547
    - type: nauc_precision_at_1000_diff1
      value: 6.471252357066656
    - type: nauc_precision_at_1000_max
      value: 19.69714506243997
    - type: nauc_precision_at_1000_std
      value: 19.55604767049242
    - type: nauc_precision_at_100_diff1
      value: 14.901264085785481
    - type: nauc_precision_at_100_max
      value: 18.109459081509822
    - type: nauc_precision_at_100_std
      value: 21.114563137000474
    - type: nauc_precision_at_10_diff1
      value: 27.5518231119986
    - type: nauc_precision_at_10_max
      value: 15.967381663307059
    - type: nauc_precision_at_10_std
      value: 11.45892974481074
    - type: nauc_precision_at_1_diff1
      value: 41.66420742315266
    - type: nauc_precision_at_1_max
      value: 20.29699577568541
    - type: nauc_precision_at_1_std
      value: 6.552893551004773
    - type: nauc_precision_at_20_diff1
      value: 24.871167172495863
    - type: nauc_precision_at_20_max
      value: 16.035625528276007
    - type: nauc_precision_at_20_std
      value: 16.40037479366967
    - type: nauc_precision_at_3_diff1
      value: 35.34609472177138
    - type: nauc_precision_at_3_max
      value: 20.28057060245756
    - type: nauc_precision_at_3_std
      value: 9.58695451354911
    - type: nauc_precision_at_5_diff1
      value: 31.12453786882641
    - type: nauc_precision_at_5_max
      value: 17.714809323391766
    - type: nauc_precision_at_5_std
      value: 9.540687572068887
    - type: nauc_recall_at_1000_diff1
      value: 13.176944792680187
    - type: nauc_recall_at_1000_max
      value: 17.215938373520867
    - type: nauc_recall_at_1000_std
      value: 31.763351387419913
    - type: nauc_recall_at_100_diff1
      value: 15.598307875167269
    - type: nauc_recall_at_100_max
      value: 11.571312022801102
    - type: nauc_recall_at_100_std
      value: 18.72066053860531
    - type: nauc_recall_at_10_diff1
      value: 25.20073017671981
    - type: nauc_recall_at_10_max
      value: 12.05920538584769
    - type: nauc_recall_at_10_std
      value: 9.127287803525167
    - type: nauc_recall_at_1_diff1
      value: 40.25943612185486
    - type: nauc_recall_at_1_max
      value: 17.181254846998176
    - type: nauc_recall_at_1_std
      value: 4.311873998223975
    - type: nauc_recall_at_20_diff1
      value: 21.87476573323018
    - type: nauc_recall_at_20_max
      value: 10.324185189089619
    - type: nauc_recall_at_20_std
      value: 12.342028690096459
    - type: nauc_recall_at_3_diff1
      value: 32.78814063821437
    - type: nauc_recall_at_3_max
      value: 16.638784171801436
    - type: nauc_recall_at_3_std
      value: 8.529115114779637
    - type: nauc_recall_at_5_diff1
      value: 28.192900822422317
    - type: nauc_recall_at_5_max
      value: 13.974726351715857
    - type: nauc_recall_at_5_std
      value: 8.09305084632621
    - type: ndcg_at_1
      value: 11.758000000000001
    - type: ndcg_at_10
      value: 15.862000000000002
    - type: ndcg_at_100
      value: 19.949
    - type: ndcg_at_1000
      value: 22.917
    - type: ndcg_at_20
      value: 17.249
    - type: ndcg_at_3
      value: 12.992
    - type: ndcg_at_5
      value: 14.266000000000002
    - type: precision_at_1
      value: 11.758000000000001
    - type: precision_at_10
      value: 2.82
    - type: precision_at_100
      value: 0.575
    - type: precision_at_1000
      value: 0.098
    - type: precision_at_20
      value: 1.7870000000000001
    - type: precision_at_3
      value: 5.822
    - type: precision_at_5
      value: 4.315
    - type: recall_at_1
      value: 9.831
    - type: recall_at_10
      value: 21.762999999999998
    - type: recall_at_100
      value: 40.207
    - type: recall_at_1000
      value: 61.635
    - type: recall_at_20
      value: 26.826
    - type: recall_at_3
      value: 13.969999999999999
    - type: recall_at_5
      value: 17.154
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval (default)
      revision: CQADupstackRetrieval is a combined dataset
      split: test
      type: CQADupstackRetrieval
    metrics:
    - type: main_score
      value: 17.016083333333334
    - type: ndcg_at_10
      value: 17.016083333333334
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
      value: 11.457
    - type: map_at_1
      value: 6.798
    - type: map_at_10
      value: 9.513
    - type: map_at_100
      value: 10.11
    - type: map_at_1000
      value: 10.181999999999999
    - type: map_at_20
      value: 9.852
    - type: map_at_3
      value: 8.459999999999999
    - type: map_at_5
      value: 9.095
    - type: mrr_at_1
      value: 8.43558282208589
    - type: mrr_at_10
      value: 11.242818190670953
    - type: mrr_at_100
      value: 11.841115877888047
    - type: mrr_at_1000
      value: 11.910635997616325
    - type: mrr_at_20
      value: 11.596258015622588
    - type: mrr_at_3
      value: 10.122699386503067
    - type: mrr_at_5
      value: 10.782208588957056
    - type: nauc_map_at_1000_diff1
      value: 33.754657655521825
    - type: nauc_map_at_1000_max
      value: 20.457874599194977
    - type: nauc_map_at_1000_std
      value: 4.356173597738065
    - type: nauc_map_at_100_diff1
      value: 33.75222679569881
    - type: nauc_map_at_100_max
      value: 20.373956157972724
    - type: nauc_map_at_100_std
      value: 4.252302912475765
    - type: nauc_map_at_10_diff1
      value: 34.77872705587748
    - type: nauc_map_at_10_max
      value: 20.93118729929346
    - type: nauc_map_at_10_std
      value: 3.481910641472398
    - type: nauc_map_at_1_diff1
      value: 42.058523271621276
    - type: nauc_map_at_1_max
      value: 19.398661310678737
    - type: nauc_map_at_1_std
      value: -1.9329828695069966
    - type: nauc_map_at_20_diff1
      value: 34.32132356844234
    - type: nauc_map_at_20_max
      value: 20.836011847513134
    - type: nauc_map_at_20_std
      value: 3.410902073845993
    - type: nauc_map_at_3_diff1
      value: 36.8129992491477
    - type: nauc_map_at_3_max
      value: 21.49364083314497
    - type: nauc_map_at_3_std
      value: 2.8543672506917117
    - type: nauc_map_at_5_diff1
      value: 35.945765614409595
    - type: nauc_map_at_5_max
      value: 21.821959253251073
    - type: nauc_map_at_5_std
      value: 3.1795889661755754
    - type: nauc_mrr_at_1000_diff1
      value: 33.022280754336535
    - type: nauc_mrr_at_1000_max
      value: 20.31974398955361
    - type: nauc_mrr_at_1000_std
      value: 6.915574901994777
    - type: nauc_mrr_at_100_diff1
      value: 32.98012701377776
    - type: nauc_mrr_at_100_max
      value: 20.217936050257485
    - type: nauc_mrr_at_100_std
      value: 6.853368541174533
    - type: nauc_mrr_at_10_diff1
      value: 34.0521482962105
    - type: nauc_mrr_at_10_max
      value: 20.594837283745004
    - type: nauc_mrr_at_10_std
      value: 6.58219400975866
    - type: nauc_mrr_at_1_diff1
      value: 40.45214208803864
    - type: nauc_mrr_at_1_max
      value: 20.246074459121917
    - type: nauc_mrr_at_1_std
      value: 3.6861996527886007
    - type: nauc_mrr_at_20_diff1
      value: 33.40956751827326
    - type: nauc_mrr_at_20_max
      value: 20.570275995460932
    - type: nauc_mrr_at_20_std
      value: 6.243011136595918
    - type: nauc_mrr_at_3_diff1
      value: 36.31911031414795
    - type: nauc_mrr_at_3_max
      value: 21.695701449295836
    - type: nauc_mrr_at_3_std
      value: 6.71267279773233
    - type: nauc_mrr_at_5_diff1
      value: 35.13580430980389
    - type: nauc_mrr_at_5_max
      value: 21.723293067977693
    - type: nauc_mrr_at_5_std
      value: 6.269186070012771
    - type: nauc_ndcg_at_1000_diff1
      value: 26.716650512928574
    - type: nauc_ndcg_at_1000_max
      value: 18.323227051095493
    - type: nauc_ndcg_at_1000_std
      value: 10.182374858813544
    - type: nauc_ndcg_at_100_diff1
      value: 27.023329777242445
    - type: nauc_ndcg_at_100_max
      value: 17.4041094989256
    - type: nauc_ndcg_at_100_std
      value: 8.607201276878204
    - type: nauc_ndcg_at_10_diff1
      value: 31.921453307307818
    - type: nauc_ndcg_at_10_max
      value: 20.328563944294817
    - type: nauc_ndcg_at_10_std
      value: 5.531328567900397
    - type: nauc_ndcg_at_1_diff1
      value: 40.45214208803864
    - type: nauc_ndcg_at_1_max
      value: 20.246074459121917
    - type: nauc_ndcg_at_1_std
      value: 3.6861996527886007
    - type: nauc_ndcg_at_20_diff1
      value: 30.279986443553863
    - type: nauc_ndcg_at_20_max
      value: 20.274259234859194
    - type: nauc_ndcg_at_20_std
      value: 5.0661641286538925
    - type: nauc_ndcg_at_3_diff1
      value: 35.40139952163887
    - type: nauc_ndcg_at_3_max
      value: 21.8390120280498
    - type: nauc_ndcg_at_3_std
      value: 5.417193004461638
    - type: nauc_ndcg_at_5_diff1
      value: 34.323991615044044
    - type: nauc_ndcg_at_5_max
      value: 22.44454175298003
    - type: nauc_ndcg_at_5_std
      value: 5.058913656381477
    - type: nauc_precision_at_1000_diff1
      value: 8.13341460956022
    - type: nauc_precision_at_1000_max
      value: 13.380869610400731
    - type: nauc_precision_at_1000_std
      value: 25.77566088719011
    - type: nauc_precision_at_100_diff1
      value: 12.028198307574947
    - type: nauc_precision_at_100_max
      value: 9.99491259218647
    - type: nauc_precision_at_100_std
      value: 20.26038939641748
    - type: nauc_precision_at_10_diff1
      value: 25.497863066445802
    - type: nauc_precision_at_10_max
      value: 19.951934819022966
    - type: nauc_precision_at_10_std
      value: 13.029428588116488
    - type: nauc_precision_at_1_diff1
      value: 40.45214208803864
    - type: nauc_precision_at_1_max
      value: 20.246074459121917
    - type: nauc_precision_at_1_std
      value: 3.6861996527886007
    - type: nauc_precision_at_20_diff1
      value: 21.270433967723527
    - type: nauc_precision_at_20_max
      value: 20.20704051155486
    - type: nauc_precision_at_20_std
      value: 10.606697205011349
    - type: nauc_precision_at_3_diff1
      value: 34.304974107764636
    - type: nauc_precision_at_3_max
      value: 24.786027767206704
    - type: nauc_precision_at_3_std
      value: 12.919584289443248
    - type: nauc_precision_at_5_diff1
      value: 31.235010233089454
    - type: nauc_precision_at_5_max
      value: 25.888178221422027
    - type: nauc_precision_at_5_std
      value: 12.04974180403603
    - type: nauc_recall_at_1000_diff1
      value: 10.70347303527697
    - type: nauc_recall_at_1000_max
      value: 11.531776655259092
    - type: nauc_recall_at_1000_std
      value: 20.09518174937834
    - type: nauc_recall_at_100_diff1
      value: 12.277161162587646
    - type: nauc_recall_at_100_max
      value: 9.031651314357903
    - type: nauc_recall_at_100_std
      value: 14.946530478779566
    - type: nauc_recall_at_10_diff1
      value: 25.751282561301597
    - type: nauc_recall_at_10_max
      value: 18.410538940956624
    - type: nauc_recall_at_10_std
      value: 7.052566618916148
    - type: nauc_recall_at_1_diff1
      value: 42.058523271621276
    - type: nauc_recall_at_1_max
      value: 19.398661310678737
    - type: nauc_recall_at_1_std
      value: -1.9329828695069966
    - type: nauc_recall_at_20_diff1
      value: 21.876105916783473
    - type: nauc_recall_at_20_max
      value: 18.14029808306082
    - type: nauc_recall_at_20_std
      value: 5.721370338729993
    - type: nauc_recall_at_3_diff1
      value: 32.349105117433645
    - type: nauc_recall_at_3_max
      value: 22.475284730157217
    - type: nauc_recall_at_3_std
      value: 6.577737452085277
    - type: nauc_recall_at_5_diff1
      value: 30.45726437530916
    - type: nauc_recall_at_5_max
      value: 22.993204324458517
    - type: nauc_recall_at_5_std
      value: 6.237822274407502
    - type: ndcg_at_1
      value: 8.436
    - type: ndcg_at_10
      value: 11.457
    - type: ndcg_at_100
      value: 14.618
    - type: ndcg_at_1000
      value: 16.803
    - type: ndcg_at_20
      value: 12.67
    - type: ndcg_at_3
      value: 9.396
    - type: ndcg_at_5
      value: 10.458
    - type: precision_at_1
      value: 8.436
    - type: precision_at_10
      value: 2.025
    - type: precision_at_100
      value: 0.391
    - type: precision_at_1000
      value: 0.063
    - type: precision_at_20
      value: 1.304
    - type: precision_at_3
      value: 4.192
    - type: precision_at_5
      value: 3.221
    - type: recall_at_1
      value: 6.798
    - type: recall_at_10
      value: 15.878999999999998
    - type: recall_at_100
      value: 30.768
    - type: recall_at_1000
      value: 47.451
    - type: recall_at_20
      value: 20.466
    - type: recall_at_3
      value: 10.224
    - type: recall_at_5
      value: 12.881
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
      value: 9.754999999999999
    - type: map_at_1
      value: 5.489999999999999
    - type: map_at_10
      value: 7.9350000000000005
    - type: map_at_100
      value: 8.376999999999999
    - type: map_at_1000
      value: 8.458
    - type: map_at_20
      value: 8.14
    - type: map_at_3
      value: 7.166
    - type: map_at_5
      value: 7.5840000000000005
    - type: mrr_at_1
      value: 7.054370268410186
    - type: mrr_at_10
      value: 9.948655764209787
    - type: mrr_at_100
      value: 10.44089540191581
    - type: mrr_at_1000
      value: 10.510808098620316
    - type: mrr_at_20
      value: 10.18549289814409
    - type: mrr_at_3
      value: 9.027299839412715
    - type: mrr_at_5
      value: 9.52626749254416
    - type: nauc_map_at_1000_diff1
      value: 32.76388527748132
    - type: nauc_map_at_1000_max
      value: 26.76472945437023
    - type: nauc_map_at_1000_std
      value: 5.076773141116664
    - type: nauc_map_at_100_diff1
      value: 32.84910041131489
    - type: nauc_map_at_100_max
      value: 26.776649275369763
    - type: nauc_map_at_100_std
      value: 4.982288267487467
    - type: nauc_map_at_10_diff1
      value: 33.69288297350157
    - type: nauc_map_at_10_max
      value: 27.030787162656093
    - type: nauc_map_at_10_std
      value: 4.319996549665479
    - type: nauc_map_at_1_diff1
      value: 45.07110295953283
    - type: nauc_map_at_1_max
      value: 31.183919870403624
    - type: nauc_map_at_1_std
      value: 3.2596636083232524
    - type: nauc_map_at_20_diff1
      value: 33.18385578478434
    - type: nauc_map_at_20_max
      value: 26.750880392311256
    - type: nauc_map_at_20_std
      value: 4.560028824060983
    - type: nauc_map_at_3_diff1
      value: 36.134060387060806
    - type: nauc_map_at_3_max
      value: 28.53718072767372
    - type: nauc_map_at_3_std
      value: 3.8039060416364054
    - type: nauc_map_at_5_diff1
      value: 34.85287692775015
    - type: nauc_map_at_5_max
      value: 27.89364342330856
    - type: nauc_map_at_5_std
      value: 4.119474259507159
    - type: nauc_mrr_at_1000_diff1
      value: 32.015809492076826
    - type: nauc_mrr_at_1000_max
      value: 27.431639711646994
    - type: nauc_mrr_at_1000_std
      value: 5.95554166485951
    - type: nauc_mrr_at_100_diff1
      value: 32.07039747646208
    - type: nauc_mrr_at_100_max
      value: 27.452847130237775
    - type: nauc_mrr_at_100_std
      value: 5.905310921828455
    - type: nauc_mrr_at_10_diff1
      value: 32.93108532798797
    - type: nauc_mrr_at_10_max
      value: 27.768472855609204
    - type: nauc_mrr_at_10_std
      value: 5.580104763303006
    - type: nauc_mrr_at_1_diff1
      value: 43.888408590108355
    - type: nauc_mrr_at_1_max
      value: 32.903967259484176
    - type: nauc_mrr_at_1_std
      value: 3.514629542175588
    - type: nauc_mrr_at_20_diff1
      value: 32.408176921975254
    - type: nauc_mrr_at_20_max
      value: 27.470576205679897
    - type: nauc_mrr_at_20_std
      value: 5.716181575723001
    - type: nauc_mrr_at_3_diff1
      value: 35.354655207362356
    - type: nauc_mrr_at_3_max
      value: 29.14309593167405
    - type: nauc_mrr_at_3_std
      value: 4.63189493416609
    - type: nauc_mrr_at_5_diff1
      value: 33.970622089384825
    - type: nauc_mrr_at_5_max
      value: 28.6239836688986
    - type: nauc_mrr_at_5_std
      value: 5.122010745650993
    - type: nauc_ndcg_at_1000_diff1
      value: 25.030181517448163
    - type: nauc_ndcg_at_1000_max
      value: 24.25419053775242
    - type: nauc_ndcg_at_1000_std
      value: 9.178235317241148
    - type: nauc_ndcg_at_100_diff1
      value: 26.546832760443966
    - type: nauc_ndcg_at_100_max
      value: 24.42201784253177
    - type: nauc_ndcg_at_100_std
      value: 7.9899910907634375
    - type: nauc_ndcg_at_10_diff1
      value: 29.856179532797423
    - type: nauc_ndcg_at_10_max
      value: 25.424197578846012
    - type: nauc_ndcg_at_10_std
      value: 5.1638300059562035
    - type: nauc_ndcg_at_1_diff1
      value: 43.888408590108355
    - type: nauc_ndcg_at_1_max
      value: 32.903967259484176
    - type: nauc_ndcg_at_1_std
      value: 3.514629542175588
    - type: nauc_ndcg_at_20_diff1
      value: 28.387788168718874
    - type: nauc_ndcg_at_20_max
      value: 24.54850515588615
    - type: nauc_ndcg_at_20_std
      value: 5.896669986261477
    - type: nauc_ndcg_at_3_diff1
      value: 34.072630397644424
    - type: nauc_ndcg_at_3_max
      value: 28.28910465749962
    - type: nauc_ndcg_at_3_std
      value: 4.108392335721374
    - type: nauc_ndcg_at_5_diff1
      value: 32.01123351290829
    - type: nauc_ndcg_at_5_max
      value: 27.245024254467303
    - type: nauc_ndcg_at_5_std
      value: 4.721870277645733
    - type: nauc_precision_at_1000_diff1
      value: 10.47217681263907
    - type: nauc_precision_at_1000_max
      value: 20.919793131324727
    - type: nauc_precision_at_1000_std
      value: 14.804007062294563
    - type: nauc_precision_at_100_diff1
      value: 16.685502515637722
    - type: nauc_precision_at_100_max
      value: 23.37373409901207
    - type: nauc_precision_at_100_std
      value: 13.953311698132442
    - type: nauc_precision_at_10_diff1
      value: 22.478790016325785
    - type: nauc_precision_at_10_max
      value: 23.607477242235102
    - type: nauc_precision_at_10_std
      value: 7.794068171304157
    - type: nauc_precision_at_1_diff1
      value: 43.888408590108355
    - type: nauc_precision_at_1_max
      value: 32.903967259484176
    - type: nauc_precision_at_1_std
      value: 3.514629542175588
    - type: nauc_precision_at_20_diff1
      value: 19.959179713421722
    - type: nauc_precision_at_20_max
      value: 21.738126842321893
    - type: nauc_precision_at_20_std
      value: 9.007914166096132
    - type: nauc_precision_at_3_diff1
      value: 29.984253127282134
    - type: nauc_precision_at_3_max
      value: 28.271022607772796
    - type: nauc_precision_at_3_std
      value: 5.620451575052563
    - type: nauc_precision_at_5_diff1
      value: 26.198401324939464
    - type: nauc_precision_at_5_max
      value: 26.593956126902786
    - type: nauc_precision_at_5_std
      value: 6.684705108310583
    - type: nauc_recall_at_1000_diff1
      value: 9.812234445343657
    - type: nauc_recall_at_1000_max
      value: 17.800710147129053
    - type: nauc_recall_at_1000_std
      value: 15.826278320231745
    - type: nauc_recall_at_100_diff1
      value: 14.586175748060896
    - type: nauc_recall_at_100_max
      value: 18.340956025066333
    - type: nauc_recall_at_100_std
      value: 12.791161727474043
    - type: nauc_recall_at_10_diff1
      value: 21.286255365948538
    - type: nauc_recall_at_10_max
      value: 20.04866550317387
    - type: nauc_recall_at_10_std
      value: 5.645106302785361
    - type: nauc_recall_at_1_diff1
      value: 45.07110295953283
    - type: nauc_recall_at_1_max
      value: 31.183919870403624
    - type: nauc_recall_at_1_std
      value: 3.2596636083232524
    - type: nauc_recall_at_20_diff1
      value: 18.757519729175094
    - type: nauc_recall_at_20_max
      value: 18.59809411356838
    - type: nauc_recall_at_20_std
      value: 7.482712453171494
    - type: nauc_recall_at_3_diff1
      value: 29.350550830882405
    - type: nauc_recall_at_3_max
      value: 26.26284543188125
    - type: nauc_recall_at_3_std
      value: 4.284032658092434
    - type: nauc_recall_at_5_diff1
      value: 25.247444183841345
    - type: nauc_recall_at_5_max
      value: 23.639030774195213
    - type: nauc_recall_at_5_std
      value: 5.05748857090612
    - type: ndcg_at_1
      value: 7.054
    - type: ndcg_at_10
      value: 9.754999999999999
    - type: ndcg_at_100
      value: 12.252
    - type: ndcg_at_1000
      value: 14.658999999999999
    - type: ndcg_at_20
      value: 10.508000000000001
    - type: ndcg_at_3
      value: 8.265
    - type: ndcg_at_5
      value: 8.929
    - type: precision_at_1
      value: 7.054
    - type: precision_at_10
      value: 1.807
    - type: precision_at_100
      value: 0.368
    - type: precision_at_1000
      value: 0.06899999999999999
    - type: precision_at_20
      value: 1.1199999999999999
    - type: precision_at_3
      value: 3.9690000000000003
    - type: precision_at_5
      value: 2.863
    - type: recall_at_1
      value: 5.489999999999999
    - type: recall_at_10
      value: 13.422
    - type: recall_at_100
      value: 24.962999999999997
    - type: recall_at_1000
      value: 42.725
    - type: recall_at_20
      value: 16.259
    - type: recall_at_3
      value: 9.155000000000001
    - type: recall_at_5
      value: 10.923
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
      value: 16.884
    - type: map_at_1
      value: 11.259
    - type: map_at_10
      value: 14.371999999999998
    - type: map_at_100
      value: 14.921999999999999
    - type: map_at_1000
      value: 15.012
    - type: map_at_20
      value: 14.643
    - type: map_at_3
      value: 13.196
    - type: map_at_5
      value: 13.786000000000001
    - type: mrr_at_1
      value: 13.619402985074627
    - type: mrr_at_10
      value: 17.155739161336175
    - type: mrr_at_100
      value: 17.682382182436477
    - type: mrr_at_1000
      value: 17.762865075369113
    - type: mrr_at_20
      value: 17.394179616617638
    - type: mrr_at_3
      value: 15.951492537313436
    - type: mrr_at_5
      value: 16.497201492537318
    - type: nauc_map_at_1000_diff1
      value: 47.4265740975564
    - type: nauc_map_at_1000_max
      value: 28.882262726128438
    - type: nauc_map_at_1000_std
      value: 8.733456805684261
    - type: nauc_map_at_100_diff1
      value: 47.47182414534892
    - type: nauc_map_at_100_max
      value: 28.85824710228484
    - type: nauc_map_at_100_std
      value: 8.689373453465027
    - type: nauc_map_at_10_diff1
      value: 48.02651594284678
    - type: nauc_map_at_10_max
      value: 29.238822235344035
    - type: nauc_map_at_10_std
      value: 8.33007800978345
    - type: nauc_map_at_1_diff1
      value: 56.39452680423106
    - type: nauc_map_at_1_max
      value: 32.60008414160042
    - type: nauc_map_at_1_std
      value: 6.843961503288069
    - type: nauc_map_at_20_diff1
      value: 47.63901968476526
    - type: nauc_map_at_20_max
      value: 29.025324617088327
    - type: nauc_map_at_20_std
      value: 8.643210479120588
    - type: nauc_map_at_3_diff1
      value: 49.40628498975407
    - type: nauc_map_at_3_max
      value: 30.22948877331367
    - type: nauc_map_at_3_std
      value: 7.289154264399903
    - type: nauc_map_at_5_diff1
      value: 48.664130342694136
    - type: nauc_map_at_5_max
      value: 30.14327671294244
    - type: nauc_map_at_5_std
      value: 7.939333631753251
    - type: nauc_mrr_at_1000_diff1
      value: 44.58799837398294
    - type: nauc_mrr_at_1000_max
      value: 31.03541915705859
    - type: nauc_mrr_at_1000_std
      value: 10.403824515337941
    - type: nauc_mrr_at_100_diff1
      value: 44.601824537567715
    - type: nauc_mrr_at_100_max
      value: 31.02756566133194
    - type: nauc_mrr_at_100_std
      value: 10.374041246429492
    - type: nauc_mrr_at_10_diff1
      value: 45.08809081749144
    - type: nauc_mrr_at_10_max
      value: 31.57615351364963
    - type: nauc_mrr_at_10_std
      value: 10.29441865771061
    - type: nauc_mrr_at_1_diff1
      value: 53.78193049233505
    - type: nauc_mrr_at_1_max
      value: 35.795787308983364
    - type: nauc_mrr_at_1_std
      value: 9.700924818901061
    - type: nauc_mrr_at_20_diff1
      value: 44.74335182043816
    - type: nauc_mrr_at_20_max
      value: 31.18129900426782
    - type: nauc_mrr_at_20_std
      value: 10.385325054118825
    - type: nauc_mrr_at_3_diff1
      value: 46.73779708259278
    - type: nauc_mrr_at_3_max
      value: 32.65075209697959
    - type: nauc_mrr_at_3_std
      value: 9.728066031213869
    - type: nauc_mrr_at_5_diff1
      value: 45.92982408736637
    - type: nauc_mrr_at_5_max
      value: 32.467526279204826
    - type: nauc_mrr_at_5_std
      value: 9.989919602029717
    - type: nauc_ndcg_at_1000_diff1
      value: 40.92066479403982
    - type: nauc_ndcg_at_1000_max
      value: 26.324838581358712
    - type: nauc_ndcg_at_1000_std
      value: 11.523782722688093
    - type: nauc_ndcg_at_100_diff1
      value: 41.69901831802912
    - type: nauc_ndcg_at_100_max
      value: 26.05948550508969
    - type: nauc_ndcg_at_100_std
      value: 10.741879131890466
    - type: nauc_ndcg_at_10_diff1
      value: 43.984470289795006
    - type: nauc_ndcg_at_10_max
      value: 27.712165270383217
    - type: nauc_ndcg_at_10_std
      value: 9.664252780617716
    - type: nauc_ndcg_at_1_diff1
      value: 53.78193049233505
    - type: nauc_ndcg_at_1_max
      value: 35.795787308983364
    - type: nauc_ndcg_at_1_std
      value: 9.700924818901061
    - type: nauc_ndcg_at_20_diff1
      value: 42.87969088645589
    - type: nauc_ndcg_at_20_max
      value: 26.93508319676996
    - type: nauc_ndcg_at_20_std
      value: 10.383528785973736
    - type: nauc_ndcg_at_3_diff1
      value: 46.50711903290246
    - type: nauc_ndcg_at_3_max
      value: 30.119861670148136
    - type: nauc_ndcg_at_3_std
      value: 8.209698597192652
    - type: nauc_ndcg_at_5_diff1
      value: 45.5276661506903
    - type: nauc_ndcg_at_5_max
      value: 29.727216155363013
    - type: nauc_ndcg_at_5_std
      value: 8.969137019208551
    - type: nauc_precision_at_1000_diff1
      value: 13.186344514919291
    - type: nauc_precision_at_1000_max
      value: 14.081180493706894
    - type: nauc_precision_at_1000_std
      value: 13.331957277782028
    - type: nauc_precision_at_100_diff1
      value: 25.836947568988094
    - type: nauc_precision_at_100_max
      value: 19.399450264723857
    - type: nauc_precision_at_100_std
      value: 15.996979763079173
    - type: nauc_precision_at_10_diff1
      value: 31.611911937904136
    - type: nauc_precision_at_10_max
      value: 23.67106809118961
    - type: nauc_precision_at_10_std
      value: 12.494002491494403
    - type: nauc_precision_at_1_diff1
      value: 53.78193049233505
    - type: nauc_precision_at_1_max
      value: 35.795787308983364
    - type: nauc_precision_at_1_std
      value: 9.700924818901061
    - type: nauc_precision_at_20_diff1
      value: 28.52666886145722
    - type: nauc_precision_at_20_max
      value: 21.954240311035203
    - type: nauc_precision_at_20_std
      value: 14.844645388086807
    - type: nauc_precision_at_3_diff1
      value: 38.45498467923997
    - type: nauc_precision_at_3_max
      value: 29.266449529306882
    - type: nauc_precision_at_3_std
      value: 9.049210381929473
    - type: nauc_precision_at_5_diff1
      value: 36.09730656980118
    - type: nauc_precision_at_5_max
      value: 28.837127135797243
    - type: nauc_precision_at_5_std
      value: 11.158339114522931
    - type: nauc_recall_at_1000_diff1
      value: 21.260887713456125
    - type: nauc_recall_at_1000_max
      value: 16.113129212962036
    - type: nauc_recall_at_1000_std
      value: 18.480136835190926
    - type: nauc_recall_at_100_diff1
      value: 27.104482564680143
    - type: nauc_recall_at_100_max
      value: 15.992106261015381
    - type: nauc_recall_at_100_std
      value: 13.84189240491372
    - type: nauc_recall_at_10_diff1
      value: 35.07971219401454
    - type: nauc_recall_at_10_max
      value: 21.285398091407597
    - type: nauc_recall_at_10_std
      value: 11.2371939944325
    - type: nauc_recall_at_1_diff1
      value: 56.39452680423106
    - type: nauc_recall_at_1_max
      value: 32.60008414160042
    - type: nauc_recall_at_1_std
      value: 6.843961503288069
    - type: nauc_recall_at_20_diff1
      value: 32.39512106898805
    - type: nauc_recall_at_20_max
      value: 19.218626368924355
    - type: nauc_recall_at_20_std
      value: 12.883976865810729
    - type: nauc_recall_at_3_diff1
      value: 42.44181844531972
    - type: nauc_recall_at_3_max
      value: 26.878784537566723
    - type: nauc_recall_at_3_std
      value: 8.021682738108238
    - type: nauc_recall_at_5_diff1
      value: 39.71281577688504
    - type: nauc_recall_at_5_max
      value: 26.741868241320095
    - type: nauc_recall_at_5_std
      value: 9.776821004059626
    - type: ndcg_at_1
      value: 13.619
    - type: ndcg_at_10
      value: 16.884
    - type: ndcg_at_100
      value: 19.919999999999998
    - type: ndcg_at_1000
      value: 22.61
    - type: ndcg_at_20
      value: 17.802
    - type: ndcg_at_3
      value: 14.601
    - type: ndcg_at_5
      value: 15.47
    - type: precision_at_1
      value: 13.619
    - type: precision_at_10
      value: 2.8080000000000003
    - type: precision_at_100
      value: 0.485
    - type: precision_at_1000
      value: 0.08099999999999999
    - type: precision_at_20
      value: 1.66
    - type: precision_at_3
      value: 6.468
    - type: precision_at_5
      value: 4.496
    - type: recall_at_1
      value: 11.259
    - type: recall_at_10
      value: 22.148
    - type: recall_at_100
      value: 36.338
    - type: recall_at_1000
      value: 56.37
    - type: recall_at_20
      value: 25.444
    - type: recall_at_3
      value: 15.601
    - type: recall_at_5
      value: 17.904999999999998
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
      value: 18.986
    - type: map_at_1
      value: 11.219
    - type: map_at_10
      value: 15.572
    - type: map_at_100
      value: 16.496
    - type: map_at_1000
      value: 16.666
    - type: map_at_20
      value: 16.073999999999998
    - type: map_at_3
      value: 14.173
    - type: map_at_5
      value: 14.915000000000001
    - type: mrr_at_1
      value: 14.82213438735178
    - type: mrr_at_10
      value: 19.52365267582659
    - type: mrr_at_100
      value: 20.370290185635753
    - type: mrr_at_1000
      value: 20.467043542503724
    - type: mrr_at_20
      value: 20.0766545965337
    - type: mrr_at_3
      value: 18.21475625823452
    - type: mrr_at_5
      value: 18.945981554677203
    - type: nauc_map_at_1000_diff1
      value: 42.231943470301474
    - type: nauc_map_at_1000_max
      value: 26.47159454229298
    - type: nauc_map_at_1000_std
      value: 8.142899408562116
    - type: nauc_map_at_100_diff1
      value: 42.20734027834296
    - type: nauc_map_at_100_max
      value: 26.482392045352114
    - type: nauc_map_at_100_std
      value: 7.869302970334234
    - type: nauc_map_at_10_diff1
      value: 43.04836148095647
    - type: nauc_map_at_10_max
      value: 26.854456008820886
    - type: nauc_map_at_10_std
      value: 7.199117428761973
    - type: nauc_map_at_1_diff1
      value: 52.69584045825562
    - type: nauc_map_at_1_max
      value: 32.26169513753074
    - type: nauc_map_at_1_std
      value: 6.952498233745584
    - type: nauc_map_at_20_diff1
      value: 42.41625410983439
    - type: nauc_map_at_20_max
      value: 26.907750306130733
    - type: nauc_map_at_20_std
      value: 7.478967739706924
    - type: nauc_map_at_3_diff1
      value: 44.785788923058384
    - type: nauc_map_at_3_max
      value: 27.412957229850438
    - type: nauc_map_at_3_std
      value: 6.907258583517531
    - type: nauc_map_at_5_diff1
      value: 43.634053742171005
    - type: nauc_map_at_5_max
      value: 27.311414645244174
    - type: nauc_map_at_5_std
      value: 6.782368796408486
    - type: nauc_mrr_at_1000_diff1
      value: 40.121034147067355
    - type: nauc_mrr_at_1000_max
      value: 26.418816188019484
    - type: nauc_mrr_at_1000_std
      value: 11.036789931313589
    - type: nauc_mrr_at_100_diff1
      value: 40.09038771859193
    - type: nauc_mrr_at_100_max
      value: 26.35109915559335
    - type: nauc_mrr_at_100_std
      value: 11.004694419173386
    - type: nauc_mrr_at_10_diff1
      value: 40.70815905748883
    - type: nauc_mrr_at_10_max
      value: 26.39730116006313
    - type: nauc_mrr_at_10_std
      value: 10.795296410891202
    - type: nauc_mrr_at_1_diff1
      value: 49.49023740663914
    - type: nauc_mrr_at_1_max
      value: 32.80752877856241
    - type: nauc_mrr_at_1_std
      value: 9.182609293548452
    - type: nauc_mrr_at_20_diff1
      value: 40.09097766117321
    - type: nauc_mrr_at_20_max
      value: 26.543696500831608
    - type: nauc_mrr_at_20_std
      value: 11.045110550071236
    - type: nauc_mrr_at_3_diff1
      value: 42.547772290792786
    - type: nauc_mrr_at_3_max
      value: 27.248503683439974
    - type: nauc_mrr_at_3_std
      value: 11.12811144130018
    - type: nauc_mrr_at_5_diff1
      value: 41.182672458130945
    - type: nauc_mrr_at_5_max
      value: 27.204022967551346
    - type: nauc_mrr_at_5_std
      value: 10.736058227235059
    - type: nauc_ndcg_at_1000_diff1
      value: 38.283155226012525
    - type: nauc_ndcg_at_1000_max
      value: 23.952454186870728
    - type: nauc_ndcg_at_1000_std
      value: 11.202190633221258
    - type: nauc_ndcg_at_100_diff1
      value: 37.28326924063582
    - type: nauc_ndcg_at_100_max
      value: 23.059861557232345
    - type: nauc_ndcg_at_100_std
      value: 9.94550524440808
    - type: nauc_ndcg_at_10_diff1
      value: 39.63812221599438
    - type: nauc_ndcg_at_10_max
      value: 24.35015593369919
    - type: nauc_ndcg_at_10_std
      value: 9.315660164781054
    - type: nauc_ndcg_at_1_diff1
      value: 49.49023740663914
    - type: nauc_ndcg_at_1_max
      value: 32.80752877856241
    - type: nauc_ndcg_at_1_std
      value: 9.182609293548452
    - type: nauc_ndcg_at_20_diff1
      value: 37.63726489914318
    - type: nauc_ndcg_at_20_max
      value: 24.728684570593007
    - type: nauc_ndcg_at_20_std
      value: 9.986169134250208
    - type: nauc_ndcg_at_3_diff1
      value: 41.86142781421585
    - type: nauc_ndcg_at_3_max
      value: 25.373436332199645
    - type: nauc_ndcg_at_3_std
      value: 9.66682128586139
    - type: nauc_ndcg_at_5_diff1
      value: 40.642745287564594
    - type: nauc_ndcg_at_5_max
      value: 25.56873621658099
    - type: nauc_ndcg_at_5_std
      value: 9.25538178041856
    - type: nauc_precision_at_1000_diff1
      value: 11.480722649998393
    - type: nauc_precision_at_1000_max
      value: 1.8213948061833445
    - type: nauc_precision_at_1000_std
      value: 29.23515602956654
    - type: nauc_precision_at_100_diff1
      value: 14.18816101118032
    - type: nauc_precision_at_100_max
      value: 2.440318670740079
    - type: nauc_precision_at_100_std
      value: 29.24020499259622
    - type: nauc_precision_at_10_diff1
      value: 27.712287052106255
    - type: nauc_precision_at_10_max
      value: 16.786789482138776
    - type: nauc_precision_at_10_std
      value: 14.310510991471832
    - type: nauc_precision_at_1_diff1
      value: 49.49023740663914
    - type: nauc_precision_at_1_max
      value: 32.80752877856241
    - type: nauc_precision_at_1_std
      value: 9.182609293548452
    - type: nauc_precision_at_20_diff1
      value: 20.46872198920085
    - type: nauc_precision_at_20_max
      value: 14.825240542929851
    - type: nauc_precision_at_20_std
      value: 20.953665146043296
    - type: nauc_precision_at_3_diff1
      value: 36.03554983971536
    - type: nauc_precision_at_3_max
      value: 21.854122073954194
    - type: nauc_precision_at_3_std
      value: 13.04509621136731
    - type: nauc_precision_at_5_diff1
      value: 32.79763412951098
    - type: nauc_precision_at_5_max
      value: 21.11796990161242
    - type: nauc_precision_at_5_std
      value: 13.431327120495338
    - type: nauc_recall_at_1000_diff1
      value: 30.09802696990947
    - type: nauc_recall_at_1000_max
      value: 13.40584644567289
    - type: nauc_recall_at_1000_std
      value: 16.521370765894975
    - type: nauc_recall_at_100_diff1
      value: 26.309114191114602
    - type: nauc_recall_at_100_max
      value: 13.350873360428366
    - type: nauc_recall_at_100_std
      value: 11.078547445094047
    - type: nauc_recall_at_10_diff1
      value: 31.32014394352729
    - type: nauc_recall_at_10_max
      value: 18.345182060137695
    - type: nauc_recall_at_10_std
      value: 9.128692650287276
    - type: nauc_recall_at_1_diff1
      value: 52.69584045825562
    - type: nauc_recall_at_1_max
      value: 32.26169513753074
    - type: nauc_recall_at_1_std
      value: 6.952498233745584
    - type: nauc_recall_at_20_diff1
      value: 25.40389262415684
    - type: nauc_recall_at_20_max
      value: 19.21175870928344
    - type: nauc_recall_at_20_std
      value: 10.924171074066592
    - type: nauc_recall_at_3_diff1
      value: 38.07498529415478
    - type: nauc_recall_at_3_max
      value: 21.675031784523334
    - type: nauc_recall_at_3_std
      value: 7.885136540556627
    - type: nauc_recall_at_5_diff1
      value: 33.03739602855325
    - type: nauc_recall_at_5_max
      value: 20.891017025098222
    - type: nauc_recall_at_5_std
      value: 7.259719761129051
    - type: ndcg_at_1
      value: 14.822
    - type: ndcg_at_10
      value: 18.986
    - type: ndcg_at_100
      value: 22.996
    - type: ndcg_at_1000
      value: 26.569
    - type: ndcg_at_20
      value: 20.62
    - type: ndcg_at_3
      value: 16.778000000000002
    - type: ndcg_at_5
      value: 17.742
    - type: precision_at_1
      value: 14.822
    - type: precision_at_10
      value: 3.755
    - type: precision_at_100
      value: 0.8540000000000001
    - type: precision_at_1000
      value: 0.163
    - type: precision_at_20
      value: 2.4899999999999998
    - type: precision_at_3
      value: 8.235000000000001
    - type: precision_at_5
      value: 5.968
    - type: recall_at_1
      value: 11.219
    - type: recall_at_10
      value: 24.784
    - type: recall_at_100
      value: 43.143
    - type: recall_at_1000
      value: 68.416
    - type: recall_at_20
      value: 31.266
    - type: recall_at_3
      value: 17.607999999999997
    - type: recall_at_5
      value: 20.468
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
      value: 14.105
    - type: map_at_1
      value: 9.766
    - type: map_at_10
      value: 12.35
    - type: map_at_100
      value: 12.794
    - type: map_at_1000
      value: 12.876000000000001
    - type: map_at_20
      value: 12.548
    - type: map_at_3
      value: 11.583
    - type: map_at_5
      value: 11.855
    - type: mrr_at_1
      value: 10.35120147874307
    - type: mrr_at_10
      value: 13.323137634597895
    - type: mrr_at_100
      value: 13.8122389813538
    - type: mrr_at_1000
      value: 13.891191650266954
    - type: mrr_at_20
      value: 13.550088548700803
    - type: mrr_at_3
      value: 12.41528034504005
    - type: mrr_at_5
      value: 12.74799753542822
    - type: nauc_map_at_1000_diff1
      value: 30.214009272387493
    - type: nauc_map_at_1000_max
      value: 27.100911874185957
    - type: nauc_map_at_1000_std
      value: 4.556062715371813
    - type: nauc_map_at_100_diff1
      value: 30.283972909659536
    - type: nauc_map_at_100_max
      value: 27.101751795355376
    - type: nauc_map_at_100_std
      value: 4.530095632746722
    - type: nauc_map_at_10_diff1
      value: 30.703580851962275
    - type: nauc_map_at_10_max
      value: 27.45889128777842
    - type: nauc_map_at_10_std
      value: 4.056332236709348
    - type: nauc_map_at_1_diff1
      value: 38.44336021108366
    - type: nauc_map_at_1_max
      value: 31.341289082946698
    - type: nauc_map_at_1_std
      value: 5.249357458733503
    - type: nauc_map_at_20_diff1
      value: 30.50519884637743
    - type: nauc_map_at_20_max
      value: 27.340643104548395
    - type: nauc_map_at_20_std
      value: 4.165692308941953
    - type: nauc_map_at_3_diff1
      value: 32.38602261885505
    - type: nauc_map_at_3_max
      value: 28.903602549949543
    - type: nauc_map_at_3_std
      value: 3.5402281277974756
    - type: nauc_map_at_5_diff1
      value: 32.2685825283353
    - type: nauc_map_at_5_max
      value: 28.485087249150176
    - type: nauc_map_at_5_std
      value: 3.8418506057303445
    - type: nauc_mrr_at_1000_diff1
      value: 30.308168307291954
    - type: nauc_mrr_at_1000_max
      value: 26.895198553568438
    - type: nauc_mrr_at_1000_std
      value: 6.332711766194871
    - type: nauc_mrr_at_100_diff1
      value: 30.366219069831494
    - type: nauc_mrr_at_100_max
      value: 26.88024956005868
    - type: nauc_mrr_at_100_std
      value: 6.328345475093812
    - type: nauc_mrr_at_10_diff1
      value: 30.60181659497291
    - type: nauc_mrr_at_10_max
      value: 27.33947661988829
    - type: nauc_mrr_at_10_std
      value: 5.98212349517898
    - type: nauc_mrr_at_1_diff1
      value: 38.01665824488639
    - type: nauc_mrr_at_1_max
      value: 31.273295508014538
    - type: nauc_mrr_at_1_std
      value: 7.49596621052432
    - type: nauc_mrr_at_20_diff1
      value: 30.504642171833616
    - type: nauc_mrr_at_20_max
      value: 27.093254296264142
    - type: nauc_mrr_at_20_std
      value: 6.011940896215445
    - type: nauc_mrr_at_3_diff1
      value: 32.30298334779263
    - type: nauc_mrr_at_3_max
      value: 28.46795259170204
    - type: nauc_mrr_at_3_std
      value: 5.233276939737523
    - type: nauc_mrr_at_5_diff1
      value: 32.317520734292316
    - type: nauc_mrr_at_5_max
      value: 28.31645764893187
    - type: nauc_mrr_at_5_std
      value: 5.514394216402804
    - type: nauc_ndcg_at_1000_diff1
      value: 25.46804692303833
    - type: nauc_ndcg_at_1000_max
      value: 24.577578434016004
    - type: nauc_ndcg_at_1000_std
      value: 8.08099372903191
    - type: nauc_ndcg_at_100_diff1
      value: 25.7728600426837
    - type: nauc_ndcg_at_100_max
      value: 23.852719795214735
    - type: nauc_ndcg_at_100_std
      value: 7.271020641236757
    - type: nauc_ndcg_at_10_diff1
      value: 27.787864887098827
    - type: nauc_ndcg_at_10_max
      value: 25.82070997315848
    - type: nauc_ndcg_at_10_std
      value: 4.84958725429997
    - type: nauc_ndcg_at_1_diff1
      value: 38.01665824488639
    - type: nauc_ndcg_at_1_max
      value: 31.273295508014538
    - type: nauc_ndcg_at_1_std
      value: 7.49596621052432
    - type: nauc_ndcg_at_20_diff1
      value: 27.23687052702463
    - type: nauc_ndcg_at_20_max
      value: 25.3030643349024
    - type: nauc_ndcg_at_20_std
      value: 5.128184329356223
    - type: nauc_ndcg_at_3_diff1
      value: 30.94323024403614
    - type: nauc_ndcg_at_3_max
      value: 28.112791463025488
    - type: nauc_ndcg_at_3_std
      value: 3.4748257092667845
    - type: nauc_ndcg_at_5_diff1
      value: 30.979886062267525
    - type: nauc_ndcg_at_5_max
      value: 27.832062407091833
    - type: nauc_ndcg_at_5_std
      value: 4.066523891816962
    - type: nauc_precision_at_1000_diff1
      value: 13.717212581088436
    - type: nauc_precision_at_1000_max
      value: 14.726337919465527
    - type: nauc_precision_at_1000_std
      value: 19.286677279311952
    - type: nauc_precision_at_100_diff1
      value: 13.83440364507339
    - type: nauc_precision_at_100_max
      value: 13.983610901499812
    - type: nauc_precision_at_100_std
      value: 17.767107323199852
    - type: nauc_precision_at_10_diff1
      value: 18.989269379083463
    - type: nauc_precision_at_10_max
      value: 20.291510121396815
    - type: nauc_precision_at_10_std
      value: 8.518048232551553
    - type: nauc_precision_at_1_diff1
      value: 38.01665824488639
    - type: nauc_precision_at_1_max
      value: 31.273295508014538
    - type: nauc_precision_at_1_std
      value: 7.49596621052432
    - type: nauc_precision_at_20_diff1
      value: 18.381866045394073
    - type: nauc_precision_at_20_max
      value: 18.90966326296592
    - type: nauc_precision_at_20_std
      value: 9.141677018751377
    - type: nauc_precision_at_3_diff1
      value: 26.100613624838605
    - type: nauc_precision_at_3_max
      value: 24.76218487581011
    - type: nauc_precision_at_3_std
      value: 2.4322989886641495
    - type: nauc_precision_at_5_diff1
      value: 26.83172966704407
    - type: nauc_precision_at_5_max
      value: 24.090343452479146
    - type: nauc_precision_at_5_std
      value: 4.535854021501322
    - type: nauc_recall_at_1000_diff1
      value: 13.245456056842464
    - type: nauc_recall_at_1000_max
      value: 19.61498051994092
    - type: nauc_recall_at_1000_std
      value: 17.188990206491262
    - type: nauc_recall_at_100_diff1
      value: 14.025440613222711
    - type: nauc_recall_at_100_max
      value: 15.06663046965985
    - type: nauc_recall_at_100_std
      value: 12.610345211569749
    - type: nauc_recall_at_10_diff1
      value: 21.102550210495654
    - type: nauc_recall_at_10_max
      value: 21.76066577972798
    - type: nauc_recall_at_10_std
      value: 5.1852219341177115
    - type: nauc_recall_at_1_diff1
      value: 38.44336021108366
    - type: nauc_recall_at_1_max
      value: 31.341289082946698
    - type: nauc_recall_at_1_std
      value: 5.249357458733503
    - type: nauc_recall_at_20_diff1
      value: 19.281075192679307
    - type: nauc_recall_at_20_max
      value: 20.050580691482935
    - type: nauc_recall_at_20_std
      value: 5.836669306240979
    - type: nauc_recall_at_3_diff1
      value: 27.334543456325626
    - type: nauc_recall_at_3_max
      value: 26.711101790009558
    - type: nauc_recall_at_3_std
      value: 2.3329176939418037
    - type: nauc_recall_at_5_diff1
      value: 27.75488164284888
    - type: nauc_recall_at_5_max
      value: 26.285171746330576
    - type: nauc_recall_at_5_std
      value: 3.361376753158064
    - type: ndcg_at_1
      value: 10.351
    - type: ndcg_at_10
      value: 14.105
    - type: ndcg_at_100
      value: 16.765
    - type: ndcg_at_1000
      value: 19.220000000000002
    - type: ndcg_at_20
      value: 14.82
    - type: ndcg_at_3
      value: 12.398000000000001
    - type: ndcg_at_5
      value: 12.879999999999999
    - type: precision_at_1
      value: 10.351
    - type: precision_at_10
      value: 2.144
    - type: precision_at_100
      value: 0.373
    - type: precision_at_1000
      value: 0.062
    - type: precision_at_20
      value: 1.238
    - type: precision_at_3
      value: 5.114
    - type: precision_at_5
      value: 3.401
    - type: recall_at_1
      value: 9.766
    - type: recall_at_10
      value: 18.595
    - type: recall_at_100
      value: 31.669999999999998
    - type: recall_at_1000
      value: 50.659
    - type: recall_at_20
      value: 21.248
    - type: recall_at_3
      value: 13.876
    - type: recall_at_5
      value: 15.015
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CUADAffiliateLicenseLicenseeLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 73.73737373737373
    - type: ap
      value: 65.8818399825594
    - type: ap_weighted
      value: 65.8818399825594
    - type: f1
      value: 72.61993404956918
    - type: f1_weighted
      value: 72.61993404956918
    - type: main_score
      value: 73.73737373737373
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADAffiliateLicenseLicensorLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 79.54545454545453
    - type: ap
      value: 73.12252964426878
    - type: ap_weighted
      value: 73.12252964426878
    - type: f1
      value: 79.53488372093022
    - type: f1_weighted
      value: 79.53488372093024
    - type: main_score
      value: 79.54545454545453
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADAntiAssignmentLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 70.64846416382251
    - type: ap
      value: 63.215973012261415
    - type: ap_weighted
      value: 63.215973012261415
    - type: f1
      value: 68.89855743269304
    - type: f1_weighted
      value: 68.89855743269304
    - type: main_score
      value: 70.64846416382251
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADAuditRightsLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 60.44407894736842
    - type: ap
      value: 57.470171721677076
    - type: ap_weighted
      value: 57.470171721677076
    - type: f1
      value: 57.63732113071247
    - type: f1_weighted
      value: 57.63732113071247
    - type: main_score
      value: 60.44407894736842
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADCapOnLiabilityLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 49.518459069020864
    - type: ap
      value: 49.761431703402096
    - type: ap_weighted
      value: 49.761431703402096
    - type: f1
      value: 49.48302433823829
    - type: f1_weighted
      value: 49.48302433823827
    - type: main_score
      value: 49.518459069020864
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADChangeOfControlLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 71.875
    - type: ap
      value: 64.42982456140352
    - type: ap_weighted
      value: 64.42982456140352
    - type: f1
      value: 70.87723707120934
    - type: f1_weighted
      value: 70.8772370712093
    - type: main_score
      value: 71.875
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADCompetitiveRestrictionExceptionLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 53.181818181818194
    - type: ap
      value: 51.65110565110565
    - type: ap_weighted
      value: 51.65110565110565
    - type: f1
      value: 47.02513150204559
    - type: f1_weighted
      value: 47.025131502045596
    - type: main_score
      value: 53.181818181818194
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADCovenantNotToSueLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 67.53246753246754
    - type: ap
      value: 60.65974025974026
    - type: ap_weighted
      value: 60.65974025974026
    - type: f1
      value: 64.03885671586028
    - type: f1_weighted
      value: 64.03885671586026
    - type: main_score
      value: 67.53246753246754
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADEffectiveDateLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 56.35593220338983
    - type: ap
      value: 53.54749704375246
    - type: ap_weighted
      value: 53.54749704375246
    - type: f1
      value: 56.26090868196132
    - type: f1_weighted
      value: 56.26090868196131
    - type: main_score
      value: 56.35593220338983
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADExclusivityLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 61.154855643044606
    - type: ap
      value: 56.35333840225783
    - type: ap_weighted
      value: 56.35333840225783
    - type: f1
      value: 57.26109628910987
    - type: f1_weighted
      value: 57.26109628910987
    - type: main_score
      value: 61.154855643044606
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADExpirationDateLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 80.82191780821917
    - type: ap
      value: 77.03374913905259
    - type: ap_weighted
      value: 77.03374913905259
    - type: f1
      value: 80.66062530224343
    - type: f1_weighted
      value: 80.66062530224343
    - type: main_score
      value: 80.82191780821917
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADGoverningLawLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 92.12328767123289
    - type: ap
      value: 88.44810149857499
    - type: ap_weighted
      value: 88.44810149857499
    - type: f1
      value: 92.12245616092896
    - type: f1_weighted
      value: 92.12245616092899
    - type: main_score
      value: 92.12328767123289
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADIPOwnershipAssignmentLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 64.0625
    - type: ap
      value: 59.78260869565217
    - type: ap_weighted
      value: 59.78260869565217
    - type: f1
      value: 63.33748443337483
    - type: f1_weighted
      value: 63.33748443337485
    - type: main_score
      value: 64.0625
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADInsuranceLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 80.3883495145631
    - type: ap
      value: 76.65387764650838
    - type: ap_weighted
      value: 76.65387764650838
    - type: f1
      value: 80.20173184889143
    - type: f1_weighted
      value: 80.20173184889143
    - type: main_score
      value: 80.3883495145631
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADIrrevocableOrPerpetualLicenseLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 78.21428571428572
    - type: ap
      value: 70.19711163153788
    - type: ap_weighted
      value: 70.19711163153788
    - type: f1
      value: 77.68807722955938
    - type: f1_weighted
      value: 77.6880772295594
    - type: main_score
      value: 78.21428571428572
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADJointIPOwnershipLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 85.9375
    - type: ap
      value: 79.55607476635514
    - type: ap_weighted
      value: 79.55607476635514
    - type: f1
      value: 85.89119015866969
    - type: f1_weighted
      value: 85.89119015866969
    - type: main_score
      value: 85.9375
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADLicenseGrantLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 72.56446991404013
    - type: ap
      value: 65.06701026209069
    - type: ap_weighted
      value: 65.06701026209069
    - type: f1
      value: 71.72168495320604
    - type: f1_weighted
      value: 71.72168495320604
    - type: main_score
      value: 72.56446991404013
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADLiquidatedDamagesLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 80.45454545454544
    - type: ap
      value: 73.2605583392985
    - type: ap_weighted
      value: 73.2605583392985
    - type: f1
      value: 80.33713703726801
    - type: f1_weighted
      value: 80.33713703726798
    - type: main_score
      value: 80.45454545454544
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADMinimumCommitmentLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 75.51813471502591
    - type: ap
      value: 68.84511159342107
    - type: ap_weighted
      value: 68.84511159342107
    - type: f1
      value: 75.48815213647933
    - type: f1_weighted
      value: 75.48815213647931
    - type: main_score
      value: 75.51813471502591
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADMostFavoredNationLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 73.4375
    - type: ap
      value: 65.80668604651162
    - type: ap_weighted
      value: 65.80668604651162
    - type: f1
      value: 72.62893081761007
    - type: f1_weighted
      value: 72.62893081761007
    - type: main_score
      value: 73.4375
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADNoSolicitOfCustomersLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 82.14285714285714
    - type: ap
      value: 73.68421052631578
    - type: ap_weighted
      value: 73.68421052631578
    - type: f1
      value: 81.55467720685114
    - type: f1_weighted
      value: 81.55467720685111
    - type: main_score
      value: 82.14285714285714
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADNoSolicitOfEmployeesLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 88.02816901408453
    - type: ap
      value: 81.23742454728371
    - type: ap_weighted
      value: 81.23742454728371
    - type: f1
      value: 87.92698174543636
    - type: f1_weighted
      value: 87.92698174543636
    - type: main_score
      value: 88.02816901408453
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADNonCompeteLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 53.84615384615385
    - type: ap
      value: 52.05651491365778
    - type: ap_weighted
      value: 52.05651491365778
    - type: f1
      value: 53.70967410723452
    - type: f1_weighted
      value: 53.70967410723452
    - type: main_score
      value: 53.84615384615385
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADNonDisparagementLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 82.0
    - type: ap
      value: 73.75757575757575
    - type: ap_weighted
      value: 73.75757575757575
    - type: f1
      value: 81.5270935960591
    - type: f1_weighted
      value: 81.5270935960591
    - type: main_score
      value: 82.0
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADNonTransferableLicenseLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 72.69372693726936
    - type: ap
      value: 68.36025144171039
    - type: ap_weighted
      value: 68.36025144171039
    - type: f1
      value: 72.20320188509251
    - type: f1_weighted
      value: 72.20320188509251
    - type: main_score
      value: 72.69372693726936
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADNoticePeriodToTerminateRenewalLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 81.53153153153154
    - type: ap
      value: 73.22254687119553
    - type: ap_weighted
      value: 73.22254687119553
    - type: f1
      value: 81.003861003861
    - type: f1_weighted
      value: 81.003861003861
    - type: main_score
      value: 81.53153153153154
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADPostTerminationServicesLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 59.52970297029702
    - type: ap
      value: 55.494262149873045
    - type: ap_weighted
      value: 55.494262149873045
    - type: f1
      value: 58.91289033889372
    - type: f1_weighted
      value: 58.91289033889372
    - type: main_score
      value: 59.52970297029702
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADPriceRestrictionsLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 86.95652173913044
    - type: ap
      value: 80.11272141706925
    - type: ap_weighted
      value: 80.11272141706925
    - type: f1
      value: 86.85714285714286
    - type: f1_weighted
      value: 86.85714285714286
    - type: main_score
      value: 86.95652173913044
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADRenewalTermLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 81.86528497409327
    - type: ap
      value: 74.56574832804549
    - type: ap_weighted
      value: 74.56574832804549
    - type: f1
      value: 81.72348484848484
    - type: f1_weighted
      value: 81.72348484848484
    - type: main_score
      value: 81.86528497409327
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADRevenueProfitSharingLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 78.9405684754522
    - type: ap
      value: 75.88346617170725
    - type: ap_weighted
      value: 75.88346617170725
    - type: f1
      value: 78.5609048595758
    - type: f1_weighted
      value: 78.5609048595758
    - type: main_score
      value: 78.9405684754522
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADRofrRofoRofnLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 67.53623188405797
    - type: ap
      value: 61.059567408520365
    - type: ap_weighted
      value: 61.059567408520365
    - type: f1
      value: 66.55819428096656
    - type: f1_weighted
      value: 66.55819428096656
    - type: main_score
      value: 67.53623188405797
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADSourceCodeEscrowLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 79.66101694915253
    - type: ap
      value: 73.06967984934086
    - type: ap_weighted
      value: 73.06967984934086
    - type: f1
      value: 79.63761863675583
    - type: f1_weighted
      value: 79.63761863675583
    - type: main_score
      value: 79.66101694915253
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADTerminationForConvenienceLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 82.55813953488372
    - type: ap
      value: 76.9289284938057
    - type: ap_weighted
      value: 76.9289284938057
    - type: f1
      value: 82.5580452030568
    - type: f1_weighted
      value: 82.55804520305684
    - type: main_score
      value: 82.55813953488372
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADThirdPartyBeneficiaryLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 86.76470588235293
    - type: ap
      value: 82.30837789661318
    - type: ap_weighted
      value: 82.30837789661318
    - type: f1
      value: 86.76184295911746
    - type: f1_weighted
      value: 86.76184295911744
    - type: main_score
      value: 86.76470588235293
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADUncappedLiabilityLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 78.91156462585033
    - type: ap
      value: 70.63036269784295
    - type: ap_weighted
      value: 70.63036269784295
    - type: f1
      value: 78.23054507237377
    - type: f1_weighted
      value: 78.23054507237376
    - type: main_score
      value: 78.91156462585033
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADUnlimitedAllYouCanEatLicenseLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 75.0
    - type: ap
      value: 67.5
    - type: ap_weighted
      value: 67.5
    - type: f1
      value: 74.60317460317461
    - type: f1_weighted
      value: 74.60317460317461
    - type: main_score
      value: 75.0
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADVolumeRestrictionLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 68.32298136645963
    - type: ap
      value: 67.47730530339226
    - type: ap_weighted
      value: 67.47730530339226
    - type: f1
      value: 65.23267138078504
    - type: f1_weighted
      value: 65.23267138078504
    - type: main_score
      value: 68.32298136645963
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CUADWarrantyDurationLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 77.18749999999999
    - type: ap
      value: 70.84930981595093
    - type: ap_weighted
      value: 70.84930981595093
    - type: f1
      value: 77.18549481888057
    - type: f1_weighted
      value: 77.18549481888057
    - type: main_score
      value: 77.18749999999999
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CanadaTaxCourtOutcomesLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 45.90163934426229
    - type: f1
      value: 41.86755057433674
    - type: f1_weighted
      value: 52.49140373560517
    - type: main_score
      value: 45.90163934426229
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ClimateFEVER (default)
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
      split: test
      type: mteb/climate-fever
    metrics:
    - type: main_score
      value: 5.558
    - type: map_at_1
      value: 2.099
    - type: map_at_10
      value: 3.6790000000000003
    - type: map_at_100
      value: 4.021
    - type: map_at_1000
      value: 4.083
    - type: map_at_20
      value: 3.843
    - type: map_at_3
      value: 3.107
    - type: map_at_5
      value: 3.398
    - type: mrr_at_1
      value: 4.364820846905538
    - type: mrr_at_10
      value: 7.478723954293985
    - type: mrr_at_100
      value: 8.041420875649584
    - type: mrr_at_1000
      value: 8.120754871238086
    - type: mrr_at_20
      value: 7.760020669319687
    - type: mrr_at_3
      value: 6.438653637350702
    - type: mrr_at_5
      value: 7.028230184581975
    - type: nauc_map_at_1000_diff1
      value: 26.989583880363355
    - type: nauc_map_at_1000_max
      value: 19.651932768180743
    - type: nauc_map_at_1000_std
      value: 28.682949493303113
    - type: nauc_map_at_100_diff1
      value: 27.123176019982058
    - type: nauc_map_at_100_max
      value: 19.598769909181605
    - type: nauc_map_at_100_std
      value: 28.431702256094276
    - type: nauc_map_at_10_diff1
      value: 28.090105463174243
    - type: nauc_map_at_10_max
      value: 19.316825624764327
    - type: nauc_map_at_10_std
      value: 27.879940536760657
    - type: nauc_map_at_1_diff1
      value: 38.86635884960338
    - type: nauc_map_at_1_max
      value: 23.66935741341746
    - type: nauc_map_at_1_std
      value: 25.594810836643088
    - type: nauc_map_at_20_diff1
      value: 27.932097656688153
    - type: nauc_map_at_20_max
      value: 19.705436224378094
    - type: nauc_map_at_20_std
      value: 28.005161889024915
    - type: nauc_map_at_3_diff1
      value: 31.343508506514787
    - type: nauc_map_at_3_max
      value: 17.617676175693653
    - type: nauc_map_at_3_std
      value: 27.372138781240235
    - type: nauc_map_at_5_diff1
      value: 29.21950281006726
    - type: nauc_map_at_5_max
      value: 18.039174755804527
    - type: nauc_map_at_5_std
      value: 26.278075304640147
    - type: nauc_mrr_at_1000_diff1
      value: 21.017635057347793
    - type: nauc_mrr_at_1000_max
      value: 20.84007387790555
    - type: nauc_mrr_at_1000_std
      value: 24.684523933084744
    - type: nauc_mrr_at_100_diff1
      value: 21.051698171004
    - type: nauc_mrr_at_100_max
      value: 20.79459868740917
    - type: nauc_mrr_at_100_std
      value: 24.62077347403019
    - type: nauc_mrr_at_10_diff1
      value: 21.926692626233184
    - type: nauc_mrr_at_10_max
      value: 20.868215747512338
    - type: nauc_mrr_at_10_std
      value: 24.10229968572614
    - type: nauc_mrr_at_1_diff1
      value: 32.12007148649377
    - type: nauc_mrr_at_1_max
      value: 25.428643110489634
    - type: nauc_mrr_at_1_std
      value: 19.946229629460547
    - type: nauc_mrr_at_20_diff1
      value: 21.617935715645125
    - type: nauc_mrr_at_20_max
      value: 21.046484288936377
    - type: nauc_mrr_at_20_std
      value: 24.297367370651244
    - type: nauc_mrr_at_3_diff1
      value: 24.094623370861303
    - type: nauc_mrr_at_3_max
      value: 19.713811945549196
    - type: nauc_mrr_at_3_std
      value: 23.568839477173757
    - type: nauc_mrr_at_5_diff1
      value: 22.3010395396166
    - type: nauc_mrr_at_5_max
      value: 20.569180907488864
    - type: nauc_mrr_at_5_std
      value: 23.15568498862624
    - type: nauc_ndcg_at_1000_diff1
      value: 17.73440786298746
    - type: nauc_ndcg_at_1000_max
      value: 21.164734898511266
    - type: nauc_ndcg_at_1000_std
      value: 32.20409116224434
    - type: nauc_ndcg_at_100_diff1
      value: 19.491657641927414
    - type: nauc_ndcg_at_100_max
      value: 19.73425182329514
    - type: nauc_ndcg_at_100_std
      value: 29.633697891721162
    - type: nauc_ndcg_at_10_diff1
      value: 23.236666416810397
    - type: nauc_ndcg_at_10_max
      value: 19.859686062177957
    - type: nauc_ndcg_at_10_std
      value: 27.607123060751103
    - type: nauc_ndcg_at_1_diff1
      value: 32.12007148649377
    - type: nauc_ndcg_at_1_max
      value: 25.428643110489634
    - type: nauc_ndcg_at_1_std
      value: 19.946229629460547
    - type: nauc_ndcg_at_20_diff1
      value: 22.766492789770794
    - type: nauc_ndcg_at_20_max
      value: 20.68653243447615
    - type: nauc_ndcg_at_20_std
      value: 27.80598558578259
    - type: nauc_ndcg_at_3_diff1
      value: 26.430176145767764
    - type: nauc_ndcg_at_3_max
      value: 17.178786585572514
    - type: nauc_ndcg_at_3_std
      value: 26.551392559385945
    - type: nauc_ndcg_at_5_diff1
      value: 24.359838503352492
    - type: nauc_ndcg_at_5_max
      value: 18.139249994062958
    - type: nauc_ndcg_at_5_std
      value: 25.04579441208386
    - type: nauc_precision_at_1000_diff1
      value: 3.5941753705590855
    - type: nauc_precision_at_1000_max
      value: 23.295418071068074
    - type: nauc_precision_at_1000_std
      value: 37.823737794558035
    - type: nauc_precision_at_100_diff1
      value: 7.711362755764835
    - type: nauc_precision_at_100_max
      value: 21.000892665907962
    - type: nauc_precision_at_100_std
      value: 35.56596455340648
    - type: nauc_precision_at_10_diff1
      value: 14.603402002580449
    - type: nauc_precision_at_10_max
      value: 22.112935744796918
    - type: nauc_precision_at_10_std
      value: 30.665912790934176
    - type: nauc_precision_at_1_diff1
      value: 32.12007148649377
    - type: nauc_precision_at_1_max
      value: 25.428643110489634
    - type: nauc_precision_at_1_std
      value: 19.946229629460547
    - type: nauc_precision_at_20_diff1
      value: 14.716417574100266
    - type: nauc_precision_at_20_max
      value: 23.926389785704096
    - type: nauc_precision_at_20_std
      value: 30.69168946837732
    - type: nauc_precision_at_3_diff1
      value: 18.67632522519008
    - type: nauc_precision_at_3_max
      value: 15.461714107477059
    - type: nauc_precision_at_3_std
      value: 24.408621037612654
    - type: nauc_precision_at_5_diff1
      value: 14.433484685750017
    - type: nauc_precision_at_5_max
      value: 18.682282289432337
    - type: nauc_precision_at_5_std
      value: 24.03615092175192
    - type: nauc_recall_at_1000_diff1
      value: 7.5569286948470955
    - type: nauc_recall_at_1000_max
      value: 18.988365246129565
    - type: nauc_recall_at_1000_std
      value: 32.73921563811838
    - type: nauc_recall_at_100_diff1
      value: 12.11778715469688
    - type: nauc_recall_at_100_max
      value: 16.608390547005357
    - type: nauc_recall_at_100_std
      value: 29.88269190630321
    - type: nauc_recall_at_10_diff1
      value: 20.008263704255814
    - type: nauc_recall_at_10_max
      value: 19.07669508851797
    - type: nauc_recall_at_10_std
      value: 28.95827325426037
    - type: nauc_recall_at_1_diff1
      value: 38.86635884960338
    - type: nauc_recall_at_1_max
      value: 23.66935741341746
    - type: nauc_recall_at_1_std
      value: 25.594810836643088
    - type: nauc_recall_at_20_diff1
      value: 19.54693652826011
    - type: nauc_recall_at_20_max
      value: 20.582517703572815
    - type: nauc_recall_at_20_std
      value: 28.52204311008764
    - type: nauc_recall_at_3_diff1
      value: 25.95757457673112
    - type: nauc_recall_at_3_max
      value: 13.802011828871594
    - type: nauc_recall_at_3_std
      value: 28.160988060479163
    - type: nauc_recall_at_5_diff1
      value: 21.718874199874673
    - type: nauc_recall_at_5_max
      value: 15.812170162395233
    - type: nauc_recall_at_5_std
      value: 24.970427791223297
    - type: ndcg_at_1
      value: 4.365
    - type: ndcg_at_10
      value: 5.558
    - type: ndcg_at_100
      value: 7.637
    - type: ndcg_at_1000
      value: 9.700000000000001
    - type: ndcg_at_20
      value: 6.215
    - type: ndcg_at_3
      value: 4.314
    - type: ndcg_at_5
      value: 4.795
    - type: precision_at_1
      value: 4.365
    - type: precision_at_10
      value: 1.6740000000000002
    - type: precision_at_100
      value: 0.384
    - type: precision_at_1000
      value: 0.076
    - type: precision_at_20
      value: 1.111
    - type: precision_at_3
      value: 3.084
    - type: precision_at_5
      value: 2.423
    - type: recall_at_1
      value: 2.099
    - type: recall_at_10
      value: 7.371999999999999
    - type: recall_at_100
      value: 14.976999999999999
    - type: recall_at_1000
      value: 27.328000000000003
    - type: recall_at_20
      value: 9.288
    - type: recall_at_3
      value: 4.299
    - type: recall_at_5
      value: 5.509
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ContractNLIConfidentialityOfAgreementLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 64.63414634146342
    - type: ap
      value: 59.62772785622593
    - type: ap_weighted
      value: 59.62772785622593
    - type: f1
      value: 64.58674609084142
    - type: f1_weighted
      value: 64.58674609084142
    - type: main_score
      value: 64.63414634146342
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLIExplicitIdentificationLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 56.88073394495412
    - type: ap
      value: 21.457096600107935
    - type: ap_weighted
      value: 21.457096600107935
    - type: f1
      value: 50.91501389288109
    - type: f1_weighted
      value: 61.74750556638211
    - type: main_score
      value: 56.88073394495412
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLIInclusionOfVerballyConveyedInformationLegalBenchClassification
        (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 60.431654676258994
    - type: ap
      value: 55.25139990309542
    - type: ap_weighted
      value: 55.25139990309542
    - type: f1
      value: 60.4234611999793
    - type: f1_weighted
      value: 60.435751414398844
    - type: main_score
      value: 60.431654676258994
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLILimitedUseLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 73.07692307692307
    - type: ap
      value: 63.954526895988565
    - type: ap_weighted
      value: 63.954526895988565
    - type: f1
      value: 73.01454916133815
    - type: f1_weighted
      value: 73.10187264315704
    - type: main_score
      value: 73.07692307692307
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLINoLicensingLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 82.09876543209876
    - type: ap
      value: 75.19529587058324
    - type: ap_weighted
      value: 75.19529587058324
    - type: f1
      value: 82.08169647965215
    - type: f1_weighted
      value: 82.0748688986735
    - type: main_score
      value: 82.09876543209876
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLINoticeOnCompelledDisclosureLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 78.87323943661971
    - type: ap
      value: 72.12365099689045
    - type: ap_weighted
      value: 72.12365099689045
    - type: f1
      value: 78.83545310015897
    - type: f1_weighted
      value: 78.83545310015897
    - type: main_score
      value: 78.87323943661971
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLIPermissibleAcquirementOfSimilarInformationLegalBenchClassification
        (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 72.47191011235954
    - type: ap
      value: 64.74719101123597
    - type: ap_weighted
      value: 64.74719101123597
    - type: f1
      value: 71.08377813877931
    - type: f1_weighted
      value: 71.08377813877931
    - type: main_score
      value: 72.47191011235954
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLIPermissibleCopyLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 41.379310344827594
    - type: ap
      value: 19.168356997971607
    - type: ap_weighted
      value: 19.168356997971607
    - type: f1
      value: 38.75776397515528
    - type: f1_weighted
      value: 46.18547868922682
    - type: main_score
      value: 41.379310344827594
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLIPermissibleDevelopmentOfSimilarInformationLegalBenchClassification
        (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 71.3235294117647
    - type: ap
      value: 65.14279624893436
    - type: ap_weighted
      value: 65.14279624893436
    - type: f1
      value: 71.3219789132198
    - type: f1_weighted
      value: 71.3219789132198
    - type: main_score
      value: 71.3235294117647
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLIPermissiblePostAgreementPossessionLegalBenchClassification
        (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 39.63963963963964
    - type: ap
      value: 25.290389847351868
    - type: ap_weighted
      value: 25.290389847351868
    - type: f1
      value: 39.56115400243804
    - type: f1_weighted
      value: 40.64033151396011
    - type: main_score
      value: 39.63963963963964
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLIReturnOfConfidentialInformationLegalBenchClassification
        (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 71.21212121212122
    - type: ap
      value: 63.13978196600149
    - type: ap_weighted
      value: 63.13978196600149
    - type: f1
      value: 70.88460645460877
    - type: f1_weighted
      value: 70.7910308096052
    - type: main_score
      value: 71.21212121212122
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLISharingWithEmployeesLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 73.52941176470588
    - type: ap
      value: 66.24576478752499
    - type: ap_weighted
      value: 66.24576478752499
    - type: f1
      value: 71.13098607494621
    - type: f1_weighted
      value: 71.42467085328414
    - type: main_score
      value: 73.52941176470588
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLISharingWithThirdPartiesLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 68.88888888888889
    - type: ap
      value: 51.569719636083924
    - type: ap_weighted
      value: 51.569719636083924
    - type: f1
      value: 66.28762541806019
    - type: f1_weighted
      value: 68.26458565589
    - type: main_score
      value: 68.88888888888889
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ContractNLISurvivalOfObligationsLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 49.044585987261144
    - type: ap
      value: 47.085151843488305
    - type: ap_weighted
      value: 47.085151843488305
    - type: f1
      value: 48.28722002635046
    - type: f1_weighted
      value: 47.92846772907698
    - type: main_score
      value: 49.044585987261144
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CorporateLobbyingLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 70.40816326530613
    - type: ap
      value: 29.59183673469388
    - type: ap_weighted
      value: 29.59183673469388
    - type: f1
      value: 41.31736526946107
    - type: f1_weighted
      value: 58.181595991690074
    - type: main_score
      value: 70.40816326530613
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CyrillicTurkicLangClassification (default)
      revision: e42d330f33d65b7b72dfd408883daf1661f06f18
      split: test
      type: tatiana-merz/cyrillic_turkic_langs
    metrics:
    - type: accuracy
      value: 61.19140625
    - type: f1
      value: 59.377085898563365
    - type: f1_weighted
      value: 59.385881195883925
    - type: main_score
      value: 61.19140625
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB DBPedia (default)
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: dev
      type: mteb/dbpedia
    metrics:
    - type: main_score
      value: 7.161
    - type: map_at_1
      value: 0.599
    - type: map_at_10
      value: 2.243
    - type: map_at_100
      value: 3.1189999999999998
    - type: map_at_1000
      value: 3.488
    - type: map_at_20
      value: 2.522
    - type: map_at_3
      value: 1.397
    - type: map_at_5
      value: 1.951
    - type: mrr_at_1
      value: 8.955223880597014
    - type: mrr_at_10
      value: 18.287728026533994
    - type: mrr_at_100
      value: 18.978113584928742
    - type: mrr_at_1000
      value: 19.053758841865573
    - type: mrr_at_20
      value: 18.61199952617863
    - type: mrr_at_3
      value: 14.676616915422885
    - type: mrr_at_5
      value: 17.06467661691542
    - type: nauc_map_at_1000_diff1
      value: -2.930033724497058
    - type: nauc_map_at_1000_max
      value: 3.5995430754716904
    - type: nauc_map_at_1000_std
      value: 5.61203479120595
    - type: nauc_map_at_100_diff1
      value: -5.4531441891668795
    - type: nauc_map_at_100_max
      value: -0.0055832626529105185
    - type: nauc_map_at_100_std
      value: 3.439773391163607
    - type: nauc_map_at_10_diff1
      value: -14.3319757103363
    - type: nauc_map_at_10_max
      value: -9.021024411612359
    - type: nauc_map_at_10_std
      value: 1.0275253768638628
    - type: nauc_map_at_1_diff1
      value: 22.607506151253776
    - type: nauc_map_at_1_max
      value: 10.921408762597743
    - type: nauc_map_at_1_std
      value: -2.0177080867009054
    - type: nauc_map_at_20_diff1
      value: -11.794157692538237
    - type: nauc_map_at_20_max
      value: -6.44484538876576
    - type: nauc_map_at_20_std
      value: 1.039851694368717
    - type: nauc_map_at_3_diff1
      value: -7.469347804676409
    - type: nauc_map_at_3_max
      value: -5.393936026725367
    - type: nauc_map_at_3_std
      value: 9.280689460783249
    - type: nauc_map_at_5_diff1
      value: -15.955321054747321
    - type: nauc_map_at_5_max
      value: -9.855092671604572
    - type: nauc_map_at_5_std
      value: 0.06180279408320787
    - type: nauc_mrr_at_1000_diff1
      value: -2.821396337906413
    - type: nauc_mrr_at_1000_max
      value: 5.972877383405757
    - type: nauc_mrr_at_1000_std
      value: -1.6896049835004336
    - type: nauc_mrr_at_100_diff1
      value: -2.8632536639982105
    - type: nauc_mrr_at_100_max
      value: 5.973020236396294
    - type: nauc_mrr_at_100_std
      value: -1.809958349128643
    - type: nauc_mrr_at_10_diff1
      value: -4.515463799529893
    - type: nauc_mrr_at_10_max
      value: 5.030384515417533
    - type: nauc_mrr_at_10_std
      value: -1.547480529694615
    - type: nauc_mrr_at_1_diff1
      value: 8.719512377821816
    - type: nauc_mrr_at_1_max
      value: 16.272382792823382
    - type: nauc_mrr_at_1_std
      value: -3.187491782487964
    - type: nauc_mrr_at_20_diff1
      value: -2.908929872190089
    - type: nauc_mrr_at_20_max
      value: 6.58409584409903
    - type: nauc_mrr_at_20_std
      value: -1.1174417761572792
    - type: nauc_mrr_at_3_diff1
      value: -1.6595580931793985
    - type: nauc_mrr_at_3_max
      value: 9.640215787928428
    - type: nauc_mrr_at_3_std
      value: 2.889288978742377
    - type: nauc_mrr_at_5_diff1
      value: -6.89298539225687
    - type: nauc_mrr_at_5_max
      value: 6.578043390443974
    - type: nauc_mrr_at_5_std
      value: -0.6581933130437475
    - type: nauc_ndcg_at_1000_diff1
      value: 3.75625342513744
    - type: nauc_ndcg_at_1000_max
      value: 6.952585708583143
    - type: nauc_ndcg_at_1000_std
      value: 5.400684775811628
    - type: nauc_ndcg_at_100_diff1
      value: -2.242186789473446
    - type: nauc_ndcg_at_100_max
      value: 1.7125259047701242
    - type: nauc_ndcg_at_100_std
      value: -0.6824733710981048
    - type: nauc_ndcg_at_10_diff1
      value: -11.969827974466098
    - type: nauc_ndcg_at_10_max
      value: -4.424965429405649
    - type: nauc_ndcg_at_10_std
      value: 0.03592313276976773
    - type: nauc_ndcg_at_1_diff1
      value: -4.197220327746547
    - type: nauc_ndcg_at_1_max
      value: 9.247135683163954
    - type: nauc_ndcg_at_1_std
      value: -6.671985136155276
    - type: nauc_ndcg_at_20_diff1
      value: -8.358422632396593
    - type: nauc_ndcg_at_20_max
      value: -1.0551974757194074
    - type: nauc_ndcg_at_20_std
      value: 2.0508581550409524
    - type: nauc_ndcg_at_3_diff1
      value: -7.53212458402589
    - type: nauc_ndcg_at_3_max
      value: 3.6347588818172336
    - type: nauc_ndcg_at_3_std
      value: 5.073680163820697
    - type: nauc_ndcg_at_5_diff1
      value: -17.183713921651613
    - type: nauc_ndcg_at_5_max
      value: -2.598662858319381
    - type: nauc_ndcg_at_5_std
      value: -0.4734708395726036
    - type: nauc_precision_at_1000_diff1
      value: 22.034829237918075
    - type: nauc_precision_at_1000_max
      value: 29.133045600628414
    - type: nauc_precision_at_1000_std
      value: 22.48207630228867
    - type: nauc_precision_at_100_diff1
      value: 22.17246050117164
    - type: nauc_precision_at_100_max
      value: 25.497860199414003
    - type: nauc_precision_at_100_std
      value: 14.10941839109608
    - type: nauc_precision_at_10_diff1
      value: -2.3976462009254527
    - type: nauc_precision_at_10_max
      value: 3.2185747947259737
    - type: nauc_precision_at_10_std
      value: 1.1160090019272848
    - type: nauc_precision_at_1_diff1
      value: 8.719512377821816
    - type: nauc_precision_at_1_max
      value: 16.272382792823382
    - type: nauc_precision_at_1_std
      value: -3.187491782487964
    - type: nauc_precision_at_20_diff1
      value: 8.125877087406765
    - type: nauc_precision_at_20_max
      value: 14.004634012058606
    - type: nauc_precision_at_20_std
      value: 6.076987698320296
    - type: nauc_precision_at_3_diff1
      value: -5.415944490965941
    - type: nauc_precision_at_3_max
      value: 6.0110244505222
    - type: nauc_precision_at_3_std
      value: 6.0205421596952675
    - type: nauc_precision_at_5_diff1
      value: -19.55829195099795
    - type: nauc_precision_at_5_max
      value: -2.3847548504000993
    - type: nauc_precision_at_5_std
      value: -4.296125770063572
    - type: nauc_recall_at_1000_diff1
      value: 5.793923275597914
    - type: nauc_recall_at_1000_max
      value: 2.365078190964481
    - type: nauc_recall_at_1000_std
      value: 3.5546888704254744
    - type: nauc_recall_at_100_diff1
      value: 1.652314810086157
    - type: nauc_recall_at_100_max
      value: 1.2466358966197024
    - type: nauc_recall_at_100_std
      value: -5.516640557428562
    - type: nauc_recall_at_10_diff1
      value: -18.83385802183443
    - type: nauc_recall_at_10_max
      value: -15.04302952000884
    - type: nauc_recall_at_10_std
      value: -0.9615025531726922
    - type: nauc_recall_at_1_diff1
      value: 22.607506151253776
    - type: nauc_recall_at_1_max
      value: 10.921408762597743
    - type: nauc_recall_at_1_std
      value: -2.0177080867009054
    - type: nauc_recall_at_20_diff1
      value: -8.960549697900921
    - type: nauc_recall_at_20_max
      value: -6.8364201397227164
    - type: nauc_recall_at_20_std
      value: -1.2091707122721411
    - type: nauc_recall_at_3_diff1
      value: -17.196135512311084
    - type: nauc_recall_at_3_max
      value: -10.816815002699384
    - type: nauc_recall_at_3_std
      value: 12.535755202753904
    - type: nauc_recall_at_5_diff1
      value: -23.856486271404066
    - type: nauc_recall_at_5_max
      value: -13.129773406696268
    - type: nauc_recall_at_5_std
      value: -2.885196394596191
    - type: ndcg_at_1
      value: 6.715999999999999
    - type: ndcg_at_10
      value: 7.161
    - type: ndcg_at_100
      value: 9.506
    - type: ndcg_at_1000
      value: 14.194
    - type: ndcg_at_20
      value: 6.969
    - type: ndcg_at_3
      value: 7.285
    - type: ndcg_at_5
      value: 7.436
    - type: precision_at_1
      value: 8.955
    - type: precision_at_10
      value: 6.866
    - type: precision_at_100
      value: 2.343
    - type: precision_at_1000
      value: 0.557
    - type: precision_at_20
      value: 5.0
    - type: precision_at_3
      value: 9.453
    - type: precision_at_5
      value: 8.955
    - type: recall_at_1
      value: 0.599
    - type: recall_at_10
      value: 5.234
    - type: recall_at_100
      value: 14.610999999999999
    - type: recall_at_1000
      value: 31.723000000000003
    - type: recall_at_20
      value: 6.797000000000001
    - type: recall_at_3
      value: 2.1239999999999997
    - type: recall_at_5
      value: 3.836
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
      value: 9.612
    - type: map_at_1
      value: 1.5150000000000001
    - type: map_at_10
      value: 3.324
    - type: map_at_100
      value: 4.593
    - type: map_at_1000
      value: 4.942
    - type: map_at_20
      value: 3.775
    - type: map_at_3
      value: 2.349
    - type: map_at_5
      value: 2.83
    - type: mrr_at_1
      value: 17.75
    - type: mrr_at_10
      value: 25.455257936507948
    - type: mrr_at_100
      value: 26.384386588195795
    - type: mrr_at_1000
      value: 26.43428730177263
    - type: mrr_at_20
      value: 26.012663071147983
    - type: mrr_at_3
      value: 22.916666666666668
    - type: mrr_at_5
      value: 24.42916666666667
    - type: nauc_map_at_1000_diff1
      value: 22.13041079857
    - type: nauc_map_at_1000_max
      value: 30.847169046279717
    - type: nauc_map_at_1000_std
      value: 26.662372161640164
    - type: nauc_map_at_100_diff1
      value: 22.33437365695696
    - type: nauc_map_at_100_max
      value: 30.631982988659413
    - type: nauc_map_at_100_std
      value: 24.343041349757826
    - type: nauc_map_at_10_diff1
      value: 24.027517719649303
    - type: nauc_map_at_10_max
      value: 25.07712884251914
    - type: nauc_map_at_10_std
      value: 13.947979384184976
    - type: nauc_map_at_1_diff1
      value: 36.83267850021598
    - type: nauc_map_at_1_max
      value: 19.169430946850284
    - type: nauc_map_at_1_std
      value: 9.884774862276792
    - type: nauc_map_at_20_diff1
      value: 23.514668795309415
    - type: nauc_map_at_20_max
      value: 27.504950445908978
    - type: nauc_map_at_20_std
      value: 17.094975030047124
    - type: nauc_map_at_3_diff1
      value: 26.34278610573698
    - type: nauc_map_at_3_max
      value: 20.845843284715972
    - type: nauc_map_at_3_std
      value: 7.67049397964597
    - type: nauc_map_at_5_diff1
      value: 25.7750795640811
    - type: nauc_map_at_5_max
      value: 22.947480091712098
    - type: nauc_map_at_5_std
      value: 11.721230195408548
    - type: nauc_mrr_at_1000_diff1
      value: 22.232372488450842
    - type: nauc_mrr_at_1000_max
      value: 27.572890316358283
    - type: nauc_mrr_at_1000_std
      value: 16.214637981707586
    - type: nauc_mrr_at_100_diff1
      value: 22.236444609236038
    - type: nauc_mrr_at_100_max
      value: 27.58760243571819
    - type: nauc_mrr_at_100_std
      value: 16.244413870712897
    - type: nauc_mrr_at_10_diff1
      value: 22.225463768969977
    - type: nauc_mrr_at_10_max
      value: 28.085279372515014
    - type: nauc_mrr_at_10_std
      value: 16.63553736106648
    - type: nauc_mrr_at_1_diff1
      value: 29.84035077607877
    - type: nauc_mrr_at_1_max
      value: 29.694489641199347
    - type: nauc_mrr_at_1_std
      value: 13.521637546163495
    - type: nauc_mrr_at_20_diff1
      value: 22.04153237789325
    - type: nauc_mrr_at_20_max
      value: 27.694203519607907
    - type: nauc_mrr_at_20_std
      value: 16.41753082494305
    - type: nauc_mrr_at_3_diff1
      value: 23.699732601185406
    - type: nauc_mrr_at_3_max
      value: 28.552272889924087
    - type: nauc_mrr_at_3_std
      value: 15.054097838038286
    - type: nauc_mrr_at_5_diff1
      value: 23.127326455282443
    - type: nauc_mrr_at_5_max
      value: 28.769272111978832
    - type: nauc_mrr_at_5_std
      value: 16.113310297737975
    - type: nauc_ndcg_at_1000_diff1
      value: 19.30064409197478
    - type: nauc_ndcg_at_1000_max
      value: 28.102160223624878
    - type: nauc_ndcg_at_1000_std
      value: 30.203518553202162
    - type: nauc_ndcg_at_100_diff1
      value: 18.61374183566408
    - type: nauc_ndcg_at_100_max
      value: 26.626236693773404
    - type: nauc_ndcg_at_100_std
      value: 25.742758699186076
    - type: nauc_ndcg_at_10_diff1
      value: 22.519496459830016
    - type: nauc_ndcg_at_10_max
      value: 29.403797316052678
    - type: nauc_ndcg_at_10_std
      value: 20.893386965358616
    - type: nauc_ndcg_at_1_diff1
      value: 32.866635298438084
    - type: nauc_ndcg_at_1_max
      value: 26.59719751655438
    - type: nauc_ndcg_at_1_std
      value: 11.114394574061539
    - type: nauc_ndcg_at_20_diff1
      value: 21.157000991633115
    - type: nauc_ndcg_at_20_max
      value: 27.740565719664534
    - type: nauc_ndcg_at_20_std
      value: 21.639809971682443
    - type: nauc_ndcg_at_3_diff1
      value: 25.11861929994868
    - type: nauc_ndcg_at_3_max
      value: 30.05796948174576
    - type: nauc_ndcg_at_3_std
      value: 15.558218990994382
    - type: nauc_ndcg_at_5_diff1
      value: 23.56633730677446
    - type: nauc_ndcg_at_5_max
      value: 29.407157319632233
    - type: nauc_ndcg_at_5_std
      value: 18.567271816504054
    - type: nauc_precision_at_1000_diff1
      value: 15.34548548807785
    - type: nauc_precision_at_1000_max
      value: 10.572226641262324
    - type: nauc_precision_at_1000_std
      value: 29.1034314360236
    - type: nauc_precision_at_100_diff1
      value: 15.716430228733962
    - type: nauc_precision_at_100_max
      value: 29.095076486854232
    - type: nauc_precision_at_100_std
      value: 38.5066690028862
    - type: nauc_precision_at_10_diff1
      value: 19.68952528017596
    - type: nauc_precision_at_10_max
      value: 36.890169328577436
    - type: nauc_precision_at_10_std
      value: 30.965796095297055
    - type: nauc_precision_at_1_diff1
      value: 29.84035077607877
    - type: nauc_precision_at_1_max
      value: 29.694489641199347
    - type: nauc_precision_at_1_std
      value: 13.521637546163495
    - type: nauc_precision_at_20_diff1
      value: 18.030808015274253
    - type: nauc_precision_at_20_max
      value: 37.61603054850129
    - type: nauc_precision_at_20_std
      value: 34.160861586371816
    - type: nauc_precision_at_3_diff1
      value: 20.899695298609572
    - type: nauc_precision_at_3_max
      value: 35.736648108449906
    - type: nauc_precision_at_3_std
      value: 21.012939343933635
    - type: nauc_precision_at_5_diff1
      value: 20.038574686656855
    - type: nauc_precision_at_5_max
      value: 37.244225604024464
    - type: nauc_precision_at_5_std
      value: 27.105877764557317
    - type: nauc_recall_at_1000_diff1
      value: 7.621037010770166
    - type: nauc_recall_at_1000_max
      value: 14.556069262959875
    - type: nauc_recall_at_1000_std
      value: 24.912834855259458
    - type: nauc_recall_at_100_diff1
      value: 5.640854515267624
    - type: nauc_recall_at_100_max
      value: 12.319243091931583
    - type: nauc_recall_at_100_std
      value: 18.20593364111766
    - type: nauc_recall_at_10_diff1
      value: 9.625612977495116
    - type: nauc_recall_at_10_max
      value: 17.05920473206263
    - type: nauc_recall_at_10_std
      value: 10.7221437835498
    - type: nauc_recall_at_1_diff1
      value: 36.83267850021598
    - type: nauc_recall_at_1_max
      value: 19.169430946850284
    - type: nauc_recall_at_1_std
      value: 9.884774862276792
    - type: nauc_recall_at_20_diff1
      value: 8.05059067573258
    - type: nauc_recall_at_20_max
      value: 15.8154139120262
    - type: nauc_recall_at_20_std
      value: 12.679202204644218
    - type: nauc_recall_at_3_diff1
      value: 16.446191987706968
    - type: nauc_recall_at_3_max
      value: 16.891019665567892
    - type: nauc_recall_at_3_std
      value: 5.902427268316366
    - type: nauc_recall_at_5_diff1
      value: 16.441740431697145
    - type: nauc_recall_at_5_max
      value: 18.339945932093187
    - type: nauc_recall_at_5_std
      value: 11.244004704766795
    - type: ndcg_at_1
      value: 13.0
    - type: ndcg_at_10
      value: 9.612
    - type: ndcg_at_100
      value: 11.403
    - type: ndcg_at_1000
      value: 15.142
    - type: ndcg_at_20
      value: 9.419
    - type: ndcg_at_3
      value: 10.821
    - type: ndcg_at_5
      value: 10.462
    - type: precision_at_1
      value: 17.75
    - type: precision_at_10
      value: 9.15
    - type: precision_at_100
      value: 3.0
    - type: precision_at_1000
      value: 0.716
    - type: precision_at_20
      value: 6.763
    - type: precision_at_3
      value: 13.417000000000002
    - type: precision_at_5
      value: 12.35
    - type: recall_at_1
      value: 1.5150000000000001
    - type: recall_at_10
      value: 5.858
    - type: recall_at_100
      value: 15.643
    - type: recall_at_1000
      value: 28.51
    - type: recall_at_20
      value: 8.25
    - type: recall_at_3
      value: 2.995
    - type: recall_at_5
      value: 4.117
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBpediaClassification (default)
      revision: 9abd46cf7fc8b4c64290f26993c540b92aa145ac
      split: test
      type: fancyzhx/dbpedia_14
    metrics:
    - type: accuracy
      value: 79.6484375
    - type: f1
      value: 78.34279956840108
    - type: f1_weighted
      value: 78.35088313144212
    - type: main_score
      value: 79.6484375
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB DefinitionClassificationLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 84.51757666417352
    - type: ap
      value: 80.76707736262222
    - type: ap_weighted
      value: 80.76707736262222
    - type: f1
      value: 84.51702233000746
    - type: f1_weighted
      value: 84.52014045969152
    - type: main_score
      value: 84.51757666417352
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB Diversity1LegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 76.33333333333334
    - type: ap
      value: 23.666666666666668
    - type: ap_weighted
      value: 23.666666666666668
    - type: f1
      value: 43.28922495274102
    - type: f1_weighted
      value: 66.08821676118463
    - type: main_score
      value: 76.33333333333334
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB Diversity2LegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 74.66666666666669
    - type: ap
      value: 25.333333333333336
    - type: ap_weighted
      value: 25.333333333333336
    - type: f1
      value: 42.74809160305343
    - type: f1_weighted
      value: 63.83715012722646
    - type: main_score
      value: 74.66666666666669
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB Diversity3LegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 58.666666666666664
    - type: ap
      value: 58.666666666666664
    - type: ap_weighted
      value: 58.666666666666664
    - type: f1
      value: 36.97478991596639
    - type: f1_weighted
      value: 43.383753501400555
    - type: main_score
      value: 58.666666666666664
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB Diversity4LegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 53.333333333333336
    - type: ap
      value: 53.333333333333336
    - type: ap_weighted
      value: 53.333333333333336
    - type: f1
      value: 34.782608695652165
    - type: f1_weighted
      value: 37.10144927536233
    - type: main_score
      value: 53.333333333333336
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB Diversity5LegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 57.333333333333336
    - type: ap
      value: 57.333333333333336
    - type: ap_weighted
      value: 57.333333333333336
    - type: f1
      value: 36.440677966101696
    - type: f1_weighted
      value: 41.78531073446328
    - type: main_score
      value: 57.333333333333336
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB Diversity6LegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 55.33333333333334
    - type: ap
      value: 55.335312709510575
    - type: ap_weighted
      value: 55.335312709510575
    - type: f1
      value: 53.72075888745626
    - type: f1_weighted
      value: 54.239086387916736
    - type: main_score
      value: 55.33333333333334
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB EmotionClassification (default)
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: test
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 29.500000000000004
    - type: f1
      value: 25.366180985174143
    - type: f1_weighted
      value: 31.616367697127934
    - type: main_score
      value: 29.500000000000004
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB EmotionClassification (default)
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: validation
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 29.59
    - type: f1
      value: 25.66115067003055
    - type: f1_weighted
      value: 31.610928656113497
    - type: main_score
      value: 29.59
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FaithDial (default)
      revision: 7a414e80725eac766f2602676dc8b39f80b061e4
      split: test
      type: McGill-NLP/FaithDial
    metrics:
    - type: main_score
      value: 13.203999999999999
    - type: map_at_1
      value: 4.603
    - type: map_at_10
      value: 9.689
    - type: map_at_100
      value: 10.934000000000001
    - type: map_at_1000
      value: 11.06
    - type: map_at_20
      value: 10.282
    - type: map_at_3
      value: 7.46
    - type: map_at_5
      value: 8.601
    - type: mrr_at_1
      value: 3.9177277179236047
    - type: mrr_at_10
      value: 9.372463970896874
    - type: mrr_at_100
      value: 10.603150618822562
    - type: mrr_at_1000
      value: 10.7286670506961
    - type: mrr_at_20
      value: 9.954996988904508
    - type: mrr_at_3
      value: 7.190662748938949
    - type: mrr_at_5
      value: 8.24844923277832
    - type: nauc_map_at_1000_diff1
      value: 5.307634687499811
    - type: nauc_map_at_1000_max
      value: 2.3021513473591937
    - type: nauc_map_at_1000_std
      value: -17.73170584094867
    - type: nauc_map_at_100_diff1
      value: 5.297350465897308
    - type: nauc_map_at_100_max
      value: 2.346907480087932
    - type: nauc_map_at_100_std
      value: -17.732933045818474
    - type: nauc_map_at_10_diff1
      value: 6.045977877604437
    - type: nauc_map_at_10_max
      value: 1.8368181824684384
    - type: nauc_map_at_10_std
      value: -19.787304492799954
    - type: nauc_map_at_1_diff1
      value: 1.3052717698444036
    - type: nauc_map_at_1_max
      value: -4.135496842891768
    - type: nauc_map_at_1_std
      value: -19.25157996189646
    - type: nauc_map_at_20_diff1
      value: 5.761740069816983
    - type: nauc_map_at_20_max
      value: 2.2984777745182807
    - type: nauc_map_at_20_std
      value: -18.75124467493425
    - type: nauc_map_at_3_diff1
      value: 6.651930299284997
    - type: nauc_map_at_3_max
      value: -0.3272549806355308
    - type: nauc_map_at_3_std
      value: -21.098596102590484
    - type: nauc_map_at_5_diff1
      value: 6.967992538819455
    - type: nauc_map_at_5_max
      value: 0.5435787268710469
    - type: nauc_map_at_5_std
      value: -20.283953347398604
    - type: nauc_mrr_at_1000_diff1
      value: 6.740910238395446
    - type: nauc_mrr_at_1000_max
      value: 2.260193924794291
    - type: nauc_mrr_at_1000_std
      value: -16.012044193795997
    - type: nauc_mrr_at_100_diff1
      value: 6.722495330136685
    - type: nauc_mrr_at_100_max
      value: 2.303043406886841
    - type: nauc_mrr_at_100_std
      value: -16.020952265971687
    - type: nauc_mrr_at_10_diff1
      value: 7.499027953700563
    - type: nauc_mrr_at_10_max
      value: 1.7369780903909435
    - type: nauc_mrr_at_10_std
      value: -17.773058332780796
    - type: nauc_mrr_at_1_diff1
      value: 7.479923371906451
    - type: nauc_mrr_at_1_max
      value: -6.618146247607683
    - type: nauc_mrr_at_1_std
      value: -17.69446400002114
    - type: nauc_mrr_at_20_diff1
      value: 7.167945669605475
    - type: nauc_mrr_at_20_max
      value: 2.272029597435147
    - type: nauc_mrr_at_20_std
      value: -17.15567528957464
    - type: nauc_mrr_at_3_diff1
      value: 8.689535713040886
    - type: nauc_mrr_at_3_max
      value: -0.503459138449647
    - type: nauc_mrr_at_3_std
      value: -18.50457781869527
    - type: nauc_mrr_at_5_diff1
      value: 8.688882139587488
    - type: nauc_mrr_at_5_max
      value: 0.6822164815544203
    - type: nauc_mrr_at_5_std
      value: -18.323678647634363
    - type: nauc_ndcg_at_1000_diff1
      value: 3.895349559751926
    - type: nauc_ndcg_at_1000_max
      value: 4.497321779831305
    - type: nauc_ndcg_at_1000_std
      value: -11.297185296929218
    - type: nauc_ndcg_at_100_diff1
      value: 2.8704577253134365
    - type: nauc_ndcg_at_100_max
      value: 5.389954929442454
    - type: nauc_ndcg_at_100_std
      value: -10.400630555415756
    - type: nauc_ndcg_at_10_diff1
      value: 6.092068255087623
    - type: nauc_ndcg_at_10_max
      value: 4.227250873974054
    - type: nauc_ndcg_at_10_std
      value: -19.171869390880573
    - type: nauc_ndcg_at_1_diff1
      value: 1.3052717698444036
    - type: nauc_ndcg_at_1_max
      value: -4.135496842891768
    - type: nauc_ndcg_at_1_std
      value: -19.25157996189646
    - type: nauc_ndcg_at_20_diff1
      value: 5.40179215063042
    - type: nauc_ndcg_at_20_max
      value: 5.316262069583032
    - type: nauc_ndcg_at_20_std
      value: -16.253163982932534
    - type: nauc_ndcg_at_3_diff1
      value: 7.419223521385511
    - type: nauc_ndcg_at_3_max
      value: 0.5830467018062534
    - type: nauc_ndcg_at_3_std
      value: -21.398247993882336
    - type: nauc_ndcg_at_5_diff1
      value: 7.871015584820952
    - type: nauc_ndcg_at_5_max
      value: 1.911179358773651
    - type: nauc_ndcg_at_5_std
      value: -20.05509945356285
    - type: nauc_precision_at_1000_diff1
      value: -0.844755882557819
    - type: nauc_precision_at_1000_max
      value: 9.219453102597015
    - type: nauc_precision_at_1000_std
      value: 29.23861313970078
    - type: nauc_precision_at_100_diff1
      value: -3.7470853890619606
    - type: nauc_precision_at_100_max
      value: 10.533862037156355
    - type: nauc_precision_at_100_std
      value: 8.252086567057157
    - type: nauc_precision_at_10_diff1
      value: 5.901773888339623
    - type: nauc_precision_at_10_max
      value: 8.111412609207008
    - type: nauc_precision_at_10_std
      value: -18.07076007909741
    - type: nauc_precision_at_1_diff1
      value: 1.3052717698444036
    - type: nauc_precision_at_1_max
      value: -4.135496842891768
    - type: nauc_precision_at_1_std
      value: -19.25157996189646
    - type: nauc_precision_at_20_diff1
      value: 4.510193698541817
    - type: nauc_precision_at_20_max
      value: 10.055538647436114
    - type: nauc_precision_at_20_std
      value: -11.60139299594993
    - type: nauc_precision_at_3_diff1
      value: 8.853244226690453
    - type: nauc_precision_at_3_max
      value: 2.3906768293455305
    - type: nauc_precision_at_3_std
      value: -21.96838812494048
    - type: nauc_precision_at_5_diff1
      value: 9.38307261489558
    - type: nauc_precision_at_5_max
      value: 4.352929382840095
    - type: nauc_precision_at_5_std
      value: -19.535985352739786
    - type: nauc_recall_at_1000_diff1
      value: -0.8447558825574738
    - type: nauc_recall_at_1000_max
      value: 9.219453102597296
    - type: nauc_recall_at_1000_std
      value: 29.23861313970089
    - type: nauc_recall_at_100_diff1
      value: -3.747085389061965
    - type: nauc_recall_at_100_max
      value: 10.533862037156396
    - type: nauc_recall_at_100_std
      value: 8.252086567057194
    - type: nauc_recall_at_10_diff1
      value: 5.901773888339621
    - type: nauc_recall_at_10_max
      value: 8.111412609207008
    - type: nauc_recall_at_10_std
      value: -18.07076007909743
    - type: nauc_recall_at_1_diff1
      value: 1.3052717698444036
    - type: nauc_recall_at_1_max
      value: -4.135496842891768
    - type: nauc_recall_at_1_std
      value: -19.25157996189646
    - type: nauc_recall_at_20_diff1
      value: 4.510193698541801
    - type: nauc_recall_at_20_max
      value: 10.055538647436121
    - type: nauc_recall_at_20_std
      value: -11.601392995949936
    - type: nauc_recall_at_3_diff1
      value: 8.853244226690453
    - type: nauc_recall_at_3_max
      value: 2.390676829345526
    - type: nauc_recall_at_3_std
      value: -21.96838812494048
    - type: nauc_recall_at_5_diff1
      value: 9.383072614895593
    - type: nauc_recall_at_5_max
      value: 4.352929382840121
    - type: nauc_recall_at_5_std
      value: -19.535985352739782
    - type: ndcg_at_1
      value: 4.603
    - type: ndcg_at_10
      value: 13.203999999999999
    - type: ndcg_at_100
      value: 20.254
    - type: ndcg_at_1000
      value: 23.923
    - type: ndcg_at_20
      value: 15.354000000000001
    - type: ndcg_at_3
      value: 8.469
    - type: ndcg_at_5
      value: 10.536
    - type: precision_at_1
      value: 4.603
    - type: precision_at_10
      value: 2.478
    - type: precision_at_100
      value: 0.6
    - type: precision_at_1000
      value: 0.09
    - type: precision_at_20
      value: 1.6629999999999998
    - type: precision_at_3
      value: 3.803
    - type: precision_at_5
      value: 3.2910000000000004
    - type: recall_at_1
      value: 4.603
    - type: recall_at_10
      value: 24.779999999999998
    - type: recall_at_100
      value: 60.039
    - type: recall_at_1000
      value: 89.667
    - type: recall_at_20
      value: 33.251999999999995
    - type: recall_at_3
      value: 11.41
    - type: recall_at_5
      value: 16.454
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FeedbackQARetrieval (default)
      revision: 1ee1cd0
      split: test
      type: lt2c/fqa
    metrics:
    - type: main_score
      value: 19.026
    - type: map_at_1
      value: 19.026
    - type: map_at_10
      value: 26.287
    - type: map_at_100
      value: 27.294
    - type: map_at_1000
      value: 27.381
    - type: map_at_20
      value: 26.823999999999998
    - type: map_at_3
      value: 24.18
    - type: map_at_5
      value: 25.365
    - type: mrr_at_1
      value: 19.026104417670684
    - type: mrr_at_10
      value: 26.287052973799952
    - type: mrr_at_100
      value: 27.29426430169323
    - type: mrr_at_1000
      value: 27.380630702740504
    - type: mrr_at_20
      value: 26.824443943374348
    - type: mrr_at_3
      value: 24.1800535475234
    - type: mrr_at_5
      value: 25.364792503346674
    - type: nauc_map_at_1000_diff1
      value: 40.81899763873748
    - type: nauc_map_at_1000_max
      value: 11.253631614437268
    - type: nauc_map_at_1000_std
      value: 1.5897060898020656
    - type: nauc_map_at_100_diff1
      value: 40.78701343792848
    - type: nauc_map_at_100_max
      value: 11.27294926630661
    - type: nauc_map_at_100_std
      value: 1.6118772584552687
    - type: nauc_map_at_10_diff1
      value: 41.075611489073324
    - type: nauc_map_at_10_max
      value: 11.521202364241029
    - type: nauc_map_at_10_std
      value: 1.2931734299571058
    - type: nauc_map_at_1_diff1
      value: 48.17546169609799
    - type: nauc_map_at_1_max
      value: 13.494189949598375
    - type: nauc_map_at_1_std
      value: 0.07263746580580938
    - type: nauc_map_at_20_diff1
      value: 40.841882938863435
    - type: nauc_map_at_20_max
      value: 11.418649006248861
    - type: nauc_map_at_20_std
      value: 1.4175148500460242
    - type: nauc_map_at_3_diff1
      value: 42.213517992662815
    - type: nauc_map_at_3_max
      value: 12.808728940816176
    - type: nauc_map_at_3_std
      value: 1.0861600000182654
    - type: nauc_map_at_5_diff1
      value: 41.6309141720988
    - type: nauc_map_at_5_max
      value: 11.996308489388992
    - type: nauc_map_at_5_std
      value: 1.2641645150076395
    - type: nauc_mrr_at_1000_diff1
      value: 40.81899763873748
    - type: nauc_mrr_at_1000_max
      value: 11.253631614437268
    - type: nauc_mrr_at_1000_std
      value: 1.5897060898020656
    - type: nauc_mrr_at_100_diff1
      value: 40.78701343792848
    - type: nauc_mrr_at_100_max
      value: 11.27294926630661
    - type: nauc_mrr_at_100_std
      value: 1.6118772584552687
    - type: nauc_mrr_at_10_diff1
      value: 41.075611489073324
    - type: nauc_mrr_at_10_max
      value: 11.521202364241029
    - type: nauc_mrr_at_10_std
      value: 1.2931734299571058
    - type: nauc_mrr_at_1_diff1
      value: 48.17546169609799
    - type: nauc_mrr_at_1_max
      value: 13.494189949598375
    - type: nauc_mrr_at_1_std
      value: 0.07263746580580938
    - type: nauc_mrr_at_20_diff1
      value: 40.841882938863435
    - type: nauc_mrr_at_20_max
      value: 11.418649006248861
    - type: nauc_mrr_at_20_std
      value: 1.4175148500460242
    - type: nauc_mrr_at_3_diff1
      value: 42.213517992662815
    - type: nauc_mrr_at_3_max
      value: 12.808728940816176
    - type: nauc_mrr_at_3_std
      value: 1.0861600000182654
    - type: nauc_mrr_at_5_diff1
      value: 41.6309141720988
    - type: nauc_mrr_at_5_max
      value: 11.996308489388992
    - type: nauc_mrr_at_5_std
      value: 1.2641645150076395
    - type: nauc_ndcg_at_1000_diff1
      value: 37.7525819268389
    - type: nauc_ndcg_at_1000_max
      value: 8.537400436184365
    - type: nauc_ndcg_at_1000_std
      value: 2.9622195950411925
    - type: nauc_ndcg_at_100_diff1
      value: 36.787603237032975
    - type: nauc_ndcg_at_100_max
      value: 8.608543884213873
    - type: nauc_ndcg_at_100_std
      value: 3.8384319334640695
    - type: nauc_ndcg_at_10_diff1
      value: 38.17646042200737
    - type: nauc_ndcg_at_10_max
      value: 10.09464701041161
    - type: nauc_ndcg_at_10_std
      value: 1.82746325273071
    - type: nauc_ndcg_at_1_diff1
      value: 48.17546169609799
    - type: nauc_ndcg_at_1_max
      value: 13.494189949598375
    - type: nauc_ndcg_at_1_std
      value: 0.07263746580580938
    - type: nauc_ndcg_at_20_diff1
      value: 37.27227964097512
    - type: nauc_ndcg_at_20_max
      value: 9.739171990515723
    - type: nauc_ndcg_at_20_std
      value: 2.3086094833252115
    - type: nauc_ndcg_at_3_diff1
      value: 40.37281782985726
    - type: nauc_ndcg_at_3_max
      value: 12.624015391541455
    - type: nauc_ndcg_at_3_std
      value: 1.407593942089084
    - type: nauc_ndcg_at_5_diff1
      value: 39.35750963645447
    - type: nauc_ndcg_at_5_max
      value: 11.236243459280038
    - type: nauc_ndcg_at_5_std
      value: 1.722451235770262
    - type: nauc_precision_at_1000_diff1
      value: 12.726040453874319
    - type: nauc_precision_at_1000_max
      value: -30.085818447743566
    - type: nauc_precision_at_1000_std
      value: 15.649828948529738
    - type: nauc_precision_at_100_diff1
      value: 20.374750836627285
    - type: nauc_precision_at_100_max
      value: -4.315521193959148
    - type: nauc_precision_at_100_std
      value: 15.928528368224907
    - type: nauc_precision_at_10_diff1
      value: 30.394845120941987
    - type: nauc_precision_at_10_max
      value: 5.92964609786744
    - type: nauc_precision_at_10_std
      value: 3.297191207595148
    - type: nauc_precision_at_1_diff1
      value: 48.17546169609799
    - type: nauc_precision_at_1_max
      value: 13.494189949598375
    - type: nauc_precision_at_1_std
      value: 0.07263746580580938
    - type: nauc_precision_at_20_diff1
      value: 26.72269495712158
    - type: nauc_precision_at_20_max
      value: 4.521447508378409
    - type: nauc_precision_at_20_std
      value: 5.180527682236829
    - type: nauc_precision_at_3_diff1
      value: 35.59077406479908
    - type: nauc_precision_at_3_max
      value: 12.151097771811763
    - type: nauc_precision_at_3_std
      value: 2.24486462426719
    - type: nauc_precision_at_5_diff1
      value: 33.428016378866076
    - type: nauc_precision_at_5_max
      value: 9.15731660897423
    - type: nauc_precision_at_5_std
      value: 2.9353909916486294
    - type: nauc_recall_at_1000_diff1
      value: 12.726040453874369
    - type: nauc_recall_at_1000_max
      value: -30.085818447743364
    - type: nauc_recall_at_1000_std
      value: 15.649828948529635
    - type: nauc_recall_at_100_diff1
      value: 20.374750836627264
    - type: nauc_recall_at_100_max
      value: -4.315521193959231
    - type: nauc_recall_at_100_std
      value: 15.928528368224876
    - type: nauc_recall_at_10_diff1
      value: 30.394845120942005
    - type: nauc_recall_at_10_max
      value: 5.929646097867471
    - type: nauc_recall_at_10_std
      value: 3.297191207595157
    - type: nauc_recall_at_1_diff1
      value: 48.17546169609799
    - type: nauc_recall_at_1_max
      value: 13.494189949598375
    - type: nauc_recall_at_1_std
      value: 0.07263746580580938
    - type: nauc_recall_at_20_diff1
      value: 26.722694957121647
    - type: nauc_recall_at_20_max
      value: 4.521447508378419
    - type: nauc_recall_at_20_std
      value: 5.1805276822368524
    - type: nauc_recall_at_3_diff1
      value: 35.59077406479911
    - type: nauc_recall_at_3_max
      value: 12.151097771811772
    - type: nauc_recall_at_3_std
      value: 2.2448646242671857
    - type: nauc_recall_at_5_diff1
      value: 33.42801637886615
    - type: nauc_recall_at_5_max
      value: 9.15731660897428
    - type: nauc_recall_at_5_std
      value: 2.9353909916486782
    - type: ndcg_at_1
      value: 19.026
    - type: ndcg_at_10
      value: 30.245
    - type: ndcg_at_100
      value: 35.716
    - type: ndcg_at_1000
      value: 38.421
    - type: ndcg_at_20
      value: 32.242
    - type: ndcg_at_3
      value: 25.884
    - type: ndcg_at_5
      value: 28.016999999999996
    - type: precision_at_1
      value: 19.026
    - type: precision_at_10
      value: 4.287
    - type: precision_at_100
      value: 0.697
    - type: precision_at_1000
      value: 0.092
    - type: precision_at_20
      value: 2.543
    - type: precision_at_3
      value: 10.274
    - type: precision_at_5
      value: 7.199
    - type: recall_at_1
      value: 19.026
    - type: recall_at_10
      value: 42.870999999999995
    - type: recall_at_100
      value: 69.729
    - type: recall_at_1000
      value: 91.968
    - type: recall_at_20
      value: 50.853
    - type: recall_at_3
      value: 30.823
    - type: recall_at_5
      value: 35.994
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FinancialPhrasebankClassification (default)
      revision: 1484d06fe7af23030c7c977b12556108d1f67039
      split: train
      type: takala/financial_phrasebank
    metrics:
    - type: accuracy
      value: 67.97703180212015
    - type: f1
      value: 57.55594804795911
    - type: f1_weighted
      value: 68.01782223640284
    - type: main_score
      value: 67.97703180212015
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FrenkEnClassification (default)
      revision: 52483dba0ff23291271ee9249839865e3c3e7e50
      split: test
      type: classla/FRENK-hate-en
    metrics:
    - type: accuracy
      value: 55.289004780530206
    - type: ap
      value: 41.78925787378802
    - type: ap_weighted
      value: 41.78925787378802
    - type: f1
      value: 54.04961911556596
    - type: f1_weighted
      value: 54.99825667370393
    - type: main_score
      value: 55.289004780530206
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FunctionOfDecisionSectionLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 16.621253405994548
    - type: f1
      value: 15.693085823082844
    - type: f1_weighted
      value: 15.880480382757908
    - type: main_score
      value: 16.621253405994548
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB GPUSpeedTask (default)
      revision: '1.0'
      split: test
      type: 'GPUSpeedTask'
    metrics:
    - type: avg_words_per_sec
      value: 7186456.843601672
    - type: main_score
      value: 7186456.843601672
    - type: num_gpus
      value: 300
    - type: physical_cores
      value: 3600
    - type: time_mean
      value: 5.055342401776995
    - type: time_std
      value: 1.0630782067852145
    - type: total_cores
      value: 7200
    task:
      type: Speed
  - dataset:
      config: default
      name: MTEB GeoreviewClassification (default)
      revision: 3765c0d1de6b7d264bc459433c45e5a75513839c
      split: test
      type: ai-forever/georeview-classification
    metrics:
    - type: accuracy
      value: 41.3623046875
    - type: f1
      value: 39.78804299557415
    - type: f1_weighted
      value: 39.787468620260825
    - type: main_score
      value: 41.3623046875
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB GeoreviewClusteringP2P (default)
      revision: 97a313c8fc85b47f13f33e7e9a95c1ad888c7fec
      split: test
      type: ai-forever/georeview-clustering-p2p
    metrics:
    - type: main_score
      value: 59.713474431847416
    - type: v_measure
      value: 59.713474431847416
    - type: v_measure_std
      value: 1.1676689250848244
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB HeadlineClassification (default)
      revision: 2fe05ee6b5832cda29f2ef7aaad7b7fe6a3609eb
      split: test
      type: ai-forever/headline-classification
    metrics:
    - type: accuracy
      value: 68.9013671875
    - type: f1
      value: 68.80041842725984
    - type: f1_weighted
      value: 68.80034868754102
    - type: main_score
      value: 68.9013671875
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ImdbClassification (default)
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
      split: test
      type: mteb/imdb
    metrics:
    - type: accuracy
      value: 58.35799999999999
    - type: ap
      value: 55.16102855038145
    - type: ap_weighted
      value: 55.16102855038145
    - type: f1
      value: 57.51452465161078
    - type: f1_weighted
      value: 57.514524651610785
    - type: main_score
      value: 58.35799999999999
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB InappropriatenessClassification (default)
      revision: 601651fdc45ef243751676e62dd7a19f491c0285
      split: test
      type: ai-forever/inappropriateness-classification
    metrics:
    - type: accuracy
      value: 59.11132812499999
    - type: ap
      value: 55.4713646939923
    - type: ap_weighted
      value: 55.4713646939923
    - type: f1
      value: 58.8968409989092
    - type: f1_weighted
      value: 58.8968409989092
    - type: main_score
      value: 59.11132812499999
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB InsurancePolicyInterpretationLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 20.30075187969925
    - type: f1
      value: 11.25
    - type: f1_weighted
      value: 6.851503759398496
    - type: main_score
      value: 20.30075187969925
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB InternationalCitizenshipQuestionsLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 60.107421875
    - type: ap
      value: 46.4447988877498
    - type: ap_weighted
      value: 46.4447988877498
    - type: f1
      value: 56.153528268151675
    - type: f1_weighted
      value: 58.210838762771935
    - type: main_score
      value: 60.107421875
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB JCrewBlockerLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 79.62962962962962
    - type: ap
      value: 86.55394524959743
    - type: ap_weighted
      value: 86.55394524959743
    - type: f1
      value: 61.60310277957336
    - type: f1_weighted
      value: 79.14242620124973
    - type: main_score
      value: 79.62962962962962
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB KinopoiskClassification (default)
      revision: 5911f26666ac11af46cb9c6849d0dc80a378af24
      split: test
      type: ai-forever/kinopoisk-sentiment-classification
    metrics:
    - type: accuracy
      value: 50.46666666666666
    - type: f1
      value: 49.1239356856144
    - type: f1_weighted
      value: 49.123935685614384
    - type: main_score
      value: 50.46666666666666
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsBenefitsLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 66.66666666666667
    - type: ap
      value: 61.11111111111111
    - type: ap_weighted
      value: 61.11111111111111
    - type: f1
      value: 66.66666666666667
    - type: f1_weighted
      value: 66.66666666666667
    - type: main_score
      value: 66.66666666666667
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsBusinessLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 70.11494252873564
    - type: ap
      value: 68.24378508420207
    - type: ap_weighted
      value: 68.24378508420207
    - type: f1
      value: 68.07339449541284
    - type: f1_weighted
      value: 68.07339449541284
    - type: main_score
      value: 70.11494252873564
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsConsumerLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 58.143322475570045
    - type: ap
      value: 54.72001493806926
    - type: ap_weighted
      value: 54.72001493806926
    - type: f1
      value: 58.13788145283024
    - type: f1_weighted
      value: 58.13788145283024
    - type: main_score
      value: 58.143322475570045
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsCourtsLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 60.41666666666667
    - type: ap
      value: 56.07638888888889
    - type: ap_weighted
      value: 56.07638888888889
    - type: f1
      value: 59.78835978835979
    - type: f1_weighted
      value: 59.78835978835979
    - type: main_score
      value: 60.41666666666667
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsCrimeLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 70.63953488372093
    - type: ap
      value: 65.3728949478749
    - type: ap_weighted
      value: 65.3728949478749
    - type: f1
      value: 70.45754079263989
    - type: f1_weighted
      value: 70.45754079263989
    - type: main_score
      value: 70.63953488372093
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsDivorceLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 62.66666666666667
    - type: ap
      value: 57.45794392523364
    - type: ap_weighted
      value: 57.45794392523364
    - type: f1
      value: 60.886571056062586
    - type: f1_weighted
      value: 60.886571056062586
    - type: main_score
      value: 62.66666666666667
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsDomesticViolenceLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 68.39080459770115
    - type: ap
      value: 62.26053639846742
    - type: ap_weighted
      value: 62.26053639846742
    - type: f1
      value: 68.30601092896174
    - type: f1_weighted
      value: 68.30601092896174
    - type: main_score
      value: 68.39080459770115
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsEducationLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 69.64285714285714
    - type: ap
      value: 62.222222222222214
    - type: ap_weighted
      value: 62.222222222222214
    - type: f1
      value: 66.56129258868984
    - type: f1_weighted
      value: 66.56129258868984
    - type: main_score
      value: 69.64285714285714
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsEmploymentLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 63.521126760563384
    - type: ap
      value: 58.7392648574373
    - type: ap_weighted
      value: 58.7392648574373
    - type: f1
      value: 63.4682967433563
    - type: f1_weighted
      value: 63.4682967433563
    - type: main_score
      value: 63.521126760563384
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsEstatesLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 70.78651685393258
    - type: ap
      value: 64.05564472980203
    - type: ap_weighted
      value: 64.05564472980203
    - type: f1
      value: 70.54855542828051
    - type: f1_weighted
      value: 70.54855542828051
    - type: main_score
      value: 70.78651685393258
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsFamilyLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 75.48828125
    - type: ap
      value: 68.42998798076924
    - type: ap_weighted
      value: 68.42998798076924
    - type: f1
      value: 75.3630731744256
    - type: f1_weighted
      value: 75.3630731744256
    - type: main_score
      value: 75.48828125
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsHealthLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 64.60176991150443
    - type: ap
      value: 58.96246566981995
    - type: ap_weighted
      value: 58.96246566981995
    - type: f1
      value: 63.877567329976834
    - type: f1_weighted
      value: 63.877567329976834
    - type: main_score
      value: 64.60176991150443
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsHousingLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 48.73046875
    - type: ap
      value: 49.376600701618464
    - type: ap_weighted
      value: 49.376600701618464
    - type: f1
      value: 46.38903847304493
    - type: f1_weighted
      value: 46.38903847304493
    - type: main_score
      value: 48.73046875
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsImmigrationLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 83.5820895522388
    - type: ap
      value: 77.43325625394155
    - type: ap_weighted
      value: 77.43325625394155
    - type: f1
      value: 83.5674470457079
    - type: f1_weighted
      value: 83.5674470457079
    - type: main_score
      value: 83.5820895522388
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsTortsLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 63.19444444444444
    - type: ap
      value: 58.41384863123993
    - type: ap_weighted
      value: 58.41384863123993
    - type: f1
      value: 63.17846287451151
    - type: f1_weighted
      value: 63.17846287451151
    - type: main_score
      value: 63.19444444444444
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LearnedHandsTrafficLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 69.7841726618705
    - type: ap
      value: 62.353917770760766
    - type: ap_weighted
      value: 62.353917770760766
    - type: f1
      value: 66.90476190476191
    - type: f1_weighted
      value: 66.90476190476191
    - type: main_score
      value: 69.7841726618705
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LegalReasoningCausalityLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 56.36363636363636
    - type: ap
      value: 64.75724991854024
    - type: ap_weighted
      value: 64.75724991854024
    - type: f1
      value: 52.85714285714286
    - type: f1_weighted
      value: 51.220779220779214
    - type: main_score
      value: 56.36363636363636
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MAUDLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 27.607421875
    - type: f1
      value: 14.84669450435061
    - type: f1_weighted
      value: 28.881436838109853
    - type: main_score
      value: 27.607421875
    task:
      type: Classification
  - dataset:
      config: zh-CN
      name: MTEB MassiveIntentClassification (zh-CN)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 5.208473436449227
    - type: f1
      value: 3.062867346742466
    - type: f1_weighted
      value: 3.5821384620305414
    - type: main_score
      value: 5.208473436449227
    task:
      type: Classification
  - dataset:
      config: ko
      name: MTEB MassiveIntentClassification (ko)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.5319435104236723
    - type: f1
      value: 0.5994050487142139
    - type: f1_weighted
      value: 1.0538452549913138
    - type: main_score
      value: 2.5319435104236723
    task:
      type: Classification
  - dataset:
      config: hi
      name: MTEB MassiveIntentClassification (hi)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.558843308675185
    - type: f1
      value: 1.258311921873436
    - type: f1_weighted
      value: 1.4083594758704836
    - type: main_score
      value: 2.558843308675185
    task:
      type: Classification
  - dataset:
      config: kn
      name: MTEB MassiveIntentClassification (kn)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.0645595158036314
    - type: f1
      value: 1.2240987569096886
    - type: f1_weighted
      value: 1.0817495786784068
    - type: main_score
      value: 2.0645595158036314
    task:
      type: Classification
  - dataset:
      config: ka
      name: MTEB MassiveIntentClassification (ka)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.6395427034297243
    - type: f1
      value: 0.7660068670322584
    - type: f1_weighted
      value: 0.7729737527960681
    - type: main_score
      value: 2.6395427034297243
    task:
      type: Classification
  - dataset:
      config: am
      name: MTEB MassiveIntentClassification (am)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.276395427034297
    - type: f1
      value: 0.7755708386766476
    - type: f1_weighted
      value: 0.9189927682322296
    - type: main_score
      value: 2.276395427034297
    task:
      type: Classification
  - dataset:
      config: my
      name: MTEB MassiveIntentClassification (my)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 3.9576328177538667
    - type: f1
      value: 1.0681259563998668
    - type: f1_weighted
      value: 1.5818553042962555
    - type: main_score
      value: 3.9576328177538667
    task:
      type: Classification
  - dataset:
      config: el
      name: MTEB MassiveIntentClassification (el)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 9.663752521856086
    - type: f1
      value: 4.860476294706458
    - type: f1_weighted
      value: 6.8590598543643395
    - type: main_score
      value: 9.663752521856086
    task:
      type: Classification
  - dataset:
      config: lv
      name: MTEB MassiveIntentClassification (lv)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 22.32347007397445
    - type: f1
      value: 20.939653553666744
    - type: f1_weighted
      value: 20.899939110877806
    - type: main_score
      value: 22.32347007397445
    task:
      type: Classification
  - dataset:
      config: ml
      name: MTEB MassiveIntentClassification (ml)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.390719569603228
    - type: f1
      value: 0.46817075523593493
    - type: f1_weighted
      value: 0.8438228708667787
    - type: main_score
      value: 2.390719569603228
    task:
      type: Classification
  - dataset:
      config: mn
      name: MTEB MassiveIntentClassification (mn)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 28.994620040349695
    - type: f1
      value: 27.571069823401256
    - type: f1_weighted
      value: 27.263930155378503
    - type: main_score
      value: 28.994620040349695
    task:
      type: Classification
  - dataset:
      config: ur
      name: MTEB MassiveIntentClassification (ur)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.4478816408876933
    - type: f1
      value: 1.497656725806116
    - type: f1_weighted
      value: 1.5398763678691354
    - type: main_score
      value: 2.4478816408876933
    task:
      type: Classification
  - dataset:
      config: fa
      name: MTEB MassiveIntentClassification (fa)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 3.3355749831876267
    - type: f1
      value: 0.6816922655284716
    - type: f1_weighted
      value: 1.0887948480367862
    - type: main_score
      value: 3.3355749831876267
    task:
      type: Classification
  - dataset:
      config: ro
      name: MTEB MassiveIntentClassification (ro)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 31.72494956287828
    - type: f1
      value: 29.577749786404826
    - type: f1_weighted
      value: 29.551193355600514
    - type: main_score
      value: 31.72494956287828
    task:
      type: Classification
  - dataset:
      config: is
      name: MTEB MassiveIntentClassification (is)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 24.845326160053798
    - type: f1
      value: 22.11363990784136
    - type: f1_weighted
      value: 23.65026728412048
    - type: main_score
      value: 24.845326160053798
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
      value: 50.164761264290526
    - type: f1
      value: 47.85763581891828
    - type: f1_weighted
      value: 48.98444884040328
    - type: main_score
      value: 50.164761264290526
    task:
      type: Classification
  - dataset:
      config: hu
      name: MTEB MassiveIntentClassification (hu)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 25.524546065904502
    - type: f1
      value: 23.753046097467873
    - type: f1_weighted
      value: 23.826312126027823
    - type: main_score
      value: 25.524546065904502
    task:
      type: Classification
  - dataset:
      config: fr
      name: MTEB MassiveIntentClassification (fr)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 31.50638870208473
    - type: f1
      value: 31.370642915213388
    - type: f1_weighted
      value: 30.505546915456012
    - type: main_score
      value: 31.50638870208473
    task:
      type: Classification
  - dataset:
      config: th
      name: MTEB MassiveIntentClassification (th)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 3.739071956960323
    - type: f1
      value: 1.411228354273586
    - type: f1_weighted
      value: 1.216275118762689
    - type: main_score
      value: 3.739071956960323
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB MassiveIntentClassification (de)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 32.1049092131809
    - type: f1
      value: 29.794603179718106
    - type: f1_weighted
      value: 30.137050786689766
    - type: main_score
      value: 32.1049092131809
    task:
      type: Classification
  - dataset:
      config: tr
      name: MTEB MassiveIntentClassification (tr)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 27.562205783456626
    - type: f1
      value: 25.683266426146687
    - type: f1_weighted
      value: 25.803636686733057
    - type: main_score
      value: 27.562205783456626
    task:
      type: Classification
  - dataset:
      config: pt
      name: MTEB MassiveIntentClassification (pt)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 34.347679892400805
    - type: f1
      value: 31.465774161046767
    - type: f1_weighted
      value: 31.735356981669327
    - type: main_score
      value: 34.347679892400805
    task:
      type: Classification
  - dataset:
      config: sq
      name: MTEB MassiveIntentClassification (sq)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 32.38063214525891
    - type: f1
      value: 29.53168994128031
    - type: f1_weighted
      value: 30.112896935570273
    - type: main_score
      value: 32.38063214525891
    task:
      type: Classification
  - dataset:
      config: zh-TW
      name: MTEB MassiveIntentClassification (zh-TW)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 6.809011432414256
    - type: f1
      value: 5.205218706422693
    - type: f1_weighted
      value: 5.178287349465675
    - type: main_score
      value: 6.809011432414256
    task:
      type: Classification
  - dataset:
      config: hy
      name: MTEB MassiveIntentClassification (hy)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.723604572965703
    - type: f1
      value: 0.6429150866665544
    - type: f1_weighted
      value: 0.9113227866994432
    - type: main_score
      value: 2.723604572965703
    task:
      type: Classification
  - dataset:
      config: da
      name: MTEB MassiveIntentClassification (da)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 33.95427034297243
    - type: f1
      value: 32.204428726904936
    - type: f1_weighted
      value: 32.47064251083498
    - type: main_score
      value: 33.95427034297243
    task:
      type: Classification
  - dataset:
      config: af
      name: MTEB MassiveIntentClassification (af)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 30.403496973772697
    - type: f1
      value: 27.814640020382342
    - type: f1_weighted
      value: 29.552471475522786
    - type: main_score
      value: 30.403496973772697
    task:
      type: Classification
  - dataset:
      config: ar
      name: MTEB MassiveIntentClassification (ar)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 3.796234028244788
    - type: f1
      value: 2.4115955159178712
    - type: f1_weighted
      value: 2.9705530799117428
    - type: main_score
      value: 3.796234028244788
    task:
      type: Classification
  - dataset:
      config: jv
      name: MTEB MassiveIntentClassification (jv)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 28.533960995292528
    - type: f1
      value: 26.21221777741412
    - type: f1_weighted
      value: 27.072811075990217
    - type: main_score
      value: 28.533960995292528
    task:
      type: Classification
  - dataset:
      config: te
      name: MTEB MassiveIntentClassification (te)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.2125084061869535
    - type: f1
      value: 1.0173733514352028
    - type: f1_weighted
      value: 1.316987953476142
    - type: main_score
      value: 2.2125084061869535
    task:
      type: Classification
  - dataset:
      config: tl
      name: MTEB MassiveIntentClassification (tl)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 32.017484868863484
    - type: f1
      value: 29.32295890060929
    - type: f1_weighted
      value: 29.657369574195414
    - type: main_score
      value: 32.017484868863484
    task:
      type: Classification
  - dataset:
      config: sw
      name: MTEB MassiveIntentClassification (sw)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 27.790854068594484
    - type: f1
      value: 26.66461334490106
    - type: f1_weighted
      value: 26.3309301465354
    - type: main_score
      value: 27.790854068594484
    task:
      type: Classification
  - dataset:
      config: ja
      name: MTEB MassiveIntentClassification (ja)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 5.611970410221924
    - type: f1
      value: 3.949675565526302
    - type: f1_weighted
      value: 3.8008532811790516
    - type: main_score
      value: 5.611970410221924
    task:
      type: Classification
  - dataset:
      config: ms
      name: MTEB MassiveIntentClassification (ms)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 28.940820443846675
    - type: f1
      value: 26.913943613442726
    - type: f1_weighted
      value: 27.58112937211184
    - type: main_score
      value: 28.940820443846675
    task:
      type: Classification
  - dataset:
      config: nb
      name: MTEB MassiveIntentClassification (nb)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 32.29993275050437
    - type: f1
      value: 30.38953729738546
    - type: f1_weighted
      value: 30.973971090234315
    - type: main_score
      value: 32.29993275050437
    task:
      type: Classification
  - dataset:
      config: fi
      name: MTEB MassiveIntentClassification (fi)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 31.13315400134499
    - type: f1
      value: 28.151659309577315
    - type: f1_weighted
      value: 28.919992380957805
    - type: main_score
      value: 31.13315400134499
    task:
      type: Classification
  - dataset:
      config: id
      name: MTEB MassiveIntentClassification (id)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 33.56422326832549
    - type: f1
      value: 32.13999124730796
    - type: f1_weighted
      value: 31.821742347727334
    - type: main_score
      value: 33.56422326832549
    task:
      type: Classification
  - dataset:
      config: cy
      name: MTEB MassiveIntentClassification (cy)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 31.68123739071957
    - type: f1
      value: 28.08132049625695
    - type: f1_weighted
      value: 30.136632177167293
    - type: main_score
      value: 31.68123739071957
    task:
      type: Classification
  - dataset:
      config: sl
      name: MTEB MassiveIntentClassification (sl)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 31.388702084734366
    - type: f1
      value: 30.06510634561652
    - type: f1_weighted
      value: 29.575793355168027
    - type: main_score
      value: 31.388702084734366
    task:
      type: Classification
  - dataset:
      config: es
      name: MTEB MassiveIntentClassification (es)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 31.032279757901815
    - type: f1
      value: 30.20555955874916
    - type: f1_weighted
      value: 28.87618616461917
    - type: main_score
      value: 31.032279757901815
    task:
      type: Classification
  - dataset:
      config: bn
      name: MTEB MassiveIntentClassification (bn)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 3.0766644250168125
    - type: f1
      value: 1.1659097449170488
    - type: f1_weighted
      value: 1.6261385516847686
    - type: main_score
      value: 3.0766644250168125
    task:
      type: Classification
  - dataset:
      config: sv
      name: MTEB MassiveIntentClassification (sv)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 30.22864828513786
    - type: f1
      value: 29.514038012557155
    - type: f1_weighted
      value: 28.79006788550934
    - type: main_score
      value: 30.22864828513786
    task:
      type: Classification
  - dataset:
      config: ru
      name: MTEB MassiveIntentClassification (ru)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 57.97915265635507
    - type: f1
      value: 56.5014953445001
    - type: f1_weighted
      value: 56.64147015986123
    - type: main_score
      value: 57.97915265635507
    task:
      type: Classification
  - dataset:
      config: az
      name: MTEB MassiveIntentClassification (az)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 23.577673167451245
    - type: f1
      value: 23.44310534002699
    - type: f1_weighted
      value: 22.73388843513862
    - type: main_score
      value: 23.577673167451245
    task:
      type: Classification
  - dataset:
      config: it
      name: MTEB MassiveIntentClassification (it)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 35.24209818426362
    - type: f1
      value: 34.17643389765681
    - type: f1_weighted
      value: 31.88705168526876
    - type: main_score
      value: 35.24209818426362
    task:
      type: Classification
  - dataset:
      config: pl
      name: MTEB MassiveIntentClassification (pl)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 26.815736381977135
    - type: f1
      value: 23.59490629738082
    - type: f1_weighted
      value: 24.824019034766742
    - type: main_score
      value: 26.815736381977135
    task:
      type: Classification
  - dataset:
      config: vi
      name: MTEB MassiveIntentClassification (vi)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 23.71889710827169
    - type: f1
      value: 20.9474996841838
    - type: f1_weighted
      value: 21.8696712485011
    - type: main_score
      value: 23.71889710827169
    task:
      type: Classification
  - dataset:
      config: ta
      name: MTEB MassiveIntentClassification (ta)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 1.4996637525218561
    - type: f1
      value: 0.3621176226135693
    - type: f1_weighted
      value: 0.40253328041710507
    - type: main_score
      value: 1.4996637525218561
    task:
      type: Classification
  - dataset:
      config: he
      name: MTEB MassiveIntentClassification (he)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.2461331540013454
    - type: f1
      value: 0.590566331230622
    - type: f1_weighted
      value: 0.6162176049666722
    - type: main_score
      value: 2.2461331540013454
    task:
      type: Classification
  - dataset:
      config: nl
      name: MTEB MassiveIntentClassification (nl)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 32.43779421654338
    - type: f1
      value: 29.65516413448003
    - type: f1_weighted
      value: 30.056107103546008
    - type: main_score
      value: 32.43779421654338
    task:
      type: Classification
  - dataset:
      config: km
      name: MTEB MassiveIntentClassification (km)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 5.137861466039005
    - type: f1
      value: 1.5034651435201778
    - type: f1_weighted
      value: 1.8580225168667703
    - type: main_score
      value: 5.137861466039005
    task:
      type: Classification
  - dataset:
      config: zh-CN
      name: MTEB MassiveIntentClassification (zh-CN)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 5.15002459419577
    - type: f1
      value: 3.2849878732080238
    - type: f1_weighted
      value: 3.171516129361724
    - type: main_score
      value: 5.15002459419577
    task:
      type: Classification
  - dataset:
      config: ko
      name: MTEB MassiveIntentClassification (ko)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.3610427939006393
    - type: f1
      value: 0.6344240632132025
    - type: f1_weighted
      value: 0.8741011326135733
    - type: main_score
      value: 2.3610427939006393
    task:
      type: Classification
  - dataset:
      config: hi
      name: MTEB MassiveIntentClassification (hi)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.4299065420560746
    - type: f1
      value: 1.1990062972384772
    - type: f1_weighted
      value: 1.2846405130538945
    - type: main_score
      value: 2.4299065420560746
    task:
      type: Classification
  - dataset:
      config: kn
      name: MTEB MassiveIntentClassification (kn)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.100344318740777
    - type: f1
      value: 1.0691096895187684
    - type: f1_weighted
      value: 1.0245515267986838
    - type: main_score
      value: 2.100344318740777
    task:
      type: Classification
  - dataset:
      config: ka
      name: MTEB MassiveIntentClassification (ka)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.144613871126414
    - type: f1
      value: 0.38751721719666626
    - type: f1_weighted
      value: 0.5494302003085859
    - type: main_score
      value: 2.144613871126414
    task:
      type: Classification
  - dataset:
      config: am
      name: MTEB MassiveIntentClassification (am)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.1347761928184945
    - type: f1
      value: 0.7186972868374003
    - type: f1_weighted
      value: 0.8692320111678621
    - type: main_score
      value: 2.1347761928184945
    task:
      type: Classification
  - dataset:
      config: my
      name: MTEB MassiveIntentClassification (my)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 3.9744220363994094
    - type: f1
      value: 1.320159702083562
    - type: f1_weighted
      value: 1.6615339662178419
    - type: main_score
      value: 3.9744220363994094
    task:
      type: Classification
  - dataset:
      config: el
      name: MTEB MassiveIntentClassification (el)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 8.740777176586326
    - type: f1
      value: 4.625508580628892
    - type: f1_weighted
      value: 5.910937912610004
    - type: main_score
      value: 8.740777176586326
    task:
      type: Classification
  - dataset:
      config: lv
      name: MTEB MassiveIntentClassification (lv)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 22.056074766355138
    - type: f1
      value: 20.067449871163735
    - type: f1_weighted
      value: 20.679581641637213
    - type: main_score
      value: 22.056074766355138
    task:
      type: Classification
  - dataset:
      config: ml
      name: MTEB MassiveIntentClassification (ml)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.287260206591244
    - type: f1
      value: 0.5144479181790914
    - type: f1_weighted
      value: 0.7532382956194585
    - type: main_score
      value: 2.287260206591244
    task:
      type: Classification
  - dataset:
      config: mn
      name: MTEB MassiveIntentClassification (mn)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 28.514510575504183
    - type: f1
      value: 27.670683007330656
    - type: f1_weighted
      value: 26.797727875405965
    - type: main_score
      value: 28.514510575504183
    task:
      type: Classification
  - dataset:
      config: ur
      name: MTEB MassiveIntentClassification (ur)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.5528775209050663
    - type: f1
      value: 1.5528439347982526
    - type: f1_weighted
      value: 1.59863069765228
    - type: main_score
      value: 2.5528775209050663
    task:
      type: Classification
  - dataset:
      config: fa
      name: MTEB MassiveIntentClassification (fa)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 3.1578947368421053
    - type: f1
      value: 0.612147286970534
    - type: f1_weighted
      value: 0.9311100758788083
    - type: main_score
      value: 3.1578947368421053
    task:
      type: Classification
  - dataset:
      config: ro
      name: MTEB MassiveIntentClassification (ro)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 30.472208558780135
    - type: f1
      value: 28.570236227937524
    - type: f1_weighted
      value: 29.26182782217857
    - type: main_score
      value: 30.472208558780135
    task:
      type: Classification
  - dataset:
      config: is
      name: MTEB MassiveIntentClassification (is)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 24.12690605017216
    - type: f1
      value: 21.730073248467978
    - type: f1_weighted
      value: 23.3232094260056
    - type: main_score
      value: 24.12690605017216
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveIntentClassification (en)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 50.6837186424004
    - type: f1
      value: 46.24633043195857
    - type: f1_weighted
      value: 49.89222156091109
    - type: main_score
      value: 50.6837186424004
    task:
      type: Classification
  - dataset:
      config: hu
      name: MTEB MassiveIntentClassification (hu)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 24.869650762420065
    - type: f1
      value: 22.646829281311646
    - type: f1_weighted
      value: 23.75607068147335
    - type: main_score
      value: 24.869650762420065
    task:
      type: Classification
  - dataset:
      config: fr
      name: MTEB MassiveIntentClassification (fr)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 30.83620265617314
    - type: f1
      value: 30.12388095110573
    - type: f1_weighted
      value: 29.755084946082466
    - type: main_score
      value: 30.83620265617314
    task:
      type: Classification
  - dataset:
      config: th
      name: MTEB MassiveIntentClassification (th)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 3.7924249877029017
    - type: f1
      value: 1.3490081402255192
    - type: f1_weighted
      value: 1.1964792923823864
    - type: main_score
      value: 3.7924249877029017
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB MassiveIntentClassification (de)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 30.85095917363502
    - type: f1
      value: 28.76898470499743
    - type: f1_weighted
      value: 29.742721084026552
    - type: main_score
      value: 30.85095917363502
    task:
      type: Classification
  - dataset:
      config: tr
      name: MTEB MassiveIntentClassification (tr)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 26.22233152975898
    - type: f1
      value: 24.13532374526957
    - type: f1_weighted
      value: 24.801681753477833
    - type: main_score
      value: 26.22233152975898
    task:
      type: Classification
  - dataset:
      config: pt
      name: MTEB MassiveIntentClassification (pt)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 33.85145105755042
    - type: f1
      value: 30.993852084910046
    - type: f1_weighted
      value: 31.47706557692265
    - type: main_score
      value: 33.85145105755042
    task:
      type: Classification
  - dataset:
      config: sq
      name: MTEB MassiveIntentClassification (sq)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 31.69699950811608
    - type: f1
      value: 28.43551777754717
    - type: f1_weighted
      value: 29.35991647173387
    - type: main_score
      value: 31.69699950811608
    task:
      type: Classification
  - dataset:
      config: zh-TW
      name: MTEB MassiveIntentClassification (zh-TW)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 6.296114117068371
    - type: f1
      value: 4.469538815411268
    - type: f1_weighted
      value: 4.470912934534107
    - type: main_score
      value: 6.296114117068371
    task:
      type: Classification
  - dataset:
      config: hy
      name: MTEB MassiveIntentClassification (hy)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.6660108214461387
    - type: f1
      value: 0.7095128645283928
    - type: f1_weighted
      value: 0.900359447084975
    - type: main_score
      value: 2.6660108214461387
    task:
      type: Classification
  - dataset:
      config: da
      name: MTEB MassiveIntentClassification (da)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 32.24790949335957
    - type: f1
      value: 30.09602016401104
    - type: f1_weighted
      value: 31.27365296679004
    - type: main_score
      value: 32.24790949335957
    task:
      type: Classification
  - dataset:
      config: af
      name: MTEB MassiveIntentClassification (af)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 29.85243482538121
    - type: f1
      value: 27.02898547703625
    - type: f1_weighted
      value: 29.19825733648402
    - type: main_score
      value: 29.85243482538121
    task:
      type: Classification
  - dataset:
      config: ar
      name: MTEB MassiveIntentClassification (ar)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 3.413674372848008
    - type: f1
      value: 2.3814730307183596
    - type: f1_weighted
      value: 2.758592436005351
    - type: main_score
      value: 3.413674372848008
    task:
      type: Classification
  - dataset:
      config: jv
      name: MTEB MassiveIntentClassification (jv)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 27.59960649286769
    - type: f1
      value: 25.169829835887036
    - type: f1_weighted
      value: 26.378021821617065
    - type: main_score
      value: 27.59960649286769
    task:
      type: Classification
  - dataset:
      config: te
      name: MTEB MassiveIntentClassification (te)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.0363994097393014
    - type: f1
      value: 0.7934004289138196
    - type: f1_weighted
      value: 1.1834679007875544
    - type: main_score
      value: 2.0363994097393014
    task:
      type: Classification
  - dataset:
      config: tl
      name: MTEB MassiveIntentClassification (tl)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 31.43630103295622
    - type: f1
      value: 28.28710817943075
    - type: f1_weighted
      value: 29.47693147061905
    - type: main_score
      value: 31.43630103295622
    task:
      type: Classification
  - dataset:
      config: sw
      name: MTEB MassiveIntentClassification (sw)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 27.515986227250366
    - type: f1
      value: 25.65654395144761
    - type: f1_weighted
      value: 26.414094210360055
    - type: main_score
      value: 27.515986227250366
    task:
      type: Classification
  - dataset:
      config: ja
      name: MTEB MassiveIntentClassification (ja)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 5.986227250368913
    - type: f1
      value: 3.9449730568824433
    - type: f1_weighted
      value: 3.8102259721047833
    - type: main_score
      value: 5.986227250368913
    task:
      type: Classification
  - dataset:
      config: ms
      name: MTEB MassiveIntentClassification (ms)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 28.155435317265127
    - type: f1
      value: 25.708172487585202
    - type: f1_weighted
      value: 27.024916707588677
    - type: main_score
      value: 28.155435317265127
    task:
      type: Classification
  - dataset:
      config: nb
      name: MTEB MassiveIntentClassification (nb)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 31.485489424495817
    - type: f1
      value: 29.47639008406045
    - type: f1_weighted
      value: 30.377692398014027
    - type: main_score
      value: 31.485489424495817
    task:
      type: Classification
  - dataset:
      config: fi
      name: MTEB MassiveIntentClassification (fi)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 30.403344810624695
    - type: f1
      value: 26.82843832763937
    - type: f1_weighted
      value: 28.11110907470959
    - type: main_score
      value: 30.403344810624695
    task:
      type: Classification
  - dataset:
      config: id
      name: MTEB MassiveIntentClassification (id)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 32.70044269552386
    - type: f1
      value: 30.910774335551594
    - type: f1_weighted
      value: 31.371749140831422
    - type: main_score
      value: 32.70044269552386
    task:
      type: Classification
  - dataset:
      config: cy
      name: MTEB MassiveIntentClassification (cy)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 29.429414658140686
    - type: f1
      value: 25.594886516936256
    - type: f1_weighted
      value: 28.392261199556877
    - type: main_score
      value: 29.429414658140686
    task:
      type: Classification
  - dataset:
      config: sl
      name: MTEB MassiveIntentClassification (sl)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 29.636005902606982
    - type: f1
      value: 28.287023938527234
    - type: f1_weighted
      value: 27.924913519954554
    - type: main_score
      value: 29.636005902606982
    task:
      type: Classification
  - dataset:
      config: es
      name: MTEB MassiveIntentClassification (es)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 30.63453025086079
    - type: f1
      value: 29.5921601385162
    - type: f1_weighted
      value: 28.58410607526952
    - type: main_score
      value: 30.63453025086079
    task:
      type: Classification
  - dataset:
      config: bn
      name: MTEB MassiveIntentClassification (bn)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.867683226758485
    - type: f1
      value: 1.0374630680286294
    - type: f1_weighted
      value: 1.3261691151267023
    - type: main_score
      value: 2.867683226758485
    task:
      type: Classification
  - dataset:
      config: sv
      name: MTEB MassiveIntentClassification (sv)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 29.754058042302017
    - type: f1
      value: 27.921243093926957
    - type: f1_weighted
      value: 28.600526975101815
    - type: main_score
      value: 29.754058042302017
    task:
      type: Classification
  - dataset:
      config: ru
      name: MTEB MassiveIntentClassification (ru)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 58.06197737333989
    - type: f1
      value: 53.92404816772661
    - type: f1_weighted
      value: 56.72057857737771
    - type: main_score
      value: 58.06197737333989
    task:
      type: Classification
  - dataset:
      config: az
      name: MTEB MassiveIntentClassification (az)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 22.725036891293655
    - type: f1
      value: 22.05764593465915
    - type: f1_weighted
      value: 22.36326529771844
    - type: main_score
      value: 22.725036891293655
    task:
      type: Classification
  - dataset:
      config: it
      name: MTEB MassiveIntentClassification (it)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 34.57943925233645
    - type: f1
      value: 33.54269802516337
    - type: f1_weighted
      value: 31.59380780190696
    - type: main_score
      value: 34.57943925233645
    task:
      type: Classification
  - dataset:
      config: pl
      name: MTEB MassiveIntentClassification (pl)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 26.050172159370387
    - type: f1
      value: 23.37018289487783
    - type: f1_weighted
      value: 24.52891801190779
    - type: main_score
      value: 26.050172159370387
    task:
      type: Classification
  - dataset:
      config: vi
      name: MTEB MassiveIntentClassification (vi)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 23.10378750614855
    - type: f1
      value: 19.634766811442688
    - type: f1_weighted
      value: 21.39922163237278
    - type: main_score
      value: 23.10378750614855
    task:
      type: Classification
  - dataset:
      config: ta
      name: MTEB MassiveIntentClassification (ta)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 1.382193802262666
    - type: f1
      value: 0.2962201919122291
    - type: f1_weighted
      value: 0.36568543738308745
    - type: main_score
      value: 1.382193802262666
    task:
      type: Classification
  - dataset:
      config: he
      name: MTEB MassiveIntentClassification (he)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 2.0560747663551404
    - type: f1
      value: 0.4742414282381403
    - type: f1_weighted
      value: 0.5861893507001308
    - type: main_score
      value: 2.0560747663551404
    task:
      type: Classification
  - dataset:
      config: nl
      name: MTEB MassiveIntentClassification (nl)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 30.5115592720118
    - type: f1
      value: 27.61045064110582
    - type: f1_weighted
      value: 28.987990654116114
    - type: main_score
      value: 30.5115592720118
    task:
      type: Classification
  - dataset:
      config: km
      name: MTEB MassiveIntentClassification (km)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: validation
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 4.377766847024103
    - type: f1
      value: 1.2676703377671132
    - type: f1_weighted
      value: 1.426174554035529
    - type: main_score
      value: 4.377766847024103
    task:
      type: Classification
  - dataset:
      config: zh-CN
      name: MTEB MassiveScenarioClassification (zh-CN)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 10.601882985877605
    - type: f1
      value: 6.8689500634035365
    - type: f1_weighted
      value: 8.260029142337519
    - type: main_score
      value: 10.601882985877605
    task:
      type: Classification
  - dataset:
      config: ko
      name: MTEB MassiveScenarioClassification (ko)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 5.62542030934768
    - type: f1
      value: 1.9399090161521315
    - type: f1_weighted
      value: 1.7790298099358886
    - type: main_score
      value: 5.62542030934768
    task:
      type: Classification
  - dataset:
      config: hi
      name: MTEB MassiveScenarioClassification (hi)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 7.407531943510423
    - type: f1
      value: 3.622072056826428
    - type: f1_weighted
      value: 3.444172662951229
    - type: main_score
      value: 7.407531943510423
    task:
      type: Classification
  - dataset:
      config: kn
      name: MTEB MassiveScenarioClassification (kn)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 7.602555480833894
    - type: f1
      value: 3.9001734711485803
    - type: f1_weighted
      value: 3.4912256692008397
    - type: main_score
      value: 7.602555480833894
    task:
      type: Classification
  - dataset:
      config: ka
      name: MTEB MassiveScenarioClassification (ka)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 7.010759919300605
    - type: f1
      value: 2.1485666974093878
    - type: f1_weighted
      value: 2.3739456428263477
    - type: main_score
      value: 7.010759919300605
    task:
      type: Classification
  - dataset:
      config: am
      name: MTEB MassiveScenarioClassification (am)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 7.679892400806995
    - type: f1
      value: 2.728187383195907
    - type: f1_weighted
      value: 3.0454310752856353
    - type: main_score
      value: 7.679892400806995
    task:
      type: Classification
  - dataset:
      config: my
      name: MTEB MassiveScenarioClassification (my)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 10.729657027572292
    - type: f1
      value: 4.138439669406968
    - type: f1_weighted
      value: 4.843092536146883
    - type: main_score
      value: 10.729657027572292
    task:
      type: Classification
  - dataset:
      config: el
      name: MTEB MassiveScenarioClassification (el)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 17.952252858103563
    - type: f1
      value: 12.418135741505608
    - type: f1_weighted
      value: 15.228054842385186
    - type: main_score
      value: 17.952252858103563
    task:
      type: Classification
  - dataset:
      config: lv
      name: MTEB MassiveScenarioClassification (lv)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 29.29388029589779
    - type: f1
      value: 25.95638727776611
    - type: f1_weighted
      value: 27.82646328315652
    - type: main_score
      value: 29.29388029589779
    task:
      type: Classification
  - dataset:
      config: ml
      name: MTEB MassiveScenarioClassification (ml)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 6.923335574983189
    - type: f1
      value: 2.2338102382542795
    - type: f1_weighted
      value: 2.837475945704109
    - type: main_score
      value: 6.923335574983189
    task:
      type: Classification
  - dataset:
      config: mn
      name: MTEB MassiveScenarioClassification (mn)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 33.70208473436449
    - type: f1
      value: 31.451013524608147
    - type: f1_weighted
      value: 33.4571016718763
    - type: main_score
      value: 33.70208473436449
    task:
      type: Classification
  - dataset:
      config: ur
      name: MTEB MassiveScenarioClassification (ur)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 8.530598520511097
    - type: f1
      value: 3.993356806346034
    - type: f1_weighted
      value: 4.275297414153249
    - type: main_score
      value: 8.530598520511097
    task:
      type: Classification
  - dataset:
      config: fa
      name: MTEB MassiveScenarioClassification (fa)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 6.6240753194351045
    - type: f1
      value: 2.559179690443991
    - type: f1_weighted
      value: 2.8775036329690353
    - type: main_score
      value: 6.6240753194351045
    task:
      type: Classification
  - dataset:
      config: ro
      name: MTEB MassiveScenarioClassification (ro)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 40.01681237390719
    - type: f1
      value: 36.15548220887307
    - type: f1_weighted
      value: 38.91143847106075
    - type: main_score
      value: 40.01681237390719
    task:
      type: Classification
  - dataset:
      config: is
      name: MTEB MassiveScenarioClassification (is)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 33.10356422326833
    - type: f1
      value: 29.87073203020746
    - type: f1_weighted
      value: 32.736926298821786
    - type: main_score
      value: 33.10356422326833
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
      value: 61.291190316072644
    - type: f1
      value: 58.09487277036398
    - type: f1_weighted
      value: 60.52223749579593
    - type: main_score
      value: 61.291190316072644
    task:
      type: Classification
  - dataset:
      config: hu
      name: MTEB MassiveScenarioClassification (hu)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 36.40551445864156
    - type: f1
      value: 32.12815170334265
    - type: f1_weighted
      value: 35.421611675898745
    - type: main_score
      value: 36.40551445864156
    task:
      type: Classification
  - dataset:
      config: fr
      name: MTEB MassiveScenarioClassification (fr)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 42.90181573638198
    - type: f1
      value: 39.00450485042174
    - type: f1_weighted
      value: 41.74577968212385
    - type: main_score
      value: 42.90181573638198
    task:
      type: Classification
  - dataset:
      config: th
      name: MTEB MassiveScenarioClassification (th)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 8.261600537995966
    - type: f1
      value: 3.8946817615361597
    - type: f1_weighted
      value: 3.7437491646031926
    - type: main_score
      value: 8.261600537995966
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB MassiveScenarioClassification (de)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 42.07128446536651
    - type: f1
      value: 38.28996078984755
    - type: f1_weighted
      value: 41.04738811504033
    - type: main_score
      value: 42.07128446536651
    task:
      type: Classification
  - dataset:
      config: tr
      name: MTEB MassiveScenarioClassification (tr)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 34.845326160053794
    - type: f1
      value: 32.52170618407094
    - type: f1_weighted
      value: 33.35658510579412
    - type: main_score
      value: 34.845326160053794
    task:
      type: Classification
  - dataset:
      config: pt
      name: MTEB MassiveScenarioClassification (pt)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 40.78681909885676
    - type: f1
      value: 37.33575502776686
    - type: f1_weighted
      value: 38.66002021299529
    - type: main_score
      value: 40.78681909885676
    task:
      type: Classification
  - dataset:
      config: sq
      name: MTEB MassiveScenarioClassification (sq)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 42.65635507733692
    - type: f1
      value: 38.53947437411434
    - type: f1_weighted
      value: 41.52520693995739
    - type: main_score
      value: 42.65635507733692
    task:
      type: Classification
  - dataset:
      config: zh-TW
      name: MTEB MassiveScenarioClassification (zh-TW)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 11.926698049764628
    - type: f1
      value: 8.724194514820493
    - type: f1_weighted
      value: 10.266244979280504
    - type: main_score
      value: 11.926698049764628
    task:
      type: Classification
  - dataset:
      config: hy
      name: MTEB MassiveScenarioClassification (hy)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 8.779421654337593
    - type: f1
      value: 3.47659510611439
    - type: f1_weighted
      value: 4.092370736159162
    - type: main_score
      value: 8.779421654337593
    task:
      type: Classification
  - dataset:
      config: da
      name: MTEB MassiveScenarioClassification (da)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 43.6852723604573
    - type: f1
      value: 39.338012150585094
    - type: f1_weighted
      value: 43.3756140521009
    - type: main_score
      value: 43.6852723604573
    task:
      type: Classification
  - dataset:
      config: af
      name: MTEB MassiveScenarioClassification (af)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 40.83725622057835
    - type: f1
      value: 36.67993326074695
    - type: f1_weighted
      value: 40.73536387442413
    - type: main_score
      value: 40.83725622057835
    task:
      type: Classification
  - dataset:
      config: ar
      name: MTEB MassiveScenarioClassification (ar)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 11.859448554135843
    - type: f1
      value: 6.502577103628851
    - type: f1_weighted
      value: 9.922384035467028
    - type: main_score
      value: 11.859448554135843
    task:
      type: Classification
  - dataset:
      config: jv
      name: MTEB MassiveScenarioClassification (jv)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 37.22932078009414
    - type: f1
      value: 34.37198836784653
    - type: f1_weighted
      value: 36.41682430619207
    - type: main_score
      value: 37.22932078009414
    task:
      type: Classification
  - dataset:
      config: te
      name: MTEB MassiveScenarioClassification (te)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 6.909885675857431
    - type: f1
      value: 2.659712889039866
    - type: f1_weighted
      value: 3.315252295282912
    - type: main_score
      value: 6.909885675857431
    task:
      type: Classification
  - dataset:
      config: tl
      name: MTEB MassiveScenarioClassification (tl)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 38.157363819771355
    - type: f1
      value: 33.871383306341926
    - type: f1_weighted
      value: 37.16844466757229
    - type: main_score
      value: 38.157363819771355
    task:
      type: Classification
  - dataset:
      config: sw
      name: MTEB MassiveScenarioClassification (sw)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 35.65904505716207
    - type: f1
      value: 32.95848641686319
    - type: f1_weighted
      value: 33.46347965861419
    - type: main_score
      value: 35.65904505716207
    task:
      type: Classification
  - dataset:
      config: ja
      name: MTEB MassiveScenarioClassification (ja)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 10.601882985877605
    - type: f1
      value: 8.05499004226519
    - type: f1_weighted
      value: 8.12291817923475
    - type: main_score
      value: 10.601882985877605
    task:
      type: Classification
  - dataset:
      config: ms
      name: MTEB MassiveScenarioClassification (ms)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 38.97108271687962
    - type: f1
      value: 34.19920488698337
    - type: f1_weighted
      value: 37.406365439450006
    - type: main_score
      value: 38.97108271687962
    task:
      type: Classification
  - dataset:
      config: nb
      name: MTEB MassiveScenarioClassification (nb)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 39.04505716207128
    - type: f1
      value: 35.380977049887605
    - type: f1_weighted
      value: 38.79082603370826
    - type: main_score
      value: 39.04505716207128
    task:
      type: Classification
  - dataset:
      config: fi
      name: MTEB MassiveScenarioClassification (fi)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 35.18829858776059
    - type: f1
      value: 30.972699263943966
    - type: f1_weighted
      value: 34.66929745941575
    - type: main_score
      value: 35.18829858776059
    task:
      type: Classification
  - dataset:
      config: id
      name: MTEB MassiveScenarioClassification (id)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 39.53934095494284
    - type: f1
      value: 37.19939485401421
    - type: f1_weighted
      value: 38.163540271879384
    - type: main_score
      value: 39.53934095494284
    task:
      type: Classification
  - dataset:
      config: cy
      name: MTEB MassiveScenarioClassification (cy)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 39.85205110961668
    - type: f1
      value: 34.567211938088086
    - type: f1_weighted
      value: 38.93137139872493
    - type: main_score
      value: 39.85205110961668
    task:
      type: Classification
  - dataset:
      config: sl
      name: MTEB MassiveScenarioClassification (sl)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 35.978480161398785
    - type: f1
      value: 33.70493150778863
    - type: f1_weighted
      value: 34.89613180942136
    - type: main_score
      value: 35.978480161398785
    task:
      type: Classification
  - dataset:
      config: es
      name: MTEB MassiveScenarioClassification (es)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 37.12508406186954
    - type: f1
      value: 34.14887874344704
    - type: f1_weighted
      value: 35.491336292250615
    - type: main_score
      value: 37.12508406186954
    task:
      type: Classification
  - dataset:
      config: bn
      name: MTEB MassiveScenarioClassification (bn)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 8.846671149966376
    - type: f1
      value: 3.772079613264656
    - type: f1_weighted
      value: 4.569880079881123
    - type: main_score
      value: 8.846671149966376
    task:
      type: Classification
  - dataset:
      config: sv
      name: MTEB MassiveScenarioClassification (sv)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 36.11970410221924
    - type: f1
      value: 33.64741825888341
    - type: f1_weighted
      value: 36.04738800166304
    - type: main_score
      value: 36.11970410221924
    task:
      type: Classification
  - dataset:
      config: ru
      name: MTEB MassiveScenarioClassification (ru)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 62.89509078681911
    - type: f1
      value: 62.296937620668366
    - type: f1_weighted
      value: 61.50844245234364
    - type: main_score
      value: 62.89509078681911
    task:
      type: Classification
  - dataset:
      config: az
      name: MTEB MassiveScenarioClassification (az)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 30.31607262945528
    - type: f1
      value: 27.373913596444382
    - type: f1_weighted
      value: 29.154743431705356
    - type: main_score
      value: 30.31607262945528
    task:
      type: Classification
  - dataset:
      config: it
      name: MTEB MassiveScenarioClassification (it)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 42.68997982515131
    - type: f1
      value: 39.34921574451304
    - type: f1_weighted
      value: 41.39971354124732
    - type: main_score
      value: 42.68997982515131
    task:
      type: Classification
  - dataset:
      config: pl
      name: MTEB MassiveScenarioClassification (pl)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 31.62071284465367
    - type: f1
      value: 27.53427875798914
    - type: f1_weighted
      value: 30.442690748521006
    - type: main_score
      value: 31.62071284465367
    task:
      type: Classification
  - dataset:
      config: vi
      name: MTEB MassiveScenarioClassification (vi)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 31.889710827168795
    - type: f1
      value: 29.1527074423781
    - type: f1_weighted
      value: 29.84128781391531
    - type: main_score
      value: 31.889710827168795
    task:
      type: Classification
  - dataset:
      config: ta
      name: MTEB MassiveScenarioClassification (ta)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 7.007397444519166
    - type: f1
      value: 1.763256752893296
    - type: f1_weighted
      value: 2.3996756522652913
    - type: main_score
      value: 7.007397444519166
    task:
      type: Classification
  - dataset:
      config: he
      name: MTEB MassiveScenarioClassification (he)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 7.612642905178212
    - type: f1
      value: 2.0115132382174585
    - type: f1_weighted
      value: 2.8178938596974503
    - type: main_score
      value: 7.612642905178212
    task:
      type: Classification
  - dataset:
      config: nl
      name: MTEB MassiveScenarioClassification (nl)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 40.93813046402152
    - type: f1
      value: 35.475977992563635
    - type: f1_weighted
      value: 40.249098836834044
    - type: main_score
      value: 40.93813046402152
    task:
      type: Classification
  - dataset:
      config: km
      name: MTEB MassiveScenarioClassification (km)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 8.510423671822462
    - type: f1
      value: 2.77822187113745
    - type: f1_weighted
      value: 3.488782507211019
    - type: main_score
      value: 8.510423671822462
    task:
      type: Classification
  - dataset:
      config: zh-CN
      name: MTEB MassiveScenarioClassification (zh-CN)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 10.560747663551401
    - type: f1
      value: 7.321692095226571
    - type: f1_weighted
      value: 8.136926309421098
    - type: main_score
      value: 10.560747663551401
    task:
      type: Classification
  - dataset:
      config: ko
      name: MTEB MassiveScenarioClassification (ko)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 5.622233152975899
    - type: f1
      value: 1.7454943918873769
    - type: f1_weighted
      value: 1.5544580080510706
    - type: main_score
      value: 5.622233152975899
    task:
      type: Classification
  - dataset:
      config: hi
      name: MTEB MassiveScenarioClassification (hi)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 7.50614854894245
    - type: f1
      value: 3.671558894965337
    - type: f1_weighted
      value: 3.6075123924941224
    - type: main_score
      value: 7.50614854894245
    task:
      type: Classification
  - dataset:
      config: kn
      name: MTEB MassiveScenarioClassification (kn)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 8.047220855878013
    - type: f1
      value: 4.199596683728984
    - type: f1_weighted
      value: 3.705979981207572
    - type: main_score
      value: 8.047220855878013
    task:
      type: Classification
  - dataset:
      config: ka
      name: MTEB MassiveScenarioClassification (ka)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 6.591244466305953
    - type: f1
      value: 1.9804826267181144
    - type: f1_weighted
      value: 2.1652032753558714
    - type: main_score
      value: 6.591244466305953
    task:
      type: Classification
  - dataset:
      config: am
      name: MTEB MassiveScenarioClassification (am)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 7.511067388096411
    - type: f1
      value: 2.641163180255864
    - type: f1_weighted
      value: 3.03599461945174
    - type: main_score
      value: 7.511067388096411
    task:
      type: Classification
  - dataset:
      config: my
      name: MTEB MassiveScenarioClassification (my)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 11.234628627643877
    - type: f1
      value: 4.53829675095688
    - type: f1_weighted
      value: 5.119828126415879
    - type: main_score
      value: 11.234628627643877
    task:
      type: Classification
  - dataset:
      config: el
      name: MTEB MassiveScenarioClassification (el)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 16.438760452533202
    - type: f1
      value: 12.026293516540374
    - type: f1_weighted
      value: 13.40697491103347
    - type: main_score
      value: 16.438760452533202
    task:
      type: Classification
  - dataset:
      config: lv
      name: MTEB MassiveScenarioClassification (lv)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 28.470241023118547
    - type: f1
      value: 26.06308403577423
    - type: f1_weighted
      value: 26.913188635640108
    - type: main_score
      value: 28.470241023118547
    task:
      type: Classification
  - dataset:
      config: ml
      name: MTEB MassiveScenarioClassification (ml)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 7.34874569601574
    - type: f1
      value: 2.163368202700301
    - type: f1_weighted
      value: 2.9794749471502735
    - type: main_score
      value: 7.34874569601574
    task:
      type: Classification
  - dataset:
      config: mn
      name: MTEB MassiveScenarioClassification (mn)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 33.482538121003444
    - type: f1
      value: 31.74224548475336
    - type: f1_weighted
      value: 32.974792871093996
    - type: main_score
      value: 33.482538121003444
    task:
      type: Classification
  - dataset:
      config: ur
      name: MTEB MassiveScenarioClassification (ur)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 8.735858337432365
    - type: f1
      value: 4.387957216974412
    - type: f1_weighted
      value: 4.487011850573568
    - type: main_score
      value: 8.735858337432365
    task:
      type: Classification
  - dataset:
      config: fa
      name: MTEB MassiveScenarioClassification (fa)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 6.8027545499262185
    - type: f1
      value: 2.724940339247371
    - type: f1_weighted
      value: 2.9191909608862248
    - type: main_score
      value: 6.8027545499262185
    task:
      type: Classification
  - dataset:
      config: ro
      name: MTEB MassiveScenarioClassification (ro)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 39.77865223807182
    - type: f1
      value: 36.713842977439086
    - type: f1_weighted
      value: 38.411147363742614
    - type: main_score
      value: 39.77865223807182
    task:
      type: Classification
  - dataset:
      config: is
      name: MTEB MassiveScenarioClassification (is)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 32.611903590752576
    - type: f1
      value: 30.478777350564933
    - type: f1_weighted
      value: 32.33376716992967
    - type: main_score
      value: 32.611903590752576
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveScenarioClassification (en)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 60.81652729955731
    - type: f1
      value: 57.85686645797947
    - type: f1_weighted
      value: 59.96336225413508
    - type: main_score
      value: 60.81652729955731
    task:
      type: Classification
  - dataset:
      config: hu
      name: MTEB MassiveScenarioClassification (hu)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 35.041810132808656
    - type: f1
      value: 32.32895536298411
    - type: f1_weighted
      value: 34.08983039599136
    - type: main_score
      value: 35.041810132808656
    task:
      type: Classification
  - dataset:
      config: fr
      name: MTEB MassiveScenarioClassification (fr)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 42.4151500245942
    - type: f1
      value: 39.716877977971514
    - type: f1_weighted
      value: 40.98904556640093
    - type: main_score
      value: 42.4151500245942
    task:
      type: Classification
  - dataset:
      config: th
      name: MTEB MassiveScenarioClassification (th)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 8.253812100344318
    - type: f1
      value: 4.2941598559113645
    - type: f1_weighted
      value: 3.7137986151126743
    - type: main_score
      value: 8.253812100344318
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB MassiveScenarioClassification (de)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 40.65912444663059
    - type: f1
      value: 37.90162745459205
    - type: f1_weighted
      value: 39.942707376839756
    - type: main_score
      value: 40.65912444663059
    task:
      type: Classification
  - dataset:
      config: tr
      name: MTEB MassiveScenarioClassification (tr)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 33.85145105755042
    - type: f1
      value: 32.41363211826809
    - type: f1_weighted
      value: 32.696811929693745
    - type: main_score
      value: 33.85145105755042
    task:
      type: Classification
  - dataset:
      config: pt
      name: MTEB MassiveScenarioClassification (pt)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 40.22626660108214
    - type: f1
      value: 37.84448697275546
    - type: f1_weighted
      value: 37.82059370217246
    - type: main_score
      value: 40.22626660108214
    task:
      type: Classification
  - dataset:
      config: sq
      name: MTEB MassiveScenarioClassification (sq)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 42.06591244466306
    - type: f1
      value: 38.76214747335659
    - type: f1_weighted
      value: 40.65484003509404
    - type: main_score
      value: 42.06591244466306
    task:
      type: Classification
  - dataset:
      config: zh-TW
      name: MTEB MassiveScenarioClassification (zh-TW)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 11.682242990654206
    - type: f1
      value: 8.850699907144218
    - type: f1_weighted
      value: 9.655517346069553
    - type: main_score
      value: 11.682242990654206
    task:
      type: Classification
  - dataset:
      config: hy
      name: MTEB MassiveScenarioClassification (hy)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 8.52926709296606
    - type: f1
      value: 3.4189589714301167
    - type: f1_weighted
      value: 3.894511154092698
    - type: main_score
      value: 8.52926709296606
    task:
      type: Classification
  - dataset:
      config: da
      name: MTEB MassiveScenarioClassification (da)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 41.14117068371864
    - type: f1
      value: 38.08063702754415
    - type: f1_weighted
      value: 40.65305294882936
    - type: main_score
      value: 41.14117068371864
    task:
      type: Classification
  - dataset:
      config: af
      name: MTEB MassiveScenarioClassification (af)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 39.3654697491392
    - type: f1
      value: 36.43369907401146
    - type: f1_weighted
      value: 39.09920883835431
    - type: main_score
      value: 39.3654697491392
    task:
      type: Classification
  - dataset:
      config: ar
      name: MTEB MassiveScenarioClassification (ar)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 11.362518445646828
    - type: f1
      value: 6.2728348209099565
    - type: f1_weighted
      value: 8.903159425462325
    - type: main_score
      value: 11.362518445646828
    task:
      type: Classification
  - dataset:
      config: jv
      name: MTEB MassiveScenarioClassification (jv)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 36.246925725528776
    - type: f1
      value: 34.242775177193415
    - type: f1_weighted
      value: 34.90531238831363
    - type: main_score
      value: 36.246925725528776
    task:
      type: Classification
  - dataset:
      config: te
      name: MTEB MassiveScenarioClassification (te)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 6.861780619773734
    - type: f1
      value: 2.7017710457799873
    - type: f1_weighted
      value: 3.1681349264113137
    - type: main_score
      value: 6.861780619773734
    task:
      type: Classification
  - dataset:
      config: tl
      name: MTEB MassiveScenarioClassification (tl)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 38.17019183472701
    - type: f1
      value: 34.777811838185485
    - type: f1_weighted
      value: 36.90042555420213
    - type: main_score
      value: 38.17019183472701
    task:
      type: Classification
  - dataset:
      config: sw
      name: MTEB MassiveScenarioClassification (sw)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 35.32710280373832
    - type: f1
      value: 33.32826385073952
    - type: f1_weighted
      value: 33.388725291289916
    - type: main_score
      value: 35.32710280373832
    task:
      type: Classification
  - dataset:
      config: ja
      name: MTEB MassiveScenarioClassification (ja)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 11.20511559272012
    - type: f1
      value: 8.976181412932425
    - type: f1_weighted
      value: 8.576498601594645
    - type: main_score
      value: 11.20511559272012
    task:
      type: Classification
  - dataset:
      config: ms
      name: MTEB MassiveScenarioClassification (ms)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 38.85391047712739
    - type: f1
      value: 34.90571468739814
    - type: f1_weighted
      value: 36.82763280572209
    - type: main_score
      value: 38.85391047712739
    task:
      type: Classification
  - dataset:
      config: nb
      name: MTEB MassiveScenarioClassification (nb)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 38.052139695031975
    - type: f1
      value: 35.272001887507564
    - type: f1_weighted
      value: 37.42041278303434
    - type: main_score
      value: 38.052139695031975
    task:
      type: Classification
  - dataset:
      config: fi
      name: MTEB MassiveScenarioClassification (fi)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 34.500737825873095
    - type: f1
      value: 30.68780970737908
    - type: f1_weighted
      value: 33.716051134823
    - type: main_score
      value: 34.500737825873095
    task:
      type: Classification
  - dataset:
      config: id
      name: MTEB MassiveScenarioClassification (id)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 39.596655189375305
    - type: f1
      value: 37.72092200675893
    - type: f1_weighted
      value: 37.89234511492137
    - type: main_score
      value: 39.596655189375305
    task:
      type: Classification
  - dataset:
      config: cy
      name: MTEB MassiveScenarioClassification (cy)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 38.93261190359076
    - type: f1
      value: 34.67593293977394
    - type: f1_weighted
      value: 37.58144266593478
    - type: main_score
      value: 38.93261190359076
    task:
      type: Classification
  - dataset:
      config: sl
      name: MTEB MassiveScenarioClassification (sl)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 35.336940482046245
    - type: f1
      value: 34.06391073492543
    - type: f1_weighted
      value: 34.19964460077873
    - type: main_score
      value: 35.336940482046245
    task:
      type: Classification
  - dataset:
      config: es
      name: MTEB MassiveScenarioClassification (es)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 36.28135759960649
    - type: f1
      value: 33.98213113943637
    - type: f1_weighted
      value: 34.432683108706726
    - type: main_score
      value: 36.28135759960649
    task:
      type: Classification
  - dataset:
      config: bn
      name: MTEB MassiveScenarioClassification (bn)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 8.789965568125922
    - type: f1
      value: 3.615951273986677
    - type: f1_weighted
      value: 4.543124755655086
    - type: main_score
      value: 8.789965568125922
    task:
      type: Classification
  - dataset:
      config: sv
      name: MTEB MassiveScenarioClassification (sv)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 35.78947368421053
    - type: f1
      value: 33.641144471139874
    - type: f1_weighted
      value: 35.35509200878473
    - type: main_score
      value: 35.78947368421053
    task:
      type: Classification
  - dataset:
      config: ru
      name: MTEB MassiveScenarioClassification (ru)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 64.14658140678799
    - type: f1
      value: 63.45318114952019
    - type: f1_weighted
      value: 62.837233214870004
    - type: main_score
      value: 64.14658140678799
    task:
      type: Classification
  - dataset:
      config: az
      name: MTEB MassiveScenarioClassification (az)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 29.616330545991143
    - type: f1
      value: 27.89304924236733
    - type: f1_weighted
      value: 28.557344732597763
    - type: main_score
      value: 29.616330545991143
    task:
      type: Classification
  - dataset:
      config: it
      name: MTEB MassiveScenarioClassification (it)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 41.1952779144122
    - type: f1
      value: 38.70295863724121
    - type: f1_weighted
      value: 39.8087264213271
    - type: main_score
      value: 41.1952779144122
    task:
      type: Classification
  - dataset:
      config: pl
      name: MTEB MassiveScenarioClassification (pl)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 30.15248401377275
    - type: f1
      value: 27.24749237955316
    - type: f1_weighted
      value: 29.24459561389263
    - type: main_score
      value: 30.15248401377275
    task:
      type: Classification
  - dataset:
      config: vi
      name: MTEB MassiveScenarioClassification (vi)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 31.942941465814062
    - type: f1
      value: 29.238187005403976
    - type: f1_weighted
      value: 29.360530025850295
    - type: main_score
      value: 31.942941465814062
    task:
      type: Classification
  - dataset:
      config: ta
      name: MTEB MassiveScenarioClassification (ta)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 7.211018199704869
    - type: f1
      value: 1.858123064629565
    - type: f1_weighted
      value: 2.531232017204237
    - type: main_score
      value: 7.211018199704869
    task:
      type: Classification
  - dataset:
      config: he
      name: MTEB MassiveScenarioClassification (he)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 7.948844072798819
    - type: f1
      value: 2.1010859887190896
    - type: f1_weighted
      value: 3.0480176454133283
    - type: main_score
      value: 7.948844072798819
    task:
      type: Classification
  - dataset:
      config: nl
      name: MTEB MassiveScenarioClassification (nl)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 38.92277422528283
    - type: f1
      value: 35.488036321576146
    - type: f1_weighted
      value: 38.18536556200914
    - type: main_score
      value: 38.92277422528283
    task:
      type: Classification
  - dataset:
      config: km
      name: MTEB MassiveScenarioClassification (km)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: validation
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 8.150516478111165
    - type: f1
      value: 2.72691932389948
    - type: f1_weighted
      value: 3.3948665965609117
    - type: main_score
      value: 8.150516478111165
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
      value: 20.786832589263845
    - type: v_measure
      value: 20.786832589263845
    - type: v_measure_std
      value: 1.6048001943974946
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
      value: 18.181247067178756
    - type: v_measure
      value: 18.181247067178756
    - type: v_measure_std
      value: 1.5798786706707373
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB NYSJudicialEthicsLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 45.20547945205479
    - type: ap
      value: 50.160551683623055
    - type: ap_weighted
      value: 50.160551683623055
    - type: f1
      value: 44.53941120607787
    - type: f1_weighted
      value: 44.28963561383653
    - type: main_score
      value: 45.20547945205479
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB NewsClassification (default)
      revision: eb185aade064a813bc0b7f42de02595523103ca4
      split: test
      type: fancyzhx/ag_news
    metrics:
    - type: accuracy
      value: 73.78552631578948
    - type: f1
      value: 73.47724204580956
    - type: f1_weighted
      value: 73.47724204580956
    - type: main_score
      value: 73.78552631578948
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB OPP115DataRetentionLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 69.31818181818183
    - type: ap
      value: 64.09705159705157
    - type: ap_weighted
      value: 64.09705159705157
    - type: f1
      value: 69.12280701754385
    - type: f1_weighted
      value: 69.12280701754386
    - type: main_score
      value: 69.31818181818183
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB OPP115DataSecurityLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 63.868065967016484
    - type: ap
      value: 62.05622742346708
    - type: ap_weighted
      value: 62.05622742346708
    - type: f1
      value: 60.25914242202488
    - type: f1_weighted
      value: 60.22323273501004
    - type: main_score
      value: 63.868065967016484
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB OPP115DoNotTrackLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 88.18181818181819
    - type: ap
      value: 85.12727272727273
    - type: ap_weighted
      value: 85.12727272727273
    - type: f1
      value: 88.15734989648034
    - type: f1_weighted
      value: 88.15734989648034
    - type: main_score
      value: 88.18181818181819
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB OPP115FirstPartyCollectionUseLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 69.55896452540749
    - type: ap
      value: 64.53342029559877
    - type: ap_weighted
      value: 64.53342029559877
    - type: f1
      value: 69.32286869541191
    - type: f1_weighted
      value: 69.31770813082186
    - type: main_score
      value: 69.55896452540749
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB OPP115InternationalAndSpecificAudiencesLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 77.75510204081633
    - type: ap
      value: 75.20843296586462
    - type: ap_weighted
      value: 75.20843296586462
    - type: f1
      value: 77.09799280479909
    - type: f1_weighted
      value: 77.11382676229348
    - type: main_score
      value: 77.75510204081633
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB OPP115PolicyChangeLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 89.0951276102088
    - type: ap
      value: 87.15879085780726
    - type: ap_weighted
      value: 87.15879085780726
    - type: f1
      value: 89.04203698995461
    - type: f1_weighted
      value: 89.04380667729642
    - type: main_score
      value: 89.0951276102088
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB OPP115ThirdPartySharingCollectionLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 64.27672955974842
    - type: ap
      value: 62.893075413619535
    - type: ap_weighted
      value: 62.893075413619535
    - type: f1
      value: 60.459952085405675
    - type: f1_weighted
      value: 60.4135944642598
    - type: main_score
      value: 64.27672955974842
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB OPP115UserAccessEditAndDeletionLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 67.09956709956711
    - type: ap
      value: 62.92853137890984
    - type: ap_weighted
      value: 62.92853137890984
    - type: f1
      value: 66.41414141414141
    - type: f1_weighted
      value: 66.39337093882548
    - type: main_score
      value: 67.09956709956711
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB OPP115UserChoiceControlLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 70.69857697283311
    - type: ap
      value: 63.961545634799855
    - type: ap_weighted
      value: 63.961545634799855
    - type: f1
      value: 70.33565944829778
    - type: f1_weighted
      value: 70.34414874711732
    - type: main_score
      value: 70.69857697283311
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB OralArgumentQuestionPurposeLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 20.51282051282051
    - type: f1
      value: 17.434477437885
    - type: f1_weighted
      value: 21.50138868825342
    - type: main_score
      value: 20.51282051282051
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB OverrulingLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 69.580078125
    - type: ap
      value: 64.66695246425695
    - type: ap_weighted
      value: 64.66695246425695
    - type: f1
      value: 69.55969170904413
    - type: f1_weighted
      value: 69.5473829295991
    - type: main_score
      value: 69.580078125
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB PROALegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 49.47368421052632
    - type: ap
      value: 49.47368421052632
    - type: ap_weighted
      value: 49.47368421052632
    - type: f1
      value: 33.09859154929578
    - type: f1_weighted
      value: 32.750185322461085
    - type: main_score
      value: 49.47368421052632
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB PatentClassification (default)
      revision: 2f38a1dfdecfacee0184d74eaeafd3c0fb49d2a6
      split: test
      type: ccdv/patent-classification
    metrics:
    - type: accuracy
      value: 29.306640625000004
    - type: f1
      value: 22.127646065227754
    - type: f1_weighted
      value: 26.66185625260182
    - type: main_score
      value: 29.306640625000004
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB PersonalJurisdictionLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 51.99999999999999
    - type: ap
      value: 44.107526881720425
    - type: ap_weighted
      value: 44.107526881720425
    - type: f1
      value: 51.92307692307692
    - type: f1_weighted
      value: 51.61538461538463
    - type: main_score
      value: 51.99999999999999
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB PoemSentimentClassification (default)
      revision: 329d529d875a00c47ec71954a1a96ae167584770
      split: test
      type: google-research-datasets/poem_sentiment
    metrics:
    - type: accuracy
      value: 35.96153846153845
    - type: f1
      value: 25.717059445124445
    - type: f1_weighted
      value: 42.39026561619051
    - type: main_score
      value: 35.96153846153845
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB PoemSentimentClassification (default)
      revision: 329d529d875a00c47ec71954a1a96ae167584770
      split: validation
      type: google-research-datasets/poem_sentiment
    metrics:
    - type: accuracy
      value: 35.80952380952381
    - type: f1
      value: 26.76432080315997
    - type: f1_weighted
      value: 41.90402765909788
    - type: main_score
      value: 35.80952380952381
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB RUParaPhraserSTS (default)
      revision: 43265056790b8f7c59e0139acb4be0a8dad2c8f4
      split: test
      type: merionum/ru_paraphraser
    metrics:
    - type: cosine_pearson
      value: 65.17293362215221
    - type: cosine_spearman
      value: 72.14872507255558
    - type: euclidean_pearson
      value: 69.39028550512482
    - type: euclidean_spearman
      value: 72.14872507255558
    - type: main_score
      value: 72.14872507255558
    - type: manhattan_pearson
      value: 69.30934614737492
    - type: manhattan_spearman
      value: 72.04933049290007
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB RedditClustering (default)
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
      split: test
      type: mteb/reddit-clustering
    metrics:
    - type: main_score
      value: 26.275710753496597
    - type: v_measure
      value: 26.275710753496597
    - type: v_measure_std
      value: 4.029689555202136
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
      value: 40.4828876757081
    - type: v_measure
      value: 40.4828876757081
    - type: v_measure_std
      value: 10.162859998011204
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RiaNewsRetrieval (default)
      revision: 82374b0bbacda6114f39ff9c5b925fa1512ca5d7
      split: test
      type: ai-forever/ria-news-retrieval
    metrics:
    - type: main_score
      value: 51.271
    - type: map_at_1
      value: 36.21
    - type: map_at_10
      value: 46.208
    - type: map_at_100
      value: 47.004000000000005
    - type: map_at_1000
      value: 47.044000000000004
    - type: map_at_20
      value: 46.693
    - type: map_at_3
      value: 43.669999999999995
    - type: map_at_5
      value: 45.196
    - type: mrr_at_1
      value: 36.22
    - type: mrr_at_10
      value: 46.21178571428571
    - type: mrr_at_100
      value: 47.007420014661236
    - type: mrr_at_1000
      value: 47.04734848842366
    - type: mrr_at_20
      value: 46.69688042104938
    - type: mrr_at_3
      value: 43.668333333333585
    - type: mrr_at_5
      value: 45.199833333333274
    - type: nauc_map_at_1000_diff1
      value: 46.94937854830209
    - type: nauc_map_at_1000_max
      value: 20.810031674720868
    - type: nauc_map_at_1000_std
      value: -2.8474964036416845
    - type: nauc_map_at_100_diff1
      value: 46.93710679472339
    - type: nauc_map_at_100_max
      value: 20.808355966268614
    - type: nauc_map_at_100_std
      value: -2.8341393346842607
    - type: nauc_map_at_10_diff1
      value: 46.85305633304179
    - type: nauc_map_at_10_max
      value: 20.74714400194472
    - type: nauc_map_at_10_std
      value: -3.0251519873045534
    - type: nauc_map_at_1_diff1
      value: 52.76907950247656
    - type: nauc_map_at_1_max
      value: 20.909404191190152
    - type: nauc_map_at_1_std
      value: -4.486212769404569
    - type: nauc_map_at_20_diff1
      value: 46.854283528399826
    - type: nauc_map_at_20_max
      value: 20.774565284237017
    - type: nauc_map_at_20_std
      value: -2.8952917224271846
    - type: nauc_map_at_3_diff1
      value: 47.6120187355803
    - type: nauc_map_at_3_max
      value: 20.94624350299643
    - type: nauc_map_at_3_std
      value: -3.5249841066101704
    - type: nauc_map_at_5_diff1
      value: 46.961741404854
    - type: nauc_map_at_5_max
      value: 20.84061893727113
    - type: nauc_map_at_5_std
      value: -3.2560895841762707
    - type: nauc_mrr_at_1000_diff1
      value: 46.94210158390746
    - type: nauc_mrr_at_1000_max
      value: 20.823017819566672
    - type: nauc_mrr_at_1000_std
      value: -2.873564388596409
    - type: nauc_mrr_at_100_diff1
      value: 46.92983853646228
    - type: nauc_mrr_at_100_max
      value: 20.821328345843625
    - type: nauc_mrr_at_100_std
      value: -2.860179131955564
    - type: nauc_mrr_at_10_diff1
      value: 46.845920501930316
    - type: nauc_mrr_at_10_max
      value: 20.760199941251056
    - type: nauc_mrr_at_10_std
      value: -3.0506119945281385
    - type: nauc_mrr_at_1_diff1
      value: 52.7384650230153
    - type: nauc_mrr_at_1_max
      value: 20.916918175962735
    - type: nauc_mrr_at_1_std
      value: -4.553119995428164
    - type: nauc_mrr_at_20_diff1
      value: 46.84707480256205
    - type: nauc_mrr_at_20_max
      value: 20.78745076885492
    - type: nauc_mrr_at_20_std
      value: -2.921144125415831
    - type: nauc_mrr_at_3_diff1
      value: 47.621438923503305
    - type: nauc_mrr_at_3_max
      value: 20.964983104645327
    - type: nauc_mrr_at_3_std
      value: -3.5359639119054154
    - type: nauc_mrr_at_5_diff1
      value: 46.95496065526142
    - type: nauc_mrr_at_5_max
      value: 20.85370692098222
    - type: nauc_mrr_at_5_std
      value: -3.2815901993324985
    - type: nauc_ndcg_at_1000_diff1
      value: 45.22512963946746
    - type: nauc_ndcg_at_1000_max
      value: 20.827437126737433
    - type: nauc_ndcg_at_1000_std
      value: -1.5970972641072643
    - type: nauc_ndcg_at_100_diff1
      value: 44.870296183306195
    - type: nauc_ndcg_at_100_max
      value: 20.734194655306457
    - type: nauc_ndcg_at_100_std
      value: -1.1285720744844427
    - type: nauc_ndcg_at_10_diff1
      value: 44.428914407493004
    - type: nauc_ndcg_at_10_max
      value: 20.440243514420057
    - type: nauc_ndcg_at_10_std
      value: -2.1210028369378167
    - type: nauc_ndcg_at_1_diff1
      value: 52.76907950247656
    - type: nauc_ndcg_at_1_max
      value: 20.909404191190152
    - type: nauc_ndcg_at_1_std
      value: -4.486212769404569
    - type: nauc_ndcg_at_20_diff1
      value: 44.333669717530185
    - type: nauc_ndcg_at_20_max
      value: 20.503130801298607
    - type: nauc_ndcg_at_20_std
      value: -1.6040287688898405
    - type: nauc_ndcg_at_3_diff1
      value: 45.988171772625634
    - type: nauc_ndcg_at_3_max
      value: 20.901834276482294
    - type: nauc_ndcg_at_3_std
      value: -3.228341348463241
    - type: nauc_ndcg_at_5_diff1
      value: 44.77257666022731
    - type: nauc_ndcg_at_5_max
      value: 20.70409124701764
    - type: nauc_ndcg_at_5_std
      value: -2.7157792836026826
    - type: nauc_precision_at_1000_diff1
      value: 24.715455802573878
    - type: nauc_precision_at_1000_max
      value: 25.642760620422127
    - type: nauc_precision_at_1000_std
      value: 20.124139669932596
    - type: nauc_precision_at_100_diff1
      value: 31.317204301075428
    - type: nauc_precision_at_100_max
      value: 20.717841497411385
    - type: nauc_precision_at_100_std
      value: 15.071826819138575
    - type: nauc_precision_at_10_diff1
      value: 35.455731038677605
    - type: nauc_precision_at_10_max
      value: 19.1279684555736
    - type: nauc_precision_at_10_std
      value: 1.47750077627525
    - type: nauc_precision_at_1_diff1
      value: 52.76907950247656
    - type: nauc_precision_at_1_max
      value: 20.909404191190152
    - type: nauc_precision_at_1_std
      value: -4.486212769404569
    - type: nauc_precision_at_20_diff1
      value: 33.12837939512509
    - type: nauc_precision_at_20_max
      value: 19.114872213547194
    - type: nauc_precision_at_20_std
      value: 4.913450374911581
    - type: nauc_precision_at_3_diff1
      value: 41.17113816710835
    - type: nauc_precision_at_3_max
      value: 20.751510760974718
    - type: nauc_precision_at_3_std
      value: -2.3503705806184496
    - type: nauc_precision_at_5_diff1
      value: 37.71917213552412
    - type: nauc_precision_at_5_max
      value: 20.221342669216565
    - type: nauc_precision_at_5_std
      value: -0.9301420941546075
    - type: nauc_recall_at_1000_diff1
      value: 24.715455802574407
    - type: nauc_recall_at_1000_max
      value: 25.64276062042252
    - type: nauc_recall_at_1000_std
      value: 20.124139669932728
    - type: nauc_recall_at_100_diff1
      value: 31.31720430107529
    - type: nauc_recall_at_100_max
      value: 20.717841497411516
    - type: nauc_recall_at_100_std
      value: 15.071826819138751
    - type: nauc_recall_at_10_diff1
      value: 35.455731038677655
    - type: nauc_recall_at_10_max
      value: 19.127968455573654
    - type: nauc_recall_at_10_std
      value: 1.47750077627532
    - type: nauc_recall_at_1_diff1
      value: 52.76907950247656
    - type: nauc_recall_at_1_max
      value: 20.909404191190152
    - type: nauc_recall_at_1_std
      value: -4.486212769404569
    - type: nauc_recall_at_20_diff1
      value: 33.12837939512524
    - type: nauc_recall_at_20_max
      value: 19.1148722135474
    - type: nauc_recall_at_20_std
      value: 4.91345037491176
    - type: nauc_recall_at_3_diff1
      value: 41.171138167108374
    - type: nauc_recall_at_3_max
      value: 20.751510760974682
    - type: nauc_recall_at_3_std
      value: -2.35037058061848
    - type: nauc_recall_at_5_diff1
      value: 37.71917213552414
    - type: nauc_recall_at_5_max
      value: 20.221342669216575
    - type: nauc_recall_at_5_std
      value: -0.9301420941545763
    - type: ndcg_at_1
      value: 36.21
    - type: ndcg_at_10
      value: 51.271
    - type: ndcg_at_100
      value: 55.289
    - type: ndcg_at_1000
      value: 56.401
    - type: ndcg_at_20
      value: 53.028
    - type: ndcg_at_3
      value: 46.078
    - type: ndcg_at_5
      value: 48.825
    - type: precision_at_1
      value: 36.21
    - type: precision_at_10
      value: 6.7250000000000005
    - type: precision_at_100
      value: 0.864
    - type: precision_at_1000
      value: 0.095
    - type: precision_at_20
      value: 3.7089999999999996
    - type: precision_at_3
      value: 17.68
    - type: precision_at_5
      value: 11.940000000000001
    - type: recall_at_1
      value: 36.21
    - type: recall_at_10
      value: 67.25
    - type: recall_at_100
      value: 86.4
    - type: recall_at_1000
      value: 95.26
    - type: recall_at_20
      value: 74.18
    - type: recall_at_3
      value: 53.04
    - type: recall_at_5
      value: 59.699999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB RuBQReranking (default)
      revision: 2e96b8f098fa4b0950fc58eacadeb31c0d0c7fa2
      split: test
      type: ai-forever/rubq-reranking
    metrics:
    - type: main_score
      value: 62.15027154459556
    - type: map
      value: 62.15027154459556
    - type: mrr
      value: 68.09500782905037
    - type: nAUC_map_diff1
      value: 33.062970148901556
    - type: nAUC_map_max
      value: 11.090302786599219
    - type: nAUC_map_std
      value: 5.660375803457896
    - type: nAUC_mrr_diff1
      value: 35.578332777596685
    - type: nAUC_mrr_max
      value: 14.981311816105839
    - type: nAUC_mrr_std
      value: 5.550039824115788
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB RuBQRetrieval (default)
      revision: e19b6ffa60b3bc248e0b41f4cc37c26a55c2a67b
      split: test
      type: ai-forever/rubq-retrieval
    metrics:
    - type: main_score
      value: 51.734
    - type: map_at_1
      value: 28.510999999999996
    - type: map_at_10
      value: 43.631
    - type: map_at_100
      value: 44.988
    - type: map_at_1000
      value: 45.052
    - type: map_at_20
      value: 44.462
    - type: map_at_3
      value: 38.937
    - type: map_at_5
      value: 41.833
    - type: mrr_at_1
      value: 41.312056737588655
    - type: mrr_at_10
      value: 53.36138316634781
    - type: mrr_at_100
      value: 53.949276632310216
    - type: mrr_at_1000
      value: 53.97463197704906
    - type: mrr_at_20
      value: 53.72140863635181
    - type: mrr_at_3
      value: 50.43341213553989
    - type: mrr_at_5
      value: 52.32466509062269
    - type: nauc_map_at_1000_diff1
      value: 28.763838953386795
    - type: nauc_map_at_1000_max
      value: 24.058720207454833
    - type: nauc_map_at_1000_std
      value: 0.43914028345667794
    - type: nauc_map_at_100_diff1
      value: 28.74115734128027
    - type: nauc_map_at_100_max
      value: 24.067201633751907
    - type: nauc_map_at_100_std
      value: 0.48479657643151175
    - type: nauc_map_at_10_diff1
      value: 28.78055585777882
    - type: nauc_map_at_10_max
      value: 23.660824446842014
    - type: nauc_map_at_10_std
      value: -0.13417257945838412
    - type: nauc_map_at_1_diff1
      value: 31.726698171475988
    - type: nauc_map_at_1_max
      value: 18.706684051084675
    - type: nauc_map_at_1_std
      value: -3.1112088462944576
    - type: nauc_map_at_20_diff1
      value: 28.821888050893524
    - type: nauc_map_at_20_max
      value: 24.054108877450066
    - type: nauc_map_at_20_std
      value: 0.29933097295171895
    - type: nauc_map_at_3_diff1
      value: 29.414059668041187
    - type: nauc_map_at_3_max
      value: 21.603288627966425
    - type: nauc_map_at_3_std
      value: -1.2582454726026868
    - type: nauc_map_at_5_diff1
      value: 28.763709067820066
    - type: nauc_map_at_5_max
      value: 22.83472652858084
    - type: nauc_map_at_5_std
      value: -0.9139576784503077
    - type: nauc_mrr_at_1000_diff1
      value: 32.788260400997885
    - type: nauc_mrr_at_1000_max
      value: 26.645815716166126
    - type: nauc_mrr_at_1000_std
      value: -1.751195655856463
    - type: nauc_mrr_at_100_diff1
      value: 32.77886459571929
    - type: nauc_mrr_at_100_max
      value: 26.65637126850806
    - type: nauc_mrr_at_100_std
      value: -1.7267980184678584
    - type: nauc_mrr_at_10_diff1
      value: 32.78874216502045
    - type: nauc_mrr_at_10_max
      value: 26.4839655119896
    - type: nauc_mrr_at_10_std
      value: -1.9790149014956449
    - type: nauc_mrr_at_1_diff1
      value: 35.13232635364635
    - type: nauc_mrr_at_1_max
      value: 23.697653866746013
    - type: nauc_mrr_at_1_std
      value: -3.229619940147812
    - type: nauc_mrr_at_20_diff1
      value: 32.77802354989702
    - type: nauc_mrr_at_20_max
      value: 26.68040225454969
    - type: nauc_mrr_at_20_std
      value: -1.75616956975016
    - type: nauc_mrr_at_3_diff1
      value: 32.984816761600435
    - type: nauc_mrr_at_3_max
      value: 26.13901825373233
    - type: nauc_mrr_at_3_std
      value: -2.52193076369521
    - type: nauc_mrr_at_5_diff1
      value: 32.84967841683121
    - type: nauc_mrr_at_5_max
      value: 26.529547373322448
    - type: nauc_mrr_at_5_std
      value: -2.5581887401849595
    - type: nauc_ndcg_at_1000_diff1
      value: 28.596338371171104
    - type: nauc_ndcg_at_1000_max
      value: 26.398864343527546
    - type: nauc_ndcg_at_1000_std
      value: 2.0928142009674264
    - type: nauc_ndcg_at_100_diff1
      value: 28.25901263389625
    - type: nauc_ndcg_at_100_max
      value: 26.93052809711281
    - type: nauc_ndcg_at_100_std
      value: 3.1368035623322266
    - type: nauc_ndcg_at_10_diff1
      value: 28.273504061219295
    - type: nauc_ndcg_at_10_max
      value: 25.70274506672966
    - type: nauc_ndcg_at_10_std
      value: 1.031980357515916
    - type: nauc_ndcg_at_1_diff1
      value: 35.288927336386486
    - type: nauc_ndcg_at_1_max
      value: 23.407964640774143
    - type: nauc_ndcg_at_1_std
      value: -3.2088824424845743
    - type: nauc_ndcg_at_20_diff1
      value: 28.27252389476242
    - type: nauc_ndcg_at_20_max
      value: 26.959280568356686
    - type: nauc_ndcg_at_20_std
      value: 2.355748254409649
    - type: nauc_ndcg_at_3_diff1
      value: 29.507109145825144
    - type: nauc_ndcg_at_3_max
      value: 23.171704666301913
    - type: nauc_ndcg_at_3_std
      value: -1.4521550440778286
    - type: nauc_ndcg_at_5_diff1
      value: 28.488416363267216
    - type: nauc_ndcg_at_5_max
      value: 24.63470555569984
    - type: nauc_ndcg_at_5_std
      value: -0.9243408985702865
    - type: nauc_precision_at_1000_diff1
      value: -1.6853041487515183
    - type: nauc_precision_at_1000_max
      value: 7.960967030916032
    - type: nauc_precision_at_1000_std
      value: 3.6491508412352784
    - type: nauc_precision_at_100_diff1
      value: 1.1138125936003078
    - type: nauc_precision_at_100_max
      value: 14.425287491557784
    - type: nauc_precision_at_100_std
      value: 8.976522577047673
    - type: nauc_precision_at_10_diff1
      value: 9.746060862351767
    - type: nauc_precision_at_10_max
      value: 21.23608774117671
    - type: nauc_precision_at_10_std
      value: 5.704741335087523
    - type: nauc_precision_at_1_diff1
      value: 35.288927336386486
    - type: nauc_precision_at_1_max
      value: 23.407964640774143
    - type: nauc_precision_at_1_std
      value: -3.2088824424845743
    - type: nauc_precision_at_20_diff1
      value: 6.326610022834949
    - type: nauc_precision_at_20_max
      value: 20.35842844947274
    - type: nauc_precision_at_20_std
      value: 8.561077634074318
    - type: nauc_precision_at_3_diff1
      value: 20.23921207457269
    - type: nauc_precision_at_3_max
      value: 22.983126702497753
    - type: nauc_precision_at_3_std
      value: 0.3762065769613514
    - type: nauc_precision_at_5_diff1
      value: 14.130374029335451
    - type: nauc_precision_at_5_max
      value: 22.27280203101339
    - type: nauc_precision_at_5_std
      value: 1.4403304333986182
    - type: nauc_recall_at_1000_diff1
      value: 5.336939388003354
    - type: nauc_recall_at_1000_max
      value: 31.706880957377347
    - type: nauc_recall_at_1000_std
      value: 34.42854130495
    - type: nauc_recall_at_100_diff1
      value: 13.06348098921675
    - type: nauc_recall_at_100_max
      value: 35.43003105581946
    - type: nauc_recall_at_100_std
      value: 28.949432461425634
    - type: nauc_recall_at_10_diff1
      value: 19.58510835348359
    - type: nauc_recall_at_10_max
      value: 25.98205980928563
    - type: nauc_recall_at_10_std
      value: 6.643640648680416
    - type: nauc_recall_at_1_diff1
      value: 31.726698171475988
    - type: nauc_recall_at_1_max
      value: 18.706684051084675
    - type: nauc_recall_at_1_std
      value: -3.1112088462944576
    - type: nauc_recall_at_20_diff1
      value: 17.50381042355996
    - type: nauc_recall_at_20_max
      value: 31.185904487900324
    - type: nauc_recall_at_20_std
      value: 13.510200942211565
    - type: nauc_recall_at_3_diff1
      value: 24.227382984516147
    - type: nauc_recall_at_3_max
      value: 21.40248626451014
    - type: nauc_recall_at_3_std
      value: -0.469137375497106
    - type: nauc_recall_at_5_diff1
      value: 21.25980638967181
    - type: nauc_recall_at_5_max
      value: 23.853364661344404
    - type: nauc_recall_at_5_std
      value: 0.7407724495151051
    - type: ndcg_at_1
      value: 41.253
    - type: ndcg_at_10
      value: 51.734
    - type: ndcg_at_100
      value: 56.796
    - type: ndcg_at_1000
      value: 58.044
    - type: ndcg_at_20
      value: 53.982
    - type: ndcg_at_3
      value: 44.448
    - type: ndcg_at_5
      value: 48.306
    - type: precision_at_1
      value: 41.253
    - type: precision_at_10
      value: 10.674
    - type: precision_at_100
      value: 1.437
    - type: precision_at_1000
      value: 0.159
    - type: precision_at_20
      value: 6.0280000000000005
    - type: precision_at_3
      value: 24.901
    - type: precision_at_5
      value: 18.038
    - type: recall_at_1
      value: 28.510999999999996
    - type: recall_at_10
      value: 65.646
    - type: recall_at_100
      value: 86.37
    - type: recall_at_1000
      value: 94.926
    - type: recall_at_20
      value: 73.236
    - type: recall_at_3
      value: 47.492000000000004
    - type: recall_at_5
      value: 56.552
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB RuReviewsClassification (default)
      revision: f6d2c31f4dc6b88f468552750bfec05b4b41b05a
      split: test
      type: ai-forever/ru-reviews-classification
    metrics:
    - type: accuracy
      value: 60.6591796875
    - type: f1
      value: 60.34177974754267
    - type: f1_weighted
      value: 60.3424791407144
    - type: main_score
      value: 60.6591796875
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB RuSTSBenchmarkSTS (default)
      revision: 7cf24f325c6da6195df55bef3d86b5e0616f3018
      split: test
      type: ai-forever/ru-stsbenchmark-sts
    metrics:
    - type: cosine_pearson
      value: 78.67181755069355
    - type: cosine_spearman
      value: 78.48157070388886
    - type: euclidean_pearson
      value: 78.16400243944963
    - type: euclidean_spearman
      value: 78.48124817526005
    - type: main_score
      value: 78.48157070388886
    - type: manhattan_pearson
      value: 78.04437263885238
    - type: manhattan_spearman
      value: 78.34292373482941
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB RuSciBenchGRNTIClassification (default)
      revision: 673a610d6d3dd91a547a0d57ae1b56f37ebbf6a1
      split: test
      type: ai-forever/ru-scibench-grnti-classification
    metrics:
    - type: accuracy
      value: 52.9296875
    - type: f1
      value: 51.36892216551846
    - type: f1_weighted
      value: 51.38263945115431
    - type: main_score
      value: 52.9296875
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB RuSciBenchGRNTIClusteringP2P (default)
      revision: 673a610d6d3dd91a547a0d57ae1b56f37ebbf6a1
      split: test
      type: ai-forever/ru-scibench-grnti-classification
    metrics:
    - type: main_score
      value: 47.548401486969844
    - type: v_measure
      value: 47.548401486969844
    - type: v_measure_std
      value: 0.9652047055316595
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RuSciBenchOECDClassification (default)
      revision: 26c88e99dcaba32bb45d0e1bfc21902337f6d471
      split: test
      type: ai-forever/ru-scibench-oecd-classification
    metrics:
    - type: accuracy
      value: 40.7861328125
    - type: f1
      value: 38.417161317304625
    - type: f1_weighted
      value: 38.41751508417981
    - type: main_score
      value: 40.7861328125
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB RuSciBenchOECDClusteringP2P (default)
      revision: 26c88e99dcaba32bb45d0e1bfc21902337f6d471
      split: test
      type: ai-forever/ru-scibench-oecd-classification
    metrics:
    - type: main_score
      value: 41.44039335680795
    - type: v_measure
      value: 41.44039335680795
    - type: v_measure_std
      value: 1.2447867997057736
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB SCDBPAccountabilityLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 64.64379947229551
    - type: ap
      value: 91.77095548714944
    - type: ap_weighted
      value: 91.77095548714944
    - type: f1
      value: 56.37541231445849
    - type: f1_weighted
      value: 70.25628045216064
    - type: main_score
      value: 64.64379947229551
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB SCDBPAuditsLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 59.89445910290237
    - type: ap
      value: 75.9408508806894
    - type: ap_weighted
      value: 75.9408508806894
    - type: f1
      value: 59.26805814808528
    - type: f1_weighted
      value: 61.147261012536525
    - type: main_score
      value: 59.89445910290237
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB SCDBPCertificationLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 59.78835978835979
    - type: ap
      value: 79.40365504574285
    - type: ap_weighted
      value: 79.40365504574285
    - type: f1
      value: 56.06802055297283
    - type: f1_weighted
      value: 62.49406105045939
    - type: main_score
      value: 59.78835978835979
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB SCDBPTrainingLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 59.102902374670194
    - type: ap
      value: 78.86277214171828
    - type: ap_weighted
      value: 78.86277214171828
    - type: f1
      value: 58.122144043570934
    - type: f1_weighted
      value: 60.91223239928431
    - type: main_score
      value: 59.102902374670194
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB SCDBPVerificationLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 62.796833773087066
    - type: ap
      value: 66.09764646131225
    - type: ap_weighted
      value: 66.09764646131225
    - type: f1
      value: 62.562263119916494
    - type: f1_weighted
      value: 62.19476909661592
    - type: main_score
      value: 62.796833773087066
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB SCDDAccountabilityLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 60.84656084656085
    - type: ap
      value: 96.40608145845859
    - type: ap_weighted
      value: 96.40608145845859
    - type: f1
      value: 46.04166666666668
    - type: f1_weighted
      value: 71.16512345679011
    - type: main_score
      value: 60.84656084656085
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB SCDDAuditsLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 61.741424802110814
    - type: ap
      value: 94.08312772646127
    - type: ap_weighted
      value: 94.08312772646127
    - type: f1
      value: 50.59825064499599
    - type: f1_weighted
      value: 69.72736628137642
    - type: main_score
      value: 61.741424802110814
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB SCDDCertificationLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 62.43386243386243
    - type: ap
      value: 92.94462068443907
    - type: ap_weighted
      value: 92.94462068443907
    - type: f1
      value: 49.37181663837012
    - type: f1_weighted
      value: 70.32551510197236
    - type: main_score
      value: 62.43386243386243
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB SCDDTrainingLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 53.825857519788926
    - type: ap
      value: 89.02073335965477
    - type: ap_weighted
      value: 89.02073335965477
    - type: f1
      value: 47.22918407128933
    - type: f1_weighted
      value: 60.86559112527728
    - type: main_score
      value: 53.825857519788926
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB SCDDVerificationLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 49.07651715039577
    - type: ap
      value: 76.04960744098202
    - type: ap_weighted
      value: 76.04960744098202
    - type: f1
      value: 47.939930963310914
    - type: f1_weighted
      value: 51.65413225324895
    - type: main_score
      value: 49.07651715039577
    task:
      type: Classification
  - dataset:
      config: zh
      name: MTEB STS22 (zh)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 10.783707479640047
    - type: cosine_spearman
      value: 32.82859566062349
    - type: euclidean_pearson
      value: 21.280811252412548
    - type: euclidean_spearman
      value: 32.82859566062349
    - type: main_score
      value: 32.82859566062349
    - type: manhattan_pearson
      value: 21.510100649883686
    - type: manhattan_spearman
      value: 32.924353350152195
    task:
      type: STS
  - dataset:
      config: de-fr
      name: MTEB STS22 (de-fr)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 10.185699265034293
    - type: cosine_spearman
      value: 17.504453225721367
    - type: euclidean_pearson
      value: 11.256743769494715
    - type: euclidean_spearman
      value: 17.504453225721367
    - type: main_score
      value: 17.504453225721367
    - type: manhattan_pearson
      value: 9.741426548627869
    - type: manhattan_spearman
      value: 16.976476678309815
    task:
      type: STS
  - dataset:
      config: pl-en
      name: MTEB STS22 (pl-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 44.8697112464095
    - type: cosine_spearman
      value: 42.075721562892944
    - type: euclidean_pearson
      value: 43.40637455102888
    - type: euclidean_spearman
      value: 42.075721562892944
    - type: main_score
      value: 42.075721562892944
    - type: manhattan_pearson
      value: 45.13522626066653
    - type: manhattan_spearman
      value: 42.53935152687679
    task:
      type: STS
  - dataset:
      config: ru
      name: MTEB STS22 (ru)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 51.4108131114559
    - type: cosine_spearman
      value: 60.05716921675363
    - type: euclidean_pearson
      value: 52.595208834301246
    - type: euclidean_spearman
      value: 60.05157835366835
    - type: main_score
      value: 60.05716921675363
    - type: manhattan_pearson
      value: 52.49640999228367
    - type: manhattan_spearman
      value: 59.89412865698913
    task:
      type: STS
  - dataset:
      config: fr
      name: MTEB STS22 (fr)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 26.610436064600535
    - type: cosine_spearman
      value: 42.00247648193326
    - type: euclidean_pearson
      value: 33.894760545223065
    - type: euclidean_spearman
      value: 42.00247648193326
    - type: main_score
      value: 42.00247648193326
    - type: manhattan_pearson
      value: 33.80795212984925
    - type: manhattan_spearman
      value: 42.14922985413102
    task:
      type: STS
  - dataset:
      config: de
      name: MTEB STS22 (de)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: -5.737945045891398
    - type: cosine_spearman
      value: 8.163885149544491
    - type: euclidean_pearson
      value: -2.214478704390943
    - type: euclidean_spearman
      value: 8.16472976205313
    - type: main_score
      value: 8.163885149544491
    - type: manhattan_pearson
      value: -1.7539096573944195
    - type: manhattan_spearman
      value: 8.6906872178124
    task:
      type: STS
  - dataset:
      config: tr
      name: MTEB STS22 (tr)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 2.043942714330888
    - type: cosine_spearman
      value: 15.459553758272923
    - type: euclidean_pearson
      value: 8.816942314411607
    - type: euclidean_spearman
      value: 15.459553758272923
    - type: main_score
      value: 15.459553758272923
    - type: manhattan_pearson
      value: 9.32963790399984
    - type: manhattan_spearman
      value: 15.7857074615967
    task:
      type: STS
  - dataset:
      config: de-en
      name: MTEB STS22 (de-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 17.695301514955418
    - type: cosine_spearman
      value: 21.545599222945675
    - type: euclidean_pearson
      value: 18.353827841283753
    - type: euclidean_spearman
      value: 21.545599222945675
    - type: main_score
      value: 21.545599222945675
    - type: manhattan_pearson
      value: 17.009036963688505
    - type: manhattan_spearman
      value: 20.508582325360287
    task:
      type: STS
  - dataset:
      config: it
      name: MTEB STS22 (it)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 32.630588839696415
    - type: cosine_spearman
      value: 39.69250140711604
    - type: euclidean_pearson
      value: 37.54122176804933
    - type: euclidean_spearman
      value: 39.69250140711604
    - type: main_score
      value: 39.69250140711604
    - type: manhattan_pearson
      value: 37.79703600372667
    - type: manhattan_spearman
      value: 39.742229485575024
    task:
      type: STS
  - dataset:
      config: pl
      name: MTEB STS22 (pl)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 0.3113685198259237
    - type: cosine_spearman
      value: 9.707385637292596
    - type: euclidean_pearson
      value: -2.4832855952463206
    - type: euclidean_spearman
      value: 9.80177503118972
    - type: main_score
      value: 9.707385637292596
    - type: manhattan_pearson
      value: -2.325293004138977
    - type: manhattan_spearman
      value: 10.060452403624826
    task:
      type: STS
  - dataset:
      config: fr-pl
      name: MTEB STS22 (fr-pl)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 47.546556133158575
    - type: cosine_spearman
      value: 39.440531887330785
    - type: euclidean_pearson
      value: 48.2920143634797
    - type: euclidean_spearman
      value: 39.440531887330785
    - type: main_score
      value: 39.440531887330785
    - type: manhattan_pearson
      value: 45.769523538925824
    - type: manhattan_spearman
      value: 50.709255283710995
    task:
      type: STS
  - dataset:
      config: de-pl
      name: MTEB STS22 (de-pl)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 0.33007020080694816
    - type: cosine_spearman
      value: 25.52831180119127
    - type: euclidean_pearson
      value: 5.7124033000823164
    - type: euclidean_spearman
      value: 25.52831180119127
    - type: main_score
      value: 25.52831180119127
    - type: manhattan_pearson
      value: 5.62314566860622
    - type: manhattan_spearman
      value: 23.83463610871175
    task:
      type: STS
  - dataset:
      config: ar
      name: MTEB STS22 (ar)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 22.766025640460693
    - type: cosine_spearman
      value: 27.950069575571522
    - type: euclidean_pearson
      value: 26.551723755491363
    - type: euclidean_spearman
      value: 27.939678639817668
    - type: main_score
      value: 27.950069575571522
    - type: manhattan_pearson
      value: 26.681060475093854
    - type: manhattan_spearman
      value: 27.986878582632468
    task:
      type: STS
  - dataset:
      config: es-en
      name: MTEB STS22 (es-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 38.597910358452815
    - type: cosine_spearman
      value: 42.766194189894094
    - type: euclidean_pearson
      value: 39.991306255692045
    - type: euclidean_spearman
      value: 42.766194189894094
    - type: main_score
      value: 42.766194189894094
    - type: manhattan_pearson
      value: 39.74918349185897
    - type: manhattan_spearman
      value: 42.574140880355976
    task:
      type: STS
  - dataset:
      config: es-it
      name: MTEB STS22 (es-it)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 31.245905627830638
    - type: cosine_spearman
      value: 32.83240215980029
    - type: euclidean_pearson
      value: 33.06481984956772
    - type: euclidean_spearman
      value: 32.83240215980029
    - type: main_score
      value: 32.83240215980029
    - type: manhattan_pearson
      value: 32.75706899386791
    - type: manhattan_spearman
      value: 32.334081823391806
    task:
      type: STS
  - dataset:
      config: es
      name: MTEB STS22 (es)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 16.966347433363
    - type: cosine_spearman
      value: 45.3129129914676
    - type: euclidean_pearson
      value: 28.50940505249936
    - type: euclidean_spearman
      value: 45.3129129914676
    - type: main_score
      value: 45.3129129914676
    - type: manhattan_pearson
      value: 28.314847203862147
    - type: manhattan_spearman
      value: 45.72042962859271
    task:
      type: STS
  - dataset:
      config: zh-en
      name: MTEB STS22 (zh-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 34.66358594216254
    - type: cosine_spearman
      value: 31.24659955360722
    - type: euclidean_pearson
      value: 34.878197534840744
    - type: euclidean_spearman
      value: 31.24659955360722
    - type: main_score
      value: 31.24659955360722
    - type: manhattan_pearson
      value: 34.70743093532992
    - type: manhattan_spearman
      value: 30.441251812127955
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
      value: 41.376318618780324
    - type: cosine_spearman
      value: 47.061970299820764
    - type: euclidean_pearson
      value: 44.89590651276241
    - type: euclidean_spearman
      value: 47.061970299820764
    - type: main_score
      value: 47.061970299820764
    - type: manhattan_pearson
      value: 44.780089700405576
    - type: manhattan_spearman
      value: 46.742447019531525
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SensitiveTopicsClassification (default)
      revision: 416b34a802308eac30e4192afc0ff99bb8dcc7f2
      split: test
      type: ai-forever/sensitive-topics-classification
    metrics:
    - type: accuracy
      value: 24.443359375
    - type: f1
      value: 21.903258801323084
    - type: lrap
      value: 36.34758843315896
    - type: main_score
      value: 24.443359375
    task:
      type: MultilabelClassification
  - dataset:
      config: default
      name: MTEB StackExchangeClustering (default)
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
      split: test
      type: mteb/stackexchange-clustering
    metrics:
    - type: main_score
      value: 33.50613168016603
    - type: v_measure
      value: 33.50613168016603
    - type: v_measure_std
      value: 3.91782276122889
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
      value: 27.98150942889309
    - type: v_measure
      value: 27.98150942889309
    - type: v_measure_std
      value: 2.0056109104136226
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB TERRa (default)
      revision: 7b58f24536063837d644aab9a023c62199b2a612
      split: dev
      type: ai-forever/terra-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 59.60912052117264
    - type: cosine_accuracy_threshold
      value: 81.55556917190552
    - type: cosine_ap
      value: 56.08760299515377
    - type: cosine_f1
      value: 67.33167082294264
    - type: cosine_f1_threshold
      value: 78.14505100250244
    - type: cosine_precision
      value: 54.43548387096774
    - type: cosine_recall
      value: 88.23529411764706
    - type: dot_accuracy
      value: 59.60912052117264
    - type: dot_accuracy_threshold
      value: 81.55556917190552
    - type: dot_ap
      value: 56.08760299515377
    - type: dot_f1
      value: 67.33167082294264
    - type: dot_f1_threshold
      value: 78.14503908157349
    - type: dot_precision
      value: 54.43548387096774
    - type: dot_recall
      value: 88.23529411764706
    - type: euclidean_accuracy
      value: 59.60912052117264
    - type: euclidean_accuracy_threshold
      value: 60.736143589019775
    - type: euclidean_ap
      value: 56.08760299515377
    - type: euclidean_f1
      value: 67.33167082294264
    - type: euclidean_f1_threshold
      value: 66.11342430114746
    - type: euclidean_precision
      value: 54.43548387096774
    - type: euclidean_recall
      value: 88.23529411764706
    - type: main_score
      value: 56.265447472512676
    - type: manhattan_accuracy
      value: 60.91205211726385
    - type: manhattan_accuracy_threshold
      value: 877.9421806335449
    - type: manhattan_ap
      value: 56.265447472512676
    - type: manhattan_f1
      value: 67.16791979949875
    - type: manhattan_f1_threshold
      value: 930.9440612792969
    - type: manhattan_precision
      value: 54.47154471544715
    - type: manhattan_recall
      value: 87.58169934640523
    - type: max_ap
      value: 56.265447472512676
    - type: max_f1
      value: 67.33167082294264
    - type: max_precision
      value: 54.47154471544715
    - type: max_recall
      value: 88.23529411764706
    - type: similarity_accuracy
      value: 59.60912052117264
    - type: similarity_accuracy_threshold
      value: 81.55557513237
    - type: similarity_ap
      value: 56.08760299515377
    - type: similarity_f1
      value: 67.33167082294264
    - type: similarity_f1_threshold
      value: 78.1450629234314
    - type: similarity_precision
      value: 54.43548387096774
    - type: similarity_recall
      value: 88.23529411764706
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB TelemarketingSalesRuleLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 51.06382978723404
    - type: ap
      value: 64.12529550827422
    - type: ap_weighted
      value: 64.12529550827422
    - type: f1
      value: 48.74348032242769
    - type: f1_weighted
      value: 46.65516580410197
    - type: main_score
      value: 51.06382978723404
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TextualismToolDictionariesLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 69.1588785046729
    - type: ap
      value: 13.91484942886812
    - type: ap_weighted
      value: 13.91484942886812
    - type: f1
      value: 53.57001972386588
    - type: f1_weighted
      value: 75.94757507050821
    - type: main_score
      value: 69.1588785046729
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TextualismToolPlainLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 52.121212121212125
    - type: ap
      value: 44.68029172320217
    - type: ap_weighted
      value: 44.68029172320217
    - type: f1
      value: 50.48433048433048
    - type: f1_weighted
      value: 48.79288612621945
    - type: main_score
      value: 52.121212121212125
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ToxicChatClassification (default)
      revision: 3e0319203c7162b9c9f8015b594441f979c199bc
      split: test
      type: lmsys/toxic-chat
    metrics:
    - type: accuracy
      value: 73.56529209621992
    - type: ap
      value: 21.641229801673067
    - type: ap_weighted
      value: 21.641229801673067
    - type: f1
      value: 60.19489676894062
    - type: f1_weighted
      value: 77.21280694246968
    - type: main_score
      value: 73.56529209621992
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ToxicConversationsClassification (default)
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
      split: test
      type: mteb/toxic_conversations_50k
    metrics:
    - type: accuracy
      value: 57.7734375
    - type: ap
      value: 9.305482173252097
    - type: ap_weighted
      value: 9.305482173252097
    - type: f1
      value: 44.43839832998249
    - type: f1_weighted
      value: 67.10615100631958
    - type: main_score
      value: 57.7734375
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
      value: 55.29994340690435
    - type: f1
      value: 55.3098112653406
    - type: f1_weighted
      value: 54.4846442708958
    - type: main_score
      value: 55.29994340690435
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TweetTopicSingleClassification (default)
      revision: 87b7a0d1c402dbb481db649569c556d9aa27ac05
      split: test_2021
      type: cardiffnlp/tweet_topic_single
    metrics:
    - type: accuracy
      value: 52.522150029533364
    - type: f1
      value: 40.24714634897976
    - type: f1_weighted
      value: 57.39523757985323
    - type: main_score
      value: 52.522150029533364
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
      value: 19.90344454285597
    - type: v_measure
      value: 19.90344454285597
    - type: v_measure_std
      value: 1.8260774855268984
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB UCCVCommonLawLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 52.127659574468076
    - type: ap
      value: 42.829212190914326
    - type: ap_weighted
      value: 42.829212190914326
    - type: f1
      value: 50.50895050895051
    - type: f1_weighted
      value: 51.84200503349441
    - type: main_score
      value: 52.127659574468076
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB UnfairTOSLegalBenchClassification (default)
      revision: 12ca3b695563788fead87a982ad1a068284413f4
      split: test
      type: nguha/legalbench
    metrics:
    - type: accuracy
      value: 19.3359375
    - type: f1
      value: 11.24236763925133
    - type: f1_weighted
      value: 27.137659267661597
    - type: main_score
      value: 19.3359375
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB VieMedEVBitextMining (default)
      revision: d03c69413bc53d1cea5a5375b3a953c4fee35ecd
      split: test
      type: nhuvo/MedEV
    metrics:
    - type: accuracy
      value: 8.69140625
    - type: f1
      value: 7.772120924359041
    - type: main_score
      value: 7.772120924359041
    - type: precision
      value: 7.525730353438241
    - type: recall
      value: 8.69140625
    task:
      type: BitextMining
  - dataset:
      config: default
      name: MTEB WikiCitiesClustering (default)
      revision: ddc9ee9242fa65332597f70e967ecc38b9d734fa
      split: test
      type: jinaai/cities_wiki_clustering
    metrics:
    - type: main_score
      value: 56.66855146861069
    - type: v_measure
      value: 56.66855146861069
    - type: v_measure_std
      value: 0.0
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB YahooAnswersTopicsClassification (default)
      revision: 78fccffa043240c80e17a6b1da724f5a1057e8e5
      split: test
      type: community-datasets/yahoo_answers_topics
    metrics:
    - type: accuracy
      value: 41.787109375
    - type: f1
      value: 40.33967050694529
    - type: f1_weighted
      value: 40.3509380795682
    - type: main_score
      value: 41.787109375
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB YelpReviewFullClassification (default)
      revision: c1f9ee939b7d05667af864ee1cb066393154bf85
      split: test
      type: Yelp/yelp_review_full
    metrics:
    - type: accuracy
      value: 43.5888671875
    - type: f1
      value: 42.36578282497966
    - type: f1_weighted
      value: 42.363220099893724
    - type: main_score
      value: 43.5888671875
    task:
      type: Classification
---


Быстрая модель BERT для расчетов эмбеддингов предложений на русском языке. Модель основана на [cointegrated/rubert-tiny2](https://huggingface.co/cointegrated/rubert-tiny2)  - имеет аналогичные размеры контекста (2048), ембеддинга (312) и быстродействие.



## Использование
```Python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sergeyzh/rubert-tiny-turbo')

sentences = ["привет мир", "hello world", "здравствуй вселенная"]
embeddings = model.encode(sentences)
print(util.dot_score(embeddings, embeddings))
```

## Метрики

Оценки модели на бенчмарке [encodechka](https://github.com/avidale/encodechka):

| model                              | CPU       | GPU      | size     |   Mean S  | Mean S+W   |   dim  |
|:-----------------------------------|----------:|---------:|---------:|----------:|-----------:|-------:|
| [sergeyzh/LaBSE-ru-turbo](https://huggingface.co/sergeyzh/LaBSE-ru-turbo)            |   120.40  |   8.05   |  490     |    0.789  |   0.702    |   768  |
| BAAI/bge-m3                        | 523.40    | 22.50    | 2166     |    0.787  |   0.696    |  1024  |
| intfloat/multilingual-e5-large     | 506.80    | 30.80    | 2136     |    0.780  |   0.686    |  1024  |
| intfloat/multilingual-e5-base      | 130.61    | 14.39    | 1061     |    0.761  |   0.669    |   768  |
| **sergeyzh/rubert-tiny-turbo**     |   5.51    |  3.25    |  111     |    0.749  |   0.667    |   312  |
| intfloat/multilingual-e5-small     |  40.86    | 12.09    |  449     |    0.742  |   0.645    |   384  |
| cointegrated/rubert-tiny2          |   5.51    |  3.25    |  111     |    0.704  |   0.638    |   312  |

| model                              | STS      | PI       | NLI      | SA       | TI       | IA       | IC       | ICX      | NE1      | NE2      |
|:-----------------------------------|:---------|:---------|:---------|:---------|:---------|:---------|:---------|:---------|:---------|:---------|
| [sergeyzh/LaBSE-ru-turbo](https://huggingface.co/sergeyzh/LaBSE-ru-turbo)            |   0.864  |  0.748   |  0.490   |  0.814   |  0.974   |  0.806   |  0.815   |  0.801   |  0.305   |  0.404   |
| BAAI/bge-m3                        |  0.864   |  0.749   |  0.510   |  0.819   |  0.973   |  0.792   |  0.809   |  0.783   |  0.240   |  0.422   |
| intfloat/multilingual-e5-large     |  0.862   |  0.727   |  0.473   |  0.810   |  0.979   |  0.798   |  0.819   |  0.773   |  0.224   |  0.374   |
| intfloat/multilingual-e5-base      |  0.835   |  0.704   |  0.459   |  0.796   |  0.964   |  0.783   |  0.802   |  0.738   |  0.235   |  0.376   |
| **sergeyzh/rubert-tiny-turbo**     |  0.828   |  0.722   |  0.476   |  0.787   |  0.955   |  0.757   |  0.780   |  0.685   |  0.305   |  0.373   |
| intfloat/multilingual-e5-small     |  0.822   |  0.714   |  0.457   |  0.758   |  0.957   |  0.761   |  0.779   |  0.691   |  0.234   |  0.275   |
| cointegrated/rubert-tiny2          |  0.750   |  0.651   |  0.417   |  0.737   |  0.937   |  0.746   |  0.757   |  0.638   |  0.360   |  0.386   |

Оценки модели на бенчмарке [ruMTEB](https://habr.com/ru/companies/sberdevices/articles/831150/):

|Model Name                         | Metric              | sbert_large_ mt_nlu_ru | sbert_large_ nlu_ru | rubert-tiny2    | rubert-tiny-turbo | multilingual-e5-small | multilingual-e5-base | multilingual-e5-large |
|:----------------------------------|:--------------------|-----------------------:|--------------------:|----------------:|------------------:|----------------------:|---------------------:|----------------------:|
|CEDRClassification                 | Accuracy            |         0.368          |         0.358       |      0.369      |        0.390      |        0.401          |        0.423         |       **0.448**       |
|GeoreviewClassification            | Accuracy            |         0.397          |         0.400       |      0.396      |        0.414      |        0.447          |        0.461         |       **0.497**       |
|GeoreviewClusteringP2P             | V-measure           |         0.584          |         0.590       |      0.442      |        0.597      |        0.586          |        0.545         |       **0.605**       |
|HeadlineClassification             | Accuracy            |         0.772          |       **0.793**     |      0.742      |        0.686      |        0.732          |        0.757         |         0.758         |
|InappropriatenessClassification    | Accuracy            |       **0.646**        |         0.625       |      0.586      |        0.591      |        0.592          |        0.588         |         0.616         |
|KinopoiskClassification            | Accuracy            |         0.503          |         0.495       |      0.491      |        0.505      |        0.500          |        0.509         |       **0.566**       |
|RiaNewsRetrieval                   | NDCG@10             |         0.214          |         0.111       |      0.140      |        0.513      |        0.700          |        0.702         |       **0.807**       |
|RuBQReranking                      | MAP@10              |         0.561          |         0.468       |      0.461      |        0.622      |        0.715          |        0.720         |       **0.756**       |
|RuBQRetrieval                      | NDCG@10             |         0.298          |         0.124       |      0.109      |        0.517      |        0.685          |        0.696         |       **0.741**       |
|RuReviewsClassification            | Accuracy            |         0.589          |         0.583       |      0.570      |        0.607      |        0.612          |        0.630         |       **0.653**       |
|RuSTSBenchmarkSTS                  | Pearson correlation |         0.712          |         0.588       |      0.694      |        0.787      |        0.781          |        0.796         |       **0.831**       |
|RuSciBenchGRNTIClassification      | Accuracy            |         0.542          |         0.539       |      0.456      |        0.529      |        0.550          |        0.563         |       **0.582**       |
|RuSciBenchGRNTIClusteringP2P       | V-measure           |       **0.522**        |         0.504       |      0.414      |        0.481      |        0.511          |        0.516         |         0.520         |
|RuSciBenchOECDClassification       | Accuracy            |         0.438          |         0.430       |      0.355      |        0.415      |        0.427          |        0.423         |       **0.445**       |
|RuSciBenchOECDClusteringP2P        | V-measure           |       **0.473**        |         0.464       |      0.381      |        0.411      |        0.443          |        0.448         |         0.450         |
|SensitiveTopicsClassification      | Accuracy            |       **0.285**        |         0.280       |      0.220      |        0.244      |        0.228          |        0.234         |         0.257         |
|TERRaClassification                | Average Precision   |         0.520          |         0.502       |      0.519      |        0.563      |        0.551          |        0.550         |       **0.584**       |

|Model Name                         | Metric              | sbert_large_ mt_nlu_ru | sbert_large_ nlu_ru | rubert-tiny2    | rubert-tiny-turbo | multilingual-e5-small | multilingual-e5-base | multilingual-e5-large |
|:----------------------------------|:--------------------|-----------------------:|--------------------:|----------------:|------------------:|----------------------:|----------------------:|---------------------:|
|Classification                     | Accuracy            |         0.554          |        0.552        |      0.514      |        0.535      |        0.551          |        0.561          |      **0.588**       |
|Clustering                         | V-measure           |       **0.526**        |        0.519        |      0.412      |        0.496      |        0.513          |        0.503          |        0.525         |
|MultiLabelClassification           | Accuracy            |         0.326          |        0.319        |      0.294      |        0.317      |        0.314          |        0.329          |      **0.353**       |
|PairClassification                 | Average Precision   |         0.520          |        0.502        |      0.519      |        0.563      |        0.551          |        0.550          |      **0.584**       |
|Reranking                          | MAP@10              |         0.561          |        0.468        |      0.461      |        0.622      |        0.715          |        0.720          |      **0.756**       |
|Retrieval                          | NDCG@10             |         0.256          |        0.118        |      0.124      |        0.515      |        0.697          |        0.699          |      **0.774**       |
|STS                                | Pearson correlation |         0.712          |        0.588        |      0.694      |        0.787      |        0.781          |        0.796          |      **0.831**       |
|Average                            | Average             |         0.494          |        0.438        |      0.431      |        0.548      |        0.588          |        0.594          |      **0.630**       |



