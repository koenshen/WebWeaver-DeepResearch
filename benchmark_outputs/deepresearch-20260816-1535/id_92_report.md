

# Analysis and Study of Singles Badminton Player Actions Using Sports Videos: A Refined Research Framework

---

## Executive Summary

This report presents a comprehensive, refined research framework for analyzing and studying singles badminton player actions from sports videos, organized across four interdependent research components: (1) object detection and tracking, (2) recognition of technical actions, (3) recognition of tactical intent, and (4) prediction of subsequent actions. Each component is analyzed with respect to state-of-the-art methodologies, available datasets, technical challenges, performance benchmarks, and recommended optimization strategies. The framework emphasizes a modular, video-based pipeline in which each component feeds semantically richer representations into the next—from raw pixel-level detection to high-level tactical forecasting—while maintaining computational feasibility and real-time applicability.

---

## Component 1: Object Detection and Tracking within Badminton Videos

### 1.1 Problem Definition and Scope

Object detection and tracking in badminton videos involves identifying and continuously localizing three primary entities across video frames: (1) the players (singles: two players), (2) the shuttlecock, and (3) the court/playing boundaries. This component forms the foundational layer of the entire pipeline, as all subsequent action recognition, tactical analysis, and prediction tasks depend on accurate spatial-temporal localization of these entities.

### 1.2 Key Technical Challenges

