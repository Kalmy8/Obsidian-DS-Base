is a common machine-learning technique used to decrease model's variance

## Problem statement
Let's state a linear regression problem as:
$$\large y_i = \sum_{j=0}^m w_j X_{ij} + \epsilon_i$$
For this problem, according to the Gauss-Markov theorem, if:
- expectation of all random errors is zero: $E[\epsilon_{i}] = 0,$
- all random errors have the same finite variance, this property is called [homoscedasticity] $Var(\epsilon_{i}) = \sigma^{2} < \inf,$
- random errors are uncorrelated: $\forall i \neq j: \text{Cov}\left(\epsilon_i, \epsilon_j\right) = 0$
then the **Ordinary Least Squares** (OLS) method outputs the optimal unbiased linear estimation with lowest variance possible.

The OLS method suggest you to minimize the mean squared error stated like:
$$\large \mathcal{L}(\mathbf{X}, \mathbf{y}, \mathbf{w}) = \frac{1}{2n} \sum_{i=1}^n \left( y_i - \sum_{j=1}^p X_{ij} w_j \right)^{2},$$
where:
- n is the number of samples.
- p is the number of features.

Analytical solution for OLS is well-known:
$$\large w=(X^{T}X)^{-1}X^{T}y$$

However, all of the model's features have a perfect linear dependency over each other, the $\large X^{T}X$ matrix will be a singular one, meaning that it has a zero determinant.

Zero determinant makes the inverse operation ($(X^{T}X)^{-1}$) impossible because of the zero division: $A^{-1}=\frac{adj(A)}{det(A)}$.

In real-world scenarios, a perfect dependency, is, of course, not possible. However, having a lot of highly correlated features do result into small, close to zero determinant, which leads to dividing on a very small number while inversing the matrix. 
**This makes the OLS solution highly unstable** (the model has high variance), and **the coefficients** of the output estimator **do lose their interpretability**.

### Example of multicollinearity 
*w_true[1]*,*w_true[2]* are the weights assigned to the almost linear-dependent features, and the sum of the weights is somewhere near *-1.64*. 

We could use analytic solution to find optimal weights for this problem:
![Pasted image 20241126112637.png](📁%20files/Pasted%20image%2020241126112637.png)
... and we end up with weights equal to *-186*, *+184*. Note, that their sum is somewhat near *-1.64*

On practice, if you were to repeatedly re-calculate the solution again, you would get all the possible combinations of weights like *-1002/+1000* or *-152/+150* and so on. 

The weights could be enormous, but they do balance each other to somewhat like *-1.64* for your training set. **Whenever you will have to make predictions on new, unseen data, this enormous weights will lead you to very poor results, if distribution of these correlated features will change slightly from you training set**.

## Solution: Regularization!
Regularization technique suggest modifying the problem itself by changing the OLS cost function this way:
$$\large \mathcal{L}(\mathbf{X}, \mathbf{y}, \mathbf{w}) = \frac{1}{2n} \sum_{i=1}^n \left( y_si - \sum_{j=1}^p X_{ij} w_j \right)^2 + \lambda \sum_{j=1}^p w_{j}^{2},$$
where
-  $\lambda$ is the regularization coefficient.

This leads to a different analytical solution:
$$\large w=(X^{T}X+\lambda I)^{-1}X^{T}y,$$
where
- $I$ is a diagonal matrix of ones.

As you can see now, **we have introduced some bias to our model (as we now are solving a different problem)**, so our solution won't be no more optimal according to the Gauss-Markov theorem. What do we get instead?

Adding the regularization term breaks the linear dependency between original $X$ matrix rows and columns:
![Pasted image 20241126121100.png](📁%20files/Pasted%20image%2020241126121100.png)

This means that the determinant of the matrix will take greater distance from zero, and that means that our inverse operation won't explode model's weights anymore, providing a more stable, low-variance solution.

Thus, **Adjusting the regularization coefficient $\lambda$ allows as to balance between the bias and the variance of our model:**
- Higher $\lambda$ leads to higher bias, lower variance
- Lower $\lambda$ leads to lower bias, higher variance 

Another plus of the regularization is the **enforced interpretability**:
as we penalize the model increasing the weights, now only really significant/strong features which do really decrease the error could get relatively big weights. 

This property also allows us to refer to a regularization as to a **feature-selection technique**, which can be useful not to only fight the multicollinearity problem.

## $L^{1}$ and $L^{2}$ regularization
The $\large \lambda \sum_{j=1}^p w_{j}^{2}$ term we have introduced to the OLS loss function is called the $\large L^{2}$ regularization, meaning that we penalize the model for the squared values of the weights 

However, that's not the only option. In reality, the other terms is often used, the so-called $\large L^{1}$ regularization:
$$\lambda \sum_{j=1}^p |w_{j}|$$

Here we do penalize the model for the absolute values of the weights.

This little trick allows the model to perform the feature selection task even better, by **assigning the exact 0 value as a weight for unhelpful features**.

This might be counter-intuitive, but we have a simple explanation for that:

Let's assume that you are using the Gradient Descent algorithm for learning the best parameters for your model, and you managed to make it near global loss function minimum.

Your loss function can be divided into 2 simpler functions: the first part is responsible for tuning the parameters for the greater predictions, and the second part is responsible for not letting the weights to increase too much. This 2 functions are fighting against each other, one is trying to pick the weights, and the other one is trying to set them all the way down to zero.

The training process stops when you end up in some balance point in between. The derivative for the first function is, and the derivative of the second is just +1/-1 or zero.



#🃏/data-science 
## Key questions
