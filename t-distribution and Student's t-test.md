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

**Related:** [[Central Limit Theorem (CLT)]], [[variance]], [[mathematical expectation]], [[chi-square distribution for sample variance]]

## Assumptions

⚠️ **Required for valid t-test:**
1. **Data is i.i.d.**: Observations must be independent and identically distributed
2. **Population is approximately normal** (especially for small $n < 30$)
3. **Random sampling** from the population
4. **For two-sample t-test**: Equal variances (homoscedasticity) or use Welch's correction

## Definition

The **t-distribution** (Student's t-distribution) is used when:
- The population standard deviation $\sigma$ is **unknown**
- We estimate it using the sample standard deviation $s$
- Sample size $n$ is small to moderate

### t-Statistic

When $\sigma$ is unknown, the CLT-based z-score is replaced by:

$$
t = \frac{\bar X - \mu}{s / \sqrt{n}}
$$

where:
- $\bar X$ is the sample mean
- $\mu$ is the hypothesized population mean
- $s$ is the sample standard deviation: $s = \sqrt{\frac{1}{n-1}\sum_{i=1}^n(X_i - \bar X)^2}$
- $n$ is the sample size

This statistic follows a **t-distribution with $n-1$ degrees of freedom**:

$$
t \sim t_{n-1}
$$

### Properties of t-Distribution

1. **Symmetric around 0** (like standard normal)
2. **Heavier tails** than normal distribution (more probability in extremes)
3. **Degrees of freedom (df)**: $df = n - 1$ for one-sample test
4. **Converges to standard normal** as $n \to \infty$ (for $n > 30$, practically indistinguishable)

## t-Distribution vs Normal Distribution

| Aspect | Normal $\mathcal{N}(0,1)$ | t-Distribution $t_{\nu}$ |
|--------|---------------------------|--------------------------|
| **When to use** | $\sigma$ known | $\sigma$ unknown, estimated by $s$ |
| **Tails** | Thinner | Heavier (more outliers) |
| **Parameters** | None (standard) | Degrees of freedom $\nu = n-1$ |
| **Shape for small $n$** | Fixed | Wider, flatter |
| **Convergence** | - | $t_{\nu} \to \mathcal{N}(0,1)$ as $\nu \to \infty$ |

## Types of t-Tests

### 1. One-Sample t-Test

**Purpose:** Test if a sample mean differs from a hypothesized population mean $\mu_0$.

**Hypotheses:**
- $H_0: \mu = \mu_0$ (null hypothesis)
- $H_1: \mu \neq \mu_0$ (two-sided alternative)

**Test statistic:**

$$
t = \frac{\bar X - \mu_0}{s / \sqrt{n}} \sim t_{n-1}
$$

**Decision:** Reject $H_0$ if $|t| > t_{\alpha/2, n-1}$ (critical value from t-table).

### 2. Two-Sample t-Test (Independent Samples)

**Purpose:** Test if two independent samples have different means.

**Hypotheses:**
- $H_0: \mu_1 = \mu_2$
- $H_1: \mu_1 \neq \mu_2$

**Test statistic (equal variances assumed):**

$$
t = \frac{\bar X_1 - \bar X_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t_{n_1 + n_2 - 2}
$$

where $s_p$ is the pooled standard deviation:

$$
s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}}
$$

**Welch's t-test** (unequal variances): Uses modified df, more robust.

### 3. Paired t-Test

**Purpose:** Test if paired observations have a mean difference of zero (e.g., before-after measurements).

**Test statistic:**

$$
t = \frac{\bar D}{s_D / \sqrt{n}} \sim t_{n-1}
$$

where $D_i = X_{i,\text{after}} - X_{i,\text{before}}$ are the paired differences.

## Confidence Intervals

### One-Sample CI for $\mu$

$$
\bar X \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}
$$

**Interpretation:** We are $(1-\alpha) \times 100\%$ confident that $\mu$ lies in this interval.

### Example
For $n=20$, $\bar X = 50$, $s = 5$, and 95% CI ($\alpha = 0.05$):
- $df = 19$, $t_{0.025, 19} \approx 2.093$
- $CI = 50 \pm 2.093 \cdot \frac{5}{\sqrt{20}} = 50 \pm 2.34 = [47.66, 52.34]$

## Demonstration

