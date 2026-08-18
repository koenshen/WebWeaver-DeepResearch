# Comprehensive Literature Review: Data Synthesis Methods for Tool-Augmented LLM Agent Training (2025)

## 1. TaskCraft: Automated Generation of Agentic Tasks

**Paper:** Shi et al., 2025 — arXiv:2506.10055, ICLR 2026
**URL:** https://arxiv.org/abs/2506.10055 | **Code:** https://github.com/OPPO-PersonalAI/TaskCraft

### Motivation and Core Innovation
Existing instruction data lacks tool interaction, and current agentic benchmarks (e.g., GAIA) rely on costly human annotation, limiting scalability. TaskCraft introduces an automated workflow for generating **difficulty-scalable, multi-tool, and verifiable agentic tasks** with execution trajectories. Starting from simple atomic tasks, it expands them using **depth-based** (sequential chaining of sub-tasks) and **width-based** (parallel, combinable sub-tasks) extensions to create structurally and hierarchically complex challenges. Each task is verified for solvability by an agent but unsolvable by a bare LLM. The final dataset contains **~36,000 tasks** across varying difficulty levels.

### Key Takeaways and Claimed Contributions
- First automated pipeline to synthesize agentic tasks with tool interaction trajectories at scale.
- Significantly reduces reliance on human annotation for agent training data.
- Demonstrates that synthetic tasks improve both prompt optimization (prompt learning) and supervised fine-tuning (SFT) of agent foundation models.

### Empirical Setup
- **Models:** Qwen2.5-3B-Base, Qwen2.5-3B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-32B-Instruct, DeepSeek-R1-Distill-Llama-8B.
- **Baselines:** MHQA (multi-hop QA) data, Search-R1, R1-Searcher, WebSailor, WebThinker, WebDancer, SimpleDeepSearcher, Search-o1.
- **Training Configs:** SFT with learning rate 5e-6, weight decay 0.1, warmup + cosine decay. RL (Search-R1 style): policy lr=1e-6, value lr=1e-5, KL divergence π=0.001, clip ratio ε=0.2, action budget=4, retrieval depth=3.
- **Compute Budget:** Not explicitly specified.
- **Evaluation Benchmarks & Key Results:**
  - **GAIA (103 questions):** MHQA baseline 38.8% → +2.5k TaskCraft tasks = 60.2% (+21.4) → +8k TaskCraft = 60.8% (+22.0). Qwen2.5-7B-Instruct with 5k MHQA + 2.5k TaskCraft (SFT) + 8k TaskCraft (RL) achieves 40.8% on GAIA, 13.4% on BrowserComp, 16.0% on HLE. Qwen2.5-32B-Instruct with 7.5k TaskCraft achieves 60.2% on GAIA.
  - **WebWalker:** 55.0% (Qwen2.5-7B-Instruct + 7.5k TaskCraft).
  - **BrowserComp:** 12.4% (Qwen2.5-7B-Instruct + 7.5k TaskCraft), 13.4% with SFT+RL.
  - **HLE:** 16.4% (Qwen2.5-7B-Instruct + 7.5k TaskCraft).
  - **Multi-hop QA (HotpotQA, Musique, Bamboogle):** +14.0% average SFT improvement for Qwen2.5-3B-Base, +6.0% for Qwen2.5-3B-Instruct over base workflow. Up to +19.2% on Bamboogle when combined with Search-R1 RL.

### Limitations
- The paper does not explicitly discuss failure modes. The main limitation is that the data generation pipeline is computationally intensive (requires strong LLMs for verification and expansion). The generated tasks are constrained to the capabilities of the generating LLM, and quality may degrade for tasks requiring extremely long trajectories.

---

## 2. Beyond Ten Turns: Unlocking Long-Horizon Agentic Search with Large-Scale Asynchronous RL (ASearcher)

**Paper:** Gao et al., 2025 — arXiv:2508.07976, NeurIPS 2025
**URL:** https://arxiv.org/abs/2508.07976 | **Code:** https://github.com/inclusionAI/ASearcher

