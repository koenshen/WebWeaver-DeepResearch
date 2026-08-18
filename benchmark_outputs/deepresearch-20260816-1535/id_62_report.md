
# Scaling Ion Trap Quantum Computing: Strategies, Feasibility, and Outlook

## 1. Introduction

Ion trap quantum computing has long been recognized as one of the most promising platforms for building a fault-tolerant quantum computer. Trapped ions offer exquisite coherence properties, naturally identical qubits, and the highest-fidelity quantum gates of any physical modality. However, the central challenge has always been **scaling**: moving from small demonstrations of 5–30 qubits to the millions of physical qubits required for practically useful, error-corrected computation.

This report examines the major proposed scaling strategies, assesses their feasibility based on current technological progress, and evaluates which approaches are most likely to succeed. The analysis draws on the latest publicly available data from leading companies and academic groups, including Quantinuum, IonQ, Universal Quantum, Oxford Ionics, ETH Zurich, and others.

---

## 2. The Core Scaling Challenge

In a conventional linear ion trap, qubits are confined in a single string. Multi-qubit gates are performed by exciting collective motional modes of the entire chain. As the number of ions increases, the motional mode spectrum becomes densely packed, making it exponentially harder to address individual modes without crosstalk. In practice, single-chain traps become impractical beyond roughly 30–50 ions [^nature2023scaling]. Moreover, the control electronics, laser delivery optics, and vacuum requirements all become increasingly complex as the system grows.

The field has converged on several approaches to circumvent these limitations, each with its own engineering trade-offs.

---

## 3. The QCCD Architecture: Shuttling as a Scaling Path

### 3.1 Principle

The Quantum Charge-Coupled Device (QCCD) architecture, proposed in 2002 by Kielpinski, Monroe, and Wineland, is the most mature and commercially advanced scaling approach [^kielpinski2002]. In QCCD, ions are not confined to a single chain. Instead, they are held in a multi-zone trap with dedicated **memory regions**, **gate regions**, **readout zones**, and **loading zones**. Ions are physically shuttled between zones by dynamically varying DC electrode voltages. This allows the system to maintain small, manageable ion crystals for high-fidelity operations while using transport to achieve all-to-all connectivity.

### 3.2 Quantinuum: The Leading QCCD Implementation

Quantinuum (formed from the merger of Honeywell Quantum Solutions and Cambridge Quantum) has executed the QCCD vision more aggressively than any other organization. Their commercial systems have evolved through three generations:

| System | Year | Qubits | Key Features | Reported Fidelities |
|--------|------|--------|--------------|---------------------|
| H1 | 2021 | 20 | Linear trap, Yb⁺ qubits | 99.997% 1Q, 99.8% 2Q |
| H2 | 2023 | 56 | Race-track trap, parallel gate zones | 99.998% 1Q, 99.8% 2Q |
| Helios | 2025 | 98 | Barium qubits, 4-way X-junction, ring storage | 99.9975% 1Q, 99.92% 2Q |

**Helios represents a major architectural leap.** Published in *Nature* in 2026, Helios uses ¹³⁷Ba⁺ hyperfine qubits and features a rotatable ion storage ring connected to two quantum logic regions via a four-way X-junction [^helios2026]. This design decouples memory storage from gate operations, enabling parallelized cooling and gating that increases effective clock speed. Key performance metrics:

- Average single-qubit gate infidelity: **2.5 × 10⁻⁵**
- Average two-qubit gate infidelity: **7.9 × 10⁻⁴**
- State preparation and measurement (SPAM) error: **3.3 × 10⁻⁴**
- 48 logical qubits demonstrated from 98 physical qubits using color codes — a **2:1 encoding ratio**, the best in the industry [^entangledfuture2026]

### 3.3 Solving the Wiring and Sorting Problems

In March 2024, Quantinuum announced a breakthrough that directly addresses two critical roadblocks to QCCD scaling: the "wiring problem" (each qubit requires numerous control signals) and the "sorting problem" (efficiently moving ions through junctions). Their solution uses a clever combination of a fixed number of analog signals with a single digital input per qubit, dramatically reducing control complexity. The scheme was demonstrated on three distinct systems, proving reproducibility [^quantinuum2024scaling].

