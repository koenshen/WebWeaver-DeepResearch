

# 大模型模拟药物效应与系统性药物评估：现状与未来展望

## 摘要

传统药物研究，即使借助多组学技术，也难以从系统层面宏观解析药物对机体的整体影响，而个体异质性进一步增加了评估的复杂性。近年来，以大语言模型（LLM）和基础模型（Foundation Model）为代表的人工智能技术，正在深刻变革药物研发范式。本报告系统调研了当前大模型在药物效应模拟、系统性药物评估、多组学整合、个性化用药及数字孪生等方向的应用现状，分析了现有技术的能力边界与核心挑战，并对该领域的未来发展方向进行了前瞻性研判。

---

## 1. 引言：传统药物研究的困境与新范式萌芽

传统药物研发是一个漫长、高成本且高风险的过程，一款新药从靶点发现到上市通常需要超过10年时间，耗费数十亿美元。即使在多组学（基因组学、转录组学、蛋白质组学、代谢组学）技术日益成熟的今天，研究者仍然面临以下核心困境：

- **还原论局限**：传统方法往往聚焦于单一靶点或单一通路，难以捕捉药物在复杂生物网络中的系统性效应。
- **个体异质性**：患者的遗传背景、表观遗传状态、肠道微生物组、环境暴露等因素导致药物反应高度个体化，群体平均数据难以指导精准用药。
- **数据孤岛**：多组学数据、临床数据、文献知识之间缺乏有效整合机制。

大语言模型与基础模型的崛起，为突破这些困境提供了全新的技术路径。这类模型不仅能够理解和生成人类语言，更重要的是，它们正在被训练用于理解生物学的"语言"——DNA序列、基因表达谱、蛋白质结构、分子指纹等，从而实现对药物效应的系统性模拟与预测。

---

## 2. 大模型在药物效应模拟中的核心能力

### 2.1 单细胞基础模型：扰动响应预测

单细胞转录组学技术的成熟使得在单细胞水平上研究药物和基因扰动成为可能。近年来，多个基于Transformer架构的单细胞基础模型相继问世，展现出强大的扰动响应预测能力。

**scGPT** 是首个单细胞基础模型，采用生成式预训练Transformer架构，在来自CELLxGENE Discover的3300万个人类正常细胞转录组上训练，覆盖51个器官/组织、441项独立研究。该模型能够执行多模态计算生物学工作流，包括跨组织细胞类型注释、多批次整合、多组学数据对齐（如scRNA-seq/scATAC-seq共嵌入），以及**体外扰动响应预测**（CRISPRi/化学扰动）[^1]。

**scFoundation**（xTrimoGene）包含1亿参数，在超过5000万个人类单细胞RNA测序数据集上训练，可直接用于药物响应预测、单细胞药物响应分类和扰动预测[^2]。

**Geneformer** 在2800万个单细胞转录组上预训练后，仅使用有限的外部队列（n=1500）即实现了稳健的靶点预测。该模型推荐的mTOR抑制剂依维莫司在实验中显示出显著的功能改善：射血分数增加18.3%，胶原I沉积减少52%，最大线粒体呼吸能力提升37%[^1]。

**关键发现**：然而，独立评估研究（Ahlmann-Eltze et al., 2025; Boiarsky et al., 2024）指出，在扰动预测任务上，深度学习方法**并不总是优于简单的PCA加线性回归基线**。这表明单细胞基础模型在表征学习、批次校正等任务上确实有效，但扰动预测的能力仍需审慎评估[^3][^4]。

### 2.2 语言模型驱动的药物响应预测

大语言模型在药物响应预测中的应用正在快速发展。核心思路是将多组学数据编码为自然语言提示，利用LLM的语义理解能力进行预测。

