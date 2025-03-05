states, that datapoints you are working with were brought from the **same** (static, not dynamically changing) general population **independently** (meaning that they are fetched truly randomly)

As the result of such a process, we do get **subsamples of the same distribution**, as the original one, this is often denoted like
 $$X^i \stackrel{D}{=} X$$

this assumption is a key-requirement for most part of ML algorithms, and statistical tests.

If the assumption is true, then all the [descriptional statistics](Теория%20вероятностей/random%20variable.md#^0882fd) will be the same for the distributed and for an original random variable.

**Caution**
While the equality holds mathematically under i.i.d., **empirically**, individual subsets may slightly deviate from the population distribution due to random sampling variability (as mentioned earlier).

Hopefully, according to the [Law of Big Numbers](Law%20of%20Big%20Numbers.md),  **as your sample size increases, empirical deviations from the true population distribution become statistically negligible**


#🃏/probability-theory 
#### Key questions:

what does the assumption of independence and identical distribution (i.i.d.) state?
?
Datapoints you are working with were brought from the **same** (static, not dynamically changing) general population **independently** (meaning that they are fetched truly randomly)

if the assumption is true, what would be the effect? How does the assumption rely's on the [Law of Big Numbers](Law%20of%20Big%20Numbers.md) to state that?
?
- If the assumption is true, then all the [descriptional statistics](Теория%20вероятностей/random%20variable.md#^0882fd) will be the same for the distributed and for an original random variable
- [Law of Big Numbers](Law%20of%20Big%20Numbers.md) says that all descriptional statistic of an i.i.d. - sample will converge to general population statistics as you increase the number of observations 