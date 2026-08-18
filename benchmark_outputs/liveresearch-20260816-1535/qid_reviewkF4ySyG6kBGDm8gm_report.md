
# Routing for Large Language Models: A Literature Review

## 1. Introduction

As large language models (LLMs) have scaled to hundreds of billions of parameters, the question of *how to route*—whether dispatching tokens to specialized sub-networks within a single model, or directing queries to different models, strategies, and configurations—has become a central concern in the field. This review traces the evolution of routing research from 2022 to 2025 across two complementary axes: (i) expert routing within Mixture-of-Experts (MoE) architectures, and (ii) broader routing paradigms that allocate queries across models, adaptation methods, retrieval depths, decoding strategies, and multi-agent controllers. We focus exclusively on papers published at top AI conferences and journals.

## 2. Expert Routing in Mixture-of-Experts Architectures

### 2.1 From Token-Choice to Expert-Choice and Soft Routing

The early 2022 landscape was dominated by sparse MoE architectures employing fixed top-*k* token-to-expert routing, as exemplified by GShard (Lepikhin et al., 2021) and Switch Transformer (Fedus et al., 2022). A fundamental limitation of these approaches is that every token is forced to activate a fixed number of experts, regardless of its complexity or informational content. Clark et al. (2022) provided a theoretical foundation for understanding these trade-offs, deriving unified scaling laws for routed language models that characterize performance as a function of both base model size and expert count. Their analysis, presented at ICML 2022, revealed that the performance gains from routing follow a saturating function of the number of experts, with diminishing returns beyond a certain threshold.

