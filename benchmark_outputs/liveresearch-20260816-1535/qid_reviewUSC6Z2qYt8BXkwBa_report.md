

# A Comprehensive Literature Review of Recent RL Algorithms for Improving LLM Reasoning Beyond GRPO

**Research Date:** August 17, 2026

---

## Executive Summary

Since DeepSeek's R1 popularized Group Relative Policy Optimization (GRPO) for eliciting chain-of-thought reasoning in LLMs, a surge of research has emerged to address GRPO's documented failure modes: entropy collapse, gradient vanishing, token-level importance sampling variance, length inflation, and training instability (particularly for Mixture-of-Experts models). This review analyzes ten algorithms—DAPO, GFPO, GMPO, GPPO, GPG, CPO, RPO, PPO, COPO, and GSPO—with respect to their motivation, core innovation, differences from GRPO, empirical setup, and limitations.

A key observation is that these algorithms cluster around distinct failure-mode fixes:
- **Exploration/entropy collapse** → DAPO (Clip-Higher), GMPO (wider clipping), GPPO (gradient preservation)
- **Gradient vanishing / sample wastage** → DAPO (Dynamic Sampling), COPO (global consistency reward), GFPO (filtering)
- **Importance ratio variance / unit mismatch** → GSPO (sequence-level), GMPO (geometric mean)
- **Length inflation** → GFPO (filtering for conciseness)
- **Training complexity** → GPG (minimalist objective)

---

## 1. DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization)

### 1.1 Motivation and Core Idea
DAPO, proposed by ByteDance Seed, Tsinghua AIR, and HKU, addresses the reproducibility crisis in large-scale LLM RL. The authors found that a naive GRPO run on Qwen2.5-32B achieved only **30 points on AIME 2024**, far below DeepSeek's reported 47 points. Through careful analysis, they identified four distinct failure modes: entropy collapse, reward noise from truncated samples, ineffective sample-level loss aggregation, and gradient collapse on prompts with uniform accuracy.

### 1.2 Core Innovation (Four Techniques)
1. **Clip-Higher:** Decouples the upper and lower clipping thresholds (ε_low = 0.2, ε_high = 0.28). The standard symmetric clip in GRPO suppresses low-probability "exploration" tokens; raising the upper bound allows these tokens to increase in probability and prevents entropy collapse.
2. **Dynamic Sampling:** Over-samples prompts and filters out groups where accuracy is 0% or 100% (where advantage is zero), ensuring every batch has effective gradients.
3. **Token-Level Policy Gradient Loss:** Replaces GRPO's sample-level loss (averaging per-sample then across samples) with a token-level aggregation, crucial for long-CoT scenarios where per-sample normalization biases against long or short responses.
4. **Overlong Reward Shaping:** Applies a length-aware soft penalty (rather than a hard cut) for truncated responses to reduce reward noise.

### 1.3 Differences vs. GRPO
- Asymmetric clipping (GRPO uses symmetric ε)
- Dynamic filtering of zero-gradient groups (GRPO wastes these)
- Token-level loss instead of sample-level
- Soft length penalty instead of hard truncation

### 1.4 Empirical Setup and Results
- **Model:** Qwen2.5-32B (base, from scratch, no SFT)
- **Framework:** verl; **Compute:** 128×H20 GPUs
- **Config:** AdamW, lr=1e-6, prompt batch 512, 16 responses/prompt, max gen 20,480 tokens
- **Dataset:** DAPO-Math-17K (open-sourced); rule-based verifier
- **Benchmark:** AIME 2024 (avg@32)

| Method | AIME 2024 avg@32 |
|---|---|
| DeepSeek-R1-Zero-Qwen-32B | 47 |
| Naive GRPO | 30 |
| + Overlong Filtering | 36 |
| + Clip-Higher | 38 |
| + Soft Overlong Punishment | 41 |
| + Token-level Loss | 42 |
| + Dynamic Sampling (**DAPO**) | **50** |

