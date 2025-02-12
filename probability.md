#🃏/probability-theory 
is the real value showing how likely you are to get some outcome of an experiment, the outcome could be an **elementary event** or just an **event**.

let's define a [fundamental probability set](Теория%20вероятностей/elementary%20event,%20fundamental%20probability%20set%20and%20an%20event.md) as $\Omega = \{w_{1}, w_{2}, .., w_{n}\}$.

For each **elementary event** inside the set, let's assign a value $P_i$ in such way that $\sum\limits_{i=1}^{n}P_{i}= 1$, where $P_{i} \geq 0$.

Now each **elementary** event has some probability assigned to it, and it makes sense that [events](Теория%20вероятностей/elementary%20event,%20fundamental%20probability%20set%20and%20an%20event.md#^f9d291) will also have some probability. For an event $A$, it can defined as:
$P(A)=\sum\limits_{k: w_{k}\in A}P_k$

---
Probabilities do have properties, which are obvious from the definition:
1) $P(\emptyset) = 0$
2) $P(\Omega) = 1$
3) $0\leq P(A) \leq1$
4)  $P(A\cup B) = P(A) + P(B) - P(A \cap B)$
>[!proof]-
>Let $P(A \cap B)$ be not zero.
>Then the whole fundamental probability space $A\cup B$ can be divided into sets
>- $A \setminus B = {w_{i},i\in A, i\not\in B }$   
>- $B \setminus A = {w_{i},i\in B, i\not\in A }$
>- $A \cap B = {w_{i},i\in B, i\in A }$
>  $$\underbrace{\sum\limits_{w_{i} \in A \cup B} P(w_{i})}_{P(A\cup B)}=\sum\limits_{w_{i} \in A \setminus B} P(w_{i}) + \sum\limits_{w_{i} \in B \setminus A} P(w_{i})$$
>  $$=\underbrace{\sum\limits_{w_{i} \in A } P(w_{i})}_{P(A)} + \underbrace{\sum\limits_{w_{i} \in B } P(w_{i})}_{P(B)} - \underbrace{\sum\limits_{w_{i} \in A\cap B } P(w_{i})}_{P(A\cap B)}$$

1) if $A\cap B =0,\ then\ P(A \cup B) = P(A) + P(B)$
   This is obvious from [4]
6) $P(A \cup B) \leq P(A) + P(B)$
   This is obvious from [4]
7) $P(\neg{A}) = 1 - P(A)$
   That one is obvious from the probability definition ($\sum\limits_{i=1}^{n}P_{i}= 1$)

#### Key questions:
How is the probability of an elementary event within a fundamental probability set defined, and what is the condition for the sum of these probabilities?
?
The probability is a number assigned to each of the elementary events, showing how likely you are to get this event from a probability experiment. It is required that $\sum\limits_{w\in\Omega} P(w)=1$
<!--SR:!2025-02-12,4,278-->


How is the probability of an event $A$ calculated if you know the probabilities of the elementary events in $A$?
?
$P(A) = \sum\limits_{w\in A}(P(w))$
<!--SR:!2025-02-12,4,278-->


Prove $P(A\cup B) = P(A) + P(B) - P(A \cap B)$
?
>[!proof]-
>Let $P(A \cap B)$ be not zero.
>Then the whole fundamental probability space $A\cup B$ can be divided into sets
>- $A \setminus B = {w_{i},i\in A, i\not\in B }$
>- $B \setminus A = {w_{i},i\in B, i\not\in A }$
>- $A \cap B = {w_{i},i\in B, i\in A }$
>  $$\underbrace{\sum\limits_{w_{i} \in A \cup B} P(w_{i})}_{P(A\cup B)}=\sum\limits_{w_{i} \in A \setminus B} P(w_{i}) + \sum\limits_{w_{i} \in B \setminus A} P(w_{i})$$
>  $$=\underbrace{\sum\limits_{w_{i} \in A } P(w_{i})}_{P(A)} + \underbrace{\sum\limits_{w_{i} \in B } P(w_{i})}_{P(B)} - \underbrace{\sum\limits_{w_{i} \in A\cap B } P(w_{i})}_{P(A\cap B)}$$
<!--SR:!2025-02-12,4,278-->



How can you calculate the **probability of the complement** of an event $A$, denoted as $P(\neg{A})$?
?
$$P(\Omega) = 1,$$
$$\Omega = \{A\cup\neg{A}\},$$
$$P(\Omega)=P(A)+P(\neg{A}),$$
$$P(\neg{A})= P(\Omega)- P(A) = 1 - P(A)$$
<<<<<<< HEAD
<!--SR:!2025-08-31,218,330-->
=======

>>>>>>> main

