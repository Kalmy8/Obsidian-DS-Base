**Codewords:** Pivot, Melt, Stack, Unstack, Reshape Operations, Wide vs. Long Format, DataFrame Modifications, Views vs. Copies, apply/map Methods, DataFrame Structure Alterations

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
    'student': ['John', 'John', 'John', 'John'],
    'subject': ['math', 'math', 'physics', 'physics'],
    'year': [2022, 2023, 2022, 2023],
    'grade': [85, 88, 90, 92]
}
df_long = pd.DataFrame(data_long)
```

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
```

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
    var_name=['subject', 'year'],
    value_name='grade'
)
```

## 4. Stack and Unstack
### Stack
Moves the innermost column level to become the innermost index level:
```python
# Stack columns to create MultiIndex
df_stacked = df_wide.stack()

# Stack specific level
df_stacked = df_wide.stack(level=0)
```

### Unstack
The opposite of stack:
```python
# Unstack index to columns
df_unstacked = df_long.unstack()

# Unstack specific level
df_unstacked = df_long.unstack(level='year')
```

**Practice Problem 1: Data Reshaping Challenge**
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

## 5. Modifying DataFrame Values
### Direct Assignment
```python
# Modify single value
df.loc[0, 'age'] = 25

# Modify multiple values
df.loc[df['age'] < 20, 'status'] = 'junior'

# Conditional modifications
df.loc[df['grade'] >= 90, 'grade_letter'] = 'A'
df.loc[(df['grade'] >= 80) & (df['grade'] < 90), 'grade_letter'] = 'B'
```

### Using map() for Series
```python
# Map values in a series
df['grade_letter'] = df['grade'].map({
    90: 'A',
    80: 'B',
    70: 'C',
    60: 'D'
})

# Using lambda with map
df['age_group'] = df['age'].map(lambda x: 'Adult' if x >= 18 else 'Minor')

# Map with dictionary
status_mapping = {'active': 1, 'inactive': 0, 'pending': 2}
df['status_code'] = df['status'].map(status_mapping)
```

### Using apply() for Series or DataFrame
```python
# Apply to a series
df['name'] = df['name'].apply(str.upper)

# Apply to entire DataFrame
df = df.apply(pd.to_numeric, errors='ignore')

# Apply with lambda
df['full_name'] = df.apply(lambda row: f"{row['first_name']} {row['last_name']}", axis=1)

# Apply with custom function
def calculate_score(row):
    return row['exam'] * 0.7 + row['homework'] * 0.3

df['final_score'] = df.apply(calculate_score, axis=1)

# Apply to columns (axis=0)
df.apply(lambda x: x.max() - x.min(), axis=0)
```

### Using applymap() for DataFrame
```python
# Apply function to every element
df = df.applymap(str.strip)  # Remove whitespace from all string elements

# Format all numeric values
df = df.applymap(lambda x: f"${x:.2f}" if isinstance(x, (int, float)) else x)
```

**Practice Problem 2: Apply vs. Map Challenge**
```python
data = {
    'name': ['John Smith', 'Anna Johnson', 'Peter Brown'],
    'scores': [[85, 90, 88], [92, 95, 89], [78, 82, 80]]
}
df = pd.DataFrame(data)
```
Tasks:
- Use `apply()` to extract first and last names into separate columns
- Use `map()` to categorize names by first letter (A-M: Group 1, N-Z: Group 2)
- Calculate the average score for each student using `apply()`
- Create a custom function that returns the highest score and apply it to each student
- Compare the performance of `apply()` vs. a loop for calculating statistics

## 6. Understanding Views vs. Copies
### Chain Assignment Warning
```python
# This will raise a warning
df[df['age'] > 20]['grade'] = 90  # Wrong!

# Correct way
df.loc[df['age'] > 20, 'grade'] = 90
```

### Creating Copies
```python
# Create a deep copy
df_copy = df.copy()

# Create a view
df_view = df.loc[:]  # This is a view, modifications will affect original

# When slicing creates a copy vs view
subset = df[['name', 'age']]  # Copy
subset = df.loc[:, ['name', 'age']]  # View

# Demonstrate the difference
df_copy = df.copy()
df_view = df.loc[:]
df_copy.loc[0, 'age'] = 100  # Original df not affected
df_view.loc[0, 'age'] = 100  # Original df is modified
```

### SettingWithCopyWarning
```python
# Common scenarios that trigger the warning
subset = df[df['age'] > 20]  # This creates a copy
subset['status'] = 'adult'   # Warning: may not modify original

# How to properly modify a subset
df.loc[df['age'] > 20, 'status'] = 'adult'  # Correct way

# Using .copy() to explicitly create a copy
subset = df[df['age'] > 20].copy()  # No warning when modifying
subset['status'] = 'adult'  # This is fine, clearly modifying a copy
```

**Practice Problem 3: Views vs. Copies Challenge**
```python
data = {
    'id': [1, 2, 3, 4, 5],
    'value': [10, 20, 30, 40, 50]
}
original_df = pd.DataFrame(data)
```
Tasks:
- Create a copy of the DataFrame and a view of the DataFrame
- Modify a value in both the copy and the view
- Show how the original DataFrame is affected in each case
- Create a situation where chained assignment would raise a warning
- Show the correct way to modify values in a filtered DataFrame

## 7. Structural Modifications
### Renaming Columns
```python
# Rename specific columns
df = df.rename(columns={'old_name': 'new_name'})

