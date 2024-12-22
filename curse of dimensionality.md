#🃏/data-science #🌱 
#####  Definition
By definition, the **curse of dimensionality** describes a problem when **the amount of data (observations) required to extract some meaningful knowledge increases exponentially while new features (dimensions) occur**.

Let's provide a simple example:
You are trying to predict some target based on **two features: gender and height**. In order to extract some **general predictive power (not to be overfitted)**, your algorithm should ideally explore all possible combinations of gender and height (which is not really possible since height is a [[continuous variable]]) Less ideally, it should at least observe most part of the combinations, **representing the full range of variance of your variables**. It looks like parsing a 2d grid.

Now imagine that you have added just one more feature to your dataset: the age group. As well as in the previous example, **your data should then cover all possible combinations of 3 variables**, which now feels like parsing a cube, not a 2d grid. So, adding only one feature results into a vast increase of the parameter combinations. 

Let's visualize this phenomena, assuming we only have binary features and we need only 10 observations for our ML algorithm to crack the feature's effect on the target variable.
![[Pasted image 20241108182410.png]]
Looking on such illustration, one would say that **the amount of required data will grow up exponentially as new dimensions are added**.

Adding more features means even more data is required for machine learning, so eventually several problems will occur:

##### 1. Empty space problem
 This problems refers to the situation when your data can no more cover all possible N-dimensional features space that you have created, so any ML algorithm you choose won't be able to discover true relationships between your variables and will only learn some frequent combinations inside your data, so it **will be overfitted on your exact features distributions**. 

#####  2. Non-meaningful distances problem
As new dimensions are added, the data becomes more sparse and the distances between data points will increase:
- Imagine you only have one feature with every observations laying within the [0,1] range. Maximum distance between 2 observations would be 1
- Now imagine you have 2 features, so the hyperspace is the 1x1 square. Maximum distance between 2 observations would be $\sqrt{2}$
- With 3 features, maximum distance would be $\sqrt{3}$, in general, with *n* features, the distance would become $\sqrt{n}$

So, we could say that more dimensions means more distance between our data points. But, as we have mentioned, we could not cover all the high-dimensional space with data, so, practically **the maximum distance often increases slower, then the minimum distance**. This can be illustrated, if we create a lot of multivariate observations with consisting of uniformally-distributed features:
![[Pasted image 20241108183934.png]]

As you can see, in high-dimensional spaces the **difference between the closest neighbour and the farthest one diminishes, observations become roughly equidistant**, so all of them are now far away from each other, and most part of the distance metrics will make no more sense

###### N-ball explanation
The unintuitive behavior stated in the previous section can be explained with an N-ball math object.

The n-ball of radius $R$ is the collection of points at a distance at most R from the center of the space 0. 
In 1d it's a section, 
In 2d it's a circle, 
In 3d it's a sphere. 

Now let's say that the points reachable with half of the radius $R/2$ from the center will form **the inner part** of the n-ball, and the other point will form **the outer part**. 

As you can imagine, the outer part should cover more volume in space, but what's the concrete  $\frac{V_{inner}}{V_{total}}$ ratio?


![[Pasted image 20241108192451.png | 300]]
For the 1D n-ball, it's 0.5, we can clearly see that from the figure above.

![[Pasted image 20241108192550.png | 300]]
For the 2D n-ball, it's 0.25, which also makes sense

![[Pasted image 20241108192658.png | 600]]
For the 3D n-ball, it's only about 0.125

For 10D (which can not be drawn really), the calculated ratio is about 0.001

So every new dimension multiplies the ratio by $1/2$. meaning that in **high-dimensional spaces most part of the n-ball volume will be concentrated closer to the shell**. 
Now imagine that the center of the n-ball is one of your data points, and you are willing to calculate the closest and the farthest neighbour distances inside the $R$ radius. **Even in 10D space 99.9% of your data will be concentrated close to the n-ball surface, so they all will be the equidistantly far**.

##### Positive effects
As we can see now, euclidian-distance-based algorithms will probably fail to learn any general knowledge from your high-dimensional data. Despite that, there are some cons within high-dimeshional spaces:
1. Datapoints often become linear-separably. [[Support Vector Machines (SVM)]] utilize this phenomena by using kernel-trick. 
2. Neural Networks do not rely on distance between the points at all, dealing very well with highly-dimensional data, extracting relationships between all the features and the target variable

#### Key questions:

