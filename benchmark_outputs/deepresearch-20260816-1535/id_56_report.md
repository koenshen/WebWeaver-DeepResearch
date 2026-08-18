

# Solving First-Price Sealed-Bid Auctions with Two Asymmetric Bidders: A Comprehensive Research Report

## 1. Introduction

In a first-price sealed-bid auction with two bidders, each bidder \(i\) draws a private valuation \(v_i\) independently from a distribution \(F_i\) on support \([v_i, \bar{v}_i]\) (with density \(f_i\)), submits a bid \(b_i\), and pays his bid if he wins. When the two distributions differ ex ante (i.e., \(F_1 \neq F_2\)), the auction is said to be *asymmetric*. Unlike the symmetric case — where a closed-form equilibrium bid function \(b(v) = \mathbb{E}[\max_{j\neq i} v_j \mid v_j \leq v]\) exists — asymmetric first-price auctions generally do not admit simple closed-form solutions. However, a rich theoretical and numerical literature has established that an equilibrium exists, is unique, and can be characterized via a system of ordinary differential equations (ODEs) for the inverse bid functions. This report surveys the general methods available for solving such auctions.

---

## 2. Existence and Uniqueness of Equilibrium

The existence of a pure-strategy Bayesian Nash equilibrium for two asymmetric bidders was first established by **Maskin and Riley (2000a)** and **Lebrun (1999)**. The equilibrium bid functions are strictly increasing, continuous, and differentiable almost everywhere. Uniqueness is more subtle:

