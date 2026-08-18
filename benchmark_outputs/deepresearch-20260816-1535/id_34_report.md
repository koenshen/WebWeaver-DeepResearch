
# 二维半导体低接触电阻的物理机制：统一理论探索与未来发展路线图

## 摘要

二维半导体（如二硫化钼 MoS₂）的金属-半导体接触电阻问题，是制约其走向实际应用的核心瓶颈。近年来，科研人员开发了半金属接触、范德华接触、边缘接触、相工程、缓冲层插入等多种策略，均实现了极低的接触电阻。然而，每种方法背后往往有独特的物理解释，导致该领域缺乏明确的发展方向。本文通过系统梳理各类低接触电阻技术的物理机制，提出一个可能的统一理论框架——“费米能级钉扎解除与界面态饱和”，并以此为基础预测该领域的未来发展方向。

---

## 1. 引言：接触电阻问题的根源

二维半导体（如 MoS₂）与金属接触时，理想情况下应遵循肖特基-莫特定律（Schottky-Mott rule），即肖特基势垒高度（SBH）由金属功函数与半导体电子亲和能之差决定。然而，实际器件中观测到的势垒高度往往与金属功函数几乎无关，这一现象被称为**费米能级钉扎**（Fermi Level Pinning, FLP）[1]。

FLP 的主要成因包括：

- **金属诱导的带隙态（Metal-Induced Gap States, MIGS）**：金属的扩展波函数渗入半导体，在带隙中产生连续态，导致费米能级被钉扎在电荷中性能级附近 [2]。
- **缺陷诱导的带隙态（Defect-Induced Gap States, DIGS）**：金属沉积或器件制备过程中引入的晶格缺陷、空位、化学残留等，在带隙中产生局域态 [3]。
- **界面偶极子与轨道杂化**：金属与硫族元素的强化学键合导致能带结构畸变，产生界面偶极 [4]。

FLP 的直接后果是肖特基势垒高度无法通过选择金属功函数来有效调节，从而产生高接触电阻（Rc）。对于单层 MoS₂，理论量子极限接触电阻约为 26 Ω·μm（在面载流子密度 10¹³ cm⁻² 时），但传统蒸发金属（如 Ti、Ni、Au）的接触电阻通常在 10³–10⁴ Ω·μm 量级，差距巨大 [1]。

---

## 2. 主要低接触电阻策略及其物理机制

### 2.1 半金属接触（Semi-Metal Contact）

**代表性工作**：Shen 等（2021）利用铋（Bi）作为 MoS₂ 的接触电极，实现了 123 Ω·μm 的超低接触电阻 [5]。

**物理解释——弱金属化与带隙态饱和机制**：
- 半金属（如 Bi、Sb）在费米能级处的态密度（DOS）几乎为零，这导致金属与半导体接触时，MIGS 的产生被显著抑制 [6]。
- 由于 Bi 的 pz 轨道与 MoS₂ 的 dz² 轨道弱耦合，MIGS 的波函数在进入 MoS₂ 带隙后迅速衰减，且这些有限的 MIGS 被来自 Bi 的电子完全填充，即“带隙态饱和”（Gap-State Saturation, GSS）[5]。
- 带隙态饱和后，费米能级不再被钉扎，而是能够自由移动至 MoS₂ 的导带底附近，形成准欧姆接触。
- 此外，Bi 与 MoS₂ 的层间距较大（约 3.3 Å），属于弱范德华接触，进一步抑制了轨道杂化 [7]。

**核心机制**：**利用费米能级处接近零的 DOS 来抑制 MIGS 的产生，并通过带隙态饱和实现费米能级解钉扎。**

### 2.2 范德华接触（Van der Waals Contact）

