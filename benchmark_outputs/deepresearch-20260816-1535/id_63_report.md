
# Mitigating Material Damage in Lithium Niobate After Plasma Etching: A Comprehensive Review

## 1. Introduction

Lithium niobate (LiNbO₃, LN) is a key material for nonlinear integrated photonics, offering strong electro-optic and nonlinear optical coefficients, broad transparency, and a mature thin-film platform (LNOI). However, its chemical inertness and hard crystalline structure make plasma etching a challenging process. Dry etching of LN is dominated by physical sputtering (typically Ar⁺) or reactive ion etching (RIE) using fluorine- or chlorine-based chemistries, each introducing distinct damage mechanisms:

- **Redeposition of non-volatile byproducts** (e.g., LiF, LiCl, sputtered LiNbO₃) on sidewalls, causing micro-masking, surface roughening, and tapered profiles.
- **Ion-induced lattice damage**: amorphization, point defects, and oxygen vacancies from energetic ion bombardment.
- **Surface stoichiometry disruption**: preferential sputtering of Li and O, leading to Li-deficient or oxygen-deficient surface layers.
- **Sidewall roughness** from micro-masking and redeposition, which is the dominant source of optical propagation loss in etched waveguides.

This report systematically reviews the state-of-the-art strategies to mitigate these damage mechanisms, organized into **pre-etch treatments**, **in-situ process optimization**, **post-etch cleaning and annealing**, and **emerging techniques**.

---

## 2. Pre-Etch Surface Treatments

### 2.1 Proton Exchange (PE)

Proton exchange replaces surface Li⁺ ions with H⁺ by immersing LN in a hot acid bath (e.g., benzoic acid at 200–250°C). This dramatically reduces the Li concentration at the surface, thereby suppressing the formation of non-volatile LiF during subsequent fluorine-based plasma etching. Hu et al. demonstrated that CHF₃/Ar ICP etching of proton-exchanged LN yields nearly vertical sidewalls with negligible undercut and an etch rate of ~5.7 μm/h, compared to the severe LiF redeposition seen on untreated LN [1].

**Limitations:** PE degrades the ferroelectric and nonlinear optical properties of LN, requires a dedicated high-temperature step, and is not suitable for all device designs. A post-annealing step (e.g., 330°C for 1–2 h) can partially restore the electro-optic coefficient but adds complexity.

### 2.2 H₂ Plasma Surface Treatment

As a lower-cost alternative to proton exchange, Tok and co-workers demonstrated that a brief H₂ plasma treatment (prior to metal mask deposition) induces proton substitution at the LN surface, similar to PE but without wet chemistry [2]. This treatment mitigates surface stress on the LN film (especially on X- and Y-cut substrates) and reduces metal mask delamination. The result is improved etching profile verticality and reduced sidewall roughness, as shown in Figure 5 of [2].

**Process:** H₂ plasma at moderate ICP power (150 W, 40 V DC bias) for 2–5 minutes before lithography and metallization.

### 2.3 High-Temperature Reduction in H₂/Ar

Annealing LN in a reducing atmosphere (e.g., 10% H₂ + Ar at 400°C for 2 h) prior to etching creates oxygen vacancies and causes Li volatilization near the surface [3]. This generates a porous, defective layer that etches significantly faster in both dry and wet processes. The technique can enhance etch rates and improve sidewall angles (up to 85°) but may compromise crystal quality and requires careful control to avoid excessive damage.

---

## 3. In-Situ Process Optimization

### 3.1 Gas Chemistry Selection

**Argon-only (physical sputtering):** Using pure Ar ICP-RIE avoids the formation of LiF or LiCl entirely, as no chemical reaction occurs. This eliminates redeposition of non-volatile halides, though the process is purely physical, leading to slower etch rates and potential redeposition of sputtered LN itself. Ulliac et al. developed an Ar-based ICP-RIE process (2 mTorr, 600–700 W ICP) that achieves smooth sidewalls when followed by a wet cleaning step [4].

