---
tags:
- reinforcement-learning
- atari
- babyai
- metaworld
- mujoco-ant
- mujoco
datasets: jat-project/jat-dataset
pipeline_tag: reinforcement-learning
model-index:
- name: jat-project/jat
  results:
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Atari 57
      type: atari
    metrics:
    - type: iqm_expert_normalized_total_reward
      value: 0.14 [0.14, 0.15]
      name: IQM expert normalized total reward
    - type: iqm_human_normalized_total_reward
      value: 0.38 [0.37, 0.39]
      name: IQM human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: BabyAI
      type: babyai
    metrics:
    - type: iqm_expert_normalized_total_reward
      value: 0.99 [0.99, 0.99]
      name: IQM expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: MetaWorld
      type: metaworld
    metrics:
    - type: iqm_expert_normalized_total_reward
      value: 0.65 [0.64, 0.67]
      name: IQM expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: MuJoCo
      type: mujoco
    metrics:
    - type: iqm_expert_normalized_total_reward
      value: 0.85 [0.83, 0.86]
      name: IQM expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Alien
      type: atari-alien
    metrics:
    - type: total_reward
      value: 1518.70 +/- 568.14
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.08 +/- 0.03
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.19 +/- 0.08
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Amidar
      type: atari-amidar
    metrics:
    - type: total_reward
      value: 89.17 +/- 78.73
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.04 +/- 0.04
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.05 +/- 0.05
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Assault
      type: atari-assault
    metrics:
    - type: total_reward
      value: 1676.91 +/- 780.73
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.09 +/- 0.05
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 2.80 +/- 1.50
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Asterix
      type: atari-asterix
    metrics:
    - type: total_reward
      value: 844.50 +/- 546.85
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.18 +/- 0.16
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.08 +/- 0.07
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Asteroids
      type: atari-asteroids
    metrics:
    - type: total_reward
      value: 1357.90 +/- 453.01
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.00 +/- 0.00
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.01 +/- 0.01
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Atlantis
      type: atari-atlantis
    metrics:
    - type: total_reward
      value: 51843.00 +/- 123857.07
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.13 +/- 0.40
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 2.41 +/- 7.66
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Bank Heist
      type: atari-bankheist
    metrics:
    - type: total_reward
      value: 977.80 +/- 156.49
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.74 +/- 0.12
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 1.30 +/- 0.21
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Battle Zone
      type: atari-battlezone
    metrics:
    - type: total_reward
      value: 16780.00 +/- 6926.15
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.06 +/- 0.02
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.45 +/- 0.19
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Beam Rider
      type: atari-beamrider
    metrics:
    - type: total_reward
      value: 768.36 +/- 364.06
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.01 +/- 0.01
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.02 +/- 0.02
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Berzerk
      type: atari-berzerk
    metrics:
    - type: total_reward
      value: 616.20 +/- 296.08
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.01 +/- 0.01
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.20 +/- 0.12
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Bowling
      type: atari-bowling
    metrics:
    - type: total_reward
      value: 22.32 +/- 5.18
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.00
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: -0.01 +/- 0.04
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Boxing
      type: atari-boxing
    metrics:
    - type: total_reward
      value: 92.31 +/- 18.24
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.94 +/- 0.19
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 7.68 +/- 1.52
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Breakout
      type: atari-breakout
    metrics:
    - type: total_reward
      value: 7.93 +/- 5.66
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.01 +/- 0.01
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.22 +/- 0.20
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Centipede
      type: atari-centipede
    metrics:
    - type: total_reward
      value: 5888.27 +/- 2594.62
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.40 +/- 0.27
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.38 +/- 0.26
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Chopper Command
      type: atari-choppercommand
    metrics:
    - type: total_reward
      value: 2371.00 +/- 1195.43
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.02 +/- 0.01
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.24 +/- 0.18
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Crazy Climber
      type: atari-crazyclimber
    metrics:
    - type: total_reward
      value: 97145.00 +/- 30388.04
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.51 +/- 0.18
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 3.45 +/- 1.21
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Defender
      type: atari-defender
    metrics:
    - type: total_reward
      value: 39317.50 +/- 16246.15
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.10 +/- 0.05
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 2.30 +/- 1.03
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Demon Attack
      type: atari-demonattack
    metrics:
    - type: total_reward
      value: 795.10 +/- 982.55
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.01 +/- 0.01
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.35 +/- 0.54
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Double Dunk
      type: atari-doubledunk
    metrics:
    - type: total_reward
      value: 13.40 +/- 11.07
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.81 +/- 0.28
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.91 +/- 0.32
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Enduro
      type: atari-enduro
    metrics:
    - type: total_reward
      value: 103.11 +/- 28.05
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.04 +/- 0.01
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.12 +/- 0.03
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Fishing Derby
      type: atari-fishingderby
    metrics:
    - type: total_reward
      value: -31.67 +/- 22.54
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.61 +/- 0.23
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.46 +/- 0.17
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Freeway
      type: atari-freeway
    metrics:
    - type: total_reward
      value: 27.57 +/- 1.87
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.81 +/- 0.06
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.93 +/- 0.06
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Frostbite
      type: atari-frostbite
    metrics:
    - type: total_reward
      value: 2875.60 +/- 1679.84
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.21 +/- 0.13
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.66 +/- 0.39
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Gopher
      type: atari-gopher
    metrics:
    - type: total_reward
      value: 5508.80 +/- 2802.03
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.06 +/- 0.03
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 2.44 +/- 1.30
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Gravitar
      type: atari-gravitar
    metrics:
    - type: total_reward
      value: 1330.50 +/- 918.23
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.30 +/- 0.24
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.36 +/- 0.29
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: H.E.R.O.
      type: atari-hero
    metrics:
    - type: total_reward
      value: 11932.00 +/- 3036.87
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.25 +/- 0.07
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.37 +/- 0.10
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Ice Hockey
      type: atari-icehockey
    metrics:
    - type: total_reward
      value: 7.61 +/- 5.28
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.52 +/- 0.15
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 1.55 +/- 0.44
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: James Bond
      type: atari-jamesbond
    metrics:
    - type: total_reward
      value: 425.00 +/- 632.51
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.01 +/- 0.02
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 1.45 +/- 2.31
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Kangaroo
      type: atari-kangaroo
    metrics:
    - type: total_reward
      value: 375.00 +/- 314.13
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.62 +/- 0.60
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.11 +/- 0.11
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Krull
      type: atari-krull
    metrics:
    - type: total_reward
      value: 10743.30 +/- 1311.26
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.93 +/- 0.13
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 8.57 +/- 1.23
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Kung-Fu Master
      type: atari-kungfumaster
    metrics:
    - type: total_reward
      value: 253.00 +/- 233.86
      name: Total reward
    - type: expert_normalized_total_reward
      value: -0.00 +/- 0.01
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: -0.00 +/- 0.01
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Montezuma's Revenge
      type: atari-montezumarevenge
    metrics:
    - type: total_reward
      value: 0.00 +/- 0.00
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.00 +/- 0.00
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.00 +/- 0.00
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Ms. Pacman
      type: atari-mspacman
    metrics:
    - type: total_reward
      value: 1610.10 +/- 504.08
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.20 +/- 0.08
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.20 +/- 0.08
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Name This Game
      type: atari-namethisgame
    metrics:
    - type: total_reward
      value: 7726.40 +/- 2166.18
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.26 +/- 0.10
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.94 +/- 0.38
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Phoenix
      type: atari-phoenix
    metrics:
    - type: total_reward
      value: 1814.20 +/- 1275.29
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.00 +/- 0.00
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.16 +/- 0.20
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: PitFall
      type: atari-pitfall
    metrics:
    - type: total_reward
      value: -4.61 +/- 15.86
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.99 +/- 0.07
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.03 +/- 0.00
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Pong
      type: atari-pong
    metrics:
    - type: total_reward
      value: 16.54 +/- 10.34
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.89 +/- 0.25
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 1.05 +/- 0.29
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Private Eye
      type: atari-privateeye
    metrics:
    - type: total_reward
      value: 44.00 +/- 49.64
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.25 +/- 0.66
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.00 +/- 0.00
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Q*Bert
      type: atari-qbert
    metrics:
    - type: total_reward
      value: 2118.50 +/- 2764.25
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.05 +/- 0.06
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.15 +/- 0.21
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: River Raid
      type: atari-riverraid
    metrics:
    - type: total_reward
      value: 3925.20 +/- 1530.94
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.19 +/- 0.11
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.16 +/- 0.10
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Road Runner
      type: atari-roadrunner
    metrics:
    - type: total_reward
      value: 6929.00 +/- 5577.35
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.09 +/- 0.07
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.88 +/- 0.71
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Robotank
      type: atari-robotank
    metrics:
    - type: total_reward
      value: 10.22 +/- 4.71
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.10 +/- 0.06
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.83 +/- 0.49
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Seaquest
      type: atari-seaquest
    metrics:
    - type: total_reward
      value: 859.80 +/- 407.80
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.31 +/- 0.16
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.02 +/- 0.01
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Skiing
      type: atari-skiing
    metrics:
    - type: total_reward
      value: -15960.04 +/- 5887.52
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.18 +/- 0.93
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.09 +/- 0.46
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Solaris
      type: atari-solaris
    metrics:
    - type: total_reward
      value: 1202.60 +/- 445.27
      name: Total reward
    - type: expert_normalized_total_reward
      value: -0.29 +/- 3.79
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: -0.00 +/- 0.04
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Space Invaders
      type: atari-spaceinvaders
    metrics:
    - type: total_reward
      value: 326.85 +/- 141.89
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.01 +/- 0.00
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.12 +/- 0.09
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Star Gunner
      type: atari-stargunner
    metrics:
    - type: total_reward
      value: 5219.00 +/- 3544.03
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.01 +/- 0.01
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.48 +/- 0.37
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Surround
      type: atari-surround
    metrics:
    - type: total_reward
      value: 1.52 +/- 4.60
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.59 +/- 0.24
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.70 +/- 0.28
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Tennis
      type: atari-tennis
    metrics:
    - type: total_reward
      value: -12.80 +/- 3.70
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.32 +/- 0.11
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.34 +/- 0.12
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Time Pilot
      type: atari-timepilot
    metrics:
    - type: total_reward
      value: 11603.00 +/- 4323.25
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.12 +/- 0.07
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 4.84 +/- 2.60
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Tutankham
      type: atari-tutankham
    metrics:
    - type: total_reward
      value: 108.82 +/- 70.14
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.35 +/- 0.25
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.62 +/- 0.45
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Up and Down
      type: atari-upndown
    metrics:
    - type: total_reward
      value: 19074.60 +/- 9961.77
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.04 +/- 0.02
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 1.66 +/- 0.89
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Venture
      type: atari-venture
    metrics:
    - type: total_reward
      value: 0.00 +/- 0.00
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.00
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.00 +/- 0.00
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Video Pinball
      type: atari-videopinball
    metrics:
    - type: total_reward
      value: 12466.69 +/- 8723.07
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.03 +/- 0.02
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.71 +/- 0.49
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Wizard of Wor
      type: atari-wizardofwor
    metrics:
    - type: total_reward
      value: 2231.00 +/- 2042.92
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.03 +/- 0.04
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.40 +/- 0.49
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Yars Revenge
      type: atari-yarsrevenge
    metrics:
    - type: total_reward
      value: 11190.85 +/- 7342.58
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.03 +/- 0.03
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.16 +/- 0.14
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Zaxxon
      type: atari-zaxxon
    metrics:
    - type: total_reward
      value: 5976.00 +/- 2889.54
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.08 +/- 0.04
      name: Expert normalized total reward
    - type: human_normalized_total_reward
      value: 0.65 +/- 0.32
      name: Human normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Action Obj Door
      type: babyai-action-obj-door
    metrics:
    - type: total_reward
      value: 0.92 +/- 0.22
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.88 +/- 0.36
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Blocked Unlock Pickup
      type: babyai-blocked-unlock-pickup
    metrics:
    - type: total_reward
      value: 0.95 +/- 0.01
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.01
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Boss Level No Unlock
      type: babyai-boss-level-no-unlock
    metrics:
    - type: total_reward
      value: 0.49 +/- 0.43
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.49 +/- 0.49
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Boss Level
      type: babyai-boss-level
    metrics:
    - type: total_reward
      value: 0.54 +/- 0.43
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.54 +/- 0.49
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Find Obj S5
      type: babyai-find-obj-s5
    metrics:
    - type: total_reward
      value: 0.94 +/- 0.04
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.04
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Go To Door
      type: babyai-go-to-door
    metrics:
    - type: total_reward
      value: 0.99 +/- 0.02
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.03
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Go To Imp Unlock
      type: babyai-go-to-imp-unlock
    metrics:
    - type: total_reward
      value: 0.53 +/- 0.41
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.60 +/- 0.55
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Go To Local
      type: babyai-go-to-local
    metrics:
    - type: total_reward
      value: 0.87 +/- 0.16
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.93 +/- 0.22
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Go To Obj Door
      type: babyai-go-to-obj-door
    metrics:
    - type: total_reward
      value: 0.98 +/- 0.04
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.98 +/- 0.08
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Go To Obj
      type: babyai-go-to-obj
    metrics:
    - type: total_reward
      value: 0.94 +/- 0.03
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.01 +/- 0.03
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Go To Red Ball Grey
      type: babyai-go-to-red-ball-grey
    metrics:
    - type: total_reward
      value: 0.92 +/- 0.05
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.06
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Go To Red Ball No Dists
      type: babyai-go-to-red-ball-no-dists
    metrics:
    - type: total_reward
      value: 0.93 +/- 0.03
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.03
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Go To Red Ball
      type: babyai-go-to-red-ball
    metrics:
    - type: total_reward
      value: 0.91 +/- 0.09
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.98 +/- 0.12
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Go To Red Blue Ball
      type: babyai-go-to-red-blue-ball
    metrics:
    - type: total_reward
      value: 0.91 +/- 0.08
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.99 +/- 0.10
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Go To Seq
      type: babyai-go-to-seq
    metrics:
    - type: total_reward
      value: 0.73 +/- 0.33
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.76 +/- 0.38
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Go To
      type: babyai-go-to
    metrics:
    - type: total_reward
      value: 0.78 +/- 0.28
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.82 +/- 0.35
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Key Corridor
      type: babyai-key-corridor
    metrics:
    - type: total_reward
      value: 0.87 +/- 0.13
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.96 +/- 0.14
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Mini Boss Level
      type: babyai-mini-boss-level
    metrics:
    - type: total_reward
      value: 0.53 +/- 0.41
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.56 +/- 0.50
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Move Two Across S8N9
      type: babyai-move-two-across-s8n9
    metrics:
    - type: total_reward
      value: 0.05 +/- 0.19
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.05 +/- 0.20
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: One Room S8
      type: babyai-one-room-s8
    metrics:
    - type: total_reward
      value: 0.92 +/- 0.04
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.04
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Open Door
      type: babyai-open-door
    metrics:
    - type: total_reward
      value: 0.99 +/- 0.00
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.01
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Open Doors Order N4
      type: babyai-open-doors-order-n4
    metrics:
    - type: total_reward
      value: 0.96 +/- 0.14
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.96 +/- 0.17
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Open Red Door
      type: babyai-open-red-door
    metrics:
    - type: total_reward
      value: 0.92 +/- 0.03
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.03
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Open Two Doors
      type: babyai-open-two-doors
    metrics:
    - type: total_reward
      value: 0.98 +/- 0.00
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.00
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Open
      type: babyai-open
    metrics:
    - type: total_reward
      value: 0.95 +/- 0.08
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.99 +/- 0.10
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Pickup Above
      type: babyai-pickup-above
    metrics:
    - type: total_reward
      value: 0.92 +/- 0.06
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.01 +/- 0.07
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Pickup Dist
      type: babyai-pickup-dist
    metrics:
    - type: total_reward
      value: 0.87 +/- 0.12
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.02 +/- 0.16
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Pickup Loc
      type: babyai-pickup-loc
    metrics:
    - type: total_reward
      value: 0.85 +/- 0.19
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.92 +/- 0.23
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Pickup
      type: babyai-pickup
    metrics:
    - type: total_reward
      value: 0.79 +/- 0.30
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.85 +/- 0.36
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Put Next Local
      type: babyai-put-next-local
    metrics:
    - type: total_reward
      value: 0.67 +/- 0.32
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.73 +/- 0.35
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Put Next S7N4
      type: babyai-put-next
    metrics:
    - type: total_reward
      value: 0.85 +/- 0.25
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.89 +/- 0.26
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Synth Loc
      type: babyai-synth-loc
    metrics:
    - type: total_reward
      value: 0.77 +/- 0.34
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.78 +/- 0.43
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Synth Seq
      type: babyai-synth-seq
    metrics:
    - type: total_reward
      value: 0.57 +/- 0.43
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.58 +/- 0.49
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Synth
      type: babyai-synth
    metrics:
    - type: total_reward
      value: 0.75 +/- 0.35
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.78 +/- 0.43
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Unblock Pickup
      type: babyai-unblock-pickup
    metrics:
    - type: total_reward
      value: 0.79 +/- 0.29
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.86 +/- 0.35
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Unlock Local
      type: babyai-unlock-local
    metrics:
    - type: total_reward
      value: 0.98 +/- 0.01
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.01
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Unlock Pickup
      type: babyai-unlock-pickup
    metrics:
    - type: total_reward
      value: 0.75 +/- 0.03
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.05
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Unlock To Unlock
      type: babyai-unlock-to-unlock
    metrics:
    - type: total_reward
      value: 0.85 +/- 0.31
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.88 +/- 0.32
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Unlock
      type: babyai-unlock
    metrics:
    - type: total_reward
      value: 0.43 +/- 0.43
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.48 +/- 0.52
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Assembly
      type: metaworld-assembly
    metrics:
    - type: total_reward
      value: 243.78 +/- 10.44
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.99 +/- 0.05
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Basketball
      type: metaworld-basketball
    metrics:
    - type: total_reward
      value: 1.71 +/- 0.63
      name: Total reward
    - type: expert_normalized_total_reward
      value: -0.00 +/- 0.00
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: BinPicking
      type: metaworld-bin-picking
    metrics:
    - type: total_reward
      value: 314.42 +/- 196.40
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.74 +/- 0.46
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Box Close
      type: metaworld-box-close
    metrics:
    - type: total_reward
      value: 482.86 +/- 146.37
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.93 +/- 0.34
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Button Press Topdown Wall
      type: metaworld-button-press-topdown-wall
    metrics:
    - type: total_reward
      value: 268.30 +/- 82.78
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.51 +/- 0.18
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Button Press Topdown
      type: metaworld-button-press-topdown
    metrics:
    - type: total_reward
      value: 269.14 +/- 82.81
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.52 +/- 0.18
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Button Press Wall
      type: metaworld-button-press-wall
    metrics:
    - type: total_reward
      value: 608.87 +/- 169.50
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.90 +/- 0.25
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Button Press
      type: metaworld-button-press
    metrics:
    - type: total_reward
      value: 624.03 +/- 73.53
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.97 +/- 0.12
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Coffee Button
      type: metaworld-coffee-button
    metrics:
    - type: total_reward
      value: 334.92 +/- 301.67
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.43 +/- 0.43
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Coffee Pull
      type: metaworld-coffee-pull
    metrics:
    - type: total_reward
      value: 38.00 +/- 63.97
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.13 +/- 0.25
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Coffee Push
      type: metaworld-coffee-push
    metrics:
    - type: total_reward
      value: 151.38 +/- 207.69
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.30 +/- 0.42
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Dial Turn
      type: metaworld-dial-turn
    metrics:
    - type: total_reward
      value: 752.25 +/- 138.50
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.95 +/- 0.18
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Disassemble
      type: metaworld-disassemble
    metrics:
    - type: total_reward
      value: 40.87 +/- 9.35
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.22 +/- 3.71
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Door Close
      type: metaworld-door-close
    metrics:
    - type: total_reward
      value: 530.48 +/- 29.02
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.06
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Door Lock
      type: metaworld-door-lock
    metrics:
    - type: total_reward
      value: 678.98 +/- 194.57
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.81 +/- 0.28
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Door Open
      type: metaworld-door-open
    metrics:
    - type: total_reward
      value: 574.71 +/- 50.82
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.99 +/- 0.10
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Door Unlock
      type: metaworld-door-unlock
    metrics:
    - type: total_reward
      value: 761.82 +/- 114.70
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.94 +/- 0.16
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Drawer Close
      type: metaworld-drawer-close
    metrics:
    - type: total_reward
      value: 519.05 +/- 154.38
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.54 +/- 0.21
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Drawer Open
      type: metaworld-drawer-open
    metrics:
    - type: total_reward
      value: 486.02 +/- 34.17
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.98 +/- 0.09
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Faucet Close
      type: metaworld-faucet-close
    metrics:
    - type: total_reward
      value: 366.78 +/- 86.77
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.23 +/- 0.17
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Faucet Open
      type: metaworld-faucet-open
    metrics:
    - type: total_reward
      value: 685.01 +/- 65.52
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.96 +/- 0.14
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Hammer
      type: metaworld-hammer
    metrics:
    - type: total_reward
      value: 678.36 +/- 79.36
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.98 +/- 0.13
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Hand Insert
      type: metaworld-hand-insert
    metrics:
    - type: total_reward
      value: 695.27 +/- 134.25
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.94 +/- 0.18
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Handle Press Side
      type: metaworld-handle-press-side
    metrics:
    - type: total_reward
      value: 65.07 +/- 69.65
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.01 +/- 0.09
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Handle Press
      type: metaworld-handle-press
    metrics:
    - type: total_reward
      value: 695.97 +/- 311.48
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.79 +/- 0.40
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Handle Pull Side
      type: metaworld-handle-pull-side
    metrics:
    - type: total_reward
      value: 145.34 +/- 179.01
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.37 +/- 0.47
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Handle Pull
      type: metaworld-handle-pull
    metrics:
    - type: total_reward
      value: 514.56 +/- 205.75
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.77 +/- 0.31
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Lever Pull
      type: metaworld-lever-pull
    metrics:
    - type: total_reward
      value: 250.51 +/- 220.33
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.34 +/- 0.40
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Peg Insert Side
      type: metaworld-peg-insert-side
    metrics:
    - type: total_reward
      value: 305.94 +/- 166.53
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.97 +/- 0.53
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Peg Unplug Side
      type: metaworld-peg-unplug-side
    metrics:
    - type: total_reward
      value: 120.73 +/- 169.26
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.26 +/- 0.37
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Pick Out Of Hole
      type: metaworld-pick-out-of-hole
    metrics:
    - type: total_reward
      value: 2.08 +/- 0.05
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.00 +/- 0.00
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Pick Place Wall
      type: metaworld-pick-place-wall
    metrics:
    - type: total_reward
      value: 62.30 +/- 131.13
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.14 +/- 0.29
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Pick Place
      type: metaworld-pick-place
    metrics:
    - type: total_reward
      value: 311.95 +/- 180.95
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.74 +/- 0.43
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Plate Slide Back Side
      type: metaworld-plate-slide-back-side
    metrics:
    - type: total_reward
      value: 689.54 +/- 157.90
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.94 +/- 0.23
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Plate Slide Back
      type: metaworld-plate-slide-back
    metrics:
    - type: total_reward
      value: 197.00 +/- 1.58
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.24 +/- 0.00
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Plate Slide Side
      type: metaworld-plate-slide-side
    metrics:
    - type: total_reward
      value: 122.56 +/- 24.56
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.16 +/- 0.04
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Plate Slide
      type: metaworld-plate-slide
    metrics:
    - type: total_reward
      value: 456.66 +/- 198.51
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.84 +/- 0.44
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Push Back
      type: metaworld-push-back
    metrics:
    - type: total_reward
      value: 71.38 +/- 100.60
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.84 +/- 1.20
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Push Wall
      type: metaworld-push-wall
    metrics:
    - type: total_reward
      value: 216.66 +/- 256.33
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.28 +/- 0.35
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Push
      type: metaworld-push
    metrics:
    - type: total_reward
      value: 583.25 +/- 296.10
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.78 +/- 0.40
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Reach Wall
      type: metaworld-reach-wall
    metrics:
    - type: total_reward
      value: 681.90 +/- 186.63
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.89 +/- 0.31
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Reach
      type: metaworld-reach
    metrics:
    - type: total_reward
      value: 347.45 +/- 190.66
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.37 +/- 0.36
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Shelf Place
      type: metaworld-shelf-place
    metrics:
    - type: total_reward
      value: 60.57 +/- 97.16
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.25 +/- 0.40
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Soccer
      type: metaworld-soccer
    metrics:
    - type: total_reward
      value: 309.21 +/- 172.64
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.82 +/- 0.47
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Stick Pull
      type: metaworld-stick-pull
    metrics:
    - type: total_reward
      value: 364.98 +/- 234.82
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.70 +/- 0.45
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Stick Push
      type: metaworld-stick-push
    metrics:
    - type: total_reward
      value: 91.05 +/- 204.71
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.14 +/- 0.33
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Sweep Into
      type: metaworld-sweep-into
    metrics:
    - type: total_reward
      value: 714.98 +/- 209.19
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.89 +/- 0.27
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Sweep
      type: metaworld-sweep
    metrics:
    - type: total_reward
      value: 15.82 +/- 16.34
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.01 +/- 0.03
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Window Close
      type: metaworld-window-close
    metrics:
    - type: total_reward
      value: 347.90 +/- 222.50
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.54 +/- 0.42
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Window Open
      type: metaworld-window-open
    metrics:
    - type: total_reward
      value: 574.72 +/- 75.65
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.97 +/- 0.14
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Ant
      type: mujoco-ant
    metrics:
    - type: total_reward
      value: 4993.13 +/- 1656.89
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.86 +/- 0.28
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Inverted Double Pendulum
      type: mujoco-doublependulum
    metrics:
    - type: total_reward
      value: 8744.92 +/- 1471.45
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.94 +/- 0.16
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Half Cheetah
      type: mujoco-halfcheetah
    metrics:
    - type: total_reward
      value: 6601.12 +/- 488.36
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.89 +/- 0.06
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Hopper
      type: mujoco-hopper
    metrics:
    - type: total_reward
      value: 1435.45 +/- 361.77
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.77 +/- 0.20
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Humanoid
      type: mujoco-humanoid
    metrics:
    - type: total_reward
      value: 695.92 +/- 115.07
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.09 +/- 0.02
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Inverted Pendulum
      type: mujoco-pendulum
    metrics:
    - type: total_reward
      value: 117.64 +/- 21.73
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.24 +/- 0.05
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Pusher
      type: mujoco-pusher
    metrics:
    - type: total_reward
      value: -24.93 +/- 6.47
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.05
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Reacher
      type: mujoco-reacher
    metrics:
    - type: total_reward
      value: -5.77 +/- 2.27
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.00 +/- 0.06
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Humanoid Standup
      type: mujoco-standup
    metrics:
    - type: total_reward
      value: 113587.22 +/- 21821.69
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.33 +/- 0.09
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Swimmer
      type: mujoco-swimmer
    metrics:
    - type: total_reward
      value: 94.08 +/- 3.94
      name: Total reward
    - type: expert_normalized_total_reward
      value: 1.02 +/- 0.04
      name: Expert normalized total reward
  - task:
      type: reinforcement-learning
      name: Reinforcement Learning
    dataset:
      name: Walker 2d
      type: mujoco-walker
    metrics:
    - type: total_reward
      value: 4381.69 +/- 848.39
      name: Total reward
    - type: expert_normalized_total_reward
      value: 0.95 +/- 0.18
      name: Expert normalized total reward
