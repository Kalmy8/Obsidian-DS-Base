---
type: note
status: done
tags: ['math/statistics']
sources:
-
authors:
-
---
#🃏/semantic/math

**Codewords:** gradient descent, batch gradient descent, stochastic gradient descent, mini-batch gradient descent, learning rate, convergence, optimization, cost function, parameters update

## Gradient Descent Overview

**Gradient Descent** is a fundamental optimization algorithm used in machine learning to minimize the cost function by iteratively adjusting model parameters in the direction of steepest descent. It's the backbone of training most machine learning models, from linear regression to deep neural networks.

The core idea is simple: if you want to minimize a function, move in the direction opposite to its gradient (slope). The gradient points to the direction of steepest ascent, so moving in the opposite direction leads us toward the minimum.

### Mathematical Foundation

For a cost function J(θ) with parameters θ, the gradient descent update rule is:

```
θ = θ - α * ∇J(θ)
```

Where:

```python
import numpy as np
import matplotlib.pyplot as plt

def simple_cost_function(theta: float, x: np.ndarray, y: np.ndarray) -> float:
 """Simple quadratic cost function for demonstration."""
 predictions = theta * x
 return np.mean((predictions - y) ** 2)

def gradient(theta: float, x: np.ndarray, y: np.ndarray) -> float:
 """Gradient of the cost function."""
 predictions = theta * x
 return 2 * np.mean((predictions - y) * x)

# Example data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10]) # Perfect linear relationship: y = 2x
```

## 1. Batch Gradient Descent (BGD)

**Batch Gradient Descent** uses the entire training dataset to compute the gradient at each iteration. It processes all training examples simultaneously to update the parameters.

### Characteristics:
- **Stable convergence**: Uses all data points, providing stable gradient estimates
- **Memory intensive**: Requires loading entire dataset into memory
- **Slow per iteration**: Must process all examples before each update
- **Smooth convergence**: Less noisy than stochastic methods

```python
def batch_gradient_descent(
 x: np.ndarray, 
 y: np.ndarray, 
 learning_rate: float = 0.01, 
 max_iterations: int = 1000,
 tolerance: float = 1e-6
) -> tuple[float, list[float]]:
 """
 Implements batch gradient descent for linear regression.
 
 :param x: Input features
 :param y: Target values
 :param learning_rate: Step size for parameter updates
 :param max_iterations: Maximum number of iterations
 :param tolerance: Convergence threshold
 :return: Final parameter value and cost history
 """
 theta = 0.0 # Initialize parameter
 cost_history = []
 
 for iteration in range(max_iterations):
 # Compute cost
 cost = simple_cost_function(theta, x, y)
 cost_history.append(cost)
 
 # Check convergence
 if iteration > 0 and abs(cost_history[-2] - cost_history[-1]) < tolerance:
 print(f"Converged after {iteration} iterations")
 break
 
 # Compute gradient using ALL training examples
 grad = gradient(theta, x, y)
 
 # Update parameter
 theta = theta - learning_rate * grad
 
 if iteration % 100 == 0:
 print(f"Iteration {iteration}: theta = {theta:.4f}, cost = {cost:.6f}")
 
 return theta, cost_history

# Example usage
theta_final, costs = batch_gradient_descent(x, y, learning_rate=0.1)
print(f"Final parameter: {theta_final:.4f}")
print(f"Expected: 2.0 (since y = 2x)")
```

---

**Practice Problem: Batch Gradient Descent Implementation**

Given a dataset with multiple features, implement batch gradient descent for multiple linear regression.

```python
# Toy dataset for multiple linear regression
np.random.seed(42)
n_samples = 100
X = np.random.randn(n_samples, 2) # 2 features
true_weights = np.array([3.0, -2.0])
true_bias = 1.5
y = X @ true_weights + true_bias + 0.1 * np.random.randn(n_samples)

print(f"True weights: {true_weights}")
print(f"True bias: {true_bias}")
print(f"Dataset shape: X={X.shape}, y={y.shape}")
```

**Tasks:**
1. Implement batch gradient descent for multiple linear regression (y = Xw + b)
2. Track both weights and bias parameters
3. Plot the cost function convergence
4. Compare final parameters with true values

