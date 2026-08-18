

# Cloud Provider Comparison Report: AWS vs. Google Cloud vs. Microsoft Azure vs. Oracle Cloud (2026)

**Date of analysis: August 2026** — All pricing data reflects US regions (primarily US East/N. Virginia/us-east-1) unless otherwise noted. Prices are list/on-demand rates and can change; verify against official provider pricing pages before making procurement decisions.

---

## 1. Pricing (US Regions — Compute & Storage)

### 1.1 Compute (On-Demand, General Purpose, US East)

All four providers bill per-second for Linux compute (with a 60-second minimum on AWS and Azure; Google bills per-second with a 1-minute minimum). OCI uses an OCPU (physical core) model with flexible VM shapes.

| Provider | Representative Instance (2 vCPU / 8 GB) | On-Demand Monthly (US East) | 1-Year Reserved/Committed | Spot/Preemptible |
|---|---|---|---|---|
| **AWS** | `m5.large` / `t3.medium` | ~$70/mo (`m5.large` ~$0.096/hr) | ~$18/mo (1-yr, `t3.medium`) | ~$9/mo (Spot) |
| **Azure** | `D2s_v3` / `B2s` | ~$70/mo (`D2s_v3`) | ~$17/mo (1-yr, `B2s`) | ~$3/mo (Spot) |
| **GCP** | `e2-standard-2` / `e2-medium` | ~$49–65/mo (`e2-standard-2`) | ~$15/mo (1-yr, `e2-medium`); up to 57–70% CUD | ~$6/mo (Preemptible) |
| **OCI** | `VM.Standard` (AMD, 4 vCPU/16 GB) | ~$54/mo (4 vCPU/16 GB) | ~40% lower with Universal Credit discount | Flat 50% discount (Preemptible) |

Key notes:

- **AWS** reference rates (us-east-1, Linux, On-Demand, June 2026): `t3.micro` $0.0104/hr (~$7.59/mo), `m5.large` $0.096/hr (~$70/mo), `t4g.nano` $0.0042/hr. Savings Plans/Reserved Instances reduce rates ~35–72%.
- **Azure** `D2s_v3` ~$70.08/mo; Azure offers the largest discounts on general and compute-optimized instances among the big three, plus Azure Hybrid Benefit for customers with existing Microsoft licenses.
- **GCP** auto-applies sustained-use discounts (20–30%) and offers committed use discounts up to 57% (1-year) and 70% (3-year, memory-optimized). GCP is often the cheapest of the big three for on-demand general compute before egress.
- **OCI** advertises roughly **50% lower compute** than AWS/Azure equivalents. A 4 vCPU/16 GB AMD VM is ~$54/mo vs. ~2.3x that on AWS/Azure. OCI also offers flexible VM shapes (choose exact OCPU/RAM), and preemptible VMs at a flat 50% discount.
- **GPU compute (2026):** OCI lists NVIDIA H100 at ~$5.12/GPU-hr vs. ~$12.29/GPU-hr on AWS — a ~58% cost advantage claimed by Oracle.

### 1.2 Object Storage (Standard Tier, US)

| Provider | Service | Standard $/GB/mo | Cold/Infrequent $/GB/mo | Archive $/GB/mo |
|---|---|---|---|---|
| **AWS** | S3 Standard | $0.023 (first 50 TB) | S3 Standard-IA: $0.0125 | Glacier Deep Archive: $0.00099 |
| **Azure** | Blob Hot (LRS) | $0.018 | Cool: $0.01 | Archive: $0.002 |
| **GCP** | Cloud Storage Standard (regional) | $0.020 | Nearline: $0.010 | Archive: $0.0012 (regional) / $0.0024 (multi-region) |
| **OCI** | Object Storage Standard | $0.0255 | Infrequent Access: $0.015 | Archive: $0.0026 |

Key notes:

- **Azure** is consistently the cheapest for standard object storage among the big three at $0.018/GB/mo (LRS, US East).
- **AWS S3** is the most expensive standard tier at $0.023/GB/mo, but offers the deepest archive tier (Glacier Deep Archive at $0.00099/GB/mo).
- **GCP** reduced Archive multi-region pricing in 2026 from $0.004 to $0.0024/GB/mo, while raising Nearline multi-region to $0.015/GB/mo.
- **OCI Object Storage** is priced at $0.0255/GB/mo standard — higher than Azure/GCP for the base tier, but OCI's **block storage** is dramatically cheaper (see below).

### 1.3 Block Storage (Premium/SSD, US)

| Provider | Service | $/GB/mo | Notes |
|---|---|---|---|
| **AWS** | EBS gp3 | $0.08 | IOPS/throughput billed separately above baseline |
| **Azure** | Premium SSD v2 | $0.113 (base) | IOPS/throughput provisioned separately |
| **GCP** | Persistent Disk SSD | $0.17 | Premium tier, US regions |
| **OCI** | Block Storage | $0.0255 | Oracle claims ~5x cheaper than AWS/Azure for comparable performance |

Oracle's Cloud Economics page highlights that for 1,000 GB of block storage, OCI costs ~$43 vs. AWS $195, Azure $200, GCP $187 — a 4–5x difference. For high-IOPS workloads (e.g., 1 TB at 75K IOPS), OCI lists $60/mo vs. AWS $4,000, Azure $460, GCP $540.

### 1.4 Data Egress (First 10 TB, US)

