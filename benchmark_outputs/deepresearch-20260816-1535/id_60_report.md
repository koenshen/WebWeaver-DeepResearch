
# Comprehensive Cislunar Space Situational Awareness: Architectures, Technologies, and Short-Term Tracking Effectiveness

## 1. Introduction

Cislunar space—the volume extending from geosynchronous Earth orbit (GEO) approximately 35,786 km altitude out to and including the Moon's orbit at ~384,400 km—is experiencing a rapid expansion of human activity. The U.S. National Cislunar Science & Technology Strategy (2022) identified cislunar space situational awareness (CSSA) as a key national priority. By the early 2030s, over 120 active vehicles and more than 400 spacecraft are expected to operate in this region. Unlike near-Earth space, where Keplerian two-body dynamics dominate, cislunar space is governed by complex three-body gravitational interactions (Earth-Moon-Sun), creating unique challenges for detection, tracking, orbit determination, and traffic management.

This report synthesizes the current state of the art in CSSA, covering sensing architectures, detection and tracking methodologies, orbit determination techniques, key operational programs, and strategies for supporting short-term tracking and monitoring task effectiveness.

## 2. Fundamental Challenges of Cislunar Space Situational Awareness

### 2.1 Physical and Dynamical Challenges

The challenges of CSSA are fundamentally different from those in LEO or GEO:

| **Challenge** | **Description** | **Source** |
|---|---|---|
| **Extreme distances** | Signal intensity falls off as 1/R⁴ for passive optical systems; objects at lunar distances are 10⁶× fainter than equivalent objects in GEO | AFRL Primer on Cislunar Space |
| **Complex dynamics** | Non-Keplerian motion governed by the circular restricted three-body problem (CR3BP); orbits are chaotic and unstable | Frueh et al. (2021) |
| **Lunar proximity** | The Moon's albedo creates severe optical background noise; lunar exclusion angles limit observation windows | University of Maryland FaXT project |
| **Slow apparent motion** | Cislunar objects have orbital periods of days to weeks; very short observation arcs (hours) capture only a tiny fraction of the orbit | AFRL Primer |
| **Illumination constraints** | Passive EO sensors require solar illumination; the Sun's apparent motion relative to the Earth-Moon system creates periodic blind zones | Purdue University CSSA paper |
| **Uncertainty propagation** | Three-body dynamics produce highly non-Gaussian, banana-shaped uncertainty distributions, invalidating conventional Gaussian filters | Frueh et al. (2021) |

### 2.2 Observability Gaps

A critical finding from the Purdue University study (2021) is that even a global network of ground-based optical sensors with limiting magnitude 20 cannot provide full coverage of many cislunar orbit families. Large fractions of high-value orbits (e.g., L1/L2 halo orbits, distant retrograde orbits) remain unobservable for extended periods. Single ground stations face particularly severe gaps for objects in highly elliptical or distant orbits.

## 3. Sensor Architectures for Cislunar SSA

### 3.1 Sensor Types

The AFRL Primer on Cislunar Space identifies four primary sensor phenomenologies:

| **Category** | **Type** | **Utility for Cislunar** | **Limitations** |
|---|---|---|---|
| **Passive Electro-Optical (EO)** | Telescopes (optical) | High — leverages reflected sunlight; widely available | Requires illumination; lunar albedo interference; limited by weather (ground-based) |
| **Active EO** | Laser ranging | Low — beam divergence at lunar distances requires prohibitive power; extreme pointing sensitivity | Not practical for wide-area surveillance |
| **Passive Radio-Frequency (RF)** | Antennas | High — if the target is transmitting; useful for cooperative objects | Useless for non-cooperative/non-transmitting objects |
| **Active RF** | Radar | Low to moderate — requires enormous power for lunar-range detection; Space Fence limited to ~40,000 km | Ground-based radar ineffective beyond GEO |

The consensus across multiple studies is that **passive optical sensors** are the most practical and widely available sensing modality for cislunar SSA, but they must be supplemented by space-based assets for complete coverage.

### 3.2 Sensor Location Strategies

