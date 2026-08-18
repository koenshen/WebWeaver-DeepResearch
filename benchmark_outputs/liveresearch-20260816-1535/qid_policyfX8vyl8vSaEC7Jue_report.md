

# Ransomware Payment Disclosure Requirements in the U.S.: A Cross-Industry Analysis

**Prepared for:** Risk Analysis – Incident Disclosure Procedures  
**Date:** August 17, 2026  
**Scope:** Regulatory filing and public/investor disclosure obligations across financial services, healthcare, and critical infrastructure

---

## Executive Summary

Ransomware payment disclosure in the United States has evolved into a multi-layered regulatory obligation spanning the SEC, Treasury’s OFAC, CISA, HHS, state financial regulators, and the Department of Justice. The patchwork of requirements creates both overlapping and divergent duties for enterprises. This report synthesizes the current regulatory landscape, enforcement actions that have exposed disclosure weaknesses, and strategic lessons for building a defensible disclosure framework.

---

## 1. Key Disclosure Requirements

### 1.1 SEC Cybersecurity Incident Disclosure Rules (Item 1.05 of Form 8-K)

The SEC’s final rule, adopted July 26, 2023, and effective December 18, 2023, requires public companies to disclose material cybersecurity incidents on Form 8-K within **four business days** of determining materiality. The disclosure must describe the material aspects of the incident’s nature, scope, and timing, as well as the material impact or reasonably likely material impact on the registrant’s financial condition and results of operations. [SEC Fact Sheet](https://www.sec.gov/newsroom/press-releases/2023-139)

**Materiality Standard:** The SEC applies the same standard articulated by the Supreme Court in *TSC Industries v. Northway* and *Basic v. Levinson* — information is material if there is a “substantial likelihood that a reasonable investor would consider it important” in making an investment decision. The SEC declined to adopt a cybersecurity-specific materiality standard. [SEC Statement on Cybersecurity Disclosure, Dec. 14, 2023](https://www.sec.gov/newsroom/speeches-statements/gerding-cybersecurity-disclosure-20231214)

**Ransomware-Specific C&DIs (June 24, 2024):** The SEC’s Division of Corporation Finance issued five new Compliance & Disclosure Interpretations that directly address ransomware payments:

| C&DI | Ruling |
|------|--------|
| **104B.05** | A materiality determination is required **even if** a ransomware payment ends the incident or returns data before the determination is made. |
| **104B.06** | Disclosure is required **even if** a payment ends the incident before the 8-K filing deadline. |
| **104B.07** | **Insurance reimbursement** does not automatically render an incident immaterial; registrants must consider long-term effects, brand perception, and potential insurance cost increases. |
| **104B.08** | The **size of the ransom payment alone** is not determinative of materiality. |
| **104B.09** | A **series of individually immaterial** ransomware incidents must be aggregated if related (e.g., same threat actor or vulnerability) and assessed collectively for materiality. |

[SEC C&DIs (full text)](https://www.sec.gov/divisions/corpfin/guidance/8-kinterp.htm) | [Mintz Summary](https://www.mintz.com/insights-center/viewpoints/2901/2024-07-11-sec-issues-updated-guidance-cybersecurity-incident)

**Annual Disclosures (Form 10-K):** Registrants must describe their cybersecurity risk management, strategy, and governance, including board oversight and management’s role in assessing material risks from cybersecurity threats.

### 1.2 OFAC Sanctions Advisory on Ransomware Payments

The Office of Foreign Assets Control (OFAC) issued an Updated Advisory on September 21, 2021, superseding its October 2020 advisory, warning that making or facilitating ransomware payments may violate U.S. sanctions laws. Key points:

- **Strict liability:** Violations do not require knowledge that the recipient is a sanctioned party; a U.S. person may be held liable even if unaware.
- **Strong discouragement:** The U.S. government “strongly discourages” ransom payments.
- **Third-party risk:** Financial institutions, cyber insurers, and incident response firms that facilitate payments face enforcement risk.
- **Mitigating factors** that reduce enforcement severity include: having a risk-based sanctions compliance program, following CISA cybersecurity guidance, promptly reporting to law enforcement, and providing full cooperation.
- OFAC has designated ransomware actors and virtual currency exchanges (e.g., SUEX OTC, S.R.O.) under its cyber-related sanctions program.

[OFAC Ransomware Advisory (Oct 2020)](https://ofac.treasury.gov/recent-actions/20201001) | [Hunton Summary of 2021 Updated Advisory](https://www.hunton.com/insights/legal/ofacs-updated-advisory-on-ransomware-payments)

### 1.3 CISA — Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA)

Enacted March 2022, CIRCIA requires CISA to develop regulations for covered entities in 16 critical infrastructure sectors to report:

- **Covered cyber incidents** within **72 hours** of reasonably believing the incident occurred.
- **Ransom payments** within **24 hours** of payment.

The proposed rule (NPRM published April 4, 2024) is not yet final; CISA extended the rulemaking deadline. Until final rules take effect, CISA encourages voluntary reporting. Covered sectors include financial services, healthcare, energy, IT, communications, and transportation, among others.

[CISA CIRCIA Overview](https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia) | [IBM Summary of CIRCIA](https://www.ibm.com/think/insights/circia-ransomware-reporting-important-details)

### 1.4 HIPAA / HHS — Healthcare Sector

HHS’s Office for Civil Rights (OCR) has issued guidance stating that ransomware that encrypts electronic protected health information (ePHI) generally constitutes a **presumed breach** under HIPAA because the ePHI is considered “acquired” by an unauthorized individual. Covered entities must:

- **Notify affected individuals** without unreasonable delay.
- **Notify the HHS Secretary** (breaches affecting 500+ individuals filed via OCR portal).
- **Notify media** (for breaches affecting 500+ individuals in a state/jurisdiction).
- **Timeline:** Breach notification must be made within **60 days** of discovery of the breach.

A breach may be avoided if the entity demonstrates a **low probability that the PHI has been compromised** based on a four-factor risk assessment (nature of PHI, unauthorized person, whether PHI was actually acquired/viewed, extent of mitigation). If ePHI was encrypted by the entity in accordance with HHS guidance, no breach notification is required, but careful analysis of the encryption implementation is needed.

[HHS Ransomware Fact Sheet](https://www.hhs.gov/hipaa/for-professionals/security/guidance/cybersecurity/ransomware-fact-sheet/index.html)

### 1.5 NYDFS — Financial Services (New York)

The New York Department of Financial Services (NYDFS) amended its cybersecurity regulation (23 NYCRR Part 500) effective November 2023, with full compliance by April 29, 2024. Key provisions:

- **Cybersecurity event notice:** Report to NYDFS within **72 hours** of determining a cybersecurity event has occurred, regardless of materiality.
- **Ransom payment notification:** Report within **24 hours** of making any extortion payment; within **30 days** submit a full written explanation of why the payment was made, alternatives considered, and compliance with applicable laws.
- **Reporting triggers:** Any successful deployment of ransomware on a material part of the information systems, or any intrusion involving privileged account access, must be reported.

[NYDFS Ransomware Guidance (June 2021)](https://www.dfs.ny.gov/industry_guidance/industry_letters/il20210630_ransomware_guidance) | [ACA Global Summary of NYDFS Amendments](https://www.acaglobal.com/industry-insights/new-york-state-department-financial-services-expands-cybersecurity-rules)

### 1.6 DOJ — False Claims Act (Civil Cyber-Fraud Initiative)

Launched in October 2021, the DOJ’s Civil Cyber-Fraud Initiative uses the False Claims Act (FCA) to pursue government contractors and grant recipients that knowingly misrepresent cybersecurity practices or fail to timely report cyber incidents. In 2025, major settlements included:

- **Illumina** ($9.8M) — selling DNA sequencers with cybersecurity vulnerabilities to federal agencies, allegedly misrepresenting compliance with ISO and NIST standards.
- **Raytheon/Nightwing** ($8.5M) — successor liability for pre-acquisition cybersecurity failures.
- **MORSE Corp** ($4.6M) — failure to implement required NIST SP 800-171 controls.

[Mintz 2026 FCA Update](https://www.mintz.com/insights-center/viewpoints/2406/2026-01-13-cybersecurity-related-enforcement-under-false-claims-act)

---

## 2. Enforcement Actions Highlighting Disclosure Shortcomings

### 2.1 SEC Enforcement Actions

**Blackbaud Inc. (2023) — $3 Million Penalty**  
Blackbaud disclosed a ransomware attack in July 2020, initially claiming that no donor bank account information or social security numbers were accessed. Within days, the company’s technology and customer relations personnel learned these claims were false, yet the company filed a quarterly report that omitted material information and characterized the risk of exfiltration as hypothetical. The SEC charged violations of antifraud provisions, reporting provisions, and disclosure controls.  
[SEC Charge Against Blackbaud](https://www.hunton.com/privacy-and-cybersecurity-law-blog/sec-brings-cyber-disclosure-enforcement-action)

**Unisys, Avaya, Check Point, Mimecast (2024) — Total $7 Million in Penalties**  
The SEC charged four companies with making materially misleading disclosures about cybersecurity intrusions linked to the SolarWinds Orion compromise. Key findings:

- **Unisys** ($4M) — described risks as hypothetical while knowing it had experienced two intrusions with data exfiltration; also charged with deficient disclosure controls.
- **Avaya** ($1M) — stated the threat actor accessed a “limited number of email messages” while knowing it had accessed at least 145 files in a cloud file-sharing environment.
- **Check Point** ($995K) — used generic language about cyber intrusions despite specific knowledge.
- **Mimecast** ($990K) — failed to disclose the nature of exfiltrated code and the quantity of encrypted credentials accessed.

The SEC’s Acting Director of Enforcement stated: “While public companies may become targets of cyberattacks, it is incumbent upon them to not further victimize their shareholders … by providing misleading disclosures.”  
[SEC Press Release 2024-174](https://www.sec.gov/newsroom/press-releases/2024-174)

**First American Financial Corporation (2021) — $487,616 Penalty**  
The SEC’s **first-ever** penalty for deficient cybersecurity disclosure controls. FAFC’s information security personnel knew of a vulnerability exposing 800+ million documents months before a journalist disclosed it, but failed to escalate the issue to senior executives. The SEC found that FAFC had “no disclosure controls and procedures related to cybersecurity.”  
[Holland & Knight Summary](https://www.hklaw.com/en/insights/publications/2021/06/sec-issues-first-ever-penalties-for-deficient-cybersecurity-risk)

**SolarWinds Corp. and CISO Timothy Brown (2023–2025)**  
The SEC filed charges in October 2023 alleging fraud and internal control failures — the first time the SEC charged a CISO as an individual in a cybersecurity disclosure case. The complaint alleged that SolarWinds made misleading claims about following the NIST framework, maintained generic risk disclosures while ignoring specific known risks, and filed a misleading 8-K about the SUNBURST breach. The case was voluntarily dismissed with prejudice in November 2025, but the SEC stated the dismissal “does not necessarily reflect the Commission’s position on any other case,” signaling continued enforcement intent.  
[SEC Press Release 2023-227](https://www.sec.gov/newsroom/press-releases/2023-227) | [White & Case Analysis](https://www.whitecase.com/insight-alert/secs-charges-against-solarwinds-and-its-chief-information-security-officer-provide)

### 2.2 Healthcare Sector Enforcement

**Change Healthcare Ransomware Attack (2024)**  
The attack on the largest U.S. medical clearinghouse resulted in a reported $22 million ransom payment, disruption of 15 billion annual transactions, and an estimated $100 million per day in deferred revenue for providers. HHS OCR opened a HIPAA compliance investigation. The breach ultimately affected 192.7 million individuals. The attack was attributed to a lack of multi-factor authentication on a legacy Citrix portal.  
[JAMA Health Forum Analysis](https://jamanetwork.com/journals/jama-health-forum/fullarticle/2823757) | [HHS FAQ on Change Healthcare](https://www.hhs.gov/hipaa/for-professionals/special-topics/change-healthcare-cybersecurity-incident-frequently-asked-questions/index.html)

**OCR HIPAA Settlement**  
A benefit plan that experienced a ransomware attack settled with OCR for $245,000 and a two-year corrective action plan after failing to complete a thorough security risk assessment.  
[Kean Miller Summary](https://www.keanmiller.com/insights/blog/louisiana-law-blog/hhs-ocr-ransomware-attacks-usually-qualify-as-a-hipaa-breach)

### 2.3 OFAC / Sanctions Enforcement

While OFAC has not publicly announced a civil penalty specifically for a ransomware payment to a sanctioned entity, the designation of SUEX OTC in 2021 and the Updated Advisory’s strict liability language serve as a warning. OFAC’s enforcement guidelines emphasize that the existence, nature, and adequacy of a sanctions compliance program is a key mitigating factor. Failure to screen ransomware payment recipients against the SDN list before payment could result in significant penalties.

---

## 3. Lessons for Enterprises on Disclosure Strategy

### 3.1 Build Integrated Regulatory Calendars

The overlapping timelines across regulators create a coordination challenge that must be addressed pre-incident:

| Regulator | Trigger | Timeline |
|-----------|---------|----------|
| SEC (Form 8-K) | Materiality determination | 4 business days |
| NYDFS | Any cybersecurity event | 72 hours |
| NYDFS | Ransom payment | 24 hours + 30-day written justification |
| CISA (CIRCIA, when final) | Covered cyber incident | 72 hours |
| CISA (CIRCIA, when final) | Ransom payment | 24 hours |
| HIPAA/HHS | Breach of PHI affecting 500+ | 60 days (with media notification) |
| OFAC | Sanctions screening | Pre-payment due diligence |

**Lesson:** A single incident response playbook must incorporate all applicable notification timelines. The ransomware payment decision is particularly time-sensitive: OFAC screening must occur before payment, while NYDFS requires notification within 24 hours of payment and CIRCIA (when final) will also require 24-hour notification.

### 3.2 Materiality Determinations: Speed vs. Accuracy

The SEC requires materiality determinations “without unreasonable delay” after discovery. The SEC’s C&DIs clarify that even if a ransomware payment ends the incident before the determination is made, the company must still assess materiality. Enterprises should:

- **Establish a pre-defined materiality assessment team** (legal, finance, cybersecurity, operations, investor relations) that can convene within hours.
- **Document the rationale** for materiality determinations, including quantitative and qualitative factors considered.
- **Aggregate related incidents** — a single threat actor exploiting the same vulnerability across multiple attacks may be collectively material even if each incident individually is not.
- **Do not rely on insurance reimbursement** as a sole factor for immateriality.

### 3.3 Avoid “Hypothetical” Risk Language When Risk Has Materialized

The Unisys, Avaya, Check Point, and Mimecast cases demonstrate that describing risks as “hypothetical” or “generic” when the company knows the risk has already materialized is a violation of antifraud provisions. The SEC’s Crypto Assets and Cyber Unit Acting Chief stated: “The federal securities laws prohibit half-truths, and there is no exception for statements in risk-factor disclosures.”

**Lesson:** Risk factor disclosures in annual reports must be updated promptly when known risks materialize. A company cannot simultaneously disclose a material incident under Item 1.05 while maintaining stale risk-factor language that treats the incident category as hypothetical.

### 3.4 Disclosure Controls Are a First Line of Defense

The FAFC action established that the SEC will enforce Rule 13a-15(a) — requiring disclosure controls and procedures — even in the absence of a finding that the final disclosure was materially misleading. The SEC’s theory is that if information does not flow up to senior executives responsible for disclosure, the controls are deficient regardless of the outcome.

**Lesson:** Enterprises must implement and document:

- **Escalation protocols** that ensure cybersecurity incidents and vulnerabilities are reported to the disclosure committee.
- **Cross-functional integration** between the CISO, legal, finance, and the CEO/CFO.
- **Regular testing** of disclosure controls, including tabletop exercises that simulate ransomware incidents.
- **Sub-certifications** from the CISO to senior executives regarding the completeness of incident reporting.

### 3.5 Ransomware Payment Decision Frameworks

Given the sanctions risks, disclosure obligations, and business pressures, enterprises should establish a pre-defined decision framework for ransomware payments:

1. **Sanctions screening:** Immediately check the threat actor and any demanded payment addresses against the OFAC SDN List and any other applicable sanctions lists. Contact OFAC if there is any sanctions nexus.
2. **Law enforcement engagement:** Promptly report to CISA, FBI, and/or Secret Service. This is a significant mitigating factor for OFAC enforcement.
3. **Insurance coordination:** Review cyber insurance policy for ransom coverage, sub-limits, and pre-approved vendors. Note that insurance reimbursement does not eliminate SEC disclosure obligations.
4. **Regulatory notification:** Determine which regulatory bodies require notification and on what timeline (SEC, NYDFS, CISA, OCR, state breach notification laws).
5. **Public disclosure:** Prepare holding statements and draft 8-K language concurrently with the materiality determination.

### 3.6 Healthcare-Specific Considerations

The Change Healthcare attack demonstrated the cascading impact of a ransomware incident on third parties. Key lessons for healthcare entities:

- **Assume ransomware on ePHI is a breach.** HHS guidance presumes a breach when ePHI is encrypted. The burden is on the entity to demonstrate low probability of compromise.
- **Conduct the four-factor risk assessment** promptly and document it thoroughly.
- **Third-party risk management:** Ensure that business associate agreements include clear incident notification obligations and that the entity has contingency plans for clearinghouse outages.
- **Prepare for OCR investigation.** The Change Healthcare incident triggered an immediate OCR investigation; entities should maintain readiness for post-incident regulatory review.

### 3.7 Government Contractor / FCA Exposure

The DOJ’s Civil Cyber-Fraud Initiative continues to expand. Entities that receive federal funds or contract with the government must:

- Ensure compliance with NIST SP 800-171, DFARS, and FedRAMP requirements as applicable.
- Promptly self-disclose cybersecurity failures; DOJ treats self-disclosure as a significant mitigating factor.
- Conduct thorough due diligence in acquisitions to avoid successor liability for pre-acquisition cybersecurity failures (as in the Raytheon/Nightwing case).

### 3.8 The “No Harm, No Foul” Fallacy

Multiple enforcement actions demonstrate that the SEC and DOJ will pursue enforcement even in the absence of evidence that a breach caused financial harm to investors. The SEC’s theory is that misleading disclosures — even without proven investor harm — violate the securities laws. Similarly, the DOJ’s FCA theory does not require an actual data breach; misrepresentations about cybersecurity practices alone can be sufficient.

---

## 4. Strategic Recommendations

1. **Create a unified incident disclosure matrix** that maps each regulatory obligation (SEC, NYDFS, HIPAA, CISA, OFAC, state breach notification) to the specific incident type, trigger, timeline, and reporting content.

2. **Pre-position ransomware payment decision-making** by establishing a cross-functional team, pre-negotiating with incident response firms, and conducting OFAC screening training.

3. **Audit disclosure controls and procedures** for cybersecurity incidents, ensuring that vulnerability information and security alerts are escalated to senior management and the disclosure committee without unreasonable delay.

4. **Update risk-factor disclosures dynamically** — when a known risk materializes, the risk-factor language must be updated to reflect that the risk is no longer hypothetical.

5. **Conduct tabletop exercises** that simulate the full disclosure timeline (SEC 4-day, NYDFS 24-hour, CIRCIA 24-hour) to test the organization’s ability to meet multiple deadlines simultaneously.

6. **Document all materiality determinations** with a written rationale that explicitly addresses the factors in the SEC’s C&DIs (quantitative and qualitative impact, insurance, ransom amount, aggregation of related incidents).

7. **Engage legal counsel** with expertise in cybersecurity disclosure, sanctions, and healthcare regulatory compliance before an incident occurs.

---

## References

1. SEC, “SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure by Public Companies,” July 26, 2023.  
   https://www.sec.gov/newsroom/press-releases/2023-139

2. SEC Division of Corporation Finance, Compliance & Disclosure Interpretations, Item 1.05 (June 24, 2024).  
   https://www.sec.gov/divisions/corpfin/guidance/8-kinterp.htm

3. SEC, “SEC Charges Four Companies With Misleading Cyber Disclosures,” Oct. 22, 2024.  
   https://www.sec.gov/newsroom/press-releases/2024-174

4. SEC, “SEC Charges SolarWinds and Chief Information Security Officer with Fraud, Internal Control Failures,” Oct. 30, 2023.  
   https://www.sec.gov/newsroom/press-releases/2023-227

5. SEC, “SolarWinds Corp. and Timothy G. Brown — Litigation Release No. 26423,” Nov. 20, 2025.  
   https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26423

6. SEC, “Statement on Cybersecurity Disclosure,” Erik Gerding, Dec. 14, 2023.  
   https://www.sec.gov/newsroom/speeches-statements/gerding-cybersecurity-disclosure-20231214

7. Mintz, “SEC Issues Updated Guidance on Cybersecurity Incident Disclosure Under Item 1.05 of Form 8-K,” July 11, 2024.  
   https://www.mintz.com/insights-center/viewpoints/2901/2024-07-11-sec-issues-updated-guidance-cybersecurity-incident

8. Hunton, “OFAC’s Updated Advisory on Ransomware Payments,” Sept. 2021.  
   https://www.hunton.com/insights/legal/ofacs-updated-advisory-on-ransomware-payments

9. OFAC, “Ransomware Advisory,” Oct. 1, 2020.  
   https://ofac.treasury.gov/recent-actions/20201001

10. CISA, “Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA).”  
    https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia

11. IBM, “Important details about CIRCIA ransomware reporting.”  
    https://www.ibm.com/think/insights/circia-ransomware-reporting-important-details

12. HHS, “Fact Sheet: Ransomware and HIPAA,” July 11, 2016.  
    https://www.hhs.gov/hipaa/for-professionals/security/guidance/cybersecurity/ransomware-fact-sheet/index.html

13. HHS, “Change Healthcare Cybersecurity Incident Frequently Asked Questions.”  
    https://www.hhs.gov/hipaa/for-professionals/special-topics/change-healthcare-cybersecurity-incident-frequently-asked-questions/index.html

14. NYDFS, “Ransomware Guidance for All New York State Regulated Entities,” June 30, 2021.  
    https://www.dfs.ny.gov/industry_guidance/industry_letters/il20210630_ransomware_guidance

15. ACA Global, “New York DFS’ Expanded Cybersecurity Regulations,” Nov. 6, 2023.  
    https://www.acaglobal.com/industry-insights/new-york-state-department-financial-services-expands-cybersecurity-rules

16. Holland & Knight, “SEC Issues First-Ever Penalties for Deficient Cybersecurity Risk Controls,” June 2021.  
    https://www.hklaw.com/en/insights/publications/2021/06/sec-issues-first-ever-penalties-for-deficient-cybersecurity-risk

17. Hunton, “SEC Brings Cyber Disclosure Enforcement Action — Blackbaud,” March 2023.  
    https://www.hunton.com/privacy-and-cybersecurity-law-blog/sec-brings-cyber-disclosure-enforcement-action

18. White & Case, “The SEC’s Charges Against SolarWinds and its Chief Information Security Officer,” Oct. 2023.  
    https://www.whitecase.com/insight-alert/secs-charges-against-solarwinds-and-its-chief-information-security-officer-provide

19. Mintz, “Cybersecurity-Related Enforcement Under the False Claims Act in 2025,” Jan. 2026.  
    https://www.mintz.com/insights-center/viewpoints/2406/2026-01-13-cybersecurity-related-enforcement-under-false-claims-act

20. JAMA Health Forum, “Lessons From the Change Healthcare Ransomware Attack,” 2024.  
    https://jamanetwork.com/journals/jama-health-forum/fullarticle/2823757

21. Kean Miller, “HHS OCR: Ransomware Attacks Usually Qualify as a HIPAA Breach.”  
    https://www.keanmiller.com/insights/blog/louisiana-law-blog/hhs-ocr-ransomware-attacks-usually-qualify-as-a-hipaa-breach

22. Morgan Lewis, “SEC Releases Interpretations on Ransomware Attacks and Payment Disclosures,” July 2024.  
    https://www.morganlewis.com/pubs/2024/07/sec-releases-interpretations-on-ransomware-attacks-and-payment-disclosures

23. MoFo, “U.S. SEC Issues Updated Guidance on Cybersecurity Disclosure,” June 2024.  
    https://www.mofo.com/resources/insights/240625-u-s-sec-issues-updated-guidance-on-cybersecurity-disclosure

24. Alston & Bird, “SEC Settles Enforcement Action for Disclosure Controls Violations Stemming from Data Security Incident” (FAFC).  
    https://www.alstonprivacy.com/sec-settles-enforcement-action-for-disclosure-controls-violations-stemming-from-data-security-incident

25. Cleary Gottlieb, “Cybersecurity Disclosure and Enforcement Developments and Predictions,” 2025.  
    https://www.clearygottlieb.com/news-and-insights/publication-listing/cybersecurity-disclosure-and-enforcement-developments-and-predictions

---

*This report is prepared for internal risk analysis purposes. It does not constitute legal advice. Organizations should consult with qualified legal counsel on specific disclosure obligations.*