**DRPLLM**（Drug Response Prediction using Large Language Model）是一个代表性框架，它将Llama-8b大语言模型与深度神经网络回归头结合，将细胞系基因表达、突变和药物属性格式化为自然语言提示并提取嵌入向量。在GDSC v2和CCLE数据集上训练后，该模型达到了0.71的Spearman秩相关系数，超参数优化后提升至0.74。在患者来源异种移植（PDX）队列上的验证表明，嵌入方法（SCC=0.45）显著优于传统提示工程方法（SCC=0.06），展示了LLM在个性化癌症药物响应预测中的潜力[^5]。

**CancerGPT** 展示了LLM在小样本药物协同作用预测中的能力。该模型利用LLM预训练权重中编码的先验知识，在零样本设置下即实现了显著预测精度，在大多数情况下优于XGBoost等传统表格预测模型。这对于数据稀缺的罕见病或新药组合研究具有重要意义[^6]。

### 2.3 多模态框架：整合结构化与无结构化数据

药物效应评估的关键挑战之一是将结构化分子数据与无结构化临床信息（如病历、医学文献、影像报告）进行整合。多模态LLM框架正在成为解决这一问题的有力工具。

在药物响应预测的综述中，研究者指出："多模态LLM框架通过实现跨结构化与非结构化领域的知识驱动建模，进一步扩展了现有范式。这些框架能够捕捉单模态模型遗漏的互补信息，LLM可以整合生物医学文献、临床笔记和分子数据，支持上下文感知的预测和假设生成"[^7]。

在肿瘤学中，多模态LLM智能体系统已展现出可行性，通过融合放射组学、病理学和指南文本，提供个性化治疗推荐[^7]。

---

## 3. 系统性药物评估：从靶点到临床的全链条模拟

### 3.1 药物-靶点相互作用与分子性质预测

基础模型在药物发现早期阶段的应用已经相当成熟：

- **NVIDIA BioNeMo** 平台提供了多种基础模型，包括首个基因组学模型DNABERT（用于预测基因组区域功能、分析基因突变效应），以及小分子基础模型（MoLFormer-XL, Uni-Mol 2, MolMIM等），支持药物候选物生成、ADMET性质预测和合成路线规划[^8]。
- **LFM2-2.6B-MMAI** 是Insilico Medicine与Liquid AI合作开发的轻量级科学基础模型，仅26亿参数即在多个药物发现任务上达到或超越10倍规模系统的性能。该模型可在私有基础设施上运行，全程保护数据隐私[^9]。
- **DiffDock** 等工具可在虚拟环境中预测药物与蛋白质靶点的对接方式，使研究者能在进入体外或体内研究之前测试数百个候选分子[^10]。

### 3.2 药物毒性预测：从单终点到多模态整合

药物毒性是临床试验失败的主要原因之一（约30%的失败源于意外毒性）。AI驱动的毒性预测正在成为标准早期检查点。

2025年，该领域呈现以下趋势：
- **从单终点预测向多模态整合发展**：AI模型正在整合多组学数据、分子结构、临床前和临床数据进行毒性预测[^11]。
- **生成式AI应用于毒性通路预测**：生成模型被用于模拟化学毒性通路，NLP技术被用于从文献中提取毒性数据[^12]。
- **市场快速增长**：AI预测毒理学市场在2025年估值2.8亿美元，预计到2035年将达到22.5亿美元，年复合增长率23.2%[^12]。

前沿进展包括：用于hERG通道阻断预测的模型已达到临床可靠性水平；肝毒性预测仍面临较大挑战，因为其涉及异质性且往往具有个体特异性的生物学机制[^13]。

### 3.3 药物相互作用预测

多药联用（polypharmacy）在临床实践中极为常见，但药物-药物相互作用（DDI）的预测一直是重大挑战。大语言模型在这一领域展现出显著优势：