### 3.4 Roadmap: Sol and Apollo

Quantinuum's roadmap extends to:

- **Sol (2027)**: Trap chip already fabricated, advancing through product validation
- **Apollo (2029)**: Next-generation system with significant architectural subsystems in prototyping

The company has partnered with **Infineon** (2024) to co-develop future ion trap chips leveraging Infineon's semiconductor manufacturing expertise, and with **Quanta Computer** (2026) to design modular, manufacturable infrastructure [^quantinuum-infineon2024][^quantinuum-quanta2026].

### 3.5 Assessment

**Strengths:** Highest gate fidelities in the industry; proven scaling from 20 to 98 qubits across three generations; best logical qubit encoding ratio; strong commercial traction ($8M quarterly revenue, +279% YoY).  
**Weaknesses:** Physical gate operations are slower than superconducting qubits (microseconds vs. nanoseconds); shuttling adds latency and potential heating; the architecture's ultimate limit for single-chip scaling is not yet known.

---

## 4. Photonic Interconnects and Modular Architectures

### 4.1 Principle

An alternative to shuttling all qubits within a single trap is to **network multiple smaller ion trap modules via photonic interconnects**. In this approach, each module contains a small number of high-fidelity qubits. Remote entanglement between modules is generated by collecting photons from ions, interfering them at a Bell-state analyzer, and heralding success. This enables distributed quantum computing across chips, analogous to how classical supercomputers network multiple nodes.

### 4.2 IonQ: The Modular Vision

IonQ has staked its entire scaling roadmap on photonic interconnects. The company's strategy is built on three pillars:

1. **High-fidelity single-chip modules** using "electronic quantum computing" (EQC) technology acquired from Oxford Ionics
2. **Photonic interconnects** acquired from Lightsynq for linking modules
3. **Reconfigurable Multicore Quantum Architecture (RMQA)** for flexible ion chain routing

**Key roadmap milestones (announced June 2025)** [^ionqroadmap2025]:

| Year | Physical Qubits | Logical Qubits | Enabling Technology |
|------|----------------|----------------|---------------------|
| 2025 | ~100 (Tempo) | — | EQC trap chip |
| 2027 | ~10,000 (single chip) | — | 2D ion trap array (300× density increase) |
| 2028 | ~20,000 (2 chips) | ~1,600 | Photonic interconnect between chips |
| 2030 | ≥2,000,000 (multi-module) | 40,000–80,000 | Fully networked modular system |

IonQ's **Oxford Ionics acquisition** brings a 2D ion trap technology that offers up to 300× higher trap density compared to linear 1D systems, while maintaining fidelity and parallel operation [^ionqblog2025]. The **Lightsynq acquisition** contributes quantum memory-based photonic interconnects that increase the ion-ion entanglement rate by up to 50× compared to memoryless solutions, making clustered quantum computing commercially viable.

In April 2026, IonQ demonstrated the **first photonic interconnection of two commercial trapped-ion quantum computers**, generating entanglement between two independent systems in collaboration with the Air Force Research Laboratory [^ionqphotonic2026].

### 4.3 Alternative Photonic Networking Approaches

**Nu Quantum** (Cambridge, UK) has opened a dedicated trapped-ion qubit networking lab focused on building a "Qubit-Photon Interface" (QPI) that enables modular scaling through an "Entanglement Fabric" technology roadmap [^nuquantum2026].

**Monroe group at Duke/IonQ** has demonstrated fast photon-mediated entanglement between continuously-cooled trapped ions at rates of 250 Hz with >97% fidelity, representing a six-order-of-magnitude improvement over two decades [^monroe2024].

### 4.4 Assessment

**Strengths:** Avoids the complexity of large single-chip traps; leverages existing semiconductor-like manufacturing for modules; naturally supports distributed and fault-tolerant architectures; enables scaling beyond the physical limits of a single chip.  
**Weaknesses:** Photonic entanglement rates are currently low (∼10–250 Hz), creating a bottleneck for algorithms requiring many remote operations; probabilistic entanglement generation adds overhead; the technology is less mature than QCCD shuttling; no commercial system yet operates with photonic interconnects at scale.

