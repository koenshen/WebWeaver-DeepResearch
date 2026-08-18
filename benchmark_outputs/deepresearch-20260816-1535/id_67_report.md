

# Recent Research Progress in Reinforcement Learning: Efficient Exploration Under Sparse Rewards and Constraints, and Implications for Trajectory Planning

## 1. Introduction

The twin challenges of **sparse rewards** and **safety constraints** represent two of the most fundamental open problems in reinforcement learning (RL). In sparse-reward settings, the agent receives little or no feedback until it stumbles upon a goal state, making random exploration exponentially inefficient. In constrained settings, the agent must explore while never violating safety limits—a tension that often leads to overly conservative policies. This report surveys the most significant recent advances (2024–2026) in addressing these two challenges, and then analyzes their implications for the downstream problem of trajectory planning in robotics, autonomous driving, and related domains.

---

## 2. Efficient and Proactive Exploration Under Sparse Rewards

### 2.1 The Go-Explore Family: From Heuristics to Foundation Models

The **Go-Explore** paradigm, originally introduced by Ecoffet et al. (2019), fundamentally reframes the exploration problem by separating it into two phases: **return** to a promising previously visited state, then **explore** from there. This "first return, then explore" principle achieved superhuman performance on Montezuma's Revenge and other hard-exploration Atari games, where traditional RL algorithms scored near zero.