The first major paradigm shift came with **Expert Choice Routing** (Zhou et al., NeurIPS 2022) [https://proceedings.neurips.cc/paper_files/paper/2022/hash/2f00ecd787b432c1d36f3de9800728eb-Abstract-Conference.html]. Instead of having *tokens select the top-*k* experts*, Zhou et al. inverted the routing mechanism: *experts select the top-*k* tokens*. This reversal guarantees perfect load balancing without auxiliary loss terms, as each expert receives a fixed bucket size. Tokens are naturally routed to a variable number of experts, enabling heterogeneous computation. The authors demonstrated a 2× improvement in training convergence over GShard and Switch Transformer, and superior fine-tuning performance on 11 GLUE and SuperGLUE tasks. Expert Choice Routing established that the routing perspective—who does the selecting—matters profoundly for both training stability and efficiency.

Building on this insight, **Soft MoE** (Puigcerver et al., ICLR 2024) [https://proceedings.iclr.cc/paper_files/paper/2024/file/79fea214543ba263952ac3f4e5452b14-Paper-Conference.pdf] took the next logical step: replacing discrete token-to-expert assignments with fully differentiable, continuous routing. Instead of dispatching subsets of tokens to experts, Soft MoE passes convex combinations of all input tokens to each expert. Each expert processes a learned weighted average of tokens, and the dispatch weights are learned end-to-end. This eliminates two fundamental problems of sparse MoE—token dropping and expert imbalance—while remaining fully differentiable. Applied to Vision Transformers, Soft MoE-Base/16 achieved 10.5× lower inference cost (5.7× lower wall-clock time) than ViT-Huge/14 at matching performance. The Soft MoE framework demonstrated that the hard, discrete routing decisions of traditional MoE are not a necessary evil, but rather a design choice that can be replaced with smoother alternatives.

### 2.2 Fine-Grained and Shared Expert Architectures

A parallel line of work questioned the granularity at which expert specialization occurs. While standard MoE layers partition the feedforward network into a small number (e.g., 8 or 16) of large experts, **DeepSeekMoE** (Dai et al., ACL 2024) [https://aclanthology.org/2024.acl-long.70.pdf] argued that finer-grained expert segmentation could dramatically improve specialization. The key insight is combinatorial: with 16 experts and top-2 routing, only 120 expert combinations exist; by splitting each expert into 4 smaller experts and activating 8, the number of possible combinations explodes to over 4.4 billion. DeepSeekMoE combines this fine-grained segmentation with *shared expert isolation*, where a small number of experts are always activated to capture common knowledge, while routed experts handle specialized patterns. This architecture achieved comparable performance to LLaMA2 7B with only 40% of the computation, demonstrating that expert granularity and architectural structure are critical design dimensions. The DeepSeekMoE architecture was subsequently scaled to 236B total parameters in DeepSeek-V2, which further integrated low-rank compression for KV cache efficiency.

The idea of structured expert sharing was further extended by **Multi-Head Mixture-of-Experts (MH-MoE)** (Wu et al., NeurIPS 2024) [https://neurips.cc/virtual/2024/poster/94304]. MH-MoE splits each input token into multiple sub-tokens (analogous to multi-head attention), assigns each sub-token to a different expert, and then reintegrates the processed representations. This mechanism increases expert activation diversity—each token effectively engages multiple experts across different representation subspaces—without increasing the number of activated parameters per token. MH-MoE demonstrated significant improvements over standard sparse MoE across a range of language understanding tasks, particularly when scaling to larger numbers of experts.

### 2.3 Dynamic and Adaptive Expert Allocation

A persistent limitation of top-*k* routing is its static nature: every token, regardless of difficulty, activates the same number of experts. **"Harder Task Needs More Experts: Dynamic Routing in MoE Models"** (Huang et al., ACL 2024) [https://aclanthology.org/2024.acl-long.696.pdf] directly addressed this by introducing a cumulative-thresholding mechanism that selects experts based on the cumulative probability distribution of routing scores. The router sorts expert probabilities in descending order and activates experts until the cumulative probability exceeds a threshold *p*. This allows simpler tokens to activate fewer experts (sometimes just one), while harder tokens can activate more. Across five downstream tasks, the dynamic model activated an average of 1.76 experts per token—fewer than the fixed 2 of top-2 routing—while maintaining or improving performance. The authors further observed that the average number of activated experts naturally decreases during training, suggesting that the model learns to be more discriminative over time.

The theme of adaptive computation was extended to the *depth* dimension by **Mixture-of-Depths (MoD)** (Raposo et al., 2024). MoD equips each transformer block with a router that determines which tokens should undergo full computation (self-attention and MLP) and which can take a residual skip. This is conceptually analogous to MoE, but with "experts" being entire transformer blocks rather than feedforward sub-networks. MoD demonstrated that transformers can learn to dynamically allocate FLOPs to specific token positions, achieving up to 50% reduction in per-forward-pass computation at iso-performance. The approach is complementary to MoE and can be combined with it, suggesting a future where both width (expert selection) and depth (layer selection) are dynamically routed.

**Ada-K Routing** (Zhao et al., ICLR 2025) [https://iclr.cc/virtual/2025/poster/30715] proposed a learnable allocator module that determines the number of activated experts per token using reinforcement learning (PPO). Unlike thresholding-based methods, Ada-K allocators are fully pluggable, making them applicable to any existing MoE-based LLM without architectural modification. The allocator takes the token representation as input and outputs a customized expert count, enabling the model to trade off computation and performance on a per-token basis. Analysis revealed that harder tasks, middle transformer layers, and content words (as opposed to function words) tend to activate more experts, providing interpretable insights into how MoE models allocate computational resources.

### 2.4 Differentiable and Scalable Routing Mechanisms

The non-differentiability of the top-*k* operator has long been recognized as a fundamental limitation of sparse MoE. **ReMoE: Fully Differentiable Mixture-of-Experts with ReLU Routing** (Wang et al., ICLR 2025) [https://arxiv.org/abs/2412.14711] proposed a remarkably simple yet effective solution: replace the Softmax+TopK router with a ReLU activation. The ReLU function naturally produces sparse outputs (zeroing out negative values), and crucially, it is fully differentiable. The sparsity level is controlled via an adaptive L1 regularization that targets a desired budget. ReMoE consistently outperformed vanilla TopK-routed MoE across model sizes from 182M to 978M parameters, expert counts from 4 to 128, and varying granularities. Moreover, ReMoE exhibited superior scalability with respect to the number of experts, as the fully differentiable routing allows gradients to flow through all experts, preventing the "dead expert" problem that plagues sparse MoE when experts are rarely selected.

**Dynamic Mixture of Experts (DynMoE)** (Guo et al., ICLR 2025) [https://arxiv.org/abs/2405.14297] took a different approach to the same problem. Rather than enforcing sparsity through a discrete operator, DynMoE introduces a gating mechanism that allows each token to be processed by *all* experts, but with weights learned through an auto-tuning framework. The key innovation is a temperature-based gating function that can be adjusted during training to control the degree of expert specialization. Unlike traditional MoE where the number of activated experts is a hyperparameter, DynMoE learns the optimal routing strategy as part of training. The method demonstrated consistent improvements across language, vision, and vision-language tasks, suggesting that the hard sparsity constraint of traditional MoE may be suboptimal.

### 2.5 Scaling and System-Level Routing Innovations

The transition from research prototypes to production-scale MoE systems has driven several architectural innovations. **Mixtral 8x7B** (Jiang et al., 2024) demonstrated that a sparse MoE with 8 experts and top-2 routing, totaling 46.7B parameters but activating only 12.9B, could match or exceed the performance of dense models like LLaMA 2 70B while offering 6× faster inference. Mixtral validated that MoE routing could deliver on its promise of dense-model quality at sparse-model cost, and it became a widely adopted open-weight model.

**Branch-Train-MiX (BTX)** (Sukhbaatar et al., ICML 2024) [https://arxiv.org/abs/2403.07816] introduced a novel training paradigm for multi-domain MoE. Rather than training a single MoE model from scratch, BTX starts from a seed dense model, branches it to train expert LLMs in embarrassingly parallel fashion on distinct data domains (e.g., coding, math, Wikipedia), and then merges the experts by placing their feedforward parameters into MoE layers. A lightweight MoE fine-tuning stage learns token-level routing. This approach dramatically reduces communication costs and enables asynchronous training of domain experts. BTX suggests that routing can be applied not just at inference time, but also as a framework for distributed training.

**MoEUT: Mixture-of-Experts Universal Transformers** (Csordás et al., NeurIPS 2024) [https://proceedings.neurips.cc/paper_files/paper/2024/hash/321387ba926b8e58d3591c0aeb52ffc2-Abstract-Conference.html] combined MoE routing with Universal Transformers (weight-shared across layers). MoEUT applies MoE to both feedforward and attention layers, and introduces novel layer-normalization and grouping schemes. For the first time, a shared-layer Transformer design achieved competitive performance on language modeling tasks (BLiMP, PIQA) while using significantly less compute and memory. This work suggests that routing can enable parameter reuse across layers without sacrificing representational capacity.

## 3. Broader Routing Paradigms: Query Allocation Across Models and Strategies

### 3.1 Ensemble and Cascade Routing

While MoE routing operates within a single model, a complementary line of research considers routing across *multiple independently trained LLMs*, each with different capabilities, costs, and latencies. The goal is to match each query to the most appropriate model, balancing quality and cost.

**LLM-Blender** (Jiang et al., ACL 2023) [https://aclanthology.org/2023.acl-long.792] was an early and influential framework for ensembling LLMs. It operates in two stages: first, a *Pairwise Ranking Model* (PaRM) compares the outputs of candidate LLMs in a pairwise manner; second, a *Generative Fusion* model (GenF) synthesizes the top-ranked outputs into a final response. LLM-Blender demonstrated that no single open-source LLM consistently outperforms others across all inputs, and that ensembling can achieve consistently superior performance. The key insight is that ranking is more reliable when done in a pairwise, comparative fashion rather than through absolute scoring.

**FrugalGPT** (Chen et al., TMLR 2024) [https://jmlr.org/tmlr/papers] introduced the cascade paradigm, where queries are first directed to a cheap, small model; if the small model's response is deemed unreliable (via self-verification), the query is escalated to a larger, more expensive model. This *LLM cascade* approach was shown to reduce costs by up to 98% while maintaining the performance of cutting-edge models like GPT-4. FrugalGPT formalized the cost-quality trade-off as a learnable optimization problem, where the cascade structure (which models to use, in what order, and at what confidence thresholds) is learned from data.

### 3.2 Quality-Aware and Preference-Based Routing

The cascade paradigm was refined by **Hybrid LLM** (Ding et al., ICLR 2024) [https://proceedings.iclr.cc/paper_files/paper/2024/file/b47d93c99fa22ac0b377578af0a1f63a-Paper-Conference.pdf], which introduced a quality-aware router that predicts the *response quality gap* between a small and large model for each query. Rather than relying on self-verification (which can be noisy), Hybrid LLM trains a separate router to estimate how much better the large model will perform on a given query. The router can be tuned at test time to achieve different cost-quality trade-offs. Hybrid LLM demonstrated that 40% of calls to the large model could be eliminated with no drop in response quality, and that the router's predictions generalize across different model pairs.

**RouteLLM** (Ong et al., ICLR 2025) [https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html] advanced the state of the art by framing routing as a learning problem from *human preference data*. Rather than relying on annotated quality scores (which are expensive and subjective), RouteLLM leverages the vast amounts of pairwise preference data generated by platforms like Chatbot Arena. The router is trained to predict which model a human would prefer for a given query, using techniques including matrix factorization, SW ranking, and fine-tuned classifiers. RouteLLM achieved 85% cost reduction on MT-Bench while maintaining 95% of GPT-4 performance, sending only 14% of queries to the expensive model. The framework was released as an open-source serving system, establishing a practical infrastructure for deploying LLM routers.

**AutoMix** (Aggarwal et al., NeurIPS 2024) [https://neurips.cc/virtual/2024/poster/94293] combined the strengths of self-verification and principled decision-making under uncertainty. AutoMix uses a few-shot self-verification mechanism to estimate the reliability of a small model's output, and then employs a Partially Observable Markov Decision Process (POMDP) to decide whether to accept the small model's answer or route to a larger model. The POMDP formulation naturally handles the uncertainty inherent in self-verification, which can be noisy. AutoMix consistently reduced computational cost by over 50% for comparable performance across five language models and five challenging datasets, demonstrating that principled uncertainty modeling improves routing decisions.

### 3.3 Routing Benchmarks, Evaluation, and Controllable Systems

As the field matured, the need for standardized evaluation became apparent. **RouterBench** (Hu et al., ICML Workshop 2024) [https://icml.cc/virtual/2024/39041] introduced the first comprehensive benchmark for multi-LLM routing systems, comprising over 405,000 inference outcomes from 11 representative LLMs across 64 tasks. RouterBench provides a cost-quality analytic framework using metrics like AIQ and convex hull operations to compare routing strategies. The benchmark revealed that no single routing strategy dominates across all cost-quality regimes, and that the optimal strategy depends on the specific task distribution and cost constraints of the deployment.

**TensorOpera Router** (Stripelis et al., EMNLP 2024) addressed the system-level challenges of deploying routers in production, proposing a multi-model inference serving system that dynamically selects the optimal LLM for each query based on both query characteristics and system state (e.g., GPU utilization, queue lengths). This work highlighted that routing decisions in practice must consider not only model quality and cost, but also latency, throughput, and hardware constraints.

### 3.4 Unified Frameworks and Advanced Routing Strategies

A significant theoretical advance came from **A Unified Approach to Routing and Cascading for LLMs** (Dekoninck et al., ICML 2025) [https://proceedings.mlr.press/v267/dekoninck25a.html], which derived optimal strategies for both routing and cascading and proved their optimality conditions. The key insight is that routing (selecting one model per query) and cascading (running models sequentially until a satisfactory answer is obtained) are not mutually exclusive but can be combined. Dekoninck et al. introduced *cascade routing*, a unified framework that iteratively picks the best model, allowing models to be skipped, reordered, or run as few as necessary. This approach consistently outperformed both pure routing and pure cascading, and the theoretical analysis clarified the conditions under which each strategy is optimal.

**Self-REF: Learning to Route LLMs with Confidence Tokens** (Chuang et al., ICML 2025) [https://proceedings.mlr.press/v267/chuang25b.html] introduced a lightweight fine-tuning strategy that teaches LLMs to express their confidence through special *confidence tokens*. The model is trained to output a confidence token (e.g., "CONFIDENT" or "UNCERTAIN") alongside its answer, and the confidence score is extracted from the token's embedding. Self-REF demonstrated that intrinsic confidence signals can be learned more reliably than post-hoc methods (e.g., verbalized confidence or examining token probabilities). The confidence scores were then used for routing and rejection learning, outperforming prior approaches on four datasets and two base LLMs. This work suggests that routing signals can be *internalized* by models rather than requiring external classifiers.

### 3.5 Multi-Agent and Modular Controllers

The final frontier of routing research involves deploying LLMs as agents that can dynamically compose tools, call sub-models, and orchestrate multi-step reasoning. **Router-R1** (Zhang et al., 2025) [https://neurips.cc/virtual/2025/poster/119214] formulated multi-LLM routing as a reinforcement learning problem where the router itself is an LLM that interleaves "think" actions (internal deliberation) with "route" actions (dynamic model invocation). The router can call multiple models sequentially, aggregate their responses, and maintain an evolving context. Router-R1 uses a lightweight rule-based reward combining format rewards, outcome rewards, and cost penalties, trained via RL. This approach enables complex tasks that require the complementary strengths of multiple LLMs, such as fact-checking claims by first querying a retrieval model, then a reasoning model, and finally a verification model.

The broader multi-agent routing landscape has seen significant activity at NeurIPS 2024. **Chain-of-Agents (CoA)** (Zhang et al., 2024) [https://neurips.cc/virtual/2024/poster/95563] introduced a framework where multiple worker agents sequentially process different segments of a long-context input, passing information through natural language, with a manager agent synthesizing the contributions. This is effectively a routing mechanism where the *information flow* between agents is dynamically determined by the content. **Multi-Agent Collaboration via Evolving Orchestration** (Dang et al., 2025) [https://neurips.cc/virtual/2025/poster/118584] proposed a "puppeteer" paradigm where a centralized orchestrator dynamically directs specialized agents in response to evolving task states, trained via reinforcement learning to adaptively sequence and prioritize agents. These works suggest that routing is evolving from a one-shot model selection problem to a dynamic, multi-step orchestration challenge.

## 4. Discussion and Future Directions

The 2022–2025 period has witnessed a remarkable evolution in routing for LLMs. Within MoE architectures, the trajectory has been from discrete, fixed routing (top-*k*) to increasingly flexible mechanisms: expert-choice routing (variable experts per token), soft routing (fully differentiable assignments), dynamic routing (input-dependent expert counts), and fine-grained expert architectures (increased combinatorial flexibility). The common thread is the move toward computation that is *truly conditional* on the input, rather than being determined by fixed architectural hyperparameters.

In the broader routing paradigm, the field has progressed from simple heuristics (send everything to the strongest model) to sophisticated learned routers that leverage human preferences, confidence signals, uncertainty modeling, and reinforcement learning. The unification of routing and cascading into a single theoretical framework, and the extension of routing to multi-agent orchestration, point toward a future where LLM systems are not monolithic but composed of dynamically assembled components.

Several open challenges remain. First, the interaction between MoE-style routing (within a model) and query-level routing (across models) is underexplored: could a single architecture support both forms of routing? Second, the computational overhead of the router itself—which can be non-trivial for complex models like Router-R1—needs to be minimized. Third, the theoretical understanding of when routing is beneficial, and for which types of queries, remains incomplete. Finally, the deployment of routing systems in production requires addressing fairness, robustness, and safety concerns that arise when different queries are handled by different models.

## References

1. Zhou, Y., Lei, T., Liu, H., Du, N., Huang, Y., Zhao, V., Dai, A., Chen, Z., Le, Q., & Laudon, J. (2022). Mixture-of-Experts with Expert Choice Routing. *NeurIPS 2022*. https://proceedings.neurips.cc/paper_files/paper/2022/hash/2f00ecd787b432c1d36f3de9800728eb-Abstract-Conference.html

2. Puigcerver, J., Riquelme, C., Mustafa, B., & Houlsby, N. (2024). From Sparse to Soft Mixtures of Experts. *ICLR 2024*. https://proceedings.iclr.cc/paper_files/paper/2024/file/79fea214543ba263952ac3f4e5452b14-Paper-Conference.pdf

3. Clark, A., de las Casas, D., Guy, A., Mensch, A., Paganini, M., Hoffmann, J., Damoc, B., Hechtman, B., Cai, T., Borgeaud, S., et al. (2022). Unified Scaling Laws for Routed Language Models. *ICML 2022*. https://proceedings.mlr.press/v162/clark22a/clark22a.pdf

4. Dai, D., Deng, C., Zhao, C., Xu, R.X., Gao, H., Chen, D., Li, J., Zeng, W., Yu, X., Wu, Y., et al. (2024). DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models. *ACL 2024*. https://aclanthology.org/2024.acl-long.70.pdf

5. Wu, X., Huang, S., Wang, W., Ma, S., Dong, L., & Wei, F. (2024). Multi-Head Mixture-of-Experts. *NeurIPS 2024*. https://neurips.cc/virtual/2024/poster/94304

6. Huang, Q., An, Z., Zhuang, N., Tao, M., Zhang, C., Jin, Y., Xu, K., Chen, L., Huang, S., & Feng, Y. (2024). Harder Task Needs More Experts: Dynamic Routing in MoE Models. *ACL 2024*. https://aclanthology.org/2024.acl-long.696.pdf

7. Raposo, D., Ritter, S., Richards, B., Lillicrap, T., Humphreys, P.C., & Santoro, A. (2024). Mixture-of-Depths: Dynamically allocating compute in transformer-based language models. *arXiv:2404.02258*.

8. Zhao, Z., Guo, L., Cheng, J., Gao, X., Huang, H., & Liu, J. (2025). Ada-K Routing: Boosting the Efficiency of MoE-based LLMs. *ICLR 2025*. https://iclr.cc/virtual/2025/poster/30715

9. Wang, Z., Zhu, J., & Chen, J. (2025). ReMoE: Fully Differentiable Mixture-of-Experts with ReLU Routing. *ICLR 2025*. https://arxiv.org/abs/2412.14711

10. Guo, Y., Cheng, Z., Tang, X., Tu, Z., & Lin, T. (2025). Dynamic Mixture of Experts: An Auto-Tuning Approach for Efficient Transformer Models. *ICLR 2025*. https://arxiv.org/abs/2405.14297

11. Csordás, R., Irie, K., Schmidhuber, J., Potts, C., & Manning, C.D. (2024). MoEUT: Mixture-of-Experts Universal Transformers. *NeurIPS 2024*. https://proceedings.neurips.cc/paper_files/paper/2024/hash/321387ba926b8e58d3591c0aeb52ffc2-Abstract-Conference.html

12. Jiang, D., Ren, X., & Lin, B.Y. (2023). LLM-Blender: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion. *ACL 2023*. https://aclanthology.org/2023.acl-long.792

13. Chen, L., Zaharia, M., & Zou, J. (2024). FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance. *TMLR 2024*. https://jmlr.org/tmlr/papers

14. Ding, D., Mallick, A., Wang, C., Sim, R., Mukherjee, S., Ruhle, V., Lakshmanan, L.V.S., & Awadallah, A. (2024). Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing. *ICLR 2024*. https://proceedings.iclr.cc/paper_files/paper/2024/file/b47d93c99fa22ac0b377578af0a1f63a-Paper-Conference.pdf

15. Ong, I., Almahairi, A., Wu, V., Chiang, W.-L., Wu, T., Gonzalez, J.E., Kadous, M.W., & Stoica, I. (2025). RouteLLM: Learning to Route LLMs from Preference Data. *ICLR 2025*. https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html

16. Aggarwal, P., Madaan, A., Anand, A., Potharaju, S.P., Mishra, S., Zhou, P., Gupta, A., Rajagopal, D., Kappaganthu, K., Yang, Y., et al. (2024). AutoMix: Automatically Mixing Language Models. *NeurIPS 2024*. https://neurips.cc/virtual/2024/poster/94293

17. Hu, Q., et al. (2024). RouterBench: A Benchmark for Multi-LLM Routing System. *ICML Workshop 2024*. https://icml.cc/virtual/2024/39041

18. Stripelis, D., Xu, Z., Hu, Z., Shah, A.D., Jin, H., Yao, Y., Zhang, J., Zhang, T., Avestimehr, S., & He, C. (2024). TensorOpera Router: A Multi-Model Router for Efficient LLM Inference. *EMNLP 2024*.

19. Dekoninck, J., Baader, M., & Vechev, M. (2025). A Unified Approach to Routing and Cascading for LLMs. *ICML 2025*. https://proceedings.mlr.press/v267/dekoninck25a.html

20. Chuang, Y.-N., Sarma, P.K., Gopalan, P., Boccio, J., Bolouki, S., Hu, X., & Zhou, H. (2025). Learning to Route LLMs with Confidence Tokens. *ICML 2025*. https://proceedings.mlr.press/v267/chuang25b.html

21. Zhang, H., Feng, T., & You, J. (2025). Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning. *NeurIPS 2025*. https://neurips.cc/virtual/2025/poster/119214

22. Zhang, Y., Sun, R., Chen, Y., Pfister, T., Zhang, R., & Arik, S. (2024). Chain of Agents: Large Language Models Collaborating on Long-Context Tasks. *NeurIPS 2024*. https://neurips.cc/virtual/2024/poster/95563

23. Dang, Y., Qian, C., Luo, X., Fan, J., Xie, Z., Shi, R., Chen, W., Yang, C., Che, X., Tian, Y., et al. (2025). Multi-Agent Collaboration via Evolving Orchestration. *NeurIPS 2025*. https://neurips.cc/virtual/2025/poster/118584

24. Jiang, A.Q., Sablayrolles, A., Roux, A., Mensch, A., Savary, B., Bamford, C., Chaplot, D.S., et al. (2024). Mixtral of Experts. *arXiv:2401.04088*.

25. Sukhbaatar, S., Golovneva, O., Sharma, V., Xu, H., Lin, X.V., Rozière, B., Kahn, J., Li, D., tau Yih, W., Weston, J., & Li, X. (2024). Branch-Train-MiX: Mixing Expert LLMs into a Mixture-of-Experts LLM. *ICML 2024*. https://arxiv.org/abs/2403.07816

26. Fedus, W., Zoph, B., & Shazeer, N. (2022). Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity. *JMLR*, 23(1):5232–5270.

27. Lepikhin, D., Lee, H., Xu, Y., Chen, D., Firat, O., Huang, Y., Krikun, M., Shazeer, N., & Chen, Z. (2021). GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding. *ICLR 2021*.

28. Du, N., Huang, Y., Dai, A.M., Tong, S., Lepikhin, D., Xu, Y., Krikun, M., Zhou, Y., Yu, A.W., Firat, O., et al. (2022). GLaM: Efficient Scaling of Language Models with Mixture-of-Experts. *ICML 2022*.

29. Zoph, B., Bello, I., Kumar, S., Du, N., Huang, Y., Dean, J., Shazeer, N., & Fedus, W. (2022). ST-MoE: Designing Stable and Transferable Sparse Expert Models. *arXiv:2202.08906*.

30. Shazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., & Dean, J. (2017). Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer. *ICLR 2017*.
