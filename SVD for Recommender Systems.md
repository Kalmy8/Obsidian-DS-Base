---
type: note
status: done
tags: [tech/ml/recsys]
sources:
- "[[Recommender Systems Course]]"
authors:
-
---
#🃏/source/recsys-course

**Codewords:** Singular Value Decomposition (SVD), Matrix Factorization, Latent Factor Model, FunkSVD, Dimensionality Reduction, Collaborative Filtering

## Singular Value Decomposition (SVD) for Recommender Systems

**Singular Value Decomposition (SVD)** is a powerful matrix factorization technique from linear algebra. In the context of recommender systems, it's used to decompose the user-item interaction matrix into smaller, dense matrices representing latent (hidden) features of users and items.

The core idea is that the original ratings matrix `R` (users x items) can be approximated by the product of three other matrices:

`R ≈ U · Σ · Vᵀ`

![[https://miro.medium.com/v2/resize:fit:1400/1*5cI-T4y2Q3-O8C-12V4-VA.png]]

### The Problem with Pure SVD

Pure SVD cannot be directly applied to typical recommender system problems because the user-item rating matrix `R` is **sparse**—it has many missing values. SVD requires a dense matrix with no missing entries. While we could fill the missing values (e.g., with the mean rating), this is often inaccurate and computationally expensive.

## FunkSVD: The Netflix Prize Approach

A more practical approach, often referred to as **FunkSVD** (popularized during the Netflix Prize competition), is a latent factor model that directly learns the factor matrices `U` and `V` without needing to perform a full SVD.

It bypasses the sparse matrix problem by only considering the ratings that are actually present in the matrix. The model learns to predict a rating for user `u` and item `i` as the dot product of their latent feature vectors:

`r̂_ui = p_uᵀ · q_i`

### The Optimization Problem

The goal is to find the user (`p_u`) and item (`q_i`) vectors that minimize the prediction error on the set of known ratings (`K`). This is done by minimizing a loss function, typically the regularized squared error:

`Loss = Σ_(u,i)∈K (r_ui - p_uᵀ · q_i)² + λ (||p_u||² + ||q_i||²)`

This loss function is identical in structure to the one you defined for collaborative filtering. It can be optimized using either **Stochastic Gradient Descent (SGD)** or **Alternating Least Squares (ALS)**.

### Example: Training with Stochastic Gradient Descent (SGD)

```python
import numpy as np

# Sample user-item rating matrix (0 means no rating)
ratings = np.array([
 [5, 3, 0, 1],
 [4, 0, 0, 1],
 [1, 1, 0, 5],
 [1, 0, 0, 4],
 [0, 1, 5, 4],
])

def funk_svd(ratings_matrix, n_factors=2, learning_rate=0.01, n_epochs=100, lambda_reg=0.02):
 """
 Implements FunkSVD using Stochastic Gradient Descent.
 """
 n_users, n_items = ratings_matrix.shape
 
 # Initialize user and item latent feature matrices with random values
 P = np.random.rand(n_users, n_factors) # User features
 Q = np.random.rand(n_items, n_factors) # Item features
 
 # Get the coordinates of non-zero ratings
 non_zero_ratings = ratings_matrix.nonzero()
 
 for epoch in range(n_epochs):
 # Iterate over each known rating
 for u, i in zip(non_zero_ratings[0], non_zero_ratings[1]):
 # Prediction error
 error = ratings_matrix[u, i] - np.dot(P[u, :], Q[i, :])
 
 # Update user and item vectors using SGD
 p_u_old = P[u, :]
 q_i_old = Q[i, :]
 
 P[u, :] += learning_rate * (error * q_i_old - lambda_reg * p_u_old)
 Q[i, :] += learning_rate * (error * p_u_old - lambda_reg * q_i_old)

 return P, Q.T

# Run the SVD
user_features, item_features = funk_svd(ratings)

# Reconstructed (predicted) full ratings matrix
predicted_ratings = np.dot(user_features, item_features)

print("Original Ratings:\n", ratings)
print("\nPredicted Ratings:\n", predicted_ratings)

# Example: Predict rating for user 2, item 2 (which was unknown)
user_id = 2
item_id = 2
predicted_rating = predicted_ratings[user_id, item_id]
print(f"\nPredicted rating for user {user_id}, item {item_id}: {predicted_rating:.2f}")
```

**Practice Problem: Hyperparameter Tuning for SVD**

Using the provided `funk_svd` implementation and dataset, investigate the impact of different hyperparameters on the model's performance.

```python
# Toy data for the problem
practice_ratings = np.array([
 [5, 5, 2, 0, 1],
 [4, 0, 3, 1, 2],
 [0, 4, 1, 5, 5],
 [1, 2, 5, 0, 0],
 [2, 0, 0, 4, 1],
 [3, 3, 3, 3, 3],
])
```

**Task:**
1. Calculate the Mean Squared Error (MSE) on the *known* ratings for the default hyperparameters (`n_factors=2`, `learning_rate=0.01`, `lambda_reg=0.02`).
2. Experiment with the number of latent factors (`n_factors`). Try values like 1, 5, and 10. How does this affect the reconstruction error and the predicted ratings?
3. Experiment with the learning rate (`learning_rate`). Try a smaller value (0.001) and a larger value (0.1). What do you observe?
4. Experiment with the regularization parameter (`lambda_reg`). Try a value of 0 and a larger value (0.2). How does this impact the values in the predicted matrix?

---

**Key Questions:**

1. What is the main limitation of applying pure SVD to recommender system problems?
?
- Pure SVD requires a dense matrix with no missing values. However, user-item rating matrices in real-world scenarios are extremely sparse, containing mostly unknown ratings.
<!--SR:!2026-01-08,1,230-->

2. How does FunkSVD (or latent factor models) solve the sparsity problem?
?
- It ignores the missing values and focuses only on the known ratings. It directly learns the user and item latent feature matrices by minimizing the prediction error on these known ratings, typically using optimization algorithms like SGD or ALS.
<!--SR:!2026-01-08,1,230-->

3. What is the relationship between Collaborative Filtering, Matrix Factorization, and SVD?
?
- **Collaborative Filtering** is the high-level approach of using the "wisdom of the crowd" (user-item interactions) to make recommendations.
- **Matrix Factorization** is a class of collaborative filtering models that decomposes the user-item matrix into latent feature matrices.
- **SVD** is a specific matrix factorization technique. In practice, algorithms like FunkSVD that are *inspired* by SVD are used to perform the factorization on sparse matrices.
<!--SR:!2026-01-08,1,230-->

4. What is the role of the regularization term in the SVD loss function?
?
- The regularization term (`λ (||p_u||² + ||q_i||²)`) prevents the model from overfitting to the training data. It penalizes overly large values in the user and item feature vectors, leading to a more generalizable model that performs better on unseen data.
<!--SR:!2026-01-08,1,230-->

### "FunkSVD" vs. True SVD: A Critical Clarification

It is important to note that the term "SVD" as used in the recommender system community is a **historical misnomer**. The model described here is technically a **Latent Factor Model solved with Gradient Descent**.

| Aspect | Classical SVD (Linear Algebra) | FunkSVD (Recommender Systems) |
| :--- | :--- | :--- |
| **Formula** | `R = U · Σ · Vᵀ` | `R ≈ P · Qᵀ` |
| **Input Matrix** | Requires a **dense** matrix (no missing values) | Designed for **sparse** matrices (many missing values) |
| **Output Matrices**| `U` and `V` are **orthogonal** | `P` and `Q` are **not** orthogonal |
| **Sigma (`Σ`)** | Has an explicit diagonal matrix of singular values | Has **no** explicit `Σ` matrix; its effect is absorbed into `P` and `Q` |

The name "FunkSVD" became popular during the Netflix Prize after Simon Funk successfully used this method. While it's conceptually similar to SVD (decomposing a matrix), it is a different, more flexible algorithm designed to solve a different problem (prediction on sparse data).
