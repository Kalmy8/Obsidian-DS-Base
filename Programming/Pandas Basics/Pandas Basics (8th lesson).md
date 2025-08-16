**Codewords:** Seaborn visualization

### 0. Where do different type of plots come?

Generally speaking, there are only 2 types of variables you can observe in a dataset:
- [[discrete variable]]: school grade, blood type, color
- [[continuous variable]]: age, height, weight

All the plots in the world do only answer 2 questions:
- What is the relationship between some several (2 or more) variables?
- What are the characteristics of a single given variable?

Thus, every different plot covers up some combination above:
1) Lineplot/scatterplot shows the **relationship** between 2 **continuous** variables
2) Histogram shows the **distribution** of a given **continuous or discrete variable**

### Mock DataFrame
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({
    'city': np.random.choice(['Moscow', 'London', 'Paris'], 100),
    'year': np.random.choice([2022, 2023], 100),
    'sales': np.random.normal(1000, 200, 100).astype(int),
    'profit': np.random.normal(200, 50, 100).astype(int),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})
```

# Plotting Relationships

## Relationship Visualization Table

| Plot Type         | X         | Y         | Use Case                        | Seaborn Function      |
|-------------------|-----------|-----------|----------------------------------|-----------------------|
| Scatter           | Continuous| Continuous| Relationship between 2 continuous variables | sns.scatterplot       |
| Line              | Discrete/Continuous| Continuous| Trend over time/group         | sns.lineplot          |
| Bar               | Discrete  | Continuous| Compare means/totals by group   | sns.barplot           |
| Swarm/Strip       | Discrete  | Continuous| Show all points by group        | sns.swarmplot/stripplot|
| Heatmap           | Discrete  | Discrete  | Crosstab relationships          | sns.heatmap           |

## Relationship Plot Examples

### 1. Scatterplot (two continuous variables)
```python
sns.scatterplot(data=df, x='sales', y='profit')
plt.title('Sales vs. Profit Relationship')
plt.show()
```

### 2. Lineplot (trend over time/group)
```python
df_grouped = df.groupby('year')['sales'].mean().reset_index()
sns.lineplot(data=df_grouped, x='year', y='sales')
plt.title('Sales Trend by Year')
plt.show()
```

### 3. Barplot (discrete + continuous)
```python
sns.barplot(data=df, x='city', y='sales', estimator=np.mean)
plt.title('Average Sales by City')
plt.show()
```

### 4. Swarmplot (all points by group)
```python
sns.swarmplot(data=df, x='city', y='sales')
plt.title('Sales Distribution by City')
plt.show()
```

### 5. Heatmap (two discrete variables)
```python
ct = pd.crosstab(df['city'], df['category'])
sns.heatmap(ct, annot=True, fmt='d', cmap='Blues')
plt.title('City vs. Category Relationship')
plt.show()
```

## Practice Problems: Relationship Visualization

**Practice Problem: Relationship Analysis**

You have a dataset with student performance data:

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
students_df = pd.DataFrame({
    'student_id': range(1, 101),
    'study_hours': np.random.normal(15, 5, 100).round(1),
    'exam_score': np.random.normal(75, 15, 100).round(1),
    'attendance_rate': np.random.normal(85, 10, 100).round(1),
    'major': np.random.choice(['Computer Science', 'Mathematics', 'Physics', 'Chemistry'], 100),
    'year': np.random.choice([1, 2, 3, 4], 100),
    'gpa': np.random.normal(3.2, 0.5, 100).round(2)
})
```

**Tasks:**

1. Show how average GPA changes over the years. What pattern do you see?

2. Visualize the relationship between major and year (how many students of each major are in each year). Which year has the most Computer Science students?

3. Create a visualization showing the relationship between study hours and exam scores. What type of relationship do you observe?

4. Compare average exam scores across different majors. Which major has the highest average score?

5. Show how study hours vary across different majors. Which major has students with the highest study hours?

**Expected Outputs:**
- 5 different plots showing relationships between variables
- Brief interpretation of each relationship pattern
- Identification of key insights from each visualization

---

### Remaining Plot Types