**代表性工作**：
- Liu 等（2018）通过机械转移预沉积的金属层，实现了 MoS₂/Au 的范德华接触，获得接近肖特基-莫特极限的钉扎因子（S ≈ 0.96）[8]。
- 王淼等（2024）利用低温范德华外延生长 2D Cd 金属，实现了 70–100 Ω·μm 的超低接触电阻 [9]。
- 英国剑桥大学团队利用 In/Au 合金蒸发，在单层 MoS₂ 上实现 3000 ± 300 Ω·μm 的低接触电阻，并发现界面为无缺陷的范德华键合 [10]。

**物理解释——界面纯净度与 MIGS 抑制**：
- 传统金属蒸发工艺会在二维半导体表面引入等离子体损伤、化学残留和晶格缺陷，这些 DIGS 是 FLP 的重要来源。
- 范德华接触通过机械转移或弱外延生长，避免了金属原子与二维晶格直接共价键合，从而：
  - 保持半导体能带结构的完整性；
  - 消除界面缺陷态；
  - 减小金属-半导体波函数重叠，降低 MIGS 密度。
- 但范德华间隙本身会产生隧穿势垒。理论计算表明，当间隙宽度小于约 2 Å 时，隧穿电阻可以忽略 [11]。

**核心机制**：**通过物理隔离或弱键合来实现“无损伤界面”，从源头消除 DIGS 和 MIGS，恢复费米能级的可调性。**

### 2.3 边缘接触（Edge Contact）

**代表性工作**：Yang 等（2016）利用 1D 边缘接触，在 MoS₂ 上获得了钉扎因子 S ≈ 0.975 的费米能级解钉扎，并实现 432 cm²/V·s 的空穴迁移率 [12]。

**物理解释**：
- 边缘接触中，金属与 MoS₂ 在原子层的边缘处形成共价键合，轨道重叠强，界面态密度高。
- 但与顶部接触不同，边缘接触的载流子注入是横向的，沿每一层独立注入，避免了层间电阻。
- 强轨道杂化导致接触区域半导体被“金属化”——带隙消失，形成类似欧姆接触的能带结构。
- 边缘接触的最优性能取决于金属与边缘的原子级匹配度。

**核心机制**：**通过边缘共价键合实现接触区域的局部金属化，使肖特基势垒在几何上被“短路”。**

### 2.4 缓冲层插入（Buffer Layer Insertion）

**代表性工作**：
- 在金属与 MoS₂ 之间插入石墨烯、h-BN、TiO₂ 或 MoSe₂ 等缓冲层，可显著降低接触电阻 [13]。
- 插入 MoSe₂ 层后，SBH 从 ~100 meV 降至 ~25 meV，接触电阻下降一个数量级 [14]。

**物理解释**：
- 缓冲层作为“隔离层”，一方面物理上阻止金属波函数渗入半导体，减少 MIGS；
- 另一方面，缓冲层本身可以提供能带对齐的中间态，使费米能级降至钉扎路径。
- 例如，MoSe₂ 作为插层时，其电子亲和能略小于 MoS₂，导致 FLP 被耦合到 MoSe₂ 的导带底附近，从而降低 SBH [14]。

**核心机制**：**利用中间层来“解耦”金属与半导体之间的电子态相互作用，同时提供更优的能带对准。**

### 2.5 相工程（Phase Engineering）

**代表性工作**：将 MoS₂ 的 2H（半导体相）接触区域转化为 1T 或 1T′（金属相），实现准欧姆接触 [15]。

**物理解释**：
- 2H-MoS₂ 是半导体，具有 1.8 eV 的带隙；1T′-MoS₂ 是金属，无带隙。
- 局域相变后，载流子从金属电极进入 1T′-MoS₂，再通过 2H/1T′ 界面注入半导体通道。
- 该界面的势垒极低，因为 1T′ 相的费米能级与 2H 相的导带底自然对齐。

**核心机制**：**在接触区域原位产生金属相，消除半导体-金属界面的本征带隙，本质上是将“接触”从异质结转变为同质结。**

### 2.6 掺杂工程（Doping Engineering）

