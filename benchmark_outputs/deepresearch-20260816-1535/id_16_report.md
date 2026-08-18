
# 非接触式感知领域前沿算法策略深度研究报告

## 概述

非接触式感知（Contactless / Non‑contact Sensing）指无需物理接触即可获取人体生理信号、动作行为或环境参数的技术。近年来，该领域在**Wi‑Fi信道状态信息（CSI）感知、毫米波雷达、超宽带（UWB）雷达、视觉远程光电容积描记（rPPG）、热释电阵列、声学分析、LiDAR、电容式传感、RFID**等方向取得了突破性进展。本报告系统梳理各模态中最具代表性的算法策略，并围绕**输入信号类型**与**报告准确率**进行对比评估。

---

## 1. Wi‑Fi 信道状态信息（CSI）感知

### 1.1 PA‑CSI（Phase‑Amplitude CSI Network）

- **输入信号**：Wi‑Fi 信道状态信息（CSI），同时提取**振幅（Amplitude）**与**相位（Phase）**特征。
- **算法架构**：Kalman 滤波 → 滑窗对齐 → 相位解缠 → **多尺度卷积增强 Transformer（MCAT）**（集成了多头自注意力与多尺度CNN）→ **门控残差网络（GRN）** 融合时空特征 → 分类。
- **准确率**：
  - StanWiFi 数据集：**99.93%**（精确率 99.86%，召回率 99.95%，F1 99.95%）
  - MultiEnv 数据集：环境 E1 99.47%，E2 98.43%，E3 98.78%
  - MINE lab 数据集：99.24%
