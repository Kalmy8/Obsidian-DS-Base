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

**Related:** [[Law of Large Numbers (LLN)]], [[variance]], [[mathematical expectation]], [[descriptional statistics]], [[t-distribution and Student's t-test]]

## Assumptions

For the Central Limit Theorem to hold:
1. **i.i.d. assumption**: Random variables $X_1, X_2, \ldots, X_n$ must be independent and identically distributed [[assumption of independence and identical distribution (i.i.d.)]]
2. **Finite variance**: $\mathbb{E}[X] = \mu$ and $\mathrm{Var}(X) = \sigma^2 < \infty$
3. **Large enough $n$**: The approximation improves as $n$ grows
	- ⚠️ **"$n \geq 30$" is a rule of thumb, not a law**:
	- For symmetric distributions: $n = 10$ might suffice
	- For heavily skewed or heavy-tailed distributions: $n = 100+$ may be needed

## Statement

If $X_1,\ldots,X_n$ are i.i.d. with $\mathbb{E}[X]=\mu$ and $\mathrm{Var}(X)=\sigma^2 < \infty$, then for sufficiently large $n$:

$$
\bar X \approx \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)
$$

where:
- $\bar X = \frac{1}{n}\sum_{i=1}^n X_i$ is the sample mean
- $\mu$ is the population mean
- $\sigma^2$ is the population variance
- $n$ is the sample size
- $\frac{\sigma^2}{n}$ is the variance of the sampling distribution

**Standard Error (SE):**

$$
SE(\bar X) = \frac{\sigma}{\sqrt{n}}
$$

This is the standard deviation of the sampling distribution of $\bar X$.

### Important Nuances
1. CLT is about the **sampling distribution of $\bar X$** (distribution of means across repeated samples), **not** about the raw $X$
2. The population $X$ can have **any distribution** (as long as variance is finite)
3. The spread of $\bar X$ shrinks with $n$ as $\sigma/\sqrt{n}$

## Demonstration

>[!info]- Code snippet: CLT with skewed population
>```python
>import matplotlib.pyplot as plt
>import numpy as np
>import seaborn as sns
>
>rng = np.random.default_rng(42)
>
># Non-normal population (exponential is heavily right-skewed)
>mu_pop = 10.0
>sigma_pop = 10.0  # for exponential, std = scale
>X_pop = rng.exponential(scale=mu_pop, size=200_000)
>
># 1) Show original population distribution
>fig, ax = plt.subplots(figsize=(10, 5))
>sns.histplot(x=X_pop[:25_000], bins=60, stat="density", alpha=0.35, ax=ax)
>sns.kdeplot(x=X_pop[:25_000], ax=ax)
>ax.axvline(mu_pop, color="red", linestyle="--", linewidth=2, label=f"μ = {mu_pop:.1f}")
>ax.set_title("Original Population: Exponential (heavily skewed, NOT normal)")
>ax.set_xlabel("x")
>ax.legend()
>plt.show()
>
># 2) Function to generate m samples of size n and compute their means
>def sample_means(pop: np.ndarray, n: int, m: int = 5_000) -> np.ndarray:
>    idx = rng.integers(0, len(pop), size=(m, n))
>    return pop[idx].mean(axis=1)
>
>n_values = [5, 30, 200]
>m = 8_000
>
># 3) Show sampling distributions for different n
>fig, axes = plt.subplots(1, 3, figsize=(18, 5))
>
>for ax, n in zip(axes, n_values, strict=True):
>    means = sample_means(X_pop, n=n, m=m)
>    theoretical_se = sigma_pop / np.sqrt(n)
>    
>    sns.histplot(x=means, bins=60, stat="density", alpha=0.35, ax=ax)
>    sns.kdeplot(x=means, ax=ax)
>    ax.axvline(mu_pop, color="black", linestyle="--", linewidth=2, label=f"μ = {mu_pop:.1f}")
>    ax.set_title(f"Sample means (n={n})")
>    ax.set_xlabel("Mean")
>    
>    # Stats box
>    stats_txt = (
>        f"mean(means) = {np.mean(means):.2f}\n"
>        f"std(means) = {np.std(means, ddof=1):.2f}\n"
>        f"SE theory = {theoretical_se:.2f}"
>    )
>    ax.text(
>        0.98, 0.98, stats_txt,
>        transform=ax.transAxes, va="top", ha="right",
>        fontsize=9, bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.8}
>    )
>    ax.legend()
>
>plt.suptitle("CLT: Distribution of sample means approaches normal as n grows (even though population was NOT normal)")
>plt.tight_layout()
>plt.show()
>```


## What About Other Statistics?

CLT focuses on the **sample mean**, but other statistics have their own sampling distributions:

| Statistic | Sampling Distribution | Notes |
|-----------|----------------------|-------|
| Sample Variance $S^2$ | [[chi-square distribution for sample variance\|Chi-square]] (if population is normal) | $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$ |
| Sample Std $S$ | Chi distribution | Skewed, not normal (even for large $n$) |
| Sample Mean (unknown $\sigma$) | [[t-distribution and Student's t-test\|t-distribution]] | Use when $\sigma$ is estimated from data |
| Functions of means | [[delta method\|Delta method]] | Approximate normality via Taylor expansion |

## Review questions

What does the Central Limit Theorem state?
?
- For i.i.d. random variables with finite mean $\mu$ and variance $\sigma^2$, the sample mean $\bar X$ is approximately normal: $\bar X \approx \mathcal{N}(\mu, \sigma^2/n)$
- This holds for **large enough $n$**, regardless of the population distribution
- CLT describes the **sampling distribution of $\bar X$**, not the raw data $X$

What are the key assumptions for CLT?
?
- Random variables must be **i.i.d.** (independent and identically distributed)
- Population must have **finite variance**: $\sigma^2 < \infty$
- Sample size $n$ should be **sufficiently large** (rule of thumb: $n \geq 30$ for most distributions)
- For skewed/heavy-tailed distributions, larger $n$ may be needed

How does the standard error (SE) of the sample mean change with $n$?
?
- $SE(\bar X) = \sigma/\sqrt{n}$ decreases as $n$ increases
- This means confidence intervals get narrower for larger samples
- To halve SE, you need to quadruple $n$ (due to square root relationship)

What is the difference between CLT and LLN?
?
- **LLN**: Sample mean converges to $\mu$ (point convergence: $\bar X \to \mu$)
- **CLT**: Distribution of $\bar X$ converges to normal (distributional convergence: $\bar X \sim \mathcal{N}(\mu, \sigma^2/n)$)
- CLT tells us **how** $\bar X$ is distributed, LLN tells us **where** it converges

When should you use t-distribution instead of normal for CLT?
?
- Use t-distribution when population standard deviation $\sigma$ is **unknown** and estimated from sample ($s$)
- The test statistic becomes $t = \frac{\bar X - \mu}{s/\sqrt{n}} \sim t_{n-1}$
- For large $n$ ($n > 30$), t-distribution converges to normal, so the difference becomes negligible
- See [[t-distribution and Student's t-test]] for details