---

## 5. Microfabricated Ion Traps: The Hardware Foundation

All scaling approaches depend on advanced ion trap chip fabrication. The evolution of trap designs is itself a critical scaling strategy.

### 5.1 Surface-Electrode Traps

Surface-electrode (SE) traps place all electrodes in a single plane, with ions trapped 50–100 μm above the chip surface. This geometry is compatible with standard semiconductor fabrication processes and enables:

- Dense integration of electrodes and control lines
- Multi-zone architectures with junctions
- Integration of photonic waveguides and detectors

**Sandia National Laboratories** has been a leading supplier of high-quality surface traps, and their designs have been used by Quantinuum, IonQ, and numerous academic groups [^sandiatraps].

### 5.2 3D MEMS Traps

**Infineon Technologies** has developed industrially microfabricated ion traps using MEMS processes that achieve trap depths of ∼1 eV, an order of magnitude deeper than typical surface traps [^infineon2022]. This is critical for stable long-term operation. Infineon's traps have demonstrated parallel shuttling of two ion arrays with a storage capacity of 18 ions, and the company is working on cryogenic control electronics and optics integration for higher qubit counts [^infineon2024].

### 5.3 Universal Quantum: CMOS-Based Traps

**Universal Quantum** (UK) is pursuing a radical modular approach using CMOS fabrication to integrate advanced features. Their iQPU (integrated Quantum Processing Unit) design uses a large array of surface-electrode traps connected via junctions, supported by multiple interconnect layers. Individual iQPUs are connected using **UQConnect**, a microwave-based chip-link technology that has demonstrated record-breaking connection fidelities [^universalquantum2024]. The company has developed the first commercial ASIC for integration into their iQPU modules.

### 5.4 Assessment

Microfabrication is a **necessary but not sufficient** condition for scaling. The key challenge is moving from research-scale fabrication (a few chips at a time) to high-volume manufacturing with consistent quality. Infineon's partnership with Quantinuum and IonQ's planned acquisition of SkyWater's foundry capacity indicate that the industry recognizes this bottleneck.

---

## 6. Integrated Photonics: Solving the Laser Delivery Problem

One of the most underappreciated scaling challenges is **optical access**. Current trapped-ion systems rely on bulk optics (lenses, mirrors, beam splitters) to deliver multiple laser beams to each ion. Scaling to hundreds or thousands of qubits with individual addressing using free-space optics is widely considered impractical.

### 6.1 Integrated Waveguide Delivery

The solution is to integrate photonic waveguides directly into the ion trap chip. Laser light is coupled into the chip via optical fibers, routed through on-chip waveguides, and emitted vertically toward the ions through grating couplers. This approach offers:

- **Stability**: Waveguides share common mechanical and thermal fluctuations with the trap, drastically reducing beam-pointing drift
- **Scalability**: A single optical input can be split to serve multiple zones via integrated splitters
- **Compactness**: Eliminates the need for large vacuum windows and external optics

### 6.2 Key Demonstrations

**ETH Zurich's Trapped Ion Quantum Information Group** has demonstrated entangling gates using integrated photonics in surface traps, with waveguide-integrated beam delivery enabling passive stability and tight focusing [^ethintegratedphotonics].

**MIT Lincoln Laboratory** has developed photonic integrated circuits (PICs) that distribute light from multiple input lasers to arrays of trapped ions using vertical grating couplers [^llintegratedphotonics].

**Carmelo Mordini et al. (2025)**, in a study published in *Physical Review X*, demonstrated a multizone QCCD device with integrated photonics, showing parallel coherent operations in two separate trap zones and careful characterization of optical crosstalk [^mordini2025]. The device featured integrated waveguide splitters with <0.2 dB loss, enabling a single optical input to serve multiple zones.

**Infineon** is actively developing integrated photonics as part of their roadmaps, and the **ACHIEVE** EU project has brought together multiple European partners to advance integrated photonic ion traps [^infineon2026].