### Motivation and Core Innovation
Existing open-source search agents are limited by **small turn limits (≤10)** in online RL, which restricts learning of complex multi-step search strategies. Additionally, large-scale high-quality QA pairs for training are scarce. ASearcher introduces a **fully asynchronous RL training system** (AReaL) that decouples trajectory rollouts from model updates, enabling long-horizon search (up to 128 turns) without efficiency loss. It also develops a **prompt-based data synthesis agent** that iteratively modifies seed questions via **Injection** (adding supporting facts) and **Fuzzing** (obfuscating variable names) to create challenging, tool-requiring QA pairs.

### Key Takeaways and Claimed Contributions
- First scalable asynchronous RL training for search agents with up to 128 tool-call turns.
- Autonomous data synthesis agent producing 134k+ QA pairs from 14k seeds.
- ASearcher achieves state-of-the-art results among open-source 32B agents on GAIA, xBench-DeepSearch, and Frames.
- Demonstrates that RL training with long-horizon trajectories yields substantial improvements over prompt-based agents.

### Empirical Setup
- **Models:** Qwen2.5-7B, Qwen2.5-14B (base LLMs), QwQ-32B (LRM).
- **Baselines:** Search-R1, R1-Searcher, Search-o1, DeepResearcher, SimpleDeepSearcher, WebThinker, WebDancer, Qwen-2.5 direct generation, QwQ-32B direct generation.
- **Training Configs:** GRPO algorithm. Turn limit = 32 for 7B/14B, 128 for QwQ-32B. Batch size = 128 (7B/14B), 64 (QwQ). Training data = 35k samples each. Dynamic filtering to exclude queries lacking meaningful training signals. Reward: F1 + format reward for base LLMs, LLM-as-Judge for LRMs.
- **Compute Budget:** 7,600 H800 GPU hours for ASearcher-Web-QwQ training.
- **Evaluation Benchmarks & Key Results:**
  - **GAIA (Avg@4):** ASearcher-Web-QwQ = 52.8 (Pass@4 = 70.1). RL improvement: +20.8% (initial 43.7 → 52.8). Final v2 achieves 58.7.
  - **xBench-DeepSearch (Avg@4):** 42.1 (Pass@4 = 68.0). RL improvement: +46.7% (initial 28.7 → 42.1). Final v2 achieves 51.1.
  - **Frames (Avg@4):** 70.9 (Pass@4 = 78.4). Final v2 achieves 74.5.
  - **Local KB setting (7 datasets):** ASearcher-Local-7B avg F1=58.0, LasJ=61.0. ASearcher-Local-14B avg F1=60.0, LasJ=65.6 (surpasses Search-R1-32B).
  - **Web-based setting:** ASearcher-Web-14B avg F1=61.5.

### Limitations
- **Small model capacity:** The 7B model fails to learn valid webpage browsing, while the 14B model can. The authors hypothesize that 7B capacity is insufficient to stably learn summarizing lengthy webpages in a zero-RL-training setting.
- The data synthesis agent relies on strong LLMs (e.g., QwQ-32B), creating a dependency on expensive models.
- Long-horizon training (128 turns) introduces high variance in trajectory collection time, which the asynchronous system addresses but adds engineering complexity.

---

## 3. DeepDive: Advancing Deep Search Agents with Knowledge Graphs and Multi-Turn RL

**Paper:** Lu et al., 2025 — arXiv:2509.10446
**URL:** https://arxiv.org/abs/2509.10446 | **Code:** https://github.com/THUDM/DeepDive

### Motivation and Core Innovation
Open models significantly lag behind proprietary LLMs as deep search agents (e.g., BrowseComp). The gap is attributed to the **shortage of hard-to-find (complex, multi-hop) data** and the **absence of multi-turn RL training**. DeepDive proposes a two-pronged data synthesis strategy: (1) **automated KG-based synthesis** using Knowledge Graphs to generate complex, verifiable questions requiring multi-hop search, and (2) **semi-automated i.i.d. synthesis** with human annotators supported by OpenAI o3 with search capabilities. The combined data is used in an end-to-end multi-turn RL training framework.

### Key Takeaways and Claimed Contributions
- Open-source competitive results on BrowseComp (15.3% for DeepDive-32B, 22.2% with i.i.d. data + RL).
- Data contributes to GLM-4.5/GLM-4.6 models' strong BrowseComp performance.
- Demonstrates that KG-based data + multi-turn RL can significantly close the gap with proprietary systems.

