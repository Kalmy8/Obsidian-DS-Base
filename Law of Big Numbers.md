---
type: note
status: done
tags: []
sources:
-
authors:
-
---
guarantees that **as your sample size increases**, empirical deviations from the true population distribution become statistically negligible. Specifically:

#### Weak Law of Large Numbers
For i.i.d. random variables $X_1, X_2, ..., X_n$ with finite expectation $\mu$ :

$$
\lim_{n \to \infty} P\left(\left|\frac{1}{n}\sum_{i=1}^n X_i - \mu\right| \geq \varepsilon \right) = 0 \quad \text{for any } \varepsilon > 0
$$

*Interpretation*: The sample mean converges in probability to the population mean.

#### Strong Law of Large Numbers
Strengthens this to almost sure convergence:

$$
P\left(\lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^n X_i = \mu \right) = 1
$$

#### Statistics beyound mean

### Convergence Rates
1. **[[mathematical expectation]] (1st Moment)** 
2. **[[variance]] (2nd Moment)** 
3. **[[skewness]] (3rd Moment)** 
4. **[[kurtosis]] (4th Moment)** 

### Intuition

Higher moments **amplify outliers**, making them noisier and slower to stabilize.

### Empirical Example
For a standard normal distribution ($\mu = 0$, $\sigma^2 = 1$, skewness = 0, kurtosis = 3):

| Statistic | True Value | Sample Size for ±5% Error |
|-------------|------------|---------------------------|
| Mean | 0 | ~100 |
| Variance | 1 | ~1,000 |
| Skewness | 0 | ~10,000 |
| Kurtosis | 3 | ~100,000 |

### Practical Implications for ML/Statistics
1. **Dataset Size Matters** Small samples ($n < 30$) may show significant deviations from population parameters. LLN explains why:
	 - Training/validation splits should be large enough
	 - Bootstrapping works better with larger $n$

2. **Validation of i.i.d. Assumption** If your data violates i.i.d. (e.g., time-series dependencies), LLN conclusions become unreliable.

Absolutely! Let me break it down step by step:

---

### **What Are Error Bars?**
Error bars are graphical representations of the variability or uncertainty in data. They often show:
- **Standard Error (SE)**: How much the sample mean might fluctuate around the true population mean.
- **Confidence Intervals (CI)**: A range where the true mean is likely to lie.

---

### **Standard Error Formula**
The standard error of the mean (SEM) is calculated as:
\[
\text{SEM} = \frac{\sigma}{\sqrt{n}}
\]
- \( \sigma \): Population standard deviation (spread of the data)
- \( n \): Sample size (number of observations)

---

### **Why Does SEM Shrink as \( n \) Grows?**
1. **Intuition**: 
 - Larger samples (\( n \)) provide more information about the population. 
 - More data points reduce the uncertainty in estimating the true mean.

2. **Mathematically**: 
 - The denominator \( \sqrt{n} \) grows as \( n \) increases. 
 - For example: 
 - If \( n = 100 \), \( \sqrt{n} = 10 \), so SEM = \( \sigma / 10 \). 
 - If \( n = 10,000 \), \( \sqrt{n} = 100 \), so SEM = \( \sigma / 100 \). 

3. **Visualization**: 
 ![Standard Error vs Sample Size](https://www.statisticshowto.com/wp-content/uploads/2016/01/standard-error-formula.png) 
 - As \( n \) increases, the SEM curve flattens, showing diminishing returns.

---

### **Practical Implications**
1. **Tighter Error Bars**: 
 - Smaller SEM → narrower confidence intervals → more precise estimates.

2. **Sample Size Planning**: 
 - To halve SEM, you need to quadruple \( n \) (since \( \sqrt{4n} = 2\sqrt{n} \)).

3. **Statistical Significance**: 
 - Larger \( n \) makes it easier to detect small effects (e.g., in A/B testing).

---

### **Example**
Suppose \( \sigma = 10 \):

| Sample Size (\( n \)) | SEM (\( \sigma / \sqrt{n} \)) | Error Bar Width (95% CI ≈ 2×SEM) |
|-----------------------|-------------------------------|-----------------------------------|
| 100 | \( 10 / 10 = 1 \) | ±2 |
| 400 | \( 10 / 20 = 0.5 \) | ±1 |
| 10,000 | \( 10 / 100 = 0.1 \) | ±0.2 |

---

### **Key Takeaway**
- **Error bars tighten as \( n \) grows** because SEM shrinks. 
- This reflects increasing confidence in the sample mean as a reliable estimate of the population mean. 

Does this clarify the connection between sample size, standard error, and error bars?

4. **Cross-Validation Stability** 
 Multiple train/test splits yield similar metrics _if_ LLN conditions hold.
 
2. **A/B Testing** 
 Required sample sizes are calculated using LLN principles to ensure detected differences are real.