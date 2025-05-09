**Codewords:** Data Quality, Missing Values, Outliers, Data Profiling, Data Cleaning, Data Types

## Basic Data Quality with ydata-profiling

ydata-profiling is a widely used 3rd-party python library, which allows you
to build handy and extensive html data reports with just several lines of code

```python
import pandas as pd
from ydata_profiling import ProfileReport

# Generate a profile report
profile = ProfileReport(df, title="Data Quality Report")
profile.to_file("report.html")

# Minimal report for large datasets 
# (only descriptive statistics)
profile = ProfileReport(df, minimal=True)

# Custom report configuration
# see more here: (https://docs.profiling.ydata.ai/latest/advanced_settings/available_settings/)

# Example 3: Performance-oriented configuration for large datasets
profile_large = ProfileReport(
    df,
    title="Large Dataset Report",
    minimal=True,                      # Enable minimal mode
    pool_size=4,                       # Use 4 CPU cores
    correlations=None,                 # Disable all correlations
    interactions={"continuous": False}, # Disable interaction plots
    vars={
        "num": {"low_categorical_threshold": 0},  # Disable categorical conversion
        "cat": {
            "characters": False,
            "words": False,
            "length": False
        }
    }
)
```

**ydata_profiling struggles to deal with really big (~15+ features/200k+ observations) datasets.**
- This problem can be usually solved by excluding pairwise interactions from the report, but sometimes that might not be enough
	- In such situations, I recommend you to form a random subsample of your data by using `df.sample(frac = ..., replace = False)`

When the report is ready, you should read it carefully, looking for several possible problems:
- Abnormal values
- Missing values
- Duplicated values
- Highly-correlated values
- Outliers
- Heavily skewed distributions 

## 1. Handling Abnormal Values

Abnormal values are values that can not be achieved in the real world, contradict the physical sense

For example:
- If you have a real-estate dataset, there might be negative/fractioned floor values like -1/3.5, which simply makes no sense
- If you are observing people weight/height dataset, there might be extraordinary (1000kg/500m) values, which are unachievable in real world

Such values usually occure in datasets by mistake, hence they should be considered MISSING, so we do inpute them with NaN's

## 2. Handling Outliers
### Detecting Outliers
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better visualizations
sns.set(style="whitegrid")

# Create a toy restaurant bill dataset
np.random.seed(42)  # For reproducibility

# Create normal distribution for most bills
normal_bills = np.random.normal(loc=20, scale=5, size=95)  # Mean $20, SD $5

# Add some outliers
outlier_bills = np.array([50, 65, 75, 120, 5])  # Very high and very low bills

# Combine data
bill_data = {
    'table_number': range(1, 101),
    'total_bill': np.concatenate([normal_bills, outlier_bills]),
    'day': np.random.choice(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], 100),
    'time': np.random.choice(['Lunch', 'Dinner'], 100),
    'size': np.random.choice([1, 2, 3, 4], 100, p=[0.2, 0.4, 0.3, 0.1])
}

# Create DataFrame
df = pd.DataFrame(bill_data)

# Display basic statistics
print("Dataset Statistics:")
print(df['total_bill'].describe())

# 1. Visual detection using boxplot
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y='total_bill', data=df)
plt.title('Boxplot of Restaurant Bills')
plt.ylabel('Bill Amount ($)')

