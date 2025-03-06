**Codewords:** DataFrame, Series, CSV Loading, DataFrame Information Methods, Data Import

## 1. Loading Data with Pandas
Pandas is a powerful data manipulation library that makes it easy to work with structured data. There are multiple ways to load data:

### CSV Files
```python
import pandas as pd

# Load .csv with comprehensive parameters
df = pd.read_csv('data.csv', 
                 sep=',',                # Delimiter 
                 header=0,               # Row to use as column names
                 index_col='id',         # Column to set as index
                 usecols=['col1', 'col2'],  # Only read specific columns
                 nrows=100,              # Read only first 100 rows
                 skiprows=[0, 2],        # Skip specific rows
                 na_values=['NA', 'Missing'],  # Custom NA values
                 converters={'col1': lambda x: x.upper()},  # Convert values in col1 to uppercase
                 true_values=['yes'],    # Values to consider as True
                 false_values=['no'],    # Values to consider as False
                 skipinitialspace=True,  # Skip spaces after delimiter
                 parse_dates=['date_col'],  # Parse date columns
                 chunksize=50,           # Read file in chunks of 50 rows
                 # Return TextFileReader object for iteration
                 encoding='utf-8',       # File encoding
                 on_bad_lines='skip')    # Skip lines with errors
```

**Practice Problem: Grouping and Indexing**
- **Mock CSV Entry**:
  ```plaintext
  student_id,student_name,student_age,student_grade,student_city,enrollment_date
  id,name,age,grade,city,date_joined
  1,John,20,85,New York,2023-01-01
  2,Anna,22,92,Boston,2023-01-15
  3,Peter,21,78,Chicago,2023-02-01
  4,Sarah,19,95,Boston,2023-03-01
  5,Michael,20,88,Chicago,2023-04-01
  6,Emma,22,91,New York,2023-05-01
  ```
- **Tasks**:
  1. Load the CSV file using `pd.read_csv()` with the following parameters:
     - Set `header` to 1 to use the second row as column names.
     - Set `index_col` to 'id'.
     - Use `usecols` to read only 'name', 'age', and 'date_joined'.
     - Limit the data to the first 5 rows using `nrows`.
     - Skip the first row using `skiprows`.
     - Parse 'date_joined' as a date using `parse_dates`.

**Practice Problem: Handling Boolean and NA Values**
- **Mock CSV Entry**:
  ```plaintext
  id,name,active,grade
  1,John,yes,85
  2,Anna,no,NA
  3,Peter,Missing,78
  4,Sarah,yes,95
  5,Michael,NA,88
  6,Emma,yes,Missing
  ```
- **Tasks**:
  1. Load the CSV file using `pd.read_csv()` with the following parameters:
     - Define `true_values` as ['yes'] and `false_values` as ['no'] for the 'active' column.
     - Define `na_values` as ['NA', 'Missing'] for missing data.

**Practice Problem: Converters and Chunking**
- **Mock CSV Entry**:
  ```plaintext
  id,name,age,grade
  1,John,20,85
  2,Anna,22,92
  3,Peter,21,78
  4,Sarah,19,95
  5,Michael,20,88
  6,Emma,22,91
  ```
- **Tasks**:
  1. Load the CSV file using `pd.read_csv()` with the following parameters:
     - Use `converters` to convert the 'name' column to uppercase.
     - Load the data in chunks of 2 rows using `chunksize`.

**Practice Problem: Handling Special Cases**
- **Mock CSV Entry**:
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
- **Tasks**:
  1. Load the CSV file using `pd.read_csv()` with the following parameters:
     - Use custom `sep` for pipe-delimited data.
     - Set `skipinitialspace=True` to handle extra spaces.
     - Handle bad lines using `on_bad_lines='warn'`.

### Other Data Formats

While we'll focus primarily on CSV files in our practice, Pandas can also load data from many other formats:

1. Excel files: `pd.read_excel('data.xlsx')`
2. JSON files: `pd.read_json('data.json')`
3. SQL databases: `pd.read_sql('SELECT * FROM table', connection)`


## 2. DataFrame and Series Objects
### DataFrame
A DataFrame is a 2-dimensional labeled data structure. Think of it as an Excel spreadsheet:
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


**Practice Problem: DataFrame Creation**
- **Tasks**:
  - Create a DataFrame from a dictionary and print its shape, size, and data types.

  
### Series
A Series is a 1-dimensional labeled array that can hold data of any type:
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

**Practice Problem: Series Exploration**
- **Tasks**:
  - Create a Series with a custom index and print its attributes.
  - Add a constant value to each element in the Series and print the result.


## 3. Basic Information Methods
### describe()
Provides statistical summary of numerical columns:
```python
df.describe()  # Shows count, mean, std, min, 25%, 50%, 75%, max

# Include non-numeric columns
df.describe(include='all')

# Specific statistics
df.describe(percentiles=[0.05, 0.5, 0.95])
```

**Practice Problem: Statistical Summary**
# Create a sample DataFrame
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
df = pd.DataFrame(data)
```

- **Tasks**:
  - Use `describe()` to obtain a statistical summary of a DataFrame.
  - Include non-numeric columns in the summary and interpret the results.
  - Calculate the 10th and 90th percentiles of a numeric column.

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

**Practice Problem: DataFrame Info**
- **Tasks**:
  - Use `info()` to display detailed information about a DataFrame.
  - Analyze the memory usage
  - Identify columns with missing values

### Other Useful Methods
```python
# First/last 5 rows
df.head()
df.tail()

# Sample random rows
df.sample(n=3)  # 3 random rows
df.sample(frac=0.1)  # 10% of rows
```

**Practice Problem: Data Exploration**
- **Tasks**:
  - Use `head()`, `tail()`, and `sample()` to explore a DataFrame.
  - Count the number of missing values in each column


#🃏/pandas-basics

**Key Questions:**

1. When loading CSV files with pandas, several problems may occur:
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

2. How do the `info()` and `describe()` methods differ in terms of the information they provide about a DataFrame?
?
- The `info()` method provides a concise summary of a DataFrame, including the number of non-null entries, data types, and memory usage. 
- The `describe()` method, on the other hand, provides a statistical summary of numerical columns (count, mean, percentiles...)

3. What are the main differences between a DataFrame and a Series in Pandas?
?
- A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types, similar to a spreadsheet or SQL table. 
- A Series is a 1-dimensional labeled array capable of holding any data type. 
- Essentially, a DataFrame is a collection of Series.

4. What are some basic attributes of DataFrame and Series objects, such as size and shape, and how can they be accessed?
?
- Basic attributes of DataFrame and Series objects include `shape`, `size`, and `dtypes`. The `shape` attribute returns a tuple representing the dimensionality, `size` returns the number of elements, and `dtypes` returns the data types of each column. These can be accessed using `df.shape`, `df.size`, and `df.dtypes` for a DataFrame, and similarly for a Series.