**代表性工作**：
- 利用氯化物（如 AuCl₃、PEI）进行表面电荷转移掺杂，将 MoS₂ 接触电阻降至 0.5 kΩ·μm [16]。
- 等离子体处理（如 Ar⁺ 或 O₂ 等离子体）可在接触区域引入高浓度施主杂质。

**物理解释**：
- 重掺杂使肖特基势垒宽度变窄，载流子通过隧穿效应而非热发射注入，从而有效降低接触电阻。
- 掺杂还可以改变半导体的费米能级位置，使其与金属功函数对齐。
- 但二维半导体的极薄厚度使其难以通过传统离子注入实现稳定的重掺杂，表面电荷转移掺杂成为主要替代方案。

**核心机制**：**通过增加接触区域载流子浓度来减小势垒宽度，实现隧穿主导的欧姆接触。**

---

## 3. 统一理论框架的探索

### 3.1 各类策略的“共同分母”

尽管上述策略在物理图像上各不相同，但仔细分析可以发现它们具有以下**共同特征**：

| 策略 | MIGS 抑制 | DIGS 消除 | 势垒降低 | 隧穿增强 | 费米能级解钉扎 |
|------|-----------|-----------|----------|----------|----------------|
| 半金属接触 | ★★★★★ | ★★★ | ★★★★ | ★★★ | ★★★★★ |
| 范德华接触 | ★★★★ | ★★★★★ | ★★★ | ★★ | ★★★★★ |
| 边缘接触 | ★★ | ★★★ | ★★★★★ | ★★★★ | ★★★ |
| 缓冲层插入 | ★★★★ | ★★★★ | ★★★★ | ★★★ | ★★★★ |
| 相工程 | ★★ | ★★★ | ★★★★★ | ★★★★★ | ★★★★ |
| 掺杂工程 | ★ | ★★ | ★★★ | ★★★★★ | ★★★ |

**核心洞察**：所有成功的低接触电阻策略，最终都实现了以下三个物理目标中的**至少两个**：

1. **费米能级解钉扎**：使肖特基势垒高度重新具有可调性，从而能与半导体能带边缘对齐。
2. **界面态密度最小化**：在费米能级所在能量范围内，将 MIGS 和 DIGS 的密度降至最低。
3. **载流子注入效率最大化**：通过降低势垒高度或宽度，使热发射或隧穿电流达到最大。

### 3.2 建议的统一理论模型：“界面态饱和-费米能级解钉扎”模型

基于上述分析，本文提出一个可能的统一理论框架——**有效界面态调控（Effective Interface State Engineering, EISE）** 模型，其核心主张如下：

> **任何成功的低接触电阻方案，本质上都是通过降低费米能级附近界面态密度来实现费米能级解钉扎，使肖特基势垒高度能够接近肖特基-莫特极限，从而获得极低的接触电阻。**

具体而言：

- **半金属接触**（如 Bi、Sb）利用半金属自身的零 DOS 特性，从源头上抑制 MIGS 的产生，并通过带隙态饱和机制使费米能级自由移动。
- **范德华接触**通过物理隔离避免金属与半导体的强耦合，从而消除 MIGS 和 DIGS 的来源。
- **缓冲层插入**通过中间层来“吸收”或“屏蔽” MIGS，同时优化能带对齐。
- **边缘接触**和**相工程**通过改变接触区域的电子结构，实质上是将半导体“变成”金属，从而完全消除界面势垒。
- **掺杂工程**通过改变费米能级位置来绕过 FLP 的影响，虽然不直接消除 MIGS，但通过增加载流子浓度使隧穿电流主导，本质上等效于“有效势垒降低”。

### 3.3 该统一模型的局限性

必须指出，EISE 模型目前仍是一个描述性框架，而非严格的第一性原理模型。其局限性在于：