- LLM在DDI预测任务上的表现与传统方法相当甚至更优。小模型在临床应用中具有显著实用意义，因为其计算资源需求更低[^14]。
- 基于药物-靶点基因关联数据的机器学习框架报告DDI识别准确率约95%[^15]。
- 基于CYP450酶抑制数据的DDI预测模型已达到约80%的准确率，但转运蛋白介导的相互作用和复杂多药组合的预测仍不成熟[^15]。

### 3.4 药代动力学/药效动力学（PK/PD）模拟

PK/PD模型是药物开发的核心工具，描述药物在体内的吸收、分布、代谢、排泄（ADME）过程及其效应。AI正在重塑这一领域：

- **机器学习与生理药代动力学（PBPK）模型的融合**正在成为标准方法。例如，AI-PBPK混合模型已在醛固酮合成酶抑制剂的PK/PD性质预测中得到验证[^16]。
- **Certara**等公司正将ML集成到PK/PD建模软件中，以提高模型开发效率并发现传统方法可能忽视的生物学洞察[^17]。
- 大语言模型被用于自动生成PK/PD建模代码、生成可视化并辅助模型诊断[^18]。

---

## 4. 个体异质性：从群体平均到个性化模拟

### 4.1 数字孪生：个体化药物评估的前沿

数字孪生（Digital Twin）——个体患者的虚拟复制品——代表了药物评估从群体平均向个体化模拟的范式跃迁。

**核心概念**：数字孪生不同于合成患者数据，它通过链接真实患者与其精确的虚拟对应物，实现疾病轨迹预测和药物治疗效果的仿真与模拟。数字孪生模型在大规模异质数据上训练，能够高效学习患者诊断、临床变量和结局之间的复杂关系，从而显著增强个性化预测能力[^19]。

**LLM驱动的数字孪生**：大语言模型预训练在大型生物医学和临床数据语料上，可通过微调生成个体特定的纵向轨迹，标志着新一代数字孪生的诞生。LLM基模型不需要先验数据预处理或整合，可以处理来自不同机构、实验室和患者群体的原始数据。其预训练特性使零样本预测成为可能，模型可以通过训练数据中的模式推断未明确训练过的变量——这对于处理高度异质、稀疏或不完整的数据集尤为重要[^19]。

**应用案例**：
- 在肿瘤学中，"癌症替身"（Cancer Avatar）通过整合影像、组织学和基因组数据，允许临床医生在做出治疗决策前虚拟测试不同的治疗方案[^20]。
- 在脊髓性肌萎缩症（SMA）中，数字孪生已被用于模拟腺相关病毒（AAV）载体的生物分布和免疫原性，并以前瞻性方式与临床试验数据进行了验证[^20]。
- 在心律失常治疗中，约翰霍普金斯大学的基因型特异性心脏孪生项目使用MRI和基因组数据创建患者3D复制品，模拟导管消融可能对个体患者心室颤动回路的影响[^21]。

### 4.2 多组学整合驱动的患者分层

AI驱动的多组学整合从根本上重新配置了药物发现的范式，其核心转变之一是从群体化治疗走向整合个体多组学特征的患者特异性数字孪生模拟[^1]。

**PERCEPTION**（PERsonalized Single-Cell Expression-Based Planning for Treatments in ONcology）是一个精准肿瘤学计算流程，它利用公开可用的匹配批量细胞和单细胞表达谱，预测靶向治疗的反应。在两个涉及多发性骨髓瘤、乳腺癌和肺癌患者的临床试验中，该方法成功预测了患者对靶向治疗的反应[^1]。

**Hu等人**通过共识聚类分析8个AD脑组织数据集和3个血液数据集，揭示了两种分子层面不同的阿尔茨海默病亚型，建立了针对不同亚型的个性化治疗干预框架[^1]。

---

## 5. 当前能力的客观评估与核心挑战

尽管大模型在药物效应模拟中展现出巨大潜力，但独立、系统的评估揭示了其当前能力的边界。

### 5.1 扰动预测：简单基线仍具竞争力