### 6.3 Assessment

Integrated photonics is **essential for scaling beyond ∼50 qubits**. The technology has been proven in principle, but widespread adoption requires solving challenges related to:

- **Dielectric charging**: The waveguide materials can build up charge and create stray electric fields that heat the ions
- **Optical crosstalk**: Light scattered from waveguides can interfere with measurements in adjacent zones
- **Fabrication yield**: Integrating photonics, electronics, and trap electrodes on a single chip requires complex multi-layer processing

---

## 7. Experimental and Alternative Approaches

### 7.1 Penning Traps (ETH Zurich)

Researchers at ETH Zurich have demonstrated a **Penning trap** approach that replaces RF fields with a strong static magnetic field (3 Tesla) for ion confinement [^penning2024]. This eliminates RF heating and removes the linear grid restrictions that limit conventional traps to ∼30 qubits. The micro-Penning trap, fabricated on a chip, confined a single ion for several days with coherence times exceeding gate operation times.

**Caveat**: The approach has so far only been shown for a single ion. Scaling to multi-ion operations and performing multi-qubit gates remain to be demonstrated. The superconducting magnet is bulky, and strong magnetic fields complicate laser control.

### 7.2 All-Electronic Control (Oxford Ionics / Universal Quantum)

**Oxford Ionics** (now part of IonQ) developed a technique using "electronic qubit control" (EQC) that eliminates the need for complex laser systems for certain operations. Their approach achieved 99.99% two-qubit gate fidelity in 2025, and the 2D trap design offers up to 300× higher qubit density [^oxfordionics2025].

**Universal Quantum** uses microwave-based control (UQLogic) rather than laser-driven gates, which simplifies the control hardware and reduces the need for complex optical systems. Their approach is designed for integration with CMOS fabrication.

### 7.3 Cryogenic Systems

Operating ion traps at cryogenic temperatures (∼4 K) provides several benefits:

- **Ultra-high vacuum**: Cryopumping achieves the required vacuum levels (∼10⁻¹¹ Torr) much faster than room-temperature bake-out
- **Reduced heating rates**: Lower motional heating improves gate fidelities
- **Stability**: Cryogenic environments dampen thermal and mechanical noise

Quantinuum, Infleqtion, and several academic groups have developed cryogenic ion trap packages. The approach is widely seen as necessary for large-scale systems, though it adds complexity and cost.

---

## 8. Error Correction and Logical Qubit Scaling

Scaling the number of physical qubits is only half the challenge. Practical quantum computing requires **fault-tolerant logical qubits** — encoded qubits that can detect and correct errors during computation.

### 8.1 The Encoding Ratio Advantage

Trapped ions have a critical advantage in error correction: **extremely low physical error rates allow for very efficient encoding**. Quantinuum has demonstrated 48 logical qubits from 98 physical qubits using color codes, a 2:1 physical-to-logical ratio [^helios2026]. This is far better than the ∼1000:1 overhead typically required for surface codes on superconducting qubits.

The implications for a cryptographically relevant quantum computer (CRQC) are direct. If 2:1 encoding is achievable, then the ∼1,400 logical qubits estimated for RSA-2048 factoring would require only ∼2,800 physical qubits — a number that could be reached within a few years [^gidney2025].

### 8.2 Quantinuum's Logical Qubit Progress

- **2024**: Real-time quantum error correction and teleported CNOT gates on H2
- **2025**: 48 logical qubits on Helios, with "near five-nines" logical fidelity
- **2026**: Continued progress toward Sol, with a novel QEC code family

### 8.3 IonQ's Walking Cat Architecture

IonQ has published a detailed blueprint for fault-tolerant quantum computing called the "Walking Cat" architecture [^ionqwalkingcat]. The architecture is designed for two capabilities already demonstrated on QCCD hardware: >99.99% two-qubit gate fidelity and reliable ion transport. It features:

- Memory blocks under continuous error correction
- Magic state factories for T-gate synthesis
- Physical shuttling of ions to dedicated gate and optical zones
- Configurations spanning 102 to 220 logical qubits with a few thousand to tens of thousands of physical qubits

