

# Redefining Credibility: Quasi-Experimental Estimation in the Top Five Journals, 2014–2024

## 1. Introduction

The decade from 2014 to 2024 witnessed a fundamental redefinition of credibility standards in empirical economics. The "credibility revolution," articulated by Angrist and Pischke (2010), accelerated through a wave of methodological innovations that transformed how the five core quasi-experimental estimators—instrumental variables (IV), difference-in-differences (DiD) under staggered adoption, synthetic control (SC), regression discontinuity (RD), and interactive fixed-effects (IFE) panel methods—are implemented, validated, and interpreted. The top five general-interest journals (American Economic Review, Quarterly Journal of Economics, Journal of Political Economy, Econometrica, and Review of Economic Studies) served as both the proving ground for these advances and the stage for an ongoing tension between design-based and structural approaches.

This report synthesizes the methodological transformations, inferential advances, and publication trends that have reshaped applied practice. It draws on the working paper "Tracking the Credibility Revolution across Fields" (Goldsmith-Pinkham, 2025, NBER WP 35051), which provides systematic keyword-based evidence on method mentions in 11 top journals, alongside the specific methodological contributions published in the top five.

---

## 2. The Five Core Estimators: Redefining Standards

### 2.1 Instrumental Variables: From the F ≥ 10 Rule to Weak-IV-Robust Revolution

The most dramatic revision of credibility standards occurred in IV practice. For two decades, the Stock and Yogo (2005) threshold of a first-stage F-statistic ≥ 10 served as the primary gatekeeper for instrument strength. The 2014–2024 period saw this standard systematically dismantled.

**The Power Asymmetry Problem.** Keane and Neal (2024), in their *Annual Review of Economics* survey "A Practical Guide to Weak Instruments," documented that the 2SLS t-test suffers from a "power asymmetry" that persists even at F ≥ 10: standard errors are artificially small precisely when the 2SLS estimate is close to OLS, inflating the probability of false positives. Reviewing IV papers published in the *American Economic Review* from 2011–2023, they found that approximately one-quarter of key results obtained using the t-test were overturned by the Anderson-Rubin (AR) test. They advocate abandoning the 2SLS t-test entirely and raising the acceptable F-threshold to at least 50.

**The AR and CLR Tests as New Standards.** The Anderson-Rubin (1949) test, revived through the work of Andrews, Stock, and Sun (2019, *Annual Review of Economics*), provides correct coverage regardless of instrument strength. In the just-identified case, the AR test is simply the t-test from the regression of the outcome on the first-stage fitted values, but with a variance estimator that does not suffer from the power asymmetry. For overidentified models, the conditional likelihood ratio (CLR) test of Moreira (2003), extended to heteroskedastic settings by Kleibergen (2005), is the uniformly most powerful unbiased test. The Montiel Olea and Pflueger (2013) effective F-statistic provides a similarly robust diagnostic.

**Implementation in Practice.** The Stata `weakiv` package (Finlay, Magnusson, and Schaffer, 2013) and the new `estat weakrobust` command in Stata 19 now make weak-IV-robust inference routine. Andrews, Stock, and Sun (2019) documented that in a sample of 230 IV regressions from 17 AER papers, many first-stage F-statistics fell in ranges where robust inference is essential. The practical response has been a marked increase in the reporting of AR confidence intervals and CLR tests in top-five publications.

**Key Reference:** https://www.annualreviews.org/content/journals/10.1146/annurev-economics-092123-111021

### 2.2 Difference-in-Differences under Staggered Adoption: The Heterogeneity-Robust Revolution

The most transformative methodological development of the decade was the recognition that two-way fixed effects (TWFE) regressions with staggered treatment timing and heterogeneous treatment effects produce biased estimates—potentially with the wrong sign. This insight, building on the Goodman-Bacon (2021) decomposition, sparked a family of heterogeneity-robust estimators.

**The Goodman-Bacon Decomposition.** Goodman-Bacon (2021, *Journal of Econometrics*) showed that the TWFE DiD estimator is a weighted average of all possible 2×2 DiD comparisons, some of which use already-treated units as controls ("forbidden comparisons"). When treatment effects vary over time, these comparisons introduce bias. The `bacondecomp` Stata package and `ddtiming` command allow researchers to diagnose the composition of their TWFE estimate.