### Empirical Setup
- **Models:** GLM-Z1-9B-0414, QwQ-32B.
- **Baselines:** WebSailor, Search-o1, DeepSeek-R1-Browse, R1-Searcher, WebDancer, WebThinker, Qwen-2.5-32B-Instruct, Qwen3-235B.
- **Training Configs:** Total dataset = 3,250 QA pairs (1,016 SFT + 2,234 RL). SFT trajectories = 858 via reject sampling. RL: KL penalty β=0, learning rate 1e-6. Contamination rate: KG data 2.6%, i.i.d. data 3.4% (both clean).
- **Compute Budget:** Not explicitly specified.
- **Evaluation Benchmarks & Key Results:**
  - **BrowseComp:** DeepDive-9B (sft-only) = 5.6%; DeepDive-9B (RL) = 6.3%; DeepDive-32B (sft-only) = 9.5%; DeepDive-32B (RL) = 15.3% (surpasses WebSailor, Search-o1, DeepSeek-R1-Browse). With i.i.d. data + RL → 22.2%.
  - **Generalization on simple search tasks:** DeepDive-9B: 15.7% (search), 35.0% (multi-hop), 15.3% (combined). DeepDive-32B: 14.8% (search), 25.6% (multi-hop), 50.5% (combined), 29.3% (overall).

### Limitations
- The i.i.d. data synthesis still requires human annotators (though supported by o3), limiting full automation.
- The KG-based data is constrained to knowledge present in the KG, potentially limiting coverage of real-world, rapidly changing information.
- No explicit discussion of failure modes in the available material.

---

## 4. WebThinker: Empowering Large Reasoning Models with Deep Research Capability

**Paper:** Li et al., 2025 — arXiv:2504.21776, NeurIPS 2025
**URL:** https://arxiv.org/abs/2504.21776 | **Code:** https://github.com/RUC-NLPIR/WebThinker

### Motivation and Core Innovation
Large Reasoning Models (LRMs) like OpenAI-o1 and DeepSeek-R1 demonstrate impressive reasoning but are limited by **static internal knowledge**, hindering performance on knowledge-intensive tasks and research report generation. WebThinker is a **deep research agent** that integrates a **Deep Web Explorer** module for dynamic search, navigation, and extraction, and employs an **Autonomous Think-Search-and-Draft** strategy to interleave reasoning, information gathering, and report writing. Training uses **iterative online Direct Preference Optimization (DPO)** for RL-based research tool utilization.

### Key Takeaways and Claimed Contributions
- Endows LRMs with autonomous web search, navigation, and report drafting capabilities.
- Iterative online DPO training for research tool utilization.
- Significantly outperforms existing methods (Search-o1, RAG workflows, direct reasoning) and strong proprietary systems on complex reasoning and report generation tasks.

### Empirical Setup
- **Models:** QwQ-32B (primary LRM), DeepSeek-R1 series, Qwen2.5-Instruct (assistant LLM for summarization and report writing).
- **Baselines:** Direct reasoning, various RAG workflows, Search-o1, and other autonomous search agents.
- **Training Configs:** Iterative online DPO. Search engine: Bing Web Search API, later Google Serper API. Web crawler: Crawl4AI.
- **Compute Budget:** Not explicitly specified.
- **Evaluation Benchmarks & Key Results:**
  - **GPQA (PhD-level Science QA, 198 questions):** WebThinker-32B achieves 70.7% (up to +21.5% over baselines).
  - **GAIA (103 questions):** 48.5% (WebThinker-32B).
  - **WebWalkerQA (680 questions):** 46.5% (WebThinker-32B).
  - **Humanity's Last Exam (HLE, 500 questions):** 15.8% (WebThinker-32B).
  - **Report generation (Glaive / Reasoning-v1-20m):** Significantly outperforms baselines.
  - WebThinker-32B consistently outperforms Search-o1, various RAG workflows, and direct reasoning across all benchmarks.

### Limitations
- Per the NeurIPS reviewer comments, the paper discusses limitations in the conclusion section. Key limitations likely include: (1) dependency on search engine API quality and availability; (2) computational cost of iterative online DPO with long trajectories; (3) potential for web content to be noisy or misleading, affecting response quality; (4) the approach is demonstrated on QwQ-32B scale and may not transfer to smaller models.