---

## 9. Comparative Assessment of Scaling Strategies

| Strategy | Maturity | Scalability Limit | Key Advantage | Key Challenge |
|----------|----------|-------------------|---------------|---------------|
| **QCCD Shuttling** | Commercial | 100–1000 qubits per chip | Highest fidelities; proven at 98 qubits | Shuttling latency; chip complexity |
| **Photonic Interconnects** | Prototype | 10⁶+ qubits (distributed) | Enables unlimited modular scaling | Low entanglement rates; system complexity |
| **Microfabricated Traps** | Commercial (3D/SE) | 10⁴ qubits per chip | Semiconductor manufacturing leverage | Yield; integration of photonics |
| **Integrated Photonics** | Research | 10³–10⁴ qubits per chip | Solves laser delivery bottleneck | Dielectric charging; crosstalk |
| **Cryogenic Operation** | Commercial | All scales | Better vacuum; lower noise | Cost; complexity; optical access |
| **All-Electronic Control** | Prototype | 10³–10⁴ per chip | Reduces laser requirement | Limited to certain gate types |
| **Penning Traps** | Research | Unknown | No RF heating; no grid restrictions | Strong magnets; early-stage |

### 9.1 Which Approaches Are Most Likely to Succeed?

**For the near term (2025–2028)**, the QCCD architecture is the clear frontrunner. Quantinuum has demonstrated a working path from 20 to 98 qubits with steadily improving fidelities, and the Sol system (2027) is expected to push further. The QCCD approach benefits from the most mature supply chain, the clearest engineering roadmap, and the best error correction results.

**For the medium term (2028–2032)**, modular architectures using photonic interconnects are likely to become dominant. IonQ's aggressive roadmap — 20,000 physical qubits by 2028, 2 million by 2030 — is ambitious but grounded in the acquisition of enabling technologies (Oxford Ionics for 2D traps, Lightsynq for photonic interconnects). The key question is whether photonic entanglement rates can be improved from the current ∼250 Hz to the ∼MHz rates required for distributed quantum computing.

**For the long term (2032+)**, a combination of all strategies will likely be needed:

- **QCCD** within each module for high-fidelity local operations
- **Photonic interconnects** between modules for system-wide connectivity
- **Integrated photonics** within each chip for scalable laser delivery
- **Cryogenic operation** for stability and vacuum
- **Advanced error correction** (color codes, LDPC codes) for efficiency

---

## 10. Critical Challenges Remaining

### 10.1 Gate Speed

Trapped-ion two-qubit gates take microseconds, compared to nanoseconds for superconducting qubits. This translates to longer algorithm runtimes. Quantinuum is addressing this through parallelized operations (Helios separates cooling and gating in space rather than time), but the fundamental speed limit remains a concern for applications requiring fast circuit execution.

### 10.2 Laser System Complexity

Even with integrated photonics, each qubit species requires specific laser wavelengths for cooling, state preparation, detection, and gating. Dual-species architectures (e.g., Yb⁺/Ba⁺) add further complexity. The industry is moving toward simpler atomic species (e.g., Ba⁺, which has a more convenient optical spectrum) and microwave-based control where possible.

### 10.3 Control Electronics

As the number of qubits grows, the number of control signals grows proportionally. Quantinuum's "wiring problem" solution is a critical step, but scaling to millions of qubits will require cryogenic control electronics, multiplexed signal delivery, and efficient classical-quantum interfaces.

### 10.4 Vacuum and Lifetime

Large ion traps require extreme high vacuum (∼10⁻¹¹ Torr) to prevent collisions with background gas from destroying the ion chain. Cryogenic operation helps, but maintaining vacuum integrity across large, multi-module systems is a significant engineering challenge.

### 10.5 Manufacturing Yield

Ion trap chips with hundreds of electrodes, integrated waveguides, and junctions are complex to fabricate. Yield must improve dramatically for commercial viability. Infineon's industrial MEMS fabrication and IonQ's planned SkyWater acquisition are steps toward solving this.

