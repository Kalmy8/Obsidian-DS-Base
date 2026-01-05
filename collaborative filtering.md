---
type: note
status: done
tags: [tech/ml/recsys]
sources:
- "[[Recommender Systems Course]]"
authors:
-
---
- [[content and item based recommendations]] approach assumes feature vectors for content were already pre-calculated and "frozen"
	- in most cases that's not true (sometimes it's very hard to come up with a set of features like for music, sometimes our pre-calculated features won't be accurate)
- **Collaborative filtering approach combines both content and item based recommendation problems:** the main idea is to 
	- We can do this sequentially (Alternating Least Squares):![[Pasted image 20251023013300.png]]
	- Or simultaneously (which is more effective and simply combines both optimization loss functions into a single one)![[Pasted image 20251023013050.png]]