**Chlorine-based chemistries (BCl₃, Cl₂):** LiCl has a lower melting point (605°C) than LiF (845°C), making it more volatile and easier to remove from the surface. Cl-based etching generally yields better sidewall profiles than F-based chemistry [3]. However, Cl chemistries are more corrosive and less commonly used in production tools.

**Fluorine-based chemistries (SF₆, CHF₃, CF₄):** These are the most widely used reactive chemistries for LN. The key challenge is the non-volatile LiF byproduct. Strategies to mitigate LiF include:
- Adding O₂ to the gas mixture (e.g., SF₆/O₂) to form volatile NbOF₃ and reduce LiF accumulation [5].
- Using high substrate temperatures (>200°C) to increase LiF volatility [5, 6].
- Periodic interruption with HF wet cleaning [5].

**Bromine-based chemistry (HBr/BCl₃/Ar):** Recently reported atomic layer etching (ALE) processes using HBr-based chemistries demonstrate that Br-containing etch products are more volatile than Cl- or F-based counterparts, significantly reducing surface roughness and redeposition [7].

### 3.2 Atomic Layer Etching (ALE)

ALE is a cyclic, self-limiting process that altern between a surface modification step and a removal step, providing atomic-level control and minimal damage.

**Directional ALE:** Chen et al. reported a directional ALE process for LN using sequential exposures of an HBr/BCl₃/Ar plasma (modification step) and a low-power Ar plasma (directional removal step) [7]. Key results:
- Etch per cycle (EPC) of 1.04 ± 0.01 nm/cycle with 84.6% synergy at 0°C.
- At 200°C, synergy decreases to 56.8% but surface smoothing is observed (Rq = 0.25 ± 0.03 nm after 20 cycles, unchanged from the control).
- No aspect-ratio-dependent etching (ARDE) down to 150 nm gaps.
- The HBr chemistry enhances volatility of etch products compared to Cl- and F-based chemistries.

**Isotropic ALE:** An isotropic process using H₂ plasma followed by HBr/BCl₃/Ar plasma was also demonstrated, yielding EPC of 1.43 ± 0.02 nm/cycle with 97.9% synergy at 0°C [7].

**Post-ALE recovery:** The authors note that oxygen plasma ashing or annealing may be necessary to restore surface stoichiometry and crystallinity after ALE [7].

### 3.3 Redeposition-Free ICP Etching via Parameter Optimization

Kaufmann et al. established a systematic workflow to achieve redeposition-free Ar ICP etching of LNOI by balancing DC bias, chamber pressure, and mask geometry [8]. Three main methods were identified:

**Method 1 – Parameter tuning:** High DC bias (≥600 V) combined with moderate pressure (5–7 mTorr) enables removal of sputtered material before it can redeposit. At 600 V DC bias, redeposition vanishes at 5–7 mTorr. However, this regime is sensitive to chamber cleanliness and mask quality.

**Method 2 – Dense structure proximity:** In dense arrays of features, ion deflection between neighboring sidewalls enhances the lateral etch component, effectively removing redeposited material. Redeposition-free etching is achieved down to 1 μm gaps at 11 mTorr and 600 V DC bias.

**Method 3 – Trapezoidal mask shape:** Using a positively sloped (trapezoidal) mask edge increases the angle of incident ion bombardment on the sidewall, preventing redeposition buildup.

### 3.4 Substrate Temperature Control

Osipov et al. systematically studied the effect of substrate temperature on SF₆ ICP etching of LN [5]. Key findings:
- The etch rate is a complex function of temperature, with a maximum at ~200°C.
- Below 200°C, increasing temperature enhances the volatility of reaction products.
- Above 200°C, LiF redeposition begins to block the surface, reducing etch rate.
- Adding O₂ to SF₆ improves surface morphology (Rms = 30.52 nm for SF₆/O₂ vs. 119.37 nm for SF₆/Ar) [5].