---

## 11. Conclusion

The most effective approaches to scaling ion trap quantum computing are **converging on a hybrid strategy**:

1. **Near-term (2025–2027)**: QCCD architectures with multi-zone traps, exemplified by Quantinuum's Helios and the upcoming Sol system. These systems will continue to push physical qubit counts toward 200–500 and demonstrate increasingly sophisticated error correction with favorable encoding ratios.

2. **Medium-term (2027–2030)**: The emergence of modular systems using photonic interconnects, led by IonQ's roadmap. The combination of 2D trap technology (Oxford Ionics) and quantum-memory-enhanced photonic links (Lightsynq) could enable a step-change in qubit count, potentially reaching thousands of logical qubits.

3. **Long-term (2030+)**: Fully distributed architectures with integrated photonics, all-electronic control, and advanced error correction. The goal is fault-tolerant systems with millions of physical qubits capable of solving commercially and scientifically valuable problems.

**Quantinuum currently holds the strongest position** in terms of demonstrated hardware, error correction, and commercial traction. **IonQ has the most ambitious roadmap** and has made bold bets on modular photonic scaling. **Universal Quantum and Infineon** are building important enabling technologies, while **ETH Zurich** and others continue to explore alternative trap designs that could simplify scaling.

The trapped-ion platform's fundamental advantages — perfect qubit uniformity, unmatched coherence, and the highest-fidelity gates — remain intact. The path to large-scale systems is clearer than ever, but the engineering challenges of integrating millions of qubits with reliable control, photonics, and error correction will require sustained effort and investment over the coming decade.

---

## References

[^nature2023scaling]: "Scaling up trapped-ion quantum computers," *Nature Research Custom Media*, 2023. https://www.nature.com/articles/d42473-023-00438-5

[^kielpinski2002]: D. Kielpinski, C. Monroe, D. J. Wineland, "Architecture for a large-scale ion-trap quantum computer," *Nature*, 417, 709–711 (2002). https://www.nature.com/articles/nature00784

[^helios2026]: "A 98-qubit trapped-ion quantum computer with all-to-all connectivity," *Nature*, 2026. https://www.nature.com/articles/s41586-026-10676-4

[^entangledfuture2026]: "Trapped-Ion Quantum Computing 2026," *Entangled Future*. https://entangledfuture.com/guides/trapped-ion-quantum-computing

[^quantinuum2024scaling]: "Quantinuum Proves Their Quantum Computers Will Scale with Major Hardware Innovation," Quantinuum Press Release, March 2024. https://www.quantinuum.com/press-releases/quantinuum-proves-their-quantum-computers-will-scale-with-major-hardware-innovation

[^quantinuum-infineon2024]: "Infineon and Quantinuum announce partnership," Quantinuum Press Release, November 2024. https://www.quantinuum.com/press-releases/infineon-and-quantinuum-announce-partnership-to-accelerate-quantum-computing-towards-meaningful-real-world-applications

[^quantinuum-quanta2026]: "Quantinuum Q2 2026 Results," Quantinuum Press Release, August 2026. https://www.quantinuum.com/press-releases

[^ionqroadmap2025]: "IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality," IonQ Blog, June 2025. https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality

[^ionqblog2025]: "IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality," IonQ Blog, 2025. https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality

[^ionqphotonic2026]: "IonQ Photonic Interconnect: First Networked Commercial Quantum Computers," *PostQuantum*, April 2026. https://postquantum.com/industry-news/ionq-photonic-interconnect-networked-quantum

[^ionqwalkingcat]: "Blueprint for Fault-Tolerant Trapped-Ion Quantum Computing: The Walking Cat Architecture," IonQ Blog, April 2026. https://www.ionq.com/blog/blueprint-for-fault-tolerant-trapped-ion-quantum-computing-the-walking-cat-architecture

[^monroe2024]: J. O'Reilly et al., "Fast photon-mediated entanglement of continuously-cooled trapped ions for quantum networking," *Phys. Rev. Lett.* 133, 090802 (2024). https://iontrap.duke.edu/2025/03/22/fast-and-hi-fi-photonic-interconnections-of-pristine-quantum-memories