| Provider | Egress $/GB | Free Tier |
|---|---|---|
| **AWS** | $0.09/GB (first 10 TB) | 100 GB/mo |
| **Azure** | $0.087/GB (Premium); $0.04/GB (ISP routing) | 100 GB/mo |
| **GCP** | $0.12/GB (premium tier) | 100 GB/mo (some services free egress, e.g., Cloud Run) |
| **OCI** | $0.0085/GB (after 10 TB) | **10 TB/mo free** |

OCI's egress pricing is the standout differentiator — after 10 TB free, it charges ~$0.0085/GB, roughly **10x cheaper than AWS/Azure** and ~14x cheaper than GCP. AWS charges $0.09/GB for the first 10 TB; GCP is the most expensive at $0.12/GB.

### 1.5 Pricing Summary Table

| Dimension | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| General compute (2 vCPU/8 GB) | ~$70/mo | ~$70/mo | ~$49–65/mo | ~$54/mo (4 vCPU/16 GB) |
| Object storage (standard) | $0.023/GB | **$0.018/GB** | $0.020/GB | $0.0255/GB |
| Block storage (SSD) | $0.08/GB | $0.113/GB | $0.17/GB | **$0.0255/GB** |
| Egress (first 10 TB) | $0.09/GB | $0.087/GB | $0.12/GB | **$0.0085/GB** (10 TB free) |
| Discount mechanisms | Savings Plans, RI (up to 72%) | Reserved (up to ~72%), Hybrid Benefit | Sustained Use (20–30%), CUD (up to 70%) | UC discounts, flat 50% preemptible |
| Overall cost position | Most expensive for storage/egress | Cheapest big-3 object storage | Cheapest big-3 compute | Cheapest compute/block/egress, pricier object storage |

---

## 2. Machine Learning & AI Services

### 2.1 AWS (Amazon Bedrock + SageMaker AI)

- **Amazon Bedrock** is the serverless, API-first generative AI service for accessing frontier and open models (Anthropic Claude, Meta Llama, Mistral, Amazon Nova, Cohere, etc.) without managing infrastructure. Key 2026 capabilities include: Knowledge Bases (RAG), Guardrails, **AgentCore** (build/deploy/operate AI agents), Flows, Data Automation, and Prompt Management.
- **Amazon SageMaker AI** is the full-lifecycle ML platform for building, training, and deploying custom models. Supports predictive ML, classical ML, and generative AI; includes JumpStart model hub (~1,000 models), serverless customization (SFT, DPO, RLVR, RLAIF), HyperPod for large-scale training, and purpose-built silicon (**Trainium/Inferentia**) for lower-cost inference.
- **Purpose-built AI services:** Textract (documents), Comprehend (NLP), Polly (TTS), Translate, Lex (chatbots), Personalize (recommendations), Forecast, Rekognition (vision), Kendra (search).
- **Differentiator:** Broadest portfolio of AI services and deepest integration with enterprise data services; strongest position for custom training at scale with custom silicon.

### 2.2 Google Cloud (Gemini Enterprise Agent Platform, formerly Vertex AI)

- **Major 2026 change:** At Google Cloud Next 2026 (April), **Vertex AI was rebranded and expanded into the Gemini Enterprise Agent Platform**. The console now redirects to the Agent Platform; all Vertex AI features (Model Garden, AutoML, Custom Training, Pipelines, Model Registry, Endpoints) are subsumed under it.
- **Gemini models:** Gemini 3.1 Pro (preview, 1M token context), Gemini 2.5 series (retiring Oct 2026), Veo 3.1 Lite (video), Imagen (image), plus open models via Model Garden (Llama, DeepSeek, Mistral, Qwen) and partners (Claude Sonnet 4.6 available).
- **Agent Platform components:** Agent Garden (pre-built agents), Agent Studio, Agent Engine, RAG Engine, Vector Search, Memory Bank, Sessions, plus **Model Garden** with 200+ models.
- **Infrastructure:** Google TPUs (v5e/v6e) alongside GPUs (H100, A100, L4); deep integration with BigQuery for data analytics; Gemini Enterprise app for employees.
- **Differentiator:** Best-in-class generative AI (Gemini), TPU infrastructure, and native data/Analytics integration (BigQuery).

### 2.3 Microsoft Azure (Microsoft Foundry + Azure OpenAI + Azure ML)

- **Microsoft Foundry** is now the central AI platform, pulling together what was previously separate: **Azure OpenAI Service** is now "Foundry Models sold by Azure," and the model catalog has expanded to **11,000+ models** spanning OpenAI (GPT-5.2 now available), Anthropic, Meta, Google, xAI, DeepSeek, and Hugging Face, plus Microsoft's own MAI family.
- **Azure Machine Learning** remains the full MLOps platform for training, deploying, and managing custom models; includes model catalog, prompt flow, responsible AI tools, managed online/batch endpoints, and ONNX Runtime.
- **Azure AI Services** (prebuilt): Azure AI Search, Document Intelligence, Speech, Vision, Language, Translator, plus Azure AI Bot Service.
- **Differentiator:** Strongest OpenAI/enterprise productivity integration (Microsoft 365, Copilot, Fabric), the largest model catalog (11,000+), and enterprise-grade governance/responsible AI tooling.

### 2.4 Oracle Cloud (OCI Enterprise AI + OCI AI Services)