# 2. Using IQR (Interquartile Range) method
# Calculate Q1, Q3, and IQR
Q1 = df['total_bill'].quantile(0.25)
Q3 = df['total_bill'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers_iqr = (df['total_bill'] < lower_bound) | (df['total_bill'] > upper_bound)
print(f"\nOutlier detection summary:")
print(f"Q1 (25th percentile): ${Q1:.2f}")
print(f"Q3 (75th percentile): ${Q3:.2f}")
print(f"IQR: ${IQR:.2f}")
print(f"Lower bound: ${lower_bound:.2f}")
print(f"Upper bound: ${upper_bound:.2f}")
print(f"Number of outliers detected: {outliers_iqr.sum()} ({outliers_iqr.sum()/len(df)*100:.1f}%)")
```

**Why are outliers important to detect?**

1. **They can skew statistics**: Mean and standard deviation are heavily influenced by extreme values
2. **They can bias models**: Machine learning algorithms can be pulled toward outliers
3. **They may indicate data quality issues**: Outliers might be errors that need correction
4. **They could represent important insights**: Some outliers reveal rare but important patterns

### Handling Outliers

Once detected, we have several options for handling outliers:

```python
# Option 1: Remove outliers
# Good when outliers are errors or not relevant to analysis
df_clean = df[~outliers_iqr]
print(f"Original dataset size: {len(df)}")
print(f"After removing outliers: {len(df_clean)}")

# Option 2: Cap outliers (Winsorization)
# Replaces extreme values with the boundary values
df['total_bill_capped'] = df['total_bill'].clip(lower=lower_bound, upper=upper_bound)

# Option 3: Log transformation to reduce impact of outliers
# Good for right-skewed data with positive values
df['total_bill_log'] = np.log1p(df['total_bill'])  # log1p avoids issues with zero values
```

**Let's compare all 3 options on the bill data above:**
```python
# Compare distributions after outlier treatment
plt.figure(figsize=(15, 5))

# Original data
plt.subplot(1, 3, 1)
sns.histplot(df['total_bill'], kde=True)
plt.title('Original Distribution')
plt.xlabel('Bill Amount ($)')

# Capped data
plt.subplot(1, 3, 2)
sns.histplot(df['total_bill_capped'], kde=True)
plt.title('Distribution after Capping')
plt.xlabel('Bill Amount ($)')

# Log-transformed data
plt.subplot(1, 3, 3)
sns.histplot(df['total_bill_log'], kde=True)
plt.title('Distribution after Log Transform')
plt.xlabel('Log(Bill Amount + 1)')

plt.tight_layout()
plt.show()

# Compare statistics
print("\nComparison of statistics:")
stats_df = pd.DataFrame({
    'Original': df['total_bill'].describe(),
    'After removing outliers': df_clean['total_bill'].describe(),
    'After capping': df['total_bill_capped'].describe(),
    'After log transform': df['total_bill_log'].describe()
})
print(stats_df)
```

**Practice Problem: Outlier Analysis**
```python
# Use this DataFrame for practice
np.random.seed(42)
data = {
    'product_id': range(1, 101),
    'price': np.concatenate([
        np.random.normal(50, 10, 95),   # Normal prices
        np.array([100, 125, 5, 8, 150])  # Outlier prices
    ]),
    'quantity': np.concatenate([
        np.random.poisson(lam=5, size=95),  # Normal quantities
        np.array([20, 25, 30, 0, 35])      # Outlier quantities
    ]),
    'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home'], 100)
}
df_products = pd.DataFrame(data)
```
- **Tasks**:
  1. Use boxplots to identify outliers in both price and quantity columns by category.
     - Expected output: Boxplots showing distribution of values across categories with outliers visible
  
  2. Apply the IQR method to detect outliers in the price column.
     - Expected output: A list of products with outlier prices and their details
  
  3. Handle outliers using two different methods:
     - Remove outliers and calculate mean price by category
     - Cap outliers and calculate mean price by category
     - Expected output: Comparison of category means before and after outlier treatment
  
  4. Create a visualization showing the distribution of prices:
     - Before outlier treatment
     - After removing outliers
     - After capping outliers
     - Expected output: Three histograms showing the effect of different treatments

# 3. Handling Missing Values

Let's create a dataset with some missing values:

```python
# Create sample dataset with missing values
data = {
    'age': [25, np.nan, 35, 28, np.nan, 45, 32],
    'salary': [50000, 60000, np.nan, 55000, 65000, np.nan, 70000], 
    'department': ['IT', 'HR', np.nan, 'IT', 'Finance', 'HR', np.nan],
    'performance': [4.5, np.nan, 4.2, np.nan, 3.8, 4.1, 4.4]
}
df = pd.DataFrame(data)

print("Original data:")
print(df)

# Find missing values
missing = df.isnull()

