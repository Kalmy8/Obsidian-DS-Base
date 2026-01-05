## Time complexity
is an attribute of an algorithm. Thus it has to be hardware-independent.

It's calculated **as the number of atomic elementary operations** which interpreter should do to process N-sized collection.

The notation is $O(N)$ and it means the approximate upper estimate of complexity if value $N$ is enormous. 

![Pasted image 20241202183217.png](Pasted%20image%2020241202183217.png)
Since it's a rough estimate, some weird stuff is happening here, but you will eventually get used to it:
- $O(constant\times N + constant)$ roughly equals to $O(N)$, even if the constant is huge (like $1e10$). That's because $N$ is considered to approach the infinity, so even $1e10\times N$ is far better than $N\ log(N)$

Some common operations complexity would be:
- Slicing O(n)
- sum O(n)
- Indexing O(1)
- Append/pop O(1)
- Insert O(n)

## Space Complexity

Space complexity is usually divided into 2 categories:
- Input space: that's just how much memory you has to allocate to store the input collections
- Auxiliary space: that's just **how much additional memory beyond the input space** you has to allocate. It depends on several key factors:
	- **Variables**: How many variables are you using?
	- **Data structures**: How much space do additional lists, sets, dictionaries, etc., require?
	- **Function call stack**: Recursive functions use space for each level of recursion.

[neetcode algorithms tasks](neetcode%20algorithms%20tasks.md)
[yandex algorithms lections](yandex%20algorithms%20lections.md)
[yandex algorithms practicum](yandex%20algorithms%20practicum.md)