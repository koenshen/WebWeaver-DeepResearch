
# Liability Allocation in Accidents Involving Vehicles with Advanced Driver-Assistance Systems (ADAS): A Comprehensive Analysis of Shared Human-Machine Responsibility

## 1. Introduction

The rapid deployment of vehicles equipped with Advanced Driver-Assistance Systems (ADAS) operating at SAE Levels 2 and 3 has created a complex liability landscape. Unlike fully autonomous vehicles, these systems operate in a shared-control paradigm where the human driver and the automated system divide the driving task, often in fluid and context-dependent ways. This shared mode creates a fundamental tension: traditional legal frameworks assume a single human driver is in control, while the technical reality involves a dynamic partnership between human and machine. This report integrates technical principles, existing legal frameworks, and relevant case law to systematically examine the boundaries of responsibility between the driver and the system, and concludes with proposed regulatory guidelines.

---

## 2. Technical Principles of ADAS and the SAE Framework

### 2.1 The SAE J3016 Taxonomy

The Society of Automotive Engineers (SAE) International Standard J3016 defines six levels of driving automation, which form the technical foundation for liability allocation[^1][^2]:

| SAE Level | Name | Who Monitors Environment | Who Performs Dynamic Driving Task | Fallback Performance |
|-----------|------|------------------------|----------------------------------|---------------------|
| 0 | No Automation | Driver | Driver | Driver |
| 1 | Driver Assistance | Driver | Driver + System (either steering OR accel/brake) | Driver |
| 2 | Partial Automation | Driver | System (both steering AND accel/brake) | Driver |
| 3 | Conditional Automation | System | System | Driver (fallback-ready) |
| 4 | High Automation | System | System | System |
| 5 | Full Automation | System | System | System |

### 2.2 The Critical Distinction: Level 2 vs. Level 3

The most consequential legal distinction lies between Level 2 and Level 3. At Level 2, the driver must remain fully engaged and monitor the road environment at all times. The system provides continuous assistance with steering, acceleration, and braking, but the driver retains ultimate responsibility[^3]. At Level 3, the system monitors the environment and handles the dynamic driving task within its Operational Design Domain (ODD). The driver may disengage from driving and engage in other activities—such as reading or watching a movie—but must be available to take over when the system requests a transition[^4].

This distinction is not merely technical. It fundamentally alters the legal attribution of responsibility. At Level 2, the driver is legally the "driver" in the traditional sense. At Level 3, the system becomes the primary driver, and the human becomes a fallback-ready supervisor.

### 2.3 The Handover Problem

The handover (or transition of control) from system to human is the most technically and legally problematic aspect of Level 3 automation. When the system encounters a situation outside its ODD—such as construction zones, severe weather, or unmapped roads—it must issue a takeover request (TOR) to the human driver with sufficient lead time. Research has identified several critical challenges[^5][^6]:

- **Automation bias**: Drivers become over-reliant on the system and fail to monitor the road adequately, even when required to do so.
- **Out-of-the-loop unfamiliarity**: Drivers who have been disengaged from the driving task require significant time to regain situational awareness.
- **Insufficient transition time**: The system may underestimate the time required for safe handover, particularly in complex scenarios.
- **Driver state monitoring limitations**: Camera-based driver monitoring systems may fail to detect impairment, drowsiness, or distraction.

### 2.4 Operational Design Domain (ODD) and System Limitations

Each ADAS is designed to operate only within a specific ODD—the conditions under which the system is designed to function. Mercedes-Benz's Drive Pilot, for example, is only approved for use on mapped German highways at speeds below 60 km/h[^7]. When the vehicle exits the ODD, the system must issue a TOR. If the system fails to detect an ODD boundary condition, or if the driver fails to respond to a TOR, liability becomes ambiguous.

---

## 3. Existing Legal Frameworks

### 3.1 International Legal Framework

#### 3.1.1 Vienna Convention on Road Traffic (1968)

The Vienna Convention traditionally required that "every moving vehicle or combination of vehicles shall have a driver" (Article 8) and that "every driver shall at all times be able to control his vehicle" (Article 8(5)). These provisions were historically interpreted as requiring a human driver to be in control at all times.

In March 2016, an amendment added Article 8(5bis), which allows automated driving systems to satisfy the requirement that a driver be in control, provided the system can be overridden or switched off by the driver[^8]. A further amendment proposed in 2021 (Article 34 bis) more explicitly allows automated driving systems to fulfill the driver role if they comply with domestic technical regulations and international legal instruments[^9]. These amendments provide the international legal foundation for Level 3 and Level 4 systems.

#### 3.1.2 UN Regulation No. 157 (Automated Lane Keeping Systems)

UN Regulation No. 157, adopted by the UN Economic Commission for Europe (UNECE), provides the first internationally harmonized type-approval requirements for SAE Level 3 systems. Key provisions relevant to liability include[^10][^11]:

- The ALKS must be in "primary control" of the vehicle while active.
- The driver must remain "available" to take over and must be monitored by a driver monitoring system.
- The system must issue transition demands that allow sufficient time for the driver to resume control.
- If the driver does not respond to a transition demand, the system must perform a Minimum Risk Maneuver (MRM), bringing the vehicle to a safe stop.
- The system must include a Data Storage System for Automated Driving (DSSAD) to record when the system is engaged and when it issues transition demands.

The regulation does not directly address liability, but it establishes the technical baseline that national liability frameworks rely upon. The requirement for a DSSAD is particularly important for determining fault in post-accident investigations.

### 3.2 National Legal Frameworks

#### 3.2.1 Germany

Germany has been at the forefront of establishing a legal framework for automated driving. The 2017 amendment to the Road Traffic Act (StVG) was the first in the world to regulate Level 3 and Level 4 systems[^12][^13].

**Key provisions:**

- **Sections 1a and 1b StVG**: Define the rights and duties of drivers using highly or fully automated driving functions. The driver may delegate the driving task to the system but must remain alert and capable of taking over control without undue delay when the system prompts or when the driver realizes the conditions for automated operation are no longer met.
- **Section 63a StVG**: Mandates the installation of a "black box" (DSSAD) that records data on whether the vehicle or the driver was in control, when takeover requests were issued, and when the system was deactivated.
- **Increased liability limits**: The maximum strict liability for the vehicle holder was doubled to €10 million for personal injury and €2 million for property damage when a highly or fully automated driving function is engaged[^14].
- **Autonomous Driving Act (2021)**: Further extended the framework to allow Level 4 driverless vehicles in defined operating areas, introducing the concept of a "Technical Supervisor" who can remotely monitor and intervene.

The German approach establishes a presumption of driver liability when the system is not engaged, and a potential shift toward manufacturer liability when the system is active and the driver was not at fault. The DSSAD data is critical for determining which party was in control at the time of the crash.

#### 3.2.2 United Kingdom

The UK has established a comprehensive two-part legislative framework.

**Automated and Electric Vehicles Act 2018 (AEVA 2018)**[^15][^16]:

- Provides that when an accident is caused by an automated vehicle driving itself on a road or public place in Great Britain, the insurer is primarily liable for damage to the insured person or any other person.
- This is a strict liability regime—the insurer must pay regardless of whether the manufacturer or the driver was at fault.
- The insurer may then recover costs from the party actually at fault (e.g., the manufacturer, software developer, or other responsible party) through subrogation.
- The Act applies to vehicles listed by the Secretary of State as "automated vehicles," which must be capable of driving themselves without human monitoring.

**Automated Vehicles Act 2024 (AVA 2024)**[^17][^18][^19]:

- Establishes the "user-in-charge" (UiC) concept—a person who is in position to control the vehicle but is not liable for the manner of driving while the vehicle is driving itself.
- Section 47 provides that the UiC is not liable for the manner of driving when the vehicle is operating in automated mode.
- Exceptions from immunity apply if the UiC fails to comply with duties (e.g., failing to take control when required, failing to ensure the vehicle is in a roadworthy condition, or tampering with the system).
- Creates a new regulatory framework for authorizing, operating, and regulating self-driving vehicles.
- Establishes that corporations (manufacturers, software developers, insurers) can be held responsible for the driving behavior of automated vehicles.

The UK framework is notable for its clarity: when the system is in automated mode, the human user is explicitly immune from liability for the manner of driving, and the insurer is the first point of compensation.

#### 3.2.3 United States

The United States lacks a comprehensive federal framework for automated vehicle liability. Instead, a patchwork of state laws, federal safety regulations, and common law tort principles governs liability.

**Federal Level:**