[^nuquantum2026]: "Nu Quantum Opens State-of-the-Art Trapped-Ion Qubit Networking Lab," *The Quantum Insider*, February 2026. https://thequantuminsider.com/2026/02/10/nu-quantum-opens-state-of-the-art-trapped-ion-qubit-networking-lab-in-cambridge-to-accelerate-distributed-quantum-computing

[^sandiatraps]: Sandia National Laboratories, "Microfabricated ion traps." https://www.sandia.gov/quantum/microfabricated-ion-traps/

[^infineon2022]: "Industrially microfabricated ion trap with 1 eV trap depth," *Quantum Science and Technology* (2022). https://iopscience.iop.org/article/10.1088/2058-9565/ac7072

[^infineon2024]: "Trapped ion quantum computing," Infineon Technologies. https://www.infineon.com/technology/trapped-ions

[^infineon2026]: "Next generation HPC with quantum bits based on trapped ions," ACHIEVE Project. https://28digital.eu/fileadmin/2026/eu-projects/achieve/articles/ACHIEVE_Article_HPC-Quantum_Infineon.pdf

[^universalquantum2024]: "Scaling ion-trap chips: beyond the micro-fab adventures," Universal Quantum. https://universalquantum.com/knowledge-hub/scaling-ion-trap-chips-beyond-micro-fab-adventures

[^universalquantum2024b]: "Universal Quantum develops key enabler of million-qubit quantum computer," Universal Quantum. https://universalquantum.com/knowledge-hub/universal-quantum-develops-key-enabler-of-million-qubit-quantum-computer

[^ethintegratedphotonics]: "Integrated photonics for trapped ions," ETH Zurich Trapped Ion Quantum Information Group. https://tiqi.ethz.ch/research/integrated-photonics-for-trapped-ions.html

[^llintegratedphotonics]: "Integrated photonics may light the way to quantum computing," MIT Lincoln Laboratory. https://www.ll.mit.edu/news/integrated-photonics-may-light-way-quantum-computing

[^mordini2025]: C. Mordini et al., "Multizone Trapped-Ion Qubit Control in an Integrated Photonics QCCD Device," *Phys. Rev. X* 15, 011040 (2025). https://link.aps.org/doi/10.1103/PhysRevX.15.011040

[^penning2024]: "New ion trapping approach could help quantum computers scale up," *Physics World*, 2024. https://physicsworld.com/a/new-ion-trapping-approach-could-help-quantum-computers-scale-up

[^oxfordionics2025]: "IonQ reports 99.99% two-qubit gate fidelity," referenced in multiple sources. https://postquantum.com/industry-news/ionqroadmap-crqc

[^gidney2025]: Post-quantum cryptography analysis, referenced in *PostQuantum* analysis. https://postquantum.com/quantum-modalities/trapped-ion-qubits

[^monroe2014]: C. Monroe et al., "Large-scale modular quantum-computer architecture with atomic memory and photonic interconnects," *Phys. Rev. A* 89, 022317 (2014). https://link.aps.org/doi/10.1103/PhysRevA.89.022317

[^blakestad2009]: R. B. Blakestad et al., "High-Fidelity Transport of Trapped-Ion Qubits through an X-Junction Trap Array," *Phys. Rev. Lett.* 102, 153002 (2009). https://inspirehep.net/literature/2932430

[^quantinuum-qccd]: "Quantum Charge-coupled Device (QCCD)," Quantinuum. https://www.quantinuum.com/glossary-item/quantum-charge-coupled-device-qccd

[^ionq-technology]: "Our Trapped Ion Technology," IonQ. https://www.ionq.com/technology

[^ionq-roadmap]: "Roadmap," IonQ. https://www.ionq.com/roadmap

[^ionq-blog-interconnect]: "Enabling Networked Quantum Computing with Ion-Photon Entanglement," IonQ Blog. https://www.ionq.com/blog/enabling-networked-quantum-computing-with-ion-photon-entanglement