2025年发表在《Nature Methods》上的一项基准研究引发了广泛讨论。研究表明，在预测基因扰动效应的任务中，**简单的线性加性模型（即假设每个基因对扰动的贡献是独立的）反而优于最先进的深度学习方法**。研究者分析认为，部分原因在于实验数据集通常基于基因上同质的癌细胞系，在简化实验室条件下培养，这降低了生物复杂性和变异性，使得简单模型足以捕捉主要的效应模式[^3]。

然而，也有研究显示，在足够大的数据规模和适当模态下，基础模型可以达到接近实验误差极限的性能。Genbio AI的融合模型在Jurkat和K562细胞系中的预测结果与估计的实验误差极限相匹配[^22]。

**综合评判**：单细胞基础模型在表征学习、批次校正、零样本注释等任务上确实有效，但扰动预测的"杀手级应用"尚未到来。该领域需要更大规模、更多样化的扰动数据，以及更精细的评估框架。

### 5.2 大模型的固有局限

LLM应用于药物评估面临以下核心挑战[^19][^23]：

| 挑战 | 说明 |
|------|------|
| **幻觉** | 模型可能生成看似合理但事实上错误的药物效应预测，在高风险医疗场景中不可接受 |
| **数据偏差** | 训练数据可能反映特定人群、特定实验条件，导致对未充分代表群体的预测偏差 |
| **模型漂移** | 随着新药上市、新研究结果发表，模型的知识会逐渐过时，需要持续更新评估 |
| **可解释性** | 深度学习模型（尤其是大型Transformer）的"黑箱"性质使得监管机构难以审查其决策依据 |
| **验证困难** | 在真实的临床试验开展之前，难以确认模型预测的可靠性 |
| **数据隐私** | 患者级多组学数据和临床数据的训练涉及严格的隐私保护要求 |

斯坦福大学的MedHELM（医学大语言模型整体评估）框架强调：仅基于考试式基准（如USMLE）评估临床准备度是不够的，就像仅凭书面交规考试评估驾驶能力——需要涵盖临床推理、患者管理、沟通能力等多维度指标的全面评估[^24]。

---

## 6. 未来发展方向

### 6.1 从单模态到多模态全息整合

未来药物评估模型将从单一数据模态走向多模态深度融合。这包括：
- **分子层**：基因组、转录组、蛋白质组、代谢组、表观基因组
- **细胞层**：单细胞转录组、空间转录组
- **组织器官层**：病理影像、放射组学
- **个体层**：电子健康记录、可穿戴设备数据、生活方式数据
- **群体层**：真实世界证据、临床试验数据

IBM Research的BMFM（生物医学基础模型）技术已开始整合小分子、蛋白质和单细胞RNA-seq数据，采用多模态对齐策略学习跨模态嵌入[^25]。

### 6.2 大型扰动模型（LPM）与虚拟细胞

继单细胞基础模型之后，**大型扰动模型（Large Perturbation Models, LPM）**正在成为下一代药物模拟的核心技术。GSK团队在《Nature Computational Science》上发表的LPM采用不同于传统相关性学习的策略，直接在跨细胞类型、跨条件的CRISPR扰动数据上训练，旨在预测尚未在实验中被测试过的生物学效应[^4]。

**虚拟细胞（Virtual Cell）**的概念正在从科幻走向现实：用AI模拟完整细胞内的所有生物学过程，包括基因调控、代谢通路、信号转导，以及药物干预对这些网络的扰动。这将使药物效应模拟从"预测某个终点"进化为"模拟整个生物学过程"。

### 6.3 临床整合：从辅助工具到临床决策核心

未来5-10年的关键演进路径[^19][^26]：

**短期（1-3年）**：
- 扩大来自多样化患者群体的深度分子谱数据集
- 完善生成式AI的鲁棒性和法规合规性
- 推进用户教育和伦理指南建设

