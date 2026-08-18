

# OCR HIPAA Enforcement Analysis: High-Penalty Actions, Security Rule Violations, and Corrective Action Trends (2021–2026)

## Executive Summary

Over the past five years, the HHS Office for Civil Rights (OCR) has intensified its HIPAA enforcement efforts, collecting over $145 million in total penalties since 2003, with a notable acceleration in both settlement volume and penalty amounts from 2021 through 2026. This report examines the most significant enforcement actions exceeding $1 million, identifies the Security Rule violations that most frequently drive large penalties, provides concrete examples of risk assessment failures, and details the typical corrective action requirements imposed through resolution agreements.

---

## Part I: High-Penalty Cases Over $1 Million (2021–2026)

The following table summarizes the largest OCR enforcement actions from the past five years. These cases span both large healthcare providers (covered entities) and business associates, and they consistently involve fundamental Security Rule failures.

| Year | Entity | Type | Penalty | Primary Violations Cited |
|------|--------|------|---------|--------------------------|
| 2021 | Excellus Health Plan | Covered Entity (Health Plan) | $5,100,000 | Multi-year risk analysis failure; risk management failure; lack of information system activity reviews; lack of technical policies to prevent unauthorized ePHI access |
| 2021 | CHSPSC, LLC | Business Associate | $2,300,000 | Failure to implement security measures; breach affecting >6 million records |
| 2023 | L.A. Care Health Plan | Covered Entity (Health Plan) | $1,300,000 | Risk analysis failure; insufficient security measures; insufficient reviews of information system activity; impermissible disclosure of ePHI of 1,498 individuals |
| 2023 | Banner Health | Covered Entity (Hospital System) | $1,250,000 | Risk analysis failure; failure to review system activity; failure to verify identity for PHI access; lack of technical safeguards |
| 2024 | Montefiore Medical Center | Covered Entity (Hospital) | $4,750,000 | Failure to conduct comprehensive risk analysis; failure to implement procedures to review records of information system activity; failure to implement audit controls |
| 2024 | Gulf Coast Pain Consultants | Covered Entity (Provider) | $1,190,000 | HIPAA Security Rule violations (risk analysis failure central) |
| 2025 | Solara Medical Supplies | Covered Entity (DME Supplier) | $3,000,000 | Risk analysis failure; risk management failure; breach notification failure; impermissible disclosure of ePHI of 114,007 patients |
| 2025 | Warby Parker | Covered Entity (Retail/Eyewear) | $1,500,000 (CMP) | No adequate risk analysis; insufficient security measures; no procedures to review system activity logs (credential-stuffing attack) |
| 2026 | MMG Fusion, LLC | Business Associate | $10,000* | Impermissible disclosure of PHI (~15 million individuals affected); risk analysis failure; failure to timely notify covered entities of breach |

*While MMG Fusion's $10,000 monetary amount is low, the case is notable for its massive scale (15 million individuals affected) and the three-year corrective action plan imposed. The low penalty reflected OCR's consideration of the entity's financial condition.
**Source:** HHS OCR Resolution Agreements index; HIPAA Journal penalty database; Medcurity analysis of OCR settlements.

**Key observations:**
- Risk analysis failure is the single common thread across every high-penalty case.
- Business associates are increasingly targeted: CHSPSC ($2.3M), MMG Fusion ($10K with 3-year CAP), and actions against BST & Co. CPAs, Health Fitness Corporation, and Comstar show OCR's expanding focus on vendors.
- The largest single-year total in recent history was 2022 (22 settlements), followed by 2025 (21 settlements).

---

## Part II: Top 10 Security Rule Violations That Most Often Lead to Large Penalties

Based on analysis of OCR enforcement actions from 2021–2026, the following Security Rule violations are the most frequently cited in high-penalty cases. The list is ordered by prevalence in settlements exceeding $1 million.

