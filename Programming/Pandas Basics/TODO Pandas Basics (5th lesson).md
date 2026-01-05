---
type: note
status: inbox
tags:
- tech/python
- tech/stack/pandas
sources:
- null
- '[[Pandas Basics Course]]'
authors:
- null
---
#🃏/semantic/pandas #🃏/pandas-basics-course

**Codewords:** GroupBy, Aggregation, Transform, Rolling Windows
# General Principle: split-apply-combine

The "split-apply-combine" strategy is a powerful way to perform complex data analysis:
1. **Split:** The data is grouped based on some criteria (e.g., by course, by semester)
2. **Apply:** A function is applied to each group independently. This could be:
 - aggregation (like `sum()`, `mean()`), 
 - transformation (like standardizing data within the group),
 - filtration (like discarding entire groups),
 - custom function 
3. **Combine:** The results of these operations are then combined into a new DataFrame or Series

TODO examples with apply and cross-column interactions
TODO say that without agg you do not need groupby: transform and filter 
are just syntax sugar

# Mock DataFrame
Let's define a reusable mock DataFrame for our examples. This DataFrame contains student grades and related information for various courses.

```python
import pandas as pd
import numpy as np

# Reusable Mock DataFrame for GroupBy examples
np.random.seed(42) # for reproducibility
data_grades = {
 'student_id': range(1001, 1021),
 'student_name': [f'Student_{i}' for i in range(20)],
 'course_name': np.random.choice(['Algebra Basics', 'Calculus I', 'Physics for Beginners', 'Intro to Programming'], 20),
 'semester_taken': np.random.choice(['Fall 2023', 'Spring 2024'], 20),
 'grade_percentage': np.random.randint(60, 101, 20),
 'attendance_days': np.random.randint(10, 21, 20),
 'project_score': np.random.randint(0, 101, 20),
 'total_possible_attendance': 20
}
df_grades = pd.DataFrame(data_grades)
```

# 1. Split: GroupBy Operations

```python
# Group by single column (e.g., by course_name)
grouped_by_course = df_grades.groupby('course_name')

# Iterating through groups (e.g., by course_name)
print("Iterating through groups by course_name:")
for name, group in grouped_by_course:
 print(name, '\n\n')
 print(group[['student_name', 'grade_percentage', 'course_name']].head(2)) 
 print("-" * 30)
```

```python
# Group by multiple columns (e.g., by course_name and semester_taken)

grouped_by_course_and_semester = df_grades.groupby(['course_name', 'semester_taken'])

# Iterating through groups (e.g., by course_name)
print("Iterating through groups by course_name:")
for name, group in grouped_by_course_and_semester:
 print(name, '\n\n')
 print(group[['student_name', 'grade_percentage', 'course_name']].head(2)) 
 print("-" * 30)
```
# 2. Apply

### 1. Aggregation

Aggregation is a process where a function is applied to a group of items, mapping a sequence of values to a single summary value (e.g., `Sequence[] -> single entity`). Common aggregations include `mean`, `sum`, `min`, `max`, and `count`. However, you can also use custom functions for more complex summaries, like joining strings or collecting values into a list.

```python
# Example: Mean grade_percentage per course_name
df_grades.groupby('course_name')['grade_percentage'].mean()

# Example: Multiple stats for grade_percentage per course_name
df_grades.groupby('course_name')['grade_percentage'].agg(['mean', 'std', 'count'])

 # Example: Different aggregations for different columns in df_grades
df_grades.groupby('course_name').agg(
 avg_grade=('grade_percentage', 'mean'),
 total_attendance=('attendance_days', 'sum'),
 avg_project_score=('project_score', 'mean')
)

# Example: Using custom aggregation functions like string joining or collecting into a list
df_grades.groupby('course_name').agg(
 all_students=('student_name', ', '.join),
 grade_as_list=('grade_percentage', list)
)

# More advanced aggregation examples
df_grades.groupby('course_name').agg(
 # Get the number of unique semesters a course was offered in
 unique_semesters=('semester_taken', 'nunique'),
 # Find the range of grades in each course
 grade_range=('grade_percentage', lambda x: x.max() - x.min()),
 # Get the name of the first student in the group (assuming data is sorted meaningfully)
 first_student_in_group=('student_name', 'first')
)
```

