---
type: note
status: done
tags: [math/statistics, math/probability-theory]
sources:
-
authors:
-
---

#🃏/semantic/math/statistics #🃏/semantic/math/probability-theory

Descriptive statistics are numeric summaries of a [random variable](random%20variable.md) (and its distribution).

Common examples:
- [mathematical expectation](mathematical%20expectation.md)
- [variance](variance.md)
- [skewness](skewness.md)
- [kurtosis](kurtosis.md)

## Moments (integral/sum formulas)

### Raw (initial) n-th moment

$$m_n = E[X^n]$$

- Discrete case (PMF):
$$m_n=\sum\limits_{i=1}^{N}x_i^n p_i$$

- Continuous case (PDF):
$$m_n=\int\limits_{-\infty}^{\infty}x^n f(x)\,dx$$

### Central n-th moment

$$\mu_n = E[(X-\mu)^n],\quad \mu=E[X]$$

- Discrete case (PMF):
$$\mu_n=\sum\limits_{i=1}^{N}(x_i-\mu)^n p_i$$

- Continuous case (PDF):
$$\mu_n=\int\limits_{-\infty}^{\infty}(x-\mu)^n f(x)\,dx$$

#### Key questions

Write the formula for calculating the **n-th moment** for both discrete and continuous random variables (raw and central versions).
?
- Raw (initial) n-th moment: $m_n=E[X^n]$
  - Discrete: $$m_n=\sum\limits_{i=1}^{N}x_i^n p_i$$
  - Continuous: $$m_n=\int\limits_{-\infty}^{\infty}x^n f(x)\,dx$$
- Central n-th moment: $\mu_n=E[(X-\mu)^n]$, where $\mu=E[X]$
  - Discrete: $$\mu_n=\sum\limits_{i=1}^{N}(x_i-\mu)^n p_i$$
  - Continuous: $$\mu_n=\int\limits_{-\infty}^{\infty}(x-\mu)^n f(x)\,dx$$
<!--SR:!2027-01-07,365,350-->