| Rank | Violation (45 CFR §) | Description | Frequency in High-Penalty Cases |
|------|---------------------|-------------|-------------------------------|
| 1 | **Risk Analysis Failure** (§164.308(a)(1)(ii)(A)) | Failure to conduct an accurate and thorough assessment of risks and vulnerabilities to ePHI | Cited in ~90% of all Security Rule enforcement actions |
| 2 | **Risk Management Failure** (§164.308(a)(1)(ii)(B)) | Failure to implement security measures sufficient to reduce identified risks to a reasonable level | Nearly universal in cases citing risk analysis failure |
| 3 | **Information System Activity Review** (§164.308(a)(1)(ii)(D)) | Failure to implement procedures to regularly review records of information system activity (e.g., audit logs, access reports) | Present in Excellus, Montefiore, L.A. Care, Banner, Warby Parker |
| 4 | **Audit Controls** (§164.312(b)) | Failure to implement hardware, software, and/or procedural mechanisms to record and examine activity in information systems | Cited in Montefiore ($4.75M) and multiple other large cases |
| 5 | **Access Control** (§164.312(a)(1)) | Failure to implement technical policies and procedures for ePHI access (e.g., unique user IDs, emergency access procedures) | Present in Banner Health, Excellus, and BayCare cases |
| 6 | **Security Incident Procedures** (§164.308(a)(6)(ii)) | Failure to identify and respond to suspected or known security incidents | Cited in Solara ($3M) and multiple ransomware cases |
| 7 | **Workforce Security / Training** (§164.308(a)(5)(ii)(A)) | Failure to provide adequate security awareness training for all workforce members | Cited in Children's Hospital Colorado ($548K), Montefiore |
| 8 | **Device and Media Controls** (§164.310(d)(1)) | Failure to address disposal, re-use, accountability, and data backup of devices containing ePHI | Common in theft/loss cases (e.g., unencrypted laptops) |
| 9 | **Encryption of ePHI** (§164.312(a)(2)(iv) / §164.312(e)(2)(ii)) | Failure to encrypt ePHI at rest and in transit | Frequently a compounding factor (e.g., Heritage Valley, OK State University) |
| 10 | **Business Associate Agreements** (§164.308(b)(1)) | Failure to obtain satisfactory written assurances from business associates | Growing trend; cited in CHSPSC, MMG Fusion, and Elgon cases |

**Source:** HHS OCR Enforcement Highlights; HIPAA Journal; Medcurity 2026 Risk Analysis Pattern Report; LegalClarity OCR Settlement News.

---

## Part III: Common Risk Assessment Failures with Concrete Examples

OCR's own Risk Analysis Initiative (launched October 2024) has made §164.308(a)(1)(ii)(A) compliance a standalone enforcement priority. The following three failures recur across high-penalty cases.

### Failure 1: Complete Absence of a Compliant Risk Analysis

**The Problem:** The entity never performed a documented, organization-wide risk analysis that meets the Security Rule's requirements. This is the most common finding in OCR investigations.

**Concrete Example — Solara Medical Supplies ($3,000,000, January 2025)**
Solara Medical Supplies, a national durable medical equipment supplier, suffered a phishing attack in 2019 that exposed the ePHI of 114,007 individuals. OCR's investigation found that Solara had **failed to conduct an accurate and thorough risk analysis** to assess risks and vulnerabilities to ePHI. It also failed to implement risk management and failed to provide timely breach notifications. The resolution agreement required a comprehensive, organization-wide risk analysis, a risk management plan, policy revisions, enhanced workforce training, and two years of OCR monitoring.
**Source:** HHS.gov – Solara Medical Supplies Resolution Agreement and Corrective Action Plan; LegalClarity OCR Settlement News.

### Failure 2: Incomplete or Non-Comprehensive Risk Analysis

**The Problem:** The entity performed a risk analysis, but it did not cover all ePHI, all systems, all locations, or all relevant threats. OCR expects an enterprise-wide scope.

**Concrete Example — Montefiore Medical Center ($4,750,000, December 2024)**
Montefiore Medical Center, a large New York hospital system, had a breach when an employee stole and sold patient information. OCR's investigation found that Montefiore **failed to conduct a comprehensive risk analysis** that covered all systems containing ePHI. The entity also failed to implement procedures to regularly review records of information system activity and failed to implement hardware, software, and/or procedural mechanisms to record and examine system activity. The settlement required a multi-year corrective action plan with a full enterprise-wide risk analysis.
**Source:** HHS.gov; HIPAA Journal; Legal HIE 2024 Year in Review.

### Failure 3: Failure to Update Risk Analysis After Environmental or Operational Changes

**The Problem:** The entity may have conducted an initial risk analysis but did not update it after significant changes (e.g., new technology, new threats, expansion of operations, or after a breach).