```python
# Example: Aggregating with multiple column groups 
df_grades.groupby(['course_name', 'semester_taken'])['grade_percentage'].mean()

# Example: Multiple stats for grade_percentage per course_name
df_grades.groupby(['course_name', 'semester_taken'])['grade_percentage'].agg(['mean', 'std', 'count'])

 # Example: Different aggregations for different columns in df_grades
df_grades.groupby(['course_name', 'semester_taken']).agg(
 avg_grade=('grade_percentage', 'mean'),
 total_attendance=('attendance_days', 'sum'),
 avg_project_score=('project_score', 'mean')
)
```
#### Practice Problem: Basic Aggregation Operations

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
- Calculate the average grade and attendance by city.
- For each city, create a comma-separated string of student names and collect all grades into a list.
- For each city, find the range of grades (`max` - `min`) and the number of unique genders present.
- For each city, get the name of the first student that appears in the data.
- Find cities where the average grade is above 85.
- Calculate the percentage of students in each city with grades above 90 using a custom function with `.agg()`.
- Determine if there are significant grade differences by gender in each city by calculating the mean and standard deviation of grades.

### 2. Transform Operations TODO убрать насовсем?
todo description
Sequence[N] --> Sequence[N]

```python
# Add mean grade_percentage for each course_name to each student's row
df_grades['grade_percentage_mean'] = df_grades.groupby('course_name')['grade_percentage'].transform('mean')

# Group-wise normalization (z-score) of grade_percentage within each course_name
df_grades['grade_percentage_z_score'] = df_grades.groupby('course_name')['grade_percentage'].transform(lambda x: (x - x.mean()) / x.std())

### Custom Transforms using df_grades
df_grades['grade_percentage_rank'] = df_grades.groupby('course_name')['grade_percentage'].transform(lambda x: x.rank(pct=True))

# Calculate deviation of attendance_days from the median attendance_days in that course_name
df_grades['attendance_dev_from_course_median'] = df_grades.groupby('course_name')['attendance_days'].transform(lambda x: x - x.median())
```

#### Practice Problem: Transform 
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
- Create a grading curve where the top 10% get A, next 20% get B, etc.

### 3. Filter Operations TODO убрать насовсем?

Filtration allows you to discard entire groups based on a group-wise computation that evaluates to `True` or `False`. This is useful when you want to focus your analysis on groups that meet certain criteria.

```python

# Example: Keep only courses where the average attendance_days is above 15
df_grades.groupby('course_name').filter(lambda x: x['attendance_days'].mean() > 1)

# Example: Keep only courses with at least 8 students
df_popular_courses = df_grades.groupby('course_name').filter(lambda x: len(x) >= 8) 

```

#### Practice Problem: Filtering Student Data 
Using `df_grades`:

1. Filter out `semester_taken` where the average `project_score` is below 70. Store the result in `df_strong_project_semesters`.
 - Output: A DataFrame containing only rows from semesters where the average project score was >= 70.
 - Columns: all columns from df_grades.

2. Filter `df_grades` to keep only `course_name` groups where all students have `attendance_days` greater than 12. Store the result in `df_high_attendance_courses`.
 - Output: A DataFrame containing only rows from courses where every student attended more than 12 days.
 - Columns: all columns from df_grades.

3. Find `course_name` groups where the range of `grade_percentage` (max - min) is less than 15 points. Store in `df_consistent_grade_courses`.
 - Output: A DataFrame containing only rows from courses where the difference between the max and min grade is less than 15.
 - Columns: all columns from df_grades.

### 4. Custom Operations with apply

The `.apply()` method is the most flexible GroupBy method, giving you complete control over what to do with each group. A critical difference from `.agg()` lies in what is passed to the function:
- **`.agg()`** passes each column of a group as a `pd.Series` to its function.
- **`.apply()`** passes the **entire group as a `pd.DataFrame`** to its function.

This allows `.apply()` to perform complex calculations involving multiple columns at once. While `agg()` returns a single aggregated value per group and `transform()` returns a sequence of the same size as the group, `.apply()` can return a scalar, a Series, or even a DataFrame of any shape.

