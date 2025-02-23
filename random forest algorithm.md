is the bagged version of the [decision tree algorithm](decision%20tree%20algorithm.md). Speaking more precisely, random forest algorithm, in contrast with just bagging over trees, **assumes that you are using only a subset of features** to train each tree in the ensemble

In accordance to the original paper by *Leo Breiman*, "Random Forests" (Machine Learning, 45, 5-32, 2001), the overall random forest ensemble variance can be described as:
$$\large Varf(x) = \rho(x)\sigma^2(x)$$
$$\large \rho(x) = Corr\left[T(x_1,\Theta_1(Z)),T(x_2,\Theta_2(Z))\right],$$
where
- $ρ(x)$ is the **correlation between the predictions of these two randomly generated trees** on a specific input x. It captures the correlation introduced by the randomness in the tree-building process itself, not just the correlation between the trees in a single realized forest.
- $\Theta_{1}(Z)$ and $\Theta_{2}(Z)$ are a randomly selected pair of trees on randomly selected elements of the sample $Z$;
- $T(x,\Theta_{i}(Z))$ is the output of the i-th tree classifier on an input vector x;
- $\sigma^{2}(x)$ is the sample variance of any randomly selected tree $$\large \sigma^2(x) = Var\left[T(x,\Theta(X))\right]$$

$ρ(x)$ is a *theoretical correlation*. It's not calculated from the trees in a single, already-trained random forest. Instead, it represents the expected **correlation between any two trees (= between their predictions)** if you were to repeatedly:
- Sample a new training dataset from the overall population
- Train a pair of random trees on this new dataset (using bootstrapping and random feature selection).





### Most important hyperparameters:
#### Depth
Since bagging technique does target model's variance to be reduced, we still need somewhat complex models to lower the bias. So it is recommended to build depth trees with no pruning at all, since we have overfitting problem covered up with bagging.  

#### Number of estimators
In theory, when estimators are independent and uncorrelated, we can **reduce variance by $k$ times where $k$ is the number of estimators**. In reality, true independency is unachievable, so from some point adding new estimators do increase computational expenses and training time, but does not result into any performance boost. 

So we should find some optimal number of estimators, probably by plotting the relationship between some metric and the number of estimators.

#### Number of features
Insights from the original works on Random Forests by *Leo Breiman* and subsequent research. 

- For classification problems, it's advised to take $m = \sqrt{n}$ features, where $n$ denotes the quantity of features within the dataset.
	- The resulting $m$ is big enough to build meaningful predictors, and small enough for trees to be somewhat independent
- For regression problems, the recommendation will be $m = \frac{n}{3}$
	- $\frac{n}{3} is larger than \sqrt{n}$, and that's because regression trees usually do need more features to capture target variable due to it's continuous origin

Selecting proper $m$ value is crucial for overall ensemble performance, because with larger $m$ most part of the trees are being trained on the same features thus being correlated thus result into greater variance. As $m$ approaches $n$, the resulting benefit in variance will vanish.
![Pasted image 20241120105356.png](Pasted%20image%2020241120105356.png)

#### Number of samples in leaf
Insights from the original works on Random Forests by *Leo Breiman* and subsequent research. 

- It is recommended to build each tree until all of its leaves contain only $n_{min}=1$ examples for classification
	- This way, we do fully-grown trees with no pruning at all, because we can be sure that bagging will take care of overfitting, and we are interested to lower the bias as much as we can
- For regression problems, the recommendation will be and $n_{min}=5$ examples.
	- Due to the continuous nature of the target variable, predicting every and each value will include too much noise into our data, so we use a larger value to smooth the predictions a little (you can think of it as of binning the target feature).

#🃏/probability-theory 
## Key questions

How is random forest different from just bagging over the decision trees? What is the additional parameter and what is it's purpose? How should you tune this parameter?
?
- Random forest suggest you to use $m =$ *number of features* parameter, which is different from the simple bagging, where all the available features are used for training all the trees.
- This helps trees in the forest to be uncorrelated with each other, by not only training them on different bootstrap samples, but also on different features.
- For regression problems, starting from $m = \frac{1}{3}$ is optimal, because regression tasks are generally harder and require more data to be solved with low bias.
- For classification problems, starting point is $m = \sqrt{\text{Total number of features}}$
<!--SR:!2025-03-09,14,290-->


How does the total random forest variance is related with the individual tree variance? Provide a math equation and an intuition
?
- $$\large Varf(x) = \rho(x)\sigma^2(x)$$
- $$\large \rho(x) = Corr\left[T(x_1,\Theta_1(Z)),T(x_2,\Theta_2(Z))\right],$$
where
- $ρ(x)$ is the theoretical correlation between the predictions of these two randomly generated trees on a specific input x. It captures the correlation introduced by the randomness in the tree-building process itself, not just the correlation between the trees in a single realized forest.
- $\Theta_{1}(Z)$ and $\Theta_{2}(Z)$ are a randomly selected pair of trees on randomly selected elements of the sample $Z$;
- $T(x,\Theta_{i}(Z))$ is the output of the i-th tree classifier on an input vector x;
- $\sigma^{2}(x)$ is the sample variance of any randomly selected tree $$\large \sigma^2(x) = Var\left[T(x,\Theta(X))\right]$$
- This formula clearly shows that the total variance term is proportional to both single tree variance and the correlation between two random trees from the forest. No matter how single tree variance is big, if correlation is close to zero the all-together error would also be.
<!--SR:!2025-03-11,16,290-->


How to tune tree *depth* and *min_samples_leaf* parameters for both classification and regression tasks?
?
- Depth parameter does usually stay unlimited, because tree's variance does not bother us too much when using bagging. So this way our trees will have the lowest bias possible
- Min_samples_leaf parameter is usually set to 1 for classification tasks, resulting into fully-grown tree, for the same purpose
- Min_samples_leaf parameter is usually set to 5-6 for regression tasks, because continuous data do always contain some noise, and we would like to sort of "bin" this data by increasing min_samples_leaf. This way, our tree won't remember each and every observation and won't be so overfitted.
<!--SR:!2025-03-10,15,290-->