Cryogenic etching (temperatures below −50°C) has been used in other materials to condense volatile byproducts and protect the surface, but its application to LN is not yet reported in the literature.

### 3.5 Periodic Etching with Cooling and Cleaning Breaks

For deep etching, thermal management is critical due to LN's low thermal conductivity. Tok et al. implemented a periodic process: 20 min etching followed by 4 min cooling (plasma off), with a full solvent clean (acetone, IPA, DI water) after each hour of cumulative etching [2]. This prevents thermal damage to the mask, reduces redeposition buildup, and allows deep, vertical etching.

### 3.6 Pulsed Bias Plasma

Pulsed RF bias during etching (alternating between high and low bias power) has been used in other material systems to reduce charge-induced damage, lower average ion energy, and improve selectivity [9]. For LN, bias-pulsed ALE has been suggested as a future direction to decrease process time while maintaining damage-free etching [7]. No experimental demonstrations on LN are yet available.

### 3.7 Hard Mask Engineering

The choice of mask material and geometry significantly affects etch quality.

**Metal mask selection:**
- **Ti/Al/Cr stack:** Tok et al. showed that a Ti/Al/Cr hard mask prevents redeposition of AlF₃ (a non-volatile byproduct) by using a Cr cap layer, which forms volatile CrF₄ [2].
- **Ni masks:** Electroplated Ni masks offer high selectivity in fluorine-based etching but can introduce roughness due to columnar grain structure [4].
- **Cr masks:** Widely used, but can suffer from micromasking if redeposited.

**DLC hard mask:** Liang et al. used diamond-like carbon (DLC) as a hard mask for Ar ion beam etching (IBE) of LN, achieving an etching selectivity of up to 3:1 (LN:DLC) and enabling deep etching with steep sidewalls [10].

**Annealed HSQ mask:** Thermal annealing of hydrogen silsesquioxane (HSQ) resist before etching improves the LN/HSQ etching selectivity from 0.55 to ~1, enabling deeper etching without mask erosion [11].

---

## 4. Post-Etch Damage Recovery

### 4.1 Wet Chemical Cleaning

Wet cleaning is the most common post-etch treatment to remove redeposited byproducts.

**SC-1 solution (NH₄OH:H₂O₂:H₂O = 1:1:5):** Standard cleaning step 1 at 70–85°C effectively removes LiF redeposition and sidewall debris. Hu et al. used SC-1 after each hour of fluorine-based ICP etching to maintain clean sidewalls [12]. SC-1 also etches LN at a slow rate (0.3 nm/min), which can smooth surface roughness [13].

**Hydrofluoric acid (HF):** Dilute HF (3.7–50%) at 40–90°C selectively removes LiF and other non-volatile fluoride compounds. Osipov et al. used a 30-second HF dip every 90 minutes during deep SF₆ ICP etching to maintain a high etch rate of 421 nm/min [5].

**Potassium hydroxide (KOH):** Hot KOH (40% solution at 70°C for 30 min) effectively removes redeposited LN sputtered material after Ar ICP etching [8].

**Buffered HF (BHF):** Used to strip HSQ masks after ALE [7].

### 4.2 Post-Etch Annealing

**Oxygen annealing:** Annealing in O₂ or air at 300–500°C for several hours restores oxygen stoichiometry damaged by plasma exposure. This reduces optical absorption losses and recovers the material-limited Q-factor [14, 15]. Shi et al. demonstrated that a slow-heating post-process annealing in O₂ can reduce waveguide loss by ~50% and increase the intrinsic Q-factor of microring resonators by ~100% [15].

**Pressurized oxygen annealing:** A patent by [16] describes pressurized annealing in O₂ gas at elevated temperatures to suppress oxygen out-diffusion and prevent formation of a surface layer with reduced refractive index, which can cause optical leakage.

