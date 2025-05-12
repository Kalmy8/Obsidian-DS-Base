**Codewords:** Time Series, Visualization, Memory Optimization, String Methods, Categorical Data

## 1. Time Series Data
### Working with Dates and Times
```python
# Creating datetime objects
import pandas as pd
from datetime import datetime

# Create a series of dates
dates = pd.date_range(start='2023-01-01', end='2023-01-31', freq='D')
dates = pd.date_range(start='2023-01-01', periods=31, freq='D')

# Create a DataFrame with date index
df = pd.DataFrame({'value': range(31)}, index=dates)

# Convert string columns to datetime
df['date_col'] = pd.to_datetime(df['string_date_col'])
df['date_col'] = pd.to_datetime(df['string_date_col'], format='%Y-%m-%d')
df['date_col'] = pd.to_datetime(df['string_date_col'], errors='coerce')  # Invalid dates become NaT
```

### Date Components and Properties
```python
# Access date components
df['year'] = df['date_col'].dt.year
df['month'] = df['date_col'].dt.month
df['day'] = df['date_col'].dt.day
df['weekday'] = df['date_col'].dt.weekday  # 0 = Monday, 6 = Sunday
df['day_name'] = df['date_col'].dt.day_name()

# Date properties
df['is_weekend'] = df['date_col'].dt.weekday >= 5
df['quarter'] = df['date_col'].dt.quarter
df['is_month_end'] = df['date_col'].dt.is_month_end
```

### Resampling Time Series
```python
# Set a datetime index
df.set_index('date_col', inplace=True)

# Downsample to monthly frequency
monthly_mean = df.resample('M').mean()
monthly_sum = df.resample('M').sum()

# Upsample to daily frequency (with fill method)
daily = monthly_mean.resample('D').ffill()  # Forward fill
daily = monthly_mean.resample('D').bfill()  # Backward fill
daily = monthly_mean.resample('D').interpolate()  # Interpolation

# Common frequencies
# 'D': calendar day
# 'B': business day
# 'W': weekly (default Sunday)
# 'M': month end
# 'Q': quarter end
# 'A': year end
# 'H': hourly
# 'T' or 'min': minute
# 'S': second
```

### Shifting and Lagging
```python
# Shift data (time lag)
df['previous_day'] = df['value'].shift(1)  # Shift 1 day back
df['next_day'] = df['value'].shift(-1)  # Shift 1 day forward

# Calculate differences
df['daily_change'] = df['value'].diff()  # Current value - previous value
df['pct_change'] = df['value'].pct_change()  # Percentage change

# Rolling calculations with time-based windows
df['7d_avg'] = df['value'].rolling('7D').mean()  # 7-day rolling average
df['30d_std'] = df['value'].rolling('30D').std()  # 30-day rolling standard deviation
```

## 2. Pandas Visualization
### Basic Plotting
```python
# Plot a Series
s = pd.Series(range(10))
s.plot()

# Plot a DataFrame
df = pd.DataFrame({
    'A': range(10),
    'B': [x*2 for x in range(10)],
    'C': [x**2 for x in range(10)]
})
df.plot()

# Common plot types
df.plot(kind='line')
df.plot(kind='bar')
df.plot(kind='barh')
df.plot(kind='hist')
df.plot(kind='box')
df.plot(kind='area')
df.plot(kind='scatter', x='A', y='B')
df.plot(kind='pie', y='A')
```

### Customizing Plots
```python
# Plot customization
df.plot(
    figsize=(10, 6),
    title='My Plot',
    grid=True,
    legend=True,
    alpha=0.7,
    color=['r', 'g', 'b'],
    style=['-', '--', ':']
)

# Multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
df['A'].plot(ax=axes[0, 0], title='A')
df['B'].plot(ax=axes[0, 1], title='B')
df['C'].plot(ax=axes[1, 0], title='C')
(df['A'] / df['B']).plot(ax=axes[1, 1], title='A/B')

# Save figure
plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
```

### Statistical Visualizations
```python
# Distribution visualization
df['A'].plot(kind='hist', bins=20)
df.plot(kind='box')
df.plot(kind='density')

# Correlation visualization
correlation = df.corr()
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm')

# Grouped bar chart
grouped = df.groupby('category').mean()
grouped.plot(kind='bar')
```

## 5. Categorical Data
### Creating and Using Categories
```python
# Convert to categorical
df['category_col'] = df['category_col'].astype('category')

# Create with ordered categories
df['size'] = pd.Categorical(
    df['size'],
    categories=['small', 'medium', 'large'],
    ordered=True
)

# Working with categories
print(df['category_col'].cat.categories)  # Get categories
print(df['category_col'].cat.codes)  # Get underlying codes

# Modify categories
df['category_col'] = df['category_col'].cat.add_categories(['new_category'])
df['category_col'] = df['category_col'].cat.remove_categories(['old_category'])
df['category_col'] = df['category_col'].cat.rename_categories({'old': 'new'})
df['category_col'] = df['category_col'].cat.reorder_categories(['c', 'b', 'a'], ordered=True)
```

