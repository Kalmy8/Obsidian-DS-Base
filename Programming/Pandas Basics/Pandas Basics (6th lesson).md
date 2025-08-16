**Codewords:** DataFrame Modifications, Views vs. Copies, apply/map Methods

## Mock DataFrame for Examples
```python
import pandas as pd
import numpy as np

# Create a comprehensive DataFrame for practice
data = {
    'student_id': [1001, 1002, 1003, 1004, 1005, 1006],
    'first_name': ['John', 'Anna', 'Peter', 'Maria', 'David', 'Sarah'],
    'last_name': ['Smith', 'Johnson', 'Brown', 'Rodriguez', 'Wilson', 'Davis'],
    'age': [20, 22, 19, 24, 21, 23],
    'grade_math_midterm': [85, 92, 78, 95, 88, 90],
    'grade_math_final': [87, 94, 82, 93, 85, 92],
    'grade_science_midterm': [90, 89, 85, 97, 91, 88],
    'email': [' john.smith@email.com ', 'anna.johnson@email.com', ' peter.brown@email.com', 
              'maria.rodriguez@email.com', ' david.wilson@email.com', 'sarah.davis@email.com'],
    'status': ['active', 'active', 'inactive', 'active', 'active', 'inactive'],
    'enrollment_date': pd.to_datetime(['2023-01-15', '2023-02-01', '2023-01-20', 
                                      '2023-01-10', '2023-02-15', '2023-01-25'])
}
df = pd.DataFrame(data)
df
```

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

**Practice Problem 1: Direct Assignment**
Using the mock DataFrame `df` created above:

Tasks:
1. Update Peter Brown's age to 20.
2. Set all inactive students' status to 'on_hold'.
3. Create a new column 'grade_category' and assign 'high' to students with math midterm >= 90.
4. Add a new column 'full_name' by combining first_name and last_name.
5. Create an 'adult' column: True for age >= 21, False otherwise.

### Using apply() for Series or DataFrame
```python
# Apply to a series
df['first_name'] = df['first_name'].apply(str.upper)

# Apply to rows
df['full_name'] = df.apply(lambda row: f"{row['first_name']} {row['last_name']}", axis=1)

# Apply to columns (axis=0)
df.apply(lambda x: x.max() - x.min(), axis=0)
```

#### Tip: using replace instead of 'apply'

Replace is generally faster and more readable for simple cases

```python
# Replace specific values
df['status'] = df['status'].replace('inactive', 'disabled')

# Replace multiple values
df = df.replace({'yes': True, 'no': False})

# Replace using regex
df['text'] = df['text'].replace(r'^old_', 'new_', regex=True)
```

### Using map() for entire DataFrame 
```python
# Apply function to every element
df = df.map(str.strip)  # Remove whitespace from all string elements

# Increase all numeric values
df = df.map(lambda x: x + 10)

# Convert all lists to their lengths
df = df.map(lambda x: len(x) if isinstance(x, list) else x)
```

**Practice Problem 2: Apply Challenge**
Tasks:
1. Create a 'grade_math_average' column by calculating the average of midterm and final math grades.
2. Create a 'name_category' column: Group 1 for first names A-M, Group 2 for N-Z.
3. Clean all email addresses (remove whitespace) using apply.
4. Create a 'grade_math_max' column showing the higher of midterm or final math grade.
5. Apply a function to create 'enrollment_month' column from enrollment_date.
6. Uppercase all string columns in the DataFrame 
7. Format all numeric columns to strings with two decimal places (85 --> "85.00")


## 6. Understanding Views vs. Copies problem

### What are Views and Copies?
```python
# A VIEW shares memory with original data - changes affect both objects
# A COPY creates independent memory - changes only affect the copy

# Demonstrate the difference
df_copy = df.copy() # Guarantees a copy
df_view = df.loc[:] # Guarantees a view
df_copy.loc[0, 'age'] = 100  # Original df not affected
df_view.loc[0, 'age'] = 100  # Original df is modified

# Whether operations return views or copies depends on context:
# - Some indexing operations may return views
# - Some return copies  
# - This unpredictability causes SettingWithCopyWarning

# Example 1:
subset = df[df['age'] > 20]     # Might be view or copy - unclear
subset['status'] = 'adult'      # Warning occures

# Example 2:
df[df['age'] > 20]['grade'] = 90  # Might be view or copy - unclear
```

### Solutions

#### Safety techinque
```python
# 1: Use .loc for direct modification  
df.loc[df['age'] > 20, 'status'] = 'adult'  # Clear intent: modify original

# 2: Explicit copy when you want independent data
subset = df[df['age'] > 20].copy()  # Clearly a copy
subset['status'] = 'adult'          # No warning, clearly modifying copy only

# 3: Aviod chain operators
df['status'] = df['status'].where(df['age'] <= 20, 'adult')  # No chaining
```

#### Copy-on-Write (CoW) - Modern Solution
```python
# Enable CoW (will be default in pandas 3.0+):
pd.options.mode.copy_on_write = True

# With CoW: operations create "lazy copies" that copy only when modified
df_subset = df[df['age'] > 20]  # Lazy copy
df_subset.iloc[0, 0] = 100      # Automatically triggers copy, original unchanged

# CoW benefits:
# - Eliminates SettingWithCopyWarning
# - Predictable behavior: modifications never affect other objects  
# - Better performance through delayed copying
```