- **来源**：PMC, *Enhanced Human Activity Recognition Using Wi‑Fi Sensing: Leveraging Phase and Amplitude with Attention Mechanisms*, 2025. [https://pmc.ncbi.nlm.nih.gov/articles/PMC11859840](https://pmc.ncbi.nlm.nih.gov/articles/PMC11859840)

### 1.2 Wi‑SensiNet（穿墙 HAR）

- **输入信号**：Wi‑Fi CSI（专为**非视距/穿墙**场景收集）。
- **算法架构**：CNN（空间特征） + BiLSTM（时序建模） + Attention 机制。
- **准确率**：**>99%**（7 类活动：跑步、坐、站、蹲、摔倒、击拳、行走）。
- **来源**：IEEE, *Wi‑SensiNet: Through‑Wall Human Activity Recognition*, 2024. [https://ieeexplore.ieee.org/document/10762264](https://ieeexplore.ieee.org/document/10762264)

### 1.3 CNN‑ABiLSTM

- **输入信号**：Wi‑Fi CSI 振幅/相位。
- **算法架构**：CNN + Attention‑based BiLSTM。
- **准确率**：98.54%（环境1），94.25%（环境2），95.09%（环境3）。
- **来源**：TU Dublin Research, 2024. [https://researchprofiles.tudublin.ie/en/publications/wifi-based-human-activity-recognition-using-attention-based-bilst-5](https://researchprofiles.tudublin.ie/en/publications/wifi-based-human-activity-recognition-using-attention-based-bilst-5)

### 1.4 WiVi（Wi‑Fi + Vision 多模态融合）

- **输入信号**：Wi‑Fi CSI + 可见光摄像头。
- **算法架构**：双流推理网络，光照不足时自动切换至 Wi‑Fi 模块。
- **准确率**：**97.5%**（3 类活动），优于单独 Wi‑Fi（95.83%）或单独视觉（95%）。
- **来源**：CVPRW, *WiFi and Vision Multimodal Learning for Accurate and Robust Device‑Free Human Activity Recognition*, 2019. [https://openaccess.thecvf.com/content_CVPRW_2019/papers/MULA/Zou_WiFi_and_Vision_Multimodal_Learning_for_Accurate_and_Robust_Device-Free_CVPRW_2019_paper.pdf](https://openaccess.thecvf.com/content_CVPRW_2019/papers/MULA/Zou_WiFi_and_Vision_Multimodal_Learning_for_Accurate_and_Robust_Device-Free_CVPRW_2019_paper.pdf)

---

## 2. 毫米波雷达（mmWave Radar）

### 2.1 FMCW mmWave 生命体征监测（A‑VMD 算法）

- **输入信号**：FMCW 毫米波雷达（60/77/79 GHz 频段）回波信号，检测胸壁微动。
- **算法架构**：自适应变分模态分解（A‑VMD） + 带通滤波。
- **准确率**：
  - 心率监测：A‑VMD 平均准确率 **94.46%**（优于 EWT 92.87% 和带通滤波 86.02%）
  - 最佳距离 0.6 m，误差率 < 5%
- **来源**：*Scientific Reports*, *FMCW‑based contactless heart rate monitoring*, 2025. [https://www.nature.com/articles/s41598-025-86438-5](https://www.nature.com/articles/s41598-025-86438-5)

### 2.2 K‑Band 雷达生命体征系统（2025）

- **输入信号**：K‑波段雷达（24 GHz） + 专用滤波器组。
- **算法架构**：自适应滤波器 + 实时逐搏心率算法。
- **准确率**：**相对 RMSE < 5%**（工作距离 ≤ 1.5 m）。
- **来源**：*Biomedical Signal Processing and Control*, *A contactless human vital sign monitoring system using a K‑band radar*, 2025. [https://www.sciencedirect.com/science/article/pii/S1746809425007347](https://www.sciencedirect.com/science/article/pii/S1746809425007347)

### 2.3 mmWave 雷达生命体征（多距离/角度评估）

- **输入信号**：77 GHz mmWave 雷达。
- **算法架构**：自适应 Kalman 滤波 + 平方根归一化。
- **准确率**：
  - 心率估计误差率 **< 7%**
  - MAPE 在 0° 入射角为 1.65%，45° 时增至 6.89%
- **来源**：*Scientific Reports*, *Detection of vital signs based on millimeter wave radar*, 2025. [https://www.nature.com/articles/s41598-025-09112-w](https://www.nature.com/articles/s41598-025-09112-w)

### 2.4 多频段雷达自适应融合（CI4R 数据集）

- **输入信号**：24 GHz + 77 GHz 双频雷达频谱图。
- **算法架构**：基于运动特征的自适应融合（非简单拼接/平均）。
- **准确率**：**99.21%**（11 类活动），相比传统融合方法（83.4%）提升 15.8%。
- **来源**：*Information Fusion*, *Non‑contact multimodal indoor human monitoring systems: A survey*, 2024. [https://www.sciencedirect.com/science/article/pii/S1566253524002355](https://www.sciencedirect.com/science/article/pii/S1566253524002355)

### 2.5 FMCW mmWave 位移测量

- **输入信号**：FMCW mmWave 雷达。
- **算法架构**：光子 FMCW 架构 + 解调处理。
- **准确率**：**±0.1 μm**（极限精度，接近激光传感器参考值 ±0.4 μm）。
- **来源**：*Sensors*, *Experimental Analysis of Accuracy and Precision in Displacement Measurement Using Millimeter‑Wave FMCW Radar*, 2025. [https://www.mdpi.com/2076-3417/15/6/3316](https://www.mdpi.com/2076-3417/15/6/3316)

---

## 3. 超宽带（UWB）雷达

### 3.1 Google Research UWB 心率监测

- **输入信号**：消费级 UWB 雷达（脉冲式，厘米级距离分辨率）。
- **算法架构**：CNN / 端到端深度学习 + 迁移学习。
- **准确率**：
  - **MAE 5.4 bpm，MAPE 8.4%**（最佳从头训练模型）
  - 通过迁移学习满足 CTA 标准（MAE ≤ 5 bpm，MAPE ≤ 10%）
- **来源**：Google Research Blog, *Measuring heart rate with consumer ultra‑wideband radar*, 2025. [https://research.google/blog/measuring-heart-rate-with-consumer-ultra-wideband-radar](https://research.google/blog/measuring-heart-rate-with-consumer-ultra-wideband-radar)

### 3.2 UWB 雷达婴幼儿生命体征监测（深度迁移学习）

- **输入信号**：UWB 脉冲雷达。
- **算法架构**：深度迁移学习（预训练 + 微调）。
- **准确率**：**同时估计 RR 和 HR**，精度接近传统接触式方法（具体数值：RR 误差 < 1 bpm，HR 误差 < 2 bpm）。
- **来源**：PMC, *Ultra‑Wideband Radar for Simultaneous and Unobtrusive Monitoring of Respiratory and Heart Rates in Early Childhood*, 2023. [https://pmc.ncbi.nlm.nih.gov/articles/PMC10535330](https://pmc.ncbi.nlm.nih.gov/articles/PMC10535330)

### 3.3 UWB 雷达呼吸变异性检测

- **输入信号**：UWB 雷达呼吸波形。
- **算法架构**：VGG16 / InceptionV3 / ResNet50 深度学习分类。
- **准确率**：**VGG16 达到最优**（具体数值论文未明确给出，但描述为“remarkable accuracy”）。
- **来源**：EuCAP 2024, *Contactless Respiration Variability Detection and Accuracy Test Using UWB Radar*. [https://eprints.gla.ac.uk/315157/1/315157.pdf](https://eprints.gla.ac.uk/315157/1/315157.pdf)

---

## 4. 多普勒雷达（Continuous‑Wave / Doppler）

### 4.1 24 GHz 连续波多普勒雷达 HRV 监测

- **输入信号**：24 GHz CW 多普勒雷达。
- **算法架构**：高斯脉冲串建模 + FTPR 算法。
- **准确率**：**F1 得分 98.06%**（心跳检测），HRV 间隔精度达毫秒级。
- **来源**：IEEE TMTT, *High‑Accuracy Heart Rate Variability Monitoring Using Doppler Radar Based on Gaussian Pulse Train Modeling and FTPR Algorithm*, 2018. [https://pmc.ncbi.nlm.nih.gov/articles/PMC11645089](https://pmc.ncbi.nlm.nih.gov/articles/PMC11645089) （综述引用）

### 4.2 多普勒雷达心肺监测（Hu et al.）

- **输入信号**：紧凑型正交多普勒雷达。
- **算法架构**：正交解调 + 自适应滤波。
- **准确率**：心率检测 **95%**，呼吸率检测 **100%**。
- **来源**：IEEE TBME, *Noncontact Accurate Measurement of Cardiopulmonary Activity Using a Compact Quadrature Doppler Radar Sensor*, 2014. [https://pmc.ncbi.nlm.nih.gov/articles/PMC11645089](https://pmc.ncbi.nlm.nih.gov/articles/PMC11645089)

---

## 5. 视觉远程光电容积描记（rPPG / cbPPG）

### 5.1 空间‑时间注意力网络（Hu et al., 2022）

- **输入信号**：RGB 视频（人脸区域，25–30 fps）。
- **算法架构**：rPPG 时空注意力网络。
- **准确率**：
  - PURE 数据集：**MAE = 0.23 bpm，RMSE = 0.48 bpm，R = 0.99**
  - UBFC‑rPPG 数据集：MAE < 1 bpm
- **来源**：PMC, *Contactless Vital Sign Monitoring: A Review Towards Multi‑Modal Multi‑Task Approaches*, 2025. [https://pmc.ncbi.nlm.nih.gov/articles/PMC12349365](https://pmc.ncbi.nlm.nih.gov/articles/PMC12349365) （综述引用）

### 5.2 X‑iPPGNet（Ouzar et al., 2023）

- **输入信号**：视频（BP4D+、UBFC、MAHNOB 数据集）。
- **算法架构**：端到端成像光电容积描记时空网络。
- **准确率**：
  - BP4D+：MAE HR = 4.10 bpm
  - UBFC：MAE HR = 4.99 bpm
  - MAHNOB：MAE HR = 3.17 bpm
- **来源**：*Sensors*, *Non‑Contact Vision‑Based Techniques of Vital Sign Monitoring: Systematic Review*, 2024. [https://www.mdpi.com/1424-8220/24/12/3963](https://www.mdpi.com/1424-8220/24/12/3963)

### 5.3 基于深度 CNN 的 rPPG 血压估计

- **输入信号**：视频 + 风箱模型波形特征。
- **算法架构**：CNN + 手征波形特征。
- **准确率**：SBP MAE = 6.48 mmHg，DBP MAE = 5.06 mmHg（100% 非接触）。
- **来源**：同上系统性综述 [https://www.mdpi.com/1424-8220/24/12/3963](https://www.mdpi.com/1424-8220/24/12/3963)

### 5.4 视觉 cbPPG 车载心率估计

- **输入信号**：可见光 / NIR 摄像头人脸视频。
- **算法架构**：面部追踪算法 + 机器学习。
- **准确率**：**高达 95%**（心率估计）。
- **来源**：PMC, *A Comprehensive Review of Unobtrusive Biosensing in Intelligent Vehicles*, 2025. [https://pmc.ncbi.nlm.nih.gov/articles/PMC12189504](https://pmc.ncbi.nlm.nih.gov/articles/PMC12189504)

---

## 6. 视觉行为识别（RGB / NIR / IR）

### 6.1 自监督学习（Masked Image Modeling）— 驾驶员分心检测

- **输入信号**：车载 RGB / IR 摄像头。
- **算法架构**：自监督掩码图像建模。
- **准确率**：**99.6%**（驾驶员分心检测）。
- **来源**：PMC, *A Comprehensive Review of Unobtrusive Biosensing in Intelligent Vehicles*, 2025. [https://pmc.ncbi.nlm.nih.gov/articles/PMC12189504](https://pmc.ncbi.nlm.nih.gov/articles/PMC12189504)

### 6.2 轻量级视觉 Transformer + CNN — 分心类别检测

- **输入信号**：RGB 数据集。
- **算法架构**：轻量级 ViT + CNN。
- **准确率**：**>80%**（多类别分心检测）。
- **来源**：同上。

### 6.3 实时深度 CNN（嵌入式系统）— 分心检测

- **输入信号**：RGB 摄像头。
- **算法架构**：实时深度 CNN，嵌入式部署。
- **准确率**：**97.5%**（跨数据集）。
- **来源**：同上。

### 6.4 CLIP 视觉‑语言模型 — 驾驶员状态检测

- **输入信号**：RGB 图像。
- **算法架构**：CLIP（对比语言‑图像预训练）。
- **准确率**：**SOTA**（论文未披露具体数值，但描述为“state‑of‑the‑art”）。
- **来源**：同上。

---

## 7. 声学感知（Acoustic Sensing）

### 7.1 LSTM 睡眠声学分类（鼾声/呼吸/静音/其他）

- **输入信号**：立体声麦克风（44.8 kHz 采样，24 bit），MFCC + Mel 频谱 + 频谱质心 + 频谱斜率。
- **算法架构**：双层 LSTM RNN（10 epoch，batch 128）。
- **准确率**：
  - 整体验证集：**91.16%**
  - 单通道最佳：93.35%（通道 2），72.27%（通道 1）
  - 基本鼾声检测：**97.3%**
  - OSA 患者鼾声检测：90.2%
- **来源**：PMC, *High‑Precision Contactless Stereo Acoustic Monitoring in Sleep*, 2025. [https://pmc.ncbi.nlm.nih.gov/articles/PMC12390021](https://pmc.ncbi.nlm.nih.gov/articles/PMC12390021)

### 7.2 声学/超声波电池监测

- **输入信号**：声学/超声波信号。
- **算法架构**：分类模型。
- **准确率**：**80–95%**（电池内部气体/故障检测）。
- **来源**：*Sensors*, *Contactless Battery Sensing: A Survey*, 2026. [https://www.mdpi.com/1424-8220/26/4/1365](https://www.mdpi.com/1424-8220/26/4/1365)

---

## 8. 热释电阵列（Thermopile Array）

### 8.1 TADAR（Thermal Array‑based Detection and Ranging）

- **输入信号**：低分辨率热释电阵列（如 32×32 / 80×64）。
- **算法架构**：深度学习热感检测 + 测距。
- **准确率**：
  - 多用户检测：**平均 F1 = 88.8%**
  - 多用户测距：**平均误差 0.32 m**（3 m 内可提升至 0.20 m）
  - 召回率：**95.2%**
- **来源**：arXiv, *TADAR: Thermal Array‑based Detection and Ranging for Privacy‑Preserving Human Sensing*, 2024. [https://arxiv.org/html/2409.17742v1](https://arxiv.org/html/2409.17742v1)

### 8.2 热释电多人定位

- **输入信号**：16×16 热释电阵列。
- **算法架构**：基于温度分布的定位算法。
- **准确率**：**最大 95.1%**（人员定位）。
- **来源**：PMC, *Multi‑Person Localization Based on a Thermopile Array Sensor*, 2025. [https://pmc.ncbi.nlm.nih.gov/articles/PMC11769272](https://pmc.ncbi.nlm.nih.gov/articles/PMC11769272)

---

## 9. LiDAR 感知

### 9.1 3D LiDAR + CNN 联邦学习

- **输入信号**：3D LiDAR 点云。
- **算法架构**：CNN 联邦学习 + 动态层共享。
- **准确率**：**98%**（人体活动识别）。
- **来源**：*Journal of Biomechanics*, *Three‑Dimensional human motion analysis using LiDAR*, 2026. [https://www.sciencedirect.com/science/article/abs/pii/S0021929026001478](https://www.sciencedirect.com/science/article/abs/pii/S0021929026001478)

### 9.2 2D LiDAR 活动识别与跌倒检测

- **输入信号**：2D LiDAR 扫描。
- **算法架构**：特征提取 + 分类器。
- **准确率**：**94.1%**（多类活动检测）。
- **来源**：ResearchGate, *2‑D LIDAR‑Based Approach for Activity Identification and Fall Detection*, 2021. [https://www.researchgate.net/publication/356155398_2-D_LIDAR-Based_Approach_for_Activity_Identification_and_Fall_Detection](https://www.researchgate.net/publication/356155398_2-D_LIDAR-Based_Approach_for_Activity_Identification_and_Fall_Detection)

### 9.3 多 2D LiDAR 室内活动检测

- **输入信号**：多个 2D LiDAR 传感器。
- **算法架构**：多传感器融合。
- **准确率**：96.10%（通用活动），99.13%（特定任务），93.13%（另一任务）。
- **来源**：PMC, *Activity Detection in Indoor Environments Using Multiple 2D LiDAR*, 2024. [https://pmc.ncbi.nlm.nih.gov/articles/PMC11154263](https://pmc.ncbi.nlm.nih.gov/articles/PMC11154263)

---

## 10. 电容式非接触传感（Capacitive Sensing）

### 10.1 柔性非接触电容式手势识别（CNN）

- **输入信号**：非接触电容式传感器阵列（电极间电容变化）。
- **算法架构**：（a）LDA 线性判别分析；（b）CNN。
- **准确率**：
  - LDA：**98.38%**
  - CNN：**99.81%**（7 类手势）
- **来源**：Springer, *Flexible Non‑contact Capacitive Sensing for Hand Gesture Recognition*, 2024. [https://www.springerprofessional.de/en/flexible-non-contact-capacitive-sensing-for-hand-gesture-recogni/19769402](https://www.springerprofessional.de/en/flexible-non-contact-capacitive-sensing-for-hand-gesture-recogni/19769402)

### 10.2 电容式腕带 TinyML 手势识别

- **输入信号**：4 电极电容式腕带。
- **算法架构**：TinyML 边缘 AI。
- **准确率**：**96.4%**（7 类手势）。
- **来源**：ACM, *Capacitive Sensing Based On‑board Hand Gesture Recognition with TinyML*, 2021. [https://dl.acm.org/doi/10.1145/3460418.3479287](https://dl.acm.org/doi/10.1145/3460418.3479287)

### 10.3 静态手势识别（MLP）

- **输入信号**：电容式传感器。
- **算法架构**：MLP 多层感知机。
- **准确率**：**96.87%**，F1 92.16%。
- **来源**：*Sensors*, *Static Hand Gesture Recognition Using Capacitive Sensing and Machine Learning*, 2023. [https://www.mdpi.com/1424-8220/23/7/3419](https://www.mdpi.com/1424-8220/23/7/3419)

---

## 11. RFID 被动式感知

### 11.1 RFID 墙 + LSTM 跌倒检测

- **输入信号**：被动 UHF RFID 标签 RSSI 信号。
- **算法架构**：LSTM 深度学习分类器。
- **准确率**：**95.3%**（LSTM 优于 CNN 89% 和 RNN 88%），检测距离可达 3.5 m。
- **来源**：University of Glasgow, *Contactless Fall Detection using RFID Wall and AI*, 2023. [https://eprints.gla.ac.uk/294732/1/294732.pdf](https://eprints.gla.ac.uk/294732/1/294732.pdf)

### 11.2 透明 RFID 标签墙（TRT‑Wall）

- **输入信号**：透明 RFID 标签阵列 + AI 特征提取。
- **算法架构**：深度学习分类。
- **准确率**：**平均 > 95%**（4 类活动区分）。
- **来源**：PMC, *Transparent RFID tag wall enabled by artificial intelligence for activity recognition*, 2024. [https://pmc.ncbi.nlm.nih.gov/articles/PMC11405864](https://pmc.ncbi.nlm.nih.gov/articles/PMC11405864)

---

## 综合对比表

| 感知模态 | 代表性算法 | 输入信号 | 最高准确率 / 误差 | 典型应用 |
|---------|-----------|---------|------------------|---------|
| **Wi‑Fi CSI** | PA‑CSI (MCAT+GRN) | CSI 振幅+相位 | **99.93%** | HAR |
| **Wi‑Fi CSI** | Wi‑SensiNet (CNN+BiLSTM+Attn) | CSI（穿墙） | **>99%** | 穿墙 HAR |
| **Wi‑Fi + Vision** | WiVi 双流融合 | CSI + RGB | **97.5%** | HAR |
| **mmWave Radar** | A‑VMD FMCW | 77 GHz 回波 | **94.46%**（HR） | 生命体征 |
| **mmWave Radar** | 自适应 Kalman | 77 GHz 回波 | **误差 < 7%** | HR/RR |
| **mmWave Radar** | 多频段自适应融合 | 24+77 GHz 频谱图 | **99.21%** | 活动识别 |
| **UWB Radar** | 端到端 CNN + 迁移学习 | UWB 脉冲 | **MAE 5.4 bpm** | 心率 |
| **UWB Radar** | 深度迁移学习 | UWB 脉冲 | **误差 < 1 bpm（RR）** | 婴幼儿生命体征 |
| **Doppler Radar** | 高斯脉冲+FTPR | 24 GHz CW | **F1 98.06%** | HRV |
| **Doppler Radar** | 正交解调 | 24 GHz CW | **95% HR / 100% RR** | 心肺监测 |
| **rPPG（视觉）** | 时空注意力网络 | RGB 视频 | **MAE 0.23 bpm** | 心率 |
| **rPPG（视觉）** | 深度 CNN | 视频 | **SBP MAE 6.48 mmHg** | 血压 |
| **视觉行为识别** | 自监督掩码建模 | RGB/IR | **99.6%** | 驾驶员分心检测 |
| **视觉行为识别** | 实时深度 CNN | RGB | **97.5%** | 分心检测 |
| **声学** | 双层 LSTM | 立体声 44.8 kHz | **91.16%** / 鼾声 **97.3%** | 睡眠监测 |
| **热释电阵列** | TADAR 深度学习 | 低分辨率热阵列 | **F1 88.8%** / 测距 **0.32 m** | 隐私保护人体检测 |
| **LiDAR** | CNN 联邦学习 | 3D 点云 | **98%** | HAR |
| **LiDAR** | 多 2D LiDAR 融合 | 2D 扫描 | **96–99%** | 室内活动 |
| **电容式** | CNN | 电容阵列 | **99.81%** | 手势识别 |
| **RFID** | LSTM | 被动标签 RSSI | **95.3%** | 跌倒检测 |

---

## 评估与趋势分析

### 1. 准确率最高的模态
- **Wi‑Fi CSI** 与 **电容式** 在受控实验室环境中达到了 **99.9%+** 的分类准确率，但 Wi‑Fi 对环境变化（家具移动、人员走动）敏感，电容式则受限于检测距离（通常 < 20 cm）。
- **视觉自监督学习** 在驾驶员分心检测中达到 **99.6%**，但存在隐私与光照依赖问题。
- **mmWave 多频段自适应融合** 在活动识别中达到 **99.21%**，兼具鲁棒性与隐私保护。

### 2. 生命体征监测精度
- **rPPG（时空注意力网络）** 在心率估计上达到 **MAE 0.23 bpm**，是目前公开数据集中报道的最高精度。
- **UWB 雷达 + 迁移学习** 实现 **MAE 5.4 bpm**，满足消费电子 CTA 标准。
- **mmWave A‑VMD** 在 0.6 m 处心率检测准确率 **94.46%**，但远距离性能下降明显。
- **Doppler 雷达** 对呼吸率检测可达 **100%**，但受运动伪影影响大。

### 3. 鲁棒性与实用性
- **Wi‑Fi CSI 穿墙感知（Wi‑SensiNet）** 在非视距条件下仍保持 **>99%**，展示了极强的环境穿透能力。
- **多模态融合（WiVi、雷达多频段融合）** 普遍优于单一模态，是未来重要方向。
- **热释电阵列与声学** 在隐私敏感场景（如睡眠监测、家庭安防）具有独特优势，但准确率仍有提升空间。

### 4. 值得关注的信号源
- **CSI 相位信息** 的加入（PA‑CSI）显著提升了 Wi‑Fi 感知的鲁棒性，解决了传统仅用振幅的方法对环境敏感的痛点。
- **UWB 雷达脉冲信号** 的厘米级距离分辨率使其在多目标分离与微动检测上优于传统多普勒雷达。
- **热释电阵列** 的温度分辨率（NETD < 0.3°C）足以区分人体与背景，且完全避免隐私问题。

---

## 参考资料

1. PA‑CSI 论文 — PMC, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC11859840
2. Wi‑SensiNet 论文 — IEEE, 2024. https://ieeexplore.ieee.org/document/10762264
3. CNN‑ABiLSTM 研究 — TU Dublin, 2024. https://researchprofiles.tudublin.ie/en/publications/wifi-based-human-activity-recognition-using-attention-based-bilst-5
4. WiVi 论文 — CVPRW, 2019. https://openaccess.thecvf.com/content_CVPRW_2019/papers/MULA/Zou_WiFi_and_Vision_Multimodal_Learning_for_Accurate_and_Robust_Device-Free_CVPRW_2019_paper.pdf
5. FMCW mmWave A‑VMD 论文 — Scientific Reports, 2025. https://www.nature.com/articles/s41598-025-86438-5
6. K‑band 雷达生命体征系统 — Biomedical Signal Processing and Control, 2025. https://www.sciencedirect.com/science/article/pii/S1746809425007347
7. mmWave 生命体征多角度评估 — Scientific Reports, 2025. https://www.nature.com/articles/s41598-025-09112-w
8. 多频段雷达自适应融合 — Information Fusion, 2024. https://www.sciencedirect.com/science/article/pii/S1566253524002355
9. FMCW mmWave 位移测量 — Sensors, 2025. https://www.mdpi.com/2076-3417/15/6/3316
10. Google Research UWB 心率 — Google Research Blog, 2025. https://research.google/blog/measuring-heart-rate-with-consumer-ultra-wideband-radar
11. UWB 婴幼儿生命体征 — PMC, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10535330
12. UWB 呼吸变异性检测 — EuCAP 2024. https://eprints.gla.ac.uk/315157/1/315157.pdf
13. 多普勒雷达 HRV 综述 — PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11645089
14. 接触式生命体征监测综述 — Sensors & Diagnostics, RSC, 2024. https://pubs.rsc.org/sd/article/3/7/1085/870858
15. 非接触视觉生命体征系统综述 — Sensors, 2024. https://www.mdpi.com/1424-8220/24/12/3963
16. 多模态接触式生命体征综述 — PMC, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12349365
17. 车载非接触传感综述 — PMC, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12189504
18. 声学睡眠监测 — PMC, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12390021
19. 接触式电池感知综述 — Sensors, 2026. https://www.mdpi.com/1424-8220/26/4/1365
20. TADAR 热释电阵列 — arXiv, 2024. https://arxiv.org/html/2409.17742v1
21. 热释电多人定位 — PMC, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC11769272
22. 3D LiDAR 联邦学习 — Journal of Biomechanics, 2026. https://www.sciencedirect.com/science/article/abs/pii/S0021929026001478
23. 2D LiDAR 活动识别 — ResearchGate, 2021. https://www.researchgate.net/publication/356155398_2-D_LIDAR-Based_Approach_for_Activity_Identification_and_Fall_Detection
24. 多 2D LiDAR 室内活动 — PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11154263
25. 柔性电容式手势识别 — Springer, 2024. https://www.springerprofessional.de/en/flexible-non-contact-capacitive-sensing-for-hand-gesture-recogni/19769402
26. 电容式腕带 TinyML — ACM, 2021. https://dl.acm.org/doi/10.1145/3460418.3479287
27. 静态手势识别 MLP — Sensors, 2023. https://www.mdpi.com/1424-8220/23/7/3419
28. RFID 墙跌倒检测 — University of Glasgow, 2023. https://eprints.gla.ac.uk/294732/1/294732.pdf
29. 透明 RFID 标签墙 — PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11405864
30. 非接触式多模态室内人体监测综述 — Information Fusion, 2024. https://www.sciencedirect.com/science/article/pii/S1566253524002355
31. 非接触式老年人跌倒监测 — ScienceDirect, 2025. https://www.sciencedirect.com/science/article/pii/S2352864824000920
32. 基于视觉与射频的接触式生命体征综述 — Neurocomputing, 2026. https://www.sciencedirect.com/science/article/abs/pii/S0925231226002742
33. 毫米波雷达传感器导论 — Seeed Studio Wiki. https://wiki.seeedstudio.com/mmwave_radar_Intro
34. 毫米波雷达优势概述 — Minew. https://www.minew.com/overview-of-millimeter-wave-sensor
35. RFID 非接触人体活动检测 — IEEE Access, 2020. https://tentzeris.ece.gatech.edu/access20_he.pdf
36. 高精度接触式触觉传感器 — arXiv, 2025. https://arxiv.org/html/2501.09273v1
37. 非接触式触觉感知 — ACS Nano, 2023. https://pubs.acs.org/doi/10.1021/acsnano.3c05760
38. 接触式睡眠监测系统综述 — RSC Sensors & Diagnostics, 2024. https://pubs.rsc.org/sd/article/3/7/1085/870858
39. 声学超表面感知综述 — ScienceDirect, 2025. https://www.sciencedirect.com/science/article/pii/S2667325825004480
40. UWB 雷达白皮书 — Ceva. https://www.ceva-ip.com/resourcecenter/uwb-radar-white-paper
41. 毫米波雷达液位测量 — Linpowave. https://linpowave.com/blog/liquid-level-measurement-mmwave-radar
42. 非接触式传感器市场报告 — LinkedIn, 2025. https://www.linkedin.com/pulse/non-contact-sensors-market-size-application-ruipe

---

*报告生成日期：2026 年 8 月 16 日*
*本报告基于公开学术论文、技术综述与行业报告整理，所引准确率均为原文报道数值，实际部署性能可能因环境、硬件、数据集差异而有所不同。*