>[!info]- Code snippet: Compare t-distribution to normal
>```python
>import matplotlib.pyplot as plt
>import numpy as np
>from scipy import stats
>
>x = np.linspace(-4, 4, 500)
>
>plt.figure(figsize=(12, 6))
>plt.plot(x, stats.norm.pdf(x), label="Normal N(0,1)", linewidth=2, color="black")
>
>for df in [1, 3, 10, 30]:
>    plt.plot(x, stats.t.pdf(x, df=df), label=f"t(df={df})", alpha=0.7)
>
>plt.title("t-Distribution vs Normal: Heavier tails for small df")
>plt.xlabel("x")
>plt.ylabel("Density")
>plt.legend()
>plt.grid(True, alpha=0.3)
>plt.show()
>```

>[!info]- Code snippet: One-sample t-test
>```python
>import numpy as np
>from scipy import stats
>
>rng = np.random.default_rng(42)
>
># Sample from N(50, 5^2), n=20
>sample = rng.normal(loc=50, scale=5, size=20)
>
># Test H0: mu = 48 (should reject since true mu=50)
>mu_0 = 48.0
>t_stat, p_value = stats.ttest_1samp(sample, popmean=mu_0)
>
>print(f"Sample mean: {np.mean(sample):.2f}")
>print(f"Sample std: {np.std(sample, ddof=1):.2f}")
>print(f"t-statistic: {t_stat:.3f}")
>print(f"p-value: {p_value:.4f}")
>print(f"Reject H0 at α=0.05? {p_value < 0.05}")
>```

## When to Use t-Test vs z-Test

| Scenario | Use |
|----------|-----|
| $\sigma$ known, any $n$ | **z-test** (normal distribution) |
| $\sigma$ unknown, $n < 30$ | **t-test** (t-distribution) |
| $\sigma$ unknown, $n \geq 30$ | **t-test** (or z-test, very similar) |
| Non-normal population, small $n$ | Consider non-parametric tests |
| Non-normal population, large $n$ | **t-test** (CLT kicks in) |

## Practical Considerations

### Advantages
- Accounts for uncertainty in estimating $\sigma$ with $s$
- More conservative (wider CIs, harder to reject $H_0$) for small samples
- Robust to mild deviations from normality for moderate $n$

### Limitations
- Assumes population is approximately normal (critical for $n < 30$)
- Sensitive to outliers (especially for small $n$)
- Equal variance assumption in two-sample test (use Welch's if violated)

### Robustness
- For $n > 30$: CLT makes t-test fairly robust to non-normality
- For heavily skewed data: Consider transformations (log, sqrt) or non-parametric tests
- For outliers: Use robust alternatives (trimmed mean, Wilcoxon test)

## Review questions

What is the t-distribution and when is it used?
?
- The t-distribution is used when population standard deviation $\sigma$ is **unknown** and must be estimated from sample ($s$)
- It has **heavier tails** than the normal distribution, accounting for uncertainty in $s$
- Parameterized by degrees of freedom: $df = n-1$ for one-sample test
- Converges to standard normal as $n \to \infty$

What is the formula for the one-sample t-statistic?
?
- $t = \frac{\bar X - \mu_0}{s / \sqrt{n}} \sim t_{n-1}$
- $\bar X$ is sample mean, $\mu_0$ is hypothesized population mean
- $s$ is sample standard deviation (computed with $n-1$ correction)
- $n$ is sample size, degrees of freedom $= n-1$

What are the assumptions for a valid t-test?
?
- Data must be **i.i.d.** (independent and identically distributed)
- Population should be **approximately normal** (especially for small $n < 30$)
- For two-sample t-test: **equal variances** or use Welch's correction
- Random sampling from the population

How does the t-distribution differ from the normal distribution?
?
- t-distribution has **heavier tails** (more probability in extremes)
- Shape depends on **degrees of freedom** (flatter for small df)
- Accounts for uncertainty from estimating $\sigma$ with $s$
- Converges to normal as $df \to \infty$ (practically same for $n > 30$)

When should you use t-test vs z-test?
?
- **z-test**: Use when $\sigma$ is known (rare in practice)
- **t-test**: Use when $\sigma$ is unknown and estimated from sample (most common)
- For $n \geq 30$, t and z tests give very similar results due to convergence
- For small $n$ with unknown $\sigma$, must use t-test