**The New Estimators.** Four major approaches emerged, each published in or near the top five:

- **Callaway and Sant'Anna (2021, *Journal of Econometrics*):** Computes group-time average treatment effects ATT(g,t) using only clean comparisons between a treated cohort and never-treated or not-yet-treated units. Aggregates into event-study, group, and calendar-time parameters. Implements doubly robust estimation with covariates. The `did` R package is the most widely used implementation.

- **Sun and Abraham (2021, *Journal of Econometrics*):** The interaction-weighted (IW) estimator saturates the event-study specification with cohort-by-event-time interactions, estimating cohort-specific dynamic effects and aggregating with sample-size weights. Implemented in Stata via `eventstudyinteract` and in R via `fixest::feols(... ~ sunab(cohort, time))`.

- **Borusyak, Jaravel, and Spiess (2024, *Review of Economic Studies*):** The imputation estimator uses untreated observations to estimate a model for Y(0), then imputes counterfactuals for treated units. The difference between observed and imputed outcomes yields treatment effects. This approach is efficient, using all pre-treatment periods, and can handle non-absorbing treatments. The `didimputation` R package implements it.

- **de Chaisemartin and D'Haultfœuille (2020, *American Economic Review*):** The DID_M estimator for the contemporaneous effect of a treatment switch, using only groups that change treatment status. Extended to dynamic effects via DID_l in subsequent work. Handles non-binary, non-absorbing treatments. The `did_multiplegt` Stata package implements the full suite.

**What Comparative Simulations Show.** A comprehensive simulation study in the *Annual Review of Public Health* (Wing et al., 2024) compared these estimators across scenarios. Key findings include:
- When parallel trends holds and effects are homogeneous, all estimators perform similarly.
- With staggered adoption and heterogeneous effects, TWFE bias can be severe (up to 50% of the true effect). 
- The Borusyak-Jaravel-Spiess imputation estimator and Wooldridge (2021) extended TWFE generally have lower RMSE than Callaway-Sant'Anna and Sun-Abraham, reflecting precision gains from using all pre-treatment periods.
- Callaway-Sant'Anna and Sun-Abraham are more robust to violations of the parallel trends assumption conditional on covariates.
- The de Chaisemartin-D'Haultfœuille estimator is uniquely suited to non-absorbing treatments.

**Head-to-Head Reanalyses.** Baker, Larcker, and Wang (2022, *Journal of Financial Economics*) reanalyzed 49 published staggered DiD studies in finance and accounting. Switching from TWFE to heterogeneity-robust estimators produced qualitatively similar but often less precise estimates, with the median ratio of estimates being 1.01. However, statistical significance changed in about 20% of cases. Chiu et al. (2026) replicated this pattern in a broader reanalysis.

**Athey and Imbens (2022, *Journal of Econometrics*)** provided a design-based perspective, showing that under random assignment of treatment timing, the standard TWFE estimator is unbiased for a weighted average of treatment effects even with staggered adoption, clarifying the conditions under which the older methods remain valid.

**Key References:**
- https://www.aeaweb.org/articles?id=10.1257/aer.20181169
- https://academic.oup.com/restud/article/91/6/3253/7601390
- https://www.sciencedirect.com/science/article/abs/pii/S0304407620303948
- https://www.sciencedirect.com/science/article/abs/pii/S0304407621001445

### 2.3 Synthetic Control: From Case Studies to Formal Inference

The synthetic control method, introduced by Abadie, Diamond, and Hainmueller (2010, *JASA*), evolved from a descriptive tool for comparative case studies into a formal inferential framework.

**The Abadie (2021) Synthesis.** Abadie's *Journal of Economic Literature* article (2021) codified best practices: the importance of a convex combination of donor units, the requirement for a long pre-treatment period, the use of in-space and in-time placebo tests, and the reporting of post-treatment RMSPE ratios. He cautioned against using synthetic control when the number of pre-treatment periods is small (< 10–15) or the donor pool is limited.

