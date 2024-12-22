states, that datapoints you are working with were brought from the **same** (static, not dynamically changing) general population **independently** (meaning that they are fetched truly randomly)

As the result of such a process, we do get **subsamples of the same distribution**, as the original one, this is often denoted like
$$X^{i}=^{D}X$$

this assumption is a key-requirement for most part of ML algorithms, and statistical tests.

If the assumption is true, then all the [[random variable#^0882fd | descriptional statistics]] will be the same for the distributed and for an original random variable.

**Caution**
While the equality holds mathematically under i.i.d., **empirically**, individual subsets may slightly deviate from the population distribution due to random sampling variability (as mentioned earlier).

Hopefully, according to the [[Law of Big Numbers]], sample 





#🃏/probability-theory #🌱
#### Key questions:
what does the assumption of independence and identical distribution (i.i.d.) state?
?
Datapoints you are working with were brought from the **same** (static, not dynamically changing) general population **independently** (meaning that they are fetched truly randomly)
<!--SR:!2025-01-24,50,310-->