- **OCI Enterprise AI** (GA in 2026): End-to-end platform for building, deploying, and governing production AI applications and agents. Combines managed access to leading models (with zero-data-retention endpoints), agent development/orchestration, built-in security, observability, and governance. Offers sovereign AI options.
- **OCI Generative AI:** Fully managed service with Cohere LLMs (Command models), fine-tuning on dedicated AI clusters, RAG via Generative AI Agents, and integration via API/CLI/console.
- **OCI AI Services:** Language (sentiment, entity recognition, translation), Speech (STT/TTS), Vision (object detection, classification, OCR), Document Understanding, and Digital Assistant (chatbots).
- **OCI Data Science:** Managed Jupyter notebooks supporting open-source frameworks, LangChain, and vector databases for RAG workflows; in-database ML in Oracle Autonomous Database.
- **AI Infrastructure:** OCI offers NVIDIA GPUs (H100, A100, L40S, GB200) at aggressive price points; Oracle claims ~58% cost advantage on H100 clusters vs. AWS.
- **Differentiator:** Deep integration with Oracle Database/Applications (Fusion, EBS), sovereign AI options, and aggressive GPU pricing. Smaller third-party model ecosystem and less mature MLOps tooling than the big three.

### 2.5 AI/ML Summary Table

| Dimension | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| Primary GenAI platform | Amazon Bedrock | Microsoft Foundry (incl. Azure OpenAI) | Gemini Enterprise Agent Platform (ex-Vertex AI) | OCI Enterprise AI |
| ML platform | SageMaker AI | Azure Machine Learning | Agent Platform (ex-Vertex AI) | OCI Data Science |
| Model catalog | ~1,000 (JumpStart); Bedrock multi-provider | 11,000+ models | 200+ (Model Garden) | Cohere + select open models |
| Flagship models | Amazon Nova, Claude, Llama, Mistral | GPT-5.2, MAI, Claude, Llama, DeepSeek | Gemini 3.1 Pro, Gemma, Veo, Imagen | Cohere Command, open models |
| Custom silicon | Trainium, Inferentia | Maia (in development) | TPU v5e/v6e | NVIDIA-only (no custom silicon) |
| Key differentiator | Broadest service portfolio | Largest model catalog, OpenAI/Office integration | Gemini models, TPUs, BigQuery integration | GPU price/performance, DB integration |

---

## 3. Enterprise Support, SLAs & Support Experience

### 3.1 AWS Support Plans (2026)

- **Basic** (free, included): Docs, forums, Trusted Advisor (limited).
- **Business Support+** ($29/mo min, or 9% of charges up to $10K): 24/7 access, AI-powered assistance, response times: General <24h, System impaired <12h, Production impaired <4h, Production down <1h, Business-critical down <30 min.
- **Enterprise Support** ($5,000/mo min, or 10% of charges up to $150K): Dedicated Technical Account Manager (TAM), 15-min response for business-critical down, Trusted Advisor Priority (465+ checks), AWS Security Incident Response included, architecture reviews, Well-Architected reviews.
- **Unified Operations** ($50,000/mo min, or 10% up to $1M): Highest tier; includes AWS Incident Detection and Response (5-min response), Countdown Premium, DevOps Agent, 24x7 proactive engagement.
- **Notable 2026 change:** AWS is discontinuing Developer, Business, and Enterprise On-Ramp plans effective **January 1, 2027**, consolidating into Business Support+, Enterprise Support, and Unified Operations.
- **SLAs:** AWS offers 99.9%–99.99% availability SLAs per service (EC2 99.99% with multi-AZ; S3 99.9%; RDS 99.95% Multi-AZ). Service credits apply for breaches.

### 3.2 Google Cloud Support Plans (2026)

- **Basic** (free): Docs, community forums, no SLA.
- **Standard** (~$150/mo or 3% of spend): Business-hours support, 4-hour response for high-priority issues, no 24/7.
- **Enhanced** (~$500/mo or 3% of spend): 24/7 support, 1-hour P1 response, architecture reviews.
- **Premium** ($15,000/mo min, or tiered % of spend): Dedicated Technical Account Manager (TAM), 15-min P1 response, 2-hr P2, 4-hr P3, 8-hr P4; Customer Aware Support; access to Assured Support and Mission Critical Services; P0 case filing with 5-minute response; 24/7 support in English, Japanese, Mandarin, Korean, French.
- **SLAs:** GCP generally offers 99.9%–99.99% per-service SLAs (Compute Engine 99.99% multi-zone; Cloud Storage 99.9% regional, 99.99% multi-region; BigQuery 99.99%).
- **Experience note:** Google's Premium Support is widely regarded as strong for enterprise, with dedicated TAMs and fast P1 response, but the $15K/mo minimum is higher than AWS's $5K Enterprise minimum.

### 3.3 Microsoft Azure Support Plans (2026)

- **Basic** (included, free): Docs, community, limited self-help.
- **Developer** ($29/mo): Business-hours support; Sev C <8 business hours.
- **Standard** ($100/mo): 24/7 Sev A support; Sev C <8 business hours, Sev B <4 hours, Sev A <1 hour.
- **ProDirect** ($1,000/mo): Sev C <4 business hours, Sev B <2 hours, Sev A <1 hour; named support engineer; architecture guidance.
- **Unified Enterprise** (custom pricing, typically $15K+/mo): Sev C <4 business hours, Sev B <2 hours, Sev A <1 hour; **Azure Rapid Response: Sev A <15 min**; Unified Enhanced Response: <30 min; catastrophic Sev 1: <15 min. Includes FastTrack, proactive services, and a dedicated Delivery Manager.
- **SLAs:** Azure publishes service-specific SLAs (e.g., Virtual Machines 99.9% single instance, 99.95% availability set, 99.99% zone-redundant; Blob Storage 99.9%; SQL Database 99.99% for zone-redundant). The SLA document (January 1, 2026 edition) specifies service credits: <99.9% → 10%, <99% → 25%, <95% → 100% depending on service.
- **Experience note:** Azure's Unified Enterprise is the most expensive among the big three but includes the fastest catastrophic-response SLA (15 min) and deep Microsoft ecosystem integration.

