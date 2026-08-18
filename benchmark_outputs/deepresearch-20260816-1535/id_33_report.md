
# 先进制程芯片金属薄膜沉积技术深度调研报告

## 摘要

在当今 5nm、3nm 乃至 2nm 先进制程逻辑芯片的制造中，金属薄膜的沉积主要依赖**物理气相沉积（PVD）**、**化学气相沉积（CVD）** 和**原子层沉积（ALD）** 三种技术。**电子束蒸发（E-beam evaporation）** 和**分子束外延（MBE）** 在 **高性能 CMOS 逻辑芯片的大规模量产中基本不被采用**，前者因其线-of-sight 特性、X 射线损伤及台阶覆盖率差，后者因其极低的沉积速率和高昂成本，均被排除在先进逻辑制造的主流工艺之外。然而，电子束蒸发在化合物半导体、MEMS、光学镀膜等领域仍有重要应用，MBE 则在 III-V 族化合物半导体、量子器件和特种光电芯片中不可或缺。

---

## 1. 物理气相沉积（PVD）

### 1.1 在先进制程中的角色

PVD（尤其是磁控溅射）是先进逻辑芯片制造中**最成熟的金属薄膜沉积技术之一**，广泛用于前段（FEOL）和后段（BEOL）工艺。Applied Materials 是 PVD 设备的绝对龙头，占据约 85% 的市场份额[^1]。

### 1.2 沉积的金属薄膜

| 金属薄膜 | 应用场景 | 制程节点 |
|---------|---------|---------|
| **Cu 种子层** | 铜互连双大马士革工艺中电镀铜前的种子层 | 所有节点（7nm/5nm/3nm） |
| **Ta / TaN** | 铜扩散阻挡层/衬垫层（传统工艺） | 7nm 及以上，5nm 开始部分被 ALD 替代 |
| **Ti / TiN** | 接触孔粘附层、金属硬掩模、功函数金属（部分） | 所有节点 |
| **Al** | 键合焊盘（Al Pad）、部分铝互连 | 28nm 及以上，在先进节点仅用于顶层焊盘 |
| **Co** | 局部互连及衬垫层 | 7nm/5nm 开始引入 |

### 1.3 选择原因

- **高沉积速率**：适合大规模量产，产能高[^2]。
- **高纯度**：物理过程无化学反应副产物，薄膜纯度高[^3]。
- **适用范围广**：可沉积几乎所有金属和合金。
- **工艺成熟**：已在产线中应用数十年，成本可控。

### 1.4 局限性

- **台阶覆盖率差**：PVD 是线-of-sight 工艺，在高深宽比（> 5:1）的沟槽和通孔中覆盖率快速下降[^4]。
- **厚度均匀性受限**：在 5nm 以下节点，PVD 难以实现 < 2nm 的超薄均匀阻挡层，因此**ALD 正在逐步替代 PVD 用于 TaN 阻挡层沉积**[^5][^6]。

---

## 2. 化学气相沉积（CVD）

### 2.1 在先进制程中的角色

CVD 在先进逻辑芯片制造中同样不可或缺，主要用于**填充接触孔和通孔**、沉积**衬垫层**和**局部互连金属**。Lam Research 的 ALTUS 系列是 CVD/ALD 金属沉积的标杆设备[^7]。

### 2.2 沉积的金属薄膜

| 金属薄膜 | 应用场景 | 制程节点 |
|---------|---------|---------|
| **W（钨）** | 接触孔插塞、通孔填充、DRAM 字线 | 所有节点（5nm/3nm 仍大量使用） |
| **TiN（CVD）** | 钨阻挡层/粘附层（MOCVD） | 14nm 及以上，先进节点逐步被 ALD 替代 |
| **Co（钴）** | 局部互连、Cu 衬垫层、Cu 盖帽层 | 7nm/5nm/3nm 广泛使用 |
| **Ru（钌）** | Cu 衬垫层、替代 Cu 的互连金属 | 5nm/3nm 评估及初步量产 |
| **Mo（钼）** | 字线、接触孔填充（新兴） | 3nm 以下研发及初步量产 |

### 2.3 选择原因