**Conformal Inference Revolution.** The most significant inferential advance came from Chernozhukov, Wüthrich, and Zhu (2021, *JASA*), who introduced conformal inference for synthetic controls. Their method recasts the causal inference problem as a counterfactual prediction and structural breaks testing problem, developing permutation inference procedures that are provably robust against misspecification. The key innovation is that the p-value from a conformal test is approximately valid under weak conditions, even when the synthetic control weights are estimated with error. The method works with difference-in-differences, canonical SC, constrained Lasso, factor models, and matrix completion methods.

**Bayesian Synthetic Control.** Multiple Bayesian approaches emerged:
- Pang (2014) proposed a Bayesian multi-level factor model for synthetic control.
- Sakaguchi (2026, *Econometrics Journal*) developed identification and Bayesian inference for synthetic control with spillover effects.
- The "Bayesian infinite interactive fixed effects modeling" approach (JSM 2026) uses cumulative shrinkage process priors to handle unknown numbers of factors.

**Synthetic Difference-in-Differences.** Arkhangelsky, Athey, Hirshberg, Imbens, and Wager (2021, *American Economic Review*) proposed SDID, which combines synthetic control unit weights with DiD time weights. The estimator is doubly robust: it remains consistent if either the unit weights or the time weights correctly absorb confounding. It produces a single ATT scalar with valid jackknife and placebo inference. The `synthdid` R and Stata packages implement it. SDID has seen take-up in applied work, though the "Tracking the Credibility Revolution" paper shows that synthetic control mentions plateaued after 2020 and SDID remains rare.

**Key References:**
- https://arxiv.org/pdf/1712.09089
- https://www.aeaweb.org/articles?id=10.1257/aer.20190159
- https://www.aeaweb.org/content/file?id=12409

### 2.4 Regression Discontinuity: Bias Correction and Optimal Bandwidth Selection

The Calonico, Cattaneo, and Titiunik (2014, *Econometrica*) paper "Robust Data-Driven Inference in the Regression-Discontinuity Design" fundamentally changed RD practice. Their key insight: the MSE-optimal bandwidth for point estimation is too large for valid inference. They proposed robust bias-corrected (RBC) confidence intervals that remain valid even when using the MSE-optimal bandwidth.

**Theoretical Refinements.** Calonico, Cattaneo, and Farrell (2020, *Econometrics Journal*) established coverage error expansions for RBC confidence intervals and derived inference-optimal bandwidth choices. The optimal bandwidth for confidence intervals, h^RBC, is smaller than the MSE-optimal bandwidth and yields coverage error that decays at rate O(n^{-(2+p)/(3+p)}), faster than undersmoothing. They also developed data-driven implementations (rule-of-thumb and direct plug-in) and extended the framework to fuzzy RD, kink RD, clustered sampling, and covariate adjustment.

**Implementation.** The `rdrobust` R and Stata packages (Calonico, Cattaneo, Farrell, and Titiunik, 2018, *JASA*) implement the full suite: local polynomial point estimation, robust bias-corrected confidence intervals, data-driven bandwidth selection (MSE-optimal, CER-optimal, and various plug-in methods), and RD plots. The `rdbwselect` function provides multiple bandwidth selectors. The packages have become the de facto standard for RD analysis in top-five publications.

**Practical Impact.** The "Tracking the Credibility Revolution" paper shows that RD mentions have flattened across all fields at around 8–9 percentage points, suggesting the method has reached a natural ceiling. However, the quality of RD implementations has improved dramatically, with nearly all top-five RD papers now using `rdrobust` and reporting robustness to bandwidth choice.

**Key References:**
- https://rdpackages.github.io/references/Calonico-Cattaneo-Farrell_2020_ECTJ.pdf
- https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1453&context=r-journal

### 2.5 Interactive Fixed-Effects Panel Methods: Factor Models Unify the Toolkit

Bai's (2009, *Econometrica*) interactive fixed effects (IFE) model, which incorporates unit-specific intercepts interacted with time-varying factors, became the foundation for a new generation of panel methods.

**The Generalized Synthetic Control Method.** Xu (2017, *Political Analysis*) proposed the generalized synthetic control (GSC) method, which links synthetic control and IFE models under a unified framework. GSC first estimates an IFE model using only control group data, obtaining latent factors. It then estimates factor loadings for each treated unit by projecting pre-treatment treated outcomes onto the factor space, and imputes counterfactuals. The method handles multiple treated units, variable treatment periods, and provides standard errors. The `gsynth` R package implements it.