---

## 5. WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization

**Paper:** Tao et al., 2025 — arXiv:2507.15061, ICLR 2026
**URL:** https://arxiv.org/abs/2507.15061 | **Data:** https://huggingface.co/datasets/iic/WebShaper

### Motivation and Core Innovation
Existing approaches for information-seeking (IS) agent training adopt an **information-driven paradigm** (collect web data → generate questions based on retrieval), which may cause **inconsistency between information structure and reasoning structure**. WebShaper proposes a **formalization-driven** framework based on **set theory** and **Knowledge Projections (KP)**, enabling precise control over reasoning structure. The synthesis process starts with seed tasks and uses a multi-step expansion with an agentic **Expander** that retrieves, validates, and composes KP operations to create increasingly complex questions.

### Key Takeaways and Claimed Contributions
- Formalization-driven data synthesis that ensures alignment between information structure and reasoning structure.
- Achieves state-of-the-art among open-source IS agents on GAIA and WebWalkerQA.
- Fully open-source pipeline with transparent computational costs.
- Demonstrates generalizability of synthesized data across multiple backbone models (Qwen2.5-32B, Qwen2.5-72B, QwQ-32B).

### Empirical Setup
- **Models:** Qwen2.5-32B, Qwen2.5-72B, QwQ-32B.
- **Baselines:** WebSailor, WebDancer, WebThinker, Search-o1, SimpleDeepSearcher, and various training data compositions (MHQA, E2HQA, WebWalkerQA).
- **Training Configs:**
  - **SFT:** Batch size 32, learning rate 5e-6, warmup + cosine decay, weight decay 0.1.
  - **RL:** 8 rollouts per group, temperature 1.0, top-p 1.0, batch size 128, mini-batch size 32, learning rate 1e-6.
  - Training data: 5,000 samples per dataset for comparison; released dataset contains 500 high-quality QA pairs.
- **Compute Budget:** Not explicitly specified, but the paper claims computational costs are transparent and measurable.
- **Evaluation Benchmarks & Key Results:**
  - **GAIA:** WebShaper on Qwen2.5-72B achieves 60.19 (SOTA at publication). RL improvement: +7.8 (32B: 52.4→60.2), +13.5 (72B: 46.6→60.1). WebShaper data achieves 5-10 point improvements over baseline datasets.
  - **WebWalkerQA:** 52.50 (SOTA at publication). RL improvement: +6.7 (32B: 44.6→51.3), +5.8 (72B: 46.4→52.2).
  - **Average GAIA score:** Qwen2.5-32B with WebShaper reaches 43.6, outperforming WebWalkerQA-based training.
  - **QwQ-32B backbone:** WebWalkerQA 53.3, E2HQA 45.6, MHQA 41.7.

### Limitations
- The released dataset is relatively small (500 QA pairs), which may raise questions about scalability.
- The formalization relies on Knowledge Projections, which may not cover all real-world information-seeking patterns.
- The agentic Expander requires strong LLMs for retrieval, validation, and expansion, creating significant upfront computational cost.
- Not explicitly stated, but the set-theoretic formalization may be less flexible for extremely open-ended or ambiguous queries.

---

## 6. WebWalkerQA: Benchmarking LLMs in Web Traversal

**Paper:** Wu et al., 2025 — arXiv:2501.07572, ACL 2025
**URL:** https://arxiv.org/abs/2501.07572 | **Data:** https://huggingface.co/datasets/callanwu/WebWalkerQA

### Motivation and Core Innovation
Traditional search engines retrieve **shallow content**, limiting LLMs' ability to handle complex, multi-layered information. WebWalkerQA is a **benchmark** designed to assess LLMs' ability to perform **web traversal**—systematic exploration of website subpages via clickable links to extract high-quality data. The accompanying **WebWalker** framework is a multi-agent system that mimics human-like web navigation through an **explore-critic paradigm**: an Explorer agent navigates while a Critic agent provides memory and guidance.

### Key Takeaways and Claimed Contributions
- First benchmark specifically targeting web traversal (vertical and horizontal) rather than shallow retrieval.
- Proposes a multi-agent framework (WebWalker) that outperforms ReAct and Reflexion baselines.
- Demonstrates that even advanced models struggle with multi-source, depth-oriented web traversal (accuracy <40%).
- 680 QA pairs from real-world scenarios, categorized into single-source and multi-source queries.