- **NHTSA Standing General Order 2021-01**: Requires manufacturers and operators of vehicles equipped with Level 2 ADAS or Levels 3-5 ADS to report crashes involving these systems[^20][^21]. This data collection is essential for identifying safety defects and informing liability determinations.
- **No federal preemption of liability**: The federal motor vehicle safety standards do not exempt manufacturers from common law liability. The failed AV START Act (2017-2018) would have established a federal framework but never passed[^22][^23].
- **NHTSA does not have a formal AV liability rule**: The agency relies on its existing authority to investigate defects and issue recalls. The Trump administration's 2025 framework streamlined crash reporting requirements for AVs[^24].

**State Level:**

State approaches vary significantly. California has the most developed regulatory framework:

- **California DMV regulations**: Require manufacturers to obtain permits for testing and deployment, report collisions, and maintain insurance coverage[^25].
- **Assembly Bill 1777 (2025)**: Holds manufacturers or operators liable for traffic violations committed by their autonomous vehicles, allowing law enforcement to issue citations directly to the manufacturer[^26].
- **Strict product liability**: California applies strict liability principles, meaning injured parties do not need to prove negligence, only that the product was defective.

Several states (e.g., Florida, Texas, Michigan) have enacted laws that clarify that when an automated driving system is engaged, the system is deemed the "driver" or "operator" for purposes of liability[^27].

**Product Liability Regime:**

Under US product liability law, claims against ADAS manufacturers can be based on three theories[^28][^29]:

1. **Design defects**: The system's design is unreasonably dangerous. For ADAS, this might include inadequate driver monitoring, failure to warn of limitations, or algorithms that misjudge traffic scenarios.
2. **Manufacturing defects**: A specific unit deviates from the intended design (e.g., faulty sensor).
3. **Failure to warn**: The manufacturer failed to adequately disclose the system's limitations or operational requirements.

Courts increasingly treat the ADAS or ADS as the "product" subject to product liability standards, not merely a component of the vehicle[^30].

#### 3.2.4 China

China has taken a more experimental approach, with regional exemptions and special regulations. Shenzhen permitted fully autonomous vehicles on certain roads from 2022. Mercedes-Benz received approval to test Level 3 systems in Beijing in December 2023[^31]. The Chinese approach is developing rapidly but remains fragmented, with liability allocation primarily governed by revisions to the Road Traffic Safety Law and product liability principles.

### 3.3 Insurance Frameworks

The shift from human driver to automated system has profound implications for insurance. Key developments include[^32][^33]:

- **Hybrid policies**: Some insurers offer policies that split coverage between the driver (when operating manually) and the manufacturer/technology provider (when ADAS is engaged).
- **Product liability insurance**: Manufacturers and software developers are increasingly expected to carry product liability policies that cover failures of the automated system.
- **Shifting loss ratios**: As higher levels of automation are deployed, the proportion of liability attributable to human error decreases, while the proportion attributable to product defects increases.
- **Partnerships**: Insurance companies are partnering with technology providers (e.g., Munich Re and Mobileye, Swiss Re and Baidu) to develop data-driven risk assessment models for AVs.

---

## 4. Relevant Case Law

### 4.1 Tesla Autopilot Cases (Level 2 ADAS)

Tesla's Autopilot system is classified as SAE Level 2, meaning the driver must remain engaged and attentive at all times. However, Tesla's marketing—using names like "Autopilot" and "Full Self-Driving"—has been a central issue in litigation, with plaintiffs arguing that the company's branding encouraged over-reliance on the system.

#### 4.1.1 *Benavides v. Tesla* (2025, Florida Federal Jury)

