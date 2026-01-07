---
type: note
status: done
tags: [math/probability-theory]
sources:
-
authors:
-
---

#🃏/semantic/math/probability-theory

**Definition**: 

Skewness measures the **asymmetry** of a probability distribution.

- **Positive skew**: Right tail longer; mass concentrated on the left (e.g., income distribution).
 
- **Negative skew**: Left tail longer; mass concentrated on the right (e.g., age at retirement).
 

**Formula**:

$$\text{Skewness} = \frac{E[(X-\mu)^3]}{\sigma^3} = \frac{\mu_3}{\sigma^3}$$

_(Standardized third central moment)_

**Formulas via PMF/PDF:**

- Discrete case (PMF):
$$\text{Skewness} = \frac{1}{\sigma^3}\sum\limits_{i=1}^{N}(x_i - \mu)^3 p_i$$

- Continuous case (PDF):
$$\text{Skewness} = \frac{1}{\sigma^3}\int\limits_{-\infty}^{\infty}(x - \mu)^3 f(x)\,dx$$

where $\mu = E[X]$ and $\sigma^2 = V(X)$.

**Interpretation**:

- **Zero**: Symmetric distribution (e.g., normal distribution).
 
- **|Skewness| > 1**: Significant asymmetry.
 

**Practical Uses**:

1. **Risk Assessment**: In finance, stock returns often have negative skew (crash risk).
 
2. **Quality Control**: Detects process shifts (e.g., tool wear causing asymmetric defects).
 
3. **Model Selection**: Guides choice of transformations (e.g., log-transform for right-skewed data).
4. 
### Key Questions (Skewness)

1. **How does positive skew affect the mean vs. median?** 
 ? 
 Mean > median in positive skew (tail pulls mean upward).
 
2. **Why is skewness critical in regression modeling?** 
 ? 
 Skewed residuals violate normality assumption, biasing predictions.
 
3. **Interpret skewness = -0.8 for exam scores.** 
 ? 
 Left-skewed: More high scores, mean < median.
4. 