---

## 2. Stochastic Gradient Descent (SGD)

**Stochastic Gradient Descent** updates parameters using only one training example at a time. It randomly selects one example per iteration, making it much faster per iteration but more noisy in convergence.

### Characteristics:
- **Fast per iteration**: Processes only one example at a time
- **Memory efficient**: Doesn't need entire dataset in memory
- **Noisy convergence**: High variance in gradient estimates
- **Can escape local minima**: Noise can help escape shallow local minima
- **Requires learning rate scheduling**: Often needs decreasing learning rate

```python
def stochastic_gradient_descent(
 x: np.ndarray, 
 y: np.ndarray, 
 learning_rate: float = 0.01, 
 max_iterations: int = 1000,
 tolerance: float = 1e-6
) -> tuple[float, list[float]]:
 """
 Implements stochastic gradient descent for linear regression.
 
 :param x: Input features
 :param y: Target values
 :param learning_rate: Step size for parameter updates
 :param max_iterations: Maximum number of iterations
 :param tolerance: Convergence threshold
 :return: Final parameter value and cost history
 """
 theta = 0.0
 cost_history = []
 n_samples = len(x)
 
 for iteration in range(max_iterations):
 # Randomly select one training example
 random_idx = np.random.randint(0, n_samples)
 x_i = x[random_idx]
 y_i = y[random_idx]
 
 # Compute cost on current example
 cost = simple_cost_function(theta, x_i, y_i)
 cost_history.append(cost)
 
 # Compute gradient using ONLY the selected example
 grad = 2 * (theta * x_i - y_i) * x_i
 
 # Update parameter
 theta = theta - learning_rate * grad
 
 if iteration % 100 == 0:
 print(f"Iteration {iteration}: theta = {theta:.4f}, cost = {cost:.6f}")
 
 return theta, cost_history

# Example usage
theta_sgd, costs_sgd = stochastic_gradient_descent(x, y, learning_rate=0.1, max_iterations=500)
print(f"SGD Final parameter: {theta_sgd:.4f}")
```

---

**Practice Problem: SGD with Learning Rate Decay**

Implement stochastic gradient descent with exponential learning rate decay to improve convergence.

```python
# Same toy dataset as before
X_sgd = np.random.randn(50, 1).flatten()
y_sgd = 2 * X_sgd + 1 + 0.1 * np.random.randn(50)
```

**Tasks:**
1. Implement SGD with exponential learning rate decay: α_t = α_0 * decay^t
2. Compare convergence with fixed learning rate SGD
3. Experiment with different decay rates (0.95, 0.99, 0.999)
4. Plot both cost curves and learning rate schedules

---

## 3. Mini-Batch Gradient Descent (MBGD)

**Mini-Batch Gradient Descent** strikes a balance between batch and stochastic methods by using a small subset (mini-batch) of training examples for each parameter update. This is the most commonly used variant in practice.

### Characteristics:
- **Balanced approach**: Combines stability of batch with speed of stochastic
- **Vectorizable**: Can leverage matrix operations for efficiency
- **Tunable batch size**: Can adjust mini-batch size based on computational resources
- **Smoother than SGD**: Less noisy than pure stochastic methods
- **Faster than batch**: Doesn't require processing entire dataset

```python
def mini_batch_gradient_descent(
 x: np.ndarray, 
 y: np.ndarray, 
 batch_size: int = 32,
 learning_rate: float = 0.01, 
 max_iterations: int = 1000,
 tolerance: float = 1e-6
) -> tuple[float, list[float]]:
 """
 Implements mini-batch gradient descent for linear regression.
 
 :param x: Input features
 :param y: Target values
 :param batch_size: Size of mini-batch
 :param learning_rate: Step size for parameter updates
 :param max_iterations: Maximum number of iterations
 :param tolerance: Convergence threshold
 :return: Final parameter value and cost history
 """
 theta = 0.0
 cost_history = []
 n_samples = len(x)
 
 for iteration in range(max_iterations):
 # Randomly select mini-batch
 batch_indices = np.random.choice(n_samples, size=batch_size, replace=False)
 x_batch = x[batch_indices]
 y_batch = y[batch_indices]
 
 # Compute cost on mini-batch
 cost = simple_cost_function(theta, x_batch, y_batch)
 cost_history.append(cost)
 
 # Compute gradient using mini-batch
 grad = gradient(theta, x_batch, y_batch)
 
 # Update parameter
 theta = theta - learning_rate * grad
 
 if iteration % 100 == 0:
 print(f"Iteration {iteration}: theta = {theta:.4f}, cost = {cost:.6f}")
 
 return theta, cost_history

# Example usage
theta_mbgd, costs_mbgd = mini_batch_gradient_descent(x, y, batch_size=10, learning_rate=0.1)
print(f"Mini-batch GD Final parameter: {theta_mbgd:.4f}")
```

