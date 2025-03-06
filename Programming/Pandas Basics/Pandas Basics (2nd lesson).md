**Codewords:** Boolean Indexing, Advanced loc/iloc, Multiple Conditions, Sorting, Filter Method

## 1. Basic Indexing with loc and iloc
### loc - Label-based indexing
```python
import pandas as pd

# Create a sample DataFrame
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)
print(df)
```

Label-based indexing with `loc`:
```python
# Select single row by label
df.loc[0]  

# Select multiple rows and columns by label
df.loc[0:2, ['name', 'age']]
```

**Practice Problem: loc Indexing**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Select the row with index 2 using `loc`. 
     - Expected output: A Series with Peter's information
  2. Select rows with indexes 1 through 3 and only the 'name' and 'grade' columns.
     - Expected output: A DataFrame with 3 rows (Anna, Peter, Sarah) and 2 columns (name, grade)


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

**Practice Problem: iloc Indexing**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Use `iloc` to select the last row of the DataFrame.
  2. Select the first 3 rows and first 2 columns using `iloc`.
  3. Select the values at positions [0,1] and [2,3] (row, column) using `iloc`.

### Direct column and row access
```python
# Access single column (returns Series)
df['name']

# Access multiple columns (returns DataFrame)
df[['name', 'age']]

# Access rows by slicing
df[0:2]  # First two rows
```

**Practice Problem: Direct Access**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Extract the 'grade' column as a Series.
     - Expected output: A Series with values [85, 92, 78, 95, 88]
 
  2. Extract the 'grade' column as a Dataframe.
    
  3. Create a new DataFrame from the old one with only the 'name', 'age', and 'city' columns.
     - Expected output: A DataFrame with all rows but only the name, age, and city columns
     
  4. Extract the first 3 rows using direct slicing.
     - Expected output: A DataFrame with the first 3 rows (John, Anna, Peter)

> Note! Direct access should be avoided. Always use loc/iloc instead!

## 2. Advanced Indexing with loc and iloc
### Boolean Indexing
```python
# Create a sample DataFrame
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)

# Select all students with age > 20
df.loc[df['age'] > 20]

# Select all students whose name starts with 'A'
a_names = df.loc[df['name'].str.startswith('A')]
```

**Practice Problem: Boolean Indexing**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Select all students with an age greater than 20.
     - Expected output: A DataFrame with Anna, Peter, and Michael
  2. Identify students with a grade of 90 or higher and create a new DataFrame.
     - Expected output: A DataFrame with Anna and Sarah
  3. Find all students from 'Boston'.
     - Expected output: A DataFrame with Anna and Sarah
  4. Find all students whose name ends with 'h'.
     - Expected output: A DataFrame with Sarah

### Understanding Boolean Masks
A boolean mask is a Series or DataFrame of the same shape as your original DataFrame, but containing only `True` and `False` values. These masks are the foundation of boolean indexing.

```python
# Create a sample DataFrame
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)

# Create a boolean mask
mask = df['age'] > 20
print("Boolean mask:")
print(mask)

# Using the mask to filter the DataFrame
filtered_df = df[mask]  # Equivalent to df.loc[mask]
print("\nFiltered DataFrame:")
print(filtered_df)
```

**Practice Problem: Working with Boolean Masks**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Create a boolean mask for students with grades above 85 and print the mask.
     - Expected output: A Series with [False, True, False, True, True]
  
  2. Create a mask for students whose names contain the letter 'e', then use it to filter the DataFrame.
     - Expected output: A DataFrame with Peter and Michael
  
  3. Create two masks: one for age > 20 and another for grade > 90. Print both masks side by side with the original data.
     - Expected output: DataFrame with original data plus two boolean columns

### Multiple Conditions
Combine conditions using & (and) and | (or):
```python
# Create a sample DataFrame
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)

# Students over 20 AND with grade >= 90
df.loc[(df['age'] > 20) & (df['grade'] >= 90)]

# Students from Boston OR New York
df.loc[df['city'].isin(['Boston', 'New York'])]

# Students over 22 OR with grade >= 95 
df.loc[(df['age'] > 22) | (df['grade'] >= 95)]
```

**Practice Problem: Multiple Conditions**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Select students over 20 years old who also have a grade of 90 or higher.
     - Expected output: A DataFrame with only Anna
  2. Select students from either 'Boston' or 'New York' with grades above 85.
     - Expected output: A DataFrame with Anna, Sarah, and Michael
  3. Find students who are under 21 years old and not from Chicago.
     - Expected output: A DataFrame with John and Sarah
  4. Find students who are either from Boston or have a grade above 90.
     - Expected output: A DataFrame with Anna, Sarah