- 难以定量预测不同材料组合的最优接触电阻。
- 未充分考虑界面偶极子、晶格失配、热膨胀系数差异等二级效应。
- 在实践中，多种机制的协同效应（如半金属接触同时具有范德华间隙）使得实验观测难以完全归因于单一机制。

尽管如此，EISE 模型为理解该领域提供了一个清晰的思维框架，并有助于指导后续研究方向。

---

## 4. 未来发展方向与技术路线图

### 4.1 短期方向（2026–2028）：理论深化与材料筛选

- **建立统一的接触电阻理论模型**：结合第一性原理计算（DFT）与非平衡格林函数（NEGF），开发能够同时考虑 MIGS、DIGS、界面偶极子和隧穿效应的定量预测工具 [17]。
- **高通量材料筛选**：利用 DFT 计算筛选具有以下特性的候选接触材料：
  - 在费米能级处具有极低 DOS（如半金属、拓扑半金属）；
  - 与 MoS₂ 等二维半导体具有大层间距（>3 Å）；
  - 功函数与半导体导带底或价带顶匹配。
- **器件级仿真**：将统一理论模型集成到 TCAD 等工业级仿真工具中，实现从材料到器件的完整设计流程。

### 4.2 中期方向（2028–2032）：工艺集成与性能极限

- **接触电阻的量子极限**：MoS₂ 的理论量子极限接触电阻约为 26 Ω·μm（在 10¹³ cm⁻² 载流子密度下）。目前最佳结果（Bi 接触 123 Ω·μm、Cd 接触 70–100 Ω·μm）已接近但尚未达到此极限 [5][9]。未来需要：
  - 进一步优化界面纯净度；
  - 实现接触区域的高浓度掺杂（>10¹³ cm⁻²）；
  - 采用 2D 金属（如 1T′-WTe₂、VS₂）作为电极，实现完全无悬挂键的 2D/2D 接触 [18]。
- **CMOS 兼容性**：开发与现有硅基 CMOS 工艺兼容的低接触电阻方案，包括：
  - 低温（<400°C）金属沉积工艺；
  - 无光刻胶残留的干法转移技术；
  - 与高 k 介质栅极堆叠兼容的接触方案 [19]。
- **p 型接触的突破**：目前 n 型接触（电子注入）已取得显著进展，但高效 p 型接触（空穴注入）仍是短板。需要开发与 MoS₂ 价带顶对齐的高功函数接触材料。

### 4.3 长期方向（2032–2040）：全二维集成与三维异构集成

- **全二维晶体管**：利用 2D 金属电极（如石墨烯、1T′-MoS₂、NbS₂）与 2D 半导体沟道构成全二维异质结，实现无界面缺陷的欧姆接触 [20]。
- **三维单片集成（M3D）**：二维半导体凭借其低温工艺兼容性和原子级厚度，是实现三维集成电路的理想候选材料。接触电阻的降低将直接决定多层堆叠技术的可行性 [21]。
- **超越 CMOS 的功能器件**：低接触电阻使二维半导体光电器件、自旋电子器件、神经形态器件的性能潜力得以释放。

### 4.4 技术路线图总结

| 时间节点 | 关键目标 | 预期指标 |
|----------|----------|----------|
| 2026–2028 | 统一理论模型建立；高通量材料筛选 | 预测精度 < 50% 误差 |
| 2028–2030 | 接触电阻达到量子极限的 2 倍以内 | Rc < 50 Ω·μm |
| 2030–2032 | CMOS 兼容工艺验证；300 mm 晶圆级演示 | 均匀性 < 10% 变异 |
| 2032–2035 | p 型接触突破；全 2D 晶体管演示 | 空穴 Rc < 100 Ω·μm |
| 2035–2040 | 三维集成；超越 CMOS 功能器件 | 多层堆叠性能 > 硅基方案 |

---

## 5. 结论

