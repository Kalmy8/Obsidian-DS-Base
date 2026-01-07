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
#🃏/semantic/pandas #🃏/source/pandas-basics-course

**Codewords:** Pivot, Melt, Stack, Unstack, Reshape Operations, Wide vs. Long Format

TODO make pivot and melt methods to make table "more wide" or "more long" format

TODO объяснить что таблица полностью задается пересечением 
индекса, колонки и значения
## 1. Understanding Data Formats
### Wide (Unstacked/Spreadsheet) Format

- Each row represents a complete set of observations for one subject/entity
- Thus, one row per subject/entity
- Variables "spread" across multiple columns

```python
# Wide format example
data_wide = {
 'student': ['John', 'Anna', 'Peter'],
 'math_2022': [85, 92, 78],
 'math_2023': [88, 95, 82],
 'physics_2022': [90, 88, 75],
 'physics_2023': [92, 85, 80]
---
}
df_wide = pd.DataFrame(data_wide)
```

### Long Format

- Each row represents a single measurement for one subject/entity
- Thus, each subject/entity will appear in N rows, where N is the number of metrics you measure
- Variables are typically stored in a single column

```python
# Long format example
data_long = {
 'student': ['John', 'John', 'John', 'John', 'Anna', 'Anna', 'Anna', 'Anna'],
 'subject': ['math', 'math', 'physics', 'physics', 'math', 'math', 'physics', 'physics'],
 'year': [2022, 2023, 2022, 2023, 2022, 2023, 2022, 2023],
 'grade': [85, 88, 90, 92, 92, 95, 88, 85]
}
df_long = pd.DataFrame(data_long)
```
## 2. Reshaping 

Usually includes switching from Wide to Long data formats and vice-versa

### `pd.pivot_table()`

Method is used to switch from long to wide format:

![[Pasted image 20250511105228.png]]

```python
# Calculate mean grades by subject and year
df_pivot = df_long.pivot_table(
 values='grade',
 index='student',
 columns=['subject', 'year'],
 aggfunc='mean'
)

# Multiple aggregation functions
df_pivot = df_long.pivot_table(
 values='grade',
 index='student',
 columns='subject',
 aggfunc=['mean', 'max', 'min']
)

# Adding margins (row/column totals)
df_pivot = df_long.pivot_table(
 values='grade',
 index='student',
 columns='subject',
 aggfunc='mean',
 margins=True,
 margins_name='Average'
)
```

**Tasks:**
- Calculate the average grade for each student across all subjects and years.
 - Expected output: A DataFrame with students as the index and a single column showing the average grade.
- Create a pivot table that shows the maximum grade each student achieved in each subject, regardless of the year.
 - Expected output: A DataFrame with students as the index and subjects as columns, showing the maximum grade for each subject.
- Generate a pivot table that displays the minimum grade for each subject in each year, with students as the index.
	- Expected output: A DataFrame with students as the index, and a multi-level column index for subjects and years, showing the minimum grade.
- Create a pivot table with the total grades for each student, adding margins to show the overall total for each subject.
	- Expected output: A DataFrame with students as the index and subjects as columns, including a row and column for totals.
- Construct a pivot table that shows both the mean and standard deviation of grades for each subject and year, with students as the index.
 - Expected output: A DataFrame with students as the index, and a multi-level column index for subjects and years, showing both the mean and standard deviation.

### `pd.melt()`

Method is used to convert from wide to long format
![[Pasted image 20250511105255.png]]
```python
# Melt all the columns
df_long = df_wide.melt(
 id_vars=['student'], 
 var_name='subject', 
 value_name='grade'
)

# Handling multiple column levels
df_long = df_wide.melt(
 id_vars=['student'],
 value_vars=['math_2022', 'math_2023', 'physics_2022', 'physics_2023'], # Melt only specific columns
 var_name='subject_year',
 value_name='grade'
)

# Post-processing melted data
# Split the subject_year column into separate columns
df_long[['subject', 'year']] = df_long['subject_year'].str.split('_', expand=True)

# Complex melting with multiple id variables
df_long = pd.melt(
 df_wide,
 id_vars=['student', 'school'],
 value_vars=['math_2022', 'math_2023', 'physics_2022', 'physics_2023'],
 var_name='subject_year',
 value_name='grade'
)
```

