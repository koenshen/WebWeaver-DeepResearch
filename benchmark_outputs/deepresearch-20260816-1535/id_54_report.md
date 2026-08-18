

# Machine Learning Models for Asset Allocation in FinTech: A Comparative Analysis and the Case for Hybrid Frameworks

## 1. Introduction

The application of machine learning (ML) to asset allocation and portfolio optimization has become a central pillar of modern FinTech. Since Harry Markowitz introduced Modern Portfolio Theory (MPT) in 1952, the field has evolved from a single-period quadratic optimization problem into a rich ecosystem of models that range from classical mean-variance (MV) optimization to the Black-Litterman (BL) Bayesian framework and, more recently, to deep learning (DL) and deep reinforcement learning (DRL) architectures. Each generation of models has addressed specific shortcomings of its predecessors, yet each also introduces new limitations. This report systematically examines the core differences among these three families of models across three dimensions—**risk measurement**, **return prediction**, and **asset allocation**—and then evaluates the growing body of research on hybrid frameworks that seek to combine their respective strengths into a more general-purpose and effective modeling paradigm.

---

## 2. Core Differences Among Model Families

### 2.1. Mean-Variance Optimization (Markowitz, 1952)

**Risk Measurement.** The MV model defines risk as the variance (or standard deviation) of portfolio returns, measured via the historical covariance matrix of asset returns. The optimization problem is formulated as:

\[
\max_w \left( w^T \mu - \frac{\gamma}{2} w^T \Sigma w \right)
\]

where \(w\) are asset weights, \(\mu\) is the vector of expected returns, \(\Sigma\) the covariance matrix, and \(\gamma\) the risk-aversion parameter (Markowitz, 1952). This approach assumes that returns are multivariate normally distributed and that the covariance structure is stationary over time.

**Return Prediction.** Expected returns are estimated directly from historical sample means. This backward-looking approach is the model's Achilles' heel: small estimation errors in \(\mu\) lead to extreme, unstable, and highly concentrated portfolio weights (Michaud, 1989). The model provides no mechanism for incorporating forward-looking views or qualitative information.

**Asset Allocation.** The optimization yields a single-period allocation on the efficient frontier. However, the resulting portfolios are often unintuitive—concentrating 40–50% in a single asset—and are highly sensitive to the input parameters. Updating the data by one month can produce dramatically different allocations (MarketXLS, 2024).