---

**Practice Problem: Mini-Batch Size Comparison**

Compare the performance of different mini-batch sizes on convergence speed and final accuracy.

```python
# Larger toy dataset for mini-batch comparison
np.random.seed(42)
X_large = np.random.randn(200, 1).flatten()
y_large = 2.5 * X_large + 1.2 + 0.15 * np.random.randn(200)
```

**Tasks:**
1. Implement mini-batch gradient descent with batch sizes: [1, 10, 32, 64, 200]
2. Compare convergence curves for each batch size
3. Measure training time for each variant
4. Analyze the trade-off between batch size and convergence stability

---

## Comparison of Gradient Descent Variants

| Aspect | Batch GD | Stochastic GD | Mini-Batch GD |
|--------|----------|---------------|---------------|
| **Speed per iteration** | Slow | Fast | Medium |
| **Memory usage** | High | Low | Medium |
| **Convergence stability** | Very stable | Noisy | Stable |
| **Parallelization** | Difficult | Easy | Easy |
| **Use case** | Small datasets | Large datasets | Most practical cases |

### When to Use Each Method:

- **Batch GD**: Small datasets (< 10,000 examples), when you need stable convergence
- **Stochastic GD**: Very large datasets, online learning, when memory is limited
- **Mini-Batch GD**: Most practical scenarios, deep learning, when you want balanced performance

---

**Practice Problem: Complete Comparison**

Implement all three variants and compare their performance on the same dataset.

```python
# Comprehensive comparison dataset
np.random.seed(42)
X_compare = np.random.randn(1000, 1).flatten()
y_compare = 3.2 * X_compare + 0.8 + 0.2 * np.random.randn(1000)
```

**Tasks:**
1. Implement all three gradient descent variants
2. Run each method for the same number of iterations
3. Plot convergence curves on the same graph
4. Measure computational time for each method
5. Analyze which method converges fastest and most accurately

---

**Key Questions:**

1. How does the gradient descent minimizes the cost function?
?
- Gradient descent minimizes a cost function by iteratively moving in the direction opposite to the gradient (slope). Since the gradient points to the direction of steepest ascent, moving in the opposite direction leads toward the minimum.
<!--SR:!2026-01-09,4,270-->

2. What are the three main variants of gradient descent and their key characteristics?
?
- **Batch GD**: Uses entire dataset, stable but slow per iteration, memory intensive
- **Stochastic GD**: Uses one example at a time, fast but noisy convergence, memory efficient
- **Mini-Batch GD**: Uses small subset of data, balanced approach, most practical for real applications
<!--SR:!2026-01-09,4,270-->

3. Why is mini-batch gradient descent preferred in practice?
?
- It combines the stability of batch gradient descent with the speed of stochastic gradient descent. It's vectorizable, tunable, and provides a good balance between convergence stability and computational efficiency.
<!--SR:!2026-01-09,4,270-->

4. What role does the learning rate play in gradient descent?
?
- The learning rate (α) controls the step size in each parameter update. Too large values can cause overshooting and divergence, while too small values lead to slow convergence. It's a critical hyperparameter that often needs tuning or scheduling.
<!--SR:!2026-01-09,4,270-->

5. How does stochastic gradient descent help escape local minima?
?
- The noise introduced by using single examples creates randomness in the gradient estimates, which can help the algorithm escape shallow local minima and potentially find better solutions, though it also makes convergence less stable.
<!--SR:!2026-01-09,4,270-->
