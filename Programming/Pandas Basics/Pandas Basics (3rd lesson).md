**Codewords:** Data Quality, Missing Values, Outliers, Data Profiling, Data Cleaning, Data Types

## 1. Data Quality Assessment
### Basic Data Quality Checks
```python
# Check for missing values
print(df.isnull().sum())

# Calculate percentage of missing values
missing_percent = (df.isnull().sum() / len(df)) * 100

# Check data types
print(df.dtypes)

# Check for duplicates
print(df.duplicated().sum())

# Basic statistics
print(df.describe())

# Unique values in categorical columns
print(df['category'].value_counts())
print(df['category'].nunique())  # Number of unique values
```

**Practice Problem: Data Quality Checks**
- Check for missing values in a DataFrame and calculate the percentage of missing values.
- Identify the data types of each column and check for duplicates.
- Generate a basic statistical summary and count unique values in a categorical column.

### Using ydata-profiling
```python
import pandas as pd
from ydata_profiling import ProfileReport

# Generate a profile report
profile = ProfileReport(df, title="Data Quality Report")
profile.to_file("report.html")

# Minimal report for large datasets
profile = ProfileReport(df, minimal=True)
```

## 2. Handling Missing Values
### Detection and Analysis
```python
# Find missing values
missing = df.isnull()

# Calculate percentage of missing values
missing_percent = (df.isnull().sum() / len(df)) * 100

# Visualize missing values pattern
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(df.isnull(), yticklabels=False, cbar=True)
plt.title('Missing Value Pattern')
plt.show()

# Check for correlation between missing values
missing_corr = df.isnull().corr()
```

**Practice Problem: Missing Data Imputation**
- Analyze the pattern of missing values in a DataFrame.
- Implement multiple imputation strategies: mean, median, mode, forward fill, backward fill, and interpolation.
- Compare the results of different imputation methods and evaluate which method preserves the original data distribution best.

### Handling Strategies
```python
# Drop rows with any missing values
df_clean = df.dropna()

# Drop rows with missing values in specific columns
df_clean = df.dropna(subset=['important_column'])

# Drop rows with all missing values
df_clean = df.dropna(how='all')

# Fill missing values with a specific value
df['column'].fillna(0)

# Fill with mean/median/mode
df['age'].fillna(df['age'].mean())
df['category'].fillna(df['category'].mode()[0])

# Forward/backward fill
df['value'].fillna(method='ffill')  # forward fill
df['value'].fillna(method='bfill')  # backward fill

# Interpolation
df['value'].interpolate(method='linear')
```

## 3. Handling Outliers
### Detecting Outliers
```python
import numpy as np
import matplotlib.pyplot as plt

# Visual detection
plt.boxplot(df['value'])
plt.title('Boxplot for Outlier Detection')
plt.show()

# Using Z-score
from scipy import stats
z_scores = stats.zscore(df['value'])
outliers_z = np.abs(z_scores) > 3
print(f"Z-score outliers: {outliers_z.sum()}")

# Using IQR
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_iqr = (df['value'] < lower_bound) | (df['value'] > upper_bound)
print(f"IQR outliers: {outliers_iqr.sum()}")

# Compare methods
plt.figure(figsize=(10, 6))
plt.scatter(range(len(df)), df['value'], c=['red' if x else 'blue' for x in outliers_z], label='Z-score')
plt.scatter(range(len(df)), df['value'], c=['green' if x else 'blue' for x in outliers_iqr], alpha=0.5, label='IQR')
plt.legend()
plt.title('Outlier Detection Comparison')
plt.show()
```

**Practice Problem: Outlier Detection and Handling**
- Identify outliers using both Z-score and IQR methods.
- Compare the results of both methods and create a summary of outliers by category.
- Handle outliers using different methods (removal, capping, etc.) and visualize the distribution before and after outlier treatment.

### Handling Outliers
```python
# Remove outliers
df_clean = df[~outliers_iqr]

# Cap outliers
df['value_capped'] = df['value'].clip(lower=lower_bound, upper=upper_bound)

# Replace with boundaries
df.loc[df['value'] > upper_bound, 'value_boundary'] = upper_bound
df.loc[df['value'] < lower_bound, 'value_boundary'] = lower_bound

# Replace with NaN and then interpolate
df.loc[outliers_iqr, 'value_interp'] = np.nan
df['value_interp'] = df['value_interp'].interpolate()
```

## 4. Data Type Issues
### Converting Data Types
```python
# Convert to numeric
df['value'] = pd.to_numeric(df['value'], errors='coerce')  # 'coerce' turns invalid values to NaN

# Convert to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Convert categories
df['category'] = df['category'].astype('category')

# Memory optimization with categories
df['high_cardinality'] = df['high_cardinality'].astype('category')

# Get memory usage
df.memory_usage(deep=True)
```

**Practice Problem: Data Type Conversion**
- Convert columns to appropriate data types, including numeric and datetime.
- Optimize memory usage by converting high cardinality columns to categorical types.
- Clean numeric strings and extract numeric values from mixed-type columns.

### Handling Mixed Types
```python
# Clean numeric strings
df['value'] = df['value'].str.replace('$', '').str.replace(',', '')
df['value'] = pd.to_numeric(df['value'], errors='coerce')

# Extract numeric values
df['number'] = df['mixed_column'].str.extract('(\d+)').astype(float)

# String cleaning
df['text'] = df['text'].str.strip().str.lower()
```

## 5. Duplicate Detection and Handling
```python
# Check for duplicate rows
duplicates = df.duplicated()
print(f"Number of duplicates: {duplicates.sum()}")

# Show duplicate rows
df[df.duplicated(keep=False)]  # keep=False shows all duplicates

# Drop duplicates
df_clean = df.drop_duplicates()

# Drop duplicates based on specific columns
df_clean = df.drop_duplicates(subset=['name', 'address'])

# Keep first/last occurrence
df_clean = df.drop_duplicates(keep='first')  # or 'last'
```

**Practice Problem: Duplicate Handling**
- Identify and remove duplicate rows in a DataFrame.
- Standardize date formats and create a new column with the months since joining.
- Calculate the total balance by month after converting balance strings to numeric values.

#🃏/pandas-basics
**Review Questions:**
1. What are the main strategies for handling missing values and when should each be used?
2. How do Z-score and IQR methods differ in detecting outliers?
3. What are the pros and cons of different outlier handling strategies?
4. How can you handle mixed data types in a column?
5. What are the key components of a data quality assessment?
6. How does data type conversion affect memory usage in pandas?
7. What is the difference between `fillna()` and `interpolate()`?
8. Why is it important to check for duplicates and what are the best practices for handling them? 