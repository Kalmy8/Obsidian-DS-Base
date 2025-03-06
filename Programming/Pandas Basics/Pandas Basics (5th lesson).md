**Codewords:** Pivot, Melt, Stack, Unstack, Reshape Operations, Wide vs. Long Format

## 1. Understanding Data Formats
### Wide Format
Data where each subject's repeated measurements are in separate columns:
```python
# Wide format example
data_wide = {
    'student': ['John', 'Anna', 'Peter'],
    'math_2022': [85, 92, 78],
    'math_2023': [88, 95, 82],
    'physics_2022': [90, 88, 75],
    'physics_2023': [92, 85, 80]
}
df_wide = pd.DataFrame(data_wide)
```

### Long Format
Data where each observation is a separate row:
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

**Practice Problem 1: Transform Between Data Formats**
```python
data = {
    'student': ['John', 'John', 'John', 'Anna', 'Anna', 'Anna'],
    'year': [2022, 2023, 2024, 2022, 2023, 2024],
    'math': [85, 88, 92, 92, 95, 96],
    'physics': [90, 92, 94, 88, 85, 90],
    'chemistry': [87, 89, 91, 91, 94, 95]
}
df = pd.DataFrame(data)
```
Tasks:
- Convert to wide format with years as columns
- Calculate year-over-year improvement for each subject
- Create a summary showing each student's best subject
- Find which student improved the most in each subject from 2022 to 2024
- Create a stacked bar chart showing grades by subject and year for each student

## 2. Reshaping with pivot
### Basic Pivot
```python
# Convert long to wide format
df_wide = df_long.pivot(
    index='student',
    columns='subject',
    values='grade'
)

# Multiple values
df_wide = df_long.pivot(
    index='student',
    columns=['subject', 'year'],
    values='grade'
)

# Reshape the index/columns after pivot
df_wide = df_wide.reset_index()  # Convert index to column
```

### pivot_table
More flexible than pivot, handles duplicate values:
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

**Practice Problem 2: Working with Pivot and Pivot Table**
```python
data = {
    'student': ['John', 'Anna', 'Peter', 'Sarah'],
    'math_midterm': [85, 92, 78, 90],
    'math_final': [88, 95, 82, 92],
    'physics_midterm': [90, 88, 75, 85],
    'physics_final': [92, 85, 80, 88],
    'chemistry_midterm': [86, 90, 82, 87],
    'chemistry_final': [89, 93, 84, 91]
}
df = pd.DataFrame(data)
```
Tasks:
- Convert to long format with separate subject and exam columns
- Calculate average grade by subject for each student
- Find the highest grade for each exam type (midterm/final)
- Create a summary showing min, max, and mean grades by subject
- Create a pivot table showing the improvement from midterm to final for each student and subject

## 3. Reshaping with melt
### Basic Melt
```python
# Convert wide to long format
df_long = df_wide.melt(
    id_vars=['student'],
    var_name='subject',
    value_name='grade'
)

# Handling multiple column levels
df_long = df_wide.melt(
    id_vars=['student'],
    value_vars=['math_2022', 'math_2023', 'physics_2022', 'physics_2023'],
    var_name='subject_year',
    value_name='grade'
)

# Post-processing melted data
# Split the subject_year column into separate columns
df_long[['subject', 'year']] = df_long['subject_year'].str.split('_', expand=True)
```

### Advanced Melt
```python
# Complex melting with multiple id variables
df_long = pd.melt(
    df_wide,
    id_vars=['student', 'school'],
    value_vars=['math_2022', 'math_2023', 'physics_2022', 'physics_2023'],
    var_name='subject_year',
    value_name='grade'
)

# Melt only specific columns
cols_to_melt = [col for col in df_wide.columns if col.startswith('math') or col.startswith('physics')]
df_long = pd.melt(
    df_wide, 
    id_vars=['student'], 
    value_vars=cols_to_melt,
    var_name='subject_year', 
    value_name='grade'
)
```

