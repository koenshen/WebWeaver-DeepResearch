
# Third-Party Risk in Finance, Healthcare, and Technology: Lessons from the 2025–2026 Breach Wave

**Prepared for:** Risk Management Review  
**Period analyzed:** 2025–2026 (with selected 2024 context where chains continued into 2025)  
**Sectors covered:** Finance, Healthcare, Technology  
**Regions covered:** Americas, Europe, Asia-Pacific, Australia

---

## Executive Summary

The 2025–2026 period represents a watershed moment for third-party risk management. Data from the Verizon 2025 Data Breach Investigations Report (DBIR) shows that **30% of all breaches now involve a third party** — double the 15% recorded in the prior year and the largest single-year shift in the DBIR's history. SecurityScorecard's 2025 Global Third-Party Breach Report found that in some regions, the third-party breach rate exceeds 70% (Singapore, 71.4%; Netherlands, 70.4%; Japan, 60%). The Black Kite Third-Party Breach Report 2026 (based on 2025 data) documented that each breached vendor now compromises an average of **5.28 downstream companies** — the highest "blast radius" ever recorded — with 719 named victim companies and an estimated 26,000 "shadow victims" affecting 433 million people.

This report analyzes the root causes, business impacts, and emerging best practices from the most significant third-party breaches across three critical sectors.

---

## Section 1: Common Root Causes

### 1.1 Supply Chain Exploitation via Concentrated Vendor Dependencies

The most significant structural root cause of 2025's breach wave is **risk concentration** — the phenomenon whereby a single vendor failure cascades across hundreds of downstream organizations. The Black Kite report identified an "Elite 50" group of highly interconnected shared vendors with the following alarming characteristics:

- **70%** have at least one unpatched vulnerability listed in the CISA Known Exploited Vulnerabilities (KEV) catalog.
- **62%** have corporate credentials currently circulating in stealer logs on the dark web.
- **52%** have already suffered at least one verified data breach.
- **18%** were breached again in the last 12 months alone.
- Their average Ransomware Susceptibility Index (RSI) sits at **0.465** — well above the 0.4 high-risk threshold where attack probability jumps 11.6×.

**Illustrative cases:**

| Incident | Sector | Vendor | Downstream Impact |
|----------|--------|--------|-------------------|
| SitusAMC (Nov 2025) | Finance | Real-estate loan/mortgage servicing vendor | JPMorgan Chase, major banks; accounting records and legal agreements stolen |
| Salesforce OAuth Campaign (Aug 2025) | Cross-sector | Salesforce CRM (via malicious OAuth apps) | 700+ organizations including Allianz Life, Google, Cisco, Adidas, Qantas, Air France-KLM, multiple luxury brands |
| Conduent Business Services (2025) | Healthcare | Back-office services business associate | 62+ million Americans' PHI exposed — third-largest healthcare breach in history |
| Marks & Spencer / TCS Contractor (Apr 2025) | Retail/Tech | TCS (Tata Consultancy Services) contractor | 6.5M+ customer records; M&S took online operations offline; Co-op checkout disruptions |

