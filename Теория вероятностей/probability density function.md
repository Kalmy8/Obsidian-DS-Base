---
Tags: ""
---

For continuous random variables, which can take on an infinite number of values within a range (like the height of people), the probability of any single value is actually zero. Instead, we look at the probability of the variable falling within an interval. This is captured by the **probability density function (PDF)**, and probabilities are calculated by integrating the PDF over the desired interval.

>[!Example]
>For many real-world tasks, the **[standard distributions](standard%20distributions.md)**, for example a **[Gaussian distribution](Gaussian%20distribution.md)** are usually taken for PDF: 
>$$f(h) = \frac{1}{\sqrt{2 \pi \sigma^2}} \, e^{-\frac{(h - \mu)^2}{2 \sigma^2}}$$
We can now find $P(160<Y<170)$ by integrating the PDF of $Y$ from 160 to 170: 
$$P(160<Y<170) = \int\limits_{160}^{170} f(h)dh$$