**Metal-assisted annealing:** Depositing a reactive metal (e.g., Al) on the etched LN surface and annealing at high temperature creates a Cr-LNO alloyed layer that is resistant to wet etching. Subsequent wet etching removes the alloyed layer, transforming the sidewall from 60° to a perfect 90° angle while preserving ferroelectric properties [3].

### 4.3 Oxygen Plasma Ashing

Post-etch oxygen plasma treatment is recommended after ALE to remove residual organic contaminants and restore surface stoichiometry [7]. This is particularly important for ALE processes using HBr chemistries, where bromine residues may remain on the surface.

### 4.4 Combined Dry-Wet Hybrid Processes

The most effective approach for achieving damage-free, vertical sidewalls often combines multiple techniques:

1. **Dry etching** (RIE, ICP, or ALE) to define the structure.
2. **Wet cleaning** (SC-1, HF, or KOH) to remove redeposited byproducts.
3. **Annealing** (O₂ or pressurized) to restore crystallinity and stoichiometry.
4. **Optional second wet etch** to smooth the final sidewall.

For example, the process flow in [3] uses RIE + Al deposition + high-temperature annealing + wet etching to convert a 60° sidewall into a 90° sidewall with smooth morphology.

---

## 5. Emerging and Advanced Techniques

### 5.1 Ion Beam Etching (IBE) with Optimized Masks

Argon ion beam etching (IBE) is a purely physical process that avoids chemical damage but can introduce significant sidewall redeposition. Liang et al. demonstrated that a DLC hard mask enables high selectivity (3:1) and steep sidewalls in Ar IBE of LN [10]. The DLC mask is patterned using an intermediate SiO₂ hard mask that is etched by standard fluorine plasma, followed by O₂ plasma to transfer the pattern into DLC.

### 5.2 Ion Implantation-Enhanced Etching

Pre-implantation of heavy ions (e.g., Cu, Ti, O) at MeV energies creates a damaged surface layer that etches selectively in HF. This technique, called "ion beam enhanced etching" (IBEE), can achieve etch rates of 100 nm/s with smooth, vertical sidewalls [17]. The damage is subsequently removed by the wet etch, leaving a pristine LN surface. This approach is promising for nanostructuring but requires an ion accelerator.

### 5.3 Chemo-Mechanical Etching (CME)

Photolithography-assisted chemo-mechanical etching (PCME) achieves ultra-high Q factors (up to 4.04 × 10⁷) by combining mechanical polishing with chemical etching, completely avoiding plasma damage [18]. This technique is not yet scalable to complex circuits but offers a benchmark for minimal loss.

### 5.4 Directional ALE Combined with Isotropic ALE

A proposed process flow for TFLN devices consists of:
1. **Directional ALE** to define the vertical structure.
2. **Isotropic ALE** to smooth waveguide sidewalls by removing residual roughness.
3. **Post-ALE oxygen plasma or annealing** to restore surface stoichiometry.

This combination could eliminate the need for wet cleaning entirely, enabling all-dry, damage-free fabrication [7].

---

## 6. Summary of Recommendations

| Strategy | Method | Damage Mitigated | Key References |
|---|---|---|---|
| **Pre-etch** | Proton exchange | LiF redeposition | [1] |
| **Pre-etch** | H₂ plasma treatment | Mask delamination, sidewall roughness | [2] |
| **Pre-etch** | Reducing atmosphere anneal | Enhances etch rate, improves sidewall angle | [3] |
| **In-situ** | Ar-only chemistry | Eliminates LiF/LiCl formation | [4, 8] |
| **In-situ** | Cl-based chemistry | Reduces non-volatile halides | [3] |
| **In-situ** | HBr-based ALE | Minimal redeposition, atomic-level control | [7] |
| **In-situ** | High DC bias + moderate pressure | Redeposition-free etching | [8] |
| **In-situ** | Substrate heating (150–200°C) | Increases volatility of etch products | [5, 7] |
| **In-situ** | Periodic etching + cooling | Prevents thermal damage, manages redeposition | [2] |
| **In-situ** | Trapezoidal mask shape | Reduces sidewall redeposition | [8] |
| **In-situ** | DLC hard mask | High selectivity IBE | [10] |
| **Post-etch** | SC-1 wet cleaning | Removes LiF and redeposited material | [12, 13] |
| **Post-etch** | HF wet cleaning | Removes LiF | [5] |
| **Post-etch** | KOH wet cleaning | Removes sputtered LN redeposition | [8] |
| **Post-etch** | O₂ annealing | Restores stoichiometry, reduces optical loss | [14, 15] |
| **Post-etch** | Pressurized O₂ annealing | Suppresses oxygen out-diffusion | [16] |
| **Post-etch** | Metal-assisted annealing + wet etch | Achieves 90° vertical sidewalls | [3] |
| **Post-etch** | Oxygen plasma ashing | Removes residues, restores stoichiometry | [7] |

