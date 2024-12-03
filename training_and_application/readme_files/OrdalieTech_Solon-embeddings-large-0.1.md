---
tags:
- mteb
model-index:
- name: Solon-embeddings-large-0.1
  results:
  - task:
      type: sentence-similarity
      name: Passage Retrieval
    dataset:
      type: unicamp-dl/mmarco
      name: mMARCO-fr
      config: french
      split: validation
    metrics:
      - type: recall_at_500
        name: Recall@500
        value: 92.7
      - type: recall_at_100
        name: Recall@100
        value: 82.7
      - type: recall_at_10
        name: Recall@10
        value: 55.5
      - type: map_at_10
        name: MAP@10
        value: 29.4
      - type: ndcg_at_10
        name: nDCG@10
        value: 35.8
      - type: mrr_at_10
        name: MRR@10
        value: 29.9
  - task:
      type: Clustering
    dataset:
      type: lyon-nlp/alloprof
      name: MTEB AlloProfClusteringP2P
      config: default
      split: test
      revision: 392ba3f5bcc8c51f578786c1fc3dae648662cb9b
    metrics:
    - type: v_measure
      value: 64.16942168287153
  - task:
      type: Clustering
    dataset:
      type: lyon-nlp/alloprof
      name: MTEB AlloProfClusteringS2S
      config: default
      split: test
      revision: 392ba3f5bcc8c51f578786c1fc3dae648662cb9b
    metrics:
    - type: v_measure
      value: 38.17076313383054
  - task:
      type: Reranking
    dataset:
      type: lyon-nlp/mteb-fr-reranking-alloprof-s2p
      name: MTEB AlloprofReranking
      config: default
      split: test
      revision: 666fdacebe0291776e86f29345663dfaf80a0db9
    metrics:
    - type: map
      value: 64.8770878097632
    - type: mrr
      value: 66.39132423169396
  - task:
      type: Retrieval
    dataset:
      type: lyon-nlp/alloprof
      name: MTEB AlloprofRetrieval
      config: default
      split: test
      revision: 392ba3f5bcc8c51f578786c1fc3dae648662cb9b
    metrics:
    - type: map_at_1
      value: 29.62
    - type: map_at_10
      value: 40.963
    - type: map_at_100
      value: 41.894
    - type: map_at_1000
      value: 41.939
    - type: map_at_3
      value: 37.708999999999996
    - type: map_at_5
      value: 39.696999999999996
    - type: mrr_at_1
      value: 29.62
    - type: mrr_at_10
      value: 40.963
    - type: mrr_at_100
      value: 41.894
    - type: mrr_at_1000
      value: 41.939
    - type: mrr_at_3
      value: 37.708999999999996
    - type: mrr_at_5
      value: 39.696999999999996
    - type: ndcg_at_1
      value: 29.62
    - type: ndcg_at_10
      value: 46.942
    - type: ndcg_at_100
      value: 51.629999999999995
    - type: ndcg_at_1000
      value: 52.927
    - type: ndcg_at_3
      value: 40.333999999999996
    - type: ndcg_at_5
      value: 43.922
    - type: precision_at_1
      value: 29.62
    - type: precision_at_10
      value: 6.589
    - type: precision_at_100
      value: 0.882
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_3
      value: 15.976
    - type: precision_at_5
      value: 11.33
    - type: recall_at_1
      value: 29.62
    - type: recall_at_10
      value: 65.889
    - type: recall_at_100
      value: 88.212
    - type: recall_at_1000
      value: 98.575
    - type: recall_at_3
      value: 47.927
    - type: recall_at_5
      value: 56.64900000000001
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
      value: 42.077999999999996
    - type: f1
      value: 40.64511241732637
  - task:
      type: Retrieval
    dataset:
      type: maastrichtlawtech/bsard
      name: MTEB BSARDRetrieval
      config: default
      split: test
      revision: 5effa1b9b5fa3b0f9e12523e6e43e5f86a6e6d59
    metrics:
    - type: map_at_1
      value: 0.901
    - type: map_at_10
      value: 1.524
    - type: map_at_100
      value: 1.833
    - type: map_at_1000
      value: 1.916
    - type: map_at_3
      value: 1.276
    - type: map_at_5
      value: 1.276
    - type: mrr_at_1
      value: 0.901
    - type: mrr_at_10
      value: 1.524
    - type: mrr_at_100
      value: 1.833
    - type: mrr_at_1000
      value: 1.916
    - type: mrr_at_3
      value: 1.276
    - type: mrr_at_5
      value: 1.276
    - type: ndcg_at_1
      value: 0.901
    - type: ndcg_at_10
      value: 2.085
    - type: ndcg_at_100
      value: 3.805
    - type: ndcg_at_1000
      value: 6.704000000000001
    - type: ndcg_at_3
      value: 1.41
    - type: ndcg_at_5
      value: 1.41
    - type: precision_at_1
      value: 0.901
    - type: precision_at_10
      value: 0.40499999999999997
    - type: precision_at_100
      value: 0.126
    - type: precision_at_1000
      value: 0.037
    - type: precision_at_3
      value: 0.601
    - type: precision_at_5
      value: 0.36
    - type: recall_at_1
      value: 0.901
    - type: recall_at_10
      value: 4.054
    - type: recall_at_100
      value: 12.613
    - type: recall_at_1000
      value: 36.937
    - type: recall_at_3
      value: 1.802
    - type: recall_at_5
      value: 1.802
  - task:
      type: BitextMining
    dataset:
      type: rbawden/DiaBLa
      name: MTEB DiaBLaBitextMining (fr-en)
      config: fr-en
      split: test
      revision: 5345895c56a601afe1a98519ce3199be60a27dba
    metrics:
    - type: accuracy
      value: 88.90048712595686
    - type: f1
      value: 86.94952864886115
    - type: precision
      value: 86.20344379175826
    - type: recall
      value: 88.90048712595686
  - task:
      type: Clustering
    dataset:
      type: lyon-nlp/clustering-hal-s2s
      name: MTEB HALClusteringS2S
      config: default
      split: test
      revision: e06ebbbb123f8144bef1a5d18796f3dec9ae2915
    metrics:
    - type: v_measure
      value: 24.087988843991155
  - task:
      type: Clustering
    dataset:
      type: mlsum
      name: MTEB MLSUMClusteringP2P
      config: default
      split: test
      revision: b5d54f8f3b61ae17845046286940f03c6bc79bc7
    metrics:
    - type: v_measure
      value: 43.79603865728535
  - task:
      type: Clustering
    dataset:
      type: mlsum
      name: MTEB MLSUMClusteringS2S
      config: default
      split: test
      revision: b5d54f8f3b61ae17845046286940f03c6bc79bc7
    metrics:
    - type: v_measure
      value: 37.746550373003
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
      value: 89.26088318196052
    - type: f1
      value: 88.95811185929033
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
      value: 68.55308487316003
    - type: f1
      value: 48.2936682439785
  - task:
      type: Classification
    dataset:
      type: masakhane/masakhanews
      name: MTEB MasakhaNEWSClassification (fra)
      config: fra
      split: test
      revision: 8ccc72e69e65f40c70e117d8b3c08306bb788b60
    metrics:
    - type: accuracy
      value: 81.51658767772511
    - type: f1
      value: 77.695234448912
  - task:
      type: Clustering
    dataset:
      type: masakhane/masakhanews
      name: MTEB MasakhaNEWSClusteringP2P (fra)
      config: fra
      split: test
      revision: 8ccc72e69e65f40c70e117d8b3c08306bb788b60
    metrics:
    - type: v_measure
      value: 40.80377094681114
  - task:
      type: Clustering
    dataset:
      type: masakhane/masakhanews
      name: MTEB MasakhaNEWSClusteringS2S (fra)
      config: fra
      split: test
      revision: 8ccc72e69e65f40c70e117d8b3c08306bb788b60
    metrics:
    - type: v_measure
      value: 28.79703837416241
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
      value: 67.40080699394755
    - type: f1
      value: 65.60793135686376
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
      value: 71.29455279085406
    - type: f1
      value: 70.80876673828983
  - task:
      type: Retrieval
    dataset:
      type: jinaai/mintakaqa
      name: MTEB MintakaRetrieval (fr)
      config: fr
      split: test
      revision: efa78cc2f74bbcd21eff2261f9e13aebe40b814e
    metrics:
    - type: map_at_1
      value: 16.625999999999998
    - type: map_at_10
      value: 25.224999999999998
    - type: map_at_100
      value: 26.291999999999998
    - type: map_at_1000
      value: 26.395000000000003
    - type: map_at_3
      value: 22.378999999999998
    - type: map_at_5
      value: 24.009
    - type: mrr_at_1
      value: 16.625999999999998
    - type: mrr_at_10
      value: 25.224999999999998
    - type: mrr_at_100
      value: 26.291999999999998
    - type: mrr_at_1000
      value: 26.395000000000003
    - type: mrr_at_3
      value: 22.378999999999998
    - type: mrr_at_5
      value: 24.009
    - type: ndcg_at_1
      value: 16.625999999999998
    - type: ndcg_at_10
      value: 30.074
    - type: ndcg_at_100
      value: 35.683
    - type: ndcg_at_1000
      value: 38.714999999999996
    - type: ndcg_at_3
      value: 24.188000000000002
    - type: ndcg_at_5
      value: 27.124
    - type: precision_at_1
      value: 16.625999999999998
    - type: precision_at_10
      value: 4.566
    - type: precision_at_100
      value: 0.729
    - type: precision_at_1000
      value: 0.097
    - type: precision_at_3
      value: 9.801
    - type: precision_at_5
      value: 7.305000000000001
    - type: recall_at_1
      value: 16.625999999999998
    - type: recall_at_10
      value: 45.659
    - type: recall_at_100
      value: 72.85000000000001
    - type: recall_at_1000
      value: 97.42
    - type: recall_at_3
      value: 29.402
    - type: recall_at_5
      value: 36.527
  - task:
      type: PairClassification
    dataset:
      type: GEM/opusparcus
      name: MTEB OpusparcusPC (fr)
      config: fr
      split: test
      revision: 9e9b1f8ef51616073f47f306f7f47dd91663f86a
    metrics:
    - type: cos_sim_accuracy
      value: 83.58310626702998
    - type: cos_sim_ap
      value: 94.01979957812989
    - type: cos_sim_f1
      value: 88.70135958743555
    - type: cos_sim_precision
      value: 84.01420959147424
    - type: cos_sim_recall
      value: 93.94240317775571
    - type: dot_accuracy
      value: 83.58310626702998
    - type: dot_ap
      value: 94.01979957812989
    - type: dot_f1
      value: 88.70135958743555
    - type: dot_precision
      value: 84.01420959147424
    - type: dot_recall
      value: 93.94240317775571
    - type: euclidean_accuracy
      value: 83.58310626702998
    - type: euclidean_ap
      value: 94.01979957812989
    - type: euclidean_f1
      value: 88.70135958743555
    - type: euclidean_precision
      value: 84.01420959147424
    - type: euclidean_recall
      value: 93.94240317775571
    - type: manhattan_accuracy
      value: 83.58310626702998
    - type: manhattan_ap
      value: 93.99936024003892
    - type: manhattan_f1
      value: 88.6924150767799
    - type: manhattan_precision
      value: 83.45008756567425
    - type: manhattan_recall
      value: 94.63753723932473
    - type: max_accuracy
      value: 83.58310626702998
    - type: max_ap
      value: 94.01979957812989
    - type: max_f1
      value: 88.70135958743555
  - task:
      type: PairClassification
    dataset:
      type: paws-x
      name: MTEB PawsX (fr)
      config: fr
      split: test
      revision: 8a04d940a42cd40658986fdd8e3da561533a3646
    metrics:
    - type: cos_sim_accuracy
      value: 60.6
    - type: cos_sim_ap
      value: 60.18915797975459
    - type: cos_sim_f1
      value: 62.491349480968864
    - type: cos_sim_precision
      value: 45.44539506794162
    - type: cos_sim_recall
      value: 100
    - type: dot_accuracy
      value: 60.6
    - type: dot_ap
      value: 60.091135216056024
    - type: dot_f1
      value: 62.491349480968864
    - type: dot_precision
      value: 45.44539506794162
    - type: dot_recall
      value: 100
    - type: euclidean_accuracy
      value: 60.6
    - type: euclidean_ap
      value: 60.18915797975459
    - type: euclidean_f1
      value: 62.491349480968864
    - type: euclidean_precision
      value: 45.44539506794162
    - type: euclidean_recall
      value: 100
    - type: manhattan_accuracy
      value: 60.650000000000006
    - type: manhattan_ap
      value: 60.2082343915352
    - type: manhattan_f1
      value: 62.491349480968864
    - type: manhattan_precision
      value: 45.44539506794162
    - type: manhattan_recall
      value: 100
    - type: max_accuracy
      value: 60.650000000000006
    - type: max_ap
      value: 60.2082343915352
    - type: max_f1
      value: 62.491349480968864
  - task:
      type: STS
    dataset:
      type: Lajavaness/SICK-fr
      name: MTEB SICKFr
      config: default
      split: test
      revision: e077ab4cf4774a1e36d86d593b150422fafd8e8a
    metrics:
    - type: cos_sim_pearson
      value: 79.77067200230256
    - type: cos_sim_spearman
      value: 76.7445532523278
    - type: euclidean_pearson
      value: 76.34017074673956
    - type: euclidean_spearman
      value: 76.7453011027832
    - type: manhattan_pearson
      value: 76.19578084197778
    - type: manhattan_spearman
      value: 76.56293456459228
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (fr)
      config: fr
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_pearson
      value: 81.2564160237984
    - type: cos_sim_spearman
      value: 83.30552085410882
    - type: euclidean_pearson
      value: 82.00494560507786
    - type: euclidean_spearman
      value: 83.30552085410882
    - type: manhattan_pearson
      value: 81.93132229157803
    - type: manhattan_spearman
      value: 83.04357992939353
  - task:
      type: STS
    dataset:
      type: stsb_multi_mt
      name: MTEB STSBenchmarkMultilingualSTS (fr)
      config: fr
      split: test
      revision: 93d57ef91790589e3ce9c365164337a8a78b7632
    metrics:
    - type: cos_sim_pearson
      value: 80.34931905288978
    - type: cos_sim_spearman
      value: 79.99372771100049
    - type: euclidean_pearson
      value: 78.37976845123443
    - type: euclidean_spearman
      value: 79.99452356550658
    - type: manhattan_pearson
      value: 78.24434042082316
    - type: manhattan_spearman
      value: 79.87248340061164
  - task:
      type: Summarization
    dataset:
      type: lyon-nlp/summarization-summeval-fr-p2p
      name: MTEB SummEvalFr
      config: default
      split: test
      revision: b385812de6a9577b6f4d0f88c6a6e35395a94054
    metrics:
    - type: cos_sim_pearson
      value: 30.476001473421586
    - type: cos_sim_spearman
      value: 29.687350195905456
    - type: dot_pearson
      value: 30.476000875190685
    - type: dot_spearman
      value: 29.662224660056562
  - task:
      type: Reranking
    dataset:
      type: lyon-nlp/mteb-fr-reranking-syntec-s2p
      name: MTEB SyntecReranking
      config: default
      split: test
      revision: b205c5084a0934ce8af14338bf03feb19499c84d
    metrics:
    - type: map
      value: 88.28333333333333
    - type: mrr
      value: 88.28333333333333
  - task:
      type: Retrieval
    dataset:
      type: lyon-nlp/mteb-fr-retrieval-syntec-s2p
      name: MTEB SyntecRetrieval
      config: default
      split: test
      revision: 77f7e271bf4a92b24fce5119f3486b583ca016ff
    metrics:
    - type: map_at_1
      value: 69
    - type: map_at_10
      value: 79.906
    - type: map_at_100
      value: 79.982
    - type: map_at_1000
      value: 79.982
    - type: map_at_3
      value: 77.667
    - type: map_at_5
      value: 79.51700000000001
    - type: mrr_at_1
      value: 69
    - type: mrr_at_10
      value: 79.906
    - type: mrr_at_100
      value: 79.982
    - type: mrr_at_1000
      value: 79.982
    - type: mrr_at_3
      value: 77.667
    - type: mrr_at_5
      value: 79.51700000000001
    - type: ndcg_at_1
      value: 69
    - type: ndcg_at_10
      value: 84.60499999999999
    - type: ndcg_at_100
      value: 84.868
    - type: ndcg_at_1000
      value: 84.868
    - type: ndcg_at_3
      value: 80.333
    - type: ndcg_at_5
      value: 83.647
    - type: precision_at_1
      value: 69
    - type: precision_at_10
      value: 9.9
    - type: precision_at_100
      value: 1
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 29.333
    - type: precision_at_5
      value: 19.2
    - type: recall_at_1
      value: 69
    - type: recall_at_10
      value: 99
    - type: recall_at_100
      value: 100
    - type: recall_at_1000
      value: 100
    - type: recall_at_3
      value: 88
    - type: recall_at_5
      value: 96
  - task:
      type: Retrieval
    dataset:
      type: jinaai/xpqa
      name: MTEB XPQARetrieval (fr)
      config: fr
      split: test
      revision: c99d599f0a6ab9b85b065da6f9d94f9cf731679f
    metrics:
    - type: map_at_1
      value: 42.027
    - type: map_at_10
      value: 64.331
    - type: map_at_100
      value: 65.657
    - type: map_at_1000
      value: 65.7
    - type: map_at_3
      value: 57.967999999999996
    - type: map_at_5
      value: 62.33800000000001
    - type: mrr_at_1
      value: 65.688
    - type: mrr_at_10
      value: 72.263
    - type: mrr_at_100
      value: 72.679
    - type: mrr_at_1000
      value: 72.69099999999999
    - type: mrr_at_3
      value: 70.405
    - type: mrr_at_5
      value: 71.587
    - type: ndcg_at_1
      value: 65.688
    - type: ndcg_at_10
      value: 70.221
    - type: ndcg_at_100
      value: 74.457
    - type: ndcg_at_1000
      value: 75.178
    - type: ndcg_at_3
      value: 65.423
    - type: ndcg_at_5
      value: 67.05499999999999
    - type: precision_at_1
      value: 65.688
    - type: precision_at_10
      value: 16.208
    - type: precision_at_100
      value: 1.975
    - type: precision_at_1000
      value: 0.207
    - type: precision_at_3
      value: 39.831
    - type: precision_at_5
      value: 28.652
    - type: recall_at_1
      value: 42.027
    - type: recall_at_10
      value: 78.803
    - type: recall_at_100
      value: 95.051
    - type: recall_at_1000
      value: 99.75500000000001
    - type: recall_at_3
      value: 62.62799999999999
    - type: recall_at_5
      value: 70.975