**中长期（3-10年）**：
- 生成式AI将成为临床实践的基础组成部分，在"临床医生在环"（clinician-in-the-loop）框架下常规支持患者特异性治疗决策
- AI驱动的数字孪生将实现从药物发现到临床用药的全链条个性化
- 监管框架（如FDA 2025年发布的AI辅助药物开发指南）将逐步成熟，为AI药物评估提供标准化路径[^27]

### 6.4 基础模型数量爆发与整合需求

Delile等人（2025）的综述显示，自2022年以来，药物发现领域的基础模型数量呈爆发式增长，迄今已发表超过200个模型，涵盖靶点发现、分子性质优化、临床前应用等多个领域[^28]。然而，这种繁荣也带来了新的挑战：如何选择、评估和整合这些模型？行业内正在形成共识，需要建立统一的评估基准和互操作性标准。

---

## 7. 结论

大模型正在从根本上改变药物效应评估的范式——从还原论向系统论跃迁，从群体平均向个体化模拟演进，从单一数据模态向多模态整合深化。具体而言：

1. **当前已具备的能力**：单细胞基础模型可以预测基因扰动和药物处理的转录组响应；LLM驱动的框架（如DRPLLM）能够整合多组学数据预测药物响应；AI毒性预测模型已对特定终点（如hERG通道阻断）达到临床可靠性水平；数字孪生技术正在使个体化药物模拟成为可能。

2. **仍需克服的挑战**：扰动预测的精度尚未系统性超越简单基线；模型幻觉、可解释性、数据偏差和验证困难等核心问题有待解决；真实世界临床验证的案例仍然有限。

3. **未来趋势**：从单模态到全息多模态整合、从相关性学习到因果推断、从静态模型到持续更新、从研究工具到临床核心决策支持、从"一个模型应对所有任务"到专业化基础模型生态。

大模型能否完全替代传统的药物效应评估方法？目前来看，更可能的答案是：**AI将成为传统方法的强大补充，而非替代**。最有前景的路径是"AI+机制模型"混合方法——利用AI发现数据中的复杂模式，同时利用机制模型（如PBPK、系统生物学模型）提供生物学可解释性和因果推断能力。最终，药物评估将从"依赖实验和临床观察"转向"AI预测+实验验证"的闭环迭代模式，大幅加速药物研发进程，提升个体化用药的精准度。

---

## 参考资料

[^1]: Hu, Y. et al. (2026). Multi-omics and artificial intelligence for precision drug discovery. *Nature Reviews* (Signal Transduction and Targeted Therapy). https://www.nature.com/articles/s41392-026-02631-6

[^2]: Cui, H. et al. (2024). scGPT: Toward Building a Foundation Model for Single-Cell Multi-Omics Using Generative AI. *Nature Methods*, 21, 1470–1480. https://pmc.ncbi.nlm.nih.gov/articles/PMC12984679

[^3]: Ahlmann-Eltze, C., Huber, W., & Anders, S. (2025). Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines. *Nature Methods*. https://www.nature.com/articles/s41592-025-02772-6

[^4]: Miladinovic, D. et al. (2025). Large Perturbation Models. *Nature Computational Science*. https://www.linkedin.com/posts/vsavova_deep-learning-based-gene-perturbation-effect-activity-7360314175551639552-mjBK

[^5]: DRPLLM: A Large Language Model-Based Framework for Predicting Drug Response in Cancer Using Multi-Omics Data. Mayo Clinic. https://mayoclinic.elsevierpure.com/en/publications/drpllm-a-large-language-model-based-framework-for-predicting-drug

[^6]: CancerGPT for few shot drug pair synergy prediction using large pretrained language models. *npj Digital Medicine*. https://www.nature.com/articles/s41746-024-01024-9

[^7]: Drug response in the era of precision medicine: A methodological review. *PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12722026