---

## 7. Conclusion

The mitigation of plasma-induced damage in LN requires a multi-faceted approach combining pre-etch surface conditioning, optimized in-situ etching parameters, and post-etch recovery. The most promising recent developments are:

1. **Atomic layer etching (ALE)** using HBr-based chemistry, which offers atomic-level precision with minimal surface roughening and no aspect-ratio-dependent etching.
2. **Redeposition-free ICP etching** achieved by careful balancing of DC bias, pressure, and mask geometry.
3. **Post-etch oxygen annealing** to restore stoichiometry and reduce optical losses.
4. **Hybrid processes** combining dry etching, metal-assisted annealing, and wet cleaning to achieve perfectly vertical, damage-free sidewalls.

For LN-based nonlinear photonics, the combination of directional ALE for structure definition, followed by isotropic ALE for sidewall smoothing and O₂ annealing for stoichiometry recovery, represents a promising all-dry fabrication route that could eliminate the need for wet chemistry while achieving the low optical losses required for high-Q nonlinear devices.

---

## References

[1] H. Hu, A.P. Milenin, R.B. Wehrspohn, H. Hermann, W. Sohler, "Plasma etching of proton-exchanged lithium niobate," *Journal of Vacuum Science & Technology A*, vol. 24, no. 4, pp. 1012–1015, 2006.  
https://pubs.aip.org/avs/jva/article/24/4/1012/102827/Plasma-etching-of-proton-exchanged-lithium-niobate

[2] M. Tok et al., "High-Quality Dry Etching of LiNbO₃ Assisted by Proton Substitution through H₂-Plasma Surface Treatment," *Nanomaterials*, vol. 12, no. 16, 2836, 2022.  
https://www.mdpi.com/2079-4991/12/16/2836

[3] H. Lin et al., "Advanced Etching Techniques of LiNbO₃ Nanodevices," *Micromachines*, vol. 14, no. 10, 2789, 2023.  
https://pmc.ncbi.nlm.nih.gov/articles/PMC10609314

[4] G. Ulliac, V. Calero, A. Ndao, F. Baida, M.P. Bernal, "Argon plasma inductively coupled plasma reactive ion etching study for smooth sidewall thin film lithium niobate waveguide application," *Optical Materials*, vol. 53, pp. 1–5, 2016.  
https://www.sciencedirect.com/science/article/abs/pii/S0925346715301816

[5] A.A. Osipov, S.E. Alexandrov, G.A. Iankevich, "The effect of a lithium niobate heating on the etching rate in SF₆ ICP plasma," *Materials Research Express*, vol. 6, 046306, 2019.  
https://cns1.rc.fas.harvard.edu/facilities/docs/The%20effect%20of%20a%20lithium%20niobate%20heating%20on%20the%20etching%20rate%20in%20SF6%20ICP%20plasma.pdf

[6] H. Zhang et al., "Angle-optimized ion-beam etching for high-verticality and smooth sidewalls in thin-film lithium niobate," *Optics Express*, vol. 34, no. 4, pp. 6870, 2026.  
https://opg.optica.org/oe/abstract.cfm?uri=oe-34-4-6870

