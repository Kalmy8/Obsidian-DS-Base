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

**Codewords:** Boolean Indexing, Advanced loc/iloc, Multiple Conditions, Sorting, Filter Method

TODO logical indexing with columns
### Mock DataFrame for further examples and problems

```python
import pandas as pd

# Create a sample DataFrame
data = {
 'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
 'age': [20, 22, 21, 19, 23],
 # Grade columns with course prefix
 'grade_math_midterm': [85, 92, 78, 95, 88],
 'grade_math_final': [88, 95, 80, 98, 90],
 'grade_physics_midterm': [80, 95, 75, 90, 85],
 'grade_physics_final': [82, 90, 78, 88, 87],
 # Data columns with year and period suffixes
 'scores_2023_Q1': [88, 91, 79, 94, 86],
 'scores_2023_Q2': [90, 93, 81, 96, 89],
 'scores_2022_Q4': [84, 89, 77, 91, 85],
 # Height with unit suffix
 'height_cm': [175, 165, 180, 168, 190],
 'weight_kg': [70, 58, 75, 60, 80]
---
}
df = pd.DataFrame(data)
print(df)
```

### 1. Direct column and row access
```python
# Access single column (returns Series)
df['name']

# Access multiple columns (returns DataFrame)
df[['name', 'age']]

# Access rows by slicing
df[0:2] # First two rows
```

**Tasks:**
1. Extract the 'grade' column as a Series.
 - Get frequency counts of unique values 
 - Get descriptive statistics
2. Extract the 'grade' column as a Dataframe.
3. Create a new DataFrame from the old one with only the 'name', 'age', and 'city' columns.
4. Extract the first 3 rows using direct slicing.
 
>[!warning] 
>Direct access should be used with caution because of the Copy/View logic

## 1. Basic Indexing with loc and iloc

### loc - Label-based indexing

```python
# Select single row by label
df.loc[0] 

# Select multiple rows and columns by label
df.loc[0:2, ['name', 'age']]
```

### iloc - Integer-based indexing
Integer-based indexing with `iloc`:
```python
# Select single row by position
df.iloc[0]

# Select multiple rows and columns by position
df.iloc[0:2, 0:2]

# Select specific positions
df.iloc[[0, 2], [1, 2]]
```

**Tasks:**
- **Using loc:**
 1. Select the row with index 2 
 2. Select rows with indexes 1 through 3 and only the 'name' and 'grade' columns.

- **Using iloc**:
 1. Select the last row of the DataFrame.
 2. Select the first 3 rows and first 2 columns using `iloc`.
 3. Select the values at positions [0,1] and [2,3] (row, column) using `iloc`.

## 2. Boolean Indexing 

### Understanding Boolean Masks

A boolean mask is a Series or DataFrame of the same shape as your original DataFrame, but containing only `True` and `False` values. These masks are the foundation of boolean indexing.

```python
# Create a boolean mask
mask = df['age'] > 20
print("Boolean mask:")
print(mask)

# Using the mask to filter the DataFrame
filtered_df = df.loc[mask]
print("\nFiltered DataFrame:")
print(filtered_df)
```

- **Tasks**:
 1. Create a boolean mask for students with grades above 85 and print the mask.
 - Expected output: A Series with [False, True, False, True, True] 
 2. Create a mask for students whose names contain the letter 'e', then use it to filter the DataFrame.
 - Expected output: A DataFrame with Peter and Michael
 3. Create two masks: one for age > 20 and another for grade > 90. Print both masks side by side with the original data.
 - Expected output: DataFrame with original data plus two boolean columns

### Applying the mask
```python
# Select all students with age > 20
df.loc[df['age'] > 20]

# Select all students whose name starts with 'A'
df.loc[df['name'].str.startswith('A')]
```

- **Tasks**:
 1. Select students with a grade of 90 or higher and create a new DataFrame.
 - Expected output: A DataFrame with Anna and Sarah
 2. Find all students from 'Boston'.
 - Expected output: A DataFrame with Anna and Sarah
 3. Find all students whose name ends with 'h'.
 - Expected output: A DataFrame with Sarah