### Memory Benefits
```python
# Check memory usage before
before = df['text_col'].memory_usage(deep=True)

# Convert to category
df['text_col'] = df['text_col'].astype('category')

# Check memory usage after
after = df['text_col'].memory_usage(deep=True)
print(f"Memory reduction: {(1 - after/before)*100:.2f}%")
```

#🃏/pandas-basics
**In-conspect Problems:**
1. Time Series Analysis:
```python
# Stock price data
import pandas as pd
import numpy as np

# Create date range
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='B')  # Business days

# Create stock price data
np.random.seed(42)
stock_data = pd.DataFrame({
    'price': 100 + np.cumsum(np.random.normal(0, 1, len(dates)))
}, index=dates)

# Add some missing days
stock_data = stock_data.drop(stock_data.index[10:20])
stock_data = stock_data.drop(stock_data.index[150:155])
```
Tasks:
- Calculate daily returns and annualized volatility
- Fill in missing dates using appropriate methods
- Create monthly and quarterly summaries of the stock performance
- Calculate a 10-day and 30-day moving average
- Compare the performance in different quarters and months
- Create a visualization showing the stock price, moving averages, and highlighting the best and worst months

2. Data Visualization Challenge:
```python
# Sales data by region and product
data = {
    'region': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East', 'East', 'West', 'West', 'West'],
    'product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'sales': [100, 120, 90, 80, 95, 110, 120, 140, 100, 90, 110, 105],
    'profit': [20, 25, 15, 15, 20, 22, 25, 30, 18, 18, 22, 21],
    'year': [2021, 2021, 2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022, 2022, 2022]
}
df = pd.DataFrame(data)
```
Tasks:
- Create a bar chart showing sales by region
- Create a grouped bar chart comparing sales for different products within each region
- Create a scatter plot of sales vs. profit with different colors for each region
- Create a heatmap showing the correlation between numerical variables
- Create a pie chart showing the proportion of sales by product
- Create a composite visualization with multiple subplots showing different aspects of the data

3. Memory Optimization:
```python
# Function to create a large dummy dataset
def create_large_df(rows=1000000, cols=10):
    import numpy as np
    import pandas as pd
    import string
    
    # Create a large DataFrame
    data = {}
    
    # Numeric columns
    for i in range(5):
        data[f'int_col_{i}'] = np.random.randint(0, 1000, rows)
        data[f'float_col_{i}'] = np.random.normal(100, 25, rows)
    
    # Categorical columns with repeating values
    categories = ['cat_' + c for c in string.ascii_lowercase[:10]]
    for i in range(3):
        data[f'cat_col_{i}'] = np.random.choice(categories, rows)
    
    # Date column
    data['date_col'] = pd.date_range(start='2020-01-01', periods=rows, freq='s')
    
    # Text column
    phrases = [
        'Lorem ipsum dolor sit amet',
        'consectetur adipiscing elit',
        'sed do eiusmod tempor incididunt',
        'ut labore et dolore magna aliqua',
        'Ut enim ad minim veniam'
    ]
    data['text_col'] = np.random.choice(phrases, rows)
    
    return pd.DataFrame(data)

# Create a sample DataFrame
large_df = create_large_df(100000)  # 100,000 rows
```
Tasks:
- Analyze the memory usage of the dataset by column and data type
- Apply type conversion strategies to reduce memory usage 
- Convert appropriate columns to categorical type
- Design a function that automatically optimizes a DataFrame's memory usage
- Compare the performance (speed) of the original vs. optimized DataFrames for common operations
- Create a visualization showing memory usage before and after optimization

4. Text Data Processing:
```python
# Product reviews data
import pandas as pd

data = {
    'product_id': ['A001', 'A001', 'A002', 'A002', 'A003', 'A003', 'A004', 'A004'],
    'rating': [4, 5, 2, 1, 5, 4, 3, 4],
    'review_text': [
        "This product is great and works as expected.",
        "Love this! Best purchase I've made in 2023.",
        "Disappointed with the quality, broke after 2 weeks of use.",
        "Terrible product, doesn't work at all. Waste of money.",
        "Excellent product, highly recommend for all users.",
        "Very good performance and easy to use interface.",
        "Average product, nothing special but gets the job done.",
        "Good value for money, happy with my purchase."
    ]
}
reviews = pd.DataFrame(data)
```
Tasks:
- Extract word counts from each review
- Identify common positive and negative words
- Categorize reviews as positive (4-5), neutral (3), or negative (1-2)
- Create a function to check if reviews contain specific keywords
- Calculate the average rating when specific words appear in reviews
- Visualize the relationship between review length and rating
- Create a summary of top positive and negative phrases for each product

**Review Questions:**
1. What are the differences between `pd.date_range()`, `pd.to_datetime()`, and `pd.Timestamp()`?
2. How can you resample time series data, and what options do you have for filling missing values?
3. What are the advantages of converting string columns to categorical type?
4. How would you identify columns that could benefit from memory optimization?
5. What are the key differences between pandas' built-in plotting functions and using matplotlib directly?
6. How can you handle very large datasets that don't fit in memory?
7. What string methods are most useful when cleaning and processing text data in pandas?
8. When working with time series data, how do you calculate period-over-period changes? 