**Practice Problem 3: Real-world Data Reshaping with Melt**
```python
# Sales data by product, region, and quarter
data = {
    'product': ['ProductA', 'ProductA', 'ProductA', 'ProductA', 'ProductB', 'ProductB', 'ProductB', 'ProductB'],
    'region': ['North', 'South', 'North', 'South', 'North', 'South', 'North', 'South'],
    'quarter': ['Q1', 'Q1', 'Q2', 'Q2', 'Q1', 'Q1', 'Q2', 'Q2'],
    'sales': [100, 150, 120, 170, 90, 110, 95, 130],
    'units': [50, 70, 60, 80, 40, 50, 45, 60]
}
sales_df = pd.DataFrame(data)
```
Tasks:
- Create a pivot table showing sales by product and region for each quarter
- Calculate the total sales and units for each product and region
- Reshape the data to show quarter-over-quarter growth for each product
- Create a summary showing which region had the highest sales for each product
- Convert the data to show sales and units side by side for easier comparison

## 4. Stack and Unstack
### Stack
Moves the innermost column level to become the innermost index level:
```python
# Stack columns to create MultiIndex
df_stacked = df_wide.stack()

# Stack specific level
df_stacked = df_wide.stack(level=0)

# Naming stacked index level
df_stacked = df_wide.stack(level=0, dropna=False)
df_stacked.index.names = ['student', 'subject']
```

### Unstack
The opposite of stack:
```python
# Unstack index to columns
df_unstacked = df_long.set_index(['student', 'subject']).unstack()

# Unstack specific level
df_unstacked = df_long.set_index(['student', 'subject', 'year']).unstack(level='year')

# Fill NaN values after unstacking
df_unstacked = df_unstacked.fillna(0)
```

## 5. Advanced Reshaping Techniques
### Using pivot_table for Complex Aggregations
```python
# Multiple aggregations with custom names
df_pivot = df_long.pivot_table(
    values='grade',
    index=['student'],
    columns=['subject'],
    aggfunc={
        'grade': [
            ('Average', 'mean'),
            ('Highest', 'max'),
            ('Lowest', 'min')
        ]
    }
)

# Flattening column names
df_pivot.columns = ['_'.join(col).strip() for col in df_pivot.columns.values]
```

### Combining Reshape Operations
```python
# Complex transformation with pivot_table and melt
# First, create summary by student and subject
summary = df_long.pivot_table(
    values='grade',
    index=['student'],
    columns=['subject'],
    aggfunc=['mean', 'max', 'min']
)

# Then reshape the summary
summary_flat = summary.reset_index()
summary_long = pd.melt(
    summary_flat,
    id_vars=['student'],
    value_vars=[col for col in summary_flat.columns if col[0] in ['mean', 'max', 'min']],
    var_name=['stat', 'subject'],
    value_name='value'
)
```

**Practice Problem 4: Multi-level Reshaping Challenge**
```python
# Create a multi-level DataFrame
import pandas as pd
import numpy as np

np.random.seed(42)
subjects = ['Math', 'Physics', 'Chemistry']
assessments = ['Quiz', 'Midterm', 'Final']
students = ['Student_1', 'Student_2', 'Student_3']

# Create multi-level columns
columns = pd.MultiIndex.from_product([subjects, assessments], names=['Subject', 'Assessment'])

# Create data
data = np.random.randint(70, 100, size=(len(students), len(subjects) * len(assessments)))

# Create DataFrame
df = pd.DataFrame(data, index=students, columns=columns)
```
Tasks:
- Convert to long format with Subject, Assessment, and Grade columns
- Calculate the average grade for each student by subject
- Find which assessment type has the highest average score across all subjects
- Create a summary showing the best performing student in each subject
- Convert back to wide format but with Assessment as the primary column level

#🃏/pandas-basics
**Review Questions:**
1. What are the main differences between `pivot()` and `pivot_table()`?
2. When would you use `melt()` instead of `stack()`?
3. How do you handle multiple column levels when using `melt()`?
4. What is the relationship between wide and long format data?
5. How can you aggregate data while pivoting?
6. What happens when pivot encounters duplicate values? How can you handle this?
7. How would you flatten a hierarchical index after reshaping operations?
8. What are the advantages and disadvantages of wide versus long format data? 