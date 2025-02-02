#🃏/probability-theory 
is an average weighted outcome of a given random variable.

##### Definition
For [discrete variable](../discrete%20variable.md) it is defined as 
$$E(X)=\sum\limits_{w_k \in \Omega} X(w_{k})P(X = X(w_{k})),\ or$$
$$E(X)=\sum\limits_{i = 1}^N x_{i} p_{i},$$
where $x_{i}$ is an [elementary event](elementary%20event,%20fundamental%20probability%20set%20and%20an%20event.md#^f482b1) (same as $X(w_{k})$);
$p_{i}$ is the [probability](../probability.md) of this event (same as $P(X = x)$).

For [continuous variable](../continuous%20variable.md) is is defined as 
$$E(X)=\int\limits_{-\infty}^{\infty} x f(x) dx, $$
where $x$ is an random variable function outcome, $f(x)$ is simply the probability of the outcome $x$  ([probability density function](probability%20density%20function.md) applied to outcome $x$).

>[!Note]
>Mathematical expectation is often denoted as $\mu$

#####  Properties:
**1. Linearity:**

* $E[aX + b] = aE[X] + b$, where *a* and *b* are constants.  This means the expected value of a linear transformation of a random variable is the same linear transformation of the expected value.
>[!proof]-
> **For discrete case:**
> $E[aX + b] =$    *Applying the definition*
> $= \sum(ax_i + b)p_{i} =$  *Splitting sums*
> $= \sum ax_{i}p_{i}+ \sum bp_{i}=$    *Factor out constants*
> $= a \sum x_{i}p_{i} + b \sum p_{i}=$ *$\sum p_{i} = 1$ by definiton of probability*
> $= a E(X) + b$  
> **For continuous case by analogue, using $\int$**
* $E[X + Y] = E[X] + E[Y]$, even if *X* and *Y* are not independent. This extends to any finite sum of random variables.


**2. Constant Value:**

* $E[c] = c$, where *c* is a constant.  The expected value of a constant is just the constant itself.

**3. Product of Independent Random Variables:**

* $E[XY] = E[X]E[Y]$, if *X* and *Y* are independent random variables.  This doesn't generally hold if *X* and *Y* are dependent.

**4. Non-negativity:**

* $If\ X ≥ 0,\ then\ E[X] ≥ 0.$ If a random variable is always non-negative, its expected value must also be non-negative.

**5. Monotonicity:**

* $If\ X ≤ Y, then\ E[X] ≤ E[Y].$ If one random variable is always less than or equal to another, its expected value is also less than or equal.

**6. Jensen's Inequality (for Convex Functions):**

* **If *f(x)* is a convex function, then E[f(X)] ≥ f(E[X]).**
* **If *f(x)* is a concave function, then E[f(X)] ≤ f(E[X]).** This inequality relates the expected value of a function of a random variable to the function of the expected value.

**7. Law of the Unconscious Statistician (LOTUS):**

* $E[g(X)] = \sum g(x)P(X=x)$ for discrete random variables.
* $E[g(X)] = \int g(x)f(x)dx$ for continuous random variables with probability density function f(x).  This allows us to calculate the expected value of a function of a random variable without needing to find the distribution of g(X) directly.

**8. Relationship to Mean:**

* The expected value is the population mean. If you were to sample from the distribution infinitely many times, the average of your samples would approach the expected value.

**9. Law of total expectation:**
$$E[X] = E_Y[E[X|Y]]$$

#### Key questions
Give the intuitive definition of a mathematical expectation, provide formal mathematical definitions for both [discrete](../discrete%20variable.md) and [continuous](../continuous%20variable.md) random variable
?
Mathematical expectation is an average weighted outcome of a given random variable. For discrete case, the formula would be:
$$E[X]=\sum\limits_{w_{i}\in \Omega}X(w_{i})P(X = X(w_{i})) = \sum\limits_{i=1}^{N}x_{i}p_{i}$$
For continuous case, the formula would be:
$$E[X]=\int\limits_{w\in \Omega}X(w)dP(w)= \int\limits_{-\inf}^{\inf}xf(x)dx$$


