---
type: note
status: done
tags: [math/probability-theory]
sources:
-
authors:
-
---
**An Event** is just an arbitrary subspace of the **fundamental probability set**. They are usually denoted with grand alphabet letters like $A,B$ and since they are **sets**, all set-defined mathematical operations are available for them, including **intersection/difference/union** and etc. ^f9d291

Example: 
Let's say we are tossing a coin 2 times so our **fundamental probability set** is defined as:
$$\Omega = \{w : (a_{1},a_{2}),a \in(Heads/Tails)\}$$
When we could define an Event $A$ as:
$$A = \{(Heads, Heads)\}, or$$
$$A = \{(Heads, Tails)\}, or$$
$$A = \{(Tails, Heads)\}, or$$
$$A = \{(Tails, Tails)\}.$$

#### Key questions:

What is an elementary event in the context of probability experiment such as rolling one/two dice(s) experiment? How is it usually denoted?
?
Elementary event is a single outcome of a probability experiment. If you roll a single dice, you can get 6 possible outcomes, each outcome will be called an elementary event and will be denoted like $w_{1},w_{2},..,w_{6}$. If you roll 2 dices at once, there are 36 possible outcomes and they will be denoted like $w_{1},w_{2},..,w_{36}$.
<!--SR:!2026-01-09,299,330-->

What is a fundamental probability set? How would you define a fundamental probability set for rolling two dice?
?
Fundamental probability set is a mathematical set containing all possible outcomes of a probability experiment. For rolling 2 dices, we can define it like $\Omega=\{(i,j):i,j = 1,2..,6\}$
<!--SR:!2026-10-03,365,350-->

What is the difference between denoting elementary events as sequences vs. collections? Give a real-world example of each.
?
Tossing a coin 2 times in a row: $\Omega=\{w : (a,b)\text{ for } a,b \in (Heads, Tails)\}$
Rolling 2 dices at once: $\Omega=\{w : [a,b]\text{ for } a,b \in (⚀⚁⚂⚃⚄⚅)\}$
<!--SR:!2026-07-20,365,330-->

Definition of an event in probability. Example of how it can be represented using subsets of a fundamental probability set
?
Event is just an arbitrary subspace of the fundamental probability set. So given the set $\Omega = \{w_{1},w_{2},..,w_{6}\}$ an event can be defined as $A = \{w_{1}\}$ or $B = \{w_{4},w_{5},w_{6}\}$.
<!--SR:!2025-10-19,253,330-->