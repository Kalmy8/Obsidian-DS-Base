---
type: note
status: done
tags: ['tech/ml']
sources:
-
authors:
-
---
 
##### Definition
By definition, the **curse of dimensionality** describes a problem when **the amount of data (observations) required to extract some meaningful knowledge increases exponentially while new features (dimensions) occur**.

Let's provide a simple example:
You are trying to predict some target based on **two features: gender and height**. In order to extract some **general predictive power (not to be overfitted)**, your algorithm should ideally explore all possible combinations of gender and height (which is not really possible since height is a [continuous variable](continuous%20variable.md)) Less ideally, it should at least observe most part of the combinations, **representing the full range of variance of your variables**. It looks like parsing a 2d grid.

Now imagine that you have added just one more feature to your dataset: the age group. As well as in the previous example, **your data should then cover all possible combinations of 3 variables**, which now feels like parsing a cube, not a 2d grid. So, adding only one feature results into a vast increase of the parameter combinations. 

Let's visualize this phenomena, assuming we only have binary features and we need only 10 observations for our ML algorithm to crack the feature's effect on the target variable.
![Pasted image 20241108182410.png](Pasted%20image%2020241108182410.png)
Looking on such illustration, one would say that **the amount of required data will grow up exponentially as new dimensions are added**.

Adding more features means even more data is required for machine learning, so eventually several problems will occur:

##### 1. Empty space problem
 This problems refers to the situation when your data can no more cover all possible N-dimensional features space that you have created, so any ML algorithm you choose won't be able to discover true relationships between your variables and will only learn some frequent combinations inside your data, so it **will be overfitted on your exact subsample features distributions**. 

##### 2. Non-meaningful distances problem
As new dimensions are added, the data becomes more sparse and the distances between data points will increase:
- Imagine you only have one feature with every observations laying within the [0,1] range. Maximum distance between 2 observations would be 1
- Now imagine you have 2 features, so the hyperspace is the 1x1 square. Maximum distance between 2 observations would be $\sqrt{2}$
- With 3 features, maximum distance would be $\sqrt{3}$, in general, with *n* features, the distance would become $\sqrt{n}$

So, we could say that more dimensions means more distance between our data points. But, as we have mentioned, we could not cover all the high-dimensional space with data, so, practically **the maximum distance often increases slower, then the minimum distance**. This can be illustrated, if we create a lot of multivariate observations with consisting of uniformally-distributed features:
![Pasted image 20241108183934.png](Pasted%20image%2020241108183934.png)

As you can see, in high-dimensional spaces the **difference between the closest neighbour and the farthest one diminishes, observations become roughly equidistant**, so all of them are now far away from each other, and most part of the distance metrics will make no more sense

###### N-ball explanation
The unintuitive behavior stated in the previous section can be explained with an N-ball math object.

The n-ball of radius $R$ is the collection of points at a distance at most R from the center of the space 0. 
In 1d it's a section, 
In 2d it's a circle, 
In 3d it's a sphere. 

Now let's say that the points reachable with half of the radius $R/2$ from the center will form **the inner part** of the n-ball, and the other point will form **the outer part**. 

As you can imagine, the outer part should cover more volume in space, but what's the concrete $\frac{V_{inner}}{V_{total}}$ ratio?

![300](Pasted%20image%2020241108192451.png)
For the 1D n-ball, it's 0.5, we can clearly see that from the figure above.

![300](Pasted%20image%2020241108192550.png)
For the 2D n-ball, it's 0.25, which also makes sense

![600](Pasted%20image%2020241108192658.png)
For the 3D n-ball, it's only about 0.125

For 10D (which can not be drawn really), the calculated ratio is about 0.001

So every new dimension multiplies the ratio by $1/2$. meaning that in **high-dimensional spaces most part of the n-ball volume will be concentrated closer to the shell**. 
Now imagine that the center of the n-ball is one of your data points, and you are willing to calculate the closest and the farthest neighbour distances inside the $R$ radius. **Even in 10D space 99.9% of your data will be concentrated close to the n-ball surface, so they all will be the equidistantly far**.

##### Dealing with the curse

**Choose more robust algorithms:**

✅ **SVMs** (with kernels) and **Neural Networks** do handle high-D well, cause they do not rely on pure distances
✅ **Tree-based methods** will also do well thanks to the same reasons
❌ **Pure distance-based methods** (K-means, DBSCAN) will suffer the most

**Apply Dimensionality Reduction (PCA, t-SNE)**

**Consider spending more time doing a proper [[feature selection]]**

#🃏/semantic/ml #### Key questions:

What is the fundamental problem described by the curse of dimensionality? **Illustrate that problem:** assume you need 30 data observations for some binary classification problem with a single binary descriptive and a single binary target feature. How many data points will you require for 2 descriptive features? 3 features? How do continuous features affect this situation?
?
- The exponential increase in required data volume as features/dimensions are added, making ML models struggle to find meaningful patterns.
- 2 features do create 4 possible combinations (0/0; 0/1; 1/0; 1/1), 3 featured do create 8 ($2^3$) combinations, generally $k$ features create at least $2^{k}$ combinations
- Situation is getting worse with continuous features, as they do have much more than 2 possible values, so the data requirement grows more like $m^{k}$, where $m$ is an average amount of unique values contained by features
<!--SR:!2026-01-09,4,270-->

What is the **empty space problem**? Why it leads to overfitting?
?
- Empty space problem is a situation when your data covers is located very sparse in some areas of the N-dimensional space
- Models then have too little local evidence to extract any general knowledge so they start relying on common feature combinations / noise rather on learning general relationships (which leads to high variance)
<!--SR:!2026-01-09,4,270-->

How does maximum Euclidean distance change with added dimensions? What's the maximum euclidian distance for 1D and 10D spaces?
?
- It grows as $\sqrt{n}$ (for n features)
- $\sqrt{1} = 1$ and $\sqrt{10} = 3.16$
<!--SR:!2026-01-09,4,270-->

Why do distance metrics become unreliable in high dimensions?
?
- Minimum and maximum distances converge - all points become roughly equidistant, making nearest neighbor searches meaningless.
![Pasted image 20241108183934.png](📁%20files/Pasted%20image%2020241108183934.png)
<!--SR:!2026-01-09,4,270-->

What's the volume ratio formula for inner n-ball? What percentage of a 10D, 2D and 1D n-ball's volume lies in its outer shell?
?
- $(1/2)^{n}$ in $n$-dimentional space
- ~99.9% (only 0.1% in the inner sphere), compared to 50% in 1D and 25% in 2D.
- ![300](📁%20files/Pasted%20image%2020241108192550.png)
<!--SR:!2026-01-09,4,270-->

Which ML methods handle high dimensionality well? Why?
?
 - Methods which do not rely on distance metrics OR have strong regularization mechanism (to exclude non-informative features):
 - Linear models with Regularization
 - Tree Models
 - SVMs: Exploit linear separability in high-D spaces via kernel trick
 - Neural Networks: Learn feature interactions directly without distance metrics
<!--SR:!2026-01-09,4,270-->