**Intelligent Go-Explore (IGE)**, presented at ICML 2024 by Lu, Hu, and Clune, dramatically extends this approach. Where Go-Explore required manually designed heuristics to determine which states are "interesting" enough to archive, IGE replaces these heuristics with the internalized human notions of interestingness captured by **pretrained foundation models** (FMs). This provides an instinctive ability to identify new objects, locations, or behaviors—even serendipitous discoveries that cannot be predicted ahead of time. On the Game of 24 mathematical reasoning task, IGE reaches 100% success rate **70.8% faster** than the best graph search baseline. On BabyAI-Text, it exceeds the previous state-of-the-art with orders of magnitude fewer online samples, and on TextWorld it succeeds in settings where prior FM-based agents like Reflexion completely fail (Lu et al., 2024, [https://icml.cc/virtual/2024/35852](https://icml.cc/virtual/2024/35852)).

### 2.2 Automated Curricula for Directed Exploration

The **DISCOVER** framework (Hübotter et al., NeurIPS 2025) addresses a key limitation of prior exploration methods: they often explore without direction, treating the entire state space as equally important. DISCOVER argues that solving challenging sparse-reward tasks requires first solving **simpler, relevant subtasks** whose achievement teaches the agent skills needed for the target task. The method automatically selects exploratory goals that point toward the target task, extracting this "sense of direction" from existing RL algorithms without any prior information.

A key theoretical contribution is a formal bound on the time until the target task becomes achievable—a bound that depends only on the agent's initial distance to the target, not on the volume of the task space. This is a significant step toward making exploration in high-dimensional, long-horizon tasks tractable. Empirical evaluations in high-dimensional environments show that DISCOVER solves exploration problems beyond the reach of prior state-of-the-art methods (Hübotter et al., 2025, [https://arxiv.org/abs/2505.19850](https://arxiv.org/abs/2505.19850)).

### 2.3 Model-Based Exploration: DreamerV3 and Extensions

**DreamerV3** (Hafner et al., Nature 2025) represents a major milestone in model-based RL. It learns a world model from experience and uses it to train an actor-critic policy entirely from imagined trajectories. The algorithm masters a wide range of domains—over 150 tasks from 8 domains—with a **fixed set of hyperparameters**, eliminating the need for task-specific tuning. Most notably, DreamerV3 became the first algorithm to collect a diamond in Minecraft **without any human data or pre-defined curricula**, achieving this after approximately 30 million environment steps (about 17 days of real-time experience) (Hafner et al., 2025, [https://github.com/danijar/dreamerv3](https://github.com/danijar/dreamerv3); FindingTheta, 2025, [https://www.findingtheta.com/blog/the-evolution-of-imagination-a-deep-dive-into-dreamerv3-and-its-conquest-of-minecraft](https://www.findingtheta.com/blog/the-evolution-of-imagination-a-deep-dive-into-dreamerv3-and-its-conquest-of-minecraft)).

**DreamerV3-XP** (Bierling et al., 2025) extends DreamerV3 with two targeted exploration enhancements: (1) a **prioritized replay buffer** that scores trajectories by return, reconstruction loss, and value error, and (2) an **intrinsic reward** based on the disagreement of an ensemble of world models over predicted environment rewards. This ensemble-based uncertainty estimation drives exploration toward trajectories the model knows least about. DreamerV3-XP achieves faster learning and lower dynamics model loss, particularly in sparse-reward settings (Bierling et al., 2025, [https://arxiv.org/abs/2510.21418](https://arxiv.org/abs/2510.21418)).

### 2.4 Curiosity-Driven Exploration: New Directions

The **Intrinsic Curiosity Module (ICM)** (Pathak et al., 2017) remains a foundational approach, formulating curiosity as the prediction error of an agent's ability to predict the consequences of its own actions in a learned feature space. Recent work (2025) has extended curiosity-driven exploration in several directions:

- **Curiosity-Driven Exploration with Hierarchical Vision Transformers** (2025) incorporates modern vision transformer architectures to improve feature representations for curiosity in high-dimensional visual environments, showing significant gains in sparse-reward settings (ScienceDirect, 2025, [https://www.sciencedirect.com/science/article/abs/pii/S0925231225009245](https://www.sciencedirect.com/science/article/abs/pii/S0925231225009245)).

- **Adaptive Self-Supervised Learning for Action Games** (Farooq et al., 2025) demonstrates a curiosity-driven approach that adaptively balances exploration and exploitation in action games, achieving faster convergence than standard ICM baselines (Farooq et al., 2025, [https://www.mdpi.com/2073-431X/14/10/434](https://www.mdpi.com/2073-431X/14/10/434)).

- **Curiosity-Driven Exploration for LLMs** (arXiv 2509.09675, 2025) applies curiosity principles to large language models, using intrinsic reward signals to guide more efficient exploration of reasoning and action spaces (arXiv, 2025, [https://arxiv.org/abs/2509.09675](https://arxiv.org/abs/2509.09675)).

- **CERMIC** (NeurIPS 2025) introduces multi-agent curiosity calibration, where agents dynamically adjust their intrinsic curiosity based on inferred multi-agent context, preventing the confusion of environmental stochasticity with meaningful novelty in multi-agent settings (NeurIPS, 2025, [https://neurips.cc/virtual/2025/poster/120209](https://neurips.cc/virtual/2025/poster/120209)).

### 2.5 LLM-Guided Exploration

A rapidly emerging paradigm leverages the procedural knowledge and commonsense reasoning of **Large Language Models (LLMs)** to guide RL exploration:

- **LLM-Augmented Observations** (ICAPS 2025 Workshop) provides LLM-generated action recommendations through augmented observation spaces, allowing RL agents to learn *when* to follow or ignore this guidance. This achieves a **71% relative improvement** in final success rates on challenging BabyAI environments, with agents reaching performance thresholds **up to 9× faster** (arXiv, 2025, [https://arxiv.org/abs/2510.08779](https://arxiv.org/abs/2510.08779)).

- **ExploRLLM** (ICRA 2025) integrates LLM knowledge into RL exploration by using a residual action space and observation space derived from affordances recognized by foundation models. The LLM hierarchically generates language model programs that guide exploration toward meaningful states, significantly reducing the time and cost of training (Ma et al., 2025, [https://explorllm.github.io](https://explorllm.github.io)).

- **LLM-TALE** (ICRA 2026) introduces task- and affordance-level planning using LLMs to directly steer RL exploration. Unlike prior approaches that assume optimal LLM-generated plans, LLM-TALE corrects suboptimality online and explores multimodal affordance-level plans without human supervision. It demonstrates zero-shot sim-to-real transfer on real robotic pick-and-place tasks (arXiv, 2025, [https://arxiv.org/abs/2509.16615](https://arxiv.org/abs/2509.16615)).

- **LLM-Explorer** (2025) uses an LLM as a plug-in policy exploration module that periodically replaces fixed exploration noise (e.g., ε-greedy or Gaussian noise) with adaptively generated action distributions, enabling the exploration strategy to respond to the agent's learning status (OpenReview, 2025, [https://openreview.net/forum?id=VA5P0rUZPx](https://openreview.net/forum?id=VA5P0rUZPx)).

### 2.6 Exploration-Guided Reward Shaping

**EXPLORS** (Devidze et al., NeurIPS 2022) remains a highly cited framework for self-supervised reward shaping. It learns an intrinsic reward function in combination with exploration-based bonuses to maximize the agent's utility with respect to extrinsic rewards. The framework operates without any domain knowledge and is theoretically grounded in a special family of MDPs. Follow-up work (2024–2025) has extended these ideas to multi-agent settings and combined them with LLM-based heuristics (Devidze et al., 2022, [https://proceedings.neurips.cc/paper_files/paper/2022/hash/266c0f191b04cbbbe529016d0edc847e-Abstract-Conference.html](https://proceedings.neurips.cc/paper_files/paper/2022/hash/266c0f191b04cbbbe529016d0edc847e-Abstract-Conference.html)).

---

## 3. Proactive Exploration Under Constraints (Safe Exploration)

### 3.1 ActSafe: Active Exploration with Safety Guarantees

**ActSafe** (As et al., ICLR 2025) is a model-based RL algorithm that achieves safe and efficient exploration by learning a **well-calibrated probabilistic model** of the system and then planning **optimistically with respect to epistemic uncertainty** about dynamics while enforcing **pessimism with respect to safety constraints**. Under regularity assumptions, ActSafe provides formal guarantees of safety during learning while also obtaining a near-optimal policy in finite time. A practical variant extends to high-dimensional visual control tasks. Empirically, ActSafe achieves state-of-the-art performance on standard safe deep RL benchmarks, including Safety-Gymnasium, while ensuring safety throughout training (As et al., 2025, [https://arxiv.org/abs/2410.09486](https://arxiv.org/abs/2410.09486); [https://yardenas.github.io/actsafe](https://yardenas.github.io/actsafe)).

### 3.2 ORAC: Optimistic Exploration for Risk-Averse Constrained RL

**ORAC** (McCarthy et al., ECAI 2025) addresses the problem of **Risk-Averse Constrained Reinforcement Learning (RaCRL)**, where the goal is to minimize the likelihood of rare and catastrophic constraint violations caused by environmental randomness. Standard risk-averse approaches lead to conservative exploration that converges to suboptimal policies. ORAC constructs an exploratory policy by maximizing a local **Upper Confidence Bound (UCB)** of the reward value function while minimizing a local **Lower Confidence Bound (LCB)** of the risk-averse cost value function. The weighting assigned to the cost value is dynamically adjusted based on whether the safety constraint is exceeded. This approach encourages exploration of uncertain regions while maintaining safety. Experiments on Safety-Gymnasium and the CityLearn building energy management environment show that ORAC prevents convergence to suboptimal policies and significantly improves the reward-cost trade-off (McCarthy et al., 2025, [https://arxiv.org/abs/2507.08793](https://arxiv.org/abs/2507.08793); [https://research.ibm.com/publications/optimistic-exploration-for-risk-averse-constrained-reinforcement-learning](https://research.ibm.com/publications/optimistic-exploration-for-risk-averse-constrained-reinforcement-learning)).

### 3.3 Safe Exploration via Policy Priors (SOOPER)

**SOOPER** (2025) tackles safe exploration by using suboptimal yet conservative policies (obtained from offline data or simulators) as **priors**. It uses probabilistic dynamics models to optimistically explore while pessimistically falling back to the conservative policy prior when needed. This approach provides formal safety guarantees while still enabling efficient learning. The key insight is that safety must be maintained throughout *all* episodes of training, not just at convergence (arXiv, 2025, [https://arxiv.org/html/2601.19612v1](https://arxiv.org/html/2601.19612v1)).

### 3.4 Constrained Exploration in Off-Policy Safe RL

Recent work (ICLR 2026) addresses the critical issue that off-policy safe RL methods often lack cost-compliant exploration—the agent can be misled into risky areas during data collection. Methods like **MICE** employ a memory-based intrinsic cost around unsafe states, causing the cost critic to conservatively overestimate risk. This is combined with techniques like **Truncated Quantile Critics (TQC)** and local policy convexification via the augmented Lagrangian method to achieve strong safety and sample efficiency even with high update-to-data ratios (ICLR, 2026, [https://proceedings.iclr.cc/paper_files/paper/2026/file/c383e44d9a878d1982d9abb838bd5d8a-Paper-Conference.pdf](https://proceedings.iclr.cc/paper_files/paper/2026/file/c383e44d9a878d1982d9abb838bd5d8a-Paper-Conference.pdf)).

### 3.5 Risk-Aware Constrained RL with Optimized Certainty Equivalents

A framework for risk-aware constrained RL (2025) uses **Optimized Certainty Equivalents (OCEs)**—a broad class of risk measures that includes Conditional Value-at-Risk (CVaR), entropic risk, and mean-variance. This work provides per-stage robustness properties jointly in reward values and time, offering a principled way to incorporate risk awareness into constrained RL. The framework dynamically adjusts conservativeness during policy updates, reducing constraint violations by up to 99% in benchmark tasks (MIT, 2025, [https://dspace.mit.edu/entities/publication/f4b2f8c6-fee9-42ad-8bd6-aaf1e9cde79f](https://dspace.mit.edu/entities/publication/f4b2f8c6-fee9-42ad-8bd6-aaf1e9cde79f)).

### 3.6 Generalized Safe Exploration (MASE)

The **MASE** meta-algorithm (NeurIPS 2023) provides a unified formulation for common safe exploration problems. It combines an unconstrained RL algorithm with an uncertainty quantifier to guarantee safety in the current episode while properly penalizing unsafe explorations before actual safety violation occurs. Two variants are proposed: one based on generalized linear models with theoretical guarantees, and another for deep RL settings (NeurIPS, 2023, [https://proceedings.neurips.cc/paper_files/paper/2023/hash/5d4cd12ef6efedbf26b69b410f1f7d67-Abstract-Conference.html](https://proceedings.neurips.cc/paper_files/paper/2023/hash/5d4cd12ef6efedbf26b69b410f1f7d67-Abstract-Conference.html)).

---

## 4. Analysis and Implications for Trajectory Planning Problems

Trajectory planning—the problem of generating a sequence of states or actions from a start to a goal while avoiding obstacles and satisfying constraints—is a natural downstream application of the exploration techniques surveyed above. The following analysis connects specific advances to trajectory planning challenges.

### 4.1 Sparse Rewards in Trajectory Planning

Trajectory planning problems in robotics and autonomous driving are fundamentally sparse-reward problems: the agent receives a reward only when it reaches the goal, and all intermediate states provide zero feedback. This is particularly acute in long-horizon tasks like navigation through unknown environments, where the probability of randomly stumbling upon the goal is negligible.

**Key implications:**

- **Go-Explore and IGE** directly address the "needle-in-a-haystack" problem of long-horizon trajectory planning. The archive-and-return mechanism is well-suited to trajectory planning because waypoints naturally serve as "cells" to archive, and the trajectory itself can be segmented into sub-trajectories for robustification. The replacement of hand-coded heuristics with foundation models (IGE) means that trajectory planners can now leverage general world knowledge to identify promising partial trajectories—e.g., recognizing that reaching a doorway is a meaningful subgoal even if the final destination is unknown.

- **DISCOVER's** goal-directed curriculum learning is directly applicable to trajectory planning in complex environments. Rather than exploring the entire state space, DISCOVER's directed goal selection can be used to progressively plan trajectories through increasingly challenging regions, with the formal bound on time-to-achievement providing a certificate of exploration efficiency. This is especially valuable in settings like autonomous driving, where the vehicle must navigate through a sequence of traffic scenarios of increasing difficulty.

- **DreamerV3's** world model allows trajectory planning entirely in imagination, enabling the agent to simulate thousands of candidate trajectories from a single real-world experience. The Minecraft diamond achievement is a particularly relevant demonstration: the agent learned to plan a multi-step sequence (collect wood → craft table → craft pickaxe → mine stone → craft iron pickaxe → mine diamond) that required hundreds of distinct actions across a long horizon, with no intermediate reward. This is directly analogous to complex trajectory planning tasks in robotics that require sequencing multiple skills.

### 4.2 Constraints in Trajectory Planning

Trajectory planning is inherently constrained: the robot must avoid collisions, respect joint limits, maintain stability, and satisfy dynamic constraints (e.g., velocity and acceleration limits). Safe exploration techniques are therefore essential for training RL-based trajectory planners.

**Key implications:**

- **ActSafe's** optimistic exploration with pessimistic safety enforcement maps naturally onto trajectory planning under uncertainty. The probabilistic world model captures uncertainty about the environment (e.g., unknown obstacle positions, uncertain dynamics), and the optimistic planning explores promising trajectories while the safety pessimism ensures that the robot never ventures into regions where collision is likely. The formal safety guarantee during learning is particularly important for real-world deployment, where the robot must learn *while* operating safely.

- **ORAC's** UCB/LCB approach is well-suited to risk-averse trajectory planning. In autonomous driving, for example, the "reward" (progress toward destination) can be maximized optimistically while the "cost" (collision risk) is bounded pessimistically. The dynamic adjustment of cost weighting based on constraint satisfaction creates an adaptive planner that becomes more conservative near safety boundaries and more exploratory in safe regions.

- **SOOPER's** use of conservative policy priors from offline data is directly applicable to trajectory planning: a trajectory planner can be pre-trained on safe demonstrations (offline data) and then fine-tuned online with a safety fallback. If the planner attempts a trajectory that becomes unsafe, it can revert to the conservative prior, preventing catastrophic failures.

- **The risk-aware OCE framework** provides a principled way to handle multiple trajectory quality metrics beyond simple collision avoidance. For instance, trajectory planners can optimize for mean travel time while controlling the tail risk of extreme delays or high acceleration (which causes passenger discomfort).

### 4.3 LLM-Guided Trajectory Planning

The integration of LLMs into trajectory planning represents perhaps the most transformative recent development.

**Key implications:**

- **LLM-Augmented Observations** enable trajectory planners to incorporate high-level semantic knowledge into the planning process. For example, an LLM can suggest that "the robot should go around the table, not through the chairs" as an action recommendation, and the RL agent learns when to follow or ignore this guidance based on experience. This is particularly valuable for trajectory planning in human environments, where the optimal path depends on semantic understanding (e.g., "don't walk across the clean floor").

- **ExploRLLM** and **LLM-TALE** demonstrate that LLMs can generate task-level and affordance-level plans that guide trajectory search. The hierarchical decomposition—LLM generates high-level plan, RL fills in low-level trajectory—is a natural fit for trajectory planning problems. The ability to correct suboptimal LLM plans online addresses a key limitation of pure LLM-based planning (which can produce physically infeasible trajectories) while still benefiting from the LLM's broad knowledge.

- **LLM-Explorer's** adaptive exploration policy replaces fixed noise schedules with context-dependent exploration, which is critical for trajectory planning in non-stationary environments. The exploration strategy can adapt based on the difficulty of the current planning problem, spending more exploration budget in challenging scenarios.

### 4.4 From Exploration to Robust Trajectory Generation

Several specific technical contributions of the surveyed works have direct implications for trajectory planner design:

| Technique | Trajectory Planning Application |
|-----------|----------------------------------|
| **Prioritized replay (DreamerV3-XP)** | Prioritize trajectories that are high-return, have high reconstruction error, or high value error, focusing learning on the most informative segments |
| **Ensemble disagreement (DreamerV3-XP)** | Use ensemble of world models to identify trajectory segments with high model uncertainty, driving exploration where the dynamics model is least accurate |
| **Curiosity-driven exploration (ICM)** | Formulate curiosity as prediction error in a learned feature space, naturally biasing exploration toward novel trajectory patterns |
| **Automated curricula (DISCOVER)** | Progressively increase trajectory complexity, from simple straight-line paths to complex obstacle courses |
| **Safe fallback policies (SOOPER)** | Maintain a conservative default trajectory that can be executed if the proposed trajectory becomes unsafe |
| **Risk-aware constraints (ORAC, OCE)** | Explicitly bound the probability of constraint violation, enabling trajectory planners with formal safety certificates |

### 4.5 Open Challenges and Future Directions

Despite significant progress, several challenges remain for the application of these exploration techniques to trajectory planning:

1. **Computational cost**: Many of the methods surveyed (DreamerV3, ActSafe, IGE) require substantial computational resources. Deploying them on embedded systems for real-time trajectory planning remains challenging.

2. **Sim-to-real transfer**: While LLM-TALE demonstrates zero-shot sim-to-real transfer for pick-and-place tasks, generalizing to diverse real-world trajectory planning scenarios remains an open problem.

3. **Multi-agent trajectory planning**: The CERMIC framework for multi-agent curiosity calibration is a step toward multi-robot trajectory planning, but scalable methods for coordinating exploration among multiple robots under safety constraints are still needed.

4. **Formal safety guarantees**: ActSafe and MASE provide theoretical safety guarantees under specific assumptions, but extending these guarantees to complex, high-dimensional trajectory planning problems with learned dynamics models remains an active research area.

5. **Integration of LLM and low-level control**: Current LLM-guided approaches still face challenges with the gap between semantic-level planning and continuous low-level trajectory generation. More work is needed on hierarchical frameworks that tightly couple LLM reasoning with optimization-based trajectory generation.

---

## 5. Conclusion

Recent research has produced a rich toolkit for addressing the fundamental challenges of exploration in reinforcement learning. For sparse rewards, the field has moved from heuristic-based methods (Go-Explore) to foundation-model-guided exploration (IGE), automated curricula (DISCOVER), and world-model-based imagination (DreamerV3). For constrained exploration, the field has developed principled methods for optimistic exploration with pessimistic safety enforcement (ActSafe, ORAC), risk-aware planning (OCE), and safe policy priors (SOOPER).

The integration of LLMs into both exploration paradigms represents a particularly promising direction, enabling agents to leverage vast amounts of general knowledge to guide exploration toward semantically meaningful states and actions. For trajectory planning, these advances offer concrete algorithmic components: goal-directed exploration for long-horizon planning, safety-aware exploration for collision-free navigation, and LLM-guided exploration for semantically informed trajectory generation.

The convergence of model-based RL, safe exploration, and foundation model integration suggests that the next generation of trajectory planners will be capable of learning complex, long-horizon behaviors in the real world while maintaining formal safety guarantees.

---

## References

1. Ecoffet, A., et al. (2019). "Go-Explore: a New Approach for Hard-Exploration Problems." *arXiv:1901.10995*. [https://arxiv.org/abs/1901.10995](https://arxiv.org/abs/1901.10995)

2. Lu, C., Hu, S., & Clune, J. (2024). "Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models." *ICML 2024*. [https://icml.cc/virtual/2024/35852](https://icml.cc/virtual/2024/35852)

3. Hübotter, J., et al. (2025). "DISCOVER: Automated Curricula for Sparse-Reward Reinforcement Learning." *NeurIPS 2025*. [https://arxiv.org/abs/2505.19850](https://arxiv.org/abs/2505.19850)

4. Hafner, D., et al. (2025). "Mastering Diverse Control Tasks through World Models." *Nature*. [https://github.com/danijar/dreamerv3](https://github.com/danijar/dreamerv3)

5. Bierling, L., et al. (2025). "DreamerV3-XP: Optimizing exploration through uncertainty estimation." *arXiv:2510.21418*. [https://arxiv.org/abs/2510.21418](https://arxiv.org/abs/2510.21418)

6. Pathak, D., et al. (2017). "Curiosity-driven Exploration by Self-supervised Prediction." *ICML 2017*. [https://pathak22.github.io/noreward-rl](https://pathak22.github.io/noreward-rl)

7. Farooq, S.S., et al. (2025). "Curiosity-Driven Exploration in Reinforcement Learning: An Adaptive Self-Supervised Learning Approach for Playing Action Games." *Computers*, 14(10), 434. [https://www.mdpi.com/2073-431X/14/10/434](https://www.mdpi.com/2073-431X/14/10/434)

8. "Curiosity-driven exploration based on hierarchical vision transformer for deep reinforcement learning with sparse rewards." (2025). *Neurocomputing*. [https://www.sciencedirect.com/science/article/abs/pii/S0925231225009245](https://www.sciencedirect.com/science/article/abs/pii/S0925231225009245)

9. "CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models." (2025). *arXiv:2509.09675*. [https://arxiv.org/abs/2509.09675](https://arxiv.org/abs/2509.09675)

10. "CERMIC: Curiosity-Driven Exploration through Multi-Agent Calibration." (2025). *NeurIPS 2025*. [https://neurips.cc/virtual/2025/poster/120209](https://neurips.cc/virtual/2025/poster/120209)

11. Devidze, R., Kamalaruban, P., & Singla, A. (2022). "Exploration-Guided Reward Shaping for Reinforcement Learning under Sparse Rewards." *NeurIPS 2022*. [https://proceedings.neurips.cc/paper_files/paper/2022/hash/266c0f191b04cbbbe529016d0edc847e-Abstract-Conference.html](https://proceedings.neurips.cc/paper_files/paper/2022/hash/266c0f191b04cbbbe529016d0edc847e-Abstract-Conference.html)

12. "Guiding Exploration in Reinforcement Learning Through LLM-Augmented Observations." (2025). *ICAPS 2025 Workshop*. [https://arxiv.org/abs/2510.08779](https://arxiv.org/abs/2510.08779)

13. Ma, R., et al. (2025). "ExploRLLM: Guiding Exploration in Reinforcement Learning with Large Language Models." *ICRA 2025*. [https://explorllm.github.io](https://explorllm.github.io)

14. "LLM-Guided Task- and Affordance-Level Exploration in Reinforcement Learning (LLM-TALE)." (2025). *ICRA 2026*. [https://arxiv.org/abs/2509.16615](https://arxiv.org/abs/2509.16615)

15. "LLM-Explorer: A Plug-in Reinforcement Learning Policy Exploration Module." (2025). [https://openreview.net/forum?id=VA5P0rUZPx](https://openreview.net/forum?id=VA5P0rUZPx)

16. As, Y., et al. (2025). "ActSafe: Active Exploration with Safety Constraints for Reinforcement Learning." *ICLR 2025*. [https://arxiv.org/abs/2410.09486](https://arxiv.org/abs/2410.09486)

17. As, Y., et al. (2025). "ActSafe Project Page." [https://yardenas.github.io/actsafe](https://yardenas.github.io/actsafe)

18. McCarthy, J., et al. (2025). "Optimistic Exploration for Risk-Averse Constrained Reinforcement Learning." *ECAI 2025*. [https://arxiv.org/abs/2507.08793](https://arxiv.org/abs/2507.08793)

19. McCarthy, J., et al. (2025). "ORAC: Optimistic Risk-averse Actor Critic." *IBM Research*. [https://research.ibm.com/publications/optimistic-exploration-for-risk-averse-constrained-reinforcement-learning](https://research.ibm.com/publications/optimistic-exploration-for-risk-averse-constrained-reinforcement-learning)

20. "Safe Exploration via Policy Priors (SOOPER)." (2025). *arXiv:2601.19612*. [https://arxiv.org/html/2601.19612v1](https://arxiv.org/html/2601.19612v1)

21. "Off-Policy Safe Reinforcement Learning with Constrained Optimistic Exploration." (2026). *ICLR 2026*. [https://proceedings.iclr.cc/paper_files/paper/2026/file/c383e44d9a878d1982d9abb838bd5d8a-Paper-Conference.pdf](https://proceedings.iclr.cc/paper_files/paper/2026/file/c383e44d9a878d1982d9abb838bd5d8a-Paper-Conference.pdf)

22. Feng, M. (2025). "Risk-Aware Reinforcement Learning with Safety Constraints." *MIT PhD Thesis*. [https://dspace.mit.edu/entities/publication/f4b2f8c6-fee9-42ad-8bd6-aaf1e9cde79f](https://dspace.mit.edu/entities/publication/f4b2f8c6-fee9-42ad-8bd6-aaf1e9cde79f)

23. "Safe Exploration in Reinforcement Learning: A Generalized Formulation and Algorithms (MASE)." (2023). *NeurIPS 2023*. [https://proceedings.neurips.cc/paper_files/paper/2023/hash/5d4cd12ef6efedbf26b69b410f1f7d67-Abstract-Conference.html](https://proceedings.neurips.cc/paper_files/paper/2023/hash/5d4cd12ef6efedbf26b69b410f1f7d67-Abstract-Conference.html)

24. "Almost surely safe exploration and exploitation for deep reinforcement learning with state safety estimation." (2024). *Information Sciences*. [https://www.sciencedirect.com/science/article/abs/pii/S0020025524001749](https://www.sciencedirect.com/science/article/abs/pii/S0020025524001749)

25. "A survey of constraint formulations in safe reinforcement learning." (2024). *IJCAI 2024*. [https://dl.acm.org/doi/10.24963/ijcai.2024/913](https://dl.acm.org/doi/10.24963/ijcai.2024/913)

26. "Trajectory Planning for Safe Dual Control with Active Exploration." (2025). *arXiv:2604.15507*. [https://arxiv.org/html/2604.15507](https://arxiv.org/html/2604.15507)

27. "Consistency Trajectory Planning: High-Quality and Efficient Trajectory Optimization for Offline Model-Based Reinforcement Learning." (2025). *arXiv:2507.09534*. [https://arxiv.org/abs/2507.09534](https://arxiv.org/abs/2507.09534)

28. "Path Planning in Sparse Reward Environments: A DQN Approach with Adaptive Reward Shaping and Curriculum Learning." (2025). *Algorithms*, 19(1), 89. [https://www.mdpi.com/1999-4893/19/1/89](https://www.mdpi.com/1999-4893/19/1/89)

29. "Hierarchical reinforcement learning for handling sparse rewards in multi-goal navigation." (2024). *Artificial Intelligence Review*, 57, 156. [https://link.springer.com/article/10.1007/s10462-024-10794-3](https://link.springer.com/article/10.1007/s10462-024-10794-3)

30. "Multi-objective trajectory optimization method for industrial robots based on improved TD3 algorithm." (2025). *Scientific Reports*, 15, 41970. [https://www.nature.com/articles/s41598-025-25949-7](https://www.nature.com/articles/s41598-025-25949-7)

31. "Space Trajectory Planning with a General Reinforcement-Learning Algorithm." (2025). *Aerospace*, 12(4), 352. [https://www.mdpi.com/2226-4310/12/4/352](https://www.mdpi.com/2226-4310/12/4/352)

32. "Deep reinforcement learning trajectory planning for robotic manipulator based on simulation-efficient training." (2025). *Scientific Reports*, 15, 8286. [https://www.nature.com/articles/s41598-025-93175-2](https://www.nature.com/articles/s41598-025-93175-2)

33. "A trajectory planning and tracking method based on deep hierarchical reinforcement learning." (2025). *Journal of Intelligent and Connected Vehicles*. [https://www.sciopen.com/article/10.26599/JICV.2025.9210056](https://www.sciopen.com/article/10.26599/JICV.2025.9210056)

34. OpenDILab. "Awesome Exploration Methods in Reinforcement Learning." (Continually updated). [https://github.com/opendilab/awesome-exploration-rl](https://github.com/opendilab/awesome-exploration-rl)

35. "The impact of intrinsic rewards on exploration in Reinforcement Learning." (2025). *Neural Computing and Applications*, 37, 16269–16303. [https://link.springer.com/article/10.1007/s00521-025-11340-0](https://link.springer.com/article/10.1007/s00521-025-11340-0)

36. "Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications." (2024). *IEEE Access*, 12, 175473–175500. [https://arxiv.org/html/2408.10215v1](https://arxiv.org/html/2408.10215v1)