- **优异的台阶覆盖率**：相比 PVD，CVD 的台阶覆盖率显著更好，可填充高深宽比结构[^8]。
- **选择性沉积能力**：CVD Co 已实现金属-金属选择性沉积，用于 Cu 盖帽层以提升电迁移可靠性[^9]。
- **适合填充**：CVD W 从 0.35μm 时代起就是接触孔填充的标准工艺，至今仍在 5nm/3nm 节点使用[^10]。

### 2.4 局限性

- **前驱体成本高**：金属有机前驱体（如 Co、Ru 前驱体）价格昂贵。
- **杂质引入**：CVD 反应副产物可能引入 C、H、F 等杂质，影响薄膜质量。
- **温度要求**：部分 CVD 工艺需要较高温度（> 400°C），可能对热预算有限的后段工艺造成挑战。

---

## 3. 原子层沉积（ALD）

### 3.1 在先进制程中的角色

**ALD 是 5nm/3nm 节点金属薄膜沉积中增长最快的技术**，也是满足先进制程极端工艺要求的**核心使能技术**。随着线宽缩小和深宽比增加，ALD 因其**原子级厚度控制**和**无与伦比的台阶覆盖率**成为不可替代的工艺[^11][^12]。

### 3.2 沉积的金属薄膜

#### 3.2.1 前段（FEOL）——高 k 金属栅极（HKMG）

| 金属薄膜 | 应用场景 | 说明 |
|---------|---------|------|
| **TiN** | PMOS 功函数金属 | 通过 ALD 实现共形覆盖，功函数约 5.0 eV[^13] |
| **TiAlC / TiAl** | NMOS 功函数金属 | 通过 ALD 沉积，实现 N 型功函数[^14] |
| **TaN** | 功函数调节层、阻挡层 | 中间能隙功函数，用于栅极堆叠[^15] |
| **W（ALD）** | 栅极填充金属 | 22nm 节点即引入，用于替代栅极金属填充[^16] |

#### 3.2.2 后段（BEOL）——互连

| 金属薄膜 | 应用场景 | 制程节点 |
|---------|---------|---------|
| **TaN（ALD）** | Cu 扩散阻挡层 | 5nm 及以下替代 PVD TaN[^6] |
| **Co（ALD）** | 衬垫层、局部互连 | 7nm/5nm/3nm |
| **Ru（ALD）** | 衬垫层、替代 Cu 互连 | 5nm/3nm |
| **Mo（ALD）** | 字线、接触填充 | 3nm 以下（Lam ALTUS Halo 已量产）[^17] |
| **W（ALD）** | 成核层 + 阻挡层 | 所有先进节点 |

### 3.3 选择原因

- **原子级厚度控制**：每循环生长约 0.1 nm，可实现亚纳米级精度[^12]。
- **完美台阶覆盖率**：即使在深宽比 > 20:1 的结构中也能实现 100% 共形覆盖[^18]。
- **低温工艺**：ALD 可在 150–350°C 范围内沉积，适合热预算敏感的后段工艺[^19]。
- **薄膜致密、杂质少**：自限制反应机制确保薄膜质量高、缺陷密度低[^20]。
- **超薄阻挡层**：5nm 节点需要 ≤ 2nm 的 TaN 阻挡层，只有 ALD 能实现[^5]。

### 3.4 局限性

- **沉积速率极低**：每循环仅 0.1 nm，导致产能远低于 PVD/CVD[^21]。
- **前驱体昂贵且开发难度大**：金属 ALD 前驱体需要高挥发性和热稳定性，开发周期长。

---

## 4. 电子束蒸发（E-beam Evaporation）

### 4.1 在先进制程中的角色

**电子束蒸发在先进逻辑芯片（5nm/3nm）的高量产制造中基本不被采用**。其线-of-sight 沉积特性、X 射线辐射损伤以及无法共形覆盖高深宽比结构的缺点，使其无法满足先进制程的要求。

### 4.2 沉积的金属薄膜

| 金属薄膜 | 应用场景 | 说明 |
|---------|---------|------|
| Al、Cu、Au、Pt、Ti、Ni 等 | 科研、化合物半导体、MEMS | 非先进逻辑主流 |
| 难熔金属（W、Ta、Mo） | 光学镀膜、特种涂层 | 高熔点材料蒸发优势 |

