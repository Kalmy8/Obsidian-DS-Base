is an ensembling ML method, which targets to reduce total error variance component.

the main idea of bagging: instead of training one estimator, we could train several, using different subsamples of the training data, and then take the average prediction.

Subsamples are usually formed using the [bootstrap technique](bootstrap%20technique.md), 

let's take the standard [bias and variance](Теория%20вероятностей/bias%20and%20variance%20tradeoff.md#^2b2fb4) decomposition for the Mean Squared Error metric, and take a look how exactly bagging help to reduce variance.

First let us prove that the **ensembling does not affect the bias term:** 
![800](bias%20of%20bagging.md)
bias of a single estimator equals to bias of any basic model inside the ensemble

Now let's take a look at the variance term:
![800](variance%20of%20bagging.md)
As you can see, in ideal scenario, when ensemble models are independent, **transferring to composition versus the single estimator reduced the variance by k times**.

**In real applications, the complete independency is unachievable**, because bootstrapped subsamples will overlap with each other somehow, but you should get the main idea: **Both individual estimator variance and the covariance between base estimator predictions do increase total variance of the ensemble**

This core property of bagging defines the way it is most commonly used: **bagging allows you to take some [strong learner](model%20complexity.md), which usually do suffer from [overfitting](Теория%20вероятностей/bias%20and%20variance%20tradeoff.md#^4e8203), and reduce it's variance**, achieving both low bias (due to the model complexity) and low variance (due to the bagging) error terms.

Thus bagging is usually to used over [decision tree algorithm](decision%20tree%20algorithm.md), which, with some nuances, result into [random forest algorithm](random%20forest%20algorithm.md).

#🃏/data-science  
## Key questions:

What is the core idea of a bagging technique, how can it be described? What benefits does it provide?
?
- Bagging techniques includes changing from a single estimator to a set of estimators and averaging their predictions
- In an ideal scenario, when base estimators are independent from each other, **bagging decreases the variance term of the model by k times where k is the number of estimators**
<!--SR:!2025-02-19,62,310-->

How are ensemble variance and bias different from the single estimator variance and bias? Provide a mathematical formula
?
Bias is the same
![800](bias%20of%20bagging.md)
variance is decreased by \<number of base models> time, if base models are uncorrelated
![800](variance%20of%20bagging.md)
<!--SR:!2025-02-15,7,234-->