### Advanced Column Selection
```python
# Select columns that start with 'grade'
df.loc[:, df.columns.str.startswith('grade')]

# Select numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df.loc[:, numeric_cols]

# Select all columns EXCEPT 'name' and 'city'
df.loc[:, ~df.columns.isin(['name', 'city'])]
```

**Practice Problem: Advanced Column Selection**
- **Tasks**:
 1. Select all columns that start with 'grade'.
 - Expected output: A DataFrame with all rows and only the grade_math, grade_physics, and grade_chemistry columns
 2. Select all numeric columns in the DataFrame.
 - Expected output: A DataFrame with all rows and the age, grade_math, grade_physics, and grade_chemistry columns
 3. Select only the string columns in the DataFrame.
 - Expected output: A DataFrame with all rows and the name and city columns
 4. Select all columns except 'name' and 'grade_math'.
 - Expected output: A DataFrame with all rows and the age, grade_physics, grade_chemistry, and city columns

### Multiple Conditions

Combine conditions using & (and) and | (or):
```python
# Students over 20 AND with grade >= 90
df.loc[(df['age'] > 20) & (df['grade'] >= 90)]

# Students from Boston OR New York
df.loc[df['city'].isin(['Boston', 'New York'])]

# Students over 22 OR with grade >= 95 
df.loc[(df['age'] > 22) | (df['grade'] >= 95)]
```

**Tasks**:
- Select students over 21 years old who have a grade of 85 or higher and are not from New York.
	- Expected output: A DataFrame with students who meet all three conditions.
- Select students from either 'Los Angeles' or 'San Francisco' with grades above 80 and who are under 25 years old.
	- Expected output: A DataFrame with students who meet all three conditions.
- Find students who are under 23 years old, not from Chicago, and have a grade between 70 and 90.
	- Expected output: A DataFrame with students who meet all three conditions.
- Find students who are either from Boston or have a grade above 95, and are also over 18 years old.
	- Expected output: A DataFrame with students who meet all three conditions.

## 3. Sorting Data
### sort_values()
```python
# Sort by age
df.sort_values('age')

# Sort by multiple columns
df.sort_values(['city', 'grade'], ascending=[True, False])
```

- **Tasks**:
 1. Sort the DataFrame by age in ascending order.
 - Expected output: A DataFrame ordered as Sarah, John, Peter, Anna, Michael
 2. Sort the DataFrame by city in ascending order and grade in descending order.
 - Expected output: A DataFrame where Boston entries are first (Sarah then Anna), followed by Chicago (Peter), then New York (Michael then John)
 3. Sort the DataFrame by grade in descending order and reset the index.
 - Expected output: A DataFrame ordered by grade (highest to lowest) with new index values starting from 0

## 4. The filter() Method
```python
# Use filter(like) to select columns containing a specific substring
# Select all columns with 'grade_math' in their name
math_grades = df.filter(like='grade_math')
print("Math grades columns:")
print(math_grades.head())

# Use filter(regex) with more complex pattern matching
# Select all columns for 2023 data
data_2023 = df.filter(regex='_2023_Q[0-9]')
print("\n2023 data columns:")
print(data_2023.head())

# Select all midterm grades with regex
midterm_grades = df.filter(regex='grade_.*_midterm')
print("\nMidterm grades:")
print(midterm_grades.head())
```

**Practice Problem: Using filter()**
- **Tasks**:
 1. Use `filter(like)` to select all math-related grade columns.
 - Expected output: A DataFrame with all rows and only the grade_math_midterm and grade_math_final columns
 2. Use `filter(regex)` to select all columns that end with '_final'.
 - Expected output: A DataFrame with all rows and only the grade_math_final and grade_physics_final columns
 3. Use `filter(regex)` to select all score columns from 2023.
 - Expected output: A DataFrame with all rows and only the scores_2023_Q1 and scores_2023_Q2 columns
 4. Use `filter(regex)` to select all midterm and lab columns.
 - Expected output: A DataFrame with all rows containing grade_math_midterm, grade_physics_midterm, and grade_chemistry_lab columns

### Automatic dtype inference and selection

