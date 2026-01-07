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

For [continuous random variables](continuous%20variable.md), we cannot assign a probability to a single point (since there are infinitely many points). Instead, we use the **probability density function (PDF)**, denoted as $f(x)$, which describes the "density" of probability at each point.

The PDF has the following key properties:

1. **Non-negativity**: $f(x) \geq 0$ for all $x$
2. **Normalization**: $\int_{-\infty}^{\infty} f(x) dx = 1$ (the total area under the curve equals 1)
3. **Probability via integration**: The probability that a random variable $X$ falls in an interval $[a, b]$ is given by:
   $$P(a \leq X \leq b) = \int_{a}^{b} f(x) dx$$

>[!Important]
>For continuous random variables, $P(X = x) = 0$ for any specific value $x$. Only intervals have non-zero probability.

**Relationship with CDF:**
The [cumulative distribution function](cumulative%20distribution%20function.md) $F(x) = P(X \leq x)$ is related to the PDF by:
$$F(x) = \int_{-\infty}^{x} f(t) dt$$

And conversely, the PDF is the derivative of the CDF:
$$f(x) = \frac{d}{dx} F(x)$$

>[!Example] Height measurement
>If $Y$ is a random variable representing height (in cm) following a normal distribution, the PDF is:
>$$f(h) = \frac{1}{\sqrt{2 \pi \sigma^2}} \, e^{-\frac{(h - \mu)^2}{2 \sigma^2}}$$
>
>We can find the probability that a person's height is between 160cm and 170cm by integrating the PDF:
>$$P(160 \leq Y \leq 170) = \int_{160}^{170} f(h) dh$$

#### Key questions

What is a probability density function (PDF)? How does it differ from a [probability mass function](probability%20mass%20function.md)?
?
- PDF is used for [continuous random variables](continuous%20variable.md) and describes the "density" of probability at each point
- Unlike PMF (which gives probabilities for discrete values), PDF does not give probabilities directly - only the integral of PDF over an interval gives probability
- For continuous variables, $P(X = x) = 0$ for any specific $x$; only intervals have non-zero probability
- PDF must satisfy: $f(x) \geq 0$ and $\int_{-\infty}^{\infty} f(x) dx = 1$
<!--SR:!2027-01-07,365,350-->

How do you calculate the probability that a continuous random variable falls in an interval $[a, b]$ using its PDF?
?
The probability is calculated by integrating the PDF over the interval:
$$P(a \leq X \leq b) = \int_{a}^{b} f(x) dx$$
This represents the area under the PDF curve between $a$ and $b$.
<!--SR:!2027-01-07,365,350-->

What is the relationship between PDF and [cumulative distribution function](cumulative%20distribution%20function.md)?
?
- The CDF $F(x) = P(X \leq x)$ is the integral of the PDF: $F(x) = \int_{-\infty}^{x} f(t) dt$
- The PDF is the derivative of the CDF: $f(x) = \frac{d}{dx} F(x)$
- This means the PDF describes the rate of change of the cumulative probability
<!--SR:!2027-01-07,365,350-->
