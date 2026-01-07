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

**Related:** [[Central Limit Theorem (CLT)]], [[variance]], [[mathematical expectation]], [[Law of Large Numbers (LLN)]]

## Definition

The **delta method** is a statistical technique used to approximate the distribution of a **function of an asymptotically normal estimator**. It leverages Taylor expansion to derive the asymptotic variance of transformed statistics.

## The Main Result

If $X_n$ is a sequence of random variables such that:

$$
\sqrt{n}(X_n - \theta) \xrightarrow{D} \mathcal{N}(0, \sigma^2)
$$

(i.e., $X_n$ is asymptotically normal)

And $g(\cdot)$ is a **differentiable function** at $\theta$ with $g'(\theta) \neq 0$, then:

$$
\sqrt{n}(g(X_n) - g(\theta)) \xrightarrow{D} \mathcal{N}(0, \sigma^2 \cdot [g'(\theta)]^2)
$$

where:
- $\theta$ is the true parameter value
- $X_n$ is an estimator (e.g., sample mean)
- $g(\cdot)$ is a smooth transformation function
- $g'(\theta)$ is the derivative of $g$ evaluated at $\theta$
- $\xrightarrow{D}$ denotes convergence in distribution

## Practical Formula

For practical use, the **asymptotic variance** of $g(X_n)$ is:

$$
\text{Var}(g(X_n)) \approx [g'(\theta)]^2 \cdot \text{Var}(X_n)
$$

Or equivalently, the **standard error** of $g(X_n)$ is:

$$
SE(g(X_n)) \approx |g'(\theta)| \cdot SE(X_n)
$$

## Common Examples

### 1. Logarithm Transformation

If $\bar X \xrightarrow{D} \mathcal{N}(\mu, \sigma^2/n)$, then:

$$
\log(\bar X) \xrightarrow{D} \mathcal{N}\left(\log(\mu), \frac{\sigma^2}{n\mu^2}\right)
$$

Since $g(x) = \log(x)$, we have $g'(x) = 1/x$, so $g'(\mu) = 1/\mu$.

### 2. Square Root (e.g., for Standard Deviation)

If $S^2 \xrightarrow{D} \mathcal{N}(\sigma^2, \text{Var}(S^2))$, then:

$$
S = \sqrt{S^2} \xrightarrow{D} \mathcal{N}\left(\sigma, \frac{\text{Var}(S^2)}{4\sigma^2}\right)
$$

Since $g(x) = \sqrt{x}$, we have $g'(x) = \frac{1}{2\sqrt{x}}$, so $g'(\sigma^2) = \frac{1}{2\sigma}$.

### 3. Ratio Estimator

If $\bar X \xrightarrow{D} \mathcal{N}(\mu_X, \sigma^2_X/n)$ and $\bar Y \xrightarrow{D} \mathcal{N}(\mu_Y, \sigma^2_Y/n)$, then:

$$
R = \frac{\bar X}{\bar Y} \xrightarrow{D} \mathcal{N}\left(\frac{\mu_X}{\mu_Y}, \frac{1}{n\mu^2_Y}(\sigma^2_X + R^2\sigma^2_Y - 2R\sigma_{XY})\right)
$$

(using multivariate delta method with covariance)

## Intuition

The delta method uses a **first-order Taylor expansion**:

$$
g(X_n) \approx g(\theta) + g'(\theta)(X_n - \theta)
$$

Since $X_n - \theta$ is approximately normal, and we're applying a linear transformation (first-order), the result is also approximately normal.

## When to Use

✅ **Use delta method when:**
- You have an asymptotically normal estimator (e.g., sample mean)
- You need to transform that estimator (log, sqrt, ratio, etc.)
- You want approximate confidence intervals or hypothesis tests for the transformed parameter

⚠️ **Limitations:**
- Requires **large sample size** ($n$ sufficiently large)
- Function $g$ must be **differentiable** at $\theta$
- $g'(\theta) \neq 0$ (otherwise, need higher-order delta method)
- Approximation quality depends on how "linear" $g$ is near $\theta$

## Multivariate Delta Method

For vector-valued estimators $\mathbf{X}_n$ with covariance matrix $\Sigma$, and $g: \mathbb{R}^k \to \mathbb{R}$:

$$
\text{Var}(g(\mathbf{X}_n)) \approx \nabla g(\theta)^T \Sigma \nabla g(\theta)
$$

where $\nabla g(\theta)$ is the gradient vector of $g$ at $\theta$.

## Review questions

What is the delta method and when is it used?
?
- The delta method is a statistical technique to approximate the distribution of a **function of an asymptotically normal estimator**
- Used when you have an asymptotically normal estimator (e.g., sample mean) and need to transform it (log, sqrt, ratio, etc.)
- Leverages Taylor expansion to derive asymptotic variance of transformed statistics
- Requires large sample size and differentiable transformation function

What is the main formula of the delta method?
?
- If $\sqrt{n}(X_n - \theta) \xrightarrow{D} \mathcal{N}(0, \sigma^2)$ and $g$ is differentiable at $\theta$ with $g'(\theta) \neq 0$, then:
$$\sqrt{n}(g(X_n) - g(\theta)) \xrightarrow{D} \mathcal{N}(0, \sigma^2 \cdot [g'(\theta)]^2)$$
- Practical formula for variance: $\text{Var}(g(X_n)) \approx [g'(\theta)]^2 \cdot \text{Var}(X_n)$
- For standard error: $SE(g(X_n)) \approx |g'(\theta)| \cdot SE(X_n)$

What are common applications of the delta method?
?
- **Logarithm transformation**: $\log(\bar X)$ has variance $\sigma^2/(n\mu^2)$ since $g'(x) = 1/x$
- **Square root**: For sample variance $S^2$, the std $S = \sqrt{S^2}$ uses $g'(x) = 1/(2\sqrt{x})$
- **Ratio estimator**: Finding distribution of $\bar X / \bar Y$ (requires multivariate version)
- Any smooth transformation of an asymptotically normal estimator

What are the key limitations of the delta method?
?
- Requires **large sample size** ($n$ sufficiently large) for good approximation
- Function $g$ must be **differentiable** at $\theta$
- Requires $g'(\theta) \neq 0$ (otherwise need higher-order delta method)
- Approximation quality depends on how "linear" $g$ is near $\theta$
- Uses first-order Taylor expansion, so ignores higher-order terms

