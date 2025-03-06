**Codewords:** GroupBy, Aggregation, Transform, Rolling Windows, Custom Aggregations

## 1. GroupBy Operations
### Basic Grouping
```python
# Group by single column
grouped = df.groupby('city')

# Group by multiple columns
grouped = df.groupby(['city', 'grade_level'])

# Basic aggregations
city_means = df.groupby('city')['grade'].mean()
city_stats = df.groupby('city')['grade'].agg(['mean', 'std', 'count'])

# Iterating through groups
for name, group in df.groupby('city'):
    print(f"City: {name}, Count: {len(group)}")
    print(group.head())
```

### Multiple Aggregations
```python
# Different aggregations for different columns
agg_dict = {
    'grade': ['mean', 'max'],
    'age': 'mean',
    'attendance': 'sum'
}
result = df.groupby('city').agg(agg_dict)

# Named aggregations
result = df.groupby('city').agg(
    avg_grade=('grade', 'mean'),
    max_grade=('grade', 'max'),
    avg_age=('age', 'mean')
)

# Custom column names
result.columns = ['_'.join(col).strip() for col in result.columns.values]
```

**Practice Problem 1: Basic GroupBy Operations**
```python
data = {
    'student': ['John', 'Anna', 'Peter', 'Sarah', 'Mike', 'Emma', 'David', 'Linda'],
    'city': ['New York', 'Boston', 'New York', 'Boston', 'Chicago', 'Chicago', 'New York', 'Boston'],
    'grade': [85, 92, 78, 95, 88, 84, 90, 86],
    'attendance': [0.9, 0.95, 0.85, 0.92, 0.88, 0.91, 0.94, 0.87],
    'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F']
}
df = pd.DataFrame(data)
```
Tasks:
- Calculate the average grade and attendance by city
- Add columns for: city_avg_grade, grade_diff_from_city_avg
- Find cities where the average grade is above 85
- Calculate the percentage of students in each city with grades above 90
- Determine if there are significant grade differences by gender in each city

## 2. Transform Operations
### Basic Transforms
```python
# Add mean grade by city
df['city_mean_grade'] = df.groupby('city')['grade'].transform('mean')

# Multiple transforms
transforms = {
    'grade': ['mean', 'std'],
    'age': 'mean'
}
df_transformed = df.groupby('city').transform(transforms)

# Creating multiple columns at once
df[['grade_mean', 'grade_std']] = df.groupby('city')['grade'].transform(['mean', 'std'])

# Group-wise normalization
df['grade_normalized'] = df.groupby('city')['grade'].transform(lambda x: (x - x.mean()) / x.std())
```

### Custom Transforms
```python
# Calculate percentile within each group
def percentile_rank(x):
    return x.rank(pct=True)

df['grade_percentile'] = df.groupby('city')['grade'].transform(percentile_rank)

# Z-score within groups
df['grade_zscore'] = df.groupby('city')['grade'].transform(lambda x: (x - x.mean()) / x.std())

# Calculate deviation from group median
df['grade_dev_from_median'] = df.groupby('city')['grade'].transform(lambda x: x - x.median())
```

**Practice Problem 2: Transform vs. Aggregation Challenge**
```python
import pandas as pd
import numpy as np

# Create student data with multiple tests
np.random.seed(42)
students = ['S' + str(i).zfill(3) for i in range(1, 31)]
classes = ['Math', 'Physics', 'Chemistry'] * 10
tests = np.random.randint(60, 100, size=30)
absences = np.random.randint(0, 10, size=30)

data = {
    'student_id': students,
    'class': classes,
    'test_score': tests,
    'absences': absences
}
df = pd.DataFrame(data)
```
Tasks:
- Calculate each student's test score relative to their class average
- Identify which students scored above their class average
- For each class, add columns showing:
  - Class average score
  - Student's percentile within the class
  - Normalized score (z-score)
- Calculate a weighted final score that accounts for absences
- Create a grading curve where the top 10% get A, next 20% get B, etc.

## 3. Rolling Window Operations
### Basic Rolling
```python
# Simple moving average
df['3_day_avg'] = df['value'].rolling(window=3).mean()

# Rolling with min_periods
df['3_day_avg'] = df['value'].rolling(window=3, min_periods=1).mean()

# Different window functions
df['rolling_sum'] = df['value'].rolling(window=3).sum()
df['rolling_max'] = df['value'].rolling(window=3).max()
df['rolling_std'] = df['value'].rolling(window=3).std()
```

### Rolling with GroupBy
```python
# Rolling average by group
df['rolling_avg'] = df.groupby('city')['value'].rolling(3).mean().reset_index(0, drop=True)

# Complex example with multiple steps
def rolling_by_group(df, group_col, value_col, window):
    # Group the dataframe
    grouped = df.groupby(group_col)
    # Apply rolling mean to each group
    rolling_means = grouped[value_col].rolling(window=window).mean()
    # Reset the index to align with original dataframe
    result = rolling_means.reset_index(level=0, drop=True)
    return result

df['rolling_avg_by_city'] = rolling_by_group(df, 'city', 'value', 3)
```

