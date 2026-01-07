---
type: note
status: done
tags: [math/statistics, math/probability-theory]
sources:
  - "[[Statistics Basics Course]]"
authors:
  - 
---

## Lecture goal
- Build intuition for: **population → descriptive statistics → LLN → CLT → hypothesis testing ([[p-value]])**

>[!info]- Setup code snippet
>```python
># Setup (copy once per lecture)
>from __future__ import annotations
>
>from dataclasses import dataclass
>from typing import Callable, Literal
>
>import matplotlib.pyplot as plt
>import numpy as np
>import numpy.typing as npt
>import pandas as pd
>import seaborn as sns
>from scipy import stats
>
>RNG_SEED: int = 42
>rng: np.random.Generator = np.random.default_rng(RNG_SEED)
>
>sns.set_theme(context="talk", style="whitegrid")
>plt.rcParams["figure.figsize"] = (11, 5)
>plt.rcParams["figure.dpi"] = 120
>
>FloatArray = npt.NDArray[np.float64]
>
># Helper: population object (values + 4 descriptive stats)
>@dataclass(frozen=True)
>class Population:
>    name: str
>    values: FloatArray
>    mean: float
>    median: float
>    var: float
>    std: float
>    skew: float
>    kurtosis_excess: float
>
>    @classmethod
>    def from_values(cls, *, name: str, values: FloatArray) -> Population:
>        mean: float = float(np.mean(values))
>        median: float = float(np.median(values))
>        var: float = float(np.var(values, ddof=0))
>        std: float = float(np.std(values, ddof=0))
>        skew: float = float(stats.skew(values, bias=False))
>        kurtosis_excess: float = float(stats.kurtosis(values, fisher=True, bias=False))
>        return cls(
>            name=name,
>            values=values,
>            mean=mean,
>            median=median,
>            var=var,
>            std=std,
>            skew=skew,
>            kurtosis_excess=kurtosis_excess,
>        )
>
>    @classmethod
>    def exponential(cls, *, scale: float, n: int, rng: np.random.Generator) -> Population:
>        values: FloatArray = rng.exponential(scale=scale, size=n).astype(np.float64)
>        return cls.from_values(name=f"Exponential(scale={scale})", values=values)
>
>    @classmethod
>    def normal(cls, *, mu: float, sigma: float, n: int, rng: np.random.Generator) -> Population:
>        values: FloatArray = rng.normal(loc=mu, scale=sigma, size=n).astype(np.float64)
>        return cls.from_values(name=f"Normal(μ={mu}, σ={sigma})", values=values)
>
>    @classmethod
>    def uniform(cls, *, low: float, high: float, n: int, rng: np.random.Generator) -> Population:
>        values: FloatArray = rng.uniform(low=low, high=high, size=n).astype(np.float64)
>        return cls.from_values(name=f"Uniform(low={low}, high={high})", values=values)
>
>    @classmethod
>    def lognormal(cls, *, mu: float, sigma: float, n: int, rng: np.random.Generator, shift: float = 0.0) -> Population:
>        values: FloatArray = (rng.lognormal(mean=mu, sigma=sigma, size=n) + shift).astype(np.float64)
>        shift_label: str = f", shift={shift}" if shift != 0.0 else ""
>        return cls.from_values(name=f"LogNormal(μ={mu}, σ={sigma}{shift_label})", values=values)
>
>    @classmethod
>    def triangular(cls, *, low: float, mode: float, high: float, n: int, rng: np.random.Generator) -> Population:
>        values: FloatArray = rng.triangular(left=low, mode=mode, right=high, size=n).astype(np.float64)
>        return cls.from_values(name=f"Triangular(low={low}, mode={mode}, high={high})", values=values)
>
>    @classmethod
>    def beta_scaled(
>        cls,
>        *,
>        a: float,
>        b: float,
>        low: float,
>        high: float,
>        n: int,
>        rng: np.random.Generator,
>    ) -> Population:
>        # Beta lives on [0,1]; scale to [low, high]
>        unit: FloatArray = rng.beta(a=a, b=b, size=n).astype(np.float64)
>        values: FloatArray = (low + (high - low) * unit).astype(np.float64)
>        return cls.from_values(name=f"Beta(a={a}, b={b}) scaled to [{low}, {high}]", values=values)
>
>    def sample(
>        self,
>        *,
>        fraction: float,
>        rng: np.random.Generator,
>        strategy: Literal["without_replacement", "bootstrap"] = "without_replacement",
>    ) -> Population:
>        if not (0.0 < fraction <= 1.0):
>            raise ValueError(f"fraction must be in (0, 1], got {fraction}")
>
>        n_full: int = int(self.values.size)
>        n: int = max(1, int(round(n_full * fraction)))
>
>        match strategy:
>            case "without_replacement":
>                values: FloatArray = rng.choice(self.values, size=n, replace=False).astype(np.float64)
>            case "bootstrap":
>                values = rng.choice(self.values, size=n, replace=True).astype(np.float64)
>            case _:
>                raise ValueError(f"Unexpected sampling strategy: {strategy}")
>
>        name: str = f"Sample({strategy}, fraction={fraction:.4f}) of {self.name}"
>        return Population.from_values(name=name, values=values)
>```

