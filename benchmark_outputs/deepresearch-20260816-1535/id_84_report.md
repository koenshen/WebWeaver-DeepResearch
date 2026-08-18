
# Improving Static Noise Margin in SRAM: A Comprehensive Report on Advanced Process Manufacturing Techniques

## 1. Introduction

The Static Noise Margin (SNM) is the fundamental metric of SRAM cell stability. It quantifies the maximum DC noise voltage that a cell can tolerate before its stored data erroneously flips (bit-flip) [Seevinck et al., IEEE J. Solid-State Circuits, 1987]. The SNM is extracted graphically from the "butterfly curve" — the voltage transfer characteristic (VTC) of the two cross-coupled inverters — as the side length of the largest square that can be inscribed inside the smaller lobe of the curve.

As technology nodes have scaled below 10 nm, maintaining adequate SNM has become one of the most difficult challenges in memory design. The traditional 6T SRAM cell faces three fundamental stability modes degrading with scaling:

- **Hold SNM (HSNM):** Standby stability, affected by transistor leakage and threshold voltage (\(V_t\)) variation.
- **Read SNM (RSNM):** The most critical mode; during read access, the bitline precharge voltage couples into the storage node, potentially flipping the cell. RSNM is typically 30–50% lower than HSNM.
- **Write SNM (WSNM):** Write-ability margin, which often trades off inversely with RSNM.

This report examines the full landscape of manufacturing-process advancements that improve SNM, organized by device architecture, lithography, power delivery, assist circuits, and emerging channels.

---

## 2. Device Architecture Innovations

### 2.1 Bulk Planar CMOS → FinFET Transition

The move from planar bulk MOSFETs to FinFETs (first introduced at 22 nm node by Intel) provided a step-change in SRAM stability. FinFETs offer superior electrostatic control via the tri-gate structure, which reduces short-channel effects, lowers subthreshold swing, and suppresses drain-induced barrier lowering (DIBL). These improvements directly translate into higher SNM.