This is powerful for complex operations where the output for each group is not a simple aggregation or transformation:
* `agg()`: `group -> single value` (e.g., `mean`, `sum`)
* `transform()`: `group -> series of same size` (e.g., z-score)
* `apply()`: `group -> scalar | series | dataframe` (e.g., return top N rows, or a dataframe of custom stats)

Use `.apply()` when your logic doesn't fit `agg` or `transform`, but remember it can be slower.

```python
# Example 1: For each semester, select the top 2 students based on grade_percentage.
# This returns a DataFrame for each group, and pandas concatenates them.
top_students_per_semester = df_grades.groupby('semester_taken').apply(lambda group: group.nlargest(2, 'grade_percentage'))

# Example 2: For each course, calculate a set of custom statistics and return them as a dictionary.
# Pandas will convert the dictionary to a Series for each group.
def get_course_stats(group):
 return {
 'grade_range': group['grade_percentage'].max() - group['grade_percentage'].min(),
 'project_score_avg': group['project_score'].mean(),
 'attendance_to_grade_corr': group['attendance_days'].corr(group['grade_percentage'])
 }

course_custom_stats = df_grades.groupby('course_name').apply(get_course_stats)

# Example 3: Apply a function that returns a modified DataFrame for each group.
def standardize_and_rank(group):
 return pd.DataFrame({
 'student_id': group['student_id'],
 'grade_zscore': (group['grade_percentage'] - group['grade_percentage'].mean()) / group['grade_percentage'].std(),
 'project_rank': group['project_score'].rank(method='dense', ascending=False)
 })

df_processed_groups = df_grades.groupby('course_name').apply(standardize_and_rank)
```

#### Practice Problem: Custom Group-wise Analysis

Using `df_grades`:
1. For each `semester_taken`, identify students who scored below that semester's average `grade_percentage` but had a `project_score` in the top 25% for that semester. Return a DataFrame with `student_id`, `student_name`, `grade_percentage`, and `project_score`.
2. Write a function that, for each `course_name`, returns a DataFrame containing the student with the highest and lowest `grade_percentage`. The DataFrame should contain the `student_name` and their `grade_percentage`.
3. For each `course_name`, calculate a "consistency score," defined as `1 / standard deviation of grade_percentage`. Also, find the student with the median `project_score`. Return these two values with custom labels: `'consistency_score'` and `'median_project_student'`.

# Rolling Window Operations
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

**Review Questions:**

Why use `agg()`, `transform()`, `filter()` and `apply()`?
For every operation provide a simple example
?
- `agg()` is used to **unite all the group's observations** into a single/several characteristics
	- Example: divide students by groups and calculate group's mean
- `transform()` is used to **modify every observation** based on the group's statistics 
	- Example: calculate ranks given people's heights
- `filter()` is used to **exclude certain groups** based on their single/several characteristics
	- Example: divide students by groups and exclude groups where average score <= 40
- `apply()` is more general and can be used for everything

Fill the gaps:
- `agg()` maps Sequence[N] -> ...
- `transform()` maps Sequence[N] -> ...
- `filter` maps Sequence[N] -> ...
- `apply` maps Sequence[N] -> ...
?
- `agg()` maps Sequence[N] -> Single Entity 
- `transform()` maps Sequence[N] -> Sequence[N]
- `filter` maps Sequence[N] -> Sequence[M<=N]
- `apply` maps Sequence[N] -> Sequence[M], where `M` can be arbitrary

TODO ITS NOT TRUE I GUESS
Crucial distinguish:
- `agg()`, `transform()`, `filter()` can hold functions, which take ... as their parameter
- `apply()` can hold functions, which take ... as their parameter
?
- `agg()`, `transform()`, `filter()` can hold functions, which take **a single Column (pd.Series)** as their parameter
- `apply()` can hold functions, which **take a whole group (pd.DataFrame)** as their parameter

Why won't we always use `apply()`?
?
It is much slower compared to more specific `agg()`, `transform()`, `filter()`

When would you use `rolling()` operations?
?
While calculating statistics for structured data, like calculating mean average for a time series