## 1) Populations + descriptive statistics (practice-first)

### Short theory speech
- **Population**: a distribution / generator of values.
- **Sample**: finite i.i.d. draws $X_1,\dots,X_n$ from one population.
- **[[random variable]]**: outcome → number (example: `wealth_usd`).
- **[[probability]]**: number in $[0,1]$ (example: $P(160 < height\_cm < 170)$).
- **[[probability density function]]**: for continuous $X$, probabilities are **areas**:
  - $P(a \le X \le b)=\int_a^b f(x)\,dx$
- **Density plots ([[histograms]])**:
  - histogram with `stat="density"` approximates a PDF (area $\approx 1$)
  - KDE is a smooth PDF approximation
- **[[descriptional statistics]]:**
	- [[mathematical expectation]] (mean)
	- [[variance]]
	- [[kurtosis]]
	- [[skewness]] 

### Demo: one DataFrame of people (4 columns, 4 different distributions)

>[!info]- Code snippet
>```python
>import matplotlib.pyplot as plt
>import numpy as np
>import seaborn as sns
>import pandas as pd
>
>n: int = 250_000
>
># "People" table (one row = one person)
># Each column is a different random variable / distribution.
>pop_age_years: Population = Population.triangular(low=18.0, mode=32.0, high=80.0, n=n, rng=rng)
>pop_height_cm: Population = Population.normal(mu=170.0, sigma=10.0, n=n, rng=rng)
># "wealth" is right-skewed with long tail
>pop_wealth_usd: Population = Population.lognormal(mu=10.2, sigma=0.8, n=n, rng=rng, shift=0.0)
># exam scores: bounded [0,100] and slightly skewed
>pop_exam_score_pct: Population = Population.beta_scaled(a=4.0, b=2.0, low=0.0, high=100.0, n=n, rng=rng)
>
>df_people: pd.DataFrame = pd.DataFrame(
>    {
>        "age_years": np.round(pop_age_years.values).astype(int),
>        "height_cm": pop_height_cm.values,
>        "wealth_usd": pop_wealth_usd.values,
>        "exam_score_pct": pop_exam_score_pct.values,
>    }
>)
>
>specs: list[tuple[str, str, Population]] = [
>    ("age_years", "years", pop_age_years),
>    ("height_cm", "cm", pop_height_cm),
>    ("wealth_usd", "usd", pop_wealth_usd),
>    ("exam_score_pct", "score", pop_exam_score_pct),
>]
>
>fig, axes = plt.subplots(2, 2, figsize=(14, 9))
>
>for ax, (col, xlabel, pop) in zip(axes.ravel(), specs, strict=True):
>    x: np.ndarray = df_people[col].to_numpy()
>    x = x[:25_000]
>
>    # heavy tail: trim extreme tail ONLY for visualization
>    if col == "wealth_usd":
>        x = x[x <= np.quantile(x, 0.995)]
>
>    sns.histplot(x=x, bins=60, stat="density", alpha=0.35, ax=ax)
>    sns.kdeplot(x=x, ax=ax)
>    ax.axvline(pop.mean, color="black", linestyle="--", linewidth=2)
>    ax.axvline(pop.median, color="black", linestyle=":", linewidth=2)
>
>    ax.set_title(col)
>    ax.set_xlabel(xlabel)
>
>    stats_txt = (
>        f"mean={pop.mean:.2f}\n"
>        f"var={pop.var:.2f}\n"
>        f"skew={pop.skew:.2f}\n"
>        f"kurt(excess)={pop.kurtosis_excess:.2f}"
>    )
>    ax.text(
>        0.02,
>        0.98,
>        stats_txt,
>        transform=ax.transAxes,
>        va="top",
>        ha="left",
>        fontsize=10,
>        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.8},
>    )
>
>plt.suptitle("One DataFrame of people: 4 columns (hist + KDE) + descriptive stats")
>plt.tight_layout()
>plt.show()
>```