No single sensor location can observe all of cislunar space. The following architectural approaches are being pursued:

#### 3.2.1 Earth Ground-Based Sensors

- **Advantages**: Existing infrastructure; lower cost per node; can be globally distributed
- **Disadvantages**: Atmospheric effects; limited to nighttime; Earth's rotation breaks continuous coverage; severe geometric dilution of precision for distant objects
- **Key finding**: A global network of electro-optical sensors is mandatory even for large (several-meter) objects, yet still leaves significant coverage gaps (Frueh et al., 2021)

#### 3.2.2 Earth Orbiting Space-Based Sensors

- **Advantages**: No atmospheric interference; above weather; wider field of regard
- **Disadvantages**: Still subject to solar illumination cycles; orbital motion creates changing perspectives; limited by sensor size/mass constraints
- **Examples**: AFRL's Oracle-P, NASA's planned cis-lunar telescopes

#### 3.2.3 Moon-Based Sensors

- **Advantages**: Proximity to cislunar targets; stable lunar surface platform; favorable geometry for observing Earth-Moon Lagrange points
- **Key result**: A study by Raytheon (Koblick & Choi, 2022) demonstrated that four mid-latitude narrow-field-of-view angles-only sensors on the Moon can maintain 100% track custody of all tested cislunar target trajectories. Adding space-based measurements improved position estimation error by a factor of five.
- **Disadvantages**: Lunar dust; thermal extremes; communication latency; power constraints during lunar night

#### 3.2.4 Cislunar Space-Based Sensors (Orbiting Observers)

- **Advantages**: Unique vantage points; can observe from within the domain; LiAISON navigation capability
- **Disadvantages**: All repeating natural orbits in cislunar space are unstable, requiring stationkeeping fuel; limited "real estate" of useful orbits
- **Key orbit families**: L1/L2 halo orbits, distant retrograde orbits (DROs), Lyapunov orbits, W4W5 family, synodic-resonant orbits (29.5-day period)

### 3.3 The Need for Heterogeneous, Distributed Architectures

All major studies emphasize that a **multi-tier, heterogeneous sensor network** is essential:

- **Earth-based**: Global optical telescope network for initial detection and coarse tracking
- **Space-based (Earth orbit)**: Space-based telescopes for persistent monitoring without atmospheric limitations
- **Cislunar orbit**: Observer satellites in L1/L2 halo, DRO, or resonant orbits for mid-range tracking
- **Lunar surface**: Fixed sensors for terminal tracking and precision orbit determination

The multi-sensor data fusion approach has been shown to improve overall visibility by approximately 5–11% compared to radar-only or optical-only architectures, as radar performance is not affected by solar illumination conditions (ERAU fusion study).

## 4. Detection and Tracking Methodologies

### 4.1 Track-Before-Detect (TBD) Techniques

Traditional detect-before-track approaches suffer from low signal-to-noise ratio (SNR) in cislunar space. The **Fast X-ray Transform (FaXT)** methodology, developed for asteroid detection, is being adapted for cislunar SSA under AFRL sponsorship. Key characteristics:

- Uses dynamic programming to integrate energy along possible trajectories
- Capable of detecting objects up to 10× fainter than conventional methods
- Demonstrated on CAPSTONE (a CubeSat in lunar orbit) as a proof of concept
- Particularly effective for small, highly maneuverable platforms and distant objects

**Source**: University of Maryland FaXT/Cislunar Detection Project

### 4.2 DARPA Track at Big Distances with Track-Before-Detect (TBD2)

DARPA's TBD2 program directly addresses the cislunar detection gap:

- **Goal**: Develop software algorithms for continuous space-based detection and tracking of objects in cislunar space
- **Approach**: Pair commercially available optical sensors with onboard processing computers
- **Capability targets**: Track objects as small as 10–20 cm at distances of 200,000–400,000 km within hours
- **Payload designs**: Two configurations — one for Sun-Earth L1 (1.5 million km from Earth) and one for "beyond GEO/cislunar orbits"
- **Strategic value**: Monitor the "Earth-Moon corridor" for potential threats and objects of interest