二维半导体接触电阻问题看似存在多种互不兼容的解决方案，但本文通过系统分析认为，**所有成功的低接触电阻策略共享一个核心物理机制**：通过降低金属与半导体界面费米能级附近的电子态密度，实现费米能级解钉扎，使肖特基势垒高度接近理想值。这一“有效界面态调控”模型为理解该领域提供了一个统一的理论框架，并为未来的研究方向提供了清晰的指引。

未来的发展将从当前的“经验性探索”转向“理论指导下的理性设计”，其最终目标是实现完全欧姆的、与硅基 CMOS 工艺兼容的、可用于大规模集成的二维半导体接触方案。

---

## 参考资料

[1] Zheng, Y., Gao, J., Han, C., & Chen, W. (2021). Ohmic Contact Engineering for Two-Dimensional Materials. *Cell Reports Physical Science*, 2, 100298.  
https://www.cell.com/cell-reports-physical-science/fulltext/S2666-3864(20)30324-6

[2] Guo, Y., et al. (2016). Study on the intrinsic origin of the strong Fermi level pinning at metal/MoS₂ interfaces. *Nano Letters*, 16(4), 2535–2540.  
https://pubs.acs.org/doi/10.1021/acs.nanolett.6b00319

[3] Addou, R., et al. (2015). Surface defects on natural MoS₂. *ACS Applied Materials & Interfaces*, 7(21), 11338–11344.  
https://pubs.acs.org/doi/10.1021/acsami.5b01751

[4] Liu, X., et al. (2022). Fermi Level Pinning Dependent 2D Semiconductor Devices. *Advanced Materials*, 34, 2108425.  
https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202108425

[5] Shen, P.-C., et al. (2021). Ultralow contact resistance between semimetal and monolayer semiconductors. *Nature*, 593, 211–217.  
https://www.nature.com/articles/s41586-021-03472-9  
https://repository.kaust.edu.sa/bitstreams/f00e55c2-160a-467c-b7c5-5a3c17804f17/download

[6] Su, T., et al. (2023). Semimetal contacts to monolayer semiconductor: weak metalization as an effective mechanism to Schottky barrier lowering. *Journal of Physics D: Applied Physics*, 56, 235001.  
https://ui.adsabs.harvard.edu/abs/2023JPhD...56w4001S/abstract

[7] Direct Visualization of Metal-Induced Gap State Distribution and Valley Band Evolution at Metal Versus Semimetal MoS₂ Interfaces. *Nature Communications*.  
https://pmc.ncbi.nlm.nih.gov/articles/PMC12120976/

[8] Liu, Y., et al. (2018). Approaching the Schottky-Mott limit in van der Waals metal–semiconductor junctions. *Nature*, 557, 696–700.  
https://www.nature.com/articles/s41586-018-0129-8

[9] Wang, M., et al. (2025). 2D Cd metal contacts via low-temperature van der Waals epitaxy towards high-performance 2D transistors. *Nature Communications*, 16, 59174.  
https://www.nature.com/articles/s41467-025-59174-7

[10] Van der Waals contacts between three-dimensional metals and two-dimensional semiconductors. *Nature Nanotechnology*.  
https://www.repository.cam.ac.uk/items/29198282-f390-4a70-8f70-cb142f85f14c

[11] Fundamentals of low-resistive 2D-semiconductor metal contacts: an ab-initio NEGF study. *npj 2D Materials and Applications*, 7, 42 (2023).  
https://communities.springernature.com/posts/fundamentals-of-low-resistive-2d-semiconductor-metal-contacts-an-ab-initio-negf-study

[12] Yang, Z., et al. (2016). 1D edge contacts to 2D materials. *ACS Nano*, 10(6), 6392–6399.  
https://pubs.acs.org/doi/10.1021/acsnano.6b01993

[13] Cui, X., et al. (2017). Low-temperature ohmic contact to monolayer MoS₂ by Van der Waals bonded Co/h-BN electrodes. *Nano Letters*, 17, 4781–4786.  
https://pubs.acs.org/doi/10.1021/acs.nanolett.7b01536