[7] G. Chen et al., "Directional atomic layer etching of lithium niobate using Br-based plasma," *arXiv preprint*, 2025.  
https://arxiv.org/html/2511.01825v1

[8] F. Kaufmann et al., "Redeposition-free inductively-coupled plasma etching of lithium niobate for integrated photonics," *Nanophotonics*, 2023.  
https://pmc.ncbi.nlm.nih.gov/articles/PMC11501321

[9] M. Darnon, "Pulsed plasmas for etching in microelectronics," CNRS.  
https://plasmas-froids.cnrs.fr/wp-content/uploads/2021/01/MaximeDarnon.pdf

[10] X. Liang et al., "High density lithium niobate photonic integrated circuits," *Nature Communications*, vol. 14, 40502, 2023.  
https://www.nature.com/articles/s41467-023-40502-8

[11] S. He et al., "Improved selectivity in dry etching of lithium niobate with thermal annealed hydrogen silsesquioxane mask," *Nanotechnology*, vol. 36, 05201, 2025.  
https://ui.adsabs.harvard.edu/abs/2025Nanot..36.5201H/abstract

[12] H. Hu, R. Ricken, W. Sohler, "Etching of Lithium Niobate: From Ridge Waveguides to Photonic Crystal Structures," *European Conference on Integrated Optics (ECIO)*, 2008.  
https://www.ecio-conference.org/wp-content/uploads/2016/05/2008/2008_WeD3.pdf

[13] "Thin film LiNbO₃ surface preparation using SC-1," *Optical Materials Express*, vol. 15, no. 11, 2826, 2025.  
https://opg.optica.org/ome/fulltext.cfm?uri=ome-15-11-2826

[14] G. Chen et al., "Advances in lithium niobate photonics: development status and perspectives," *Advanced Photonics*, vol. 4, no. 3, 034003, 2022.  
https://www.spiedigitallibrary.org/journals/Advances-in-lithium-niobate-photonics-development-status-and-perspectives/volume-4/issue-03/034003/Advances-in-lithium-niobate-photonics-development-status-and-perspectives/10.1117/1.AP.4.3.034003.full

[15] J. Shi et al., "Reduced material loss caused by Electron Beam Lithography in thin-film lithium niobate through post-process annealing," *Optical Materials*, vol. 149, 115051, 2024.  
https://www.sciencedirect.com/science/article/abs/pii/S0925346724002325

[16] "Method for pressurized annealing of lithium niobate and resulting lithium niobate structures," WO1999063393A2, 1999.  
https://patents.google.com/patent/WO1999063393A2/en

[17] P. Nekvindova et al., "Modification of the etching properties of x-cut Lithium Niobate by ion implantation," *Nuclear Instruments and Methods in Physics Research B*, vol. 266, pp. 2901–2905, 2008.  
https://www.sciencedirect.com/science/article/abs/pii/S0168583X07018150

[18] C. Li et al., "Ultra-high Q lithium niobate microring monolithically fabricated by photolithography assisted chemo-mechanical etching," *Optica Open*, 2023.  
https://preprints.opticaopen.org/articles/preprint/Ultra-high_Q_lithium_niobate_microring_monolithically_fabricated_by_photolithography_assisted_chemo-mechanical_etching/23561415

[19] D. Zhu et al., "Integrated photonics on thin-film lithium niobate," *Advances in Optics and Photonics*, vol. 13, no. 2, pp. 242–352, 2021.  
https://opg.optica.org/aop/abstract.cfm?uri=aop-13-2-242

[20] A. Osipov et al., "Optical diagnostic of LiNbO₃ etching in NF₃/Ar ICP plasma: Part I," *Sensors and Actuators A: Physical*, vol. 335, 113370, 2022.  
https://www.sciencedirect.com/science/article/abs/pii/S0924424721006117

