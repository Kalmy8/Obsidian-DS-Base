**Codewords:** Merge, Join, Concatenate, SQL-style Joins, Combining DataFrames

## 1. Concatenating DataFrames
### Basic Concatenation
```python
# Vertical concatenation (adding rows)
df3 = pd.concat([df1, df2])

# Horizontal concatenation (adding columns)
df3 = pd.concat([df1, df2], axis=1)

# Reset index after concatenation
df3 = pd.concat([df1, df2]).reset_index(drop=True)
```

### Advanced Concatenation
```python
# Handling different columns
df3 = pd.concat([df1, df2], join='outer')  # Keep all columns
df3 = pd.concat([df1, df2], join='inner')  # Keep only common columns

# Adding keys to track source
df3 = pd.concat([df1, df2], keys=['source1', 'source2'])

# Ignoring index
df3 = pd.concat([df1, df2], ignore_index=True)

# Append method (alternative syntax)
df3 = df1._append(df2)  # Note: append() is deprecated
```

## 2. Merging DataFrames
### Basic Merges
```python
# Inner join - only keep rows with matching keys in both frames
df3 = pd.merge(df1, df2, on='student_id')

# Outer join - keep all rows from both frames
df3 = pd.merge(df1, df2, on='student_id', how='outer')

# Left join - keep all rows from left frame
df3 = pd.merge(df1, df2, on='student_id', how='left')

# Right join - keep all rows from right frame
df3 = pd.merge(df1, df2, on='student_id', how='right')
```

### Advanced Merges
```python
# Merge on multiple columns
df3 = pd.merge(df1, df2, on=['student_id', 'year'])

# Merge with different column names
df3 = pd.merge(df1, df2, left_on='student_id', right_on='id')

# Merge with index
df3 = pd.merge(df1, df2, left_index=True, right_index=True)

# Merge with mix of columns and index
df3 = pd.merge(df1, df2, left_on='key', right_index=True)

# Controlling which columns appear in the result
df3 = pd.merge(df1[['student_id', 'grade']], df2[['student_id', 'name']], on='student_id')
```

## 3. Join Operations
### Using join()
```python
# Join on index (equivalent to left join)
df3 = df1.join(df2)

# Specify join type
df3 = df1.join(df2, how='inner')
df3 = df1.join(df2, how='outer')
df3 = df1.join(df2, how='right')

# Join with specific columns
df3 = df1.join(df2[['grade', 'attendance']])

# Join with a key column
df3 = df1.set_index('student_id').join(df2.set_index('student_id'))

# Join with different index names
df3 = df1.join(df2, lsuffix='_left', rsuffix='_right')
```

## 4. Handling Duplicate Columns
### Suffixes and Indicators
```python
# Add suffixes to duplicate columns
df3 = pd.merge(df1, df2, on='student_id', suffixes=('_x', '_y'))

# Add indicator column to track source
df3 = pd.merge(df1, df2, on='student_id', indicator=True)
df3[df3['_merge'] == 'left_only']  # Only in left DataFrame
df3[df3['_merge'] == 'right_only']  # Only in right DataFrame
df3[df3['_merge'] == 'both']  # In both DataFrames
```

### Combining Data
```python
# Combine overlapping columns
def combine_grades(row):
    return row['grade_x'] if pd.notnull(row['grade_x']) else row['grade_y']

df3['grade'] = df3.apply(combine_grades, axis=1)

# Coalesce columns using numpy where
import numpy as np
df3['grade'] = np.where(pd.notnull(df3['grade_x']), df3['grade_x'], df3['grade_y'])
```

## 5. Practical Merge Patterns
### Many-to-Many Relationships
```python
# Data with many-to-many relationships
students = pd.DataFrame({
    'student_id': [1, 2, 3],
    'name': ['John', 'Anna', 'Peter']
})

courses = pd.DataFrame({
    'course_id': ['A', 'B', 'C'],
    'course_name': ['Math', 'Physics', 'Chemistry']
})

# Enrollment table (many-to-many relationship)
enrollments = pd.DataFrame({
    'student_id': [1, 1, 2, 2, 3],
    'course_id': ['A', 'B', 'A', 'C', 'B']
})

# Get complete enrollment information
complete = enrollments.merge(students, on='student_id').merge(courses, on='course_id')
```

### Sequential Merges
```python
# Step-by-step merges
# First merge students with grades
students_with_grades = pd.merge(students, grades, on='student_id', how='left')

# Then merge with attendance
complete_data = pd.merge(students_with_grades, attendance, on='student_id', how='left')

# Alternatively, use method chaining
complete_data = (students
                .merge(grades, on='student_id', how='left')
                .merge(attendance, on='student_id', how='left'))
```

### Conditional Joins
```python
# Create a date range condition
df1['date'] = pd.to_datetime(df1['date'])
df2['start_date'] = pd.to_datetime(df2['start_date'])
df2['end_date'] = pd.to_datetime(df2['end_date'])

# Merge with cross join
cross_join = pd.merge(df1, df2, how='cross')

# Apply date range filter after merge
filtered = cross_join[
    (cross_join['date'] >= cross_join['start_date']) & 
    (cross_join['date'] <= cross_join['end_date'])
]
```