**Practice Problem 3: Time Series Rolling Windows**
```python
import numpy as np
import pandas as pd
from datetime import datetime

# Create a date range
dates = pd.date_range('2023-01-01', periods=20)

# Create synthetic time series data
data = {
    'date': dates,
    'value': [10, 12, 15, 14, 16, 18, 17, 20, 22, 21, 19, 23, 25, 24, 26, 28, 27, 30, 32, 31],
    'group': ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
```
Tasks:
- Calculate 3-day and 7-day rolling averages for each group
- Find the maximum value in each group's rolling window
- Compare each value to its group's moving average (as a percentage difference)
- Identify trends by calculating the rolling correlation between values and time
- Create a summary showing min, max, and mean values by month for each group

## 4. Advanced Aggregation Techniques
### Custom Aggregation Functions
```python
def iqr(x):
    return x.quantile(0.75) - x.quantile(0.25)

# Use custom function in aggregation
df.groupby('city')['grade'].agg(iqr)

# Multiple custom functions
def grade_summary(x):
    return pd.Series({
        'mean': x.mean(),
        'above_90': (x >= 90).sum(),
        'below_60': (x < 60).sum()
    })

df.groupby('city')['grade'].apply(grade_summary)

# Custom function that returns a DataFrame
def comprehensive_stats(group):
    stats = {
        'count': len(group),
        'mean_grade': group['grade'].mean(),
        'pass_rate': (group['grade'] >= 60).mean(),
        'top_student': group.loc[group['grade'].idxmax()]['name']
    }
    return pd.Series(stats)

df.groupby('city').apply(comprehensive_stats)
```

### Filter Groups
```python
# Filter groups with more than 5 students
def filter_size(x):
    return len(x) > 5

filtered = df.groupby('city').filter(filter_size)

# Filter based on mean grade
def filter_mean_grade(x):
    return x['grade'].mean() > 80

filtered = df.groupby('city').filter(filter_mean_grade)

# Combining filter with aggregation
high_performing_groups = (
    df.groupby('city')
    .filter(lambda x: x['grade'].mean() > 85)
    .groupby('city')
    .agg({
        'grade': ['mean', 'min', 'max'],
        'name': 'count'
    })
)
```

**Practice Problem 4: Custom Aggregations Challenge**
```python
data = {
    'store': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'product': ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z'],
    'sales': [100, 120, 90, 80, 95, 110, 120, 140, 100],
    'returns': [5, 8, 3, 4, 7, 6, 8, 10, 5],
    'stock': [50, 60, 45, 40, 50, 55, 60, 70, 50]
}
df = pd.DataFrame(data)
```
Tasks:
- Calculate net sales (sales - returns) for each store-product combination
- Find the return rate (returns/sales) by store
- Create a custom aggregation function that computes:
  - Total sales
  - Average return rate
  - Stock turnover (sales/stock)
  - Best-selling product
- Create a "performance score" combining sales performance and return rates
- Rank stores based on overall performance

## 5. Combining GroupBy with Other Operations
### Groupby and Join
```python
# Create group statistics
city_stats = df.groupby('city').agg(
    avg_grade=('grade', 'mean'),
    student_count=('name', 'count')
)

# Join back to original DataFrame
df_with_stats = df.join(city_stats, on='city')

# Alternative approach using transform
df['avg_grade'] = df.groupby('city')['grade'].transform('mean')
df['student_count'] = df.groupby('city')['name'].transform('count')
```

### Hierarchical Grouping
```python
# Groupby with hierarchical index
hierarchical = df.groupby(['city', 'grade_level']).agg({
    'grade': ['mean', 'count'],
    'attendance': 'mean'
})

# Access specific group
nyc_high_school = hierarchical.loc[('New York', 'High School')]

# Unstack to reshape
reshaped = hierarchical.unstack(level='grade_level')

# Create hierarchical column index
df.columns = pd.MultiIndex.from_tuples([
    ('student', 'name'), ('student', 'age'), 
    ('performance', 'grade'), ('performance', 'attendance')
])
grouped = df.groupby(('student', 'age')).mean()
```

#🃏/pandas-basics
**Review Questions:**
1. What is the difference between `transform()` and `agg()`?
2. How can you apply different aggregation functions to different columns?
3. When would you use `rolling()` operations, and what are their key parameters?
4. How can you create custom aggregation functions?
5. What is the difference between `filter()` and `transform()` in groupby operations?
6. How do you handle hierarchical group structures?
7. What are the advantages and limitations of the `transform()` method?
8. How can you optimize groupby operations for large datasets? 