[14] Andrews, K. (2020). Improved Contacts and Device Performance in MoS₂ Transistors Using 2D Semiconductor Interlayer. *Digital Commons at Wayne State University*.  
https://digitalcommons.wayne.edu/oa_dissertations/2343

[15] Kappera, R., et al. (2014). Phase-engineered low-resistance contacts for ultrathin MoS₂ transistors. *Nature Materials*, 13, 1128–1134.  
https://www.nature.com/articles/nmat4080

[16] Yang, L., et al. (2014). High-performance MoS₂ field-effect transistors enabled by chloride doping: Record low contact resistance (0.5 kΩ·µm) and record high drain current (460 µA/µm). *VLSI Technology Symposium*.  
https://ieeexplore.ieee.org/document/6894403

[17] Deylgat, E. (2024). Comparing contact resistance of edge-, top-, and hybrid-contacted two-dimensional materials. *Physical Review Applied*, 21, 044001.  
https://link.aps.org/doi/10.1103/ddpx-1tt4

[18] Imec. (2023). 2D-material based devices in the logic scaling roadmap.  
https://www.imec-int.com/en/articles/introducing-2d-material-based-devices-logic-scaling-roadmap

[19] O'Brien, K. P., et al. (2021). Advancing 2D Monolayer CMOS Through Contact, Channel and Interface Engineering. *IEEE IEDM 2021*.  
https://ieeexplore.ieee.org/document/9720651

[20] Chuang, H.-J., et al. (2016). Low-Resistance 2D/2D Ohmic Contacts: A Universal Approach to High-Performance WSe₂, MoS₂, and MoSe₂ Transistors. *Nano Letters*, 16, 1896–1902.  
https://pubs.acs.org/doi/10.1021/acs.nanolett.5b05066

[21] Challenges and prospects of 2D electronics for future monolithic complementary field-effect transistors. *Nature Communications*, 17, 71986 (2026).  
https://www.nature.com/articles/s41467-026-71986-9

[22] The contacts between two-dimensional materials and metal electrodes. *Nano Research* (2026).  
https://www.sciopen.com/article/10.26599/NR.2026.94908584

[23] Reducing the contact resistance in 2D semiconducting transistors. *Physics World*.  
https://physicsworld.com/a/reducing-the-contact-resistance-in-2d-semiconducting-transistors

[24] Low Contact Resistance on Monolayer MoS₂ Field-Effect Transistors Achieved by CMOS-Compatible Metal Contacts. *ACS Nano*, 18(33), 22444–22453 (2024).  
https://pubs.acs.org/doi/10.1021/acsnano.4c07267

[25] The Roadmap of 2D Materials and Devices Toward Chips. *Nano-Micro Letters*, 16, 12 (2024).  
https://link.springer.com/article/10.1007/s40820-023-01273-5

[26] Self-passivation reduces the Fermi level pinning in the metal-semiconductor contacts. *Nature Communications*, 16, 65695 (2025).  
https://www.nature.com/articles/s41467-025-65695-y

[27] Contact engineering for two-dimensional van der Waals materials. *Materials Science and Engineering: R*, 160, 100794 (2025).  
https://www.sciencedirect.com/science/article/pii/S2772949424000445

[28] Study of gold and bismuth electrical contacts to a MoS₂ monolayer. *arXiv:2501.07444* (2025).  
https://arxiv.org/html/2501.07444v1

[29] Fermi Level Depinning in Two-Dimensional Materials Using a Dielectric Interlayer. *ACS Applied Electronic Materials*, 4(8), 3720–3729 (2022).  
https://pubs.acs.org/doi/10.1021/acsaelm.2c00609

[30] Engineering of metal-MoS₂ contacts to overcome Fermi level pinning. *Solid-State Electronics*, 200, 108372 (2023).  
https://www.sciencedirect.com/science/article/abs/pii/S0038110122001502