**Shuttlecock-specific challenges.** The shuttlecock is arguably the most difficult object to detect in sports video analysis. It is extremely small (often only 2–5 pixels in broadcast footage), moves at exceptionally high speeds (the fastest shot in badminton can exceed 400 km/h, making it the fastest ball game in the world), and is frequently subject to motion blur, afterimages, occlusions (by players, nets, or the shuttlecock's own feathers), and background interference. These characteristics make generic object detectors (e.g., standard YOLO variants) inadequate for shuttlecock tracking without substantial modification (https://www.sciencedirect.com/science/article/abs/pii/S0957417420306436).

**Player-specific challenges.** Player detection is complicated by rapid directional changes, frequent occlusions between players and against the court background, similar jersey/appearance between opponents, camera angle variations in broadcast footage, and the need for identity preservation across frame switches and long rallies (https://arxiv.org/html/2508.13507v1).

### 1.3 State-of-the-Art Approaches

#### 1.3.1 Shuttlecock Tracking

**TrackNet family.** The TrackNet architecture, introduced by Huang et al. (2019), was specifically designed for tracking high-speed, tiny objects in sports videos. TrackNet employs a heatmap-based deep learning approach that processes multiple consecutive frames (typically 3–5 frames) simultaneously to exploit temporal motion information. This design effectively addresses motion blur and afterimage problems by leveraging temporal context (https://dr.lib.iastate.edu/bitstreams/24171391-e255-411c-8c4e-0d0e3d7c0953/download).

**TrackNetV2** introduced architectural refinements including Multiple-In Multiple-Out (MIMO) design, reduced input size for faster processing, and reduced GPU memory consumption, improving both accuracy and real-time capability (https://scholar.nycu.edu.tw/en/publications/tracknetv2-efficient-shuttlecock-tracking-network).

**TrackNetV3** represents the current state-of-the-art in shuttlecock tracking. It comprises two core modules: (1) a trajectory prediction module that leverages estimated background information and mixup data augmentation for robustness against visual interference, and (2) a trajectory rectification module that creates "repair masks" by analyzing predicted trajectories and correcting paths via inpainting when the shuttlecock is occluded or temporarily lost. Benchmark results demonstrate TrackNetV3's superiority:

| Model | Accuracy | Precision | Recall | F1 | FPS |
|-------|----------|-----------|--------|-----|-----|
| YOLOv7 | 57.82% | 78.53% | 59.96% | 68.00% | 34.77 |
| TrackNetV2 | 94.98% | 99.64% | 94.56% | 97.03% | 27.70 |
| TrackNetV3 | 97.51% | 97.79% | 99.33% | 98.56% | 25.11 |

(https://github.com/qaz812345/TrackNetV3; https://dl.acm.org/doi/abs/10.1145/3595916.3626370)

**Alternative approaches.** The improved Tiny YOLOv2 with Unscented Kalman Filter (UKF) combination has been shown to achieve an average trajectory tracking accuracy of 91.40% and recall of 84.60%, with precision/recall of 96.7%/95.7% at 29.2 frames/second across four simple and complex badminton flight scenarios (https://www.sciencedirect.com/science/article/pii/S2405844024148967). U-Net-based residual learning approaches have also been explored for shuttlecock detection (https://joiv.org/index.php/joiv/article/viewFile/2132/1043).

#### 1.3.2 Player Detection and Tracking

**YOLO family.** YOLO (You Only Look Once) variants—particularly YOLOv5, YOLOv7, and YOLOv8—are the dominant approaches for player detection in badminton. These one-stage detectors offer an optimal balance of speed and accuracy for real-time applications. Hybrid architectures combining YOLOv8n for player detection with ResNet50 for court keypoint extraction have been demonstrated for badminton action recognition pipelines (https://www.scribd.com/document/858063606/Badminton-HYBRID-DEEP-LEARNING-MODEL).

**Multi-object tracking.** For sustained identity preservation, tracking-by-detection paradigms are preferred. DeepSORT (Deep Simple Online and Realtime Tracking) is widely used in badminton analysis pipelines, associating detections across frames via appearance features and motion prediction (https://www.springerprofessional.de/en/badminton-player-s-shot-prediction-using-deep-learning/25253060). Recent work has emphasized the importance of identity preservation mechanisms (ID switching prevention) in multi-player scenarios, with empirically determined pixel thresholds proving robust for typical badminton court dynamics (https://arxiv.org/html/2508.13507v1).

#### 1.3.3 Court Detection and Homography Mapping

Court detection typically employs model-based approaches following Farin et al.'s methodology, which detect line segments and match them to known court templates. These court models enable homography transformation—mapping 2D image coordinates to real-world court coordinates—which is essential for tactical analysis (e.g., computing player court coverage, shot placement areas) and for grounding action recognition in physical space (https://cs.stanford.edu/people/paulliu/files/cvpr-2022.pdf).

#### 1.3.4 Pose Estimation

Pose estimation serves as a bridge between object tracking and action recognition. OpenPose, with its Part Affinity Fields (PAFs), has been widely adopted for extracting 25 key body points per player in badminton analysis (https://github.com/mithileshgau/Openpose-Analysis). AlphaPose provides an alternative with strong performance on sports data (https://github.com/mithileshgau/Openpose-Analysis). More recent approaches leverage YOLOv8-Pose, which integrates pose estimation into the YOLO architecture for improved speed, with domain-specific enhancements using efficient local attention mechanisms (https://pmc.ncbi.nlm.nih.gov/articles/PMC12298368).

### 1.4 Recommended Methodological Framework

Based on the literature, the following optimized pipeline is recommended for Component 1:

1. **Input preprocessing**: Frame extraction at 25–30 FPS from broadcast or fixed-camera footage, with resolution normalization.
2. **Player detection**: Fine-tuned YOLOv8 model on a badminton-specific player dataset (e.g., Roboflow's badminton players dataset or a custom-annotated corpus) (https://universe.roboflow.com/hongy20/badminton-players-detection-gwgb1).
3. **Player tracking**: DeepSORT or ByteTrack for identity preservation across frames, with homography-based position mapping to court coordinates.
4. **Pose estimation**: YOLOv8-Pose or MMPose for 17-keypoint skeleton extraction per player, feeding downstream action recognition.
5. **Shuttlecock tracking**: TrackNetV3 for trajectory estimation, given its superior accuracy (97.51%) and robustness to occlusion.
6. **Court detection**: Model-based court line detection with homography estimation for grounding all positions in real-world coordinates.
7. **Fusion layer**: Synchronize all tracking outputs into a unified spatiotemporal representation (player positions, skeletons, shuttlecock trajectory, court coordinates) for downstream processing.

### 1.5 Evaluation Metrics

Standard evaluation metrics include: detection accuracy (IoU-based), tracking precision/recall, F1-score, multi-object tracking accuracy (MOTA), identity-switch frequency, and processing speed (FPS). For shuttlecock tracking, position error thresholds (e.g., success defined as <12 pixels deviation from annotated position) are commonly used (https://spyro-soft.com/blog/artificial-intelligence-machine-learning/instant-review-system-for-badminton-computer-vision-use-case).

---

## Component 2: Recognition of Technical Actions Performed by Singles Players

### 2.1 Problem Definition

Technical action recognition (also termed "stroke recognition" or "shot classification") refers to automatically identifying which badminton stroke type a player is executing—such as clear, smash, drop shot, drive, net shot, lift, push, serve, and defensive shots—from video data. This component transforms low-level tracking data into semantically meaningful action labels that form the basis for tactical analysis and prediction.

### 2.2 Action Taxonomy

A comprehensive action taxonomy for badminton singles typically includes 18–23 distinct stroke types. The VideoBadminton dataset defines 18 classes aligned with Badminton World Federation (BWF) standards, including: Short Serve, Cross-Court Flight, Lift, Tap Smash, Block, Drop Shot, Push Shot, Transitional Slice, and others (https://arxiv.org/html/2403.12385v2). The ShuttleSet dataset defines 10 distinct shot types: net shot, clear, push/rush, smash, defensive shot, drive, lob, drop shot, serve, and unknown/error (https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf). A broader study of international matches identified 23 initial technical action features including High, Smash, Dribble, Push, Slice/Drop, Lift, Block Smash, Net Front, Clear, and Drive (https://www.nature.com/articles/s41598-025-87610-7).

### 2.3 Methodological Approaches

#### 2.3.1 Video-Based Deep Learning Architectures

**3D CNNs and hybrid architectures.** The R(2+1)D architecture, which factorizes 3D convolutions into 2D spatial and 1D temporal convolutions, has been effectively applied to badminton shot classification. Hybrid models combining YOLOv8n (player detection), ResNet50 (court keypoints), and r3d_18 (shot classification) have demonstrated real-time processing capability in integrated systems (https://www.scribd.com/document/858063606/Badminton-HYBRID-DEEP-LEARNING-MODEL).

**Two-stream networks.** Following Simonyan and Zisserman's seminal two-stream ConvNet architecture (spatial stream on RGB frames + temporal stream on optical flow), badminton-specific adaptations have been developed to capture both appearance and motion cues (https://www.semanticscholar.org/paper/Recognition-of-Badminton-Action-Using-Convolutional-Rahmad-Sufri/fab4f2e98a08f588f931a4e5c93885ba612c305d).

**State-of-the-art video recognition models.** A comprehensive benchmark on the VideoBadminton dataset (7,822 clips, 18 action classes, 145 minutes of footage) evaluated multiple architectures:

| Model | Top-1 Accuracy | Mean Class Accuracy |
|-------|---------------|---------------------|
| **SlowFast** | **82.80%** | **73.80%** |
| Video Swin Transformer | 81.99% | — |
| PoseC3D | 80.76% | — |
| R(2+1)D | 79.53% | — |
| ST-GCN | 74.41% | — |
| TimeSformer | 73.18% | — |
| MViT-V2 | 14.23% | — |

(https://arxiv.org/html/2403.12385v2)

SlowFast's dual-pathway architecture—a Slow pathway at low frame rate capturing spatial semantics and a Fast pathway at high frame rate capturing fine temporal motion—proved optimal for fine-grained badminton action recognition.

#### 2.3.2 Skeleton-Based Approaches

**Graph Convolutional Networks (GCNs).** ST-GCN (Spatial-Temporal Graph Convolutional Network) treats skeleton joints as graph nodes with natural body connections as edges, learning spatial patterns via graph convolutions and temporal patterns via temporal convolutions (https://arxiv.org/html/2403.12385v2).

**Pose-based classification.** PoseC3D, which processes skeleton data as 3D heatmap volumes, achieved 80.76% Top-1 accuracy on VideoBadminton—competitive with video-based methods while being more computationally efficient (https://arxiv.org/html/2403.12385v2).

**Transformer-based skeleton models.** The Badminton Stroke-type Transformer (BST) represents the current frontier. BST shifts focus from player poses to shuttlecock trajectory information as the primary input modality, processing player poses and shuttlecock trajectories through separate pathways fused in a second transformer encoder. BST demonstrates that leveraging shuttlecock trajectory—the interactive medium between players—significantly improves stroke-type classification accuracy. It outperforms previous state-of-the-art on ShuttleSet, BadmintonDB, and a tennis dataset (TenniSet) (https://github.com/Va6lue/BST-Badminton-Stroke-type-Transformer; https://openaccess.thecvf.com/content/CVPR2026W/CVsports/html/Chang_BST_Badminton_Stroke-type_Transformer_for_Skeleton-based_Action_Recognition_in_Racket_CVPRW_2026_paper.html).

#### 2.3.3 Recurrent and Sequential Models

**LSTM-based recognition.** LSTM networks trained on keypoint movements during shot execution have been successfully applied to classify fundamental shots (Clear, Serve, Smash) (https://link.springer.com/chapter/10.1007/978-3-031-60935-0_28).

**CNN-LSTM hybrids.** Combining CNN feature extractors with LSTM temporal modeling has proven effective. A framework combining CNN, LSTM, and self-attention mechanisms achieved 97.83% accuracy on a dataset of 37 badminton actions, demonstrating the power of hybrid architectures for capturing both time-domain and global signals (https://www.nature.com/articles/s41598-025-02771-9).

#### 2.3.4 Ensemble and Hybrid Feature Approaches

**Spatio-temporal features with ensemble learning.** Recent work combining handcrafted RGB-based descriptors (HOG, Histogram of Optical Flow), skeleton-based features, and Fast Dynamic Time Warping (FDTW) temporal features with weighted ensemble learning (SVM, Logistic Regression, Random Forest, AdaBoost) achieved 95.38% accuracy (E2 ensemble of SVM+LR+AdaBoost) on badminton stroke recognition (https://www.techscience.com/cmc/v81n2/58683).

**Hybrid RGB-skeleton features.** Combining RGB descriptors, skeleton features, and ensemble machine learning (Random Forest, AdaBoost) achieved 98.21% accuracy, with the best-performing feature combination being ROMI, DTW, and HOF (https://www.etasr.com/index.php/ETASR/article/view/15586).

#### 2.3.5 Wearable/Sensor-Based Recognition

While this research project focuses on video-based analysis, it is informative that IMU-based approaches (two sensors on racket and wrist) with 1D-CNN achieve 97.16% accuracy for six stroke types and 86.07% for fifteen shuttle trajectories, outperforming traditional machine learning (KNN: 94.94%/78.71%; SVM: 94.32%/75.06%) (https://www.nature.com/articles/s41598-025-25158-2).

### 2.4 Action Quality Assessment

Beyond recognition, deep learning methods have been developed for action quality assessment. A recent system achieved professional-level stroke identification accuracy of 83.08% (Top-1) and 96.89% (Top-3), demonstrating that deep learning can approach expert-level action evaluation (https://journals.sagepub.com/doi/10.1177/1088467X251353444).

### 2.5 Recommended Methodological Framework

For optimal technical action recognition in this research project:

1. **Primary approach**: Implement a multi-modal recognition system combining:
   - Skeleton-based recognition using the BST Transformer architecture (leveraging both player poses and shuttlecock trajectory), given its demonstrated state-of-the-art performance.
   - Video-based recognition using SlowFast as a complementary modality for context-rich features.
2. **Feature fusion**: Ensemble predictions from skeleton-based and video-based models via soft voting or learned fusion, leveraging complementary strengths.
3. **Temporal context**: Incorporate rally-level temporal context (previous strokes) via LSTM or attention mechanisms to disambiguate strokes with similar visual appearance but different rally contexts.
4. **Shot boundary detection**: Use shuttlecock hit detection (via TrackNet trajectory discontinuities combined with player swing detection via YOLO) to segment continuous video into discrete stroke events, enabling frame-accurate action segmentation (https://www.mdpi.com/1424-8220/24/13/4372).

---

## Component 3: Recognition of Tactical Intent behind Singles Players' Actions

### 3.1 Problem Definition

Tactical intent recognition moves beyond identifying *what* action a player performs to understanding *why* they perform it—the strategic purpose behind each stroke. In badminton singles, tactical intent encompasses: offensive vs. defensive posture, shot placement strategy (e.g., targeting opponent's backhand corner, forcing movement to the net), rally progression management (e.g., building an attack sequence), and adaptation to opponent positioning and tendencies.

### 3.2 The Data Foundation: Turn-Based Sequence Analysis

Tactical intent cannot be understood from isolated strokes; it requires modeling the rally as a turn-based sequence of interdependent actions. This has driven the creation of stroke-level datasets with rich tactical annotations.

**ShuttleSet** is the largest publicly available badminton singles dataset with stroke-level records. It comprises 44 broadcast matches (2018–2021), 104 sets, 3,685 rallies, and 36,492 strokes involving 27 top-ranking men's and women's singles players. Each stroke is annotated with temporal, spatial, tactical, and posture information, including 18 distinct shot types, hitting locations, and player positions. The dataset was created via a computer-aided labeling tool with expert annotation to ensure reliability (https://ar5iv.labs.arxiv.org/html/2306.04948; https://dl.acm.org/doi/10.1145/3580305.3599906).

**ShuttleSet22** provides a train/validation/test split of ShuttleSet for benchmarked stroke forecasting: 30,172 strokes in 2,888 rallies (training), 1,400 strokes in 450 rallies (validation), and 2,040 strokes in 654 rallies (testing) (https://arxiv.org/html/2306.15664v1).

### 3.3 Methodological Approaches to Tactical Analysis

#### 3.3.1 Sequence Modeling for Stroke Influence and Tactical Patterns

**Long Short-Term Dependency Modeling.** Deep learning approaches using LSTM architectures have quantified the influence of individual shots within rallies, modeling how each stroke contributes to point outcomes. This approach establishes the causal chain of tactical intent—each stroke's value is understood in terms of how it shapes subsequent rally dynamics (https://arxiv.org/html/2508.13507v1).

**Deep Learning Rally Outcome Prediction.** A player-independent framework using CNN-extracted stroke features (ResNet-18) fed into LSTM/GRU models demonstrated that Bidirectional LSTM provides the best rally outcome prediction performance, capturing the tactical progression of rallies (https://ui.adsabs.harvard.edu/abs/2022spcs.conf...25T/abstract).

#### 3.3.2 Position-Aware and Player-Style Modeling

**ShuttleNet** introduced a Position-aware Fusion of Rally Progress and Player Styles framework, incorporating two modified encoder-decoder extractors: one modeling rally progress (the sequential structure of the rally) and one modeling individual player styles. A position-aware gated fusion network combines these contexts. ShuttleNet formulates stroke forecasting as a turn-based sequence prediction task with multiple outputs (shot type and area coordinates), explicitly modeling the alternating nature of badminton singles. This framework demonstrated that both rally-level context and player-specific characteristics are critical for understanding tactical patterns (https://arxiv.org/abs/2112.01044; https://ojs.aaai.org/index.php/AAAI/article/view/20341).

#### 3.3.3 Machine Learning for Technical-Tactical Pattern Mining

**Random Forest with Technical Action Frequencies.** A large-scale study of 303 international matches (2019–2023) involving top-10 BWF players (153 men's singles matches/358 games; 150 women's singles/344 games) developed a random forest model to predict game outcomes from technical action frequency features. The model achieved:
- **Men's model**: Accuracy 87%, Sensitivity 0.93, Specificity 0.80, PPV 0.84, NPV 0.91 (AUC = 0.9656 with optimal hyperparameters).
- **Women's model**: Accuracy 83%, Sensitivity 0.92, Specificity 0.68, PPV 0.82, NPV 0.85 (AUC = 0.8950).

SHAP analysis identified **Net Front, Slice/Drop, and Push** as the most influential technical actions for winning outcomes in both sexes—these represent tactical control patterns (net control, variation, and aggressive driving). Notably, male models required only 5 key features while female models required 22, reflecting more complex tactical styles in women's singles (https://www.nature.com/articles/s41598-025-87610-7).

**Support Vector Machine for Player-Specific Analysis.** Research on An Se-young (2023 BWF world #1) established a scoring and losing prediction model using improved data classification, achieving 87.5% prediction accuracy with SVM (https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0312801).

#### 3.3.4 Deep Reinforcement Learning for Tactical Evaluation

**Q-function-based tactical evaluation.** Deep reinforcement learning has been applied to evaluate tactical behaviors using Q-functions, providing detailed insights into the strategic value of player actions within technical and tactical contexts. This approach goes beyond descriptive statistics to prescriptive tactical evaluation (https://www.nature.com/articles/s41598-025-87610-7).

**Offline reinforcement learning for tactical decision-making.** More recent work applies offline reinforcement learning (specifically Conservative Q-Learning, CQL, with Hybrid Action Space) to derive optimal tactical policies directly from match data, eliminating human dependency in tactical policy generation. This approach achieved significantly higher average rewards than behavior policies, demonstrating potential for automated tactical training and recommendation (https://www.sciencedirect.com/science/article/abs/pii/S0952197625034268).

#### 3.3.5 Visualization and Interpretability for Tactical Understanding

**TIVEE (Tactics in Immersive Virtual Environments).** A 3D visualization system providing multi-level exploration of spatial tactics dynamics, enabling coaches to understand tactical patterns through immersive visualization of player movements and shot placements (https://www.nature.com/articles/s41598-025-87610-7).

**CoachAI Platform.** A comprehensive AI coach platform integrates OpenPose for pose estimation, TrackNet for shuttlecock tracking, and tactical analysis modules for automated match analysis and training support (https://inoliao.github.io/CoachAI; https://arxiv.org/pdf/2403.08956).

### 3.4 Recommended Methodological Framework

For tactical intent recognition in this research project:

1. **Stroke-level annotation**: Build on the ShuttleSet taxonomy and annotation structure, mapping recognized technical actions to tactical labels (offensive, defensive, neutral; court-zone targeting; shot combination patterns).
2. **Sequence modeling**: Employ transformer-based architectures (following ShuttleNet's position-aware fusion paradigm) to model rally progress and player styles jointly.
3. **Positional context**: Incorporate player court positions and shuttlecock trajectory data to infer tactical intent—e.g., a smash from the baseline (offensive intent) vs. a defensive lift from the net area (reactive intent).
4. **Counterfactual/reinforcement learning analysis**: Apply deep RL (Q-function or CQL-based) to evaluate the strategic value of recognized actions, distinguishing intent from mere execution.
5. **Explainability**: Use SHAP values and attention visualization to make tactical intent recognition interpretable for coaches and players.

---

## Component 4: Prediction of Singles Players' Subsequent Actions

### 4.1 Problem Definition

Action prediction (also termed "action forecasting" or "anticipation") in badminton singles involves predicting the player's next stroke—including shot type, placement/area, and potentially subsequent movement—based on the observed rally history. This is a fundamentally more challenging task than recognition because it requires modeling not just what has happened, but projecting forward based on tactical understanding, player tendencies, and rally dynamics.

### 4.2 The Predictive Task Formulation

Following the formulation in RallyTemPose, a stroke is defined as the motion of a player from preparing to hit the shuttle until shortly after racket-shuttle contact. A rally is a sequence of alternating strokes between players. The prediction objective is: given the observed sequence of strokes s₁:i, player skeleton poses K₁:i, and player ground positions G₁:i, predict the next stroke sᵢ₊₁ (https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf).

### 4.3 State-of-the-Art Approaches

#### 4.3.1 Transformer-Based Forecasting

**RallyTemPose** is the current state-of-the-art transformer encoder-decoder model for badminton stroke forecasting. Its architecture comprises:

- **Encoder**: A linear projection layer embeds raw player positions and skeleton poses into tokens; a learnable Joint Encoding (JE) provides joint arrangement information; a Spatial Transformer (ST) captures inter-keypoint spatial relationships; Grouped Pooling Blocks (GPB) aggregate and reduce dimensionality; a Temporal Transformer (TT) models pose movement dynamics over time; both inter-player (cross-attention) and intra-player (self-attention) are computed.
- **Decoder**: An embedding layer maps stroke sequences to tokens; player-specific representations condition the decoding; a Decoder Block (DB) combines self-attention, dual cross-attention, and adaptive fusion; an MLP head predicts next-stroke probabilities.
- **Enhanced stroke embeddings**: Stroke descriptions are processed through a pre-trained BERT language model to generate semantically rich stroke embeddings.
- **Training**: Combined main cross-entropy loss and auxiliary loss on latent stroke representations (γ = 0.3).

**Performance results:**

| Dataset | Accuracy | Top-2 Accuracy | Top-3 Accuracy |
|---------|----------|----------------|----------------|
| ShuttleSet | 54.3% | 77.3% | 92.5% |
| BadmintonDB | 62.8% | — | 93.1% |

RallyTemPose outperformed all baseline approaches (Seq2Seq, Transformer, Actionformer + Transformer decoder). Ablation studies revealed that **player ground position** is the most critical input component (removing it causes a 2.6% performance drop), while player-specific embeddings provide only marginal accuracy gains but enable valuable player-style analysis. The latent representations show useful properties for player comparison and tactical analysis, with t-SNE visualizations revealing clear groupings of stroke types and partial groupings of player styles (https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf).

#### 4.3.2 Position-Aware Fusion Models

**ShuttleNet** approaches prediction as a stroke forecasting problem with multiple outputs (shot type and area coordinates). Its position-aware fusion of rally progress and player styles demonstrated superior performance over conventional sequential models (LSTM, Seq2Seq, Transformer) for predicting future strokes. The model explicitly captures the turn-based nature of badminton by separating the styles of both players and integrating them with current rally conditions (https://arxiv.org/abs/2112.01044).

#### 4.3.3 Shuttlecock Trajectory Prediction

**Player-information-aware trajectory prediction.** Future shuttlecock trajectory prediction using player information has been investigated with LSTM as the primary model, compared against RNN, GRU, Transformer, and Seq2Seq architectures. The study demonstrated that incorporating player posture information significantly improves trajectory prediction accuracy, and that player position information is crucial for predicting shuttlecock destination (https://pmc.ncbi.nlm.nih.gov/articles/PMC10219238).

**Physics-based trajectory forecasting.** The Stanford CVPR 2022 work on shuttle trajectory reconstruction from monocular badminton video integrates court detection, shuttlecock tracking, and player pose analysis to segment videos into rallies and reconstruct faithful 3D trajectories for each shot using nonlinear optimization (https://cs.stanford.edu/people/paulliu/files/cvpr-2022.pdf).

#### 4.3.4 Neural Network-Based Smash Return Prediction

A specialized approach for smash return prediction uses machine learning applied to positional information of players and shuttlecock to predict where a player will hit a smash based on opponent location, and subsequently predict where the opponent will hit the return and whether they can successfully return the smash. This models the strategic anticipation inherent in professional play (https://ui.adsabs.harvard.edu/abs/2023SPIE12592E..1LK/abstract).

#### 4.3.5 Hybrid KNN-HMM for Real-Time Prediction

A recent real-time stroke prediction system integrating K-Nearest Neighbors with Hidden Markov Models (KNN-HMM) achieved 97.5% accuracy with 32ms latency and 90.8% streaming accuracy. This approach leverages HMM's sequential modeling capabilities combined with KNN's classification power for real-time deployment scenarios (https://link.springer.com/article/10.1186/s40537-026-01396-7).

### 4.4 Benchmarking and Evaluation

**ShuttleSet22 Stroke Forecasting Benchmark.** The official benchmark for stroke forecasting tasks uses ShuttleSet22, evaluating models on predicting future strokes (shot types and area coordinates) given observed strokes. The challenge revealed that improvements primarily focused on shot type prediction (from 2.1777 to 1.7892 error), while area coordinate prediction remains challenging (0.6997 to 0.6797), with most teams inferior to the ShuttleNet baseline on this dimension. This indicates that spatial placement prediction is a critical open challenge (https://arxiv.org/html/2306.15664v1).

### 4.5 Recommended Methodological Framework

For action prediction in this research project:

1. **Multi-modal input fusion**: Integrate skeleton poses, player court positions, shuttlecock trajectories, and stroke history as inputs—mirroring RallyTemPose's architecture, which demonstrated that ground positions are the most critical input.
2. **Transformer-based encoder-decoder**: Adopt the transformer paradigm for its demonstrated superiority in capturing long-range dependencies in turn-based sequences.
3. **Player-style modeling**: Incorporate player-specific embeddings to capture individual playing tendencies and predictability (with the noted finding that some players are >20% more predictable than others, indicating variance in stroke masking ability).
4. **Hierarchical prediction**: Predict at multiple levels—shot type, placement area, and subsequent player movement—following ShuttleNet's multi-output formulation.
5. **Temporal horizon**: Evaluate prediction at increasing temporal offsets (immediate next stroke vs. 2–3 strokes ahead) to characterize the limits of predictability in badminton.
6. **Real-time capability**: For practical applications, explore lightweight prediction architectures (e.g., KNN-HMM hybrid) that achieve high accuracy with minimal latency.

---

## Integrated Pipeline Architecture

The four research components form a hierarchical, interdependent pipeline:

```
Component 1: Detection & Tracking
    ↓ (player boxes, skeletons, shuttlecock trajectory, court coordinates)
Component 2: Technical Action Recognition
    ↓ (stroke type labels, confidence scores, temporal boundaries)
Component 3: Tactical Intent Recognition
    ↓ (tactical labels: offensive/defensive/neutral, strategic patterns)
Component 4: Subsequent Action Prediction
    ↓ (forecasted stroke type, placement, player movement)
```

Key design principles for the integrated framework:

1. **Error propagation minimization**: Each component should output calibrated confidence scores so that uncertainty propagates appropriately downstream.
2. **Modular extensibility**: Components should be independently replaceable as improved models emerge.
3. **Shared representation**: All components operate on a unified spatiotemporal representation (positions, skeletons, trajectories, stroke events) to avoid redundant processing.
4. **Real-time feasibility**: Where possible, models should be selected for inference speed (TrackNetV3 at 25 FPS; YOLO-family detectors at >30 FPS) to enable live match analysis.

---

## Datasets Summary

| Dataset | Content | Size | Key Features | Reference |
|---------|---------|------|--------------|-----------|
| **ShuttleSet** | Broadcast singles matches (2018–2021) | 44 matches, 104 sets, 3,685 rallies, 36,492 strokes, 27 players | 18 shot types, spatial/temporal/tactical labels | https://ar5iv.labs.arxiv.org/html/2306.04948 |
| **ShuttleSet22** | Split of ShuttleSet | 30,172 train strokes, 1,400 validation, 2,040 test | Benchmark for stroke forecasting | https://arxiv.org/html/2306.15664v1 |
| **VideoBadminton** | Self-recorded footage | 7,822 clips, 18 action classes, 145 min | Player locations + shuttle trajectory annotations | https://arxiv.org/html/2403.12385v2 |
| **BadmintonDB** | Professional men's singles (Momota vs. Ginting) | 9 matches, 811 rallies, 9,671 strokes | 10 shot types per BWF coach guide | https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf |
| **xBHPE** | Dedicated badminton pose dataset | 4,000 annotated samples (Kinect v2) | Domain-specific pose estimation | https://pmc.ncbi.nlm.nih.gov/articles/PMC12298368 |
| **BWF match corpus** | Super750+ international matches (2019–2023) | 303 matches (153 men's, 150 women's) | Technical action frequencies + outcomes | https://www.nature.com/articles/s41598-025-87610-7 |

---

## Open Challenges and Future Directions

1. **Fine-grained action discrimination**: Distinguishing visually similar strokes (e.g., fast drop vs. slow smash, cross-court clear vs. straight clear) remains challenging, with the best models achieving ~83% Top-1 accuracy on 18-class recognition (https://arxiv.org/html/2403.12385v2).
2. **Tactical intent grounding**: Bridging the gap between recognizing *what* action occurs and understanding *why* remains largely open; offline RL and counterfactual analysis offer promising directions (https://www.sciencedirect.com/science/article/abs/pii/S0952197625034268).
3. **Spatial placement prediction**: Area coordinate forecasting lags behind shot type prediction, with most models performing near baseline on placement prediction (https://arxiv.org/html/2306.15664v1).
4. **Cross-domain generalization**: Models trained on one dataset (e.g., broadcast footage) often fail on others (e.g., amateur recordings, different camera angles); recent work on singles-trained models applied to doubles highlights the generalization gap (https://arxiv.org/html/2508.13507v1).
5. **Real-time prediction latency**: Achieving sub-frame prediction for live coaching applications requires lightweight architectures; KNN-HMM at 32ms latency demonstrates feasibility but with accuracy trade-offs (https://link.springer.com/article/10.1186/s40537-026-01396-7).
6. **Multimodal integration**: Combining video analysis with wearable sensor data (IMU-based stroke recognition at 97.16% accuracy) could enhance robustness, though deployment complexity increases (https://www.nature.com/articles/s41598-025-25158-2).
7. **Explainability for coaching**: SHAP-based feature attribution (as demonstrated in the technical action frequency model) and attention visualization in transformers offer paths toward interpretable tactical analysis that coaches can act upon (https://www.nature.com/articles/s41598-025-87610-7).

---

## References

1. Chen, Y.-J., & Wang, Y.-S. (2023). TrackNetV3: Enhancing Shuttlecock Tracking with Augmentations and Trajectory Rectification. ACM Multimedia Asia. https://dl.acm.org/doi/abs/10.1145/3595916.3626370

2. TrackNetV3 Official Implementation. https://github.com/qaz812345/TrackNetV3

3. Sun, N.-E., Lin, Y.-C., Chuang, S.-P., Hsu, T.-H., Yu, D.-R., Chung, H.-Y., & Ik, T.-U. (2020). TrackNetV2: Efficient Shuttlecock Tracking Network. ICPAI 2020. https://scholar.nycu.edu.tw/en/publications/tracknetv2-efficient-shuttlecock-tracking-network

4. Huang, Y.-H., et al. (2019). TrackNet: A Deep Learning Network for Tracking High-Speed and Tiny Objects in Sports Applications. https://dr.lib.iastate.edu/bitstreams/24171391-e255-411c-8c4e-0d0e3d7c0953/download

5. Wu, Y., et al. (2025). Enhanced Pose Estimation for Badminton Players via Improved YOLOv8-Pose with Efficient Local Attention. PMC. https://pmc.ncbi.nlm.nih.gov/articles/PMC12298368

6. Su, Y., & Liu, Z. (2018). Position Detection for Badminton Tactical Analysis based on Multi-person Pose Estimation. IEEE. https://www.semanticscholar.org/paper/Position-Detection-for-Badminton-Tactical-Analysis-Su-Liu/6fed1746570e4022b9b6ac707ec9bb66ecc5a8db

7. Zhang, Y., et al. (2024). Enhancing Badminton Game Analysis: An Approach to Shot Refinement via a Fusion of Shuttlecock Tracking and Hit Detection from Monocular Camera. Sensors, 24(13), 4372. https://www.mdpi.com/1424-8220/24/13/4372

8. Wang, W.-Y., et al. (2023). ShuttleSet: A Human-Annotated Stroke-Level Singles Dataset for Badminton Tactical Analysis. KDD 2023. https://ar5iv.labs.arxiv.org/html/2306.04948

9. Wang, W.-Y., et al. (2022). ShuttleNet: Position-Aware Fusion of Rally Progress and Player Styles for Stroke Forecasting in Badminton. AAAI 2022. https://arxiv.org/abs/2112.01044

10. Wang, W.-Y., et al. (2023). ShuttleSet22: Benchmarking Stroke Forecasting with Stroke-Level Badminton Dataset. https://arxiv.org/html/2306.15664v1

11. Ibh, M., Graßhof, S., & Hansen, D. W. (2024). A Stroke of Genius: Predicting the Next Move in Badminton. CVPR 2024 Workshop on Computer Vision in Sports. https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf

12. Chang, et al. (2026). BST: Badminton Stroke-type Transformer for Skeleton-based Action Recognition in Racket Sports. CVPR 2026 Workshop. https://openaccess.thecvf.com/content/CVPR2026W/CVsports/html/Chang_BST_Badminton_Stroke-type_Transformer_for_Skeleton-based_Action_Recognition_in_Racket_CVPRW_2026_paper.html

13. BST Official Implementation. https://github.com/Va6lue/BST-Badminton-Stroke-type-Transformer

14. Benchmarking Badminton Action Recognition with a New Fine-Grained Dataset. arXiv:2403.12385. https://arxiv.org/html/2403.12385v2

15. Ashfaq, F., Jhanjhi, N. Z., & Khan, N. A. (2023). Badminton Player's Shot Prediction Using Deep Learning. In: Innovation and Technology in Sports. Springer. https://www.springerprofessional.de/en/badminton-player-s-shot-prediction-using-deep-learning/25253060

16. Predicting badminton outcomes through machine learning and technical action frequencies. Scientific Reports. https://www.nature.com/articles/s41598-025-87610-7

17. Yuan, H., Wang, Y., Yang, K., & Bin, Y. (2024). Prediction model and technical and tactical decision analysis of women's badminton singles based on machine learning. PLOS ONE, 19(11), e0312801. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0312801

18. Offline reinforcement learning for badminton tactical decision-making. Engineering Applications of Artificial Intelligence. https://www.sciencedirect.com/science/article/abs/pii/S0952197625034268

19. Kim, J. (2023). AI-powered Badminton Video Detection: Enhancing Gameplay Analysis and Training. TechRxiv. https://www.techrxiv.org/doi/full/10.36227/techrxiv.23708325.v2

20. Zhang, et al. (2024). Deep learning neural network-assisted badminton movement recognition and physical fitness training optimization. Heliyon. https://www.sciencedirect.com/science/article/pii/S2405844024148967

21. Rahmad, N. A., Sufri, N. A. J., As'ari, M. A., & Azaman, A. (2019). Recognition of Badminton Action Using Convolutional Neural Network. IJEEI, 7(4), 750–756. https://www.semanticscholar.org/paper/Recognition-of-Badminton-Action-Using-Convolutional-Rahmad-Sufri/fab4f2e98a08f588f931a4e5c93885ba612c305d

22. An Action Recognition Technology for Badminton Players Using Deep Learning. (2022). Wiley. https://onlinelibrary.wiley.com/doi/10.1155/2022/3413584

23. Li, Y., Feng, Y., Wang, X., & Lu, G. (2026). Deep learning-based badminton action recognition and quality assessment. Sage Journals. https://journals.sagepub.com/doi/10.1177/1088467X251353444

24. Improving Badminton Action Recognition Using Spatio-Temporal Analysis and a Weighted Ensemble Learning Model. CMC. https://www.techscience.com/cmc/v81n2/58683

25. Purnama, B., Erfianto, B., & Wirawan, I. R. (2024). Time Series Classification of Badminton Pose using LSTM with Landmark Tracking. JEEEMI, 7(1), 27–37. https://jeeemi.org/index.php/jeeemi/article/view/488

26. Badminton Shot Recognition with LSTM Network. Springer. https://link.springer.com/chapter/10.1007/978-3-031-60935-0_28

27. Wearable sensing for badminton stroke recognition with one-dimensional convolutional neural network. Scientific Reports. https://www.nature.com/articles/s41598-025-25158-2

28. The analysis of motion recognition model for badminton player movements using machine learning. Scientific Reports. https://www.nature.com/articles/s41598-025-02771-9

29. Future Prediction of Shuttlecock Trajectory in Badminton Using Player's Information. PMC. https://pmc.ncbi.nlm.nih.gov/articles/PMC10219238

30. A study on badminton smash return prediction simulation based on neural networks. SPIE. https://ui.adsabs.harvard.edu/abs/2023SPIE12592E..1LK/abstract

31. Real-time stroke prediction in badminton integrating AI with the KNN-HMM model. Journal of Big Data. https://link.springer.com/article/10.1186/s40537-026-01396-7

32. Shuttle trajectory reconstruction from monocular badminton video. CVPR 2022. https://cs.stanford.edu/people/paulliu/files/cvpr-2022.pdf

33. Bridging the Gap: Doubles Badminton Analysis with Singles-Trained Models. arXiv:2508.13507. https://arxiv.org/html/2508.13507v1

34. CoachAI: AI for Sports. https://inoliao.github.io/CoachAI

35. AI coach for badminton. arXiv:2403.08956. https://arxiv.org/pdf/2403.08956

36. Spyrosoft. Instant review system for badminton: computer vision system use case. https://spyro-soft.com/blog/artificial-intelligence-machine-learning/instant-review-system-for-badminton-computer-vision-use-case

37. Detecting the shuttlecock for a badminton robot: A YOLO based approach. Expert Systems with Applications. https://www.sciencedirect.com/science/article/abs/pii/S0957417420306436

38. Shuttlecock Detection Algorithm for Badminton Video based on Active Learning. IEEE. https://ieeexplore.ieee.org/iel8/11194313/11194318/11194356.pdf

39. Mithilesh Gau. OpenPose Analysis for Badminton Player Movement. https://github.com/mithileshgau/Openpose-Analysis

40. Badminton players detection dataset. Roboflow. https://universe.roboflow.com/hongy20/badminton-players-detection-gwgb1

41. A Real-Time Deep Learning Approach to Badminton Player Positioning and Movement Tracking. National Central University. https://scholars.ncu.edu.tw/en/publications/a-real-time-deep-learning-approach-to-badminton-player-positionin

42. A deep learning based framework for badminton rally outcome prediction. ISPACS 2022. https://ui.adsabs.harvard.edu/abs/2022spcs.conf...25T/abstract

43. Ding, N., Takeda, K., & Fujii, K. (2022). Deep reinforcement learning in a racket sport for player evaluation with technical and tactical contexts. IEEE Access, 10, 54764–54772. https://www.nature.com/articles/s41598-025-87610-7

44. Chu, X., et al. (2022). TIVEE: Visual exploration and explanation of badminton tactics in immersive visualizations. IEEE TVCG, 28(1), 118–128. https://www.nature.com/articles/s41598-025-87610-7

45. Shuttlecock Tracking and Player Service Fault Detection. Jaypee University. http://www.ir.juit.ac.in:8080/jspui/bitstream/123456789/11333/1/Shuttlecock%20Tracking%20and%20Player%20Service%20Fault%20Detection.pdf

46. Toan Nguyen Khanh. Badminton-Analysis: Computer vision for player and shuttlecock detection. GitHub. https://github.com/ToanNguyenKhanh/Badminton-Analysis

47. Purnama, B., et al. Enhanced Badminton Stroke Recognition Using Hybrid RGB–Skeleton Features and Ensemble Learning. ETASR. https://www.etasr.com/index.php/ETASR/article/view/15586

48. From Motion to Rally: Deep Learning for Badminton Video Analysis. Monash University Thesis. https://bridges.monash.edu/articles/thesis/From_Motion_to_Rally_Deep_Learning_for_Badminton_Video_Analysis/32674761

49. See, S. Y. (2025). A Comparative Analysis of Deep Learning Models and Gradient Computation for Rally Detection in Badminton Videos. SN Computer Science. https://dl.acm.org/doi/abs/10.1007/s42979-025-03935-0

50. ShuttleNet Official Implementation. https://github.com/wywyWang/ShuttleNet

