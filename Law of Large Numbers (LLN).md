---
type: note
status: done
tags: [math/statistics, math/probability-theory]
sources:
- "[[Statistics Basics (1st)]]"
authors:
-
---

#🃏/semantic/math/statistics #🃏/semantic/math/probability-theory

**Related:** [[Central Limit Theorem (CLT)]], [[variance]], [[mathematical expectation]], [[descriptional statistics]]

## Assumptions

For the Law of Large Numbers to hold:
1. **i.i.d. assumption**: Random variables $X_1, X_2, \ldots, X_n$ must be independent and identically distributed [[assumption of independence and identical distribution (i.i.d.)]]
	- ⚠️ **Violation of i.i.d.** (e.g., time-series dependencies, non-stationary data) makes LLN conclusions unreliable.
2. **Finite moments**: The moment of interest (e.g., $\mathbb{E}[X]$ for mean) must exist and be finite
3. **Higher moments**: For convergence of variance, skewness, kurtosis, the respective moments must exist

## Definition

The Law of Large Numbers guarantees that **as sample size increases**, sample statistics converge to their population counterparts.

### Weak Law of Large Numbers

For i.i.d. random variables $X_1, X_2, \ldots, X_n$ with finite expectation $\mu$:

$$
\lim_{n \to \infty} P\left(\left|\frac{1}{n}\sum_{i=1}^n X_i - \mu\right| \geq \varepsilon \right) = 0 \quad \text{for any } \varepsilon > 0
$$

**Interpretation:** The sample mean converges in probability to the population mean.

### Strong Law of Large Numbers

Strengthens this to almost sure convergence:

$$
P\left(\lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^n X_i = \mu \right) = 1
$$

**Interpretation:** The sample mean converges to $\mu$ with probability 1 (almost surely).

## Convergence Rates for Different Moments

Higher moments **amplify outliers**, making them noisier and slower to stabilize:

| Moment | Statistic | Convergence Speed |
|--------|-----------|-------------------|
| 1st | [[mathematical expectation\|Mean]] | Fast (~$\sqrt{n}$) |
| 2nd | [[variance\|Variance]] | Moderate |
| 3rd | [[skewness\|Skewness]] | Slow |
| 4th | [[kurtosis\|Kurtosis]] | Very slow |


## Demonstration

>[!info]- Code snippet: LLN for all 4 moments convergence
>```python
>import matplotlib.pyplot as plt
>import numpy as np
>from scipy import stats
>
>rng = np.random.default_rng(42)
>
># Population: lognormal (skewed, heavy-tailed)
>X_stream = rng.lognormal(mean=2.0, sigma=0.8, size=50_000)
>
># True population moments
>pop_mean = np.mean(X_stream)
>pop_var = np.var(X_stream, ddof=0)
>pop_skew = stats.skew(X_stream, bias=False)
>pop_kurt = stats.kurtosis(X_stream, fisher=True, bias=False)
>
># Compute running moments
>n_vals = np.unique(np.geomspace(10, len(X_stream), num=200).astype(int))
>running_mean = np.empty(len(n_vals))
>running_var = np.empty(len(n_vals))
>running_skew = np.empty(len(n_vals))
>running_kurt = np.empty(len(n_vals))
>
>for i, n in enumerate(n_vals):
>    X_n = X_stream[:n]
>    running_mean[i] = np.mean(X_n)
>    running_var[i] = np.var(X_n, ddof=0)
>    running_skew[i] = stats.skew(X_n, bias=False)
>    running_kurt[i] = stats.kurtosis(X_n, fisher=True, bias=False)
>
># Plot all 4 moments
>fig, axes = plt.subplots(2, 2, figsize=(14, 9))
>
>axes[0, 0].plot(n_vals, running_mean, alpha=0.7, label="Sample mean")
>axes[0, 0].axhline(pop_mean, color="red", linestyle="--", linewidth=2, label=f"Pop mean = {pop_mean:.2f}")
>axes[0, 0].set_title("Mean convergence (fast)")
>axes[0, 0].set_xlabel("Sample size (n)")
>axes[0, 0].set_xscale("log")
>axes[0, 0].legend()
>axes[0, 0].grid(True, alpha=0.3)
>
>axes[0, 1].plot(n_vals, running_var, alpha=0.7, label="Sample var", color="orange")
>axes[0, 1].axhline(pop_var, color="red", linestyle="--", linewidth=2, label=f"Pop var = {pop_var:.2f}")
>axes[0, 1].set_title("Variance convergence (moderate)")
>axes[0, 1].set_xlabel("Sample size (n)")
>axes[0, 1].set_xscale("log")
>axes[0, 1].legend()
>axes[0, 1].grid(True, alpha=0.3)
>
>axes[1, 0].plot(n_vals, running_skew, alpha=0.7, label="Sample skew", color="green")
>axes[1, 0].axhline(pop_skew, color="red", linestyle="--", linewidth=2, label=f"Pop skew = {pop_skew:.2f}")
>axes[1, 0].set_title("Skewness convergence (slow)")
>axes[1, 0].set_xlabel("Sample size (n)")
>axes[1, 0].set_xscale("log")
>axes[1, 0].legend()
>axes[1, 0].grid(True, alpha=0.3)
>
>axes[1, 1].plot(n_vals, running_kurt, alpha=0.7, label="Sample kurt", color="purple")
>axes[1, 1].axhline(pop_kurt, color="red", linestyle="--", linewidth=2, label=f"Pop kurt = {pop_kurt:.2f}")
>axes[1, 1].set_title("Kurtosis convergence (very slow)")
>axes[1, 1].set_xlabel("Sample size (n)")
>axes[1, 1].set_xscale("log")
>axes[1, 1].legend()
>axes[1, 1].grid(True, alpha=0.3)
>
>plt.suptitle("LLN: All 4 moments converge to population values (but at different speeds)")
>plt.tight_layout()
>plt.show()
>```

## Review questions

What are the assumptions, formula (weak law), and intuition for Law of Large Numbers?
?
- **Assumptions**: i.i.d. random variables $X_1, X_2, \ldots, X_n$ with finite mean $\mu$
- **Formula (Weak Law)**: $\lim_{n \to \infty} P\left(\left|\bar X_n - \mu\right| \geq \varepsilon \right) = 0$ for any $\varepsilon > 0$
- **Intuition**: As sample size $n$ grows, the sample mean $\bar X_n$ converges to the population mean $\mu$ (deviations become negligible)

Why do higher moments (variance, skewness, kurtosis) converge slower than the mean?
?
- Higher moments **amplify outliers** (variance uses $X^2$, skewness $X^3$, kurtosis $X^4$)
- This makes them much noisier and slower to stabilize
- **Convergence speed**: mean (fast) → variance (moderate) → skewness (slow) → kurtosis (very slow)

