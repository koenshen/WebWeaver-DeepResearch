
# Hallucination Detection in Large Language Models: A Literature Review

## 1. Introduction

The propensity of large language models (LLMs) to generate plausible yet factually incorrect content—commonly referred to as hallucination—has emerged as one of the most critical barriers to their reliable deployment. The period from 2023 to 2025 has witnessed an explosion of research dedicated to detecting, measuring, and understanding hallucinations, spanning benchmark construction, uncertainty quantification, internal state probing, and theoretical analysis. This review systematically traces the evolution of these complementary lines of inquiry, covering empirical detection algorithms, evaluation frameworks, interpretability-driven methods, and foundational theoretical insights.

## 2. Benchmarking Hallucination: From Coarse-Grained to Fine-Grained Evaluation

The development of rigorous benchmarks has been a prerequisite for progress in hallucination detection. Early efforts focused on constructing large-scale, multi-task evaluation suites. Li et al. (2023) introduced **HaluEval**, a benchmark comprising 35,000 samples across question answering (QA), knowledge-grounded dialogue, and summarization, with both automatically generated and human-annotated hallucinated instances. Their evaluation revealed that even ChatGPT achieved only 62.59% accuracy on QA hallucination recognition, highlighting the difficulty of the task, while providing external knowledge boosted performance to 76.83% (https://aclanthology.org/2023.emnlp-main.397).

A parallel line of work sought to move beyond binary judgments toward more granular evaluation. Min et al. (2023) proposed **FActScore**, which decomposes long-form generations into atomic facts and computes the percentage of facts supported by a reliable knowledge source. Applied to biography generation, the metric revealed that ChatGPT achieves only 58% factual precision, and the automated estimator achieved under 2% error rate relative to human annotation (https://aclanthology.org/2023.emnlp-main.741). This atomic-fact paradigm has been widely adopted in subsequent work.

The need for domain-specific and automatically verifiable benchmarks led to further innovations. Oh et al. (2024) presented **ERBench**, which converts any relational database with entity-relationship constraints into an LLM benchmark, enabling continuous evaluation and verification of both answer correctness and reasoning quality (https://neurips.cc/virtual/2024/poster/97458). In the financial domain, Ji et al. (2025) introduced **PHANTOM**, a benchmark for long-context financial QA that captures the complexities of numerical precision and domain-specific language, demonstrating that out-of-the-box models severely struggle with real-world hallucinations in high-stakes settings (https://neurips.cc/virtual/2025/poster/121830). Bang et al. (2025) contributed **HalluLens**, a comprehensive benchmark synthesizing multiple hallucination types across diverse tasks (https://aclanthology.org/2025.acl-long.1176).

Complementing these evaluation-oriented benchmarks, Ji et al. (2024) introduced **ANAH**, a bilingual dataset providing analytical annotation of hallucinations at the sentence level, covering hallucination type classification, reference retrieval, and content correction across ~12,000 sentence-level annotations for ~4,300 LLM responses (https://aclanthology.org/2024.acl-long.442). The subsequent ANAH-v2 scaled this to ~822,000 annotated sentences using an iterative self-training framework, producing a 7B-parameter annotator that surpassed GPT-4 in zero-shot hallucination detection on HaluEval (https://neurips.cc/virtual/2024/poster/95407).

## 3. Uncertainty-Based Detection: From Token Probabilities to Semantic Entropy

A foundational approach to hallucination detection exploits the intuition that models are uncertain when they hallucinate. Manakul et al. (2023) proposed **SelfCheckGPT**, a zero-resource black-box method that samples multiple responses from an LLM and measures inconsistency: factual sentences yield similar sampled passages, while hallucinated sentences cause divergence. Their approach achieved considerably higher AUC-PR scores than grey-box methods on the WikiBio dataset (https://aclanthology.org/2023.emnlp-main.557). Zhang et al. (2023) enhanced uncertainty-based detection by focusing on three aspects mimicking human factuality checking: informative keywords, unreliable tokens in historical context, and token properties such as type and frequency, achieving state-of-the-art results without requiring external knowledge (https://aclanthology.org/2023.emnlp-main.58).

A significant theoretical advance came with the introduction of **semantic entropy** by Farquhar, Kossen, Kuhn, and Gal (2024). Rather than measuring uncertainty over token sequences, which conflates lexical variation with factual uncertainty, semantic entropy clusters semantically equivalent generations before computing entropy. This unsupervised method, published in *Nature*, demonstrated robust detection of confabulations across diverse domains and generalized better to out-of-distribution inputs than supervised alternatives (https://www.nature.com/articles/s41586-024-07421-0). However, the computational cost of semantic entropy—requiring 5–10 model generations per query—motivated Kossen et al. (2024) to propose **Semantic Entropy Probes (SEPs)**, which train linear probes on LLM hidden states to approximate semantic entropy from a single generation. SEPs retain high detection performance while reducing overhead to nearly zero, and generalize better to out-of-distribution data than probes trained directly on accuracy (https://icml.cc/virtual/2024/39442).

## 4. Internal State Probing: Leveraging Representations for Hallucination Detection

A rapidly growing line of research investigates whether LLMs' internal representations encode signals that can predict hallucination. Chen et al. (2024) proposed **INSIDE**, a framework that leverages internal hidden states for hallucination detection. They introduced **EigenScore**, a metric that computes the eigenvalues of the covariance matrix of multiple response embeddings in the dense representation space, measuring semantic consistency. A test-time feature clipping technique truncates extreme activations to mitigate overconfident generations. EigenScore achieved AUROC improvements of up to 8.9% over lexical similarity baselines on the SQuAD dataset (https://iclr.cc/virtual/2024/poster/18385).

Sriramanan et al. (2024) presented **LLM-Check**, which analyzes attention maps, hidden activations, and output probabilities from a single forward pass, achieving speedups of up to 45–450× over consistency-based methods while maintaining strong detection performance across diverse settings including RAG (https://neurips.cc/virtual/2024/poster/95584). Du et al. (2024) introduced **HaloScope**, a NeurIPS 2024 spotlight that addresses the critical challenge of labeled data scarcity by leveraging unlabeled LLM generations. The framework estimates membership (truthful vs. hallucinated) via embedding factorization to identify a hallucination subspace, then trains a binary classifier. HaloScope outperforms competitive rivals without requiring extra data collection or human annotations (https://neurips.cc/virtual/2024/poster/93676).

Chuang et al. (2024) proposed the **Lookback Lens**, a remarkably simple yet effective method that detects contextual hallucinations using only attention maps. The detector computes the ratio of attention weights on context versus newly generated tokens for each attention head, and trains a linear classifier on these features. This approach transfers across tasks and even across model sizes (e.g., from 7B to 13B) without retraining, and a guided decoding variant reduces hallucinations by 9.6% on the XSum summarization task (https://aclanthology.org/2024.emnlp-main.84). Su et al. (2024) further demonstrated that unsupervised real-time hallucination detection is feasible using only internal states, without requiring annotated data (https://aclanthology.org/2024.findings-acl.854).

## 5. LLM-as-Judge and Learning-Based Evaluation for Factual Consistency

A parallel thread has focused on training specialized models to evaluate factual consistency, particularly for summarization. Zha et al. (2023) proposed **AlignScore**, a unified alignment function trained on a diverse set of textual entailment and fact verification datasets. Based on RoBERTa, AlignScore achieved state-of-the-art results on the SummaC and TRUE benchmarks, with the large variant averaging 73.9% across datasets and outperforming both prior specialized metrics and LLM-based evaluators (https://aclanthology.org/2023.acl-long.634).

Gunaratna et al. (2023) introduced **TrueTeacher**, a method for generating synthetic training data for factual consistency evaluation by annotating diverse model-generated summaries using FLAN-PaLM 540B. The resulting 1.4M training examples, when combined with ANLI data, enabled a T5-11B student model to achieve a ROC-AUC of 87.8 on the TRUE benchmark, outperforming the LLM teacher itself (84.9). TrueTeacher is the only method that consistently improves out-of-domain performance, and human evaluation confirmed 89% labeling accuracy (https://aclanthology.org/2023.emnlp-main.127).

Liu et al. (2023) proposed **G-Eval**, a framework that uses GPT-4 with chain-of-thought prompting and a form-filling paradigm to assess NLG quality. G-Eval achieved a Spearman correlation of 0.514 with human judgments on the SummEval benchmark, outperforming all previous methods (https://aclanthology.org/2023.emnlp-main.153). This work catalyzed the broader "LLM-as-a-Judge" paradigm for hallucination evaluation.

## 6. Self-Contradiction and Logical Consistency

Mündler et al. (2024) provided a comprehensive investigation of **self-contradictory hallucinations**, where an LLM generates contradictory sentences within the same context. Their analysis revealed that ChatGPT produces self-contradictions in 17.7% of sentences during open-domain generation, and crucially, 35.2% of these self-contradictions cannot be verified using external online text. They proposed a prompting-based framework that detects and mitigates self-contradictions with approximately 80% F1 score, iteratively refining generated text to remove contradictions while preserving fluency (https://iclr.cc/virtual/2024/poster/19094). This work underscores the importance of internal consistency as a signal orthogonal to external factuality.

## 7. Theoretical Foundations: The Impossibility of Elimination

While the majority of the literature focuses on empirical detection, a growing body of theoretical work has examined the fundamental limits of hallucination mitigation. Xu et al. (2024) formalized hallucination as inconsistency between a computable LLM and a computable ground-truth function, proving that LLMs cannot learn all computable functions and will therefore inevitably hallucinate on some inputs regardless of architecture or training data quality. This result, while originally disseminated as a preprint, has been widely cited and discussed in subsequent peer-reviewed work, establishing that hallucination probability can be driven to statistically negligible levels but not to zero while preserving model performance. The theoretical analysis has profound implications for detection: if hallucination cannot be eliminated entirely, robust detection methods become essential for trustworthy deployment. Subsequent work by Suzuki et al. (2025) further showed that hallucinations can be made statistically negligible with sufficient data, though the impossibility of complete elimination remains a formal constraint.

## 8. Summary and Outlook

The 2023–2025 period has seen remarkable progress in hallucination detection, characterized by three converging trends. First, benchmarks have evolved from coarse-grained binary classification (HaluEval) to fine-grained atomic evaluation (FActScore) and domain-specific, automatically verifiable frameworks (ERBench, PHANTOM). Second, detection methods have diversified from sampling-based consistency checks (SelfCheckGPT) to computationally efficient internal-state probing (INSIDE, SEPs, Lookback Lens) and data-efficient learning from unlabeled generations (HaloScope). Third, theoretical work has clarified the fundamental limits of hallucination elimination, motivating the continued development of robust detection as a complementary strategy.

Despite these advances, significant challenges remain. The generalization of detection methods across diverse tasks, domains, and model architectures requires further investigation. The interplay between uncertainty-based signals and internal representation patterns is not yet fully understood. Most critically, bridging the gap between detection and actionable mitigation—where detected hallucinations trigger reliable correction mechanisms—represents the frontier for future research.

---

## References

1. Bang, Y., Ji, Z., Schelten, A., Hartshorn, A., Fowler, T., Zhang, C., Cancedda, N., & Fung, P. (2025). HalluLens: LLM Hallucination Benchmark. *ACL 2025*. https://aclanthology.org/2025.acl-long.1176

2. Chen, C., Liu, K., Chen, Z., Gu, Y., Wu, Y., Tao, M., Fu, Z., & Ye, J. (2024). INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection. *ICLR 2024*. https://iclr.cc/virtual/2024/poster/18385

3. Chuang, Y.-S., Qiu, L., Hsieh, C.-Y., Krishna, R., Kim, Y., & Glass, J. (2024). Lookback Lens: Detecting and Mitigating Contextual Hallucinations in Large Language Models Using Only Attention Maps. *EMNLP 2024*. https://aclanthology.org/2024.emnlp-main.84

4. Du, X., Xiao, C., & Li, S. (2024). HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection. *NeurIPS 2024* (Spotlight). https://neurips.cc/virtual/2024/poster/93676

5. Farquhar, S., Kossen, J., Kuhn, L., & Gal, Y. (2024). Detecting hallucinations in large language models using semantic entropy. *Nature*, 630, 625–630. https://www.nature.com/articles/s41586-024-07421-0

6. Gunaratna, K., et al. (2023). TrueTeacher: Learning Factual Consistency Evaluation with Large Language Models. *EMNLP 2023*. https://aclanthology.org/2023.emnlp-main.127

7. Ji, L., Seyler, D., Kaur, G., Hegde, M., & Dasgupta, K. (2025). PHANTOM: A Benchmark for Hallucination Detection in Financial Long-Context QA. *NeurIPS 2025*. https://neurips.cc/virtual/2025/poster/121830

8. Ji, Z., Gu, Y., Zhang, W., Lyu, C., Lin, D., & Chen, K. (2024). ANAH: Analytical Annotation of Hallucinations in Large Language Models. *ACL 2024*. https://aclanthology.org/2024.acl-long.442

9. Gu, Y., Ji, Z., Zhang, W., Lyu, C., Lin, D., & Chen, K. (2024). ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models. *NeurIPS 2024*. https://neurips.cc/virtual/2024/poster/95407

10. Kossen, J., Han, J., Razzak, M., Schut, L., Malik, S., & Gal, Y. (2024). Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs. *ICML 2024 Workshop on Foundation Models in the Wild*. https://icml.cc/virtual/2024/39442

11. Li, J., Cheng, X., Zhao, W. X., Nie, J.-Y., & Wen, J.-R. (2023). HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models. *EMNLP 2023*. https://aclanthology.org/2023.emnlp-main.397

12. Liu, Y., Iter, D., Xu, Y., Wang, S., Xu, R., & Zhu, C. (2023). G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment. *EMNLP 2023*. https://aclanthology.org/2023.emnlp-main.153

13. Manakul, P., Liusie, A., & Gales, M. J. F. (2023). SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models. *EMNLP 2023*. https://aclanthology.org/2023.emnlp-main.557

14. Min, S., Krishna, K., Lyu, X., Lewis, M., Yih, W.-t., Koh, P., Iyyer, M., Zettlemoyer, L., & Hajishirzi, H. (2023). FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation. *EMNLP 2023*. https://aclanthology.org/2023.emnlp-main.741

15. Mündler, N., He, J., Jenko, S., & Vechev, M. (2024). Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation. *ICLR 2024*. https://iclr.cc/virtual/2024/poster/19094

16. Oh, J., Kim, S., Seo, J., Wang, J., Xu, R., Xie, X., & Whang, S. (2024). ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models. *NeurIPS 2024* (Datasets & Benchmarks Track). https://neurips.cc/virtual/2024/poster/97458

17. Sriramanan, G., Bharti, S., Sadasivan, V. S., Saha, S., Kattakinda, P., & Feizi, S. (2024). LLM-Check: Investigating Detection of Hallucinations in Large Language Models. *NeurIPS 2024*. https://neurips.cc/virtual/2024/poster/95584

18. Su, W., Wang, C., Ai, Q., Hu, Y., Wu, Z., Zhou, Y., & Liu, Y. (2024). Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models. *Findings of ACL 2024*. https://aclanthology.org/2024.findings-acl.854

19. Zha, Y., Yang, Y., Li, R., & Hu, Z. (2023). AlignScore: Evaluating Factual Consistency with A Unified Alignment Function. *ACL 2023*. https://aclanthology.org/2023.acl-long.634

20. Zhang, T., Qiu, L., Guo, Q., Deng, C., Zhang, Y., Zhang, Z., Zhou, C., Wang, X., & Fu, L. (2023). Enhancing Uncertainty-Based Hallucination Detection with Stronger Focus. *EMNLP 2023*. https://aclanthology.org/2023.emnlp-main.58
