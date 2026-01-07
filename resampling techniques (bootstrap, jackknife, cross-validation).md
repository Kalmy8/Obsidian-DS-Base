---
type: note
status: done
tags: [math/statistics, machine-learning]
sources:
- "[[Statistics Basics (1st)]]"
authors:
-
---

#🃏/semantic/math/statistics #🏷️/semantic/machine-learning

**Related:** [[Law of Large Numbers (LLN)]], [[Central Limit Theorem (CLT)]], [[variance]], [[statistical sampling techniques]]

## Definition

**Resampling techniques** are computational methods for:
1. Estimating the **variability** of a statistic (standard error, confidence intervals)
2. Assessing **model performance** and generalization
3. Avoiding strong parametric assumptions

These methods repeatedly draw samples from the original data to simulate the sampling distribution.

## Bootstrap

### Concept

The **bootstrap** estimates the sampling distribution of a statistic by:
1. Repeatedly resampling **with replacement** from the original sample
2. Computing the statistic on each resample
3. Using the distribution of these statistics to estimate variability

**Key insight:** The sample approximates the population, so resampling from the sample approximates resampling from the population.

### Algorithm

1. Given sample $\mathbf{X} = (X_1, \ldots, X_n)$
2. For $b = 1, \ldots, B$ (e.g., $B = 1000$):
   - Draw $n$ observations **with replacement** from $\mathbf{X}$ → $\mathbf{X}^*_b$
   - Compute statistic $\hat\theta^*_b$ on $\mathbf{X}^*_b$
3. Use $\{\hat\theta^*_1, \ldots, \hat\theta^*_B\}$ to estimate:
   - **Standard error**: $SE(\hat\theta) \approx \text{std}(\hat\theta^*_1, \ldots, \hat\theta^*_B)$
   - **Confidence interval**: Use percentiles (e.g., 2.5% and 97.5% for 95% CI)

### When to Use

✅ **Good for:**
- Estimating SE of complex statistics (median, correlation, ratio)
- Non-parametric confidence intervals
- When theoretical formulas are unavailable or hard to derive

⚠️ **Limitations:**
- Assumes the sample is representative of the population
- Requires sufficient sample size ($n \geq 30$ typically)
- With replacement: some observations appear multiple times in each resample

### Demonstration

>[!info]- Code snippet: Bootstrap for median CI
>```python
>import numpy as np
>import matplotlib.pyplot as plt
>
>rng = np.random.default_rng(42)
>
># Original sample from skewed distribution
>sample = rng.lognormal(mean=2.0, sigma=0.5, size=100)
>
># Bootstrap
>B = 10_000
>bootstrap_medians = np.empty(B)
>
>for b in range(B):
>    resample = rng.choice(sample, size=len(sample), replace=True)
>    bootstrap_medians[b] = np.median(resample)
>
># Results
>median_est = np.median(sample)
>se_median = np.std(bootstrap_medians, ddof=1)
>ci_lower, ci_upper = np.percentile(bootstrap_medians, [2.5, 97.5])
>
>print(f"Sample median: {median_est:.2f}")
>print(f"Bootstrap SE: {se_median:.2f}")
>print(f"95% Bootstrap CI: [{ci_lower:.2f}, {ci_upper:.2f}]")
>
># Plot
>plt.figure(figsize=(10, 5))
>plt.hist(bootstrap_medians, bins=50, density=True, alpha=0.6, edgecolor='black')
>plt.axvline(median_est, color='red', linestyle='--', linewidth=2, label=f'Sample median = {median_est:.2f}')
>plt.axvline(ci_lower, color='green', linestyle=':', linewidth=2, label=f'95% CI')
>plt.axvline(ci_upper, color='green', linestyle=':', linewidth=2)
>plt.title("Bootstrap Distribution of Median")
>plt.xlabel("Median")
>plt.ylabel("Density")
>plt.legend()
>plt.show()
>```

## Jackknife

### Concept

The **jackknife** estimates bias and variance by:
1. Systematically leaving out **one observation at a time**
2. Computing the statistic on each reduced sample
3. Using these statistics to assess stability and bias

**Key idea:** Assess how much each observation influences the statistic.

### Algorithm

1. Given sample $\mathbf{X} = (X_1, \ldots, X_n)$
2. For $i = 1, \ldots, n$:
   - Create sample $\mathbf{X}_{(-i)} = (X_1, \ldots, X_{i-1}, X_{i+1}, \ldots, X_n)$ (all except $X_i$)
   - Compute statistic $\hat\theta_{(-i)}$ on $\mathbf{X}_{(-i)}$
3. Estimate:
   - **Bias**: $\text{bias} = (n-1)(\bar{\hat\theta}_{(\cdot)} - \hat\theta)$
   - **Standard error**: $SE(\hat\theta) = \sqrt{\frac{n-1}{n}\sum_{i=1}^n(\hat\theta_{(-i)} - \bar{\hat\theta}_{(\cdot)})^2}$

where $\bar{\hat\theta}_{(\cdot)} = \frac{1}{n}\sum_{i=1}^n \hat\theta_{(-i)}$.

### When to Use

✅ **Good for:**
- Bias estimation and correction
- Influence analysis (which observations are most important)
- Computationally cheaper than bootstrap (only $n$ resamples vs. $B \gg n$)

⚠️ **Limitations:**
- Less accurate than bootstrap for many statistics
- Assumes smooth statistics (can fail for median, quantiles)
- Not suitable for small $n$

### Demonstration