**Tasks:**
- Melt the DataFrame to convert all subject-year columns into a long format, keeping 'student' as the identifier, and then filter the data to show only entries where the grade is above 85.
 - Expected output: A DataFrame with 'student', 'subject_year', and 'grade' columns, filtered to show only grades above 85.
- Melt the DataFrame to include only 'math_2023' and 'physics_2022' columns, using 'student' as the identifier, and then sort the resulting DataFrame by 'grade' in descending order.
 - Expected output: A DataFrame with 'student', 'subject_year', and 'grade' columns, sorted by grade.
- After melting the DataFrame, split the 'subject_year' column into separate 'subject' and 'year' columns, and then filter to show only the 'math' subject.
 - Expected output: A DataFrame with 'student', 'subject', 'year', and 'grade' columns, filtered to show only 'math' entries.
- Melt the DataFrame while keeping 'student' as the identifier, and then filter the resulting DataFrame to show only entries for the year 2023.
 - Expected output: A DataFrame with 'student', 'subject_year', and 'grade' columns, filtered to show only entries for 2023.
- Melt the DataFrame and then use the resulting long DataFrame to find all entries where the student's name starts with 'J'.
 - Expected output: A DataFrame with 'student', 'subject_year', and 'grade' columns, filtered to show only entries for students whose names start with 'J'.

What are the wide and long data formats? What methods allow you to switch from wide to long format and vice versa?
?
- Long format:
    - Each row represents a single measurement for one subject/entity
    - Thus, each subject/entity will appear in N rows, where N is the number of metrics you measure
    - Variables are typically stored in a single column:
student_id	| exam	| score
s1	| exam_math	| 90
s1	| exam_english	| 85
s2	| exam_math	| 70
s2	| exam_english	| 88
- Wide format:
    - Each row represents a complete set of observations for one subject/entity
    - Thus, one row per subject/entity
    - Variables "spread" across multiple columns
student_id | exam_math | exam_english
s1	| 90	| 85
s2	| 70	| 88
- Long -> Wide: `pivot_table()`
- Wide -> Long: `melt()`
<!--SR:!2026-01-09,4,270-->

What happens when `pivot_table()` encounters duplicate values?
?
- It aggregates them together using user-defined function passed with `aggfunc` parameter (default is `mean`)
<!--SR:!2026-01-09,4,270-->

How would you flatten a hierarchical index after reshaping operations?
?
- With `reset_index()` method
<!--SR:!2026-01-09,4,270-->

After melting, you often encounter composite values you would like to expand in a separate column:
| index | student | subject | grade |
| ----- | ------- | --------- | ----- |
| 0 | John | math_2022 | 85 |
| 1 | Anna | math_2022 | 92 |
| 2 | Peter | math_2022 | 78 |
| 3 | John | math_2023 | 88 |
So for that table, you want to split 'subject' column into 'subject' and 'year' columns. How do you handle such situation?
?
- By using `df['subject'].str.split(by = '_', expand = True)` accessor on that value column Series
<!--SR:!2026-01-10,3,250-->

Given this data:
```python
data_wide = {
    'student': ['John', 'Anna', 'Peter'],
    'math_2022': [85, 92, 78],
    'math_2023': [88, 95, 82],
    'physics_2022': [90, 88, 75],
    'physics_2023': [92, 85, 80],
}
```
- Convert it to long format
- Convert it back again to the original format
?
```python
df_wide.melt( # Use melt (wide -> long)
    id_vars=['student'],
    var_name='subject',
    value_name='grade') \
	    .pivot_table( # Use pivot_table (long -> wide)
   index='student', 
   columns='subject') \
	   .reset_index()
```
<!--SR:!2026-01-09,4,270-->