**Concrete Example — Warby Parker ($1,500,000 Civil Money Penalty, February 2025)**
Warby Parker experienced a credential-stuffing attack between September and November 2018 that exposed nearly 198,000 individuals' data. Smaller follow-up attacks occurred in 2020 and 2022. OCR determined that Warby Parker **failed to conduct an adequate risk analysis** at any point relevant to the Security Rule violations. The company also failed to implement sufficient security measures and failed to implement procedures to review system activity logs. Because OCR imposed a civil money penalty (CMP) rather than a negotiated settlement, no corrective action plan was attached, but the $1.5M penalty reflects the gravity of the failures.
**Source:** HHS.gov – Penalty Against Warby Parker; BankInfoSecurity; LegalClarity.

---

## Part IV: Typical Corrective Actions OCR Requires in Resolution Agreements

When OCR resolves a case through a settlement agreement (rather than a CMP), the entity must sign a **Resolution Agreement** and a **Corrective Action Plan (CAP)** . OCR monitors compliance for a defined period—typically **two to three years**. The following corrective actions appear in virtually every high-penalty resolution agreement.

### 1. Enterprise-Wide Risk Analysis
- Conduct a complete, accurate, and thorough risk analysis that covers all ePHI created, received, maintained, or transmitted by the organization.
- The analysis must identify all potential risks and vulnerabilities to the confidentiality, integrity, and availability of ePHI.
- Must be performed by or under the oversight of a qualified professional.
- **Examples:** Solara Medical Supplies, Montefiore Medical Center, L.A. Care Health Plan, Banner Health, Gulf Coast Pain Consultants.

### 2. Risk Management Plan
- Develop and implement a written risk management plan that specifies security measures sufficient to reduce identified risks to a reasonable and appropriate level.
- The plan must include a timeline for implementation and assign responsibility for each action.
- **Examples:** All cases above; also BST & Co. CPAs, Northeast Radiology.

### 3. Policy and Procedure Revisions
- Review and revise all HIPAA Privacy, Security, and Breach Notification Rule policies and procedures.
- Revised policies must be submitted to OCR for review and approval.
- **Examples:** Every resolution agreement since 2021.

### 4. Workforce Training
- Provide enhanced HIPAA training to all workforce members who have access to ePHI.
- Training must cover the updated policies and procedures, the risk analysis findings, and the entity's specific obligations.
- Training must be provided initially and then annually (or more frequently) during the CAP term.
- **Examples:** Solara Medical Supplies, Montefiore, Banner Health, Children's Hospital Colorado.

### 5. Third-Party Assessment / Independent Review
- Retain an independent third-party assessor to evaluate the entity's compliance with the CAP and the HIPAA Rules.
- The assessor's reports must be submitted to OCR.
- **Examples:** MMG Fusion (3-year monitoring), Gulf Coast Pain Consultants, Solara Medical Supplies.

### 6. Annual Compliance Reporting
- Submit annual reports to OCR detailing the entity's progress in implementing the CAP, including any breaches or security incidents during the reporting period.
- Reports must be certified by a senior official of the entity.
- **Examples:** All resolution agreements with a multi-year CAP.

### 7. OCR Monitoring and Oversight
- OCR retains the right to conduct site visits, interviews, and document reviews throughout the CAP term.
- Failure to comply with the CAP can result in additional CMPs or enforcement action.
- **Examples:** Standard in all OCR resolution agreements.

### 8. Specific Remediation Based on the Underlying Violation
- **If access control failures:** Implement unique user IDs, automatic logoff, encryption, and emergency access procedures.
- **If audit control failures:** Implement mechanisms to record and examine activity in all information systems containing ePHI.
- **If BAA failures:** Obtain and maintain HIPAA-compliant business associate agreements with all vendors.
- **If breach notification failures:** Develop and implement breach notification policies and procedures that comply with the 60-day reporting requirement.

**Summary of CAP Duration:** Most CAPs run for **two years** (e.g., Solara, BayCare, Top of the World Ranch). The most egregious or complex cases receive **three-year CAPs** (e.g., MMG Fusion, OHSU 2016 settlement). OCR may also require a longer period if the entity had a prior enforcement action.

**Source:** HHS.gov – Resolution Agreements page; HHS OCR press releases for individual settlements; Medcurity 2026 analysis; LegalClarity OCR Settlement News.

---

## Key Trends and Takeaways

1. **Risk analysis is the non-negotiable foundation.** Approximately 90% of OCR Security Rule enforcement actions cite a deficient risk analysis. The Risk Analysis Initiative (Oct 2024) formalized this focus, producing 12 enforcement actions in its first 18 months.