### Empirical Setup
- **Models:** GPT-4o, Qwen-Plus, Qwen2.5 series (7B, 14B, 32B, 72B).
- **Baselines:** ReAct, Reflexion.
- **Training Configs:** WebWalker is driven by prompting without additional training (zero-shot agent framework).
- **Compute Budget:** Not applicable (prompting-based, no training).
- **Evaluation Benchmarks & Key Results:**
  - **WebWalkerQA (680 questions):** WebWalker with GPT-4o achieves 55.00% accuracy on easy single-source QAs, and 65% on hard multi-source QAs (with action count 1583). On multi-source tasks, WebWalker often shows a significant performance gap over ReAct and Reflexion.
  - **Overall:** Even advanced models struggle to exceed 40% accuracy on multi-source and depth-oriented tasks, emphasizing the benchmark's challenge.
  - **Metrics:** Question-answering accuracy (acc.) and action count (A.C.) for efficiency.

### Limitations
- The benchmark is relatively small (680 questions) and may not cover all web traversal scenarios.
- WebWalker is a prompting-based framework without training, so its performance is bounded by the underlying LLM's capabilities.
- Even with optimized frameworks, accuracy on complex multi-source tasks remains low (<40% for many configurations), indicating significant room for improvement.
- The benchmark may not fully capture the dynamic nature of real web content (e.g., JavaScript-rendered pages, login-required content).

---

## 7. Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning

**Paper:** Jin et al., 2025 — arXiv:2503.09516
**URL:** https://arxiv.org/abs/2503.09516 | **Code:** https://github.com/PeterGriffinJin/Search-R1

### Motivation and Core Innovation
Existing RAG treats retrieval as a **static preprocessing step**, tool-use approaches rely on **prompting (lacking generalization)** or **expensive SFT with large-scale annotations**, and the non-differentiable nature of search complicates end-to-end learning. Search-R1 extends the DeepSeek-R1 RL framework to enable LLMs to **autonomously generate search queries during step-by-step reasoning** with real-time retrieval. Key innovations: **retrieved token masking** for stable RL training (preventing the model from optimizing over retrieved content), **multi-turn interleaved reasoning and search**, and a **simple outcome-based reward** (exact match).

### Key Takeaways and Claimed Contributions
- First RL framework to train LLMs for interleaved reasoning and search from scratch.
- Demonstrates consistent improvements across 3 model families and 7 QA datasets.
- Provides empirical insights into RL optimization methods, LLM choices, and response length dynamics.
- Open-source codebase and model checkpoints.

### Empirical Setup
- **Models:** Qwen2.5-3B (Base/Instruct), Qwen2.5-7B (Base/Instruct), Llama-3.2-3B (Base/Instruct).
- **Baselines:** Direct inference, CoT, RAG, IRCoT, Search-o1, SFT, RL without search (R1).
- **Training Configs:** Wikipedia 2018 dump + E5 retriever. Training on merged NQ + HotpotQA. PPO: policy lr=1e-6, value lr=1e-5, GAE λ=1, γ=1. GRPO: lr=1e-6, 5 samples/prompt. Retrieved token masking applied.
- **Compute Budget:** Not explicitly specified.
- **Evaluation Benchmarks & Key Results (Exact Match):**
  - **Qwen2.5-7B (GRPO):** Avg EM across 7 datasets: 0.517 (vs. best RAG baseline ~0.367). **26% average relative improvement** over RAG baselines. Key gains: NQ 0.134→0.396, TriviaQA 0.408→0.582, HotpotQA 0.183→0.345, Bamboogle 0.120→0.320.
  - **Qwen2.5-3B (GRPO):** **21% average relative improvement** over RAG baselines. Avg EM: 0.365 (vs. best RAG baseline ~0.302).
  - **LLaMA3.2-3B (GRPO):** **10% average relative improvement** over RAG baselines.
  - Gains hold across both in-distribution (NQ, HotpotQA) and out-of-distribution (TriviaQA, PopQA, 2WikiMultiHopQA, Musique, Bamboogle) evaluation.

