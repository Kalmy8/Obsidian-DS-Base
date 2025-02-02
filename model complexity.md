is a relative/intuitive metric which measures the model ability to extract unobvious, logically/computationally complex relationships between the independent and the target variable

Some classic ML model's estimated complexity:

| Model                         | Complexity     | Bias                            | Variance | Stability |
| ----------------------------- | -------------- | ------------------------------- | -------- | --------- |
| Linear Regression             | Low            | High                            | Low      | High      |
| Polynomial Regression         | Medium         | Low to High (depends) on degree | High     | Low       |
| Decision Trees                | Medium         | Low to High (depends on depth)  | High     | Low       |
| Support Vector Machines (SVM) | Medium to High | Low to High (depends on kernel) | Medium   | Medium    |
| Neural Networks               | High           | Low                             | High     | Low       |

**Explanation:**
- **Complexity:** This refers to the model's capacity to learn complex patterns. More complex models can fit intricate relationships but are also more prone to overfitting.
- **Bias:** This measures the systematic error of a model. High bias models make strong assumptions about the data, leading to underfitting.
- **Variance:** This measures the sensitivity of a model to small changes in the training data. High variance models are prone to overfitting, as they can capture noise in the data.
- **Stability:** This refers to how sensitive a model's predictions are to small changes in the training data. More stable models are less prone to overfitting.

**General Trend:**

- **Simple models** (like linear regression) are generally more stable but can suffer from high bias, leading to underfitting.
- **Complex models** (like neural networks) are usually longer/more expensive to train and inference, and they are prone to overfitting, meaning that they do often require some [variance-reducing techniques](variance-reducing%20techniques.md).