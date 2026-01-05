---
type: note
status: done
tags: []
sources:
-
authors:
-
---

is an ensembling ML method, which targets to reduce total error bias component.

the main idea of boosting: instead of training one estimator, we could train several, such that each next estimator would compensate the error of the previous one. 

## Intuitive description
1. Define the error metric $$L(y,x) = \frac{1}{2}\sum\limits_{i-1}^{N}(y_{i} - a(x_{i}))^{2} \to min $$
2. Define an ensemble as the composition of several estimators: 
 $$a(x) = a_{K}(x) = b_1(x)+b_2(x)+..+b_K(x)$$
3. Define the first basic estimator (let it be from the tree family $\mathcal{B}$)
 $$\large b_1(x) =\arg\min_{b \in \mathcal{B}} \mathcal{L}(y, b(x))$$
4. Calculate the error between basic estimator prediction and the actual value:
 $$\large s_{i}^{1}=y_{i}-b_{1}(x_{i})$$
5. Define the second estimator to compensate the error:
 $$\large b_2(x) =\arg\min_{b \in \mathcal{B}} \mathcal{L}(s^{1}, b(x))$$
6. Update the composition:
 $$a_{2}(x)=a_{1}(x)+b_{2}(x)$$
7. Loop the process:
	1. Calculate error on step *k*:
	 $$s_{i}^{k-1}=y_{i}-a_{k-1}(x_{i})$$
	2. Train the estimator $b_{k}$ to predict that error:
	 $$b_k(x) =\arg\min_{b \in \mathcal{B}} \mathcal{L}(s^{k-1}, b(x))$$
	3. Update the composition:
	 $$a_{k}(x)=a_{k-1}(x)+b_{k}(x)$$

## Learning process
More formally, this algorithm can be described as follows:

Let $\mathcal{L}$ – be the derivable loss function, and our complex estimator $a(x)$ is stated as:
$$\large a(x)=a_{k}(x)=b_{1}(x)+..+b_{k}(x)$$

Each next estimator is got from the previous one:
$$\large a_{k}(x)=a_{k-1}(x)+b_{k}$$

Newly added $b_{k}$ is trained in such way that:
 $$\large b_k(x) =\arg\min_{b \in \mathcal{B}}\sum\limits_{i=1}^{N} \mathcal{L}(y_{i}, a_{k-1}(x)+b(x_{i}))$$
 
The origin $b_{0}$ is trained to minimize the error on the train set:
 $$\large b_0(x) =\arg\min_{b \in \mathcal{B}}\sum\limits_{i=1}^{N} \mathcal{L}(y_{i}, b(x_{i}))$$
In order to train $b_{k}$, let's break the loss function into the Taylor series and take the first term:
$$\large \mathcal{L}(y_i, a_{k-1}(x_i) + b(x_i)) \approx \mathcal{L}(y_i, a_{k-1}(x_i)) 
+ b(x_i) \frac{\partial \mathcal{L}(y_i, z)}{\partial z} \bigg|_{z = a_{k-1}(x_i)}$$

For the sake of simplicity, let's denote the partial derivative $\large \frac{\partial \mathcal{L}(y_i, z)}{\partial z} \bigg|_{z = a_{k-1}(x_i)} = g_{i}^{k-1}$

Thus the equation for $b_{k}$ can be simplified to 
 $$\large b_k(x) \approx \arg\min_{b \in \mathcal{B}}\sum\limits_{i=1}^{N} b(x_i) g_{i}^{k-1}$$

We can notice, that the resulting summation expression on the right is equal to the dot product of vectors: 
 $$\large b_k(x) \approx \arg\min_{b \in \mathcal{B}} B(X) \cdot G^{k-1}$$

In order to minimize the dot product, we should set $$\large B(X) = -kG^{k-1}$$

In other words, on each step, newly added estimator $B$ is trained to predict the **antigradient of the loss function at the point $\large x_{i}$**.

## Scoring functions
In order to train $\large b_{k}$ such that it would predict the antigradient of the loss function, we should solve the regression problem:
$$\large g_{i}^{k-1} = b_{k}(x_{i}), \text{or vectorized:}$$
$$\large G^{k-1} = B_{k}(X)$$

## Learning rate
In practice, estimators predicting the antigradient itself do often result into overfitting and can spoil the algorithm convergency. It's a well-known problem of the gradient descent algorithm, and it can be solved by introducing **the learning rate coefficient**.

With learning rate, the ensemble model will look like follows:
$$\large a_{k+1}(x)=a_{k}(x)+ \eta b_{k+1}(x),$$
were $\eta \in (0,1]$.

