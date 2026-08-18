

# Cloud-Based Train Control Systems for Urban Rail Transit: Recent Developments and Key Technologies

## 1. Introduction

Urban rail transit systems worldwide are undergoing a profound digital transformation. At the heart of this evolution is the migration from traditional, hardware-centric Communication-Based Train Control (CBTC) to cloud-native, software-defined train control architectures. Cloud computing, edge computing, 5G communications, artificial intelligence, and digital twin technologies are converging to create a new generation of train control systems that promise greater capacity, reliability, scalability, and cost efficiency. This report provides a comprehensive overview of the most recent developments in cloud-based train control systems and the key technologies that underpin them.

---

## 2. Recent Developments in Cloud-Based Train Control

### 2.1 Hitachi Rail — SelTrac G9 (2024–2025)

In November 2024, Hitachi Rail announced a **C$100 million (US$71.5 million) investment**, supported by C$4.5 million from the Government of Ontario through Invest Ontario, to develop the next generation of its SelTrac CBTC system — **SelTrac G9**. The new system will integrate **AI, 5G communications, edge computing, and cloud computing** into the urban rail signalling architecture. SelTrac, originally the world's first moving-block CBTC system, is currently operational on over 100 lines across 40 cities globally. The G9 generation aims to deliver lower costs, reduced carbon footprint, and improved passenger experience. The investment is expected to create 100 new jobs and retain 1,000 skilled positions at Hitachi Rail's Toronto engineering centre.

- **Source:** Railway Technology, November 2024  
  https://www.railway-technology.com/news/hitachi-rail-urban-rail-signalling-canada

- **Source:** Mass Transit Magazine, November 2024  
  https://www.masstransitmag.com/rail/railroad-signals-ptc-control-systems-and-products/press-release/55245968/hitachi-rail-hitachi-rail-invest-ontario-to-fund-c100-million-to-upgrade-cbtc-signaling-technology

### 2.2 Siemens Mobility — Train2Cloud and Signaling X

Siemens Mobility has developed **Train2Cloud**, a next-generation CBTC system that replaces proprietary hardware with off-the-shelf servers and a security-hardened operating system, running on an on-customer-premise "signalling data centre". The system uses the **DS3 (Distributed Smart Safe System)** safety platform to run safety-critical CBTC applications — including Automatic Train Protection (ATP) and interlocking — alongside non-safe applications like Automatic Train Supervision (ATS) on the same hardware. Train2Cloud supports high-performance IP-based networks and **5G**, and can integrate Big Data Analytics.

At a higher level, Siemens' **Signaling X** platform is a cloud-native architecture designed to accelerate the roll-out of digital train control technologies by decoupling hardware from software, making scaling easier and reducing costs. This platform is applicable to both mainline and mass transit operations.

Siemens also achieved a world first in 2024 with the **first cloud-based interlocking** in operation for ÖBB (Austrian Federal Railways) in Achau, using the DS3 platform.

- **Source:** Siemens Mobility — Train2Cloud  
  https://www.mobility.siemens.com/global/en/portfolio/digital-solutions-software/infrastructure/signaling-x/train2cloud.html

- **Source:** Siemens Press — First signalling in the cloud in operation  
  https://press.siemens.com/global/en/pressrelease/first-signalling-cloud-operation

- **Source:** Railway Gazette International — Train control moves into the cloud (Siemens white paper)  
  https://www.railwaygazette.com/whitepaper/train-control-moves-into-the-cloud-sponsored-by-siemens-mobility

### 2.3 Software-Defined Train Control (SDTC) — Research from China

A 2022 paper published in *Urban Rail Transit* (Springer) introduced a novel **Software-Defined Train Control (SDTC)** architecture. SDTC virtualises the core functions of CBTC — including the Vehicle Onboard Controller (VOBC) — into the cloud, with only sensors and input/output (IO) units remaining on the trackside and the train. The system uses cloud-based computing and high-speed wireless communication.

