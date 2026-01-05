---
type: note
status: done
tags: []
sources:
-
authors:
-
---
allow you to create subsamples of the original dataset with ability to prognose how will the descriptive statistic change because of such operation

| **Technique** | **Key Idea** | **Pros** | **Cons** |
| ------------------------ | ----------------------------------- | ------------------------------- | ------------------------------------ |
| **Bagging** | Random samples with replacement | Easy, variance reduction | May not reduce covariance completely |
| **Subsampling** | Random samples without replacement | Reduces dependence | Can leave out data points entirely |
| **Stratified Sampling** | Maintains class proportions | Good for imbalanced datasets | Adds complexity |
| **Jackknife Resampling** | Excludes one data point at a time | Theoretically robust | Computationally expensive |
| **Boosting Sampling** | Weighted sampling for hard examples | Reduces bias and variance | Prone to overfitting and noise |
| **Random Subspace** | Samples columns instead of rows | Great for high-dimensional data | Needs large feature space |
| **Cluster Sampling** | Samples within pre-defined clusters | Ensures diverse subsets | Relies on good clustering |