**Source**: DARPA TBD2 solicitation, Space.com report

### 4.3 Multi-Object Tracking with Space-Based Observers

Purdue University research has developed sensor tasking algorithms for constellations of optical observers in cislunar space:

- **Dynamics models**: Circular restricted three-body problem (CR3BP) for target dynamics; bi-circular restricted four-body problem for Sun position
- **Uncertainty representation**: Particle filters outperform Gaussian representations for delayed feedback environments in cislunar space
- **Demonstrated applications**: Tracking simulated small satellite breakups in Lyapunov orbit and Lunar Gateway breakup scenarios

**Source**: Purdue University Graduate School thesis on multi-object tracking

## 5. Orbit Determination in Cislunar Space

### 5.1 Challenges for Orbit Determination

Traditional two-body-based initial orbit determination (IOD) methods fail in the cislunar regime:

| **Challenge** | **Impact** |
|---|---|
| Non-Keplerian dynamics | Two-body IOD assumptions invalid |
| Short observation arcs | Hours of observation capture <1% of orbit period |
| Unknown maneuvers | Active spacecraft may execute unmodeled stationkeeping or evasive maneuvers |
| Low SNR | Sparse measurements with high angular noise |
| Chaos | Sensitive dependence on initial conditions makes long-term prediction unreliable |

### 5.2 Emerging IOD and OD Approaches

#### 5.2.1 Multi-Constrained Optimization for Short-Arc IOD

Recent work (2026) presents a multi-constrained optimization algorithm for angles-only short-arc observations in cislunar space. By integrating orbital energy constraints, geometric constraints, and three-body dynamics, the algorithm provides robust IOD solutions from very short data arcs.

#### 5.2.2 Physics-Informed Orbit Determination (PIOD)

Scorsoglio et al. (2023) introduced Physics-Informed Neural Networks (PINNs) for cislunar orbit determination:

- Uses the restricted perturbed two-body problem framework
- Angle-only observations processed through neural networks that embed the dynamics equations
- Addresses the error drift problem of numerical integration
- Suitable for non-cooperative objects where batch least-squares (DSN-based) methods are unavailable

#### 5.2.3 Collocation and Nonlinear Programming for Maneuver Reconstruction

A 2025 study demonstrates that collocation and nonlinear programming can enable accurate IOD and maneuver reconstruction for active spacecraft with unknown maneuvers. This greatly enhances operational capability for initial detection and tracking.

#### 5.2.4 Probabilistic IOD Methods

Bolden et al. (2022) and subsequent work (ArXiv 2026) have developed probabilistic IOD methods specifically for cislunar space:

- Admissible region-based methods adapted for three-body dynamics
- Bayesian approaches for handling measurement uncertainty
- Particle filter-based track maintenance

#### 5.2.5 Machine Learning for Orbit Classification

- Martin et al. demonstrated efficacy of ML for classifying cislunar objects into periodic orbit families based on observational features
- Zhou et al. developed LSTM-based neural networks for libration point orbit classification

### 5.3 Precision Orbit Determination (POD)

For cooperative objects, the NASA Deep Space Network (DSN) provides range and Doppler tracking capable of reducing position and velocity errors to <0.1 km and <0.1 cm/s. However, this method is unavailable for non-cooperative objects.

The LiAISON (Linked Autonomous Interplanetary Satellite Orbit Navigation) technique enables autonomous OD using only inter-satellite measurements, requiring at least one spacecraft in a suitably asymmetric orbit. This was demonstrated by the CAPSTONE mission.

## 6. Key Operational Programs and Initiatives

### 6.1 AFRL Oracle Family of Systems

The Oracle program is the U.S. Department of Defense's primary investment in cislunar SSA:

| **Component** | **Designation** | **Status** | **Mission** |
|---|---|---|---|
| **Oracle-M** (formerly D2S2) | Mobility Pathfinder | Hot fire test completed March 2025; ILC achieved; manifested on NSSL | Demonstrate cislunar operations, high mobility, track known cislunar objects |
| **Oracle-P** (formerly Oracle Prime) | SSA Experiment | Delivery 2026; launch 2027 | Search for unknown/lost objects; maintain custody of known objects; wide- and narrow-field-of-view sensors with onboard processing |