## 2) [[Law of Large Numbers (LLN)]]: moments converge

### Short theory speech
If $X_1,\dots,X_n$ are i.i.d. and the moment exists, then sample moments converge to population moments as $n$ grows.

For the mean:

$$
\bar X_n \to \mu
$$

### Demo: sample sizes grid + 4 moments convergence

>[!info]- Code snippet
>```python
>import matplotlib.pyplot as plt
>import numpy as np
>import seaborn as sns
>from scipy import stats
>
>pop: Population = Population.lognormal(mu=10.2, sigma=0.8, n=400_000, rng=rng)
>
># 1) Grid: how samples of different size look
>sample_sizes = [30, 300, 3_000, 30_000]
>fig, axes = plt.subplots(2, 2, figsize=(14, 9))
>
>for ax, n in zip(axes.ravel(), sample_sizes, strict=True):
>    sample: Population = pop.sample(fraction=float(n) / float(pop.values.size), rng=rng, strategy="without_replacement")
>    x = sample.values
>    x_plot = x[x <= np.quantile(x, 0.995)]
>    sns.histplot(x=x_plot, bins=60, stat="density", alpha=0.35, ax=ax)
>    sns.kdeplot(x=x_plot, ax=ax)
>    ax.set_title(f"Sample from wealth_usd (n={n})")
>    ax.set_xlabel("usd")
>    ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
>
>plt.suptitle("Samples from the same population (different n)")
>plt.tight_layout()
>plt.show()
>
># 2) 4 moments convergence: estimate moments as n grows
>max_n = 30_000
>x_stream = pop.sample(fraction=float(max_n) / float(pop.values.size), rng=rng, strategy="without_replacement").values
>
>n_grid = np.unique(np.geomspace(20, max_n, num=60).astype(int))
>mean_hat = np.empty(n_grid.size, dtype=float)
>var_hat = np.empty(n_grid.size, dtype=float)
>skew_hat = np.empty(n_grid.size, dtype=float)
>kurt_hat = np.empty(n_grid.size, dtype=float)
>
>for i, n in enumerate(n_grid):
>    x_n = x_stream[:n]
>    mean_hat[i] = float(np.mean(x_n))
>    var_hat[i] = float(np.var(x_n, ddof=0))
>    skew_hat[i] = float(stats.skew(x_n, bias=False))
>    kurt_hat[i] = float(stats.kurtosis(x_n, fisher=True, bias=False))
>
>fig, axes = plt.subplots(2, 2, figsize=(14, 9))
>
>axes[0, 0].plot(n_grid, mean_hat, label="sample mean")
>axes[0, 0].axhline(pop.mean, color="black", linestyle="--", label="population mean")
>axes[0, 0].set_title("Mean convergence")
>
>axes[0, 1].plot(n_grid, var_hat, label="sample var")
>axes[0, 1].axhline(pop.var, color="black", linestyle="--", label="population var")
>axes[0, 1].set_title("Variance convergence")
>
>axes[1, 0].plot(n_grid, skew_hat, label="sample skew")
>axes[1, 0].axhline(pop.skew, color="black", linestyle="--", label="population skew")
>axes[1, 0].set_title("Skewness convergence")
>
>axes[1, 1].plot(n_grid, kurt_hat, label="sample kurtosis (excess)")
>axes[1, 1].axhline(pop.kurtosis_excess, color="black", linestyle="--", label="population kurtosis (excess)")
>axes[1, 1].set_title("Kurtosis convergence")
>
>for ax in axes.ravel():
>    ax.set_xlabel("n")
>    # Force scientific notation for cleaner y-axis labels
>    ax.ticklabel_format(axis="y", style="scientific", scilimits=(-2, 2))
>    ax.legend()
>
>plt.suptitle("LLN: sample moments converge to population moments")
>plt.tight_layout()
>plt.show()
>```

## 3) [[Central Limit Theorem (CLT)]]: sampling distribution of the mean

### Short theory speech
If $X_1,\dots,X_n$ are i.i.d. with $\mathbb{E}[X]=\mu$ and $\mathrm{Var}(X)=\sigma^2 < \infty$, then for large $n$:

$$
\bar X \approx \mathcal{N}\left(\mu,\frac{\sigma^2}{n}\right)
$$

