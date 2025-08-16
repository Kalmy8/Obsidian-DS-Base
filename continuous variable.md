 a variable which has **continuous distribution**, e.g. it can take arbitrary numeric values from some interval. Some common examples would be:
- Height (any number from 50cm to 220cm)
- Weight (any number from 40kg to 150kg)
- Salary 
- Distance
- Temperature
- ...
Some common-used visualization techniques for such variables would be: [histograms](histograms.md), [boxplots](boxplots.md), [scatterplots](scatterplots.md)

In practice, a continuous variable can be treated as a [discrete variable](discrete%20variable.md), if number of observations is small and the measurements are clearly separable from each other (imagine that the measurements were done with some inaccurate device, for example a thermometer which could only show you 0/10/20/30 degrees).

In such sense, **a continuous variable is more like a characteristic of your dataset** and not of the nature of the original variable.   

~Continuous variables can be truly transformed to discrete~ ones using the [binning technique](binning%20technique.md).