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

**Related:** [[variance]], [[standard distributions]], [[probability density function]], [[Central Limit Theorem (CLT)]]

## Definition

⚠️ **Important Assumptions**

This result requires the population to be **normally distributed**!
- If the population is **not normal**, the relationship below does **not** hold
- For non-normal populations, the distribution of $S^2$ can be quite different
- CLT does **not** apply to sample variance the same way it applies to sample means

---

When drawing a random sample of size $n$ from a **normal population** with variance $\sigma^2$, the sample variance $S^2$ (computed with Bessel's correction) has a specific relationship to the **chi-square distribution**:

$$
\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}
$$

where:
- $S^2$ is the sample variance: $S^2 = \frac{1}{n-1}\sum_{i=1}^n(X_i - \bar X)^2$
- $\sigma^2$ is the true population variance
- $n$ is the sample size
- $\chi^2_{n-1}$ is the chi-square distribution with $n-1$ degrees of freedom

## Key Properties

### Expected Value
$$
\mathbb{E}[S^2] = \sigma^2
$$
The sample variance is an **unbiased estimator** of the population variance (when using $n-1$ correction).

### Variance of Sample Variance
$$
\text{Var}(S^2) = \frac{2\sigma^4}{n-1}
$$

As $n$ increases, the variance of $S^2$ decreases, making it a more precise estimator.

## Sample Standard Deviation

The sample standard deviation $S = \sqrt{S^2}$ follows a **chi distribution** (not chi-square!) with $n-1$ degrees of freedom:

$$
S = \frac{\sigma}{\sqrt{n-1}} \cdot \chi_{n-1}
$$

**Important:** Unlike the sample mean (which becomes normal via CLT), the sample standard deviation:
- Has a **skewed distribution** (especially for small $n$)
- Only approaches normality for very large $n$
- Has approximate standard error: $SE(S) \approx \frac{\sigma}{\sqrt{2n}}$

## Applications

1. **Confidence Intervals for Variance**: Use the chi-square distribution to construct confidence intervals for $\sigma^2$
2. **Hypothesis Testing**: Test claims about population variance (e.g., variance homogeneity tests)
3. **Quality Control**: Monitor process variability in manufacturing

## Example

If we sample $n=20$ observations from $\mathcal{N}(\mu, \sigma^2)$ and compute $S^2$:

$$
\frac{19 S^2}{\sigma^2} \sim \chi^2_{19}
$$

We can use this to find a 95% confidence interval for $\sigma^2$:

$$
\left[\frac{19 S^2}{\chi^2_{0.975, 19}}, \frac{19 S^2}{\chi^2_{0.025, 19}}\right]
$$

## Review questions

What is the relationship between sample variance and chi-square distribution for normal populations?
?
- When sampling from a normal population with variance $\sigma^2$, the scaled sample variance follows chi-square distribution: $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$
- This requires the population to be normally distributed
- The sample variance $S^2$ is an unbiased estimator: $\mathbb{E}[S^2] = \sigma^2$

How does the distribution of sample standard deviation differ from sample variance?
?
- Sample variance $S^2$ follows a scaled chi-square distribution
- Sample standard deviation $S$ follows a **chi distribution** (not chi-square!)
- Unlike the sample mean, $S$ has a **skewed distribution**, especially for small $n$
- Only approaches normality for very large sample sizes
- Approximate standard error: $SE(S) \approx \frac{\sigma}{\sqrt{2n}}$

What are the key assumptions required for the chi-square relationship of sample variance?
?
- The population must be **normally distributed** (critical assumption!)
- If the population is not normal, the relationship $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$ does not hold
- The Central Limit Theorem does **not** apply to sample variance the same way it applies to sample means
- Sample size $n$ determines the degrees of freedom: $n-1$