### 3.4 Oracle Cloud Support (2026)

- **Key differentiator:** OCI **includes enterprise-grade support at no extra charge** with its base service fees. Oracle explicitly markets: "There is no extra charge for technical support of production workloads using OCI. This is in stark contrast to other providers, who can charge 3% to 10% of the prior month."
- Oracle provides 24/7 access to a global team of 18,000+ support specialists in 20+ languages across 175 countries.
- **Oracle Support Rewards:** Customers earn $0.25–$0.33 in rewards for every $1 spent on OCI, which can be applied to reduce on-premises Oracle technical support fees (potentially to zero).
- **Premier Support for Software:** Applies to on-premises Oracle products; offers 24/7 technical support, priority service-request handling, and 2-hour onsite hardware service for systems. Support costs ~22% of net license value annually (for licensed software, not OCI).
- **OCI SLAs:** Oracle offers 99.95% availability SLA for compute (with certain configurations), 99.9% for object storage, and 99.95% for Autonomous Database. Oracle also advertises **no egress fees within OCI** and inter-region transfers at flat low rates.
- **Experience note:** Oracle's OCI support model is fundamentally different — support is bundled, not a separate line-item. This can reduce total cost, but enterprise customers report that OCI's account management and ecosystem maturity trail the big three. The support experience varies significantly; Oracle is often perceived as more aggressive in commercial negotiations.

### 3.5 Enterprise Support Summary Table

| Dimension | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| Entry paid plan | Business Support+ $29/mo | Developer $29/mo | Standard ~$150/mo | Included with OCI usage |
| Top enterprise tier | Enterprise $5K/mo min; Unified Ops $50K/mo | Unified Enterprise (custom, ~$15K+/mo) | Premium $15K/mo min | No separate enterprise tier (bundled) |
| Fastest P1/Sev A response | 15 min (Enterprise/Unified) | 15 min (Azure Rapid Response, Unified) | 15 min (Premium) | 24/7 via included support; no published 15-min tier |
| Dedicated TAM | Yes (Enterprise/Unified) | Yes (ProDirect/Unified) | Yes (Premium) | Account team; varies |
| Support cost model | % of spend (up to 10%) | Flat + % for higher tiers | Tiered % of spend | Bundled in usage |
| SLA typical compute | 99.99% (multi-AZ) | 99.95–99.99% | 99.99% (multi-zone) | 99.95% |
| Unique feature | Trusted Advisor, DevOps Agent, Incident Detection | Azure Rapid Response, FastTrack | Assured Support, Mission Critical Services | Support Rewards, zero-cost bundled support |

---

## 4. Infrastructure & Availability

### 4.1 AWS

- **Regions:** 39 geographic regions worldwide (including GovCloud and the new AWS European Sovereign Cloud, which opened its first region in Brandenburg, Germany in January 2026).
- **Availability Zones:** 123 AZs, with 7 more AZs and 2 new regions (Saudi Arabia, Chile) announced.
- **Edge locations:** 700+ CloudFront Points of Presence, 43 Local Zones, 245+ countries/territories served.
- **US presence:** 9 regions in North America (N. Virginia, Ohio, Oregon, N. California, Canada Central, Canada West/Calgary, Mexico Central, GovCloud East/West), with a new AZ in Maryland (N. Virginia) opening in 2026 to support AI workloads.
- **Scale:** 900+ data centers globally (industry estimates); the largest cloud infrastructure footprint of any provider.

### 4.2 Google Cloud

- **Regions:** 43 global regions (as of July 2026, per official Google Cloud locations page).
- **Zones:** 130 zones.
- **Edge locations:** 200+ network edge locations.
- **US regions:** us-central1 (Iowa), us-east1 (S. Carolina), us-east4 (N. Virginia), us-east5 (Columbus), us-west1 (Oregon), us-west2 (LA), us-west3 (Salt Lake City), us-west4 (Las Vegas), us-south1 (Dallas).
- **Expansion:** New regions planned in Mexico, Malaysia, Thailand, New Zealand, Greece, Norway, Austria, Sweden, and Kuwait.

### 4.3 Microsoft Azure

- **Regions:** 70+ announced regions (more than any other cloud provider per Microsoft); ~60+ live/GA regions.
- **Availability Zones:** 35+ regions currently support AZs; Microsoft announced in 2026 it is adding AZs to East US 2 (Virginia) and South Central US (Texas), plus 3 AZs for Azure Government Arizona.
- **Edge locations:** 190+ edge POPs in 190+ countries (via Azure CDN/Front Door).
- **US presence:** Strongest US public-sector footprint with dedicated government regions (Azure Government in Virginia, Arizona, Texas, and DoD regions).
- **Unique model:** Region pairs for geo-replication and disaster recovery sequencing.

### 4.4 Oracle Cloud Infrastructure (OCI)

