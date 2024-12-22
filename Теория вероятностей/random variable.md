#🃏/probability-theory 
is **a function** on a [[elementary event, fundamental probability set and an event | fundamental probability set]], which maps every outcome of the probability set to a real (or complex) value. ^216b8e

Example: let $\Omega = \{(i,j): i,j = 1,2,3.. \}$. Then the random variable $X$ can be defined as:
$$X(i,j)= 3i + 6j, or$$ $$X(i,j)= i*j, or$$ $$X(i,j)= \sqrt{i}, etc$$ 
>[!Note] 
>Random variables are usually denoted with capital latin letters like $X, Y, Z$
>A **single outcome** of such a function is usually denoted with the lowercase letter, so 
>$$x = X(i,j),\ for (i,j) \in \Omega$$

Random variable can take arbitrary values with certain [[probability | probabilities]]. We can express the bond between a random variable and it's likelihood to take some value with help of the **3 common functions:**
- [[probability mass function]] for a [[discrete variable]]
- [[probability density function]] for a [[continuous variable]]
- [[cumulative distribution function]] for both variables

Finally, a random variable has all kinds of **descriptional statistics**: ^0882fd
- [[mathematical expectation]]
- [[variance]]

#### Key questions
What is a random variable? Define several of them given the set $\Omega = \{(i,j): i,j = 1,2,3.. \}$
?
A random variable is **a function** which maps elementary events from the fundamental probability set to real values. Given this set, we can define many random variables like:
$$X(i,j)= 3i + 6j, or$$ $$X(i,j)= i*j, or$$ $$X(i,j)= \sqrt{i}, etc$$
<!--SR:!2025-01-29,56,310--> 

How is a random variable bonded with probability? How can you express the likelihood that some random variable will take a certain  value?
?
Probability is a property of an elementary event. Random variables maps elementary events to certain values, so, for every value the random variable can take, the likelihood will be the sum of corresponding elementary events probabilities. This fact is usually expressed with the usage of [[probability density function]]/[[probability mass function]]/[[cumulative distribution function]].
<!--SR:!2025-01-09,38,290-->

What are the descriptional statistics of a random variable, why would you need one? Name as much as you can remember
?
Descriptional statistics describe the set of values which a random variable can take, so they allow you to make useful assumptions about the variable even not looking on the distribution. Popular statistics are:
- [[mathematical expectation]]
- [[variance]]
<!--SR:!2025-02-02,60,310-->