[^8]: NVIDIA BioNeMo Expands Computer-Aided Drug Discovery With New Foundation Models. https://blogs.nvidia.com/blog/bionemo-ai-drug-discovery-foundation-models-microservices

[^9]: New AI foundation model aims to speed up drug discovery. *Drug Target Review*. https://www.drugtargetreview.com/new-ai-foundation-model-aims-to-speed-up-drug-discovery/1866838.article

[^10]: Foundation Models in Drug Discovery: BiopharmaTrend. https://www.biopharmatrend.com/artificial-intelligence/foundation-models-in-biology-198

[^11]: Zhang, J. et al. (2025). Computational toxicology in drug discovery: applications of ... *Briefings in Bioinformatics*, 26(5), bbaf533. https://academic.oup.com/bib/article/26/5/bbaf533/8276062

[^12]: Artificial Intelligence (AI) in Predictive Toxicology Market Report 2025. https://www.researchandmarkets.com/reports/5954509/artificial-intelligence-ai-in-predictive

[^13]: AI toxicity prediction: What machine learning models can (and can't) tell you about drug safety. *Drug Discovery News*. https://www.drugdiscoverynews.com/ai-toxicity-prediction-what-machine-learning-models-can-and-can-t-tell-you-about-drug-safety-17358

[^14]: LLMs for Drug-Drug Interaction Prediction. *arXiv*. https://arxiv.org/pdf/2502.06890

[^15]: Predicting drug-drug interactions with AI: Methods, datasets, and practical application. *Drug Discovery News*. https://www.drugdiscoverynews.com/predicting-drug-drug-interactions-with-ai-methods-datasets-and-practical-application-17360

[^16]: Prediction of pharmacokinetic/pharmacodynamic properties of aldosterone synthase inhibitors using an AI-PBPK model. *Frontiers in Pharmacology*. https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1578117/full

[^17]: Machine Learning for PK/PD Modeling in Drug Development. Certara. https://www.certara.com/blog/machine-learning-for-pk-pd-modeling-in-drug-development

[^18]: How AI could transform drug modeling and pharmacometric workflows. *DevDiscourse*. https://www.devdiscourse.com/article/technology/3646623-how-ai-could-transform-drug-modeling-and-pharmacometric-workflows

[^19]: Generative AI and digital twins: shaping a paradigm shift from precision to truly personalized medicine. *Expert Opinion on Drug Discovery*. https://www.tandfonline.com/doi/full/10.1080/17460441.2025.2507376

[^20]: Digital Twins in Personalized Medicine: Bridging Innovation ... *PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12653454

[^21]: Enhancing randomized clinical trials with digital twins. *npj Systems Biology and Applications*. https://www.nature.com/articles/s41540-025-00592-0

[^22]: Foundation Models Improve Perturbation Response Prediction. Genbio AI. https://genbio.ai/foundation-models-improve-perturbation-response-prediction

[^23]: LLM Evaluation for Biotech: A Methodological Guide. IntuitionLabs. https://intuitionlabs.ai/articles/llm-evaluation-biotech-guide

[^24]: Holistic Evaluation of Large Language Models for Medical Applications. Stanford HAI. https://hai.stanford.edu/news/holistic-evaluation-of-large-language-models-for-medical-applications

[^25]: Biomedical Foundation Models - IBM Research. https://research.ibm.com/projects/biomedical-foundation-models

[^26]: How AI is transforming drug discovery. *Drug Discovery News*. https://www.drugdiscoverynews.com/ai-is-transforming-drug-discovery-16706

[^27]: Artificial Intelligence for Drug Development | FDA. https://www.fda.gov/about-fda/center-drug-evaluation-and-research-cder/artificial-intelligence-drug-development

[^28]: Delile, J. et al. (2025). Foundation models in drug discovery: Phenomenal growth today, transformative potential tomorrow? *Drug Discovery Today*, 30(12), 104518. https://pubmed.ncbi.nlm.nih.gov/41167387