- **Regions:** 50+ public cloud regions worldwide (Oracle claims 50+; the official price list references 50+ regions with uniform pricing).
- **Availability Domains (ADs):** OCI uses "Availability Domains" — the first four regions (Ashburn, Phoenix, Frankfurt, London) have 3 ADs; newer regions typically have 1 AD but use fault domains (FDs) for high availability.
- **Edge/Alloy/Dedicated:** OCI offers distributed cloud options — Oracle Alloy, Compute Cloud@Customer, and dedicated regions — enabling sovereign/hybrid deployments. Oracle also has interconnects with Azure (Oracle Database@Azure) and AWS (Oracle Database@AWS, available in 12 AWS regions as of April 2026).
- **US presence:** US East (Ashburn), US West (Phoenix, San Jose, Boardman), US Central (Chicago, Columbus), Canada (Toronto, Montreal), plus GovCloud equivalents.
- **Uniform pricing:** Oracle advertises uniform pricing across all 50+ regions (no regional premium), a differentiator versus AWS/Azure/GCP, which vary pricing by region.

### 4.5 Infrastructure Summary Table

| Dimension | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| Regions | 39 (incl. sovereign/EU) | 70+ announced (~60+ live) | 43 | 50+ |
| Availability Zones / Domains | 123 AZs | 35+ regions with AZs | 130 zones | Up to 3 ADs per region; FDs in all |
| Edge locations | 700+ PoPs, 43 Local Zones | 190+ PoPs | 200+ edge locations | CDN via Oracle + partner edge |
| Countries served | 245+ | 190+ | 200+ | ~50+ regions worldwide |
| US regions | 9 (incl. GovCloud) | ~15+ (incl. Government) | 9 | ~10+ (incl. GovCloud) |
| Unique differentiator | Largest overall footprint | Largest region count, strongest gov/public sector | TPU/AI-optimized infrastructure | Uniform global pricing, sovereign/distributed cloud |
| Intercloud partnerships | — | Oracle@Azure, OCI interconnects | Oracle@GCP | Database@AWS, Database@Azure, Database@GCP |

---

## 5. Security & Compliance

### 5.1 AWS

- **Certifications/Attestations:** ISO 27001, 27017, 27018, 27701, 9001, 20000-1, 22301 (2026 re-certified with no findings); CSA STAR CCM v4.0; SOC 1/2/3; HITRUST CSF; FedRAMP (Moderate/High); PCI DSS; HIPAA; GDPR; IRAP; C5 (Germany); and regional certifications (e.g., Dubai Electronic Security Centre, renewed January 2026).
- **Key services:** AWS Artifact (compliance reports), IAM, KMS, Nitro Enclaves (confidential computing), GuardDuty, Security Hub, Macie, Inspector, WAF/Shield (DDoS), CloudTrail, Config, Detective, and AWS Security Incident Response (included with Enterprise/Unified Support).
- **AI security:** Bedrock Guardrails, Bedrock Data Automation, SageMaker Model Monitor, and encrypted-by-default AI services.
- **Scale:** AWS claims the most extensive set of compliance programs of any cloud provider (300+ security, compliance, and governance services and features).

### 5.2 Google Cloud

- **Certifications/Attestations:** ISO 27001, 27017, 27018, 27701, 42001 (AI management); SOC 1/2/3; FedRAMP (Moderate and High); HITRUST; HIPAA; IL4/IL5 (DoD); ITAR; StateRAMP; CMMC; FIPS 140-2; CSA STAR; MARS-E; Protected B (Canada).
- **Key services:** Security Command Center Enterprise (merged with Google Security Operations/Mandiant), Chronicle, IAM, Cloud KMS/External Key Manager, Confidential Computing (Confidential VMs, Confidential Space), BeyondCorp Enterprise (Zero Trust), VPC Service Controls, Cloud Armor (DDoS/WAF), Event Threat Detection, Data Loss Prevention.
- **AI security:** Gemini Enterprise Agent Platform includes built-in security, governance, and Access Transparency; Gemini Enterprise compliance docs list FedRAMP, HIPAA, ISO 27001/42001, IL4/IL5, ITAR, SOC 1/2/3.
- **Differentiator:** Mandiant threat intelligence integration, strong Zero Trust (BeyondCorp), and leading AI governance standards (ISO 42001).

### 5.3 Microsoft Azure

- **Certifications/Attestations:** **100+ compliance certifications**, including 50+ region/country-specific; ISO 27001, 27017, 27018, 27701, 20000-1, 22301, 9001; SOC 1/2/3; FedRAMP High; HITRUST; PCI DSS; HIPAA; DoD IL2/4/5/6; CMMC; FIPS 140; IRAP (Australia); C5 (Germany); MTCS (Singapore); ENS (Spain); plus financial/healthcare/education/media-specific offerings.
- **Key services:** Microsoft Defender for Cloud, Defender XDR, Microsoft Sentinel (SIEM), Microsoft Entra ID (identity), Purview (data governance/compliance), Key Vault (HSM), Azure Confidential Computing, DDoS Protection, Azure Policy, Blueprints, Service Trust Portal.
- **AI security:** Microsoft Foundry includes responsible AI tools, content safety, and model governance; Azure OpenAI offers enterprise-grade data privacy (no training on customer data).
- **Differentiator:** Broadest compliance portfolio (100+ offerings), strongest integration with Microsoft 365/Entra for enterprise identity, and deep public-sector/government compliance coverage.

### 5.4 Oracle Cloud Infrastructure (OCI)