# Calculate percentage of missing values
missing_percent = (df.isnull().sum() / len(df)) * 100
```

**Missing values can become a problem:** 
- Any ML algorithm by definition tries to extract some meaningful insights from your data/it's patterns/features distributions. 
- Missing values make your data incomplete, which makes it risky to rely on, as it simply can become non-representative

Let's see why missing values are problematic with a simple example
(copy/past this into Google Collab):

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style
sns.set(style="whitegrid")

# Create a complete dataset of 100 people with height and weight
np.random.seed(42)  # For reproducibility

# Create four distinct groups of people to represent diversity
# Group 1: Short and light weight
heights_1 = np.random.normal(160, 5, 25)  # cm
weights_1 = np.random.normal(55, 5, 25)   # kg

# Group 2: Short and heavy weight
heights_2 = np.random.normal(165, 5, 25)  # cm
weights_2 = np.random.normal(85, 8, 25)   # kg

# Group 3: Tall and light weight
heights_3 = np.random.normal(185, 5, 25)  # cm
weights_3 = np.random.normal(70, 5, 25)   # kg

# Group 4: Tall and heavy weight
heights_4 = np.random.normal(190, 5, 25)  # cm
weights_4 = np.random.normal(100, 8, 25)  # kg

# Combine all groups
heights = np.concatenate([heights_1, heights_2, heights_3, heights_4])
weights = np.concatenate([weights_1, weights_2, weights_3, weights_4])

# Create colors to distinguish the groups
groups = np.repeat(['Group 1', 'Group 2', 'Group 3', 'Group 4'], 25)
colors = np.repeat(['blue', 'green', 'orange', 'red'], 25)

# Create the complete dataset
complete_data = pd.DataFrame({
    'height': heights,
    'weight': weights,
    'group': groups,
    'color': colors
})

# Show the effect on trend lines (what an algorithm might learn)
plt.figure(figsize=(10, 6))

# Complete data trend
plt.subplot(1, 2, 1)
for group in complete_data['group'].unique():
    subset = complete_data[complete_data['group'] == group]
    plt.scatter(subset['height'], subset['weight'], label=group, alpha=0.5)

# Add overall trend line
sns.regplot(x='height', y='weight', data=complete_data, scatter=False, 
            line_kws={"color": "black", "lw": 2}, label='True relationship')
plt.title('Complete Data: True Relationship')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.legend()

# Biased data trend
plt.subplot(1, 2, 2)
for group in biased_data['group'].unique():
    subset = biased_data[biased_data['group'] == group]
    valid_subset = subset.dropna()
    plt.scatter(valid_subset['height'], valid_subset['weight'], label=group, alpha=0.5)

# Add biased trend line (calculated only on available data)
valid_data = biased_data.dropna()
sns.regplot(x='height', y='weight', data=valid_data, scatter=False, 
            line_kws={"color": "red", "lw": 2}, label='Biased relationship')
plt.title('Biased Data: Misleading Relationship')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.legend()
plt.tight_layout()
plt.show()
```

### Dropping missing values

- Simple drop is the safest way to eliminate data gaps, because it does not introduce any artificial bias in statistics
	- On the other hand, you lose some portion of potentially useful information as well
	- If the dataset is big enough, dropping even 30% can be acceptable, as long as your data stays representative (think of the example above)

```python
print(df.dropna(subsample = ...,
                thresh = ...))
```


### Imputation

- Imputation means "guessing": we do replace missing values with some likely value we are expecting
	- Thus we want our "guess" to be as much probable as possible
#### Mean imputation 
- Simplest imputing method, which might be good for numeric columns with normal distribution
- When you do impute missing values with some constant value (as in this case) - **you introduce some artificial bias from the real data, driving it to be rather non-representative** 
	- Thus you should be careful with this approach, and do not impute too much data.
	- **It is unrecommended to impute non-normal distribution with this method,** because in such distributions MEAN VALUE IS NOT THE MOST POSSIBLE VALUE (so the "guess" is bad)
```python
print("\nMean imputation for age:")
df['age_mean'] = df['age'].fillna(df['age'].mean())
print(df)
```

#### Median imputation 
- All theses about mean imputation are also valid for median imputation
- The only difference here: median is more suitable for distributions with outliers, because the median value itself is more robust to outliers, than the mean

