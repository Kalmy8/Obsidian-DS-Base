#🃏/probability-theory 
is **a function** on a [fundamental probability set](elementary%20event,%20fundamental%20probability%20set%20and%20an%20event.md), which maps every outcome of the probability set to a real (or complex) value. ^216b8e

Example: let $\Omega = \{(i,j): i,j = 1,2,3.. \}$. Then the random variable $X$ can be defined as:
$$X(i,j)= 3i + 6j, or$$ $$X(i,j)= i*j, or$$ $$X(i,j)= \sqrt{i}, etc$$ 
>[!Note] 
>Random variables are usually denoted with capital latin letters like $X, Y, Z$
>A **single outcome** of such a function is usually denoted with the lowercase letter, so 
>$$x = X(i,j),\ for (i,j) \in \Omega$$

Random variable can take arbitrary values with certain [probabilities](../probability.md). We can express the bond between a random variable and it's likelihood to take some value with help of the **3 common functions:**
- [probability mass function](probability%20mass%20function.md) for a [discrete variable](../discrete%20variable.md)
- [probability density function](probability%20density%20function.md) for a [continuous variable](../continuous%20variable.md)
- [cumulative distribution function](cumulative%20distribution%20function.md) for both variables

Finally, a random variable has all kinds of **descriptional statistics**: ^0882fd
- [mathematical expectation](mathematical%20expectation.md)
- [variance](variance.md)
- [[skewness]]
- [[kurtosis]]

#### Key questions
What is a random variable? Define several of them given the set $\Omega = \{(i,j): i,j = 1,2,3.. \}$
?
A random variable is **a function** which maps elementary events from the fundamental probability set to real values. Given this set, we can define many random variables like:
$$X(i,j)= 3i + 6j, or$$ $$X(i,j)= i*j, or$$ $$X(i,j)= \sqrt{i}, etc$$
 

How is a random variable bonded with probability? How can you express the likelihood that some random variable will take a certain  value?
?
Probability is a property of an elementary event. Random variables maps elementary events to certain values, so, for every value the random variable can take, the likelihood will be the sum of corresponding elementary events probabilities. This fact is usually expressed with the usage of [probability density function](probability%20density%20function.md)/[probability mass function](probability%20mass%20function.md)/[cumulative distribution function](cumulative%20distribution%20function.md).


What are the descriptional statistics of a random variable, why would you need one? Name as much as you can remember
?
Descriptional statistics describe the set of values which a random variable can take, so they allow you to make useful assumptions about the variable even not looking on the distribution. Popular statistics are:
- [mathematical expectation](mathematical%20expectation.md)
- [variance](variance.md)