- **Certifications/Attestations:** ISO 27001, SOC 1/2/3, FedRAMP (Moderate/High for OCI), PCI DSS, HIPAA, GDPR, CSA STAR, FIPS 140-2, HITRUST CSF, DoD DISA SRG IL5 (for OCI Government Cloud), C5 (Germany), and regional frameworks.
- **Key services:** Oracle Cloud Guard (security posture), Security Zones, Vault (KMS/HSM), IAM, Network Security Groups, Web Application Firewall (WAF), DDoS Protection, Bastion, Data Safe, and Audit. OCI also offers isolated/sovereign cloud options (Oracle Alloy, Government Cloud, EU Sovereign Cloud).
- **AI security:** OCI Enterprise AI includes built-in security, observability, and governance; zero-data-retention endpoints for AI models.
- **Differentiator:** Strong security for Oracle Database workloads (Data Safe, Database Vault, Transparent Data Encryption); sovereign/distributed cloud options; but a smaller overall compliance catalog than AWS/Azure/GCP.

### 5.5 Security & Compliance Summary Table

| Dimension | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| ISO 27001 | ✔ | ✔ | ✔ | ✔ |
| SOC 1/2/3 | ✔ | ✔ | ✔ | ✔ |
| FedRAMP | Moderate/High | High | Moderate/High | Moderate/High |
| HIPAA | ✔ | ✔ | ✔ | ✔ |
| PCI DSS | ✔ | ✔ | ✔ | ✔ |
| HITRUST | ✔ | ✔ | ✔ | ✔ |
| DoD IL levels | IL2/4/5 | IL2/4/5/6 | IL4/5 | IL5 (GovCloud) |
| C5 (Germany) | ✔ | ✔ | ✔ | ✔ |
| Total compliance offerings | 300+ services/features | 100+ certifications | ~90+ (est.) | ~50+ (est.) |
| AI-specific standards | ISO 42001 (in progress) | Responsible AI tools, ISO 42001 | ISO 42001 certified | Enterprise AI governance |
| Key differentiator | Broadest security service catalog | Most compliance certifications, best gov coverage | Mandiant intel, Zero Trust (BeyondCorp) | Oracle DB security depth, sovereign options |
| Native SIEM/SOAR | Security Hub, Detective | Microsoft Sentinel | Security Command Center Enterprise | Cloud Guard, Security Zones |

---

## 6. Overall Summary Table

| Dimension | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| **Compute pricing (US)** | Mid (~$70/mo for 2vCPU/8GB) | Mid (~$70/mo) | Low-mid (~$49–65/mo with SUD) | **Lowest** (~$54/mo for 4vCPU/16GB) |
| **Storage pricing (US)** | Highest standard object ($0.023/GB); deep archive cheapest | **Lowest standard object** ($0.018/GB) | Mid ($0.020/GB) | Highest object standard ($0.0255/GB); **block storage cheapest** |
| **Egress pricing** | $0.09/GB | $0.087/GB | $0.12/GB (highest) | **$0.0085/GB (lowest, 10 TB free)** |
| **AI/ML breadth** | **Broadest portfolio** | Largest model catalog (11K+) | Best Gemini/TPU integration | Growing; DB-integrated; best GPU price |
| **Enterprise support** | TAM at $5K/mo; 15-min P1; strong tooling | Unified Enterprise; 15-min rapid response; Microsoft ecosystem | Premium at $15K/mo; 15-min P1; strong TAM model | **Support bundled (no extra fee)**; Support Rewards |
| **Infrastructure scale** | **Largest** (39 regions, 123 AZs, 700+ PoPs) | Most regions (70+ announced) | 43 regions, 130 zones | 50+ regions, uniform pricing |
| **Security/compliance** | **Broadest service catalog** | **Most certifications (100+)** | Strong AI security, Mandiant | Strong Oracle DB security, sovereign options |
| **Best overall for** | Enterprises needing max services/global reach | Microsoft-centric, regulated industries | AI-native, data analytics, ML | Cost-sensitive, Oracle DB workloads, high-egress apps |

---

## 7. Key Strategic Takeaways (2026)

1. **Pricing:** OCI wins decisively on compute, block storage, and egress (10 TB free, then ~10x cheaper than competitors). Azure wins on standard object storage among the big three. GCP is the cheapest big-three option for on-demand compute. AWS is the most expensive on storage/egress but offers the deepest archive tier (Glacier Deep Archive at $0.00099/GB/mo).

2. **AI/ML:** AWS leads in breadth of services; Azure leads in model catalog breadth and OpenAI integration; Google leads in frontier Gemini models, TPUs, and agentic AI (via the new Gemini Enterprise Agent Platform); OCI is the value player with aggressive GPU pricing and deep Oracle Database integration.

3. **Enterprise Support:** AWS and Google both offer 15-minute P1 response at top tiers, with AWS's $5K/mo Enterprise minimum being the most accessible. Azure's Unified Enterprise offers the fastest catastrophic-response (15 min) but at higher cost. OCI's bundled-support model is unique and can reduce total cost of ownership.

4. **Infrastructure:** AWS has the largest global footprint. Azure has the most regions and strongest government presence. GCP has the most AI-optimized infrastructure. OCI offers uniform global pricing and the most flexible distributed/sovereign cloud options.

5. **Security/Compliance:** All four are enterprise-grade. Azure leads on compliance certification count (100+); AWS leads on security service breadth; Google leads on AI-specific compliance (ISO 42001) and threat intelligence (Mandiant); OCI leads on Oracle database security and sovereign cloud options.

---

## References