license: mit
language:
- fr
---

# Solon Embeddings — large 0.1

SOTA Open source french embedding model.

**Instructions :**  
Add "query : " before the *query* to retrieve to increase performance of retrieval.  
No instructions needed for *passages*.


| Model | Mean Score |
| --- | --- |
| **OrdalieTech/Solon-embeddings-large-0.1** | 0.7490 |
| cohere/embed-multilingual-v3 | 0.7402 |
| **OrdalieTech/Solon-embeddings-base-0.1** | 0.7306 |
| openai/ada-002 | 0.7290 |
| cohere/embed-multilingual-light-v3 | 0.6945 |
| antoinelouis/biencoder-camembert-base-mmarcoFR | 0.6826 |
| dangvantuan/sentence-camembert-large | 0.6756 |
| voyage/voyage-01 | 0.6753 |
| intfloat/multilingual-e5-large | 0.6660 |
| intfloat/multilingual-e5-base | 0.6597 |
| Sbert/paraphrase-multilingual-mpnet-base-v2 | 0.5975 |
| dangvantuan/sentence-camembert-base | 0.5456 |
| EuropeanParliament/eubert_embedding_v1 | 0.5063 |

These results have been obtained through 9 french benchmarks on a variety of text similarity tasks (classification, reranking, STS) :
- AmazonReviewsClassification (MTEB)
- MassiveIntentClassification (MTEB)
- MassiveScenarioClassification (MTEB)
- MTOPDomainClassification (MTEB)
- MTOPIntentClassification (MTEB)
- STS22 (MTEB)
- MiraclFRRerank (Miracl)
- OrdalieFRSTS (Ordalie)
- OrdalieFRReranking (Ordalie)

We created OrdalieFRSTS and OrdalieFRReranking to enhance the benchmarking capabilities of French STS and reranking assessments.

(evaluation script available here : github.com/OrdalieTech/mteb)