where:
- $\bar X$ is the sample mean
- $\mu$ is the population mean
- $\sigma^2$ is the population variance
- $n$ is the sample size
- $\sigma^2/n$ is the variance of the sampling distribution (standard error squared: $SE^2 = \sigma^2/n$)

CLT is about **$\bar X$ across repeated samples**, not about the raw population $X$.

**What about other statistics?** CLT focuses on the sample mean, but other statistics have their own sampling distributions:

1. **Sample Variance** ($S^2$): When the population is normal, $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$ (chi-square distribution with $n-1$ degrees of freedom) → [[chi-square distribution for sample variance]]
2. **Sample Standard Deviation** ($S$): Follows a **chi distribution** (not normal!), skewed right especially for small $n$. Approximate standard error: $SE(S) \approx \sigma/\sqrt{2n}$ → [[chi-square distribution for sample variance]]
3. **General statistics**: For "smooth" functions of means (e.g., ratios, products), the **[[delta method]]** provides asymptotic normality

### Demo: abnormal population → sample means become “more normal”

>[!info]- Code snippet
>```python
>import matplotlib.pyplot as plt
>import numpy as np
>import seaborn as sns
>
># Abnormal (skewed) population
>pop: Population = Population.exponential(scale=10.0, n=400_000, rng=rng)
>x_pop: np.ndarray = pop.values
>
># 1) Population plot
>fig, ax = plt.subplots()
>x_plot = x_pop[:25_000]
>sns.histplot(x=x_plot, bins=60, stat="density", alpha=0.35, ax=ax)
>sns.kdeplot(x=x_plot, ax=ax)
>ax.axvline(pop.mean, color="black", linestyle="--", linewidth=2, label=f"mean ≈ {pop.mean:.2f}")
>ax.axvline(pop.median, color="black", linestyle=":", linewidth=2, label=f"median ≈ {pop.median:.2f}")
>ax.set_title("Population (exponential): hist + KDE")
>ax.legend()
>plt.show()
>
># 2) Sampling distribution of the mean for different n
>def sample_means(*, pop_values: np.ndarray, n: int, m: int) -> np.ndarray:
>    idx = rng.integers(0, pop_values.size, size=(m, n))
>    return pop_values[idx].mean(axis=1)
>
>n_list = [5, 30, 200]
>m = 8_000
>
>fig, axes = plt.subplots(1, 3, figsize=(18, 5))
>
>for ax, n in zip(axes, n_list, strict=True):
>    means = sample_means(pop_values=x_pop, n=n, m=m)
>    mean_of_means = float(np.mean(means))
>    std_of_means = float(np.std(means, ddof=1))
>    theoretical_se = pop.std / float(np.sqrt(n))
>
>    sns.histplot(x=means, bins=60, stat="density", alpha=0.35, ax=ax)
>    sns.kdeplot(x=means, ax=ax)
>    ax.axvline(pop.mean, color="black", linestyle="--", linewidth=2, label=f"pop.mean={pop.mean:.2f}")
>    ax.set_title(f"Sample means (n={n})")
>    ax.set_xlabel("mean")
>
>    # Add stats as text box
>    stats_txt = (
>        f"mean(means)≈{mean_of_means:.2f}\n"
>        f"std(means)≈{std_of_means:.2f}\n"
>        f"pop.std/√n≈{theoretical_se:.2f}"
>    )
>    ax.text(
>        0.98,
>        0.98,
>        stats_txt,
>        transform=ax.transAxes,
>        va="top",
>        ha="right",
>        fontsize=9,
>        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.8},
>    )
>    ax.legend(loc="upper left")
>
>plt.suptitle("CLT: distribution of sample means gets closer to normal as n grows")
>plt.tight_layout()
>plt.show()
>```

## 4) Hypothesis Testing & p-values: practical CLT application

### Short theory speech

**[[p-value]]** is the probability of observing a result as extreme as (or more extreme than) what we got, **assuming $H_0$ is true**.

**Three types of tests:**
1. **Right-tailed** ($H_1: \mu > \mu_0$): p-value = $P(Z \geq z)$ where $z = \frac{\bar x - \mu_0}{SE}$
2. **Left-tailed** ($H_1: \mu < \mu_0$): p-value = $P(Z \leq z)$
3. **Two-tailed** ($H_1: \mu \neq \mu_0$): p-value = $2 \cdot P(Z \geq |z|)$

**Decision rule:** If p-value $< \alpha$ (e.g., 0.05), reject $H_0$.

### Demo: nootropics experiment (physics class exam scores)

