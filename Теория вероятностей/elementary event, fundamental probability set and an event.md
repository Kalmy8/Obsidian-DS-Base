#🃏/probability-theory
let's say you are running some **experiment** which can result into multiple different outcomes. Each outcome then will be called an **elementary event**, altogether they do **form a fundamental probability set**. ^f482b1

**Example: for rolling a dice**, all possible outcomes would be $1,2,3,4,5,6$. Each single outcome is called an **elementary event**. 

Usually every elementary event is assigned to small omega Greek letter like $w_{1},w_{2},..,w_{6}$.

We can then define a fundamental probability set on this experiment as a set containing all elementary events and denote this set with the letter $\Omega$:
$$\Omega = \{w_{1},w_{2},..,w_{6}\}$$
---
**You can also define an elementary event as a combination or sequence if your outcome is complex.** For example, for rolling 2 dices, the set would be
$$\Omega = \{w : (i,j); i,j \in(⚀⚁⚂⚃⚄⚅) \}$$ as your outcome now includes actually 2 "facts".

The general denotion rule is :
$$\Omega = \{w : [a,b,c]\}\ for\ collections,$$
$$\Omega = \{w : (a,b,c)\}\ for\ ordered\ sequences$$ 

**Some other examples:**
n-attempts to toss a coin results in:
$$\Omega = \{w : (a_{1},a_2,..,a_{n}),a \in(Heads/Tails)\}$$ 

extracting 2 balls from a box with black/white balls results into
$$\Omega = \{w : [a_{1},a_{2}],a \in(White/Black)\}$$ 

---
**An Event** is just an arbitrary subspace of the **fundamental probability set**. They are usually denoted with grand alphabet letters like $A,B$ and since they are **sets**, all set-defined mathematical operations are available for them, including **intersection/difference/union** and etc. ^f9d291

Example: 
Let's say we are tossing a coin 2 times so our **fundamental probability set** is defined as:
$$\Omega = \{w : (a_{1},a_{2}),a \in(Heads/Tails)\}$$
When we could define an Event $A$ as:
$$A = \{(Heads, Heads)\}, or$$
$$A =  \{(Heads, Tails)\}, or$$
$$A =  \{(Tails, Heads)\}, or$$
$$A = \{(Tails, Tails)\}.$$

#### Key questions:

What is an elementary event in the context of probability experiment such as rolling one/two dice(s) experiment? How is it usually denoted?
?
Elementary event is a single outcome of a probability experiment. If you roll a single dice, you can get 6 possible outcomes, each outcome will be called an elementary event and will be denoted like $w_{1},w_{2},..,w_{6}$. If you roll 2 dices at once, there are 36 possible outcomes and they will be denoted like $w_{1},w_{2},..,w_{36}$.
<!--SR:!2025-03-01,70,310-->

What is a fundamental probability set? How would you define a fundamental probability set for rolling two dice?
?
Fundamental probability set is a mathematical set containing all possible outcomes of a probability experiment. For rolling 2 dices, we can define it like $\Omega=\{(i,j):i,j = 1,2..,6\}$
<!--SR:!2025-09-21,236,330-->

What is the difference between denoting elementary events as sequences vs. collections? Give a real-world example of each.
?
Tossing a coin 2 times in a row: $\Omega=\{w : (a,b)\text{ for } a,b \in (Heads, Tails)\}$
Rolling 2 dices at once: $\Omega=\{w : [a,b]\text{ for } a,b \in (⚀⚁⚂⚃⚄⚅)\}$
<!--SR:!2025-02-20,26,290-->

Definition of an event in probability. Example of how it can be represented using subsets of a fundamental probability set
?
Event is just an arbitrary subspace of the fundamental probability set. So given the set $\Omega = \{w_{1},w_{2},..,w_{6}\}$ an event can be defined as  $A = \{w_{1}\}$ or $B = \{w_{4},w_{5},w_{6}\}$.
<!--SR:!2025-02-01,59,310-->