#🃏/pandas-basics
**In-conspect Problems:**
1. Given these three DataFrames:
```python
# Students basic info
students_info = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Anna', 'Peter', 'Sarah', 'Mike'],
    'age': [20, 22, 21, 19, 23]
})

# Students grades
students_grades = pd.DataFrame({
    'student_id': [1, 2, 3, 6, 7],
    'math': [85, 92, 78, 90, 85],
    'physics': [90, 88, 75, 92, 80]
})

# Students attendance
students_attendance = pd.DataFrame({
    'student_id': [1, 2, 4, 5, 8],
    'days_present': [42, 45, 40, 38, 41],
    'days_total': [45, 45, 45, 45, 45]
})
```
Tasks:
- Merge the DataFrames to get complete student records
- Find students who have info in all three DataFrames
- Find students who have basic info but no grades or attendance
- Calculate attendance percentage and create a summary DataFrame with student name, age, math grade, physics grade, and attendance percentage
- Identify students who have conflicting records (e.g., in one DataFrame but not others)

2. Working with hierarchical data:
```python
# School A data
school_a_students = pd.DataFrame({
    'student_id': ['A001', 'A002', 'A003', 'A004'],
    'name': ['John', 'Anna', 'Peter', 'Sarah'],
    'grade': [85, 92, 78, 95]
})

# School B data
school_b_students = pd.DataFrame({
    'student_id': ['B001', 'B002', 'B003', 'B004'],
    'name': ['Mike', 'Emma', 'David', 'Linda'],
    'grade': [88, 84, 90, 86]
})

# District data
district_info = pd.DataFrame({
    'school_id': ['A', 'B'],
    'school_name': ['North High', 'South High'],
    'location': ['Downtown', 'Suburb']
})
```
Tasks:
- Combine all student data into a single DataFrame while preserving school information
- Add a prefix to student_id to indicate the school (if not already present)
- Create a complete district report with student information and school details
- Find the average grade by school
- Create a hierarchical index with school and student information

3. Time-series data merging:
```python
# Product A sales by month
product_a = pd.DataFrame({
    'month': pd.date_range('2023-01-01', periods=6, freq='M'),
    'sales_A': [100, 120, 110, 130, 150, 140]
})

# Product B sales by month
product_b = pd.DataFrame({
    'month': pd.date_range('2023-03-01', periods=6, freq='M'),
    'sales_B': [90, 100, 120, 110, 130, 125]
})

# Marketing expenses by month
marketing = pd.DataFrame({
    'month': pd.date_range('2023-02-01', periods=8, freq='M'),
    'expenses': [50, 60, 70, 65, 75, 80, 70, 60]
})
```
Tasks:
- Merge the sales and marketing data by month
- Create a complete timeline with all months, filling missing values with appropriate methods
- Calculate the total sales (A + B) for months where both products have data
- Calculate the ratio of sales to marketing expenses for each month
- Create a visualization-ready DataFrame with month as index and columns for each product's sales and marketing expenses

4. Advanced relationship modeling:
```python
# Authors
authors = pd.DataFrame({
    'author_id': [1, 2, 3, 4, 5],
    'author_name': ['John Smith', 'Emily Jones', 'David Brown', 'Sarah Wilson', 'Michael Taylor']
})

# Books
books = pd.DataFrame({
    'book_id': [101, 102, 103, 104, 105, 106],
    'title': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E', 'Book F'],
    'genre': ['Fiction', 'Science', 'Fiction', 'Biography', 'Science', 'History']
})

# Authorship (mapping authors to books, including co-authorship)
authorship = pd.DataFrame({
    'author_id': [1, 2, 2, 3, 4, 4, 5, 5],
    'book_id': [101, 101, 102, 103, 104, 105, 105, 106]
})

# Book sales
sales = pd.DataFrame({
    'book_id': [101, 102, 103, 104, 105, 106],
    'copies_sold': [5000, 7500, 3000, 8000, 6000, 4500],
    'revenue': [50000, 90000, 30000, 120000, 72000, 54000]
})
```
Tasks:
- Create a complete book catalog with titles, authors, genres, and sales information
- Handle co-authorship by creating a proper relationship between authors and books
- Calculate each author's total sales and revenue
- Find the most successful author-genre combination
- Create a summary showing each author's books, sales, and revenue share (for co-authored books, split revenue proportionally)

**Review Questions:**
1. What are the main differences between `concat()` and `merge()` in pandas?
2. Explain the different join types (inner, outer, left, right) and when you would use each one.
3. How do you handle duplicate columns when merging DataFrames?
4. What is the purpose of the `indicator` parameter in `merge()`?
5. What are some common issues that can arise when merging DataFrames, and how can you prevent them?
6. How do you perform a many-to-many merge in pandas?
7. When would you use `join()` instead of `merge()`?
8. How can you track the source of data when concatenating multiple DataFrames? 