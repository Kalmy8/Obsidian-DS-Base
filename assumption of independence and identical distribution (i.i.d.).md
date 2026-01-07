---
type: note
status: done
tags: ['math/probability-theory']
sources:
-
authors:
-
---
#🃏/semantic/math/probability-theory

states, that datapoints you are working with were brought from the **same** (static, not dynamically changing) general population **independently** (meaning that they are fetched truly randomly)

As the result of such a process, we do get **subsamples of the same distribution**, as the original one, this is often denoted like
 $$X^i \stackrel{D}{=} X$$

this assumption is a key-requirement for most part of ML algorithms, and statistical tests.

If the assumption is true, then all the [[descriptional statistics]] will be the same for the distributed and for an original random variable.

**Caution**
While the equality holds mathematically under i.i.d., **empirically**, individual subsets may slightly deviate from the population distribution due to random sampling variability (as mentioned earlier).

Hopefully, according to the [[Law of Large Numbers (LLN)]], **as your sample size increases, empirical deviations from the true population distribution become statistically negligible**

#### Key questions:

what does the assumption of independence and identical distribution (i.i.d.) state? If the assumption is true, what would be the effect?
?
- Datapoints you are working with were brought from the **same** (static, not dynamically changing) general population **independently** (meaning that they are fetched truly randomly)
- If the assumption is true, then all the [[descriptional statistics]] will be the same for the distributed and for an original random variable (according to the [[Law of Large Numbers (LLN)]])
<!--SR:!2026-01-09,4,280-->