**Key Limitations.**
- Extreme sensitivity to input parameters (Black & Litterman, 1992).
- Assumption of normal distributions, which fails in real markets with fat tails and asymmetric correlations (Ryan O'Connell, CFA, 2024).
- Inability to incorporate investor views or qualitative insights.
- Unstable, concentrated portfolios that are difficult to implement in practice.

---

### 2.2. Black-Litterman Model (Black & Litterman, 1990, 1992)

**Risk Measurement.** The BL model retains the covariance matrix \(\Sigma\) from MPT but introduces a Bayesian framework that distinguishes between two sources of uncertainty: (1) the uncertainty in the market equilibrium prior, scaled by a parameter \(\tau\) (typically 0.025–0.05), and (2) the uncertainty in each investor view, captured by the diagonal matrix \(\Omega\). The posterior covariance of the blended expected returns is:

\[
\text{Cov}(E(R)) = \left[(\tau\Sigma)^{-1} + P^T\Omega^{-1}P\right]^{-1}
\]

This precision-weighted approach means that risk measurement is adaptive: views with high confidence (low \(\Omega\)) exert greater influence on the posterior distribution (Idzorek, 2007; He & Litterman, 2002).

**Return Prediction.** Instead of relying solely on historical averages, the BL model starts with **implied equilibrium excess returns** derived via reverse optimization:

\[
\Pi = \lambda \Sigma w_{\text{mkt}}
\]

where \(\lambda\) is the risk-aversion coefficient and \(w_{\text{mkt}}\) are market-capitalization weights. These equilibrium returns represent the market's collective expectation. The investor then specifies absolute or relative views (encoded in the pick matrix \(P\) and view vector \(Q\)) with associated confidence levels. The posterior expected excess return is a precision-weighted average:

\[
E(R) = \left[(\tau\Sigma)^{-1} + P^T\Omega^{-1}P\right]^{-1} \left[(\tau\Sigma)^{-1}\Pi + P^T\Omega^{-1}Q\right]
\]

This Bayesian blending produces return predictions that are more stable and intuitive than historical averages (Ryan O'Connell, CFA, 2024).

**Asset Allocation.** The posterior expected returns are fed into a standard mean-variance optimizer to produce portfolio weights. Because the starting point is the market portfolio, the resulting allocations are naturally diversified and anchored to observable market weights. Small changes in views produce proportional shifts in allocations, avoiding the erratic behavior of pure MVO (MarketXLS, 2024).

**Key Limitations.**
- The model's effectiveness depends critically on the **quality of investor views**, which can be swayed by personal biases, market sentiment, or incomplete knowledge (Kahneman & Riepe, 1998; Bertsimas et al., 2012).
- Confidence calibration (\(\Omega\)) is subjective and lacks a universally accepted method.
- Assumes normally distributed returns and a stable covariance matrix—conditions that break down during market crises (Ryan O'Connell, CFA, 2024).
- The model is a **single-period framework** and does not naturally accommodate dynamic rebalancing strategies.
- The market portfolio is difficult to define in practice, as it should theoretically include all risky assets (Hudson & Thames, 2024).

---

### 2.3. Deep Learning and Deep Reinforcement Learning Models

**Risk Measurement.** Deep learning models depart from parametric assumptions about return distributions. Architectures such as Long Short-Term Memory (LSTM) networks have been shown to reduce volatility forecasting errors by **32%** compared to traditional GARCH models (Chong et al., as cited in Agal et al., 2025). More advanced frameworks use **differentiable optimization layers** that directly enforce risk parity constraints, solving:

\[
\min_{w_t} \left\| \frac{w_t \circ (\hat{\Sigma}_t w_t)}{w_t^T \hat{\Sigma}_t w_t} - b \right\|_2^2 + \lambda_1 \|w_t\|_1 + \lambda_2 \|w_t - w_{t-1}\|_2^2
\]

where \(b\) is the target risk contribution vector (Agal et al., 2025, *Scientific Reports*). This formulation enables end-to-end training through backpropagation, integrating risk management directly into the optimization process.

**Return Prediction.** Deep learning models excel at capturing complex, non-linear relationships in financial time series. Architectures explored include:
- **LSTM/GRU networks** for capturing long-term dependencies in price and volatility data (Chen et al., 2015; Nelson et al., 2017).
- **Transformers** with self-attention mechanisms for modeling long-range dependencies in time series (Vaswani et al., 2017; Zhu & Yen, 2024).
- **Generative Adversarial Networks (GANs)** combined with Transformers for generating synthetic price paths and extracting latent patterns (Zhu & Yen, 2024, arXiv:2404.02029).
- **Large Language Models (LLMs)** such as FinGPT and BloombergGPT for processing unstructured text (news, earnings calls, central bank communications) to generate return forecasts (Wu et al., 2023; Liu et al., 2023; Lee et al., 2025).

A key advantage is that DL models can incorporate **alternative data** (satellite imagery, social media sentiment, credit card transactions) that are inaccessible to traditional models (MarketXLS, 2024). However, the low signal-to-noise ratio in financial data means that shallow learning often outperforms deep learning in return prediction (Gu et al., 2020).

**Asset Allocation.** Deep learning models can be trained to optimize portfolio weights directly:
- **Deep Reinforcement Learning (DRL)** agents (e.g., using PPO, SAC, or DDPG algorithms) learn optimal trading policies through trial and error in simulated environments, explicitly handling transaction costs, market impact, and multi-period optimization (Jiang et al., 2017; Liu et al., 2021; Kochliaridis et al., 2023).
- **End-to-end neural networks** with differentiable optimization layers learn to map market data directly to portfolio weights, jointly optimizing return prediction and risk budgeting (Uysal et al., as cited in Agal et al., 2025).

**Key Limitations.**
- **Poor interpretability.** DRL agents are "black boxes" that do not fully address the interpretability of resulting strategies, limiting deployability in practice (ACM CODS-COMAD, 2025). The optimization problem and resulting strategies in MPT are appealing to human intuition, whereas DRL agents are trained by maximizing a portfolio objective using a stack of black-box DL models.
- **Overfitting risk.** ML models can find patterns in historical data that do not persist, especially in the low signal-to-noise environment of financial markets (MarketXLS, 2024).
- **Large data requirements.** DL models typically require vast amounts of high-quality data to train effectively, which may not be available for all asset classes or market regimes.
- **Regime sensitivity.** Models trained on one market regime may perform poorly when conditions fundamentally change.
- **Biased gradient updates.** Sharpe loss functions used in DL-based portfolio optimization can produce biased gradients under stochastic gradient descent when profits and losses are negative (Kubo & Nakagawa, 2025, SSRN).
- **Instability in DRL training.** DRL algorithms are known to be unstable, difficult to calibrate, and prone to convergence issues (Belantari, 2025).

---

### 2.4. Summary Comparison

| Dimension | Mean-Variance (MPT) | Black-Litterman | Deep Learning / DRL |
|---|---|---|---|
| **Risk Measurement** | Historical covariance; assumes normal distribution | Bayesian posterior combining market covariance and view uncertainty | Learned from data via LSTM, attention, or differentiable optimization layers; no parametric assumptions |
| **Return Prediction** | Historical sample means (backward-looking) | Precision-weighted blend of equilibrium returns + investor views | Data-driven forecasting via neural networks; can incorporate alternative data and unstructured text |
| **Asset Allocation** | Single-period quadratic optimization; produces concentrated, unstable weights | Bayesian prior → posterior → MVO; produces diversified, stable weights anchored to market cap | Multi-period, adaptive; learned via RL or end-to-end differentiable optimization |
| **Interpretability** | High (simple, transparent) | Medium (Bayesian structure is traceable; views are explicit) | Low ("black box"; SHAP/XAI methods are still emerging) |
| **Data Requirements** | Low (historical returns only) | Medium (covariance + market caps + views) | Very high (large datasets, alternative data) |
| **Stability** | Low (highly sensitive to inputs) | High (anchored to equilibrium) | Variable (depends on regularization and regime) |

---

## 3. Hybrid Frameworks: Combining Strengths for a More General-Purpose Model

A growing body of research demonstrates that the limitations of each model family can be mitigated by combining them. The core insight is that **each model excels at a different part of the portfolio optimization pipeline**, and a well-designed hybrid can leverage these complementary strengths.

### 3.1. Deep Learning–Enhanced Black-Litterman (Substituting Views)

The most active area of hybrid research replaces subjective human views in the BL model with objective, data-driven forecasts generated by deep learning models. This addresses the BL model's primary weakness—view subjectivity and bias—while retaining its robust Bayesian framework.

**CGL-BL Framework (Su et al., 2026, *Expert Systems with Applications*).** This framework combines:
- **CEEMDAN** (Complete Ensemble Empirical Mode Decomposition with Adaptive Noise) to decompose return time series into interpretable intrinsic mode functions (IMFs).
- **Genetic Algorithm–optimized LSTM (GLSTM)** for predicting each IMF component.
- A second **LSTM** for non-linear ensemble integration of the component forecasts.
- The resulting **CGL return predictions** are used as investor views in the Black-Litterman model.

Results: The CGL-BL portfolio achieved **49.9–70.3% excess returns** on the SSE 50 Index and **59.4–76.8%** on the DJIA Index over benchmarks, with significantly improved risk management.

**Transformer-Based DRL + BL (Kochliaridis et al., 2024, *Neural Computing and Applications*).** This hybrid proposes a Transformer-based DRL agent that learns the dynamic correlation structure between asset returns, combined with the BL model to implement a long/short strategy. The DRL agent handles the complex, non-linear market dynamics, while the BL model provides the structured Bayesian framework for portfolio construction.

**SSA-MAEMD-TCN + BL (Wang et al., 2025, arXiv:2505.01781).** This framework integrates Singular Spectrum Analysis (SSA), Multivariate Aligned Empirical Mode Decomposition (MA-EMD), and Temporal Convolutional Networks (TCN) to generate high-precision stock price forecasts as BL inputs. The hybrid approach significantly outperforms standard BL and pure DL models.

**LLM-Enhanced Black-Litterman (Lee et al., 2025, arXiv:2504.14345).** This recent work proposes using Large Language Models (LLMs) to generate not only return predictions but also **uncertainty estimates** from unstructured text (news, earnings calls, central bank communications). These uncertainty estimates are used to calibrate the confidence levels (\(\Omega\)) in the BL model, automatically down-weighting biased or unstable predictions. This bridges the gap between unstructured LLM insights and structured portfolio optimization.

### 3.2. Differentiable Risk Budgeting with Neural Networks

Agal et al. (2025, *Scientific Reports*) propose a framework that integrates: 
- **LSTM networks** for volatility forecasting and regime detection.
- A **differentiable optimization layer** that enforces risk parity constraints end-to-end.
- A **regime-switching mechanism** for dynamic risk targets.

This hybrid achieves a **Sharpe ratio of 1.38**, representing a **55% improvement** over traditional risk parity (0.89) and a **23% improvement** over the deep learning-only alternative (1.12), with a controlled volatility of 11.9% and maximum drawdown of 16.2%. The framework successfully bridges the gap between return prediction and risk management.

### 3.3. Natural Language Processing + BL for Systematic View Generation

MarketXLS (2024) describes how NLP models can process news articles, earnings call transcripts, and social media data to generate **systematic views** about asset classes, which then feed into the BL framework. This creates a **hybrid human-AI optimization process** where the BL model's Bayesian structure provides stability and interpretability, while the AI component provides scalability and objectivity.

### 3.4. Theory-Guided Machine Learning for Return Prediction

Gu et al. (2020) established theoretical foundations for neural portfolio optimization, proving that deep networks can approximate the optimal portfolio function with bounded error. More recent work has explored **theory-guided ML** that incorporates financial constraints (e.g., no-arbitrage conditions, factor model structures) into neural network architectures, combining the flexibility of DL with the economic interpretability of traditional models.

---

## 4. Toward a General-Purpose Modeling Framework

The evidence from the literature suggests several principles for building a more general-purpose and effective portfolio optimization framework:

### 4.1. Modular Architecture with Bayesian Integration

The most promising hybrid frameworks adopt a **modular pipeline**:
1. **Data Layer.** Multiple data sources (historical prices, alternative data, unstructured text, market microstructure).
2. **Forecasting Layer.** Deep learning models (LSTM, Transformers, GANs, LLMs) generate return predictions and uncertainty estimates.
3. **Bayesian Integration Layer.** The Black-Litterman framework blends these data-driven forecasts with market equilibrium priors, using the uncertainty estimates to calibrate confidence levels automatically.
4. **Optimization Layer.** A constrained optimizer (MVO, risk parity, or differentiable optimization) produces final portfolio weights.

### 4.2. Automatic Uncertainty Quantification

A critical advantage of the BL framework is its ability to quantify and propagate uncertainty. Hybrid models that generate **both predictions and prediction uncertainty** (e.g., via Bayesian neural networks, Monte Carlo dropout, or ensemble methods) can automatically calibrate the confidence levels in the BL model, reducing the subjectivity that has historically limited the BL approach.

### 4.3. Regime-Aware Dynamic Adaptation

Financial markets exhibit regime shifts (e.g., low volatility vs. crisis periods). Effective frameworks should incorporate:
- **Regime detection** using clustering or hidden Markov models.
- **Regime-dependent risk targets** (e.g., higher risk parity target during stable periods, capital preservation during crises).
- **Adaptive model selection** that weights models differently across regimes.

### 4.4. Interpretability via Economic Distillation

The "black box" problem of deep learning can be addressed through:
- **Economic distillation** of DRL models to understand which features drive allocations (ACFR, 2021).
- **Explainable AI (XAI)** techniques such as SHAP (SHapley Additive exPlanations) to identify feature importance (PMC, 2025).
- **Structured architectures** that incorporate financial theory (e.g., factor models, no-arbitrage constraints) into neural network design.

### 4.5. Practical Implementation Considerations

- **Constraint handling.** The BL model produces posterior expected returns, not final portfolio weights. These must be fed into a constrained optimizer that respects investment policy constraints (e.g., long-only, turnover limits, sector limits) (Ryan O'Connell, CFA, 2024).
- **Transaction costs.** Multi-period models (RL-based) naturally incorporate transaction costs; single-period models (MV, BL) should be augmented with turnover constraints.
- **Computational efficiency.** Differentiable optimization layers enable end-to-end training but may be computationally intensive for large-scale portfolios.

---

## 5. Conclusion

The three families of models—Mean-Variance, Black-Litterman, and Deep Learning—each offer distinct advantages and limitations across the dimensions of risk measurement, return prediction, and asset allocation. Mean-Variance provides a simple, theoretically elegant foundation but suffers from input sensitivity and unrealistic assumptions. Black-Litterman addresses these issues through a Bayesian framework that blends market equilibrium with investor views, but remains dependent on the quality and objectivity of those views. Deep learning models offer powerful, data-driven forecasting and adaptive allocation but lack interpretability and are prone to overfitting and instability.

The emerging consensus in the literature is that **no single model is sufficient** for all market conditions. The most promising direction is the development of **hybrid frameworks** that combine the strengths of multiple approaches: deep learning for objective return prediction and uncertainty quantification, the Black-Litterman Bayesian structure for stable and intuitive integration of forecasts with market equilibrium, and differentiable optimization layers for end-to-end, risk-aware portfolio construction. Such frameworks have demonstrated excess returns of 50–77% over benchmarks, Sharpe ratio improvements of 23–55%, and superior risk management during stress periods.

The path toward a truly general-purpose modeling framework lies in modular, Bayesian architectures that are **data-driven yet theoretically grounded**, **adaptive yet stable**, and **powerful yet interpretable**. As the FinTech field continues to evolve, the integration of large language models, alternative data, and differentiable programming within structured Bayesian frameworks represents the most promising research frontier.

---

## References

1. Agal, S., Zhang, Y., & India, A. (2025). A machine learning approach to risk based asset allocation in portfolio optimization. *Scientific Reports*. https://www.nature.com/articles/s41598-025-26337-x

2. Belantari, A. (2025). Deep Reinforcement Learning SAC Portfolio Optimization. *Medium*. https://medium.com/@abatrek059/deep-reinforcement-learning-sac-portfolio-optimization-part-three-9c1431f63ff9

3. Bertsimas, D., Gupta, V., & Paschalidis, I. C. (2012). Data-driven estimation in equilibrium using inverse optimization. *Mathematical Programming*, 138(1), 595-635.

4. Black, F., & Litterman, R. (1990). Asset allocation: combining investor views with market equilibrium. *Goldman Sachs Fixed Income Research*, 115(1), 7-18.

5. Black, F., & Litterman, R. (1992). Global portfolio optimization. *Financial Analysts Journal*, 48(5), 28-43.

6. Chen, K., Zhou, Y., & Dai, F. (2015). A LSTM-based method for stock returns prediction: A case study of China stock market. *IEEE International Conference on Big Data*, 2823-2824.

7. Colasanto, F., Grilli, L., Santoro, D., & Villani, G. (2022). BERT's sentiment score for portfolio optimization: a fine-tuned view in Black and Litterman model. *Neural Computing and Applications*, 34(20), 17507-17521.

8. Creamer, G. G. (2015). Can a corporate network and news sentiment improve portfolio optimization using the Black-Litterman model? *Quantitative Finance*, 15(8), 1405-1416.

9. Gu, S., Kelly, B., & Xiu, D. (2020). Empirical asset pricing via machine learning. *Review of Financial Studies*, 33(5), 2223-2273.

10. He, G., & Litterman, R. (2002). The intuition behind Black-Litterman model portfolios. *Available at SSRN 334304*. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=334304

11. Hudson & Thames. (2024). Bayesian Portfolio Optimisation: Introducing the Black-Litterman Model. https://hudsonthames.org/bayesian-portfolio-optimisation-the-black-litterman-model/

12. Idzorek, T. (2007). A step-by-step guide to the Black-Litterman model: Incorporating user-specified confidence levels. In *Forecasting Expected Returns in the Financial Markets* (pp. 17-38). Academic Press.

13. Jiang, Z., Xu, D., & Liang, J. (2017). A deep reinforcement learning framework for the financial portfolio management problem. *arXiv preprint arXiv:1706.10059*. https://arxiv.org/abs/1706.10059

14. Kahneman, D., & Riepe, M. W. (1998). Aspects of investor psychology. *Journal of Portfolio Management*, 24(4), 52-65.

15. Kochliaridis, V., Kouloumpris, E., & Vlahavas, I. (2023). Combining deep reinforcement learning with technical analysis and trend monitoring on cryptocurrency markets. *Neural Computing and Applications*, 35, 1-18.

16. Kochliaridis, V., et al. (2024). Combining transformer based deep reinforcement learning with Black-Litterman model for portfolio optimization. *Neural Computing and Applications*. https://link.springer.com/article/10.1007/s00521-024-09805-9

17. Kubo, K., & Nakagawa, K. (2025). Portfolio Optimization Using Deep Learning with Risk Aversion Utility Function. *SSRN*. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5020148

18. Lee, J., et al. (2025). LLM-Enhanced Black-Litterman Portfolio Optimization. *arXiv:2504.14345*. https://arxiv.org/html/2504.14345v2

19. Liu, X. Y., Yang, H., Gao, J., & Wang, C. D. (2021). FinRL: Deep reinforcement learning framework to automate trading in quantitative finance. *Proceedings of the Second ACM International Conference on AI in Finance*, 1-9.

20. MarketXLS. (2024). Portfolio Optimization — Black-Litterman, AI & Advanced Techniques Guide. https://marketxls.com/blog/advanced-portfolio-optimization-black-litterman-ai

21. Markowitz, H. (1952). Portfolio selection. *Journal of Finance*, 7(1), 77-91.

22. Michaud, R. O. (1989). The Markowitz optimization enigma: Is 'optimized' optimal? *Financial Analysts Journal*, 45(1), 31-42.

23. O'Connell, R. (2024). The Black-Litterman Model. https://ryanoconnellfinance.com/black-litterman-model

24. Shi, S., Li, J., Li, G., Pan, P., Chen, Q., & Sun, Q. (2022). GPM: A graph convolutional network based reinforcement learning framework for portfolio management. *Neurocomputing*, 498, 14-27.

25. Song, Z., Wang, Y., Qian, P., Song, S., Coenen, F., Jiang, Z., & Su, J. (2023). From deterministic to stochastic: an interpretable stochastic model-free reinforcement learning framework for portfolio optimization. *Applied Intelligence*, 53(12), 15188-15203.

26. Su, X., et al. (2026). Objective Black-Litterman views through deep learning: A novel hybrid model for enhanced portfolio returns. *Expert Systems with Applications*, 295, 128868. https://www.sciencedirect.com/science/article/abs/pii/S0957417425024856

27. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.

28. Wang, Z., et al. (2025). Enhancing Black-Litterman Portfolio via Hybrid Forecasting Model Combining Multivariate Decomposition and Noise Reduction. *arXiv:2505.01781*. https://arxiv.org/html/2505.01781v2

29. Wu, H., Xu, J., Wang, J., & Long, M. (2021). Autoformer: Decomposition transformers with auto-correlation for long-term series forecasting. *Advances in Neural Information Processing Systems*, 34, 22419-22430.

30. Zhu, Y., & Yen, J. (2024). Enhancing Portfolio Optimization with Transformer-GAN Integration: A Novel Approach in the Black-Litterman Framework. *arXiv:2404.02029*. https://arxiv.org/html/2404.02029v3

31. ACM CODS-COMAD. (2025). Deployability of Deep Reinforcement Learning in Portfolio Management. *Proceedings of the 8th International Conference on Data Science and Management of Data*. https://dl.acm.org/doi/10.1145/3703323.3703333

32. FE Training. (2024). Black-Litterman Model - Definition, Example, Formula, Pros & Cons. https://www.fe.training/free-resources/portfolio-management/black-litterman-model

33. PMC. (2025). Advanced investing with deep learning for risk-aligned portfolio optimization. https://pmc.ncbi.nlm.nih.gov/articles/PMC12364330/