In August 2025, a Miami federal jury rendered the first verdict holding Tesla liable for a fatal Autopilot-involved crash[^34][^35]. The jury found Tesla 33% responsible for the crash, with the driver bearing 67% fault. The verdict included approximately $129 million in compensatory damages (Tesla's share: ~$43 million) and $200 million in punitive damages. The case centered on two questions:

1. Whether Autopilot was defectively designed because it could be activated in unsafe conditions and failed to adequately monitor driver attention.
2. Whether Tesla's marketing suggested capabilities beyond what the system could safely deliver, supporting punitive damages.

The verdict is on appeal, but it signals that juries are willing to assign significant liability to manufacturers when ADAS design and marketing contribute to accidents.

#### 4.1.2 Additional Tesla Cases

- **Walter Huang settlement (2024)**: Tesla settled a wrongful death lawsuit on the eve of trial involving a 2018 crash where a Model X on Autopilot struck a highway barrier. The settlement was confidential[^36].
- **Jovani Maldonado Garcia settlement (2025)**: Tesla settled a confidential wrongful death case involving a 2019 crash where a Model 3 allegedly operating on Autopilot killed a 15-year-old boy[^37].
- **NHTSA investigations**: NHTSA opened a formal investigation into Autopilot in 2021 and closed it in 2024 while opening a recall-effectiveness review, linking Autopilot engagement to numerous fatal and severe-injury crashes[^38].

#### 4.1.3 Legal Significance

The Tesla cases establish several important precedents for Level 2 ADAS liability:

- **Manufacturer liability is not precluded by driver responsibility**: Even where the driver is primarily at fault, manufacturers can be held partially liable for design defects and inadequate warnings.
- **Marketing matters**: Overstated claims of capability can support punitive damages and shift liability toward the manufacturer.
- **Driver monitoring adequacy is a key issue**: Systems that fail to adequately monitor driver engagement may be found defectively designed.

### 4.2 Uber ATG Crash (2018, Arizona)

The first fatality involving a fully autonomous vehicle occurred in March 2018 when an Uber test vehicle (a Volvo XC90 equipped with Uber's prototype Level 3/4 system) struck and killed Elaine Herzberg in Tempe, Arizona[^39][^40].

**Key findings:**

- **Criminal liability**: Arizona prosecutors determined that Uber was not criminally responsible. The safety driver, Rafaela Vasquez, was charged with negligent homicide, pled guilty to endangerment, and received three years of probation[^41].
- **Technical failures**: The Uber vehicle's software had detected the pedestrian but classified her as a "false positive" and did not initiate braking. The emergency braking system had been disabled by Uber.
- **Safety driver distraction**: Vasquez was streaming an episode of *The Voice* on her phone at the time of the crash.
- **NTSB investigation**: The National Transportation Safety Board found that the probable cause was the safety driver's failure to monitor the road, combined with the inadequate safety culture and system design at Uber.

**Legal significance**: The Uber case illustrates the "handover problem" in its most extreme form. The system was designed to handle the driving task but failed to detect and respond to a pedestrian. The safety driver was supposed to intervene but was distracted. The result was that the safety driver—not the manufacturer—bore the criminal consequences, while Uber avoided criminal liability but faced civil lawsuits and reputational damage.

### 4.3 Mercedes-Benz Drive Pilot Liability

Mercedes-Benz has taken a unique position by publicly stating that it will accept legal liability for accidents caused when its Drive Pilot Level 3 system is engaged[^7][^42]. This has been widely reported as a significant industry first.

However, the precise scope of this liability acceptance is contested. Critics, including safety expert Phil Koopman, have argued that Mercedes-Benz's statements have been misleading[^43][^44]:

- **Initial position (2022)**: Mercedes-Benz suggested that "once you engage Drive Pilot, you are no longer legally liable for the car's operation until it disengages."
- **Refined position (2023-2024)**: Mercedes-Benz clarified that it accepts product liability—meaning it will pay for damages caused by defects in its system—but that the driver retains tort liability for negligence, such as failing to respond to takeover requests or using the system outside its ODD.
- **Koopman's critique**: Mercedes-Benz's representatives have stated that the human driver retains the duty of care for potential harm to other road users even when using Drive Pilot, undermining the claim that the company "takes responsibility."

This ambiguity highlights a critical gap between marketing claims and legal reality. Even where a manufacturer accepts product liability, the driver may still face negligence claims if they fail to fulfill their fallback duties.

### 4.4 Waymo Incidents (Level 4)

Waymo operates Level 4 autonomous vehicles in several US cities, primarily in San Francisco, Phoenix, and Los Angeles. These vehicles operate without a human driver in the driver's seat.

**Key incidents**[^45][^46]:

- **January 2025 fatal collision (San Francisco)**: A Waymo vehicle was stopped in traffic at a red light when a Tesla traveling at approximately 95 mph struck multiple stopped vehicles, including the Waymo. One person was killed. The Waymo was unoccupied and was not at fault.
- **May 2025 recall**: Waymo voluntarily recalled software after two of its vehicles struck the same towed cargo in separate incidents, marking the first recall of a fully autonomous vehicle due to a software defect.
- **October 2024 collision**: A Waymo was hit by a vehicle that crossed a double yellow line and struck another vehicle, which then hit the Waymo.
- **December 2025 traffic standoff**: Two Waymo vehicles appeared to collide on a dead-end street, and three Waymos created a traffic jam that blocked residents.

**Legal significance**: Waymo's Level 4 operations eliminate the driver as a responsible party. Liability falls entirely on the manufacturer, operator, or software developer. The January 2025 fatal collision, while not the Waymo's fault, raises questions about the liability of autonomous vehicle companies when they are involved in multi-vehicle collisions where they are not the primary cause. The recall demonstrates that product liability principles apply fully to Level 4 systems.

---

## 5. Analysis of Liability Boundaries

### 5.1 The Spectrum of Responsibility

The allocation of liability in ADAS accidents can be conceptualized as a spectrum based on the SAE level and the specific circumstances of the crash:

| Scenario | Likely Liable Party | Rationale |
|----------|-------------------|-----------|
| Driver manually driving | Driver | Traditional negligence |
| Level 2 engaged, driver fails to monitor | Driver (primary) + Manufacturer (secondary) | Driver has monitoring duty; manufacturer may share liability for design defects |
| Level 2 engaged, system malfunctions | Manufacturer | Product defect |
| Level 3 engaged, system fails to detect hazard | Manufacturer | System is in primary control |
| Level 3 engaged, driver fails to respond to TOR | Driver (primary) + Manufacturer (potential) | Driver has duty to take over; manufacturer may share liability if TOR was inadequate |
| Level 3 engaged, driver asleep | Driver | Driver violated duty to remain available |
| Level 4 engaged, system error | Manufacturer/Operator | No human driver to bear responsibility |
| Level 4 engaged, third-party causes crash | Third-party driver | Traditional negligence; manufacturer may have secondary liability for design |

### 5.2 The Level 2 Liability Conundrum

The majority of ADAS-equipped vehicles on the road today are Level 2 systems. The legal challenge is that Level 2 requires the driver to be "fully engaged and attentive," but the system performs the dynamic driving task, creating a tension between what the law requires and what human psychology permits[^47][^48].

Research on automation bias confirms that humans are poor at monitoring automated systems for extended periods. Drivers become complacent, trust the system beyond its capabilities, and are slow to respond when intervention is needed[^49]. Courts are beginning to recognize this reality. The *Benavides* verdict suggests that manufacturers cannot simply rely on the Level 2 label to avoid liability; they must design systems that account for foreseeable human limitations.

### 5.3 The Level 3 Handover Problem

Level 3 systems create a "responsibility gap" during the handover period. The system is driving, but the driver must be ready to take over. Key questions include[^50][^51]:

- **Who is responsible during the transition period?** If the system issues a TOR requesting driver takeover, but the driver is slow to respond, is the system responsible for failing to allow sufficient time, or is the driver responsible for failing to respond promptly?
- **What constitutes "sufficient" transition time?** UN R157 requires that the system provide sufficient time, but what is sufficient depends on the specific scenario and the driver's state.
- **What if the system fails to detect an ODD boundary?** If the system continues operating outside its ODD without issuing a TOR, and a crash occurs, the manufacturer is likely liable.
- **What if the driver is incapacitated?** If the driver has a medical emergency and cannot respond to a TOR, the system must perform a Minimum Risk Maneuver. If the MRM is inadequate, the manufacturer may be liable.

### 5.4 Product Liability and the "Computer Driver" Standard

Scholars have proposed that when an automated driving system is engaged, the system should be held to the standard of a "competent, attentive, and unimpaired human driver"[^52][^53]. If the system fails to meet this standard, the manufacturer is liable. This approach has several advantages:

- It provides a clear, objective benchmark for evaluating system performance.
- It aligns with the reasonable person standard in negligence law.
- It avoids the need to prove specific technical defects in complex software.

The UK's Automated Vehicles Act 2024 adopts a similar approach by requiring that automated vehicles be "capable of driving safely and legally" without human intervention, and by holding corporations responsible for the manner of driving[^18].

### 5.5 Evidence and Data Recording

The availability of data is critical for liability determination. Key data sources include[^54][^55]:

- **Event Data Recorders (EDRs)**: Record vehicle dynamics data (speed, braking, steering) in the moments before and during a crash. These are required in US vehicles under 49 CFR Part 563.
- **Data Storage System for Automated Driving (DSSAD)**: Specifically designed for automated vehicles, these record when the system is engaged, when takeover requests are issued, and whether the driver responded. Required under UN R157.
- **Driver Monitoring System (DMS) data**: Records information about driver attention, eye gaze, and readiness to take over.
- **Sensor and perception data**: Records what the vehicle's sensors detected and how the system interpreted the environment.

The availability of this data is essential for determining whether the driver or the system was in control, whether the system issued adequate warnings, and whether the driver was paying attention. However, data access and privacy concerns remain significant barriers to effective liability determination.

---

## 6. Challenges and Gaps

### 6.1 Regulatory Fragmentation

The lack of a harmonized international framework for ADAS liability creates uncertainty for manufacturers, insurers, and consumers. While the UNECE has established technical standards through UN R157, liability allocation remains a matter of national law. In the US, the absence of federal legislation means that 50 different state liability regimes may apply, creating significant compliance burdens and jurisdictional uncertainty[^56].

### 6.2 The "Responsibility Gap"

As systems become more autonomous, the traditional concept of "driver" becomes increasingly difficult to apply. If a Level 4 vehicle causes a crash, there is no human driver to hold responsible. The law must determine whether liability falls on the manufacturer, the software developer, the fleet operator, the remote operator, or some combination of these parties. Current legal frameworks are often ill-equipped to answer this question.

### 6.3 The Knowledge Gap

The "consumer expectations test" in product liability law requires courts to determine what an ordinary consumer would expect from a product. For highly complex ADAS systems, consumers have limited understanding of system capabilities and limitations. Courts may struggle to determine what constitutes a reasonable consumer expectation for a system that uses machine learning and operates in ways that are not transparent to the user[^57].

### 6.4 The Algorithmic Black Box

Machine learning algorithms used in ADAS are often opaque, making it difficult to determine why a system made a particular decision. This "black box" problem creates significant challenges for plaintiffs who must prove that a specific defect caused an accident. Manufacturers may resist disclosure of proprietary algorithms, while plaintiffs may lack the technical expertise to evaluate system behavior.

### 6.5 Cybersecurity and Third-Party Interference

ADAS systems are vulnerable to cyberattacks, software bugs, and over-the-air update failures. If a third party hacks an ADAS system and causes a crash, the liability implications are complex. The manufacturer may be liable for inadequate cybersecurity, or the insurer may be liable under the primary insurance framework, with the right to recover from the hacker.

---

## 7. Regulatory Guidelines and Recommendations

Based on the technical, legal, and case law analysis above, the following regulatory guidelines are proposed:

### 7.1 Establish a Clear Legal Baseline for SAE Levels

**Recommendation**: Legislatures should enact laws that explicitly define the legal status of the driver and the system for each SAE level. The UK's AVA 2024 approach—which provides that the user-in-charge is not liable for the manner of driving when the vehicle is driving itself—should serve as a model. For Level 2, the law should clarify that the driver retains primary responsibility but that manufacturers can be held liable for design defects that fail to account for foreseeable human over-reliance.

### 7.2 Mandate Adequate Data Recording

**Recommendation**: All vehicles with Level 2 or higher ADAS should be required to include a DSSAD that records, at minimum:
- When the system is engaged and disengaged.
- Takeover requests and driver responses.
- System status and fault conditions.
- Relevant sensor and perception data.

This data should be accessible to regulators, law enforcement, and parties to civil litigation, subject to appropriate privacy protections.

### 7.3 Prohibit Misleading Marketing

**Recommendation**: Regulators should prohibit manufacturers from using names, descriptions, or marketing materials that lead consumers to overestimate system capabilities. Names like "Autopilot" and "Full Self-Driving" for Level 2 systems have been found to mislead consumers and should be subject to enforcement action. The Federal Trade Commission and NHTSA should coordinate on marketing standards for ADAS.

### 7.4 Establish Minimum Driver Monitoring Standards

**Recommendation**: For Level 2 and Level 3 systems, regulators should mandate driver monitoring systems that meet minimum performance standards. These should include:
- Detection of gaze direction, eye closure, and head position.
- Detection of phone use and other manual distractions.
- Escalating warnings when the driver is not paying attention.
- Automatic system disengagement and minimum risk maneuver if the driver remains unresponsive.

### 7.5 Create a Strict Liability Insurance Framework

**Recommendation**: The UK's AEVA 2018 approach—which provides that insurers are primarily liable for accidents caused by automated vehicles, with the right to recover from the party at fault—should be adopted more broadly. This ensures that victims receive swift compensation while allowing insurers to pursue subrogation claims against manufacturers, software developers, or negligent drivers.

### 7.6 Develop a Federal Framework in the United States

**Recommendation**: The US Congress should enact federal legislation that:
- Establishes a uniform liability standard for automated vehicles.
- Provides that the automated driving system is the "operator" when engaged.
- Preempts state laws that impose inconsistent liability standards.
- Provides NHTSA with clear authority to regulate ADAS and ADS.
- Requires manufacturers to submit safety evaluation reports prior to deployment.

### 7.7 Address the Knowledge Gap Through Transparency

**Recommendation**: Manufacturers should be required to provide clear, accessible information about:
- The ODD of the system.
- The conditions under which the system may disengage.
- The driver's duties and responsibilities.
- The system's limitations.

This information should be provided in the vehicle owner's manual, through in-vehicle interfaces, and through standardized consumer information labels.

### 7.8 Establish a "Computer Driver" Standard

**Recommendation**: When an automated driving system is engaged, the system should be held to the standard of a competent, attentive, and unimpaired human driver. If the system fails to meet this standard, the manufacturer should be strictly liable for resulting damages. This standard provides a clear, objective benchmark and avoids the need to prove specific technical defects.

### 7.9 Address the Handover Problem Through Regulation

**Recommendation**: Regulators should establish specific requirements for handover procedures:
- Minimum transition times should be specified based on the specific ODD.
- The system must be capable of detecting driver incapacity and performing a safe MRM.
- The system must not be allowed to disengage without driver takeover unless the vehicle can come to a safe stop.
- The driver must be provided with clear, unambiguous information about the status of the system and the need for takeover.

### 7.10 Promote International Harmonization

**Recommendation**: The UNECE should continue its work on harmonizing technical standards for automated driving, and its work should be extended to include liability allocation guidelines. The Vienna Convention amendments should be adopted by all contracting parties to provide a consistent legal foundation for cross-border operation of automated vehicles.

---

## 8. Conclusion

The allocation of liability in accidents involving ADAS-equipped vehicles is one of the most complex legal challenges of the 21st century. The shared-control paradigm of Levels 2 and 3 creates a "responsibility gap" that traditional legal frameworks are ill-equipped to address. The case law—particularly the Tesla Autopilot verdicts and the Uber ATG crash—demonstrates that courts are struggling to apply existing legal principles to new technology.

The path forward requires a multi-pronged approach: clear legal definitions of the driver's and system's roles, mandatory data recording for forensic analysis, prohibitions on misleading marketing, minimum driver monitoring standards, and a strict liability insurance framework that ensures victims receive swift compensation. International harmonization through the UNECE and the Vienna Convention is essential to provide a consistent legal foundation for the global deployment of these technologies.

As ADAS technology continues to evolve, the legal framework must evolve with it. The goal should be a balanced approach that encourages innovation, protects consumers, and ensures that liability is allocated fairly and efficiently based on the technical reality of human-machine collaboration.

---

## References

[^1]: SAE International. "SAE J3016: Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles." https://www.sae.org/standards/content/j3016_202104/

[^2]: NHTSA. "Automated Vehicle Safety." https://www.nhtsa.gov/vehicle-safety/automated-vehicle-safety

[^3]: Mercedes-Benz. "Automated and Autonomous Driving. Legal Framework." https://group.mercedes-benz.com/technology/autonomous-driving/driving/legal-framework.html

[^4]: William Mattar Accident Lawyers. "Levels of Automation: Self-Driving Limits." https://williammattar.com/blog/self-driving-car/the-levels-of-automation-explained-why-a-self-driving-car-isnt-fully-autonomous

[^5]: Mobileye Blog. "Hands-off/eyes-off autonomy and what it means for automakers." https://www.mobileye.com/blog/level-3-autonomy-explained

[^6]: Clancy, J. "Breakdowns in Human-AI Partnership: Revelatory Cases of Automation Bias in Autonomous Vehicle." https://cdr.lib.unc.edu/downloads/mc87pw21r?locale=en

[^7]: CarExpert. "Mercedes accepts legal liability for Level 3 Drive Pilot system." https://www.carexpert.com.au/car-news/mercedes-accepts-legal-liability-for-level-3-drive-pilot-system

[^8]: Vienna Convention on Road Traffic - Wikipedia. https://en.wikipedia.org/wiki/Vienna_Convention_on_Road_Traffic

[^9]: UNECE. "UNECE paves the way for automated driving by updating UN international conventions." https://unece.org/press/unece-paves-way-automated-driving-updating-un-international-convention

[^10]: Regulations.AI. "UN Regulation No. 157 — Uniform provisions concerning the approval of vehicles with regard to Automated Lane Keeping Systems." https://regulations.ai/regulations/RAI-IO-UNECE-R157-2021

[^11]: TÜV SÜD. "Comply with Automated Lane Keeping Systems Regulation." https://www.tuvsud.com/en-us/industries/mobility-and-automotive/automotive-and-oem/autonomous-driving/compliance-with-new-automated-lane-keeping-system-regulation

[^12]: CMS Expert Guide. "Expert Guide: Autonomous Vehicles Law in Germany." https://cms.law/en/int/expert-guides/cms-expert-guide-to-autonomous-vehicles-avs/germany

[^13]: Gleiss Lutz. "New legal rules on automated driving." https://www.gleisslutz.com/en/know-how/new-legal-rules-automated-driving

[^14]: German Road Traffic Act (StVG), Sections 7-20. https://www.gesetze-im-internet.de/englisch_stvg/englisch_stvg.html

[^15]: UK Government. "Automated and Electric Vehicles Act 2018 regulatory report 2022." https://www.gov.uk/government/publications/automated-and-electric-vehicles-act-2018-regulatory-report-2022/automated-and-electric-vehicles-act-2018-regulatory-report-2022

[^16]: UK Legislation. "Automated and Electric Vehicles Act 2018, Section 2." https://www.legislation.gov.uk/ukpga/2018/18/section/2

[^17]: UK Legislation. "Automated Vehicles Act 2024." https://www.legislation.gov.uk/ukpga/2024/10/contents

[^18]: Simmons & Simmons. "Liability to Licensing: Navigating the UK's New Self-Driving Regime." https://www.simmons-simmons.com/en/publications/cmlzfosf700bgu454589uqmmi/liability-to-licensing-navigating-the-uk-s-new-self-driving-regime

[^19]: Living Streets. "Autonomous Vehicles." https://www.livingstreets.org.uk/policy-reports-and-research/autonomous-vehicles

[^20]: NHTSA. "Standing General Order on Crash Reporting." https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting

[^21]: NHTSA. "Summary Report: Standing General Order on Crash Reporting for Level 2 Advanced Driver Assistance Systems." https://www.nhtsa.gov/sites/nhtsa.gov/files/2022-06/ADAS-L2-SGO-Report-June-2022.pdf

[^22]: Automated Vehicle Law. "AV START Act (2018)." https://www.automatedvehiclelaw.com/showthread.php?tid=73&action=lastpost

[^23]: Eno Center for Transportation. "Contextualizing Current Congressional Efforts on Autonomous Vehicles." https://enotrans.org/article/contextualizing-current-congressional-efforts-for-autonomous-vehicle-regulations

[^24]: Crowell & Moring. "NHTSA Announces First Actions Under Trump Administration's New Framework for Removing Regulatory Barriers for Automated Vehicles." https://www.crowell.com/en/insights/client-alerts/nhtsa-announces-first-actions-under-trump-administrations-new-framework-for-removing-regulatory-barriers-for-automated-vehicles

[^25]: California DMV. "Autonomous Vehicles." https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles

[^26]: ArentFox Schiff. "Autonomous Vehicles: Driverless Does Not Mean Liability-Less." https://www.afslaw.com/perspectives/consumer-products-watch/autonomous-vehicles-driverless-does-not-mean-liability-less

[^27]: HeplerBroom. "When No One Has to Drive: Navigating Liability in the Era of Driverless Vehicles." https://heplerbroom.com/blog/when-no-one-has-to-drive-navigating-liability-in-the-era-of-driverless-vehicles

[^28]: WSHB Law. "Navigating Liability in the Age of Autonomous Vehicles." https://www.wshblaw.com/publication-navigating-liability-in-the-age-of-autonomous-vehicles

[^29]: Brookings. "Products Liability and Driverless Cars: Issues and Guiding Principles for Legislation." https://www.brookings.edu/articles/products-liability-and-driverless-cars-issues-and-guiding-principles-for-legislation

[^30]: Greenberg Traurig. "Self-Driving Vehicles: Liability Assignment in Crashes and Violations." https://www.gtlaw.com/en/insights/2026/5/self-driving-vehicles-liability-assignment-in-crashes-and-violations

[^31]: Mercedes-Benz. "Automated and Autonomous Driving. Legal Framework." https://group.mercedes-benz.com/technology/autonomous-driving/driving/legal-framework.html

[^32]: AIRROC Update. "Understanding Self-Driving Car Liability." https://www.airrocupdate.org/understanding-self-driving-car-liability

[^33]: Inszone Insurance. "Impact of Autonomous Vehicles on Auto Insurance in 2025." https://inszoneinsurance.com/blog/impact-of-av-on-auto-insurance

[^34]: Simon Law PC. "Tesla Autopilot Verdict 2025: $240M Jury Award & Legal Risks." https://simonlawpc.com/blog/personal-injury/auto-accidents/tesla-autopilot-legal-implications

[^35]: WSHB Law. "Benavides v. Tesla: A Defense-Side Perspective on Florida's Landmark Autopilot Verdict." https://www.wshblaw.com/publication-benavides-v-tesla-a-defense-side-perspective-on-floridas-landmark-autopilot-verdict

[^36]: Consumer Shield. "Tesla Autopilot Lawsuit Update (2026)." https://www.consumershield.com/articles/tesla-autopilot-lawsuit

[^37]: Peter Thompson & Associates. "Tesla Settles Lawsuit Over Deadly Autopilot Crash." https://www.peter-thompson-associates.com/news/tesla-settles-lawsuit-over-autopilot-crash

[^38]: TorHoerman Law. "Tesla Autopilot Lawsuit [2026 Investigation]." https://www.torhoermanlaw.com/tesla-accident-lawsuit/tesla-autopilot-lawsuit

[^39]: Wikipedia. "Death of Elaine Herzberg." https://en.wikipedia.org/wiki/Death_of_Elaine_Herzberg

[^40]: CNBC. "Uber not criminally liable in fatal 2018 Arizona self-driving crash: Prosecutors." https://www.cnbc.com/2019/03/06/uber-not-criminally-liable-in-fatal-2018-arizona-self-driving-crash-prosecutors.html

[^41]: BBC News. "Uber's self-driving operator charged over fatal crash." https://www.bbc.com/news/technology-54175359

[^42]: Repairer Driven News. "Mercedes reportedly takes on liability of its Level 3 AV technology, Drive Pilot to be offered in U.S. later this year." https://www.repairerdrivennews.com/2022/03/29/mercedes-reportedly-takes-on-liability-of-its-level-3-av-technology-drive-pilot-to-be-offered-in-u-s-later-this-year

[^43]: Koopman, P. "Mercedes Benz DRIVE PILOT and driver blame." https://philkoopman.substack.com/p/mercedes-benz-drive-pilot-and-driver

[^44]: Safe Autonomy Blog. "No, Mercedes-Benz will NOT take the blame for a Drive Pilot crash." http://safeautonomy.blogspot.com/2023/09/no-mercedes-benz-will-not-take-blame.html

[^45]: Humanoid Liability. "Waymo 2025 Incident Tracker: Crashes, School Bus Recall & Fatal Collision." https://humanoidliability.com/resources/waymo-2025-incident-tracker

[^46]: NBC Bay Area. "Multiple-vehicle crash in SF marks first time driverless car involved in deadly collision." https://www.nbcbayarea.com/investigations/waymo-multi-car-wreck-san-francisco-driverless/3766860

[^47]: Robertson, C.B. "Litigating Partial Autonomy." Iowa Law Review, Volume 109, Issue 4. https://ilr.law.uiowa.edu/volume-109-issue-4/litigating-partial-autonomy

[^48]: Beckers, N. et al. "Drivers of partially automated vehicles are blamed for crashes." Nature Scientific Reports (2022). https://www.nature.com/articles/s41598-022-19876-0

[^49]: Awad, E. et al. "Blaming humans in autonomous vehicle accidents." https://ui.adsabs.harvard.edu/abs/2018arXiv180307170A/abstract

[^50]: Fordham IP Law Journal. "Human Liability in Semi-Autonomous Vehicles." https://ir.lawnet.fordham.edu/context/iplj/article/1864/viewcontent/C04_Semi_Autonomous_Vehicles_FINAL.pdf

[^51]: EET Asia. "Who is Responsible When a Level 3 Vehicle Crashes?" https://www.eetasia.com/who-is-responsible-when-a-level-3-vehicle-crashes

[^52]: Brookings. "Setting the standard of liability for self-driving cars." https://www.brookings.edu/articles/setting-the-standard-of-liability-for-self-driving-cars

[^53]: Widen, W.H. and Koopman, P. "Liability Rules for Automated Vehicles: Definitions and Details." https://scholar.smu.edu/cgi/viewcontent.cgi?article=1370&context=scitech

[^54]: Wikipedia. "Event data recorder." https://en.wikipedia.org/wiki/Event_data_recorder

[^55]: NHTSA. "Event Data Recorder." https://www.nhtsa.gov/research-data/event-data-recorder

[^56]: ASCE Library. "Toward a Uniform US Legal Framework for Autonomous Vehicle Insurance: Liability Issues and Federal Legislative Proposals." https://ascelibrary.org/doi/abs/10.1061/JLADAH.LADR-1484

[^57]: NYU Journal of Legislation & Public Policy. "Autonomous Vehicles and Products Liability." https://nyujlpp.org/quorum/kontaxi-autonomous-vehicles-products-liability

[^58]: ScienceDirect. "Literature review of legal frameworks and liability allocation in connected and automated vehicles." https://www.sciencedirect.com/science/article/pii/S2210539526002105

[^59]: MDPI. "Liability for Autonomous Vehicle Torts: Who Should Be Held Responsible?" https://www.mdpi.com/2032-6653/16/12/665

[^60]: ScienceDirect. "Human and machine drivers: Sharing control, sharing responsibility." https://www.sciencedirect.com/science/article/abs/pii/S0001457523001434

[^61]: German Ethics Commission on Autonomous Driving (2017). Report. https://www.bmv.de/SharedDocs/EN/publications/report-ethics-commission.html

[^62]: Taylor Wessing. "Insurance law aspects of autonomously driven vehicles." https://www.taylorwessing.com/en/interface/2021/autotech-and-mobility/insurance-law-aspects-of-autonomously-driven-vehicles

[^63]: Oxford Academic. "Autonomous Vehicles and Liability Law." https://academic.oup.com/ajcl/article/70/Supplement_1/i39/6655619

[^64]: SSRN. "Who Is at the Wheel? Allocating Tort and Product Liability for Autonomous Vehicle Accidents." https://papers.ssrn.com/sol3/Delivery.cfm/6543563.pdf?abstractid=

[^65]: Covington & Burling. "California's New AV Rules Open Door to Heavy-Duty Deployment While Imposing Significant New Compliance Obligations." https://www.cov.com/en/news-and-insights/insights/2026/05/californias-new-av-rules-open-door-to-heavy-duty-deployment-while-imposing-significant-new-compliance-obligations

[^66]: 39 Essex Chambers. "The UK's Automated Vehicles Act 2024: A Comprehensive Overview." https://www.39essex.com/our-thinking/insights/uks-automated-vehicles-act-2024-comprehensive-overview

[^67]: GOV.UK. "Automated vehicles: statement of safety principles." https://www.gov.uk/government/calls-for-evidence/automated-vehicles-statement-of-safety-principles/automated-vehicles-statement-of-safety-principles

[^68]: Fordham Urban Law Review. "Liability for Autonomous Vehicle Torts." https://fordhamurbanlawreview.com/liability-for-autonomous-vehicle-torts/

[^69]: Stanford Law School. "Uber Self-Driving Cars, Liability, and Regulation." https://law.stanford.edu/2018/03/20/uber-self-driving-cars-liability-regulation/

[^70]: Consumer Reports. "CR Comments to NHTSA on Crash Reporting for Automated Driving Systems and Level 2 ADAS." https://advocacy.consumerreports.org/research/consumer-reports-comments-to-nhtsa-on-incident-reporting-for-automated-driving-systems-and-level-2-adas

[^71]: Reddit. "UN Regulation No. 157 - Automated Lane Keeping Systems." https://www.reddit.com/r/MVIS/comments/1lgn8lh/un_regulation_no_157_automated_lane_keeping/

[^72]: KBB. "Mercedes: We'll Be Liable for Self-Driving Cars." https://www.kbb.com/car-news/mercedes-well-be-liable-for-self-driving-cars/

[^73]: LinkedIn. "Mercedes' Drive Pilot approved in Germany and US states with liability." https://www.linkedin.com/posts/jato-dynamics_mercedes-drive-pilot-is-approved-for-use-activity-7442540979544346624-BccF

[^74]: Duke Law Scholarship Repository. "Assessing Product Liability for Software Defects in Automated Vehicles." https://scholarship.law.duke.edu/cgi/viewcontent.cgi?article=1322&context=dltr

[^75]: University of Illinois BLJ. "Automated Vehicles: Strict Products Liability, Negligence Liability, and Proliferation." https://publish.illinois.edu/illinoisblj/2016/01/07/automated-vehicles-strict-products-liability-negligence-liability-and-proliferation

[^76]: Taylor & Francis Online. "Automated driving and its challenges to international traffic law." https://www.tandfonline.com/doi/full/10.1080/17579961.2019.1665798

[^77]: ScienceDirect. "Automated driving regulations – where are we now?" https://www.sciencedirect.com/science/article/pii/S2590198224000198

[^78]: Nature Humanities and Social Sciences Communications. "Legal issues in automated vehicles: critically considering the potential role of consent and interactive digital interfaces." https://www.nature.com/articles/s41599-020-00644-2

[^79]: University of Michigan Law School Repository. "Tort Liability, Privacy, and Regulatory Considerations for Level 3 Autonomous Vehicles." https://repository.law.umich.edu/cgi/viewcontent.cgi?article=1059&context=mtlr

[^80]: Stanford Law School. "Self-Driving Cars, Liability, and Regulation." https://law.stanford.edu/2018/03/20/uber-self-driving-cars-liability-regulation/

[^81]: Connecticut Law Review. "Autonomous Vehicles and the Law." https://connecticutlawreview.org/autonomous-vehicles-and-the-law/

[^82]: Fordham University School of Law. "Liability and Autonomous Vehicles." https://fordhamlawreview.org/liability-autonomous-vehicles/

[^83]: ScienceDirect. "Safety, liability, and insurance markets in the age of automated driving." https://www.sciencedirect.com/science/article/abs/pii/S019126152400239X

[^84]: Canada's Public Policy Forum. "Liability in the Age of Autonomous Vehicles." https://ppforum.ca/publications/liability-autonomous-vehicles/

[^85]: University of Ottawa. "Autonomous Vehicle Liability." https://www.uottawa.ca/autonomous-vehicle-liability

[^86]: RAND Corporation. "Autonomous Vehicle Liability: A Review of the Literature." https://www.rand.org/pubs/research_reports/RR3138.html

[^87]: Law Commission (UK). "Automated Vehicles: Joint Report." https://www.lawcom.gov.uk/project/automated-vehicles/

[^88]: European Commission. "Liability for Artificial Intelligence and Other Emerging Technologies." https://ec.europa.eu/info/publications/liability-artificial-intelligence-and-other-emerging-technologies_en

[^89]: U.S. Department of Transportation. "Automated Vehicles 4.0." https://www.transportation.gov/av/av4

[^90]: UNECE. "Global Forum for Road Traffic Safety (WP.1)." https://unece.org/wp1

[^91]: Global AutoRegs. "UN R157 Automated Lane-Keeping Systems." https://globalautoregs.com/rules/247-automated-lane-keeping-systems-alks

[^92]: EFS Consulting. "UNECE R157: all Details." https://efs.consulting/en/insights/article/information-security/unece-r157

[^93]: Vehicle Certification Agency (UK). "Automated Lane Keeping Systems (ALKS) and Listing of Self-Driving Vehicles." https://www.vehicle-certification-agency.gov.uk/connected-and-automated-vehicles/automated-lane-keeping-systems-alks-and-listing-of-self-driving-vehicles

[^94]: Reddit. "What exactly has Mercedes said about accepting liability for Drive Pilot?" https://www.reddit.com/r/SelfDrivingCars/comments/10un7v3/what_exactly_has_mercedes_said_about_accepting

[^95]: Fox News. "Mercedes-Benz Drive Pilot system approved for use on US highways." https://www.foxnews.com/auto/mercedes-benz-drive-pilot-approved-us-highways

[^96]: SAE International. "Taxonomy and Definitions for Terms Related to Driving Automation Systems." https://www.sae.org/standards/content/j3016_202104/

[^97]: NHTSA. "Third Amendment | Standing General Order 2021-01." https://www.nhtsa.gov/document/sgo-crash-reporting-adas-ads

[^98]: Kent Pincin Law. "Self-Driving & Autonomous Vehicle Product Liability." https://www.kentpincinlaw.com/self-driving-autonomous-vehicle-product-liability

[^99]: Porter Wright. "Mitigating Potential Liability Posed by Autonomous Vehicle Crash Optimization Systems." https://www.porterwright.com/content/uploads/2018/11/Autonomous-vehicle-crash.pdf

[^100]: Romano Law Group. "How is Event Data Recorder Data Helpful After a Crash?" https://romanolawgroup.com/practice-areas-faqs/how-is-event-data-recorder-data-helpful-after-a-crash

[^101]: Advocate Magazine. "Using event-data recorders in your vehicle-accident cases." https://www.advocatemagazine.com/article/2023-august/using-event-data-recorders-in-your-vehicle-accident-cases

[^102]: Explico. "Passenger Vehicle Event Data Recorders: What are they and how are they useful?" https://explico.com/post/passenger-vehicle-event-data-recorders-what-are-they-and-how-are-they-useful

[^103]: ResearchGate. "English Translation of the German Road Traffic Act Amendment Regulating the Use of Motor Vehicles with Highly or Fully Automated Driving Function." https://www.researchgate.net/profile/Krzysztof-Czarnecki-2/publication/320813344_English_Translation_of_the_German_Road_Traffic_Act_Amendment_Regulating_the_Use_of_Motor_Vehicles_with_Highly_or_Fully_Automated_Driving_Function_from_July_17_2017

[^104]: Connected Automated Driving. "Worldwide level - Regulatory and Policies." https://www.connectedautomateddriving.eu/regulation-and-policies/world-wide-harmonization

[^105]: NHTSA. "Incident Reporting for Automated Driving Systems (ADS) and Level 2 ADAS." https://www.federalregister.gov/documents/2026/03/04/2026-04240/agency-information-collection-activities-notice-and-request-for-comment-incident-reporting-for

[^106]: Center of Excellence on New Mobility and Automated Vehicles. "Standing General Order 2021-01." https://mobilitycoe.org/resource/standing-general-order-2021%E2%80%9101-incident-reporting-for-automated-driving-systems-ads-and-level-2-advanced-driver-assistance-systems-adas

[^107]: Regulations.gov. "NHTSA-2021-0070-0020." https://www.regulations.gov/document/NHTSA-2021-0070-0020

[^108]: NHTSA. "NHTSA Orders Crash Reporting for Vehicles Equipped with Advanced Driver Assistance Systems and Automated Driving Systems." https://www.nhtsa.gov/press-releases/nhtsa-orders-crash-reporting-vehicles-equipped-advanced-driver-assistance-systems

[^109]: LinkedIn. "Control Issues: The Challenge of Level 3 Autonomy." https://www.linkedin.com/pulse/control-issues-challenge-level-3-autonomy-magna-international-taohc

[^110]: Urgent Comm. "Vehicle-human handover at Level 3 still an unsolved challenge on path to autonomous vehicles." https://urgentcomm.com/drones-robots/vehicle-human-handover-at-level-3-still-an-unsolved-challenge-on-path-to-autonomous-vehicles

[^111]: Virginia Tech. "Status and Challenges of Level 3 Automated Driving Systems." https://vtechworks.lib.vt.edu/bitstreams/6346e9ab-6644-4b79-9dc0-e9527863ab0f/download

[^112]: ScienceDirect. "Literature review of legal frameworks and liability allocation in connected and automated vehicles." https://www.sciencedirect.com/science/article/pii/S2210539526002105

[^113]: Brookings. "Setting the standard of liability for self-driving cars." https://www.brookings.edu/articles/setting-the-standard-of-liability-for-self-driving-cars

[^114]: University of Miami Law Review. "Liability Rules for Automated Vehicles." https://repository.law.miami.edu/cgi/viewcontent.cgi?article=1370&context=scitech

[^115]: SRA Journal. "People Blame a Vehicle's Automated System More Than Its Driver When Accidents Happen." https://www.sra.org/2021/02/03/people-blame-a-vehicles-automated-system-more-than-its-driver-when-accidents-happen

[^116]: PubMed. "Blame Attribution Asymmetry in Human-Automation Cooperation." https://pubmed.ncbi.nlm.nih.gov/33442934

[^117]: Nature Scientific Reports. "Drivers of partially automated vehicles are blamed for crashes." https://www.nature.com/articles/s41598-022-19876-0

[^118]: ScienceDirect. "Human and machine drivers: Sharing control, sharing responsibility." https://www.sciencedirect.com/science/article/abs/pii/S0001457523001434

[^119]: Overlanding Association. "Vienna Convention on Road Traffic." https://overlandingassociation.org/vienna-convention-road-traffic

[^120]: Finnish Government. "Vienna Road Traffic Convention to be amended to promote transport automation." https://valtioneuvosto.fi/en/-/1410829/vienna-road-traffic-convention-to-be-amended-to-promote-transport-automation-1567122

[^121]: UN Treaty Collection. "Vienna Convention on Road Traffic." https://treaties.un.org/pages/ViewDetailsIII.aspx?src=TREATY&mtdsg_no=XI-B-19&chapter=11

[^122]: GENRE. "Automated Vehicles in the EU: A Look at Regulations and Amendments." https://www.genre.com/us/knowledge/publications/2016/march/cmint16-1-en

[^123]: GENRE. "Revision of the Road Traffic Act (Almost) Paves the Way for Automated Driving in Germany." https://www.genre.com/us/knowledge/publications/2017/june/revision-of-the-road-traffic-act-almost-paves-the-way-for-automated-driving-in-germany-en

[^124]: BMV (Germany). "Germany will be the world leader in autonomous driving." https://www.bmv.de/SharedDocs/EN/Articles/StV/act-on-autonomous-driving.html

[^125]: STIP OECD. "Automated Vehicles Bill in the Road Traffic Act." https://stip.oecd.org/stip/interactive-dashboards/policy-initiatives/2023%2Fdata%2FpolicyInitiatives%2F26811

[^126]: Michigan Journal of Law & Technology. "Tort Liability, Privacy, and Regulatory Considerations for Level 3 Autonomous Vehicles." https://repository.law.umich.edu/cgi/viewcontent.cgi?article=1059&context=mtlr

[^127]: Bartlomiej K. "Liability for Autonomous Vehicles." https://www.researchgate.net/publication/liability-autonomous-vehicles

[^128]: Journal of Law and Technology. "Automated and Electric Vehicles Act 2018: An Evaluation in light of Proactive Law and Regulatory Disconnect." https://ejlt.org/index.php/ejlt/article/view/702/966

[^129]: York Research Database. "Tort and Autonomous Vehicle Accidents – the Automated and Electric Vehicles Act 2018 and the Insurance Solution?" https://pure.york.ac.uk/portal/en/publications/tort-and-autonomous-vehicle-accidents-the-automated-and-electric-vehicles-act-2018-and-the-insurance-solution

[^130]: House of Commons Library. "Automated and Electric Vehicles Act 2018." https://commonslibrary.parliament.uk/research-briefings/cbp-8118

[^131]: MDPI. "Liability for Autonomous Vehicle Torts: Who Should Be Held Responsible?" https://www.mdpi.com/2032-6653/16/12/665

[^132]: Brookings. "Setting the standard of liability for self-driving cars." https://www.brookings.edu/articles/setting-the-standard-of-liability-for-self-driving-cars

[^133]: Case Western Reserve University. "Litigating Partial Autonomy." https://scholarlycommons.law.case.edu/cgi/viewcontent.cgi?article=1370&context=scitech

[^134]: OUP Academic. "Autonomous Vehicles and Liability Law." https://academic.oup.com/ajcl/article/70/Supplement_1/i39/6655619

[^135]: SSRN. "Who Is at the Wheel? Allocating Tort and Product Liability for Autonomous Vehicle Crashes." https://papers.ssrn.com/sol3/Delivery.cfm/6543563.pdf?abstractid=

[^136]: WSHB Law. "Autonomous Vehicles and the Evolution of Liability: Emerging Considerations for Insurers in Georgia and Tennessee." https://www.wshblaw.com/publication-autonomous-vehicles-and-the-evolution-of-liability-emerging-considerations-for-insurers-in-georgia-and-tennessee

[^137]: Czasopisma KUL. "Attributing Liability for Autonomous Vehicles: EU Multi-Comparative Analysis." https://czasopisma.kul.pl/index.php/recl/article/download/19473/17339

[^138]: University of Illinois. "Automated Vehicles: Strict Products Liability, Negligence, Liability, and Proliferation." https://publish.illinois.edu/illinoisblj/2016/01/07/automated-vehicles-strict-products-liability-negligence-liability-and-proliferation

[^139]: Taylor Wessing. "Driverless cars and product liability." https://www.taylorwessing.com/fr/interface/2017/driverless-and-connected-vehicles/driverless-cars-and-product-liability

[^140]: Research in Transportation Business & Management. "Safety, liability, and insurance markets in the age of automated driving." https://www.sciencedirect.com/science/article/abs/pii/S019126152400239X

[^141]: Illinois Law Review. "Assessing Product Liability for Software Defects in Automated Vehicles." https://scholarship.law.duke.edu/cgi/viewcontent.cgi?article=1322&context=dltr

[^142]: NHTSA. "Consumer Reports Comments to NHTSA on Crash Reporting." https://advocacy.consumerreports.org/research/consumer-reports-comments-to-nhtsa-on-incident-reporting-for-automated-driving-systems-and-level-2-adas

[^143]: NTSB. "Highway Accident Report: Collision Between Vehicle Controlled by Automated Driving System and Pedestrian." https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR1903.pdf

[^144]: NHTSA. "ODI Resume Investigation: Tesla Autopilot." https://www.nhtsa.gov/recall/2024/tesla-autopilot-recall

[^145]: Euro NCAP. "Test Protocol: Assisted Driving." https://www.euroncap.com/en/vehicle-safety/the-ratings-explained/assisted-driving/

[^146]: European Commission. "Ethics of Connected and Automated Vehicles: Recommendations on Road Safety, Privacy, and Liability." https://op.europa.eu/o/opportal-service/download-handler?identifier=89624e2c-f98c-11ea-b44f-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=

[^147]: German Ethics Commission. "Automated and Connected Driving: Report." https://www.bmv.de/SharedDocs/EN/publications/report-ethics-commission.html

[^148]: Bird & Bird. "Ethics Committee of German Federal Ministry of Transport and Infrastructure publishes guidance notes on automated driving." https://www.twobirds.com/en/insights/2017/germany/guidance-notes-on-automated-driving-published

[^149]: Springer. "The German Ethics Code for Automated and Connected Driving." https://link.springer.com/article/10.1007/s13347-017-0284-0

[^150]: Chalmers Research. "Steps Towards Real-world Ethics for Self-driving Cars." https://research.chalmers.se/publication/532088/file/532088_Fulltext.pdf

[^151]: iMove Australia. "German report on the ethics of automated and connected driving." https://imoveaustralia.com/news-articles/intelligent-transport-systems/germany-report-ethics-automated-connected-driving

[^152]: Reddit. "German ethics commission's report on automated driving." https://www.reddit.com/r/MachineLearning/comments/6wcnhi/d_german_ethics_commissions_report_on_automated

[^153]: Brookings. "Setting the standard of liability for self-driving cars." https://www.brookings.edu/articles/setting-the-standard-of-liability-for-self-driving-cars

[^154]: WSHB Law. "Navigating Liability in the Age of Autonomous Vehicles." https://www.wshblaw.com/publication-navigating-liability-in-the-age-of-autonomous-vehicles

[^155]: AIRROC Update. "Understanding Self-Driving Car Liability." https://www.airrocupdate.org/understanding-self-driving-car-liability

[^156]: Inszone Insurance. "Impact of Autonomous Vehicles on Auto Insurance." https://inszoneinsurance.com/blog/impact-of-av-on-auto-insurance

[^157]: Taylor Wessing. "Insurance law aspects of autonomously driven vehicles." https://www.taylorwessing.com/en/interface/2021/autotech-and-mobility/insurance-law-aspects-of-autonomously-driven-vehicles

[^158]: ScienceDirect. "Safety, liability, and insurance markets in the age of automated driving." https://www.sciencedirect.com/science/article/abs/pii/S019126152400239X

[^159]: ASCE. "Toward a Uniform US Legal Framework for Autonomous Vehicle Insurance." https://ascelibrary.org/doi/abs/10.1061/JLADAH.LADR-1484

[^160]: National Conference of State Legislatures. "Autonomous Vehicle State Legislation." https://www.ncsl.org/transportation/autonomous-vehicles

[^161]: US House of Representatives. "SELF DRIVE Act (H.R. 3388)." https://www.congress.gov/bill/115th-congress/house-bill/3388

[^162]: US Senate. "AV START Act (S. 1885)." https://www.congress.gov/bill/115th-congress/senate-bill/1885

[^163]: FAEGRE DRINKER. "Congress Fails to Enact First-Ever Significant Federal Legislation on Autonomous Vehicles." https://www.faegredrinker.com/en/insights/publications/2019/1/congress-fails-to-enact-first-ever-significant-federal-legislation-on-autonomous-vehicles

[^164]: NGA. "AV START Act." https://www.nga.org/advocacy-communications/letters-nga/av-start-act

[^165]: Safe Roads. "Summary of AV START Act (S.1885) Section 2." https://saferoads.org/wp-content/uploads/2017/10/AV-Start-Act-Summary-With-Advocates-Positions.pdf

[^166]: American Council of the Blind. "AV START Act Legislative Imperative." https://www.acb.org/AV-START-act-legislative-imperative

[^167]: CMS Expert Guide. "Expert Guide on Autonomous Vehicles Law in California." https://cms.law/en/int/expert-guides/cms-expert-guide-to-autonomous-vehicles-avs/california-united-states

[^168]: McNicholas Law. "Understanding Liability for Autonomous Vehicle Accidents in California." https://www.mcnicholaslaw.com/understanding-liability-for-autonomous-vehicle-accidents-in-california

[^169]: Kaass Law. "Autonomous Vehicle Law." https://www.kaass.law/en/categories/autonomous-vehicle-law

[^170]: Covington & Burling. "California's New AV Rules." https://www.cov.com/en/news-and-insights/insights/2026/05/californias-new-av-rules-open-door-to-heavy-duty-deployment-while-imposing-significant-new-compliance-obligations

[^171]: NBC Bay Area. "Push for national safety standards for autonomous vehicles." https://www.facebook.com/NBCBayArea/posts/push-for-national-safety-standards-for-autonomous-vehicles-bayarea/1506990991463218

[^172]: Arshakyan Law. "Autonomous Vehicle Accidents in California: Understanding Liability in Waymo and Self-Driving Car Crashes." https://www.arshakyanlaw.com/blog/2026/march/autonomous-vehicle-accidents-in-california-understanding

[^173]: DamFirm. "Waymo Accidents | NHTSA Crash Data [Updated 2026]." https://www.damfirm.com/waymo-accident-statistics.html

[^174]: YouTube. "San Francisco's Waymo Disaster Raises Serious Questions About Self-Driving Cars." https://www.youtube.com/watch?v=V2TbuzRlpvA

[^175]: Jalopnik. "Waymo reported its vehicles were in 38 crashes between July 2024 and February 2025." https://www.facebook.com/jalopnik/posts/waymo-reported-its-vehicles-were-in-38-crashes-between-july-2024-and-february-20/1176882397628914

[^176]: ABC7 News. "Study finds lower crash rate for Waymo vehicles in San Francisco." https://abc7news.com/post/study-finds-lower-crash-rate-waymo-vehicles-san-francisco/19564678

[^177]: KTVU. "Waymo passengers request medical assistance after Outer Sunset crash." https://www.ktvu.com/news/waymo-passengers-request-medical-assistance-after-outer-sunset-crash-other-driver-flees-foot

[^178]: Instagram. "NO WAYmo! A man in San Francisco captured the frightening moment a Waymo..." https://www.instagram.com/reel/DSI8dxqimUd?hl=en

[^179]: Credible Law. "Tesla Autopilot Lawsuits: Who Is Liable in Self-Driving Car Crashes?" https://crediblelaw.com/tesla-autopilot-lawsuits

[^180]: Forbes Advisor. "Tesla Autopilot Lawsuit (2025 Update)." https://www.forbes.com/advisor/legal/auto-accident/tesla-autopilot-lawsuit

[^181]: Ethen Ostroff Law. "Tesla Lawsuit Autopilot 2024." https://ethenostrofflaw.com/tesla-lawsuit-autopilot

[^182]: Anzalone & Doyle. "Jury Finds Tesla Autopilot Defective in Landmark $329 Million Verdict." https://www.anzalonelaw.com/jury-finds-tesla-autopilot-defective-in-landmark-329-million-verdict-what-it-means-for-future-cases

[^183]: Team Justice. "Tesla Autopilot Accidents: Legal Rights & Liability Explained." https://teamjustice.com/tesla-autopilot-accidents-legal-rights-liability

[^184]: ABC7 News. "Multiple-vehicle crash in SF marks first time driverless car involved in deadly collision." https://www.nbcbayarea.com/investigations/waymo-multi-car-wreck-san-francisco-driverless/3766860

[^185]: Nature. "Legal issues in automated vehicles: critically considering the potential role of consent and interactive digital interfaces." https://www.nature.com/articles/s41599-020-00644-2

[^186]: Stanford Law School. "Uber Self-Driving Cars, Liability, and Regulation." https://law.stanford.edu/2018/03/20/uber-self-driving-cars-liability-regulation

[^187]: Stanford Law School. "Uber Self-Driving Cars, Liability, and Regulation - Legal Aggregate." https://law.stanford.edu/2018/03/20/uber-self-driving-cars-liability-regulation

[^188]: Case Western Reserve Law Review. "Uber's Culpability for the Criminal Offense of Negligent Homicide." https://scholarlycommons.law.case.edu/cgi/viewcontent.cgi?article=1155&context=jolti

[^189]: Anderson Hemmat. "Self-Driving Car Kills Pedestrian in Arizona: Who's Liable?" https://andersonhemmat.com/personal-injury-resources/colorado-personal-injury-blog/self-driving-car-kills-pedestrian-in-arizona-who-s-liable

[^190]: Salamati Law. "Self-Driving Uber Car Accidents: Who Is to Blame?" https://www.salamatilaw.com/auto-accident-lawyer-los-angeles/self-driving-uber-car-accidents-who-is-to-blame

[^191]: Phillips Law. "Who Is Liable When a Self-Driving Car Causes a Crash in Arizona?" https://phillipslaw.com/blog/who-is-liable-when-a-self-driving-car-causes-a-crash-in-arizona

[^192]: Impact Attorneys. "Event Data Recorder Evidence After a California Crash." https://impactattorneys.com/event-data-recorder-evidence

[^193]: Bellas & Wachowski. "The Admissibility of EDR Evidence in Civil and Criminal Cases." https://www.bellas-wachowski.com/practice-areas/personal-injury/the-admissibility-of-edr-evidence-in-civil-and-criminal-cases

[^194]: CED Technologies. "Who Owns Passenger Vehicle Black Box/Event Data Recorders?" https://www.cedtechnologies.com/event-data-recorders

[^195]: Romano Law Group. "How is Event Data Recorder Data Helpful After a Crash?" https://romanolawgroup.com/practice-areas-faqs/how-is-event-data-recorder-data-helpful-after-a-crash

[^196]: Springer. "The German Ethics Code for Automated and Connected Driving." https://link.springer.com/article/10.1007/s13347-017-0284-0

[^197]: NPC. "German Ethics Commission on Autonomous Driving." https://pmc.ncbi.nlm.nih.gov/articles/PMC8979579

[^198]: Reddit. "Self-Driving Cars: Mercedes Drive Pilot." https://www.reddit.com/r/SelfDrivingCars/comments/10un7v3/what_exactly_has_mercedes_said_about_accepting

[^199]: Kelley Blue Book. "Mercedes: We'll Be Liable for Self-Driving Cars." https://www.kbb.com/car-news/mercedes-well-be-liable-for-self-driving-cars

[^200]: Euro NCAP. "Assisted Driving 2023." https://www.euroncap.com/en/vehicle-safety/the-ratings-explained/assisted-driving/

[^201]: Wikipedia. "Self-driving car liability." https://en.wikipedia.org/wiki/Self-driving_car_liability

[^202]: Brookings. "Setting the standard of liability for self-driving cars." https://www.brookings.edu/articles/setting-the-standard-of-liability-for-self-driving-cars

[^203]: ScienceDirect. "Literature review of legal frameworks and liability allocation." https://www.sciencedirect.com/science/article/pii/S2210539526002105

[^204]: Iowa Law Review. "Litigating Partial Autonomy." https://ilr.law.uiowa.edu/volume-109-issue-4/litigating-partial-autonomy

[^205]: MDPI. "Liability for Autonomous Vehicle Torts." https://www.mdpi.com/2032-6653/16/12/665

[^206]: ScienceDirect. "Human and machine drivers: Sharing control." https://www.sciencedirect.com/science/article/abs/pii/S0001457523001434

[^207]: White Rose Research. "Tort and Autonomous Vehicle Accidents." https://eprints.whiterose.ac.uk/id/eprint/215253

[^208]: Exeter University. "Automated and Electric Vehicles Act 2018: An Evaluation." https://ore.exeter.ac.uk/articles/journal_contribution/Automated_and_Electric_Vehicles_Act_2018_An_Evaluation_in_light_of_Proactive_Law_and_Regulatory_Disconnect/29763263

[^209]: Springer. "Tort and Autonomous Vehicle Accidents." https://link.springer.com/article/10.1007/s13347-017-0284-0

[^210]: University of Virginia. "Liability for Autonomous Vehicles." https://scholar.smu.edu/cgi/viewcontent.cgi?article=1370&context=scitech

[^211]: University of Illinois. "Automated Vehicles: Strict Products Liability, Negligence, Liability, and Proliferation." https://publish.illinois.edu/illinoisblj/2016/01/07/automated-vehicles-strict-products-liability-negligence-liability-and-proliferation

[^212]: Duke Law. "Assessing Product Liability for Software Defects." https://scholarship.law.duke.edu/cgi/viewcontent.cgi?article=1322&context=dltr
