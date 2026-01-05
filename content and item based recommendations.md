---
type: note
status: done
tags: [tech/ml/recsys]
sources:
- "[[Recommender Systems Course]]"
authors:
-
---
- **Assume that the promoted content has some common features (so can be represented with a vector), we have defined and calculated them!**
	- Users would also have some features, our **goal here would be to learn those feature vectors,** which would give us the possibility to predict if the user will like a particular movie or not 
	- User's ratings can be expressed with a linear regression like: score = content_vector X user_vector 
	- ![[Pasted image 20251023010145.png]]
	- We can now state a mathematical optimization problem, picking for example a mean square error loss function:
		- ![[Pasted image 20251023012700.png]]
- **Opposite situation: assume that our users have some common measurable features (like how do you like romantical movies?)** 
	- If we think of our ratings like of a linear combination of user's and content's vectors, then, again, you can state an opposite learning task as follows:
	- ![[Pasted image 20251023012552.png]]