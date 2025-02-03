measures how far are random variable outcomes are distributed around it's [mathematical expectation](mathematical%20expectation.md).

For any random variable, the variance can be defined as:
$$V(X) = E(X - E(X))^2 = E(X - \mu)^{2}$$

This formula is often simplified:
$$(X - E(X))^{2}= X^{2} - 2 X E(X) + E(X)^2$$
Apply mathematical expectation for both sides:
$$V(X)= E(X^{2}) - E(2 X E(X)) + E(E(X)^2)$$
Simplify: factor out constants, with respect that $E(constant) = constant$:
$$V(X)= E(X^{2}) - 2 E(X) E(X) + E(X)^{2} = E(X^{2})- E(X)^2 $$ 

>[!Note]
>In general, variance is often denoted as $\sigma^2$
>If some sample of the data is described, it is usually denoted as $s^2$

#🃏/probability-theory
## Review questions
What is the intuitive definition of variance? Write down the formal mathematical definition and it's simplified version.
?
- Variance is a descriptive statistic showing how far "in average" are random variable outcomes distributed around it's mathematical expectation
- The original formula is $$\sigma^{2}=E(X-E(X))^{2}=E(X-\mu)^{2}$$
- The simplified version useful for calculus is $$\sigma^{2}=E(X^{2})-E(X)^{2}$$
<!--SR:!2025-05-03,105,310-->