### Advanced Column Selection
```python
# Create a sample DataFrame with more grade columns
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade_math': [85, 92, 78, 95, 88],
    'grade_physics': [80, 95, 75, 90, 85],
    'grade_chemistry': [90, 85, 80, 92, 95],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)

# Select columns that start with 'grade'
df.loc[:, df.columns.str.startswith('grade')]

# Select numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df.loc[:, numeric_cols]

# Select all columns except 'name' and 'city'
df.loc[:, ~df.columns.isin(['name', 'city'])]
```

**Practice Problem: Advanced Column Selection**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade_math': [85, 92, 78, 95, 88],
    'grade_physics': [80, 95, 75, 90, 85],
    'grade_chemistry': [90, 85, 80, 92, 95],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Select all columns that start with 'grade'.
     - Expected output: A DataFrame with all rows and only the grade_math, grade_physics, and grade_chemistry columns
  2. Select all numeric columns in the DataFrame.
     - Expected output: A DataFrame with all rows and the age, grade_math, grade_physics, and grade_chemistry columns
  3. Select only the string columns in the DataFrame.
     - Expected output: A DataFrame with all rows and the name and city columns
  4. Select all columns except 'name' and 'grade_math'.
     - Expected output: A DataFrame with all rows and the age, grade_physics, grade_chemistry, and city columns

## 3. Sorting Data
### sort_values()
```python
# Create a sample DataFrame
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)

# Sort by age
df.sort_values('age')

# Sort by multiple columns
df.sort_values(['city', 'grade'], ascending=[True, False])
```

**Practice Problem: Sorting with sort_values()**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Sort the DataFrame by age in ascending order.
     - Expected output: A DataFrame ordered as Sarah, John, Peter, Anna, Michael
  2. Sort the DataFrame by city in ascending order and grade in descending order.
     - Expected output: A DataFrame where Boston entries are first (Sarah then Anna), followed by Chicago (Peter), then New York (Michael then John)
  3. Sort the DataFrame by grade in descending order and reset the index.
     - Expected output: A DataFrame ordered by grade (highest to lowest) with new index values starting from 0

### sort_index()
```python
# Create a DataFrame with custom index
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88]
}
df = pd.DataFrame(data, index=['E', 'A', 'C', 'B', 'D'])

# Sort by index
df.sort_index()

# Sort by column index
df.sort_index(axis=1)
```

**Practice Problem: Sorting with sort_index()**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade': [85, 92, 78, 95, 88]
}
df = pd.DataFrame(data, index=['E', 'A', 'C', 'B', 'D'])
```
- **Tasks**:
  1. Sort the DataFrame by its index in ascending order.
     - Expected output: A DataFrame ordered as A (Anna), B (Sarah), C (Peter), D (Michael), E (John)
  2. Sort the DataFrame by its index in descending order.
     - Expected output: A DataFrame ordered as E (John), D (Michael), C (Peter), B (Sarah), A (Anna)
  3. Sort the DataFrame columns alphabetically.
     - Expected output: A DataFrame with columns ordered as 'age', 'grade', 'name'

## 4. The filter() Method
```python
# Create a sample DataFrame with more complex column naming patterns
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
}
df = pd.DataFrame(data)

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
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    # Grade columns with course prefix
    'grade_math_midterm': [85, 92, 78, 95, 88],
    'grade_math_final': [88, 95, 80, 98, 90],
    'grade_physics_midterm': [80, 95, 75, 90, 85],
    'grade_physics_final': [82, 90, 78, 88, 87],
    'grade_chemistry_lab': [90, 85, 80, 92, 95],
    # Data columns with year and period suffixes
    'scores_2023_Q1': [88, 91, 79, 94, 86],
    'scores_2023_Q2': [90, 93, 81, 96, 89],
    'scores_2022_Q4': [84, 89, 77, 91, 85],
    # Measurement columns
    'height_cm': [175, 165, 180, 168, 190],
    'weight_kg': [70, 58, 75, 60, 80]
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Use `filter(like='grade_math')` to select all math-related grade columns.
     - Expected output: A DataFrame with all rows and only the grade_math_midterm and grade_math_final columns
  
  2. Use `filter(regex)` to select all columns that end with '_final'.
     - Expected output: A DataFrame with all rows and only the grade_math_final and grade_physics_final columns
  
  3. Use `filter(regex)` to select all score columns from 2023.
     - Expected output: A DataFrame with all rows and only the scores_2023_Q1 and scores_2023_Q2 columns
  
  4. Use `filter(regex)` to select all midterm and lab columns.
     - Expected output: A DataFrame with all rows containing grade_math_midterm, grade_physics_midterm, and grade_chemistry_lab columns