**Sources:** [Black Kite 2026 Third-Party Breach Report](https://blackkite.com/reports/third-party-breach-report-2026); [FortifyData Third-Party Breaches 2025](https://fortifydata.com/blog/top-third-party-data-breaches-in-2025); [Cybersecurity Dive — SitusAMC](https://www.cybersecuritydive.com/news/bank-vendor-cyberattack-supply-chain/806293); [UpGuard Biggest Data Breaches Financial Services](https://www.upguard.com/blog/biggest-data-breaches-financial-services)

### 1.2 Misconfigured Cloud Services and API Vulnerabilities

The proliferation of cloud-based SaaS and API integrations created a massive attack surface that attackers exploited ruthlessly in 2025.

**Key examples:**

- **Allianz Life Insurance (July 2025):** Attackers compromised a third-party cloud-based CRM system via social engineering. The breach affected approximately 1.5 million customers. No direct attack on Allianz's own systems occurred — the entire incident was a cloud vendor supply chain attack. (Source: [UpGuard Financial Services Breaches](https://www.upguard.com/blog/biggest-data-breaches-financial-services))

- **TransUnion (August 2025):** Unauthorized access to a third-party Salesforce application supporting U.S. consumer support operations exposed 4.4 million records including names, dates of birth, and Social Security numbers. The attack was attributed to the combined Scattered Spider and ShinyHunters groups using voice phishing and malicious OAuth-connected apps. (Source: [UpGuard Financial Services Breaches](https://www.upguard.com/blog/biggest-data-breaches-financial-services))

- **Ascension Health (Mid-2025):** A third-party business partner's MOVEit Transfer software vulnerability allowed attackers to access 437,329 patient records including names, SSNs, medical diagnoses, and clinical details. This was a downstream effect of the MOVEit mass-exploitation patterns that continued from 2023–2024. (Source: [FortifyData Third-Party Breaches 2025](https://fortifydata.com/blog/top-third-party-data-breaches-in-2025))

- **HealthEC LLC:** A single healthcare IT vendor compromise cascaded to expose 45 million patient records across dozens of downstream hospital systems and health networks. (Source: [Black Kite 2025 Third-Party Breach Report](https://blackkite.com/reports/black-kite-third-party-breach-report-2025))

### 1.3 Credential Misuse and Social Engineering

The IBM Cost of a Data Breach 2025 report identifies stolen credentials as the most expensive initial vector, and the Verizon 2025 DBIR confirms that credential misuse was a primary driver of the third-party breach surge.

**Key examples:**

- **Change Healthcare (Feb 2024, fallout continuing into 2025–2026):** The root cause was compromised Citrix credentials with no multi-factor authentication (MFA) enabled. The breach affected 192.7 million individuals — the largest healthcare data breach in history — and disrupted claims processing for hundreds of thousands of healthcare providers. The nine-day detection delay between initial access and ransomware deployment was a critical failure. (Source: [Cynomi TPRM Statistics 2026](https://cynomi.com/blog/third-party-risk-management-statistics-every-msp-should-know-in-2026); [Hyperproof Change Healthcare Analysis](https://hyperproof.io/resource/understanding-the-change-healthcare-breach))

- **Salesforce OAuth Campaign (2025):** Attackers tricked employees at multiple organizations into approving malicious OAuth apps disguised as Salesforce tools. This allowed credential harvesting, exfiltration of AWS access keys, passwords, and Snowflake tokens across 700+ organizations. (Source: [FortifyData Third-Party Breaches 2025](https://fortifydata.com/blog/top-third-party-data-breaches-in-2025))

- **Workday Breach (August 2025):** Fraudsters gained access to Workday's third-party CRM platform through targeted social engineering. Attackers impersonated HR and IT staff via phone and text messages to trick employees into providing login credentials, exposing business contact information of customers. (Source: [SecureFrame Supply Chain Attacks 2026](https://secureframe.com/blog/supply-chain-attacks))

### 1.4 Unpatched Edge Security Appliances

A recurring pattern across 2025–2026 is the exploitation of vulnerabilities in edge security appliances — firewalls, file transfer solutions, and VPNs — at vendor sites.

**Key examples:**

- **Marquis Software Solutions (2026):** A marketing and analytics vendor serving 74+ U.S. financial institutions was compromised through exploitation of a SonicWall device vulnerability. Up to 1.35 million customers' personal and account information was exposed. (Source: [UpGuard Financial Services Breaches](https://www.upguard.com/blog/biggest-data-breaches-financial-services))

- **Multiple Incidents via File Transfer Exploits:** The pattern seen with MOVEit (2023), GoAnywhere (2023), Cleo (2024), and continuing into 2025 demonstrates that file transfer solutions remain a persistent vulnerability in the supply chain. The Black Kite report notes that 53.77% of organizations globally have at least one critical unpatched vulnerability. (Source: [Black Kite 2026 Third-Party Breach Report](https://blackkite.com/reports/third-party-breach-report-2026))

### 1.5 Software Supply Chain Attacks (Open Source and CI/CD)

The technology sector faced a new wave of attacks on the software supply chain itself.

**Key examples:**

- **GitHub Account Compromise (March 2025):** Attackers exploited missing authentication and weak role-based access control, stealing OAuth tokens that led to unauthorized access to private repositories, injection of malicious code, and harvesting of encryption keys. 1.5 billion records were exposed. (Source: [TechDemocracy Top 5 Software Supply Chain Attacks 2025](https://www.techdemocracy.com/resources/top-5-software-supply-chain-attacks-in-2025-266))

- **Shai-Hulud npm Worm (September 2025):** A self-replicating worm compromised 500+ npm packages, targeting GitHub Personal Access Tokens and API keys for AWS, GCP, and Azure. CISA issued an emergency alert. (Source: [CISA Alert on npm Compromise](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem))

- **Red Hat Consulting GitLab Breach (April 2025):** Attackers gained unauthorized access to a self-managed GitLab instance, stealing 570 GB of internal data from 28,000+ repositories including client configurations, automation scripts, and API keys. (Source: [Ethixbase360 Top 10 Third-Party Breaches 2025](https://ethixbase360.com/top-10-third-party-cyber-breaches-of-2025-what-they-mean-for-your-tprm-strategy))

---

## Section 2: Business Impacts Observed Across Multiple Clients

### 2.1 Financial Impacts

The financial toll of third-party breaches in 2025–2026 has been severe and multi-dimensional:

| Metric | Value | Source |
|--------|-------|--------|
| Average cost of third-party breach | **$4.91 million** | IBM Cost of Data Breach 2025 |
| Average cost of supply chain compromise | **$4.91 million** (267-day lifecycle, longest of any vector) | IBM 2025 |
| Healthcare breach average | **$7.42 million** | IBM 2025 |
| Financial services breach average | **$5.56 million** | IBM 2025 |
| Remediation cost when breach originates from third-party | **~$4.8 million** | Reports 2025 |
| US average breach cost | **$10.22 million** | IBM 2025 |
| Cencora ransomware payment | **$75 million** (largest on record) | Black Kite 2025 Report |

**Sources:** [Cynomi TPRM Statistics 2026](https://cynomi.com/blog/third-party-risk-management-statistics-every-msp-should-know-in-2026); [Black Kite 2025 Third-Party Breach Report](https://blackkite.com/reports/black-kite-third-party-breach-report-2025); [Compunnel Supply Chain Breaches 2025](https://www.compunnel.com/blogs/supply-chain-breaches-2025-the-weakest-links-that-cost-millions)

### 2.2 Operational Disruption and Patient Care Impact (Healthcare)

Healthcare suffered the most severe operational consequences:

- **Change Healthcare disruption:** Claims processing for hundreds of thousands of healthcare providers was disrupted for weeks. The American Medical Association reported that nearly two-thirds of physicians used personal funds to cover operational costs during the outage. (Source: [Cynomi TPRM Statistics 2026](https://cynomi.com/blog/third-party-risk-management-statistics-every-msp-should-know-in-2026))

- **NHS Advanced Computer Group:** The ICO fined Advanced Computer Software Group £3.08 million in March 2025 for ransomware failings that impacted critical health supply chains. The ICO framed the case as a warning about MFA gaps in health infrastructure. (Source: [UpGuard Biggest Data Breaches UK](https://www.upguard.com/blog/biggest-data-breaches-uk))

- **UK Healthcare Technology Provider DXS (December 2025):** Hackers breached internal servers of a tech provider for Britain's National Health Service, highlighting that current UK regulations do not automatically include third-party health IT suppliers within security standards. (Source: [The Record — DXS Hack](https://therecord.media/uk-nhs-tech-provider-dxs-discloses-hack))

- **Ascension Health:** 437,329 patients' medical identity theft risk increased due to exposure of SSNs, medical diagnoses, and clinical details. (Source: [FortifyData Third-Party Breaches 2025](https://fortifydata.com/blog/top-third-party-data-breaches-in-2025))

### 2.3 Regulatory and Legal Fallout

Regulatory scrutiny intensified dramatically across all regions:

- **SEC Disclosure Pressure:** Once materiality is determined, the four-business-day clock starts for SEC reporting. Weak supplier communications become immediate reputational liabilities. (Source: [Compunnel Supply Chain Breaches 2025](https://www.compunnel.com/blogs/supply-chain-breaches-2025-the-weakest-links-that-cost-millions))

- **GDPR Enforcement:** Fines since 2018 totaled ~€5.9 billion as of early 2025, with processor/controller disputes after vendor breaches remaining an active enforcement lane. (Source: [Compunnel Supply Chain Breaches 2025](https://www.compunnel.com/blogs/supply-chain-breaches-2025-the-weakest-links-that-cost-millions))

- **DORA (EU Digital Operational Resilience Act):** Effective January 2025, DORA now requires financial entities to maintain a register of all ICT third-party providers, conduct risk assessments before outsourcing critical functions, and include specific contractual clauses covering incident reporting, audit rights, and exit strategies. Compliance has been "mixed" according to Cisco's Chief Privacy Officer. (Source: [CNBC — DORA Compliance](https://www.cnbc.com/2025/01/17/dora-many-banks-arent-ready-for-tough-new-eu-cybersecurity-law.html); [Cynomi TPRM Statistics 2026](https://cynomi.com/blog/third-party-risk-management-statistics-every-msp-should-know-in-2026))

- **Australian Clinical Labs (ACL):** The Federal Court ordered ACL to pay A$5.8 million in civil penalties — A$4.2 million for failing to protect personal information, A$800,000 for failing to assess whether an eligible data breach had occurred, and A$800,000 for failing to notify the Commissioner. The decision established that delay and inadequate assessment are independently punishable. (Source: [UpGuard Biggest Data Breaches Australia](https://www.upguard.com/blog/biggest-data-breaches-australia))

### 2.4 Class-Action Litigation

Multiple class-action lawsuits were filed in 2025:

- **TransUnion:** Class actions filed within days of the breach announcement. (Source: [UpGuard Financial Services Breaches](https://www.upguard.com/blog/biggest-data-breaches-financial-services))
- **Allianz Life:** Multiple class actions filed in the District of Minnesota. (Source: [UpGuard Financial Services Breaches](https://www.upguard.com/blog/biggest-data-breaches-financial-services))
- **LoanDepot:** Consolidated class action settled for approximately $25 million. (Source: [UpGuard Financial Services Breaches](https://www.upguard.com/blog/biggest-data-breaches-financial-services))
- **Qantas:** Facing class-action claims following the offshore contact-center platform breach that exposed 5.7–6 million customer records. (Source: [FortifyData Third-Party Breaches 2025](https://fortifydata.com/blog/top-third-party-data-breaches-in-2025))

### 2.5 Reputational and Trust Erosion

The Black Kite report's finding of an average 117-day disclosure delay (up from 76 days in 2024) means that organizations are operating in a "silent window" of undisclosed risk for nearly four months. This erodes trust when breaches eventually come to light. The 26,000 "shadow victims" — organizations impacted but never officially named — represents a massive trust deficit in the reporting ecosystem. (Source: [Black Kite 2026 Third-Party Breach Report](https://blackkite.com/reports/third-party-breach-report-2026))

---

## Section 3: Regional Analysis — Global Examples

### 3.1 Americas

**United States — Finance Sector**

The **Salesforce OAuth campaign** (August 2025) was the single most impactful supply chain attack of the year, targeting 700+ organizations. The attack on **Allianz Life** alone exposed 1.5 million customers, while **TransUnion** exposed 4.4 million individuals. The attack vector — social engineering to trick employees into approving malicious OAuth apps — demonstrated that even well-resourced financial institutions are vulnerable when their third-party ecosystem is exploited. (Sources: [FortifyData](https://fortifydata.com/blog/top-third-party-data-breaches-in-2025); [UpGuard Financial Services](https://www.upguard.com/blog/biggest-data-breaches-financial-services))

**United States — Healthcare Sector**

The **Change Healthcare** breach (detected February 2024, with notifications continuing through 2025–2026) remains the largest healthcare data breach in history at 192.7 million individuals. The root cause — compromised Citrix credentials without MFA — was a fundamental access-control failure. The **Conduent Business Services** breach (2025) exposed 62+ million Americans' PHI, and **HealthEC LLC** exposed 45 million patient records. Together, these three incidents alone affected nearly 300 million people. (Sources: [Hyperproof](https://hyperproof.io/resource/understanding-the-change-healthcare-breach); [UpGuard Healthcare Breaches](https://www.upguard.com/blog/biggest-data-breaches-in-healthcare); [Black Kite 2025](https://blackkite.com/reports/black-kite-third-party-breach-report-2025))

### 3.2 Europe

**European Banks — Systemic Vendor Risk**

Third-party cyber breaches surged 25% at Europe's top 100 financial institutions in 2025. Research found that nearly all major firms experienced at least one cyber breach through a supplier or service provider in the previous 12 months. The **MOVEit campaign** (2023) continued to produce downstream effects through 2025, with Deutsche Bank, ING Bank, Postbank, and Comdirect all reporting data leaks originating from the same third-party business vendor exploited by the Cl0p ransomware group. (Sources: [SecurityBrief UK](https://securitybrief.co.uk/story/third-party-cyber-breaches-surge-25-in-europe-s-top-banks); [ENISA Threat Landscape Finance 2024–2025](https://www.enisa.europa.eu/sites/default/files/2025-02/Finance%20TL%202024_Final.pdf))

**Switzerland — UBS and Pictet via Chain IQ Group (June 2025):** A sophisticated ransomware attack on procurement vendor Chain IQ Group AG exposed over 130,000 employee records from UBS and Pictet, among others. The attackers used previously unseen tools and tactics. (Source: [FortifyData Third-Party Breaches 2025](https://fortifydata.com/blog/top-third-party-data-breaches-in-2025))

**UK — Healthcare and Retail**

- **Advanced Computer Software Group:** The ICO fined the NHS software supplier £3.08 million for ransomware failings, explicitly citing multi-factor authentication gaps in critical health supply chains. (Source: [UpGuard Biggest Data Breaches UK](https://www.upguard.com/blog/biggest-data-breaches-uk))
- **Marks & Spencer (April 2025):** A targeted cyberattack traced back to social engineering against employees at a TCS contractor forced M&S to manually operate logistics, disrupted food distribution, and temporarily halted online shopping. Over 6.5 million customer records were compromised. (Source: [FortifyData Third-Party Breaches 2025](https://fortifydata.com/blog/top-third-party-data-breaches-in-2025))
- **Harrods (May 2025):** Attackers exploited a flaw in a third-party supplier portal, exposing customer data. (Source: [FortifyData Third-Party Breaches 2025](https://fortifydata.com/blog/top-third-party-data-breaches-in-2025))

**EU DORA Implementation:** The Digital Operational Resilience Act, effective January 2025, mandates rigorous IT risk management, incident reporting, operational resilience testing, and third-party risk management for financial entities. Despite this, a CNBC report noted that many banks remain unprepared. (Source: [CNBC — DORA](https://www.cnbc.com/2025/01/17/dora-many-banks-arent-ready-for-tough-new-eu-cybersecurity-law.html))

### 3.3 Asia-Pacific

**Japan — Highest Third-Party Breach Rate in the Region**

SecurityScorecard's 2025 report found that **60% of breaches in Japan involve third parties**, one of the highest rates globally. The Aon 2026 survey confirmed that cyber and supply chain risks are reshaping Japan's business landscape, with companies urgently needing to address supply chain risk management. (Sources: [SecurityScorecard 2025 Global Third-Party Breach Report](https://securityscorecard.com/company/press/securityscorecard-2025-global-third-party-breach-report-reveals-surge-in-vendor-driven-attacks); [Aon Japan Survey](https://www.aon.com/apac/in-the-press/asia-newsroom/2026/cyber-and-supply-chain-risks-reshaping-japans-business-landscape-aon-survey))

**Singapore — 71.4% Third-Party Breach Rate**

Singapore recorded the highest third-party breach rate globally at 71.4%, according to SecurityScorecard's analysis of 1,000 breaches. The city-state's highly interconnected financial and technology sectors make it particularly vulnerable to cascading vendor failures. (Source: [SecurityScorecard 2025 Global Third-Party Breach Report](https://securityscorecard.com/company/press/securityscorecard-2025-global-third-party-breach-report-reveals-surge-in-vendor-driven-attacks))

**Australia — Healthcare Sector Under Siege**

- **MediSecure (2024–2025):** Approximately 12.9 million individuals had their personal and health information relating to prescriptions exposed. The breach affected data distributed by MediSecure's systems until November 2023. (Source: [Australian Government Home Affairs — MediSecure](https://www.homeaffairs.gov.au/about-us/our-portfolios/cyber-security/cyber-coordinator/medisecure-cyber-security-incident))
- **Australian Clinical Labs (ACL) (February 2025):** 940.7 GB of data exfiltrated. The Federal Court imposed A$5.8 million in penalties for failures including failure to assess whether an eligible data breach had occurred. (Source: [UpGuard Biggest Data Breaches Australia](https://www.upguard.com/blog/biggest-data-breaches-australia))
- **OAIC Data:** Australia received 1,205 data breach notifications in 2025 (up 8% from 2024), with health service providers the most frequently affected sector (225 notifications). (Source: [UpGuard Biggest Data Breaches Australia](https://www.upguard.com/blog/biggest-data-breaches-australia))

**Korea — SK Telecom Breach**

A major telecommunications/data breach resulted in a $96 million fine, demonstrating that regulatory costs in Asia-Pacific are escalating rapidly. (Source: [Ethixbase360 Top 10 Third-Party Breaches 2025](https://ethixbase360.com/top-10-third-party-cyber-breaches-of-2025-what-they-mean-for-your-tprm-strategy))

### 3.4 Middle East and Africa

**Dubai and Lebanon Healthcare Sector (2025):**

- A ransomware attack on **Dubai's NHS Moorfields Hospital** was carried out through an IT provider, compromising patient data.
- A breach in **Lebanon** exposed over a decade of patient records from four hospitals: Bellevue Medical Center, Nini Hospital, Notre Dame University Hospital, and Haykel Hospital.
- Similar incidents surged across Saudi Arabia and the UAE, disrupting healthcare services through attacks on external vendors. (Source: [Cedar Rose — Managing Third-Party Risks in Healthcare](https://www.cedar-rose.com/blog/managing-third-party-risks-in-healthcare-3-key-risks-strategies))

---

## Section 4: Risk Management Best Practices Now Being Adopted

### 4.1 From Static Assessments to Continuous Intelligence

The most significant shift in TPRM practice is the move from periodic, questionnaire-based vendor assessments to **continuous monitoring** using real-time threat intelligence.

**What is changing:**
- Organizations are replacing annual vendor security questionnaires with real-time intelligence feeds covering ransomware susceptibility, dark web credential exposure, and known exploited vulnerabilities.
- The Black Kite report found that self-reported vendor security questionnaires "produced no useful signal" in the Cencora, Cleo, or HealthEC incidents — the compromised vendors were trusted partners. Real-time intelligence on rising RSI scores or dark web exposure would have surfaced the risk earlier. (Source: [Black Kite 2025 Third-Party Breach Report](https://blackkite.com/reports/black-kite-third-party-breach-report-2025))
- The **"silent window"** — the gap between detection (median 10 days) and public disclosure (average 117 days) — is being addressed through continuous monitoring tools that provide visibility into the active threat layer before a breach is disclosed. (Source: [Black Kite 2026 Third-Party Breach Report](https://blackkite.com/reports/third-party-breach-report-2026))

### 4.2 Mapping the "Fragile Core" — Concentration Risk Management

Organizations are adopting **concentration-aware resilience** — identifying the central nodes in their supply chain whose failure would trigger cascading operational failures.

**Practices being adopted:**
- Mapping all critical vendor dependencies and identifying single points of failure.
- Modeling the financial and operational impact of a failure at the most concentrated points of dependency.
- Requiring vendors to demonstrate their own subcontractor risk management (fourth-party risk).
- The 2026 TPRM guidance from Safe Security emphasizes that "nth-party risk" — the risk introduced by vendors' vendors — is now a growing concern. (Source: [Safe Security 2026 TPRM Guide](https://safe.security/resources/blog/2026-guide-to-third-party-risk-management-tprm))

### 4.3 Contractual and Regulatory Levers

**Regulatory drivers reshaping TPRM:**

| Regulation | Region | Key Requirements |
|------------|--------|------------------|
| **DORA** | EU | Mandatory ICT third-party register, pre-outsourcing risk assessments, contractual clauses for incident reporting and audit rights, concentration risk assessments |
| **NIS2** | EU | Supply chain security policies, incident reporting, security clauses in vendor contracts |
| **SEC Cyber Rules** | US | 4-business-day materiality disclosure; third-party incidents explicitly covered |
| **HIPAA** | US | OCR now directly targeting business associates; OCR settlements in 2025 included Northeast Radiology ($350K), Warby Parker ($1.5M), BayCare Health System ($800K) |
| **Australian Privacy Act** | Australia | A$5.8M penalty against ACL established that delay and inadequate assessment are independently punishable |
| **Japan APPI** | Japan | Vendor supervision requirements codified |

**Sources:** [Cynomi TPRM Statistics 2026](https://cynomi.com/blog/third-party-risk-management-statistics-every-msp-should-know-in-2026); [CNBC DORA](https://www.cnbc.com/2025/01/17/dora-many-banks-arent-ready-for-tough-new-eu-cybersecurity-law.html); [HIPAA Journal 2026 Statistics](https://www.hipaajournal.com/healthcare-data-breach-statistics); [UpGuard Australia](https://www.upguard.com/blog/biggest-data-breaches-australia)

### 4.4 Zero Trust Applied to Third-Party Access

The Change Healthcare breach — caused by a single set of compromised Citrix credentials without MFA — has driven a wave of **Zero Trust** adoption for vendor access.

**Practices being adopted:**
- Mandatory MFA for all vendor access to internal systems.
- Just-in-time (JIT) privileged access management for third-party users.
- Network segmentation to limit vendor access to only the systems and data required.
- Continuous session monitoring and behavioral analytics for vendor accounts.
- The AHA (American Hospital Association) now recommends treating cyber disruptions like natural disasters, with explicit business continuity planning for third-party system failures. (Source: [AHA Monitoring Third-Party Cyber Risks](https://www.aha.org/08/2025/ke/monitoring-and-mitigating-third-party-cyber-risks))

### 4.5 API and SaaS Security Controls

Given the centrality of API and SaaS compromises in 2025's breaches, organizations are implementing:

- API gateways with rate limiting, encryption, and strict permission controls.
- OAuth token lifecycle management — the Salesforce OAuth campaign demonstrated that once tokens are stolen, they can be used to pivot across hundreds of connected services.
- Third-party SaaS application discovery and inventory — the Hy-Vee/Atlassian breach (June 2025) using stolen infostealer credentials showed that organizations often lack visibility into which SaaS tools their vendors use. (Source: [FortifyData Third-Party Breaches 2025](https://fortifydata.com/blog/top-third-party-data-breaches-in-2025))

### 4.6 Software Supply Chain Security (Technology Sector)

The technology sector is adopting **SBOMs (Software Bill of Materials)** and **NIST C-SCRM (Cybersecurity Supply Chain Risk Management)** frameworks:

- CISA's emergency alert on the **Shai-Hulud npm worm** (September 2025) drove immediate adoption of dependency pinning, credential rotation, and CI/CD pipeline scanning.
- The **tj-actions compromise** at Black Hat USA 2025 highlighted the risk of compromised CI/CD workflows.
- Organizations are now pinning npm package dependency versions to known safe releases and rotating all developer credentials after any suspected compromise. (Source: [CISA Alert on npm Compromise](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem); [TechDemocracy Software Supply Chain Attacks 2025](https://www.techdemocracy.com/resources/top-5-software-supply-chain-attacks-in-2025-266))

### 4.7 Cyber Insurance as a TPRM Driver

Major cyber insurance carriers now require vendor risk assessments as a standard underwriting condition. Organizations with continuous monitoring and documented vendor oversight are rewarded with more favorable terms. The Black Kite report notes that insurers are increasingly using Ransomware Susceptibility Index data to price policies, making vendor security posture directly tied to premium costs. (Sources: [Cynomi TPRM Statistics 2026](https://cynomi.com/blog/third-party-risk-management-statistics-every-msp-should-know-in-2026); [Black Kite 2026 Third-Party Breach Report](https://blackkite.com/reports/third-party-breach-report-2026))

---

## Section 5: Key Takeaways for Risk Managers

**1. The "blast radius" is the new risk metric.** Every vendor relationship now carries a multiplier effect. With 5.28 downstream victims per breached vendor, a single weak vendor can compromise your entire ecosystem.

**2. Credentials are the #1 root cause.** The IBM 2025 report identifies stolen credentials as the most expensive initial vector at $4.92 million per incident. MFA is no longer optional — it is the baseline requirement for every vendor with network access.

**3. Concentration is the hidden risk.** The "Elite 50" vendors — the most interconnected shared service providers — are statistically the weakest link. 70% have unpatched KEV-listed vulnerabilities. Risk managers must map their concentration risk and model failure scenarios.

**4. The silent window is growing.** The disclosure gap has widened from 76 days (2024) to 117 days (2025). Continuous monitoring, not periodic questionnaires, is the only way to shrink this window.

**5. Regulation is accelerating.** DORA, NIS2, SEC cyber rules, and Australian Privacy Act enforcement are creating a compliance imperative for TPRM. The ACL penalty in Australia established that failing to assess and report a breach is independently punishable.

**6. Healthcare remains the highest-risk sector.** At $7.42 million average breach cost, 279-day breach lifecycle, and 41% of breaches starting with third parties, healthcare requires the most aggressive TPRM posture.

**7. Finance is the most targeted sector.** 90% of breaches against financial institutions are financially motivated. Supply chain compromise contributed to 30% of finance-sector breaches in 2025. DORA compliance is now mandatory for EU financial institutions.

**8. Technology is the enabler and the vulnerability.** Technology vendors enabled 46.75% of third-party breaches. Open-source supply chain attacks (npm, PyPI, GitHub) are growing exponentially, with Cybersecurity Ventures projecting the annual cost of software supply chain attacks to reach $138 billion by 2031.

---

## References

1. Black Kite. "Third-Party Breach Report 2026." https://blackkite.com/reports/third-party-breach-report-2026
2. Black Kite. "Third-Party Breach Report 2025." https://blackkite.com/reports/black-kite-third-party-breach-report-2025
3. Verizon. "2025 Data Breach Investigations Report." https://www.verizon.com/about/news/2025-data-breach-investigations-report-apac
4. IBM. "Cost of a Data Breach Report 2025." https://www.ibm.com/reports/data-breach
5. SecurityScorecard. "2025 Global Third-Party Breach Report." https://securityscorecard.com/company/press/securityscorecard-2025-global-third-party-breach-report-reveals-surge-in-vendor-driven-attacks
6. Cynomi. "Third-Party Risk Management Statistics Every MSP Should Know in 2026." https://cynomi.com/blog/third-party-risk-management-statistics-every-msp-should-know-in-2026
7. FortifyData. "Third-Party Data Breaches in 2026 (Updated Monthly)." https://fortifydata.com/blog/top-third-party-data-breaches-in-2025
8. UpGuard. "34 Biggest Healthcare Data Breaches (Updated July 2026)." https://www.upguard.com/blog/biggest-data-breaches-in-healthcare
9. UpGuard. "26 Biggest Data Breaches in Finance (Updated July 2026)." https://www.upguard.com/blog/biggest-data-breaches-financial-services
10. UpGuard. "23 Biggest Data Breaches in Australia (Updated July 2026)." https://www.upguard.com/blog/biggest-data-breaches-australia
11. UpGuard. "Biggest Data Breaches in the UK (Updated July 2026)." https://www.upguard.com/blog/biggest-data-breaches-uk
12. UpGuard. "Biggest Data Breaches in Europe (Updated July 2026)." https://www.upguard.com/blog/biggest-data-breaches-europe
13. Ethixbase360. "Top 10 Third-Party Cyber Breaches of 2025." https://ethixbase360.com/top-10-third-party-cyber-breaches-of-2025-what-they-mean-for-your-tprm-strategy
14. Hyperproof. "Understanding the Change Healthcare Breach." https://hyperproof.io/resource/understanding-the-change-healthcare-breach
15. HIPAA Journal. "Healthcare Data Breach Statistics – Updated for 2026." https://www.hipaajournal.com/healthcare-data-breach-statistics
16. HIPAA Journal. "More Than One-Third of Data Breaches Due to Third-Party Supplier Compromises." https://www.hipaajournal.com/more-than-one-third-data-breaches-third-party-compromises
17. Safe Security. "2026 Guide to Third Party Risk Management (TPRM)." https://safe.security/resources/blog/2026-guide-to-third-party-risk-management-tprm
18. CISA. "Widespread Supply Chain Compromise Impacting npm Ecosystem." https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem
19. TechDemocracy. "Top 5 Software Supply Chain Attacks in 2025." https://www.techdemocracy.com/resources/top-5-software-supply-chain-attacks-in-2025-266
20. SecureFrame. "Supply Chain Attacks: Recent Examples, Trends & How to Prevent Them in 2026." https://secureframe.com/blog/supply-chain-attacks
21. Cybersecurity Dive. "Hackers steal sensitive data from major banking industry vendor." https://www.cybersecuritydive.com/news/bank-vendor-cyberattack-supply-chain/806293
22. CNBC. "Banks fail to comply with EU DORA cyber law as it enters effect." https://www.cnbc.com/2025/01/17/dora-many-banks-arent-ready-for-tough-new-eu-cybersecurity-law.html
23. SecurityBrief UK. "Third-party cyber breaches surge 25% in Europe's top banks." https://securitybrief.co.uk/story/third-party-cyber-breaches-surge-25-in-europe-s-top-banks
24. ENISA. "Threat Landscape: Finance Sector 2024–2025." https://www.enisa.europa.eu/sites/default/files/2025-02/Finance%20TL%202024_Final.pdf
25. American Hospital Association. "Monitoring and Mitigating Third-party Cyber Risks." https://www.aha.org/08/2025/ke/monitoring-and-mitigating-third-party-cyber-risks
26. The Record. "Hackers breach internal servers of tech provider for Britain's health service." https://therecord.media/uk-nhs-tech-provider-dxs-discloses-hack
27. Australian Government – Department of Home Affairs. "MediSecure cyber security incident." https://www.homeaffairs.gov.au/about-us/our-portfolios/cyber-security/cyber-coordinator/medisecure-cyber-security-incident
28. Aon. "Cyber and Supply Chain Risks Reshaping Japan's Business Landscape." https://www.aon.com/apac/in-the-press/asia-newsroom/2026/cyber-and-supply-chain-risks-reshaping-japans-business-landscape-aon-survey
29. Cedar Rose. "Managing Third-Party Risks in Healthcare: 3 Key Risks & Strategies." https://www.cedar-rose.com/blog/managing-third-party-risks-in-healthcare-3-key-risks-strategies
30. Compunnel. "Supply Chain Breaches 2025: The Weakest Links That Cost Millions." https://www.compunnel.com/blogs/supply-chain-breaches-2025-the-weakest-links-that-cost-millions
31. DeepStrike. "Supply Chain Attack Statistics 2025: Costs, Cases, Defenses." https://deepstrike.io/blog/supply-chain-attack-statistics-2025
32. DeepStrike. "Healthcare Cybersecurity Statistics 2026." https://deepstrike.io/blog/healthcare-cybersecurity-statistics
33. HelpNetSecurity. "Shadow AI, deepfakes, and supply chain compromise are rewriting the financial sector threat playbook." https://www.helpnetsecurity.com/2026/04/22/financial-sector-cyber-threats-report
34. RFA. "Year in Review: The Top 6 Cyber Attacks That Targeted Financial Firms in 2025." https://www.rfa.com/post/year-in-review-the-top-6-cyber-attacks-that-targeted-financial-firms-in-2025
35. ProcessUnity. "10 Critical Third-Party Risk Management Challenges in 2026." https://www.processunity.com/resources/blogs/10-critical-third-party-risk-management-challenges-and-how-to-mitigate-them
36. Ponemon-Sullivan Privacy Report. "State of Third-Party Risk Assessments 2026." https://ponemonsullivanreport.com/2026/03/state-of-third-party-risk-assessments
37. Cobalt. "Healthcare Data Breach Statistics: 2025 Roundup." https://www.cobalt.io/blog/healthcare-data-breach-statistics
38. ECRI. "Mitigating Third-Party Risks in Healthcare." https://home.ecri.org/blogs/ecri-blog/mitigating-third-party-risks-in-healthcare-protecting-patient-care-and-data
39. Black Cell. "Data Protection Incidents Related to the Supply Chain in 2025." https://blackcell.io/data-protection-incidents-related-to-the-supply-chain-in-2025
40. SWIF. "Supply Chain Attack Statistics for 2026." https://www.swif.ai/blog/supply-chain-attack-statistics
