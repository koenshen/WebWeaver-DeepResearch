
# The Evolution of Evaluation Practices for Single-Agent and Multi-Agent Systems Based on Large Language Models (2023–2025): A Literature Review

---

## 1. Introduction

The rapid advancement of large language models (LLMs) has catalyzed a paradigm shift from static text-generation systems to interactive, autonomous agents capable of planning, tool use, multi-turn reasoning, and collaboration. This transition has created an urgent need for robust evaluation frameworks that go beyond traditional NLP metrics. Over the period 2023–2025, research communities have produced a proliferation of benchmarks, sandbox environments, and evaluation protocols for both single-agent and multi-agent systems. This report provides a structured literature review covering four dimensions: (1) benchmarks and sandbox environments, (2) evaluation metrics, (3) implementation and cost considerations, and (4) future directions. Important factual claims are cited with source URLs.

---

## 2. Benchmarks and Sandbox Environments

### 2.1 Single-Agent Benchmarks

**AgentBench** (Liu et al., 2023) is a landmark multi-environment benchmark that evaluates LLM agents across eight distinct environments: operating system, database, knowledge graph, digital card game, lateral thinking puzzles, house-holding (ALFWorld), web shopping (WebShop), and web browsing (Mind2Web). It was designed to assess reasoning and decision-making in multi-turn, open-ended settings. The estimated solving turns per problem range from 5 to 50. A key strength is its **task diversity**; a key limitation is that the environments are closed-box, risking evaluation of API-specific learning rather than general capability. (Source: https://arxiv.org/abs/2308.03688)

**WebArena** (Zhou et al., 2023) provides a self-hostable, realistic web environment with fully functional websites across four domains: e-commerce, social forum discussions, collaborative software development, and content management. It includes tools (e.g., a map) and external knowledge bases (e.g., user manuals). The benchmark tasks evaluate functional correctness via programmatic validation. The best GPT-4-based agent originally achieved only 10.59% success, highlighting the difficulty. **Strengths**: high realism, reproducibility, and long-horizon tasks. **Limitations**: limited to web-based interaction; early versions had lower scalability. (Source: https://arxiv.org/abs/2307.13854; https://webarena.dev)

**SWE-bench** (Jimenez et al., 2024) evaluates LLMs on real-world GitHub issues. Given a codebase and an issue description, the agent must generate a patch that passes manually written unit tests. The original benchmark contains 2,294 instances from 12 Python repositories. **Strengths**: direct relevance to software engineering; tasks are grounded in real-world problems. **Limitations**: evaluation can be noisy due to under-specified issue descriptions or overly specific unit tests. The human-verified subset, **SWE-bench Verified** (OpenAI, August 2024), consists of 500 samples validated by professional developers to address these issues. (Source: https://arxiv.org/abs/2310.06770; https://openai.com/index/introducing-swe-bench-verified)

**GAIA** (Mialon et al., 2023) is a benchmark for general AI assistants containing 450–466 questions requiring multi-step reasoning, web browsing, multimodal understanding, and tool use. Questions are conceptually simple for humans (92% human success) but challenging for AI (15% for GPT-4 with plugins). **Strengths**: real-world grounding, non-gameability, and automatic evaluation with unambiguous answers. **Limitations**: limited to short-form answer tasks; may not fully capture complex agentic workflows. (Source: https://arxiv.org/abs/2311.12983; https://ai.meta.com/research/publications/gaia-a-benchmark-for-general-ai-assistants)

**MINT** (Wang et al., 2023) evaluates LLMs in multi-turn interaction with tools and language feedback. It repurposes existing datasets for reasoning, coding, and decision-making tasks. GPT-4 simulates user feedback. **Strengths**: focus on iterative improvement via feedback; automatic evaluation. **Limitations**: GPT-4-as-simulator may introduce bias; limited task diversity. (Source: https://arxiv.org/abs/2309.10691; https://xwang.dev/mint-bench)

**τ-bench** (Yao et al., 2024) focuses on tool-agent-user interaction in real-world domains (retail and airline). Agents converse with an LLM-simulated user, call domain-specific tools, and follow policy documents. It uses a `pass^k` reliability metric across repeated trials. **Strengths**: dynamic multi-turn interaction; policy compliance evaluation. **Limitations**: limited domain coverage; requires careful user simulation. (Source: https://arxiv.org/abs/2406.12045; https://sierra.ai/blog/benchmarking-ai-agents)

**TheAgentCompany** (Xu et al., 2024) provides an extensible benchmark where agents interact with a simulated software company environment—browsing the web, writing code, running programs, and communicating with coworkers. With 175 tasks, the best agent achieves ~30% full autonomy. **Strengths**: high realism; multi-modal interaction (web, terminal, communication). **Limitations**: complex setup; lower scores for open-weight models. (Source: https://arxiv.org/abs/2412.14161; https://the-agent-company.com)

**RE-Bench** (Wijk et al., 2024) from METR evaluates frontier AI R&D capabilities with 7 challenging ML research engineering environments, comparing agents against human experts (71 attempts by 61 experts). **Strengths**: direct human comparison; open-ended tasks. **Limitations**: small number of tasks; high cost. (Source: https://arxiv.org/abs/2411.15114; https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms)

**AgentQuest** (Gioacchini et al., 2024) is a modular benchmark framework allowing developers to easily integrate multiple benchmarks and metrics. It supports out-of-the-box evaluation across various capabilities and provides base classes for extensibility. **Strengths**: modularity; ease of use. **Limitations**: relies on underlying benchmark quality; primarily a framework rather than a benchmark itself. (Source: https://arxiv.org/abs/2404.06411; https://github.com/nec-research/agentquest)

### 2.2 Multi-Agent Benchmarks and Sandboxes

**AgentSims** (Lin et al., 2023) is an open-source sandbox for evaluating LLMs through task-based simulations in a social environment. Researchers can design evaluation questions at configurable intervals to test specific agent capabilities. **Strengths**: flexible evaluation design; supports social interaction scenarios. **Limitations**: limited scalability; evaluation is QA-based, which may not capture complex behaviors. (Source: https://arxiv.org/abs/2308.04026; https://github.com/py499372727/AgentSims)

**AvalonBench** (Light et al., 2023) evaluates LLMs playing the social deduction game The Resistance: Avalon. It incorporates a game environment, rule-based bots, and ReAct-style LLM agents with role-specific prompts. ChatGPT playing good roles achieved only 22.2% win rate against rule-based bots. **Strengths**: captures complex social reasoning, deception, and collaboration. **Limitations**: single game domain; may not generalize to other multi-agent tasks. (Source: https://arxiv.org/abs/2310.05036; https://github.com/jonathanmli/Avalon-LLM)

**LLM-Deliberation** (Abdelnabi et al., 2023/2024) uses scorable multi-agent, multi-issue negotiation games to evaluate LLM communication and decision-making. Agents must cooperate, compete, or act maliciously based on assigned incentives. **Strengths**: captures nuanced social dynamics; tunable difficulty. **Limitations**: text-based only; evaluation requires multiple metrics. (Source: https://arxiv.org/abs/2309.17234; https://github.com/S-Abdelnabi/LLM-Deliberation)

**CRAB** (Xu et al., 2024, ACL 2025 Findings) is a cross-environment agent benchmark framework supporting multimodal agents across Linux and Android platforms. It introduces a graph-based fine-grained evaluation method and automated task synthesis through sub-task composition. **Strengths**: cross-platform support; fine-grained evaluation; automated task generation. **Limitations**: complex setup; limited to GUI-based environments. (Source: https://arxiv.org/abs/2407.01511; https://www.camel-ai.org/blogs/crab-cross-platform-agent-benchmark)

**BALROG** (Paglieri et al., 2024) and **GAMEBENCH** (Costarelli et al., 2024) are additional multi-agent benchmarks focusing on game-based and collaborative task evaluation. They are referenced in major surveys but have less detailed public documentation. (Source: https://arxiv.org/html/2507.21504v1)

### 2.3 Comparative Analysis: Single-Agent vs. Multi-Agent Benchmarks

| Dimension | Single-Agent Benchmarks | Multi-Agent Benchmarks |
|-----------|------------------------|------------------------|
| **Task Diversity** | High; covers web, code, reasoning, tool use, planning | Moderate; often focused on social interaction, negotiation, or game playing |
| **Scalability** | Generally high; automated evaluation with programmatic checkers | Moderate; requires simulating multiple agents, increasing cost and complexity |
| **Realism** | Varies; GAIA and TheAgentCompany emphasize real-world tasks | Moderate; game-based environments may not fully reflect real-world multi-agent dynamics |
| **Trade-offs** | Simpler evaluation but may miss interactive and social dimensions | Richer social signals but harder to automate evaluation and ensure reproducibility |

**Key insight**: Single-agent benchmarks are maturing rapidly with strong automation and task diversity, while multi-agent benchmarks are still in an earlier stage, often limited to specific game-like scenarios. The trade-off is between **evaluator simplicity and behavioral richness**.

---

## 3. Metrics

### 3.1 Metric Families in Single-Agent Evaluation

**Task Completion Rate (Success Rate):** The most common metric. It measures whether the agent achieves the predefined goal. Used in SWE-bench (passing unit tests), WebArena (functional correctness), GAIA (exact answer match), and AgentBench (goal-based). **Limitation**: binary success/failure provides limited fine-grained insight into partial progress or failure modes. (Source: https://arxiv.org/html/2507.21504v1)

**Pass^k Reliability:** Introduced by τ-bench, this metric reports the probability that an agent succeeds on at least k out of N repeated trials. It captures consistency and reliability, which is critical for enterprise deployment. **Trade-off**: requires multiple runs, increasing cost. (Source: https://arxiv.org/abs/2406.12045)

**String Matching / Exact Match:** Used in GAIA and many closed-form question tasks. Simple, automated, and interpretable. **Limitation**: fails for open-ended or multi-correct-answer tasks.

**Tool Calling Accuracy:** Evaluates whether the agent selects the correct tool and passes correct arguments. Critical in function-calling benchmarks (e.g., BFCL, ToolBench). **Limitation**: does not capture the quality of the overall task execution.

**LLM-as-a-Judge:** A powerful LLM (e.g., GPT-4) evaluates the agent's output based on custom criteria. Used in MINT, AgentQuest, and many RAG evaluation pipelines. **Strengths**: scalable, can handle subjective criteria. **Limitations**: bias toward the judge model's preferences; can be inconsistent; requires additional API calls. (Source: https://arxiv.org/html/2508.02994v1; https://mlflow.org/llm-as-a-judge)

**Agent-as-a-Judge (Zhuge et al., 2024):** An extension where the evaluating agent is embedded in the same environment and can assess process-level quality, not just final output. **Strengths**: better suited for multi-turn and interactive tasks. **Limitations**: more complex to implement; may inherit the same biases. (Source: https://arxiv.org/html/2507.21504v1)

**Human Evaluation:** Used for validation in benchmarks like SWE-bench Verified (93 professional software developers reviewed samples). **Strengths**: gold standard for quality. **Limitations**: expensive, slow, not scalable. (Source: https://epoch.ai/benchmarks/swe-bench-verified)

### 3.2 Metric Families in Multi-Agent Evaluation

**Information Sharing Effectiveness:** Measures how well agents exchange relevant information. Used in AgentSims and AvalonBench.

**Adaptive Role Switching:** Evaluates whether agents can dynamically adjust their roles based on the situation. Used in MATSA and GAMEBENCH.

**Reasoning Rating:** Assesses the quality of reasoning in multi-agent debate or negotiation. Used in LLM-Deliberation.

**Agreement Rate:** In negotiation games, measures whether agents reach a mutually acceptable deal. (Source: https://arxiv.org/abs/2309.17234)

**Win Rate:** In competitive games like Avalon, measures the proportion of games won by the agent's team. (Source: https://arxiv.org/abs/2310.05036)

**Graph-based Fine-grained Evaluation:** Used in CRAB, where tasks are decomposed into sub-tasks, and each sub-task is evaluated independently. This provides partial credit and identifies specific failure modes. **Strengths**: fine-grained, interpretable. **Limitations**: requires task decomposition, which may be non-trivial. (Source: https://arxiv.org/abs/2407.01511)

### 3.3 Comparative Analysis of Metrics

| Metric | Single-Agent | Multi-Agent | Relies On |
|--------|-------------|-------------|-----------|
| Task Completion Rate | Very common | Common | String matching, programmatic check |
| Pass^k | Emerging | Rare | Repeated trials |
| LLM-as-a-Judge | Common | Emerging | LLM judge |
| Agent-as-a-Judge | Rare | Emerging | Agent evaluator |
| Human Evaluation | Validation only | Validation only | Human annotators |
| Graph-based Evaluation | Rare | Used in CRAB | Automated sub-task checking |
| Social/Game-specific Metrics | Rare | Common | Game state, rules |

**Key insight**: Single-agent evaluation is dominated by **task completion** and **tool accuracy** metrics, with growing adoption of **LLM-as-a-Judge** for subjective quality. Multi-agent evaluation relies more on **social interaction metrics** and **graph-based decompositions**, but lacks standardized, widely adopted metrics. The trade-off is between **simplicity and automation** (single-agent) and **behavioral richness** (multi-agent).

---

## 4. Implementation and Cost

### 4.1 Implementation Approaches

**Docker-based environments:** SWE-bench, WebArena, and TheAgentCompany use Docker containers to ensure reproducibility. SWE-bench moved to a fully containerized evaluation harness in June 2024. WebArena provides pre-configured Docker images and even an Amazon Machine Image. (Source: https://www.swebench.com; https://github.com/web-arena-x/webarena)

**Self-hosted sandboxes:** AgentSims and CRAB provide open-source sandbox environments that researchers can deploy locally. AgentSims uses a tick-based simulation system. CRAB supports in-memory, Docker, virtual machine, or distributed physical machine deployment. (Source: https://arxiv.org/abs/2308.04026; https://arxiv.org/abs/2407.01511)

**API-based evaluation:** MINT and τ-bench rely on external LLM APIs (e.g., GPT-4 for user simulation). This introduces cost and dependency on provider availability.

**Graph-based task synthesis:** CRAB automates task generation by combining sub-tasks into complex tasks using a graph-based method, reducing manual effort. (Source: https://arxiv.org/abs/2407.01511)

### 4.2 Human Annotation Involvement

| Benchmark | Human Annotation | Details |
|-----------|----------------|---------|
| SWE-bench | Extensive | Original: manual collection of GitHub issues and unit tests. SWE-bench Verified: 93 developers reviewed 500 samples, each reviewed by 3 annotators. |
| WebArena | Moderate | Human annotators recorded trajectories for ~170 tasks. Task design involved manual specification. |
| GAIA | Extensive | 466 questions were manually designed and validated. Human baseline established (92% success). |
| AgentBench | None | Tasks are automatically derived from existing environments. |
| MINT | None | Uses existing datasets and GPT-4 for user simulation. |
| τ-bench | Moderate | Tasks, databases, and policies are manually designed. |
| TheAgentCompany | Moderate | Synthetic data generation combined with manual task specification. |
| RE-Bench | Extensive | 71 human expert attempts collected for comparison. |
| AvalonBench | None | Rule-based game environment; automated evaluation. |
| LLM-Deliberation | None | Automated game generation and evaluation. |
| CRAB | None | Automated sub-task composition and graph-based evaluation. |
| AgentQuest | None | Modular framework; human annotation depends on the integrated benchmark. |

**Key insight**: Human annotation is most heavily used in benchmarks that aim for high realism and validity (GAIA, SWE-bench Verified, RE-Bench). Fully automated benchmarks (AgentBench, CRAB, MINT) scale better but may suffer from lower task validity or evaluator bias.

### 4.3 Scalability and Reliability

**Scalability challenges:**
- **Cost**: LLM-as-a-Judge evaluation requires additional API calls, increasing cost. 92% of current benchmarks do not measure token usage or API costs (Source: https://www.linkedin.com/posts/raphaelmansuy_survey-on-evaluation-of-llm-based-agents-activity-7308701023554990080-Okfs).
- **Task complexity**: Multi-agent evaluation requires simulating multiple agents, which scales quadratically in cost.
- **Environment setup**: Docker-based environments are reproducible but require significant infrastructure.

**Reliability challenges:**
- **Benchmark exploitation**: Recent work (Moogician, 2026) found that every major agent benchmark can be exploited to achieve near-perfect scores without solving tasks. SWE-bench, WebArena, GAIA, and others were found vulnerable to adversarial attacks on the evaluation harness. (Source: https://moogician.github.io/blog/2026/trustworthy-benchmarks-cont)
- **Inconsistent evaluation**: SWE-bench has known issues with unit test quality and issue description ambiguity. SWE-bench Verified and subsequent validation efforts (e.g., UTBoost) have corrected hundreds of erroneous evaluations. (Source: https://arxiv.org/html/2506.09289v1)
- **Harness dependence**: Different scaffolding/harnesses can produce 10%+ score swings for the same model on SWE-bench. (Source: https://www.reddit.com/r/LocalLLaMA/comments/1qnt8vp/lets_talk_about_the_swebench_verified)

---

## 5. Future Directions

### 5.1 Unified Evaluation Pipelines

The proliferation of benchmarks has created a fragmented landscape. Several concrete directions can advance unified, generalizable evaluation:

**1. Modular Benchmark Frameworks:**
AgentQuest and CRAB demonstrate the value of modular, extensible architectures. Future work should develop a **standardized evaluation protocol** that allows plug-and-play integration of new benchmarks, metrics, and agent architectures. This would reduce duplication and improve comparability across studies.

**2. Unified Multi-Domain Evaluation Suites:**
AgentBench's multi-environment approach is a step in the right direction. Future pipelines should integrate **single-agent, multi-agent, web, code, reasoning, and social interaction** tasks into a single coherent suite with standardized scoring.

**3. Hierarchical Evaluation Metrics:**
Current metrics are either too coarse (binary success/failure) or too fine-grained (step-level accuracy). Future work should develop **hierarchical metrics** that provide both aggregate scores and diagnostic sub-scores for different capabilities (planning, tool use, error recovery, collaboration).

**4. Cost-Aware and Efficiency Metrics:**
92% of current benchmarks do not measure cost. Future evaluation should incorporate **Pareto-optimal frontiers** that trade off task success against token usage, API cost, latency, and number of steps. τ-bench's leaderboard already includes cost information, setting a precedent. (Source: https://hal.cs.princeton.edu/taubench_airline)

**5. Adversarial Robustness Evaluation:**
Given the demonstrated exploitability of current benchmarks, future pipelines must include **adversarial testing** and **canary mechanisms** to detect benchmark gaming. This includes randomized task instances, dynamic evaluation conditions, and validation against known attack vectors. (Source: https://moogician.github.io/blog/2026/trustworthy-benchmarks-cont)

### 5.2 Design Principles for Future Benchmarks

**Principle 1: Realism through Ecological Validity.**
Benchmarks should mimic real-world conditions as closely as possible. TheAgentCompany and GAIA exemplify this by grounding tasks in authentic workplace scenarios and everyday problems. Future benchmarks should incorporate **noise, ambiguity, and partial observability** that characterize real-world deployment.

**Principle 2: Multi-dimensional Evaluation.**
A single success rate is insufficient. Future benchmarks should report **capability profiles** across multiple dimensions: task completion, reliability (pass^k), efficiency (cost/time), safety, robustness, and generalization.

**Principle 3: Automated Validation with Human Oversight.**
Human annotation is essential for validity but expensive. Future pipelines should combine **automated task generation** (as in CRAB) with **human-in-the-loop validation** (as in SWE-bench Verified) to balance scale and quality.

**Principle 4: Dynamic and Interactive Evaluation.**
Static benchmarks risk overfitting and saturation. Future benchmarks should be **dynamic**—incorporating new tasks, varying difficulty, and adapting to agent improvements. LLM-Deliberation's tunable difficulty and CRAB's graph-based task synthesis are promising directions.

**Principle 5: Standardized Reporting.**
The field needs a **minimum reporting standard** for agent evaluations, including: model version, scaffold/harness, hyperparameters, number of trials, cost, and confidence intervals. This would improve reproducibility and comparability across studies.

### 5.3 Open Research Questions

- **How to evaluate multi-agent systems at scale?** Current multi-agent benchmarks are limited to small numbers of agents (2–10). Scalable evaluation for larger agent collectives remains an open problem.
- **How to measure emergent behaviors?** Many important multi-agent behaviors (coordination, specialization, deception) are emergent and difficult to capture with predefined metrics.
- **How to ensure safety in multi-agent evaluation?** No standardized safety tests exist for multi-agent systems. As agents become more capable, safety evaluation becomes critical.
- **How to bridge the gap between benchmark and production?** There is a significant disconnect between benchmark performance and production success (Source: https://galileo.ai/blog/benchmarks-multi-agent-ai). Future work should develop **continuous evaluation pipelines** that monitor agent behavior in production environments.

---

## 6. Conclusion

The period 2023–2025 has witnessed an explosion of evaluation frameworks for LLM-based agents, reflecting the rapid maturation of the field. Single-agent benchmarks have achieved strong automation, diversity, and realism (GAIA, SWE-bench, WebArena), while multi-agent benchmarks are emerging with innovative game-based and collaboration-focused designs (AvalonBench, CRAB, LLM-Deliberation). However, significant challenges remain: metrics are fragmented, benchmarks are vulnerable to exploitation, cost is rarely measured, and multi-agent evaluation lacks standardized protocols. Future progress depends on developing unified, modular, cost-aware, and adversarially robust evaluation pipelines that balance automation with human oversight.

---

## References

1. Liu, X., et al. (2023). AgentBench: Evaluating LLMs as Agents. *arXiv:2308.03688*. https://arxiv.org/abs/2308.03688
2. Zhou, S., et al. (2023). WebArena: A Realistic Web Environment for Building Autonomous Agents. *arXiv:2307.13854*. https://arxiv.org/abs/2307.13854
3. Jimenez, C. E., et al. (2024). SWE-bench: Can Language Models Resolve Real-world Github Issues? *ICLR 2024*. https://arxiv.org/abs/2310.06770
4. OpenAI. (2024). Introducing SWE-bench Verified. https://openai.com/index/introducing-swe-bench-verified
5. Mialon, G., et al. (2023). GAIA: a benchmark for General AI Assistants. *arXiv:2311.12983*. https://arxiv.org/abs/2311.12983
6. Wang, X., et al. (2023). MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback. *ICLR 2024*. https://arxiv.org/abs/2309.10691
7. Yao, S., et al. (2024). τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains. *arXiv:2406.12045*. https://arxiv.org/abs/2406.12045
8. Xu, F. F., et al. (2024). TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks. *arXiv:2412.14161*. https://arxiv.org/abs/2412.14161
9. Wijk, H., et al. (2024). RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts. *arXiv:2411.15114*. https://arxiv.org/abs/2411.15114
10. Gioacchini, L., et al. (2024). AgentQuest: A Modular Benchmark Framework to Measure Progress and Improve LLM Agents. *NAACL 2024*. https://arxiv.org/abs/2404.06411
11. Lin, J., et al. (2023). AgentSims: An Open-Source Sandbox for Large Language Model Evaluation. *arXiv:2308.04026*. https://arxiv.org/abs/2308.04026
12. Light, J., et al. (2023). AvalonBench: Evaluating LLMs Playing the Game of Avalon. *NeurIPS 2023 FMDM Workshop*. https://arxiv.org/abs/2310.05036
13. Abdelnabi, S., et al. (2023). LLM-Deliberation: Evaluating LLMs with Interactive Multi-Agent Negotiation Games. *arXiv:2309.17234*. https://arxiv.org/abs/2309.17234
14. Xu, T., et al. (2024). CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents. *ACL 2025 Findings*. https://arxiv.org/abs/2407.01511
15. Mohammadi, M., et al. (2025). Evaluation and Benchmarking of LLM Agents: A Survey. *arXiv:2507.21504*. https://arxiv.org/html/2507.21504v1
16. Mohammadi, M., et al. (2025). Survey on Evaluation of LLM-based Agents. *arXiv:2503.16416*. https://arxiv.org/abs/2503.16416
17. Sierra AI. (2024). τ-Bench: Benchmarking AI agents for the real-world. https://sierra.ai/blog/benchmarking-ai-agents
18. METR. (2024). Evaluating frontier AI R&D capabilities of language model agents against human experts. https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms
19. Moogician. (2026). How We Broke Top AI Agent Benchmarks: And What Comes Next. https://moogician.github.io/blog/2026/trustworthy-benchmarks-cont
20. Epoch AI. (2024). SWE-bench Verified. https://epoch.ai/benchmarks/swe-bench-verified
21. Rigorous Evaluation of Coding Agents on SWE-Bench. (2025). *arXiv:2506.09289*. https://arxiv.org/html/2506.09289v1
22. CAMEL-AI. (2024). CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents. https://www.camel-ai.org/blogs/crab-cross-platform-agent-benchmark
23. The Reliability Gap: Agent Benchmarks for Enterprise. https://simmering.dev/blog/agent-benchmarks
24. Galileo AI. (2024). Benchmarking Multi-Agent AI: Insights & Practical Use. https://galileo.ai/blog/benchmarks-multi-agent-ai
25. ACM. (2025). Survey of Emerging Trends in LLM Agent Benchmarking. https://dl.acm.org/doi/10.1145/3784013.3784018
26. Arize AI. (2025). LLM as a Judge - Primer and Pre-Built Evaluators. https://arize.com/guides/llm-as-a-judge
27. DeepEval. (2026). LLM-as-a-Judge in 2026: Top evaluation techniques. https://deepeval.com/blog/llm-as-a-judge
28. When AIs Judge AIs: The Rise of Agent-as-a-Judge Evaluation for LLMs. (2025). *arXiv:2508.02994*. https://arxiv.org/html/2508.02994v1
29. SWE-bench Official Site. https://www.swebench.com
30. WebArena Official Site. https://webarena.dev
31. GAIA Leaderboard. https://hal.cs.princeton.edu/gaia
32. τ-bench Leaderboard. https://hal.cs.princeton.edu/taubench_airline
33. TheAgentCompany GitHub. https://github.com/TheAgentCompany/TheAgentCompany
34. RE-Bench GitHub. https://github.com/METR/RE-Bench
35. AgentQuest GitHub. https://github.com/nec-research/agentquest
36. CRAB GitHub. https://github.com/camel-ai/crab