#### 1. Automatically convert columns to best dtypes
```python
# Convert all columns to the best possible dtypes (e.g., string, Int64, boolean, category)
df = df.convert_dtypes()
print(df.dtypes)
```
- This makes your DataFrame more memory efficient and enables use of modern pandas features (like nullable types and better string handling).

#### 2. Select columns by dtype
```python
# Select all numeric columns
df_numeric = df.select_dtypes(include='number')
print(df_numeric.head())

# Select all string columns
df_string = df.select_dtypes(include='string')
print(df_string.head())

# Select all boolean columns
df_bool = df.select_dtypes(include='boolean')
print(df_bool.head())

# Select all categorical columns (if any)
df_cat = df.select_dtypes(include='category')
print(df_cat.head())
```
- This is useful for quickly filtering columns for analysis, plotting, or further processing.

## More Practice Problems

**Practice Problem 1: Combining Multiple Techniques**

Use the same DataFrame provided at the beginning of the lesson:

- **Tasks**:
 1. Use `convert_dtypes()` on the DataFrame and print the resulting dtypes.
 3. Select all string columns using and print the result.
 5. Select all students who are either from Boston or have a math grade above 90, then sort them by age.
 - Expected output: A sorted DataFrame with Anna, Sarah, and Michael (meeting the condition)
 6. Select all grade columns using the filter method, then calculate the average of each student across all subjects.
 - Expected output: A Series with the average grades for each student
 7. Find students whose math grade is higher than their physics grade, and display only their name and both grades.
 - Expected output: A DataFrame with John, Peter, and Sarah (who have higher math than physics grades)
 8. Find students whose name starts with 'P' or 'S'.
 - Expected output: A DataFrame with Peter and Sarah

**Key Questions:**

What is the difference between `loc` and `iloc` indexing methods in Pandas?
?
- `loc` is label-based indexing that uses the row and column labels (index values) to select data
- `iloc` is integer position-based indexing that uses the row and column positions (0-based integers) to select data

What exactly is a boolean mask in pandas, how is it created and used?
?
- A boolean mask is a Series of True/False values with the same index as the DataFrame
- Created by applying a condition to a DataFrame column: `mask = df['age'] > 20`
- The mask can be used to filter rows and columns when applied within `.loc()`: `df.loc[mask]`

How do you combine multiple conditions in Boolean indexing (and/or/NOT)
?
- Use `&` for AND conditions: `df.loc[(df['age'] > 20) & (df['grade'] >= 90)]`
- Use `|` for OR conditions: `df.loc[(df['age'] > 22) | (df['grade'] >= 95)]`
- Use `~` for NOT conditions: `df.loc[~(df['city'] == 'Chicago')]`

5. What are different ways to select specific columns in a DataFrame? 
 Consider methods that:
 - Use label-based indexing
 - Use index-based indexing
 - Filter based on column name patterns 
 - Filter only numeric columns
 - Select all except of 2 columns
?
- Using `loc`: `df.loc[:, ['col1', 'col2']]`
- Using `iloc`: `df.iloc[:, 5:]`
- Using `filter` method: `df.filter(like = grade')` or `df.loc[:, df.columns.str.startswith('grade')]` 
- Using data types: `df.select_dtypes(include=['int64', 'float64'])`
- Excluding columns: `df.loc[:, ~df.columns.isin(['name', 'city'])]`

How do you sort values within the dataframe? How do you switch the order (ascending/descending)?
?
- `sort_values()` method
- `sort_values(..., ascending = True/False)`

How does the `filter()` method work and what are its different approaches?
?
- `filter(like='string')`: Selects columns containing the specified substring
- `filter(regex='pattern')`: Selects columns matching the regular expression pattern

What does `convert_dtypes()` do in pandas? Why is it useful?
?
- It automatically converts columns to the best possible dtype (e.g., string, Int64, boolean, category), making the DataFrame more memory efficient and enabling modern pandas features.

How do you select all columns of a specific dtype (e.g., numeric, string, boolean, category) in a DataFrame?
?
- Use `df.select_dtypes(include='number')` for numeric, `include='string'` for string, `include='boolean'` for boolean, and `include='category'` for categorical columns.
