---
type: note
status: done
tags: [tech/ml/recsys]
sources:
-
authors:
-
- "[[Recommender Systems Course]]"
---
4. We calculate the error using a loss function (like MSE for explicit ratings, or BPR/WARP for implicit).
5. The magic step: The error gradient is backpropagated to update **all the feature embeddings** that were used to construct `p_A` and `q_X`.

So, if `user_A` has features (`age=30`, `country=UK`) and `item_X` has features (`genre=action`, `year=2020`), this single interaction will nudge the embedding vectors for all four of those features. The interaction data is teaching the model what the features *mean* in terms of user preference.

### How This Solves the Cold-Start Problem (Mathematically)

Let's say a new user `z` signs up and provides their features, `F_z = {age=30, country=CA}`.
 `p_z = (embedding for 'age=30') + (embedding for 'country=CA')`

The model can create this vector `p_z` because the feature embeddings for `age=30` and `country=CA` have already been trained on the interactions of thousands of other users. The model can infer the preferences of user `z` based on the learned preferences associated with their features. It can then compute `p_z · q_i` for all items `i` and generate a ranked list of recommendations from day one.

**Key Questions:**

1. What is the fundamental mathematical difference between how a hybrid model and a pure collaborative filtering model represent a user?
?
- In **pure collaborative filtering** (like SVD), a user `u` is represented by a single, unique latent vector `p_u` that is learned directly from their interaction history.
- In a **hybrid model** (like LightFM), a user `u` is represented by the **sum of the latent vectors of their features** (`p_u = Σ e_j`). The model learns the feature vectors, not the user vector itself.

2. During training of a hybrid model, what parameters are actually being updated by the optimizer?
?
- The optimizer updates the embedding matrices for the **features** (`E_U` and `E_I`). When an interaction `(u, i)` is processed, the gradients from the loss function flow back to modify the embeddings of all features belonging to user `u` and item `i`.

3. Explain step-by-step how a hybrid model recommends an item to a brand-new user who has no interaction history but has provided features.
?
- 1. The model takes the new user's features (e.g., `age=25`, `location=DE`).
- 2. It looks up the pre-trained embedding vectors for each of these features in its user-feature embedding matrix (`E_U`).
- 3. It sums these feature vectors to construct a complete latent representation for the new user (`p_new_user`).
- 4. It calculates the dot product of this new user vector with the latent vectors of all existing items (`r̂ = p_new_user · q_i`).
- 5. Finally, it ranks the items by this score and presents the top-ranked items as the recommendation.