Key findings from the study include:
- The SDTC architecture improves **Mean Time Between Failures (MTBF) by 39%** compared to traditional CBTC, as calculated via Markov modelling.
- Warm standby server redundancy reduces maintenance complexity.
- The architecture enables **signalling-as-a-service** (SaaS) by allowing flexible scaling of functions.

- **Source:** Urban Rail Transit (Springer), 2022  
  https://link.springer.com/article/10.1007/s40864-022-00165-y

- **Source:** Academia.edu  
  https://www.academia.edu/90804465/Architecture_Design_and_Reliability_Evaluation_of_a_Novel_Software_Defined_Train_Control_System

### 2.4 Cloud-Edge Computing for Train Control (2025)

A 2025 paper published in *Urban Mass Transit* (Tongji University) analysed the **compatibility of cloud-edge computing with urban rail transit train control systems**. The study explored the feasibility of meeting the **SIL4 safety integrity level** standard using cloud-edge computing technology. It identified three key technical challenges:

1. **Decoupling of data and computing units**
2. **Secure migration strategies**
3. **Distributed fault detection**

The paper proposed a four-dimensional security assessment framework and a unified access control strategy based on virtualisation interfaces, providing a theoretical basis for building a new "cloud-edge-end" collaborative train control system.

- **Source:** Urban Mass Transit, 2025, Vol. 28, No. 8, pp. 202-209,228  
  https://umt1998.tongji.edu.cn/en/article/doi/10.16037/j.1007-869x.20241491

### 2.5 Alstom — Agate and Digital Signalling

Alstom's **Agate** train control and information system brings **IT and cloud technologies onboard**, including AI, cloud computing, and edge computing. The platform enables customers to develop and host their own applications, offering scalability over the train's lifespan. Alstom also offers its **Urbalis CBTC** range for urban signalling, which supports all Grades of Automation (GoA) from driver-assisted to fully driverless operation.

In March 2025, Alstom introduced the **Atlas ETCS Level 3** system, which incorporates **5G communication technology and cloud-based data analytics** for real-time operational insights.

- **Source:** Alstom — Agate  
  https://www.alstom.com/solutions/components/agate-train-control-and-information-systems-enabling-digital-train

- **Source:** Alstom — Urban signalling (Urbalis CBTC)  
  https://www.alstom.com/solutions/signalling/urban-signalling/communications-based-train-control-world-leading-high-capacity-signalling

- **Source:** HTF Market Insights (reporting on Alstom Atlas ETCS Level 3, March 2025)  
  https://www.htfmarketinsights.com/report/4418975-global-communicationsbased-train-control-systems-market

### 2.6 Thales (now Hitachi Rail) — SelTrac G7/G8

Thales (whose urban rail signalling business was acquired by Hitachi Rail) previously launched the **SelTrac G7** and **G8** generations. The G8 system, launched in 2021, incorporated **cloud applications, IoT, 5G, and AI** for decision support and smart maintenance. Thales' SelTrac has been installed on 86 metro lines in 40 cities, transporting over 3 billion passengers per year.

- **Source:** Railway Gazette International, March 2021  
  https://www.railwaygazette.com/infrastructure/2021/03/25/thales-launches-eighth-generation-cbtc-train-control-system

- **Source:** Thales Group — SelTrac G7 launch  
  https://www.thalesgroup.com/en/news-centre/press-releases/thales-launches-seltractm-g7-latest-generation-train-control-system

### 2.7 T-Systems and Hitachi Rail — Digital Interlocking from the Cloud

In Germany, T-Systems (Deutsche Telekom) and Hitachi Rail are collaborating to deliver **digital interlocking systems from the sovereign cloud**. The approach centralises the control logic in the T Cloud, while only the physical switches, barriers, and signals remain trackside. This reduces complexity, safeguards assets from theft, and enables modernisation of legacy signal boxes.

- **Source:** T-Systems — Digital interlockings from the cloud  
  https://www.t-systems.com/de/en/insights/newsroom/expert-blogs/digital-interlockings-from-the-cloud-1087146

### 2.8 Market Context and Growth