**Oracle-M** completed a critical hot fire test (March 16–21, 2025) at Edwards AFB, validating its integrated Hall Effect thruster propulsion module. The satellite is a secondary payload on a near-term National Security Space Launch and will provide unprecedented SSA capability for continuous tracking beyond GEO. Data from both Oracle experiments will be available via the Unified Data Library.

**Oracle-P** features wide- and narrow-field-of-view sensors with cutting-edge onboard processing to reduce data downlink volume. It was originally designed to demonstrate ASCENT green propellant, but that module was decoupled for accelerated development.

**Source**: AFRL Oracle fact sheet; SSC Newsroom release

### 6.2 DARPA Programs

| **Program** | **Focus** | **Status** |
|---|---|---|
| **TBD2** (Track at Big Distances with Track-Before-Detect) | Onboard processing algorithms with commercial optical sensors for continuous detection of faint objects | Contract solicitation active |
| **LASSO** (Lunar Assay via Small Satellite Orbiter) | Autonomous, highly maneuverable small satellites in low lunar orbit for SSA | Prototype agreements solicited |
| **NOM4D** (Novel Orbital and Moon Manufacturing, Materials, and Mass-efficient Design) | In-space manufacturing; relevant for lunar infrastructure | Active |

### 6.3 Cislunar Highway Patrol System (CHPS)

AFRL's CHPS program aims to deploy spacecraft as remote sensing platforms to monitor the region about the Moon. CHPS spacecraft were planned to launch in 2025 to experiment with space traffic management concepts. The program is designed to improve the U.S. Space Force's ability to track and identify artificial objects operating at lunar distances and beyond.

### 6.4 NASA and ESA Contributions

- **Lunar Gateway**: A key asset in NRHO that will serve as a communications hub, science laboratory, and staging point; can host SSA sensors
- **CAPSTONE**: CubeSat demonstrating autonomous navigation (LiAISON) and cislunar operations; used as a test target for FaXT detection algorithms
- **ARTEMIS**: P1 and P2 spacecraft (former THEMIS) — first satellites to achieve Earth-Moon Lagrange point orbits; demonstrated DSN-based OD
- **LuGRE** (NASA/Italian Space Agency): Received GPS signals on the lunar surface in March 2025, demonstrating the potential for GNSS-based cislunar navigation

### 6.5 Commercial and Academic Efforts

- **Rhea Space Activity**: Developing a "lunar intelligence dashboard" under Air Force contract to track and visualize objects in cislunar space
- **University of Maryland**: FaXT algorithm adaptation for cislunar faint object detection
- **Purdue University**: CSSA constellation design, uncertainty propagation, and multi-object tracking
- **Embry-Riddle Aeronautical University**: Multi-sensor data fusion for cislunar SSA
- **Johns Hopkins APL**: Deep Space Catalog and VLBI-based tracking studies

## 7. Supporting Short-Term Cislunar Tracking and Monitoring Tasks

For operational effectiveness of short-term (hours to days) tracking and monitoring tasks, the following strategies are essential:

### 7.1 Sensor Tasking and Scheduling

The "Too-Short-Arc" (TSA) problem is critical in cislunar space. With orbital periods of days to weeks, even several hours of observation capture an insufficient fraction of the orbit for traditional IOD. Key approaches:

- **Dynamic sensor tasking**: Algorithms that prioritize sensors based on predicted target visibility, illumination conditions, and geometric dilution of precision
- **Particle filter-based uncertainty propagation**: Enables robust tasking decisions even with highly non-Gaussian uncertainties
- **Capacity-based optimization**: Ball Aerospace and AFRL have developed scheduling algorithms that maximize the number of objects tracked given sensor constraints

### 7.2 Rapid Initial Orbit Determination