- **Maskin and Riley (2003)** prove uniqueness for two bidders under the assumption that the valuation distributions have a common lower bound and satisfy a log-concavity condition at the lower extremity.
- **Lebrun (2006)** proves uniqueness requiring log-concavity of the distribution functions.
- **A very recent paper (2025/2026)** proves uniqueness under only the assumptions that the distributions have a common support \([0,1]\) and are continuously differentiable with strictly positive densities, removing the need for log-concavity or mass points at the lower boundary. See “Uniqueness of equilibrium in asymmetric first-price auctions,” *Economics Letters*, 2026 (available at [https://www.sciencedirect.com/science/article/abs/pii/S0165176526001369](https://www.sciencedirect.com/science/article/abs/pii/S0165176526001369)).

Thus, for a wide class of distributions, the equilibrium is unique.

---

## 3. The General Method: The System of Differential Equations

The standard approach, pioneered by Maskin and Riley (2000a), works with **inverse bid functions** rather than bid functions directly. Let \(\beta_i(v)\) be the equilibrium bid of bidder \(i\) with valuation \(v\), and define \(\phi_i(b) = \beta_i^{-1}(b)\) (the valuation that leads to a bid of \(b\)).

**Maskin and Riley (2000a)** derive the following system of ODEs for the inverse bid functions \(\phi_1(b)\), \(\phi_2(b)\):

\[
\frac{F_1'(\phi_1(b))}{F_1(\phi_1(b))} \cdot \phi_1'(b) = \frac{1}{\phi_2(b) - b}
\]
\[
\frac{F_2'(\phi_2(b))}{F_2(\phi_2(b))} \cdot \phi_2'(b) = \frac{1}{\phi_1(b) - b}
\]

**Source:** Maskin & Riley (2000a), “Asymmetric Auctions,” *Review of Economic Studies*, 67(3), 413–438. Equations (2.12) in the original paper: [http://www.econ.ucla.edu/riley/research/asyRES.PDF](http://www.econ.ucla.edu/riley/research/asyRES.PDF)

### 3.1 Boundary Conditions

Let \(b_*\) be the minimum bid and \(b^*\) the maximum bid in equilibrium. The boundary conditions are:

\[
\phi_i(b_*) = \underline{v}_i, \quad \phi_i(b^*) = \bar{v}_i, \quad i=1,2
\]

where \(b^*\) is the **common maximum bid** (the highest valuation bidder bids the same amount). A key intermediate condition is that at the upper end:

\[
\beta_1(\bar{v}_1) = \beta_2(\bar{v}_2) = b^*
\]

If the lower supports differ, the lower boundary may involve a “gap” or a “bunching” region. **Maskin and Riley (2000a)** also provide a boundary condition for the case where the supports differ:

\[
b_* = \arg\max_b (b - \underline{v}_1) F_2(b) \quad \text{or} \quad b_* = \arg\max_b (b - \underline{v}_2) F_1(b)
\]

depending on the ordering of the lower bounds.

### 3.2 Equivalent Formulation in Terms of \(\ell_i(b) = F_i(\phi_i(b))\)

An equivalent and more numerically convenient formulation uses \(\ell_i(b) = F_i(\phi_i(b))\), the probability that bidder \(i\)'s valuation is below \(\phi_i(b)\). For two bidders, the system becomes:

\[
1 = [F_1^{-1}(\ell_1(b)) - b] \cdot \frac{\ell_2'(b)}{\ell_2(b)}
\]
\[
1 = [F_2^{-1}(\ell_2(b)) - b] \cdot \frac{\ell_1'(b)}{\ell_1(b)}
\]

with boundary conditions \(\ell_i(b_*) = F_i(\underline{v}_i)\), \(\ell_i(b^*) = 1\).

**Source:** Gayle & Richard (2008), “Numerical Solutions of Asymmetric, First-Price, Independent Private Values Auctions,” *Computational Economics*, 32, 387–414. Equations (3) for the general \(n\)-bidder case: [https://capcp.la.psu.edu/wp-content/uploads/sites/11/2020/07/NumericalSolutions.pdf](https://capcp.la.psu.edu/wp-content/uploads/sites/11/2020/07/NumericalSolutions.pdf)

---

## 4. Analytic Solutions for Special Cases

While no general closed-form solution exists, several important special cases yield analytic solutions.

### 4.1 Uniform Distributions (Kaplan & Zamir, 2012)

The most comprehensive analytic solution is for two bidders with **uniform distributions** on \([v_1, \bar{v}_1]\) and \([v_2, \bar{v}_2]\), with or without a minimum bid \(m\). **Kaplan and Zamir (2012)** derive explicit piecewise solutions for the equilibrium bid functions. The solution involves different regimes depending on the parameter values (e.g., whether the supports overlap, whether one distribution stochastically dominates the other).

**Key result:** For two bidders with \(v_i \sim U[a_i, \bar{v}_i]\) and no minimum bid, the equilibrium bid functions are quadratic in the valuations over certain regions and linear in others.

**Source:** Kaplan & Zamir (2012), “Asymmetric first-price auctions with uniform distributions: analytic solutions to the general case,” *Economic Theory*, 50, 269–302. [https://link.springer.com/article/10.1007/s00199-010-0563-9](https://link.springer.com/article/10.1007/s00199-010-0563-9)

### 4.2 Shifted Distributions (Maskin & Riley, 2000a)

If the weak buyer’s valuation is uniform on \([0,1]\) and the strong buyer’s valuation is uniform on \([2,3]\), an equilibrium exists where the strong buyer always bids 1, and the weak buyer bids his valuation. This is a corner solution due to the non-overlapping supports.

### 4.3 Stretched Distributions (Maskin & Riley, 2000a)

If \(F_w\) is uniform on \([0, 1/(1+z)]\) and \(F_s\) is uniform on \([0, 1/(1-z)]\) for \(z>0\), the inverse bid functions are:

\[
\phi_w(b) = \frac{1}{2}b + \frac{1}{2}z b^2, \quad \phi_s(b) = \frac{1}{2}b - \frac{1}{2}z b^2
\]

**Source:** Maskin & Riley (2000a), Example 2, pp. 418–419: [http://www.econ.ucla.edu/riley/research/asyRES.PDF](http://www.econ.ucla.edu/riley/research/asyRES.PDF)

### 4.4 Distributions with Mass Points (Maskin & Riley, 2000a)

Example 3 considers two-point distributions where the weak buyer has probability mass at both 0 and 2, while the strong buyer has mass only at 2. The equilibrium involves mixed strategies and can be solved analytically.

### 4.5 Linear Bid Functions (Cheng, 2006)

Harrison Cheng (2006) identifies a class of distribution pairs that lead to **linear bidding strategies**. For exponential-type distributions, linear equilibrium strategies exist.

---

## 5. Numerical Methods

Since closed-form solutions are rare, the primary general method for solving asymmetric first-price auctions is numerical.

### 5.1 The Backward Shooting Method (Marshall, Meurer, Richard, & Stromquist, 1994)

**MMRS (1994)** developed the foundational numerical algorithm:

1. **Transformation:** Define \(h_i(t) = F_i(\phi_i(t))\) (or related functions).
2. **Backward solving:** Start from the unknown common maximum bid \(b^*\) and solve the system of ODEs backward toward \(b = 0\).
3. **Shooting:** Adjust \(b^*\) (the terminal condition) until the initial conditions (e.g., \(h_i(0) = 0\)) are satisfied.
4. **Taylor series expansions:** Use piecewise polynomial expansions around base points to compute the solution with high accuracy.

The authors show that forward solving is unstable (explosive), but backward solving is stable. The algorithm uses recurrence relations for Taylor coefficients derived from the ODEs.

**Source:** Marshall, Meurer, Richard, & Stromquist (1994), “Numerical Analysis of Asymmetric First Price Auctions,” *Games and Economic Behavior*, 7, 193–220. [https://capcp.la.psu.edu/wp-content/uploads/sites/11/numericalanalysis.pdf](https://capcp.la.psu.edu/wp-content/uploads/sites/11/numericalanalysis.pdf)

### 5.2 The Gayle–Richard Algorithm (2008)

**Gayle and Richard (2008)** extend the MMRS approach to handle arbitrary distributions (not just uniform) and provide a fully automated, robust algorithm:

- The algorithm works with \(\ell_i(t) = F_i(\lambda_i(t))\).
- It uses a similar backward Taylor-series expansion method.
- The terminal value \(t^*\) (common maximum bid) is found by minimizing the sum of squared deviations of the initial conditions.
- The method automatically handles different support boundaries and reserve prices.

**Source:** Gayle & Richard (2008), “Numerical Solutions of Asymmetric, First-Price, Independent Private Values Auctions,” *Computational Economics*, 32, 387–414. [https://capcp.la.psu.edu/wp-content/uploads/sites/11/2020/07/NumericalSolutions.pdf](https://capcp.la.psu.edu/wp-content/uploads/sites/11/2020/07/NumericalSolutions.pdf)

### 5.3 The Hubbard–Paarsch Computational Framework (2014)

**Hubbard and Paarsch (2014)** provide a comprehensive survey of computational methods for solving asymmetric auction models. They categorize approaches into:

- **Direct methods:** Solving the ODE system via shooting or collocation.
- **Indirect methods:** Using the mechanism design approach (Myerson, 1981) to compute virtual valuations and then deriving bids.
- **Simulation-based methods:** For more complex settings.

**Source:** Hubbard & Paarsch (2014), “On the Numerical Solution of Equilibria in Auction Models with Asymmetries within the Private-Values Paradigm,” in *Handbook of Computational Economics*, Vol. 3, 37–115.

### 5.4 The Kirkegaard Approach: Working with Winning Probabilities (2005, 2009)

**Kirkegaard (2005, 2009)** proposes an alternative approach that avoids solving the ODE system directly. Instead:

- Focus on the equilibrium **winning probability function** \(q_i(v)\) (the probability that bidder \(i\) with valuation \(v\) wins).
- The equilibrium bid is given by \(b_i(v) = v - \frac{\int_0^v q_i(x) dx}{q_i(v)}\) (derived from the envelope theorem).
- The winning probabilities must satisfy a system of integral equations that can be solved numerically.
- This approach often requires less computation and provides cleaner comparative statics.

**Source:** Kirkegaard (2009), “Asymmetric first price auctions,” *Journal of Economic Theory*, 144(4), 1617–1635. [https://www.sciencedirect.com/science/article/pii/S0022053109000295](https://www.sciencedirect.com/science/article/pii/S0022053109000295)

### 5.5 Perturbation Methods (Fibich, Gavious, & Sela, 2002–2004)

For **small asymmetries**, Fibich, Gavious, and Sela develop perturbation methods:

- Expand the equilibrium around the symmetric benchmark.
- The first-order effect of asymmetry depends only on the sum of the distribution perturbations.
- This yields simple analytic approximations valid for small deviations from symmetry.

**Source:** Fibich et al., “Revenue Equivalence in Asymmetric Auctions,” [https://www.math.tau.ac.il/~fibich/Manuscripts/RET2.pdf](https://www.math.tau.ac.il/~fibich/Manuscripts/RET2.pdf)

---

## 6. Practical Implementation Steps

To solve a two-bidder asymmetric first-price auction with arbitrary distributions \(F_1, F_2\):

1. **Check existence conditions:** Ensure distributions are continuous, strictly increasing, and have no atoms (or handle atoms with the Maskin–Riley boundary conditions).
2. **Set up the ODE system:** Use the inverse bid function formulation:
   \[
   \phi_1'(b) = \frac{F_1(\phi_1(b))}{F_1'(\phi_1(b))} \cdot \frac{1}{\phi_2(b) - b}, \quad \phi_2'(b) = \frac{F_2(\phi_2(b))}{F_2'(\phi_2(b))} \cdot \frac{1}{\phi_1(b) - b}
   \]
3. **Determine boundary conditions:**
   - If the lower supports are equal (\(\underline{v}_1 = \underline{v}_2 = \underline{v}\)), then \(b_* = \underline{v}\) and \(\phi_i(b_*) = \underline{v}\).
   - If not, the lower boundary may involve a “gap” where the bidder with the higher lower bound does not bid for low valuations.
   - The upper boundary satisfies \(\phi_1(b^*) = \bar{v}_1\), \(\phi_2(b^*) = \bar{v}_2\).
4. **Solve numerically:**
   - Use a backward shooting algorithm from the unknown \(b^*\).
   - Adjust \(b^*\) until the initial conditions at the lower bound are satisfied.
   - Implement using Taylor series expansions (MMRS) or standard ODE solvers (Runge–Kutta).
5. **Transform back:** Convert \(\phi_i(b)\) to the bid functions \(\beta_i(v) = \phi_i^{-1}(v)\).

---

## 7. Key Properties of the Equilibrium

Several robust properties hold for any two asymmetric bidders:

- **Strict monotonicity:** Bid functions are strictly increasing in valuations.
- **Ordering of aggressiveness:** The bidder with the stochastically weaker distribution (in the sense of first-order stochastic dominance) bids more aggressively, i.e., \(\beta_w(v) > \beta_s(v)\) for all \(v\) (Maskin & Riley, 2000a, Proposition 3.2).
- **Mean-preserving spread of winning probabilities:** The strong bidder’s winning probability is a mean-preserving spread of the weak bidder’s (Kirkegaard, 2005, Theorem 1).
- **Bid distribution ordering:** The strong bidder’s bid distribution first-order stochastically dominates the weak bidder’s (Kirkegaard, 2005, Proposition 2).

---

## 8. Software and Tools

- **BIDCOMP:** A program developed by John Riley available at UCLA for computing bidding strategies in asymmetric auctions ([http://www.econ.ucla.edu/riley/research/index.htm](http://www.econ.ucla.edu/riley/research/index.htm)).
- **QuantEcon:** Python examples for symmetric first-price auctions that can be extended ([https://python.quantecon.org/two_auctions.html](https://python.quantecon.org/two_auctions.html)).
- **MATLAB toolboxes:** Custom implementations based on the MMRS and Gayle–Richard algorithms are available on request from several authors.

---

## 9. Conclusion

There is no single “general formula” for solving a first-price sealed-bid auction with two asymmetric bidders, but there is a **general method**. The method consists of:

1. Transforming the problem into a system of ODEs for the inverse bid functions.
2. Solving the ODE system numerically with appropriate boundary conditions.
3. Using backward shooting (or related numerical techniques) to handle the unknown terminal bid.

This approach works for any distributions satisfying standard regularity conditions (continuity, differentiability, strictly increasing). For the special case of uniform distributions, Kaplan and Zamir (2012) provide fully analytic solutions. For small asymmetries, perturbation methods provide useful approximations. The field is mature, with well-established existence and uniqueness results, and a range of computational tools available for practical implementation.

---

## References

1. Maskin, E. & Riley, J. (2000a). “Asymmetric Auctions.” *Review of Economic Studies*, 67(3), 413–438. [http://www.econ.ucla.edu/riley/research/asyRES.PDF](http://www.econ.ucla.edu/riley/research/asyRES.PDF)

2. Maskin, E. & Riley, J. (2000b). “Equilibrium in Sealed High Bid Auctions.” *Review of Economic Studies*, 67(3), 439–454. [https://www.jstor.org/stable/2566961](https://www.jstor.org/stable/2566961)

3. Maskin, E. & Riley, J. (2003). “Uniqueness of Equilibrium in Sealed High-Bid Auctions.” *Games and Economic Behavior*, 45(2), 395–409. [https://www.sciencedirect.com/science/article/pii/S0899825603001507](https://www.sciencedirect.com/science/article/pii/S0899825603001507)

4. Lebrun, B. (1999). “First Price Auctions in the Asymmetric N Bidder Case.” *International Economic Review*, 40(1), 125–142. [https://www.jstor.org/stable/2648842](https://www.jstor.org/stable/2648842)

5. Lebrun, B. (2006). “Uniqueness of the Equilibrium in First-Price Auctions.” *Games and Economic Behavior*, 55(1), 131–151. [https://econ.laps.yorku.ca/files/2015/10/lebrunb-u.pdf](https://econ.laps.yorku.ca/files/2015/10/lebrunb-u.pdf)

6. “Uniqueness of equilibrium in asymmetric first-price auctions.” (2026). *Economics Letters*. [https://www.sciencedirect.com/science/article/abs/pii/S0165176526001369](https://www.sciencedirect.com/science/article/abs/pii/S0165176526001369)

7. Kaplan, T.R. & Zamir, S. (2012). “Asymmetric first-price auctions with uniform distributions: analytic solutions to the general case.” *Economic Theory*, 50(2), 269–302. [https://link.springer.com/article/10.1007/s00199-010-0563-9](https://link.springer.com/article/10.1007/s00199-010-0563-9)

8. Marshall, R.C., Meurer, M.J., Richard, J.-F., & Stromquist, W. (1994). “Numerical Analysis of Asymmetric First Price Auctions.” *Games and Economic Behavior*, 7(2), 193–220. [https://capcp.la.psu.edu/wp-content/uploads/sites/11/numericalanalysis.pdf](https://capcp.la.psu.edu/wp-content/uploads/sites/11/numericalanalysis.pdf)

9. Gayle, W.-R. & Richard, J.-F. (2008). “Numerical Solutions of Asymmetric, First-Price, Independent Private Values Auctions.” *Computational Economics*, 32, 387–414. [https://capcp.la.psu.edu/wp-content/uploads/sites/11/2020/07/NumericalSolutions.pdf](https://capcp.la.psu.edu/wp-content/uploads/sites/11/2020/07/NumericalSolutions.pdf)

10. Kirkegaard, R. (2009). “Asymmetric first price auctions.” *Journal of Economic Theory*, 144(4), 1617–1635. [https://www.sciencedirect.com/science/article/pii/S0022053109000295](https://www.sciencedirect.com/science/article/pii/S0022053109000295)

11. Kirkegaard, R. (2005). “A Simple Approach to Analyzing Asymmetric First Price Auctions.” Brock University Working Paper 0504. [https://brocku.ca/repec/pdf/0504.pdf](https://brocku.ca/repec/pdf/0504.pdf)

12. Hubbard, T.P. & Paarsch, H.J. (2014). “On the Numerical Solution of Equilibria in Auction Models with Asymmetries within the Private-Values Paradigm.” In *Handbook of Computational Economics*, Vol. 3, 37–115. [https://www.uoguelph.ca/economics/repec/workingpapers/2015/2015-02.pdf](https://www.uoguelph.ca/economics/repec/workingpapers/2015/2015-02.pdf)

13. Fibich, G., Gavious, A., & Sela, A. (2004). “Revenue Equivalence in Asymmetric Auctions.” *Journal of Economic Theory*, 115(2), 309–321. [https://www.math.tau.ac.il/~fibich/Manuscripts/RET2.pdf](https://www.math.tau.ac.il/~fibich/Manuscripts/RET2.pdf)

14. Griesmer, J.H., Levitan, R.E., & Shubik, M. (1967). “Toward a Study of Bidding Processes, Part IV: Games with Unknown Costs.” *Naval Research Logistics Quarterly*, 14(4), 415–433.

15. Plum, M. (1992). “Characterization and Computation of Nash-Equilibria for Auctions with Incomplete Information.” *International Journal of Game Theory*, 20(4), 393–418.

16. Cheng, H. (2006). “Ranking Auction Formats in Asymmetric Auctions.” University of Southern California Working Paper.

17. Amann, E. & Leininger, W. (1996). “Asymmetric All-Pay Auctions with Incomplete Information: The Two-Player Case.” *Games and Economic Behavior*, 14(1), 1–18.

18. Myerson, R.B. (1981). “Optimal Auction Design.” *Mathematics of Operations Research*, 6(1), 58–73.