# Rename using a function
df.columns = df.columns.str.replace(' ', '_')

# Apply formatting to all column names
df.columns = [col.lower() for col in df.columns]

# Rename with pattern
df = df.rename(columns=lambda x: f"col_{x}" if not x.startswith('col_') else x)
```

### Adding/Removing Columns
```python
# Add new column
df['new_column'] = values

# Add multiple columns
df = df.assign(
    new_col1 = df['col1'] * 2,
    new_col2 = lambda x: x['col2'].str.upper()
)

# Drop columns
df = df.drop(['column1', 'column2'], axis=1)

# Drop columns inplace
df.drop(['column1', 'column2'], axis=1, inplace=True)

# Drop by position
df = df.drop(df.columns[2], axis=1)  # Drop third column
```

### Index Operations
```python
# Set index
df = df.set_index('id')

# Reset index
df = df.reset_index()

# Multi-level index
df = df.set_index(['category', 'subcategory'])

# Change index name
df.index.name = 'student_id'

# Access levels of a MultiIndex
df.index.get_level_values(0)
```

## 8. Advanced DataFrame Modifications
### Conditional Column Creation
```python
# Using numpy.where
import numpy as np
df['status'] = np.where(df['age'] >= 18, 'Adult', 'Minor')

# Multiple conditions with numpy.select
conditions = [
    df['grade'] >= 90,
    df['grade'] >= 80,
    df['grade'] >= 70
]
choices = ['A', 'B', 'C']
df['letter_grade'] = np.select(conditions, choices, default='F')
```

### Using the replace Method
```python
# Replace specific values
df['status'] = df['status'].replace('inactive', 'disabled')

# Replace multiple values
df = df.replace({'yes': True, 'no': False})

# Replace using regex
df['text'] = df['text'].replace(r'^old_', 'new_', regex=True)
```

### Working with Dates and Times
```python
# Format datetime columns
df['date'] = df['date'].dt.strftime('%Y-%m-%d')

# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

# Add/subtract time periods
from datetime import timedelta
df['next_week'] = df['date'] + timedelta(days=7)
```

**Practice Problem 4: DataFrame Modification Practice**
```python
data = {
    'name': ['John Smith', 'Anna Johnson', 'Peter Brown', 'Maria Rodriguez'],
    'age': [20, 22, 21, 25],
    'grade': [85, 92, 78, 95],
    'email': [' john@email.com ', 'anna@email.com', ' peter@email.com', 'maria@email.com']
}
df = pd.DataFrame(data)
```
Tasks:
- Clean all email addresses (remove whitespace)
- Create a new column with last names only
- Create an 'age_group' column: '18-20', '21-23', '24+'
- Rename all columns to be lowercase and replace spaces with underscores
- Create a 'grade_letter' column with the appropriate letter grade

**Practice Problem 5: Advanced Structural Modifications**
```python
# Create a DataFrame with multi-level columns
import pandas as pd
import numpy as np

np.random.seed(42)
data = {
    ('Math', 'Midterm'): np.random.randint(70, 100, 5),
    ('Math', 'Final'): np.random.randint(70, 100, 5),
    ('Science', 'Midterm'): np.random.randint(70, 100, 5),
    ('Science', 'Final'): np.random.randint(70, 100, 5)
}
df = pd.DataFrame(data, index=['Student_1', 'Student_2', 'Student_3', 'Student_4', 'Student_5'])
```
Tasks:
- Create a new column for each subject showing the average of Midterm and Final
- Add a row showing the class average for each exam
- Create a new DataFrame showing only the Final scores
- Reset the index and rename it to 'student_name'
- Create a function that calculates a weighted score (70% Final, 30% Midterm) and apply it to the DataFrame

## 5. Exporting Data
```python
# Export to CSV
df.to_csv('output.csv', index=False)

# Export to Excel
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

# Export to JSON
df.to_json('output.json')

# Export to SQL
df.to_sql('table_name', engine, if_exists='replace', index=False)
```

**Practice Problem: Data Export**
- **Tasks**:
  - Export a DataFrame to CSV, Excel, and JSON formats.
  - Customize the output by excluding the index and specifying a different delimiter for the CSV file.
  - Verify the exported files by loading them back into Pandas and checking their contents.

  
#🃏/pandas-basics
**Review Questions:**
1. What is the difference between `map()`, `apply()`, and `applymap()`?
2. Why does pandas raise a warning about chained assignments? How can you avoid it?
3. When does pandas create a view vs. a copy of the data?
4. What is the difference between `df = df.drop()` and `df.drop(inplace=True)`?
5. How can you efficiently rename multiple columns in a DataFrame?
6. When should you use `np.where()` vs. `df.loc[]` for conditional assignments?
7. What is the performance difference between various DataFrame modification methods?
8. How can you modify values in a filtered DataFrame without triggering a SettingWithCopyWarning? 