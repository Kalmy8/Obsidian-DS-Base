**Codewords:** DataFrame, Series, CSV Loading, DataFrame Information Methods, Data Import

## 1. Loading Data with Pandas

Pandas is a powerful data manipulation library that makes it easy to work with structured data. There are multiple ways to load data:

### CSV Files
```python
import pandas as pd

# Load .csv with comprehensive parameters
df = pd.read_csv('data.csv', 
                 sep=',',                       # Column delimiter in the CSV file
                 header=0,                      # Which row to use for column names (0-based)
                 index_col='id',                # Column to use as DataFrame index
                 usecols=['col1', 'col2'],     # List of columns to read (others will be ignored)
                 nrows=100,                     # Number of rows to read from the file
                 skiprows=[0, 2],               # List of row indices to skip
                 na_values=['NA', 'Missing'],   # Values to treat as NaN
                 true_values=['yes'],           # Values to interpret as True
                 false_values=['no'],           # Values to interpret as False
                 skipinitialspace=True,         # Remove leading spaces after delimiter
                 parse_dates=['date_col'],      # Columns to parse as datetime
                 encoding='utf-8',              # File encoding (always use UTF-8)
                 converters={'col1': lambda x: x.upper()},  # Custom value conversions per column
                 on_bad_lines='skip',           # How to handle lines with parsing errors
                 chunksize=50)                  # Read file in chunks of this size
                                               # Returns TextFileReader for iteration
```

**Mock CSV Entry for Practice Problems:**

  ```plaintext
  id,name,age,grade,city,date_joined,active
  1,John,20,85,New York,2023-01-01,yes
  2,Anna,22,NA,Boston,2023-01-15,no
  3,Peter,21,Missing,Chicago,2023-02-01,yes
  4,Sarah,19,95,Boston,2023-03-01,yes
  5,Michael,20,88,Chicago,2023-04-01,NA
  6,Emma,22,Missing,New York,2023-05-01,yes
  ```

**Task 1**:
  1. Load the CSV file using `pd.read_csv()` with the following parameters:
     - Use the second row as column names.
     - Set 'id' as the index column.
     - Read only 'name', 'age', and 'date_joined' columns.
     - Limit the data to the first 5 rows using `nrows`.
     - Skip the first row.
     - Parse 'date_joined' as a date.

**Task 2: Handling Boolean and NA Values**
  1. Load the CSV file with the following settings:
     - Define `true_values` as ['yes'] and `false_values` as ['no'] for the 'active' column.
     - Define `na_values` as ['NA', 'Missing'] for missing data.

**Task 3: Converters and Chunking**
  1. Load the CSV file using `pd.read_csv()` with the following settings:
     - Convert the 'name' column to uppercase.
     - Load the data in chunks of 2 rows.

**Task 4: Handling Special Cases**

For this task, use another CSV Mock:
  ```plaintext
  id|  name|  age|  grade|  city
  1|  John|  20|  85|  New York
  2|  Аnna|  22|  92|  Boston
  3|  Peter|  21|  78|  Chicago
  4|  Sarah|  19|  95|  Boston
  5|  Michael|  20|  88|  Chicago
  6|  Emma|  22|  91|  New York
  7|  Invalid|  Data|  Here
  8|  Bad,Line,Format
  9|  Incomplete|  Row
  ```
  1. Load the CSV file with the following settings:
     - Use custom separator for pipe-delimited data.
     - Handle unnecessary spaces.
     - Show warning on bad lines using.

### Other Data Formats

While we'll focus primarily on CSV files, Pandas can also load data from many other formats:
1. Excel files: `pd.read_excel('data.xlsx')`
2. JSON files: `pd.read_json('data.json')`
3. SQL databases: `pd.read_sql('SELECT * FROM table', connection)`

## 2. DataFrame and Series Objects
### DataFrame
A DataFrame is a **2-dimensional labeled data structure**. Think of it as an Excel spreadsheet:
- Columns can have different types (int, float, string, etc.)
- Both rows and columns have labels/indexes
- Size-mutable: you can add/remove rows and columns

```python
# Creating a DataFrame
data = {
    'name': ['John', 'Anna', 'Peter'],
    'age': [28, 22, 35],
    'city': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)

# Accessing DataFrame attributes
print(df.shape)        # (rows, columns)
print(df.size)         # Total number of elements
print(df.dtypes)       # Data types of each column
```

### Series

A Series is a **1-dimensional labeled array** that can hold data of any type:
```python
# Creating a Series
ages = pd.Series([28, 22, 35], name='age')

# Creating with custom index
cities = pd.Series(['New York', 'Paris', 'London'], index=['John', 'Anna', 'Peter'])

# Accessing Series attributes
print(ages.shape)     # (n,) where n is length
print(ages.size)      # Length of Series
print(ages.dtype)     # Data type
```

Series objects have many useful methods not directly available on DataFrames (or that work differently):

```python
# Example Series (imagine this came from df['column_name'])
s = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'], name='fruits')

# Count occurrences of each unique value
print("\nValue Counts:")
print(s.value_counts())
# apple     3
# banana    2
# orange    1
# Name: fruits, dtype: int64

# Get unique values
print("\nUnique Values:")
print(s.unique()) # ['apple' 'banana' 'orange']

# Get the number of unique values
print("\nNumber of Unique Values:")
print(s.nunique()) # 3

# Check for membership
print("\nIs 'apple' in Series?")
print(s.isin(['apple']))
# 0     True
# 1    False
# 2     True
# 3    False
# 4    False
# 5     True
# Name: fruits, dtype: bool

# String operations (using .str accessor)
string_series = pd.Series(['First Last', 'John Doe', 'Jane Smith'], name='full_names')
print("\nString Operations (First Word):")
print(string_series.str.split(' ').str[0])
# 0    First
# 1     John
# 2     Jane
# Name: full_names, dtype: object
```

