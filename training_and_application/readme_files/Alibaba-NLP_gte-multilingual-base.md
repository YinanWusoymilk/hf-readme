---
tags:
- mteb
- sentence-transformers
- transformers
- multilingual
- sentence-similarity
license: apache-2.0
language:
- af
- ar
- az
- be
- bg
- bn
- ca
- ceb
- cs
- cy
- da
- de
- el
- en
- es
- et
- eu
- fa
- fi
- fr
- gl
- gu
- he
- hi
- hr
- ht
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ky
- lo
- lt
- lv
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- 'no'
- pa
- pl
- pt
- qu
- ro
- ru
- si
- sk
- sl
- so
- sq
- sr
- sv
- sw
- ta
- te
- th
- tl
- tr
- uk
- ur
- vi
- yo
- zh
model-index:
- name: gte-multilingual-base (dense)
  results:
  - task:
      type: Clustering
    dataset:
      type: PL-MTEB/8tags-clustering
      name: MTEB 8TagsClustering
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 33.66681726329994
  - task:
      type: STS
    dataset:
      type: C-MTEB/AFQMC
      name: MTEB AFQMC
      config: default
      split: validation
      revision: b44c3b011063adb25877c13823db83bb193913c4
    metrics:
    - type: cos_sim_spearman
      value: 43.54760696384009
  - task:
      type: STS
    dataset:
      type: C-MTEB/ATEC
      name: MTEB ATEC
      config: default
      split: test
      revision: 0f319b1142f28d00e055a6770f3f726ae9b7d865
    metrics:
    - type: cos_sim_spearman
      value: 48.91186363417501
  - task:
      type: Classification
    dataset:
      type: PL-MTEB/allegro-reviews
      name: MTEB AllegroReviews
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 41.689860834990064
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
      value: 54.20241337977897
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
      value: 44.34083695608643
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
      value: 64.91495250072002
  - task:
      type: Retrieval
    dataset:
      type: lyon-nlp/alloprof
      name: MTEB AlloprofRetrieval
      config: default
      split: test
      revision: 392ba3f5bcc8c51f578786c1fc3dae648662cb9b
    metrics:
    - type: ndcg_at_10
      value: 53.638
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
      value: 75.95522388059702
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
      value: 80.717625
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
      value: 43.64199999999999
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
      value: 40.108
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
      value: 40.169999999999995
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
      value: 39.56799999999999
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
      value: 35.75000000000001
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
      value: 33.342000000000006
  - task:
      type: Retrieval
    dataset:
      type: mteb/arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
    metrics:
    - type: ndcg_at_10
      value: 58.231
  - task:
      type: Retrieval
    dataset:
      type: clarin-knext/arguana-pl
      name: MTEB ArguAna-PL
      config: default
      split: test
      revision: 63fc86750af76253e8c760fc9e534bbf24d260a2
    metrics:
    - type: ndcg_at_10
      value: 53.166000000000004
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
      value: 46.01900557959478
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
      value: 41.06626465345723
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
      value: 61.87514497610431
  - task:
      type: STS
    dataset:
      type: mteb/biosses-sts
      name: MTEB BIOSSES
      config: default
      split: test
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
    metrics:
    - type: cos_sim_spearman
      value: 81.21450112991194
  - task:
      type: STS
    dataset:
      type: C-MTEB/BQ
      name: MTEB BQ
      config: default
      split: test
      revision: e3dda5e115e487b39ec7e618c0c6a29137052a55
    metrics:
    - type: cos_sim_spearman
      value: 51.71589543397271
  - task:
      type: Retrieval
    dataset:
      type: maastrichtlawtech/bsard
      name: MTEB BSARDRetrieval
      config: default
      split: test
      revision: 5effa1b9b5fa3b0f9e12523e6e43e5f86a6e6d59
    metrics:
    - type: ndcg_at_10
      value: 26.115
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (de-en)
      config: de-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: f1
      value: 98.6169102296451
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (fr-en)
      config: fr-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: f1
      value: 97.89603052314916
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (ru-en)
      config: ru-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: f1
      value: 97.12388869645537
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (zh-en)
      config: zh-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: f1
      value: 98.15692469720906
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
      value: 85.36038961038962
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
      value: 37.5903826674123
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
      value: 34.21474277151329
  - task:
      type: Classification
    dataset:
      type: PL-MTEB/cbd
      name: MTEB CBD
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 62.519999999999996
  - task:
      type: PairClassification
    dataset:
      type: PL-MTEB/cdsce-pairclassification
      name: MTEB CDSC-E
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_ap
      value: 74.90132799162956
  - task:
      type: STS
    dataset:
      type: PL-MTEB/cdscr-sts
      name: MTEB CDSC-R
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_spearman
      value: 90.30727955142524
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/CLSClusteringP2P
      name: MTEB CLSClusteringP2P
      config: default
      split: test
      revision: 4b6227591c6c1a73bc76b1055f3b7f3588e72476
    metrics:
    - type: v_measure
      value: 37.94850105022274
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/CLSClusteringS2S
      name: MTEB CLSClusteringS2S
      config: default
      split: test
      revision: e458b3f5414b62b7f9f83499ac1f5497ae2e869f
    metrics:
    - type: v_measure
      value: 38.11958675421534
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/CMedQAv1-reranking
      name: MTEB CMedQAv1
      config: default
      split: test
      revision: 8d7f1e942507dac42dc58017c1a001c3717da7df
    metrics:
    - type: map
      value: 86.10950950485399
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/CMedQAv2-reranking
      name: MTEB CMedQAv2
      config: default
      split: test
      revision: 23d186750531a14a0357ca22cd92d712fd512ea0
    metrics:
    - type: map
      value: 87.28038294231966
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-android
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: f46a197baaae43b4f621051089b82a364682dfeb
    metrics:
    - type: ndcg_at_10
      value: 47.099000000000004
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-english
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
    metrics:
    - type: ndcg_at_10
      value: 45.973000000000006
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-gaming
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
    metrics:
    - type: ndcg_at_10
      value: 55.606
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-gis
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: 5003b3064772da1887988e05400cf3806fe491f2
    metrics:
    - type: ndcg_at_10
      value: 36.638
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-mathematica
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
    metrics:
    - type: ndcg_at_10
      value: 30.711
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-physics
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
    metrics:
    - type: ndcg_at_10
      value: 44.523
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-programmers
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
    metrics:
    - type: ndcg_at_10
      value: 37.940000000000005
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
    metrics:
    - type: ndcg_at_10
      value: 38.12183333333333
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-stats
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
    metrics:
    - type: ndcg_at_10
      value: 32.684000000000005
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-tex
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: 46989137a86843e03a6195de44b09deda022eec7
    metrics:
    - type: ndcg_at_10
      value: 26.735
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-unix
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
    metrics:
    - type: ndcg_at_10
      value: 36.933
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-webmasters
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
    metrics:
    - type: ndcg_at_10
      value: 33.747
  - task:
      type: Retrieval
    dataset:
      type: mteb/cqadupstack-wordpress
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
    metrics:
    - type: ndcg_at_10
      value: 28.872999999999998
  - task:
      type: Retrieval
    dataset:
      type: mteb/climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
    metrics:
    - type: ndcg_at_10
      value: 34.833
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CmedqaRetrieval
      name: MTEB CmedqaRetrieval
      config: default
      split: dev
      revision: cd540c506dae1cf9e9a59c3e06f42030d54e7301
    metrics:
    - type: ndcg_at_10
      value: 43.78
  - task:
      type: PairClassification
    dataset:
      type: C-MTEB/CMNLI
      name: MTEB Cmnli
      config: default
      split: validation
      revision: 41bc36f332156f7adc9e38f53777c959b2ae9766
    metrics:
    - type: cos_sim_ap
      value: 84.00640599186677
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CovidRetrieval
      name: MTEB CovidRetrieval
      config: default
      split: dev
      revision: 1271c7809071a13532e05f25fb53511ffce77117
    metrics:
    - type: ndcg_at_10
      value: 80.60000000000001
  - task:
      type: Retrieval
    dataset:
      type: mteb/dbpedia
      name: MTEB DBPedia
      config: default
      split: test
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
    metrics:
    - type: ndcg_at_10
      value: 40.116
  - task:
      type: Retrieval
    dataset:
      type: clarin-knext/dbpedia-pl
      name: MTEB DBPedia-PL
      config: default
      split: test
      revision: 76afe41d9af165cc40999fcaa92312b8b012064a
    metrics:
    - type: ndcg_at_10
      value: 32.498
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/DuRetrieval
      name: MTEB DuRetrieval
      config: default
      split: dev
      revision: a1a333e290fe30b10f3f56498e3a0d911a693ced
    metrics:
    - type: ndcg_at_10
      value: 87.547
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/EcomRetrieval
      name: MTEB EcomRetrieval
      config: default
      split: dev
      revision: 687de13dc7294d6fd9be10c6945f9e8fec8166b9
    metrics:
    - type: ndcg_at_10
      value: 64.85
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
      value: 47.949999999999996
  - task:
      type: Retrieval
    dataset:
      type: mteb/fever
      name: MTEB FEVER
      config: default
      split: test
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
    metrics:
    - type: ndcg_at_10
      value: 92.111
  - task:
      type: Retrieval
    dataset:
      type: clarin-knext/fiqa-pl
      name: MTEB FiQA-PL
      config: default
      split: test
      revision: 2e535829717f8bf9dc829b7f911cc5bbd4e6608e
    metrics:
    - type: ndcg_at_10
      value: 28.962
  - task:
      type: Retrieval
    dataset:
      type: mteb/fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
    metrics:
    - type: ndcg_at_10
      value: 45.005
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
      value: 25.133776435657595
  - task:
      type: Retrieval
    dataset:
      type: mteb/hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
    metrics:
    - type: ndcg_at_10
      value: 63.036
  - task:
      type: Retrieval
    dataset:
      type: clarin-knext/hotpotqa-pl
      name: MTEB HotpotQA-PL
      config: default
      split: test
      revision: a0bd479ac97b4ccb5bd6ce320c415d0bb4beb907
    metrics:
    - type: ndcg_at_10
      value: 56.904999999999994
  - task:
      type: Classification
    dataset:
      type: C-MTEB/IFlyTek-classification
      name: MTEB IFlyTek
      config: default
      split: validation
      revision: 421605374b29664c5fc098418fe20ada9bd55f8a
    metrics:
    - type: accuracy
      value: 44.59407464409388
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
      value: 74.912
  - task:
      type: Classification
    dataset:
      type: C-MTEB/JDReview-classification
      name: MTEB JDReview
      config: default
      split: test
      revision: b7c64bd89eb87f8ded463478346f76731f07bf8b
    metrics:
    - type: accuracy
      value: 79.26829268292683
  - task:
      type: STS
    dataset:
      type: C-MTEB/LCQMC
      name: MTEB LCQMC
      config: default
      split: test
      revision: 17f9b096f80380fce5ed12a9be8be7784b337daf
    metrics:
    - type: cos_sim_spearman
      value: 74.8601229809791
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
      value: 42.331902754246556
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
      value: 40.92029335502153
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/Mmarco-reranking
      name: MTEB MMarcoReranking
      config: default
      split: dev
      revision: 8e0c766dbe9e16e1d221116a3f36795fbade07f6
    metrics:
    - type: map
      value: 32.19266316591337
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MMarcoRetrieval
      name: MTEB MMarcoRetrieval
      config: default
      split: dev
      revision: 539bbde593d947e2a124ba72651aafc09eb33fc2
    metrics:
    - type: ndcg_at_10
      value: 79.346
  - task:
      type: Retrieval
    dataset:
      type: mteb/msmarco
      name: MTEB MSMARCO
      config: default
      split: dev
      revision: c5a29a104738b98a9e76336939199e264163d4a0
    metrics:
    - type: ndcg_at_10
      value: 39.922999999999995
  - task:
      type: Retrieval
    dataset:
      type: clarin-knext/msmarco-pl
      name: MTEB MSMARCO-PL
      config: default
      split: test
      revision: 8634c07806d5cce3a6138e260e59b81760a0a640
    metrics:
    - type: ndcg_at_10
      value: 55.620999999999995
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
      value: 92.53989968080255
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
      value: 88.26993519301212
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
      value: 90.87725150100067
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
      value: 87.48512370811149
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
      value: 89.45141627823591
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
      value: 83.45750452079565
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
      value: 72.57637938896488
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
      value: 63.50803043110736
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
      value: 71.6577718478986
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
      value: 64.05887879736925
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
      value: 65.27070634636071
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
      value: 63.04520795660037
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
      value: 80.66350710900474
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
      value: 44.016506455899425
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
      value: 40.67730129573544
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
      value: 57.94552790854068
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
      value: 49.273705447209146
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
      value: 55.490921318090116
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
      value: 60.97511768661733
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
      value: 57.5689307330195
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
      value: 48.34902488231337
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
      value: 63.6684599865501
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
      value: 62.54539340954942
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
      value: 63.08675184936112
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
      value: 72.12508406186953
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
      value: 67.41425689307331
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
      value: 65.59515803631474
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
      value: 62.90517821116342
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
      value: 67.91526563550774
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
      value: 55.198386012104905
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
      value: 65.04371217215869
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
      value: 63.31203765971756
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
      value: 55.521183591123055
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
      value: 66.06254203093476
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
      value: 56.01546738399461
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
      value: 67.27975790181574
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
      value: 66.79556153328849
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
      value: 50.18493611297915
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
      value: 47.888365837256224
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
      value: 50.79690652320108
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
      value: 57.225958305312716
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
      value: 64.58641560188299
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
      value: 59.08204438466711
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
      value: 59.54606590450572
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
      value: 53.443174176193665
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
      value: 61.65097511768661
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
      value: 53.45662407531944
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
      value: 63.739071956960316
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
      value: 66.36180228648286
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
      value: 66.3920645595158
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
      value: 68.06993947545395
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
      value: 63.123739071956955
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
      value: 67.46133154001346
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
      value: 60.54472091459314
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
      value: 58.204438466711494
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
      value: 65.69603227975792
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
      value: 51.684599865501
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
      value: 58.523873570948226
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
      value: 58.53396099529253
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
      value: 61.88298587760591
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
      value: 56.65097511768662
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
      value: 64.8453261600538
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
      value: 58.6247478143914
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
      value: 64.16274377942166
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
      value: 69.61667787491594
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
      value: 64.17283120376598
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
      value: 64.89912575655683
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
      value: 57.27975790181573
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
      value: 62.269670477471415
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
      value: 65.10423671822461
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
      value: 62.40753194351043
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
      value: 55.369872225958304
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
      value: 71.60726294552792
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
      value: 70.30262273032952
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
      value: 69.52925353059851
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
      value: 76.28446536650976
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
      value: 72.45460659045058
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
      value: 70.26563550773368
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
      value: 67.20578345662408
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
      value: 72.64963012777405
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
      value: 61.698049764626774
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
      value: 70.14458641560188
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
      value: 70.51445864156018
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
      value: 60.13786146603901
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
      value: 70.61533288500337
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
      value: 61.526563550773375
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
      value: 71.99731002017484
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
      value: 71.59381304640216
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
      value: 57.010759919300604
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
      value: 53.26160053799597
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
      value: 57.800941492938804
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
      value: 62.387357094821795
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
      value: 69.5359784801614
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
      value: 63.36919973100203
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
      value: 64.81506388702084
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
      value: 59.35104236718225
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
      value: 66.67787491593813
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
      value: 59.4250168123739
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
      value: 71.49630127774043
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
      value: 71.95696032279758
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
      value: 70.11768661735036
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
      value: 71.86953597848016
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
      value: 68.51042367182247
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
      value: 71.65097511768661
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
      value: 66.81573638197713
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
      value: 65.26227303295225
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
      value: 72.51513113651646
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
      value: 58.29858776059179
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
      value: 62.72696704774714
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
      value: 66.57700067249496
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
      value: 68.22797579018157
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
      value: 61.97041022192333
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
      value: 70.72629455279085
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
      value: 63.16072629455278
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
      value: 67.92199058507062
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
      value: 74.40484196368527
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
      value: 71.61398789509079
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MedicalRetrieval
      name: MTEB MedicalRetrieval
      config: default
      split: dev
      revision: 2039188fb5800a9803ba5048df7b76e6fb151fc6
    metrics:
    - type: ndcg_at_10
      value: 61.934999999999995
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
      value: 33.052031054565205
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
      value: 31.969909524076794
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
      value: 31.7530992892652
  - task:
      type: Retrieval
    dataset:
      type: jinaai/mintakaqa
      name: MTEB MintakaRetrieval (fr)
      config: fr
      split: test
      revision: efa78cc2f74bbcd21eff2261f9e13aebe40b814e
    metrics:
    - type: ndcg_at_10
      value: 34.705999999999996
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (ar)
      config: ar
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 55.166000000000004
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (de)
      config: de
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 55.155
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (en)
      config: en
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 50.993
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (es)
      config: es
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 81.228
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (fr)
      config: fr
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 76.19
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (hi)
      config: hi
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 45.206
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (it)
      config: it
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 66.741
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (ja)
      config: ja
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 52.111
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (ko)
      config: ko
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 46.733000000000004
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (pt)
      config: pt
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 79.105
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (ru)
      config: ru
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 64.21
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (th)
      config: th
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 35.467
  - task:
      type: Retrieval
    dataset:
      type: Shitao/MLDR
      name: MTEB MultiLongDocRetrieval (zh)
      config: zh
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 27.419
  - task:
      type: Classification
    dataset:
      type: C-MTEB/MultilingualSentiment-classification
      name: MTEB MultilingualSentiment
      config: default
      split: validation
      revision: 46958b007a63fdbf239b7672c25d0bea67b5ea1a
    metrics:
    - type: accuracy
      value: 61.02000000000001
  - task:
      type: Retrieval
    dataset:
      type: mteb/nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
    metrics:
    - type: ndcg_at_10
      value: 36.65
  - task:
      type: Retrieval
    dataset:
      type: clarin-knext/nfcorpus-pl
      name: MTEB NFCorpus-PL
      config: default
      split: test
      revision: 9a6f9567fda928260afed2de480d79c98bf0bec0
    metrics:
    - type: ndcg_at_10
      value: 26.831
  - task:
      type: Retrieval
    dataset:
      type: mteb/nq
      name: MTEB NQ
      config: default
      split: test
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
    metrics:
    - type: ndcg_at_10
      value: 58.111000000000004
  - task:
      type: Retrieval
    dataset:
      type: clarin-knext/nq-pl
      name: MTEB NQ-PL
      config: default
      split: test
      revision: f171245712cf85dd4700b06bef18001578d0ca8d
    metrics:
    - type: ndcg_at_10
      value: 43.126999999999995
  - task:
      type: PairClassification
    dataset:
      type: C-MTEB/OCNLI
      name: MTEB Ocnli
      config: default
      split: validation
      revision: 66e76a618a34d6d565d5538088562851e6daa7ec
    metrics:
    - type: cos_sim_ap
      value: 72.67630697316041
  - task:
      type: Classification
    dataset:
      type: C-MTEB/OnlineShopping-classification
      name: MTEB OnlineShopping
      config: default
      split: test
      revision: e610f2ebd179a8fda30ae534c3878750a96db120
    metrics:
    - type: accuracy
      value: 84.85000000000001
  - task:
      type: PairClassification
    dataset:
      type: GEM/opusparcus
      name: MTEB OpusparcusPC (fr)
      config: fr
      split: test
      revision: 9e9b1f8ef51616073f47f306f7f47dd91663f86a
    metrics:
    - type: cos_sim_ap
      value: 100
  - task:
      type: Classification
    dataset:
      type: laugustyniak/abusive-clauses-pl
      name: MTEB PAC
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 65.99189110918043
  - task:
      type: STS
    dataset:
      type: C-MTEB/PAWSX
      name: MTEB PAWSX
      config: default
      split: test
      revision: 9c6a90e430ac22b5779fb019a23e820b11a8b5e1
    metrics:
    - type: cos_sim_spearman
      value: 16.124364530596228
  - task:
      type: PairClassification
    dataset:
      type: PL-MTEB/ppc-pairclassification
      name: MTEB PPC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_ap
      value: 92.43431057460192
  - task:
      type: PairClassification
    dataset:
      type: PL-MTEB/psc-pairclassification
      name: MTEB PSC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_ap
      value: 99.06090138049724
  - task:
      type: PairClassification
    dataset:
      type: paws-x
      name: MTEB PawsX (fr)
      config: fr
      split: test
      revision: 8a04d940a42cd40658986fdd8e3da561533a3646
    metrics:
    - type: cos_sim_ap
      value: 58.9314954874314
  - task:
      type: Classification
    dataset:
      type: PL-MTEB/polemo2_in
      name: MTEB PolEmo2.0-IN
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 69.59833795013851
  - task:
      type: Classification
    dataset:
      type: PL-MTEB/polemo2_out
      name: MTEB PolEmo2.0-OUT
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 44.73684210526315
  - task:
      type: STS
    dataset:
      type: C-MTEB/QBQTC
      name: MTEB QBQTC
      config: default
      split: test
      revision: 790b0510dc52b1553e8c49f3d2afb48c0e5c48b7
    metrics:
    - type: cos_sim_spearman
      value: 39.36450754137984
  - task:
      type: Retrieval
    dataset:
      type: clarin-knext/quora-pl
      name: MTEB Quora-PL
      config: default
      split: test
      revision: 0be27e93455051e531182b85e85e425aba12e9d4
    metrics:
    - type: ndcg_at_10
      value: 80.76299999999999
  - task:
      type: Retrieval
    dataset:
      type: mteb/quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 88.022
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
      value: 55.719165988934385
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
      value: 62.25390069273025
  - task:
      type: Retrieval
    dataset:
      type: mteb/scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 18.243000000000002
  - task:
      type: Retrieval
    dataset:
      type: clarin-knext/scidocs-pl
      name: MTEB SCIDOCS-PL
      config: default
      split: test
      revision: 45452b03f05560207ef19149545f168e596c9337
    metrics:
    - type: ndcg_at_10
      value: 14.219000000000001
  - task:
      type: PairClassification
    dataset:
      type: PL-MTEB/sicke-pl-pairclassification
      name: MTEB SICK-E-PL
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_ap
      value: 75.4022630307816
  - task:
      type: STS
    dataset:
      type: mteb/sickr-sts
      name: MTEB SICK-R
      config: default
      split: test
      revision: a6ea5a8cab320b040a23452cc28066d9beae2cee
    metrics:
    - type: cos_sim_spearman
      value: 79.34269390198548
  - task:
      type: STS
    dataset:
      type: PL-MTEB/sickr-pl-sts
      name: MTEB SICK-R-PL
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_spearman
      value: 74.0651660446132
  - task:
      type: STS
    dataset:
      type: Lajavaness/SICK-fr
      name: MTEB SICKFr
      config: default
      split: test
      revision: e077ab4cf4774a1e36d86d593b150422fafd8e8a
    metrics:
    - type: cos_sim_spearman
      value: 78.62693119733123
  - task:
      type: STS
    dataset:
      type: mteb/sts12-sts
      name: MTEB STS12
      config: default
      split: test
      revision: a0d554a64d88156834ff5ae9920b964011b16384
    metrics:
    - type: cos_sim_spearman
      value: 77.50660544631359
  - task:
      type: STS
    dataset:
      type: mteb/sts13-sts
      name: MTEB STS13
      config: default
      split: test
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
    metrics:
    - type: cos_sim_spearman
      value: 85.55415077723738
  - task:
      type: STS
    dataset:
      type: mteb/sts14-sts
      name: MTEB STS14
      config: default
      split: test
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
    metrics:
    - type: cos_sim_spearman
      value: 81.67550814479077
  - task:
      type: STS
    dataset:
      type: mteb/sts15-sts
      name: MTEB STS15
      config: default
      split: test
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
    metrics:
    - type: cos_sim_spearman
      value: 88.94601412322764
  - task:
      type: STS
    dataset:
      type: mteb/sts16-sts
      name: MTEB STS16
      config: default
      split: test
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
    metrics:
    - type: cos_sim_spearman
      value: 84.33844259337481
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (ko-ko)
      config: ko-ko
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_spearman
      value: 81.58650681159105
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (ar-ar)
      config: ar-ar
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_spearman
      value: 78.82472265884256
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-ar)
      config: en-ar
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_spearman
      value: 76.43637938260397
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-de)
      config: en-de
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_spearman
      value: 84.71008299464059
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-en)
      config: en-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_spearman
      value: 88.88074713413747
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-tr)
      config: en-tr
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_spearman
      value: 76.36405640457285
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (es-en)
      config: es-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_spearman
      value: 83.84737910084762
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (es-es)
      config: es-es
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_spearman
      value: 87.03931621433031
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (fr-en)
      config: fr-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_spearman
      value: 84.43335591752246
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (it-en)
      config: it-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_spearman
      value: 83.85268648747021
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (nl-en)
      config: nl-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_spearman
      value: 82.45786516224341
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (en)
      config: en
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 67.20227303970304
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de)
      config: de
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 60.892838305537126
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (es)
      config: es
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 72.01876318464508
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (pl)
      config: pl
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 42.3879320510127
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (tr)
      config: tr
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 65.54048784845729
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (ar)
      config: ar
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 58.55244068334867
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (ru)
      config: ru
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 66.48710288440624
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (zh)
      config: zh
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 66.585754901838
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (fr)
      config: fr
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 81.03001290557805
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de-en)
      config: de-en
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 62.28001859884359
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (es-en)
      config: es-en
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 79.64106342105019
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (it)
      config: it
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 78.27915339361124
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (pl-en)
      config: pl-en
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 78.28574268257462
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (zh-en)
      config: zh-en
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 72.92658860751482
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (es-it)
      config: es-it
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 74.83418886368217
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de-fr)
      config: de-fr
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 56.01064022625769
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de-pl)
      config: de-pl
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 53.64332829635126
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (fr-pl)
      config: fr-pl
      split: test
      revision: eea2b4fe26a775864c896887d910b76a8098ad3f
    metrics:
    - type: cos_sim_spearman
      value: 73.24670207647144
  - task:
      type: STS
    dataset:
      type: C-MTEB/STSB
      name: MTEB STSB
      config: default
      split: test
      revision: 0cde68302b3541bb8b3c340dc0644b0b745b3dc0
    metrics:
    - type: cos_sim_spearman
      value: 80.7157790971544
  - task:
      type: STS
    dataset:
      type: mteb/stsbenchmark-sts
      name: MTEB STSBenchmark
      config: default
      split: test
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
    metrics:
    - type: cos_sim_spearman
      value: 86.45763616928973
  - task:
      type: STS
    dataset:
      type: stsb_multi_mt
      name: MTEB STSBenchmarkMultilingualSTS (fr)
      config: fr
      split: test
      revision: 93d57ef91790589e3ce9c365164337a8a78b7632
    metrics:
    - type: cos_sim_spearman
      value: 84.4335500335282
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
      value: 84.15276484499303
  - task:
      type: Retrieval
    dataset:
      type: mteb/scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
    metrics:
    - type: ndcg_at_10
      value: 73.433
  - task:
      type: Retrieval
    dataset:
      type: clarin-knext/scifact-pl
      name: MTEB SciFact-PL
      config: default
      split: test
      revision: 47932a35f045ef8ed01ba82bf9ff67f6e109207e
    metrics:
    - type: ndcg_at_10
      value: 58.919999999999995
  - task:
      type: PairClassification
    dataset:
      type: mteb/sprintduplicatequestions-pairclassification
      name: MTEB SprintDuplicateQuestions
      config: default
      split: test
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
    metrics:
    - type: cos_sim_ap
      value: 95.40564890916419
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
      value: 63.41856697730145
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
      value: 31.709285904909112
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
      value: 52.09341030060322
  - task:
      type: Summarization
    dataset:
      type: mteb/summeval
      name: MTEB SummEval
      config: default
      split: test
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
    metrics:
    - type: cos_sim_spearman
      value: 30.58262517835034
  - task:
      type: Summarization
    dataset:
      type: lyon-nlp/summarization-summeval-fr-p2p
      name: MTEB SummEvalFr
      config: default
      split: test
      revision: b385812de6a9577b6f4d0f88c6a6e35395a94054
    metrics:
    - type: cos_sim_spearman
      value: 29.744542072951358
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
      value: 88.03333333333333
  - task:
      type: Retrieval
    dataset:
      type: lyon-nlp/mteb-fr-retrieval-syntec-s2p
      name: MTEB SyntecRetrieval
      config: default
      split: test
      revision: 77f7e271bf4a92b24fce5119f3486b583ca016ff
    metrics:
    - type: ndcg_at_10
      value: 83.043
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/T2Reranking
      name: MTEB T2Reranking
      config: default
      split: dev
      revision: 76631901a18387f85eaa53e5450019b87ad58ef9
    metrics:
    - type: map
      value: 67.08577894804324
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/T2Retrieval
      name: MTEB T2Retrieval
      config: default
      split: dev
      revision: 8731a845f1bf500a4f111cf1070785c793d10e64
    metrics:
    - type: ndcg_at_10
      value: 84.718
  - task:
      type: Classification
    dataset:
      type: C-MTEB/TNews-classification
      name: MTEB TNews
      config: default
      split: validation
      revision: 317f262bf1e6126357bbe89e875451e4b0938fe4
    metrics:
    - type: accuracy
      value: 48.726
  - task:
      type: Retrieval
    dataset:
      type: mteb/trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 57.56
  - task:
      type: Retrieval
    dataset:
      type: clarin-knext/trec-covid-pl
      name: MTEB TRECCOVID-PL
      config: default
      split: test
      revision: 81bcb408f33366c2a20ac54adafad1ae7e877fdd
    metrics:
    - type: ndcg_at_10
      value: 59.355999999999995
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (sqi-eng)
      config: sqi-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 82.765
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (fry-eng)
      config: fry-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 73.69942196531792
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kur-eng)
      config: kur-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 32.86585365853657
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tur-eng)
      config: tur-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 95.81666666666666
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (deu-eng)
      config: deu-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 97.75
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nld-eng)
      config: nld-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 93.78333333333335
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ron-eng)
      config: ron-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 90.72333333333333
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ang-eng)
      config: ang-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 42.45202558635395
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ido-eng)
      config: ido-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 77.59238095238095
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (jav-eng)
      config: jav-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 35.69686411149825
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (isl-eng)
      config: isl-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 82.59333333333333
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (slv-eng)
      config: slv-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 84.1456922987907
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cym-eng)
      config: cym-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 52.47462133594857
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kaz-eng)
      config: kaz-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 67.62965440356746
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (est-eng)
      config: est-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 79.48412698412699
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (heb-eng)
      config: heb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 75.85
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (gla-eng)
      config: gla-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 27.32600866497127
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mar-eng)
      config: mar-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 84.38
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (lat-eng)
      config: lat-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 42.98888712165028
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (bel-eng)
      config: bel-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 85.55690476190476
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (pms-eng)
      config: pms-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 46.68466031323174
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (gle-eng)
      config: gle-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 32.73071428571428
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (pes-eng)
      config: pes-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 88.26333333333334
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nob-eng)
      config: nob-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 96.61666666666666
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (bul-eng)
      config: bul-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 91.30666666666666
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cbk-eng)
      config: cbk-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 70.03714285714285
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hun-eng)
      config: hun-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 89.09
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (uig-eng)
      config: uig-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 59.570476190476185
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (rus-eng)
      config: rus-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 92.9
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (spa-eng)
      config: spa-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 97.68333333333334
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hye-eng)
      config: hye-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 80.40880503144653
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tel-eng)
      config: tel-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 89.7008547008547
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (afr-eng)
      config: afr-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 81.84833333333333
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mon-eng)
      config: mon-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 71.69696969696969
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (arz-eng)
      config: arz-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 55.76985790822269
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hrv-eng)
      config: hrv-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 91.66666666666666
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nov-eng)
      config: nov-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 68.36668519547896
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (gsw-eng)
      config: gsw-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 36.73992673992674
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nds-eng)
      config: nds-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 63.420952380952365
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ukr-eng)
      config: ukr-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 91.28999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (uzb-eng)
      config: uzb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 40.95392490046146
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (lit-eng)
      config: lit-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 77.58936507936508
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ina-eng)
      config: ina-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 91.28999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (lfn-eng)
      config: lfn-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 63.563650793650794
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (zsm-eng)
      config: zsm-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 94.35
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ita-eng)
      config: ita-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 91.43
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cmn-eng)
      config: cmn-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 95.73333333333332
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (lvs-eng)
      config: lvs-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 79.38666666666667
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (glg-eng)
      config: glg-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 89.64
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ceb-eng)
      config: ceb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 21.257184628237262
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (bre-eng)
      config: bre-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 13.592316017316017
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ben-eng)
      config: ben-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 73.22666666666666
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (swg-eng)
      config: swg-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 51.711309523809526
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (arq-eng)
      config: arq-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 24.98790634904795
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kab-eng)
      config: kab-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 17.19218192918193
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (fra-eng)
      config: fra-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 93.26666666666667
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (por-eng)
      config: por-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 94.57333333333334
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tat-eng)
      config: tat-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 42.35127206127206
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (oci-eng)
      config: oci-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 51.12318903318903
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (pol-eng)
      config: pol-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 94.89999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (war-eng)
      config: war-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 23.856320290390055
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (aze-eng)
      config: aze-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 79.52833333333334
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (vie-eng)
      config: vie-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 95.93333333333334
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nno-eng)
      config: nno-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 90.75333333333333
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cha-eng)
      config: cha-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 30.802919708029197
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mhr-eng)
      config: mhr-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 15.984076294076294
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (dan-eng)
      config: dan-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 91.82666666666667
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ell-eng)
      config: ell-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 91.9
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (amh-eng)
      config: amh-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 76.36054421768706
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (pam-eng)
      config: pam-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 9.232711399711398
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hsb-eng)
      config: hsb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 45.640803181175855
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (srp-eng)
      config: srp-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 86.29
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (epo-eng)
      config: epo-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 88.90833333333332
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kzj-eng)
      config: kzj-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 11.11880248978075
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (awa-eng)
      config: awa-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 48.45839345839346
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (fao-eng)
      config: fao-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 65.68157033805888
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mal-eng)
      config: mal-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 94.63852498786997
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ile-eng)
      config: ile-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 81.67904761904761
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (bos-eng)
      config: bos-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 89.35969868173258
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cor-eng)
      config: cor-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 5.957229437229437
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cat-eng)
      config: cat-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 91.50333333333333
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (eus-eng)
      config: eus-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 63.75498778998778
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (yue-eng)
      config: yue-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 82.99190476190476
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (swe-eng)
      config: swe-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 92.95
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (dtp-eng)
      config: dtp-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 9.054042624042623
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kat-eng)
      config: kat-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 72.77064981488574
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (jpn-eng)
      config: jpn-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 93.14
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (csb-eng)
      config: csb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 29.976786498525627
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (xho-eng)
      config: xho-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 67.6525821596244
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (orv-eng)
      config: orv-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 33.12964812964813
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ind-eng)
      config: ind-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 92.30666666666666
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tuk-eng)
      config: tuk-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 34.36077879427633
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (max-eng)
      config: max-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 52.571845212690285
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (swh-eng)
      config: swh-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 58.13107263107262
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hin-eng)
      config: hin-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 93.33333333333333
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (dsb-eng)
      config: dsb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 42.87370133925458
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ber-eng)
      config: ber-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 20.394327616827614
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tam-eng)
      config: tam-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 84.29967426710098
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (slk-eng)
      config: slk-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 88.80666666666667
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tgl-eng)
      config: tgl-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 67.23062271062273
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ast-eng)
      config: ast-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 78.08398950131233
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mkd-eng)
      config: mkd-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 77.85166666666666
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (khm-eng)
      config: khm-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 67.63004001231148
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ces-eng)
      config: ces-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 89.77000000000001
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tzl-eng)
      config: tzl-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 40.2654503616042
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (urd-eng)
      config: urd-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 83.90333333333334
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ara-eng)
      config: ara-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 77.80666666666666
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kor-eng)
      config: kor-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 84.08
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (yid-eng)
      config: yid-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 60.43098607367475
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (fin-eng)
      config: fin-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 88.19333333333333
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tha-eng)
      config: tha-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 90.55352798053529
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (wuu-eng)
      config: wuu-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: f1
      value: 88.44999999999999
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/ThuNewsClusteringP2P
      name: MTEB ThuNewsClusteringP2P
      config: default
      split: test
      revision: 5798586b105c0434e4f0fe5e767abe619442cf93
    metrics:
    - type: v_measure
      value: 57.25416429643288
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/ThuNewsClusteringS2S
      name: MTEB ThuNewsClusteringS2S
      config: default
      split: test
      revision: 8a8b2caeda43f39e13c4bc5bea0f8a667896e10d
    metrics:
    - type: v_measure
      value: 56.616646560243524
  - task:
      type: Retrieval
    dataset:
      type: mteb/touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
    metrics:
    - type: ndcg_at_10
      value: 22.819
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
      value: 71.02579999999999
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
      value: 57.60045274476514
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
      value: 50.346666699466205
  - task:
      type: PairClassification
    dataset:
      type: mteb/twittersemeval2015-pairclassification
      name: MTEB TwitterSemEval2015
      config: default
      split: test
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
    metrics:
    - type: cos_sim_ap
      value: 71.88199004440489
  - task:
      type: PairClassification
    dataset:
      type: mteb/twitterurlcorpus-pairclassification
      name: MTEB TwitterURLCorpus
      config: default
      split: test
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
    metrics:
    - type: cos_sim_ap
      value: 85.41587779677383
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/VideoRetrieval
      name: MTEB VideoRetrieval
      config: default
      split: dev
      revision: 58c2597a5943a2ba48f4668c3b90d796283c5639
    metrics:
    - type: ndcg_at_10
      value: 72.792
  - task:
      type: Classification
    dataset:
      type: C-MTEB/waimai-classification
      name: MTEB Waimai
      config: default
      split: test
      revision: 339287def212450dcaa9df8c22bf93e9980c7023
    metrics:
    - type: accuracy
      value: 82.58000000000001
  - task:
      type: Retrieval
    dataset:
      type: jinaai/xpqa
      name: MTEB XPQARetrieval (fr)
      config: fr
      split: test
      revision: c99d599f0a6ab9b85b065da6f9d94f9cf731679f
    metrics:
    - type: ndcg_at_10
      value: 67.327