### Limitations
- **Retrieval inaccuracy:** The search engine may return irrelevant or noisy information, which can mislead the LLM's reasoning.
- **Retriever quality:** Using weaker retrievers (e.g., Random, BM25) significantly limits final model performance.
- **Brittle reward signal:** Exact match (EM) is a coarse reward; it fails to reward semantically correct answers phrased differently.
- The paper acknowledges the need for more sophisticated reward mechanisms, dynamic retrieval adjustments based on uncertainty, and integration with diverse information sources beyond web search.
- Single-turn retrieval per reasoning step; no explicit mechanism for complex multi-turn search strategies.

---

## 8. AutoCoA: Internalizing Chain-of-Action Generation into Reasoning Models (Agent Models)

**Paper:** Zhang et al., 2025 — arXiv:2503.06580
**URL:** https://arxiv.org/abs/2503.06580 | **Code:** https://github.com/ADaM-BJTU/AutoCoA

### Motivation and Core Innovation
Traditional **agentic workflows** (e.g., ReAct) rely on **external prompts** to manage tool interactions, making tool usage a **passive, scripted behavior**. AutoCoA proposes **Large Agent Models (LAMs)** that internalize **Chain-of-Action (CoA)** generation, enabling autonomous decisions about when and how to use tools. The framework combines **SFT and RL** with three key components: (1) **step-level action triggering** via contrastive learning (CoT+A), (2) **trajectory-level CoA optimization** with observation masking, and (3) an **internal world model** learned by predicting environment responses, enabling simulated environment exploration before costly real-environment RL.

### Key Takeaways and Claimed Contributions
- Shifts from agentic workflows (prompting-based) to agent models (internalized, learned).
- Internal world model reduces real-environment interaction costs during RL.
- AutoCoA-trained models significantly outperform ReAct-based workflows, especially on long-horizon, multi-step tasks.
- Agent models maintain high accuracy at 5+ actions, while ReAct workflows show declining success rates.