## 5. Comprehensive Practice Problems

**Practice Problem 1: Combining Multiple Techniques**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade_math': [85, 92, 78, 95, 88],
    'grade_physics': [80, 95, 75, 90, 85],
    'grade_chemistry': [90, 85, 80, 92, 95],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Select all students who are either from Boston or have a math grade above 90, then sort them by age.
     - Expected output: A sorted DataFrame with Anna, Sarah, and Michael (meeting the condition)
  2. Select all grade columns using the filter method, then calculate the average of each student across all subjects.
     - Expected output: A Series with the average grades for each student
  3. Find students whose math grade is higher than their physics grade, and display only their name and both grades.
     - Expected output: A DataFrame with John, Peter, and Sarah (who have higher math than physics grades)

**Practice Problem 2: Advanced Selection**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [20, 22, 21, 19, 23],
    'grade_math': [85, 92, 78, 95, 88],
    'grade_physics': [80, 95, 75, 90, 85],
    'grade_chemistry': [90, 85, 80, 92, 95],
    'city': ['New York', 'Boston', 'Chicago', 'Boston', 'New York']
}
df = pd.DataFrame(data)
```
- **Tasks**:
  2. Find students whose name starts with 'P' or 'S'.
     - Expected output: A DataFrame with Peter and Sarah
  3. Identify the top student in each city (highest math grade).
     - Expected output: A Series or DataFrame showing the student with highest math grade in each city


#🃏/pandas-basics

**Key Questions:**

1. What is the difference between `loc` and `iloc` indexing methods in Pandas?
?
- `loc` is label-based indexing that uses the row and column labels (index values) to select data
- `iloc` is integer position-based indexing that uses the row and column positions (0-based integers) to select data

2. How do you use Boolean indexing to filter rows in a DataFrame?
?
- Create a Boolean mask by applying a condition to a column: `df['age'] > 20`
- Use the mask with `loc` to filter rows: `df.loc[df['age'] > 20]`
- For string operations, use string methods: `df.loc[df['name'].str.startswith('A')]`
- The result includes only rows where the condition evaluates to True

3. What exactly is a boolean mask in pandas, how is it created and used?
?
- A boolean mask is a Series of True/False values with the same index as the DataFrame
- Created by applying a condition to a DataFrame column: `mask = df['age'] > 20`
- The mask can be used to filter rows and columns: `df.loc[mask]`

4. How do you combine multiple conditions in Boolean indexing (and/or/NOT)
?
- Use `&` for AND conditions: `df.loc[(df['age'] > 20) & (df['grade'] >= 90)]`
- Use `|` for OR conditions: `df.loc[(df['age'] > 22) | (df['grade'] >= 95)]`
- Use `~` for NOT conditions: `df.loc[~(df['city'] == 'Chicago')]`

5. What are different ways to select specific columns in a DataFrame? 
   Consider methods that:
   - Use label-based indexing
   - Filter based on column name patterns
   - Filter based on data types
   - Exclude certain columns
?
- Using `loc`: `df.loc[:, ['col1', 'col2']]`
- Using string methods: `df.loc[:, df.columns.str.startswith('grade')]` 
- Using data types: `df.select_dtypes(include=['int64', 'float64'])`
- Excluding columns: `df.loc[:, ~df.columns.isin(['name', 'city'])]`

6. What is the difference between `sort_values()` and `sort_index()` methods?
?
- `sort_values()` sorts the DataFrame by the values in specified columns
- `sort_index()` sorts the DataFrame by the row or column index/labels
- `sort_values()` parameters include: 'by' (column names), 'ascending' (True/False), 'inplace' (True/False)
- `sort_index()` parameters include: 'axis' (0 for rows, 1 for columns), 'ascending' (True/False), 'inplace' (True/False)

7. How does the `filter()` method work and what are its different approaches?
?
- `filter(like='string')`: Selects columns containing the specified substring
- `filter(regex='pattern')`: Selects columns matching the regular expression pattern