---

## gte-multilingual-base

The **gte-multilingual-base** model is the latest in the [GTE](https://huggingface.co/collections/Alibaba-NLP/gte-models-6680f0b13f885cb431e6d469) (General Text Embedding) family of models, featuring several key attributes:

- **High Performance**: Achieves state-of-the-art (SOTA) results in multilingual retrieval tasks and multi-task representation model evaluations when compared to models of similar size.
- **Training Architecture**: Trained using an encoder-only transformers architecture, resulting in a smaller model size. Unlike previous models based on decode-only LLM architecture (e.g., gte-qwen2-1.5b-instruct), this model has lower hardware requirements for inference, offering a 10x increase in inference speed.
- **Long Context**: Supports text lengths up to **8192** tokens.
- **Multilingual Capability**: Supports over **70** languages.
- **Elastic Dense Embedding**: Support elastic output dense representation while maintaining the effectiveness of downstream tasks, which significantly reduces storage costs and improves execution efficiency.
- **Sparse Vectors**: In addition to dense representations, it can also generate sparse vectors.


**Paper**: [mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual Text Retrieval](https://arxiv.org/pdf/2407.19669)

## Model Information
- Model Size: 305M
- Embedding Dimension: 768
- Max Input Tokens: 8192


## Usage 

- **It is recommended to install xformers and enable unpadding for acceleration,
refer to [enable-unpadding-and-xformers](https://huggingface.co/Alibaba-NLP/new-impl#recommendation-enable-unpadding-and-acceleration-with-xformers).**
- **How to use it offline: [new-impl/discussions/2](https://huggingface.co/Alibaba-NLP/new-impl/discussions/2#662b08d04d8c3d0a09c88fa3)**
- **How to use with [TEI](https://github.com/huggingface/text-embeddings-inference): [refs/pr/7](https://huggingface.co/Alibaba-NLP/gte-multilingual-base/discussions/7#66bfb82ea03b764ca92a2221)**



### Get Dense Embeddings with Transformers
```python
# Requires transformers>=4.36.0

import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer

input_texts = [
    "what is the capital of China?",
    "how to implement quick sort in python?",
    "北京",
    "快排算法介绍"
]

model_name_or_path = 'Alibaba-NLP/gte-multilingual-base'
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModel.from_pretrained(model_name_or_path, trust_remote_code=True)

# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=8192, padding=True, truncation=True, return_tensors='pt')

outputs = model(**batch_dict)

dimension=768 # The output dimension of the output embedding, should be in [128, 768]
embeddings = outputs.last_hidden_state[:, 0][:dimension]

embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:1] @ embeddings[1:].T) * 100
print(scores.tolist())

# [[0.3016996383666992, 0.7503870129585266, 0.3203084468841553]]
```

### Use with sentence-transformers
```python
# Requires sentences-transformers>=3.0.0

from sentence_transformers import SentenceTransformer

input_texts = [
    "what is the capital of China?",
    "how to implement quick sort in python?",
    "北京",
    "快排算法介绍"
]

model_name_or_path="Alibaba-NLP/gte-multilingual-base"
model = SentenceTransformer(model_name_or_path, trust_remote_code=True)
embeddings = model.encode(input_texts, normalize_embeddings=True) # embeddings.shape (4, 768)

# sim scores
scores = model.similarity(embeddings[:1], embeddings[1:])

print(scores.tolist())
# [[0.301699697971344, 0.7503870129585266, 0.32030850648880005]]
```

### Use with custom code to get dense embeddigns and sparse token weights
```python
# You can find the script gte_embedding.py in https://huggingface.co/Alibaba-NLP/gte-multilingual-base/blob/main/scripts/gte_embedding.py

from gte_embedding import GTEEmbeddidng

model_name_or_path = 'Alibaba-NLP/gte-multilingual-base'
model = GTEEmbeddidng(model_name_or_path)
query = "中国的首都在哪儿"

docs = [
    "what is the capital of China?",
    "how to implement quick sort in python?",
    "北京",
    "快排算法介绍"
]

embs = model.encode(docs, return_dense=True,return_sparse=True)
print('dense_embeddings vecs', embs['dense_embeddings'])
print('token_weights', embs['token_weights'])
pairs = [(query, doc) for doc in docs]
dense_scores = model.compute_scores(pairs, dense_weight=1.0, sparse_weight=0.0)
sparse_scores = model.compute_scores(pairs, dense_weight=0.0, sparse_weight=1.0)
hybrid_scores = model.compute_scores(pairs, dense_weight=1.0, sparse_weight=0.3)

print('dense_scores', dense_scores)
print('sparse_scores', sparse_scores)
print('hybrid_scores', hybrid_scores)

# dense_scores [0.85302734375, 0.257568359375, 0.76953125, 0.325439453125]
# sparse_scores [0.0, 0.0, 4.600879669189453, 1.570279598236084]
# hybrid_scores [0.85302734375, 0.257568359375, 2.1497951507568356, 0.7965233325958252]

```

## Evaluation

We validated the performance of the **gte-multilingual-base** model on multiple downstream tasks, including multilingual retrieval, cross-lingual retrieval, long text retrieval, and general text representation evaluation on the [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard), among others.

### Retrieval Task

Retrieval results on [MIRACL](https://arxiv.org/abs/2210.09984) and [MLDR](https://arxiv.org/abs/2402.03216) (multilingual), [MKQA](https://arxiv.org/abs/2007.15207) (crosslingual), [BEIR](https://arxiv.org/abs/2104.08663) and [LoCo](https://arxiv.org/abs/2402.07440) (English).

![image](./images/mgte-retrieval.png)

- Detail results on [MLDR](https://arxiv.org/abs/2402.03216)

![image](./images/mgte-retrieval.png)

- Detail results on [LoCo](https://arxiv.org/abs/2402.07440)

### MTEB 

Results on MTEB English, Chinese, French, Polish

![image](./images/mgte-mteb.png)

**More detailed experimental results can be found in the [paper](https://arxiv.org/pdf/2407.19669)**.


## Cloud API Services

In addition to the open-source [GTE](https://huggingface.co/collections/Alibaba-NLP/gte-models-6680f0b13f885cb431e6d469) series models, GTE series models are also available as commercial API services on Alibaba Cloud.

- [Embedding Models](https://help.aliyun.com/zh/model-studio/developer-reference/general-text-embedding/): Rhree versions of the text embedding models are available: text-embedding-v1/v2/v3, with v3 being the latest API service.
- [ReRank Models](https://help.aliyun.com/zh/model-studio/developer-reference/general-text-sorting-model/): The gte-rerank model service is available.

Note that the models behind the commercial APIs are not entirely identical to the open-source models.

## Citation
If you find our paper or models helpful, please consider cite:

```
@misc{zhang2024mgte,
      title={mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual Text Retrieval}, 
      author={Xin Zhang and Yanzhao Zhang and Dingkun Long and Wen Xie and Ziqi Dai and Jialong Tang and Huan Lin and Baosong Yang and Pengjun Xie and Fei Huang and Meishan Zhang and Wenjie Li and Min Zhang},
      year={2024},
      eprint={2407.19669},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2407.19669}, 
}
```