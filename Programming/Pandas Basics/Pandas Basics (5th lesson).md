**Codewords:** GroupBy, Aggregation, Transform, Rolling Windows

# General Principle: split-apply-combine

The "split-apply-combine" strategy is a powerful way to perform complex data analysis:
1.  **Split:** The data is grouped based on some criteria (e.g., by course, by semester)
2.  **Apply:** A function is applied to each group independently. This could be:
    - aggregation (like `sum()`, `mean()`), 
    - transformation (like standardizing data within the group),
    - filtration (like discarding entire groups),
    - custom function 
3.  **Combine:** The results of these operations are then combined into a new DataFrame or Series

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
- Calculate the average grade and attendance by city using 
- Find cities where the average grade is above 85 using  and boolean indexing
- Calculate the percentage of students in each city with grades above 90 using  with a custom function
- Determine if there are significant grade differences by gender in each city using with mean and std

### 2. Transform Operations

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
- Calculate a weighted final score that accounts for absences
- Create a grading curve where the top 10% get A, next 20% get B, etc.

### 3. Filter Operations

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

The `.apply()` method is the most flexible GroupBy method. It takes a function and applies it to each group. The function can return a scalar, a Series, or a DataFrame. Pandas will then try to combine the results in a sensible way.
Use `.apply()` when the desired operation doesn't fit neatly into `agg()`, `transform()`, or `filter()`. However, be mindful that `.apply()` can be slower than the more specific functions for common operations.

```python
# Example: For each course, return a Series with the range of grade_percentage and average project_score

df_grades.groupby('course_name')['grade_percentage'].apply(lambda x: x.max() - x.min())

# Example: For each semester, select the top 2 students based on grade_percentage
df_grades.groupby('semester_taken')['grade_percentage'].apply(lambda x : x.nlargest(2))

# Example: Apply a function that returns a DataFrame, modifying the group
df_grades_with_norm_project = df_grades.groupby('course_name')['project_score'].apply(lambda x: (x - x.mean()) / x.std())
```

#### Practice Problem: Custom Group-wise Analysis

Using `df_grades`:
1.  Write a custom apply function that, for each `course_name`, calculates the average `attendance_days` and the number of unique `semester_taken` the course was offered in. The function should return a Pandas Series. Store the result in `course_attendance_semester_info`.
2.  Write a custom apply function that, for each `semester_taken`, identifies students who scored below the semester's average `grade_percentage` but above the semester's average `project_score`. The function should return a DataFrame containing `student_id`, `student_name`, `grade_percentage`, and `project_score` for these students. Store the result in `df_mixed_performers_per_semester`.
3.  For each `course_name`, use `.apply()` to add a new column `is_top_project_scorer` which is `True` if the student's `project_score` is equal to the maximum `project_score` in that course, and `False` otherwise.

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


#🃏/pandas-basics
**Review Questions:**

What is the difference between `agg()`, `transform()`, `filter()` and `apply()`?
For every operation provide a simple example
?
- `agg()` is used to **unite all the group's observations** into a single/several characteristics
	- Example: divide students by groups and calculate group's mean
- `transform()` is used to **modify every observation** based on the group's statistics 
	- Example: calculate ranks given people's heights
- `filter()` is used to **exclude certain groups** based on their single/several characteristics
	- Example: divide students by groups and exclude groups where average score <= 40
- `apply()`  is more general and can be used for everything

`pd.Series` `apply(func...)` method accepts a function. What will be assigned as the first parameter of that `func` function when using:
- Ordinal pandas dataframe?
- GroupbyObject?
?
- a whole single column/row of the dataframe `pd.Series` object
- only few within-group observations of that column passed as `pd.Series` object

Why won't we always use `apply()`?
?
It is much slower compared to more specific  `agg()`, `transform()`, `filter()`

When would you use `rolling()` operations?
?
While calculating statistics for structured data, like calculating mean average for a time series