**Scenario:** You teach physics. You know your students' exam scores follow $\mathcal{N}(\mu=70, \sigma=10)$. You select 30 random students, give them nootropics before the exam, and observe their mean score.

**Question:** Did nootropics improve performance?

>[!info]- Code snippet
>```python
>import matplotlib.pyplot as plt
>import numpy as np
>from scipy import stats
>
># 1) Population: all students (without nootropics)
>mu_0 = 70.0  # population mean (null hypothesis)
>sigma = 10.0  # population std (known)
>
># 2) Experiment: 30 students with nootropics
>n = 30
># Simulate treatment effect (unknown to us at first, let's say +3 points)
>treatment_effect = 3.0
>rng_experiment = np.random.default_rng(123)
>sample_treated = rng_experiment.normal(loc=mu_0 + treatment_effect, scale=sigma, size=n)
>
>x_bar = float(np.mean(sample_treated))
>print(f"Observed sample mean: {x_bar:.2f}")
>
># 3) Formulate hypothesis
># H0: mu = 70 (nootropics have no effect)
># H1: mu > 70 (nootropics improve scores) → RIGHT-TAILED TEST
>
># 4) Calculate test statistic
>se = sigma / np.sqrt(n)
>z = (x_bar - mu_0) / se
>print(f"Test statistic z = {z:.3f}")
>
># 5) Calculate p-value (right-tailed)
>p_value = 1 - stats.norm.cdf(z)
>print(f"p-value = {p_value:.4f}")
>
># 6) Decision
>alpha = 0.05
>if p_value < alpha:
>    print(f"✅ Reject H0 (p={p_value:.4f} < α={alpha}): nootropics likely have an effect!")
>else:
>    print(f"❌ Fail to reject H0 (p={p_value:.4f} ≥ α={alpha}): insufficient evidence")
>
># 7) Visualization
>fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))
>
># Left: Null distribution (sampling distribution under H0)
>x_range = np.linspace(mu_0 - 4*se, mu_0 + 4*se, 500)
>null_dist = stats.norm.pdf(x_range, loc=mu_0, scale=se)
>
>ax1.plot(x_range, null_dist, 'b-', linewidth=2, label=f"Null: N({mu_0}, {se:.2f}²)")
>ax1.axvline(mu_0, color='black', linestyle='--', linewidth=2, label=f"H0: μ={mu_0}")
>ax1.axvline(x_bar, color='red', linestyle='-', linewidth=2, label=f"Observed: x̄={x_bar:.2f}")
>
># Shade rejection region (right tail, α=0.05)
>critical_value = mu_0 + stats.norm.ppf(1 - alpha) * se
>x_reject = x_range[x_range >= critical_value]
>y_reject = stats.norm.pdf(x_reject, loc=mu_0, scale=se)
>ax1.fill_between(x_reject, y_reject, alpha=0.3, color='red', label=f"Rejection region (α={alpha})")
>
>ax1.set_title("Null Distribution (sampling distribution under H0)")
>ax1.set_xlabel("Sample mean")
>ax1.set_ylabel("Density")
>ax1.legend()
>ax1.grid(True, alpha=0.3)
>
># Right: Standard normal (z-score)
>z_range = np.linspace(-4, 4, 500)
>std_norm = stats.norm.pdf(z_range, loc=0, scale=1)
>
>ax2.plot(z_range, std_norm, 'b-', linewidth=2, label="N(0, 1)")
>ax2.axvline(0, color='black', linestyle='--', linewidth=2, label="z=0 (H0)")
>ax2.axvline(z, color='red', linestyle='-', linewidth=2, label=f"Observed z={z:.2f}")
>
># Shade p-value region (right tail)
>z_pvalue = z_range[z_range >= z]
>y_pvalue = stats.norm.pdf(z_pvalue, loc=0, scale=1)
>ax2.fill_between(z_pvalue, y_pvalue, alpha=0.3, color='green', label=f"p-value={p_value:.4f}")
>
>ax2.set_title("Standardized (z-score)")
>ax2.set_xlabel("z")
>ax2.set_ylabel("Density")
>ax2.legend()
>ax2.grid(True, alpha=0.3)
>
>plt.suptitle(f"Right-tailed test: H0: μ=70 vs H1: μ>70 (p={p_value:.4f})")
>plt.tight_layout()
>plt.show()
>```

### Practice: Coffee shop wait times

