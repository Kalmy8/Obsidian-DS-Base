##### Bias-variance decomposition

^2b2fb4

A prediction task in ML can be stated as follows:
$$Y = f(x) + \epsilon,$$
where $Y$ is a target variable,
$f(x)$ is the function we search for: it maps an independent variable $x$ to the target variable $Y$,
$\epsilon$ is the noise term with zero [mathematical expectation](mathematical%20expectation.md) and constant [variance](variance.md). It means that finding the perfect $f(x)$ is not always possible. 

Since we do not have an access to whole data in the entire world, we do sample some portion of it and call it a **dataset**. Let's denote our trained model (the function) as  $\hat{f}()^D$. Then the inference of our model on some data can be denoted as $\hat{f}(x)^D$.

Let's define the **mean error of the model on the dataset D** as follows:
$$E_x[(\hat{f}(x)^{D} - Y)^2],$$
where $\hat{f}(x)^{D}$ is our prediction made with model  trained on dataset D;
$Y$ is the target variable.
The square operation is needed so errors in positive and negative directions would not compensate each other.

To define the **mean error of the model in general** we also need to account that our datasets might be a little different, so we should compute the mean error across all different datasets possible. This results into following:
$$E_D[E_x[(\hat{f}(x)^{D} - Y)^2]]$$