```python
print("\nMedian imputation for salary:")
df['salary_median'] = df['salary'].fillna(df['salary'].median())
print(df)
```

#### Mode imputation 

- suitable for categorical data

```python
print("\nMode imputation for department:")
df['dept_mode'] = df['department'].fillna(df['department'].mode()[0])
print(df)
```

#### Time series imputation
#### Forward/backward fill 
- Good for time series or ordered data

```python
print("\nForward fill for performance:")
df['perf_ffill'] = df['performance'].bfill()
# or df['perf_ffill'] = df['performance'].ffill()
```

#### Interpolation  
useful for numeric data with clear trends

```python
print("\nLinear interpolation for performance:")
df['perf_interp'] = df['performance'].interpolate(method='linear')
print(df)
```


**Practice Problem: Missing Values Detection**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael', 'Emma'],
    'age': [25, None, 35, 28, None, 45],
    'salary': [50000, 60000, None, 55000, 65000, None],
    'department': ['IT', 'HR', None, 'IT', 'Finance', 'HR'],
    'rating': [4.5, None, 4.2, None, 3.8, 4.1]
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Calculate and display the percentage of missing values in each column.
     - Expected output: A Series showing percentage of NaN values per column
  
  3. Count how many rows have at least one missing value.
     - Expected output: A single number representing rows with any NaN

**Practice Problem: Basic Imputation Strategies**
```python
# Use this DataFrame for practice
data = {
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Michael', 'Emma'],
    'age': [25, None, 35, 28, None, 45],
    'salary': [50000, 60000, None, 55000, 65000, None],
    'department': ['IT', 'HR', None, 'IT', 'Finance', 'HR'],
    'rating': [4.5, None, 4.2, None, 3.8, 4.1]
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Fill missing ages with the mean age.
     - Expected output: A Series with no NaN values, missing ages replaced with mean
  
  2. Fill missing salaries with the median salary.
     - Expected output: A Series with no NaN values, missing salaries replaced with median
  
  3. Fill missing departments with the mode (most common value).
     - Expected output: A Series with no NaN values, missing departments replaced with most frequent department

**Practice Problem: Advanced Imputation Methods**
```python
# Use this DataFrame for practice
data = {
    'date': pd.date_range(start='2023-01-01', periods=6, freq='D'),
    'sales': [100, None, 120, None, None, 150],
    'temperature': [20, None, 22, 25, None, 23],
    'stock_level': [500, None, 400, 350, None, 200]
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Use forward fill to impute missing sales values.
     - Expected output: A Series with no NaN values, missing values filled with previous valid value
  
  2. Use linear interpolation for missing temperature values.
     - Expected output: A Series with no NaN values, missing values interpolated based on surrounding values
  
  3. Use backward fill for missing stock levels.
     - Expected output: A Series with no NaN values, missing values filled with next valid value



# 4. Data Type Issues
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

# 5. Duplicate Detection and Handling
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

**Practice Problem: Customizing Data Profiling Reports**
```python
# Use this DataFrame for practice
data = {
    'age': np.random.normal(35, 10, 1000),
    'salary': np.random.lognormal(10, 0.5, 1000),
    'department': np.random.choice(['IT', 'HR', 'Finance', 'Sales'], 1000),
    'performance': np.random.uniform(1, 5, 1000),
    'join_date': pd.date_range(start='2020-01-01', periods=1000, freq='D')
}
df = pd.DataFrame(data)
```
- **Tasks**:
  1. Create a minimal profile report focusing only on basic statistics.
     - Disable all correlations and interactions
     - Show only basic summary statistics
     - Expected output: A lightweight HTML report
  
  2. Create a report focused on correlation analysis.
     - Enable Spearman and Pearson correlations
     - Set correlation warning threshold to 0.8
     - Include correlation heatmaps
     - Expected output: A report highlighting variable relationships
  
  3. Create a comprehensive report for missing value analysis.
     - Enable all missing value plots
     - Set custom descriptions for each variable
     - Customize the appearance with a different theme
     - Expected output: A detailed report about data completeness

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

# TODO нормальные вопросы