**Relationship to Other Methods.** The GSC framework clarifies that:
- DiD is a special case of IFE with a single factor and additive unit and time effects.
- Canonical SC is a special case with constrained weights (non-negative, sum to one).
- Matrix completion methods (Athey et al., 2018; Bai and Ng, 2020) are also special cases.

**Theoretical Advances.** Moon and Weidner (2015, *Econometrica*) provided the asymptotic theory for linear regression with an unknown number of factors as interactive fixed effects. They showed that the least squares estimator is consistent and asymptotically normal when the number of factors used in estimation is at least as large as the true number. Subsequent work extended IFE to high-dimensional settings, dynamic models, and time-varying parameters.

**Key References:**
- https://www.econometricsociety.org/publications/econometrica/2009/07/01/panel-data-models-interactive-fixed-effects
- https://www.cambridge.org/core/journals/political-analysis/article/generalized-synthetic-control-method-causal-inference-with-interactive-fixed-effects-models/B63A8BD7C239DD4141C67DA10CD0E4F3

---

## 3. Comparative Simulations and Head-to-Head Applications

### 3.1 When the Estimators Diverge

A systematic comparison by Kennedy-Shaffer (2024, *Pharmacoepidemiology*) using simulation studies found that the five estimators yield meaningfully different causal conclusions in three scenarios:

1. **When parallel trends fails but the factor model holds:** IFE and GSC methods outperform DiD and SC, which rely on different assumptions. DiD requires additive parallel trends, while SC requires that the convex combination of control units matches the treated unit's trajectory. IFE relaxes both by allowing unobserved confounders to vary over time.