For short-term tasks, operators need IOD solutions that are accurate enough to enable re-acquisition by other sensors. Recent advances:

- **Multi-constrained optimization** using orbital energy, geometry, and dynamics constraints
- **Collocation methods** that simultaneously estimate orbit and maneuvers
- **Probabilistic IOD** that provides uncertainty regions rather than point estimates, reducing the risk of losing the target

### 7.3 Persistent Coverage Through Constellation Design

The design of CSSA constellations is a multi-objective optimization problem balancing:

| **Objective** | **Metrics** | **Trade-offs** |
|---|---|---|
| Coverage | Fraction of volume/time with detection capability | More satellites = higher cost |
| Track custody | Mean time to re-acquire; probability of track loss | Stability vs. coverage diversity |
| Orbit determination accuracy | Position/velocity error at epoch | Observation geometry vs. revisit time |
| Resilience | Performance under satellite failures | Distributed vs. centralized architectures |
| Cost | Number of satellites, launch costs, stationkeeping fuel | Constellation size vs. individual capability |

Optimal architectures use a mix of:
- **L1/L2 halo orbits** for persistent monitoring of the "Cone of Shame" and low-energy transfer corridors
- **Distant retrograde orbits (DROs)** for stable, long-duration surveillance
- **Synodic-resonant orbits** (29.5-day period) for favorable solar illumination geometry
- **Earth-Moon resonance orbits** for surveillance of the entire cislunar volume (Frueh et al., 2021 ESA paper)

### 7.4 Data Fusion and Integration

The Unified Data Library (UDL) is being leveraged by the Oracle program to aggregate data from multiple sources. Key fusion strategies:

- **Angles-only fusion**: Combining angular measurements from geographically dispersed sensors provides triangulation with improved accuracy
- **Range + angles fusion**: When available (e.g., from radar or DSN), range measurements dramatically improve OD accuracy
- **VLBI (Very Long Baseline Interferometry) enhancement**: JHU APL demonstrated that adding a space-based telescope to ground-based VLBI assets significantly improves tracking accuracy
- **Multi-sensor fusion**: Combining radar and optical data improves overall visibility by 5–11%, as radar is not affected by solar illumination conditions

### 7.5 Onboard Processing and Autonomy

For short-term effectiveness, latency is critical. DARPA TBD2 and Oracle-P both emphasize onboard processing:

- **Onboard detection**: Process raw optical images on the spacecraft, reducing downlink requirements
- **Autonomous tracking**: Algorithms that can maintain track custody without ground intervention
- **Real-time maneuver detection**: Identify and characterize unknown maneuvers within hours, not days

### 7.6 Operational CONOPS Recommendations

Based on the Mitchell Institute report and AFRL guidance:

1. **Establish a dedicated cislunar SDA operations center** analogous to the Joint Space Operations Center (JSpOC) for near-Earth space
2. **Develop a cislunar object catalog** (the Deep Space Catalog concept from JHU APL) that tracks all known objects, including debris, inactive spacecraft, and active missions
3. **Implement a tiered warning system**: Early warning from space-based sensors (e.g., TBD2 at L1), follow-up from cislunar observers (Oracle), and precision tracking from lunar surface assets
4. **Create standard interfaces for data sharing** between military, civil (NASA), and commercial operators
5. **Invest in specialized training** for cislunar operations personnel, as the dynamics and sensor characteristics differ fundamentally from near-Earth operations

## 8. Summary of Key Findings

1. **Ground-based optical sensors alone are insufficient** for comprehensive CSSA, even with a global network; space-based and lunar-based sensors are mandatory.

2. **Heterogeneous multi-sensor architectures** combining Earth-based, Earth-orbiting, cislunar-orbiting, and lunar surface sensors provide the best coverage and tracking accuracy.

3. **Track-before-detect algorithms** (FaXT, DARPA TBD2) are essential for detecting faint objects at extreme ranges, enabling detection of objects 10× fainter than conventional methods.

4. **Three-body dynamics** render traditional two-body IOD methods invalid; new approaches using multi-constrained optimization, physics-informed neural networks, and probabilistic methods are required.