---

# Model Card for Jat

This is a multi-modal and multi-task model.

## Model Details

### Model Description

- **Developed by:** The JAT Team
- **License:** Apache 2.0

### Model Sources

- **Repository:** <https://github.com/huggingface/jat>
- **Paper:** <https://huggingface.co/papers/2402.09844>
- **Demo:** Coming soon

## Training

<details>
    <summary>The model was trained on the following tasks:</summary>

- Alien
- Amidar
- Assault
- Asterix
- Asteroids
- Atlantis
- Bank Heist
- Battle Zone
- Beam Rider
- Berzerk
- Bowling
- Boxing
- Breakout
- Centipede
- Chopper Command
- Crazy Climber
- Defender
- Demon Attack
- Double Dunk
- Enduro
- Fishing Derby
- Freeway
- Frostbite
- Gopher
- Gravitar
- H.E.R.O.
- Ice Hockey
- James Bond
- Kangaroo
- Krull
- Kung-Fu Master
- Montezuma's Revenge
- Ms. Pacman
- Name This Game
- Phoenix
- PitFall
- Pong
- Private Eye
- Q*Bert
- River Raid
- Road Runner
- Robotank
- Seaquest
- Skiing
- Solaris
- Space Invaders
- Star Gunner
- Surround
- Tennis
- Time Pilot
- Tutankham
- Up and Down
- Venture
- Video Pinball
- Wizard of Wor
- Yars Revenge
- Zaxxon
- Action Obj Door
- Blocked Unlock Pickup
- Boss Level No Unlock
- Boss Level
- Find Obj S5
- Go To Door
- Go To Imp Unlock
- Go To Local
- Go To Obj Door
- Go To Obj
- Go To Red Ball Grey
- Go To Red Ball No Dists
- Go To Red Ball
- Go To Red Blue Ball
- Go To Seq
- Go To
- Key Corridor
- Mini Boss Level
- Move Two Across S8N9
- One Room S8
- Open Door
- Open Doors Order N4
- Open Red Door
- Open Two Doors
- Open
- Pickup Above
- Pickup Dist
- Pickup Loc
- Pickup
- Put Next Local
- Put Next S7N4
- Synth Loc
- Synth Seq
- Synth
- Unblock Pickup
- Unlock Local
- Unlock Pickup
- Unlock To Unlock
- Unlock
- Assembly
- Basketball
- BinPicking
- Box Close
- Button Press Topdown Wall
- Button Press Topdown
- Button Press Wall
- Button Press
- Coffee Button
- Coffee Pull
- Coffee Push
- Dial Turn
- Disassemble
- Door Close
- Door Lock
- Door Open
- Door Unlock
- Drawer Close
- Drawer Open
- Faucet Close
- Faucet Open
- Hammer
- Hand Insert
- Handle Press Side
- Handle Press
- Handle Pull Side
- Handle Pull
- Lever Pull
- Peg Insert Side
- Peg Unplug Side
- Pick Out Of Hole
- Pick Place Wall
- Pick Place
- Plate Slide Back Side
- Plate Slide Back
- Plate Slide Side
- Plate Slide
- Push Back
- Push Wall
- Push
- Reach Wall
- Reach
- Shelf Place
- Soccer
- Stick Pull
- Stick Push
- Sweep Into
- Sweep
- Window Close
- Window Open
- Ant
- Inverted Double Pendulum
- Half Cheetah
- Hopper
- Humanoid
- Inverted Pendulum
- Pusher
- Reacher
- Humanoid Standup
- Swimmer
- Walker 2d

</details>

## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("jat-project/jat")
```

## Citation


```bibtex
@article{gallouedec2024jack,
    title = {{Jack of All Trades, Master of Some, a Multi-Purpose Transformer Agent}},
    author = {Gallouédec, Quentin and Beeching, Edward and Romac, Clément and Dellandréa, Emmanuel},
    journal = {arXiv preprint arXiv:2402.09844},
    year = {2024},
    url = {https://arxiv.org/abs/2402.09844}
}
```