### 4.3 未被先进逻辑采用的原因

- **线-of-sight 沉积**：无法覆盖高深宽比沟槽和通孔的侧壁/底部，台阶覆盖率极差[^22]。
- **X 射线损伤**：高能电子束轰击靶材产生 X 射线，可能损伤 CMOS 栅氧化层，影响器件可靠性[^23]。
- **均匀性受限**：在大尺寸晶圆（300mm）上难以实现高均匀性。
- **产能低**：单批处理能力有限，不适合大规模量产。

### 4.4 仍在使用的地方

- **化合物半导体制造**：GaAs、InP 等 III-V 族器件中用于金属电极沉积（如 AuGeNi、Ti/Pt/Au）[^24]。
- **MEMS 和传感器**：用于 lift-off 工艺，线-of-sight 特性反而有利于侧壁无覆盖。
- **光学镀膜和科研**：高纯度薄膜沉积，用于研究级器件。

---

## 5. 分子束外延（MBE）

### 5.1 在先进制程中的角色

**MBE 在先进逻辑芯片（5nm/3nm）的高量产制造中同样不被采用**。其极低的生长速率（< 3000 nm/h）、超高真空要求（10⁻⁸–10⁻¹² Torr）以及高昂的维护成本，使其无法满足大规模量产的需求[^25]。

### 5.2 沉积的金属薄膜

| 金属薄膜 | 应用场景 | 说明 |
|---------|---------|------|
| 金属薄膜在 CMOS 量产中**不使用** | — | — |

MBE 主要用于**半导体薄膜**（如 GaAs、InGaAs、SiGe）的外延生长，**而非金属薄膜**。在先进逻辑制造中，MBE 曾用于研发 SiGe 沟道应变工程，但量产中已被 CVD 外延替代。

### 5.3 未被先进逻辑采用的原因

- **沉积速率极低**：< 1 μm/h，远低于量产需求[^25]。
- **设备成本极高**：单台 MBE 系统 > 100 万美元，维护成本高[^26]。
- **产能低**：无法支持每月数万片晶圆的大规模生产。
- **金属薄膜沉积限制**：MBE 不适于沉积金属薄膜用于互连或接触。

### 5.4 仍在使用的地方

- **III-V 族化合物半导体**：用于 HEMT、HBT、激光器、LED 等器件[^27]。
- **量子器件和拓扑绝缘体**：需要原子级精确控制界面的高端研究[^28]。
- **硅光子集成**：用于在硅上外延 BaTiO₃ 等光学材料（imec 与 Veeco 合作开发 300mm MBE 平台）[^29]。

---

## 6. 综合对比

| 项目 | PVD | CVD | ALD | E-beam Evaporation | MBE |
|------|-----|-----|-----|-------------------|-----|
| **先进逻辑量产使用** | ✅ 广泛使用 | ✅ 广泛使用 | ✅ 核心使能技术 | ❌ 不使用 | ❌ 不使用 |
| **台阶覆盖率** | 一般 | 好 | 优秀 | 极差 | 一般 |
| **厚度控制精度** | ~5 nm | ~1 nm | ~0.1 nm | ~5 nm | 原子级 |
| **沉积速率** | 高 | 高 | 极低 | 中 | 极低 |
| **薄膜纯度** | 高 | 中 | 高 | 高 | 极高 |
| **量产成本** | 低 | 中 | 高 | 中 | 极高 |
| **主要金属薄膜** | Cu种子层、Ta/TaN、TiN、Al | W、Co、Ru、TiN | TaN、TiN、TiAlC、Co、Ru、Mo、W | 不用于先进逻辑 | 不用于先进逻辑 |
| **适用场景** | 互连、硬掩模、焊盘 | 接触填充、衬垫层、互连 | 阻挡层、功函数金属、栅极填充 | 化合物半导体、MEMS、光学 | III-V 族、量子器件、研发 |

---

## 7. 先进制程实际工艺示例

### 7.1 5nm/3nm 铜互连典型流程