The global **Communication-Based Train Control (CBTC) market** was valued at **USD 2.4 billion in 2024** and is projected to grow at a **CAGR of 8.1%** to 2034 (GMInsights) or reach **USD 8.59 billion by 2035** (LinkedIn/Market Growth Reports). According to SCI Verkehr, Europe is currently the world's largest market for digital train control, signalling, and safety systems, accounting for nearly half of the global ~EUR 20 billion CCS market. China dominates Asia with over 65% of regional volume, driven by expansion of high-speed and metro networks and government investment in 5G-based systems.

- **Source:** GMInsights — CBTC Market Report 2025-2034  
  https://www.gminsights.com/industry-analysis/communication-based-train-control-market

- **Source:** Railway PRO, April 2026 (SCI Verkehr study)  
  https://www.railwaypro.com/wp/europe-the-largest-market-for-digital-train-control-and-signalling

- **Source:** LinkedIn/FactMR — CBTC Systems Market  
  https://www.linkedin.com/pulse/communications-based-train-control-systems-market-hdpkf

---

## 3. Key Technologies Enabling Cloud-Based Train Control

### 3.1 Cloud Computing and Edge Computing

Cloud computing provides the centralised, scalable infrastructure for hosting train control applications, data analytics, and system management. However, the ultra-low latency requirements of safety-critical train control functions (e.g., emergency braking, real-time train separation) necessitate **edge computing** — processing data closer to the trackside and train. The combination of cloud and edge creates a **"cloud-edge-end" collaborative architecture**, where:

- **Cloud** handles centralised supervision, analytics, big data processing, and non-real-time functions.
- **Edge** handles real-time, latency-sensitive safety functions close to the trackside.
- **End** devices (onboard controllers, sensors, IO units) are the physical interface with the railway.

The compatibility analysis published in *Urban Mass Transit* (2025) confirmed that cloud-edge computing can meet SIL4 requirements through elastic computing power expansion and distributed redundant architecture.

- **Source:** Urban Mass Transit, 2025  
  https://umt1998.tongji.edu.cn/en/article/doi/10.16037/j.1007-869x.20241491

### 3.2 5G and FRMCS (Future Railway Mobile Communication System)

**5G** is the foundational communication technology for next-generation cloud-based train control, providing the high bandwidth, ultra-reliable low-latency communication (URLLC), and network slicing capabilities needed for real-time train control, video, and IoT data.

**FRMCS (Future Railway Mobile Communication System)** is the global standard, developed by UIC and 3GPP, designed to replace GSM-R. Built on 5G, FRMCS provides a **cloud-based, broadband-ready architecture** that supports:

- Automated train control (ATO)
- Real-time machine-to-machine communication
- Mission-critical voice and data
- Predictive maintenance
- Cross-border interoperability

Nokia launched the **first commercial 5G radio solution for FRMCS** in 2025, featuring a cloud-native 5G standalone core optimised for railway operations. Deutsche Bahn has established a FRMCS/5G test environment in the Ore Mountains, and Ericsson is conducting FRMCS trials in Sweden.

- **Source:** Nokia — FRMCS  
  https://www.nokia.com/industries/railways/frmcs

- **Source:** Converge Digest — Nokia launches 5G FRMCS solution  
  https://convergedigest.com/nokia-launches-5g-frmcs-solution-to-modernize-railways

- **Source:** Global Railway Review — Evolving railway communications for 5G and FRMCS  
  https://www.globalrailwayreview.com/evolving-railway-communications-for-5g-and-frmcs/292557.article

- **Source:** Digitale Schiene Deutschland — FRMCS/5G mobile communication  
  https://digitale-schiene-deutschland.de/en/FRMCS-5G-mobile-communication

### 3.3 Software-Defined Architecture and Virtualisation

Cloud-based train control systems increasingly adopt **software-defined architectures** that decouple the control logic from the underlying hardware. This is achieved through:

- **Virtualisation** — running multiple safety-critical and non-safety applications as virtual machines on the same hardware, with strong partitioning to ensure safety.
- **Containerisation** — using Kubernetes (K8s) and container orchestration platforms to manage distributed applications.
- **Hardware independence** — replacing proprietary, custom hardware with commercial off-the-shelf (COTS) servers, reducing costs and supply chain dependencies.

Wind River Studio, for example, provides a **Kubernetes-based distributed cloud infrastructure** that supports partitioned virtual machines for safety applications, ensuring interference-free operation.

- **Source:** Wind River — Next-Generation Train Control Systems  
  https://www.windriver.com/resource/rail-transportation-use-case

- **Source:** Siemens — Train2Cloud  
  https://www.mobility.siemens.com/global/en/portfolio/digital-solutions-software/infrastructure/signaling-x/train2cloud.html

### 3.4 Artificial Intelligence and Machine Learning

AI and ML are being integrated into cloud-based train control systems at multiple levels:

- **Decision support** — AI helps operators manage incidents and optimise scheduling.
- **Predictive maintenance** — ML algorithms analyse sensor data (vibration, temperature, acoustics) to predict equipment failures before they occur.
- **Computer vision** — AI-based object detection for obstacle avoidance, especially in driverless tram and light rail systems (e.g., OTIV's cloud-based computing platform).
- **Dynamic scheduling** — AI optimises train movements, energy consumption, and passenger flow.

The *Smart Train Control and Monitoring System (TCMS)* with predictive maintenance, published in 2025, demonstrates how cloud-based analytics, ML, and sensor fusion can predict failures in AC, battery, and traction subsystems with severity assessment.

- **Source:** Hatch — Next generation in advanced train control, July 2025  
  https://www.hatch.com/About-Us/Publications/Blogs/2025/07/Next-generation-in-advanced-train-control-A-smart-response-to-urban-growth

- **Source:** OTIV (startup) — cloud-based autonomous driving for trams/light rail  
  https://www.skyquestt.com/report/urban-rail-transit-market

- **Source:** Smart TCMS with predictive maintenance (ScienceDirect, 2025)  
  https://www.sciencedirect.com/science/article/pii/S2590198225000880

### 3.5 Digital Twin Technology

Digital twins — virtual replicas of physical assets, systems, and processes — are becoming a critical enabler for cloud-based train control. They allow:

- **Real-time monitoring** of track, rolling stock, and signalling equipment.
- **Predictive maintenance** by simulating wear and failure modes.
- **Scenario simulation** for testing operational changes without disrupting service.
- **Lifecycle management** of assets.

A systematic review published in 2025 identified IoT, AI, and cloud computing as critical enablers for digital twin implementation in railways, with challenges including data integration, high costs, and cybersecurity.

- **Source:** ScienceDirect — Revolutionizing railway systems: A systematic review of digital twin technologies (2025)  
  https://www.sciencedirect.com/science/article/pii/S2949867825000273

- **Source:** Envision Rail Management — Digital Twins for Metro Efficiency  
  https://www.envisionesl.com/blog/digital-twins-metro-maintenance-planning

### 3.6 Cybersecurity and Zero-Trust Architectures

As train control systems move to the cloud, cybersecurity becomes paramount. Cloud-based systems introduce new attack surfaces that must be mitigated. Key approaches include:

- **Zero-trust network architectures** — where no device or user is trusted by default, even within the network perimeter.
- **Self-learning trust algorithms** for intelligent urban railway cloud platforms.
- **Secure migration strategies** for moving safety-critical functions to the cloud.
- **Unified access control** based on virtualisation interfaces.

- **Source:** ACM — Secure Mechanism of Intelligent Urban Railway Cloud Platform (2022)  
  https://dl.acm.org/doi/abs/10.1145/3546000.3546015

- **Source:** Global Railway Review — All intelligence-first rail (2025)  
  https://www.globalrailwayreview.com/all-intelligence-first-rail-is-shaping-the-future-of-the-industry/383031.article

### 3.7 Communication-Based Train Control (CBTC) Evolution

CBTC remains the foundational technology for urban rail train control, and its evolution is central to the cloud transition. Modern CBTC systems:

- Use **moving-block** signalling (rather than fixed-block) to reduce headways to 90 seconds or less.
- Support **all Grades of Automation (GoA)** from GoA 1 (driver-assisted) to GoA 4 (fully driverless/UTO).
- Increasingly rely on **Wi-Fi, LTE, and 5G** for train-to-wayside communication.
- Are being enhanced with **train-to-train (T2T) communication** for even faster and more distributed control.

Future CBTC systems will benefit from **cloud-based data analytics** for operational insights, as demonstrated by Alstom's Atlas ETCS Level 3.

- **Source:** Wikipedia — Communications-based train control  
  https://en.wikipedia.org/wiki/Communications-based_train_control

- **Source:** Pacific Blue Engineering — CBTC Systems and Transit Control Guide  
  https://pacificblueengineering.com/cbtc-systems-transit-control-complete-guide

- **Source:** Hitachi Rail — Urban Rail Control & Supervision  
  https://www.hitachirail.com/products-and-solutions/urban-rail-control-supervision

---

## 4. Architecture Overview

The emerging architecture of cloud-based train control systems can be summarised as a **layered, cloud-edge-end collaborative model**:

| Layer | Components | Functions |
|-------|------------|-----------|
| **Cloud Layer** | Central data centres, cloud platforms (private/hybrid) | Centralised ATS, big data analytics, AI/ML, digital twin, fleet management, remote monitoring, cybersecurity management |
| **Edge Layer** | Wayside edge servers, signalling data centres (on-premise) | Zone control (ZC), interlocking (CI/CBI), radio block centre (RBC), real-time train separation, ATP |
| **Communication Layer** | 5G/FRMCS, LTE, IP/MPLS, network slicing | Ultra-reliable low-latency communication, train-to-wayside, train-to-train, IoT connectivity |
| **End / Field Layer** | Onboard controllers (VOBC), sensors, IO units, signals, switches, track circuits, axle counters | Physical train control, position detection, actuator control, data acquisition |

The key innovation is that **safety-critical functions need not all reside in proprietary hardware at the trackside**. Through virtualisation, strong partitioning (e.g., DS3 safety platform), and high-reliability cloud infrastructure, functions such as interlocking, ATP, and even some VOBC functions can be deployed in the cloud/edge data centre, with only the minimum necessary IO and sensor hardware remaining in the field.

- **Source:** Springer — SDTC Architecture (2022)  
  https://link.springer.com/article/10.1007/s40864-022-00165-y

- **Source:** Siemens — Train2Cloud  
  https://www.mobility.siemens.com/global/en/portfolio/digital-solutions-software/infrastructure/signaling-x/train2cloud.html

---

## 5. Challenges and Considerations

Despite the significant progress, several challenges remain:

1. **Safety Certification (SIL4)** — Ensuring that cloud-based virtualised systems can meet the highest safety integrity level (SIL4) is a major challenge. The DS3 platform and the cloud-edge framework from Tongji University are pioneering efforts to address this.

2. **Latency and Determinism** — Safety-critical train control functions require deterministic, low-latency responses. Edge computing is essential to meet these requirements, but the distribution of functions between cloud and edge must be carefully architected.

3. **Cybersecurity** — Cloud-based systems increase the attack surface. Zero-trust, secure migration, and virtualisation-based access control are key mitigation strategies.

4. **Interoperability** — Legacy systems, different CBTC/ETCS standards, and proprietary vendor implementations must coexist. Open architectures (e.g., Signaling X) and standardised interfaces (e.g., FRMCS) are part of the solution.

5. **Data Integration and Silos** — OT (operational technology) data is often siloed across different systems and suppliers. Standardised APIs, containerisation, and open data platforms are needed to break down these silos.

6. **Cost of Migration** — Brownfield (retrofit) migration from legacy signalling to cloud-based CBTC is expensive and complex. The MTA in New York, for example, committed over $2 billion to transition legacy signalling to CBTC.

- **Source:** MDPI — Toward Smart Railway Infrastructure Predictive Maintenance (2026)  
  https://www.mdpi.com/1424-8220/26/8/2333

- **Source:** Cisco — Rail CBTC and Safety Design Guide (2024)  
  https://www.cisco.com/c/dam/en/us/td/docs/solutions/Verticals/Transportation/Rail-CBTC/Rail_CBTC_Design_Guide.pdf

---

## 6. Future Outlook

The direction of travel is clear: **"Go Broadband, Go Cloud, Go Intelligence"** (as articulated by Huawei at Connect 2025). The convergence of cloud-native architectures, 5G/FRMCS, AI, digital twins, and edge computing will enable:

- **Fully autonomous, driverless metro operations** (GoA 4) at scale.
- **Dynamic capacity management** — adjusting headways and scheduling in real-time based on demand.
- **Predictive and prescriptive maintenance** — reducing downtime and extending asset life.
- **Signalling-as-a-Service (SaaS)** — flexible, scalable, hardware-independent train control.
- **Seamless integration** between urban rail, mainline, and high-speed networks.

The market is expected to continue its strong growth trajectory, with Europe leading in modernisation and China leading in new-build deployments, and increasing investment in cloud-based signalling technologies from all major suppliers.

- **Source:** Global Railway Review — All intelligence-first rail (2025)  
  https://www.globalrailwayreview.com/all-intelligence-first-rail-is-shaping-the-future-of-the-industry/383031.article

- **Source:** Hatch — Next generation in advanced train control (2025)  
  https://www.hatch.com/About-Us/Publications/Blogs/2025/07/Next-generation-in-advanced-train-control-A-smart-response-to-urban-growth

---

## 7. References

| # | Reference | URL |
|---|-----------|-----|
| 1 | Hitachi Rail / Invest Ontario — SelTrac G9 investment (Nov 2024) | https://www.railway-technology.com/news/hitachi-rail-urban-rail-signalling-canada |
| 2 | Mass Transit Magazine — Hitachi Rail, Invest Ontario to fund C$100M (Nov 2024) | https://www.masstransitmag.com/rail/railroad-signals-ptc-control-systems-and-products/press-release/55245968/hitachi-rail-hitachi-rail-invest-ontario-to-fund-c100-million-to-upgrade-cbtc-signaling-technology |
| 3 | Siemens Mobility — Train2Cloud | https://www.mobility.siemens.com/global/en/portfolio/digital-solutions-software/infrastructure/signaling-x/train2cloud.html |
| 4 | Siemens Press — First signalling in the cloud in operation | https://press.siemens.com/global/en/pressrelease/first-signalling-cloud-operation |
| 5 | Railway Gazette International — Train control moves into the cloud (Siemens white paper) | https://www.railwaygazette.com/whitepaper/train-control-moves-into-the-cloud-sponsored-by-siemens-mobility |
| 6 | Springer — Architecture Design and Reliability Evaluation of SDTC (Urban Rail Transit, 2022) | https://link.springer.com/article/10.1007/s40864-022-00165-y |
| 7 | Academia.edu — SDTC paper | https://www.academia.edu/90804465/Architecture_Design_and_Reliability_Evaluation_of_a_Novel_Software_Defined_Train_Control_System |
| 8 | Tongji University — Compatibility Analysis of Urban Rail Transit Train Control System and Cloud-Edge Computing (Urban Mass Transit, 2025) | https://umt1998.tongji.edu.cn/en/article/doi/10.16037/j.1007-869x.20241491 |
| 9 | Alstom — Agate Train Control and Information Systems | https://www.alstom.com/solutions/components/agate-train-control-and-information-systems-enabling-digital-train |
| 10 | Alstom — Urban signalling (Urbalis CBTC) | https://www.alstom.com/solutions/signalling/urban-signalling/communications-based-train-control-world-leading-high-capacity-signalling |
| 11 | Thales Group — SelTrac G7 launch | https://www.thalesgroup.com/en/news-centre/press-releases/thales-launches-seltractm-g7-latest-generation-train-control-system |
| 12 | Railway Gazette — Thales launches eighth generation CBTC (2021) | https://www.railwaygazette.com/infrastructure/2021/03/25/thales-launches-eighth-generation-cbtc-train-control-system |
| 13 | T-Systems — Digital interlockings from the cloud | https://www.t-systems.com/de/en/insights/newsroom/expert-blogs/digital-interlockings-from-the-cloud-1087146 |
| 14 | Nokia — FRMCS (Future Railway Mobile Communication System) | https://www.nokia.com/industries/railways/frmcs |
| 15 | Converge Digest — Nokia launches 5G FRMCS solution | https://convergedigest.com/nokia-launches-5g-frmcs-solution-to-modernize-railways |
| 16 | Global Railway Review — Evolving railway communications for 5G and FRMCS | https://www.globalrailwayreview.com/evolving-railway-communications-for-5g-and-frmcs/292557.article |
| 17 | Digitale Schiene Deutschland — FRMCS/5G mobile communication | https://digitale-schiene-deutschland.de/en/FRMCS-5G-mobile-communication |
| 18 | GMInsights — CBTC Market Report 2025-2034 | https://www.gminsights.com/industry-analysis/communication-based-train-control-market |
| 19 | Railway PRO — Europe the largest market for digital train control (April 2026) | https://www.railwaypro.com/wp/europe-the-largest-market-for-digital-train-control-and-signalling |
| 20 | Wind River — Next-Generation Train Control Systems | https://www.windriver.com/resource/rail-transportation-use-case |
| 21 | Hatch — Next generation in advanced train control (July 2025) | https://www.hatch.com/About-Us/Publications/Blogs/2025/07/Next-generation-in-advanced-train-control-A-smart-response-to-urban-growth |
| 22 | Global Railway Review — All intelligence-first rail (2025) | https://www.globalrailwayreview.com/all-intelligence-first-rail-is-shaping-the-future-of-the-industry/383031.article |
| 23 | ScienceDirect — Revolutionizing railway systems: A systematic review of digital twin technologies (2025) | https://www.sciencedirect.com/science/article/pii/S2949867825000273 |
| 24 | ACM — Secure Mechanism of Intelligent Urban Railway Cloud Platform (2022) | https://dl.acm.org/doi/abs/10.1145/3546000.3546015 |
| 25 | Wikipedia — Communications-based train control | https://en.wikipedia.org/wiki/Communications-based_train_control |
| 26 | Pacific Blue Engineering — CBTC Systems and Transit Control Guide | https://pacificblueengineering.com/cbtc-systems-transit-control-complete-guide |
| 27 | Hitachi Rail — Urban Rail Control & Supervision | https://www.hitachirail.com/products-and-solutions/urban-rail-control-supervision |
| 28 | Cisco — Rail CBTC and Safety Design Guide (2024) | https://www.cisco.com/c/dam/en/us/td/docs/solutions/Verticals/Transportation/Rail-CBTC/Rail_CBTC_Design_Guide.pdf |
| 29 | Envision Rail Management — Digital Twins for Metro Efficiency | https://www.envisionesl.com/blog/digital-twins-metro-maintenance-planning |
| 30 | ScienceDirect — Smart TCMS with predictive maintenance (2025) | https://www.sciencedirect.com/science/article/pii/S2590198225000880 |
| 31 | MDPI — Toward Smart Railway Infrastructure Predictive Maintenance (2026) | https://www.mdpi.com/1424-8220/26/8/2333 |
| 32 | SkyQuest — Urban Rail Transit Market Report (OTIV) | https://www.skyquestt.com/report/urban-rail-transit-market |
| 33 | LinkedIn / HTF Market Insights — CBTC Systems Market | https://www.htfmarketinsights.com/report/4418975-global-communicationsbased-train-control-systems-market |
| 34 | LinkedIn / FactMR — CBTC Market | https://www.linkedin.com/pulse/communications-based-train-control-systems-market-hdpkf |

---

*This report is based on publicly available information as of August 2026. The field of cloud-based train control is evolving rapidly, and readers are encouraged to consult the referenced sources for the most current details.*