5. **Uncertainty propagation** in cislunar space produces highly non-Gaussian distributions that demand particle filter or other non-parametric methods for accurate orbit determination.

6. **Onboard processing** is critical for short-term effectiveness, reducing latency and enabling autonomous tracking.

7. **The Oracle family of systems** (Oracle-M and Oracle-P) represents the U.S. military's primary near-term investment, with Oracle-M achieving initial launch capability after successful hot fire testing in March 2025.

8. **DARPA's TBD2 program** addresses the gap in continuous space-based detection capability, targeting objects as small as 10–20 cm at distances up to 400,000 km.

9. **Lunar surface sensors** offer unique advantages for persistent custody, with demonstrated 100% track maintenance capability in simulation studies.

10. **Data fusion across sensor types** (optical, radar, RF) and locations (ground, space, lunar) improves overall tracking performance by 5–11% and dramatically improves position estimation accuracy.

## 9. Conclusion

Achieving comprehensive and accurate situational awareness of cislunar space targets requires a fundamental departure from near-Earth SSA paradigms. The complex three-body dynamics, extreme distances, and unique illumination conditions demand a multi-tiered, heterogeneous sensor architecture that spans Earth ground stations, Earth-orbiting platforms, cislunar-orbiting observers, and lunar surface assets. Short-term tracking effectiveness is supported by advanced detection algorithms (track-before-detect), rapid IOD methods adapted for non-Keplerian dynamics, onboard processing for reduced latency, and robust sensor tasking strategies that account for the highly time-varying observability of cislunar orbits.

The U.S. has made significant investments through AFRL's Oracle program, DARPA's TBD2 and LASSO programs, and the CHPS concept, with Oracle-M reaching operational readiness. However, the operational community must continue to develop the enabling technologies—particularly in autonomous onboard processing, three-body orbit determination, and multi-sensor data fusion—to ensure that cislunar space remains a safe, secure, and sustainable domain for the expanding range of civil, commercial, and national security activities planned for the coming decades.

---

## References

1. U.S. Space Force Space Systems Command. "Oracle-M Hot Fire Test: A Major Milestone in Cislunar Space Situational Awareness and National Security." March 2025. https://www.ssc.spaceforce.mil/Newsroom/Article/4176371/oracle-m-hot-fire-test-a-major-milestone-in-cislunar-space-situational-awarenes

2. Frueh, C., Howell, K., DeMars, K.J., Bhadauria, S., & Gupta, M. "Cislunar Space Situational Awareness." AAS 21-290, 2021. https://engineering.purdue.edu/people/kathleen.howell.1/Publications/Conferences/2021_AAS_FruHowDeMBha.pdf

3. Air Force Research Laboratory. "AFRL's Oracle Family of Systems: Developing Nation's 1st Cislunar Space Situational Awareness Capabilities." https://afresearchlab.com/afrls-oracle-family-of-systems-developing-nations-1st-cislunar-space-situational-awareness-capabilities-2

4. Air Force Research Laboratory. "A Primer on Cislunar Space." Distribution A: Approved for public release. https://www.afrl.af.mil/Portals/90/Documents/RV/A%20Primer%20on%20Cislunar%20Space_Dist%20A_PA2021-1271.pdf

5. University of Maryland. "Cislunar Detection and Tracking – FaXT Project." 2024. https://tamz.umd.edu/project/rapid_disco

6. Galbreath, C. "Securing Cislunar Space and the First Island Off the Coast of Earth." Mitchell Institute for Aerospace Studies, 2024. https://www.mitchellaerospacepower.org/securing-cislunar-space-and-the-first-island-off-the-coast-of-earth

7. Tingley, B. "US military wants to track 'potential threats' coming from the moon." Space.com, 2025. https://www.space.com/space-exploration/launches-spacecraft/us-military-wants-to-track-potential-threats-coming-from-the-moon

8. Koblick, D.C. & Choi, J.S. "Cislunar Orbit Determination Benefits of Moon-Based Sensors." AMOS Conference, 2022. https://amostech.com/TechnicalPapers/2022/Poster/Koblick_2.pdf