[^infineon-2024b]: "Trapped ion quantum computing," Infineon Technologies. https://www.infineon.com/technology/trapped-ions

[^zuriq2025]: "ZuriQ and Infineon join forces to advance ion-trap chip technology," ZuriQ, May 2025. https://zuriq.com/news/zuriq-and-infineon-join-forces-to-advance-ion-trap-chip-technology

[^universalquantum-blog]: "Scaling ion-trap chips: beyond the micro-fab adventures," Universal Quantum. https://universalquantum.com/knowledge-hub/scaling-ion-trap-chips-beyond-micro-fab-adventures

[^nature2025errorcorrection]: Google Quantum AI, "Quantum error correction below the surface code threshold," *Nature* 638, 920–926 (2025). https://www.nature.com/articles/s41586-024-08449-y

[^aps2025scaling]: "Scaling Up a Trapped-Ion Quantum Computer," *Physics* 16, 209 (2023). https://link.aps.org/doi/10.1103/Physics.16.209

[^physrevx2023]: S. A. Moses et al., "A Race-Track Trapped-Ion Quantum Processor," *Phys. Rev. X* 13, 041052 (2023). https://link.aps.org/doi/10.1103/PhysRevX.13.041052

[^duke2025photonics]: "Fast and Hi-Fi Photonic Interconnections between Pristine Quantum Memories," Duke Ion Trap Group, March 2025. https://iontrap.duke.edu/2025/03/22/fast-and-hi-fi-photonic-interconnections-of-pristine-quantum-memories

[^arxiv2025qccd]: "Scaling and assigning resources on ion trap QCCD architectures," arXiv:2408.00225 (2024). https://arxiv.org/abs/2408.00225

[^nature2021qccd]: "Demonstration of the trapped-ion quantum-CCD computer architecture," *Nature* 592, 209–213 (2021). https://www.nature.com/articles/s41586-021-03318-4

[^prx2024scalable]: "Scalable Architecture for Trapped-Ion Quantum Computing Using rf Traps," *Phys. Rev. X* 14, 041017 (2024). https://link.aps.org/doi/10.1103/PhysRevX.14.041017

[^monroe2013review]: C. Monroe and J. Kim, "Scaling the Ion Trap Quantum Processor," *Science* 339, 1164–1169 (2013). https://iontrap.duke.edu/files/2025/03/science.1231298.pdf

[^postquantum2026]: "Trapped-Ion Quantum Computing: How It Works, Who Builds It," *PostQuantum*. https://postquantum.com/quantum-modalities/trapped-ion-qubits

[^postquantumcrqc2025]: "IonQ's 2025 Roadmap: Toward a Cryptographically Relevant Quantum Computer by 2028," *PostQuantum*. https://postquantum.com/industry-news/ionqroadmap-crqc

[^jstmoonshot]: "Moonshot R&D Progress Report Goal 6: Research and development for photonic interconnects of ion traps," Japan Science and Technology Agency. https://www.jst.go.jp/moonshot/en/program/goal6/appeal/63_takahashi_ap01.html

[^arxiv2025photonic]: "Scalable Trapped Ion Addressing with Adjoint-optimized Multimode Photonic Circuits," arXiv:2505.08997 (2025). https://arxiv.org/html/2505.08997v1

[^naturecomm2024]: "Multi-site integrated optical addressing of trapped ions," *Nature Communications* (2024). https://www.nature.com/articles/s41467-024-47882-5

[^pennylane]: "Trapped ion quantum computers," PennyLane Demos. https://pennylane.ai/demos/tutorial_trapped_ions

[^readingthequantum]: "Are trapped ions hard to scale?" *Reading the Quantum* (2024). https://m-malinowski.github.io/2024/02/06/scaling-ions.html

[^ieee2025modular]: "Quantum Computing Companies Focus on Modular Set Ups," *IEEE Spectrum*. https://spectrum.ieee.org/quantum-computers

[^aps2025modular]: "Large-scale modular quantum-computer architecture with atomic memory and photonic interconnects," *Phys. Rev. A* 89, 022317. https://link.aps.org/doi/10.1103/PhysRevA.89.022317
