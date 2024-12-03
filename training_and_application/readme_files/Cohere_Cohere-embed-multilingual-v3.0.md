---
tags:
- mteb
model-index:
- name: embed-multilingual-v3.0
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
      value: 77.85074626865672
    - type: ap
      value: 41.53151744002314
    - type: f1
      value: 71.94656880817726
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
      value: 95.600375
    - type: ap
      value: 93.57882128753579
    - type: f1
      value: 95.59945484944305
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
      value: 49.794
    - type: f1
      value: 48.740439663130985
  - task:
      type: Retrieval
    dataset:
      type: arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 55.105000000000004
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
      value: 48.15653426568874
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
      value: 40.78876256237919
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
      value: 62.12873500780318
    - type: mrr
      value: 75.87037769863255
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
      value: 86.01183720167818
    - type: cos_sim_spearman
      value: 85.00916590717613
    - type: euclidean_pearson
      value: 84.072733561361
    - type: euclidean_spearman
      value: 85.00916590717613
    - type: manhattan_pearson
      value: 83.89233507343208
    - type: manhattan_spearman
      value: 84.87482549674115
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
      value: 86.09415584415584
    - type: f1
      value: 86.05173549773973
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
      value: 40.49773000165541
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
      value: 36.909633073998876
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 49.481
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 47.449999999999996
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 59.227
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 37.729
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 29.673
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 44.278
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 43.218
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 40.63741666666667
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 33.341
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 29.093999999999998
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 40.801
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 40.114
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 33.243
  - task:
      type: Retrieval
    dataset:
      type: climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 29.958000000000002
  - task:
      type: Retrieval
    dataset:
      type: dbpedia-entity
      name: MTEB DBPedia
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 41.004000000000005
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
      value: 48.150000000000006
    - type: f1
      value: 43.69803436468346
  - task:
      type: Retrieval
    dataset:
      type: fever
      name: MTEB FEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 88.532
  - task:
      type: Retrieval
    dataset:
      type: fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 44.105
  - task:
      type: Retrieval
    dataset:
      type: hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 70.612
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
      value: 93.9672
    - type: ap
      value: 90.72947025321227
    - type: f1
      value: 93.96271599852622
  - task:
      type: Retrieval
    dataset:
      type: msmarco
      name: MTEB MSMARCO
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 43.447
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
      value: 94.92476060191517
    - type: f1
      value: 94.69383758972194
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
      value: 78.8873689010488
    - type: f1
      value: 62.537485052253885
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
      value: 74.51244115669132
    - type: f1
      value: 72.40074466830153
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
      value: 79.00470746469401
    - type: f1
      value: 79.03758200183096
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
      value: 36.183215937303736
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
      value: 33.443759055792135
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
      value: 32.58713095176127
    - type: mrr
      value: 33.7326038566206
  - task:
      type: Retrieval
    dataset:
      type: nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 36.417
  - task:
      type: Retrieval
    dataset:
      type: nq
      name: MTEB NQ
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 63.415
  - task:
      type: Retrieval
    dataset:
      type: quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 88.924
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
      value: 58.10997801688676
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
      value: 65.02444843766075
  - task:
      type: Retrieval
    dataset:
      type: scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 19.339000000000002
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
      value: 86.61540076033945
    - type: cos_sim_spearman
      value: 82.1820253476181
    - type: euclidean_pearson
      value: 83.73901215845989
    - type: euclidean_spearman
      value: 82.182021064594
    - type: manhattan_pearson
      value: 83.76685139192031
    - type: manhattan_spearman
      value: 82.14074705306663
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
      value: 85.62241109228789
    - type: cos_sim_spearman
      value: 77.62042143066208
    - type: euclidean_pearson
      value: 82.77237785274072
    - type: euclidean_spearman
      value: 77.62042142290566
    - type: manhattan_pearson
      value: 82.70945589621266
    - type: manhattan_spearman
      value: 77.57245632826351
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
      value: 84.8307075352031
    - type: cos_sim_spearman
      value: 85.15620774806095
    - type: euclidean_pearson
      value: 84.21956724564915
    - type: euclidean_spearman
      value: 85.15620774806095
    - type: manhattan_pearson
      value: 84.0677597021641
    - type: manhattan_spearman
      value: 85.02572172855729
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
      value: 83.33749463516592
    - type: cos_sim_spearman
      value: 80.01967438481185
    - type: euclidean_pearson
      value: 82.16884494022196
    - type: euclidean_spearman
      value: 80.01967218194336
    - type: manhattan_pearson
      value: 81.94431512413773
    - type: manhattan_spearman
      value: 79.81636247503731
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
      value: 88.2070761097028
    - type: cos_sim_spearman
      value: 88.92297656560552
    - type: euclidean_pearson
      value: 87.95961374550303
    - type: euclidean_spearman
      value: 88.92298798854765
    - type: manhattan_pearson
      value: 87.85515971478168
    - type: manhattan_spearman
      value: 88.8100644762342
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
      value: 85.48103354546488
    - type: cos_sim_spearman
      value: 86.91850928862898
    - type: euclidean_pearson
      value: 86.06766986527145
    - type: euclidean_spearman
      value: 86.91850928862898
    - type: manhattan_pearson
      value: 86.02705585360717
    - type: manhattan_spearman
      value: 86.86666545434721
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
      value: 90.30267248880148
    - type: cos_sim_spearman
      value: 90.08752166657892
    - type: euclidean_pearson
      value: 90.4697525265135
    - type: euclidean_spearman
      value: 90.08752166657892
    - type: manhattan_pearson
      value: 90.57174978064741
    - type: manhattan_spearman
      value: 90.212834942229
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
      value: 67.10616236380835
    - type: cos_sim_spearman
      value: 66.81483164137016
    - type: euclidean_pearson
      value: 68.48505128040803
    - type: euclidean_spearman
      value: 66.81483164137016
    - type: manhattan_pearson
      value: 68.46133268524885
    - type: manhattan_spearman
      value: 66.83684227990202
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
      value: 87.12768629069949
    - type: cos_sim_spearman
      value: 88.78683817318573
    - type: euclidean_pearson
      value: 88.47603251297261
    - type: euclidean_spearman
      value: 88.78683817318573
    - type: manhattan_pearson
      value: 88.46483630890225
    - type: manhattan_spearman
      value: 88.76593424921617
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
      value: 84.30886658431281
    - type: mrr
      value: 95.5964251797585
  - task:
      type: Retrieval
    dataset:
      type: scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 70.04599999999999
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
      value: 99.87524752475248
    - type: cos_sim_ap
      value: 96.79160651306724
    - type: cos_sim_f1
      value: 93.57798165137615
    - type: cos_sim_precision
      value: 95.42619542619542
    - type: cos_sim_recall
      value: 91.8
    - type: dot_accuracy
      value: 99.87524752475248
    - type: dot_ap
      value: 96.79160651306724
    - type: dot_f1
      value: 93.57798165137615
    - type: dot_precision
      value: 95.42619542619542
    - type: dot_recall
      value: 91.8
    - type: euclidean_accuracy
      value: 99.87524752475248
    - type: euclidean_ap
      value: 96.79160651306724
    - type: euclidean_f1
      value: 93.57798165137615
    - type: euclidean_precision
      value: 95.42619542619542
    - type: euclidean_recall
      value: 91.8
    - type: manhattan_accuracy
      value: 99.87326732673267
    - type: manhattan_ap
      value: 96.7574606340297
    - type: manhattan_f1
      value: 93.45603271983639
    - type: manhattan_precision
      value: 95.60669456066945
    - type: manhattan_recall
      value: 91.4
    - type: max_accuracy
      value: 99.87524752475248
    - type: max_ap
      value: 96.79160651306724
    - type: max_f1
      value: 93.57798165137615
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
      value: 68.12288811917144
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
      value: 35.22267280169542
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
      value: 52.39780995606098
    - type: mrr
      value: 53.26826563958916
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
      value: 31.15118979569649
    - type: cos_sim_spearman
      value: 30.99428921914572
    - type: dot_pearson
      value: 31.151189338601924
    - type: dot_spearman
      value: 30.99428921914572
  - task:
      type: Retrieval
    dataset:
      type: trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 83.372
  - task:
      type: Retrieval
    dataset:
      type: webis-touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 32.698
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
      value: 71.1998
    - type: ap
      value: 14.646205259325157
    - type: f1
      value: 54.96172518137252
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
      value: 62.176004527447645
    - type: f1
      value: 62.48549068096645
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
      value: 50.13767789739772
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
      value: 86.38016331882935
    - type: cos_sim_ap
      value: 75.1635976260804
    - type: cos_sim_f1
      value: 69.29936305732484
    - type: cos_sim_precision
      value: 66.99507389162561
    - type: cos_sim_recall
      value: 71.76781002638522
    - type: dot_accuracy
      value: 86.38016331882935
    - type: dot_ap
      value: 75.16359359202374
    - type: dot_f1
      value: 69.29936305732484
    - type: dot_precision
      value: 66.99507389162561
    - type: dot_recall
      value: 71.76781002638522
    - type: euclidean_accuracy
      value: 86.38016331882935
    - type: euclidean_ap
      value: 75.16360246558416
    - type: euclidean_f1
      value: 69.29936305732484
    - type: euclidean_precision
      value: 66.99507389162561
    - type: euclidean_recall
      value: 71.76781002638522
    - type: manhattan_accuracy
      value: 86.27883411813792
    - type: manhattan_ap
      value: 75.02872038741897
    - type: manhattan_f1
      value: 69.29256284011403
    - type: manhattan_precision
      value: 68.07535641547861
    - type: manhattan_recall
      value: 70.55408970976254
    - type: max_accuracy
      value: 86.38016331882935
    - type: max_ap
      value: 75.16360246558416
    - type: max_f1
      value: 69.29936305732484
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
      value: 89.39729110878255
    - type: cos_sim_ap
      value: 86.48560260020555
    - type: cos_sim_f1
      value: 79.35060602690982
    - type: cos_sim_precision
      value: 76.50632549496105
    - type: cos_sim_recall
      value: 82.41453649522637
    - type: dot_accuracy
      value: 89.39729110878255
    - type: dot_ap
      value: 86.48559829915334
    - type: dot_f1
      value: 79.35060602690982
    - type: dot_precision
      value: 76.50632549496105
    - type: dot_recall
      value: 82.41453649522637
    - type: euclidean_accuracy
      value: 89.39729110878255
    - type: euclidean_ap
      value: 86.48559993122497
    - type: euclidean_f1
      value: 79.35060602690982
    - type: euclidean_precision
      value: 76.50632549496105
    - type: euclidean_recall
      value: 82.41453649522637
    - type: manhattan_accuracy
      value: 89.36042224550782
    - type: manhattan_ap
      value: 86.47238558562499
    - type: manhattan_f1
      value: 79.24500641378047
    - type: manhattan_precision
      value: 75.61726236273344
    - type: manhattan_recall
      value: 83.23837388358484
    - type: max_accuracy
      value: 89.39729110878255
    - type: max_ap
      value: 86.48560260020555
    - type: max_f1
      value: 79.35060602690982