9. Bolden, M., Hussein, I., Borowski, H., See, R., & Griggs, E. "Probabilistic Initial Orbit Determination and Object Tracking in Cislunar Space Using Optical Sensors." AMOS Conference, 2022.

10. DeCoster, M.E. et al. "Building the Future of Cislunar Surveillance: In-Space Assembly and Manufacturing-Enabled Sensor Architectures for Large-Volume Space Situational Awareness." *New Space*, 2025. https://journals.sagepub.com/doi/10.1177/21680256251390412

11. Scorsoglio, A. et al. "Physics-Informed Orbit Determination for Cislunar Space Applications." AMOS Conference, 2023. https://ui.adsabs.harvard.edu/abs/2023amos.conf....1S/abstract

12. "Initial Orbit Determination for Cislunar Objects with Unknown Maneuvers via Collocation and Nonlinear Programming." *Journal of the Astronautical Sciences*, 2025. https://link.springer.com/article/10.1007/s40295-025-00513-7

13. "Cislunar Orbit Determination and Tracking via Simulated Space-Based Optical Measurements." https://s3.us-west-2.amazonaws.com/advspace.publicshare/Thompson+-+Simulated+Optical+Measurements+for+Cislunar+OD.pdf

14. "Multi-Objective Optimization of Cislunar Space Situational Awareness Constellations for Direct Transfer Orbit Scenarios." *Aerospace Science and Technology*, 2026. https://www.sciencedirect.com/science/article/abs/pii/S1270963826018997

15. "Cislunar Space Situational Awareness Constellation Design and Planning with Facility Location Problem." *Journal of Spacecraft and Rockets*. https://arc.aiaa.org/doi/10.2514/1.A36361

16. "Cislunar initial orbit determination for angles-only short arcs based on multi-constrained optimization." *Aerospace Science and Technology*, 2026. https://www.sciencedirect.com/science/article/abs/pii/S1270963826003792

17. "Probabilistic Methods for Initial Orbit Determination and Orbit Determination in Cislunar Space." arXiv:2602.18058, 2026. https://arxiv.org/abs/2602.18058

18. "Cislunar Space Traffic Management: Surveillance Through Earth-Moon Resonance Orbits." 8th ESA/ESOC European Conference on Space Debris, 2021. https://engineering.purdue.edu/people/kathleen.howell.1/Publications/Conferences/2021_ESA_FruHowDeMBhaGup.pdf

19. National Science & Technology Council. "National Cislunar Science & Technology Strategy." White House, 2022. https://www.whitehouse.gov/ostp/news-updates/2022/11/17/fact-sheet-first-national-cislunar-science-technology-strategy/

20. Johns Hopkins APL. "APL Is Setting the Path to Prevent Traffic Jams in Space." 2022. https://www.jhuapl.edu/news/news-releases/221205-apl-cislunar-traffic-management

21. Biesecker, C. "DARPA Program Seeks Autonomous, Maneuverable Satellites For Cislunar Domain Awareness." *Defense Daily*, 2025. https://www.defensedaily.com/darpa-program-seeks-autonomous-maneuverable-satellites-for-cislunar-domain-awareness/space

22. Embry-Riddle Aeronautical University. "Multi-Sensor Data Fusion for Enhanced Cislunar Space Situational Awareness." https://commons.erau.edu/cgi/viewcontent.cgi?article=2225&context=discovery-day

23. Dahlke, J.A. "Heuristic Design of Cislunar Space Situational Awareness Architectures." AFIT Scholar, 2024. https://scholar.afit.edu/etd/8350

24. Klonowski, M. "Cislunar Space Situational Awareness Architecture Design." University of Colorado Boulder. https://hanspeterschaub.info/Papers/grads/MichaelKlonowski.pdf

25. "Cislunar Space Situational Awareness via Earth-Moon Lagrange Points." *IFAC-PapersOnLine*, 2025. https://www.sciencedirect.com/science/article/pii/S2405896325020269