1. **低 k 介电质沉积**（PECVD / CVD）
2. **通孔/沟槽刻蚀**
3. **阻挡层沉积**：**ALD TaN**（2–3 nm）→ 替代传统 PVD TaN[^5]
4. **衬垫层沉积**：**CVD Co** 或 **CVD Ru**（1–2 nm）[^30]
5. **Cu 种子层沉积**：**PVD Cu**（20–50 nm）[^31]
6. **Cu 电镀填充**（ECD）
7. **CMP 平坦化**
8. **Cu 盖帽层**：**选择性 CVD Co**（~3 nm）[^9]

### 7.2 5nm/3nm HKMG 栅极典型流程（后栅极工艺）

1. **伪栅极去除**
2. **界面层**：化学氧化 SiO₂（~0.5 nm）
3. **高 k 介电质**：**ALD HfO₂**（1–3 nm）[^32]
4. **PMOS 功函数金属**：**ALD TiN**（~3–5 nm）[^13]
5. **NMOS 功函数金属**：**ALD TiAlC**（~3–5 nm）[^14]
6. **阻挡层**：**ALD TaN**（~2 nm）
7. **栅极填充金属**：**CVD/ALD W** 或 **CVD Al**[^16]

---

## 8. 设备厂商格局

| 沉积技术 | 主要供应商 | 市场份额特点 |
|---------|-----------|------------|
| **PVD** | Applied Materials（~85%）、Evatec、Ulvac | AMAT 绝对主导[^1] |
| **CVD（金属）** | Applied Materials、Lam Research、TEL | 三强主导，CR3 > 80%[^1] |
| **ALD（金属）** | ASM、TEL、Lam Research、Applied Materials | 竞争格局相对分散，ASM 在 HKMG 领域领先[^1] |
| **E-beam** | 无大规模量产设备商 | 仅用于研发和特殊应用 |
| **MBE** | Veeco、Riber、SVT Associates | 仅用于化合物半导体和研发[^29] |

---

## 9. 未来趋势

- **ALD 占比持续提升**：随着制程微缩到 2nm 以下，ALD 将覆盖更多金属薄膜沉积步骤，包括阻挡层、功函数金属、互连金属等[^11]。
- **PVD 仍不可替代**：Cu 种子层、Al 焊盘、部分硬掩模等仍需 PVD 的高速率和低成本。
- **CVD 向选择性沉积演进**：选择性 CVD Co 和 W 在先进节点中用于减少工艺步骤、提升良率[^9]。
- **新材料引入**：Ru、Mo 等替代金属的沉积更多地依赖 ALD 和 CVD，传统 PVD 面临挑战[^17][^30]。
- **E-beam 和 MBE 在 CMOS 量产中无应用前景**，但在化合物半导体、硅光子、量子计算等新兴领域需求增长。

---

## 参考资料

[^1]: 薄膜沉积设备行业分析，观研报告网，2024. https://m.chinabaogao.com/detail/554904.html

[^2]: Wafer World, "Silicon Manufacturing: Comparing Physical Vapor, Atomic Layer, and Chemical Vapor Deposition." https://www.waferworld.com/post/silicon-manufacturing-comparing-physical-vapor-atomic-layer-and-chemical-vapor-deposition

[^3]: SK 海力士新闻中心，"半导体前端工艺：第五篇 沉积." https://news.skhynix.com/cn/semiconductor-front-end-process-episode-5-deposition

[^4]: 腾讯云开发者社区，"薄膜沉积设备." https://cloud.tencent.com/developer/news/2504574

[^5]: Z. Wu et al., "PVD-Treated ALD TaN for Cu Interconnect Extension to 5nm Node and Beyond," IITC 2018. https://ieeexplore.ieee.org/document/8430433

[^6]: TSMC Research, "Interconnect Research." https://research.tsmc.com/chinese/research/interconnect/publish-time-7.html

[^7]: Lam Research, "Deposition — ALTUS Product Family." https://www.lamresearch.com/products/our-processes/deposition

[^8]: 知乎，"芯片制造的核心工艺：一文看懂薄膜沉积." https://zhuanlan.zhihu.com/p/521919587

[^9]: AtomicLimits, "Metal-on-metal area-selective deposition — Why cobalt succeeded where tungsten failed." https://www.atomiclimits.com/2022/01/13/metal-on-metal-area-selective-deposition-why-cobalt-succeeded-where-tungsten-failed