---


# Cohere embed-multilingual-v3.0

This repository contains the tokenizer for the Cohere `embed-multilingual-v3.0` model. See our blogpost [Cohere Embed V3](https://txt.cohere.com/introducing-embed-v3/) for more details on this model.

You can use the embedding model either via the Cohere API, AWS SageMaker or in your private deployments.

## Usage Cohere API

The following code snippet shows the usage of the Cohere API. Install the cohere SDK via:
```
pip install -U cohere
```

Get your free API key on: www.cohere.com


```python
# This snippet shows and example how to use the Cohere Embed V3 models for semantic search.
# Make sure to have the Cohere SDK in at least v4.30 install: pip install -U cohere 
# Get your API key from: www.cohere.com
import cohere
import numpy as np

cohere_key = "{YOUR_COHERE_API_KEY}"   #Get your API key from www.cohere.com
co = cohere.Client(cohere_key)

docs = ["The capital of France is Paris",
        "PyTorch is a machine learning framework based on the Torch library.",
        "The average cat lifespan is between 13-17 years"]


#Encode your documents with input type 'search_document'
doc_emb = co.embed(docs, input_type="search_document", model="embed-multilingual-v3.0").embeddings
doc_emb = np.asarray(doc_emb)


#Encode your query with input type 'search_query'
query = "What is Pytorch"
query_emb = co.embed([query], input_type="search_query", model="embed-multilingual-v3.0").embeddings
query_emb = np.asarray(query_emb)
query_emb.shape

#Compute the dot product between query embedding and document embedding
scores = np.dot(query_emb, doc_emb.T)[0]

#Find the highest scores
max_idx = np.argsort(-scores)

print(f"Query: {query}")
for idx in max_idx:
  print(f"Score: {scores[idx]:.2f}")
  print(docs[idx])
  print("--------")
```

## Usage AWS SageMaker
The embedding model can be privately deployed in your AWS Cloud using our [AWS SageMaker marketplace offering](https://aws.amazon.com/marketplace/pp/prodview-z6huxszcqc25i). It runs privately in your VPC, with latencies as low as 5ms for query encoding.

## Usage AWS Bedrock
Soon the model will also be available via AWS Bedrock. Stay tuned

## Private Deployment
You want to run the model on your own hardware? [Contact Sales](https://cohere.com/contact-sales) to learn more.

## Supported Languages
This model was trained on nearly 1B English training pairs and nearly 0.5B Non-English training pairs from 100+ languages. 

Evaluation results can be found in the [Embed V3.0 Benchmark Results spreadsheet](https://docs.google.com/spreadsheets/d/1w7gnHWMDBdEUrmHgSfDnGHJgVQE5aOiXCCwO3uNH_mI/edit?usp=sharing).