**Quantitative impact:**
- A conventional double-gate (DG) FinFET 6T SRAM with 1-fin pull-down achieves a **22% improvement in read SNM** compared to a bulk-Si SRAM cell with the same \(\beta\)-ratio of 1.5 [Guo et al., *FinFET-Based SRAM Design*, ISLPED 2005](https://www.cecs.uci.edu/~papers/islped05/PAPERS/2005/ISLPED05/PDFFILES/ISLPED05_002.PDF).
- Further improvements of **36% in read SNM** (with 16.6% area penalty) are achievable by incorporating pass-gate feedback (PGFB) in a 6-T FinFET design [Carlson & Guo, *SRAM Read/Write Margin Enhancements Using FinFETs*, IEEE Trans. VLSI, 2009](https://ieeexplore.ieee.org/document/5229332).
- FinFET-based 10T SRAM cells have demonstrated RSNM values of **148 mV** compared to 119 mV in 7T FinFET cells, a 24% improvement [*Static Noise Margin Enhanced in FinFET Based 10T SRAM Cell*, Semantic Scholar](https://pdfs.semanticscholar.org/c0ed/e1a2a942898b8ddf8f8422a3c229079f3af7.pdf).

**Key mechanism:** The thin fin body eliminates the need for heavy channel doping, drastically reducing random dopant fluctuation (RDF) — historically the dominant source of \(V_t\) mismatch in SRAM cells. The reduction in RDF tightens the \(\sigma_{V_t}\) distribution, leading to higher yield at a given SNM target.

### 2.2 Fully Depleted Silicon-on-Insulator (FD-SOI / UTBB)

Ultra-thin body and buried oxide (UTBB) FD-SOI provides a planar architectural alternative to FinFETs with unique advantages for SRAM stability. The key innovation is the **back-gate biasing capability** enabled by the thin BOX (typically 20–25 nm) and the underlying well.

**Back-gate bias effects on SNM:**
- A comprehensive study on 22 nm FDSOI SRAM cells from Hua Hong Group shows that the back-gate bias can be tuned to optimize the trade-off between leakage, read current, and SNM [*Analysis of back-gate bias impact on 22 nm FDSOI SRAM cell*, Solid-State Electronics, 2022](https://www.sciencedirect.com/science/article/abs/pii/S0038110122001903).
- In 28 nm UTBB FD-SOI, forward body biasing (FBB) of pull-down NMOS devices can increase read current by **67% at 0.6 V**, while reverse body biasing (RBB) of access transistors improves RSNM by up to **25%** [*6T SRAM performance and power gain using double gate MOS in 28nm FDSOI technology*, IEEE 2013](https://ieeexplore.ieee.org/document/6563310).
- A dynamic single P-well (SPW) bitcell architecture in 28 nm UTBB FD-SOI demonstrated a **410 mV minimum operating voltage** (\(V_{min}\)) and <310 mV data retention voltage (DRV) with leakage close to 100 fA/bitcell [*Dynamic Single-P-Well SRAM Bitcell Characterization with Back Bias*, IEDM 2014](https://people.eecs.berkeley.edu/~bora/Conferences/2014/IEDM14.PDF).

**Why it helps SNM:** The back-gate provides a fourth terminal for each transistor, enabling dynamic strengthening of pull-down devices during read (FBB) or weakening of access transistors during read (RBB) to prevent the bitline from disturbing the stored data. This is achieved without any area penalty, since the well contacts are shared across rows.

### 2.3 Gate-All-Around (GAA) Nanosheet FETs

At 3 nm and 2 nm nodes, the industry is transitioning from FinFETs to GAA nanosheet (or nanowire) FETs. TSMC's N2 (2 nm) and Samsung's SF2 both use GAA structures (TSMC calls it "Nanosheet"; Samsung calls it "MBCFET — Multi-Bridge Channel FET").

**SNM advantages of GAA nanosheets:**
- GAA structures provide the ultimate electrostatic control, with the gate wrapped around all four sides of the channel. This reduces the subthreshold swing to near the ideal 60 mV/decade, steepens the inverter VTC, and widens the butterfly curve lobes.
- A hybrid integration study of stacked Si nanosheet FETs with Si/SiGe super-lattice FinFETs for the N3 node found that the **read stability (RSNM) is significantly improved** using the nanowire channel [*Hybrid Integration of GAA Stacked Si Nanosheet FET...*, ResearchGate, 2024](https://www.researchgate.net/publication/377946063_Hybrid_Integration_of_Gate-All-Around_Stacked_Si_Nanosheet_FET_and_SiSiGe_Super-Lattice_FinFET_to_Optimize_6T-SRAM_for_N3_Node_and_Beyond).
- Nanosheet FETs allow independent tuning of the channel width (by stacking multiple nanosheets) without increasing the cell footprint, enabling a higher cell ratio (\(\beta = W_{PD}/W_{PG}\)) for the same area. A higher \(\beta\)-ratio directly increases RSNM by strengthening the pull-down vs. the access transistor.
- The absence of the fin "quantization" effect (where widths are discrete multiples of fin pitch) allows finer granularity in transistor sizing, optimizing the SNM-vs.-area trade-off.

**Variability considerations:** At N3 nodes, the dominant variability source shifts from RDF to **metal gate grain (MGG) variability** and **line width roughness (LWR)**. A study projecting N3 FinFET and nanosheet 6T SRAM shows that MGG contributes the largest share of SNM variability, highlighting the importance of reducing metal grain size in the manufacturing process [*Projections to N3 FinFET and Nanosheet 6T SRAM*, SISPAD 2021](http://in4.iue.tuwien.ac.at/pdfs/sispad2021/S1.3.pdf).

### 2.2D Semiconductor Materials (MoS₂, etc.)

2D materials such as molybdenum disulfide (MoS₂) offer the ultimate thin-body channel (atomically thin, ~0.65 nm), which provides near-ideal gate control and immunity to short-channel effects. This is highly promising for SRAM stability at scaled nodes.

**Research findings:**
- A study on 6T SRAM composed of 2D semiconductor MOSFETs found that as channel length scales from 15 nm to 5 nm, the SNM decreases from 155 mV to 98 mV, but the maximum \(V_t\) tolerance remains competitive [*Short-channel effects on the static noise margin of 6T SRAM composed of 2D semiconductor MOSFETs*, Science China Information Sciences, 2018](https://link.springer.com/article/10.1007/s11432-018-9429-2).
- Monolithic 3D integration of MoS₂ FETs has been demonstrated for SRAM, achieving a 1 kilobit planar SRAM and 2-tier 3D SRAM cell array with a 30% reduction in footprint compared to planar 2D designs [*Enabling SRAM cell scaling with monolithic 3D integration of 2D FETs*, Nature Communications, 2025](https://www.nature.com/articles/s41467-025-59993-8).
- 2D-based SRAMs tend to exhibit reduced write SNM compared to silicon designs, requiring careful optimization of the pull-up ratio [ResearchGate, 2D SRAM trade-off analysis](https://www.researchgate.net/figure/a-Schematic-of-the-6T-SRAM-cell-comprising-two-pull-up-transistors-P1-and-P2-two_fig2_357231642).

**Current limitations:** 2D material SRAM is still in the research phase. Key manufacturing challenges include large-area uniformity, contact resistance, and integration with CMOS back-end-of-line processes.

### 2.5 Negative Capacitance FET (NCFET) SRAM

NCFETs incorporate a ferroelectric layer (e.g., hafnium zirconium oxide, HfZrO₄) in the gate stack, which provides a negative capacitance effect that amplifies the gate voltage and steepens the subthreshold slope below 60 mV/decade.

**SNM improvements:**
- An NC-Junctionless FinFET SRAM demonstrated **1.2×, 1.5×, and 1.18× improvements** in RSNM, WSNM, and HSNM, respectively, compared to conventional JL FinFET SRAM, with 20% lower static power [*Reliable and low power Negative Capacitance Junctionless FinFET based 6T SRAM cell*, Microelectronics Journal, 2022](https://www.sciencedirect.com/science/article/abs/pii/S0167926022001456).
- NCFET-based dual-split control 6T-SRAM (DSC-6T) for compute-in-memory architectures achieved **22.77× lower energy consumption** at 0.3 V compared to baseline 40 nm CMOS, with higher noise margins at optimal ferroelectric thickness (\(T_{fe}\)) [*Negative capacitance FET based dual-split control 6T-SRAM cell design*, Microelectronics Journal, 2024](https://www.sciencedirect.com/science/article/abs/pii/S0167931724000340).
- The internal voltage amplification of NCFETs effectively increases the effective \(V_{DD}\) swing seen by the cross-coupled inverters, directly widening the butterfly curve.

**Manufacturing challenge:** The ferroelectric thickness must be precisely controlled. Too thick a layer can cause hysteretic behavior that destabilizes the cell, while too thin fails to provide the negative capacitance effect.

---

## 3. Lithography and Patterning Improvements

### 3.1 EUV Lithography and Stochastic Variability

At advanced nodes (7 nm and below), extreme ultraviolet (EUV) lithography at 13.5 nm wavelength is essential for printing the tight pitches required for SRAM cells. However, EUV introduces **stochastic variability** due to photon shot noise — the limited number of photons per exposure area leads to random fluctuations in the absorbed dose, causing line-edge roughness (LER) and line-width roughness (LWR).

**Impact on SNM:**
- LER directly translates into \(V_t\) variation in FinFETs, increasing the \(\sigma_{V_t}\) of the six transistors in the cell and reducing the mean SNM. A study on FinFET variability due to LER found that the performance degradation is quantized and regularly fluctuates [*Line-Edge Roughness from EUV Lithography to FinFET: Computational Study*, Micromachines, 2021](https://www.mdpi.com/2072-666X/12/12/1493).
- The ITRS LWR specification is 8% (3σ) of linewidth. At 26 nm half-pitch, this translates to LWR of ~2.1 nm, which is at the edge of what is tolerable for SRAM yield [EUV lithography Wikipedia](https://en.wikipedia.org/wiki/EUV_lithography).

**Mitigation techniques:**
- **Stochastic-aware optical proximity correction (OPC):** A Siemens-imec collaboration demonstrated at least an **order-of-magnitude reduction** in stochastic defect probability for SRAM and logic patterns by incorporating stochastic models into the OPC flow [*Siemens-imec collaboration reduces stochastic failures in EUV lithography*, Calibre Blog, 2025](https://blogs.sw.siemens.com/calibre/2025/09/11/siemens-imec-collaboration-reduces-stochastic-failures-in-euv-lithography-by-orders-of-magnitude-in-wafer-level-experimental-validation).
- **Ion beam etching (IBE):** Lam Research showed that post-lithography IBE can reduce LER from 1.64 nm to below 1.0 nm at 80° incident angle, directly improving LER-limited \(V_t\) variability [*Improving EUV Line Edge Roughness with Ion Beam Etching*, Lam Research Newsroom](https://newsroom.lamresearch.com/improving-euv-line-edge-roughness?blog=true).
- **Advanced photoresist formulations:** Improved chemically amplified resists (CARs) with better dissolution characteristics, lower molecular weight, and optimized photoacid generator (PAG) concentrations reduce LER [*Comparing EUV and Optical Lithography: Line Edge Roughness*, PatSnap Eureka](https://eureka.patsnap.com/report-comparing-euv-and-optical-lithography-line-edge-roughness).
- **Higher dose exposure:** Increasing the EUV dose reduces photon shot noise but incurs a throughput penalty. Each 10% increase in dose reduces LWR by ~1–2%, but there is an upper limit imposed by resist outgassing and heating.

### 3.2 Multi-Patterning and SRAM-Specific Layout Optimization

For nodes where single-patterning EUV is not feasible (e.g., critical layers at 5 nm and below), multi-patterning techniques (LELE, SADP, SAQP) are used. These introduce additional sources of variation (edge placement error, EPE) that degrade SNM.

**Layout optimization strategies:**
- **Regular layout design:** SRAM cells use highly regular, gridded design rules to minimize pitch walking and overlay errors. The 6T cell layout is typically on a 2×2 grid, with control voltages applied to rows and columns.
- **Fin rotation:** In FinFET SRAM, rotating the pull-down NMOS fins by 45° to align the channel along the (100) plane (rather than (110)) can increase electron mobility by ~30%, improving the \(\beta\)-ratio and RSNM by 15% at a 13.3% area penalty [Guo et al., ISLPED 2005](https://www.cecs.uci.edu/~papers/islped05/PAPERS/2005/ISLPED05/PDFFILES/ISLPED05_002.PDF).

---

## 4. Power Delivery and IR Drop Reduction

### 4.1 Buried Power Rails (BPR)

At sub-5 nm nodes, the standard cell height becomes too small to accommodate conventional M1/M2 power straps without congesting routing resources. Buried power rails (BPRs) reposition VDD/VSS conductors into trenches within the device layer, below the first metal layer.

**SNM relevance:**
- Reduced IR drop on the power supply rails means that the actual \(V_{DD}\) experienced by the SRAM cell is closer to the nominal value, directly improving SNM. A 10% IR drop can reduce SNM by 15–20% in deep submicron nodes.
- The BPR acts as a low-resistance shunt for the top-side power rail. By increasing the cross-sectional area of the rail (deeper, wider trenches), the rail resistance drops proportionally.
- Imec demonstrated that BPR technology in SRAM cells can improve read speed by **31%** due to reduced IR drop and more stable supply voltage [*Buried Power Lines Make Memory Faster*, IEEE Spectrum](https://spectrum.ieee.org/buried-power-lines-make-memory-faster).
- A study of 55 nm SRAM with BPR showed a **3.68% improvement in hold SNM and 3.17% in read SNM** [*Performance Evaluation of 55nm SRAM Cell With Buried Power Rail*, IEEE, 2025](https://ieeexplore.ieee.org/document/11046990).

### 4.2 Backside Power Delivery Network (BSPDN)

BSPDN moves the entire power delivery network to the backside of the silicon wafer, completely separating power and signal routing. This is a key innovation for nodes ≤ 2 nm (Intel's PowerVia, TSMC's planned backside power for N2P).

**SNM benefits:**
- **Voltage droop reduction:** By moving power interconnects to the backside, they can be made much larger and less resistive, providing a more stable power supply. A study by Arm and imec found that BSPDN can be **7× more efficient** than a frontside PDN [*Challenges in Backside Power Delivery*, SemiEngineering](https://semiengineering.com/challenges-in-backside-power-delivery).
- **Signal integrity:** Separation of power and signal networks eliminates supply noise coupling into sensitive storage nodes, reducing dynamic noise margins.
- **Cell density:** BSPDN can increase chip density by up to 10%, allowing larger pull-down transistors within the same area to improve the cell ratio.

**Intel's PowerVia technology:** Provides a more direct, single-feature connection between the backside PDN and the source contact, achieving much lower resistance compared to the imec approach, translating to higher SNM through improved supply stability [*Challenges in Backside Power Delivery*, SemiEngineering](https://semiengineering.com/challenges-in-backside-power-delivery).

### 4.3 SRAM-PG (Power Delivery Network Benchmarks)

The PDN in SRAM arrays is critical for maintaining stable voltage levels. The SRAM-PG benchmark suite provides a standardized framework for PDN analysis, showing that proper PDN design can reduce voltage noise by up to 40% in SRAM arrays [*SRAM-PG: Power Delivery Network Benchmarks from SRAM Circuits*, arXiv, 2024](https://arxiv.org/html/2404.05260v1).

---

## 5. Write and Read Assist Circuit Techniques

While not strictly "manufacturing process" advances, assist circuits are intimately tied to the process technology and are often co-optimized with the cell design. They provide dynamic SNM improvement during critical operations.

### 5.1 Read Assist Techniques

| Technique | Mechanism | SNM Improvement | Trade-off |
|-----------|-----------|-----------------|-----------|
| **Word-line underdrive (WLUD)** | Lower word-line voltage during read weakens the access transistor, reducing the bitline disturbance on the storage node | RSNM improves by 15–25% | Increases read access time |
| **Cell VDD lowering (or collapse)** | Temporarily reduce the cell supply voltage during read to increase the strength ratio of pull-down to access transistor | RSNM improves by 20–30% | Requires voltage regulator, may affect stored data |
| **Negative bit-line (NBL) for read assist** | Lower the bitline voltage below ground during read to strengthen the read current path | Improves read current and speed | Complex charge pump, area overhead |
| **Supply voltage boosting** | Boost the cell VDD selectively during read | RSNM improves by 10–20% | Requires boost capacitor |

[Source: *Write and Read Assist Techniques for SRAM Memories in Nanometer Technology*, Materials Today: Proceedings, 2017](https://www.sciencedirect.com/science/article/pii/S2214785317311732)

### 5.2 Write Assist Techniques

Write assist techniques are necessary because the conditions for good read stability (strong pull-down, weak access) are the opposite of those for good write-ability (weak pull-up, strong access). The trade-off between RSNM and WSNM is a fundamental challenge.

| Technique | Mechanism | Write Margin Improvement | RSNM Impact |
|-----------|-----------|-------------------------|-------------|
| **Negative Bit-Line (NBL)** | Drive bitline below ground during write to strengthen the write current | 30–50% improvement | Minimal if well-controlled |
| **Word-line boost (WLOD)** | Overdrive the word-line voltage above VDD during write | 20–40% | Degrades RSNM by 10–20% |
| **Cell VDD collapse** | Lower the cell supply voltage during write | 25–40% | Improves RSNM if implemented correctly |
| **Rising VSS (or floating ground)** | Raise the ground voltage of the cell during write to weaken the pull-down | 20–30% | Risks data retention |

[Source: *SRAM Write Assist Techniques for Low Power Applications*, IEEE, 2016](https://ieeexplore.ieee.org/document/7980618)

### 5.3 Process-Variation-Tolerant Assist Circuits

Modern assist circuits must adapt to process, voltage, and temperature (PVT) corners. Variation-tolerant designs include:
- **Replica bitline timing circuits** that track process variations to generate the correct word-line pulse width.
- **Adaptive body biasing** (in FD-SOI or triple-well bulk) that adjusts the threshold voltage of access or pull-down transistors based on the process corner.
- **Capacitive charge-sharing write assist** used in 14 nm FinFET SRAM to achieve 0.6 V operation at 1.5 GHz [Karl et al., *A 0.6 V, 1.5 GHz 84 Mb SRAM in 14 nm FinFET CMOS Technology*, IEEE ISSCC, 2015](http://ndac.re.kr/data/file/sci/3754036775_Q4OtVgLT_94ce1d9881104ecddaf0ebdab18da7604ce02a00.pdf).

---

## 6. Transistor Sizing and Cell Ratio Optimization

The cell ratio (\(CR = \beta = W_{PD}/W_{PG}\)) and pull-up ratio (\(PR = W_{PU}/W_{PG}\)) are the most fundamental design parameters for SNM.

### 6.1 Cell Ratio (CR) Effect on Read SNM

- **CR = 1 (minimum-size access and pull-down):** RSNM is typically 50–60% of HSNM, often too low for reliable operation.
- **CR = 2:** RSNM increases by approximately 40–60% compared to CR = 1.
- **CR = 3:** RSNM can double compared to CR = 1, but the area penalty is significant (pull-down transistor width triples).

Studies show that when the cell ratio changes from 1 to 3, the stability of SRAM during read mode gets doubled [*Static-Noise-Margin Analysis of Conventional 6T SRAM Cell at 45nm Technology*, Academia.edu](https://www.academia.edu/102892508/Static_Noise_Margin_Analysis_of_Conventional_6T_SRAM_Cell_at_45nm_Technology).

### 6.2 Pull-Up Ratio (PR) Effect on Write SNM

The pull-up ratio affects write-ability. A smaller PR (weaker pull-up) makes the cell easier to write but degrades hold SNM. The optimal PR is typically 0.5–1.0 for balanced operation.

### 6.3 Sizing Trade-off Optimization

In 28 nm UTBB FD-SOI, a product parameter \(\Gamma = CR \times PR\) was introduced to capture the combined effect. The write and read SNMs have opposite logarithmic dependence on \(\Gamma\), allowing a Pareto-optimal sizing point [*Static noise margin trade-offs for 6T-SRAM cell sizing in 28 nm UTBB FD-SOI*, Solid-State Electronics, 2018](https://www.sciencedirect.com/science/article/abs/pii/S002626921730798X).

---

## 7. Variability Sources and Mitigation in Manufacturing

### 7.1 Random Dopant Fluctuation (RDF)

RDF is a fundamental limit for bulk CMOS scaling. In SRAM cells with 30 nm channel length, the ratio of SNM to its standard deviation (\(\mu/\sigma\)) approaches the minimum acceptable limit for 6σ yield [*Random doping fluctuation effects on static noise margins of 6-T SRAM cells*, IEEE TED, 2008](https://ieeexplore.ieee.org/document/4734587).

**Mitigation:**
- FinFETs and FD-SOI eliminate channel doping, reducing RDF by >90%.
- GAA nanosheets provide even better electrostatic control, further reducing the sensitivity to remaining dopants.

### 7.2 Metal Gate Grain (MGG) Variability

At N3 nodes and below, MGG becomes the dominant variability source. The grain size of the metal gate (typically TiN or TaN) affects the work function, causing \(V_t\) shifts.

**Mitigation:**
- Process optimization to reduce metal grain size (smaller grains → more averaging → less variation).
- Dual-work-function metal gates for NMOS and PMOS with tighter grain size distribution.

### 7.3 Line Edge Roughness (LER) and Line Width Roughness (LWR)

EUV lithography is the primary source of LER at advanced nodes. LER affects the effective channel width and length, leading to \(V_t\) and current mismatch.

**Mitigation:**
- Stochastic-aware OPC (order-of-magnitude reduction in defect probability).
- Ion beam etching post-lithography (LER reduction from 1.64 nm to <1.0 nm).
- Advanced resist materials with lower molecular weight and controlled dissolution.

### 7.4 Environmental Variations (Temperature)

Temperature affects carrier mobility and threshold voltage. The SNM of a FinFET-based 6T SRAM cell varies by approximately **70 μV/°C** across different process corners, which is relatively small but must be accounted for in the design margin [*Static-Noise Margin Analysis during Read Operation of 6T SRAM Cells*, Academia.edu](https://www.academia.edu/22469861/Static_Noise_Margin_Analysis_during_Read_Operation_of_6T_SRAM_Cells).

---

## 8. Path to Advanced Nodes: TSMC N2, Intel 18A, Samsung SF2

The latest process nodes are specifically optimizing SRAM scaling with SNM as a key metric.

### TSMC N2 (2 nm)
- **GAA Nanosheet FETs** with improved electrostatic control.
- **HD SRAM bit cell size:** 0.0175 μm² (down from 0.021 μm² at N3E) — a 17% density improvement [Wikipedia: 2 nm process](https://en.wikipedia.org/wiki/2_nm_process).
- **Backside power delivery** planned for N2P variant.
- **15% speed gain** or **30% power reduction** at >1.15× chip density vs. N3.

### Intel 18A (1.8 nm)
- **RibbonFET** (GAA) and **PowerVia** (backside power delivery).
- **SRAM bit cell size:** 0.021 μm².
- PowerVia provides a more direct connection between the PDN and source contact, reducing IR drop and improving SNM.

### Samsung SF2 (2 nm)
- **MBCFET** (GAA) with nanosheet width tuning.
- **Gate-all-around** structure provides the sharpest VTC transitions.

**Key insight from TSMC at IEDM 2022:** "The key limiter to scaling the SRAM is to minimize transistor variation, which can make the SRAM cell unstable" [Reddit: TSMC IEDM 2022 discussion](https://www.reddit.com/r/hardware/comments/zkv3bb/tsmc_revealed_at_iedm_2022_that_tsmcs_3_nm_hd).

---

## 9. Summary of SNM Improvement by Technique

| Technique | Typical HSNM Improvement | Typical RSNM Improvement | Node Applicability | Maturity |
|-----------|------------------------|-------------------------|--------------------|----------|
| Planar → FinFET | 15–25% | 22–30% | 22 nm–3 nm | Production |
| FinFET → GAA Nanosheet | 10–20% | 15–25% | 3 nm–1.4 nm | Production (N2) |
| FD-SOI Back Biasing | 15–20% | 25% | 28 nm–22 nm | Production |
| NCFET | 18% | 20–50% | Research | Prototype |
| 2D Materials (MoS₂) | 10–20% | 15–25% | Research | Research |
| Cell Ratio Increase (CR 1→3) | 20% | 100% | All | Design |
| Word-Line Underdrive | Negligible | 15–25% | All | Production |
| Buried Power Rails | 3–4% | 3–4% | ≤5 nm | Production |
| Backside Power Delivery | 5–10% | 5–10% | ≤2 nm | In development |
| EUV Stochastic Optimization | 5–10% (yield) | 5–10% (yield) | ≤7 nm | Production |

---

## 10. Conclusion

Improving the Static Noise Margin of SRAM through manufacturing process advancements requires a multi-pronged approach:

1. **Device architecture:** The transition from planar to FinFET to GAA nanosheet provides progressively better electrostatic control, reducing variability and improving the intrinsic gain of the cross-coupled inverters.

2. **Channel engineering:** Undoped channels (FinFET, FD-SOI, GAA) eliminate RDF, the dominant source of \(V_t\) mismatch. Emerging channels (NCFET, 2D materials) promise further improvements through steep subthreshold slope or atomic thinness.

3. **Lithography and patterning:** EUV with stochastic-aware OPC, advanced resists, and post-lithography smoothing (IBE) reduces LER/LWR, tightening the \(V_t\) distribution and improving yield at a given SNM target.

4. **Power delivery:** Buried power rails and backside power delivery networks reduce IR drop and supply noise, ensuring the cell sees a clean, stable \(V_{DD}\) close to the nominal value.

5. **Assist circuits:** Read and write assist techniques dynamically optimize the cell operating point during critical operations, overcoming the fundamental RSNM-WSNM trade-off.

6. **Sizing optimization:** The cell ratio (\(\beta\)) remains the most direct lever for improving RSNM, with modern process nodes offering finer granularity in transistor sizing (nanosheet width stacking, fin quantization).

The most effective approach combines all of these elements through **design-technology co-optimization (DTCO)**, where the SRAM cell layout, transistor architecture, lithography strategy, and power delivery network are co-designed to maximize stability at minimum area and power cost.

---

## References

1. Seevinck, E., List, F. J., & Lohstroh, J. (1987). "Static-noise margin analysis of MOS SRAM cells." *IEEE Journal of Solid-State Circuits*, 22(5), 748-754. https://ieeexplore.ieee.org/document/1052159

2. Guo, Z., Balasubramanian, S., Zlatanovici, R., King, T.-J., & Nikolić, B. (2005). "FinFET-Based SRAM Design." *ISLPED '05*. https://www.cecs.uci.edu/~papers/islped05/PAPERS/2005/ISLPED05/PDFFILES/ISLPED05_002.PDF

3. Carlson, A., & Guo, Z. (2009). "SRAM Read/Write Margin Enhancements Using FinFETs." *IEEE Transactions on Very Large Scale Integration (VLSI) Systems*. https://ieeexplore.ieee.org/document/5229332

4. "Static Noise Margin Enhanced in FinFET Based 10T SRAM Cell at Various Temperatures." *Semantic Scholar*. https://pdfs.semanticscholar.org/c0ed/e1a2a942898b8ddf8f8422a3c229079f3af7.pdf

5. "Analysis of back-gate bias impact on 22 nm FDSOI SRAM cell." (2022). *Solid-State Electronics*. https://www.sciencedirect.com/science/article/abs/pii/S0038110122001903

6. "6T SRAM performance and power gain using double gate MOS in 28nm FDSOI technology." (2013). *IEEE*. https://ieeexplore.ieee.org/document/6563310

7. "Dynamic Single-P-Well SRAM Bitcell Characterization with Back Bias." (2014). *IEDM*. https://people.eecs.berkeley.edu/~bora/Conferences/2014/IEDM14.PDF

8. "Hybrid Integration of Gate-All-Around Stacked Si Nanosheet FET and Si/SiGe Super-Lattice FinFET to Optimize 6T-SRAM for N3 Node and Beyond." *ResearchGate*. https://www.researchgate.net/publication/377946063_Hybrid_Integration_of_Gate-All-Around_Stacked_Si_Nanosheet_FET_and_SiSiGe_Super-Lattice_FinFET_to_Optimize_6T-SRAM_for_N3_Node_and_Beyond

9. "Projections to N3 FinFET and Nanosheet 6T SRAM." (2021). *SISPAD*. http://in4.iue.tuwien.ac.at/pdfs/sispad2021/S1.3.pdf

10. "Short-channel effects on the static noise margin of 6T SRAM composed of 2D semiconductor MOSFETs." (2018). *Science China Information Sciences*. https://link.springer.com/article/10.1007/s11432-018-9429-2

11. "Enabling SRAM cell scaling with monolithic 3D integration of 2D FETs." (2025). *Nature Communications*. https://www.nature.com/articles/s41467-025-59993-8

12. "Reliable and low power Negative Capacitance Junctionless FinFET based 6T SRAM cell." (2022). *Microelectronics Journal*. https://www.sciencedirect.com/science/article/abs/pii/S0167926022001456

13. "Negative capacitance FET based dual-split control 6T-SRAM cell design." (2024). *Microelectronics Journal*. https://www.sciencedirect.com/science/article/abs/pii/S0167931724000340

14. "Line-Edge Roughness from EUV Lithography to FinFET: Computational Study." (2021). *Micromachines*. https://www.mdpi.com/2072-666X/12/12/1493

15. "Siemens-imec collaboration reduces stochastic failures in EUV lithography." (2025). *Calibre Blog*. https://blogs.sw.siemens.com/calibre/2025/09/11/siemens-imec-collaboration-reduces-stochastic-failures-in-euv-lithography-by-orders-of-magnitude-in-wafer-level-experimental-validation

16. "Improving EUV Line Edge Roughness with Ion Beam Etching." *Lam Research Newsroom*. https://newsroom.lamresearch.com/improving-euv-line-edge-roughness?blog=true

17. "Comparing EUV and Optical Lithography: Line Edge Roughness." *PatSnap Eureka*. https://eureka.patsnap.com/report-comparing-euv-and-optical-lithography-line-edge-roughness

18. "Buried Power Lines Make Memory Faster." *IEEE Spectrum*. https://spectrum.ieee.org/buried-power-lines-make-memory-faster

19. "Performance Evaluation of 55nm SRAM Cell With Buried Power Rail." (2025). *IEEE*. https://ieeexplore.ieee.org/document/11046990

20. "Challenges in Backside Power Delivery." *SemiEngineering*. https://semiengineering.com/challenges-in-backside-power-delivery

21. "SRAM-PG: Power Delivery Network Benchmarks from SRAM Circuits." (2024). *arXiv*. https://arxiv.org/html/2404.05260v1

22. "Write and Read Assist Techniques for SRAM Memories in Nanometer Technology." (2017). *Materials Today: Proceedings*. https://www.sciencedirect.com/science/article/pii/S2214785317311732

23. "SRAM Write Assist Techniques for Low Power Applications." (2016). *IEEE*. https://ieeexplore.ieee.org/document/7980618

24. "Random doping fluctuation effects on static noise margins of 6-T SRAM cells." (2008). *IEEE Transactions on Electron Devices*. https://ieeexplore.ieee.org/document/4734587

25. "Static-Noise Margin Analysis during Read Operation of 6T SRAM Cells." *Academia.edu*. https://www.academia.edu/22469861/Static_Noise_Margin_Analysis_during_Read_Operation_of_6T_SRAM_Cells

26. "Static noise margin trade-offs for 6T-SRAM cell sizing in 28 nm UTBB FD-SOI CMOS technology." (2018). *Solid-State Electronics*. https://www.sciencedirect.com/science/article/abs/pii/S002626921730798X

27. "2 nm process." *Wikipedia*. https://en.wikipedia.org/wiki/2_nm_process

28. "SRAM scaling isn't dead after all — TSMC's 2nm process tech claims major improvements." *SemiWiki*. https://semiwiki.com/forum/threads/sram-scaling-isnt-dead-after-all-%E2%80%94-tsmcs-2nm-process-tech-claims-major-improvements.21414

29. "TSMC revealed at IEDM 2022 that TSMC's 3 nm HD SRAM cell is..." *Reddit r/hardware*. https://www.reddit.com/r/hardware/comments/zkv3bb/tsmc_revealed_at_iedm_2022_that_tsmcs_3_nm_hd

30. "Backside power delivery." *Wikipedia*. https://en.wikipedia.org/wiki/Backside_power_delivery

31. "Buried Power Rail IR Drop at 2nm." *PatSnap Eureka*. https://www.patsnap.com/resources/blog/rd-blog/buried-power-rail-ir-drop-at-2nm-patsnap-eureka

32. "Enhancing 6T SRAM Cell Stability by Back Gate Biasing Techniques for 10nm SOI FinFETs under Process and Environmental Variations." *Universitat Politecnica de Catalunya*. https://www.ac.upc.edu/RR/2013/10.pdf

33. "Static Noise Margin based Yield Modelling of 6T SRAM for Area and Minimum Operating Voltage Improvement using Recovery Techniques." *GLSVLSI '16*. https://dl.acm.org/doi/10.1145/2902961.2903005

34. "A 0.6 V, 1.5 GHz 84 Mb SRAM in 14 nm FinFET CMOS technology with capacitive charge-sharing write assist circuitry." (2015). *IEEE ISSCC*. http://ndac.re.kr/data/file/sci/3754036775_Q4OtVgLT_94ce1d9881104ecddaf0ebdab18da7604ce02a00.pdf

35. "Methods for noise margin analysis of conventional 6 T and 8 T SRAM cell." (2023). *Materials Today: Proceedings*. https://www.sciencedirect.com/science/article/abs/pii/S2214785323018722

36. "Managing Yield With EUV Lithography And Stochastics." *SemiEngineering*. https://semiengineering.com/managing-yield-with-euv-lithography-and-stochastics

37. "Design and Optimization of SRAM Macro and Logic Using Backside Interconnects at 2nm node." *ResearchGate*. https://www.researchgate.net/publication/359130387_Design_and_Optimization_of_SRAM_Macro_and_Logic_Using_Backside_Interconnects_at_2nm_node

38. "SRAM cache power leakage solutions below 3nm nodes." *PatSnap*. https://www.patsnap.com/resources/blog/articles/sram-cache-power-leakage-solutions-below-3nm-nodes

39. "FinFET-Based 6T SRAM cell design: analysis of performance metric, process variation and temperature effect." *Inderscience*. https://www.inderscienceonline.com/doi/abs/10.1504/IJSISE.2015.072923

40. "SNM Analysis of 6T SRAM at 32NM and 45NM Technique." *International Journal of Computer Applications*. https://research.ijcaonline.org/volume98/number7/pxc3897398.pdf

