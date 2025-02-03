one of the [statistical sampling techniques](statistical%20sampling%20techniques.md), which can be formally described as follows:

Let's say we have some dataset $D$ size of $N$ observations. For $M$ times, we will pick $N$ observations from the $D$ dataset, with return. This way we will get $M$ subsamples of the original data, which can be denoted like $X_{1},X_{2},..,X_{M}$.

Notice that each original dataset observation has an equal chance of $\frac{1}{N}$ to be picked at a time, thus $1-\frac{1}{N}$ chance not to be picked. To form one complete subsample $X_{i}$, we do repeat the procedure $N$ times, so the resulting chance for the observation **not to be picked at all** is $(1-\frac{1}{N})^{N}$.
Notice that we can utilize on well-known limit here:
$$\lim_{N\to\inf}(1-\frac{1}{N})^{N}=\frac{1}{e} \approx 36\%$$
In reality, $N$ does not need to be so big at all:

| Dataset Size ($n$)   | $\left(1 - \frac{1}{n}\right)^n$ | Difference from $e^{-1}$ ($\approx 0.368$) |
|-----------------------|----------------------------------|-------------------------------------------|
| $10$                 | $0.3487$                        | $0.0192$                                  |
| $30$                 | $0.3677$                        | $0.0002$                                  |
| $50$                 | $0.3679$                        | $\approx 0.0000$                          |
| $100$                | $0.3679$                        | $\approx 0.0000$                          |
| $1,000$              | $0.3679$                        | $\approx 0.0000$                          |
As you can see, even for $N\geq 10$ the calculated chance is practically the same.

#🃏/data-science 
## Key questions

How can the bootstrap sampling technique be described? What is the chance for every observation to be picked into a subsample?
?
- From the dataset size $N$, we pick $N$ samples with return.
- Every observation chance to be included $\approx 64\%$
<!--SR:!2025-02-14,55,310-->