>[!info]- Code snippet: Jackknife for mean SE
>```python
>import numpy as np
>
>rng = np.random.default_rng(42)
>sample = rng.normal(loc=50, scale=10, size=30)
>
>n = len(sample)
>jackknife_means = np.empty(n)
>
>for i in range(n):
>    # Leave-one-out sample
>    loo_sample = np.delete(sample, i)
>    jackknife_means[i] = np.mean(loo_sample)
>
># Jackknife SE
>se_jackknife = np.sqrt((n - 1) / n * np.sum((jackknife_means - np.mean(jackknife_means))**2))
>
># Compare to analytical SE
>se_analytical = np.std(sample, ddof=1) / np.sqrt(n)
>
>print(f"Sample mean: {np.mean(sample):.2f}")
>print(f"Jackknife SE: {se_jackknife:.2f}")
>print(f"Analytical SE: {se_analytical:.2f}")
>print(f"Difference: {abs(se_jackknife - se_analytical):.4f}")
>```

## Cross-Validation (CV)

### Concept

**Cross-validation** assesses model performance by:
1. Splitting data into **training** and **validation** sets
2. Training on training set, evaluating on validation set
3. Repeating with different splits to get robust performance estimate

**Key goal:** Estimate how well a model generalizes to unseen data.

### Types of Cross-Validation

#### 1. k-Fold Cross-Validation

**Algorithm:**
1. Split data into $k$ equal-sized folds
2. For $i = 1, \ldots, k$:
   - Use fold $i$ as validation, rest as training
   - Train model and compute error $e_i$
3. Average errors: $\text{CV error} = \frac{1}{k}\sum_{i=1}^k e_i$

**Common choices:** $k = 5$ or $k = 10$.

#### 2. Leave-One-Out Cross-Validation (LOOCV)

- Special case of k-fold with $k = n$ (each fold is a single observation)
- **Pros:** Uses almost all data for training (unbiased)
- **Cons:** Computationally expensive ($n$ models to train)

#### 3. Stratified k-Fold

- For classification: ensures each fold has similar class proportions
- Reduces variance in CV estimates

#### 4. Time-Series CV (Rolling Window)

- For temporal data: train on past, validate on future
- Respects time ordering (no future information leakage)

### When to Use

✅ **Good for:**
- Model selection (comparing different algorithms)
- Hyperparameter tuning
- Estimating generalization error
- Small to medium datasets

⚠️ **Limitations:**
- Computationally expensive (train $k$ models)
- Can be biased for very small datasets
- Time-series: simple k-fold violates temporal order

### Demonstration

>[!info]- Code snippet: k-Fold CV for regression
>```python
>import numpy as np
>from sklearn.model_selection import KFold
>from sklearn.linear_model import LinearRegression
>from sklearn.metrics import mean_squared_error
>
>rng = np.random.default_rng(42)
>
># Synthetic data
>n = 100
>X = rng.uniform(0, 10, size=(n, 1))
>y = 2 * X.ravel() + 3 + rng.normal(0, 1, size=n)
>
># 5-fold CV
>kf = KFold(n_splits=5, shuffle=True, random_state=42)
>cv_errors = []
>
>for train_idx, val_idx in kf.split(X):
>    X_train, X_val = X[train_idx], X[val_idx]
>    y_train, y_val = y[train_idx], y[val_idx]
>    
>    model = LinearRegression()
>    model.fit(X_train, y_train)
>    y_pred = model.predict(X_val)
>    
>    mse = mean_squared_error(y_val, y_pred)
>    cv_errors.append(mse)
>
>print(f"5-Fold CV MSE: {cv_errors}")
>print(f"Mean CV MSE: {np.mean(cv_errors):.3f} ± {np.std(cv_errors):.3f}")
>```

## Comparison Table

| Method | Resampling Strategy | Use Case | Computational Cost |
|--------|-------------------|----------|-------------------|
| **Bootstrap** | With replacement, $B$ resamples | SE, CI for any statistic | $O(B \cdot n)$ |
| **Jackknife** | Leave-one-out, $n$ resamples | Bias correction, influence | $O(n)$ |
| **k-Fold CV** | Non-overlapping splits | Model evaluation | $O(k \cdot \text{train time})$ |
| **LOOCV** | Leave-one-out for models | Unbiased error estimate | $O(n \cdot \text{train time})$ |

## Review questions

What is the key difference between bootstrap and jackknife?
?
- **Bootstrap**: Resample **with replacement** (same size as original), creates $B$ resamples (e.g., 1000+)
- **Jackknife**: Leave **one observation out** at a time, creates $n$ resamples (one per observation)
- Bootstrap is more general and accurate; jackknife is faster and good for bias estimation

When should you use bootstrap?
?
- When you need **standard error or confidence intervals** for complex statistics (median, correlation, ratio)
- When theoretical formulas are unavailable or hard to derive
- Requires sufficient sample size ($n \geq 30$) and representative sample
- More accurate than jackknife for most statistics

What is k-fold cross-validation and why is it used?
?
- Split data into $k$ equal folds; train on $k-1$ folds, validate on 1 fold; repeat $k$ times
- Used for **model evaluation** and **hyperparameter tuning**
- Provides robust estimate of generalization error by averaging across $k$ splits
- Common choices: $k=5$ or $k=10$

What are the advantages and disadvantages of LOOCV?
?
- **Advantages**: Nearly unbiased (trains on $n-1$ data points), deterministic (no randomness in splits)
- **Disadvantages**: Very expensive ($n$ models to train), high variance in error estimate
- Generally prefer k-fold ($k=5$ or $k=10$) for better bias-variance tradeoff

How does cross-validation differ from bootstrap for model evaluation?
?
- **Cross-validation**: Non-overlapping splits, each observation used once per fold, for **model performance**
- **Bootstrap**: With-replacement sampling, observations can appear multiple times, for **parameter uncertainty**
- CV estimates generalization error; bootstrap estimates sampling variability of statistics
- Use CV for model selection, bootstrap for confidence intervals

