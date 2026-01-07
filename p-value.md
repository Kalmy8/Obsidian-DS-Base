---
type: note
status: done
tags: [math/statistics, hypothesis-testing]
sources:
- "[[Statistics Basics (1st)]]"
authors:
-
---

#🃏/semantic/math/statistics #🏷️/hypothesis-testing

**Related:** [[Central Limit Theorem (CLT)]], [[t-distribution and Student's t-test]], [[variance]], [[probability]]

## Definition

The **p-value** is the probability of observing a test statistic as extreme as (or more extreme than) the one computed from the sample data, **assuming the null hypothesis $H_0$ is true**.

$$
\text{p-value} = P(\text{observed result or more extreme} \mid H_0 \text{ is true})
$$

**Intuition:** The p-value measures how "surprising" or "unusual" the observed data is under the assumption that $H_0$ is true.

## Interpretation

### Decision Rule

- **Small p-value** (typically $< \alpha$, e.g., 0.05): 
  - Evidence **against** $H_0$ 
  - Reject $H_0$ in favor of $H_1$
  - The observed result is **unlikely** under $H_0$

- **Large p-value** ($\geq \alpha$):
  - **Insufficient evidence** against $H_0$
  - Fail to reject $H_0$ (not the same as "accepting" $H_0$!)
  - The observed result is **plausible** under $H_0$

### Significance Level ($\alpha$)

The **significance level** $\alpha$ is a threshold chosen before the test:
- Common choices: $\alpha = 0.05$, $0.01$, or $0.10$
- Represents the maximum acceptable probability of **Type I error** (rejecting true $H_0$)
- Decision: Reject $H_0$ if p-value $< \alpha$

## Types of Hypothesis Tests

### 1. Right-Tailed Test

**Hypotheses:**
- $H_0: \mu = \mu_0$
- $H_1: \mu > \mu_0$ (parameter is **greater** than hypothesized)

**p-value calculation:**

$$
\text{p-value} = P(Z \geq z) = 1 - \Phi(z)
$$

where $z = \frac{\bar x - \mu_0}{SE}$ is the test statistic.

**When to use:** Testing if a treatment **increases** something (e.g., drug improves performance).

### 2. Left-Tailed Test

**Hypotheses:**
- $H_0: \mu = \mu_0$
- $H_1: \mu < \mu_0$ (parameter is **less** than hypothesized)

**p-value calculation:**

$$
\text{p-value} = P(Z \leq z) = \Phi(z)
$$

**When to use:** Testing if a treatment **decreases** something (e.g., drug lowers blood pressure).

### 3. Two-Tailed Test

**Hypotheses:**
- $H_0: \mu = \mu_0$
- $H_1: \mu \neq \mu_0$ (parameter is **different** from hypothesized, in either direction)

**p-value calculation:**

$$
\text{p-value} = 2 \cdot P(Z \geq |z|) = 2 \cdot (1 - \Phi(|z|))
$$

**When to use:** Testing if a parameter **differs** in any direction (e.g., quality control: is the mean off-target?).

## Example

Suppose you test if a coin is fair ($H_0: p = 0.5$) by flipping it 100 times:
- Observed: 60 heads
- Test statistic: $z = \frac{0.60 - 0.50}{\sqrt{0.5 \cdot 0.5 / 100}} = 2.0$
- p-value (two-tailed): $2 \cdot P(Z \geq 2.0) = 2 \cdot 0.0228 = 0.0456$

**Interpretation:** At $\alpha = 0.05$, reject $H_0$ (p = 0.0456 < 0.05). The coin is likely biased.

## Common Misconceptions

### ❌ What p-value is NOT:

1. **NOT** the probability that $H_0$ is true
   - p-value = $P(\text{data} \mid H_0)$, not $P(H_0 \mid \text{data})$

2. **NOT** the probability of making a wrong decision
   - That's the Type I error rate $\alpha$, set beforehand

3. **NOT** the probability that the result is due to chance alone
   - All results have some randomness; p-value measures compatibility with $H_0$

4. **NOT** the size or importance of the effect
   - Small p-value doesn't mean large practical significance
   - With huge sample size, tiny effects can have small p-values

### ✅ What p-value IS:

- A measure of **compatibility** between data and $H_0$
- A **conditional probability**: assumes $H_0$ is true
- A **continuous measure** of evidence, not a binary yes/no

## Relationship to Confidence Intervals

For a two-tailed test at significance level $\alpha$:
- If the $(1-\alpha) \times 100\%$ confidence interval for $\mu$ **excludes** $\mu_0$, then p-value $< \alpha$
- If the CI **includes** $\mu_0$, then p-value $\geq \alpha$

This provides a visual way to assess hypothesis tests.

## Demonstration

>[!info]- Code snippet: Visualize p-value
>```python
>import matplotlib.pyplot as plt
>import numpy as np
>from scipy import stats
>
># Example: right-tailed test
>z_obs = 2.5  # observed test statistic
>
>z_range = np.linspace(-4, 4, 500)
>pdf = stats.norm.pdf(z_range, loc=0, scale=1)
>
>plt.figure(figsize=(10, 6))
>plt.plot(z_range, pdf, 'b-', linewidth=2, label='Standard Normal N(0,1)')
>plt.axvline(0, color='black', linestyle='--', linewidth=1, label='H0: z=0')
>plt.axvline(z_obs, color='red', linestyle='-', linewidth=2, label=f'Observed z={z_obs}')
>
># Shade p-value region
>z_tail = z_range[z_range >= z_obs]
>pdf_tail = stats.norm.pdf(z_tail, loc=0, scale=1)
>plt.fill_between(z_tail, pdf_tail, alpha=0.3, color='red', label=f'p-value={1-stats.norm.cdf(z_obs):.4f}')
>
>plt.title('Right-tailed test: p-value is the area in the tail')
>plt.xlabel('z-score')
>plt.ylabel('Density')
>plt.legend()
>plt.grid(True, alpha=0.3)
>plt.show()
>```

## Review questions

What is a p-value and what does it measure?
?
- The p-value is the probability of observing a result as extreme as (or more extreme than) what we got, **assuming $H_0$ is true**
- It measures how "surprising" or "incompatible" the observed data is with the null hypothesis
- Formula: $\text{p-value} = P(\text{observed or more extreme} \mid H_0)$

How do you interpret a small vs. large p-value?
?
- **Small p-value** (< $\alpha$, e.g., 0.05): Evidence against $H_0$ → reject $H_0$. The data is unlikely under $H_0$
- **Large p-value** (≥ $\alpha$): Insufficient evidence → fail to reject $H_0$. The data is plausible under $H_0$
- Note: "Fail to reject" is NOT the same as "accept" $H_0$

What is the difference between right-tailed, left-tailed, and two-tailed p-values?
?
- **Right-tailed** ($H_1: \mu > \mu_0$): $\text{p-value} = P(Z \geq z)$, test if parameter is **greater**
- **Left-tailed** ($H_1: \mu < \mu_0$): $\text{p-value} = P(Z \leq z)$, test if parameter is **smaller**
- **Two-tailed** ($H_1: \mu \neq \mu_0$): $\text{p-value} = 2 \cdot P(Z \geq |z|)$, test if parameter is **different** (either direction)

What is a common misconception about p-values?
?
- **Misconception**: p-value is the probability that $H_0$ is true
- **Reality**: p-value = $P(\text{data} \mid H_0)$, not $P(H_0 \mid \text{data})$
- p-value is a conditional probability assuming $H_0$ is true, not a probability about $H_0$ itself
- Small p-value doesn't mean large effect size; with huge samples, tiny effects can have small p-values

What is the relationship between p-value and confidence intervals?
?
- For a two-tailed test at level $\alpha$: If the $(1-\alpha) \times 100\%$ CI for $\mu$ **excludes** $\mu_0$, then p-value < $\alpha$
- If the CI **includes** $\mu_0$, then p-value ≥ $\alpha$
- CIs provide a visual way to assess hypothesis tests and show effect size
