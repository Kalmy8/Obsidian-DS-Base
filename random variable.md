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

A random variable is **a function** which maps elementary events from the fundamental probability set to real values.

$$X(i,j)= 3i + 6j, or$$ $$X(i,j)= i*j, or$$ $$X(i,j)= \sqrt{i}, etc$$ 
>[!Note] 
>Random variables are usually denoted with capital latin letters like $X, Y, Z$
>A **single outcome** of such a function is usually denoted with the lowercase letter, so 
>$$x = X(i,j),\ for (i,j) \in \Omega$$

Random variable can take arbitrary values with certain [probabilities](../probability.md). We can express the bond between a random variable and it's likelihood to take some value with help of the **3 common functions:**
- [probability mass function](probability%20mass%20function.md) for a [discrete variable](../discrete%20variable.md)
- [probability density function](probability%20density%20function.md) for a [continuous variable](../continuous%20variable.md)
- [cumulative distribution function](cumulative%20distribution%20function.md) for both variables

>[!Example] Height measurement example
>**Experiment**: Measuring a random person's height
>
>**Fundamental probability set** $\Omega$: The set of all possible height values (e.g., all real numbers in range [50cm, 250cm]). Each specific height value (like $\omega = 175$cm) is an elementary event.
>
>**Random variable** $X$: Even though outcomes are already numbers, we still define a function. The simplest is the **identity function**:
>- $X(\omega) = \omega$ (maps height in cm to itself)
>
>But we can define **many different random variables** on the same experiment:
>- $X_1(\omega) = \omega$ (height in cm)
>- $X_2(\omega) = \omega/100$ (height in meters)
>- $X_3(\omega) = 1$ if $\omega > 180$ else $0$ (tall/not tall indicator)
>- $X_4(\omega) = (\omega - 170)^2$ (squared deviation from 170cm)
>
>So even when outcomes are numbers, the random variable is still a **function** - often the identity function, but not necessarily.

Finally, a random variable has all kinds of **[[descriptional statistics]]**: ^0882fd
- [mathematical expectation](mathematical%20expectation.md)
- [variance](variance.md)
- [[skewness]]
- [[kurtosis]]

#### Key questions
What is a random variable? Define several of them given the set $\Omega = \{(i,j): i,j = 1,2,3.. \}$
?
A random variable is **a function** which maps elementary events from the fundamental probability set to real values. Given this set, we can define many random variables like:
$$X(i,j)= 3i + 6j, or$$ $$X(i,j)= i*j, or$$ $$X(i,j)= \sqrt{i}, etc$$
<!--SR:!2027-01-07,365,350-->

How is a random variable bonded with probability? How can you express the likelihood that some random variable will take a certain value?
?
Probability is a property of an elementary event. Random variables maps elementary events to certain values, so, for every value the random variable can take, the likelihood will be the sum of corresponding elementary events probabilities. This fact is usually expressed with the usage of [probability density function](probability%20density%20function.md)/[probability mass function](probability%20mass%20function.md)/[cumulative distribution function](cumulative%20distribution%20function.md).
<!--SR:!2026-07-20,365,330-->

What are the descriptional statistics of a random variable, why would you need one? Name as much as you can remember
?
Descriptional statistics describe the set of values which a random variable can take, so they allow you to make useful assumptions about the variable even not looking on the distribution. Popular statistics are:
- [mathematical expectation](mathematical%20expectation.md)
- [variance](variance.md)
<!--SR:!2026-05-16,129,310-->

When the outcome of an experiment is already a number (like height in cm), what is the random variable? Can you define multiple random variables for the same experiment?
?
Even when outcomes are numbers, a random variable is still a **function**. The simplest is the identity function $X(\omega) = \omega$ (maps the height value to itself). However, you can define many different random variables on the same experiment: $X_1(\omega) = \omega$ (height in cm), $X_2(\omega) = \omega/100$ (height in meters), $X_3(\omega) = 1$ if $\omega > 180$ else $0$ (tall/not tall indicator), etc. The random variable is a **choice** of how to represent the outcome numerically.
<!--SR:!2027-01-07,365,350-->