[^10]: MDPI, "Process Optimization of Via Plug Multilevel Interconnections in CMOS Logic Devices." https://pmc.ncbi.nlm.nih.gov/articles/PMC7019522

[^11]: SemiEngineering, "Making Chips At 3nm And Beyond." https://semiengineering.com/making-chips-at-3nm-and-beyond

[^12]: Wikipedia, "Atomic layer deposition." https://en.wikipedia.org/wiki/Atomic_layer_deposition

[^13]: MDPI, "Atomic Layer Deposition (ALD) of Metal Gates for CMOS." https://www.mdpi.com/2076-3417/9/11/2388

[^14]: PMC, "CMOS Scaling for the 5 nm Node and Beyond: Device, Process and Technology." https://pmc.ncbi.nlm.nih.gov/articles/PMC11123950

[^15]: Eureka PatSnap, "Tantalum Gate Electrode Material." https://eureka.patsnap.com/materials/tantalum-gate-electrode

[^16]: G. Wang et al., "Application of atomic layer deposition tungsten (ALD W) as gate filling metal for 22 nm and beyond nodes CMOS technology," ECS J. Solid State Sci. Technol., 2014. https://doi.org/10.1149/2.015404jss

[^17]: Lam Research, "Lam Research Ushers in New Era of Semiconductor Metallization with ALTUS Halo for Molybdenum Atomic Layer Deposition." https://newsroom.lamresearch.com/2025-02-19-Lam-Research-Ushers-in-New-Era-of-Semiconductor-Metallization-with-ALTUS-R-Halo-for-Molybdenum-Atomic-Layer-Deposition

[^18]: ASM, "ALD (Atomic Layer Deposition)." https://www.asm.com/our-technology-products/ald

[^19]: Materion, "Atomic Layer Deposition: Significance and Application in Modern Microelectronics." https://www.materion.com/en/insights/blog/atomic-layer-deposition-significance-application-in-modern-microelectronics

[^20]: AIP, "Atomic layer deposition of metals: Precursors and film growth." https://pubs.aip.org/aip/apr/article/6/4/041309/124304/Atomic-layer-deposition-of-metals-Precursors-and

[^21]: 上海交通大学 AEMD 平台，"薄膜沉积." https://aemd.sjtu.edu.cn/guide/44.html

[^22]: UniversityWafer, "E-Beam Evaporated Metals on Silicon Wafers." https://www.universitywafer.com/e-beam-evaporated-metals.html

[^23]: SAMaterials, "Electron Beam Evaporation: For High-Melting-Point Materials." https://www.samaterials.com/content/electron-beam-evaporation.html

[^24]: Compound Semiconductor, "The Resurgence Of Electron Beam Evaporation." https://compoundsemiconductor.net/article/96507/The_Resurgence_Of_Electron_Beam_Evaporation

[^25]: Wikipedia, "Molecular-beam epitaxy." https://en.wikipedia.org/wiki/Molecular-beam_epitaxy

[^26]: IntechOpen, "Molecular Beam Epitaxy: Principals, Advantages and Challenges." https://www.intechopen.com/chapters/1218932

[^27]: AIP, "Development of molecular beam epitaxy technology for III–V." https://pubs.aip.org/avs/jva/article/31/5/050814/244842/Development-of-molecular-beam-epitaxy-technology

[^28]: Stanford University, "Molecular Beam Epitaxy — Shen Laboratory." https://arpes.stanford.edu/research/tool-development/molecular-beam-epitaxy

[^29]: imec, "Integration of barium titanate on silicon photonics." https://www.imec-int.com/en/press/veeco-and-imec-develop-300mm-compatible-process-enable-integration-barium-titanate-silicon

[^30]: SemiEngineering, "Interconnects Approach Tipping Point." https://semiengineering.com/interconnects-approach-tipping-point

[^31]: Applied Materials, "PVD." https://www.appliedmaterials.com/us/en/semiconductor/products/processes/pvd.html

[^32]: MDPI, "CMOS Scaling for the 5 nm Node and Beyond: Device, Process and Technology." https://www.mdpi.com/2079-4991/14/10/837

---

*报告生成日期：2026 年 8 月 16 日*