**Background:** A coffee shop chain advertises that average wait time is 5 minutes ($\mu_0 = 5.0$ min) with $\sigma = 1.5$ min. A customer activist suspects wait times are actually **longer** and collects data from 40 random visits.

**Given data:**

>[!info]- Code snippet
>```python
>import numpy as np
>from scipy import stats
>
># Population (advertised)
>mu_0 = 5.0  # minutes (null hypothesis)
>sigma = 1.5  # minutes (population std, assumed known)
>
># Sample: 40 random visits
>sample_wait_times = np.array([
>    5.2, 6.1, 4.8, 5.9, 6.3, 5.5, 4.9, 5.8, 6.0, 5.4,
>    5.7, 6.2, 5.3, 5.1, 6.5, 5.6, 5.0, 6.4, 5.8, 5.2,
>    6.0, 5.9, 5.4, 5.7, 6.1, 5.3, 5.5, 5.8, 6.2, 5.6,
>    5.1, 5.9, 6.3, 5.4, 5.7, 6.0, 5.2, 5.8, 6.1, 5.5
>])
>
>n = len(sample_wait_times)
>x_bar = np.mean(sample_wait_times)
>
>print(f"Sample size: n = {n}")
>print(f"Sample mean: x̄ = {x_bar:.3f} minutes")
>print(f"Population mean (H0): μ₀ = {mu_0} minutes")
>print(f"Population std: σ = {sigma} minutes")
>```

**Tasks:**
1. Formulate $H_0$ and $H_1$ (is this right-tailed, left-tailed, or two-tailed?)
2. Calculate the standard error (SE)
3. Calculate the z-statistic: $z = \frac{\bar x - \mu_0}{SE}$
4. Calculate the p-value
5. Make a decision at $\alpha = 0.05$ (reject or fail to reject $H_0$?)
6. Interpret the result in plain English

**Expected output (qualitative):**
- $H_1: \mu > 5.0$ (right-tailed test, since we suspect wait times are **longer**)
- Sample mean should be slightly above 5.0
- p-value should be small if the effect is real
- Decision: likely reject $H_0$, supporting the activist's suspicion

>[!tip]+ What if you don't know the population distribution?
>In practice, you often **don't know** $\mu_0$ and $\sigma$ of the general population. In such cases, you still can use:**
>- [[resampling techniques (bootstrap, jackknife, cross-validation)|resampling techniques]]: estimate population statistics right from your sample 
>- **Permutation test**: Shuffle treatment labels to test if the difference is real
>- **t-test**: Use sample std $s$ instead of $\sigma$ (see [[t-distribution and Student's t-test]])
>
>These methods let you perform hypothesis testing **without** assuming a known population distribution!

#🃏/semantic/math/statistics #🃏/semantic/math/probability-theory #🃏/source/statistics-basics-course

**Key Questions:**

1. How do you calculate the probability $(a < X < b)$?
?
By calculating the area under the curve between $a$ and $b$

2. What descriptive statistics did you learn from the lecture? What are their meanings?
?
- mean, variance, skewness, kurtosis (excess)
- pls see [[descriptional statistics]]  for meanings

2. What does LLN guarantee (conceptually)?
?
- Sample [[descriptional statistics]]  stabilizes near the population ones as $n$ grows: $\bar X_n \to \mu$.

2. What does CLT guarantee (conceptually)?
   ?
   - For i.i.d. random variables with finite mean $\mu$ and variance $\sigma^2$, the sample mean $\bar X$ is approximately normal: $\bar X \approx \mathcal{N}(\mu, \sigma^2/n)$
- This holds for **large enough $n$**, regardless of the population distribution
- CLT describes the **sampling distribution of $\bar X$**, not the raw data $X$

2. What is a p-value and how do you interpret it?
?
- The p-value is the probability of observing a result as extreme as (or more extreme than) what we got, **assuming $H_0$ is true**
- **Small p-value** (< $\alpha$, e.g., 0.05): Evidence against $H_0$ → reject $H_0$
- **Large p-value** (≥ $\alpha$): Insufficient evidence → fail to reject $H_0$

8. What is the difference between right-tailed, left-tailed, and two-tailed tests?
?
- **Right-tailed** ($H_1: \mu > \mu_0$): p-value = $P(Z \geq z)$ (test if mean is greater)
- **Left-tailed** ($H_1: \mu < \mu_0$): p-value = $P(Z \leq z)$ (test if mean is smaller)
- **Two-tailed** ($H_1: \mu \neq \mu_0$): p-value = $2 \cdot P(Z \geq |z|)$ (test if mean is different)