**Practice Problem 3: Views vs. Copies Challenge**
Tasks:
1. Create a copy of the DataFrame and a view of the DataFrame.
2. Modify a value in both the copy and the view.
3. Show how the original DataFrame is affected in each case.
4. Create a situation where chained assignment would raise a warning.
5. Show the correct way to modify values in a filtered DataFrame.

## 7. Structural Modifications

### Adding/Removing Columns
```python

# Add new column
df.loc[:, 'new_column'] = values

# remove columns using drop
df = df.drop(['column1', 'column2'], axis=1)
df = df.drop(df.columns[2], axis=1)  # Drop third column
# or using slicing
df = df.loc[:, ~df.columns.isin(['column1', 'column2'])]
```
#### Tip: Adding columns conditionally
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

### Renaming Columns
```python
# Rename specific columns
df = df.rename(columns={'old_name': 'new_name'})
df = df.rename(columns=lambda x: f"col_{x}" if not x.startswith('col_') else x)

# Rename using a function
df.columns = df.columns.str.replace(' ', '_')

# Apply formatting to all column names
df.columns = [col.lower() for col in df.columns]
```

### Adding/Removing Rows
```python

# Add/update a row (as a Series or dict)
df.loc[len(df)] = [value1, value2, ...]  # Add at the end
# or append a row
df = pd.concat([df, pd.DataFrame([{'col1': v1, 'col2': v2}])], ignore_index=True)

# remove rows using drop
df = df.drop([0, 2], axis=0)  # Remove rows with index 0 and 2
# or using slicing
df = df[df['age'] >= 21]  # Keep only rows where age >= 21
```

**Practice Problem 4: DataFrame Modification Practice**
Tasks:
1. Delete the row for "Peter Brown" from the DataFrame.
2. Append a new student: "Linda White", age 23, grade_math_midterm 88, grade_math_final 90, grade_science_midterm 85, email "linda.white@email.com", status "active", enrollment_date "2023-03-01".
3. Update "Anna Johnson"'s grade_math_final to 95 and age to 23.
4. Create a new column with last names only.
5. Create an 'age_group' column: '18-20', '21-23', '24+'.
6. Rename all columns to be lowercase and replace spaces with underscores.
7. Create a 'grade_letter' column with the appropriate letter grade (A: >=90, B: 80-89, C: 70-79, F: <70) based on 'grade_math_final'.

## Index Operations

```python
# Set index
df = df.set_index('id')

# Reset index
df = df.reset_index()
```

**Practice Problem 5: Index Operations**
Tasks:
1. Group the DataFrame by `status` and `age`, and calculate the mean of `grade_math_midterm` and `grade_math_final` for each group.
2. Observe the resulting DataFrame: does it have a MultiIndex?
3. Reset the index so `status` and `age` become columns again (flat DataFrame).
4. Set the `student_id` as an index.

**Practice Problem 6: Advanced Structural Modifications**
Tasks:
1. For each student, create a new column 'math_score_weighted' as 70% final + 30% midterm.
2. Add a row showing the class average for each exam (math midterm, math final, science midterm).
3. Create a new DataFrame showing only students with 'grade_math_final' >= 90.
4. Reset the index and rename it to 'student_number'.

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

# Export to pickle TODO
df.to_pickle('output.pkl')
```
pickle стандартная python библиотека, которая создана
чтобы сохранять и загружать питоновские объекты

**Practice Problem: Data Export**
- **Tasks**:
  - Export a DataFrame to CSV, Excel, and JSON formats.
  - Customize the output by excluding the index and specifying a different delimiter for the CSV file.
  - Verify the exported files by loading them back into Pandas and checking their contents.

  
#🃏/pandas-basics
**Review Questions:**

In pandas, we have 2 main methods to modify dataframe values. All
other methods are just syntax sugar and enforce simplicity. 
What are those main methods? What do they do?
?
- `apply` acts a function on a single column/row of a dataframe
- `map` acts a function on every element of the dataframe
    
What's the difference between dataframe view and copy?
?
- View of the dataframe is a new reference to the same python object, thus
changes on view affect the original df
- Copy is a separate object in python, thus changes only affect this new copy

Why does pandas raise SettingWithCopyWarning?
?
- Some pandas operations can unpredictibly return a view or a copy, so when you modify them you can not be sure if you are changing the original df or not

How to modify values correctly so SettingWithCopyWarning occures?
?
- By always using .loc (which guarantees to return a view)

2 ways to delete a column or a row from a dataframe
?
- Using `drop` (simpler, faster)
- Using `.loc/.iloc`

You have a DataFrame with a column "salary" containing employee salaries. You want to create a new column "salary_band" that assigns:
"low" for salaries below 50,000
"medium" for salaries between 50,000 and 100,000 (inclusive)
"high" for salaries above 100,000
How can you do that in pandas? 
?
```python
import numpy as np
  conditions = [
      df['salary'] < 50000,
      (df['salary'] >= 50000) & (df['salary'] <= 100000),
      df['salary'] > 100000
  ]
  choices = ['low', 'medium', 'high']
  df['salary_band'] = np.select(conditions, choices)
```