1. AWS Global Infrastructure — Regions & AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az
2. AWS Global Infrastructure: https://aws.amazon.com/about-aws/global-infrastructure
3. AWS S3 Pricing: https://aws.amazon.com/s3/pricing
4. AWS EC2 On-Demand Pricing: https://aws.amazon.com/ec2/pricing/on-demand
5. AWS EBS Pricing: https://aws.amazon.com/ebs/pricing
6. AWS Support Plans: https://aws.amazon.com/premiumsupport/plans
7. AWS Support Pricing: https://aws.amazon.com/premiumsupport/pricing
8. AWS Enterprise Support: https://aws.amazon.com/premiumsupport/plans/enterprise
9. AWS Support Plan Documentation (EOS notices): https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html
10. AWS Compliance Programs: https://aws.amazon.com/compliance/programs
11. AWS ISO & CSA STAR 2026 Certification Blog: https://aws.amazon.com/blogs/security/2026-iso-and-csa-star-certificates-are-now-available-with-two-additional-services
12. AWS DESC 2026 Certification Blog: https://aws.amazon.com/blogs/security/aws-completes-the-2026-annual-dubai-electronic-security-centre-desc-certification-audit
13. AWS ML Decision Guide: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/ml-guide.html
14. AWS Bedrock vs SageMaker Decision Guide: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/bedrock-or-sagemaker.html
15. AWS Machine Learning: https://aws.amazon.com/ai/machine-learning
16. AWS SageMaker: https://aws.amazon.com/sagemaker
17. AWS AI/ML Landscape 2026 (dev.to): https://dev.to/aws-builders/the-aws-aiml-landscape-in-2026-simplified-17i3
18. AWS EC2 Pricing Guide 2026 (Usage.ai): https://www.usage.ai/blogs/aws/ec2/pricing
19. AWS S3 Pricing Guide 2026 (CloudZero): https://www.cloudzero.com/blog/s3-pricing
20. AWS Pricing Changes 2026 (Spendark): https://spendark.com/blog/aws-pricing-changes-2026
21. AWS S3 Pricing Guide (CloudBum): https://cloudburn.io/blog/amazon-s3-pricing
22. Cloud Pricing Comparison 2026 (EffectiveSoft): https://www.effectivesoft.com/blog/cloud-pricing-comparison.html
23. Cloud Storage Pricing Comparison 2026 (Finout): https://www.finout.io/blog/cloud-storage-pricing-comparison
24. AWS vs Azure vs GCP Pricing Guide 2026 (Usage.ai): https://www.usage.ai/blogs/finops/multi-cloud/cloud-pricing-comparison
25. Cloud Pricing Comparison (Cast AI): https://cast.ai/blog/cloud-pricing-comparison
26. Azure Pricing Overview: https://azure.microsoft.com/en-us/pricing
27. Azure Blob Storage Pricing: https://azure.microsoft.com/en-us/pricing/details/storage/blobs
28. Azure Managed Disks Pricing: https://azure.microsoft.com/en-us/pricing/details/managed-disks
29. Azure Support Plans: https://azure.microsoft.com/en-us/support/plans
30. Azure Support Response Times: https://azure.microsoft.com/en-us/support/plans/response
31. Azure SLA for Online Services (Jan 2026): https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services
32. Azure Compliance: https://azure.microsoft.com/en-us/explore/trusted-cloud/compliance
33. Azure Compliance Documentation: https://learn.microsoft.com/en-us/azure/compliance
34. Azure List of Regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
35. Azure Availability Zones Overview: https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview
36. Azure Product Availability by Region: https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table
37. Azure US Infrastructure Investment Blog: https://azure.microsoft.com/en-us/blog/microsofts-commitment-to-supporting-cloud-infrastructure-demand-in-the-united-states
38. Azure Machine Learning: https://azure.microsoft.com/en-us/products/machine-learning
39. Azure Machine Learning Docs: https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning
40. Azure OpenAI in Foundry Models: https://azure.microsoft.com/en-us/products/ai-foundry/models/openai
41. Microsoft Foundry Models in Azure ML: https://learn.microsoft.com/en-us/azure/machine-learning/foundry-models-overview
42. Microsoft Azure AI Guide 2026 (Voiceflow): https://www.voiceflow.com/blog/microsoft-azure
43. Azure vs GCP Pricing 2026 (Spendark): https://spendark.com/blog/azure-vs-gcp-pricing
44. Azure Pricing 2026 (CheckThat): https://checkthat.ai/brands/microsoft-azure/pricing
45. AWS vs Azure Pricing 2026 (CloudZero): https://www.cloudzero.com/blog/aws-vs-azure-pricing
46. Azure Pricing Guide 2026 (Sedai): https://sedai.io/blog/microsoft-azure-pricing-guide
47. Google Cloud Pricing Overview: https://cloud.google.com/pricing
48. Google Cloud Storage Pricing: https://cloud.google.com/storage/pricing
49. Google Cloud Locations (Regions & Zones): https://cloud.google.com/about/locations
50. Google Cloud Regions & Zones Docs: https://docs.cloud.google.com/compute/docs/regions-zones
51. Google Cloud Compliance Offerings: https://cloud.google.com/security/compliance/offerings
52. Google Cloud Compliance Resources: https://cloud.google.com/compliance
53. Gemini Enterprise Agent Platform Compliance: https://docs.cloud.google.com/gemini/enterprise/docs/compliance-security-controls
54. Google Cloud Premium Support: https://cloud.google.com/support/premium
55. Google Cloud Premium Support Docs: https://docs.cloud.google.com/support/docs/premium
56. Google Cloud Support Plans Guide (DigitalOcean): https://www.digitalocean.com/resources/articles/google-cloud-support
57. Cloud Support Plan Pricing Benchmarks (VendorBenchmark): https://vendorbenchmark.com/blog/cloud-support-plan-pricing-benchmark-comparison
58. Google Cloud Pricing 2026 (Eon): https://www.eon.io/blog/google-cloud-pricing
59. GCP Storage Pricing Guide 2026 (CloudZero): https://www.cloudzero.com/blog/gcp-storage-pricing
60. GCP Compute Engine Pricing 2026 (Usage.ai): https://www.usage.ai/blogs/gcp/compute-engine
61. GCP Regions Guide (CloudZero): https://www.cloudzero.com/blog/gcp-regions
62. Google Cloud Next 2026 Welcome Blog: https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next26
63. Gemini Enterprise Agent Platform Product Page: https://cloud.google.com/products/gemini-enterprise-agent-platform
64. Gemini Enterprise Agent Platform Docs: https://docs.cloud.google.com/gemini-enterprise-agent-platform
65. Vertex AI Release Notes: https://docs.cloud.google.com/vertex-ai/docs/release-notes
66. Vertex AI Replaced by Gemini Enterprise Agent Platform (GCP Study Hub): https://gcpstudyhub.com/blog/vertex-ai-replaced-by-gemini-enterprise-agent-platform
67. Google Unveils Gemini Enterprise Agent Platform (HPCwire): https://www.hpcwire.com/aiwire/2026/04/23/google-unveils-gemini-enterprise-agent-platform
68. Oracle Cloud Pricing: https://www.oracle.com/cloud/pricing
69. Oracle Cloud Economics: https://www.oracle.com/cloud/economics
70. Oracle OCI Price List: https://www.oracle.com/cloud/price-list
71. Oracle Cloud Cost Estimator: https://www.oracle.com/cloud/costestimator.html
72. Oracle Public Cloud Regions: https://www.oracle.com/cloud/public-cloud-regions
73. Oracle OCI Regions & Availability Domains Docs: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm
74. Oracle Cloud Service Availability: https://www.oracle.com/cloud/distributed-cloud/service-availability
75. Oracle AI Services: https://www.oracle.com/artificial-intelligence/ai-services
76. Oracle Enterprise AI: https://www.oracle.com/artificial-intelligence/enterprise-ai
77. Oracle Artificial Intelligence: https://www.oracle.com/artificial-intelligence
78. Oracle Support: https://www.oracle.com/support
79. Oracle Premier Support: https://www.oracle.com/support/premier
80. Oracle Cloud Compliance (Canada): https://www.oracle.com/ca-en/corporate/cloud-compliance
81. Oracle Software Technical Support Policies (Aug 2026): https://www.oracle.com/contracts/docs/057419.pdf
82. Oracle Cloud Pricing Guide 2026 (CloudZero): https://www.cloudzero.com/blog/oracle-cloud-pricing
83. Oracle Cloud Infrastructure Pricing 2026 (VendorBenchmark): https://vendorbenchmark.com/vendors/oracle-cloud-infrastructure-pricing
84. Oracle Cloud Infrastructure Pricing (TrustRadius): https://www.trustradius.com/products/oracle-cloud-infrastructure/pricing
85. OCI Cost Management 2026 (Opslyft): https://www.opslyft.com/guides/oci-cost-optimization
86. Oracle Cloud Infrastructure Guide 2026 (AppsTek): https://appstekcorp.com/blog/what-is-oracle-cloud-infrastructure
87. Oracle Cloud Infrastructure Pros/Cons (Finout): https://www.finout.io/blog/oracle-cloud-infrastructure-pros-cons
88. OCI Regions & Availability Domains Guide (K21 Academy): https://k21academy.com/oracle/oci-regions-availability-domains
89. Oracle Database@AWS Availability (April 2026): https://aws.amazon.com/about-aws/whats-new/2026/04/oracle-database-aws-available-twelve-regions
90. OCI High Availability Blog: https://blogs.oracle.com/cloud-infrastructure/high-availability-strategy-oracle-cloud-regions
91. Oracle Cloud Security Best Practices 2026 (SentinelOne): https://www.sentinelone.com/cybersecurity-101/cloud-security/oracle-cloud-security
92. OCI Certification Best Practices (Oracle A-Team): https://www.ateam-oracle.com/ciso-perspectives-oci-certification-best-practices
93. Flexera 2026 State of the Cloud (via CRN): https://www.crn.com/news/cloud/2026/azure-vs-aws-vs-gcp-vs-oracle-vs-ibm-client-spending-face-off-flexera-report
94. Cloud Computing Cost 2026 (Rackspace Spot): https://spot.rackspace.com/blog/cloud-computing-cost
95. Cloud Infrastructure Map (TeleGeography): https://www.cloudinfrastructuremap.com
96. AWS vs Azure vs Google Cloud Comparison 2026 (Northflank): https://northflank.com/blog/aws-vs-azure-vs-google-cloud
97. Public Sector Network Cloud Comparison: https://publicsectornetwork.com/insight/aws-vs-microsoft-azure-vs-google-cloud-vs-oracle-cloud-infrastructure-a-comprehensive-comparison
98. Cloud Service Equivalents (CanvasCloud): https://www.canvascloud.ai/cloud-service-equivalents
99. AWS Support Response Times 2026 (DigitalOcean): https://www.digitalocean.com/resources/articles/aws-support-response-time
100. Google Cloud Support Plans (Wursta): https://wursta.com/google-cloud-support-understanding-the-new-pricing-model-and-alternatives

---

*Note: All prices and certifications are as reported by official provider pages and reputable third-party sources as of August 2026. Cloud pricing is dynamic; consult official pricing calculators before final procurement decisions. Compliance certifications are continuously updated; check each provider's compliance portal for the latest scope.*