## 3. Basic Information Methods (both for DF and Series)
### describe()
Provides statistical summary of numerical columns:
```python
df.describe()  # Shows count, mean, std, min, 25%, 50%, 75%, max

# Include non-numeric columns
df.describe(include='all')

# Specific statistics
df.describe(percentiles=[0.05, 0.5, 0.95])
```

### info()
Shows DataFrame information including:
- Total rows and columns
- Column names and data types
- Memory usage
- Non-null counts

```python
df.info()

# Customize display
df.info(verbose=True, memory_usage='deep')
```

### Other Useful Methods
```python
# First/last 5 rows
df.head()
df.tail()

# Sample random rows
df.sample(n=3)  # 3 random rows
df.sample(frac=0.1)  # 10% of rows
df.sample(frac=1)  # Often used for dataset shuffling

```

### Practice Problems:

#####  Task 1: Dataframe

Create a sample DataFrame from a python dictionary: 
```python
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [25, None, 28, 19, 23],
    'city': ['New York', 'Boston', None, 'Boston', 'New York'],
    'salary': [50000, 45000, 65000, None, 55000],
    'experience': [2, 1, None, 0, 3],
    'department': ['Sales', 'Marketing', 'Engineering', None, 'Marketing'],
    'is_manager': [True, False, True, None, False],
    'performance_rating': ['Good', 'Excellent', None, 'Good', 'Excellent']
}
```

Given this dataframe:
- Observe:
	- shape, 
	- number of entries,
	- memory usage,
	- number of missing values for each column,
	- data types,
	- few first and last entries,
	- descriptive statistics
- Count the number of missing values in each column
- Retrieve a shuffled version of a dataset


##### Task 2: Series

```python
import pandas as pd
import numpy as np

data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael'],
    'age': [25, np.nan, 28, 19, 23],
    'city': ['New York', 'Boston', np.nan, 'Boston', 'New York'],
    'salary': [50000, 45000, 65000, np.nan, 55000],
    'experience': [2, 1, np.nan, 0, 3],
    'department': ['Sales', 'Marketing', 'Engineering', np.nan, 'Marketing'],
    'is_manager': [True, False, True, np.nan, False],
    'performance_rating': ['Good', 'Excellent', np.nan, 'Good', 'Excellent']
}
df_practice = pd.DataFrame(data)
print("Original Practice DataFrame for Series Operations:")
print(df_practice)
```

**City Analysis**:
-   Select the 'city' column as a Series 
  (hint: `df_practice.loc[:, 'city']`)
-   How many unique cities are there? (Print the number)
-   What are the unique city names? (Print the array of unique names)
-   What is the frequency of each city? (Print the counts)

 **Department Analysis**:
  -   Select the 'department' column as a Series.
    (hint: `df_practice.loc[:, 'department']`)
  -   What is the most frequent department?
  -   How many employees are in the 'Marketing' department?
 
 **Performance Rating Transformation**:
  -   Select the 'performance_rating' column as a Series
    (hint: `df_practice.loc[:, 'performance_rating']`).
  -   Convert all performance ratings to lowercase and print the resulting Series.
  -   Check which original ratings were 'Excellent' (resulting in a boolean Series).


#🃏/pandas-basics

**Key Questions:**

When loading CSV files with pandas, several problems may occur:
- Selective file upload (delimiters, headers, column selection, index columns)
- Data volume (large files, partial loading)
- Data cleaning (missing values, transformations, redundant spaces, boolean values)
- Special data types (dates, encodings)
- Error handling (lines with errors)
What `read_csv()` parameters can help you solving them?
?
  - `sep`, `header`, `usecols`, `index_col`: These parameters help manage unusual file structures by specifying delimiters, headers, selecting specific columns, and setting index columns.
  - `nrows`, `chunksize`: These parameters assist in handling large files by limiting the number of rows read and processing the file in chunks.
  - `na_values`, `converters`, `skipinitialspace`, `true_values`, `false_values`: These parameters aid in data cleaning by defining missing value indicators, applying transformations, ignoring spaces after delimiters, and specifying boolean values.
  - `parse_dates`, `encoding`: These parameters handle special data types by parsing dates and specifying file encoding.
  - `on_bad_lines`: This parameter manages lines with errors, such as skipping or warning.

How to create a DataFrame of a python dictionary?
?
- By passing that dictionary inside `pd.DataFrame()` method

How do the `info()` and `describe()` methods differ in terms of the information they provide about a DataFrame?
?
- The `info()` method provides a concise summary of a DataFrame, including the number of non-null entries, data types, and memory usage. 
- The `describe()` method, on the other hand, provides a statistical summary of numerical columns (count, mean, percentiles...)

What are the main differences between a DataFrame and a Series in Pandas?
?
- A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types, similar to a spreadsheet or SQL table. 
- A Series is a 1-dimensional labeled array capable of holding any data type. 
- Essentially, a DataFrame is a collection of Series.
- Series and DataFrame has different methods

What are some common Series methods which are not available for DataFrame?
- To get frequency counts of unique values
- To get the count of unique values
- To check for membership
- For vectorized string operations (switching case, splitting)
- For datetime operations
?
- s.value_counts()
- s.nunique() 
- s.isin([...])
- .str accessor 
- .dt accessor

What are the `.size`, `.shape` attributes of a DataFrame and Series objects, such as size and shape, and how can they be accessed?
?
- The `shape` attribute returns a tuple representing the dimensionality, 
- `size` returns the number of elements

Why would you use `df.sample(frac=1)` line?
?
- It is often used to shuffle dataframe, as it returns all the same rows in a random order