2. **Business associates face equal exposure.** OCR has increasingly targeted business associates—CHSPSC ($2.3M), MMG Fusion (15M individuals affected), BST & Co. CPAs ($175K), Health Fitness Corporation ($227K)—and the trend is accelerating. Third-party involvement in healthcare data breaches doubled from 15% to 30% year-over-year in 2025.

3. **Corrective actions are more burdensome than the fines.** The cost of implementing a multi-year CAP—including independent assessments, annual reporting, and comprehensive remediation—often far exceeds the monetary penalty.

4. **Small breaches can trigger large penalties.** High-dollar settlements frequently stem from breaches affecting relatively few individuals (e.g., Memorial Hermann $2.4M for 1 person; NY-Presbyterian $2.2M for 2 people). The penalty reflects the underlying compliance failure, not the breach size.

5. **OCR is using CMPs more aggressively.** The Warby Parker and Gulf Coast Pain Consultants cases show OCR is willing to pursue civil money penalties (with no negotiated settlement) when entities fail to cooperate or demonstrate willful neglect.

---

## References

1. HHS OCR – Resolution Agreements Index
   https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/index.html

2. HHS OCR – Enforcement Highlights (cumulative data through October 2024)
   https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/data/enforcement-highlights/index.html

3. HHS OCR – Solara Medical Supplies Resolution Agreement and Corrective Action Plan (January 2025)
   https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/solara-ra-cap/index.html

4. HHS OCR – Penalty Against Warby Parker (February 2025)
   https://www.hhs.gov/press-room/penalty-against-warby-parker.html

5. HHS OCR – MMG Fusion, LLC Settlement (March 2026)
   https://www.hhs.gov/press-room/ocr-mmg-fusion-hipaa-agreement.html

6. HHS OCR – BST & Co. CPAs, LLP Settlement (August 2025)
   https://www.hhs.gov/press-room/hhs-ocr-bst-hipaa-settlement.html

7. HHS OCR – Top of the World Ranch Treatment Center Settlement (February 2026)
   https://www.hhs.gov/press-room/ocr-settles-hipaa-security-rule-investigation-twrtc.html

8. HIPAA Journal – HIPAA Violation Fines and Settlements (2026 update)
   https://www.hipaajournal.com/hipaa-violation-fines

9. HIPAA Journal – What Are the Penalties for HIPAA Violations? (2026 update)
   https://www.hipaajournal.com/what-are-the-penalties-for-hipaa-violations-7096

10. FaxSipIt – HIPAA Violation Statistics: 2026 Enforcement, Fines & Breach Data
    https://www.faxsipit.com/blogs/hipaa-violation-statistics

11. Medcurity – The Risk Analysis Failure Pattern in HHS OCR Settlements (2026)
    https://medcurity.com/risk-analysis-failure-pattern-hhs-ocr-settlements-2026

12. Ogletree Deakins – 2025 Enforcement Trends: Risk Analysis Failures at the Center of HHS's Multimillion-Dollar HIPAA Penalties
    https://ogletree.com/insights-resources/blog-posts/2025-enforcement-trends-risk-analysis-failures-at-the-center-of-hhss-multimillion-dollar-hipaa-penalties

13. LegalClarity – OCR HIPAA Settlement News: Latest Enforcement Actions
    https://legalclarity.org/ocr-hipaa-settlement-news-latest-enforcement-actions

14. Legal HIE – A Look Back at 2024: HIPAA Enforcement Year in Review
    https://www.legalhie.com/a-look-back-at-2024-hipaa-enforcement-year-in-review

15. MedComply.ai – HIPAA Enforcement Tracker: Every OCR Fine and Settlement
    https://medcomply.ai/enforcement

16. HHS OCR – Anthem Resolution Agreement ($16 million, 2018)
    https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/anthem/index.html

17. HHS OCR – 

18. Compliancy Group – HIPAA Violation Fines & Lawsuit Settlements Directory
    https://compliancy-group.com/hipaa-fines-directory-year

19. McDonald Hopkins – OCR Announces Risk Analysis Initiative Enforcement Actions
    https://www.mcdonaldhopkins.com/insights/news/ocr-announces-risk-analysis-initiative-enforcement-actions

20. BankInfoSecurity – Warby Parker HIPAA Fine Coverage
    https://www.bankinfosecurity.com/warby-parker-hipaa-fine-a-27571