### Empirical Setup
- **Models:** R1-Distill-Qwen-7B (primary). DeepSeek-R1 for comparison.
- **Baselines:** Model only (R1-Distill-Qwen-7B, DeepSeek-R1), Agent workflow (Qwen-7B-Base(ReAct), R1-Distill-Qwen-7B(ReAct)), Agent model variants (SFT-stage1, SFT-stage2, etc.).
- **Training Configs:** 20,000 samples from HotpotQA (10k CoT, 10k CoA, 1,500 CoT+A contrastive pairs). SFT: LLaMA-Factory. RL: verl framework, 96 optimization steps on 4,608 problems, single node Nvidia H20 GPUs, GRPO algorithm. Reward: exact match + format penalty.
- **Compute Budget:** Single node Nvidia H20 GPUs (no detailed hours); 96 RL optimization steps.
- **Evaluation Benchmarks & Key Results:**
  - **Single-hop QA:** Natural Questions (NQ), TriviaQA.
  - **Multi-hop QA:** HotpotQA, 2WikiMultihopQA (2WIKI), MuSiQue, Bamboogle.
  - AutoCoA variants substantially outperform the initial policy model with ReAct workflow across all datasets.
  - SFT-stage1&2 (when-to-act then how-to-act) enhances learning over SFT-stage2 alone.
  - Direct RL shows marginal gains, but combining simulated environment training (RL-stage1) with a small portion of real interaction (RL-stage2) improves adaptation and significantly reduces interaction costs.
  - CoA learning enables longer-horizon tasks (higher #action); agent models maintain high accuracy at 5 actions, whereas ReAct shows declining success rates.

### Limitations
- **Small model scale:** Only tested on R1-Distill-Qwen-7B; scalability to larger models is not validated.
- **Knowledge memorization:** The model's superior performance could be partly due to knowledge memorization rather than genuine search capability. On questions requiring unknown temporal knowledge, performance drops drastically.
- **Limited action types:** The framework focuses solely on search actions; extension to diverse tool types (calculator, code interpreter, etc.) is future work.
- **Preliminary exploration:** The authors explicitly note this is an initial attempt, with a wide range of potential approaches (pure RL, improved sampling, loss design) yet to be explored.
- **Open-ended tasks:** The current experiments are limited to QA; extension to open-ended, generative tasks is needed.

---

## Cross-Cutting Themes and Comparative Analysis

| Dimension | TaskCraft | ASearcher | DeepDive | WebThinker | WebShaper | WebWalkerQA | Search-R1 | AutoCoA |
|-----------|-----------|-----------|----------|------------|-----------|-------------|-----------|---------|
| **Data Synthesis Paradigm** | Depth/width expansion from atomic tasks | Iterative injection + fuzzing from seeds | KG-based + semi-automated i.i.d. | Think-Search-Draft trajectory | Set-theoretic formalization + KP expansions | Benchmark (manual) + multi-agent framework | RL from scratch (no data synthesis) | Contrastive CoT+A + CoA trajectory synthesis |
| **Training Method** | SFT + RL (Search-R1 style) | GRPO (asynchronous RL) | SFT + multi-turn RL | Iterative online DPO | SFT + RL (DAPO) | Prompting only (no training) | PPO / GRPO with token masking | SFT + GRPO (simulated + real) |
| **Max Turns** | 4 (action budget) | 128 (QwQ) | Not specified | Not specified | Not specified | Not specified | 1 retrieval per step | ~5+ |
| **Primary Benchmarks** | GAIA, WebWalker, BrowserComp, HLE | GAIA, xBench, Frames | BrowseComp | GPQA, GAIA, WebWalkerQA, HLE | GAIA, WebWalkerQA | WebWalkerQA (own) | NQ, HotpotQA, TriviaQA, 7 datasets | NQ, TriviaQA, HotpotQA, 2WIKI, MuSiQue, Bamboogle |
| **Best GAIA Score** | 60.8% (32B) | 58.7% (QwQ-32B) | - | 48.5% (32B) | 60.19% (72B) | - | - | - |
| **Best BrowseComp Score** | 16.0% (7B RL) | - | 22.2% (32B + i.i.d. RL) | - | - | - | - | - |
| **Open Source** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## References

1. Shi, D., Cao, J., Chen, Q., et al. (2025). TaskCraft: Automated Generation of Agentic Tasks. *ICLR 2026*. arXiv:2506.10055. https://arxiv.org/abs/2506.10055 | Code: https://github.com/OPPO-PersonalAI/TaskCraft

2. Gao, J., Fu, W., Xie, M., et al. (2025). Beyond Ten Turns: Unlocking Long-Horizon Agentic Search with Large-Scale Asynchronous RL. *NeurIPS 2025*. arXiv:2508.07976. https://arxiv.org/abs/2508.07976 | Code: https://github.com/inclusionAI/ASearcher

3. Lu, R., et al. (2025). DeepDive: Advancing Deep Search Agents with Knowledge Graphs and Multi-Turn RL. arXiv:2509.10446. https://arxiv.org/abs/2509.10446 | Code: https://github.com/THUDM/DeepDive

4. Li, X., Jin, J., Dong, G., et al. (2025). WebThinker: Empowering Large Reasoning Models with Deep Research Capability. *NeurIPS 2025*. arXiv:2504.21776. https://arxiv.org/abs/2504.21776 | Code: https://github.com/RUC-NLPIR/WebThinker

5. Tao, Z., Wu, J., Yin, W., et al. (2025). WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization. *ICLR 2026*. arXiv:2507.15061. https://arxiv.org/abs/2507.15061 | Data: https://huggingface.co/datasets/iic/WebShaper

6. Wu, J., Yin, W., Jiang, Y., et al. (2025). WebWalker: Benchmarking LLMs in Web Traversal. *ACL 2025*. arXiv:2501.07572. https://arxiv.org/abs/2501.07572 | Data: https://huggingface.co/datasets/callanwu/WebWalkerQA

7. Jin, B., Zeng, H., Yue, Z., et al. (2025). Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning. arXiv:2503.09516. https://arxiv.org/abs/2503.09516 | Code: https://github.com/PeterGriffinJin/Search-R1

8. Zhang, Y., Yang, Y., Shu, J., et al. (2025). Agent models: Internalizing Chain-of-Action Generation into Reasoning models. arXiv:2503.06580. https://arxiv.org/abs/2503.06580 | Code: https://github.com/ADaM-BJTU/AutoCoA