Now let's apply some math to simplify this equation...
>[!Math proof]-
>Change Y inplace :
>$$E_D[E_x[(\hat{f}(x)^{D} - f(x) - \epsilon)^{2}]$$
> For now only take the inner term, break the square:
> $$E_x[(\hat{f}(x)^{D} - f(x))^{2} - 2(\hat{f}(x)^{D} - f(x)) \epsilon +\epsilon^{2}]$$
> Using [linearity of the mathematical expectation](mathematical%20expectation.md):
> $$E_x[(\hat{f}(x)^{D} - f(x))^{2}] - 2E_x[(\hat{f}(x)^{D} - f(x)]E_x[ \epsilon] +E_x[\epsilon^{2}]$$
> Since $E_x[\epsilon]=0$ and  $Var(\epsilon) = E_x[\epsilon^{2}]-E_x[\epsilon]^{2} = E_x[\epsilon^{2}]$:
> $$E_x[(\hat{f}(x)^{D} - f(x))^{2}]+ Var(\epsilon)$$
> Let's not forget the main equation:
> $$E_D[E_x[(\hat{f}(x)^{D} - f(x))^{2}]+ Var(\epsilon)]$$
> Apply the linearity here + the fact that $Var(\epsilon)$ is independent of $D$, so applying $E_D$ for it changes nothing:
> $$E_D[E_x[(\hat{f}(x)^{D} - f(x))^{2}]]+ Var(\epsilon)$$
> Swap the $E_D$ and $E_x$ operations due to the [Law of total expectation](mathematical%20expectation.md):
> $$E_x[E_D[(\hat{f}(x)^{D} - f(x))^{2}]]+ Var(\epsilon)$$
> Introduce $\bar{\hat{f}}(x) = E_D[f(x)^D]$. It stands for a "perfect" (trained on all possible datasets/world data) model prediction. Explore the inner term:
> $$E_D[(\hat{f}(x)^{D} - \bar{\hat{f}}(x) + \bar{\hat{f}}(x) - f(x))^{2}]$$
> Breaking the square once again:
> $$E_D[(\hat{f}(x)^{D} - \bar{\hat{f}}(x))^{2}] - 2\underbrace{E_D[(\hat{f}(x)^{D} - \bar{\hat{f}}(x)]}_{0, since\ \bar{\hat{f}}(x) = E_D[f(x)^D]}E_D[(\bar{\hat{f}}(x) - f(x))]+ E_D[(\bar{\hat{f}}(x) - f(x))^{2}]$$
>  $$E_D[(\hat{f}(x)^{D} - \bar{\hat{f}}(x))^{2}] + E_D[(\bar{\hat{f}}(x) - f(x))^{2}]$$
>  In the second term, everything is independent of $D$, so applying $E_D$ takes no effect:
>  $$\underbrace{E_D[(\hat{f}(x)^{D} - \bar{\hat{f}}(x))^{2}]}_{Variance} + \underbrace{(\bar{\hat{f}}(x) - f(x))^{2}}_{Bias^2}$$
 
  Resulting equation:
  $$\text{Error} = E_X[\underbrace{E_D[(\hat{f}(x)^{D} - \bar{\hat{f}}(x))^{2}]}_{Variance}] + E_x[\underbrace{(\bar{\hat{f}}(x) - f(x))^{2}}_{Bias^{2}}]+\underbrace{\sigma^2}_{Irreducable\  error}$$  
  
> Note: we have given the mathematical proof for the **MSE** error function, but the concept of bias-variance decomposition goes beyond just MSE and can be applied practically to every model.

##### Bias-variance intuition
Bias-variance equation shows that our model's **mean error** can be decomposed into 3 main parts:
- Irreducable error, which is the variance of the white noise in real-world data
- Bias error, which can be defined as our perfectly trained model error over the real target variable value
- Variance error, which can be defined as our model's **sensitivity** to the data - pertubarations across different datasets. 

**High bias means our model, even if being trained ideally, fails to correctly catch the relationships between an independent and the target variable.** This typically shows that **our model is just not complex enough** (like when a linear model is used to catch non-linear relationships), and such situation is called **overfitting**

**High variance** means that our model is too sensitive to the pertubarations in our training data (in how we choose the $D$ dataset). This typically shows that **our model relies too much on the specific of the original training dataset**, and such situation is called **underfitting**

##### Bias-variance tradeoff
![Pasted image 20241111113132.png](Pasted%20image%2020241111113132.png)
While bias and variance do not directly depend on each other in theory, in practice they do often form an inverse relationship.

You see: high bias usually means that the [model complexity](../model%20complexity.md) is too low, and the model fails to catch the relationships in data properly. You do increase the complexity (by making a [polynomial regression](../polynomial%20regression.md) instead of a [linear](../linear%20regression.md) one), and the bias reduces.

However, your model can now be too complex, which allows it to successfully catch all the relationships inside the training dataset, but now it fails to extract some general meaning from the training data, it just "memorizes" all the correct answers. 

This how dealing with high bias resulted into high variance: the model now will make poor predictions on new, unseen dataset.

**Your main goal as an engineer is to find the optimum point**, where the model won't be complex enough to get overfitted on one hand, and won't be to simple to get underfitted on the other.

In order to do that, you often have to choose the model which will be complex enough, and apply some [variance-reducing techniques](../variance-reducing%20techniques.md).
If you actually struggle to pick a model which could handle complex relationships within your data, you can instead apply some of the [bias-reducing techniques](../bias-reducing%20techniques.md)

#🃏/data-science 
## Review questions

What is the bias and the variance? Take a Mean Squared Error (MSE) metric and break it down to the bias-variance decomposition formula. For each term in the resulting equation, provide an intuition
?
>$$E_D[E_x[(\hat{f}(x)^{D} - Y)^2]]$$
$$E_D[E_x[(\hat{f}(x)^{D} - f(x) - \epsilon)^{2}]$$
> For now only take the inner term, break the square:
$$E_x[(\hat{f}(x)^{D} - f(x))^{2} - 2(\hat{f}(x)^{D} - f(x)) \epsilon +\epsilon^{2}]$$
> Using [linearity of the mathematical expectation](mathematical%20expectation.md):
$$E_x[(\hat{f}(x)^{D} - f(x))^{2}] - 2E_x[(\hat{f}(x)^{D} - f(x)]E_x[ \epsilon] +E_x[\epsilon^{2}]$$
> Since $E_x[\epsilon]=0$ and  $Var(\epsilon) = E_x[\epsilon^{2}]-E_x[\epsilon]^{2} = E_x[\epsilon^{2}]$:
 $$E_x[(\hat{f}(x)^{D} - f(x))^{2}]+ Var(\epsilon)$$
> Let's not forget the main equation:
 $$E_D[E_x[(\hat{f}(x)^{D} - f(x))^{2}]+ Var(\epsilon)]$$
> Apply the linearity here + the fact that $Var(\epsilon)$ is independent of $D$, so applying $E_D$ for it changes nothing:
$$E_D[E_x[(\hat{f}(x)^{D} - f(x))^{2}]]+ Var(\epsilon)$$
> Swap the $E_D$ and $E_x$ operations due to the [Law of total expectation](mathematical%20expectation.md):
 $$E_x[E_D[(\hat{f}(x)^{D} - f(x))^{2}]]+ Var(\epsilon)$$
> Introduce $\bar{\hat{f}}(x) = E_D[f(x)^D]$. It stands for a "perfect" (trained on all possible datasets/world data) model prediction. Explore the inner term:
$$E_D[(\hat{f}(x)^{D} - \bar{\hat{f}}(x) + \bar{\hat{f}}(x) - f(x))^{2}]$$
> Breaking the square once again:
$$E_D[(\hat{f}(x)^{D} - \bar{\hat{f}}(x))^{2}] - 2\underbrace{E_D[(\hat{f}(x)^{D} - \bar{\hat{f}}(x)]}_{0, since\ \bar{\hat{f}}(x) = E_D[f(x)^D]}E_D[(\bar{\hat{f}}(x) - f(x))]+ E_D[(\bar{\hat{f}}(x) - f(x))^{2}]$$
$$E_D[(\hat{f}(x)^{D} - \bar{\hat{f}}(x))^{2}] + E_D[(\bar{\hat{f}}(x) - f(x))^{2}]$$
>  In the second term, everything is independent of $D$, so applying $E_D$ takes no effect:
$$\underbrace{E_D[(\hat{f}(x)^{D} - \bar{\hat{f}}(x))^{2}]}_{Variance} + \underbrace{(\bar{\hat{f}}(x) - f(x))^{2}}_{Bias^2}$$
>Resulting equation:
$$\text{Error} = E_X[\underbrace{E_D[(\hat{f}(x)^{D} - \bar{\hat{f}}(x))^{2}]}_{Variance}] + E_x[\underbrace{(\bar{\hat{f}}(x) - f(x))^{2}}_{Bias^{2}}]+\underbrace{\sigma^2}_{Irreducable\  error}$$
<!--SR:!2025-07-19,161,310-->


What is the bias-variance tradeoff, why does it occur? How is it bonded with definitions of overfitting and underfitting?
?
- Bias and variance tradeoff is a common problem when bias and variance error components form an inverse relationship between each other: decreasing one error component results into increasing the other one
- Overfitting is a state when the bias term is relatively small, but the variance term is high, meaning that the model relies too much on the exact training data distributions and observations, making it less valid for further predictions ^4e8203
- Underfitting is a state when the bias term is relatively high, and the variance term is low. This usually means that your model isn't complex enough to extract meaningful dependencies from the training data (like when applying linear regression to describe non-linear dependency).
<!--SR:!2025-08-09,167,310-->

What are the "strong" and "weak" learners? How to pick an optimal ML model for your task in terms of bias-variance balance?
?
- Strong learners are complex models, which are powerful in capturing dependencies between variables inside the training data. Weak learners are more simple models, which do not dig so deep down into the training data so can miss some dependencies.
- Model must be strong enough to capture dependencies from the training data, so the bias term would not go high. On the other hand, it must be somewhat restricted to not rely on the training data too much, so it could extract some general meaning and apply it further.
<!--SR:!2025-08-13,171,310-->
