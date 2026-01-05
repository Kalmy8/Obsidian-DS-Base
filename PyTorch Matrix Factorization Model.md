---
type: note
status: done
tags: [tech/ml/recsys]
sources:
-
authors:
- "[[Recommender Systems Course]]"
---

 1. Get model predictions (`outputs = model(x)`).
 2. Calculate the difference between predictions and actual ratings (`loss = loss_fn(...)`).
 3. Calculate gradients (`loss.backward()`).
 4. Update the model's embedding vectors (`optimizer.step()`).

**Stage 4: Analysis of Learned Embeddings**

This final step proves that the latent factors aren't just random numbers; they have successfully captured implicit properties like genre, tone, and audience appeal from the data.

**Key Questions:**

1. Is the model in the notebook a content-based, collaborative filtering, or hybrid model?
?
- It is a pure **collaborative filtering** model. It only uses the user-item interaction matrix (the ratings) to learn. It does not use any side information like movie genres or user demographics.

2. What is the purpose of the `torch.nn.Embedding` layer in this model?
?
- It serves as an efficient lookup table to store and retrieve the latent factor vectors for users and items. Given a user's integer index, it returns their corresponding `n_factor`-dimensional vector.

3. What does the final K-Means clustering step demonstrate?
?
- It demonstrates that the model has learned meaningful representations (embeddings) for the movies. By clustering these embeddings, we can see that movies with similar implicit characteristics (like genre or target audience) are grouped together, even though this information was never explicitly given to the model. It learned these relationships solely from user rating patterns.

4. How does this model handle the sparsity of the rating matrix?
?
- The model avoids the sparsity problem rather than fighting it. It does this in three key ways:
 1. **It never creates the full user-item matrix.** It works directly with the `ratings_df` DataFrame, which is a long list of known `(user, item, rating)` interactions—an efficient way to store sparse data.
 2. **It only trains on existing data.** The `DataLoader` feeds the model batches of known ratings. The millions of missing ratings are completely ignored during training, making the process computationally efficient.
 3. **It uses `torch.nn.Embedding` for storage.** Instead of a giant `n_users x n_items` matrix, it stores two smaller, dense matrices for user and item factors (`n_users x n_factors` and `n_items x n_factors`). This is vastly more memory-efficient.