| Category          | Plot Type         | X         | Y         | Use Case                        | Seaborn Function      |
|-------------------|-------------------|-----------|-----------|----------------------------------|-----------------------|
| **Counts**        | Countplot         | Discrete  | –         | Frequency of categories         | sns.countplot         |
| **Proportions**   | Pie               | Discrete  | –         | Proportions                     | pandas .plot.pie      |
| **Distributions** | Box/Violin        | Discrete  | Continuous| Distribution by group           | sns.boxplot/violinplot|
|                   | Histogram/KDE     | Continuous| –         | Distribution                    | sns.histplot/kdeplot  |
|                   | Jointplot         | Continuous| Continuous| Distribution of 2 variables     | sns.jointplot         |

# Counts, Proportions, and Distributions

## Countplot (discrete frequency)
```python
sns.countplot(data=df, x='city')
plt.title('City Frequency')
plt.show()
```

## Pie chart (proportions, pandas)
```python
df['category'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Category Proportions')
plt.ylabel('')
plt.show()
```

## Distribution Plot Types

Distribution plots show the characteristics of variables. The choice between them is often a matter of preference:

- **Histogram**: Most honest representation of data
- **KDE**: Smoother, more visually appealing version of histogram
- **Box plot**: Simplified summary showing median, quartiles, and outliers
- **Violin plot**: Compromise between box plot and full distribution shape

## Histogram (distribution)
```python
sns.histplot(df['sales'], bins=20)
plt.title('Sales Distribution')
plt.show()
```

## KDE plot (smooth distribution)
```python
sns.kdeplot(df['sales'])
plt.title('Sales Distribution (KDE)')
plt.show()
```

## Boxplot (discrete + continuous)
```python
sns.boxplot(data=df, x='city', y='sales')
plt.title('Sales by City')
plt.show()
```

## Violinplot (discrete + continuous)
```python
sns.violinplot(data=df, x='city', y='sales')
plt.title('Sales by City (Violin)')
plt.show()
```

## Jointplot (distribution of 2 variables)
```python
sns.jointplot(data=df, x='sales', y='profit', kind='scatter')
plt.suptitle('Sales vs. Profit Distribution', y=1.02)
plt.show()
```

## Practice Problems: Counts, Proportions, and Distributions

**Practice Problem: Comprehensive Analysis**

Using the students dataset:

**Tasks:**

1. Show the distribution of exam scores. What's the most common score range?

2. Show how many students are in each major. Which major has the most students?

3. Show the distribution of GPA by year. Do students improve their GPA over time?

4. Visualize the relationship between study hours and exam scores with a distribution plot. What pattern do you observe?

5. Show the proportion of students in each year. What percentage of students are in year 2?

6. Compare the distribution of study hours across different majors. Which major has the most consistent study hours?

**Expected Outputs:**
- Countplot showing student counts by major
- Pie chart showing year proportions
- Histogram or KDE of exam scores
- Box plot or violin plot of study hours by major
- Box plot of GPA by year
- Joint plot of study hours vs exam scores
- Interpretation of all patterns and trends

---


#🃏/pandas-basics

**Key Questions:**

1. What are the two main questions that all plots answer?
?
- What is the relationship between variables?
- Or what are the characteristics of a variable?

2. When would you use a line plot instead of a scatter plot?
?
- When showing trends over time or ordered categories
- When X-axis represents a sequence or progression

3. What's the difference between a bar plot and a swarm plot for discrete vs continuous data?
?
- Bar plot shows aggregated values (means/totals)
- Swarm plot shows individual data points distributed by group

5. How do you create a heatmap to show relationships between two discrete variables?
?
- Use pd.crosstab() to create a contingency table
- Pass the result to sns.heatmap()

---

# Bonus: Pairplot (All Pairwise Relationships)

## Pairplot Overview

Pairplot is a powerful tool that shows all pairwise relationships in your dataset at once. It creates a matrix of plots where each variable is plotted against every other variable.

## Pairplot Example
```python
sns.pairplot(df, hue='city')
plt.suptitle('All Pairwise Relationships', y=1.02)
plt.show()
```

**What it shows:**
- Diagonal: Distribution of each variable (histogram or KDE)
- Off-diagonal: Scatter plots between all variable pairs
- Color coding: Can use `hue` parameter to color by categorical variable

**When to use:**
- Exploratory data analysis
- Quick overview of all relationships
- Identifying patterns across multiple variables