### 1.5 Limitations
- Evaluated only on math; no code or multimodal validation
- Requires careful tuning of two clip hyperparameters
- The four techniques are presented as a package; contributions are coupled
- Compute-heavy (128 GPUs), limiting accessibility

**Sources:** [DAPO arXiv](https://arxiv.org/pdf/2503.14476) | [DAPO project page](https://dapo-sia.github.io) | [verl DAPO recipe](https://verl.readthedocs.io/en/latest/algo/dapo.html)

---

## 2. GFPO (Group Filtered Policy Optimization)

### 2.1 Motivation and Core Idea
GFPO (Microsoft Research, Aug 2025) targets **length inflation**: RLVR-trained LLMs tend to produce verbose, filler-heavy responses to game reward. GFPO's insight is that sampling *larger* groups during training and then *filtering* to desirable traits (conciseness, token efficiency) teaches the model to "think less at inference time" by "sampling more at training time."

### 2.2 Core Innovation
- Sample a larger group (e.g., G=8→24) per prompt, then filter to retain a subset (k≤8) based on:
  - **Response length** (shortest k responses)
  - **Token efficiency** (reward per token ratio)
- **Adaptive Difficulty GFPO:** dynamically allocates more training resources (larger sampling) to harder problems based on real-time difficulty estimates.

### 2.3 Differences vs. GRPO
GRPO trains on all sampled responses. GFPO deliberately *discards* samples that exhibit undesirable properties (verbosity), reshaping the gradient signal toward concise reasoning.

### 2.4 Empirical Setup and Results
- **Model:** Phi-4-reasoning (14B); compared against Phi-4-reasoning-plus (GRPO baseline)
- **Group size:** G ∈ {8, 16, 24}, retained k ≤ 8
- **Benchmarks:** AIME 2024/2025, GPQA, Omni-MATH, LiveCodeBench
- **Headline results:**
  - GFPO cuts GRPO's length inflation by **46–71%** while maintaining accuracy
  - Reward-per-token filtering increases reduction to **71–85%**
  - **7% increase in training time → ~30% reduction in end-to-end latency** (90 seconds faster on hard queries)
  - Modest accuracy gains on coding (Shortest 8/24 GFPO: 59.2% vs. GRPO 56.7% on LiveCodeBench)

### 2.5 Limitations
- Increased training-time compute is a fundamental trade-off
- Filtering criteria (length, token efficiency) may not transfer to tasks where verbosity is genuinely useful
- Accuracy preservation is "maintained" rather than improved on most benchmarks

**Sources:** [GFPO arXiv](https://arxiv.org/abs/2508.09726) | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/sample-more-to-think-less-group-filtered-policy-optimization-for-concise-reasoning) | [OpenReview](https://openreview.net/forum?id=UKOqoULbZS)

---

## 3. GMPO (Geometric-Mean Policy Optimization)

### 3.1 Motivation and Core Idea
GMPO (Microsoft Research, Jul 2025) diagnoses GRPO's instability as arising from **outlier importance sampling ratios**. GRPO maximizes the arithmetic mean of token-level rewards, which is sensitive to extreme ratios (πθ/πθ_old), leading to unstable updates. GMPO replaces the arithmetic mean with the **geometric mean**, which is inherently robust to outliers (computed in log-space).

### 3.2 Core Innovation
- Optimize the geometric mean of token-level rewards: J_GMPO = (∏_t r_t(θ)·Â_i)^{1/|o_i|}
- Includes sign(Â_i) to maintain correct optimization direction for negative advantages
- Uses **wider clipping thresholds** (e^{-0.4}, e^{0.4}) enabled by the added stability
- Theoretically shown to be a weighted policy gradient with more stable weights than GRPO

### 3.3 Differences vs. GRPO
- Aggregation function: geometric vs. arithmetic mean
- Wider clipping range (e^{-0.4}, e^{0.4}) vs. GRPO's (0.8, 1.2)

### 3.4 Empirical Setup and Results
- **Models:** Qwen2.5-Math-1.5B/7B, DeepSeek-R1-Distill-Qwen-7B (language); Qwen2.5-VL-Instruct-7B (multimodal)
- **Training:** MATH Level 3–5 (8,523 samples), 8 rollouts/question, 1024 rollouts/round, 8 updates/round, batch 128, 8×A800 GPUs
- **Benchmarks:** AIME24, AMC, MATH500, OlympiadBench, Minerva, Geometry3K

| Model | GRPO Avg Pass@1 | GMPO Avg Pass@1 | Δ |
|---|---|---|---|
| GMPO-7B (R1-Distill) | 59.3 | 63.4 | +4.1% |
| GMPO-1.5B | 42.5 | 43.9 | +1.4% |
| GMPO-7B (Qwen2.5-Math) | 51.2 | 52.7 | +1.5% |
| Geometry3K (multimodal) | 53.3 | 54.7 | +1.4% |

### 3.5 Limitations
- Evaluated only on math and geometry; no code/general reasoning
- Requires careful tuning of wide clipping thresholds
- The geometric mean may over-suppress genuine high-value tokens (not just outliers)

**Sources:** [GMPO arXiv](https://arxiv.org/abs/2507.20673) | [GMPO HTML](https://arxiv.org/html/2507.20673v1) | [HuggingFace](https://huggingface.co/papers/2507.20673)

---

## 4. GPPO (Gradient-Preserving Clipping Policy Optimization)

### 4.1 Motivation and Core Idea
GPPO (Kuaishou, Klear-Reasoner, Aug 2025) identifies two fatal flaws in standard PPO/GRPO clipping:
1. **High-entropy token clipping:** Tokens beyond the upper clip bound (1+ε) are often valuable exploratory decisions; clipping them prematurely kills exploration.
2. **Delayed convergence on negative samples:** Suboptimal trajectories with ratio below (1−ε) have their gradients truncated, slowing learning from mistakes.

### 4.2 Core Innovation
GPPO decouples forward computation from gradient propagation using a **stop-gradient (sg) operation**:
- Forward pass is identical to standard clipping (the term δ/sg(δ) ≡ 1)
- Backward pass *preserves bounded gradients* from clipped tokens
- Enables "gentle" backpropagation from out-of-bound tokens, enhancing exploration and negative-sample learning simultaneously

A follow-up, **CE-GPPO** (ACL 2026), provides systematic entropy analysis: it classifies clipped tokens into four categories (PA&HP, PA&LP, NA&HP, NA&LP) and shows that reintroducing gradients from NA&LP (negative-advantage, low-probability) tokens is key to entropy stabilization.

### 4.3 Differences vs. GRPO
GRPO/PPO discard gradients entirely outside the clip range. GPPO retains them in a bounded manner, effectively relaxing the trust region while maintaining stability.

### 4.4 Empirical Setup and Results (Klear-Reasoner-8B)
- **Model:** Qwen3-8B-Base; long-CoT SFT (1.5M samples distilled from DeepSeek-R1-0528), then two-stage RL (math then code)
- **Config:** 32K max length; lr 1e-6 (math) / 5e-7 (code); 8 responses/prompt; GPPO with ε_h=0.28, no KL loss; joint SFT loss (α=0.1)
- **Compute:** Not fully disclosed (industrial setting)

| Benchmark | Klear-Reasoner-8B |
|---|---|
| AIME 2024 (avg@64) | **90.5%** |
| AIME 2025 (avg@64) | **83.2%** |
| HMMT 2025 | 70.8% |
| LiveCodeBench V5 | 66.0% |
| LiveCodeBench V6 | 58.1% |

CE-GPPO experiments (across model scales on math benchmarks) show consistent gains over DAPO and GRPO baselines, with stable entropy throughout training.

### 4.5 Limitations
- Heavy reliance on high-quality SFT data (DeepSeek-R1-0528 distillation)
- GPPO introduces tunable scaling coefficients (β₁, β₂); the general form adds hyperparameter burden
- Evaluation limited to math and code
- CE-GPPO partially relaxes the PPO trust-region guarantee (theoretically justified as stable, but a departure from classical clipping)

**Sources:** [Klear-Reasoner arXiv](https://arxiv.org/abs/2508.07629) | [CE-GPPO arXiv](https://arxiv.org/abs/2509.20712) | [CE-GPPO GitHub](https://github.com/Kwai-Klear/CE-GPPO)

---

## 5. GPG (Group Policy Gradient)

### 5.1 Motivation and Core Idea
GPG (Chu et al., AMAP; ICLR 2026) argues that GRPO is needlessly complex. It revisits the **traditional policy gradient (PG)** and shows that directly optimizing the original RL objective—without surrogate losses, KL penalties, critics, or reference models—is simpler and stronger. GPG specifically addresses **advantage and gradient estimation bias** in GRPO.

### 5.2 Core Innovation
- Eliminates the critic, reference model, KL divergence constraints, and surrogate loss
- Uses a *corrected* advantage function to fix estimation bias
- Directly optimizes the policy gradient objective; the clipped objective is preserved in a PPO-style form but without the auxiliary machinery

### 5.3 Differences vs. GRPO
- No KL penalty; no reference model
- No surrogate loss complexity
- Corrected advantage estimator reduces bias

### 5.4 Empirical Setup and Results
- **Models:** Qwen2-VL-2B (multimodal), Qwen2.5-Math-7B (unimodal); also tested on reasoning grounding, CV-Bench, fine-grained classification, GEOQA
- **Results (highlights):**
  - **LISA grounding (Qwen2-VL-2B):** GPG mIoU_test 51.5% vs. GRPO 37.6% (+13.9 pts)
  - **CV-Bench:** GPG 76.15% vs. GRPO 59.47% (+16.7 pts)
  - **Fine-grained classification (avg 4 datasets):** GPG 89.0% vs. GRPO 81.9% (+7.1 pts)
  - **GEOQA:** GPG 50.80% vs. GRPO 47.48% (+3.32 pts)
  - **Math (Qwen2.5-Math-7B, AIME 24/AMC/MATH-500):** GPG 48.3/30.0/76.2 vs. GRPO (Dr. GRPO) 43.7/26.7/74.6
- Training reduces compute cost vs. GRPO

### 5.5 Limitations
- The paper does not explicitly enumerate limitations
- As a "minimalist" approach, it may lack the safety rails (KL) that prevent catastrophic drift in some settings
- A separate paper (Chen et al., arXiv:2510.03679, also named GPG) generalizes this to general MDPs and notes the need for careful group size and binning choices

**Sources:** [GPG arXiv](https://arxiv.org/abs/2504.02546) | [GPG GitHub](https://github.com/amap-ml/gpg) | [verl GPG docs](https://verl.readthedocs.io/en/latest/algo/gpg.html) | [GPG general-MDP paper](https://arxiv.org/html/2510.03679v1)

---

## 6. CPO (Comparative Policy Optimization)

### 6.1 Important Note on Ambiguity
The acronym "CPO" is ambiguous in the literature. The user's framing ("Comparative Policy Optimization") matches an **ACL Findings 2025 paper** on role-playing dialogue. However, the more widely cited "CPO" in LLM reasoning is **Chain of Preference Optimization** (NeurIPS 2024), which is a *preference optimization* method (DPO-style), not an RL method. I cover both briefly.

### 6.2 Comparative Policy Optimization (ACL Findings 2025)
- **Motivation:** Addresses reward ambiguity in role-playing dialogue, where multiple valid responses exist and a single reward signal is ambiguous.
- **Core idea:** Uses comparative signals (pairwise or group-based preferences) to optimize policy without relying on a single absolute reward.
- **Empirical setup:** Role-playing dialogue benchmarks; limited public details on model size/config.
- **Limitation:** Task-specific (dialogue), not demonstrated for math/code reasoning.

**Source:** [CPO ACL Anthology](https://aclanthology.org/2025.findings-emnlp.18)

### 6.3 Chain of Preference Optimization (NeurIPS 2024)
- **Motivation:** CoT decoding is not always deliberate/optimal; Tree-of-Thought (ToT) finds better paths but at high inference cost.
- **Core idea:** Fine-tune LLMs to align CoT steps with ToT preferences, using both selected (preferred) and unselected (dispreferred) thoughts. Not RL—uses preference loss.
- **Results:** Average +4.3% (max +9.7%) over standard CoT across QA, fact verification, and arithmetic reasoning; +2.7% over TS-SFT.
- **Limitation:** Requires ToT inference to generate training data (offline, not on-policy RL).

**Source:** [CPO arXiv (Chain of Preference)](https://arxiv.org/html/2406.09136v2) | [CPO GitHub](https://github.com/sail-sg/CPO)

---

## 7. RPO (Reparameterization Proximal Policy Optimization)

### 7.1 Important Clarification
The RPO in this review (arXiv:2508.06214, ICML 2026) is a **robotics/continuous-control** method, NOT an LLM-reasoning algorithm. It addresses sample efficiency in differentiable simulators. There is no widely-adopted "RPO" for LLM reasoning as of this review; the closest LLM-relevant work is the reparameterization gradient family. I include it for completeness given the user's request.

### 7.2 Motivation and Core Idea
Reparameterization Policy Gradient (RPG) achieves high sample efficiency by backpropagating through differentiable dynamics, but suffers from (1) under-utilization of expensive dynamics Jacobians (no sample reuse) and (2) training instability (exploding/vanishing gradients).

### 7.3 Core Innovation
- Proves that under sample reuse, RPG naturally optimizes a **PPO-style surrogate objective via Backpropagation Through Time (BPTT)**—unifying on- and off-policy updates.
- Introduces a clipped policy gradient mechanism tailored for RPG (asymmetric, independent of advantage sign).
- Adds explicit KL divergence regularization (clipping alone is insufficient).

### 7.4 Empirical Setup and Results
- **Environments:** DFlex and Rewarped simulators (Hopper, Ant, Anymal, Humanoid, Hand Reorient)
- **Results:** SOTA final performance and superior sample efficiency vs. SAPO, SHAC, PPO, GI-PPO; RPO trains in ~81 minutes vs. SHAC's ~313 minutes

### 7.5 Limitations
- Not validated on LLM reasoning
- Requires differentiable dynamics (not applicable to standard LLM text generation)
- Future work: sim-to-real transfer

**Source:** [RPO arXiv](https://arxiv.org/abs/2508.06214)

---

## 8. PPO (Proximal Policy Optimization)

### 8.1 Motivation and Role
PPO (Schulman et al., 2017) is the foundational RL algorithm for LLM post-training, used in the original RLHF pipelines (InstructGPT, etc.). For reasoning tasks, it has largely been superseded by GRPO and its variants, but recent work (e.g., "PPO works fine for reasoning") has re-examined it.

### 8.2 Core Idea
- Clipped surrogate objective constrains the importance sampling ratio to [1−ε, 1+ε]
- Uses a **learned value function (critic)** for advantage estimation (GAE)
- Requires a reference model for KL penalty

### 8.3 Differences vs. GRPO
- PPO requires a critic network (memory/compute overhead); GRPO replaces it with group-based normalization
- PPO uses GAE with a value function; GRPO uses group mean/std normalization
- PPO uses a KL penalty from reference model; GRPO variants often drop it

### 8.4 Empirical Setup and Results (Comparative Study, arXiv:2512.07611)
A 2025 study systematically compared PPO, GRPO, and DAPO for reasoning enhancement:
- **Setup:** Models fine-tuned on Countdown Game, then evaluated on general-purpose reasoning benchmarks
- **Findings:** All RL-trained models outperform base models; PPO remains competitive but requires more memory; GRPO/DAPO show better compute efficiency
- Parametric study found group size G and entropy bonus are the most influential hyperparameters

### 8.5 Limitations
- High memory/compute overhead (four models: policy, reference, value, reward)
- Trained reward model needed (vs. rule-based rewards in GRPO)
- Less sample-efficient for reasoning-specific rewards

**Sources:** [PPO arXiv](https://arxiv.org/abs/1707.06347) | [PPO vs GRPO comparison](https://arxiv.org/html/2512.07611v1) | [Raschka analysis](https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training)

---

## 9. COPO (Consistency-Aware Policy Optimization)

### 9.1 Motivation and Core Idea
COPO (arXiv:2508.04138, NeurIPS 2025) addresses the **gradient vanishing** problem in GRPO: when all responses to a prompt converge to the same outcome (all correct or all incorrect), the group-based advantage degenerates to zero, wasting samples. DAPO's dynamic sampling filters these out, but COPO argues this *wastes* potentially valuable training signal.

### 9.2 Core Innovation
1. **Inter-group global reward:** Computes a batch-level, prompt-level reward based on *outcome consistency*. Even when intra-group advantages are zero, the global loss provides meaningful learning signal (encouraging correct self-consistent reasoning paths).
2. **Entropy-based soft blending:** Adaptively weights local (intra-group) vs. global (inter-group) losses using response consistency entropy. Low entropy (high consistency) → more global; high entropy → more local, preserving credit assignment precision.

### 9.3 Differences vs. GRPO
- Adds a second (global) loss term on top of GRPO's local group-relative loss
- DAPO discards zero-gradient groups; COPO exploits them via the global loss

### 9.4 Empirical Setup and Results
- **Models:** Qwen2.5-Instruct 3B and 7B (60 steps); Qwen2.5-Math-1.5B-Instruct (negative control)
- **Config:** DAPO-MATH-17k dataset; 6 responses/prompt; batch 512; 32 mini-batches; AdamW lr=1e-6; asymmetric clip ε=0.2; 2048 max tokens; verl framework
- **Benchmarks:** MATH-500, AIME 2024, GSM8k, AIME 2025

| Model / Metric | GRPO | COPO | Δ |
|---|---|---|---|
| 7B MATH-500 mean@8 | 63.58 | 65.80 | +2.22 |
| 7B AIME24 mean@64 | 12.86 | 13.85 | +0.99 |
| 7B MATH-500 maj@8 | — | 69.27 | — |
| 7B AIME24 maj@64 | — | 21.07 | — |
| 3B MATH-500 mean@8 | 55.83 | 60.38 | +4.55 |

### 9.5 Limitations
- **Underperforms GRPO on small math-tuned models** (Qwen2.5-Math-1.5B-Instruct) by ~1%—the local/global objective conflict harms models with task-specific pretraining
- Two new hyperparameters (γ, ρ) for the blending weight
- Global loss may dilute credit assignment on high-quality responses

**Sources:** [COPO arXiv](https://arxiv.org/abs/2508.04138) | [COPO HTML](https://arxiv.org/html/2508.04138v1) | [OpenReview](https://openreview.net/forum?id=JkmKzsMaAu)

---

## 10. GSPO (Group Sequence Policy Optimization)

### 10.1 Motivation and Core Idea
GSPO (Qwen Team, Alibaba; arXiv:2507.18071) identifies a **fundamental ill-posedness in GRPO's objective**: GRPO applies token-level importance weights πθ(y_t)/πθ_old(y_t), but importance sampling requires averaging over many samples to correct distribution mismatch. A single token sample fails this role, injecting high-variance noise that accumulates over long sequences—leading to **irreversible model collapse**, especially in MoE models where expert routing volatility (10% expert turnover per update) exacerbates ratio fluctuation.

### 10.2 Core Innovation
- **Sequence-level importance ratio:** s_i(θ) = (πθ(y_i|x) / πθ_old(y_i|x))^(1/|y_i|), i.e., length-normalized sequence likelihood ratio (geometric mean of token ratios)
- **Sequence-level clipping, rewarding, and optimization:** the unit of optimization matches the unit of reward (whole sequence)
- Eliminates the need for **Routing Replay** (a previously required trick for MoE stability)

### 10.3 Differences vs. GRPO
- Token-level → sequence-level importance ratios and clipping
- GRPO requires Routing Replay for MoE convergence; GSPO does not
- GSPO clips a much larger fraction of tokens (~15% vs. ~0.13% for GRPO), yet achieves *better* training efficiency—proving GRPO's token-level gradients are noisy

### 10.4 Empirical Setup and Results
- **Model:** Cold-start model fine-tuned from Qwen3-30B-A3B-Base (MoE)
- **Config:** 4 mini-batches per rollout batch; GSPO clip range 3e-4/4e-4 vs. GRPO 0.2/0.27
- **Benchmarks:** AIME'24 (Pass@1 avg over 32), LiveCodeBench (202410–202502, avg@8), CodeForces (Elo)
- **Results:** GSPO achieves higher training reward and benchmark performance under the same compute; stable training with continuous improvement via compute scaling, query updates, and length extension
- **Production impact:** Successfully applied to the latest Qwen3 (Instruct, Coder, Thinking) models

### 10.5 Limitations
- Clipping ranges differ by orders of magnitude from GRPO, requiring different hyperparameter intuition
- Not explicitly discussed, but a follow-up paper (Length-Unbiased Sequence Policy Optimization) notes GSPO's sequence-level clipping can introduce **length bias** (gradients dominated by positive samples, leading to shorter responses)
- Evaluation primarily on math/code; general reasoning not shown

**Sources:** [GSPO arXiv](https://arxiv.org/abs/2507.18071) | [Qwen blog](https://qwenlm.github.io/blog/gspo) | [HuggingFace](https://huggingface.co/papers/2507.18071)

---

## Cross-Cutting Trends and Research Insights

### 1. The GRPO Failure-Mode Taxonomy
The literature converges on a shared set of GRPO deficiencies, each spawning an algorithmic fix:

| Failure Mode | Addressed By |
|---|---|
| Entropy collapse / exploration death | DAPO (Clip-Higher), GMPO (wider clip), GPPO/CE-GPPO (gradient preservation) |
| Gradient vanishing / sample wastage | DAPO (Dynamic Sampling), COPO (global reward), GFPO (filtering) |
| Token-level importance ratio variance | GSPO (sequence-level), GMPO (geometric mean) |
| Length inflation | GFPO (length/efficiency filtering), GSPO (length bias noted) |
| Training complexity / overhead | GPG (minimalist objective) |
| MoE instability | GSPO (sequence-level, no Routing Replay) |

### 2. Convergence on "Unit of Optimization"
A deep theoretical theme unites GMPO, GSPO, and GPPO: **the unit of optimization should match the unit of reward**. GSPO moves to sequence-level; GMPO changes the aggregation statistic; GPPO preserves gradients at the token level. This suggests the token-level importance weight itself is the root instability, and sequence-level or robust-aggregation approaches are the most promising directions.

### 3. Compute-Time vs. Inference-Time Trade-off
GFPO explicitly trades training-time compute for inference-time efficiency (sample more to think less). COPO argues against *discarding* zero-gradient samples (as DAPO does) in favor of *exploiting* them. This is a fundamental design philosophy split: discard vs. repurpose.

### 4. The Clipping Dilemma
Every algorithm grapples with clipping:
- DAPO: asymmetric (raise ceiling)
- GMPO: wider symmetric range
- GPPO: preserve out-of-bound gradients
- GSPO: clip whole sequences
- GPG: eliminate the surrogate entirely

The field has not reached consensus on whether clipping should be loosened, widened, preserved, or removed—suggesting this is the key open question.

### 5. Reproducibility as a First-Class Concern
DAPO and Klear-Reasoner both explicitly position open-sourcing (code, data, configs) as core contributions. The field recognizes that hidden training details (DeepSeek-R1, OpenAI o1) are a major barrier to progress.

---

## References

1. DAPO: [https://arxiv.org/pdf/2503.14476](https://arxiv.org/pdf/2503.14476) | Project: [https://dapo-sia.github.io](https://dapo-sia.github.io) | verl recipe: [https://verl.readthedocs.io/en/latest/algo/dapo.html](https://verl.readthedocs.io/en/latest/algo/dapo.html)
2. GFPO: [https://arxiv.org/abs/2508.09726](https://arxiv.org/abs/2508.09726) | Microsoft Research: [https://www.microsoft.com/en-us/research/publication/sample-more-to-think-less-group-filtered-policy-optimization-for-concise-reasoning](https://www.microsoft.com/en-us/research/publication/sample-more-to-think-less-group-filtered-policy-optimization-for-concise-reasoning) | OpenReview: [https://openreview.net/forum?id=UKOqoULbZS](https://openreview.net/forum?id=UKOqoULbZS)
3. GMPO: [https://arxiv.org/abs/2507.20673](https://arxiv.org/abs/2507.20673) | HTML: [https://arxiv.org/html/2507.20673v1](https://arxiv.org/html/2507.20673v1) | HF: [https://huggingface.co/papers/2507.20673](https://huggingface.co/papers/2507.20673)
4. GPPO (Klear-Reasoner): [https://arxiv.org/abs/2508.07629](https://arxiv.org/abs/2508.07629) | CE-GPPO: [https://arxiv.org/abs/2509.20712](https://arxiv.org/abs/2509.20712) | CE-GPPO GitHub: [https://github.com/Kwai-Klear/CE-GPPO](https://github.com/Kwai-Klear/CE-GPPO)
5. GPG: [https://arxiv.org/abs/2504.02546](https://arxiv.org/abs/2504.02546) | GitHub: [https://github.com/amap-ml/gpg](https://github.com/amap-ml/gpg) | verl: [https://verl.readthedocs.io/en/latest/algo/gpg.html](https://verl.readthedocs.io/en/latest/algo/gpg.html) | General-MDP GPG: [https://arxiv.org/html/2510.03679v1](https://arxiv.org/html/2510.03679v1)
6. CPO (Chain of Preference Optimization): [https://arxiv.org/html/2406.09136v2](https://arxiv.org/html/2406.09136v2) | GitHub: [https://github.com/sail-sg/CPO](https://github.com/sail-sg/CPO) | CPO (Comparative, dialogue): [https://aclanthology.org/2025.findings-emnlp.18](https://aclanthology.org/2025.findings-emnlp.18)
7. RPO (Reparameterization PPO): [https://arxiv.org/abs/2508.06214](https://arxiv.org/abs/2508.06214) | ICML 2026: [https://icml.cc/virtual/2026/poster/63789](https://icml.cc/virtual/2026/poster/63789)
8. PPO: [https://arxiv.org/abs/1707.06347](https://arxiv.org/abs/1707.06347) | PPO/GRPO/DAPO comparison: [https://arxiv.org/html/2512.07611v1](https://arxiv.org/html/2512.07611v1) | Raschka survey: [https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training](https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training)
9. COPO: [https://arxiv.org/abs/2508.04138](https://arxiv.org/abs/2508.04138) | HTML: [https://arxiv.org/html/2508.04138v1](https://arxiv.org/html/2508.04138v1) | OpenReview: [https://openreview.net/forum?id=JkmKzsMaAu](https://openreview.net/forum?id=JkmKzsMaAu)
10. GSPO: [https://arxiv.org/abs/2507.18071](https://arxiv.org/abs/2507.18071) | Qwen blog: [https://qwenlm.github.io/blog/gspo](https://qwenlm.github.io/blog/gspo) | HF: [https://huggingface.co/papers/2507.18071](https://huggingface.co/papers/2507.18071)
11. GRPO background: DeepSeekMath [https://arxiv.org/abs/2402.03300](https://arxiv.org/abs/2402.03300) | Wolfe GRPO explainer: [https://cameronrwolfe.substack.com/p/grpo](https://cameronrwolfe.substack.com/p/grpo)
12. Policy optimization survey (blog): [https://ydnyshhh.github.io/posts/policy_optimization](https://ydnyshhh.github.io/posts/policy_optimization)

---

*Report compiled from publicly available arXiv preprints, conference proceedings, and official project pages. Full empirical details were not uniformly available for all algorithms (notably CPO and RPO, which lie outside the core LLM-reasoning RL literature); where information was incomplete, this is explicitly noted.*