2. **When treatment timing is staggered and effects are heterogeneous:** TWFE DiD can produce estimates with the wrong sign. The heterogeneity-robust DiD estimators (Callaway-Sant'Anna, Sun-Abraham, Borusyak-Jaravel-Spiess, de Chaisemartin-D'Haultfœuille) converge to the same estimand when parallel trends holds, but diverge when the parallel trends assumption is conditional on covariates (Callaway-Sant'Anna allows this, while the others require unconditional parallel trends or different conditioning sets).

3. **When the instrument is weak:** IV estimates diverge from SC and DiD estimates. The Keane and Neal (2024) simulations show that at F ≈ 10–20, 2SLS estimates are often closer to OLS than to the true effect, and OLS itself may be the better estimator. The AR test overturns t-test results in one-quarter of AER papers.

### 3.2 Head-to-Head Applications

**The Mariel Boatlift.** The reanalysis of the Mariel Boatlift natural experiment became a canonical head-to-head comparison. Peri and Yasenov (2019, *Journal of Human Resources*) used SC to study the labor market effects of the Mariel immigration, finding no significant negative effects on less-educated workers. This contradicted earlier DiD estimates. The divergence was attributed to the SC method's ability to construct a better counterfactual than the simple DiD comparison.

**Minimum Wage Studies.** The minimum wage literature has seen extensive head-to-head comparisons. Cengiz et al. (2019, *AER: Insights*) used a stacked DiD approach and found that minimum wage increases reduced employment in low-wage jobs, while earlier studies using TWFE had found mixed results. The Goodman-Bacon decomposition revealed that the TWFE estimates were contaminated by comparisons between early- and late-adopting states.

**California Proposition 99.** The canonical SC application (Abadie et al., 2010) was revisited by Arkhangelsky et al. (2021) using SDID. SDID produced a similar point estimate to canonical SC but with tighter confidence intervals, demonstrating the efficiency gains from the doubly robust approach.

---

## 4. Advances in Inference: Reshaping Applied Practice

### 4.1 Weak-IV-Robust Tests

The practical impact of the weak-IV-robust inference literature has been substantial. The new Stata 19 `estat weakrobust` command implements the CLR, AR, and Kleibergen (2005) tests for heteroskedastic and clustered data. The `weakiv` Stata package (Finlay, Magnusson, and Schaffer) provides inversion of AR and CLR tests to form confidence intervals. The Montiel Olea-Pflueger effective F-statistic is now standard in top-five publications.

Keane and Neal (2024) advocate a complete shift in practice: "applied researchers should abandon the 2SLS t-test altogether and adopt AR instead, regardless of the level of instrument strength." This represents a radical departure from the F ≥ 10 rule.

### 4.2 Heterogeneity-Robust DiD Estimators

The adoption of heterogeneity-robust DiD estimators has been rapid. The "Research Unit Tests" project (Ricardo Dahis) now requires that papers with staggered adoption use or address heterogeneity-robust methods. The *Annual Review of Public Health* guide (Wing et al., 2024) recommends estimating at least two specifications: the simple TWFE regression and one of the new estimators, with explanation of any divergence.

Key practical considerations:
- **Callaway-Sant'Anna and Sun-Abraham** are conceptually similar, with CS allowing for conditional parallel trends and doubly robust estimation.
- **Borusyak-Jaravel-Spiess** is more efficient when the parallel trends assumption is unconditional, as it uses all pre-treatment periods.
- **de Chaisemartin-D'Haultfœuille** is uniquely suited to non-absorbing treatments.
- **Stacked DiD** (Cengiz et al., 2019) is a simpler alternative that avoids the negative-weight problem by creating cohort-specific datasets.

### 4.3 Conformal and Bayesian Inference in Synthetic Control

Conformal inference (Chernozhukov, Wüthrich, and Zhu, 2021) provides exact finite-sample p-values under the assumption of exchangeability, which in the SC context translates to the assumption that the treatment assignment is independent of the counterfactual outcomes. The method is:
- **Robust to misspecification:** Valid even when the SC model is misspecified, provided the estimator is approximately consistent.
- **Flexible:** Works with SC, DiD, factor models, and matrix completion.
- **Computationally feasible:** The permutation-based p-value can be computed efficiently.

Bayesian approaches (Pang, 2014; Sakaguchi, 2026) offer a different inferential paradigm, modeling the uncertainty about factor loadings and treatment effects through posterior distributions. These methods are particularly useful when the number of pre-treatment periods is small.

### 4.4 Bias-Corrected RD with Robust Bandwidth Selection

The `rdrobust` package has become the standard for RD analysis. The recommended practice in top-five publications is:
1. Report local linear (or quadratic) estimates with a data-driven MSE-optimal bandwidth.
2. Construct robust bias-corrected confidence intervals.
3. Report sensitivity to bandwidth choice (usually using a bandwidth range of 0.5× to 2× the optimal).
4. Present RD plots with binning and local polynomial fits.

The Calonico-Cattaneo-Farrell (2020) CER-optimal bandwidth is now recommended for inference, as it minimizes coverage error rather than MSE.

### 4.5 Factor-Model Approaches for Panels

The Bai (2009) IFE estimator, implemented in the `interFE` R function and `InteractiveFixedEffectModels.jl` Julia package, allows researchers to control for unobserved common shocks with heterogeneous impacts. The Xu (2017) GSC method extends this to causal inference, providing a unified framework that encompasses DiD and SC.

The practical recommendation from Xu (2017) is to use cross-validation to select the number of factors, and to test for excessive extrapolation when the number of control units is small. The GSC method is particularly valuable when the parallel trends assumption is questionable, as it allows for time-varying unobserved confounders.

---

## 5. The Evolving Publication Record: Credible Design vs. Structural Modeling

### 5.1 Aggregate Trends across Top Five Journals

The "Tracking the Credibility Revolution across Fields" working paper (Goldsmith-Pinkham, 2025, NBER WP 35051) provides systematic evidence on method mentions in 11 top journals, including the AER, QJE, JPE, Econometrica, and REStud. Key findings:

- **As of 2024, 63% of applied micro papers mention experimental or quasi-experimental methods**, compared to 47% in finance and 39% in macro/other fields.
- **Growth outside applied micro is driven overwhelmingly by DiD.** Including DiD raises the share of finance papers mentioning any experimental/quasi-experimental method by roughly 55% versus 30% for applied micro.
- **IV trends are broadly flat across fields**, suggesting the method has reached a steady state.
- **RD mentions have flattened** at around 8–9 percentage points across all fields.
- **Synthetic control mentions plateaued after 2020**, with SDID remaining rare.
- **Structural model mentions are markedly higher in finance and macro journals**, reinforcing the pattern that these fields maintain a larger structural modeling tradition.

### 5.2 Journal-Level Variation

The paper reports substantial heterogeneity across individual journals:
- **AEJ: Applied Economics and AEJ: Economic Policy** show the highest rates of credibility revolution methods.
- **AER and QJE** show higher rates than JPE among the general-interest journals.
- **Econometrica** shows a unique pattern: it publishes a high share of methods papers, with asymptotic theory and Monte Carlo simulation appearing in 86% and 65% of papers respectively. Nonparametric estimation (58%), time series models (54%), and structural/GMM/MLE methods (54%) are far more prevalent in Econometrica than in applied journals.
- **REStud** has seen a significant increase in quasi-experimental methods, particularly with the publication of the Borusyak-Jaravel-Spiess (2024) imputation estimator.

### 5.3 The Structural vs. Design-Based Tension

The paper documents a striking gap between the methods studied in econometrics journals (dominated by nonparametric estimation, asymptotic theory, and structural methods) and those used by applied researchers (dominated by DiD and identification strategies). This gap is most pronounced in the *Journal of Econometrics*, where credibility revolution methods appear far less frequently than in applied journals.

However, the relationship is not adversarial. The paper notes that "when applied micro papers use structural models, they typically pair them with complementary research designs—a pattern far less common in finance and macro." This suggests a convergence toward a "hybrid" approach in which structural models are used to extrapolate results from quasi-experimental designs to new populations or policy counterfactuals.

### 5.4 Shifting Norms of "Credible Design"

The publication record reveals several normative shifts:

1. **Pre-registration and transparency:** The inclusion of pre-analysis plans and replication packages has become standard in top-five journals.

2. **Diagnostic testing:** The Goodman-Bacon decomposition, the Callaway-Sant'Anna pre-trend test, and the weak-IV-robust F-statistic are now expected in top-five publications.

3. **Multiple estimators:** The norm is shifting toward reporting results from multiple heterogeneity-robust estimators and explaining any divergence.

4. **Sensitivity analysis:** Robustness checks to bandwidth choice (RD), instrument strength (IV), parallel trends violation (DiD), and donor pool composition (SC) are now standard.

5. **Administrative data:** The use of administrative data, which the "Tracking the Credibility Revolution" paper tracks as a separate category, has increased dramatically, particularly in applied micro.

---

## 6. Conclusion

The 2014–2024 period represents a transformative decade for quasi-experimental methods in the top five economics journals. The five core estimators have been redefined through:

- **IV:** The shift from the F ≥ 10 rule to weak-IV-robust inference (AR/CLR tests) as the gold standard.
- **DiD:** The recognition of TWFE bias under staggered adoption and the proliferation of heterogeneity-robust estimators (Callaway-Sant'Anna, Sun-Abraham, Borusyak-Jaravel-Spiess, de Chaisemartin-D'Haultfœuille).
- **SC:** The development of formal inference through conformal prediction, Bayesian methods, and the synthetic DiD synthesis.
- **RD:** The establishment of robust bias-corrected inference and optimal bandwidth selection as standard practice.
- **IFE:** The unification of DiD and SC under the interactive fixed effects framework, with the generalized synthetic control method providing a practical implementation.

The credibility revolution continues to advance, with applied microeconomics leading the way at 63% experimental/quasi-experimental method adoption, while finance and macro lag at 47% and 39% respectively. The tension between design-based and structural approaches persists, but a hybrid model is emerging in which structural methods complement rather than compete with quasi-experimental designs. The top five journals have served as both the primary outlet for these methodological advances and the arena in which new credibility standards are established and enforced.

---

## References

1. Abadie, A. (2021). "Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects." *Journal of Economic Literature*, 59(2), 391–425. https://www.aeaweb.org/content/file?id=12409

2. Andrews, I., Stock, J.H., and Sun, L. (2019). "Weak Instruments in IV Regression: Theory and Practice." *Annual Review of Economics*, 11, 727–753. https://www.annualreviews.org/doi/10.1146/annurev-economics-063016-103756

3. Arkhangelsky, D., Athey, S., Hirshberg, D.A., Imbens, G.W., and Wager, S. (2021). "Synthetic Difference-in-Differences." *American Economic Review*, 111(12), 4088–4118. https://www.aeaweb.org/articles?id=10.1257/aer.20190159

4. Athey, S. and Imbens, G.W. (2022). "Design-based Analysis in Difference-In-Differences Settings with Staggered Adoption." *Journal of Econometrics*, 226(1), 62–79. https://www.sciencedirect.com/science/article/abs/pii/S0304407621000488

5. Bai, J. (2009). "Panel Data Models with Interactive Fixed Effects." *Econometrica*, 77(4), 1229–1279. https://www.econometricsociety.org/publications/econometrica/2009/07/01/panel-data-models-interactive-fixed-effects

6. Borusyak, K., Jaravel, X., and Spiess, J. (2024). "Revisiting Event-Study Designs: Robust and Efficient Estimation." *Review of Economic Studies*, 91(6), 3253–3285. https://academic.oup.com/restud/article/91/6/3253/7601390

7. Callaway, B. and Sant'Anna, P.H.C. (2021). "Difference-in-Differences with Multiple Time Periods." *Journal of Econometrics*, 225(2), 200–230. https://www.sciencedirect.com/science/article/abs/pii/S0304407620303948

8. Calonico, S., Cattaneo, M.D., and Farrell, M.H. (2020). "Optimal Bandwidth Choice for Robust Bias-Corrected Inference in Regression Discontinuity Designs." *Econometrics Journal*, 23(2), 192–210. https://academic.oup.com/ectj/article/23/2/192/5625071

9. Calonico, S., Cattaneo, M.D., and Titiunik, R. (2014). "Robust Data-Driven Inference in the Regression-Discontinuity Design." *Econometrica*, 82(6), 2295–2326. https://journals.sagepub.com/doi/10.1177/1536867X1401400413

10. Chernozhukov, V., Wüthrich, K., and Zhu, Y. (2021). "An Exact and Robust Conformal Inference Method for Counterfactual and Synthetic Controls." *Journal of the American Statistical Association*, 116(536), 1849–1864. https://arxiv.org/pdf/1712.09089

11. de Chaisemartin, C. and D'Haultfœuille, X. (2020). "Two-Way Fixed Effects Estimators with Heterogeneous Treatment Effects." *American Economic Review*, 110(9), 2964–2996. https://www.aeaweb.org/articles?id=10.1257/aer.20181169

12. Goldsmith-Pinkham, P. (2025). "Tracking the Credibility Revolution across Fields." NBER Working Paper 35051. https://www.nber.org/system/files/working_papers/w35051/w35051.pdf

13. Goodman-Bacon, A. (2021). "Difference-in-Differences with Variation in Treatment Timing." *Journal of Econometrics*, 225(2), 254–277. https://www.sciencedirect.com/science/article/abs/pii/S0304407621001445

14. Keane, M. and Neal, T. (2024). "A Practical Guide to Weak Instruments." *Annual Review of Economics*, 16, 185–212. https://www.annualreviews.org/content/journals/10.1146/annurev-economics-092123-111021

15. Moon, H.R. and Weidner, M. (2015). "Linear Regression for Panel with Unknown Number of Factors as Interactive Fixed Effects." *Econometrica*, 83(4), 1543–1579. https://users.ox.ac.uk/~econ0610/ecta9382.pdf

16. Sun, L. and Abraham, S. (2021). "Estimating Dynamic Treatment Effects in Event Studies with Heterogeneous Treatment Effects." *Journal of Econometrics*, 225(2), 175–199. https://lsun20.github.io/event_studies_slides.pdf

17. Wing, C., Yozwiak, M., Hollingsworth, A., Freedman, S., and Simon, K. (2024). "Designing Difference-in-Difference Studies with Staggered Treatment Adoption: Key Concepts and Practical Guidelines." *Annual Review of Public Health*, 45, 485–505. https://www.annualreviews.org/content/journals/10.1146/annurev-publhealth-061022-050825

18. Xu, Y. (2017). "Generalized Synthetic Control Method: Causal Inference with Interactive Fixed Effects Models." *Political Analysis*, 25(1), 57–76. https://www.cambridge.org/core/journals/political-analysis/article/generalized-synthetic-control-method-causal-inference-with-interactive-fixed-effects-models/B63A8BD7C239DD4141C67DA10CD0E4F3

